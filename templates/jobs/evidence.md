---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
---
> Author: <role> · <model id> · <effort> · <date>
<!-- Template: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); cause list aligned with rules/knowledge.md §8 by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3. The job's evidence ledger: written by the integrator and reviewers, checked by the lead at readiness, read by /improve.; revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021: belief check, BAR line, target-experience sentence); revised by orchestrator-writer · claude-opus-5-5 · default · 2026-10-24 (J023: came-back-right row for the loosening rule); revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design: no G2) -->

# Evidence: <job-id>

## 1. Checks (per candidate revision)
A failed check stays visible until a passing run on a repaired revision supersedes it. Missing evidence is "not verified", never a pass.

| Candidate @rev | Check | Result | Evidence (file, log line, capture) | Label (gate / MCP / owner / not verified) | By | Date |
| --- | --- | --- | --- | --- | --- | --- |

## 2. Protected list (must stay passed)
| Since @rev | What | Check that proves it |
| --- | --- | --- |

## 3. Defects
Cause (the list in `rules/knowledge.md` §8, word for word): context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · defect found by the owner after internal review · owner taste change.

| ID | Found @rev | By | Class (blocking / recommendation / new request) | Cause | Owner of the fix | Fixed @rev | Rechecked |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 4. Metrics at close
| Metric | Value |
| --- | --- |
| First-pass acceptance (gates passed with no change request) | |
| Came back right, per gate, for the loosening rule (`rules/company.md` §2): job type; G1 yes / no · G3 yes / no (no G2 since J024) (yes = the owner accepted the first packet with no change request) | |
| Repair rounds, by cause | |
| Defects the owner found after internal review | |
| Stale or lost hand-offs | |
| "Done" claims without evidence | |
| Usage: estimate vs actual (tokens) | |
| Owner decisions asked | |
| What more iteration would fix | |
| Hand-backs by `BAR` line: bar met / floor only (reasons) / no `BAR` row (J021) | |
| `proposals` raised / taken by the lead or owner (J021) | |
