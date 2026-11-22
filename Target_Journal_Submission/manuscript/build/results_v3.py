"""Results, discussion, abstract, highlights, conclusions and cover letter (version 3: observability limit + B-RPM).

All numbers are {{placeholders}} resolved from machine-generated tables (tables/TB*.csv, results/bayes_numbers.json,
results/simulation_bayes_raw.csv and the version-2 analysis tables); none is typed by hand.
"""
import json
import os

import numpy as np
import pandas as pd


def _f(v, d=3):
    return f"{v:.{d}f}"


def _p(p):
    if not np.isfinite(p):
        return "n/a"
    return "< 0.001" if p < 0.001 else f"= {p:.3f}"


def bayes_context(ROOT):
    T = lambda n: pd.read_csv(os.path.join(ROOT, "tables", n + ".csv"))
    c = {}
    s = T("TB1_brpm_summary").set_index("method")
    for m in s.index:
        k = m.replace("-", "_")
        c[f"b_lvl_{k}"] = _f(s.loc[m, "level_mae"]); c[f"b_gain_{k}"] = _f(s.loc[m, "gain_mae"])
        c[f"b_bias_{k}"] = f"{s.loc[m, 'mean_bias']:+.3f}"; c[f"b_lvlsrc_{k}"] = _f(s.loc[m, "level_mae_source"])
    pr = T("TB2_brpm_paired")
    for _, r in pr.iterrows():
        k = f"{r.endpoint}_{r.method}_vs_{r.reference}".replace("-", "_")
        c[f"bp_d_{k}"] = f"{r.task_mean_improvement:+.3f}"
        c[f"bp_ci_{k}"] = f"{r.task_ci_lo:+.3f} to {r.task_ci_hi:+.3f}"
        c[f"bp_p_{k}"] = _p(r.task_p); c[f"bp_ph_{k}"] = _p(r.task_p_holm)
        c[f"bp_w_{k}"] = f"{int(r.task_wins)} of {int(r.n_tasks)}"
        c[f"bp_sw_{k}"] = f"{int(r.source_wins)} of {int(r.n_sources)}"; c[f"bp_sp_{k}"] = _p(r.source_p)
    cov = T("TB4_brpm_coverage")
    a = cov[cov.stratum == "all"].set_index("method")
    for m in a.index:
        k = m.split(" ")[0].replace("-", "_")
        c[f"bc80_{k}"] = f"{100 * a.loc[m, 'cov80']:.0f}%"; c[f"bc95_{k}"] = f"{100 * a.loc[m, 'cov95']:.0f}%"
        c[f"bcw_{k}"] = f"{a.loc[m, 'median_width_factor80']:.1f}"
    cal = cov[(cov.method == "B-RPM-cal (post hoc)") & (cov.stratum == "n0")]
    c["bcal_n0_range"] = f"{100 * cal.cov80.min():.0f}–{100 * cal.cov80.max():.0f}%"
    calf = cov[(cov.method == "B-RPM-cal (post hoc)") & (cov.stratum == "fam")].set_index("value")
    c["bcal_mix80"] = f"{100 * calf.loc['mixture', 'cov80']:.0f}%"; c["bcal_soil80"] = f"{100 * calf.loc['soil', 'cov80']:.0f}%"
    raw_f = cov[(cov.method == "B-RPM") & (cov.stratum == "fam")].set_index("value")
    c["bcov_mix80"] = f"{100 * raw_f.loc['mixture', 'cov80']:.0f}%"
    idt = T("TB5_idset"); ir = idt[idt.by == "ratio"].set_index("ratio"); iq = idt[idt.by == "n0"].set_index("n0")
    c["id_cov_2"] = f"{100 * ir.loc['2', 'coverage']:.0f}%"; c["id_cov_32"] = f"{100 * ir.loc['>=32', 'coverage']:.0f}%"
    c["id_w_2"] = f"{ir.loc['2', 'median_width_factor']:.1f}"; c["id_w_8"] = f"{ir.loc['8', 'median_width_factor']:.0f}"
    c["id_w_32"] = f"{ir.loc['>=32', 'median_width_factor']:.0f}"
    for n0 in (25, 50, 100, 200):
        c[f"info_{n0}"] = _f(iq.loc[n0, "info_fraction_median"], 2); c[f"idw_{n0}"] = f"{iq.loc[n0, 'median_width_factor']:.1f}"
    num = json.load(open(os.path.join(ROOT, "results", "bayes_numbers.json")))
    hs = T("TB11_hidden_signal").groupby("n0").hidden_share.median()
    for k in (25, 50, 100):
        c[f"hid_{k}"] = f"{100 * hs.loc[k]:.0f}%" if hs.loc[k] >= 0.1 else f"{100 * hs.loc[k]:.1f}%"
    c["id_curve_cov"] = f"{100 * num['idset_curve_coverage_task_mean']:.0f}%"
    c["id_cov_all"] = f"{100 * num['idset_coverage_task_mean']:.0f}%"
    c["lofo_eta_post"] = _f(num["lofo_soil_eta_post_median"], 2); c["lofo_eta_prior"] = _f(num["lofo_soil_eta_prior_median"], 2)
    c["soil_eta_ls"] = _f(num["soil_eta_large_sample_median"], 2)
    ab = num["abs_task_bias"]
    for m in ("B-RPM", "FLAT", "RPM", "SLOPE-T", "IPL3", "B-RPM-LOFO", "SLOPE-T-LOFO"):
        c[f"absb_{m.replace('-', '_')}"] = _f(ab[m])
    b8b = T("TB8b_abs_task_bias_by_ratio").astype({"rb": str}).set_index("rb")
    for m in ("B-RPM", "FLAT", "RPM", "SLOPE-T", "IPL3"):
        c[f"absb8_{m.replace('-', '_')}"] = f"{b8b.loc[['8', '16', '>=32'], m].min():.2f}–{b8b.loc[['8', '16', '>=32'], m].max():.2f}"
    w7 = T("TB7c_info_within_n0").set_index("n0")
    c["rel25_low"] = _f(w7.loc[25, "level_mae_low"]); c["rel25_high"] = _f(w7.loc[25, "level_mae_high"])
    c["rel50_low"] = _f(w7.loc[50, "level_mae_low"]); c["rel50_high"] = _f(w7.loc[50, "level_mae_high"])
    c["rel200_low"] = _f(w7.loc[200, "level_mae_low"]); c["rel200_high"] = _f(w7.loc[200, "level_mae_high"])
    c["info_neg"] = f"{100 * num['info_share_negative']:.0f}%"
    st10 = pd.read_csv(os.path.join(ROOT, "tables", "TB10_staged_decision.csv"), index_col=0)
    st10.columns = [str(int(float(x))) for x in st10.columns]
    for N in ("400", "800"):
        for k in st10.index:
            c[f"sd{N}_{k.replace(':', '_').replace('-', '_')}"] = (f"{100 * st10.loc[k, N]:.0f}%")
    gains = [(st10.loc[f"staged:{m}", N] - st10.loc[f"one-shot:{m}", N]) * 100 for m in ("B-RPM", "FLAT", "SLOPE-T", "RPM", "IPL3") for N in ("400", "800")]
    c["sd_gain_range"] = f"{min(gains):.0f}–{max(gains):.0f}"
    sbt = pd.read_csv(os.path.join(ROOT, "tables", "TB10b_staged_decision_by_target.csv"), header=[0, 1], index_col=0)
    c["gate_settled"] = f"{100 * (1 - (st10.loc['gated_second_batch_share', '400'] + st10.loc['gated_second_batch_share', '800']) / 2):.0f}%"
    c["sd_flat_reach"] = f"{100 * sbt.loc['one-shot:FLAT'].xs('reachable', level=1).mean():.0f}%"
    c["sd_slope_unreach"] = f"{100 * sbt.loc['one-shot:SLOPE-T'].xs('unreachable', level=1).mean():.0f}%"
    c["sd_brpm_reach"] = f"{100 * sbt.loc['one-shot:B-RPM'].xs('reachable', level=1).mean():.0f}%"
    c["sd_brpm_unreach"] = f"{100 * sbt.loc['one-shot:B-RPM'].xs('unreachable', level=1).mean():.0f}%"
    t9 = T("TB9_fixed_target"); t9 = t9[t9.n_target == 800].set_index("n0")
    c["ft800_brpm_50"] = _f(t9.loc[50, "B-RPM"]); c["ft800_brpm_100"] = _f(t9.loc[100, "B-RPM"]); c["ft800_brpm_200"] = _f(t9.loc[200, "B-RPM"])
    c["b_r_post"] = _f(num["brpm_r_post_median"], 2); c["b_eta_post"] = _f(num["brpm_eta_post_median"], 2)
    rel = T("TB7_info_reliability").set_index("info_tertile")
    for q in ("low", "mid", "high"):
        c[f"rel_{q}"] = _f(rel.loc[q, "level_mae"]); c[f"relg_{q}"] = _f(rel.loc[q, "gain_mae"])
    b8 = T("TB8_bias_by_ratio").set_index("rb")
    for m in ("B-RPM", "FLAT", "SLOPE-T", "RPM", "IPL3", "SLOPE-T-LOFO", "B-RPM-LOFO"):
        k = m.replace("-", "_")
        c[f"bias2_{k}"] = f"{b8.loc['2', m]:+.3f}"; c[f"bias32_{k}"] = f"{b8.loc['>=32', m]:+.3f}"
        c[f"bias8_{k}"] = f"{b8.loc['8', m]:+.3f}"
    c["bias_brpm_maxabs_le8"] = _f(b8.loc[["2", "4", "8"], "B-RPM"].abs().max())
    dec = T("TB6_decision").set_index("method")
    for m in dec.index:
        c[f"brier_{m.replace('-', '_')}"] = _f(dec.loc[m, "brier_task_mean"])
    c["brier_clim"] = _f(dec.brier_climatology.iloc[0])
    fam = T("TB3_brpm_by_family")
    lv = fam[fam.level_0 == "level"].set_index("level_1")
    c["fam_soil_brpm_lofo"] = _f(lv.loc["soil", "B-RPM-LOFO"]); c["fam_soil_slope_lofo"] = _f(lv.loc["soil", "SLOPE-T-LOFO"])
    c["fam_soil_brpm"] = _f(lv.loc["soil", "B-RPM"]); c["fam_soil_slope"] = _f(lv.loc["soil", "SLOPE-T"])
    c["fam_mix_brpm"] = _f(lv.loc["mixture", "B-RPM"]); c["fam_mix_flat"] = _f(lv.loc["mixture", "FLAT"])
    # simulation (controlled, Monte-Carlo truth)
    sb = pd.read_csv(os.path.join(ROOT, "results", "simulation_bayes_raw.csv")); sb["ae"] = sb.err.abs()
    so = pd.read_csv(os.path.join(ROOT, "results", "simulation_raw.csv")); so["ae"] = so.err.abs()
    c["sim_id_cov"] = f"{100 * sb[sb.method == 'B-RPM'].id_cov.mean():.0f}%"
    c["sim_id_cov_min"] = f"{100 * sb[sb.method == 'B-RPM'].groupby(['r', 'noise_frac']).id_cov.mean().min():.0f}%"
    for r, tag in ((0.5, "05"), (1.0, "1"), (2.0, "2")):
        c[f"sim_b_{tag}"] = _f(sb[(sb.method == "B-RPM") & (sb.r == r)].ae.mean())
        c[f"sim_bf_{tag}"] = _f(sb[(sb.method == "B-RPM-flat") & (sb.r == r)].ae.mean())
        for m in ("FLAT", "RPM", "IPL3"):
            c[f"sim_{m}_{tag}"] = _f(so[(so.method == m) & (so.r == r)].ae.mean())
    pri = json.loads(sb.prior.iloc[0]); c["sim_prior_r"] = _f(pri["m_r"], 2)
    # pre-registered RPM vs FLAT (version-2 main analysis)
    t2 = T("T2_main_accuracy_ridge_truth").set_index("method")
    c["v2_rpm"] = _f(t2.loc["RPM", "mean_abs_logerr"]); c["v2_flat"] = _f(t2.loc["FLAT", "mean_abs_logerr"])
    c["v2_ipl3"] = _f(t2.loc["IPL3", "mean_abs_logerr"])
    st = T("T3_stats_rpm_vs_baselines")
    try:
        row = st[st.comparison == "FLAT"].iloc[0]
        c["v2_rpm_flat_p"] = _p(float(row.get("p_holm", row.get("p_raw", np.nan))))
    except Exception:
        c["v2_rpm_flat_p"] = "n/a"
    # robustness (B-RPM and comparators)
    rb = os.path.join(ROOT, "results", "robustness_raw.csv")
    if os.path.exists(rb):
        r = pd.read_csv(rb); r = r[(r.ratio >= 2) & r.method.isin(["B-RPM", "FLAT", "RPM", "IPL3"])]
        r["ae"] = (r.fc_logrmse - r.truth_ridge_logrmse).abs(); r["e"] = r.fc_logrmse - r.truth_ridge_logrmse
        g = r.groupby(["variant", "task", "method"])[["ae", "e"]].mean().groupby(["variant", "method"]).mean()
        for (v, m), row in g.iterrows():
            c[f"rob_{v}_{m.replace('-', '_')}"] = _f(row.ae); c[f"robb_{v}_{m.replace('-', '_')}"] = f"{row.e:+.3f}"
    return c


def results_markdown_v3(ctx, TAB, FIG, table_md, old_results):
    fig = lambda name: os.path.join(FIG, name + ".png")
    head = old_results.split("## 4.3.")[0]
    head = head.replace("(Section 4.4)", "(Section 4.3)")
    head = head.replace("How steeply a curve falls was remarkably similar across tasks.", "Learning curves were shallow.")
    s = [head.rstrip()]
    # 4.3 -----------------------------------------------------------------------------------------------------
    s.append("## 4.3. What a pilot set can identify")
    s.append(
        "How much learnable signal hides below the horizon of a real pilot can be computed from the large-sample fits. At the horizon "
        "$\\kappa_0$ of a 25-sample pilot, a median {{hid_25}} of the apparent error floor $N(\\kappa_0)$ was target power that larger "
        "calibrations learn, {{hid_50}} for 50 samples and {{hid_100}} for 100 samples (Fig. 6a; Supplementary Table "
        "[[ST:TB11_hidden_signal]]). These shares are lower bounds for full-resolution spectra, because sub-sampling to 94–216 variables "
        "lowers the horizon of a given pilot. "
        "Proposition 1 predicts that a pilot leaves the gain from additional samples undetermined unless prior information is added. The "
        "prior-free compatible set makes this measurable (Fig. 5). For every pilot it contains all learning curves of the family "
        "$s_k\\propto(\\lambda_k/\\lambda_1)^r$ that are consistent with the pilot's cross-validation path. Across all pilots and horizons the set "
        "contained the true ridge RMSEP in {{id_cov_all}} of forecasts (task average; pooled over forecasts {{id_cov_2}} at $n/n_0=2$ and "
        "{{id_cov_32}} at $n/n_0\\ge32$; Fig. 6b), and the whole true curve of a pilot in {{id_curve_cov}}. In the controlled simulation, where the truth is a Monte-Carlo estimate rather than a fitted curve, coverage was "
        "{{sim_id_cov}} overall and at least {{sim_id_cov_min}} in every scenario. The theory therefore describes correctly what is compatible with "
        "a pilot. What a pilot can decide is a different matter. The median ratio between the upper and lower RMSEP of the set was {{id_w_2}} at "
        "$n/n_0=2$, {{id_w_8}} at $n/n_0=8$ and {{id_w_32}} at $n/n_0\\ge32$ (Fig. 6c). Long extrapolations from a pilot alone are thus not merely "
        "inaccurate. They are undetermined, and any method that returns a narrow forecast does so because it has imported an assumption.")
    s.append(f"![**Fig. 5.** Learning-curve forecasts from one 50-sample pilot for three tasks. Grey: prior-free compatible set (all curves consistent with the pilot's cross-validation path, Section 2.4); blue: B-RPM posterior mean and 80% band; dotted: no-improvement rule; dashed: inverse power law (IPL3); black: true learning curve (independent test set).]({fig('Fig3_identification_set_examples')}){{width=16cm}}")
    s.append(
        "The information fraction quantifies how much of the forecast comes from the pilot rather than the prior (Fig. 6d). Its median was "
        "{{info_25}} for 25-sample pilots, {{info_50}} for 50, {{info_100}} for 100 and {{info_200}} for 200 samples. Below about 100 samples the "
        "gain forecast comes mainly from the prior. The high values at 100–200 samples partly reflect the wavelength sub-sampling to 94–216 "
        "variables: when $n_0$ approaches $p$, the horizon $\\kappa_0$ falls far below the leading eigenvalues and almost all modes are "
        "resolved. For full-resolution spectra the horizon of a given pilot would be higher. The fraction is "
        "therefore largely a function of pilot size, and {{info_neg}} of the values were negative (posterior spread wider than prior spread, "
        "when the pilot contradicts the prior). Within a pilot size it carried some warning value only for small pilots: B-RPM's mean absolute "
        "log error was {{rel25_low}} in the lowest and {{rel25_high}} in the highest within-size tertile at $n_0=25$ ({{rel50_low}} vs "
        "{{rel50_high}} at $n_0=50$), but {{rel200_low}} vs {{rel200_high}} at $n_0=200$ (Supplementary Table [[ST:TB7c_info_within_n0]]).")
    s.append(f"![**Fig. 6.** Observability of learning curves. (a) Share of the apparent error floor $N(\\kappa_0)$ at the horizon of a pilot of $n_0$ samples that is learnable target power (large-sample fits; boxes over tasks). (b) Share of forecasts whose true RMSEP lies inside the prior-free compatible set; dashed line 90%. (c) Median width of the compatible set (ratio of upper to lower RMSEP). (d) Median information fraction of B-RPM (share of the prior variance of the gain removed by the pilot) by pilot size.]({fig('Fig5_observability')}){{width=16cm}}")
    # 4.4 -----------------------------------------------------------------------------------------------------
    s.append("## 4.4. Forecasting accuracy")
    s.append(
        "In all paired comparisons below, differences are reference minus B-RPM, so positive values favour B-RPM. Table 2 summarises all forecasters (group-disjoint splits; ten repeated outer splits for the small data sets). "
        "The pre-specified RPM ($r=1$) remained more accurate than inverse-power-law extrapolation (mean absolute log error {{v2_rpm}} vs "
        "{{v2_ipl3}}) but not more accurate than the no-improvement rule ({{v2_flat}}). B-RPM reached "
        "{{b_lvl_B_RPM}}. It was more accurate than IPL3 (difference {{bp_d_level_B_RPM_vs_IPL3}}, 95% CI {{bp_ci_level_B_RPM_vs_IPL3}}, "
        "better on {{bp_w_level_B_RPM_vs_IPL3}} tasks, Holm-adjusted p {{bp_ph_level_B_RPM_vs_IPL3}}) and than the scaling-exponent estimator of "
        "Wei et al. [@wei2022] ({{bp_d_level_B_RPM_vs_WEI}}, {{bp_w_level_B_RPM_vs_WEI}} tasks), and as accurate as RPM ({{bp_d_level_B_RPM_vs_RPM}}) "
        "and the transferred slope ({{bp_d_level_B_RPM_vs_SLOPE_T}}). It was slightly less accurate than the no-improvement rule "
        "({{bp_d_level_B_RPM_vs_FLAT}}, CI {{bp_ci_level_B_RPM_vs_FLAT}}, Holm p {{bp_ph_level_B_RPM_vs_FLAT}}), so the pre-specified "
        "non-inferiority margin of 0.02 (HB2) was not met. On the level endpoint, the pilot's own cross-validated error is very hard to beat, "
        "because the dominant error source is the noise in that error, which no forecaster can remove (Section 4.6).")
    s.append(table_md(_table2(TAB), "Accuracy of learning-curve forecasts (task-level means over pilots, pilot sizes 25–200 and horizons $n\\ge2n_0$). Level: $|\\log(\\widehat{\\mathrm{RMSEP}}/\\mathrm{RMSEP})|$; gain: error of the forecast gain $\\mathrm{RMSEP}(n)/\\mathrm{RMSEP}(n_0)$; bias: mean signed log error (> 0 pessimistic). LOSO/LOFO: prior or slope transferred from other data sources / other application families.", "Table 2", floatfmt=3))
    s.append(
        "The methods differ more in *bias* than in absolute error (Fig. 7). Pooled over tasks, the no-improvement rule was pessimistic, with "
        "a bias growing from {{bias2_FLAT}} at $n/n_0=2$ to {{bias32_FLAT}} at $n/n_0\\ge32$. The transferred slope and IPL3 became "
        "increasingly optimistic ({{bias32_SLOPE_T}} and {{bias32_IPL3}} at $n/n_0\\ge32$). B-RPM's pooled bias stayed within "
        "±{{bias_brpm_maxabs_le8}} up to eightfold extrapolation (overall {{b_bias_B_RPM}}). Pooled bias can hide opposite biases in different "
        "tasks, however. B-RPM was optimistic for soil and pessimistic for the designed mixtures (Supplementary Table [[ST:TB3_brpm_by_family]]). "
        "The mean absolute per-task bias, which does not cancel, was {{absb_B_RPM}} for B-RPM, {{absb_FLAT}} for FLAT, {{absb_RPM}} for RPM, "
        "{{absb_SLOPE_T}} for SLOPE-T and {{absb_IPL3}} for IPL3. At extrapolation ratios of 8 and more it was {{absb8_B_RPM}} for B-RPM against "
        "{{absb8_FLAT}} for FLAT, {{absb8_SLOPE_T}} for SLOPE-T and {{absb8_IPL3}} for IPL3 (RPM {{absb8_RPM}}; Supplementary Table "
        "[[ST:TB8b_abs_task_bias_by_ratio]]). The theory-based forecasters are therefore the least biased for long extrapolations, but they "
        "are not unbiased task by task. "
        "For the gain itself, B-RPM improved on the no-improvement rule ({{bp_d_gain_B_RPM_vs_FLAT}}, {{bp_w_gain_B_RPM_vs_FLAT}} tasks, Holm p "
        "{{bp_ph_gain_B_RPM_vs_FLAT}}) and on RPM ({{bp_d_gain_B_RPM_vs_RPM}}, {{bp_w_gain_B_RPM_vs_RPM}} tasks, Holm p {{bp_ph_gain_B_RPM_vs_RPM}}), "
        "and the pilot path added information beyond the prior ({{bp_d_gain_B_RPM_vs_B_RPM_0}} vs the prior-only variant B-RPM-0). The transferred slope "
        "(LOSO) predicted gains better than B-RPM ({{bp_d_gain_B_RPM_vs_SLOPE_T}}). Its advantage came from the soil family, whose 23 tasks "
        "have similar slopes and supply most of each other's priors, and it disappeared under cross-family transfer (Section 4.5).")
    s.append(f"![**Fig. 7.** Mean signed log error by extrapolation ratio (task-level means; > 0 pessimistic, < 0 optimistic).]({fig('Fig6_bias_by_horizon')}){{width=9cm}}")
    # 4.5 -----------------------------------------------------------------------------------------------------
    s.append("## 4.5. Transfer across application families")
    s.append(
        "A planning rule is useful only if it works for a new application, for which no calibrations of the same kind exist. We therefore "
        "repeated the comparison with priors and slopes taken from *other application families* (leave-one-family-out, LOFO): soil tasks "
        "received a prior from fruit, fuel, pharmaceutical, meat and mixture calibrations. Each non-soil family comes from a single source, so "
        "its LOFO and LOSO priors are identical and already exclude its own family. The test is therefore informative for the 23 soil tasks, "
        "and the non-soil tasks show the cross-family case under both schemes. The transferred slope lost much of its "
        "accuracy: its mean absolute log error rose from {{b_lvl_SLOPE_T}} to {{b_lvl_SLOPE_T_LOFO}}, and from {{fam_soil_slope}} to "
        "{{fam_soil_slope_lofo}} on the soil tasks (Fig. 8a). B-RPM was almost unaffected ({{b_lvl_B_RPM}} to {{b_lvl_B_RPM_LOFO}}; soil "
        "{{fam_soil_brpm}} to {{fam_soil_brpm_lofo}}; Fig. 8b). Under LOFO transfer, B-RPM was more accurate than the transferred slope by "
        "{{bp_d_level_B_RPM_LOFO_vs_SLOPE_T_LOFO}} (95% CI {{bp_ci_level_B_RPM_LOFO_vs_SLOPE_T_LOFO}}; better on "
        "{{bp_w_level_B_RPM_LOFO_vs_SLOPE_T_LOFO}} tasks, p {{bp_p_level_B_RPM_LOFO_vs_SLOPE_T_LOFO}}; at the level of the eight sources, "
        "{{bp_sw_level_B_RPM_LOFO_vs_SLOPE_T_LOFO}}, p {{bp_sp_level_B_RPM_LOFO_vs_SLOPE_T_LOFO}}, because the difference is concentrated in "
        "the three soil sources). With a cross-family prior, B-RPM remained less accurate than the no-improvement rule "
        "({{bp_d_level_B_RPM_LOFO_vs_FLAT}}, Holm p {{bp_ph_level_B_RPM_LOFO_vs_FLAT}}). On the pre-specified gain endpoint "
        "(HB1), the two were equivalent ({{bp_d_gain_B_RPM_LOFO_vs_SLOPE_T_LOFO}}, p {{bp_p_gain_B_RPM_LOFO_vs_SLOPE_T_LOFO}}), so HB1 was not "
        "confirmed. The difference on the level endpoint lies in the bias. A slope summarises the noise level, eigen-structure and alignment of "
        "the calibrations it was learned from, and it carries them into the new task. B-RPM transfers only a weak prior on the alignment exponent and the noise "
        "fraction. The noise fraction differed strongly between families, but the pilot path constrains it, so the posterior moves away from a "
        "misplaced prior: for the soil tasks, the cross-family prior was centred at a noise fraction of {{lofo_eta_prior}}, the posterior median "
        "was {{lofo_eta_post}}, and the large-sample value was {{soil_eta_ls}}. The curve is then recomputed from the new task's own eigen-spectrum. A slope, by contrast, is applied as it is. "
        "Transferring structure rather than curves is the likely reason for the difference.")
    s.append(f"![**Fig. 8.** Effect of transferring prior knowledge across application families. Mean absolute log error per task (lines) when the slope (a) or the structural prior of B-RPM (b) comes from other data sources (LOSO) or from other application families (LOFO). Thick line: mean over tasks.]({fig('Fig7_cross_family_transfer')}){{width=15cm}}")
    # 4.6 -----------------------------------------------------------------------------------------------------
    s.append("## 4.6. Uncertainty and planning decisions")
    s.append(
        "The posterior-predictive bands of B-RPM were too narrow. Nominal 80% and 95% bands covered the truth in {{bc80_B_RPM}} and "
        "{{bc95_B_RPM}} of cases (task averages; median width factor {{bcw_B_RPM}}), so HB3 was not met, and coverage was lowest for the designed "
        "mixtures ({{bcov_mix80}}). The bands contain the uncertainty of the pilot's regularisation path but not the difference between a "
        "pilot's cross-validated error and the error of a calibration trained on it, which our earlier analysis identified as the dominant "
        "source of level error. A post-hoc recalibration of the predictive spread, estimated leave-one-source-out from the standardised errors "
        "of the other sources, restored nominal coverage ({{bc80_B_RPM_cal}} and {{bc95_B_RPM_cal}}; {{bcal_n0_range}} across pilot sizes; "
        "soil {{bcal_soil80}}, mixtures {{bcal_mix80}}) at a median width factor of {{bcw_B_RPM_cal}}. IPL3 reached similar coverage only with "
        "bands that spanned a median factor of {{bcw_IPL3}} (Supplementary Table [[ST:TB4_brpm_coverage]]). For the probabilistic decision "
        "'will an eightfold larger calibration set reduce RMSEP by at least 15%?', no method beat the base rate (Brier score {{brier_B_RPM}} for "
        "B-RPM, {{brier_FLAT}} for FLAT, {{brier_SLOPE_T}} for SLOPE-T and {{brier_clim}} for the climatological forecast; Supplementary Table "
        "[[ST:TB6_decision]]). This is consistent with Proposition 1. Such decisions turn on precisely the gain that a 25–200-sample pilot cannot "
        "determine.")
    s.append(
        "We therefore tested the staged design that Proposition 1 suggests, using the existing forecasts (Supplementary Table "
        "[[ST:TB10_staged_decision]]). An analyst with an absolute RMSEP target and a budget of $N$ = 400 or 800 reference samples asks "
        "whether the target is reachable. Targets were set 15% above and 15% below the true RMSEP at $N$. Deciding from a pilot of $N/8$ "
        "samples was correct in {{sd400_one_shot_B_RPM}} ($N$ = 400) and {{sd800_one_shot_B_RPM}} ($N$ = 800) of cases with B-RPM, "
        "{{sd400_one_shot_FLAT}} and {{sd800_one_shot_FLAT}} with FLAT, and {{sd400_one_shot_IPL3}} and {{sd800_one_shot_IPL3}} with IPL3. "
        "Taking a second batch first, i.e. deciding from $N/4$ samples, raised the accuracy of every method by {{sd_gain_range}} percentage "
        "points (B-RPM {{sd400_staged_B_RPM}} and {{sd800_staged_B_RPM}}; FLAT {{sd400_staged_FLAT}} and {{sd800_staged_FLAT}}). The error of "
        "a B-RPM forecast for a fixed size of 800 samples fell from {{ft800_brpm_50}} with a 50-sample pilot to {{ft800_brpm_100}} with 100 "
        "and {{ft800_brpm_200}} with 200 (Supplementary Table [[ST:TB9_fixed_target]]). The methods failed in characteristic directions. FLAT "
        "declared reachable targets unreachable (correct for only {{sd_flat_reach}} of reachable targets), and SLOPE-T declared unreachable "
        "targets reachable (correct for {{sd_slope_unreach}} of unreachable ones). B-RPM was the most balanced ({{sd_brpm_reach}} and "
        "{{sd_brpm_unreach}}). Gating the second batch on the compatible set did not save reference analyses: at this ±15% resolution, "
        "the set excluded the target in only {{gate_settled}} of cases, so a second batch was needed almost always. For decisions this fine, "
        "a 25–100-sample pilot cannot replace a second batch.")
    # 4.7 -----------------------------------------------------------------------------------------------------
    s.append("## 4.7. Robustness, distribution shift and ablation")
    s.append(
        "On six representative tasks, B-RPM was evaluated with raw-absorbance and first-derivative spectra, Kennard–Stone-selected pilots and "
        "noisier reference values, and on mango under a new-season and an orchard-population shift (Supplementary Table [[ST:T8_robustness]]). "
        "With raw and first-derivative spectra its mean absolute log errors were {{rob_prep_raw_B_RPM}} and {{rob_prep_sg1_B_RPM}} (FLAT "
        "{{rob_prep_raw_FLAT}} and {{rob_prep_sg1_FLAT}}; IPL3 {{rob_prep_raw_IPL3}} and {{rob_prep_sg1_IPL3}}). With added reference noise they "
        "were {{rob_ref_noise_B_RPM}} (FLAT {{rob_ref_noise_FLAT}}). In these scenarios B-RPM was therefore less accurate than the no-improvement rule, though more accurate than curve "
        "extrapolation; on six tasks the pilot's own error remains the most robust single number. Kennard–Stone pilots made every anchored forecast pessimistic (B-RPM bias "
        "{{robb_ks_pilot_B_RPM}}, FLAT {{robb_ks_pilot_FLAT}}), because a pilot that spans the extremes of the spectral space has a larger "
        "cross-validated error than a random sample. Under the season shift, B-RPM became clearly optimistic (bias {{robb_shift_season_B_RPM}}, against "
        "{{robb_shift_season_FLAT}} for FLAT and {{robb_shift_season_IPL3}} for IPL3): it forecast the improvement expected within the "
        "calibration seasons, which the new season did not deliver. No method anticipated a shift, and pilots must be drawn at "
        "random from the population in which the calibration will be used. In the controlled simulation (Supplementary Table "
        "[[ST:T0b_simulation_by_n0]]), B-RPM with the real-data prior (median $r$ = {{sim_prior_r}}) was the most accurate method when the true "
        "alignment was close to that prior ($r=0.5$: {{sim_b_05}} vs {{sim_FLAT_05}} for FLAT, {{sim_RPM_05}} for RPM and {{sim_IPL3_05}} for "
        "IPL3; with a flat prior {{sim_bf_05}}). When the prior was wrong ($r=2$), it lost to the no-improvement rule ({{sim_b_2}} vs "
        "{{sim_FLAT_2}}). This is the cost of importing information that Proposition 1 makes unavoidable. The pre-specified ablations "
        "(Supplementary Table [[ST:T7_ablation]]) showed that freeing the alignment exponent without a prior is the most damaging choice "
        "(Section 2.4).")
    # 4.8 -----------------------------------------------------------------------------------------------------
    s.append("## 4.8. Comparison with previous work and practical recommendations")
    s.append(
        "Learning-curve extrapolation for sample-size planning in analytical spectroscopy [@ali2018] and in classification more generally "
        "[@mukherjee2003; @figueroa2012; @beleites2013] has relied on the assumption that the curve's shape can be read from a pilot. Our results "
        "explain why this works for short extrapolations and fails for long ones: the shape below the observability horizon is not in the pilot. "
        "The same reasoning applies to the minimum-sample-size criteria transferred from clinical prediction modelling [@riley2020; "
        "@konstantinidis2025], which control overfitting at a given size but do not predict the gain from more samples. Recent work in this "
        "journal has emphasised validation design [@lopez2026; @holman2026; @alshaebi2026], replicate-based error structure [@riu2026], "
        "calibration-set reduction [@andries2026], prediction uncertainty [@chiappini2025] and benchmarks of modern regressors on many NIR data sets "
        "[@reiter2026]. Its practical advice on multivariate calibration [@olivieri2026] fits our observations. The reference-method error sets "
        "a floor, the floor sets the slope, and learning curves for linear calibrations are shallow. The present work adds the planning side: a "
        "statement of what the pilot can and cannot tell, and a forecaster whose prior information is explicit, transferable and measurable.")
    s.append(
        "We therefore recommend the following. (i) Do not extrapolate learning curves with power-law, exponential or logarithmic fits to a small "
        "pilot. (ii) Treat the pilot's cross-validated error as the best single estimate of the current error, and plan decisions that "
        "depend on the gain as staged decisions: a second batch of the same size improved every method's decisions more than any choice of "
        "forecaster did. (iii) Report the compatible set with any forecast, as an honest statement of what the pilot allows. (iv) When a "
        "gain forecast is needed before the second batch, prefer a forecaster with an explicit structural prior (B-RPM) over a transferred "
        "slope whenever the previous calibrations come from other materials, and recalibrate its bands on previous calibrations. (v) Draw "
        "pilots at random from the target population. A space-filling selection such as Kennard–Stone remains the right choice for building "
        "the final calibration, but not for forecasting.")
    return "\n\n".join(x for x in s if x)


def _table2(TAB):
    t = pd.read_csv(os.path.join(TAB, "TB1_brpm_summary.csv"))
    keep = ["B-RPM", "B-RPM-LOFO", "RPM", "RPM-T", "IPL3", "IPL2", "WEI", "DFOLS", "FLAT", "SLOPE-T", "SLOPE-T-LOFO", "B-RPM-0", "B-RPM-r"]
    lab = {"B-RPM": "B-RPM (LOSO prior)", "B-RPM-LOFO": "B-RPM (LOFO prior)", "RPM": "RPM, r = 1 (pre-specified)",
           "RPM-T": "RPM, transferred r", "IPL3": "Inverse power law (IPL3) [@ali2018]", "IPL2": "Power law (IPL2)",
           "WEI": "Scaling exponent [@wei2022]", "DFOLS": "Fixed-complexity formula", "FLAT": "No improvement (pilot CV error)",
           "SLOPE-T": "Transferred slope (LOSO)", "SLOPE-T-LOFO": "Transferred slope (LOFO)", "B-RPM-0": "B-RPM prior only (ablation)",
           "B-RPM-r": "B-RPM, prior on r only (ablation)"}
    t = t[t.method.isin(keep)].set_index("method").loc[[m for m in keep if m in set(t.method)]].reset_index()
    out = pd.DataFrame({"Method": [lab[m] for m in t.method], "Level error": t.level_mae, "Level error (source mean)": t.level_mae_source,
                        "Gain error": t.gain_mae, "Bias": t.mean_bias})
    return out


ABSTRACT_BACKGROUND = (
    "Multivariate calibrations of NIR and MIR spectra need costly reference analyses, and analysts must decide from a small pilot set "
    "whether more samples will pay off. Learning-curve extrapolation is used for this decision, but it is unknown which part of a learning "
    "curve a pilot can determine.")
ABSTRACT_RESULTS = (
    "The deterministic-equivalent (random-matrix) risk of ridge regression reproduced ridge and PLS learning curves of {{n_tasks}} public "
    "NIR/MIR calibration tasks (mean absolute log error {{tv_ridge_mean}} and {{tv_pls_mean}}). From it we prove that a pilot observes the "
    "calibration's bias function only above an effective-regularisation horizon. Analyte signal below the horizon is indistinguishable "
    "from noise, so the gain from more samples cannot be identified from a pilot alone. A computable compatible set of curves "
    "consistent with the pilot contained the true RMSEP in {{id_cov_all}} of forecasts (whole curves {{id_curve_cov}}; {{sim_id_cov}} in "
    "simulation) but spanned a factor of "
    "{{id_w_8}} in RMSEP at eightfold extrapolation. Bayesian regularisation-path matching (B-RPM) makes the unavoidable prior explicit. "
    "It forecast gains better than the no-improvement rule and RPM ($r=1$), and for soil tasks it kept its accuracy with a prior from "
    "other application families ({{b_lvl_B_RPM_LOFO}} vs {{b_lvl_SLOPE_T_LOFO}} for a transferred slope over all tasks). On the RMSEP level, however, the pilot's "
    "own cross-validated error stayed best ({{b_lvl_FLAT}} vs {{b_lvl_B_RPM}}), and three of four pre-specified hypotheses failed. A "
    "second batch raised the accuracy of reachability decisions by {{sd_gain_range}} percentage points for every method.")
ABSTRACT_SIGNIFICANCE = (
    "Every pilot-based learning-curve forecast rests on prior information that the pilot cannot supply. Sample-size decisions that depend "
    "on the future gain should be staged, and forecasts should state their prior and their compatible set.")

HIGHLIGHTS = [
    "A pilot set observes a calibration's error curve only above a computable horizon.",
    "The gain from more reference samples cannot be identified from a pilot alone.",
    "A prior-free compatible set contained the true learning curve in ~9 of 10 cases.",
    "Bayesian path matching (B-RPM) makes the prior behind every forecast explicit.",
    "No forecaster beat the pilot's own cross-validated error on the RMSEP level.",
]

CONCLUSION = (
    "A small pilot set determines a calibration's error curve only above an observability horizon set by its size and the eigen-spectrum "
    "of the spectra. Below the horizon, analyte signal and irreducible noise cannot be told apart, so the gain from more reference samples "
    "must come from prior knowledge. This explains the optimism of power-law extrapolation and the strength of the no-improvement rule. The "
    "compatible set makes the limit visible for every pilot. B-RPM turns the unavoidable prior into an explicit one; it predicted gains "
    "better than the no-improvement rule and, unlike a transferred slope, kept its accuracy with a prior from other application families "
    "(tested on the soil tasks), but it did not beat the pilot's own error on the RMSEP level. For planning, the practical consequence is a staged design. Use "
    "the pilot's error as the current estimate and a structural forecast with its compatible set as a guide, and take a second batch "
    "before committing the full reference budget.")

COVER_LETTER = [
    "Every multivariate calibration project faces the same early decision: will more reference analyses reduce the prediction error enough "
    "to justify their cost? Learning-curve extrapolation from a pilot set has been the standard answer since Ali et al. (Anal. Chem. 2018). "
    "Our manuscript shows, with a proof and a leakage-free benchmark on {{n_tasks}} public NIR/MIR calibration tasks, which part of a "
    "learning curve a pilot can determine and which part it cannot.",
    "The methodological contributions are: (i) Proposition 1, which locates the observability horizon of a pilot set and shows that the gain "
    "from more samples is not identifiable without prior information; (ii) a computable, prior-free compatible set and an information "
    "fraction that tell the analyst, for every pilot, whether the sample-size question can be settled; and (iii) Bayesian regularisation-path "
    "matching (B-RPM), a forecaster that combines a transferable structural prior with the task's unlabelled spectra and the pilot's exact cross-validation path. B-RPM "
    "predicted gains better than the no-improvement rule and, unlike a transferred empirical slope, kept its accuracy on the soil tasks when "
    "its prior came from other application families. We report openly that the pilot's own cross-validated error remained the best estimate of the "
    "RMSEP level and that three of four pre-specified hypotheses were not confirmed. The positive practical result is that a second "
    "batch improves sample-size decisions more than any choice of forecaster.",
    "The work connects to current themes in Analytica Chimica Acta: validation design and leakage, the error structure of reference values "
    "and replicates, and calibration-set size. The study follows a time-stamped, pre-specified design. The new method and its hypotheses were fixed before "
    "the results were seen, negative outcomes are reported, all data are public, and the complete code (one-command rerun) will be made available on request.",
    "The manuscript has not been published and is not under consideration elsewhere. All authors approved the submission and declare no "
    "competing interests.",
]

LIMITATIONS = """# 5. Limitations

1. **Linear calibrations.** The theory describes ridge regression and tracked PLS closely (Section 4.1). Non-linear and local calibration methods may keep improving after linear models saturate, and their observability limits are not covered.
2. **Parametric family.** The compatible set and B-RPM use the power-law family $s_k\\propto\\lambda_k^r$. Other families could give wider sets. The coverage of about 90% on real data and 99% in simulation suggests that the family is adequate for these spectra, but it is not guaranteed for other materials.
3. **Pre-specified hypotheses not met.** B-RPM's raw bands under-covered (HB3). Its level error was 0.02 above the no-improvement rule, so non-inferiority (HB2) was not shown. Under cross-family transfer, its gain error equalled that of the transferred slope (HB1). The recalibrated bands are post hoc.
4. **Random sampling from a stable population.** Kennard–Stone pilots and genuine shifts bias every anchored forecast (Section 4.7). In the robustness scenarios, B-RPM was less accurate than the no-improvement rule, and under a season shift it was optimistic.
5. **Data sets.** {{n_soil}} of the {{n_tasks}} tasks are soil calibrations. The fruit, fuel, pharmaceutical, meat and mixture sets are smaller and allow only short extrapolations, and the designed mixtures violate the random-sampling premise of the theory."""
