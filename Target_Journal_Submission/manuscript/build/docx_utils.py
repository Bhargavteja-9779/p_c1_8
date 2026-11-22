import os
"""python-docx post-processing for the journal manuscript."""
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm


def _suppress_ln(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    if pPr.find(qn("w:suppressLineNumbers")) is None:
        pPr.append(OxmlElement("w:suppressLineNumbers"))


def _add_page_number(section):
    section.footer.is_linked_to_previous = False
    p = section.footer.paragraphs[0] if section.footer.paragraphs else section.footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _suppress_ln(p)
    run = p.add_run()
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), tag); run._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = text; run._r.append(it)


def _line_numbers(section):
    sp = section._sectPr
    ln = sp.find(qn("w:lnNumType"))
    if ln is None:
        ln = OxmlElement("w:lnNumType"); sp.append(ln)
    ln.set(qn("w:countBy"), "1"); ln.set(qn("w:restart"), "continuous"); ln.set(qn("w:distance"), "283")


def _three_rule_table(tbl):
    """Elsevier-style table: top, header-bottom and bottom rules only; 9-pt single-spaced text."""
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge, val in (("top", "single"), ("bottom", "single"), ("left", "nil"), ("right", "nil"),
                      ("insideH", "nil"), ("insideV", "nil")):
        e = OxmlElement(f"w:{edge}"); e.set(qn("w:val"), val); e.set(qn("w:sz"), "6"); e.set(qn("w:color"), "000000")
        borders.append(e)
    old = tblPr.find(qn("w:tblBorders"))
    if old is not None:
        tblPr.remove(old)
    tblPr.append(borders)
    for i, row in enumerate(tbl.rows):
        for cell in row.cells:
            if i == 0:
                tcPr = cell._tc.get_or_add_tcPr()
                b = OxmlElement("w:tcBorders"); bt = OxmlElement("w:bottom")
                bt.set(qn("w:val"), "single"); bt.set(qn("w:sz"), "6"); bt.set(qn("w:color"), "000000")
                b.append(bt); tcPr.append(b)
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
                for r in p.runs:
                    r.font.size = Pt(8.5); r.font.name = "Times New Roman"
                    if i == 0:
                        r.font.bold = True


def _number_equations(d):
    """Place each display equation (m:oMathPara) in a borderless two-cell table with a right-aligned number."""
    M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
    body = d.element.body
    k = 0
    for p in list(body.iterchildren(qn("w:p"))):
        if p.find(".//" + M + "oMathPara") is None:
            continue
        k += 1
        tbl = d.add_table(rows=1, cols=2)
        tblPr = tbl._tbl.tblPr
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "bottom", "left", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{edge}"); e.set(qn("w:val"), "nil"); borders.append(e)
        tblPr.append(borders)
        tbl.columns[0].width = Cm(14.5); tbl.columns[1].width = Cm(1.5)
        c0, c1 = tbl.rows[0].cells
        c0.width = Cm(14.5); c1.width = Cm(1.5)
        p.addprevious(tbl._tbl)                     # move the table to the equation's position
        c0._tc.remove(c0._tc.find(qn("w:p")))
        c0._tc.append(p)                            # move the equation paragraph into the left cell
        num = c1.paragraphs[0]; num.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = num.add_run(f"({k})"); r.font.name = "Times New Roman"; r.font.size = Pt(12)
        for cell in (c0, c1):
            tcPr = cell._tc.get_or_add_tcPr()
            va = OxmlElement("w:vAlign"); va.set(qn("w:val"), "center"); tcPr.append(va)
            for pp in cell.paragraphs:
                _suppress_ln(pp)
    return k


def _explicit_delimiters(d):
    """OMML <m:d> delimiters default to parentheses in Word, but LibreOffice renders missing begChr/endChr
    as bars; make every default delimiter explicit so both renderers show parentheses."""
    M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
    n = 0
    for dd in d.element.body.iter("{%s}d" % M):
        dPr = dd.find("{%s}dPr" % M)
        if dPr is None:
            dPr = OxmlElement("m:dPr"); dd.insert(0, dPr)
        for tag, ch in (("begChr", "("), ("endChr", ")")):
            if dPr.find("{%s}%s" % (M, tag)) is None:
                e = OxmlElement(f"m:{tag}"); e.set("{%s}val" % M, ch); dPr.insert(0, e); n += 1
    return n


def set_metadata(d, title=""):
    """Neutral document properties (author = corresponding author; no tool names)."""
    cp = d.core_properties
    cp.author = "P N Bhargav Teja"; cp.last_modified_by = "P N Bhargav Teja"
    cp.comments = ""; cp.title = title; cp.keywords = ""; cp.subject = ""


def postprocess(docx_path, max_img_cm=16.0):
    d = Document(docx_path)
    set_metadata(d, os.path.splitext(os.path.basename(docx_path))[0].replace("_", " "))
    _explicit_delimiters(d)
    n_eq = _number_equations(d)
    for s in d.sections:
        s.page_height = Cm(29.7); s.page_width = Cm(21.0)
        s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.5)
        _line_numbers(s); _add_page_number(s)
    for t in d.tables:
        if t._tbl.find(".//{http://schemas.openxmlformats.org/officeDocument/2006/math}oMathPara") is not None:
            continue          # equation tables stay borderless
        _three_rule_table(t)
        nrow = len(t.rows)
        for ri, row in enumerate(t.rows):
            for cell in row.cells:
                for p in cell.paragraphs:
                    _suppress_ln(p)
        for row in t.rows:                                   # rows never break across pages
            trPr = row._tr.get_or_add_trPr()
            if trPr.find(qn("w:cantSplit")) is None:
                trPr.append(OxmlElement("w:cantSplit"))
    for shape in d.inline_shapes:
        if shape.width > Cm(max_img_cm):
            ratio = Cm(max_img_cm) / shape.width
            shape.width = Cm(max_img_cm); shape.height = int(shape.height * ratio)
    # keep table captions with their tables and figure images with their captions
    for p in d.paragraphs:
        if p.text.startswith("Table ") or p.style.name in ("Captioned Figure", "Figure"):
            p.paragraph_format.keep_with_next = True
    d.save(docx_path)
