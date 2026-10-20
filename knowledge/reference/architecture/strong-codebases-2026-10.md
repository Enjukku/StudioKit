---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "owner-supplied research paper 'Strong Game Codebases' (ChatGPT, 2026-10-20); file kept outside git at C:\\Users\\Firew\\Downloads\\Strong_Game_Codebases_Research.docx"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Paraphrased digest for J001 step 6 (architecture, code review). Paper sections in brackets. Trust: owner material. Its Roblox claims cite current Roblox docs that the local mirror holds; its studio evidence (Riot, Valve, Epic, Mojang, Blizzard, Wube, 2021-2025) is experience reports used as principles, not engine facts.

# Strong game codebases: digest of the owner's research paper

## Core claim
A strong codebase makes the **consequences of a change understandable before it ships**: who owns a fact, who may change it, when a change becomes true, how it reaches other systems, what happens on failure. Framework names matter less than a small set of **enforced boundaries**. Goal: likely changes cheap, dangerous changes visible, old decisions reversible. [Exec, §1]

## Principles to carry into skills
| ID | Principle | Paper |
| --- | --- | --- |
| A-01 | Start from **invariants** (rules that must stay true: no double spend, one shot = one ammo, no double reward on retry). For each: owner, inputs, clock, failure response, test | §2.1 |
| A-02 | **Ownership ≠ authority ≠ location.** A client copy of health is not ownership. "Shared" code is not "trusted" code. One authoritative writer per mutable aggregate (a character's combat state, an inventory, a match phase, a save record); others request through its interface | §2.2 |
| A-03 | **Capability review:** ask what an object *can* do, not what we intend (Valve sticky-bomb bug: a reused NPC kept player control) | §2.2 |
| A-04 | **Time is part of the interface.** Name the clock for each rule; a tween ending never decides damage; client timestamps are claims | §2.3 |
| A-05 | **Five boundaries:** simulation vs presentation; commands vs state vs events (`FireWeapon` request ≠ `WeaponFired` result; events for independent reactions only, never hidden vetoes); definitions vs runtime instances vs durable ownership; session vs durable state (rewards as uniquely identified requests to the persistence owner); domain rules vs platform adapters (only for nondeterministic, expensive, failing or changing dependencies, not every engine call) | §3.1-3.5 |
| A-06 | Data-driven content, but **no second programming language in config**: a small set of behaviour interfaces, every definition validated against them | §3.3 |
| A-07 | **Directed dependencies:** composition root → feature orchestrators → domain owners and pure policies → narrow interfaces → platform adapters. A cycle signals a missing owner or orchestrator; deferring a lookup does not fix it | §4.1, §6.1 |
| A-08 | Boundaries earn their place (an invariant, a replacement seam, a test seam or a distinct lifecycle). No universal "GameService"; no dozens of forwarding modules | §4.1 |
| A-09 | **Module contract**, six items: owns; callers may request; promises on success; how it fails; dependencies; how it stops. Plus: yields? re-entrant? returns copies or internals? | §4.2 |
| A-10 | **Lifecycle is gameplay:** construct → init → start → run → stop → destroy; every connection, task, instance has a lifetime owner (character, session, match, server); after any yield, re-check a session or generation token; cleanup safe to call twice; test repeated start-stop and respawn loops | §4.3 |
| A-11 | Plain modules and composition are the default; ECS only for large regular workloads, benchmarked on a real slice; hybrids fine without two writable copies of one fact | §4.4 |
| A-12 | Genre pressures: shooters = time and trust (define history window, stale-claim policy); MOBA-like ability games = explicit execution model (eligible → target → reserve → commit → effect → done/cancel) and documented modifier order; sandbox = durable ids separate from runtime ids, offline simulation rules, crafting and trading as transactions, schema migrations with fixtures | §5 |
| A-13 | Roblox: composition root per side, not a service locator; strict types for contracts but runtime decoding at the boundary (types are not security); results distinguish **denied / temporarily unavailable / completed** | §6.1-6.2 |
| A-14 | Roblox: authority independent of replication; every remote a public API (version, action id, bounded payload; cheap rejects first; aggregate denial logs) | §6.3-6.4 |
| A-15 | Roblox: profile as a **state machine** (loading, ready, degraded, closing, closed); never "load failed = new player"; old and new servers live at once, so schema changes need a compatibility plan; per-key updates are not multi-record transactions | §6.5 |
| A-16 | Roblox: streamed objects are temporary representations; attach and detach controllers; waits need timeouts | §6.6 |
| A-17 | Parallel Luau only for a measured independent workload; workers produce candidates, the owner applies them | §6.7 |
| A-18 | **Locality test:** a new content item should touch only its definition, behaviour and tests; if it touches saves, every remote and unrelated UI, the boundary is wrong. A new mechanic deserves a design review | §7 |
| A-19 | Performance is a contract: content, runtime and collaboration scale differ; test peak and unusual cases; profiler labels per domain; fixed repeatable benchmark scenario with recorded device and content version | §8 |
| A-20 | **AI delegation:** a bounded slice or contract (owned files, interface, invariants, allowed dependencies, tests, non-goals), not "improve the architecture"; adversarial review (duplicated authority, callbacks outliving owners, effects after yields, retries repeating side effects); tests written from independent acceptance examples; one owner per shared contract change; executable checks plus a short explanation | §9 |
| A-21 | Packages earn adoption by a concrete risk or work reduction; record version, owner, update path and replacement cost | §9 |
| A-22 | **Refactor without rewrites:** characterise one painful change → contract + tests → adapter in front of the old path → new path behind a gate → limited slice → retire deliberately. A feature flag is not a rollback if data changed | §10 |
| A-23 | **Audit** (evidence per item): ownership, dependencies, contracts, authority, lifecycle, persistence, streaming, performance, extensibility, release safety. Fix by harm and blast radius: data corruption and exploitable authority first | §11 |

## How it maps to the kit
- Already covered: A-14 (`networking-security` N-02), A-15 (`data-saving` D-04, D-08), A-17 and A-19 (`performance` F-07, F-08, F-10).
- New for step 6 (architecture + code review): A-01 to A-13, A-16, A-18, A-20 to A-23.
- Step 7 (anti-over-engineering): A-05 adapters only where they pay, A-08, A-11, A-21.

## Kit verdict (orchestrator, 2026-10-20): where the paper does not fit Roblox as written
- **Protocol versions on remotes** (§6.4): not needed. Each Roblox server sends its own client code, so a client and its server always match. Versions are needed for saved data and for cross-server messages (MessagingService, MemoryStore, DataStore), where old and new servers meet.
- **"No service locator"** (§6.1): Luau `require` already makes dependencies visible in the file. The real risk is lookup by name at runtime (a string registry). Singleton services required directly are acceptable when their start order is explicit.
- Studio evidence (Riot, Valve, Mojang, Blizzard) is from large non-Roblox teams; use it for principles, not for sizes, tools or numbers.

## Applied to approved skills (2026-10-20)
networking-security (capability review, cheap checks first, re-check after yields, no remote versions, N-14 outcomes and quiet logs); data-saving (newer-schema guard, named session states, shutdown honesty, award ids); performance (fixed benchmark scene, peaks, cache and wake owners); ui-basics (late answers dropped, streamed-out targets, WaitForChild timeouts); orchestration (code briefs: owned files, interface, invariants, non-goals, briefer-written failure checks).

