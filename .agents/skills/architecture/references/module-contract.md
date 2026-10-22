> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Templates for `architecture`. Source: owner research paper (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-01, A-09, A-10, A-18). Revised by J018 maker architect · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (plan header with the game parameters, feature plan items 10-12, design budget, builder brief interface rows, presentation and pipeline rows in the Roblox layout; repair round 1 after the stage 3 review: triangle row, isolation proof, losers' reopen evidence; repair round 2: test hooks and settings point to the builder's one list).

# Templates

## Invariant card (one per rule that must always hold)
| Field | Example |
| --- | --- |
| Rule | A reward is granted once per quest completion, even if the request is retried |
| Owner | QuestService (server) |
| Inputs | player session, quest id, completion id |
| Clock | server `time()` at acceptance |
| On failure | denied (already granted) or unavailable (save not ready); no partial grant |
| Test | replay the same completion id twice; save failure between check and grant |

## Module contract (top of every important module, as a comment block)
```lua
--[[
Owns:        <the facts only this module may change>
Requests:    <public functions callers may use; which ones yield>
Promises:    <what is true after success>
Fails:       <how it rejects: denied / unavailable / error; what stays unchanged>
Needs:       <modules and services it depends on>
Lifetime:    <server | session | character | match>; how it stops (Destroy, cleanup)
Notes:       <re-entrant? returns copies or internal tables?>
]]
```

## Feature plan (before code, for M and L work)
Plan header (above item 1): the problem in one line; the target-experience line quoted from the brief; the game parameters from `knowledge/design/game-profile.md` (camera, device mix, players per server, input, session shape, streaming); the genre pressure (`SKILL.md` R-16); the inputs used, each with its revision (feature spec, timing list, read card, cue table, motion table).
1. Player-facing goal (one sentence) and the invariants (cards above).
2. Owners: which module owns each new or changed fact; who may request changes.
3. Messages: client requests (intent names), server results (with request id, outcome, tier, reason code, cause), events for independent reactions.
4. Data: definitions (content tables), runtime state, saved state (and schema change, if any).
5. Placement: server-only, client-only or shared; download size of shared parts.
6. Lifetimes: what is created, who cleans it up, what happens on respawn, leave and round reset. Characters and creatures: the animation states, transitions and interruption rules are fixed with the animator and the builder before keying, with one owner of the animation state machine and a cleanup event on every interruption.
7. Failure paths: denied, unavailable, save failure, player leaves mid-action, object streamed out, late or lost confirmation.
8. Tests: unit (pure rules), server (Luau Execution or Studio), multi-client cases, negative cases.
9. Locality check: list every file the feature changes and why each must change; content kept apart by data, with its spy or golden test (`SKILL.md` §3 step 9).
10. Presentation contract: one row per player-visible event (`presentation-contract.md`), or "n/a: nothing player-visible".
11. Design budget at the worst case (the table below).
12. Options: only for consequential choices: the 2-3 options, the pick and why each other option lost, and for each loser the evidence that would reopen it (the lead files it as a closed door when a gate drops it).

## Design budget (worst case, in the plan)
Each row: the number, its unit, its source (measured with the recipe, `performance/references/budgets.md`, a craft's budget block, or PROPOSAL with the test that will settle it). An engine limit is a ceiling to stay well under, never the budget.
| Row | Worst case to state | Where the number comes from |
| --- | --- | --- |
| Players and rate | players per server × events per second per player at the busiest moment | game profile; feature spec frequency field |
| Server work | handlers per second, simulation steps, Server Authority cost if used | measured on a spike; `networking-security` N-09 |
| Remotes | messages per second per client per remote, payload bytes | `networking-security` N-06 (about 500 requests per second per client per remote type is a ceiling) |
| Effects on one client | live effects, emitters and particles at peak, live copies per frequent effect | the VFX read card and `spec.json` budget block; ceilings: particle Rate 400 per second per emitter, 100 on mobile (`effects/particle-emitters.md:212`); Highlight 255 per client, extras silently ignored (`effects/highlighting.md:37`) |
| Sounds on one client | voices at peak, cue rate after merging | the sound designer's mix plan (voice cap, pooling) |
| Instances and join size | replicated instances, ReplicatedStorage bytes, streamed model groups | `performance` F-04, F-06 |
| Triangles on one client at peak | asset classes × live copies × triangles per mesh (pets, crowds, debris, spawned props) | the modeler's per-asset budget (`modeling-design` M-13); `performance` F-01 (no published triangle budget: measure the baseline device); 20,000 per mesh is the upload limit (`art/modeling/specifications.md:34`), a ceiling, never the budget |
| Texture memory | textures per asset class × size; a 1024² texture costs four times a 512² one | `performance` F-03 (textures ≤ 512² by default); `performance-optimization/improve.md:567` |
| Frame time | the target on the baseline device | `performance` F-01, F-02 |
| Expensive features | each per-frame loop, physics simulation, large instance count, new remote or new driven joint chain, with the reason it earns its cost | the plan; cut or simplified when the reason is weak |

## Builder brief interface rows (`fixed.interface` of the build ticket)
The build ticket format is `engineering-craft/references/handoffs.md` §1; these rows fill its `interface` key so the builder, the crafts and the qa-lead read one contract. One row per item; names from `knowledge/design/vocabulary.md`.
| Row | Holds | Example (melee hit) |
| --- | --- | --- |
| Exposes | public functions with yields and outcomes | `CombatService.requestSwing(player, swingId): ("done" \| "denied" \| "unavailable", reason?)` |
| Remote | name, direction, payload, rate limit, channel | `Combat.Swing` client → server `{swingId, aimDir}`, 6 per second |
| Result event | name, who receives it, payload fields | `Combat.HitResolved` to all clients in range `{requestId, attacker, target, outcome, tier, cause, position}` |
| Consumes | data files by path and owner; events by id | `content/combat/weapons` (game-designer values, feature-builder file); timing list `timing-swing.json` rev 3 |
| Presentation wired | the contract rows this builder wires; the one client module that owns caps and pools | rows P-1..P-6; `MeleePresenter` (client) |
| Settings read | the local comfort service and which settings | the comfort module's `reducedMotion()`, `shakeScale()`, `reduceFlashes()`, `clarity()` (`engineering-craft/references/presentation.md` §6) |
| Lifetime | the owner that cleans up | character lifetime; cleanup on unequip, death, leave |
| Test hooks | the hooks and debug log lines the presentation seeds need, by their names in `engineering-craft/references/presentation.md` §9 (that list is the only one) | this feature's seeds pick `Reject`, `DelayMs`, `Viewer`, `Reduced`, `Clarity`, `FxLog` |

## Roblox layout (default; a game may differ, recorded in its overlay)
| Place | Holds |
| --- | --- |
| `ServerScriptService` | one server entry Script (`RunContext = Server`) that starts services in an explicit order; server-only services and rules |
| `ServerStorage` | server-only content (future levels, templates, secrets-free config) |
| `ReplicatedStorage` | shared modules the client needs: message names and types, definitions safe to show, pure calculations, packages |
| Client entry | one `Script` with `RunContext = Client` in ReplicatedStorage (Roblox's recommendation, `scripting/locations.md:36-40`) or one LocalScript in StarterPlayerScripts; it starts controllers in order |
| `ReplicatedFirst` | only the loading screen |
| Content source (files) | definitions and tuning as data, compiled or required by the owners |
| Presentation data (files) | effect specs `content/vfx/<effect-id>/spec.json` (vfx-designer); the cue table, cue id → asset id (sound-designer); the UI motion table `content/ui/_system/motion-table.md` (ui-ux-designer); timing lists `content/anim/<asset-id>/timing-<action-id>.json` (animator); comfort defaults (architect names the file, ui-ux-designer designs the screen). Code reads them by id |
| Client presentation | one presenter per feature under the client entry: it listens to the feature's result events and markers, draws per viewer, reads the comfort service, and owns the caps and pools of its frequent effects |
| Audio buses | one bus per category the sound designer's mix plan names (for example ui, sfx, foley, ambience, music) |
| Studio containers | one folder or model per discipline and area (for example Blockout, Lighting, Art_SiteB, Effects), each with one owner in the job card at a time |
| Kits | reusable pieces as Packages, so a placeholder updates everywhere when the detailed version is published (`projects/assets/packages.md:14, 19`) |
| Names and folders | the game's naming and folder rules are written in its overlay before production; a tool enforces and renames, not hand edits |
Lifecycle per service or controller: `init()` (build state, no yields, no other module's work) → `start()` (connect events, begin loops) → `destroy()` (cleanup, safe to call twice).
