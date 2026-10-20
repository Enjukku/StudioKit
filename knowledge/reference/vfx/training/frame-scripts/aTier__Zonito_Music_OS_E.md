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

# aTier__Zonito_Music_OS_E · A · camera side, about 40 studs, dark stone-tile floor
Event: a character (right) triggers a gold note barrage: a gold sparkle swirl around it, gold streak ribbons flying left, then 3-4 gold round bursts with spark fountains on the floor, fading over about 2 s.
Phases: idle 0-800 ms · build 800-2250 · swirl burst 2265-2800 · streaks 3200-3700 · ground bursts 4400-5500 · tail to 5.8 s
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| --- | --- | --- | --- | --- | --- | --- |
| 0-2000 | 0.9-2.2 (character and a floor glow) | 0.49-0.80 x, 0.09-0.69 y | none, character stands; faint gold pulse on the floor at 1.0 s | #E8C060 faint | 0.1 % | still |
| 2265 (onset) | 25.7 at 2301, 24 at 2403 (whole-frame box 0-1 x/y: a screen-wide exposure change, not particles) | whole frame | whole image brightens and shifts warm for about 3 frames | #766C66 mean | 1 % | flash |
| 2821 | 4.4 | 0.62-0.89 x, 0.39-0.70 y | big gold swirl cloud around the character, 1 curved trail upper right, ~40 sparks | #FFD060, #F0A020 | 0.6 % | spins up and out |
| 3234 | 2.8 | 0.60-0.96 x | thin curved gold ribbons flying right and left, ~15 spark clusters | #FFC850 | 0.06 % | streaks fly |
| 4495 | 6.3 | 0.54-1.0 x, 0.41-0.78 y | 3 round bright gold puff bursts on the floor with thin spark fountains going up | #FFD770 core, #E08A20 | 1.3 % | puffs grow |
| 4920 (peak) | 7.9 | 0.56-1.0 x, 0.41-0.88 y | 4 gold puffs, each about 0.07 of screen width, 30+ sparks above | #FFE090 | 1.6 % | bloom |
| 5335 | 6.0 | 0.56-1.0 x | puffs shrink, sparks drop | #D8A850 | 0.5 % | fade |
| 5748 | 3.5 | 0.57-0.99 x, 0.51-0.84 y | small cracked starburst rings on the floor, few sparks | #B07838 | 0 % | tail |
Layers seen: sparkle swirl 1, curved gold ribbons about 4, round puff bursts 3-4, spark fountains 3-4, floor starburst rings 3, floor glow 1.
Size vs character: swirl about 4 character heights wide; each ground puff about 1.5 character heights (character about 0.1 of screen height).
What makes it look good:
- three beats with gaps: swirl, streaks, ground bursts (about 1.5 s apart), so the barrage is readable
- one hue (gold) with white-hot cores; the dark floor makes it pop
- bursts are staggered in position and time, so they look like separate notes
Weak points:
- the 25 % reading at 2.3-2.4 s is a whole-frame exposure change (box = full screen); treat it as one big flash, not effect area
- timings from the 12-frame sheet are about 0.5 s apart, so beat times are within 250 ms
