---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J004-T10
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J004-T10 grade of the trend-scout eval answers

Answers under test: `knowledge/jobs/J004-trend-scout/trend-scout/eval-answers.md` (line numbers below are from that file). Checks: `.agents/skills/trend-scan/evals/briefs.md`. Expected answers for E4/E5: `hidden-cases.md` (A5-A8, B, C1-C5). Inputs the agent had: `eval-inputs.md`. I redid all arithmetic. Grading is on the written checks only; style and length are not graded. "borderline" = I judge a near miss; the lead may rule it either way (see Sensitivity).

## Result table

| Eval | Checks passed | Verdict |
| --- | --- | --- |
| E1 | 4/4 | PASS |
| E2 | 4/4 | PASS |
| E3 | 3/4 | FAIL (E3-3 borderline) |
| E4 | 3/4 | FAIL (E4-4 borderline) |
| E5 | 2/4 | FAIL (E5-2 clear; E5-4 borderline) |

Pass rule: an eval passes only when every check passes; the agent passes the set at >= 4 of 5.

**SET: 2/5 evals passed**

## Sensitivity (for the lead)
- E5 fails on E5-2 whatever else is ruled, so the best possible result is 4/5.
- E3-3, E4-4 are the two borderline fails that decide the set. If both are ruled pass, the set is 4/5 (agent passes). If either stays fail, the set is 3/5 or less (agent does not pass).
- E4-4 and E5-4 test content the eval inputs never provoke (no sub-mechanic claim in the E4 input; no `created` date in the E5 table). Eval fix, not only agent fix: see proposals P3, P5.
- E5-2 conflicts with a skill rule (no loop from titles). See proposal P4. The lead must decide which side is right before the agent is retrained.

---

## E1 - Label the numbers

| Check | Verdict | Evidence / reason |
| --- | --- | --- |
| E1-1 Each number carries one label (OFF, OFF, 3P-E with vendor/range/accuracy, DER) | pass | 4,210 "OFF (Games API `playing`)"; 12,400,000 "OFF (Games API `visits`)"; 85,000 "3P-E (tracker; name UNKNOWN) ... range UNKNOWN ... accuracy UNKNOWN" (vendor was not in the brief, so UNKNOWN is honest); ratio "DER, momentum". The two means are tagged "our store ... 3P-S-class" (not a defined label), see extra issue 1; the DER tag is on the ratio and the differences. |
| E1-2 Ratio is momentum, not week-over-week | pass | "It is momentum. It is NOT week-over-week growth and NOT g7." 3,900/2,100 = 1.857 correct. |
| E1-3 No conversion of CCU or visits into users, players or money | pass | "What it is not: daily users, unique people"; visits "not players, sales, retention"; revenue "no dollar value". |
| E1-4 Owner sentence keeps the doubt, no profit claim | pass | "the 85,000 Robux/day figure is one tracker's estimate with unknown accuracy and I do not use it." The words "third-party" are absent, the doubt is kept. |

Arithmetic checked: 3,900-2,100 = 1,800; (2,100x7-3,900)/6 = 1,800; 4,210/3,900 = 1.08. All correct.

## E2 - Is it a breakout?

| Check | Verdict | Evidence / reason |
| --- | --- | --- |
| E2-1 No automatic breakout flag (84 % < 90 % gate, 3 h gap) | pass | "Do not set a breakout flag. The coverage gate holds it ... (84 % < 90 %)"; "Longest gap 3 h; gap limit is 60 min (PROPOSAL), so it stays a gap". |
| E2-2 g7 +100 %, added CCU +900, coverage caveat | pass | Table: "g7 +100 %", "Added CCU +900", "last week 84 %, week before 97 %: the two weeks are not equally covered". |
| E2-3 Video as alternative explanation; asks troughs / independent creators / next week | pass | "one big, named alternative explanation"; check list items 3 (troughs), 7 (other independent creators), 8 (next complete week). |
| E2-4 Thresholds called PROPOSAL | pass | "Rule check (PROPOSAL flag rule, `formulas.md` section 3)"; file header: "All thresholds named here are PROPOSAL values". |

Arithmetic checked: 1,800/900-1 = +100 %; 0.84x1,800 = 1,512, 1,512/900 = 1.68 = +68 %; day split 8-11 = 4 days, 12-14 = 3 days. All correct.

## E3 - Copying a loop

| Check | Verdict | Evidence / reason |
| --- | --- | --- |
| E3-1 Abstract loop may be borrowed | pass | "Loop (abstract) | pass ... A loop idea is free to borrow." Loop stated as catch, sell or catalogue, better gear, rarer pools. The legal basis (ideas and methods of play not protected) is not given; the check does not ask for it. |
| E3-2 Anime look HOLD unless licensed; name fail with trademark and discovery reasons | pass | "A franchise theme without a licence is HOLD"; "'Fisch Legends' FAIL ... same or confusingly similar name ... trademark confusion and, on Roblox, lower discovery for games that closely resemble existing ones". |
| E3-3 Asks for a visible first-session twist and independently made assets | **fail (borderline)** | Assets half passes: "Pass only if made by the studio or licensed"; "documented asset sources"; thumbnail "must not resemble" the Fisch icon. Twist half is a near miss: the answer asks for "a stated twist" that "must change a player decision, stake, cooperation or expression". It never says the twist must be visible, nor that a new player must see it in the first session. The skill has that wording (`opportunities.md` line 29, "clear first-session twist") but the agent did not carry it into the gate. |
| E3-4 No "safe copying percentage" | pass | No percentage or tolerance is given anywhere. |

## E4 - Timing (cut-off 2026-10-20)

| Check | Verdict | Evidence / reason |
| --- | --- | --- |
| E4-1 Days computed correctly, called time since the recorded (sampled) maximum, not a trend lifetime | pass | 423 / 269 / 123 match the paper (HC-A5..A7) and my count. "highest recorded sample ... (3P-S, tracker, not the true peak)"; "It does NOT say current CCU, how steeply the game fell, or that demand is gone"; "No half-life". Verity has no recorded peak, so the answer gives event ages 143 / 102 / 87 and says peak UNKNOWN (correct; 143, 102, 87 and the lags 41/56/15 re-counted). The phrase "dated mass-adoption high point" is a little stronger than "sampled maximum" but the definition stays right. |
| E4-2 All three theses too late for an "early original wave" claim | pass | Thesis 1 "No ... 423 days"; thesis 2 "No ... 269 days"; thesis 3 "Not as worded ... a documented cross-platform wave, which already closes an 'early wave' claim ... 'first-mover' is contradicted or at least unproven". The "Not as worded" hedge is soft but the reasons close the claim. See extra issue 6. |
| E4-3 Timing not zero demand; durable families can carry an original game with current evidence | pass | "Not concluded: that thesis 1 or 2 have no demand now"; "Fishing, PvP, survival families: Not 'early', but durable ... An original game can still enter, if it has its own current evidence and a stated twist". |
| E4-4 Rejects a new sub-mechanic claim that has no dated evidence | **fail (borderline)** | The words "sub-mechanic" (or regional audience, underserved experience) never appear and no such claim is rejected. Nearest text: "if it has its own current evidence and a stated twist" (about an original game, not about an undated claim) and "A twist alone does not guarantee staying power". The input holds no such claim, so the agent was not prompted; the check still asks for the rejection, and the skill does not tell the scout to state it unprompted (P3). |

## E5 - Three candidates from tracker data

| Check | Verdict | Evidence / reason |
| --- | --- | --- |
| E5-1 Momentum computed, labelled overlapping not WoW, inputs 3P-S | pass | "x3.34 / x2.75 / x1.99" equal +233.9 / +174.9 / +99.4 % (1,005/301 = 3.339; 3,466/1,261 = 2.749; 20,489/10,274 = 1.994). The ratio form is the skill's own (`formulas.md` line 19). "All momentum values are momentum, **not** weekly growth"; "tracker data gives no non-overlapping weeks"; "Source: RoVitals, 3P-S". The word "overlapping" appears only as "non-overlapping", yet the label is clear. Percent form is not shown (minor). |
| E5-2 Ranks research priority with 3 cards, each with loop, original theme direction, main doubt | **fail** | The ranking exists (Backseat Rally, Dog, Robot Fighter; "Research ticket"). There are no cards: loop is "UNKNOWN" for all three ("loop line, twist and theme are all UNKNOWN"), no original theme direction is given for any, and the main doubt is not given per game. Generic "Missing evidence" items 4, 6, 7 mention ads, loop line and rights, but not as per-card doubts (bought traffic for Robot Fighter; loop not yet inspected for Backseat Rally; source inspiration needs a rights-aware difference for Dog). The agent applied the skill rule "not from titles" and refused to give even a labelled hypothesis. Honest, but the check is not met (see P4). |
| E5-3 Refuses a full weighted total; gives known points, range, completeness | pass | "Gates are open, so **no score is given**"; table "Lower 0 / Upper 100 / Completeness 0 %" per candidate; "any single number would be invented". |
| E5-4 Tracker "created" date is not a launch date; no revenue, retention or profit claim | **fail (borderline)** | The no-claim half passes: "Revenue evidence is none (tracker CCU is not money)"; "Not concluded: ... CCU equals users or money". The `created` half is never stated. The answer asks for "Universe ID and `created` date for each" without saying the tracker date is not the public launch date. The table has no `created` date, so the agent was not prompted. |

Arithmetic checked: added players 704 / 2,205 / 10,215; implied 6-day means 183.7 / 893.5 / 8,571.5; 24 h/peak 0.36 / 0.35 / 0.70; 7 d/peak 0.11 / 0.13 / 0.35. All correct.

## Extra issues (not covered by a check)

1. E1: the two store means are labelled "3P-S-class sampling of an OFF counter". Not a defined label; samples the studio collected itself from an official counter are not third-party. The skill has no label for own-store means (P1).
2. E1 and E5: "Added players, 24 h vs 7 d". The difference of two mean CCU values is added CCU, not added players. The wording invites the "CCU = players" reading the rest of the answer avoids.
3. E2: "So the rise is probably real" is an unlabelled judgement. It rests on a zero-fill bound that ignores the week before's 3 % hole and the video. The same section says no conclusion.
4. E4: "Verity is a franchise character" and the "abstract tension (a helpful companion turns unreliable)" are not in the inputs ("series debut", "fan song", "Roblox game video"). Unsupported by the inputs and not labelled as assumption.
5. E4: RIVALS is listed among games that "still hold big 2026 audiences". `loops.md` line 28 says only "established; rise/fade dates UNKNOWN" for RIVALS. The other four (Fisch, Fish It, Steal a Brainrot, 99 Nights) are supported; all five day counts (367, 317, 374, 381, 248) are correct.
6. E4: Verity is named the "Best supported path" while the same answer says peak, Roblox number and direction are UNKNOWN and rights are HOLD. "Best supported" has no support in the answer; the paper's verdict is that all three are too late.
7. E5: the ranking rule (24 h/peak ratio first, then added players) is not traced to a skill. All three peaks sit on the same day inside the 24 h window, so the ratio mostly measures one day's shape. The rule puts the lowest-momentum game first. It is labelled "may change", so this is a weak-method issue, not a false claim.
8. E5: the "implied mean of the other 6 days" figures assume at least 7 days of tracking and equal coverage. Game age and tracking start are UNKNOWN (the answer says so elsewhere), so the table needs that condition on the numbers themselves.

Extra issues: 8.

## Good practice seen (not graded)
E2 bounds the coverage effect instead of correcting the number; E5 names the shared-cause risk (all three peaked the same Tuesday) which the checks do not ask for; E1 and E2 never convert CCU into users or money.

## Skill-gap proposals (PROPOSAL, for the lead; none applied)

| id | Where the answer went wrong | Proposal |
| --- | --- | --- |
| P1 | E1: invented "3P-S-class" for own-store means | `market-trends` SKILL step 2: add the label rule for the studio's own store: "own store, built from OFF samples: label DER, with window, coverage and read time". |
| P2 | E3-3: asked for "a stated twist" only | Put "visible to a new player in the first session" into the G5 row of `opportunities.md` and the rights-gate template, not only into the Room score row. |
| P3 | E4-4: no sub-mechanic rejection (and the E4 input holds no such claim) | Add one rule to the timing part of `loops.md`/`outside-trends.md`: a new sub-mechanic, regional audience or underserved-experience claim is rejected until it has its own dated, current evidence; state it whenever a timing verdict closes an early-wave claim. Add such a claim to the E4 input so the check can be run. |
| P4 | E5-2: no loop/theme/doubt on the cards because the skill forbids a title-only identity | Decide: either (a) allow a card to carry a labelled "loop hypothesis (UNVERIFIED, from title/family)" plus an original theme direction and a fixed doubt line (bought traffic, loop not inspected, rights-aware difference), or (b) change check E5-2 to accept "loop UNKNOWN" with the doubts per card. Today the skill and the check pull in opposite directions. |
| P5 | E5-4: `created` caveat not stated (and the table has no `created` date) | `signals-and-metrics.md` already says `created` is not the launch date (line 25). Add it to the `trend-scan` checklist as a line to print whenever tracker age is used, and add a `created` column to the E5 input so the check is provoked. |
| P6 | E5-1: only the ratio shown | State in `formulas.md` that owner-facing output shows momentum as ratio and percent together (x3.34, +233.9 %), always with "overlapping windows". |
| P7 | E5 ranking: invented rule; E4: "Not as worded", "best supported path" | Give the scout a research-priority ordering rule (what leads, what is a tie-break) and a rule that a cross-platform spread plus a dated Roblox example closes an early-wave claim without a "best path" recommendation. |
| P8 | Extras 3 and 8: judgements and derived figures without their validity condition | Add to the `trend-scan` checklist: every derived figure carries its assumption in the same row (equal coverage, tracking length), and no "probably" verdict is written when a gate is open. |
