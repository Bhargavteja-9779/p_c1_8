"""Ablation of the eigen-spectrum source for RPM-T (transferred alignment exponent).

Pre-registered ablation (E6) showed no benefit of unlabelled spectra when r = 1; this follow-up,
defined before RPM-T results were inspected (EXPERIMENT_LOG 2026-11-16 14:45), repeats the
comparison for RPM-T on identical pilots (n0 in {50, 100}, pilots 0-9):
  RPM-T (pool eigen-spectrum) | RPM-T-pilotcov | RPM-T-pilotcov+tail | RPM-T-U250
"""
from __future__ import annotations

import os

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task, TASKS_FULL, TASKS_QUICK
from src.models.forecasters import RPMForecaster, eigen_spectrum, complete_tail_powerlaw
from src.evaluation.forecast_experiment import run_truth, task_seed


def ablate_task(spec, paths, r_loso, n0_list=(50, 100), n_pilots=10):
    task = load_task(spec, paths["raw"], paths["cache"])
    fn = os.path.join(paths["raw_out"], f"forecasts_ablT_{task.name.replace(':', '__')}.csv")
    if os.path.exists(fn):
        return fn
    truth = run_truth(task, paths["raw_out"], with_pls=True)
    X, y, g = task.X, task.y, task.groups
    pool = truth["pool"]; tn = np.array(truth["n"]); tr = np.array(truth["ridge_mse"])
    lam_pool = truth["lam"]; base = task_seed(task.name); r_bar = float(r_loso[task.name])
    rows = []
    for n0 in n0_list:
        if n0 * 2 > tn.max() or n0 >= len(pool) // 2:
            continue
        hz = tn[tn >= 2 * n0]; trh = tr[tn >= 2 * n0]
        for s in range(n_pilots):
            rng = np.random.default_rng(base + 1000 * n0 + s)          # identical pilots
            pil = rng.choice(pool, n0, replace=False)
            X0, y0, g0 = X[pil], y[pil], g[pil]
            lam_p = eigen_spectrum(X0)
            lam_t = complete_tail_powerlaw(lam_p, X.shape[1])
            others = np.setdiff1d(pool, pil)
            urng = np.random.default_rng(base + 7 * n0 + s)
            u_idx = np.concatenate([pil, urng.choice(others, min(max(250 - n0, 0), len(others)), replace=False)])
            lam_u = eigen_spectrum(X[u_idx])
            for nm, lam in (("RPM-T", lam_pool), ("RPM-T-pilotcov", lam_p), ("RPM-T-pilotcov+tail", lam_t), ("RPM-T-U250", lam_u)):
                f = RPMForecaster(n_boot=0, r_mode="fixed", r_value=r_bar).fit_forecast(X0, y0, g0, lam, hz)
                lp = np.log(np.sqrt(f["point"]))
                for i, n in enumerate(hz):
                    rows.append({"task": task.name, "family": task.family, "n0": n0, "pilot": s, "method": nm, "n": int(n),
                                 "ratio": n / n0, "fc_logrmse": float(lp[i]), "truth_ridge_logrmse": float(np.log(np.sqrt(trh[i])))})
    pd.DataFrame(rows).to_csv(fn, index=False)
    return fn


def run_ablation_t(paths, mode, jobs):
    at = pd.read_csv(os.path.join(paths["results"], "alignment_exponents.csv"))
    r_loso = dict(zip(at.task, at.r_loso_prior))
    specs = [tuple(s) for s in (TASKS_QUICK if mode == "quick" else TASKS_FULL)]
    Parallel(n_jobs=jobs, verbose=5)(delayed(ablate_task)(s, paths, r_loso) for s in specs)
