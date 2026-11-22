"""Analysis of the native-resolution confirmation study (HC1, supplementary/FULLRES_preregistration_addendum.md)."""
import glob
import json
import os
import re

import numpy as np
import pandas as pd

from experiments.refinement import source_of
from experiments.bayes import family_of_source
from experiments.bayes_analysis import paired, holm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW = os.path.join(ROOT, "results", "fullres_all", "raw")
GEN = {"KSSL-MIR:OC", "ICRAF-MIR:clay", "KSSL-VisNIR:clay", "Neospectra-NIR:pH", "Diesel:bp50", "Tablets:assay"}


def main():
    df = pd.concat([pd.read_csv(f) for f in glob.glob(os.path.join(RAW, "forecasts_rob_fullall_*.csv"))], ignore_index=True)
    df = df[df.method != "_timing"].copy()
    # SLOPE-T from native-resolution truth slopes of OTHER sources (split-0 truth files)
    sl = {}
    for f in glob.glob(os.path.join(RAW, "truth_*.npz")):
        stem = os.path.basename(f)[6:-4]
        if re.search(r"__s\d+$", stem):
            continue
        z = np.load(f, allow_pickle=True)
        sl[stem.replace("__", ":")] = float(np.polyfit(np.log2(z["n"].astype(float)), 0.5 * np.log(z["ridge_mse"]), 1)[0])
    sl = pd.Series(sl); src = {t: source_of(t) for t in sl.index}
    loso = {t: float(sl[[u for u in sl.index if src[u] != src[t]]].median()) for t in sl.index}
    b = df[df.method == "FLAT"].copy(); b["method"] = "SLOPE-T"
    b["fc_logrmse"] = b.pilot_cv_logrmse + b.task.map(loso) * np.log2(b.n / b.n0)
    df = pd.concat([df, b], ignore_index=True)
    t0 = df[df.ratio == 1].groupby(["task", "split", "n0"]).truth_ridge_logrmse.first().rename("t0").reset_index()
    df = df.merge(t0, on=["task", "split", "n0"], how="left")
    ev = df[df.ratio >= 2].copy()
    ev["err"] = ev.fc_logrmse - ev.truth_ridge_logrmse; ev["abs_err"] = ev.err.abs()
    ev["gain_abs_err"] = ((ev.fc_logrmse - ev.pilot_cv_logrmse) - (ev.truth_ridge_logrmse - ev.t0)).abs()
    M = ["B-RPM", "FLAT", "RPM", "IPL3", "SLOPE-T", "IPL2", "DFOLS"]
    lvl = ev[ev.method.isin(M)].groupby(["task", "method"]).abs_err.mean().unstack()
    gn = ev[ev.method.isin(M)].groupby(["task", "method"]).gain_abs_err.mean().unstack()
    bias = ev[ev.method.isin(M)].groupby(["task", "method"]).err.mean().unstack()
    held = [t for t in lvl.index if t not in GEN]
    srcs = pd.Series({t: source_of(t) for t in lvl.index})
    num = {"n_tasks": int(len(lvl)), "n_heldout": len(held)}
    rows = []
    for scope, idx in (("held-out (HC1)", held), ("all", list(lvl.index)), ("hypothesis-generating", [t for t in lvl.index if t in GEN])):
        for m in M:
            if m in lvl:
                rows.append({"scope": scope, "method": m, "n_tasks": len(idx), "level_mae": lvl.loc[idx, m].mean(),
                             "gain_mae": gn.loc[idx, m].mean(), "abs_task_bias": bias.loc[idx, m].abs().mean(), "mean_bias": bias.loc[idx, m].mean()})
    T1 = pd.DataFrame(rows)
    tests = []
    for scope, idx in (("held-out (HC1)", held), ("all", list(lvl.index))):
        for ref in ("FLAT", "RPM", "IPL3", "SLOPE-T"):
            for ep, T in (("level", lvl), ("gain", gn)):
                r_t = paired(T.loc[idx, "B-RPM"].values, T.loc[idx, ref].values)
                Ts = T.loc[idx, ["B-RPM", ref]].groupby(srcs.loc[idx]).mean(); r_s = paired(Ts["B-RPM"].values, Ts[ref].values)
                tests.append({"scope": scope, "endpoint": ep, "reference": ref, "improvement": r_t["mean_diff"], "ci_lo": r_t["lo"],
                              "ci_hi": r_t["hi"], "p": r_t["p"], "wins": r_t["wins"], "n": r_t["n"], "source_improvement": r_s["mean_diff"],
                              "source_p": r_s["p"], "source_wins": r_s["wins"], "n_sources": r_s["n"]})
    T2 = pd.DataFrame(tests)
    T2["p_holm_within_scope"] = np.nan
    for sc in T2.scope.unique():
        msk = T2.scope == sc
        T2.loc[msk, "p_holm_within_scope"] = holm(T2.loc[msk, "p"].fillna(1).values)
    # by family and by n0 (held-out)
    fam = pd.Series({t: family_of_source(source_of(t)) for t in lvl.index})
    T3 = lvl.loc[held, [m for m in M if m in lvl]].groupby(fam.loc[held]).mean()
    T4 = ev[ev.method.isin(M) & ev.task.isin(held)].groupby(["n0", "task", "method"]).abs_err.mean().groupby(["n0", "method"]).mean().unstack()
    tab = os.path.join(ROOT, "tables")
    T1.to_csv(os.path.join(tab, "TC1_native_resolution_summary.csv"), index=False)
    T2.to_csv(os.path.join(tab, "TC2_native_resolution_tests.csv"), index=False)
    T3.reset_index().to_csv(os.path.join(tab, "TC3_native_resolution_by_family.csv"), index=False)
    T4.reset_index().to_csv(os.path.join(tab, "TC4_native_resolution_by_n0.csv"), index=False)
    pd.set_option("display.width", 220)
    print(T1.round(3).to_string()); print(T2.round(4).to_string()); print(T3.round(3)); print(T4.round(3))


if __name__ == "__main__":
    main()
