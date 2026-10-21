---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 follow-ups review
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-21

# Review: J016 follow-ups 4e48885 (base 97a7eeb), by reviewer

```text
<spec>
artifact: commit 4e48885 (git diff 97a7eeb 4e48885)
reviewer: reviewer
looked_at_first: [the diff of tools/context_packet.py, tools/eval_context.py, tools/workflows/wf_harness.mjs, .agents/workflows/jobs/*.js, tools/tests/test_job_workflows.py, tools/tests/test_context_tools.py; knowledge/jobs/active.md; rules/company.md §9 row "Studio drivers"]
findings:
  - {id: F1, class: recommendation, where: "tools/eval_context.py:161-173", expected: "a saved run written before 4e48885 (rows have no role/job keys) still pairs every case with its saved row", observed: "a saved row without role/job keys gets the key (task, None, None); every current case that has a role or job gets (task, role, job), so it never matches and prints 'new case'", evidence: "python tools/eval_context.py --compare <97a7eeb:knowledge/logs/improve/2026-10-21-retrieval.json> prints 'new case' for 14 of 33 cases (all with role or job); a per-case regression in those 14 is not shown. Severity low: RESULT (overall recall@10) is unaffected, and the only saved file in the repo was regenerated in this commit with role/job keys", smallest_fix: "when a saved row has no 'role' key, match it on task alone (old behaviour); or accept it and note that pre-4e48885 saved runs compare overall only"}
  - {id: F2, class: recommendation, where: "tools/context_packet.py:482 and :691", expected: "an open job listed in knowledge/jobs/active.md is never treated as closed", observed: "the closed check compares the folder name with the active.md id by exact match; tools/hooks/compact_context.py:109 resolves the same ids with resolve_job (unique prefix allowed), so a line '- J8 · ...' is valid for the hook but makes the open folder J8-open count as closed", evidence: "temp-root probe: active.md '- J8 · an open job', folder J8-open: rank(..., 'orchestrator') scores J8-open/reviews/chest.md 1.392 vs 2.81 with '- J8-open · ...' (x0.5 for the lead on an open job). Severity low: the file header and AGENTS.md define <job-id> as the folder name, and the real line in history was '- J016-orchestration · ...'", smallest_fix: "build self.active with resolve_job per id (skip ids that do not resolve), the same way the hook reads them"}
  - {id: F3, class: recommendation, where: "tools/workflows/wf_harness.mjs:109; tools/tests/test_job_workflows.py (no test)", expected: "a wording drift between studioRule() and the harness regex fails a test", observed: "no test proves the Studio regex matches any brief; if a workflow reverted to 'Studio writer', every Studio step would hold nothing and overlap checks would pass silently", evidence: "planted fault: job-ui-screen.js with studioWrite on B4-ui-effects (runs beside B2-implement) gives violation 'Studio held by two agents at once'; the same plant with 'Studio writer' wording gives violation ''. Pre-existing gap, not introduced here; the check works today", smallest_fix: "one test asserting that a planted parallel Studio step (or a scenario flag) yields the 'Studio held by two agents' violation"}
keep:
  - "Change 1: studioRule(false) forbids any Studio MCP use in all six Studio workflows; every step whose checks need a capture, play-test, probe or measurement in Studio is a studioWrite step (scan of every stage x size brief); review steps without Studio judge captures recorded by a driver step; no 'Studio writer' left in workflows or tools; wording matches rules/company.md §9 'Studio drivers (read or write)'"
  - "Change 1: harness regex matches the new wording (planted overlap caught)"
  - "Change 2: C3-code-owners runs at the end of contract(), after the needs rounds and merges; contract() precedes production() in M build and opens proof() for L, so B2-implement, B5, fixFindings code/chain and R3-integrate all cite an existing contract-code.md; proof-mode repairs return before any builder step; the call has agentType, model on its tier, effort, S_HANDBACK, intent/spec/checks (harness violation empty); the test asserts C3 exists and comes before B2 and that B2's brief cites contract-code.md"
  - "Change 3: keys (task, role, job), in-order pairing via pop(0); the new test fails on the 97a7eeb compare (spot-checked: '->' found, MRR 0.50 -> 1.00) and passes on 4e48885"
  - "Change 4: factor applied once (history or closed); open jobs keep full weight for orchestrator and doc-keeper; --job exempts the named job; ACTIVE_JOB_RE '^- (\\S+) · (.+)$' matches the documented and historical line format and skips the header prose; no active.md gives None (nothing closed); the test covers None, orchestrator, doc-keeper and the --job exception and fails without the fix (equal scores for role None)"
verdict: ready for the next review
</spec>
```

Tests: `python -m unittest tools.tests.test_job_workflows tools.tests.test_context_tools -v` → `Ran 100 tests in 15.069s` / `OK` (no skips; Node present).
