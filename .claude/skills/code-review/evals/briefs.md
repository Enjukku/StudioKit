> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Eval briefs for `code-review`. Give the reviewer the brief and a seeded diff; score the must-pass checks. Each seeded diff contains one planted defect (E-10 contains none; E-12 and E-14 plant several). Revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): common checks C1-C4 and E-06 to E-14 test the rebuilt book's presentation checks (PT rows, `references/presentation.md`); old and new scores do not compare.

# code-review evals

## Common checks (every brief, must pass)
- C1 Goal questions written before the findings, 2-4, each naming an invariant (SKILL.md §3 step 2; `references/review-method.md` §2).
- C2 Reading passes recorded at the review's depth: standard and deep record pass 1 in file order over the whole change and pass 2 in trace order per player path with the failure sweep; a quick review (V-13, e.g. E-10) records pass 1 and the tests (V-15; `references/review-method.md` §2).
- C3 A could-not-check list: per line the step, the missing input, what closes it and who supplies it; empty only when said so (V-16; `references/review-method.md` §5).
- C4 Every runtime claim (timing, rate, feel, what a player sees) is labelled gate-verified, MCP-verified, owner-confirmed or not verified; nothing is passed that its input cannot show (V-10, V-16; `references/presentation.md` §1).

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

## E-06 Sell shows "+N" before the server answers
Seeded diff: a sell button's handler plays the coin burst and a "+50" label, then calls `SellRemote:InvokeServer(itemId)`; the denied return value is ignored.
Must pass:
- Reports PT-01 (High; Critical if the currency is also sold for Robux) with the denied sequence: the server rejects the sale (item locked or already sold) and the player still sees "+50" (`references/presentation.md` PT-01, §3).
- Fix direction: attempt cue in the input handler, outcome layer only in the result handler for that request; a pending state past the slow-answer threshold. Asks for the `Reject` and `DelayMs` run logs or lists them as could-not-check (§4).

## E-07 Buy button enabled from the count-up
Seeded diff: the shop enables Buy when `displayedCoins >= price`, where `displayedCoins` is the tweened counter value.
Must pass:
- Reports PT-03 (High) with the sequence: right after a gain the display lags the true balance (or leads it after a spend), so Buy is wrong for the length of the count-up; logic must read the true server value (`references/presentation.md` PT-03).

## E-08 Reveal windup reads the tier
Seeded diff: a paid egg's client reveal picks a longer, gold-tinted windup when `result.tier == "Legendary"`.
Must pass:
- Reports PT-04 as Critical (policy): the windup code has access to the result and hints at a better outcome; cites `platform-policy` `references/rules.md` §A (one identical windup up to the result frame) (`references/presentation.md` PT-04, §3).
- Requests the lowest-vs-highest frame compare from the UI designer or lists it as could-not-check.

## E-09 Another player's hit shakes my camera
Seeded diff: a client `HitConfirmed` handler shakes the camera on every hit in the server, whoever the attacker; the shake has no reduced-motion or shake-setting branch.
Must pass:
- Reports PT-06 (High): another player's event moves my camera; camera effects only from the local player's own events.
- Reports PT-09 (Medium): the shake asks no comfort setting and has no reduced path (`references/presentation.md` PT-06, PT-09, §3).

## E-10 Clean data-only change (calibration)
Seeded diff: two new rows in an item data table (name, price, icon id) in the existing shape, read by unchanged code; the tests load the table.
Must pass:
- Verdict "no blocking findings" with a keep list (`references/review-method.md` §5; SKILL.md §7 principle 18; `references/worked-examples.md` WE-3).
- Fails if any finding is invented (a severity on a nitpick, a demanded abstraction or extra test).

## E-11 Two hit-stops on one track
Seeded diff: hit-stop saves `track.Speed` into `previous`, calls `AdjustSpeed(0)`, and after the timer calls `AdjustSpeed(previous)`.
Must pass:
- Reports PT-08 (High) with the sequence: a second hit lands during the first stop, saves `previous = 0`, and its restore leaves the track paused; fix direction: one owner per track, a stop-until time, the base speed (`references/presentation.md` PT-08).

## E-12 Presentation decides gameplay
Seeded diff: (a) a sword's client `GetMarkerReachedSignal("contact")` handler calls `humanoid:TakeDamage(20)` on the touched enemy; (b) a quest reward tween's `Completed` handler fires a remote that grants 100 coins.
Must pass:
- Reports PT-18 for both: (a) damage decided by a client marker (High); (b) a grant decided by a tween's `Completed` (Critical, money) (`references/presentation.md` PT-18, §3).
- Names that `Completed` also fires on `Cancel`, so a cancelled tween still grants the coins; fix direction: the handler sends an intent at most, the server decides on its own clock and hit test.

## E-13 Ungated test hook
Seeded diff: a server combat script reads `ServerStorage.TestHooks.Outcome` and, when set, forces the hit result; no `RunService:IsStudio()` gate.
Must pass:
- Reports PT-19 as Critical: an attribute set in Studio is saved with the place, so the forced `Outcome` acts on live servers; fix: gate every read behind `IsStudio()` and keep the hook out of the default project file (`references/presentation.md` PT-19, §3).

## E-14 Comfort module missing settings
Seeded diff: a comfort module exposing only `reducedMotion()` and `shakeScale()`; a low-health red flash gated on `GuiService.ReducedMotionEnabled`; a full-screen damage tint that asks no setting.
Must pass:
- Reports PT-09 three times (Medium each): the module does not answer flashes, screen effects and clarity from the contract's five settings; the flash asks the wrong setting (motion, not flashes); the tint asks none (`references/presentation.md` PT-09, §3; `architecture` `references/presentation-contract.md` §4).
