"""Manuscript content for Analytica Chimica Acta: front matter, results/discussion, closing, letters.

All numbers are placeholders {{key}} resolved from context_builder.build_context (machine-generated results).
"""
import os

import pandas as pd

from context_builder import build_context
import docx_utils

TITLE = ("Random-matrix theory of multivariate calibration learning curves: what a small pilot set can and cannot predict")
SHORT_TITLE = "Forecasting calibration learning curves"
KEYWORDS = ["Multivariate calibration", "Sample-size planning", "Learning curve", "Near-infrared spectroscopy",
            "Ridge regression", "Random-matrix theory"]


def context(numbers, RES, TAB):
    return build_context(numbers, RES, TAB)


def front_matter(ctx):
    from results_text import ABSTRACT_BACKGROUND, ABSTRACT_RESULTS, ABSTRACT_SIGNIFICANCE
    lines = [f"# {TITLE}", "",
             "[Author 1]^a^, [Author 2]^a,\\*^", "",
             "^a^ [Department, Institution, City, Country]", "",
             "\\* Corresponding author: [name, e-mail]", "",
             "## Abstract", "",
             f"**Background:** {ABSTRACT_BACKGROUND}", "",
             f"**Results:** {ABSTRACT_RESULTS}", "",
             f"**Significance:** {ABSTRACT_SIGNIFICANCE}", "",
             "**Keywords:** " + "; ".join(KEYWORDS), ""]
    return "\n".join(lines)


def results_discussion(ctx, TAB, FIG, table_md):
    from results_text import results_markdown
    return results_markdown(ctx, TAB, FIG, table_md)


def closing(ctx):
    from results_text import LIMITATIONS, CONCLUSION
    text = LIMITATIONS + "\n\n" + open(os.path.join(os.path.dirname(__file__), "closing.md")).read()
    return text.replace("{{conclusion_text}}", CONCLUSION)


def postprocess_docx(path):
    docx_utils.postprocess(path)


def highlight_lines(ctx):
    from results_text import HIGHLIGHTS
    return [h.replace("{{", "{").replace("}}", "}").format(**ctx) if "{" in h else h for h in HIGHLIGHTS]


def cover_letter_paragraphs(ctx):
    from results_text import COVER_LETTER
    import re
    return [re.sub(r"\{\{([^}]+)\}\}", lambda m: ctx[m.group(1).strip()], p) for p in COVER_LETTER]
