---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010-T25 (hidden runner: the agent's suites run against the correct module and planted-fault versions it never saw)
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# QA lead: new only (plan C, J010-D3: no old arm; the old game had no QA agent)

| Task (study row) | Hidden checks passed | What that covers |
| --- | --- | --- |
| QA1 one shared "nothing loose at load" check (C16, C25, C26) | 14 / 14 | correct module passes (no false failures); all hidden planted faults caught, including the real-scale one; layouts added after hand-in are checked with no test edit; strict types; tests do not copy the module |
| QA2 structure rules with long removal sequences (A05, A21) | 11 / 11 | includes the 2 faults only random removal sequences catch (a good hand-only suite misses them) |
| QA3 route network checks (R01) | 13 / 13 | includes faults only real plans reveal; plans added later are checked |
| Fix rounds | 0 | |
| Tokens / minutes | 301k / 38 (Opus medium) | |

The agent's own planted-fault checks: 28/28, 26/26, 29/29 (QA1 needed one internal repair: 2 of its own faults survived its first suite; it added 2 cases). Caveat: the tasks rebuild past traps that the `testing` book describes. Its note: the tests folder is visible to builders in a real project; protect it (testing T-06).
