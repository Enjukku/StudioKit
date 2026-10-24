---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B1
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Helpers (RateLimit, Amount, Ledger) + Types: Q1-Q9 evidence

Code: `roblox-game-framework/src/Helpers/{RateLimit,Amount,Ledger}.luau`, `src/Types/init.luau`. Specs: `src/Helpers/{RateLimit,Amount,Ledger,Helpers,Usage}.spec.luau` (Lune). Contract: `contracts/Helpers.md` + `README.md` (Types), files as of 2026-10-24.

**Red run before code** (`lune run tools/spec/run.luau src/Helpers`, no modules yet):
```
FAIL src/Helpers/Amount.spec.luau: could not load: require "./Amount" ...: no module at src/Helpers/Amount
FAIL src/Helpers/Ledger.spec.luau: could not load: require "./Ledger" ...: no module at src/Helpers/Ledger
FAIL src/Helpers/RateLimit.spec.luau: could not load: require "./RateLimit" ...: no module at src/Helpers/RateLimit
specs: 4 files, 0 passed, 4 failed
```
Green: `specs: 5 files, 21 passed, 0 failed` (src/Helpers). The behaviour-level reds are the planted faults below.

| Q | Result | Evidence |
| --- | --- | --- |
| Q1 | pass | 8 functions + `MAX`, as in the contract. The returned objects are Allowance {take, reset, size} and Cooldown {ready, remaining, reset, size}. One extra exported type, `RateLimit.Clock`. Types: 4 types, no values (`return table.freeze({})`) |
| Q2 | pass (gate-verified for my files) | every file starts with `--!strict`; luau-lsp gives 0 errors on all Helpers/Types files, including `Usage.spec`; selene and stylua are clean. The `:: any` grep over the code files finds 0 hits. Internal casts are `log :: { unknown }` (Ledger) and `entry :: string`, never in a public type |
| Q3 | pass | row table below; 14 of 14 planted faults turned a spec red (2 survived the first run and closed after new cases) |
| Q4 | pass | failure rows: bad constructor args and NaN rate → `error` (H-T10); NaN or inf clock → no credit (H-T4); non-number `Amount.*` → 0 or false (H-T5, isWhole spec); `record` cap < 1, NaN or inf → `error` (H-T10) |
| Q5 | pass | H-T9: 1,000 table keys, then `reset` on each (and a second `reset`) → `size()` is 0 for Allowance and Cooldown. Amount and Ledger hold no state |
| Q6 | pass in Lune; engine not verified | Lune 0.11.1, 3 runs (scratchpad `b1-helpers/bench*.txt`). `take` 0.24-0.31 µs, `ready` 0.18-0.20 µs, `whole` 0.18-0.19 µs, `isWhole` 0.17-0.22 µs, `seen` on 100 ids (miss) 0.63-0.74 µs: all 0 KB `gcinfo` growth over 100k calls (H-T3 asserts 0). `record` on 100 ids: 8.4-8.7 µs in a default environment (≤ 20 µs budget), 1 array (`table.create`). Under the spec runner's custom `environment` it costs 26-30 µs, because a custom environment turns off Luau's builtin fast paths (Roblox does not do this). Engine and native-code numbers are not verified |
| Q7 | n/a | no client input reaches Helpers (contract). `Amount.isWhole` is the N-02 count check that Net and handler code call |
| Q8 | pass | Luau only: `table.freeze`, `table.create`, `table.find`, `math.floor` (`luau/tables.md:329-349`). Own code is needed because the engine's ~500 req/s throttle is network-level, not per handler (`scripting/events/remote.md:410-411` points to the Throttling section) |
| Q9 | pass | the contract Usage block runs as `Usage.spec.luau` "Q9 the contract's usage example runs", type-checked strict |

## Test row → spec
| Row | Spec (file: name) |
| --- | --- |
| H-T1 | RateLimit.spec: "H-T1 allowance 5/s burst 5: first 5 pass, then one per 0.2 s" |
| H-T2 | RateLimit.spec: "H-T2 jitter: 2 calls 10 ms apart after a quiet second both pass at burst 2" (+ a long quiet spell saves only `burst`) |
| H-T3 | RateLimit.spec: "H-T3 a Player-like table key and a number key are independent"; "H-T3 100k take and ready on existing keys allocate nothing" |
| H-T4 | RateLimit.spec: "H-T4 allowance: a clock that jumps back 10 s gains no credit"; "...NaN or inf from the clock gains no credit"; "H-T4 cooldown: a clock that jumps back or returns NaN is not ready" |
| H-T5 | Amount.spec: "H-T5 whole maps every bad input to 0..."; "H4 whole never returns NaN, inf, a negative or a fraction" (10k seeded values); add, isWhole, MAX specs |
| H-T6 | Ledger.spec: "H-T6 seen on bad input is false, never an error"; "H-T6 record on bad input: no error, only non-empty strings kept" |
| H-T7 | Ledger.spec: "H-T7 record at cap 3 with 5 ids keeps the last 3, frozen, input untouched, duplicate ignored"; "H-T7 record at the real cap (200 awards) over 1,000 ids" |
| H-T8 | Helpers.spec: "H-T8 the three files require nothing and touch no Roblox service" (`require(`, `game:`, `GetService`) |
| H-T9 | RateLimit.spec: "H-T9 reset then size() is 0 after 1,000 keys" |
| H-T10 | RateLimit.spec: "H-T10 bad constructor arguments error"; Ledger.spec: "H-T10 record with cap < 1, NaN or inf errors" |

## Planted faults (one at a time, restored after each; script: scratchpad `b1-helpers/plant_b1.py`)
| Fault | Caught by |
| --- | --- |
| `whole` lets NaN through / lets inf through | H-T5 |
| `add` without saturation | add spec |
| `isWhole` accepts fractions | isWhole spec |
| `record` adds a duplicate (double grant) | H-T7 |
| `record` ignores cap / returns unfrozen / accepts NaN cap | H-T7 / H-T6 / H-T10 |
| `seen` accepts an empty id | H-T6 |
| allowance stamp follows a backwards clock | H-T4 |
| allowance without the burst cap | H-T2 (survived round 1; the long-quiet case was added) |
| allowance `reset` leaks the key | H-T9 |
| cooldown passes a new key on a NaN clock | H-T4 cooldown (survived round 1; the NaN new-key case was added) |
| allowance accepts a 0 or NaN rate | H-T10 |

## Decisions inside the contract
- The clock guard is `t - t == 0` (finite). An Allowance keeps the latest finite reading per key, which never moves back, so a back jump followed by a return grants nothing (H3). For a key first seen at a NaN time, the stamp is `-inf`, so no credit comes from it.
- A new Cooldown key at a NaN time is not ready (it denies, so the key is not stuck on a NaN stamp). `remaining` is clamped to [0, seconds].
- `Ledger.record` keeps the existing ids in their order. It does not remove duplicates that are already in a corrupt input; it only never adds `id` twice (H5 as written). A fractional cap is floored.
