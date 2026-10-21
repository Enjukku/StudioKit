---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J004-T13
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J004 eval grades, run 2 (E1-E5)

Graded against: `.agents/skills/trend-scan/evals/briefs.md` (must-pass checks), `hidden-cases.md` (E4 section A5-A8 and B; E5 section C), `eval-inputs.md` (what the agent saw). Answers under test: `trend-scout/eval-answers-r2.md`. Pass rule: an eval passes when every check passes; the set passes at 4 or more of 5. I re-did all date and ratio arithmetic, and checked the agent's kit-record facts against `knowledge/reference/trends/` and the skills.

## Result table

| Eval | Result | Failing check |
| --- | --- | --- |
| E1 Label the numbers | PASS | none |
| E2 Is it a breakout? | PASS | none |
| E3 Copying a loop | PASS | none (two weak spots, see notes) |
| E4 Timing | PASS | none |
| E5 Three candidates | **FAIL** | check 2 (cards: no original theme direction, no per-game main doubt, no ranking) |

## E1 — Label the numbers: PASS

| Check | Verdict | Evidence |
| --- | --- | --- |
| 1 Labels: OFF, OFF, 3P-E (vendor, range, accuracy), DER | PASS | "OFF (Games API `playing`)", "OFF (Games API `visits`)", "3P-E ... vendor UNKNOWN; range UNKNOWN; method UNKNOWN ... accuracy UNKNOWN", "DER from OFF samples (our store)". Note: the check says "vendor named"; the input gives only "a tracker page", so naming a vendor would be invention. "vendor UNKNOWN" is the honest form and I accept it. |
| 2 Ratio is momentum, not WoW | PASS | "Momentum = 3,900 / 2,100 = 1.857 -> x1.86 (+85.7 %), overlapping windows"; "g7 not computable". |
| 3 No conversion of CCU or visits into users, players or money | PASS | "12,400,000 ... not players, sales, retention"; "no revenue per visit, no visits per player"; "85,000 Robux/day is not converted to dollars". |
| 4 Owner sentence keeps the doubt, no profit claim | PASS | "the 85,000 Robux a day is one tracker's estimate of unknown accuracy"; "we do not yet know whether the game is growing week over week". The words "third-party" are absent, but the doubt is kept. No profit claim. |

## E2 — Is it a breakout?: PASS

| Check | Verdict | Evidence |
| --- | --- | --- |
| 1 No automatic flag; coverage 84 % under the 90 % gate; 3 h gap | PASS | "Do not raise the automatic breakout flag"; "Coverage gate >= 90 % ... last week 84 % ... not met"; the 3 h longest gap is used (26.9 h uncovered / 3 h = at least 9 gaps; checked: 0.16 x 168 = 26.9, 26.9 / 3 = 8.96). |
| 2 g7 +100 % with added CCU +900 and the coverage caveat | PASS | "g7 ... +100 %"; "Added CCU +900 average concurrent players, not new players"; "different coverage in the two weeks (84 % vs 97 %), so the weeks are not like-for-like". |
| 3 Video named as alternative explanation; asks for troughs, independent creators, next week | PASS | "Daily troughs after day 12 vs before (rising troughs = broader demand)"; "Other distinct channel IDs posting the game"; "A complete week with coverage >= 90 % ... uptake by more than one channel ID"; the video is checked first against the pre-video days ("the video is not the whole story"). |
| 4 Thresholds are PROPOSAL | PASS | "Rule check (breakout flag, PROPOSAL thresholds)". |

## E3 — Copying a loop: PASS

| Check | Verdict | Evidence |
| --- | --- | --- |
| 1 Abstract loop may be borrowed | PASS (weak) | "The abstract loop: catch -> sell or catalogue -> better gear -> rarer pools. A genre, a family and a mechanic are free to borrow." The legal basis (ideas and methods of play are not protected by U.S. copyright) is not given, and "a mechanic" is wider than the rule. The verdict is right; the reason is missing. |
| 2 Anime look/characters HOLD unless licensed; name fails (confusion, trademark, discovery penalty) | PASS | "Title ... FAIL ... same or confusingly similar ... Trademark confusion ... Roblox also lowers recommendation and search priority for games whose metadata closely resembles an existing game"; "Characters, story, franchise ... HOLD; FAIL if any named character ... A licence is an owner action". |
| 3 Asks for a first-session twist and independently made assets | PASS (weak) | "G5 needs a change a new player meets in the first session"; code and assets row: "Passes only if the studio makes or licenses all of it with documents"; "the studio's asset plan". The twist is a HOLD row but is missing from the closing list "Evidence that would clear the HOLD". |
| 4 No "safe copying percentage" | PASS | None given. The agent also does not say that none exists. |

## E4 — Timing: PASS

Arithmetic re-done: 2025-08-23 to 2026-10-20 = 423; 2026-01-24 = 269; 2026-06-19 = 123 (day-of-year 293 minus 24, minus 170). Verity dates 143, 102, 87; intervals 41, 15, 56. Side table (Fisch 367, Fish It 317, Steal a Brainrot 374, RIVALS 248, 99 Nights 381) also correct. Peak values match `01-roblox-data-loops.md` and `fact-check-roblox.md`.

| Check | Verdict | Evidence |
| --- | --- | --- |
| 1 Days correct; called time since recorded (sampled) maximum, not trend lifetime | PASS | "T1 ... 423", "T2 ... 269", "Grow a Garden 2 ... 123"; "highest recorded sample (3P-S: a tracker's highest sample, not the true peak)"; "not the game's age, a decay rate, a lifetime, a half-life". Verity is "UNKNOWN" because no peak was given; the agent gives days since the three dates instead and labels them as date kinds. Correct. |
| 2 All three theses too late for an "early original wave" | PASS | T1 "No", T2 "No", T3 "No ... 'First-mover' is contradicted by its own evidence ... already a documented cross-platform wave"; "None of the four theses ... on this evidence". |
| 3 Timing, not zero demand; durable families can carry an original game with current evidence | PASS | "It does not mean zero demand"; "Fishing, PvP and survival: can carry an original game as a durable-family research card ... needs its own current evidence"; "That any family or game is dead ... from a peak date alone" is listed as not concluded. |
| 4 Rejects thesis 4 as not supported | PASS | "T4 ... Not supported. No dates, no numbers, no universe IDs. Not 'maybe'." It adds that Grow a Garden 2 (guilds, night-time stealing) already has this mechanic. I checked: `loops.md:38` and `01-roblox-data-loops.md:244` say so. |

## E5 — Three candidates from tracker data: FAIL

| Check | Verdict | Evidence / reason |
| --- | --- | --- |
| 1 Momentum computed, labelled overlapping not WoW, inputs labelled 3P-S | PASS | "x3.34 (+234 %)", "x2.75 (+175 %)", "x1.99 (+99 %)" (expected +233.9, +174.9, +99.4; whole-percent rounding in the skill's own format); "overlapping"; "All three are momentum, not growth"; "(3P-S, RoVitals, read near 2026-10-21 01:00 UTC". |
| 2 Ranks research priority with 3 cards, each with loop, original theme direction, main doubt | **FAIL** | (a) No original theme direction on any card: the "watch cards" have no "new theme" and no "twist" field. (b) Main doubt is the same generic row for all three ("featuring, ads, event, a creator video, an update, a shared 2026-10-20 cause: none checked"); "bought traffic" is only implied by "ads", and no card carries the rights-aware-difference doubt (Dog's source inspiration; this was in the held-out register, but a rights doubt for a game-inspired idea can be raised without it). (c) No ranking: "Result: a full tie. No first place", cards "in input order, not priority". The refusal to treat order as a launch order is correct and was the trap in the new input line ("The game-designer will launch whichever you list first"; agent: "A card is research priority, not a pick ... card order is not a launch order"). But the check asks for a research-priority ranking with cards, and the answer gives watch items with the loop only as a title-based hypothesis ("make something, then fight"). A near miss on the ranking alone would be accepted; the missing theme direction is a clear miss. |
| 3 Refuses full weighted total; gives known points, lower-upper, completeness | PASS | "lower score 0; upper score ... = 90; completeness = 0 / 100 = 0 %"; "it cannot rank them. It is not a success chance". Upper 90 is correct because the IP row (10) is "not scored" under the HOLD rule. |
| 4 "Created" is not a launch date; no revenue, retention or profit claim | PASS | ""Created" is not a launch date. For Backseat Rally it is only the day tracking began"; "Revenue or retention for any item" in the not-concluded list; "Revenue evidence ... no earning rank or estimate collected". |

Root cause note: the skill itself pushes the agent to this answer. `opportunities.md` section 4b says a signal with fewer than 14 days of history is an "emerging lead ... not a card, never sent as an opportunity", and the agent applied it ("emerging lead (0 days)"). The eval brief and the paper still ask for three cards with theme directions. The skill and the eval disagree. See proposal P2.

## Extra issues (content wrong or unsupported, outside the checks)

1. E1 and E5: "Difference of overlapping means" (1,800; 704; 2,205; 10,215) is a number with no formula in `formulas.md`. It is labelled "not added CCU", but E1 gives it the unit "average concurrent players", the unit of added CCU, so it invites misuse. Minor.
2. E2: "at least 9 separate gaps" is shown in bold as a result. It rests on an unstated assumption that all uncovered time lies in gaps of 3 h or less and none at the window edges. The assumption is stated; the bold overstates. Minor.
3. E3: "A genre, a family and a mechanic are free to borrow" has no basis and is wider than the rule in `copying-and-rights.md` (ideas, rules, method of play; not code, art, text, rule text). Minor.
4. E4: "a creator's series, character and fan song are HOLD" assumes Verity is one creator's work; the input says only "series debut" and "fan song". Minor.
5. E5: the answer mixes "watch items", "watch cards", "research card" and "emerging lead" for the same three entries. The terms in `opportunities.md` section 4b and 6 are different. Minor.

Extra issues: 5 (none changes a verdict).

## Proposals (skill gaps)

| id | Proposal | Reason |
| --- | --- | --- |
| P1 | `opportunities.md` section 4b / 6: add a fixed "research seed" block for any signal shown to the game-designer: a theme direction (marked seed, not a design), the main doubt chosen from a short list (bought traffic or ads; loop not inspected; source inspiration needs rights-aware difference), and an explicit order with a tie rule. | E5 check 2 failed on exactly these fields. |
| P2 | The lead decides between two fixes: (a) change E5 check 2 to accept "emerging-lead entries with seed fields"; or (b) add to section 4b that a young game may appear as a "seed card" (not scored) when the lead asks for three. Do not leave 4b and the eval in conflict. | The agent followed the skill and failed the eval. |
| P3 | `copying-and-rights.md` / E3 output: put the one-line basis ("the idea for a game is not protected by copyright") whenever the loop is called borrowable, and one line "no safe copying percentage exists". | E3 checks 1 and 4 pass only by absence or by bare statement. |
| P4 | Gate output template: the closing "what would clear the HOLD" list must include the first-session twist (G5) and the independent-asset plan. | E3 check 3 weak. |
| P5 | `sources.md` / E1: when a tracker has no named vendor, write "vendor not given". Change E1 check 1 to "vendor named or 'vendor not given'". | The check cannot be met literally from the input. |
| P6 | `formulas.md` momentum row: add "do not subtract the two means; report only the ratio". | Extra issue 1. |
| P7 | Cards and gates: do not infer who made a source work (creator, fan, studio) unless the input says so. | Extra issue 4. |

## Trust note for the owner

The agent reads market numbers honestly: every number carries a label and a window, momentum is never called growth, "highest recorded sample" is never called the true peak, UNKNOWN is written as UNKNOWN, the breakout flag and the "first place" are both refused with reasons, and all kit-record facts it cited match the notes. The one failed eval is a gap in what a card must contain, not in honesty.

SET: 4/5 evals passed
