import os, sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.training.learning_curves import split_task  # noqa: E402
from src.models.theory import power_signal, optimal_risk  # noqa: E402
from src.models.forecasters import (RPMForecaster, fit_rpm, forecast_theory, curve_forecast,  # noqa: E402
                                    eigen_spectrum, complete_tail_powerlaw)
from src.models.ridge import ridge_cv_path  # noqa: E402
from src.preprocessing.spectra import snv, preprocess  # noqa: E402


def test_split_is_group_disjoint_and_complete():
    rng = np.random.default_rng(0)
    groups = rng.integers(0, 300, size=2000).astype(str)
    pool, test = split_task(groups, seed=3)
    assert len(np.intersect1d(pool, test)) == 0
    assert len(pool) + len(test) == len(groups)
    assert len(set(groups[pool]) & set(groups[test])) == 0, "a group appears on both sides"


def test_split_deterministic():
    g = np.arange(500).astype(str)
    a = split_task(g, seed=11); b = split_task(g, seed=11)
    assert np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1])


def test_snv_rowwise_only():
    X = np.random.default_rng(1).normal(size=(10, 50))
    Z = snv(X)
    np.testing.assert_allclose(Z.mean(1), 0, atol=1e-12); np.testing.assert_allclose(Z.std(1), 1, atol=1e-12)
    # sample-wise: transforming a subset gives identical rows (no cross-sample information)
    np.testing.assert_allclose(snv(X[:3]), Z[:3])
    np.testing.assert_allclose(preprocess(X[:4], "sg1"), preprocess(X, "sg1")[:4])


def _synthetic(n, p=80, seed=0, sigma2=0.2):
    rng = np.random.default_rng(seed)
    lam = 1.0 / np.arange(1, p + 1) ** 1.6
    U = np.linalg.qr(rng.normal(size=(p, p)))[0]
    beta = U @ (rng.normal(size=p) * 1.0)   # isotropic coefficients => r = 1 in the eigenbasis
    X = rng.normal(size=(n, p)) @ (U * np.sqrt(lam)).T
    y = X @ beta + np.sqrt(sigma2) * rng.normal(size=n)
    return X, y, lam, U, beta


def test_rpm_recovers_learning_curve_on_synthetic_data():
    """Consistency check in a well-specified setting: with the true eigen-spectrum and a 240-sample
    pilot, the median RPM forecast of the n = 960 risk is within 20 % of the theoretical truth.
    (Variability for small pilots is quantified in experiment E0, not asserted here.)"""
    X, y, lam, U, beta = _synthetic(6000, seed=4)
    s_true = lam * (U.T @ beta) ** 2
    truth = optimal_risk(lam, s_true, 0.2, 960)[0]
    errs = []
    for s in range(8):
        idx = np.random.default_rng(s).choice(6000, 240, replace=False)
        f = RPMForecaster(n_boot=0).fit_forecast(X[idx], y[idx], None, lam, [960])
        errs.append(np.log(f["point"][0] / truth))
    assert abs(np.median(errs)) < np.log(1.2), errs


def test_rpm_forecast_never_below_fitted_noise():
    X, y, lam, _, _ = _synthetic(300, seed=5)
    e = ridge_cv_path(X[:80], y[:80], np.logspace(-12, 1, 53) * lam.max())
    p = fit_rpm(lam, e, 79.0)
    fc = forecast_theory(lam, p, [200, 800, 3200])
    assert np.all(fc >= np.exp(p["log_sigma2"]) * 0.999)
    assert fc[0] >= fc[1] >= fc[2]


def test_curve_forecast_ipl3_shapes():
    ms = np.array([20., 30., 40., 50.]); es = 0.3 + 2.0 * ms ** -0.7
    out = curve_forecast("IPL3", ms, es, [100, 400])
    assert out["point"][0] > out["point"][1] > 0.29


def test_tail_completion_monotone():
    lam = 1.0 / np.arange(1, 31) ** 1.5
    full = complete_tail_powerlaw(lam, 120)
    assert len(full) == 120 and np.all(np.diff(full[29:]) <= 0)


def test_eigen_spectrum_matches_covariance():
    X = np.random.default_rng(2).normal(size=(200, 10)) * np.arange(1, 11)
    lam = eigen_spectrum(X)
    np.testing.assert_allclose(np.sort(lam)[::-1], np.sort(np.linalg.eigvalsh(np.cov(X.T)))[::-1], rtol=1e-8)
