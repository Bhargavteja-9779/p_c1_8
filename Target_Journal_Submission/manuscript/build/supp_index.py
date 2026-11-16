"""Single source of truth for Supplementary Material numbering.

The manuscript refers to supplementary items symbolically ([[ST:table_name]], [[SF:figure_name]],
[[SN:note_file]]); `resolve` replaces the tokens with the numbers implied by the order below, and
build_supplementary.py compiles the Supplementary Material in exactly this order.
"""
import re

TABLES = [
    ("T1_tasks", "Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60)."),
    ("T9_theory_validity_full_pool_fit", "Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves (absolute log error per task)."),
    ("T9b_kappa_collapse_dispersion", "κ-collapse: across-n standard deviation of rescaled log test errors plotted against κ, compared with the same errors plotted against the raw penalty μ."),
    ("T17_posthoc_slope_explanation", "POST HOC: regression of the ground-truth learning-curve slope (log RMSE per doubling of n) on large-sample theory parameters, and Spearman correlations."),
    ("T17b_slope_by_region", "POST HOC: learning-curve slopes and alignment exponents by spectral region."),
    ("T2_main_accuracy_ridge_truth", "Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%)."),
    ("T2b_accuracy_by_n0", "Forecast accuracy by pilot size n0."),
    ("T3_stats_rpm_vs_baselines", "Paired two-sided Wilcoxon signed-rank tests (task level) of the pre-registered RPM against every other method; Holm-adjusted p-values; median paired difference (other − RPM; positive favours RPM) with bootstrap 95% CI; matched-pairs rank-biserial correlation."),
    ("T3c_posthoc_stats_slopeT_reference", "POST HOC: paired tests with SLOPE-T as the reference method."),
    ("T18_posthoc_by_ratio_stratum", "POST HOC: accuracy and paired tests stratified by extrapolation ratio n/n0 (short: < 16; long: ≥ 16)."),
    ("T12_error_by_extrapolation_ratio", "Absolute log error by extrapolation ratio n/n0."),
    ("T4_main_accuracy_pls_truth", "Forecast accuracy against the PLS ground truth."),
    ("T4b_stats_pls_truth", "Paired tests against the PLS ground truth."),
    ("S0_accuracy_excluding_ICRAF_VisNIR", "Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work."),
    ("S0_stats_excluding_ICRAF_VisNIR", "Paired tests excluding the ICRAF-VisNIR tasks."),
    ("T7b_ablation_eigenspectrum_rpmT", "Eigen-spectrum source ablation for RPM-T (defined before RPM-T results were inspected)."),
    ("T15_posthoc_bracket", "POST HOC: coverage and width of forecast brackets."),
    ("T5_interval_coverage", "Empirical coverage, median width factor (multiplicative, on RMSE) and share of bands wider than a factor of ten, for 80% and 95% forecast bands."),
    ("T16_posthoc_loso_conformal_bands", "POST HOC: leave-one-source-out split-conformal bands (coverage and median width factor)."),
    ("T6_sample_size_decisions", "Pre-registered sample-size decision metric: share of pilots whose forecast calibration size n̂ for the RMSE truly achieved at n* = 4n0 or 16n0 lies within a factor of two of n*, and share whose forecast never reaches the target."),
    ("T14_posthoc_gain_and_decision", "POST HOC: error of the forecast gain RMSE(n)/RMSE(n0) and balanced accuracy of the decision 'an 8× larger calibration set reduces RMSEP by ≥ 10%'."),
    ("T14b_posthoc_gain_stats", "POST HOC: paired tests of gain error (reference: pre-registered RPM)."),
    ("T7_ablation", "Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task)."),
    ("T8_robustness", "Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios)."),
    ("T0_simulation", "E0 simulation with Monte-Carlo ground truth (median absolute and signed log error)."),
    ("T0b_simulation_by_n0", "E0 simulation summarised by pilot size."),
    ("T13_error_analysis_per_task", "Per-task error analysis (RPM vs IPL3) with spectral and fitted descriptors."),
    ("T13b_error_correlates", "Spearman correlations between per-task RPM error and task descriptors."),
    ("T11_accuracy_by_family", "Accuracy by data-set family."),
    ("T10_runtime", "Measured run time per pilot."),
    ("T3_stats_n0_25", "Paired tests against RPM at pilot size n0 = 25."),
    ("T3_stats_n0_50", "Paired tests against RPM at pilot size n0 = 50."),
    ("T3_stats_n0_100", "Paired tests against RPM at pilot size n0 = 100."),
    ("T3_stats_n0_200", "Paired tests against RPM at pilot size n0 = 200."),
]
FIGS = [
    ("Fig10_sample_size_decisions", "Pre-registered sample-size decision metric by method."),
    ("Fig9_error_analysis", "Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent."),
    ("Fig11_dataset_overview", "Data-set overview: number of samples and eigen-decay exponent by family."),
]
NOTES = [("EXPERIMENT_DESIGN_preregistration.md", "Pre-registered experimental design"),
         ("DATA_LEAKAGE_AUDIT.md", "Data-leakage audit"),
         ("LITERATURE_MATRIX_AND_NOVELTY_MAP.md", "Literature matrix and novelty map")]

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
