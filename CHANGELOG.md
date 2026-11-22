# CHANGELOG

_Created 2026-11-15._

## 2026-11-21/22
- Novelty upgrade: Proposition 1 (observability horizon), compatible set, information fraction, B-RPM (pre-specified, HB1-HB4).
- Full v2 pipeline re-run on re-downloaded data; analysis-stage fixes (split-0 truth, ratio>=2 endpoints, provenance sources).
- Robustness stage fixed (baselines were missing) and extended with B-RPM; simulation with B-RPM.
- Staged-decision analysis; per-task absolute bias; within-n0 information fraction.
- Manuscript rebuilt (new Results/Discussion, abstract, highlights, cover letter, graphical abstract); 14 verified references added.

## 2026-11-22 (final pre-submission checks)
- Reference list: author-name style unified (initials), published proceedings versions added for arXiv preprints,
  corrected entries (Frank, Savitzky, Loureiro, Wilcoxon pages, Riley volume, Vander Heyden).
- Theory: Proposition 2 set as its own paragraph; max/min over the finite model set; punctuation of Eq. (6).
- Text: circular cross-reference (Sections 4.4/4.6) and duplicated parentheses removed; cover letter hypothesis count
  aligned with abstract (four of five); AI-use declaration aligned with the Elsevier template.
- Supplementary notes and code comments: internal process references removed; leakage-audit "verified by" column neutral.
- Document properties set to the corresponding author; internal review material removed from the submission folder.
- PDF rendering: equations require LibreOffice Math (apt-get install libreoffice-math); superscript asterisks use U+2217.
- New: manuscript/build/build_package.py -> submission_package/ACA_Submission.zip (all files for Editorial Manager).
