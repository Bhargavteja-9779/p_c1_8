"""Real-world case study (session 4): planning a calibration campaign with a target RMSEP.

A laboratory must reach a target RMSEP T and wants to buy as few reference analyses as possible; the largest affordable
calibration is N_max (the largest truth-grid size of the task, >= 800). Targets: T = (1 + tau) x true RMSEP at N_max,
tau in {0.05, 0.15} (reachable within the budget). Oracle n* = smallest grid size whose true RMSEP <= T.
Policies (cost = number of reference analyses bought, grid sizes only):
  FIXED       buy N_max.
  ONE-SHOT(M) from a 50-sample pilot buy n_hat = smallest grid n >= 50 with forecast(n) <= T (N_max if none).
  STAGED(M)   from the 50-sample pilot compute n_hat; if n_hat <= 100 buy it; otherwise first extend to 200 samples,
              re-forecast from the 200-sample pilot and buy the smallest n >= 200 with forecast <= T (N_max if none).
Outcome: SUCCESS if true RMSEP at the bought size <= T; otherwise the target is missed and another purchase round is needed.
Reported per policy: success rate, mean cost relative to the oracle (cost / n*), and expected total cost with recourse
(on failure the lab continues to n*; total = max(bought, n*)), relative to N_max, plus the number of purchase rounds.
Pilots of 50 and 200 samples are independent random draws from the same pool (approximation of nested batches).
"""
import os
import numpy as np
import pandas as pd

METHODS = ["B-RPM", "FLAT", "SLOPE-T", "RPM", "IPL3", "WEI"]
PER_TASK = {}
QGRID = np.round(np.arange(0.05, 0.996, 0.025), 3)


def decision_calibrated(R, m, q, scheme):
    """Conformal-risk-control-style threshold: for each held-out group (source for LOSO, family for LOFO) choose the
    smallest threshold q' whose success rate on the OTHER groups (task-averaged) is >= q; apply it to the held-out group."""
    from experiments.refinement import source_of
    from experiments.bayes import family_of_source
    grp = R.task.map(source_of) if scheme == "LOSO" else R.task.map(lambda t: family_of_source(source_of(t)))
    cost, ok = [], []
    for gv in grp.unique():
        tr, te = R[grp != gv], R[grp == gv]
        qsel = QGRID[-1]
        for qq in QGRID:
            col = f"G:{m}:{qq:.2f}_ok"
            if col in tr and tr.groupby("task")[col].mean().mean() >= q:
                qsel = qq; break
        c_ = f"G:{m}:{qsel:.2f}_cost"; o_ = f"G:{m}:{qsel:.2f}_ok"
        d = te[["task", "n_star", c_, o_]].dropna()
        cost.append(pd.DataFrame({"task": d.task, "over": d[c_] / d.n_star, "ok": d[o_].astype(float),
                                  "tot": np.maximum(d[c_], d.n_star) / te.loc[d.index, "n_max"], "q_used": qsel}))
    x = pd.concat(cost).groupby("task").mean()
    PER_TASK[(m, q)] = x
    return {"policy": f"CAL{int(q * 100)}:{m}", "n_tasks": len(x), "success_rate": x.ok.mean(), "cost_over_oracle": x.over.mean(),
            "total_cost_rel_Nmax": x.tot.mean(), "mean_rounds": 1 + (1 - x.ok).mean(), "q_used_mean": x.q_used.mean()}


def _nhat(fc, ns, T, nmin, nmax):
    ok = [(n, f) for n, f in zip(ns, fc) if n >= nmin and f <= T]
    return min(n for n, _ in ok) if ok else nmax


def _recal(df):
    """LOSO predictive sd for log RMSEP forecasts. B-RPM: band-based sd x inflation factor from OTHER sources' standardised
    errors (80 % level). SLOPE-T: empirical sd of the log error of OTHER sources in the same extrapolation-ratio bin."""
    from experiments.refinement import source_of
    d = df[df.ratio >= 2].copy(); d["source"] = d.task.map(source_of)
    b = d[d.method == "B-RPM"].copy(); b["sd0"] = (b.hi80 - b.lo80) / 2.5631
    b["z"] = ((b.fc_logrmse - b.truth_ridge_logrmse) / b.sd0).abs()
    cfac = {s_: float(b[b.source != s_].z.quantile(0.8)) / 1.2816 for s_ in b.source.unique()}
    from experiments.bayes import family_of_source
    d["fam"] = d.source.map(family_of_source)
    bl = d[d.method == "B-RPM-LOFO"].copy(); bl["sd0"] = (bl.hi80 - bl.lo80) / 2.5631
    bl["z"] = ((bl.fc_logrmse - bl.truth_ridge_logrmse) / bl.sd0).abs()
    for f_ in bl.fam.unique():
        cfac[("LOFO", f_)] = float(bl[bl.fam != f_].z.quantile(0.8)) / 1.2816
    ssd = {}
    for m, key in (("SLOPE-T", "source"), ("SLOPE-T-LOFO", "fam")):
        sl = d[d.method == m].copy(); sl["rb"] = np.round(np.log2(sl.ratio)).astype(int)
        sl["e"] = sl.fc_logrmse - sl.truth_ridge_logrmse
        for v in sl[key].unique():
            for r_ in sl.rb.unique():
                ssd[(m, v, r_)] = float(sl[(sl[key] != v) & (sl.rb == r_)].e.std())
    return cfac, ssd


def run_campaign(df, out_tab, qs=(0.5, 0.8, 0.9)):
    from scipy.stats import norm
    from experiments.refinement import source_of
    cfac, ssd = _recal(df)
    rows = []
    tr = df[df.method == "FLAT"].groupby(["task", "split", "n"]).truth_ridge_logrmse.first()
    for (task, split), g in df[df.n0.isin([50, 200])].groupby(["task", "split"]):
        t = tr.loc[(task, split)]
        nmax = int(t.index.max())
        if nmax < 800:
            continue
        grid = np.array(sorted(t.index)); tv = t.loc[grid].values
        for tau in (0.05, 0.15):
            T = tv[-1] + np.log(1 + tau)
            nstar = int(grid[np.argmax(tv <= T)])
            for s in sorted(g.pilot.unique()):
                rec = {"task": task, "split": split, "pilot": s, "tau": tau, "n_star": nstar, "n_max": nmax}
                rec["FIXED_cost"] = nmax; rec["FIXED_ok"] = True; rec["FIXED_rounds"] = 1
                for m in METHODS:
                    a = g[(g.method == m) & (g.n0 == 50) & (g.pilot == s)].sort_values("n")
                    if not len(a):
                        continue
                    n1 = _nhat(a.fc_logrmse.values, a.n.values, T, 50, nmax)
                    ok1 = bool(t.loc[n1] <= T + 1e-12)
                    rec[f"ONE:{m}_cost"] = n1; rec[f"ONE:{m}_ok"] = ok1
                    rec[f"ONE:{m}_total"] = max(n1, nstar); rec[f"ONE:{m}_rounds"] = 1 + (not ok1)
                    if n1 <= 100:
                        n2 = n1; rounds = 1
                    else:
                        b = g[(g.method == m) & (g.n0 == 200) & (g.pilot == s)].sort_values("n")
                        n2 = _nhat(b.fc_logrmse.values, b.n.values, T, 200, nmax) if len(b) else n1
                        rounds = 2
                    ok2 = bool(t.loc[n2] <= T + 1e-12)
                    rec[f"STG:{m}_cost"] = n2; rec[f"STG:{m}_ok"] = ok2
                    rec[f"STG:{m}_total"] = max(n2, nstar); rec[f"STG:{m}_rounds"] = rounds + (not ok2)
                # risk-calibrated planning: smallest n with P(RMSEP(n) <= T) >= q
                from experiments.bayes import family_of_source
                for m in ("B-RPM", "SLOPE-T", "B-RPM-LOFO", "SLOPE-T-LOFO"):
                    a = g[(g.method == m) & (g.n0 == 50) & (g.pilot == s)].sort_values("n")
                    a = a[a.n >= 100]
                    if not len(a):
                        continue
                    src = source_of(task)
                    fam_ = family_of_source(src)
                    if m == "B-RPM":
                        sd = (a.hi80 - a.lo80).values / 2.5631 * cfac[src]
                    elif m == "B-RPM-LOFO":
                        sd = (a.hi80 - a.lo80).values / 2.5631 * cfac[("LOFO", fam_)]
                    else:
                        key = src if m == "SLOPE-T" else fam_
                        sd = np.array([ssd.get((m, key, int(round(np.log2(r)))), np.nan) for r in a.ratio])
                    pr = norm.cdf((T - a.fc_logrmse.values) / np.maximum(sd, 1e-3))
                    for qq in QGRID:                       # full threshold grid for decision calibration
                        okn = [n for n, p_ in zip(a.n.values, pr) if p_ >= qq]
                        n1 = int(min(okn)) if okn else nmax
                        rec[f"G:{m}:{qq:.2f}_cost"] = n1; rec[f"G:{m}:{qq:.2f}_ok"] = bool(t.loc[n1] <= T + 1e-12)
                    for q in qs:
                        okn = [n for n, p_ in zip(a.n.values, pr) if p_ >= q]
                        n1 = int(min(okn)) if okn else nmax
                        ok1 = bool(t.loc[n1] <= T + 1e-12)
                        k = f"RISK{int(q * 100)}:{m}"
                        rec[f"{k}_cost"] = n1; rec[f"{k}_ok"] = ok1; rec[f"{k}_total"] = max(n1, nstar); rec[f"{k}_rounds"] = 1 + (not ok1)
                rows.append(rec)
    R = pd.DataFrame(rows)
    pol = ["FIXED"] + [f"{p}:{m}" for p in ("ONE", "STG") for m in METHODS] + \
          [f"RISK{int(q * 100)}:{m}" for m in ("B-RPM", "SLOPE-T", "B-RPM-LOFO", "SLOPE-T-LOFO") for q in qs]
    summ = []
    for p in pol:
        if f"{p}_cost" not in R:
            continue
        d = R[[ "task", "tau", "n_star", "n_max", f"{p}_cost", f"{p}_ok"] + ([f"{p}_total", f"{p}_rounds"] if p != "FIXED" else [])].dropna()
        tot = d[f"{p}_total"] if p != "FIXED" else d[f"{p}_cost"]
        rnd = d[f"{p}_rounds"] if p != "FIXED" else 1
        tm = pd.DataFrame({"task": d.task, "ok": d[f"{p}_ok"].astype(float), "over": d[f"{p}_cost"] / d.n_star,
                           "tot": tot / d.n_max, "rounds": rnd}).groupby("task").mean()
        summ.append({"policy": p, "n_tasks": len(tm), "success_rate": tm.ok.mean(), "cost_over_oracle": tm.over.mean(),
                     "total_cost_rel_Nmax": tm.tot.mean(), "mean_rounds": tm.rounds.mean() if p != "FIXED" else 1.0})
    for m, scheme in (("B-RPM", "LOSO"), ("SLOPE-T", "LOSO"), ("B-RPM-LOFO", "LOFO"), ("SLOPE-T-LOFO", "LOFO")):
        for q in (0.8, 0.9):
            summ.append(decision_calibrated(R, m, q, scheme))
    S = pd.DataFrame(summ)
    from scipy.stats import wilcoxon
    tests = []
    for q in (0.8, 0.9):
        for a_, b_ in (("B-RPM-LOFO", "SLOPE-T-LOFO"), ("B-RPM", "SLOPE-T")):
            xa, xb = PER_TASK[(a_, q)], PER_TASK[(b_, q)]
            idx = xa.index.intersection(xb.index)
            for col in ("ok", "over"):
                dlt = (xa.loc[idx, col] - xb.loc[idx, col]).values
                try:
                    p = float(wilcoxon(dlt).pvalue)
                except ValueError:
                    p = 1.0
                rng = np.random.default_rng(1); bs = [rng.choice(dlt, len(dlt)).mean() for _ in range(4000)]
                tests.append({"q": q, "method": a_, "reference": b_, "endpoint": "success" if col == "ok" else "cost_over_oracle",
                              "mean_diff": float(dlt.mean()), "ci_lo": float(np.quantile(bs, 0.025)), "ci_hi": float(np.quantile(bs, 0.975)),
                              "p": p, "n_tasks": len(idx), "wins": int((dlt > 0).sum())})
    pd.DataFrame(tests).to_csv(os.path.join(out_tab, "TB12b_campaign_tests.csv"), index=False)
    orc = R.groupby("task").apply(lambda x: (x.n_star / x.n_max).mean(), include_groups=False).mean()
    S.loc[len(S)] = {"policy": "ORACLE", "n_tasks": R.task.nunique(), "success_rate": 1.0, "cost_over_oracle": 1.0,
                     "total_cost_rel_Nmax": orc, "mean_rounds": 1.0}
    os.makedirs(out_tab, exist_ok=True)
    S.to_csv(os.path.join(out_tab, "TB12_campaign_planning.csv"), index=False)
    return S, R


if __name__ == "__main__":
    from experiments.bayes_analysis import load_all, add_slope
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    raw = os.path.join(root, "results", "raw")
    df = load_all(raw); df, _ = add_slope(df, raw)
    S, R = run_campaign(df, os.path.join(root, "tables"))
    pd.set_option("display.width", 200); print(S.round(3))
