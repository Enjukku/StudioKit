---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: J013 G2 test (SYNTHETIC TEST DATA, universe 9000000001)
supersedes: []
---
**SYNTHETIC TEST DATA.** Every file in this folder comes from universe 9000000001, which does not exist (`.tools/analytics-data/9000000001/README-TEST.md`). The JSON files are unchanged tool outputs and cannot carry this label inside them; this file labels them all.

> Author: analyst · claude-opus-5-5 · high · 2026-10-21

| Files | Made by | Rerun (from the repo root unless noted) |
| --- | --- | --- |
| `show-<Metric>.json`, `show-stderr.txt` | `python tools/analytics/analytics.py show --metric <Metric> --universe 9000000001` | same command |
| `maturity-all-cohorts.json` | `stats maturity --first-play <date> --n <1/7/30> --lag-days 1 --now 2026-10-21T12:00:00Z`, every cohort | loop in J013-T05b hand-back |
| `stats-diff-*.json` (+ `.stderr.txt`) | `stats diff --xa --na --xb --nb` with the counts in `derived-counts.json` `periods` | inputs are inside each file |
| `stats-did-*.json` | `stats did` per matched weekday, phone vs computer | args are inside each file |
| `derived-counts.json` | `derive_counts.py` (reads only `show-*.json`, `maturity-all-cohorts.json`) | `python derive_counts.py` from this folder |
| `ranges-other-metrics.json` | `ranges_other_metrics.py` (reads only `show-*.json`) | `python ranges_other_metrics.py` from this folder |
