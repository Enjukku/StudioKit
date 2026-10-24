---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-Q3
supersedes: []
---
> Author: qa-lead · claude-opus-5-5 · medium · 2026-10-24

# Admin protected acceptance: trace table, planted faults, verdict (J025-Q3)

## Sources (revision = file as of 2026-10-24)
| Source | Revision |
| --- | --- |
| `roblox-game-framework/contracts/Admin.md` (frozen) | Ad1-Ad10, Built-in tools, Server-authority order, Tests |
| `build-log.md` CC-16..CC-19 | CC-17 negative target ids; CC-19 all of Admin in ServerScriptService |
| `contracts/README.md` rule 6 | one sampled line per kind per 10 s (PROPOSAL) |
| `build-plan.md` Q5 | 1,000 cycles leave 0 connections and 0 entries |
| Candidate | `src/Admin/init.luau` sha256 `a509b4f5437cdf65b4769a014a79ba83ced1e395704adcef90d777d638fe3984`; `src/Admin/Builtins.luau` `6f4e60f55c1a0c3df5723112cb6f183f26bfe8f480ee28822a6e9982d36b77e3`; fakes `test/World.luau` `7a5f4637…09dd`, `test/Lune.luau` `d37886cb…3076`, `Client/Core.luau` `d44c6d4b…b6d277` |

Lane: Lune 0.11.1, offline, fake engine (`src/Admin/test/World.luau`) with the fake Net (Admin's own handler is what runs). Protected: `tests/acceptance/Admin/` (qa-lead only). Expected values from the contract; the built-in id list and the Studio-only list are copied from the contract into `Harness.luau`, not read from `Core.luau`.

## Trace table
Player-facing rows (PF): n/a. This is a server security block with no visible output of its own; the panel's look and feedback are not in this brief.

| Row | Behaviour / failure (contract) | Spec (file: test prefix) | Oracle | Plants that turn it red |
| --- | --- | --- | --- | --- |
| A1 | Non-admin calls every built-in (15) and every game control kind (5), targets none/self/admin/absent, valid values: `denied, not_admin`; world, Humanoids, pivots, attributes, exemptions, panels, kicks, game spies, Session calls, pushes, log unchanged; counted (core.info `denied.Admin` = 80) | Caller: `Ad2 a non-admin calls every` | Ad2; world snapshot equality; count = calls made | P01, P19, P25 |
| A2 | Order: non-admin's Studio-only (in and out of Studio), unknown id, non-string id, NaN, out of range, wrong target type, 500-byte text: all `not_admin` | Caller: `Ad2 order` | Server-authority order line | P01, P32 |
| A3 | Loses admin: late call from a departed admin's Player, and from a departed group admin: `not_admin`; rejoin below minRank: `not_admin`, no panel | Caller: `Ad2 a player who loses admin` | Ad1 decided per join; Ad2 | P01, P05, P07, P27, P28 |
| A4 | Admin outside Studio, each Studio-only built-in (valid, malformed, wrong-type values): `studio_only`; Session never called; nothing changed | Studio: `Ad3 outside Studio` | Ad3; order (Studio before value) | P02, P06, P19 |
| A5 | Studio-only list is exactly the contract's: every other built-in runs outside Studio (kick a present player: done, gone); in Studio reset/set reach Session with path `{currency,gold}` value 5 | Studio: `Ad3 the Studio-only list` | Contract built-in table | P04, P07, P19 |
| A6 | Allow-list: listed ids admin with panel; unlisted neither | Who: `Ad1 allow-list` | Ad1 | P05, P19 |
| A7 | Group: rank 255 and 100 (= minRank) admin; 99, non-member not; rank read throws: not admin, no panel, one warn; not promoted later | Who: `Ad1 group rank` | Ad1 fail closed | P01, P05, P20, P21 |
| A8 | Studio: -1 yes, -2 no; user-owned place creator yes, other user no; group-owned place: user id = group id no, -1 yes; live server: -1 and creator no, allow-listed yes | Who: `Ad1 Studio` | Ad1, Ad-T15, `DataModel.yaml:27-35,52` | P19, P22, P23 |
| A9 | Game controls: number (NaN, ±inf, 0, 1e6+1, 2.5, "5", true, table, nil), slider (NaN, ±inf, ±0.001 outside, "8", true, table, nil), toggle (1, 0, "true", NaN, table, nil), text (21 bytes on max 20, number, bool, table, nil), button (1, false, true, "", NaN), non-integer number 0..1 (NaN, ±inf, outside, "0.5"): `bad_input`, no action ran, nothing changed; limits 1, 1e6, 20 bytes, false, nil, 0.5 accepted and reach the action unchanged | Values: `Ad4 game controls` | Ad4 | P03, P08, P09, P10, P11, P14 |
| A10 | Slider snap (min 0 max 10 step 4): 10→8, 9.9→8, 8→8, 7.99→4, 4→4, 3.99→0, 0→0; (min 1 max 10 step 4): 10→9, 9→9, 8.99→5, 4.9→1, 1→1 | Values: `Ad4 slider snap` | Ad4 formula `min + floor((v-min)/step)*step` (review N3) | P03, P12, P13, P14 |
| A11 | Built-in limits: walkSpeed 501, -1, NaN, inf, "16"; jump -inf, 500.5; kick 0, 5, 2.5, NaN, free text; fly 1; noclip "on"; heal 1; place and setSaved 101 bytes; setSaved false: `bad_input`, nothing changed; walkSpeed 500 and 0 accepted | Values: `Ad4 built-in values` | Built-in table limits (0-500, reasons 1-4, text 100) | P03, P08, P10, P11, P14 |
| A12 | Absent target (none sent, 999, -2 absent, a player who left) for every "target" action (goto, bring, kick, saveView, give_coins) and every "self or target" action (walkSpeed, jump, spawn, respawn, heal): `no_target`, no fallback to the admin, no save pushed | Targets: `Ad5 an absent target` | Ad5 | P04, P16, P19 |
| A13 | Target id "200", 200.5, NaN, ±inf, true, table: `bad_input`, nothing changed; present -2 is a valid target (healed) | Targets: `Ad5 a target id that is not` | Ad4/Ad5, CC-17 | P15, P19 |
| A14 | Non-admin never receives the panel: joined before start, normal join, after respawn, failed group read, Studio -2 (no FrameworkAdmin, Pages, Frames or LocalScript anywhere under the Player); admin gets exactly one copy, ResetOnSpawn false, pages and frames are copies, originals stay in ServerStorage | Panel: `Ad6 a non-admin never receives` | Ad6 | P05, P19, P20 |
| A15 | Pages in ReplicatedStorage, Workspace or unparented; frames in ReplicatedStorage or Workspace: `start` errors, AdminAction not answered, an allow-listed admin gets no panel; pages in ServerScriptService start | Panel: `Ad6 pages or frames outside` | Ad6, `access-control.md:65-75` | P17, P18 |
| A16 | Placement data: `src/Admin` maps to `ServerScriptService` only in `tools/placement.json` and to `ServerScriptService.Framework.Admin` only in `test.project.json` | Panel: `Ad6 CC-19 placement data` | CC-19 | none (data row: fails when a project file moves Admin) |
| A17 | Flood: 1,000 non-admin calls over 100 virtual s, every id with mixed values and targets: all `not_admin`, nothing changed, `_debugCounts` unchanged, warn lines between 1 and 11, 0 accepted-action lines, `denied.Admin` = 1,000 | Flood: `Ad2 flood: 1,000` | Ad2, README rule 6 | P01, P19, P24, P25, P32 |
| A18 | No per-call state: 10,000 non-admin calls, live heap (collector forced through a full cycle) grows ≤ 128 KB | Flood: `Ad2 flood: a non-admin call keeps no` | Budget "non-admin 0 cost" | P01, P24, P26, P32 |
| A19 | Leaks: 1,000 cycles of admin join, panel present, core.info, fly on, walkSpeed, fly off, non-admin join + refused call, both leave: `_debugCounts` all 0, live connections back to the post-start value | Leak: `Ad9 leaks` | Ad9, Q5 | P01, P19, P27-P31 |

## Planted faults (through `World.patch`; `src/` never edited)
Result: **32 of 32 caught**, each by its target spec with its own label (Planted.spec.luau); false alarms on the unpatched build: **0** (the 19 specs pass). Full matrix (every plant × every spec, run once in a throwaway spec): above, column 5.

| Plant | Fault | Target spec | Label |
| --- | --- | --- | --- |
| P01 | caller check removed | Caller A1 | `[Ad2] non-admin` |
| P02 | Studio check removed | Studio A4 | `[Ad3] live admin` |
| P03 | value check removed | Values A9 | `[Ad4]` |
| P04 | target check removed | Targets A12 | `[Ad5]` |
| P05 | clone-only-to-admins removed (both guards) | Panel A14 | `[Ad6] non-admin` |
| P06/P07 | Studio-only flag off / on for every built-in | Studio A4 / A5 | `[Ad3]`, `[Ad3 list]` |
| P08/P09 | finiteness dropped: slider / non-integer number | Values A9 | `grid value NaN`, `ratio value NaN` |
| P10/P11 | text length / integer check dropped | Values A9 | `motd value`, `give_coins value 2.5` |
| P12/P13 | snap from 0 / snap up | Values A10 | `offset`, `grid 10` |
| P14 | value check removed (built-ins) | Values A11 | `[Ad4 builtin]` |
| P15/P16 | target type check dropped / absent target falls back to admin | Targets A13 / A12 | `[Ad5 type]`, `[Ad5]` |
| P17/P18 | pages / frames placement check dropped | Panel A15 | `[Ad6 start] pages/frames` |
| P19-P23 | allow-list ignored; group fail open; `>` minRank; creator without CreatorType; Studio rules live | Who A6-A8 | per plant |
| P24-P26 | log per refusal; refusals not counted; per-call string kept | Flood A17/A18 | `sampled lines`, `counted`, `live heap growth` |
| P27-P31 | admin flag, exemption, info allowance, CharacterAdded kept after leave | Caller A3, Leak A19 | `late call after leave`, `Admin entries`, `live connections` |
| P32 | caller check moved after Studio/action/value checks | Caller A2 | `[Ad2 order]` |

Equivalent mutants (not counted as plants): removing only one of the two Ad6 guards (`onJoin` admin test, `givePanel` admins test) leaves the panel admin-only: the other guard holds it (checked once, both specs green). Defence in depth, not a gap.

## Results (verdict bound to the candidate hashes above)
| Check | Verdict | Evidence |
| --- | --- | --- |
| 19 specs + 32 plants, `lune run tools/spec/run.luau tests/acceptance/Admin` | PASS, gate-verified | `specs: 9 files, 51 passed, 0 failed`; 3 runs, byte-identical output (sha256 `7c4256a9913d7968…` ×3); hashes of init/Builtins identical before and after |
| Gate `python tools/gate.py` | FAIL (not Admin) | transport, format, lint, rules, types, build, copy-tool PASS; specs `472 passed, 6 failed`, all in `src/Net/Transport.spec.luau` (Net-T16 :222, Net-T23 :442, :469, :484) and `tests/acceptance/Net` (Framework X1 :37, Planted P09 :44): Net mid-repair by others |
| First attempt vs repaired | First candidate passed every frozen spec; 0 product repair rounds. Test-side fixes before freezing: one spec order bug (my own refused call counted as a warn), one plant syntax error (caught by its label), one flaky memory oracle replaced (below) | this file |

Flake found and removed: a `gcinfo()` delta missed P26 in one matrix run (garbage left by earlier specs was collected during the measurement). Replaced by a live-heap reading after a forced full collector cycle: clean -48..0 KB vs planted ~520 KB per 5,000 calls; now 10,000 calls with a 128 KB limit.

## Could not check (lane cannot show it)
| Item | Missing input | Closes it |
| --- | --- | --- |
| A real exploit client firing AdminAction; Net's checks in front (rate, NaN before Admin, not_ready) | real transport, two clients | `src/Admin/AdminNet.spec.luau` (builder) + Studio multi-client Ad-T4/Ad-T8 (P2-5) |
| `ResetOnSpawn` on a real respawn; a non-admin client's PlayerGui in a real server | Studio play with 2 clients | Ad-T8 Studio multi-client |
| Panel client open/close cycles (Screens, client) | Studio client | Ad-T12 Studio |
| `GroupService:GetRolesInGroupAsync` real answer shape and real `RunService:IsStudio()`/`CreatorType` | engine | Admin.engine.spec (Studio) |
| Session's second Studio lock | real Session | Session acceptance |

## Questions (with defaults)
1. "Loses admin mid-session": the contract decides admin once per join (Ad1), so a player removed from `allow` or demoted in the group keeps admin until they leave. Default: keep (contract); tested as leave + late call and rejoin after demotion.
2. Text `maxLength` unit is not stated in Ad4 (code counts bytes, `Core.luau` TEXT_MAX comment). Default: bytes; no multi-byte case in the set.
3. Net acceptance X1 expects a `0` target refused while CC-17 widened the target range to negative integers: Net owners to confirm the X1 expectation still matches CC-17.

## Weakness of this set
The memory oracle (A18) is a screening aid: it proves no retained state per call in Lune's collector, not Roblox server memory; and every row runs on the builder's fake engine, so a fake that disagrees with the engine (Instance cloning, `IsDescendantOf`, signals) would hide a real fault. Next step: the Studio multi-client Ad-T4/Ad-T8 run (P2-5).

## Result card (owner)
Admin refuses every non-admin call for every tool, keeps Studio-only tools off live servers, refuses bad numbers, text and targets without changing anything, sends the panel only to admins, stays quiet and stateless under a 1,000-call flood, and leaks nothing over 1,000 join/leave cycles: 19 checks, each shown able to fail (32 planted faults caught). Gate-verified offline only; the two-client Studio run is still to do.
