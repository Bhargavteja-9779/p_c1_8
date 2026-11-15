"""Deterministic-equivalent (random-matrix) risk of ridge regression.

Notation (per-sample normalisation): a ridge model trained on n samples solves
    beta_hat = argmin (1/n) sum_i (y_i - a - x_i' beta)^2 + mu * ||beta||^2 .
Let Sigma = sum_k lam_k u_k u_k' be the population covariance of the (pre-processed)
spectra, s_k the target power carried by mode k (variance of the linear part of
E[y|x] along u_k) and sigma2 the residual (irreducible + non-linear) variance.

The effective regularisation kappa = kappa(n, mu) is the unique root in
[mu, mu + tr(Sigma)/n] of
    kappa * (1 - (1/n) * sum_k lam_k / (lam_k + kappa)) = mu .            (Eq. 1)
The expected test MSE (on noisy test labels) is then approximated by
    E(n, mu) = (1 + 1/n) * N(kappa) / (1 - df2(kappa)/n),                 (Eq. 2)
    N(kappa) = sigma2 + sum_k s_k * (kappa / (lam_k + kappa))^2,          (Eq. 3)
    df2(kappa) = sum_k (lam_k / (lam_k + kappa))^2 ,                       (Eq. 4)
where the factor (1 + 1/n) accounts for estimating the intercept.
References: Dobriban & Wager (2018, Ann. Stat.); Hastie et al. (2022, Ann. Stat.);
Bordelon et al. (2020, ICML); Canatar et al. (2021, Nat. Commun.); Simon et al.
(2023, TMLR); Atanasov et al. (2024).
"""
from __future__ import annotations

import numpy as np

DEFAULT_MU_REL = np.logspace(-12, 1, 53)


def solve_kappa(lam: np.ndarray, n: float, mu: np.ndarray, iters: int = 80) -> np.ndarray:
    """Vectorised bisection (in log space) for Eq. 1. `mu` may be an array (>0)."""
    lam = np.asarray(lam, float)
    mu = np.atleast_1d(np.asarray(mu, float))
    lo = np.log(mu)
    hi = np.log(mu + lam.sum() / n + 1e-300)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        k = np.exp(mid)
        g = k * (1.0 - (lam[None, :] / (lam[None, :] + k[:, None])).sum(1) / n) - mu
        pos = g > 0
        hi = np.where(pos, mid, hi)
        lo = np.where(pos, lo, mid)
    return np.exp(0.5 * (lo + hi))


def df2_of(lam: np.ndarray, kappa: np.ndarray) -> np.ndarray:
    L = lam[None, :] / (lam[None, :] + np.atleast_1d(kappa)[:, None])
    return (L ** 2).sum(1)


def bias_function(lam: np.ndarray, s: np.ndarray, sigma2: float, kappa: np.ndarray) -> np.ndarray:
    """N(kappa) of Eq. 3 for an array of kappa values."""
    kappa = np.atleast_1d(kappa)
    B = (kappa[:, None] / (lam[None, :] + kappa[:, None])) ** 2
    return sigma2 + B @ s


def risk(lam, s, sigma2, n, mu, intercept=True):
    """Eq. 2 for each mu (array). Returns np.inf where df2 >= n (theory invalid)."""
    mu = np.atleast_1d(mu)
    k = solve_kappa(lam, n, mu)
    d2 = df2_of(lam, k)
    N = bias_function(lam, s, sigma2, k)
    pref = (1.0 + 1.0 / n) if intercept else 1.0
    with np.errstate(divide="ignore", invalid="ignore"):
        out = pref * N / (1.0 - d2 / n)
    out[d2 >= n] = np.inf
    return out


def optimal_risk(lam, s, sigma2, n, mu_rel=DEFAULT_MU_REL, intercept=True):
    """min over the ridge grid of Eq. 2 -> approximates a CV-tuned ridge calibration."""
    r = risk(lam, s, sigma2, n, mu_rel * lam.max(), intercept=intercept)
    j = int(np.argmin(r))
    return float(r[j]), float(mu_rel[j] * lam.max())


def power_signal(lam: np.ndarray, log_tau2: float, r: float) -> np.ndarray:
    """Parametric target-power spectrum s_k = tau2 * (lam_k/lam_1)^r (r = 1: isotropic prior)."""
    return np.exp(log_tau2) * (lam / lam.max()) ** r
