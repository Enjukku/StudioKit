---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J003
supersedes: []
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J003-T09b: grade of the G2 pitch set (evals brief 1) and independent re-rating

Order of work: I read `pitch-set.md`, the 3 records, `candidates.md`, the rubric, the eval briefs and `fact-check-roblox.md` first. I wrote my 10 ratings (Part 2, "grader" column) before I opened `funnel.md`. I did not open any `hidden-` file. I had no web access. Anything that rests only on a web page or a live Roblox counter is marked "not re-checked".

## Part 1: checks against evals brief 1

| check | must? | pass/fail | evidence (file, section) | note |
| --- | --- | --- | --- | --- |
| C1 Proposes, never decides | must | pass | `pitch-set.md` intro ("Titles, numbers and content are PROPOSAL"), "My recommendation" (one pick, tradeoff, objection), "Decision" (owner picks); each record opens "Everything here is PROPOSAL"; `git diff` shows `knowledge/design/decisions.md` unchanged | Minor: the proposals were not added to `knowledge/design/open-questions.md` (AGENTS.md section 0). The brief did not ask for it. The default "I prepare the pre-production step 1 brief" starts no build and the pitch template allows a default. |
| C2 No invented numbers | must | pass (with a weak point) | Every player count in `pitch-set.md` "Why now" has a source and date (see the number table). Test sizes (4-6 players, 8 players, 5 treasures, 4 zones) are labelled "my proposals". No Roblox benchmark band is used as a target. Unknowns say "not verified" (Kick peak, shared-goal evidence, Rob cost of delay). | Weak point: "the pure run-from-danger game faded" compares an event peak (2026-01-24) with one late-evening snapshot (2,251). J004 summary rule 04 and `01-roblox-data-loops.md:155-156` warn against exactly this. J004 row 3 gives a 7-day peak of 32,495 that the pitch did not use. The pitch does disclose the time-of-day limit (Limits). The problem is method, not an invented number. |
| C3 Policy and rights | must | pass | Each record field 12 lists a `platform-policy` check (Robux, random, trade, text, ads, links, AI, data, maturity, franchise, chat). Field 9 flags the public-domain folk tale (Rob) and names what is not used ("no brainrot", "no lucky blocks", "no tsunami"). Paid random handled with RC21/RC23. `platform-policy` section 3 exists. | Other games are named only as loop references, as 1.1 requires. Watch item: "Kick the Meteor" shares the "Kick" word and the pattern of its reference; the record notes this and the loop is the closest copy of the three (RC42 risk). |
| C4 Paths and hand-back shape | no | pass on paths; hand-back not seen | Ledger row J003-T07 names `knowledge/jobs/J003-game-designer/g2/`; `pitch-set.md`, `funnel.md`, `candidates.md`, `concepts/*.md` are there. Records have typed frontmatter and author lines. | The designer's hand-back message (`rules/messages.md` section 3, `coverage`) was not in my inputs. Lead should confirm it. If the lead counts C4 as failed, the result is 10 of 11 and the verdict does not change. |
| C5 STE writing | no | pass | `pitch-set.md`: short active sentences, a plain table of titles, no rubric codes in the owner text. | One sentence runs about 30 words ("My checks ran at about 04:00 UTC ..."). "Critic check" is the designer's term, not the owner's. Records are dense tables, which the kit allows for AI readers. |
| 1.1 Exactly 3 cards, all 8 elements | must | pass | `pitch-set.md` sections 1-3: each has Fantasy, First image, Loop + Twist, Signature moment, Why now, Smallest version, Biggest risk with Test. | Rob's first image is "table height" in the pitch set and "floor-level" in the record. Small mismatch. |
| 1.2 Title test | must | pass | `pitch-set.md` "Next to your examples": action per title (rob / kick / drain) and the question each makes. Rubric C-02 allows an outsized object or a stake. | "Rob the Sleeping Giant" has an explicit stake. "Kick the Meteor" and "Drain the Ocean" carry the stake in the object only, like the owner's own "Destroy the Sun". |
| 1.3 Different families or fantasies | no | pass | Kick for distance (K), sneak and carry (R/S), shared-server scavenging (F/C): three different central actions and three roles (hero, thief, explorer). `funnel.md` section 3 table of families. | All three still end in "earn at a base, buy an upgrade". That is the shared Roblox spine the owner asked for. Not a skin of one loop. |
| 1.4 Real funnel counts, separate critic, no totals | no | pass (one miscount) | `pitch-set.md` intro; `funnel.md` section 0. Recount: 40 raw rows (ok), 13 candidates (ok), 3 merges to 10 (ok), 7 survivors (ok), 11 families (ok). Ratings are per criterion with no total (`funnel.md` section 6, record field 12). | Miscount: "10 seeds" (pitch-set and `funnel.md` section 0 and 4). The section 4 table uses 12 different seeds (1, 4, 6, 8, 11, 13, 14, 16, 19, 22, 32, 34). The critic pass was the same agent in the same context (disclosed in `funnel.md` section 6 and pitch-set Limits). The reasons table also uses facts that are not in `candidates.md` (the owner's dam game, tracker peaks), so it was not "only candidates.md and the rubric" as stated. |
| 1.5 One recommendation, objection, mind-changer | no | pass | `pitch-set.md` "My recommendation": tradeoff, "Strongest objection" (Steal a Brainrot may be huge because of player theft, which this pitch removes), "What would change my view" (trip-10 test; owner wants bigger scale). | Honest and specific. See the note on the recommendation in the verdict. |
| 1.6 Records with 13 fields | no | pass | All 3 records in `g2/concepts/` have fields 1-13. | Path is `g2/concepts/`, not `knowledge/design/concepts/` as the eval text says. The skill (SKILL.md step 7) says the brief's path wins and the ledger names `g2/`. Fix the eval wording. |

Result: passed 11 of 11 (10 of 11 if C4 counts as unverified). Must checks failed: none. The pass rule (80 % and no must check failed) is met. Verdict: **PASS**.

### Number spot-check

| claim | stated source | verdict |
| --- | --- | --- |
| Steal a Brainrot had over 25 million concurrent in September 2025 | Roblox newsroom 2025-12-16, RC45 | ok. RC45 confirmed. The tracker max is 2025-10-11 (J004 I19); the pitch uses only the official figure. |
| Escape Tsunami For Brainrots peak 4,996,032 on 2026-01-24 | J004 note `01-roblox-data-loops.md:212` (row 3, S18); J004 `fact-check-roblox.md:184` (K03) | ok (tracker maximum, as the pitch says) |
| Fish It peak 2,716,766 on 2025-12-07 | `01-roblox-data-loops.md:213` (row 4, S21); K06 | ok |
| "Fishing games are holding, not rising" (J004 trend note) | `01-roblox-data-loops.md:213` | partly. The note says "Proven 2025 peaks, 2026 residual audiences". "Not rising" is fair. "Holding" is the designer's gloss; Fish It is about 97 % below its peak. |
| "The pure run-from-danger game faded" (2,251 now vs 4,996,032 peak) | J004 row 3; DG2 snapshot | partly. Direction fits "much smaller recent event scale". Size is overstated by a late-evening snapshot against an event peak; J004 gives a 7-day peak of 32,495 and says the decline dates are UNK. |
| FY2025 average DAU mix: mobile 83 % | RC01, 10-K FY2025 | ok |
| Chat is off for many young accounts | RC31 | ok (Kids: off; self-declared Select: off) |
| Paid boosts need numeric odds and the `ArePaidRandomItemsRestricted` gate | RC21, RC23 | ok |
| "No reliable trend lifetime found" (Kick record, "IR1 summary row 14") | `01-roblox-data-loops.md:47` | ok |
| 153,037 / 70,628 / 7,380 / 2,251 players, 2026-10-21 03:56-03:59 UTC; Kick a Lucky Block named in the Q2 2026 letter filed 2026-07-30 | Roblox public API counters; SEC exhibit 99.1 | not re-checked (web only). The magnitudes for Steal a Brainrot (159,490), Fish It (69,352) and Escape Tsunami (2,823) in J004 agree. Kick a Lucky Block and Animal Hospital are not in J004 or `fact-check-roblox.md`. |

Checked 10 claims: 7 ok, 2 partly, 1 not re-checked. No claim is invented or contradicted by its source.

## Part 2: independent re-rating of the 10 candidates

Scale: F FAIL, U UNKNOWN, P PLAUSIBLE, O OBSERVED. Column order RB1 to RB9 (fantasy, distinct, hook, agency, feasible, taste, social/safety, evidence, loop proof). "Grader" ratings were written before I opened `funnel.md`; I did not change them afterwards. The designer's source ids (for example the 7,380 and 19,329 counts) were visible to me only as ids on `candidates.md`.

| candidate | grader RB1-9 | designer RB1-9 | differences |
| --- | --- | --- | --- |
| C01 Kick the Meteor | P P P U P P P P O | P P P U P U P P O | RB6 only (see note on taste) |
| C02 Rob the Sleeping Giant | P P P P P P U P P | P P P P P U U P P | RB6 only |
| C03 Be the Giant | P U U U U U U U U | P P P P U U P U U | RB2, RB3, RB4, RB7: I am stricter. The candidate sheet gives no base loop, no choices and no abuse handling. Both of us rule it out. |
| C04 Drain the Ocean | P P P U U P P P O | P P P U U U P P O | RB6 only |
| C05 Guard the Dragon Egg | P P P P P P P P O | P P P P U U P P O | RB5: designer U (night variety, creature AI, art weight). RB6. |
| C06 Catch a Tornado | P P P U U P P P O | P P P U U U P P O | RB6 only |
| C07 Babysit a Kaiju | P P P P P U P P O | P P U P U U P P P | RB3 (designer U: "kaiju" word), RB5 (designer U), RB9 (designer P; I say O) |
| C09 Feed the Black Hole | P P P U U P U U U | P P P U U U P U U | RB6; RB7 (I say U: the server-wide map loss can be used to grief) |
| C10 Ride the Giant Turtle | P P P U U U P P O | P P P P U U P P P | RB4 (I say U: no repeat choice stated); RB9 (designer P; I say O) |
| C11 Steal a Star | P P P P P U U P O | P F P P P U P P O | RB2 (designer F; I say P); RB7 (I say U: stranger-versus-stranger theft) |

Agreement: 71 of 90 cells match (79 %). The only FAIL-versus-not-FAIL split is C11 RB2. The 6 RB6 splits are my looser reading of the owner's three examples ("big, impossible, with a stake"). The rubric says taste is raised only by the owner's explicit reasoning about the concept, and no taste log exists. So the designer's U on every RB6 is the better reading, and I do not use RB6 to choose between candidates.

After reading the designer's reasons I accept one change to my own sheet: C05 RB5 should be U (I had no production-cost evidence for creature AI and several nights).

### Where the designer's sheet is not consistent with itself

1. RB9 uses one evidence class two ways. C01 is O on a Roblox letter (2026-07-30) plus 7,380 players at one moment. C07 is P on the same two kinds of evidence (letter plus 19,329 players), and C10 is P with a current count plus a J004 seven-day mean (14,813). Either all are O or all are P. The reasons table does not explain the C07 or C10 P.
2. RB2 closeness to the reference gets three different ratings. C11 is F ("same action, reward and escalation with a new noun", plus a "Steal a ..." title). C01 is P although the note says it is "closest of all to its reference". C05 is P, yet "expression close to its reference (RC42)" is a reason given for not pitching it. No rule in the rubric says where P ends and F starts.
3. C11's F rests partly on its title. A title can be changed; the twist (stars cannot be taken from a base) removes the base raid that defines the reference. I would rate it U and keep it out for RB6/RB7 reasons, not RB2.
4. The "cheapest test for each open risk" table (SKILL.md step 5) has no row for many U ratings: C05 RB6; C06 RB6; C07 RB5, RB6, RB9; C10 RB5, RB6; all of C03 except RB9; and all of C09.

## Verdict

Part 1 passes: 11 of 11 checks (10 of 11 if C4 is read as unverified) and no must check failed. The pitch set meets the brief. It has one miscount (seeds), one weak trend argument, and an independence gap in the critic pass. None of the three breaks a rule.

### Should the same 3 be pitched?

Two of three: yes. One slot: close call, I would not pitch the same set without a stated reason.

- C01 Kick the Meteor and C02 Rob the Sleeping Giant survive my independent rating with the same blocking unknown each (C01 repeat play after the last zone; C02 griefing through the shared noise meter). Both unknowns are cheap to test.
- Third slot: I would pitch C05 Guard the Dragon Egg or, at minimum, explain why C04 Drain the Ocean beats it. On the two rubric criteria that can be rated from evidence, C05 is stronger: its loop proof is the best current evidence of any reference game in the set (96,183 players at the sample, RC48 award), and its open unknown is production weight (RB5). C04 has two open unknowns at the same time, agency (RB4) and phone feasibility of lowering water (RB5), and the second one can end the concept. J004 also calls fishing "residual audiences". The owner already has a water-and-server-goal game (the dam), which the designer notes. The designer's reasons against C05 (heavy production, expression close to 99 Nights) are fair, but the second one is rated P in the table, so the table does not show it. Taste is the owner's: Drain the Ocean may match "Destroy the Sun" better than a night-camp game. That is a reason to show the choice to the owner, not to hide it.
- The recommendation (Rob) is allowed, but the owner should see it plainly: of the three pitches it has the weakest loop proof (P against O and O) and an open social-safety unknown. Its case rests on Steal a Brainrot, whose player-versus-player theft the pitch removes. The designer states this as the strongest objection, so I count it as honest, not a defect.

## Skill gaps (what to change in the kit)

| gap | skill rule | suggested change |
| --- | --- | --- |
| Trend claims compare a peak with one snapshot | `rubric-taste-evidence.md` RB9 row; `idea-method.md` section 5 ("proven loop") and J004 summary rule 04 | Say: to call a loop faded or held, use a time-weighted or matched-weekday value (the J004 7-day peak or mean), never one off-peak snapshot against an event peak. Say what RB9 needs for O. |
| RB9 O versus P has no anchor | `rubric-taste-evidence.md` RB9 | Define O (for example: an official statement or at least two dated observations of the same game) so equal evidence gets equal ratings. |
| RB2 F versus P has no anchor | `rubric-taste-evidence.md` RB2 | Say what separates FAIL from PLAUSIBLE when the twist is close to the reference, and that a title problem is a naming fix, not an RB2 FAIL. |
| RB6 with no taste log | `rubric-taste-evidence.md` RB6 and section 2 | State that RB6 stays UNKNOWN until the owner gives reasoning, and that it is not used to rank. Both the designer and the grader would have agreed. |
| Critic is not independent | `idea-method.md` section 1 step 6 | When the critic cannot be a fresh context, pass it only `candidates.md`, and add the owner context and evidence it needs to that file first. Or let the lead run the fresh critic before the pitch goes out. |
| Each open risk needs a cheapest test | `SKILL.md` step 5 and section 6 self-check | Add a self-check line: "every U or F rating has a row with its cheapest test". |
| No line on why these 3 and not the other survivors | `pitch-template.md` section 4 and `SKILL.md` step 6 | Add: for each survivor not pitched, one line with the rubric reason, and name the reserve with its reason. |
| Count slips (10 seeds against 12) | `idea-method.md` section 1 | Add: recount each step from its table before reporting. |
| Pitch path wording | `evals/briefs.md` check 1.6 | Write "`knowledge/design/concepts/` or the path the brief names". |
