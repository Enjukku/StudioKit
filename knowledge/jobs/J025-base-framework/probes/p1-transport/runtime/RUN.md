---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# P1 runtime harness: how to run it (solo play-test via Studio MCP)

What it checks in the engine: the Blink 0.18.9 server deserializer, fed hand-crafted buffers over the real `BLINK_RELIABLE_REMOTE` / `BLINK_UNRELIABLE_REMOTE` (the bytes an exploiter can send with `FireServer`), plus three 1000/s spam runs. The offline Lune run (`../offline/blink.out.txt`) already gives the same verdicts on stand-in datatypes; this run confirms them on engine `Vector3`, `CFrame`, `Instance` and remote replication.

## Files
| Path | Role |
| --- | --- |
| `default.project.json` | Rojo project; maps `../gen/blink/Server.luau` → `ServerScriptService.Net.BlinkServer`, `Client.luau`/`Types.luau` → `ReplicatedStorage.Net` (no copies) |
| `src/server/P1Server.server.luau` | listeners on every client event; prints `P1 <case> <accepted\|rejected> <detail>` per case |
| `src/client/P1Client.client.luau` | waits for `workspace.P1Run == true`, then sends every case bracketed by `P1Case` begin/end (RemoteEvents stay ordered across instances: `scripting/events/remote.md:377`) |
| `probe-transport.rbxl` | built place |

## Steps
1. Build (from `probes/p1-transport/scratch`, where `rokit.toml` pins the tools): `rojo build ../runtime/default.project.json -o ../runtime/probe-transport.rbxl`. Expect `Built project to probe-transport.rbxl`.
2. Open `probe-transport.rbxl` in Studio as the only probe window. `list_roblox_studios` → take the id whose name contains `probe-transport`. Never target the two game windows.
3. `start_stop_play` `is_start: true` (solo play).
4. `get_console_output`: expect `P1 server ready (Blink 0.18.9)`.
5. `execute_luau` Client: `return workspace:FindFirstChild("P1ClientOnly") ~= nil` → `true`. `execute_luau` Server: same code → `false` (the part exists only on the client; this is the missing-Instance case).
6. `execute_luau` Server: `workspace:SetAttribute("P1Run", true)`.
7. Wait about 30 s (34 cases × ~0.2 s, then 3 spam runs × ~4 s). `execute_luau` Server, in a loop with `task.wait(1)` inside, until `workspace:GetAttribute("P1Done") == true` (give up after 90 s → record RUNNER FAILED with the last P1 line).
8. `get_console_output`; keep the lines that start with `P1 `. Deserializer errors also print their own error and stack lines: expected, ignore them.
9. `start_stop_play` `is_start: false`; close the probe window.

## Expected Output lines for a pass
A pass = every line below appears with the same verdict and the detail fragment. "gap" rows are expected accepts that `Net` must reject itself (`../verdict.md` §3).

| Case | Verdict | Detail contains | Note |
| --- | --- | --- | --- |
| redeem_ok | accepted | `len=6 utf8=true` | |
| redeem_empty | rejected | `larger than or equal to 1` | |
| redeem_25_ascii | rejected | `smaller than or equal to  24` | |
| redeem_bad_utf8 | accepted | `utf8=false` | gap G3 |
| redeem_truncated | rejected | `out of bounds` | |
| delta_ok | accepted | `gym=1.5` | |
| delta_gym_nan / _inf / _ninf | rejected | `got nan` / `got inf` / `got -inf` | |
| delta_endsAt_nan_unranged | accepted | `endsAt=nan` | gap G1 |
| delta_bad_enum | rejected | `Unexpected enum: 7` | |
| delta_labels_9 | rejected | `smaller than or equal to 8` | |
| delta_cells_5000_unbounded_map | accepted | `cells=5000` | gap G4 |
| blob_256 / blob_257 | accepted / rejected | `len=256` / `got 257` | |
| fire_ok | accepted | `target=Workspace.P1Target` | |
| fire_origin_nan / _inf / _ninf | rejected | `magnitude of "Value.Origin"` | |
| fire_dir_nan | rejected | `magnitude of "Value.Direction"` | |
| fire_dist_inf | rejected | `"Value.Distance"` | |
| fire_gear_33 | rejected | `smaller than or equal to  32` | |
| fire_missing_instance_client_only | rejected | `Expected an Instance, got nil` | |
| fire_wrong_class | rejected | `of type "BasePart"` | |
| pick_ok | accepted | `target=P1Target` | |
| pick_cframe_nan / pick_cframe_inf | accepted | `aimPos=nan` / `aimPos=inf` | gap G2 |
| pick_vector_nan_unranged | accepted | `point=nan` | gap G1 |
| wrongtype_string_not_buffer | rejected | `buffer expected` | gap G6 (an error line per packet) |
| wrongtype_instances_missing | rejected | `attempt to index nil` | gap G6 |
| unknown_event_id_200 | rejected | `silent` | |
| batch_ok_bad_ok | accepted | `RedeemCode(len=3` and `then error` | gap G6: earlier events in a batch are already delivered |
| view_ok | accepted | `pos=5, 0, 0` | |
| view_pos_nan / view_look_ninf | rejected | `magnitude of "Value1"` / `"Value2"` | |
| spam_raw_reliable_1000 | `received 1000/1000` | `last_arrival_after_s` (record it: the engine throttle delays, never drops, `remote.md:378`) | gap G5 |
| spam_api_reliable_1000 | `received 1000/1000` | record `last_arrival_after_s` | gap G5 (Blink batches per Heartbeat, so ~60 packets) |
| spam_api_unreliable_1000 | `received N/1000` | record N; drops above the throttle are engine behaviour (`remote.md:403-405`) | gap G5 |
| done | `P1 done` | | |

A line that differs from this table: record the exact line, mark that case FAIL in `../verdict.md` §2, and do not change the harness to make it match.
