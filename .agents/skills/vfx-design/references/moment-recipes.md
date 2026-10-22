> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13. Revised by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (MO-02 follows "shake is occasional"; §D split into what the effect owes and what `platform-policy` owns).

# Moment recipes

One compact recipe per gameplay moment. Use it after the importance rating and before the effect card.
Evidence base: `knowledge/reference/vfx/02a-moments-action.md` (02a), `02b-moments-reward-mood.md` (02b),
`contradictions.md` (X-/PD- rows). R-ids resolve in `00-sources.md`.

Tags: [study] [preprint] [practice] [spec] [inference] [P] (PROPOSAL start value, untested, owner may change).
"lead D" = tier D source, a lead only. "single C" = one tier C publication. Phases: W windup · C crescendo ·
P punch · F follow-through · D dissipation · HS hit-stop. f@60 = 16.7 ms frame (R-217 [spec]). P = 0 ms.
Importance = a studio's 1-10 scale per viewer (R-368 [practice], single C). No source maps the rating to size,
brightness or duration (X-27), so every rating below is [P]; test T-RANK.

## A. Rules

| ID | Rule (testable) | Evidence |
| --- | --- | --- |
| MO-01 | Rate every moment 1-10 for player (who causes or receives it), ally and enemy before picking layers. Coverage, peak value and lifetime must rise with the rating across the set (T-RANK). | R-368 [practice]; R-080 [practice]; X-27 |
| MO-02 | Screen-level channels (100% white core, FOV kick, post-effect flash, slow motion, camera moves) only at importance ≥8. Trauma shake (t³ keeps +0.2 at 0.8% of max) is occasional: rare heavy moments of the local player at ≥8, or below 8 only when the owner allows it; the "trauma" values in the recipes below apply only then. [P] | PD-06; R-372 [practice] single C; R-124 [practice] |
| MO-03 | Final blow of a match or a boss = importance 8: FOV kick allowed (≤4° in ≤0.15 s), slow motion allowed. An ordinary kill or finishing a prop or hero-mover part stays 7: no FOV kick, no slow motion, shake only. [P] | settles 02a final-blow row (7) vs PD-04; R-443 lead D; R-073 [preprint] |
| MO-04 | Gameplay information first, theme last: a live threat or telegraph is never out-ranked by reward, movement or ambient. The brightest, most saturated pixel on screen belongs to the top-priority element. | R-060, R-080 [practice]; 02b G10 [inference] |
| MO-05 | P fires on the server-confirmed state change (credit, sale, purchase, roll, break). No celebration before confirm; show a pending state if confirm takes >100 ms. | R-005 [preprint]; R-043 [study]; R-153 [practice]; 02b G1 |
| MO-06 | Amplify only what is tied to the real outcome; the request (button, throw, open) stays small. | R-043 [study] (competence −.43, n=678) |
| MO-07 | Sound transient from the same event as the P frame; measured offset 0 to +40 ms late, never >1 frame early. No deliberate sound lead. | PD-14; R-070 [study]; R-170 [spec]; X-17 |
| MO-08 | Flash safety on the combined screen: hard governor ≤3 general and ≤3 red flashes in any 1 s; design target ≤2 large-area flashes per rolling 1 s. Red pulses count as red flashes. | R-165 [spec]; PD-11 [P] |
| MO-09 | Hit-stop only on weapon contact, on the attacker's and the target's clients only (`camera-and-screen.md` §D). 0 ms on explosions, charges, the projectile's thrower, rapid fire and crowds. | R-156, R-134 [practice]; PD-02 [P] |
| MO-10 | Shake = trauma model, rotation only, shake = t³, delayed by distance for blasts. No shake on light hits, blocked hits, warnings, per block, dash in multiplayer. Respect the shake slider and off. | R-124 [practice]; R-363 single C; R-074 [practice]; X-40 |
| MO-11 | A telegraph, zone or area ring equals the real hit area and timing; progress ends and the cue is removed on the damage frame. Never draw an indicator larger than its hitbox by default. | R-080, R-060 [practice]; X-31 |
| MO-12 | Colour never carries meaning alone: add shape, icon, tier name or layer count. Must pass greyscale and a colour-blind filter. | R-398 [practice]; R-015 [practice]; 02b G7 |
| MO-13 | Anything that blocks sight is see-through by 2 s; impact dust 1.5-3 s; huge-blast and collapse clouds ≤5 s at falling opacity; nothing over 8 s in play areas. [P] | PD-16; R-031 [practice] (one gadget); X-54 |
| MO-14 | Debris fades, never pops; no floating leftovers after a break. | R-011, R-031 [practice] |
| MO-15 | Pulse rates: lasting zones steady or ≤1 Hz; countdowns 1 → 2 → 3 Hz; low health 1 Hz below the flash threshold; never >3 Hz at full contrast. [P] | PD-12, PD-13; R-165 [spec] |
| MO-16 | Reveal windup is identical for every rolled tier; escalation starts only after P. Windup stage count may follow the egg type bought, never the result. | R-316 [practice]; X-59 |
| MO-17 | A higher-tier layer never plays on a lower result (no near-miss). | [inference], both runs |
| MO-18 | Paid random items: odds per outcome visible before purchase (§D). | R-208 [spec] |
| MO-19 | Other players' reward and movement effects: LocalTransparencyModifier 0.5, no shake, flash or post effect from others. Threats and pickups stay full. [P] | PD-08; R-028, R-008 [practice] |
| MO-20 | Reduced motion (GuiService.ReducedMotionEnabled): tween Time 0 or swap motion for a fade; no FOV change, speed lines, push-in or camera dip. Separate controls for shake, full-screen effects, speed lines. | R-450 [spec]; R-074 [practice] |
| MO-21 | Toy-block vocabulary: effects built from block-shaped pieces in the block palette; toy-scale effects play fast, not slowed; no realistic smoke on blocks. | R-135 [practice]; R-313, R-303 [practice] |
| MO-22 | Frequent moments are shorter and subtler than rare ones; exits shorter than entrances. | R-370 [practice] single C; R-158 [practice] |
| MO-23 | Normal hit ≤4 channels; [superseded v2: budget = textures + live particles, SKILL.md §4]; ≤4 full-detail blasts per client, the rest play the primary layer only. [P] | PD-10; R-248 [practice] |
| MO-24 | Never random-start a meaningful one-shot (flash, telegraph, countdown); random static cells only for chips, shards, splinters. | R-209 [spec]; 02a build notes [inference] |
| MO-25 | Rapid or chained impacts each get their own onset: ≥170 ms apart for small local flashes, 340 ms for large flashes. | R-144 [practice]; R-138 [study]; PD-11 |
| MO-26 | Projectile head brighter than its trail; a charge never brighter than its release. | R-367 [practice] single C |
| MO-27 | Destruction and fuses are deterministic: no random fuse delay; countdown visuals track the server fuse. | R-255, R-080 [practice] |
| MO-28 | Every primary flipbook layer has a readable static fallback (low-memory clients turn flipbooks off). | R-209 [spec] |

## B. Shared tunables

| Value | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Brightest flash peak | 2 f@60 = 33 ms [P] | 1-2 f brightest; flash sprite Lifetime 0.05-0.1 s incl. fade [P] | lost on a 30 fps phone | rapid hits merge | MO-08 | R-387, R-344, R-388 [practice]; PD-01; X-34 |
| Hit-stop light / heavy / crit or finisher | 50 / 100 / 150 ms [P] | 0-400 test grid (T-HS) | hit reads soft | "laggy on repeat" | <0.54 s (enjoyable/stressful boundary, one VR game [study]); 30 f cap lead D | R-156, R-154 [practice]; R-035 [study]; PD-02 |
| Hit-stop when blocked | 0.67 × unblocked (≈35 / 67 ms) [P] | 0-1 × | block feels mushy | block slows combat | as above | R-442 lead D |
| Trauma per event | +0.2 small, +0.5 big [practice] | +0.05-0.6 [P] per row | weight rating low | motion discomfort | trauma clamps at 1 | R-124 [practice]; R-397 single C |
| Shake max angle at trauma 1 | 3° per axis [P] | 1-6° (T-CAM) | as above | aim lost | rotation only | PD-03; R-124 [practice] |
| Trauma decay | 1.0/s linear [P] | 0.5-1.5/s | event needs a tail | screen busy | — | PD-03; R-397 0.5/s [practice] single C |
| FOV kick (importance ≥8) | −4° in 80 ms, back in 150 ms [P] | −2 to −4° | — | comfort, reduced motion | ≤4° in ≤0.15 s; FOV clamp 1-120, default 70 [spec] | PD-04; R-182 [spec] |
| Final-blow slow motion (≥8) | 0.3× for 400 ms, 100 ms ease in/out, local [P] | 0.2-0.5×, 150-400 ms (T-SLOW) | finish not felt | other threat live | no global freeze (no global time scale [inference]) | R-082 [practice]; R-068 [study]; R-073 [preprint] |
| Telegraph lead | 600 ms one dodge direction; 1000 ms for 2-4 safe spots [P] | 400-1200 (T-DODGE) | hit rate high on 30 fps phone | fights drag | floor: simple RT 230.8 ms [study]; 4-choice RT 727-865 ms [study] | R-130, R-108 [study]; R-373 single C; PD-07 |
| Countdown blink | 1 Hz armed, 2 Hz last 2 s, 3 Hz last 1 s [P] | constant 1 Hz alt. | "when will it blow" errors | — | 3 Hz full contrast | PD-13; R-165 [spec]; R-346 single C |
| Zone fill | Transparency 0.75, opaque outline, pulse ≤1 Hz [P] | 0.5-0.9 (T-ZONE) | zone missed | occupants hidden | MO-15 | R-336 single C; PD-12 |
| Chain link spacing | 340 ms large flashes; ≥170 ms small [P] | 170-500 (T-CHAIN) | links miscounted | chain drags | <167 ms merges; ≤3 flashes/s | R-144 [practice]; R-138 [study]; R-165 [spec] |
| Dust clear-by | see-through by 2 s [P] | impact 1.5-3 s; big ≤5 s | blast feels weightless | targets hidden | nothing >8 s in play | PD-16 |
| Building dust TimeScale | 0.6 [P] | 0.4-1.0 (T-SCALE) | owner wants "big" | owner wants "toy" | blocks and chips never slowed | PD-17; X-55 (owner) |
| Collapse windup | 1.5 s creak + trickle + lean [P] | 0.5-3 s (T-COLLAPSE) | unfair deaths | drags | — | PD-19; R-001 [practice]; R-447 internal |
| Blast light | Range 2-3× fireball radius, hold 2 f, fade ≤0.3 s, Shadows off [P] | — | blast looks flat | — | Range 120 studs [spec]; ≤4 transient lights per client [P] | R-344 single C; R-203 [spec]; PD-21 |
| Trail Lifetime | projectile 0.15 s; swing 0.12-0.2 s; dash 0.2 s [P] | 0.1-0.4 (T-TRAIL, T11) | path unreadable | masks next swing | 0.01-20 s, default 2 [spec] | R-236 [spec]; R-305 [practice] |
| Spark start | Lifetime 0.2-0.6 s, Speed 20-40, Drag 10, SpreadAngle 180 [spec] | Emit 20-100 (T-MAT) | — | per-hit clutter | Rate ≤400/s, 100/s mobile [spec] | R-189, R-209 [spec] (tutorial, not a standard) |
| Sound offset | 0 to +40 ms late [P] | — | — | — | never >1 frame early | PD-14; R-070 [study] |
| Others' effects | LocalTransparencyModifier 0.5 [P] | size, lifetime, count cuts optional | — | crowd frame time | no shake/flash/post from others | PD-08 |
| Continuous emitter live count | ≤40 per emitter on phones [P] | Rate × mean Lifetime | — | frame time | Lifetime ≤20 s [spec] | PD-20; R-209 [spec] |
| Live Highlights per client | ≤20 [P] | 10-50 | — | mobile cost | 255 slots [spec] | PD-09; R-195, R-196 [spec] |
| Scorch / crack decals | persist until regen [P] | — | — | count | ≤30 live, oldest fades first [P] | PD-18 |

## C. Recipes

Column keys. Imp = player/ally/enemy [P]; "≤" = toned per MO-19. Layers = role → Roblox part. Timing in ms
unless f@60. "no number found" = no source in either research run.

### C1. Hits

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Light hit | 2/≤2/≤2 | contact here, small damage, direction | contact flash → OneShot flipbook on contact Attachment, Emit(1); flecks → ParticleEmitter VelocityParallel; target flash → Highlight (Occluded) FillTransparency eased to 1 | P flash 2 f@60, full size by 4 f@60; HS 50 melee, 0 projectile/rapid; F flecks 100-200; D ≤250 [P] | local high-value accent; no 100% white; base avoids 0/100% value (R-372, R-120) | small wedge along hit direction, fast expand then taper [inference] | none (MO-10) | transient on P; vary samples, never timing | smoke, light on rapid fire, full-screen flash, reward sparkle, hit-stop per rapid shot |
| Heavy hit | 4/≤4/≤4 | strong contact; next attack stays visible | dense core flipbook; directional breakup; dust puff; few debris; PointLight for P; camera | W per animation; P flash 2 f@60, core full 5 f@60; HS 100 attacker + target (AdjustSpeed(0), emitter TimeScale 0); F dust/debris 300-500; D ≤700 [P] | bright compact core on lower-value mass; no 100% white | clear force axis; squash then open; freeze on best pose; attacker vibrates, sideways on ground, vertical in air (R-134, R-144) | trauma +0.2, no FOV kick | contact on P; debris on own contacts | one HS length for all strengths; HS >0.5 s; shake on every hit |
| Critical hit | 5/≤4/≤4 | crit condition met, extra damage | base hit + distinct accent shape (star/burst) + crit number or icon; optional local impact card → one-cell sprite or BillboardGui | W 0; P accent + card 2 f@60; HS 150 melee, 0 projectile; F accent 200; D ≤500 [P] | distinct accent colour + shape (R-398); 100% white only if crit is top tier | sharp angular focal shape (R-081, R-129 [study]); enlarge the accent, not every layer | trauma +0.3, no FOV kick | accent layered on contact transient, same frame | full-screen flash per crit (breaks MO-08); hue-only difference; moving the contact point |
| Final blow, match or boss | 8/≤4/≤4 (MO-03) | target finished; reward next | heavy layers + defeat break (material row) + local slow motion + FOV kick + restrained aftermath; optional Camera ColorCorrection (counts as 1 flash) | HS 150; slow motion 0.3× 400 ms, ease 100; D aftermath ≤1.5 s [P] | peak contrast at completion; 100% white core allowed (≥8) | directional force resolves to a clean end | trauma +0.4; FOV −4° ≤0.15 s, back 150 ms; skip push if a live threat is near [P] | defeat transient on first HS frame; tail at normal speed | global freeze; victory before server confirm; celebration hiding a live threat |
| Ordinary kill / last part of prop or mover | 7/≤4/≤4 (MO-03) | target finished | heavy layers + defeat break + aftermath | HS 150; no slow motion; D ≤1.5 s [P] | no 100% white | as above | trauma +0.4; no FOV kick [P] | as above | FOV kick, slow motion |
| Blocked hit | 2/≤2/≤2 | landed, no damage, why ("need stronger gear") | ricochet sparks; surface flash → Highlight; "too strong" icon | HS 0.67× unblocked; P 2 f@60; F sparks 150-250; D ≤300 [P] | defence colour ≠ damage colour + shape cue | hard stop, tangential reflection; bright point on the surface | none | clink at contact; never silent (R-019) | debris, dust, the damaging burst |

### C2. Explosions

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Small (grenade, starter) | 3/≤3/≤3 | source, true radius, detonation moment | flash sprite + PointLight; core OneShot flipbook; leader + small sparks; debris cone; small smoke; optional scorch Decal | W bulge 1 f@60; P flash 2 f@60, core full 5 f@60; F sparks 0.2-0.4 s, debris 0.4 s; D core gone 0.5 s, smoke 1.0 s [P]; one 18-layer example lived 0.5 s (R-388 single C) | HDR-bright start; desaturated light, not saturated orange; brown dirt sinks, grey smoke rises (R-344 single C) | clumped cones, not a sphere; ground debris ~45° cone; squash then burst | trauma +0.15 within 1× radius → 0 at 3× [P] | detonation on flash frame | spherical spawn, blobby sparks, ring wider than damage radius, all layers peaking on one frame |
| Medium (barrel, charge) | 5/≤5/≤5 | source, true radius, what broke | small layers + dust skirt + physical debris + lit smoke + bloom spike + decal | W bulge 2 f@60; P flash 2 f@60, core full 6 f@60; F debris 0.5-1.0 s; D smoke 2-3 s, see-through by 2 s [P] | smoke brighter on top, darker below | big shapes first, then detail; shockwave outruns smoke; swap to destroyed mesh at flash peak (R-363 single C) | trauma +0.35, distance-delayed; no FOV kick [P] | as small; low body + debris tails | object vanishing before the flash; opaque screen-sized smoke |
| Huge (top weapon, charge stack) | 8/≤5/≤5 | something big happened; true radius; what is gone | flash · shockwave ring · fireball · hero chunks + small bits · dust skirt · smoke column · scorch · PointLight · bloom spike · Camera ColorCorrection | W bulge 2 f@60 (+100 pre-glow only if gameplay warns); P flash 3 f@60, fireball full 200, ring full 250; C secondary pops 100-300; F debris 1-2 s; D smoke ≤5 s, see-through by 2 s [P] | 100% white core allowed; dark smoke mass for contrast | low-frequency mass first; human-scale anchor in frame (R-263) | trauma +0.5 distance-delayed (start from RbxCameraShaker Explosion preset, R-403 single C); FOV −4° in 80 ms; ColorCorrection Brightness +0.2 → 0 over 150 ms = 1 flash [P] | transient on flash; heavy bass (R-264); debris tails on contacts | a small explosion scaled up; indicator bigger than real radius; debris pop-in |
| Chain | each link its size row; whole ≤8 | cause → effect link by link | per link flash + core; ONE shared residue smoke; optional fuse cue between links | link interval 340 large / ≥170 small; trauma +0.15 per link, clamped at 1 [P] | escalate only with real outcome (R-043); later links never cover the first impact point | sequence along the true propagation path | trauma accumulates (R-124) | one transient per link on its flash frame | all links peaking at once; >3 large flashes/s |
| Delayed charge (charge) | armed 5, last 1 s 7, detonation = size row | armed, spot, time left, radius | armed glow sprite + PointLight on charge; beep; last-second growth; optional true-radius ring for owner; detonation row | blink 1/2/3 Hz (MO-15); glow grows over last 1 s; inward squash last 2 f@60; detonate on server fuse [P]; fuse length: no number found (owner) | red/orange + shape cue; small area only | stable position, then outward impulse; one element grows while another shrinks (R-346 single C) | none while armed | beep on each blink onset; detonation on flash | random fuse delay; blink >3 Hz; countdown drifting from fuse |

### C3. Breaking (material tag drives emitters and sound; R-021, R-011)

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wood | 2 (4 if it opens a route) | what broke, the opening | few plank bodies; splinters → random static cells (FlipbookStartRandom, Framerate 0); light dust; scar Decal | P detach + chips 2 f@60; F splinters 0.3-0.6 s; D dust gone 0.8 s [P]; wood timing: no number found | warm brown from block colour, nearest palette colour | long thin splinters along grain and force; joists stay (R-323) | none; +0.05 only for large wooden structures [P] | crack on first detach; knocks on landings | metal sparks, round chunks, haze, uniform cubes |
| Stone / concrete | 3 (5 structural) | where the wall opened, cover left | slab bodies; rubble sprites; impact dust; trail dust emitter parented to falling chunks; crack decals | W crack-decal stage if damage accumulates; P detach + puff 2 f@60; F default gravity, no slowing; D dust 1.5-3 s, settled ≤2 s [P] | grey-neutral dust, LightInfluence 1; nearby lights tint debris (R-056) | real fracture shapes; dust size from fall height (R-334 single C); dust follows chunk rotation (R-137) | +0.1 per large slab landing within 20 studs [P] | break + each big slab landing | equal cubes, dust hiding the new opening, floaty fragments |
| Glass | 2 | pane gone, space open | thin shard particles, several silhouettes; few glints (LightEmission 1); tiny dust; no smoke | P shatter + glint 2 f@60; F shards 0.4-0.8 s; D glints off 1.0 s, shards cleared ≤2 s [P] | clear to pale; shards take light tint | texture particles, random static cell each (R-056, R-209) | none | crack on frame 1, scatter tail | thick chunks, dust cloud, sustained glitter (reads as reward) |
| Metal | 3 | dented or torn, what stands | bent/detached plate bodies; short sparks on hard hits only; little dust; dent Decal | P sparks Emit 20-40; F 0.2-0.6 s; D ≤0.8 s [P] | sparks LightEmission 1; hot yellow → orange → dark [inference] | streaks VelocityParallel; bend or tear, not chips (R-262) | +0.1 heavy blows only [P] | clang at contact, ring tail | soft dust billow, splinters, fireworks every hit |
| Toy plastic / block (default) | 1 per block; 3 group opening something | which blocks came loose, what stands, collectable vs waste | the real blocks as bodies (same as intact model); stud-pop accent sprite; tiny chips tinted from source block; minimal dust; no smoke | P stud-pop 2 f@60; F chips 0.15-0.3 s, blocks at real physics speed; D chips gone 0.4 s; HS none per block [P] | block palette only (R-313, R-314) | break by connection groups (R-324, R-135); pop = squash then stretch | none per block; camera belongs to the cause | clack at detach and per landing; voice cap needed, no number found | big or realistic smoke (R-303), motion-blur trails, identical dust per block |
| Building collapse | 9 | failing, where it falls, space changed, cover left | stress cues (crack decals, dust-trickle emitter, creak, lean); hero chunks as bodies; client-side small bits; chunk trail dust; ground dust bloom; decals | W 1.5 s creak + trickle + lean; P first big drop; F physics speed; D bloom 3-5 s, see-through by 2 s [P]; owner clip: stood ~3 s, tipped as one, ~6 s to ground (R-447 internal) | dark structural mass readable through restrained dust | apple-core (R-019); tip as one piece, break up on landing; coarse then fine (R-287) | trauma +0.6 at ground contact within 40 studs, falloff, t³, long decay; no FOV change [P] | sound from first visible movement, biggest at ground contact (R-001) | same timing every floor, bouncy debris, pop-in, floating leftovers, dust hiding escape routes |

### charge. Abilities and weapons

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Windup / charge | own 3; enemy charge at player 6 | attack coming, strength, release time, cancel | gather → ParticleEmitter Shape sphere, ShapeInOut Inward; growing glow core; step rings; tether → Beam | 3 steps, 2 f@60 pulse on each gameplay threshold; full-charge hold loop ≤2 Hz; cancel = 100 ms collapse; release on next rendered frame [P]; designer windup example 0.5-2 s (R-310) | brightness rises toward release; peak saved for P | inward/rising; squash before release | none at start value [P] | riser follows charge; tick per step; release transient on P | crescendo misstating timing; charge brighter than release |
| Projectile | own 3; incoming 6 | origin, path, position, will it hit | body (brightest) + Trail + optional small PointLight | trail Lifetime 0.15 s [P] | head highest value (MO-26) | tapered along velocity; VelocityParallel streaks | none | launch on release; impact on authoritative collision | trail brighter or wider than hitbox; flicker hiding position |
| Swing trail | 1 | path or arc | Trail between two blade Attachments; Beam for continuous laser | on from ~20% to ~80% of swing; Lifetime 0.12-0.2 s; WidthScale 1 → 0 [P] | below the impact; owner or team colour | crescent, sharp leading edge (R-337 single C) | none | whoosh at swing start [inference] | trail across teleport (call Trail:Clear()); masking next swing |
| Muzzle flash | 2 | fired here, this direction | OneShot flipbook at muzzle Attachment + PointLight/SpotLight; smoke wisp | P sprite + light 2 f@60 on next rendered frame after input, client side; F wisp 0.3 s; D ≤0.4 s [P] | short bright core, LightEmission 1 | directional cone along aim | heavy launchers only: pitch kick 1°, recover 120 ms [P] | shot transient on muzzle frame | flash hiding the aim target; rapid fire >3 large flashes/s |
| Weapon impact | 3 (heavy 4) | hit here, direction, material | contact core; accent on surface normal; material row fragments; mark Decal | P 2 f@60, full 4 f@60; HS 0 projectile; D core ≤0.4 s [P] | per material | oriented to incoming direction and normal | none unless heavy | on hit confirm (confirmed hits wait for round trip, R-102) | same response on every material or shield |
| Area attack | 5 | exact area, activation, expiry | true boundary (primary); source accent; shockwave ring → ring MeshPart tween or flat emitter; sparse interior | ring full radius 150, fade 200; boundary for whole active window, removed on last tick [P] | outline contrast + shape cue | real hit shape; thick vertical border rings (flat circles go oval), terrain-conformed (R-336 single C) | trauma by size row +0.15 to +0.5 [P] | warning, activation, expiry | dense fill hiding occupants; decorative rings read as the area; lingering after damage ends |

### C5. Warnings

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Telegraph | 9 for the threatened player | where and when the hit lands | ground boundary (part/MeshPart ring + Decal or SurfaceGui); progress fill or shrink-to-zero tween; source animation cue; audio cue; symbol; threat Highlight Occluded | lead 600 / 1000 ms (§B); progress ends on damage frame; removed that frame [P] | high contrast + pattern backup; orange is one game's AoE default (R-427 lead D) | geometrically true; short angular contours read threatening (R-081 [study]) | none; keep control | cue at telegraph start and at trigger (R-080) | bloom widening the area; random-start flipbook; lead below the reaction floor |
| Danger zone | 7 | hurts now, extent, end | stable perimeter part; low-rate interior emitter (no random start); hazard symbol | steady or ≤1 Hz; fade starts 500 before expiry, ends on expiry frame [P]; zone numbers: no number found | opaque outline, fill Transparency 0.75, colour + pattern [P] | hard true edge (R-104); thick vertical border | none | activation and expiry; low loop only if needed | fade that outlasts or precedes the hazard |
| Timer | 6 (by consequence) | time left before a real event | BillboardGui or HUD number/ring; final-state cue; ticks | tick 1 Hz; last 2 s 2 Hz; last 1 s 3 Hz max; progress monotonic [P] | contrast, not hue-only | monotonic unless gameplay changes it | none | tick per threshold; distinct expiry | false last-second holds; >3 Hz |
| Low health | 8 | health critical; recovery | HUD bar state (primary); edge vignette → ScreenGui ImageLabel or Camera ColorCorrection; heartbeat | enter ≤25% health; edge pulse 1 Hz, luminance swing <0.10 (not a flash); off on heal [P]; pulse rate: spec cap only | red edge, low opacity; centre clear | edge only | no shake, no tunnel vision | heartbeat on pulse; entry and recovery sounds | heavy red wash; pulse ≥3 Hz; anything removing control |

### C6. Collecting and rewards

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pickup (block credited) | 2/1/1 | this is mine now, at credit | local pop at pickup point; stream to backpack chip (batched); chip tick; burst Emit 6-10, Lifetime 0.2-0.4 s [P] | P 0-80 (scale 1.0 → 1.15); F 80-220 shrink to chip; D ≤80; whole ≤300; same-kind within 100 ms merge [P]; pickup timing: no number found | reward colour on the item, mid value; never brighter than a threat | compact block silhouette; exit eased in (0.3,0,1,1, R-157) | none | tick on credit frame; pitch steps up in a streak, reset 1000 after last [P] | combat-like burst, shake, full-screen flash (rare pickups only, R-151), tail >300 |
| Coins / blocks to counter | 2/0/0 | value travels to the right counter; final number true | representative ImageLabel sprites (not one per unit), cap 20 on screen; curved path; arrival pulse; count-up | P burst 200; F flight 500 eased in, 30 stagger; count-up ≤600; offsets 0/+80/+140 [P]; DevForum scripts 1.55-1.7 s [practice, lead D] | gold; brightest at arrival only; glow painted in (post effects skip GUI, R-220) | arcs converge on the counter; burst Quad Out, flight Quad In | none; reduced motion: chip pulse + "+N" only | ticks on first 5 arrivals, one closing chunk on final credited arrival [P] | paths over critical UI or threats; flights >1 s; count lagging spendable balance |
| Backpack full | 6 at transition, 3 held/0/0 | capacity reached; blocks not credited; go sell | chip state: bar full + "FULL" label + icon; one-shot pulse; deny cue per refused block; optional pointer to Sell button | P 150 (scale 1.0 → 1.12); F 300; static after; re-pulse every 2000, ≤3 times; deny ≤200, ≤1 per 500 [P]; no source | brightest HUD element for 450 ms only; never colour alone (owner O1: red vs own colour) | stable state; animate only transition and refusals | none | one "full" cue at transition; soft thud per refusal, rate-limited | celebration implying acceptance; endless flashing; modal in combat |
| Sell | 4, big haul 5/1/1 | backpack emptied, gold credited, amount | chip drains; coin burst at player; stream to gold chip; "+N gold" TextLabel; count-up | W 0 before confirm; P spark 0 + fountain +80 + "+N"; F stream 500, count-up from +140, ≤600; D 300 [P] | gold; burst size in 3 steps at ≥1×, ≥5×, ≥25× player's median sale [P] | sold goods visibly connect to proceeds | none; big haul gets a larger character-centred burst | sale chunk on confirm; ticks on arrivals; tally sting at count-up end | effect before confirm; endless coin shower; count-up >1000; locking the player |
| Level-up | 6/2/2 | new level and benefit active | rising rings/studs; "Level N" banner + benefit line; light pulse | P 150; C 300; F 600; D 400 (≈1.45 s); banner taps away; input never blocked [P] | gold-white below pure white | upward; banner overshoot (EasingStyle Back) | none near danger; else 5% zoom-in over 300, off under reduced motion [P] | sting on confirmed change | aura that looks like an active buff; covering threats or charge timers |
| Unlock | 6, stage 7/2/2 | named feature available, and where | lock breaks into blocks; silhouette reveal; stable unlocked icon; beacon at location until visited | W 300 (2 lock shakes); P 125 break flash; F 500 scale in with overshoot; D 300 (≈1.2 s) [P] | silhouette before ornament; reads in greyscale | settles into a usable state | stage gate: pan to gate ≤1.5 s, skippable, outside danger [P] | clack on P; chime when item fully visible | ownership before confirm; unlock bigger than Legendary |

### C7. Reveals by rarity

Windup V1 (all tiers, MO-16): 3 wobble beats at 0/450/900, each 250 ms, amplitude ×1/×2/×4, one crack stage per
beat, neutral warm-white crack light, P at 1350 [P]. Ratio from Pokerogue code (beats 2000/3500/5000, hatch 5875;
R-439 lead D). No rarity tint before P (R-316 [practice]); tell A/B is open (X-58, T5). Tap per beat, pitch
rising; crack sound on beat 3. Optional 3% push-in, off under reduced motion [P].

| Tier | Imp self/other | Added layers (cumulative) | After P [P] | Item visible [P] | Colour (project [P], R-465) | Camera [P] | Sound |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common | 3/0-1 | flash (UI Frame transparency tween, 125 ms, R-439 lead D), shell blocks out, item pop with overshoot, tier frame + name | ≈1.1 s (hold 600) | P+125 | stone grey; flash peak ≤80% white | none | pop on P; jingle ≤400 ms |
| Uncommon | 4/1 | + ring burst behind item (300) | ≈1.2 s | P+125 | lime | none | + chime |
| Rare | 5/2 | + light rays (C 200), sparkle burst, banner | ≈1.6 s (hold 800) | P+325 | azure | none | + sparkle tail |
| Epic | 7/2 | + crescendo 600 (converging particles), motion ring | ≈2.1 s (hold 1000) | P+725 | violet | push-in 4% across C | + riser ending on item frame |
| Legendary | 8/3 (toast only) | + crescendo 1000, unique motif (Grid8x8 OneShot), 1-2 frames pure-white core on item frame, inspect hold until tap (auto 2500 in quick-open) | ≈2.9 s + hold | P+1125 | gold, textured glow not Gaussian (R-277) | push-in 8% + one decaying shake ≤300 | + fanfare on item frame; music ducks |
| Mythic | ≥8 | + crescendo 1200, tier-colour screen-edge vignette, name banner | ≈3.5 s + hold | P+1325 | magenta | push-in 10% + one shake | longer sting |
| Secret | ≥8; others server toast only | + crescendo 1250, silhouette morph | ≈4.2 s + hold; tap to reveal ≤6 s total | P+1375 | black + animated rainbow edge (UIGradient) | push-in 12% + two shakes ≥400 apart | unique sting; toast sound for others |

Ladder basis: intensity grows with rarity (R-071 [practice], direction only); rarer rewards gave longer post-reward
pauses (R-088 [study], abstract); 10 s attention limit (R-153). Every push-in, shake and pure white off under reduced
motion. Item silhouette visible on every frame from "item visible" on (frame-step, T6). Each tier nameable without
its colour (T7).

Quick-open (up to 25) and skip: a tap any time after confirm jumps to P; minimum hold 500 with item + tier
name; tiles pop 50 apart, lowest tier first; only the best tile plays its C and F; best tile ×1.2; one shared flash
per batch; ≤5 tile sounds/s; batch ≤2500 + best-tier C; option to auto-skip Common and Uncommon [P]. Basis: R-439,
R-437 lead D; MO-08.

### C8. Movement

| Moment | Imp | Job | Layers | Timing | Value / colour | Shape / motion | Camera | Sound sync | Leave out |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dash | 3/2/2 | start, direction, destination; any damaging part | start puff; Trail along path; arrival puff | puff 0-100; trail 200; arrival 150; no freeze by default [P]; Celeste freeze 0.05 s, directional shake 0.2 s (R-154 [practice]) | movement palette, low saturation; silhouette clear | trail along real path, broken across gaps | none; optional 0.2 s directional nudge, off under reduced motion [P] | whoosh on start; scuff on arrival | cloud hiding destination; shake per dash in multiplayer |
| Jump | 2/1/1 | takeoff; double-jump state | small ground puff (Grid4x4 OneShot, LightEmission 0, LightInfluence 1); double-jump ring | puff Lifetime 250-350; ring 200 [P]; no number found | surface-material dust, low contrast | puff flat, then breaks up | none | foot leaving ground | radial burst that reads as an area attack |
| Landing | 2, big fall 4 | contact and how hard | dust ring sized by fall height (3 steps); optional bits | F 200/300/400 by step; D 300; big fall camera dip 150 [P]; Celeste long-fall shake 0.5 s (R-154) | surface-material dust | outward ground motion | big falls only; off under reduced motion | ground contact, heavier with height | same big landing every step |
| Speed lines | 1/0/0 | you are boosted | sparse streaks (Squash >0, VelocityParallel) at screen edges or along velocity | fade in 150, hold while above speed threshold, fade out 200 [P] | low-contrast white [inference], out of the focal path | radial or along velocity, consistently | FOV +5° over 200 as a sustained state (not a kick), gated by motion setting [P] (PD-05) | wind loop scaled to speed | full-screen high-contrast lines; lines without real speed |
| Teleport | 5/3/3 | departure, arrival, now here | departure: body breaks into blocks + light column (Beam); arrival: column + blocks assemble + marker | W 300 glow; P 100 pop; fade 150 out/150 in if loading; arrival P 100; F 400; D 300 [P] | navigation colour (blue, project [P]) | clear jump, no fake path; break up by subdividing shapes, not opacity (R-286) | fade through a dark block colour, never white | departure and confirmed arrival as two sounds | continuous trail suggesting a path; white flash; long transitions |

### C9. Ambient and mood (importance 1, 2 where it changes play; never the brightest pixel)

| Moment | Layers | Values [P] unless tagged | Leave out |
| --- | --- | --- | --- |
| Dust in light | sparse motes in light volumes (Grid2x2 static random); optional SunRaysEffect | Lifetime 6-10 s; speed 0.1-0.3 studs/s; Rate ≤5/s per volume (≈40 live); fade in and out 30% of life each (abrupt onsets capture attention, R-087 [study]) | bright pulsing motes near interactables; pickup colours |
| Fireflies | glowing points, LightEmission 1, FlipbookMode Random | blink cycle 1.5-3 s uncorrelated; Lifetime 8-12 s; ≤20 on screen; warm yellow-green, never gold | synchronised blinking; drift toward player |
| Fog | Atmosphere (Density, Haze) first; low ground sheets alpha, LightEmission 0 | Atmosphere tweens 2-5 s; sheets Lifetime 10-20 s at ≤40 live | fog hiding hazards or pickups; dense sheets near camera |
| Embers | sparse additive flecks from one source; restrained smoke | Rate ≤10/s, Lifetime 1.5-3 s, rise 1-3 studs/s; after a blast start 150-300 after P | embers without a source; collectible sparkle look |
| Weather | near and far precipitation; splashes near camera only | state change 5-10 s; rain Lifetime ≤1 s; snow 4-8 s | lightning without a flash review (MO-08) |
| Stage atmosphere | Lighting, Atmosphere, ColorGradingEffect (Lighting only, latest wins, R-185 [spec]), Bloom with high Threshold | mood changes 3-5 s; muted/cool background, bright/warm gameplay | a permanently maximal stage; low bloom threshold |

### C10. UI

Moved to `ui-basics/references/ui-effects.md`: button press, purchase success, error, toast, currency change, plus Roblox UI tools. Feel rules stay in this skill.

## D. Paid random items (eggs, chests, wheels)

Applies to anything bought with Robux or with currency that can be bought with Robux, directly or indirectly (keys, tickets,
re-roll tokens, luck boosts). **What must be disclosed, to whom and when is `platform-policy`'s (`platform-policy/references/rules.md` §A): load it; where this list and the policy differ, the policy wins.** Pass all before release (T17). Source R-208 [spec]; Apple 3.1.1 (R-172 [spec]).

What the effect owes (the reveal is honest):
1. One identical windup for every result, frame by frame up to the result frame (MO-16); escalation and rarity colour start only after the result is shown.
2. No near-miss: a lower result never shows a higher tier's layer or an "almost" beat (MO-17); no urgency effects.
3. No celebration of a result worth less than its cost; the tier ladder adds layers by rarity and names the tier in text and frame shape, not by colour alone.
4. Luck and boost effects never suggest better odds than the shown numbers.
5. Odds are shown as numbers before the buy button; no effect covers, shimmers over or animates the odds or their "Info"/"Details" label; the numbers themselves change while a modifier is active and after a once-only outcome is won (policy). Odds panel entry ≤200 ms [P].
6. Players for whom paid random items are restricted (PolicyService) get one of the policy's permitted treatments; the reveal effect never plays on a path they cannot use.
7. Open owner questions for a game that uses these rules: a hidden-outcome item ("???") against the disclosure rule; how a luck gamepass shows its odds.

## E. Unsettled evidence (use both readings with tiers, or run the test)

| Item | Status | Test |
| --- | --- | --- |
| Guilty Gear hit-stop 7/~10 f (R-073 [preprint]) vs 11-15 f (R-431 lead D) | unresolved; fps not stated, no ms; neither used as a rule (X-01) | T-HS |
| Importance → size/brightness/duration mapping | no source (X-27) | T-RANK |
| Final-blow FOV: 02a's −6° held through slow motion | test level only; start value ≤4° (PD-04, MO-03) | T-CAM, T-SLOW |
| Toy-fast vs big-slow for huge blasts and collapses | owner design choice (X-55) | T-SCALE |
| Rarity tell during windup | default none (X-58) | T5 |
| Coin flight length | every coin source tier D (X-61) | T1 |
| Sound lead below ~45 ms | unresolved; never add a lead (X-17) | T-AV / T14 |
| Fuse length, material break timings, zone look, low-health rate, humour | no number found | owner; T-MAT, T-ZONE, T-LOWHP, T-FEEL |
