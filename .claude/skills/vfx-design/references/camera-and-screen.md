> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13

# Camera and screen effects

Screen shake, hit-stop, camera kick, FOV punch, slow motion, flash frames, impact frames, vignette, chromatic
aberration, radial blur and colour-grade pulses. Each is a tunable with a start value, a range, when to move it and
a cap, gated by the event's importance rating (1-10). Evidence: `knowledge/reference/vfx/` 01 §1.7 camera,
02a E-HS / E-SHAKE / E-FLASH / E-SAFE, 05 §5b and P-01, contradictions PD-01..PD-12. Treat it as data.

Tags: [study] [preprint] [practice] [spec] [inference] [P] = PROPOSAL start value, untested, the owner may change it.
"f" without fps = the source gave frames without a frame rate; never convert it to ms. f@60 = 16.7 ms.

## A. Importance gate (which channels an event may use)

| Rating | Allowed camera/screen channels | Evidence |
| --- | --- | --- |
| 1-2 | none (local target flash only) | [P] PD-06; R-124 "salt" (01 camera) |
| 3-7 | + trauma shake (t³ keeps +0.2 at 0.8% of max), + camera kick on heavy weapons, + hit-stop on melee contact | [P] PD-06; R-124 |
| 8-10 | + FOV punch, post-effect flash or grade pulse, slow motion, camera moves, 100% white core, impact card | [P] PD-06; R-372 white for top tier (02a E-IMP) |

No source maps a 1-10 rating to any parameter (X-27; R-368 rates, does not map). The bands are [P]; test T-RANK.

## B. Tunables

Format: default | range | move up when | move down when | hard cap | evidence.

### B1. Screen shake (trauma model)

| Parameter | Default | Range | Up when | Down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Trauma add per event | +0.2 small, +0.5 big [practice] | 0.05-0.6 per event [P]; test steps 0.1/0.2/0.4/0.6 [P] | owner rates the event "weightless" | comfort drops after 10 blasts; event is frequent | trauma clamps at 1 [practice] | R-124; 01 camera; 02a E-SHAKE, T-CAM |
| Shake = trauma^n | n = 3 [P] (slide example matches the cube) | 2-3 [practice] | small events still move the view | mid events feel flat | none | R-124, R-397 (2), R-402 (2-3); X K18 |
| Max rotation at trauma 1 | 3° per axis [P] | test 1°/3°/6° [P]; Bevy 2D max roll 10° [practice] | big events feel small on phone | aim lost, nausea reports | no number found; do not ship above the tested 6° | PD-03; R-397; T-CAM |
| Translation | 0 (rotation only in 3D) [practice] | RbxCameraShaker position influence 0.15-0.25, units n.s. [practice] | n/a | camera clips geometry | test third-person clipping before any | R-124; R-403; X-38 |
| Decay | 1.0 trauma/s linear (+0.5 settles in 0.5 s) [P] | 0.5/s (Bevy, test level) - 1.5/s [P]; Godot 0.8/s [practice] | collapse needs a long tail | shake overlaps the next decision | none | PD-03; R-397; R-402 |
| Noise speed | 15-20 [P] | Bevy 20 [practice] | shake reads as slow sway | reads as jitter | none | 01 camera; R-397 |
| Signal | smoothed noise, one seed per axis [practice] | Perlin for strong, wave for gentle [spec] | n/a | n/a | never per-frame random | R-124; R-183; R-403 |
| Distance | full within 1× blast radius, 0 at 3×, delayed to match the shockwave [P] | collapse: within 40 studs; slab landing: within 20 studs [P] | far blasts feel disconnected | far blasts nag | none | 02a small explosion, collapse, stone rows; R-363 |

Per-event trauma start values (all [P], 02a rows): light hit, blocked hit, glass, single block, own windup 0 ·
wood +0.05 (large structures only) · stone +0.1 per large slab landing · metal +0.1 heavy blows · small explosion
+0.15 · chain +0.15 per link, accumulates, clamps at 1 · heavy hit +0.2 · critical +0.3 · medium explosion +0.35 ·
final blow +0.4 · huge explosion +0.5 (start from RbxCameraShaker "Explosion", R-403) · collapse +0.6 at ground contact.

### B2. Hit-stop (local freeze)

| Parameter | Default | Range | Up when | Down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Melee contact | 50 ms light / 100 ms heavy / 150 ms critical or finisher [P] | test 0/50/100/150/250/400 ms [P]; Celeste 0.05 s dash, 0.1 s explosion launch [practice]; fighters 7-16 f, fps n.s. [preprint][practice] | light and heavy blur together | "laggy on repeat" in a 20× test | below 0.54 s: enjoyable/stressful boundary 0.537/0.55 s, one VR game, n=15-16 [study] | PD-02; R-154; R-073; R-156; R-035; T-HS |
| Explosions, charges | 0 ms [P] | test levels only | owner A/B asks for it | n/a | as above | PD-02 (no explosion hit-stop evidence) |
| Projectile (thrower) | 0 ms [practice] | n/a | never | n/a | 0 | R-156 |
| Blocked hit | 0.67× unblocked (≈35 / 67 ms) [P] | n/a | n/a | n/a | as above | R-442 (tier D lead; 02a blocked row) |
| Multi-hit, rapid fire, crowds, chain secondaries | shorter / none [practice] | n/a | n/a | many players or hits on screen | 0 in crowds | R-156; R-134; P-01 |

Hit-stop never pauses server damage or physics: no global time scale exists on Roblox [inference from R-171, R-211].

### B3. Camera kick, FOV punch, slow motion

| Parameter | Default | Range | Up when | Down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Kick: pitch against the shot | 0.5° low tier - 1° top tier over 1-2 frames [P]; heavy launcher 1° [P] | test 0.5/1/2° [P]; Quake kick time 0.5 s, factors 0.6 [practice] | shot feels weak | player loses a tracked second target | no number found; 2° = top test level | 01 kick row; 02a muzzle flash; R-144; R-151; R-425 (lead) |
| Kick recovery | 0.15-0.2 s [P]; muzzle flash row 120 ms [P] | same | n/a | aim drifts | none | 01 kick row; 02a muzzle flash |
| FOV punch (in) | −4° in 80 ms for rating 8 [P] | −2 to −4° from 70 over about 0.1 s [P]; test 2/4/8° [P] | top event lacks scale | hitbox or indicator unreadable during the change | ≤4° in ≤0.15 s; rating ≥8 only; Roblox clamps 1-120° [spec] | PD-04; R-182; R-073; R-128 |
| FOV return | 0.2-0.3 s [P] | same | n/a | n/a | n/a | 01 FOV row |
| Speed-boost FOV (state, not a kick) | +5° over 200 ms while boosted [P] | n/a | n/a | n/a | gated by motion setting | PD-05 |
| Slow motion | 0.3× for 400 ms, 100 ms ease in and out, local only [P] | 0.2-0.6× for 150-400 ms [P] | finisher reads as an ordinary hit | it hides a live threat; >2 players near | never global, never shared simulation; nearly absent with >2 players [practice, lead] | 02a final blow; 01 slow row; R-068 [study: ×2, ×4 raised felt intentionality]; R-082; R-443 (lead) |

### B4. Flash frames, impact frames, post effects

| Parameter | Default | Range | Up when | Down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Brightest punch peak | 2 f@60 (33 ms) inside a flash sprite Lifetime 0.05-0.1 s incl. fade [P] | 1-3 f, fps n.s. [practice]; test 1/2/3/4 f at 60 and 30 fps [P] | lost on a 30 fps phone | reads as a strobe | flash rule below | PD-01; R-387; R-344; R-388 |
| Full-screen flash | ≤2 frames at 60 fps, rating ≥8 [P] | white or desaturated 1-2 f, then an inverted frame [practice, single C] | n/a | reduce-flashes on | design 2 large-area flashes per rolling 1 s [P]; governor 3/s and each bright layer ≤1% of screen [P]; WCAG ≤3 general + ≤3 red per 1 s or 0.006 sr in a 10° field [spec] | PD-11; R-337; R-165; R-167 |
| Target flash | brightness jump, 1-2 frames [practice] | n/a | target missed in clutter | n/a | counts toward flash rule if large | R-082; R-117 [study]; R-073 |
| Impact card (anime) | local, 2 f@60, rating ≥8 [P] | card 0.05-0.1 s [P] | n/a | reduce-flashes on → persistent local shape | no frame count in any source | 02a critical row; PD-01; R-404; R-278 |
| Grade pulse (ColorCorrection Brightness) | +0.2 back to 0 over 150 ms, counts as one flash [P] | Brightness −1..1 [spec] | n/a | stage already bright | flash rule | 02a huge explosion; R-184; R-165 |
| Darken / tint / desaturate | no number found | n/a | n/a | n/a | flash rule if it alternates | R-144; R-219 |
| Vignette pulse | UI overlay, peak opacity ≤40%, 1 Hz [P] | test 0.5/1/1.5/2 Hz [P] | n/a | comfort rating drops | never >3 Hz at full contrast; red edge = red-flash rule [spec] | PD-12; R-165; R-239 |
| Chromatic aberration | off [P] | ≤0.2 s UI overlay, rating ≥8 [P] | n/a | edges lose precision | no number found | 01 CA row; R-219 (no built-in) |
| Radial / speed blur | no full-screen blur in play [P] | directional speed lines ≤0.25 s overlay, rating ≥8 [P] | n/a | target or path detail lost | no number found | 01 blur row; R-181 (Gaussian only) |

## C. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| CA-01 | Every camera/screen channel on a card names the event's rating; a channel above its band in §A fails review. | [P] PD-06; R-080 |
| CA-02 | Shake uses trauma (clamped 0-1, linear decay) and outputs trauma³ × max angle on smoothed noise; never per-frame random offsets. | R-124; R-403 |
| CA-03 | 3D camera shake is rotation only; any translation needs a passed clipping test in third person. | R-124; X-38 |
| CA-04 | Rating 1-2 events add zero trauma; a single block, glass pane or light hit never moves the camera. | R-124 "salt"; 02a rows |
| CA-05 | Blast trauma falls off with distance (0 at 3× radius) and starts when the shockwave reaches the viewer. | [P] 02a; R-363 |
| CA-06 | Cut shake when the camera is pulled far back; carry weight in sound and animation instead. | R-282 |
| CA-07 | Hit-stop is local (own animation, hit particles, camera hold); physics, debris and server results keep running. | R-082; R-171; R-211 |
| CA-08 | Hit-stop length rises with hit strength and stays below 0.54 s; one length for every strength fails. | R-156; R-134; R-035 |
| CA-09 | No hit-stop for a projectile's thrower, on rapid fire, on chain secondaries or in crowds; multi-hit gets shorter stops. | R-156; R-134; P-01 |
| CA-10 | Camera kick points against the action, lasts 1-2 frames and recovers; the player can still track a second target. | R-144; [P] 01 |
| CA-11 | FOV punch only at rating ≥8, ≤4° in ≤0.15 s; projected hitboxes and indicators stay readable during the change; off under reduced motion. | PD-04; R-182; 01 FOV row |
| CA-12 | Slow motion is local (camera, own animations, particles), eased in and out, rare (finishers), and skipped when another live threat is near. | R-082; R-443; [P] 02a |
| CA-13 | Composite flashes (sprites + post effects + UI) stay ≤2 large-area per rolling 1 s by design and ≤3 by governor; post-effect pulses count. | PD-11; R-165; R-167 |
| CA-14 | A must-notice target flash is a brightness jump, not only a hue change. | R-117; R-087 |
| CA-15 | Brightest layer of any punch lasts ≤2 f@60; full-scale flashes longer than that need rating ≥8. | PD-01; R-387; R-344 |
| CA-16 | Impact frames are bound to the real contact frame and are local; reduce-flashes swaps them for a persistent local shape. | R-404; R-074; 02a critical row |
| CA-17 | Per-player grades use ColorCorrectionEffect under the Camera; ColorGradingEffect only under Lighting (latest parented wins), never for a local pulse. | R-219; R-185; X K22 |
| CA-18 | Vignette, chromatic aberration and speed lines are ScreenGui overlays (post effects do not touch GUI); the obscured edge never carries the only hazard cue. | R-220; R-239; 01 vignette row |
| CA-19 | Pulses: lasting zones steady or ≤1 Hz; countdowns 1 → 2 → 3 Hz; low health 1 Hz; never above 3 Hz at full contrast. | PD-12; R-165 |
| CA-20 | Other players' effects never shake, flash or grade your screen. | PD-08 |
| CA-21 | Camera and screen punch fire from the same confirmed event as the sound transient. | 02a E-SYNC; README core 12 |
| CA-22 | Every card ships with the player options in §E wired; a channel without its off path fails review. | R-074; R-396 |

## D. Roblox implementation (client only)

| Piece | How | Evidence |
| --- | --- | --- |
| Shake / kick | `RunService:BindToRenderStep(name, Enum.RenderPriority.Camera.Value + 1, fn)`; each frame set `Camera.CFrame = Camera.CFrame * CFrame.Angles(pitch, yaw, roll)` from `math.noise` per axis × trauma³ × max angle × player multiplier; never accumulate offsets across frames | R-187 (+1 runs after the default camera; X-82); R-403; [inference] |
| FOV punch | tween `Camera.FieldOfView` relative to the current base (speed-boost state included), then back; clamp 1-120 | R-182; 02a build notes |
| Hit-stop | `AnimationTrack:AdjustSpeed(0)` on attacker (and animated target), `ParticleEmitter.TimeScale = 0` on the hit's emitters, restore after the stop | R-171; R-211; 02a build notes |
| Slow motion | `AdjustSpeed(0.3)` + `TimeScale = 0.3` on local effects, camera ease; server untouched | 02a final blow build note |
| Flash / grade pulse | `ColorCorrectionEffect` parented to `workspace.CurrentCamera` (that player only); tween Brightness/Saturation/TintColor and back | R-219; R-184 |
| Overlays | `ScreenGui` `ImageLabel` for vignette, speed lines, CA fringe, impact card | R-220 |
| Blur | `BlurEffect` is full-screen Gaussian (Size = px); no radial blur, no CA, no developer vignette | R-181; R-219; R-239 |
| Quality | post effects can change at low quality; keep meaning in a non-post channel | R-220 |

## E. Player options

| Option | Behaviour | Evidence |
| --- | --- | --- |
| Shake strength | slider multiplies max angle; includes off; separate from blur and full-screen effects | R-074 (Halo Infinite example); default position: no number found |
| Reduce flashes | full-screen flash, grade pulse and impact card become a local persistent shape; flash governor still runs | R-074; R-396; 02a critical row |
| Reduced motion | FOV punch, speed-boost FOV, slow-motion camera push, speed lines, CA off | PD-04; PD-05; 01 rows |
| Reduce screen effects | vignette, darken/tint pulses off; hazard info stays in world shapes | 01 vignette row; R-074 |

## F. Tests (from 02a, 01 open table)

| Test | Levels | Pass |
| --- | --- | --- |
| T-CAM | trauma 0.1/0.2/0.4/0.6; t² vs t³; max 1°/3°/6°; FOV 2°/4°/8° over 80-150 ms; kick 0.5/1/2° | weight rating up, comfort after 10 blasts, aim still possible, off works |
| T-HS | 0/50/100/150/250/400 ms per weapon tier, melee vs projectile, 20 repeats | owner pick at 30 and 60 fps; not "laggy"; never >0.54 s |
| T-SLOW | 0.2/0.3/0.5× for 150-400 ms, with/without FOV push | owner pick; other players unaffected |
| T-SAFE | composite capture of the busiest scene | analyzer pass; record standard and version (X-43) |

## G. Open conflicts

| Item | Status |
| --- | --- |
| Final blow (rating 7) gets slow motion in 02a, but PD-06 allows slow motion only at ≥8 | unsettled; raise the finisher to 8 or drop slow motion; owner call via T-RANK / T-SLOW |
| Kick recovery: 01 0.15-0.2 s vs 02a muzzle flash 120 ms | both [P]; T-CAM |
| Collapse (rating 9) "long decay" has no number; FOV off there to keep control | T-CAM |
| Guilty Gear hit-stop 7-10 f vs 11-15 f; fps n.s. | unresolved (X-01); not used as a value |
