"""Manuscript content for Analytica Chimica Acta: front matter, results/discussion, closing, letters.

All numbers are placeholders {{key}} resolved from context_builder.build_context (machine-generated results).
"""
import os

import pandas as pd

from context_builder import build_context
import docx_utils

TITLE = ("What can a pilot set tell about a calibration learning curve? An observability limit for sample-size planning in spectroscopy")
SHORT_TITLE = "Forecasting calibration learning curves"
KEYWORDS = ["Multivariate calibration", "Sample-size planning", "Learning curve", "Identifiability", "Bayesian forecasting",
            "Near-infrared spectroscopy"]


def context(numbers, RES, TAB):
    ctx = build_context(numbers, RES, TAB)
    from results_v3 import bayes_context
    ctx.update(bayes_context(os.path.abspath(os.path.join(TAB, ".."))))
    ctx["title"] = TITLE
    return ctx


def front_matter(ctx):
    from results_v3 import ABSTRACT_BACKGROUND, ABSTRACT_RESULTS, ABSTRACT_SIGNIFICANCE
    lines = [f"# {TITLE}", "",
             "P N Bhargav Teja^a,\\*^, [Second author]^b^", "",
             "^a^ [Department, Institution, City, Country]", "", "^b^ [Department, Institution, City, Country]", "",
             "\\* Corresponding author: P N Bhargav Teja, [e-mail]", "",
             "## Abstract", "",
             f"**Background:** {ABSTRACT_BACKGROUND}", "",
             f"**Results:** {ABSTRACT_RESULTS}", "",
             f"**Significance:** {ABSTRACT_SIGNIFICANCE}", "",
             "**Keywords:** " + "; ".join(KEYWORDS), ""]
    return "\n".join(lines)


def results_discussion(ctx, TAB, FIG, table_md):
    from results_text import results_markdown
    from results_v3 import results_markdown_v3
    return results_markdown_v3(ctx, TAB, FIG, table_md, results_markdown(ctx, TAB, FIG, table_md))


def closing(ctx):
    from results_v3 import LIMITATIONS, CONCLUSION
    text = LIMITATIONS + "\n\n" + open(os.path.join(os.path.dirname(__file__), "closing.md")).read()
    return text.replace("{{conclusion_text}}", CONCLUSION)


def postprocess_docx(path):
    docx_utils.postprocess(path)


def highlight_lines(ctx):
    from results_v3 import HIGHLIGHTS
    return [h.replace("{{", "{").replace("}}", "}").format(**ctx) if "{" in h else h for h in HIGHLIGHTS]


def cover_letter_paragraphs(ctx):
    from results_v3 import COVER_LETTER
    import re
    return [re.sub(r"\{\{([^}]+)\}\}", lambda m: ctx[m.group(1).strip()], p) for p in COVER_LETTER]
