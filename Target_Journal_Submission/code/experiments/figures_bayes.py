"""Figures for the observability analysis and B-RPM (generated from results/raw and tables/TB*; no typed numbers)."""
from __future__ import annotations

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from experiments.figures import _save, INK, INK2, MUTED
from experiments.bayes_analysis import load_all, add_slope, add_gain

BLUE, ORANGE, AQUA, YEL, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#8a8984"


def fig_idset_examples(df, paths, tasks=("KSSL-VisNIR:clay", "Mango:DM", "Diesel:bp50"), n0=50, pilot=0):
    fig, axs = plt.subplots(1, len(tasks), figsize=(7.4, 2.5))
    for ax, t in zip(axs, tasks):
        d = df[(df.task == t) & (df.n0 == n0) & (df.pilot == pilot) & (df.split == 0)]
        b = d[d.method == "B-RPM"].sort_values("n")
        if not len(b):
            continue
        n = b.n.values
        ax.fill_between(n, np.exp(b.id_lo), np.exp(b.id_hi), color=GREY, alpha=0.18, lw=0, label="Identification set (prior-free)")
        ax.fill_between(n, np.exp(b.lo80), np.exp(b.hi80), color=BLUE, alpha=0.25, lw=0, label="B-RPM 80 % band")
        ax.plot(n, np.exp(b.fc_logrmse), color=BLUE, marker="o", label="B-RPM")
        for m, c, ls, mk in (("FLAT", AQUA, ":", "^"), ("IPL3", ORANGE, "--", "s")):
            g = d[d.method == m].sort_values("n")
            ax.plot(g.n, np.exp(g.fc_logrmse), color=c, ls=ls, marker=mk, label={"FLAT": "No improvement", "IPL3": "IPL3"}[m])
        ax.plot(n, np.exp(b.truth_ridge_logrmse), color=INK, lw=2.0, label="True learning curve")
        ax.set_xscale("log"); ax.set_yscale("log"); ax.set_title(t); ax.set_xlabel("Calibration size $n$")
        ax.set_ylim(np.exp(b.truth_ridge_logrmse.min()) / 2.5, np.exp(b.truth_ridge_logrmse.max()) * 2.5)
    axs[0].set_ylabel("RMSEP")
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.17))
    fig.tight_layout()
    _save(fig, paths, "Fig3_identification_set_examples")


def fig_observability(paths):
    t = pd.read_csv(os.path.join(paths["tables"], "TB5_idset.csv"))
    r = t[t.by == "ratio"]; q = t[t.by == "n0"]
    fig, axs = plt.subplots(1, 3, figsize=(7.4, 2.3))
    x = np.arange(len(r))
    axs[0].bar(x, r.coverage, color=BLUE); axs[0].axhline(0.9, color=INK2, ls="--", lw=1)
    axs[0].set_xticks(x, [f"{v}x" for v in r.ratio]); axs[0].set_ylim(0, 1); axs[0].set_title("(a) Truth inside identification set")
    axs[0].set_xlabel("Extrapolation ratio $n/n_0$"); axs[0].set_ylabel("Share of forecasts")
    axs[1].plot(x, r.median_width_factor, color=ORANGE, marker="s"); axs[1].set_yscale("log")
    axs[1].set_xticks(x, [f"{v}x" for v in r.ratio]); axs[1].set_title("(b) Width of identification set")
    axs[1].set_xlabel("Extrapolation ratio $n/n_0$"); axs[1].set_ylabel("Median upper/lower RMSEP")
    xq = np.arange(len(q))
    axs[2].bar(xq, q.info_fraction_median, color=AQUA)
    axs[2].set_xticks(xq, [str(int(v)) for v in q.n0]); axs[2].set_ylim(0, 1)
    axs[2].set_title("(c) Information from the pilot"); axs[2].set_xlabel("Pilot size $n_0$"); axs[2].set_ylabel("Median information fraction")
    fig.tight_layout(); _save(fig, paths, "Fig5_observability")


def fig_bias(paths, methods=("B-RPM", "FLAT", "SLOPE-T", "RPM", "IPL3")):
    t = pd.read_csv(os.path.join(paths["tables"], "TB8_bias_by_ratio.csv"))
    sty = {"B-RPM": (BLUE, "-", "o"), "FLAT": (AQUA, ":", "^"), "SLOPE-T": (YEL, "-.", "D"), "RPM": (GREY, "-", "v"), "IPL3": (ORANGE, "--", "s")}
    lab = {"B-RPM": "B-RPM", "FLAT": "No improvement", "SLOPE-T": "Transferred slope", "RPM": "RPM (r = 1)", "IPL3": "IPL3"}
    fig, ax = plt.subplots(figsize=(3.6, 2.6))
    x = np.arange(len(t))
    for m in methods:
        c, ls, mk = sty[m]
        ax.plot(x, t[m], color=c, ls=ls, marker=mk, label=lab[m])
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_xticks(x, [f"{v}x" for v in t.rb]); ax.set_xlabel("Extrapolation ratio $n/n_0$")
    ax.set_ylabel("Mean signed log error\n(> 0 pessimistic, < 0 optimistic)")
    ax.legend(loc="lower left", fontsize=6.8)
    fig.tight_layout(); _save(fig, paths, "Fig6_bias_by_horizon")


def fig_transfer(df, paths):
    ev = df[df.ratio >= 2]
    lvl = ev.groupby(["task", "method"]).abs_err.mean().unstack()
    fam = ev.groupby("task").fam.first()
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 2.6), sharey=True)
    for ax, (m, title) in zip(axs, (("SLOPE-T", "(a) Transferred empirical slope"), ("B-RPM", "(b) B-RPM (transferred structure)"))):
        a, b = lvl[m], lvl[m + "-LOFO"]
        for t in lvl.index:
            c = BLUE if fam[t] == "soil" else ORANGE
            ax.plot([0, 1], [a[t], b[t]], color=c, alpha=0.55, lw=0.9, marker="o", ms=2.5)
        ax.plot([0, 1], [a.mean(), b.mean()], color=INK, lw=2.2, marker="D", ms=5)
        ax.set_xticks([0, 1], ["Prior from other\nsources (LOSO)", "Prior from other\nfamilies (LOFO)"]); ax.set_xlim(-0.3, 1.3)
        ax.set_title(title)
    axs[0].set_ylabel("Mean |log error| per task")
    from matplotlib.lines import Line2D
    fig.legend([Line2D([], [], color=BLUE), Line2D([], [], color=ORANGE), Line2D([], [], color=INK, lw=2.2)],
                  ["Soil task", "Non-soil task", "Mean over tasks"], loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.08), fontsize=6.8)
    fig.tight_layout(); _save(fig, paths, "Fig7_cross_family_transfer")


def make_bayes_figures(paths):
    df = load_all(paths["raw_out"]); df, _ = add_slope(df, paths["raw_out"]); df = add_gain(df)
    fig_idset_examples(df, paths); fig_observability(paths); fig_bias(paths); fig_transfer(df, paths)


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    make_bayes_figures({"raw_out": os.path.join(root, "results", "raw"), "tables": os.path.join(root, "tables"),
                        "figures": os.path.join(root, "figures"), "results": os.path.join(root, "results")})
