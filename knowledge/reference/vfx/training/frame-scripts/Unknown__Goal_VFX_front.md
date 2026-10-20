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

# Unknown__Goal_VFX_front · ungraded · camera front, about 35 studs (no character; a large cracked lava-rock ball stands behind as a prop, ~25% of screen width)
Event: the same GOAL celebration seen from the front: a white-gold splash fills the screen, then sharp gold block letters GOAL with sparks, then they fade out.
Phases: idle 0-1300 ms · splash 1340-1650 · word hold 1650-2150 · fade 2150-2400 · empty after 2450
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0-1206 | 0 | - | empty (rock ball in background) | - | - | - |
| 1377 | 55.3 | whole screen | white-gold splash with spiky outlined shards, white core, curved arcs left | #FFFFFF, #FFE8A0, #FFB030 | bright_pct 28 (peak) | explodes from the centre in 1-2 frames |
| 1549 | 58.8 (peak 62.9 at 1264) | 0.10-1.0 | splash splitting, letters GOAL appear under it, bits of splash to the right | #FFE090, #FFA020 | bright 18 | shards fly outward |
| 1720 | 35.5 | 0.12-1.0 | sharp gold letters GOAL (~0.43 of screen wide, ~0.17 high) with orange crack texture, ~12 bright orange flake bits flying around, 5 four-point stars | #FFD060 letters, #E06820 edge, #FFFFFF stars | bright 10 | flakes outward, letters scale in |
| 1891 | 15.6 | 0.23-0.97 | letters steady, ~6 stars, small dots | #FFE080 | bright 5.6 | stars twinkle |
| 2234 | 8.7 | 0.12-0.88 | letters fade to dark orange, edges melt | #8A3A20 | bright 0.05 | dissolve |
| 2410 | 0.17 | 0.08-0.88 low | 2-3 pale sparkle dots | #B7B5A8 | none | gone |
Layers seen: splash shards ~12, white core flash 1, flakes ~15, four-point stars ~8, text 1, glow haze 1
Size vs character: no character; the text is ~0.43 of screen width, about 1.7 times the rock ball
What makes it look good:
- Brightest onset frame (28% near-white), then a fast drop to a readable word.
- Letters have a crack-lava texture that matches the scene prop.
- Splash edges are outlined and liquid: anime cartoon style.
Weak points:
- The splash covers the whole screen for ~0.3 s; coverage is high by design.
