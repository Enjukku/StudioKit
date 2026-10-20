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

# cTier__the_circle_thingie_E · C · camera side, about 35 studs (character ~9% of screen height); sky tint changes a lot
Event: blue flames rise around the dummy and a glowing ring spreads on the floor; the whole sky shifts through blues and violet while it plays.
Phases: idle 0-800 ms · flame rise 800-1400 · tint plateau 1400-3400 · violet burst 3400-4300 · fade 4300-5300 · tail dots 5300-7000
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0-600 | 0.16 | at dummy | dummy | - | none | still |
| 1061 | 8.2 | wide, 0.29-1.0 height | 4 jagged blue flame tongues round the dummy | #3050FF, #8090FF centre | peak_luma 245 | flames flick up |
| 1262 | 12 | wide | flames ~1.3 heights tall, small octagon ring on floor | #4060FF | bright 0.017 | rising |
| 1856 | 33.6 | whole width | flames ~1.5 heights, floor ring with dark octagon plates, brighter blue sky | #4070FF flames, sky #2B87F4 | soft | flicker |
| 3488 | 2.5 | 0.63-0.82 | flames short | #3848B0 | low | sky back to normal |
| 3897 | 35 (peak 43.9 at 3831) | whole width | flames soft violet, octagon ring flat on floor | #8A78FF flames, sky #5560FF | glow | sky tint jumps again |
| 4107 | 7.0 | 0.61-0.88 | flames ~1.2 heights, a few sparks drift up | #6870FF | peak 255 | thins out |
| 4732 | 0.3 | 0.67-0.79 | ring only, dim | #2A3C90 | none | fades |
Layers seen: flame tongues ~4, floor ring 1, sparks ~8, whole-sky tint 1
Size vs character: flame column ~1.5 heights; ring ~3 character widths
What makes it look good:
- One coherent blue/violet palette.
- Floor ring anchors the flames to the ground.
Weak points:
- 25-35% of the coverage is sky tint; the visible effect is only ~3% of the screen. Metrics overstate.
- Flames are low-res with no bright core, no ring wave, small in frame.
- Tint changes every few frames with no event behind it.
