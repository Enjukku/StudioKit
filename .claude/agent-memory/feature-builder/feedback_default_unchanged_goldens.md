---
name: default-unchanged-goldens
description: How to prove "output unchanged without the new flag" for kit tools when other chats edit the repo in parallel
metadata:
  type: feedback
---

Record golden outputs with the OLD tool on a checked-in fixture repo before the first edit, then also diff `git show HEAD:<tool>` against the new tool on the live repo (same tree, same moment).

**Why:** J016-T01 (2026-10-21): live-repo before/after files differed only because parallel chats added notes; the HEAD-vs-new run (15/15 identical) and fixture goldens were the real proof. Same for gate drift: old and new `sync_harness --check` gave the same report, so the drift was not mine.

**How to apply:** any brief with "byte-identical when the flag is absent" or "must not change default behaviour". Also: for never-fail hooks, assert a normal skip writes nothing to stderr, or the catch-all hides a removed check (planted fault survived until then). See [[planted-faults-unequal]].
