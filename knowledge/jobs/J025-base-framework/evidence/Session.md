---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B6
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · high · 2026-10-24

# Session: Q1-Q9 evidence (J025-B6)

Artifact: `roblox-game-framework/src/Session/` {init.luau 638, Data.luau 148, Session.spec.luau, Receipts.spec.luau, Data.spec.luau, Session.engine.spec.luau, test/FakeWorld.luau 680, test/Fixtures.luau}, files as of 2026-10-24 (uncommitted, rule 7). Contract `contracts/Session.md` (frozen: F1-F4, F8, F9, F11, N2, R1, R2). `vendor/ProfileStore/` unchanged: no patch (seam S-00 worked, P-1 not needed). Split: `Data.luau` = pure load/seal rules (contract's "Migrate"); receipts stay in `init.luau` (one user, no separate module).

## Red run, first green, gate
- Red (Session = `return {}` stub): `lune run tools/spec/run.luau src/Session` → `3 files, 6 passed, 36 failed`: every FakeWorld spec "attempt to call a nil value" (Session.start), planted-fault specs "expected 1, got 0" (patch target missing), Data Q6 red (my fixture was 8.3 KB, not 10: fixed the fixture). Data.luau was written before its spec (honest: its 6 pure specs never ran red).
- First green: 40/42. Two real finds: (1) two join-time receipts: the first `OnAfterSave` woke both confirms, the second waited a 10 s retry → confirm now wakes only on a save that holds its own id; (2) planted F4 survived because `degrade` also disconnected `OnSessionEnd` → removed the disconnect so the own-end flag the contract names is the guard (the plant now turns S-T3 red).
- Gate: `python tools/gate.py` → format, lint, rules, types (0 errors), specs `20 files, 198 passed, 0 failed`, build, copy-tool PASS; `RESULT: PASS` (gate-verified).

## Q1-Q9
| Q | Result | Evidence |
| --- | --- | --- |
| Q1 API | PASS (11, as the contract) | 2 module functions (`start`, `status`) + 7 methods + 2 signals; spec hook `_debugCounts()` (README leak rule, not API) |
| Q2 strict | PASS (gate-verified) | every file `--!strict`; luau-lsp new solver 0 errors; exported types hold no `any`; 7 internal casts in init.luau (:508 def→Map, :531 ProfileStore.New params, :535 ProcessReceipt dictionary, :545/:559 Map→T, :563/:569 fn→Change). FakeWorld reaches `@lune/*` through `loadShared` so luau-lsp type-checks it too |
| Q3 tests can fail | PASS | row table below; 14 planted faults, 14 red (sweep script, each on the real file, restored; P12 survived first → S-T7 gained the inside-OnSessionEnd case) |
| Q4 failure rows | PASS (Lune) | every Failure-behaviour row → spec: load errors/throttle S-T2 (+hang); lock held live/crashed S-T7 thief, S-T23 crash; migration/validate S-T19; newer save S-T3; leave mid-load S-T13; save errors S-T23; stolen S-T7; receipt not here/degraded/loading S-T22, S-T24; unknown product/grant error S-T24; malformed record S-T26; save not confirmed S-T23. H-S1..H-S6 are QA's |
| Q5 leaks | PASS (Lune) | S-T14: 1,000 join/leave (every 3rd mid-load, every 2nd with an update) → `_debugCounts` {entries 0, waiters 0, connections 0, timers 0}; ProfileStore ActiveSessionCheck, AutoSaveList, UpdateQueue empty; PlayerAdded/PlayerRemoving 1 connection each |
| Q6 cost | PASS (Lune screening) / not verified (engine) | update, 10 KB save, 3 top keys: median 6.8 / 8.2 / 7.4 µs over 3 runs (p90 10-12 µs) vs 50 µs. Own load (migrate+reconcile+seal+validate) 10 KB: median 0.37-0.39 ms vs 2 ms. One save round trip in FakeWorld incl. JSON 1.1-1.2 ms (fake, not engine). Allocations per update: 1 coroutine (S4 yield guard) + the tables `fn` changed (+1 Ledger array for award/receipt); `seal` skips unchanged levels by reference. Session has 0 per-frame work (no Heartbeat; one `task.delay` per loading player) |
| Q7 authority | PASS | no client input. Entry points: ProcessReceipt (PurchaseId non-empty string, PlayerId and ProductId numbers, CurrencySpent through `Amount.whole`; player on this server and `ready`; product in `def.products`); PlayerAdded/PlayerRemoving; `award` rejects an id that is not a 1-64 char string (`bad_input`) |
| Q8 engine first | PASS | below |
| Q9 usage | PASS | runs in Lune (Session.spec "Q9 ..."); type-checks with a typed T in Session.engine.spec.luau `usageExample` (planted `n.Coins = "free"` → types FAIL, restored) |

## Q3 row → spec (Session.spec unless noted; R = Receipts.spec, D = Data.spec), planted fault → red
| Row | Spec | Planted fault (red) |
| --- | --- | --- |
| S-00 | "S-00 seam ..." | - |
| S-T1, S3 | "S-T1 join ..." | P1 no ready check |
| S-T2 | "S-T2 every load call fails ...", "S-T2 ... hangs ..." | P7 degraded writes, P8 no timer |
| S-T3, S7, S12 own end | "S-T3 a v3 save ..." | planted S7 fence, planted F4 own-end flag (in suite) |
| S-T4 | D "S-T4" ×4, "S-T4 GWS v0 and DS v1 records ..." | P9 reconcile overwrites |
| S-T5, S-T6, S1 | "S-T5 ...", "S-T6 ..." | P4 no seal (freeze) |
| S-T7, S12 | "S-T7 ..." (closing, IsClosing, inside OnSessionEnd, after steal + kick) | P12 skip IsActive |
| S-T8..S-T11, S4-S6 | "S-T8..S-T11 ...", D "seal refuses ...", D "S5 seal walks only ..." | P4, P11 PurchaseIds check, P14 yield kept |
| S-T12, S11 | "S-T12 award ..." | P10 award without log |
| S-T13 | "S-T13 leave mid-load ..." (in throttle wait, after lock write) | P6 entry kept |
| S-T14 | "S-T14 Q5 1,000 ..." | P6 |
| S-T15, S13 / S-T16, S14 | "S-T15 ...", "S-T16 ..." | - |
| S-T18, S15 | "S-T18 Studio edits ..." | P5 no Studio check |
| S-T19, F1 | "S-T19 ..." | planted F1 (no deep copy, in suite) |
| S-T26, R1 | "S-T26 malformed record ..." | - |
| S-T20, S10 | R "S-T20 grant and id in one update ..." | P2 id in a 2nd update, P3 grant before save |
| S-T21 / S-T22 / S-T23 / S-T24 / S-T25 | R "S-T21 ...", "S-T22" ×2, "S-T23" ×2, "S-T24 ...", "S-T25 ..." | planted F2 (in suite), P13 waiters not resumed, P3 |
| F11 / H-S5 shape | "H-S5 shape: shutdown ... kicks nobody" | planted F11 (in suite) |
| S-T17 | Session.engine.spec.luau (two-phase recipe in its header) | not run (engine lane) |

## Q8 engine features
| Feature | Docs | Use |
| --- | --- | --- |
| `MarketplaceService.ProcessReceipt` | `_api-reference/classes/MarketplaceService.yaml:2237-2310` (join-time call, no retry timer, may yield, two servers) | set once in `start`; waits while loading; NotProcessedYet unless a save holding the id landed |
| Grant-then-confirm pattern | `production/monetization/developer-products.md:251-309` | grant + id in one update; confirm via `LastSavedData` |
| `DataModel:BindToClose` 30 s | `_api-reference/classes/DataModel.yaml:544-560` | ProfileStore's release; FakeWorld kills at +30 s |
| Throttle queues, 301-306 dropped | `cloud-services/data-stores/error-codes-and-limits.md:15-24, 637-657` | FakeWorld `throttle`, `queueFull` (304) |
| Session lock, autosave, retries | `vendor/ProfileStore/init.luau:1364-1625, 709-935, 2193-2239` (vendored; CD-2) | unchanged; own code adds fence, migrations, degraded, timeout, receipts, awards, prefix |

## Probe (FakeWorld) and decisions inside the contract
- Probe: a player who leaves mid-load and rejoins the **same** server while the first load call is still throttled gets `degraded` ("load_failed: no session"): ProfileStore hands the new call the cancelled call's job result (`init.luau:1433-1446`, `:1603-1605`). Without throttling (4 gaps 0.02-0.15 s) the rejoin is `ready`. Built as the contract says (nil while present → degraded); question to the lead.
- Load timeout is a `task.delay(120)` per loading player (exact 120 s, and a `hang` cannot block it); `Cancel` = "status is no longer loading". Entries are made on first sight (PlayerAdded, receipt, `wait`, `selector`), never again after leave (SessionStatus attribute).
- Outcomes: fn error or yield → `unavailable, error`; fn returns non-table / bad data → `denied, invalid_data`; deny passes the fn's reason. Template must pass seal and `validate` at start.
- PROPOSAL values: TEXT.sessionMoved, AWARD_CAP 200, LOG_EVERY 10 s. TEXT.degraded is not in Session: the banner belongs to the UI that reads `SessionStatus`.

## Could not check
S-T17 and every engine claim (Studio lane, not run, brief rule); ProfileStore's own `warn` per DataStore error (`init.luau:425`) is unsampled, so the quiet-log rule holds for Session's lines only; real UpdateAsync timing differs from FakeWorld's "transform at call time" model.

## Repair round 1 (review code-session-r1 F1, F2, N1; feature-builder · claude-opus-5-5 · high · 2026-10-24)
Files: `src/Session/init.luau` 359dbebc → 089fd470e25ea0fb87d89ee323b8cc219500d73f6841ecf3df7632d2a4a03ce7; `Data.luau` unchanged 9b66b8417044aa74971b3b0366e1724a2513e9fadef8085dce363264289c4787; `Session.spec.luau` +3 specs → a86726a8…f1dbf. Vendor unpatched, no API change.
| Finding | Change (init.luau) | Spec (Session.spec.luau) | Red on 359dbebc | Green |
| --- | --- | --- | --- | --- |
| F1 lost save | `releasing[UserId]` = the profile's OnAfterSave connection, set in `onLeave` before `EndSession` (only when `IsActive`), cleared on its first fire; `load` waits (`task.wait()`) while set and still `loading`; the 120 s timer is armed before the wait | R1-F1 "leave save fails 10 s, rejoin the same server at +12 s ..." | `:504 expected 43, got 42` | PASS |
| F2 / T-8 | `StartSessionAsync` again every `LOAD_RETRY` = 1 s while it returns nil, `loading` and not `IsClosing`; timer and leave end it through `Cancel`; the late-profile check kept | R1-F2 "leave mid-load, rejoin ... throttles 6 s ..." | `:532 expected "ready", got "degraded"` | PASS |
| N1 | after `Data.load`: status not `loading` → `profile:EndSession()`, return (Data still the raw save) | R1-N1 "a migration that waits 2 s and a leave at 1 s ..." | `:560 expected "closed", got "ready"` | PASS |
- Leak (Q5): marks are counted in `_debugCounts().connections`; S-T14 (1,000 cycles) and the three R1 specs end at all zeros.
- Runs: `lune run tools/spec/run.luau src/Session tests/acceptance/Session` → `specs: 14 files, 93 passed, 0 failed` (QA's `Rejoin.spec.luau` 6 specs included: F1 ×2 classes, F2, CC-6 ×4). Gate (final run, after the parallel Net edit settled): every check PASS, specs `34 files, 284 passed, 0 failed`, `RESULT: PASS`. Earlier runs failed only on `src/Net/` (lint `math.isfinite`, transport), files another session was editing.
- Remaining window (not closed, named): an autosave or receipt save in flight at leave whose answer lands before a failing release also fires OnAfterSave and clears the mark early; loss needs an update accepted after that save's transform, a failed release and a same-server rejoin inside the back-off. ProfileStore exposes no "release landed" event; closing it needs a vendor patch (CD rule: unpatched) or a data compare.
- Residual of N1 as briefed: a same-server rejoin *during* the yielding migration still errors "already loaded in this session" → degraded (the profile is ended only when the migration returns). Migrations are pure by contract (S4).

## Repair round 3 (review code-recheck-r2 R2-1; feature-builder · claude-opus-5-5 · high · 2026-10-24)
Files (sha256): `vendor/ProfileStore/init.luau` 799263dc → `cfda9e90c3ea8e712f8233c30efebd35c801d7e4d30c20b914c3f8c8c2556a03` (patch P-1, 3 lines: :924 change, :130 doc, :984 type; `PATCHES.md` row P-1); `src/Session/init.luau` 089fd470 → `4dee452194b19820febb3070b3c6981d388973ac1ca41ce22e238fcd4c3b2eb7` (`onLeave` hold clears only when `OnAfterSave`'s second argument is true; `Profile.OnAfterSave: Event<(Map, boolean)>`; two comment lines); `Session.spec.luau` → `fe9456e3…2bed` (+5 specs). `Data.luau` unchanged.
| Spec (Session.spec.luau) | Red before (vendor 799263dc, init 089fd470) | Green after |
| --- | --- | --- |
| R2-1 P1 receipt save in flight at leave, release fails 12 s, same-server rejoin at +13 s: 143 kept (latency 1 s) | `:181 expected 143, got 142` | PASS (record 143, `PurchaseIds` {p-1}, released, counts 0) |
| R2-1 P2 A's release fails past B's steal, leave B, rejoin A: ready, A's mark cleared | green on 089fd470 too (it guards the fix, as the review asked); red under the review's data-compare clear planted into the new code: `at value.connections: expected 0, got 1` | PASS |
| planted P-1 off (vendor line back to upstream) turns P1 red | n/a (plant line absent) | red as `:180 expected "ready", got "loading"`: without P-1 the hold never clears, so the rejoin waits and degrades at 120 s (never the stale record). A ProfileStore update that drops P-1 turns this spec red in the gate |
| P-1 keeps records byte-identical: no-op session on GWS v0 and DS v1, whole stored record (Data and MetaData) canonical text equal with P-1 on and off | n/a | PASS |
- QA plants: none of the 19 `from` texts touch the changed lines (grep of `tests/acceptance/Session/Planted.spec.luau`); `tests/acceptance/Session` `specs: 11 files, 51 passed, 0 failed`; `src/Session` `3 files, 50 passed, 0 failed`.
- Gate: `PASS types 0 errors (strict, new solver); control flagged 2/2` · `PASS specs 34 files, 293 passed, 0 failed` · `SKIP engine 11 Jest specs` · `RESULT: PASS` (gate-verified).
- Left as is: CC-6 (a release that never lands keeps the hold → degraded at 120 s) is unchanged by design; every claim is FakeWorld (engine lane S-T17 not run).
