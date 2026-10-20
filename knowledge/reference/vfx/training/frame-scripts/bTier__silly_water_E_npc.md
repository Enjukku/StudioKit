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

# bTier__silly_water_E_npc · B · camera front, close to a target dummy (a pale pillar with a label "Water AOE Testing Dummy"), about 20 studs; near-black floor, bright sky. Timing * approximated
Event: same water swirl as silly_water_E, centred on a dummy: a blue wave ring on the floor with 3-4 bright splash balls and a star burst, sparkle crowns in the sky, then it fades; a second small pulse starts at the end.
Phases: build 0-1000 ms · hold 1000-3500 · fade 3500-4300 · idle · second pulse from 6500
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0 | 7.2 | 0,.01,.78,.78 | swirl ring on floor about 50% of screen width, splash balls 3, sky crown above | #2060F0, #D8FFFF | 0.4% | swirl turning |
| 1009 | 38.8 | full | swirl big (floor around dummy lit blue), one 8-point star burst below the dummy, 2 side balls, 2 sky crowns (f030) | #2858F0 floor, burst #C8FFFF | 0.4% | camera tilt/lighting: floor looks lit; coverage inflated (sky and floor shift) |
| 1498 | 30.9 | 0-1,.01-.76 | swirl, balls, floor glow | | 0 | |
| 1977 | 4.9 | .01,.05,.77,.75 | swirl thinner; floor still lit | | 0.2% | |
| 2948 | 5.8 | | big star burst right of dummy (about 8% screen width), 2 balls, crescent wave arc, sky crowns (f090) | white-cyan, #2060E8 | 0.9% (max) | bursts pulse |
| 3998 | 4.0 | | swirl thins to a few faint blobs | #2858C8 | 0.3% | |
| 4516+ | 17.6-20.7 | .0,.44,.89,1.0 | floor and sky darker (lighting change, not effect) | #0E1A40 | 0 | |
| 6983 | 21.4 | .0,.05,.89,1.0 | second pulse: bright ball and splash ring around dummy | | 0.4% | restarts |
Layers seen: swirl wave ring 1, splash balls 3-4, star burst 1, sky sparkle crowns 2-3, droplets ~20, floor glow 1, dummy label (not effect).
Size vs character: dummy about 12% of screen height; swirl about 5 dummy heights across.
What makes it look good:
- Burst with spiky star plus orbiting soft balls: two contrasting shapes.
- Floor glow makes the effect look lit on the tiles.
Weak points:
- Coverage 30-40% around 1000-1500 ms is lighting and sky change, not particles: metrics are unreliable in this clip.
- The sky crowns are far from the dummy and unrelated to the hit.
- Without the blur pre-phase the start is abrupt.
