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

# Unknown__Gabimaru_Aura · ungraded · camera side, about 20 studs (character ~20% of screen height, centre of screen)
Event: a looping aura: a thin magenta-pink glow hugs the character outline and orange flame flecks flicker off the shoulders and head.
Phases: looping, no windup or end. 0-3000 ms is a steady state with small flicker.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 1.1 | 0.53-0.68 x 0.33-0.66 | magenta rim light round arms, torso and legs, ~15 orange flecks on head and shoulders | #FF50C0 rim, #FF9030 flecks, #FFFFFF dots | peak_luma 239 | flecks pop and die |
| 520 | 0.9 | 0.53-0.70 x 0.31-0.66 | 2 flame flecks rise above the head | #FFA040 | low | rise ~0.5 heights |
| 1415 | 1.0 | 0.53-0.70 x 0.30-0.65 | rim steady, a streak of orange to the right | #FF70A0 | low | flicker |
| 1766 | 0.9 | 0.53-0.69 | rim slightly paler, white dot clusters at the hands | #FF80D0 | bright 0.04 | pulse |
| 2634 | 0.9 | 0.53-0.70 | flecks at the head | #FF9040 | low | flicker |
| 2977 | 1.0 | 0.54-0.71 | same as 0 ms | same | low | loop |
Layers seen: rim glow 1, flame flecks ~15, white spark dots ~10
Size vs character: aura hugs the body, about 0.3 heights thick; flecks reach ~0.5 heights above the head
What makes it look good:
- Two colours with clear jobs: pink for the body line, orange for moving energy.
- Flecks rise and die at different times, so the loop does not look mechanical.
Weak points:
- Metrics unreliable for a loop: aura is part of the median background, so coverage ~1% understates it. The effect is small, ~1% of screen.
- Flame flecks are tiny; no ground ring, no light spill on the floor.
- A cracked lava-rock prop appears in the front clip only; ignore it here.
