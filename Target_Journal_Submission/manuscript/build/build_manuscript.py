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
RES = os.environ.get("MS_RES", os.path.join(ROOT, "results"))
TAB = os.environ.get("MS_TAB", os.path.join(ROOT, "tables"))
FIG = os.environ.get("MS_FIG", os.path.join(ROOT, "figures"))
OUT = os.environ.get("MS_OUT", os.path.join(ROOT, "manuscript"))


def load_numbers():
    return json.load(open(os.path.join(RES, "numbers.json")))


USED = {}

SOURCES = [("tv_", "tables/T9_theory_validity_full_pool_fit.csv"), ("collapse_", "tables/T9b_kappa_collapse_dispersion.csv"),
           ("r_", "results/alignment_exponents.csv"), ("n_r_below", "results/alignment_exponents.csv"),
           ("mae_", "tables/T2_main_accuracy_ridge_truth.csv"), ("medae_", "tables/T2_main_accuracy_ridge_truth.csv"),
           ("bias_", "tables/T2_main_accuracy_ridge_truth.csv"), ("w20_", "tables/T2_main_accuracy_ridge_truth.csv"),
           ("w10_", "tables/T2_main_accuracy_ridge_truth.csv"), ("st_", "tables/T3_stats_rpm_vs_baselines.csv"),
           ("pls_", "tables/T4_main_accuracy_pls_truth.csv"), ("covw", "tables/T5_interval_coverage.csv"),
           ("cov", "tables/T5_interval_coverage.csv"), ("decfail_", "tables/T6_sample_size_decisions.csv"),
           ("dec_", "tables/T6_sample_size_decisions.csv"), ("ablT_", "tables/T7b_ablation_eigenspectrum_rpmT.csv"),
           ("abl_", "tables/T7_ablation.csv"), ("gain", "tables/T14_posthoc_gain_and_decision.csv"),
           ("gdec_", "tables/T14_posthoc_gain_and_decision.csv"), ("gst_", "tables/T14b_posthoc_gain_stats.csv"),
           ("sim", "tables/T0b_simulation_by_n0.csv"), ("rob", "tables/T8_robustness.csv"),
           ("s0_", "tables/S0_stats_excluding_ICRAF_VisNIR.csv"), ("t_", "tables/T10_runtime.csv"),
           ("n_tasks", "tables/T1_tasks.csv"), ("n_soil", "tables/T1_tasks.csv"), ("n_pilots_total", "results/numbers.json"),
           ("n_forecasts", "results/numbers.json"), ("abstract_", "composed from T2/T3/T5/alignment (see text)")]


def source_of_key(key):
    for pre, src in SOURCES:
        if key.startswith(pre):
            return src
    return "results/numbers.json"


def fill(text, ctx):
    def rep(m):
        key = m.group(1).strip()
        if key not in ctx:
            if os.environ.get("MS_ALLOW_MISSING") == "1":   # pipeline tests only; final builds fail hard
                return f"[MISSING:{key}]"
            raise KeyError(f"placeholder {key} missing")
        USED[key] = str(ctx[key])
        return str(ctx[key])
    return re.sub(r"\{\{([^}]+)\}\}", rep, text)


def write_provenance(path):
    lines = ["# Claim–evidence map (automatic part): every number placeholder used in the manuscript", "",
             "| Placeholder | Value in manuscript | Machine-generated source |", "|---|---|---|"]
    for k in sorted(USED):
        lines.append(f"| `{k}` | {USED[k]} | `{source_of_key(k)}` |")
    open(path, "w").write("\n".join(lines) + "\n")


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
    cells = [[f(v) for v in r] for r in d.itertuples(index=False)]
    head = "| " + " | ".join(str(c) for c in d.columns) + " |"
    def numeric(i):
        vals = [r[i].replace("%", "").replace(",", "").replace("–", "").replace("+", "").replace("−", "").replace("<", "").strip() for r in cells]
        ok = 0
        for v in vals:
            try:
                float(v.split()[0]); ok += 1
            except (ValueError, IndexError):
                pass
        return ok >= 0.8 * max(len(vals), 1)
    num = [numeric(i) for i in range(len(d.columns))]
    # numeric cells must not wrap: non-breaking spaces and word joiners around dashes / slashes
    for r in cells:
        for i in range(len(r)):
            if num[i] or len(r[i]) <= 12:
                r[i] = (r[i].replace(" ", "\u00a0").replace("–", "\u2060–\u2060").replace("/", "\u2060/\u2060"))
    def vis(s):
        return len(s.replace("\u2060", ""))
    # column widths (in characters): numeric cells never wrap; text columns shrink towards their longest
    # unbreakable token only as far as needed to fit the text width (16 cm at 8.5 pt ~ 0.15 cm per character)
    ncol = len(d.columns)
    cap = (16.0 - 0.38 * ncol) / 0.15
    hard, soft = [], []
    for i, c in enumerate(d.columns):
        hw = 1.15 * max((len(w) for w in str(c).split()), default=1)          # bold header word
        toks = [max((vis(t) for t in r[i].split(" ")), default=1) for r in cells]
        full = [vis(r[i]) for r in cells]
        hard.append(max(toks + [hw]) + 1.5)
        soft.append(max(full + [hw]) + 1.5)
    widths = list(soft)
    excess = sum(widths) - cap
    if excess > 0:
        shrink = [(s - h) if not num[i] else 0.0 for i, (s, h) in enumerate(zip(soft, hard))]
        tot = sum(shrink)
        if tot > 0:
            widths = [s - min(excess, tot) * k / tot for s, k in zip(soft, shrink)]
    dashes = [max(3, int(round(3 * w))) for w in widths]
    sep = "|" + "|".join(("-" * (n - 1) + ":") if (i > 0 and num[i]) else (":" + "-" * (n - 1)) for i, n in enumerate(dashes)) + "|"
    rows = ["| " + " | ".join(r) + " |" for r in cells]
    return f"\n**{label}.** {caption}\n\n" + "\n".join([head, sep] + rows) + "\n"


def main():
    sys.path.insert(0, HERE)
    import content  # noqa: E402  (results-dependent text and tables)
    numbers = load_numbers()
    refs = json.load(open(os.path.join(ROOT, "manuscript", "refs", "verified_refs.json")))
    ctx = content.context(numbers, RES, TAB)
    front = content.front_matter(ctx)
    parts = [open(os.path.join(HERE, "part1_intro_theory_methods.md")).read().replace("FIGDIR", FIG),
             content.results_discussion(ctx, TAB, FIG, table_md),
             content.closing(ctx)]
    body = fill("\n\n".join(parts), ctx)
    body, order = number_citations(body, refs)
    reflist = "\n\n".join(f"[{i + 1}] {format_reference(refs[k])}" for i, k in enumerate(order))
    front = fill(front, ctx)
    import supp_index
    md = supp_index.resolve(front + "\n\n" + body + "\n\n# References\n\n" + reflist + "\n")
    md_path = os.path.join(HERE, "manuscript_full.md")
    open(md_path, "w").write(md)
    json.dump({"citation_order": order}, open(os.path.join(HERE, "citation_order.json"), "w"), indent=1)
    docx_path = os.path.join(OUT, "Final_Manuscript.docx")
    subprocess.run(["pandoc", md_path, "-f", "markdown+tex_math_dollars+pipe_tables+implicit_figures",
                    "-o", docx_path, "--reference-doc", os.path.join(HERE, "reference_aca.docx"),
                    "--resource-path", ROOT], check=True)
    content.postprocess_docx(docx_path)
    os.makedirs(os.path.join(ROOT, "REVIEW"), exist_ok=True)
    write_provenance(os.path.join(ROOT, "REVIEW", "claim_evidence_map_numbers.md"))
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", OUT, docx_path], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("built", docx_path, "and PDF;", len(order), "references")


if __name__ == "__main__":
    main()
