---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016
supersedes: []
---
> Author: doc-keeper · claude-haiku-5-5 · medium · 2026-10-21 (facts from the lead)

# Evidence: J016-orchestration

## 1. Checks (per candidate revision)
A failed check stays visible until a passing run on a repaired revision supersedes it. Missing evidence is "not verified", never a pass.

| Candidate @rev | Check | Result | Evidence (file, log line, capture) | Label (gate / MCP / owner / not verified) | By | Date |
| --- | --- | --- | --- | --- | --- | --- |
| 322c8ad | gate (python tools/verify.py) | PASS, 585 tests | commit message | gate-verified | lead | 2026-10-21 |
| 763a11e | gate | PASS, 635 tests | commit message | gate-verified | lead | 2026-10-21 |
| d2d0601 | gate | PASS, 641 tests | commit message | gate-verified | lead | 2026-10-21 |
| 93b59b2 | gate | PASS, 641 tests | commit message | gate-verified | lead | 2026-10-21 |
| eb3c740 | gate | PASS, 641 tests | commit message | gate-verified | lead | 2026-10-21 |
| 322c8ad-763a11e | mechanics rehearsal R1-R6 on Haiku | 5 of 6 pass; R2a fail (roles without SendMessage) | pilot-plan.md §2 | live probe | lead | 2026-10-21 |
| eb3c740 | message tool and image browser after a restart (C22, C24) | pass | knowledge/reference/studio/claude-code-capabilities.md C22, C24 | live probe | lead | 2026-10-21 |
| all | real job run of any job workflow | not run | owner J016-D8, J016-D9 | not verified | — | 2026-10-21 |

## 2. Protected list (must stay passed)
| Since @rev | What | Check that proves it |
| --- | --- | --- |
| 93b59b2 | all 641 gate tests | python tools/verify.py |
| 93b59b2 | retrieval: 16 of the original 19 cases (cases 1, 10, 16 fail as before J016) | python tools/eval_context.py --compare knowledge/logs/improve/2026-10-21-retrieval.json |

## 3. Defects
Cause (the list in `rules/knowledge.md` §8, word for word): context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · defect found by the owner after internal review · owner taste change.

| ID | Found @rev | By | Class (blocking / recommendation / new request) | Cause | Owner of the fix | Fixed @rev | Rechecked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1-A5 audit | 322c8ad | auditors A-E | blocking ×57 (A 8, B 16, C 13, D 7, E 13) | mixed: interface conflict, brief gap, context missing, craft error (see reviews/*-322c8ad-*.md) | fixers W1-W4 | 763a11e | yes, by the same auditors (reviews/*-763a11e-*.md) |
| recheck new | 763a11e | auditors A-E | blocking ×6 (from the fixes) | interface conflict | W2, W3, lead | d2d0601 | yes, rechecker A6 (reviews/repair-round-1-d2d0601-rechecker.md) |
| RC-N1 | d2d0601 | rechecker A6 | blocking ×1 (M feature build went on with pending images) | craft error | lead | 93b59b2 | harness test (old script done after 24 agents, new blocked after 8) |
| R2a | 322c8ad | rehearsal | blocking (14 roles could not send messages) | context missing | owner J016-D6 | fe6a048 | live probe after restart (eb3c740) |

## 4. Metrics at close
| Metric | Value |
| --- | --- |
| First-pass acceptance (gates passed with no change request) | 3 of 3 owner gates passed with no change request (G1 J016-D4, G2 J016-D5, G3 J016-D9) |
| Repair rounds, by cause | internal only: 1 fix round (4 makers) + 1 repair round (2 makers) + 1 lead seam fix; causes in knowledge/inbox/2026-10-21-J016-G3-orchestrator.md rows 2-10 |
| Defects the owner found after internal review | 0 (no real job has run yet) |
| Stale or lost hand-offs | 0 found; 1 rehearsal hand-off blocked (sound-designer had no SendMessage) |
| "Done" claims without evidence | none found in the rechecks |
| Usage: estimate vs actual (tokens) | estimate steps 1-7 about 3.5-4.5 M; actual steps 1-8 about 5.3 M; G3 audit, fixes and rechecks about 7.7 M; close probes about 0.2 M; total about 13.2 M |
| Owner decisions asked | 9 (J016-D1..D9) |
| What more iteration would fix | run the first real jobs of every type through the lead (J016-D10) and file their results; the open follow-ups in the job card |
