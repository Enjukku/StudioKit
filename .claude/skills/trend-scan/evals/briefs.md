> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20. Kit evals: universal (J004 step 5). Graded by a separate agent (Sonnet, high) that does not see the skills' authoring notes. The hidden inputs and expected answers for E4 and E5 live in `knowledge/jobs/J004-trend-scout/hidden-cases.md` (lead and grader only; never give that file to the trend-scout).

# Eval briefs: trend-scout (skills market-trends + trend-scan)

Pass rule: an eval passes when every must-pass check passes. The agent passes the set at ≥ 4 of 5 evals (job card J004).

## E1 — Label the numbers (open)
**Brief:** "Here are four numbers for one Roblox game, from one week: players online now 4,210 (Games API, 14:02 UTC); visits 12,400,000 (Games API); estimated revenue 85,000 Robux/day (a tracker page); 24 h mean 3,900 vs 7-day mean 2,100 (our store). Write the rising-games row and one sentence for the owner."
**Must pass:**
- [ ] Each number carries one label: OFF, OFF, 3P-E (vendor named or "vendor not given", range or "range not given", accuracy UNKNOWN), DER.
- [ ] The 3,900 / 2,100 ratio is called momentum, not week-over-week growth.
- [ ] No conversion of CCU or visits into daily users, players or money.
- [ ] The owner sentence keeps the doubt ("third-party estimate") and gives no profit claim.

## E2 — Is it a breakout? (open)
**Brief:** "Our store has 15 days of samples for universe 123. Last complete week: mean 1,800, coverage 84 %, longest gap 3 h. Week before: mean 900, coverage 97 %. A big YouTuber posted a video about the game on day 12. Flag it or not, and say what to check."
**Must pass:**
- [ ] No automatic breakout flag: coverage 84 % is under the 90 % gate (PROPOSAL) and a 3 h gap exists.
- [ ] g7 = +100 % is shown with added CCU +900 and with the coverage caveat.
- [ ] Names the creator video as an alternative explanation and asks for troughs / independent creators / next week.
- [ ] Calls the thresholds PROPOSAL, not platform rules.

## E3 — Copying a loop (open)
**Brief:** "The game-designer wants a fishing-collection game with the look of a popular anime and the name 'Fisch Legends'. Give the rights and policy gate for the opportunity card."
**Must pass:**
- [ ] The abstract loop (catch → sell → upgrade → rarer pools) may be borrowed (ideas and methods of play are not protected by U.S. copyright).
- [ ] The anime look and characters: HOLD unless licensed; the name: fail (confusing with an existing game, trademark risk, Roblox discovery penalises look-alike metadata).
- [ ] Asks for a twist a new player meets in the first session and for independently made assets.
- [ ] Does not give a "safe copying percentage".

## E4 — Timing and "too late" (hidden: HC-A5..A8 and section B)
**Brief:** the inputs of section B in `hidden-cases.md` only, plus the cut-off date.
**Must pass:**
- [ ] Days since each recorded peak computed correctly and called "time since the recorded (sampled) maximum", not a trend lifetime.
- [ ] All three theses are too late for an "early original wave" claim.
- [ ] Says this is about timing, not zero demand; durable families (fishing, PvP, survival) can still carry an original game with current evidence.
- [ ] Rejects thesis 4 (a new sub-mechanic claimed early with no dated evidence) as not supported.

## E5 — Three candidates from tracker data (hidden: HC-C1..C5)
**Brief:** the section C input table in `hidden-cases.md` only, with "Give the top 3 opportunities and score them."
**Must pass:**
- [ ] Momentum computed (+233.9 %, +174.9 %, +99.4 % from rounded inputs) and labelled overlapping, not week-over-week; inputs labelled 3P-S.
- [ ] Gives 3 research entries (cards, or emerging leads per `opportunities.md` §4b since the games are young), each with a loop (hypothesis allowed), an original theme direction and its own main doubt (bought traffic; loop not yet inspected; source inspiration needs rights-aware difference), in research-priority order with the tie-break stated; never a launch order.
- [ ] Refuses a full weighted total: gives known points, lower–upper range and completeness instead.
- [ ] Tracker "created" date is not a launch date; no revenue, retention or profit claim.

**Leak note (lead):** two of the E5 games appear by name in the paper's loop catalogue (RP:150-151), which is in `knowledge/reference/trends/01-roblox-data-loops.md`. The skills do not name them. E5 therefore tests method (labels, windows, refusal to score), not recall. The three-month build figure of HC-A3 is also visible in the notes, so HC-A3 is not used.
