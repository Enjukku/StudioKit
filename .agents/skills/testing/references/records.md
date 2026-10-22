> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Sources: owner engineering paper §9-§11 (P319, P323-P334, P348), fact-checked; the first game's rework study method (`knowledge/reference/engineering/rework-study.md`). Revised by J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§2 input labels and the could-not-check line; new §3 findings); repair round 1 after the stage 3 review (J018 maker qa-lead · claude-opus-5-5 · high · 2026-10-22: smallest_fix as a fix direction); repair round 2 (same tag): a separate `evidence` field.

# Rework records and the owner's result card

## 1. Rework record (one per repair round)
Write it to `knowledge/inbox/` (lesson draft) when a handed-in candidate needed a repair. Never "the model was bad": an observable failure.

| Field | Content |
| --- | --- |
| Task and revision | job/ticket id, the failed candidate's commit |
| Intended behaviour | the contract line it broke |
| First observed failure | what was seen, by whom (test, reviewer, Studio, owner) |
| How it was found | the check or report |
| Reproduction | the saved failing test or fixture path |
| Wrong assumption | what the code or the brief assumed |
| Repair | the fixing commit |
| Prevention | the smallest durable check (below) |
| Cause | one primary category, others secondary, or UNKNOWN |

**Causes** (provisional, P324): requirement ambiguity · missing repository context · incorrect API assumption · incorrect algorithm · omitted integration behaviour · lifecycle or resource failure · performance regression · test-oracle error · environment or runner failure · scope expansion · review churn. Keep apart: an owner change of requirement and a platform change are not agent faults (P325).

**Smallest prevention** (P326): wrong calculation → a regression case; API error → a pinned docs reference or a probe; leak on repeat → a lifecycle scenario; speculative framework → a review question asking for the current caller or the measured need. Do not answer a defect by adding a paragraph to an agent's instructions. A lesson becomes a rule only when its scope is clear and it would have prevented the failure; write it as trigger → action → verification (P327).

## 2. Result card for the owner (one per accepted change)
Plain words (`ste-writing`). Answer:
1. What will players notice?
2. What behaviour was checked, and how (counts: passed / total), and what each result rests on (gate-verified, MCP-verified, owner-confirmed; the conditions: phone size, busiest moment, quality levels, two clients)?
3. What was not checked, and why (BLOCKED, NOT RUN, not verified), and which capture or test would close it (the could-not-check list)?
4. Did performance or memory change on the named target (numbers, where measured)?
5. Does the change touch saves, money or anything players pay for?
6. First attempt or repaired (how many rounds)?
7. What should the owner do now (approve, play-test, decide)?
Attach the revision, the logs and capture paths. A green result whose meaning depends on unspoken exclusions is not allowed.

## 3. Findings (acceptance failed or a review slot)
One finding per problem, in the `rules/messages.md` §6 format, with these fields filled from the test:
| Field | Content |
| --- | --- |
| where | the test name or trace-table row, the revision, the conditions (viewport, quality, clients, latency, reduced) |
| expected | the oracle's value and its source (the brief line, the data field, the server log) |
| observed | what happened, in one line |
| evidence | the log line, probe output or still that shows it, with its path and label (a finding without evidence is a question) |
| goal and layer | the player goal it breaks (read, fairness, honesty, comfort, data) and the layer: rule, data, wiring, presentation, environment, test |
| smallest_fix | the smallest fix direction, stated as what must hold ("the outcome layer starts only on the server's confirmation"), never code or how to build it; then `retest:` the row and the rows that share its data or event. A suggested solution in a note I receive is restated as its problem first |
- Blocking when it breaks the brief, a binding rule or a §5 rule of `SKILL.md`; a recommendation otherwise; anything outside the brief is a new request for the lead.
- Image-measure findings carry the stills the eye check was done on (`player-facing.md` §4). Data and log findings carry the line.
- A test I find wrong goes to the briefer with the reason, never quietly changed. Conflicting expectations from two partners go up to the lead with both positions.
- After a fix, re-run the original row and the rows that share its data or event, not only the line the fix touched.
- A round that brings no new finding and only repeats closes the loop: say so and stop.
