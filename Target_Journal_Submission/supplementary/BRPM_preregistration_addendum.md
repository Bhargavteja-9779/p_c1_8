# Pre-specification addendum: Bayesian regularisation-path matching (B-RPM)

_Written and committed on 2026-11-21, before any version-2 forecast result was inspected. The version-2 main
stage was running at that time; only version-1 results (archived unchanged) had been seen._

## Rationale
Version-1 results and their internal audit showed that (i) no pilot-only forecaster beat the no-improvement rule (FLAT) on
the registered level endpoint, (ii) a transferred empirical slope (SLOPE-T) predicted gains well within the soil
family but failed when transferred across application families, and (iii) RPM with a transferred alignment exponent
failed through noise-floor collapse. The observability argument (manuscript Proposition 1) implies that the gain
beyond the pilot depends on target power in modes the pilot cannot resolve, which must come from prior knowledge.
B-RPM makes that prior explicit, transfers it at the level of structural parameters (alignment exponent r and noise
fraction eta) that the deterministic-equivalent theory combines with the task's own unlabelled eigen-spectrum, and
propagates prior and pilot uncertainty into a posterior-predictive forecast.

## Fixed specification (no tuning on version-2 outcomes)
* Grid: r in 32 points on [0.05, 1.6]; eta in 40 points, logit-uniform on [5e-4, 0.97].
* Prior: Gaussian in r and logit(eta); median and 1.4826 x MAD of the large-sample (full-pool, r free) fits of all
  tasks from other sources (LOSO); SD floors 0.1 (r) and 0.3 (logit eta).
* Likelihood: log CV-MSE along the exact LOGO path (validity cut-off df2/n_eff <= 0.8, as RPM), kappa-quadrature
  weights normalised to m_eff = 2 effective observations; residual variance = delta-method variance of log CV-MSE at
  the pilot optimum; total variance V profiled.
* Point forecast: posterior mean of log RMSE. Bands: 80 % / 95 % quantiles of the posterior-predictive mixture with
  Gaussian anchor noise (sd = half the square root of the residual variance).
* Prior-free identification set: range of cell forecasts with profile deviance <= 6 of the best cell, widened by +-1.96 anchor sd (HB4: it contains the true curve in >= 90 % of pilot-horizon pairs; its width is reported by horizon).
* Variants: B-RPM-LOFO (prior from other application families), B-RPM-r (prior on r only), B-RPM-0 (prior only),
  B-RPM-m10 (m_eff = 10). Same pilots and seeds as the main stage.

## Hypotheses and endpoints (stated before results)
* HB1 (primary for B-RPM): mean task-level gain error |log predicted gain - log true gain| (ratio >= 2) of B-RPM-LOFO
  is lower than that of SLOPE-T transferred leave-one-family-out (paired Wilcoxon over tasks; also source-level).
* HB2: B-RPM's mean task-level |log error| on the registered level endpoint is not worse than FLAT (non-inferiority
  margin 0.02 log units, task-level bootstrap CI).
* HB3: B-RPM 80 % bands cover 70-90 % within every application family and every pilot-size stratum.
* Reported regardless of outcome. If HB1 fails, the manuscript reports it as such.
