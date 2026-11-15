#!/usr/bin/env python3
"""Empirical submission-to-acceptance times from PubMed history dates.

For each journal (ISSN), retrieves research articles that entered PubMed in a
date window, parses <History> PubMedPubDate entries (received / revised /
accepted) and reports the distribution of received->accepted durations.

Caveats (reported in journal_verification.md):
  * Only ACCEPTED papers have an acceptance date (this is inherent to the
    definition of submission-to-acceptance).
  * 'received' is the publisher-deposited original-receipt date; some
    publishers reset it for 'reject-and-resubmit' manuscripts, which would bias
    durations downward.
  * Reviews / editorials are excluded via publication-type filters.
"""
import argparse, json, sys, time, statistics, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
from datetime import date

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def get(url, tries=4):
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "research-script/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # network hiccup / 429
            time.sleep(2 * (t + 1))
    raise RuntimeError("failed: " + url)

def esearch(term, retmax=400):
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": retmax,
                                "retmode": "json", "sort": "pub_date"})
    d = json.loads(get(EUTILS + "esearch.fcgi?" + q))
    return d["esearchresult"]["idlist"], int(d["esearchresult"]["count"])

def pdate(el):
    try:
        y = int(el.findtext("Year")); m = int(el.findtext("Month") or 1); d = int(el.findtext("Day") or 1)
        return date(y, m, d)
    except Exception:
        return None

def efetch(ids):
    out = []
    for i in range(0, len(ids), 150):
        chunk = ids[i:i+150]
        q = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"})
        root = ET.fromstring(get(EUTILS + "efetch.fcgi?" + q))
        for art in root.findall(".//PubmedArticle"):
            pmid = art.findtext(".//PMID")
            hist = {}
            for pd in art.findall(".//History/PubMedPubDate"):
                st = pd.get("PubStatus")
                if st in ("received", "revised", "accepted"):
                    dd = pdate(pd)
                    if dd and (st not in hist or st == "revised"):
                        hist[st] = dd
            out.append((pmid, hist))
        time.sleep(0.4)
    return out

def summarize(days):
    if not days:
        return {}
    days = sorted(days)
    n = len(days)
    q = statistics.quantiles(days, n=4) if n >= 4 else [days[0], statistics.median(days), days[-1]]
    return {"n": n, "median": statistics.median(days), "mean": round(statistics.mean(days), 1),
            "q1": q[0], "q3": q[2], "pct_le_60": round(100 * sum(d <= 60 for d in days) / n, 1),
            "pct_le_100": round(100 * sum(d <= 100 for d in days) / n, 1)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--journals", required=True, help="json file: list of {name, issn}")
    ap.add_argument("--start", default="2025/07/01")
    ap.add_argument("--end", default="2026/10/31")
    ap.add_argument("--retmax", type=int, default=300)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    journals = json.load(open(a.journals))
    results = []
    for j in journals:
        term = (f'"{j["issn"]}"[IS] AND ("{a.start}"[EDAT] : "{a.end}"[EDAT]) '
                'AND journal article[pt] NOT review[pt] NOT editorial[pt] NOT comment[pt] NOT erratum[pt]')
        try:
            ids, count = esearch(term, a.retmax)
            recs = efetch(ids) if ids else []
        except Exception as e:
            print("ERR", j["name"], e, file=sys.stderr); continue
        days = [(h["accepted"] - h["received"]).days for _, h in recs
                if "received" in h and "accepted" in h and 0 <= (h["accepted"] - h["received"]).days < 1500]
        s = summarize(days)
        s.update({"journal": j["name"], "issn": j["issn"], "pubmed_hits_in_window": count,
                  "sampled": len(recs), "with_dates": len(days), "window": f"{a.start}-{a.end}"})
        results.append(s)
        print(json.dumps(s), flush=True)
    json.dump(results, open(a.out, "w"), indent=1)

if __name__ == "__main__":
    main()
