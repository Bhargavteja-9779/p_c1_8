"""Bayesian regularisation-path matching (B-RPM) on exactly the main-run pilots (identical seeds; paired comparisons).

Specified 2026-11-21 (session 3) BEFORE any version-2 forecast result had been inspected; see EXPERIMENT_LOG.md and
supplementary/BRPM_preregistration_addendum.md. Variants:
  B-RPM        primary: prior on r and logit(eta) from large-sample fits of OTHER sources (LOSO), m_eff = 2
  B-RPM-LOFO   prior from other application FAMILIES only (soil tasks get a non-soil prior and vice versa)
  B-RPM-r      prior on r only (flat on eta)                         -> role of the noise prior
  B-RPM-0      prior only (pilot path ignored except for its level)   -> what the pilot shape adds
  B-RPM-m10    m_eff = 10 (sensitivity to the effective-observation count)
"""
from __future__ import annotations

import os

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task, TASKS_FULL, TASKS_QUICK
from src.evaluation.forecast_experiment import run_truth, task_seed, n_splits_for, _sfx
from src.models.theory import DEFAULT_MU_REL
from src.models.ridge import ridge_cv_path
from src.models.bayes_rpm import fit_forecast_brpm, prior_from_table, precompute_horizons
from experiments.refinement import alignment_table

FAMILY = {"ICRAF": "soil", "KSSL": "soil", "AfSIS1": "soil", "Mango": "fruit", "Diesel": "fuel", "Tablets": "pharma",
          "Tecator": "meat", "CGL": "mixture"}


def family_of_source(src):
    return FAMILY.get(src, src)


def bayes_task(spec, cfg, paths, tab, split, force=False):
    task = load_task(spec, paths["raw"], paths["cache"], prep=cfg.get("prep", "snv"))
    out = os.path.join(paths["raw_out"], f"forecasts_bayes_{_sfx(task, split)}.csv")
    if os.path.exists(out) and not force:
        return task.name
    truth = run_truth(task, paths["raw_out"], with_pls=True, split=split)
    src = tab.loc[tab.task == task.name, "source"].iloc[0]
    fam = family_of_source(src)
    pri = prior_from_table(tab, exclude_sources=(src,))
    pri_f = prior_from_table(tab, exclude_families=(fam,))
    pri_r = dict(pri, s_e=np.inf)
    X, y, g = task.X, task.y, task.groups
    pool = truth["pool"]
    tn = np.array(truth["n"]); tr = np.array(truth["ridge_mse"])
    lam = truth["lam"]; mu_grid = DEFAULT_MU_REL * lam.max()
    base_seed = task_seed(task.name) + 7919 * split
    npil = cfg["n_pilots"] if n_splits_for(task) == 1 else cfg.get("n_pilots_split", 10)
    rows = []
    for n0 in cfg["n0_list"]:
        if n0 * 2 > tn.max() or n0 >= len(pool) // 2:
            continue
        sel = tn >= n0; horizons = tn[sel]; tr_h = tr[sel]
        pre = precompute_horizons(lam, horizons)
        for s in range(npil):
            rng = np.random.default_rng(base_seed + 1000 * n0 + s)
            pil = rng.choice(pool, n0, replace=False)
            X0, y0, g0 = X[pil], y[pil], g[pil]
            e, vlog = ridge_cv_path(X0, y0, mu_grid, groups=g0, return_var=True)
            j = int(np.argmin(e))
            gsz = float(np.mean(np.unique(g0, return_counts=True)[1])); n_eff = n0 - gsz
            res = {}
            for nm, pr, m in (("B-RPM", pri, 2.0), ("B-RPM-LOFO", pri_f, 2.0), ("B-RPM-r", pri_r, 2.0),
                              ("B-RPM-0", pri, 1e-9), ("B-RPM-m10", pri, 10.0)):
                res[nm] = fit_forecast_brpm(lam, e, n_eff, horizons, pr, vlog[j], m_eff=m, pre=pre)
            for nm, f in res.items():
                for i, n in enumerate(horizons):
                    row = {"task": task.name, "family": task.family, "split": split, "n0": n0, "pilot": s, "method": nm,
                           "n": int(n), "ratio": float(n / n0), "fc_logrmse": float(f["point_logrmse"][i]),
                           "truth_ridge_logrmse": float(np.log(np.sqrt(tr_h[i]))),
                           "pilot_cv_logrmse": float(np.log(np.sqrt(e[j]))),
                           "info_gain": float(f["info_gain"][i]), "gain_post_sd": float(f["gain_post_sd"][i]),
                           "gain_prior_sd": float(f["gain_prior_sd"][i])}
                    for a, (lo, hi) in f["bands"].items():
                        row[f"lo{int(a*100)}"] = float(lo[i]); row[f"hi{int(a*100)}"] = float(hi[i])
                    row.update({k: v for k, v in f["post"].items()})
                    row["id_lo"] = float(f["id_lo"][i]); row["id_hi"] = float(f["id_hi"][i])
                    rows.append(row)
    pd.DataFrame(rows).to_csv(out, index=False)
    return task.name


def run_bayes(cfg, paths, mode, jobs, force=False):
    specs = [tuple(s) for s in (TASKS_QUICK if mode == "quick" else TASKS_FULL)]
    tab = alignment_table(paths["raw_out"])
    tab["family"] = [family_of_source(s) for s in tab.source]
    tab.to_csv(os.path.join(paths["results"], "alignment_exponents.csv"), index=False)
    jobs_list = []
    for sp in specs:
        k = 10 if sp[0] in ("diesel", "tecator", "cgl", "tablets") else 1
        jobs_list += [(sp, j) for j in range(k)]
    Parallel(n_jobs=jobs, verbose=5)(delayed(bayes_task)(sp, cfg, paths, tab, j, force) for sp, j in jobs_list)
