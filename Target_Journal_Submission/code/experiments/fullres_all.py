"""Native-resolution confirmation study (pre-specified in supplementary/FULLRES_preregistration_addendum.md).
Run: RPM_FULLRES=1 python -m experiments.fullres_all [jobs]
Stage 1: ground truth for all tasks/splits; stage 2: LOSO priors from native-resolution large-sample fits;
stage 3: pilots (FLAT, RPM, IPL3/IPL2/EXP3/LOG2, DFOLS, B-RPM)."""
import os
import sys

assert os.environ.get("RPM_FULLRES") == "1", "set RPM_FULLRES=1"
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task, TASKS_FULL
from src.evaluation.forecast_experiment import run_truth, run_pilots, n_splits_for
from src.models.bayes_rpm import prior_from_table
from experiments.refinement import alignment_table
from experiments.bayes import family_of_source

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "results", "fullres_all", "raw")
RAW = os.path.abspath(os.path.join(ROOT, "..", "data_raw")); CACHE = os.path.join(ROOT, "code", "data", "cache")
SMALL = ("diesel", "tablets", "tecator", "cgl")


def truth_unit(spec, split):
    task = load_task(spec, RAW, CACHE)
    run_truth(task, OUT, with_pls=False, split=split)
    return task.name


def pilot_unit(spec, split, priors):
    task = load_task(spec, RAW, CACHE)
    truth = run_truth(task, OUT, with_pls=False, split=split)
    npil = 20 if n_splits_for(task) == 1 else 10
    run_pilots(task, truth, OUT, n0_list=(25, 50, 100, 200), n_pilots=npil, n_boot=0, ablation_n0=(), ablation_pilots=0,
               tag="rob_fullall", brpm_prior=priors[task.name], split=split, diagnostics=False)
    return task.name


if __name__ == "__main__":
    jobs = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    os.makedirs(OUT, exist_ok=True)
    units = [(s, j) for s in sorted(TASKS_FULL, key=lambda s: 0 if s[0] == "ossl" and str(s[1]).startswith("KSSL") else 1)
             for j in range(10 if s[0] in SMALL else 1)]
    Parallel(n_jobs=jobs, verbose=5)(delayed(truth_unit)(s, j) for s, j in units)
    at = alignment_table(OUT); at["family"] = [family_of_source(x) for x in at.source]
    at.to_csv(os.path.join(ROOT, "results", "fullres_all", "alignment_exponents_fullres.csv"), index=False)
    priors = {t: prior_from_table(at, exclude_sources=(s,)) for t, s in zip(at.task, at.source)}
    Parallel(n_jobs=jobs, verbose=5)(delayed(pilot_unit)(s, j, priors) for s, j in units)
    print("done")
