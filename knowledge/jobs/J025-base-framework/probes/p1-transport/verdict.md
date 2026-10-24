---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# P1 verdict: transport generator for `Net`

**Pick: Blink 0.18.9.** Zap 0.6.29 fails three of five tests on our payloads (a ranged vector kills the event, output is not deterministic, output is `--!nocheck`). Blink passes all five, with the gaps in §3 that `Net` must check itself. Every validation claim below is read from the generated deserializer (`gen/<tool>/Server.luau:line`) and confirmed by the offline receive run (`offline/<tool>.out.txt`, Lune 0.11.1, stand-in datatypes). The engine run (`runtime/`) is NOT RUN: the lead runs it in the probe window (`runtime/RUN.md`).

## 1. Setup
| Item | Value |
| --- | --- |
| Blink | v0.18.9, published 2026-09-19T07:26Z (GitHub releases API). A `v1.0.0-pre.10` pre-release came out the same day: not evaluated |
| Zap | v0.6.29, published 2026-06-23T07:48Z; the newest 0.6.x |
| Install | `scratch/rokit.toml`: `rokit install --no-trust-check` installs both; `blink --version` → `Blink 0.18.9`, `zap --version` → `cli 0.6.29` |
| Schemas | `schemas/net.blink`, `schemas/net.zap`: the same 7 events. (a) `DamState`/`EchoDelta`: GWS dam push (`GreatWallSim/src/client/Controllers/NetController.luau:39-52`) with nested map and string array; (b) `RedeemCode`: GWS `CodesService.redeemCode(player, text)` (`CodesService.luau:6`); (c) `RequestFire`: DS `WeaponService.requestFire` (gear, origin, direction, shotId, distance: `WeaponService.luau:609-617`) plus a `BasePart` target and a `CFrame` aim (neither game sends an Instance client→server today, so this field is added); `Pick`: Instance + CFrame + unranged vector; `Blob`: `buffer(..256)`; (d) `ReportView` unreliable: DS `BrickWorldService.reportView` camera (`BrickWorldService.luau:17`) |
| Analyzer | luau-lsp 1.69.0, `--definitions=roblox-game-framework/tools/types/globalTypes.d.luau` |

## 2. Results per test
| Test | Blink 0.18.9 | Zap 0.6.29 |
| --- | --- | --- |
| **T1 strict analyze** | **PASS.** All 3 files start `--!strict` (`Server.luau:1`); analyze: Server 0 errors 0 warnings, Client 0/0, Types 0/0. Internal `:: any` on 4 lines (`Server.luau:226,228,250,296`); public types exact | **FAIL.** Server and Client start `--!nocheck` and `--!nolint` (`Server.luau:3-4`): analyze reports 0/0 because nothing is checked. Forced to `--!strict`: Server 23 errors, Client 26 (`scratch/strictcheck/zap_*.txt`), among them the vector bug below (`(385,10) Expected 'number', got 'vector'`) |
| **T2 server receive** (ranged float, ranged vector, string/array/buffer over max, wrong type, missing Instance) | **PASS on every declared bound.** Ranged float: `if not (x >= min)` / `if not (x <= max)` (`Server.luau:243-244`): NaN, +inf, −inf rejected (`delta_gym_nan/inf/ninf`). Half ranges are filled with the type limit, so inf still fails (`scratch/half/out/S.luau:169-173`). Ranged vector: magnitude check (`:306-307,312-313`): NaN, ±inf rejected (`fire_origin_*`, `fire_dir_nan`, `view_*`). String `string(1..24)`: byte length checked after read (`:289-290`; `redeem_empty`, `redeem_25_ascii`). Array `[..8]` (`:265-266`), buffer `(..256)` (`:340`) rejected over max. Missing or client-only Instance → `typeof ~= "Instance"` error (`:320`); wrong class → `IsA` (`:321`). Bad enum index → error (`:238`). Truncated packet → `buffer access out of bounds`. Gaps: §3 G1-G6 | **FAIL.** Ranged float and buffer/array caps work (`assert(x >= 0)`, `:346-347`, `:383`). But a vector with ranged components asserts on the field **before it is read** (`Server.luau:270-275`, `:400-405`): every `RequestFire` and every `ReportView` packet, valid or not, errors `attempt to compare number <= nil` (`fire_ok`, `view_ok` rejected). `string.utf8(1..24)` is checked as 1..96 **bytes** with no character count (`:307`): 96 ASCII chars accepted (`redeem_96_ascii`). Enum with no bit set → field silently `nil` (`:336-341`: no `else` branch; `delta_bad_enum` accepted). Instance nil / class checked (`pick_missing_instance`, `pick_wrong_class`). UTF-8 validity checked (`redeem_bad_utf8` rejected) |
| **T3 unreliable** | **PASS.** `Type: Unreliable` events share one `UnreliableRemoteEvent` `BLINK_UNRELIABLE_REMOTE` (`Server.luau` remote setup); each `Fire` sends one packet at once, no batching (`Client.luau:495-503`); receive is validated like reliable (`view_*`). No send-side check of the 1,000-byte cap (engine drops larger, `scripting/events/remote.md:403`) | **FAIL in practice.** Supported (`unreliable[1]`, one remote per unreliable event), but our ranged-vector payload hits the bug above: `view_ok` rejected |
| **T4 size, readability** | Server 682 lines / 26.6 KB, Client 512 / 17.6 KB, Types 160 / 3.4 KB. One `ReadEVENT_<Name>` function per event, field names in every error message, dispatcher is a flat `if Index ==` chain (`:458-525`). Readable | Server 935 / 31.6 KB, Client 548 / 17.9 KB, Types 29. Deserialize is inlined in the dispatcher; the struct writer is copied for each of `Fire`/`FireAll`/`FireList`/`FireExcept` (`DamState` block `:483-760`). Readable but longer |
| **T5 rokit pin, deterministic** | **PASS.** Installs from `blink = "1Axen/blink@0.18.9"`. 5 runs with the outputs deleted between runs: byte-identical (sha256 `b0fa64b2…` Server, `08765586…` Client, `2b145396…` Types) | **FAIL.** Installs from `zap = "red-blox/zap@0.6.29"`, but 5 runs give 5 different hashes: type exports come out in a random order (`diff` of `Types.luau`: `Cell` and `DamPhase` swap). A byte-compare gate cannot work |

Both: reliable events are batched and sent once per `Heartbeat` (Blink `Server.luau:457`, Zap `SendEvents` on Heartbeat): up to one frame of added delay unless `ManualReplication` / `manual_event_loop` is set. Both: map types take **no size bound** (Blink parser `scratch/blink-src/src/Parser.luau:1402-1431`, although the Blink docs page `docs/pages/language/4-types.mdx` shows `map …(1..100)`; Zap grammar `scratch/zap-src/zap/src/parser/grammar.lalrpop:124`).

## 3. What `Net` must still check itself (Blink gaps)
| Id | Gap (evidence) | `Net` rule |
| --- | --- | --- |
| G1 | Unranged `f32`/`f64`/`vector` get no check: NaN and inf pass (`Server.luau:245` `EndsAt`, `:380` `Value3`; `delta_endsAt_nan_unranged`, `pick_vector_nan_unranged` accepted) | Schema rule: every number and vector a client sends carries a range. Gate check: a `From: Client` event with a bare `f32`, `f64` or `vector` fails. Per-axis or zone bounds against server state stay in the handler |
| G2 | `CFrame` is never checked (`:329`, `:376`; `pick_cframe_nan`, `pick_cframe_inf` accepted) | No `CFrame` in `From: Client` events: send a ranged `vector` position plus ranged angles; or `Net` checks every component finite |
| G3 | Strings: byte length only, no UTF-8 check (`:289-290`; `redeem_bad_utf8` accepted) | `Net` text reader: `utf8.len(s) ~= nil`, then the game's normalize (GWS `CodeRules.normalize`); bounds in the schema are bytes |
| G4 | Maps: `u16` count with no cap (`:247`; `delta_cells_5000_unbounded_map` accepted) | No maps in `From: Client` events; use bounded arrays `T[..n]`. Gate check |
| G5 | No rate limit: 1000 valid packets → 1000 listener calls (`spam_1000_redeem`) | `Net` per-player, per-event token bucket (GWS `Lib/RateLimit.luau` `allowance`), plus ready, ownership, range against server state, idempotency (N-02 steps 3-7) |
| G6 | Rejection is an `error()` inside `OnServerEvent`, no `pcall`, no non-buffer check (`:463` `buffer.len` on any value): each bad packet writes one error with stack to the server Output (a client can flood the log), events earlier in the same batch were already delivered and later ones are dropped (`batch_ok_bad_ok`: first accepted, rest lost). `Net` never sees a rejection | Accept it: handlers must not assume all events of a batch arrive. `Net` cannot count or kick on malformed packets without patching generated code (not proposed). Watch for log flood in the soak |
| G7 | Instance check is `typeof` + `IsA` only (`:320-321`): any replicated `BasePart` passes, including another player's | `Net` handler checks ownership/location (`IsDescendantOf`, owner attribute, distance) |
| G8 | No listener connected → events queue in a Lua table, warn past 256, no cap (`:488-491`) | `Net` connects every `From: Client` event at require time, before players join |
| G9 | Buffer is allocated at the client's declared length (up to 65,535 bytes) before the max check (`:337-340`) | Accept (bounded, freed at once) |

CLI quirks seen: `blink -q <file>` fails with `os error 2` (do not use `-q` in the gate); an output path with no folder (`"S.luau"`) fails `Access is denied`; use `./out/…` style paths.

## 4. Pin and gate
- Rokit pin: `blink = "1Axen/blink@0.18.9"`
- Gate "generated output is current" (Blink writes to the paths in the schema's `option ServerOutput/ClientOutput/TypesOutput`): `rokit install && blink src/Net/net.blink && git diff --exit-code -- src/Net/Generated` (non-zero exit = stale). Without git: copy the folder, regenerate, compare bytes. Valid because T5 showed byte-identical output.

## 5. Open
- Runtime harness: NOT RUN (lead runs `runtime/RUN.md`); the offline results are not engine evidence for `Vector3`/`CFrame`/`Instance` behaviour.
- Blink 1.0.0 pre-releases are moving fast (pre.9, pre.10 on 2026-09-18/19): re-run this probe before moving to 1.0.
