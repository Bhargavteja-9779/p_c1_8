"""Learning-curve forecasters for multivariate calibration.

Proposed: Regularisation-Path Matching (RPM).
  1. Eigen-spectrum lam_k of the population covariance from (cheap) unlabelled spectra.
  2. Exact leave-one-(group-)out MSE of ridge on the labelled pilot along a penalty grid.
  3. For each penalty mu_j the theory gives kappa_j = kappa(n_eff, mu_j) and the prefactor
     P_j = (1 + 1/n_eff) / (1 - df2(kappa_j)/n_eff); the pilot therefore observes the bias
     function N(kappa) only on kappa >= kappa_min(n0).
  4. A two-parameter model N(kappa) = sigma2 + tau2 * sum_k (lam_k/lam_1)^r (kappa/(lam_k+kappa))^2
     (r = 1, i.e. an isotropic coefficient prior) is fitted in log space to the observed path.
  5. Forecast at any n: min over the penalty grid of the theoretical risk (Eq. 2 in theory.py).
  6. Uncertainty: Bayesian bootstrap (Dirichlet weights) of the pilot.

Baselines: flat (no improvement), inverse power law with asymptote (IPL3), pure power law
(IPL2), exponential saturation (EXP3), logarithmic (LOG2) learning-curve extrapolation from
within-pilot sub-sampling, and a classical fixed-complexity degrees-of-freedom formula (DF-OLS).
"""
from __future__ import annotations

import warnings
import numpy as np
from scipy.optimize import minimize, curve_fit
from scipy.stats import norm

from .theory import solve_kappa, df2_of, bias_function, optimal_risk, power_signal, DEFAULT_MU_REL
from .ridge import ridge_cv_path, RidgeCV

warnings.filterwarnings("ignore", category=RuntimeWarning)


# --------------------------------------------------------------------------------------
# Eigen-spectrum helpers
# --------------------------------------------------------------------------------------
def eigen_spectrum(X, floor_rel=1e-14):
    Xc = np.asarray(X, float) - np.mean(X, 0)
    s = np.linalg.svd(Xc, compute_uv=False)
    lam = s ** 2 / max(len(Xc) - 1, 1)
    lam = lam[lam > floor_rel * lam[0]]
    return lam


def complete_tail_powerlaw(lam_obs, p, fit_frac=0.5):
    """Extend a truncated eigen-spectrum (e.g. from a small pilot) to p modes by a power-law tail."""
    k = np.arange(1, len(lam_obs) + 1)
    m = max(3, int(len(lam_obs) * fit_frac))
    sl, ic = np.polyfit(np.log(k[:m]), np.log(lam_obs[:m]), 1)
    kk = np.arange(1, p + 1)
    tail = np.exp(ic) * kk.astype(float) ** sl
    out = tail.copy(); out[:len(lam_obs)] = lam_obs
    return out


# --------------------------------------------------------------------------------------
# RPM
# --------------------------------------------------------------------------------------
def _path_points(lam, e, n_eff, mu_rel, cutoff, w=None):
    mus = mu_rel * lam.max()
    k = solve_kappa(lam, n_eff, mus)
    d2 = df2_of(lam, k)
    pref = (1.0 + 1.0 / n_eff) / (1.0 - d2 / n_eff)
    ok = np.isfinite(e) & (e > 0) & (d2 / n_eff <= cutoff)
    if w is None:
        return k[ok], pref[ok], e[ok]
    return k[ok], pref[ok], e[ok], w[ok]


def fit_rpm(lam, path_mse, n_eff, mu_rel=DEFAULT_MU_REL, r_mode="fixed1", cutoff=0.8, r_prior=None, path_var_log=None, r_value=1.0):
    """Fit (log tau2, r, log sigma2) to an observed CV path. Returns dict of parameters.

    If `path_var_log` (delta-method variance of log CV-MSE per path point) is given, the log-space
    least-squares fit is inverse-variance weighted (weights normalised to mean 1)."""
    wv = None if path_var_log is None else 1.0 / np.clip(np.asarray(path_var_log, float), 1e-12, None)
    if wv is None:
        k, P, e = _path_points(lam, path_mse, n_eff, mu_rel, cutoff); W = np.ones(len(k))
        if len(k) < 3:
            k, P, e = _path_points(lam, path_mse, n_eff, mu_rel, 0.95); W = np.ones(len(k))
    else:
        k, P, e, W = _path_points(lam, path_mse, n_eff, mu_rel, cutoff, wv)
        if len(k) < 3:
            k, P, e, W = _path_points(lam, path_mse, n_eff, mu_rel, 0.95, wv)
        W = W / W.mean()
    ln = lam / lam.max()
    B = (k[:, None] / (lam[None, :] + k[:, None])) ** 2      # (J, p)
    loge = np.log(e)
    v = float(np.max(e))

    def model(lt, r, ls):
        return P * (np.exp(ls) + (B @ (ln ** r)) * np.exp(lt))

    fixed = r_mode in ("fixed1", "fixed")
    r_fix = 1.0 if r_mode == "fixed1" else float(r_value)

    def loss(th):
        if fixed:
            lt, ls = th; r = r_fix
        else:
            lt, r, ls = th
        pen = 0.0 if (r_prior is None or fixed) else ((r - r_prior[0]) / r_prior[1]) ** 2
        return float(np.sum(W * (np.log(model(lt, r, ls)) - loge) ** 2)) + pen

    best = None
    for frac_noise in (0.1, 0.4, 0.8):
        ls0 = np.log(max(frac_noise * np.min(e), 1e-12))
        for r0 in ((r_fix,) if fixed else (0.3, 1.0, 1.8)):
            lt0 = np.log(max(v - frac_noise * np.min(e), 1e-12) / np.sum(ln ** r0))
            if fixed:
                x0 = [lt0, ls0]; bnds = [(lt0 - 25, lt0 + 25), (np.log(v) - 25, np.log(v) + 2)]
            else:
                x0 = [lt0, r0, ls0]; bnds = [(lt0 - 40, lt0 + 40), (-0.5, 3.0), (np.log(v) - 25, np.log(v) + 2)]
            res = minimize(loss, x0, method="L-BFGS-B", bounds=bnds)
            if best is None or res.fun < best.fun:
                best = res
    if fixed:
        lt, ls = best.x; r = r_fix
    else:
        lt, r, ls = best.x
    return {"log_tau2": float(lt), "r": float(r), "log_sigma2": float(ls), "loss": float(best.fun),
            "n_points": int(len(k))}


def forecast_theory(lam, params, ns, mu_rel=DEFAULT_MU_REL):
    s = power_signal(lam, params["log_tau2"], params["r"])
    sig2 = np.exp(params["log_sigma2"])
    return np.array([optimal_risk(lam, s, sig2, n, mu_rel)[0] for n in ns])


class RPMForecaster:
    name = "RPM"

    def __init__(self, mu_rel=DEFAULT_MU_REL, r_mode="fixed1", cutoff=0.8, n_boot=50, seed=0,
                 r_prior=None, cv="logo", weighted=False, r_value=1.0):
        self.mu_rel = mu_rel; self.r_mode = r_mode; self.cutoff = cutoff
        self.n_boot = n_boot; self.seed = seed; self.r_prior = r_prior; self.cv = cv; self.weighted = weighted
        self.r_value = r_value

    def _path(self, X0, y0, g0, lam, w=None):
        """Returns (CV MSE path, variance of log CV MSE or None)."""
        mus = self.mu_rel * lam.max()
        if self.cv == "kfold10":
            return kfold_ridge_path(X0, y0, mus, g0, k=10, seed=self.seed), None
        if self.weighted:
            return ridge_cv_path(X0, y0, mus, groups=g0, weights=w, return_var=True)
        return ridge_cv_path(X0, y0, mus, groups=g0, weights=w), None

    def fit_forecast(self, X0, y0, g0, lam, ns):
        n0 = len(y0)
        gsz = 1.0 if g0 is None else float(np.mean(np.unique(g0, return_counts=True)[1]))
        n_eff = n0 - gsz
        e, ev = self._path(X0, y0, g0, lam)
        self.params_ = fit_rpm(lam, e, n_eff, self.mu_rel, self.r_mode, self.cutoff, self.r_prior, ev, self.r_value)
        point = forecast_theory(lam, self.params_, ns, self.mu_rel)
        out = {"point": point, "params": self.params_, "path": e}
        if self.n_boot and self.n_boot > 0:
            rng = np.random.default_rng(self.seed)
            sims = []
            for _ in range(self.n_boot):
                w = rng.dirichlet(np.ones(n0)) * n0
                eb, evb = self._path(X0, y0, g0, lam, w)
                pb = fit_rpm(lam, eb, n_eff, self.mu_rel, self.r_mode, self.cutoff, self.r_prior, evb, self.r_value)
                sims.append(forecast_theory(lam, pb, ns, self.mu_rel))
            sims = np.log(np.sqrt(np.array(sims)))
            out["boot_logrmse"] = sims
        return out


def kfold_ridge_path(X, y, mus, groups=None, k=10, seed=0):
    """Grouped K-fold CV path (ablation alternative to exact LOGO)."""
    rng = np.random.default_rng(seed)
    n = len(y)
    g = np.arange(n) if groups is None else np.asarray(groups)
    ug = np.unique(g); perm = rng.permutation(len(ug))
    fid_g = dict(zip(ug[perm], np.arange(len(ug)) % min(k, len(ug))))
    fid = np.array([fid_g[v] for v in g])
    sse = np.zeros(len(mus))
    for f in np.unique(fid):
        tr, te = fid != f, fid == f
        Xm, ym = X[tr].mean(0), y[tr].mean()
        U, S, Vt = np.linalg.svd(X[tr] - Xm, full_matrices=False)
        uy = U.T @ (y[tr] - ym); m = tr.sum()
        Xte = X[te] - Xm
        for j, mu in enumerate(mus):
            b = Vt.T @ ((S / (S ** 2 + m * mu)) * uy)
            sse[j] += np.sum((Xte @ b + ym - y[te]) ** 2)
    return sse / n


def fit_ml2(lam_vecs, X0, y0, lam):
    """Marginal-likelihood (type-II ML) alternative to path matching (ablation)."""
    lam_val, U = lam_vecs
    n0 = len(y0)
    T0 = (X0 - X0.mean(0)) @ U
    y0c = y0 - y0.mean()
    ln = lam_val / lam_val.max()
    v = np.var(y0c)

    def nll(th):
        lt, ls = th
        wv = np.exp(lt) * ln ** 0.0 / lam_val.max()   # r = 1 => prior var of b_k = tau2 / lam_1
        K = (T0 * wv) @ T0.T + np.exp(ls) * np.eye(n0)
        try:
            Lc = np.linalg.cholesky(K)
        except np.linalg.LinAlgError:
            return 1e12
        a = np.linalg.solve(Lc, y0c)
        return 0.5 * a @ a + np.sum(np.log(np.diag(Lc)))
    best = None
    for f in (0.1, 0.4, 0.8):
        res = minimize(nll, [np.log(v * (1 - f) / ln.sum() + 1e-12), np.log(v * f + 1e-12)], method="L-BFGS-B",
                       bounds=[(np.log(v) - 30, np.log(v) + 10), (np.log(v) - 25, np.log(v) + 2)])
        if best is None or res.fun < best.fun:
            best = res
    return {"log_tau2": float(best.x[0]), "r": 1.0, "log_sigma2": float(best.x[1])}


# --------------------------------------------------------------------------------------
# Empirical learning-curve extrapolation baselines
# --------------------------------------------------------------------------------------
def pilot_subsample_curve(X0, y0, g0, mu_grid, fracs=(0.25, 0.4, 0.55, 0.7, 0.85), n_splits=20, seed=0):
    """Within-pilot learning curve: train ridge (inner LOGO-tuned) on m samples, validate on the rest."""
    rng = np.random.default_rng(seed)
    n0 = len(y0)
    g = np.arange(n0) if g0 is None else np.asarray(g0)
    ug = np.unique(g)
    ms, es = [], []
    for f in fracs:
        target = int(round(f * n0)); vals = []; sizes = []
        for _ in range(n_splits):
            perm = rng.permutation(ug)
            cnt = np.cumsum([np.sum(g == u) for u in perm])
            kk = int(np.searchsorted(cnt, target)) + 1
            trg = set(perm[:kk].tolist())
            tr = np.array([v in trg for v in g])
            if tr.sum() < 5 or (~tr).sum() < 3:
                continue
            m = RidgeCV(mu_grid).fit(X0[tr], y0[tr], g[tr])
            vals.append(np.mean((m.predict(X0[~tr]) - y0[~tr]) ** 2)); sizes.append(tr.sum())
        if vals:
            ms.append(float(np.mean(sizes))); es.append(float(np.mean(vals)))
    full = ridge_cv_path(X0, y0, mu_grid, groups=g0)
    gsz = float(np.mean(np.unique(g, return_counts=True)[1]))
    ms.append(n0 - gsz); es.append(float(np.min(full)))
    return np.array(ms), np.array(es)


CURVES = {
    "IPL3": (lambda m, a, b, c: a + b * m ** (-c), lambda e: [0.5 * e.min(), e.max() * 2, 0.5],
             ([0, 0, 0.01], [np.inf, np.inf, 3.0])),
    "IPL2": (lambda m, b, c: b * m ** (-c), lambda e: [e.max() * 2, 0.3], ([0, 0.0], [np.inf, 3.0])),
    "EXP3": (lambda m, a, b, c: a + b * np.exp(-c * m), lambda e: [0.8 * e.min(), e.max(), 0.01],
             ([0, 0, 1e-6], [np.inf, np.inf, 1.0])),
    "LOG2": (lambda m, a, b: np.maximum(a - b * np.log(m), 1e-12), lambda e: [e.max() * 1.5, 0.1 * e.max()],
             ([0, 0], [np.inf, np.inf])),
}


def fit_curve(kind, ms, es):
    f, p0f, bnds = CURVES[kind]
    try:
        popt, pcov = curve_fit(f, ms, es, p0=p0f(es), bounds=bnds, sigma=1.0 / np.sqrt(ms), maxfev=50000)
    except Exception:
        return None
    return f, popt, pcov


def curve_forecast(kind, ms, es, ns, alphas=(0.8, 0.95)):
    fit = fit_curve(kind, ms, es)
    ns = np.asarray(ns, float)
    if fit is None:
        pt = np.full(len(ns), es[-1])
        return {"point": pt, "bands": {a: (np.log(np.sqrt(pt)), np.log(np.sqrt(pt))) for a in alphas}, "failed": True}
    f, popt, pcov = fit
    pt = np.maximum(f(ns, *popt), 1e-12)
    bands = {}
    eps = 1e-6
    G = np.zeros((len(ns), len(popt)))
    for i in range(len(popt)):
        dp = np.zeros(len(popt)); dp[i] = eps * max(1.0, abs(popt[i]))
        G[:, i] = (f(ns, *(popt + dp)) - f(ns, *(popt - dp))) / (2 * dp[i])
    pcov = np.where(np.isfinite(pcov), pcov, 0.0)
    sd = np.sqrt(np.clip(np.einsum("ij,jk,ik->i", G, pcov, G), 0, None))
    for a in alphas:
        z = norm.ppf(0.5 + a / 2)
        lo = np.maximum(pt - z * sd, 1e-12); hi = pt + z * sd
        bands[a] = (np.log(np.sqrt(lo)), np.log(np.sqrt(hi)))
    return {"point": pt, "bands": bands, "failed": False, "popt": popt}


def flat_forecast(X0, y0, g0, mu_grid, ns):
    e = ridge_cv_path(X0, y0, mu_grid, groups=g0)
    return np.full(len(ns), float(np.min(e)))


def dfols_forecast(X0, y0, g0, mu_grid, ns):
    """Classical fixed-complexity formula: E(n) = s2 * (1 + 1/n + df/(n - df - 1)), df = tr(H) at the
    pilot-optimal ridge penalty and s2 = RSS/(n0 - df - 1)."""
    n0 = len(y0)
    m = RidgeCV(mu_grid).fit(X0, y0, g0)
    Xc = X0 - X0.mean(0)
    S = np.linalg.svd(Xc, compute_uv=False)
    df = float(np.sum(S ** 2 / (S ** 2 + n0 * m.mu_)))
    rss = float(np.sum((m.predict(X0) - y0) ** 2))
    s2 = rss / max(n0 - df - 1, 1.0)
    ns = np.asarray(ns, float)
    return s2 * (1 + 1 / ns + df / np.maximum(ns - df - 1, 1.0))
