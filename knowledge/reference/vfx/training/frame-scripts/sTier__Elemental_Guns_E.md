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

# sTier__Elemental_Guns_E · S · camera side, about 35 studs
Event: a character at the right edge fires a fire-and-ice shot; a bolt flies left across the field and fades about 3 s later.
Phases: gun glow 0-1100 ms · muzzle flash 1200-1400 · travel 1400-2900 · tail 2900-3470.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| 0-136 | 15.8 (sky baseline, not effect) | x.03-1 y0-.65 | none | | | |
| 277-1109 | 0.7-0.9 | x.70-.90 y.36-.63 | small glow on gun and hand, tiny streaks | #4aa0f0 blue, #ff9030 orange | peak_luma 213-250 | static glow |
| 1248 | 2.7 | x.68-.91 y.37-.68 | muzzle flash: white-blue ball with orange spikes, blue puff on the ground | #ffffff core, #ffa030 | bright 0.23% | leaves gun |
| 1517 | 3.0 | x.54-.90 y.39-.60 | thin streak: round orange glow head, orange spark band, blue-white dot at the tip | #ffa020 / #50b0ff | head peak_luma 245 | moves left, ~0.4 screen widths per 400 ms |
| 1648-1781 | 3.4 (peak) | x.39-.87 | same band, about 0.3 screen long, trail of blue sparkles above | | bright 0.1% | steady speed |
| 2305-2700 | 1.4-1.6 | x.02-.87 | bolt reaches the left edge, spark trail thins to an orange dash plus faint blue line | #e08030 | dim | decelerates |
| 3395-3534 | 1.7 | | last orange dash, no impact shown | #c07040 | dim | fades |
Layers seen: orange fire core 1, white-blue ice tip 1, spark stream ~30 tiny, blue sparkles ~10, muzzle flash 1, ground glow 1.
Size vs character: bolt head is about 0.4 character height; trail about 4-5 character heights long. Whole effect is small on screen.
What makes it look good:
- Fire in the middle and ice at the tip: two readable colours in one thin streak.
- Blue-white bloom on the muzzle for 2-3 frames sells the shot.
- Long thin spark tail shows speed.
Weak points:
- Camera is far; this is the small version, see the _follow clip for the close view. No impact frames.
