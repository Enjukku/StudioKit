---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-Q2
supersedes: []
---
> Author: qa-lead · claude-opus-5-5 · medium · 2026-10-24

# Net protected acceptance: trace table, planted faults, verdict (J025-Q2)

## 1. Sources of truth (framework repo is uncommitted by rule 7: revision = file hash)
| Source | Revision |
| --- | --- |
| `contracts/Net.md` (frozen; N1-N8, failure table, patch steps 1-4, Net-T1..T21) + CC-8 (step 5), CC-13, CC-14 in `build-log.md` | as of 2026-10-24 |
| `reviews/code-net-r1.md` F1, F2 (lead message 2026-10-24: add protected specs, red now, green after fix) | as of 2026-10-24 |
| `src/Net/init.luau` | sha256 `778b4a742e9b054ab64e2d86c83eb7d4ba62976a360f4a21745dfde383c48a46` |
| `src/Net/Generated/Server.luau` (framework messages, patched) | sha256 `db9a6a815ee918c78eb4d051e973b481d9039e6d8a1525eda2818f5bc332604b` |
| `src/Net/tools/patch-generated.luau` | sha256 `7f6834107c767d44716bdbf025120584a161f7de61aa3eca3fd37cea12fb808a` |
| Engine numbers mirrored | `probes/p1-transport/runtime/runtime-result.md:66` (5 Output lines per raised error), `:68` (flood heartbeat) |
| Real policies | template `Coins.luau` CoinsCollect rate 4 burst 8; template `Core.luau` StateHydrate rate 1 burst 2 beforeReady |
| Runtime | Lune 0.11.1, Blink 0.18.9, `tools/spec/run.luau`; own fake engine in `tests/acceptance/Net/Harness.luau` (does not use `src/Net/test/`) |

Oracles: contract values and the engine's P1 numbers, hand-written; nothing read from `src/`. Each failed check raises `<label>: ...`; `Planted.spec.luau` asserts the label of the planted cause.
Schema: `tests/acceptance/Net/acceptance.blink` (game-style, passes the gate's schema lint): ranged f32/f64/vector, `string(..16)`, `u8[..8]`, `buffer(..16)`, `Instance(BasePart)`, `unknown`, a listener-less event, an unreliable vector, a function with `Reply`; generated + patched into `.gate/net-acceptance/` at load. `Framework.spec` runs the committed `src/Net/Generated/Server.luau`.

## 2. Trace table (lane: Lune gate `specs`; files `roblox-game-framework/tests/acceptance/Net/<File>.spec.luau`)
| # | Brief case / contract row | Spec | Oracle (expected) |
| --- | --- | --- | --- |
| A1 | spam over rate; N1(3), N2, Net-T3 | Rate R1 (answer), R2 (on, refill after 1 s), R3 (per player) | 8 done + 92 `denied rate` of 100; 8 then 4 handled; state = accepted; 0 lines |
| A2 | NaN/+inf/-inf every ranged type; failure rows 1, 3 | NonFinite N1 | 15 packets (f32, f64, vector, unreliable vector, function f64): handler 0, 15 decode rejects, engine Output 0, <= 1 line; in-range control 5 |
| A3 | range (finite out of range) | NonFinite N2 | 6 rejects, handler 0; bounds -180/180, 0/100, 1000 pass |
| A4 | NaN/inf in unranged data; N1(4), Net-T4 | NonFinite N3 | number, Vector3, Vector2, CFrame pos + rotation, nested, +-inf keys: all `bad_input`, handler 0 |
| A5 | oversize string / array / buffer; truncated | Oversize O1-O4 | 17/255 > 16, 33/0 vs 1..32, 9/255 > 8, 17/255 > 16, 3 truncated kinds: rejected, 0 Output; bound values pass |
| A6 | walk limits; Net-T5 | Oversize O5 | 600, 513 values, depth 9 denied; 500 values, depth 8 pass |
| A7 | wrong type | WrongType W1, W2 | non-buffer payloads: 5 rejects, 0 Output; unknown index 200 and server index 3: nothing runs |
| A8 | missing / wrong / foreign Instance; N7, G7 | WrongType I1, I2 | nil, Folder, 5, "Part" rejected; foreign part reaches the handler unchanged (ownership is the handler's) |
| A9 | wrong state; N1(1-2), Net-T1, T2 | State S1, S2, S3 | loading: 0 handled, `unavailable not_ready`, beforeReady passes; closing/closed: `unavailable closing`; degraded/ready pass; out of Players: 0, no rate entry |
| A10 | bad UTF-8; N1(4), G3 | Utf8 U1-U3 | 6 invalid kinds in string, function arg, unknown, nested, key: `bad_input`, handler 0; valid multi-byte passes |
| A11 | 1,000 malformed flood; guard, N5, Net-T9, T17 | Flood F1, F2 | 20 decoded then 980 blocked, 0 engine Output, <= 1 line / 10 s, other player served, served again after 10 s; 30 s: 60 decoded, <= 3 lines, 1 strike entry, 0 after leave |
| A12 | event with no listener; step 3, Net-T15 (Lune), T20 | NoListener Q1, Q2; Framework X3 | 256 queued incl. 10 boot-window events, 20 `no_listener` then blocked, 0 Output; one 10,000-event packet: 1 reject; AdminAction without Admin capped |
| A13 | player leaves mid-handler; G10, CC-8, N6, Net-T10 | Leave L1, L2, L3 | 0 sends to 100 leavers, stayer gets done; 1,000 cycles: rate + strikes 0; packet after leave: no state, no reply |
| A14 | replayed key; N4, N7 | Replay K1 | one packet = 1 call + 1 reply; 20 replays: 8 calls, 20 replies all invocation 7; no dedupe in Net (idempotency: Session S10/S11, Q1 A13-A16) |
| A15 | pcall guard (handler); N3 | HandlerError E1 | 1,000 throws: 1,000 `unavailable error`, 0 engine Output, <= 1 line, next call done |
| A16 | framework module itself; CC-17 | Framework X1, X2 | AdminAction NaN, +-inf, +-(2^53+2) target, 33-byte id: 6 decode rejects; target 0 decodes (CC-17) and the handler's presence check answers `denied no_target`, nothing changes; NaN / bad UTF-8 / depth 9 value: `bad_input`; StateHydrate at template policy: 2 of 100 |
| A17 | review F1 / CC-13 (valid-event flood) | Flood F3, F4, F5 | 65,535-event packet: calls <= 600, 1 reject, 1 strike (255-event batch passes whole); 500 x 255 in 1 s: blocked, calls <= 1,200; 65,535 unknown indexes: 1 reject, 1 strike |
| A18 | review F2 / CC-14 (T-10) | Leave L4 | Fire + FireList to 50 departed, 2 Heartbeats: 0 sends to departed, stayer 1 send |
| A19 | Net-T14 H (planted faults) | Planted (50 target rows over 31 plants) | §3 |

PF-rows: n/a (no player-facing presentation; server transport only).

## 3. Planted faults (`Plants.luau`; source text rewritten at load, `src/` never edited; matrix run 2026-10-24 on the hashes in §1, A17/A18 excluded)
| Plant | Check removed | Specs red (matrix) |
| --- | --- | --- |
| P01 | rate | R1 R2 R3 K1 X2 |
| P02 | Session readiness | S1 S2 X2 |
| P03 | player in Players, both sites (`check` N1 step 1 and `allow` R2-1; one site alone is equivalent since R2-1) | S3 |
| P31 | `allow` decodes for a sender who left (R2-1) | L3 (Act checks run = 0) |
| P04 | every Blink range check | N1 N2 X1 (+F1 F2 lines) |
| P05 | Net finite number | N3 X1 |
| P06 | range + Net finite (both layers) | N1 (handler reached) N2 N3 X1 F1 F2 |
| P07 / P08 | UTF-8 strings / keys | U1 U2 U3 X1 / U3 |
| P09 | whole walk | N3 O5 U1-U3 X1 |
| P10 / P11 | 512-value cap / depth cap | O5 / O5 X1 |
| P12-P14 | string / array / buffer bound | O1 / O2 / O3 (+F1 F2) |
| P15 | Instance class | I1 |
| P16 | queue cap 256 | Q1 Q2 X3 |
| P17 | patch pcall around decode | F1 F2 N1 N2 O1-O4 I1 W1 Q1 Q2 X1 X3 |
| P18 / P19 | allow not asked / strike never blocks | F1 F2 Q1 X3 |
| P20 / P21 / P22 | decode / bad_input / handler-error line sampling | F1 F2 Q1 N1 / N3 U1 / E1 |
| P23 | answer's xpcall | E1 |
| P24 / P25 / P26 | rate reset / strike reset / strike after leave | L2 / L2 F2 / L3 |
| P27 | patch steps 5 + 6 (G10, CC-14); step 5 alone is equivalent since step 6 | L1 |
| P29 | event allowance asked once per packet (CC-13) | F3 F4 F5 |
| P30 | patch step 6 off (CC-14, T-10) | L4 |
| P28 | decode rejects not counted | 14 specs |
Result (Q2b, hashes of §4b): **30 of 30 plants caught through their 49 target rows, 0 stale**; correct build: 0 false alarms. Step 5 alone survives since CC-14 (step 6 drops the entry): equivalent, so P27 removes both. The builder's own plants (evidence/Net.md "Repair round 1": once per packet on Transport T23, allowance not reset, step 6 off on T22, lint bound off) are not repeated; P29/P30 hold the protected F3-F5 and L4. Ownership: n/a (N7: no check in Net to remove; I2 holds the boundary). Idempotency: n/a (N7). Not planted: Instance `typeof` line alone (a non-Instance then raises on `:IsA`, still rejected; argued, not run). 

## 4. Verdict (2026-10-24, init `778b4a74`, Generated/Server `db9a6a81`, patch `7f683410`)
| Item | Verdict | Evidence (label) |
| --- | --- | --- |
| A1-A16 (33 specs) | PASS | 3 runs, logs byte-identical (md5 `3c992512…`), `specs: 13 files, 78 passed, 4 failed` (gate-verified lane, run by qa-lead) |
| A19 planted (45 rows) | PASS | same runs |
| A17 F3, F4, F5 | FAIL (intended: review F1) | F3 65,535 calls; F4 never blocked; F5 0 rejects |
| A18 L4 | FAIL (intended: review F2 / T-10) | 50 sends to departed players |
| `python tools/gate.py` | FAIL on specs only (the 4 above); transport, format, lint, rules, types (0 errors), build, copy-tool PASS; src/Admin: no failure | gate output 2026-10-24 |

## 4b. Verdict Q2b (2026-10-24, init `18bbd1c50db70cc7075923caf65aac59a86d58c2aff6056cb3c83ebb83787831`, Generated/Server `e5066c66e4ca8b1e45b08379e791a673a6e40b976443caade9ef3cf8de7327f4`, patch `248faf42…`)
| Item | Verdict | Evidence (label) |
| --- | --- | --- |
| A1-A18 (37 specs) incl. F3, F4, F5, L4 | PASS (F3-F5, L4 red on 778b4a74, green now: review F1, F2 closed for the protected rows) | 3 runs `13 files, 86 passed, 0 failed`, logs byte-identical (md5 `5e077eb1…`) (gate-verified lane) |
| A19 planted (49 rows) | PASS | same runs |
| `python tools/gate.py` | RESULT: PASS (60 files, 482 specs; transport, format, lint, rules, types, build, copy-tool PASS) | gate output 2026-10-24 |

## 4c. Verdict Q2c (2026-10-24, init `9067f189b3b6d00670dc34adeca1602b97bb4020ca1d26a1647bca40a3c6dbf0`, Generated/Server `e5066c66…27f4`)
| Item | Verdict | Evidence (label) |
| --- | --- | --- |
| A1-A18 (37 specs; L3 adds the R2-1 row) + A19 (50 planted rows, 31 plants, 0 survivors, 0 stale) | PASS | 3 runs `13 files, 87 passed, 0 failed`, logs byte-identical (md5 `65e7c94d…`) (gate-verified lane) |
| `python tools/gate.py` | RESULT: PASS | gate output 2026-10-24 |

## 5. Could not check
| Step | Missing input | Closes it |
| --- | --- | --- |
| Engine Output and heartbeat under a real flood (Net-T12, T18, F1 engine size) | Studio multi-client lane | studio-operator, engine batch T-4 |
| FireClient on a departed Player (raises or silent) | Studio probe | review F2 engine ticket |

Weakness: the fake engine runs `task.spawn` synchronously and has no native codegen, so costs and ordering under the real scheduler are not proven here; A17's numbers (600) are PROPOSAL values from CC-13 and must follow the contract if the owner changes them.
