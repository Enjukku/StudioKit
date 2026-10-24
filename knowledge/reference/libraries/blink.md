---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
roles: [feature-builder, reviewer, architect, qa-lead]
---
> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24

# Blink (network code generator): package record

| Field | Value |
| --- | --- |
| Package | Blink, IDL compiler written in Luau, by 1Axen (`github.com/1Axen/blink`) |
| Version | **0.18.9**, published 2026-09-19 (last push 2026-09-23), checked 2026-10-24 (`research/net-signals-cleanup.md`) |
| Licence | MIT |
| Where pinned | toolchain, not a runtime package: `rokit.toml` `blink 0.18.9` in the framework and in each game (template); the generated `Remotes` modules (`src/server/Remotes.luau`, `src/shared/Remotes.luau`) are produced by `python tools/gate.py --transport`, never edited by hand |
| Used by | the game's one schema `net/game.blink` (framework messages in `src/Net/framework.blink`, imported `as Framework`); the Net block guards the generated server module |
| Probe | J025-P1 PASS for Blink, FAIL for Zap 0.6.x (`knowledge/jobs/J025-base-framework/probes/p1-transport/verdict.md`) |

## Why chosen
- One schema file is the single source of truth for both sides; generated typed code; buffers instead of Roblox's default encoding; receive-side checks of every declared type, range and bound (P1 T2: NaN, ±inf, oversize strings, arrays, buffers, bad enums, missing or wrong-class Instances all rejected).
- Newest release in its group; Zap failed P1 (ranged vectors asserted before read, `string.utf8` bounds counted as bytes, a silent `nil` enum). Closed door CD-1 keeps plain RemoteEvents and Networker out.

## Known gaps and how the framework covers them
G1-G10 (P1 §3 and Net CC-8): full table in `networking-security` §7. In short:

| Gap | Covered by |
| --- | --- |
| G1 unranged numbers, G2 `CFrame`, G4 maps, unbounded arrays, `Sync`/`Polling` client calls | schema lint `Framework-tools/Net/schema-lint.luau` (gate) + Net's finite walk |
| G3 no UTF-8 check | Net walk `utf8.len` |
| G5 no rate limit | Net per-handler rate + per-event allowance (CC-13) |
| G6 decode errors raise unguarded (log flood, heartbeat 16.7 → 42.3 ms) | deterministic patch `patch-generated.luau`: `pcall` per dispatcher, `SetGuard`, counted rejects, strikes, block |
| G7 Instance args: `typeof` + `IsA` only | the handler (ownership, N-02 step 4) |
| G8 listener-less queue without a cap | patch caps at 256 (`no_listener`) |
| G9 buffer allocated before the max check | accepted (≤ 65,535 bytes, freed at once) |
| G10 send entries for departed players | patch steps 5-6 |

## Update path
A new Blink version re-runs probe P1 first; the patch fails loudly (non-zero exit, names the anchor) when an anchor is missing or repeated, so the gate stops before a changed generator ships. Then regenerate (gate `--transport`: byte-compare), run Net's specs and `tests/acceptance/Net/`, move the pin in `rokit.toml` in a framework tag. Fallback: Zap only if a P1 re-run passes it (swap point: the generated `On`/`Fire` functions passed into blocks, `contracts/README.md` rule 2).
