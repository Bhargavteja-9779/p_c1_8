#!/usr/bin/env python3
"""Retrieve titles/abstracts/history dates of a journal's papers matching a topic query (PubMed)."""
import argparse, json, time, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
def get(u):
    for t in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "research-script/1.0"}), timeout=90) as r:
                return r.read()
        except Exception:
            time.sleep(2 * (t + 1))
    raise RuntimeError(u)
ap = argparse.ArgumentParser()
ap.add_argument("--term", required=True); ap.add_argument("--retmax", type=int, default=400); ap.add_argument("--out", required=True)
a = ap.parse_args()
d = json.loads(get(E + "esearch.fcgi?" + urllib.parse.urlencode({"db": "pubmed", "term": a.term, "retmax": a.retmax, "retmode": "json"})))
ids = d["esearchresult"]["idlist"]; print("count", d["esearchresult"]["count"], "fetched", len(ids))
recs = []
for i in range(0, len(ids), 150):
    root = ET.fromstring(get(E + "efetch.fcgi?" + urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids[i:i+150]), "retmode": "xml"})))
    for art in root.findall(".//PubmedArticle"):
        t = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
        ab = " ".join("".join(x.itertext()) for x in art.findall(".//Abstract/AbstractText"))
        doi = next((x.text for x in art.findall(".//ArticleId") if x.get("IdType") == "doi"), None)
        y = art.findtext(".//PubDate/Year") or art.findtext(".//ArticleDate/Year")
        recs.append({"pmid": art.findtext(".//PMID"), "year": y, "doi": doi, "title": t, "abstract": ab})
    time.sleep(0.4)
json.dump(recs, open(a.out, "w"), indent=1)
