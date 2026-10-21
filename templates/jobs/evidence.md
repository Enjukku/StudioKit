---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
---
> Author: <role> · <model id> · <effort> · <date>
<!-- Template: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016). The job's evidence ledger: written by the integrator and reviewers, checked by the lead at readiness, read by /improve. -->

# Evidence: <job-id>

## 1. Checks (per candidate revision)
A failed check stays visible until a passing run on a repaired revision supersedes it. Missing evidence is "not verified", never a pass.

| Candidate @rev | Check | Result | Evidence (file, log line, capture) | Label (gate / MCP / owner / not verified) | By | Date |
| --- | --- | --- | --- | --- | --- | --- |

## 2. Protected list (must stay passed)
| Since @rev | What | Check that proves it |
| --- | --- | --- |

## 3. Defects
Cause: context missed · context missing · brief gap · interface conflict · craft error · tool failure · review broke correct work · found by the owner after internal review · owner taste change.

| ID | Found @rev | By | Class (blocking / recommendation / new request) | Cause | Owner of the fix | Fixed @rev | Rechecked |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 4. Metrics at close
| Metric | Value |
| --- | --- |
| First-pass acceptance (gates passed with no change request) | |
| Repair rounds, by cause | |
| Defects the owner found after internal review | |
| Stale or lost hand-offs | |
| "Done" claims without evidence | |
| Usage: estimate vs actual (tokens) | |
| Owner decisions asked | |
| What more iteration would fix | |
