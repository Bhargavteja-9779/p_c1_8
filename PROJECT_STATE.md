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

## 4. Next steps
1. Write journal_selection/*.md (selected, comparison, verification).
2. Literature matrix + novelty map + hypothesis/RQs + pre-registered experimental design (EXPERIMENT_DESIGN.md).
3. Data download scripts (OSSL libraries, mango DMC, Tecator, …), leakage audit, implementation, run_all.py quick/full.

## 5. Exact next execution step
See bottom of this file (updated continuously).
