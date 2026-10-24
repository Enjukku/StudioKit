---
name: parallel-gate-and-planted-faults
description: Framework repo gate is shared by parallel block builders; planted faults on check rules find real gaps (J025-B3 Loader, 2026-10-24)
metadata:
  type: feedback
---

When several builders write src/<Block>/ in parallel, `python tools/gate.py` shows RESULT: FAIL from others' half-built blocks. Prove your own block clean per check (stylua --check src/<Block>, selene src/<Block>, luau-lsp on your files, lune run tools/spec/run.luau src/<Block>) and count gate problem lines per block.

**Why:** J025-B3: the whole-repo gate could not pass mid-stage; per-block proof plus a per-block count made the hand-back honest.
**How to apply:** report C1 as FAIL-from-others with the per-block count, never as PASS.

Planted faults per validation clause (not only per row) pay off: in the Loader, a survived fault exposed that `{ [1]="Save", [3]="Shop" }` passed the After check. A redundant clause shows up as a fault that survives: delete it.
