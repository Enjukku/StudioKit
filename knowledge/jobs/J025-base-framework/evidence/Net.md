---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B7
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · high · 2026-10-24

# Net: Q1-Q9 evidence (J025-B7)

Artifact: `roblox-game-framework/src/Net/` {init.luau, framework.blink, Generated/{Server,Client}.luau, tools/{patch-generated,schema-lint}.luau, Net.spec, Transport.spec, Lint.spec, Net.engine.spec, test/{World,Blink,sample.blink}}, files as of 2026-10-24 (uncommitted, rule 7). Contract `contracts/Net.md` (frozen, r2 "ready"). Blink 0.18.9, Lune 0.11.1, luau-lsp 1.70.1.

## Net-T0 first (Blink `function`, generated from `test/sample.blink`)
`function Buy { Yield: Coroutine, Data: string(1..32), Return: Framework.Reply }` generates `Buy.On(Listener: (Player, string) -> Reply): ()`: the listener's return is written as the reply (Blink pcalls it; on error it sends a failure byte and **warns once per error**, so Net must never raise). **On returns nothing**: no disconnect, and luau-lsp flags `Types.AnswerListen` (`-> () -> ()`) against it (`Expected '() -> ()', got '()'`). Net works at run time (cast `:: (() -> ())?`, `answer`'s returned function closes the registration: later calls get `unavailable, closing`); the type mismatch is question Q-1. Imports: `import "./framework" as Framework` works; options of an imported file are ignored, so `framework.blink` keeps its own output options (`Remotes.Framework.X` in a game, `Remotes.X` in the repo's own output).

## Red run (before code)
`lune run tools/spec/run.luau src/Net` with Net.spec only, no `init.luau`: `specs: 1 files, 0 passed, 17 failed` (each: file not found). First green: 17/17 unchanged. Transport and lint rows each carry an **unpatched control** that must hurt (5 Output lines per bad packet; 10,000 queued + 9,743 warns).

## Q1-Q9
| Q | Result | Evidence |
| --- | --- | --- |
| Q1 API | 4 public functions (`guard`, `on`, `answer`, `stats`) + spec hook `_debugCounts` | `init.luau:246-326` |
| Q2 strict | every file `--!strict`; luau-lsp 0 errors (gate types PASS); no `:: any` in `init.luau` (grep: 0); the patched Server module also analyzes clean (checked by hand: the gate skips `Generated/`) | gate log |
| Q3 rows | table below; 40 planted faults, 40 caught, 0 survivors after one test was added (N4 survived first: a player removed from Players while Session still said ready; Net-T1 now has that case) | `plant.py` run, list below |
| Q4 failures | every failure-table row has a spec: decode errors T17, flood T17/T18, NaN/UTF-8 T4, no-listener flood T20, spam T3, loading/leaving T1/T2, handler error T7, missing anchor T16 | specs |
| Q5 leak | 1,000 join/leave cycles with calls, rejects, a reject and a call after leave: `_debugCounts()` `{rate=0, rejects=0}`; 1 PlayerRemoving connection | Net-T10 |
| Q6 cost (Lune, 3 runs) | accepted call 1.96-2.29 us (budget 20), denied 0.21-0.26 us (10); gcinfo +0 KB over 20,000 calls: no allocation in Net's path. Guard per packet: valid 1.9-2.4 us unpatched vs 2.1-2.5 us patched (+0.1-0.4 us), rejected 3.7-4.3 us (budget 10). Flood sim: 1,000 bad packets 0.36-0.64 ms, 20 decoded, 980 dropped before decode, 1 Output line (unpatched: 5,000). Engine numbers: not verified (Net-T13, T18 written, not run) | Net.spec Q6, Transport.spec Q6 |
| Q7 | table below | |
| Q8 engine | RemoteEvent/UnreliableRemoteEvent through Blink (`scripting/events/remote.md:370-411`: reliable no-handler queue, unreliable drops; `_api-reference/classes/UnreliableRemoteEvent.yaml:42-63`); `math.isfinite` (`scripting/security/client-server-boundary.md:85`, `_api-reference/libraries/math.yaml:367`); token bucket (`client-server-boundary.md:169`) via Helpers RateLimit | |
| Q9 usage | contract usage runs in Lune (`Q9` spec, fake Remotes); typed wiring against the real generated module in `Net.engine.spec.luau` (gate types PASS) needs the AnswerListen cast (Q-1) | Net.spec, engine spec |

## Rows to specs (Lune unless marked)
T0 Transport `Net-T0`; T1-T11 Net.spec `Net-T1`..`Net-T11`; T12, T15, T18 `Net.engine.spec.luau` (realClient, flood; not run); T13 Net.spec `Q6 / Net-T13` + engine `timing` (not run); T14 = the planted-fault run below (QA writes the H version); T16 Transport two rows (determinism + 7 anchor cases); T17 Transport three rows (spy guard, unpatched control, through Net); T19 Lint.spec five rows; T20 Transport three rows (boot window + flood, one-packet batch, unpatched control).

## Planted faults (each alone; `src/Net` specs; all CAUGHT)
Net: skip ready (T2,T6) · skip walk (T4,T5,T6,T9) · never reset rate (T10) · skip in-Players (T1) · skip rate (T0,T3,T6,T9) · no xpcall in answer / on (T7) · reply check off (T8) · log every bad_input (T9) · no strike block (T17,T20,guard) · strike state after leave (T10) · depth and value count off by one (T5) · CFrame, Vector3, string key unchecked (T4) · guard not required, duplicate allowed (T11) · closed ignored · stats not a copy · degraded refused, beforeReady ignored (T2). Patch: no pcall (T17,T20,Q6) · allow ignored (T17,T20) · queue cap off (T16,T20) · missing anchor tolerated (T16) · not idempotent (T16) · cap error not `no_listener`, cap off by one (T20) · final unguarded-dispatcher check removed (T16). Lint: range, CFrame, map, Sync, function Data, generics, merges, UsePolling, tagged-enum variants, unreadable-exits-0 (T19).

## Q7: server entry points x checks (spec that proves it)
| Entry point | type | NaN/inf | range | rate | ownership | state |
| --- | --- | --- | --- | --- | --- | --- |
| Patched dispatcher (packet bytes, both remotes) | Blink decode, non-buffer and nil caught (T17) | ranged fields: Blink; lint forces ranges (T19) | Blink declared bounds (T17) | blocked 10 s after 20 rejects/1 s (T17, T20, guard) | sender only: its own batch lost (T17 mixed packet) | no-listener queue capped 256 (T20) |
| `Net.on` wrapper | walk typeof (T4) | walk: numbers, Vector3/2, CFrame, nested, keys (T4) | depth 8, 512 values (T5); server-state range: handler (N7) | per player x handler (T3) | in Players (T1); object ownership: handler (N7, engine T12) | Session status + beforeReady (T2) |
| `Net.answer` wrapper | same + Reply shape (T8) | same (T4) | same (T5) | same (T3, T0 through Blink) | same | same + closed registration |
| `guard.allow` / `guard.reject` (called by generated code) | err as string; kinds fixed (no attacker text as key) | n/a | err text cut to 200 bytes in the sample line | 1 sample line per 10 s server-wide (guard, T17) | no state for a player not in Players (T10) | reset on PlayerRemoving (T10) |

## Decisions made (inside the contract)
- Queue cap raises `no_listener` inside the guarded dispatcher instead of calling reject inline: one reject per packet and the rest of that packet dropped (bounded work per packet; G6 already accepts losing the rest of a sender's batch).
- Stats key `"(decode)"` with denied `{bad_packet, no_listener, blocked}`; reject kinds are fixed words so an attacker cannot grow the table.
- Only `bad_input` denials and handler errors log (sampled per handler); rate / not_ready / closing are counted only.
- Values walked count every argument and table value (string and number keys checked, not counted): a Blink array from a client must stay at 511 elements or fewer per call.
- Patch idempotence by a marker line; the patch also fails when a name `SetGuard` exists or any unguarded dispatcher remains.

## Follow-ups B7b (J025-B7b, feature-builder · claude-opus-5-5 · high · 2026-10-24)
Lead decisions CC-7..CC-9 + selene std. Files as of 2026-10-24. sha256: `src/Net/init.luau` 778b4a74…8a46, `src/Net/tools/patch-generated.luau` 7f683410…808a, `src/Net/Generated/Server.luau` db9a6a81…604b, `src/Types/init.luau` 1819b417…5c61.

| Item | Change | Red first | Green | Planted faults |
| --- | --- | --- | --- | --- |
| Q-1 (CC-7) | `Types.AnswerListen<A...> = ((Player, A...) -> Reply) -> ()`; `Net.answer` no longer casts or calls a disconnect (its returned function still closes the registration); cast removed from `Net.engine.spec.luau` (AdminAction wiring now typed against the real generated module) and the Timing fake returns nothing | gate types: `Net.engine.spec.luau:129: Expected '() -> ()', but got '()'` | gate types 0 errors | old type back = the red run |
| Q-3 (CC-8, G10) | patch step 5: in every Blink function reply writer, `if Player.Parent ~= Players then return end` before `Load(PlayersMap[Player])`; count-checked (`matched x of y function replies`); marker check covers it | Transport `Net-T21`: patched 100 replies to departed players (expected 0) | unpatched control 100 (entries created after PlayerRemoving cleared them: kept for the server's life), patched 0, the staying player still gets `{BUY, 2, done}` | F1 step off (T16 x2, T21), F2 count check off (T16 anchor case), F3 marker check ignores step 5 (T16 stripped case), F4 wrong condition (T16, T21): 4/4 caught |
| Q-2 (CC-9) | install.py: `src/<Block>/tools/` → `<game>/Framework-tools/<Block>/`, `src/<Block>/Generated/` skipped; check_lock scans `Framework-tools/`; reinstall replaces it; an unowned `Framework-tools/` is refused; README + REQUIRES one line each | test_copy_tool: 3 FAIL (Generated copied, no Framework-tools, unowned folder accepted) | 9/9; real `install.py --blocks Net` into a temp game: `Framework-tools/Net/{patch-generated,schema-lint}.luau`, no `Generated/`, copied checker PASS (14 files) | 5/5 caught (lock skips tools, reinstall keeps old tools, unowned folder overwritten, Generated copied, tools not copied) |
| Q-4 | `roblox-std.yml`: `math.isfinite`, `math.isinf`, `math.isnan` (one Luau addition; signatures from docs mirror `_api-reference/libraries/math.yaml:367-421`; selene 0.32.0's Luau base lacks them, so no generator output has them); header names the third change; allow line removed from `init.luau` | `selene src/Net` without the allow line: 1 error | 0 errors | entry removed = the red run |

Gate: in the live repo every FAIL line is in `src/Admin/` (parallel B8, half-built: lint 1, types 15+); Session specs were briefly red mid-run from a live Session edit and green again (293/293). A copy of the repo without `src/Admin/` (nothing else changed): `RESULT: PASS` (transport, format, lint, rules, types 0 errors, specs 293/293, build, copy-tool 9/9). Patched `Generated/Server.luau` analyzes clean by hand (the gate skips Generated). Net specs 33/33.
Not covered: an event `Fire(player)` after a yield to a player who already left creates the same lasting entry (game call, not a function reply); step 5 does not cover it (follow-up F-B7b-1).

## Repair round 1 (J025-R-Net-fix1, feature-builder · claude-opus-5-5 · high · 2026-10-24)
Review `reviews/code-net-r1.md` F1, F2, R1 = CC-13..CC-15; lead's CC-17 (AdminAction target range). sha256 after: `init.luau` 18bbd1c5…7831, `tools/patch-generated.luau` 248faf42…641f, `tools/schema-lint.luau` 2941dcdf…6ba0, `Generated/Server.luau` e5066c66…27f4 (`Generated/Client.luau` unchanged e6b3d031…e553), `framework.blink` ddf5d9a9…7eae75.

| Item | Change | Red first (on init 778b4a74, patch 7f683410) | Green | Planted fault |
| --- | --- | --- | --- | --- |
| F1 (CC-13) | patch step 2: each event loop starts `local Current = Guard; if Current and not Current.allow(Player) then error("flood", 0) end` (2 loops, count-checked, marker-checked); GuardedConnect keeps only pcall + reject. Net: `allow` = in Players? → blocked? → one credit of a per-player event allowance (`RateLimit.allowance`, PROPOSAL 600/s burst 600, reset on leave, counted in `_debugCounts().rate`); `reject` counts a blocked sender's packet as `blocked` (no strike), else kind `flood` / `no_listener` / `bad_packet` + strike | Transport `Net-T23` x3: 65,535 calls, `flood` nil, 0 rejects for unknown indexes; QA F3-F5 red | 255-event batch whole (0 denials); 65,535-event packet → 600 calls, 1 `flood`, 1 strike; other player unaffected; 500 × 255 in 1 s → 20 `flood`, 478 `blocked`, calls ≤ 1,200; 65,535 (reliable) and 1,000 (unreliable) unknown indexes → 1 `flood`; QA F3-F5 green | check asked only at `RecieveCursor == 0` (once per packet): T23 x3 + T16 red; allowance not reset on leave: Net-T10/Q5 red (rate 1000) |
| F2 (CC-14) | patch step 6, anchor `if Send.Cursor <= 0 then continue end` (once or exit 1): `if Player.Parent ~= Players then PlayersMap[Player] = nil continue end`; step 5 kept; marker check covers step 6 | `Net-T22`: 100 sends to departed (unpatched control also 100); QA L4 red (50) | patched 0 to departed, staying player 1 Heartbeat batch; QA L4 green | step 6 off: T22 + T16 x2 red |
| R1 (CC-15) | lint: every array in client data needs an upper bound ≤ 511 (`[n]`, `[a..b]`, `[..b]`), naming event and field; server arrays untouched | Lint `Net-T19`: missing `OpenArray` line | 5 bad shapes (`u8[]`, `u16[1..]`, `[..512]`, `[600]`, outer `[]` of a nested array) each one line; `[..511]`, `[1..50]`, `[4]`, nested bounded, server `u8[]` pass; framework + sample schemas pass | bound rule off: T19 red |
| CC-17 | `framework.blink` AdminAction target `f64(-9007199254740991..9007199254740991)?`; regenerated + patched | `CC-17` spec: -2 rejected (`targets` empty) | on the committed framework module: -2 and -(2^53-1) reach the handler and get `done`; NaN, +inf, -inf, ±(2^53+2) → 5 `bad_packet`, no reply; -2.5 reaches the handler (integer + presence are Admin's checks) | old range = the red run |
| Net-T16 | anchor cases for step 6 and the event loops; stripped-marked-file cases for steps 2 (per event), 5, 6 | step 6 anchor change patched silently | all exit 1 naming the anchor; second run unchanged | covered above |

Q6 (Lune, 3 runs each): one 65,535-event packet **before 106.0 / 107.0 / 109.0 ms, after 1.20-1.68 ms**. Accepted one-event packet: patched 2.11-2.38 µs vs unpatched 2.02-2.20 µs (+0.1-0.3 µs; budget 20 µs). Per blocked packet now ~3 µs (was ~0.4 µs): it runs the pcall'd prelude + `error("flood")` + `reject` before it is dropped; 1,000-packet flood 3.1-3.6 ms total (was 0.39 ms), inside the 18/25 ms heartbeat budget. Engine numbers not verified (Net-T18 variant with a valid-event flood is in the engine batch).
Patched `Generated/Server.luau` analyzes clean by hand (luau-lsp, new solver; the gate skips Generated).
Net spec edit: `Net.spec` guard row now calls `reject(p, "flood")` after each refused `allow` (what the patched module does), because `blocked` is counted in `reject` (so a blocked sender's non-buffer packet, which raises before the first event, is counted too).
Gate: all PASS except specs 476/478: QA `Framework.spec` X1 (and Planted P09 through it) expect a target of 0 to be rejected by the range; CC-17 makes 0 decode. Outside src/Net (QA update needed).
Weakness: a packet from a sender already out of Players is not bounded by the event allowance (no state may be created for them, N6; each event is denied `closing`); whether the engine delivers packets after PlayerRemoving is not verified.

## Repair round 3 (J025-R-Net-fix3, feature-builder · claude-opus-5-5 · high · 2026-10-24)
Review `reviews/code-net-r2.md` R2-1, R2-2. sha256 after: `init.luau` 9067f189…dbf0, `tools/schema-lint.luau` fad552c2…1e7a; `Generated/Server.luau` e5066c66…27f4 and `Generated/Client.luau` e6b3d031…e553 unchanged (no regeneration needed); `framework.blink` unchanged.

| Item | Change | Red first (init 18bbd1c5, lint 2941dcdf) | Green | Planted fault |
| --- | --- | --- | --- | --- |
| R2-1 | `allow`: a sender whose `Parent ~= Players` gets `false` (was `true`); `reject` already keeps no state for them | Transport `Net-T23 ... sender no longer in Players`: `expected 0, got 65535` decoded events | 0 decoded, `(decode).flood` 1, `StateHydrate.closing` 0, `_debugCounts` {rate 0, rejects 0}, 0 Output | `return true` back: same row red (65535) |
| R2-2 | lint `check` returns the most values Net's walk counts per value (array 1 + upper × inner, struct 1 + fields, merged fields join the outer table, tuple = sum, tagged enum + 1 tag, set 1 + flags); a value over 512 fails at the innermost such field with no size problem inside it, naming event and field (one line per event) | Lint `Net-T19` bad list: missing `event "Grid" field "Data": up to 4161 values per call, over 512` | bad: `u8(0..255)[..64][..64]` 4161, `(u8[..300], u8[..300])` 602, `Data.Cells` `u8[..32][..32]` 1057, `struct { A: u8[..511] }` 513, tagged enum at 513, set of 600 flags 601, each one line; safe at the boundary: `u8[..511]`, `struct { A: u8[..510] }`, `(u8[..255], u8[..255])`, tagged enum at 512, merged struct at 512, `u8[..16][..16]` 273; framework.blink and template/net/game.blink (scratch copy with its `../Framework/Net/` import) exit 0 | 7/7 caught: multiply → add, struct +1 dropped, tag +1 dropped, set counted as 1, tuple +1 added (safe `Sum` red), report removed, merge −1 dropped (safe `MergedOk` red) |

Spec edit (own): the safe `Arrays` row `struct { A: u8[..511], B, C, D }` was 579 values (Net refuses its full call): split into `Arrays` (B, C, D: 67) and `Flat` `u8[..511]` (512).
Gate (2026-10-24, live repo): transport, format, lint, rules, types (0 errors), build, copy-tool PASS; specs 486 passed, 1 failed: QA `Planted.spec.luau:43` **P03** "player-present check removed (N1 step 1): State S3 -> red: the planted fault survived". Cause: P03 disables the first `if player.Parent ~= Players then` (`check`, init.luau:129); with R2-1 every event of a departed sender is refused in `allow` before decode, so S3 never reaches `check` and stays green. The plant is obsolete, not a Net defect (like P27 after CC-14); `check`'s step 1 is still proven by `Net.spec` Net-T1 (direct listener calls). Not edited (QA's file). Retarget for QA: plant both sites (`all = true`), then S3's "rate entries" (allow would take a credit) and "handler calls" turn red.
Not verified: whether the engine delivers OnServerEvent after removal (review could-not-check; Studio probe in the engine batch).
