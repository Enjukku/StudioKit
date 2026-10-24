---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B2
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Config: Q1-Q9 evidence (J025-B2)

Files: `roblox-game-framework/src/Config/init.luau`, `Config.spec.luau`, `Config.engine.spec.luau`, `test/FakeConfig.luau`. Contract: `contracts/Config.md` (2026-10-24). Lune 0.11.1, luau-lsp 1.70.1 (new solver).

| Q | Result | Evidence |
| --- | --- | --- |
| Q1 | pass | 6 functions, as the contract: `start`, `number`, `boolean`, `string`, `json`, `override`; exported type `Key` |
| Q2 | pass | `--!strict`; luau-lsp 0 errors on `init.luau`, `test/FakeConfig.luau`, `Config.engine.spec.luau`; grep `any` in `init.luau` = 0 |
| Q3 | pass | rows below; planted faults 9/9 red (table 2) |
| Q4 | pass | every failure row of the contract has a spec (table 1, C-T1, C-T2, C-T4) |
| Q5 | pass | no per-player state; one server-lifetime `UpdateAvailable` connection. Spec "Q5 1,000 updates keep one UpdateAvailable connection": 1 listener after 1,000 publishes. Warn sampler tables are bounded by the declared key count + 1 |
| Q6 | pass (Lune); engine not verified | read 0.105 µs (median of 3 × 1e6 calls, spread 0.104-0.116 s), 0.0 KB over 1e5 reads (screening: `collectgarbage("count")`), no engine call (C-T3 spec). Refresh of 100 keys 0.066 ms (3 × 100). Budget ≤ 1 µs / ≤ 1 ms. Allocation only on refresh: one table + one closure per key |
| Q7 | n/a | no client input; server only (C4: `start` errors unless `RunService:IsServer()`), placed in ServerScriptService (`tools/placement.json`) |
| Q8 | pass | built on ConfigService (table 3); own code adds declared kinds, defaults, limits and non-throwing reads (the engine has none) |
| Q9 | pass (type-checked), run not verified | usage example is the `beforeAll` + "Q9 usage" case of `Config.engine.spec.luau`; `Amount.whole` replaced by `math.floor` (Helpers is another block) |

## 1. Contract test rows → specs (`Config.spec.luau` unless marked)
| Row | Spec name(s) |
| --- | --- |
| C-T1 | "before the first load every read is the default; after the load, the live values"; "a key not set live reads its default, quietly"; "the first load fails: defaults stay, retries at 2, 4 and 8 s, then one warn"; "the load fails twice then succeeds" |
| C-T2 | "wrong type, out of range, too long or failing check: the default and one warn naming each key"; "a number above max, below min, NaN or inf is refused"; "string length counts characters, not bytes"; "a check that errors refuses the value, never throws"; "the same bad value over many refreshes: at most one warn per key per 10 s" |
| C-T3 | "a getter of the wrong kind or an undeclared key errors"; "reads never yield and never call the engine"; "a bad declaration errors at start, naming the key"; "start runs once" |
| C-T4 | "UpdateAvailable: every key switches in one step" (a GetValue spy reads mid-rebuild: still the old value); "Refresh throwing keeps the old values, with a sampled warn"; "a json value is frozen" |
| C-T5 | "start on the client errors" (no GetConfigAsync call) |
| C-T6 | Lune: "(logic) override outside Studio errors"; "(logic) override in Studio sets and clears a testing value, through the same checks". Engine: `Config.engine.spec.luau` "C-T6 in Studio, override sets and clears a ConfigService testing value" (written, not run) |
| C-T7 | `Config.engine.spec.luau` "C-T7 no config published: reads are the defaults, never throw, never yield" (written, not run) |

Red run before code (stub returning 0/false/""/nil): `specs: 1 files, 1 passed, 19 failed`, e.g. `FAIL src/Config/Config.spec.luau:51: C-T1 before the first load every read is the default; after the load, the live values: expected 1, got 0`. After: 20 passed, 0 failed.

## 2. Planted faults (one at a time, restored after; `lune run tools/spec/run.luau src/Config`)
| Fault | Caught by |
| --- | --- |
| drop the `max` limit | C-T2 (3 specs red) |
| rebuild writes into the live cache (`read = values`) | C-T4 one step |
| two retries instead of three | C-T1 retries |
| no warn sampling (`WARN_EVERY_SECONDS = 0`) | C-T2 sampled (2 red) |
| no server check | C-T5 |
| no Studio check on override | C-T6 |
| json value not frozen | C-T4 frozen |
| live value used without its rule | C-T2 (5 red) |
| an unset key warns | C-T1 quiet default (2 red) |

## 3. Engine features and docs read
`_api-reference/classes/ConfigService.yaml:52-64` (GetConfigAsync yields; throws when nothing ever loaded), `:30-50` ClearTestingValue, `:107-130` SetTestingValue (GetValue returns the testing value); `ConfigSnapshot.yaml:72-93` GetValue, `:119-137` Refresh (no Yields tag), `:138-150` UpdateAvailable; `RunService.yaml:44-100` context table (Edit: IsServer true), `:554-579` IsServer, `:580-590` IsStudio; `production/configs.md:60-83` (types, limits in characters, staged values Studio-only).

## 4. Decisions inside the contract (builder's call, for the reviewer)
- Unset key (`GetValue` nil) → default with no warn; a `GetValue` error → default + sampled warn. Docs silent on what GetValue does for a key that was never created: C-T7 / a probe settles it.
- `override` re-reads all keys from the snapshot after Set/Clear (the engine does not say SetTestingValue fires UpdateAvailable). Before the first load it changes only the engine value (C1 keeps defaults).
- String `maxLength` counts characters (`utf8.len`), as `configs.md:72` does; invalid UTF-8 is refused.
- Declaration checks at `start`: unknown kind or field, non-finite or crossed min/max, maxLength not a whole number ≥ 0, json without `check`, a default that breaks its own rule → error naming the key. Defaults and live json tables are deep-frozen (one value shared by every reader).
- After the 4th failed load, one warn; no retry until restart (no snapshot means no UpdateAvailable to listen to), as the contract's failure table says.
