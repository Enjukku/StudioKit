---
name: reference-mirror-search-tips
description: Tool quirks when searching the Roblox docs mirror (Glob/Grep) and where animation/physics facts live (J006)
metadata:
  type: reference
---

- Glob with a pattern that starts at a subfolder fails when `path` is the subfolder with backslashes. Use `path` = repo root and a forward-slash pattern: `knowledge/external/roblox-creator-docs/<dir>/*.md`. `**/Name*.yaml` with path inside `_api-reference` works.
- Grep: `head_limit: 0` means unlimited (burned tokens on terrain.md). Grep for `Tween` case-sensitively; `tween` matches "between".
- Long table lines show as "[Omitted long matching line]" in Grep; open them with Read (offset/limit) instead.
- API names differ from guesses: Workspace property is `ClientAnimatorThrottling` (type `ClientAnimatorThrottlingMode`); `BulkMoveTo` lives on `WorldRoot.yaml`; Prismatic properties live on `SlidingBallConstraint.yaml`.
- Server-tween replication, Humanoid/animator cost and physics mitigations are all in `performance-optimization/improve.md` (lines ~240-285, 475-526). Sleep and wake rules: `physics/sleep-system.md`.
- Kit fact-check ids `RT01-RT33` already exist in `knowledge/reference/animation/02-blender-roblox-process.md`; J006-T03 used `RT<q>-<n>` to avoid a clash.
