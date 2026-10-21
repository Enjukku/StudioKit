---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J011
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Lessons: building the progression-designer agent (J011)

## What worked
- Starting tools first (Opus) in wave 1, in parallel with the paper extractors, put the longest task on the critical path early; the lead had already read the math sections and could brief exact fixtures by line.
- Briefing the tool builder with the paper's exact fixture values (Fraction equality) made "the formulas from the paper" testable: 2,550 bulk-buy equalities, the Lemonade waits, the M04 tables and the breakpoint example all pass in both the curve library and the simulator.
- Running the new agent on the worked examples as its first real task tested skills and tools together: it found 15 precise gaps with file:line, including a crash bug, and the tools were fixed in one batch (T11) before the owner saw anything.
- Fact-checkers found real errors in the paper: the TFT XP values sum to 268, not the 228 → 288 totals (earlier levels carry the rest); 7.87 is the source's simplified-base example, not the cost at 10 owned; Hearthstone changed total AND spacing; six restricted-player treatments, not four.
- Hidden evals as new symptoms (not the paper's own cases) tested application, not recall.

## What failed or cost time
- The planned hidden cases were cases the paper teaches, so they ended up in the skills; pick hidden cases after deciding what the skills will contain.
- A separate grader running while the tool builder changed the tools saw stale example runs (0 of 18 byte-identical); sequence graders after tool changes, or pin the tool version in the brief.
- Continuous exact simulation with exponential prices made huge reports (17 MB for 18 minutes); size, not speed, is the limit; a lean mode was needed.

## Owner corrections
None yet (G2 pending).
