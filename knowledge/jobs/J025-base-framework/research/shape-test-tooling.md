---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# J025 research: framework shape, distribution, testing, tooling, live config

All "checked" dates are 2026-10-24 unless stated. Labels: **DOC** = documented fact (Roblox docs or the repo's own page), **KIT** = earlier kit note, not re-checked by me, **COMM** = community claim, **INF** = my inference. "nv" = not verified. Release dates come from GitHub release pages/API as fetched on 2026-10-24; the API returned 403 after the first batch, so some rows have only repo-page facts (no commit date).

## 0. Answers first

| Question | Answer (PROPOSAL) | Why in one line |
| --- | --- | --- |
| Template repo, Wally packages or both? | **Both, split by life cycle.** Wally packages (our own scope) for single-purpose blocks that change slowly and are shared; a GitHub template repo for the skeleton that each game owns and edits | A block is code you want fixed once for all games; a skeleton is code each game must change. D-112 (adopt piece by piece) needs the first; "bugless on day one" needs the second |
| Bootstrap that needs no central list? | **One entry Script per side + our own ~100-line loader that scans a `Systems` folder, reads each module's declared `After` list, and runs `init` for all, then `start` for all** | Roblox's own docs recommend one entry script plus modules with `start()` (DOC, section 1); the folder scan removes the list; declared dependencies replace hand-ordered lists |
| Test stack for real in-engine checks of saves and remotes? | **Three layers:** Lune (pure logic, every change) + Jest through Open Cloud Luau Execution (server modules in a real engine, no players) + Studio `StudioTestService` multi-client tests (remotes, join/leave, saves with real peers). Luau Execution alone cannot prove remotes | Luau Execution has no physics, no auto-running scripts, no persistence of changes (DOC, section 3) and no client |

## 1. Bootstrap and framework shape

Roblox's own script-location page: one `Script` with `RunContext = Client` in ReplicatedStorage, one with `RunContext = Server` in ServerScriptService, ModuleScripts for the rest, a `start()` per module "so that all modules can load before you begin executing their code" (`knowledge/external/roblox-creator-docs/scripting/locations.md:36-51`, mirror rev `7400643`, 2026-10-20). `RunContext` values Legacy/Server/Client/Plugin; only `Script` supports non-Legacy (`_api-reference/enums/RunContext.yaml:11-20`). DOC.

| Rank | Option | Owner / status (checked) | Licence | Strict / types | Fit and weakest part |
| --- | --- | --- | --- | --- | --- |
| **1 (pick)** | **Own loader**: entry Script, folder scan, `{Name, After, init, start, stop}` per module, phases init-all then start-all, per-module `pcall` plus yield timeout, report in one log | ours | ours | `--!strict`, one `System` type | Removes the central list (agent adds a file, touches nothing else). Offline-testable under Lune (fake folder). Weakest: we own the bugs of ~100 lines (cycle detection, error isolation); must be tested hard. Matches `rules/packages.md` ("game's own small modules are often enough", line 20) and `anti-overengineering` |
| 2 | Prvd 'M Wrong | repo "Intuitive and extendable Luau provider framework", 637 commits, 36 stars, v0.2 is MPL-2.0 (older MIT/Apache); no release list; last commit date nv (github.com/prvdmwrong/prvdmwrong, 2026-10-24) | MPL-2.0 | "type-safe APIs", strict mode not stated | Declares `dependencies` per provider, `constructor` then `start` in own thread. Page lists `pesde.toml` and `rokit.toml`, no Wally manifest. Weakest: tiny community, not on Wally, adds a contract every agent must learn (`rules/packages.md:20`) |
| 3 | Knit (Sleitnick) | **archived 2024-07-31**, "will no longer receive updates" (github.com/Sleitnick/Knit) | MIT | n/a | Do not adopt (fails maintained test, `rules/packages.md:7`) |
| 4 | Flamework | "extensible game framework. It requires typescript" (github.com/rbxts-flamework/core, 160 stars, MIT; commit dates nv) | MIT | TypeScript (roblox-ts) only | Our stack is Luau `--!strict` (`AGENTS.md` §2); a second language is out of scope |
| 5 | Lumin | **could not be found** by two searches; nv | nv | nv | Ask the owner for a link if it matters |
| 6 | Community Knit successors: Vanguard 0.1.15, OwlKnit 1.1.2, Kernel 1.0.1 | DevForum threads (COMM; posts found 2026, first-post dates not read) | nv | nv | Version numbers are young; none shown with studio adoption. Not candidates |

ECS (option, not default; `A-11`: ECS only for large regular workloads, benchmarked on a real slice):

| Package | Status (checked) | Licence | Note |
| --- | --- | --- | --- |
| Jecs (Ukendio) | v0.11.0, 2026-03-10 (API); 475 stars, 862 commits (github.com/Ukendio/jecs) | MIT | "fast, portable ECS for Luau". Self-reported benchmarks only; no named production game found (COMM search, nv) |
| Matter (matter-ecs) | last push 2024-12-31 (API), not archived, 116 stars | MIT | Older, has loop/debugger features; one DevForum poster says Jecs is faster but drops some features (COMM, single anecdote). 22 months since last push fails the 12-month rule (`rules/packages.md:7`) by commit date |

INF: ECS is a block a game opts into if a measured slice needs it; the base framework should not depend on it. Parallel Luau/Actors: units of isolation, scripts under one Actor run serially, parallel work needs several Actors and `task.desynchronize()` (`scripting/multithreading.md:27-61`, DOC); no framework should wrap it by default (`A-17`).

**Where top studios/projects stand (honest answer).** I found **no public engineering write-up** of a large Roblox studio's framework. What exists:
- Roblox's own reference CI sample (Selene + StyLua + Rojo build + Luau Execution tests) is archived since 2024-09-25 and says it "has not been battle tested" (github.com/Roblox/place-ci-cd-demo). DOC.
- Wally's repo is under `UpliftGames` (Adopt Me's studio); that shows who built the package manager, not their game's layout. DOC (repo owner) / INF.
- DevForum threads (COMM, no consensus): plain ModuleScripts without a framework are often called enough; Knit "no longer recommended" by its author (search summary of DevForum 3169926, 2818025, 2823121; I did not open the posts).
- Open-source starters (COMM): `LocalPulse/jecs-template` (Wally + Rokit + Rojo files, empty `src/`), `iceeburr/roblox-template` (Rojo + Tarmac + GitHub Actions), `rproj` (Rust scaffolder: Rojo, Wally, Selene, StyLua, luau-lsp, CI; Jest or TestEZ; alpha, Windows). None verified for licence or activity.
- The owner's own record: five-package stack (DataService, signal, charm, janitor, Networker) in every game since 2026-05-23 (`research/old-framework.md`, KIT).

## 2. Distribution

| Rank | Option | Status (checked) | Licence | Cost / risk |
| --- | --- | --- | --- | --- |
| **1 (pick)** | **Wally, our own scope, plus a GitHub template repo for the skeleton** | Wally 0.3.2 released 2023-06-05; repo pushed 2026-10-12, not archived, 88 open issues (API). KIT notes 0.4 is alpha (nv by me) | MPL-2.0 (API) | Already in every game since 2026-05. Weakest: last *release* is 3.4 years old (commits are recent, so the 12-month rule passes by commit); the public index has no private packages |
| 2 | Private Wally registry | Wally docs 0.3.x: multiple registries "can be used to have split public/private registries" (search summary of Wally docs, nv on setup) | MPL-2.0 (server in same repo) | We run a server and keys. **Needed only if the framework must stay proprietary** (`Enjukku/roblox-game-framework` is described as "Proprietary", `old-framework.md` C2): anything published to the public index is public |
| 3 | pesde | v0.7.4, 2026-09-09; MIT; 130 stars, 679 commits; own registry; can also use Wally and git sources; targets Roblox, Lune, Luau (github.com/pesde-pkg/pesde; docs.rs summary) | MIT | Git sources solve the private case without a server. Weakest: 0.x ("15 unstable releases (3 breaking)", lib.rs, COMM), a second package manager beside Wally, I could not read its Roblox guide (404) so Wally-dependency handling is nv |
| 4 | Git submodule / subtree + Rojo `$path` | no tool | n/a | Zero tooling and private, but no versions or lock file; "update deliberately, pin versions" (`rules/packages.md:17`) becomes manual. Fallback only |
| 5 | Studio packages / Creator Store | Package Overrides is beta (Studio 743+, 2026-10-15, `whats-new.md:55`) | n/a | Not file-based; conflicts with `files` source mode (`AGENTS.md` §3). Skip |

**Which parts go where (INF):**

| In Wally packages (versioned, no game rules) | In the template repo (each game edits) |
| --- | --- |
| Session/data (lock, states, migrations), Transport (validated remotes), Config wrapper, Lifecycle loader, small utilities (janitor-class cleanup, signal) | `default.project.json`, `rokit.toml`, `wally.toml` + lock, `selene.toml`, `stylua.toml`, `.luaurc`, `tools/verify.py` gate, CI file, folder layout (`Systems/`, `Shared/`, `Content/`), the two entry Scripts, game-profile stub, one sample system + test, test-place config |

Reason: a package block holds what must be identical in every game (so a bug fix ships once, per D-112); skeleton files differ per game and rot if versioned as a package. A game adopts one block by adding one `wally.toml` line and a one-file adapter (`rules/packages.md:12`).

## 3. Testing

Facts that decide the stack (DOC unless stated):
- **Luau Execution limits** (create.roblox.com/docs/cloud/reference/features/luau-execution.md, fetched 2026-10-24): 5 min per task, 4 MB script, 10 incomplete tasks per place (429 beyond), create 5/min per key owner, logs 450 KB, results kept 24 h. **Not supported: physics simulation; Server and Local scripts do not run automatically; DataModel changes are local to the task.** Scopes `universe.place.luau-execution-session:write` / `:read`.
- `RunService` context table lists "Luau Execution" as its own row (`_api-reference/classes/RunService.yaml:128-135`); no client exists in it (INF).
- **Whether `DataStoreService` works inside Luau Execution: nv.** `SecurityCapability.yaml:89` shows a DataStore capability but not whether the session has it. Needs a 10-minute probe.
- `StudioTestService:ExecuteMultiplayerTestAsync`: plugin-only, up to 8 simulated clients, one session at a time per Studio instance; server/client contexts, `EndTest`, `GetTestArgs` (`_api-reference/classes/StudioTestService.yaml:20-87`).
- Teleports do not work in a Studio test (`factcheck-engine.md:153`, KIT).

| Rank | Tool | Owner / latest (checked) | Licence | Strict support | Cost in our gate |
| --- | --- | --- | --- | --- | --- |
| **1 (pick, pure logic)** | **Lune** | lune-org/lune **v0.11.1, 2026-10-21** (fixes an HTTPS certificate issue and a `@lune/roblox` regression; v0.11.0 2026-10-11 updates reflection DB to 0.741). KIT says 0.11.0: newer now | nv | Runs Luau; type checking is by luau-lsp, not Lune | Seconds, one binary via Rokit. Limited Roblox API: DataModel-free logic only |
| **1 (pick, server in real engine)** | **Jest** (`roblox/jest` + `roblox/jest-globals`) | Roblox/jest-roblox: README pins **3.20.0**, no GitHub releases listed, not archived, 575 commits, 50 stars, 7 open issues; KIT says 3.20.1 (2026-08-30), nv by me | MIT | Types for strict: nv (docs page silent) | Needs API key, a published test place version, network and up to 5 min per task. Merge lane, not per-edit |
| 2 | `jsdotlua/jest-lua` | v3.10.0, 2024-12-23; MIT; 57 stars; 470 commits | MIT | nv | Older community fork; KIT says it is separate. Use only if `roblox/jest` fails |
| 3 | TestEZ | **archived 2024-09-14** (github.com/Roblox/testez); Apache-2.0 | Apache-2.0 | n/a | Keep old suites only |
| 4 | run-in-roblox | 0.3.0, 2020-07-20 (KIT, `factcheck-engine.md:118`); repo page not readable (403) | nv | n/a | Legacy; needs installed Studio. Skip |
| 5 | Community Jest runners (`jest-roblox-cli`, `rproj`) | COMM; rproj uses Open Cloud scopes `luau-execution-session:write` plus Memory Store | nv | nv | Convenience wrappers; not adopt-tested |
| engine proof | **Studio MCP + StudioTestService** | Built into Studio (`studio/mcp.md`); multi-client DOC above | Roblox | n/a | Studio open, one driver; manual or nightly lane |

**Answer to "real in-engine checks for saves and remotes":**

| Check | Best layer | Reason / gap |
| --- | --- | --- |
| Save migrations, reward math, session state machine | Lune | Pure; fastest |
| Save module against the real DataStore API | Luau Execution + Jest **only if** the probe shows DataStore works there; else Studio play with a **separate test universe** (`code-review/references/testing.md:18`) | Gap: nv |
| Remote validation rules (types, NaN, rate, ownership) | Lune against the validator functions; then Studio multi-client | The remote itself needs a client |
| Remote round trip, replication, join/leave, rejoin before save ends | `ExecuteMultiplayerTestAsync` (2-8 clients) driven from a plugin, result via `EndTest` string | Plugin-only; Studio must be open; no CI headless path found (INF) |
| Physics, streaming, rendering | Studio scenarios; phone for device claims | `testing` skill T-09, T-11 |

Weakest part of the pick: **there is no headless CI route for multi-client tests**; the engine lane for remotes depends on an open Studio (one driver per Studio, `AGENTS.md` §3). Reduce the risk by keeping remote handlers thin and testing their validators in Lune.

## 4. Tooling

| Rank | Tool | Owner / latest (checked) | Licence | Strict mode | Cost in `python tools/verify.py` |
| --- | --- | --- | --- | --- | --- |
| **Pick** | **Rokit** (installs the rest from `rokit.toml`) | rojo-rbx/rokit v1.2.0, **2025-09-30** (13 months, commits nv) | nv | n/a | One-time install. Release is over 12 months old: check commit date at adoption |
| **Pick** | **Rojo** | rojo-rbx/rojo **v7.7.1, 2026-10-02** (Windows `\\?\` path fixes; plugin fallback when api.github.com is blocked) | nv (KIT) | n/a | `rojo build` seconds. Script Sync is not a replacement: Roblox says Rojo is better when the file system is the source of truth (`scripting/sync.md:23`) |
| **Pick** | **Wally** | see section 2 | MPL-2.0 | Types need `wally-package-types` | `wally install` network once per lock change |
| **Pick** | **wally-package-types** | JohnnyMorganz v1.7.0, 2026-09-24 | nv | Makes package types visible to the strict checker | ~1 s after install. Required for `--!strict` with Wally packages (INF) |
| **Pick** | **luau-lsp** `analyze` | JohnnyMorganz/luau-lsp **1.70.1, 2026-09-27** | nv | Yes, `strictDatamodelTypes`; new type solver must be on for strict (`whats-new.md:69`) | Seconds on a mid-size repo (INF); heaviest static step |
| **Pick** | **StyLua** | JohnnyMorganz **v2.6.0, 2026-10-10** | nv | n/a | `--check` under a second |
| **Pick** | **Selene** | Kampfkarren **0.32.0, 2026-10-01** | nv | Lints; does not replace luau-lsp | ~1 s. Overlaps luau-lsp; keep for style/unused rules only (INF) |
| Optional | **Darklua** | seaofvoices **v0.19.0, 2026-06-10** | nv | n/a | Only for bundling/transforming (e.g. a pure-Luau package for Lune); skip unless a package needs it |
| Optional | **Lune** | section 3 | | | |
| Not now | **pesde** | section 2 | MIT | | Second manager |

Gate sketch (INF): format check, selene, `luau-lsp analyze`, Lune tests, `rojo build` ≈ one minute (KIT estimate `factcheck-engine.md:25`); Jest/Luau Execution and Studio runs stay outside the per-edit gate. Record the Studio build with every engine run (`testing.md:37`).

## 5. Live config

| Fact | Source |
| --- | --- |
| `ConfigService` is **server only**; `GetConfigAsync()` (no player, no experiments), `GetConfigForPlayerAsync(player)` (applies experiments), `ConfigSnapshot:Refresh()`, `SetTestingValue(key, value)` / `ClearTestingValue(key)` (override for the current server only) | `_api-reference/classes/ConfigService.yaml:11-14, 52-137` |
| Both getters **yield** and **throw if config never loaded** and no earlier config exists | same file, lines 63-64, 87-88 |
| Types string, number, boolean, JSON; ≤ 1,000 active configs; string/JSON ≤ 100,000 chars; numbers exact to 2^53 | `production/configs.md:26, 70-75` |
| New configs are **staged** (visible to you in Studio play only) until **Publish now** (about 15 s to 1 min) or **Publish over 15 min**; clients may take minutes | `production/configs.md:79-83` |
| Conditional values by country, language, new vs returning, source, payer status, engagement, etc.; first matching global rule wins | `production/configs.md:88-111` |
| Configs "do nothing unless you use them within your code" | `production/configs.md:60` |

PROPOSAL for the block (INF): a thin typed wrapper in the server package: every key declared in a data file with a default and a type; read through the snapshot, fall back to the default on the first-load error; refresh by interval; a `Set(key, value)` test hook using `SetTestingValue`; nothing client-side except values our Transport pushes. Content tables that must never change live (saves, prices tied to receipts) stay out of configs. Risk: Experiments/targeting touch money and player grouping, so `platform-policy` and `analytics` review applies (`AGENTS.md` §2). Whether ConfigService works inside Luau Execution tests: nv; if not, tests use the default path.

## 6. Risks and unknowns for the owner

| # | Item | How to close |
| --- | --- | --- |
| 1 | Public vs private package index (proprietary framework?) | Owner decision; then probe private Wally registry or pesde git sources |
| 2 | Does DataStore (and ConfigService) work in a Luau Execution task? | 10-minute probe with a throwaway key (`engineering-craft` `references/probes.md`); decides the save-test lane |
| 3 | `roblox/jest` version, strict-type support, and per-task start-up time | Install on a scratch place and run one spec |
| 4 | No studio engineering write-ups found; the "what top studios use" line rests on archived Roblox samples and COMM threads | Accept; the choice stands on the adopt test, not on popularity |
| 5 | Rokit, Rojo, Selene, luau-lsp, StyLua, Darklua licences not read | Read before the `knowledge/reference/<package>.md` records |
| 6 | Wally 0.4 alpha status and Wally git/private details | Read the Wally releases page at adoption |
| 7 | Lumin not found | Owner link |

**Recommended next action:** the lead takes the three picks to G1 (own loader, Wally + template repo, Lune + Jest + Studio multi-client), and a researcher runs the two probes (items 2 and 3) before the architect writes the limits sheet.

## docs_read

Mirror: `scripting/locations.md`, `scripting/multithreading.md` (Actors), `scripting/sync.md`, `production/configs.md`, `_api-reference/classes/ConfigService.yaml`, `StudioTestService.yaml`, `RunService.yaml`, `enums/RunContext.yaml`, `enums/SecurityCapability.yaml` (grep), `cloud-services/http-service.md` (grep); `knowledge/reference/roblox/whats-new.md`; `knowledge/reference/architecture/strong-codebases-2026-10.md` (A-11, A-17, A-21); `roblox-operations-2026-10.md` and `engineering/paper/factcheck-engine.md` (grep); `rules/packages.md`; `.agents/skills/testing/SKILL.md`; `code-review/references/testing.md`. Web (2026-10-24): create.roblox.com Luau Execution reference; GitHub pages/APIs for rojo, rokit, luau-lsp, selene, StyLua, lune, wally, pesde, jest-roblox, jest-lua, darklua, wally-package-types, jecs, matter, Knit, testez, prvdmwrong, flamework, place-ci-cd-demo; roblox.github.io/jest-roblox. Not opened: `.agents/skills/engineering-craft/SKILL.md`, `rules/anti-overengineering.md` (cited only by line from the brief).
