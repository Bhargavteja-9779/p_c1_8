"""python-docx post-processing for the journal manuscript."""
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm


def _add_page_number(section):
    p = section.footer.paragraphs[0] if section.footer.paragraphs else section.footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
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


def postprocess(docx_path, max_img_cm=16.0):
    d = Document(docx_path)
    for s in d.sections:
        s.page_height = Cm(29.7); s.page_width = Cm(21.0)
        s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.5)
        _line_numbers(s); _add_page_number(s)
    for t in d.tables:
        _three_rule_table(t)
    for shape in d.inline_shapes:
        if shape.width > Cm(max_img_cm):
            ratio = Cm(max_img_cm) / shape.width
            shape.width = Cm(max_img_cm); shape.height = int(shape.height * ratio)
    # keep table captions with their tables and figure images with their captions
    for p in d.paragraphs:
        if p.text.startswith("Table ") or p.style.name in ("Captioned Figure", "Figure"):
            p.paragraph_format.keep_with_next = True
    d.save(docx_path)
