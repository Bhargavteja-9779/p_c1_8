"""Publication figures generated from machine-readable results (never from typed numbers).

Palette: validated categorical slots (blue, orange, aqua) for at most three series per panel;
comparisons across more methods encode identity by axis position. Lines also differ by marker
and dash so identity never relies on colour alone.
"""
from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0"
C = {"RPM": "#2a78d6", "RPM-w": "#2a78d6", "IPL3": "#eb6834", "FLAT": "#1baf7a"}
STYLE = {"RPM": dict(marker="o", ls="-"), "RPM-w": dict(marker="o", ls="-"), "IPL3": dict(marker="s", ls="--"), "FLAT": dict(marker="^", ls=":")}
LBL = {"RPM": "RPM", "RPM-w": "RPM-w", "IPL3": "IPL3 extrapolation", "FLAT": "No improvement",
       "IPL2": "IPL2", "EXP3": "EXP3", "LOG2": "LOG2", "DFOLS": "DF-OLS"}

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.titlesize": 8.5, "axes.titleweight": "bold",
                     "legend.frameon": False, "legend.fontsize": 7.5, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "lines.linewidth": 1.5,
                     "lines.markersize": 4.5, "savefig.dpi": 300, "figure.dpi": 110, "pdf.fonttype": 42})


def _save(fig, paths, name):
    os.makedirs(paths["figures"], exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(paths["figures"], f"{name}.{ext}"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def fig_workflow(paths):
    fig, ax = plt.subplots(figsize=(7.6, 2.5)); ax.axis("off"); ax.set_xlim(0, 11.2); ax.set_ylim(0, 3.2)
    boxes = [(0.1, 1.9, "Unlabelled spectra\n(cheap, many)", "eigen-spectrum $\\lambda_k$"),
             (0.1, 0.3, "Labelled pilot\n($n_0$ reference values)", "exact LOGO error\nalong ridge path $e(\\mu)$"),
             (3.5, 1.1, "Regularisation-path\nmatching", "$\\mu\\mapsto\\kappa(n_0,\\mu)$;\nfit $\\tau^2,\\sigma^2$ of $N(\\kappa)$"),
             (6.7, 1.1, "Deterministic-equivalent\nrisk at any $n$", "$\\min_\\mu\\,\\frac{(1+1/n)N(\\kappa)}{1-df_2/n}$\n+ bootstrap bands")]
    for x, y, t, s in boxes:
        ax.add_patch(plt.Rectangle((x, y), 2.9, 1.0, fc="#f4f6fb", ec=MUTED, lw=0.8))
        ax.text(x + 1.45, y + 0.68, t, ha="center", va="center", fontsize=7.6, color=INK, weight="bold")
        ax.text(x + 1.45, y + 0.24, s, ha="center", va="center", fontsize=6.8, color=INK2)
    for (x0, y0, x1, y1) in [(3.0, 2.4, 3.5, 1.75), (3.0, 0.8, 3.5, 1.45), (6.4, 1.6, 6.7, 1.6)]:
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1.0))
    ax.annotate("", xy=(10.15, 1.6), xytext=(9.65, 1.6), arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1.0))
    ax.text(10.7, 1.6, "forecast\nRMSE($n$)\n→ sample-size\ndecision", ha="center", va="center", fontsize=7, color=INK)
    _save(fig, paths, "Fig1_workflow")


def fig_theory_validity(tv, collapse, paths, tasks=("KSSL-MIR:OC", "ICRAF-MIR:clay", "Mango:DM", "Neospectra-NIR:pH")):
    tasks = [t for t in tasks if t in set(tv.task)]
    fig, axes = plt.subplots(2, len(tasks), figsize=(1.85 * len(tasks) + 0.4, 3.9), squeeze=False)
    for j, t in enumerate(tasks):
        g = tv[(tv.task == t) & (tv["mode"] == "free")].sort_values("n")
        ax = axes[0, j]
        ax.plot(g.n, np.exp(g.ridge_logrmse), color=C["RPM"], marker="o", ls="-", label="Empirical ridge (LOGO-tuned)")
        ax.plot(g.n, np.exp(g.pls_logrmse), color=C["IPL3"], marker="s", ls="--", label="Empirical PLS (CV-tuned)")
        ax.plot(g.n, np.exp(g.theory_logrmse), color=INK, ls=":", lw=1.2, label="Theory (full-pool path fit)")
        ax.set_xscale("log"); ax.set_title(t, fontsize=7.5); ax.set_xlabel("calibration size $n$")
        if j == 0:
            ax.set_ylabel("test RMSE")
        ax2 = axes[1, j]
        pts = collapse.get(t, [])
        shades = plt.cm.Blues(np.linspace(0.45, 0.95, max(len(pts), 1)))
        for (n, k, nn), col in zip(pts, shades):
            ax2.plot(k, nn, color=col, lw=1.2, label=f"n={n}")
        ax2.set_xscale("log"); ax2.set_yscale("log"); ax2.set_xlabel("effective regularisation $\\kappa$")
        if j == 0:
            ax2.set_ylabel("rescaled test MSE  $N(\\kappa)$")
        if j == len(tasks) - 1:
            ax2.legend(fontsize=6, loc="upper left", ncol=1, handlelength=1.2)
    axes[0, 0].legend(loc="upper right", fontsize=6.2)
    fig.text(0.01, 0.98, "a", weight="bold", fontsize=10); fig.text(0.01, 0.49, "b", weight="bold", fontsize=10)
    fig.tight_layout()
    _save(fig, paths, "Fig2_theory_validity_and_collapse")


def fig_examples(df, paths, tasks=("KSSL-VisNIR:clay", "Mango:DM", "Diesel:bp50"), n0=50, pilot=0):
    tasks = [t for t in tasks if t in set(df.task)]
    fig, axes = plt.subplots(1, len(tasks), figsize=(2.4 * len(tasks), 2.4))
    axes = np.atleast_1d(axes)
    for ax, t in zip(axes, tasks):
        g = df[(df.task == t) & (df.n0 == n0) & (df.pilot == pilot)]
        if not len(g):
            continue
        tr = g[g.method == "RPM"].sort_values("n")
        ax.plot(tr.n, np.exp(tr.truth_ridge_logrmse), color=INK, lw=1.8, marker="D", ms=3.5, label="Actual (truth)")
        for m in ("RPM", "IPL3", "FLAT"):
            h = g[g.method == m].sort_values("n")
            ax.plot(h.n, np.exp(h.fc_logrmse), color=C[m], **STYLE[m], label=LBL[m])
            if m == "RPM" and h.lo80.notna().any():
                ax.fill_between(h.n, np.exp(h.lo95), np.exp(h.hi95), color=C[m], alpha=0.12, lw=0)
                ax.fill_between(h.n, np.exp(h.lo80), np.exp(h.hi80), color=C[m], alpha=0.22, lw=0)
        ax.axvline(n0, color=MUTED, lw=0.8, ls="--")
        ax.set_xscale("log"); ax.set_yscale("log"); ax.set_title(t, fontsize=7.5); ax.set_xlabel("calibration size $n$")
        ax.text(0.02, 0.03, f"pilot $n_0$ = {n0}", transform=ax.transAxes, fontsize=6, color=INK2)
    axes[0].set_ylabel("RMSEP (log scale)")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=4, fontsize=6.6, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.08, 1, 1)); _save(fig, paths, "Fig3_example_forecasts")


def fig_main_accuracy(df, paths, methods=("RPM", "RPM-w", "IPL3", "IPL2", "EXP3", "LOG2", "FLAT", "DFOLS")):
    n0s = sorted(df.n0.unique())
    fig, axes = plt.subplots(1, len(n0s), figsize=(1.9 * len(n0s) + 0.6, 2.8), sharey=True)
    axes = np.atleast_1d(axes)
    for ax, n0 in zip(axes, n0s):
        pt = df[(df.n0 == n0) & df.method.isin(methods)].groupby(["task", "method"]).abs_err.mean().unstack()
        for i, m in enumerate(methods):
            if m not in pt:
                continue
            v = np.clip(pt[m].dropna().values, 1e-3, None)
            col = C["RPM"] if m.startswith("RPM") else "#9a9993"
            ax.scatter(np.full(len(v), i) + np.random.default_rng(i).uniform(-0.18, 0.18, len(v)), v, s=6, color=col, alpha=0.6, lw=0)
            ax.plot([i - 0.3, i + 0.3], [np.median(v)] * 2, color=INK, lw=1.6)
        ax.set_yscale("log"); ax.set_xticks(range(len(methods))); ax.set_xticklabels(methods, rotation=60, fontsize=6.5)
        ax.set_title(f"pilot $n_0$ = {n0}")
    axes[0].set_ylabel("per-task mean |log(RMSE$_{fc}$/RMSE$_{true}$)|")
    fig.tight_layout(); _save(fig, paths, "Fig4_main_accuracy")


def fig_ratio(df, paths):
    fig, ax = plt.subplots(figsize=(3.4, 2.6))
    d = df[df.method.isin(["RPM", "IPL3", "FLAT"])].copy()
    d["rb"] = 2.0 ** np.round(np.log2(d.ratio))
    for m in ("RPM", "IPL3", "FLAT"):
        g = d[d.method == m].groupby("rb").abs_err.median()
        ax.plot(g.index, g.values, color=C[m], **STYLE[m], label=LBL[m])
        ax.text(g.index[-1] * 1.08, g.values[-1], m, color=INK2, fontsize=6.5, va="center")
    ax.set_xscale("log", base=2); ax.set_xlabel("extrapolation ratio $n/n_0$"); ax.set_ylabel("median |log error|")
    ax.legend(fontsize=6.5); fig.tight_layout(); _save(fig, paths, "Fig5_error_vs_extrapolation_ratio")


def fig_coverage(T5, paths):
    fig, ax = plt.subplots(figsize=(3.0, 2.6))
    ax.plot([70, 100], [70, 100], color=MUTED, lw=0.9, ls="--")
    for m in ("RPM", "IPL3"):
        g = T5[T5.method == m]
        ax.plot(g.nominal, g.coverage_rows, color=C[m], **STYLE[m], label=LBL[m])
    ax.set_xlabel("nominal coverage (%)"); ax.set_ylabel("empirical coverage (%)"); ax.set_xlim(70, 100)
    ax.legend(fontsize=6.5, loc="lower right"); fig.tight_layout(); _save(fig, paths, "Fig6_interval_coverage")


def fig_ablation(T7, paths):
    t = T7[T7.variant != "RPM"].sort_values("mean_diff_vs_rpm")
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    y = np.arange(len(t))
    ax.errorbar(t.mean_diff_vs_rpm, y, xerr=[t.mean_diff_vs_rpm - t.ci95_lo, t.ci95_hi - t.mean_diff_vs_rpm], fmt="o", color=C["RPM"], ms=4, lw=1, capsize=0)
    ax.axvline(0, color=MUTED, lw=0.9)
    ax.set_yticks(y); ax.set_yticklabels(t.variant, fontsize=6.8)
    ax.set_xlabel("Δ mean |log error| vs full RPM (+ = worse)")
    fig.tight_layout(); _save(fig, paths, "Fig7_ablation")


def fig_robustness(rob_path, paths):
    if not os.path.exists(rob_path):
        return
    rb = pd.read_csv(rob_path); rb["abs_err"] = (rb.fc_logrmse - rb.truth_ridge_logrmse).abs()
    t = rb.groupby(["variant", "method"]).apply(lambda g: g.groupby("task").abs_err.mean().mean()).unstack()
    t = t[[m for m in ("RPM", "IPL3", "FLAT") if m in t.columns]]
    fig, ax = plt.subplots(figsize=(4.2, 2.7))
    y = np.arange(len(t))
    for k, m in enumerate(t.columns):
        ax.scatter(t[m].values, y + (k - 1) * 0.18, color=C[m], marker=STYLE[m]["marker"], s=18, label=LBL[m], zorder=3)
    ax.set_yticks(y); ax.set_yticklabels(t.index, fontsize=6.8); ax.set_xlabel("mean |log error|")
    ax.legend(fontsize=6.3, loc="lower right"); fig.tight_layout(); _save(fig, paths, "Fig8_robustness")


def fig_error_analysis(ea, paths):
    cols = [("theory_fit_err", "theory misfit (full pool)"), ("noise_frac", "fitted noise fraction $\\sigma^2/\\mathrm{var}(y)$"),
            ("eigen_decay_exponent", "eigen-decay exponent")]
    fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.3), sharey=True)
    fams = sorted(ea.family.dropna().unique())
    mk = dict(zip(fams, ["o", "s", "^", "D", "v", "P"]))
    for ax, (c, lab) in zip(axes, cols):
        for f in fams:
            g = ea[ea.family == f]
            ax.scatter(g[c], g.rpm_mae, s=16, marker=mk[f], color=C["RPM"], alpha=0.75, label=f, lw=0)
        ax.set_xlabel(lab)
    axes[0].set_ylabel("RPM per-task |log error|"); axes[-1].legend(fontsize=6, loc="upper right", title="family", title_fontsize=6)
    fig.tight_layout(); _save(fig, paths, "Fig9_error_analysis")


def fig_decisions(dec_rows, paths, methods=("RPM", "RPM-w", "IPL3", "IPL2", "EXP3", "LOG2", "FLAT", "DFOLS")):
    fig, ax = plt.subplots(figsize=(3.6, 2.5))
    s = dec_rows.groupby("method").success_factor2.mean().reindex(methods) * 100
    f = dec_rows.groupby("method").failure.mean().reindex(methods) * 100
    x = np.arange(len(methods))
    ax.bar(x - 0.2, s.values, width=0.38, color=C["RPM"], label="n̂ within factor 2 of n*")
    ax.bar(x + 0.2, f.values, width=0.38, color="#9a9993", label="never reaches target")
    ax.set_xticks(x); ax.set_xticklabels(methods, rotation=60, fontsize=6.5); ax.set_ylabel("% of pilot decisions")
    ax.legend(fontsize=6.3); fig.tight_layout(); _save(fig, paths, "Fig10_sample_size_decisions")


def fig_datasets(T1, paths):
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    fams = sorted(T1.family.unique()); mk = dict(zip(fams, ["o", "s", "^", "D", "v", "P"]))
    for f in fams:
        g = T1[T1.family == f]
        ax.scatter(g.n_pool + g.n_test, g.eigen_decay_exponent, marker=mk[f], color=C["RPM"], s=18, label=f, lw=0, alpha=0.8)
    ax.set_xscale("log"); ax.set_xlabel("samples (pool + test)"); ax.set_ylabel("eigen-decay exponent")
    ax.legend(fontsize=6.3, title="family", title_fontsize=6.3); fig.tight_layout(); _save(fig, paths, "Fig11_dataset_overview")


def make_all(df, T1, tv, collapse, T5, dec_rows, T7, ea, paths, rob_path):
    fig_workflow(paths)
    fig_theory_validity(tv, collapse, paths)
    fig_examples(df, paths)
    fig_main_accuracy(df, paths)
    fig_ratio(df, paths)
    if len(T5):
        fig_coverage(T5, paths)
    if len(T7):
        fig_ablation(T7, paths)
    fig_robustness(rob_path, paths)
    fig_error_analysis(ea, paths)
    fig_decisions(dec_rows, paths)
    fig_datasets(T1, paths)
