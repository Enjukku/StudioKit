---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: studio-operator · claude-sonnet-5-5 · medium · 2026-10-24

# J025 probes P2-P5: verdicts

All checks MCP-verified unless marked. Probe place: `probes/p2-5-engine/probe-engine.rbxl` (rojo 7.7.0 build). studio_id used: `4f4adf4d-bfa2-4d50-b56b-26b8bee2c010` (first window, Jest edit lane + failed server lane), then `44e398c1-50e0-422d-8ad7-62dde30b1244` (rebuilt place with LoadStringEnabled; all later runs). P5 child entries (listed only while a test runs): server `10819e65-5a79-4c87-b999-fa86f20d8269`, client `c5c07613-875c-4652-b9b4-bed2d9878107`. The two game windows were never targeted (their ids were never passed). Probe window (pid 1885336) closed at the end; the two game processes (269876, 822904) still running.

## P2 Open Cloud Luau Execution: BLOCKED (no key)
`knowledge/design/keys.json` is blank, so nothing was tried. Per brief nobody was asked.
Follow-up for the owner (later, not now): one Open Cloud API key, scopes `universe.place.luau-execution-session:write` and `universe.place.luau-execution-session:read` (shape-test-tooling.md §3), restricted to the test universe/place. Open questions still untested: DataStore/ConfigService inside a task, Jest under the "Luau Execution" RunService context, `loadstring` there.
Means for the framework: the Jest merge lane in CI is not proven. The Studio lane below (P3) is the lane we can prove today.

## P3 Jest in Studio: PASS in the Edit data model; PASS in the play-test Server data model only with `LoadStringEnabled = true`
Package: `roblox/jest` + `roblox/jest-globals` **3.20.1**, from the Wally index (`wally.toml` dev-dependencies; `wally install` downloaded 51 packages). 3.21.0 does not exist (`No packages were found that matched roblox/jest@>=3.21.0`). Chosen over `jsdotlua/jest` 3.10.x because the roblox one is on the index at the newer version, so the fallback was not needed.
Specs: 5 passing tests (basic, require ReplicatedStorage module, require ServerScriptService module, `task.wait(0.25)`, ProfileStore 1.0.3 mock start+end) + 1 deliberate failure. `ProfileStore.luau` copied unchanged from GWS `_Index/lm-loleris_profilestore@1.0.3`.

| Lane | Command | Result (Output / return, quoted) |
| --- | --- | --- |
| (a) MCP `execute_luau`, Edit DM (plugin context) | `Jest.runCLI(ReplicatedStorage, {ci=true}, {ServerScriptService.Specs}):await()` (`tools/run_jest.luau`) | `[Edit] wall=0.42s suites=5 suitesFailed=1 tests=6 passed=5 failed=1 success=false`; second run `wall=0.42s tests=6 passed=5 failed=1`. Output: `Test Suites: 1 failed, 4 passed, 5 total / Tests: 1 failed, 5 passed, 6 total / Time: 0.415 s` |
| (b1) play-test Server DM, place without LoadStringEnabled | same | **FAIL** (twice): `suites=5 tests=0`, every suite `Test suite failed to run ... jest-runtime:1190: loadstring() is not available` |
| (b2) play-test Server DM, `ServerScriptService.LoadStringEnabled = true` | same | `[Server] ok=true wall=0.50s suites=5 suitesFailed=1 tests=6 passed=5 failed=1`; run 2 `wall=0.42s ... passed=5 failed=1` |

- `LoadStringEnabled` is NotScriptable: neither a plugin (`execute_luau` Edit) nor a script can set or read it (`LoadStringEnabled is not a valid member`). It was set through Rojo `$properties` in `default.project.json` and the place rebuilt. Play-lane tests therefore need it in the project file of the test place.
- Spec needs: a `jest.config` ModuleScript (`return { testMatch = {"**/*.spec"} }`) in the spec folder, or runCLI errors `Could not find a config file`. Specs are named `<name>.spec`.
- Strict type check: `luau-lsp analyze --definitions=tools/globalTypes.d.luau --sourcemap=sourcemap.json --ignore "DevPackages/**" --ignore "vendor/**" src` = **0 errors** on all 6 `--!strict` specs (`tools/analyze-after-wpt.txt` is empty). Two traps found with negative controls: (1) without `wally-package-types --sourcemap sourcemap.json DevPackages/` the Wally link file makes `JestGlobals` type `any`, so errors like `local e: string = JestGlobals` and `JestGlobals.noSuchThing()` pass silently; after it they are flagged. (2) Even then Jest matchers are typed `(...any) -> nil`, so `expect(1).toBeCloseTo("a")` and `expect(1).toBe()` are NOT flagged. Strict covers the spec's own code and the module API, not matcher arguments.
- In spec: `require` of ServerScriptService and ReplicatedStorage modules, `task.wait` and the ProfileStore mock all worked. ProfileStore printed `[ProfileStore]: Roblox API services unavailable - data will not be saved` (harmless; the Mock path is used). Not tested: the real DataStore path.
- Meaning: test lane for server code = Studio MCP `execute_luau` in Edit (no play needed, 0.4 s, plugin context). Play-test Server lane works if the test place has `LoadStringEnabled=true`. CI headless remains P2.
- Alternative if later needed: none required; jsdotlua/jest not tried.

## P4 Animation markers and replication: PASS (Anim API shape confirmed, one trap)
Setup: KeyframeSequence `P4Seq` (4 keyframes 0/0.5/0.8/1.0 s, markers `MarkA`@0.5 with value `p_MarkA`, `MarkB`@0.8), registered with `KeyframeSequenceProvider:RegisterKeyframeSequence` (returns a 32-char hash string, not an `rbxassetid`). Server rig: `Players:CreateHumanoidModelFromDescription(..., R15)`. Solo player `Enjukku`.
1. Marker on the playing side (server, `Play(0)`): MarkA fired at 498.4 ms after Play (want 500, err -1.6 ms), MarkB 814.9 ms (want 800, err +14.9 ms; TimePosition at fire 0.817). Run 2: err +16.6 ms both. Spread is one frame (about 16.7 ms). Param string arrived (`p_MarkA`).
2. Server rig track seen by the client: yes. Client `Animator.AnimationPlayed` fired about 50 ms after the server Play (106.577 -> 106.628) with the server's temporary hash id, and `GetMarkerReachedSignal` fired on the client for both markers (TimePosition 0.500/0.817, 0.504/0.804) on every run. So server-registered temporary ids resolve on the client for replicated tracks. First play: `track.Length` was 0 in the AnimationPlayed handler (1 on later plays), so never read Length there.
3. Client track on its own character: server saw `Animator.AnimationPlayed` 65 ms later with the client's id (`cc003b45...`, client registered the same sequence and got a different hash than the server) and `GetPlayingAnimationTracks()` on the server listed 2 tracks (idle + custom), dropping to 1 when it ended.
4. `LoadAnimation` twice with the same Animation: **two different tracks** (`t1==t2 false`; a second Animation instance with the same id also gives a different track). `GetTrackByAnimationId(id)` returned **nil** even after both loads (before Play), so it cannot serve as a "loaded" cache lookup in the server context; cache in the module.
5. Trap (reproduced 3 times, rig P4Rig run 2, P4RigA replay, P4RigB plays 2 and 3): on the client, a server rig that plays the same animation id again gives the SAME client track object (identity probe: `track#1` both times) and `AnimationPlayed` fires again. Connecting `GetMarkerReachedSignal` inside each `AnimationPlayed` stacks handlers: markers fired once, then 2x, then 3x. The loaded-twice case itself did not duplicate (P4RigB first play: once). Meaning for `Anim`: connect marker handlers once per track object (keep a set of tracks) or disconnect on `Ended`; never per play event.
Meaning for framework: `Anim` as sketched in state-ui-animation.md §7 holds (caller names the Animator; load once; markers by name). Add: dedupe on track object. Temporary-id fallback was not needed.
Limits: solo Play only, one client; no real uploaded asset; priority/fade effects not measured.

## P5 Multi-client from MCP: PASS with 1 client; 2 clients NOT tried (memory)
- Start: `StudioTestService:ExecuteMultiplayerTestAsync(1, "P5:1:<hold>")` called from MCP `execute_luau` in the Edit DM works (plugin security OK). Wrapped in `task.spawn`; the call yields until the test ends, so the result is written to a ServerStorage attribute and read later. 3 runs, all started and ended: `ok=true res=P5-OK players=1 after=23.5s`; `after=61.4s` (hold 45); `ok=true res=P5-ENDED-FROM-MCP-SERVER after=38.7s`.
- Windows: while a test runs, `list_roblox_studios` shows two extra entries with `name: null` (server and client); they appear about 25-40 s after launch (boot time) and disappear when the test ends. Early polls showed the entries but `get_studio_state` said "not connected" until they finished booting. The Edit studio_id stays listed but `get_studio_state` says `Mode: Edit, DataModels: Edit` during the test (the test runs in separate processes). Process window titles: `Server - Roblox Studio`, `Place1 - Roblox Studio`.
- Output per side: `get_console_output` on each child id worked. Server: `[P5-SERVER] test args = P5:1:100, want 1 clients` / `players joined = 1 after 7.5s` / `player Player1`. Client: `[P5-CLIENT] Player1 sees P5 flag, replicated players = 1`. `execute_luau` also works on each child (server id with `Server`, client id with `Client`): `server DM: players=1 [Player1] P5flag=true`, `client DM: local=Player1 players=1 P5flag=true`.
- End: `StudioTestService:EndTest(str)` on the server returns `str` as the value of `ExecuteMultiplayerTestAsync` (string). It works from a server Script and from MCP `execute_luau` (Server DM) (first call wins). Both child processes exit within 8 s and free their memory. The hold script in the place used `GetTestArgs()` on the server only (client `GetTestArgs` has a known issue); the client learned the state from a replicated Workspace attribute.
- Memory (free physical MB, this PC): before launch 1258; peak load dips measured 95 (run 1), 41 (run 2), 360 (run 3, later sample); during steady test 772; after the test 3429; after closing the probe window 5322 (other apps had also freed). Process sizes during: probe window 2037-2351 MB, Server 1535-1612 MB, client 1462-1685 MB. One client alone pushed free memory under the 300 MB limit in 2 of 3 runs, so **2 clients were not started** (not verified; expect it to fail on this PC).
- Meaning for step 8 (2-client proof): the lane is Edit-DM `execute_luau` start (task.spawn) + a server Script with `GetTestArgs`/`EndTest`, read each side's Output through the child ids, and read the result from the attribute. It needs about 3.2 GB of extra RAM per client pair on top of the Studio window; the PC needs the game windows closed first, or the 2-client proof runs on a larger machine or the owner's. Alternative if memory keeps blocking: 1-client scenario plus a second client emulated by a server-side fake player flow for the remote path (weaker, not a replacement for replication).

## Harness files
`default.project.json`, `rokit.toml`, `wally.toml`/`wally.lock`, `src/` (specs, modules, `P5Server.server.luau`, `P5Client.client.luau`), `vendor/ProfileStore.luau` (unchanged copy), `tools/run_jest.luau`, `tools/globalTypes.d.luau`, `tools/analyze-after-wpt.txt`. P4 runs were done as inline `execute_luau` snippets (not saved as files).
