# PROJECT_STATE.md — persistent research checkpoint

_Last updated: 2026-11-15 (session 1)_

## 1. Target journal (Phase 0) — SELECTED
**Analytica Chimica Acta (ACA)**, Elsevier. ISSN 0003-2670 (print) / 1873-4324 (online).
- JCR 2026 release (2025 JIF): **6.1**; 5-yr IF 5.8 (Elsevier shop page). Category: Chemistry, Analytical (SCIE) — **Q1, rank 23/110** (ablesci relay of JCR 2026; bioxbio confirms 6.1).
- Empirical submission→acceptance (PubMed history dates, research articles entering PubMed 2025-07-01…2026-10-31): median 61 d (n=300 sample; IQR 45–85; 49% ≤60 d; 90% ≤100 d). Larger n=1000 re-run in `Target_Journal_Submission/journal_selection/data/final3_acceptance_times_n1000.json`.
- Official ScienceDirect "Journal insights" panel could not be fetched (HTTP 403); ablesci relays "平均5.9周 (Elsevier website)" review cycle — unverified label.
- Scope: fundamental new methodological developments incl. chemometric techniques and data treatment; discourages routine application papers.
- Format: structured abstract (Background/Results/Significance) used by recent research papers; highlights; graphical abstract; ~5 keywords.

## 2. Topic (Phases 1–5) — SELECTED after stress test
**Forecasting multivariate-calibration learning curves from small pilot sets for sample-size planning in spectroscopy.**
Method: *regularization-path matching (RPM)* — fit a deterministic-equivalent (random-matrix) risk model of ridge regression to the pilot set's leave-one-out error along the regularization path, using the eigen-spectrum of (cheap) unlabeled spectra; extrapolate the identifiable bias function N(kappa) to forecast test RMSE at any future calibration size n; bootstrap bands.
- ABANDONED direction (prior art): conformal / interval calibration of NIR models under season/instrument/region shift — already published (Talanta 2026, doi:10.1016/j.talanta.2026.130941) and SSRN 2026 preprints (aggregated ICP for NIR). Also avoided toxicology/hazard topics.
- Closest prior art: Ali et al. 2018 Anal Chem (doi:10.1021/acs.analchem.8b02167) — empirical IPL learning-curve sample-size planning (Raman classification); ML theory (Bordelon 2020; Canatar 2021 Nat Commun; Jacot 2020 KARE; Wei-Hu-Steinhardt 2022; Spigler 2020; Atanasov 2024) — risk at current n / omniscient explanations, not pilot-based forecasting.

## 3. Feasibility evidence (scratch, not manuscript results)
ICRAF-ISRIC VisNIR soils, 6 properties: omniscient theory within ~±10% MSE of empirical ridge curves up to n≈800. Pilot forecasting MAE|log RMSE ratio| (n=200–1600): RPM(r=1) 0.161 / 0.125 vs IPL 0.376 / 0.222 vs flat 0.175 / 0.135 (n0=50 / 100). To be re-run properly in the pipeline.

## 3b. Implementation status (session 1)
- Code: Target_Journal_Submission/code (src/, experiments/, tests/ [16 tests pass], run_all.py quick/full, config/*.yaml).
- Data: data_raw/ (gitignored; `code/scripts/download_data.py` re-downloads with SHA256SUMS). 38 tasks load.
- Pre-registration frozen: supplementary/EXPERIMENT_DESIGN_preregistration.md; leakage audit: supplementary/DATA_LEAKAGE_AUDIT.md;
  literature matrix/novelty map: supplementary/LITERATURE_MATRIX_AND_NOVELTY_MAP.md; references verified: manuscript/refs/verified_refs.json (48/48).
- RUNNING: `python run_all.py --mode full --stage main --jobs 4` (started 19:13 UTC 2026-11-15); outputs results/raw/truth_*.npz, forecasts_main_*.csv (resumable: finished tasks are skipped on restart).
- - Simulation finding (pre-main-analysis): at n0=60, p=80 synthetic, unweighted RPM is optimistic (pilot LOO skew near interpolation). Implemented inverse-variance-weighted path fit (RPMForecaster(weighted=True)); default unchanged. To evaluate in E0 simulation + as documented refinement on all tasks (forecast-only rerun).

## 4. Next steps
1. Write journal_selection/*.md (selected, comparison, verification).
2. Literature matrix + novelty map + hypothesis/RQs + pre-registered experimental design (EXPERIMENT_DESIGN.md).
3. Data download scripts (OSSL libraries, mango DMC, Tecator, …), leakage audit, implementation, run_all.py quick/full.

## 5. Exact next execution step (updated 2026-11-19)
Status: all experiment stages DONE; manuscript, supplementary, highlights, cover letter built (manuscript/build/*.py);
journal historical-paper analysis written (journal_selection/journal_paper_analysis.md).
Internal audit of version 1 completed.
Candidate verified ACA references to add if reviewers ask for positioning (Crossref-checked 2026-11-16):
 Olivieri 2026 ACA 1396:345155; Holman & Kurouski 2026 ACA 1414:345655; Lopez et al. 2026 ACA 1384:344838;
 Riu et al. 2026 ACA 1419:345885; Al-Shaebi et al. 2026 ACA 1423:346185; Fan et al. 2025 ACA 1379:344728.


## 6. Session 3 (2026-11-21) — NOVELTY UPGRADE (user: avoid desk rejection; check recent ACA papers)
Diagnosis: v1 headline "theory-based forecaster no better than FLAT" = weak novelty (novelty scan
`journal_selection/recent_aca_novelty_scan_2026-11.md`). New contribution set:
 1. **Proposition 1 (observability horizon / non-identifiability of the gain)** + identification-set corollary —
    `manuscript/build/theory_observability.md` (to be merged into Section 2).
 2. **B-RPM** (Bayesian path matching with transferred structural prior on r, eta) — `code/src/models/bayes_rpm.py`,
    stage `bayes` (`experiments/bayes.py`), pre-specified in `supplementary/BRPM_preregistration_addendum.md` (HB1–HB4)
    before any v2 result was inspected. Evaluation: `python3 -m experiments.bayes_analysis` (from code/) -> results/bayes_numbers.json, tables/TB*.
 3. Must-cite / baselines from scan: Ali 2018; Konstantinidis et al. arXiv 2510.01210 (Riley-type minimum n for
    chemometric regression); Beleites 2013 ACA; Breure 2025 Geoderma; Wei-Hu-Steinhardt 2022; Dicker 2014; Janson 2017.
Run order (session 3): main (running, started 20:57 UTC) -> refinement -> bayes -> simulation -> ablation_t -> robustness -> analysis
 -> bayes_analysis -> rewrite manuscript around Prop. 1 + B-RPM (title/abstract/highlights/cover letter) -> rebuild -> commit/push.
Commands: cd Target_Journal_Submission/code && nohup python3 run_all.py --mode full --stage <stage> --jobs 4 &  (stages resumable)

## 7. Status at 2026-11-22 ~02:30 UTC (session 3)
DONE: v2 pipeline (all stages) + B-RPM + rebuilt manuscript/supplement/letters/GA.
Key honest results: compatible set covers 91% pointwise / 86% whole-curve; FLAT best on level (0.262 vs B-RPM 0.282);
B-RPM best on gain vs FLAT/RPM/IPL3; cross-family robust vs transferred slope (soil only); HB1-HB3 failed, HB4 met pointwise;
staged second batch +4-10 points decision accuracy for all methods.
NEXT (optional polish): trim main text to ~7000 words (Sections 4.1-4.2 and Methods); re-run editor desk screen;
author/declaration placeholders must be filled by the user.
Rebuild: cd Target_Journal_Submission/code && python3 run_all.py --mode full --stage analysis (runs bayes_analysis + figures);
         cd ../manuscript/build && python3 build_manuscript.py && python3 build_supplementary.py && python3 build_letters.py

## 8. Status at end of session 3 (2026-11-22)
Editor re-screen after cycle-2 fixes: desk-reject probability 0.38 (from 0.45); all of its "no new data" items addressed afterwards
(unsupported gain-vs-power-law claim removed, soil scope of transfer stated, pre-specified wording, new title/highlights,
staged-cost caveat, compatible-set naming, supplement cleanup, hidden-signal illustration Fig 6a/TB11). Main text ~7,050 words.
Remaining for the USER: author names/affiliations, CRediT, funding, AI-use statement confirmation, code deposit (DOI) on acceptance.
Known limitations that need new data: multi-source non-soil families for a real cross-family test; full-resolution spectra.
Deliverables: manuscript/Final_Manuscript.{docx,pdf}, manuscript/figures_submission/Figure_1..8, manuscript/Graphical_Abstract.png,
manuscript/Highlights.*, manuscript/cover_letter.*, supplementary/Supplementary_Material.*.

## 9. Session 4 (2026-11-22) — "go wild" strengthening; RESUME HERE
User instructions: first author P N Bhargav Teja, second author placeholder; no funding; no competing interests; code
"available on request"; maximise novelty; real-world framing allowed. (Author/declaration edits DONE in content.py/closing.md.)
DONE this session:
 - Campaign-planning case study: code/experiments/campaign.py -> tables/TB12_campaign_planning.csv, TB12b_campaign_tests.csv;
   figure Fig9_campaign_planning (fig_campaign in experiments/figures_bayes.py). KEY RESULT: with priors from OTHER application
   families, decision-calibrated B-RPM delivers 72%/88% success at requested 80%/90% vs 28%/40% for slope planning
   (+45 points, 23/24 tasks, p<0.001); point forecasters only differ in implicit risk attitude.
 - 6-task full-resolution run (experiments/fullres.py -> results/fullres_summary.csv, results/raw/fullres): B-RPM 0.249 vs
   FLAT 0.287, RPM 0.333, IPL3 0.463; hidden-signal shares larger at native resolution.
 - Pre-spec addendum 2 committed (supplementary/FULLRES_preregistration_addendum.md, hypothesis HC1 on 32 held-out tasks).
RUNNING / TO RESUME:
 1. Native-resolution confirmation study: cd Target_Journal_Submission/code && RPM_FULLRES=1 nohup python3 -m experiments.fullres_all 4 &
    (resumable; outputs results/fullres_all/raw/{truth_*,forecasts_rob_fullall_*}.csv). Check: ps aux | grep fullres_all
 2. Then write analysis for HC1: B-RPM vs FLAT/RPM/IPL3/SLOPE-T (SLOPE-T from full-res truth slopes, LOSO) on the 32 tasks
    excluding KSSL-MIR:OC, ICRAF-MIR:clay, KSSL-VisNIR:clay, Neospectra-NIR:pH, Diesel:bp50, Tablets:assay; Wilcoxon + source level.
    Report honestly whichever way it goes; if confirmed, make native resolution the headline accuracy result.
 3. Manuscript: add Section "Real-world case study: planning a calibration campaign" (TB12, Fig 9; cite conformal risk control,
    Angelopoulos et al. arXiv 2208.02814 — verify), native-resolution results section + table, related-work capability table
    (Ali 2018, Figueroa 2012, Beleites 2013, Riley 2020/Konstantinidis 2025, Wei 2022, Adriaensen 2023, this work);
    update abstract/highlights/cover letter/GA; add TB12/TB12b/fullres tables to supp_index; rebuild all; commit/push.
 4. Optional: external datasets (nothing found).

## 10. Status 2026-11-22 ~12:30 UTC (session 4 continued)
DONE: native-resolution study (38 tasks; HC1 NOT confirmed, reported; other results replicate) -> TC1-TC5, Section 4.8;
campaign case study in manuscript (4.7, Fig 7); Table 3 related-work capability matrix; Proposition 2 (minimax bound);
fresh-editor fixes (equations, glyphs, claims, figure count 7, abstract 238 words, body ~7.8k words).
Fresh editor (cycle 3) estimate before fixes: desk-reject 0.55 -> ~0.40 with fixes; re-screen of v5 requested.
REMAINING for user: second author name, affiliations, e-mail. Code: "available on request" (user choice).

## 11. FINAL (2026-11-22, pre-submission)
Submission package: Target_Journal_Submission/submission_package/ACA_Submission.zip (rebuild: cd manuscript/build &&
python3 build_manuscript.py && python3 build_supplementary.py && python3 build_letters.py && python3 build_package.py).
Requires: pip install -r code/requirements.txt; apt-get install libreoffice-math (else equations vanish from PDFs).
Internal review material removed from the branch (kept in git history). Remaining for the USER: second author, affiliations,
e-mail, reviewer e-mails.
