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

# aTier__Ayato_Showcase_Q · A · camera side, about 35 studs
Event: the character performs several quick sword slashes in place; each makes a thin gold crescent with sparks.
Phases: slash 1 at 0 ms · slash 2 390-570 · slash 3 800-1000 · slash 4 1430-1530 · tail to 2575 ms
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.4 | 0.59-0.73 x, 0.43-0.61 y | gold ring-shaped crescent around the waist, ~10 sparks | #FFD36B, glow #F5C46A | 0.04 % near-white | crescent sweeps 100 ms |
| 101-294 | 0.1-0.35 | thin | fading spark dots | #E0B060 | none | drift left |
| 390 | 1.7 | 0.52-0.72 x | wide crescent + dotted spark trail to the left | #FFE08A | 0.09 % | sweeps right-to-left |
| 809 | 2.8 (peak) | 0.49-0.68 x, 0.37-0.66 y | tall crescent arc across the body | #F0C060 | 0 % near-white | 100 ms sweep |
| 998 | 1.7 | 0.52-0.67 x | thinner crescent | #FFF0B0 core | 0.12 % | fade |
| 1432 | 1.3 | 0.59-0.73 x | wide thin arc | #FFD36B | 0.05 % | sweep |
| 1631+ | <0.1 | none | empty | none | none | end |
Layers seen: crescent 1 per slash (4 slashes), sparks ~10 per slash, faint warm glow around the body.
Size vs character: each crescent is about 1-1.5 character widths wide; the character is 0.16 of screen height.
What makes it look good:
- thin bright crescents, each on screen only 100-200 ms (about 4-6 frames)
- slashes come at uneven intervals (about 400 ms, 400 ms, 600 ms), so the rhythm feels played
- warm gold on a dark character gives strong contrast
Weak points:
- peak coverage under 3 %: it is a subtle effect and reads small at distance
- one slash (about 670-800 ms) looks nearly empty
