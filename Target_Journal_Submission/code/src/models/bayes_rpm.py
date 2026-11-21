"""Bayesian regularisation-path matching (B-RPM).

Motivation (Proposition 1 of the manuscript, "observability horizon"): a pilot of n0 samples observes the bias
function N(kappa) only for kappa >= kappa_min(n0). Target power carried by modes with eigenvalues below
kappa_min(n0) is (to first order in lam_k/kappa) indistinguishable from irreducible noise in the pilot, yet it is
learned when the calibration grows to n. The gain from n0 to n therefore depends on a quantity the pilot cannot
measure, and every pilot-based forecaster has to supply it from prior knowledge, explicitly or implicitly
(FLAT: "no learnable tail"; power laws: "the tail continues the within-pilot trend").

B-RPM makes that prior explicit and transferable at the level of *structure* instead of the level of curves:
  * model   N(kappa) = V * [ eta + (1 - eta) * b_r(kappa) ],
            b_r(kappa) = sum_k (lam_k/lam_1)^r (kappa/(lam_k+kappa))^2 / sum_k (lam_k/lam_1)^r ,
    eta = irreducible-noise fraction, r = alignment exponent, V = total variance (N(inf) = V);
    lam_k from (cheap) unlabelled spectra of the task itself;
  * prior   r ~ N(m_r, s_r^2), logit(eta) ~ N(m_e, s_e^2), estimated from large-sample fits of *previous*
            calibrations of other data sources (no information from the task being forecast);
  * likelihood: the pilot's exact leave-one-(group-)out path, log CV-MSE residuals with variance s2 (delta-method
            variance of log CV-MSE at the pilot optimum) and kappa-quadrature weights normalised to an effective
            number of independent path observations m_eff (fixed at 2 a priori: level and curvature);
            V is profiled out (weighted mean of log residuals);
  * forecast: posterior-predictive mixture over a (r, eta) grid of the deterministic-equivalent optimal risk at n,
            with the anchor (level) uncertainty added as a Gaussian of sd = 0.5*sqrt(s2) on log RMSE.

All kappa-dependent quantities are independent of (r, eta, V) and are precomputed once per pilot, so the full
posterior over 1,200 grid cells costs a few milliseconds.

Also provides `posterior_information`: the prior-to-posterior contraction of the gain forecast, a per-pilot measure
of how much the pilot itself says about the future gain (0 = nothing beyond the prior, 1 = fully determined).
"""
from __future__ import annotations

import numpy as np
from scipy.special import expit, logit, logsumexp
from scipy.stats import norm

from .theory import solve_kappa, df2_of, DEFAULT_MU_REL
from .forecasters import _kappa_quadrature

R_GRID = np.linspace(0.05, 1.6, 32)
ETA_GRID = expit(np.linspace(logit(5e-4), logit(0.97), 40))


def _bnorm(lam, kappa, r_grid):
    """b_r(kappa) for each kappa (rows) and r (columns), normalised so that b_r(inf) = 1."""
    ln = lam / lam.max()
    Wr = ln[:, None] ** r_grid[None, :]                                # (p, R)
    B = (kappa[:, None] / (lam[None, :] + kappa[:, None])) ** 2         # (J, p)
    return (B @ Wr) / Wr.sum(0)[None, :]                               # (J, R)


def precompute_horizons(lam, ns, mu_rel=DEFAULT_MU_REL, r_grid=R_GRID):
    """For each horizon n: prefactor P_j(n) and b_r(kappa_j(n)) over the penalty grid (J) -> arrays (H, J), (H, J, R)."""
    mus = mu_rel * lam.max()
    P, Bn = [], []
    for n in ns:
        k = solve_kappa(lam, float(n), mus)
        d2 = df2_of(lam, k)
        with np.errstate(divide="ignore", invalid="ignore"):
            pref = (1.0 + 1.0 / n) / (1.0 - d2 / n)
        pref[d2 >= n] = np.inf
        P.append(pref); Bn.append(_bnorm(lam, k, r_grid))
    return np.array(P), np.array(Bn)


def fit_forecast_brpm(lam, path_mse, n_eff, ns, prior, path_var_log_opt, mu_rel=DEFAULT_MU_REL, cutoff=0.8,
                      m_eff=2.0, r_grid=R_GRID, eta_grid=ETA_GRID, pre=None, alphas=(0.8, 0.95)):
    """prior = dict(m_r, s_r, m_e, s_e) (m_e, s_e on the logit-eta scale; s_r or s_e = inf -> flat prior).
    Returns dict(point: forecast MSE per horizon, bands: {alpha: (lo, hi) log RMSE}, post: posterior summary)."""
    mus = mu_rel * lam.max()
    k = solve_kappa(lam, n_eff, mus)
    d2 = df2_of(lam, k)
    pref = (1.0 + 1.0 / n_eff) / (1.0 - d2 / n_eff)
    e = np.asarray(path_mse, float)
    ok = np.isfinite(e) & (e > 0) & (d2 / n_eff <= cutoff)
    if ok.sum() < 3:
        ok = np.isfinite(e) & (e > 0) & (d2 / n_eff <= 0.95)
    k, pref, loge = k[ok], pref[ok], np.log(e[ok])
    w = _kappa_quadrature(k)
    w = w / w.sum() * m_eff
    b0 = _bnorm(lam, k, r_grid)                                         # (J, R)
    # model in log space: log e_j = log V + log P_j + log(eta + (1-eta) b0_jr)
    shape = np.log(eta_grid[None, None, :] + (1 - eta_grid[None, None, :]) * b0[:, :, None])   # (J, R, E)
    resid0 = loge[:, None, None] - np.log(pref)[:, None, None] - shape                          # (J, R, E)
    logV = np.tensordot(w, resid0, axes=(0, 0)) / w.sum()                                       # (R, E)
    sse = np.tensordot(w, (resid0 - logV[None]) ** 2, axes=(0, 0))                              # (R, E)
    s2 = float(max(path_var_log_opt, 1e-4))
    loglik = -0.5 * sse / s2
    lp_r = 0.0 if not np.isfinite(prior["s_r"]) else -0.5 * ((r_grid - prior["m_r"]) / prior["s_r"]) ** 2
    le = logit(eta_grid)
    lp_e = 0.0 if not np.isfinite(prior["s_e"]) else -0.5 * ((le - prior["m_e"]) / prior["s_e"]) ** 2
    logprior = np.add.outer(np.broadcast_to(lp_r, r_grid.shape), np.broadcast_to(lp_e, eta_grid.shape))
    logpost = loglik + logprior
    post = np.exp(logpost - logsumexp(logpost))                                                  # (R, E)
    logprior_n = logprior - logsumexp(logprior)
    prior_w = np.exp(logprior_n)
    # forecasts per grid cell
    if pre is None:
        pre = precompute_horizons(lam, ns, mu_rel, r_grid)
    P, Bn = pre                                                                                   # (H,J), (H,J,R)
    H = P.shape[0]
    mean_lr = np.empty(H); lo = {a: np.empty(H) for a in alphas}; hi = {a: np.empty(H) for a in alphas}
    gain_post_sd = np.empty(H); gain_prior_sd = np.empty(H)
    lr_cells_all = []
    sd_a = 0.5 * np.sqrt(s2)
    for h in range(H):
        # risk/V = min_j P_j (eta + (1-eta) b_jr)
        val = P[h][:, None, None] * (eta_grid[None, None, :] + (1 - eta_grid[None, None, :]) * Bn[h][:, :, None])
        rmin = np.min(val, axis=0)                                                                # (R, E)
        lr = 0.5 * (logV + np.log(rmin))                                                          # log RMSE per cell
        lr_cells_all.append(lr)
        mean_lr[h] = float(np.sum(post * lr))
        # predictive mixture quantiles (cells x Gaussian anchor noise)
        grid = np.linspace(lr.min() - 5 * sd_a, lr.max() + 5 * sd_a, 600)
        cdf = np.sum(post[..., None] * norm.cdf((grid[None, None, :] - lr[..., None]) / sd_a), axis=(0, 1))
        for a in alphas:
            lo[a][h] = float(np.interp(0.5 - a / 2, cdf, grid)); hi[a][h] = float(np.interp(0.5 + a / 2, cdf, grid))
    # information about the gain (relative to the anchor at the first horizon) contributed by the pilot
    lr0 = lr_cells_all[0]
    for h in range(H):
        gcell = lr_cells_all[h] - lr0
        mpost = np.sum(post * gcell); mprior = np.sum(prior_w * gcell)
        gain_post_sd[h] = np.sqrt(max(np.sum(post * (gcell - mpost) ** 2), 0))
        gain_prior_sd[h] = np.sqrt(max(np.sum(prior_w * (gcell - mprior) ** 2), 0))
    pr = post.sum(1); pe = post.sum(0)
    summary = {"r_post_mean": float(pr @ r_grid), "eta_post_mean": float(pe @ eta_grid),
               "r_post_sd": float(np.sqrt(max(pr @ (r_grid - pr @ r_grid) ** 2, 0))),
               "logit_eta_post_sd": float(np.sqrt(max(pe @ (le - pe @ le) ** 2, 0))),
               "s2": s2, "n_points": int(ok.sum())}
    with np.errstate(divide="ignore", invalid="ignore"):
        info = 1.0 - (gain_post_sd / gain_prior_sd) ** 2
    return {"point_logrmse": mean_lr, "point": np.exp(2 * mean_lr), "bands": {a: (lo[a], hi[a]) for a in alphas},
            "post": summary, "info_gain": info, "gain_post_sd": gain_post_sd, "gain_prior_sd": gain_prior_sd}


def prior_from_table(tab, exclude_sources=(), exclude_families=(), sd_floor_r=0.1, sd_floor_e=0.3):
    """Robust prior moments from large-sample fits of other calibrations (columns r_full_pool, noise_frac_full_pool,
    source, family)."""
    t = tab[~tab.source.isin(exclude_sources) & ~tab.family.isin(exclude_families)]
    r = t.r_full_pool.to_numpy(float)
    e = logit(np.clip(t.noise_frac_full_pool.to_numpy(float), 1e-4, 0.99))
    mad = lambda x: 1.4826 * np.median(np.abs(x - np.median(x)))
    return {"m_r": float(np.median(r)), "s_r": float(max(mad(r), sd_floor_r)),
            "m_e": float(np.median(e)), "s_e": float(max(mad(e), sd_floor_e)), "n_cal": int(len(t))}
