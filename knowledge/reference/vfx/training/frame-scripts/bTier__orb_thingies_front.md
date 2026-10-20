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

# bTier__orb_thingies_front · B · camera front, about 30 studs; grey floor, pale sky; three small orbs in a row at centre (blue star, red, green plus), each about 3% of screen width (looping item idle; no character)
Event: three coloured orb pickups float side by side, each with a flickering coloured flame on top and a coloured floor glow patch (blue, red-pink, green); they hold a steady glow.
Phases: loop only. Frames 0-180 ms are brighter (coverage 1.5%, near-white 0.35%); metrics decay to 0.05% by 700 ms because the median absorbs the loop. Treat as unreliable.
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0 | 1.5 | .51,.45,.71,.57 | 3 small round orbs side by side (spacing about 7% of screen width), pale and glowing at first; icons inside: star (blue), drop (red), plus (green) | blue #3070F0, red #F04050, green #40E040 | 0.35% | |
| 180 | 1.5 | same | same, full glow | | 0.35% | |
| 310 | 1.0 | .52,.46,.71,.56 | icons clearer as glow dims: dark ring around each orb | | 0.02% | glow decays |
| 489 | 0.14 | | | | 0 | |
| 694 | 0.06 | | steady glow with flame wisps above each | | 0 | |
Layers seen: orb body 3, coloured halo 3, flame wisp on top of each ~3, floor colour patches 3 (blue, magenta, green blended, about 25% of screen width together), small sparkles ~3.
Size vs character: no character; each orb about 3% of screen width, whole row about 12%.
What makes it look good:
- One colour per orb with a clear icon: instant read of type.
- Coloured floor patches blend into a rainbow glow.
Weak points:
- Looping: metrics read near zero after 0.4 s because the idle is in the median background; do not trust the low values.
- Orbs are tiny at this camera; icon detail is lost.
- The first 0.4 s brightness is the fade-in only; after that it is static.
