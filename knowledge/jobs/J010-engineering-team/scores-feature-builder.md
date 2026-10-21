---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010-T18, T19; hidden runner eng-evals-hidden/run.py (no lead access to tests)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Feature-builder: new vs old (3 hidden-test tasks, Opus high both)

FB1 ability remote with cooldown (study A12), FB2 per-player coin piles (A13, C06), FB3 saves + migration + session lock + receipts (new task). One run per arm, offline Luau (no Studio). Hidden by instruction, not enforced.

| | New (kit) | Old (DestructionSimulator HEAD) |
| --- | --- | --- |
| Hidden tests passed, first hand-in | 58 / 58 (18, 18, 22) | 58 / 58 (18, 18, 22) |
| Fix rounds needed | 0 | 0 |
| Product code written (non-comment lines; FB1 / FB2 / FB3) | 110 / 173 / 270 = 553 | 121 / 167 / 321 = 609 |
| Own tests written (lines) | 1,546 | 1,353 |
| Own planted-fault checks reported | 36 faults, 33 caught | 6 faults, 6 caught |
| Tokens / minutes | 309k / 50 | 225k / 27 |

Reading: no difference in correctness on these tasks; both passed every hidden check first time, including the real past traps. The new builder wrote about 9 % less product code and tested its own tests far more; it used 37 % more tokens and almost twice the time. The tasks did not separate the two arms (ceiling): a harder or larger task would be needed to show a quality difference.
