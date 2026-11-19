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
                                  flat_forecast, dfols_forecast, nested_cv_mse, pilot_test_mse, dicker_noise,
                                  wei_exponent)
from ..training.learning_curves import split_task, truth_curve, TRUTH_GRID


def task_seed(name):
    return int(hashlib.sha256(name.encode()).hexdigest()[:8], 16) % (2 ** 31)


def _bands_from_boot(boot):
    q = np.quantile(boot, [0.025, 0.1, 0.9, 0.975], axis=0)
    return {0.95: (q[0], q[3]), 0.8: (q[1], q[2])}


SMALL_N = 1000          # tasks with fewer samples are evaluated over repeated outer splits
N_SPLITS_SMALL = 10


def n_splits_for(task):
    return N_SPLITS_SMALL if len(task.y) < SMALL_N else 1


def _sfx(task, split):
    return task.name.replace(":", "__") + ("" if split == 0 else f"__s{split}")


def run_truth(task, out_dir, with_pls=True, grid=TRUTH_GRID, force=False, split=0):
    path = os.path.join(out_dir, f"truth_{_sfx(task, split)}.npz")
    if os.path.exists(path) and not force:
        z = np.load(path, allow_pickle=True)
        return {k: z[k] for k in z.files}
    seed = task_seed(task.name) + 7919 * split
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
               ridge_mse_reps=tc["ridge_mse_reps"], mus=tc["mus"], lam=lam, path_full=path_full,
               full_fits=json.dumps(full_fits), var_test=float(np.var(task.y[test])),
               var_pool=float(np.var(task.y[pool])), seconds=time.time() - t0, reps=np.array(tc["reps"]), split=split)
    np.savez_compressed(path, **res)
    return {k: (np.array(v) if not isinstance(v, np.ndarray) else v) for k, v in res.items()}


def run_pilots(task, truth, out_dir, n0_list=(25, 50, 100, 200), n_pilots=20, n_boot=50,
               ablation_n0=(50, 100), ablation_pilots=10, force=False, tag="main", extra_rpm=None, split=0,
               diagnostics=True):
    """All forecasters on identical random pilots. Rows are written for every truth size n >= n0, including
    n = n0 itself (ratio 1, used for the level/gain decomposition; forecasting metrics use ratio >= 2)."""
    path = os.path.join(out_dir, f"forecasts_{tag}_{_sfx(task, split)}.csv")
    if os.path.exists(path) and not force:
        return pd.read_csv(path)
    X, y, g = task.X, task.y, task.groups
    pool, test = truth["pool"], truth["test"]
    tn = np.array(truth["n"]); tr = np.array(truth["ridge_mse"]); tp = np.array(truth["pls_mse"]) if len(truth["pls_mse"]) else None
    tor = np.min(np.array(truth["ridge_mu_mse"]), axis=1)            # oracle-tuned truth (best fixed penalty)
    lam_pool = truth["lam"]
    mu_grid = DEFAULT_MU_REL * lam_pool.max()
    var_pool = float(truth["var_pool"]) if "var_pool" in truth else float(np.var(y[pool]))
    # pool covariance (unlabelled spectra) for the noise-variance estimator
    mean_pool = X[pool].mean(0)
    _, Sp, Vtp = np.linalg.svd(X[pool] - mean_pool, full_matrices=False)
    lam_vec = Sp ** 2 / (len(pool) - 1)
    rows = []
    base_seed = task_seed(task.name) + 7919 * split
    Xu_extra = task.X_unlabeled_extra
    if Xu_extra is not None and getattr(task, "X_unlabeled_groups", None) is not None:
        Xu_extra = Xu_extra[~np.isin(task.X_unlabeled_groups, np.unique(g[test]))]   # no spectra from test-set sites
    for n0 in n0_list:
        if n0 * 2 > tn.max() or n0 >= len(pool) // 2:
            continue
        sel = tn >= n0
        horizons = tn[sel]
        tr_h = tr[sel]; tor_h = tor[sel]; tp_h = tp[sel] if tp is not None else np.full(len(horizons), np.nan)
        for s in range(n_pilots):
            rng = np.random.default_rng(base_seed + 1000 * n0 + s)
            pil = rng.choice(pool, n0, replace=False)
            X0, y0, g0 = X[pil], y[pil], g[pil]
            res = {}
            t_rpm_point = t_rpm_boot = np.nan
            if tag == "main":
                # ---- RPM (unlabelled pool spectra for the eigen-spectrum)
                fr = RPMForecaster(n_boot=n_boot, seed=base_seed + s)
                f = fr.fit_forecast(X0, y0, g0, lam_pool, horizons)
                res["RPM"] = (f["point"], _bands_from_boot(f["boot_logrmse"]) if n_boot else None, f["params"])
                t_rpm_point, t_rpm_boot = fr.t_point_, fr.t_boot_
                path0 = f["path"]
                # the originally registered implementation (every mu-grid point weighted equally), point forecast only
                gsz0 = float(np.mean(np.unique(g0, return_counts=True)[1]))
                pv1 = fit_rpm(lam_pool, path0, n0 - gsz0, DEFAULT_MU_REL, kappa_weights=False)
                res["RPM-v1"] = (forecast_theory(lam_pool, pv1, horizons), None, pv1)
            else:
                path0 = ridge_cv_path(X0, y0, mu_grid, groups=g0)
            for nm, kw in (extra_rpm or []):
                kw = dict(kw)
                if kw.pop("dicker_floor", False):
                    sg, _ = dicker_noise(X0, y0, mean_pool, lam_vec, Vtp.T)
                    kw["sigma2_floor"] = sg if sg > 0 else None
                nb = kw.pop("n_boot", n_boot)
                fx = RPMForecaster(n_boot=nb, seed=base_seed + s, **kw).fit_forecast(X0, y0, g0, lam_pool, horizons)
                res[nm] = (fx["point"], _bands_from_boot(fx["boot_logrmse"]) if nb else None, fx["params"])
            pilot_cv = float(np.min(path0))
            diag = {}
            if diagnostics:
                diag["pilot_nested_logrmse"] = 0.5 * float(np.log(nested_cv_mse(X0, y0, g0, mu_grid, seed=base_seed + s)))
                diag["pilot_test_logrmse"] = 0.5 * float(np.log(pilot_test_mse(X0, y0, g0, mu_grid, X[test], y[test])))
                sg, tg = dicker_noise(X0, y0, mean_pool, lam_vec, Vtp.T)
                diag["dicker_sigma2_frac"] = sg / var_pool; diag["dicker_tau2_frac"] = tg / var_pool
                wz = wei_exponent(X0, y0, lam_pool, mu_grid)
                diag["wei_alpha"], diag["wei_gamma"], diag["wei_delta"] = wz["alpha"], wz["gamma"], wz["delta"]
            if tag == "main":
                # ---- empirical learning-curve extrapolation family
                t1 = time.perf_counter()
                ms, es = pilot_subsample_curve(X0, y0, g0, mu_grid, seed=base_seed + s)
                for kind in ("IPL3", "IPL2", "EXP3", "LOG2"):
                    cf = curve_forecast(kind, ms, es, horizons)
                    res[kind] = (cf["point"], cf["bands"], {"failed": cf["failed"], "floored": cf["floored"]})
                t_curve = time.perf_counter() - t1
                res["FLAT"] = (np.full(len(horizons), pilot_cv), None, {})
                res["DFOLS"] = (dfols_forecast(X0, y0, g0, mu_grid, horizons), None, {})
                # Wei et al. (2022) scaling exponent, anchored at the pilot CV error (noiseless rate; alpha clipped to [0, 2])
                if diagnostics and np.isfinite(diag["wei_alpha"]):
                    a = float(np.clip(diag["wei_alpha"], 0.0, 2.0))
                    res["WEI"] = (pilot_cv * (horizons / n0) ** (-a), None, {"clipped": bool(a != diag["wei_alpha"])})
                else:
                    res["WEI"] = (np.full(len(horizons), pilot_cv), None, {"clipped": True})
            # ---- ablations (subset of pilots / pilot sizes)
            if tag == "main" and n0 in ablation_n0 and s < ablation_pilots:
                gsz = float(np.mean(np.unique(g0, return_counts=True)[1])); n_eff = n0 - gsz
                e = path0
                for nm, kw in (("RPM-rfree", {"r_mode": "free"}), ("RPM-cut0.5", {"cutoff": 0.5}),
                               ("RPM-cut0.95", {"cutoff": 0.95})):
                    p = fit_rpm(lam_pool, e, n_eff, DEFAULT_MU_REL, **kw)
                    res[nm] = (forecast_theory(lam_pool, p, horizons), None, p)
                lam_p = eigen_spectrum(X0)
                ep = ridge_cv_path(X0, y0, DEFAULT_MU_REL * lam_p.max(), groups=g0)
                p = fit_rpm(lam_p, ep, n_eff, DEFAULT_MU_REL)
                res["RPM-pilotcov"] = (forecast_theory(lam_p, p, horizons), None, p)
                lam_t = complete_tail_powerlaw(lam_p, X.shape[1])
                ept = ridge_cv_path(X0, y0, DEFAULT_MU_REL * lam_t.max(), groups=g0)
                p = fit_rpm(lam_t, ept, n_eff, DEFAULT_MU_REL)
                res["RPM-pilotcov+tail"] = (forecast_theory(lam_t, p, horizons), None, p)
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
                fk = RPMForecaster(n_boot=0, cv="kfold10", seed=base_seed + s).fit_forecast(X0, y0, g0, lam_pool, horizons)
                res["RPM-kfold10"] = (fk["point"], None, fk["params"])
                Xc = X[pool] - X[pool].mean(0)
                _, Sv, Vt = np.linalg.svd(Xc, full_matrices=False)
                lam_v = Sv ** 2 / (len(pool) - 1); keep = lam_v > 1e-14 * lam_v[0]
                p = fit_ml2((lam_v[keep], Vt[keep].T), X0, y0, lam_v[keep])
                res["RPM-ML2"] = (forecast_theory(lam_v[keep], p, horizons), None, p)
            for meth, (pt, bands, params) in res.items():
                lp = np.log(np.sqrt(np.maximum(pt, 1e-300)))
                fl = params.get("floored") if isinstance(params, dict) else None
                for i, n in enumerate(horizons):
                    row = {"task": task.name, "family": task.family, "split": split, "n0": n0, "pilot": s, "method": meth,
                           "n": int(n), "ratio": float(n / n0), "fc_logrmse": float(lp[i]),
                           "truth_ridge_logrmse": float(np.log(np.sqrt(tr_h[i]))),
                           "truth_oracle_logrmse": float(np.log(np.sqrt(tor_h[i]))),
                           "truth_pls_logrmse": float(np.log(np.sqrt(tp_h[i]))) if np.isfinite(tp_h[i]) else np.nan,
                           "pilot_cv_logrmse": float(np.log(np.sqrt(pilot_cv)))}
                    row.update(diag)
                    if fl is not None:
                        row["floored"] = bool(fl[i])
                    if bands is not None:
                        for a, (lo, hi) in bands.items():
                            row[f"lo{int(a*100)}"] = float(lo[i]); row[f"hi{int(a*100)}"] = float(hi[i])
                    if meth.startswith("RPM") and isinstance(params, dict) and "log_tau2" in params:
                        row["log_sigma2"] = params["log_sigma2"]; row["log_tau2"] = params["log_tau2"]; row["r"] = params["r"]
                    rows.append(row)
            trow = {"task": task.name, "family": task.family, "split": split, "n0": n0, "pilot": s, "method": "_timing",
                    "n": -1, "t_rpm_point_sec": t_rpm_point, "t_rpm_boot_sec": t_rpm_boot}
            if tag == "main":
                trow["t_curve_sec"] = t_curve
            rows.append(trow)
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return df
