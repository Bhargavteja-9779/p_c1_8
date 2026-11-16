"""Aggregate raw results into metrics, statistics, tables, figures and numbers.json.

Every number quoted in the manuscript is read from results/numbers.json or from tables/*.csv,
both written here from the raw per-pilot results.
"""
from __future__ import annotations

import glob
import json
import os

import numpy as np
import pandas as pd

from src.statistics.tests import paired_comparison, bootstrap_ci_mean
from src.data.datasets import TASKS_FULL
from src.models.theory import DEFAULT_MU_REL, solve_kappa, df2_of, risk, power_signal

MAIN_METHODS = ["RPM", "RPM-w", "RPM-T", "RPM-wT", "IPL3", "IPL2", "EXP3", "LOG2", "FLAT", "DFOLS", "SLOPE-T"]
ABL_METHODS = ["RPM", "RPM-rfree", "RPM-ML2", "RPM-pilotcov", "RPM-pilotcov+tail", "RPM-U250", "RPM-Uextra",
               "RPM-kfold10", "RPM-cut0.5", "RPM-cut0.95"]
LABELS = {"RPM": "RPM (pre-registered, r = 1)", "RPM-w": "RPM-w (weighted path fit)", "RPM-T": "RPM-T (transferred alignment)", "RPM-wT": "RPM-wT (weighted + transferred)", "SLOPE-T": "Transferred slope (SLOPE-T)", "IPL3": "Inverse power law (IPL3)", "IPL2": "Power law (IPL2)",
          "EXP3": "Exponential (EXP3)", "LOG2": "Logarithmic (LOG2)", "FLAT": "No improvement (FLAT)",
          "DFOLS": "Fixed-complexity formula (DF-OLS)"}


# ------------------------------------------------------------------------------------------
def load_main(raw_dir, tag="main"):
    files = sorted(glob.glob(os.path.join(raw_dir, f"forecasts_{tag}_*.csv")))
    files += sorted(glob.glob(os.path.join(raw_dir, "forecasts_refine_*.csv")))   # RPM-w (Phase-19 refinement)
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True) if files else pd.DataFrame()
    timing = df[df.method == "_timing"].copy() if len(df) else df
    df = df[df.method != "_timing"].copy() if len(df) else df
    if len(df):
        df["err"] = df["fc_logrmse"] - df["truth_ridge_logrmse"]
        df["abs_err"] = df["err"].abs()
        df["err_pls"] = df["fc_logrmse"] - df["truth_pls_logrmse"]
        df["abs_err_pls"] = df["err_pls"].abs()
    return df, timing


def per_task(df, col="abs_err", methods=MAIN_METHODS, by=None):
    keys = ["task"] + ([by] if by else [])
    t = df[df.method.isin(methods)].groupby(keys + ["method"])[col].mean().unstack("method")
    return t[[m for m in methods if m in t.columns]]


def source_of(task_name):
    lib = task_name.split(":")[0]
    for pre in ("ICRAF", "KSSL", "AfSIS1", "Neospectra", "Mango", "Diesel", "Tablets", "Tecator", "CGL"):
        if lib.startswith(pre):
            return pre
    return lib


def add_slope_transfer(df, raw_dir):
    """Simple competitor (added after the pre-registration, as a hostile-reviewer check): extrapolate the
    pilot CV error with the median log-RMSE slope per doubling of n observed in the ground-truth curves of
    OTHER data sources (leave-one-source-out)."""
    slopes = {}
    for f in glob.glob(os.path.join(raw_dir, "truth_*.npz")):
        z = np.load(f, allow_pickle=True); name = os.path.basename(f)[6:-4].replace("__", ":")
        x = np.log2(z["n"].astype(float)); yv = 0.5 * np.log(z["ridge_mse"])
        slopes[name] = float(np.polyfit(x, yv, 1)[0]) if len(x) >= 2 else np.nan
    st = pd.Series(slopes)
    src = {t: source_of(t) for t in st.index}
    loso = {t: float(st[[u for u in st.index if src[u] != src[t]]].median()) for t in st.index}
    base = df[df.method == "RPM"].copy()
    base["method"] = "SLOPE-T"
    base["fc_logrmse"] = base.pilot_cv_logrmse + base.task.map(loso) * np.log2(base.n / base.n0)
    for c in ("lo80", "hi80", "lo95", "hi95", "log_sigma2", "log_tau2", "r"):
        if c in base:
            base[c] = np.nan
    base["err"] = base.fc_logrmse - base.truth_ridge_logrmse; base["abs_err"] = base.err.abs()
    base["err_pls"] = base.fc_logrmse - base.truth_pls_logrmse; base["abs_err_pls"] = base.err_pls.abs()
    return pd.concat([df, base], ignore_index=True), pd.DataFrame({"task": st.index, "slope_per_doubling": st.values,
                                                                     "slope_loso_prior": [loso[t] for t in st.index]})


def summary_table(df, methods=MAIN_METHODS, err="err"):
    rows = []
    d = df[df.method.isin(methods)]
    pt = d.groupby(["task", "method"]).agg(mae=(err, lambda x: np.mean(np.abs(x))), bias=(err, "mean"),
                                           medae=(err, lambda x: np.median(np.abs(x))),
                                           w10=(err, lambda x: np.mean(np.abs(x) <= np.log(1.1))),
                                           w20=(err, lambda x: np.mean(np.abs(x) <= np.log(1.2)))).reset_index()
    for m in methods:
        s = pt[pt.method == m]
        if not len(s):
            continue
        lo, hi = bootstrap_ci_mean(s.mae.values, seed=1)
        rows.append({"method": m, "label": LABELS.get(m, m), "n_tasks": len(s), "mean_abs_logerr": s.mae.mean(),
                     "ci95_lo": lo, "ci95_hi": hi, "median_task_abs_logerr": s.mae.median(),
                     "median_abs_logerr_rows": float(np.median(np.abs(d[d.method == m][err]))),
                     "mean_bias": s.bias.mean(), "pct_within_10": 100 * d[d.method == m][err].abs().le(np.log(1.1)).mean(),
                     "pct_within_20": 100 * d[d.method == m][err].abs().le(np.log(1.2)).mean()})
    return pd.DataFrame(rows)


def stats_vs_rpm(df, methods=MAIN_METHODS, col="abs_err", ref="RPM"):
    pt = per_task(df, col, methods)
    others = {m: pt[m].values for m in methods if m != ref and m in pt}
    return pd.DataFrame(paired_comparison(pt[ref].values, others, seed=3))


def coverage_table(df, methods=("RPM", "RPM-w", "RPM-T", "RPM-wT", "IPL3", "IPL2", "EXP3", "LOG2")):
    rows = []
    for m in methods:
        d = df[(df.method == m) & df["lo80"].notna()]
        if not len(d):
            continue
        for lev in (80, 95):
            cov = ((d[f"lo{lev}"] <= d.truth_ridge_logrmse) & (d.truth_ridge_logrmse <= d[f"hi{lev}"])).astype(float)
            per_t = cov.groupby(d.task).mean()
            width = (d[f"hi{lev}"] - d[f"lo{lev}"]).groupby(d.task).mean()
            w_rows = (d[f"hi{lev}"] - d[f"lo{lev}"])
            rows.append({"method": m, "nominal": lev, "coverage_rows": 100 * cov.mean(), "coverage_task_mean": 100 * per_t.mean(),
                         "coverage_task_median": 100 * per_t.median(), "mean_width_log": width.mean(),
                         "mean_width_factor": float(np.exp(width.mean())),
                         "median_width_factor": float(np.exp(w_rows.median())),
                         "pct_width_factor_gt10": float(100 * (w_rows > np.log(10)).mean())})
    return pd.DataFrame(rows)


def decision_table(df, methods=MAIN_METHODS):
    """Forecast of the calibration size needed to reach the RMSE that is actually achieved at n* (4 n0, 16 n0)."""
    rows = []
    d = df[df.method.isin(methods)]
    for (task, n0, pilot, m), g in d.groupby(["task", "n0", "pilot", "method"]):
        g = g.sort_values("n")
        ns = np.concatenate([[n0], g.n.values]).astype(float)
        fc = np.concatenate([[g.pilot_cv_logrmse.iloc[0]], g.fc_logrmse.values])
        truth = dict(zip(g.n.values, g.truth_ridge_logrmse.values))
        for mult in (4, 16):
            nstar = n0 * mult
            if nstar not in truth:
                continue
            T = truth[nstar]
            below = np.flatnonzero(fc <= T)
            if len(below) == 0:
                nhat = np.inf
            else:
                j = below[0]
                if j == 0:
                    nhat = ns[0]
                else:  # log-log interpolation between grid points
                    x0, x1 = np.log(ns[j - 1]), np.log(ns[j]); y0, y1 = fc[j - 1], fc[j]
                    nhat = float(np.exp(x0 + (T - y0) * (x1 - x0) / (y1 - y0))) if y1 != y0 else ns[j]
            err = np.abs(np.log2(nhat / nstar)) if np.isfinite(nhat) else np.inf
            rows.append({"task": task, "n0": n0, "pilot": pilot, "method": m, "mult": mult, "nhat": nhat,
                         "abs_log2_err": err, "success_factor2": float(err <= 1.0), "failure": float(not np.isfinite(nhat))})
    r = pd.DataFrame(rows)
    out = []
    for (m, mult), g in r.groupby(["method", "mult"]):
        pt = g.groupby("task").success_factor2.mean()
        fin = g[np.isfinite(g.abs_log2_err)]
        out.append({"method": m, "target": f"{mult}n0", "pct_within_factor2": 100 * g.success_factor2.mean(),
                    "pct_within_factor2_task_mean": 100 * pt.mean(), "pct_never_reaches_target": 100 * g.failure.mean(),
                    "median_abs_log2_err_finite": float(fin.abs_log2_err.median()) if len(fin) else np.nan})
    return pd.DataFrame(out), r


def posthoc_gain(df, raw_dir, methods):
    """POST-HOC (not pre-registered): forecast of the *gain* RMSE(n)/RMSE(n0) and a planning decision.

    gain error = |log(fc(n)/pilot_cv) - log(truth(n)/truth(n0))|; truth(n0) from the ground-truth curve
    (available for n0 in the truth grid, i.e. 50, 100, 200). Decision: 'an 8x larger calibration set
    reduces RMSEP by >= 10 %'; balanced accuracy of each method's prediction (FLAT always predicts no).
    """
    tr = {}
    for f in glob.glob(os.path.join(raw_dir, "truth_*.npz")):
        z = np.load(f, allow_pickle=True); name = os.path.basename(f)[6:-4].replace("__", ":")
        tr[name] = dict(zip(z["n"].tolist(), (0.5 * np.log(z["ridge_mse"])).tolist()))
    d = df[df.method.isin(methods)].copy()
    d["t_n0"] = [tr.get(t, {}).get(int(n0), np.nan) for t, n0 in zip(d.task, d.n0)]
    d = d[d.t_n0.notna()]
    d["gain_fc"] = d.fc_logrmse - d.pilot_cv_logrmse
    d["gain_true"] = d.truth_ridge_logrmse - d.t_n0
    d["gain_abs_err"] = (d.gain_fc - d.gain_true).abs()
    pt = d.groupby(["task", "method"]).gain_abs_err.mean().unstack()
    rows = []
    thr = np.log(0.9)
    for m in methods:
        if m not in pt:
            continue
        g = d[(d.method == m) & (d.ratio == 8)]
        yt = g.gain_true <= thr; yp = g.gain_fc <= thr
        sens = float((yp & yt).sum() / max(yt.sum(), 1)); spec = float((~yp & ~yt).sum() / max((~yt).sum(), 1))
        rows.append({"method": m, "n_tasks": int(pt[m].notna().sum()), "mean_task_gain_abs_err": pt[m].mean(),
                     "median_task_gain_abs_err": pt[m].median(), "mean_gain_bias": float((d[d.method == m].gain_fc - d[d.method == m].gain_true).mean()),
                     "decision_8x_10pct_balanced_acc": 0.5 * (sens + spec), "decision_sensitivity": sens, "decision_specificity": spec,
                     "prevalence_worthwhile": float(yt.mean()) if len(g) else np.nan})
    return pd.DataFrame(rows), pt


def theory_validity(raw_dir):
    """RQ1: theory curve fitted to the full-pool CV path vs empirical ridge / PLS truth at each n."""
    rows, collapse = [], {}
    for f in sorted(glob.glob(os.path.join(raw_dir, "truth_*.npz"))):
        z = np.load(f, allow_pickle=True)
        name = os.path.basename(f)[6:-4].replace("__", ":")
        lam = z["lam"]; ns = z["n"]; fits = json.loads(str(z["full_fits"]))
        pool_n = len(z["pool"])
        for mode, p in fits.items():
            s = power_signal(lam, p["log_tau2"], p["r"]); sig2 = np.exp(p["log_sigma2"])
            for i, n in enumerate(ns):
                th = float(np.min(risk(lam, s, sig2, n, DEFAULT_MU_REL * lam.max())))
                rows.append({"task": name, "mode": mode, "n": int(n), "pool_n": pool_n,
                             "theory_logrmse": 0.5 * np.log(th), "ridge_logrmse": 0.5 * np.log(z["ridge_mse"][i]),
                             "pls_logrmse": 0.5 * np.log(z["pls_mse"][i]) if len(z["pls_mse"]) else np.nan,
                             "r": p["r"], "noise_frac": sig2 / z["var_test"]})
        # kappa-collapse data: empirical test MSE at fixed mu, rescaled by the theory prefactor
        mus = z["mus"]; emp = z["ridge_mu_mse"]
        pts = []
        for i, n in enumerate(ns):
            k = solve_kappa(lam, n, mus); d2 = df2_of(lam, k)
            ok = d2 / n < 0.8
            pts.append((int(n), k[ok], (emp[i][ok] * (1 - d2[ok] / n) / (1 + 1 / n))))
        collapse[name] = pts
    return pd.DataFrame(rows), collapse


def collapse_dispersion(collapse, raw_dir):
    """Quantify the kappa-collapse: on a common grid inside the overlap of the kappa ranges observed at
    different n, the across-n standard deviation of log N_hat(kappa) (rescaled empirical test MSE).
    Reference ('no collapse'): the same statistic for the un-rescaled test MSE against the raw penalty mu."""
    rows = []
    for f in glob.glob(os.path.join(raw_dir, "truth_*.npz")):
        z = np.load(f, allow_pickle=True); name = os.path.basename(f)[6:-4].replace("__", ":")
        pts = collapse.get(name, [])
        if len(pts) < 3:
            continue
        lo = max(np.log(k.min()) for _, k, _ in pts if len(k)); hi = min(np.log(k.max()) for _, k, _ in pts if len(k))
        if not np.isfinite(lo) or hi <= lo:
            continue
        grid = np.linspace(lo, hi, 25)
        curves = []
        for n, k, nn in pts:
            o = np.argsort(k)
            curves.append(np.interp(grid, np.log(k[o]), np.log(nn[o])))
        disp = float(np.mean(np.std(np.array(curves), axis=0)))
        # reference: raw test MSE vs log(mu) (no kappa mapping, no prefactor) over the same number of n
        mus = np.log(z["mus"]); emp = np.log(z["ridge_mu_mse"])
        ref = float(np.mean(np.std(emp[:len(pts)], axis=0)))
        rows.append({"task": name, "n_curves": len(pts), "collapse_sd_log": disp, "no_collapse_ref_sd_log": ref})
    return pd.DataFrame(rows)


def eigen_decay(lam, kmax=60):
    k = np.arange(1, min(kmax, len(lam)) + 1)
    return float(-np.polyfit(np.log(k), np.log(lam[:len(k)]), 1)[0])


# ------------------------------------------------------------------------------------------
def write_table(df, paths, name, float_fmt="{:.3f}", caption=""):
    os.makedirs(paths["tables"], exist_ok=True)
    df.to_csv(os.path.join(paths["tables"], name + ".csv"), index=False)
    def fmt(v):
        if isinstance(v, (float, np.floating)):
            if not np.isfinite(v):
                return "–" if np.isnan(v) else ("∞" if v > 0 else "-∞")
            return float_fmt.format(v) if abs(v) >= 1e-3 or v == 0 else f"{v:.2e}"
        return str(v)
    cols = list(df.columns)
    md = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    md += ["| " + " | ".join(fmt(v) for v in r) + " |" for r in df.itertuples(index=False)]
    open(os.path.join(paths["tables"], name + ".md"), "w").write((f"**{caption}**\n\n" if caption else "") + "\n".join(md) + "\n")
    tex = ["\\begin{tabular}{" + "l" * len(cols) + "}", "\\hline", " & ".join(c.replace("_", "\\_") for c in cols) + " \\\\", "\\hline"]
    tex += [" & ".join(fmt(v).replace("_", "\\_").replace("%", "\\%") for v in r) + " \\\\" for r in df.itertuples(index=False)]
    tex += ["\\hline", "\\end{tabular}"]
    open(os.path.join(paths["tables"], name + ".tex"), "w").write("\n".join(tex) + "\n")


def run_analysis(cfg, paths, mode, log):
    from experiments import figures as F
    raw = paths["raw_out"]
    df, timing = load_main(raw)
    if not len(df):
        print("no results yet"); return
    df, slope_tab = add_slope_transfer(df, raw)
    slope_tab.to_csv(os.path.join(paths["results"], "slope_per_doubling.csv"), index=False)
    numbers = {"mode": mode}
    tasks = sorted(df.task.unique()); numbers["n_tasks"] = len(tasks)
    numbers["n_forecast_rows"] = int(len(df[df.method.isin(MAIN_METHODS)]))
    numbers["n_pilots_total"] = int(df[df.method == "RPM"].groupby(["task", "n0", "pilot"]).ngroups)
    # ---------------- datasets table (T1)
    meta_rows = []
    for f in sorted(glob.glob(os.path.join(raw, "truth_*.npz"))):
        z = np.load(f, allow_pickle=True); name = os.path.basename(f)[6:-4].replace("__", ":")
        meta_rows.append({"task": name, "n_pool": len(z["pool"]), "n_test": len(z["test"]), "p": int(len(z["lam"])) ,
                          "max_n_truth": int(z["n"].max()), "eigen_decay_exponent": eigen_decay(z["lam"]),
                          "truth_seconds": float(z["seconds"])})
    T1 = pd.DataFrame(meta_rows)
    fam = df.groupby("task").family.first(); T1["family"] = T1.task.map(fam)
    write_table(T1, paths, "T1_tasks", caption="Calibration tasks, split sizes and spectral properties")
    numbers["n_tasks_by_family"] = T1.family.value_counts().to_dict()
    # ---------------- main results (T2, T3)
    T2 = summary_table(df); write_table(T2, paths, "T2_main_accuracy_ridge_truth", caption="Forecast accuracy vs ridge truth")
    T3 = stats_vs_rpm(df); write_table(T3, paths, "T3_stats_rpm_vs_baselines", float_fmt="{:.4f}", caption="Paired Wilcoxon tests (task level)")
    by_n0 = []
    for n0, g in df.groupby("n0"):
        s = summary_table(g); s.insert(0, "n0", n0); by_n0.append(s)
        st = stats_vs_rpm(g); st.insert(0, "n0", n0); write_table(st, paths, f"T3_stats_n0_{n0}", float_fmt="{:.4f}")
    T2b = pd.concat(by_n0); write_table(T2b, paths, "T2b_accuracy_by_n0", caption="Accuracy by pilot size")
    # sensitivity S0: excluding ICRAF-VisNIR (used in exploratory feasibility work)
    d0 = df[~df.task.str.startswith("ICRAF-VisNIR")]
    S0 = summary_table(d0); write_table(S0, paths, "S0_accuracy_excluding_ICRAF_VisNIR")
    S0s = stats_vs_rpm(d0); write_table(S0s, paths, "S0_stats_excluding_ICRAF_VisNIR", float_fmt="{:.4f}")
    # by family
    fam_rows = []
    for fm, g in df.groupby("family"):
        s = summary_table(g, methods=["RPM", "IPL3", "FLAT", "DFOLS"]); s.insert(0, "family", fm); fam_rows.append(s)
    write_table(pd.concat(fam_rows), paths, "T11_accuracy_by_family")
    # by extrapolation ratio
    df["ratio_bin"] = np.round(np.log2(df.ratio)).astype(int)
    rr = df[df.method.isin(["RPM", "IPL3", "FLAT", "DFOLS"])].groupby(["method", "ratio_bin"]).abs_err.agg(["mean", "median", "count"]).reset_index()
    rr["ratio"] = 2.0 ** rr.ratio_bin; write_table(rr, paths, "T12_error_by_extrapolation_ratio")
    # ---------------- PLS truth (T4)
    dpls = df[df.truth_pls_logrmse.notna()].copy()
    T4 = summary_table(dpls, err="err_pls"); write_table(T4, paths, "T4_main_accuracy_pls_truth")
    T4s = stats_vs_rpm(dpls, col="abs_err_pls"); write_table(T4s, paths, "T4b_stats_pls_truth", float_fmt="{:.4f}")
    # ---------------- coverage (T5) and decisions (T6)
    T5 = coverage_table(df); write_table(T5, paths, "T5_interval_coverage")
    T6, dec_rows = decision_table(df); write_table(T6, paths, "T6_sample_size_decisions")
    # ---------------- ablation (T7)
    dab = df[df.method.isin(ABL_METHODS)]
    keys = dab[dab.method == "RPM-rfree"][["task", "n0", "pilot"]].drop_duplicates()
    dab = dab.merge(keys, on=["task", "n0", "pilot"])
    pta = per_task(dab, "abs_err", ABL_METHODS)
    abl = []
    for m in ABL_METHODS:
        if m not in pta:
            continue
        if m == "RPM":
            r0 = pta["RPM"].dropna()
            abl.append({"variant": m, "n_tasks": int(len(r0)), "mean_abs_logerr": float(r0.mean()), "rpm_same_tasks": float(r0.mean()),
                        "mean_diff_vs_rpm": 0.0, "ci95_lo": 0.0, "ci95_hi": 0.0})
            continue
        both = pd.DataFrame({"RPM": pta["RPM"], "V": pta[m]}).dropna()
        lo, hi = bootstrap_ci_mean(both["V"].values - both["RPM"].values, seed=5)
        abl.append({"variant": m, "n_tasks": int(len(both)), "mean_abs_logerr": float(both["V"].mean()), "rpm_same_tasks": float(both["RPM"].mean()),
                    "mean_diff_vs_rpm": float((both["V"] - both["RPM"]).mean()), "ci95_lo": lo, "ci95_hi": hi})
    T7 = pd.DataFrame(abl)
    st = paired_comparison(pta["RPM"].values, {m: pta[m].values for m in ABL_METHODS if m != "RPM" and m in pta}, seed=7)
    T7 = T7.merge(pd.DataFrame(st)[["comparison", "p_raw", "p_holm", "rank_biserial"]].rename(columns={"comparison": "variant"}), on="variant", how="left")
    write_table(T7, paths, "T7_ablation", float_fmt="{:.4f}")
    # ---------------- POST-HOC gain analysis (T14)
    gm = [m for m in ["RPM", "RPM-w", "RPM-T", "RPM-wT", "IPL3", "IPL2", "EXP3", "LOG2", "FLAT", "DFOLS", "SLOPE-T"] if m in set(df.method)]
    T14, gpt = posthoc_gain(df, raw, gm)
    write_table(T14, paths, "T14_posthoc_gain_and_decision", float_fmt="{:.3f}")
    ref_g = "RPM"
    T14s = pd.DataFrame(paired_comparison(gpt[ref_g].values, {m: gpt[m].values for m in gm if m != ref_g and m in gpt}, seed=11))
    T14s.insert(0, "reference", ref_g)
    write_table(T14s, paths, "T14b_posthoc_gain_stats", float_fmt="{:.4f}")
    numbers["posthoc_gain"] = T14.to_dict(orient="records"); numbers["posthoc_gain_stats"] = T14s.to_dict(orient="records")
    # ---------------- POST-HOC bracket analysis (T15)
    def bracket(lo_m, hi_m, label):
        k = ["task", "n0", "pilot", "n"]
        A_ = df[df.method == lo_m][k + ["fc_logrmse", "truth_ridge_logrmse"]].rename(columns={"fc_logrmse": "a"})
        B_ = df[df.method == hi_m][k + ["fc_logrmse"]].rename(columns={"fc_logrmse": "b"})
        m = A_.merge(B_, on=k)
        if not len(m):
            return None
        lo = np.minimum(m.a, m.b); hi = np.maximum(m.a, m.b)
        cov = ((lo <= m.truth_ridge_logrmse) & (m.truth_ridge_logrmse <= hi)).astype(float)
        out = {"bracket": label, "n_forecasts": int(len(m)), "coverage_pct": 100 * cov.mean(),
               "coverage_task_mean_pct": 100 * cov.groupby(m.task).mean().mean(),
               "median_width_log": float(np.median(hi - lo)), "median_width_factor": float(np.exp(np.median(hi - lo)))}
        for n0, g in m.assign(cov=cov, w=hi - lo).groupby("n0"):
            out[f"coverage_n0_{n0}"] = 100 * g["cov"].mean(); out[f"median_width_factor_n0_{n0}"] = float(np.exp(g["w"].median()))
        return out
    br = [b for b in (bracket("RPM-T", "RPM", "[RPM-T, RPM]"), bracket("IPL3", "FLAT", "[IPL3, FLAT]"), bracket("RPM", "FLAT", "[RPM, FLAT]")) if b]
    if br:
        T15 = pd.DataFrame(br); write_table(T15, paths, "T15_posthoc_bracket", float_fmt="{:.3f}")
        numbers["posthoc_bracket"] = T15.to_dict(orient="records")
    # ---------------- POST-HOC: SLOPE-T as reference (T3c), LOSO-conformal bands (T16), slope explanation (T17)
    ptS = per_task(df, "abs_err", MAIN_METHODS)
    T3c = pd.DataFrame(paired_comparison(ptS["SLOPE-T"].values, {m: ptS[m].values for m in MAIN_METHODS if m != "SLOPE-T"}, seed=13))
    T3c.insert(0, "reference", "SLOPE-T")
    write_table(T3c, paths, "T3c_posthoc_stats_slopeT_reference", float_fmt="{:.4f}")
    numbers["stats_slopeT_reference"] = rec(T3c, "comparison") if False else T3c.to_dict(orient="records")
    # leave-one-source-out conformal bands: band = forecast - quantiles of the log errors of the same method,
    # same extrapolation-ratio bin, observed on tasks of OTHER data sources
    df["src"] = df.task.map(source_of); df["rbin"] = np.round(np.log2(df.ratio)).astype(int)
    conf_rows = []
    for m in ["RPM", "RPM-w", "SLOPE-T", "FLAT", "IPL3"]:
        dm = df[df.method == m]
        cov = {80: [], 95: []}; wid = {80: [], 95: []}
        for s, g in dm.groupby("src"):
            other = dm[dm.src != s]
            for rb, gg in g.groupby("rbin"):
                e = other[other.rbin == rb].err.values
                if len(e) < 20:
                    e = other.err.values
                for lev in (80, 95):
                    lo_q, hi_q = np.quantile(e, [(1 - lev / 100) / 2, 1 - (1 - lev / 100) / 2])
                    lo = gg.fc_logrmse - hi_q; hi = gg.fc_logrmse - lo_q
                    cov[lev] += list(((lo <= gg.truth_ridge_logrmse) & (gg.truth_ridge_logrmse <= hi)).astype(float))
                    wid[lev] += list(hi - lo)
        for lev in (80, 95):
            conf_rows.append({"method": m, "nominal": lev, "coverage_pct": 100 * float(np.mean(cov[lev])),
                              "median_width_factor": float(np.exp(np.median(wid[lev])))})
    T16 = pd.DataFrame(conf_rows)
    write_table(T16, paths, "T16_posthoc_loso_conformal_bands", float_fmt="{:.3f}")
    numbers["posthoc_conformal"] = T16.to_dict(orient="records")
    df.drop(columns=["src", "rbin"], inplace=True)
    al_p = os.path.join(paths["results"], "alignment_exponents.csv")
    if os.path.exists(al_p):
        import statsmodels.api as sm
        from scipy.stats import spearmanr
        alg = pd.read_csv(al_p)
        mm = slope_tab.merge(alg, on="task").merge(T1[["task", "eigen_decay_exponent", "family"]], on="task")
        rows17 = []
        for c in ["noise_frac_full_pool", "r_full_pool", "eigen_decay_exponent", "n_pool"]:
            rho, p = spearmanr(mm[c], mm.slope_per_doubling)
            rows17.append({"descriptor": c, "spearman_rho": rho, "p": p})
        X = sm.add_constant(np.column_stack([mm.r_full_pool, np.log(mm.noise_frac_full_pool), mm.eigen_decay_exponent]))
        fit = sm.OLS(mm.slope_per_doubling.values, X).fit()
        rows17.append({"descriptor": "OLS: slope ~ r + log(noise fraction) + eigen-decay", "spearman_rho": np.nan, "p": float(fit.f_pvalue), "r2": float(fit.rsquared)})
        T17 = pd.DataFrame(rows17)
        write_table(T17, paths, "T17_posthoc_slope_explanation", float_fmt="{:.4f}")
        def region(t):
            lib = t.split(":")[0]
            return "MIR (soil)" if "MIR" in lib else ("Vis/NIR (soil)" if ("VisNIR" in lib or "Neospectra" in lib) else lib)
        mm["region"] = mm.task.map(region)
        T17b = mm.groupby("region").slope_per_doubling.agg(["count", "median", "min", "max"]).reset_index()
        write_table(T17b, paths, "T17b_slope_by_region", float_fmt="{:.3f}")
        numbers["slope_median"] = float(mm.slope_per_doubling.median()); numbers["slope_q1"] = float(mm.slope_per_doubling.quantile(0.25))
        numbers["slope_q3"] = float(mm.slope_per_doubling.quantile(0.75)); numbers["slope_min"] = float(mm.slope_per_doubling.min())
        numbers["slope_max"] = float(mm.slope_per_doubling.max()); numbers["slope_ols_r2"] = float(fit.rsquared)
        numbers["slope_ols_p_noise"] = float(fit.pvalues[2]); numbers["slope_spearman"] = T17.to_dict(orient="records")
    # ---------------- POST HOC: stratified by extrapolation ratio (T18), reference RPM-w
    t18 = []
    for lab, cond in (("ratio <= 8", df.ratio <= 8), ("ratio >= 16", df.ratio >= 16)):
        dd = df[cond & df.method.isin(["RPM", "RPM-w", "SLOPE-T", "FLAT", "IPL3"])]
        pm = dd.groupby(["task", "method"]).abs_err.mean().unstack(); pmed = dd.groupby(["task", "method"]).abs_err.median().unstack()
        stt = pd.DataFrame(paired_comparison(pm["RPM-w"].values, {m: pm[m].values for m in ["RPM", "SLOPE-T", "FLAT", "IPL3"]}, seed=17))
        for m in ["RPM-w", "RPM", "SLOPE-T", "FLAT", "IPL3"]:
            row = {"stratum": lab, "method": m, "n_tasks": int(pm[m].notna().sum()), "mean_task_mean_abs": float(pm[m].mean()),
                   "mean_task_median_abs": float(pmed[m].mean())}
            if m != "RPM-w":
                s_ = stt[stt.comparison == m].iloc[0]
                row.update({"diff_vs_RPMw": float(s_.median_diff), "p_holm": float(s_.p_holm), "RPMw_wins": int(s_.ref_wins), "RPMw_losses": int(s_.ref_losses)})
            t18.append(row)
    T18 = pd.DataFrame(t18); write_table(T18, paths, "T18_posthoc_by_ratio_stratum", float_fmt="{:.4f}")
    numbers["posthoc_ratio_strata"] = T18.to_dict(orient="records")
    # ---------------- POST HOC: noise-floor identifiability (T19): pilot-fitted noise fraction vs large-sample fit
    vt, fullnf = {}, {}
    for f in sorted(glob.glob(os.path.join(raw, "truth_*.npz"))):
        z = np.load(f, allow_pickle=True); name = os.path.basename(f)[6:-4].replace("__", ":")
        vt[name] = float(z["var_test"]); fits = json.loads(str(z["full_fits"]))
        fullnf[name] = {k: float(np.exp(v["log_sigma2"]) / vt[name]) for k, v in fits.items()}
    pp = df[df.method.isin(["RPM", "RPM-T"]) & df.log_sigma2.notna()].drop_duplicates(["task", "n0", "pilot", "method"])
    pp = pp.assign(nf=np.exp(pp.log_sigma2) / pp.task.map(vt))
    t19 = []
    for (t, m, n0), g in pp.groupby(["task", "method", "n0"]):
        ref = fullnf[t].get("free", np.nan)
        t19.append({"task": t, "method": m, "n0": int(n0), "noise_frac_full_pool_rfree": ref,
                    "noise_frac_full_pool_r1": fullnf[t].get("fixed1", np.nan), "median_pilot_noise_frac": float(g.nf.median()),
                    "pct_pilots_below_tenth_of_full": float(100 * (g.nf < 0.1 * ref).mean())})
    T19 = pd.DataFrame(t19)
    if len(T19):
        write_table(T19, paths, "T19_posthoc_noise_floor_identifiability", float_fmt="{:.4f}")
        numbers["noise_floor"] = {f"{m}_n0_{n0}": {"median_pct_pilots_below_tenth": float(g.pct_pilots_below_tenth_of_full.median()),
                                                   "median_ratio_pilot_to_full": float((g.median_pilot_noise_frac / g.noise_frac_full_pool_rfree).median())}
                                  for (m, n0), g in T19.groupby(["method", "n0"])}
        # per-pilot link between noise-floor underestimation and signed forecast error (RPM-T, n/n0 >= 8)
        from scipy.stats import spearmanr
        q = df[(df.method == "RPM-T") & df.log_sigma2.notna()].copy()
        q["lr"] = np.log(np.exp(q.log_sigma2) / q.task.map(vt) / q.task.map({t: v.get("free", np.nan) for t, v in fullnf.items()}))
        q["serr"] = q.fc_logrmse - q.truth_ridge_logrmse
        q = q[q.ratio >= 8]
        col = q.lr < np.log(0.1)
        pil = q.drop_duplicates(["task", "n0", "pilot"])
        numbers["noise_floor"]["collapse_RPM_T"] = {
            "pct_pilots_noise_below_tenth": float(100 * (pil.lr < np.log(0.1)).mean()),
            "pct_pilots_noise_below_tenth_by_n0": {int(k): float(100 * (g.lr < np.log(0.1)).mean()) for k, g in pil.groupby("n0")},
            "mean_signed_err_collapsed": float(q[col].serr.mean()), "mean_signed_err_other": float(q[~col].serr.mean()),
            "mean_abs_err_collapsed": float(q[col].serr.abs().mean()), "mean_abs_err_other": float(q[~col].serr.abs().mean()),
            "spearman_lr_vs_signed_err": float(spearmanr(q.lr.clip(-30, 30), q.serr).statistic), "n_forecasts": int(len(q))}
        k = T19[(T19.task == "KSSL-MIR:OC") & (T19.method == "RPM-T") & (T19.n0 == 25)]
        if len(k):
            numbers["noise_floor"]["example_KSSL_MIR_OC"] = {"pilot_median_n0_25": float(k.median_pilot_noise_frac.iloc[0]),
                                                            "full_pool_rfree": float(k.noise_frac_full_pool_rfree.iloc[0])}
    # ---------------- RPM-T eigen-spectrum ablation (T7b)
    abt_files = sorted(glob.glob(os.path.join(raw, "forecasts_ablT_*.csv")))
    if abt_files:
        ab = pd.concat([pd.read_csv(f) for f in abt_files], ignore_index=True)
        ab["abs_err"] = (ab.fc_logrmse - ab.truth_ridge_logrmse).abs(); ab["err"] = ab.fc_logrmse - ab.truth_ridge_logrmse
        V = ["RPM-T", "RPM-T-pilotcov", "RPM-T-pilotcov+tail", "RPM-T-U250"]
        ptb = ab.groupby(["task", "method"]).abs_err.mean().unstack()[V]
        stb = pd.DataFrame(paired_comparison(ptb["RPM-T"].values, {m: ptb[m].values for m in V[1:]}, seed=9))
        T7b = pd.DataFrame({"variant": V, "n_tasks": [int(ptb[m].notna().sum()) for m in V], "mean_abs_logerr": [ptb[m].mean() for m in V],
                            "median_task_abs_logerr": [ptb[m].median() for m in V], "mean_bias": [ab[ab.method == m].err.mean() for m in V]})
        T7b = T7b.merge(stb[["comparison", "median_diff", "ci95_lo", "ci95_hi", "p_holm", "ref_wins", "ref_losses"]].rename(columns={"comparison": "variant"}), on="variant", how="left")
        write_table(T7b, paths, "T7b_ablation_eigenspectrum_rpmT", float_fmt="{:.4f}")
        numbers["ablation_rpmT"] = rec(T7b, "variant") if "rec" in dir() else T7b.to_dict(orient="records")
    # ---------------- RQ1 theory validity (T9)
    tv, collapse = theory_validity(raw)
    tv["err_ridge"] = tv.theory_logrmse - tv.ridge_logrmse; tv["err_pls"] = tv.theory_logrmse - tv.pls_logrmse
    T9 = tv.groupby(["task", "mode"]).agg(mean_abs_err_ridge=("err_ridge", lambda x: np.mean(np.abs(x))),
                                          mean_abs_err_pls=("err_pls", lambda x: np.mean(np.abs(x))),
                                          r=("r", "first"), noise_frac=("noise_frac", "first")).reset_index()
    write_table(T9, paths, "T9_theory_validity_full_pool_fit")
    cd = collapse_dispersion(collapse, raw)
    if len(cd):
        write_table(cd, paths, "T9b_kappa_collapse_dispersion", float_fmt="{:.4f}")
        numbers["collapse_sd_median"] = float(cd.collapse_sd_log.median()); numbers["collapse_ref_sd_median"] = float(cd.no_collapse_ref_sd_log.median())
    # ---------------- efficiency (T10)
    T10 = pd.DataFrame([{"component": "RPM point forecast + 50 bootstrap refits (s per pilot)", "mean": timing.t_rpm_sec.mean(), "median": timing.t_rpm_sec.median(), "max": timing.t_rpm_sec.max()},
                        {"component": "Within-pilot sub-sampling curve for IPL/EXP/LOG fits (s per pilot)", "mean": timing.t_curve_sec.mean(), "median": timing.t_curve_sec.median(), "max": timing.t_curve_sec.max()}])
    write_table(T10, paths, "T10_runtime")
    # ---------------- error analysis (T13)
    rpm_t = per_task(df, "abs_err", ["RPM"]).RPM
    bias_t = df[df.method == "RPM"].groupby("task").err.mean()
    ea = T1.set_index("task")[["family", "eigen_decay_exponent", "n_pool"]].join(rpm_t.rename("rpm_mae")).join(bias_t.rename("rpm_bias"))
    ea = ea.join(T9[T9["mode"] == "free"].set_index("task")[["mean_abs_err_ridge", "noise_frac", "r"]].rename(columns={"mean_abs_err_ridge": "theory_fit_err"}))
    ea = ea.join(per_task(df, "abs_err", ["IPL3"]).IPL3.rename("ipl3_mae"))
    from scipy.stats import spearmanr
    cors = []
    for c in ["eigen_decay_exponent", "theory_fit_err", "noise_frac", "r", "n_pool"]:
        ok = ea[[c, "rpm_mae"]].dropna()
        rho, p = spearmanr(ok[c], ok["rpm_mae"]); cors.append({"descriptor": c, "spearman_rho": rho, "p": p, "n": len(ok)})
    write_table(ea.reset_index().sort_values("rpm_mae", ascending=False), paths, "T13_error_analysis_per_task")
    write_table(pd.DataFrame(cors), paths, "T13b_error_correlates", float_fmt="{:.4f}")
    # ---------------- robustness (T8)
    rob_path = os.path.join(paths["results"], "robustness_raw.csv")
    if os.path.exists(rob_path):
        rb = pd.read_csv(rob_path)
        rb["abs_err"] = (rb.fc_logrmse - rb.truth_ridge_logrmse).abs(); rb["err"] = rb.fc_logrmse - rb.truth_ridge_logrmse
        cov80 = lambda g: np.mean((g.lo80 <= g.truth_ridge_logrmse) & (g.truth_ridge_logrmse <= g.hi80)) * 100 if g.lo80.notna().any() else np.nan
        T8 = rb.groupby(["variant", "method"]).apply(lambda g: pd.Series({"n_tasks": g.task.nunique(), "mean_abs_logerr": g.groupby("task").abs_err.mean().mean(),
                                                                           "mean_bias": g.err.mean(), "coverage80": cov80(g)})).reset_index()
        write_table(T8, paths, "T8_robustness")
        numbers["robustness"] = T8.to_dict(orient="records")
    # ---------------- E0 simulation (T0)
    sim_path = os.path.join(paths["results"], "simulation_raw.csv")
    if os.path.exists(sim_path):
        sm = pd.read_csv(sim_path); sm["abs_err"] = sm.err.abs()
        T0 = sm.groupby(["r", "noise_frac", "n0", "method"]).agg(median_abs_err=("abs_err", "median"), mean_abs_err=("abs_err", "mean"),
                                                                median_bias=("err", "median")).reset_index()
        write_table(T0, paths, "T0_simulation")
        T0b = sm.groupby(["method", "n0"]).agg(median_abs_err=("abs_err", "median"), median_bias=("err", "median")).reset_index()
        write_table(T0b, paths, "T0b_simulation_by_n0")
        numbers["simulation"] = T0b.to_dict(orient="records")
        numbers["simulation_full"] = T0.to_dict(orient="records")
    # ---------------- numbers.json
    def rec(t, key="method"):
        return {r[key]: {k: (float(v) if isinstance(v, (int, float, np.floating, np.integer)) else v) for k, v in r.items()} for r in t.to_dict(orient="records")}
    numbers.update({"main_ridge": rec(T2), "stats_ridge": rec(T3, "comparison"), "main_pls": rec(T4),
                    "stats_pls": rec(T4s, "comparison"), "coverage": T5.to_dict(orient="records"),
                    "decisions": T6.to_dict(orient="records"), "ablation": rec(T7, "variant"),
                    "sensitivity_no_icraf_visnir": rec(S0), "sensitivity_no_icraf_visnir_stats": rec(S0s, "comparison"),
                    "by_n0": T2b.to_dict(orient="records"), "theory_validity_summary": T9.groupby("mode")[["mean_abs_err_ridge", "mean_abs_err_pls"]].mean().to_dict(),
                    "theory_validity_median": T9.groupby("mode")[["mean_abs_err_ridge", "mean_abs_err_pls"]].median().to_dict(),
                    "error_correlates": cors, "runtime": T10.to_dict(orient="records"),
                    "pct_tasks_rpm_better_than_ipl3": float(100 * np.mean(per_task(df).RPM < per_task(df).IPL3)),
                    "pct_tasks_rpm_better_than_flat": float(100 * np.mean(per_task(df).RPM < per_task(df).FLAT))})
    json.dump(numbers, open(os.path.join(paths["results"], "numbers.json"), "w"), indent=1, default=str)
    df.to_csv(os.path.join(paths["results"], "raw_results.csv"), index=False)
    json.dump({"main": T2.to_dict(orient="records"), "pls": T4.to_dict(orient="records")}, open(os.path.join(paths["results"], "metrics.json"), "w"), indent=1, default=str)
    json.dump({"ridge": T3.to_dict(orient="records"), "pls": T4s.to_dict(orient="records"), "ablation": T7.to_dict(orient="records")},
              open(os.path.join(paths["results"], "statistics.json"), "w"), indent=1, default=str)
    # ---------------- figures
    F.make_all(df, T1, tv, collapse, T5, dec_rows, T7, ea, paths, rob_path)
    log.write(json.dumps({"stage": "analysis", "tasks": len(tasks)}) + "\n"); log.flush()
