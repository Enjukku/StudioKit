---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B2
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Motion: Q1-Q9 evidence (J025-B2)

Files: `roblox-game-framework/src/Motion/init.luau`, `Motion.spec.luau`, `Motion.engine.spec.luau`. Contract: `contracts/Motion.md` (2026-10-24). Lune 0.11.1 (`@lune/roblox` Enum; TweenInfo, TweenService, GuiService faked), luau-lsp 1.70.1.

| Q | Result | Evidence |
| --- | --- | --- |
| Q1 | pass | 3 functions, as the contract: `rows`, `play`, `reduced`; exported types `Timing`, `Row` |
| Q2 | pass | `--!strict`; luau-lsp 0 errors on `init.luau` and `Motion.engine.spec.luau` (Jest group); grep `any` in `init.luau` = 0 |
| Q3 | pass | rows below; planted faults 5/5 red (table 2) |
| Q4 | pass | failure rows: bad table (M-T1), unknown id (M-T6), engine error (M-T7 Lune + engine), destroyed instance (M-T7 engine) |
| Q5 | pass (code read) | no lifetime: module state is the frozen row cache only; no connection (reduced state is read at each play), no tween registry (M5). M-T4 spec: 1,000 plays keep 1,000 tweens in the fake's list, none in Motion |
| Q6 | pass (Lune); engine not verified | `play` 0.140 µs of Motion's own cost (median of 3 × 1e6, fake Create; budget ≤ 30 µs incl. engine), 0.0 KB over 1e5 plays (screening). `rows` for 100 rows 0.59-0.65 ms (3 runs; 1.10-1.25 ms before caching the two Enum lookups in locals; budget ≤ 1 ms). Hot-path allocation: the engine Tween only (M-T4: TweenInfo count unchanged by 1,000 plays) |
| Q7 | n/a | client presentation only; no server entry point |
| Q8 | pass | TweenService + TweenInfo + GuiService.ReducedMotionEnabled (table 3); own code adds the motion table, the required reduced variant and its checks |
| Q9 | pass with a usage fix | the contract's example as written (`return table.freeze({...})`, no annotation) does not type-check against `{ [string]: Row }`: luau-lsp "Expected { [string]: Timing & { reduced: "instant" \| Timing } } but got { read panel_open: { ... reduced: string ... } }" (probe 2026-10-24, `.gate/probe`, deleted). Annotated then frozen it does: `local rows: { [string]: Motion.Row } = {...}; return table.freeze(rows)`. That form is the Q9 case "Q9 usage" in `Motion.engine.spec.luau` (type-checked, run not verified). Proposed one-line change to the contract's Usage (architect) |

## 1. Contract test rows → specs (`Motion.spec.luau` unless marked)
| Row | Spec name(s) |
| --- | --- |
| M-T1 | "a row without reduced: rows errors with the row id"; "time NaN, -1, 11 and inf, and a NaN delay"; "an unknown field, in the row or in reduced"; "a style or direction of the wrong enum, and a bad reduced value"; "rows runs once" |
| M-T2 | Lune: "(logic) reduced() reads GuiService.ReducedMotionEnabled and the next play follows it". Engine: "M-T2 reduced() equals GuiService.ReducedMotionEnabled". The toggle is manual: the property is ReadOnly (`GuiService.yaml:276`), so a script cannot flip it; flip Studio's Reduce Motion and run again |
| M-T3 | Lune: "(logic) reduced + instant: time 0 with the goal; with reducedGoal: the reducedGoal"; "(logic) both variants carry time, style, direction and delay". Engine: "M-T3 the end state carries the goal ..." |
| M-T4 | "1,000 plays create no TweenInfo: at most rows x 2, all built before the first play" (1 shared instant + 5 for 3 rows; 6 after 1,000 plays) |
| M-T5 | Engine: "M-T5 row A then row B on the same property: the final value is B's" (A Cancelled) |
| M-T6 | "an unknown row id errors, and play before rows errors" |
| M-T7 | Lune: "(logic) an error from TweenService:Create reaches the caller unchanged". Engine: "a goal property the instance lacks ..."; "the instance destroyed mid-tween ..." |

Engine rows: written, not run (`Motion.engine.spec.luau`). Red run before code (stub): `specs: 1 files, 1 passed, 11 failed`, e.g. `FAIL src/Motion/Motion.spec.luau:82: M-T1 a row without reduced: rows errors with the row id: expected false, got true`. After: 12 passed.

## 2. Planted faults
| Fault | Caught by |
| --- | --- |
| a missing `reduced` falls back to instant | M-T1 (2 red) |
| reducedGoal ignored | M-T3 |
| time cap 100 s | M-T1 |
| reduced state ignored in play | M-T2, M-T3 (3 red) |
| `rows` callable twice | M-T1 once |

## 3. Engine features and docs read
`_api-reference/classes/TweenService.yaml:33-35` (a newer tween on the same property cancels the old), `:49-90` Create; `GuiService.yaml:262-282` ReducedMotionEnabled (Hidden, ReadOnly, read security None, maps to the Settings toggle); `ui/animation.md:27-45` (tweens on the client). GWS source `src/client/Ui/Motion.luau:30-39` read; it also reads `GuiService.ReducedMotionEnabled` directly.

## 4. Decisions inside the contract
- `reduced()` and `play` read `GuiService.ReducedMotionEnabled` at the call instead of caching it from a `GetPropertyChangedSignal` connection (contract Lifecycle line). Same truth, no state and no connection to own; M2 holds (no second setting, follows every change). Reviewer: say if the connection is wanted.
- One shared `TweenInfo.new(0)` for every `"instant"` reduced variant (M4: ≤ rows × 2).
- The 10 s cap (PROPOSAL) applies to `delay` too; a missing delay is 0.
- Unknown fields are errors in the row and in `reduced` (typos such as `easing` fail the boot).
