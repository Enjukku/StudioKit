> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20. Revised by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (the ring size curve eases in fast).

# Pro defaults: values per layer job, recipes per effect type, budget

Source: 30 measured pro Roblox effects (S+A tier columns preferred) in `knowledge/reference/vfx/training/building-blocks.md` (BB) and `curve-library.md` (CL); craft rules from `tutorials.md` (TU); Roblox limits from `roblox-vfx-api-card.md`. Values are **starting points with a measured basis**: copy them, then move one only with a reason. Hidden test effects are not in this data (benchmark.md).

## A. Defaults per layer job
All rows: **LightInfluence 0**. Size = peak size in studs at a normal character-scale effect (scale with the effect, §C). Curves: names from CL; copy keypoints from `content/vfx/curves.json`. "S+A" values replace the all-tier median where they differ (BB §6).
| Job | Lifetime s | Speed / Drag | Brightness | LightEmission | ZOffset | Count | Size studs | Orientation / notes | Size curve | Transparency curve |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| core (hot centre) | 0.4 (0.15-0.5) | ~0 / 0-5 | 5 (4-6) | 1 | 0-0.1 | 3 burst or stream | 0.2-1 (tiny) | FaceCamera; colour moves hot→body (77%) | linear shrink | opaque hold |
| flare / star | 0.7 (0.25-1.1) | 0 / 0 | 4-5 (to 15 for tiny) | 1 | +1.5 | 2 | 1.6-2 (to 9) | FaceCamera, Speed 0; 4-point star or cross | bump (early peak) | opaque hold |
| impact burst (shape) | **0.12** (0.07-0.2) | 0 / 0 | 3-4 | 0.1-1 | **+2.8** (1.8-3.7) | 1-2 | 7.7-8.3 (4-27) | solid shape, no holes; 25% flat (perpendicular) | linear shrink (start big) | opaque hold |
| white flash | **0.03-0.05** | 0 | high | 1 | highest | 1 (+1 slightly longer) | ≥ impact | TU-12/13; "if you can see its shape it lasts too long" | grow or shrink | opaque hold |
| glow / halo | 0.7 (0.04-2) | 0 / 0 | 1.5-2 | 1 | +2 to +3 | 1 | **13-15** | FaceCamera, soft-edged texture | constant size | opaque hold or V (fade in, hold, out) |
| ring / shockwave | **0.2** (0.2-0.5) | 0 / 0 | 5-6 | 0 | 0 (−0.3-0.2) | 1-2 | 5.7-9 | flat VelocityPerpendicular (63%) or FaceCamera; starts at ~0.56 of max | constant size, `ease-out grow`, or grow from 38% with a key at about t 0.25 at ≥0.7 of max (fast in, ease out: `measure.md` §5) | fade in, hold, fade out |
| spark | 0.85 (0.5-1.3) | **25 (15-50) / 5.5 (3.6-9)** | 5 | 0 | +1.5 | **15** (5-25) | 1.3 (0.4-3) | Spread 360; 20% VelocityParallel | linear shrink | opaque hold |
| ember / spec | 0.8 (0.4-1.6) | 1-7 / 0-4 | 3-5 | 0-0.2 | 0 | 2-8 | 1-1.5 | off-centre spec textures rotate; may rise (Accel +) | linear shrink | fade in |
| streak / speedline | 0.5 (0.2-0.75) | 8-24 / 3.6 | 6 | 0 | 0 | 6 | 1.4 | **VelocityParallel + Squash** (65%) | linear shrink | opaque hold |
| flame body | 0.7 (0.3-0.9) | 10 (0-65) / 0-12 | **7.5** | 0 (some −0.3) | 0 | 5 | 3.9 (0.7-13) | **flipbook** 4x4 (94%), Spread 360, colour shifts (70%) | constant size | opaque hold |
| smoke | 1.0 (0.6-1.5) | 15 / 3.4 | 2 | 0 | 0 to −1 | 10 | 3 (1-12) | **flipbook**, darker, under fire, outlasts it; starts transparent | partial grow | faint |
| liquid / splash | 0.75 | 0 / 0 | 2.5 | 1 | 0 | 1-2 | 5 | flipbook 65% | constant size | linear fade |
| wisp / swirl | 0.6 | 0-34 / 0-5 | 4.5 | 0 | 0 | 5 | 1-3 | RotSpeed for swirl | linear shrink | opaque hold |
| slash / crescent | 0.3-0.6 | **0.01** / 0 | 3 | 0-0.5 | 0 / ±0.001 layers | 1 per texture | 3.7 (2.3-16) | VelocityPerpendicular 91%; RotSpeed > 360°/s for short lives; 3-5 textures layered (TU, TV4) | partial grow | fade from translucent |
| ground decal / crack | 1.0-1.3 | 0 / 0 | 3 | 0 | **0** (lift attachment instead) | 1-2 | 5-7 | flat; grows fast then stops | ease-out grow | constant then fade |
| lightning | 0.2-1.0 | 0 / 0 | **15** (4-30) | 1 | 0 | 1-5 | 0.3-30 | FaceCameraWorldUp for bolts; flipbook 89% | constant size | opaque hold |
| dark underlay / twin | 0.4 (0.25-0.6) | as its partner | as partner, darker colour | 1 with dark colour, or 0 | partner − 0.001 to −1 | as partner | as partner, grows | flat 73% | S-curve grow | late fade |
| debris chunks | 0.8 (0.75-1) | 22-100 / 5.5-7 | 4 | 0.25 | 0 | 5-12 | 0.8 | Accel −3 to −40 (falls); toy-block debris uses the block path instead | linear shrink | opaque hold |
| PointLight | effect life | — | 1.4 (0-4) | — | — | 1 | Range 9 (5-16) | in 20/30 effects; Shadows off unless needed | — | tween Brightness |
| Beam | — | TextureSpeed 1.3-3 (vary per layer) | 1 (to 15) | 0-1 | — | — | Width0 6 → Width1 20 | Segments = keypoints − 1 if straight, more if curved (to ~50); semicircle CurveSize = diameter × 2/3 | — | ends transparent |
| Trail | 0.5 (0.1-0.8) | — | 4 | 0-1 | — | 2-4 stacked | WidthScale taper | FaceCamera 100% | width linear shrink | colour hot→body |

## B. Recipes per effect type (jobs that pro units of this type use; all fire at 0 ms unless noted)
Share = % of pro units of that type with the job (BB §8). "Add" = from tutorials / craft rules.
| Type | Core jobs (share) | Add | Size of unit | Timing skeleton |
| --- | --- | --- | --- | --- |
| **Projectile (in flight)** | flame body 47% (flipbook), core, flare 40% (star/cross on the head), streak 27% (VelocityParallel), ember 60%, spark 53%, glow 47%, trail stack 2-4 (Trail or Beam) | dark twin of the body; world-space wake rings (LockedToPart off); PointLight on the head | 13 emitters | stream while flying; head flare and core continuous |
| **Impact / explosion** | impact burst 89%, flare 56%, spark 56% (EmitCount ~31), glow 56%, splash/fire 56%, wisp 44%, smoke 33% | white flash 0.03-0.05 s + second slightly longer; fire ring (VelocityParallel, Spread 180, Speed high + Drag); fireball body (FaceCamera, low speed); dark smoke under; embers; shockwave ring; wind (perpendicular, Spread 180, ~5, very random size); ground mark; faint rainbow flare | 10 emitters | flash 0-50 ms → shape to ~150 ms → sparks/flares to ~1 s → smoke/embers 1-1.5 s → mark fades by ~1.3 s |
| **Burst / one-shot** (hit, pop) | ember 41%, flare 35%, streak 32%, glow 30%, smoke 27% | impact star 0.05 s | 4 emitters | everything at 0 ms, lifetimes do the order |
| **Slash** | slash/crescent 3-5 textures (base colour, dark twin −0.001, bright thin, faint wide, 1.5× randomised extra), core, streak, glow, flare | beam arcs (TV4) swept by a rotating attachment (~175°), sparks along the arc (LockedToPart), impact star 0.05 s, Highlight flash, ground wind | 10 emitters | slash life 0.2-0.3 s; beams width tween to 0 in the slash time |
| **Beam attack** | main flat beam (opaque base, ends transparent), wavy and energy layers under, VelocityParallel spike lines, stars, crystal flipbook | **start**: crescent wind ring, impact flipbook + black twin, glow, flare, shock rings; **end**: impact, glow, shards (Drag ~6), circle impact, specs, smoke that lags (unlocked); side wind beams | ~60 live particles total in TV5 | widths/brightness tween in on start, to 0 on end; TextureSpeed differs per layer |
| **Strike (lightning, meteor)** | bolt (FaceCameraWorldUp, stylised, touches ground), impact 0.05 s + flipped growing copy, glow, flash glow | ground ring, ground lightning over a duration (fast + slow), dust (realistic + dark), sun rays (negative ZOffset), cracks, long tiny specs, slower inward impact, outward smoke ring (Speed ~150 + Drag), debris parts with trails | — | impact layers no fade-in |
| **Aura / loop** | flare 44%, ember 40%, smoke 32% (all continuous) | specs (size fade), swirl via off-centre rotating textures, glow without flicker (Rate 2, Life 1, V curve), PointLight, ground rings and faint circle, spiral beams, snow/particles from a Disc, Highlight fill | 3 emitters per unit | everything fades in and out; Rate × Lifetime ≤ ~50 per emitter |

## C. Scale and budget
- **Scale with the effect:** sizes above fit a ~8-stud impact. Multiply size, speed and spread distance together (a 2× effect = 2× size and 2× speed; lifetimes stay). The frame script decides the scale (screen %), not the table.
- **Budget per effect (v2):** S+A median 38 emitters, 12 unique textures, ~720 est. live at peak. Our caps: live ≤ ~1000 near the camera, Rate ≤400/s (100 mobile), unique textures as few as the shared set allows, ≤4 heavy effects per client at once. Low tier: drop decoration (embers, wisps, faint accents, extra twins), keep truth layers, flash, impact shape, ring and ground mark.
- **Estimate live particles:** Σ over burst emitters of EmitCount + Σ over streams of Rate × mean Lifetime.
