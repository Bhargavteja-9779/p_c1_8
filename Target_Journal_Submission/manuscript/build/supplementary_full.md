# Supplementary Material

**How many reference samples does a spectroscopic calibration need? Forecasting multivariate-calibration learning curves from small pilot sets with random-matrix theory**

All tables and figures below are generated automatically by `run_all.py` from the per-pilot raw results.

**Table S1.** Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60).

| task | n pool | n test | p | max n truth | eigen decay exponent | truth seconds | family |
|---|---|---|---|---|---|---|---|
| ICRAF-VisNIR:OC | 2774 | 926 | 208 | 1600 | 3.665 | 13.410 | soil |
| Mango:DM | 3016 | 1005 | 94 | 1600 | 4.480 | 5.679 | fruit |
| Tecator:fat | 180 | 60 | 99 | 100 | 5.647 | 1.424 | meat |

**Table S2.** Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%).

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 3 | 0.260 | 0.227 | 0.302 | 0.252 | 0.236 | 0.092 | 14.035 | 36.842 |
| RPM-w | RPM-w (weighted path fit) | 3 | 0.250 | 0.218 | 0.267 | 0.265 | 0.233 | 0.107 | 8.772 | 35.088 |
| RPM-T | RPM-T (transferred alignment) | 3 | 0.268 | 0.146 | 0.352 | 0.305 | 0.189 | 0.017 | 35.088 | 49.123 |
| RPM-wT | RPM-wT (weighted + transferred) | 3 | 0.415 | 0.151 | 0.824 | 0.271 | 0.200 | -0.151 | 26.316 | 47.368 |
| IPL3 | Inverse power law (IPL3) | 3 | 0.584 | 0.145 | 1.269 | 0.337 | 0.178 | -0.533 | 26.316 | 50.877 |
| IPL2 | Power law (IPL2) | 3 | 0.809 | 0.145 | 1.951 | 0.331 | 0.536 | -0.787 | 17.544 | 29.825 |
| EXP3 | Exponential (EXP3) | 3 | 0.489 | 0.151 | 0.841 | 0.474 | 0.171 | -0.370 | 29.825 | 52.632 |
| LOG2 | Logarithmic (LOG2) | 3 | 7.306 | 0.411 | 12.906 | 8.600 | 12.855 | -7.305 | 3.509 | 7.018 |
| FLAT | No improvement (FLAT) | 3 | 0.164 | 0.089 | 0.227 | 0.176 | 0.123 | 0.027 | 42.105 | 78.947 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 3 | 1.060 | 0.150 | 2.783 | 0.246 | 0.167 | -0.977 | 28.070 | 57.895 |
| SLOPE-T | Transferred slope (SLOPE-T) | 3 | 0.252 | 0.203 | 0.307 | 0.245 | 0.245 | -0.231 | 14.035 | 40.351 |

**Table S3.** Forecast accuracy by pilot size n0.

| n0 | method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | RPM | RPM (pre-registered, r = 1) | 3 | 0.242 | 0.139 | 0.335 | 0.252 | 0.163 | 0.066 | 21.212 | 54.545 |
| 50 | RPM-w | RPM-w (weighted path fit) | 3 | 0.246 | 0.197 | 0.323 | 0.218 | 0.206 | 0.094 | 12.121 | 45.455 |
| 50 | RPM-T | RPM-T (transferred alignment) | 3 | 0.257 | 0.077 | 0.352 | 0.343 | 0.124 | -0.011 | 45.455 | 63.636 |
| 50 | RPM-wT | RPM-wT (weighted + transferred) | 3 | 0.409 | 0.072 | 0.824 | 0.331 | 0.162 | -0.171 | 39.394 | 54.545 |
| 50 | IPL3 | Inverse power law (IPL3) | 3 | 0.946 | 0.145 | 2.172 | 0.521 | 0.534 | -0.930 | 21.212 | 27.273 |
| 50 | IPL2 | Power law (IPL2) | 3 | 1.222 | 0.145 | 2.999 | 0.521 | 0.954 | -1.208 | 9.091 | 12.121 |
| 50 | EXP3 | Exponential (EXP3) | 3 | 0.285 | 0.187 | 0.474 | 0.194 | 0.171 | -0.145 | 30.303 | 51.515 |
| 50 | LOG2 | Logarithmic (LOG2) | 3 | 8.482 | 0.411 | 13.910 | 11.124 | 12.862 | -8.482 | 0.000 | 3.030 |
| 50 | FLAT | No improvement (FLAT) | 3 | 0.145 | 0.079 | 0.227 | 0.128 | 0.108 | 0.006 | 48.485 | 87.879 |
| 50 | DFOLS | Fixed-complexity formula (DF-OLS) | 3 | 1.098 | 0.141 | 2.783 | 0.369 | 0.197 | -1.050 | 15.152 | 48.485 |
| 50 | SLOPE-T | Transferred slope (SLOPE-T) | 3 | 0.285 | 0.245 | 0.347 | 0.263 | 0.303 | -0.270 | 6.061 | 30.303 |
| 100 | RPM | RPM (pre-registered, r = 1) | 2 | 0.299 | 0.260 | 0.337 | 0.299 | 0.302 | 0.299 | 4.167 | 12.500 |
| 100 | RPM-w | RPM-w (weighted path fit) | 2 | 0.273 | 0.195 | 0.350 | 0.273 | 0.260 | 0.273 | 4.167 | 20.833 |
| 100 | RPM-T | RPM-T (transferred alignment) | 2 | 0.245 | 0.232 | 0.258 | 0.245 | 0.276 | 0.245 | 20.833 | 29.167 |
| 100 | RPM-wT | RPM-wT (weighted + transferred) | 2 | 0.223 | 0.197 | 0.249 | 0.223 | 0.232 | 0.223 | 8.333 | 37.500 |
| 100 | IPL3 | Inverse power law (IPL3) | 2 | 0.124 | 0.107 | 0.141 | 0.124 | 0.113 | -0.003 | 33.333 | 83.333 |
| 100 | IPL2 | Power law (IPL2) | 2 | 0.367 | 0.093 | 0.642 | 0.367 | 0.160 | -0.338 | 29.167 | 54.167 |
| 100 | EXP3 | Exponential (EXP3) | 2 | 0.878 | 0.098 | 1.659 | 0.878 | 0.153 | -0.739 | 29.167 | 54.167 |
| 100 | LOG2 | Logarithmic (LOG2) | 2 | 8.548 | 5.445 | 11.650 | 8.548 | 12.715 | -8.544 | 8.333 | 12.500 |
| 100 | FLAT | No improvement (FLAT) | 2 | 0.169 | 0.102 | 0.235 | 0.169 | 0.147 | 0.155 | 33.333 | 66.667 |
| 100 | DFOLS | Fixed-complexity formula (DF-OLS) | 2 | 0.127 | 0.092 | 0.161 | 0.127 | 0.126 | 0.065 | 45.833 | 70.833 |
| 100 | SLOPE-T | Transferred slope (SLOPE-T) | 2 | 0.193 | 0.128 | 0.257 | 0.193 | 0.152 | -0.169 | 25.000 | 54.167 |

**Table S4.** Paired two-sided Wilcoxon signed-rank tests (task level) of the pre-registered RPM against every other method; Holm-adjusted p-values; median paired difference (other − RPM; positive favours RPM) with bootstrap 95% CI; matched-pairs rank-biserial correlation.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 3 | 3.000 | 1.000 | -0.033 | -0.035 | 0.038 | 0.000 | 1 | 2 | 1.000 |
| RPM-T | 3 | 2.000 | 0.750 | 0.004 | -0.081 | 0.100 | 0.333 | 2 | 1 | 1.000 |
| RPM-wT | 3 | 3.000 | 1.000 | -0.030 | -0.076 | 0.572 | 0.000 | 1 | 2 | 1.000 |
| IPL3 | 3 | 2.000 | 0.750 | 0.035 | -0.107 | 1.042 | 0.333 | 2 | 1 | 1.000 |
| IPL2 | 3 | 2.000 | 0.750 | 0.029 | -0.107 | 1.724 | 0.333 | 2 | 1 | 1.000 |
| EXP3 | 3 | 1.000 | 0.500 | 0.222 | -0.076 | 0.539 | 0.667 | 2 | 1 | 1.000 |
| LOG2 | 3 | 0.000 | 0.250 | 8.298 | 0.160 | 12.679 | 1.000 | 3 | 0 | 1.000 |
| FLAT | 3 | 0.000 | 0.250 | -0.126 | -0.138 | -0.024 | -1.000 | 0 | 3 | 1.000 |
| DFOLS | 3 | 2.000 | 0.750 | 0.019 | -0.152 | 2.531 | 0.333 | 2 | 1 | 1.000 |
| SLOPE-T | 3 | 2.000 | 0.750 | -0.007 | -0.099 | 0.080 | -0.333 | 1 | 2 | 1.000 |

**Table S5.** Forecast accuracy against the PLS ground truth.

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 3 | 0.270 | 0.211 | 0.320 | 0.279 | 0.208 | 0.041 | 15.789 | 42.105 |
| RPM-w | RPM-w (weighted path fit) | 3 | 0.254 | 0.244 | 0.271 | 0.247 | 0.218 | 0.055 | 14.035 | 40.351 |
| RPM-T | RPM-T (transferred alignment) | 3 | 0.285 | 0.142 | 0.430 | 0.283 | 0.169 | -0.034 | 28.070 | 54.386 |
| RPM-wT | RPM-wT (weighted + transferred) | 3 | 0.439 | 0.147 | 0.922 | 0.249 | 0.169 | -0.203 | 26.316 | 52.632 |
| IPL3 | Inverse power law (IPL3) | 3 | 0.615 | 0.204 | 1.281 | 0.359 | 0.184 | -0.585 | 22.807 | 49.123 |
| IPL2 | Power law (IPL2) | 3 | 0.845 | 0.204 | 1.969 | 0.362 | 0.560 | -0.839 | 10.526 | 28.070 |
| EXP3 | Exponential (EXP3) | 3 | 0.523 | 0.138 | 0.859 | 0.573 | 0.157 | -0.421 | 28.070 | 59.649 |
| LOG2 | Logarithmic (LOG2) | 3 | 7.357 | 0.510 | 12.924 | 8.638 | 12.872 | -7.356 | 3.509 | 3.509 |
| FLAT | No improvement (FLAT) | 3 | 0.166 | 0.085 | 0.260 | 0.152 | 0.107 | -0.025 | 42.105 | 80.702 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 3 | 1.092 | 0.142 | 2.881 | 0.254 | 0.173 | -1.028 | 26.316 | 52.632 |
| SLOPE-T | Transferred slope (SLOPE-T) | 3 | 0.287 | 0.233 | 0.325 | 0.303 | 0.263 | -0.282 | 15.789 | 28.070 |

**Table S6.** Paired tests against the PLS ground truth.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 3 | 2.000 | 0.750 | -0.035 | -0.048 | 0.036 | -0.333 | 1 | 2 | 1.000 |
| RPM-T | 3 | 2.000 | 0.750 | 0.004 | -0.069 | 0.110 | 0.333 | 2 | 1 | 1.000 |
| RPM-wT | 3 | 3.000 | 1.000 | -0.030 | -0.064 | 0.602 | 0.000 | 1 | 2 | 1.000 |
| IPL3 | 3 | 2.000 | 0.750 | 0.080 | -0.116 | 1.070 | 0.333 | 2 | 1 | 1.000 |
| IPL2 | 3 | 2.000 | 0.750 | 0.083 | -0.116 | 1.758 | 0.333 | 2 | 1 | 1.000 |
| EXP3 | 3 | 1.000 | 0.500 | 0.253 | -0.073 | 0.580 | 0.667 | 2 | 1 | 1.000 |
| LOG2 | 3 | 0.000 | 0.250 | 8.359 | 0.190 | 12.713 | 1.000 | 3 | 0 | 1.000 |
| FLAT | 3 | 0.000 | 0.250 | -0.126 | -0.127 | -0.060 | -1.000 | 0 | 3 | 1.000 |
| DFOLS | 3 | 2.000 | 0.750 | 0.043 | -0.137 | 2.561 | 0.333 | 2 | 1 | 1.000 |
| SLOPE-T | 3 | 3.000 | 1.000 | -0.016 | -0.045 | 0.114 | 0.000 | 1 | 2 | 1.000 |

**Table S7.** Empirical coverage and mean width (as a multiplicative factor on RMSE) of 80% and 95% forecast bands.

| method | nominal | coverage rows | coverage task mean | coverage task median | mean width log | mean width factor |
|---|---|---|---|---|---|---|
| RPM | 80 | 29.825 | 30.864 | 33.333 | 0.259 | 1.295 |
| RPM | 95 | 33.333 | 33.333 | 33.333 | 0.349 | 1.417 |
| RPM-w | 80 | 33.333 | 33.333 | 33.333 | 0.273 | 1.314 |
| RPM-w | 95 | 35.088 | 34.568 | 33.333 | 0.367 | 1.444 |
| RPM-T | 80 | 43.860 | 40.741 | 33.333 | 0.443 | 1.558 |
| RPM-T | 95 | 57.895 | 50.617 | 48.148 | 0.573 | 1.773 |
| RPM-wT | 80 | 56.140 | 49.383 | 44.444 | 0.508 | 1.661 |
| RPM-wT | 95 | 61.404 | 53.086 | 55.556 | 0.644 | 1.903 |
| IPL3 | 80 | 71.930 | 80.247 | 81.481 | 10.168 | 26044.420 |
| IPL3 | 95 | 84.211 | 88.889 | 85.185 | 10.633 | 41495.003 |
| IPL2 | 80 | 24.561 | 37.037 | 44.444 | 2.518 | 12.404 |
| IPL2 | 95 | 28.070 | 39.506 | 51.852 | 3.431 | 30.904 |
| EXP3 | 80 | 50.877 | 65.432 | 74.074 | 8.248 | 3818.469 |
| EXP3 | 95 | 57.895 | 70.370 | 74.074 | 8.385 | 4380.409 |
| LOG2 | 80 | 17.544 | 32.099 | 29.630 | 5.793 | 328.059 |
| LOG2 | 95 | 21.053 | 44.444 | 29.630 | 6.164 | 475.300 |

**Table S8.** Pre-registered sample-size decision metric: share of pilots whose forecast calibration size n̂ for the RMSE truly achieved at n* = 4n0 or 16n0 lies within a factor of two of n*, and share whose forecast never reaches the target.

| method | target | pct within factor2 | pct within factor2 task mean | pct never reaches target | median abs log2 err finite |
|---|---|---|---|---|---|
| DFOLS | 4n0 | 0.000 | 0.000 | 50.000 | 2.000 |
| DFOLS | 16n0 | 8.333 | 8.333 | 50.000 | 3.500 |
| EXP3 | 4n0 | 0.000 | 0.000 | 41.667 | 2.000 |
| EXP3 | 16n0 | 0.000 | 0.000 | 66.667 | 3.476 |
| FLAT | 4n0 | 0.000 | 0.000 | 66.667 | 2.000 |
| FLAT | 16n0 | 0.000 | 0.000 | 91.667 | 4.000 |
| IPL2 | 4n0 | 25.000 | 25.000 | 0.000 | 1.694 |
| IPL2 | 16n0 | 8.333 | 8.333 | 0.000 | 3.324 |
| IPL3 | 4n0 | 16.667 | 16.667 | 16.667 | 1.651 |
| IPL3 | 16n0 | 8.333 | 8.333 | 25.000 | 3.157 |
| LOG2 | 4n0 | 16.667 | 16.667 | 0.000 | 1.908 |
| LOG2 | 16n0 | 0.000 | 0.000 | 0.000 | 3.796 |
| RPM | 4n0 | 0.000 | 0.000 | 66.667 | 2.000 |
| RPM | 16n0 | 0.000 | 0.000 | 83.333 | 3.242 |
| RPM-T | 4n0 | 0.000 | 0.000 | 58.333 | 2.000 |
| RPM-T | 16n0 | 0.000 | 0.000 | 66.667 | 1.889 |
| RPM-w | 4n0 | 0.000 | 0.000 | 66.667 | 2.000 |
| RPM-w | 16n0 | 0.000 | 0.000 | 83.333 | 3.536 |
| RPM-wT | 4n0 | 8.333 | 8.333 | 58.333 | 2.000 |
| RPM-wT | 16n0 | 16.667 | 16.667 | 66.667 | 1.333 |
| SLOPE-T | 4n0 | 33.333 | 33.333 | 0.000 | 1.287 |
| SLOPE-T | 16n0 | 8.333 | 8.333 | 0.000 | 2.825 |

**Table S9.** Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task).

| variant | n tasks | mean abs logerr | rpm same tasks | mean diff vs rpm | ci95 lo | ci95 hi | p raw | p holm | rank biserial |
|---|---|---|---|---|---|---|---|---|---|
| RPM | 3 | 0.238 | 0.238 | 0.000 | 0.000 | 0.000 | – | – | – |
| RPM-rfree | 3 | 0.338 | 0.238 | 0.100 | 0.008 | 0.281 | 0.250 | 1.000 | 1.000 |
| RPM-ML2 | 3 | 0.161 | 0.238 | -0.077 | -0.139 | -0.018 | 0.250 | 1.000 | -1.000 |
| RPM-pilotcov | 3 | 0.230 | 0.238 | -0.008 | -0.111 | 0.097 | 0.750 | 1.000 | -0.333 |
| RPM-pilotcov+tail | 3 | 0.282 | 0.238 | 0.043 | -0.001 | 0.081 | 0.500 | 1.000 | 0.667 |
| RPM-U250 | 3 | 0.197 | 0.238 | -0.041 | -0.105 | -2.11e-09 | 0.250 | 1.000 | -1.000 |
| RPM-Uextra | 1 | 0.382 | 0.382 | 0.000354 | 0.000354 | 0.000354 | 1.000 | 1.000 | 1.000 |
| RPM-kfold10 | 3 | 0.229 | 0.238 | -0.010 | -0.055 | 0.065 | 1.000 | 1.000 | 0.000 |
| RPM-cut0.5 | 3 | 0.216 | 0.238 | -0.023 | -0.207 | 0.202 | 0.750 | 1.000 | -0.333 |
| RPM-cut0.95 | 3 | 0.246 | 0.238 | 0.007 | 0.000 | 0.022 | 1.000 | 1.000 | 1.000 |

**Table S11.** Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios).

| variant | method | n tasks | mean abs logerr | mean bias | coverage80 |
|---|---|---|---|---|---|
| iid_ref_seasons123 | FLAT | 1.000 | 0.133 | 0.130 | – |
| iid_ref_seasons123 | IPL3 | 1.000 | 0.039 | -0.037 | 80.000 |
| iid_ref_seasons123 | RPM | 1.000 | 0.311 | 0.311 | 0.000 |
| iid_ref_seasons123 | RPM-T | 1.000 | 0.254 | 0.201 | 50.000 |
| iid_ref_seasons123 | RPM-wT | 1.000 | 0.264 | 0.264 | 50.000 |
| ks_pilot | FLAT | 2.000 | 0.120 | 0.119 | – |
| ks_pilot | IPL3 | 2.000 | 0.121 | -0.076 | 91.667 |
| ks_pilot | RPM | 2.000 | 0.091 | 0.096 | 16.667 |
| ks_pilot | RPM-T | 2.000 | 0.048 | 0.011 | 58.333 |
| ks_pilot | RPM-wT | 2.000 | 0.115 | -0.006 | 41.667 |
| prep_sg1 | FLAT | 2.000 | 0.388 | 0.079 | – |
| prep_sg1 | IPL3 | 2.000 | 0.276 | 0.038 | 100.000 |
| prep_sg1 | RPM | 2.000 | 0.416 | 0.179 | 0.000 |
| prep_sg1 | RPM-T | 2.000 | 0.439 | 0.004 | 41.667 |
| prep_sg1 | RPM-wT | 2.000 | 0.455 | -0.028 | 8.333 |
| ref_noise | FLAT | 2.000 | 0.120 | 0.130 | – |
| ref_noise | IPL3 | 2.000 | 0.406 | -0.609 | 75.000 |
| ref_noise | RPM | 2.000 | 0.227 | 0.255 | 8.333 |
| ref_noise | RPM-T | 2.000 | 0.238 | 0.243 | 25.000 |
| ref_noise | RPM-wT | 2.000 | 0.207 | 0.236 | 41.667 |
| shift_population | FLAT | 1.000 | 0.457 | 0.457 | – |
| shift_population | IPL3 | 1.000 | 0.267 | 0.267 | 100.000 |
| shift_population | RPM | 1.000 | 0.555 | 0.555 | 0.000 |
| shift_population | RPM-T | 1.000 | 0.527 | 0.527 | 0.000 |
| shift_population | RPM-wT | 1.000 | 0.535 | 0.535 | 0.000 |
| shift_season | FLAT | 1.000 | 0.474 | -0.474 | – |
| shift_season | IPL3 | 1.000 | 2.120 | -2.120 | 40.000 |
| shift_season | RPM | 1.000 | 0.326 | -0.326 | 0.000 |
| shift_season | RPM-T | 1.000 | 0.622 | -0.622 | 0.000 |
| shift_season | RPM-wT | 1.000 | 0.472 | -0.472 | 0.000 |

**Table S12.** Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves.

| task | mode | mean abs err ridge | mean abs err pls | r | noise frac |
|---|---|---|---|---|---|
| ICRAF-VisNIR:OC | fixed1 | 0.067 | 0.082 | 1.000 | 0.548 |
| ICRAF-VisNIR:OC | free | 0.055 | 0.015 | 0.339 | 0.459 |
| Mango:DM | fixed1 | 0.155 | 0.147 | 1.000 | 0.319 |
| Mango:DM | free | 0.074 | 0.056 | 0.313 | 0.166 |
| Tecator:fat | fixed1 | 0.174 | 0.198 | 1.000 | 0.023 |
| Tecator:fat | free | 0.177 | 0.201 | 0.692 | 0.021 |

**Table S13.** Measured run time per pilot.

| component | mean | median | max |
|---|---|---|---|
| RPM point forecast + 50 bootstrap refits (s per pilot) | 0.261 | 0.195 | 0.543 |
| Within-pilot sub-sampling curve for IPL/EXP/LOG fits (s per pilot) | 0.332 | 0.276 | 0.748 |

**Table S14.** Accuracy by data-set family.

| family | method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fruit | RPM | RPM (pre-registered, r = 1) | 1 | 0.227 | 0.227 | 0.227 | 0.227 | 0.222 | 0.227 | 11.111 | 40.741 |
| fruit | IPL3 | Inverse power law (IPL3) | 1 | 1.269 | 1.269 | 1.269 | 1.269 | 0.161 | -1.222 | 25.926 | 55.556 |
| fruit | FLAT | No improvement (FLAT) | 1 | 0.089 | 0.089 | 0.089 | 0.089 | 0.092 | 0.061 | 55.556 | 100.000 |
| fruit | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 0.246 | 0.246 | 0.246 | 0.246 | 0.172 | -0.219 | 29.630 | 55.556 |
| meat | RPM | RPM (pre-registered, r = 1) | 1 | 0.252 | 0.252 | 0.252 | 0.252 | 0.285 | -0.221 | 33.333 | 33.333 |
| meat | IPL3 | Inverse power law (IPL3) | 1 | 0.145 | 0.145 | 0.145 | 0.145 | 0.059 | -0.106 | 66.667 | 66.667 |
| meat | FLAT | No improvement (FLAT) | 1 | 0.227 | 0.227 | 0.227 | 0.227 | 0.112 | -0.153 | 33.333 | 66.667 |
| meat | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 2.783 | 2.783 | 2.783 | 2.783 | 0.866 | -2.783 | 0.000 | 0.000 |
| soil | RPM | RPM (pre-registered, r = 1) | 1 | 0.302 | 0.302 | 0.302 | 0.302 | 0.245 | 0.272 | 14.815 | 33.333 |
| soil | IPL3 | Inverse power law (IPL3) | 1 | 0.337 | 0.337 | 0.337 | 0.337 | 0.207 | -0.273 | 22.222 | 44.444 |
| soil | FLAT | No improvement (FLAT) | 1 | 0.176 | 0.176 | 0.176 | 0.176 | 0.157 | 0.172 | 29.630 | 59.259 |
| soil | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 0.150 | 0.150 | 0.150 | 0.150 | 0.154 | 0.072 | 29.630 | 66.667 |

**Table S15.** Absolute log error by extrapolation ratio n/n0.

| method | ratio bin | mean | median | count | ratio |
|---|---|---|---|---|---|
| DFOLS | 1 | 0.690 | 0.167 | 15 | 2.000 |
| DFOLS | 2 | 0.192 | 0.142 | 12 | 4.000 |
| DFOLS | 3 | 0.201 | 0.175 | 12 | 8.000 |
| DFOLS | 4 | 0.206 | 0.161 | 12 | 16.000 |
| DFOLS | 5 | 0.248 | 0.203 | 6 | 32.000 |
| FLAT | 1 | 0.112 | 0.087 | 15 | 2.000 |
| FLAT | 2 | 0.110 | 0.092 | 12 | 4.000 |
| FLAT | 3 | 0.146 | 0.137 | 12 | 8.000 |
| FLAT | 4 | 0.176 | 0.156 | 12 | 16.000 |
| FLAT | 5 | 0.165 | 0.164 | 6 | 32.000 |
| IPL3 | 1 | 0.271 | 0.105 | 15 | 2.000 |
| IPL3 | 2 | 0.524 | 0.151 | 12 | 4.000 |
| IPL3 | 3 | 0.733 | 0.192 | 12 | 8.000 |
| IPL3 | 4 | 0.960 | 0.236 | 12 | 16.000 |
| IPL3 | 5 | 2.190 | 1.035 | 6 | 32.000 |
| RPM | 1 | 0.216 | 0.187 | 15 | 2.000 |
| RPM | 2 | 0.250 | 0.210 | 12 | 4.000 |
| RPM | 3 | 0.285 | 0.237 | 12 | 8.000 |
| RPM | 4 | 0.307 | 0.273 | 12 | 16.000 |
| RPM | 5 | 0.280 | 0.215 | 6 | 32.000 |

**Table S16.** Per-task error analysis (RPM vs IPL3) with spectral and fitted descriptors.

| task | family | eigen decay exponent | n pool | rpm mae | rpm bias | theory fit err | noise frac | r | ipl3 mae |
|---|---|---|---|---|---|---|---|---|---|
| ICRAF-VisNIR:OC | soil | 3.665 | 2774 | 0.302 | 0.272 | 0.055 | 0.459 | 0.339 | 0.337 |
| Tecator:fat | meat | 5.647 | 180 | 0.252 | -0.221 | 0.177 | 0.021 | 0.692 | 0.145 |
| Mango:DM | fruit | 4.480 | 3016 | 0.227 | 0.227 | 0.074 | 0.166 | 0.313 | 1.269 |

**Table S17.** Spearman correlations between per-task RPM error and task descriptors.

| descriptor | spearman rho | p | n |
|---|---|---|---|
| eigen_decay_exponent | -0.500 | 0.667 | 3 |
| theory_fit_err | -0.500 | 0.667 | 3 |
| noise_frac | 0.500 | 0.667 | 3 |
| r | 0.500 | 0.667 | 3 |
| n_pool | -0.500 | 0.667 | 3 |

**Table S18.** POST HOC: error of the forecast gain RMSE(n)/RMSE(n0) and balanced accuracy of the decision 'an 8× larger calibration set reduces RMSEP by ≥ 10%'.

| method | n tasks | mean task gain abs err | median task gain abs err | mean gain bias | decision 8x 10pct balanced acc | decision sensitivity | decision specificity | prevalence worthwhile |
|---|---|---|---|---|---|---|---|---|
| RPM | 3 | 0.243 | 0.271 | 0.281 | 0.083 | 0.167 | 0.000 | 1.000 |
| RPM-w | 3 | 0.260 | 0.236 | 0.281 | 0.083 | 0.167 | 0.000 | 1.000 |
| RPM-T | 3 | 0.207 | 0.203 | 0.220 | 0.125 | 0.250 | 0.000 | 1.000 |
| RPM-wT | 3 | 0.323 | 0.238 | 0.188 | 0.125 | 0.250 | 0.000 | 1.000 |
| IPL3 | 3 | 0.597 | 0.321 | -0.657 | 0.333 | 0.667 | 0.000 | 1.000 |
| IPL2 | 3 | 0.810 | 0.320 | -1.018 | 0.500 | 1.000 | 0.000 | 1.000 |
| EXP3 | 3 | 0.414 | 0.236 | -0.269 | 0.167 | 0.333 | 0.000 | 1.000 |
| LOG2 | 3 | 7.190 | 8.612 | -10.151 | 0.500 | 1.000 | 0.000 | 1.000 |
| FLAT | 3 | 0.173 | 0.158 | 0.158 | 0.000 | 0.000 | 0.000 | 1.000 |
| DFOLS | 3 | 0.883 | 0.142 | -0.160 | 0.292 | 0.583 | 0.000 | 1.000 |
| SLOPE-T | 3 | 0.188 | 0.196 | -0.185 | 0.500 | 1.000 | 0.000 | 1.000 |

**Table S19.** POST HOC: paired tests of gain error (reference: pre-registered RPM).

| reference | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM-w | 3 | 1.000 | 0.500 | 0.038 | -0.035 | 0.048 | 0.667 | 2 | 1 | 1.000 |
| RPM | RPM-T | 3 | 2.000 | 0.750 | -2.03e-05 | -0.117 | 0.009 | -0.333 | 1 | 2 | 1.000 |
| RPM | RPM-wT | 3 | 3.000 | 1.000 | -0.033 | -0.090 | 0.362 | 0.000 | 1 | 2 | 1.000 |
| RPM | IPL3 | 3 | 0.000 | 0.250 | 0.116 | 0.050 | 0.897 | 1.000 | 3 | 0 | 1.000 |
| RPM | IPL2 | 3 | 0.000 | 0.250 | 0.116 | 0.049 | 1.536 | 1.000 | 3 | 0 | 1.000 |
| RPM | EXP3 | 3 | 3.000 | 1.000 | -0.012 | -0.085 | 0.610 | 0.000 | 1 | 2 | 1.000 |
| RPM | LOG2 | 3 | 0.000 | 0.250 | 8.342 | 0.009 | 12.491 | 1.000 | 3 | 0 | 1.000 |
| RPM | FLAT | 3 | 1.000 | 0.500 | -0.112 | -0.166 | 0.069 | -0.667 | 1 | 2 | 1.000 |
| RPM | DFOLS | 3 | 3.000 | 1.000 | -0.179 | -0.186 | 2.286 | 0.000 | 1 | 2 | 1.000 |
| RPM | SLOPE-T | 3 | 1.000 | 0.500 | -0.075 | -0.108 | 0.016 | -0.667 | 1 | 2 | 1.000 |

**Table S20.** POST HOC: coverage and width of forecast brackets.

| bracket | n forecasts | coverage pct | coverage task mean pct | median width log | median width factor | coverage n0 50 | median width factor n0 50 | coverage n0 100 | median width factor n0 100 |
|---|---|---|---|---|---|---|---|---|---|
| [RPM-T, RPM] | 57 | 19.298 | 13.580 | 0.054 | 1.056 | 33.333 | 1.056 | 0.000 | 1.041 |
| [IPL3, FLAT] | 57 | 54.386 | 58.025 | 0.290 | 1.337 | 69.697 | 1.960 | 33.333 | 1.070 |
| [RPM, FLAT] | 57 | 19.298 | 13.580 | 0.149 | 1.160 | 21.212 | 1.152 | 16.667 | 1.224 |

**Table S21.** E0 simulation with Monte-Carlo ground truth (median absolute and signed log error).

| r | noise frac | n0 | method | median abs err | mean abs err | median bias |
|---|---|---|---|---|---|---|
| 1.000 | 0.300 | 40 | FLAT | 0.147 | 0.143 | 0.070 |
| 1.000 | 0.300 | 40 | IPL3 | 0.167 | 0.221 | -0.167 |
| 1.000 | 0.300 | 40 | RPM | 0.219 | 0.231 | -0.219 |
| 1.000 | 0.300 | 40 | RPM-T | 0.702 | 2.927 | -0.702 |
| 1.000 | 0.300 | 40 | RPM-w | 0.220 | 0.233 | -0.220 |
| 1.000 | 0.300 | 40 | RPM-wT | 0.665 | 2.749 | -0.665 |

**Table S22.** E0 simulation summarised by pilot size.

| method | n0 | median abs err | median bias |
|---|---|---|---|
| FLAT | 40 | 0.147 | 0.070 |
| IPL3 | 40 | 0.167 | -0.167 |
| RPM | 40 | 0.219 | -0.219 |
| RPM-T | 40 | 0.702 | -0.702 |
| RPM-w | 40 | 0.220 | -0.220 |
| RPM-wT | 40 | 0.665 | -0.665 |

**Table S23.** Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work.

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 2 | 0.239 | 0.227 | 0.252 | 0.239 | 0.228 | 0.003 | 13.333 | 40.000 |
| RPM-w | RPM-w (weighted path fit) | 2 | 0.242 | 0.218 | 0.265 | 0.242 | 0.243 | 0.046 | 6.667 | 30.000 |
| RPM-T | RPM-T (transferred alignment) | 2 | 0.249 | 0.146 | 0.352 | 0.249 | 0.083 | -0.111 | 53.333 | 66.667 |
| RPM-wT | RPM-wT (weighted + transferred) | 2 | 0.487 | 0.151 | 0.824 | 0.487 | 0.118 | -0.343 | 40.000 | 56.667 |
| IPL3 | Inverse power law (IPL3) | 2 | 0.707 | 0.145 | 1.269 | 0.707 | 0.160 | -0.664 | 30.000 | 56.667 |
| IPL2 | Power law (IPL2) | 2 | 1.048 | 0.145 | 1.951 | 1.048 | 1.150 | -1.028 | 6.667 | 13.333 |
| EXP3 | Exponential (EXP3) | 2 | 0.313 | 0.151 | 0.474 | 0.313 | 0.170 | -0.166 | 26.667 | 56.667 |
| LOG2 | Logarithmic (LOG2) | 2 | 6.658 | 0.411 | 12.906 | 6.658 | 13.871 | -6.658 | 0.000 | 3.333 |
| FLAT | No improvement (FLAT) | 2 | 0.158 | 0.089 | 0.227 | 0.158 | 0.092 | -0.046 | 53.333 | 96.667 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 2 | 1.514 | 0.246 | 2.783 | 1.514 | 0.184 | -1.501 | 26.667 | 50.000 |
| SLOPE-T | Transferred slope (SLOPE-T) | 2 | 0.276 | 0.245 | 0.307 | 0.276 | 0.286 | -0.256 | 10.000 | 30.000 |

**Table S24.** Paired tests excluding the ICRAF-VisNIR tasks.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 2 | 1.000 | 1.000 | 0.002 | -0.033 | 0.038 | 0.333 | 1 | 1 | 1.000 |
| RPM-T | 2 | 1.000 | 1.000 | 0.010 | -0.081 | 0.100 | 0.333 | 1 | 1 | 1.000 |
| RPM-wT | 2 | 1.000 | 1.000 | 0.248 | -0.076 | 0.572 | 0.333 | 1 | 1 | 1.000 |
| IPL3 | 2 | 1.000 | 1.000 | 0.468 | -0.107 | 1.042 | 0.333 | 1 | 1 | 1.000 |
| IPL2 | 2 | 1.000 | 1.000 | 0.809 | -0.107 | 1.724 | 0.333 | 1 | 1 | 1.000 |
| EXP3 | 2 | 1.000 | 1.000 | 0.073 | -0.076 | 0.222 | 0.333 | 1 | 1 | 1.000 |
| LOG2 | 2 | 0.000 | 0.500 | 6.419 | 0.160 | 12.679 | 1.000 | 2 | 0 | 1.000 |
| FLAT | 2 | 0.000 | 0.500 | -0.081 | -0.138 | -0.024 | -1.000 | 0 | 2 | 1.000 |
| DFOLS | 2 | 0.000 | 0.500 | 1.275 | 0.019 | 2.531 | 1.000 | 2 | 0 | 1.000 |
| SLOPE-T | 2 | 1.000 | 1.000 | 0.037 | -0.007 | 0.080 | 0.333 | 1 | 1 | 1.000 |

![**Figure S1.** Pre-registered sample-size decision metric by method.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig10_sample_size_decisions.png){width=15cm}

![**Figure S2.** Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig9_error_analysis.png){width=15cm}

![**Figure S3.** Data-set overview: number of samples and eigen-decay exponent by family.](/home/user/p_c1_8/Target_Journal_Submission/results_quick/figures/Fig11_dataset_overview.png){width=15cm}

# Note: Pre-registered experimental design


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


# Note: Data-leakage audit


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


# Note: Literature matrix and novelty map


All references were verified against Crossref / DataCite / arXiv (`manuscript/refs/verified_refs.json`).

## 1. Literature matrix

| Paper (year, venue) | Problem | Data | Method | Evaluation | What it does NOT address |
|---|---|---|---|---|---|
| Ali et al. (2018, *Anal. Chem.*) | Sample-size planning for multivariate (Raman) data | Raman spectra, classification tasks | Empirical learning curves (sub-sampling) + inverse-power-law fit; effect-size considerations | Extrapolated classifier performance on Raman data | Regression calibration; no theory linking curve shape to spectral covariance; no use of unlabelled spectra; no systematic multi-dataset validation of forecast accuracy/coverage |
| Mukherjee et al. (2003, *J. Comput. Biol.*) | Data-set size for microarray classifiers | Microarray data | Inverse power law (IPL) fit to sub-sampled error rates, significance by permutation | Few data sets | Regression; spectroscopy; extrapolation accuracy far beyond the pilot |
| Figueroa et al. (2012, *BMC Med. Inform. Decis. Mak.*) | Predicting sample size for classification | Clinical text/NLP | Weighted non-linear IPL fit with confidence intervals | Annotated corpora | Same as above; intervals derived from curve-fit covariance only |
| Viering & Loog (2023, *IEEE TPAMI*) | Review of learning-curve shapes | — | Survey: power laws, exponentials, non-monotone curves | — | Notes that well-behaved parametric shapes are not guaranteed; no domain method |
| Adriaensen et al. (2023, NeurIPS; arXiv:2310.20447) | Bayesian learning-curve extrapolation (epochs) | AutoML benchmarks | Prior-data fitted network (LC-PFN) | Hyper-parameter optimisation curves | Sample-size curves; spectroscopy |
| Riley et al. (2020, *BMJ*) | Minimum sample size for clinical prediction models | Clinical regressions | Closed-form criteria (shrinkage, R², optimism) for low-dimensional models | Simulation/worked examples | p ≫ n spectral calibration; data-dependent curve forecasting |
| Ng et al. (2020, *SOIL*); Kuang & Mouazen (2014, *Geoderma*) | Effect of calibration-set size in soil spectroscopy | Soil VisNIR/NIR libraries | Empirical accuracy vs sample size for PLSR, Cubist, CNN | Single libraries | No forecasting method; curves only observed after the fact |
| Bouckaert et al. (2011, *Chemom. Intell. Lab. Syst.*); Faber & Kowalski (1997, *J. Chemom.*) | Prediction uncertainty in multivariate calibration | NIR data | Interval methods; error propagation | Coverage and width | Uncertainty at a fixed calibration size, not as a function of n |
| Dobriban & Wager (2018, *Ann. Stat.*); Hastie et al. (2022, *Ann. Stat.*) | Asymptotic risk of ridge regression | Theory + simulations | Random-matrix (Marchenko–Pastur) deterministic equivalents | Theory, synthetic data | Practical estimation of the target-power spectrum from small labelled pilots; chemometrics |
| Bordelon et al. (2020, ICML); Canatar et al. (2021, *Nat. Commun.*); Simon et al. (2021, arXiv) | Spectrum-dependent learning curves; task–model alignment | Kernel regression on images | Learning curves from kernel eigenvalues and target coefficients (omniscient: full data used) | Synthetic + MNIST/CIFAR | Forecasting from a small pilot; analytical chemistry |
| Spigler et al. (2020, *J. Stat. Mech.*) | Exponent of learning curves on real data | MNIST, CIFAR | Relates curve exponent to decay of target coefficients (kernel PCA on full data) | Image data | Practical pilot-based forecasting |
| Jacot et al. (2020, NeurIPS, KARE); Wei, Hu & Steinhardt (2022, ICML); Craven & Wahba (1978, GCV) | Risk estimation from training data | Images, Higgs | KARE/GCV estimators of risk *at the current n and penalty* | Image data | Extrapolation of risk to larger n |
| Atanasov et al. (2024, arXiv) | Unified deterministic-equivalence view | Theory | S-transform renormalisation of the ridge | Theory | Applications to calibration planning |
| Talanta (2026) group-conformal NIR intervals (doi:10.1016/j.talanta.2026.130941) | Prediction intervals under new seasons/instruments/regions | NIR | Group-conformal calibration using PLS diagnostics | Coverage under shift | Sample-size planning / learning-curve forecasting |

## 2. Gap analysis
- **What exists:** (i) empirical learning-curve extrapolation with parametric shapes (IPL), introduced to chemometrics for Raman classification (Ali et al. 2018); (ii) observations that calibration accuracy saturates with sample size in soil spectroscopy; (iii) random-matrix theory that predicts ridge learning curves *if the population covariance and the target's coefficients are known*.
- **What fails / is missing:** parametric curve shapes fitted to a small pilot are unconstrained in the extrapolation region and, as our experiments show, tend to be optimistic; the theory has not been turned into a *practical* forecaster that uses only a small labelled pilot plus cheap unlabelled spectra; no study has quantified forecast accuracy, uncertainty calibration and decision quality across many spectroscopic calibration problems.
- **Why it matters:** reference analyses (wet chemistry, oven drying, chromatographic assays) dominate the cost of building NIR/MIR calibrations; analysts must decide how many samples to send for reference analysis and whether a target RMSEP is achievable at all.
- **What this work adds:** regularisation-path matching (RPM) — a forecaster that maps the pilot's exact leave-one-group-out errors along the ridge path onto the theory's effective-regularisation axis (identifying the observable part of the bias function N(κ)), fits a two-parameter model with the eigen-spectrum taken from unlabelled spectra, and extrapolates to any n with bootstrap uncertainty; plus a leakage-controlled, multi-domain benchmark (38 tasks) and an identifiability analysis.
- **How verified:** E0 simulation with Monte-Carlo truth; E1 theory validity; E2–E5 forecast accuracy, coverage and decisions vs six baselines with task-level paired tests; E6 ablations; E7 robustness (pre-processing, PLS truth, Kennard–Stone pilots, season and population shift, reference noise).

## 3. Novelty map
| Existing work | Contribution | Proposed work — genuinely different element |
|---|---|---|
| Ali et al. 2018 | IPL extrapolation of empirical learning curves for Raman classification | Theory-constrained forecast for regression calibration; extrapolation governed by the measured eigen-spectrum, not by an assumed curve shape |
| Mukherjee 2003 / Figueroa 2012 | Parametric curve fitting, curve-fit confidence intervals | Uses the whole regularisation path at fixed n0 instead of sub-samples of the pilot; Bayesian-bootstrap bands |
| Dobriban & Wager 2018; Hastie et al. 2022 | Asymptotic ridge risk given Σ and β | Practical estimation from a small pilot; regularisation-path ↔ κ mapping; identifiability analysis; validation on 38 real calibration tasks |
| Canatar et al. 2021; Bordelon et al. 2020 | Omniscient spectrum-dependent learning curves | Non-omniscient forecaster; unlabelled spectra for the spectrum; chemical interpretation (alignment, noise floor) |
| KARE / GCV (Jacot 2020; Wei 2022) | Risk at the current n | Risk at future n (extrapolation) |
| Soil sample-size studies (Ng 2020; Kuang 2014) | Observed size effects | Predictive, pre-hoc planning tool |

**Closest prior art and residual risk.** No published work was found that forecasts calibration learning curves from a pilot by fitting deterministic-equivalent ridge risk to the cross-validation regularisation path. The individual ingredients (ridge risk theory, LOO/GCV, learning-curve extrapolation) are known; a reviewer may therefore judge the contribution as a principled combination. The paper addresses this by (a) demonstrating where the combination adds predictive value and where it does not (negative results reported), (b) analysing identifiability, and (c) providing a decision-oriented evaluation.

## 4. Topic-selection record
≥ 15 candidate directions were screened (conformal NIR intervals under shift — abandoned, prior art incl. Talanta 2026; standard-free calibration transfer — crowded in ACA 2026; local/library modelling — crowded; validation/splitting protocols — crowded; label noise — ACA 2026; small-sample deep learning — crowded; Raman bacterial ID — generic-DL risk; retention-time transfer — strong competing groups; CCS prediction — incremental; LIBS matrix effects — domain data limits; censored reference values — data scarcity; multi-fidelity calibration — no public data; EEM-PARAFAC model selection — prior ARD work; spectral XAI faithfulness — evaluation-only; sample-size planning by empirical IPL — prior art Ali 2018; **theory-based learning-curve forecasting — selected**). Toxicology/hazard-prediction topics were excluded by design.

