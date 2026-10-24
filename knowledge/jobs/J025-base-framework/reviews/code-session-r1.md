---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: Session code rev 1 (J025-R-Session), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\src\Session\` (repo uncommitted by rule 7; revision = the sha256 below). Depth: deep (saves, purchases). Round 1. Code and vendor read before `evidence/Session.md` and `test-plans/Session.md`.

Goal questions: (1) Can any sequence of leave, rejoin, failing store, steal, crash or shutdown lose or duplicate an accepted update (S1, S2, S10, S12)? (2) Is a purchase granted at most once and confirmed only after a save holding its id landed (S10, D-11, CC-4)? (3) Do GWS v0 and DS v1 saves load, migrate and stay byte-identical when nothing changed (S7, S8, F9)? (4) Does any player end `degraded`, `closed` or kicked when the contract says `ready` (S9, S12, T-8)?

## Files reviewed (sha256)

| File | sha256 |
| --- | --- |
| src/Session/init.luau | 359dbebc2de8deac3bb853f8c0ead89d326ba2d8c50c14e20efc0acdc414a8b5 |
| src/Session/Data.luau | 9b66b8417044aa74971b3b0366e1724a2513e9fadef8085dce363264289c4787 |
| src/Session/test/FakeWorld.luau | 1b760d1c243824130ccd65c58bc55c3d86c668131abfc837040a3ab16db0ee9e |
| src/Session/test/Fixtures.luau | 2c0801017c208e79fa4b4e9f89c761dd11299ee03b823da2f013756f1f9768d6 |
| vendor/ProfileStore/init.luau (1.0.3, unpatched, `PATCHES.md`: none) | 799263dc0d281f360432e172f57ef337761ec38482575273b3cb079d114ecf71 |

Hashes equal QA's trace table (`test-plans/Session.md` §1).

## Runs (2026-10-24)

| Run | Result (last lines) | Label |
| --- | --- | --- |
| `python tools/gate.py` | `PASS specs 13.9s 33 files, 275 passed, 0 failed` · `SKIP engine 10 Jest specs, Studio lane only` · `RESULT: PASS` (src/Net now passes too) | gate-verified |
| `lune run tools/spec/run.luau src/Session tests/acceptance/Session` | `specs: 13 files, 84 passed, 0 failed` | gate-verified |
| Scratch copy, 2 probe specs added (F1, F2 sequences below), candidate code unchanged | `FAIL ... R gold kept: expected 43, got 42` · `FAIL ... T8 rejoined player ready: expected "ready", got "degraded"` · `specs: 11 files, 42 passed, 2 failed` | Lune probe (FakeWorld runs the real ProfileStore), not engine |
| Same scratch copy with both fix sketches below applied | `specs: 14 files, 86 passed, 0 failed` (84 existing + 2 probes) | Lune probe; scratch deleted after the run |

## Findings (most harmful first)

### F1 · blocking · Critical · harm 1 (lost save) · S1, S2, D-04
- **where:** `src/Session/init.luau:187-191` (load starts a session with no wait) with `:257-269` (leave: `EndSession` and forget); vendor `init.luau:1462-1489` (same-server rejoin: `IsThisSession` true at `:1469`, so the new load takes the record as it is), `:755-760` (the old release writes only if `SessionLoadCount == load_index`, `:759`).
- **observed (sequence):** player ready on server S with saved gold 42 → update to 43 (in memory, not yet autosaved) → leaves; `EndSession` starts the release save, which fails (5xx, or 304 queue full) and backs off 1, 2, 4, 8 s (vendor `:927-930`) → the store answers again → the player rejoins **the same server** before the release retry → new load's `UpdateAsync` sees `ActiveSession` = this server, takes the record (gold 42) and bumps `SessionLoadCount` → the release retry then finds the count changed and writes nothing. The player plays on 42; every later save writes 42. Gold 43 (all progress since the last landed save, up to the 300 s autosave) is gone for good, silently. Probe: fail every UpdateAsync for the key for 10 s after leave, rejoin at +12 s → rejoin `ready` with 42, record 42 after the second leave.
- **expected:** an accepted update survives a leave whose save the store eventually takes (contract failure table, "Errors / throttling during autosave or leave save: ... data stays in memory until the session ends"; S2 "load = lock" should not load a record this server has not finished writing).
- **evidence:** code read (D) + scratch Lune probe on the candidate (FakeWorld loads the unpatched vendor). Not covered by A1-A25 (no same-server rejoin after a failed leave save).
- **smallest_fix:** Session keeps a per-UserId "release pending" mark: set in `onLeave` before `EndSession`, cleared by that profile's `OnAfterSave` (it fires after the release lands, vendor `:924`); `load` waits while the mark is set and the entry is still `loading` (the 120 s timer still applies: a release that never lands ends `degraded`, never stale). About 8 lines; the sketch passed all 84 specs.
- **protect:** leave mid-load still `closed` with no lock (S-T13); the 120 s timer and `Cancel` still end the wait; no mark left after a landed release (S-T14 counts); shutdown unchanged.
- **retest:** new Lune spec (StoreFailure): "leave save fails 10 s, rejoin same server at +12 s: rejoined data and record keep 43"; plus the 1,000-cycle leak spec.

### F2 · blocking · High · harm 4 (wrong degraded) · S2, S9 · T-8 confirmed
- **where:** `src/Session/init.luau:187-201` (a nil from `StartSessionAsync` while still `loading` → `degrade("load_failed")`); vendor `init.luau:1426-1446` (the second call steals the first call's job result), `:1455-1460` + `:1495-1501` (the cancelled first call's transform takes no session), `:1601-1605` (`ActiveSession` not a table → `return nil`).
- **observed (sequence):** join → load A's `UpdateAsync` is throttled (6 s) → player leaves at 1 s (A's `Cancel` true) → rejoins the same server at 2 s → load B finds A's job and waits for its result → A's transform runs with `Cancel` true and takes no session (record `ActiveSession` nil; also when another server holds it) → B gets that result and returns nil → Session degrades the present player: whole session on the template copy (shows zero progress), no saves, purchases `NotProcessedYet`. Probe: `degraded at 6.12 s`, log `load_failed: 7: no session`.
- **expected:** the rejoined player loads and reaches `ready` (failure table: only a load that fails for 120 s ends `degraded`).
- **evidence:** code read (D) + scratch Lune probe on the candidate; maker probe in `evidence/Session.md:66` agrees.
- **smallest_fix (the lead's idea holds):** retry `StartSessionAsync` while it returns nil, the entry is still `loading` and `ProfileStore.IsClosing` is false, with `task.wait(1)` between calls (a nil can come back at once, e.g. "another session tried to load", `:1593-1595`); the 120 s timer and leave end the loop through `Cancel`. Keep the after-call check that ends a late profile. Sketch: `repeat ok, result = pcall(...) until not (ok and result == nil and entry.status == "loading" and not ProfileStore.IsClosing and task.wait(1))`.
- **protect:** S-T2 (degraded at 120 s, not earlier, not later), S-T13 (leave mid-load leaves no lock), A3 (store down for good → degraded at 120 s), shutdown during load (`IsClosing` → no retry).
- **retest:** new Lune spec (StoreFailure or Throttle): "leave mid-load, rejoin same server while the first load throttles 6 s: rejoined player ready with the saved data"; A3 and S-T2 unchanged.

### N1 · recommendation · Medium · harm 4 (leak, race after a yield) · S2, V-08
- **where:** `src/Session/init.luau:215-227`; `Data.luau:126`, `:141`.
- **observed:** `Data.load` runs the game's migrations and `validate` inside `pcall`, which lets them yield; nothing re-checks the entry after it. A migration or `validate` that yields (a `task.wait`, a store read) while the player leaves: `onLeave` sees `loading` and closes the entry without `EndSession` → `load` resumes, assigns `profile.Data` and sets `ready` on the closed entry → the session lock and autosave stay on this server until shutdown, and a rejoin on this server errors "already loaded in this session" (vendor `:1390-1392`) → `degraded`.
- **expected:** the contract calls migrations pure; the update path already turns a yield into a refusal (S4), the load path does not.
- **evidence:** code read (D); not run.
- **smallest_fix:** after `Data.load`, `if entry.status ~= "loading" then profile:EndSession() return end` (2 lines; `profile.Data` is still the raw save, so the release writes it unchanged).
- **retest:** Lune spec with a migration that waits 2 s and a leave at 1 s: `closed`, record released, rejoin `ready`.

## Lead rulings asked for

- **T-8:** confirmed (F2), blocking, fix in this repair round as the lead wants: retry while loading, bounded by the 120 s timer, 1 s between calls. F1 is its neighbour (same-server rejoin, other phase) and should land in the same round; both edits sit in `load`.
- **F-Q3:** add the row (contract change CC-6), not blocking for the code. Wording to cover both cases the vendor treats alike: "Autosave or leave save fails longer than the steal time, or never answers: ProfileStore's release keeps retrying (or hangs) and this server no longer answers force-load requests (subscription closed at `init.luau:721-723`); the next server steals at ~40 s; progress since the last landed save is lost (the crashed-server bound, autosave 300 s). Same server after F1's fix: the rejoin waits for the release and ends `degraded` at 120 s if it never lands. A hung release also holds `BindToClose` until the 30 s kill (`:2233`); other saves are unaffected." Test: Lune, `hang` on the leave save, player joins server B → B ready ≤ 50 s, record = last landed save, no duplicate grant.

## Contract changes CC-4, CC-5
- CC-4: code fires `Purchased` only when this call returns `PurchaseGranted` and the write was not a duplicate (`init.luau:458-461`): at most once, as amended. Holds.
- CC-5: the `IsActive` guard stays in `refusal` (`:286`) and `confirm` (`:411`, `:417`); A24 holds it. Holds.

```text
<spec>
artifact: roblox-game-framework/src/Session/init.luau@359dbebc, Data.luau@9b66b841 (vendor ProfileStore@799263dc unpatched)
reviewer: reviewer
looked_at_first: [contracts/Session.md, src/Session/init.luau, src/Session/Data.luau, vendor/ProfileStore/init.luau 655-960, 1030-1200, 1380-1620, 2190-2242, src/Helpers/Ledger.luau, src/Helpers/Amount.luau]
findings:
  - {id: F1, class: blocking, where: "init.luau:187-191, :257-269; vendor :1462-1489, :759", expected: "an update accepted before leave survives a failed-then-retried leave save", observed: "leave save fails, same-server rejoin loads the stale record, the release then writes nothing: progress since the last landed save lost", evidence: "Critical; D + scratch Lune probe on the candidate (expected 43, got 42)", smallest_fix: "release-pending mark per UserId set in onLeave, cleared on the profile's OnAfterSave; load waits while set and still loading", protect: "S-T13, S-T14, 120 s timer, shutdown", retest: "StoreFailure spec: leave save fails 10 s, rejoin same server +12 s keeps 43"}
  - {id: F2, class: blocking, where: "init.luau:187-201; vendor :1427-1446, :1601-1605", expected: "rejoined present player reaches ready", observed: "leave mid-throttled-load + same-server rejoin → degraded for the whole session (T-8)", evidence: "High; D + scratch Lune probe (degraded at 6.12 s, load_failed no session)", smallest_fix: "retry StartSessionAsync while nil, still loading, not IsClosing, 1 s apart; timer and Cancel end it", protect: "S-T2, S-T13, A3, shutdown during load", retest: "spec: leave mid-load, rejoin same server while first load throttles 6 s → ready"}
  - {id: N1, class: recommendation, where: "init.luau:215-227; Data.luau:126, :141", expected: "a leave during load never leaves a lock behind", observed: "a yielding migration or validate + leave → closed entry set ready, profile never ended, rejoin degraded", evidence: "Medium; D only", smallest_fix: "re-check entry.status after Data.load; EndSession and return", retest: "spec: migration waits 2 s, leave at 1 s → closed, released, rejoin ready"}
keep: [one write path with ready/IsClosing/IsActive refusal (S3); yield guard by coroutine (S4); id checked and recorded in the same assignment as the grant (D-11); PurchaseGranted only from LastSavedData; own-end flag set before every EndSession and no kick when IsClosing (S12, F4, F11); deep-copy load with profile.Data assigned only after validate (F1 of contracts-r1); structural-sharing seal that freezes as it checks; Studio prefix and studio-only edits by IsStudio at call time; waiters resumed on every leave path; vendor unpatched]
weakest_part: "both blocking findings are proven only in FakeWorld; real per-key request order and same-server rejoin timing on Roblox are modelled, not measured"
could_not_check: [{step: "F1/F2 on the engine", missing_input: "a probe place with real DataStore errors and a same-server rejoin", closes_it: "engine probe after the fix (S-T17 lane)", who: "studio-operator"}, {step: "old GWS/DS saves holding arrays with holes or mixed keys (seal would degrade them)", missing_input: "a sample of real old records", closes_it: "a DataStore read of a few live GWS/DS keys or the owner's word that none exist", who: "qa-lead / owner"}, {step: "Q9 card in engineering-craft references/framework.md", missing_input: "step 9 not done yet", closes_it: "step 9", who: "writer"}, {step: "Session.engine.spec", missing_input: "Studio lane", closes_it: "T-4 engine batch", who: "studio-operator"}]
verdict: fix-first
</spec>
```

Verdict: **fix-first** on init.luau 359dbebc and Data.luau 9b66b841: blocking F1, F2.
