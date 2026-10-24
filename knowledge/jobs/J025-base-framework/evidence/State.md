---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B4
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# State: Q1-Q9 evidence (J025-B4)

Artifact: `roblox-game-framework/src/State/` {init.luau, State.spec.luau, State.engine.spec.luau, test/World.luau}, files as of 2026-10-24 (repo uncommitted, rule 7). Contract: `contracts/State.md` (frozen; review r1 "ready"). Packages: Charm 0.11.1, charm-sync **0.4.1** (the contract's "charm-sync 0.11" is the Charm line; charm-sync has its own version).

## Contract risk first: per-player filtering in charm-sync 0.4.1 (St2)
Source read: `Packages/_Index/littensy_charm-sync@0.4.1/charm-sync/src/server.luau`. Subscriptions are per client (`addSignalsToClient(client, {key = getter})`), but tracked states are global by key (`trackSignal` warns and ignores a second getter on one key, :53-58). So filtering works per **key**, not per value: each player subscribes to its own wire key `"<name>@<UserId>"` whose getter returns `{ [UserId] = entry }` only; State renames the key to `<name>` in its send wrapper. Neither the contract's primary path (a filter on one map value) nor its fallback (one syncer per player: the server module is a singleton) fits 0.4.1 as written; this per-key subscription is the filter. Proof: St-T2 (every payload to B inspected recursively: no `1001`, no `secret`), planted fault F1 (getter returns the whole map) turns it red.

## Red run (before code; stub erroring "not built")
`lune run tools/spec/run.luau src/State` → `specs: 1 files, 0 passed, 13 failed` (each "State.server not built"). First green run: 13/13; no spec changed after code except the Q6 row gaining a flush counter when the dirty gate was added.

## Q1-Q9
| Q | Result | Evidence |
| --- | --- | --- |
| Q1 API | PASS | 6 functions (`server`, `hydrate`, `setPrivate`, `track`, `client`, `mine`) + `Atoms` type, as the contract. Spec hook `_debugCounts()` (README leak rule) |
| Q2 strict | PASS (gate-verified) | `--!strict` in all 4 files; luau-lsp new solver 0 errors; `grep ":: any" src/State/init.luau` = 0. `any` appears only inside the contract's own `Atoms` type (`Atom<any>`) |
| Q3 tests can fail | PASS | row table below; 7 planted faults, 7 red |
| Q4 failure paths | PASS (Lune) | hydrate spam → one snapshot per accepted call (St-T10; rate is Net's); patch before hydrate dropped (St-T4); view error keeps last value, one sampled warn (St-T7); hydrate/track/setPrivate after leave do nothing (failure row spec); shared+private name clash refused at `server` |
| Q5 leaks | PASS (Lune) | St-T6: 1,000 join → hydrate → track → setPrivate → frame → leave cycles: `_debugCounts` = {subscribed 1, effects 0, entries 0, wireKeys 1} (the 1 is the setup's fake client p1); the source atom changed after the loop re-runs 0 views |
| Q6 cost | over PROPOSAL in Lune / not verified (engine) | Lune, 50 hydrated players, 4,000 iterations × 3 runs: one private change + frame 0.149 / 0.151 / 0.154 ms; one shared change + frame 0.136 / 0.150 / 0.146 ms (budget ≤ 0.1 ms); idle frame 0.00016-0.00018 ms. Bytes (JSON proxy): 10,293 B view → 10,333 B hydrate (≤ 12 KB), one changed field → 55 B patch (≤ 64 B). Cost is O(players) per change: each player's wire getter is a charm-sync effect on the shared map atom, and `flush` runs a per-client select (3 tables per client). Idle: charm-sync's own interval diffs and allocates per client every frame; State turns it off (`config.interval = -1`) and flushes on Heartbeat only after a synced atom changed (planted fault "dirty never set" → 6 red) |
| Q7 server authority | PASS | the client sends only the hydrate request, no arguments, reached through `Net.on` (rate, readiness). `hydrate` ignores a player who left. Client copy decides nothing; the client drops patches for keys without a snapshot |
| Q8 engine first | PASS | below |
| Q9 usage | PASS (Lune) | spec "Q9": the contract usage example with fake Net/Save/Remotes/View: client coins 3, then 8 after a server change |

## Contract test rows → specs (`src/State/State.spec.luau` unless named)
| Row | Spec | Planted fault → red |
| --- | --- | --- |
| St-T1 | "St-T1: a server atom change reaches the client atom; a client write is overwritten by the next patch" | dirty gate off → red |
| St-T2 | "St-T2: player B's payloads never hold player A's key" | F1 getter returns whole map → red; F4 hydrate without reset → red |
| St-T3 | "St-T3: one changed field of a 100-field view sends that field only" | (dirty gate off → red) |
| St-T4 | "St-T4: a patch before hydrate is ignored; hydrate + patches equals the server" | F2 no pre-hydrate drop → red |
| St-T5 | "St-T5: in-place mutation ... errors in Studio mode" (sets `Charm.flags.frozen`, as Studio does) | n/a: Charm's freeze, not State code |
| St-T6 | "St-T6: 1,000 join/leave cycles ..." + "St6: leave removes the entry ..." | F3 leave skips dispose → red; F6 leave keeps entries → red |
| St-T7 | "St-T7: track follows a selector through 3 updates ..." | F5 no pcall around view → red |
| St-T10 | "St-T10: 5 accepted hydrate calls send 5 full snapshots ..." | F4 → red (0 snapshots) |
| St-T8 | `State.engine.spec.luau` "St-T8 ..." (scenario `bytes`) | written, NOT RUN (engine lane) |
| St-T9 H | `State.engine.spec.luau` "St-T9 ..." (scenario `twoClients`); QA's H spec is separate | written, NOT RUN |

## Q8 engine features
| Need | Engine / package | Source |
| --- | --- | --- |
| Leaf flags on world objects | Instance attributes (St8; not State) | `_api-reference/classes/Instance.yaml:1338` |
| Ordered delivery the snapshot-then-patch order relies on | reliable RemoteEvent order | `scripting/events/remote.md:374-383` |
| Leave cleanup | `Players.PlayerRemoving` | `_api-reference/classes/Players.yaml:1610` |
| Frame flush | `RunService.Heartbeat` | `_api-reference/classes/RunService.yaml:743` |
Own code still needed: the engine replicates no tables; charm-sync leaves transport, per-player filtering, hydration order and leave cleanup to the caller (`research/state-ui-animation.md` §2).

## Deviations and notes
- Lune seam: `test/World.luau` (fake Players, RunService) + the spec's `load` (luau.load with a fake `game`), Session's FakeWorld pattern. The spec holds the `@lune/` calls, so the fake stays type-checked; the spec itself is not (gate rule for `@lune/` files).
- St-T1's overwrite holds for whole-value atoms; a client write to a table field that the next patch does not touch stays until that field changes (charm-sync applies diffs). St1 stays a code-review rule.
- `track` keeps a plain `{ [map] = dispose }` per player instead of a Janitor (one kind of item; same lifetime rule).
