> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13

# Effect card and genre presets

Sources: `knowledge/reference/vfx/06-mistakes-08-card-09-review.md` (Output 8 card, worked example, T-xx tests),
`10-genre-presets.md`, `12-gaps.md` (G-xx), `contradictions.md` (PD start values, X rows). R-ids resolve in `00-sources.md`.
Tags: [study] [preprint] [practice] [spec] [inference] [P] (PROPOSAL start value, untested, owner may change).
Tunable shape: default | range | move up when | move down when | hard cap | evidence. "no number found" stays as written.

## A. Card rules

| ID | Rule | Test | Evidence |
| --- | --- | --- | --- |
| CD-01 | Fill `communication_job` and `importance_rating` before any `asset_id`. Card order: job, rating, trigger, truth, feeling, layers, timing, camera, sound, repetition, viewers, reduced, budget, review, evidence, meta. | No asset id on a card whose job fields are null. | 06 §8.1 order |
| CD-02 | `null` = not chosen. Never write 0 for "unknown". Write "no number found" where the evidence base has none. | grep the card: every 0 has a tag and basis. | 06 §8.1 null |
| CD-03 | Every number is `{v, tag, ev, tune}`. Every [P] path is listed in `evidence.proposals`. Status stays `draft` until Output 9 review runs; `owner_confirmed` only after the owner says so. | Count [P] values = count of `proposals` paths. | 06 §8.1; AGENTS.md §0 |
| CD-04 | `gameplay_truth` (area shape, size, fuse, contact, rate) is read from the gameplay config and the server. The VFX card never sets it. | Each truth value names its config field. | 06 §8.1 gameplay-owned |
| CD-05 | Drawn area = server area at cast, contact and expiry, in every quality tier, viewer variant and reduced mode. | Debug sphere of `area_size_studs` overlaid at contact: ring edge, flash edge and dust stop line sit on it in each variant (Output 9 R2). | [practice] R-060, R-080, R-033 |
| CD-06 | One distinct job per layer; delete a layer with no job (M-41). Layer count follows the type recipe (vfx-craft/references/pro-defaults.md §B; v2). [superseded v2: no emitter cap; budget = textures + live particles, SKILL.md §4; Low drops decoration layers.] ≤4 full-detail blasts per client; extras play primary layers only. | Count emitters + beams per tier; count live blasts in T-10. | [P] PD-10; R-351 (≈1 draw call per emitter, single tier C) |
| CD-07 | Over budget: merge layers that share sheet, blend (LightEmission), LightInfluence and phase; never merge a truth layer (area edge, contact, outcome) into a decorative one. Say which layers merged and why. | Merged layer keeps both jobs in its `job` text; truth layers untouched. | [inference] from CD-05, CD-06 |
| CD-08 | Rate importance 1-10 per viewer (player, ally, threatened). Only rating ≥8 gets 100% white core, FOV kick, post-effect flash, slow motion, camera moves. Trauma shake allowed from 3. | Channel list per layer vs rating. | [practice] R-368 single tier C; mapping [P] PD-06 (X-27: no source maps rating to parameters) |
| CD-09 | Big feedback only on a confirmed outcome (`success_dependent: true`): punch layers wait for the server result; the action cue stays small and never covers the impact point. | Rejected request: no punch layer plays. | [study] R-043 |
| CD-10 | Phase times in ms from the trigger. Source frame counts stay frames, "fps not stated"; own conversions use 60 FPS (1 f = 16.7 ms) and say so. | Every frame value has a fps note. | [spec] R-198; 06 keys |
| CD-11 | One sound event per visual landmark. Main sound locks to the punch frame: measured 0 to 40 ms late, never more than 1 frame early. | Phone screen + audio capture (T-07). | [P] PD-14; R-070, R-169, R-170 |
| CD-12 | Other players' non-threat effects: LocalTransparencyModifier 0.5, no shake, flash or post effect from others. Own effects, threats and pickups stay full. | Two-client capture: bystander view vs threatened view. | [practice] R-028; [P] PD-08 |
| CD-13 | Reduced-effects variant keeps footprint, contact, outcome and pickups. Flash -> steady shape, blink -> steady glow + countdown fill, shake -> none (M-89). ReducedMotionEnabled sets shake and FOV kick to 0. | Reduced capture still answers "where, when, what happened". | [practice] R-074, R-016; [spec] R-455 |
| CD-14 | Lights: Shadows false. Flipbooks: 1024x1024 sheet with a static fallback cell (flipbooks turn off on low-memory clients). Pool reset list complete (M-80). | `ParticleFlipbookTextureCompatible`; reuse a pooled copy 20 times, compare first and last. | [spec] R-200, R-214, R-209 |
| CD-15 | Short card allowed only when every viewer rating is ≤3, there is no area, threat or reward, and rate is known. Otherwise full card. | Rating and truth fields present on every short card. | bands [P] PD-06 (01: 1-3 / 4-7 / 8-10) |
| CD-16 | Name the genre preset(s) in every effect set and list each departure. No preset number is a validated genre default. | Deliverable header names the preset. | 10 scope (no Roblox VFX breakdown exists, G-88) |
| CD-17 | Genre not listed: blend the two nearest presets and state the blend. | Blend named in the header. | [inference] |

## B. Full card template

```yaml
# EFFECT CARD v1. null = not chosen. Number = {v, tag, ev, tune}. tag: study|preprint|practice|spec|inference|P
communication_job:
  what_it_is: null            # the event in plain words
  what_it_does: null          # gameplay consequence the viewer must understand
  how_big: null               # tiny | normal | big | rare_climax; matches the consequence (M-11)
  must_be_read_in_ms: null    # from gameplay, else "no number found"
importance_rating:            # 1-10 per viewer (R-368); bands and rights PD-06
  player: null
  ally: null                  # other player not threatened
  enemy_or_threatened: null   # anyone inside the area
  outranks: []
  yields_to: []
  rationale: null
trigger: {event: null, authority: null, success_dependent: null, cancel_or_interrupt: null, max_rate_per_s: null}
  # authority: server | client_predicted_server_confirms | client_cosmetic
gameplay_truth:               # read only (CD-04)
  area_shape: null            # sphere | box | cone | line, exactly as the server query
  area_size_studs: null
  origin: null                # attachment, contact point, surface normal
  telegraph_start_ms: null
  contact_ms: null
  active_end_ms: null         # last dangerous moment (M-05)
  hitbox_match_check: null    # overlay method + result (CD-05)
  footprint_locked_across_variants: true
feeling_target: {words: [], style_reference: null, reads_wrong_if: []}   # reads_wrong_if = Output 6 M-ids
layers:                       # one job each (CD-06)
  - name: null                # L1, L2 ...
    role: null                # primary | secondary | tertiary
    job: null
    phase: null               # windup | crescendo | punch | follow_through | dissipation
    roblox_part: null         # ParticleEmitter | Beam | Trail | PointLight | SpotLight | Highlight | Decal | MeshPart | camera
    asset_id: null
    flipbook: {sheet_px: 1024, layout: null, mode: null, framerate_fps: null, start_random: null, blend_frames: null, peak_cell: null}
      # layout Grid2x2|Grid4x4|Grid8x8|Custom; mode OneShot|Loop|PingPong|Random (R-213); fps max 30, OneShot ignores it (R-209)
      # start_random false for one-shots (M-73); blend_frames false = stepped drawings (M-72); null when not a flipbook
    blend_mode: null          # LightEmission 0 normal | 1 additive (R-211, M-22)
    light_influence: null     # always explicit: 0 self-lit, 1 scene-lit (M-24)
    colour: null              # ColorSequence keypoints
    transparency: null        # NumberSequence, fade in and out (M-67)
    size_studs: null
    lifetime_s: null          # cap 20 s (R-209)
    count: null               # Emit(n) or Rate/s; Rate cap 400, 100 on mobile (R-209)
    speed_studs_s: null
    emission_shape: null
    start_offset_ms: null     # from contact_ms; negative = before
    z_offset_studs: null      # flash over fireball over dust (R-211)
    orientation: null
    randomise: null           # decorative axes only; never footprint, contact, team, power (M-56)
    min_quality_tier: null
phase_timing: {windup_ms: null, crescendo_ms: null, punch_ms: null, follow_through_ms: null, dissipation_ms: null, fps_note: null}
camera_screen: {shake: null, hit_stop_ms: null, screen_flash: null, fov_kick_deg: null, post_effects: null, applies_to: null}
  # shake = trauma {add, exponent, decay_per_s, max_rotation_deg, falloff}, rotation only (R-124)
  # FOV clamp 1-120, default 70 (R-182); post effects never pulsed (M-84); applies_to self|players_in_falloff|all
sound_sync: {sound_events: [], visual_landmark: null, offset_ms: null, measured_offset_ms: null}   # CD-11
repetition_plan: {expected_rate: null, variants: null, random_ranges: null, semantic_invariants: [], concurrency_cap: null, escalation: null}
viewer_variants: {self: null, others_not_threatened: null, threatened_or_inside_area: null, offscreen_or_far: null}
reduced_effects_variant: {keeps: [], drops: [], replaces: []}
performance_budget: {target_device: null, max_live_particles: null, emitters: null, unique_textures: null, lights: null,
                     concurrency_tested: null, measured_gpu_ms_delta: null, pool_reset: []}   # GPU delta = Stats.RenderGPUFrameTime (R-461)
review_results: {truth: null, communication_importance: null, visibility_clutter: null, theme_polish: null, safety: null, performance: null, notes: []}
evidence: {source_ids: [], proposals: []}
card_meta: {id: null, version: null, status: null}    # status draft | in_review | owner_confirmed
```

**Short card (minor effects, CD-15):** `communication_job`, `importance_rating` (3 viewers), `trigger`, one line per
layer (name, role, job, roblox_part, asset_id, blend_mode, light_influence, colour, size, lifetime, count),
`repetition_plan` (rate, variants, concurrency_cap), `viewer_variants.others_not_threatened`, `reduced_effects_variant`,
`performance_budget.emitters`, `evidence.proposals`, `card_meta`.

## C. Worked example: heavy charge breaking a block wall (destruction preset)

Timed fuse; t = 0 = armed. Remote-trigger variant drops L2 and the windup. Gameplay owns radius and fuse.
**Merge (CD-07):** the source card had 6 emitters (L4, L5a, L5b, L6, L7, L8); PD-10 allows 5 at High. L5b outward puffs
merge into L5a as **L5 fireball**: same sheet, LightEmission 1, LightInfluence 0, colour ramp and phase; one emitter
fires `Emit(1)` at contact, then sets Size ×0.5 and Speed 8-14 and fires `Emit(3)` at +33 ms (Emit uses the properties
current at the call [inference]). L6 and L8 share a sheet too but L6 carries truth (its stop line = area edge), so they
stay apart. At Low (≤3 emitters): L4, L5 (no second Emit), L6; L7 and L8 dropped. Source card kept L7 at Low at half
count; PD-10 ("Low drops chips") wins.

```yaml
communication_job: {what_it_is: "Heavy charge stuck on a block wall detonates", what_it_does: "server breaks connected blocks in the sphere; hole; loose blocks fall, collectable", how_big: big, must_be_read_in_ms: "no number found; hole readable when L8 clears (T-12)"}
importance_rating: {player: 8 [P], ally: 4 [P], enemy_or_threatened: 8 [P], outranks: [ambient_dust, block_chip_small, pickup_sparkle], yields_to: [stage_climax_event, low_health_warning]}  # R-080, R-372, R-028; T-02, T-06
trigger: {event: "ChargeDetonated {charge_id, position, normal, radius, broken_block_ids}", authority: server, success_dependent: true, cancel_or_interrupt: "charge removed: stop L1-L3, no punch, Clear() emitters", max_rate_per_s: "gameplay config"}
gameplay_truth: {area_shape: sphere, area_size_studs: "gear table", origin: "charge attachment, wall normal", telegraph_start_ms: 0, contact_ms: 1500 [P], active_end_ms: 1500, hitbox_match_check: "debug sphere at contact; L1, L4 edges and L6 stop line on it"}
feeling_target: {words: [sudden, heavy, satisfying], style_reference: "chunky block debris, little gritty smoke (R-135, R-303)", reads_wrong_if: [M-01, M-03, M-09, M-32, M-36, M-51, M-54]}
layers:
  - {name: L1_area_ring, role: primary, job: "which blocks break", phase: windup, roblox_part: "flat ring MeshPart or Decal, radius = area", colour: "project danger colour", transparency: "fill 0.8, outline 0.2 [P] (R-336; T-03)", pattern: "dashed (R-015, R-398)", lifetime: "0 to contact", min_quality_tier: lowest}
  - {name: L2_fuse_blink, role: secondary, job: "armed + time left", phase: windup, roblox_part: "Neon strip + PointLight Shadows false", blink: "1 Hz armed, 2 Hz last 2 s, 3 Hz last 1 s [P] PD-13; 1500 ms fuse skips the 1 Hz step", min_quality_tier: lowest}
  - {name: L3_inward_squash, role: tertiary, job: "pre-punch tell", phase: crescendo, roblox_part: "charge mesh scale tween", start_offset_ms: "-33 [P] (R-380, 2 f@60)", scale: "0.85 [P] no number found", min_quality_tier: lowest}
  - {name: L4_flash_core, role: primary, job: "the punch: brightest pixel at contact", phase: punch, roblox_part: "ParticleEmitter, Enabled false, Emit(1)", blend_mode: 1, light_influence: 0, colour: "warm near-white (1.00, 0.96, 0.86) [P]", size: "0.8 x blast diameter [P] (R-363)", lifetime_s: "0.05 [P] PD-01", z_offset_studs: "1.0 [P]", min_quality_tier: lowest}
  - {name: L5_fireball, role: primary, job: "hot mass leaving along the normal + 2-3 smaller puffs carrying it outward (R-115)", phase: "punch -> follow_through", roblox_part: "ParticleEmitter; Emit(1) at 0, Emit(3) at +33 ms", flipbook: {layout: Grid4x4, mode: OneShot, start_random: false, blend_frames: false, peak_cell: "3 [P]"}, blend_mode: 1, light_influence: 0, colour: "white-hot 0 -> orange 0.3 -> grey-brown 1.0 [P]", transparency: "0 at 0, 0 at 0.6, 1 at 1.0 [P]", size: "core 0.4 -> 0.7 x radius; puffs 0.5 x core [P]", lifetime_s: "core 0.45-0.55, puffs 0.4-0.6 [P] (R-388)", speed: "puffs 8-14 [P], stop inside area", emission_shape: "cone along wall normal (R-344)", z_offset_studs: "0.5 [P]", min_quality_tier: "lowest (puffs: medium)"}
  - {name: L6_dust_ring, role: secondary, job: "radius and weight; stop line = area edge", phase: follow_through, roblox_part: "ParticleEmitter, Shape Disc, ShapeStyle Surface, facing normal", flipbook: {layout: Grid4x4, mode: OneShot, blend_frames: true}, blend_mode: 0, light_influence: 1, colour: "struck block colour toward grey [P]", lifetime_s: "0.6-0.9 [P] (R-363)", count: "Emit(24) [P]", speed_and_drag: "tuned so ring stops at area_size_studs; record values", min_quality_tier: lowest}
  - {name: L7_block_chips, role: secondary, job: "material + direction; NOT the collectable blocks", phase: follow_through, roblox_part: ParticleEmitter, flipbook: {layout: Grid4x4, mode: Loop, framerate_fps: 0, start_random: true}, blend_mode: 0, light_influence: 1, colour: "struck block colour (break event)", size: "0.3-0.6 [P]", lifetime_s: "0.6-1.0 [P]", speed: "20-40, Drag 10 (tutorial example R-189, not design evidence)", acceleration: "gravity 196.2 down [spec R-222]", emission_shape: "45° cone (R-344)", count: "Emit(16) [P] (R-248)", min_quality_tier: medium}
  - {name: L8_dust_cloud, role: tertiary, job: "weight and aftermath; clears the hole first", phase: dissipation, roblox_part: "ParticleEmitter, L6 sheet", blend_mode: 0, light_influence: 1, colour: "block toward grey, lighter top (R-344) [P]", size: "0.5 -> 1.0 x radius [P]", lifetime_s: "2.0-3.0 [P] PD-16", time_scale: "0.6 [P] PD-17", count: "Emit(6) [P]", start_offset_ms: "50 [P] (R-388)", emission_shape: "behind the L6 front, never ahead (R-363)", transparency: "fade in 0.1, out from 0.5 [P]", min_quality_tier: medium}
  - {name: L9_blast_light, role: secondary, job: "lights nearby blocks", phase: punch, roblox_part: "PointLight on charge attachment, Shadows false", colour: "desaturated warm white (R-344)", range: "2.5 x L5 core radius [P] PD-21", brightness: "8 -> 0 [P] no number found", timing: "hold 2 f, 0 by 150 ms [P] PD-21", min_quality_tier: medium}
  - {name: L10_scorch, role: tertiary, job: "history at the hole rim", phase: dissipation, roblox_part: "Decal on surviving rim blocks (client)", persistence: "until regeneration, then fade 0.5 s; ≤30 per client, oldest first [P] PD-18", min_quality_tier: high}
phase_timing: {windup_ms: "0-1100 [P]", crescendo_ms: "1100-1500 [P] (R-346)", punch_ms: "1500-1550", follow_through_ms: "1550-2050 [P] (R-388)", dissipation_ms: "2050-4550 [P]", fps_note: "R-380, R-387, R-344, R-388 fps not stated; 60 FPS conversions"}
camera_screen: {shake: {add: 0.5, exponent: 3, decay_per_s: "1.0 [P] PD-03", max_rotation_deg: "3 [P]", falloff: "linear to 0 at 3 x area from camera [P] (R-134)", delay_far: "distance / shock-front speed (R-363)"}, hit_stop_ms: "0 [P] PD-02", screen_flash: none, fov_kick_deg: "-4 in ≤0.15 s, off under reduced motion [P] PD-04", post_effects: none, applies_to: players_in_falloff}
sound_sync: {sound_events: ["charge_fuse_beep per L2 blink", "charge_detonate", "block_clack per landing (physics)"], visual_landmark: "first L4 frame", offset_ms: 0, measured_offset_ms: null}
repetition_plan: {expected_rate: "gameplay config", variants: "3 sheets (fireball, dust L6+L8, chips); variety from rotation 0-360, size ±15% [P]", semantic_invariants: [area_size_studs, contact_ms, L4 colour, L1 colour+pattern, onset order], concurrency_cap: "4 full blasts; more play L1, L4, L5 core only [P] PD-10", escalation: "chain links keep own centre and onset; onsets <167 ms apart drop secondary layers, never delay a punch [P] (R-144, R-138)"}
viewer_variants: {self: full, others_not_threatened: "L7, L8 at LocalTransparencyModifier 0.5; no shake/flash/post [P] PD-08", threatened_or_inside_area: full, offscreen_or_far: "skip puffs, L6-L10 off-screen; distance null (T-10)"}
reduced_effects_variant: {keeps: [L1, L4, "L5 core", L6, "L7 half count"], drops: [L3, "L5 puffs", L9, L10, shake, fov_kick], replaces: ["L2 blink -> steady glow + ring fill countdown (R-074, R-016)", "L8 lifetime x0.5"]}
performance_budget: {target_device: "low-end Android <2 GB, Quality Level 1 and Automatic (R-036)", max_live_particles: "51 (1+4+24+16+6, arithmetic)", emitters: "5 High (L4, L5, L6, L7, L8), 3 Low", unique_textures: "3 sheets 1024 + core + ring", lights: "1 during blast (L9); L2 is pre-blast", concurrency_tested: null, measured_gpu_ms_delta: null, pool_reset: ["Clear()", "Enabled false", "TimeScale 1", "Size/Speed restored after the puff Emit", "light Brightness 0, Enabled false", "ring Transparency 1", "disconnect events"]}
review_results: {truth: null, communication_importance: null, visibility_clutter: null, theme_polish: null, safety: null, performance: null, notes: []}
evidence: {proposals: [importance_rating.*, gameplay_truth.contact_ms, layers.*, phase_timing.*, camera_screen.shake.decay_per_s, camera_screen.shake.max_rotation_deg, camera_screen.shake.falloff, camera_screen.hit_stop_ms, camera_screen.fov_kick_deg, repetition_plan.*, viewer_variants.others_not_threatened]}
card_meta: {id: vfx.charge.heavy.wall, version: 2, status: draft}   # v2 = L5a+L5b merge for PD-10
```

### C.1 Example tunables

| Value | default | range | move up when | move down when | hard cap | evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Fuse `contact_ms` | 1500 [P] | test 400/600/800/1200 (T-01) | players fail to step away | owner rates it slow | floor above 213-231 ms reaction [study] | R-310 0.5-2 s [practice]; R-130; gameplay owns it |
| Fuse blink final rate | 1→2→3 Hz [P] | 1-3 Hz (T-04) | urgency rated low | n/a | 3 flashes/s [spec] | PD-13; R-165 |
| Crescendo | 400 ms [P] | 0/150/300/500 (T-08) | reads sudden-unfair | reads slow | no number found | R-346 single tier C |
| L4 flash Lifetime | 0.05 s [P] | 0.05-0.1 s incl. fade, peak 2 f@60 (PD-01) | "no punch" | flash count near cap | ≤2 large flashes/s design, 3/s governor [P]+[spec] | R-387, R-344, R-312; PD-11; T-09 |
| L5 core Lifetime | 0.45-0.55 s [P] | test 0.3/0.5/0.8 (T-09) | feels thin | clutters next blast | 20 s engine [spec] | R-388 single tier C |
| L8 dust Lifetime | 2.0-3.0 s [P] | 1.5-3 s impact dust | owner wants weight | hole unreadable | see-through by 2 s; ≤5 s; nothing >8 s [P] | PD-16; C-09 (R-363 vs R-031); T-12 |
| L8 TimeScale | 0.6 [P] | 0.4-1.0 (T-13) | reads "toy" when "big" wanted | reads slow/floaty | 0..1 [spec] | PD-17; X-55 owner call; R-211 |
| Chip / ring counts | 16 / 24 [P] | T-10 grid | looks sparse on PC | GPU delta high on baseline phone | Rate 400, 100 mobile [spec] | R-248 [practice]; R-209 |
| Shake max rotation | 3° [P] | 1/3/6° (T-14) | impact rated weak | comfort or aim error | 0 under ReducedMotion [spec] | R-124 trauma +0.5, t³ [practice]; PD-03 |
| Shake decay | 1.0/s [P] | 0.5/s test level | no number found | tail too long | no number found | PD-03; R-397 single tier C |
| Hit-stop (blast) | 0 ms [P] | 0/50/100/150 (T-15) | weight rated low | "lag" reports | no explosion number found | PD-02; R-154, R-134 |
| FOV kick | -4° in ≤0.15 s [P] | 2/4/8° (T-16) | n/a above cap | comfort complaints | 4° [P]; FOV 1-120 [spec] | PD-04; R-182; no source gives degrees |
| L9 light Range | 2.5x core [P] | 2-3x [practice] | blast floats | light spill on far blocks | 120 studs [spec]; ≤4 lights/client [P] | R-344 single tier C; R-203; PD-21 |
| Sound offset | 0 ms | 0 to +40 ms late, ≤1 f early [P] | n/a | n/a | 1 f early | PD-14; R-070, R-169, R-170; T-07 |
| Others' LTM | 0.5 [P] | alpha 100/70/40/0% (T-06) | own threat or pickup found slower in crowds | allies' actions unreadable | threats and pickups never reduced | R-028 [practice]; PD-08; no % found (C-14) |
| Size spread | ±15% [P] | 0/10/25% (T-17) | repeats spotted | footprint reads unstable | never on footprint (M-56) | no sourced range |

## D. Genre presets (start emphases, all numbers [P] unless tagged; source 10-genre-presets.md)

Shared baseline: truth over theme (R-060); big feedback on confirmed outcome (R-043); medium build (R-101 [study]);
rating ≥8 rights only (PD-06); composite ≤3 flashes/s [spec R-165], design ≤2; colour never alone (R-015);
others' effects reduced (PD-08); shake/flash/others sliders (R-074); 1024 sheets + static fallback (R-214);
sync per CD-11.

| Genre | Feeling | Importance ceiling | Palette and value | Camera and screen | Signature moments |
| --- | --- | --- | --- | --- | --- |
| Simulator | satisfaction, progress, triumph on rare | pickup 2, sell 4-5, purchase 5, level-up 6-7, Legendary 8, Mythic 9-10 (hatcher only, toast for others) | reward gold only on rewards; rarity by name + layers + motif; white only Legendary+ | none on collect/sell/UI; reveal push-in 3-12%, one shake Epic+ only | 02b R1-R6, V1-V8, U1-U5 |
| Destruction | impact, weight, satisfaction; humour on toys | block 1, group 3, wall/medium blast 5, huge 8, collapse 9 | block palette; additive only flash cores and sparks; desaturated blast light | trauma by mass and distance, t³, delayed by shock front; no shake per block; blast hit-stop 0; FOV only ≥8 | 02a explosions, material breaks, collapse; 02b R1 |
| Battlegrounds / combat | power, impact, fair danger | hit 2, heavy 4, crit 5, final blow 7 (≤4 bystanders), ultimate 9-10, telegraph at viewer 9 | ally/enemy by viewer relation; one colour per ability category | hit-stop 50/100/150 ms local (PD-02), none for throwers, rapid fire, crowds; review from target camera | 02a hits, windup, projectile, area attack, telegraph |
| Horror | fear, tension, relief | ambient 1, clue 3-4, threat + telegraph 8-9, rare scare 9 | low-value stage, small emissive accents; markers ≥3:1 [spec R-238] | no forced disorienting camera; vignette UI ≤40%, pulse 1 Hz (PD-12) | 02b A1, A3, A6; 02a danger zone, timer |
| Obby | flow, precision, triumph at checkpoint | jump 1-2, dash 3, checkpoint 5-6, finish 6-7, hazard telegraph 8-9 | edges, goals, hazards carry contrast; movement low saturation | no shake on movement; dash nudge 0.2 s; speed FOV +5° behind motion setting (PD-05) | 02b M1-M5, R6 |
| Tycoon | satisfaction, causality | tick 1, purchase 5, build done 5-6, unlock 6-7, rebirth 8 | one colour per resource; gold reserved; loops low saturation | none on ticks; unlock pan ≤1.5 s, skippable | 02b R2, U2, U5, R5, R6 |
| Disaster survival | danger, awe, urgency, relief | lethal boundary + warning 9-10, collapse 9, weather 1-2, survival reward 5 | one hazard colour + shape for all disasters; spectacle below the boundary | collapse trauma by distance; no takeover while a threat is live; lightning counts as flash | 02a collapse, huge blast, danger zone; 02b A5 |
| Anime-style | power, hype, graphic force | basic 2, special 5, ultimate 9-10 (only tier with impact frame) | hard light/dark split; two-tone smoke; one shape family per element | impact frame local, or full-screen ≤2 f@60 top tier only, in flash cap; zoom in, hold, out | 02a windup, crit, final blow, crescent trail; 02b M1, M4 |

| Genre | Density and clutter | Repetition | Mobile | Accessibility | Avoid |
| --- | --- | --- | --- | --- | --- |
| Simulator | same-kind pickups in 100 ms merge; ≤8 live copies, ≤10 particles each; coin sprites ≤20 | 3 recombined variants; escalate only on real outcome (R-094, R-043) | glow painted into UI sprites (R-220); coin flight ≤0.5 s, count-up ≤0.6 s | tier name + frame shape; paid random items show every % first [spec R-208] | celebration before confirm; near-miss; rarity tint in windup |
| Destruction | chunk : bits : dust 1 : 5-10 : 20-50; sight-blocking dust clear by 2 s | same material + weapon = same family; cosmetic size ±15-25%; ≥2 sheets or ≥16 cells | PD-10 budget; debris fades, never pops (R-011) | chain flashes ≥340 ms apart; reduced keeps footprint + outcome | VFX hiding a structural change; smoke ahead of shockwave; realistic smoke on toys |
| Battlegrounds / combat | ≤4 attention effects per viewer (R-139); PvP dimmer than PvE | each rapid hit keeps own onset (R-144); skins keep silhouette | muzzle next frame client-side; confirmed hit waits for server (R-102) | telegraph 600 ms (1 direction) / 1000 ms (2-4 choices) (PD-07) | indicator ≠ hitbox; crit hiding next threat |
| Horror | sparse anomalies; fog never hides hazard or route [spec R-174] | vary non-semantic parts; threat language fixed (R-087) | Atmosphere before near fog sheets (overdraw) | picture carries every warning without sound | red full-screen pulses; sound-only warnings |
| Obby | trails never cover edges or landing spot; Bloom Threshold ≥0.9 | landing puff Lifetime 250-350 ms; 3 sizes by fall height | first response ≤100 ms of tap (R-153); trail 0.15-0.3 s | reduced motion removes FOV, speed lines | trails that suggest a path; radial bursts that read as attacks |
| Tycoon | loops local and subordinate; cull unseen; ≤8 live copies | ticks merge; count-up ≤0.6 s; 3 variants | ≤40 live particles per continuous emitter (PD-20) | signed "+N/-N" with true balance | max spectacle on every purchase; lagging counters |
| Disaster survival | cut cosmetic smoke before threat geometry; safe route visible | hazard language identical every time; timers monotonic | worst overlap test at quality 1, 2 GB Android, 10-15 min (R-036) | warning = audio + visual + shape | spectacle hiding the safe route; lightning >3/s |
| Anime-style | one impact frame per beat; ≤1 stepped accent layer | stepped holds, FlipbookBlendFrames false; bespoke sheet per hero move | FlipbookFramerate 15 (PD-15); 4x4 at 1024 | reduced-flash swaps impact card for a steady local shape | soft motion blur; stepping physics blocks; inversion on routine hits |

## E. Untested (do not fill without a test; 12-gaps.md)

Rating -> parameter mapping (G-01); impact-frame length (G-08); punch and crescendo length (G-09, G-10); fuse cadence
(G-16); shake and FOV degrees (G-19, G-20); others' opacity % (G-27); dust linger (G-30); decal budget (G-31); toy vs
building speed (G-33); variant counts and random ranges (G-38, G-39); sound offset on phones (G-47, G-48); transient
light and Highlight cost (G-72, G-74); VFX frame share on the baseline phone (G-77); composite flash pass (G-80);
reduced mode keeps information (G-84); genre transfer of juice findings (G-85); credited Roblox VFX breakdowns (G-88).
