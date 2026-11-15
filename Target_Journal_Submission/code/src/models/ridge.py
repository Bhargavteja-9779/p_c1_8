"""Ridge and PLS calibration models with exact closed-form cross-validation.

Ridge (per-sample normalisation, unpenalised intercept):
    min_{a,beta} sum_i w_i (y_i - a - x_i' beta)^2 + n * mu * ||beta||^2 .
For a linear smoother y_hat = H y, deleting a group g gives the exact residuals
    r_g = (I - H_gg)^{-1} e_g ,  e = y - y_hat ,
which is used for leave-one-out (groups of size 1) and leave-one-group-out CV.
"""
from __future__ import annotations

import numpy as np


def _group_batches(groups, n):
    """Partition sample indices into batches of equal-size groups: {size: int array (G, size)}."""
    if groups is None:
        return {1: np.arange(n)[:, None]}
    groups = np.asarray(groups)
    _, inv, counts = np.unique(groups, return_inverse=True, return_counts=True)
    order = np.argsort(inv, kind="stable")
    starts = np.concatenate([[0], np.cumsum(counts)[:-1]])
    batches = {}
    for size in np.unique(counts):
        gids = np.flatnonzero(counts == size)
        idx = order[starts[gids][:, None] + np.arange(size)[None, :]]
        batches[int(size)] = idx
    return batches


def ridge_cv_path(X, y, mus, groups=None, weights=None, return_var=False):
    """Exact (weighted) LOO / LOGO mean-squared error for each per-sample ridge penalty in `mus`.

    Leave-one-group-out residuals r_g = (I - H_gg)^{-1} e_g are computed in batches of
    equal-size groups. Returns CV MSE values (weighted by `weights` if given).
    """
    X = np.asarray(X, float); y = np.asarray(y, float)
    n = len(y)
    w = np.ones(n) if weights is None else np.asarray(weights, float) * n / np.sum(weights)
    sw = w.sum()
    xm = (w[:, None] * X).sum(0) / sw
    ym = (w * y).sum() / sw
    Xc = X - xm; yc = y - ym
    sq = np.sqrt(w)
    Z = sq[:, None] * Xc
    U, S, _ = np.linalg.svd(Z, full_matrices=False)
    Uty = U.T @ (sq * yc)
    S2 = S ** 2
    batches = _group_batches(groups, n)
    out = np.empty(len(np.atleast_1d(mus)))
    var_log = np.empty(len(out))
    for j, mu in enumerate(np.atleast_1d(mus)):
        d = S2 / (S2 + n * mu)
        e = yc - (U @ (d * Uty)) / sq
        r = np.empty(n)
        for size, idx in batches.items():
            if size == 1:
                i = idx[:, 0]
                hii = (U[i] ** 2) @ d + w[i] / sw
                r[i] = e[i] / np.clip(1.0 - hii, 1e-10, None)
            else:
                Ug = U[idx]                                   # (G, s, r)
                M = np.einsum("gir,r,gjr->gij", Ug, d, Ug)    # [U D U']_gg
                sg = sq[idx]
                H = M * (sg[:, None, :] / sg[:, :, None]) + (w[idx] / sw)[:, None, :]
                A = np.eye(size)[None] - H
                try:
                    r[idx] = np.linalg.solve(A, e[idx][..., None])[..., 0]
                except np.linalg.LinAlgError:
                    r[idx] = np.stack([np.linalg.lstsq(a, b, rcond=None)[0] for a, b in zip(A, e[idx])])
        out[j] = np.sum(w * r ** 2) / sw
        if return_var:
            # delta-method variance of log(CV MSE) from the spread of the squared CV residuals
            v = np.sum(w ** 2 * (r ** 2 - out[j]) ** 2) / sw ** 2
            var_log[j] = v / max(out[j] ** 2, 1e-300)
    if return_var:
        return out, var_log
    return out


class RidgeCV:
    """Ridge with the penalty chosen by exact LOO / LOGO over a grid of per-sample penalties."""

    def __init__(self, mus, groups_cv=True):
        self.mus = np.atleast_1d(mus)
        self.groups_cv = groups_cv

    def fit(self, X, y, groups=None):
        X = np.asarray(X, float); y = np.asarray(y, float)
        cv = ridge_cv_path(X, y, self.mus, groups if self.groups_cv else None)
        j = int(np.nanargmin(cv))
        self.mu_ = float(self.mus[j]); self.cv_path_ = cv; self.cv_mse_ = float(cv[j])
        self.xm_ = X.mean(0); self.ym_ = y.mean()
        Xc = X - self.xm_
        U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
        n = len(y)
        self.coef_ = Vt.T @ ((S / (S ** 2 + n * self.mu_)) * (U.T @ (y - self.ym_)))
        return self

    def predict(self, X):
        return (np.asarray(X, float) - self.xm_) @ self.coef_ + self.ym_


def pls1_coefs(X, y, n_comp):
    """Kernel PLS1 (Dayal & MacGregor 1997). Returns (coef matrix p x A, xm, ym) for 1..A components."""
    X = np.asarray(X, float); y = np.asarray(y, float)
    xm = X.mean(0); ym = y.mean()
    Xc = X - xm; yc = y - ym
    XtX = Xc.T @ Xc
    Xty = Xc.T @ yc
    p = X.shape[1]
    A = int(min(n_comp, len(y) - 1, p))
    W = np.zeros((p, A)); P = np.zeros((p, A)); Q = np.zeros(A); R = np.zeros((p, A))
    B = np.zeros((p, A))
    xy = Xty.copy()
    for a in range(A):
        w = xy / (np.linalg.norm(xy) + 1e-300)
        r = w.copy()
        for j in range(a):
            r = r - (P[:, j] @ w) * R[:, j]
        tt = r @ XtX @ r
        if tt <= 1e-300:
            A = a; break
        pa = (XtX @ r) / tt
        qa = (xy @ r) / tt
        xy = xy - pa * qa * tt
        W[:, a] = w; P[:, a] = pa; Q[a] = qa; R[:, a] = r
        B[:, a] = (R[:, :a + 1] @ Q[:a + 1])
    return B[:, :max(A, 1)], xm, ym


class PLSCV:
    """PLS1 with the number of latent variables chosen by K-fold (grouped) cross-validation."""

    def __init__(self, max_comp=30, n_folds=10, seed=0):
        self.max_comp = max_comp; self.n_folds = n_folds; self.seed = seed

    def fit(self, X, y, groups=None):
        X = np.asarray(X, float); y = np.asarray(y, float)
        n = len(y)
        rng = np.random.default_rng(self.seed)
        g = np.arange(n) if groups is None else np.asarray(groups)
        ug = np.unique(g)
        folds = min(self.n_folds, len(ug))
        perm = rng.permutation(len(ug))
        fold_of_group = dict(zip(ug[perm], np.arange(len(ug)) % folds))
        fid = np.array([fold_of_group[v] for v in g])
        A = int(min(self.max_comp, n - n // folds - 2, X.shape[1]))
        A = max(A, 1)
        sse = np.zeros(A)
        for f in range(folds):
            tr = fid != f; te = ~tr
            B, xm, ym = pls1_coefs(X[tr], y[tr], A)
            pred = (X[te] - xm) @ B + ym
            k = pred.shape[1]
            sse[:k] += ((pred - y[te][:, None]) ** 2).sum(0)
            if k < A:
                sse[k:] += np.inf
        self.n_comp_ = int(np.argmin(sse)) + 1
        self.cv_mse_ = float(sse[self.n_comp_ - 1] / n)
        B, self.xm_, self.ym_ = pls1_coefs(X, y, self.n_comp_)
        self.coef_ = B[:, -1]
        return self

    def predict(self, X):
        return (np.asarray(X, float) - self.xm_) @ self.coef_ + self.ym_
