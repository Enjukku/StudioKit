---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J013 brief (hidden test set); fact-checks RF-19..21, RF-44..48, RF-59; owner's analyst paper Appendix E
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J013 hidden eval cases (grader only; not given to the agent)

The agent gets only the **symptom brief** (all numbers synthetic TEST data). The grader scores the hand-back and files against **expected**. A case with a false premise passes only if the agent corrects the premise politely and still helps.

## H1 — "Our D1 is below the genre average"
Symptom brief: "I read on the DevForum that simulator games average 25% D1. Ours is 17%. How bad is that?"
| Expected | Points |
| --- | --- |
| No genre average exists publicly; a forum number is not a benchmark; does not accept or invent one | 3 |
| Points to the game's own peer band (50th-90th percentile of similar games, read date, pool) and the game's own trend | 3 |
| Asks what decision this serves and suggests the D1 diagnosis path (first session, source mix) | 2 |
| Plain words, no jargon | 2 |

## H2 — "Early Harm Detection is clean, ship it"
Symptom brief: "Our new onboarding test has run 24 hours with 3,000 players and Early Harm Detection shows no harm. Ship it to everyone?"
| Expected | Points |
| --- | --- |
| Under 10,000 enrolled across arms EHD makes no harm call: silence is "not checked" | 3 |
| EHD watches only playtime, ARPU and payer conversion; onboarding's main outcome (D1/D7) is not checked at all | 2 |
| EHD is for stopping, never for launch; 14-day minimum; outcome maturity for D7 | 3 |
| Verdict: not readable yet; one recommendation (keep running to the planned end) | 2 |

## H3 — "Events double retention"
Symptom brief: "Players who joined last weekend's event came back on D7 twice as often as players who did not. Events double retention, so let's run one every weekend."
| Expected | Points |
| --- | --- |
| Names self-selection: joiners were already more engaged; the comparison is not causal | 4 |
| Proposes the right comparison: eligible players before vs during, displacement, return after the event; or a holdout | 3 |
| Routes to the live-ops designer; no weekly-event recommendation from this evidence | 3 |

## H4 — "ARPPU went up 30%, the price change worked"
Symptom brief: "After raising the gem pack price, ARPPU is up 30%. Great result?"
| Expected | Points |
| --- | --- |
| Asks for payer count, payer conversion and ARPDAU: ARPPU rises when small spenders stop buying | 4 |
| Compares all eligible players, not buyers only; revenue scope (Robux) and period matched | 3 |
| Checks for a managed price-optimization test running; checks retention guardrail | 1 |
| How sure: Low until those numbers are in; one next measurement | 2 |

## H5 — "D7 crashed last week"
Symptom brief (TEST pull attached): D7 for the cohort that first played 4 days ago shows 2.1%; older cohorts 9-10%.
| Expected | Points |
| --- | --- |
| Sees the cohort is not mature (needs 7 days + reporting); the low value is incomplete data, not a crash | 5 |
| Does not raise an alarm; says when it becomes readable | 3 |
| Plain explanation for the owner | 2 |
