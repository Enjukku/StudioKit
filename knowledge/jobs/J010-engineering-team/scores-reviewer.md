---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010-T20, T21, T23 (blind grade eng-evals-hidden/RV/scores.md; P = new, Q = old, map.json)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Reviewer: new vs old (13 changes: 10 planted bugs, 3 clean controls; blind Sonnet-high grader)

Planted bugs rebuilt from past rework (A12, A13, C06, B08, EG5, E1, E2) plus receipt-before-save, NaN validation and a connection leak. Both Opus high, offline, one run each. Hidden by instruction, not enforced.

| | New (kit) | Old (DestructionSimulator HEAD) |
| --- | --- | --- |
| Planted bugs found with proof | **10 / 10** | 9 / 10 (missed CH06) |
| Critical bugs found | 5 / 5 | 5 / 5 |
| High bugs found | 4 / 4 | 3 / 4 |
| Severity right | 10 / 10 | 9 / 9 |
| Verdicts right (approve / request changes) | 13 / 13 | 12 / 13 |
| False blockers on clean changes | 0 | 0 |
| Other false alarms | 0 | 0 |
| Extra real findings | 0 | 1 |
| Rubric pass mark | PASS | PASS |
| Tokens / minutes | 145k / 7 | 139k / 7 |

The old miss: CH06 reads the player's position at CharacterAdded, before Roblox places the character; a respawning player gets a false strike and is snapped back. The old review suspected it under "not checked" but approved the change. Caveat: this exact engine trap (study E1) is listed in the new kit's `engineering-craft` → `references/probes.md`, so the new reviewer had been taught it. Both reviewers caught every money, save and exploit bug and raised no false alarms.
