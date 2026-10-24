---
name: memory-oracle-lune
description: "No per-call state" checks in Lune specs: a gcinfo() delta is flaky; read the live heap after forcing a full collector cycle (J025-Q3, 2026-10-24)
metadata:
  type: feedback
---

A peak `gcinfo()` delta around a loop missed a planted per-call string in one matrix run: the collector freed garbage from earlier specs during the measurement. Read the live heap instead: allocate short-lived garbage worth 3x the current heap (forces at least one full incremental cycle) and keep the lowest reading, before and after the loop.

**Why:** measured on the Admin flood spec: clean -48..0 KB vs planted ~520 KB per 5,000 calls with the forced-cycle reading; the plain delta was not reliable.

**How to apply:** size the loop so one retained table/string per call is at least 2x the limit (10,000 calls, 128 KB limit); always run the full plant x spec matrix more than once before freezing, a memory plant that is caught once can still be flaky. Related: [[planted-faults-session-fakes]].
