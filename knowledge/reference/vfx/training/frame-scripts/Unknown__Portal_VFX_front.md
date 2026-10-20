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

# Unknown__Portal_VFX_front · ungraded · camera front, about 25 studs (no character; the portal is ~0.25 of screen width, ~35-45% of screen height)
Event: the same looping portal seen from the front: a blinding white core in a ball of black ink smoke, blue lightning arcs, dark orbit rings and blue dots.
Phases: looping, no windup or end.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 7.4 | 0.44-0.81 x 0.07-0.80 | white core ~0.15 wide, black smoke ball ~0.3 wide, a column of smoke rising above, blue arcs round the core | #FFFFFF, #3C70FF, #05080A | peak 253, bright 0.11 | boiling |
| 552 | 7 | 0.08-0.86 | wide thin dark orbit rings to the left, 6 blue dots | #4070FF | bright 0.37 | rings circle |
| 1084 | 7.9 | 0.37-0.97 | rings to the right, white core ~0.14 wide, blue squiggles on top | #FFFFFF | bright 0.31 | rings turn |
| 1619 | 7.7 | 0.27-0.83 | smoke ball dense, ~10 blue dots, arcs bright | #A0C0FF arcs | bright 0.32 | pulse |
| 2142 | 7.2 | 0.18-0.95 | rings left and right, core steady | #FFFFFF | bright 0.30 | turning |
| 2499 | 8.8 (peak 2469 ms) | 0.27-1.0 x 0.13-0.97 | large orbit ring over the right, smoke chunks | #FFFFFF | bright 0.35 | sweep |
| 2850 | 7.6 | 0.28-0.87 x 0.01-0.97 | smoke above and below | #FFFFFF | bright 0.57 | loop |
Layers seen: white core 1, black smoke mass (about 15 pieces), lightning arcs ~10, orbit rings 2-3, blue dots ~10, squiggles ~6
Size vs character: no character; portal ~0.25 of screen width, rings ~0.7
What makes it look good:
- Pure-white core against black smoke gives the strongest contrast of any clip.
- Irregular ink-smoke edges: anime style.
Weak points:
- Metrics unreliable for a loop; the thin orbit rings change the box width from frame to frame.
- Black smoke has no floor shadow or glow, the portal floats.
