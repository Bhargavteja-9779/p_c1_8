"""Single source of truth for Supplementary Material numbering.

The manuscript refers to supplementary items symbolically ([[ST:table_name]], [[SF:figure_name]],
[[SN:note_file]]); `resolve` replaces the tokens with the numbers implied by the order below, and
build_supplementary.py compiles the Supplementary Material in exactly this order.
"""
import re

TABLES = [
    ("TB2_brpm_paired", "Paired comparisons of B-RPM (pre-specified hypotheses HB1–HB2 and exploratory comparisons): mean improvement over the reference (positive favours B-RPM), bootstrap 95% CI, Wilcoxon p (task level, Holm-adjusted) and source-level results."),
    ("TB12_campaign_planning", "Campaign-planning case study: share of campaigns meeting the target RMSEP, reference analyses bought relative to the oracle, total cost with recourse and purchase rounds, for fixed, one-shot, staged, risk-based and decision-calibrated policies."),
    ("TB12b_campaign_tests", "Paired comparisons of decision-calibrated planning (B-RPM vs transferred slope; task level): difference in success rate and in cost relative to the oracle."),
    ("TC1_native_resolution_summary", "Native-resolution confirmation study: level error, gain error and bias by method for the 32 held-out tasks, the 6 hypothesis-generating tasks and all 38 tasks."),
    ("TC2_native_resolution_tests", "Native-resolution confirmation study: paired comparisons of B-RPM (HC1 and secondary endpoints), task and source level."),
    ("TC3_native_resolution_by_family", "Native-resolution level error by application family (held-out tasks)."),
    ("TC4_native_resolution_by_n0", "Native-resolution level error by pilot size (held-out tasks)."),
    ("TC5_native_hidden_signal", "Native resolution: share of the apparent error floor at the observability horizon that is learnable target power."),
    ("TB11_hidden_signal", "Share of the apparent error floor at the observability horizon of a pilot that is learnable target power, per task and pilot size (large-sample fits)."),
    ("TB5_idset", "Prior-free compatible set: coverage of the true RMSEP, median width factor and median information fraction, by extrapolation ratio and pilot size (HB4)."),
    ("TB8_bias_by_ratio", "Mean signed log error by extrapolation ratio for all forecasters (pooled over tasks)."),
    ("TB10b_staged_decision_by_target", "Reachability decisions split into reachable and unreachable targets."),
    ("T1_tasks", "Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60)."),
    ("T9_theory_validity_full_pool_fit", "Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves (absolute log error per task)."),
    ("T17_posthoc_slope_explanation", "POST HOC: regression of the ground-truth learning-curve slope (log RMSE per doubling of n) on large-sample theory parameters, and Spearman correlations."),
    ("TB1_brpm_summary", "All forecasters on the version-2 design: task-level mean absolute log error (level), mean absolute gain error, mean signed bias, and source-level means."),
    ("TB3_brpm_by_family", "Level and gain error by application family for all forecasters."),
    ("TB4_brpm_coverage", "Coverage and median width factor of 80% and 95% bands by family and pilot size, including the post-hoc leave-one-source-out recalibration of B-RPM."),
    ("TB6_decision", "Brier score of the probabilistic decision 'an eightfold larger calibration set reduces RMSEP by at least 15%'."),
    ("TB8b_abs_task_bias_by_ratio", "Mean absolute per-task bias by extrapolation ratio (does not allow opposite task biases to cancel)."),
    ("TB7c_info_within_n0", "B-RPM level error by tertile of the information fraction within each pilot size."),
    ("TB9_fixed_target", "Forecast error for a fixed target calibration size (400, 800, 1600) by pilot size: value of a larger pilot or second batch."),
    ("TB10_staged_decision", "Reachability decisions for an absolute RMSEP target at budget N: one-shot (pilot N/8), staged (second batch, N/4) and compatible-set-gated policies."),
    ("T2_main_accuracy_ridge_truth", "Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%)."),
    ("T4_main_accuracy_pls_truth", "Forecast accuracy against the PLS ground truth."),
    ("S0_accuracy_excluding_ICRAF_VisNIR", "Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work."),
    ("T7_ablation", "Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task)."),
    ("T8_robustness", "Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios)."),
    ("T0b_simulation_by_n0", "E0 simulation summarised by pilot size."),
    ("T10_runtime", "Measured run time per pilot."),
]
FIGS = [
    ("Fig12_alignment_exponents", "Alignment exponent r estimated from the full calibration pool of each task, grouped by spectral region and sample type; dashed line: isotropic prior r = 1."),
    ("Fig13_slope_vs_noise", "Slope of the ground-truth learning curve (log RMSE per doubling of n) against the irreducible-noise fraction of the large-sample fit (post hoc)."),
    ("Fig4_main_accuracy", "Distribution of task-level forecast errors for all methods of the first design (version-2 data)."),
    ("Fig8_robustness", "Robustness scenarios: mean absolute log error by method."),
    ("Fig10_sample_size_decisions", "Pre-registered sample-size decision metric by method."),
    ("Fig9_error_analysis", "Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent."),
    ("Fig11_dataset_overview", "Data-set overview: number of samples and eigen-decay exponent by family."),
]
NOTES = [("EXPERIMENT_DESIGN_preregistration.md", "Pre-specified protocol of the first design (time-stamped)"),
         ("BRPM_preregistration_addendum.md", "Pre-specification addendum for B-RPM (hypotheses HB1–HB4), reproduced as committed (internal file references removed); 'version 2' refers to the final re-analysis reported in the article and 'identification set' to the compatible set"),
         ("FULLRES_preregistration_addendum.md", "Pre-specification addendum 2: native-resolution confirmation study (hypothesis HC1)"),
         ("DATA_LEAKAGE_AUDIT.md", "Data-leakage audit")
]

_IDX = {"ST": {n: i for i, (n, _) in enumerate(TABLES, 1)},
        "SF": {n: i for i, (n, _) in enumerate(FIGS, 1)},
        "SN": {n: i for i, (n, _) in enumerate(NOTES, 1)}}


def resolve(text):
    """Replace [[ST:x]] / [[SF:x]] / [[SN:x]] tokens by S-numbers; unknown names raise."""
    def rep(m):
        kind, name = m.group(1), m.group(2)
        if name not in _IDX[kind]:
            raise KeyError(f"unknown supplementary item {kind}:{name}")
        return ("" if kind == "SN" else "S") + str(_IDX[kind][name])
    return re.sub(r"\[\[(ST|SF|SN):([A-Za-z0-9_.\-]+)\]\]", rep, text)
