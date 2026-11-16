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

## 5. Exact next execution step (updated 2026-11-16 14:57 UTC)
Status: main stage DONE (38 tasks). Pre-registered result: RPM (r=1) >> IPL3/IPL2/EXP3/LOG2/DF-OLS (Holm p<1e-4), ≈ FLAT (n.s.).
Key findings: theory reproduces curves (mean |log err| 0.10), kappa-collapse SD 0.041 vs 0.52; alignment exponent r<1 in 38/38 tasks
(median ~0.55; Vis/NIR ~0.37, MIR ~0.62). RPM-T (transferred r) FAILS (noise-floor collapse) -> negative result, reported.
RUNNING: /tmp/claude-0/chain.sh (refinement -> simulation -> robustness -> analysis), then /tmp/claude-0/chain2.sh (ablation_t -> analysis).
If interrupted: cd Target_Journal_Submission/code && for st in refinement simulation ablation_t robustness analysis; do python3 run_all.py --mode full --stage $st --jobs 4; done
(all stages resumable; finished tasks skipped).
THEN:
1. Check pending claims in manuscript/build/results_text.py against tables (robustness, simulation, error analysis wording).
2. Write abstract results/significance, highlights, conclusion, cover letter (results_text.py), build: python3 manuscript/build/build_manuscript.py; build_letters.py; build_supplementary.py.
3. Review cycle 1: 10 background Agent reviewers using scratchpad/reviewer_brief.md -> REVIEW/raw/cycle_01/*.json; verify serious issues; fix; REVIEW/review_01.md.
4. Repeat cycles 2-10; final audits; package; decision.
