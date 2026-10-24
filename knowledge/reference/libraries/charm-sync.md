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

# charm-sync (atom replication): package record

| Field | Value |
| --- | --- |
| Package | charm-sync by littensy (`littensy/charm-sync`, same repo family as Charm) |
| Version | **0.4.1** (Wally; newest index entry 2026-10-01; needs charm >= 0.11.0, < 0.12.0); checked 2026-10-24 (framework `CHANGELOG.md`) |
| Licence | MIT (`Packages/_Index/littensy_charm-sync@0.4.1/charm-sync/LICENSE`) |
| Where pinned | framework `wally.toml` `CharmSync = "littensy/charm-sync@0.4.1"`; `wally.lock`; at `ReplicatedStorage.Packages` |
| Used by | the State block only; game code never calls it |

## Why chosen
Server-to-client patches (changed paths only, State St3) and ordered hydration for Charm atoms, from Charm's own author; it replaces DataService's full-table replication and the hand-written client copies of earlier games (`contracts/State.md` Extraction source).

## Known gaps and how the framework covers them

| Gap (0.4.1) | Covered by |
| --- | --- |
| Transport is left to the caller | State takes the generated Blink `Fire`/`On` functions (`State.server(atoms, send)`, `State.client(atoms, receive, hydrate)`) |
| No per-player filtering of one value: tracked states are global by key (`server.luau:53-58` warns on a second getter) | State subscribes each player to its own wire key `"<name>@<UserId>"` returning only that entry, and renames it back in its send wrapper (`knowledge/jobs/J025-base-framework/evidence/State.md` §Contract risk); proof St-T2 (every payload), St-T9 (two real clients, H) |
| Hydration order and late joiners left to the caller | State: patches before the hydrate snapshot are ignored (St4); hydrate request through `Net.on` with `beforeReady = true` |
| No cleanup on leave | State removes the player's entries and `track` effects on `PlayerRemoving` (St6, St-T6: 1,000 cycles, 0 entries) |
| A client write to a table field the next patch does not touch stays until that field changes (diff apply) | client writes are forbidden by review (State St1, `code-review`) |
| Cost over the PROPOSAL budget in Lune (one change + frame about 0.15 ms for 50 players vs 0.1 ms) | recorded as floor in `evidence/State.md`; engine cost not verified (St-T8, Studio multi-client) |

## Update path
Move only together with Charm, inside its declared range; re-run St-T2 and St-T9 first (the per-key filter depends on `addSignalsToClient` and `trackSignal` behaviour). Replacement cost: the State block only.
