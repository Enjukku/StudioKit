---
name: lune-bench-and-shared-scratch
description: Lune micro-bench under luau.load custom environment is ~3x slow (builtins deopt); parallel builders share one scratchpad, use an own subfolder (J025-B1, 2026-10-24)
metadata:
  type: feedback
---

Two facts from J025-B1 (2026-10-24, Lune 0.11.1):

- `luau.load(src, { environment = {...} })` (the framework spec runner) turns off Luau's builtin fast paths:
  `Ledger.record` on 100 ids cost 26-30 µs there and 8.4-8.7 µs loaded without `environment`. Loop-light code
  (`take`, `whole`) barely changes. Luau `collectgarbage("collect")` is invalid; `gcinfo()` delta over an
  allocation-free loop is exactly 0 (the GC only steps on allocation), so assert 0.
- Parallel builders spawned by one lead share the same scratchpad folder; another builder overwrote my `plant.py`
  mid-run. Keep scratch files in `scratchpad/<ticket-id>/` with ticket-named scripts.

**Why:** a budget check measured through the runner's environment would have reported a false over-budget; a shared
script name silently ran someone else's fault planter.
**How to apply:** Q6 numbers: bench pure modules loaded without `environment` (say so); planted-fault and bench
scripts go in a ticket subfolder. Related: [[roblox-toolchain-probes]].
