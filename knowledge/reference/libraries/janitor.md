---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
roles: [feature-builder, reviewer]
---
> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24

# Janitor (cleanup): package record

| Field | Value |
| --- | --- |
| Package | Janitor by howmanysmall (+ Validark and others), `howmanysmall/janitor` |
| Version | **1.18.3** (Wally; newest index entry 2025-03-13); repo push 2026-07-28; GitHub releases stop at v1.17.0 (2024-08-12); 151 stars, 6 issues; checked 2026-10-24 (`research/net-signals-cleanup.md`) |
| Licence | MIT (`Packages/_Index/howmanysmall_janitor@1.18.3/janitor/LICENSE`) |
| Dependencies | pulls `howmanysmall/typed-promise` 4.0.6 → `evaera/promise` 4.0.0 (MIT) even when unused; the framework does not use Promise (engine `task` + `pcall`, common rule 5) |
| Where pinned | framework `wally.toml` `Janitor = "howmanysmall/janitor@1.18.3"`; `wally.lock`; at `ReplicatedStorage.Packages` |
| Used by | Screens (one Janitor per open: `handle.janitor`), Anim, State, Admin; game screens add their connections and tweens to `handle.janitor` |

## Why chosen
`--!strict` and `--!optimize 2` in the source; already in every earlier game (migration cost zero); keyed add and replace. Trove (sleitnick, no dependencies) was the alternative; a switch is justified only for a new game with no legacy code that wants typed-promise out of the lock file (`research/net-signals-cleanup.md` §cleanup).

## Known gaps and how the framework covers them

| Gap | Covered by |
| --- | --- |
| Cleanup order is not a guarantee | no block depends on it; no code that can throw runs in a cleanup (`contracts/README.md` rule 3) |
| `Destroy()` makes a later `Add` from a yielding builder fail or leak | Screens closes with `janitor:Cleanup()` (CC-10) so a late `Add` is still cleaned |
| Pulls a Promise library | Promise is never required by framework or game code (`code-review` §8 B5 allows only this transitive copy) |
| GitHub releases lag Wally | the Wally version and `wally.lock` are the pin of record |

## Update path
One package per change; read the diff (it is about 1,000 lines); run Screens, Anim, State and Admin specs plus their leak rows (1,000 cycles, 0 entries); new framework tag. Replacement cost: the four blocks above (each holds its own Janitor).
