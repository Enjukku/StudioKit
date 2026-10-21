---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J013; owner's analyst paper Appendix C (knowledge/reference/analyst/02-statistics-experiments.md §5 verdict rules)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# A/B test result: <test name> · <test id>

Workflow: `analysis-craft` §3 (experiments). Copy to `knowledge/jobs/<job>/analyst/tests/<test-id>-result.md`. Plan: `<test-id>-plan.md`. Write the result only after the planned outcome end date, or for an operational stop (then the verdict is "stopped", not a win).

## Part 1 — For the owner

| | |
| --- | --- |
| **Verdict** | <one of the 6 below> |
| **In plain words** | <the verdict sentence from the table, filled in> |
| **What we recommend** | <one action> · who · for which players · check again on <date> |
| **What we still do not know** | <the range of effects the data still allows; longer-term effects; players not tested> |

Check the rows in order; the first one that is true is the verdict (`analysis-design/references/experiments-updates.md` §6; `tools/analytics` `analytics.py stats verdict`). "Likely range" = the interval [L, U] of the primary effect, higher = better; b = smallest worthwhile effect; h = harm margin.

| # | Verdict | When it applies | Sentence for the owner |
| --- | --- | --- | --- |
| 0 | **No verdict yet** | the outcome window has not finished | "Too early: the players in this test have not had <N> days yet. We read it on <date>." |
| 1 | **Invalid** | uneven split (sample-ratio check failed), broken assignment, logging failure, contamination, or stopped early on ordinary p-values | "The test setup failed, so it cannot tell us if the change helped. Fix <problem> first." |
| 2 | **Harmful** | U ≤ −h, or a guardrail beyond its harm margin, or a confirmed severe problem | "This version hurt <outcome>. Keep or go back to the current version." |
| 3 | **Useful improvement** | L > 0 and the middle estimate ≥ b, and no guardrail can be beyond its margin (strict option: L ≥ b; rule = PROPOSAL until the owner decides) | "The test supports <benefit> for <players>. We recommend <action>, and we will keep watching <guardrail>." |
| 4 | **No worthwhile effect** | U < b and L > −h | "Any gain is too small to be worth it. Do not do this change for this reason." |
| 5 | **Inconclusive** | anything else; name why: gain unproven, harm not ruled out, or a guardrail not cleared | "We do not know yet whether this helped. Keep the current version while we <one next action>." |

## Part 2 — Evidence

| Outcome | Control | Treatment | Absolute difference (units) | Relative difference | Likely range (level, method) | Players per arm | Role |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Primary | | | | or "not meaningful" | | | decides (smallest worthwhile: <x>) |
| Guardrail | | | | | | | harm margin: <x> |
| Diagnostic | | | | | exploratory | | explanation only |

| Check | Result |
| --- | --- |
| Source of the numbers | Roblox Experiments results (pull id) and/or `analytics.py stats` output file; every number traces to one |
| Sample-ratio check | expected split, observed counts, p value (`analytics.py stats srm`); fail → verdict Invalid |
| Timing | enrollment window, outcome window, cohorts finished, real duration vs plan |
| Exposure and logging | arms had the same chance to log; incidents |
| Deviations from the plan | what changed, when, why, effect on the reading |
| Population | who was eligible; what this does not apply to |
| Guardrail conclusion | harm ruled out within its margin / not ruled out (say so even if revenue rose) |
| Mechanism evidence | diagnostics and observed play that support or contradict the why |
| Exploratory splits | labelled exploratory; confirm in a new test before acting |
| Early Harm Detection | flagged / not flagged; with fewer than 10,000 enrolled across the compared arms it cannot flag, so "not flagged" means "not checked" |
| Files | plan, pulls, stats outputs |
