> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13. Revised by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (SC-69 information areas and height, SC-70 ambient effects).

# Scene, hierarchy and clutter

Where an effect goes, how loud it may be next to everything else on screen, and when it may peak. Effect-level
layer recipes and timing live in other reference files; this file judges the **composite** frame.
Evidence: `knowledge/reference/vfx/03-scene-rulebook.md` (V-xx rows, R-ids in `00-sources.md`) and
`contradictions.md` (X-xx, PD-xx). Every SC rule carries its V-id in brackets so the trail survives.

Tags: [study] peer-reviewed; [preprint]; [practice] named studio, practitioner or vendor (tier C = single maker
post); [spec] standard or Roblox docs; [inference] reasoning; [P] PROPOSAL start value, untested, owner may change.
"no number found" means the evidence base has none: do not invent one, run the named test.

## A. Scene review procedure

1. **Rate** every effect 1-10 for each viewer: self, other players/allies, enemies/targets (SC-12).
2. **Name the focus** of each effect (SC-01) and the decision each cue supports.
3. **Place** it in a band (§C table) and give it only that band's channels (SC-14).
4. **Build per viewer relation** (SC-44..SC-49); tone down others' non-threat effects.
5. **Check the stage**: effect × brightest, darkest, most saturated, most patterned surface (SC-50..SC-55).
6. **Stage the big moments** in order (SC-60..SC-68) and space them over time (SC-56..SC-59).
7. **Run the composite stress test** (SC-29) at max cadence and real player count; measure the §B budgets.
8. Report each check as gate-verified / MCP-verified / owner-confirmed / not verified, with the context of SC-30.

## B. Tunable values

| parameter | default | range | move up when | move down when | hard cap | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Attention-needing effects per viewer at once (own action, nearest threat, pickup, one ambient) | 4 [P] | sweep 2/4/8/16 + 1 pickup | sweep knee sits higher | find time or misses rise | knee of the sweep | working memory 3-5 items [study]; track "four or more" [study, abs]; R-139, R-145, R-029; 03 V-31 |
| Feature Congestion rise, busiest view vs effects off | ≤+30% [P] | correlate with the count sweep | FC rise shows no find-time cost | find time rises | none found | FC↔clutter rating rho 0.60 [study]; +28% FC ≈ +8% find time, +69% ≈ +21-28% [study + arithmetic]; R-014, R-029; 03 V-33 |
| Screen pixels changed by effects (difference image) | routine ≤20%; top-band peak ≤50% for ≤1 s [P] | test grid 5/10/20/35/50% | pickup still found fast at higher coverage | find-the-pickup time rises | no number found | no studio or study number; flash-area limits are not a coverage budget; R-168, R-396, R-029; 03 V-38 |
| Pixels brighter than stage diffuse white, routine play | ≤14% [P] | brightness sweep like the count sweep | top-band moment | focus loses pop | none found | 5.6-14% above reference white in 107 graded HDR stills (broadcast, not effects) [spec]; R-166; 03 V-39 |
| World 99th-percentile value below effect focus peak | ≥1 stop (2×) [P] | ExposureCompensation sweep, 0.5-stop steps | focus missed on bright stages | stage looks dead | ExposureCompensation -5..5, +1 = 2× [spec] | HDR headroom 1000/203 cd/m² ≈2.3 stops [spec + arithmetic]; R-166, R-203, R-355; 03 V-65 |
| Overdraw (dark-grey additive view: value ≈0.1 × layers) | frame avg ≤2.5 layers; hotspots ≤7 outside focus [P] | k-stack 1/2/4/8/16 on low-end phone | GPU frame time has headroom | GPU time over budget | none found; debugger saturates at 10 | 2.44-2.48 frag/px "quite high", 10× "too much", one scene [practice]; halving 3 emitters removed most 7+ overdraw [spec, Unreal]; R-132, R-204, R-332; 03 V-36 |
| Live particles per routine block impact, 8+ players blasting | ≤10 [P] | 3-10 per effect seen shipped | few players, GPU headroom | GPU frame time rises | Rate 400/s per emitter, 100/s mobile; Lifetime 20 s [spec] | shipped mobile cuts impact 30→2, 10 impacts 300→20 [practice, tier B]; R-248, R-385, R-209; 03 V-34, V-35 |
| Full-detail blasts per client | ≤4; [superseded v2: budget = textures + live particles, SKILL.md §4] [P] | test T-10 | — | GPU time rises | — | PD-10 start value; inference |
| Active Highlights per client | 20 [P] | test 10/20/50 | GPU headroom at 50 | RenderGPUFrameTime rises | 255 shown, extras silently ignored; disabled keeps its slot [spec] | first Highlight up to 1 ms GPU on mobile, cost grows with coverage [spec]; R-196, R-461; PD-09; 03 V-20 |
| Other players' non-threat effects | LocalTransparencyModifier 0.5 (50% opacity); no shake, flash or post effect from others [P] | A/B 100/70/40/0% alpha, threats pinned | comfort OK and players miss allies' actions | own threat/pickup find time rises | threats and pickups always full | no % in any shipped setting [practice]; WoW 3 levels; R-028, R-250, R-008; PD-08, X-72; 03 V-58 |
| Readable danger edge vs true radius | ±5%, never inside the hitbox [P] | test -10/-5/0/+5/+10% | — | stand-or-move errors | edge never inside hitbox | studio practice: must match, no tolerance stated [practice]; R-060, R-080; 03 V-43, V-44 |
| Focus onset lead over look-alike debris | ≥150 ms [P] | timed spot-the-spark test at phone size | focus still crowded | punch feels late | — | crowding drops at ≈150 ms separation in time [study]; R-138; 03 V-11 |
| Telegraph lead, avoidable hazard, phones | 600 ms one known direction; 1000 ms for 2-4 safe spots [P] | harness 400/600/800/1200 ms | hit rate below target | dodges trivial | floor 0.25 s rule of thumb [practice] | simple RT 230.8 ms, SD 26.8, n=1469 [study]; 4-choice 727-865 ms [study]; R-130, R-108, R-373; PD-07; 03 V-51 |
| Main action done by fraction of lifetime | 25% [P] | — | read test fails (action unclear) | "which hit was it" errors | — | "first quarter" [practice, single tier C]; R-355; X-32; 03 V-24 |
| Top-band screen-level moments per player | ≤1 per 30 s [P] | test every 15/30/60 s | session feels flat | fatigue rating rises | — | L4D peak 3-5 s, relax 30-45 s (threat model, not VFX) [practice]; rarer onsets capture more [study, abs]; R-140, R-077; 03 V-75 |
| Same-type flash spacing per viewer | design target 2 large-area flashes per rolling s [P]; ≥334 ms apart | tracking test | — | tracking errors | 3 flashes in any 1 s (composite); each bright flash layer ≤1% of screen [P] | WCAG ≤3/s or 0.006 sr in 10° field ≈2.8% of 1024×768 [spec]; R-165, R-167, R-077; PD-11, X-43, X-44; 03 V-55, V-78 |
| Looping pulse rate | lasting danger zones steady or ≤1 Hz; countdowns 1→2→3 Hz; low health 1 Hz; safe/heal ≤1 Hz [P] | classify test 0.5/1/1.5/2 Hz | — | — | 3 Hz at full contrast [spec] | heal <60 BPM [practice, single tier C]; danger "faster than a heartbeat", no bpm [practice]; R-346, R-071, R-165; PD-12, X-33; 03 V-21 |
| Contrast of critical markers vs local background | 3:1 floor [spec] | 4.5:1 standard, 7:1 high-contrast mode [practice] | high-contrast setting on | — | floor, not a target for every effect | WCAG 2.2; Microsoft XAG 102; R-238, R-059; 03 V-47 |
| FOV kick (big moment) | only rating ≥8, ≤4° in ≤0.15 s, off under reduced motion [P] | T-CAM | — | many players share scene | FOV clamp 1-120, default 70 [spec] | R-182; PD-04; 03 V-88 |
| Vision-blocking aftermath dust | see-through by 2 s; impact dust 1.5-3 s; big clouds ≤5 s [P] | T-DUST | — | target behind dust unreadable | nothing over 8 s in play areas [P] | THE FINALS cut lingering smoke on one gadget [practice]; R-031, R-363; PD-16, X-54 |

## C. Importance band → allowed channels (start map, PROPOSAL)

No source maps a rating to size, brightness, duration or count (X-27); this map is [P] (V-15, PD-06), tune by T-RANK.

| rating | blend and value | screen-level channels | other |
| --- | --- | --- | --- |
| 8-10 | additive core; 100% white core allowed | FOV kick, post-effect flash, slow motion, camera moves; trauma shake | 9-10 gets the largest area |
| 6-8 (below 8) | additive core, peak below pure white | none by default; trauma shake only on a rare heavy hit when the owner allows (shake is occasional) | Highlight allowed |
| 3-5 | normal blend, small additive accents, mid value | none by default; owner-allowed shake as above (t³ keeps +0.2 trauma at 0.8% of max) | — |
| 1-2 ambient | low saturation, value ≤ stage diffuse white, no onset flash | none | fade in, never pop |

## D. Rules

### 1. Focal point and eye path

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-01 [V-01] | One focus per effect: the element carrying the gameplay message (projectile head, contact point, blast origin, danger edge). Card field `focus` filled. | Freeze punch frame: reviewer points at one element. | [practice] R-367, R-120 |
| SC-02 [V-02, V-03] | The focus owns the value extremes and top saturation; the rest stays mid. Pure white only for ratings 8-10; 3 overlapping copies of a lower-band additive effect must not clip to white. | Greyscale + saturation-only views: focus is the peak patch; overlap test. | [practice, single tier C] R-367, R-372, R-120; X-29 |
| SC-03 [V-04] | Steer the eye with value, then colour, then shape; confirm with a timed find test, because vision science ranks colour, motion, orientation, size above luminance. | Blur/greyscale shows the path AND timed find passes. | [practice tier C] + [study] R-358, R-117; X-30 unresolved |
| SC-04 [V-05] | At windup, punch and aftermath the brightest, most saturated pixels sit on the top-priority gameplay element, never on dust or embers. Brightest is necessary, not sufficient. | Max-luminance pixel location per phase; timed "what to react to". | [inference + study] R-080, R-084, R-002 |
| SC-05 [V-06] | Leave calm, low-detail rest areas around the focus. | Edge-density map: busiest region = focus. | [practice] R-367, R-311 |
| SC-06 [V-07] | Direction reads in a still: brightest at the head, taper or blur the tail. | Pause at 3 path points; no head/tail confusion. | [practice] R-080, R-120 |
| SC-07 [V-08] | Windup cue sits on the screen spot of the later punch. | Overlay windup and punch frames. | [practice] R-071 |
| SC-08 [V-09] | Must-notice layers are at full strength on their first visible frame; ambient layers fade in. Onset alone fails when the player hunts a known shape: test. | Frame-step first frames. | [study] R-087, R-002 (1057 vs 998 ms vs 560 vs 557 ms ns); X-36 |
| SC-09 [V-10] | Toward-camera (looming) motion only for top-band punches, always paired with a brightness onset; routine debris moves across or away. | Classify main motion per layer. | [study] looming RT p=.087 ns, R-065, R-117; X-35 |
| SC-10 [V-11] | The focus differs from neighbours in shape, size, colour or motion, or leads them by ≥150 ms (§B); supporting particles stay uniform. | Punch frame: one differing feature or onset lead. | [study] R-138, R-054; X-37 |
| SC-11 [V-12] | Warnings are detected in peripheral vision at phone size while the player tracks something else. | Central task + peripheral warning vs no-effects baseline. | [inference] R-084, R-054; no number found |

### 2. Hierarchy across all effects

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-12 [V-13] | Rate each effect 1-10 per viewer group (self, others/allies, enemies) before building. | Card holds 3 ratings + decision each cue supports. | [practice, single tier C] R-368; X-28 |
| SC-13 [V-14] | Attention follows rating: size, brightness, saturation, motion, duration rank like importance. Control effects and decisive defences read stronger than plain damage. | Peak luminance × area and lifetime ranked; no inversion. | [practice] R-080, R-374 |
| SC-14 [V-15] | An effect uses only its band's channels (§C). | Channel audit per card. | [P] PD-06 |
| SC-15 [V-16] | Conflict order: (1) correct gameplay info (hitbox, threat, pickup, path), (2) readability, (3) theme. A theme layer that hides tier-1 info is cut. | Frame scan for hidden edges/pickups/path. | [practice] R-060 |
| SC-16 [V-17, V-18] | Prominence order: threat to the local player > own action feedback > pickups/objectives > other players' effects > ambient. Own-weapon feedback stays below threat. | Busy-scene measure; post-fight "describe your muzzle flash": most cannot. | [inference] R-071, R-028; [practice] R-071 |
| SC-17 [V-19] | Value bands: UI > effect focus > characters > world. | Median luminance per layer. | [practice, single tier C] R-355; "world last" [inference] |
| SC-18 [V-20, V-49] | Must-find actors win by outline/silhouette (Highlight, DepthMode AlwaysOnTop) before brighter particles; delete retired Highlights, do not disable them. | Count active Highlights vs §B; testers find pickup inside a blast cloud. | [practice + spec] R-071, R-195, R-196 |
| SC-19 [V-21] | Pulse rate carries meaning (§B rates); danger faster than safe; never above 3 Hz at full contrast. | Measure every loop's frequency. | [practice] R-071, R-346; [spec] R-165 |

### 3. Clutter and budgets

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-20 [V-22, V-27] | Cut fine detail that carries no gameplay; strip decoration from often-checked cues even at a cost in impact. | Remove one layer at play distance: same read = delete. | [practice] R-060, R-033, R-300 |
| SC-21 [V-23] | One dominant hue + one complement per effect; competitors desaturated. | 3+ dominant hues = fail. | [practice] R-120, R-374 |
| SC-22 [V-24, V-25] | Short effects; outros cut first; main action done by 25% of lifetime (§B); dissipate once the job is done. A new threat in the aftermath area is found first. | Timeline + aftermath find test. | [practice tier C] R-355; R-358 |
| SC-23 [V-26] | No danger border, hue or motion after the last damage tick (a deliberate blink-out is fine). | Stop on final tick. | [inference + practice] R-060, R-355 |
| SC-24 [V-28] | Strong saturation only for weapons, abilities, hazards, pickups; ambient grounded. | Saturation histogram per class. | [practice] R-300, R-100 |
| SC-25 [V-29, V-42] | Prefer a cheap non-particle cue (bloom pulse, shake, rumble) over a bigger burst when it carries the message; when capping, keep a cheap confirmation of the player's accepted action. | Swap test; at max cap accepted vs dropped input still distinguishable. | [practice] R-071; [inference] R-043 |
| SC-26 [V-30, V-31, V-32, V-33] | Noise budget follows rating; attention-needing effects per viewer ≤ §B count; pickup and threat hues differ from nearby effects; FC score tracked per build. | Count sweep + hue check + FC vs effects-off. | [study] clutter: find time 0.61→0.78 s (+28%), absent 0.81→1.86 s; R-029, R-014, R-139 |
| SC-27 [V-34, V-35, V-36] | Engine caps are ceilings, not budgets. Fewer, larger particles; cut per-effect count as concurrent emitters rise; halve worst emitters before shrinking the meaningful silhouette. | Scene Analysis Transparent/Particles counts; overdraw view; §B. | [spec] R-209, R-225; [practice] R-248, R-132; X-83 (cost = count × pixels × layers) |
| SC-28 [V-37, V-38, V-39] | Thin by screen coverage: fade opacity and size as coverage grows, thin near-camera particles, thin the costliest systems first under GPU pressure. Keep §B coverage and brightness budgets. | Camera inside smoke: pickup and path findable, GPU in budget. | [practice] R-114 (no threshold); [P] budgets |
| SC-29 [V-40] | Stress-test the full composite (all players, flashes, lights, post, UI, camera) at max cadence and real player count. Per-asset passes do not count. | Scripted worst-case replay on target phones. | [inference] R-041, R-080, R-167; no transferable number |
| SC-30 [V-41] | Every coverage, brightness or timing number lists device, resolution, quality level, FOV, camera distance, capture and display fps. | Missing field = fail. | [inference + spec] R-182; ms = 1000 × frames / fps |

### 4. Gameplay clarity

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-31 [V-43, V-44] | Readable danger edge = real gameplay geometry at cast, impact, expiry (§B tolerance); never inside the hitbox; scorch/crack marks never overstate the broken area. Offsetting indicators is an owner decision, never a default. | Overlay server blast sphere at 3 moments. | [practice] R-060, R-080, R-032; X-31 |
| SC-32 [V-45] | Ground zones: outline + fill, follow slopes and stairs, add a vertical or camera-facing edge. | View on flat, slope, stairs from play camera. | [practice, single tier C] R-336 |
| SC-33 [V-46] | Effects never cover HUD-critical UI; text over moving play gets a backing. | Worst composite: all critical UI legible. | [practice] R-074, R-355 |
| SC-34 [V-47] | Critical markers meet the §B contrast floor on every stage's lowest-contrast background. | Contrast measure per stage. | [spec] R-238; [practice] R-059 |
| SC-35 [V-48] | Colour is never the only channel; two sides: orange vs blue, not red vs green. | Colour-blind simulation; plan on 8% of male players (4-5% low case). | [practice] R-015, R-398; X-84 |
| SC-36 [V-50] | Decorative contrast stays out of path and target screen regions; play space lit. | Mark regions under the real camera. | [practice] R-100; third-person transfer [inference] |
| SC-37 [V-51] | Telegraph lead per §B, plus a sound cue ahead. | Dodge harness on 30 fps phone and PC. | [study] R-130, R-108; PD-07 |
| SC-38 [V-52] | Hit confirmation only for server-confirmed outcomes; attempt feedback is immediate and looks different. | Rejected predicted hit never reads as a hit. | [practice] R-102 |
| SC-39 [V-53] | Identity and indicator size survive every skin, tier or recolour. | Blind name-the-ability per variant. | [practice] R-060, R-049 |
| SC-40 [V-54] | Nonessential shake, head bob, blur, auto camera moves each have an off setting; feedback still reads at minimum. | Aim/move during shake at min setting. | [practice] R-074 |
| SC-41 [V-55] | Count flashes on the full composite against the strictest standard (WCAG); never merge standards; a toggle is not the fix. | Full-screen capture of worst overlap. | [spec] R-165, R-167, R-168; X-43, X-44, X-45 |
| SC-42 [V-56] | More players on screen = fewer, quieter effects each; PvP/crowded effects smaller, dimmer or more transparent than solo/PvE; no cinematic zooms with many players. | N = 1/8/16/max: local threat and pickup find time flat. | [practice] R-041, R-071; no-zoom [tier D lead + inference] R-443 |
| SC-43 [V-71, V-72] | Depth: background calm, midground carries contrast, foreground sparse. Depth of field off in active play (shops, menus, paused beats only) unless a test shows no find-time loss. | Mask effects; DoF on/off distant-pickup find time. | [preprint] R-063; [practice] R-114; [spec] R-190 (low-end may render differently) |
| SC-69 | Effects never cover what players use: other players and units, targets, the HUD, shop and placement areas, the smallest gameplay object on the floor. List those areas for the game camera and give each effect a maximum height: no tall columns over characters (a third-person or top-down camera looks down, so anything above a character hides it from others). One player's effect hiding what another needs is unfair, not only noisy. | Worst-count capture: effect pixels against the marked areas (`review.md` BL-09, IG-02). | [practice] |

### 5. Ally, enemy and other players

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-44 [V-57] | Build each effect per viewer relation; show a range or warning only to viewers who can act on it. | Spawn as each viewer type. | [practice, single tier C] R-368, R-049 |
| SC-45 [V-58] | Tone down by viewer relation, not caster: others' non-threat effects per §B; own, pet, NPC and anything threatening the viewer stay full. | A/B grid, threats pinned at 100%. | [practice] R-028; [P] PD-08 |
| SC-46 [V-59] | Offer a local clarity setting (all / reduced / essential, or per category); it changes only that player's screen. Default level: not stated in any source. | Two-client test. | [practice] R-008, R-028 |
| SC-47 [V-60, V-61] | One ally/enemy colour pair keyed to the viewer's relation, carried by outlines; one colour = one meaning per category, never reused as decoration. | Same effect seen by ally and enemy; colour-meaning table. | [practice] R-071, R-033, R-111, R-368; X-41 |
| SC-48 [V-62] | Allied spectacle only if the hostile-facing indicator, timing and primary shape are identical. | Compare enemy-facing frames. | [practice] R-049 |
| SC-49 [V-63] | On Roblox: server sends the event, each client draws for its relation. Per-player grades: ColorCorrectionEffect under the Camera; ColorGradingEffect only in Lighting (latest parented wins), set from the client. | Two-client post-effect test. | [spec] R-185, R-219; X-48 |

### 6. Stage palette and value room

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-50 [V-64] | Stage backgrounds muted (lower saturation, similar values); gameplay objects and effects brighter and warmer; the world never uses an effect's colour at that effect's value. | Per-stage saturation/value spread. | [preprint] R-063; [practice] R-100 |
| SC-51 [V-65] | Keep value headroom per §B. | Luminance histogram per stage. | [spec] R-166, R-203; [P] |
| SC-52 [V-66, V-67] | Test every effect on every stage's extreme surfaces; if the hue matches the stage add a complement. Fix the stage (quiet ground decoration) before boosting the effect, or log why not. | Effect × surface screenshot matrix; first logged change. | [practice] R-300, R-100 |
| SC-53 [V-68] | Adapt brightness per stage with one environment multiplier (or ExposureCompensation) in content data, not per-emitter edits. Brightness scales light only when LightInfluence = 0. | Scattered overrides = fail. | [practice tier C] R-378, R-356; [spec] R-211 |
| SC-54 [V-69, V-73] | Bloom only on focus pixels: set BloomEffect.Threshold so ambient does not glow (1 = only pure white blooms, 0 = all). Additive (LightEmission 1) for focus and sparks, normal (0) for smoke and dust. | Bloom-on screenshot; blend audit. | [spec] R-180, R-211; gameplay Threshold value: no number found |
| SC-55 [V-70, V-74] | Faint, wispy, desaturated effects fail on busy stages: use broad, crisp, bold shapes. The composition reads with bloom, lights and camera effects off. | Busy-stage first-glance ID; polish-off test. | [practice, single tier C] R-355; [inference] R-340 |
| SC-70 | Ambient stage effects (smoke, torches, embers, motes) stay tiny, slow and partly hidden: a little smoke, flames slowed, the base tucked behind a pillar or ledge, lowered until they only suggest; never the brightest or fastest thing near a sightline, and never in a reserved gameplay colour. A map mechanic's effect (teleporter, jump pad, hazard idle) stays in the background except at the moments the game-designer planned for it. | Capture near each sightline: the ambient layer is visible but not the brightest or fastest thing there (`review.md` CP-12). | [practice] |

### 7. Pacing over time

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-56 [V-75] | Alternate build-up, short peak, fade, quiet stretch; top-band rate per §B. | Intensity (brightness × area) per second over a session. | [practice] R-140 (VFX transfer = inference, X-74) |
| SC-57 [V-76] | Top-band channels (100% white, shake, full-screen post, loudest noise) are for peaks; routine repeats never use every channel. | Channel uses per minute, routine vs peak. | [practice] R-372, R-080 |
| SC-58 [V-77] | Scale intensity with outcome and rarity and tie it to success; no amplification step without an outcome change. | Intensity rank = outcome rank. | [study] Kao 2024 amplification without success: competence -.43, effectance -.19 (Model A n=678), R-043; Kao 2020 medium/high beat extreme, small effects, R-101; X-06..X-13 |
| SC-59 [V-78, V-79] | Space same-type onsets per §B and vary the cue. Tune top-band effects by overshoot then dial back until SC-13 and SC-26 pass; the threat ceiling always wins. | Onset spacing; version log shows overshoot + dial-back. | [study] R-077; [practice] R-307; X-73 |

### 8. Film staging of a big moment

| ID [V] | Rule | Test | Evidence |
| --- | --- | --- | --- |
| SC-60 [V-80] | Order: setup → beat before (at the payoff spot) → payoff → aftermath (follow-through, dissipation, reveal of changed space) → time to process. Instant effects may skip windup by design. | Reviewer marks every phase; ms per phase: no number found. | [practice] R-360, R-359, R-305, R-071 |
| SC-61 [V-81] | Setup: dim or pause competing effects before the peak so the payoff has a baseline to beat. | Pre-windup frame quieter than routine. | [practice] R-144 |
| SC-62 [V-82] | Beat before at two scales: object tell 1-2 frame inward bulge (fps not stated); gameplay telegraph per §B; camera slow push-in, short hold, fast pull-out, hold before the punch. | Tell present; hold precedes punch. | [practice, single tier C] R-380; R-310; [preprint] R-073 |
| SC-63 [V-83] | One peak per effect package; brightest layer 1-2 frames, shape full size fast; everything else dimmer and shorter. Start value: brightest peak 2 f@60 (33 ms) inside a flash sprite Lifetime 0.05-0.1 s [P]. | Mark the peak on the timeline. | [practice] R-387, R-312 (hit frame 0.1 s), R-300; PD-01, X-34 |
| SC-64 [V-84] | Hit-stop scales by weight, routine hits shorter. Start values [P]: weapon contact 50/100/150 ms (light/heavy/critical), local only; explosions and charges 0 ms; none on rapid fire or in crowds. | Per-tier parameter. | [preprint] R-073 7 f / ~10 f vs [tier D] R-431 11-15 f (X-01 unresolved); [study] enjoyed 0.37-0.39 s, unpleasant ≈0.54-0.55 s, outer limit (R-035, X-02); PD-02 |
| SC-65 [V-85, V-87] | Aftermath shows true radius (ground edge) and the changed space (hole, route, fallen blocks) through the dust; keep a player-sized scale anchor in the peak frame. Decoration never overstates collision truth. | Aftermath frame: edge = radius, change visible. | [practice] R-071, R-099, R-021, R-263 |
| SC-66 [V-86] | Exit order: main glow, then flare, then sparks, then small bokeh; a short breath between blast and embers. | Lifetimes ordered; durations: no number found. | [practice] R-312; [tier C] R-339 |
| SC-67 [V-88] | No film cuts by default: cinematic moves, zooms or slow motion only when control and threats are paused; FOV changes per §B. | Player safe/paused or keeps a usable view. | [spec] R-182; [inference]; R-443 lead |
| SC-68 [V-89] | Trigger visual punch and sound transient from one event; measure output per device. Start [P]: sound 0-40 ms late, never more than 1 frame early. | Captured onset offset. | [spec] R-170, R-169 (broadcast, not game budgets); [study] R-078; PD-14, X-17, X-18 |

## E. Studio methods worth copying

| Studio | Method | Source |
| --- | --- | --- |
| A large competitive studio (MOBA and shooter) | Goal order hitbox > readability > theme; 1-10 rating × 3 viewers over 750 abilities; 2-colour cut; white for ultimates; one colour per ability category; ornament above player height | R-060, R-368, R-374, R-372, R-033, R-100 |
| Blizzard WoW 11.2 | Spell Density: reduce only other party members' visuals (Everything / Reduced / Essential), no % stated | R-028 |
| NetEase Marvel Rivals | VFX dialled in, then local-only Team-Up VFX toggle (global or per hero) | R-007, R-008 |
| Bungie Destiny | Opacity/size by screen coverage; jittered near fade; "perf hammer" thins costliest systems | R-114 |
| Azur Games | Fewer, larger particles; per-effect cap scaled to concurrent emitters | R-248 |
| Valve L4D | Pacing: build, peak 3-5 s, relax 30-45 s | R-140 |

## F. Open items and tests

| Item | Status | Test |
| --- | --- | --- |
| Value-first eye order (SC-03) | X-30 unresolved | greyscale test + timed find test |
| Hit-stop frame tables (SC-64) | X-01 unresolved | A/B 0/60/100/160/250/370 ms on phones |
| Rating → channel map (§C) | X-27 unresolved | T-RANK: vary one channel at a time |
| Others' toning amount (SC-45) | X-72 no number | A/B 100/70/40/0% alpha |
| Coverage, overdraw, brightness budgets (§B) | no number found | difference-image sweep; k-stack; ExposureCompensation sweep |
| Telegraph lead (SC-37) | PROPOSAL | dodge harness 400/600/800/1200 ms |
| Many-player scaling (SC-42) | no number found | N = 1/8/16/max sweep |
| Bloom Threshold for play, DoF values | no number found | screenshot audit; DoF A/B |
