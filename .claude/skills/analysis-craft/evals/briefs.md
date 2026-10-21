# Eval briefs: analyst (analysis-design + analysis-craft)

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Built in J013. Run each brief with the `analyst` role in a fresh context (Sonnet medium unless the brief says Opus high). All numbers below are **synthetic TEST data**, not a real game: the agent must not present them as real. A separate grader (Sonnet, high) scores the must-pass checks from the files, not the hand-back. Hidden cases live in `knowledge/jobs/J013-analyst/evals-hidden.md` and go only to the grader.

## E1 — "Why did retention drop?" (deep investigation, Opus high)
Brief: TEST pull for universe 0 (put these rows in a file the agent reads): new players per week 4,300 / 4,280 / 6,900 (week 3 after a creator video on day 15); D1 by first-play week: 20.2% / 20.0% / 15.1%; D1 by source in week 3: Home recommendations 19.8% (n 2,950), Other (outside links) 11.2% (n 3,500), Search 20.5% (n 450); phone share of new players 58% / 59% / 74%; place version 112 went live on day 16; P10 client FPS on phones 31 / 31 / 30; crash rate unchanged. Ask: why did retention drop, and what should we do?
| ID | Must pass |
| --- | --- |
| E1-1 | Metric contract written; D1 cohorts labelled mature; counts next to rates; retained count stated (week 3 retained more players in total) |
| E1-2 | Finds the mix change (outside-link players) before blaming the game; shows within-source D1 is stable for Home and Search |
| E1-3 | Competing-explanations table with at least 3 rows (source mix, version 112, device/performance), each with evidence for and against |
| E1-4 | Every computed number (weighted D1, retained counts, differences) comes from `tools/analytics/analytics.py stats` or shown arithmetic; none typed from nowhere |
| E1-5 | Causal words: "linked to" / "consistent with", not "caused"; how sure = Medium or Low with reasons |
| E1-6 | One recommendation with owner (marketing for the source; or game designer for first session of outside-link players), measure and review date; marketing hand-off brief in `handoffs.md` §3 format |

## E2 — "Is this test result real? Can we ship?"
Brief: Roblox Experiments, in-game test of a new shop layout, 50/50, planned 21 days with primary outcome payer conversion and smallest worthwhile effect +0.3 points. Day 9 dashboard: variant payer conversion 2.9% vs control 2.5%, "statistically significant"; enrolled 18,040 control vs 17,120 variant; Early Harm Detection: no flag. Ask: can we ship now?
| ID | Must pass |
| --- | --- |
| E2-1 | Runs the sample-ratio check with `analytics.py stats srm` on 18,040 vs 17,120 against 50/50 and reports the result (expected: fails the p < 0.0005 alarm → Invalid until diagnosed) |
| E2-2 | Says day 9 of 21 is before the planned end: no early winner even without the SRM problem |
| E2-3 | Says no EHD flag is not safety and EHD never picks winners (only playtime, ARPU, payer conversion; 24 h) |
| E2-4 | Verdict = Invalid (owner sentence from the template); recommends diagnosing the split with engineering, not reweighting |
| E2-5 | Uses `templates/analytics/ab-test-result.md`; Part 1 in plain words |

## E3 — Plan an A/B test for a small game
Brief: game with about 600 DAU, ~180 new players a day. The game designer wants to test a shorter tutorial; they hope for +2 points D1 (baseline D1 18%). Ask: write the test plan.
| ID | Must pass |
| --- | --- |
| E3-1 | `analytics.py stats samplesize` run for two proportions (18% → 20%, α 0.05, power 0.8) with inputs shown; players per arm and days of enrollment from unique new players per day (not DAU × days) |
| E3-2 | Compares with Roblox's 14-60 day limit and says the MDE shown at setup decides; states honestly if the game cannot detect +2 points in 60 days |
| E3-3 | Offers the paper's alternatives when underpowered: test a bigger change, fix observed severe problems directly, playtest, or accept a descriptive before/after labelled as such |
| E3-4 | Plan template fully filled before exposure: one primary outcome, smallest worthwhile effect in points, guardrails with margins, fixed end date, outcome end = enrollment end + 1 day for D1 |
| E3-5 | Owner actions listed (create the experiment in Creator Hub); nothing changed by the agent |

## E4 — What should a new feature log?
Brief: the game adds a crafting bench: players combine 3 materials into gear; crafting costs coins; the designer's question is "do players understand crafting, and is it too expensive?". Ask: the measurement spec and the engineering brief.
| ID | Must pass |
| --- | --- |
| E4-1 | Starts from the decision and at least 2 competing explanations (unclear vs unaffordable vs not wanted) |
| E4-2 | Separates saw / chose / result (incl. server-decided failure with reason: not enough coins, missing material) / delivered |
| E4-3 | Each event has the 16 contract fields; properties ranked, max 3 custom fields, bucketed |
| E4-4 | Economy events for coin spend with sink naming; no per-click or client-side logging; no typed text |
| E4-5 | Engineering brief in `handoffs.md` §5 format with the acceptance walk (success, cancel, retry, interruption, returning player); no Luau written by the analyst |

## E5 — Weekly page
Brief: TEST weekly pull (provided as a file): DAU, new users, D1 for last week's cohorts, D7 including the cohort that started 3 days ago, session length, payer conversion, ARPPU, P10 FPS by platform, last pull 25 days ago, the window crosses 2026-10-12, one funnel with an 18% drop at step 4 of 9 and a 4% drop at step 2 affecting more players. Ask: the weekly page.
| ID | Must pass |
| --- | --- |
| E5-1 | Uses `templates/analytics/weekly-report.md`; Part 1 has exactly one finding, one recommendation, how sure with reasons, decision or "none" |
| E5-2 | The 3-day-old D7 cohort is shown as not mature, never as a number |
| E5-3 | Warns the last pull is older than 21 days (performance history gap risk) |
| E5-4 | Marks 2026-10-12 for discovery numbers |
| E5-5 | Ranks the funnel problem by players affected, not by percentage drop |
| E5-6 | Routing table filled; a brief to each role that must act (live-ops-designer via `handoffs.md` §4) |
