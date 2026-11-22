"""Decision value of the planning workflow (added in version 2; uses existing forecasts only).

Scenario: the analyst has an absolute RMSEP target T and a budget of N reference samples (N = 400 or 800). Is T
reachable at N? Targets are set 15 % above and 15 % below the true RMSEP at N (one reachable and one unreachable
target per task), so a policy is correct when its forecast falls on the right side of T.
Policies (per task, averaged over pilots/splits):
  one-shot(M):  decide from a pilot of n0 = N/8 with forecaster M.
  staged(M):    decide from a pilot of 2 n0 = N/4 (i.e. after a second batch of n0 samples).
  gated:        decide from the n0 pilot with B-RPM if the prior-free identification set excludes T (the pilot settles the
                question); otherwise take the second batch and decide with B-RPM from 2 n0. Reported: accuracy and the share
                of cases that needed the second batch (extra reference cost).
Pilots of size n0 and 2 n0 are independent random draws from the same pool (an approximation of a nested second batch).
"""
import os
import numpy as np
import pandas as pd


def run_staged(df, out_tab):
    rows = []
    for N in (400, 800):
        n0 = N // 8
        d = df[(df.n == N) & df.n0.isin([n0, 2 * n0])]
        tasks = sorted(set(d[d.n0 == n0].task) & set(d[d.n0 == 2 * n0].task))
        for c, reach in ((1.15, True), (1 / 1.15, False)):
            for t in tasks:
                g = d[d.task == t]
                lt = g.truth_ridge_logrmse.iloc[0] + np.log(c)       # log target (truth may differ by split; use per row)
                rec = {"N": N, "task": t, "target": "reachable" if reach else "unreachable"}
                for m in ("B-RPM", "FLAT", "SLOPE-T", "RPM", "IPL3"):
                    for stage, k in (("one-shot", n0), ("staged", 2 * n0)):
                        x = g[(g.method == m) & (g.n0 == k)]
                        if len(x):
                            tgt = x.truth_ridge_logrmse + np.log(c)
                            rec[f"{stage}:{m}"] = float(((x.fc_logrmse <= tgt) == reach).mean())
                b1 = g[(g.method == "B-RPM") & (g.n0 == n0)].copy()
                b2 = g[(g.method == "B-RPM") & (g.n0 == 2 * n0)]
                if len(b1) and len(b2):
                    tgt = b1.truth_ridge_logrmse + np.log(c)
                    settled = (b1.id_hi <= tgt) | (b1.id_lo > tgt)
                    dec1 = (b1.id_hi <= tgt)                          # set entirely below target -> reachable
                    acc_settled = ((dec1 == reach) & settled).sum()
                    acc2 = float(((b2.fc_logrmse <= b2.truth_ridge_logrmse + np.log(c)) == reach).mean())
                    rec["gated"] = float((acc_settled + (~settled).sum() * acc2) / len(b1))
                    rec["gated_second_batch_share"] = float((~settled).mean())
                rows.append(rec)
    t = pd.DataFrame(rows)
    summ = t.drop(columns=["task"]).groupby(["N", "target"]).mean().T
    allm = t.drop(columns=["task", "target"]).groupby("N").mean().T
    os.makedirs(out_tab, exist_ok=True)
    allm.to_csv(os.path.join(out_tab, "TB10_staged_decision.csv"))
    summ.to_csv(os.path.join(out_tab, "TB10b_staged_decision_by_target.csv"))
    return allm, summ


if __name__ == "__main__":
    from experiments.bayes_analysis import load_all, add_slope, add_gain
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    raw = os.path.join(root, "results", "raw")
    df = load_all(raw); df, _ = add_slope(df, raw); df = add_gain(df)
    a, s = run_staged(df, os.path.join(root, "tables"))
    print(a.round(3)); print(s.round(3))
