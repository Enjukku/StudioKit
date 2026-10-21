> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20. Kit reference: universal (J004). Evidence: owner research paper, notes `knowledge/reference/trends/02-outside-access-scoring.md` (**N2**) §8-§11 and `01-roblox-data-loops.md` (**N1**) §13-§14. Tags: **O** = paper or kit method (OPINION), never a measured predictor. Every cut-off here is **PROPOSAL** until backtested or owner-approved.

# Opportunities: from signal to a research card

## 1. What an opportunity is
An opportunity is a **rising player behaviour** with dated evidence, a **proven loop** it runs on, and a **remaining time window** the studio can still use (N1 §0, RP:5 O). A popular name alone is not an opportunity. The scout ranks **research priority**; the game-designer turns a card into pitches; the owner decides. The scout never designs the game and never claims a green light.

## 2. Gates first (all must pass before any score)
| Gate | Pass when | Fail or unknown → |
| --- | --- | --- |
| G1 Evidence | Evidence was collected through an allowed route (registry row "allowed" or "manual") | drop the evidence, not just the score |
| G2 Original | The studio can make the content itself or holds a licence | HOLD the branded version; an original design on the same abstract loop may continue |
| G3 Audience and policy | The theme and loop fit Roblox rules and the intended age group (`platform-policy`) | HOLD or fail |
| G4 Scope | A credible technical scope exists (designer or architect estimate, not the scout's guess) | mark "scope unknown"; card stays research-only |
| G5 New decision | The twist changes a player decision, a stake, cooperation or expression (not just a noun), and a new player meets it in the first session | not an opportunity yet |

An unknown IP right is **HOLD**, not a small minus that a big trend can outweigh (N2 §9, RP:367 O). On HOLD, do not score the IP row at 0 as well: report the HOLD once (N2 §13 item 11).

## 3. Score (only after the gates)
Rate each dimension 0-5. Score = Σ (weight × rating / 5), max 100 (N2 §9 O).

| Dimension | Weight | 0 | 3 | 5 |
| --- | ---: | --- | --- | --- |
| Growth speed and persistence | 18 | falling, or one spike | positive non-overlapping week growth with ≥ 90 % coverage | growth in several weeks in a row, troughs rising |
| Addressable demand | 10 | below the studio's test economics | enough relevant players for a small test | broad relevant audience in independent signals |
| Revenue evidence | 15 | contradictory or none | official earning rank held over time; cash UNKNOWN | authorised unit economics (own data or owner disclosure) |
| Audience and device fit | 10 | cannot reach or wrong audience | fits one named cohort and touch controls | tested appeal on every target device |
| Build feasibility and timing | 15 | high-case build longer than the window | existing systems cover a scoped launch | prototype works; plan leaves learning time |
| Room and difference | 12 | many close copies, no new decision | clear first-session twist and a gap | gap confirmed by competitor review and tests |
| IP and policy certainty | 10 | (gate HOLD: do not score) | original content, dependencies checked | rights and policy documented |
| Staying power | 10 | rests on a passing meme | a return reason that does not need the meme | several tested reasons to return |

Ratings 1, 2 and 4 sit between the anchors; write one line on why (the paper anchors only 0, 3, 5: N2 §13 item 10).

**UNKNOWN is never a neutral 3.** For each UNKNOWN dimension publish the **lower score** (rating 0) and the **upper score** (rating 5), plus **completeness** = assessed weight / 100 (RP:369 O).

| Result (PROPOSAL) | Action |
| --- | --- |
| lower score ≥ 75, all gates pass, completeness ≥ 80 % | may go to the game-designer as a "prototype candidate" |
| upper score ≥ 60, or wide range | research or playtest ticket |
| upper score < 60 | watch or reject |
| upper ≥ 75 but completeness < 80 % or a gate HOLD | research ticket; name the missing evidence |

Use the **lower** score for the top band and the **upper** score for the watch line, so missing data never promotes a card (lead rule, closes N2 §13 item 9). A score is not a success chance: an 85 is not 85 % (RP:383 O).

## 4. The card (9 record fields + card fields)
The game-designer's intake (`game-concept/references/idea-method.md` §2) needs these 9 fields for every opportunity: observation date · rising player behaviour · audience · evidence (source, metric, date) · comparison period · outside trigger · alternative explanation · proven loop · lasting or temporary. The weekly template (`templates/trends/weekly-report.md` §2) adds: new theme, twist, money, competition, rights gate, score, smallest test, decision owner and next review.

**Smallest test** (RP:385 O): hypothesis · audience · first-session promise · new decision · reusable systems · high-case delivery · evidence still needed · time/cost cap · success signal · guardrail · stop condition · next review date. Success signals come from the studio's own economics and baseline; never an invented universal D1 or CCU target.

## 4b. Emerging lead (before a card is possible)
For a signal with < 14 days of our history, one sample, or a single source. Not scored, not a card, never sent as an opportunity.
| Field | Value |
| --- | --- |
| ID and name | universe / app / channel ID; name as the source shows it |
| What was seen | number(s) with label, window and read time |
| Loop | hypothesis from title/description, or observed |
| Why it might matter | one line |
| Missing evidence | e.g. 2 complete weeks of samples; independent creators; gameplay inspection |
| Theme direction | "original theme required" + what to stay clear of (the source game's name, characters, look) |
| Main doubt | one or more from: bought traffic or ads · featuring or an event · loop not inspected · source inspiration needs rights-aware difference · single source |
| Rights gate | not checked / HOLD + reason |
| Next check | date and what will be read |

Order leads by M-16 (evidence quality, breadth, completeness); if still tied, the larger measured level first (more players = more evidence to inspect), and say it is a tie-break, not a pick.

## 5. Timing and "too late"
- No typical trend lifetime exists (survivor bias, censored dates, events not comparable: N2 §8 O). Do not write "trends last N weeks".
- **Remaining window** = conservative date when demand falls below the studio's threshold − today. **Slack** = window − high-case build time − learning time after launch (RP:354 O). Until the threshold is set by the owner, slack is qualitative: "ample / tight / negative".
- Negative slack → suggest an update or event in an existing game, a reusable prototype, or reject (RP:354 O).
- **A narrower claim needs its own dates.** "A new sub-mechanic / a regional audience / an underserved niche is still early" is rejected unless it comes with its own dated, labelled evidence (a rising series, named universe IDs, creator breadth). Without it, write "not supported", not "maybe".
- **Too late for an "early wave" claim** when dated mass adoption already happened: the record peak of the reference game lies months back, or the theme is already a documented cross-platform wave. This does not mean zero demand: a durable family (fishing, PvP, survival) can still carry an original game, which needs its own current evidence.
- Half-life only on a falling, event-free weekly series: half-life = ln 2 / |decay slope of ln(signal)|. Never fit it to a rising curve (RP:352 O).

## 6. Three cards, never three green lights
- At most 3 cards; fewer when fewer are defensible. "No qualified build opportunity" is a valid week (RP:408 O).
- Each card names the evidence that would kill it.
- Next week, every card gets a line in "Fading, rejected and wrong last week" or stays with new evidence.
