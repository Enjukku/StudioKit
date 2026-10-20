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

# bTier__silly_water_E · B · camera side-front, about 30 studs; near-black floor with blue grid, bright sky; character right of centre (about 12% of screen height). Timing * approximated (0.6 s delay added by us)
Event: the screen blurs and darkens, then a big blue water swirl (a ring of waves with 3-4 bright splash balls) fills the floor around the character and fades; 2-3 sparkle bursts pop in the sky. A second dark vignette at about 6.2 s ends the clip.
Phases: blur/dim pre-phase 0-1000 ms · swirl build 1000-1400 · swirl hold 1400-5800 · fade 5800-6100 · dark end 6200+
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0 | 43 | full | whole screen blurred and darkened, sky deep blue #1840D8, floor black #060A18; character as a glowing outline with a small blue glow (f014 at 491 ms) | #1A3CE0, #0A1030 | 0 | a post-effect, not particles; coverage is the dim, not the effect |
| 491 | 54 | full | peak of the blur/dim; white-blue oval puddle appears under the character (sheet frame 2) | #C0E8FF puddle | 0 | |
| 946 | 27.7 | full | blur clears; swirl ring appears: a ring of foamy waves about 55% screen width on the floor, 3-4 white-cyan splash balls and a 6-point star burst, sparkle bursts in the sky (about 3% screen width each) | wave #2060F0, balls #D8FFFF, sparks #60F0FF | 0.01% | swirl rotates |
| 1404 | 12.1 | full-width, to .87 | swirl at full size, floor lit blue (tiles glow #1A40C0), sky sparks | #3060F0 | 0.2% | |
| 1869 | 12.0 | .0-1.0,.01-.85 | swirl holds, balls orbit around the character; bright star burst (f056) | white #FFFFFF, blue #2850E0 | 0.8% | orbiting |
| 3805 | 5.4 | .54,.04,.95,.87 | smaller swirl at right (right of the ring is the character), sky burst crown (f112) | #3070F0 | 1.0% | |
| 5787 | 2.6 | .52,.44,.93,.83 | thin swirl, droplets | #2A5ACC | 0.2% | fading |
| 6293+ | 19.7-22.8 | .44,.45,1,1 | floor goes darker and sky changes (lighting change, not effect): swirl is very faint | #131728 | 0 | end |
Layers seen: swirl wave ring 1, splash balls 3-4, 6-point star burst 1, water droplets ~30, sky sparkle crowns 2-3, ground glow 1 (floor lit), blur/dim post effect 1, puddle 1.
Size vs character: swirl about 4-5 character widths across at peak.
What makes it look good:
- Big ground-anchored swirl with moving bright balls: lots of motion for 4 s.
- Blue glow lights the floor tiles, so the effect looks lit.
- Pre-blur/dim builds a beat before the burst.
Weak points:
- Coverage 43-54% at the start is the post-effect, not effect; metrics unreliable there and in the tail (sky and floor change at 6.2 s).
- Long hold (4 s) at low contrast; the swirl looks like a noisy blue stain.
- Sky sparkles are detached from the swirl; scattered with no link.
