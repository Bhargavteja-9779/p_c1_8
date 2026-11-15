"""Phase-19 refinement: inverse-variance-weighted regularisation-path matching (RPM-w).

Motivation (documented in EXPERIMENT_LOG.md): in the E0 simulation with p > n0, the leave-one-out
errors at weakly regularised path points are heavy-tailed; an unweighted log-space fit is pulled
toward a pilot's low values, giving optimistic forecasts. RPM-w weights every path point by the
inverse of the delta-method variance of log CV-MSE estimated from the pilot's own CV residuals.
It is evaluated on exactly the same pilots as the main run (identical seeds) so comparisons are paired.
"""
from __future__ import annotations

import os
import time

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task, TASKS_FULL, TASKS_QUICK
from src.models.forecasters import RPMForecaster
from src.evaluation.forecast_experiment import run_truth, task_seed


def source_of(task_name):
    lib = task_name.split(":")[0]
    for pre in ("ICRAF", "KSSL", "AfSIS1", "Neospectra", "Mango", "Diesel", "Tablets", "Tecator", "CGL"):
        if lib.startswith(pre):
            return pre
    return lib


def alignment_table(raw_out):
    """Large-sample alignment exponent r (path fit on the full calibration pool, r free) for every task."""
    import glob, json
    rows = []
    for f in sorted(glob.glob(os.path.join(raw_out, "truth_*.npz"))):
        z = np.load(f, allow_pickle=True)
        name = os.path.basename(f)[6:-4].replace("__", ":")
        fit = json.loads(str(z["full_fits"]))["free"]
        rows.append({"task": name, "source": source_of(name), "r_full_pool": fit["r"],
                     "noise_frac_full_pool": float(np.exp(fit["log_sigma2"]) / z["var_test"]), "n_pool": len(z["pool"])})
    t = pd.DataFrame(rows)
    t["r_loso_prior"] = [float(t[t.source != s].r_full_pool.median()) for s in t.source]
    return t


def _bands(boot):
    q = np.quantile(boot, [0.025, 0.1, 0.9, 0.975], axis=0)
    return {95: (q[0], q[3]), 80: (q[1], q[2])}


def refine_task(spec, cfg, paths, r_loso):
    task = load_task(spec, paths["raw"], paths["cache"], prep=cfg.get("prep", "snv"))
    fn = os.path.join(paths["raw_out"], f"forecasts_refine_{task.name.replace(':', '__')}.csv")
    if os.path.exists(fn):
        return fn
    truth = run_truth(task, paths["raw_out"], with_pls=True)
    X, y, g = task.X, task.y, task.groups
    pool = truth["pool"]; tn = np.array(truth["n"]); tr = np.array(truth["ridge_mse"]); tp = np.array(truth["pls_mse"])
    lam = truth["lam"]; base = task_seed(task.name)
    rows = []
    for n0 in cfg["n0_list"]:
        if n0 * 2 > tn.max() or n0 >= len(pool) // 2:
            continue
        hz = tn[tn >= 2 * n0]; trh = tr[tn >= 2 * n0]; tph = tp[tn >= 2 * n0]
        for s in range(cfg["n_pilots"]):
            rng = np.random.default_rng(base + 1000 * n0 + s)       # identical to run_pilots
            pil = rng.choice(pool, n0, replace=False)
            r_bar = float(r_loso[task.name])
            for meth, kw in (("RPM-w", dict(weighted=True)),
                             ("RPM-T", dict(r_mode="fixed", r_value=r_bar)),
                             ("RPM-wT", dict(weighted=True, r_mode="fixed", r_value=r_bar))):
                t0 = time.time()
                f = RPMForecaster(n_boot=cfg["n_boot"], seed=base + s, **kw).fit_forecast(X[pil], y[pil], g[pil], lam, hz)
                dt = time.time() - t0
                b = _bands(f["boot_logrmse"]); lp = np.log(np.sqrt(f["point"]))
                for i, n in enumerate(hz):
                    rows.append({"task": task.name, "family": task.family, "n0": n0, "pilot": s, "method": meth, "n": int(n),
                                 "ratio": n / n0, "fc_logrmse": float(lp[i]), "truth_ridge_logrmse": float(np.log(np.sqrt(trh[i]))),
                                 "truth_pls_logrmse": float(np.log(np.sqrt(tph[i]))), "pilot_cv_logrmse": float(np.log(np.sqrt(np.min(f["path"])))),
                                 "lo80": b[80][0][i], "hi80": b[80][1][i], "lo95": b[95][0][i], "hi95": b[95][1][i],
                                 "log_sigma2": f["params"]["log_sigma2"], "log_tau2": f["params"]["log_tau2"], "r": f["params"]["r"], "t_sec": dt})
    pd.DataFrame(rows).to_csv(fn, index=False)
    return fn


def run_refinement(cfg, paths, mode, jobs):
    specs = [tuple(s) for s in (TASKS_QUICK if mode == "quick" else TASKS_FULL)]
    order = sorted(specs, key=lambda s: 0 if s[0] == "ossl" and s[1] and s[1].startswith("KSSL") else 1)
    at = alignment_table(paths["raw_out"])
    at.to_csv(os.path.join(paths["results"], "alignment_exponents.csv"), index=False)
    r_loso = dict(zip(at.task, at.r_loso_prior))
    Parallel(n_jobs=jobs, verbose=5)(delayed(refine_task)(s, cfg, paths, r_loso) for s in order)
