---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J014 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Ledger: J014-live-ops-designer

Fields: `templates/jobs/ledger.md`. Paper = `C:\Users\Firew\Downloads\live-ops-designer-research.txt` (LP), outside git.

| id | from | to | ask | inside | status | hops | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J014-T01 | lead | extractor (Sonnet high) | LP mandate, 15 rules, §1-§5 (lines 1-247): cases, rhythm, content types, events, ranking + 2 templates → notes | yes | done (42 FC rows: 32 P1; 31 limits; 2 templates captured) | 1 | knowledge/reference/live-ops/01-mandate-cases-rhythm-events-ranking.md | 2026-10-21 |
| J014-T02 | lead | extractor (Sonnet high) | LP §6-§11 + don'ts + open questions (lines 248-536): feedback, communication, measurement, health, Roblox rules, process + 4 templates → notes | yes | done (53 FC rows: 39 P1; 17 Roblox-rule rows; 5 templates captured) | 1 | knowledge/reference/live-ops/02-feedback-comms-measurement-rules-process.md | 2026-10-21 |
| J014-T03 | lead | researcher (Sonnet high) | feedback routes fact sheet (Roblox surveys, in-game text + filtering + younger players, data store + Open Cloud, Discord API, terms, export, privacy) | yes | done (Q1-Q8, route cards R1-R9; 3 gaps 403/not found; K-01..K-03 platform-policy updates) | 1 | knowledge/reference/live-ops/feedback-routes-fact-sheet.md | 2026-10-21 |
| J014-T04 | lead | fact-checker (researcher, Sonnet high) | Roblox R01-R22 + every §10 rule + limited-time offers / age bands | yes | done (58 rows: 49 confirmed, 5 corrected, 4 unverified; KU-1..KU-9 kit updates proposed) | 1 | knowledge/reference/live-ops/fact-check-roblox.md | 2026-10-21 |
| J014-T05 | lead | fact-checker (researcher, Sonnet high) | studio cases G01-G30: dates, numbers, scope | yes | done (36 rows: 18 confirmed, 9 corrected, 8 unverified, 1 dropped) | 1 | knowledge/reference/live-ops/fact-check-cases.md | 2026-10-21 |
| J014-T06 | lead | feature-builder (Opus medium) | feedback count tool + offline tests (`T06-count-tool-brief.md`) | yes | done (19 tests; 12/12 planted faults caught; lead re-ran tests OK) | 1 | tools/liveops/feedback_count.py, tools/tests/test_feedback_count.py | 2026-10-21 |
| J014-T07 | lead | test-pack builder (Sonnet high) | synthetic live game pack with 10 traps + grader key (digest item 7) | yes | done ("Mothlight Meadow", 151 items, traps T1-T10, key from a real tool run) | 1 | test-pack/, hidden-grader/ | 2026-10-21 |
| J014-T08 | lead | live-ops-designer (Opus high) | G2 test on the pack (no access to hidden-grader/) | yes | done (needs-decision: 4 urgent harms routed; rank 1 = fix harms + Orchard way-finding + free Halloween quest; 14 skill gaps, fixed: skill-gaps-T08.md) | 1 | g2/live-ops/ (trial, not a gate: J014-D8) | 2026-10-21 |
| J014-T09 | lead | grader (Sonnet high) | grade T08 against hidden-grader/T07-key.md + E1/E2, separate context | yes | done (24.5 / 26; traps 10/10 PASS; E1 8/8; E2 4 PASS 1 PARTIAL 2 N/A; no safety failure; counts byte-identical on re-run) | 1 | grades-g2.md | 2026-10-21 |
