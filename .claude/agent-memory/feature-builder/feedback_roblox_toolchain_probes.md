---
name: roblox-toolchain-probes
description: Measured Roblox toolchain facts (2026-10-24): wally install wipes Packages/, luau-lsp resolves string requires on disk, selene std roblox refreshes each run, Lune chunk names
metadata:
  type: feedback
---

Probe the toolchain before fixing a layout or a gate on it; four facts from J025-S2 (2026-10-24, wally 0.3.2,
luau-lsp 1.70.1, selene 0.32.0, Lune 0.11.1, Rojo 7.7.1, Windows):

- `wally install` deletes everything inside `Packages/` (a `Packages/Framework/` copy vanished). Never put our own
  code under Packages/, ServerPackages/ or DevPackages/.
- `luau-lsp analyze` resolves string requires (`require("../../vendor/X")`) on the file system, even with
  `--sourcemap`. Keep the disk layout identical to the DataModel layout (siblings on disk = siblings in the project).
- `.luaurc` `languageMode: strict` also makes vendored nonstrict files strict (hundreds of errors in ProfileStore);
  rely on the `--!strict` header plus a header check instead. Studio ignores `.luaurc`.
- selene `std = "roblox"` regenerates its cached std on every run (network); pin it: `selene generate-roblox-std`,
  rename `name:` and the file, point `std` at it. Its `assert` needs a message unless you edit the std.
- Lune error chunk names are absolute paths without `.luau`, with backslashes; luau-lsp exits 0 on lint warnings,
  1 on type errors; stylua `--output-format=json` still exits 1 on a mismatch; Rojo ignores `.py` files in a `$path`.

- S2b additions: luau-lsp resolves `require("@game/<Service>/...")` through the sourcemap with full types (the
  cross-service require form); Lune 0.11 has NO global `task` (inject `@lune/task`) and `luau.load(src, {debugName =
  "@path", environment = {require = ...}})` gives clean `path:line` errors plus a custom Roblox-style resolver;
  Blink 0.18.9 fails with "not a terminal" when an output folder is missing; wally-package-types errors on a second
  run (stamp it); a Jest-heavy luau-lsp run costs 10-50 s on a loaded machine, so split it into a parallel process.

**Why:** each of these silently broke one design choice before the probe (install location, require paths, gate
network rule).
**How to apply:** for any gate or repo skeleton, run a 1-minute probe per tool assumption in the scratchpad first.
Related: [[vendor-facts-measure-first]].
