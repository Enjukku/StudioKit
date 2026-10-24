---
name: per-field-vs-per-call-bounds
description: Schema lints that bound each array alone miss nested/summed shapes; departed-sender branches that "allow" skip the flood bound under Deferred signals
metadata:
  type: feedback
---

When a lint enforces a per-array bound to match a per-call runtime budget (e.g. Net's 512-value walk), probe a nested shape (`T[..64][..64]`) and a tuple of two bounded arrays: per-field checks pass them, the runtime always denies them, and decode work is bought first. Also: any guard branch that returns "allow" for a sender already out of Players skips the per-event bound; under Deferred signals a pending OnServerEvent can resume after removal (deferred.md: pending handlers run after ancestry change). Prefer "refuse with no state" there.

**Why:** J025 Net r2 (2026-10-24): R1 fix bounded each array but a 64x64 grid passed the lint; maker's open weakness was the allow-true departed branch.

**How to apply:** On any lint or guard fix, run one scratch probe of the composed shape; for departed-player branches ask whether refusing loses anything. Related: [[batched-transport-flood]].
