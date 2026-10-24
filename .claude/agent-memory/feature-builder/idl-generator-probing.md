---
name: idl-generator-probing
description: How to judge a network IDL generator (Blink, Zap): read the generated deserializer and feed it crafted buffers offline in Lune; vendor docs were wrong twice (J025 P1, 2026-10-24)
metadata:
  type: feedback
---

Judge a code generator by its generated output, never its docs, and run the generated receive handler offline before Studio.

**Why:** J025 P1 (2026-10-24): Blink docs show bounded maps, the 0.18.9 parser has none; Zap 0.6.29 docs list ranged vectors, its output asserts on the field before reading it (every packet errors); Zap output is `--!nocheck` (analyze "passes" trivially) and not deterministic across runs. None of this was visible in the docs or the research sheet.

**How to apply:** for any generator: (1) analyze output, and if the header is `--!nocheck` force `--!strict` on a copy; (2) regenerate 5x with the output deleted to test determinism; (3) load the generated server module in Lune via `@lune/luau` `load(src, {environment=...})` with stub services and `@lune/roblox` datatypes, call the captured `OnServerEvent` handler with hand-built buffers (NaN, inf, oversize, wrong type, missing Instance, batch ok-bad-ok). Harness pattern: J025 `probes/p1-transport/offline/run_receive.luau`. Related: [[studio-probe-before-claims]]
