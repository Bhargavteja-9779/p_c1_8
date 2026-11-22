# What a pilot set can tell about a calibration learning curve: an observability limit and Bayesian regularisation-path matching for sample-size planning in spectroscopy

[Author 1]^a^, [Author 2]^a,\*^

^a^ [Department, Institution, City, Country]

\* Corresponding author: [name, e-mail]

## Abstract

**Background:** Multivariate calibrations of NIR and MIR spectra need costly reference analyses, and analysts must decide from a small pilot set whether more samples will pay off. Learning-curve extrapolation is used for this decision, but it is unknown which part of a learning curve a pilot can determine.

**Results:** The deterministic-equivalent (random-matrix) risk of ridge regression reproduced ridge and PLS learning curves of 38 public NIR/MIR calibration tasks (mean absolute log error 0.130 and 0.153). From it we prove that a pilot observes the calibration's bias function only above an effective-regularisation horizon. Analyte signal below the horizon is indistinguishable from noise, so the gain from more samples cannot be identified from a pilot alone. A computable compatible set of curves consistent with the pilot contained the true RMSEP in 91% of forecasts (whole curves 86%; 99% in simulation) but spanned a factor of 15 in RMSEP at eightfold extrapolation. Bayesian regularisation-path matching (B-RPM) makes the unavoidable prior explicit. It forecast gains better than the no-improvement rule and power-law extrapolation and kept its accuracy with a prior from another application family (0.292 vs 0.392 for a transferred slope). On the RMSEP level, however, the pilot's own cross-validated error stayed best (0.262 vs 0.282), and three of four pre-specified hypotheses failed. A second batch raised the accuracy of reachability decisions by 4–10 percentage points for every method.

**Significance:** Every pilot-based learning-curve forecast rests on prior information that the pilot cannot supply. Sample-size decisions that depend on the future gain should be staged, and forecasts should state their prior and their compatible set.

**Keywords:** Multivariate calibration; Sample-size planning; Learning curve; Identifiability; Bayesian forecasting; Near-infrared spectroscopy


# 1. Introduction

Multivariate calibration of near-infrared (NIR), mid-infrared (MIR) and visible–near-infrared (VisNIR) spectra is the workhorse of rapid quantitative analysis in agriculture, food, fuels, pharmaceuticals and soil science [1,2]. Once a calibration exists, a measurement costs seconds; building it does not. Every calibration sample needs a reference value from a slower and more expensive primary method — oven drying, combustion analysis, wet chemistry or chromatographic assay — and this cost usually dominates the development budget. Analysts therefore face a recurring planning question before most of the reference work is done: *how many calibration samples are needed to reach a target prediction error, and is that target achievable at all with a linear calibration?* Current guidance is largely heuristic, for example minimum sample numbers expressed relative to model complexity, or experience from related applications. Formal minimum-sample-size criteria developed for low-dimensional clinical prediction models, which limit overfitting and optimism under linear-Gaussian assumptions, have only recently been transferred to chemometrics [3,4]. They bound overfitting at a given size but do not predict how the error of a high-dimensional spectral calibration decreases as samples are added. Empirical studies in soil spectroscopy show that accuracy keeps improving well beyond a few hundred samples before levelling off [5–7], but such curves are observed only after the data have been collected.

A learning curve — prediction error as a function of calibration size — answers the planning question if it can be forecast early. The established approach, introduced to analytical chemistry for Raman classification by Ali et al. [8] and rooted in earlier work on microarray and text classification [9,10], sub-samples a small pilot data set, fits a parametric curve such as an inverse power law and extrapolates it. Its weakness is structural: the curve shape is assumed rather than derived, and a small pilot constrains it only near the pilot size, so long extrapolations are fragile [11]. Learning-curve extrapolation is also an active topic in automated machine learning, where curves over training epochs are extrapolated with learned priors [12], and empirical scaling laws are extrapolated in deep learning [13,14]; none of these approaches uses the structure of spectroscopic data.

Statistical learning theory offers such structure. For ridge regression in high dimensions, "deterministic-equivalent" formulas derived with random-matrix theory predict the expected test error from two ingredients: the eigenvalue spectrum of the covariance of the inputs and the way the target signal is distributed across the corresponding eigenvectors [15–18]. The same results explain why learning curves of kernel methods differ between tasks ("spectral bias" and "task–model alignment") [19–22]. These analyses are, however, *omniscient*: they explain a learning curve when the full data are available. Related estimators such as generalised cross-validation (GCV) [23] and the kernel-alignment risk estimator [24,25] estimate the risk at the *current* sample size, not at a larger one. Wei et al. [25] used these estimators to predict how the error of trained neural representations scales with the number of samples, and Beleites et al. [26] showed in this journal that the test sets of small classification studies are too small to estimate performance reliably, let alone its future improvement. No study has asked which part of a calibration learning curve a pilot set can determine at all. The question matters because planning methods are judged by how well they extrapolate, and a method that extrapolates well on one application can fail on another for reasons that remain invisible without such an analysis. Spectroscopy is a good setting in which to answer it. Ridge regression, principal-component regression and partial least squares (PLS) are closely related shrinkage estimators [27–29], and unlabelled spectra are cheap, so the covariance spectrum can be estimated accurately long before many reference values exist.

This paper makes three contributions. (i) **An observability limit.** We prove that a pilot of $n_0$ samples observes the bias function of a ridge calibration only above an effective-regularisation horizon set by $n_0$ and the eigen-spectrum; target signal carried by spectral modes below that horizon is indistinguishable from irreducible noise in the pilot, yet it is learned when the calibration grows (Proposition 1). The gain from adding samples is therefore not identifiable from a pilot alone, and every forecaster, including power-law extrapolation and the no-improvement rule, implicitly supplies a prior. The corollary is a computable, prior-free *compatible set* of learning curves consistent with the pilot, and an *information fraction* that measures how much the pilot adds to the prior about the future gain. (ii) **Bayesian regularisation-path matching (B-RPM).** Instead of assuming a curve shape, B-RPM places a transferable prior on two structural parameters of the deterministic-equivalent risk, the alignment exponent and the noise fraction, learned from previous calibrations of other materials. It combines this prior with the pilot's exact leave-one-group-out regularisation path and the eigen-spectrum of the task's own unlabelled spectra, and returns a posterior-predictive learning curve in a fraction of a second. (iii) **A leakage-free benchmark on 38 calibration tasks** from six public sources (soils, mango fruit, diesel fuel, pharmaceutical tablets, meat and designed mixtures). It includes a pre-registered first design, a pre-specified evaluation of B-RPM (hypotheses fixed before results were seen), a controlled simulation, group-disjoint repeated splits and the strictest transfer test available, in which priors come from a different application family. The main results are as follows. The theory reproduces ridge and PLS learning curves. The compatible set contains the true curve in about nine of ten cases, but it is wide at long horizons. B-RPM predicts gains better than power-law extrapolation and the no-improvement rule and keeps its accuracy when its prior comes from a different application family, whereas a transferred empirical slope does not. No forecaster beats the pilot's own cross-validated error on the RMSEP level, and a second batch of samples improves sample-size decisions more than any choice of forecaster.

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

with $w_j=1$ in the pre-registered version (RPM). In the refined version (RPM-w; Section 3.6), $w_j$ is the inverse of the delta-method variance of $\log e(\mu_j)$, estimated from the pilot's own squared LOGO residuals. The forecast is $\widehat{\mathrm{RMSE}}(n)=\{\min_{\mu}E_{\hat{\boldsymbol\theta}}(n,\mu)\}^{1/2}$ for any $n$. Uncertainty bands are obtained with a Bayesian bootstrap of the pilot [30]: Dirichlet weights enter the weighted ridge fit and the weighted LOGO path, Eq. (5) is refitted, and the forecasts are recomputed.

## 2.4. What a pilot set can identify: the observability horizon

Write the deterministic-equivalent risk as $E(n,\mu)=P(n,\kappa)\,N(\kappa)$ with $\kappa=\kappa(n,\mu)$ (Eqs. 1–4). For a pilot of $n_0<\mathrm{rank}(\Sigma)$ samples, $\kappa(n_0,\mu)$ decreases to a strictly positive limit $\kappa_0=\lim_{\mu\to0}\kappa(n_0,\mu)$, the root of $\sum_k\lambda_k/(\lambda_k+\kappa_0)=n_0$, as the penalty vanishes. Even an infinitely repeated pilot of size $n_0$, observed at every penalty, therefore reveals the bias function $N(\kappa)$ only on the half-line $\kappa\ge\kappa_0$. We call $\kappa_0$ the *observability horizon* of the pilot. Modes with $\lambda_k\gg\kappa_0$ are resolved by the pilot; modes with $\lambda_k\ll\kappa_0$ are not.

**Proposition 1 (non-identifiability of the gain).** Let $(s,\sigma^2)$ be a target-power spectrum and noise variance, let $T$ be any set of modes with $\lambda_k\le\delta\kappa_0$ for some $\delta>0$, and let $S_T=\sum_{k\in T}s_k$. Define the alternative model $(s',\sigma'^2)$ with $s'_k=0$ for $k\in T$, $s'_k=s_k$ otherwise, and $\sigma'^2=\sigma^2+S_T$. Then

(a) for every penalty, the risk of a pilot of size $n_0$ differs between the two models by at most
$$0\le E'(n_0,\mu)-E(n_0,\mu)\le 2\delta\,S_T\,P(n_0,\kappa),\qquad(6)$$
i.e. by a relative amount of at most $2\delta S_T/N(\kappa_0)$;

(b) at a calibration size $n$ and any penalty for which $\kappa_n=\kappa(n,\mu)\le\delta'\min_{k\in T}\lambda_k$, the risks differ by at least
$$E'(n,\mu)-E(n,\mu)\ \ge\ (1-\delta'^2)\,S_T\,P(n,\kappa_n)\ \ge\ (1-\delta'^2)\,S_T.\qquad(7)$$

*Proof.* $N'(\kappa)-N(\kappa)=\sum_{k\in T}s_k\,[1-\kappa^2/(\lambda_k+\kappa)^2]=\sum_{k\in T}s_k\,\lambda_k(\lambda_k+2\kappa)/(\lambda_k+\kappa)^2$. Each summand lies in $[0,2\lambda_k/\kappa]$, because $\kappa\lambda_k(\lambda_k+2\kappa)\le2\lambda_k(\lambda_k+\kappa)^2$ for all $\lambda_k,\kappa\ge0$. For $\kappa\ge\kappa_0$ and $\lambda_k\le\delta\kappa_0$ this gives $0\le N'-N\le2\delta S_T$. The prefactor $P(n,\kappa)$ depends only on the eigenvalues, not on $(s,\sigma^2)$, and $\kappa(n,\mu)$ does not depend on them either; multiplying by $P(n_0,\kappa)$ gives (a). For (b), $\kappa_n/(\lambda_k+\kappa_n)\le\kappa_n/\lambda_k\le\delta'$ for $k\in T$, so each summand is at least $s_k(1-\delta'^2)$, and $P\ge1$. $\square$

Because $N'\ge N$ everywhere, the alternative model is also never better at its own optimal penalty, and in the numerical examples of Section 4.2 the difference in optimal risk is of the same order as $S_T$.

In words: target power hidden below the observability horizon looks like irreducible noise in the pilot's regularisation path (to first order in $\lambda_k/\kappa_0$), yet it is learned once the calibration is large enough for $\kappa_n$ to pass below those eigenvalues. The statement concerns the expected cross-validation path, which is the only information used by path-matching methods and, through the within-pilot learning curve, by curve extrapolation. Sampling noise in a cross-validated path (relative standard deviation of order $(2/n_0)^{1/2}$) makes the two models practically indistinguishable whenever $2\delta S_T/N(\kappa_0)$ is smaller than that noise. Because the gain from $n_0$ to $n$ is essentially the target power in the band $\kappa_n\lesssim\lambda_k\lesssim\kappa_0$, **a forecaster based on the pilot's error path cannot predict the gain without an assumption about how target power is distributed below the horizon.** Every published learning-curve extrapolation makes that assumption implicitly. The no-improvement rule assumes no power below the horizon. Inverse-power-law fits assume that the within-pilot trend continues. RPM with $r=1$ assumes power proportional to the eigenvalue, which puts almost none below the horizon. Estimators that use the full pilot data rather than its error path, such as the method-of-moments and EigenPrism estimators of the noise variance [31,32], can in principle separate signal from noise without a prior on the signal. However, under a Gaussian design with known covariance, their standard error grows with $\sqrt{p}/n_0$, which is large for spectra with $p\gg n_0$. In our data such an estimator did not prevent noise-floor collapse (variant RPM-TD, Table 2). That weak modes act as effective noise for a given sample size is known from the theory of learning curves [16,20]. What Proposition 1 adds is the consequence for forecasting: it locates the horizon for a given pilot and turns it into a statement about the gain that a planner can check.

**Corollary (compatible set).** For a given parametric family of target-power spectra, the parameters whose predicted path is consistent with the observed pilot path, up to the sampling noise of the path, define a *compatible set* of learning curves. It is computable from the pilot and the unlabelled spectra alone. It is not an identification region in the strict sense: within a parametric family the parameters are identified in the noiseless limit, so the set's width reflects the precision that a pilot of size $n_0$ allows together with the bounds of the family. We report it for the family $s_k\propto(\lambda_k/\lambda_1)^r$, $r\in[0.05,1.6]$, with noise fraction $\eta\in[5\times10^{-4},0.97]$ (Section 2.5). In chemometric terms, $\kappa_0$ is the eigenvalue level at which a ridge model fitted to the pilot uses all $n_0$ effective degrees of freedom. Spectral directions whose variance lies well above it, roughly the leading principal components, are resolved by the pilot; directions well below it are not.

## 2.5. Bayesian regularisation-path matching (B-RPM)

Proposition 1 tells us where information must come from: the distribution of target power below the observability horizon. B-RPM supplies it as an explicit, transferable prior on *structural* parameters rather than on curve shapes. The bias function is parametrised as
$$N(\kappa)=V\left[\eta+(1-\eta)\,b_r(\kappa)\right],\qquad b_r(\kappa)=\frac{\sum_k(\lambda_k/\lambda_1)^r\,\kappa^2/(\lambda_k+\kappa)^2}{\sum_k(\lambda_k/\lambda_1)^r},\qquad(8)$$
where $V$ is the total variance ($N(\infty)=V$), $\eta$ the irreducible-noise fraction and $r$ the alignment exponent; the eigenvalues $\lambda_k$ are those of the task's own unlabelled spectra. The prior is Gaussian in $r$ and in $\mathrm{logit}\eta$, with location and scale (median and $1.4826\times$ median absolute deviation) taken from large-sample fits of previous calibrations, here all tasks of *other* data sources (leave-one-source-out) or, in a stricter test, of other application families. The likelihood is built from the pilot's exact leave-one-group-out path: log CV-MSE residuals have the delta-method variance of the log CV-MSE at the pilot optimum, and path points carry $\kappa$-quadrature weights scaled to $m_{\mathrm{eff}}=2$ effective observations (the level and the curvature of the path, since all points reuse the same residuals); $V$ is profiled out. The posterior on a $32\times40$ grid of $(r,\eta)$ is combined with the deterministic-equivalent optimal risk at every horizon to give a posterior-predictive distribution of $\log\mathrm{RMSEP}(n)$, to which the anchor uncertainty is added. All $\kappa$-dependent terms do not depend on $(r,\eta,V)$ and are precomputed, so a complete forecast with bands takes about 0.2 s. Two by-products are reported for every pilot: the prior-free compatible set (Corollary) and the *information fraction* $1-\mathrm{var}_{\mathrm{post}}(\text{gain})/\mathrm{var}_{\mathrm{prior}}(\text{gain})$, which measures how much the pilot itself adds to the prior about the future gain.

Fig. 1 summarises the workflow. B-RPM was specified, implemented and committed to the project repository before any forecast of the final re-analysis was inspected, with hypotheses HB1–HB4 fixed in advance (Supplementary Material, B-RPM addendum).

![**Fig. 1.** Workflow of Bayesian regularisation-path matching. The unlabelled spectra fix the eigen-spectrum and hence the observability horizon of the pilot; the pilot's exact leave-one-group-out path is the likelihood; previous calibrations of other materials supply the structural prior. Outputs are the prior-free compatible set, the posterior-predictive learning curve and the information fraction.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig1_workflow.png){width=16cm}

# 3. Materials and methods

## 3.1. Data sets

The study uses 38 calibration tasks from public sources (Table 1): six soil spectral libraries from the Open Soil Spectral Library v1.3 [33] (ICRAF-ISRIC VisNIR and MIR, KSSL MIR and VisNIR [34], AfSIS-1 MIR and a handheld NeoSpectra NIR set), each with organic carbon (OC), clay, pH(H$_2$O) and cation-exchange capacity (CEC) where available; dry-matter content of 4021 mango fruits measured with a handheld Vis–SWNIR instrument [35,36]; six properties of diesel fuels (Southwest Research Institute NIR set); the active-ingredient assay of 655 tablets from the IDRC 2002 shoot-out; fat, moisture and protein of the Tecator meat data [37]; and four constituents of a designed casein–glucose–lactate–moisture (CGL) mixture set. OC and CEC were log-transformed ($\log(1+y)$) because of their skewness. Libraries with restrictive licences (LUCAS; the Serbian OSSL subset) were excluded. KSSL libraries were capped at 15,000 samples, sampled by whole sites.

## 3.2. Pre-processing and leakage control

Reflectance was converted to absorbance, and all spectra were standard-normal-variate (SNV) transformed [38] after wavelength sub-sampling to 94–216 variables (Table 1). Both operations are sample-wise, so no information passes between calibration and test samples. Replicate scans of the same physical sample were averaged before any split. This applies to the two cheek scans of each mango fruit (fruit identity was reconstructed from metadata and validated by spectral distance), to duplicate KSSL scans, and to the multi-instrument NeoSpectra measurements, for which the instrument-averaged spectrum was used. Soil layers from the same site or profile were assigned to the same group. Every split is group-disjoint, and every cross-validation, inside pilots and inside ground-truth fits, leaves out whole groups [39]. Unlabelled spectra used by RPM and B-RPM were taken only from the calibration pool, never from the test set. Supplementary Note 3 documents the full leakage audit.

## 3.3. Ground-truth learning curves

For each task, a group-disjoint test set (25% of samples, at most 3000) was held out using a seed derived from the task name; the remaining samples form the pool. Tasks with fewer than 1000 samples (fuel, tablets, meat, mixtures) were evaluated over ten independent group-disjoint outer splits, so that their ground truth does not rest on one small test set. For $n\in\{25,50,100,200,400,800,1600,3200,6400\}$ (up to the pool size), $n$ pool samples were drawn at random, and two calibrations were fitted. The first was ridge, with the penalty chosen by exact LOGO cross-validation over a 53-point grid. The second was PLS1 (kernel algorithm [40]), with 1–30 latent variables chosen by grouped 10-fold cross-validation. The test MSE of each was recorded. The expected curve was estimated from 30 ($n\le400$), 16 ($n\le1600$) or 8 repetitions.

## 3.4. Pilot forecasting protocol

For pilot sizes $n_0\in\{25,50,100,200\}$, pilots were drawn at random from the pool with predefined seeds: 20 per task for the large libraries and 10 per outer split for the small data sets. Each forecaster received only the pilot (spectra, reference values, group labels), the unlabelled pool spectra and, where stated, information from *other* data sources. It forecast the test RMSEP at every grid size $n\ge2n_0$. The level endpoint is the absolute log ratio $|\log(\widehat{\mathrm{RMSEP}}/\mathrm{RMSEP}_{\mathrm{true}})|$ against the ridge ground truth; the gain endpoint is the absolute error of the forecast gain, $|\log(\widehat{\mathrm{RMSEP}}(n)/\widehat{\mathrm{RMSEP}}_{\mathrm{pilot}})-\log(\mathrm{RMSEP}_{\mathrm{true}}(n)/\mathrm{RMSEP}_{\mathrm{true}}(n_0))|$, which removes the noise of the pilot's own error estimate. Both are averaged within tasks (over splits, pilots, pilot sizes and horizons), so that every task counts once. Secondary endpoints are the signed bias by extrapolation ratio, the coverage and width of 80% and 95% bands, the coverage and width of the compatible set, and the Brier score of the probabilistic decision "an eightfold larger calibration set reduces RMSEP by at least 15%".

## 3.5. Forecasters

All forecasters use the same ridge calibration and the same pilot.

- **B-RPM** (Section 2.5), with the prior learned leave-one-source-out (LOSO) from the large-sample fits of the other data sources (sources defined by sample provenance; KSSL and NeoSpectra form one source), and **B-RPM-LOFO**, with the prior learned from other *application families* only. Ablations: prior on $r$ only (B-RPM-r), prior only without the pilot path (B-RPM-0) and $m_{\mathrm{eff}}=10$ (B-RPM-m10).
- **RPM** ($r=1$; the pre-registered method of the first design, Section 2.3), and its post-hoc variants with a transferred exponent (RPM-T) and noise floors (RPM-TD with the Dicker estimator [31]; RPM-TP with a transferred lower bound).
- **IPL3**, an inverse power law with asymptote, $e(m)=a+bm^{-c}$, as used by Ali et al. [8] following [9,10], fitted by weighted non-linear least squares to a within-pilot learning curve (training on 25–85% of the pilot, 20 group-disjoint splits per fraction) plus the full-pilot cross-validated error; **IPL2**, a pure power law; **EXP3** and **LOG2**, exponential and logarithmic curves.
- **WEI**, the scaling exponent of Wei et al. [25], estimated from the unlabelled eigen-decay and the pilot's regularisation path and anchored at the pilot error.
- **FLAT**, the pilot's cross-validated error (no improvement), and **DF-OLS**, a classical fixed-complexity formula.
- **SLOPE-T**, the pilot's cross-validated error extrapolated with the median ground-truth slope per doubling of $n$ of the other data sources, and **SLOPE-T-LOFO**, with the slope of other application families.

## 3.6. Design history, simulation and robustness

The study has three stages, all documented in a time-stamped experiment log. (1) The first design (RPM, baselines, ablations) was pre-registered before any result was seen. (2) After an internal audit, the whole study was re-run with corrected soil groups, repeated outer splits for small data sets, provenance-based sources, a $\kappa$-quadrature weighting of the path fit and floor-free curve bands; first-version outputs are archived unchanged. (3) B-RPM, the compatible set and the hypotheses HB1–HB4 were specified and committed before any version-2 forecast was inspected: HB1, B-RPM-LOFO has a lower gain error than SLOPE-T-LOFO; HB2, B-RPM is non-inferior to FLAT on the level endpoint (margin 0.02); HB3, the 80% bands of B-RPM cover 70–90% in every family and pilot-size stratum; HB4, the compatible set contains the truth in at least 90% of cases. The leave-one-source-out recalibration of the B-RPM bands (Section 4.6) was added after HB3 had failed and is labelled post hoc.

**Simulation.** Gaussian spectra with $\lambda_k=k^{-1.6}$ ($p=150$), alignment $r\in\{0.5,1,2\}$ and noise fractions 0.1 and 0.3 were simulated; the ground truth is the Monte-Carlo test error of LOO-tuned ridge (30 repetitions, 4000 test samples), not the theory. B-RPM was given the real-data prior, which is approximately correct for $r=0.5$ and wrong for $r=2$.

**Robustness.** Six representative tasks were rerun with raw-absorbance and Savitzky–Golay first-derivative spectra [41], Kennard–Stone-selected pilots [42] and Gaussian noise added to the reference values (variance 25% of $\mathrm{var}(y)$). Mango was also evaluated under a new harvest season (calibration on seasons 1–3, test on season 4, with an i.i.d. reference split of the same size) and with orchard populations held out.

## 3.7. Statistical analysis

The task is the unit of analysis. The pre-specified hypotheses HB1–HB4 are confirmatory and are reported with unadjusted p-values and confidence intervals; all other comparisons are exploratory. Paired comparisons use two-sided Wilcoxon signed-rank tests on per-task means [43], with Holm correction over the comparisons of a table, and 95% bootstrap confidence intervals of the mean paired difference (4000 resamples of tasks). Because tasks share spectra within a source, every comparison is repeated at the level of the eight data sources (means over the tasks of a source); both levels are reported.

## 3.8. Implementation and reproducibility

All methods were implemented in Python (NumPy, SciPy, pandas, scikit-learn). The closed-form LOGO ridge path, the PLS1 implementation and the theory were unit-tested against brute-force refits, scikit-learn and Monte-Carlo simulation. A single command (`run_all.py`) downloads nothing silently, runs all experiments with deterministic seeds and regenerates every table, figure and number from machine-readable outputs. Computations ran on a 4-core CPU without a GPU.


# 4. Results and discussion


**Table 1.** Calibration tasks. ICRAF, KSSL, AfSIS1 and Neospectra are soil spectral libraries; Mango: fruit dry matter; Diesel: fuel properties; Tablets: pharmaceutical assay; Tecator: meat; CGL: designed casein–glucose–lactate–moisture mixtures. N = samples after replicate averaging (pool + group-disjoint test set); p = spectral variables after sub-sampling; max. n = largest calibration size in the ground-truth curve.

| Library | Spectral range | Properties | Tasks | N per task | p | Max. n (truth) |
|:---------------------------------------------|:--------------------------------------------------------|:-------------------------------------------------------|---------------------:|-------------------------------------------:|-------------:|----------------------------:|
| ICRAF-VisNIR | VisNIR 400–2480 nm | OC, clay, pH, CEC | 4 | 3,654⁠–⁠3,776 | 208 | 1,600 |
| ICRAF-MIR | MIR 4000–600 cm⁻¹ | OC, clay, pH, CEC | 4 | 3,652⁠–⁠3,774 | 212 | 1,600 |
| KSSL-MIR | MIR 4000–600 cm⁻¹ | OC, clay, pH, CEC | 4 | 15,000⁠–⁠15,003 | 212 | 6,400 |
| KSSL-VisNIR | VisNIR 400–2480 nm | OC, clay, pH, CEC | 4 | 15,000⁠–⁠15,011 | 208 | 6,400 |
| AfSIS1-MIR | MIR 4000–600 cm⁻¹ | OC, clay, pH | 3 | 1,896⁠–⁠1,904 | 212 | 800 |
| Neospectra-NIR | NIR 1350–2550 nm, handheld | OC, clay, pH, CEC | 4 | 2,096⁠–⁠2,106 | 150 | 800 |
| Mango | SWNIR 684–990 nm, handheld | dry matter | 1 | 4,021 | 94 | 1,600 |
| Diesel | NIR 750–1550 nm | 6 fuel properties | 6 | 381⁠–⁠395 | 200 | 200 |
| Tablets | NIR 600–1898 nm | assay | 1 | 655 | 216 | 400 |
| Tecator | NIR 850–1050 nm | fat, moisture, protein | 3 | 215 | 99 | 100 |
| CGL | NIR 1104–2495 nm | 4 constituents | 4 | 231 | 116 | 100 |


## 4.1. Calibration learning curves follow the deterministic-equivalent theory

Fig. 2a compares, for four representative tasks, the expected test RMSE of cross-validated ridge and PLS calibrations with the deterministic-equivalent curve of Eq. (3). The curve was fitted once to the cross-validation path of the full calibration pool (three parameters, $r$ free) and then evaluated at every calibration size. Across all 38 tasks, this single fit reproduced the empirical ridge learning curves with a mean absolute log error of 0.130 (median task 0.105) and the PLS curves with 0.153 (median 0.132); with $r$ fixed at 1 the errors rose to 0.198 and 0.220 (Supplementary Table S6). The largest deviations occurred for CGL:lactate (0.40), Tecator:fat (0.38), CGL:moisture (0.35): small fuel and designed-mixture sets, whose samples are not a random draw from a population, which is a premise of the theory. The structural assumption on which RPM rests — that the calibration size $n$ and the penalty $\mu$ act on the error only through the effective regularisation $\kappa$ and the prefactor of Eq. (3) — was tested directly. Empirical test errors measured at fixed penalties for calibration sizes from 50 to 6400 collapse onto a single curve once plotted against $\kappa(n,\mu)$ and rescaled (Fig. 2b). The across-$n$ standard deviation of the rescaled log-errors was 0.037 (median over 38 tasks with at least three calibration sizes), compared with 0.515 for the same errors plotted against the raw penalty.

![**Fig. 2.** Validity of the deterministic-equivalent theory. (a) Expected test RMSE of LOGO-tuned ridge and CV-tuned PLS calibrations (markers) and the theory fitted to the full-pool cross-validation path (dotted). (b) κ-collapse: empirical test MSE at fixed penalty for different calibration sizes $n$ (shades), rescaled by the theory prefactor and plotted against the effective regularisation κ.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig2_theory_validity_and_collapse.png){width=16cm}

## 4.2. Analyte signal extends into weak spectral modes, and the noise floor sets the slope

The large-sample fits also estimate the alignment exponent $r$, which describes how the analyte signal is distributed over the eigenvalues of the spectral covariance ($s_k\propto\lambda_k^{r}$). In all 38 tasks, $r$ was below 1 (median 0.55, interquartile range 0.40–0.66, range 0.32–0.88; Fig. 3). The analyte signal therefore carries more power in low-variance spectral directions than an isotropic coefficient prior ($r=1$) implies. The exponent was lowest for Vis/NIR soil and SWNIR fruit spectra (median 0.38), whose broad, overlapping overtone and combination bands and strong scattering leave the chemical information in subtle shape differences. It was higher for MIR soil spectra (median 0.59), whose fundamental vibrations concentrate the information in better-resolved, high-variance features. Because weak modes become learnable only gradually, learning curves keep improving over a wide range of $n$.

![**Fig. 3.** Alignment exponent $r$ estimated from the full calibration pool of each task (dots; bars = medians), grouped by spectral region and sample type. Dashed line: the isotropic prior $r=1$ assumed by RPM. Grey band: range of the leave-one-source-out priors used by RPM-T.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig12_alignment_exponents.png){width=11cm}

Learning curves were shallow. Fitting $\log\mathrm{RMSE}$ against $\log_2 n$ over each ground-truth curve gave a median slope of -0.097 per doubling of $n$ (interquartile range -0.144 to -0.079), i.e. a typical RMSE reduction of about 9.3% for every doubling of the calibration set. The medians for the MIR (-0.107) and Vis/NIR (-0.083) soil libraries were nearly identical despite their different alignment exponents. The steepest curves belonged to the designed CGL mixtures (-0.516) and the meat data (-0.122), whose reference noise is small. In a post-hoc regression, the large-sample theory parameters explained most of the between-task variation of the slope ($R^2$ = 0.78; Supplementary Table S7). The irreducible-noise fraction $\sigma^2/\mathrm{var}(y)$ was the dominant term (Spearman $\rho$ = +0.54, p = 0.0005; Fig. 4): the closer a calibration is to its noise floor, the less it gains from more samples. This explains why a learning curve cannot be read from its first points. Its slope is set mainly by the noise floor, and the noise floor is precisely what a small pilot cannot identify (Section 4.3).

![**Fig. 4.** Slope of the ground-truth learning curve (log RMSE per doubling of $n$) against the irreducible-noise fraction of the large-sample fit (post hoc).](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig13_slope_vs_noise.png){width=9cm}

## 4.3. What a pilot set can identify

Proposition 1 predicts that a pilot leaves the gain from additional samples undetermined unless prior information is added. The prior-free compatible set makes this measurable (Fig. 5). For every pilot it contains all learning curves of the family $s_k\propto(\lambda_k/\lambda_1)^r$ that are consistent with the pilot's cross-validation path. Across all pilots and horizons the set contained the true ridge RMSEP in 91% of forecasts (task average; pooled over forecasts 88% at $n/n_0=2$ and 98% at $n/n_0\ge32$; Fig. 6a), and the whole true curve of a pilot in 86%. In the controlled simulation, where the truth is a Monte-Carlo estimate rather than a fitted curve, coverage was 99% overall and at least 98% in every scenario. The theory therefore describes correctly what is compatible with a pilot. What a pilot can decide is a different matter. The median ratio between the upper and lower RMSEP of the set was 3.4 at $n/n_0=2$, 15 at $n/n_0=8$ and 58 at $n/n_0\ge32$ (Fig. 6b). Long extrapolations from a pilot alone are thus not merely inaccurate. They are undetermined, and any method that returns a narrow forecast does so because it has imported an assumption.

![**Fig. 5.** Learning-curve forecasts from one 50-sample pilot for three tasks. Grey: prior-free compatible set (all curves consistent with the pilot's cross-validation path, Section 2.4); blue: B-RPM posterior mean and 80% band; dotted: no-improvement rule; dashed: inverse power law (IPL3); black: true learning curve (independent test set).](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig3_identification_set_examples.png){width=16cm}

The information fraction quantifies how much of the forecast comes from the pilot rather than the prior (Fig. 6c). Its median was 0.17 for 25-sample pilots, 0.36 for 50, 0.83 for 100 and 0.95 for 200 samples. Below about 100 samples the gain forecast comes mainly from the prior. The high values at 100–200 samples partly reflect the wavelength sub-sampling to 94–216 variables: when $n_0$ approaches $p$, the horizon $\kappa_0$ falls far below the leading eigenvalues and almost all modes are resolved. For full-resolution spectra the horizon of a given pilot would be higher. The fraction is therefore largely a function of pilot size, and 20% of the values were negative (posterior spread wider than prior spread, when the pilot contradicts the prior). Within a pilot size it carried some warning value only for small pilots: B-RPM's mean absolute log error was 0.420 in the lowest and 0.313 in the highest within-size tertile at $n_0=25$ (0.327 vs 0.224 at $n_0=50$), but 0.136 vs 0.129 at $n_0=200$ (Supplementary Table S13).

![**Fig. 6.** Observability of learning curves. (a) Share of forecasts whose true RMSEP lies inside the prior-free compatible set; dashed line 90%. (b) Median width of the compatible set (ratio of upper to lower RMSEP). (c) Median information fraction of B-RPM (share of the prior variance of the gain removed by the pilot) by pilot size.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig5_observability.png){width=16cm}

## 4.4. Forecasting accuracy

In all paired comparisons below, differences are reference minus B-RPM, so positive values favour B-RPM. Table 2 summarises all forecasters (group-disjoint splits; ten repeated outer splits for the small data sets). The pre-registered RPM ($r=1$) remained more accurate than inverse-power-law extrapolation (mean absolute log error 0.284 vs 0.425) but not more accurate than the no-improvement rule (0.262). B-RPM reached 0.282. It was more accurate than IPL3 (difference +0.143, 95% CI +0.088 to +0.196, better on 33 of 38 tasks, Holm-adjusted p = 0.001) and than the scaling-exponent estimator of Wei et al. [25] (+0.117, 33 of 38 tasks), and as accurate as RPM (+0.002) and the transferred slope (+0.004). It was slightly less accurate than the no-improvement rule (-0.020, CI -0.038 to -0.003, Holm p = 0.222), so the pre-specified non-inferiority margin of 0.02 (HB2) was not met. On the level endpoint, the pilot's own cross-validated error is very hard to beat, because the dominant error source is the noise in that error, which no forecaster can remove (Section 4.6).


**Table 2.** Accuracy of learning-curve forecasts (task-level means over pilots, pilot sizes 25–200 and horizons $n\ge2n_0$). Level: $|\log(\widehat{\mathrm{RMSEP}}/\mathrm{RMSEP})|$; gain: error of the forecast gain $\mathrm{RMSEP}(n)/\mathrm{RMSEP}(n_0)$; bias: mean signed log error (> 0 pessimistic). LOSO/LOFO: prior or slope transferred from other data sources / other application families.

| Method | Level error | Level error (source mean) | Gain error | Bias |
|:-------------------------------------------------------------------------------------------------------------|---------------------:|----------------------------:|---------------------:|---------------------:|
| B-RPM (LOSO prior) | 0.282 | 0.304 | 0.265 | 0.008 |
| B-RPM (LOFO prior) | 0.292 | 0.310 | 0.273 | 0.001 |
| RPM, r = 1 (pre-registered) | 0.284 | 0.326 | 0.355 | 0.143 |
| RPM, transferred r | 0.505 | 0.555 | 0.453 | -0.301 |
| Inverse power law (IPL3) [8] | 0.425 | 0.440 | 0.309 | -0.253 |
| Power law (IPL2) | 0.535 | 0.587 | 0.371 | -0.437 |
| Scaling exponent [25] | 0.399 | 0.446 | 0.240 | -0.340 |
| Fixed-complexity formula | 1.198 | 1.152 | 1.077 | -1.089 |
| No improvement (pilot CV error) | 0.262 | 0.277 | 0.344 | 0.139 |
| Transferred slope (LOSO) | 0.286 | 0.279 | 0.188 | -0.125 |
| Transferred slope (LOFO) | 0.392 | 0.341 | 0.278 | -0.248 |
| B-RPM prior only (ablation) | 0.398 | 0.402 | 0.408 | 0.084 |
| B-RPM, prior on r only (ablation) | 0.344 | 0.378 | 0.291 | -0.106 |


The methods differ more in *bias* than in absolute error (Fig. 7). Pooled over tasks, the no-improvement rule was pessimistic, with a bias growing from +0.001 at $n/n_0=2$ to +0.271 at $n/n_0\ge32$. The transferred slope and IPL3 became increasingly optimistic (-0.326 and -0.665 at $n/n_0\ge32$). B-RPM's pooled bias stayed within ±0.040 up to eightfold extrapolation (overall +0.008). Pooled bias can hide opposite biases in different tasks, however. B-RPM was optimistic for soil and pessimistic for the designed mixtures (Supplementary Table S9). The mean absolute per-task bias, which does not cancel, was 0.170 for B-RPM, 0.175 for FLAT, 0.183 for RPM, 0.226 for SLOPE-T and 0.269 for IPL3. At extrapolation ratios of 8 and more it was 0.14–0.17 for B-RPM against 0.19–0.27 for FLAT, 0.23–0.34 for SLOPE-T and 0.28–0.66 for IPL3 (RPM 0.13–0.18; Supplementary Table S12). The theory-based forecasters are therefore the least biased for long extrapolations, but they are not unbiased task by task. For the gain itself, B-RPM improved on the no-improvement rule (+0.079, 30 of 38 tasks, Holm p = 0.001) and on RPM (+0.090, 33 of 38 tasks, Holm p < 0.001), and the pilot path added information beyond the prior (+0.143 vs the prior-only variant B-RPM-0). The transferred slope (LOSO) predicted gains better than B-RPM (-0.077). Its advantage came from the soil family, whose 23 tasks have similar slopes and supply most of each other's priors, and it disappeared under cross-family transfer (Section 4.5).

![**Fig. 7.** Mean signed log error by extrapolation ratio (task-level means; > 0 pessimistic, < 0 optimistic).](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig6_bias_by_horizon.png){width=9cm}

## 4.5. Transfer across application families

A planning rule is useful only if it works for a new application, for which no calibrations of the same kind exist. We therefore repeated the comparison with priors and slopes taken from *other application families* (leave-one-family-out, LOFO): soil tasks received a prior from fruit, fuel, pharmaceutical, meat and mixture calibrations. Each non-soil family comes from a single source, so its LOFO and LOSO priors are identical and already exclude its own family. The test is therefore informative for the 23 soil tasks, and the non-soil tasks show the cross-family case under both schemes. The transferred slope lost much of its accuracy: its mean absolute log error rose from 0.286 to 0.392, and from 0.258 to 0.435 on the soil tasks (Fig. 8a). B-RPM was almost unaffected (0.282 to 0.292; soil 0.214 to 0.230; Fig. 8b). Under LOFO transfer, B-RPM was more accurate than the transferred slope by +0.101 (95% CI +0.048 to +0.158; better on 27 of 38 tasks, p = 0.001; at the level of the eight sources, 4 of 8, p = 0.641, because the difference is concentrated in the three soil sources). With a cross-family prior, B-RPM remained less accurate than the no-improvement rule (-0.030, Holm p = 0.008). On the pre-specified gain endpoint (HB1), the two were equivalent (+0.006, p = 0.720), so HB1 was not confirmed. The difference on the level endpoint lies in the bias. A slope summarises the noise level, eigen-structure and alignment of the calibrations it was learned from, and it carries them into the new task. B-RPM transfers only a weak prior on the alignment exponent and the noise fraction. The noise fraction differed strongly between families, but the pilot path constrains it, so the posterior moves away from a misplaced prior: for the soil tasks, the cross-family prior was centred at a noise fraction of 0.04, the posterior median was 0.27, and the large-sample value was 0.20. The curve is then recomputed from the new task's own eigen-spectrum. A slope, by contrast, is applied as it is. Transferring structure rather than curves is the reason B-RPM generalises.

![**Fig. 8.** Effect of transferring prior knowledge across application families. Mean absolute log error per task (lines) when the slope (a) or the structural prior of B-RPM (b) comes from other data sources (LOSO) or from other application families (LOFO). Thick line: mean over tasks.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig7_cross_family_transfer.png){width=15cm}

## 4.6. Uncertainty and planning decisions

The posterior-predictive bands of B-RPM were too narrow. Nominal 80% and 95% bands covered the truth in 55% and 73% of cases (task averages; median width factor 1.7), so HB3 was not met, and coverage was lowest for the designed mixtures (11%). The bands contain the uncertainty of the pilot's regularisation path but not the difference between a pilot's cross-validated error and the error of a calibration trained on it, which our earlier analysis identified as the dominant source of level error. A post-hoc recalibration of the predictive spread, estimated leave-one-source-out from the standardised errors of the other sources, restored nominal coverage (79% and 95%; 80–85% across pilot sizes; soil 89%, mixtures 26%) at a median width factor of 2.4. IPL3 reached similar coverage only with bands that spanned a median factor of 13.8 (Supplementary Table S10). For the probabilistic decision 'will an eightfold larger calibration set reduce RMSEP by at least 15%?', no method beat the base rate (Brier score 0.290 for B-RPM, 0.274 for FLAT, 0.294 for SLOPE-T and 0.247 for the climatological forecast; Supplementary Table S11). This is consistent with Proposition 1. Such decisions turn on precisely the gain that a 25–200-sample pilot cannot determine.

We therefore tested the staged design that Proposition 1 suggests, using the existing forecasts (Supplementary Table S15). An analyst with an absolute RMSEP target and a budget of $N$ = 400 or 800 reference samples asks whether the target is reachable. Targets were set 15% above and 15% below the true RMSEP at $N$. Deciding from a pilot of $N/8$ samples was correct in 68% ($N$ = 400) and 76% ($N$ = 800) of cases with B-RPM, 74% and 76% with FLAT, and 63% and 67% with IPL3. Taking a second batch first, i.e. deciding from $N/4$ samples, raised the accuracy of every method by 4–10 percentage points (B-RPM 78% and 84%; FLAT 80% and 86%). The error of a B-RPM forecast for a fixed size of 800 samples fell from 0.244 with a 50-sample pilot to 0.158 with 100 and 0.121 with 200 (Supplementary Table S14). The methods failed in characteristic directions. FLAT declared reachable targets unreachable (correct for only 55% of reachable targets), and SLOPE-T declared unreachable targets reachable (correct for 33% of unreachable ones). B-RPM was the most balanced (80% and 64%). Gating the second batch on the compatible set did not save reference analyses: at this ±15% resolution, the set excluded the target in only 7% of cases, so a second batch was needed almost always. For decisions this fine, a 25–100-sample pilot cannot replace a second batch.

## 4.7. Robustness, distribution shift and ablation

On six representative tasks, B-RPM was evaluated with raw-absorbance and first-derivative spectra, Kennard–Stone-selected pilots and noisier reference values, and on mango under a new-season and an orchard-population shift (Supplementary Table S20). With raw and first-derivative spectra its mean absolute log errors were 0.289 and 0.319 (FLAT 0.215 and 0.272; IPL3 0.467 and 0.398). With added reference noise they were 0.143 (FLAT 0.117). In these scenarios B-RPM was therefore less accurate than the no-improvement rule, though more accurate than curve extrapolation; on six tasks the pilot's own error remains the most robust single number. Kennard–Stone pilots made every anchored forecast pessimistic (B-RPM bias +0.084, FLAT +0.233), because a pilot that spans the extremes of the spectral space has a larger cross-validated error than a random sample. Under the season shift, B-RPM became clearly optimistic (bias -0.502, against -0.255 for FLAT and -1.040 for IPL3): it forecast the improvement expected within the calibration seasons, which the new season did not deliver. No method anticipated a shift, and pilots must be drawn at random from the population in which the calibration will be used. In the controlled simulation (Supplementary Table S21), B-RPM with the real-data prior (median $r$ = 0.55) was the most accurate method when the true alignment was close to that prior ($r=0.5$: 0.224 vs 0.408 for FLAT, 0.346 for RPM and 0.251 for IPL3; with a flat prior 0.400). When the prior was wrong ($r=2$), it lost to the no-improvement rule (0.362 vs 0.095). This is the cost of importing information that Proposition 1 makes unavoidable. The pre-registered ablations (Supplementary Table S19) showed that freeing the alignment exponent without a prior is the most damaging choice (Section 2.4).

## 4.8. Comparison with previous work and practical recommendations

Learning-curve extrapolation for sample-size planning in analytical spectroscopy [8] and in classification more generally [9,10,26] has relied on the assumption that the curve's shape can be read from a pilot. Our results explain why this works for short extrapolations and fails for long ones: the shape below the observability horizon is not in the pilot. The same reasoning applies to the minimum-sample-size criteria transferred from clinical prediction modelling [3,4], which control overfitting at a given size but do not predict the gain from more samples. Recent work in this journal has emphasised validation design [44–46], replicate-based error structure [47], calibration-set reduction [48], prediction uncertainty [49] and benchmarks of modern regressors on many NIR data sets [50]. Its practical advice on multivariate calibration [51] fits our observations. The reference-method error sets a floor, the floor sets the slope, and learning curves for linear calibrations are shallow. The present work adds the planning side: a statement of what the pilot can and cannot tell, and a forecaster whose prior information is explicit, transferable and measurable.

We therefore recommend the following. (i) Do not extrapolate learning curves with power-law, exponential or logarithmic fits to a small pilot. (ii) Treat the pilot's cross-validated error as the best single estimate of the current error, and plan decisions that depend on the gain as staged decisions: a second batch of the same size improved every method's decisions more than any choice of forecaster did. (iii) Report the compatible set with any forecast, as an honest statement of what the pilot allows. (iv) When a gain forecast is needed before the second batch, prefer a forecaster with an explicit structural prior (B-RPM) over a transferred slope whenever the previous calibrations come from other materials, and recalibrate its bands on previous calibrations. (v) Draw pilots at random from the target population. A space-filling selection such as Kennard–Stone remains the right choice for building the final calibration, but not for forecasting.

# 5. Limitations

1. **Linear calibrations.** The theory describes ridge regression and tracked PLS closely (Section 4.1). Non-linear and local calibration methods may keep improving after linear models saturate, and their observability limits are not covered.
2. **Parametric family.** The compatible set and B-RPM use the power-law family $s_k\propto\lambda_k^r$. Other families could give wider sets. The coverage of about 90% on real data and 99% in simulation suggests that the family is adequate for these spectra, but it is not guaranteed for other materials.
3. **Pre-specified hypotheses not met.** B-RPM's raw bands under-covered (HB3). Its level error was 0.02 above the no-improvement rule, so non-inferiority (HB2) was not shown. Under cross-family transfer, its gain error equalled that of the transferred slope (HB1). The recalibrated bands are post hoc.
4. **Random sampling from a stable population.** Kennard–Stone pilots and genuine shifts bias every anchored forecast (Section 4.7). In the robustness scenarios, B-RPM was less accurate than the no-improvement rule, and under a season shift it was optimistic.
5. **Data sets.** 23 of the 38 tasks are soil calibrations. The fruit, fuel, pharmaceutical, meat and mixture sets are smaller and allow only short extrapolations, and the designed mixtures violate the random-sampling premise of the theory.

# 6. Conclusions

A small pilot set determines a calibration's error curve only above an observability horizon set by its size and the eigen-spectrum of the spectra. Below the horizon, analyte signal and irreducible noise cannot be told apart, so the gain from more reference samples must come from prior knowledge. This explains the optimism of power-law extrapolation and the strength of the no-improvement rule. The compatible set makes the limit visible for every pilot. B-RPM turns the unavoidable prior into an explicit one; it predicted gains better than power-law extrapolation and the no-improvement rule and, unlike a transferred slope, kept its accuracy across application families, but it did not beat the pilot's own error on the RMSEP level. For planning, the practical consequence is a staged design. Use the pilot's error as the current estimate and a structural forecast with its compatible set as a guide, and take a second batch before committing the full reference budget.

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

[26] C. Beleites, U. Neugebauer, T. Bocklitz, C. Krafft, J. Popp, Sample size planning for classification models, Analytica Chimica Acta 760 (2013), 25-33. https://doi.org/10.1016/j.aca.2012.11.007.

[27] l. E. Frank, J. H. Friedman, A Statistical View of Some Chemometrics Regression Tools, Technometrics 35 (1993), 109-135. https://doi.org/10.1080/00401706.1993.10485033.

[28] A. E. Hoerl, R. W. Kennard, Ridge Regression: Biased Estimation for Nonorthogonal Problems, Technometrics 12 (1970), 55-67. https://doi.org/10.1080/00401706.1970.10488634.

[29] R. D. Cook, L. Forzani, Partial least squares prediction in high-dimensional regression, The Annals of Statistics 47 (2019), 884-908. https://doi.org/10.1214/18-aos1681.

[30] D. B. Rubin, The Bayesian Bootstrap, The Annals of Statistics 9 (1981), 130-134. https://doi.org/10.1214/aos/1176345338.

[31] L. H. Dicker, Variance estimation in high-dimensional linear models, Biometrika 101 (2014), 269-284. https://doi.org/10.1093/biomet/ast065.

[32] L. Janson, R. F. Barber, E. Candès, EigenPrism: Inference for High Dimensional Signal-to-Noise Ratios, Journal of the Royal Statistical Society Series B: Statistical Methodology 79 (2017), 1037-1065. https://doi.org/10.1111/rssb.12203.

[33] J. L. Safanelli, T. Hengl, L. L. Parente, R. Minarik, D. E. Bloom, K. Todd-Brown, et al., Open Soil Spectral Library (OSSL): Building reproducible soil calibration models through open development and community engagement, PLOS ONE 20 (2025), e0296545. https://doi.org/10.1371/journal.pone.0296545.

[34] J. Sanderman, K. Savage, S. R. Dangal, Mid‐infrared spectroscopy for prediction of soil health indicators in the United States, Soil Science Society of America Journal 84 (2020), 251-261. https://doi.org/10.1002/saj2.20009.

[35] N. Anderson, K. Walsh, P. Subedi, C. Hayes, Achieving robustness across season, location and cultivar for a NIRS model for intact mango fruit dry matter content, Postharvest Biology and Technology 168 (2020), 111202. https://doi.org/10.1016/j.postharvbio.2020.111202.

[36] N. Anderson, K. Walsh, P. Subedi, J. Walsh, Mango DMC and NIR spectra, Mendeley Data (2026). https://doi.org/10.17632/46htwnp833.6.

[37] C. Borggaard, H. H. Thodberg, Optimal minimal neural interpretation of spectra, Analytical Chemistry 64 (1992), 545-551. https://doi.org/10.1021/ac00029a018.

[38] R. J. Barnes, M. S. Dhanoa, S. J. Lister, Standard Normal Variate Transformation and De-Trending of Near-Infrared Diffuse Reflectance Spectra, Applied Spectroscopy 43 (1989), 772-777. https://doi.org/10.1366/0003702894202201.

[39] S. Kapoor, A. Narayanan, Leakage and the reproducibility crisis in machine-learning-based science, Patterns 4 (2023), 100804. https://doi.org/10.1016/j.patter.2023.100804.

[40] B. S. Dayal, J. F. MacGregor, Improved PLS algorithms, Journal of Chemometrics 11 (1997), 73-85. https://doi.org/10.1002/(SICI)1099-128X(199701)11:1<73::AID-CEM435>3.0.CO;2-#.

[41] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of Data by Simplified Least Squares Procedures., Analytical Chemistry 36 (1964), 1627-1639. https://doi.org/10.1021/ac60214a047.

[42] R. W. Kennard, L. A. Stone, Computer Aided Design of Experiments, Technometrics 11 (1969), 137-148. https://doi.org/10.1080/00401706.1969.10490666.

[43] F. Wilcoxon, Individual Comparisons by Ranking Methods, Biometrics Bulletin 1 (1945), 80. https://doi.org/10.2307/3001968.

[44] E. Lopez, G. Gorla, J. Etxebarria-Elezgarai, J. M. Amigo, A. Seifert, The importance of choosing a proper validation strategy in predictive models. Part 2: Recipes for (avoiding) overfitting-A tutorial, Analytica Chimica Acta 1384 (2026), 344838. https://doi.org/10.1016/j.aca.2025.344838.

[45] A. P. Holman, D. Kurouski, Cross-study validation and guidance for resampling approaches for partial least squares discriminant analysis in spectral machine learning, Analytica Chimica Acta 1414 (2026), 345655. https://doi.org/10.1016/j.aca.2026.345655.

[46] Z. Al-Shaebi, M. Akdeniz, S. I. Yerlitas Tastan, P. Sagiroğlu, M. A. Atalay, G. Erturk Zararsiz, et al., Impact of dataset partitioning on the reliability of SERS–machine learning models for antimicrobial resistance classification, Analytica Chimica Acta 1423 (2026), 346185. https://doi.org/10.1016/j.aca.2026.346185.

[47] J. Riu, G. Gorla, M. Monti, M. Campeny, J. Quesada, B. Giussani, Measurement replicates under the lens: evaluating NIR spectroscopic error quality through multivariate error analysis, Analytica Chimica Acta 1419 (2026), 345885. https://doi.org/10.1016/j.aca.2026.345885.

[48] J. P. Andries, Y. V. Heyden, Calibration set reduction by iterative alternating reduction of predictive variables and calibration samples subsets, Analytica Chimica Acta 1429 (2026), 346468. https://doi.org/10.1016/j.aca.2026.346468.

[49] F. A. Chiappini, M. R. Alcaraz, L. Forzani, A bootstrap-assisted methodology for the estimation of prediction uncertainty in multilayer perceptron-based calibration, Analytica Chimica Acta 1353 (2025), 343954. https://doi.org/10.1016/j.aca.2025.343954.

[50] R. Reiter, D. Cornet, F. Michel, L. Rouan, G. Beurier, Using tabular foundation models for robust calibration of near-infrared chemical sensing data, Analytica Chimica Acta 1431 (2026), 346549. https://doi.org/10.1016/j.aca.2026.346549.

[51] A. C. Olivieri, Old advice on multivariate calibration: still in force, but not always followed. A tutorial, Analytica Chimica Acta 1396 (2026), 345155. https://doi.org/10.1016/j.aca.2026.345155.
