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

# bTier__bow_thngiemajig · B · camera side, about 30-40 studs; grey tiled floor, pale sky; a floating bow item at centre-right, about 40% of screen height (looping item idle, no character)
Event: a floating blue-violet bow with a glowing string, sparkles and spiky rays around it, pulsing about every 1 s; a violet glow patch lights the floor under it.
Phases: loop only (idle pulse about every 0.8-1.0 s): dim at about 0-400 ms · bright at about 620 and 1460-1670 · dim at 1041 and 2080 · bright at 2500-2700
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0 | 3.5 | .49,.29,.70,.69 | thin curved bow (blue-violet frame, pointed tips), dark inner strip, ~10 white sparkles on the frame, violet floor glow patch about 25% screen width | bow #3030D8, sparkles #E0E8FF, floor #A8A0E8 | 0 | shimmer |
| 414 | 0.6 | .52,.28,.68,.68 | brighter string line, light halo | #C0C8FF | 0 | |
| 621 | 0.36 | .59,.27,.66,.68 | string glows white-lilac, small halo, 6-8 thin star rays, 4-point sparkles | white-lilac #F0F0FF, rays #5050E8 | 0.04% | pulse up |
| 1041 | 0.25 | .60,.28,.65,.66 | dim phase: bow outline clear, string dark (f035) | #3838D0 | 0 | pulse down |
| 1462 | 0.3 | .61,.37,.65,.66 | bright phase: string a white-lilac bar, 8 rays, sparkles around frame (f049) | #E8E8FF | 0.06% | pulse up |
| 2080 | 0.33 | .60,.35,.65,.66 | dim phase | #3030C8 | 0 | |
| 2504-2718 | 0.34-0.41 | | bright phase again | | 0.07% | |
Layers seen: bow frame 1 (model, glowing blue edge), string glow 1, star rays 6-8, 4-point sparkles ~10, halo 1, floor glow patch 1 (violet), a faint blue floor streak at left (scenery or distant light, not effect).
Size vs character: no character; bow about 40% of screen height and 7% of width; floor patch about 25% of screen width.
What makes it look good:
- Clear silhouette; two-tone (deep blue frame, white-lilac string) reads as magic.
- Pulse cycle with rays gives life to a still item.
- Floor light patch grounds it.
Weak points:
- Looping: the median background already holds the idle, so coverage reads under 1% (lower bound only).
- Pulse is small (halo 7% of screen width), rays thin and low contrast, sparkles tiny.
- Flat idle: no motion of the bow itself seen.
