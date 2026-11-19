"""Loaders for the public spectroscopic calibration data sets used in the study.

Every loader returns a `Task` with pre-processed spectra X (N x p), reference values y,
leakage-control group labels (soil profile/site, fruit, or sample), wavelength axis and
metadata. Replicate scans of one physical sample are averaged *before* any splitting.
Raw files are expected under `<raw_root>` (see scripts/download_data.py).
"""
from __future__ import annotations

import gzip
import warnings
import io
import os
import zipfile
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
import scipy.io as sio

from ..preprocessing.spectra import preprocess

warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
warnings.filterwarnings("ignore", message="you are shuffling")


@dataclass
class Task:
    name: str
    family: str
    X: np.ndarray
    y: np.ndarray
    groups: np.ndarray
    wavelengths: np.ndarray
    meta: dict = field(default_factory=dict)
    X_unlabeled_extra: np.ndarray | None = None
    X_unlabeled_groups: np.ndarray | None = None      # site/profile group of each unlabelled spectrum


OSSL_PROPS = {
    "OC": (["oc_usda.c729_w.pct", "oc_usda.c1059_w.pct"], "log1p", "% w/w"),
    "clay": (["clay.tot_usda.a334_w.pct"], "none", "% w/w"),
    "pH": (["ph.h2o_usda.a268_index"], "none", "pH units"),
    "CEC": (["cec_usda.a723_cmolc.kg"], "log1p", "cmol(+)/kg"),
}

OSSL_LIBS = {
    # name: (folder, spectral type, column prefix, (start, stop, step) in axis units, unit suffix, instrument)
    "ICRAF-VisNIR": ("ICRAF_ISRIC", "visnir", (400, 2480, 10), "ref", "ASD FieldSpec (VisNIR, 350-2500 nm)"),
    "ICRAF-MIR": ("ICRAF_ISRIC", "mir", (600, 4000, 16), "abs", "Bruker Tensor 27 HTS-XT (MIR)"),
    "KSSL-MIR": ("KSSL", "mir", (600, 4000, 16), "abs", "Bruker Vertex 70 HTS-XT (MIR)"),
    "KSSL-VisNIR": ("KSSL", "visnir", (400, 2480, 10), "ref", "ASD LabSpec (VisNIR)"),
    "AfSIS1-MIR": ("AFSIS1", "mir", (600, 4000, 16), "abs", "Bruker Tensor 27 HTS-XT (MIR)"),
    "Neospectra-NIR": ("Neospectra", "nir", (1350, 2550, 8), "ref", "Si-Ware NeoSpectra handheld MEMS FT-NIR"),
}


def _cache_path(cache_dir, key):
    os.makedirs(cache_dir, exist_ok=True)
    return os.path.join(cache_dir, key + ".npz")


def _read_ossl(raw_root, folder, stype, rng_axis, suffix, cache_dir):
    key = f"ossl_{folder}_{stype}"
    cp = _cache_path(cache_dir, key)
    if os.path.exists(cp):
        z = np.load(cp, allow_pickle=True)
        return z["ids"], z["X"], z["axis"], pd.DataFrame(z["meta"].tolist()) if "meta" in z else None
    path = os.path.join(raw_root, "ossl", folder, f"ossl_{stype}_v1.3.csv.gz")
    with gzip.open(path, "rt") as fh:
        header = fh.readline().strip().split(",")
    start, stop, step = rng_axis
    want = {f"scan_{stype}.{v}_{suffix}" for v in range(start, stop + 1, step)}
    scols = [c for c in header if c in want]
    extra = [c for c in ("scan.lab_src_txt",) if c in header]
    df = pd.read_csv(path, usecols=["id.layer_local_c"] + scols + extra, low_memory=False)
    if extra:
        # Neospectra: keep only spectra averaged over multiple scanners (one row per physical sample)
        df = df[df["scan.lab_src_txt"] == "Multiple"].drop(columns=extra)
    axis = np.array([float(c.split(".")[1].split("_")[0]) for c in scols])
    # average replicate scans of the same layer before anything else
    df = df.groupby("id.layer_local_c", sort=False)[scols].mean().reset_index()
    ids = df["id.layer_local_c"].astype(str).to_numpy()
    X = df[scols].to_numpy(np.float32)
    np.savez_compressed(cp, ids=ids, X=X, axis=axis)
    return ids, X, axis, None


def _icraf_profiles(site):
    """ICRAF-ISRIC has no site identifier and ~11% of layers lack coordinates. Profiles are reconstructed from
    runs of consecutive sample numbers within an ID prefix whose layer sequence increases (a new profile starts
    when the prefix changes, the layer sequence does not increase, or the sample number jumps by more than 3).
    Where coordinates exist this agrees with the coordinate groups for ~98.5% of profiles."""
    s = site[["id.layer_local_c", "layer.sequence_usda_uint16"]].copy()
    s["pref"] = s["id.layer_local_c"].str.split("_").str[0]
    s["num"] = pd.to_numeric(s["id.layer_local_c"].str.extract(r"(\d+)$")[0], errors="coerce")
    s = s.sort_values(["pref", "num"])
    seq = s["layer.sequence_usda_uint16"].to_numpy(); pref = s["pref"].to_numpy(); num = s["num"].to_numpy()
    prof, p = [], 0
    for i in range(len(s)):
        if i == 0 or pref[i] != pref[i - 1] or not (seq[i] > seq[i - 1]) or not (num[i] - num[i - 1] <= 3):
            p += 1
        prof.append(p)
    return pd.Series(["P_%d" % v for v in prof], index=s.index).reindex(site.index)


def _ossl_groups(raw_root, folder, site):
    """Group label (site / profile) per layer, used for group-disjoint splits and leave-one-group-out CV.
    KSSL: dataset site id. Neospectra: the KSSL site of the matching KSSL layer (Neospectra soils are KSSL
    archive samples). AfSIS1: sentinel site + sampling cluster. ICRAF-ISRIC: coordinates, else the profile
    reconstructed from sample-number runs. A layer receives its own group only if none of these exists."""
    lid = site["id.layer_local_c"].astype(str)
    coords = None
    lon, lat = site.get("longitude.point_wgs84_dd"), site.get("latitude.point_wgs84_dd")
    if lon is not None and lat is not None:
        coords = pd.Series(np.where(lon.notna() & lat.notna(), "C_" + lon.round(5).astype(str) + "_" + lat.round(5).astype(str), None), index=site.index)
    if "id.dataset.site_ascii_txt" in site.columns and site["id.dataset.site_ascii_txt"].notna().mean() > 0.5:
        g = "S_" + site["id.dataset.site_ascii_txt"].astype(str)
        g[site["id.dataset.site_ascii_txt"].isna()] = None
    elif folder == "Neospectra" and "id.kssl.lay_local_txt" in site.columns:
        ks = pd.read_csv(os.path.join(raw_root, "ossl", "KSSL", "ossl_soilsite_v1.3.csv.gz"), low_memory=False,
                         usecols=["id.layer_local_c", "id.dataset.site_ascii_txt"])
        kmap = dict(zip(ks["id.layer_local_c"].astype(str), ks["id.dataset.site_ascii_txt"].astype(str)))
        key = pd.to_numeric(site["id.kssl.lay_local_txt"], errors="coerce")
        g = pd.Series([("S_" + kmap[str(int(k))]) if (pd.notna(k) and str(int(k)) in kmap) else None for k in key], index=site.index)
    elif "site.name_src_txt" in site.columns and "site.cluster_src_id" in site.columns:
        ok = site["site.name_src_txt"].notna() & site["site.cluster_src_id"].notna()
        g = pd.Series(np.where(ok, "A_" + site["site.name_src_txt"].astype(str) + "_" + site["site.cluster_src_id"].astype(str), None), index=site.index)
    elif folder == "ICRAF_ISRIC":
        prof = _icraf_profiles(site)
        g = coords.where(coords.notna(), prof) if coords is not None else prof
    else:
        g = pd.Series([None] * len(site), index=site.index)
    if coords is not None:
        g = g.where(g.notna(), coords)
    return g.where(g.notna(), "L_" + lid)


def load_ossl(raw_root, lib, prop, cache_dir, max_n=15000, seed=0, prep="snv"):
    folder, stype, rng_axis, suffix, instrument = OSSL_LIBS[lib]
    ids, Xraw, axis, _ = _read_ossl(raw_root, folder, stype, rng_axis, suffix, cache_dir)
    lab = pd.read_csv(os.path.join(raw_root, "ossl", folder, "ossl_soillab_v1.3.csv.gz"), low_memory=False)
    site = pd.read_csv(os.path.join(raw_root, "ossl", folder, "ossl_soilsite_v1.3.csv.gz"), low_memory=False)
    cols, transform, unit = OSSL_PROPS[prop]
    col = next((c for c in cols if c in lab.columns and lab[c].notna().sum() > 500), None)
    if col is None:
        raise KeyError(f"{prop} not available in {lib}")
    lab = lab[["id.layer_local_c", col]].dropna()
    lab["id.layer_local_c"] = lab["id.layer_local_c"].astype(str)
    lab = lab.groupby("id.layer_local_c", as_index=False)[col].mean()
    # leakage-control group: the site / profile a layer belongs to (see _ossl_groups)
    site["id.layer_local_c"] = site["id.layer_local_c"].astype(str)
    site["grp"] = _ossl_groups(raw_root, folder, site)
    site = site.drop_duplicates("id.layer_local_c")[["id.layer_local_c", "grp"]]
    idx = pd.DataFrame({"id.layer_local_c": ids, "row": np.arange(len(ids))})
    m = idx.merge(lab, on="id.layer_local_c").merge(site, on="id.layer_local_c", how="left")
    m["grp"] = m["grp"].fillna("L_" + m["id.layer_local_c"])
    # unlabelled spectra of the same library (no reference value for this property)
    unl_rows = np.setdiff1d(np.arange(len(ids)), m["row"].to_numpy())
    rng = np.random.default_rng(seed)
    if len(m) > max_n:  # cap by whole groups to keep profiles intact
        ug = np.array(m["grp"].unique(), dtype=object); rng.shuffle(ug)
        keep, tot = [], 0
        sizes = m.groupby("grp").size()
        for g in ug:
            if tot >= max_n:
                break
            keep.append(g); tot += sizes[g]
        m = m[m["grp"].isin(set(keep))]
    X = Xraw[m["row"].to_numpy()].astype(float)
    y = m[col].to_numpy(float)
    if transform == "log1p":
        y = np.log1p(np.clip(y, 0, None))
    ok = np.all(np.isfinite(X), 1) & np.isfinite(y)
    X, y, grp = X[ok], y[ok], m["grp"].to_numpy()[ok]
    absorb = suffix == "ref"
    Xp = preprocess(X, prep, absorbance_from_reflectance=absorb)
    Xu = None; Gu = None
    if len(unl_rows) > 0:
        sel = unl_rows if len(unl_rows) <= 20000 else rng.choice(unl_rows, 20000, replace=False)
        Xu_raw = Xraw[sel].astype(float)
        fin = np.all(np.isfinite(Xu_raw), 1)
        Xu_raw = Xu_raw[fin]
        gmap = dict(zip(site["id.layer_local_c"], site["grp"]))
        Gu = np.array([gmap.get(i, "L_" + i) for i in ids[sel][fin]], dtype=object)
        Xu = preprocess(Xu_raw, prep, absorbance_from_reflectance=absorb) if len(Xu_raw) else None
    return Task(name=f"{lib}:{prop}", family="soil", X=Xp, y=y, groups=grp, wavelengths=axis,
                meta={"library": lib, "property": prop, "column": col, "transform": transform, "unit": unit,
                      "instrument": instrument, "spectral_type": stype, "prep": prep,
                      "source": "Open Soil Spectral Library v1.3", "license": "CC-BY 4.0 / ODbL (AfSIS1)",
                      "n_groups": int(len(np.unique(grp)))},
                X_unlabeled_extra=Xu, X_unlabeled_groups=Gu)


def load_mango(raw_root, prep="snv", group_level="fruit"):
    d = pd.read_csv(os.path.join(raw_root, "mango", "MangoDMC_NIR_Data_v3.csv"))
    wl = [c for c in d.columns if c.isdigit() and 684 <= int(c) <= 990]
    d = d[d["Temp"] == "No"].copy()
    d["fruit"] = d.groupby(["Season", "Pop", "Date", "Cultivar", "Type", d["DM"].round(8)]).ngroup()
    agg = d.groupby("fruit").agg({**{c: "mean" for c in wl}, "DM": "first", "Pop": "first", "Season": "first"})
    X = agg[wl].to_numpy(float); y = agg["DM"].to_numpy(float)
    grp = agg.index.to_numpy() if group_level == "fruit" else agg["Pop"].astype(str).to_numpy()
    Xp = preprocess(X, prep, absorbance_from_reflectance=False)
    return Task(name="Mango:DM", family="fruit", X=Xp, y=y, groups=grp, wavelengths=np.array([float(c) for c in wl]),
                meta={"library": "Mango", "property": "DM", "transform": "none", "unit": "% w/w",
                      "instrument": "Felix F750 handheld Vis-SWNIR", "spectral_type": "swnir", "prep": prep,
                      "source": "Anderson et al. 2020 / Mendeley Data doi:10.17632/46htwnp833", "license": "CC BY 4.0",
                      "season": agg["Season"].to_numpy(), "pop": agg["Pop"].astype(str).to_numpy(),
                      "n_groups": int(len(np.unique(grp)))})


def _ev_mat(path, key):
    o = sio.loadmat(path, squeeze_me=True, struct_as_record=False)[key]
    return np.asarray(o.data, float), o


def _parse_ev_csv(text):
    """Parse an Eigenvector DataSet CSV export: returns (axis or None, labels, numeric rows, header)."""
    import csv
    rows = list(csv.reader(io.StringIO(text)))
    axis, header, labels, vals = None, None, [], []
    for r in rows:
        if not r:
            continue
        if r[0] == "Axisscale":
            axis = np.array([float(v) for v in r[2:] if v.strip() != ""])
        elif r[0] == "Label" and len(r) > 3:
            header = [c.strip() for c in r]
        elif r[0] == "" and len(r) > 2 and r[1].strip() not in ("", "Label"):
            labels.append(r[1].strip())
            vals.append([float(v) if v.strip() not in ("", "NaN") else np.nan for v in r[2:]])
    width = max(len(v) for v in vals)
    M = np.full((len(vals), width), np.nan)
    for i, v in enumerate(vals):
        M[i, :len(v)] = v
    return axis, np.array(labels), M, header


def load_diesel(raw_root, prop, prep="snv"):
    base = os.path.join(raw_root, "eigenvector", "SWRI_Diesel_NIR_CSV.zip")
    with zipfile.ZipFile(base) as z:
        prop_txt = z.read("diesel_prop.csv").decode("latin-1")
        spec_txt = z.read("diesel_spec.csv").decode("latin-1")
    axis, s_lab, S, _ = _parse_ev_csv(spec_txt)
    _, p_lab, P, header = _parse_ev_csv(prop_txt)
    names = [h for h in header[2:] if h]
    j = names.index(prop.upper())
    lab = dict(zip(p_lab, P[:, j]))
    X = S[:, :len(axis)]
    y = np.array([lab.get(l, np.nan) for l in s_lab], float)
    ok = np.isfinite(y) & np.all(np.isfinite(X), 1)
    X, y = X[ok][:, ::2], y[ok]
    axis = axis[::2]
    Xp = preprocess(X, prep, absorbance_from_reflectance=False)
    return Task(name=f"Diesel:{prop}", family="fuel", X=Xp, y=y, groups=np.arange(len(y)), wavelengths=axis,
                meta={"library": "Diesel (SWRI)", "property": prop, "transform": "none", "unit": "-",
                      "instrument": "NIR 750-1550 nm (SWRI)", "spectral_type": "nir", "prep": prep,
                      "source": "Eigenvector Research data archive (SWRI diesel NIR)",
                      "license": "public research archive (no licence stated)", "n_groups": int(len(y))})


def load_tablets(raw_root, prep="snv"):
    path = os.path.join(raw_root, "eigenvector", "nir_shootout_2002.mat__x", "nir_shootout_2002.mat")
    if not os.path.exists(path):
        with zipfile.ZipFile(os.path.join(raw_root, "eigenvector", "nir_shootout_2002.mat_.zip")) as z:
            z.extractall(os.path.join(raw_root, "eigenvector", "nir_shootout_2002.mat__x"))
    Xs, ys = [], []
    for part in ("calibrate", "validate", "test"):
        X, o = _ev_mat(path, f"{part}_1"); Y, _ = _ev_mat(path, f"{part}_Y")
        Xs.append(X); ys.append(Y[:, 2])  # columns: weight, hardness, assay
        axis = np.asarray(o.axisscale[1, 0], float)
    X = np.vstack(Xs)[:, ::3]; y = np.concatenate(ys); axis = axis[::3]
    ok = np.isfinite(y) & np.all(np.isfinite(X), 1)
    Xp = preprocess(X[ok], prep, absorbance_from_reflectance=False)
    return Task(name="Tablets:assay", family="pharma", X=Xp, y=y[ok], groups=np.arange(ok.sum()), wavelengths=axis,
                meta={"library": "IDRC 2002 tablets", "property": "assay", "transform": "none", "unit": "mg",
                      "instrument": "NIR spectrometer 1 (IDRC 2002 shoot-out)", "spectral_type": "nir", "prep": prep,
                      "source": "IDRC 2002 shoot-out via Eigenvector archive", "license": "public research archive (no licence stated)",
                      "n_groups": int(ok.sum())})


def load_tecator(raw_root, prop, prep="snv"):
    path = os.path.join(raw_root, "tecator", "tecator.arff")
    rows, attrs, in_data = [], [], False
    for line in open(path, encoding="latin-1"):
        s = line.strip()
        if not s or s.startswith("%"):
            continue
        if s.lower().startswith("@attribute"):
            attrs.append(s.split()[1])
        elif s.lower().startswith("@data"):
            in_data = True
        elif in_data:
            rows.append([float(v) for v in s.split(",")])
    D = pd.DataFrame(rows, columns=attrs)
    acols = [c for c in attrs if c.lower().startswith("absorbance")]
    target = {"fat": "fat", "moisture": "moisture", "protein": "protein"}[prop]
    tcol = next(c for c in attrs if c.lower() == target)
    X = D[acols].to_numpy(float); y = D[tcol].to_numpy(float)
    # the data provider designates the last 25 samples (sets E1, E2) for extrapolation studies and asks users to
    # ignore them for interpolation work; they are excluded (samples 1-215 are used)
    X, y = X[:215], y[:215]
    Xp = preprocess(X, prep, absorbance_from_reflectance=False)
    return Task(name=f"Tecator:{prop}", family="meat", X=Xp, y=y, groups=np.arange(len(y)),
                wavelengths=np.linspace(850, 1050, X.shape[1]),
                meta={"library": "Tecator", "property": prop, "transform": "none", "unit": "% w/w",
                      "instrument": "Tecator Infratec Food & Feed Analyzer (850-1050 nm)", "spectral_type": "nir",
                      "prep": prep, "source": "StatLib / OpenML data id 505", "license": "public domain; redistribution with the Tecator permission note",
                      "n_groups": len(y), "excluded": "extrapolation sets E1/E2 (last 25 samples), as designated by the data provider"})


def load_cgl(raw_root, prop, prep="snv"):
    path = os.path.join(raw_root, "eigenvector", "CGL_nir.mat__x", "CGL_nir.mat")
    if not os.path.exists(path):
        with zipfile.ZipFile(os.path.join(raw_root, "eigenvector", "CGL_nir.mat_.zip")) as z:
            z.extractall(os.path.join(raw_root, "eigenvector", "CGL_nir.mat__x"))
    X, o = _ev_mat(path, "Spectra"); Y, _ = _ev_mat(path, "PropVals")
    j = {"casein": 0, "glucose": 1, "lactate": 2, "moisture": 3}[prop]
    axis = np.asarray(o.axisscale[1, 0], float)
    y = Y[:, j]; ok = np.isfinite(y)
    Xp = preprocess(X[ok], prep, absorbance_from_reflectance=False)
    return Task(name=f"CGL:{prop}", family="mixture", X=Xp, y=y[ok], groups=np.arange(ok.sum()), wavelengths=axis,
                meta={"library": "CGL (Naes & Isaksson design)", "property": prop, "transform": "none", "unit": "% w/w",
                      "instrument": "NIR 1104-2495 nm", "spectral_type": "nir", "prep": prep,
                      "source": "Eigenvector Research data archive", "license": "public research archive (no licence stated)",
                      "designed_experiment": True, "n_groups": int(ok.sum())})


TASKS_FULL = (
    [("ossl", lib, prop) for lib in ("ICRAF-VisNIR", "ICRAF-MIR", "KSSL-MIR", "KSSL-VisNIR", "Neospectra-NIR")
     for prop in ("OC", "clay", "pH", "CEC")]
    + [("ossl", "AfSIS1-MIR", p) for p in ("OC", "clay", "pH")]
    + [("mango", None, "DM")]
    + [("diesel", None, p) for p in ("bp50", "cn", "d4052", "freeze", "total", "visc")]
    + [("tablets", None, "assay")]
    + [("tecator", None, p) for p in ("fat", "moisture", "protein")]
    + [("cgl", None, p) for p in ("casein", "glucose", "lactate", "moisture")]
)

TASKS_QUICK = [("ossl", "ICRAF-VisNIR", "OC"), ("mango", None, "DM"), ("tecator", None, "fat")]


def load_task(spec, raw_root, cache_dir, prep="snv", seed=0, max_n=15000, group_level="fruit"):
    kind, lib, prop = spec
    if kind == "ossl":
        return load_ossl(raw_root, lib, prop, cache_dir, max_n=max_n, seed=seed, prep=prep)
    if kind == "mango":
        return load_mango(raw_root, prep=prep, group_level=group_level)
    if kind == "diesel":
        return load_diesel(raw_root, prop, prep=prep)
    if kind == "tablets":
        return load_tablets(raw_root, prep=prep)
    if kind == "tecator":
        return load_tecator(raw_root, prop, prep=prep)
    if kind == "cgl":
        return load_cgl(raw_root, prop, prep=prep)
    raise ValueError(kind)
