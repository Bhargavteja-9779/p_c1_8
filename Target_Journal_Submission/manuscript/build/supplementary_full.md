# Supplementary Material

**What can a pilot set tell about a calibration learning curve? An observability limit for sample-size planning in spectroscopy**

All tables and figures below are generated automatically by `run_all.py` from the per-pilot raw results.

**Table S1.** Paired comparisons of B-RPM (pre-specified hypotheses HB1–HB2 and exploratory comparisons): mean improvement over the reference (positive favours B-RPM), bootstrap 95% CI, Wilcoxon p (task level, Holm-adjusted) and source-level results.

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

**Table S2.** Share of the apparent error floor at the observability horizon of a pilot that is learnable target power, per task and pilot size (large-sample fits).

| task | family | n0 | hidden share | p |
|---|---|---|---|---|
| AfSIS1-MIR:OC | soil | 25 | 0.289 | 212 |
| AfSIS1-MIR:OC | soil | 50 | 0.082 | 212 |
| AfSIS1-MIR:OC | soil | 100 | 0.007 | 212 |
| AfSIS1-MIR:OC | soil | 150 | 0.000646 | 212 |
| AfSIS1-MIR:clay | soil | 25 | 0.250 | 212 |
| AfSIS1-MIR:clay | soil | 50 | 0.096 | 212 |
| AfSIS1-MIR:clay | soil | 100 | 0.015 | 212 |
| AfSIS1-MIR:clay | soil | 150 | 0.002 | 212 |
| AfSIS1-MIR:pH | soil | 25 | 0.377 | 212 |
| AfSIS1-MIR:pH | soil | 50 | 0.169 | 212 |
| AfSIS1-MIR:pH | soil | 100 | 0.031 | 212 |
| AfSIS1-MIR:pH | soil | 150 | 0.005 | 212 |
| CGL:casein | mixture | 25 | 0.532 | 116 |
| CGL:casein | mixture | 50 | 0.217 | 116 |
| CGL:casein | mixture | 100 | 0.010 | 116 |
| CGL:glucose | mixture | 25 | 0.668 | 116 |
| CGL:glucose | mixture | 50 | 0.342 | 116 |
| CGL:glucose | mixture | 100 | 0.020 | 116 |
| CGL:lactate | mixture | 25 | 0.470 | 116 |
| CGL:lactate | mixture | 50 | 0.164 | 116 |
| CGL:lactate | mixture | 100 | 0.007 | 116 |
| CGL:moisture | mixture | 25 | 0.374 | 116 |
| CGL:moisture | mixture | 50 | 0.114 | 116 |
| CGL:moisture | mixture | 100 | 0.004 | 116 |
| Diesel:bp50 | fuel | 25 | 0.252 | 200 |
| Diesel:bp50 | fuel | 50 | 0.124 | 200 |
| Diesel:bp50 | fuel | 100 | 0.037 | 200 |
| Diesel:bp50 | fuel | 150 | 0.007 | 200 |
| Diesel:cn | fuel | 25 | 0.005 | 200 |
| Diesel:cn | fuel | 50 | 0.002 | 200 |
| Diesel:cn | fuel | 100 | 0.000425 | 200 |
| Diesel:cn | fuel | 150 | 7.01e-05 | 200 |
| Diesel:d4052 | fuel | 25 | 0.556 | 200 |
| Diesel:d4052 | fuel | 50 | 0.311 | 200 |
| Diesel:d4052 | fuel | 100 | 0.097 | 200 |
| Diesel:d4052 | fuel | 150 | 0.018 | 200 |
| Diesel:freeze | fuel | 25 | 0.110 | 200 |
| Diesel:freeze | fuel | 50 | 0.049 | 200 |
| Diesel:freeze | fuel | 100 | 0.014 | 200 |
| Diesel:freeze | fuel | 150 | 0.003 | 200 |
| Diesel:total | fuel | 25 | 0.010 | 200 |
| Diesel:total | fuel | 50 | 0.002 | 200 |
| Diesel:total | fuel | 100 | 0.000431 | 200 |
| Diesel:total | fuel | 150 | 5.64e-05 | 200 |
| Diesel:visc | fuel | 25 | 0.192 | 200 |
| Diesel:visc | fuel | 50 | 0.095 | 200 |
| Diesel:visc | fuel | 100 | 0.029 | 200 |
| Diesel:visc | fuel | 150 | 0.006 | 200 |
| ICRAF-MIR:CEC | soil | 25 | 0.215 | 212 |
| ICRAF-MIR:CEC | soil | 50 | 0.068 | 212 |
| ICRAF-MIR:CEC | soil | 100 | 0.008 | 212 |
| ICRAF-MIR:CEC | soil | 150 | 0.000713 | 212 |
| ICRAF-MIR:OC | soil | 25 | 0.208 | 212 |
| ICRAF-MIR:OC | soil | 50 | 0.064 | 212 |
| ICRAF-MIR:OC | soil | 100 | 0.007 | 212 |
| ICRAF-MIR:OC | soil | 150 | 0.000621 | 212 |
| ICRAF-MIR:clay | soil | 25 | 0.254 | 212 |
| ICRAF-MIR:clay | soil | 50 | 0.102 | 212 |
| ICRAF-MIR:clay | soil | 100 | 0.016 | 212 |
| ICRAF-MIR:clay | soil | 150 | 0.002 | 212 |
| ICRAF-MIR:pH | soil | 25 | 0.209 | 212 |
| ICRAF-MIR:pH | soil | 50 | 0.075 | 212 |
| ICRAF-MIR:pH | soil | 100 | 0.010 | 212 |
| ICRAF-MIR:pH | soil | 150 | 0.001 | 212 |
| ICRAF-VisNIR:CEC | soil | 25 | 0.031 | 208 |
| ICRAF-VisNIR:CEC | soil | 50 | 0.010 | 208 |
| ICRAF-VisNIR:CEC | soil | 100 | 0.002 | 208 |
| ICRAF-VisNIR:CEC | soil | 150 | 0.000595 | 208 |
| ICRAF-VisNIR:OC | soil | 25 | 0.153 | 208 |
| ICRAF-VisNIR:OC | soil | 50 | 0.074 | 208 |
| ICRAF-VisNIR:OC | soil | 100 | 0.026 | 208 |
| ICRAF-VisNIR:OC | soil | 150 | 0.008 | 208 |
| ICRAF-VisNIR:clay | soil | 25 | 0.237 | 208 |
| ICRAF-VisNIR:clay | soil | 50 | 0.137 | 208 |
| ICRAF-VisNIR:clay | soil | 100 | 0.057 | 208 |
| ICRAF-VisNIR:clay | soil | 150 | 0.018 | 208 |
| ICRAF-VisNIR:pH | soil | 25 | 0.247 | 208 |
| ICRAF-VisNIR:pH | soil | 50 | 0.143 | 208 |
| ICRAF-VisNIR:pH | soil | 100 | 0.059 | 208 |
| ICRAF-VisNIR:pH | soil | 150 | 0.018 | 208 |
| KSSL-MIR:CEC | soil | 25 | 0.519 | 212 |
| KSSL-MIR:CEC | soil | 50 | 0.230 | 212 |
| KSSL-MIR:CEC | soil | 100 | 0.035 | 212 |
| KSSL-MIR:CEC | soil | 150 | 0.003 | 212 |
| KSSL-MIR:OC | soil | 25 | 0.445 | 212 |
| KSSL-MIR:OC | soil | 50 | 0.128 | 212 |
| KSSL-MIR:OC | soil | 100 | 0.010 | 212 |
| KSSL-MIR:OC | soil | 150 | 0.000517 | 212 |
| KSSL-MIR:clay | soil | 25 | 0.493 | 212 |
| KSSL-MIR:clay | soil | 50 | 0.284 | 212 |
| KSSL-MIR:clay | soil | 100 | 0.075 | 212 |
| KSSL-MIR:clay | soil | 150 | 0.013 | 212 |
| KSSL-MIR:pH | soil | 25 | 0.336 | 212 |
| KSSL-MIR:pH | soil | 50 | 0.155 | 212 |
| KSSL-MIR:pH | soil | 100 | 0.031 | 212 |
| KSSL-MIR:pH | soil | 150 | 0.004 | 212 |
| KSSL-VisNIR:CEC | soil | 25 | 0.178 | 208 |
| KSSL-VisNIR:CEC | soil | 50 | 0.093 | 208 |
| KSSL-VisNIR:CEC | soil | 100 | 0.036 | 208 |
| KSSL-VisNIR:CEC | soil | 150 | 0.011 | 208 |
| KSSL-VisNIR:OC | soil | 25 | 0.298 | 208 |
| KSSL-VisNIR:OC | soil | 50 | 0.154 | 208 |
| KSSL-VisNIR:OC | soil | 100 | 0.058 | 208 |
| KSSL-VisNIR:OC | soil | 150 | 0.017 | 208 |
| KSSL-VisNIR:clay | soil | 25 | 0.189 | 208 |
| KSSL-VisNIR:clay | soil | 50 | 0.102 | 208 |
| KSSL-VisNIR:clay | soil | 100 | 0.041 | 208 |
| KSSL-VisNIR:clay | soil | 150 | 0.013 | 208 |
| KSSL-VisNIR:pH | soil | 25 | 0.233 | 208 |
| KSSL-VisNIR:pH | soil | 50 | 0.132 | 208 |
| KSSL-VisNIR:pH | soil | 100 | 0.054 | 208 |
| KSSL-VisNIR:pH | soil | 150 | 0.017 | 208 |
| Mango:DM | fruit | 25 | 0.299 | 94 |
| Mango:DM | fruit | 50 | 0.141 | 94 |
| Neospectra-NIR:CEC | soil | 25 | 0.047 | 150 |
| Neospectra-NIR:CEC | soil | 50 | 0.010 | 150 |
| Neospectra-NIR:CEC | soil | 100 | 0.000413 | 150 |
| Neospectra-NIR:OC | soil | 25 | 0.104 | 150 |
| Neospectra-NIR:OC | soil | 50 | 0.024 | 150 |
| Neospectra-NIR:OC | soil | 100 | 0.000948 | 150 |
| Neospectra-NIR:clay | soil | 25 | 0.119 | 150 |
| Neospectra-NIR:clay | soil | 50 | 0.035 | 150 |
| Neospectra-NIR:clay | soil | 100 | 0.003 | 150 |
| Neospectra-NIR:pH | soil | 25 | 0.131 | 150 |
| Neospectra-NIR:pH | soil | 50 | 0.039 | 150 |
| Neospectra-NIR:pH | soil | 100 | 0.003 | 150 |
| Tablets:assay | pharma | 25 | 0.073 | 216 |
| Tablets:assay | pharma | 50 | 0.010 | 216 |
| Tablets:assay | pharma | 100 | 0.000368 | 216 |
| Tablets:assay | pharma | 150 | 1.66e-05 | 216 |
| Tecator:fat | meat | 25 | 0.007 | 99 |
| Tecator:fat | meat | 50 | 0.001 | 99 |
| Tecator:moisture | meat | 25 | 0.000377 | 99 |
| Tecator:moisture | meat | 50 | 4.74e-05 | 99 |
| Tecator:protein | meat | 25 | 0.192 | 99 |
| Tecator:protein | meat | 50 | 0.065 | 99 |

**Table S3.** Prior-free compatible set: coverage of the true RMSEP, median width factor and median information fraction, by extrapolation ratio and pilot size (HB4).

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

**Table S4.** Mean signed log error by extrapolation ratio for all forecasters (pooled over tasks). Key forecasters shown; all forecasters are in the machine-readable table files.

| rb | B-RPM | B-RPM-LOFO | RPM | IPL3 | WEI | FLAT | SLOPE-T | SLOPE-T-LOFO |
|---|---|---|---|---|---|---|---|---|
| 2 | -0.006 | -0.018 | 0.049 | -0.108 | -0.235 | 0.001 | -0.101 | -0.141 |
| 4 | 0.040 | 0.031 | 0.149 | -0.180 | -0.337 | 0.141 | -0.063 | -0.143 |
| 8 | -0.031 | -0.036 | 0.145 | -0.274 | -0.308 | 0.184 | -0.130 | -0.279 |
| 16 | -0.114 | -0.111 | 0.103 | -0.381 | -0.360 | 0.192 | -0.244 | -0.489 |
| >=32 | -0.134 | -0.146 | 0.169 | -0.665 | -0.414 | 0.271 | -0.326 | -0.673 |

**Table S5.** Reachability decisions split into reachable and unreachable targets.

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

**Table S6.** Calibration tasks: pool and test sizes, number of spectral variables, largest ground-truth calibration size and eigen-decay exponent (slope of log λk vs log k, k ≤ 60).

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

**Table S7.** Theory validity: deterministic-equivalent curve fitted to the full-pool cross-validation path (r free or r = 1) vs empirical ridge and PLS learning curves (absolute log error per task).

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
| Neospectra-NIR:CEC | fixed1 | 0.110 | 0.145 | 1.000 | 0.469 |
| Neospectra-NIR:CEC | free | 0.073 | 0.102 | 0.461 | 0.436 |
| Neospectra-NIR:OC | fixed1 | 0.084 | 0.108 | 1.000 | 0.311 |
| Neospectra-NIR:OC | free | 0.041 | 0.038 | 0.462 | 0.268 |
| Neospectra-NIR:clay | fixed1 | 0.132 | 0.146 | 1.000 | 0.541 |
| Neospectra-NIR:clay | free | 0.078 | 0.081 | 0.379 | 0.480 |
| Neospectra-NIR:pH | fixed1 | 0.218 | 0.239 | 1.000 | 0.367 |
| Neospectra-NIR:pH | free | 0.157 | 0.178 | 0.382 | 0.319 |
| Tablets:assay | fixed1 | 0.110 | 0.126 | 1.000 | 0.043 |
| Tablets:assay | free | 0.091 | 0.102 | 0.879 | 0.042 |
| Tecator:fat | fixed1 | 0.389 | 0.437 | 1.000 | 0.017 |
| Tecator:fat | free | 0.378 | 0.426 | 0.630 | 0.015 |
| Tecator:moisture | fixed1 | 0.088 | 0.103 | 1.000 | 0.049 |
| Tecator:moisture | free | 0.081 | 0.093 | 0.769 | 0.047 |
| Tecator:protein | fixed1 | 0.273 | 0.323 | 1.000 | 0.060 |
| Tecator:protein | free | 0.224 | 0.274 | 0.406 | 0.034 |

**Table S8.** POST HOC: regression of the ground-truth learning-curve slope (log RMSE per doubling of n) on large-sample theory parameters, and Spearman correlations.

| descriptor | spearman rho | p | r2 |
|---|---|---|---|
| noise_frac_full_pool | 0.541 | 0.000455 | – |
| r_full_pool | -0.331 | 0.042 | – |
| eigen_decay_exponent | -0.261 | 0.114 | – |
| n_pool | 0.453 | 0.004 | – |
| OLS: slope ~ r + log(noise fraction) + eigen-decay | – | 2.3e-11 | 0.783 |

**Table S9.** All forecasters on the version-2 design: task-level mean absolute log error (level), mean absolute gain error, mean signed bias, and source-level means.

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

**Table S10.** Level and gain error by application family for all forecasters. Key forecasters shown; all forecasters are in the machine-readable table files.

| level 0 | level 1 | B-RPM | B-RPM-LOFO | RPM | IPL3 | WEI | FLAT | SLOPE-T | SLOPE-T-LOFO |
|---|---|---|---|---|---|---|---|---|---|
| level | fruit | 0.219 | 0.219 | 0.350 | 0.679 | 0.365 | 0.168 | 0.209 | 0.209 |
| level | fuel | 0.350 | 0.350 | 0.405 | 0.459 | 0.433 | 0.361 | 0.330 | 0.330 |
| level | meat | 0.270 | 0.270 | 0.275 | 0.390 | 0.681 | 0.261 | 0.304 | 0.304 |
| level | mixture | 0.569 | 0.569 | 0.603 | 0.360 | 0.491 | 0.474 | 0.375 | 0.375 |
| level | pharma | 0.387 | 0.387 | 0.430 | 0.445 | 0.661 | 0.356 | 0.313 | 0.313 |
| level | soil | 0.214 | 0.230 | 0.189 | 0.420 | 0.327 | 0.199 | 0.258 | 0.435 |
| gain | fruit | 0.231 | 0.231 | 0.491 | 0.611 | 0.275 | 0.269 | 0.161 | 0.161 |
| gain | fuel | 0.360 | 0.360 | 0.505 | 0.307 | 0.215 | 0.404 | 0.285 | 0.285 |
| gain | meat | 0.268 | 0.268 | 0.332 | 0.231 | 0.345 | 0.247 | 0.164 | 0.164 |
| gain | mixture | 0.777 | 0.777 | 0.805 | 0.372 | 0.268 | 0.659 | 0.540 | 0.540 |
| gain | pharma | 0.122 | 0.122 | 0.172 | 0.254 | 0.440 | 0.273 | 0.101 | 0.101 |
| gain | soil | 0.158 | 0.171 | 0.243 | 0.299 | 0.217 | 0.292 | 0.109 | 0.259 |

**Table S11.** Coverage and median width factor of 80% and 95% bands by family and pilot size, including the post-hoc leave-one-source-out recalibration of B-RPM.

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
| B-RPM-LOFO-cal (post hoc) | fam | soil | 0.881 | 0.971 | 2.008 | 23 |
| B-RPM-LOFO-cal (post hoc) | n0 | 25 | 0.815 | 0.952 | 3.149 | 38 |
| B-RPM-LOFO-cal (post hoc) | n0 | 50 | 0.805 | 0.959 | 2.312 | 38 |
| B-RPM-LOFO-cal (post hoc) | n0 | 100 | 0.848 | 0.947 | 1.781 | 31 |
| B-RPM-LOFO-cal (post hoc) | n0 | 200 | 0.801 | 0.946 | 1.469 | 25 |
| B-RPM-LOFO-cal (post hoc) | all | all | 0.794 | 0.947 | 2.375 | 38 |

**Table S12.** Brier score of the probabilistic decision 'an eightfold larger calibration set reduces RMSEP by at least 15%'.

| method | brier task mean | prevalence | mean prob | brier climatology |
|---|---|---|---|---|
| B-RPM | 0.290 | 0.448 | 0.497 | 0.247 |
| B-RPM-LOFO | 0.291 | 0.448 | 0.478 | 0.247 |
| SLOPE-T | 0.294 | 0.448 | 0.661 | 0.247 |
| SLOPE-T-LOFO | 0.358 | 0.448 | 0.758 | 0.247 |
| FLAT | 0.274 | 0.448 | 0.319 | 0.247 |
| RPM | 0.306 | 0.448 | 0.240 | 0.247 |
| IPL3 | 0.277 | 0.448 | 0.487 | 0.247 |

**Table S13.** Mean absolute per-task bias by extrapolation ratio (does not allow opposite task biases to cancel). Key forecasters shown; all forecasters are in the machine-readable table files.

| rb | B-RPM | B-RPM-LOFO | RPM | IPL3 | WEI | FLAT | SLOPE-T | SLOPE-T-LOFO |
|---|---|---|---|---|---|---|---|---|
| 2 | 0.139 | 0.151 | 0.147 | 0.124 | 0.235 | 0.107 | 0.156 | 0.196 |
| 4 | 0.193 | 0.203 | 0.197 | 0.205 | 0.337 | 0.179 | 0.221 | 0.300 |
| 8 | 0.147 | 0.157 | 0.162 | 0.278 | 0.308 | 0.187 | 0.228 | 0.372 |
| 16 | 0.143 | 0.149 | 0.131 | 0.381 | 0.361 | 0.192 | 0.251 | 0.489 |
| >=32 | 0.171 | 0.191 | 0.182 | 0.665 | 0.418 | 0.271 | 0.337 | 0.673 |

**Table S14.** B-RPM level error by tertile of the information fraction within each pilot size.

| n0 | level mae low | level mae mid | level mae high |
|---|---|---|---|
| 25 | 0.420 | 0.379 | 0.313 |
| 50 | 0.327 | 0.282 | 0.224 |
| 100 | 0.233 | 0.163 | 0.185 |
| 200 | 0.136 | 0.141 | 0.129 |

**Table S15.** Forecast error for a fixed target calibration size (400, 800, 1600) by pilot size: value of a larger pilot or second batch.

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

**Table S16.** Reachability decisions for an absolute RMSEP target at budget N: one-shot (pilot N/8), staged (second batch, N/4) and compatible-set-gated policies.

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

**Table S17.** Forecast accuracy against the ridge ground truth (per-task means of |log(RMSE_fc/RMSE_true)|, bootstrap 95% CI over tasks, bias and share of forecasts within ±10% and ±20%).

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

**Table S18.** Forecast accuracy against the PLS ground truth.

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

**Table S19.** Sensitivity analysis excluding the four ICRAF-VisNIR tasks used in exploratory work.

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

**Table S20.** Pre-registered ablation of RPM (n0 ∈ {50,100}, 10 pilots per task).

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

**Table S21.** Robustness and distribution-shift experiments (six representative tasks and mango shift scenarios).

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

**Table S22.** E0 simulation summarised by pilot size.

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

**Table S23.** Measured run time per pilot.

| component | mean | median | max |
|---|---|---|---|
| RPM point forecast (s per pilot) | 0.019 | 0.017 | 0.117 |
| RPM 50 group-bootstrap refits (s per pilot) | 0.952 | 0.881 | 2.717 |
| Within-pilot sub-sampling curve for IPL/EXP/LOG fits (s per pilot) | 0.277 | 0.168 | 1.481 |

![**Figure S1.** Distribution of task-level forecast errors for all methods of the first design (version-2 data).](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig4_main_accuracy.png){width=15cm}

![**Figure S2.** Robustness scenarios: mean absolute log error by method.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig8_robustness.png){width=15cm}

![**Figure S3.** Pre-registered sample-size decision metric by method.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig10_sample_size_decisions.png){width=15cm}

![**Figure S4.** Per-task RPM error against theory misfit, fitted noise fraction and eigen-decay exponent.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig9_error_analysis.png){width=15cm}

![**Figure S5.** Data-set overview: number of samples and eigen-decay exponent by family.](/home/user/p_c1_8/Target_Journal_Submission/figures/Fig11_dataset_overview.png){width=15cm}

# Supplementary Note 1: Pre-specified protocol of the first design (time-stamped)


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


# Supplementary Note 2: Pre-specification addendum for B-RPM (hypotheses HB1–HB4), reproduced verbatim as committed; 'version 2' refers to the final re-analysis reported in the article and 'identification set' to the compatible set


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

