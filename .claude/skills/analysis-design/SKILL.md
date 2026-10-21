---
name: analysis-design
description: Read a Roblox game's own player data correctly and turn it into one decision a non-expert owner can act on - what changed, for which players, how sure we are, and one recommendation. Covers the metric contract, Roblox metric definitions (D1/D7/D30 cohorts, session time, payer conversion, ARPPU, performance tails, economy, funnels), peer benchmarks and why no "good D1" table exists, measurement breaks (2026-10-12), diagnosing why players leave or stall (symptom split, competing explanations, non-finishers, causal words), economy and purchase reading, player feedback as data, Roblox Experiments and update measurement (enough players and time, sample-ratio checks, early harm vs winners, five verdicts), and plain reporting. Use for "why did retention drop", "did the update help", "where do players quit", "is the economy broken", "is this test result real", "what should this feature log", "weekly numbers". Read by the analyst first; game designer, progression designer and marketing read it to use the analyst's numbers correctly.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J013 from the owner's analyst research paper (2026-10-21; VERIFIED / EXPERIENCE / OPINION tags kept) and three fact-checks (`knowledge/reference/analyst/01-roblox-platform-facts.md` RF ids, `02-statistics-experiments.md` ST ids, `03-practice-diagnosis-reporting.md` PR and C ids; read 2026-10-21). Tags: **V** documented fact · **E** someone's reported result, never a target · **O** the paper's or studio's practice. Logging code belongs to the `analytics` skill; this skill reads the data.

# Analysis design: read player data right, say it simply

## 1. When this skill starts
It answers five questions, in order:
1. **What decision is this for?** A number nobody will act on is not worth pulling.
2. **What exactly are we measuring?** The metric contract: what we counted, out of whom, which days, which players, which version of the rule (`references/metrics-roblox.md` §1).
3. **Can the data answer it yet?** Enough players, finished cohorts, no measurement break, the right design for the claim.
4. **What is the most likely explanation, and what else could it be?** Competing explanations, checked against evidence (`references/diagnosis.md`).
5. **What do we tell the owner?** One finding, the evidence, how sure, one recommendation (`references/reporting.md`).

The analyst owns the evidence. The owner decides; each specialist owns its fix (E, C26). How to pull data, calculate and write the files: `analysis-craft`.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The metric contract, Roblox metric definitions and API names, when numbers exist, benchmarks, what to watch first, measurement breaks | `references/metrics-roblox.md` |
| Why players leave or stall: symptom split, competing explanations, funnels, non-finishers, causal words, player voice, economy, purchases, fair monetization, the diagnosis checklist | `references/diagnosis.md` |
| A/B tests (Roblox Experiments), enough players and time, sample-ratio checks, early harm, verdicts, measuring updates and events | `references/experiments-updates.md` |
| The answer shape, how sure, plain words, routing, charts, integrity rules | `references/reporting.md` |
| How to do the work: tools, steps, templates, event specs, hand-offs | `analysis-craft` |
| Logging code, AnalyticsService limits, Configs for tests | `analytics` |
| Paid random items, younger players, player data | `platform-policy` |

## 3. Steps
1. **Frame.** Turn the question into outcome, players, window and decision; a different answer must change an action. *Check:* the metric contract is written.
2. **Inventory.** Which dashboards, API metrics, events and history exist; what the game is eligible for (10 DAU for dashboards, 100 for benchmarks and performance, ~1,000 for useful experiments). *Check:* no planned analysis depends on data that does not exist.
3. **Freeze and validate.** Pull, save, then check completeness, point status, maturity, breaks, impossible values, totals. *Check:* another analyst could rebuild the input from the files.
4. **Describe.** How big, how many players, how spread, how uncertain. *Check:* every rate has its counts and units.
5. **Localize.** Where in time, which segments, which step; did the player mix change? *Check:* segments add up to the total.
6. **Explain.** Competing explanations with predictions; seek evidence against each; add observed play or feedback from the affected players. *Check:* at least two explanations tested.
7. **Bound the claim.** Causal words match the design: experiment > strong comparison > before/after > story (`references/diagnosis.md` §5). *Check:* "inconclusive" and "invalid" were allowed answers.
8. **Report and learn.** One finding, evidence, how sure, one action with owner and review date; record the prediction and later the outcome, nulls included. *Check:* the owner can decide without decoding statistics.

## 4. Craft core (what separates a trustworthy analyst from a plausible one)
| ID | Practice | Evidence |
| --- | --- | --- |
| A-01 | **No number from writing.** Every number resolves to a saved pull or a `analytics.py stats` output; measured, calculated, estimated and opinion stay apart | O, AP:464 (PR-AI01) |
| A-02 | **Compare cohorts of equal, finished age.** D7 means a return on the 8th day counting first play as day 1; a cohort is readable only after its window passed. Never put an immature D7 next to a mature one | V RF-13..15; O AP:19 |
| A-03 | **Denominators everywhere.** Sum counts before ratios; never average daily percentages; summed DAU is player-days; peak CCU is not DAU | O, AP:55; V RF-12 |
| A-04 | **No invented benchmark.** Roblox shows a 50th-90th percentile band of similar games; no public "good D1 by genre and age" exists; the docs' example band and creator case uplifts are not targets | V RF-19..21, RF-59; O AP:110 |
| A-05 | **Mark measurement breaks.** 2026-10-12 discovery recording, event version changes, logging bugs; a pipeline change is not a behaviour change | V RF-55..57 |
| A-06 | **Where is not why.** A funnel locates the loss; the reason needs competing explanations, observed play or a test | O, AP:24, 153 |
| A-07 | **Count the non-finishers.** Time-to-milestone among finishers only makes a hard step look easy; use a fixed window and the share who reached it | O, AP:171; S8 |
| A-08 | **Mix before blame.** A rate can fall because different players arrived; check source and new/returning mix, show retained counts next to rates | O, AP:136, 503 |
| A-09 | **Read tails by device.** P10 FPS and P90 memory by device and version; an average improves when weak phones leave; keep our own history (Roblox keeps 28 days) | V RF-11, RF-33..36 |
| A-10 | **Plan the test before it starts.** One primary outcome, smallest worthwhile effect in absolute units, guardrails with harm margins, players and days needed, decision date; Roblox's MDE at setup decides if the game can answer it | O, AP:247; V RF-41 |
| A-11 | **Enough players and time, or no verdict.** 14-60 days, whole weeks, outcomes matured; sample-ratio check passes; a fixed end date, no early winners; early harm detection only stops tests | V RF-40..48; ST (`references/experiments-updates.md`) |
| A-12 | **Five verdicts, honestly.** Useful improvement · Harmful · Inconclusive · No worthwhile effect · Invalid. Significance alone is not size, importance or truth | O, AP:281; V S5 |
| A-13 | **Compare all eligible players.** Never buyers-only, finishers-only or event-joiners vs non-joiners: the change can change who is in the group | O, AP:218, 626 |
| A-14 | **People, not comments.** Theme rate = contributors who raised it ÷ contributors heard from; filtered sources stay labelled; silence is not approval | O, AP:356 |
| A-15 | **One finding, one recommendation.** "How sure" in High / Medium / Low with reasons, never a made-up percentage; when the cause is unknown, say so | O, AP:414-416 (owner J013) |

## 5. Rules (final check, short)
- No number without its source file; no rate without counts; no unit missing.
- **Part 1 (the owner's part) never holds a hypothetical, example or made-up number, even labelled.** Explain a mechanism in words; worked examples go to Part 2, marked hypothetical.
- No benchmark, threshold, "good value", player count or test length that is not documented or computed for this game.
- No "caused" without a valid experiment or a strong causal design; no winner from early, harm-screen or exploratory data.
- No D7/D30 from an immature cohort; no comparison across a measurement break without a note.
- Paid random items, younger players and player data follow `platform-policy`; fairness is a constraint, never a test variable.
- Player data stays aggregate; no personal identifiers in any file; the API key never appears anywhere (`analysis-craft`).
- The analyst recommends; the owner decides; specialists choose their fixes.

## 6. Self-check before returning
- [ ] The metric contract is written for every number in the answer.
- [ ] Cohorts mature, breaks marked, point status (`Projected`, `NotStatisticallySignificant`) shown.
- [ ] At least two explanations checked; causal words match the design.
- [ ] The answer has one finding, evidence with counts, how sure with reasons, one recommendation with owner and review date.
- [ ] Every number traces to a pull or a `analytics.py stats` output.
- [ ] Part 1 has no number that is not from a pull, the owner's question, or shown arithmetic on those two (no example counts, no "with 100 players…"); say "few" or "many" instead.

Project overlay: if `knowledge/overlays/analysis-design.md` exists, read it after this file; it wins for this game.
