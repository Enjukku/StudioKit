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

# sTier__space_thingiemajig · S · camera side, about 30 studs
Event: a looping galaxy-cloud aura: a tall dark indigo mass full of star dust and leaf-like wisps, pulsing slowly (about 3 s cycle).
Phases: loop only; slow breathing, no windup or tail.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| 0 | 5.5 | x.38-.83 y.13-.95 | dense mass of ~100 overlapping leaf-shaped dark sprites, white-blue speckles in the middle | #2a2070, #4a3ab0, speckles #c0c8ff | peak_luma 198 | edge sprites drift |
| 1300 | 1.3 (min) | x.44-.81 y.06-.89 | same mass, more white nebula wisps on the right | #5a50c0 | peak_luma 235 | |
| 2942 | 5.3 | x.2-.84 y.06-.99 | wider, up to 0.64 screen width, edge sprites reach left | #3a2e90 | 236 | cycle repeats |
Layers seen: dark leaf sprites ~100, nebula glow clouds ~6, white speckle stars ~30, white wisps ~8.
Size vs character: mass is about 3-4 character heights tall (no character visible).
What makes it look good:
- Dark core with bright stars inside gives a space depth look; stylised sprite shapes, not soft fog.
- Slow pulse keeps the loop alive without flashing.
Weak points:
- Looping: most of the effect is in the median background, so coverage is low and nearly meaningless; use box and sheet.
