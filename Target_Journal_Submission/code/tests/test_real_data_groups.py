"""Real-data checks of the leakage-control groups (skipped when the raw data are not present)."""
import os

import numpy as np
import pytest

from src.data.datasets import load_task
from src.training.learning_curves import split_task

RAW = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data_raw"))
CACHE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "cache"))
pytestmark = pytest.mark.skipif(not os.path.isdir(os.path.join(RAW, "ossl")), reason="raw OSSL data not available")


@pytest.mark.parametrize("lib,min_prefix,prefixes", [("ICRAF-VisNIR", 0.99, ("C_", "P_")),
                                                      ("Neospectra-NIR", 0.98, ("S_",)),
                                                      ("AfSIS1-MIR", 0.95, ("A_",))])
def test_groups_reconstructed(lib, min_prefix, prefixes):
    t = load_task(("ossl", lib, "OC"), RAW, CACHE)
    g = np.asarray(t.groups).astype(str)
    assert np.mean([x.startswith(prefixes) for x in g]) >= min_prefix     # few per-layer fallback groups
    pool, test = split_task(t.groups, 1)
    assert not set(g[pool]) & set(g[test])                                  # group-disjoint split


def test_unlabelled_groups_available():
    t = load_task(("ossl", "KSSL-MIR", "OC"), RAW, CACHE)
    assert t.X_unlabeled_extra is not None and t.X_unlabeled_groups is not None
    assert len(t.X_unlabeled_groups) == len(t.X_unlabeled_extra)
