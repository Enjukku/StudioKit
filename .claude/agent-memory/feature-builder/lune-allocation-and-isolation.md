---
name: lune-allocation-and-isolation
description: Lune spec craft - how to measure allocations reliably with gcinfo and keep leak-count specs from cascading
metadata:
  type: feedback
---

Measure hot-path allocation in Lune with `gcinfo()` max growth over ~10,000 calls, run BEFORE any big timing loop; `collectgarbage("collect")` is not allowed in Luau, and a delta taken after a 100k-call loop hid a planted one-table-per-call fault (the collector was mid-sweep). Leak specs on module-level counters take a per-test baseline (`since()` closure), never absolute zero, or one red test reddens every later one.

**Why:** J025-B5 (Anim, 2026-10-24): planted fault F9 survived the first Q6 spec; cascades from absolute-zero checks made planted-fault results unreadable.
**How to apply:** any framework block's Q5/Q6 Lune specs; always run planted faults one at a time and check each red set is the row it targets.
