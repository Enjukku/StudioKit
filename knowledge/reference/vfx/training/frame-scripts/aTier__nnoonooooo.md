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

# aTier__nnoonooooo · A · camera side, about 30 studs
Event: a small blue-violet energy ball idles at the centre, then pops into a white-blue starburst with electric spikes that shrinks back into the ball in about 600 ms.
Phases: idle 0-800 ms · pop 818 ms · decay 850-1530 · idle again
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-800 | not counted (idle ball sits in the median) | about 0.58-0.62 x, 0.4-0.5 y | small round ball with swirl texture, a few specks, blue floor glow | #8090E0, #B0B8F0 | low | slow spin |
| 818 (onset, peak) | 3.1 | 0.47-0.71 x, 0.34-0.72 y | white-blue starburst, about 10 sharp spikes, soft violet halo | #F0F4FF core, #7080E8 | 0.55 % near-white | pops in 1 frame |
| 848 | 2.3 | 0.52-0.68 x, 0.39-0.65 y | burst shrinking, wispy streaks | #9AA8E8 | 0.2 % | contracts |
| 905-1060 | 1.9-1.4 | 0.55-0.68 x, 0.39-0.62 y | blue wisps curling round the ball | #8A98D0 | 0 % | swirl |
| 1265 | 0.9 | 0.56-0.66 x | thin wisps | #8A96C8 | 0 % | fade |
| 1533 | 0.1 | ball only | idle ball | n/a | n/a | end |
Layers seen: ball 1, starburst spikes 1, halo 1, wisps ~5, floor glow 1.
Size vs character: no character; burst about 0.2 of screen width at peak, the ball is about 0.03.
What makes it look good:
- sharp spikes on a soft halo: a hard layer over a soft layer
- fast pop, slow decay (1 frame up, about 700 ms down)
- cool hue range (blue to violet) with one white-hot frame
Weak points:
- low coverage (3 %), small on screen, easy to miss at a distance
- the idle ball is not counted in coverage
