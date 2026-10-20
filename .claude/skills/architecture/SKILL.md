---
name: architecture
description: Design how a Roblox game's code fits together so new content is easy to add and changes stay safe - invariants, one owner per fact, simulation vs presentation, requests vs results vs events, definitions vs runtime vs saved state, module contracts, lifecycles and cleanup, dependency direction, client/server/shared placement, content as data, genre pressures, refactoring without rewrites. Use when planning a new system or feature, when one change needs edits in many files, when bugs come from timing, duplicates or leaks, or before a refactor. Pairs with `code-review` (checking) and the anti-over-engineering rules (keeping it small).
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 6. Evidence: owner research papers (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-01..A-23, `roblox-operations-2026-10.md`), checked against the Roblox docs mirror; Roblox-specific claims cite the mirror.

# Architecture: make every change understandable before it ships

## 1. When this skill starts
A new system or feature (M or L job), a refactor, or a report that a "small" change touched many files or caused duplicates, leaks or timing bugs. For S work, keep to the existing structure and skip to §6.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Invariant card, module contract block, feature plan, Roblox layout | `references/module-contract.md` |
| The principles with their evidence | `knowledge/reference/architecture/strong-codebases-2026-10.md` |
| Testing, releases, rollback | `knowledge/reference/architecture/roblox-operations-2026-10.md`; `code-review` skill |
| Remotes, saves, performance, UI specifics | `networking-security`, `data-saving`, `performance`, `ui-basics` skills |

## 3. Steps
1. **Write the invariants** (rules that must always hold) as cards: owner, inputs, clock, failure response, test.
2. **Name one owner per fact** and how others request changes.
3. **Fill the feature plan** (`references/module-contract.md`): messages, data split, placement, lifetimes, failure paths, tests.
4. **Run the locality check:** list each file the feature changes and why. A content item that changes saves, many remotes or unrelated UI means a boundary is wrong; fix the boundary first, or record why not.
5. **Put the contract block** at the top of each new or changed important module.
6. **Hand to `code-review`** with the plan, so the reviewer checks against intent, not just the diff.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| R-01 | **Invariants first, classes later.** "Combat is server-side" is too vague; "the server weapon checks ammo and cooldown before accepting a shot, and a rejected shot changes nothing" can be built and tested. **Timed multi-step actions** (bursts, combos, channels, crafting timers) need four more invariants: what each step consumes; what cancels the action (death, unequip, leave); that no new trigger starts while one runs; and the late-step policy (skip, run now, or catch up within a limit) | A-01 |
| R-02 | **One writer per fact.** A character's combat state, an inventory, a match phase, a save record each has one owner module; others request through its functions. A client copy of a value is not ownership; shared code is not trusted code | A-02 |
| R-03 | **Capability review:** list what each object *can* do, especially reused or inherited ones, not only what we intend | A-03 |
| R-04 | **Name the clock** for every timed rule (server `time()`, round time, save time); a tween or animation finishing never decides gameplay; client timestamps are claims | A-04 |
| R-05 | **Simulation vs presentation.** Server rules produce results with an id; the client renders them (effects, sound, UI) and may predict, then reconciles. Rules testable without a camera, rig or effects | A-05; `networking-security` N-03 |
| R-06 | **Requests vs results vs events.** `requestFire` asks; `ShotResolved` reports; events are only for independent reactions (sound, analytics, UI refresh), never hidden vetoes. Things that must succeed or fail together are direct calls. **Rewards are award requests with an id**, sent to the data layer, which applies each id once (`data-saving` D-11); the feature never changes currency directly | A-05 |
| R-07 | **Definitions vs runtime vs saved.** Definitions (data tables: id, stats, asset ids) are read-only; runtime instances hold per-player state; saves hold stable ids and durable values, never object graphs. Data picks among supported behaviours; it never becomes a second programming language | A-05, A-06 |
| R-08 | **Dependencies point one way:** entry scripts → feature owners → pure rules → small adapters (clock, random, storage, transport, spatial queries). Pure rules never fetch UI, saves or global services. A require cycle means a missing owner or a merge, not a lazy require | A-07 |
| R-09 | **A boundary must earn its place** (an invariant, a test seam, a swap point or its own lifetime). No god "GameService"; no layers of forwarding modules; wrap only what is nondeterministic, slow, failing or likely to change | A-05, A-08 |
| R-10 | **Contracts beat file names.** Every important module states what it owns, its requests, promises, failures, needs and lifetime, plus whether calls yield and whether returned tables are copies | A-09 |
| R-11 | **Lifecycles are gameplay.** `init` (no yields) → `start` → `destroy`. Every connection, task and temporary instance has a lifetime owner (server, session, character, match). After any yield, re-check a session or generation token before acting. Cleanup is safe twice. Test repeated respawn, round reset and screen open/close | A-10; Roblox Plant reference project (`resources/plant-reference-project.md`) |
| R-12 | **Placement is security and download size.** Server-only rules in ServerScriptService or ServerStorage; shared code only when the client needs it; nothing secret in shared code | `networking-security` N-05; `performance` F-06 |
| R-13 | **Results have three outcomes:** done, denied (do not retry), temporarily unavailable (may retry). Types state the contract; runtime checks at the boundary turn untrusted input into validated values | A-13 |
| R-14 | **Streamed objects are temporary views.** Controllers attach when a model streams in and detach when it leaves; waits have timeouts; the server never assumes a client has a model loaded | A-16; `workspace/streaming/` |
| R-15 | **Plain modules first.** Modules with composition are the default; an entity-component system only for large, regular workloads, after benchmarking a real slice; never two writable copies of one fact | A-11 |
| R-16 | **Genre pressure decides the hard parts:** shooters → time and trust (history window, stale-claim policy, Server Authority option); ability games → one execution model (eligible → target → reserve → commit → effect → done or cancel) and a documented modifier order; sandboxes and tycoons → durable ids, offline-progress rules, crafting and trading as transactions | A-12 |
| R-17 | **Content vs mechanic.** A new item using existing behaviour is data plus tests. A new mechanic gets a design review and may extend the interfaces; do not force it into the first interface | A-18 |
| R-18 | **Refactor without rewrites:** pick one painful change; write its contract and tests; put an adapter in front of the old code; build the new path behind a switch; move a small slice; retire the old path on purpose. A switch is not a rollback when saved data changed | A-22; `data-saving` D-15 |

## 5. Rules (final check)
- No feature plan without its invariants and owners.
- No second writer for a fact; no gameplay decision in presentation code.
- No require cycles; no lookup of modules by name at runtime.
- No connection, task or temporary instance without a lifetime owner.
- No new framework or abstraction layer unless it removes a concrete risk now (`rules/packages.md`).

## 6. Self-check before returning
- [ ] Invariant cards exist for each rule the feature must keep, each with a test.
- [ ] Locality check written; each changed file justified.
- [ ] Contract blocks on new or changed important modules.
- [ ] Failure paths covered: denied, unavailable, leave mid-action, respawn, streamed out.
- [ ] Repeated lifecycle test planned (respawn, reset, reopen ×20).

Project overlay: if `knowledge/overlays/architecture.md` exists, read it after this file; it wins for this game.
