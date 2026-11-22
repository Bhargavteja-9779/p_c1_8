"""Graphical abstract (Elsevier: 1328 x 531 px minimum, 5:2), drawn from real results of one pilot (no typed numbers)."""
import os
import numpy as np
import matplotlib.pyplot as plt
from experiments.bayes_analysis import load_all

INK, INK2, BLUE, GREY, AQUA, ORANGE = "#0b0b0b", "#52514e", "#2a78d6", "#8a8984", "#1baf7a", "#eb6834"


def main(root):
    df = load_all(os.path.join(root, "results", "raw"))
    task = "ICRAF-MIR:OC"
    e = df[(df.task == task) & (df.n0 == 50) & (df.method == "B-RPM") & (df.ratio >= 2)].copy()
    e["ae"] = (e.fc_logrmse - e.truth_ridge_logrmse).abs()
    pe = e.groupby("pilot").ae.mean()
    pil = int((pe - pe.median()).abs().idxmin())         # representative pilot: median B-RPM error
    d = df[(df.task == task) & (df.n0 == 50) & (df.pilot == pil) & (df.split == 0)]
    b = d[d.method == "B-RPM"].sort_values("n"); f = d[d.method == "FLAT"].sort_values("n"); p = d[d.method == "IPL3"].sort_values("n")
    fig = plt.figure(figsize=(13.28, 5.31), dpi=100)
    ax0 = fig.add_axes([0.0, 0.0, 0.27, 1.0]); ax0.axis("off")
    ax0.text(0.08, 0.86, "Small pilot set", fontsize=19, weight="bold", color=INK)
    ax0.text(0.08, 0.76, "$n_0$ reference analyses", fontsize=15, color=INK2)
    ax0.text(0.08, 0.58, "+ unlabelled spectra", fontsize=17, weight="bold", color=INK)
    ax0.text(0.08, 0.49, "eigen-spectrum → horizon $\\kappa_0$", fontsize=14, color=INK2)
    ax0.text(0.08, 0.31, "+ previous calibrations", fontsize=17, weight="bold", color=INK)
    ax0.text(0.08, 0.22, "prior on alignment, noise", fontsize=14, color=INK2)
    ax = fig.add_axes([0.345, 0.17, 0.35, 0.68])
    n = b.n.values
    ax.fill_between(n, np.exp(b.id_lo), np.exp(b.id_hi), color=GREY, alpha=0.22, lw=0, label="What the pilot allows")
    ax.fill_between(n, np.exp(b.lo80), np.exp(b.hi80), color=BLUE, alpha=0.28, lw=0, label="B-RPM forecast (80 %)")
    ax.plot(n, np.exp(b.fc_logrmse), color=BLUE, lw=3, marker="o")
    ax.plot(p.n, np.exp(p.fc_logrmse), color=ORANGE, ls="--", lw=2.5, marker="s", label="Power-law extrapolation")
    ax.plot(n, np.exp(b.truth_ridge_logrmse), color=INK, lw=3.5, label="True learning curve")
    ax.set_xscale("log"); ax.set_yscale("log")
    lo = np.exp(b.truth_ridge_logrmse.min()) / 1.8; hi = np.exp(b.truth_ridge_logrmse.max()) * 3.0
    ax.set_ylim(lo, hi); ax.set_xlabel("Number of calibration samples $n$", fontsize=14); ax.set_ylabel("RMSEP", fontsize=14)
    ax.tick_params(labelsize=11); ax.legend(fontsize=10.5, loc="upper right", frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title("Soil organic carbon (MIR), 50-sample pilot\n(pilot with the median B-RPM error)", fontsize=12, color=INK2)
    ax2 = fig.add_axes([0.72, 0.0, 0.28, 1.0]); ax2.axis("off")
    ax2.text(0.02, 0.84, "Observability limit", fontsize=18, weight="bold", color=INK)
    ax2.text(0.02, 0.70, "signal below $\\kappa_0$ looks like noise:\nthe gain is not identifiable\nfrom the pilot alone", fontsize=13.5, color=INK2, va="top")
    ax2.text(0.02, 0.42, "B-RPM", fontsize=18, weight="bold", color=BLUE)
    ax2.text(0.02, 0.32, "explicit, transferable prior;\nbetter gain forecasts; generalises\nacross materials.  Stage the decision.", fontsize=13.5, color=INK2, va="top")
    fig.savefig(os.path.join(root, "manuscript", "Graphical_Abstract.png"), dpi=100, facecolor="white")
    fig.savefig(os.path.join(root, "manuscript", "Graphical_Abstract.pdf"), facecolor="white")


if __name__ == "__main__":
    main(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
