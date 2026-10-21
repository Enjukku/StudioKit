---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J005-T10 (character-rigger S2 on the teddy, first real run of the rig workflow)
supersedes: []
---
> Author: character-rigger · claude-opus-5-5 · high · 2026-10-21

# Lessons: rigger S2 on a merged Tripo plush (teddy)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | A plane search that maximised "crease cover" picked cut planes that cut through the arm tube or ran into the head; mirroring the left plane to the right side gave a ring through the head | Define limb cuts from named landmarks (armpit valley, front and back crease points, outer top point; crotch, belly crease, seat fold), not from an optimiser; flood-fill the part from a seed inside the half-spaces, because cut planes are infinite and catch far geometry | output/rigs/teddy/s2/scripts/analyze_s2.py (crease_landmarks, grow()) |
| 2 | Labelling parts by "positive side of the plane" put the outer thighs on the arm and gave a long torn sheet in the posed proxy | A part = the connected region on the far side of its cut that contains the part's own seed; check per-part vertex counts before posing | s2/proxy/compare_shoulder/A_ring_top_0p644__SP3_front.png (before the fix) |
| 3 | The posed proxy (faces split by label in memory, grey spheres as root stand-ins, Z1 linear blend) answered questions the plan alone could not: the seat reaches the floor at -0.16 not -0.22, the tail cannot clear the floor at the §B rock-back, the head rim meets the shoulders at roll 10 | Run a cheap rigid-by-label proxy of every stress pose at S2, before briefing the modeler; give the animator contact onsets and floor numbers as limits | s2/proxy/proxy_measures.json |
| 4 | Signed-distance "penetration depth" on open, split parts gave nonsense (head "inside" the trunk at its top) | Use BVH overlap between posed parts with the faces next to the shared cut removed (rest gap), and report onset angles; do not report depth on open shells | proxy_measures.json sweeps_single_axis |
| 5 | The bandages looked like raised cuffs in the renders but the geometric lip was 0.001-0.004 units | Measure a cover before relying on it: colour edges are a visual seam line, not a socket; say which kind of cover each cut has | inventory.json cuts.wrist_*.bandage_lip_step |
| 6 | 295 of 297 stitch strips were open single-sided strips (1,281 of 1,301 open edges) | On generated plush models, count open edges per island: decoration strips break the watertight and volume rules and must be closed at S3 | inventory.json mesh |
| 7 | Roblox clips have no scale channel (CurveAnimation: Position and Rotation; Pose: CFrame) | Answer every "squash" need as not supported for scale, or as a bone translation with a stated travel and where it lands | CurveAnimation.yaml:24-30, Pose.yaml:13 |
| 8 | Shoulder variant A (shoulder cap goes with the arm) opened a gap next to the collar; variant B (chest keeps the cap) kept the arm seam 0.08 below the head seam | Keep neighbouring seams apart; prefer a cut where the static part's overhang covers the moving part's root | s2/proxy/compare_shoulder/AB_grid.png |
| 9 | Blender headless resolved relative output paths away from the shell's working directory | Pass absolute paths to headless Blender scripts | this task (renders missing on the first run) |
