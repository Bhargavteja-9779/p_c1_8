# Analytica Chimica Acta — historical paper analysis and comparison with its strongest related papers

_Prepared 2026-11-16. Source corpus: `data/aca_chemometrics_subset.json` (129 ACA research/tutorial articles indexed in PubMed 2025–2026 whose titles/abstracts match chemometrics / multivariate-calibration / spectroscopic machine-learning terms; retrieved with `scripts/pubmed_journal_corpus.py`). The 26 papers below are every **method-, benchmark-, tutorial- or critique-type** paper in that subset (sensor/assay papers that merely apply machine learning were excluded). Counts are read from the published abstracts only (full texts were not accessed), so "not stated" means "not stated in the abstract"._

## 1. Papers analysed (n = 26)

| # | Year | DOI | Type | Data sets (abstract) | Simulated data | Baselines / comparison | Formal statistics in abstract | Relevance to this work |
|---|---|---|---|---|---|---|---|---|
| 2 | 2026 | 10.1016/j.aca.2026.346321 | Method comparison (PCA/ASCA/vASCA) | 1 (serum Raman, rats) | no | 3 methods | ANOVA-based | low |
| 10 | 2026 | 10.1016/j.aca.2026.346227 | Concept/critique (label noise) | 3 case studies | no | — | no | reference-value quality |
| 16 | 2026 | 10.1016/j.aca.2026.346185 | Benchmark (data partitioning, SERS) | 1 (15 000 spectra, 15 isolates) | no | 12 partitions × 5 models × 3 FS | no | **leakage / group splits** |
| 23 | 2026 | 10.1016/j.aca.2026.346104 | New method (unsupervised calibration transfer) | 3 | no | representative CT methods | no | low |
| 30 | 2026 | 10.1016/j.aca.2026.345989 | New tools (MCR complexity/outliers) | 1 simulated + 3 public (corn, wine, marzipan) | yes | — | no | low |
| 37 | 2026 | 10.1016/j.aca.2026.345885 | New index (replicates via error covariance) | portable-NIR data sets (number not stated) | no | — | no | **planning of measurement effort** |
| 41 | 2026 | 10.1016/j.aca.2026.345813 | Benchmark (pre-processing pipelines, AIMS) | 1 model system | no | 10 × 3 × 3 pipelines | no | low |
| 46 | 2026 | 10.1016/j.aca.2026.345655 | Tutorial/benchmark (resampling for PLS-DA) | **12** | no | resampling schemes | Bayesian Bradley–Terry | **validation / CV bias** |
| 48 | 2026 | 10.1016/j.aca.2026.345682 | New framework (liblex, local models) | 1 cross-continental soil case | no | LOCAL, Cubist, PLS, CNN | no | soil spectral libraries |
| 51 | 2026 | 10.1016/j.aca.2026.345651 | New method (evolutionary subset selection) | 1 cross-continental soil case | no | LOCAL, Cubist, PLS, CNN | no | soil spectral libraries |
| 54 | 2026 | 10.1016/j.aca.2026.345578 | New model (1D-CNN, LIBS) | 1 (1019 + 150 external) | no | ML baselines | no | low |
| 64 | 2026 | 10.1016/j.aca.2026.345242 | Tutorial (local PLS; R/Julia code) | examples | no | — | no | code availability practice |
| 65 | 2026 | 10.1016/j.aca.2026.345387 | Comparison (calibration transfer, sensors) | 1 experimental system | no | 4 methods | no | low |
| 69 | 2026 | 10.1016/j.aca.2026.345258 | New method (VIP stability, bootstrap/permutation) | metabolomics data (number not stated) | no | — | resampling-based | bootstrap practice |
| 70 | 2026 | 10.1016/j.aca.2026.345155 | Tutorial/critique (multivariate calibration advice) | 1 public (fruit dry matter, Vis–NIR) | no | literature shallow/deep models vs PLS | **statistical comparison of RMSEP; reference uncertainty** | **same mango data; reference-error floor** |
| 75 | 2026 | 10.1016/j.aca.2026.345159 | Systematic study (data order, sample size) | simulated + 1 experimental | yes | PLS-DA, N-PLS-DA, PARAFAC-DA | no | sample-size effects |
| 76 | 2026 | 10.1016/j.aca.2025.345050 | New DL framework | 1 benchmark | no | ML methods | no | low |
| 88 | 2026 | 10.1016/j.aca.2025.344838 | Tutorial (validation, overfitting) | — | — | — | — | **validation / leakage** |
| 95 | 2026 | 10.1016/j.aca.2025.344889 | New method (tree-based SIMCA) | 6 (5 omics + wine) | no | SIMCA, OC-SVM, IF | no | low |
| 106 | 2025 | 10.1016/j.aca.2025.344728 | New method (low-data NIR calibration) | **5 data sets, 21 responses, 10 spectrometers** | no | benchmark methods | no | **small-sample calibration** |
| 108 | 2025 | 10.1016/j.aca.2025.344658 | Discussion (robustness Raman vs NIR) | 2 case studies | no | — | no | season shift (fruit) |
| 110 | 2025 | 10.1016/j.aca.2025.344692 | New procedure (matrix matching, MCR-ALS) | simulated + experimental | yes | — | no | low |
| 117 | 2025 | 10.1016/j.aca.2025.344575 | New algorithm (variable selection, SIMCA) | 3 | no | full-spectrum SIMCA | no | low |
| 122 | 2025 | 10.1016/j.aca.2025.344459 | Comparison (calibration transfer, coal) | 1 (264 samples, 2 analysers) | no | S/B, PDS, DANN | no | low |
| 126 | 2025 | 10.1016/j.aca.2025.344304 | Critique (rotational ambiguity in MCR) | several experimental | no | — | no | critical-methodology genre |
| 128 | 2025 | 10.1016/j.aca.2025.344301 | New method (robust model screening) | 1 lab + 2 public (corn) | no | CARS | no | robustness under new conditions |

## 2. What the journal publishes (patterns)

1. **Genre.** ACA accepts not only new algorithms (13/26) but also benchmarks, tutorials and critical analyses of established practice (13/26: #2, 10, 16, 41, 46, 64, 65, 70, 88, 108, 122, 126 and #75). A paper whose main message is partly a *negative* or *limiting* result ("what a pilot can and cannot predict") fits this critical-methodology tradition (#70, #88, #126 are explicitly of this kind).
2. **Evidence base.** New-method papers typically use 1–6 data sets (median ≈ 3); the largest multi-data-set studies are #46 (12 data sets) and #106 (5 data sets / 21 responses / 10 instruments). Simulated data accompany real data in fundamental papers (#30, #75, #110).
3. **Statistics.** Formal significance testing is rare in the abstracts (only #46 uses an explicit statistical model; #70 *calls for* proper statistical comparison of RMSEP). Effect sizes, multiplicity control and pre-registration are absent from all 26 abstracts.
4. **Validation and leakage** are a live editorial theme in 2026 (#16, #46, #88), as is the uncertainty of reference values (#10, #70) and the planning of measurement effort (#37 replicates; #75 sample size).
5. **Domain overlap.** Soil spectral libraries (#48, #51), fruit dry matter by Vis–NIR (#70, same public mango data set as ours) and small-sample NIR calibration (#106) are all current ACA topics.

## 3. Comparison with the strongest related ACA papers (Global Update 7)

| Criterion | #46 resampling benchmark | #106 PLSELM (low-data NIR) | #70 calibration tutorial | #16 partitioning benchmark | **This manuscript** |
|---|---|---|---|---|---|
| Question | Which CV scheme estimates test performance best? | Better calibration with few samples | Are simple PLS models enough? | How does partitioning bias SERS-ML? | How much can a small pilot set predict about the RMSEP at larger *n*? |
| Data sets / tasks | 12 | 5 / 21 responses | 1 | 1 | **11 sources / 38 tasks** (soil VisNIR/MIR/handheld NIR, fruit, fuel, tablets, meat, mixtures) |
| Group-aware splitting | sample-level | not stated | not stated | isolate-level (core message) | **group-disjoint** (profile/site/fruit) + replicate averaging |
| Theory | none | none | none | none | **deterministic-equivalent risk; identifiability limit** |
| Simulation with known truth | no | no | no | no | **yes (E0, Monte-Carlo truth)** |
| Statistics | Bayesian Bradley–Terry | not stated | RMSEP comparison advocated | not stated | **task-level Wilcoxon, Holm, bootstrap CI, rank-biserial** |
| Pre-registration / negative results | no | no | no | no | **yes (pre-registered design; failed refinement reported)** |
| Code / data | not stated | not stated | — | not stated | **public data + full code, one-command rerun** |

**Where this manuscript is stronger.** Breadth of evidence (38 tasks from 11 independent sources versus ≤ 12 data sets), a mechanistic theory that is validated directly (κ-collapse, alignment exponents), a simulation with Monte-Carlo ground truth, group-disjoint evaluation, pre-registration with fully disclosed post-hoc work, and formal statistics with multiplicity control.

**Where it is weaker or riskier.** (i) The practically best forecasters are simple rules (no-improvement rule, transferred slope), and the theory-based forecaster is not significantly better than the no-improvement rule; ACA referees may read this as "the method does not work". The manuscript must therefore lead with the *knowledge* contribution (what is and is not identifiable from a pilot, and why curves are shallow) and present the forecasting benchmark as the evidence, not oversell RPM. (ii) Unlike #106 and #48/#51, no new instrument data were measured. (iii) The topic (sample-size planning) is less common in ACA than calibration transfer or local modelling, so the introduction must connect to ACA's current validation/leakage and reference-uncertainty themes (#16, #46, #70, #88, #37).

**Actions derived from this analysis** (to be checked against the reviewer cycles): cite the directly related recent ACA work after DOI verification (#70 reference-error floor and same mango data; #46/#88 validation; #37 measurement-effort planning; #16 group-level partitioning); keep the structured abstract and the critical-methodology framing; make the practical recommendation explicit (use the no-improvement rule or a transferred slope with leave-one-source-out calibrated bands; do not trust curve-shape extrapolation).
