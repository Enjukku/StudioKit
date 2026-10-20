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

# cTier__fiya_beam_E · C · camera side, about 35 studs (character ~9% of screen height); camera framing drifts and lighting flickers
Event: a fire column bursts up from the dummy, then a thick flame beam sweeps left along the floor with black chunks flying; one frame range turns the screen green and orange.
Phases: idle 0-800 ms · column 800-2400 · beam start 2400-2800 · screen tint/blur 2800-3200 · beam loop 3200-8000 (clip ends mid-effect)
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0-600 | 6.2 (constant dummy/shadow) | 0.44-0.96 | dummy | dark blue | none | still |
| 1237 | 14.8 | wide | ragged flame column over dummy, ~1.3 heights tall, orange glow on floor | #FFB020 core, #E06010 edge, floor #603018 | bright_pct 0.13 | flames flicker upward |
| 2217 | 25 | whole width | same column, ~2 heights tall | #FFC030 | bright 0.18 | flicker |
| 3037 | 87 | full screen | whole picture re-tinted: green sky, orange floor, huge blurry orange beam from dummy to centre-left | #FF6A20 beam, sky #0A5038 | camera in heavy blur | a few frames; a camera/post effect, not particles |
| 3462 | 3.4 | 0.40-0.92 | sharp flame beam ~0.45 of screen wide, ~60 small flame blobs, ~5 black chunks flying | #FFC040 core, #E07010 edge | bright 0.9 | beam streaks left, chunks tumble |
| 4295-8000 | 3.1-4.4 | 0.07-0.97 | beam repeats, chunks fall, framing drifts | same | steady | loop, no change |
Layers seen: flame blobs ~60, beam streaks 3-4, black rock chunks ~10, floor orange glow 1, camera blur/tint 1
Size vs character: column ~2 heights tall; beam ~7 heights long
What makes it look good:
- Beam core is bright yellow fading to red-orange edge, reads clearly as fire.
- Orange floor glow ties the fire to the ground.
Weak points:
- Black chunks are plain dark cubes with no glow; they read as dirt.
- Metrics unreliable: 87% at 3037 ms is a screen tint and camera blur; the real effect is ~4%. The clip loops; no single event.
- Column and beam are two unrelated effects with no link.
