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

# bTier__orb_thingies · B · camera side, about 20-30 studs; grey floor, pale sky; one orb pickup at centre-right, about 30% of screen height (looping item idle; no character)
Event: a floating round badge (dark-blue disc with a bright ring, crosshair ticks and a glossy star) with rainbow flame wisps rising from its top, floor lit pink and blue, small star sparkles orbiting; subtle pulse for about 3 s.
Phases: loop only; sparkle positions change every few frames; small brightness dips at about 1038-1243 ms and 2330 ms
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0 | 0.8 | .51,.36,.65,.83 | disc about 17% of screen width, ring glow, star in the middle, rainbow flame wisps above (blue to pink to green), pink-purple floor glow below, 3 tiny 5-point stars near the ring | disc #05103A, ring #A8D8FF, star #C8F0FF, floor #C090C8 | 0.14% | wisps flicker |
| 207 | 0.7 | same | same, stars move | | 0.19% | |
| 622 | 0.2 | .51,.37,.65,.80 | sparkle stars on the star face, thin outer ring | #E0F8FF | 0.07% | |
| 1038 | 0.58 | .52,.36,.65,.78 | 3 white star sparkles orbit the disc (f035); wisps pink and cyan | #FFFFFF stars, wisps #50A0FF #FF80C0 | 0.06% | orbiting |
| 1664 | 0.4 | | same | | 0.04% | |
| 2545 | 0.58 | .51,.36,.66,.60 | same, one sparkle at the ring bottom | | 0.03% | |
| 2962 | 0.15 | | | | 0.01% | |
Layers seen: disc 1 (dark body, glowing blue ring, 4 ticks, star in the centre), rainbow flame wisps ~6 (blue, pink, green, soft), floor colour glow 1 (pink, violet), star sparkles ~3 (5-point), thin outer ring 1.
Size vs character: no character; disc about 17% of screen width, 30% of screen height with wisps.
What makes it look good:
- Dark disc with bright ring: strong icon silhouette at distance.
- Rainbow wisps add colour motion above a static shape.
- Floor colour glow lights the ground.
Weak points:
- Looping: median background holds the idle, so coverage under 1% (lower bound only).
- Wisps are soft low-detail blobs that look like a smear; sparkles are tiny.
- Mostly static: only sparkles and wisps move.
