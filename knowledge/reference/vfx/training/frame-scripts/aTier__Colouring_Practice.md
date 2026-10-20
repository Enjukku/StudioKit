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

# aTier__Colouring_Practice · A · camera side, about 30 studs
Event: a small lime-green glowing orb idles, then bursts into a big green and white explosion with leaf-like shards, then returns to the idle orb.
Phases: idle loop 0-950 ms · burst peak 960 ms · debris 1200-1450 · return to idle 1700+
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-720 | 0.2-0.4 (idle in median) | 0.58-0.70 x, 0.35-0.57 y | small glowing orb, 5-8 dark green specks | #D8F060 core, #4CAF50 | 0.1 % | pulsing |
| 785 (onset) | 21 at 817 | grows to 0.39-0.81 x | white-yellow starburst, 20+ spikes | #FFFFE0 core, #7CFC00 rim | 9.9 % near-white | explodes in 1-2 frames |
| 964 | 14.5 | 0.39-0.81 x, 0.21-0.88 y | white burst fading, green swirling tendrils, ~30 gold sparks | #C8F090, #6FD34F | 6.7 % | expands, drops fast |
| 1203 | 9.4 | 0.38-0.84 x, 0.03-0.91 y | ~50 dark green leaf shards flying outward, soft green haze, spark dots | #1F6B2A, #5DBB63 | 0.3 % | shards fly up and down |
| 1452 | 1.0 | 0.44-0.79 x | few shards, haze | #64896F | 0 % | falling, fading |
| 1708+ | 0.2 | back to orb | idle orb | #C8DE9E | 0.1 % | loop |
Layers seen: hot white core 1, starburst spikes 1, shards ~50, gold sparks ~30, green swirl tendrils 3-4, haze 1, ground glow 1, idle orb 1.
Size vs character: no character; the burst reaches about 0.4 of screen width and 0.7 of screen height.
What makes it look good:
- white-hot core flash (about 6 frames) that sells the hit before the colour layers appear
- dark shards against the bright core give value contrast
- fast fall-off: peak to under 1 % in about 500 ms
Weak points:
- the idle orb is a loop and sits in the background median, so onset coverage reads low
- the burst starts abruptly with no windup
