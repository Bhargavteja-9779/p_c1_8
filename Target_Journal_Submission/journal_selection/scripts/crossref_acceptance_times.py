#!/usr/bin/env python3
"""Empirical submission-to-acceptance times from Crossref 'assertion' metadata.

Springer Nature and Taylor & Francis deposit 'received' and 'accepted' dates as
Crossref assertions. Elsevier/OUP/IEEE/Wiley/SAGE do not (verified on 2026-11-15),
so those publishers are measured via PubMed instead (pubmed_acceptance_times.py).
"""
import argparse, json, sys, time, statistics, urllib.request, urllib.parse
from datetime import datetime

API = "https://api.crossref.org/works"

def get(url, tries=6):
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "research-script/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read())
        except Exception:
            time.sleep(3 * (t + 1))
    raise RuntimeError("failed " + url)

def parse_date(s):
    s = str(s).strip()
    for fmt in ("%Y-%m-%d", "%d %B %Y", "%d %b %Y", "%B %d, %Y", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--journals", required=True)
    ap.add_argument("--from_date", default="2025-07-01")
    ap.add_argument("--until_date", default="2026-10-31")
    ap.add_argument("--max_items", type=int, default=400)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = []
    for j in json.load(open(a.journals)):
        days, seen, cursor = [], 0, "*"
        while seen < a.max_items:
            q = urllib.parse.urlencode({
                "filter": f"issn:{j['issn']},from-pub-date:{a.from_date},until-pub-date:{a.until_date},type:journal-article",
                "rows": 200, "cursor": cursor, "select": "DOI,assertion,title"})
            try:
                d = get(API + "?" + q)
            except Exception as e:
                print("ERR", j["name"], e, file=sys.stderr); break
            items = d["message"]["items"]
            if not items:
                break
            for it in items:
                seen += 1
                A = {x.get("name"): x.get("value") for x in it.get("assertion", [])}
                r, ac = parse_date(A.get("received", "")), parse_date(A.get("accepted", ""))
                if r and ac and 0 <= (ac - r).days < 1500:
                    days.append((ac - r).days)
            cursor = d["message"].get("next-cursor")
            time.sleep(1.0)
            if not cursor:
                break
        s = {"journal": j["name"], "issn": j["issn"], "sampled": seen, "with_dates": len(days)}
        if days:
            days.sort(); n = len(days); qs = statistics.quantiles(days, n=4) if n >= 4 else [days[0], 0, days[-1]]
            s.update({"n": n, "median": statistics.median(days), "mean": round(statistics.mean(days), 1),
                      "q1": qs[0], "q3": qs[2], "pct_le_60": round(100 * sum(x <= 60 for x in days) / n, 1),
                      "pct_le_100": round(100 * sum(x <= 100 for x in days) / n, 1)})
        res.append(s)
        print(json.dumps(s), flush=True)
    json.dump(res, open(a.out, "w"), indent=1)

if __name__ == "__main__":
    main()
