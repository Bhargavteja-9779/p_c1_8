# Journal verification log

All measurements are reproducible with the scripts in `scripts/`; raw outputs are in `data/`.

## 1. Method for acceptance-time verification
- **PubMed (Elsevier, OUP, ACS, RSC, IOP, AIP and other MEDLINE/PMC-indexed journals):** `scripts/pubmed_acceptance_times.py` queries E-utilities for articles of a given ISSN entering PubMed in a date window (journal-article publication type; reviews, editorials, comments, errata excluded), parses `<History>/<PubMedPubDate PubStatus="received|accepted">` and reports the distribution of accepted − received (days).
- **Crossref (Springer Nature, Taylor & Francis):** `scripts/crossref_acceptance_times.py` parses the publisher-deposited `received`/`accepted` assertions. Elsevier, OUP, IEEE, Wiley and SAGE do not deposit these assertions (checked 2026-11-15), and IEEE records in PubMed carry no history dates, so IEEE timelines could not be measured.
- **Caveats.** (i) Only accepted papers have an acceptance date (this is inherent to the metric). (ii) "Received" is the publisher-deposited original receipt date; some publishers reset it for reject-and-resubmit manuscripts, which would bias durations downward. (iii) These are *empirical distributions of accepted papers*, not guarantees for any individual manuscript.

## 2. Analytica Chimica Acta — verification record
| Item | Evidence | Status |
|---|---|---|
| Legitimacy / publisher | Elsevier journal page (shop.elsevier.com/journals/analytica-chimica-acta/0003-2670), NLM catalogue (PubMed ISSN 0003-2670 / 1873-4324) | Verified |
| 2025 JIF = 6.1; 5-yr IF = 5.8 | Publisher page (shop.elsevier.com, fetched 2026-11-15); bioxbio.com "2025 (2026 update) 6.1" | Verified (two sources) |
| JCR category & quartile: Chemistry, Analytical, SCIE, Q1, 23/110 | ablesci.com relay of JCR 2026 (released 2026-06-17) | Verified via relay (Clarivate itself not accessible) |
| Submission→acceptance | `data/final3_acceptance_times_n1000.json`: median 62 d, IQR 46–84, n = 999, 48.9 % ≤ 60 d, 87.2 % ≤ 100 d | Empirically verified |
| Topic-matched subset | `data/aca_chemometrics_subset_acceptance_times.json`: median 73 d, IQR 51–96.5, n = 118, 77.1 % ≤ 100 d | Empirically verified |
| Official first-decision / review time | ScienceDirect insights panel → HTTP 403. ablesci relays "平均5.9周 (Elsevier website)" (≈ 41 d) without a label | **UNVERIFIED** |
| Scope | Publisher page (aims & scope text); listings reproducing the official scope ("new analytical methods, including chemometric techniques and data treatment"; "discourages specialized application-oriented submissions"; tutorials on chemometric methods welcome) | Verified |
| Recent comparable papers | `data/aca_dataanalysis_corpus_2023_2026.json` (312 records, titles+abstracts from PubMed) | Verified |
| Abstract format | 18/40 recent ACA records in PubMed have labelled abstracts "BACKGROUND / RESULTS / SIGNIFICANCE (AND NOVELTY)"; median abstract 220 words; median 5 keywords | Observed |
| APC (OA route) | Not available on any accessible official page | **UNVERIFIED** (subscription route has no APC) |
| Data/code policy | Elsevier research-data policy: data-availability statement required; code/data sharing encouraged | Standard Elsevier policy (Guide for Authors itself not fetchable) |

## 3. Other journals: raw measurements
- `data/pubmed_acceptance_times_batch1.json` (45 journals: biomedical informatics, OUP, IEEE (no dates), environmental)
- `data/pubmed_acceptance_times_batch2.json` (40 journals: ACS, Elsevier analytical/environmental, RSC, Wiley, Springer)
- `data/crossref_acceptance_times.json` (49 Springer Nature / T&F journals)
- Official relayed metrics for 20 Elsevier/ACS/IEEE/Wiley/Springer/RSC journals were collected by a delegated search and are summarised in `journal_comparison.md` (sources: manusights.com relays of ScienceDirect insights; ACS journal-metrics snippets; Springer journal pages; ablesci/bioxbio JCR relays).

## 4. Requirements that could not be satisfied or verified
1. No high-JIF (≥ 8) Q1 journal with a scope suitable for a chemometric methodology paper was found with verified submission→acceptance ≤ 100 d; the fast high-JIF journals (Water Research, Chemical Engineering Journal, J. Hazardous Materials) are scope mismatches.
2. No suitable journal had a verified median ≤ 30 days.
3. ACA's official first-decision time and OA APC are unverified (publisher pages blocked automated access).
4. Individual acceptance within 100 days cannot be guaranteed: 12.8 % of ACA papers overall, and 22.9 % of its chemometrics papers, took longer than 100 days in the measurement window.
