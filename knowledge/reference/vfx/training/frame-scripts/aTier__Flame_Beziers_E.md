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

# aTier__Flame_Beziers_E · A · camera side, about 40 studs, dark ocean scene
Event: a barrage of about 8 red-orange fire missiles arcs through the sky from the upper right and dives to the ground at the centre; each hit makes an orange burst and a spreading lava-red ground patch.
Phases: launch 0-400 ms · travel 400-2000 · dive 2000-2400 · impact 2400-2750 · embers 2750-3400 · quiet to 5 s
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 4.1 | 0.11-0.91 x, 0.01-0.61 y | cloud sky is part of the median; thin flame ribbons start at the top right | #FF5A20 | none | begin |
| 364 | 4.7 | 0.12-0.86 x | bundle of about 8 curved flame ribbons with black ash specks | #FF6A28, #FFB060 core, #1A1A1A ash | 1 % | arcing left |
| 1059 | 3.5 | 0.14-0.84 x | ribbons shorter, bunched at the top centre, zig-zag | #FF5030 | 0 % | travel |
| 2069 | 4.2 | 0.19-0.90 x, 0.61 y | ribbons turn vertical, about 4 tall streaks falling | #FF5A28 | 0 % | dive |
| 2406 | 7.4 | 0.33-0.91 x, 0.02-0.71 y | 2 yellow-orange explosion blobs at the ground, flame spikes, vertical streaks above | #FFC040 core, #FF4A10 | 0 % | burst |
| 2741 (peak) | 8.7 | 0.16-0.90 x, 0.03-0.82 y | flat red lava-like patch spreading, fire spikes, ~30 sparks, red light on the floor | #E03010, #FF7A20 | 0 % | ground glow spreads |
| 3075 | 2.2 | 0.20-0.90 x | patch cooling to dark red | #7A1E1E | 0 % | fade |
| 3416 | 0.3 | none | nearly empty | none | none | end |
Layers seen: flame ribbon trails ~8, ash specks ~20, explosion blobs 2, ground lava patch 1, flame spikes ~6, sparks ~30, red floor light 1.
Size vs character: no character; the ground patch is about 0.3 of screen width.
What makes it look good:
- long curved trails sell speed before the hit
- the impact adds a ground light and patch, not only a flash
- orange on a dark blue scene gives maximum hue contrast
Weak points:
- metrics unreliable: the sky and clouds reflect the median background (0.11-0.91 x box from frame 0), and after 3.4 s the box drifts; read coverage as relative only
- no near-white flash at impact (bright 0 %)
