"""E0: controlled simulation with Monte-Carlo ground truth.

Gaussian design x ~ N(0, Sigma), Sigma eigenvalues lam_k = k^-1.6 (p = 150, random eigenvectors),
y = x' beta + eps with target power s_k = lam_k * b_k^2 and E[s_k] proportional to lam_k^r.
r = 1 is the isotropic case assumed by default RPM; r = 0.5 (signal in weak modes) and r = 2
(signal in dominant modes) are misspecified. Ground truth = Monte-Carlo test MSE of LOO-tuned ridge
(30 repetitions, 4000 test samples), i.e. NOT computed from the theory being evaluated.
"""
from __future__ import annotations

import json
import os
import time

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from src.models.theory import DEFAULT_MU_REL
from src.models.ridge import RidgeCV
from src.models.forecasters import RPMForecaster, pilot_subsample_curve, curve_forecast


def _make(p, r, noise_frac, seed):
    rng = np.random.default_rng(seed)
    lam = np.arange(1, p + 1, dtype=float) ** -1.6
    U = np.linalg.qr(rng.normal(size=(p, p)))[0]
    b = rng.normal(size=p) * np.sqrt(lam ** (r - 1))   # E[s_k] = lam_k * E[b_k^2] = lam_k^r
    signal = float(np.sum(lam * b ** 2))
    sigma2 = noise_frac / (1 - noise_frac) * signal
    A = U * np.sqrt(lam)
    beta = U @ b
    return lam, A, beta, sigma2


def _draw(A, beta, sigma2, n, rng):
    X = rng.normal(size=(n, A.shape[0])) @ A.T
    return X, X @ beta + np.sqrt(sigma2) * rng.normal(size=n)


def _scenario(p, r, noise_frac, n0_list, n_pilots, seed, reps=30):
    lam, A, beta, sigma2 = _make(p, r, noise_frac, seed)
    rng = np.random.default_rng(seed + 1)
    Xt, yt = _draw(A, beta, sigma2, 4000, rng)
    mus = DEFAULT_MU_REL * lam.max()
    horizons_all = sorted({m * n0 for n0 in n0_list for m in (4, 16)})
    truth = {}
    for n in horizons_all:
        errs = []
        for _ in range(reps):
            X, y = _draw(A, beta, sigma2, n, rng)
            errs.append(np.mean((RidgeCV(mus).fit(X, y).predict(Xt) - yt) ** 2))
        truth[n] = float(np.mean(errs))
    rows = []
    for n0 in n0_list:
        hz = [4 * n0, 16 * n0]
        for s in range(n_pilots):
            prng = np.random.default_rng(seed * 1000 + n0 * 10 + s)
            X0, y0 = _draw(A, beta, sigma2, n0, prng)
            res = {}
            f = RPMForecaster(n_boot=0).fit_forecast(X0, y0, None, lam, hz); res["RPM"] = f["point"]
            fw = RPMForecaster(n_boot=0, weighted=True).fit_forecast(X0, y0, None, lam, hz); res["RPM-w"] = fw["point"]
            # transferred alignment: r fixed at the median large-sample estimate from the real-data libraries (0.46);
            # in this simulation it is correct for r = 0.5 and misspecified for r = 1 and r = 2
            res["RPM-T"] = RPMForecaster(n_boot=0, r_mode="fixed", r_value=0.46).fit_forecast(X0, y0, None, lam, hz)["point"]
            res["RPM-wT"] = RPMForecaster(n_boot=0, weighted=True, r_mode="fixed", r_value=0.46).fit_forecast(X0, y0, None, lam, hz)["point"]
            ms, es = pilot_subsample_curve(X0, y0, None, mus, n_splits=10, seed=s)
            res["IPL3"] = curve_forecast("IPL3", ms, es, hz)["point"]
            res["FLAT"] = np.full(2, np.min(f["path"]))
            for m, v in res.items():
                for i, n in enumerate(hz):
                    rows.append({"p": p, "r": r, "noise_frac": noise_frac, "n0": n0, "pilot": s, "method": m, "n": n,
                                 "ratio": n / n0, "err": 0.5 * np.log(v[i] / truth[n])})
    return rows


def run_simulation(paths, mode="full", jobs=4):
    out = os.path.join(paths["results"], "simulation_raw.csv")
    if os.path.exists(out):
        return pd.read_csv(out)
    n0_list = (30, 60, 120) if mode == "full" else (40,)
    n_pilots = 30 if mode == "full" else 4
    scen = [(150, r, nf) for r in (0.5, 1.0, 2.0) for nf in (0.1, 0.3)] if mode == "full" else [(100, 1.0, 0.3)]
    t0 = time.time()
    res = Parallel(n_jobs=jobs, verbose=5)(delayed(_scenario)(p, r, nf, n0_list, n_pilots, seed=17 + i)
                                           for i, (p, r, nf) in enumerate(scen))
    df = pd.DataFrame([row for rr in res for row in rr])
    df.to_csv(out, index=False)
    print(f"simulation done in {time.time() - t0:.0f}s")
    return df
