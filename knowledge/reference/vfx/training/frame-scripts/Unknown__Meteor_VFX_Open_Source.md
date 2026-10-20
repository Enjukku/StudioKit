---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: frame-script agent · claude-sonnet-5-5 · medium · 2026-10-20

# Unknown__Meteor_VFX_Open_Source · ungraded · camera side, about 80 studs (no character; two small dark spheres far right as scale)
Event: a lava-rock meteor falls from the upper right with an orange spark trail and ring wisps, hits the floor and makes a flat orange ring, flame burst and dark cinders.
Phases: clip starts mid-effect (a previous meteor burning in the lower-left corner at 0-150 ms) · fall 300-1600 · impact 1700-2000 · cinders 2000-2600 · tail 2600-3600
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 13.9 (leftover from an earlier meteor, not this one) | 0-0.64 x 0.56-1.0 | big burning rock and flame ring at the lower-left edge, flames and sparks | #FF9030, #E04010 | peak_luma 229 | fading |
| 355 | 3.9 | 0.02-0.77 x 0.11-1.0 | cracked rock ball ~0.08 of screen width at top right, ringed by 2-3 thin pink-orange swirl lines, ~10 orange leaf-shaped sparks drifting down | #FFA060 rings, #FF5020 sparks | low | rock falls, sparks drop |
| 1079 | 2.6 | 0.10-0.83 | rock near the centre, trail of ~20 spark flakes above and behind | #E05030 | low | falling |
| 1788 | 3.7 | 0.39-0.75 x 0.20-0.80 | impact: orange flame bloom ~0.15 wide on the floor, orange ring around it, sparks rising ~0.2 of the screen | #FFC060 core, #E07020 ring | bright 0 | blooms up from the point of contact |
| 1961 | 4.4 (peak after start at 1961) | 0.34-0.70 | flat orange ring ~0.2 wide on the floor, dark cinders and smoke above a red ember crack | #FF8030 ring, #1A1A1A cinders | low | ring expands |
| 2514 | 0.6 | 0.34-0.65 | red ember cracks and a few dark specks on the floor | #7A3030 | none | fade |
| 3274 | 0.08 | small | faint scorch marks | #624A55 | none | near empty |
Layers seen: rock 1, swirl rings ~3, spark flakes ~25, flame bloom 1, ground ring 1, cinders ~15, scorch mark 1
Size vs character: no character; the rock ~0.08 of screen width, impact ring ~0.2
What makes it look good:
- Long falling trail of leaf-shaped sparks sells speed; impact is a clear hit with a ring and flame.
- Leftover scorch and ember cracks on the floor after the hit.
- Orange ring on the floor shows the blast radius.
Weak points:
- Impact peak is only ~4% of the screen with no bright flash (bright_pct ~0) and no screen shake or smoke body.
- Clip starts in the middle of an earlier effect, and the first frames mix two meteors; coverage 0-300 ms is not this meteor.
