# 1. Introduction

Multivariate calibration of near-infrared (NIR), mid-infrared (MIR) and visible–near-infrared (VisNIR) spectra is the workhorse of rapid quantitative analysis in agriculture, food, fuels, pharmaceuticals and soil science [@wold2001; @westad2015]. Once a calibration exists, a measurement costs seconds; building it does not. Every calibration sample needs a reference value from a slower and more expensive primary method — oven drying, combustion analysis, wet chemistry or chromatographic assay — and this cost usually dominates the development budget. Analysts therefore face a recurring planning question before most of the reference work is done: *how many calibration samples are needed to reach a target prediction error, and is that target achievable at all with a linear calibration?* Current guidance is largely heuristic, for example minimum sample numbers expressed relative to model complexity, or experience from related applications. Formal minimum-sample-size criteria developed for low-dimensional clinical prediction models, which limit overfitting and optimism under linear-Gaussian assumptions, have only recently been transferred to chemometrics [@riley2020; @konstantinidis2025]. They bound overfitting at a given size but do not predict how the error of a high-dimensional spectral calibration decreases as samples are added. Empirical studies in soil spectroscopy show that accuracy keeps improving well beyond a few hundred samples before levelling off [@ng2020; @kuang2014; @luca2017], but such curves are observed only after the data have been collected.

A learning curve — prediction error as a function of calibration size — answers the planning question if it can be forecast early. The established approach, introduced to analytical chemistry for Raman classification by Ali et al. [@ali2018] and rooted in earlier work on microarray and text classification [@mukherjee2003; @figueroa2012], sub-samples a small pilot data set, fits a parametric curve such as an inverse power law and extrapolates it. Its weakness is structural: the curve shape is assumed rather than derived, and a small pilot constrains it only near the pilot size, so long extrapolations are fragile [@viering2023]. Learning-curve extrapolation is also an active topic in automated machine learning, where curves over training epochs are extrapolated with learned priors [@adriaensen2023], and empirical scaling laws are extrapolated in deep learning [@hestness2017; @kaplan2020]; none of these approaches uses the structure of spectroscopic data.

Statistical learning theory offers such structure. For ridge regression in high dimensions, "deterministic-equivalent" formulas derived with random-matrix theory predict the expected test error from two ingredients: the eigenvalue spectrum of the covariance of the inputs and the way the target signal is distributed across the corresponding eigenvectors [@dobriban2018; @hastie2022; @bach2024; @atanasov2024]. The same results explain why learning curves of kernel methods differ between tasks ("spectral bias" and "task–model alignment") [@bordelon2020; @canatar2021; @spigler2020; @loureiro2022]. These analyses are, however, *omniscient*: they explain a learning curve when the full data are available. Related estimators such as generalised cross-validation (GCV) [@craven1979] and the kernel-alignment risk estimator [@jacot2020; @wei2022] estimate the risk at the *current* sample size, not at a larger one. To our knowledge, the theory has not been turned into a forecasting tool, and it has not been exploited in chemometrics, although spectroscopy is an ideal setting for it. Ridge regression, principal-component regression and partial least squares (PLS) are closely related shrinkage estimators [@frank1993; @hoerl1970]. And unlabelled spectra are cheap, so the covariance spectrum can be estimated accurately long before many reference values exist.

This paper makes three contributions. (i) It shows on real spectroscopic data that the deterministic-equivalent risk of ridge regression reproduces empirical learning curves of ridge and PLS calibrations, and that test errors measured at different calibration sizes and penalties collapse onto a single function of the effective regularisation. (ii) It introduces *regularisation-path matching* (RPM), a forecaster that uses only a small labelled pilot set and unlabelled spectra. The exact leave-one-group-out error of ridge along its penalty path is mapped onto the theory's effective-regularisation axis; the part of the bias function that the pilot can identify is fitted with a two-parameter model; and the result is extrapolated to any calibration size with bootstrap uncertainty. (iii) It evaluates the approach without data leakage on {{n_tasks}} calibration tasks from six public sources (soils, mango fruit, diesel fuel, pharmaceutical tablets, meat and designed mixtures), against established learning-curve extrapolation methods, with a controlled simulation, ablations, robustness and distribution-shift experiments, and decision-oriented metrics. Where the approach does not help, this is reported.

# 2. Theory

## 2.1. Setting and notation

Let $\mathbf{x}\in\mathbb{R}^{p}$ denote a spectrum after sample-wise pre-processing and $y$ the reference value. A ridge calibration with an unpenalised intercept is fitted to $n$ samples,

$$
\hat{\boldsymbol\beta}_{\mu}=\arg\min_{a,\boldsymbol\beta}\;\frac{1}{n}\sum_{i=1}^{n}\left(y_i-a-\mathbf{x}_i^{\top}\boldsymbol\beta\right)^2+\mu\lVert\boldsymbol\beta\rVert^{2}, \tag{1}
$$

with penalty $\mu>0$ per sample. Let $\boldsymbol\Sigma=\sum_{k}\lambda_k\mathbf{u}_k\mathbf{u}_k^{\top}$ be the population covariance of the spectra ($\lambda_1\ge\lambda_2\ge\dots$), $\boldsymbol\beta^{*}$ the coefficient vector of the best linear predictor, $s_k=\lambda_k(\mathbf{u}_k^{\top}\boldsymbol\beta^{*})^{2}$ the target variance carried by mode $k$, and $\sigma^{2}$ the residual variance, which comprises reference-method error and any non-linearity that a linear calibration cannot capture.

## 2.2. Deterministic-equivalent risk

Random-matrix theory shows that a ridge model trained on $n$ samples behaves, in expectation, like a population ridge with a larger *effective* penalty $\kappa$, the unique root of [@dobriban2018; @hastie2022; @atanasov2024]

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

with $w_j=1$ in the pre-registered version (RPM). In the refined version (RPM-w; Section 3.6), $w_j$ is the inverse of the delta-method variance of $\log e(\mu_j)$, estimated from the pilot's own squared LOGO residuals. The forecast is $\widehat{\mathrm{RMSE}}(n)=\{\min_{\mu}E_{\hat{\boldsymbol\theta}}(n,\mu)\}^{1/2}$ for any $n$. Uncertainty bands are obtained with a Bayesian bootstrap of the pilot [@rubin1981]: Dirichlet weights enter the weighted ridge fit and the weighted LOGO path, Eq. (5) is refitted, and the forecasts are recomputed.

## 2.4. What a pilot can and cannot identify

A pilot identifies $N(\kappa)$ only for $\kappa\ge\kappa_{\min}(n_0)$, whereas the risk at $n>n_0$ involves $N(\kappa)$ at smaller $\kappa$. The extrapolation therefore rests on two pieces of information. The first is the unlabelled eigen-spectrum, which states *how many* modes become learnable between $\kappa_{\min}(n_0)$ and $\kappa(n)$; this is measured, not assumed. The second is the parametric form of $s_k$, which states *how much* target power those modes carry; this is assumed. No pilot, however analysed, can separate target power hidden in weak modes from irreducible noise without such an assumption. This identifiability limit is shared by every extrapolation method, and Section 4 quantifies its consequences. Empirical curve fitting, by contrast, must assume the shape of the whole curve.

# 3. Materials and methods

## 3.1. Data sets

The study uses {{n_tasks}} calibration tasks from public sources (Table 1): six soil spectral libraries from the Open Soil Spectral Library v1.3 [@safanelli2025] (ICRAF-ISRIC VisNIR and MIR, KSSL MIR and VisNIR [@sanderman2020], AfSIS-1 MIR and a handheld NeoSpectra NIR set), each with organic carbon (OC), clay, pH(H$_2$O) and cation-exchange capacity (CEC) where available; dry-matter content of 4021 mango fruits measured with a handheld Vis–SWNIR instrument [@anderson2020; @mango_data]; six properties of diesel fuels (Southwest Research Institute NIR set); the active-ingredient assay of 655 tablets from the IDRC 2002 shoot-out; fat, moisture and protein of the Tecator meat data [@borggaard1992]; and four constituents of a designed casein–glucose–lactate–moisture (CGL) mixture set. OC and CEC were log-transformed ($\log(1+y)$) because of their skewness. Libraries with restrictive licences (LUCAS; the Serbian OSSL subset) were excluded. KSSL libraries were capped at 15,000 samples, sampled by whole sites.

## 3.2. Pre-processing and leakage control

Reflectance was converted to absorbance, and all spectra were standard-normal-variate (SNV) transformed [@barnes1989] after wavelength sub-sampling to 100–220 variables (Table 1). Both operations are sample-wise, so no information passes between calibration and test samples. Replicate scans of the same physical sample were averaged before any split. This applies to the two cheek scans of each mango fruit (fruit identity was reconstructed from metadata and validated by spectral distance), to duplicate KSSL scans, and to the multi-instrument NeoSpectra measurements, for which the instrument-averaged spectrum was used. Soil layers from the same site or profile were assigned to the same group. Every split is group-disjoint, and every cross-validation, inside pilots and inside ground-truth fits, leaves out whole groups [@kapoor2023]. Unlabelled spectra used by RPM were taken only from the calibration pool, never from the test set. Supplementary Table S1 documents the full leakage audit.

## 3.3. Ground-truth learning curves

For each task, a group-disjoint test set (25% of samples, at most 3000) was held out once, using a seed derived from the task name. The remaining samples form the pool. For $n\in\{50,100,200,400,800,1600,3200,6400\}$ (up to the pool size), $n$ pool samples were drawn at random, and two calibrations were fitted. The first was ridge, with the penalty chosen by exact LOGO cross-validation over a 53-point grid. The second was PLS1 (kernel algorithm [@dayal1997]), with 1–30 latent variables chosen by grouped 10-fold cross-validation. The test MSE of each was recorded. The expected curve was estimated from 30 ($n\le400$), 16 ($n\le1600$) or 8 repetitions.

## 3.4. Pilot forecasting protocol

For pilot sizes $n_0\in\{25,50,100,200\}$, 20 pilots per task were drawn at random from the pool with predefined seeds. Each forecaster received only the pilot (spectra, reference values, group labels) and, for RPM, the unlabelled pool spectra. It forecast the test RMSE at every grid size $n\ge2n_0$. The primary endpoint is the absolute log-ratio $|\log(\widehat{\mathrm{RMSE}}/\mathrm{RMSE}_{\mathrm{true}})|$ against the ridge ground truth, averaged within each task. Secondary endpoints are the same against the PLS ground truth, the signed bias, the proportion of forecasts within ±10% and ±20%, the empirical coverage of 80% and 95% bands, and a sample-size decision metric. For the decision metric, the target RMSE is the true RMSE at $n^{*}=4n_0$ or $16n_0$, each method's forecast curve (anchored at the pilot's cross-validated error) gives the size $\hat n$ at which the target is reached, and a decision counts as correct if $\hat n$ lies within a factor of two of $n^{*}$.

## 3.5. Baselines

All baselines use the same ridge calibration and the same pilot.

- **IPL3**: an inverse power law with asymptote, $e(m)=a+bm^{-c}$, as used by Ali et al. [@ali2018] following [@mukherjee2003; @figueroa2012]. It is fitted by weighted non-linear least squares to a within-pilot learning curve, obtained by training on 25–85% of the pilot (20 group-disjoint splits per fraction, validated on the remainder) plus the full-pilot cross-validated error; intervals come from the delta method.
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

**Robustness (E7).** Six representative tasks were rerun with raw absorbance and Savitzky–Golay first-derivative spectra [@savitzky1964], with Kennard–Stone-selected pilots [@kennard1969], and with Gaussian noise added to the reference values (variance 25% of $\mathrm{var}(y)$). Mango was additionally evaluated under two distribution shifts: a new harvest season (calibration on seasons 1–3, test on season 4), with an i.i.d. reference split of the same size, and orchard-population-grouped splits.

## 3.7. Statistical analysis

The task is the unit of analysis. RPM was compared with each baseline using two-sided Wilcoxon signed-rank tests on per-task mean errors [@wilcoxon1945], with Holm correction across the baselines. Effect sizes are the median paired difference, with a 95% bootstrap confidence interval (10,000 resamples of tasks), and the matched-pairs rank-biserial correlation [@kerby2014]. Results are also stratified by pilot size, extrapolation ratio and data-set family. A sensitivity analysis excluded the four ICRAF-VisNIR tasks, which had been used in exploratory work before the design was frozen.

## 3.8. Implementation and reproducibility

All methods were implemented in Python (NumPy, SciPy, pandas, scikit-learn). The closed-form LOGO ridge path, the PLS1 implementation and the theory were unit-tested against brute-force refits, scikit-learn and Monte-Carlo simulation. A single command (`run_all.py`) downloads nothing silently, runs all experiments with deterministic seeds and regenerates every table, figure and number from machine-readable outputs. Computations ran on a 4-core CPU without a GPU.
