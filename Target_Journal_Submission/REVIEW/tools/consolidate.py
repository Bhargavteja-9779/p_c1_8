#!/usr/bin/env python3
"""Consolidate one review cycle into REVIEW/review_XX.md.

Inputs : REVIEW/raw/cycle_XX/R*.json        (independent reviewer reports, written by the reviewer agents)
         REVIEW/raw/cycle_XX/decisions.json  (verification + response per issue id, written by the author agent):
             {"<issue id>": {"verdict": "accepted|partly|rejected", "severity_after_verification": "...",
                             "verification": "...", "response": "...", "status": "fixed|fixed-text|open|wontfix"}}
Output : REVIEW/review_XX.md
Usage  : python3 consolidate.py 01
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REVIEW = os.path.dirname(HERE)
SEV = ["FATAL", "CRITICAL", "MAJOR", "MODERATE", "MINOR"]


def main(cycle):
    cyc = f"{int(cycle):02d}"
    raw = os.path.join(REVIEW, "raw", f"cycle_{cyc}")
    files = sorted(glob.glob(os.path.join(raw, "R*.json")), key=lambda p: int(os.path.basename(p)[1:].split(".")[0]))
    reviews = [json.load(open(f)) for f in files]
    dpath = os.path.join(raw, "decisions.json")
    decisions = json.load(open(dpath)) if os.path.exists(dpath) else {}
    out = [f"# Review cycle {cyc}", "",
           f"Independent reviewer reports: {len(reviews)} (raw JSON in `REVIEW/raw/cycle_{cyc}/`). "
           "Every FATAL/CRITICAL/MAJOR issue was verified against the code, data and results before acting; "
           "the verdict, the response and the resulting change are listed per issue.", ""]
    out += ["## Recommendations", "", "| Reviewer | Recommendation | FATAL | CRITICAL | MAJOR | MODERATE | MINOR |", "|---|---|---|---|---|---|---|"]
    tot = {s: 0 for s in SEV}
    for r in reviews:
        c = {s: sum(1 for i in r.get("issues", []) if i.get("severity") == s) for s in SEV}
        for s in SEV:
            tot[s] += c[s]
        out.append(f"| {r.get('reviewer','?')} | {r.get('recommendation','?')} | " + " | ".join(str(c[s]) for s in SEV) + " |")
    out.append("| **Total** | | " + " | ".join(str(tot[s]) for s in SEV) + " |")
    out.append("")
    for s in SEV:
        items = [(r, i) for r in reviews for i in r.get("issues", []) if i.get("severity") == s]
        if not items:
            continue
        out += [f"## {s} issues ({len(items)})", ""]
        for r, i in items:
            d = decisions.get(i.get("id", ""), {})
            out += [f"### {i.get('id','?')} — {i.get('title','')}", "",
                    f"*Reviewer:* {r.get('reviewer','?')}", "",
                    f"*Issue:* {i.get('description','')}", "",
                    f"*Evidence cited:* {i.get('evidence','')}", "",
                    f"*Requested action:* {i.get('corrective_action','')}" + (f" (new experiment: {i.get('proposed_experiment','')})" if i.get("requires_new_experiment") else ""), ""]
            if d:
                out += [f"*Verification:* **{d.get('verdict','?')}**" + (f" (severity after verification: {d['severity_after_verification']})" if d.get("severity_after_verification") else "") + f" — {d.get('verification','')}", "",
                        f"*Response / change:* {d.get('response','')} — status: **{d.get('status','open')}**", ""]
            else:
                out += ["*Verification / response:* pending", ""]
    st = {}
    for d in decisions.values():
        st[d.get("status", "open")] = st.get(d.get("status", "open"), 0) + 1
    out += ["## Status summary", "", "| Status | Issues |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(st.items())]
    path = os.path.join(REVIEW, f"review_{cyc}.md")
    open(path, "w").write("\n".join(out) + "\n")
    print("wrote", path, "issues:", sum(tot.values()), "decisions:", len(decisions))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1")
