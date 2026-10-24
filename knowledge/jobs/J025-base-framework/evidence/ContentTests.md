---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B2
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# ContentTests: Q1-Q9 evidence (J025-B2)

Files: `roblox-game-framework/src/ContentTests/Check.luau`, `Check.spec.luau`, `Check.usage.spec.luau`. Contract: `contracts/ContentTests.md` (2026-10-24). Lune 0.11.1, luau-lsp 1.70.1. Placement `none` (`tools/placement.json`).

| Q | Result | Evidence |
| --- | --- | --- |
| Q1 | pass | 5 functions, as the contract: `unique`, `refs`, `range`, `each`, `none`; exported types `Rows`, `Row` |
| Q2 | pass | `--!strict`; luau-lsp 0 errors on `Check.luau` and `Check.usage.spec.luau`; grep `:: any` in `Check.luau` = 0 |
| Q3 | pass | rows below; planted faults 6/6 red (table 2) |
| Q4 | pass | contract failure rows: row not a table, field missing (CT-T1), field in no row (CT-T7), problems found (CT-T6) |
| Q5 | n/a | pure functions, no lifetime |
| Q6 | pass | a spec over 2,000 rows (unique + range + refs + each + none) 6-7 ms in Lune (3 runs); budget ≤ 50 ms |
| Q7 | n/a | offline tests only |
| Q8 | pass | no engine feature: content is plain Luau; Luau strict types catch shape (`luau/type-checking.md`), this catches values |
| Q9 | pass with a type change (needs-decision) | `Check.usage.spec.luau` runs the contract's example on typed, frozen tables (green) and on a bad icon (red) |

## The API type change (needs-decision)
The contract types `Rows = { [string]: { [string]: unknown } } | { { [string]: unknown } }`. luau-lsp (new solver) rejects every real game table against it: `{ [string]: Item }` fails ("Expected the indexer result to be exactly `unknown`, but got `Item`": indexers are invariant), and a frozen literal fails because its rows are sealed tables with `read` fields. Also tried: generic `{ [K]: V }` and `{ read [unknown]: unknown }`: both reject frozen literals. `{}` accepts annotated, frozen and array tables and rejects a number (probe 2026-10-24). Built: `export type Rows = {}` for `rows` and `targets`, and `rule: (key: string, row: Row) -> string?` with `Row = { read [string]: unknown }`. Same five functions, arguments and meaning; checks stay run-time (CT1). Default if not answered: keep this.

## 1. Contract test rows → specs (`Check.spec.luau`)
| Row | Spec name(s) |
| --- | --- |
| CT-T1 | "malformed rows give problem lines, never an error, and the table is unchanged" (frozen input; a number row, a missing field, a nested table, a string price); "rows that are not a table at all are one problem line" |
| CT-T2 | "the same input twice gives identical sorted output"; "unique names the value and every row that uses it, sorted"; "array rows are named by index" |
| CT-T3 | "range flags NaN, inf, a string, a fraction and below-min: 5 problems"; "range above max, and fractions allowed without integer" |
| CT-T4 | "the helper touches no engine: no game, no services, no require" (reads `Check.luau`, comments stripped) |
| CT-T5 | "refs with a string field and an array field; a missing target is named" |
| CT-T6 | "a planted duplicate id in a sample table turns the spec red, listing every problem"; "no problems: none returns quietly". The template's own sample table and its spec are step 7's (contract) |
| CT-T7 | "a field present in no row is one problem line naming it" (range, unique, refs) |
| (each) | "each runs any rule; a rule that errors is a problem line, not an error" |

Red run before code (stub returning `{}`): `specs: 1 files, 2 passed, 11 failed`, e.g. `FAIL src/ContentTests/Check.spec.luau:36: CT-T1 malformed rows give problem lines, never an error, and the table is unchanged: expected 2, got 0`. After: 13 + 2 usage passed.

## 2. Planted faults
| Fault | Caught by |
| --- | --- |
| no integer check | CT-T3 |
| duplicates need 3 users | CT-T2 (3 red) |
| no "missing in all rows" line | CT-T7 |
| `none` does not sort | CT-T6 |
| non-table row visited | CT-T1 (2 red) |
| a rule error escapes | each |

## 3. Line format (stable, for spec output)
`<row>.<field>: <value> <problem>`; a row is `'key'` or `[index]`; strings shown `'x'`, numbers as written, other values as `a table` (never an address); duplicates `<field> <value> used by rows <a>, <b>`; `none` errors with `<n> content problems:` and the sorted lines.

## 4. Open for the template (step 7)
The contract's usage requires `@framework/ContentTests/Check`; no such alias exists (REQUIRES.md: `@game`, `@self`, `@spec`, relative) and ContentTests has no place in the DataModel. The game's Lune specs need a path to `Framework/ContentTests/Check.luau` in the install: the template builder's or the lead's call.
