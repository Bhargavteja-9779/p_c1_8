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

MAIN_METHODS = ["RPM", "RPM-w", "RPM-T", "RPM-wT", "IPL3", "IPL2", "EXP3", "LOG2", "FLAT", "DFOLS"]
ABL_METHODS = ["RPM", "RPM-rfree", "RPM-ML2", "RPM-pilotcov", "RPM-pilotcov+tail", "RPM-U250", "RPM-Uextra",
               "RPM-kfold10", "RPM-cut0.5", "RPM-cut0.95"]
LABELS = {"RPM": "RPM (pre-registered, r = 1)", "RPM-w": "RPM-w (weighted path fit)", "RPM-T": "RPM-T (transferred alignment)", "RPM-wT": "RPM-wT (weighted + transferred)", "IPL3": "Inverse power law (IPL3)", "IPL2": "Power law (IPL2)",
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
            rows.append({"method": m, "nominal": lev, "coverage_rows": 100 * cov.mean(), "coverage_task_mean": 100 * per_t.mean(),
                         "coverage_task_median": 100 * per_t.median(), "mean_width_log": width.mean(),
                         "mean_width_factor": float(np.exp(width.mean()))})
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
        both = pta[["RPM", m]].dropna()
        lo, hi = bootstrap_ci_mean(both[m].values - both["RPM"].values, seed=5) if m != "RPM" else (0.0, 0.0)
        abl.append({"variant": m, "n_tasks": len(both), "mean_abs_logerr": both[m].mean(), "rpm_same_tasks": both["RPM"].mean(),
                    "mean_diff_vs_rpm": (both[m] - both["RPM"]).mean(), "ci95_lo": lo, "ci95_hi": hi})
    T7 = pd.DataFrame(abl)
    st = paired_comparison(pta["RPM"].values, {m: pta[m].values for m in ABL_METHODS if m != "RPM" and m in pta}, seed=7)
    T7 = T7.merge(pd.DataFrame(st)[["comparison", "p_raw", "p_holm", "rank_biserial"]].rename(columns={"comparison": "variant"}), on="variant", how="left")
    write_table(T7, paths, "T7_ablation", float_fmt="{:.4f}")
    # ---------------- RQ1 theory validity (T9)
    tv, collapse = theory_validity(raw)
    tv["err_ridge"] = tv.theory_logrmse - tv.ridge_logrmse; tv["err_pls"] = tv.theory_logrmse - tv.pls_logrmse
    T9 = tv.groupby(["task", "mode"]).agg(mean_abs_err_ridge=("err_ridge", lambda x: np.mean(np.abs(x))),
                                          mean_abs_err_pls=("err_pls", lambda x: np.mean(np.abs(x))),
                                          r=("r", "first"), noise_frac=("noise_frac", "first")).reset_index()
    write_table(T9, paths, "T9_theory_validity_full_pool_fit")
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
