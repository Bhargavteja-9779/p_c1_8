"""Full-resolution robustness experiment: the main study sub-samples spectra to 94-216 variables. Here six
representative tasks are re-run with spectra at (near-)native resolution (MIR 4 cm-1, VisNIR/NIR 2 nm, diesel and tablets
undecimated): ground truth, pilots (n0 = 25, 50, 100; 10 pilots), FLAT, RPM, IPL3 and B-RPM (LOSO prior from the main
study), the compatible set and the hidden-signal share at the observability horizon.
Run:  RPM_FULLRES=1 python -m experiments.fullres
"""
import json
import os
import sys

assert os.environ.get("RPM_FULLRES") == "1", "set RPM_FULLRES=1"
import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.data.datasets import load_task
from src.evaluation.forecast_experiment import run_truth, run_pilots
from src.models.bayes_rpm import prior_from_table
from src.models.theory import solve_kappa
from experiments.bayes import family_of_source

TASKS = [("ossl", "KSSL-MIR", "OC"), ("ossl", "ICRAF-MIR", "clay"), ("ossl", "KSSL-VisNIR", "clay"),
         ("ossl", "Neospectra-NIR", "pH"), ("diesel", None, "bp50"), ("tablets", None, "assay")]


def one(spec, root):
    out = os.path.join(root, "results", "raw", "fullres"); os.makedirs(out, exist_ok=True)
    raw = os.path.abspath(os.path.join(root, "..", "data_raw")); cache = os.path.join(root, "code", "data", "cache")
    task = load_task(spec, raw, cache)
    base = task.name
    task.name = base + "[full]"
    al = pd.read_csv(os.path.join(root, "results", "alignment_exponents.csv"))
    if "family" not in al:
        al["family"] = [family_of_source(s) for s in al.source]
    src = al.loc[al.task == base, "source"].iloc[0]
    prior = prior_from_table(al, exclude_sources=(src,))
    truth = run_truth(task, out, with_pls=False)
    df = run_pilots(task, truth, out, n0_list=(25, 50, 100), n_pilots=10, n_boot=0, ablation_n0=(), ablation_pilots=0,
                    tag="rob_fullres", brpm_prior=prior, diagnostics=False)
    fit = json.loads(str(truth["full_fits"]))["free"]; lam = truth["lam"]
    vp = float(truth["var_pool"]); eta = float(np.exp(fit["log_sigma2"]) / vp)
    sk = (lam / lam.max()) ** fit["r"]; sig = eta / (1 - eta) * sk.sum()
    hid = {}
    for n0 in (25, 50, 100):
        k0 = solve_kappa(lam, float(n0), np.array([1e-14 * lam.max()]))[0]
        h = float(np.sum(sk * (k0 / (lam + k0)) ** 2)); hid[n0] = h / (h + sig)
    return {"task": base, "p_full": int(task.X.shape[1]), "n_modes": int(len(lam)), "r_full": fit["r"], "eta_full": eta,
            **{f"hidden_{k}": v for k, v in hid.items()}}


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    res = Parallel(n_jobs=int(sys.argv[1]) if len(sys.argv) > 1 else 3, verbose=5)(delayed(one)(s, root) for s in TASKS)
    pd.DataFrame(res).to_csv(os.path.join(root, "results", "fullres_summary.csv"), index=False)
    print(pd.DataFrame(res))
