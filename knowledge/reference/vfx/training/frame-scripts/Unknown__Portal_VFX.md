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

# Unknown__Portal_VFX · ungraded · camera side, about 25 studs (no character; the portal is ~0.25 of screen width, ~35% of screen height)
Event: a looping portal: a blinding white-blue core inside a mass of black ink smoke with blue lightning arcs, thin dark orbit rings and glowing blue dots flying off.
Phases: looping, no windup or end. 0-3000 ms steady, only shapes change.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 6.4 | 0.43-0.82 x 0.18-0.74 | white core blob (jagged edge) ~0.14 wide, black smoke ring ~0.3 wide, thin blue lightning round the core, 2 dark orbit rings | #FFFFFF core, #3C6CFF arcs, #05080A smoke | peak 255, bright 0.43 | core boils |
| 534 | 6.9 | 0.13-0.87 | smoke puffs thrown up, blue arcs, wide orbit rings (~0.5 wide), ~8 blue dots | #4080FF dots | bright 0.3 | orbit rings sweep |
| 1071 | 8 | 0.29-0.99 x 0.05-0.88 | ring flares to the right, ~10 blue dots, small blue squiggles | #3050FF | bright 0.34 | rings turn |
| 1609 | 6.9 | 0.17-0.90 | dark smoke chunks lifted above, blue squiggles | #A0C0FF | bright 0.49 | puffs rise |
| 2146 | 7.3 | 0.14-0.84 | core square-edged, arcs round it, smoke | #FFFFFF | bright 0.74 | pulse |
| 2873 | 6.7 | 0.35-1.0 | orbit ring crossing the right, bright core | #FFFFFF | bright 0.19 | loop |
Layers seen: white core 1, black smoke mass 1 (about 15 pieces), lightning arcs ~8, orbit rings 2-3, blue glow dots ~10, blue squiggles ~6
Size vs character: no character; the portal is about 0.25 of screen width; rings reach ~0.6 of screen width
What makes it look good:
- Extreme contrast: pure-white core against black smoke, so it reads at any distance.
- Black ink smoke has an irregular, hand-drawn edge: anime style.
- Blue arcs and dots add motion in a second colour.
Weak points:
- Metrics unreliable for a loop: part is in the median background; box width moves ±0.3 between frames because of thin rings.
- Black smoke on a sky background is heavy; the portal has no ground contact.
