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

# aTier__Death_FX · A · camera front, about 15 studs
Event: a character with long blue-green hair stands still; at 0.53 s a burst of ice-like blue-white shards pops around the body, then dark shards fall; the body dissolve is not captured (needs a real death).
Phases: idle 0-520 ms · burst 527-570 · shard fall 600-1150 · nothing after
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-500 | 0 | none | the character only | n/a | n/a | still |
| 527 (onset, peak) | 16.1 | 0.43-0.80 x, 0.20-0.84 y | ~12 sharp glass-like shards, white-blue star flashes, 2 large white chunks | #D8F4FF, #5CC8F5 | 8.3 % near-white | burst outward in 1 frame |
| 562 | 15.6 | same | shards moving out, a few dark navy shards mixed in | #FFFFFF, #0A1F40 | 6.2 % | outward |
| 594 | 1.1 | 0.48-0.74 x | burst gone, ~20 small dark navy flecks | #121E3A | 0.06 % | fall |
| 699-834 | 1.6-2.3 | 0.46-0.76 x, 0.27-0.11 y | a column of fine white-blue sparkles rising above the head | #C8E8F8 | 0.3-0.6 % | rises 0.15 of screen height in 150 ms |
| 994 | 0.8 | 0.45-0.75 x, 0.04-0.82 y | a few sparkles | #B0D8F0 | 0.15 % | fade |
| 1153 | 0.07 | none | empty | none | none | end |
Layers seen: shard burst 1 (about 12 pieces), dark shards ~20, sparkle column 1 (about 30 dots), star flash 3-4.
Size vs character: burst about 1.4x the character height; character about 0.36 of screen height.
What makes it look good:
- one frame of full-white shards (peak in the first frame) then gap: hit-stop style
- dark navy shards among bright ones add contrast
- the rising sparkle column gives a soul-leaving read after the burst
Weak points:
- burst lasts only 2 frames (about 70 ms)
- body dissolve missing; the clip shows only the particle part
