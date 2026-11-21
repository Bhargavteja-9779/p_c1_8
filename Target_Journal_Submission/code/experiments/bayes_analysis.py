"""Evaluation of B-RPM against the pre-specified hypotheses HB1-HB4 (supplementary/BRPM_preregistration_addendum.md).

Outputs: results/bayes_numbers.json and tables/TB*_*.csv/.md
"""
from __future__ import annotations

import glob
import json
import os
import re

import numpy as np
import pandas as pd
from scipy.stats import norm, wilcoxon

from experiments.refinement import source_of
from experiments.bayes import family_of_source

COMPARE = ["B-RPM", "B-RPM-LOFO", "B-RPM-r", "B-RPM-0", "B-RPM-m10", "RPM", "RPM-w", "RPM-T", "RPM-TD", "RPM-TP",
           "IPL3", "IPL2", "FLAT", "DFOLS", "WEI", "SLOPE-T", "SLOPE-T-LOFO"]


def load_all(raw_dir):
    fs = []
    for tag in ("main", "refine", "bayes"):
        fs += sorted(glob.glob(os.path.join(raw_dir, f"forecasts_{tag}_*.csv")))
    df = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    df = df[df.method != "_timing"].copy()
    df["source"] = df.task.map(source_of)
    df["fam"] = df.source.map(family_of_source)
    return df


def truth_slopes(raw_dir):
    out = {}
    for f in glob.glob(os.path.join(raw_dir, "truth_*.npz")):
        stem = os.path.basename(f)[6:-4]
        if re.search(r"__s\d+$", stem):
            continue
        z = np.load(f, allow_pickle=True)
        x = np.log2(z["n"].astype(float)); yv = 0.5 * np.log(z["ridge_mse"])
        out[stem.replace("__", ":")] = float(np.polyfit(x, yv, 1)[0])
    return pd.Series(out)


def add_slope(df, raw_dir):
    st = truth_slopes(raw_dir)
    src = {t: source_of(t) for t in st.index}; fam = {t: family_of_source(src[t]) for t in st.index}
    loso = {t: float(st[[u for u in st.index if src[u] != src[t]]].median()) for t in st.index}
    lofo = {t: float(st[[u for u in st.index if fam[u] != fam[t]]].median()) for t in st.index}
    base = df[df.method == "FLAT"].copy()
    outs = [df]
    for nm, mp in (("SLOPE-T", loso), ("SLOPE-T-LOFO", lofo)):
        b = base.copy(); b["method"] = nm
        b["fc_logrmse"] = b.pilot_cv_logrmse + b.task.map(mp) * np.log2(b.n / b.n0)
        for c in ("lo80", "hi80", "lo95", "hi95"):
            if c in b:
                b[c] = np.nan
        outs.append(b)
    return pd.concat(outs, ignore_index=True), st


def add_gain(df):
    t0 = (df[df.ratio == 1].groupby(["task", "split", "n0"]).truth_ridge_logrmse.first().rename("truth_n0"))
    df = df.merge(t0.reset_index(), on=["task", "split", "n0"], how="left")
    df["err"] = df.fc_logrmse - df.truth_ridge_logrmse
    df["abs_err"] = df.err.abs()
    df["gain_fc"] = df.fc_logrmse - df.pilot_cv_logrmse
    df["gain_true"] = df.truth_ridge_logrmse - df.truth_n0
    df["gain_err"] = df.gain_fc - df.gain_true
    df["gain_abs_err"] = df.gain_err.abs()
    return df


def paired(a, b, seed=0):
    d = np.asarray(b) - np.asarray(a)
    ok = np.isfinite(d); d = d[ok]
    if len(d) < 3:
        return dict(n=len(d), median_diff=np.nan, mean_diff=np.nan, p=np.nan, lo=np.nan, hi=np.nan, wins=np.nan)
    rng = np.random.default_rng(seed)
    bs = [np.mean(rng.choice(d, len(d))) for _ in range(4000)]
    try:
        p = float(wilcoxon(d).pvalue)
    except ValueError:
        p = 1.0
    return dict(n=int(len(d)), mean_diff=float(d.mean()), median_diff=float(np.median(d)), p=p,
                lo=float(np.quantile(bs, 0.025)), hi=float(np.quantile(bs, 0.975)), wins=int((d > 0).sum()))


def holm(ps):
    ps = np.asarray(ps, float); o = np.argsort(ps); m = len(ps); adj = np.empty(m); run = 0
    for i, j in enumerate(o):
        run = max(run, min(1.0, (m - i) * ps[j])); adj[j] = run
    return adj


def run_bayes_analysis(paths):
    raw = paths["raw_out"]; tabs = paths["tables"]
    df = load_all(raw)
    df, slopes = add_slope(df, raw)
    df = add_gain(df)
    ev = df[(df.ratio >= 2) & df.method.isin(COMPARE)]
    num = {}
    # level and gain endpoints: task means (each task weighted once; splits/pilots/horizons averaged)
    lvl = ev.groupby(["task", "method"]).abs_err.mean().unstack()
    gn = ev.groupby(["task", "method"]).gain_abs_err.mean().unstack()
    bias = ev.groupby(["task", "method"]).err.mean().unstack()
    src = pd.Series({t: source_of(t) for t in lvl.index})
    rows = []
    for m in [c for c in COMPARE if c in lvl]:
        rows.append({"method": m, "n_tasks": int(lvl[m].notna().sum()), "level_mae": lvl[m].mean(), "level_median": lvl[m].median(),
                     "mean_bias": bias[m].mean(), "gain_mae": gn[m].mean(), "gain_median": gn[m].median(),
                     "level_mae_source": lvl[m].groupby(src).mean().mean(), "gain_mae_source": gn[m].groupby(src).mean().mean()})
    TB1 = pd.DataFrame(rows)
    num["TB1_summary"] = TB1.to_dict("records")
    # HB1: gain error of B-RPM-LOFO vs SLOPE-T-LOFO (task and source level); also B-RPM vs SLOPE-T (LOSO)
    comps = [("SLOPE-T-LOFO", "B-RPM-LOFO", "gain"), ("SLOPE-T", "B-RPM", "gain"), ("FLAT", "B-RPM", "level"),
             ("SLOPE-T", "B-RPM", "level"), ("RPM", "B-RPM", "level"), ("RPM", "B-RPM", "gain"), ("IPL3", "B-RPM", "level"),
             ("IPL3", "B-RPM", "gain"), ("FLAT", "B-RPM", "gain"), ("B-RPM-0", "B-RPM", "gain"), ("RPM-T", "B-RPM", "level"),
             ("WEI", "B-RPM", "level"), ("WEI", "B-RPM", "gain")]
    out = []
    for ref, m, ep in comps:
        T = lvl if ep == "level" else gn
        if ref not in T or m not in T:
            continue
        r_t = paired(T[m].values, T[ref].values)            # positive diff = method better than reference
        Ts = T[[ref, m]].groupby(src).mean()
        r_s = paired(Ts[m].values, Ts[ref].values)
        out.append({"endpoint": ep, "method": m, "reference": ref, "task_mean_improvement": r_t["mean_diff"],
                    "task_ci_lo": r_t["lo"], "task_ci_hi": r_t["hi"], "task_p": r_t["p"], "task_wins": r_t["wins"], "n_tasks": r_t["n"],
                    "source_mean_improvement": r_s["mean_diff"], "source_p": r_s["p"], "source_wins": r_s["wins"], "n_sources": r_s["n"]})
    TB2 = pd.DataFrame(out); TB2["task_p_holm"] = holm(TB2.task_p.fillna(1).values)
    num["TB2_paired"] = TB2.to_dict("records")
    # by family (gain and level)
    fam = pd.Series({t: family_of_source(source_of(t)) for t in lvl.index})
    TB3 = pd.concat({"level": lvl.groupby(fam).mean(), "gain": gn.groupby(fam).mean()}, axis=0)
    num["TB3_by_family"] = TB3.reset_index().rename(columns={"level_0": "endpoint", "level_1": "family"}).to_dict("records")
    # HB3: coverage by family and by n0
    cov = []
    for m in ["B-RPM", "B-RPM-LOFO", "RPM", "IPL3"]:
        g = ev[(ev.method == m) & ev.lo80.notna()]
        if not len(g):
            continue
        g = g.assign(c80=(g.truth_ridge_logrmse >= g.lo80) & (g.truth_ridge_logrmse <= g.hi80),
                     c95=(g.truth_ridge_logrmse >= g.lo95) & (g.truth_ridge_logrmse <= g.hi95),
                     wf80=np.exp(g.hi80 - g.lo80))
        for key in ("fam", "n0"):
            for v, gg in g.groupby(key):
                tm = gg.groupby("task")[["c80", "c95"]].mean().mean()
                cov.append({"method": m, "stratum": key, "value": v, "cov80": tm.c80, "cov95": tm.c95,
                            "median_width_factor80": float(gg.wf80.median()), "n_tasks": gg.task.nunique()})
        tm = g.groupby("task")[["c80", "c95"]].mean().mean()
        cov.append({"method": m, "stratum": "all", "value": "all", "cov80": tm.c80, "cov95": tm.c95,
                    "median_width_factor80": float(g.wf80.median()), "n_tasks": g.task.nunique()})
    # POST HOC (labelled as such): leave-one-source-out recalibration of the B-RPM predictive spread. The standardised
    # error z = err / sd_pred (sd_pred from the 80 % band) of all OTHER sources gives the inflation factor
    # c = q_a(|z|) / z_a for each nominal level a; no information from the forecast source is used.
    for m in ["B-RPM", "B-RPM-LOFO"]:
        g = ev[(ev.method == m) & ev.lo80.notna()].copy()
        sd = (g.hi80 - g.lo80) / (2 * norm.ppf(0.9)); z = (g.err / sd).abs()
        for a, nm in ((0.8, "80"), (0.95, "95")):
            za = norm.ppf(0.5 + a / 2)
            c = pd.Series({s_: float(z[g.source != s_].quantile(a)) / za for s_ in g.source.unique()})
            g["c" + nm] = (g.err.abs() <= g.source.map(c) * za * sd)
        g["wf80"] = np.exp(2 * g.source.map(pd.Series({s_: float(z[g.source != s_].quantile(0.8)) for s_ in g.source.unique()})) * sd)
        for key in ("fam", "n0"):
            for v, gg in g.groupby(key):
                tm = gg.groupby("task")[["c80", "c95"]].mean().mean()
                cov.append({"method": m + "-cal (post hoc)", "stratum": key, "value": v, "cov80": tm.c80, "cov95": tm.c95,
                            "median_width_factor80": float(gg.wf80.median()), "n_tasks": gg.task.nunique()})
        tm = g.groupby("task")[["c80", "c95"]].mean().mean()
        cov.append({"method": m + "-cal (post hoc)", "stratum": "all", "value": "all", "cov80": tm.c80, "cov95": tm.c95,
                    "median_width_factor80": float(g.wf80.median()), "n_tasks": g.task.nunique()})
    TB4 = pd.DataFrame(cov); num["TB4_coverage"] = TB4.to_dict("records")
    # information fraction as a reliability diagnostic (B-RPM)
    b = ev[ev.method == "B-RPM"].copy()
    b["info_tertile"] = pd.qcut(b.info_gain.clip(-1, 1), 3, labels=["low", "mid", "high"])
    TB7 = b.groupby("info_tertile", observed=True).agg(level_mae=("abs_err", "mean"), gain_mae=("gain_abs_err", "mean"),
                                                       info_median=("info_gain", "median"), n=("abs_err", "size")).reset_index()
    TB7b = b.groupby("n0").agg(info_median=("info_gain", "median")).reset_index()
    num["TB7_info_reliability"] = TB7.astype({"info_tertile": str}).to_dict("records"); num["TB7_info_by_n0"] = TB7b.to_dict("records")
    # signed bias by extrapolation ratio
    rb2 = pd.cut(ev.ratio, [1.5, 3, 6, 12, 24, 1e9], labels=["2", "4", "8", "16", ">=32"])
    TB8 = ev.assign(rb=rb2).groupby(["rb", "task", "method"], observed=True).err.mean().groupby(["rb", "method"], observed=True).mean().unstack()
    num["TB8_bias_by_ratio"] = TB8.reset_index().astype({"rb": str}).to_dict("records")
    # level endpoint under leave-one-family-out transfer (structural prior vs transferred slope)
    for ref, m in (("SLOPE-T-LOFO", "B-RPM-LOFO"), ("FLAT", "B-RPM-LOFO")):
        r_t = paired(lvl[m].values, lvl[ref].values)
        Ts = lvl[[ref, m]].groupby(src).mean(); r_s = paired(Ts[m].values, Ts[ref].values)
        out.append({"endpoint": "level", "method": m, "reference": ref, "task_mean_improvement": r_t["mean_diff"],
                    "task_ci_lo": r_t["lo"], "task_ci_hi": r_t["hi"], "task_p": r_t["p"], "task_wins": r_t["wins"], "n_tasks": r_t["n"],
                    "source_mean_improvement": r_s["mean_diff"], "source_p": r_s["p"], "source_wins": r_s["wins"], "n_sources": r_s["n"]})
    TB2 = pd.DataFrame(out); TB2["task_p_holm"] = holm(TB2.task_p.fillna(1).values)
    num["TB2_paired"] = TB2.to_dict("records")
    # HB4: identification set
    g = ev[(ev.method == "B-RPM") & ev.id_lo.notna()]
    g = g.assign(cid=(g.truth_ridge_logrmse >= g.id_lo) & (g.truth_ridge_logrmse <= g.id_hi), wid=np.exp(g.id_hi - g.id_lo))
    rb = pd.cut(g.ratio, [1.5, 3, 6, 12, 24, 1e9], labels=["2", "4", "8", "16", ">=32"])
    TB5 = g.groupby(rb, observed=True).agg(coverage=("cid", "mean"), median_width_factor=("wid", "median"),
                                            info_fraction_median=("info_gain", "median"), n=("cid", "size")).reset_index()
    TB5["by"] = "ratio"
    TB5b = g.groupby("n0").agg(coverage=("cid", "mean"), median_width_factor=("wid", "median"),
                               info_fraction_median=("info_gain", "median"), n=("cid", "size")).reset_index()
    num["TB5_idset_by_ratio"] = TB5.astype({"ratio": str}).to_dict("records"); num["TB5_idset_by_n0"] = TB5b.to_dict("records")
    num["idset_coverage_task_mean"] = float(g.groupby("task").cid.mean().mean())
    # probabilistic planning decision: P(RMSEP(n) <= 0.85 x pilot CV RMSEP) at n = 8 n0
    dec = []
    thr = np.log(0.85)
    d8 = ev[(ev.ratio == 8)]
    # calibrated Gaussian predictive for point forecasters: residual sd of log error from OTHER sources (LOSO)
    for m in ["B-RPM", "B-RPM-LOFO", "SLOPE-T", "SLOPE-T-LOFO", "FLAT", "RPM", "IPL3"]:
        g = d8[d8.method == m].copy()
        if not len(g):
            continue
        target = g.pilot_cv_logrmse + thr
        if m.startswith("B-RPM") or (m in ("RPM", "IPL3") and g.lo80.notna().all()):
            sd = (g.hi80 - g.lo80) / (2 * norm.ppf(0.9))
        else:
            sd = pd.Series([float(g[g.source != s].err.std()) for s in g.source], index=g.index)
        p = norm.cdf((target - g.fc_logrmse) / sd.clip(lower=1e-3))
        yv = (g.truth_ridge_logrmse <= target).astype(float)
        g = g.assign(p=p, y=yv, bs=(p - yv) ** 2)
        tb = g.groupby("task")[["bs", "y", "p"]].mean()
        dec.append({"method": m, "brier_task_mean": tb.bs.mean(), "prevalence": tb.y.mean(), "mean_prob": tb.p.mean(),
                    "brier_climatology": float(((tb.y.mean() - g.groupby("task").y.mean()) ** 2).mean() + (g.groupby("task").y.var(ddof=0)).mean())})
    TB6 = pd.DataFrame(dec); num["TB6_decision"] = TB6.to_dict("records")
    # posterior summaries
    pb = ev[ev.method == "B-RPM"].groupby("task")[["r_post_mean", "eta_post_mean", "r_post_sd"]].mean()
    num["brpm_r_post_median"] = float(pb.r_post_mean.median()); num["brpm_eta_post_median"] = float(pb.eta_post_mean.median())
    # LOFO prior vs posterior noise fraction for the soil tasks (mechanism of structural transfer)
    al = pd.read_csv(os.path.join(paths["results"], "alignment_exponents.csv"))
    soil = ev.fam == "soil"
    num["lofo_soil_eta_post_median"] = float(ev[soil & (ev.method == "B-RPM-LOFO")].groupby("task").eta_post_mean.mean().median())
    num["lofo_soil_eta_prior_median"] = float(al[al.family != "soil"].noise_frac_full_pool.median())
    num["soil_eta_large_sample_median"] = float(al[al.family == "soil"].noise_frac_full_pool.median())
    os.makedirs(tabs, exist_ok=True)
    for nm, t in (("TB1_brpm_summary", TB1), ("TB2_brpm_paired", TB2), ("TB3_brpm_by_family", TB3.reset_index()),
                  ("TB4_brpm_coverage", TB4), ("TB5_idset", pd.concat([TB5.astype({"ratio": str}), TB5b.assign(by="n0")])),
                  ("TB6_decision", TB6), ("TB7_info_reliability", TB7), ("TB8_bias_by_ratio", TB8.reset_index())):
        t.to_csv(os.path.join(tabs, nm + ".csv"), index=False)
    json.dump(num, open(os.path.join(paths["results"], "bayes_numbers.json"), "w"), indent=1, default=float)
    return num


if __name__ == "__main__":
    import sys
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sub = sys.argv[1] if len(sys.argv) > 1 else "results"
    paths = {"raw_out": os.path.join(root, sub, "raw"), "tables": os.path.join(root, "tables" if sub == "results" else sub + "/tables"),
             "results": os.path.join(root, sub)}
    n = run_bayes_analysis(paths)
    print(pd.DataFrame(n["TB1_summary"]).round(3).to_string())
