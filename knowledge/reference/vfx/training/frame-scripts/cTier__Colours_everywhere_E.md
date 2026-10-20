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

# cTier__Colours_everywhere_E · C · camera side, about 35 studs (character ~9% of screen height)
Event: a dummy on the right fires small multicolour firework bursts into the air while the whole sky flashes through blue, green and purple tints.
Phases: idle 0-800 ms · sparks build 800-1800 · bursts 1800-2700 · sky colour flash 2700-3700 · tail 3700-4400 · idle after 4400
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0-600 | 0.0 | tiny box at dummy (0.76-0.79, 0.56-0.59) | dummy only, small hat | blue-white dummy | none | still |
| 1088 | 1.1 | wide, 0-1 x 0.34-0.97 | faint pink floor glow, a few blue dots near dummy | #2A55E0 dots, #A04060 glow | low | dots rise |
| 1877 | 7.4 | whole width | 3 small dot clusters right of dummy, sky turning bluer | #3A8FD0 sky, #FFFFFF, #FFE040 dots | low, peak_luma 238 | clusters drift up-right |
| 2477 | 16 | right third plus sky | 3 round sparkle-ball bursts (~25 dots each), thin smoke wisps | #FF3030, #6060FF, #A040C0, #FFE040 | soft | bursts swell to ~7% of screen width |
| 2893 | 46 | full screen (sky) | same bursts, much dimmer | sky #38C858 green, floor dark green | sky bright, bursts dim | sky tint jumps each frame |
| 3099 | 45 | full screen | bursts fading | sky #3A2D58 purple-dark | dark | sky tint again |
| 3309 | 37 | full screen | few dots left | sky #5F5FE5 blue | dark | sky tint |
| 3747 | 3.8 | right, 0.70-1.0 | fading red/purple dots | #A04864 | low | drift and fade |
| 4372 | 0.07 | tiny | dummy only | - | none | idle |
Layers seen: burst balls 3, round dots ~60, soft smoke wisps 3, floor glow 1, full-sky colour tint 1
Size vs character: each burst about 1 character height wide; cluster spans ~4 heights
What makes it look good: nothing strong; the colour variety reads as a party effect.
Weak points:
- Coverage from 2700 ms is the sky colour change, not particles. Metrics unreliable there; the effect itself is only ~3-8% of the screen.
- Dots are tiny and soft, no shape hierarchy (no core, ring or flare): reads as noise.
- Sky tint cycling every frame looks like a bug, not a flash; there is no hit moment.
