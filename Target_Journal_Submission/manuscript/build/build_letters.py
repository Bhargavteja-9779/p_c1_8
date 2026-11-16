#!/usr/bin/env python3
"""Generate the cover letter (DOCX) and highlights (DOCX) for Analytica Chimica Acta.

Highlights: Elsevier requires 3-5 bullet points of at most 85 characters (including spaces).
All quantitative statements are taken from results/numbers.json via context_builder.
"""
import json
import os
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Cm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from context_builder import build_context  # noqa: E402


def _doc():
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(12)
    for s in d.sections:
        s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.5)
    return d


def highlights(lines, path):
    for l in lines:
        if len(l) > 85:
            raise ValueError(f"highlight too long ({len(l)} chars): {l}")
    d = _doc()
    d.add_heading("Highlights", level=1)
    for l in lines:
        d.add_paragraph(l, style="List Bullet")
    d.save(path)


def cover_letter(paragraphs, title, path):
    d = _doc()
    for t in ("[Corresponding author name]", "[Department, Institution]", "[Address]", "[E-mail]", "", "[Date]", ""):
        d.add_paragraph(t)
    d.add_paragraph("The Editors\nAnalytica Chimica Acta")
    d.add_paragraph("")
    d.add_paragraph("Dear Editors,")
    p = d.add_paragraph(); p.add_run("We submit the manuscript entitled ").italic = False
    r = p.add_run(f"“{title}”"); r.italic = True
    p.add_run(" for consideration as a Research Paper in Analytica Chimica Acta.")
    for para in paragraphs:
        d.add_paragraph(para).paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    d.add_paragraph("Yours sincerely,")
    d.add_paragraph("[Corresponding author name], on behalf of all authors")
    d.save(path)


def main():
    import content
    res = os.environ.get("MS_RES", os.path.join(ROOT, "results")); tab = os.environ.get("MS_TAB", os.path.join(ROOT, "tables"))
    out = os.environ.get("MS_OUT", os.path.join(ROOT, "manuscript"))
    numbers = json.load(open(os.path.join(res, "numbers.json")))
    ctx = build_context(numbers, res, tab)
    highlights(content.highlight_lines(ctx), os.path.join(out, "Highlights.docx"))
    cover_letter(content.cover_letter_paragraphs(ctx), content.TITLE, os.path.join(out, "cover_letter.docx"))
    import subprocess
    for f in ("cover_letter.docx", "Highlights.docx"):
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", out, os.path.join(out, f)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("letters built")


if __name__ == "__main__":
    main()
