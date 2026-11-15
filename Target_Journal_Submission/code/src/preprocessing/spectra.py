"""Sample-wise spectral pre-processing (no information is shared across samples, so it
cannot leak between calibration and test sets)."""
from __future__ import annotations

import numpy as np
from scipy.signal import savgol_filter


def snv(X):
    X = np.asarray(X, float)
    mu = X.mean(1, keepdims=True); sd = X.std(1, keepdims=True)
    return (X - mu) / np.where(sd > 0, sd, 1.0)


def preprocess(X, method="snv", absorbance_from_reflectance=False):
    X = np.asarray(X, float)
    if absorbance_from_reflectance:
        X = np.log10(1.0 / np.clip(X, 1e-4, None))
    if method in (None, "none", "raw"):
        return X
    if method == "snv":
        return snv(X)
    if method == "sg1":
        w = 11 if X.shape[1] >= 21 else (X.shape[1] // 2) * 2 - 1
        return savgol_filter(X, window_length=w, polyorder=2, deriv=1, axis=1)
    if method == "snv_sg1":
        w = 11 if X.shape[1] >= 21 else (X.shape[1] // 2) * 2 - 1
        return savgol_filter(snv(X), window_length=w, polyorder=2, deriv=1, axis=1)
    raise ValueError(method)
