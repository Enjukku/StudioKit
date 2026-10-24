---
name: release-mark-discriminator
description: A "release pending" mark cleared on ProfileStore OnAfterSave is also cleared by earlier in-flight saves; a data-compare clear strands it after a stolen release. Probe both before ruling.
metadata:
  type: feedback
---

When a fix waits for "the release landed" over ProfileStore 1.0.3, check what fires the clearing signal. OnAfterSave fires for every landed save (vendor :924), IsActive is already false for all of them after EndSession, and the per-key FIFO queue makes an in-flight autosave or receipt save land just before the release's first attempt.

**Why:** J025 recheck r2 (2026-10-24). Probe P1 proved the early clear: a receipt save in flight at leave, then a failing release and a same-server rejoin lost the last update (143 to 142). The obvious fix (clear only when lastSaved deep-equals the data at leave) passed P1. Probe P2 showed it strands the mark when the release lands on a record another server stole (rejoin degraded at 120 s, connection leaked).

**How to apply:** for any "wait until X landed" mark over a vendor signal, write two probes: an early fire from another source, and the case where the awaited event lands but means something else (stolen, overwritten). Rule a fix complete only when both are green. See [[same-server-rejoin]], [[end-path-callers]].
