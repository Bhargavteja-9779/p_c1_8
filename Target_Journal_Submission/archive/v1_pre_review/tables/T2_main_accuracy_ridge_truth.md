**Forecast accuracy vs ridge truth**

| method | label | n_tasks | mean_abs_logerr | ci95_lo | ci95_hi | median_task_abs_logerr | median_abs_logerr_rows | mean_bias | pct_within_10 | pct_within_20 |
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
