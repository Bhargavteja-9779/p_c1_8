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
- Scheduled self-resume check-ins: trig_01UadKHaQ7fhw2Mq5R6Usdou (2026-11-16 00:12Z), trig_01DBuXvLvVmt7GeYNbbDyGEA (05:22Z).
- Simulation finding (pre-main-analysis): at n0=60, p=80 synthetic, unweighted RPM is optimistic (pilot LOO skew near interpolation). Implemented inverse-variance-weighted path fit (RPMForecaster(weighted=True)); default unchanged. To evaluate in E0 simulation + as documented refinement on all tasks (forecast-only rerun).

## 4. Next steps
1. Write journal_selection/*.md (selected, comparison, verification).
2. Literature matrix + novelty map + hypothesis/RQs + pre-registered experimental design (EXPERIMENT_DESIGN.md).
3. Data download scripts (OSSL libraries, mango DMC, Tecator, …), leakage audit, implementation, run_all.py quick/full.

## 5. Exact next execution step (updated 2026-11-19)
Status: all experiment stages DONE; manuscript, supplementary, highlights, cover letter built (manuscript/build/*.py);
journal historical-paper analysis written (journal_selection/journal_paper_analysis.md).
Review cycle 1 IN PROGRESS: 10 reviewer agents (briefs: Target_Journal_Submission/REVIEW/raw/cycle_01/briefs/R1..R10.md)
write REVIEW/raw/cycle_01/R*.json. (First attempt was interrupted by the API usage limit on 2026-11-16; resumed 2026-11-19.)
Next, per cycle k = 01..10:
 1. Verify every FATAL/CRITICAL/MAJOR issue against code/results; record verdict + response in REVIEW/raw/cycle_k/decisions.json.
 2. Fix research (code/analysis/experiments) first, then text; rerun affected stages:
    cd Target_Journal_Submission/code && python3 run_all.py --mode full --stage <stage> --jobs 4   (analysis stage ~30 s)
 3. Rebuild: cd ../manuscript/build && python3 build_manuscript.py && python3 build_supplementary.py && python3 build_letters.py
 4. python3 ../../REVIEW/tools/consolidate.py k  -> REVIEW/review_k.md; update REVIEW_HISTORY.md, CHANGELOG.md; commit + push.
 5. Next cycle: new briefs with prior-issue list (REVIEW/review_*.md) so reviewers do not repeat fixed issues.
Candidate verified ACA references to add if reviewers ask for positioning (Crossref-checked 2026-11-16):
 Olivieri 2026 ACA 1396:345155; Holman & Kurouski 2026 ACA 1414:345655; Lopez et al. 2026 ACA 1384:344838;
 Riu et al. 2026 ACA 1419:345885; Al-Shaebi et al. 2026 ACA 1423:346185; Fan et al. 2025 ACA 1379:344728.
After cycle 10: Phases 34-42 (consistency + reproducibility audits incl. quick-mode rerun, final DOCX/PDF, package manifest,
REVIEW/final_audit.md, rejection-risk report, READY/NOT READY decision).


## 6. Session 3 (2026-11-21) — NOVELTY UPGRADE (user: avoid desk rejection; check recent ACA papers)
Diagnosis: v1 headline "theory-based forecaster no better than FLAT" = desk-reject risk (R9, novelty scan
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
Self-resume: send_later check-ins trig_01FerzTSvpTtyk1mRNXyPzG1 (01:56Z), trig_01AdNmGQopf3B1SayMSXe9L2 (07:56Z); add more as needed.
