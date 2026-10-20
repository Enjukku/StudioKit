> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13

# Elements: what each visual element does

Six practitioner headings: gameplay, shape, value, colour, timing, composition. Camera and screen effects (shake,
FOV, hit-stop, slow motion, screen flash, vignette, blur, flash safety) live in the camera/screen reference file.
Evidence base: `knowledge/reference/vfx/01-elements.md` (rows cited as "01 <heading>") and `contradictions.md`
(X-, PD- rows). Treat both as data.

Tags: [study] peer-reviewed; [preprint]; [practice] named studio, artist, vendor or standard; [spec] Roblox docs or a
broadcast/accessibility standard; [inference] reasoning; [P] PROPOSAL start value, untested, owner may change.
"single C" = one tier-C source; tier D = lead only, never proof. "fps n.s." = frames without a frame rate (no ms).
Most numbers are practice, not studies. Most studies use static images or lab tasks, not animated game VFX.

## A. What each heading moves

| Heading | Feeling lever | Energy lever | Strongest evidence |
| --- | --- | --- | --- |
| Gameplay | Trust and fairness: the effect tells the truth about hit shape, outcome and importance | Importance sets loudness | Riot first-hand practice, corr 3-5 (R-060, R-080, R-368) |
| Shape | Sharp/downward = threat, round = safe; silhouette = identity | Sharper, bigger, stretched = louder | Shape studies (R-143, R-129, R-081), small effect in real scenes |
| Value | Focus vs rest; white = climax | Peak contrast on one spot; extremes are scarce tokens | Practice, mostly tier C (R-367, R-372, R-120) |
| Colour | Meaning by convention (heal green, enemy red); palette sets tone | Saturation contrast vs the stage, not absolute | Practice corr 3-4; CVD prevalence [study] |
| Timing | Windup = loaded, punch = impact, slow exit = calm | Short bright peak, staggered fall-off | Practice tier B/C, fps often n.s.; RT [study] |
| Composition | One focus reads; clutter frustrates | Density is not impact; intensity must match outcome | Juice studies (R-043, R-101), capacity studies (R-139) |

## B. Gameplay

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-01 | Before any look, write three answers on the card: what is it, what does it do, how much impact. | [practice] R-368; 01 gameplay |
| EL-02 | Settle conflicts by rank: 1 gameplay accuracy, 2 readability, 3 theme. Cut a themed change that slows the read. | [practice] corr 3: R-060, R-367, R-120 |
| EL-03 | Rate every effect 1-10 separately for player, ally, enemy. Size, peak value, saturation, sharpness and lifetime must rise monotonically with the rating; a basic hit never looks like an ultimate. | [practice] R-368, R-080, R-360; mapping [P] (X-27) |
| EL-04 | The drawn danger shape equals the server hit shape, at the same size on every skin. No "smaller for player, larger for enemy" bias unless the owner decides it. | [practice] R-060, R-080, R-033; X-31 |
| EL-05 | Predicted vs confirmed: the client cosmetic (muzzle, swing) starts on the next rendered frame; the confirmed-hit effect waits for the server result and looks different. On Roblox the server owns results. | [practice] R-102; transfer [inference] |
| EL-06 | One colour or silhouette per rule-bearing category, stable across the roster. Never reuse a rule colour for decoration. | [practice] R-033, R-268 |
| EL-07 | Tone other players' non-threat effects (PD-08 values). Own effects, threats and pickups stay at 100%. No shake, flash or post effect from other players. | [practice] R-028, R-008; values [P] |
| EL-08 | Own-weapon feedback stays below enemy and hazard cues. Review from the target's camera. If testers remember the muzzle flash, it is too strong. | [practice] R-071 |
| EL-09 | Quality tiers and the low-memory flipbook fallback remove decoration only. Every information layer survives the lowest tier with flipbooks off. | [practice] R-104; [spec] R-209, R-220 |
| EL-10 | No near-permanent glow outside home or empowered states: it reads as an active ability. | [practice] R-080 |
| EL-11 | Every telegraph uses at least 2 channels (VFX + sound or animation), so a missed glance is survivable. | [practice] corr 3: R-080, R-320, R-280 |
| EL-12 | Confirm-first: at game speed and camera distance, a viewer must tell that something happened before any polish. Block it in over-strong ("push to 11"), then dial back. | [practice] R-307 single |

| Dial | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Importance bands | 1-3 low, 4-7 mid, 8-10 high [P] | per game | n/a | n/a | 100% white core, FOV kick, post flash, slow motion, camera moves only at rating ≥8 [P]; trauma shake allowed from 3 [P] | R-368 scale; R-372; PD-06 |
| Others' non-threat effects (LocalTransparencyModifier) | 0.5 = Reduced [P] | 0 / 0.3 / 0.6 / 1 (test 100/70/40/0% opacity) [P] | crowded servers, clutter complaints | co-op where allies' effects carry info | own, threat, pickup never toned; discrete levels, not a slider | R-028 (3 levels) [practice]; R-008; PD-08 |
| Telegraph-to-hitbox edge tolerance | no number found | n/a | n/a | n/a | indicator = hitbox [practice] | R-060 |

## C. Shape

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-13 | One primary shape carries the purpose (missile front = damage); secondaries carry theme at lower value and saturation. No stacked or contradictory shapes. | [practice] R-367, R-120, R-360 |
| EL-14 | Sharpness tracks threat: damage = angular, downward spikes; heal, friendly, safe = rounded blooms. Expect a small effect in busy scenes (photo regression R²=.04). | [study] R-143, R-129, R-081; [practice] R-368 |
| EL-15 | Outward event = radial burst; aimed event = streak or beam; gathering or countdown = inward pull or vortex. | [practice] R-336 single C + [inference] |
| EL-16 | Ground area: circle for a radius, cone for a line. Low camera turns flat circles into ovals: add a thick vertical border ring or camera-facing element. Decals follow slopes. Lift = vertical shape; hold = floor ring. | [practice] R-336 single C; R-368 |
| EL-17 | Hard edge where the boundary carries information (hazard edge, vision blocker); soft edge for atmosphere. | [practice] corr 5: R-120, R-104, R-355, R-337, R-336 |
| EL-18 | Each weapon or charge has one signature silhouette; recolour freely, keep the silhouette. Success and fail differ in silhouette, not only colour (SF6 parry X vs hit O). | [practice] R-080, R-327, R-268 |
| EL-19 | Direction reads on a paused frame: stretch or taper along travel, sharp leading edge, wider trailing edge. Use `Orientation = VelocityParallel`; Trail `Lifetime` sets trail length. | [practice] R-080, R-337, R-344; [spec] R-209, R-236 |
| EL-20 | Low-frequency shape first, fine detail last; cut unneeded fine detail before raising brightness. ParticleEmitter has no erosion or dissolve: bake breakup into the flipbook frames. Coarser variants for small on-screen sizes. | [practice] R-060, R-344, R-338; [spec] R-211 |
| EL-21 | One exaggeration level per project. Stretch on fast motion, squash at apex and landing (`Squash` >0 taller, <0 wider). | [practice] R-302, R-131; [spec] R-209 |
| EL-22 | Visual scale is tuned apart from collision size, but never falsifies the danger border. | [practice] R-368, R-080; [inference] |

| Dial | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Silhouette test frame | punch frame at 64-128 px, greyscale; pass = viewer names it [P] | n/a | n/a | n/a | n/a | R-080, R-327, R-344 blur test; 01 shape |
| Flipbook frames per sheet | 4x4 = 16 (256 px tiles) [practice] | 2x2 = 4 / 4x4 = 16 / 8x8 = 64 / Custom [spec] | smooth smoke, large on screen | UI (≤9 frames [practice]), small on screen, punchy style | sheet 1024x1024 and an exact multiple of the layout [spec]; no 2048 path (X-50) | R-338 C-, R-394; R-211, R-212, R-214 |
| Trail Lifetime (s) | 2 [spec default] | 0.01-20 [spec] | slow, heavy travel | fast snaps, clutter | 20 [spec] | R-236 |
| Primary shapes per effect | 1 [practice] | 1 | never | n/a | 1 | R-367, R-120 |

## D. Value

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-23 | The focus owns the peak contrast (highest and lowest value), highest saturation and most detail; the rest is a rest area. If everything is important, nothing is. | [practice] R-367, R-358, both C |
| EL-24 | Supporting layers stay mid-value; 90-100% value and pure white only on the focus of rating ≥8 events. | [practice] R-120, R-372, R-360; band [P]; X-29 |
| EL-25 | Check value twice: greyscale screenshot on the brightest and darkest stage, plus a timed find test (X-30: value-first order is unresolved). | [inference] X-30 |
| EL-26 | At any moment the brightest pixel belongs to the top-priority gameplay element. Effects sit above characters and slightly below UI in value and saturation. | [practice] R-355 single C, R-060; [inference] R-080, R-367 |
| EL-27 | Additive (`LightEmission` 1) for hot cores; normal blend (0) for smoke so dark silhouettes survive. With LightEmission >0 dark colours turn transparent. `Brightness` scales only when `LightInfluence` = 0. | [spec] R-211, R-209 |
| EL-28 | Judge boldness at game speed and camera distance before polish: faint, desaturated, wispy first passes vanish in busy play. | [practice] R-355 single C |
| EL-29 | Climax = biggest contrast and saturation; dissipation = low contrast, low opacity. Spend peak contrast on one moment. | [practice] R-310 single |
| EL-30 | A heavy impact gets a brief world-light pulse at the impact point (one light lights both sides); no large uniform wash that erases silhouettes. More `Brightness` does not widen the lit area. | [practice] R-144; [spec] R-202, R-203 |

| Dial | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Supporting-layer value (HSV V) | 20-80% [P] | 0-100% | dark stage, effect lost | bright stage, glare | 0% and 100% avoided outside focus [practice] | R-120 (schematic, no numbers), R-360; 01 value |
| Focus peak value | 90-100% for rating ≥8 only [P] | per rating | rating ≥8 | rating ≤7 | 100% white = ultimates [practice] | R-372 C+; PD-06 |
| Focus contrast vs local background | ≥3:1 relative luminance [spec transfer, P] | ≥3:1 | missed in timed find | glare complaints | n/a | R-238 (static graphics) |
| Peak above stage diffuse white | ≤ about 2 stops [P] | sweep `ExposureCompensation`, Brightness in 0.5 steps | n/a | n/a | ExposureCompensation -5..5 [spec] | R-166 2.3 stops (broadcast HDR); R-203 |
| Bloom `Threshold` (post effect) | 0.9 on bright stages, re-tune per stage [P] | 0-1 [spec] | non-focus pixels glow | focus does not glow | only focus-tier pixels exceed it | R-180; R-363 single C |
| Blast light | Range 2-3x fireball radius, hold 2 frames, fade ≤0.3 s, Shadows off [P] | Range per blast | big blast, dark stage | crowding, cost | Range clamp 120 studs [spec]; ≤4 transient lights per client [P] | R-344 single C; R-203; PD-21 |
| `LightInfluence` on emissive cores | 0 [spec semantics] | 0-1 [spec] | effect should darken at night | must glow in the dark | n/a | R-211 (Studio insert default 1, Instance.new 0) |

## E. Colour

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-31 | One dominant hue plus at most one accent (a complementary pair needs one secondary); analogous or triadic palettes; several shades inside the hue family. | [practice] corr 3: R-120, R-374, R-355; R-358 |
| EL-32 | Saturation is relative: keep ambient grounded, reserve strong colour for weapons and abilities, avoid 0% and 100%. A goal-driven viewer may still miss the most saturated item. | [practice] R-367, R-120, R-300; [study] R-084 |
| EL-33 | Clash test: place each effect on the brightest, most saturated stage area that shares its hue; if it fades, add a contrasting secondary (all-orange shot in fire scenes got a blue secondary). | [practice] R-300; [study] R-029 |
| EL-34 | Recolour layers by function (hot core, flame, smoke). When the border is the message, the edge gets the peak, not a white centre. | [practice] R-286; [inference] |
| EL-35 | Keep hue conventions: heal green and never threatening, frost blue, gunpowder orange-red. Breaking one costs readability. | [practice] R-360, R-368; colour words [study] R-103 |
| EL-36 | Team colour follows the viewer's relation (enemy red, ally blue), never the caster, and always pairs with shape or outline. | [practice] corr 4: R-104, R-071, R-111, R-398 |
| EL-37 | Never colour alone for danger or outcome: add shape, symbol or pattern. Red often looks darker to CVD players. | [practice] R-398; [study] R-148, R-107 |
| EL-38 | Palette tone sets aggression: soft, lush palette = cute and chunky; harsh saturated = aggressive. | [practice] R-286 single |

| Dial | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Hues per effect | 1 dominant + 1 accent [practice] | 1-3 | stage hue clash (EL-33) | noise, mixed messages | no % split found | R-120, R-374 (cut to 2), R-355 |
| Blast colour-over-life (`ColorSequence`) | t=0 white-yellow, t≈0.15 orange, t≈0.5 dark red-brown, t=1 dark grey; smoke on a separate normal-blend emitter [P] | per material | n/a | n/a | n/a | R-344 single C (blackbody 0-3500 K), R-286, R-211 |
| CVD planning share | 8% of male players [study] | 4-5% low case [study] | n/a | n/a | n/a | R-148, R-107 (0.5 vs 0.6% girls unresolved, X-85); X-84 |
| Saturated-red flash test | pair with R/(R+G+B) ≥0.8 and chromaticity difference >0.2 counts as a flash [spec] | n/a | n/a | n/a | see camera/screen file | R-165 |

## F. Timing

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-39 | Name the phases on every card: windup, crescendo (skip for instant effects), punch, follow-through, dissipation. | [practice] R-346, R-345, R-115 |
| EL-40 | A dodgeable telegraph lasts at least reaction + choice + touch motor + render time; a cosmetic windup never delays a responsive control. Bigger attack = longer windup. | [study] R-130; [practice] R-310, R-373, R-302 |
| EL-41 | Punch: 1-2 frames of inward bulge, then the brightest layer for the shortest time, full shape fast. The visible consequence lands on the gameplay event. | [practice] R-380 single C, R-387, R-344, R-312 |
| EL-42 | One shared event marker drives flash, sound and camera. A steady small delay beats a jittering one. | [practice] R-346; [study] R-064, R-078; [spec] R-169 |
| EL-43 | Stagger exits: main glow first, flare almost as fast, sparks later, embers and bokeh last. Extra late sparks can break momentum. | [practice] corr 3: R-312, R-388, R-339 |
| EL-44 | Impacts front-load: the main action finishes or starts to fade within the first 25% of lifetime. Not for charges or sustained hazards. | [practice] R-355 single C; X-32 |
| EL-45 | No linear curves for motion, size or colour. NumberSequence interpolates linearly: add keypoints to ease. | [practice] R-355; [spec] R-211 |
| EL-46 | When gameplay ends the active signal retires visibly (hard blink-out or shape breakup); residue may fade but never suggests danger. Fade `Transparency` at start and end to avoid pop. | [practice] R-286, R-251, R-355; [spec] R-209 |
| EL-47 | Tempo: motion or pulse faster than a heartbeat reads danger, slower reads safe. Lasting zones steady or slow; countdowns speed up. | [practice] R-071, R-346 |
| EL-48 | One cadence per element; time the hit marker apart from the sprite cadence. Stepped cadence = punchy, hand-made. | [practice] R-112, R-275, R-286; [spec] R-211 |
| EL-49 | Length signals significance; lingering blocks later reads. Anything that hides a target is see-through by the clear-by time. | [practice] R-360, R-031, R-120 |

| Dial | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Telegraph lead (s) | 0.6 one known dodge direction; 1.0 for 2-4 safe spots [P] | test 0.4 / 0.6 / 0.8 / 1.2 [P]; spell examples 0.5-2 [practice] | phone hit rate low, more choices | players bored, never hit | floor: visual RT 0.213-0.231 s [study] + choice + motor | R-130, R-310, R-373; PD-07 |
| Brightest punch layer | 2 frames at 60 fps = 33 ms [P] | test 1/2/3/6 frames at 60 and 30 fps [P]; sources 1-2 frames, fps n.s. [practice] | effect lost at speed | strobing, glare | inside flash sprite Lifetime 0.05-0.1 s incl. fade [P] | R-387, R-344, R-312 (0.1 s); PD-01, X-34 |
| Full shape at size | about 80 ms [P] | 4-5 frames, fps n.s. [practice] | big, heavy blast | small hit | n/a | R-387 single C |
| Sound offset vs first punch frame | sound 0 to +40 ms late [P] | sweep -3..+3 frames | n/a | n/a | never more than 1 frame (16.7 ms at 60 fps) early [P]; broadcast +40 lead / -60 lag [spec] | R-169, R-170, R-078; PD-14, X-17 |
| Main action finish point | 25% of lifetime [practice single C] | test 10/25/40% | n/a | n/a | impacts only | R-355; X-32 |
| Whole-effect life | block-hit impact 0.4-0.8 s; big charge-blast core 0.8-1.5 s [P] | test 0.4/0.8/1.2 s | rating high | clutter, rapid fire | particle Lifetime 20 s [spec] | R-388 (0.5 s), R-189 (0.2-0.6 s), R-240 |
| Dust and smoke clear-by | see-through by 2 s; impact dust 1.5-3 s; huge-blast and collapse clouds ≤5 s at falling opacity [P] | test 1/3/5/10 s | weight, aftermath wanted | target behind it unreadable | nothing over 8 s in play areas [P] | R-363 (≥5 s, single C) vs R-031; PD-16, X-54 |
| Scorch/crack decal life | until structure regenerates, then fade 0.5 s [P] | n/a | n/a | frame time on low-end phone | ≤30 live decals, oldest fades first [P] | R-295, R-019; PD-18 |
| `FlipbookFramerate` (stylised sheets) | 15 (on 2s of 30) [P] | 7.5 / 10 / 12 / 15 / 24-30; 12 only where 60 Hz is guaranteed | smooth smoke | punchier, painted look | 30 [spec]; OneShot ignores it: frames / Lifetime, keep ≤30 [P] | R-112, R-388, R-416 (D); R-211, R-213; PD-15, X-42 |
| Danger pulse rate | lasting zones steady or ≤1 Hz; countdown 1 → 2 Hz (last 2 s) → 3 Hz (last 1 s) [P] | test per T-FUSE | imminence | lasting state | never above 3 Hz at full contrast [spec-derived] | R-165; PD-12, PD-13 |
| Heal pulse | below 60 BPM [practice single C] | test 40/60/80/120 BPM | n/a | n/a | not a default (X-33) | R-346 |
| Micro windup | 1-2 frames inward bulge [practice, fps n.s.] | n/a | heavy charge | rapid fire | n/a | R-380 single C |

## G. Composition

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-50 | Poster test: freeze the punch frame; a viewer points at one focus element. | [practice] R-406, R-367; test [inference] |
| EL-51 | One job per layer (core shape, sparks/debris, smoke/dust, light or ground mark). Each layer is removable by quality tier. Add a layer only if the blur test still reads. | [practice] R-144, R-388, R-295, R-283; [inference] |
| EL-52 | One hero per beat. When two effects collide, the lower-rated one dims or shortens. | [practice] R-080, R-071; [inference] R-368 |
| EL-53 | Emit in clumped cones and several directional bursts, not a uniform sphere; a ground blast throws debris in about a 45° cone. | [practice] R-344 single C |
| EL-54 | Rapid multi-hits: every impact gets its own onset (a per-impact flashing particle), or close hits fuse into one. | [practice] R-144 single |
| EL-55 | Tie intensity to the outcome; amplification beyond the outcome lowers felt competence. Put the reward beat after the action. | [study] R-043, R-101, R-079; [preprint] R-005 |
| EL-56 | Keep peak brightness and size rare: alternate short peaks with long quiet stretches. | [practice] R-140 (spawn model; transfer [inference]) |
| EL-57 | Separate depth layers: muted, cool background; bright, warm gameplay objects. | [preprint] R-063 qualitative |
| EL-58 | Aftermath shows scale: the ground-effect edge equals the true blast radius. | [practice] R-071; [inference] R-060 |
| EL-59 | Prefer a subtle cue on another channel (light pulse, sound, rumble) over more particles when it carries the message. | [practice] R-071; [preprint] R-082, R-073 |

| Dial | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Layers per normal effect | type recipe, vfx-craft/references/pro-defaults.md §B (v2; was ≤4 [P]) | test 2-6 channels | blur test still reads, rating high | mud, Feature Congestion high | [superseded v2: budget = textures + live particles, SKILL.md §4] [P] | R-144, R-388 (18 components); PD-10 |
| Full-detail blasts per client | ≤4; more play primary layers only [P] | n/a | n/a | frame time | n/a | PD-10 |
| Simultaneously relevant effects per view | ≤4 (own action, nearest threat, pickup, one ambient) [P] | test 2/4/8/16 | n/a | search misses | n/a | capacity 3-5 items [study] R-139; 4+ tracked R-145 |
| Particles per impact | no universal cap found | Azur mobile cut 30 → 2 per impact [practice] | n/a | overdraw, clutter | `Rate` 400/s, 100/s mobile [spec] | R-248 single B; R-209 |
| Live particles per continuous emitter (phones) | ≤40 (≈ Rate x mean Lifetime) [P] | ambient: low Rate, long Lifetime | n/a | n/a | n/a | PD-20 |
| Multi-hit spacing | separate hits ≥8 frames at 30 fps (267 ms) [practice] | <5 frames (167 ms) reads as one; 2-4 frames readable with per-impact flash [practice] | n/a | n/a | n/a | R-144 single, one 30 fps clip |
| Peak / relax pacing | peak 3-5 s, relax 30-45 s [practice] | n/a | n/a | n/a | n/a | R-140 (spawn model, not VFX) |
| Feedback amount | match outcome [study] | none / medium / high / extreme effects small (partial η² .003-.006) | success-dependent | amplified beyond outcome (competence -.43, Model A n=678) | n/a | R-101, R-043; X-06 (10.8% playtime not adopted), X-92 |

## H. Perception rules

Lab findings; applying them to VFX is [inference] unless stated.

| ID | Rule | Evidence |
| --- | --- | --- |
| EL-60 | A must-see layer starts with an abrupt onset (flash, burst), never a fade-in. | [study] R-087 |
| EL-61 | A hit flash is a brightness jump. A hue change alone guides attention weakly (luminance onset = probable guide; colour change = probably not). | [study] R-117 |
| EL-62 | Motion onset captures, ongoing motion does not: debris that starts moving at the blast is seen, ambient drift is not. A player hunting a known shape can ignore onsets, so the must-see layer also carries the goal feature. | [study] R-146; R-002 (2026, d=.026 in goal search); X-36 |
| EL-63 | Never rely on looming alone (shockwave toward camera); pair it with a luminance onset. | [study] R-147, R-117, R-065 (RT ns); X-35 |
| EL-64 | Make the key element differ from neighbours in shape, size, orientation, colour or motion, among uniform distractors. A spark among similar sparks does not pop. | [study] R-117, R-149, R-138 |
| EL-65 | Crowding: look-alike neighbours within about 0.4-0.5 x eccentricity blend. When the first layer must be read, offset look-alike layers by about 150 ms. No particle-gap number follows. | [study] R-138, R-054; X-37 |
| EL-66 | A repeated identical salient cue loses pull; streams of onsets disturb tracking. Keep onsets rare and vary repeated cues. | [study] R-087, R-077 |
| EL-67 | Design for pop-out: anything found by scanning costs about 20-50 ms per item (T-among-L order of magnitude). | [study] R-117 |
| EL-68 | Score clutter on Studio screenshots with a Feature Congestion-style metric; a pickup or threat sharing the background hue loses its search advantage (search +28% to +130% slower on varied backgrounds). | [study] R-142, R-014, R-029 |
| EL-69 | Stage contact, then reaction (hit, then debris): contact-then-launch reads as cause. | [study] R-097 |

## I. Conflicts and gaps

| Item | Status | Use |
| --- | --- | --- |
| Value extremes (X-29) | Avoid 0/100% vs focus takes highest and lowest | Mid-value base, extremes on the focus of rating ≥8 only |
| Value-first order (X-30) | Unresolved: art practice vs search guidance | Run greyscale and timed-find tests (EL-25) |
| Importance → parameters (X-27) | No source maps the rating | Bands are [P] (PD-06); test T-RANK |
| Indicator bias trick (X-31) | Tier A honesty wins | Owner decision only |
| 25% front-load, 60 BPM heal (X-32, X-33) | Single tier C each | 25% = impact default [P]; 60 BPM not a default |
| Linger (X-54) | Weight vs readability | Clear-by values PD-16 |
| Toy fast vs big slow (X-55) | Owner design choice | Blocks and chips stay fast; only big dust is slowed in tests |
| Sheets <1024 or non-square (X-51) | Unresolved | Author 1024x1024 until a phone test passes |
| Layer count, concurrent effects, effect-to-scene ratio, saturation band | No number in any source | Keep [P] values; run the 01 "Open / test ourselves" tests |
