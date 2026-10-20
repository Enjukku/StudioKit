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

# aTier__Slashes_2_leaf · A · camera side, about 35 studs
Event: a green crescent slash sweeps in front of a character, then a green smoky burst with glowing orbs forms to its left; the orbs drift away and the smoke fades over about 1.5 s.
Phases: crescent about 250 ms · burst about 500 · orb drift 750-1250 · fade 1250-1750
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-2400 | metrics 7-9 constant (background shift: a light patch on the left floor), max 11.5 at 119 | 0-1.0 x | not separable | n/a | 0.1-0.3 % | do not use for timing |
| about 250 (sheet frame 2) | n/a | 0.28-0.48 x, 0.38-0.52 y | 2-3 stacked glowing crescents, tapered, like a claw mark | #3EE06A, white rim #D8FFD8 | bright thin lines | sweep about 100 ms |
| about 500 | n/a | 0.2-0.45 x, 0.3-0.5 y | green smoke cloud with ~30 small leaf-like chips, 2 bright green orbs at the left end | #5FE070, #1E9A4A, orbs #A8FF90 | orbs near-white | cloud streaks left |
| about 750 | n/a | 0.1-0.4 x | smoke thinning, 3 glowing orbs trailing off to the left in a line | #4AD070 | orbs bright | orbs glide left about 0.1 of screen width |
| about 1000-1250 | n/a | 0.15-0.35 x | smoke dispersing, 2 small orbs | #3CB868 | low | fade |
| 1500+ | n/a | 0.2-0.3 x | faint wisp | #4A9878 | very low | end |
Layers seen: crescent 2-3, smoke cloud 1 (volumetric look), leaf chips ~30, glow orbs 2-3, ground ripple 1.
Size vs character: burst about 0.25 of screen width (5 character heights; character about 0.1 of screen height).
What makes it look good:
- the crescent has a white rim and saturated green body (anime style); the cloud behind is soft: two styles in layers
- orbs leading the smoke give a direction of travel
- green is the only hue, so the burst reads at once
Weak points:
- coverage numbers are not usable (constant, from a lighting patch); times come from the 12-frame sheet, about 250 ms apart
