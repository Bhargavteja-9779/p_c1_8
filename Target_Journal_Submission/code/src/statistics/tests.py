"""Paired statistical comparison across tasks (unit of analysis = task)."""
from __future__ import annotations

import numpy as np
from scipy.stats import wilcoxon


def rank_biserial(d):
    """Matched-pairs rank-biserial correlation for paired differences d (positive => first worse)."""
    d = np.asarray(d, float); d = d[d != 0]
    if len(d) == 0:
        return 0.0
    r = np.argsort(np.argsort(np.abs(d))) + 1.0
    return float((r[d > 0].sum() - r[d < 0].sum()) / r.sum())


def bootstrap_ci_median(d, n_boot=10000, seed=0, alpha=0.05):
    rng = np.random.default_rng(seed)
    d = np.asarray(d, float)
    b = np.median(rng.choice(d, size=(n_boot, len(d)), replace=True), axis=1)
    return float(np.quantile(b, alpha / 2)), float(np.quantile(b, 1 - alpha / 2))


def bootstrap_ci_mean(x, n_boot=10000, seed=0, alpha=0.05):
    rng = np.random.default_rng(seed)
    x = np.asarray(x, float)
    b = rng.choice(x, size=(n_boot, len(x)), replace=True).mean(1)
    return float(np.quantile(b, alpha / 2)), float(np.quantile(b, 1 - alpha / 2))


def holm(pvals):
    p = np.asarray(pvals, float); m = len(p)
    order = np.argsort(p); adj = np.empty(m); run = 0.0
    for k, i in enumerate(order):
        run = max(run, (m - k) * p[i]); adj[i] = min(1.0, run)
    return adj


def paired_comparison(ref, others: dict, seed=0):
    """Compare a reference method's per-task errors with each other method (lower = better).

    Returns list of dicts with Wilcoxon statistic, raw and Holm-adjusted p, median paired difference
    (other - ref; positive => reference better) with bootstrap 95% CI, rank-biserial r, win counts.
    """
    out = []
    names = list(others)
    for nm in names:
        o = np.asarray(others[nm], float); r = np.asarray(ref, float)
        ok = np.isfinite(o) & np.isfinite(r)
        d = o[ok] - r[ok]
        try:
            st = wilcoxon(o[ok], r[ok], alternative="two-sided", zero_method="wilcox")
            stat, p = float(st.statistic), float(st.pvalue)
        except ValueError:
            stat, p = np.nan, 1.0
        lo, hi = bootstrap_ci_median(d, seed=seed)
        out.append({"comparison": nm, "n_tasks": int(ok.sum()), "wilcoxon_W": stat, "p_raw": p,
                    "median_diff": float(np.median(d)), "ci95_lo": lo, "ci95_hi": hi,
                    "rank_biserial": rank_biserial(d), "ref_wins": int(np.sum(d > 0)), "ref_losses": int(np.sum(d < 0))})
    adj = holm([x["p_raw"] for x in out])
    for x, a in zip(out, adj):
        x["p_holm"] = float(a)
    return out
