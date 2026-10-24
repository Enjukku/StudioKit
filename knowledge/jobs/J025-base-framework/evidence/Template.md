---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-S7
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Template + new_game.py: evidence (J025-S7)

Artifact: `roblox-game-framework/template/` (28 files) and `tools/new_game.py`, files as of 2026-10-24 (uncommitted, rule 7). Framework working tree (no commit exists, so `--ref` is optional; default = working tree). Rojo 7.7.1, Blink 0.18.9, Lune 0.11.1, luau-lsp 1.70.1.

## C1 one command
`python tools/new_game.py --name Coinsville --out <scratchpad>/Coinsville`: 20 s wall. Steps: template copy (name filled) → framework dev tools (tools/spec, tools/types, jest.config, roblox-std.yml) → `install.py` (13 blocks, 27 files, lock) → README packages row filled from the lock → `rokit install` → `wally install` → `python tools/gate.py --transport`. Tail: `gate: 15.4s / RESULT: PASS / Created Coinsville ... Next: 1-5`.

## C2 gates
- Game gate (plain run after creation): transport, format (17 files), lint, rules, types (0 errors, 17 files), specs (3 files, 10 passed), build (game + test place), lock (27 files) PASS; engine SKIP (2 Jest specs listed); `RESULT: PASS` in 12.5 s.
- `python Framework/check_lock.py .`: PASS (27 files). Framework gate after the change: `RESULT: PASS` (20.7 s).

## C3 success test traced
| Step | Template file:line | Proof |
| --- | --- | --- |
| 1 join, load with session lock | `src/server/Main.server.luau:5` boot; `Systems/Save.luau:10` `Session.start(Schema)` | Session Lune specs (framework gate) + `src/server/Success.engine.spec.luau` (status ready; written, not run) |
| 2 validated remote changes saved state | `net/game.blink:13-17` (string 1..32); `Systems/Core.luau:14` Net.guard; `Systems/Coins.luau:23` Net.answer (rate 4/s burst 8, ready, finite); `Systems/Coins.luau:15` `Save.handle:update` → `Rules/Coins.luau:15` (known source, cap) | `Rules/Coins.spec.luau` (4 rows on the real CoinSources), `Save/Schema.spec.luau` (5), Net Lune specs; engine: `Success.engine.spec` (done + refusal writes nothing), `src/client/Hud.engine.spec.luau` (real Invoke) |
| 3 state reaches the owner | `Systems/Core.luau:27` State.track(`Schema.view`); client `Systems/Core.luau:10` State.client | State Lune specs (framework); `Success.engine.spec` (Atoms entry = view) |
| 4 UI shows it | `src/client/Systems/Hud.luau:68-72` label from `State.mine`; `:86` Invoke with pending text and reason lines | `Hud.engine.spec` (label = new server value; refusal leaves it), not run |
| 5 leave, data saves | Session (framework) on leave and BindToClose | Session Lune specs + Session engine row S-T17 (not run) |
| 6 (Studio, 2 clients) | whole flow | step 8 (lead) |

## C4 new base code a game writes = 0
Sample adds game rules only: `Rules/Coins.luau` (24 lines rule), `Systems/Coins.luau` (one Net.answer + one update call), `Save/Schema.luau` (data), `Content/CoinSources.luau`, `Hud.luau` (screen). Base wiring every game keeps ships in the template: server `Systems/Core.luau` (guard, State, hydrate, view), client `Systems/Core.luau`, the two entries, `Systems/Save.luau`. No framework file edited (lock PASS).

## Placement facts (built .rbxlx read back)
Game place: Main scripts RunContext Server (1) / Client (2) via `emitLegacyScripts: false`; `Workspace.PlayerCharacterDestroyBehavior` = 2 (Enabled, `_api-reference/enums/PlayerCharacterDestroyBehavior.yaml:30-35`; T-2 done); no `LoadStringEnabled`; no spec, ContentTests or DevPackages. Test place (gate-written from default.project.json, EC-15: one project file): `LoadStringEnabled` true, specs, ContentTests, DevPackages, jest.config under `ServerScriptService.Server`.

## Planted faults (each alone, in the created game; 10/10 caught)
Specs: duplicate CoinSources id (CT-T6) · NaN coins · cap off by one · unknown source accepted · migration drops Cash · validate lets fractions in. Gate: blink edited without `--transport` (transport FAIL) · Framework file edited (lock FAIL) · spec in `Systems/` (rules FAIL) · `Invoke(5)` (types FAIL) · unranged `f64` (schema lint FAIL, names the line).

## Tickets answered
T-2 done (above). T-5 done: ContentTests is mapped only in the test place at `ReplicatedStorage.Framework.ContentTests`; specs require `@game/ReplicatedStorage/Framework/ContentTests/Check`; the gate's rules check fails any non-spec that requires it. T-3 not done: no test-only entry that waits for PlayerAdded (recipe stays in `Loader.multiclient.engine.spec.luau`; step 8 builds it if it runs L-T12).

## Not done / open
- Admin: `src/Admin` had no specs or evidence when wired (B8 working). One marked line: `template/src/admin/Pages.luau:4` (ADMIN-PENDING); the page data (give_coins) is in place; `Framework/Admin` is installed but not mapped in `default.project.json`.
- Framework type friction: `Net.Policy` literal without `beforeReady` fails luau-lsp in `Net.answer` (`Expected 'Policy', got '{ burst, name, rate }'`); the template writes `beforeReady = false`. A frozen policy table also fails (read-only fields). Contract usage example omits it.
- The generated Client module has 2 luau-lsp errors of its own (`Remotes.luau:368, 399`); the game gate ignores type errors inside the two generated files only.
- Dev tools copied by new_game.py (tools/spec, tools/types, jest.config, roblox-std.yml) are not lock-checked.
- Jest may load game modules fresh in the engine lane: `Success.engine.spec` then fails at `Save.handle` defined (reads as BLOCKED, not a false PASS).

## T-14 (2026-10-24, feature-builder): Admin wiring, dev-tool locks, engine roots, deprecated check
- Admin wired (ADMIN-PENDING gone): `default.project.json` maps `ServerScriptService.Framework.Admin` (all of Admin, its client too: CC-19; the built place shows `Framework/Admin/Client` as a Script under ServerScriptService, `ServerStorage/AdminPages/Pages`, no `test` folder: rbxlx read). `src/server/Systems/AdminSetup.luau` starts Admin with `client = ReplicatedStorage.Shared.Remotes` (CC-16 link), `Remotes.Framework.Admin*`; `src/server/AdminActions.luau`: `allow` (PROPOSAL: empty; Studio -1 and the user creator are admins) and `give_coins` (Studio only, else `studio_only`; grant through `Save.handle:update` with `Rules/Coins.grant`, cap `coins_full`).
- Spec `src/server/AdminActions.spec.luau` runs the real `Framework/Admin` on Admin's fake world (`Framework/Admin/test/World.luau`, `root = "Framework"`): admin give_coins `done` (+500 saved), non-admin `not_admin` (nothing written), outside Studio `studio_only`. Plants in ProofGame: Admin caller check off -> :50 red; studio check off -> :56 red; grant adds nothing -> :44 red (and Coins.spec :44).
- To make that possible `install.py` now copies block `test/` helpers (no specs) to `Framework/<Block>/test/` (locked); the game project ignores `**/test` and `**/test/**`; the game gate's test project keeps them (test place + sourcemap only).
- T-11: `install.py` copies and locks `check_lock.DEV_TOOLS` (tools/spec, tools/types, tools/engine/jest.config.luau, roblox-std.yml); `new_game.py` no longer copies them. Copy-tool tests 9 -> 11 (red first: file list lacked the tools; reinstall FileNotFoundError). Plant in ProofGame: one line added to `tools/spec/run.luau` -> `lock FAIL tools/spec/run.luau: edited`.
- T-12: `tools/engine/run_jest.luau` runs every root of {RS.Framework, SSS.Framework, SSS.Server, RS.Client} that holds a `jest.config`; the game gate's test project adds `jest.config` to `ReplicatedStorage.Client` (Hud.engine.spec). Not run in Studio.
- T-13: both gates' types check count `DeprecatedApi` (framework: in src/ only). Plants: `wait(1)` in `src/Admin/PlantDep.luau` -> framework types FAIL; `spawn(...)` in ProofGame `src/server/PlantDep.luau` -> game types FAIL.
- Proof: `python tools/new_game.py --name ProofGame --out C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew-Downloads-uterd-StudioKit\4efeb851-8fbc-4f57-a493-b5ce86b15d6d\scratchpad\ProofGame` -> game gate `RESULT: PASS` (specs 4 files, 14 passed; lock 44 files).
