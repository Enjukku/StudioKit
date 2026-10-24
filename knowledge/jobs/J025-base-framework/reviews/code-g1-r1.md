---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-24

# Review: framework code G1 rev 1 (J025-R-G1), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\src\` (repo uncommitted by rule 7; revision = the sha256 below, files as of 2026-10-24). Depth: standard (no saves, money or client input in these ten blocks). Round 1. Code read before `evidence/<Block>.md`.

Goal questions: (1) Does every connection, thread, instance and per-key entry have an owner that cleans it (README rule 3, Q5)? (2) Can any path show a client a state that is not true (St2 another player's private entry; Sc3/Sc5 a screen that cannot close)? (3) Is the hot-path cost in our code or in a package (Q6)? (4) Is every engine name real and current (Q8, rule 1)?

## Files reviewed (sha256, first 16 hex)

| Block | File | sha256 |
| --- | --- | --- |
| Helpers | src/Helpers/Amount.luau | 6dc6916cd2aff903 |
| Helpers | src/Helpers/Ledger.luau | 934f2afb4bc98bb2 |
| Helpers | src/Helpers/RateLimit.luau | dd819c6e7aa011d0 |
| Types | src/Types/init.luau | 13d68fb0f5bf4401 |
| Analytics | src/Analytics/init.luau | c5bb5bd5f078648a |
| Loader | src/Loader/init.luau | 31cac3d34482de57 |
| Config | src/Config/init.luau | 714fc4b95334cce4 |
| Motion | src/Motion/init.luau | f54b01510a165a70 |
| ContentTests | src/ContentTests/Check.luau | c97bcc33db363226 |
| State | src/State/init.luau | 152ec952acd33a5d |
| Screens | src/Screens/init.luau | f0cc4fbb42598a20 |
| Anim | src/Anim/init.luau | 09f6170613869733 |

Also read: `Packages/_Index/littensy_charm-sync@0.4.1/charm-sync/src/server.luau` (all), `patch.luau:59-80`, `config.luau`.

## Verdict per block

| Block | Verdict | Why |
| --- | --- | --- |
| Helpers | ready | Every input class (NaN, inf, negative, fraction, non-number, broken clock) traced to a safe result; 8 functions + MAX as contracted |
| Types | ready | Types only; matches README shared-types block |
| Analytics | fix-first | F2 only (T-1, lead decision; one line + one test case). Rest clean |
| Loader | ready | Yield detection, cycle path, duplicate names, holes in After all traced; failure kicks present and later players |
| Config | ready | N1 is contract text, not code |
| Motion | ready | CC-2, CC-3 accepted (below) |
| ContentTests | ready | CC-1 accepted (below) |
| State | ready | St2 filter holds per key; cost ruling below (no finding: PROPOSAL budget, engine number pending T-7) |
| Screens | fix-first | F1 |
| Anim | ready | Track cache, marker connect-once, observer leak paths traced |

## Gate (run once by the reviewer, 2026-10-24)
`python tools/gate.py` last line: `RESULT: FAIL` ("gate: 16.8s, failed: format, types"). Every failing line is in `tests/acceptance/Session/*` (12 format, 9 type errors: QA's in-progress Session hard tests, out of this scope). For the ten blocks: lint PASS, rules PASS (65 files `--!strict`), specs PASS (216 passed, 0 failed), build PASS, copy-tool PASS; engine lane SKIP (Studio only). Label: gate-verified for the Lune lane; engine lane not verified.

```text
<spec>
artifact: roblox-game-framework/src/{Helpers,Types,Analytics,Loader,Config,Motion,ContentTests,State,Screens,Anim}@rev1 (sha256 table above)
reviewer: reviewer
looked_at_first: [the 12 module files above, contracts/<Block>.md and README.md, charm-sync 0.4.1 server.luau, then evidence/<Block>.md]
findings:
  - {id: F1, class: blocking, where: "src/Screens/init.luau:222-233 and :139", expected: "Sc3/Sc5: a close cleans once; never two copies; every open can be closed (README rule 3)", observed: "Screens.open runs def.build (:222) before the entry is in openList/byId (:231-232). Sequence A: build calls handle.close() (a screen that decides it has nothing to show) -> closeEntry sets closed=true, then table.remove(openList, table.find(openList, entry)) with find = nil removes the LAST element of openList (Luau optional pos = #t) -> the newest other open (e.g. the HUD) leaves openList but its ScreenGui stays on screen, its janitor never runs, byId still names it, and a later close(id) of it repeats the wrong removal; then open inserts the already-closed entry (:231): its gui shows, closeEntry returns early for it forever, blocking stays true and ScreensNav keeps sinking ButtonB. Sequence B: build yields (e.g. WaitForChild on a template not yet replicated) and the player presses the same HUD button again -> second open finds byId[id] nil -> two copies of one id (Sc5).", evidence: "Medium (structure; play-breaking in A). Code read + Lune probe: table.remove({'a','b','c'}, nil) removed 'c', #t 2. No guard elsewhere: contract does not forbid close-in-build or a yielding build; Sc-T10 covers only a throwing build.", smallest_fix: "closeEntry: remove only when table.find returns an index. open, after the pcall: if entry.closed then gui:Destroy() return handle end; and if byId[id] is set again (yielding build), close it before inserting.", protect: "Sc-T4 janitor cleaned exactly once; Sc-T10 build-error path; Q5 1,000-cycle counts", retest: "two Lune cases: build calls handle.close() with a Hud open -> Hud still in view.open and closable, nothing left in PlayerGui for the closed id; build yields, open(id) twice -> one copy"}
  - {id: F2, class: blocking, where: "src/Analytics/init.luau:251", expected: "T-1 lead decision; An3 spirit: non-finite numbers are not sent", observed: "Analytics.custom(player, 'AvgDamage', total / count) with count 0 passes NaN (or inf) straight to LogCustomEvent(value: double) -> the dashboard sum/average for that event is poisoned, or the engine throws and it only shows as an error count", evidence: "Low harm (no player-facing effect); blocking only because the lead decided T-1. Code read: value is forwarded unchecked; Amount.whole is wrong here (custom values may be negative or fractional)", smallest_fix: "first line of custom: if value ~= nil and value - value ~= 0 then return end (same 'not sent' rule as An3; a sampled warn is optional, not needed)", protect: "An-T1 unknown-name path; negative and fractional custom values still sent", retest: "An-T3 adds custom NaN, inf, -inf: spy count 0; custom -2.5: sent as -2.5"}
  - {id: N1, class: recommendation, where: "contracts/Config.md Failure row 1 vs src/Config/init.luau:114-133", expected: "contract and code say the same", observed: "contract: after the last retry 'next UpdateAvailable or server restart tries again'; code connects UpdateAvailable only on a successful GetConfigAsync, so with no snapshot nothing can fire and the server keeps defaults until restart (the code's warn says so, :132)", evidence: "code read; ConfigService.yaml GetConfigAsync throws when no config is available; UpdateAvailable lives on ConfigSnapshot only", smallest_fix: "contract text at step 9: 'defaults until the server restarts'. No code change", retest: "none"}
keep: [Amount.whole/isWhole NaN-inf-negative handling; RateLimit clock that never moves back; Ledger single allocation; Loader yield detection by coroutine status + task.cancel and the cycle path; Config whole-cache swap and deep freeze; Motion two TweenInfos per row built once; State per-key wire filter (St2) and dirty-flag flush (idle 0 alloc); Screens janitor per open and alive(); Anim track cache + connect-once per track object; ContentTests sorted problem lines]
weakest_part: "Engine-side claims (PlayerGui at client init, InputContext under PlayerGui, real tween/animator behaviour) rest on the makers' engine specs I did not run; my review is static plus Lune."
could_not_check: [
  {step: "Screens.register in a client system's init does not yield", missing_input: "a real client boot: start() calls Players.LocalPlayer:WaitForChild('PlayerGui') (init.luau:153); if PlayerGui is not there yet, Loader L4 fails the whole client boot as 'yielded'. Docs examples always WaitForChild it (players/loading-screens.md:33)", closes_it: "step-8 proof client Output shows '[Loader] booted' with Screens registered in init (or a 1-line probe)", who: "studio-operator / qa-lead"},
  {step: "State same-UserId rejoin on one server", missing_input: "a run where the old Player's PlayerRemoving lands after the new Player's track: leave() would clear the shared '<id>' entry (init.luau:92-96)", closes_it: "two-device rejoin run", who: "qa-lead"},
  {step: "planted faults", missing_input: "I did not plant my own; makers report 14/11/13/9/5/6/7/10/13 red", closes_it: "qa-lead planted-fault pass", who: "qa-lead"},
  {step: "State cost at 50 players in the engine", missing_input: "engine capture", closes_it: "T-7", who: "performance-engineer / studio-operator"}]
verdict: fix-first
</spec>
```

## Lead rulings asked for

**State cost (0.15 ms per change at 50 players, budget 0.1 ms PROPOSAL).** Where it goes: both, and mostly charm-sync. Per flush charm-sync 0.4.1 rebuilds two maps of every tracked key (shared + private maps × players) and diffs them (`server.luau:192-207`), then allocates 3 tables per client in `selectFromGlobalPatch` (`:209-250`) and `task.spawn`s the send per client (`:357-369`). Our share: one charm-sync effect per player per private map re-runs on any change of that map (`State/init.luau:71-82`, `:154`), and the send wrapper allocates one `renamed` table per payload (`:129-133`). A shared change must reach 50 clients anyway (50 sends), so 0.1 ms is 2 µs per client including the send. No simple change in our code removes the O(players) term; switching charm-sync to `preserveHistory` trades the full diff for O(players²) update scans. Recommendation: no code change now; the budget is per change but the flush is per frame (several changes in one frame cost one flush), so set the budget per frame from the T-7 engine number. Not a finding.

**T-1.** Confirmed; smallest fix in F2. Do not use `Amount.whole` for custom values.

**T-6 (sampled warn duplicated).** Leave it. Three copies are the same 12 lines (Config :32, State :41, Screens :54); Analytics needs an injected clock for its specs (:81) and Anim warns once per session (:63), so one shared helper would need a clock option to serve them: an option for one user (`rules/anti-overengineering.md` 5). It would also add Helpers edges to State and Screens and change the frozen Helpers contract, with no gain for players. Reopen it if the 10 s window becomes a tuned value.

**CC-1** (ContentTests `Rows = {}`, `Row = { read [string]: unknown }`): accepted; gate types PASS with it, checks still refuse a non-table at run time (`Check.luau:38-41`). **CC-2** (Motion usage annotation): accepted, usage text only. **CC-3** (Motion reads `ReducedMotionEnabled` at each play): accepted; every new play sees the current setting, same as a change signal, with nothing to clean. A tween already running when the setting flips keeps its variant (at most 10 s, M1 cap). Contract M2 and the Lifecycle line should say this at step 9.

## Engine APIs checked against `_api-reference/` (all present, `deprecation_message: ''`)
GuiService.ReducedMotionEnabled, :Select, .SelectedObject; UserInputService:GetLastInputType, .LastInputTypeChanged; InputContext.Priority/.Sink/.Enabled; InputAction.Pressed; InputBinding.KeyCode; ScreenGui.ScreenInsets, .DisplayOrder; LayerCollector.Enabled, .ResetOnSpawn; Enum.ScreenInsets.None/DeviceSafeInsets; Animator:LoadAnimation, .AnimationPlayed; AnimationTrack:GetMarkerReachedSignal, .Looped, .Priority, .IsPlaying, .Animation; ContentProvider:PreloadAsync; AnalyticsService:LogCustomEvent (value double), :LogEconomyEvent (transactionType string), :LogFunnelStepEvent, :LogOnboardingFunnelStepEvent; Enum.AnalyticsEconomyFlowType.Source/Sink; ConfigService:GetConfigAsync, :SetTestingValue, :ClearTestingValue; ConfigSnapshot:GetValue, :Refresh (no Yields tag), .UpdateAvailable; TweenService:Create; Instance.Destroying, :FindFirstAncestorOfClass; RunService:IsStudio, :IsServer; Player:Kick; `require("@game/...")` (LuaGlobals.yaml:626). No `wait`/`spawn`/`delay`.

## Harm areas walked
1 saves: n/a (no block writes saves; Ledger/Amount pure, traced). 2 client gain: n/a except State hydrate (no args; rate in Net) and St2 (held: per-key subscription, rename on the way out). 3 money/policy: Analytics sends no user text (An6 held). 4 leaks/races: F1; State leave, Anim destroy, Config connection, Loader failure kick traced clean. 5 performance: State ruling above; others 0 alloc per call in hot paths. 6 structure: T-6 ruling. 7 APIs: list above. 8 over-building: API counts match contracts (Helpers 8, Analytics 5, Loader 2, Config 6, Motion 3, ContentTests 5, State 6, Screens 5, Anim 3); `_`-prefixed spec hooks only.
