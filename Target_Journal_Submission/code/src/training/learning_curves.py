"""Ground-truth learning curves and group-disjoint splitting."""
from __future__ import annotations

import numpy as np

from ..models.ridge import ridge_cv_path, PLSCV
from ..models.theory import DEFAULT_MU_REL

TRUTH_GRID = (25, 50, 100, 200, 400, 800, 1600, 3200, 6400)


def reps_for(n):
    return 30 if n <= 400 else (16 if n <= 1600 else 8)


def split_task(groups, seed, test_frac=0.25, test_cap=3000):
    """Group-disjoint split into a pool (calibration candidates) and a held-out test set."""
    rng = np.random.default_rng(seed)
    groups = np.asarray(groups)
    ug = np.array(np.unique(groups), dtype=object)
    rng.shuffle(ug)
    n = len(groups)
    target = min(int(round(test_frac * n)), test_cap)
    sizes = {g: c for g, c in zip(*np.unique(groups, return_counts=True))}
    chosen, tot = [], 0
    for g in ug:
        if tot >= target:
            break
        chosen.append(g); tot += sizes[g]
    test_mask = np.isin(groups, np.array(chosen, dtype=groups.dtype))
    return np.flatnonzero(~test_mask), np.flatnonzero(test_mask)


def _ridge_all_mu(Xtr, ytr, gtr, Xte, yte, mus):
    """Test MSE for every penalty in `mus` and the LOGO-selected penalty index."""
    n = len(ytr)
    xm, ym = Xtr.mean(0), ytr.mean()
    U, S, Vt = np.linalg.svd(Xtr - xm, full_matrices=False)
    uy = U.T @ (ytr - ym)
    Xte_c = Xte - xm
    D = S[None, :] / (S[None, :] ** 2 + n * mus[:, None])          # (M, r)
    B = (D * uy[None, :]) @ Vt                                      # (M, p)
    pred = Xte_c @ B.T + ym                                         # (n_te, M)
    test_mse = ((pred - yte[:, None]) ** 2).mean(0)
    cv = ridge_cv_path(Xtr, ytr, mus, groups=gtr)
    return test_mse, int(np.nanargmin(cv)), cv


def truth_curve(X, y, groups, pool, test, ns, seed, mu_rel=DEFAULT_MU_REL, with_pls=True, pls_max=30):
    """Expected test MSE of LOGO-tuned ridge (and 10-fold-CV PLS) trained on n random pool samples."""
    rng = np.random.default_rng(seed)
    lam_max = np.linalg.eigvalsh(np.cov(X[pool].T)).max()
    mus = mu_rel * lam_max
    Xte, yte = X[test], y[test]
    out = {"n": [], "ridge_mse": [], "ridge_se": [], "pls_mse": [], "pls_se": [], "ridge_mu_mse": [], "reps": [],
           "ridge_mse_reps": []}
    for n in ns:
        if n > len(pool):
            break
        R = reps_for(n)
        r_tuned, r_allmu, p_err = [], [], []
        for r in range(R):
            sub = rng.choice(pool, n, replace=False)
            tm, j, _ = _ridge_all_mu(X[sub], y[sub], groups[sub], Xte, yte, mus)
            r_tuned.append(tm[j]); r_allmu.append(tm)
            if with_pls:
                m = PLSCV(max_comp=pls_max, n_folds=10, seed=int(rng.integers(1 << 31))).fit(X[sub], y[sub], groups[sub])
                p_err.append(np.mean((m.predict(Xte) - yte) ** 2))
        out["n"].append(n); out["reps"].append(R)
        out["ridge_mse"].append(float(np.mean(r_tuned))); out["ridge_se"].append(float(np.std(r_tuned) / np.sqrt(R)))
        out["ridge_mu_mse"].append(np.mean(np.array(r_allmu), 0))
        out["ridge_mse_reps"].append(np.array(r_tuned))
        if with_pls:
            out["pls_mse"].append(float(np.mean(p_err))); out["pls_se"].append(float(np.std(p_err) / np.sqrt(R)))
    out["ridge_mu_mse"] = np.array(out["ridge_mu_mse"])
    mr = max(len(v) for v in out["ridge_mse_reps"])           # per-repetition MSE (NaN-padded), i.e. realised calibrations
    out["ridge_mse_reps"] = np.array([np.pad(v, (0, mr - len(v)), constant_values=np.nan) for v in out["ridge_mse_reps"]])
    out["mus"] = mus; out["lam_max"] = float(lam_max)
    return out
