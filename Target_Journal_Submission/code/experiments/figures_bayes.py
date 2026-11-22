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
        ax.fill_between(n, np.exp(b.id_lo), np.exp(b.id_hi), color=GREY, alpha=0.18, lw=0, label="Compatible set (prior-free)")
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


def hidden_signal_table(paths, n0s=(25, 50, 100, 200)):
    """Share of the pilot's apparent error floor N(kappa_0) that is learnable target power (large-sample fit, r free):
    H = sum_k s_k (k0/(lam_k+k0))^2 / N(k0), at the observability horizon kappa_0 of a pilot of n0 samples."""
    from src.models.theory import solve_kappa
    al = pd.read_csv(os.path.join(paths["results"], "alignment_exponents.csv")).set_index("task")
    rows = []
    for t in al.index:
        z = np.load(os.path.join(paths["raw_out"], f"truth_{t.replace(':', '__')}.npz"), allow_pickle=True)
        lam = z["lam"]; r = al.loc[t, "r_full_pool"]; eta = al.loc[t, "noise_frac_full_pool"]
        sk = (lam / lam.max()) ** r; sig = eta / (1 - eta) * sk.sum()
        for n0 in n0s:
            if n0 >= len(lam) - 1:
                continue
            k0 = solve_kappa(lam, float(n0), np.array([1e-14 * lam.max()]))[0]
            h = float(np.sum(sk * (k0 / (lam + k0)) ** 2))
            rows.append({"task": t, "family": al.loc[t, "family"], "n0": n0, "hidden_share": h / (h + sig), "p": len(lam)})
    d = pd.DataFrame(rows)
    d.to_csv(os.path.join(paths["tables"], "TB11_hidden_signal.csv"), index=False)
    return d


def fig_observability(paths):
    t = pd.read_csv(os.path.join(paths["tables"], "TB5_idset.csv"))
    r = t[t.by == "ratio"]; q = t[t.by == "n0"]
    hs = hidden_signal_table(paths)
    fig, AX = plt.subplots(1, 4, figsize=(10.6, 2.4), gridspec_kw={"wspace": 0.6})
    x = np.arange(len(r))
    AX[0].bar(x, r.coverage, color=BLUE); AX[0].axhline(0.9, color=INK2, ls="--", lw=1)
    AX[0].set_xticks(x, [f"{v}x" for v in r.ratio]); AX[0].set_ylim(0, 1); AX[0].set_title("(a) Truth inside compatible set")
    AX[0].set_xlabel("Extrapolation ratio $n/n_0$"); AX[0].set_ylabel("Share of forecasts")
    AX[1].plot(x, r.median_width_factor, color=ORANGE, marker="s"); AX[1].set_yscale("log")
    AX[1].set_xticks(x, [f"{v}x" for v in r.ratio]); AX[1].set_title("(b) Width of compatible set")
    AX[1].set_xlabel("Extrapolation ratio $n/n_0$"); AX[1].set_ylabel("Upper/lower RMSEP")
    grp = [g.hidden_share.values for _, g in hs.groupby("n0")]
    AX[2].boxplot(grp, tick_labels=[str(k) for k in sorted(hs.n0.unique())], widths=0.55, showfliers=False,
                  medianprops=dict(color=BLUE, lw=1.6))
    AX[2].set_title("(c) Learnable signal hidden\nin the pilot's error floor"); AX[2].set_xlabel("Pilot size $n_0$")
    AX[2].set_ylabel("Share of $N(\\kappa_0)$"); AX[2].set_ylim(0, None)
    xq = np.arange(len(q))
    AX[3].bar(xq, q.info_fraction_median, color=AQUA)
    AX[3].set_xticks(xq, [str(int(v)) for v in q.n0]); AX[3].set_ylim(0, 1)
    AX[3].set_title("(d) Information from the pilot"); AX[3].set_xlabel("Pilot size $n_0$"); AX[3].set_ylabel("Median information fraction")
    fig.subplots_adjust(left=0.06, right=0.99, bottom=0.2, top=0.82); _save(fig, paths, "Fig5_observability")


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
    fig_idset_examples(df, paths); fig_observability(paths); fig_bias(paths); fig_transfer(df, paths); fig_campaign(paths)


def fig_campaign(paths):
    """Planning a calibration campaign: success rate vs samples bought (relative to the oracle) for all policies."""
    t = pd.read_csv(os.path.join(paths["tables"], "TB12_campaign_planning.csv")).set_index("policy")
    fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.1), sharey=True)
    pts = {"FIXED": ("Buy maximum", INK, "s"), "ONE:FLAT": ("No improvement", AQUA, "^"), "ONE:RPM": ("RPM (r = 1)", GREY, "v"),
           "ONE:IPL3": ("Power law (IPL3)", ORANGE, "s"), "ONE:WEI": ("Scaling exponent", "#7a5195", "P"),
           "ONE:SLOPE-T": ("Transferred slope", YEL, "D"), "ONE:B-RPM": ("B-RPM (point)", BLUE, "o")}
    ax = axs[0]
    for k, (lab, c, mk) in pts.items():
        if k in t.index:
            ax.scatter(t.loc[k, "cost_over_oracle"], t.loc[k, "success_rate"], color=c, marker=mk, s=40, label=lab, zorder=3)
    ax.set_title("(a) Point forecasts: an implicit risk attitude"); ax.set_xlabel("Samples bought / oracle"); ax.set_ylabel("Target met (share)")
    ax.legend(fontsize=6.3, loc="lower right"); ax.set_ylim(0, 1.05)
    ax = axs[1]
    for m, c, mk, lab in (("B-RPM", BLUE, "o", "B-RPM, prior from other sources"), ("B-RPM-LOFO", BLUE, "s", "B-RPM, prior from other families"),
                          ("SLOPE-T", YEL, "D", "Slope from other sources"), ("SLOPE-T-LOFO", YEL, "X", "Slope from other families")):
        xs, ys = [], []
        for q in (80, 90):
            k = f"CAL{q}:{m}"
            if k in t.index:
                xs.append(t.loc[k, "cost_over_oracle"]); ys.append(t.loc[k, "success_rate"])
        ax.plot(xs, ys, color=c, marker=mk, ls="-" if "LOFO" not in m else "--", label=lab)
        for xx, yy, q in zip(xs, ys, (80, 90)):
            ax.annotate(f"{q}%", (xx, yy), textcoords="offset points", xytext=(4, -9), fontsize=6.5, color=INK2)
    for q in (0.8, 0.9):
        ax.axhline(q, color=MUTED, lw=0.8, ls=":")
    ax.scatter(t.loc["FIXED", "cost_over_oracle"], 1.0, color=INK, marker="s", s=40)
    ax.set_title("(b) Decision-calibrated planning (requested 80% / 90%)"); ax.set_xlabel("Samples bought / oracle")
    ax.legend(fontsize=6.3, loc="lower right")
    fig.tight_layout(); _save(fig, paths, "Fig9_campaign_planning")


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    make_bayes_figures({"raw_out": os.path.join(root, "results", "raw"), "tables": os.path.join(root, "tables"),
                        "figures": os.path.join(root, "figures"), "results": os.path.join(root, "results")})
