"""Refinements evaluated on exactly the same pilots as the main run (identical seeds; paired comparisons).

RPM-w  : inverse-variance-weighted path fit (specified while the main run was executing, before any main-run
         result had been inspected; motivation: heavy-tailed LOO errors near interpolation, see EXPERIMENT_LOG.md).
RPM-T  : alignment exponent r fixed at the leave-one-source-out median of the large-sample fits (post hoc).
RPM-wT : weighted + transferred (post hoc).
RPM-TD : RPM-T with the noise variance bounded below by the method-of-moments estimate of Dicker (2014) computed
         from the pilot and the unlabelled pool covariance (added in version 2 to test whether a statistical
         noise-floor estimate removes the noise-floor collapse of RPM-T).
RPM-TP : RPM-T with a weak transferred floor sigma2 >= q05 * var(y_pool), q05 = 5th percentile of the
         large-sample noise fractions of the other sources (internal audit of version 1).
Sources are defined by sample provenance: ICRAF VisNIR/MIR = one source (same soils); KSSL and Neospectra = one
source (Neospectra soils are KSSL archive samples).
"""
from __future__ import annotations

import glob
import json
import os
import re

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task, TASKS_FULL, TASKS_QUICK
from src.evaluation.forecast_experiment import run_truth, run_pilots, n_splits_for

SOURCES = (("ICRAF", "ICRAF"), ("KSSL", "KSSL"), ("Neospectra", "KSSL"), ("AfSIS1", "AfSIS1"), ("Mango", "Mango"),
           ("Diesel", "Diesel"), ("Tablets", "Tablets"), ("Tecator", "Tecator"), ("CGL", "CGL"))


def source_of(task_name):
    lib = task_name.split(":")[0]
    for pre, src in SOURCES:
        if lib.startswith(pre):
            return src
    return lib


def truth_files(raw_out):
    """Split-0 truth file per task (repeated outer splits of small tasks are excluded here)."""
    out = {}
    for f in sorted(glob.glob(os.path.join(raw_out, "truth_*.npz"))):
        stem = os.path.basename(f)[6:-4]
        if re.search(r"__s\d+$", stem):
            continue
        out[stem.replace("__", ":")] = f
    return out


def alignment_table(raw_out):
    """Large-sample fit (full-pool path, r free) per task: alignment exponent r and noise fraction
    sigma2 / var(y_pool) (normalised by the pool variance; no test labels are used)."""
    rows = []
    for name, f in truth_files(raw_out).items():
        z = np.load(f, allow_pickle=True)
        fit = json.loads(str(z["full_fits"]))["free"]
        vp = float(z["var_pool"]) if "var_pool" in z.files else float(z["var_test"])
        rows.append({"task": name, "source": source_of(name), "r_full_pool": fit["r"],
                     "noise_frac_full_pool": float(np.exp(fit["log_sigma2"]) / vp), "n_pool": len(z["pool"])})
    t = pd.DataFrame(rows)
    t["r_loso_prior"] = [float(t[t.source != s].r_full_pool.median()) for s in t.source]
    # weak noise-floor prior for RPM-TP: 5th percentile of the large-sample noise fractions of the other sources
    t["noise_floor_loso_q05"] = [float(t[t.source != s].noise_frac_full_pool.quantile(0.05)) for s in t.source]
    return t


def refine_task(spec, cfg, paths, r_loso, split):
    task = load_task(spec, paths["raw"], paths["cache"], prep=cfg.get("prep", "snv"))
    truth = run_truth(task, paths["raw_out"], with_pls=True, split=split)
    r_bar = float(r_loso[task.name][0])
    floor = float(r_loso[task.name][1]) * float(truth["var_pool"])
    extra = [("RPM-w", dict(weighted=True)),
             ("RPM-T", dict(r_mode="fixed", r_value=r_bar, n_boot=0)),
             ("RPM-wT", dict(weighted=True, r_mode="fixed", r_value=r_bar, n_boot=0)),
             ("RPM-TD", dict(r_mode="fixed", r_value=r_bar, dicker_floor=True, n_boot=0)),
             ("RPM-TP", dict(r_mode="fixed", r_value=r_bar, sigma2_floor=floor, n_boot=0))]
    npil = cfg["n_pilots"] if n_splits_for(task) == 1 else cfg.get("n_pilots_split", 10)
    run_pilots(task, truth, paths["raw_out"], n0_list=tuple(cfg["n0_list"]), n_pilots=npil, n_boot=cfg["n_boot"],
               tag="refine", extra_rpm=extra, split=split, diagnostics=False)
    return task.name


def run_refinement(cfg, paths, mode, jobs):
    specs = [tuple(s) for s in (TASKS_QUICK if mode == "quick" else TASKS_FULL)]
    at = alignment_table(paths["raw_out"])
    at.to_csv(os.path.join(paths["results"], "alignment_exponents.csv"), index=False)
    r_loso = {t: (a, b) for t, a, b in zip(at.task, at.r_loso_prior, at.noise_floor_loso_q05)}
    jobs_list = []
    for sp in specs:
        k = 10 if (sp[0] in ("diesel", "tecator", "cgl", "tablets")) else 1
        jobs_list += [(sp, j) for j in range(k)]
    jobs_list.sort(key=lambda t: 0 if (t[0][0] == "ossl" and t[0][1] and t[0][1].startswith("KSSL")) else 1)
    Parallel(n_jobs=jobs, verbose=5)(delayed(refine_task)(sp, cfg, paths, r_loso, j) for sp, j in jobs_list)
