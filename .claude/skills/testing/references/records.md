> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Sources: owner engineering paper §9-§11 (P319, P323-P334, P348), fact-checked; the first game's rework study method (`knowledge/reference/engineering/rework-study.md`).

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
2. What behaviour was checked, and how (counts: passed / total)?
3. What was not checked, and why (BLOCKED, NOT RUN)?
4. Did performance or memory change on the named target (numbers, where measured)?
5. Does the change touch saves, money or anything players pay for?
6. First attempt or repaired (how many rounds)?
7. What should the owner do now (approve, play-test, decide)?
Attach the revision, the logs and capture paths. A green result whose meaning depends on unspoken exclusions is not allowed.
