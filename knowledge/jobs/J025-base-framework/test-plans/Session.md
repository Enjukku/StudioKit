---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-Q1
supersedes: []
---
> Author: qa-lead · claude-opus-5-5 · medium · 2026-10-24

# Session protected acceptance: trace table, planted faults, verdict (J025-Q1)

## 1. Sources of truth (revision = file hash, framework repo is uncommitted by rule 7)
| Source | Revision |
| --- | --- |
| `contracts/Session.md` (frozen; H-S1..H-S6, failure table, S1-S15) | as of 2026-10-24 |
| `reviews/contracts-r1.md` (F1, F2, F4, F9), `reviews/contracts-r2.md` (F11, N2) | as of 2026-10-24 |
| `src/Session/init.luau` | sha256 `359dbebc2de8deac3bb853f8c0ead89d326ba2d8c50c14e20efc0acdc414a8b5` |
| `src/Session/Data.luau` | sha256 `9b66b8417044aa74971b3b0366e1724a2513e9fadef8085dce363264289c4787` |
| `src/Session/test/FakeWorld.luau` | sha256 `1b760d1c243824130ccd65c58bc55c3d86c668131abfc837040a3ab16db0ee9e` |
| `src/Session/test/Fixtures.luau` | sha256 `2c0801017c208e79fa4b4e9f89c761dd11299ee03b823da2f013756f1f9768d6` |
| `vendor/ProfileStore/init.luau` (1.0.3, unpatched) | sha256 `799263dc0d281f360432e172f57ef337761ec38482575273b3cb079d114ecf71` |
| Runtime | Lune 0.11.1, `tools/spec/run.luau`, FakeWorld (latency 0.1 s, 60 frames per virtual s) |

Oracles: the contract's stated outcomes, hand-written expected v2 shapes (Fixtures header: migration 1 Coins → currency.gold, migration 2 backpack.bricks → inventory.bricks, template fills the rest), canonical-JSON byte compare of the record's `Data` (F9), and in H-S2 an independent model that counts only accepted results. No expected value is read from `src/`.

## 2. Trace table (all lane: Lune gate `specs`; data: Fixtures schema v2, GWS v0 / DS v1 saves, products 1001/1002)
Files: `roblox-game-framework/tests/acceptance/Session/<File>.spec.luau`; helpers `Harness.luau` (labelled checks, seeded xorshift, `plant`).
| # | Contract row | Spec (file: name prefix) | Oracle | Conditions |
| --- | --- | --- | --- | --- |
| A1 | H-S1, S1-S3, S10, S11 | Throttle: `H-S1 every DataStore call throttles 8 s for 2 min` | statuses `loading,ready,closing,closed` per server + attribute mirror at every change; gold/gems/ids exact; Purchased 3 | 3 players, 2 servers, server move mid-throttle, repeat receipt, repeat award |
| A2 | failure table "errors/throttling during load" | StoreFailure: `load fails for 20 s (each error class)` | loading + `not_ready` during outage; ready; plays on saved gold 42; leave saves 43; 0 kicks | 500, 304 queue full, write-landed-answer-failed, 30 s throttle |
| A3 | same row + S9, S2 | StoreFailure: `load fails for good (each error class and a call that never answers)` | loading at 119.9 s, degraded at 120 s, template copy, writes refused, Data byte-identical, later server loads it | 500, 304, failAfterWrite, 200 s throttle, hang |
| A4 | "errors/throttling during autosave or leave save" | StoreFailure: `saves fail for 6 minutes (each error class)` | data kept in memory; leave save retries and lands 11; released; critical state logged (error classes) | autosave at 300 s inside the outage |
| A5 | H-S2, S4, S10, S11 | RandomFaults: `H-S2 1,000 seeded sequences` | model: gold = done updates + 100 × distinct ids; gems = first-time awards; id sets equal; released; 0 kicks | 20 worlds × 50 players × 2 sessions, 30 % DataStore faults (half after write), repeated ids, final redelivery on a clean server |
| A6 | H-S3, S12 | Stolen: `H-S3 server B asks for a live session` | B reads A's last update (5); A closed, kicked; A's update refused; B not kicked; record 15 | live MessagingService |
| A7 | H-S3 | Stolen: `H-S3 bus drops every message` | B ready at 35-50 s; A's post-steal +1000 never in record (10); A tried ≥ 2 saves; A closed, kicked | every PublishAsync dropped, 400 s for both autosaves |
| A8 | S12, F4, F11 | Stolen: `F4 F11 Session's own ends never kick` | world.kicks = [] | leave, newer save, failed migration, load timeout, shutdown in one world |
| A9 | H-S4 (landed) | Crash: `H-S4 crash while the confirming save is answered (landed)` | record 107 + id; no decision before crash; B ready ≤ 50 s; B confirms, gold 107 | throttle 1 s on the save, crash at +1.05 s |
| A10 | H-S4 (not landed) | Crash: `H-S4 crash while the confirming save is throttled (not landed)` | record = load (0, no id); B grants once (100) | crash at +0.5 s |
| A11 | H-S5, S3, F11 | Shutdown: `H-S5 shutdown with 50 players while every write throttles 1 s` | 50 updates refused `unavailable,closing`; 50 records saved + released at 29.95 s; status and mirror `closed`; 0 kicks; killed at 30 s | 50 players |
| A12 | H-S5 + docs queue limit | Shutdown: `H-S5 ... full write queue drops 20 saves (304)` | as A11 | calls 31-50 get 304 (error-codes-and-limits.md:15-22) |
| A13 | F2, N2, S10 | Receipts: `F2 N2 a receipt delivered before PlayerAdded runs and again while the load throttles` | no decision while loading; GRANTED only when the record holds the id (checked every frame); gold 100; ids [join-1]; Purchased once | receipt in `beforeAdded`, load throttled 5 s |
| A14 | F2, failure table | Receipts: `F2 a receipt while loading, then the player leaves` | NotProcessedYet; nothing granted; rejoin grants once | |
| A15 | S10 (brief: duplicate across crash + second server) | Receipts: `S10 one PurchaseId across a crash after its save landed, then servers B and C` | B and C confirm, gold stays 100; new id still grants (200) | crash in the answer wait |
| A16 | S10, S-T21 shape | Receipts: `S10 one PurchaseId delivered on two servers at once while the session moves` | B GRANTED, record 100, ids [twice-1] | |
| A17 | F1, S2, S9 | Schema: `F1 a migration that edits its input then throws` | degraded, no kick, template copy, refused update/receipt, Data byte-identical, a fixed server reads bricks 230 | DS v1 save |
| A18 | F1, S2 | Schema: `F1 a migration whose result fails validate` | as A17 | |
| A19 | S7, S9, F4, F9 | Schema: `S7 a v3 save on a v2 server` | degraded, frozen template, update/award/receipt refused, Data byte-identical, v3 server reads gold 777 + futureField | |
| A20 | F9, S2, S8 | Schema: `F9 a GreatWallSim v0 save` | migrations [1,2]; game reads hand-written v2 (all 30 old keys kept); 2nd no-op session: no migration, Data byte-identical | |
| A21 | F9 | Schema: `F9 a DestructionSimulator v1 save` | migrations [2]; v2 shape; no-op session byte-identical | |
| A22 | F9 | Schema: `F9 a current v2 save of 10 KB with 2^53 values` | byte-identical after a no-op session | Fixtures.big(10000) |
| A23 | S3 (IsClosing) | Writes: `S3 a write while ProfileStore.IsClosing is set` | `unavailable,closing`, data unchanged | state set directly (see §4 F-Q2) |
| A24 | S3 (IsActive), H-S6 | Writes: `S3 a write after the profile stopped being active` | update `unavailable,closing`; receipt NotProcessedYet | state set directly |
| A26 | review code-session-r1 F1, S2, failure table "leave save" | Rejoin: `F1 leave save fails 10 s, rejoin the same server at +12 s` | rejoined data and record keep 43 (saved 42 + accepted 1); released | 500 and 304 on the release, same-server rejoin |
| A27 | review F2 (T-8), S2 | Rejoin: `F2 leave mid-load while the first load throttles 6 s` | rejoined player ready on gold 42, still ready at +10 s, update lands 43 | first load throttle 6 s, leave at 1 s, rejoin at 2 s |
| A28 | CC-6 (hang), S10 | Rejoin: `CC-6 leave save never answers: server B steals` | B ready ≤ 50 s on the last landed save (100); redelivered receipt GRANTED, no duplicate | release `hang` on A |
| A29 | CC-6 (fails past steal) | Rejoin: `CC-6 leave save fails for 60 s` | B ready ≤ 50 s on 42; A's late release never overwrites (record 52 = 42 + B's 10) | |
| A30 | CC-6 (same server after F1 fix) | Rejoin: `CC-6 release never answers, rejoin the same server` | loading at 60 s, degraded at 120 s, not kicked, record unchanged | |
| A31 | CC-6 (shutdown) | Rejoin: `CC-6 a hung release holds BindToClose` | other player saved + released before the kill; alive at 29.5 s, killed by 30.5 s; 0 kicks | |
| A25 | H-S6, T-05 | Planted: 18 specs (P01-P16) | each target spec red with its own label; stale plant text fails | §3 |

Player-facing rows (PF-01..PF-16): n/a. Session has no picture or sound; its one client-visible truth, the `SessionStatus` attribute, is checked against `Session.status` at every change in A1 and at shutdown in A11. Hooks asked for: none needed (FakeWorld `patch`, `beforeAdded`, `setFaults` and `ProfileStore.Test()` already exist).

## 3. Planted faults (each through FakeWorld `patch`; src/ and vendor/ untouched)
Matrix run: every plant against every acceptance spec (Lune 0.11.1, 2026-10-24). Caught 16 of 16; false alarms 0 (unpatched suite 42/42, 3 runs).
| Id | Fault (file) | Specs red (matrix) | Planted.spec target → label |
| --- | --- | --- | --- |
| P01 | H-S6 ready check removed (`refused = nil`) | 12 | Throttle H-S1 → "update before ready" |
| P02 | H-S6 PurchaseId recorded in a second update after the grant | 6 | Receipts crash+B+C → "granted once"; RandomFaults → "no duplicate grant" |
| P03 | H-S6 IsActive skipped in `refusal` and `confirm` | 1 (A24 only) | Writes inactive → "not active" |
| P04 | H-S6 newer-version fence dropped | 2 | Schema S7 → "newer save -> degraded (S7)" |
| P05 | F1 migrate the loaded table (no deep copy, Data.luau) | 2 | Schema F1 → "record Data unchanged while degraded (F1)" |
| P06 | F4 OnSessionEnd ignores Session's own end | 11 | Stolen F4 F11 → "newer save -> degraded" |
| P07 | F11 kick at ProfileStore's shutdown release | 3 | Shutdown → "kicks during shutdown" |
| P08 | F2 receipt refused while loading | 6 | Receipts F2 N2 → "join-time receipt waits" |
| P09 | N2 player with no entry yet treated as absent | 5 | Receipts F2 N2 → "join-time receipt waits" |
| P10 | S10 PurchaseGranted from memory before the save landed | 5 | Receipts F2 N2 → "PurchaseGranted only after the record holds" |
| P11 | load timeout never fires | 2 | StoreFailure for good → "degraded at 120 s" |
| P12 | accepted update not handed to ProfileStore | 14 | StoreFailure saves fail → "every update landed" |
| P13 | ledger duplicate check removed | 6 | Receipts crash+B+C → "granted once" |
| P14 | writes allowed while IsClosing | 1 (A23 only) | Writes IsClosing → "update while IsClosing" |
| P15 | OnSessionEnd leaves the entry ready | 2 | Shutdown → "status after the shutdown release" |
| P16 | stale owner may write (vendor `IsThisSession` ignores JobId) | 3 | Stolen dropped bus → "B steals at about 40 s"; RandomFaults → "no lost update" |

Plants for the F1/F2 fixes (J025-Q1c, in Planted.spec, against init.luau 089fd470…): PF1 `while releasing[userId] and entry.status == "loading" do` → `while false do`: A26 red "rejoined data keeps the update (F1)"; PF2 nil-retry loop → `while false do`: A27 red "rejoined player status (F2)"; PF3 load-timeout degrade skipped while a release is pending: A30 red "degraded at 120 s (CC-6)". Total 19 plants, each caught by its target with its own label.

## 4. Results and findings
**Verdict J025-Q1c: PASS on src/Session/init.luau sha256 089fd470e25ea0fb87d89ee323b8cc219500d73f6841ecf3df7632d2a4a03ce7, Data.luau 9b66b841…4787, vendor 799263dc…cf71 (Lune 0.11.1, 2026-10-24).** tests/acceptance: 3 runs, 11 files, 51 passed, 0 failed each run (A1-A31 and 21 Planted specs). `python tools/gate.py`: every check PASS, specs 34 files 287 passed, RESULT: PASS (gate-verified). A26 and A27, red on 359dbebc, are green on 089fd470.
J025-Q1b run (2026-10-24, src/Session/init.luau sha256 359dbebc…a8b5, 3 runs): A26 FAIL "server error 500: rejoined data keeps the update (F1): expected 43, got 42"; A27 FAIL "rejoined player status (F2): expected "ready", got "degraded""; A28-A31 PASS. 46 passed, 2 failed in each run. The two reds are review F1/F2, which the builder is fixing; they are not test faults.

| Check | Verdict | Evidence |
| --- | --- | --- |
| Acceptance suite, 3 runs | PASS 42/42 each, deterministic | `lune run tools/spec/run.luau tests/acceptance` → `specs: 10 files, 42 passed, 0 failed` ×3; with `src/Session`: 13 files, 84 passed |
| Gate `python tools/gate.py` | specs PASS (31 files, 257 passed), format/lint/types PASS for tests/; RESULT: FAIL from `src/Net` only (transport: Generated files missing; format: `src/Net/tools/patch-generated.luau`; rules: `src/Net/Net.spec.luau:17`), another ticket's work in progress | `.gate/*.log` of the 3rd run |
| Failing acceptance specs on the current build | none | |

- **F-Q1 (needs-decision, contract API line `save.Purchased`).** Purchased never fires for a purchase whose first confirmation does not return: (a) A grants, the save lands, A crashes before answering; B confirms the redelivery as a duplicate → `PurchaseGranted`, gold 100, Purchased fired 0; (b) S-T23 shape, saves fail until leave, B confirms → fired 0. The contract says "fires once, after PurchaseGranted"; exactly once across servers needs a persisted marker. Not a spec (expected value is a design choice). Default: at most once (current behaviour), contract wording changed to "at most once; never grant or count revenue from it". Retest: A9, A15 with a Purchased count.
- **F-Q2 (contract note, H-S6).** P03 (skip IsActive) and P14 (IsClosing) survive every event sequence: ProfileStore 1.0.3 removes the profile from `ActiveSessionCheck` and fires `OnSessionEnd` synchronously in one step (`init.luau:720-726`, `:916-919`), and its shutdown sets `IsClosing` then releases every profile synchronously (`:2208-2229`). Only A23/A24, which set the state directly, catch them. The guards are defense for a future ProfileStore; H-S6's "each turns a spec red" holds through A23/A24.
- **F-Q3 (open question, failure table).** No row for an autosave or leave save whose call never answers (`hang`): ProfileStore's ending save loops until success, the lock stays, the next server steals after ~40 s and progress since the last landed save is lost. Not tested. Default: accept as the crashed-server bound, add the row.

## 5. Could not check
| Step | Missing input | Closes it |
| --- | --- | --- |
| Real DataStore queue limits, latency spread, MessagingService delivery order | engine | S-T17 engine spec + H-S5 shutdown in a probe place with 1 client (review r2 could-not-check, studio-operator) |
| ProcessReceipt vs PlayerAdded order (N2) on the engine | live purchase | A13 covers both orders in the fake; a published test purchase |
| Real 30-request queue during a 50-player shutdown | engine | A12 models it with 304 drops only |
| F1/F2 same-server rejoin on the engine | probe place with real DataStore errors | S-T17 lane after the fix (studio-operator) |

## 6. Result card (for the owner)
Saves and purchases survive what real servers do, in the fake: slow and failing stores, a full queue, a crash mid-save, a second server taking the player, a full-server shutdown, old saves from both games, a broken migration and a save from a newer version. We planted 16 of the bugs these checks exist for, one at a time; every one turned a check red for its own reason, and the real code passed all checks three times in a row. Not yet proven on Roblox's real servers (§5). One design choice open: F-Q1.

## 7. Rework and weakness
First attempt: all 24 behaviour specs passed on the first candidate (no builder repair round; my own spec fixes while writing: wrong permanent-throttle length, type annotations, formatter pass). Named weakness: the only runtime is FakeWorld, so every engine-timing fact (queue, latency, message order) is modelled, not measured; next step the Studio rows in §5. Second weakness: plants match exact source text, so a builder refactor turns a plant red as "plant matches the build" until QA updates it (loud, never silent).
