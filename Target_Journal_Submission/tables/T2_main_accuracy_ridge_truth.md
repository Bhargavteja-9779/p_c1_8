**Forecast accuracy vs ridge truth**

| method | label | n_tasks | mean_abs_logerr | ci95_lo | ci95_hi | median_task_abs_logerr | median_abs_logerr_rows | mean_bias | pct_within_10 | pct_within_20 |
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
