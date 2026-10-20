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

# aTier__Ayato_Showcase_E · A · camera side, about 35 studs
Event: a black-clad character dashes left across the ground, leaving a gold slash trail, and stops 0.6 s later; the ending is partial (dash effects need a private animation).
Phases: idle 0-900 ms · dash burst 900-1450 ms · tail 1450-1600 ms · nothing after
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-190 | 1.6-1.9 (the character itself and a small gold streak, not the effect) | 0.40-0.77 x, 0.44-0.63 y | gold thin slash arc at the character's hip, a few sparks | #F2C14A on dark body | peak luma 246 | arc fades in 200 ms |
| 350-900 | 1.3 (idle character) | same | none | none | dim | character stands |
| 984 (onset) | 6.7 | 0.23-0.70 x, 0.32-0.63 y | 4-point star flare at the left tip, curved crescent trails (2-3) | #FFD36B core, #F5A623 edge | 1.2 % near-white | character jumps left, trails follow |
| 1140 | 4.3 | 0.31-0.68 x | 2 long curved gold streaks + ~15 sparks | #F7C948 | 0.5 % near-white | streaks stretch, sparks scatter |
| 1300 | 2.3 | 0.34-0.67 x | thin streaks, fading sparks | #E8B84A | 0.2 % near-white | fade |
| 1459 | 0.8 | 0.34-0.55 x | a few sparks | #B89A6A | none | tail |
Layers seen: crescent trail 2-3, 4-point star flare 1, sparks ~15, no smoke, no shock ring.
Size vs character: the whole dash is about 3 character widths long (the trail spans about 0.4 of screen width); the character is about 0.16 of screen height.
What makes it look good:
- sharp anime crescents with a bright white-gold tip, not soft blobs
- the star flare sits only at the leading end, so the eye follows the motion
- short life: bright part under 500 ms, then clean empty frame
Weak points:
- metrics.json peak (15.5 % at 917 ms) is the character's movement, not the effect; the effect itself reads about 6.7 %
- partial capture: the animation that drives the dash is missing
