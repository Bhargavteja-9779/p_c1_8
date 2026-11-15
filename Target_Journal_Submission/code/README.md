# How many reference samples does a spectroscopic calibration need?
### Code for: *Forecasting multivariate-calibration learning curves from small pilot sets by regularisation-path matching*

This repository reproduces every number, table and figure of the manuscript from public data.
All computations run on a CPU (no GPU is needed); hardware is detected and logged automatically.

## 1. Installation
```bash
conda env create -f environment.yml && conda activate rpm-learning-curves
# or
pip install -r requirements.txt
```
Tested with Python 3.13 on Linux x86_64 (4 cores, 15 GB RAM).

## 2. Data (public; ≈1.4 GB)
```bash
python scripts/download_data.py            # -> ../../data_raw (path set in config/*.yaml)
```
| Source | Content | Licence |
|---|---|---|
| Open Soil Spectral Library v1.3 (Safanelli et al., PLOS ONE 2025) | ICRAF-ISRIC VisNIR & MIR, KSSL MIR & VisNIR, AfSIS-1 MIR, Neospectra handheld NIR | CC-BY 4.0 (AfSIS-1: ODbL) |
| Mango DMC and NIR spectra (Mendeley Data doi:10.17632/46htwnp833) | 4 021 fruits, Felix F750 | CC BY 4.0 |
| Eigenvector Research data archive | SWRI diesel NIR; IDRC 2002 tablets; CGL mixtures | public research archive |
| OpenML data id 505 | Tecator meat NIR | public (StatLib) |

LUCAS and the Serbian OSSL subset are **not** used (restrictive licences). A SHA-256 manifest of the downloaded files is written to `data_raw/SHA256SUMS.txt`.

## 3. Reproduce the study
```bash
python run_all.py --mode quick     # pipeline check: 3 tasks, few pilots (~5 min); outputs in ../results_quick
python run_all.py --mode full      # complete study (38 tasks): several CPU-hours on 4 cores
```
Stages can be run separately and are resumable (finished tasks are skipped):
```bash
python run_all.py --mode full --stage main         # ground truth + pilot forecasts (E1–E6)
python run_all.py --mode full --stage simulation   # E0 controlled simulation (Monte-Carlo truth)
python run_all.py --mode full --stage refinement   # RPM-w (weighted path fit) on identical pilots
python run_all.py --mode full --stage robustness   # E7 robustness / shift experiments
python run_all.py --mode full --stage analysis     # statistics, tables, figures, numbers.json
```
Outputs (relative to the submission root): `results/raw/` (per-task truth `*.npz`, per-pilot forecasts `*.csv`),
`results/raw_results.csv`, `results/metrics.json`, `results/statistics.json`, `results/numbers.json`,
`tables/` (CSV + Markdown + LaTeX), `figures/` (PNG + PDF), `results/experiment_logs/`.
**All manuscript numbers are read from `results/numbers.json` and `tables/*.csv`.**

## 4. Tests
```bash
pytest -q tests/
```
Covers: exact closed-form LOO/LOGO ridge CV (with weights and groups) vs brute force; PLS1 vs scikit-learn;
the κ fixed point; deterministic-equivalent risk vs Monte-Carlo ridge on Gaussian data; group-disjoint splits;
sample-wise pre-processing; RPM consistency on synthetic data; curve-fit baselines.

## 5. Method in brief (see `src/models/theory.py`, `src/models/forecasters.py`)
1. Eigen-spectrum λ_k of the (pre-processed) spectral covariance from unlabelled spectra.
2. Exact leave-one-group-out MSE e(μ) of ridge on the labelled pilot along a 53-point penalty grid.
3. Each μ maps to an effective regularisation κ(n₀, μ); the pilot thus observes the bias function
   N(κ) = σ² + τ² Σ_k (λ_k/λ_1)(κ/(λ_k+κ))² on κ ≥ κ_min(n₀).
4. Fit (τ², σ²) to the path in log space (RPM-w: inverse-variance weighted).
5. Forecast RMSE(n) = sqrt(min_μ (1+1/n) N(κ(n,μ)) / (1 − df₂(κ)/n)); Bayesian-bootstrap bands.

## 6. Structure
```
config/            full.yaml, quick.yaml (all experimental settings)
src/data/          dataset loaders (replicate averaging, leakage-control groups)
src/preprocessing/ sample-wise SNV / Savitzky–Golay
src/models/        theory.py (deterministic equivalents), ridge.py (exact LOGO ridge, PLS1), forecasters.py (RPM + baselines)
src/training/      ground-truth learning curves, group-disjoint splits
src/evaluation/    forecasting experiment engine
src/statistics/    Wilcoxon + Holm, bootstrap CIs, rank-biserial
experiments/       simulation (E0), refinement (RPM-w), robustness (E7), analysis + figures
scripts/           data download
tests/             unit tests
```

## 7. Determinism
All random draws use seeds derived from task names (SHA-256) and pilot indices; BLAS is pinned to one thread per worker.
Re-running produces identical results on the same platform.
