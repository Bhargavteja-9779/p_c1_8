# Pre-specification addendum 2: native-resolution confirmation study

_Written and committed 2026-11-22 (session 4) after inspecting the six-task full-resolution robustness run
(KSSL-MIR:OC, ICRAF-MIR:clay, KSSL-VisNIR:clay, Neospectra-NIR:pH, Diesel:bp50, Tablets:assay) and BEFORE running any
other task at full resolution._

**Observation that generated the hypothesis (6 tasks, n0 = 25-100, 10 pilots):** mean task-level |log error| B-RPM 0.249,
FLAT 0.287, RPM 0.333, IPL3 0.463, whereas on the same tasks with sub-sampled spectra FLAT 0.254 < B-RPM 0.271.

**Hypothesis HC1 (confirmatory):** at near-native spectral resolution (MIR 4 cm-1, Vis-NIR/NIR 2 nm, diesel and tablets
undecimated, CGL/Tecator/mango as provided), B-RPM has a lower mean task-level absolute log error than FLAT on the 32
tasks NOT used to generate the hypothesis. Test: two-sided Wilcoxon signed-rank test over the 32 held-out tasks, alpha 0.05;
also source-level means and bootstrap CI. Secondary: B-RPM vs RPM, IPL3 and SLOPE-T (LOSO), gain error, compatible-set
coverage and hidden-signal share at native resolution (all 38 tasks).

**Design (fixed):** identical splits, seeds, pilot sizes (25, 50, 100, 200), pilot numbers (20 per task; 10 per outer split
for N < 1000) as the main study; B-RPM prior estimated leave-one-source-out from the large-sample fits at native
resolution; no bootstrap for RPM; no other change to any method.
