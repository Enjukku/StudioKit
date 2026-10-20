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

# bTier__explosion · B · camera side (low, ground plane + sky), no character visible; burst sits right of centre, about 24 studs away (INDEX)
Event: a pink anime starburst pops on the ground, throws petals, sparkles and a big white comic text shape up and to the right, then fades to thin smoke.
Phases: onset 514 ms · peak 622 ms · follow-through 650-1000 ms · tail to ~1100 ms (visible about 0.3 s per metrics, but sparks linger to ~1.1 s)
| ms | Coverage % | Where (box x0,y0,x1,y1) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 483 | 1.2 | .57,.41,.66,.59 | tiny white-pink spot | #F0D8DC | bright | appears |
| 514 | 6.3 | .50,.30,.72,.71 | spiky 12-point starburst, pink body, cream spike tips (f016) | pink #FF9FD0, cream #FFF0C8 | 3.7% near-white | pops from a point |
| 585 | 19.5 | .39,.06,.83,.86 | burst grows taller than wide; flat pink fan shapes | pink #F5A8C8 | 4.7% | expands fast, up |
| 622 | 24.5 | .37,.01,.88,.96 | peak: translucent pink spike fans, 5-6 sparks leaves/blades, star flowers, white 4-point sparkles, cream comic "text" glyph top right (f019) | pink #F4B8C8, white | 4.2% | burst top leaves the frame |
| 655-750 | 11 to 9.5 | .30,.01,1.0,.89 | fans fade; glyph shape grows to fill top right corner; 5-petal pink flowers and white 4-point sparkles scatter; grey-white smoke puffs on ground (f023) | pink #FF8FC8 flowers, smoke #C0C8D8 | 5.5% (glyph) | sparks fly out, drift |
| 849-973 | 2.4 to 2.0 | .25,.01,1.0,.94 | ~8 flowers, ~4 sparkles, thin smoke wisps (f028) | pink #FF9ACF | 0.5% | drifting up/down slowly |
| 1067-1135 | 0.6 to 0.07 | small | last wisps | grey-blue | 0 | gone |
Layers seen: starburst body 1 (pink, spiky), cream spike overlay 1, translucent pink fan shapes ~4, petal-flowers ~8, thin blade streaks ~8, 4-point sparkles ~6, comic glyph text 1, ground smoke 3-4, no ring seen.
Size vs character: no character. Burst about 40-45% of screen width and 55% of height at 585 ms; extends beyond top edge at peak.
What makes it look good:
- Hard anime starburst silhouette with pink body and cream tips (two-tone), reads in 1 frame.
- Many small secondary shapes (flowers, blades, sparkles) with a bright glow edge give a long tail after the burst.
- Burst dies in ~0.3 s, the sparks keep the beat to ~1 s.
Weak points:
- Starburst is flat and pasted; fans look like see-through cards (alpha edges visible at 622 ms).
- Smoke is faint grey on a grey floor; no ground impact ring or dust.
- Comic glyph is huge and cut by the screen edge.
