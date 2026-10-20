> Author: skill-builder · claude-opus-5-5 · default · 2026-10-13

# Flipbooks and kitbash

How to pick pre-made sprite sheets by looking at them, combine several into one effect, time, blend, tint,
size and randomise them on a Roblox ParticleEmitter, and mix them with Beam, Trail, lights and decals.
Evidence: `knowledge/reference/vfx/04-field-methods-flipbooks.md` (§1 field methods, §3 Part 8 rules, 3b, 3c),
`07-roblox-performance-accessibility.md` (ParticleEmitter rows, P-tags), `contradictions.md` (X-, PD- rows).
Tags: [spec] Roblox docs mirror · [study] · [preprint] · [practice] · [inference] (incl. arithmetic) ·
[P] PROPOSAL start value, untested, owner may change. Every [P] stays a proposal until a test or the owner settles it.

## A. Procedure (one effect)

1. Name the job: event, what it changes, rank 1-10 per viewer (rank orders only; no size/brightness mapping, 07 C-19; R-368) (FB-01).
2. Inspect each candidate sheet as data (section B) on bright and dark backgrounds (FB-02).
3. Cast roles: core / secondary / tertiary (section C); one job per layer (FB-08).
4. Check the seam: palette, value steps, contour density, edge hardness, cadence, light direction match (FB-09).
5. Mode and cadence: OneShot or Loop (FB-12); FlipbookFramerate / Lifetime from table D and 3b map (section F).
6. Blend: LightEmission, LightInfluence, Brightness, Color per layer (FB-17..FB-21).
7. Place: one Attachment, ZOffset, soft-edge workaround (FB-10, FB-22).
8. Repetition levers (FB-23..FB-25); sheet resolution vs screen size (FB-26..FB-28).
9. Static fallback with flipbooks off (FB-30); quality tiers (FB-11).
10. Review: frame-step capture at 60 fps and on a 30 Hz phone; VFX on and off (FB-07).

## B. Reading a sheet before use

| Look at | What to record | Reject or flag when |
| --- | --- | --- |
| Layout | Grid2x2 / 4x4 / 8x8 / Custom; px size; exact multiple of layout | not 1024x1024 or not an exact multiple (NotCompatible, playback off) [spec] R-214, R-211 |
| Cells | meaningful, empty, repeated cells; first meaningful, peak, last cell | peak lands late (see D "peak position"); cell 0 is not the impact |
| Silhouette | radial vs directional; edge; one readable shape at thumbnail size | edge or shape lies about the gameplay footprint (R-283, R-060) |
| Value | 2-3 value steps; dark base vs hot core; baked black background? | baked colour you must recolour (tints poorly); black bg on a normal-blend layer |
| Drawn timing | anticipation / punch / dissipation baked in; how many cells each phase holds | phases fight the game event timing; dissipation is only an opacity fade (FB-33) |
| Loop vs one-shot | does last cell flow into first? | Loop use with a visible wrap pop (FB-14); PingPong on an expanding blast (runs backward) |
| Baked parts | sparks, smoke, debris drawn in | duplicate of another layer's job |
| Alpha | straight alpha, greyscale-no-alpha, padding between cells | no padding (neighbour bleed at distance, FB-29) |
| Style | hard alpha cut-off (graphic) vs soft gradient (realistic) | style differs from the other layers (FB-09) |

## C. Kitbash roles

Role names are this skill's grouping [inference] of the 04 §3 "one job per layer" list (R-283; R-242; R-388).

| Role | Job | Typical parts | Blend / light | Drops first at Low |
| --- | --- | --- | --- | --- |
| Core | Event shape and onset; the hero read | primary flipbook (flash, fireball, impact), impact card, PointLight | additive, LightInfluence 0 | never (static fallback cell instead) |
| Secondary | Direction and material | sparks (VelocityParallel), chips (random static cells), smoke puff (dark base), Trail, Beam | sparks additive; smoke/chips normal, LightInfluence 1 | chips, puffs |
| Tertiary | Linger and evidence | dust haze, embers, lingering smoke tail, Decal scar | normal, LightInfluence 1 | lingering tails, embers |
| Real depth (not a sprite) | Big chunks | server-confirmed block bodies, mesh bits | scene-lit | n/a (gameplay) |

Order in time coarse to fine: mass first, chunks next, dust last and longest (R-287; 04 §1 film live-action).

## D. Tunables

| Parameter | default | range | move up when | move down when | hard cap | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| FlipbookFramerate, stylised layer | 15 [P] (on 2s of 30) | 5-30 [inference, 3b] | peak/emphasis layer (30); smooth soft smoke (24-30 option) | slow smoke 10 or 7.5; big/slow scale | 30 [spec] | R-211; R-112; R-267; R-275; 04 §3; PD-15 |
| FlipbookFramerate, 24-base | 12 [P] only where 60 Hz guaranteed | — | — | 30 Hz phones (uneven holds) | 30 [spec] | PD-15; 04 Conflicts (12 vs 15); R-112 |
| OneShot frames / Lifetime | ≤30 per s [P] | 16 cells → Lifetime ≥0.53 s; 4 → ≥0.13 s; 64 → ≥2.13 s [inference] | — | short punch: use fewer cells | render above 30 undocumented | R-211; R-209; X-42 |
| OneShot Lifetime min vs max | min = max [inference] | range allowed for organic only | organic variation wanted | hand-timed stepped cadence | — | R-211; 04 §3 |
| Peak cell position | first 25% of lifetime [practice, single C] | — | — | onset carries no meaning | heuristic, not rule | R-355; X-32 |
| Flash sprite Lifetime incl. fade | 0.05-0.1 s, brightest peak 2 f@60 = 33 ms [P] | — | 30 Hz phone misses it | flash count/s near limit | ≤3 flashes/s [spec] | R-388; R-344; PD-01; R-165 |
| Secondary layer onset offset | 0.033-0.067 s after core [P] | — | layers read as one blob | punch feels late | — | R-388; R-344; 04 §1 |
| Impact frame (2-tone card) | 0.05-0.1 s, hero hits only [P] | 1-3 frames test [inference] | owner wants more force | reduced-flash setting on | ≤3 flashes/s [spec] | R-278; R-404; R-037; PD-01; R-165 |
| Layers per effect | type recipe (v2; was ≤4 channels); [superseded v2: budget = textures + live particles, SKILL.md §4] [P] | — | blur test passes with headroom | phone frame time over budget | ≤4 full-detail blasts per client, rest core only [P] | PD-10; R-283; R-388 (18 parts / 6 groups) [practice C] |
| Emitter Rate | — | — | — | — | 400/s per emitter, 100/s mobile [spec]; Emit() vs cap: open | R-209; 07 rows |
| Lifetime | per role | — | — | — | 20 s [spec] | R-209 |
| Dust / smoke clear-by | sight-blocking see-through by 2 s; impact dust 1.5-3 s; collapse cloud ≤5 s [P] | — | weight lacking | target behind cloud unreadable | nothing over 8 s in play areas [P] | PD-16; R-031; R-363 [C]; X-54 |
| TimeScale, building-scale dust | 0.6 [P]; toy chips 1.0 | 0.4-1.0 [inference] | reads toy, owner wants toy | reads small, owner wants big | 0-1 [spec] | PD-17; R-222; R-313; X-55 |
| LightEmission | 1 core/sparks/fire; 0 smoke/dust/debris [inference] | 0 or 1 only [spec] | glow, energy | dark values must survive | stacked additive → white (flash risk) | R-211; R-209; R-399 [C] |
| LightInfluence | 0 emissive layers; 1 dust, smoke, debris [P] | 0-1 [spec] | layer must sit in stage light | must read in dark | set explicitly: default 1 Studio / 0 Instance.new [spec] | R-211; 07 P04; R-056 |
| Brightness (ParticleEmitter) | no number found | no range stated [spec] | self-lit layer too dim on brightest stage | outshines the threat | pure white only for top rank [practice C] | R-211; R-372 |
| ZOffset by role | core +1, sparks +0.5, smoke 0, ground dust -0.5 studs [P] | — | layer hidden behind others | draws over walls | never moves a danger footprint | 07 P05; R-211 |
| Ground-contact puff | ZOffset +0.25 to +0.5 × Size; spawn surface + normal × 0.25 × Size; Transparency 1 → target over first 0.1 s [P] | — | clip line visible | draws over geometry | — | 04 §3 soft edges; R-211; R-227 |
| Repetition variety | ≥2 sheets or ≥16 distinct cells; Rotation [0, 360]; Size envelope ±15-25% [P] | ~16 frames usually enough [practice C] | soak viewers spot repeats | silhouette loses identity | never randomise meaning | 04 §3; R-342; R-394; R-338 |
| Keypoints per Size/Transparency curve | 3-5 [P] | 2-20 [spec] | shape needs a hold | — | 20 [spec] | 07 P06; R-206; R-186 |
| Grid choice on 1024 | Grid4x4 large hero blasts, Grid8x8 small/fast [P] | 2x2 / 4x4 / 8x8 = 512 / 256 / 128 px tiles [spec + arithmetic] | effect large on screen | many silhouettes needed | 1024x1024 [spec] | 07 P03; R-212; R-214 |
| Tile px vs on-screen px | tile ≥ screen px at closest common distance (graphic); ≤2× magnification (soft smoke) [P] | — | blur visible | memory pressure | no blur threshold found | 04 §3; R-209; R-182 |
| Cell padding | ≥4 px in 128-px tile; ≥8 px in 256-px tile [P] | — | edge lines from neighbours at distance | — | spacing required, no px [spec] | R-209 |
| Unique flipbook sheets per stage | ≤8 resident [P] (~32 MiB uncompressed [inference]) | — | measured headroom on 2 GB Android | flipbooks auto-disable | no number found | 07 P21; R-209; R-036 |
| Static particle texture | 256x256 sparks/chips/motes; 512x512 puffs/large glows [P] | ≤512 unless large on screen [spec] | large on screen | tiny particle | 1024 flipbook only | 07 P18; R-200; R-332 |
| Trail Lifetime | 0.15-0.3 s thrown items, flying chunks [P] | 0.01-20 s, default 2 [spec] | direction unreadable | stale streak reads as live threat | 20 s [spec] | R-236; 07 P09 |
| Blast PointLight | Range 2-3× fireball radius, Shadows false, hold 2 frames, fade to 0 within 0.3 s; ≤4 transient blast lights per client [P] | light 1-2 frames, radius 2-3× [practice C] | world does not react | dark-stage frame time | Range 120 studs [spec] | PD-21; R-203; R-344 |
| Debris tier ratio per break | 1 : 5-10 : 20-50 chunks : cosmetic bits : dust [P] | — | break reads light | phone frame time | mobile 100/s per emitter [spec] | 04 §1; R-334; R-209 |

## E. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| FB-01 | Pick a sheet by job first (event, effect, strength). Reject a sheet whose silhouette, direction or baked timing misstates the gameplay footprint, however good it looks. | practice; R-283; R-060 |
| FB-02 | Before use, log layout, px, meaningful/empty/repeated cells, first/peak/last cell, baked parts, alpha convention; preview on bright and dark. A card without this log fails review. | practice C; R-355; R-211 |
| FB-03 | Author or accept sheets at exactly 1024x1024, an exact multiple of the layout. 2048 is out. 512 and non-square are untested: do not ship them until Studio shows Compatible. | spec; R-214; R-211; X-50; X-51 |
| FB-04 | A flipbook never stands in for real damage: VFX spawns from the server break event at its real bounds, and the hole is visible after dust clears. | practice; R-099; R-290; R-027 |
| FB-05 | Swap or remove the intact block under the brightest frame of the core layer, not at t = 0. Physics blocks run at simulation rate; never step them. | practice; R-363 [C]; R-295 |
| FB-06 | Scorch and crack decals are never larger than the removed area. | practice; R-032 |
| FB-07 | Every break VFX record names a sound id; review every breach with VFX on and off. | practice; R-011; R-021 |
| FB-08 | One job per layer (core shape, sparks direction, mesh depth, Beam path, Trail history, light response, decal evidence). Two layers with the same job: merge or drop one. | practice; R-283; R-242 |
| FB-09 | All kitbashed layers share palette, value steps, contour density, edge hardness, cadence and light direction. An incompatible realistic sheet is rejected, not hidden with Bloom. | practice; R-286; R-281 |
| FB-10 | Parent all layers to one Attachment at the contact point, oriented to the surface normal or attack direction; add a small source cue at contact. | spec + inference; R-175; R-211 |
| FB-11 | Library sheets for secondary and repeated effects; hero moments (egg hatch, boss-structure collapse) flag "new asset needed" instead of stacking stock cards. | practice; R-353; R-381; R-022; X-65 |
| FB-12 | OneShot for explosions, puffs, impacts (FlipbookFramerate is ignored; cadence = cells / Lifetime). Loop only for fire, auras, embers whose last cell flows into the first. PingPong only for reversible motion. Random for organic twinkle. | spec; R-213; R-211 |
| FB-13 | FlipbookStartRandom off when the onset carries meaning (impact, warning); on for loops and ambient. | spec; R-211 |
| FB-14 | Hide loop seams with: StartRandom, BlendFrames true, Lifetime ≤ one cycle, end-of-life fade, or a padded loop source (32 → 34 cells [practice C]). A synchronised visible wrap fails. | spec + practice C; R-393; R-211 |
| FB-15 | No per-cell hold exists: to hold a drawing, repeat its cell in the sheet or split phases into separate emitters with their own rate and Lifetime. | spec (absence); R-211 |
| FB-16 | Stepped (graphic) sheets use FlipbookBlendFrames false; soft smoke may use true (crossfade doubles silhouettes). At most one stuttery low-rate accent layer per effect. | spec; R-211; R-131; R-275 |
| FB-17 | Tint white or greyscale sheets with the Color ColorSequence (multiply). Baked-colour sheets: use as-is or reject; tint cannot add detail or brighten dark texels. Greyscale with no alpha: LightEmission 1. | spec; R-211; R-209; R-350 [C] |
| FB-18 | Toy-block worlds: dust and debris take the source block colour shifted to the nearest palette colour; reserved danger, reward and team colours are never decoration. | practice; R-313; R-104; R-033 |
| FB-19 | Smoke and dust are normal blend (LightEmission 0) so dark values survive; a puff that needs heat uses two emitters: dark base (0) + hot core (1). | spec + practice; R-211; R-286 |
| FB-20 | LightEmission does not light geometry: a blast that should light blocks adds a PointLight. | spec; R-211; R-218 |
| FB-21 | Set LightInfluence explicitly on every emitter (defaults differ between Studio insert and Instance.new). | spec; R-211 |
| FB-22 | Roblox has no soft particles: for ground-contact puffs use ZOffset, spawn offset along the normal, fade-in, soft authored alpha, smaller sprites near walls, or a flat decal/mesh ring. Check the clip line in a player-eye screenshot. | spec (absence); R-211; R-227 |
| FB-23 | Hide repetition with StartRandom, FlipbookFramerate range, Rotation [0, 360], RotSpeed range, Size envelope, Lifetime/Speed/SpreadAngle ranges, ≥2 sheets per material. There is no UV flip: use Rotation 180 or mirrored cells. | spec; R-211; R-342 [C] |
| FB-24 | Never randomise meaning: contact time, danger edge, team colour, power rank. Same weapon + same material = same break family. | practice; R-255; R-276; R-126 |
| FB-25 | Chips, shards, leaves: FlipbookStartRandom true + FlipbookFramerate 0 gives each particle one random static cell (8x8 = 64 silhouettes per sheet). | spec + practice; R-211; R-056 |
| FB-26 | Compute on-screen px ≈ 0.714 × S × H / D (S studs, D studs, H render px, FOV 70) and compare to tile px before choosing a grid. | inference; R-182; R-209 |
| FB-27 | Graphics memory follows pixel count, not disk size; reuse texture ids; few unique animated sheets per stage. | spec; R-200; R-209 |
| FB-28 | Stylised effects rarely need more than 4x4; use 8x8 only for small, fast or many-silhouette sheets. | practice C-; R-338; R-394 |
| FB-29 | Every cell has transparent padding; reject sheets with neighbour bleed in a zoom-out test. | spec; R-209 |
| FB-30 | Every sheet has a static fallback cell that still carries the meaning; danger and hit cues stay readable with flipbooks auto-disabled on low memory. | spec + practice; R-209; R-104 |
| FB-31 | Orientation: FacingCameraWorldUp for upright dust columns, VelocityParallel for sparks and streaks, VelocityPerpendicular for rings facing travel; Squash for stretch. | spec; R-211; R-215 |
| FB-32 | Freeze sprites in hit stop with TimeScale 0; nothing above 1. | spec; R-211 |
| FB-33 | Graphic smoke and poofs dissipate by a breakup cell range (carved, subdivided shape), not by a Transparency-only fade. Despawned debris fades; never pops. | practice; R-286; R-251; R-162; R-011 |
| FB-34 | Beams: continuous paths; Segments ≥ n-1 for n keypoints; animate by TextureSpeed or Texture swap (no flipbook). Trails: motion history; Clear() before reuse. | spec; R-177; R-236 |

## F. Cadence map (exposure → FlipbookFramerate) [inference, arithmetic]

| Exposure | base 30 rate | frames per drawing 60 / 30 Hz | base 24 rate | frames per drawing 60 / 30 Hz | OneShot Lifetime, 16 cells, base 30 |
| --- | --- | --- | --- | --- | --- |
| 1s | 30 (cap) | 2 / 1 | 24 | 2.5 / 1.25 | 0.533 s |
| 2s | 15 | 4 / 2 | 12 | 5 / 2.5 | 1.067 s |
| 3s | 10 | 6 / 3 | 8 | 7.5 / 3.75 | 1.6 s |
| 4s | 7.5 | 8 / 4 | 6 | 10 / 5 | 2.133 s |
| 6s | 5 | 12 / 6 | 4 | 15 / 7.5 | 3.2 s |

Non-integer frames per drawing = uneven holds on that display. Assumes render-time sampling (undocumented).
Tile map, 1024 sheet, H 1080, FOV 70 [inference]: 2x2 512 px (30 studs at 60 → 386 px); 4x4 256 px (12 at 30 → 308;
6 at 20 → 231); 8x8 128 px (2 at 10 → 154; 12 at 60 → 154). Phones may render below native height: test.

## G. Field methods a kitbasher copies

| Method | Copy as | Evidence |
| --- | --- | --- |
| Spider-Verse / Puss variable exposure per element | Pick FlipbookFramerate per layer (map F); gameplay contact, camera and input stay full rate | practice; R-271; R-267; R-275; R-112 |
| Explosions on 2s, 1s at the peak | Two-stage: stepped growth emitter, 30 fps peak emitter | practice; R-381 [C]; R-286 |
| Lowest-rate layer pops most | One stuttery accent per effect, never the threat | practice; R-275 |
| Two-tone smoke | Dark base (LightEmission 0) + hot core (1), 2-3 value steps | practice; R-286 |
| Designed dissipation (Turning Red, Bad Guys 2) | End-of-life breakup cells, hard alpha edges (scalloped), not opacity fade | practice; R-286; R-251; R-271 |
| Sprite library blended with sims | Shared palette, value steps, cadence, edge style hide the seam, not more layers | practice; R-286; R-281; 04 §3 film blend row |
| LEGO: sims replaced by bricks | Explosion = brick-sized chunk puffs popping on/off; little airborne dust, denser at wall bases | practice; R-135; R-303; R-313 |
| Smears, no motion blur | Short smear sprites or block-coloured ghost blocks | practice; R-251; R-135 |
| Anime impact frame | Rare 2-tone large card on hero hits only, reduced-flash option (D row) | practice + study [V: unverified]; R-278; R-037 |
| Anime spacing | Big jumps between cells or short fast lifetimes, not slow fades | study [V: unverified]; R-037 |
| Overwatch-style staggered onsets | Brightest layer shortest; secondary onsets offset (D row) | practice C; R-388; R-344 |
| Guilty Gear Xrd limited animation | BlendFrames false, scale pops instead of smooth tweens on hero effects | practice; R-131 |
| Textured glow (Puss) | Textured halo billboard, not Bloom alone | practice; R-277 |
| Self-lit cards at depths (Into) | LightInfluence 0 billboards, 2-3 layers separated by ZOffset and size | practice; R-381 [C]; R-286 |

## H. Open and conflicts

| Item | Status | Test |
| --- | --- | --- |
| 512 / non-square / Custom sheets play? | unresolved (X-51) | upload, read compatibility state in Studio and on a phone (O-1) |
| OneShot above 30 drawings/s | undocumented (X-42) | numbered 16-cell sheet at Lifetime 0.4 vs 0.6 s, 60 fps frame-step |
| Ground-dust ZOffset | 07 P05 says -0.5 studs; 04 soft-edge says +0.25 to +0.5 × Size: no PD row | player-eye screenshots, both values, on a ground hit |
| 15 vs 12 fps stepped default | PD-15 start 15; perceptual preference untested | 30 / 15 / 12 / 10 on 30 Hz and 60 Hz phones, owner picks |
| Toy-fast vs big-slow | owner decision (X-55) | TimeScale 1.0 / 0.6 / 0.4, ask "toy or building?" |
| Repetition visibility, tile blur point, sheet memory budget | no number found | 1000-repeat soak; grid × size × distance screenshots; F9 Memory on 2 GB Android |
