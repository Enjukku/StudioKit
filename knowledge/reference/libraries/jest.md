---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
roles: [qa-lead, feature-builder, studio-operator]
---
> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24

# Roblox Jest (engine test lane): package record

| Field | Value |
| --- | --- |
| Package | Jest for Luau by Roblox (`roblox/jest`, `roblox/jest-globals`; repo Roblox/jest-roblox) |
| Version | **3.20.1** (Wally; 3.21.0 is not on the index), checked 2026-10-24 in probe J025-P3 (`knowledge/jobs/J025-base-framework/probes/p2-5-engine/verdict.md`) |
| Licence | MIT (`research/shape-test-tooling.md`; dependency folders such as `roblox_chalk-lua`, `roblox_symbol` carry MIT LICENSE files) |
| Where pinned | framework `wally.toml` `[dev-dependencies]` `Jest`, `JestGlobals` = 3.20.1; `DevPackages/` (51 packages); dev only, never in a game place |
| Used by | the Studio engine lane: `*.engine.spec.luau`, run by `tools/engine/run_jest.luau` pasted into MCP `execute_luau`; the gate only lists engine specs |

## Why chosen
Roblox's own Jest runs inside the engine, so it can prove what Lune fakes cannot (TweenService, Animator, ConfigService fallback, DataStore with a `test_` prefix). `jsdotlua/jest-lua` 3.10.0 (2024-12-23) is the older community fork, used only if `roblox/jest` fails.

## Known gaps and how the framework covers them

| Gap | Covered by |
| --- | --- |
| Needs `loadstring`: a play-test Server run fails (`loadstring() is not available`) | Edit data model through MCP is the default lane (0.42 s for 6 specs); a Server run needs `ServerScriptService.LoadStringEnabled = true`, set only in the test project through Rojo `$properties` (NotScriptable) |
| No CI runner without Open Cloud Luau Execution | lane run through Studio MCP before merge; Open Cloud lane BLOCKED (P2: no API key) |
| Type definitions | a Jest-types negative control in the gate (framework `CHANGELOG.md`) |
| Not a substitute for multi-client checks | Studio multi-client lane (`testing` §8) |

## Update path
Bump `roblox/jest` and `roblox/jest-globals` together; re-run the engine specs in Edit and Server data models; new framework tag. Replacement cost: the engine spec files (Jest globals) and `run_jest.luau`.
