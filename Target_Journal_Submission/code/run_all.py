#!/usr/bin/env python3
"""Reproduce every experiment, statistic, table and figure of the study.

    python run_all.py --mode quick     # pipeline check (3 tasks, few pilots), ~5 min on 4 CPU cores
    python run_all.py --mode full      # complete study (38 tasks), several CPU-hours

Outputs (relative to the submission package root):
    results/raw/            truth curves (npz) and per-pilot forecasts (csv)
    results/*.csv|json      aggregated metrics, statistics
    tables/                 machine-generated tables (csv + markdown + LaTeX)
    figures/                publication figures (png + pdf)
    results/experiment_logs/run_<mode>.log
"""
import argparse
import json
import os
import platform
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np  # noqa: E402
import yaml  # noqa: E402
from joblib import Parallel, delayed  # noqa: E402

from src.data.datasets import load_task, TASKS_FULL, TASKS_QUICK  # noqa: E402
from src.evaluation.forecast_experiment import run_truth, run_pilots  # noqa: E402


def detect_hardware():
    info = {"python": platform.python_version(), "machine": platform.machine(), "cpus": os.cpu_count()}
    try:
        import torch  # optional; not required by this study
        info["cuda"] = bool(torch.cuda.is_available())
        info["mps"] = bool(getattr(torch.backends, "mps", None) and torch.backends.mps.is_available())
    except Exception:
        info["cuda"] = False; info["mps"] = False
    info["device_used"] = "cpu"  # all computations are linear algebra on CPU by design
    return info


def _one_task(spec, cfg, paths, mode):
    t0 = time.time()
    task = load_task(spec, paths["raw"], paths["cache"], prep=cfg.get("prep", "snv"))
    truth = run_truth(task, paths["raw_out"], with_pls=True)
    run_pilots(task, truth, paths["raw_out"], n0_list=tuple(cfg["n0_list"]), n_pilots=cfg["n_pilots"],
               n_boot=cfg["n_boot"], ablation_n0=tuple(cfg["ablation_n0"]), ablation_pilots=cfg["ablation_pilots"])
    return task.name, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["quick", "full"], default="quick")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2)))
    ap.add_argument("--stage", choices=["all", "main", "simulation", "refinement", "robustness", "analysis"], default="all")
    a = ap.parse_args()
    cfg = yaml.safe_load(open(os.path.join(HERE, "config", f"{a.mode}.yaml")))
    root = os.path.abspath(os.path.join(HERE, ".."))
    out_root = os.path.join(root, cfg.get("output_subdir", "results"))
    paths = {"raw": os.path.abspath(os.path.join(HERE, cfg["raw_data_dir"])), "cache": os.path.join(HERE, "data", "cache"),
             "raw_out": os.path.join(out_root, "raw"), "results": out_root,
             "tables": os.path.join(root, cfg.get("tables_subdir", "tables")),
             "figures": os.path.join(root, cfg.get("figures_subdir", "figures")),
             "logs": os.path.join(out_root, "experiment_logs")}
    for p in paths.values():
        os.makedirs(p, exist_ok=True)
    log = open(os.path.join(paths["logs"], f"run_{a.mode}.log"), "a")
    hw = detect_hardware()
    log.write(json.dumps({"start": time.strftime("%Y-%m-%d %H:%M:%S"), "mode": a.mode, "hardware": hw, "config": cfg}) + "\n"); log.flush()
    print("hardware:", hw)
    specs = [tuple(s) for s in (TASKS_QUICK if a.mode == "quick" else TASKS_FULL)]
    if a.stage in ("all", "main"):
        order = sorted(specs, key=lambda s: 0 if s[0] == "ossl" and s[1] and s[1].startswith("KSSL") else 1)
        res = Parallel(n_jobs=a.jobs, verbose=5)(delayed(_one_task)(s, cfg, paths, a.mode) for s in order)
        for name, sec in res:
            log.write(json.dumps({"task": name, "seconds": round(sec, 1)}) + "\n")
        log.flush()
    if a.stage in ("all", "simulation"):
        from experiments.simulation import run_simulation
        run_simulation(paths, a.mode, a.jobs)
        log.write(json.dumps({"stage": "simulation", "done": True}) + "\n"); log.flush()
    if a.stage in ("all", "refinement"):
        from experiments.refinement import run_refinement
        run_refinement(cfg, paths, a.mode, a.jobs)
        log.write(json.dumps({"stage": "refinement", "done": True}) + "\n"); log.flush()
    if a.stage in ("all", "robustness"):
        from experiments.robustness import run_robustness
        run_robustness(cfg, paths, a.mode, a.jobs, log)
    if a.stage in ("all", "analysis"):
        from experiments.analysis import run_analysis
        run_analysis(cfg, paths, a.mode, log)
    log.write(json.dumps({"end": time.strftime("%Y-%m-%d %H:%M:%S")}) + "\n"); log.close()


if __name__ == "__main__":
    main()
