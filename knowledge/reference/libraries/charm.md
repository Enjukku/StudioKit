---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
roles: [feature-builder, reviewer, architect]
---
> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24

# Charm (state atoms): package record

| Field | Value |
| --- | --- |
| Package | Charm by littensy (`littensy/charm`) |
| Version | **0.11.1** (Wally; newest index entry 2026-10-01); repo push 2026-10-01, updated 2026-10-23; checked 2026-10-24 (`research/state-ui-animation.md`, framework `CHANGELOG.md`) |
| Licence | MIT (`Packages/_Index/littensy_charm@0.11.1/charm/LICENSE`) |
| Where pinned | framework `wally.toml` `Charm = "littensy/charm@0.11.1"`; `wally.lock`; games through the template's `wally.toml`, at `ReplicatedStorage.Packages` |
| Used by | State (server truth and client copies), Screens (`view()` getter), Session (`selector` atom); the game's `Atoms` module and UI read atoms |
| Pairs with | charm-sync 0.4.1 (needs charm >= 0.11.0, < 0.12.0): pin the two together (`charm-sync.md`) |

## Why chosen
- The only candidate with atoms **and** a server-to-client delta sync in one maintained MIT repo; small (core `init.luau` 28.6 KB + `system.luau` 5.2 KB); reactive getters let UI and `track` views follow data without hand-written change events.
- Earlier games already ran Charm 0.10.0. Rodux and Reflex were rejected (reducer boilerplate, no replication, TS-first); Fusion and Vide state are tied to a UI library (Vide is closed door CD-4).

## Known gaps and how the framework covers them

| Gap | Covered by |
| --- | --- |
| 0.10 → 0.11 is breaking (`peek()` → `untracked()`; `atom()` second argument is an equality function; `computed()` lost its second argument; effect callbacks changed) | the framework is written for 0.11; old games moving to the framework port their atom code once |
| No file-level `--!strict` assurance in the package | framework blocks are `--!strict` and type their public API without `:: any` (Q-bar) |
| In-place mutation of an atom value is legal Lua | atoms get new tables only (State St5); Charm freezes values in Studio, and St-T5 checks the error |
| Listener order is not a contract | no block relies on it (`contracts/README.md` rule 4) |
| Lune has no `RunService.Heartbeat` | the Lune resolver gives package files a load-time `game` stub; specs call charm-sync `flush()` (`REQUIRES.md` Consequences) |

## Update path
Read the release notes for breaking changes; move Charm and charm-sync together inside the charm-sync range; run State, Screens and Session specs plus `St-T2` (privacy); new framework tag. Replacement cost: State, Screens, Session `selector`, and each game's `Atoms` module and UI getters.
