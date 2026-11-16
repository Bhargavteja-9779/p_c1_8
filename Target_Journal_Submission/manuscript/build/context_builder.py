"""Derive every number quoted in the manuscript from machine-generated result files.

`build_context(numbers, RES, TAB)` returns a flat dict of formatted strings; the manuscript text uses
only these keys ({{key}} placeholders). Nothing here is typed by hand: each value is read from
results/numbers.json, results/*.csv or tables/*.csv.
"""
import json
import os

import numpy as np
import pandas as pd


def f3(x):
    return f"{x:.3f}"


def f2(x):
    return f"{x:.2f}"


def pct(x, d=0):
    return f"{x:.{d}f}%"


def pfmt(p):
    if p < 1e-4:
        return "< 0.0001"
    return f"= {p:.4f}" if p < 0.01 else f"= {p:.3f}"


def build_context(numbers, RES, TAB):
    c = {}
    T1 = pd.read_csv(os.path.join(TAB, "T1_tasks.csv"))
    T2 = pd.read_csv(os.path.join(TAB, "T2_main_accuracy_ridge_truth.csv")).set_index("method")
    T3 = pd.read_csv(os.path.join(TAB, "T3_stats_rpm_vs_baselines.csv")).set_index("comparison")
    T4 = pd.read_csv(os.path.join(TAB, "T4_main_accuracy_pls_truth.csv")).set_index("method")
    T5 = pd.read_csv(os.path.join(TAB, "T5_interval_coverage.csv"))
    T6 = pd.read_csv(os.path.join(TAB, "T6_sample_size_decisions.csv"))
    T7 = pd.read_csv(os.path.join(TAB, "T7_ablation.csv")).set_index("variant")
    T9 = pd.read_csv(os.path.join(TAB, "T9_theory_validity_full_pool_fit.csv"))
    T10 = pd.read_csv(os.path.join(TAB, "T10_runtime.csv"))
    al = pd.read_csv(os.path.join(RES, "alignment_exponents.csv"))
    c["n_tasks"] = str(len(T1))
    fam = T1.family.value_counts()
    c["n_soil"] = str(int(fam.get("soil", 0)))
    c["n_pilots_total"] = f"{numbers['n_pilots_total']:,}"
    c["n_forecasts"] = f"{numbers['n_forecast_rows']:,}"
    # RQ1 theory validity
    fr = T9[T9["mode"] == "free"]; f1 = T9[T9["mode"] == "fixed1"]
    c["tv_ridge_mean"] = f3(fr.mean_abs_err_ridge.mean()); c["tv_ridge_median"] = f3(fr.mean_abs_err_ridge.median())
    c["tv_pls_mean"] = f3(fr.mean_abs_err_pls.mean()); c["tv_pls_median"] = f3(fr.mean_abs_err_pls.median())
    c["tv_ridge_mean_r1"] = f3(f1.mean_abs_err_ridge.mean()); c["tv_pls_mean_r1"] = f3(f1.mean_abs_err_pls.mean())
    worst = fr.sort_values("mean_abs_err_ridge", ascending=False).head(3)
    c["tv_worst"] = ", ".join(f"{t} ({v:.2f})" for t, v in zip(worst.task, worst.mean_abs_err_ridge))
    p9b = os.path.join(TAB, "T9b_kappa_collapse_dispersion.csv")
    if os.path.exists(p9b):
        cd = pd.read_csv(p9b)
        c["collapse_sd"] = f3(cd.collapse_sd_log.median()); c["collapse_ref"] = f3(cd.no_collapse_ref_sd_log.median()); c["collapse_n"] = str(len(cd))
    # alignment exponents
    c["r_median"] = f2(al.r_full_pool.median()); c["r_q1"] = f2(al.r_full_pool.quantile(0.25)); c["r_q3"] = f2(al.r_full_pool.quantile(0.75))
    c["r_min"] = f2(al.r_full_pool.min()); c["r_max"] = f2(al.r_full_pool.max())
    vis = al[al.task.str.contains("VisNIR|Neospectra|Mango")]; mir = al[al.task.str.contains("MIR")]
    c["r_vis_median"] = f2(vis.r_full_pool.median()); c["r_mir_median"] = f2(mir.r_full_pool.median())
    c["r_loso_min"] = f2(al.r_loso_prior.min()); c["r_loso_max"] = f2(al.r_loso_prior.max())
    c["n_r_below_1"] = str(int((al.r_full_pool < 1).sum()))
    # main accuracy (ridge truth)
    for m in T2.index:
        k = m.replace("-", "_")
        c[f"mae_{k}"] = f3(T2.loc[m, "mean_abs_logerr"]); c[f"mae_{k}_lo"] = f3(T2.loc[m, "ci95_lo"]); c[f"mae_{k}_hi"] = f3(T2.loc[m, "ci95_hi"])
        c[f"medae_{k}"] = f3(T2.loc[m, "median_task_abs_logerr"]); c[f"bias_{k}"] = f"{T2.loc[m, 'mean_bias']:+.3f}"
        c[f"w20_{k}"] = pct(T2.loc[m, "pct_within_20"]); c[f"w10_{k}"] = pct(T2.loc[m, "pct_within_10"])
    for m in T3.index:
        k = m.replace("-", "_")
        c[f"st_{k}_diff"] = f3(T3.loc[m, "median_diff"]); c[f"st_{k}_lo"] = f3(T3.loc[m, "ci95_lo"]); c[f"st_{k}_hi"] = f3(T3.loc[m, "ci95_hi"])
        c[f"st_{k}_p"] = pfmt(T3.loc[m, "p_holm"]); c[f"st_{k}_rb"] = f2(T3.loc[m, "rank_biserial"])
        c[f"st_{k}_wins"] = str(int(T3.loc[m, "ref_wins"])); c[f"st_{k}_losses"] = str(int(T3.loc[m, "ref_losses"]))
    for m in T4.index:
        k = m.replace("-", "_")
        c[f"pls_mae_{k}"] = f3(T4.loc[m, "mean_abs_logerr"]); c[f"pls_bias_{k}"] = f"{T4.loc[m, 'mean_bias']:+.3f}"
    # coverage
    for _, r in T5.iterrows():
        k = r.method.replace("-", "_")
        c[f"cov{int(r.nominal)}_{k}"] = pct(r.coverage_rows, 1)
        c[f"covw{int(r.nominal)}_{k}"] = f2(r.mean_width_factor)
    # decisions
    for _, r in T6.iterrows():
        k = r.method.replace("-", "_")
        c[f"dec_{r.target}_{k}"] = pct(r.pct_within_factor2, 1)
        c[f"decfail_{r.target}_{k}"] = pct(r.pct_never_reaches_target, 1)
    # ablation (r = 1 variants)
    for v in T7.index:
        k = v.replace("-", "_").replace("+", "p").replace(".", "")
        c[f"abl_{k}"] = f3(T7.loc[v, "mean_abs_logerr"])
        if v != "RPM":
            c[f"abl_{k}_diff"] = f"{T7.loc[v, 'mean_diff_vs_rpm']:+.3f}"
            c[f"abl_{k}_p"] = pfmt(T7.loc[v, "p_holm"]) if not pd.isna(T7.loc[v, "p_holm"]) else "n/a"
    c["abl_rpm_subset"] = f3(T7.loc["RPM", "mean_abs_logerr"])
    # runtime
    c["t_rpm_mean"] = f2(T10.iloc[0]["mean"]); c["t_curve_mean"] = f2(T10.iloc[1]["mean"])
    # optional blocks
    p = os.path.join(TAB, "T7b_ablation_eigenspectrum_rpmT.csv")
    if os.path.exists(p):
        T7b = pd.read_csv(p).set_index("variant")
        for v in T7b.index:
            k = v.replace("-", "_").replace("+", "p")
            c[f"ablT_{k}"] = f3(T7b.loc[v, "mean_abs_logerr"])
            if v != "RPM-T":
                c[f"ablT_{k}_p"] = pfmt(T7b.loc[v, "p_holm"]); c[f"ablT_{k}_diff"] = f"{T7b.loc[v, 'median_diff']:+.3f}"
    p = os.path.join(TAB, "T14_posthoc_gain_and_decision.csv")
    if os.path.exists(p):
        T14 = pd.read_csv(p).set_index("method")
        for m in T14.index:
            k = m.replace("-", "_")
            c[f"gain_{k}"] = f3(T14.loc[m, "mean_task_gain_abs_err"]); c[f"gainbias_{k}"] = f"{T14.loc[m, 'mean_gain_bias']:+.3f}"
            c[f"gdec_{k}"] = f2(T14.loc[m, "decision_8x_10pct_balanced_acc"])
        c["gain_prev"] = pct(100 * T14.prevalence_worthwhile.dropna().iloc[0])
        T14s = pd.read_csv(os.path.join(TAB, "T14b_posthoc_gain_stats.csv")).set_index("comparison")
        for m in T14s.index:
            k = m.replace("-", "_")
            c[f"gst_{k}_p"] = pfmt(T14s.loc[m, "p_holm"]); c[f"gst_{k}_diff"] = f3(T14s.loc[m, "median_diff"])
            c[f"gst_{k}_wins"] = str(int(T14s.loc[m, "ref_wins"])); c[f"gst_{k}_losses"] = str(int(T14s.loc[m, "ref_losses"]))
    p = os.path.join(TAB, "T0b_simulation_by_n0.csv")
    if os.path.exists(p):
        T0 = pd.read_csv(p)
        for _, r in T0.iterrows():
            k = r.method.replace("-", "_")
            c[f"sim_{k}_{int(r.n0)}"] = f3(r.median_abs_err); c[f"simb_{k}_{int(r.n0)}"] = f"{r.median_bias:+.3f}"
    p = os.path.join(TAB, "T8_robustness.csv")
    if os.path.exists(p):
        T8 = pd.read_csv(p)
        for _, r in T8.iterrows():
            k = f"{r.variant}_{r.method}".replace("-", "_").replace(".", "")
            c[f"rob_{k}"] = f3(r.mean_abs_logerr); c[f"robb_{k}"] = f"{r.mean_bias:+.3f}"
            c[f"robc_{k}"] = pct(r.coverage80, 0) if not pd.isna(r.coverage80) else "–"
    ps = os.path.join(RES, "simulation_raw.csv")
    if os.path.exists(ps):
        sm = pd.read_csv(ps); sm["ae"] = sm.err.abs()
        def med(q, col="ae"):
            return float(sm.query(q)[col].median())
        for rv, tag in ((0.5, "r05"), (1.0, "r1"), (2.0, "r2")):
            for m in ("RPM", "RPM-w", "RPM-T", "IPL3", "FLAT"):
                k = m.replace("-", "_")
                c[f"sim_{tag}_{k}"] = f3(med(f"r == {rv} and method == '{m}'"))
                c[f"simbias_{tag}_{k}"] = f"{med(f'r == {rv} and method == {chr(39)}{m}{chr(39)}', 'err'):+.3f}"
        for n0 in sorted(sm.n0.unique()):
            for m in ("RPM", "RPM-w", "RPM-T", "IPL3", "FLAT"):
                c[f"simn0_{int(n0)}_{m.replace('-', '_')}"] = f3(med(f"n0 == {n0} and method == '{m}'"))
    # post-hoc tables
    p = os.path.join(TAB, "T3c_posthoc_stats_slopeT_reference.csv")
    if os.path.exists(p):
        t = pd.read_csv(p).set_index("comparison")
        for m in t.index:
            k = m.replace("-", "_")
            c[f"stS_{k}_p"] = pfmt(t.loc[m, "p_holm"]); c[f"stS_{k}_diff"] = f"{t.loc[m, 'median_diff']:+.3f}"
            c[f"stS_{k}_wins"] = str(int(t.loc[m, "ref_wins"])); c[f"stS_{k}_losses"] = str(int(t.loc[m, "ref_losses"]))
    p = os.path.join(TAB, "T16_posthoc_loso_conformal_bands.csv")
    if os.path.exists(p):
        t = pd.read_csv(p)
        for _, r in t.iterrows():
            k = r.method.replace("-", "_")
            c[f"conf{int(r.nominal)}_{k}"] = pct(r.coverage_pct, 1); c[f"confw{int(r.nominal)}_{k}"] = f2(r.median_width_factor)
    for key in ("slope_median", "slope_q1", "slope_q3", "slope_min", "slope_max", "slope_ols_r2"):
        if key in numbers:
            c[key] = f3(numbers[key]) if "r2" not in key else f2(numbers[key])
    if "slope_median" in numbers:
        c["slope_pct_per_doubling"] = pct(100 * (1 - np.exp(numbers["slope_median"])), 1)
        c["slope_ols_p_noise"] = pfmt(numbers["slope_ols_p_noise"])
        sp = {d["descriptor"]: d for d in numbers.get("slope_spearman", [])}
        if "noise_frac_full_pool" in sp:
            c["slope_rho_noise"] = f"{sp['noise_frac_full_pool']['spearman_rho']:+.2f}"; c["slope_p_noise"] = pfmt(sp["noise_frac_full_pool"]["p"])
    p = os.path.join(TAB, "T17b_slope_by_region.csv")
    if os.path.exists(p):
        t = pd.read_csv(p).set_index("region")
        for reg, key in (("MIR (soil)", "mir"), ("Vis/NIR (soil)", "vis"), ("CGL", "cgl"), ("Tecator", "tecator"), ("Diesel", "diesel"), ("Mango", "mango"), ("Tablets", "tablets")):
            if reg in t.index:
                c[f"slope_reg_{key}"] = f3(t.loc[reg, "median"])
    p = os.path.join(TAB, "T18_posthoc_by_ratio_stratum.csv")
    if os.path.exists(p):
        t = pd.read_csv(p)
        for _, r in t.iterrows():
            st_ = "short" if "<=" in r.stratum else "long"
            k = r.method.replace("-", "_")
            c[f"strat_{st_}_{k}"] = f3(r.mean_task_mean_abs); c[f"stratmed_{st_}_{k}"] = f3(r.mean_task_median_abs)
            if not pd.isna(r.get("p_holm", np.nan)):
                c[f"strat_{st_}_{k}_p"] = pfmt(r.p_holm); c[f"strat_{st_}_{k}_wins"] = str(int(r.RPMw_wins)); c[f"strat_{st_}_{k}_losses"] = str(int(r.RPMw_losses))
            c[f"strat_{st_}_ntasks"] = str(int(r.n_tasks))
    S0 = pd.read_csv(os.path.join(TAB, "S0_stats_excluding_ICRAF_VisNIR.csv")).set_index("comparison")
    for m in S0.index:
        c[f"s0_{m.replace('-', '_')}_p"] = pfmt(S0.loc[m, "p_holm"])
    return c
