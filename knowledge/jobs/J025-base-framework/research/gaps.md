---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# J025 gaps: what the Wally index offers that our layers L1-L15 do not cover

Question (owner): is there one tool that would speed up development or lift game quality? Checked 2026-10-24.

## 1. Method and limits

| Item | State |
| --- | --- |
| Index source | `https://api.wally.run/v1/package-search?query=<word>` read through WebFetch on 2026-10-24 (name, scope, version, description). `wally.run` pages render empty; the GitHub `UpliftGames/wally-index` folder list is truncated (611 entries omitted) but per-scope folders list (e.g. `sleitnick/` 35 packages, `evaera/` 6). |
| "Widely used" | NOT measured. The API gives no download counts. Many results are re-uploads and forks (50 TopbarPlus entries, 80 zone entries). I judged use by upstream stars, age and name recognition: an inference. |
| Dates | GitHub API `pushed_at` and latest release, read 2026-10-24. Wally publish dates are not obtainable. |
| `--!strict` | Not verified for any candidate (raw-file checks for `t` and Cmdr returned 404). Item 6 below is "unknown" unless said. |
| Not covered | Download ranking; DevForum threads (not opened); Wally dependency chains beyond `wally.toml` of Cmdr and Iris. |

## 2. Candidates not in our list

Adopt-test = `rules/packages.md` items 1-6: 1 concrete need now, 2 maintained 12 months, 3 licence, 4 small and known, 5 replaceable by adapter, 6 typed. Y = pass, N = fail, ? = not verified.

| Package (Wally id) | Owner | Release / last commit (checked 2026-10-24) | Licence | Size, deps | What it does | Gap in our framework | Engine already does | Adopt-test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **cmdr** `evaera/cmdr` 1.13.1 | evaera | release 2026-09-30; push 2026-10-21; 534 stars, 18 open issues | MIT | no Wally deps (`wally.toml`) | Typed command console with autocomplete, argument types, permissions | No in-game dev/test command surface. Agents set up a test state by clicking UI | `TextChatCommand` (`_api-reference/classes/TextChatCommand.yaml:14`, `chat/examples/custom-text-chat-commands.md:13`): client event, aliases only; no typed args, no permission, no server side | 1 Y, 2 Y, 3 Y, 4 Y, 5 Y (behind a `Dev` adapter), 6 ? |
| **iris** `sirmallard/iris` 2.5.1 | SirMallard / Michael-48 | release 2026-03-27 (7 months); push 2026-10-22; 360 stars | MIT | no deps | Immediate-mode debug UI (Dear ImGui style) | No live state viewer for Session, State, Net | Studio Explorer/Properties and F9 developer console, not usable by agents inside a running multi-client test | 1 ? (humans only), 2 Y, 3 Y, 4 Y, 5 Y, 6 ? |
| **t** `osyrisrblx/t` 3.1.1 | osyrisrblx | push 2025-03-11 (19 months); 334 stars | MIT | one file | Runtime type checks for values | Validation of non-remote data: config tables, save migrations | Blink schema checks remotes (L4); `--!strict` checks only statically | 1 N (Blink covers remotes), **2 N**, 3 Y, 4 Y, 5 Y, 6 ? |
| **typeguard** `itzbbbbas/typeguard` 0.1.0, **schema** `post-ill/schema` 1.0.1 | single authors | not checked | not checked | ? | Runtime checkers whose builders double as static types | Same gap as `t` | same | 2 ?, 3 ? : unvetted, one-person re-implementations |
| **sift** `csqrl/sift` 0.0.11 | csqrl | push 2026-03-26 (7 months); 93 stars | MIT | no deps listed (not checked) | Immutable table/array/dictionary helpers | Charm atoms are updated by immutable copies; plain Luau loops do it | `table.clone`, `table.freeze`, `table.move` (Luau library; not looked up in the mirror) | 1 ?, 2 Y, 3 Y, 4 Y, 5 Y, 6 ? |
| **table-util, timer, observers, shake, spring, input, trove** `sleitnick/*` | Sleitnick (RbxUtil) | push 2026-08-11 (2.5 months); 470 stars, 48 issues | MIT | one repo, small modules | Table helpers, repeating timers, observe tags/attributes/players, camera shake, springs, input | Helpers; `trove` duplicates Janitor, `input` duplicates Input Actions, `signal` already used | Input Actions (`_api-reference/classes/InputAction.yaml`), `CollectionService` events, `task.delay` | 1 N for most; `observers` and `spring` only on demand |
| **partcache** ports (`4igz`, `cg955gtr`...), **ObjectCache** `Pyseph/ObjectCache` | many ports; the original is a Roblox model, not a GitHub repo (not verified) | ObjectCache push 2025-03-19 (19 months), 19 stars | MIT | small | Object pool for parts/models | Many-projectile or many-VFX games | Engine has `BulkMoveTo` (`BasePart.yaml` / `WorldRoot.yaml`, grep hit); pooling is a few lines | 1 N (no game needs it now), 2 N for ObjectCache, 5 Y |
| **zoneplus** (many re-uploads) / **quickzone** `ldgerrits/quickzone` 1.5.1 | 1ForeverHD / ldgerrits | ZonePlus push 2024-07-04 (27 months); quickzone push 2026-10-06, 63 stars | MIT / MIT | medium / small | Player enter/leave region events | Zones (shops, safe areas, quests) | `WorldRoot:GetPartBoundsInBox` (`WorldRoot.yaml`), `Touched` | ZonePlus 2 N; quickzone 1 N now, 2 Y |
| **topbarplus** `1foreverhd/topbarplus` 3.5.0 | 1ForeverHD | push 2026-10-20; 243 stars | NOASSERTION (GitHub could not read it) | medium | Top-bar icons and menus | Top-bar buttons | Default top bar; our `Screens` (L9) | 3 ?, 1 N |
| **log** `vorlias/log` 0.6.4, `howmanysmall/log` 1.0.5, ~40 others | single authors | not checked | not checked | ? | Levelled, structured logging | No log levels or tags; agents read raw Output over MCP | `LogService` (`LogService.yaml`), `warn`, `print` | 1 ? , 2 ?; unvetted |
| **mach6** `revvy02/mach6` 0.1.1, **packetprofiler** `pyseph/*` | single authors | not checked | not checked | ? | Profiler, remote-packet profiler | Performance tracing | `ScriptProfilerService.yaml`, MicroProfiler, `debug.profilebegin` | 2 ?; unvetted |
| **simplepath**, **astar-pathfinding**, **camera shakers**, **sound managers** (dozens of forks) | single authors | not checked | not checked | ? | NPC paths, camera shake, sound pools | Genre systems | `PathfindingService.yaml`, `SoundService`/`SoundGroup` (not looked up) | Game-specific; not framework |
| **abbreviate** `tkdriverx/abbreviate` 0.1.3, **playfab-localization** | single authors | not checked | not checked | ? | Number shortening; locale helper | Number and time text | `string.format`; `LocalizationService.yaml`, `LocalizationTable.yaml` (auto-translate is engine) | 1 Y for a formatter; package unvetted: write ~30 lines instead |
| Analytics: **no package** | n/a | n/a | n/a | n/a | GWS has `Analytics.luau` (84 lines, `games.md` §3 row, §4 rank 9) | **Not in any layer L1-L15**; ranked 9 but dropped from §3 | `AnalyticsService.yaml` | Own wrapper; skill `analytics` exists |

Out of scope (already in list or rejected): Promise, Fusion/Vide/React, Matter/Jecs, Replica/Lapis, Knit, TestEZ.

## 3. Findings that change the picture

| # | Finding | Source |
| --- | --- | --- |
| F1 | Our list has no tool for **checking content tables**. GWS hand-edits 26 config files, 5,618 lines (+3,212 server), no schema check. DS compiles 16,360 JSON files with `contentc.py` (505 lines), but economy and gear only; stages use a second compiler. | `research/games.md:166-168` |
| F2 | The index has **no widely used schema-checked config tool**. The runtime checkers (`t`) fail item 2 or are one-person projects. The only strong precedent is DS's Python compiler. | Wally search `schema`, `guard`, `osyrisrblx` (2026-10-24); `t` push 2025-03-11 |
| F3 | Both games have **no dev command surface**. The only `Dev/` code is DS PhysicsLab/FrameLedger/MemoryLedger, tied to bricks. Test setup for Studio multi-client runs (L14) has no standard way to put a player in a state (money, level, quest step). | `games.md:249`; grep of the J025 folder for Cmdr/admin: 0 hits |
| F4 | Cmdr is the one non-trivial package that is clearly maintained: release 2026-09-30, push 2026-10-21, MIT, no dependencies. Engine `TextChatCommand` is client-only with no typed arguments. | GitHub API 2026-10-24; `wally.toml`; `TextChatCommand.yaml:14` |
| F5 | Most categories (zones, pooling, pathfinding, sound, camera, i18n, number format) are either an engine feature, genre-specific, or have only forks and single-author ports. No framework-wide gain. | tables above |
| F6 | The proposal drops **analytics** between extraction rank 9 and §3 layers. Checks of the funnel are part of the kit's `analytics` skill. | `games.md:231`; proposal §3 |

## 4. The top 3 gaps, ranked

Rank = (a) how much faster agents build and verify, then (b) quality players see.

### Gap 1: schema-checked content and config tables (a: high, b: high) -> write our own small kit tool (Python), not a Luau package

- What: a generic `contentc`-style gate stage. Each game keeps content as data files with a schema (types, ranges, required ids, cross-references, NaN/inf rejected). The tool validates them and writes the typed Luau tables; the gate fails on stale output. Extract from DS `tools/content/contentc.py` and merge the two DS compilers.
- Why a kit tool, not Luau: bad numbers and broken references are found before any Studio run, in the gate, which agents already run (`AGENTS.md` §3). A runtime `t`-style check only fails once a player reaches the row. It also serves the Python-based kit and keeps numbers out of logic modules (`AGENTS.md` §2: content is data).
- Players see: no wrong prices, missing icons or unreachable quests. Agents save the play-test round trips that find typos.
- Weakest part: the schema has to be written per game, and moving GWS's 8,830 hand-edited Luau lines to data files is a large migration (do it per table, when a table is next edited). It stays "own code to keep" (the DS two-compiler drift is the warning). Engine feature that overlaps: `ConfigService` keys (L12) hold live values, not authoring tables.
- Check before building: not verified that DS's compiler generalises; read `contentc.py` first.

### Gap 2: a dev command console, `Dev` adapter over Cmdr (a: high, b: medium) -> use package Cmdr

- What: one `Dev` module registers typed commands (`give money`, `set level`, `jump to quest step`, `dump session`, `fire event`), runs only in Studio or for place-owner ids, and is stripped or disabled in live servers. Cmdr supplies parsing, autocomplete and permissions (MIT, v1.13.1, push 2026-10-21, no deps).
- Why: L14's multi-client Studio tests need a way to reach a state in one step. Without it, every verification replays the game from the start through UI. Commands give agents text output (`dump session`) instead of screenshots, which also cuts image tokens (`rules/assistants/claude.md`, Images row).
- Players see: indirectly, via fewer shipped bugs; the owner can also test balance by command.
- Weakest part: security. A console that reaches live servers is an exploit surface (N-02 in `networking-security`): the gate must prove it is off outside Studio and the `Dev` handlers must not skip `Net` checks. Cmdr adds a client UI and a larger code base than we need; if we use only five commands, a 100-line own table-of-commands module with `TextChatCommand` could be enough (inference, not tested). Strictness of Cmdr: not verified.

### Gap 3: logging and state dump built into the framework (a: medium, b: low) -> write our own small module (~50 lines), no package

- What: `Log` with level and tag (`[Session] warn ...`), one line per event, a ring buffer that a `Dev` command prints. The framework's own failures (load failed, migration run, rate limit hit, remote rejected) go through it.
- Why: agents read Studio Output over MCP as plain text; tagged lines are greppable. The index has about 40 logging libraries, all single-author; none vetted (`vorlias/log` 0.6.4 and `howmanysmall/log` 1.0.5 not checked). A package would break item 2 or 4 until checked, for a 50-line job. Engine `LogService` already reads Output.
- Players see: nothing directly. Live-ops gains a readable trail.
- Weakest part: lowest direct value; only pays off together with Gap 2. If Gap 2 is rejected, drop this one into L13 and move analytics (F6) up instead: add `Analytics` wrapper (pcall-wrapped `AnalyticsService`, funnel steps from data) as a framework helper, because new player steps and quit points need it in every game (`AGENTS.md` §2).

## 5. Honorable mentions and what to skip

| Item | Verdict |
| --- | --- |
| Number and time formatter (`1.2K`, `mm:ss`) | Write ~30 lines into L13; every UI needs it; visible polish. |
| Iris | Skip for now: humans only; agents cannot read it without screenshots. Revisit if the owner wants a live debug panel. |
| `t`, ZonePlus, ObjectCache | Fail item 2 (maintained within 12 months): 19, 27 and 19 months. |
| Sift, RbxUtil modules | Not needed now; `table.clone`/`table.freeze` cover Charm updates. Adopt on a concrete case only. |
| Localization | Engine `LocalizationService`/`LocalizationTable` with auto-translate; a game-profile decision, not a package. |

## 6. Recommended next action

Lead names Gap 1 (schema-checked content tool) as the single highest-value gap; ask `kit-engineer` for a short probe of `tools/content/contentc.py` (does it generalise?) before adding it to the build plan. Offer Gap 2 as the Luau-side runner of Gap 1's data (Cmdr behind `Dev`) only after a probe of security (Studio-only) and strictness.

## 7. Evidence list

| Evidence | Date |
| --- | --- |
| `api.wally.run/v1/package-search?query=cmdr, iris, sift, partcache, osyrisrblx, zone, log, profiler, topbar, localization, schema, abbreviate, sound, camera, pathfinding, guard` | 2026-10-24 |
| `api.github.com/repos/osyrisrblx/t, evaera/Cmdr, SirMallard/Iris, csqrl/sift, Sleitnick/RbxUtil, Quenty/NevermoreEngine, 1ForeverHD/ZonePlus, 1ForeverHD/TopbarPlus, ldgerrits/quickzone, Pyseph/ObjectCache`; releases for Iris and Cmdr | 2026-10-24 |
| `raw.githubusercontent.com/evaera/Cmdr/master/wally.toml`, `SirMallard/Iris/main/wally.toml` | 2026-10-24 |
| `api.github.com/repos/UpliftGames/wally-index/contents/sleitnick, evaera` | 2026-10-24 |
| `Roblox/PartCache` repo: 404 (original is not a GitHub repo of that name; not verified) | 2026-10-24 |
| Local: proposal §3, §7; `research/games.md:162-183, 217-249`; `rules/packages.md`; mirror classes cited above | 2026-10-24 |
