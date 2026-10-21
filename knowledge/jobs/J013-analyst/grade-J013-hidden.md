---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J013-T06b
supersedes: []
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J013 hidden-set grade (analyst, q1..q5 vs H1..H5)

Scored from the files only: `knowledge/jobs/J013-analyst/analyst/hidden-run/q1.md..q5.md` and `calc/*.json`, against `evals-hidden.md`. Whole points only. A point is given only for what is visible in the file. Pass bar: 8 of 10 and no rule break (lead, J013).

## Summary

| Case | File | Score | Bar 8/10 | Rule break | Result |
| --- | --- | --- | --- | --- | --- |
| H1 D1 benchmark | q1.md | 8/10 | met (exactly) | none | PASS |
| H2 Early Harm Detection | q2.md | 9/10 | met | none | PASS |
| H3 Events double retention | q3.md | 9/10 | met | none | PASS |
| H4 ARPPU +30% | q4.md | 8/10 | met (exactly) | none found; 1 rule question (RQ-1) | PASS, conditional on RQ-1 |
| H5 D7 crash | q5.md | 9/10 | met | none | PASS |

Extra checks (all five files): Part 1 has one finding, "How sure" with reasons, one recommendation: yes (q1.md:7-17, q2.md:7-18, q3.md:7-16, q4.md:7-18, q5.md:7-17). No number without a source or shown arithmetic: yes, except two small items listed under "Number checks". Invented or example numbers: only in q4 (RQ-1).

## H1 - q1.md: "Simulators average 25% D1; ours is 17%"

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| No public genre average; a forum number is not a benchmark; does not accept or invent one | 3 | 3 | q1.md:7 "forum claim ... not a Roblox benchmark"; q1.md:12 "no public 'good D1' for a genre"; no invented figure anywhere |
| Points to the game's own peer band (50th-90th percentile, read date, pool) and own trend | 3 | 2 | Band named q1.md:12; own trend asked q1.md:17 "last 4 weeks of D1 with new-player counts". Withheld 1: read date and pool are not named or requested. The skill requires them (`metrics-roblox.md:54`) |
| Asks what decision this serves; suggests D1 diagnosis path (first session, source mix) | 2 | 1 | Diagnosis path given: q1.md:23 "D1 by source, D1 by device, first-session funnel". Withheld 1: no question about what decision the owner is making (Part 1 only says "Do not change the game", q1.md:17) |
| Plain words, no jargon | 2 | 2 | Part 1 uses plain words; "percentile" is tied to "similar games" (q1.md:12). Jargon (cohort, metric contract) stays in Part 2 (q1.md:21) |
| **Total** | 10 | **8** | |

## H2 - q2.md: "24 h, 3,000 players, Early Harm Detection clean: ship?"

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| Under 10,000 enrolled, EHD makes no call; silence means "not checked" | 3 | 3 | q2.md:7 "means 'not enough data to say'"; q2.md:11 "flags nothing until 10,000 or more ... We have 3,000" |
| EHD watches only playtime, ARPU, payer conversion; D1/D7 not checked | 2 | 2 | q2.md:12 "only playtime, ARPU and payer conversion ... does not watch retention, and onboarding is about retention" |
| EHD is for stopping, never for launch; 14-day minimum; D7 maturity | 3 | 2 | 14 days: q2.md:13, q2.md:18. D7 maturity: q2.md:14, calc `q2-maturity-1020-d7.json` (readable 2026-10-29). Stop-only use: implied at q2.md:18 "Stop it only if EHD or a sample-ratio alarm fires" and q2.md:7 "not safe". Withheld 1: the file never states that EHD is not a launch signal |
| Verdict: not readable yet; one recommendation (keep running to planned end) | 2 | 2 | q2.md:7 "Do not ship yet"; q2.md:24 "Verdict today: Inconclusive"; q2.md:18 "Keep the test running to its planned end date" |
| **Total** | 10 | **9** | |

## H3 - q3.md: "Joiners returned on D7 twice as often; run an event every weekend"

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| Names self-selection: joiners were already more engaged; not causal | 4 | 4 | q3.md:7 "players who choose to join ... already like the game"; q3.md:11 "compares keen players with all the others"; q3.md:19 "a story, not a comparison" |
| Right comparison: eligible players before vs during, displacement, return after the event; or a holdout | 3 | 3 | q3.md:16 Option A random holdout; Option B all eligible players, event vs non-event weekends; "Never compare joiners with non-joiners". The rubric accepts "or a holdout". Displacement and return-after-event are not named. No points lost because the holdout alone meets the row |
| Routes to the live-ops designer; no weekly-event recommendation | 3 | 2 | No weekly events: q3.md:16 "Do not commit to weekly events on this evidence" (given). Routing: q3.md:16 "live-ops is a planned role, so the lead holds the ticket" (not given). That is wrong: `.agents/roles/live-ops-designer.md` exists, and `analysis-craft/references/handoffs.md:5` says it exists since J014. The agent was misled by stale text, see Gap 1 |
| **Total** | 10 | **9** | |

Bonus not scored: q3.md:11 sees that D7 for a weekend cohort is probably not mature. Small error: q3.md:11 gives 2026-10-26 for both event days, but the 2026-10-18 cohort is readable from 2026-10-27 (same rule as `calc/q5-maturity-1017-d7.json`).

## H4 - q4.md: "ARPPU up 30% after the price rise: great result?"

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| Asks for payer count, payer conversion, ARPDAU; ARPPU rises when small spenders stop buying | 4 | 4 | q4.md:7 "goes up after a price rise almost by design"; q4.md:10 "if the higher price makes some players stop paying, ARPPU can go up while total revenue goes down"; ask q4.md:18 "payer conversion, ARPU and total revenue, with player counts". Note: it says ARPU over a window (q4.md:21), not ARPDAU. Same intent, so no deduction |
| Compares all eligible players, not buyers only; revenue scope (Robux) and period matched | 3 | 2 | q4.md:23 "A-13 (compare all eligible players, not buyers only)"; q4.md:18 "for the same days before and after". Withheld 1: Robux or revenue scope is never named (q4.md:21 "Window and rule version: not given" only) |
| Checks for a managed price-optimization test; checks retention guardrail | 1 | 0 | Neither appears. The only retention mention is "D7 of payers" (q4.md:26), which is not a guardrail on all eligible players. `diagnosis.md:78` says to check for a managed price test before any other price change; the agent did not apply it |
| How sure: Low until those numbers are in; one next measurement | 2 | 2 | q4.md:16 "Low for 'great'"; q4.md:18 one pull: payer conversion, ARPU, total revenue, 4 weeks before and 2 weeks after |
| **Total** | 10 | **8** | |

Break-even arithmetic is shown and correct: 1/1.30 = 0.769, so payers may fall 23% (q4.md:11, q4.md:24).

## H5 - q5.md: "D7 crashed; the 2026-10-17 cohort shows 2.1%, older cohorts 9-10%"

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| Cohort not mature (7 days plus reporting); low value is incomplete data, not a crash | 5 | 5 | q5.md:7 "no D7 crash yet ... has not finished its seventh day ... partial number"; q5.md:10 return day 2026-10-24 is in the future; reporting lag in `calc/q5-maturity-1017-d7.json` (readable 2026-10-26), labelled PROPOSAL at q5.md:21; older cohort mature `q5-maturity-1010-d7.json` |
| No alarm; says when it becomes readable | 3 | 3 | q5.md:17 "Do nothing to the game yet ... After 2026-10-26 I read D7"; the escalation is conditional on D1 (q5.md:17) |
| Plain explanation for the owner | 2 | 1 | The core explanation is plain (q5.md:10). Withheld 1: Part 1 uses "cohort" and "mature" without a plain gloss (q5.md:7, q5.md:11, q5.md:15), plus "Opus at high effort" and the 2026-10-12 aside (q5.md:12, q5.md:17), which are noise for the owner |
| **Total** | 10 | **9** | |

Bonus not scored: q5.md:25 warns that a cohort of a few dozen players can show 2.1% by chance.

## Number checks

| Item | File | Result |
| --- | --- | --- |
| "not before 2026-11-04" (14 days plus a day, from an assumed 2026-10-20 start) | q2.md:18 | Arithmetic not shown. Dates are tied to a stated assumption but have no calc file. Minor |
| Maturity dates | q2.md:13, q3.md:11, q5.md:7, q5.md:11 | All trace to `calc/*.json` (checked: 10-23, 10-29, 10-26, 10-19). The one-day lag is labelled PROPOSAL in Part 2 only (q5.md:21, q2.md:22). Part 1 states the dates as plain fact |
| Review dates 2026-10-28 | q1.md:17, q4.md:18 | Plan dates, not data. Fine |

## Rule questions (for the lead)

| ID | Question | My reading |
| --- | --- | --- |
| RQ-1 | q4.md:12 puts made-up counts (100 and 77 payers per 1,000) and a confidence interval from them (`calc/q4-example-payer-share-10-to-7.7.json`) into the owner's Part 1. Rule A-01 says every number resolves to a pull or a `stats` output, and no number comes from writing. Is a labelled hypothetical allowed in Part 1? | I did not count it as a break. It is labelled "Example only, with made-up counts ... not our data" in three places (q4.md:12, q4.md:24, the file name), and nothing is presented as fact. It is still risky: the owner sees "-4.8 to +0.2" next to a real question, and the calc JSON has no "hypothetical" field inside. H4 passes only if the lead agrees it is not a break. If the lead rules it is one, H4 fails. Suggested rule: hypothetical inputs go in Part 2 only, with a "hypothetical" field in the saved file |
| RQ-2 | Part 1 gives readable dates that depend on an unproven one-day lag (PROPOSAL), without saying so in Part 1 (q5.md:7). Is a PROPOSAL label needed in Part 1? | Not a break because the dates are labelled in Part 2. The owner reads Part 1 alone, so add "(plus one day for reporting, our assumption)" |
| RQ-3 | q3.md:16 says the live-ops designer is "a planned role". Is the skill text or the agent wrong? | The skill text. `analysis-craft/references/handoffs.md:3` still says "live-ops designer (planned)", while line 5 says it exists since J014; `analysis-craft/SKILL.md:54` and `:97` also say planned roles go through the lead. Fix the files |

## Top 3 skill gaps the answers reveal

1. **Stale routing text sends events to the lead, not the live-ops designer.** q3.md:16. Fix the header of `analysis-craft/references/handoffs.md` (line 3) and make `SKILL.md:54,97` list which roles are still planned. Without a fix the analyst will mis-route every event question.
2. **The money checks in `diagnosis.md` were not applied to a price question.** q4.md has no managed price-optimization check, no retention guardrail on all eligible players, and no revenue scope (Robux, period). `diagnosis.md:78` has the first one, so this is a missing checklist trigger, not missing knowledge. Add a "price change" checklist line to `analysis-craft` (check managed test, then ARPPU with conversion and ARPDAU, then retention guardrail, then Robux scope).
3. **The question-framing and benchmark steps are only half used.** q1.md never asks what decision the number serves (`analysis-design/SKILL.md:12`, step 1), and it omits the band's read date and pool (`metrics-roblox.md:54`). Same pattern in q5: Part 1 keeps technical words (cohort, mature). Add to the answer template in `reporting.md`: one line "decision this serves", the band with read date and pool, and a plain-words check on Part 1. Also add the RQ-1 rule on hypothetical numbers.

## Re-score after skill fixes

Scored from `analyst/hidden-rerun/q1.md`, `analyst/hidden-rerun/q4.md` and `analyst/hidden-rerun2/q4.md`. Original scores above are unchanged. Lead ruling applied (RQ-1): any hypothetical, example or made-up number in Part 1 is a rule break and the case fails, whatever the points.

| Case | File | Points | Rule break | Result |
| --- | --- | --- | --- | --- |
| H1 re-run | hidden-rerun/q1.md | 8/10 | yes: "100 players ... 1,000 players" in Part 1 (hidden-rerun/q1.md:22) | FAIL |
| H4 first re-run | hidden-rerun/q4.md | not scored in full | yes: made-up numbers in Part 1 (hidden-rerun/q4.md:22) | FAIL (confirmed) |
| H4 second re-run | hidden-rerun2/q4.md | 10/10 | none found | PASS |

### H1 re-run - hidden-rerun/q1.md

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| No public genre average; forum number is not a benchmark; none invented | 3 | 3 | hidden-rerun/q1.md:21 "The 25% is a forum number ... Roblox publishes no 'good D1' for one genre" |
| Own peer band (50th-90th, read date, pool) and own trend | 3 | 2 | Band and pool: q1.md:22 point 2 "band of similar games (50th to 90th percentile)"; trend: q1.md:24 "our own D1 trend with counts". Withheld 1: the band's read date is still not named or requested (q1.md:24, q1.md:60) |
| Asks what decision this serves; D1 diagnosis path | 2 | 1 | Path given: q1.md:22 point 4 (source), q1.md:25, q1.md:61-62 (source, platform, first-session funnel). Withheld 1: no question about the decision; "Your decision: None" (q1.md:26) is a template line, not a question |
| Plain words | 2 | 2 | Part 1 is plain; jargon is in Part 2 |
| **Total** | 10 | **8** | |

Rule break: q1.md:22 point 3 puts "With 100 players ... With 1,000 players" in the owner's Part 1, with the tag "illustration only" and the source rows S3 and S4 (q1.md:37-38) that are made-up counts. This is a hypothetical number in Part 1, so the case FAILS under the ruling. The interval figures themselves are in Part 2 only (q1.md:49), which is allowed. The fix is small: write "with few new players ... with many" in Part 1.

### H4 first re-run - hidden-rerun/q4.md (confirming the lead's reading)

Part 1 has "Example, made up: ... 1.3 x 0.7 = 0.91" and "(4.0% to 2.8%, 40 and 28 per 1,000)" at hidden-rerun/q4.md:22 (points 2 and 3). Both are made-up numbers in the owner's Part 1. FAIL confirmed. The rest of the file is good (it checks all eligible players, q4.md:24; uses ARPDAU in the contract, q4.md:42) but still lacks the managed price-test and retention-guardrail checks.

### H4 second re-run - hidden-rerun2/q4.md

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| Payer count, payer conversion, ARPDAU; ARPPU rises when small spenders leave | 4 | 4 | hidden-rerun2/q4.md:20 point 2 "small spenders ... the average rises because they left"; ask q4.md:22 "number of payers, share of players who pay, revenue per player, total revenue"; q4.md:47 names "payer count, payer conversion, ARPDAU and total revenue" |
| All eligible players; Robux scope and period matched | 3 | 3 | q4.md:22 "all players, not only payers"; q4.md:38 unit Robux, "Equal whole weeks before and after"; q4.md:64 "same weekdays" |
| Managed price-optimization test; retention guardrail | 1 | 1 | q4.md:47 "any running managed price-optimization test; a retention guardrail on all eligible players"; q4.md:55 and q4.md:66 (owner asked); guardrail also in Part 1 q4.md:22 "day-1 and day-7 return of all players did not drop" |
| Low until the numbers are in; one next measurement | 2 | 2 | q4.md:21 "Low"; q4.md:22 one read of four numbers for the weeks before and after |
| **Total** | 10 | **10** | |

No made-up number in Part 1: the only figures are the +30% from the question and the dates. No `calc/` folder exists and q4.md:33 says so, which matches the files on disk. Result: PASS.

### Rule questions from the re-score

| ID | Question | My reading |
| --- | --- | --- |
| RQ-4 | hidden-rerun2/q4.md:22 gives "check on: 2026-11-04 (14 days after a clean before/after, see H)". The change date is unknown (q4.md:38), and section H does not explain the 14 days or the date. Is a review date with no stated base allowed? | Not a made-up data number and not hypothetical, so I did not count it as a break. It is a date with no visible arithmetic, the same kind of gap as q2.md:18 in the first run. Ask the agent to show the base ("14 days after the change date once known") |
| RQ-5 | Is a comparative phrase with plain counts, such as "with 100 players", a hypothetical number? | I counted it as one, in line with the ruling ("any"). If the lead wants a softer line, the rule should say whether words like "few" and "many" are the allowed form |

### Remaining gap after the fixes

H1 still has no question about the decision the number serves (step 1 of `analysis-design/SKILL.md`), and the read date of the band is still missing. Both appear in two runs now, so they are skill gaps and not chance. The made-up-number habit in Part 1 appeared in two of three re-runs (hidden-rerun/q1.md:22, hidden-rerun/q4.md:22) and not in the third, so the rule is not yet reliable. It needs a hard check in the self-check list ("Part 1 has no number that is not from a pull, the question, or shown arithmetic").

## Re-score 2

Scored from `analyst/hidden-rerun3/q1.md` and its `calc/` files. Earlier scores are unchanged. RQ-1 ruling applied: a hypothetical number in Part 1 fails the case.

### H1 second retry - hidden-rerun3/q1.md

| Expected item | Avail. | Given | Evidence |
| --- | --- | --- | --- |
| No public genre average; forum number is not a benchmark; none invented | 3 | 3 | hidden-rerun3/q1.md:19 "a forum post. It is not a Roblox number, and no public table of 'good' Day 1 return by genre exists"; q1.md:20 point 1 |
| Own peer band (50th-90th, read date, pool) and own trend | 3 | 3 | Band and trend: q1.md:20 points 3-4, q1.md:22 "Roblox peer band and your own last weeks". Read date and pool: q1.md:54 "Needs pull date and pool"; q1.md:74 owner "sends the band, the pool and the date". The gap from the first two runs is closed (the 50th-90th range itself is in q1.md:54) |
| Asks what decision this serves; D1 diagnosis path | 2 | 1 | Path: q1.md:23 "where new players stop in their first session"; q1.md:75 source mix, platform, first-session funnel. Withheld 1: still no question about the decision. "Your decision" (q1.md:24) asks for a screenshot or the key. "Is Day 1 return low enough to act on?" (q1.md:41) is the agent's own frame in Part 2, not asked of the owner |
| Plain words | 2 | 2 | Part 1 is plain ("a band of similar games", "by chance"). Small slips: "finished cohorts only" and "the key" (q1.md:22, :24) |
| **Total** | 10 | **9** | |

Rule check (Part 1): the only numbers are 25%, 17%, "8 points" (shown as the gap of the two given figures and tagged S1, q1.md:19) and the review date 2026-10-28 (q1.md:22). No hypothetical, example or made-up number. "With few players" (q1.md:20) uses words, not a count. No rule break. Result: PASS.

Rule questions:
- RQ-6: The hypothetical intervals sit in Part 2 only (q1.md:34, :57), labelled "HYPOTHETICAL" in both places and in the file names. Allowed by the ruling. But the calc JSON files (`calc/gap_n100_hypothetical.json`) hold the inputs 25/100 and 17/100 with no "hypothetical" field inside, so a later reader of the file alone could take them for data. Same advice as RQ-1: add the field, or keep such runs out of `calc/`.
- RQ-7: q1.md:83 puts the lesson draft inside the answer file. Not part of the rubric; it does not touch Part 1. No action from me.

## Final summary

| Case | Final file | Score | Result |
| --- | --- | --- | --- |
| H1 D1 benchmark | analyst/hidden-rerun3/q1.md | 9/10 | PASS |
| H2 Early Harm Detection | analyst/hidden-run/q2.md | 9/10 | PASS |
| H3 Events double retention | analyst/hidden-run/q3.md | 9/10 | PASS |
| H4 ARPPU +30% | analyst/hidden-rerun2/q4.md | 10/10 | PASS |
| H5 D7 crash | analyst/hidden-run/q5.md | 9/10 | PASS |

All five final files meet the bar with no rule break under the RQ-1 ruling. Two caveats stay open: H1 still never asks what decision the number serves (skill step 1 of `analysis-design/SKILL.md`; it was missed in three of three H1 runs), and H3 still routes to the lead because of the stale "planned" text (Gap 1 above), which has not been re-run.
