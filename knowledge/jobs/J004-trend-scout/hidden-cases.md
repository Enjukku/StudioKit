---
type: job
scope: universal
status: active
updated: 2026-10-20
source: J004
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

# J004 hidden test set (lead only)

DO NOT give this file, or any line of it, to the trend-scout agent, to a skill writer or to a tool builder. It holds the parts of the research paper (`Roblox_Trend_Scout_Research_2026.txt`) held out by order on 2026-10-20 (ticket J004-T02). The reference note `knowledge/reference/trends/02-outside-access-scoring.md` has none of it. Use it only to test the finished agent after the skills exist.

Layout: each case has **Input** (names, dates, numbers as the paper gives them; show only this to the agent), **Ask** (a test prompt) and **Expected** (the paper's own conclusion; keep it from the agent). Tags: VERIFIED official / VERIFIED sampled / VERIFIED derived / EXPERIENCE / OPINION as in the paper. Cutoff date used by the paper: 2026-10-20. `RP:` = paper line. I re-did all date and ratio arithmetic; it matches the paper.

## A. Timing quantities (RP:338-346, plus RP:362 and RP:361 which repeat parts)

Table header in the paper: Timing quantity | Evidence or calculation | Correct use | Mark. For each case, show the agent only the Input.

| id | Input | Ask | Expected (paper) | Mark | RP |
| --- | --- | --- | --- | --- | --- |
| HC-A1 | Grow a Garden. Official launch 2025-03-25. Roblox Q2 2025 shareholder letter (S13, filed 2025-07-31) calls it the top experience by spending within one month of its creation | What can be said about launch-to-top-spending time, and what cannot? | A documented rapid monetization rise. Exact cash is not available | VERIFIED official S13 | 340 |
| HC-A2 | Janzen "Jandel" Madsen, GamesBeat interview (S17a, published 2025-09-07, updated 2025-09-08): about 500 players to 100,000 in two weeks; about 1 million in a month. Developer recollection, not an audit | Use these to forecast how fast a small game scales? | No. EXPERIENCE about one selected outlier, not a forecast | EXPERIENCE S17a | 341 |
| HC-A3 | 99 Nights in the Forest. Official DevForum creator spotlight (S24, posted 2025-10-31): built in a sprint of three months | Use as the studio's expected delivery time? | No. A schedule example for one successful co-op survival game. Also: do not confuse a prototype story with a live game (RP:361) | EXPERIENCE S24 | 342, 361 |
| HC-A4 | Squid Game. Netflix release 2021-09-17 (S32). DevForum update log with a working minigame sequence posted 2021-09-30 06:22 UTC (S33) | Time from show to Roblox adaptation? | At most 13 days to that dated update. A fast-visibility bound. Not the first adaptation, not time to peak (same fact is in the reference note, section 2) | VERIFIED derived S32-S33 | 343 |
| HC-A5 | Grow a Garden. Rolimon's recorded maximum CCU on 2025-08-23 (S16). Cutoff 2026-10-20 | Days since peak, and what does the number mean? | 423 days. Time since the recorded peak. Not the length of the rise, not its profitable life | VERIFIED derived S16 | 344 |
| HC-A6 | Escape Tsunami For Brainrots (the "hazard-brainrot" game). Rolimon's sampled maximum 2026-01-24 (S18). Cutoff 2026-10-20 | Days since peak, and what follows? | 269 days. Time since peak. Its recent peak scale is far lower | VERIFIED derived S18 | 345 |
| HC-A7 | Grow a Garden 2. Rolimon's sampled maximum 2026-06-19 (S61). Cutoff 2026-10-20 | Days since peak, and what follows? | 123 days. A 2026 launch can already be past its peak phase | VERIFIED derived S61 | 346 |
| HC-A8 | Rule row RP:362: the hazard game's recorded peak was 269 days before the cutoff; S18, accessed 2026-10-20 | May we call an old viral theme early? | An old viral theme is not automatically early. VERIFIED derived plus OPINION interpretation | VERIFIED derived / OPINION | 362 |

Checks the agent must pass: counts days from the dates given; says "sampled/recorded maximum" not "true peak" (Rolimon's page distinguishes the two, RP:510); does not turn 423, 269 or 123 into a trend lifetime; keeps EXPERIENCE cases out of forecasts.

## B. "Already too late" paragraph (RP:356)

Input (show only this):
- Cutoff 2026-10-20.
- Candidate thesis 1: a straightforward Grow a Garden reskin. Evidence: Rolimon's maximum 2025-08-23 (S16).
- Candidate thesis 2: a January hazard-brainrot imitation. Evidence: sampled maximum 2026-01-24 (S18).
- Candidate thesis 3: a first-mover Verity adaptation. Evidence: series debut 2026-05-30, fan song 2026-07-10, Roblox game video shown 2026-07-25, spread across platforms (S34b-S34d).
- Related: Grow a Garden 2 sampled maximum 2026-06-19 (S61).
- Extra context for the agent to weigh: fishing, PvP and survival game families.

Ask: Which of these can still be sold as an "early original wave", and what may not be concluded?

Expected (paper, OPINION S16, S18, S34b-S34d, S61):
1. At the cutoff all three (the plain Garden reskin, the January hazard-brainrot imitation, the first-mover Verity adaptation) are already too late for an "early original wave" claim.
2. That is a claim about timing, not about demand: it does not mean zero current demand or zero profit. The early-entry thesis is contradicted by dated mass adoption.
3. A new sub-mechanic, a regional audience or an underserved experience needs its own current evidence.
4. Durable fishing, PvP and survival families can still support original products after the first game's peak.

Fail signs: the agent says "no demand" or "reject"; the agent writes off the whole fishing/PvP/survival families; the agent accepts a sub-mechanic claim with no dated evidence.

## C. Dated candidate example at the research cutoff (RP:387-404)

Paper note on the data (RP:389, VERIFIED sampled S25, S26, S62): genuine retrieved third-party leads, not official owner analytics. Values come from each game page, which updates separately from the ranking list. Latest sample times: Robot Fighter 2026-10-21 01:25 UTC; Dog 01:06 UTC; both are the evening of October 20 in New York. Tracker creation dates are not verified public-launch dates. Exact revenue, true retention, acquisition mix and legal clearances are unknown.

Input (show only this table):

| Candidate | 24h average CCU | Seven-day average CCU | Observed peak (date) | Source |
| --- | ---: | ---: | --- | --- |
| Create a Robot Fighter | 1,005 | 301 | 2,803 (2026-10-20) | RoVitals S25 |
| Something is Wrong With My Dog | 3,466 | 1,261 | 9,900 (2026-10-20) | RoVitals S26 |
| Backseat Rally | 20,489 | 10,274 | 29,270 (2026-10-20) | RoVitals S62 |

Register facts for these sources (also held out): S25 page has a separate hypothetical earnings model, quote "actual earnings may fall outside it". S26 reproduces a developer description, quote "Inspired by LookOut2DD's". S62: tracking began 2026-10-13, historical sampled maximum 2026-10-20, page windows differ slightly from the list inspected at the same time, quote "Over the last 7 days it averaged 10,274 players." Extractor observation, not in the paper: with tracking from 2026-10-13, the seven-day window for S62 covers almost all of its history.

| id | Ask | Expected (paper) | RP |
| --- | --- | --- | --- |
| HC-C1 | Compute momentum from the rounded inputs and name the window problem | Robot Fighter 1,005/301 - 1 = +233.9%. Dog 3,466/1,261 - 1 = +174.9%. Backseat 20,489/10,274 - 1 = +99.4%. The two windows overlap (the 24h sits inside the 7d), so this is NOT week over week | 393-395, 403 |
| HC-C2 | A teammate writes "Robot Fighter grew 234% week over week". Correct it | Wrong label: overlapping windows, not WoW. Value is derived from rounded sampled inputs. Keep the evidence tag VERIFIED sampled / derived | 393, 403 |
| HC-C3 | Give the top three research opportunities (not build approvals), each with the loop and its limit | (1) modular assembly plus wave combat, original theme, motivated by Robot Fighter's early growth. Risk: growth could reflect bought distribution. (2) group vehicle coordination, motivated by Backseat Rally's audience and momentum; pending direct loop inspection, since the page alone does not show its precise mechanic. (3) replayable familiar-companion anomaly survival, motivated by Dog's rise; wholly original character, story and audio; the source inspiration needs rights-aware differentiation | 397 |
| HC-C4 | Give each a weighted total out of 100 | Refuse: none has enough evidence for a credible full weighted total. The right report ranks research priority and leaves the investment score incomplete (with the known/unknown range and completeness, per the scoring rules in the reference note) | 397, 404 |
| HC-C5 | Can the tracker "created" date be used as launch date? Can CCU growth show profit or retention? | No to both. Creation dates are not verified launch dates. Revenue, retention, acquisition mix and clearances are unknown. No candidate has validated profit | 389, 404 |

Rule table in the paper for this example (RP:399-404; all withheld from the reference note):

| Rule | Number | Evidence mark | Source and date |
| --- | --- | --- | --- |
| Score explicit evidence and uncertainty | 0-5 per dimension, 100 weighted maximum | OPINION rubric | S03, S07; author method 2026-10-20 |
| Require meaningful completeness | Proposed 80% for funded-prototype recommendation | OPINION policy | S07; author method 2026-10-20 |
| Label overlapping-window momentum correctly | Robot Fighter +233.9%, Dog +174.9%, Backseat +99.4% | VERIFIED sampled inputs / derived | S25, S26, S62, accessed 2026-10-20 local |
| Unknown money remains unknown | No validated candidate profit supplied | OPINION evidence policy | S07, S09, S25-S26 |

(The first two rule rows repeat the scoring sheet, which is in the reference note, section 9.)

## D. Other held-out register facts

| source | withheld fact | RP |
| --- | --- | --- |
| S13 | quote: top experience based on spending within one month of its creation | 633 |
| S17a | quote: within two weeks, about 100,000 CCUs (developer interview, recollection) | 631 |
| S16 | Rolimon's Grow a Garden page, historical maximum 2025-08-23 | 521 |
| S18 | Rolimon's Escape Tsunami For Brainrots, sampled maximum 2026-01-24, recent counters | 525 |
| S61 | Rolimon's Grow a Garden 2, historical sampled maximum 2026-06-19 | 606 |
| S25, S26, S62 | RoVitals game pages: see section C | 538, 540, 608 |

Not withheld, so the agent may see them: the three-month build figure (RP:361, 484; reference note section 8 and section 13 item 16) and the 13-day Squid Game lag (reference note section 2). If the lead wants HC-A3 fully hidden, delete the RP:361 and RP:484 mentions from the reference note first.
