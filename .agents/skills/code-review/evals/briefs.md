> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `code-review`. Give the reviewer the brief and a seeded diff; score the must-pass checks. Each seeded diff contains one planted defect.

# code-review evals

## E-01 Double reward after a wait
Seeded diff: a quest handler checks completion, yields on a save, then grants coins without re-checking.
Must pass:
- Reports the race (two requests both pass the check during the yield) with the sequence, file:line and a fix direction (atomic update or completion id).

## E-02 Client price
Seeded diff: `buyItem(itemId, price)` uses the client's price.
Must pass:
- Top-severity finding under harm area 2/3; cites the networking-security rule.

## E-03 Leak on respawn
Seeded diff: a `CharacterAdded` handler connects `Humanoid.Died` and a Heartbeat loop with no cleanup.
Must pass:
- Names the missing lifetime owner; suggests a respawn ×20 test.

## E-04 Invented API
Seeded diff: calls `Players:GetPlayerFromCharacterAsync()` (does not exist) and `wait(1)`.
Must pass:
- Checks the API reference and reports the invented call; flags `wait` with its `task.wait` replacement.

## E-05 Tests that cannot fail
Seeded diff: a migration plus tests whose expected values were copied from the migration's own output.
Must pass:
- Reports that the tests mirror the code; asks for brief-owned expected results and a future-schema fixture.
