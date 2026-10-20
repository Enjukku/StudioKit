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

# cTier__blue_pewpews_E · C · camera side, about 35 studs (character ~9% of screen height)
Event: blue energy bolts leave from above the dummy in wobbly curved paths across the screen to the left floor, ending in a blue pile of squares.
Phases: idle 0-1000 ms · launch 1000-1700 · travel 1700-3000 · impact pile 3000-4100 · slow fade 4100-6000
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0-800 | 2.15 (dummy and dim floor glow, constant) | 0.39-0.81 x 0.49-0.64 | dummy | dark blue | none | still |
| 1226 | 1.8 | 0.41-0.86 x 0.32-0.62 | 2 small blue blobs above-right of dummy, one thin line | #3060FF | soft | blobs rise |
| 1843 | 2.2 | 0.41-0.93 | 4 glowing blob orbs in an arc, 3 thin wavy line trails | #4070FF blobs, #80A0FF lines | peak_luma 234 | orbs fly left along curves |
| 2825 | 2.6 | 0.47-1.0 x 0.33-0.79 | 3 long thin wavy trails, ~5 blob orbs right, pile of blue cubes on floor left | #2850E0, #6080FF | soft | trails sweep left, floor glow patch grows |
| 3228 | 3.9 (peak) | 0.43-1.0 | trails fading, cube-shard pile of ~12 squares, ~10 orbs | #3868F0 | low | pile jitters |
| 3900 | 3.3 | 0.35-0.98 | pile of squares, 3 stray squares lower left | #4070E0 | low | shards settle |
| 5000 | 1.4 | 0.34-0.81 | small blue glow pile | #3060C0 | low | slow fade |
| 5821 | 0.5 | 0.35-0.82 | faint pile | #2848A0 | none | near static |
Layers seen: glow blob orbs ~6, wavy line trails 3, square shards ~15, floor glow patch 1
Size vs character: whole pattern ~8 character widths long; each orb ~0.5 heights
What makes it look good:
- Single blue hue is coherent.
- Curved trails give each shot a readable path.
Weak points:
- Square shards read as low-poly debris, not a magic impact; no flash or ring at the landing spot.
- Never above 4% of screen; no bright core (bright_pct max 0.014).
- Impact lingers about 3 s with no clear peak.
