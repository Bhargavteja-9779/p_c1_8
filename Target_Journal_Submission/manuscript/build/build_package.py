#!/usr/bin/env python3
"""Assemble the Analytica Chimica Acta submission package (one folder + zip) from the built documents.

Run after build_manuscript.py, build_supplementary.py and build_letters.py.
Output: Target_Journal_Submission/submission_package/ACA_Submission/ and ACA_Submission.zip
"""
import datetime
import os
import shutil
import subprocess
import sys
import zipfile

from docx import Document
from docx.shared import Pt, Cm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MS = os.path.join(ROOT, "manuscript")
OUTROOT = os.path.join(ROOT, "submission_package")
PKG = os.path.join(OUTROOT, "ACA_Submission")
sys.path.insert(0, HERE)
from content import TITLE, KEYWORDS  # noqa: E402
from docx_utils import set_metadata  # noqa: E402

AUTHOR = "P N Bhargav Teja"
AFFIL = "[Department, Institution, City, Country]"


def _doc():
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(12)
    for s in d.sections:
        s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.5)
    return d


def save(d, name, title):
    set_metadata(d, title)
    p = os.path.join(PKG, name)
    d.save(p)
    return p


def title_page():
    d = _doc()
    d.add_heading("Title page", level=1)
    p = d.add_paragraph(); r = p.add_run(TITLE); r.bold = True; r.font.size = Pt(14)
    d.add_paragraph("Short title: Observability limit for calibration learning curves")
    d.add_paragraph("Article type: Research Paper")
    d.add_heading("Authors", level=2)
    d.add_paragraph(f"{AUTHOR} a,*")
    d.add_paragraph("[Second author] b")
    d.add_paragraph(f"a {AFFIL}")
    d.add_paragraph(f"b {AFFIL}")
    d.add_paragraph(f"* Corresponding author: {AUTHOR}, {AFFIL}. E-mail: [e-mail]. ORCID: [ORCID, optional]")
    d.add_heading("Keywords", level=2)
    d.add_paragraph("; ".join(KEYWORDS))
    d.add_heading("Funding", level=2)
    d.add_paragraph("This research did not receive any specific grant from funding agencies in the public, commercial, or "
                    "not-for-profit sectors.")
    d.add_heading("Declaration of competing interest", level=2)
    d.add_paragraph("The authors declare that they have no known competing financial interests or personal relationships that "
                    "could have appeared to influence the work reported in this paper.")
    return save(d, "04_Title_Page.docx", "Title page")


def competing_interest():
    d = _doc()
    d.add_heading("Declaration of interests", level=1)
    d.add_paragraph(f"Manuscript title: {TITLE}")
    d.add_paragraph("☒ The authors declare that they have no known competing financial interests or personal relationships "
                    "that could have appeared to influence the work reported in this paper.")
    d.add_paragraph("☐ The authors declare the following financial interests/personal relationships which may be considered as "
                    "potential competing interests: none.")
    d.add_paragraph("")
    d.add_paragraph(f"Corresponding author: {AUTHOR}")
    d.add_paragraph("Date: " + datetime.date.today().strftime("%d %B %Y"))
    return save(d, "09_Declaration_of_Competing_Interest.docx", "Declaration of interests")


def ai_declaration():
    closing = open(os.path.join(HERE, "closing.md")).read()
    txt = [l for l in closing.split("\n") if l.startswith("During the preparation")][0]
    d = _doc()
    d.add_heading("Declaration of generative AI and AI-assisted technologies in the writing process", level=1)
    d.add_paragraph(f"Manuscript title: {TITLE}")
    d.add_paragraph(txt)
    d.add_paragraph("The same statement appears in the manuscript, before the reference list.")
    return save(d, "10_Declaration_of_Generative_AI_Use.docx", "Declaration of generative AI use")


def suggested_reviewers():
    revs = [
        ("Alejandro C. Olivieri", "Universidad Nacional de Rosario / IQUIR (CONICET), Argentina",
         "Multivariate calibration figures of merit and practical calibration guidance (cited as ref. 52)."),
        ("Federico Marini", "Sapienza University of Rome, Italy",
         "Validation of chemometric models (cited as ref. 2)."),
        ("Liliana Forzani", "Universidad Nacional del Litoral / CONICET, Argentina",
         "Statistical theory of PLS prediction in high dimensions (refs. 29, 50)."),
        ("Thomas Bocklitz", "Leibniz Institute of Photonic Technology and Friedrich Schiller University Jena, Germany",
         "Sample-size planning and learning curves for spectroscopic data (refs. 8, 26)."),
        ("José Manuel Amigo", "University of the Basque Country / Ikerbasque, Spain",
         "Validation strategies and overfitting in chemometric models (ref. 45)."),
    ]
    d = _doc()
    d.add_heading("Suggested reviewers", level=1)
    d.add_paragraph(f"Manuscript title: {TITLE}")
    d.add_paragraph("The following experts have no collaboration or conflict of interest with the authors. Institutional "
                    "affiliations and e-mail addresses must be checked on the institutions' current web pages before they "
                    "are entered in the submission system.")
    t = d.add_table(rows=1, cols=4); t.style = "Table Grid"
    for c, h in zip(t.rows[0].cells, ["Name", "Affiliation (verify)", "E-mail (to be added)", "Expertise relevant to this work"]):
        c.text = h
    for n, a, e in revs:
        r = t.add_row().cells
        r[0].text, r[1].text, r[2].text, r[3].text = n, a, "[verify]", e
    return save(d, "11_Suggested_Reviewers.docx", "Suggested reviewers")


def figures():
    fd = os.path.join(PKG, "06_Figures"); os.makedirs(fd, exist_ok=True)
    src = os.path.join(MS, "figures_submission")
    for i in range(1, 8):
        shutil.copy(os.path.join(src, f"Figure_{i}.pdf"), fd)
        subprocess.run(["pdftoppm", "-r", "600", "-singlefile", "-tiff", "-tiffcompression", "lzw",
                        os.path.join(src, f"Figure_{i}.pdf"), os.path.join(fd, f"Figure_{i}")], check=True)
    ga = os.path.join(PKG, "03_Graphical_Abstract"); os.makedirs(ga, exist_ok=True)
    shutil.copy(os.path.join(MS, "Graphical_Abstract.pdf"), ga)
    shutil.copy(os.path.join(MS, "Graphical_Abstract.png"), ga)
    subprocess.run(["pdftoppm", "-r", "300", "-singlefile", "-tiff", "-tiffcompression", "lzw",
                    os.path.join(MS, "Graphical_Abstract.pdf"), os.path.join(ga, "Graphical_Abstract")], check=True)


def main():
    shutil.rmtree(PKG, ignore_errors=True); os.makedirs(PKG)
    cp = [("cover_letter.docx", "01_Cover_Letter.docx"), ("cover_letter.pdf", "01_Cover_Letter.pdf"),
          ("Highlights.docx", "02_Highlights.docx"),
          ("Final_Manuscript.docx", "05_Manuscript.docx"), ("Final_Manuscript.pdf", "05_Manuscript_reference.pdf")]
    for s, t in cp:
        shutil.copy(os.path.join(MS, s), os.path.join(PKG, t))
    shutil.copy(os.path.join(ROOT, "supplementary", "Supplementary_Material.docx"), os.path.join(PKG, "08_Supplementary_Material.docx"))
    shutil.copy(os.path.join(ROOT, "supplementary", "Supplementary_Material.pdf"), os.path.join(PKG, "08_Supplementary_Material.pdf"))
    figures()
    title_page(); competing_interest(); ai_declaration(); suggested_reviewers()
    for f in ("04_Title_Page.docx", "09_Declaration_of_Competing_Interest.docx", "10_Declaration_of_Generative_AI_Use.docx",
              "11_Suggested_Reviewers.docx"):
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", PKG, os.path.join(PKG, f)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.copy(os.path.join(HERE, "SUBMISSION_GUIDE.txt"), os.path.join(PKG, "00_SUBMISSION_GUIDE.txt"))
    z = os.path.join(OUTROOT, "ACA_Submission.zip")
    if os.path.exists(z):
        os.remove(z)
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for dp, _, fs in os.walk(PKG):
            for f in sorted(fs):
                p = os.path.join(dp, f)
                zf.write(p, os.path.relpath(p, OUTROOT))
    print("package:", z)


if __name__ == "__main__":
    main()
