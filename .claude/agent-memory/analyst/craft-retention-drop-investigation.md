---
name: craft-retention-drop-investigation
description: Craft lessons from the first deep retention-drop investigation (J013-T05b, 2026-10-21): reconciliation checks, overlapping events, mix split without per-source denominators
metadata:
  type: feedback
---

Before reading any segment rate, check the total lies inside the segments' min-max range on every day; a total below every segment means the split is incomplete or wrong. Also scan for identical series (two segments or metrics with equal values every day).
**Why:** in J013-T05b the platform D1 split could not contain the total on 13 days, tablet = console exactly, and four performance metrics were copies; a quick story would have used them.
**How to apply:** put the checks in the calc script (derive_counts.py pattern) and list each FAIL in the data-check table; use a failed split only for within-split comparisons, never levels.

When a marketing wave and a release overlap, the total hides the second step (the wave fading pushes the rate up). Read the release inside stable segments (usual sources) and with a per-weekday difference-in-differences plus a placebo week one week earlier.

Without new players by source, an "excess players" split from totals (extra new players and extra returners vs the same weekdays one week earlier) gives the mix effect; label it an estimate with its assumptions.

The stats tool has no weighted aggregation or mix adjustment: write a small script in calc/ that reads only the saved show files, and save its JSON. Run `stats maturity` for every cohort with a loop, and keep the tool's stricter reading if the API already returned the value.

Related: [[analyst-report-shape]]
