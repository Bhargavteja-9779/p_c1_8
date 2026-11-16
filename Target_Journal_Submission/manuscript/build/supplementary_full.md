# Supplementary Material

**Random-matrix theory of multivariate calibration learning curves: what a small pilot set can and cannot predict**

All tables and figures below are generated automatically by `run_all.py` from the per-pilot raw results.

**Table S1.** Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60).

| task | n pool | n test | p | max n truth | eigen decay exponent | truth seconds | family |
|---|---|---|---|---|---|---|---|
| AfSIS1-MIR:OC | 1425 | 477 | 212 | 800 | 2.956 | 7.329 | soil |
| AfSIS1-MIR:clay | 1421 | 475 | 212 | 800 | 2.952 | 7.431 | soil |
| AfSIS1-MIR:pH | 1427 | 477 | 212 | 800 | 2.966 | 7.910 | soil |
| CGL:casein | 173 | 58 | 116 | 100 | 4.899 | 1.249 | mixture |
| CGL:glucose | 173 | 58 | 116 | 100 | 4.886 | 1.306 | mixture |
| CGL:lactate | 173 | 58 | 116 | 100 | 4.901 | 1.987 | mixture |
| CGL:moisture | 173 | 58 | 116 | 100 | 4.910 | 1.319 | mixture |
| Diesel:bp50 | 296 | 99 | 200 | 200 | 3.785 | 3.361 | fuel |
| Diesel:cn | 286 | 95 | 200 | 200 | 3.809 | 2.725 | fuel |
| Diesel:d4052 | 296 | 99 | 200 | 200 | 3.784 | 3.844 | fuel |
| Diesel:freeze | 296 | 99 | 200 | 200 | 3.774 | 3.536 | fuel |
| Diesel:total | 296 | 99 | 200 | 200 | 3.803 | 4.743 | fuel |
| Diesel:visc | 296 | 99 | 200 | 200 | 3.782 | 4.672 | fuel |
| ICRAF-MIR:CEC | 2738 | 914 | 212 | 1600 | 2.803 | 12.675 | soil |
| ICRAF-MIR:OC | 2774 | 924 | 212 | 1600 | 2.787 | 12.936 | soil |
| ICRAF-MIR:clay | 2802 | 936 | 212 | 1600 | 2.799 | 12.774 | soil |
| ICRAF-MIR:pH | 2827 | 947 | 212 | 1600 | 2.811 | 14.148 | soil |
| ICRAF-VisNIR:CEC | 2735 | 919 | 208 | 1600 | 3.657 | 12.494 | soil |
| ICRAF-VisNIR:OC | 2774 | 926 | 208 | 1600 | 3.665 | 23.672 | soil |
| ICRAF-VisNIR:clay | 2803 | 937 | 208 | 1600 | 3.661 | 13.634 | soil |
| ICRAF-VisNIR:pH | 2828 | 948 | 208 | 1600 | 3.659 | 12.893 | soil |
| KSSL-MIR:CEC | 12001 | 3000 | 212 | 6400 | 2.763 | 25.603 | soil |
| KSSL-MIR:OC | 12002 | 3001 | 212 | 6400 | 2.757 | 24.751 | soil |
| KSSL-MIR:clay | 11997 | 3003 | 212 | 6400 | 2.742 | 28.110 | soil |
| KSSL-MIR:pH | 12002 | 3001 | 212 | 6400 | 2.758 | 26.701 | soil |
| KSSL-VisNIR:CEC | 12011 | 3000 | 208 | 6400 | 3.831 | 23.410 | soil |
| KSSL-VisNIR:OC | 11997 | 3005 | 208 | 6400 | 3.860 | 24.964 | soil |
| KSSL-VisNIR:clay | 11997 | 3005 | 208 | 6400 | 3.887 | 24.506 | soil |
| KSSL-VisNIR:pH | 11993 | 3007 | 208 | 6400 | 3.828 | 24.052 | soil |
| Mango:DM | 3016 | 1005 | 94 | 1600 | 4.480 | 5.352 | fruit |
| Neospectra-NIR:CEC | 1572 | 524 | 150 | 800 | 3.902 | 6.602 | soil |
| Neospectra-NIR:OC | 1579 | 527 | 150 | 800 | 3.907 | 5.811 | soil |
| Neospectra-NIR:clay | 1580 | 526 | 150 | 800 | 3.909 | 6.345 | soil |
| Neospectra-NIR:pH | 1571 | 525 | 150 | 800 | 3.921 | 5.723 | soil |
| Tablets:assay | 491 | 164 | 216 | 400 | 3.208 | 8.039 | pharma |
| Tecator:fat | 180 | 60 | 99 | 100 | 5.647 | 1.996 | meat |
| Tecator:moisture | 180 | 60 | 99 | 100 | 5.613 | 1.673 | meat |
| Tecator:protein | 180 | 60 | 99 | 100 | 5.657 | 1.802 | meat |

**Table S2.** Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves (absolute log error per task).

| task | mode | mean abs err ridge | mean abs err pls | r | noise frac |
|---|---|---|---|---|---|
| AfSIS1-MIR:OC | fixed1 | 0.173 | 0.207 | 1.000 | 0.050 |
| AfSIS1-MIR:OC | free | 0.121 | 0.155 | 0.683 | 0.046 |
| AfSIS1-MIR:clay | fixed1 | 0.171 | 0.208 | 1.000 | 0.173 |
| AfSIS1-MIR:clay | free | 0.108 | 0.145 | 0.520 | 0.155 |
| AfSIS1-MIR:pH | fixed1 | 0.239 | 0.202 | 1.000 | 0.160 |
| AfSIS1-MIR:pH | free | 0.164 | 0.127 | 0.518 | 0.139 |
| CGL:casein | fixed1 | 0.177 | 0.171 | 1.000 | 0.000425 |
| CGL:casein | free | 0.090 | 0.084 | 0.652 | 0.000219 |
| CGL:glucose | fixed1 | 0.095 | 0.123 | 1.000 | 0.000368 |
| CGL:glucose | free | 0.059 | 0.095 | 0.632 | 0.000181 |
| CGL:lactate | fixed1 | 0.324 | 0.366 | 1.000 | 0.000256 |
| CGL:lactate | free | 0.330 | 0.372 | 0.698 | 0.000142 |
| CGL:moisture | fixed1 | 0.284 | 0.309 | 1.000 | 0.000257 |
| CGL:moisture | free | 0.287 | 0.311 | 0.711 | 0.000153 |
| Diesel:bp50 | fixed1 | 0.081 | 0.050 | 1.000 | 0.058 |
| Diesel:bp50 | free | 0.167 | 0.103 | 0.579 | 0.043 |
| Diesel:cn | fixed1 | 0.207 | 0.173 | 1.000 | 0.613 |
| Diesel:cn | free | 0.221 | 0.187 | 0.675 | 0.599 |
| Diesel:d4052 | fixed1 | 0.292 | 0.299 | 1.000 | 0.006 |
| Diesel:d4052 | free | 0.120 | 0.119 | 0.653 | 0.004 |
| Diesel:freeze | fixed1 | 0.074 | 0.133 | 1.000 | 0.221 |
| Diesel:freeze | free | 0.024 | 0.070 | 0.568 | 0.187 |
| Diesel:total | fixed1 | 0.386 | 0.473 | 1.000 | 0.063 |
| Diesel:total | free | 0.378 | 0.465 | 0.865 | 0.062 |
| Diesel:visc | fixed1 | 0.147 | 0.218 | 1.000 | 0.122 |
| Diesel:visc | free | 0.074 | 0.140 | 0.544 | 0.094 |
| ICRAF-MIR:CEC | fixed1 | 0.083 | 0.080 | 1.000 | 0.175 |
| ICRAF-MIR:CEC | free | 0.071 | 0.048 | 0.688 | 0.166 |
| ICRAF-MIR:OC | fixed1 | 0.099 | 0.110 | 1.000 | 0.111 |
| ICRAF-MIR:OC | free | 0.069 | 0.053 | 0.631 | 0.102 |
| ICRAF-MIR:clay | fixed1 | 0.103 | 0.138 | 1.000 | 0.218 |
| ICRAF-MIR:clay | free | 0.047 | 0.087 | 0.536 | 0.200 |
| ICRAF-MIR:pH | fixed1 | 0.108 | 0.140 | 1.000 | 0.220 |
| ICRAF-MIR:pH | free | 0.067 | 0.100 | 0.618 | 0.206 |
| ICRAF-VisNIR:CEC | fixed1 | 0.131 | 0.103 | 1.000 | 0.682 |
| ICRAF-VisNIR:CEC | free | 0.146 | 0.118 | 0.571 | 0.663 |
| ICRAF-VisNIR:OC | fixed1 | 0.067 | 0.082 | 1.000 | 0.548 |
| ICRAF-VisNIR:OC | free | 0.055 | 0.015 | 0.339 | 0.459 |
| ICRAF-VisNIR:clay | fixed1 | 0.099 | 0.093 | 1.000 | 0.584 |
| ICRAF-VisNIR:clay | free | 0.117 | 0.081 | 0.384 | 0.526 |
| ICRAF-VisNIR:pH | fixed1 | 0.129 | 0.158 | 1.000 | 0.381 |
| ICRAF-VisNIR:pH | free | 0.067 | 0.099 | 0.362 | 0.331 |
| KSSL-MIR:CEC | fixed1 | 0.199 | 0.188 | 1.000 | 0.051 |
| KSSL-MIR:CEC | free | 0.157 | 0.158 | 0.653 | 0.046 |
| KSSL-MIR:OC | fixed1 | 0.113 | 0.136 | 1.000 | 0.019 |
| KSSL-MIR:OC | free | 0.098 | 0.121 | 0.839 | 0.018 |
| KSSL-MIR:clay | fixed1 | 0.161 | 0.195 | 1.000 | 0.153 |
| KSSL-MIR:clay | free | 0.084 | 0.150 | 0.470 | 0.131 |
| KSSL-MIR:pH | fixed1 | 0.096 | 0.106 | 1.000 | 0.205 |
| KSSL-MIR:pH | free | 0.046 | 0.067 | 0.525 | 0.184 |
| KSSL-VisNIR:CEC | fixed1 | 0.139 | 0.149 | 1.000 | 0.462 |
| KSSL-VisNIR:CEC | free | 0.084 | 0.117 | 0.360 | 0.400 |
| KSSL-VisNIR:OC | fixed1 | 0.171 | 0.177 | 1.000 | 0.260 |
| KSSL-VisNIR:OC | free | 0.090 | 0.120 | 0.400 | 0.208 |
| KSSL-VisNIR:clay | fixed1 | 0.104 | 0.117 | 1.000 | 0.457 |
| KSSL-VisNIR:clay | free | 0.054 | 0.087 | 0.351 | 0.393 |
| KSSL-VisNIR:pH | fixed1 | 0.150 | 0.166 | 1.000 | 0.405 |
| KSSL-VisNIR:pH | free | 0.102 | 0.144 | 0.340 | 0.333 |
| Mango:DM | fixed1 | 0.155 | 0.147 | 1.000 | 0.319 |
| Mango:DM | free | 0.074 | 0.056 | 0.313 | 0.166 |

**Table S3.** κ-collapse: across-n standard deviation of rescaled log test errors plotted against κ, compared with the same errors plotted against the raw penalty μ.

| task | n curves | collapse sd log | no collapse ref sd log |
|---|---|---|---|
| ICRAF-MIR:clay | 6 | 0.010 | 0.519 |
| ICRAF-MIR:CEC | 6 | 0.029 | 0.598 |
| Neospectra-NIR:CEC | 5 | 0.037 | 0.435 |
| Diesel:bp50 | 3 | 0.015 | 0.305 |
| ICRAF-VisNIR:clay | 6 | 0.020 | 0.445 |
| AfSIS1-MIR:OC | 5 | 0.009 | 0.475 |
| AfSIS1-MIR:clay | 5 | 0.008 | 0.469 |
| KSSL-MIR:clay | 8 | 0.038 | 0.660 |
| Tablets:assay | 4 | 0.036 | 0.308 |
| Diesel:cn | 3 | 0.042 | 0.401 |
| Diesel:total | 3 | 0.044 | 0.238 |
| Neospectra-NIR:pH | 5 | 0.043 | 0.467 |
| Mango:DM | 6 | 0.019 | 0.277 |
| ICRAF-VisNIR:pH | 6 | 0.041 | 0.565 |
| ICRAF-VisNIR:CEC | 6 | 0.048 | 0.566 |
| KSSL-VisNIR:CEC | 8 | 0.109 | 0.718 |
| KSSL-VisNIR:OC | 8 | 0.108 | 0.680 |
| AfSIS1-MIR:pH | 5 | 0.043 | 0.579 |
| ICRAF-MIR:pH | 6 | 0.012 | 0.621 |
| Diesel:visc | 3 | 0.039 | 0.338 |
| KSSL-MIR:OC | 8 | 0.033 | 0.643 |
| ICRAF-VisNIR:OC | 6 | 0.051 | 0.533 |
| Neospectra-NIR:clay | 5 | 0.046 | 0.451 |
| ICRAF-MIR:OC | 6 | 0.042 | 0.594 |
| KSSL-VisNIR:pH | 8 | 0.092 | 0.697 |
| Diesel:freeze | 3 | 0.022 | 0.321 |
| Neospectra-NIR:OC | 5 | 0.064 | 0.478 |
| KSSL-MIR:CEC | 8 | 0.046 | 0.703 |
| KSSL-MIR:pH | 8 | 0.023 | 0.678 |
| Diesel:d4052 | 3 | 0.078 | 0.376 |
| KSSL-VisNIR:clay | 8 | 0.093 | 0.743 |

**Table S4.** POST HOC: regression of the ground-truth learning-curve slope (log RMSE per doubling of n) on large-sample theory parameters, and Spearman correlations.

| descriptor | spearman rho | p | r2 |
|---|---|---|---|
| noise_frac_full_pool | 0.590 | 9.64e-05 | – |
| r_full_pool | -0.369 | 0.023 | – |
| eigen_decay_exponent | -0.411 | 0.010 | – |
| n_pool | 0.624 | 2.83e-05 | – |
| OLS: slope ~ r + log(noise fraction) + eigen-decay | – | 1.01e-09 | 0.728 |

**Table S5.** POST HOC: learning-curve slopes and alignment exponents by spectral region.

| region | count | median | min | max |
|---|---|---|---|---|
| CGL | 4 | -0.415 | -0.528 | -0.254 |
| Diesel | 6 | -0.121 | -0.428 | 0.117 |
| MIR (soil) | 11 | -0.084 | -0.113 | -0.047 |
| Mango | 1 | -0.047 | -0.047 | -0.047 |
| Tablets | 1 | -0.059 | -0.059 | -0.059 |
| Tecator | 3 | -0.195 | -0.207 | -0.163 |
| Vis/NIR (soil) | 12 | -0.079 | -0.121 | -0.052 |

**Table S6.** Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%).

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 38 | 0.284 | 0.244 | 0.340 | 0.251 | 0.195 | 0.038 | 26.065 | 47.121 |
| RPM-w | RPM-w (weighted path fit) | 38 | 0.271 | 0.233 | 0.324 | 0.246 | 0.186 | 0.035 | 26.757 | 49.047 |
| RPM-T | RPM-T (transferred alignment) | 38 | 0.531 | 0.395 | 0.697 | 0.371 | 0.210 | -0.281 | 24.477 | 44.280 |
| RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.518 | 0.380 | 0.688 | 0.333 | 0.196 | -0.307 | 26.019 | 47.215 |
| IPL3 | Inverse power law (IPL3) | 38 | 0.429 | 0.375 | 0.496 | 0.379 | 0.286 | -0.268 | 19.720 | 35.168 |
| IPL2 | Power law (IPL2) | 38 | 0.540 | 0.462 | 0.632 | 0.460 | 0.394 | -0.451 | 14.047 | 26.009 |
| EXP3 | Exponential (EXP3) | 38 | 2.000 | 1.686 | 2.343 | 1.848 | 0.403 | -1.788 | 15.542 | 28.598 |
| LOG2 | Logarithmic (LOG2) | 38 | 10.127 | 9.456 | 10.806 | 10.060 | 12.854 | -10.104 | 4.290 | 8.215 |
| FLAT | No improvement (FLAT) | 38 | 0.266 | 0.227 | 0.315 | 0.226 | 0.184 | 0.138 | 27.430 | 49.617 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 1.272 | 0.953 | 1.630 | 0.827 | 0.198 | -1.161 | 26.729 | 47.224 |
| SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.251 | 0.212 | 0.305 | 0.212 | 0.183 | -0.093 | 27.112 | 49.794 |

**Table S7.** Forecast accuracy by pilot size n0.

| n0 | method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | RPM | RPM (pre-registered, r = 1) | 38 | 0.373 | 0.310 | 0.464 | 0.318 | 0.267 | -0.013 | 19.683 | 35.423 |
| 25 | RPM-w | RPM-w (weighted path fit) | 38 | 0.347 | 0.299 | 0.408 | 0.313 | 0.257 | -0.004 | 20.159 | 37.275 |
| 25 | RPM-T | RPM-T (transferred alignment) | 38 | 0.906 | 0.597 | 1.298 | 0.542 | 0.323 | -0.634 | 16.005 | 30.661 |
| 25 | RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.886 | 0.581 | 1.269 | 0.516 | 0.308 | -0.644 | 16.323 | 32.222 |
| 25 | IPL3 | Inverse power law (IPL3) | 38 | 0.599 | 0.520 | 0.685 | 0.538 | 0.469 | -0.402 | 10.820 | 19.815 |
| 25 | IPL2 | Power law (IPL2) | 38 | 0.709 | 0.607 | 0.823 | 0.646 | 0.584 | -0.600 | 8.862 | 16.481 |
| 25 | EXP3 | Exponential (EXP3) | 38 | 3.409 | 2.783 | 4.070 | 3.056 | 0.938 | -3.166 | 7.513 | 14.048 |
| 25 | LOG2 | Logarithmic (LOG2) | 38 | 12.391 | 11.892 | 12.881 | 12.453 | 13.348 | -12.374 | 1.085 | 1.958 |
| 25 | FLAT | No improvement (FLAT) | 38 | 0.329 | 0.288 | 0.376 | 0.278 | 0.255 | 0.182 | 19.259 | 36.429 |
| 25 | DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 2.344 | 1.681 | 3.100 | 1.301 | 0.318 | -2.198 | 17.328 | 31.905 |
| 25 | SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.306 | 0.267 | 0.351 | 0.284 | 0.245 | -0.094 | 21.534 | 39.392 |
| 50 | RPM | RPM (pre-registered, r = 1) | 38 | 0.247 | 0.205 | 0.312 | 0.208 | 0.186 | 0.032 | 27.517 | 48.974 |
| 50 | RPM-w | RPM-w (weighted path fit) | 38 | 0.241 | 0.201 | 0.304 | 0.211 | 0.183 | 0.021 | 27.980 | 49.901 |
| 50 | RPM-T | RPM-T (transferred alignment) | 38 | 0.415 | 0.303 | 0.562 | 0.257 | 0.208 | -0.183 | 24.801 | 44.139 |
| 50 | RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.412 | 0.291 | 0.568 | 0.232 | 0.200 | -0.217 | 25.232 | 45.993 |
| 50 | IPL3 | Inverse power law (IPL3) | 38 | 0.422 | 0.347 | 0.513 | 0.344 | 0.307 | -0.285 | 17.980 | 33.311 |
| 50 | IPL2 | Power law (IPL2) | 38 | 0.575 | 0.463 | 0.708 | 0.493 | 0.464 | -0.508 | 11.656 | 21.623 |
| 50 | EXP3 | Exponential (EXP3) | 38 | 1.663 | 1.249 | 2.126 | 1.262 | 0.383 | -1.462 | 14.470 | 27.020 |
| 50 | LOG2 | Logarithmic (LOG2) | 38 | 10.521 | 9.565 | 11.438 | 11.245 | 12.966 | -10.493 | 2.781 | 5.629 |
| 50 | FLAT | No improvement (FLAT) | 38 | 0.236 | 0.198 | 0.295 | 0.191 | 0.190 | 0.105 | 27.185 | 48.709 |
| 50 | DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 0.775 | 0.512 | 1.112 | 0.345 | 0.212 | -0.680 | 23.675 | 44.735 |
| 50 | SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.229 | 0.188 | 0.295 | 0.195 | 0.193 | -0.126 | 25.099 | 47.550 |
| 100 | RPM | RPM (pre-registered, r = 1) | 31 | 0.229 | 0.183 | 0.302 | 0.197 | 0.169 | 0.069 | 29.469 | 53.053 |
| 100 | RPM-w | RPM-w (weighted path fit) | 31 | 0.211 | 0.165 | 0.282 | 0.178 | 0.155 | 0.059 | 31.637 | 56.903 |
| 100 | RPM-T | RPM-T (transferred alignment) | 31 | 0.285 | 0.201 | 0.401 | 0.200 | 0.178 | -0.013 | 27.876 | 50.885 |
| 100 | RPM-wT | RPM-wT (weighted + transferred) | 31 | 0.261 | 0.174 | 0.379 | 0.164 | 0.157 | -0.057 | 30.973 | 55.973 |
| 100 | IPL3 | Inverse power law (IPL3) | 31 | 0.295 | 0.238 | 0.369 | 0.244 | 0.206 | -0.182 | 25.044 | 44.690 |
| 100 | IPL2 | Power law (IPL2) | 31 | 0.392 | 0.310 | 0.493 | 0.302 | 0.286 | -0.325 | 18.407 | 33.717 |
| 100 | EXP3 | Exponential (EXP3) | 31 | 1.103 | 0.795 | 1.463 | 0.901 | 0.267 | -0.973 | 20.265 | 37.611 |
| 100 | LOG2 | Logarithmic (LOG2) | 31 | 7.486 | 6.327 | 8.631 | 7.241 | 12.049 | -7.453 | 6.416 | 11.903 |
| 100 | FLAT | No improvement (FLAT) | 31 | 0.200 | 0.153 | 0.276 | 0.165 | 0.153 | 0.075 | 32.522 | 57.965 |
| 100 | DFOLS | Fixed-complexity formula (DF-OLS) | 31 | 0.279 | 0.200 | 0.383 | 0.193 | 0.151 | -0.187 | 34.027 | 57.655 |
| 100 | SLOPE-T | Transferred slope (SLOPE-T) | 31 | 0.198 | 0.148 | 0.279 | 0.150 | 0.152 | -0.143 | 32.080 | 58.673 |
| 200 | RPM | RPM (pre-registered, r = 1) | 25 | 0.164 | 0.146 | 0.184 | 0.161 | 0.141 | 0.098 | 33.415 | 62.500 |
| 200 | RPM-w | RPM-w (weighted path fit) | 25 | 0.159 | 0.138 | 0.183 | 0.143 | 0.139 | 0.095 | 32.988 | 63.780 |
| 200 | RPM-T | RPM-T (transferred alignment) | 25 | 0.157 | 0.138 | 0.176 | 0.154 | 0.123 | 0.077 | 38.720 | 66.829 |
| 200 | RPM-wT | RPM-wT (weighted + transferred) | 25 | 0.140 | 0.121 | 0.162 | 0.123 | 0.113 | 0.046 | 42.988 | 71.951 |
| 200 | IPL3 | Inverse power law (IPL3) | 25 | 0.184 | 0.158 | 0.213 | 0.171 | 0.139 | -0.096 | 36.098 | 60.854 |
| 200 | IPL2 | Power law (IPL2) | 25 | 0.246 | 0.206 | 0.287 | 0.240 | 0.199 | -0.199 | 24.390 | 45.427 |
| 200 | EXP3 | Exponential (EXP3) | 25 | 0.645 | 0.426 | 0.890 | 0.357 | 0.170 | -0.537 | 29.512 | 52.622 |
| 200 | LOG2 | Logarithmic (LOG2) | 25 | 3.876 | 2.699 | 5.103 | 3.195 | 0.563 | -3.851 | 11.524 | 22.317 |
| 200 | FLAT | No improvement (FLAT) | 25 | 0.139 | 0.118 | 0.159 | 0.133 | 0.122 | 0.079 | 39.695 | 70.183 |
| 200 | DFOLS | Fixed-complexity formula (DF-OLS) | 25 | 0.140 | 0.118 | 0.165 | 0.127 | 0.110 | -0.082 | 43.963 | 72.744 |
| 200 | SLOPE-T | Transferred slope (SLOPE-T) | 25 | 0.149 | 0.126 | 0.173 | 0.126 | 0.131 | -0.124 | 36.829 | 65.671 |

**Table S8.** Paired two-sided Wilcoxon signed-rank tests (task level) of the pre-registered RPM against every other method; Holm-adjusted p-values; median paired difference (other − RPM; positive favours RPM) with bootstrap 95% CI; matched-pairs rank-biserial correlation.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 38 | 189.000 | 0.008 | -0.009 | -0.018 | -0.005 | -0.490 | 10 | 28 | 0.023 |
| RPM-T | 38 | 28.000 | 1.08e-08 | 0.102 | 0.024 | 0.184 | 0.924 | 34 | 4 | 5.5e-08 |
| RPM-wT | 38 | 94.000 | 1.9e-05 | 0.072 | 0.018 | 0.204 | 0.746 | 26 | 12 | 7.58e-05 |
| IPL3 | 38 | 27.000 | 9.17e-09 | 0.131 | 0.106 | 0.178 | 0.927 | 35 | 3 | 5.5e-08 |
| IPL2 | 38 | 7.000 | 1.38e-10 | 0.225 | 0.166 | 0.289 | 0.981 | 36 | 2 | 1.11e-09 |
| EXP3 | 38 | 0.000 | 7.28e-12 | 1.407 | 1.186 | 1.817 | 1.000 | 38 | 0 | 7.28e-11 |
| LOG2 | 38 | 0.000 | 7.28e-12 | 9.876 | 9.259 | 10.540 | 1.000 | 38 | 0 | 7.28e-11 |
| FLAT | 38 | 270.000 | 0.148 | -0.021 | -0.047 | 0.010 | -0.271 | 15 | 23 | 0.148 |
| DFOLS | 38 | 18.000 | 1.84e-09 | 0.610 | 0.314 | 1.238 | 0.951 | 33 | 5 | 1.29e-08 |
| SLOPE-T | 38 | 205.000 | 0.015 | -0.023 | -0.049 | 0.002 | -0.447 | 13 | 25 | 0.031 |

**Table S9.** POST HOC: paired tests with SLOPE-T as the reference method.

| reference | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SLOPE-T | RPM | 38 | 205.000 | 0.015 | 0.023 | -0.002 | 0.049 | 0.447 | 25 | 13 | 0.046 |
| SLOPE-T | RPM-w | 38 | 242.000 | 0.063 | 0.019 | -0.009 | 0.039 | 0.347 | 23 | 15 | 0.126 |
| SLOPE-T | RPM-T | 38 | 45.000 | 1.22e-07 | 0.150 | 0.086 | 0.208 | 0.879 | 31 | 7 | 6.12e-07 |
| SLOPE-T | RPM-wT | 38 | 59.000 | 6.49e-07 | 0.131 | 0.070 | 0.178 | 0.841 | 32 | 6 | 2.6e-06 |
| SLOPE-T | IPL3 | 38 | 11.000 | 4e-10 | 0.163 | 0.133 | 0.180 | 0.970 | 35 | 3 | 2.8e-09 |
| SLOPE-T | IPL2 | 38 | 4.000 | 5.09e-11 | 0.244 | 0.203 | 0.302 | 0.989 | 36 | 2 | 4.07e-10 |
| SLOPE-T | EXP3 | 38 | 0.000 | 7.28e-12 | 1.497 | 1.215 | 1.862 | 1.000 | 38 | 0 | 7.28e-11 |
| SLOPE-T | LOG2 | 38 | 0.000 | 7.28e-12 | 9.893 | 9.250 | 10.794 | 1.000 | 38 | 0 | 7.28e-11 |
| SLOPE-T | FLAT | 38 | 273.000 | 0.161 | 0.025 | -0.003 | 0.042 | 0.263 | 25 | 13 | 0.161 |
| SLOPE-T | DFOLS | 38 | 14.000 | 8e-10 | 0.609 | 0.364 | 1.206 | 0.962 | 34 | 4 | 4.8e-09 |

**Table S10.** POST HOC: accuracy and paired tests stratified by extrapolation ratio n/n0 (short: < 16; long: ≥ 16).

| stratum | method | n tasks | mean task mean abs | mean task median abs | diff vs RPMw | p holm | RPMw wins | RPMw losses |
|---|---|---|---|---|---|---|---|---|
| ratio <= 8 | RPM-w | 38 | 0.252 | 0.212 | – | – | – | – |
| ratio <= 8 | RPM | 38 | 0.260 | 0.214 | 0.010 | 0.031 | 28.000 | 10.000 |
| ratio <= 8 | SLOPE-T | 38 | 0.233 | 0.201 | -0.017 | 0.086 | 15.000 | 23.000 |
| ratio <= 8 | FLAT | 38 | 0.238 | 0.205 | -0.017 | 0.086 | 10.000 | 28.000 |
| ratio <= 8 | IPL3 | 38 | 0.332 | 0.260 | 0.097 | 4.89e-07 | 31.000 | 7.000 |
| ratio >= 16 | RPM-w | 25 | 0.291 | 0.236 | – | – | – | – |
| ratio >= 16 | RPM | 25 | 0.317 | 0.245 | 0.014 | 0.000987 | 22.000 | 3.000 |
| ratio >= 16 | SLOPE-T | 25 | 0.263 | 0.235 | -0.028 | 0.227 | 8.000 | 17.000 |
| ratio >= 16 | FLAT | 25 | 0.284 | 0.264 | 0.009 | 0.731 | 14.000 | 11.000 |
| ratio >= 16 | IPL3 | 25 | 0.689 | 0.519 | 0.398 | 4.77e-07 | 24.000 | 1.000 |

**Table S11.** Absolute log error by extrapolation ratio n/n0.

| method | ratio bin | mean | median | count | ratio |
|---|---|---|---|---|---|
| DFOLS | 1 | 1.011 | 0.222 | 2640 | 2.000 |
| DFOLS | 2 | 1.034 | 0.190 | 2360 | 4.000 |
| DFOLS | 3 | 0.981 | 0.169 | 1940 | 8.000 |
| DFOLS | 4 | 0.982 | 0.177 | 1480 | 16.000 |
| DFOLS | 5 | 1.151 | 0.195 | 1140 | 32.000 |
| DFOLS | 6 | 1.492 | 0.235 | 660 | 64.000 |
| DFOLS | 7 | 1.782 | 0.262 | 320 | 128.000 |
| DFOLS | 8 | 3.123 | 0.330 | 160 | 256.000 |
| FLAT | 1 | 0.188 | 0.132 | 2640 | 2.000 |
| FLAT | 2 | 0.209 | 0.149 | 2360 | 4.000 |
| FLAT | 3 | 0.219 | 0.174 | 1940 | 8.000 |
| FLAT | 4 | 0.240 | 0.214 | 1480 | 16.000 |
| FLAT | 5 | 0.285 | 0.255 | 1140 | 32.000 |
| FLAT | 6 | 0.332 | 0.305 | 660 | 64.000 |
| FLAT | 7 | 0.360 | 0.337 | 320 | 128.000 |
| FLAT | 8 | 0.405 | 0.379 | 160 | 256.000 |
| IPL3 | 1 | 0.250 | 0.180 | 2640 | 2.000 |
| IPL3 | 2 | 0.321 | 0.226 | 2360 | 4.000 |
| IPL3 | 3 | 0.392 | 0.271 | 1940 | 8.000 |
| IPL3 | 4 | 0.509 | 0.375 | 1480 | 16.000 |
| IPL3 | 5 | 0.677 | 0.518 | 1140 | 32.000 |
| IPL3 | 6 | 0.877 | 0.690 | 660 | 64.000 |
| IPL3 | 7 | 1.113 | 0.929 | 320 | 128.000 |
| IPL3 | 8 | 1.532 | 1.341 | 160 | 256.000 |
| RPM | 1 | 0.231 | 0.164 | 2640 | 2.000 |
| RPM | 2 | 0.246 | 0.176 | 2360 | 4.000 |
| RPM | 3 | 0.257 | 0.189 | 1940 | 8.000 |
| RPM | 4 | 0.277 | 0.208 | 1480 | 16.000 |
| RPM | 5 | 0.306 | 0.231 | 1140 | 32.000 |
| RPM | 6 | 0.355 | 0.261 | 660 | 64.000 |
| RPM | 7 | 0.423 | 0.261 | 320 | 128.000 |
| RPM | 8 | 0.581 | 0.341 | 160 | 256.000 |

**Table S12.** Forecast accuracy against the PLS ground truth.

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 38 | 0.279 | 0.237 | 0.342 | 0.244 | 0.183 | 0.000661 | 27.850 | 49.776 |
| RPM-w | RPM-w (weighted path fit) | 38 | 0.266 | 0.226 | 0.325 | 0.235 | 0.173 | -0.002 | 29.103 | 52.084 |
| RPM-T | RPM-T (transferred alignment) | 38 | 0.534 | 0.394 | 0.703 | 0.359 | 0.201 | -0.318 | 26.579 | 46.327 |
| RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.523 | 0.380 | 0.697 | 0.328 | 0.187 | -0.345 | 28.766 | 49.131 |
| IPL3 | Inverse power law (IPL3) | 38 | 0.443 | 0.385 | 0.514 | 0.387 | 0.294 | -0.305 | 18.458 | 34.121 |
| IPL2 | Power law (IPL2) | 38 | 0.562 | 0.482 | 0.659 | 0.464 | 0.420 | -0.488 | 12.262 | 23.701 |
| EXP3 | Exponential (EXP3) | 38 | 2.013 | 1.696 | 2.357 | 1.856 | 0.400 | -1.826 | 16.393 | 29.262 |
| LOG2 | Logarithmic (LOG2) | 38 | 10.161 | 9.487 | 10.844 | 10.095 | 12.880 | -10.141 | 3.953 | 7.598 |
| FLAT | No improvement (FLAT) | 38 | 0.253 | 0.213 | 0.307 | 0.201 | 0.166 | 0.101 | 30.598 | 54.168 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 1.289 | 0.965 | 1.651 | 0.835 | 0.205 | -1.198 | 25.785 | 45.804 |
| SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.263 | 0.223 | 0.322 | 0.227 | 0.206 | -0.130 | 23.617 | 44.439 |

**Table S13.** Paired tests against the PLS ground truth.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 38 | 176.000 | 0.004 | -0.009 | -0.018 | -0.005 | -0.525 | 11 | 27 | 0.012 |
| RPM-T | 38 | 14.000 | 8e-10 | 0.105 | 0.047 | 0.198 | 0.962 | 36 | 2 | 4.8e-09 |
| RPM-wT | 38 | 74.000 | 3.09e-06 | 0.080 | 0.033 | 0.221 | 0.800 | 28 | 10 | 1.24e-05 |
| IPL3 | 38 | 18.000 | 1.84e-09 | 0.155 | 0.121 | 0.184 | 0.951 | 36 | 2 | 9.2e-09 |
| IPL2 | 38 | 3.000 | 3.64e-11 | 0.235 | 0.192 | 0.316 | 0.992 | 37 | 1 | 2.91e-10 |
| EXP3 | 38 | 0.000 | 7.28e-12 | 1.428 | 1.196 | 1.834 | 1.000 | 38 | 0 | 7.28e-11 |
| LOG2 | 38 | 0.000 | 7.28e-12 | 9.905 | 9.296 | 10.569 | 1.000 | 38 | 0 | 7.28e-11 |
| FLAT | 38 | 219.000 | 0.027 | -0.026 | -0.053 | -0.006 | -0.409 | 12 | 26 | 0.055 |
| DFOLS | 38 | 12.000 | 5.09e-10 | 0.627 | 0.313 | 1.271 | 0.968 | 35 | 3 | 3.57e-09 |
| SLOPE-T | 38 | 302.000 | 0.328 | -0.009 | -0.039 | 0.017 | -0.185 | 15 | 23 | 0.328 |

**Table S14.** Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work.

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 34 | 0.290 | 0.245 | 0.350 | 0.251 | 0.198 | 0.029 | 25.896 | 46.825 |
| RPM-w | RPM-w (weighted path fit) | 34 | 0.278 | 0.236 | 0.334 | 0.249 | 0.188 | 0.028 | 26.566 | 48.585 |
| RPM-T | RPM-T (transferred alignment) | 34 | 0.563 | 0.412 | 0.737 | 0.397 | 0.215 | -0.323 | 24.190 | 43.564 |
| RPM-wT | RPM-wT (weighted + transferred) | 34 | 0.552 | 0.398 | 0.730 | 0.353 | 0.201 | -0.350 | 25.616 | 46.231 |
| IPL3 | Inverse power law (IPL3) | 34 | 0.443 | 0.384 | 0.512 | 0.398 | 0.303 | -0.280 | 18.650 | 33.467 |
| IPL2 | Power law (IPL2) | 34 | 0.556 | 0.472 | 0.653 | 0.500 | 0.421 | -0.464 | 12.657 | 23.790 |
| EXP3 | Exponential (EXP3) | 34 | 2.008 | 1.650 | 2.400 | 1.848 | 0.413 | -1.791 | 15.194 | 28.099 |
| LOG2 | Logarithmic (LOG2) | 34 | 10.383 | 9.694 | 11.076 | 10.204 | 12.854 | -10.361 | 3.283 | 6.663 |
| FLAT | No improvement (FLAT) | 34 | 0.273 | 0.229 | 0.328 | 0.226 | 0.185 | 0.137 | 27.711 | 49.492 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 34 | 1.353 | 1.000 | 1.736 | 0.851 | 0.211 | -1.248 | 25.356 | 45.043 |
| SLOPE-T | Transferred slope (SLOPE-T) | 34 | 0.260 | 0.218 | 0.318 | 0.223 | 0.194 | -0.088 | 25.378 | 47.559 |

**Table S15.** Paired tests excluding the ICRAF-VisNIR tasks.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 34 | 175.000 | 0.036 | -0.008 | -0.014 | -0.000828 | -0.412 | 10 | 24 | 0.107 |
| RPM-T | 34 | 20.000 | 4.32e-08 | 0.115 | 0.066 | 0.225 | 0.933 | 31 | 3 | 2.59e-07 |
| RPM-wT | 34 | 58.000 | 9.05e-06 | 0.101 | 0.030 | 0.229 | 0.805 | 25 | 9 | 3.62e-05 |
| IPL3 | 34 | 23.000 | 7.45e-08 | 0.142 | 0.121 | 0.198 | 0.923 | 31 | 3 | 3.73e-07 |
| IPL2 | 34 | 6.000 | 1.63e-09 | 0.233 | 0.176 | 0.332 | 0.980 | 32 | 2 | 1.3e-08 |
| EXP3 | 34 | 0.000 | 1.16e-10 | 1.231 | 1.125 | 1.817 | 1.000 | 34 | 0 | 1.16e-09 |
| LOG2 | 34 | 0.000 | 1.16e-10 | 9.915 | 9.525 | 10.788 | 1.000 | 34 | 0 | 1.16e-09 |
| FLAT | 34 | 232.000 | 0.270 | -0.021 | -0.048 | 0.015 | -0.220 | 15 | 19 | 0.270 |
| DFOLS | 34 | 13.000 | 1.02e-08 | 0.645 | 0.364 | 1.324 | 0.956 | 30 | 4 | 7.17e-08 |
| SLOPE-T | 34 | 181.000 | 0.046 | -0.021 | -0.036 | 0.005 | -0.392 | 12 | 22 | 0.107 |

**Table S16.** Eigen-spectrum source ablation for RPM-T (defined before RPM-T results were inspected).

| variant | n tasks | mean abs logerr | median task abs logerr | mean bias | median diff | ci95 lo | ci95 hi | p holm | ref wins | ref losses |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-T | 38 | 0.392 | 0.234 | -0.058 | – | – | – | – | – | – |
| RPM-T-pilotcov | 38 | 0.258 | 0.222 | 0.066 | -0.028 | -0.051 | -0.007 | 0.000687 | 10.000 | 28.000 |
| RPM-T-pilotcov+tail | 38 | 0.469 | 0.307 | 0.022 | 0.050 | 0.023 | 0.090 | 0.034 | 27.000 | 11.000 |
| RPM-T-U250 | 38 | 0.366 | 0.229 | -0.032 | -0.002 | -0.010 | -5.74e-07 | 0.002 | 12.000 | 26.000 |

**Table S17.** POST HOC: coverage and width of forecast brackets.

| bracket | n forecasts | coverage pct | coverage task mean pct | median width log | median width factor | coverage n0 25 | median width factor n0 25 | coverage n0 50 | median width factor n0 50 | coverage n0 100 | median width factor n0 100 | coverage n0 200 | median width factor n0 200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RPM-T, RPM] | 10700 | 8.262 | 12.016 | 0.027 | 1.028 | 9.894 | 1.044 | 9.172 | 1.030 | 6.814 | 1.020 | 4.817 | 1.018 |
| [IPL3, FLAT] | 10700 | 46.234 | 42.326 | 0.283 | 1.327 | 46.270 | 1.629 | 46.258 | 1.358 | 49.071 | 1.264 | 42.195 | 1.154 |
| [RPM, FLAT] | 10700 | 21.234 | 20.491 | 0.129 | 1.138 | 26.005 | 1.256 | 21.887 | 1.137 | 18.717 | 1.101 | 12.500 | 1.059 |

**Table S18.** Empirical coverage, median width factor (multiplicative, on RMSE) and share of bands wider than a factor of ten, for 80% and 95% forecast bands.

| method | nominal | coverage rows | coverage task mean | coverage task median | mean width log | mean width factor | median width factor | pct width factor gt10 |
|---|---|---|---|---|---|---|---|---|
| RPM | 80 | 42.336 | 43.165 | 44.176 | 0.379 | 1.460 | 1.373 | 0.467 |
| RPM | 95 | 58.346 | 58.504 | 62.775 | 0.558 | 1.748 | 1.588 | 0.841 |
| RPM-w | 80 | 43.729 | 45.100 | 45.385 | 0.386 | 1.471 | 1.363 | 0.477 |
| RPM-w | 95 | 59.907 | 60.607 | 62.083 | 0.568 | 1.765 | 1.569 | 0.888 |
| RPM-T | 80 | 44.168 | 44.727 | 45.357 | 0.631 | 1.880 | 1.421 | 4.187 |
| RPM-T | 95 | 59.710 | 59.255 | 62.262 | 0.931 | 2.536 | 1.674 | 7.308 |
| RPM-wT | 80 | 44.776 | 44.569 | 43.810 | 0.622 | 1.862 | 1.400 | 4.617 |
| RPM-wT | 95 | 60.748 | 59.819 | 61.667 | 0.921 | 2.513 | 1.645 | 7.327 |
| IPL3 | 80 | 82.981 | 82.372 | 85.810 | 10.386 | 32405.292 | 782102.621 | 70.215 |
| IPL3 | 95 | 89.486 | 89.182 | 91.891 | 11.489 | 97624.460 | 1072058.999 | 77.168 |
| IPL2 | 80 | 26.514 | 29.510 | 29.712 | 2.053 | 7.789 | 1.565 | 15.495 |
| IPL2 | 95 | 34.570 | 38.579 | 38.750 | 4.141 | 62.876 | 2.143 | 30.579 |
| EXP3 | 80 | 71.056 | 70.021 | 72.679 | 8.467 | 4756.037 | 502248.396 | 57.131 |
| EXP3 | 95 | 79.009 | 78.426 | 80.801 | 9.317 | 11128.964 | 799269.607 | 61.701 |
| LOG2 | 80 | 12.907 | 12.035 | 11.154 | 1.768 | 5.860 | 1.000 | 12.869 |
| LOG2 | 95 | 16.551 | 15.222 | 14.861 | 2.292 | 9.894 | 1.000 | 16.729 |

**Table S19.** POST HOC: leave-one-source-out split-conformal bands (coverage and median width factor).

| method | nominal | coverage pct | median width factor |
|---|---|---|---|
| RPM | 80 | 79.757 | 2.089 |
| RPM | 95 | 94.346 | 4.322 |
| RPM-w | 80 | 79.869 | 2.046 |
| RPM-w | 95 | 94.355 | 4.008 |
| SLOPE-T | 80 | 79.252 | 1.771 |
| SLOPE-T | 95 | 94.336 | 3.197 |
| FLAT | 80 | 79.607 | 1.766 |
| FLAT | 95 | 94.290 | 3.180 |
| IPL3 | 80 | 78.140 | 2.884 |
| IPL3 | 95 | 93.318 | 6.253 |

**Table S20.** Pre-registered sample-size decision metric: share of pilots whose forecast calibration size n̂ for the RMSE truly achieved at n* = 4n0 or 16n0 lies within a factor of two of n*, and share whose forecast never reaches the target.

| method | target | pct within factor2 | pct within factor2 task mean | pct never reaches target | median abs log2 err finite |
|---|---|---|---|---|---|
| DFOLS | 4n0 | 6.483 | 5.877 | 24.788 | 1.900 |
| DFOLS | 16n0 | 1.757 | 1.767 | 40.743 | 3.499 |
| EXP3 | 4n0 | 8.263 | 7.840 | 28.347 | 1.891 |
| EXP3 | 16n0 | 0.203 | 0.217 | 37.635 | 3.542 |
| FLAT | 4n0 | 0.000 | 0.000 | 68.305 | 2.000 |
| FLAT | 16n0 | 0.000 | 0.000 | 87.162 | 4.000 |
| IPL2 | 4n0 | 28.051 | 29.178 | 8.602 | 1.617 |
| IPL2 | 16n0 | 9.257 | 8.967 | 6.216 | 2.859 |
| IPL3 | 4n0 | 25.085 | 26.151 | 19.576 | 1.672 |
| IPL3 | 16n0 | 9.189 | 8.650 | 23.581 | 2.738 |
| LOG2 | 4n0 | 13.814 | 11.447 | 2.458 | 1.961 |
| LOG2 | 16n0 | 2.162 | 2.050 | 1.351 | 3.731 |
| RPM | 4n0 | 4.703 | 4.748 | 51.398 | 2.000 |
| RPM | 16n0 | 1.959 | 1.933 | 66.351 | 3.616 |
| RPM-T | 4n0 | 12.754 | 17.248 | 41.229 | 2.000 |
| RPM-T | 16n0 | 4.122 | 4.267 | 58.176 | 3.308 |
| RPM-w | 4n0 | 4.237 | 4.134 | 51.864 | 2.000 |
| RPM-w | 16n0 | 2.162 | 1.950 | 66.824 | 3.607 |
| RPM-wT | 4n0 | 14.237 | 19.474 | 39.534 | 2.000 |
| RPM-wT | 16n0 | 4.122 | 4.150 | 57.568 | 3.329 |
| SLOPE-T | 4n0 | 29.534 | 25.044 | 13.390 | 1.525 |
| SLOPE-T | 16n0 | 21.149 | 20.883 | 6.824 | 2.089 |

**Table S21.** POST HOC: error of the forecast gain RMSE(n)/RMSE(n0) and balanced accuracy of the decision 'an 8× larger calibration set reduces RMSEP by ≥ 10%'.

| method | n tasks | mean task gain abs err | median task gain abs err | mean gain bias | decision 8x 10pct balanced acc | decision sensitivity | decision specificity | prevalence worthwhile |
|---|---|---|---|---|---|---|---|---|
| RPM | 38 | 0.231 | 0.209 | 0.209 | 0.516 | 0.282 | 0.750 | 0.970 |
| RPM-w | 38 | 0.222 | 0.182 | 0.197 | 0.506 | 0.262 | 0.750 | 0.970 |
| RPM-T | 38 | 0.297 | 0.223 | 0.114 | 0.575 | 0.399 | 0.750 | 0.970 |
| RPM-wT | 38 | 0.279 | 0.193 | 0.079 | 0.565 | 0.430 | 0.700 | 0.970 |
| IPL3 | 38 | 0.232 | 0.182 | -0.101 | 0.598 | 0.797 | 0.400 | 0.970 |
| IPL2 | 38 | 0.311 | 0.264 | -0.291 | 0.478 | 0.956 | 0.000 | 0.970 |
| EXP3 | 38 | 1.128 | 0.962 | -1.346 | 0.683 | 0.591 | 0.775 | 0.970 |
| LOG2 | 38 | 8.471 | 8.046 | -8.289 | 0.490 | 0.980 | 0.000 | 0.970 |
| FLAT | 38 | 0.245 | 0.211 | 0.243 | 0.500 | 0.000 | 1.000 | 0.970 |
| DFOLS | 38 | 0.471 | 0.190 | -0.155 | 0.634 | 0.793 | 0.475 | 0.970 |
| SLOPE-T | 38 | 0.124 | 0.094 | -0.022 | 0.500 | 1.000 | 0.000 | 0.970 |

**Table S22.** POST HOC: paired tests of gain error (reference: pre-registered RPM).

| reference | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM-w | 38 | 230.000 | 0.041 | -0.010 | -0.018 | -0.002 | -0.379 | 12 | 26 | 0.290 |
| RPM | RPM-T | 38 | 346.000 | 0.731 | -0.000755 | -0.011 | 0.008 | 0.066 | 17 | 21 | 1.000 |
| RPM | RPM-wT | 38 | 306.000 | 0.357 | -0.034 | -0.049 | -0.018 | -0.174 | 10 | 28 | 1.000 |
| RPM | IPL3 | 38 | 356.000 | 0.841 | -0.009 | -0.043 | 0.034 | -0.039 | 17 | 21 | 1.000 |
| RPM | IPL2 | 38 | 235.000 | 0.049 | 0.023 | -0.016 | 0.105 | 0.366 | 22 | 16 | 0.297 |
| RPM | EXP3 | 38 | 0.000 | 7.28e-12 | 0.793 | 0.355 | 1.002 | 1.000 | 38 | 0 | 7.28e-11 |
| RPM | LOG2 | 38 | 0.000 | 7.28e-12 | 7.862 | 6.886 | 9.566 | 1.000 | 38 | 0 | 7.28e-11 |
| RPM | FLAT | 38 | 316.000 | 0.438 | 0.003 | -0.024 | 0.040 | 0.147 | 20 | 18 | 1.000 |
| RPM | DFOLS | 38 | 260.000 | 0.111 | -0.021 | -0.069 | 0.271 | 0.298 | 17 | 21 | 0.557 |
| RPM | SLOPE-T | 38 | 44.000 | 1.08e-07 | -0.097 | -0.135 | -0.071 | -0.881 | 5 | 33 | 8.6e-07 |

**Table S23.** Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task).

| variant | n tasks | mean abs logerr | rpm same tasks | mean diff vs rpm | ci95 lo | ci95 hi | p raw | p holm | rank biserial |
|---|---|---|---|---|---|---|---|---|---|
| RPM | 38 | 0.242 | 0.242 | 0.000 | 0.000 | 0.000 | – | – | – |
| RPM-rfree | 38 | 0.573 | 0.242 | 0.331 | 0.232 | 0.436 | 4.66e-09 | 4.19e-08 | 0.938 |
| RPM-ML2 | 38 | 0.305 | 0.242 | 0.063 | 0.007 | 0.129 | 0.626 | 1.000 | 0.093 |
| RPM-pilotcov | 38 | 0.254 | 0.242 | 0.011 | -0.010 | 0.034 | 0.720 | 1.000 | 0.069 |
| RPM-pilotcov+tail | 38 | 0.309 | 0.242 | 0.066 | 0.048 | 0.085 | 4.17e-08 | 3.34e-07 | 0.900 |
| RPM-U250 | 38 | 0.239 | 0.242 | -0.003 | -0.007 | 0.000213 | 0.841 | 1.000 | -0.039 |
| RPM-Uextra | 14 | 0.207 | 0.210 | -0.003 | -0.006 | -0.000645 | 0.049 | 0.297 | -0.600 |
| RPM-kfold10 | 38 | 0.246 | 0.242 | 0.004 | -0.005 | 0.013 | 0.586 | 1.000 | 0.104 |
| RPM-cut0.5 | 38 | 0.275 | 0.242 | 0.033 | -0.019 | 0.090 | 0.438 | 1.000 | -0.147 |
| RPM-cut0.95 | 38 | 0.259 | 0.242 | 0.017 | 0.010 | 0.024 | 0.000228 | 0.002 | 0.860 |

**Table S24.** Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios).

| variant | method | n tasks | mean abs logerr | mean bias | coverage80 |
|---|---|---|---|---|---|
| iid_ref_seasons123 | FLAT | 1.000 | 0.160 | 0.143 | – |
| iid_ref_seasons123 | IPL3 | 1.000 | 0.729 | -0.639 | 80.000 |
| iid_ref_seasons123 | RPM | 1.000 | 0.328 | 0.328 | 6.667 |
| iid_ref_seasons123 | RPM-T | 1.000 | 0.250 | 0.248 | 21.111 |
| iid_ref_seasons123 | RPM-wT | 1.000 | 0.323 | 0.323 | 21.111 |
| ks_pilot | FLAT | 6.000 | 0.330 | 0.303 | – |
| ks_pilot | IPL3 | 6.000 | 0.316 | -0.007 | 72.391 |
| ks_pilot | RPM | 6.000 | 0.363 | 0.325 | 12.826 |
| ks_pilot | RPM-T | 6.000 | 0.365 | 0.266 | 16.957 |
| ks_pilot | RPM-wT | 6.000 | 0.353 | 0.238 | 18.261 |
| prep_raw | FLAT | 6.000 | 0.201 | 0.058 | – |
| prep_raw | IPL3 | 6.000 | 0.405 | -0.322 | 70.870 |
| prep_raw | RPM | 6.000 | 0.274 | 0.052 | 34.783 |
| prep_raw | RPM-T | 6.000 | 0.389 | -0.074 | 38.043 |
| prep_raw | RPM-wT | 6.000 | 0.384 | -0.070 | 42.174 |
| prep_sg1 | FLAT | 6.000 | 0.313 | 0.035 | – |
| prep_sg1 | IPL3 | 6.000 | 0.505 | -0.278 | 64.783 |
| prep_sg1 | RPM | 6.000 | 0.368 | 0.081 | 36.087 |
| prep_sg1 | RPM-T | 6.000 | 0.392 | 0.021 | 36.739 |
| prep_sg1 | RPM-wT | 6.000 | 0.387 | -0.017 | 40.870 |
| ref_noise | FLAT | 6.000 | 0.129 | 0.069 | – |
| ref_noise | IPL3 | 6.000 | 0.313 | -0.317 | 80.435 |
| ref_noise | RPM | 6.000 | 0.214 | 0.124 | 34.783 |
| ref_noise | RPM-T | 6.000 | 0.217 | 0.117 | 36.522 |
| ref_noise | RPM-wT | 6.000 | 0.182 | 0.069 | 43.261 |
| shift_population | FLAT | 1.000 | 0.201 | 0.196 | – |
| shift_population | IPL3 | 1.000 | 0.440 | -0.285 | 68.889 |
| shift_population | RPM | 1.000 | 0.351 | 0.348 | 5.556 |
| shift_population | RPM-T | 1.000 | 0.322 | 0.296 | 6.667 |
| shift_population | RPM-wT | 1.000 | 0.374 | 0.345 | 5.556 |
| shift_season | FLAT | 1.000 | 0.250 | -0.250 | – |
| shift_season | IPL3 | 1.000 | 1.034 | -1.034 | 16.667 |
| shift_season | RPM | 1.000 | 0.115 | -0.062 | 65.556 |
| shift_season | RPM-T | 1.000 | 0.196 | -0.174 | 42.222 |
| shift_season | RPM-wT | 1.000 | 0.162 | -0.098 | 60.000 |

**Table S25.** E0 simulation with Monte-Carlo ground truth (median absolute and signed log error).

| r | noise frac | n0 | method | median abs err | mean abs err | median bias |
|---|---|---|---|---|---|---|
| 0.500 | 0.100 | 30 | FLAT | 0.444 | 0.533 | 0.444 |
| 0.500 | 0.100 | 30 | IPL3 | 0.283 | 0.326 | 0.194 |
| 0.500 | 0.100 | 30 | RPM | 0.371 | 0.438 | 0.371 |
| 0.500 | 0.100 | 30 | RPM-T | 0.582 | 1.868 | 0.086 |
| 0.500 | 0.100 | 30 | RPM-w | 0.368 | 0.438 | 0.368 |
| 0.500 | 0.100 | 30 | RPM-wT | 0.583 | 1.892 | 0.095 |
| 0.500 | 0.100 | 60 | FLAT | 0.710 | 0.726 | 0.710 |
| 0.500 | 0.100 | 60 | IPL3 | 0.349 | 0.347 | 0.349 |
| 0.500 | 0.100 | 60 | RPM | 0.454 | 0.453 | 0.454 |
| 0.500 | 0.100 | 60 | RPM-T | 0.342 | 1.690 | 0.151 |
| 0.500 | 0.100 | 60 | RPM-w | 0.452 | 0.450 | 0.452 |
| 0.500 | 0.100 | 60 | RPM-wT | 0.342 | 1.697 | 0.151 |
| 0.500 | 0.100 | 120 | FLAT | 0.604 | 0.585 | 0.604 |
| 0.500 | 0.100 | 120 | IPL3 | 0.181 | 0.223 | 0.030 |
| 0.500 | 0.100 | 120 | RPM | 0.311 | 0.301 | 0.311 |
| 0.500 | 0.100 | 120 | RPM-T | 0.194 | 0.250 | 0.008 |
| 0.500 | 0.100 | 120 | RPM-w | 0.305 | 0.293 | 0.305 |
| 0.500 | 0.100 | 120 | RPM-wT | 0.196 | 0.252 | 0.008 |
| 0.500 | 0.300 | 30 | FLAT | 0.167 | 0.179 | 0.107 |
| 0.500 | 0.300 | 30 | IPL3 | 0.198 | 0.267 | -0.084 |
| 0.500 | 0.300 | 30 | RPM | 0.152 | 0.184 | 0.043 |
| 0.500 | 0.300 | 30 | RPM-T | 0.199 | 1.431 | -0.070 |
| 0.500 | 0.300 | 30 | RPM-w | 0.152 | 0.184 | 0.047 |
| 0.500 | 0.300 | 30 | RPM-wT | 0.209 | 1.535 | -0.071 |
| 0.500 | 0.300 | 60 | FLAT | 0.174 | 0.206 | 0.174 |
| 0.500 | 0.300 | 60 | IPL3 | 0.142 | 0.186 | -0.065 |
| 0.500 | 0.300 | 60 | RPM | 0.145 | 0.162 | 0.009 |
| 0.500 | 0.300 | 60 | RPM-T | 0.214 | 1.182 | -0.053 |
| 0.500 | 0.300 | 60 | RPM-w | 0.143 | 0.162 | 0.008 |
| 0.500 | 0.300 | 60 | RPM-wT | 0.211 | 1.161 | -0.053 |
| 0.500 | 0.300 | 120 | FLAT | 0.220 | 0.221 | 0.220 |
| 0.500 | 0.300 | 120 | IPL3 | 0.161 | 0.160 | 0.051 |
| 0.500 | 0.300 | 120 | RPM | 0.101 | 0.111 | 0.058 |
| 0.500 | 0.300 | 120 | RPM-T | 0.114 | 0.151 | -0.026 |
| 0.500 | 0.300 | 120 | RPM-w | 0.106 | 0.113 | 0.049 |
| 0.500 | 0.300 | 120 | RPM-wT | 0.117 | 0.153 | -0.029 |
| 1.000 | 0.100 | 30 | FLAT | 0.366 | 0.360 | 0.359 |
| 1.000 | 0.100 | 30 | IPL3 | 0.350 | 0.430 | -0.106 |
| 1.000 | 0.100 | 30 | RPM | 0.277 | 0.466 | 0.167 |
| 1.000 | 0.100 | 30 | RPM-T | 0.689 | 3.910 | -0.689 |
| 1.000 | 0.100 | 30 | RPM-w | 0.276 | 0.602 | 0.165 |
| 1.000 | 0.100 | 30 | RPM-wT | 0.674 | 3.859 | -0.674 |
| 1.000 | 0.100 | 60 | FLAT | 0.328 | 0.317 | 0.328 |
| 1.000 | 0.100 | 60 | IPL3 | 0.186 | 0.276 | -0.131 |
| 1.000 | 0.100 | 60 | RPM | 0.162 | 0.188 | -0.059 |
| 1.000 | 0.100 | 60 | RPM-T | 8.533 | 6.742 | -8.533 |
| 1.000 | 0.100 | 60 | RPM-w | 0.162 | 0.190 | -0.060 |
| 1.000 | 0.100 | 60 | RPM-wT | 9.178 | 6.882 | -9.178 |
| 1.000 | 0.100 | 120 | FLAT | 0.250 | 0.251 | 0.250 |
| 1.000 | 0.100 | 120 | IPL3 | 0.199 | 0.260 | -0.154 |
| 1.000 | 0.100 | 120 | RPM | 0.115 | 0.140 | 0.018 |
| 1.000 | 0.100 | 120 | RPM-T | 0.256 | 0.288 | -0.233 |
| 1.000 | 0.100 | 120 | RPM-w | 0.114 | 0.143 | 0.014 |
| 1.000 | 0.100 | 120 | RPM-wT | 0.260 | 0.288 | -0.231 |
| 1.000 | 0.300 | 30 | FLAT | 0.154 | 0.189 | 0.152 |
| 1.000 | 0.300 | 30 | IPL3 | 0.253 | 0.314 | -0.153 |
| 1.000 | 0.300 | 30 | RPM | 0.105 | 0.135 | 0.005 |
| 1.000 | 0.300 | 30 | RPM-T | 0.580 | 2.294 | -0.580 |
| 1.000 | 0.300 | 30 | RPM-w | 0.105 | 0.135 | 0.005 |
| 1.000 | 0.300 | 30 | RPM-wT | 0.584 | 2.530 | -0.584 |

**Table S26.** E0 simulation summarised by pilot size.

| method | n0 | median abs err | median bias |
|---|---|---|---|
| FLAT | 30 | 0.201 | 0.154 |
| FLAT | 60 | 0.179 | 0.178 |
| FLAT | 120 | 0.186 | 0.186 |
| IPL3 | 30 | 0.258 | -0.077 |
| IPL3 | 60 | 0.244 | -0.149 |
| IPL3 | 120 | 0.124 | -0.019 |
| RPM | 30 | 0.206 | 0.046 |
| RPM | 60 | 0.175 | 0.030 |
| RPM | 120 | 0.109 | 0.038 |
| RPM-T | 30 | 0.621 | -0.581 |
| RPM-T | 60 | 0.319 | -0.223 |
| RPM-T | 120 | 0.137 | -0.063 |
| RPM-w | 30 | 0.206 | 0.046 |
| RPM-w | 60 | 0.173 | 0.028 |
| RPM-w | 120 | 0.110 | 0.039 |
| RPM-wT | 30 | 0.623 | -0.582 |
| RPM-wT | 60 | 0.330 | -0.247 |
| RPM-wT | 120 | 0.136 | -0.063 |

**Table S27.** Per-task error analysis (RPM vs IPL3) with spectral and fitted descriptors.

| task | family | eigen decay exponent | n pool | rpm mae | rpm bias | theory fit err | noise frac | r | ipl3 mae |
|---|---|---|---|---|---|---|---|---|---|
| Diesel:total | fuel | 3.803 | 296 | 1.037 | -1.034 | 0.378 | 0.062 | 0.865 | 1.285 |
| KSSL-MIR:OC | soil | 2.757 | 12002 | 0.624 | -0.456 | 0.098 | 0.018 | 0.839 | 0.809 |
| Tablets:assay | pharma | 3.208 | 491 | 0.474 | -0.335 | 0.123 | 0.042 | 0.868 | 0.510 |
| CGL:casein | mixture | 4.899 | 173 | 0.410 | 0.384 | 0.090 | 0.000219 | 0.652 | 0.358 |
| Diesel:d4052 | fuel | 3.784 | 296 | 0.383 | 0.232 | 0.120 | 0.004 | 0.653 | 0.513 |
| Diesel:cn | fuel | 3.809 | 286 | 0.346 | 0.305 | 0.221 | 0.599 | 0.675 | 0.190 |
| KSSL-VisNIR:OC | soil | 3.860 | 11997 | 0.312 | 0.163 | 0.090 | 0.208 | 0.400 | 0.542 |
| CGL:glucose | mixture | 4.886 | 173 | 0.291 | 0.208 | 0.059 | 0.000181 | 0.632 | 0.442 |
| KSSL-MIR:CEC | soil | 2.763 | 12001 | 0.280 | -0.027 | 0.157 | 0.046 | 0.653 | 0.655 |
| ICRAF-MIR:OC | soil | 2.787 | 2774 | 0.273 | 0.162 | 0.069 | 0.102 | 0.631 | 0.401 |
| AfSIS1-MIR:OC | soil | 2.956 | 1425 | 0.273 | -0.085 | 0.121 | 0.046 | 0.683 | 0.471 |
| CGL:lactate | mixture | 4.901 | 173 | 0.271 | 0.121 | 0.330 | 0.000142 | 0.698 | 0.259 |
| CGL:moisture | mixture | 4.910 | 173 | 0.270 | 0.186 | 0.287 | 0.000153 | 0.711 | 0.285 |
| ICRAF-VisNIR:CEC | soil | 3.657 | 2735 | 0.269 | 0.134 | 0.146 | 0.663 | 0.571 | 0.325 |
| Tecator:fat | meat | 5.647 | 180 | 0.266 | -0.162 | 0.177 | 0.021 | 0.692 | 0.425 |
| Diesel:bp50 | fuel | 3.785 | 296 | 0.266 | 0.162 | 0.167 | 0.043 | 0.579 | 0.363 |
| ICRAF-MIR:CEC | soil | 2.803 | 2738 | 0.260 | 0.114 | 0.071 | 0.166 | 0.688 | 0.340 |
| ICRAF-VisNIR:OC | soil | 3.665 | 2774 | 0.258 | 0.122 | 0.055 | 0.459 | 0.339 | 0.277 |
| Neospectra-NIR:OC | soil | 3.907 | 1579 | 0.254 | 0.042 | 0.075 | 0.271 | 0.454 | 0.360 |
| KSSL-VisNIR:pH | soil | 3.828 | 11993 | 0.248 | 0.160 | 0.102 | 0.333 | 0.340 | 0.511 |
| Mango:DM | fruit | 4.480 | 3016 | 0.243 | 0.225 | 0.074 | 0.166 | 0.313 | 0.680 |
| KSSL-MIR:clay | soil | 2.742 | 11997 | 0.243 | 0.049 | 0.084 | 0.131 | 0.470 | 0.563 |
| ICRAF-VisNIR:clay | soil | 3.661 | 2803 | 0.237 | 0.136 | 0.117 | 0.526 | 0.384 | 0.311 |
| KSSL-VisNIR:CEC | soil | 3.831 | 12011 | 0.236 | 0.118 | 0.084 | 0.400 | 0.360 | 0.444 |
| Diesel:visc | fuel | 3.782 | 296 | 0.236 | -0.036 | 0.074 | 0.094 | 0.544 | 0.369 |
| Diesel:freeze | fuel | 3.774 | 296 | 0.231 | 0.053 | 0.024 | 0.187 | 0.568 | 0.290 |
| AfSIS1-MIR:clay | soil | 2.952 | 1421 | 0.222 | -0.069 | 0.108 | 0.155 | 0.520 | 0.345 |
| Neospectra-NIR:clay | soil | 3.909 | 1580 | 0.220 | -0.092 | 0.075 | 0.376 | 0.376 | 0.389 |
| AfSIS1-MIR:pH | soil | 2.966 | 1427 | 0.218 | -0.064 | 0.164 | 0.139 | 0.518 | 0.418 |
| KSSL-MIR:pH | soil | 2.758 | 12002 | 0.206 | 0.118 | 0.046 | 0.184 | 0.525 | 0.479 |
| Neospectra-NIR:pH | soil | 3.921 | 1571 | 0.197 | 0.098 | 0.041 | 0.304 | 0.363 | 0.321 |
| Neospectra-NIR:CEC | soil | 3.902 | 1572 | 0.192 | 0.085 | 0.064 | 0.396 | 0.405 | 0.294 |
| ICRAF-MIR:clay | soil | 2.799 | 2802 | 0.190 | 0.064 | 0.047 | 0.200 | 0.536 | 0.311 |
| ICRAF-MIR:pH | soil | 2.811 | 2827 | 0.190 | 0.032 | 0.067 | 0.206 | 0.618 | 0.396 |
| KSSL-VisNIR:clay | soil | 3.887 | 11997 | 0.187 | 0.110 | 0.054 | 0.393 | 0.351 | 0.485 |
| Tecator:protein | meat | 5.657 | 180 | 0.169 | 0.114 | 0.043 | 0.034 | 0.423 | 0.329 |
| ICRAF-VisNIR:pH | soil | 3.659 | 2828 | 0.165 | 0.048 | 0.067 | 0.331 | 0.362 | 0.342 |
| Tecator:moisture | meat | 5.613 | 180 | 0.148 | 0.057 | 0.111 | 0.040 | 0.757 | 0.223 |

**Table S28.** Spearman correlations between per-task RPM error and task descriptors.

| descriptor | spearman rho | p | n |
|---|---|---|---|
| eigen_decay_exponent | -0.064 | 0.701 | 38 |
| theory_fit_err | 0.574 | 0.000164 | 38 |
| noise_frac | -0.394 | 0.014 | 38 |
| r | 0.563 | 0.000237 | 38 |
| n_pool | -0.203 | 0.222 | 38 |

**Table S29.** Accuracy by data-set family.

| family | method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fruit | RPM | RPM (pre-registered, r = 1) | 1 | 0.243 | 0.243 | 0.243 | 0.243 | 0.231 | 0.225 | 12.778 | 30.833 |
| fruit | IPL3 | Inverse power law (IPL3) | 1 | 0.680 | 0.680 | 0.680 | 0.680 | 0.223 | -0.574 | 25.833 | 44.722 |
| fruit | FLAT | No improvement (FLAT) | 1 | 0.167 | 0.167 | 0.167 | 0.167 | 0.124 | 0.125 | 40.833 | 65.556 |
| fruit | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 0.373 | 0.373 | 0.373 | 0.373 | 0.138 | -0.320 | 35.833 | 59.167 |
| fuel | RPM | RPM (pre-registered, r = 1) | 6 | 0.417 | 0.258 | 0.673 | 0.306 | 0.290 | -0.053 | 18.611 | 33.889 |
| fuel | IPL3 | Inverse power law (IPL3) | 6 | 0.502 | 0.282 | 0.827 | 0.366 | 0.317 | -0.290 | 13.472 | 27.917 |
| fuel | FLAT | No improvement (FLAT) | 6 | 0.402 | 0.239 | 0.611 | 0.293 | 0.279 | 0.068 | 19.861 | 34.583 |
| fuel | DFOLS | Fixed-complexity formula (DF-OLS) | 6 | 2.312 | 1.205 | 3.276 | 2.737 | 0.483 | -2.216 | 11.250 | 22.222 |
| meat | RPM | RPM (pre-registered, r = 1) | 3 | 0.194 | 0.148 | 0.266 | 0.169 | 0.157 | 0.003 | 32.222 | 57.222 |
| meat | IPL3 | Inverse power law (IPL3) | 3 | 0.326 | 0.223 | 0.425 | 0.329 | 0.252 | -0.197 | 24.444 | 38.889 |
| meat | FLAT | No improvement (FLAT) | 3 | 0.203 | 0.178 | 0.247 | 0.183 | 0.160 | 0.038 | 28.333 | 54.444 |
| meat | DFOLS | Fixed-complexity formula (DF-OLS) | 3 | 0.786 | 0.574 | 0.968 | 0.815 | 0.357 | -0.723 | 14.444 | 29.444 |
| mixture | RPM | RPM (pre-registered, r = 1) | 4 | 0.311 | 0.271 | 0.375 | 0.281 | 0.247 | 0.225 | 20.417 | 36.667 |
| mixture | IPL3 | Inverse power law (IPL3) | 4 | 0.336 | 0.272 | 0.403 | 0.322 | 0.263 | 0.024 | 21.667 | 39.583 |
| mixture | FLAT | No improvement (FLAT) | 4 | 0.437 | 0.374 | 0.531 | 0.407 | 0.380 | 0.409 | 11.250 | 21.250 |
| mixture | DFOLS | Fixed-complexity formula (DF-OLS) | 4 | 2.055 | 1.647 | 2.658 | 1.808 | 0.373 | -1.885 | 13.750 | 25.000 |
| pharma | RPM | RPM (pre-registered, r = 1) | 1 | 0.474 | 0.474 | 0.474 | 0.474 | 0.390 | -0.335 | 12.000 | 18.500 |
| pharma | IPL3 | Inverse power law (IPL3) | 1 | 0.510 | 0.510 | 0.510 | 0.510 | 0.410 | -0.399 | 6.000 | 15.000 |
| pharma | FLAT | No improvement (FLAT) | 1 | 0.327 | 0.327 | 0.327 | 0.327 | 0.313 | -0.114 | 13.500 | 23.000 |
| pharma | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 0.839 | 0.839 | 0.839 | 0.839 | 0.477 | -0.723 | 12.000 | 16.500 |
| soil | RPM | RPM (pre-registered, r = 1) | 23 | 0.250 | 0.222 | 0.290 | 0.237 | 0.184 | 0.042 | 27.533 | 49.544 |
| soil | IPL3 | Inverse power law (IPL3) | 23 | 0.426 | 0.379 | 0.480 | 0.396 | 0.283 | -0.303 | 20.133 | 35.622 |
| soil | FLAT | No improvement (FLAT) | 23 | 0.211 | 0.190 | 0.232 | 0.203 | 0.177 | 0.134 | 28.222 | 51.433 |
| soil | DFOLS | Fixed-complexity formula (DF-OLS) | 23 | 0.986 | 0.641 | 1.389 | 0.569 | 0.180 | -0.872 | 28.522 | 50.378 |

**Table S30.** Measured run time per pilot.

| component | mean | median | max |
|---|---|---|---|
| RPM point forecast + 50 bootstrap refits (s per pilot) | 1.552 | 1.399 | 4.807 |
| Within-pilot sub-sampling curve for IPL/EXP/LOG fits (s per pilot) | 0.524 | 0.321 | 3.354 |

**Table S31.** Paired tests against RPM at pilot size n0 = 25.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | RPM-w | 38 | 192.000 | 0.009 | -0.008 | -0.017 | -0.004 | -0.482 | 11 | 27 | 0.020 |
| 25 | RPM-T | 38 | 16.000 | 1.23e-09 | 0.257 | 0.037 | 0.325 | 0.957 | 37 | 1 | 8.61e-09 |
| 25 | RPM-wT | 38 | 59.000 | 6.49e-07 | 0.230 | 0.031 | 0.290 | 0.841 | 30 | 8 | 2.6e-06 |
| 25 | IPL3 | 38 | 54.000 | 3.67e-07 | 0.215 | 0.108 | 0.271 | 0.854 | 31 | 7 | 1.84e-06 |
| 25 | IPL2 | 38 | 22.000 | 3.9e-09 | 0.345 | 0.195 | 0.464 | 0.941 | 34 | 4 | 2.34e-08 |
| 25 | EXP3 | 38 | 0.000 | 7.28e-12 | 2.351 | 1.800 | 3.208 | 1.000 | 38 | 0 | 7.28e-11 |
| 25 | LOG2 | 38 | 0.000 | 7.28e-12 | 12.154 | 11.292 | 12.931 | 1.000 | 38 | 0 | 7.28e-11 |
| 25 | FLAT | 38 | 297.000 | 0.293 | -0.015 | -0.056 | 0.025 | -0.198 | 15 | 23 | 0.293 |
| 25 | DFOLS | 38 | 14.000 | 8e-10 | 0.964 | 0.796 | 1.854 | 0.962 | 35 | 3 | 6.4e-09 |
| 25 | SLOPE-T | 38 | 186.000 | 0.007 | -0.033 | -0.065 | 0.005 | -0.498 | 15 | 23 | 0.020 |

**Table S32.** Paired tests against RPM at pilot size n0 = 50.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | RPM-w | 38 | 240.000 | 0.059 | -0.002 | -0.014 | -0.000856 | -0.352 | 11 | 27 | 0.191 |
| 50 | RPM-T | 38 | 61.000 | 8.09e-07 | 0.023 | 0.009 | 0.038 | 0.835 | 32 | 6 | 4.85e-06 |
| 50 | RPM-wT | 38 | 234.000 | 0.048 | 0.015 | -0.013 | 0.039 | 0.368 | 23 | 15 | 0.191 |
| 50 | IPL3 | 38 | 28.000 | 1.08e-08 | 0.123 | 0.083 | 0.202 | 0.924 | 36 | 2 | 7.55e-08 |
| 50 | IPL2 | 38 | 16.000 | 1.23e-09 | 0.290 | 0.151 | 0.349 | 0.957 | 36 | 2 | 9.84e-09 |
| 50 | EXP3 | 38 | 0.000 | 7.28e-12 | 0.987 | 0.414 | 1.664 | 1.000 | 38 | 0 | 7.28e-11 |
| 50 | LOG2 | 38 | 0.000 | 7.28e-12 | 11.016 | 10.020 | 11.661 | 1.000 | 38 | 0 | 7.28e-11 |
| 50 | FLAT | 38 | 279.000 | 0.189 | -0.014 | -0.033 | 0.000962 | -0.247 | 13 | 25 | 0.236 |
| 50 | DFOLS | 38 | 102.000 | 3.65e-05 | 0.106 | 0.035 | 0.633 | 0.725 | 29 | 9 | 0.000182 |
| 50 | SLOPE-T | 38 | 262.000 | 0.118 | -0.019 | -0.042 | 0.010 | -0.293 | 17 | 21 | 0.236 |

**Table S33.** Paired tests against RPM at pilot size n0 = 100.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | RPM-w | 31 | 104.000 | 0.004 | -0.011 | -0.032 | -0.003 | -0.581 | 7 | 24 | 0.025 |
| 100 | RPM-T | 31 | 144.000 | 0.041 | 0.004 | 0.000197 | 0.013 | 0.419 | 21 | 10 | 0.165 |
| 100 | RPM-wT | 31 | 176.000 | 0.163 | -0.025 | -0.036 | -0.000283 | -0.290 | 10 | 21 | 0.327 |
| 100 | IPL3 | 31 | 103.000 | 0.004 | 0.083 | 0.015 | 0.112 | 0.585 | 23 | 8 | 0.025 |
| 100 | IPL2 | 31 | 39.000 | 7.01e-06 | 0.162 | 0.093 | 0.244 | 0.843 | 26 | 5 | 5.61e-05 |
| 100 | EXP3 | 31 | 18.000 | 2.36e-07 | 0.674 | 0.386 | 0.901 | 0.927 | 28 | 3 | 2.12e-06 |
| 100 | LOG2 | 31 | 1.000 | 1.86e-09 | 7.090 | 5.534 | 8.929 | 0.996 | 30 | 1 | 1.86e-08 |
| 100 | FLAT | 31 | 138.000 | 0.030 | -0.018 | -0.035 | 0.000652 | -0.444 | 11 | 20 | 0.152 |
| 100 | DFOLS | 31 | 194.000 | 0.299 | 0.000884 | -0.059 | 0.083 | 0.218 | 16 | 15 | 0.327 |
| 100 | SLOPE-T | 31 | 164.000 | 0.102 | -0.027 | -0.050 | 0.013 | -0.339 | 12 | 19 | 0.307 |

**Table S34.** Paired tests against RPM at pilot size n0 = 200.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 200 | RPM-w | 25 | 102.000 | 0.107 | -0.006 | -0.018 | 0.002 | -0.372 | 8 | 17 | 0.429 |
| 200 | RPM-T | 25 | 84.000 | 0.034 | -0.006 | -0.008 | 0.000591 | -0.483 | 8 | 17 | 0.171 |
| 200 | RPM-wT | 25 | 38.000 | 0.000376 | -0.025 | -0.045 | -0.010 | -0.766 | 5 | 20 | 0.003 |
| 200 | IPL3 | 25 | 118.000 | 0.241 | 0.017 | -0.026 | 0.065 | 0.274 | 15 | 10 | 0.482 |
| 200 | IPL2 | 25 | 47.000 | 0.001 | 0.078 | 0.002 | 0.145 | 0.711 | 18 | 7 | 0.008 |
| 200 | EXP3 | 25 | 12.000 | 4.17e-06 | 0.228 | 0.082 | 0.414 | 0.926 | 23 | 2 | 3.76e-05 |
| 200 | LOG2 | 25 | 0.000 | 5.96e-08 | 2.965 | 1.546 | 5.885 | 1.000 | 25 | 0 | 5.96e-07 |
| 200 | FLAT | 25 | 68.000 | 0.010 | -0.019 | -0.043 | 0.000192 | -0.582 | 8 | 17 | 0.058 |
| 200 | DFOLS | 25 | 109.000 | 0.156 | -0.016 | -0.067 | 0.026 | -0.329 | 12 | 13 | 0.469 |
| 200 | SLOPE-T | 25 | 126.000 | 0.339 | -0.018 | -0.077 | 0.043 | -0.225 | 10 | 15 | 0.482 |

![**Figure S1.** Pre-registered sample-size decision metric by method.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig10_sample_size_decisions.png){width=15cm}

![**Figure S2.** Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig9_error_analysis.png){width=15cm}

![**Figure S3.** Data-set overview: number of samples and eigen-decay exponent by family.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig11_dataset_overview.png){width=15cm}

# Supplementary Note 1: Pre-registered experimental design


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


# Supplementary Note 2: Data-leakage audit


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


# Supplementary Note 3: Literature matrix and novelty map


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

