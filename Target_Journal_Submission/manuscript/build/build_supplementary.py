#!/usr/bin/env python3
"""Compile the Supplementary Material (DOCX + PDF) from machine-generated tables and figures."""
import os
import subprocess

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TAB = os.environ.get("MS_TAB", os.path.join(ROOT, "tables"))
FIG = os.environ.get("MS_FIG", os.path.join(ROOT, "figures"))
SUP_SRC = os.path.join(ROOT, "supplementary")
SUP = os.environ.get("MS_OUT", SUP_SRC)

import sys
sys.path.insert(0, HERE)
from supp_index import TABLES, FIGS, NOTES  # noqa: E402  (single source of numbering)


def md_table(df, maxrows=60):
    def f(v):
        if isinstance(v, float):
            return "–" if pd.isna(v) else (f"{v:.3g}" if abs(v) < 1e-3 and v != 0 else f"{v:.3f}")
        return str(v)
    df = df.head(maxrows)
    cols = [str(c).replace("_", " ") for c in df.columns]
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    out += ["| " + " | ".join(f(v) for v in r) + " |" for r in df.itertuples(index=False)]
    return "\n".join(out)


def main():
    from content import TITLE
    parts = ["# Supplementary Material", "", f"**{TITLE}**", "",
             "All tables and figures below are generated automatically by `run_all.py` from the per-pilot raw results.", ""]
    for i, (name, cap) in enumerate(TABLES, 1):
        p = os.path.join(TAB, name + ".csv")
        if not os.path.exists(p):
            raise FileNotFoundError(p)          # numbering must never shift silently
        parts += [f"**Table S{i}.** {cap}", "", md_table(pd.read_csv(p)), ""]
    for i, (name, cap) in enumerate(FIGS, 1):
        p = os.path.join(FIG, name + ".png")
        if not os.path.exists(p):
            raise FileNotFoundError(p)
        parts += [f"![**Figure S{i}.** {cap}]({p}){{width=15cm}}", ""]
    for i, (fn, title) in enumerate(NOTES, 1):
        p = os.path.join(SUP_SRC, fn)
        txt = open(p).read().split("\n", 1)[-1]
        parts += [f"# Supplementary Note {i}: {title}", "", txt, ""]
    md = os.path.join(HERE, "supplementary_full.md")
    open(md, "w").write("\n".join(parts))
    out = os.path.join(SUP, "Supplementary_Material.docx")
    subprocess.run(["pandoc", md, "-o", out, "--reference-doc", os.path.join(HERE, "reference_aca.docx")], check=True)
    import docx_utils
    docx_utils.postprocess(out)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", SUP, out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("supplementary built:", out)


if __name__ == "__main__":
    main()
