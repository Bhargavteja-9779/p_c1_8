import os, sys
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.models.theory import solve_kappa, risk, optimal_risk, power_signal  # noqa: E402
from src.models.ridge import ridge_cv_path, RidgeCV, pls1_coefs, PLSCV  # noqa: E402


def _brute_cv(X, y, mu, groups=None, w=None):
    n = len(y)
    w = np.ones(n) if w is None else w * n / w.sum()
    g = np.arange(n) if groups is None else np.asarray(groups)
    se = np.zeros(n)
    for gg in np.unique(g):
        te = g == gg; tr = ~te
        wt = w[tr]
        xm = (wt[:, None] * X[tr]).sum(0) / wt.sum(); ym = (wt * y[tr]).sum() / wt.sum()
        Xc = X[tr] - xm
        A = Xc.T @ (wt[:, None] * Xc) + n * mu * np.eye(X.shape[1])
        b = np.linalg.solve(A, Xc.T @ (wt * (y[tr] - ym)))
        se[te] = (y[te] - ((X[te] - xm) @ b + ym)) ** 2
    return np.sum(w * se) / w.sum()


@pytest.mark.parametrize("use_groups,use_w", [(False, False), (True, False), (False, True), (True, True)])
def test_ridge_cv_closed_form_matches_brute_force(use_groups, use_w):
    rng = np.random.default_rng(0)
    n, p = 40, 15
    X = rng.normal(size=(n, p)); y = X @ rng.normal(size=p) + rng.normal(size=n)
    groups = rng.integers(0, 25, size=n) if use_groups else None
    w = rng.dirichlet(np.ones(n)) * n if use_w else None
    mus = np.array([1e-3, 1e-1, 1.0])
    fast = ridge_cv_path(X, y, mus, groups=groups, weights=w)
    slow = np.array([_brute_cv(X, y, m, groups, w) for m in mus])
    # with weights, deleting a point is not the same as zeroing its weight in the brute-force
    # reference only through the n*mu scaling; both use the full-sample n, so they agree exactly
    np.testing.assert_allclose(fast, slow, rtol=1e-6)


def test_pls_matches_sklearn():
    from sklearn.cross_decomposition import PLSRegression
    rng = np.random.default_rng(1)
    X = rng.normal(size=(60, 20)); y = X[:, :3].sum(1) + 0.1 * rng.normal(size=60)
    B, xm, ym = pls1_coefs(X, y, 5)
    for a in (1, 3, 5):
        sk = PLSRegression(n_components=a, scale=False).fit(X, y)
        np.testing.assert_allclose((X - xm) @ B[:, a - 1] + ym, sk.predict(X).ravel(), rtol=1e-6, atol=1e-8)


def test_kappa_solves_fixed_point():
    lam = np.logspace(0, -6, 200)
    for n in (20, 100, 1000):
        mu = np.logspace(-9, 0, 10)
        k = solve_kappa(lam, n, mu)
        lhs = k * (1 - (lam[None, :] / (lam[None, :] + k[:, None])).sum(1) / n)
        # when kappa >> mu (p > n, tiny mu) the bracket suffers double-precision cancellation;
        # the residual is therefore checked relative to kappa, which is what enters the risk.
        np.testing.assert_allclose(lhs, mu, rtol=1e-6, atol=1e-13 * k.max())


def test_theory_matches_simulation_gaussian():
    """Deterministic-equivalent risk vs Monte-Carlo ridge on Gaussian design (known truth)."""
    rng = np.random.default_rng(2)
    p = 120
    lam = 1.0 / np.arange(1, p + 1) ** 1.5
    U = np.linalg.qr(rng.normal(size=(p, p)))[0]
    b = rng.normal(size=p) * np.sqrt(lam) * 2.0       # coefficients in eigenbasis
    beta = U @ b
    s = lam * b ** 2
    sigma2 = 0.3
    Sig_half = U * np.sqrt(lam)
    Xt = rng.normal(size=(4000, p)) @ Sig_half.T
    yt = Xt @ beta + np.sqrt(sigma2) * rng.normal(size=4000)
    for n in (40, 160, 640):
        for mu in (1e-3, 1e-2):
            errs = []
            for _ in range(60):
                X = rng.normal(size=(n, p)) @ Sig_half.T
                y = X @ beta + np.sqrt(sigma2) * rng.normal(size=n)
                xm, ym = X.mean(0), y.mean()
                bh = np.linalg.solve((X - xm).T @ (X - xm) / n + mu * np.eye(p), (X - xm).T @ (y - ym) / n)
                errs.append(np.mean(((Xt - xm) @ bh + ym - yt) ** 2))
            th = risk(lam, s, sigma2, n, np.array([mu]))[0]
            assert abs(th / np.mean(errs) - 1) < 0.06, (n, mu, th, np.mean(errs))


def test_optimal_risk_decreases_with_n():
    lam = np.logspace(0, -8, 150)
    s = power_signal(lam, np.log(0.5), 1.0)
    vals = [optimal_risk(lam, s, 0.1, n)[0] for n in (25, 50, 100, 400, 1600)]
    assert all(a >= b - 1e-12 for a, b in zip(vals, vals[1:]))
    assert vals[-1] > 0.1  # never below the noise floor
