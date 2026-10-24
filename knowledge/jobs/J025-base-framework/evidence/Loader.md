---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B3
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Loader: Q1-Q9 evidence (J025-B3)

Artifact: `roblox-game-framework/src/Loader/` {init.luau, Loader.spec.luau, Loader.engine.spec.luau, Loader.multiclient.engine.spec.luau}, files as of 2026-10-24 (repo uncommitted, rule 7). Contract: `contracts/Loader.md` (frozen, with R7, N1, lead client-failure decision).

## Red run (before code; stub `return {}`)
`lune run tools/spec/run.luau src/Loader` → `specs: 1 files, 0 passed, 15 failed` (each "attempt to call a nil value": Loader.run/_collect/start missing). One spec bug of my own found on the first green run (L-T4 expected a call from a system with no `init`); fixed the expectation, not the code.

## Q1-Q9
| Q | Result | Evidence |
| --- | --- | --- |
| Q1 API | PASS | 2 public functions (`start`, `run`) + 3 exported types, as the contract. One spec hook `_collect(systems, load)` (discovery + require; `start` passes `require`), underscore = not public API, same convention as `_debugCounts` (contracts/README.md leak rule) |
| Q2 strict | PASS (gate-verified, Loader files) | every file `--!strict`; luau-lsp new solver 0 errors on the 4 Loader files; `grep ":: any" src/Loader/init.luau` = 0 (specs use `:: any` only to pass fake instances) |
| Q3 tests can fail | PASS | row table below; 13 planted faults, 13 red after one spec fix (F5 first survived → added string-key and hole cases to L-T9, which also found a real gap: `{ [1]="Save", [3]="Shop" }` passed the check; fixed by count vs `#After`) |
| Q4 failure paths | PASS (Lune) / not verified (engine) | every Failure-behaviour row → spec: require (L-T10), check (L-T2, L-T9), order (L-T7, L-T8), init error/yield (L-T6, L-T5), start error/yield (L5, L4); server kick L-T12 and client message L-T14 written, not run |
| Q5 leaks | PASS (by design + spec) | no lifetime: no per-player or per-open table, no connection after a good boot; only the failure `PlayerAdded` kick (server life). Spec "Q5 run keeps no state": 1,000 runs, same order, exact 4,000 calls |
| Q6 cost | PASS (Lune screening) / not verified (engine) | L-T13, 40 systems, `_collect` + `run` with no-op init/start, 3 runs × 3 invocations: medians 0.381 / 0.422 / 0.483 ms (spread 0.245-0.512) vs budget 2 ms server. Boot-only code: no per-frame work, no hot path. Studio boot report line is the record (not run) |
| Q7 server authority | n/a | no client input (contract) |
| Q8 engine first | PASS | below |
| Q9 usage | PASS (type-checked) / not run | `Loader.engine.spec.luau` "Q9 ...": the entry line type-checks in a never-called function; the Shop After Save example boots in order through `run` |

## Q3 row → spec, planted fault
| Row | Spec (Loader.spec.luau unless noted) | Planted fault → red |
| --- | --- | --- |
| L-T1 | "L-T1 discovery ..." (fake tree); engine: "L-T1 finds systems ..." | F9 walk enters system modules |
| L-T2 | "L-T2 two systems with one name ..." | F6 duplicates allowed |
| L-T3 | "L-T3 order is topological ... 100 shuffled" | F2 no name tie-break |
| L-T4 | "L-T4 every init runs once before the first start" | F11 init/start interleaved |
| L-T5 | "L-T5 an init that yields ..."; engine: "L-T5 ... task.wait()" | F1 no yield detection |
| L4 (start) | "L4 a start that yields ..." | F1 |
| L-T6 | "L-T6 the 3rd of 5 inits errors" | F3 init error does not stop |
| L5 (start) | "L5 a start that errors stops the later starts" | F11 |
| L-T7 | "L-T7 After naming a missing system ..." | F7 missing allowed |
| L-T8 | "L-T8 a cycle ... path" (+ self-cycle) | F4 path lists one name |
| L-T9 | "L-T9 a non-table module, ..." (8 bad values) | F12 holes/string keys allowed, F5b names unchecked, F13 init type unchecked |
| L-T10 | "L-T10 a require that throws ..."; engine: "L-T10 a ModuleScript that throws" | F10 require error ignored |
| L-T11 | "L-T11 a second start ..." | F8 started flag not set |
| L-T12 | Loader.multiclient.engine.spec.luau "L-T12 ..." (scenario serverFail) | not run |
| L-T13 | "L-T13 40 systems ..." (median < 2 ms) | screening number |
| L-T14 | Loader.multiclient.engine.spec.luau "L-T14 ..." (scenario clientFail, one respawn) | not run |

## Q8 engine features
| Feature | Docs | Use |
| --- | --- | --- |
| One Script per side + ModuleScripts with `start()` | `scripting/locations.md:36-51` | the pattern; Loader replaces the hand list with folder scan + `After` + cycle check + fail-loud |
| `task.cancel` closes a suspended thread so the scheduler never resumes it | `_api-reference/libraries/task.yaml:232-237` | L4 yield → cancel; Lune probe: cancelled thread did not resume after `task.wait(0.05)` |
| `ResetOnSpawn = false` keeps the message through respawn | `_api-reference/classes/LayerCollector.yaml:55-69` | client failure ScreenGui (N1) |
| `ScreenInsets.None` full-screen cover | `_api-reference/classes/ScreenGui.yaml:64-66` | client failure screen |
| `Player:Kick(message)` | `_api-reference/classes/Player.yaml:2078` | server failure, present + later players |

## Engine specs written, not run (lead batches them)
`src/Loader/Loader.engine.spec.luau` (Edit DM: L-T1, L-T5, L-T10, Q9; needs plugin rights for `ModuleScript.Source`); `src/Loader/Loader.multiclient.engine.spec.luau` (1-client play test, `workspace` attribute `LoaderScenario` = serverFail / clientFail; recipe in the file header; present-player kick needs the variant entry that waits for `PlayerAdded`).

## Decisions inside the contract
- `run` gets required values (pure); the require phase lives in `_collect`, so L-T10 runs in Lune with a throwing `load`.
- Requires run in name order (deterministic first failure); `init`/`start` in `After` order.
- `start` passes `require` as a value; the gate's string-require rule does not apply to the Loader's dynamic require (noted for the reviewer).
- Report `ms[name]` = require + init + start ms; one `print` line per boot, `warn` above 100 ms (PROPOSAL).
- Client failure: `task.spawn(showMessage)` then `error()`, so the error never waits for PlayerGui.
