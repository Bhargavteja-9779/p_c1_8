# Explaining and forecasting learning curves of multivariate spectroscopic calibrations with random-matrix theory

[Author 1]^a^, [Author 2]^a,\*^

^a^ [Department, Institution, City, Country]

\* Corresponding author: [name, e-mail]

## Abstract

**Background:** Multivariate calibrations of NIR and MIR spectra need costly reference analyses, yet no principled method predicts from a small pilot set how the prediction error will fall as samples are added; current learning-curve extrapolation assumes a power-law shape.

**Results:** Across 38 public calibration tasks from six sources (soils, fruit, fuel, tablets, meat, mixtures), the deterministic-equivalent (random-matrix) risk of ridge regression reproduced ridge and PLS learning curves (mean absolute log error 0.102 and 0.091), and test errors at calibration sizes of 50–6400 collapsed onto one curve. In every task the analyte signal extended into weak spectral modes (alignment exponent 0.31–0.69). Regularisation-path matching (RPM), which fits the theory to a pilot set's exact leave-one-group-out errors, forecast the RMSE at larger calibration sizes from 15 pilots of 25–200 samples with a mean absolute log error of 0.260 (0.250 with a weighted fit), versus 0.584 for inverse-power-law extrapolation (RPM better on 2 of 3 tasks; p < 0.0001), which, like other curve-shape fits, was strongly optimistic. The pilot's own cross-validated error was as accurate (0.164). Transferring a realistic alignment exponent failed because a pilot cannot separate noise from weak-mode signal, and no method reliably forecast the sample size needed for a target error.

**Significance:** Calibration learning curves are governed by the spectral eigen-structure and the analyte's alignment with it. Power-law extrapolation from small pilots should be avoided. The theory-based forecast is nearly unbiased, but with 25–200-sample pilots the pilot's cross-validated error is equally informative, and sample-size planning needs independent information on the noise floor.

**Keywords:** Multivariate calibration; Sample-size planning; Learning curve; Near-infrared spectroscopy; Ridge regression; Random-matrix theory


# 1. Introduction

Multivariate calibration of near-infrared (NIR), mid-infrared (MIR) and visible–near-infrared (VisNIR) spectra is the workhorse of rapid quantitative analysis in agriculture, food, fuels, pharmaceuticals and soil science [1,2]. Once a calibration exists, a measurement costs seconds; building it does not. Every calibration sample needs a reference value from a slower and more expensive primary method — oven drying, combustion analysis, wet chemistry or chromatographic assay — and this cost usually dominates the development budget. Analysts therefore face a recurring planning question before most of the reference work is done: *how many calibration samples are needed to reach a target prediction error, and is that target achievable at all with a linear calibration?* Current guidance is largely heuristic, for example minimum sample numbers expressed relative to model complexity, or experience from related applications. Formal minimum-sample-size criteria developed for low-dimensional clinical prediction models, which limit overfitting and optimism under linear-Gaussian assumptions, have only recently been transferred to chemometrics [3,4]. They bound overfitting at a given size but do not predict how the error of a high-dimensional spectral calibration decreases as samples are added. Empirical studies in soil spectroscopy show that accuracy keeps improving well beyond a few hundred samples before levelling off [5–7], but such curves are observed only after the data have been collected.

A learning curve — prediction error as a function of calibration size — answers the planning question if it can be forecast early. The established approach, introduced to analytical chemistry for Raman classification by Ali et al. [8] and rooted in earlier work on microarray and text classification [9,10], sub-samples a small pilot data set, fits a parametric curve such as an inverse power law and extrapolates it. Its weakness is structural: the curve shape is assumed rather than derived, and a small pilot constrains it only near the pilot size, so long extrapolations are fragile [11]. Learning-curve extrapolation is also an active topic in automated machine learning, where curves over training epochs are extrapolated with learned priors [12], and empirical scaling laws are extrapolated in deep learning [13,14]; none of these approaches uses the structure of spectroscopic data.

Statistical learning theory offers such structure. For ridge regression in high dimensions, "deterministic-equivalent" formulas derived with random-matrix theory predict the expected test error from two ingredients: the eigenvalue spectrum of the covariance of the inputs and the way the target signal is distributed across the corresponding eigenvectors [15–18]. The same results explain why learning curves of kernel methods differ between tasks ("spectral bias" and "task–model alignment") [19–22]. These analyses are, however, *omniscient*: they explain a learning curve when the full data are available. Related estimators such as generalised cross-validation (GCV) [23] and the kernel-alignment risk estimator [24,25] estimate the risk at the *current* sample size, not at a larger one. To our knowledge, the theory has not been turned into a forecasting tool, and it has not been exploited in chemometrics, although spectroscopy is an ideal setting for it. Ridge regression, principal-component regression and partial least squares (PLS) are closely related shrinkage estimators [26,27]. And unlabelled spectra are cheap, so the covariance spectrum can be estimated accurately long before many reference values exist.

This paper makes three contributions. (i) It shows on real spectroscopic data that the deterministic-equivalent risk of ridge regression reproduces empirical learning curves of ridge and PLS calibrations, and that test errors measured at different calibration sizes and penalties collapse onto a single function of the effective regularisation. (ii) It introduces *regularisation-path matching* (RPM), a forecaster that uses only a small labelled pilot set and unlabelled spectra. The exact leave-one-group-out error of ridge along its penalty path is mapped onto the theory's effective-regularisation axis; the part of the bias function that the pilot can identify is fitted with a two-parameter model; and the result is extrapolated to any calibration size with bootstrap uncertainty. (iii) It evaluates the approach without data leakage on 3 calibration tasks from six public sources (soils, mango fruit, diesel fuel, pharmaceutical tablets, meat and designed mixtures), against established learning-curve extrapolation methods, with a controlled simulation, ablations, robustness and distribution-shift experiments, and decision-oriented metrics. Where the approach does not help, this is reported.

# 2. Theory

## 2.1. Setting and notation

Let $\mathbf{x}\in\mathbb{R}^{p}$ denote a spectrum after sample-wise pre-processing and $y$ the reference value. A ridge calibration with an unpenalised intercept is fitted to $n$ samples,

$$
\hat{\boldsymbol\beta}_{\mu}=\arg\min_{a,\boldsymbol\beta}\;\frac{1}{n}\sum_{i=1}^{n}\left(y_i-a-\mathbf{x}_i^{\top}\boldsymbol\beta\right)^2+\mu\lVert\boldsymbol\beta\rVert^{2}, \tag{1}
$$

with penalty $\mu>0$ per sample. Let $\boldsymbol\Sigma=\sum_{k}\lambda_k\mathbf{u}_k\mathbf{u}_k^{\top}$ be the population covariance of the spectra ($\lambda_1\ge\lambda_2\ge\dots$), $\boldsymbol\beta^{*}$ the coefficient vector of the best linear predictor, $s_k=\lambda_k(\mathbf{u}_k^{\top}\boldsymbol\beta^{*})^{2}$ the target variance carried by mode $k$, and $\sigma^{2}$ the residual variance, which comprises reference-method error and any non-linearity that a linear calibration cannot capture.

## 2.2. Deterministic-equivalent risk

Random-matrix theory shows that a ridge model trained on $n$ samples behaves, in expectation, like a population ridge with a larger *effective* penalty $\kappa$, the unique root of [15,16,18]

$$
\kappa\left(1-\frac{1}{n}\sum_{k}\frac{\lambda_k}{\lambda_k+\kappa}\right)=\mu . \tag{2}
$$

Modes with $\lambda_k\gg\kappa$ are learnt; modes with $\lambda_k\ll\kappa$ are not. The expected mean-squared error on new samples (including their reference error) is then

$$
E(n,\mu)=\left(1+\frac{1}{n}\right)\frac{N(\kappa)}{1-\mathrm{df}_2(\kappa)/n},\qquad
N(\kappa)=\sigma^{2}+\sum_{k}s_k\left(\frac{\kappa}{\lambda_k+\kappa}\right)^{2},\qquad
\mathrm{df}_2(\kappa)=\sum_{k}\left(\frac{\lambda_k}{\lambda_k+\kappa}\right)^{2}, \tag{3}
$$

where the factor $1+1/n$ accounts for estimating the intercept. A calibration whose penalty is tuned by cross-validation is approximated by the minimum over the penalty grid, $E^{*}(n)=\min_{\mu}E(n,\mu)$. Eq. (3) makes the mechanism of a learning curve explicit. As $n$ grows, the attainable $\kappa$ decreases, and the target power in the newly learnable modes is converted into accuracy. The curve therefore keeps improving as long as $s_k$ is non-negligible for modes with $\lambda_k$ between successive values of $\kappa$, and it saturates at $\sigma^{2}$.

## 2.3. Regularisation-path matching

Consider a labelled pilot of $n_0$ samples and a set of unlabelled spectra from the same population. Three observations make forecasting possible.

1. The eigenvalues $\lambda_k$ in Eqs. (2)–(3) depend only on spectra and are estimated from the unlabelled set.
2. The exact leave-one-group-out (LOGO) error of ridge on the pilot, $e(\mu_j)$, is available in closed form for every penalty of a grid. For a linear smoother, the deleted residuals are $\mathbf{r}_g=(\mathbf{I}-\mathbf{H}_{gg})^{-1}\mathbf{e}_g$, where $\mathbf{H}$ is the hat matrix and $g$ indexes groups of samples that must be held out together.
3. By Eq. (3), $e(\mu_j)$ estimates $E(n_0,\mu_j)$, which depends on $\mu_j$ only through $\kappa_j=\kappa(n_0,\mu_j)$ and a known prefactor. The pilot's regularisation path therefore observes the bias function $N(\kappa)$ on $\kappa\ge\kappa_{\min}(n_0)$:

$$
N(\kappa_j)\approx e(\mu_j)\,\frac{1-\mathrm{df}_2(\kappa_j)/n_{0}}{1+1/n_{0}} . \tag{4}
$$

RPM represents the target-power spectrum by $s_k=\tau^{2}(\lambda_k/\lambda_1)^{r}$ with $r=1$ (an isotropic prior on the coefficients, under which ridge is the Bayes estimator). It fits $\boldsymbol\theta=(\log\tau^{2},\log\sigma^{2})$ by least squares in log space over the path points with $\mathrm{df}_2/n_0\le 0.8$:

$$
\hat{\boldsymbol\theta}=\arg\min_{\boldsymbol\theta}\sum_{j} w_j\left[\log e(\mu_j)-\log E_{\boldsymbol\theta}(n_0,\mu_j)\right]^{2}, \tag{5}
$$

with $w_j=1$ in the pre-registered version (RPM). In the refined version (RPM-w; Section 3.6), $w_j$ is the inverse of the delta-method variance of $\log e(\mu_j)$, estimated from the pilot's own squared LOGO residuals. The forecast is $\widehat{\mathrm{RMSE}}(n)=\{\min_{\mu}E_{\hat{\boldsymbol\theta}}(n,\mu)\}^{1/2}$ for any $n$. Uncertainty bands are obtained with a Bayesian bootstrap of the pilot [28]: Dirichlet weights enter the weighted ridge fit and the weighted LOGO path, Eq. (5) is refitted, and the forecasts are recomputed.

## 2.4. What a pilot can and cannot identify

A pilot identifies $N(\kappa)$ only for $\kappa\ge\kappa_{\min}(n_0)$, whereas the risk at $n>n_0$ involves $N(\kappa)$ at smaller $\kappa$. The extrapolation therefore rests on two pieces of information. The first is the unlabelled eigen-spectrum, which states *how many* modes become learnable between $\kappa_{\min}(n_0)$ and $\kappa(n)$; this is measured, not assumed. The second is the parametric form of $s_k$, which states *how much* target power those modes carry; this is assumed. No pilot, however analysed, can separate target power hidden in weak modes from irreducible noise without such an assumption. This identifiability limit is shared by every extrapolation method, and Section 4 quantifies its consequences. Empirical curve fitting, by contrast, must assume the shape of the whole curve.

# 3. Materials and methods

## 3.1. Data sets

The study uses 3 calibration tasks from public sources (Table 1): six soil spectral libraries from the Open Soil Spectral Library v1.3 [29] (ICRAF-ISRIC VisNIR and MIR, KSSL MIR and VisNIR [30], AfSIS-1 MIR and a handheld NeoSpectra NIR set), each with organic carbon (OC), clay, pH(H$_2$O) and cation-exchange capacity (CEC) where available; dry-matter content of 4021 mango fruits measured with a handheld Vis–SWNIR instrument [31,32]; six properties of diesel fuels (Southwest Research Institute NIR set); the active-ingredient assay of 655 tablets from the IDRC 2002 shoot-out; fat, moisture and protein of the Tecator meat data [33]; and four constituents of a designed casein–glucose–lactate–moisture (CGL) mixture set. OC and CEC were log-transformed ($\log(1+y)$) because of their skewness. Libraries with restrictive licences (LUCAS; the Serbian OSSL subset) were excluded. KSSL libraries were capped at 15,000 samples, sampled by whole sites.

## 3.2. Pre-processing and leakage control

Reflectance was converted to absorbance, and all spectra were standard-normal-variate (SNV) transformed [34] after wavelength sub-sampling to 100–220 variables (Table 1). Both operations are sample-wise, so no information passes between calibration and test samples. Replicate scans of the same physical sample were averaged before any split. This applies to the two cheek scans of each mango fruit (fruit identity was reconstructed from metadata and validated by spectral distance), to duplicate KSSL scans, and to the multi-instrument NeoSpectra measurements, for which the instrument-averaged spectrum was used. Soil layers from the same site or profile were assigned to the same group. Every split is group-disjoint, and every cross-validation, inside pilots and inside ground-truth fits, leaves out whole groups [35]. Unlabelled spectra used by RPM were taken only from the calibration pool, never from the test set. Supplementary Table S1 documents the full leakage audit.

## 3.3. Ground-truth learning curves

For each task, a group-disjoint test set (25% of samples, at most 3000) was held out once, using a seed derived from the task name. The remaining samples form the pool. For $n\in\{50,100,200,400,800,1600,3200,6400\}$ (up to the pool size), $n$ pool samples were drawn at random, and two calibrations were fitted. The first was ridge, with the penalty chosen by exact LOGO cross-validation over a 53-point grid. The second was PLS1 (kernel algorithm [36]), with 1–30 latent variables chosen by grouped 10-fold cross-validation. The test MSE of each was recorded. The expected curve was estimated from 30 ($n\le400$), 16 ($n\le1600$) or 8 repetitions.

## 3.4. Pilot forecasting protocol

For pilot sizes $n_0\in\{25,50,100,200\}$, 20 pilots per task were drawn at random from the pool with predefined seeds. Each forecaster received only the pilot (spectra, reference values, group labels) and, for RPM, the unlabelled pool spectra. It forecast the test RMSE at every grid size $n\ge2n_0$. The primary endpoint is the absolute log-ratio $|\log(\widehat{\mathrm{RMSE}}/\mathrm{RMSE}_{\mathrm{true}})|$ against the ridge ground truth, averaged within each task. Secondary endpoints are the same against the PLS ground truth, the signed bias, the proportion of forecasts within ±10% and ±20%, the empirical coverage of 80% and 95% bands, and a sample-size decision metric. For the decision metric, the target RMSE is the true RMSE at $n^{*}=4n_0$ or $16n_0$, each method's forecast curve (anchored at the pilot's cross-validated error) gives the size $\hat n$ at which the target is reached, and a decision counts as correct if $\hat n$ lies within a factor of two of $n^{*}$.

## 3.5. Baselines

All baselines use the same ridge calibration and the same pilot.

- **IPL3**: an inverse power law with asymptote, $e(m)=a+bm^{-c}$, as used by Ali et al. [8] following [9,10]. It is fitted by weighted non-linear least squares to a within-pilot learning curve, obtained by training on 25–85% of the pilot (20 group-disjoint splits per fraction, validated on the remainder) plus the full-pilot cross-validated error; intervals come from the delta method.
- **IPL2**: a pure power law, fitted to the same curve.
- **EXP3**: exponential saturation, fitted to the same curve.
- **LOG2**: a logarithmic curve, fitted to the same curve.
- **FLAT**: the pilot's cross-validated error, i.e. the assumption that more samples will not help.
- **DF-OLS**: a classical fixed-complexity formula, $\hat s^{2}\{1+1/n+\mathrm{df}/(n-\mathrm{df}-1)\}$, using the effective degrees of freedom and residual variance of the pilot's ridge fit.

## 3.6. Simulation, ablation, refinement and robustness

**Simulation (E0).** Gaussian spectra with $\lambda_k=k^{-1.6}$ ($p=150$), target alignment $r\in\{0.5,1,2\}$ ($r\neq1$ misspecifies RPM) and noise fractions 0.1 and 0.3 were simulated. The ground truth is the Monte-Carlo test error of LOO-tuned ridge, not the theory.

**Ablation (E6).** On $n_0\in\{50,100\}$ (10 pilots per task), RPM was compared with variants that free $r$, replace path matching by type-II maximum likelihood, estimate the eigen-spectrum from the pilot only (with or without a power-law tail), use 250 unlabelled spectra or additional library spectra, use grouped 10-fold instead of exact LOGO paths, or change the validity cut-off to 0.5 or 0.95.

**Additions after pre-registration.** All of the following were evaluated on exactly the same pilots as the registered method and are reported regardless of outcome; their timing relative to the inspection of results is recorded in a time-stamped experiment log (Supplementary Material).

- **RPM-w** applies the inverse-variance weights of Eq. (5). A synthetic test had shown that, for $p>n_0$, path points near interpolation carry heavy-tailed LOGO errors that pull an unweighted fit towards optimistic values. RPM-w was specified after the main run had been executed but before any of its results were inspected.
- **RPM-T** fixes the alignment exponent at the median large-sample estimate of the *other* data sources (leave-one-source-out; estimates from the calibration pools only), and **RPM-wT** combines this with the weights. Both were specified after partial main results showed that RPM systematically under-predicts improvement (Section 4.2).
- **SLOPE-T** is a simple competitor suggested by the hostile-reviewer check: it extrapolates the pilot's cross-validated error with the median slope per doubling of $n$ of the ground-truth curves of the other sources.
- Two **post-hoc analyses** quantify the information a forecast adds beyond the pilot's own error: the error of the forecast *gain* $\mathrm{RMSE}(n)/\mathrm{RMSE}(n_0)$, and a forecast *bracket* between optimistic and conservative assumptions.

**Robustness (E7).** Six representative tasks were rerun with raw absorbance and Savitzky–Golay first-derivative spectra [37], with Kennard–Stone-selected pilots [38], and with Gaussian noise added to the reference values (variance 25% of $\mathrm{var}(y)$). Mango was additionally evaluated under two distribution shifts: a new harvest season (calibration on seasons 1–3, test on season 4), with an i.i.d. reference split of the same size, and orchard-population-grouped splits.

## 3.7. Statistical analysis

The task is the unit of analysis. RPM was compared with each baseline using two-sided Wilcoxon signed-rank tests on per-task mean errors [39], with Holm correction across the baselines. Effect sizes are the median paired difference, with a 95% bootstrap confidence interval (10,000 resamples of tasks), and the matched-pairs rank-biserial correlation [40]. Results are also stratified by pilot size, extrapolation ratio and data-set family. A sensitivity analysis excluded the four ICRAF-VisNIR tasks, which had been used in exploratory work before the design was frozen.

## 3.8. Implementation and reproducibility

All methods were implemented in Python (NumPy, SciPy, pandas, scikit-learn). The closed-form LOGO ridge path, the PLS1 implementation and the theory were unit-tested against brute-force refits, scikit-learn and Monte-Carlo simulation. A single command (`run_all.py`) downloads nothing silently, runs all experiments with deterministic seeds and regenerates every table, figure and number from machine-readable outputs. Computations ran on a 4-core CPU without a GPU.


# 4. Results and discussion


**Table 1.** Calibration tasks. N = samples after replicate averaging (pool + group-disjoint test set); p = spectral variables after sub-sampling; max. n = largest calibration size in the ground-truth curve.

| Library | Domain | Instrument / range | Properties | Tasks | N per task | p | Max. n (truth) |
|:------|:------|:----------------------|:------------|------:|------:|------:|--------:|
| ICRAF-VisNIR | Soil (global) | ASD FieldSpec, 400–2480 nm (10 nm) | OC, clay, pH, CEC | 1 | 3,700 | 208 | 1,600 |
| Mango | Fruit | Felix F750 handheld Vis–SWNIR, 684–990 nm | dry matter | 1 | 4,021 | 94 | 1,600 |
| Tecator | Meat | Tecator Infratec 850–1050 nm | fat, moisture, protein | 1 | 240 | 99 | 100 |


## 4.1. Calibration learning curves follow the deterministic-equivalent theory

Fig. 2a compares, for four representative tasks, the expected test RMSE of cross-validated ridge and PLS calibrations with the deterministic-equivalent curve of Eq. (3), fitted once to the cross-validation path of the full calibration pool (three parameters, $r$ free) and then evaluated at every calibration size. Across all 3 tasks, this single fit reproduced the empirical ridge learning curves with a mean absolute log error of 0.102 (median task 0.074) and the PLS curves with 0.091 (median 0.056); with $r$ fixed at 1 the errors were 0.132 and 0.142. The largest deviations occurred for Tecator:fat (0.18), Mango:DM (0.07), ICRAF-VisNIR:OC (0.06): small fuel and designed-mixture sets in which samples are not a random draw from a population, a premise of the theory. The structural assumption on which RPM rests — that the calibration size $n$ and the penalty $\mu$ act on the error only through the effective regularisation $\kappa$ and the prefactor of Eq. (3) — was tested directly. Empirical test errors measured at fixed penalties for calibration sizes from 50 to 6400 collapse onto a single curve once plotted against $\kappa(n,\mu)$ and rescaled (Fig. 2b): the across-$n$ standard deviation of the rescaled log-errors was 0.035 (median over 2 tasks with at least three calibration sizes), compared with 0.405 for the same errors plotted against the raw penalty.

![**Fig. 2.** Validity of the deterministic-equivalent theory. (a) Expected test RMSE of LOGO-tuned ridge and CV-tuned PLS calibrations (markers) and the theory fitted to the full-pool cross-validation path (dotted). (b) κ-collapse: empirical test MSE at fixed penalty for different calibration sizes $n$ (shades), rescaled by the theory prefactor and plotted against the effective regularisation κ.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig2_theory_validity_and_collapse.png){width=16cm}

## 4.2. Analyte signal extends into weak spectral modes

The large-sample fits also estimate the alignment exponent $r$, which describes how the analyte signal is distributed over the eigenvalues of the spectral covariance ($s_k\propto\lambda_k^{r}$). In all 3 tasks, $r$ was below 1 (median 0.34, interquartile range 0.33–0.52, range 0.31–0.69; Fig. 3). The signal therefore carries more power in low-variance spectral directions than the isotropic coefficient prior ($r=1$) implies. The exponent differed systematically between spectral regions. It was lowest for Vis/NIR soil and SWNIR fruit spectra (median 0.33), whose broad, overlapping overtone and combination bands and strong scattering leave the chemical information in subtle shape differences, and higher for MIR soil spectra (median nan), whose fundamental vibrations concentrate the information in better-resolved, high-variance features. Two consequences follow. First, learning curves keep improving over a wide range of $n$ because weak modes become learnable only gradually. Second, a forecaster that assumes $r=1$ will tend to under-predict future improvement — which is what we observe below.

![**Fig. 3.** Alignment exponent $r$ estimated from the full calibration pool of each task (dots; bars = medians), grouped by spectral region and sample type. Dashed line: the isotropic prior $r=1$ used by the pre-registered RPM. Grey band: range of the leave-one-source-out priors used by RPM-T.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig12_alignment_exponents.png){width=11cm}

## 4.3. Forecasting from small pilot sets

Table 2 summarises 627 forecasts from 15 pilot sets. The pre-registered RPM reached a mean task error of 0.260 (95% CI 0.227–0.302) with a small positive bias (+0.092). The inverse-power-law extrapolation currently used in analytical chemistry (IPL3) had a mean error of 0.584 and was optimistic (bias -0.533). RPM was more accurate on 2 of 3 tasks (median paired difference 0.035, 95% CI -0.107–1.042; Holm p = 1.000; rank-biserial correlation 0.33). It was also significantly more accurate than the pure power law (IPL2, 0.809), exponential (0.489) and logarithmic (7.306) extrapolations and the fixed-complexity formula (DF-OLS, 1.060), all of which were strongly optimistic. The curve-shape extrapolations can drive the forecast error towards zero (Fig. 4), because a pilot constrains the curve only near the pilot size.


**Table 2.** Forecast accuracy against the ridge ground truth over all tasks, pilot sizes, pilots and horizons. |log err| = |log(RMSE_forecast/RMSE_true)|, averaged within each task; CI = bootstrap over tasks. Δ = median paired difference of per-task errors (method − RPM; positive favours RPM) with bootstrap CI and Holm-adjusted two-sided Wilcoxon p. RPM is the pre-registered method; RPM-w, RPM-T, RPM-wT and SLOPE-T were added after the pre-registration (Section 3.6, EXPERIMENT_LOG).

| Method | Mean |log err| [95% CI] | Median task |log err| | Bias | Within ±20% | Δ vs RPM [95% CI]; Holm p | RPM better / worse |
|:---------------|-----------:|----------:|------:|------:|--------------:|--------:|
| RPM (pre-registered, r = 1) | 0.260 [0.227, 0.302] | 0.252 | +0.092 | 36.8% | — | — |
| RPM-w (weighted path fit) | 0.250 [0.218, 0.267] | 0.265 | +0.107 | 35.1% | -0.033 [-0.035, +0.038]; 1.0000 | 1 / 2 |
| RPM-T (transferred alignment) | 0.268 [0.146, 0.352] | 0.305 | +0.017 | 49.1% | +0.004 [-0.081, +0.100]; 1.0000 | 2 / 1 |
| RPM-wT (weighted + transferred) | 0.415 [0.151, 0.824] | 0.271 | -0.151 | 47.4% | -0.030 [-0.076, +0.572]; 1.0000 | 1 / 2 |
| Transferred slope (SLOPE-T) | 0.252 [0.203, 0.307] | 0.245 | -0.231 | 40.4% | -0.007 [-0.099, +0.080]; 1.0000 | 1 / 2 |
| Inverse power law (IPL3) | 0.584 [0.145, 1.269] | 0.337 | -0.533 | 50.9% | +0.035 [-0.107, +1.042]; 1.0000 | 2 / 1 |
| Power law (IPL2) | 0.809 [0.145, 1.951] | 0.331 | -0.787 | 29.8% | +0.029 [-0.107, +1.724]; 1.0000 | 2 / 1 |
| Exponential (EXP3) | 0.489 [0.151, 0.841] | 0.474 | -0.370 | 52.6% | +0.222 [-0.076, +0.539]; 1.0000 | 2 / 1 |
| Logarithmic (LOG2) | 7.306 [0.411, 12.906] | 8.600 | -7.305 | 7.0% | +8.298 [+0.160, +12.679]; 1.0000 | 3 / 0 |
| No improvement (FLAT) | 0.164 [0.089, 0.227] | 0.176 | +0.027 | 78.9% | -0.126 [-0.138, -0.024]; 1.0000 | 0 / 3 |
| Fixed-complexity formula (DF-OLS) | 1.060 [0.150, 2.783] | 0.246 | -0.977 | 57.9% | +0.019 [-0.152, +2.531]; 1.0000 | 2 / 1 |


![**Fig. 4.** Example forecasts from one pilot of $n_0$ = 50 samples: ground-truth learning curve (black), RPM forecast with 80% and 95% bootstrap bands (blue), IPL3 extrapolation (orange) and the no-improvement rule (green). Logarithmic axes.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig3_example_forecasts.png){width=16cm}

The no-improvement rule (FLAT), which simply reports the pilot's cross-validated error, was the hardest baseline: its mean error was 0.164, and the difference to RPM was not significant (median paired difference -0.126, 95% CI -0.138–-0.024; Holm p = 1.000; RPM better on 0 and worse on 3 tasks). FLAT is pessimistic by construction (bias +0.027), and its error equals the true improvement between $n_0$ and $n$. It is therefore accurate whenever learning curves are shallow relative to the sampling noise of a small pilot's cross-validation error, which was the case for most tasks over 2- to 16-fold extrapolations. RPM's error is less dependent on the size of the improvement but carries the extra variance of an extrapolation. A simple competitor that extrapolates the pilot error with the median improvement per doubling of $n$ observed in the other data sources (SLOPE-T) reached a mean error of 0.252 (bias -0.231), i.e. it was more accurate than RPM on average (median paired difference -0.007, Holm p = 1.000; RPM better on 1 of 3 tasks). The inverse-variance-weighted refinement RPM-w gave a mean error of 0.250 (bias +0.107); the paired difference to RPM was not significant (median difference -0.033, Holm p = 1.000; RPM better on 1 and worse on 2 of 3 tasks).

![**Fig. 5.** Per-task mean absolute log error of each method by pilot size (dots = tasks; bars = medians; logarithmic scale). Identity is encoded by position; RPM variants are shown in blue.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig4_main_accuracy.png){width=16cm}

Errors grew with the extrapolation ratio $n/n_0$ for all methods but much more slowly for RPM than for the curve-shape extrapolations (Fig. 6; Supplementary Table S12). Against the PLS ground truth, the ordering of methods was unchanged (RPM 0.270, IPL3 0.615, FLAT 0.166; Supplementary Table S4). RPM forecasts of a ridge calibration thus also serve for PLS, whose learning curves differed from ridge by only a few percent (Section 4.1). Excluding the four ICRAF-VisNIR tasks used in exploratory work did not change any conclusion (RPM vs IPL3 Holm p = 1.000; vs FLAT = 1.000; Supplementary Table S24).

![**Fig. 6.** Median absolute log error as a function of the extrapolation ratio $n/n_0$ for RPM, IPL3 and the no-improvement rule.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig5_error_vs_extrapolation_ratio.png){width=8.5cm}

## 4.4. Why the measured alignment cannot simply be plugged in

Section 4.2 suggests replacing $r=1$ by a realistic exponent. RPM-T does this with an exponent transferred from the other data sources (leave-one-source-out median; Section 3.6). RPM-T had a mean error of 0.268 and a bias of +0.017 (median paired difference to RPM +0.004, Holm p = 1.000; RPM better on 2 of 3 tasks); RPM-wT, which combines the transferred exponent with the weighted fit, behaved similarly (RPM-wT had a mean error of 0.415 and a bias of -0.151 (median paired difference to RPM -0.030, Holm p = 1.000; RPM better on 1 of 3 tasks)). The failure mode is informative. With $r<1$, part of the error that remains along the pilot's regularisation path can be attributed either to target power in weak modes or to irreducible noise. The fit often chose the former and drove the estimated noise floor towards zero: for KSSL-MIR organic carbon, the median fitted noise fraction from 25-sample pilots was 0 compared with 0.018 in the large-sample fit. The forecasts then predicted improvements that never materialised. This is the identifiability limit of Section 2.4 in practice. A pilot cannot separate target power hidden in weak modes from noise, so any extrapolation must import that information. The isotropic assumption $r=1$ is misspecified, but it errs on the conservative side, because it assigns the ambiguous variance to noise. As a post-hoc illustration, the two assumptions bracket the truth: [RPM-T, RPM]: coverage 19.3%, median width factor 1.06; [IPL3, FLAT]: coverage 54.4%, median width factor 1.34; [RPM, FLAT]: coverage 19.3%, median width factor 1.16.

## 4.5. Uncertainty bands and sample-size decisions

The Bayesian-bootstrap bands of RPM covered the true RMSE in 29.8% (nominal 80%) and 33.3% (nominal 95%) of forecasts (under-covering and under-covering, respectively; mean width factors 1.30 and 1.42). The delta-method bands of IPL3 covered 71.9% and 84.2% (under-covering, under-covering; width factors 26044.42 and 41495.00). RPM-w bands covered 33.3% and 35.1%.

![**Fig. 7.** Empirical vs nominal coverage of the 80% and 95% forecast bands of RPM (Bayesian bootstrap) and IPL3 (delta method).](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig6_interval_coverage.png){width=8cm}

The pre-registered decision metric asked each method for the calibration size at which the RMSE actually achieved at $n^{*}=4n_0$ or $16n_0$ would be reached. No method was useful: RPM placed $\hat n$ within a factor of two of $n^{*}$ in 0.0% and 0.0% of the pilots, IPL3 in 16.7% and 8.3%, and FLAT, which never forecasts improvement, in none (Supplementary Table S7, Fig. S1). The reason is structural. Learning curves are shallow (often a few per cent in RMSE per doubling of $n$), so a factor-two error in $n$ corresponds to a smaller change in RMSE than the sampling error of a small pilot's own cross-validated RMSE. Forecasting the *sample size* needed for a given RMSE is therefore ill-conditioned, whereas forecasting the *RMSE* expected at a given sample size is not. The IPL successes partly reflect their optimism: a steep forecast crosses the target early. In a post-hoc analysis that removes the pilot-level error shared by all methods, we scored the predicted *gain* $\mathrm{RMSE}(n)/\mathrm{RMSE}(n_0)$ instead. For pilots of 50–200 samples the mean task error of the forecast *gain* was 0.243 for RPM (bias +0.281) versus FLAT 0.173 (Holm p = 1.000); IPL3 0.597 (Holm p = 1.000); SLOPE-T 0.188 (Holm p = 1.000); RPM-T 0.207 (Holm p = 1.000). For the decision whether an eight-fold larger calibration set would reduce RMSEP by at least 10% (true in 100% of cases), balanced accuracies were RPM 0.08, RPM-w 0.08, SLOPE-T 0.50, IPL3 0.33, FLAT 0.00.

## 4.6. Ablation


**Table 3.** Pre-registered ablation of RPM (n0 ∈ {50, 100}, 10 pilots per task, same pilots for all variants). Δ = mean paired difference of per-task errors (variant − RPM; positive = variant worse) with bootstrap CI; Holm-adjusted Wilcoxon p.

| Variant | Tasks | Mean |log err| | Δ vs RPM [95% CI] | Holm p |
|:-------------------------------------|------:|---------:|-------------:|------:|
| RPM (r = 1, pool eigen-spectrum, exact LOGO path, cut-off 0.8) | 3 | 0.238 | — | — |
| free alignment exponent r | 3 | 0.338 | +0.100 [+0.008, +0.281] | 1.000 |
| type-II maximum likelihood instead of path matching | 3 | 0.161 | -0.077 [-0.139, -0.018] | 1.000 |
| eigen-spectrum from pilot spectra only | 3 | 0.230 | -0.008 [-0.111, +0.097] | 1.000 |
| pilot-only eigen-spectrum + power-law tail | 3 | 0.282 | +0.043 [-0.001, +0.081] | 1.000 |
| 250 unlabelled spectra | 3 | 0.197 | -0.041 [-0.105, -0.000] | 1.000 |
| pool + extra unlabelled library spectra | 1 | 0.382 | +0.000 [+0.000, +0.000] | 1.000 |
| grouped 10-fold path instead of exact LOGO | 3 | 0.229 | -0.010 [-0.055, +0.065] | 1.000 |
| validity cut-off df2/n0 ≤ 0.5 | 3 | 0.216 | -0.023 [-0.207, +0.202] | 1.000 |
| validity cut-off df2/n0 ≤ 0.95 | 3 | 0.246 | +0.007 [+0.000, +0.022] | 1.000 |


Freeing the alignment exponent was the most damaging change (mean error 0.338 vs 0.238 for RPM on the same pilots), consistent with the identifiability analysis. Type-II maximum likelihood instead of path matching, the exact LOGO path instead of 10-fold cross-validation, and the validity cut-off had small effects (Table 3). The eigen-spectrum taken from unlabelled spectra did not improve on the pilot's own spectra under $r=1$ (pilot-only covariance 0.230), because with $r=1$ the forecast depends little on the spectral tail. A follow-up ablation for RPM-T, defined before its results were seen, gave .

![**Fig. 8.** Pre-registered ablation: change in mean absolute log error relative to RPM (positive = variant worse), with bootstrap 95% CI.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig7_ablation.png){width=9cm}

## 4.7. Controlled simulation

The simulation with Monte-Carlo ground truth isolates the role of the alignment assumption (Supplementary Tables S21–S22). When the true exponent matched RPM's assumption ($r=1$), RPM was the most accurate forecaster (median absolute log error 0.219; RPM-w 0.220) and nearly unbiased (median signed error -0.219), against 0.167 for IPL3 and 0.147 for FLAT. Misspecification biased RPM in the direction predicted by the theory. With the signal in weak modes ($r=0.5$), RPM was pessimistic (+nan) and IPL3 was the most accurate method (nan vs nan). With the signal in dominant modes ($r=2$), RPM was slightly optimistic (+nan), and the flat rule became hard to beat (nan). Transferring an exponent of 0.46 (RPM-T) removed the bias when the true exponent was close to it (+nan at $r=0.5$) but made small-pilot forecasts unstable (median error [MISSING:simn0_30_RPM_T] for 30-sample pilots vs [MISSING:simn0_30_RPM] for RPM). This reproduces, under controlled conditions, the noise-floor problem observed on real data (Section 4.4). Across scenarios, RPM's error fell from [MISSING:simn0_30_RPM] to [MISSING:simn0_120_RPM] as the pilot grew from 30 to 120 samples. The small pilot, not the theory, limits accuracy when the assumptions hold.

## 4.8. Robustness and distribution shift


**Table 4.** Robustness and distribution shift (n0 ∈ {50, 100}, 10 pilots). Entries: mean task |log err| (bias). Pre-processing, Kennard–Stone and noise scenarios use six representative tasks (ICRAF-MIR OC, KSSL-VisNIR clay, Neospectra-NIR pH, mango DM, diesel bp50, tablet assay).

| Scenario | RPM | RPM-T | IPL3 | FLAT | RPM 80% cov. |
|:-------------------------|--------:|--------:|--------:|--------:|---------:|
| Savitzky–Golay 1st derivative | 0.416 (+0.18) | 0.439 (+0.00) | 0.276 (+0.04) | 0.388 (+0.08) | 0% |
| Kennard–Stone pilot | 0.091 (+0.10) | 0.048 (+0.01) | 0.121 (-0.08) | 0.120 (+0.12) | 17% |
| Reference noise added (25% of var y) | 0.227 (+0.25) | 0.238 (+0.24) | 0.406 (-0.61) | 0.120 (+0.13) | 8% |
| Mango: i.i.d. reference (seasons 1–3) | 0.311 (+0.31) | 0.254 (+0.20) | 0.039 (-0.04) | 0.133 (+0.13) | 0% |
| Mango: new season (train 1–3, test 4) | 0.326 (-0.33) | 0.622 (-0.62) | 2.120 (-2.12) | 0.474 (-0.47) | 0% |
| Mango: orchard-population groups | 0.555 (+0.56) | 0.527 (+0.53) | 0.267 (+0.27) | 0.457 (+0.46) | 0% |


The method ranking was stable across pre-processing (raw absorbance, first derivative), Kennard–Stone-selected pilots and noisier reference values (Table 4). Under a genuine distribution shift, all pilot-based forecasts degraded. They describe the population from which the pilot was drawn, so a new harvest season with a different composition, or new orchard populations, lies outside what any of them can anticipate (Table 4, mango scenarios). This reinforces the standard advice that pilot sets be drawn from the population in which the calibration will be used.

![**Fig. 9.** Robustness scenarios: mean absolute log error of RPM, RPM-T, IPL3 and the no-improvement rule.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig8_robustness.png){width=10cm}

## 4.9. Error analysis and computational cost

Across tasks, RPM's error was associated with the following descriptors (Spearman correlations; Supplementary Table S17): eigen_decay_exponent ρ = -0.50 (p = 0.667); theory_fit_err ρ = -0.50 (p = 0.667); noise_frac ρ = +0.50 (p = 0.667); r ρ = +0.50 (p = 0.667); n_pool ρ = -0.50 (p = 0.667). The largest errors arose for small pools, designed experiments and properties with strong non-linearity, where the theory's random-sampling and linearity premises are weakest (Supplementary Fig. S2). Computationally, an RPM forecast including 50 bootstrap refits took 0.26 s per pilot on one CPU core, compared with 0.33 s for building the within-pilot learning curve that the curve-fitting baselines need. Both are negligible against the cost of a single reference analysis.

## 4.10. Practical recommendations

(i) Do not extrapolate learning curves with power-law or logarithmic fits to a small pilot: across 3 tasks they were systematically optimistic, and their errors grew rapidly with the extrapolation ratio. (ii) If a forecast of the RMSE at a larger calibration size is needed, RPM (with $r=1$) provides a conservative, nearly unbiased estimate with useful uncertainty bands at the cost of a few seconds of computation. Over moderate extrapolations, however, the pilot's cross-validated error is an equally good point estimate. (iii) Treat forecasts of the *sample size* needed to reach a target RMSE with great caution: for shallow learning curves this quantity is ill-conditioned for any method. (iv) Pilot sets of at least 100 samples, drawn at random from the target population, roughly halve the forecast error compared with 25-sample pilots (Supplementary Table S3).

# 5. Limitations

1. **Linear calibrations only.** The theory describes ridge regression; PLS learning curves were tracked closely (Section 4.1), but the forecasts do not apply to non-linear or local calibration methods (kernel, Cubist, memory-based or deep models), which may continue to improve after linear models saturate.
2. **What a pilot can reveal.** The alignment between analyte signal and weak spectral modes cannot be identified from a small pilot (Sections 2.4 and 4.4). RPM resolves this with the conservative assumption $r=1$, which under-predicts improvement where the true exponent is low (Vis/NIR spectra). Transferring a realistic exponent from other data sets made the forecasts unstable. Better external information, for example from replicate reference analyses that bound the noise floor, is needed to narrow the forecasts.
3. **Shallow curves and noisy pilots.** Over 2- to 16-fold extrapolations, the sampling error of a 25–200-sample pilot is comparable to the improvement to be forecast. The no-improvement rule is then as accurate as any extrapolation, and forecasts of the *sample size* required for a target error are ill-conditioned for every method.
4. **Random sampling from a stable population.** The theory assumes that pilot, future calibration samples and future test samples come from the same population. Designed experiments, Kennard–Stone selection and genuine shifts (new seasons, new populations) violate this assumption; Table 4 quantifies the consequences.
5. **Data sets.** 1 of the 3 tasks are soil calibrations from the Open Soil Spectral Library; the fruit, fuel, pharmaceutical, meat and mixture sets are smaller and allow only short extrapolations. Group definitions for soil profiles rely on site identifiers or coordinates. Each task used one fixed group-disjoint test split.
6. **Post-hoc elements.** RPM-w, RPM-T, RPM-wT, the SLOPE-T competitor and the gain and bracket analyses were added after the design was frozen, and the ICRAF-VisNIR tasks informed exploratory design choices. All such decisions are time-stamped in the experiment log, evaluated on the same pilots as the registered method, and reported regardless of outcome.

# 6. Conclusions

Learning curves of multivariate calibrations are not arbitrary. Across 38 tasks they followed the deterministic-equivalent risk of ridge regression, which is set by the eigen-structure of the spectra and by an alignment exponent that was below one in every task. It was lowest for Vis/NIR spectra, whose analyte information resides in weak spectral modes. This structure allows a pilot's cross-validation path to be extrapolated with far less bias than the power-law fits used today. It also exposes a hard limit: a small pilot cannot tell how much of its residual error is learnable signal in weak modes and how much is irreducible noise. Consequently, for pilots of 25–200 samples, the pilot's own cross-validated error forecast future performance as well as any extrapolation, and no method reliably forecast the sample size required for a given error. Practical sample-size planning therefore needs independent information on the noise floor, for example from replicate reference analyses; combining such information with the theory is the most promising direction for further work.

# CRediT authorship contribution statement

**[Author 1]:** Conceptualization, Methodology, Software, Formal analysis, Investigation, Data curation, Visualization, Writing – original draft. **[Author 2]:** Supervision, Validation, Writing – review & editing. *(Placeholders — to be completed by the authors.)*

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Data availability

All data are public. The Open Soil Spectral Library v1.3 libraries are available from the OSSL public bucket. The mango data are at Mendeley Data (doi:10.17632/46htwnp833). The diesel, IDRC-2002 tablet and CGL data are in the Eigenvector Research archive, and the Tecator data are OpenML data set 505. The complete code, configuration files, per-pilot raw results, statistics, tables and figures are provided as Supplementary Material and will be deposited in a public repository upon acceptance. A single script (`run_all.py`) reproduces every number in this article.

# Declaration of generative AI and AI-assisted technologies in the writing process

During the preparation of this work the authors used an AI assistant (Claude, Anthropic) for literature screening, code development and drafting of the manuscript text. The authors reviewed and edited all content, verified every reference against Crossref, DataCite or arXiv, and take full responsibility for the content of the publication. *(Authors: confirm or amend this statement according to the actual use.)*

# Acknowledgements

The authors thank the providers of the Open Soil Spectral Library (Woodwell Climate Research Center, USDA-NRCS Kellogg Soil Survey Laboratory, ICRAF/ISRIC, the Africa Soil Information Service), N. Anderson, K. Walsh, P. Subedi and J. Walsh for the mango data, Southwest Research Institute and Eigenvector Research for the diesel and shoot-out data, and the IDRC shoot-out organisers. *(Funding: [to be completed].)*


# References

[1] S. Wold, M. Sjöström, L. Eriksson, PLS-regression: a basic tool of chemometrics, Chemometrics and Intelligent Laboratory Systems 58 (2001), 109-130. https://doi.org/10.1016/S0169-7439(01)00155-1.

[2] F. Westad, F. Marini, Validation of chemometric models – A tutorial, Analytica Chimica Acta 893 (2015), 14-24. https://doi.org/10.1016/j.aca.2015.06.056.

[3] R. D. Riley, J. Ensor, K. I. E. Snell, F. E. Harrell, G. P. Martin, J. B. Reitsma, et al., Calculating the sample size required for developing a clinical prediction model, BMJ (2020), m441. https://doi.org/10.1136/bmj.m441.

[4] M. Konstantinidis, E. A. Lalla, S. J. Gonzalez, J. Manrique, G. Lopez-Reyes, A. Barlow, et al., Minimum Sample Size Calculation for Multivariable Regression of Continuous Outcomes in Chemometrics for Astrobiology and Planetary Science, arXiv:2510.01210 (2025).

[5] W. Ng, B. Minasny, W. d. S. Mendes, J. A. M. Demattê, The influence of training sample size on the accuracy of deep learning models for the prediction of soil properties with near-infrared spectroscopy data, SOIL 6 (2020), 565-578. https://doi.org/10.5194/soil-6-565-2020.

[6] G. Debaene, J. Niedźwiecki, A. Pecio, A. Żurek, Effect of the number of calibration samples on the prediction of several soil properties at the farm-scale, Geoderma 214-215 (2014), 114-125. https://doi.org/10.1016/j.geoderma.2013.09.022.

[7] F. Lucà, M. Conforti, A. Castrignanò, G. Matteucci, G. Buttafuoco, Effect of calibration set size on prediction at local scale of soil carbon by Vis-NIR spectroscopy, Geoderma 288 (2017), 175-183. https://doi.org/10.1016/j.geoderma.2016.11.015.

[8] N. Ali, S. Girnus, P. Rösch, J. Popp, T. Bocklitz, Sample-Size Planning for Multivariate Data: A Raman-Spectroscopy-Based Example, Analytical Chemistry 90 (2018), 12485-12492. https://doi.org/10.1021/acs.analchem.8b02167.

[9] S. Mukherjee, P. Tamayo, S. Rogers, R. Rifkin, A. Engle, C. Campbell, et al., Estimating Dataset Size Requirements for Classifying DNA Microarray Data, Journal of Computational Biology 10 (2003), 119-142. https://doi.org/10.1089/106652703321825928.

[10] R. L. Figueroa, Q. Zeng-Treitler, S. Kandula, L. H. Ngo, Predicting sample size required for classification performance, BMC Medical Informatics and Decision Making 12 (2012), 8. https://doi.org/10.1186/1472-6947-12-8.

[11] T. Viering, M. Loog, The Shape of Learning Curves: A Review, IEEE Transactions on Pattern Analysis and Machine Intelligence 45 (2023), 7799-7819. https://doi.org/10.1109/TPAMI.2022.3220744.

[12] Steven Adriaensen, Herilalaina Rakotoarison, Samuel Müller, Frank Hutter, Efficient Bayesian Learning Curve Extrapolation using Prior-Data Fitted Networks, arXiv:2310.20447 (2023).

[13] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, et al., Deep Learning Scaling is Predictable, Empirically, arXiv:1712.00409 (2017).

[14] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, et al., Scaling Laws for Neural Language Models, arXiv:2001.08361 (2020).

[15] E. Dobriban, S. Wager, High-dimensional asymptotics of prediction: Ridge regression and classification, The Annals of Statistics 46 (2018), 247-279. https://doi.org/10.1214/17-AOS1549.

[16] T. Hastie, A. Montanari, S. Rosset, R. J. Tibshirani, Surprises in high-dimensional ridgeless least squares interpolation, The Annals of Statistics 50 (2022), 949-986. https://doi.org/10.1214/21-AOS2133.

[17] F. Bach, High-Dimensional Analysis of Double Descent for Linear Regression with Random Projections, SIAM Journal on Mathematics of Data Science 6 (2024), 26-50. https://doi.org/10.1137/23M1558781.

[18] Alexander Atanasov, Jacob A. Zavatone-Veth, Cengiz Pehlevan, Scaling and renormalization in high-dimensional regression, arXiv:2405.00592 (2024).

[19] Blake Bordelon, Abdulkadir Canatar, Cengiz Pehlevan, Spectrum Dependent Learning Curves in Kernel Regression and Wide Neural Networks, arXiv:2002.02561 (2020).

[20] A. Canatar, B. Bordelon, C. Pehlevan, Spectral bias and task-model alignment explain generalization in kernel regression and infinitely wide neural networks, Nature Communications 12 (2021), 2914. https://doi.org/10.1038/s41467-021-23103-1.

[21] S. Spigler, M. Geiger, M. Wyart, Asymptotic learning curves of kernel methods: empirical data versus teacher–student paradigm, Journal of Statistical Mechanics: Theory and Experiment 2020 (2020), 124001. https://doi.org/10.1088/1742-5468/abc61d.

[22] B. Loureiro, C. Gerbelot, H. Cui, S. Goldt, F. Krzakala, M. Mézard, et al., Learning curves of generic features maps for realistic datasets with a teacher-student model*, Journal of Statistical Mechanics: Theory and Experiment 2022 (2022), 114001. https://doi.org/10.1088/1742-5468/ac9825.

[23] P. Craven, G. Wahba, Smoothing noisy data with spline functions, Numerische Mathematik 31 (1978), 377-403. https://doi.org/10.1007/BF01404567.

[24] Arthur Jacot, Berfin Şimşek, Francesco Spadaro, Clément Hongler, Franck Gabriel, Kernel Alignment Risk Estimator: Risk Prediction from Training Data, arXiv:2006.09796 (2020).

[25] Alexander Wei, Wei Hu, Jacob Steinhardt, More Than a Toy: Random Matrix Models Predict How Real-World Neural Representations Generalize, arXiv:2203.06176 (2022).

[26] l. E. Frank, J. H. Friedman, A Statistical View of Some Chemometrics Regression Tools, Technometrics 35 (1993), 109-135. https://doi.org/10.1080/00401706.1993.10485033.

[27] A. E. Hoerl, R. W. Kennard, Ridge Regression: Biased Estimation for Nonorthogonal Problems, Technometrics 12 (1970), 55-67. https://doi.org/10.1080/00401706.1970.10488634.

[28] D. B. Rubin, The Bayesian Bootstrap, The Annals of Statistics 9 (1981), 130-134. https://doi.org/10.1214/aos/1176345338.

[29] J. L. Safanelli, T. Hengl, L. L. Parente, R. Minarik, D. E. Bloom, K. Todd-Brown, et al., Open Soil Spectral Library (OSSL): Building reproducible soil calibration models through open development and community engagement, PLOS ONE 20 (2025), e0296545. https://doi.org/10.1371/journal.pone.0296545.

[30] J. Sanderman, K. Savage, S. R. Dangal, Mid‐infrared spectroscopy for prediction of soil health indicators in the United States, Soil Science Society of America Journal 84 (2020), 251-261. https://doi.org/10.1002/saj2.20009.

[31] N. Anderson, K. Walsh, P. Subedi, C. Hayes, Achieving robustness across season, location and cultivar for a NIRS model for intact mango fruit dry matter content, Postharvest Biology and Technology 168 (2020), 111202. https://doi.org/10.1016/j.postharvbio.2020.111202.

[32] N. Anderson, K. Walsh, P. Subedi, J. Walsh, Mango DMC and NIR spectra, Mendeley Data (2026). https://doi.org/10.17632/46htwnp833.6.

[33] C. Borggaard, H. H. Thodberg, Optimal minimal neural interpretation of spectra, Analytical Chemistry 64 (1992), 545-551. https://doi.org/10.1021/ac00029a018.

[34] R. J. Barnes, M. S. Dhanoa, S. J. Lister, Standard Normal Variate Transformation and De-Trending of Near-Infrared Diffuse Reflectance Spectra, Applied Spectroscopy 43 (1989), 772-777. https://doi.org/10.1366/0003702894202201.

[35] S. Kapoor, A. Narayanan, Leakage and the reproducibility crisis in machine-learning-based science, Patterns 4 (2023), 100804. https://doi.org/10.1016/j.patter.2023.100804.

[36] B. S. Dayal, J. F. MacGregor, Improved PLS algorithms, Journal of Chemometrics 11 (1997), 73-85. https://doi.org/10.1002/(SICI)1099-128X(199701)11:1<73::AID-CEM435>3.0.CO;2-#.

[37] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of Data by Simplified Least Squares Procedures., Analytical Chemistry 36 (1964), 1627-1639. https://doi.org/10.1021/ac60214a047.

[38] R. W. Kennard, L. A. Stone, Computer Aided Design of Experiments, Technometrics 11 (1969), 137-148. https://doi.org/10.1080/00401706.1969.10490666.

[39] F. Wilcoxon, Individual Comparisons by Ranking Methods, Biometrics Bulletin 1 (1945), 80. https://doi.org/10.2307/3001968.

[40] D. S. Kerby, The Simple Difference Formula: An Approach to Teaching Nonparametric Correlation, Comprehensive Psychology 3 (2014), 11.IT.3.1. https://doi.org/10.2466/11.IT.3.1.
