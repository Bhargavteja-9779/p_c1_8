# Data-leakage audit (Phase 8)

| Risk | Where it could arise | Control implemented | Verified by |
|---|---|---|---|
| Duplicate / replicate samples | Mango: two cheek scans per fruit (+ 3 temperatures for 744 fruit); KSSL VisNIR: 5 111 duplicate layer scans; Neospectra: the same soil scanned by up to 8 instruments; AfSIS: repeated scans | Replicates are averaged per physical sample *before* any split; mango restricted to the standard-temperature scans; Neospectra restricted to the 2 106 multi-scanner-averaged spectra (one row per soil) | Mango fruit reconstruction validated: median within-fruit spectral distance 0.006 vs 0.889 between random fruits; `load_ossl` groups by layer ID |
| Near-duplicates / subject leakage | Soil layers of one profile share mineralogy and spectra | Group = site/profile (KSSL site id; coordinates elsewhere); test split is group-disjoint; all CV inside pilots and ground-truth fits is leave-one-group-out (exact) or grouped K-fold | `tests/test_pipeline.py::test_split_is_group_disjoint_and_complete` |
| Temporal / source leakage | Mango seasons and orchard populations | Main analysis: fruit-level i.i.d. estimand (documented); robustness E7(c,d): season-held-out and population-grouped splits | Robustness results T8 |
| Pre-processing leakage | Column-wise scaling, PCA, or centring fitted on all data | Only sample-wise operations (absorbance conversion, SNV, Savitzky–Golay); mean-centring and ridge/PLS fitted within each training set | `test_snv_rowwise_only` |
| Test contamination via unlabelled spectra | RPM uses unlabelled spectra for the eigen-spectrum | Unlabelled spectra = pool spectra only (never test spectra); AfSIS/KSSL extra library spectra used only in an ablation | Code: `forecast_experiment.run_pilots` (lam from `truth["lam"]`, computed on pool) |
| Label leakage into forecasts | Truth curves computed on the test set | Forecasters receive only the pilot (X0, y0, groups) and unlabelled pool spectra; truth is used only for scoring | Code review (Reviewer-4 round) |
| Hyper-parameter selection on test data | Ridge penalty / PLS components | Selected by LOGO / grouped CV inside the training set only | `src/models/ridge.py` |
| Seed selection | Choosing favourable pilots | Pilot seeds derived deterministically from task name (SHA-256) and pilot index; all pilots reported | `task_seed()` |
| Design informed by evaluation data | Default r = 1 chosen in exploratory work on ICRAF-VisNIR | Disclosed; sensitivity analysis S0 excludes ICRAF-VisNIR tasks | Table S0 |
