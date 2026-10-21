---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J013; owner's analyst paper Appendix B (knowledge/reference/analyst/02-statistics-experiments.md, 03-practice-diagnosis-reporting.md); Roblox Experiments docs (knowledge/reference/analyst/01-roblox-platform-facts.md)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# A/B test plan: <test name> · <test id>

Workflow: `analysis-craft` §3 (experiments). Copy to `knowledge/jobs/<job>/analyst/tests/<test-id>-plan.md`. **Fill every field before any player sees the change.** "Not available" is a valid answer, but it may block a launch decision: say which. After the start, this file is frozen; changes go in "Deviations" of the result file.

## Part 1 — For the owner

| | |
| --- | --- |
| **What we change** | <plain sentence> |
| **Why** | <the problem we saw, with its evidence> |
| **What counts as success** | <one measure, in plain words, and the smallest gain worth shipping> |
| **What must not get worse** | <guardrails in plain words> |
| **How many players and days we need** | <N per group, about <days> days, plus <days> for results to finish> · from `analytics.py stats samplesize` |
| **Can this game answer it?** | <yes / only for a big change / no: why, and what we do instead> |
| **When we decide** | <date> |
| **Owner actions** | <create the experiment in Creator Hub with these settings; nothing else> |

## Part 2 — Full plan

| Field | Value |
| --- | --- |
| Decision owner and collaborators | |
| Problem and its evidence | source pull / query, population, dates, counts |
| Hypothesis and mechanism | <change> will improve <outcome> because <mechanism we can check> |
| Decision to make | ship / revise / reject; for which players |
| Control | current experience, config key and value, place version |
| Treatment(s) | exact difference; everything else the same. Roblox: up to 2 variants + control; recommended 1 variant 50/50 |
| Eligibility | before-treatment rules; new or all players; devices; places |
| Randomization unit | player / other (justify; shared worlds, trading, parties: say what spills over) |
| Allocation and rollout | tool setting; proportions |
| Persistence and exposure | what a player sees on later sessions; what happens if eligibility lapses (Roblox keeps the player in the arm) |
| Spillover check | trading, parties, combat, chat, shared rewards |
| Primary outcome (one) | metric name as Roblox labels it, numerator, denominator, window, unit |
| Smallest worthwhile effect | in absolute units (percentage points or minutes), with the reason |
| Guardrails and harm margins | each guardrail, the loss we will not accept |
| Diagnostics | explanation only, never the decision |
| Baseline | period, eligible population, rate or mean, spread, unique players |
| Power plan | method, α, power, MDE, allocation, players per arm (stats helper output pasted as a file path) |
| Roblox MDE shown at setup | value and date; if larger than the smallest worthwhile effect: change the question, run longer within limits, or do not test |
| Traffic forecast | unique eligible players per day (not DAU × days) |
| Enrollment start / end (UTC) | |
| Outcome end (UTC) | enrollment end + the longest outcome window (D7 needs 7 more days) |
| Decision date | |
| Duration reason | Roblox 14-60 days; whole weeks; learning or economy cycle; outcome maturity |
| Other changes and tests running | overlap policy; events; marketing |
| Logging check before start | assignment, eligibility, exposure, outcomes, version |
| Integrity checks | sample-ratio check (`analytics.py stats srm`); logging parity; join rates |
| Analysis | all assigned players (intention to treat); estimator; interval; multiple comparisons; missing data |
| Planned segment checks | before-treatment dimensions only; others are exploratory |
| Operational stop rules | severe bug, service harm, policy defect; who stops it. An Early Harm Detection flag stops a test; no flag does not mean safe, and never picks a winner |
| Statistical stop rule | fixed end date (no peeking decisions) |
| Decision rule | the verdict table in `ab-test-result.md`, filled in here with this test's numbers |
| After rollout | longer check, holdout if possible, review date |
| Saved files | this plan, pull ids, stats outputs |
