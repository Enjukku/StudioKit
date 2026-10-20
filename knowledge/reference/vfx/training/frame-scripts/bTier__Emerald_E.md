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

# bTier__Emerald_E · B · camera side-ish, about 30 studs; dark-blue tiled floor, dark wall at left; player character right of centre (about 15% of screen height)
Event: the character throws several green energy bolts to the left; they land at the wall as a green glow burst that lingers, shrinks and fades.
Phases: windup/launch 652-800 ms · travel 800-1000 · impact 1000-1100 · glow hold 1100-2300 · tail 2300-3000 (visible about 2.2 s)
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 652 | 2.8 | .56,.41,.95,.75 | 4 small green-white dashes/blades in the air near the character; faint green floor patch (f018) | dashes #C8FFE8, floor #3E9078 | 0.04% | appear |
| 800 | 5.1 | .50,.41,.95,.70 | 4 streaks (thin straight green lines, bright tip) each with a pale-green ring and 4-point star at the front; green light pool on the floor and wall (f022-26) | line #50F0A0, ring #A0FFD8, glow #2E8A66 | 0.1% | bolts fly left, rings follow | 
| 952 | 6.1 | .37,.35,.99,.68 | peak coverage: bolts spread over the floor, green wall wash | #40D890 | 0.01% | |
| 1088 | 4.4 | .34,.37,.86,.66 | bolts hit the wall base: bright white-green blob | #FFFFFF core, #50F0A0 rim | 0.1% | flash |
| 1225-1366 | 3.3-3.1 | .34,.40,.86,.65 | soft glow ball about 8% of screen width, with fine green sparkle dots floating up (f050) | core white, halo #30E090 | 0.3-0.45% | sits, slight pulse |
| 1805 | 2.6 | .38,.43,.80,.61 | brightest glow (0.8% near-white); same ball with sparkles | white / mint #80E8C0 | 0.8% | holds |
| 2240-2541 | 2.5-1.9 | .42,.39,.8,.59 | glow shrinks to a green haze with dots (f074 at 2677) | mint #60C8A0 | 0 | fading |
| 2956 | 0.2 | .47,.45,.56,.56 | last dots | | 0 | gone |
Layers seen: bolt lines 4, tip star flares 4, rings 4, impact core glow 1, green haze 1, floor/wall light wash 1, sparkle dots ~30.
Size vs character: impact glow about 0.6 character heights wide; bolt volley spans about 1.5 character heights wide.
What makes it look good:
- Clean single hue (mint green) on a dark floor, so glow reads strongly.
- Bolts have ring + star tips that make a clear read of direction.
- The glow lights the nearby wall and floor.
Weak points:
- The impact is a soft ball with no hard shape or shockwave; the long 1.2 s hold is dull and static.
- The throw has no visible windup on the character; bolts start from the air near the body.
