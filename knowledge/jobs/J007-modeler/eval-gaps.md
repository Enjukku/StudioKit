---
type: log
scope: universal
status: active
updated: 2026-10-21
source: J007-T10, J007-T11 (hidden test), build-agent step 5
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Hidden test: gaps found and what changed

Result before fixes: 4 of 6 cases passed (grades-hidden.md). H2 and H6 failed one must line each. The lead read the answer key to fix the gaps, so **this hidden set is now spent**: it cannot be used again as a blind test of these skills.

| id | case | gap | fix | file | status |
| --- | --- | --- | --- | --- | --- |
| EG01 | H2 (must failed) | comparing revisions and reference views without one matched camera, projection and lens per view | review §3: render every revision in the same camera, projection and lens as each reference view; repair at the first differing revision | modeling-design/references/review.md | fixed 2026-10-21 |
| EG02 | H6 (must failed) | style fit judged on palette and value only; no number for shape, edge, roughness, detail scale | review §3: axis-by-axis numbers vs approved neighbours (look_check value, palette, silhouette; bevel share; mean roughness; smallest readable feature); range from approved models | modeling-design/references/review.md | fixed 2026-10-21 |
| EG03 | H3 (line failed) | no re-test of every required pose in Blender and Studio after a geometry fix | rig-parts step 12: list touched poses, rigger re-runs S4 through every pose and S5 tests; weights never hide a fused bridge | modeling-craft/references/rig-parts.md | fixed 2026-10-21 |
| EG04 | H1 (weak) | silhouette check had no number | review §2 identity row: `look_check silhouette --compare` at the same camera | modeling-design/references/review.md | fixed 2026-10-21 |
