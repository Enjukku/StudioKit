---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: general-purpose · claude-sonnet-5-5 · medium · 2026-10-24

# J025 games reading: GreatWallSim (GWS) vs DestructionSimulator (DS)

Read-only. Paths: `GWS/` = `C:\Users\Firew\Downloads\uterd\GreatWallSim`, `DS/` = `...\DestructionSimulator`. Package paths are under `<game>/Packages/_Index/`. Line counts from `wc -l`. Labels: READ = source read; COUNT = grep/wc; NOT RUN = nothing was executed (no gate, no Studio).

## 0. Summary

| # | Finding | Evidence |
| --- | --- | --- |
| 1 | Both games run the same 5 packages (+3 transitive), identical source in both (only CRLF differs). Package code is MIT/Apache; no patches or forks of packages in either game. | `GWS/wally.toml`, `DS/wally.toml`; `wally.lock:1-48` |
| 2 | Save layer = ProfileStore (loleris, Apache-2.0) behind DataService (leifstout). Session lock, 300 s autosave, `BindToClose` are in ProfileStore. DataService adds **no migrations, no schema version, no receipts**. Both games reconcile only. | ProfileStore.luau:170-181, 2208; DataServiceServer.luau:196 |
| 3 | Networker has **no validation, no rate limit, no buffers**: varargs through one RemoteEvent+RemoteFunction pair per service. Both games put all validation in service handlers (`unknown` params), same convention. | NetworkerServer.luau:81-88 |
| 4 | Bootstrap, `Networkers.lua`, `PlayerSession` are copy-pasted between games (2 files byte-identical, 4 near-identical). RateLimit forked: GWS has `allowance` (+53 lines), DS does not. | section 2.1; `md5` compare |
| 5 | GWS is a UI-heavy meta game (58 generated Figma layouts, Charm in 38 files, 140 `DataService.server:` calls, full receipts); DS is a world/physics game (38,902 lines in `server/Bricks`, 16,360 content files compiled by tools, 2 Charm files, no purchases yet). The overlap is the thin infrastructure layer, ~600 lines. | section 2 |

## 1. Part 1: packages

Both games: `wally.toml:1-11` lists the same 5 deps. `wally.lock` is identical in both (CRLF aside). **Defect:** lock root package is `firew/roblox-blocks` (`wally.lock:11`) and `registry = "test"` (`:3`); the toml names are `firew/new-game` (GWS) and `firew/destruction-simulator` (DS). The lock is stale or copied from a third project. `Packages/*.lua` are wally redirectors.

### 1.1 Resolved versions and dependency tree (READ `wally.lock`, `_Index/` folder names)

| Package | Resolved | Transitive dependencies | Source lines | Licence file | `--!strict` |
| --- | --- | --- | --- | --- | --- |
| DataService | leifstout/dataservice 1.0.0 | janitor 1.18.3, Networker 0.3.1, ProfileStore (lm-loleris/profilestore 1.0.3), Signal 2.0.3 | 276+296+695+12+10 (`src/Data`, `DataServiceClient`, `DataServiceServer`, `DataServiceUtils`, `init`) | MIT, `dataservice/LICENSE` ("Leif Stout") | Server file yes (`DataServiceServer.luau:1`); Data.luau no header |
| Networker | leifstout/networker 0.3.1 | Signal 2.0.3 | 138+305+22+10 | MIT, `networker/LICENSE` | yes (all 3 files, `:1`) |
| signal | sleitnick/signal 2.0.3 | none | 432 (`signal/init.luau`) | wally.toml says MIT; **no LICENSE file** in `_Index/sleitnick_signal@2.0.3/signal/` (only `init.luau`, `init.test.luau`, `wally.toml`) | no header (nonstrict) |
| charm | littensy/charm 0.10.0 | none | 26+42+37+53+71+50+214+43+34 (`src/*`) | MIT-style, `charm/LICENSE.md` ("Copyright 2024 Littensy") | no header (nonstrict) |
| janitor | howmanysmall/janitor 1.18.3 | typed-promise 4.0.6 -> evaera/promise 4.0.0 (pulled even if unused) | 999 (`janitor/src/init.luau`) + FastDefer 33 + Promise 159 | MIT, `janitor/LICENSE` | yes (`init.luau:2`, plus `--!optimize 2`) |
| ProfileStore (transitive) | lm-loleris/profilestore 1.0.3 | none | 2242 (`ProfileStore.luau`) | **Apache-2.0**, `profilestore/LICENSE` (needs NOTICE/attribution if shipped as source) | typed (`export type` at `:970-1020`) |
| Promise (transitive) | evaera/promise 4.0.0 | none | `lib/init.lua` | MIT | no |

### 1.2 Public API and what it does (READ source)

| Package | API (3-6 lines) |
| --- | --- |
| DataService | `.server:init({template, profileStoreIndex, useMock, ...})` once (`DataServiceServer.luau:127-147`); `:get/:set/:update(player, path, cb)/:arrayInsert/:arrayRemove(player, path,...)` (`:480-612`) replicate each change to the client via Networker; `:getChangedSignal/:getIndexChangedSignal(player, path)` (`:629-688`); `:waitForData/:hasProfile/:getProfile` (`:420-462`); `:addPlayerRemovingCallback`, `:onPlayerInit` hook; global messages `sendGlobalMessage/addGlobalCallback` (`:257-293`). Client: `.client:init()` yields, `:get/:getChangedSignal/:waitForData` (`DataServiceClient.luau:40-270`). Paths are `string \| {string}`. |
| Networker | `server.new(tag, module, {methods})` makes one RemoteEvent + one RemoteFunction under `Networker/_remotes/<tag>` (`NetworkerServer.luau:46-92`); `:fire/:fireAll/:fireAllExcept/:fireRecipients/:set(players, key, value)`; client `client.new(tag, module)` yields until remotes exist (`NetworkerClient.luau:38-45`); `:fire(method, ...)`, `:fetch(method, ...)` (InvokeServer), `:getServerChangedSignal(key)`. |
| signal | `Signal.new/Wrap/Is`, `:Connect/:Once/:Wait/:Fire/:FireDeferred/:DisconnectAll/:Destroy` (`init.luau:153-409`). Batched yield-safe design (header `:1-5`). |
| charm | `atom(state)`, `computed`, `effect`, `subscribe(atom, cb)`, `observe`, `mapped`, `batch`, `peek`, `notify` (`charm/src/init.luau:15-26`). No React/Vide binding installed; no `charm-sync`. |
| janitor | `Janitor.new()`, `:Add(obj, method, index)`, `:AddPromise`, `:LinkToInstances`, `:Remove/:Cleanup/:Destroy` (`init.luau:162-995`). |
| ProfileStore | `ProfileStore.New(name, template)`, `:StartSessionAsync(key, {Cancel})`, `:GetAsync`, `:MessageAsync`, `Profile:Reconcile/:EndSession/:Save/:AddUserId/:MessageHandler`, signals `OnSessionEnd/OnAfterSave/OnLastSave`, `ProfileStore.Mock` (`ProfileStore.luau:19-166`). |

### 1.3 Risky or notable source (READ)

| Topic | Finding | file:line |
| --- | --- | --- |
| Session locking | In ProfileStore, not DataService. `SESSION_STEAL 40 s` (server waits then steals), `ASSUME_DEAD 630 s`, `LOAD_REPEAT 10 s`, `START_SESSION_TIMEOUT 120 s`. DataService passes `Cancel = player.Parent ~= Players` so a left player stops the retry loop. Well-known, battle-tested design. | ProfileStore.luau:170-175; DataServiceServer.luau:149-155 |
| Retries / critical state | ProfileStore only: 5 errors in 120 s -> critical state; backoff in `SaveProfileAsync` (`:930`). DataService adds no retry and no error surface of its own; `OnError`/`IsCriticalState` are not forwarded or used by either game (COUNT: 0 uses). | ProfileStore.luau:177-179 |
| Autosave | 300 s (`AUTO_SAVE_PERIOD`). DataService never calls `:Save()`; GWS StoreService calls `profile:Save()` itself for receipts. | ProfileStore.luau:170; GWS StoreService.luau:273 |
| BindToClose | Exists inside ProfileStore (`:2208`, sets `IsClosing`, saves all with reason "Shutdown"). DataService has **none** of its own (grep: 0). | ProfileStore.luau:2199-2226 |
| Migrations | **None.** Only `profile:Reconcile()` on load (fills missing keys). No version field handling. | DataServiceServer.luau:196 |
| Load failure | Kicks player ("Profile load fail"); `OnSessionEnd` kicks too. | DataServiceServer.luau:190-199 |
| **Bug: waitForData hangs** | `_playerRemoving` returns early when no profile exists (`:298-300`) so the `_waitSignals[player]` signal is never destroyed or fired. A player whose load failed leaves a suspended thread and a strong ref to the `Player` forever. Both games' `PlayerSession` call `waitForData` for every join (`PlayerSession.luau:43`), so the `not hasProfile` branch at `:48` is unreachable on load failure. | DataServiceServer.luau:295-323, 448-462 |
| **Bug: custom prefix ignored** | `asyncGetProfile` builds the key from `DATA_PREFIX` not `_getProfileKey`. Unused by both games (COUNT 0). | DataServiceServer.luau:394-397 |
| Client-callable by default | DataService exposes `self.get` to every client (`Networker.server.new("DataService", self, { self.get })`). Path is not validated; a bad path errors inside the remote. Returns only the caller's own data. | DataServiceServer.luau:132 |
| Replication cost | `init` sends the whole profile table to the client; every `set/update` re-sends the full value at that path (e.g. whole `Upgrades` or `PurchaseIds` table). No diffing, no buffers. | DataServiceServer.luau:402, 503, 537 |
| Networker validation | None. Server callback runs `access.method(access.module, player, ...)` with raw varargs; unknown method only `warn`s (attacker-triggerable log spam). | NetworkerServer.luau:81-88 |
| Networker serialization | Plain RemoteEvent/RemoteFunction args; **no `buffer`** (COUNT 0 in package). `fetch` = `InvokeServer`, no timeout. `set` values are not cached for late joiners (GWS works around it with `seq`: NetController.luau:5-8). | NetworkerClient.luau:112-118 |
| Networker client side | `assert(module[method])` on any server push of an unknown method. | NetworkerClient.luau:62 |
| Remotes folder | Created at runtime inside the package: `Networker/_remotes` (`NetworkerServer.luau:7-11`), so remotes are not in the Rojo tree. | |
| Signal / charm typing | Not `--!strict`; types are in annotations only. Janitor, Networker, DataService server are strict. | files above |
| Studio mock | Both games default `STUDIO_USE_MOCK = true`: Studio never exercises the real ProfileStore path. | GWS DataService.luau:27; DS DataService.luau:27 |

### 1.4 How each game uses each package (COUNT = files under `src/` with `require(...Packages.<name>)`)

| Package | GWS files | DS files | Wrapper module | Patches / workarounds |
| --- | --- | --- | --- | --- |
| DataService | 12 (11 client + server wrapper) | 3 (`HudController.luau:31`, `init.client.luau:15`, `Services/DataService.luau:17`) | `src/server/Services/DataService.luau` (41 lines, identical shape in both): calls `init` once, sets store index (`"GreatWallSim_v1"` / `"DS_Production_v1"`, `:22`), mock in Studio (`:27,37`) | Store index bump = data wipe (GWS `ProfileTemplate.luau:6-8`). GWS `Sound.luau:746` pcall-requires DataService from audio code. Server calls: 140 `DataService.server:` sites in GWS, 22 in DS. |
| Networker | 6 (client: `MetaController:31`, `NetController:19`, `WalkSpeedController:25`, `MechClimbController:45`, `RideController:25`; server `Net/Networkers.luau:25`) | 6 (client `BrickRenderController:45`, `DevStageController:23`, `PickupController:59`, `WeaponController:54`; server `Networkers.luau:25`, `PickupService.luau:104`) | `src/server/Net/Networkers.luau` (71 lines, **byte-identical** in both): registry reads each service's `clientAccess = {"name"}` and calls `Networker.server.new` | `clientAccess` is opt-in per service (GWS 16 services, DS 3: BrickWorld, Weapon, DevStage). DS DevStage sets `clientAccess = {}` outside Studio (`DevStageService.luau:42`). |
| signal | 21 | 3 | none | none. Typical: `PlayerSession.PlayerReady` (`PlayerSession.luau:19`). |
| charm | 38 | 2 (`HudController.luau:30`, `UI/EconomyState.luau:9`) | none; atoms live in `client/State/{GameState,InputState,MetaState}.luau` (GWS, 122/25/98 lines) | GWS comment: "Charm calls listeners in no fixed order" (`NetController.luau`, dam shape set before subscribers). DS `client/State/` is an empty folder; its one atom sits in `UI/EconomyState.luau` with a note (`:9-12`). |
| janitor | 84 | 41 | none | GWS: 108 `Janitor.new()`, 568 `janitor:Add` lines; DS: 64 and 251. |

## 2. Part 2: each game's own shared code, side by side

### 2.1 Bootstrap and load order

| Aspect | GWS | DS | Same / differs |
| --- | --- | --- | --- |
| Server entry | `src/server/init.server.luau` (91) | same (111) | Same 3-phase logic (require+`init` all, `start` all, register Networkers). DS adds Studio-only dev tools block (`:93-111`). |
| Client entry | `src/client/init.client.luau` (75): `DataService.client:init()` first (`:18`), then controllers | same (89) | GWS adds a `Rides` folder fallback (`:22,35-37`); DS adds a Dev block (`:73-89`). |
| Order lists | `Bootstrap/LoadOrder.luau` 21 services; `ControllerOrder.luau` 24 controllers | 8 services; 9 controllers | Hand-ordered string lists; comments say "add below dependencies". No dependency declaration or cycle check. |
| Failure policy | each `require`/`init`/`start` in `pcall`, `warn` and **continue** (`init.server.luau:38-56`) | same | A failed `DataService:init` leaves the server running with no saves (only a `warn`). |
| Wrapper contract | service = table with `init(self)`, `start(self)`, optional `clientAccess` | same | Same. `PlayerSession` is identical (76 lines) and is the "ready gate" for every other service. |
| Tests | none for bootstrap, `Networkers`, `PlayerSession`, `DataService` wrapper | none | Both: no specs (`tools/tests/luau/` has no such file). |
| Quality | Boot duplicated in both games (diff = dev block only). Client `ControllerOrder` GWS comment-per-line carries design ids (D-042...). | | |

### 2.2 Saves

| Aspect | GWS | DS |
| --- | --- | --- |
| Schema file | `server/Domain/ProfileTemplate.luau` (121): 31 flat PascalCase keys + 29 frozen path constants (`:88-119`) | `server/Domain/ProfileTemplate.luau` (46): 4 nested groups, `schemaVersion = 1` (`:28,37`) |
| Defaults | `Template` table (`:53-86`) via Reconcile | same (`:36-41`) |
| Migrations / version | **None.** Comment: rename/remove means bump store index `GreatWallSim_v1` = wipe (`:6-8`; `DataService.luau:20-22`) | `schemaVersion` + `CurrentVersion` exist but **nothing reads or migrates them** (grep: only `ProfileTemplate.luau`). Comment promises a migration (`:7-8`). `Pet` type exported, unused (`:16-25`). |
| Session lock / timing / shutdown | ProfileStore defaults (300 s, steal 40 s, BindToClose in package). Extra `LeaderboardService` `game:BindToClose` for OrderedDataStore (`LeaderboardService.luau:271`) | ProfileStore defaults only |
| Studio | mock store (`DataService.luau:27`) | same |
| Receipts | `StoreService.luau` (670): one `ProcessReceipt` (`:469`), pure `Domain/Receipts.luau` (66, cap 100 ids in profile `PurchaseIds`), grant+record in one yield-free block, then `saveAndConfirm` forces `profile:Save()` until the id is in `LastSavedData` (`:254-289`); unknown/not-ready player returns NOT_PROCESSED (`:318-330`). Good pattern. | **No purchases yet** (no `ProcessReceipt`, no MarketplaceService in `src/`). Telemetry design `knowledge/design/telemetry.md` is a plan only. |
| Atomic writes | `GrantService` (284): "every check is inside the DataService update callback" (`:24-26`); one grant path for all rewards; `Domain/CodeRules`, `LimitedStock` pure logic | `server/Economy/Ledger.luau` (71): commit/sell sequences through a `get/update` adapter, bricks before gold so a throw cannot duplicate (`:35-60`); spec `economy_ledger.spec.luau` |
| Numeric safety | `shared/Economy/Amount.luau` (29): `whole()` clamps NaN/inf/negative/fraction | same file, comment differs (text only) |
| Tests | `amount`, `receipts`, `ratelimit` specs | `economy_ledger`, `ratelimit` specs; no `amount` spec by name |
| Problems | whole-table re-replication on `update` (e.g. `Upgrades` copy in `StoreService.luau:239-243`); `PurchaseIds` (100 strings) in every join snapshot | `Backpack` write path is solid, but `schemaVersion` is dead data |

### 2.3 Remotes

| Aspect | GWS | DS |
| --- | --- | --- |
| Transport | Networker, one channel per service (`Net/Networkers.luau`) | same file |
| Client-callable services | 16 services, 29 methods (`grep clientAccess`, e.g. `StoreService:84 {requestBuy, requestSkip}`, `CodesService:46 {redeemCode}`) | 3 services, 7 methods (`WeaponService:87`, `BrickWorldService:221`, `DevStageService:42`) |
| Validation style | Params typed `unknown`; per-service checks: `PlayerSession:isReady` + `hasProfile` + cooldown + type check (`CodesService.luau:79-98`, `StatsService.luau:190-205`) | Same idiom, deeper: `readShotId/readGearId/readPosition/readDirection` readers, per-gate flood limits, reply-less rejects (`WeaponService.luau:609-652`) |
| Rate limit | `Lib/RateLimit.luau` 151 lines: `cooldown` + `allowance` (credit bucket, burst); referenced in 17 files | 98 lines, `cooldown` only; used in 7 files |
| NaN / inf | 88 self-compare checks (`x ~= x`), 221 `isFinite/math.huge` hits (COUNT) | 145 and 514 (COUNT, `Content/` excluded for the first) |
| Audit tool | **none** | `tools/remote_audit.py` (262): static check per handler for ready, rate limit, type, NaN, integer, reject; baseline 0; `tools/replication_check.py` (415): shared bytes budget |
| Problem | No shared validator module: each service re-writes "is number and not NaN" (`NetController.luau:35-38`, `Amount.whole`, `StatCurves.walkChoice`). Fixed per-service convention, not enforced by a tool in GWS. | Same duplication (`read*` helpers live inside `WeaponService`); DevStage methods are Studio-gated, good. |

### 2.4 Player state and replication

| Aspect | GWS | DS |
| --- | --- | --- |
| Truth | Server: profile via DataService; world state in services (DamService, Backpack session-only) | Server: profile + brick world (`BrickWorldService` 1,368, `server/Bricks` 82 files, 38,902 lines) |
| Replication | (a) DataService profile mirror (client `DataServicePkg.client:get/getChangedSignal`, 12 files); (b) Networker snapshots with a `seq` counter, stale snapshots dropped (`NetController.luau:5-8, 55-60`); (c) `SetAttribute` 91 sites (COUNT) | (a) same DataService mirror (3 files); (b) Networker push of brick deltas (`BrickRenderController`, `PickupController`); (c) `SetAttribute` 141 sites |
| Client cache | Charm atoms in `client/State/GameState.luau` (122), `MetaState` (98), `InputState` (25); "display cache, never source of truth" (`GameState.luau:2-3`); push shape check `validDam` (`NetController.luau:30-52`) | 1 atom file (`UI/EconomyState.luau`, 18 lines) |
| Charm sync | not used (no `charm-sync`) | not used |
| Problem | Ordering: Charm listeners fire in no fixed order, worked around by writing dependent atoms first. Snapshots carry whole tables. | Client state is thin; no common state layer. |

### 2.5 UI state and UI code

| Aspect | GWS | DS |
| --- | --- | --- |
| Library | Plain Instances, no React/Roact/Fusion/Vide (COUNT 0) | same |
| Structure | `client/Ui/` 15 files (5,366) + `Hud/` 8 (2,120) + `Panels/` 10 (5,417) + `Layouts/` **58 files, 27,650 lines GENERATED** from Figma by `tools/ui/figma_layout.py` ("do not edit", `Layouts/HUDPCQuarry.luau:2`) + `Onboarding/` 7 + `World/` 10 | `client/UI/` 16 files (5,140), hand-written (HudChip, Roller, BrickFly, Token*, SellFx) |
| Screen manager | `Ui/Screen.luau` (627): `build(layout, parent)`, `relayout`, `clone`, `setImage`, binds to generated frames; `PanelController.luau` (203): one panel stack, gamepad B closes, selection group, wires GridNav; `SafeArea.luau` (125); `Motion.luau` (531); `StudKit.luau` (870) button/bar/chip kit; `PurchaseLock.luau` (102) | none: `HudController` (363) builds chips directly; no panel stack |
| Variants | PC and Phone copies of every layout (HUDPCQuarry 2130 lines vs HUDPhoneQuarry 1720; HUDPCQuarry vs HUDPCDam same size) | n/a |
| Problems | Layout files are very large generated data (27.6 k lines in git); coupling: `Screen.luau:requires Shared.Config.UiAssets/UiSkins` (game assets); `UiFx.luau:747` requires `Feel.FeelTextures`. `Sound.luau:746` reaches into DataService. | HUD code is game-bound; `HudLayout.luau` exists twice with different content (GWS `Lib/` 515 lines, DS `UI/` 75). |

### 2.6 Animation playing

| Aspect | GWS | DS |
| --- | --- | --- |
| Manager | `client/Animation/` 13 files, 4,197 lines. `ClipPlayer.luau` (286): one player per Animator, lazy `LoadAnimation`, priority/looped from `AnimClips`, marker signals connected before `Play`, fade, hold-last-pose, skips clips with empty id (`:1-16`, `LoadAnimation` at `:109`). `AnimController` (822) drives loops from atoms; `AnimState` (652) loop table; `AnimClips` (337) data; `AnimationIds` (92) | **none** (`LoadAnimation`: 0 hits) |
| Problems | `ClipPlayer` requires `AnimClips`, `AnimationIds`, `AnimState` (`:18-21`): game-bound data. `Controllers/AnimController.luau` is a 12-line stub that forwards to `Animation/AnimController` (needed because `ControllerOrder` resolves names in `Controllers/`). | |

### 2.7 Cleanup (Janitor)

| Aspect | GWS | DS |
| --- | --- | --- |
| Janitor sites | 84 files, 108 `Janitor.new()`, 568 `:Add` | 41 files, 64 `Janitor.new()`, 251 `:Add` |
| Connect vs Janitor | 375 `:Connect(` lines vs 568 `:Add` (COUNT, `Content/` excluded) | 129 vs 251 |
| Player leave | `PlayerRemoving` 31 sites; `DataService:addPlayerRemovingCallback` | 14 sites; `DataService.server:addPlayerRemovingCallback` used at `PickupService.luau:888` |
| Character respawn | `CharacterAdded` 15 sites (e.g. `AnimController.luau:804` adds the connection to a janitor) | 9 sites |
| Pattern | Module-level `local janitor = Janitor.new()` and `janitor:Add(conn, "Disconnect")` in `start()`; per-player state in tables keyed by `Player`, reset in `PlayerRemoving` (`CodesService.luau:66-70`). No per-player Janitor registry owned by `PlayerSession`. | same |
| Problem | `task.spawn/delay/defer` 233 sites in GWS (thread lifetime tied to player left to each author); DS 40. `PlayerSession.luau:41-59` leaves a thread suspended on failed loads (1.3 bug). | |

### 2.8 Config and content as data

| Aspect | GWS | DS |
| --- | --- | --- |
| Config | Luau tables in `src/shared/Config/` (26 files, 5,618 lines: Heroes, Upgrades, Quests, Titles, DamLadder, UiAssets 616, UiPreload 1,024...) and `server/Content/` (18 files, 3,212). Hand-edited in code. Only `content/vfx` outside `src`. | JSON in `content/` (16,360 files: economy, gear, bricks, stages, ui, vfx, world) compiled by `tools/content/contentc.py` (505) and `tools/bricks/brickc.py` into **GENERATED** Luau: `shared/Content/Economy.luau`, `BrickCatalog.luau` (2,159), `Stages/` (15 files, 30,876), `Structures/` (hundreds of files). Gate stages `bricks` + `content` verify generated files are fresh (`verify.ps1` header). |
| Store ids | `tools/store/store-ids.json` + `upload_store.py` -> `shared/Config/StoreIds.luau` | n/a |
| Problem | Numbers sit in Luau modules next to logic in places (e.g. `Config/Upgrades`, `StatCurves`); no schema check on config. | `contentc` covers economy+gear only; stages/structures use a separate `brickc`. Two compilers, two validators. |

### 2.9 Tests, lint, format

| Aspect | GWS | DS |
| --- | --- | --- |
| Offline Luau | Luau CLI pure specs: `tools/tests/luau/*.spec.luau` (93 files, `_harness.luau` home-made `T.case/T.expect`), run by `tools/tests/run-pure-cases.ps1` (convention: no Roblox services) | same runner; 239 spec files; parallel pool |
| Jest / Lune / TestEZ | none (COUNT 0) | none |
| Python tests | `tools/tests/test_*.py` (kit-style, 64 entries in `tools/tests`) | 89 entries |
| Gate | `tools/verify.ps1` (400 lines): format, lint, indexes, kit (`verify.py --fast`), kblint, typecheck, suites, python | `tools/verify.ps1` (773): + remotes audit, replication check, luau_game_mirror, bricks validate, content check, known-red-suites |
| Lint / format / types | selene `std = "newgame"`, `stylua.toml` (col 120, tabs, CRLF), luau-lsp analyze; baselines `lint-baseline.txt`=0, `typecheck-baseline.txt`=0 (ratchet). Rokit pins in `rokit.toml:6-12` (rojo 7.7.0, wally 0.3.2, stylua 2.5.2, selene 0.30.1, luau-lsp 1.69.0) | same pins; + `remote-audit-baseline.txt`=0 |
| Strictness | 374/375 files `--!strict` (exception: `Ui/World/GymTierLabels.luau`); 363 `:: any` | 2402/2402 `--!strict`; 341 `:: any` |
| Missing tests (both) | `DataService` wrapper, `PlayerSession`, `Networkers.register`, `init.*.luau` bootstrap, no ProfileStore mock test | |
| NOT RUN | I did not run either gate; results above are from reading scripts and baselines only. | |

### 2.10 Quality problems, shown

| # | Problem | Where | Impact |
| --- | --- | --- | --- |
| P1 | Suspended thread + Player ref leak when profile load fails | DataServiceServer.luau:298-300,454-461; PlayerSession.luau:43 | Minor leak; unreachable "load failed" branch |
| P2 | No migration runner; store-index bump wipes saves (GWS) or `schemaVersion` unused (DS) | GWS ProfileTemplate.luau:6-8; DS ProfileTemplate.luau:28,37 | Any breaking schema change loses data |
| P3 | `init` failure only `warn`s, game keeps running | init.server.luau:50-56 (both) | Silent no-save server |
| P4 | Infra copied across games and already forked (RateLimit 151 vs 98; HUD layout; bootstrap dev blocks) | section 2.1 | Fix twice |
| P5 | `wally.lock` root `firew/roblox-blocks`, registry `test` | wally.lock:3,11 (both) | Lock does not match the project; reproducibility risk |
| P6 | Networker passes raw varargs; validation is convention only; GWS has no remote audit | NetworkerServer.luau:87; GWS `tools/` has no `remote_audit.py` | A new handler can ship unguarded |
| P7 | Full-table replication on `update` | DataServiceServer.luau:537; GWS StoreService.luau:239-243 | Bandwidth grows with table size |
| P8 | Signal and Charm not strict | package headers | Types weaker at the two most-used boundaries |
| P9 | DS `schemaVersion`/`Pet` type dead | DS ProfileTemplate.luau:16-37 | Misleading contract |
| P10 | Janitor pulls Promise chain | wally.lock:23-31 | Extra 2 packages for no use |

## 3. Part 3: DS `knowledge/design/game-framework.md` (99 lines, PROPOSAL, 2026-10-08)

"Candidates from this game" table (`:34-45`), each path checked:

| Candidate | Path in the doc | Exists now? | Size now |
| --- | --- | --- | --- |
| Bootstrap | `src/server/init.server.luau`, `src/client/init.client.luau`, `Bootstrap/LoadOrder.luau` | yes | 111 / 89 / 31 lines (GWS copies: 91 / 75 / 40) |
| Player session + save wrapper | `src/server/Services/PlayerSession.luau`, `DataService.luau` | yes | 76 / 41 lines (identical in GWS) |
| Transport + validation | `src/server/Net/Networkers.luau`, `rules/security.md` | yes | 71 lines (identical in GWS) / 38 lines |
| Economy ledger | `src/shared/Economy/Ledger.luau` | **moved**: now `src/server/Economy/Ledger.luau` | 71 lines (DS only) |
| Telemetry service | `design/telemetry.md` (planned) | doc exists, no code in DS | 121 lines; GWS has `server/Lib/Analytics.luau` (84) |
| Content-as-data compiler | `tools/` content compile, `content/` | yes | `tools/content/contentc.py` 505 lines; `tools/bricks/` 25 files; `content/` 16,360 files |
| Verify gate + context packet | `tools/verify.ps1`, `tools/context_packet.py` | yes | 773 / 371 lines |
| Blender UI render studio | `tools/art/blender/icon_studio.py` | yes | 715 lines |
| Destruction core | `src/shared/Bricks/`, brick pipeline | yes | 29 files, 10,049 lines shared (+ `server/Bricks` 82 files 38,902; `client/Bricks` 9 files 4,682) |
| AI studio layer | `AGENTS.md`, `rules/`, `.agents/skills/`, `.claude/agents/`, mods | yes | AGENTS.md 155; `rules/` 16 files 732 lines; `.agents/skills` 54 files 5,816; `.claude/agents` 15 files; `tools/claude-mods` 96 files |

Other doc claims: "extract when the second game starts" (`:47-49`); open point "two repos: code vs AI studio" (`:98-99`). The second game (GWS) now exists and the bootstrap/session/networkers files are byte-identical or near-identical in it, which is the doc's extraction trigger.

## 4. Part 4: extraction candidates (ranked)

Ranking = genre-agnostic, already identical or near-identical in both games, small, pure, covered by a spec.

| Rank | Module (source) | Lines | Why extract | Work needed |
| --- | --- | --- | --- | --- |
| 1 | Boot loop: `init.server.luau` + `init.client.luau` + `LoadOrder`/`ControllerOrder` | 91+75 | Same logic in both; dev block is the only diff | Make order list a param; fail loudly on `DataService` init failure (P3); add a spec |
| 2 | `PlayerSession` (ready gate) | 76 | Byte-identical in both; every service uses it | Fix hang on load failure (P1); owner of per-player Janitor |
| 3 | `Networkers.register` (`clientAccess` registry) | 71 | Byte-identical; opt-in surface by construction | Decide with transport research; add arg-validation helper or wrap |
| 4 | `RateLimit` (`cooldown` + `allowance`) | 151 | Pure, no requires; GWS version is a superset; both have a spec | Take GWS file; merge specs |
| 5 | `Amount.whole/add` | 29 | Pure; guards NaN/inf/negative | Rename comment generic |
| 6 | `Receipts` + `StoreService` receipt core (`saveAndConfirm`, record-then-grant) | 66 + receipt section of | Correct ProcessReceipt pattern that DS will need | Strip GWS grant kinds; keep pure parts |
| 7 | Atomic write pattern (`GrantService` principle, DS `Ledger` adapter) | 71 / 284 | Shows check-and-write inside `update`; DS `Ledger` takes a `get/update` adapter, testable offline | Extract adapter + doc, not the game grants |
| 8 | `DataService` wrapper (store index, mock flag, template) | 41 | Identical shape | Add migration runner + schema version; own the `waitForData` fix; consider forking the package |
| 9 | `Analytics` wrapper | 84 | pcall-wrapped AnalyticsService calls | GWS only; needs currency list as data |
| 10 | `ClipPlayer` (Animator loops, markers, fades) | 286 | Real manager, Janitor-clean | Decouple from `AnimClips/AnimationIds/AnimState` (`:18-21`) |
| 11 | `PanelController` (panel stack, gamepad B, selection) + `GridNav` + `DeviceResolver` + `TapGesture` + `SafeArea` | 203+37+107+94+125 | Genre-agnostic UI infrastructure; small deps (`PanelController` needs `InputController`, `InputState`) | Remove `InputController` coupling (`PanelController.luau`) |
| 12 | `remote_audit.py` + `replication_check.py` + `luau_game_mirror.py` (DS tools) | 262+415 | Gate checks GWS lacks; protect remote surface | Port to the kit gate |
| 13 | Lint/format/typecheck ratchet + pure-spec runner (`run-pure-cases.ps1`) | 400-773 | Same config in both games | Already kit-like |

### Do NOT extract

| Module | Reason |
| --- | --- |
| `server/Bricks/*`, `shared/Bricks/*`, `client/Bricks`, `World/*`, `Content/Stages|Structures` (DS) | Destruction physics (38,902+10,049 lines); game-specific; generated content |
| `Feel/*`, `Feel/Beats/*`, `Audio/*`, `Cutscenes/*`, `Rides/*` (GWS) | Game-bound VFX/SFX/ride logic (e.g. `FeelVfxDam` 1,391 lines) |
| `Ui/Layouts/*` (58 generated, 27,650 lines), `Screen.luau`, `StudKit.luau`, `UiAssets/UiSkins/UiPreload` | Output of one Figma file and one art kit; `Screen.luau` couples to game assets |
| `Services/Dam|Gym|Wheel|Limited|Ride|Quarry|MechClimb*`, `Domain/DamRound|WheelRoll|HeroRideCheck` (GWS) | Game rules |
| `Weapons/*`, `Economy/Tokens|TokenSweep|Landing*` (DS) | Game rules |
| `ProfileTemplate` bodies, `Config/*`, `content/*` data | Per-game data |
| Charm `State/` atoms (`GameState`, `MetaState`) | Hold game snapshots; the pattern (display cache + `seq` drop, `NetController.luau:5-8`) is reusable, the files are not |
| DataService package as-is | Works, but no migrations, hang bug (P1), full-table replication; decide keep/replace/fork in the package decision, not here |
| `Dev/*` tools (DS PhysicsLab, FrameLedger, MemoryLedger) | Useful performance tooling, but tied to brick world |

## 5. Not covered or not verified

| Item | State |
| --- | --- |
| Gates (`verify.ps1`/`verify.py`), Luau specs, Studio | NOT RUN (read only) |
| Per-handler validation completeness in all 30 GWS handlers | Sampled 4 (CodesService, StatsService, CoinShopService, StoreService receipt) + DS WeaponService; not audited line by line |
| Janitor leak audit | Counts only; no proof of a leak beyond P1 |
| Exact test counts per suite | File counts only |
| Content identical files across games | Filename match only for 14 pairs (script); 2 identical (`Networkers.luau`, `PlayerSession.luau`) |
