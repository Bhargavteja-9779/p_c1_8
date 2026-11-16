#!/usr/bin/env python3
"""Compile the Supplementary Material (DOCX + PDF) from machine-generated tables and figures."""
import os
import subprocess

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TAB = os.environ.get("MS_TAB", os.path.join(ROOT, "tables"))
FIG = os.environ.get("MS_FIG", os.path.join(ROOT, "figures"))
SUP_SRC = os.path.join(ROOT, "supplementary")
SUP = os.environ.get("MS_OUT", SUP_SRC)

TABLES = [
    ("T1_tasks", "Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60)."),
    ("T2_main_accuracy_ridge_truth", "Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%)."),
    ("T2b_accuracy_by_n0", "Forecast accuracy by pilot size n0."),
    ("T3_stats_rpm_vs_baselines", "Paired two-sided Wilcoxon signed-rank tests (task level) of the pre-registered RPM against every other method; Holm-adjusted p-values; median paired difference (other − RPM; positive favours RPM) with bootstrap 95% CI; matched-pairs rank-biserial correlation."),
    ("T4_main_accuracy_pls_truth", "Forecast accuracy against the PLS ground truth."),
    ("T4b_stats_pls_truth", "Paired tests against the PLS ground truth."),
    ("T5_interval_coverage", "Empirical coverage and mean width (as a multiplicative factor on RMSE) of 80% and 95% forecast bands."),
    ("T6_sample_size_decisions", "Pre-registered sample-size decision metric: share of pilots whose forecast calibration size n̂ for the RMSE truly achieved at n* = 4n0 or 16n0 lies within a factor of two of n*, and share whose forecast never reaches the target."),
    ("T7_ablation", "Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task)."),
    ("T7b_ablation_eigenspectrum_rpmT", "Eigen-spectrum source ablation for RPM-T (defined before RPM-T results were inspected)."),
    ("T8_robustness", "Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios)."),
    ("T9_theory_validity_full_pool_fit", "Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves."),
    ("T10_runtime", "Measured run time per pilot."),
    ("T11_accuracy_by_family", "Accuracy by data-set family."),
    ("T12_error_by_extrapolation_ratio", "Absolute log error by extrapolation ratio n/n0."),
    ("T13_error_analysis_per_task", "Per-task error analysis (RPM vs IPL3) with spectral and fitted descriptors."),
    ("T13b_error_correlates", "Spearman correlations between per-task RPM error and task descriptors."),
    ("T14_posthoc_gain_and_decision", "POST HOC: error of the forecast gain RMSE(n)/RMSE(n0) and balanced accuracy of the decision 'an 8× larger calibration set reduces RMSEP by ≥ 10%'."),
    ("T14b_posthoc_gain_stats", "POST HOC: paired tests of gain error (reference: pre-registered RPM)."),
    ("T15_posthoc_bracket", "POST HOC: coverage and width of forecast brackets."),
    ("T0_simulation", "E0 simulation with Monte-Carlo ground truth (median absolute and signed log error)."),
    ("T0b_simulation_by_n0", "E0 simulation summarised by pilot size."),
    ("S0_accuracy_excluding_ICRAF_VisNIR", "Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work."),
    ("S0_stats_excluding_ICRAF_VisNIR", "Paired tests excluding the ICRAF-VisNIR tasks."),
]
FIGS = [
    ("Fig10_sample_size_decisions", "Pre-registered sample-size decision metric by method."),
    ("Fig9_error_analysis", "Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent."),
    ("Fig11_dataset_overview", "Data-set overview: number of samples and eigen-decay exponent by family."),
]
NOTES = [("EXPERIMENT_DESIGN_preregistration.md", "Pre-registered experimental design"),
         ("DATA_LEAKAGE_AUDIT.md", "Data-leakage audit"),
         ("LITERATURE_MATRIX_AND_NOVELTY_MAP.md", "Literature matrix and novelty map")]


def md_table(df, maxrows=60):
    def f(v):
        if isinstance(v, float):
            return "–" if pd.isna(v) else (f"{v:.3g}" if abs(v) < 1e-3 and v != 0 else f"{v:.3f}")
        return str(v)
    df = df.head(maxrows)
    cols = [str(c).replace("_", " ") for c in df.columns]
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    out += ["| " + " | ".join(f(v) for v in r) + " |" for r in df.itertuples(index=False)]
    return "\n".join(out)


def main():
    parts = ["# Supplementary Material", "",
             "**How many reference samples does a spectroscopic calibration need? Forecasting multivariate-calibration learning curves from small pilot sets with random-matrix theory**", "",
             "All tables and figures below are generated automatically by `run_all.py` from the per-pilot raw results.", ""]
    for i, (name, cap) in enumerate(TABLES, 1):
        p = os.path.join(TAB, name + ".csv")
        if not os.path.exists(p):
            continue
        parts += [f"**Table S{i}.** {cap}", "", md_table(pd.read_csv(p)), ""]
    for i, (name, cap) in enumerate(FIGS, 1):
        p = os.path.join(FIG, name + ".png")
        if os.path.exists(p):
            parts += [f"![**Figure S{i}.** {cap}]({p}){{width=15cm}}", ""]
    for fn, title in NOTES:
        p = os.path.join(SUP_SRC, fn)
        if os.path.exists(p):
            txt = open(p).read().split("\n", 1)[-1]
            parts += [f"# Note: {title}", "", txt, ""]
    md = os.path.join(HERE, "supplementary_full.md")
    open(md, "w").write("\n".join(parts))
    out = os.path.join(SUP, "Supplementary_Material.docx")
    subprocess.run(["pandoc", md, "-o", out, "--reference-doc", os.path.join(HERE, "reference_aca.docx")], check=True)
    import docx_utils
    docx_utils.postprocess(out)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", SUP, out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("supplementary built:", out)


if __name__ == "__main__":
    main()
