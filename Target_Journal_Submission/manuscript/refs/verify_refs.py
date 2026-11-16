#!/usr/bin/env python3
"""Verify every DOI / arXiv reference against Crossref / arXiv and store the verified metadata."""
import json, sys, time, urllib.request, urllib.parse, re
import xml.etree.ElementTree as ET

DOIS = {
 "ali2018": "10.1021/acs.analchem.8b02167",
 "mukherjee2003": "10.1089/106652703321825928",
 "figueroa2012": "10.1186/1472-6947-12-8",
 "viering2023": "10.1109/TPAMI.2022.3220744",
 "riley2020": "10.1136/bmj.m441",
 "ng2020": "10.5194/soil-6-565-2020",
 "kuang2014": "10.1016/j.geoderma.2013.09.022",
 "dobriban2018": "10.1214/17-AOS1549",
 "hastie2022": "10.1214/21-AOS2133",
 "canatar2021": "10.1038/s41467-021-23103-1",
 "spigler2020": "10.1088/1742-5468/abc61d",
 "loureiro2022": "10.1088/1742-5468/ac9825",
 "craven1979": "10.1007/BF01404567",
 "marchenko1967": "10.1070/SM1967v001n04ABEH001994",
 "rubin1981": "10.1214/aos/1176345338",
 "bach2024": "10.1137/23M1558781",
 "frank1993": "10.1080/00401706.1993.10485033",
 "wold2001": "10.1016/S0169-7439(01)00155-1",
 "dayal1997": "10.1002/(SICI)1099-128X(199701)11:1<73::AID-CEM435>3.0.CO;2-#",
 "barnes1989": "10.1366/0003702894202201",
 "savitzky1964": "10.1021/ac60214a047",
 "kennard1969": "10.1080/00401706.1969.10490666",
 "faber1997": "10.1002/(SICI)1099-128X(199705)11:3<181::AID-CEM459>3.0.CO;2-7",
 "bouckaert2011": "10.1016/j.chemolab.2011.08.008",
 "kramer2011": "10.1198/jasa.2011.tm10107",
 "westad2015": "10.1016/j.aca.2015.06.056",
 "mishra2022": "10.1016/j.trac.2022.116804",
 "rinnan2009": "10.1016/j.trac.2009.07.007",
 "safanelli2025": "10.1371/journal.pone.0296545",
 "anderson2020": "10.1016/j.postharvbio.2020.111202",
 "mango_data": "10.17632/46htwnp833.6",
 "borggaard1992": "10.1021/ac00029a018",
 "sanderman2020": "10.1002/saj2.20009",
 "kapoor2023": "10.1016/j.patter.2023.100804",
 "hoerl1970": "10.1080/00401706.1970.10488634",
 "wilcoxon1945": "10.2307/3001968",
 "kerby2014": "10.2466/11.IT.3.1",
 "talanta2026": "10.1016/j.talanta.2026.130941",
 "walsh2024": "10.1016/j.saa.2024.124003",
 "luca2017": "10.1016/j.geoderma.2016.11.015",
}
ARXIV = {"bordelon2020": "2002.02561", "simon2023": "2110.03922", "jacot2020": "2006.09796", "wei2022": "2203.06176",
         "atanasov2024": "2405.00592", "adriaensen2023": "2310.20447", "hestness2017": "1712.00409", "kaplan2020": "2001.08361", "konstantinidis2025": "2510.01210"}

def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    for t in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research-script/1.0"}), timeout=60) as r:
                return json.loads(r.read())["message"]
        except Exception as e:
            err = str(e); time.sleep(3 * (t + 1))
    return {"error": err}

out = {}
for k, doi in DOIS.items():
    m = crossref(doi)
    if "error" in m:
        out[k] = {"doi": doi, "verified": False, "error": m["error"]}
    else:
        au = [f"{a.get('family','')}, {a.get('given','')}".strip(", ") for a in m.get("author", [])]
        yr = (m.get("published-print") or m.get("published-online") or m.get("issued") or {}).get("date-parts", [[None]])[0][0]
        out[k] = {"doi": doi, "verified": True, "title": (m.get("title") or [""])[0], "authors": au,
                  "year": yr, "journal": (m.get("container-title") or [""])[0], "volume": m.get("volume"),
                  "issue": m.get("issue"), "pages": m.get("page") or m.get("article-number"), "type": m.get("type"),
                  "publisher": m.get("publisher")}
    print(k, out[k].get("verified"), out[k].get("year"), (out[k].get("title") or out[k].get("error",""))[:90], "|", out[k].get("journal"), flush=True)
    time.sleep(0.6)
q = urllib.parse.urlencode({"id_list": ",".join(ARXIV.values()), "max_results": 20})
x = urllib.request.urlopen("https://export.arxiv.org/api/query?" + q, timeout=60).read()
ns = {"a": "http://www.w3.org/2005/Atom"}
root = ET.fromstring(x)
byid = {}
for e in root.findall("a:entry", ns):
    aid = e.find("a:id", ns).text.rsplit("/", 1)[-1].split("v")[0]
    byid[aid] = {"title": " ".join(e.find("a:title", ns).text.split()), "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)],
                 "year": int(e.find("a:published", ns).text[:4])}
for k, aid in ARXIV.items():
    out[k] = {"arxiv": aid, "verified": aid in byid, **byid.get(aid, {})}
    print(k, out[k]["verified"], out[k].get("year"), out[k].get("title", "")[:90], flush=True)
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "verified_refs.json", "w"), indent=1)
