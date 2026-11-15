"""E7 robustness / generalisation experiments.

(a) pre-processing variants (raw absorbance, Savitzky-Golay 1st derivative)
(b) Kennard-Stone selected pilots instead of random pilots
(c) distribution shift, mango: calibrate on seasons 1-3, test on season 4 (new season)
(d) distribution shift, mango: population(orchard/date)-grouped split instead of fruit-level split
(e) noisier reference values: Gaussian noise with variance = noise_frac * var(y) added to all labels
"""
from __future__ import annotations

import copy
import json
import os
import time

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task, load_mango
from src.models.theory import DEFAULT_MU_REL
from src.models.ridge import ridge_cv_path
from src.models.forecasters import (RPMForecaster, eigen_spectrum, pilot_subsample_curve, curve_forecast)
from src.training.learning_curves import truth_curve, split_task, TRUTH_GRID
from src.evaluation.forecast_experiment import run_truth, run_pilots, task_seed


def kennard_stone(X, k):
    """Kennard-Stone selection starting from the sample closest to the mean."""
    X = np.asarray(X, float)
    d0 = np.linalg.norm(X - X.mean(0), axis=1)
    sel = [int(np.argmin(d0))]
    mind = np.linalg.norm(X - X[sel[0]], axis=1)
    for _ in range(k - 1):
        j = int(np.argmax(mind)); sel.append(j)
        mind = np.minimum(mind, np.linalg.norm(X - X[j], axis=1))
    return np.array(sel)


def _forecast_rows(task_name, family, variant, n0, s, X0, y0, g0, lam, horizons, tr_h, n_boot, seed):
    f = RPMForecaster(n_boot=n_boot, seed=seed).fit_forecast(X0, y0, g0, lam, horizons)
    q = np.quantile(f["boot_logrmse"], [0.025, 0.1, 0.9, 0.975], axis=0)
    mu_grid = DEFAULT_MU_REL * lam.max()
    ms, es = pilot_subsample_curve(X0, y0, g0, mu_grid, seed=seed)
    ipl = curve_forecast("IPL3", ms, es, horizons)
    flat = float(np.min(f["path"]))
    rows = []
    for meth, pt, bands in (("RPM", f["point"], {"80": (q[1], q[2]), "95": (q[0], q[3])}),
                            ("IPL3", ipl["point"], {"80": ipl["bands"][0.8], "95": ipl["bands"][0.95]}),
                            ("FLAT", np.full(len(horizons), flat), None)):
        lp = np.log(np.sqrt(np.maximum(pt, 1e-300)))
        for i, n in enumerate(horizons):
            r = {"task": task_name, "family": family, "variant": variant, "n0": n0, "pilot": s, "method": meth,
                 "n": int(n), "ratio": n / n0, "fc_logrmse": float(lp[i]), "truth_ridge_logrmse": float(np.log(np.sqrt(tr_h[i])))}
            if bands is not None:
                for a, (lo, hi) in bands.items():
                    r[f"lo{a}"] = float(lo[i]); r[f"hi{a}"] = float(hi[i])
            rows.append(r)
    return rows


def _run_variant(spec, variant, cfg_r, paths, base_task=None):
    out = os.path.join(paths["raw_out"], "robustness")
    os.makedirs(out, exist_ok=True)
    fn = os.path.join(out, f"rob_{variant}_{spec[0]}_{spec[1]}_{spec[2]}.csv".replace("None", "x"))
    if os.path.exists(fn):
        return pd.read_csv(fn)
    t0 = time.time()
    rows = []
    if variant.startswith("prep_"):
        prep = variant.split("_", 1)[1]
        task = load_task(spec, paths["raw"], paths["cache"], prep=prep)
        task.name = task.name + f"[{prep}]"
        truth = run_truth(task, out, with_pls=False)
        df = run_pilots(task, truth, out, n0_list=tuple(cfg_r["n0_list"]), n_pilots=cfg_r["n_pilots"],
                        n_boot=cfg_r["n_boot"], ablation_n0=(), ablation_pilots=0, tag=f"rob_{prep}")
        df = df[df.method.isin(["RPM", "IPL3", "FLAT"])].copy(); df["variant"] = variant
        df.to_csv(fn, index=False)
        return df
    if variant == "ks_pilot":
        task = load_task(spec, paths["raw"], paths["cache"])
        truth = run_truth(task, paths["raw_out"], with_pls=True)   # identical split & truth as the main study
        pool = truth["pool"]; tn = np.array(truth["n"]); tr = np.array(truth["ridge_mse"]); lam = truth["lam"]
        for n0 in cfg_r["n0_list"]:
            if 2 * n0 > tn.max():
                continue
            horizons = tn[tn >= 2 * n0]; tr_h = tr[tn >= 2 * n0]
            for s in range(cfg_r["n_pilots"]):
                rng = np.random.default_rng(task_seed(task.name) + 7 * n0 + s)
                cand = rng.choice(pool, min(len(pool), 10 * n0), replace=False)   # candidate scans
                pil = cand[kennard_stone(task.X[cand], n0)]
                rows += _forecast_rows(task.name, task.family, variant, n0, s, task.X[pil], task.y[pil], task.groups[pil],
                                       lam, horizons, tr_h, cfg_r["n_boot"], task_seed(task.name) + s)
    elif variant in ("shift_season", "shift_population", "iid_ref_seasons123"):
        if variant == "shift_population":
            task = load_mango(paths["raw"], group_level="pop"); task.name = "Mango:DM[pop-grouped]"
            truth = run_truth(task, out, with_pls=False)
            df = run_pilots(task, truth, out, n0_list=tuple(cfg_r["n0_list"]), n_pilots=cfg_r["n_pilots"],
                            n_boot=cfg_r["n_boot"], ablation_n0=(), ablation_pilots=0, tag="rob_pop")
            df = df[df.method.isin(["RPM", "IPL3", "FLAT"])].copy(); df["variant"] = variant
            df.to_csv(fn, index=False)
            return df
        task = load_mango(paths["raw"])
        season = np.asarray(task.meta["season"])
        src = np.flatnonzero(np.isin(season, [1, 2, 3])); tgt = np.flatnonzero(season == 4)
        rng = np.random.default_rng(11)
        if variant == "shift_season":
            pool, test = src, tgt
        else:  # i.i.d. reference: held-out fruit from seasons 1-3, same size as the season-4 test set
            perm = rng.permutation(src); test = perm[:len(tgt)]; pool = perm[len(tgt):]
        tc = truth_curve(task.X, task.y, task.groups, pool, test, TRUTH_GRID, 12, with_pls=False)
        tn = np.array(tc["n"]); tr = np.array(tc["ridge_mse"])
        lam = eigen_spectrum(task.X[pool])
        for n0 in cfg_r["n0_list"]:
            horizons = tn[tn >= 2 * n0]; tr_h = tr[tn >= 2 * n0]
            for s in range(cfg_r["n_pilots"]):
                rng2 = np.random.default_rng(1000 * n0 + s)
                pil = rng2.choice(pool, n0, replace=False)
                rows += _forecast_rows("Mango:DM", "fruit", variant, n0, s, task.X[pil], task.y[pil], task.groups[pil],
                                       lam, horizons, tr_h, cfg_r["n_boot"], 100 + s)
    elif variant == "ref_noise":
        task = load_task(spec, paths["raw"], paths["cache"])
        rng = np.random.default_rng(task_seed(task.name) + 99)
        task.y = task.y + rng.normal(0, np.sqrt(cfg_r["noise_frac"] * np.var(task.y)), len(task.y))
        task.name = task.name + "[+noise]"
        truth = run_truth(task, out, with_pls=False)
        df = run_pilots(task, truth, out, n0_list=tuple(cfg_r["n0_list"]), n_pilots=cfg_r["n_pilots"],
                        n_boot=cfg_r["n_boot"], ablation_n0=(), ablation_pilots=0, tag="rob_noise")
        df = df[df.method.isin(["RPM", "IPL3", "FLAT"])].copy(); df["variant"] = variant
        df.to_csv(fn, index=False)
        return df
    df = pd.DataFrame(rows)
    df.to_csv(fn, index=False)
    return df


def run_robustness(cfg, paths, mode, jobs, log):
    cfg_r = cfg["robustness"]
    jobs_list = []
    for spec in cfg_r["tasks"]:
        spec = tuple(spec)
        for prep in cfg_r["preps"]:
            jobs_list.append((spec, f"prep_{prep}"))
        jobs_list.append((spec, "ks_pilot"))
        jobs_list.append((spec, "ref_noise"))
    jobs_list += [(("mango", None, "DM"), v) for v in ("shift_season", "iid_ref_seasons123", "shift_population")]
    t0 = time.time()
    res = Parallel(n_jobs=jobs, verbose=5)(delayed(_run_variant)(s, v, cfg_r, paths) for s, v in jobs_list)
    allr = pd.concat([r for r in res if r is not None and len(r)], ignore_index=True)
    allr.to_csv(os.path.join(paths["results"], "robustness_raw.csv"), index=False)
    log.write(json.dumps({"stage": "robustness", "rows": int(len(allr)), "seconds": round(time.time() - t0, 1)}) + "\n")
    log.flush()
