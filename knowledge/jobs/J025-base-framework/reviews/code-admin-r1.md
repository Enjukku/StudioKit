---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · high · 2026-10-24

# Review: Admin code rev 1 + Session repair round 3 recheck (J025-R-Admin), by reviewer

Artifact: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\src\Admin\` (A) and `vendor/ProfileStore/init.luau` + `src/Session/init.luau` (B). Repo uncommitted (rule 7): revision = sha256 below. Depth: **deep** (A: remotes, permission, Studio-only save writes; B: saves). Round 1 for Admin; selective recheck for R2-1. Code read before `evidence/Admin.md` and `evidence/Session.md` "Repair round 3". Contract `contracts/Admin.md` (frozen r2) + CC-16..CC-19, J025-D2, Q1-Q9.

Feature verb: **grant admin power** (permission, Studio-only save writes, kick, move other players). Weighted most: harm area 2 (who can act, what reaches which client), then 4 (per-player state), then 8 (size).

Goal questions: (1) Can a non-admin run any action, or a Studio-only action run outside Studio (Ad1-Ad3, Ad10)? (2) Can a non-admin client receive the panel code, pages or frames (Ad6)? (3) Does every accepted value and target fit its control (Ad4, Ad5), and is a flood bounded before Admin (Net rate)? (4) Does any per-player or per-open state, or any exemption, outlive its reason (Ad9, Q5)? (B) Does only the release's own save clear the same-server rejoin hold, with the stored record unchanged (R2-1)?

## Files reviewed (sha256)

| File | Lines | sha256 |
| --- | --- | --- |
| src/Admin/init.luau | 546 | a509b4f5437cdf65b4769a014a79ba83ced1e395704adcef90d777d638fe3984 |
| src/Admin/Builtins.luau | 261 | 6f4e60f55c1a0c3df5723112cb6f183f26bfe8f480ee28822a6e9982d36b77e3 |
| src/Admin/Client/init.client.luau | 230 | 57d6ca6ba188fd6b2d34b932b5693a5fc784eccf61b6bace897700fb112416fb |
| src/Admin/Client/Panel.luau | 399 | 0ba6fa3e6162b3f7bdaec83a3a751ae77730ee4e5f571db455d74d3639eff239 |
| src/Admin/Client/Core.luau | 79 | d44c6d4b28d7abe2daa423fb60fb67486a0c3472aa6b9d2a3e7805a6ceb6d277 |
| src/Admin/test/World.luau | 535 | 7a5f4637f1e33c19e8410de349ba0b66946e52654b960a31fb19c0f588f709dd |
| src/Admin/test/Lune.luau | 31 | d37886cb2556464b084780e10aa56ad81b5fcd11a3554293816688cd73693076 |
| vendor/ProfileStore/init.luau | 2242 | cfda9e90c3ea8e712f8233c30efebd35c801d7e4d30c20b914c3f8c8c2556a03 (matches brief) |
| src/Session/init.luau | | 4dee452194b19820febb3070b3c6981d388973ac1ca41ce22e238fcd4c3b2eb7 (matches brief) |

## Runs (2026-10-24)

| Run | Last lines | Label |
| --- | --- | --- |
| `python tools/gate.py` | transport, format, lint, rules PASS; `types 0 errors`; `specs 418 passed, 4 failed`; build, copy-tool PASS; engine SKIP (12 Jest specs); `RESULT: FAIL` | gate-verified |
| the 4 spec failures | all in `tests/acceptance/Net/` (Flood F3, F4, F5; Leave L4): Net repair in progress, **not counted**. Every `src/Admin` spec (incl. Planted.spec, 14 faults), `tests/acceptance/Admin` (Caller, Studio, Who) and every Session spec (incl. the 5 R2-1 rows) pass | gate-verified |
| vendor diff: GWS `ProfileStore.luau` (sha 799263dc…, matches PATCHES.md) vs `init.luau`, line endings normalised | exactly 3 changed lines: `:130` doc, `:924` `Fire(profile.LastSavedData, is_ending_session == true)`, `:984` listener type | code read (D) |
| engine APIs used, against `_api-reference/` | all exist, none tagged Deprecated: `GroupService:GetRolesInGroupAsync` (`GroupService.yaml:317-384`, args userId, groupId; returns IsMember + Roles[].Rank), `Player:GetNetworkPing` :1655, `LoadCharacterAsync` :2238, `RespawnLocation` :983, `Players:GetPlayerByUserId` :1085, `LinearVelocity` MaxForce/RelativeTo/VectorVelocity/VelocityConstraintMode :180/:334/:391/:415, `AlignOrientation` CFrame/Mode/RigidityEnabled :91/:195/:337, `RunService.PreSimulation` :962, `Humanoid.UseJumpPower` :1132, `MoveDirection` :778, `Stats:GetTotalMemoryUsageMb` :707. `Player:GetRankInGroupAsync` is Deprecated (`Player.yaml:1743`) and not used | code read (D) |

## (B) Session repair round 3: R2-1

| Finding | State | Sequence re-traced |
| --- | --- | --- |
| R2-1 (early clear of the release hold) | **closed** | Vendor: `OnAfterSave` fires only at `:924`, inside `SaveProfileAsync`; its second argument is that call's own `is_ending_session`. Non-ending saves in flight at leave (autosave `:2150`, `Profile:Save` `:1189`, receipt) fire `false`; every ending caller fires `true` once it lands: `EndSession` `:1092`, force-load `:845` and `:1347`, load-after-close `:1554`, shutdown `:2226`. `Profile:Overwrite` (`:1134`) breaks before `:924` (no fire, as upstream). Session `init.luau:292-296` clears `releasing[userId]` only on `ending == true`; `:417` (receipt wait) ignores the new argument. P1: the receipt save lands `false`, hold stays, the rejoin loads after the release: 143 (spec green). P2: A's release lands on B's record, still `is_ending_session` true, mark cleared, rejoin ready (spec green). Planted P-1 off turns P1 red (green). |
| Record byte-compatibility | **holds** | The diff touches no `EditProfile` line (`:745-806`), no key, retry or back-off; the stored record cannot change. Spec "P-1 keeps records byte-identical" (GWS v0, DS v1) green. |
| New problems in the 3 vendor lines or the Session lines | none | The extra signal argument is ignored by every other listener (`grep OnAfterSave` in src, template: only Session `:292`, `:417`). A release that never lands keeps the hold (CC-6, degraded at 120 s), unchanged by design. |

## (A) Admin findings

No blocking findings. Two recommendations, one records note.

```text
<spec>
artifact: roblox-game-framework/src/Admin/@sha256 above (rev 1)
reviewer: reviewer
looked_at_first: [src/Admin/init.luau, Builtins.luau, Client/{init.client,Panel,Core}.luau, src/Net/framework.blink, template/default.project.json, test.project.json, _api-reference GroupService/Player/LinearVelocity/AlignOrientation]
findings:
  - {id: R1, class: recommendation, where: "src/Admin/Builtins.luau:133-134, :151; src/Admin/init.luau:187-199", expected: "contracts/Admin.md API: isExempt is true 'while ... a changed walk speed/jump is on' (Ad9: exemptions end with their reason)", observed: "core.walkSpeed and core.jump set flag 'move' for any accepted value, including the default. Sequence: admin sets player X WalkSpeed 32, then back to 16 -> X stays isExempt until X respawns or leaves -> the game's movement checks skip X; an exploiter X can speed-hack undetected for the rest of that life. Harm area 2, bounded (needs an admin to touch X; ends on respawn)", evidence: "Medium. Code read (D): the only clears are setExempt(on=false) for fly/noclip, clearExempt on CharacterAdded, onLeave. No spec sets a speed back to default (Admin.spec Ad-T11/Ad-T12)", smallest_fix: "in the two runs: exempt(who, 'move', value differs from the default) where the default is StarterPlayer.CharacterWalkSpeed / CharacterJumpPower or CharacterJumpHeight (whichever UseJumpPower selects); a game-changed default stays the game's call", protect: "fly/noclip flags; respawn and leave clears (Ad-T11)", retest: "Admin.spec: walkSpeed 32 -> isExempt true; 16 -> false; jump likewise; planted 'always true' turns it red"}
  - {id: R2, class: recommendation, where: "src/Admin/init.luau:473 (start), :285 (decide)", expected: "Ad1: the group rule admits ranked members; Ad7: start refuses a def that cannot mean what it says", observed: "start accepts any finite minRank. GetRolesInGroupAsync returns IsMember false and no Roles for a non-member, so rankOf = 0 (:254-266). With minRank = 0 (or below), a game meaning 'any member' makes every player in a live server an admin: panel copied, kick, bring, saveView of everyone", evidence: "Low (needs a wrong def; the def is the game's server data) but the outcome is total. Code read (D) + GroupService.yaml:327-341 (non-member: IsMember false, Roles empty; Rank 0-255)", smallest_fix: "start: problem() unless minRank >= 1 (one condition on :473)", protect: "group-throw fail-closed (Ad-T2)", retest: "Ad-T9 case 'group minRank 0': start errors"}
  - {id: N1, class: recommendation, where: "vendor/ProfileStore/PATCHES.md (Source and P-1 rows); .gitattributes", expected: "the recorded hashes can be re-checked after commit", observed: "both the GWS source and init.luau are CRLF on disk (2242 CRLF each); PATCHES.md says 'LF'. .gitattributes is '* text=auto eol=lf', so after the first commit the checked-out file is LF and neither sha256 (799263dc, cfda9e90) matches any more", evidence: "records only, no runtime effect; no tool checks these hashes (grep tools, .github: 0 hits). python byte count (D)", smallest_fix: "record the LF-normalised hashes (or say 'CRLF bytes as copied') in PATCHES.md and evidence/Session.md", retest: "sha256 of the committed file equals the row"}
keep:
  - "Ad2 first line of the handler (init.luau:158): no read, no allocation, sampled warn, counted; Planted 'remove the caller check' red"
  - "Ad3 two locks: server IsStudio check before the action lookup (:162) + Session studio* refuse; client hides Studio rows (Panel:378)"
  - "Ad1 fail-closed: pcall group read, Studio-only -1 and user-owned-creator rules, Player2 not admin; decided once, re-checked after the yield (:329)"
  - "Ad6: panel, pages, frames and the transport link cloned only after admins[player] is re-read after WaitForChild (:297); pages/frames placement checked at start (:476-479); everything else stays in ServerScriptService"
  - "Ad4 snap-down then clamp (:131-132), finite checks on slider/number, UTF-8 + byte cap on text, integer target ids (:168)"
  - "Ad7 two-way control/action check incl. a game action shadowing a built-in (:443-453); start errors before any connection (no half state)"
  - "fly/noclip: self-only built-ins; attributes and flags are server facts cleared on respawn/leave; the client restores CanCollide, destroys its constraints and PlatformStand on stop and on CharacterRemoving"
  - "Panel PT-01/PT-15: pending at press, reply reason at the row, stale reply dropped by generation + handle.alive(); toggle shows the server attribute"
  - "per-player state (joined, admins, exempt, infoAllowance, sampler) all released in onLeave; 1,000-cycle spec"
  - "fit(): the 65,535-byte cut never splits a UTF-8 sequence"
weakest_part: "every Ad6 and fly/noclip claim is a code read plus the Lune fake; no engine run of the cloned client (see could_not_check)"
could_not_check:
  - {step: "Ad-T8/Ad-T12/Ad-T16 in the engine: a non-admin client has no panel; the cloned client runs (Script RunContext Client under the template's emitLegacyScripts=false vs LocalScript in test.project.json) and its @self/./ requires resolve; built-ins with 2 clients; boot in a Server Authority place", missing_input: "Admin.engine.spec run (S)", closes_it: "step 8 Studio multi-client proof", who: "studio-operator"}
  - {step: "Ad6 in a real game", missing_input: "the template's project file does not map Admin yet (ADMIN-PENDING); Ad6 holds only if Admin sits in ServerScriptService", closes_it: "step 7 template wiring + a grep that Admin is not under ReplicatedStorage", who: "lead / template builder"}
  - {step: "floods before Admin", missing_input: "Net per-event bound for batched packets (tests/acceptance/Net Flood F3-F5 red today)", closes_it: "Net repair green", who: "Net builder"}
  - {step: "Studio target ids", missing_input: "CC-17 is not in src/Net/framework.blink:32 (target still f64(1..9007199254740991)?): in Studio the admin (-1) cannot target Player2 (-2); the call fails at decode (fails closed)", closes_it: "CC-17 applied in the Net repair", who: "Net builder"}
  - {step: "core.info size at peak", missing_input: "measured 7.6 KB at 50 players vs CC-18 8 KB; grows ~40 B per player past that", closes_it: "a 100-player measurement or a capped player list", who: "performance-engineer (PROPOSAL budget)"}
  - {step: "fly/noclip feel and the game's movement checks", missing_input: "no game consumes isExempt yet", closes_it: "first game's movement check + Studio run", who: "owner at G3"}
verdict: ready for the next review
</spec>
```

## Over-building (Q1, rules/anti-overengineering.md)

**Concrete cuts: none.** The 1,515 lines map to contract rows, not to extras; the proposal's 400-600 estimate predates contract r2 (15 built-ins, client fly/noclip, info push, save view, Ad7 validation, 5 control kinds).

| Part | Lines | Contract rows it carries | One-user or past the contract? |
| --- | --- | --- | --- |
| init.luau types, constants, state | 1-98 | API, Ad8 ring, rate PROPOSAL | no |
| refusals, accept, handle | 100-184 | Ad2-Ad5, Ad8, README rule 6 (sampled lines) | no |
| exemption, info, sampler | 186-251 | Ad9, core.info, budget row | no |
| admin decision | 253-292 | Ad1 (GetRolesInGroupAsync per CC-19) | no |
| panel copy, join, leave | 294-352 | Ad6, lifecycle | no |
| def validation | 354-455 | Ad7 (18 spec cases) | no |
| start, API, spec hook | 457-546 | API, lifecycle | `_debugCounts` is the Q5 spec hook |
| Builtins.luau | 261 | the 15-row built-in table | `_fit`/`_assignment` exports: 2 lines, spec-only |
| Client/Core.luau | 79 | one source for page data (server checks + client draw) | no |
| Client/init.client.luau | 230 | transport link (CC-16), Screens ids, info/save output, fly/noclip (~80 lines) | no |
| Client/Panel.luau | 399 | target picker, tabs, 5 control kinds, pending/reply per row (PT-01, PT-15), frame pages | slider track click (:315-321, 7 lines) duplicates ± ; kept (normal slider use), not a cut |

`Def.client` (one field beyond the frozen contract) is CC-16, lead-fixed: not a finding.

## Harm areas walked (A)

| Area | Result |
| --- | --- |
| 1 saved data | Admin writes only via studio* in Studio (Ad10); saveView reads a frozen copy: clean |
| 2 permission | Ad1-Ad6 hold by code read + planted faults; R1, R2 |
| 3 policy, safety | kick text fixed; no admin text reaches other players through built-ins; saveView admin-only: clean |
| 4 leaks, yields | per-player and per-open state released; re-checks after both yields (decide, WaitForChild): clean |
| 5 performance | Lune Q6 under budget; info size at >50 players: could-not-check |
| 6 structure | Net.answer, RateLimit, Screens, Janitor reused; no second way: clean |
| 7 APIs | all verified, no deprecated call |
| 8 over-building | none (table above) |
