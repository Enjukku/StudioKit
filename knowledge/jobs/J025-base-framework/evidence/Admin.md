---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B8
---
> Author: feature-builder · claude-opus-5-5 · high · 2026-10-24

# Admin block: Q1-Q9 evidence (J025-B8)

Artifact: `roblox-game-framework/src/Admin/` {init.luau 546, Builtins.luau 261, Client/{init.client 230, Panel 399, Core 79}, specs Admin/AdminNet/Planted/Usage, Admin.engine.spec, test/{World,Lune}}, files as of 2026-10-24 (uncommitted, rule 7). Contract `contracts/Admin.md` (frozen r2). Lune 0.11.1, luau-lsp new solver. Labels: G gate-verified (Lune lane), NV not verified (engine).

**Red run (before behaviour):** Admin.spec against a stub with the contract API and no behaviour: 25 of 27 red, each at its own row (`expected true, got false` Ad-T1/2/3/15; `AdminAction has no listener` for every call row; `step 0: expected start to error` Ad-T9). The 2 green rows test the real Builtins cut and a source grep. Order note: the first draft of init.luau existed before the specs; the stub run stands in for the pre-code red.

## Q1 API (G)
3 public functions (`start`, `isAdmin`, `isExempt`) + types `Control`, `Page`, `Action`, `Def`, `Remotes`; spec hook `_debugCounts`. **One field beyond the contract:** `Def.client: ModuleScript?` (needs-decision, below).

## Q2 types (G)
All 12 files `--!strict`; luau-lsp 0 errors in src/Admin (gate types: the 11 errors are in `tests/acceptance/Net/`, QA's parallel work). `:: any` in exported types: 0. Internal `:: any`: 2 (Panel.luau:84, :93, property bag of `make`).

## Q3 test rows → specs (G unless NV); planted faults 14/14 red
| Row | Spec (file: test name prefix) |
| --- | --- |
| Ad-T1 | Admin.spec `Ad-T1 a user id in allow…` |
| Ad-T2 | Admin.spec `Ad-T2 group rank >= minRank…` (GroupService:GetRolesInGroupAsync fake; throw = not admin + 1 warn) |
| Ad-T3 / Ad-T15 | Admin.spec `Ad-T3 Studio rule…`, `Ad-T15 Studio, group-owned place…` (+ creator not admin outside Studio) |
| Ad-T4 | Admin.spec `Ad-T4 a non-admin calls every…` (20 ids × 3 targets; spies, Humanoid, pivots, save, kicks, prints unchanged; 1 sampled line per 10 s); AdminNet `Ad2 (Net)…`; engine `Ad-T12…Ad-T4 refusals from Player2` NV |
| Ad-T5 | Admin.spec `Ad-T5 resetSave and setSaved outside Studio…`, `Ad-T5 in Studio…`; Session lock: `src/Session/Session.spec.luau:711-724` (existing) |
| Ad-T6 | Admin.spec `Ad-T6 slider…10 -> 8`, `Ad-T6 values outside their control…` (24 values + 5 target ids) ; AdminNet `Ad4 (Net) NaN…` |
| Ad-T7 | Admin.spec `Ad-T7 unknown action…`, `Ad5 a game action with target…`; AdminNet `Ad-T7 (Net) throws…`, `Ad-T7 (Net) admin spam…` |
| Ad-T8 | Lune side: Admin.spec `Ad-T8 (Lune side) present before start…`, `Ad6 the copy carries…`; Studio: Admin.engine.spec `Ad-T8…` NV |
| Ad-T9 | Admin.spec `Ad-T9 start errors on a bad def…` (18 cases; no half state) |
| Ad-T10 | Admin.spec `Ad-T10 three actions…`, `Ad-T10 150 actions…` |
| Ad-T11 | Admin.spec `Ad-T11 fly on…1,000 joins leave 0` |
| Ad-T12 | Lune side: 5 Admin.spec `Ad-T12…` tests (each built-in); Studio: engine `Ad-T12…` NV |
| Ad-T13 | Planted.spec (14 faults, each red at its row's own assertion; reasons checked one by one) |
| Ad-T14 | Admin.spec `Ad-T14 saveView of a 100 KB save…`, `Ad-T14 the cut never splits…`; group-throw half in Ad-T2 |
| Ad-T16 | grep: Admin.spec `Ad-T16 (grep)…` G; boot in a Server Authority place: engine `Ad-T16…` NV |

Planted (Planted.spec, G): caller check removed → T4 `got done/nil`; Studio check removed → T5 Session reached (`expected 0, got 2`); NaN slider accepted → T6 `grid with nan: got done`; snap up (R5) → `expected 8, got 12`; copy to everyone → T1 non-admin has panel; group fail-open → T2; creator without CreatorType → T15; absent target → admin → T7; a line per refusal → T4 `got 60`; exemption kept on respawn → T11; leave keeps admin → T11 sampler; no log → T10; no save cut → T14; start connects before validation → T9.

## Q4 failure rows → specs (G)
Non-admin call: Ad-T4. Group read fails: Ad-T2. Admin or target leaves mid-action: Ad-T7 (left target `no_target`), character gone `Ad-T12 goto…`. Game action errors: AdminNet `throws`. Spam: AdminNet `spam`. Save over 65,535: Ad-T14. Fly in a Server Authority place: no read (Ad-T16 grep); boot NV.

## Q5 leak (G)
`Ad-T11`: 1,000 cycles (admin joins, fly on, info, leaves; a non-admin joins and leaves) → `_debugCounts` {joined 0, admins 0, exempt 0, allowance 0, sampler 0}; live fake connections = baseline − 2 (the last admin's CharacterAdded and the sampler).

## Q6 cost (Lune screen G; engine NV)
Per call over 10,000 (Admin.spec Q6): not_admin 0.20 µs, accepted `core.heal` 1.7 µs (budget 0.2 ms). Non-admin flood allocation: ≤ 4 KB gcinfo growth over 10,000 calls (asserted; a string per refusal was found and removed). `core.info` build 21 µs (10 players) / 44 µs (50). **Info size over its PROPOSAL budget:** JSON 5.4 KB (10 players, full ring of 100) / 7.6 KB (50 players) vs ≤ 4 KB: the 100-line ring alone is ~4.6 KB with 10-digit ids. Hot-path allocations: accepted actions build one log string (Ad8); refusals none.

## Q7 server entry point: AdminAction (init.luau:157), behind Net (present, Session status, rate 10/s burst 20, NaN/UTF-8/depth walk)
Order: caller :158 → Studio :162 → action exists :165 → value :167 (`accept` :120, finite :128/:134) and target id :168 → target present :179 → log :182 → run.
| Action | Caller | Type | NaN/inf | Range | Rate | State |
| --- | --- | --- | --- | --- | --- | --- |
| core.fly, core.noclip | T4 | boolean T6 | n/a | n/a | Net T7 | self only; flags cleared respawn/leave T11 |
| core.walkSpeed, core.jump | T4 | number T6 | T6, Net Ad4 | 0-500 snapped T6, T12 | Net | target present T7; Humanoid present T12 |
| core.goto, core.bring | T4 | nil, target id integer T6 | target id NaN T6 | n/a | Net | target present T7; both characters T12 |
| core.spawn, respawn, heal | T4 | nil T6 | target id T6 | n/a | Net | target present; SpawnLocation / Humanoid T12 |
| core.place | T4 | text ≤ 100 B, UTF-8 T6 | n/a | name exists T12 | Net | admin character T12 |
| core.kick | T4 | integer T6 | T6 | 1-4 T6 | Net | target present T7; fixed text T12 |
| core.info | T4 | nil | n/a | n/a | Net + 2/s T12 | n/a |
| core.saveView | T4 | nil | target id T6 | ≤ 65,535 B T14 | Net | online target, data loaded T14 |
| core.resetSave, setSaved | T4 | text, path=value T5 | inf/nan text T5 | ≤ 100 B | Net | Studio T5 + Session lock |
| game actions | T4, Q9 | per control T6 | T6 | T6 | Net AdminNet | target = true present T7; the game's own state |

## Q8 engine features (docs mirror paths)
Players `GetPlayers` sweep `Players.yaml:1553-1558`; `GetPlayerByUserId` :1085; placement `scripting/security/access-control.md:65-75`; group `GroupService.yaml:317-384` (`GetRolesInGroupAsync`; `Player:GetRankInGroupAsync` is **Deprecated**, `Player.yaml:1741-1746`, `GroupService.yaml:346`); `Player.yaml` `Kick` :2078, `LoadCharacterAsync` :2238, `GetNetworkPing` :1655 (round trip, s), `RespawnLocation` :983; `Humanoid.yaml` `JumpHeight` :608, `JumpPower` :640, `UseJumpPower` :1132, `WalkSpeed` :1159, `MoveDirection` :778, `PlatformStand` :866; `PVInstance.yaml` `GetPivot` :97, `PivotTo` :120; `CollectionService.yaml:325`; `HttpService.yaml:295`; `Stats.yaml:707`; `DataModel.yaml` `CreatorId` :27, `CreatorType` :52, `PlaceVersion` :283; `Instance.yaml:1198`; client fly `LinearVelocity.yaml:180,334,391,415`, `AlignOrientation.yaml:91,195,337`, `RunService.yaml:962`. `Workspace.AuthorityMode` never read (`Workspace.yaml:153-165`).

## Q9 usage (G)
Usage.spec `Q9 the contract's usage example runs…`: the example as written, plus 2.5 and 0 refused by Admin and a non-admin refused.

## Engine specs written, not run
`src/Admin/Admin.engine.spec.luau`: Ad-T8 (clients/solo), Ad-T12 + Ad-T4 from Player2 (clients), server side of Ad-T4/T8, Ad-T16 (authority). Need the template's entry wiring (step 7).
## T-14 (2026-10-24, feature-builder): review R1, R2
| Item | Red (before the fix) | Green / planted |
| --- | --- | --- |
| R1 `Ad-T11 walk speed or jump set back to the StarterPlayer default ends the exemption (review R1)` | `Admin.spec.luau:463 expected false, got true` (speed 32 -> 16 kept the exemption) | fix `Builtins.luau`: flags `speed`, `jump` set while value ~= `StarterPlayer.CharacterWalkSpeed` / `CharacterJumpPower` or `CharacterJumpHeight` (by `UseJumpPower`); plants "speed ... keeps" red at :463, "jump ... keeps" red at :467 |
| R2 Ad-T9 cases `group minRank 0`, `-1` (error must name `group.minRank`) | `Admin.spec.luau:375 expected start to error, got nil` | fix `init.luau` start: `problem("group.minRank is <n>; it must be 1 or more ...")`; plant `elseif false` red at :375 |
Docs: `_api-reference/classes/StarterPlayer.yaml:243-249` (CharacterJumpHeight 7.2), `:272-278` (CharacterJumpPower 50), `:358-364` (CharacterWalkSpeed 16); none Deprecated. Fake: `test/World.luau` gets a StarterPlayer service (16 / 50 / 7.2) and `Options.root` (default `src`; a game passes `Framework`). Known limit: a JumpHeight place's default 7.2 is off the slider's step-1 grid, so there an admin cannot reset the jump exemption; it ends on respawn or leave.
Runs: `lune run tools/spec/run.luau src/Admin tests/acceptance/Admin` 13 files, 99 passed, 0 failed (acceptance Admin green, unedited); Admin Planted.spec 17 faults. Gate: types `0 errors, 0 deprecated in src`; specs 486 passed, 1 failed (`tests/acceptance/Net/Planted.spec.luau:43` P03, QA's Net work in progress, not Admin). sha256 after: `init.luau` bb1293821bc96c1a13acd5c7305a58d9462187f70a6707fb051d0a4fac815f2c, `Builtins.luau` cbf4e7ee62a2e61be370aa4b4358ee74ce431624d5952c9f804ed558dd797f8c, `test/World.luau` 8cb7ecbe3e8c80b3e34e2e510c64e2c13da9042cf630ec44c9b02ecd13566bc6.
