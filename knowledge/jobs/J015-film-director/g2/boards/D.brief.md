---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J015-T09 G2 test"
supersedes: []
---
> Author: film-director · claude-opus-5-5 · high · 2026-10-21. Template: `templates/film/storyboard-brief.md`.
# Storyboard brief: boss-reveal shot D rev 2

| Field | Fill in |
| --- | --- |
| Project and revision | kit test J015 G2, `boss-reveal`, shot D, shot-list revision 5, panel revision 2 |
| Approved visual references | image 1 = previs frame 124 from `CAM_D` (`.../board_inputs/D_layout.png`); image 2 = panel `boss-reveal-p1-r1` |
| Story purpose | the statue the player walked past is alive, holds the beacon's light (amber eyes) and has seen them |
| Character intention | guardian: wakes, finds the intruder |
| Composition | guardian right, upright, head in the moon shaft; explorer small far left; dark beacon and the exit between them |
| Shot size and angle | wide, low near the water (chosen so beacon, explorer and risen head share one fixed frame) |
| Continuity constraints | guardian faces screen left, looks down left; explorer seen from behind, facing right; beacon dark; moon from above |
| Action moment | +50 (frame 124): gaze has landed on the explorer |
| Camera change | none (static); tilt alternative documented in `previs/shotD_static_vs_tilt.png` |
| Lighting and colour | brightest: the lit head and amber eyes; exit secondary |
| UI and crop | 16:9; explorer, beacon, head, eyes inside the 4:3 centre (measured 22/22 sampled frames) |
| Exclusions | exactly one statue, one explorer; no glowing beacon |
| Acceptance test | at thumbnail size: two amber eye points, the head in the light, the explorer small at left |
| Unresolved | guardian design; eye glow size (VFX brief) |

## Manifest rows
`boss-reveal-d-r1` (rejected), `boss-reveal-d-r2` (edit: change only the beacon). This was image 8 of 8: no regeneration left.

## Review
| Check | r1 | r2 |
| --- | --- | --- |
| Story purpose readable | pass | pass |
| Identity | pass | pass |
| Screen direction and eyeline | pass | pass |
| Prop, landmarks, light | **fail**: beacon glowing bright (prop state) | pass for the beacon. Two open defects: an amber reflection on the water at lower left is left over from r1's glow; the eyes are drawn as a cluster of four points, not two |
| Subject at small size | pass | pass (the eye cluster still reads as glowing eyes) |
| Continuity with next panel | fail (beacon) | pass |
| Decision | regenerate (1 of max 2) | **accept with the two defects written down**; previs and the VFX brief govern the eyes; no budget for a third image |
