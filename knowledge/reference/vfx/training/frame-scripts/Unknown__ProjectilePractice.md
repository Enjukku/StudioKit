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

# Unknown__ProjectilePractice · ungraded · camera side, about 40 studs (no character; two white egg-shaped targets, ~0.08 of screen width each, one left, one right, floating over the floor)
Event: two volleys of green-white bolts (flown by our script along curves) fly between the two targets and burst into green star flares and swirl rings on hit.
Phases: volley 1 0-1400 ms · empty 1470-1990 · volley 2 2000-3300 · empty after 3500
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 0.3 | 0.28-0.36 x 0.58-0.75 | small white burst and dust puff under the left target, one green dot | #A8D8C0, #FFFFFF | peak 250 | puff rises |
| 180 | 0.39 | 0.28-0.50 | green-white bolt with a thin tail leaving the left target to the right | #B0F0C0 | bright 0.003 | travels ~0.1 screen in 0.1 s |
| 740 | 0.26 | 0.26-0.76 x 0.45-0.53 | a long thin streak across the mid screen, tail ~0.3 wide | #C0FFD0 | bright 0.06 | speed ~0.5 screen/s |
| 1106 | 0.16 | 0.89-1.0 x 0.45-0.71 | glow and small flecks at the right target | #A0D0B8 | low | fades |
| 2020 | 0.53 | 0.34-0.47 x 0.58-0.65 | green bolt head with a streak trail near the left target | #D0FFD0 | bright 0.16 | launch |
| 2388 | 0.6 | 0.76-0.90 | bolt reaches the right target, leaf flecks | #C0F0C8 | bright 0.22 | travel |
| 2569 | 5.2 (peak) | 0.13-1.0 x 0.45-0.78 | left target has a white swirl ring ~0.2 wide and a green four-point star flare; right target ringed by a green spiral with ~15 white-green flecks and 3 streaks | #FFFFFF, #60FF90, #B0FFC8 | bright 1.2 | rings spin outward |
| 2939 | 0.5 | 0.09-1.0 x 0.31-0.82 | fading rings and green leaf bits | #70D090 | low | fade |
Layers seen: bolt head 1, streak trails 2-3, hit flares 2, swirl rings 2, leaf flecks ~8, flecks ~15, dust puff 1
Size vs character: no character; targets ~0.08 of screen width; hit ring ~0.2 of screen width
What makes it look good:
- Hit shows three layers: flash star, ring, flecks, with the second colour (white) separate from the green.
- Streak trail makes speed readable.
Weak points:
- Bolts are tiny (coverage mostly under 1%) and hard to see between the targets; hit is only ~5% for one 0.2 s.
- Bolts are flown by our script, so paths and timing are not the original effect's own; two empty gaps (about 0.5 s) in the clip.
