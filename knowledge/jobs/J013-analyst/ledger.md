---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J013 G1 (proposed)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Ledger: J013-analyst

Fields: `templates/jobs/ledger.md`. Paper = `C:\Users\Firew\Downloads\Roblox_Analyst_Research_2026.txt` (AP), outside git. Nothing starts before G1.

| id | from | to | ask | inside | status | hops | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J013-T01 | lead | extract+check A (Sonnet high) | AP Roblox platform facts R1-R21 (dashboards, retention, benchmarks, monetization, performance, economy, funnels, Experiments, EHD, Open Cloud, price optimization, paid random items, feedback, insights, 2026-10-12 break, RDC roadmap) + the 2026-08-24 Open Cloud APIs post → notes + fact-check | yes | done (80 rows: 73 confirmed, 2 corrected, 5 unverified-labelled, 0 dropped; analytics skill T-10/T-11/T-12 errors found; Experiments needs universe:read) | 1 | knowledge/reference/analyst/01-roblox-platform-facts.md | 2026-10-21 |
| J013-T02 | lead | extract+check B (Sonnet high) | AP statistics and experiment rules S1-S8 + §5, §6, §10 (power, duration, SRM, stopping, verdicts, update designs, reproducibility) → notes + fact-check | yes | done (64 rows: 45 confirmed, 7 corrected, 12 unverified-labelled, 0 dropped; F-01..F-14 check values re-run by lead in Python, all match; verdict rule needs owner G3) | 1 | knowledge/reference/analyst/02-statistics-experiments.md | 2026-10-21 |
| J013-T03 | lead | extract+check C (Sonnet high) | AP studio practice I1-I12 + §3, §4, §7, §8, §9, appendices (diagnosis, economy, purchases, feedback coding, event contract, reporting, templates, don'ts) → notes + fact-check | yes | done (48 rows: 37 confirmed (7 second-hand: Valve, Halo PDFs unreadable), 8 corrected, 2 unverified, 1 dropped; 1 needs-decision flag on analytics T-03) | 1 | knowledge/reference/analyst/03-practice-diagnosis-reporting.md | 2026-10-21 |
| J013-T04 | lead | tool builder (Opus medium) | `tools/analytics/` pull + history + stats helpers + offline tests (`T04-tool-brief.md`) | yes | done (48 offline tests; planted-key faults caught; lead re-ran tests + SRM check; 2 brief updates sent: Experiments scope, check values) | 1 | tools/analytics/, tools/tests/test_analytics_*.py | 2026-10-21 |
| J013-T05 | lead | analyst (new) | G2 test on a SYNTHETIC TEST history (no key set; digest item 8 default b): T05a weekly page (Sonnet medium), T05b deep investigation "why did D1 drop" (Opus high) | yes | done (both found the planted phone regression; T05b also the mix effect with a 3.5 / 1.9 pt split and 4 of 4 generator faults; 23 gaps reported; grading in g2-scenario.md) | 1 | knowledge/jobs/J013-analyst/analyst/g2-weekly/, g2-investigation/ | 2026-10-21 |
| J013-T06 | lead | analyst (Sonnet medium) + grader (Sonnet high) | hidden cases H1-H5: T06a analyst answers (analyst/hidden-run/), T06b separate grader; lead ruled RQ-1 (made-up numbers in Part 1 = fail); H1 and H4 re-run twice after skill fixes (T06c-e) | yes | done (final: H1 9, H2 9, H3 9, H4 10, H5 9 → 5/5 pass; open: H1 never asked the decision → template row added; H3 routing fix not re-run) | 3 | grade-J013-hidden.md |
| J013-T07 | lead | lead | fix the 23 G2 gaps: `show --breakdown`, `stats mix` (+3 tests, 51 total), README filter format, data-tools §4 reading rules (rates without counts, maturity vs API value, units, faults), finding template, urgent-problem rule, frontmatter rule, perf-engineer hand-off §6, checklist PASS meaning, stacked causes, Part 1 length, week basis; live-ops now a real role (J014) | yes | done | 1 | tools/analytics/, .agents/skills/analysis-*, templates/analytics/ | 2026-10-21 |
