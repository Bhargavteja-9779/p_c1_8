# Selected target journal

| Field | Value (with evidence source) |
|---|---|
| **TARGET JOURNAL** | **Analytica Chimica Acta** (ACA) |
| **PUBLISHER** | Elsevier B.V. (established publisher; journal founded 1947) |
| **ISSN** | 0003-2670 (print), 1873-4324 (online) |
| **JCR STATUS** | Indexed in Science Citation Index Expanded (SCIE) — JCR 2026 release (17 June 2026), relayed by ablesci.com |
| **JCR QUARTILE** | **Q1** — Chemistry, Analytical, rank 23/110 (JCR 2026 release, via ablesci.com relay of Clarivate data) |
| **JOURNAL IMPACT FACTOR** | **6.1** (2025 JIF, JCR 2026 release). Confirmed on the publisher page (shop.elsevier.com: "Impact factor 6.1; 5-year impact factor 5.8") and by bioxbio.com ("2025 (2026 update) 6.1") |
| **JCR SUBJECT CATEGORY** | Chemistry, Analytical |
| **VERIFIED REVIEW / DECISION TIMELINE** | Official ScienceDirect "Journal insights" panel could **not** be fetched (HTTP 403 to automated clients). A third-party relay (ablesci) quotes an Elsevier-reported average review cycle of "5.9 weeks" — label not independently verifiable, so **first-decision time is treated as UNVERIFIED**. |
| **VERIFIED ACCEPTANCE TIMELINE** | **Empirically verified from PubMed history dates** (received → accepted) of research articles that entered PubMed 2025-07-01…2026-10-31: **median 62 days** (IQR 46–84; n = 999); 48.9 % accepted ≤ 60 days, **87.2 % ≤ 100 days**. Topic-matched subset (chemometrics / PLS / multivariate calibration / machine learning research papers, reviews and tutorials excluded): **median 73 days** (IQR 51–97; n = 118); 35.6 % ≤ 60 days; 77.1 % ≤ 100 days. |
| **APC** | Hybrid journal: **no APC for the subscription route**. The open-access APC could not be verified on an accessible official page (publisher pages returned 403); it must be checked on the Elsevier APC price list at submission if OA is chosen. A sister fully-OA title (*Analytica Chimica Acta: X*) exists. |
| **SCOPE FIT** | Strong. Official aims & scope (Elsevier shop page and listings reproducing it): "An International Journal Devoted to All Branches of Analytical Chemistry"; emphasises **fundamental new methodological developments**, explicitly including **chemometric techniques and data treatment**; discourages routine application papers; welcomes tutorials on chemometric methods. |
| **RESEARCH FIT** | The project is a general chemometric methodology (sample-size planning / learning-curve forecasting for multivariate calibration), validated on many public spectroscopic data sets — the type of "fundamental methodological development" ACA prioritises. ACA published ≥ 19 method-focused chemometrics papers (validation strategies, calibration transfer, local modelling, label noise, MCR theory, tutorials) between mid-2025 and late-2026 (`data/aca_chemometrics_subset.json`). |
| **KEY AUTHOR GUIDELINES** | Research papers: structured abstract (*Background / Results / Significance*, observed in recent ACA research papers in PubMed; median ≈ 220 words), highlights (Elsevier standard: 3–5 bullets, ≤ 85 characters each), graphical abstract, ≈ 5 keywords, numbered sections, Elsevier reference style, data-availability statement, CRediT author statement, declaration of competing interest, declaration of generative-AI use in writing (Elsevier policy). Authors are encouraged to suggest reviewers. The full Guide for Authors could not be fetched (403); formatting therefore follows the Elsevier generic research-article template plus the conventions observed in recent ACA papers. |
| **KEY REJECTION RISKS** | (1) Desk rejection as "insufficiently analytical / too statistical" — mitigated by framing around an analytical problem (how many reference analyses are needed) and validating on spectroscopic calibrations from several analytical domains. (2) Reviewer demand for PLS (not only ridge) — addressed by evaluating forecasts against PLS learning curves. (3) Perception of incremental novelty relative to Ali et al. (2018, *Anal. Chem.*) — addressed by direct comparison with the inverse-power-law approach. (4) Limited non-soil data — addressed by including fruit, fuel, pharmaceutical and meat data sets. |

## Fallback
**Talanta** (Elsevier; 2025 JIF 6.7; Q1 Chemistry, Analytical; empirical median sub→accept 69 d overall, 68.5 d for the chemometrics subset; 79.8 % ≤ 100 d). Talanta has the higher JIF and a marginally faster chemometrics-subset timeline, but its recent chemometrics output is dominated by sensor/assay applications (≈ 6 % method-focused titles vs ≈ 15 % in ACA), so ACA was judged the better scientific fit for a pure-methodology paper. See `journal_comparison.md`.

## Integrity checks
- Elsevier is an established, non-predatory publisher; ACA is SCIE-indexed with a 79-year history.
- No hijacked-journal risk: the ISSNs above match PubMed (NLM) and the publisher page.
- No acceptance-rate figure is reported here because none could be verified (a user-reported "75 %" on ablesci was discarded as anecdotal).
