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

# bTier__Water_Barrage_E · B · camera side, about 40 studs; dark blue tiled floor, bright sky; character right of centre (about 13% of screen height)
Event: a volley of water streams arcs from high at upper right, down toward the left floor, and splashes in a bright blue-white burst; a swirl ring is left on the floor, then fades.
Phases: launch/appear 1136-1400 ms · travel 1400-1900 · impact + hold 1900-2900 · tail 2900-3700
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 1236 | 1.2 | .35,.02,.83,.48 | glowing white-cyan ball at upper right (about 3% screen width) with 3 thin ice-blue blade streaks trailing it, 2-3 thin ring discs standing around it (f036) | ball #C8F8FF, streaks #5AA8F0 | 0.15% | ball moves left and down |
| 1635 | 4.5 | .37,.04,1,.84 | 3-4 parallel water streaks about 35% screen width long, spray droplets, bright ball at head; trail reaches the floor at left | streak #4A9CE8, spray #A0D8FF | 0.7% | stream arcs |
| 2032 | 6.9 | .47,.27,1,.70 | peak: a long streak bundle from upper right to the floor at left-centre (about 55% screen width), a splash cloud of blue-white droplets at the floor end, another spray cluster upper right off-screen edge (f060) | #4AA0F0, droplets #B8E8FF, splash core #FFFFFF | 0.6% | splash grows |
| 2426 | 5.5 | .44,.25,.92,.66 | streaks thinner, splash bigger (about 8% screen width), ring discs open up | | 0.5% | |
| 2831 | 4.3 | .41,.01,.88,.66 | splash ball bright white-blue about 10% screen width with droplets on the floor; thin ring discs at upper right; streaks narrow (f084) | #C8F0FF | 0.3% | still streaming |
| 3272 | 2.0 | .41,.01,.88,.66 | smaller splash, fewer streaks | | 0.2% | fading |
| 3700 | 0.6 | | floor swirl ring only | #3A80D0 | 0 | gone |
| 4160+ | 2.6-3.1 | wide | sky/light changes only, not effect | | | |
Layers seen: leading glow ball 1, water streak ribbons ~4, spray droplets ~40, ring discs ~4 around the head, impact splash 1 (floor), swirl ring on floor 1.
Size vs character: stream length about 4-5 character heights wide on screen; splash about 1-1.5 character widths.
What makes it look good:
- Ribbons plus droplets: reads as water, not as a lazer.
- Bright core in the splash against a dark floor.
- Arc gives a clear start-to-target path.
Weak points:
- Starts at the top-right, not from the character's hand: source unclear.
- Stream is semi-transparent thin lines: low coverage (peak 7%) and little mass on a dark floor.
- Metrics after 4 s show sky changes, not effect; the sky lighting is not stable in this capture.
