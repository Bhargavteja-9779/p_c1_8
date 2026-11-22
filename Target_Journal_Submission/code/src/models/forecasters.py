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
def _kappa_quadrature(k):
    """Trapezoid weights in log kappa: each path point represents the stretch of the kappa axis it covers.
    Near the interpolation limit many penalties map to (almost) the same kappa; they then share one weight
    instead of each counting as a separate observation (internal audit of version 1)."""
    lk = np.log(np.asarray(k, float))
    order = np.argsort(lk); ls = lk[order]
    if len(ls) < 2:
        return np.ones(len(ls))
    gaps = np.diff(ls)
    w_sorted = np.zeros(len(ls))
    w_sorted[:-1] += gaps / 2; w_sorted[1:] += gaps / 2
    w = np.empty(len(ls)); w[order] = w_sorted
    w = np.clip(w, 1e-6 * max(w.max(), 1e-300), None)
    return w / w.mean()


def _path_points(lam, e, n_eff, mu_rel, cutoff, w=None, kappa_weights=True):
    mus = mu_rel * lam.max()
    k = solve_kappa(lam, n_eff, mus)
    d2 = df2_of(lam, k)
    pref = (1.0 + 1.0 / n_eff) / (1.0 - d2 / n_eff)
    ok = np.isfinite(e) & (e > 0) & (d2 / n_eff <= cutoff)
    q = _kappa_quadrature(k[ok]) if kappa_weights else np.ones(int(ok.sum()))
    ww = q if w is None else q * w[ok]
    return k[ok], pref[ok], e[ok], ww


def fit_rpm(lam, path_mse, n_eff, mu_rel=DEFAULT_MU_REL, r_mode="fixed1", cutoff=0.8, r_prior=None, path_var_log=None, r_value=1.0,
            sigma2_floor=None, kappa_weights=True):
    """Fit (log tau2, r, log sigma2) to an observed CV path. Returns dict of parameters.

    If `sigma2_floor` > 0 is given, the noise variance is constrained to sigma2 >= sigma2_floor (used with a
    statistical noise-variance estimate, see dicker_noise).

    Path points are weighted by their spacing in log kappa (`kappa_weights=True`, default since version 2);
    `kappa_weights=False` reproduces the originally registered implementation, in which every penalty of the
    log-uniform mu grid counted equally. If `path_var_log` (delta-method variance of log CV-MSE per path point)
    is given, these weights are multiplied by heuristic inverse-variance weights (RPM-w)."""
    wv = None if path_var_log is None else 1.0 / np.clip(np.asarray(path_var_log, float), 1e-12, None)
    k, P, e, W = _path_points(lam, path_mse, n_eff, mu_rel, cutoff, wv, kappa_weights)
    if len(k) < 3:                      # documented fallback: relax the validity cut-off if < 3 points remain
        k, P, e, W = _path_points(lam, path_mse, n_eff, mu_rel, 0.95, wv, kappa_weights)
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
    ls_lo = np.log(v) - 25
    if sigma2_floor is not None and np.isfinite(sigma2_floor) and sigma2_floor > 0:
        ls_lo = min(max(ls_lo, float(np.log(sigma2_floor))), np.log(v) + 1.9)
    for frac_noise in (0.1, 0.4, 0.8):
        ls0 = min(max(np.log(max(frac_noise * np.min(e), 1e-12)), ls_lo + 1e-6), np.log(v) + 1.9)
        for r0 in ((r_fix,) if fixed else (0.3, 1.0, 1.8)):
            lt0 = np.log(max(v - frac_noise * np.min(e), 1e-12) / np.sum(ln ** r0))
            if fixed:
                x0 = [lt0, ls0]; bnds = [(lt0 - 25, lt0 + 25), (ls_lo, np.log(v) + 2)]
            else:
                x0 = [lt0, r0, ls0]; bnds = [(lt0 - 40, lt0 + 40), (-0.5, 3.0), (ls_lo, np.log(v) + 2)]
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
                 r_prior=None, cv="logo", weighted=False, r_value=1.0, sigma2_floor=None, kappa_weights=True):
        self.mu_rel = mu_rel; self.r_mode = r_mode; self.cutoff = cutoff
        self.n_boot = n_boot; self.seed = seed; self.r_prior = r_prior; self.cv = cv; self.weighted = weighted
        self.r_value = r_value; self.sigma2_floor = sigma2_floor; self.kappa_weights = kappa_weights

    def _path(self, X0, y0, g0, lam, w=None):
        """Returns (CV MSE path, variance of log CV MSE or None)."""
        mus = self.mu_rel * lam.max()
        if self.cv == "kfold10":
            return kfold_ridge_path(X0, y0, mus, g0, k=10, seed=self.seed), None
        if self.weighted:
            return ridge_cv_path(X0, y0, mus, groups=g0, weights=w, return_var=True)
        return ridge_cv_path(X0, y0, mus, groups=g0, weights=w), None

    def fit_forecast(self, X0, y0, g0, lam, ns):
        import time as _time
        _t0 = _time.perf_counter()
        n0 = len(y0)
        gsz = 1.0 if g0 is None else float(np.mean(np.unique(g0, return_counts=True)[1]))
        n_eff = n0 - gsz
        e, ev = self._path(X0, y0, g0, lam)
        self.params_ = fit_rpm(lam, e, n_eff, self.mu_rel, self.r_mode, self.cutoff, self.r_prior, ev, self.r_value,
                               self.sigma2_floor, self.kappa_weights)
        point = forecast_theory(lam, self.params_, ns, self.mu_rel)
        out = {"point": point, "params": self.params_, "path": e}
        self.t_point_ = _time.perf_counter() - _t0
        _t1 = _time.perf_counter()
        if self.n_boot and self.n_boot > 0:
            rng = np.random.default_rng(self.seed)
            sims = []
            gg = np.arange(n0) if g0 is None else np.unique(np.asarray(g0), return_inverse=True)[1]
            for _ in range(self.n_boot):
                wg = rng.dirichlet(np.ones(gg.max() + 1))        # Bayesian bootstrap over groups (clusters)
                w = wg[gg] / np.bincount(gg)[gg]
                w = w / w.sum() * n0
                eb, evb = self._path(X0, y0, g0, lam, w)
                pb = fit_rpm(lam, eb, n_eff, self.mu_rel, self.r_mode, self.cutoff, self.r_prior, evb, self.r_value,
                             self.sigma2_floor, self.kappa_weights)
                sims.append(forecast_theory(lam, pb, ns, self.mu_rel))
            sims = np.log(np.sqrt(np.array(sims)))
            out["boot_logrmse"] = sims
        self.t_boot_ = _time.perf_counter() - _t1
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
        return {"point": pt, "bands": {a: (np.log(np.sqrt(pt)), np.log(np.sqrt(pt))) for a in alphas}, "failed": True,
                "floored": np.zeros(len(ns), bool)}
    f, popt, pcov = fit
    raw = f(ns, *popt)
    floored = raw <= 1.0001e-12
    pt = np.maximum(raw, 1e-12)
    bands = {}
    eps = 1e-6
    G = np.zeros((len(ns), len(popt)))
    for i in range(len(popt)):
        dp = np.zeros(len(popt)); dp[i] = eps * max(1.0, abs(popt[i]))
        G[:, i] = (f(ns, *(popt + dp)) - f(ns, *(popt - dp))) / (2 * dp[i])
    pcov = np.where(np.isfinite(pcov), pcov, 0.0)
    sd = np.sqrt(np.clip(np.einsum("ij,jk,ik->i", G, pcov, G), 0, None))
    # delta-method bands on the log scale (sd of log MSE = sd / MSE); the MSE-scale bands used in the
    # first version were clipped at zero, which made them artificially wide
    sdl = sd / pt
    for a in alphas:
        z = norm.ppf(0.5 + a / 2)
        bands[a] = (0.5 * (np.log(pt) - z * sdl), 0.5 * (np.log(pt) + z * sdl))
    return {"point": pt, "bands": bands, "failed": False, "popt": popt, "floored": floored}


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


# --------------------------------------------------------------------------------------
# Pilot diagnostics added in version 2
# --------------------------------------------------------------------------------------
def nested_cv_mse(X0, y0, g0, mu_grid, k=10, seed=0):
    """Nested grouped CV estimate of the pilot's prediction MSE: outer grouped k-fold; within each outer
    training part the penalty is selected by exact LOGO (inner loop), so the estimate is free of the
    selection optimism of min_mu CV(mu)."""
    rng = np.random.default_rng(seed)
    g = np.arange(len(y0)) if g0 is None else np.asarray(g0)
    ug = np.unique(g); perm = rng.permutation(len(ug))
    fid_g = dict(zip(ug[perm], np.arange(len(ug)) % min(k, len(ug))))
    fid = np.array([fid_g[v] for v in g])
    sse = 0.0
    for f in np.unique(fid):
        tr, te = fid != f, fid == f
        if tr.sum() < 4:
            continue
        m = RidgeCV(mu_grid).fit(X0[tr], y0[tr], g[tr])
        sse += float(np.sum((m.predict(X0[te]) - y0[te]) ** 2))
    return sse / len(y0)


def pilot_test_mse(X0, y0, g0, mu_grid, Xte, yte):
    """Realised test MSE of the calibration actually obtained from the pilot (LOGO-selected penalty)."""
    m = RidgeCV(mu_grid).fit(X0, y0, g0)
    return float(np.mean((m.predict(Xte) - yte) ** 2))


def dicker_noise(X0, y0, mean_pool, lam_pool, V_pool, rel_tol=1e-10):
    """Method-of-moments estimate of the residual variance of the best linear predictor (Dicker 2014,
    Biometrika 101:269), with the predictors whitened by the (unlabelled) pool covariance.
    Returns (sigma2_hat, tau2_hat); either can be negative (unbiased moment estimates)."""
    keep = lam_pool > rel_tol * lam_pool.max()
    W = V_pool[:, keep] / np.sqrt(lam_pool[keep])[None, :]
    Z = (X0 - mean_pool) @ W
    yc = y0 - y0.mean()
    n, p = Z.shape
    yy = float(yc @ yc); zy = Z.T @ yc; zz = float(zy @ zy)
    n1 = n - 1                       # one degree of freedom used by centring y
    sig2 = (n1 + p + 1) / (n1 * (n1 + 1)) * yy - zz / (n1 * (n1 + 1))
    tau2 = -p / (n1 * (n1 + 1)) * yy + zz / (n1 * (n1 + 1))
    return float(sig2), float(tau2)


def wei_exponent(X0, y0, lam_pool, mu_grid, cutoff=0.8, kmax=60):
    """Scaling-exponent estimator of Wei, Hu & Steinhardt (ICML 2022, Props. 4-5): eigen-decay gamma from the
    (unlabelled) spectrum, lambda_k ~ k^-(1+gamma); alignment delta from the pilot regularisation path,
    y'(XX' + N lambda I)^-1 y ~ kappa(lambda, N)^(-(1-delta)/(1+gamma)); predicted MSE scaling n^-alpha with
    alpha = gamma + delta (noiseless, optimally tuned ridge)."""
    from .theory import solve_kappa, df2_of
    n0 = len(y0)
    lam = np.sort(lam_pool)[::-1]
    k = np.arange(1, min(kmax, int(np.sum(lam > 1e-12 * lam[0]))) + 1)
    slope = np.polyfit(np.log(k), np.log(lam[: len(k)]), 1)[0]
    gamma = -slope - 1.0
    Xc = X0 - X0.mean(0); yc = y0 - y0.mean()
    U, S, _ = np.linalg.svd(Xc, full_matrices=False)
    uy = U.T @ yc; rest = float(yc @ yc - uy @ uy)
    mus = np.asarray(mu_grid, float)
    kap = np.asarray(solve_kappa(lam_pool, n0, mus), float).ravel()
    okk = np.asarray(df2_of(lam_pool, kap), float).ravel() / n0 <= cutoff
    qs = np.array([float(np.sum(uy ** 2 / (S ** 2 + n0 * mu)) + rest / (n0 * mu)) for mu in mus])[okk]
    ks = kap[okk]
    if len(qs) < 3:
        return {"alpha": np.nan, "gamma": gamma, "delta": np.nan}
    b = np.polyfit(np.log(ks), np.log(qs), 1)[0]
    delta = 1.0 + b * (1.0 + gamma)
    return {"alpha": float(gamma + delta), "gamma": float(gamma), "delta": float(delta)}
