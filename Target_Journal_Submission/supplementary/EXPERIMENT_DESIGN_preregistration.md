# Pre-registered experimental design (written before the main experiments were run)

_Frozen: 2026-11-15, before executing `run_all.py --mode full`. Any later deviation is logged in `EXPERIMENT_LOG.md` with its reason._

## Disclosure of exploratory work
Before this design was frozen, exploratory feasibility runs were made on **ICRAF-ISRIC VisNIR** (properties OC, clay, pH, CEC, sand, exchangeable Ca; pilot sizes 50 and 100). They led to two design choices: (i) fitting the theory to the pilot's cross-validation path rather than by marginal likelihood; (ii) fixing the alignment exponent at r = 1 by default. Because these choices were informed by ICRAF-VisNIR, the primary analysis is **repeated excluding the four ICRAF-VisNIR tasks** (sensitivity analysis S0). Marginal likelihood and free r remain in the ablation.

## Hypothesis
H. For linear multivariate calibration of spectroscopic data, the expected test error after calibrating with n samples is governed by the eigen-spectrum of the spectral covariance and by how the analyte signal is distributed across it. Consequently, (a) a deterministic-equivalent (random-matrix) risk model reproduces empirical learning curves, and (b) fitting that model to a small pilot's cross-validation path along the ridge penalty grid (regularisation-path matching, RPM), with the eigen-spectrum estimated from inexpensive unlabelled spectra, forecasts future calibration error more accurately than empirical learning-curve extrapolation.

## Research questions and the experiment answering each
| RQ | Question | Experiment |
|---|---|---|
| RQ1 | Does the deterministic-equivalent risk reproduce empirical ridge and PLS learning curves on real spectra? | E1: large-sample reference fit + κ-collapse test |
| RQ2 | Does RPM forecast the test RMSE at larger n more accurately than learning-curve extrapolation and simple rules? | E2 (main) + E3 (baselines) |
| RQ3 | Are RPM's uncertainty bands calibrated, and does RPM support better sample-size decisions? | E4 (coverage) + E5 (decisions) |
| RQ4 | Which components of RPM matter? | E6 (ablation) |
| RQ5 | Is RPM robust to pre-processing, model family, pilot design, distribution shift and spectral domain? | E7 (robustness / generalisation), E8 (sensitivity), E9 (error analysis), E10 (efficiency) |

## Data (38 tasks, all public)
Soil (Open Soil Spectral Library v1.3): ICRAF-ISRIC VisNIR and MIR, KSSL MIR and VisNIR (capped at 15 000 samples by whole sites), Neospectra handheld NIR (2 106 multi-scanner-averaged spectra), AfSIS-1 MIR — properties OC (log1p), clay, pH(H2O), CEC (log1p) where available (23 tasks). Fruit: mango dry matter (4 021 fruits, Felix F750, 684–990 nm). Fuel: SWRI diesel (6 properties). Pharmaceutical: IDRC-2002 tablets (assay). Meat: Tecator (fat, moisture, protein). Designed mixtures: CGL (casein, glucose, lactate, moisture). LUCAS and the Serbian OSSL subset are excluded (restrictive licences).

## Leakage controls
- Replicate scans of the same physical sample are averaged **before** splitting (mango: two cheeks per fruit, fruit identity reconstructed from metadata + exact DM value and verified by spectral distance; KSSL VisNIR: duplicate layer scans; Neospectra: multi-scanner average).
- Soil layers from the same site/profile are kept together: the test split is **group-disjoint** (site id or coordinates), and all cross-validation inside pilots and inside truth fits is **leave-one-group-out** (closed form) or grouped K-fold.
- Pre-processing is sample-wise (SNV; absorbance conversion), so it cannot leak across samples.
- Unlabelled spectra used by RPM come from the **pool only** (never from the test set).

## Protocol
- **Split:** per task, a fixed group-disjoint test set (25 % of samples, ≤ 3 000) and a pool; seed derived from the task name (SHA-256).
- **Ground truth:** expected test MSE of (a) ridge with penalty chosen by exact LOGO over a 53-point grid and (b) PLS1 with 1–30 latent variables chosen by grouped 10-fold CV, trained on n random pool samples, n ∈ {50, 100, 200, 400, 800, 1600, 3200, 6400} (≤ pool size); repetitions 30 (n ≤ 400), 16 (n ≤ 1600), 8 (larger).
- **Pilots:** n0 ∈ {25, 50, 100, 200}; 20 random pilots per (task, n0) with predefined seeds; horizons n ∈ grid with n ≥ 2 n0.
- **Primary endpoint:** absolute forecast error |log(RMSE_forecast / RMSE_truth)| against the ridge truth, averaged over pilots and horizons within each task; secondary: the same against PLS truth; bias (signed error); share within ±10 % and ±20 %.
- **Methods:** RPM (proposed; r = 1; LOGO path; validity cut-off df2/n ≤ 0.8; Bayesian bootstrap B = 50). Baselines: inverse power law with asymptote (IPL3; Mukherjee et al. 2003; Figueroa et al. 2012; Ali et al. 2018), pure power law (IPL2), exponential saturation (EXP3), logarithmic (LOG2) — fitted to a within-pilot sub-sampling learning curve (fractions 0.25–0.85, 20 splits each, plus the full-pilot CV point); FLAT (pilot CV error, i.e. no improvement); DF-OLS (fixed-complexity classical formula).
- **Uncertainty (E4):** empirical coverage of 80 % and 95 % bands (RPM: bootstrap quantiles; curve fits: delta method).
- **Decisions (E5):** for target RMSE values defined by the truth curve at n* ∈ {4 n0, 16 n0}, error of the forecast sample size required (|log2(n̂/n*)|); failure if a method never reaches the target.
- **Ablation (E6, n0 ∈ {50, 100}, 10 pilots):** free r; marginal likelihood instead of path matching; pilot-only covariance; pilot-only covariance with power-law tail; 250 unlabelled spectra; extra unlabelled library spectra (AfSIS-1); 10-fold instead of exact LOGO path; validity cut-offs 0.5 and 0.95.
- **Robustness (E7):** (a) PLS truth; (b) pre-processing variants (raw absorbance; Savitzky–Golay first derivative) on a representative subset; (c) Kennard–Stone-selected pilots; (d) shift: mango pilots + pool from seasons 1–3 forecasting a season-4 test set (and population-grouped split); (e) results by family and spectral region; (f) added reference noise.

## Statistical analysis
- Unit of analysis = task (pilots and horizons averaged within task), giving paired observations across tasks.
- Two-sided Wilcoxon signed-rank tests of RPM vs each baseline, Holm correction across baselines (family-wise α = 0.05); effect size = median paired difference with 95 % bootstrap CI (10 000 resamples of tasks) and matched-pairs rank-biserial correlation.
- Stratified summaries by n0, extrapolation ratio and family. No seeds are selected after seeing results; all pilots are reported.
