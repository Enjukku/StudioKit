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

# sTier__Mildly_wet_projectiles_E · S · camera side, about 35 studs
Event: a water shot lands on the ground left of the character: spray first, then a white-blue splash burst and a fog haze that fades in about 1 s.
Phases: small ground ripple 111-330 ms · spray arc 330-450 · burst peak ~1030 · haze 1100-2000 · tail to ~2200.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| 0-326 | 6-11 (sky baseline, not effect) | | faint ripple on the floor near the character | #7090c0 | none | |
| 456 | 22.8 | x.02-1 | small spray arc: ~12 droplets and 3 bubble rings up and right of the character | #c8e8ff | peak_luma 250 | droplets fly up and right |
| 592-922 | 23-26 | x.17-1 | spray grows, splash column low in frame, wide pale haze | #a0d0ff | bright 0.1-0.2% | |
| 1030 | 55.2 (peak) | x0-1 y.06-1 | white-blue starburst: ~20 jagged splash spikes at ground left-centre, a fog cloud spreading right and up to 0.9 width, a dark shard or two | #ffffff core, #8cc4ff body | bright 14.3% | expands from ground |
| 1138-1251 | 52-54 | | same, softer, white fog | #c8e8ff | 6-9% | spreads |
| 1481-1712 | 44-47 | x.1-1 | fading haze, droplets | #a8d0f0 | 0.8% | |
| 2061-2173 | 17 to 7 | | gone | | 0 | |
Layers seen: splash starburst 1, white fog haze 1, droplets ~15, bubble rings ~3, water-shaped streak shards 3, floor ripple 1.
Size vs character: splash about 3 character heights wide and 2 tall; haze about 5 heights wide.
What makes it look good:
- The brightest frames are white spikes, not soft fog: a hard cartoon shape that reads instantly.
- Small spray beforehand telegraphs the hit.
- Everything is the same blue-white hue so the burst stays clean.
Weak points:
- Coverage is polluted by a sky or lighting shift (about 6-25% before the burst); the burst itself is about 30% of the screen.
