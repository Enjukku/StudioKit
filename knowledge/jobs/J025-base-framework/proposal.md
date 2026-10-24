---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# J025 proposal: the base game framework (G1 packet)

Every choice in this file is a **PROPOSAL**. The owner decides. Nothing is built yet.
Evidence: `research/old-framework.md` (step 1), `research/games.md` (step 2), `research/data.md`, `research/net-signals-cleanup.md`, `research/state-ui-animation.md`, `research/shape-test-tooling.md` (step 3). All web facts were checked on 2026-10-24.

## 1. The goal question

Which framework shape gives every new game the strongest **foundation** (saves, remotes, state, UI, animation and cleanup correct on day one) with the least code to learn and keep?

## 2. Three options, ranked

| Rank | Option | What it means | Play value for us (builders) | Cost |
| --- | --- | --- | --- | --- |
| **1 (recommended)** | **Thin own layer on proven packages** | Keep the proven packages (ProfileStore, Janitor, Signal, Charm). Replace the weak ones (DataService wrapper, Networker). Write small own modules only where no good package exists (loader, save adapter, transport checks, screen manager, animation player, motion, config). | Fixes the 10 real problems found in the two games (`games.md` §2.10). Saves stay on the most proven lock code. About 1,400-1,900 lines of our own code, each module with tests. | Medium. One build job; then each old game moves over one block at a time. |
| 2 | Keep today's stack, add our modules only | DataService and Networker stay. We add loader, screens, animation player and tests around them. | Least change. | Keeps the known gaps: no save migrations (a schema change wipes saves in GWS), no remote validation or rate limit in the transport, a load-failure hang (`games.md` P1, P2, P6). |
| 3 | Write everything ourselves | Our own session lock, transport, state, UI library. | Full control. | Highest risk. A lock bug shows as lost or duplicated items in live games. Roblox calls its own lock sample "unproven" (`data.md` §2). About 3,000-5,000 lines more to test and keep. |

Rejected outright: Knit (archived 2024-07-31), Flamework (TypeScript only), ProfileService (unsupported), Roact (archived), TestEZ (archived), Lapis and Scribe as the save layer (`data.md` §5).

## 3. The layers (option 1)

"Use" = an existing package. "Own" = we write it. "Engine" = a Roblox feature, no package. Lines are estimates of our own code, without tests.

| # | Layer | Choice | Why | Weakest part |
| --- | --- | --- | --- | --- |
| L1 | **Start-up (loader)** | Own, ~100 lines | One entry script per side. The loader finds every system in a `Systems` folder, reads its `After` list, runs all `init`, then all `start`. A new system is one new file; no central list to edit. Roblox's docs recommend this shape (`scripting/locations.md:36-51`). It fixes P3: today a failed `init` only warns, and the server runs with no saves. | We own its bugs (cycle check, error isolation). It needs hard tests. |
| L2 | **Player data (saves)** | Use **ProfileStore 1.0.3** (pinned copy) + own **`Session`** adapter, ~400-600 lines | ProfileStore already runs under every game we have (DataService wraps it), so existing saves stay readable. It has the most field use of any lock library. Our adapter adds what it lacks: schema version and migrations, a fence for saves from a newer version, a "degraded" state, receipt and award ids, a Studio store prefix, offline tests on its mock store. It fixes P1, P2 and P9. | ProfileStore's last commit is 2025-07-31 (15 months). This breaks `rules/packages.md` item 2 as written. We keep and patch our own pinned copy. **Owner decision D-2.** |
| L3 | **Purchases** | Own, inside `Session` | Record the `PurchaseId` and grant in one update, wait for the save, then return `PurchaseGranted`. GWS already has a correct version (`StoreService.luau:254-289`); we extract it. | Each game still owns what a product grants. |
| L4 | **Remotes (transport)** | Use **Blink** (schema file → generated typed code) behind an own **`Net`** module, ~200-300 lines | One schema file defines every message for both sides; wrong types fail before game code runs. `Net` adds what no tool knows: rate limits (from GWS `RateLimit.luau`), ownership, range against server state, idempotency. It fixes P6 (today Networker passes raw arguments and validation is by habit). | Generator bugs happen (Blink fixed a NaN bypass on 2026-09-19), so `Net` checks stay. One main maintainer. A short probe must confirm it first (§6). Alternative: Zap (same model). |
| L5 | **State (server truth, client copy)** | Use **Charm + charm-sync**, behind an own `State` adapter, ~40 lines | GWS already uses Charm in 38 files. Server atoms are the only writers; clients get read-only copies by delta, not full tables. It fixes P7 (DataService sends the whole table on every change). | One maintainer. Moving from 0.10 to 0.11 has breaking changes: one separate change per game. |
| L6 | **Cleanup** | Use **Janitor** (keep) | Works in both games, typed, maintained (push 2026-07-28). | It pulls in Promise (P10). Cleanup order is not guaranteed: our rule says never depend on it. Alternative: Trove. |
| L7 | **Signals** | Use **sleitnick/signal** (keep) | Works, small, maintained. | Not `--!strict`; handlers fire newest first. |
| L8 | **Async** | Engine: `task` + `pcall`, no promise library | The engine already gives cancel (`task.cancel`). No game uses Promise today. | We write `all` / `first` by hand if two places ever need them. |
| L9 | **UI screens** | Own **`Screens`** manager, ~150-220 lines, on plain instances + the engine StyleSheet | No library does this. Every game needs it: layers (HUD, screen, modal, toast), a stack with back, gamepad focus, input routing through `InputContext`, a cleanup per open, late server answers dropped. GWS already has a panel stack (`PanelController.luau`); we extract and clean it. Plain instances match the kit's Figma → Roblox pipeline (GWS: 58 generated layouts). | No reactive UI library: list screens need a bit more code. **Owner decision D-4** (Vide is the alternative). |
| L10 | **Motion** | Own **`Motion`** helper on TweenService, ~80-120 lines | Plays motion rows from a data table, with a reduced-motion version (`ui-basics` U-13 already asks for this). | No springs in the engine; add ripple only if a game needs springs. |
| L11 | **Animation playback** | Own **`Anim`** module, ~150-200 lines | Load each clip once per Animator (`LoadAnimation` makes a new track every call: `Animator.yaml:208-213`), preload, play by id from a data table, markers by name, all connections cleaned. GWS already has `ClipPlayer.luau` (286 lines); we extract it without its game ties. No good public package exists. | Marker timing and replication need one Studio probe. |
| L12 | **Live config** | Own **`Config`** wrapper on ConfigService, ~60-80 lines | Every key with a type and a default in a data file; safe fallback when config is not loaded; test hook through `SetTestingValue`. | ConfigService is server only and its getters throw before first load: the wrapper must handle it. |
| L13 | **Small pure helpers** | Own, extracted | `RateLimit` (GWS, 151 lines, has a spec), `Amount` (NaN/inf-safe numbers, 29 lines), the atomic-write ledger pattern (DS `Ledger`). | None large. |
| L14 | **Tests** | Lune (pure logic, every change) + Roblox **Jest** through Open Cloud Luau Execution (server code in a real engine) + Studio multi-client tests (remotes, join and leave) | No game today tests its save wrapper, player session or start-up (`games.md` §2.9). | Luau Execution has no client and no physics, so remotes still need Studio. Two probes first (§6). |
| L15 | **Tooling** | Use Rokit, Rojo 7.7.1, Wally, luau-lsp, Selene, StyLua (pinned) | Already in both games. Add the DS gate checks GWS lacks: remote audit and replication check (`games.md` §4 rank 12). | Fix P5: both games' `wally.lock` names the wrong project. |

| ~~L16~~ | ~~Developer commands~~ | **Removed by the owner 2026-10-24** (closed door CD-6 in `decisions.md`); replaced by L19 | | |
| L19 | **Admin panel** (owner 2026-10-24, `decisions.md` J025-D2) | Own **`Admin`** block, ~400-600 lines, built on our `Screens`, `Net` and `State` blocks and the engine StyleSheet | **Built-ins, ready in every game:** fly, noclip, walk speed and jump, teleport (to a player, a player to me, to spawn, to a tagged place), respawn and heal, kick, server info (players, server FPS, ping, memory), a read-only view of a player's saved data. **Studio-only built-ins:** reset own save, set a saved value. **Per game:** a data table adds pages with buttons, toggles, sliders, text fields and number fields, each bound to a server action; a game can also add its own frame as a page. | The biggest exploit surface in the framework. Rules: the server runs every action and checks the caller (Studio, or a user-id allow-list, optionally a group rank) on every call; the panel's client code sits in `ServerStorage` and only admins get a copy; fly and noclip run on the admin's own client, so a game's movement checks must exempt admins (Server Authority games need a server-side version). Deep review (`reviewer`) and protected tests for "a non-admin call is refused". Alternative: Adonis (MIT, push 2026-10-21) — too big, and it loads its main module by asset id (`rules/packages.md` item 4). |
| L17 | **Analytics wrapper** (added 2026-10-24) | Own, extracted from GWS `Analytics` (84 lines) | Every game logs funnels and economy through `AnalyticsService` with `pcall`; the `analytics` skill already asks for it. It was extraction rank 9 but in no layer. | Currency and funnel names are per-game data. |
| L18 | **Content tests** (added 2026-10-24, owner: content stays Luau) | A Luau test pattern, not a package: one Lune spec per content table checks unique ids, references that exist, ranges | Strict types catch shape; these catch the rest before a player meets it. No compiler, no generated files. | Each game writes its own specs from the pattern. |

Total own code: about 1,900-2,600 lines, plus tests (L17-L19 added on 2026-10-24 after the owner's G1 answer; L19 is owner-requested, its built-in list and limits are PROPOSAL). This is far smaller than either game's copied base, and every part has more than one real user (`rules/anti-overengineering.md` §5).

**What the framework never holds:** game rules, content, art, layouts, sound, physics (DS bricks), economy numbers, an event bus, a dependency-injection layer, a UI theme system, or an ECS (a game adds Jecs only if a measured case needs it).

## 4. What stays per game

| Per game | Example |
| --- | --- |
| Save schema, defaults and migrations | `ProfileTemplate`, `migrations/` |
| Message schema (the Blink file) and handlers | which remotes exist and what each checks |
| Systems | the game's services and controllers in `Systems/` |
| Content as data | items, levels, catalogs, animation and motion tables, config keys |
| Screens and layouts | the Figma-generated layouts; the `Screens` registry table |
| What a purchase grants | product id → grant |
| Game profile and overlays | `knowledge/design/game-profile.md`, `knowledge/overlays/*` |

## 5. How a game starts and how old games adopt it

| Part | Proposal |
| --- | --- |
| Framework code | One repo, `Enjukku/roblox-game-framework` (it exists, empty), one folder per block, tagged versions with a changelog. |
| Getting it into a game | **Owner decision D-3.** Default: private. A kit tool copies a tagged version into the game (`Packages/Framework/`) and writes a lock line (tag + hash); the gate fails if the copy was edited. Third-party packages stay on Wally. Alternative: publish our blocks on the public Wally index (simplest, but the code is public). |
| New game | A **game template** (a GitHub template repo, or `templates/game/` in the kit) with: Rojo, Rokit, Wally files, lint and format configs, the gate, the two entry scripts, the folder layout, one sample system with its test, a filled-in packages row. Target: "player joins, data loads with a lock, a checked remote changes saved data, the UI shows it, the player leaves, data saves" works from the template with no new base code (the job card's success test). |
| Old games (GWS, DS) | One block at a time, each a small job: loader first, then `Session` (same ProfileStore keys, so no data move), then `Net`. Never two transports in one game at the same time. |

## 6. Build plan (after the owner picks)

Superseded by the full plan in `build-plan.md` (2026-10-24: quality bar Q1-Q9 and 12 steps). The short version below stays for reference.

1. **Probes (half a day each, research model):** Blink vs Zap on three real payloads + NaN, inf, oversize and spam tests; DataStore and ConfigService inside an Open Cloud Luau Execution task; Roblox Jest start-up and strict types; `Anim` markers and replication in Studio.
2. **Architect:** one short contract per block (API, invariants, owner of each fact), from the research files.
3. **Build, in this order, each with failing tests first:** L1 loader → L2/L3 `Session` → L4 `Net` → L5 `State` → L9 `Screens` → L11 `Anim` → L10 `Motion` → L12 `Config` → L13 helpers → the game template.
4. **Reviews:** `reviewer` on every block (deep review for `Session` and `Net`: saves and remotes), qa-lead protected tests for the save and remote cases.
5. **Proof:** a blank game from the template passes the success test in Studio with two clients.

## 7. How the kit's agents and books use it

| Kit part | Change (at build time) |
| --- | --- |
| `knowledge/design/game-profile.md` | The packages row becomes "framework version + blocks used + any deviation and why". |
| `engineering-craft` | New reference `references/framework.md`: each block's API and checked patterns. Rule: use the framework block before writing base code. |
| `architecture` | New systems are loader systems; `Session` owns saved data, `State` owns client copies, `Net` owns the remote surface. |
| `data-saving` | §5 Adapters names `Session` as the default adapter and maps each D-rule to the part that keeps it. |
| `networking-security` | The schema file + `Net` checks are the standard path; N-02 steps 3-7 stay in handlers. |
| `code-review` | Grep checks: `DataStoreService` outside `Session`, raw `RemoteEvent` outside `Net`, `LoadAnimation` outside `Anim`, a new transport or state library. |
| `testing` | The three test lanes of L14. |
| `ui-basics`, `animation-craft` | Use `Screens`, `Motion` and `Anim`. |
| `rules/packages.md` | A recorded exception for ProfileStore (if the owner agrees), and one `knowledge/reference/<package>.md` per package. |
| Kit tools | Framework copy tool + lock check in `tools/verify.py`; the DS remote audit and replication check moved into the kit gate. |
| Later (D-135) | The framework steward agent improves the framework from each game; not in this job. |

## 8. Decisions for the owner

| Id | Question | Options | Default (if no answer) |
| --- | --- | --- | --- |
| D-1 | Which framework shape? | 1 thin own layer on proven packages · 2 keep today's stack · 3 write everything | **1** |
| D-2 | Keep ProfileStore under the saves, with a recorded exception to the 12-month rule (we own a pinned copy)? | yes · no, write our own lock | **yes** |
| D-3 | Keep the framework code private? | private (kit copy tool) · public Wally packages | **private** |
| D-4 | UI: plain instances + StyleSheet, or the Vide library? | plain instances · Vide (after a phone probe) | **plain instances** |

The doors these answers close: option 2 and 3 (may return only if a probe in §6 fails), our own session lock (may return only if ProfileStore shows a data-loss bug we cannot patch), public packages (may return if the owner wants to share them), Vide (may return if list-heavy screens cost too much code).

## 9. Checks block

| Check | Label |
| --- | --- |
| Package versions, dates, licences (ProfileStore, DataService, Networker, Charm, Vide, Janitor, Blink, Zap) | spot-checked by `gh api` on 2026-10-24 |
| Installed package source and both games' code | read by agents (file:line in the research files); not run |
| Blink, Jest, Luau Execution, Vide performance | not verified: probes in §6 |
| Games' gates and tests | NOT RUN |
| BAR | fail (floor only): every layer has a dated source, but four choices still need probes before they are locked |

Usage: lead session about 150 k tokens; five Sonnet agents about 750 k in total. No earlier job of this type to compare.
