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

# sTier__FUGAAAA · S · camera side, about 30 studs
Event: a looping fire burst sits on a character: orange flames, burnt smoke. Loop only; the arrow animation is not replayed.
Phases: loop only, no clear windup or tail (flicker cycle about 0.8-1 s).
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| 0 | 1.8 | x.51-.73 y.38-.66 | ragged flame cluster, ~8 tongue shapes, dark smoke puffs at the sides | #ffb030, #ff6a10, smoke #503020 | peak_luma 244 | flicker |
| 374 | 2.6 (peak) | x.50-.74 y.36-.70 | flames taller and wider, bright yellow-white core streaks | #ffe070 core | bright 0.14% | puff outward |
| 736 | 1.7 | y.39-.63 | flatter, darker orange | #c07030 (mean 157,109,62) | dim | contracts |
| 857 | 1.55 | y.36-.64 | re-flare, yellow core | #ffd060 | bright 0.14% | |
| 1458 | 2.4 | | second re-flare | | | repeats about every 1 s |
Layers seen: flame tongues ~8, hot core 1, dark smoke puffs ~4, tiny embers ~10, faint light streaks 2.
Size vs character: flames about 1.5-2 character heights wide, about 1.5 tall.
What makes it look good:
- Hot yellow core with red-orange edges and dark smoke gives a layered fire.
- Flicker every about 1 s keeps it alive.
- Stylised swirling smoke puffs (cartoon), not soft fog.
Weak points:
- Coverage is low and flat because the loop is partly in the median background.
