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

# sTier__Astral_Sword_E · S · camera side/3-4 high, about 35 studs
Event: a blue crystal sword drops from the sky onto a glowing rune circle on the ground; an icy-blue burst and flame dome erupt, then settle into a lingering glyph ring. It repeats about 3 times in 5 s while the sky cycles day to dusk to night.
Phases: ground glow 0-450 ms · sword falls · impact burst ~800-1100 · dome/flame 1100-2000 · fade to ring glyph 2000-2700 · next cycle from ~3200 (dark sky).
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours | Brightness | Motion |
| 0 | 10.5 (sky/lighting, not effect) | x.30-.92 y.01-.75 | thin vertical sword high at top centre, soft blue ground pool | sword #3a6fe0, pool #2a4fd0 | dim | pool fades in |
| ~450 | 9-24 | centre ground | rune circle: concentric rings plus 6 notch glyphs, flat ellipse ~25% screen wide | rings #a8c8ff on #2a50c8 | medium | sword lower, rings appear |
| ~900 | 8-24 | y.3-.75 | spiky starburst: ~12 white-blue spikes fan up from a bright elliptical ring, flame dome behind | spikes #dff0ff, flame #3a78f0 | bright, peak_luma 240 | burst expands fast (~3 frames) |
| 1026 | 60.7 (includes big sky shift) | whole frame | wide white-blue glow, thin web lines with star nodes over the character, light streaks | #8ac0f0 / #e8f4ff | bright 0.5% near white | glow swells, view looks streaked |
| ~1350-1800 | 9-62 (sky change) | x.1-.95 | blue flame dome ~35% screen wide, white swirling ring at base, wispy blue smoke at the ground edge | dome #4a88f0, ring #ffffff | bright | dome flickers, smoke curls outward |
| ~2400-2700 | 7 | x.2-.93 y.1-.8 | faint dome, glyph ring remains, dark smoke wisps | #2a50a0 | dim | fading |
| ~3200-4900 | 15-60 (sky dark) | same | same burst again on a dark sky, sparkle stars plus 1 thin vertical beam | #3a78f0 on black | glows pop against dark | repeat |
Layers seen: ground rune circle 1, spike starburst 1 (12 spikes), flame dome 1, white swirl ring 1, smoke wisps ~10, star sparkles ~10, falling sword 1, glow/bloom haze 1.
Size vs character: dome about 5-6 character heights wide, spikes up to 4 heights; the character stands to the right, much smaller.
What makes it look good:
- Ground rune ring appears first, so the hit is telegraphed before the impact.
- Hard bright spike burst for 3 frames, then softer flame dome: sharp peak then long soft body.
- One hue (blue) with white only on the ring and spikes; dark smoke gives contrast.
Weak points:
- Coverage and mean_rgb are polluted by the sky going from day to dusk to night; use the sheet frames, not coverage, for this clip.
- It loops, so the exact windup and tail per cycle are approximate.
