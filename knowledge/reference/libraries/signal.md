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

# Signal (sleitnick): package record

| Field | Value |
| --- | --- |
| Package | Signal by Stephen Leitnick (`sleitnick/signal`, in the RbxUtil repo); maintained fork of stravant's GoodSignal |
| Version | **2.0.3** (Wally; newest index entry 2025-01-22); RbxUtil last push 2026-08-11; no GitHub releases; checked 2026-10-24 (`research/net-signals-cleanup.md`) |
| Licence | MIT per its `wally.toml`; **no LICENSE file** in the Wally package folder (`research/games.md` §1 row signal): keep the MIT notice from the RbxUtil repo when shipping source |
| Where pinned | framework `wally.toml` `Signal = "sleitnick/signal@2.0.3"`; `wally.lock`; at `ReplicatedStorage.Packages` |
| Used by | Session (`StatusChanged`, `Purchased`); games connect to those signals |

## Why chosen
Correct and fast baseline, yield-safe, typed generics (`Signal<T...>`, `Connection`); already in every earlier game; same upstream as Trove. LemonSignal was rejected (dates not verifiable, its org archived a sibling package 2025-12-23).

## Known gaps and how the framework covers them

| Gap | Covered by |
| --- | --- |
| No `--!strict` line in the package file | framework code that uses it is `--!strict`; types come through the generated package types (`wally-package-types`) |
| Handlers fire newest first | no block or game relies on handler order (`contracts/README.md` rule 4) |
| No LICENSE file in the package | notice kept from the upstream repo (above) |
| `Purchased` is a signal, so a game might grant from it | Session contract CC-4: never grant or count revenue from `Purchased` |

## Update path
One package per change; run Session specs; new framework tag. Replacement cost: Session's two signals (any other typed signal works).
