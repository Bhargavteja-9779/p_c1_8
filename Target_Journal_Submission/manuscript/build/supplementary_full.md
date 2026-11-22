# Supplementary Material

**What a pilot set can tell about a calibration learning curve: an observability limit and Bayesian regularisation-path matching for sample-size planning in spectroscopy**

All tables and figures below are generated automatically by `run_all.py` from the per-pilot raw results.

**Table S1.** Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60).

| task | n pool | n test | p | max n truth | eigen decay exponent | truth seconds | family |
|---|---|---|---|---|---|---|---|
| AfSIS1-MIR:OC | 1425 | 477 | 212 | 800 | 2.954 | 7.415 | soil |
| AfSIS1-MIR:clay | 1422 | 474 | 212 | 800 | 2.952 | 7.886 | soil |
| AfSIS1-MIR:pH | 1427 | 477 | 212 | 800 | 2.960 | 7.695 | soil |
| CGL:casein | 173 | 58 | 116 | 100 | 4.899 | 1.356 | mixture |
| CGL:glucose | 173 | 58 | 116 | 100 | 4.886 | 1.536 | mixture |
| CGL:lactate | 173 | 58 | 116 | 100 | 4.901 | 1.373 | mixture |
| CGL:moisture | 173 | 58 | 116 | 100 | 4.910 | 1.354 | mixture |
| Diesel:bp50 | 296 | 99 | 200 | 200 | 3.785 | 3.108 | fuel |
| Diesel:cn | 286 | 95 | 200 | 200 | 3.809 | 3.335 | fuel |
| Diesel:d4052 | 296 | 99 | 200 | 200 | 3.784 | 3.208 | fuel |
| Diesel:freeze | 296 | 99 | 200 | 200 | 3.774 | 3.431 | fuel |
| Diesel:total | 296 | 99 | 200 | 200 | 3.803 | 3.088 | fuel |
| Diesel:visc | 296 | 99 | 200 | 200 | 3.782 | 2.910 | fuel |
| ICRAF-MIR:CEC | 2736 | 916 | 212 | 1600 | 2.800 | 11.196 | soil |
| ICRAF-MIR:OC | 2771 | 927 | 212 | 1600 | 2.803 | 10.735 | soil |
| ICRAF-MIR:clay | 2801 | 937 | 212 | 1600 | 2.802 | 10.709 | soil |
| ICRAF-MIR:pH | 2830 | 944 | 212 | 1600 | 2.823 | 10.906 | soil |
| ICRAF-VisNIR:CEC | 2740 | 914 | 208 | 1600 | 3.643 | 10.118 | soil |
| ICRAF-VisNIR:OC | 2775 | 925 | 208 | 1600 | 3.655 | 10.636 | soil |
| ICRAF-VisNIR:clay | 2805 | 935 | 208 | 1600 | 3.671 | 10.570 | soil |
| ICRAF-VisNIR:pH | 2828 | 948 | 208 | 1600 | 3.658 | 10.358 | soil |
| KSSL-MIR:CEC | 12001 | 3000 | 212 | 6400 | 2.763 | 21.487 | soil |
| KSSL-MIR:OC | 12002 | 3001 | 212 | 6400 | 2.757 | 20.283 | soil |
| KSSL-MIR:clay | 11997 | 3003 | 212 | 6400 | 2.742 | 22.513 | soil |
| KSSL-MIR:pH | 12002 | 3001 | 212 | 6400 | 2.758 | 24.151 | soil |
| KSSL-VisNIR:CEC | 12011 | 3000 | 208 | 6400 | 3.831 | 23.183 | soil |
| KSSL-VisNIR:OC | 11997 | 3005 | 208 | 6400 | 3.860 | 19.322 | soil |
| KSSL-VisNIR:clay | 11997 | 3005 | 208 | 6400 | 3.887 | 22.154 | soil |
| KSSL-VisNIR:pH | 11993 | 3007 | 208 | 6400 | 3.828 | 21.129 | soil |
| Mango:DM | 3016 | 1005 | 94 | 1600 | 4.480 | 5.508 | fruit |
| Neospectra-NIR:CEC | 1571 | 525 | 150 | 800 | 3.903 | 4.721 | soil |
| Neospectra-NIR:OC | 1580 | 526 | 150 | 800 | 3.908 | 4.934 | soil |
| Neospectra-NIR:clay | 1580 | 526 | 150 | 800 | 3.912 | 4.787 | soil |
| Neospectra-NIR:pH | 1572 | 524 | 150 | 800 | 3.920 | 4.911 | soil |
| Tablets:assay | 491 | 164 | 216 | 400 | 3.208 | 4.543 | pharma |
| Tecator:fat | 161 | 54 | 99 | 100 | 5.686 | 1.213 | meat |
| Tecator:moisture | 161 | 54 | 99 | 100 | 5.677 | 1.343 | meat |
| Tecator:protein | 161 | 54 | 99 | 100 | 5.669 | 1.247 | meat |

**Table S2.** Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves (absolute log error per task).

| task | mode | mean abs err ridge | mean abs err pls | r | noise frac |
|---|---|---|---|---|---|
| AfSIS1-MIR:OC | fixed1 | 0.115 | 0.128 | 1.000 | 0.064 |
| AfSIS1-MIR:OC | free | 0.054 | 0.057 | 0.694 | 0.059 |
| AfSIS1-MIR:clay | fixed1 | 0.132 | 0.163 | 1.000 | 0.187 |
| AfSIS1-MIR:clay | free | 0.058 | 0.089 | 0.531 | 0.170 |
| AfSIS1-MIR:pH | fixed1 | 0.224 | 0.236 | 1.000 | 0.157 |
| AfSIS1-MIR:pH | free | 0.112 | 0.124 | 0.508 | 0.135 |
| CGL:casein | fixed1 | 0.370 | 0.353 | 1.000 | 0.000442 |
| CGL:casein | free | 0.194 | 0.177 | 0.652 | 0.000219 |
| CGL:glucose | fixed1 | 0.364 | 0.363 | 1.000 | 0.000384 |
| CGL:glucose | free | 0.208 | 0.224 | 0.629 | 0.000181 |
| CGL:lactate | fixed1 | 0.478 | 0.562 | 1.000 | 0.000268 |
| CGL:lactate | free | 0.404 | 0.487 | 0.699 | 0.000144 |
| CGL:moisture | fixed1 | 0.423 | 0.460 | 1.000 | 0.000267 |
| CGL:moisture | free | 0.353 | 0.390 | 0.712 | 0.000155 |
| Diesel:bp50 | fixed1 | 0.200 | 0.202 | 1.000 | 0.059 |
| Diesel:bp50 | free | 0.183 | 0.149 | 0.582 | 0.044 |
| Diesel:cn | fixed1 | 0.181 | 0.152 | 1.000 | 0.613 |
| Diesel:cn | free | 0.183 | 0.154 | 0.679 | 0.598 |
| Diesel:d4052 | fixed1 | 0.369 | 0.384 | 1.000 | 0.006 |
| Diesel:d4052 | free | 0.140 | 0.148 | 0.656 | 0.004 |
| Diesel:freeze | fixed1 | 0.129 | 0.185 | 1.000 | 0.221 |
| Diesel:freeze | free | 0.048 | 0.097 | 0.573 | 0.187 |
| Diesel:total | fixed1 | 0.276 | 0.298 | 1.000 | 0.063 |
| Diesel:total | free | 0.278 | 0.284 | 0.859 | 0.061 |
| Diesel:visc | fixed1 | 0.241 | 0.277 | 1.000 | 0.122 |
| Diesel:visc | free | 0.121 | 0.156 | 0.548 | 0.094 |
| ICRAF-MIR:CEC | fixed1 | 0.106 | 0.142 | 1.000 | 0.135 |
| ICRAF-MIR:CEC | free | 0.054 | 0.089 | 0.660 | 0.127 |
| ICRAF-MIR:OC | fixed1 | 0.186 | 0.187 | 1.000 | 0.113 |
| ICRAF-MIR:OC | free | 0.137 | 0.130 | 0.671 | 0.106 |
| ICRAF-MIR:clay | fixed1 | 0.127 | 0.165 | 1.000 | 0.232 |
| ICRAF-MIR:clay | free | 0.063 | 0.102 | 0.552 | 0.215 |
| ICRAF-MIR:pH | fixed1 | 0.143 | 0.176 | 1.000 | 0.201 |
| ICRAF-MIR:pH | free | 0.087 | 0.127 | 0.595 | 0.187 |
| ICRAF-VisNIR:CEC | fixed1 | 0.057 | 0.091 | 1.000 | 0.571 |
| ICRAF-VisNIR:CEC | free | 0.030 | 0.063 | 0.538 | 0.549 |
| ICRAF-VisNIR:OC | fixed1 | 0.148 | 0.183 | 1.000 | 0.478 |
| ICRAF-VisNIR:OC | free | 0.084 | 0.122 | 0.396 | 0.426 |
| ICRAF-VisNIR:clay | fixed1 | 0.168 | 0.203 | 1.000 | 0.438 |
| ICRAF-VisNIR:clay | free | 0.099 | 0.134 | 0.338 | 0.375 |
| ICRAF-VisNIR:pH | fixed1 | 0.132 | 0.147 | 1.000 | 0.444 |
| ICRAF-VisNIR:pH | free | 0.045 | 0.060 | 0.342 | 0.371 |
| KSSL-MIR:CEC | fixed1 | 0.203 | 0.220 | 1.000 | 0.051 |
| KSSL-MIR:CEC | free | 0.137 | 0.165 | 0.648 | 0.046 |
| KSSL-MIR:OC | fixed1 | 0.150 | 0.173 | 1.000 | 0.019 |
| KSSL-MIR:OC | free | 0.121 | 0.145 | 0.837 | 0.018 |
| KSSL-MIR:clay | fixed1 | 0.208 | 0.218 | 1.000 | 0.153 |
| KSSL-MIR:clay | free | 0.109 | 0.147 | 0.468 | 0.131 |
| KSSL-MIR:pH | fixed1 | 0.118 | 0.120 | 1.000 | 0.205 |
| KSSL-MIR:pH | free | 0.044 | 0.061 | 0.524 | 0.184 |
| KSSL-VisNIR:CEC | fixed1 | 0.166 | 0.188 | 1.000 | 0.462 |
| KSSL-VisNIR:CEC | free | 0.101 | 0.142 | 0.362 | 0.400 |
| KSSL-VisNIR:OC | fixed1 | 0.221 | 0.236 | 1.000 | 0.260 |
| KSSL-VisNIR:OC | free | 0.119 | 0.159 | 0.401 | 0.208 |
| KSSL-VisNIR:clay | fixed1 | 0.137 | 0.141 | 1.000 | 0.457 |
| KSSL-VisNIR:clay | free | 0.076 | 0.098 | 0.352 | 0.393 |
| KSSL-VisNIR:pH | fixed1 | 0.176 | 0.193 | 1.000 | 0.405 |
| KSSL-VisNIR:pH | free | 0.115 | 0.151 | 0.342 | 0.333 |
| Mango:DM | fixed1 | 0.186 | 0.182 | 1.000 | 0.320 |
| Mango:DM | free | 0.079 | 0.078 | 0.317 | 0.166 |

**Table S3.** κ-collapse: across-n standard deviation of rescaled log test errors plotted against κ, compared with the same errors plotted against the raw penalty μ.

| task | n curves | collapse sd log | no collapse ref sd log |
|---|---|---|---|
| Tecator:moisture | 3 | 0.062 | 0.237 |
| CGL:casein | 3 | 0.061 | 0.367 |
| ICRAF-MIR:clay | 7 | 0.013 | 0.513 |
| ICRAF-MIR:CEC | 7 | 0.020 | 0.502 |
| Neospectra-NIR:CEC | 6 | 0.030 | 0.563 |
| Diesel:bp50 | 4 | 0.049 | 0.454 |
| ICRAF-VisNIR:clay | 7 | 0.014 | 0.486 |
| AfSIS1-MIR:OC | 6 | 0.020 | 0.533 |
| AfSIS1-MIR:clay | 6 | 0.014 | 0.514 |
| KSSL-MIR:clay | 9 | 0.022 | 0.680 |
| Tablets:assay | 5 | 0.037 | 0.330 |
| Diesel:cn | 4 | 0.055 | 0.449 |
| Diesel:total | 4 | 0.032 | 0.329 |
| Neospectra-NIR:pH | 6 | 0.025 | 0.516 |
| Mango:DM | 7 | 0.042 | 0.351 |
| ICRAF-VisNIR:pH | 7 | 0.036 | 0.544 |
| Tecator:protein | 3 | 0.034 | 0.144 |
| Tecator:fat | 3 | 0.069 | 0.237 |
| CGL:lactate | 3 | 0.101 | 0.418 |
| ICRAF-VisNIR:CEC | 7 | 0.032 | 0.555 |
| KSSL-VisNIR:CEC | 9 | 0.089 | 0.829 |
| KSSL-VisNIR:OC | 9 | 0.079 | 0.795 |
| AfSIS1-MIR:pH | 6 | 0.019 | 0.519 |
| ICRAF-MIR:pH | 7 | 0.047 | 0.662 |
| Diesel:visc | 4 | 0.060 | 0.453 |
| KSSL-MIR:OC | 9 | 0.097 | 0.759 |
| ICRAF-VisNIR:OC | 7 | 0.032 | 0.560 |
| CGL:glucose | 3 | 0.157 | 0.461 |
| Neospectra-NIR:clay | 6 | 0.028 | 0.529 |
| CGL:moisture | 3 | 0.026 | 0.313 |
| ICRAF-MIR:OC | 7 | 0.053 | 0.717 |
| KSSL-VisNIR:pH | 9 | 0.064 | 0.788 |
| Diesel:freeze | 4 | 0.037 | 0.369 |
| Neospectra-NIR:OC | 6 | 0.015 | 0.438 |
| KSSL-MIR:CEC | 9 | 0.036 | 0.674 |
| KSSL-MIR:pH | 9 | 0.019 | 0.723 |
| Diesel:d4052 | 4 | 0.060 | 0.531 |
| KSSL-VisNIR:clay | 9 | 0.059 | 0.812 |

**Table S4.** POST HOC: regression of the ground-truth learning-curve slope (log RMSE per doubling of n) on large-sample theory parameters, and Spearman correlations.

| descriptor | spearman rho | p | r2 |
|---|---|---|---|
| noise_frac_full_pool | 0.541 | 0.000455 | – |
| r_full_pool | -0.331 | 0.042 | – |
| eigen_decay_exponent | -0.261 | 0.114 | – |
| n_pool | 0.453 | 0.004 | – |
| OLS: slope ~ r + log(noise fraction) + eigen-decay | – | 2.3e-11 | 0.783 |

**Table S5.** POST HOC: learning-curve slopes and alignment exponents by spectral region.

| region | count | median | min | max |
|---|---|---|---|---|
| CGL | 4 | -0.516 | -0.557 | -0.478 |
| Diesel | 6 | -0.198 | -0.413 | 0.107 |
| MIR (soil) | 11 | -0.107 | -0.157 | -0.060 |
| Mango | 1 | -0.088 | -0.088 | -0.088 |
| Tablets | 1 | -0.077 | -0.077 | -0.077 |
| Tecator | 3 | -0.122 | -0.176 | 0.013 |
| Vis/NIR (soil) | 12 | -0.083 | -0.108 | -0.047 |

**Table S6.** All forecasters on the version-2 design: task-level mean absolute log error (level), mean absolute gain error, mean signed bias, and source-level means.

| method | n tasks | level mae | level median | mean bias | gain mae | gain median | level mae source | gain mae source |
|---|---|---|---|---|---|---|---|---|
| B-RPM | 38 | 0.282 | 0.231 | 0.008 | 0.265 | 0.167 | 0.304 | 0.274 |
| B-RPM-LOFO | 38 | 0.292 | 0.240 | 0.000806 | 0.273 | 0.173 | 0.310 | 0.280 |
| B-RPM-r | 38 | 0.344 | 0.328 | -0.106 | 0.291 | 0.248 | 0.378 | 0.309 |
| B-RPM-0 | 38 | 0.398 | 0.262 | 0.084 | 0.408 | 0.213 | 0.402 | 0.459 |
| B-RPM-m10 | 38 | 0.295 | 0.281 | -0.039 | 0.256 | 0.188 | 0.330 | 0.270 |
| RPM | 38 | 0.284 | 0.229 | 0.143 | 0.355 | 0.270 | 0.326 | 0.371 |
| RPM-w | 38 | 0.286 | 0.234 | 0.134 | 0.354 | 0.254 | 0.334 | 0.376 |
| RPM-T | 38 | 0.505 | 0.276 | -0.301 | 0.453 | 0.340 | 0.555 | 0.491 |
| RPM-TD | 38 | 0.888 | 0.403 | 0.461 | 0.977 | 0.520 | 1.036 | 1.125 |
| RPM-TP | 38 | 0.506 | 0.273 | 0.095 | 0.490 | 0.297 | 0.580 | 0.558 |
| IPL3 | 38 | 0.425 | 0.398 | -0.253 | 0.309 | 0.272 | 0.440 | 0.326 |
| IPL2 | 38 | 0.535 | 0.477 | -0.437 | 0.371 | 0.335 | 0.587 | 0.428 |
| FLAT | 38 | 0.262 | 0.227 | 0.139 | 0.344 | 0.274 | 0.277 | 0.336 |
| DFOLS | 38 | 1.198 | 1.059 | -1.089 | 1.077 | 0.881 | 1.152 | 1.008 |
| WEI | 38 | 0.399 | 0.333 | -0.340 | 0.240 | 0.201 | 0.446 | 0.270 |
| SLOPE-T | 38 | 0.286 | 0.284 | -0.125 | 0.188 | 0.116 | 0.279 | 0.195 |
| SLOPE-T-LOFO | 38 | 0.392 | 0.398 | -0.248 | 0.278 | 0.255 | 0.341 | 0.246 |

**Table S7.** Paired comparisons of B-RPM (pre-specified hypotheses HB1–HB2 and secondary comparisons): mean improvement over the reference (positive favours B-RPM), bootstrap 95% CI, Wilcoxon p (task level, Holm-adjusted) and source-level results.

| endpoint | method | reference | task mean improvement | task ci lo | task ci hi | task p | task wins | n tasks | source mean improvement | source p | source wins | n sources | task p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gain | B-RPM-LOFO | SLOPE-T-LOFO | 0.006 | -0.036 | 0.048 | 0.720 | 19 | 38 | -0.034 | 0.547 | 3 | 8 | 1.000 |
| gain | B-RPM | SLOPE-T | -0.077 | -0.104 | -0.053 | 5.52e-08 | 3 | 38 | -0.079 | 0.008 | 0 | 8 | 7.72e-07 |
| level | B-RPM | FLAT | -0.020 | -0.038 | -0.003 | 0.037 | 16 | 38 | -0.027 | 0.109 | 2 | 8 | 0.222 |
| level | B-RPM | SLOPE-T | 0.004 | -0.027 | 0.033 | 0.482 | 21 | 38 | -0.025 | 0.641 | 3 | 8 | 1.000 |
| level | B-RPM | RPM | 0.002 | -0.021 | 0.026 | 0.688 | 17 | 38 | 0.022 | 0.383 | 5 | 8 | 1.000 |
| gain | B-RPM | RPM | 0.090 | 0.066 | 0.114 | 9.17e-09 | 33 | 38 | 0.097 | 0.008 | 8 | 8 | 1.38e-07 |
| level | B-RPM | IPL3 | 0.143 | 0.088 | 0.196 | 0.000114 | 33 | 38 | 0.136 | 0.109 | 7 | 8 | 0.001 |
| gain | B-RPM | IPL3 | 0.044 | -0.026 | 0.109 | 0.043 | 29 | 38 | 0.052 | 0.383 | 5 | 8 | 0.222 |
| gain | B-RPM | FLAT | 0.079 | 0.044 | 0.114 | 9.84e-05 | 30 | 38 | 0.062 | 0.109 | 6 | 8 | 0.001 |
| gain | B-RPM | B-RPM-0 | 0.143 | 0.065 | 0.229 | 0.001 | 27 | 38 | 0.186 | 0.016 | 7 | 8 | 0.011 |
| level | B-RPM | RPM-T | 0.223 | 0.087 | 0.393 | 0.012 | 25 | 38 | 0.251 | 0.039 | 7 | 8 | 0.084 |
| level | B-RPM | WEI | 0.117 | 0.056 | 0.186 | 1.9e-05 | 33 | 38 | 0.143 | 0.023 | 7 | 8 | 0.000246 |
| gain | B-RPM | WEI | -0.025 | -0.105 | 0.055 | 0.977 | 20 | 38 | -0.003 | 0.641 | 6 | 8 | 1.000 |
| level | B-RPM-LOFO | SLOPE-T-LOFO | 0.101 | 0.048 | 0.158 | 0.001 | 27 | 38 | 0.031 | 0.641 | 4 | 8 | 0.011 |
| level | B-RPM-LOFO | FLAT | -0.030 | -0.046 | -0.014 | 0.000819 | 10 | 38 | -0.033 | 0.023 | 1 | 8 | 0.008 |

**Table S8.** Level and gain error by application family for all forecasters.

| level 0 | level 1 | B-RPM | B-RPM-0 | B-RPM-LOFO | B-RPM-m10 | B-RPM-r | DFOLS | FLAT | IPL2 | IPL3 | RPM | RPM-T | RPM-TD | RPM-TP | RPM-w | SLOPE-T | SLOPE-T-LOFO | WEI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| level | fruit | 0.219 | 0.140 | 0.219 | 0.399 | 0.422 | 0.372 | 0.168 | 1.038 | 0.679 | 0.350 | 0.264 | 0.392 | 0.264 | 0.400 | 0.209 | 0.209 | 0.365 |
| level | fuel | 0.350 | 0.465 | 0.350 | 0.354 | 0.374 | 1.986 | 0.361 | 0.512 | 0.459 | 0.405 | 0.684 | 0.752 | 0.457 | 0.414 | 0.330 | 0.330 | 0.433 |
| level | meat | 0.270 | 0.225 | 0.270 | 0.295 | 0.323 | 0.963 | 0.261 | 0.557 | 0.390 | 0.275 | 0.288 | 0.922 | 0.288 | 0.281 | 0.304 | 0.304 | 0.681 |
| level | mixture | 0.569 | 1.338 | 0.569 | 0.447 | 0.443 | 1.891 | 0.474 | 0.383 | 0.360 | 0.603 | 0.489 | 3.403 | 1.960 | 0.570 | 0.375 | 0.375 | 0.491 |
| level | pharma | 0.387 | 0.295 | 0.387 | 0.433 | 0.507 | 1.268 | 0.356 | 0.715 | 0.445 | 0.430 | 1.312 | 1.383 | 0.769 | 0.459 | 0.313 | 0.313 | 0.661 |
| level | soil | 0.214 | 0.255 | 0.230 | 0.243 | 0.311 | 0.935 | 0.199 | 0.535 | 0.420 | 0.189 | 0.464 | 0.482 | 0.293 | 0.192 | 0.258 | 0.435 | 0.327 |
| gain | fruit | 0.231 | 0.276 | 0.231 | 0.321 | 0.357 | 0.295 | 0.269 | 0.954 | 0.611 | 0.491 | 0.405 | 0.533 | 0.405 | 0.541 | 0.161 | 0.161 | 0.275 |
| gain | fuel | 0.360 | 0.578 | 0.360 | 0.284 | 0.277 | 1.779 | 0.404 | 0.325 | 0.307 | 0.505 | 0.572 | 0.842 | 0.347 | 0.500 | 0.285 | 0.285 | 0.215 |
| gain | meat | 0.268 | 0.436 | 0.268 | 0.218 | 0.196 | 0.687 | 0.247 | 0.311 | 0.231 | 0.332 | 0.268 | 1.179 | 0.268 | 0.336 | 0.164 | 0.164 | 0.345 |
| gain | mixture | 0.777 | 1.551 | 0.777 | 0.653 | 0.650 | 1.817 | 0.659 | 0.333 | 0.372 | 0.805 | 0.368 | 3.609 | 2.173 | 0.766 | 0.540 | 0.540 | 0.268 |
| gain | pharma | 0.122 | 0.332 | 0.122 | 0.162 | 0.263 | 0.996 | 0.273 | 0.468 | 0.254 | 0.172 | 1.040 | 1.289 | 0.498 | 0.200 | 0.101 | 0.101 | 0.440 |
| gain | soil | 0.158 | 0.171 | 0.171 | 0.186 | 0.244 | 0.853 | 0.292 | 0.369 | 0.299 | 0.243 | 0.438 | 0.533 | 0.267 | 0.245 | 0.109 | 0.259 | 0.217 |

**Table S9.** Coverage and median width factor of 80% and 95% bands by family and pilot size, including the post-hoc leave-one-source-out recalibration of B-RPM.

| method | stratum | value | cov80 | cov95 | median width factor80 | n tasks |
|---|---|---|---|---|---|---|
| B-RPM | fam | fruit | 0.775 | 0.933 | 1.915 | 1 |
| B-RPM | fam | fuel | 0.533 | 0.731 | 1.791 | 6 |
| B-RPM | fam | meat | 0.577 | 0.739 | 1.654 | 3 |
| B-RPM | fam | mixture | 0.107 | 0.243 | 1.706 | 4 |
| B-RPM | fam | pharma | 0.539 | 0.733 | 2.108 | 1 |
| B-RPM | fam | soil | 0.620 | 0.808 | 1.524 | 23 |
| B-RPM | n0 | 25 | 0.578 | 0.753 | 1.958 | 38 |
| B-RPM | n0 | 50 | 0.567 | 0.744 | 1.671 | 38 |
| B-RPM | n0 | 100 | 0.585 | 0.790 | 1.406 | 31 |
| B-RPM | n0 | 200 | 0.530 | 0.718 | 1.235 | 25 |
| B-RPM | all | all | 0.551 | 0.732 | 1.673 | 38 |
| B-RPM-LOFO | fam | fruit | 0.775 | 0.933 | 1.915 | 1 |
| B-RPM-LOFO | fam | fuel | 0.533 | 0.731 | 1.791 | 6 |
| B-RPM-LOFO | fam | meat | 0.577 | 0.739 | 1.654 | 3 |
| B-RPM-LOFO | fam | mixture | 0.107 | 0.243 | 1.706 | 4 |
| B-RPM-LOFO | fam | pharma | 0.539 | 0.733 | 2.108 | 1 |
| B-RPM-LOFO | fam | soil | 0.588 | 0.785 | 1.457 | 23 |
| B-RPM-LOFO | n0 | 25 | 0.546 | 0.731 | 1.933 | 38 |
| B-RPM-LOFO | n0 | 50 | 0.547 | 0.730 | 1.601 | 38 |
| B-RPM-LOFO | n0 | 100 | 0.569 | 0.777 | 1.369 | 31 |
| B-RPM-LOFO | n0 | 200 | 0.524 | 0.714 | 1.231 | 25 |
| B-RPM-LOFO | all | all | 0.532 | 0.718 | 1.629 | 38 |
| RPM | fam | fruit | 0.019 | 0.050 | 1.257 | 1 |
| RPM | fam | fuel | 0.312 | 0.438 | 1.519 | 6 |
| RPM | fam | meat | 0.509 | 0.700 | 1.599 | 3 |
| RPM | fam | mixture | 0.101 | 0.182 | 1.629 | 4 |
| RPM | fam | pharma | 0.457 | 0.615 | 1.794 | 1 |
| RPM | fam | soil | 0.571 | 0.755 | 1.421 | 23 |
| RPM | n0 | 25 | 0.501 | 0.663 | 1.652 | 38 |
| RPM | n0 | 50 | 0.465 | 0.616 | 1.442 | 38 |
| RPM | n0 | 100 | 0.460 | 0.634 | 1.334 | 31 |
| RPM | n0 | 200 | 0.443 | 0.613 | 1.262 | 25 |
| RPM | all | all | 0.458 | 0.618 | 1.481 | 38 |
| IPL3 | fam | fruit | 0.753 | 0.858 | 4.461 | 1 |
| IPL3 | fam | fuel | 0.859 | 0.909 | 18.865 | 6 |
| IPL3 | fam | meat | 0.854 | 0.920 | 7.729 | 3 |
| IPL3 | fam | mixture | 0.873 | 0.914 | 36.499 | 4 |
| IPL3 | fam | pharma | 0.599 | 0.718 | 1.966 | 1 |
| IPL3 | fam | soil | 0.875 | 0.918 | 17.137 | 23 |
| IPL3 | n0 | 25 | 0.910 | 0.942 | 552.443 | 38 |
| IPL3 | n0 | 50 | 0.854 | 0.905 | 8.706 | 38 |
| IPL3 | n0 | 100 | 0.799 | 0.867 | 3.187 | 31 |
| IPL3 | n0 | 200 | 0.774 | 0.858 | 2.014 | 25 |
| IPL3 | all | all | 0.860 | 0.909 | 13.772 | 38 |
| B-RPM-cal (post hoc) | fam | fruit | 0.958 | 1.000 | 3.106 | 1 |
| B-RPM-cal (post hoc) | fam | fuel | 0.764 | 0.913 | 2.687 | 6 |
| B-RPM-cal (post hoc) | fam | meat | 0.788 | 0.930 | 2.387 | 3 |
| B-RPM-cal (post hoc) | fam | mixture | 0.258 | 0.838 | 2.296 | 4 |
| B-RPM-cal (post hoc) | fam | pharma | 0.769 | 0.971 | 3.606 | 1 |
| B-RPM-cal (post hoc) | fam | soil | 0.889 | 0.973 | 2.156 | 23 |
| B-RPM-cal (post hoc) | n0 | 25 | 0.813 | 0.953 | 3.151 | 38 |
| B-RPM-cal (post hoc) | n0 | 50 | 0.810 | 0.959 | 2.440 | 38 |
| B-RPM-cal (post hoc) | n0 | 100 | 0.852 | 0.947 | 1.845 | 31 |
| B-RPM-cal (post hoc) | n0 | 200 | 0.800 | 0.946 | 1.469 | 25 |
| B-RPM-cal (post hoc) | all | all | 0.794 | 0.947 | 2.434 | 38 |
| B-RPM-LOFO-cal (post hoc) | fam | fruit | 0.961 | 1.000 | 3.198 | 1 |
| B-RPM-LOFO-cal (post hoc) | fam | fuel | 0.774 | 0.915 | 2.760 | 6 |
| B-RPM-LOFO-cal (post hoc) | fam | meat | 0.798 | 0.932 | 2.437 | 3 |
| B-RPM-LOFO-cal (post hoc) | fam | mixture | 0.279 | 0.849 | 2.356 | 4 |
| B-RPM-LOFO-cal (post hoc) | fam | pharma | 0.779 | 0.973 | 3.726 | 1 |

**Table S10.** Prior-free compatible set: coverage of the true learning curve, median width factor and median information fraction, by extrapolation ratio and pilot size (HB4).

| ratio | coverage | median width factor | info fraction median | n | by | n0 |
|---|---|---|---|---|---|---|
| 2 | 0.876 | 3.435 | 0.517 | 5520 | ratio | – |
| 4 | 0.886 | 6.708 | 0.407 | 4120 | ratio | – |
| 8 | 0.946 | 15.019 | 0.369 | 2580 | ratio | – |
| 16 | 0.962 | 47.048 | 0.456 | 1560 | ratio | – |
| >=32 | 0.980 | 57.507 | 0.356 | 2280 | ratio | – |
| – | 0.912 | 8.981 | 0.167 | 6660 | n0 | 25.000 |
| – | 0.905 | 8.037 | 0.365 | 4780 | n0 | 50.000 |
| – | 0.929 | 5.377 | 0.826 | 2900 | n0 | 100.000 |
| – | 0.911 | 1.727 | 0.953 | 1720 | n0 | 200.000 |

**Table S11.** Brier score of the probabilistic decision 'an eightfold larger calibration set reduces RMSEP by at least 15%'.

| method | brier task mean | prevalence | mean prob | brier climatology |
|---|---|---|---|---|
| B-RPM | 0.290 | 0.448 | 0.497 | 0.247 |
| B-RPM-LOFO | 0.291 | 0.448 | 0.478 | 0.247 |
| SLOPE-T | 0.294 | 0.448 | 0.661 | 0.247 |
| SLOPE-T-LOFO | 0.358 | 0.448 | 0.758 | 0.247 |
| FLAT | 0.274 | 0.448 | 0.319 | 0.247 |
| RPM | 0.306 | 0.448 | 0.240 | 0.247 |
| IPL3 | 0.277 | 0.448 | 0.487 | 0.247 |

**Table S12.** Forecast error of B-RPM by tertile of the information fraction.

| info tertile | level mae | gain mae | info median | n |
|---|---|---|---|---|
| low | 0.373 | 0.338 | -0.052 | 5354 |
| mid | 0.297 | 0.222 | 0.438 | 5353 |
| high | 0.188 | 0.221 | 0.923 | 5353 |

**Table S13.** Mean signed log error by extrapolation ratio for all forecasters (pooled over tasks).

| rb | B-RPM | B-RPM-0 | B-RPM-LOFO | B-RPM-m10 | B-RPM-r | DFOLS | FLAT | IPL2 | IPL3 | RPM | RPM-T | RPM-TD | RPM-TP | RPM-w | SLOPE-T | SLOPE-T-LOFO | WEI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | -0.006 | 0.070 | -0.018 | -0.038 | -0.055 | -0.982 | 0.001 | -0.193 | -0.108 | 0.049 | -0.111 | 0.570 | 0.130 | 0.044 | -0.101 | -0.141 | -0.235 |
| 4 | 0.040 | 0.111 | 0.031 | -0.012 | -0.063 | -1.068 | 0.141 | -0.332 | -0.180 | 0.149 | -0.198 | 0.529 | 0.123 | 0.143 | -0.063 | -0.143 | -0.337 |
| 8 | -0.031 | -0.066 | -0.036 | -0.077 | -0.175 | -1.081 | 0.184 | -0.462 | -0.274 | 0.145 | -0.357 | -0.039 | -0.164 | 0.138 | -0.130 | -0.279 | -0.308 |
| 16 | -0.114 | -0.194 | -0.111 | -0.138 | -0.259 | -0.856 | 0.192 | -0.675 | -0.381 | 0.103 | -0.581 | -0.194 | -0.177 | 0.093 | -0.244 | -0.489 | -0.360 |
| >=32 | -0.134 | -0.217 | -0.146 | -0.172 | -0.326 | -1.177 | 0.271 | -0.998 | -0.665 | 0.169 | -0.637 | -0.218 | -0.185 | 0.156 | -0.326 | -0.673 | -0.414 |

**Table S14.** Mean absolute per-task bias by extrapolation ratio (does not allow opposite task biases to cancel).

| rb | B-RPM | B-RPM-0 | B-RPM-LOFO | B-RPM-m10 | B-RPM-r | DFOLS | FLAT | IPL2 | IPL3 | RPM | RPM-T | RPM-TD | RPM-TP | RPM-w | SLOPE-T | SLOPE-T-LOFO | WEI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 0.139 | 0.327 | 0.151 | 0.124 | 0.143 | 0.982 | 0.107 | 0.193 | 0.124 | 0.147 | 0.135 | 0.585 | 0.293 | 0.150 | 0.156 | 0.196 | 0.235 |
| 4 | 0.193 | 0.382 | 0.203 | 0.174 | 0.219 | 1.068 | 0.179 | 0.337 | 0.205 | 0.197 | 0.237 | 0.561 | 0.354 | 0.194 | 0.221 | 0.300 | 0.337 |
| 8 | 0.147 | 0.283 | 0.157 | 0.141 | 0.224 | 1.081 | 0.187 | 0.462 | 0.278 | 0.162 | 0.420 | 0.241 | 0.227 | 0.162 | 0.228 | 0.372 | 0.308 |
| 16 | 0.143 | 0.255 | 0.149 | 0.163 | 0.292 | 0.856 | 0.192 | 0.675 | 0.381 | 0.131 | 0.683 | 0.486 | 0.278 | 0.140 | 0.251 | 0.489 | 0.361 |
| >=32 | 0.171 | 0.269 | 0.191 | 0.202 | 0.364 | 1.181 | 0.271 | 0.998 | 0.665 | 0.182 | 0.782 | 0.651 | 0.330 | 0.190 | 0.337 | 0.673 | 0.418 |

**Table S15.** B-RPM level error by tertile of the information fraction within each pilot size.

| n0 | level mae low | level mae mid | level mae high |
|---|---|---|---|
| 25 | 0.420 | 0.379 | 0.313 |
| 50 | 0.327 | 0.282 | 0.224 |
| 100 | 0.233 | 0.163 | 0.185 |
| 200 | 0.136 | 0.141 | 0.129 |

**Table S16.** Forecast error for a fixed target calibration size (400, 800, 1600) by pilot size: value of a larger pilot or second batch.

| n target | n0 | n tasks | B-RPM | FLAT | IPL3 | RPM | SLOPE-T |
|---|---|---|---|---|---|---|---|
| 400 | 25 | 25 | 0.323 | 0.272 | 0.677 | 0.273 | 0.313 |
| 400 | 50 | 25 | 0.244 | 0.181 | 0.412 | 0.179 | 0.247 |
| 400 | 100 | 25 | 0.155 | 0.140 | 0.223 | 0.149 | 0.178 |
| 400 | 200 | 25 | 0.117 | 0.100 | 0.137 | 0.120 | 0.137 |
| 800 | 25 | 24 | 0.314 | 0.304 | 0.829 | 0.277 | 0.342 |
| 800 | 50 | 24 | 0.244 | 0.211 | 0.509 | 0.190 | 0.282 |
| 800 | 100 | 24 | 0.158 | 0.161 | 0.277 | 0.161 | 0.211 |
| 800 | 200 | 24 | 0.121 | 0.106 | 0.166 | 0.131 | 0.168 |
| 1600 | 25 | 17 | 0.320 | 0.328 | 1.074 | 0.305 | 0.407 |
| 1600 | 50 | 17 | 0.248 | 0.249 | 0.658 | 0.209 | 0.342 |
| 1600 | 100 | 17 | 0.170 | 0.192 | 0.350 | 0.184 | 0.275 |
| 1600 | 200 | 17 | 0.117 | 0.128 | 0.218 | 0.142 | 0.230 |

**Table S17.** Reachability decisions for an absolute RMSEP target at budget N: one-shot (pilot N/8), staged (second batch, N/4) and compatible-set-gated policies.

| Unnamed: 0 | 400 | 800 |
|---|---|---|
| one-shot:B-RPM | 0.683 | 0.761 |
| staged:B-RPM | 0.781 | 0.836 |
| one-shot:FLAT | 0.740 | 0.759 |
| staged:FLAT | 0.798 | 0.861 |
| one-shot:SLOPE-T | 0.637 | 0.652 |
| staged:SLOPE-T | 0.725 | 0.707 |
| one-shot:RPM | 0.742 | 0.759 |
| staged:RPM | 0.786 | 0.808 |
| one-shot:IPL3 | 0.631 | 0.674 |
| staged:IPL3 | 0.699 | 0.764 |
| gated | 0.789 | 0.839 |
| gated_second_batch_share | 0.937 | 0.917 |

**Table S18.** Reachability decisions split into reachable and unreachable targets.

| N | 400 | 400.1 | 800 | 800.1 |
|---|---|---|---|---|
| target | reachable | unreachable | reachable | unreachable |
| one-shot:B-RPM | 0.8464 | 0.5188 | 0.7583333333333333 | 0.7645833333333334 |
| staged:B-RPM | 0.8195999999999999 | 0.7428 | 0.7520833333333333 | 0.9208333333333334 |
| one-shot:FLAT | 0.5632 | 0.9176000000000001 | 0.5395833333333333 | 0.9791666666666666 |
| staged:FLAT | 0.6731999999999999 | 0.9236 | 0.7541666666666668 | 0.96875 |
| one-shot:SLOPE-T | 0.9412 | 0.33240000000000003 | 0.975 | 0.32916666666666666 |
| staged:SLOPE-T | 0.9528 | 0.4976 | 0.975 | 0.43958333333333327 |
| one-shot:RPM | 0.6548 | 0.8284 | 0.5833333333333334 | 0.9354166666666667 |
| staged:RPM | 0.6931999999999999 | 0.8784000000000001 | 0.65625 | 0.9604166666666667 |
| one-shot:IPL3 | 0.8508 | 0.41200000000000003 | 0.8854166666666666 | 0.46249999999999997 |
| staged:IPL3 | 0.8787999999999999 | 0.5192 | 0.9270833333333334 | 0.6 |
| gated | 0.83788 | 0.740228 | 0.7571875 | 0.9210416666666666 |
| gated_second_batch_share | 0.88 | 0.9944 | 0.8895833333333334 | 0.94375 |

**Table S19.** Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%).

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 38 | 0.284 | 0.235 | 0.341 | 0.229 | 0.210 | 0.143 | 25.031 | 44.676 |
| RPM-w | RPM-w (weighted path fit) | 38 | 0.286 | 0.236 | 0.342 | 0.234 | 0.206 | 0.134 | 25.143 | 45.131 |
| RPM-T | RPM-T (transferred alignment) | 38 | 0.505 | 0.357 | 0.686 | 0.276 | 0.218 | -0.301 | 24.639 | 43.817 |
| RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.504 | 0.356 | 0.684 | 0.305 | 0.217 | -0.323 | 25.081 | 44.072 |
| IPL3 | Inverse power law (IPL3) | 38 | 0.425 | 0.384 | 0.471 | 0.398 | 0.298 | -0.253 | 18.512 | 33.126 |
| IPL2 | Power law (IPL2) | 38 | 0.535 | 0.477 | 0.601 | 0.477 | 0.397 | -0.437 | 13.232 | 24.695 |
| EXP3 | Exponential (EXP3) | 38 | 2.032 | 1.718 | 2.374 | 1.837 | 0.449 | -1.817 | 14.533 | 26.594 |
| LOG2 | Logarithmic (LOG2) | 38 | 10.081 | 9.429 | 10.734 | 10.204 | 12.952 | -10.055 | 3.362 | 6.613 |
| FLAT | No improvement (FLAT) | 38 | 0.262 | 0.226 | 0.301 | 0.227 | 0.198 | 0.139 | 26.164 | 46.644 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 1.198 | 0.929 | 1.491 | 1.059 | 0.246 | -1.089 | 23.007 | 40.318 |
| SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.286 | 0.260 | 0.314 | 0.284 | 0.245 | -0.125 | 19.558 | 37.453 |

**Table S20.** Forecast accuracy by pilot size n0.

| n0 | method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | RPM | RPM (pre-registered, r = 1) | 38 | 0.341 | 0.284 | 0.407 | 0.270 | 0.284 | 0.130 | 18.979 | 34.144 |
| 25 | RPM-w | RPM-w (weighted path fit) | 38 | 0.351 | 0.286 | 0.430 | 0.284 | 0.280 | 0.108 | 19.054 | 34.685 |
| 25 | RPM-T | RPM-T (transferred alignment) | 38 | 0.807 | 0.507 | 1.180 | 0.363 | 0.303 | -0.584 | 18.333 | 32.477 |
| 25 | RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.808 | 0.508 | 1.181 | 0.376 | 0.306 | -0.601 | 18.063 | 32.297 |
| 25 | IPL3 | Inverse power law (IPL3) | 38 | 0.589 | 0.519 | 0.667 | 0.509 | 0.418 | -0.386 | 12.177 | 23.018 |
| 25 | IPL2 | Power law (IPL2) | 38 | 0.699 | 0.620 | 0.787 | 0.640 | 0.522 | -0.577 | 9.700 | 18.333 |
| 25 | EXP3 | Exponential (EXP3) | 38 | 3.428 | 2.798 | 4.081 | 2.993 | 0.800 | -3.199 | 8.168 | 15.856 |
| 25 | LOG2 | Logarithmic (LOG2) | 38 | 12.225 | 11.679 | 12.733 | 12.434 | 13.450 | -12.201 | 1.096 | 2.012 |
| 25 | FLAT | No improvement (FLAT) | 38 | 0.326 | 0.286 | 0.371 | 0.289 | 0.280 | 0.177 | 18.514 | 34.009 |
| 25 | DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 2.177 | 1.596 | 2.856 | 1.689 | 0.365 | -2.027 | 14.805 | 27.973 |
| 25 | SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.342 | 0.312 | 0.373 | 0.350 | 0.302 | -0.138 | 16.547 | 30.916 |
| 50 | RPM | RPM (pre-registered, r = 1) | 38 | 0.259 | 0.216 | 0.307 | 0.197 | 0.213 | 0.130 | 24.310 | 44.038 |
| 50 | RPM-w | RPM-w (weighted path fit) | 38 | 0.255 | 0.213 | 0.303 | 0.198 | 0.207 | 0.127 | 24.812 | 44.749 |
| 50 | RPM-T | RPM-T (transferred alignment) | 38 | 0.466 | 0.298 | 0.709 | 0.236 | 0.228 | -0.296 | 23.033 | 42.092 |
| 50 | RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.461 | 0.298 | 0.685 | 0.228 | 0.234 | -0.309 | 22.908 | 41.527 |
| 50 | IPL3 | Inverse power law (IPL3) | 38 | 0.418 | 0.360 | 0.484 | 0.363 | 0.309 | -0.270 | 17.762 | 31.820 |
| 50 | IPL2 | Power law (IPL2) | 38 | 0.560 | 0.469 | 0.669 | 0.473 | 0.431 | -0.491 | 12.155 | 22.448 |
| 50 | EXP3 | Exponential (EXP3) | 38 | 1.763 | 1.339 | 2.239 | 1.305 | 0.425 | -1.542 | 13.096 | 24.937 |
| 50 | LOG2 | Logarithmic (LOG2) | 38 | 10.517 | 9.702 | 11.320 | 11.106 | 13.021 | -10.495 | 2.301 | 4.498 |
| 50 | FLAT | No improvement (FLAT) | 38 | 0.232 | 0.203 | 0.265 | 0.194 | 0.198 | 0.109 | 25.481 | 46.548 |
| 50 | DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 0.784 | 0.590 | 1.007 | 0.677 | 0.256 | -0.701 | 21.736 | 38.598 |
| 50 | SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.269 | 0.243 | 0.299 | 0.255 | 0.247 | -0.155 | 19.854 | 36.883 |
| 100 | RPM | RPM (pre-registered, r = 1) | 31 | 0.198 | 0.162 | 0.239 | 0.152 | 0.156 | 0.114 | 31.310 | 56.759 |
| 100 | RPM-w | RPM-w (weighted path fit) | 31 | 0.203 | 0.162 | 0.250 | 0.148 | 0.156 | 0.120 | 30.724 | 56.310 |
| 100 | RPM-T | RPM-T (transferred alignment) | 31 | 0.254 | 0.166 | 0.388 | 0.160 | 0.158 | -0.040 | 30.724 | 56.241 |
| 100 | RPM-wT | RPM-wT (weighted + transferred) | 31 | 0.265 | 0.160 | 0.428 | 0.142 | 0.153 | -0.090 | 32.552 | 57.276 |
| 100 | IPL3 | Inverse power law (IPL3) | 31 | 0.283 | 0.240 | 0.332 | 0.254 | 0.214 | -0.151 | 25.345 | 43.621 |
| 100 | IPL2 | Power law (IPL2) | 31 | 0.386 | 0.321 | 0.461 | 0.307 | 0.298 | -0.308 | 17.759 | 32.069 |
| 100 | EXP3 | Exponential (EXP3) | 31 | 1.115 | 0.809 | 1.477 | 0.839 | 0.257 | -0.960 | 20.483 | 37.828 |
| 100 | LOG2 | Logarithmic (LOG2) | 31 | 7.640 | 6.545 | 8.721 | 7.281 | 11.835 | -7.599 | 6.310 | 12.345 |
| 100 | FLAT | No improvement (FLAT) | 31 | 0.182 | 0.154 | 0.217 | 0.147 | 0.147 | 0.096 | 33.103 | 59.517 |
| 100 | DFOLS | Fixed-complexity formula (DF-OLS) | 31 | 0.249 | 0.185 | 0.324 | 0.184 | 0.161 | -0.170 | 32.517 | 54.483 |
| 100 | SLOPE-T | Transferred slope (SLOPE-T) | 31 | 0.218 | 0.189 | 0.254 | 0.203 | 0.198 | -0.155 | 24.345 | 46.759 |
| 200 | RPM | RPM (pre-registered, r = 1) | 25 | 0.146 | 0.124 | 0.169 | 0.136 | 0.121 | 0.098 | 39.884 | 66.860 |
| 200 | RPM-w | RPM-w (weighted path fit) | 25 | 0.145 | 0.120 | 0.173 | 0.138 | 0.125 | 0.099 | 40.233 | 67.791 |
| 200 | RPM-T | RPM-T (transferred alignment) | 25 | 0.138 | 0.120 | 0.159 | 0.127 | 0.111 | 0.072 | 43.256 | 71.570 |
| 200 | RPM-wT | RPM-wT (weighted + transferred) | 25 | 0.129 | 0.109 | 0.153 | 0.112 | 0.106 | 0.047 | 45.698 | 74.477 |
| 200 | IPL3 | Inverse power law (IPL3) | 25 | 0.187 | 0.160 | 0.215 | 0.167 | 0.147 | -0.102 | 33.605 | 58.198 |
| 200 | IPL2 | Power law (IPL2) | 25 | 0.247 | 0.208 | 0.287 | 0.239 | 0.215 | -0.200 | 22.267 | 43.140 |
| 200 | EXP3 | Exponential (EXP3) | 25 | 0.640 | 0.420 | 0.887 | 0.354 | 0.165 | -0.536 | 33.140 | 53.837 |
| 200 | LOG2 | Logarithmic (LOG2) | 25 | 3.901 | 2.743 | 5.110 | 3.212 | 0.510 | -3.872 | 10.116 | 20.640 |
| 200 | FLAT | No improvement (FLAT) | 25 | 0.127 | 0.104 | 0.152 | 0.106 | 0.106 | 0.080 | 45.988 | 74.128 |
| 200 | DFOLS | Fixed-complexity formula (DF-OLS) | 25 | 0.142 | 0.119 | 0.165 | 0.134 | 0.118 | -0.079 | 42.267 | 69.012 |
| 200 | SLOPE-T | Transferred slope (SLOPE-T) | 25 | 0.189 | 0.165 | 0.212 | 0.191 | 0.186 | -0.156 | 22.326 | 48.663 |

**Table S21.** Paired two-sided Wilcoxon signed-rank tests (task level) of the pre-registered RPM against every other method; Holm-adjusted p-values; median paired difference (other − RPM; positive favours RPM) with bootstrap 95% CI; matched-pairs rank-biserial correlation.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 38 | 300.000 | 0.314 | -0.003 | -0.005 | 0.000253 | -0.190 | 14 | 24 | 0.942 |
| RPM-T | 38 | 117.000 | 0.000114 | 0.034 | 0.009 | 0.095 | 0.684 | 29 | 9 | 0.000682 |
| RPM-wT | 38 | 170.000 | 0.003 | 0.025 | 0.001 | 0.094 | 0.541 | 25 | 13 | 0.012 |
| IPL3 | 38 | 122.000 | 0.000162 | 0.177 | 0.124 | 0.218 | 0.671 | 33 | 5 | 0.000811 |
| IPL2 | 38 | 72.000 | 2.54e-06 | 0.284 | 0.201 | 0.344 | 0.806 | 33 | 5 | 1.78e-05 |
| EXP3 | 38 | 0.000 | 7.28e-12 | 1.600 | 1.094 | 2.016 | 1.000 | 38 | 0 | 7.28e-11 |
| LOG2 | 38 | 0.000 | 7.28e-12 | 9.942 | 9.269 | 10.650 | 1.000 | 38 | 0 | 7.28e-11 |
| FLAT | 38 | 322.000 | 0.491 | 1.55e-05 | -0.009 | 0.010 | -0.131 | 19 | 19 | 0.981 |
| DFOLS | 38 | 4.000 | 5.09e-11 | 0.827 | 0.358 | 1.168 | 0.989 | 37 | 1 | 4.07e-10 |
| SLOPE-T | 38 | 322.000 | 0.491 | 0.033 | -0.040 | 0.068 | 0.131 | 23 | 15 | 0.981 |

**Table S22.** POST HOC: paired tests with SLOPE-T as the reference method.

| reference | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SLOPE-T | RPM | 38 | 322.000 | 0.491 | -0.033 | -0.069 | 0.039 | -0.131 | 15 | 23 | 0.981 |
| SLOPE-T | RPM-w | 38 | 346.000 | 0.731 | -0.033 | -0.072 | 0.042 | -0.066 | 15 | 23 | 0.981 |
| SLOPE-T | RPM-T | 38 | 214.000 | 0.022 | 0.058 | -0.012 | 0.134 | 0.422 | 24 | 14 | 0.112 |
| SLOPE-T | RPM-wT | 38 | 221.000 | 0.030 | 0.044 | -0.012 | 0.124 | 0.404 | 22 | 16 | 0.118 |
| SLOPE-T | IPL3 | 38 | 21.000 | 3.25e-09 | 0.130 | 0.082 | 0.155 | 0.943 | 34 | 4 | 2.28e-08 |
| SLOPE-T | IPL2 | 38 | 7.000 | 1.38e-10 | 0.231 | 0.200 | 0.255 | 0.981 | 36 | 2 | 1.11e-09 |
| SLOPE-T | EXP3 | 38 | 0.000 | 7.28e-12 | 1.575 | 1.132 | 2.005 | 1.000 | 38 | 0 | 7.28e-11 |
| SLOPE-T | LOG2 | 38 | 0.000 | 7.28e-12 | 9.899 | 9.183 | 10.688 | 1.000 | 38 | 0 | 7.28e-11 |
| SLOPE-T | FLAT | 38 | 267.000 | 0.136 | -0.027 | -0.054 | 0.002 | -0.279 | 14 | 24 | 0.409 |
| SLOPE-T | DFOLS | 38 | 23.000 | 4.66e-09 | 0.782 | 0.269 | 1.196 | 0.938 | 35 | 3 | 2.79e-08 |

**Table S23.** POST HOC: accuracy and paired tests stratified by extrapolation ratio n/n0 (short: < 16; long: ≥ 16).

| stratum | method | n tasks | mean task mean abs | mean task median abs | diff vs RPMw | p holm | RPMw wins | RPMw losses |
|---|---|---|---|---|---|---|---|---|
| ratio <= 8 | RPM-w | 38 | 0.266 | 0.232 | – | – | – | – |
| ratio <= 8 | RPM | 38 | 0.267 | 0.233 | 0.002 | 0.809 | 24.000 | 14.000 |
| ratio <= 8 | SLOPE-T | 38 | 0.256 | 0.220 | 0.022 | 0.841 | 23.000 | 15.000 |
| ratio <= 8 | FLAT | 38 | 0.235 | 0.194 | -0.003 | 0.159 | 16.000 | 22.000 |
| ratio <= 8 | IPL3 | 38 | 0.330 | 0.255 | 0.105 | 0.004 | 31.000 | 7.000 |
| ratio >= 16 | RPM-w | 25 | 0.266 | 0.217 | – | – | – | – |
| ratio >= 16 | RPM | 25 | 0.254 | 0.217 | 0.002 | 0.560 | 16.000 | 9.000 |
| ratio >= 16 | SLOPE-T | 25 | 0.333 | 0.306 | 0.103 | 0.125 | 18.000 | 7.000 |
| ratio >= 16 | FLAT | 25 | 0.276 | 0.255 | 0.032 | 0.041 | 22.000 | 3.000 |
| ratio >= 16 | IPL3 | 25 | 0.673 | 0.507 | 0.437 | 4.77e-07 | 24.000 | 1.000 |

**Table S24.** Absolute log error by extrapolation ratio n/n0.

| method | ratio bin | mean | median | count | ratio |
|---|---|---|---|---|---|
| DFOLS | 1 | 1.210 | 0.286 | 5520 | 2.000 |
| DFOLS | 2 | 1.361 | 0.269 | 4120 | 4.000 |
| DFOLS | 3 | 1.326 | 0.212 | 2580 | 8.000 |
| DFOLS | 4 | 1.032 | 0.173 | 1560 | 16.000 |
| DFOLS | 5 | 1.089 | 0.188 | 1140 | 32.000 |
| DFOLS | 6 | 1.440 | 0.224 | 660 | 64.000 |
| DFOLS | 7 | 1.776 | 0.256 | 320 | 128.000 |
| DFOLS | 8 | 3.125 | 0.331 | 160 | 256.000 |
| FLAT | 1 | 0.239 | 0.176 | 5520 | 2.000 |
| FLAT | 2 | 0.302 | 0.195 | 4120 | 4.000 |
| FLAT | 3 | 0.280 | 0.181 | 2580 | 8.000 |
| FLAT | 4 | 0.237 | 0.191 | 1560 | 16.000 |
| FLAT | 5 | 0.270 | 0.237 | 1140 | 32.000 |
| FLAT | 6 | 0.316 | 0.291 | 660 | 64.000 |
| FLAT | 7 | 0.362 | 0.337 | 320 | 128.000 |
| FLAT | 8 | 0.403 | 0.376 | 160 | 256.000 |
| IPL3 | 1 | 0.295 | 0.221 | 5520 | 2.000 |
| IPL3 | 2 | 0.390 | 0.281 | 4120 | 4.000 |
| IPL3 | 3 | 0.448 | 0.330 | 2580 | 8.000 |
| IPL3 | 4 | 0.518 | 0.396 | 1560 | 16.000 |
| IPL3 | 5 | 0.669 | 0.520 | 1140 | 32.000 |
| IPL3 | 6 | 0.885 | 0.731 | 660 | 64.000 |
| IPL3 | 7 | 1.110 | 0.926 | 320 | 128.000 |
| IPL3 | 8 | 1.534 | 1.342 | 160 | 256.000 |
| RPM | 1 | 0.286 | 0.219 | 5520 | 2.000 |
| RPM | 2 | 0.340 | 0.223 | 4120 | 4.000 |
| RPM | 3 | 0.298 | 0.189 | 2580 | 8.000 |
| RPM | 4 | 0.239 | 0.177 | 1560 | 16.000 |
| RPM | 5 | 0.241 | 0.200 | 1140 | 32.000 |
| RPM | 6 | 0.279 | 0.230 | 660 | 64.000 |
| RPM | 7 | 0.319 | 0.255 | 320 | 128.000 |
| RPM | 8 | 0.384 | 0.294 | 160 | 256.000 |

**Table S25.** Forecast accuracy against the PLS ground truth.

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 38 | 0.275 | 0.228 | 0.328 | 0.210 | 0.200 | 0.104 | 26.333 | 46.513 |
| RPM-w | RPM-w (weighted path fit) | 38 | 0.277 | 0.230 | 0.331 | 0.217 | 0.198 | 0.095 | 26.370 | 47.055 |
| RPM-T | RPM-T (transferred alignment) | 38 | 0.513 | 0.363 | 0.697 | 0.283 | 0.216 | -0.340 | 24.720 | 43.867 |
| RPM-wT | RPM-wT (weighted + transferred) | 38 | 0.514 | 0.363 | 0.697 | 0.307 | 0.217 | -0.362 | 25.224 | 44.234 |
| IPL3 | Inverse power law (IPL3) | 38 | 0.441 | 0.398 | 0.490 | 0.413 | 0.311 | -0.291 | 17.024 | 31.806 |
| IPL2 | Power law (IPL2) | 38 | 0.560 | 0.499 | 0.628 | 0.507 | 0.425 | -0.475 | 11.513 | 22.696 |
| EXP3 | Exponential (EXP3) | 38 | 2.046 | 1.732 | 2.390 | 1.858 | 0.455 | -1.855 | 15.044 | 26.675 |
| LOG2 | Logarithmic (LOG2) | 38 | 10.116 | 9.461 | 10.769 | 10.244 | 12.973 | -10.094 | 2.902 | 6.052 |
| FLAT | No improvement (FLAT) | 38 | 0.252 | 0.217 | 0.291 | 0.219 | 0.186 | 0.100 | 28.039 | 49.097 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 38 | 1.217 | 0.946 | 1.514 | 1.080 | 0.263 | -1.128 | 21.606 | 38.250 |
| SLOPE-T | Transferred slope (SLOPE-T) | 38 | 0.303 | 0.275 | 0.333 | 0.300 | 0.262 | -0.164 | 17.291 | 34.247 |

**Table S26.** Paired tests against the PLS ground truth.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 38 | 310.000 | 0.388 | -0.002 | -0.004 | 0.000802 | -0.163 | 15 | 23 | 0.463 |
| RPM-T | 38 | 94.000 | 1.9e-05 | 0.047 | 0.012 | 0.115 | 0.746 | 32 | 6 | 0.000114 |
| RPM-wT | 38 | 125.000 | 0.0002 | 0.055 | 0.009 | 0.117 | 0.663 | 29 | 9 | 0.000799 |
| IPL3 | 38 | 95.000 | 2.06e-05 | 0.181 | 0.139 | 0.237 | 0.744 | 33 | 5 | 0.000114 |
| IPL2 | 38 | 49.000 | 2.02e-07 | 0.297 | 0.220 | 0.373 | 0.868 | 33 | 5 | 1.41e-06 |
| EXP3 | 38 | 0.000 | 7.28e-12 | 1.615 | 1.139 | 2.032 | 1.000 | 38 | 0 | 7.28e-11 |
| LOG2 | 38 | 0.000 | 7.28e-12 | 9.996 | 9.290 | 10.694 | 1.000 | 38 | 0 | 7.28e-11 |
| FLAT | 38 | 287.000 | 0.232 | -0.002 | -0.012 | 0.002 | -0.225 | 16 | 22 | 0.463 |
| DFOLS | 38 | 1.000 | 1.46e-11 | 0.846 | 0.379 | 1.184 | 0.997 | 37 | 1 | 1.16e-10 |
| SLOPE-T | 38 | 249.000 | 0.079 | 0.056 | -0.027 | 0.105 | 0.328 | 23 | 15 | 0.238 |

**Table S27.** Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work.

| method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM (pre-registered, r = 1) | 34 | 0.302 | 0.249 | 0.364 | 0.243 | 0.226 | 0.158 | 23.023 | 41.737 |
| RPM-w | RPM-w (weighted path fit) | 34 | 0.304 | 0.250 | 0.365 | 0.244 | 0.223 | 0.149 | 23.057 | 42.086 |
| RPM-T | RPM-T (transferred alignment) | 34 | 0.548 | 0.388 | 0.742 | 0.335 | 0.234 | -0.335 | 22.613 | 40.978 |
| RPM-wT | RPM-wT (weighted + transferred) | 34 | 0.548 | 0.388 | 0.740 | 0.356 | 0.235 | -0.359 | 22.914 | 41.094 |
| IPL3 | Inverse power law (IPL3) | 34 | 0.435 | 0.391 | 0.484 | 0.400 | 0.307 | -0.252 | 17.941 | 32.202 |
| IPL2 | Power law (IPL2) | 34 | 0.543 | 0.479 | 0.614 | 0.483 | 0.405 | -0.436 | 12.798 | 24.111 |
| EXP3 | Exponential (EXP3) | 34 | 2.037 | 1.677 | 2.419 | 1.837 | 0.457 | -1.807 | 14.111 | 25.937 |
| LOG2 | Logarithmic (LOG2) | 34 | 10.305 | 9.632 | 10.968 | 10.407 | 12.969 | -10.278 | 3.085 | 6.040 |
| FLAT | No improvement (FLAT) | 34 | 0.276 | 0.238 | 0.318 | 0.243 | 0.212 | 0.149 | 24.720 | 44.172 |
| DFOLS | Fixed-complexity formula (DF-OLS) | 34 | 1.251 | 0.955 | 1.566 | 1.076 | 0.261 | -1.138 | 21.518 | 38.276 |
| SLOPE-T | Transferred slope (SLOPE-T) | 34 | 0.288 | 0.260 | 0.318 | 0.284 | 0.246 | -0.109 | 19.966 | 37.674 |

**Table S28.** Paired tests excluding the ICRAF-VisNIR tasks.

| comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-w | 34 | 253.000 | 0.457 | -0.003 | -0.005 | 0.000905 | -0.150 | 13 | 21 | 0.928 |
| RPM-T | 34 | 93.000 | 0.000248 | 0.043 | 0.010 | 0.110 | 0.687 | 26 | 8 | 0.001 |
| RPM-wT | 34 | 121.000 | 0.002 | 0.052 | 0.003 | 0.136 | 0.593 | 23 | 11 | 0.008 |
| IPL3 | 34 | 110.000 | 0.000903 | 0.164 | 0.116 | 0.228 | 0.630 | 29 | 5 | 0.005 |
| IPL2 | 34 | 69.000 | 2.87e-05 | 0.278 | 0.189 | 0.336 | 0.768 | 29 | 5 | 0.000201 |
| EXP3 | 34 | 0.000 | 1.16e-10 | 1.576 | 1.064 | 2.042 | 1.000 | 34 | 0 | 1.16e-09 |
| LOG2 | 34 | 0.000 | 1.16e-10 | 10.155 | 9.366 | 10.712 | 1.000 | 34 | 0 | 1.16e-09 |
| FLAT | 34 | 237.000 | 0.309 | -0.003 | -0.026 | 0.011 | -0.203 | 16 | 18 | 0.928 |
| DFOLS | 34 | 4.000 | 8.15e-10 | 0.827 | 0.358 | 1.220 | 0.987 | 33 | 1 | 6.52e-09 |
| SLOPE-T | 34 | 297.000 | 1.000 | 0.024 | -0.045 | 0.062 | 0.002 | 19 | 15 | 1.000 |

**Table S29.** POST HOC: noise fraction σ²/var(y) fitted on pilots (RPM, RPM-T) against the large-sample fit, by task and pilot size; share of pilots below one tenth of the large-sample value.

| task | method | n0 | noise frac full pool rfree | noise frac full pool r1 | median pilot noise frac | pct pilots below tenth of full |
|---|---|---|---|---|---|---|
| AfSIS1-MIR:OC | RPM | 25 | 0.059 | 0.064 | 0.109 | 0.000 |
| AfSIS1-MIR:OC | RPM | 50 | 0.059 | 0.064 | 0.080 | 0.000 |
| AfSIS1-MIR:OC | RPM | 100 | 0.059 | 0.064 | 0.075 | 0.000 |
| AfSIS1-MIR:OC | RPM | 200 | 0.059 | 0.064 | 0.079 | 0.000 |
| AfSIS1-MIR:OC | RPM-T | 25 | 0.059 | 0.064 | 3.04e-08 | 70.000 |
| AfSIS1-MIR:OC | RPM-T | 50 | 0.059 | 0.064 | 0.031 | 15.000 |
| AfSIS1-MIR:OC | RPM-T | 100 | 0.059 | 0.064 | 0.042 | 0.000 |
| AfSIS1-MIR:OC | RPM-T | 200 | 0.059 | 0.064 | 0.065 | 0.000 |
| AfSIS1-MIR:clay | RPM | 25 | 0.170 | 0.187 | 0.227 | 0.000 |
| AfSIS1-MIR:clay | RPM | 50 | 0.170 | 0.187 | 0.233 | 0.000 |
| AfSIS1-MIR:clay | RPM | 100 | 0.170 | 0.187 | 0.222 | 0.000 |
| AfSIS1-MIR:clay | RPM | 200 | 0.170 | 0.187 | 0.217 | 0.000 |
| AfSIS1-MIR:clay | RPM-T | 25 | 0.170 | 0.187 | 0.159 | 0.000 |
| AfSIS1-MIR:clay | RPM-T | 50 | 0.170 | 0.187 | 0.178 | 0.000 |
| AfSIS1-MIR:clay | RPM-T | 100 | 0.170 | 0.187 | 0.175 | 0.000 |
| AfSIS1-MIR:clay | RPM-T | 200 | 0.170 | 0.187 | 0.198 | 0.000 |
| AfSIS1-MIR:pH | RPM | 25 | 0.135 | 0.157 | 0.267 | 0.000 |
| AfSIS1-MIR:pH | RPM | 50 | 0.135 | 0.157 | 0.238 | 0.000 |
| AfSIS1-MIR:pH | RPM | 100 | 0.135 | 0.157 | 0.244 | 0.000 |
| AfSIS1-MIR:pH | RPM | 200 | 0.135 | 0.157 | 0.194 | 0.000 |
| AfSIS1-MIR:pH | RPM-T | 25 | 0.135 | 0.157 | 0.118 | 0.000 |
| AfSIS1-MIR:pH | RPM-T | 50 | 0.135 | 0.157 | 0.144 | 0.000 |
| AfSIS1-MIR:pH | RPM-T | 100 | 0.135 | 0.157 | 0.201 | 0.000 |
| AfSIS1-MIR:pH | RPM-T | 200 | 0.135 | 0.157 | 0.166 | 0.000 |
| CGL:casein | RPM | 25 | 0.000219 | 0.000442 | 0.003 | 0.000 |
| CGL:casein | RPM | 50 | 0.000219 | 0.000442 | 0.001 | 0.000 |
| CGL:casein | RPM-T | 25 | 0.000219 | 0.000442 | 2.6e-10 | 90.000 |
| CGL:casein | RPM-T | 50 | 0.000219 | 0.000442 | 3.33e-11 | 80.000 |
| CGL:glucose | RPM | 25 | 0.000181 | 0.000384 | 0.002 | 0.000 |
| CGL:glucose | RPM | 50 | 0.000181 | 0.000384 | 0.001 | 0.000 |
| CGL:glucose | RPM-T | 25 | 0.000181 | 0.000384 | 8.74e-11 | 90.000 |
| CGL:glucose | RPM-T | 50 | 0.000181 | 0.000384 | 1.21e-11 | 90.000 |
| CGL:lactate | RPM | 25 | 0.000144 | 0.000268 | 0.001 | 0.000 |
| CGL:lactate | RPM | 50 | 0.000144 | 0.000268 | 0.00077 | 0.000 |
| CGL:lactate | RPM-T | 25 | 0.000144 | 0.000268 | 5.35e-11 | 80.000 |
| CGL:lactate | RPM-T | 50 | 0.000144 | 0.000268 | 4.44e-06 | 60.000 |
| CGL:moisture | RPM | 25 | 0.000155 | 0.000267 | 0.001 | 0.000 |
| CGL:moisture | RPM | 50 | 0.000155 | 0.000267 | 0.000666 | 0.000 |
| CGL:moisture | RPM-T | 25 | 0.000155 | 0.000267 | 2.4e-11 | 90.000 |
| CGL:moisture | RPM-T | 50 | 0.000155 | 0.000267 | 6.29e-11 | 90.000 |
| Diesel:bp50 | RPM | 25 | 0.044 | 0.059 | 0.166 | 0.000 |
| Diesel:bp50 | RPM | 50 | 0.044 | 0.059 | 0.101 | 0.000 |
| Diesel:bp50 | RPM | 100 | 0.044 | 0.059 | 0.086 | 0.000 |
| Diesel:bp50 | RPM-T | 25 | 0.044 | 0.059 | 0.026 | 20.000 |
| Diesel:bp50 | RPM-T | 50 | 0.044 | 0.059 | 0.007 | 50.000 |
| Diesel:bp50 | RPM-T | 100 | 0.044 | 0.059 | 0.027 | 0.000 |
| Diesel:cn | RPM | 25 | 0.598 | 0.613 | 0.605 | 0.000 |
| Diesel:cn | RPM | 50 | 0.598 | 0.613 | 0.578 | 0.000 |
| Diesel:cn | RPM | 100 | 0.598 | 0.613 | 0.532 | 0.000 |
| Diesel:cn | RPM-T | 25 | 0.598 | 0.613 | 0.529 | 0.000 |
| Diesel:cn | RPM-T | 50 | 0.598 | 0.613 | 0.507 | 0.000 |
| Diesel:cn | RPM-T | 100 | 0.598 | 0.613 | 0.471 | 0.000 |
| Diesel:d4052 | RPM | 25 | 0.004 | 0.006 | 0.106 | 0.000 |
| Diesel:d4052 | RPM | 50 | 0.004 | 0.006 | 0.021 | 0.000 |
| Diesel:d4052 | RPM | 100 | 0.004 | 0.006 | 0.011 | 0.000 |
| Diesel:d4052 | RPM-T | 25 | 0.004 | 0.006 | 2.66e-09 | 70.000 |
| Diesel:d4052 | RPM-T | 50 | 0.004 | 0.006 | 2.28e-10 | 90.000 |
| Diesel:d4052 | RPM-T | 100 | 0.004 | 0.006 | 1.91e-10 | 90.000 |
| Diesel:freeze | RPM | 25 | 0.187 | 0.221 | 0.439 | 0.000 |
| Diesel:freeze | RPM | 50 | 0.187 | 0.221 | 0.315 | 0.000 |

**Table S30.** Eigen-spectrum source ablation for RPM-T (defined before RPM-T results were inspected).

| variant | n tasks | mean abs logerr | median task abs logerr | mean bias | median diff | ci95 lo | ci95 hi | p holm | ref wins | ref losses |
|---|---|---|---|---|---|---|---|---|---|---|
| RPM-T | 38 | 0.433 | 0.227 | -0.181 | – | – | – | – | – | – |
| RPM-T-pilotcov | 38 | 0.249 | 0.209 | 0.047 | -0.011 | -0.026 | 0.000799 | 0.107 | 14.000 | 24.000 |
| RPM-T-pilotcov+tail | 38 | 0.465 | 0.219 | -0.243 | 0.007 | -0.010 | 0.021 | 0.528 | 21.000 | 17.000 |
| RPM-T-U250 | 38 | 0.385 | 0.225 | -0.086 | -0.000109 | -0.006 | 2.24e-06 | 0.148 | 15.000 | 23.000 |

**Table S31.** POST HOC: coverage and width of forecast brackets.

| bracket | n forecasts | coverage pct | coverage task mean pct | median width log | median width factor | coverage n0 25 | median width factor n0 25 | coverage n0 50 | median width factor n0 50 | coverage n0 100 | median width factor n0 100 | coverage n0 200 | median width factor n0 200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RPM-T, RPM] | 76360 | 42.539 | 26.523 | 0.358 | 1.430 | 43.743 | 1.549 | 46.550 | 1.446 | 34.832 | 1.209 | 16.679 | 1.037 |
| [IPL3, FLAT] | 76360 | 43.857 | 45.737 | 0.364 | 1.440 | 44.150 | 1.591 | 45.159 | 1.398 | 40.574 | 1.253 | 39.924 | 1.185 |
| [RPM, FLAT] | 76360 | 23.927 | 18.217 | 0.202 | 1.224 | 24.452 | 1.272 | 23.247 | 1.209 | 24.238 | 1.162 | 21.298 | 1.081 |

**Table S32.** Empirical coverage, median width factor (multiplicative, on RMSE) and share of bands wider than a factor of ten, for 80% and 95% forecast bands.

| method | nominal | coverage rows | coverage task mean | coverage task median | mean width log | mean width factor | median width factor | pct width factor gt10 |
|---|---|---|---|---|---|---|---|---|
| RPM | 80 | 45.025 | 45.837 | 51.310 | 0.429 | 1.536 | 1.481 | 0.330 |
| RPM | 95 | 60.909 | 61.807 | 70.913 | 0.633 | 1.883 | 1.778 | 0.716 |
| RPM-w | 80 | 46.476 | 47.274 | 52.929 | 0.439 | 1.552 | 1.494 | 0.423 |
| RPM-w | 95 | 62.553 | 63.392 | 72.056 | 0.646 | 1.909 | 1.799 | 0.803 |
| IPL3 | 80 | 85.006 | 85.997 | 87.788 | 313.454 | 13525630261996680156035075698740771013535191410900998387373018693529079312240145139923407317829645392094248679708885687459990037736718336.000 | 13.772 | 52.733 |
| IPL3 | 95 | 90.181 | 90.947 | 91.667 | 479.386 | 15654502531544877351884492538563782816543982384659471269092807907398549782588437176964027684872417786236927896699549793968827632097203241239776924574369752202540173812542704832054505172380622874137108036976640.000 | 55.198 | 61.936 |
| IPL2 | 80 | 28.724 | 29.778 | 28.333 | 0.560 | 1.751 | 1.520 | 1.544 |
| IPL2 | 95 | 41.787 | 43.253 | 41.271 | 0.857 | 2.356 | 1.898 | 4.639 |
| EXP3 | 80 | 71.407 | 72.538 | 74.194 | 9234986067817.363 | inf | 6.771 | 48.375 |
| EXP3 | 95 | 77.478 | 78.516 | 80.331 | 14123692387640.629 | inf | 18.636 | 52.061 |
| LOG2 | 80 | 15.392 | 15.825 | 16.329 | 4552.702 | inf | 1.000 | 5.909 |
| LOG2 | 95 | 19.807 | 20.414 | 22.115 | 6962.757 | inf | 1.000 | 8.630 |

**Table S33.** POST HOC: leave-one-source-out split-conformal bands (coverage and median width factor).

| method | nominal | coverage pct | median width factor |
|---|---|---|---|
| RPM | 80 | 77.889 | 2.408 |
| RPM | 95 | 93.057 | 4.657 |
| RPM-w | 80 | 78.188 | 2.446 |
| RPM-w | 95 | 93.182 | 4.681 |
| SLOPE-T | 80 | 76.912 | 2.172 |
| SLOPE-T | 95 | 92.883 | 4.157 |
| FLAT | 80 | 78.288 | 2.152 |
| FLAT | 95 | 93.182 | 4.131 |
| IPL3 | 80 | 77.447 | 3.161 |
| IPL3 | 95 | 92.939 | 8.380 |

**Table S34.** Pre-registered sample-size decision metric: share of pilots whose forecast calibration size n̂ for the RMSE truly achieved at n* = 4n0 or 16n0 lies within a factor of two of n*, and share whose forecast never reaches the target.

| method | target | pct within factor2 | pct within factor2 task mean | pct never reaches target | median abs log2 err finite |
|---|---|---|---|---|---|
| DFOLS | 4n0 | 7.290 | 6.776 | 18.458 | 1.903 |
| DFOLS | 16n0 | 2.789 | 2.783 | 36.871 | 3.536 |
| EXP3 | 4n0 | 7.430 | 8.103 | 22.243 | 1.921 |
| EXP3 | 16n0 | 0.068 | 0.050 | 34.150 | 3.608 |
| FLAT | 4n0 | 1.121 | 3.026 | 60.935 | 2.000 |
| FLAT | 16n0 | 0.000 | 0.000 | 84.762 | 4.000 |
| IPL2 | 4n0 | 24.019 | 21.930 | 4.486 | 1.692 |
| IPL2 | 16n0 | 8.027 | 7.717 | 5.510 | 2.917 |
| IPL3 | 4n0 | 22.991 | 23.377 | 14.019 | 1.710 |
| IPL3 | 16n0 | 8.095 | 7.717 | 21.701 | 2.808 |
| LOG2 | 4n0 | 11.916 | 8.893 | 1.308 | 1.968 |
| LOG2 | 16n0 | 1.633 | 1.633 | 1.361 | 3.780 |
| RPM | 4n0 | 6.589 | 6.743 | 46.963 | 2.000 |
| RPM | 16n0 | 2.245 | 2.233 | 69.864 | 3.960 |
| RPM-T | 4n0 | 14.346 | 22.599 | 33.364 | 2.000 |
| RPM-T | 16n0 | 4.354 | 4.283 | 52.449 | 3.267 |
| RPM-w | 4n0 | 6.355 | 6.447 | 48.037 | 2.000 |
| RPM-w | 16n0 | 2.449 | 2.467 | 70.340 | 4.000 |
| RPM-wT | 4n0 | 15.327 | 23.849 | 31.262 | 2.000 |
| RPM-wT | 16n0 | 4.082 | 4.083 | 51.497 | 3.247 |
| SLOPE-T | 4n0 | 27.944 | 25.154 | 4.393 | 1.590 |
| SLOPE-T | 16n0 | 14.150 | 14.000 | 4.490 | 2.545 |

**Table S35.** POST HOC: error of the forecast gain RMSE(n)/RMSE(n0) and balanced accuracy of the decision 'an 8× larger calibration set reduces RMSEP by ≥ 10%'.

| method | n tasks | mean task gain abs err | median task gain abs err | mean gain bias | decision 8x 10pct balanced acc | decision sensitivity | decision specificity | prevalence worthwhile |
|---|---|---|---|---|---|---|---|---|
| RPM | 38 | 0.290 | 0.230 | 0.284 | 0.578 | 0.286 | 0.870 | 0.961 |
| RPM-w | 38 | 0.288 | 0.211 | 0.276 | 0.592 | 0.284 | 0.900 | 0.961 |
| RPM-T | 38 | 0.375 | 0.279 | -0.091 | 0.500 | 0.601 | 0.400 | 0.961 |
| RPM-wT | 38 | 0.368 | 0.285 | -0.113 | 0.482 | 0.614 | 0.350 | 0.961 |
| IPL3 | 38 | 0.268 | 0.235 | -0.014 | 0.500 | 0.800 | 0.200 | 0.961 |
| IPL2 | 38 | 0.317 | 0.288 | -0.164 | 0.477 | 0.954 | 0.000 | 0.961 |
| EXP3 | 38 | 1.582 | 1.392 | -1.196 | 0.525 | 0.620 | 0.430 | 0.961 |
| LOG2 | 38 | 7.790 | 7.715 | -7.795 | 0.491 | 0.983 | 0.000 | 0.961 |
| FLAT | 38 | 0.254 | 0.221 | 0.254 | 0.500 | 0.000 | 1.000 | 0.961 |
| DFOLS | 38 | 0.993 | 0.816 | -0.943 | 0.535 | 0.849 | 0.220 | 0.961 |
| SLOPE-T | 38 | 0.188 | 0.116 | 0.071 | 0.500 | 1.000 | 0.000 | 0.961 |

**Table S36.** POST HOC: paired tests of gain error (reference: pre-registered RPM).

| reference | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RPM | RPM-w | 38 | 296.000 | 0.287 | -0.001 | -0.007 | 0.001 | -0.201 | 17 | 21 | 1.000 |
| RPM | RPM-T | 38 | 331.000 | 0.576 | -0.018 | -0.028 | -0.009 | -0.107 | 12 | 26 | 1.000 |
| RPM | RPM-wT | 38 | 317.000 | 0.446 | -0.036 | -0.043 | -0.027 | -0.144 | 12 | 26 | 1.000 |
| RPM | IPL3 | 38 | 370.000 | 1.000 | -0.000475 | -0.022 | 0.059 | -0.001 | 19 | 19 | 1.000 |
| RPM | IPL2 | 38 | 284.000 | 0.215 | 0.053 | 0.002 | 0.115 | 0.233 | 25 | 13 | 1.000 |
| RPM | EXP3 | 38 | 0.000 | 7.28e-12 | 1.234 | 0.659 | 1.500 | 1.000 | 38 | 0 | 7.28e-11 |
| RPM | LOG2 | 38 | 0.000 | 7.28e-12 | 7.487 | 6.780 | 8.246 | 1.000 | 38 | 0 | 7.28e-11 |
| RPM | FLAT | 38 | 278.000 | 0.184 | -0.009 | -0.045 | 0.023 | -0.250 | 16 | 22 | 1.000 |
| RPM | DFOLS | 38 | 39.000 | 5.52e-08 | 0.609 | 0.241 | 0.906 | 0.895 | 32 | 6 | 4.41e-07 |
| RPM | SLOPE-T | 38 | 45.000 | 1.22e-07 | -0.103 | -0.139 | -0.066 | -0.879 | 4 | 34 | 8.56e-07 |

**Table S37.** Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task).

| variant | n tasks | mean abs logerr | rpm same tasks | mean diff vs rpm | ci95 lo | ci95 hi | p raw | p holm | rank biserial |
|---|---|---|---|---|---|---|---|---|---|
| RPM | 38 | 0.258 | 0.258 | 0.000 | 0.000 | 0.000 | – | – | – |
| RPM-rfree | 38 | 0.554 | 0.258 | 0.296 | 0.181 | 0.409 | 8.67e-06 | 6.93e-05 | 0.771 |
| RPM-ML2 | 38 | 0.259 | 0.258 | 0.000896 | -0.054 | 0.057 | 0.500 | 1.000 | -0.128 |
| RPM-pilotcov | 38 | 0.259 | 0.258 | 0.000619 | -0.010 | 0.010 | 0.274 | 1.000 | 0.206 |
| RPM-pilotcov+tail | 38 | 0.262 | 0.258 | 0.004 | -0.004 | 0.011 | 0.096 | 0.478 | 0.312 |
| RPM-U250 | 38 | 0.260 | 0.258 | 0.002 | 0.00024 | 0.003 | 0.008 | 0.056 | 0.487 |
| RPM-Uextra | 13 | 0.162 | 0.162 | 0.000313 | -0.000313 | 0.000965 | 0.588 | 1.000 | 0.187 |
| RPM-kfold10 | 38 | 0.272 | 0.258 | 0.014 | 0.008 | 0.019 | 2.54e-06 | 2.29e-05 | 0.806 |
| RPM-cut0.5 | 38 | 0.286 | 0.258 | 0.028 | 0.010 | 0.048 | 0.040 | 0.239 | 0.382 |
| RPM-cut0.95 | 38 | 0.257 | 0.258 | -0.000657 | -0.003 | 0.000606 | 0.376 | 1.000 | 0.207 |

**Table S38.** Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios).

| variant | method | n tasks | mean abs logerr | mean bias | coverage80 |
|---|---|---|---|---|---|
| iid_ref_seasons123 | B-RPM | 1.000 | 0.212 | -0.098 | 73.333 |
| iid_ref_seasons123 | FLAT | 1.000 | 0.157 | 0.135 | – |
| iid_ref_seasons123 | IPL3 | 1.000 | 0.732 | -0.646 | 78.889 |
| iid_ref_seasons123 | RPM | 1.000 | 0.396 | 0.396 | 0.000 |
| iid_ref_seasons123 | RPM-T | 1.000 | 0.296 | 0.296 | 4.444 |
| iid_ref_seasons123 | RPM-wT | 1.000 | 0.379 | 0.379 | 4.444 |
| ks_pilot | B-RPM | 6.000 | 0.288 | 0.118 | 50.217 |
| ks_pilot | FLAT | 6.000 | 0.298 | 0.250 | – |
| ks_pilot | IPL3 | 6.000 | 0.317 | -0.082 | 77.391 |
| ks_pilot | RPM | 6.000 | 0.374 | 0.292 | 20.870 |
| ks_pilot | RPM-T | 6.000 | 0.327 | 0.187 | 31.739 |
| ks_pilot | RPM-wT | 6.000 | 0.333 | 0.171 | 31.522 |
| prep_raw | B-RPM | 6.000 | 0.290 | -0.181 | 50.862 |
| prep_raw | FLAT | 6.000 | 0.249 | -0.059 | – |
| prep_raw | IPL3 | 6.000 | 0.437 | -0.373 | 66.379 |
| prep_raw | RPM | 6.000 | 0.286 | 0.038 | 38.793 |
| prep_raw | RPM-T | 6.000 | 0.391 | -0.120 | 41.034 |
| prep_raw | RPM-wT | 6.000 | 0.441 | -0.138 | 40.862 |
| prep_sg1 | B-RPM | 6.000 | 0.321 | -0.031 | 45.517 |
| prep_sg1 | FLAT | 6.000 | 0.293 | 0.053 | – |
| prep_sg1 | IPL3 | 6.000 | 0.380 | -0.153 | 63.793 |
| prep_sg1 | RPM | 6.000 | 0.305 | 0.133 | 39.310 |
| prep_sg1 | RPM-T | 6.000 | 0.344 | 0.049 | 43.448 |
| prep_sg1 | RPM-wT | 6.000 | 0.343 | 0.026 | 43.276 |
| ref_noise | B-RPM | 6.000 | 0.139 | -0.028 | 61.724 |
| ref_noise | FLAT | 6.000 | 0.117 | 0.019 | – |
| ref_noise | IPL3 | 6.000 | 0.277 | -0.251 | 71.552 |
| ref_noise | RPM | 6.000 | 0.145 | 0.048 | 53.448 |
| ref_noise | RPM-T | 6.000 | 0.145 | 0.030 | 55.345 |
| ref_noise | RPM-wT | 6.000 | 0.142 | 0.011 | 55.690 |
| shift_population | B-RPM | 1.000 | 0.186 | 0.064 | 69.091 |
| shift_population | FLAT | 1.000 | 0.178 | 0.159 | – |
| shift_population | IPL3 | 1.000 | 0.380 | -0.233 | 73.636 |
| shift_population | RPM | 1.000 | 0.389 | 0.389 | 0.000 |
| shift_population | RPM-T | 1.000 | 0.335 | 0.335 | 2.727 |
| shift_population | RPM-wT | 1.000 | 0.381 | 0.381 | 6.364 |
| shift_season | B-RPM | 1.000 | 0.503 | -0.502 | 21.111 |
| shift_season | FLAT | 1.000 | 0.255 | -0.255 | – |
| shift_season | IPL3 | 1.000 | 1.040 | -1.040 | 41.111 |
| shift_season | RPM | 1.000 | 0.086 | 0.058 | 53.333 |
| shift_season | RPM-T | 1.000 | 0.105 | -0.065 | 77.778 |
| shift_season | RPM-wT | 1.000 | 0.099 | 0.014 | 85.556 |

**Table S39.** E0 simulation with Monte-Carlo ground truth (median absolute and signed log error).

| r | noise frac | n0 | method | median abs err | mean abs err | median bias |
|---|---|---|---|---|---|---|
| 0.500 | 0.100 | 30 | FLAT | 0.444 | 0.533 | 0.444 |
| 0.500 | 0.100 | 30 | IPL3 | 0.283 | 0.326 | 0.194 |
| 0.500 | 0.100 | 30 | RPM | 0.423 | 0.531 | 0.423 |
| 0.500 | 0.100 | 30 | RPM-T | 0.453 | 1.394 | 0.190 |
| 0.500 | 0.100 | 30 | RPM-w | 0.420 | 0.531 | 0.420 |
| 0.500 | 0.100 | 30 | RPM-wT | 0.461 | 1.439 | 0.191 |
| 0.500 | 0.100 | 60 | FLAT | 0.710 | 0.726 | 0.710 |
| 0.500 | 0.100 | 60 | IPL3 | 0.349 | 0.347 | 0.349 |
| 0.500 | 0.100 | 60 | RPM | 0.639 | 0.648 | 0.639 |
| 0.500 | 0.100 | 60 | RPM-T | 0.323 | 1.159 | 0.195 |
| 0.500 | 0.100 | 60 | RPM-w | 0.629 | 0.639 | 0.629 |
| 0.500 | 0.100 | 60 | RPM-wT | 0.324 | 1.256 | 0.171 |
| 0.500 | 0.100 | 120 | FLAT | 0.604 | 0.585 | 0.604 |
| 0.500 | 0.100 | 120 | IPL3 | 0.181 | 0.223 | 0.030 |
| 0.500 | 0.100 | 120 | RPM | 0.483 | 0.475 | 0.483 |
| 0.500 | 0.100 | 120 | RPM-T | 0.174 | 0.217 | 0.005 |
| 0.500 | 0.100 | 120 | RPM-w | 0.478 | 0.471 | 0.478 |
| 0.500 | 0.100 | 120 | RPM-wT | 0.178 | 0.218 | 0.017 |
| 0.500 | 0.300 | 30 | FLAT | 0.167 | 0.179 | 0.107 |
| 0.500 | 0.300 | 30 | IPL3 | 0.198 | 0.267 | -0.084 |
| 0.500 | 0.300 | 30 | RPM | 0.127 | 0.158 | 0.053 |
| 0.500 | 0.300 | 30 | RPM-T | 0.233 | 1.607 | -0.109 |
| 0.500 | 0.300 | 30 | RPM-w | 0.138 | 0.158 | 0.055 |
| 0.500 | 0.300 | 30 | RPM-wT | 0.207 | 1.760 | -0.103 |
| 0.500 | 0.300 | 60 | FLAT | 0.174 | 0.206 | 0.174 |
| 0.500 | 0.300 | 60 | IPL3 | 0.142 | 0.186 | -0.065 |
| 0.500 | 0.300 | 60 | RPM | 0.129 | 0.147 | 0.114 |
| 0.500 | 0.300 | 60 | RPM-T | 0.184 | 0.526 | -0.004 |
| 0.500 | 0.300 | 60 | RPM-w | 0.122 | 0.144 | 0.113 |
| 0.500 | 0.300 | 60 | RPM-wT | 0.187 | 0.600 | -0.002 |
| 0.500 | 0.300 | 120 | FLAT | 0.220 | 0.221 | 0.220 |
| 0.500 | 0.300 | 120 | IPL3 | 0.161 | 0.160 | 0.051 |
| 0.500 | 0.300 | 120 | RPM | 0.114 | 0.117 | 0.103 |
| 0.500 | 0.300 | 120 | RPM-T | 0.100 | 0.123 | -0.015 |
| 0.500 | 0.300 | 120 | RPM-w | 0.106 | 0.116 | 0.099 |
| 0.500 | 0.300 | 120 | RPM-wT | 0.091 | 0.125 | -0.013 |
| 1.000 | 0.100 | 30 | FLAT | 0.366 | 0.360 | 0.359 |
| 1.000 | 0.100 | 30 | IPL3 | 0.350 | 0.430 | -0.106 |
| 1.000 | 0.100 | 30 | RPM | 0.323 | 0.306 | 0.290 |
| 1.000 | 0.100 | 30 | RPM-T | 0.508 | 3.926 | -0.508 |
| 1.000 | 0.100 | 30 | RPM-w | 0.321 | 0.313 | 0.290 |
| 1.000 | 0.100 | 30 | RPM-wT | 0.560 | 3.992 | -0.560 |
| 1.000 | 0.100 | 60 | FLAT | 0.328 | 0.317 | 0.328 |
| 1.000 | 0.100 | 60 | IPL3 | 0.186 | 0.276 | -0.131 |
| 1.000 | 0.100 | 60 | RPM | 0.153 | 0.174 | 0.140 |
| 1.000 | 0.100 | 60 | RPM-T | 8.947 | 8.185 | -8.947 |
| 1.000 | 0.100 | 60 | RPM-w | 0.153 | 0.175 | 0.141 |
| 1.000 | 0.100 | 60 | RPM-wT | 8.064 | 7.503 | -8.064 |
| 1.000 | 0.100 | 120 | FLAT | 0.250 | 0.251 | 0.250 |
| 1.000 | 0.100 | 120 | IPL3 | 0.199 | 0.260 | -0.154 |
| 1.000 | 0.100 | 120 | RPM | 0.099 | 0.116 | 0.080 |
| 1.000 | 0.100 | 120 | RPM-T | 0.329 | 0.381 | -0.329 |
| 1.000 | 0.100 | 120 | RPM-w | 0.093 | 0.118 | 0.068 |
| 1.000 | 0.100 | 120 | RPM-wT | 0.307 | 0.384 | -0.307 |
| 1.000 | 0.300 | 30 | FLAT | 0.154 | 0.189 | 0.152 |
| 1.000 | 0.300 | 30 | IPL3 | 0.253 | 0.314 | -0.153 |
| 1.000 | 0.300 | 30 | RPM | 0.141 | 0.158 | 0.119 |
| 1.000 | 0.300 | 30 | RPM-T | 0.585 | 2.633 | -0.585 |
| 1.000 | 0.300 | 30 | RPM-w | 0.143 | 0.158 | 0.116 |
| 1.000 | 0.300 | 30 | RPM-wT | 0.561 | 2.565 | -0.561 |

**Table S40.** E0 simulation summarised by pilot size.

| method | n0 | median abs err | median bias |
|---|---|---|---|
| FLAT | 30 | 0.201 | 0.154 |
| FLAT | 60 | 0.179 | 0.178 |
| FLAT | 120 | 0.186 | 0.186 |
| IPL3 | 30 | 0.258 | -0.077 |
| IPL3 | 60 | 0.244 | -0.149 |
| IPL3 | 120 | 0.124 | -0.019 |
| RPM | 30 | 0.247 | 0.074 |
| RPM | 60 | 0.170 | 0.078 |
| RPM | 120 | 0.114 | 0.061 |
| RPM-T | 30 | 0.565 | -0.517 |
| RPM-T | 60 | 0.560 | -0.502 |
| RPM-T | 120 | 0.151 | -0.113 |
| RPM-w | 30 | 0.247 | 0.075 |
| RPM-w | 60 | 0.170 | 0.080 |
| RPM-w | 120 | 0.111 | 0.059 |
| RPM-wT | 30 | 0.582 | -0.522 |
| RPM-wT | 60 | 0.523 | -0.463 |
| RPM-wT | 120 | 0.154 | -0.103 |

**Table S41.** Per-task error analysis (RPM vs IPL3) with spectral and fitted descriptors.

| task | family | eigen decay exponent | n pool | rpm mae | rpm bias | theory fit err | noise frac | r | ipl3 mae |
|---|---|---|---|---|---|---|---|---|---|
| CGL:glucose | mixture | 4.886 | 173 | 0.762 | 0.750 | 0.208 | 0.000181 | 0.629 | 0.400 |
| Diesel:d4052 | fuel | 3.784 | 296 | 0.748 | 0.747 | 0.140 | 0.004 | 0.656 | 0.401 |
| CGL:casein | mixture | 4.899 | 173 | 0.711 | 0.711 | 0.194 | 0.000219 | 0.652 | 0.350 |
| Diesel:total | fuel | 3.803 | 296 | 0.475 | -0.144 | 0.278 | 0.061 | 0.859 | 0.868 |
| CGL:lactate | mixture | 4.901 | 173 | 0.472 | 0.462 | 0.404 | 0.000144 | 0.699 | 0.358 |
| CGL:moisture | mixture | 4.910 | 173 | 0.467 | 0.447 | 0.353 | 0.000155 | 0.712 | 0.332 |
| Diesel:bp50 | fuel | 3.785 | 296 | 0.447 | 0.415 | 0.183 | 0.044 | 0.582 | 0.453 |
| Tablets:assay | pharma | 3.208 | 491 | 0.430 | -0.022 | 0.091 | 0.042 | 0.879 | 0.445 |
| Diesel:visc | fuel | 3.782 | 296 | 0.372 | 0.345 | 0.121 | 0.094 | 0.548 | 0.395 |
| KSSL-MIR:OC | soil | 2.757 | 12002 | 0.361 | -0.145 | 0.121 | 0.018 | 0.837 | 0.809 |
| Mango:DM | fruit | 4.480 | 3016 | 0.350 | 0.350 | 0.079 | 0.166 | 0.317 | 0.679 |
| Tecator:fat | meat | 5.686 | 161 | 0.303 | -0.189 | 0.378 | 0.015 | 0.630 | 0.423 |
| Tecator:protein | meat | 5.669 | 161 | 0.279 | 0.230 | 0.224 | 0.034 | 0.406 | 0.370 |
| KSSL-VisNIR:OC | soil | 3.860 | 11997 | 0.262 | 0.158 | 0.119 | 0.208 | 0.401 | 0.553 |
| KSSL-MIR:CEC | soil | 2.763 | 12001 | 0.261 | 0.042 | 0.137 | 0.046 | 0.648 | 0.645 |
| ICRAF-MIR:OC | soil | 2.803 | 2771 | 0.255 | 0.178 | 0.137 | 0.106 | 0.671 | 0.432 |
| Tecator:moisture | meat | 5.677 | 161 | 0.243 | -0.130 | 0.081 | 0.047 | 0.769 | 0.377 |
| KSSL-MIR:clay | soil | 2.742 | 11997 | 0.242 | 0.107 | 0.109 | 0.131 | 0.468 | 0.570 |
| Neospectra-NIR:OC | soil | 3.908 | 1580 | 0.232 | 0.210 | 0.041 | 0.268 | 0.462 | 0.276 |
| AfSIS1-MIR:OC | soil | 2.954 | 1425 | 0.226 | 0.157 | 0.054 | 0.059 | 0.694 | 0.418 |
| Diesel:freeze | fuel | 3.774 | 296 | 0.210 | 0.057 | 0.048 | 0.187 | 0.573 | 0.390 |
| Neospectra-NIR:clay | soil | 3.912 | 1580 | 0.198 | 0.107 | 0.078 | 0.480 | 0.379 | 0.315 |
| KSSL-VisNIR:CEC | soil | 3.831 | 12011 | 0.186 | 0.087 | 0.101 | 0.400 | 0.362 | 0.444 |
| KSSL-VisNIR:pH | soil | 3.828 | 11993 | 0.178 | 0.121 | 0.115 | 0.333 | 0.342 | 0.515 |
| Diesel:cn | fuel | 3.809 | 286 | 0.178 | 0.054 | 0.183 | 0.598 | 0.679 | 0.251 |
| KSSL-MIR:pH | soil | 2.758 | 12002 | 0.170 | 0.089 | 0.044 | 0.184 | 0.524 | 0.482 |
| ICRAF-MIR:pH | soil | 2.823 | 2830 | 0.168 | 0.005 | 0.087 | 0.187 | 0.595 | 0.361 |
| ICRAF-MIR:CEC | soil | 2.800 | 2736 | 0.167 | 0.011 | 0.054 | 0.127 | 0.660 | 0.395 |
| AfSIS1-MIR:clay | soil | 2.952 | 1422 | 0.165 | 0.056 | 0.058 | 0.170 | 0.531 | 0.299 |
| Neospectra-NIR:CEC | soil | 3.903 | 1571 | 0.164 | 0.021 | 0.073 | 0.436 | 0.461 | 0.292 |
| KSSL-VisNIR:clay | soil | 3.887 | 11997 | 0.163 | 0.096 | 0.076 | 0.393 | 0.352 | 0.488 |
| ICRAF-MIR:clay | soil | 2.802 | 2801 | 0.156 | 0.025 | 0.063 | 0.215 | 0.552 | 0.422 |
| ICRAF-VisNIR:pH | soil | 3.658 | 2828 | 0.142 | 0.110 | 0.045 | 0.371 | 0.342 | 0.291 |
| Neospectra-NIR:pH | soil | 3.920 | 1572 | 0.139 | -0.021 | 0.157 | 0.319 | 0.382 | 0.290 |
| ICRAF-VisNIR:OC | soil | 3.655 | 2775 | 0.138 | -0.034 | 0.084 | 0.426 | 0.396 | 0.347 |
| ICRAF-VisNIR:clay | soil | 3.671 | 2805 | 0.129 | -0.061 | 0.099 | 0.375 | 0.338 | 0.408 |
| AfSIS1-MIR:pH | soil | 2.960 | 1427 | 0.123 | -0.012 | 0.112 | 0.135 | 0.508 | 0.300 |
| ICRAF-VisNIR:CEC | soil | 3.643 | 2740 | 0.121 | 0.041 | 0.030 | 0.549 | 0.538 | 0.306 |

**Table S42.** Spearman correlations between per-task RPM error and task descriptors.

| descriptor | spearman rho | p | n |
|---|---|---|---|
| eigen_decay_exponent | 0.350 | 0.031 | 38 |
| theory_fit_err | 0.640 | 1.54e-05 | 38 |
| noise_frac | -0.804 | 1.22e-09 | 38 |
| r | 0.542 | 0.000438 | 38 |
| n_pool | -0.447 | 0.005 | 38 |

**Table S43.** Accuracy by data-set family.

| family | method | label | n tasks | mean abs logerr | ci95 lo | ci95 hi | median task abs logerr | median abs logerr rows | mean bias | pct within 10 | pct within 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| fruit | RPM | RPM (pre-registered, r = 1) | 1 | 0.350 | 0.350 | 0.350 | 0.350 | 0.348 | 0.350 | 0.833 | 4.722 |
| fruit | IPL3 | Inverse power law (IPL3) | 1 | 0.679 | 0.679 | 0.679 | 0.679 | 0.225 | -0.571 | 25.833 | 45.000 |
| fruit | FLAT | No improvement (FLAT) | 1 | 0.168 | 0.168 | 0.168 | 0.168 | 0.126 | 0.128 | 40.556 | 65.278 |
| fruit | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 0.372 | 0.372 | 0.372 | 0.372 | 0.138 | -0.317 | 36.389 | 59.722 |
| fuel | RPM | RPM (pre-registered, r = 1) | 6 | 0.405 | 0.265 | 0.562 | 0.410 | 0.325 | 0.246 | 16.500 | 30.778 |
| fuel | IPL3 | Inverse power law (IPL3) | 6 | 0.459 | 0.332 | 0.639 | 0.398 | 0.336 | -0.212 | 16.194 | 29.611 |
| fuel | FLAT | No improvement (FLAT) | 6 | 0.361 | 0.248 | 0.473 | 0.343 | 0.270 | 0.133 | 20.167 | 35.806 |
| fuel | DFOLS | Fixed-complexity formula (DF-OLS) | 6 | 1.986 | 1.212 | 2.623 | 2.297 | 0.416 | -1.877 | 12.750 | 24.278 |
| meat | RPM | RPM (pre-registered, r = 1) | 3 | 0.275 | 0.243 | 0.303 | 0.279 | 0.227 | -0.030 | 22.444 | 41.333 |
| meat | IPL3 | Inverse power law (IPL3) | 3 | 0.390 | 0.370 | 0.423 | 0.377 | 0.310 | -0.277 | 14.778 | 29.333 |
| meat | FLAT | No improvement (FLAT) | 3 | 0.261 | 0.230 | 0.298 | 0.256 | 0.203 | -0.111 | 26.556 | 46.778 |
| meat | DFOLS | Fixed-complexity formula (DF-OLS) | 3 | 0.963 | 0.757 | 1.094 | 1.038 | 0.456 | -0.930 | 11.556 | 20.333 |
| mixture | RPM | RPM (pre-registered, r = 1) | 4 | 0.603 | 0.470 | 0.736 | 0.591 | 0.569 | 0.592 | 3.083 | 6.917 |
| mixture | IPL3 | Inverse power law (IPL3) | 4 | 0.360 | 0.339 | 0.387 | 0.354 | 0.279 | 0.071 | 17.917 | 33.667 |
| mixture | FLAT | No improvement (FLAT) | 4 | 0.474 | 0.443 | 0.505 | 0.470 | 0.422 | 0.446 | 8.167 | 18.417 |
| mixture | DFOLS | Fixed-complexity formula (DF-OLS) | 4 | 1.891 | 1.554 | 2.229 | 1.823 | 0.359 | -1.707 | 16.083 | 28.917 |
| pharma | RPM | RPM (pre-registered, r = 1) | 1 | 0.430 | 0.430 | 0.430 | 0.430 | 0.324 | -0.022 | 16.400 | 30.500 |
| pharma | IPL3 | Inverse power law (IPL3) | 1 | 0.445 | 0.445 | 0.445 | 0.445 | 0.323 | -0.078 | 15.400 | 27.900 |
| pharma | FLAT | No improvement (FLAT) | 1 | 0.356 | 0.356 | 0.356 | 0.356 | 0.293 | 0.206 | 16.400 | 31.600 |
| pharma | DFOLS | Fixed-complexity formula (DF-OLS) | 1 | 1.268 | 1.268 | 1.268 | 1.268 | 0.332 | -0.934 | 17.800 | 30.300 |
| soil | RPM | RPM (pre-registered, r = 1) | 23 | 0.189 | 0.167 | 0.214 | 0.168 | 0.149 | 0.059 | 33.556 | 58.778 |
| soil | IPL3 | Inverse power law (IPL3) | 23 | 0.420 | 0.370 | 0.476 | 0.408 | 0.285 | -0.310 | 19.944 | 34.944 |
| soil | FLAT | No improvement (FLAT) | 23 | 0.199 | 0.175 | 0.225 | 0.178 | 0.160 | 0.117 | 31.433 | 55.656 |
| soil | DFOLS | Fixed-complexity formula (DF-OLS) | 23 | 0.935 | 0.624 | 1.309 | 0.526 | 0.179 | -0.838 | 29.222 | 50.589 |

**Table S44.** Measured run time per pilot.

| component | mean | median | max |
|---|---|---|---|
| RPM point forecast (s per pilot) | 0.019 | 0.017 | 0.117 |
| RPM 50 group-bootstrap refits (s per pilot) | 0.952 | 0.881 | 2.717 |
| Within-pilot sub-sampling curve for IPL/EXP/LOG fits (s per pilot) | 0.277 | 0.168 | 1.481 |

**Table S45.** Paired tests against RPM at pilot size n0 = 25.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | RPM-w | 38 | 364.000 | 0.931 | -0.000186 | -0.005 | 0.004 | -0.018 | 18 | 20 | 1.000 |
| 25 | RPM-T | 38 | 130.000 | 0.00028 | 0.038 | 0.012 | 0.136 | 0.649 | 30 | 8 | 0.001 |
| 25 | RPM-wT | 38 | 145.000 | 0.000726 | 0.054 | 0.010 | 0.172 | 0.609 | 28 | 10 | 0.003 |
| 25 | IPL3 | 38 | 97.000 | 2.43e-05 | 0.288 | 0.166 | 0.361 | 0.738 | 31 | 7 | 0.000146 |
| 25 | IPL2 | 38 | 68.000 | 1.7e-06 | 0.383 | 0.300 | 0.502 | 0.816 | 32 | 6 | 1.19e-05 |
| 25 | EXP3 | 38 | 0.000 | 7.28e-12 | 2.672 | 1.700 | 4.146 | 1.000 | 38 | 0 | 7.28e-11 |
| 25 | LOG2 | 38 | 0.000 | 7.28e-12 | 12.162 | 11.290 | 12.583 | 1.000 | 38 | 0 | 7.28e-11 |
| 25 | FLAT | 38 | 301.000 | 0.321 | 0.010 | 7.45e-05 | 0.019 | 0.188 | 25 | 13 | 0.963 |
| 25 | DFOLS | 38 | 1.000 | 1.46e-11 | 1.201 | 0.915 | 2.220 | 0.997 | 37 | 1 | 1.16e-10 |
| 25 | SLOPE-T | 38 | 339.000 | 0.657 | 0.038 | -0.037 | 0.061 | 0.085 | 22 | 16 | 1.000 |

**Table S46.** Paired tests against RPM at pilot size n0 = 50.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | RPM-w | 38 | 272.000 | 0.157 | -0.003 | -0.007 | -0.000685 | -0.266 | 12 | 26 | 0.471 |
| 50 | RPM-T | 38 | 104.000 | 4.27e-05 | 0.027 | 0.009 | 0.051 | 0.719 | 31 | 7 | 0.000256 |
| 50 | RPM-wT | 38 | 157.000 | 0.001 | 0.031 | 0.000923 | 0.057 | 0.576 | 26 | 12 | 0.006 |
| 50 | IPL3 | 38 | 118.000 | 0.000122 | 0.132 | 0.101 | 0.223 | 0.682 | 33 | 5 | 0.000611 |
| 50 | IPL2 | 38 | 56.000 | 4.63e-07 | 0.244 | 0.168 | 0.336 | 0.849 | 33 | 5 | 3.24e-06 |
| 50 | EXP3 | 38 | 6.000 | 1.02e-10 | 1.083 | 0.381 | 1.850 | 0.984 | 36 | 2 | 9.17e-10 |
| 50 | LOG2 | 38 | 0.000 | 7.28e-12 | 10.808 | 9.628 | 11.630 | 1.000 | 38 | 0 | 7.28e-11 |
| 50 | FLAT | 38 | 350.000 | 0.774 | 0.005 | -0.011 | 0.015 | -0.055 | 20 | 18 | 0.774 |
| 50 | DFOLS | 38 | 25.000 | 6.58e-09 | 0.242 | 0.129 | 0.663 | 0.933 | 34 | 4 | 5.26e-08 |
| 50 | SLOPE-T | 38 | 302.000 | 0.328 | 0.051 | -0.026 | 0.083 | 0.185 | 23 | 15 | 0.656 |

**Table S47.** Paired tests against RPM at pilot size n0 = 100.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | RPM-w | 31 | 234.000 | 0.794 | -0.003 | -0.009 | 0.004 | -0.056 | 11 | 20 | 1.000 |
| 100 | RPM-T | 31 | 195.000 | 0.308 | 0.002 | -0.005 | 0.009 | 0.214 | 17 | 14 | 1.000 |
| 100 | RPM-wT | 31 | 225.000 | 0.664 | -0.011 | -0.018 | 0.006 | -0.093 | 14 | 17 | 1.000 |
| 100 | IPL3 | 31 | 78.000 | 0.000495 | 0.081 | 0.062 | 0.134 | 0.685 | 25 | 6 | 0.003 |
| 100 | IPL2 | 31 | 25.000 | 8.42e-07 | 0.130 | 0.114 | 0.229 | 0.899 | 27 | 4 | 6.74e-06 |
| 100 | EXP3 | 31 | 16.000 | 1.57e-07 | 0.701 | 0.401 | 0.901 | 0.935 | 28 | 3 | 1.42e-06 |
| 100 | LOG2 | 31 | 0.000 | 9.31e-10 | 7.164 | 6.370 | 9.009 | 1.000 | 31 | 0 | 9.31e-09 |
| 100 | FLAT | 31 | 236.000 | 0.824 | -0.002 | -0.014 | 0.015 | -0.048 | 15 | 16 | 1.000 |
| 100 | DFOLS | 31 | 150.000 | 0.055 | 0.027 | -0.002 | 0.067 | 0.395 | 18 | 13 | 0.331 |
| 100 | SLOPE-T | 31 | 176.000 | 0.163 | 0.047 | -0.015 | 0.089 | 0.290 | 19 | 12 | 0.817 |

**Table S48.** Paired tests against RPM at pilot size n0 = 200.

| n0 | comparison | n tasks | wilcoxon W | p raw | median diff | ci95 lo | ci95 hi | rank biserial | ref wins | ref losses | p holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 200 | RPM-w | 25 | 115.000 | 0.210 | -0.005 | -0.009 | 3e-05 | -0.292 | 8 | 17 | 0.423 |
| 200 | RPM-T | 25 | 107.000 | 0.141 | -0.003 | -0.009 | 0.003 | -0.342 | 9 | 16 | 0.423 |
| 200 | RPM-wT | 25 | 74.000 | 0.016 | -0.022 | -0.028 | -0.007 | -0.545 | 6 | 19 | 0.112 |
| 200 | IPL3 | 25 | 76.000 | 0.019 | 0.045 | -0.003 | 0.097 | 0.532 | 17 | 8 | 0.112 |
| 200 | IPL2 | 25 | 29.000 | 0.000103 | 0.088 | 0.021 | 0.179 | 0.822 | 22 | 3 | 0.000824 |
| 200 | EXP3 | 25 | 13.000 | 5.25e-06 | 0.240 | 0.147 | 0.341 | 0.920 | 21 | 4 | 4.72e-05 |
| 200 | LOG2 | 25 | 1.000 | 1.19e-07 | 3.120 | 1.238 | 5.508 | 0.994 | 24 | 1 | 1.19e-06 |
| 200 | FLAT | 25 | 88.000 | 0.045 | -0.013 | -0.020 | 0.003 | -0.458 | 10 | 15 | 0.180 |
| 200 | DFOLS | 25 | 158.000 | 0.916 | -0.010 | -0.028 | 0.040 | -0.028 | 12 | 13 | 0.916 |
| 200 | SLOPE-T | 25 | 83.000 | 0.032 | 0.051 | -0.020 | 0.116 | 0.489 | 16 | 9 | 0.159 |

![**Figure S1.** Distribution of task-level forecast errors for all methods of the first design (version-2 data).](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig4_main_accuracy.png){width=15cm}

![**Figure S2.** Robustness scenarios: mean absolute log error by method.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig8_robustness.png){width=15cm}

![**Figure S3.** Alignment exponents by spectral region (large-sample fits).](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig12_alignment_exponents.png){width=15cm}

![**Figure S4.** Pre-registered sample-size decision metric by method.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig10_sample_size_decisions.png){width=15cm}

![**Figure S5.** Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig9_error_analysis.png){width=15cm}

![**Figure S6.** Data-set overview: number of samples and eigen-decay exponent by family.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig11_dataset_overview.png){width=15cm}

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


# Supplementary Note 2: Pre-specification addendum for B-RPM (hypotheses HB1–HB4)


_Written 2026-11-21 ~21:00 UTC (session 3; committed in git commit "Add B-RPM ..."), before any version-2 forecast result was inspected. The version-2 main
stage was running at that time; only version-1 results (archived, `archive/v1_pre_review/`) had been seen._

## Rationale
Version-1 results and review cycle 1 showed that (i) no pilot-only forecaster beat the no-improvement rule (FLAT) on
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


# Supplementary Note 3: Data-leakage audit


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
| Design informed by evaluation data | Default r = 1 chosen in exploratory work on ICRAF-VisNIR | Disclosed; sensitivity analysis S0 excludes ICRAF-VisNIR tasks | Sensitivity tables excluding ICRAF-VisNIR |


# Supplementary Note 4: Literature matrix and novelty map


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

