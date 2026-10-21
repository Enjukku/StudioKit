---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Ledger: J010

Format: `templates/jobs/ledger.md`. Rework rows go to `knowledge/reference/engineering/rework/`; paper notes to `knowledge/reference/engineering/paper/`.

| id | from | to | ask | inside | status | hops | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J010-T01 | lead | extractor (Sonnet high) | git history 2026-09-30 → 10-04 | yes | done (26 multi-round, 10 two-round) | 1 | rework/git-a.md | 2026-10-21 |
| J010-T02 | lead | extractor (Sonnet high) | git history 2026-10-05 → 10-10 | yes | done (14 multi-round, 13 appendix) | 1 | rework/git-b.md | 2026-10-21 |
| J010-T03 | lead | extractor (Sonnet high) | git history 2026-10-11 → 10-20 | yes | done (24 multi-round, 12 appendix) | 1 | rework/git-c.md | 2026-10-21 |
| J010-T04 | lead | extractor (Sonnet high) | session logs `knowledge/logs/**` | yes | done (11 multi-round, 9 appendix, agent-review section) | 1 | rework/logs.md | 2026-10-21 |
| J010-T05 | lead | extractor (Sonnet high) | tried-and-failed, decisions, handoffs, research, old engineering agents + skills | yes | done (7 new rows, 36 updates; old-agents 190 rows) | 1 | rework/records.md | 2026-10-21 |
| J010-T06 | lead | extractor (Sonnet high) | paper §1-4 | yes | done (97 lessons, 15+8 starred claims) | 1 | paper/part-1.md | 2026-10-21 |
| J010-T07 | lead | extractor (Sonnet high) | paper §5-8 | yes | done (84 lessons, 15+7 starred claims) | 1 | paper/part-2.md | 2026-10-21 |
| J010-T08 | lead | extractor (Sonnet high) | paper §9-11, don'ts, open questions, register | yes | done (71 lessons, 90 sources) | 1 | paper/part-3.md | 2026-10-21 |
| J010-T09 | lead | fact-checker (Sonnet high) | Luau + engine claims vs docs mirror | yes | done (47 confirmed, 12 partly, 3 corrected, 1 outdated; const probe MCP-verified by lead) | 1 | paper/factcheck-engine.md | 2026-10-21 |
| J010-T10 | lead | fact-checker (Sonnet high) | Anthropic, craft, eval claims vs web | yes | done (42 confirmed, 4 partly, 2 corrected, 3 older-model-only) | 1 | paper/factcheck-practice.md | 2026-10-21 |
| J010-T11 | lead | lead | merged rework study | yes | done | 0 | knowledge/reference/engineering/rework-study.md | 2026-10-21 |
| J010-T12 | lead | test-bench writer (Opus high) | builder tasks FB1-3, QB1-3 (brief-testbench.md) | yes | done (refs 100 %, every trap fails; second correct design passes FB1-3) | 1 | eng-sandbox/tasks, eng-evals-hidden | 2026-10-21 |
| J010-T13 | lead | test-bench writer (Opus high) | reviewer set, qa-lead QA1-3, architect AR1-3 | yes | done (validated: QA ref 14/14, 11/11, 13/13; traps fail; RV 10 bugs + 3 clean; AR rubric calibrated 6/6) | 1 | eng-sandbox/tasks, eng-evals-hidden | 2026-10-21 |
| J010-T14 | lead | performance scenario builder (Opus high, Studio) | PE1-3 + capture recipe + before numbers | yes | working | 1 | eng-sandbox/tasks, eng-evals-hidden | 2026-10-21 |
| J010-T15 | lead | architect NEW (Opus high) | AR1-AR3 eval run (eval-runbook.md) | yes | done (246k tokens, 19 min) | 1 | eng-sandbox/runs/AR*/new/plan.md | 2026-10-21 |
| J010-T16 | lead | architect OLD (Opus medium, DS HEAD) | AR1-AR3 eval run | yes | done (196k tokens, 12 min) | 1 | eng-sandbox/runs/AR*/old/plan.md | 2026-10-21 |
| J010-T17 | lead | grader (Sonnet high) | AR rubric, blind to arm (labels P/Q, map.json hidden, source names scrubbed) | yes | done (181k tokens; scores-architect.md) | 1 | eng-evals-hidden/AR/scores | 2026-10-21 |
| J010-T18 | lead | feature-builder NEW (Opus high) | FB1-FB3 eval run, plan C | yes | done (first hand-in: 18/18, 18/18, 22/22; 309k tokens, 50 min) | 1 | eng-sandbox/runs/FB*/new | 2026-10-21 |
| J010-T19 | lead | feature-builder OLD (Opus high, DS HEAD) | FB1-FB3 eval run, plan C | yes | done (first hand-in: FB1 18/18, FB2 18/18, FB3 22/22; 225k tokens, 27 min) | 1 | eng-sandbox/runs/FB*/old | 2026-10-21 |
| J010-T20 | lead | reviewer NEW (Opus high) | RV eval run, plan C | yes | done (3 approve, 10 request-changes; 145k tokens, 7 min) | 1 | eng-sandbox/runs/RV/new/review.md | 2026-10-21 |
| J010-T21 | lead | reviewer OLD (Opus high, DS HEAD) | RV eval run, plan C | yes | done (4 approve, 9 request-changes; 139k tokens, 7 min) | 1 | eng-sandbox/runs/RV/old/review.md | 2026-10-21 |
| J010-T22 | lead | quick-builder NEW (Opus medium) | QB1-QB3 eval run, plan C (no old arm) | yes | done (QB1 10/10, QB2 10/10, QB3 pre-checks 6/6 + rubric grade; 146k tokens, 6 min) | 1 | eng-sandbox/runs/QB*/new | 2026-10-21 |
| J010-T23 | lead | grader (Sonnet high) | RV rubric, blind P/Q | yes | done | 1 | eng-evals-hidden/RV/scores.md | 2026-10-21 |
| J010-T24 | lead | grader (Sonnet high) | QB3 rubric | yes | done (PASS: 6/6 must-pass, 0 fail items, 9/9 citations) | 1 | eng-evals-hidden/QB3/scores.md | 2026-10-21 |
| J010-T25 | lead | qa-lead NEW (Opus medium) | QA1-QA3 eval run, plan C (no old arm) | yes | done (hidden 14/14, 11/11, 13/13; 301k tokens, 38 min) | 1 | eng-sandbox/runs/QA*/new | 2026-10-21 |
