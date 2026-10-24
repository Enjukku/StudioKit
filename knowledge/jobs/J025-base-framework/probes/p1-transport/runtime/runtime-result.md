---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: studio-operator · claude-sonnet-5-5 · medium · 2026-10-24

# P1 runtime result (Blink 0.18.9 in the real engine, solo play-test, MCP-verified)

studio_id `b253d435-3fe7-4d9d-b34f-bdc3bbe52136` (probe-transport.rbxl, rebuilt with rojo 7.7.0 before the run). Game windows untouched. Probe window stopped and its process (pid 1912400) closed. Harness unchanged. Prefix `ServerScriptService.Net.BlinkServer:` is dropped from the lines below.

## 1. RUN.md cases (34 cases + 3 spam + done): all 38 lines match the expected table; no FAIL
| Case | Expected | Observed (server Output) | Result |
| --- | --- | --- | --- |
| P1ClientOnly (client / server) | true / false | true / false | pass |
| redeem_ok | accepted `len=6 utf8=true` | accepted RedeemCode(len=6 utf8=true) | pass |
| redeem_empty | rejected | :289 Expected length of "Value" to be larger than or equal to 1, got 0 | pass |
| redeem_25_ascii | rejected | :290 ...smaller than or equal to  24, got 25 | pass |
| redeem_bad_utf8 (G3) | accepted `utf8=false` | accepted RedeemCode(len=3 utf8=false) | pass (gap confirmed) |
| redeem_truncated | rejected `out of bounds` | :288 buffer access out of bounds | pass |
| delta_ok | accepted `gym=1.5` | accepted EchoDelta(gym=1.5 endsAt=1000 phase=Building cells=1) | pass |
| delta_gym_nan / inf / ninf | rejected `got nan/inf/-inf` | :243 ...got nan / :244 ...got inf / :243 ...got -inf | pass |
| delta_endsAt_nan_unranged (G1) | accepted `endsAt=nan` | accepted EchoDelta(... endsAt=nan ...) | pass (gap confirmed) |
| delta_bad_enum | rejected `Unexpected enum: 7` | :238 Unexpected enum: 7 | pass |
| delta_labels_9 | rejected | :266 Expected "Length" to be smaller than or equal to 8, got 9 | pass |
| delta_cells_5000_unbounded_map (G4) | accepted `cells=5000` | accepted EchoDelta(... cells=5000) | pass (gap confirmed) |
| blob_256 / blob_257 | accepted / rejected | accepted Blob(len=256) / :340 Expected size of "Value" ... 256, got 257 | pass |
| fire_ok | accepted | accepted RequestFire(origin=5, 0, 0 target=Workspace.P1Target) | pass |
| fire_origin_nan / inf / ninf | rejected | :306 magnitude of "Value.Origin" ... got nan / :307 ...got inf / :307 ...got inf | pass |
| fire_dir_nan | rejected | :312 magnitude of "Value.Direction" ... got nan | pass |
| fire_dist_inf | rejected | :317 "Value.Distance" ... 200, got inf | pass |
| fire_gear_33 | rejected | :301 length of "Value.GearId" ... 32, got 33 | pass |
| fire_missing_instance_client_only | rejected | :320 Expected an Instance, got nil instead. | pass |
| fire_wrong_class | rejected `of type "BasePart"` | :321 Expected an Instance of type "BasePart", got "Folder" | pass |
| pick_ok | accepted | accepted Pick(target=P1Target aimPos=0, 0, 0 point=0, 0, 0) | pass |
| pick_cframe_nan / inf (G2) | accepted | accepted aimPos=nan, 0, 0 / aimPos=inf, 0, 0 | pass (gap confirmed) |
| pick_vector_nan_unranged (G1) | accepted | accepted point=nan, 0, 0 | pass (gap confirmed) |
| wrongtype_string_not_buffer (G6) | rejected | :463 invalid argument #1 to 'len' (buffer expected, got string) | pass |
| wrongtype_instances_missing (G6) | rejected | :366 attempt to index nil with number | pass |
| unknown_event_id_200 | rejected silent | rejected silent | pass |
| batch_ok_bad_ok (G6) | accepted + then error | accepted RedeemCode(len=3 utf8=true) \| then error: :289 ...got 0 | pass |
| view_ok | accepted | accepted ReportView(pos=5, 0, 0 look=1, 0, 0) | pass |
| view_pos_nan / view_look_ninf | rejected | :351 magnitude of "Value1" ... got nan / :358 magnitude of "Value2" ... got inf | pass |
| spam_raw_reliable_1000 | 1000/1000 | received 1000/1000 last_arrival_after_s 0.97 | pass |
| spam_api_reliable_1000 | 1000/1000 | received 1000/1000 last_arrival_after_s 0.97 | pass |
| spam_api_unreliable_1000 | N/1000 | received 1000/1000 last_arrival_after_s 0.97 (no drops) | pass, see surprises |
| done | P1 done | P1 done | pass |

Notes: `view_look_ninf` reports "got inf" for -inf (magnitude is always positive). Errors print their own stack lines (expected).

## 2. G6: one malformed packet vs the same client's other events
Method: harness P1Case bracket; per rep one bad `RedeemCode("")` then valid events as separate `FireServer` calls (not one batch): same frame = valid RedeemCode + valid Blob (reliable) + valid ReportView (unreliable); next frame (after `task.wait()`) = the same three.
| Rep | Valid sent after the bad packet | Delivered to listeners |
| --- | --- | --- |
| 1 | 3 same frame + 3 next frame | 6/6 (error line logged once) |
| 2 | 3 same frame + 3 next frame | 6/6 (error line logged once) |
So a bad packet only loses what is in its own packet (batch_ok_bad_ok: events before it delivered, after it lost). Other packets, other events and the unreliable remote are unaffected.

## 3. Log flood and server cost
Studio solo play: server and client share one machine and one Studio process, so frame numbers include the client's send cost.
| Measure | Value |
| --- | --- |
| Output lines per bad packet | 5: 1 MessageError (`BlinkServer:289: Expected length ...`) + 4 MessageInfo (`Stack Begin`, `Script '...BlinkServer', Line 289 - function ReadEVENT_RedeemCode`, `Script '...BlinkServer', Line 484`, `Stack End`). Counted: 1174 bad packets = 1174 errors = 5870 lines; 816 = 816 = 4080 |
| Flood run A (about 1000/s target, 2 s, 1173 sent + 1 single packet) | every packet logged (1174/1174); heartbeat with the single-packet period mixed in: avg 20.08 ms, max 55.99 ms (baseline avg 16.67, max 19.01) |
| Flood run B (2 s, 816 sent; client slowed itself) | every packet logged (816/816); flood heartbeat n=47 frames, avg 42.30 ms, max 81.32 ms, 39 frames over 25 ms (baseline n=269, avg 16.68, max 20.74, 0 over 25 ms); after: avg 17.17, max 68.11, 2 frames over 25 ms |
| Reading | One bad packet per frame costs nothing visible; a 1000/s bad flood drops the server to about 24 fps for its duration and recovers within a second after. The log has no cap or dedupe: nothing in Blink limits it. |
Rate limiting and kicking must happen before or around the generated receive (G5/G6).

## 4. Payload bytes (computed from the harness byte writers, not measured by Stats)
| Payload | Bytes |
| --- | --- |
| RedeemCode "ABC123" (redeem_ok) | 8 (1 id + 1 len + 6) |
| EchoDelta (delta_ok, 1 cell, 1 label) | 35 |
| RequestFire (fire_ok, gear "rocket") | 64 (+ 1 Instance in the second remote arg) |
| ReportView (view_ok) | 25 |
Stats/MicroProfiler remote traffic was not read: not measured.

## 5. Surprises and reproduction
| Surprise | Reproduced |
| --- | --- |
| spam_api_unreliable_1000 received 1000/1000 (RUN.md expected N below 1000) | Yes: second independent run, raw `OnServerEvent` count on both remotes, 1000 unreliable + 1000 reliable at about 1000/s: 1000 / 1000. Solo play has no real network, so the engine throttle (`remote.md:403-405`) may drop on a real client; not tested here. |
| last_arrival_after_s is 0.97 for all three spam runs (equals the send time; no delay seen) | Yes, same in the second raw count run (send took 0.97 s and 1.03 s). |
| Second harness run is not possible without reopening: the client runs once on `P1Run` | n/a, used custom `execute_luau` senders for the repeats. |
| An earlier raw-count attempt that ran the two MCP calls in parallel counted 0 on both remotes (timing of the two calls, not a Blink effect); redone in sequence. | Discarded. |

No harness edits. Output errors outside P1 lines: `ContentId: rbxassetid://203785492 failed due to: Asset type does not match requested type` (3 times at start, Studio default asset, unrelated).
