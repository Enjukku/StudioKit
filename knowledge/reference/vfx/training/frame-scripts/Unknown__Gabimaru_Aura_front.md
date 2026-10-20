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

# Unknown__Gabimaru_Aura_front · ungraded · camera front, about 20 studs (character ~25% of screen height, seen side-on and narrow; a large cracked lava-rock ball stands behind, left of it, ~14% of screen width, part of the scene)
Event: a looping aura: a thin magenta-pink glow hugs the character outline and orange flame flecks flicker off the head and shoulders.
Phases: looping, no windup or end. 0-3000 ms steady state.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 0.65 | 0.58-0.66 x 0.33-0.66 | magenta rim on both sides of the body, ~10 orange flecks near the head | #FF50C0 rim, #FF9030 flecks | peak_luma 236 | flecks pop |
| 557 | 0.7 | 0.58-0.66 x 0.34-0.68 | white and pink dots at the waist and hands | #FFB0E0 | low | flicker |
| 1115 | 0.55 | 0.58-0.65 | flecks fade, rim steady | #FF60B0 | low | pulse |
| 1686 | 0.8 | 0.57-0.65 | fleck cluster above head | #FF9040 | bright 0.025 | rise |
| 2215 | 0.74 | 0.57-0.66 x 0.32-0.69 | flecks at the feet | #FFA060 | low | drift |
| 2758 | 0.84 (peak 0.95 at 2485) | 0.58-0.66 x 0.28-0.66 | bright white-pink burst at the head | #FFD0F0 | bright 0.06 | flash |
| 2936 | 0.7 | 0.58-0.66 | same as 0 ms | same | low | loop |
Layers seen: rim glow 1, flame flecks ~10, white spark dots ~8
Size vs character: aura about 0.3 heights thick at the body; flecks reach ~0.4 heights over the head
What makes it look good:
- Pink body line plus orange moving flecks: two clear jobs.
- Flecks start at different times, so the loop does not repeat visibly.
Weak points:
- Metrics unreliable for a loop: part of the aura is in the median background, and the lava rock behind may be counted at times. Real effect ~0.7% of screen.
- No floor glow or ground ring; the character is lit only at the edge.
