"""Forecasting experiment for one task: ground truth, pilots, all forecasters."""
from __future__ import annotations

import hashlib
import json
import os
import time

import numpy as np
import pandas as pd

from ..models.theory import DEFAULT_MU_REL
from ..models.ridge import ridge_cv_path
from ..models.forecasters import (RPMForecaster, eigen_spectrum, complete_tail_powerlaw, fit_rpm,
                                  forecast_theory, fit_ml2, pilot_subsample_curve, curve_forecast,
                                  flat_forecast, dfols_forecast)
from ..training.learning_curves import split_task, truth_curve, TRUTH_GRID


def task_seed(name):
    return int(hashlib.sha256(name.encode()).hexdigest()[:8], 16) % (2 ** 31)


def _bands_from_boot(boot):
    q = np.quantile(boot, [0.025, 0.1, 0.9, 0.975], axis=0)
    return {0.95: (q[0], q[3]), 0.8: (q[1], q[2])}


def run_truth(task, out_dir, with_pls=True, grid=TRUTH_GRID, force=False):
    path = os.path.join(out_dir, f"truth_{task.name.replace(':', '__')}.npz")
    if os.path.exists(path) and not force:
        z = np.load(path, allow_pickle=True)
        return {k: z[k] for k in z.files}
    seed = task_seed(task.name)
    pool, test = split_task(task.groups, seed)
    t0 = time.time()
    tc = truth_curve(task.X, task.y, task.groups, pool, test, grid, seed + 1, with_pls=with_pls)
    # large-sample reference fit on the full pool path (interpolation check of the theory, RQ1)
    lam = eigen_spectrum(task.X[pool])
    gsz = float(np.mean(np.unique(task.groups[pool], return_counts=True)[1]))
    path_full = ridge_cv_path(task.X[pool], task.y[pool], DEFAULT_MU_REL * lam.max(), groups=task.groups[pool])
    full_fits = {}
    for mode in ("fixed1", "free"):
        p = fit_rpm(lam, path_full, len(pool) - gsz, DEFAULT_MU_REL, r_mode=mode)
        full_fits[mode] = p
    res = dict(pool=pool, test=test, n=np.array(tc["n"]), ridge_mse=np.array(tc["ridge_mse"]),
               ridge_se=np.array(tc["ridge_se"]), pls_mse=np.array(tc["pls_mse"]) if with_pls else np.array([]),
               pls_se=np.array(tc["pls_se"]) if with_pls else np.array([]), ridge_mu_mse=tc["ridge_mu_mse"],
               mus=tc["mus"], lam=lam, path_full=path_full, full_fits=json.dumps(full_fits),
               var_test=float(np.var(task.y[test])), seconds=time.time() - t0, reps=np.array(tc["reps"]))
    np.savez_compressed(path, **res)
    return {k: (np.array(v) if not isinstance(v, np.ndarray) else v) for k, v in res.items()}


def run_pilots(task, truth, out_dir, n0_list=(25, 50, 100, 200), n_pilots=20, n_boot=50,
               ablation_n0=(50, 100), ablation_pilots=10, force=False, tag="main", extra_rpm=None):
    path = os.path.join(out_dir, f"forecasts_{tag}_{task.name.replace(':', '__')}.csv")
    if os.path.exists(path) and not force:
        return pd.read_csv(path)
    X, y, g = task.X, task.y, task.groups
    pool, test = truth["pool"], truth["test"]
    tn = np.array(truth["n"]); tr = np.array(truth["ridge_mse"]); tp = np.array(truth["pls_mse"]) if len(truth["pls_mse"]) else None
    lam_pool = truth["lam"]
    mu_grid = DEFAULT_MU_REL * lam_pool.max()
    rows = []
    base_seed = task_seed(task.name)
    Xu_extra = task.X_unlabeled_extra
    for n0 in n0_list:
        if n0 * 2 > tn.max() or n0 >= len(pool) // 2:
            continue
        horizons = tn[tn >= 2 * n0]
        tr_h = tr[tn >= 2 * n0]; tp_h = tp[tn >= 2 * n0] if tp is not None else np.full(len(horizons), np.nan)
        for s in range(n_pilots):
            rng = np.random.default_rng(base_seed + 1000 * n0 + s)
            pil = rng.choice(pool, n0, replace=False)
            X0, y0, g0 = X[pil], y[pil], g[pil]
            t_start = time.time()
            res = {}
            # ---- proposed RPM (unlabelled pool spectra for the eigen-spectrum)
            f = RPMForecaster(n_boot=n_boot, seed=base_seed + s).fit_forecast(X0, y0, g0, lam_pool, horizons)
            res["RPM"] = (f["point"], _bands_from_boot(f["boot_logrmse"]), f["params"])
            t_rpm = time.time() - t_start
            for nm, kw in (extra_rpm or []):
                fx = RPMForecaster(n_boot=n_boot, seed=base_seed + s, **kw).fit_forecast(X0, y0, g0, lam_pool, horizons)
                res[nm] = (fx["point"], _bands_from_boot(fx["boot_logrmse"]), fx["params"])
            pilot_cv = float(np.min(f["path"]))
            # ---- empirical learning-curve extrapolation family
            t1 = time.time()
            ms, es = pilot_subsample_curve(X0, y0, g0, mu_grid, seed=base_seed + s)
            t_curve = time.time() - t1
            for kind in ("IPL3", "IPL2", "EXP3", "LOG2"):
                cf = curve_forecast(kind, ms, es, horizons)
                res[kind] = (cf["point"], cf["bands"], {"failed": cf["failed"]})
            res["FLAT"] = (np.full(len(horizons), pilot_cv), None, {})
            res["DFOLS"] = (dfols_forecast(X0, y0, g0, mu_grid, horizons), None, {})
            # ---- ablations (subset of pilots / pilot sizes)
            if n0 in ablation_n0 and s < ablation_pilots:
                gsz = float(np.mean(np.unique(g0, return_counts=True)[1])); n_eff = n0 - gsz
                e = f["path"]
                for nm, kw in (("RPM-rfree", {"r_mode": "free"}), ("RPM-cut0.5", {"cutoff": 0.5}),
                               ("RPM-cut0.95", {"cutoff": 0.95})):
                    p = fit_rpm(lam_pool, e, n_eff, DEFAULT_MU_REL, **kw)
                    res[nm] = (forecast_theory(lam_pool, p, horizons), None, p)
                # pilot-only covariance (no unlabelled spectra), with and without power-law tail completion
                lam_p = eigen_spectrum(X0)
                ep = ridge_cv_path(X0, y0, DEFAULT_MU_REL * lam_p.max(), groups=g0)
                p = fit_rpm(lam_p, ep, n_eff, DEFAULT_MU_REL)
                res["RPM-pilotcov"] = (forecast_theory(lam_p, p, horizons), None, p)
                lam_t = complete_tail_powerlaw(lam_p, X.shape[1])
                ept = ridge_cv_path(X0, y0, DEFAULT_MU_REL * lam_t.max(), groups=g0)
                p = fit_rpm(lam_t, ept, n_eff, DEFAULT_MU_REL)
                res["RPM-pilotcov+tail"] = (forecast_theory(lam_t, p, horizons), None, p)
                # small unlabelled set (250 spectra incl. pilot)
                others = np.setdiff1d(pool, pil)
                u_idx = np.concatenate([pil, rng.choice(others, min(250 - n0, len(others)), replace=False)]) if n0 < 250 else pil
                lam_u = eigen_spectrum(X[u_idx])
                eu = ridge_cv_path(X0, y0, DEFAULT_MU_REL * lam_u.max(), groups=g0)
                p = fit_rpm(lam_u, eu, n_eff, DEFAULT_MU_REL)
                res["RPM-U250"] = (forecast_theory(lam_u, p, horizons), None, p)
                if Xu_extra is not None and len(Xu_extra) > 500:
                    lam_x = eigen_spectrum(np.vstack([X[pool], Xu_extra]))
                    ex = ridge_cv_path(X0, y0, DEFAULT_MU_REL * lam_x.max(), groups=g0)
                    p = fit_rpm(lam_x, ex, n_eff, DEFAULT_MU_REL)
                    res["RPM-Uextra"] = (forecast_theory(lam_x, p, horizons), None, p)
                # 10-fold path instead of exact LOGO
                fk = RPMForecaster(n_boot=0, cv="kfold10", seed=base_seed + s).fit_forecast(X0, y0, g0, lam_pool, horizons)
                res["RPM-kfold10"] = (fk["point"], None, fk["params"])
                # type-II maximum likelihood instead of path matching
                Xc = X[pool] - X[pool].mean(0)
                _, Sv, Vt = np.linalg.svd(Xc, full_matrices=False)
                lam_v = Sv ** 2 / (len(pool) - 1); keep = lam_v > 1e-14 * lam_v[0]
                p = fit_ml2((lam_v[keep], Vt[keep].T), X0, y0, lam_v[keep])
                res["RPM-ML2"] = (forecast_theory(lam_v[keep], p, horizons), None, p)
            for meth, (pt, bands, params) in res.items():
                lp = np.log(np.sqrt(np.maximum(pt, 1e-300)))
                for i, n in enumerate(horizons):
                    row = {"task": task.name, "family": task.family, "n0": n0, "pilot": s, "method": meth,
                           "n": int(n), "ratio": float(n / n0), "fc_logrmse": float(lp[i]),
                           "truth_ridge_logrmse": float(np.log(np.sqrt(tr_h[i]))),
                           "truth_pls_logrmse": float(np.log(np.sqrt(tp_h[i]))) if np.isfinite(tp_h[i]) else np.nan,
                           "pilot_cv_logrmse": float(np.log(np.sqrt(pilot_cv)))}
                    if bands is not None:
                        for a, (lo, hi) in bands.items():
                            row[f"lo{int(a*100)}"] = float(lo[i]); row[f"hi{int(a*100)}"] = float(hi[i])
                    if meth.startswith("RPM") and isinstance(params, dict) and "log_tau2" in params:
                        row["log_sigma2"] = params["log_sigma2"]; row["log_tau2"] = params["log_tau2"]; row["r"] = params["r"]
                    rows.append(row)
            rows.append({"task": task.name, "family": task.family, "n0": n0, "pilot": s, "method": "_timing",
                         "n": -1, "t_rpm_sec": t_rpm, "t_curve_sec": t_curve})
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return df
