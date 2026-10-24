---
name: architecture
description: Design how a Roblox game's code fits together so new content is easy to add - one owner per fact, server results and the presentation contract VFX, sound, UI and animation key from, contracts, lifecycles, placement, content as data, safe refactors. Use when planning a system or feature, when a change needs edits in many files, when bugs come from timing, duplicates or leaks, or before a refactor.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J001 step 6. Evidence: owner research papers (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-01..A-23, `roblox-operations-2026-10.md`), checked against the Roblox docs mirror; Roblox-specific claims cite the mirror. Rebuilt by J018 maker architect · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (parameters first, spike, presentation contract, worst-case budget, self-review, §7 core principles; repair rounds 1 and 2 after the stage 3 reviews). PROPOSAL numbers are starting values a check may change.

# Architecture: make every change understandable before it ships

## 1. When this skill starts
A new system or feature (M or L job), a refactor, or a report that a "small" change touched many files or caused duplicates, leaks or timing bugs. For S work, keep to the existing structure and skip to §6.
Anything the player sees or hears react to (a hit, a pickup, a purchase, a hazard, a refusal) also gets a **presentation contract** (§3 step 7): the written hand-over from gameplay to animation, VFX, sound and UI ("it feels laggy", "it showed a hit that missed" and "the sound is late" start where it was never written).
**After a context compaction,** re-read §3, §5, §6 and §7 before you hand anything on: only the start of a skill survives compaction.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Invariant card, module contract block, feature plan, design budget, builder brief interface rows, Roblox layout | `references/module-contract.md` |
| The presentation contract: what it reads from each craft, event rows, comfort service, engine facts and probes, check seeds | `references/presentation-contract.md` |
| Worked examples: melee hit, coin pickup at 20 per second, boss slam, shop refusal | `references/worked-examples.md` |
| Reviewing a builder's proof, wiring or a craft's plan for cost and contract | `references/review-checklist.md` |
| The principles with their evidence | `knowledge/reference/architecture/strong-codebases-2026-10.md` |
| Testing, releases, rollback | `knowledge/reference/architecture/roblox-operations-2026-10.md`; `code-review` and `testing` skills |
| Remotes, saves, performance budgets, UI build | `networking-security`, `data-saving`, `performance`, `ui-basics` skills |

## 3. Steps
1. **Restate the problem with the game's parameters.** One line of problem; the target-experience line quoted word for word from the brief; the parameters from the game profile: camera, device mix (phone first), players per server, input, session shape, streaming; the genre pressure (R-16). *Check: AR-01.*
2. **Write the invariants** (rules that must always hold) as cards: owner, inputs, clock, failure response, test. *Check: AR-02.*
3. **Name one owner per fact** and how others request changes; one owner per code file, data file and Studio container; every shared list or registry has one owner or is derived from one source. *Check: AR-03.*
4. **Options only for consequential choices** (authority model, replication, data shape, engine feature vs custom, a framework): 2-3 designs at equal depth, one non-obvious, scored against the invariants and budget; pick with the reason; each loser is listed in the decision record with the evidence that would reopen it (the lead files it as a closed door when a gate drops it). *Check: AR-04.*
5. **Spike the risky claim first:** the claim the design rests on (feasible at a full server on the baseline phone; engine behaviour the docs do not state) gets a Studio probe or a minimal greybox measurement before the full plan. A desk estimate never rejects an engine feature. *Check: AR-05.*
6. **Fill the feature plan** (`references/module-contract.md`): messages, data split, placement, lifetimes, failure paths, tests.
7. **Write the presentation contract** (`references/presentation-contract.md`): one row per player-visible event the feature spec's feedback stack and the timing list draft imply, filled in its §3 order (the crafts are asked first). *Check: AR-06 to AR-14.*
8. **Set the design budget at the worst case:** players per server × events per second × layers on the baseline device (`references/module-contract.md` Design budget), each number with its source; presentation numbers come from the VFX and sound budget blocks; engine ceilings are not budgets. *Check: AR-15.*
9. **Run the locality check:** list each file the feature changes and why. A content item that changes saves, many remotes or unrelated UI means a boundary is wrong; fix the boundary first, or record why not. Content the feature must not touch is kept apart by data (a field in its definition, not a code branch per item) and proved by a spy test (the feature's code runs 0 times for it) or a golden test (its results do not change). *Check: AR-03.*
10. **Write the builder briefs:** the target-experience line quoted, interface rows (what each builder exposes and consumes; `references/module-contract.md`, "Builder brief interface rows"), the contract block each important module carries, the effort (high for money, saves, remotes); seed the qa-lead's trace table with invariants, failure paths and presentation check seeds. *Check: AR-16 to AR-19.*
11. **Self-review (§6), then hand to `code-review`** with the plan, so the reviewer checks against intent, not just the diff. Stop when every invariant, player-visible event, number and file has its owner and check: the plan is as long as the builder needs. A row or budget line that does not apply is one n/a line with the reason. *Check: AR-20, AR-21.*

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| R-01 | **Invariants first, classes later.** "Combat is server-side" is too vague; "the server weapon checks ammo and cooldown before accepting a shot, and a rejected shot changes nothing" can be built and tested. **Timed multi-step actions** (bursts, combos, channels, crafting timers) need four more invariants: what each step consumes; what cancels the action (death, unequip, leave); that no new trigger starts while one runs; and the late-step policy (skip, run now, or catch up within a limit) | A-01 |
| R-02 | **One writer per fact.** A character's combat state, an inventory, a match phase, a save record each has one owner module; others request through its functions. A client copy of a value is not ownership; shared code is not trusted code | A-02 |
| R-03 | **Capability review:** list what each object *can* do, especially reused or inherited ones, not only what we intend | A-03 |
| R-04 | **Name the clock** for every timed rule (server `time()`, round time, save time); a tween or animation finishing never decides gameplay; client timestamps are claims | A-04 |
| R-05 | **Simulation vs presentation.** Server rules produce results with an id; the client renders them (animation, effects, sound, UI) and may predict only through a predicted row in the contract (R-19), then reconciles. Rules testable without a camera, rig or effects. Presentation never decides gameplay: a marker, tween end or effect never deals damage, grants or moves a hit area (what plays when: R-19) | A-05; `networking-security` N-03 |
| R-06 | **Requests vs results vs events.** `requestFire` asks; `ShotResolved` reports; events are only for independent reactions (sound, analytics, UI refresh), never hidden vetoes. Things that must succeed or fail together are direct calls. **A result carries** the request id, the outcome (done with its tier, denied with a reason code, unavailable) and the cause the tier is graded by; a client prediction never becomes a confirmed outcome. **Rewards are award requests with an id**, sent to the data layer, which applies each id once (`data-saving` D-11); the feature never changes currency directly | A-05 |
| R-07 | **Definitions vs runtime vs saved.** Definitions (data tables: id, stats, asset ids) are read-only; runtime instances hold per-player state; saves hold stable ids and durable values, never object graphs. Data picks among supported behaviours; it never becomes a second programming language. **Presentation is content too:** the cue table, effect specs, the UI motion table, timelines in seconds, comfort defaults and rule sets (material by slope, spawn tables) are data files with one owner each, read by id; no asset id or timing in logic | A-05, A-06 |
| R-08 | **Dependencies point one way:** entry scripts → feature owners → pure rules → small adapters (clock, random, storage, transport, spatial queries). Pure rules never fetch UI, saves or global services. A require cycle means a missing owner or a merge, not a lazy require | A-07 |
| R-09 | **A boundary must earn its place** (an invariant, a test seam, a swap point or its own lifetime). No god "GameService"; no layers of forwarding modules; wrap only what is nondeterministic, slow, failing or likely to change | A-05, A-08 |
| R-10 | **Contracts beat file names.** Every important module states what it owns, its requests, promises, failures, needs and lifetime, plus whether calls yield and whether returned tables are copies | A-09 |
| R-11 | **Lifecycles are gameplay.** `init` (no yields) → `start` → `destroy`. Every connection, task and temporary instance has a lifetime owner (server, session, character, match). After any yield, re-check a session or generation token before acting. Cleanup is safe twice; an interrupted action fires its cleanup event (trails, loops, grip overrides). Test repeated respawn, round reset and screen open/close | A-10; Roblox Plant reference project (`resources/plant-reference-project.md`) |
| R-12 | **Placement is security and download size.** Server-only rules in ServerScriptService or ServerStorage; shared code only when the client needs it; nothing secret in shared code | `networking-security` N-05; `performance` F-06 |
| R-13 | **Results have three outcomes:** done, denied (do not retry), temporarily unavailable (may retry). Types state the contract; runtime checks at the boundary turn untrusted input into validated values. **A denial carries a reason code** the UI turns into the cause and the fix at the control ("need 40 more gold"); never silence, never colour alone | A-13; `networking-security` N-14 |
| R-14 | **Streamed objects are temporary views.** Controllers attach when a model streams in and detach when it leaves; waits have timeouts; the server never assumes a client has a model loaded | A-16; `workspace/streaming/` |
| R-15 | **Plain modules first.** Modules with composition are the default; an entity-component system only for large, regular workloads, after benchmarking a real slice; never two writable copies of one fact | A-11 |
| R-16 | **Genre pressure decides the hard parts:** shooters → time and trust (history window, stale-claim policy, Server Authority option); ability games → one execution model (eligible → target → reserve → commit → effect → done or cancel) and a documented modifier order; sandboxes and tycoons → durable ids, offline-progress rules, crafting and trading as transactions | A-12 |
| R-17 | **Content vs mechanic.** A new item using existing behaviour is data plus tests. A new mechanic gets a design review and may extend the interfaces; do not force it into the first interface | A-18 |
| R-18 | **Refactor without rewrites:** pick one painful change; write its contract and tests; put an adapter in front of the old code; build the new path behind a switch; move a small slice; retire the old path on purpose. A switch is not a rollback when saved data changed | A-22; `data-saving` D-15 |
| R-19 | **One presentation contract per player-visible action:** the attempt cue on the client at the input; the outcome layer only on the server-confirmed result, sized by its tier (a predicted row only where the spec allows it: `references/presentation-contract.md` §2 Layer); pending when slow; nothing of the outcome for a rejected request. Picture and sound start from one client event, timed by marker names and timing-list ids | `references/presentation-contract.md` §2-§3 |
| R-20 | **Per viewer:** the server sends facts (actor, target, outcome, tier, position), never a picture; each client draws for its relation (self, ally, bystander, threatened). Camera and screen channels only for the local player's own top-tier events; hit-stop runs on the attacker's and the target's clients (the per-viewer column says whether bystanders see it), never on the server | `references/presentation-contract.md` §2, §5 |
| R-21 | **One truth source for what presentation shows:** areas, fuses, radii, cooldowns, balances and the player's effective odds (modifiers and once-only wins included) come from the same data field or function the server rule uses. Countdowns follow the server timer; a threat's tell is sent at wind-up start with the server time it resolves, never together with the damage; logic uses the true balance at once. Randomness only on decoration, through the random adapter | R-07, R-08; `platform-policy` (odds) |
| R-22 | **Comfort is one local, read-only client service** (`GuiService.ReducedMotionEnabled` plus the game's settings): it changes only the local screen, never gameplay; every reduced variant keeps the information | `references/presentation-contract.md` §4 |
| R-23 | **Information survives every tier:** no gameplay fact on one channel, or on one a setting, quality level or device removes; decoration is dropped first under load | `references/presentation-contract.md` §5 |
| R-24 | **Frequent events are built for their rate:** merged per window into one burst, one sound, one label; pooled and capped by one presenter, never by each caller | `references/presentation-contract.md` §2 Rate |
| R-25 | **Build for the next craft and the pipeline:** names and folders fixed before production; kits as Packages; a manual step done a third time becomes a tool ticket; an expensive runtime feature carries the reason it earns its cost; "make it cooler" after the plan is a ticket with its cost | `references/module-contract.md` (Roblox layout, Design budget) |

## 5. Rules (final check)
- No feature plan without its invariants and owners.
- No second writer for a fact; no gameplay decision in presentation code.
- No require cycles; no lookup of modules by name at runtime.
- No connection, task or temporary instance without a lifetime owner.
- No new framework or abstraction layer unless it removes a concrete risk now (`rules/packages.md`).
- No outcome layer before the server confirms, except a predicted row the spec allows; no camera, flash or tint from another player's event; no server pause for hit-stop.
- No asset id, cue time or tuning number in logic; no second copy of a truth value; no gameplay fact on one channel.

## 6. Self-check before returning
Inputs: the decision record, briefs and probe outputs of this task, and the partner documents at the revisions you name. Mark each line PASS, FAIL, n/a (why) or not verified. Reviewing someone else's proof: `references/review-checklist.md`.
**Plan**
- [ ] AR-01 Header: problem, quoted target-experience line, every game parameter of step 1, genre pressure; a gap names its owner and a PROPOSAL. *(header vs `game-profile.md`)*
- [ ] AR-02 Every rule has a card with owner, clock, failure response, test; timed multi-step actions have the four extra invariants. *(cards)*
- [ ] AR-03 One owner per fact, code file, data file, Studio container; a reason per changed file; no content item reaches saves, many remotes or unrelated UI; content kept apart has its spy or golden test in the seeds. *(owns table, locality list)*
- [ ] AR-04 Each consequential choice: 2-3 options at equal depth, one non-obvious, the pick and why the others lost, each loser with the evidence that would reopen it; small choices: none. *(decision record)*
- [ ] AR-05 The risky claim cites a probe or measurement (path, label), or is not verified with the probe named; no engine feature rejected on a desk estimate. *(probe outputs)*
**Presentation contract** ("n/a: nothing player-visible" only when true)
- [ ] AR-06 Count the feedback-stack actions, states, threats and hazards in the feature spec, then the rows: each has its layers (attempt, outcome per tier, failure, refusal, tell, end-of-state, cleanup). *(feature spec vs contract)*
- [ ] AR-07 Every attempt row starts from the input with no server wait; every outcome row from a server result id or replicated state, never a marker; a predicted row only as the contract's Layer rule allows (spec allows it; removed on denial; never money, rewards, paid reveals); the rejected path (no outcome layer) and the slow path (pending) are written; a paid-random windup row reads only the request, the same for every outcome. *(rows)*
- [ ] AR-08 Every event id is in the vocabulary and, for motion, in the named timing-list revision; times referenced by id, never copied as numbers or frames. *(contract vs timing list)*
- [ ] AR-09 Multiplayer: per-viewer column filled; no camera, flash, tint or slow motion from another player's event; hit-stop only on the attacker's and target's clients unless the column says otherwise. *(per-viewer column)*
- [ ] AR-10 Every intense channel names its reduced variant and the information kept; the settings service is local and read-only. *(comfort column)*
- [ ] AR-11 Every drawn truth value names its one data field read by server and client; every countdown and tell carries the server time it resolves; every tell row's source is its own event sent when the wind-up starts, never the damage or outcome event; no random range on a meaningful value. *(source and truth columns; a contract read cannot see a tell event the code sends in the same step as the damage: that is `code-review` PT-05)*
- [ ] AR-12 Every event that can fire about once a second or more states rate, burst, merge window and the one owner of its cap and pool. *(rate column)*
- [ ] AR-13 Every gameplay fact names two or more channels, so that grayscale, sound off, reduced motion and the lowest graphics quality each still leave at least one. *(information column)*
- [ ] AR-14 Every presentation data table has a path and one owner; interfaces pass ids, never asset ids or timings. *(table list)*
**Budget, briefs, hand-back**
- [ ] AR-15 Every Design budget row at the worst case on the baseline device, each number with its source; each expensive feature with its reason; no engine ceiling used as a budget. *(budget table)*
- [ ] AR-16 Failure paths: denied with reason code, unavailable, leave mid-action, respawn, streamed out, late or lost confirmation, interruption with its cleanup event; characters and creatures: states, transitions and interruption rules agreed with animator and builder, one state-machine owner. *(failure list, plan item 6)*
- [ ] AR-17 Repeated lifecycle test planned (respawn, reset, reopen ×20; counts back to baseline). *(test seeds)*
- [ ] AR-18 QA seeds hold every presentation check seed the rows need (`references/presentation-contract.md` §6) and who captures each. *(trace seeds)*
- [ ] AR-19 Each brief quotes the target-experience line. Each builder brief: owned files, interface rows (exposes, consumes), the contract block each important module carries, invariants, failure checks, docs, effort (high for money, saves, remotes); each craft brief asks what the contract needs, and by when. *(briefs)*
- [ ] AR-20 Hand-back as short as the builder needs; a could-not-check list with the input that closes each; one honest weakness; each review note mapped to done or questioned, with the problem behind it. *(hand-back)*
- [ ] AR-21 Pipeline: the game's naming and folder rules are named, or proposed before production; every manual step the plan repeats per item (or a third time) has a script or a tool ticket; anything added after the plan's approval is a ticket with its cost. *(plan, tickets)*

Project overlay: if `knowledge/overlays/architecture.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's universal principles, stated for system design: the standard, an example from this craft, a check you can run, where the depth sits. Principles about pictures and sound themselves (what is read first by contrast, big before small in a picture, silhouette, pushing past real, the subject's character, one visual style) are the crafts'; my part of them is to keep their information alive in the system (rows 1, 7, 20).

| # | Principle, for my work | Example | Check | Where |
| --- | --- | --- | --- | --- |
| 1 | **The gameplay read comes first; the architecture never delays or hides it.** The attempt cue answers on the client at once; the outcome waits for the server (a predicted row only where the spec allows it); a threat's tell leaves the server when its wind-up starts, never with the damage, so the network delay does not eat the reaction window; nothing that carries a gameplay fact depends on a quality level or a setting. | A sword swing trail plays on the press; the hit spark waits for `HitResolved`; the slam's danger ring starts on `SlamWarned` at wind-up start, never on `SlamLanded`, and stays at every graphics quality. | AR-07, AR-11, AR-13; review RV-01, RV-04. | R-19, R-21, R-23 |
| 2 | **Judge it where players meet it:** the plan is sized for the baseline phone, a full server and streaming, never for Studio on a desktop. | 20 players each firing 3 effects a second on an entry-level Android phone, not one player in an empty test place. | AR-15 names device, players and rate; the proof's numbers come from that recipe (RV-03). | §3 step 8 |
| 6 | **Less is more:** the fewest modules, boundaries, remotes and layers that keep the invariants; every boundary earns its place. | One `PickupService` and one client presenter, not a pickup framework with a plugin registry. | Every boundary in the plan names its invariant, test seam, swap point or lifetime (R-09); the locality list is short. | R-09, R-25 |
| 7 | **One code for meaning across the game:** colour roles, shape codes, motion rows, cue ids and event names live as shared data with one owner; the same event name means one thing everywhere. | `contact_candidate` (the pose) and `contact_confirmed` (the server) are two events, never one "Hit". | AR-08, AR-14; review RV-05, RV-06. | R-07, R-19 |
| 8 | **Timing tells cause and effect:** one client event starts picture and sound; times come from markers and the timing list in seconds; the result plays after its cause. | The impact spark and the hit sound both fire from `contact_confirmed` on the client, not from two separate server messages. | AR-08; the code wires markers by name (RV-06). | R-19 |
| 12 | **Controlled variation, never repetition of meaning:** randomness only on decoration, through one random adapter; meaning is locked. | Pebble size varies ±15 %; the slam's radius, fuse and contact time never do. | AR-11. | R-21 |
| 13 | **Problem, constraints and target before the plan:** the parameters, the target-experience line and the behaviour contract come first. | "12 players, phones, third-person, 3-minute rounds" written before any module is named. | AR-01. | §3 step 1 |
| 14 | **Options, then a reasoned pick, where the choice is consequential:** 2-3 designs, one non-obvious, the pick tied to the invariants and budget. | Replicating crack state as a bitmask, as events, or as server-owned parts: the bitmask wins on join size. | AR-04. | §3 step 4 |
| 15 | **Cheap stages first; gates freeze decisions:** the behaviour contract and a spike before the full plan; after the plan is approved, interfaces move only by a recorded decision; a third patch on one symptom means redesign. | A 20-line probe proves marker signals fire on an observing client before the contract relies on them. | AR-05; losers with their reopen evidence (AR-04). | §3 step 5; R-18 |
| 16 | **Critique against the goal, one named problem at a time:** findings name the failure scenario, the evidence and the problem behind a requested fix. | "Delete the event bus" becomes "two writers change match phase"; the fix is one owner. | AR-20; review findings format (`references/review-checklist.md` §4). | role file |
| 17 | **Build for the next craft and for the engine:** ask each craft what it needs, give ids and data files, one owner per file, scripts for repeated steps, engine features first. | The VFX designer gets `SlamWarned` with radius and fuse keys; the effect reads them from `BossConfig`. | AR-14, AR-19, AR-21; RV-05. | R-07, R-25 |
| 18 | **Know when it is done:** the plan stops when every invariant, event, number and file has its owner and check; extra structure is a follow-up. | A 90-line plan for a pickup feature, not a 400-line framework document. | §3 step 11; AR-20. | §3 step 11 |
| 19 | **Feedback follows the real outcome:** the attempt cue at once; the outcome layer only on confirmation, sized by tier (or a predicted row the spec allows, gone the frame a denial arrives); rejected requests show no success; frequent events merged and capped. | A shop "Buy" press sinks at once; the coin burst plays on `PurchaseResolved{done}`; `denied{not_enough_gold}` shows the message at the button. | AR-07, AR-12; RV-01, RV-09. | R-19, R-24 |
| 20 | **Every player can read it:** two channels per fact; one local comfort service; reduced variants keep the information. | Reduced motion turns the fuse blink into a steady glow with a fill countdown; the ring stays. | AR-10, AR-13; RV-04. | R-22, R-23 |

## 8. Framework games (J025): systems, owners, placement
Every game built on `roblox-game-framework` (blocks, API, examples: `engineering-craft` → `references/framework.md`; contracts: `roblox-game-framework/contracts/*.md`) keeps these. They apply R-02, R-08, R-11 and R-12 to the framework's blocks.
- **New systems are Loader systems.** One ModuleScript in `src/server/Systems/` or `src/client/Systems/`: `{ After = { ... } }`, `init` (no yield: build tables, register), `start` (connect, `Net.answer`). No hand-written boot list; the Loader orders by `After` and stops the boot on any failure (`contracts/Loader.md`). A system's own helpers sit inside its module or in `Rules/` (pure).
- **One owner per kind of fact:**

| Fact | Owner | Others |
| --- | --- | --- |
| Saved player data, receipts, award ids | **Session** (`Save.handle:update`, the game's `Save` system holds the handle) | read `get`/`selector`; never `DataStoreService` or `ProcessReceipt` |
| What each client sees of server state | **State** (Charm atoms on the server, charm-sync copies on clients; the game's `Atoms` module names the writer of each atom) | clients read `State.mine`/atoms; never write them |
| The remote surface | **Net** + the game's one schema `net/game.blink` (framework messages merged in) | handlers registered with `Net.on`/`Net.answer`; never a raw remote |
| Boot order | **Loader** | each system declares `After` |
| Screen stack, `blocking` | **Screens** | gameplay reads `view().blocking`, gates its own InputContexts |
| Tween timings, clip table, config keys, analytics names, admin pages | the game's data tables | blocks read them; logic holds no literals |
| Ownership, server-state range, game state, idempotency of a request | the handler's system (N-02 steps 4-7) | Net does not decide them |

- **Placement** (`contracts/README.md` Placement; the template's `default.project.json`; the gate writes `test.project.json` from `tools/placement.json`):

| Goes to | What | Why |
| --- | --- | --- |
| `ReplicatedStorage.Framework` | Types, Helpers, Loader, State, Screens, Motion, Anim | the client needs them; nothing secret |
| `ReplicatedStorage.Packages` | Charm, charm-sync, Janitor, Signal (Wally) | shared |
| `ReplicatedStorage.Shared` | `Atoms`, `Content/` data, client `Remotes` (generated) | shared data |
| `ReplicatedStorage.Client` | `Main.client.luau`, client `Systems/` | client code |
| `ServerScriptService.Framework` | Session, Net, Config, Analytics, Admin (all of Admin, its panel client too: cloned to admins only; CC-19), `vendor/ProfileStore` | server code never replicates |
| `ServerScriptService.Server` | `Main.server.luau`, server `Systems/`, `Save/Schema`, `Rules/`, server `Remotes` (generated) | server rules |
| `ServerStorage.AdminPages` | the game's admin pages and frames | cloned to admins only |
| `<game>/Framework-tools/<Block>/` (outside the place) | Net's Lune patch and schema lint | dev only, lock-checked |
| nowhere in a place | specs, `test/` folders, ContentTests | dev only |

- A block's service is part of its require path (`@game/<Service>/Framework/<Block>`): moving a block means changing the framework's placement file and requires together, in the framework repo, never in a game.
- The framework never holds an event bus, a dependency-injection layer, a UI theme system or an ECS (J025 proposal §3); a game that needs one makes the R-09 case first.
