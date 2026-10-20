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

# bTier__Healing_VFX · B · camera front/side, about 15 studs; two grey blocky characters (about 38% of screen height each) on a grey tiled floor, green "HEALING" text sign between them
Event: a green healing pulse repeats about every 1.6 s: the left character always carries a green glow, plus plus-signs and floor rings; on each pulse the right character also gets plus-signs and rings that expand and fade.
Phases (per pulse, repeats ~0.5 s and ~2.1 s in the clip): burst 460-620 ms · hold 620-900 · fade 900-1300 · idle 1300-1800 (left character keeps a low glow)
| ms | Coverage % | Where (box) | Shapes on screen | Colours | Brightness | Motion |
|---|---|---|---|---|---|---|
| 0-300 | 0.1-0.2 | .35,.28,.5,.68 | left character only: green rim glow, ~6 small plus signs, 2 floor rings (f-idle) | glow #78E8A8, body tinted #A8D0B8 | 0.02% | slow twinkle |
| 463 | rising | | right character gets first plus signs | | | |
| 593 | 5.8 | .35,.29,.88,.68 | both characters: ~15 white plus signs of 2 sizes (small 1% of screen width, large 2.5%), green aura around left body, right body tinted mint, 2-3 concentric floor rings each about 1.2 character widths across (f018) | plus #FFFFFF, ring #40FF70, aura #50E090 | 0.26% | plus signs pop in on the body, drift up |
| 851 | 2.6 | .33,.28,.91,.73 | rings expand to about 2 character widths, double lines; plus signs fewer (about 8), green dots floating (f026) | ring #60F090 | 0.14% | rings grow outward |
| 1180 | 0.5 | .35,.27,.93,.75 | right character ring is a single thin large ellipse about 2.6 character widths, almost gone; left keeps 5 plus signs and rings (f036) | #70D8A0 | 0.03% | fading |
| 1538-1837 | 0.08-0.17 | left only | idle: left glow only | | | |
| 2135-2435 | 2.5 | .34,.24,.92,.68 | second pulse, about as strong as first | | 0.2% | repeats |
Layers seen: floor rings 2-3 per character, plus signs ~15, aura/body tint 1 per character, small glow dots ~10, text sign "HEALING" 1 (static, glow outline, light green #50E060, constant all clip).
Size vs character: rings 1.2 to 2.6 character widths; plus signs 0.05-0.15 of body height; aura hugs the body.
What makes it look good:
- Plus signs read as "heal" in a glance; two sizes give depth.
- Concentric floor rings grow and thin out, anchoring the effect to the floor.
- Body tint plus aura makes the character itself glow, not only particles.
Weak points:
- Looping: left character's idle glow sits in the median background, so coverage reads low (under 6%). Treat metrics as a lower bound.
- The effect stays low-contrast on a bright sky/grey floor; mint tint is washed out.
- Same pulse repeated with no variation; HEALING text is static.
