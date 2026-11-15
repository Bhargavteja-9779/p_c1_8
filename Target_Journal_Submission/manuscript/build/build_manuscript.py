#!/usr/bin/env python3
"""Build the Analytica Chimica Acta submission manuscript (DOCX + PDF) from machine-generated results.

* Text parts (Markdown + LaTeX math) contain {{placeholders}} filled from results/numbers.json.
* Citations [@key] are numbered in order of first appearance (Elsevier numbered style) and the
  reference list is generated from manuscript/refs/verified_refs.json (Crossref/DataCite/arXiv-verified).
* Tables are rendered from tables/*.csv; figures from figures/*.png.
* pandoc converts LaTeX math to native (editable) Word equations; python-docx adds line numbers,
  page numbers and table styling; LibreOffice converts to PDF.
"""
import json
import os
import re
import subprocess
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RES, TAB, FIG = os.path.join(ROOT, "results"), os.path.join(ROOT, "tables"), os.path.join(ROOT, "figures")
OUT = os.path.join(ROOT, "manuscript")


def load_numbers():
    return json.load(open(os.path.join(RES, "numbers.json")))


def fill(text, ctx):
    def rep(m):
        key = m.group(1).strip()
        if key not in ctx:
            raise KeyError(f"placeholder {key} missing")
        return str(ctx[key])
    return re.sub(r"\{\{([^}]+)\}\}", rep, text)


def format_reference(r):
    def authors(lst):
        out = []
        for a in lst[:6]:
            if "," in a:
                fam, giv = [s.strip() for s in a.split(",", 1)]
                ini = " ".join(p[0] + "." for p in re.split(r"[\s\-]+", giv) if p)
                out.append(f"{ini} {fam}".strip())
            else:
                out.append(a)
        s = ", ".join(out)
        return s + (", et al." if len(lst) > 6 else "")
    if "arxiv" in r:
        return f"{authors(r['authors'])}, {r['title']}, arXiv:{r['arxiv']} ({r['year']})."
    vol = f" {r['volume']}" if r.get("volume") else ""
    pages = f" {r['pages']}" if r.get("pages") else ""
    jt = r.get("journal") or r.get("publisher") or ""
    if r.get("type") == "dataset":
        return f"{authors(r['authors'])}, {r['title']}, {jt} ({r['year']}). https://doi.org/{r['doi']}."
    return f"{authors(r['authors'])}, {r['title']}, {jt}{vol} ({r['year']}){(',' + pages) if pages else ''}. https://doi.org/{r['doi']}."


def number_citations(text, refs):
    order = []
    def rep(m):
        keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
        nums = []
        for k in keys:
            if k not in refs:
                raise KeyError(f"unverified/unknown citation key {k}")
            if k not in order:
                order.append(k)
            nums.append(order.index(k) + 1)
        nums = sorted(set(nums))
        # compress ranges
        parts, i = [], 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            parts.append(f"{nums[i]}–{nums[j]}" if j - i >= 2 else ",".join(str(x) for x in nums[i:j + 1]))
            i = j + 1
        return "[" + ",".join(parts) + "]"
    text = re.sub(r"\[(@[^\]]+)\]", rep, text)
    return text, order


def table_md(df, caption, label, floatfmt=3, cols=None, rename=None):
    d = df.copy()
    if cols:
        d = d[cols]
    if rename:
        d = d.rename(columns=rename)
    def f(v):
        if isinstance(v, float):
            if pd.isna(v):
                return "–"
            if abs(v) >= 1000:
                return f"{v:,.0f}"
            return f"{v:.{floatfmt}f}"
        return str(v)
    head = "| " + " | ".join(d.columns) + " |"
    sep = "|" + "|".join([":--" if i == 0 else "--:" for i in range(len(d.columns))]) + "|"
    rows = ["| " + " | ".join(f(v) for v in r) + " |" for r in d.itertuples(index=False)]
    return f"\n**{label}.** {caption}\n\n" + "\n".join([head, sep] + rows) + "\n"


def main():
    sys.path.insert(0, HERE)
    import content  # noqa: E402  (results-dependent text and tables)
    numbers = load_numbers()
    refs = json.load(open(os.path.join(OUT, "refs", "verified_refs.json")))
    ctx = content.context(numbers, RES, TAB)
    front = content.front_matter(ctx)
    parts = [open(os.path.join(HERE, "part1_intro_theory_methods.md")).read(),
             content.results_discussion(ctx, TAB, FIG, table_md),
             content.closing(ctx)]
    body = fill("\n\n".join(parts), ctx)
    body, order = number_citations(body, refs)
    reflist = "\n\n".join(f"[{i + 1}] {format_reference(refs[k])}" for i, k in enumerate(order))
    md = front + "\n\n" + body + "\n\n# References\n\n" + reflist + "\n"
    md_path = os.path.join(HERE, "manuscript_full.md")
    open(md_path, "w").write(md)
    json.dump({"citation_order": order}, open(os.path.join(HERE, "citation_order.json"), "w"), indent=1)
    docx_path = os.path.join(OUT, "Final_Manuscript.docx")
    subprocess.run(["pandoc", md_path, "-f", "markdown+tex_math_dollars+pipe_tables+implicit_figures",
                    "-o", docx_path, "--reference-doc", os.path.join(HERE, "reference_aca.docx"),
                    "--resource-path", ROOT], check=True)
    content.postprocess_docx(docx_path)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", OUT, docx_path], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("built", docx_path, "and PDF;", len(order), "references")


if __name__ == "__main__":
    main()
