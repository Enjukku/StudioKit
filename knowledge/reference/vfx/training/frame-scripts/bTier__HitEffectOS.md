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

# bTier__HitEffectOS · B · camera side, close (burst fills frame); dark navy floor, grey-teal sky band, two faint glass cubes as scenery; no character. Timing is ours (INDEX: * 8 hit emitters fired directly)
Event: a hit effect: a purple-pink glow burst with light rays, then a white spiky arc ring, white and black blade slashes, glowing orbs and black flecks all fly outward; thins out in about 0.7 s.
Phases: onset 630 ms · peak 734 ms · follow-through 770-1000 · tail 1000-1300 (visible about 0.4 s per metrics)
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 630 | 19.6 | .31,.01,.91,.61 | soft violet burst on the floor with 6-7 rays shooting up, pink-white core, hazy and smoky edges (f019) | core #F0C8FF, body #9A40E8, rim #5020A0 | 0.8% | grows in 1 frame |
| 665 | 9.8 | .42,.09,.78,.70 | burst drops, first white blades appear | #FFFFFF | 3.5% | cut flicker |
| 699 | 17.5 | .35,.01,.86,.74 | white blade slashes and orbs | #FFFFFF | 10.3% (max) | flash |
| 734 | 24.0 | .28,.01,.93,.82 | peak: a big white spiky arc ring (like an arch about 55% of screen width), ~10 white spear blades with black-edged twin blades, ~6 white glow orbs, a few black round blobs (f022) | white #FFFFFF, lilac #E0C8FF, black #101018 | 10.3% | radiate out from centre |
| 804-869 | 15.2-11.7 | .10-.23,.01,1,.86 | ring gone; 5 long white-yellow blades 15-25% of screen long, 4 purple blades, ~8 orbs, ~15 black blades/dots (f026) | white-yellow #FFF8C8, lilac #D080FF | 2.8% | blades keep flying out, past the edge |
| 999 | 3.1 | .23,.01,1,.84 | 3 pink-white blades and 5 small orbs (f030) | pink #E8B0FF | 0.4% | slowing |
| 1162 | 1.0 | .25,.11,1,.84 | 1-2 specks | | 0.1% | |
| 1328 | 0.06 | | gone | | 0 | end |
Layers seen: ground burst with rays 1 (violet), arc ring 1 (white, spiky edge), long blades ~10 white + ~15 black, glow orbs ~8 (white, lilac, cream), black blobs ~5, haze 1.
Size vs character: no character; arc ring about 55% of screen width at peak; burst about 45% of width.
What makes it look good:
- Value contrast: white and black blades on a violet burst read as a strong hit; 10% near-white at peak.
- Fast: peak by 100 ms after onset, then thins out over about 0.5 s.
- Black elements among the light ones add a comic-book snap.
Weak points:
- Black blades and blobs look like dirt on a dark navy floor; they vanish into the background.
- The violet burst at the start is blurry smoke, not shaped; it stalls for one frame before the white wave.
- Many separate emitters hit at once with no clear order: the screen goes busy at 700-870 ms (11-24% coverage).
