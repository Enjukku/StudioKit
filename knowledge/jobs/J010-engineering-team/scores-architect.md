---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010-T15..T17 (blind grade eng-evals-hidden/AR/scores.md; labels P = new, Q = old in all three tasks, map.json)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Architect: new vs old (3 design tasks, blind Sonnet-high grader)

Tasks rebuilt from past rework: AR1 falling pieces (study A07), AR2 rubble removal (B01), AR3 machines without touching ordinary structures (L03, C24). One run per arm; no Studio (Studio was busy; both arms were told to plan probes instead). Hidden by instruction, not enforced.

| | New (kit, Opus high) | Old (DestructionSimulator HEAD, Opus medium) |
| --- | --- | --- |
| Traps avoided | 11 / 11 | 11 / 11 |
| Must-haves present | 14.5 / 15 | 14.5 / 15 |
| Over-built | no, no, no | no, no, no |
| Code size planned (AR1 / AR2 / AR3, lines) | 65-125 / 165 / 150 | 200 / 195 / 310 (reference 200 / 150-220 / 230-360) |
| Plan length (lines of plan) | 230 / 243 / 226 | 104 / 102 / 99 |
| Owner questions (total / real design / misrouted) | 16 / 14 / 2 | 15 / 15 / 0 |
| Rubric pass mark | 1 of 3 (AR1 fail, AR3 fail, each on one misrouted question) | 3 of 3 |
| Tokens / minutes | 246k / 19 | 196k / 12 |

Misses, per the grader:
- New AR1: sent a technical budget (a 30 FPS phone floor) to the owner as a question.
- New AR2: "remove only resting pieces" brings back per-piece motion state; the scan of a few hundred oldest entries could stall.
- New AR3: asked the owner a question an owner decision already answered ("nothing is left floating"); 7 questions.
- Old AR3: isolation test proves results and timing but has no call-spy proof that machine code runs 0 times for ordinary structures.

Reading: equal on design substance; the new plans are smaller in code but twice as long on paper and route two technical choices to the owner. Gap to fix in the role file: only real design forks go to the owner; budgets and anything an owner decision answers are the architect's call; plans as short as the builder needs. Grading uncertainty: three pass marks hang on one question each (grader's note).

## After the scores (J010-D3)
Fixes applied, **not re-tested** (owner plan C): `architect.md` work-method step 1 (technical budgets are PROPOSAL values, not owner questions; only real design forks no owner decision covers) and hand-back length note; `engineering-craft` EC-16 (the same rule for every engineering role).
