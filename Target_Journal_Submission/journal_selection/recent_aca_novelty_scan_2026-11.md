# Recent ACA chemometrics papers and novelty threats: scan of November 2026

Scope: forecasting learning curves (RMSEP against n) for NIR/MIR/VisNIR ridge/PLS calibrations from a pilot set, using deterministic-equivalent (random-matrix) ridge risk theory plus the eigen-spectrum of unlabelled spectra; 38 public tasks.

Method: Crossref API (ISSN 0003-2670, published from 2025-06-01; about 35 keyword queries), Crossref queries restricted to CILS, J. Chemometrics, Anal. Chem., Talanta and SAA (from 2023), and WebSearch/WebFetch for arXiv and other venues. ScienceDirect returns 403 and Crossref has no ACA abstracts, so "contribution" lines come from public abstracts, repository pages or vignettes where available. Lines marked *(title-based)* are inferred from the title and venue only. Every DOI below resolved on Crossref on 2026-11-21. Items dated 2027 are ACA articles in press that already have final volume dates.

---

## 1. Recent ACA research articles relevant to our paper (2025-06 to 2026-11)

"Why it passed" is my reading of what made the paper count as a methodological contribution.

| # | DOI | Title (short) | Contribution | Why it passed (type of novelty / evidence) |
|---|-----|---------------|--------------|---------------------------------------------|
| 1 | 10.1016/j.aca.2026.346468 | Andries & Vander Heyden, *Calibration set reduction by iterative alternating reduction of predictive variables and calibration samples subsets* (2027, in press) | Extends their OPCS idea (Talanta 2024, 10.1016/j.talanta.2023.124943): iteratively shrinks variables and calibration samples while keeping CMV predictive ability. | New **algorithm** that directly answers "how many / which calibration samples". Several real NIR sets, many X–y pairs. **Closest ACA neighbour in topic** (the number of calibration samples needed). |
| 2 | 10.1016/j.aca.2026.345155 | Olivieri, *Old advice on multivariate calibration: still in force, but not always followed. A tutorial* (2026) | Tutorial on established good practice: figures of merit, validation, sample numbers. *(title-based)* | Tutorial by a leading figure. Shows ACA values sound calibration practice. Cite it and position our work as a quantitative update to "rules of thumb". |
| 3 | 10.1016/j.aca.2025.344395 | Qian et al., *Rethinking calibration as a statistical estimation problem to improve measurement accuracy* (2025) | Replaces ordinary calibration regression with a Bayesian hierarchical model that pools information across calibration curves. | **Statistical reframing** of a routine task, with a quantified accuracy gain across three calibration methods. Shows that a "statistics lens on calibration" paper can pass when it delivers a measurable improvement. |
| 4 | 10.1016/j.aca.2026.346549 | Reiter et al., *Using tabular foundation models for robust calibration of NIR chemical sensing data* (2027, in press; arXiv 2605.21544) | Benchmarks TabPFN against PLS, ridge, CatBoost and a 1D-CNN on **66 NIR datasets** (54 regression). TabPFN ranks best but is statistically comparable to **ridge**. | **Large-scale benchmark** of a new model class. Sets the current ACA bar for the number of datasets. It also confirms that ridge is a strong NIR baseline, which supports our choice of ridge. |
| 5 | 10.1016/j.aca.2026.345651 | Ramirez-Lopez et al., *Evolutionary subset selection for domain-adaptive calibration* (2026) | `gesearch`: evolutionary selection of library samples that are coherent with a target domain. It also works when **only unlabelled target spectra** are available. | New **algorithm** plus an R package (resemble 3.0). Cross-continental soil test. Shows ACA accepts methods that exploit unlabelled spectra, which is our "cheap spectra" angle. |
| 6 | 10.1016/j.aca.2026.345682 | Ramirez-Lopez et al., *Rethinking local spectral modelling: from per-query refitting to model libraries* (2026) | Replaces per-query local PLS with precomputed model libraries. *(title-based)* | **Conceptual reframing** with computational and accuracy benefits, backed by large soil libraries and software. |
| 7 | 10.1016/j.aca.2025.343954 | Chiappini, Alcaraz & Forzani, *Bootstrap-assisted estimation of prediction uncertainty in MLP-based calibration* (2025) | Delta method plus bootstrap gives prediction variance for MLP calibration. Coverage of 95% CIs is checked on simulations, then applied to two real datasets. | **Statistical method** for an unsolved figure of merit, with the **coverage of the intervals as the validation metric**. Only two real datasets were needed, because the coverage simulation carried the evidence. |
| 8 | 10.1016/j.aca.2025.344728 | Fan et al., *PLSELM: a lightweight modeling approach for low-data calibration in NIR* (2025) | Hybrid of PLS and extreme learning machine for small calibration sets. *(title-based)* | New **algorithm** aimed at small n. Typical ACA "small-sample" paper. |
| 9 | 10.1016/j.aca.2026.345451 | Li et al., *GAN-FixMatch: generative/semi-supervised DL for small-sample quantitative NIR analysis* (2026) | Combines GAN augmentation with semi-supervised pseudo-labels to use unlabelled spectra. *(title-based)* | New **DL architecture** for small n, using agricultural and pharmaceutical data. Shows a "small-sample plus unlabelled spectra" story is in scope. |
| 10 | 10.1016/j.aca.2025.344229 | Ezenarro, *XYOnion: a layer-based method for splitting datasets into calibration and validation subsets* (2025) | New calibration/validation splitting algorithm that uses X and y. *(title-based)* | **Algorithm** compared with Kennard–Stone, SPXY and similar on several datasets. |
| 11 | 10.1016/j.aca.2025.344838 | Lopez, Gorla, …, Amigo, *The importance of choosing a proper validation strategy. Part 2: Recipes for (avoiding) overfitting – a tutorial* (2026) | Tutorial on validation design and overfitting. | Tutorial. Relevant to our "pilot CV error" estimator and to the optimism of CV at small n. |
| 12 | 10.1016/j.aca.2026.345885 | Gorla, Giussani, Riu et al., *Measurement replicates under the lens: evaluating NIR spectroscopic error quality through multivariate error analysis* (2026) | Uses the error covariance matrix (ECM) from replicates to set the **optimal number of replicates** for error estimation (portable NIR). | **Error-structure methodology** that also answers "how many measurements?". Directly useful to us: replicate-based ECM can pin the **noise floor / asymptote** of the learning curve. |
| 13 | 10.1016/j.aca.2026.346227 | Pomerantsev & Rodionova, *Mislabeling (label noise) – an often overlooked issue in chemometrics* (2026) | Raises label noise as a systematic problem. *(title-based)* | Senior-author perspective with demonstrations. Relevant because our slope is governed by the **noise fraction**, and reference-value noise is part of it. |
| 14 | 10.1016/j.aca.2025.344658 | Lintvedt, Andersen, Afseth & Wold, *Raman and NIR spectroscopy: calibration robustness for food quality – two case studies* (2025) | Discussion of robustness and long-term validity of calibrations. *(title-based)* | Applied and critical, with two case studies. Shows ACA also takes "critical discussion" papers from established groups. |
| 15 | 10.1016/j.aca.2025.344301 | Xu et al., *Method for screening near-infrared quantitative models with high robustness* (2025) | Model screening criterion for robustness. *(title-based)* | Algorithm plus criterion. |
| 16 | 10.1016/j.aca.2025.344308 | Wu et al., *Bayesian Adaptive Clustered Prior Learning (ACPL) for sparse spectroscopic regression* (2025) | Bayesian sparse regression with clustered priors on wavelengths. *(title-based)* | New **Bayesian estimator** with posterior uncertainty. |
| 17 | 10.1016/j.aca.2025.344167 | Tanzilli, Strani, Metz & Roger, *Locally-weighted-RoBoost-PLS* (2025) | PLS variant that handles nonlinearity and outliers at the same time. | New **algorithm**, several datasets, open code. |
| 18 | 10.1016/j.aca.2026.346575 | Shi, Bautista & Omstead, *Evaluation of lean chemometric methods for late-phase pharmaceutical development – prediction performance* (2026) | Evaluates "lean" (reduced-effort or reduced-sample) chemometric workflows for pharma PAT. *(title-based)* | Industrial **evaluation**. Close in spirit to sample-size economy, but likely empirical. |
| 19 | 10.1016/j.aca.2026.345655 | Holman & Kurouski, *Cross-study validation and guidance for resampling approaches for PLS-DA in spectral ML* (2026) | Cross-study validation; guidance on resampling for PLS-DA. *(title-based)* | **Many-study meta-evaluation plus guidance**. Shows ACA accepts "guidance from systematic evaluation". |
| 20 | 10.1016/j.aca.2026.345242 | Deryck, Fernández Pierna, Baeten & Lesnoff, *Step-by-step tutorial to local PLS for NIR* (2026) | Tutorial. | Tutorial. |
| 21 | 10.1016/j.aca.2025.344304 | Olivieri, *Hazards of using MCR for first-order spectral data. A rotational ambiguity analysis* (2025) | Theoretical or critical analysis showing when MCR quantitation fails. *(title-based)* | **Theory-driven critique** with a clear practical warning. A precedent that a "negative/critical" result passes when it rests on theory. |
| 22 | 10.1016/j.aca.2026.346380 | Saccenti & Camacho, *Normalisation, data structure, and recovery of PCA loadings and scores: a cautionary note* (2027, in press) | Shows normalisation distorts PCA recovery. *(title-based)* | **Cautionary/theoretical note** from known statisticians. Another precedent for critical findings, but authors of this standing get some benefit of the doubt. |
| 23 | 10.1016/j.aca.2026.345989 | Bakhshi, Abdollahi & Rajkó, *Efficient tools for MCR: outlier detection and estimation of the optimal number of components* (2026) | New tools for rank estimation and outliers in MCR. *(title-based)* | Algorithmic. Rank and noise-eigenvalue estimation sits close to our eigen-spectrum machinery. |
| 24 | 10.1016/j.aca.2025.344072 | Jakubek et al., *Improving spectroscopic detection limits with multi-pixel SNR calculations (SHERLOC)* (2025) | Multi-pixel SNR definition to improve detection limits. *(title-based)* | **Figure-of-merit methodology** with a strong application. |
| 25 | 10.1016/j.aca.2026.345285 | Williams et al., *Faster, simpler, more precise calibration curves: continuous calibration* (2026) | Extends continuous calibration. *(title-based)* | Experimental-design or calibration-strategy novelty with precision gains. |
| 26 | 10.1016/j.aca.2026.346547 | Carneiro, …, Booksh, *Consensus Projection PLS* (2027, in press) | Single-step latent-variable framework for multicomponent detection and screening. *(title-based)* | New algorithm. |
| 27 | 10.1016/j.aca.2025.344303 | Krebbers et al., *Optimizing data analysis for broadband MIR absorption spectroscopy: a hybrid dataset approach* (2025) | Mixes simulated and measured spectra to train models when labelled data are scarce. *(title-based)* | Data-efficiency method. |

Gaps in ACA coverage: no ACA paper in this window does any of the following:
- forecasts learning curves or required n for regression calibration;
- uses random-matrix or deterministic-equivalent theory;
- uses net-analyte-signal theory to predict how RMSEP scales with n.

Our topic is therefore unoccupied in ACA. Rows 1, 5, 7, 12 and 13 are the natural citations to anchor the paper in current ACA discourse.

---

## 2. Novelty threats (2018–2026, any venue)

### A. Direct threats: sample size and learning curves for spectroscopic models

| Work | DOI / ID | What it does | Threat level and how to differentiate |
|------|----------|--------------|---------------------------------------|
| Ali et al. 2018, Anal. Chem. | 10.1021/acs.analchem.8b02167 | Fits an inverse power law to a learning curve and inverts it for required training size. Raman, **classification** (6 bacteria, PCA-LDA). | **High (conceptual prior art)**. Reviewers will treat our power-law baseline as "Ali's method". We must benchmark against it explicitly and show where and why it is optimistic (we already find power-law extrapolation optimistic: frame this as a documented failure of the current standard). |
| Beleites et al. 2013, ACA | 10.1016/j.aca.2012.11.007 | Sample-size planning for **classification**. Learning curves; test-set size needed to measure performance. | Medium. Classification only. Its point that the test set masks the learning curve applies to us, so we must quantify the uncertainty of the RMSEP estimate itself. |
| Konstantinidis, Lalla et al. 2025, arXiv 2510.01210 | arXiv:2510.01210 | Ports Riley et al.'s minimum-n criteria for **continuous outcomes** (Stat. Med. 2019, 10.1002/sim.7993) to chemometrics (LIBS/Raman, planetary science). | **High and recent.** It is the only other "sample size for chemometric regression" method we found. Its formula is closed-form and uses only R² and the number of predictors (problematic for p ≫ n spectra). We should (i) cite it, (ii) include Riley/Konstantinidis as a baseline, and (iii) show the RMT effective dimension replaces "number of predictors" correctly for collinear spectra. That gives a clean, defensible novelty claim. If it reaches a journal (e.g. J. Chemometrics or Icarus) before we submit, it becomes a must-cite. |
| Ng et al. 2020, SOIL | 10.5194/soil-6-565-2020 | Empirical learning curves (350–7650 samples) for CNN vs classical models on VisNIR soil. "Effective calibration sample size". | Medium. Empirical, no forecasting. Supports our "shallow curve" finding. |
| Lucà/Conforti et al. 2017, Geoderma | 10.1016/j.geoderma.2016.11.015 | Calibration-set size study (14–144 samples) for local soil C. | Low. Empirical. |
| Breure et al. 2025, Geoderma | 10.1016/j.geoderma.2025.117504 | Propagates spectral calibration error into a decision loss (variable-rate fertiliser). Calibration-set size dominates. Diminishing returns imply an optimum sample size. | **Medium–high for a "decision rule" angle.** It already couples calibration size to an economic loss in soil spectroscopy. If we add a stopping rule we must cite it and differentiate: ours is a pilot-based forecast with uncertainty, not a geostatistical survey design. |
| Andries & Vander Heyden 2024 Talanta / 2026 ACA | 10.1016/j.talanta.2023.124943 ; 10.1016/j.aca.2026.346468 | Chooses a reduced calibration subset with equal predictive ability. | Medium. A different question ("which subset of an existing labelled set"), but reviewers may conflate the two. Contrast explicitly: they need all references first; we plan before measuring references. |
| Mohr & van Rijn 2024, Machine Learning | 10.1007/s10994-024-06619-7 | Survey of learning curves for decision-making, including data acquisition and extrapolation. | Low–medium. Generic ML. Cite it to show that learning-curve extrapolation is a recognised but unsolved problem. |
| Viering & Loog 2023, IEEE TPAMI | 10.1109/tpami.2022.3220744 | Review of learning-curve shapes: no universal parametric form; non-monotone curves happen. | Low. Supports our critique of power laws. |
| Turan, Tax, Viering & Loog 2025, Pattern Anal. Appl. | 10.1007/s10044-024-01394-6 | *Learning Learning Curves*: meta-learning to predict learning curves. | Low–medium. ML-generic. A possible extra baseline (prior from other tasks). Our 38-task bank could also serve as a meta-learning prior. |
| Figueroa et al. 2012, BMC Med Inform Decis Mak | 10.1186/1472-6947-12-8 | Weighted inverse-power-law fit for predicting required sample size. | Known. Baseline. |
| RamanBench (Koddenbrock et al., arXiv 2605.02003, NeurIPS 2026) | arXiv:2605.02003 | 77 Raman datasets, 28 models. | Low as a topic threat. **High as an evidence-scale benchmark**: ML reviewers now expect dozens of datasets. |

### B. Random-matrix and asymptotic theory near chemometrics

None of these apply RMT or deterministic equivalents to **forecast spectroscopic learning curves**. The combination with real spectral eigen-spectra on 38 public tasks remains unclaimed.

| Work | ID | What it does | Relevance |
|------|----|--------------|-----------|
| Wei, Hu & Steinhardt 2022 (ICML, PMLR 162) | (no DOI; arXiv 2203.06176) | Deterministic-equivalent ridge risk using empirical eigen-spectra predicts generalisation of real neural representations. | **Main methodological prior art.** Our contribution must be framed as transfer **plus** new chemometric content (PLS, noise identification, NAS, decisions), not as "applying Wei et al. to spectra". |
| Dobriban & Wager 2018, Ann. Stat. | 10.1214/17-aos1549 | Asymptotic ridge prediction risk. | Theory base. |
| Hastie, Montanari, Rosset & Tibshirani 2022, Ann. Stat. | 10.1214/21-aos2133 | Ridge/ridgeless risk in proportional asymptotics. | Theory base. |
| Atanasov, Zavatone-Veth & Pehlevan 2024 | arXiv:2405.00592 | Renormalised-ridge view of deterministic equivalents; scaling laws. | Theory base. Gives a clean language for "effective ridge" from unlabelled spectra. |
| Bigot, Dabo & Male 2024 | arXiv:2403.20200 | Ridge deterministic equivalents with a variance profile (non-i.i.d. rows). | Useful for heterogeneous libraries (OSSL). |
| Misiakiewicz & Saeed 2024 | arXiv:2403.08938 | Non-asymptotic deterministic equivalents for kernel ridge regression; GCV. | Gives finite-n error bounds that could support a theorem. |
| Cook & Forzani 2019, Ann. Stat. | 10.1214/18-aos1681 | PLS prediction in high dimension; "abundant" regressions reach root-n rates. | **Must cite for the PLS side.** Forzani also co-authors in ACA (row 7), so a likely reviewer pool. |
| del Val, Berrendero & Suárez 2023 | arXiv:2312.01379 | Bounds PLS-to-OLS distance via the eigenvalue distribution (Krylov view). | Helps explain why ridge theory reproduces PLS curves (eigenvalue clustering). |
| Castelli, Gannaz & Marteau 2024 | arXiv:2410.10237 | Non-asymptotic prediction bound for PLS. | PLS theory. |
| Mergny & Zdeborová 2025 | arXiv:2510.17561 | Spiked-model / BBP limits for PLS. | PLS RMT. A theory threat only if someone adds learning-curve forecasting. |
| Léger & Chatelain 2025 | arXiv:2512.15684 | High-dimensional PLS-SVD spectral analysis and fundamental limits. | Same as above. |
| Dicker 2014, Biometrika; Janson, Barber & Candès 2017, JRSS-B | 10.1093/biomet/ast065 ; 10.1111/rssb.12203 | High-dimensional noise-variance / SNR estimation. | Already known to us. The core of the "what can a pilot identify" theorem. |

Chemometrics journals (ACA, CILS, J. Chemometrics, Talanta, Anal. Chem., SAA; 2023–2026): Crossref searches for "random matrix", "Marchenko–Pastur", "deterministic equivalent" and "learning curve calibration" returned **no** regression-calibration hits.

### C. Adjacent threats: calibrated uncertainty for spectroscopic predictions

These matter if we pivot to "calibrated predictive distributions".

| Work | DOI / ID | What it does |
|------|----------|--------------|
| Duma, …, Reinikainen 2025 | arXiv:2512.23444 | Conformal-inspired, input-dependent prediction intervals for PLS/PCR, including kernel versions; NIR lab and airborne hyperspectral data; about 95% coverage. |
| Bhargav Teja 2027 (in press), Talanta | 10.1016/j.talanta.2026.130941 | *Group-conformal* NIR prediction intervals for new seasons, instruments and regions using PLS diagnostics. |
| Wiens et al. 2025, Anal. Chem. | 10.1021/acs.analchem.5c04616 | Calibrated uncertainty for soil organic carbon from Raman spectra. |
| Monte Carlo conformal for soil MIR DL, SOIL 2025 | 10.5194/soil-11-553-2025 | Conformal plus MC-dropout intervals for clay from MIR. |
| Chiappini et al. 2025, ACA | 10.1016/j.aca.2025.343954 | Bootstrap/delta-method intervals for MLP calibration. |

These cover uncertainty of **individual predictions**. **None gives a calibrated predictive distribution for the future RMSEP(n) curve**, i.e. uncertainty of the planning forecast. That gap is ours.

---

## 3. Assessment: what novelty and evidence recent ACA method papers have

Pattern across the roughly 27 papers above:

1. **A named new method that "works"** is the dominant format (rows 1, 4, 5, 7, 8, 9, 10, 16, 17, 26). The method has a name, often an acronym and software, and beats or matches baselines on a quantitative metric. Datasets range from 2 real plus simulations (row 7, where the metric was interval coverage) up to 66 (row 4).
2. **Statistical reframing with a measured gain** (rows 3, 6). Theory alone is not enough; the reframing must improve accuracy, cost or coverage.
3. **Critical or cautionary papers** (rows 13, 21, 22) pass mainly from senior, well-known authors and when backed by theory showing *why* something fails, with a prescriptive fix.
4. **Tutorials** (rows 2, 11, 20) are invited or senior-authored.

Where the current draft falls short:
- The headline results are descriptive (theory reproduces curves; curves are shallow; power laws are optimistic). The key comparative finding is **negative**: the theory forecaster does not beat "pilot CV error stays flat". An editor will read this as "elegant theory, no practical gain" and as an application of Wei et al. (2022) to spectra. That is the classic desk-reject profile under ACA's "clear, quantifiable advantages over existing approaches" clause.
- The 38 tasks are a strength, comparable to row 4. But without a winning method, the scale reads as a benchmark study, which ACA accepts less often than CILS or J. Chemometrics do.

## 4. Recommendations: making it a clear "new method that works"

Ranked by expected payoff relative to effort. Items 1–3 together would make a coherent ACA paper.

1. **Reframe the deliverable: from point forecast to calibrated predictive interval for RMSEP(n_target), plus a stopping rule.**
   - The flat-rule result is then a feature, not a failure. Theory says the curve is shallow when the noise fraction is high. The pilot CV error is therefore near-sufficient for the *point* forecast, and theory adds value in the *uncertainty* and the *decision*.
   - Evaluate with interval coverage and width across the 38 tasks (leave-one-task-out). Use decision regret against baselines: Ali-style inverse power law, Figueroa weighted IPL, Riley/Konstantinidis minimum-n, the flat rule and bootstrap of the pilot.
   - Target result: nominal coverage where power law and bootstrap under-cover, and a lower expected cost of reference analyses at a fixed target RMSEP. That is the "quantifiable advantage".
2. **A theorem on what a pilot of size n0 can identify.**
   - Using Dicker/EigenPrism-type arguments plus deterministic equivalents, show which quantities are consistently estimable from n0 labelled samples plus N unlabelled spectra: noise fraction, signal energy along the eigen-spectrum (partially), and the asymptotic slope of RMSEP(n).
   - Then show which quantity is **not** identifiable: the signal distribution beyond the pilot's effective rank. That explains *why* extrapolation is optimistic and why the flat rule is hard to beat.
   - Turn it into a computable **"identifiability horizon"** n* ≈ f(n0, spectrum). Beyond n* any forecast is prior-driven. This is a clean, citable methodological contribution that no prior work has.
3. **Anchor the noise floor with chemometric quantities: NAS and replicates.**
   - Model the RMSEP asymptote as reference-method error plus spectral noise propagated through the net analyte signal (‖NAS‖⁻¹ scaling, Lorber/Faber figures of merit).
   - Estimate it independently from replicate spectra (ECM; ACA 2026 row 12) and the reported reference-method repeatability. This turns RMT theory into **chemometric theory**: the learning curve is "NAS-limited" versus "sample-limited".
   - It gives ACA readers an interpretable diagnostic: if pilot RMSE is already within x% of the NAS/replicate floor, stop. This is distinctive, and no threat paper does it. Even on a subset of the 38 tasks (diesel, tablets and CGL have replicates or known reference error), it adds a lot.
4. **A stopping or allocation rule with explicit cost.** "Measure k more references, then re-forecast" (sequential design), based on expected RMSEP reduction per unit reference cost. Cite Breure et al. 2025 (Geoderma) as the economic motivation and differentiate as pilot-based and sequential. Report the cost saving against fixed rules of thumb (n = 100; Dardenne/Fearn) and against Konstantinidis/Riley.
5. **Use the unlabelled-spectra element as an explicit semi-supervised advantage.** Show how much the forecast's coverage and width improve as unlabelled N grows (eigen-spectrum estimation). This mirrors gesearch and GAN-FixMatch (rows 5, 9), which ACA has rewarded, and is cheap to add.
6. **Name the method and ship code** (Python/R package, e.g. on CRAN or PyPI). Most accepted ACA method papers in the scan do this.
7. **Language and positioning.**
   - Title and abstract should lead with the planning tool and its quantified advantage, not with "learning curves are shallow". Keep "power-law extrapolation is optimistic" as a strong secondary finding: it debunks the current standard (Ali 2018).
   - Explicitly state the 3–4 things that are new relative to Wei et al. 2022 (PLS, pilot identifiability theorem, NAS/replicate floor, calibrated planning intervals and stopping rule).
   - Must-cite list: Ali 2018; Beleites 2013; Konstantinidis 2025; Breure 2025; Andries 2024/2026; Reiter 2027 (ACA; ridge is competitive); Chiappini 2025; Gorla/Riu 2026; Cook & Forzani 2019; Wei 2022; Mohr & van Rijn 2024; Viering & Loog 2023.
8. **Fallback.** If none of items 1–4 can be shown to beat the flat rule on coverage or regret, the paper is honestly a theory-plus-benchmark study. Chemometrics and Intelligent Laboratory Systems or Journal of Chemometrics would then be safer homes than ACA, where a "the trivial rule is as good" headline carries high desk-reject risk.

### Things to avoid
- Claiming to be the first to do "sample size planning for spectroscopic models": Ali 2018 and Beleites 2013 were first.
- Claiming to be the first "minimum n for chemometric regression": Konstantinidis 2025.
- Presenting the power-law baseline without attributing it.
- Leaving the "theory is not better than flat" result as an unexplained conclusion. Pair it with the identifiability theorem so it reads as a *predicted* limitation.
