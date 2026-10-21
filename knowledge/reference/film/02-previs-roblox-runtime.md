---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J015-T02, Film_Director_Research_2026.txt lines 509-707 + register B, R"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Film paper part 2: storyboards, animatics, Blender previs (section 11) and Roblox runtime cameras, cues, delivery, proposed terminal contract (section 12) (lines 509-707)

Paraphrased notes. The paper (FP) stays outside git. Every row cites `FP:<line>`. **Extraction only: nothing here is fact-checked and no web access was used.** The claims are the paper's. Section 11 lists them for the fact-check pass. The paper's research cutoff is 2026-10-21 and many of its Roblox and Blender sources are undated living pages read that day, so check them live. The paper itself says (FP:511) that no Blender scene, camera converter, animatic or Roblox runtime was run for it, and that its numeric examples are maths illustrations, not recommended durations or measured film settings. Its OPINION rows are proposals, never Roblox or Blender rules.

## 0. How to read

| Key | Meaning |
| --- | --- |
| FP:n | Line n of `Film_Director_Research_2026.txt`. One paragraph = one line. Register entries (A09, A10, B01-B17, R01-R29) are at FP:1409-1427 and FP:1529-1931; they are cited by their first line in section 10. |
| Tag | The paper's own mark, copied unchanged: VERIFIED, EXPERIENCE (not used in this range), OPINION. "none" = framing text the paper does not tag. A VERIFIED paragraph that ends in the paper's own advice or inference gets two rows: the fact keeps VERIFIED, the advice row keeps the paragraph's VERIFIED mark and is labelled PROC or INFER in Kind (see X-03). |
| Kind (my label) | DOC = documented behavior, name, value or date. MATH = derived maths or arithmetic. PROC = the paper's proposed procedure. INFER = the paper's own inference. LIMIT = a caveat the paper states. FRAME = framing. The paper uses only Tag. |
| Src | The paper's source id, resolved in section 10. "acc" = accessed 2026-10-21; "live-read" = undated living page read that day. POST = dated after 2026-06-01. |
| Row IDs | SB storyboard / Disney, BL Blender, IG ChatGPT Images, RT Roblox runtime, TC terminal contract, CP review capture, EG evidence gap, N number, FC claim to check, X limit or contradiction. |
| Names | Every API, property, enum, method and Blender command is written exactly as the paper spells it, in backticks. Docs mirror root: `knowledge/external/roblox-creator-docs/` (API yaml under `_api-reference/classes/` and `_api-reference/enums/`). |
| Rule of use | Never write "Roblox requires X" or "Blender requires X" from a PROC, INFER or OPINION row. |

## 1. Storyboards and layout (section 11 opening, FP:509-525)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| SB-01 | 511 | FRAME | The section specifies a proposed pipeline. Nothing was executed. Numbers are mathematical illustrations, not recommended durations or measured settings. | OPINION | none |
| SB-02 | 513 | DOC | Disney describes layout as receiving storyboards edited into a movie, making their first 3D cinematic form, with rough character animation and temporary lights/effects. The shot returns after character animation for camera, framing and focus polish and continuity approval. | VERIFIED | A09, undated, acc |
| SB-03 | 515 | DOC | Disney's story process names character emotion, expression, timing, staging and framing. Thumbnails are refined step by step, not treated as finished illustrations at the start. | VERIFIED | A10, undated, acc |
| SB-04 | 517 | PROC | Ask for storyboard images as communication panels, not individually spectacular concept art. Supply consistent character references, shot size, viewpoint, screen direction, action, eyeline target, and the relation to the previous and next panel. Add a separate overhead blocking plan when spatial logic matters. | OPINION | 2026-10-21 |
| SB-05 | 517 | PROC | In Blender previs, replace appealing images with testable cameras, proxy geometry, actor paths and an edited sequence. | OPINION | 2026-10-21 |
| SB-06 | 517 | LIMIT | A generated image cannot prove that its implied 3D camera path is collision-free or that adjacent panels share a coherent space. | OPINION | 2026-10-21 |
| SB-07 | 517 | PROC | Ownership: the director owns revisions to the shot's intention; the animator owns performance execution within that intention; the owner approves creative changes. | OPINION | 2026-10-21 |
| SB-08 | 521-525 | DOC | Table: review edited boards before expensive final imagery (no mandatory panel count); rough layout evaluates cameras and performances together (no mandated lens mm); recheck camera and continuity after animation (no mandatory pass count). All marked VERIFIED, A09/A10. | VERIFIED | A09-A10, undated, acc |

## 2. Blender previs: pinned tool and camera specification (FP:529-549)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| BL-01 | 531 | DOC | The official Blender release listing names `5.2.2 LTS`, updated 2026-09-15, as the current 5.2 stable release. | VERIFIED | B01, 2026-09-15, POST |
| BL-02 | 531 | PROC | Put that version designation in the reproducibility manifest. Do not silently substitute a development build. | VERIFIED (paragraph mark; advice) | B01 |
| BL-03 | 533 | DOC | In the 5.2 manual the animated viewport output command is `View > Render Playblast`; still output is `Render Viewport Preview`. Older tutorials can use a different command name. | VERIFIED | B02, undated 5.2 manual, live-read |
| BL-04 | 535 | PROC | Record next to each review movie: Blender version, scene revision, output dimensions, pixel aspect, scene rate and base, output frame range, color-management settings, camera IDs, audio revision, export-converter version. Treat a change to framing, timing or color transform as a new comparison, not an invisible replacement. | OPINION | none |
| BL-05 | 539 | DOC | Blender supports perspective and orthographic camera projection. Focal length changes the perspective view angle. In orthographic projection apparent object scale does not shrink with distance. | VERIFIED | B04 (projection), undated 5.2, live-read |
| BL-06 | 539 | DOC | `Sensor Fit` decides which sensor dimension governs the view: `Horizontal` derives height from the output aspect, `Vertical` derives width, `Auto` adapts to the output dimensions. | VERIFIED | B03 (sensor fit), undated 5.2, live-read |
| BL-07 | 541 | MATH | Scope: centered, rectilinear pinhole camera, no lens shift, distortion or anamorphic squeeze. With effective gate width Sx and height Sy in mm and focal length f > 0 mm: horizontal angle H = 2 atan(Sx/(2f)); vertical angle V = 2 atan(Sy/(2f)). `atan` gives radians; multiply by 180/pi for degrees. Sx, Sy > 0 and each angle lies strictly between 0 and pi radians. The ratio inside atan is dimensionless. | VERIFIED, geometric derivation | B05, undated, acc |
| BL-08 | 541 | LIMIT | This is the ideal projection model, not a complete real lens. Edmund Optics supplies the angular-field geometry and warns that real distortion and working-distance effects limit first-order approximations. | VERIFIED, geometric derivation | B05 |
| BL-09 | 543 | MATH | Same centered projection, displayed aspect a > 0: tan(H/2) = a tan(V/2), so V = 2 atan(tan(H/2)/a). Here a = displayed width / displayed height after pixel-aspect interpretation and any intended crop, not automatically the file's width/height. The paper says this follows by dividing the two pinhole equations; Blender separately exposes output and pixel-aspect settings. | VERIFIED, geometric derivation | B05; B06, undated 5.2 (latest URL, mutable) |
| BL-10 | 545 | MATH | Camera-space projection: x_image = f X/Z and y_image = f Y/Z. At a fixed viewpoint, changing f scales the image and does not change relative depth geometry. Moving the camera changes X/Z and Y/Z differently for objects at different depths. So matching a close subject's size by moving back and raising focal length does not keep the same perspective. The paper calls this mathematical inference, not a psychological finding. | VERIFIED, geometric derivation | B05 (ideal model) |
| BL-11 | 547 | PROC | Each shot handoff supplies: projection type, camera pose, target/interest point, focal length if used, effective gate, sensor fit, output and pixel aspect, shift/crop, derived vertical and horizontal angles, focus settings, timing. A bare "40 mm" is not enough to reproduce a shot in Roblox. Do not invent a sensor gate to manufacture an engine FOV. | OPINION | none |
| BL-12 | 547 | PROC | Do not label a focal length intrinsically heroic, intimate or frightening; story, distance, framing, performance and context need study. | OPINION | none |
| BL-13 | 549 | PROC | Use perspective for the cinematic master. Keep orthographic previs for a deliberate graphic design or layout inspection. Do not call a distant long-lens perspective shot mathematically identical to orthographic. | OPINION | none |
| BL-14 | 549 | PROC | Check final framing in the actual engine viewport, including the narrowest intended display. A Blender preview does not establish mobile readability. | OPINION | none |

## 3. Blender previs: camera moves, evaluated transforms, cuts, time (FP:551-587)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| BL-15 | 553 | DOC | `Track To` points a chosen local axis at a target and controls roll with an `Up` axis. The 5.2 docs warn of unstable roll when the owner is nearly directly above the target and suggest `Damped Track` then. Track and Up axes must differ. | VERIFIED | B07, undated 5.2 (latest URL), live-read |
| BL-16 | 555 | PROC | Block a move with separately named camera-path and interest-point controls. Review roll and screen direction across the whole move, not only the ends. A look-at constraint is a convenience, not an artistic choice of whom to watch. Animate the target on purpose when attention shifts. Avoid a target crossing the camera position or an ambiguous up direction. | OPINION | none |
| BL-17 | 557 | DOC | F-curves represent single animated property channels. Linear interpolation does not ensure continuity of speed across keys. Bézier handles shape interpolation; `Auto Clamped` handles prevent unwanted overshoot between keys; continuous-acceleration handling can propagate changes farther along a curve. | VERIFIED | B08, undated 5.2, live-read |
| BL-18 | 559 | MATH | For a path p(t) world speed is ||dp/dt||, not the slope of one position channel. Straight segment of length L over T > 0 seconds: average speed L/T. | VERIFIED, mathematical derivation | none |
| BL-19 | 559 | MATH | Deliberate smoothstep progress s(u) = 3u² - 2u³, u = t/T in [0,1]. Instantaneous speed along that straight segment is (L/T)(6u - 6u²), maximum 3L/(2T) at u = 1/2, zero endpoint velocity. Endpoint acceleration is nonzero. | VERIFIED, mathematical derivation | none |
| BL-20 | 559 | LIMIT | Smoothstep is an illustrative authored easing, not Blender's universal default, not a film measurement, not evidence that the speed feels good. A curved route or independently animated aim needs separate inspection. | VERIFIED, mathematical derivation | none |
| BL-21 | 561 | PROC | Record planned duration and measured peak translation and rotation speed after the path is authored. Do not set a universal degrees-per-second camera limit from this derivation. Compare the beat with actual motion and phone readability. A smooth curve can still give distracting screen acceleration or occlusion. | OPINION | none |
| BL-22 | 563 | DOC | Blender's evaluated dependency graph (`Depsgraph`) is needed to read state with animation and constraints applied. | VERIFIED | B09, undated 5.2 API, acc |
| BL-23 | 565 | PROC | Export evaluated camera poses at explicit timestamps, or a documented analytic form plus its interpolation. Do not export only raw keyframe location when parenting or constraints shape the visible result. Include unit conversion, basis conversion, origin, handedness declaration and quaternion/matrix convention. | OPINION | none |
| BL-24 | 565 | MATH | For a rigid transform with verified basis conversion Q: orientation R_target = Q R_source Q^-1; position also needs the agreed scale and origin offset. The paper calls this coordinate-change algebra, not a verified Roblox camera-import feature. No specific axis map is asserted: establish Q with an axis-and-landmark test. | OPINION | none |
| BL-25 | 565 | PROC | After conversion test camera facing, roll, scale and landmark screen coordinates. A mesh import that completes does not prove camera timing, projection or effects transferred. | OPINION | none |
| BL-26 | 569 | DOC | Camera-bound timeline markers switch the active camera at their marker frames. Markers sit on whole frames, not fractional positions. | VERIFIED | B10, undated 5.2 (staging mirror), live-read |
| BL-27 | 571 | PROC | Use camera markers for hard cuts inside one scene; use the Video Sequencer to assemble reviewed shot outputs and audio. Name each cut by a stable shot ID, not only a temporary camera object label. Keep a shot edit-decision list outside generated board artwork. | OPINION | none |
| BL-28 | 573 | DOC | Blender exposes `fps` and `fps_base`; the effective scene rate is fps/fps_base. The output format uses frames per second. | VERIFIED | B11, B06, undated 5.2, acc |
| BL-29 | 573 | DOC | Movie-strip import can set the scene rate from encoded media. Strip documentation warns that a source/scene rate mismatch gives wrong perceived speed unless compensated. | VERIFIED | B12, B13, undated 5.2, live-read |
| BL-30 | 575 | MATH | Elapsed time versus rendered samples. With start frame k0 and rate r, frame position k occurs at t = (k-k0)/r. | VERIFIED, arithmetic | B06/B11 (rate meaning); arithmetic derived |
| BL-31 | 575 | MATH | Example at exactly 30 fps: positions 1 and 31 are 30 intervals apart, which is 1 second. Rendering inclusive frames 1 through 31 gives 31 samples; at 1/30 second each the clip lasts 31/30 seconds. | VERIFIED, arithmetic | B06/B11 |
| BL-32 | 575 | MATH | A cut list using `[start, next-start)` intervals avoids this off-by-one ambiguity. At 30 fps one interval is exactly 100/3 ms; at 60 fps exactly 50/3 ms. Neither is exactly 33 ms or 16 ms. | VERIFIED, arithmetic | B06/B11 |
| BL-33 | 577 | PROC | For a study of a published scene, log: exact edition/URL, original or accessible file, source rate as a rational where known, presentation timestamps, first included and first excluded frame of each shot, retiming, and any uncertainty. | OPINION | none |
| BL-34 | 577 | PROC | For variable-frame-rate material, measure presentation timestamps, not frame count over an assumed constant rate. Do not infer native film fps from a streaming player's display rate. A 30000/1001 source keeps that fraction; do not silently call it 30 or exactly 29.97. With only a rounded web-player timestamp, give approximate seconds with their precision and make no frame-accurate claim. | OPINION | none |
| BL-35 | 579 | PROC | When source and edit rates differ, decide explicitly between preserving duration with frame resampling and preserving every source frame with changed playback speed. Document it; an import preference must not decide the meaning silently. Temporary sound must stay aligned to the intended event after retiming. | OPINION | none |

## 4. Blender review artifacts and ChatGPT image boards (FP:581-605)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| BL-36 | 583 | DOC | Blender can write animation frames as individual image files; the Video Sequencer can combine them with an audio track into a movie. | VERIFIED | B14, undated 5.2 (staging mirror), live-read |
| BL-37 | 585 | PROC | Use three review artifacts, not one impressive render: (1) simple boards for intent and screen direction, (2) timed graybox/playblast for staging, cuts, occlusion and movement, (3) selected lighting/material frames for contrast and atmosphere. Keep an image sequence when resumability and frame audit matter; encode the review movie separately. Quote no fixed render time without hardware, scene complexity, quality settings and a measurement. | OPINION | none |
| BL-38 | 587 | PROC | Compare A/B edits with the same output rate, crop, display size and audio revision. Change one directing decision at a time (reveal order, cut point, camera distance, motion vs stillness, sound entrance). Review silent for visual comprehension and with sound for sync and emotion. Then repeat in Roblox on target displays; Blender beauty cannot validate engine timing or performance. | OPINION | none |
| IG-01 | 591 | DOC | OpenAI announced "ChatGPT Images 2.5" on 2026-09-08 and describes better reference preservation and multi-turn editing. These are vendor capability claims, not a guarantee of correct sequence geometry or continuity. | VERIFIED | B15, 2026-09-08, POST |
| IG-02 | 593 | DOC | The current official image-generation documentation still lists recurring-character consistency and precise composition as limitations. | VERIFIED | B16, undated live doc, live-read |
| IG-03 | 593 | DOC | Official ChatGPT guidance: identify uploaded references by order, explain their roles, then make focused revisions. | VERIFIED | B17, 2026-04-10 |
| IG-04 | 595 | PROC | Get approved character, environment and prop references from the art pipeline first. Generate or edit one clearly identified panel at a time when continuity matters; assemble and label outside the image model. Give a simple overhead blocking map and the previous approved panel, and treat each output as a proposal. Reuse accepted reference files, not descriptive text alone. | OPINION | none |
| IG-05 | 595 | PROC | Check identity, handedness, prop hand, entrance/exit direction, eyelines, positions, light direction and focal subject. | OPINION | none |
| IG-06 | 595 | LIMIT | Generated panels are not measured lenses, calibrated camera poses, orthographic models or automatically correct 180-degree continuity. | OPINION | none |

## 5. Roblox runtime: camera, time, cues, audio, VFX (section 12, FP:609-643)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| RT-01 | 611 | DOC | Each client owns a local `Workspace.CurrentCamera`. Setting `CameraType` to `Scriptable` stops default camera behavior from controlling the view; `CFrame` supplies position and orientation. | VERIFIED | R01, R02, undated live, acc |
| RT-02 | 611 | DOC | `Camera.Focus` also needs deliberate updating during `Scriptable` operation, because visual-detail work depends on proximity to the focus point. | VERIFIED | R01, R02 |
| RT-03 | 611 | LIMIT | `Focus` is not an instruction to load a distant set, and not a substitute for `DepthOfFieldEffect.FocusDistance`. | VERIFIED | R01, R02 |
| RT-04 | 613 | DOC | The server holds authoritative game state; client requests that affect progression or other players need server validation. | VERIFIED | R24, R25, undated live, acc |
| RT-05 | 613 | INFER | So a local cinematic finishing is not enough evidence that a reward, boss defeat, teleport, quest transition or trade should happen. | VERIFIED (paragraph mark; inference) | R24, R25 |
| RT-06 | 615 | PROC | Architecture: one presentation controller has exclusive camera ownership through a scene token. The server authorizes scene identity, participant membership and gameplay consequences. Each client runs its own camera, subtitles and cosmetic cues. | OPINION, proposed architecture | grounded in R01/R24/R25 |
| RT-07 | 615 | PROC | A scene definition holds: shot transforms or paths, FOV mode, duration data, marker IDs, asset dependencies, input policy, audio mix ownership, streaming requirements, terminal pose, approved fallback. | OPINION | same |
| RT-08 | 615 | PROC | A shared spectacle needs its own stated late-join and skip policy. A private story scene must not change other players' cameras or shared world state by accident. | OPINION | same |
| RT-09 | 619 | DOC | The `Camera` API defines `FieldOfView` as a vertical angle, clamped to 1-120 degrees, default 70. These are API range and default, not recommended lenses. | VERIFIED | R02, R03, undated live, acc |
| RT-10 | 619 | DOC | `FieldOfViewMode` decides which angle stays invariant when the viewport changes: `Vertical`, `Diagonal` or `MaxAxis`. Horizontal and vertical framing are linked by aspect ratio. | VERIFIED | R03 |
| RT-11 | 619 | LIMIT | The API's `FieldOfView` wording is more precise than the camera overview's shorthand about direction via `FieldOfViewMode`. Do not read the overview as saying a single `FieldOfView` number always means horizontal FOV. | VERIFIED (paragraph mark; reading advice) | R02, R03 (overview = R01 page, see X-05) |
| RT-12 | 621 | PROC | Store the angle convention in every exported shot, not just a number labelled "lens". A Blender focal length alone is insufficient without sensor, fit and aspect assumptions. | OPINION, framing contract | grounded in R02/R03 |
| RT-13 | 621 | PROC | Review framing at the supported viewport shapes; keep the dramatic subject, gaze target and interaction destination, not only a central crop. Letterbox masks do not create a new camera projection. If masks hide the action, reframe or calculate the intended visible aperture; film bars do not repair composition. | OPINION | grounded in R02/R03 |
| RT-14 | 623 | DOC | `BindToRenderStep` gives explicit update ordering and removal by binding name. Lower priorities run first; equal priorities run in unspecified/random order; rendering waits for these callbacks. | VERIFIED | R04, R05, undated live, acc |
| RT-15 | 623 | DOC | The scheduler page names camera movement as appropriate render-step work, and cautions against unnecessary render-step bindings. | VERIFIED | R05 |
| RT-16 | 625 | PROC | One lightweight timeline evaluation writes the final camera `CFrame`, `Focus` and FOV. Precompute spline or asset work elsewhere. Cancel obsolete tweens and remove the cinematic binding before restoring the gameplay camera. Never leave two scripts racing to assign `CFrame`. | OPINION, runtime method | grounded in R04/R05 |
| RT-17 | 625 | PROC | Camera interpolation is a directing choice: keep intended cuts discontinuous, do not smooth every transition. | OPINION | grounded in R04/R05 |
| RT-18 | 629 | DOC | Animation markers are authored on the clip timeline and observed through `AnimationTrack:GetMarkerReachedSignal()`, optionally with a string parameter. | VERIFIED | R06, R07, undated live, acc |
| RT-19 | 629 | DOC | Animation Graph events propagate through the graph with weights. Zero-weight events are silenced; blend/selection nodes can suppress events from non-primary inputs. | VERIFIED | R07 |
| RT-20 | 629 | INFER | A marker in a source clip is no proof its callback survives every graph blend. | VERIFIED (paragraph mark; inference) | R06, R07 |
| RT-21 | 631 | DOC | Animation Graphs were announced as fully released for live games in July. | VERIFIED | R08, 2026-07-15, POST |
| RT-22 | 631 | DOC | The later State Machine and Expression nodes were announced as a separate Studio beta in October. The paper says its FAQ states they work only in Studio, not in live games, during the beta. | VERIFIED | R09, 2026-10-08, POST |
| RT-23 | 631 | PROC | Do not equate base graph playback with unrestricted availability of every newer node. Check the current deployment path before choosing the beta nodes for a shipping cinematic. | VERIFIED (paragraph mark; advice) | R08, R09 |
| RT-24 | 633 | PROC | Animation markers for pose-linked details (foot contact, hand on a switch, cloth release, impact accent). Scene timeline for editorial cuts, subtitle intervals and music structure. | OPINION, cue design | grounded in R06/R07 |
| RT-25 | 633 | PROC | Cues get stable IDs and an explicit policy for pause, seek, skip and replay: a seek must not blindly replay every missed explosion or award every skipped story outcome. Test cues at blend boundaries. | OPINION | same |
| RT-26 | 635 | DOC | `Workspace:GetServerTimeNow()` returns a smoothed client approximation of server Unix time, meant to give clients roughly consistent timestamps. Documented rate tolerance: within 0.6% of local clock rate. | VERIFIED | R10, undated live, acc |
| RT-27 | 635 | LIMIT | This is not a promise of zero network offset or audiovisual sample lock. | VERIFIED | R10 |
| RT-28 | 637 | DOC | `AudioPlayer` offers readiness via `IsReady`, playhead position via `TimePosition`, and scheduled `Play`/`Stop` using an `atTime` derived from `SoundService:GetMixerTime()`. Scheduled operations give sample-accurate, frame-rate-independent local audio timing. | VERIFIED | R11, R12, undated live, acc |
| RT-29 | 637 | DOC | The mixer clock starts at an arbitrary value and can differ between machines. Roblox says it is unsuitable for synchronization across sessions or networks. | VERIFIED | R12 |
| RT-30 | 637 | DOC | `IsReady` can become false under extreme memory pressure. | VERIFIED | R11 |
| RT-31 | 639 | PROC | Clock contract for a shared event: distribute an authorized scene ID and a future server-time start; map the remaining delay onto each client's mixer clock for scheduled local sound. Keep the camera's visual timeline and local audio timeline aligned by a defined correction policy. Never send one client's raw mixer timestamp to another. Late arrival picks a deliberate catch-up, wait or fallback path. | OPINION, clock contract | grounded in R10-R12 |
| RT-32 | 639 | LIMIT | This is a proposed method, not a demonstrated sample-perfect multiplayer solution. | OPINION | same |
| RT-33 | 641 | DOC | `ParticleEmitter:Emit()` makes a burst; `Clear()` removes already emitted particles. Just disabling emission is not the same as clearing an existing burst. | VERIFIED | R13, undated live, acc |
| RT-34 | 643 | PROC | Tag spawned effects with the scene token. On a hard skip, stop future emission and decide which existing particles to clear and which to let finish. Cosmetic impacts follow the presentation cue; damage stays a server gameplay decision. | OPINION, VFX teardown | grounded in R13 |
| RT-35 | 643 | PROC | Verify the cue-to-impact relation with a frame capture; matching text timestamps cannot prove visual synchronization. | OPINION | grounded in R13 |

## 6. Roblox runtime: light, streaming, UI, tools (FP:645-679)

| ID | FP | Kind | Lesson | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| RT-36 | 647 | DOC | Post-processing can be parented to `Lighting` (shared scene) or `CurrentCamera` (one player's view). Documented effects include bloom, blur, color correction, depth of field, sun rays and `ColorGradingEffect`. | VERIFIED | R14, R15, undated live, acc |
| RT-37 | 647 | DOC | `DepthOfFieldEffect` can render differently on low-end devices or under different quality settings. | VERIFIED | R15 |
| RT-38 | 649 | PROC | Prefer scene-owned camera post-effects for a private flashback, color shift or menu-like world blur. Snapshot and restore only the properties the cinematic owns; do not overwrite a newer weather/time-of-day controller with a stale snapshot. | OPINION, lighting ownership | grounded in R14/R15 |
| RT-39 | 649 | PROC | Readability must survive reduced or absent expensive effects. Stage actor and key object with contrast, shape and light direction; do not make crucial storytelling depend only on depth-of-field blur. | OPINION | same |
| RT-40 | 651 | DOC | Roblox performance guidance recommends cutting unnecessary light/shadow work and inspecting rendering scopes. It sets no universal safe number of cinematic lights, characters or moving camera shots for all phones. | VERIFIED | R29, undated live, acc |
| RT-41 | 653 | PROC | Profile the complete reveal (asset readiness, animated actors, particles, shadows, UI, camera callbacks) on the team's supported devices; record worst transitions and repeat-play behavior. A desktop Studio preview is not a phone result. | OPINION, performance sign-off | grounded in R04/R15/R22/R29 |
| RT-42 | 653 | LIMIT | The paper claims no fixed phone memory budget, universal cutscene FPS target, camera-speed ceiling or shot-length limit. | OPINION | same |
| RT-43 | 657 | DOC | Instance streaming normally follows the player's replication focus. `RequestStreamAroundAsync` is a transient prefetch route; additional replication foci keep chosen areas loaded until released. (Register R21 quote names `Player:AddReplicationFocus()`, FP:1865.) | VERIFIED | R20, R21, undated live, acc |
| RT-44 | 657 | DOC | Extra foci raise server streaming/update work and limit client memory adaptation. The techniques guide frames prefetch success by the minimum radius, not a guarantee that every asset in a far-away composition is rendered. | VERIFIED | R20, R21 |
| RT-45 | 659 | DOC | Frustum streaming is additive and per player, extending normal streaming in the camera's view. `Player.FrustumStreaming` is server-set; client assignments have no effect. | VERIFIED | R22, undated live, acc |
| RT-46 | 659 | DOC | Limits: automatic activation can lag; rapid camera movement can invalidate the frustum and cause churn; reduced draw distance can disable it; no occlusion culling; does not reduce the normal streaming workload; more instances can raise memory and CPU use. | VERIFIED | R22 |
| RT-47 | 659 | INFER | The paper says these limits directly matter to whip pans and remote establishing shots. | VERIFIED (paragraph mark; inference) | R22 |
| RT-48 | 661 | DOC | `ContentProvider:PreloadAsync()` loads referenced assets, not whole-world instance residency. Roblox advises preloading essential assets, not the whole Workspace. Individual failures show in the callback's final `AssetFetchStatus`; the method can keep going without throwing for those assets. | VERIFIED | R23, undated live, acc |
| RT-49 | 663 | PROC | Shot-readiness contract: keep separate readiness checks for required instances, geometry/textures, animation and sound. Prepare the next set before cutting to it, then verify named critical actors and set pieces. A returned prefetch call alone is not enough. | OPINION, shot-readiness contract | grounded in R20-R23 |
| RT-50 | 663 | PROC | If the reveal cannot be made ready: use an approved close shot, opaque transition or narrative fallback, and release controls safely. | OPINION | same |
| RT-51 | 663 | PROC | On every terminal path release temporary replication foci and restore the prior frustum mode. Do not mark the whole cinematic world persistent to hide a loading bug. | OPINION | same |
| RT-52 | 667 | DOC | `ScreenGui.ScreenInsets` separates device cutouts from Roblox core-UI safe regions. `None` is meant for noninteractive background-like content, not for important controls. | VERIFIED | R16, undated live, acc |
| RT-53 | 667 | DOC | `PreferredTextSize` affects text rendering; `TextScaled` bypasses that preference; text-size constraints may cap it. | VERIFIED | R16, R17 |
| RT-54 | 667 | DOC | `ReducedMotionEnabled` expresses a preference to reduce or remove UI motion. The docs do not claim it automatically disables a custom 3D cinematic camera. | VERIFIED | R16, R17 |
| RT-55 | 669 | DOC | The Input Action System supports cross-device action bindings and switchable contexts. `InputContext` has `Enabled`, `Priority`, `Sink`; higher-priority contexts run first; sinking affects matching lower-priority bindings. It is not a global disable of every possible gameplay script. | VERIFIED | R18, R19, undated live, acc |
| RT-56 | 671 | PROC | Decorative letterbox bars go on a noninteractive full-bleed layer; subtitles and skip controls on a safe-area layer. Subtitle block: wrapping, speaker identity where needed, localization room, a backing that survives bright images. Keep the user's text scale. | OPINION, accessibility implementation | grounded in R16-R19 |
| RT-57 | 671 | PROC | Offer a reduced-camera-motion variant explicitly; do not assume a UI preference alters scripted shake. Expose Skip as touch, gamepad and keyboard actions, and keep the skip context enabled when gameplay contexts are suspended. | OPINION | same |
| RT-58 | 671 | LIMIT | No source here proves a universal wait-before-skip duration or completion-rate optimum. | OPINION | same |
| RT-59 | 675 | DOC | The original xsixx Creator Store listing names Moon Animator 2 as a Plugin with version string `V36000` (listing updated 2026-08-19). | VERIFIED | R26, POST |
| RT-60 | 675 | LIMIT | This verifies a maintained author listing only: not reliable export of every camera/effect track, not an official Roblox sequencer, not a production-tested cutscene runtime. Unofficial reuploads are not the seller's source. | VERIFIED | R26 |
| RT-61 | 677 | DOC | Roblox's runtime freecam supports cinematic capture during solo playtesting. It is a capture/view tool, not proof the motion exists as replayable gameplay logic. (Register R27 quote gives the toggle `Left Shift + P`, FP:1915.) | VERIFIED | R27, undated live, acc |
| RT-62 | 677 | DOC | `VideoFrame` plays video in games; documented limit: two videos at once. | VERIFIED | R28, undated live, acc |
| RT-63 | 677 | DOC | The video upload workflow currently describes a beta toggle and specific eligibility/asset restrictions. Upload ceilings are not recommended film durations. | VERIFIED | R28 |
| RT-64 | 679 | PROC | Small-team tool choice: Blender for previs and authored motion; Roblox's documented camera/animation/audio/UI APIs for the deterministic playback controller; Moon Animator only if its workflow demonstrably speeds iteration. Pin the plugin version. Validate one camera-plus-character-plus-audio export before building the film around it. Keep portable shot/cue data apart from plugin UI. Review captured Roblox playback, not only polished Blender renders. | OPINION | grounded in R01-R28 |

## 7. Proposed terminal state and review contract (FP:681-693)

All rows are proposals. Tag: OPINION, proposed acceptance design, grounded in R01/R04/R11-R25. Nothing was executed.

| ID | FP | Kind | Lesson | Tag |
| --- | --- | --- | --- | --- |
| TC-01 | 683 | PROC | Every run has one terminal reason and one idempotent teardown. | OPINION |
| TC-02 | 683 | PROC | Teardown steps: (a) cancel future callbacks, tweens and audio schedules; (b) disconnect cue listeners; (c) unbind camera updates; (d) stop scene-owned tracks and effects; (e) release streaming requests/foci under the server's ownership; (f) restore the current valid gameplay camera and input state; (g) remove subtitles and bars; (h) return audio mixing to its designated owner. | OPINION |
| TC-03 | 683 | PROC | Never blindly restore a destroyed pre-respawn `Humanoid`. Never overwrite a controller that took ownership after this scene started. | OPINION |
| TC-04 | 685 | PROC | Finish path: evaluate the final shot/pose; hand control back at an authored safe view; request only the permitted server transition. Do not leave a camera binding running invisibly after the bars go. | OPINION |
| TC-05 | 687 | PROC | Skip path: resolve the same authorized story outcome where that is the design, without replaying transient cues. A shared boss intro needs an explicit per-player or group policy; one player's Skip must not silently teleport everyone. Repeated skip presses have one result. | OPINION |
| TC-06 | 689 | PROC | Failure path triggers: failed required assets, removed actors, camera replacement, death/respawn, interrupted teleport, superseding scene trigger. Each runs the defined fallback and teardown. The player must not stay immobilized behind a black overlay. Test asset failure apart from a successfully returned preload call. | OPINION |
| TC-07 | 691 | PROC | Disconnect path: release server-side participant and temporary-focus ownership even if the client never sends a completion event. Rejoin follows a deliberate replay, resume or skip rule. Do not infer that a disconnected presentation earned an irreversible reward. | OPINION |

Review captures (FP:693, OPINION, "proposed tests, not tests completed by this paper"):

| ID | FP | Capture to run |
| --- | --- | --- |
| CP-01 | 693 | Normal completion |
| CP-02 | 693 | Skip during each major cue |
| CP-03 | 693 | Repeated skip |
| CP-04 | 693 | Skip during loading |
| CP-05 | 693 | Denied or missing audio |
| CP-06 | 693 | Missing streamed actor |
| CP-07 | 693 | Rapid distant cut |
| CP-08 | 693 | Low-quality rendering |
| CP-09 | 693 | Resized or aspect-changed viewport |
| CP-10 | 693 | Large text |
| CP-11 | 693 | Reduced motion |
| CP-12 | 693 | Touch and gamepad input |
| CP-13 | 693 | Respawn |
| CP-14 | 693 | Two simultaneous clients |
| CP-15 | 693 | Late join |
| CP-16 | 693 | For each: record actual camera ownership, remaining connections/instances, server state, and the visible/audible result. |
| CP-17 | 693 | Pass needs correct story comprehension and restored control, not just an empty output console. |

### 7.1 Contract at a glance (pointers only; no new claims)

| Part | Rows |
| --- | --- |
| Scene token, one camera owner, server authorizes / client presents | RT-04 to RT-08, RT-16 |
| Readiness checks (instances, geometry/textures, animation, sound), fallback | RT-49 to RT-51, RT-48, RT-43 to RT-46 |
| Terminal paths and teardown | TC-01 to TC-07 |
| Cue policy (stable IDs, seek, skip, replay) | RT-25, TC-05 |
| Clocks | RT-26 to RT-32 |
| Time convention (all OPINION or VERIFIED arithmetic): scene rate = fps/fps_base; t = (k-k0)/r; cut list as `[start, next-start)`; samples differ from intervals; keep source rates as rationals; log first included / first excluded frame | BL-28, BL-30 to BL-35 |

## 8. Numbers

### 8.1 The paper's own rule tables ("Rule | Number | Evidence | Source and date")

| ID | FP | Rule | Number | Mark (paper) | Source and date (paper) |
| --- | --- | --- | --- | --- | --- |
| N-01 | 521 | Review edited boards before expensive final imagery | No mandatory panel count | VERIFIED | A09-A10, undated; acc 2026-10-21 |
| N-02 | 523 | Rough layout evaluates cameras and performances together | No mandated lens mm | VERIFIED | A09, undated; acc |
| N-03 | 525 | Recheck camera and continuity after animation | No mandatory pass count | VERIFIED | A09, undated; acc |
| N-04 | 599 | Pin the documented stable tool | Blender 5.2.2 LTS | VERIFIED | B01, 15 September 2026 |
| N-05 | 601 | Use exact time conventions | Effective rate equals fps divided by fps_base | VERIFIED | B11, undated; acc |
| N-06 | 603 | Do not confuse samples with intervals | Frames 1 through 31 are 31 samples | VERIFIED derived arithmetic | B06 and B11, acc |
| N-07 | 605 | Review generated image continuity | No deterministic guarantee | VERIFIED and OPINION | B15, 8 September 2026; B16, acc |
| N-08 | 701 | Control and restore the local camera deliberately | API FOV values are degrees | VERIFIED and OPINION | R01 to R04, acc |
| N-09 | 703 | Separate animation, mixer and server clocks | Cross client timing guarantee UNKNOWN | VERIFIED and OPINION | R10 to R12, acc |
| N-10 | 705 | Prepare required streamed content | No universal loading delay | VERIFIED and OPINION | R20 to R23, acc |
| N-11 | 707 | Test every terminal path | No tests executed by this paper | OPINION | Proposed contract, 21 October 2026 |

### 8.2 Numbers and formulas that appear only in prose

| ID | FP | Number or formula (unchanged) | Scope | Paper's limit | Tag | Src |
| --- | --- | --- | --- | --- | --- | --- |
| N-12 | 619 | `FieldOfView` clamp 1-120 degrees, default 70 | `Camera` API | Range/default, not recommended lenses | VERIFIED | R02, R03 |
| N-13 | 635 | Within 0.6% of local clock rate | `Workspace:GetServerTimeNow()` rate tolerance | Not zero offset, not sample lock | VERIFIED | R10 |
| N-14 | 575 | 100/3 ms at 30 fps; 50/3 ms at 60 fps | One frame interval | Exactly; not 33 ms / 16 ms | VERIFIED, arithmetic | derived |
| N-15 | 575 | t = (k-k0)/r; frames 1 and 31 at 30 fps = 30 intervals = 1 s; frames 1-31 inclusive = 31 samples = 31/30 s | Frame position vs sample duration | `[start, next-start)` cut lists avoid the off-by-one | VERIFIED, arithmetic | derived |
| N-16 | 573, 601 | effective scene rate = fps/fps_base | Blender `fps`, `fps_base` | - | VERIFIED | B11 |
| N-17 | 577 | 30000/1001 | Example source rate | Keep the fraction; not 30, not exactly 29.97 | OPINION | none |
| N-18 | 541 | H = 2 atan(Sx/(2f)); V = 2 atan(Sy/(2f)); each angle in (0, pi) | Centered rectilinear pinhole, no shift/distortion/squeeze; Sx, Sy, f > 0 | Ideal model, first-order | VERIFIED, geometric derivation | B05 |
| N-19 | 543 | tan(H/2) = a tan(V/2); V = 2 atan(tan(H/2)/a); a = displayed width / displayed height after pixel aspect and crop | Same projection; a > 0 | a is not automatically file width/height | VERIFIED, geometric derivation | B05, B06 |
| N-20 | 545 | x_image = f X/Z; y_image = f Y/Z | Camera-space ideal projection | Maths inference, not psychology | VERIFIED, geometric derivation | B05 |
| N-21 | 559 | p(t) speed = ||dp/dt||; average = L/T; s(u) = 3u² - 2u³, u = t/T; speed (L/T)(6u - 6u²); peak 3L/(2T) at u = 1/2; zero endpoint velocity; endpoint acceleration nonzero | Straight segment, length L, T > 0 s | Illustrative easing, not Blender default, no feel claim | VERIFIED, mathematical derivation | none |
| N-22 | 565 | R_target = Q R_source Q^-1 (position also needs scale and origin offset) | Rigid transform, Q = verified basis conversion | Not a verified Roblox import feature; no axis map asserted | OPINION | none |
| N-23 | 677 | Two videos at once | `VideoFrame` | Upload ceilings are not film durations | VERIFIED | R28 |
| N-24 | 675 | `V36000`; listing updated 2026-08-19 | Moon Animator 2, xsixx listing | Not an exporter guarantee | VERIFIED | R26 |
| N-25 | 531, 591, 593, 631 | 5.2.2 LTS, 2026-09-15; Images 2.5, 2026-09-08; B17, 2026-04-10; Animation Graphs full release 2026-07-15; State Machine / Expression beta 2026-10-08 | Dated sources | - | VERIFIED | B01, B15, B17, R08, R09 |
| N-26 | 521-525, 561, 585, 653, 671, 697 | None established: panel count, lens mm, pass count, degrees-per-second camera limit, render time, phone memory budget, cutscene FPS target, camera-speed ceiling, shot-length limit, wait-before-skip duration, best shot duration, lens preset, acceptable cross-client audio error | Production decisions needing captures and tests | Paper claims none | VERIFIED / OPINION | n/a |

## 9. Evidence gaps the paper preserves (FP:695-697)

| ID | FP | Gap or disagreement | Tag |
| --- | --- | --- | --- |
| EG-01 | 697 | Primary docs establish available mechanisms, not an all-purpose cutscene product, benchmark or perceptual quality guarantee. | VERIFIED/OPINION |
| EG-02 | 697 | The FOV guide/API wording needs care: use the API's vertical-angle definition plus the invariant-axis semantics of the mode (the paper writes `FOVMode`; see X-05). | VERIFIED/OPINION |
| EG-03 | 697 | Base Animation Graphs and the later node betas have different release status. | VERIFIED/OPINION |
| EG-04 | 697 | Mixer-time precision does not contradict approximate server-time sync: different clocks, different guarantees. | VERIFIED/OPINION |
| EG-05 | 697 | A positive plugin listing or version does not certify its exporter. | VERIFIED/OPINION |
| EG-06 | 697 | No credible source found supplies a universal best shot duration, skip delay, lens preset, phone budget or acceptable cross-client audio error. These stay production decisions needing real captures and tests. | VERIFIED/OPINION |

## 10. Source ids used in lines 509-707 (resolved from FP:1409-1931)

All register entries are tagged VERIFIED by the paper. "acc" = accessed 2026-10-21. Quotes are the register's own, attributed to the source. The register gives no scope line for R01-R29 except R26.

| ID | Source | Date and limits | POST | URL | Cited at FP | Reg. FP | Key quote (register) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A09 | Disney Animation, "Layout & Final Layout" | undated; acc. Not a guaranteed pipeline for Roblox or every studio; no fixed lens/time budgets | live-read | https://www.disneyanimation.com/process/layout/ | 513, 521-525 | 1409 | "the first 3D representation of that storyboard" |
| A10 | Disney Animation, "Story" | undated; acc. Page text read; linked storyboard images not inspected | live-read | https://www.disneyanimation.com/process/story/ | 515, 521 | 1419 | "emotion, expression, timing, staging, and framing" |
| B01 | Blender releases | 2026-09-15 patch listing; checked 2026-10-21 | yes | https://www.blender.org/releases/ | 531, 599 | 1529 | "Last updated to 5.2.2 on September 15, 2026" |
| B02 | Blender 5.2 manual, Viewport Render | undated; acc; localized (sl) page, English content | live-read | https://docs.blender.org/manual/sl/5.2/editors/3dview/viewport_render.html | 533 | 1541 | "To render an animation, use 3D Viewport ‣ View ‣ Render Playblast." |
| B03 | Blender 5.2 manual, Cameras: sensor fit | undated; acc; localized (id) page | live-read | https://docs.blender.org/manual/id/5.2/render/cameras.html | 539 | 1551 | "Adjusts how the camera's sensor fits within the outputs dimension" (cut) |
| B04 | Blender 5.2 manual, Cameras: projection | undated; acc; localized (nl); same manual as B03; combined direct quotes restricted | live-read | https://docs.blender.org/manual/nl/5.2/render/cameras.html | 539 | 1561 | none given |
| B05 | Edmund Optics, "Understanding Focal Length and Field of View" | undated; acc; mathematical extensions identified | live-read | https://www.edmundoptics.com/knowledge-center/application-notes/imaging/understanding-focal-length-and-field-of-view | 541, 543, 545 | 1569 | "the above examples are only first-order approximations" |
| B06 | Blender 5.2 manual, Format | undated; acc; "latest" URL is mutable | live-read | https://docs.blender.org/manual/en/latest/render/output/properties/format.html | 543, 573, 575 | 1579 | "The frame rate, expressed in frames per second." |
| B07 | Blender 5.2 manual, Track To | undated; acc; "latest" URL | live-read | https://docs.blender.org/manual/en/latest/animation/constraints/tracking/track_to.html | 553 | 1589 | "the roll around the tracking axis will become unstable" |
| B08 | Blender 5.2 manual, F-Curve Properties | undated; acc; localized (id) | live-read | https://docs.blender.org/manual/id/5.2/editors/graph_editor/fcurves/properties.html | 557 | 1599 | "prevents abrupt changes in value but not in speed" |
| B09 | Blender 5.2 Python API, Depsgraph | undated; acc | live-read | https://docs.blender.org/api/5.2/bpy.types.Depsgraph.html | 563 | 1609 | "animation, constraints, and modifiers taken into account" |
| B10 | Blender 5.2 manual, Markers | undated; acc; official staging mirror, version shown 5.2 | live-read | https://docs.staging.blender.org/manual/en/latest/animation/markers.html | 569 | 1619 | "markers are always placed at a whole frame number" |
| B11 | Blender 5.2 Python API, RenderSettings | undated; acc | live-read | https://docs.blender.org/api/5.2/bpy.types.RenderSettings.html | 573, 575, 601, 603 | 1629 | "Framerate base" |
| B12 | Blender 5.2 manual, Movie Strip | undated; acc | live-read | https://docs.blender.org/manual/en/5.2/video_editing/edit/montage/strips/movie.html | 573 | 1639 | "Sets the Scene Frame Rate to the frame rate encoded in the movie file." |
| B13 | Blender 5.2 manual, Strip Properties | undated; acc; staging mirror | live-read | https://docs.staging.blender.org/manual/en/latest/video_editing/edit/montage/strips/strip_properties.html | 573 | 1649 | "the perceived speed of the media will be wrong" |
| B14 | Blender 5.2 manual, Rendering Animations | undated; acc; staging mirror | live-read | https://docs.staging.blender.org/manual/en/latest/render/output/animation.html | 583 | 1659 | "Blender creates a file for each frame of the animation" |
| B15 | OpenAI, "Introducing ChatGPT Images 2.5" | 2026-09-08. Vendor claim; not an independent continuity benchmark | yes | https://openai.com/index/introducing-chatgpt-images-2-5/ | 591, 605 | 1669 | "follows editing instructions more reliably across multiple turns" |
| B16 | OpenAI, image generation guide (API) | undated live; acc. API docs, not all ChatGPT UI settings | live-read | https://developers.openai.com/api/docs/guides/image-generation | 593, 605 | 1679 | "the model may occasionally struggle to maintain visual consistency" |
| B17 | OpenAI Academy, "Creating images with ChatGPT" | 2026-04-10 | no | https://openai.com/academy/image-generation/ | 593 | 1689 | "Refer to each image by order and explain how they relate to each other." |
| R01 | Roblox docs, Customize the camera | undated living; acc | live-read | https://create.roblox.com/docs/workspace/camera | 611, 701 | 1699 | "Setting this to Scriptable gives you full control of the camera." |
| R02 | Roblox docs, Camera API | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/Camera | 611, 619, 701 | 1707 | "Sets the angle of the camera's vertical field of view." |
| R03 | Roblox docs, FieldOfViewMode | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/enums/FieldOfViewMode | 619, 701 | 1715 | "The camera holds its vertical field of view constant when the viewport is resized." |
| R04 | Roblox docs, RunService | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/RunService | 623, 653, 701 | 1723 | "All rendering updates will wait until the code in the render step finishes." |
| R05 | Roblox docs, Task scheduler | undated living; acc | live-read | https://create.roblox.com/docs/performance-optimization/microprofiler/task-scheduler | 623 | 1731 | "Only tasks that must be done after input but before rendering" |
| R06 | Roblox docs, Animation events | undated living; acc | live-read | https://create.roblox.com/docs/animation/events | 629 | 1739 | "You can define animation event markers across the timeline span" |
| R07 | Roblox docs, Animation Graph Editor | undated living; acc | live-read | https://create.roblox.com/docs/animation/graph-editor | 629 | 1747 | "If the weight reaches zero at any point, the event is silenced." |
| R08 | Roblox DevForum, Animation Graphs full release | 2026-07-15 | yes | https://devforum.roblox.com/t/full-release-animation-graphs-create-complex-character-motion-visually/4739840 | 631 | 1755 | "With this release, animation graphs run live in your active games." |
| R09 | Roblox DevForum, State Machines and Luau Expressions beta | 2026-10-08 | yes | https://devforum.roblox.com/t/studio-beta-introducing-state-machines-and-luau-expressions-for-animation-graphs/4921939/1 | 631 | 1763 | "State Machine and Expression nodes are now in beta in the Animation Graph Editor." |
| R10 | Roblox docs, Workspace (GetServerTimeNow) | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/Workspace | 635, 639, 703 | 1771 | "The estimated Unix timestamp on the server." |
| R11 | Roblox docs, AudioPlayer | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/AudioPlayer | 637, 639, 703 | 1779 | "Denotes whether this AudioPlayer is loaded, buffered, and ready to play." |
| R12 | Roblox docs, SoundService (mixer clock) | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/SoundService | 637, 639, 703 | 1787 | "It is not suitable for synchronizing audio across sessions or networks." |
| R13 | Roblox docs, ParticleEmitter | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/ParticleEmitter | 641, 643 | 1795 | "Clears all particles that have been emitted." |
| R14 | Roblox docs, Post-processing effects | undated living; acc | live-read | https://create.roblox.com/docs/environment/post-processing-effects | 647, 649 | 1803 | "they only display to a specific player." |
| R15 | Roblox docs, DepthOfFieldEffect | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/DepthOfFieldEffect | 647, 649, 653 | 1811 | "it may render differently on low-end devices" |
| R16 | Roblox docs, ScreenGui | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/ScreenGui | 667, 671 | 1819 | "Controls the safe area insets that are applied to the contents of the ScreenGui." |
| R17 | Roblox docs, Accessibility guidelines | undated living; acc | live-read | https://create.roblox.com/docs/production/publishing/accessibility | 667, 671 | 1827 | "your user interface should accommodate each." |
| R18 | Roblox docs, Input Action System | undated living; acc | live-read | https://create.roblox.com/docs/input/input-action-system | 669, 671 | 1835 | "The cross-platform Input Action System lets you connect" |
| R19 | Roblox docs, InputContext / Priority | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/InputContext/Priority | 669, 671 | 1843 | "higher priority InputContext instances run before lower ones" |
| R20 | Roblox docs, Instance streaming | undated living; acc | live-read | https://create.roblox.com/docs/workspace/streaming | 657, 663, 705 | 1851 | "each additional focus increases the server's workload" (cut) |
| R21 | Roblox docs, Streaming techniques | undated living; acc | live-read | https://create.roblox.com/docs/workspace/streaming/techniques | 657, 663, 705 | 1859 | "use Player:AddReplicationFocus() on a limited basis" (cut) |
| R22 | Roblox docs, Frustum streaming | undated living; acc | live-read | https://create.roblox.com/docs/workspace/streaming/frustum | 653, 659, 663, 705 | 1867 | "It is not a replacement for standard instance streaming." |
| R23 | Roblox docs, ContentProvider | undated living; acc | live-read | https://create.roblox.com/docs/reference/engine/classes/ContentProvider | 661, 663, 705 | 1875 | "Only preload essential assets, not the entire Workspace." |
| R24 | Roblox docs, Client-server runtime | undated living; acc | live-read | https://create.roblox.com/docs/projects/client-server | 613, 615, 683 | 1883 | "The Roblox server is the ultimate authority for maintaining the game's state" |
| R25 | Roblox docs, Securing the client-server boundary | undated living; acc | live-read | https://create.roblox.com/docs/scripting/security/client-server-boundary | 613, 615, 683 | 1891 | "Every piece of data sent from a client must be validated by the server" |
| R26 | Creator Store listing, Moon Animator 2 (xsixx) | listing updated 2026-08-19; acc. Seller listing and version only; no export reliability or Studio test | yes | https://create.roblox.com/store/asset/4725618216/Moon-Animator- | 675, 679 | 1899 | "V36000" |
| R27 | Roblox docs, Thumbnails (free camera mode) | undated living; acc | live-read | https://create.roblox.com/docs/production/publishing/thumbnails | 677 | 1909 | "Press Left Shift + P during a solo playtest to toggle it on or off." |
| R28 | Roblox docs, Video frames | undated living; acc | live-read | https://create.roblox.com/docs/ui/video-frames | 677 | 1917 | "Currently, a maximum of two videos can play simultaneously." |
| R29 | Roblox docs, Improve performance | undated living; acc | live-read | https://create.roblox.com/docs/performance-optimization/improve | 651, 653 | 1925 | "Disabling shadow casting on appropriate parts and light objects" |

Blender access note (FP:1539): the paper says Blender pages were mostly read through a search index because direct opens returned HTTP 402, and that nothing was run.

## 11. Claims for the fact-check

Priority: P1 = Roblox, Blender or ChatGPT behaviour, API name, value, range, release status, or anything dated after 2026-06-01. P2 = derived maths the tool will rely on (formula exactly as the paper gives it). P3 = background. "Check against" gives the local mirror path guess (`knowledge/external/roblox-creator-docs/`, abbreviated `MIRROR/`), the live URL id from section 10, or the connected Blender (its bundled `data/api/` and `data/manual/` RST files, or `bpy` queries). Path guesses are my hints, not paper claims. Fact-check against the source, not the paper.

| ID | Claim (paraphrase) | FP | Pri | Check against | Src date | POST |
| --- | --- | --- | --- | --- | --- | --- |
| FC-01 | Blender `5.2.2 LTS`, updated 2026-09-15, is the current 5.2 stable release | 531, 599 | P1 | B01 live; connected Blender version string | 2026-09-15 | yes |
| FC-02 | 5.2 manual: `View > Render Playblast` renders animation; `Render Viewport Preview` is still output | 533 | P1 | B02 (try the en/5.2 URL); Blender bundled manual grep "Render Playblast"; the connected Blender's View menu | undated | live-read |
| FC-03 | Perspective and orthographic projection; focal length changes view angle; `Sensor Fit` `Horizontal` derives height, `Vertical` derives width, `Auto` adapts | 539 | P1 | B03, B04 (en/5.2); bundled manual `render/cameras`; connected Blender camera properties | undated | live-read |
| FC-04 | `Track To`: local track axis plus `Up` axis; roll unstable when owner is nearly above target; `Damped Track` suggested; Track and Up axes must differ | 553 | P1 | B07; bundled manual constraints/tracking | undated | live-read |
| FC-05 | F-curves: Linear does not give speed continuity; `Auto Clamped` prevents overshoot; continuous-acceleration handling can propagate changes along the curve | 557 | P1 | B08; bundled manual graph_editor/fcurves | undated | live-read |
| FC-06 | `Depsgraph` is needed to read state with animation, constraints and modifiers applied | 563 | P1 | B09; bundled API `bpy.types.Depsgraph` | undated | live-read |
| FC-07 | Camera-bound timeline markers switch the active camera at their frames; markers sit on whole frames | 569 | P1 | B10 (en/5.2 URL); bundled manual animation/markers; connected Blender | undated | live-read |
| FC-08 | `fps` and `fps_base` exist on render settings; effective rate = fps/fps_base | 573, 601 | P1 | B11; connected Blender `scene.render.fps`, `fps_base` | undated | live-read |
| FC-09 | Movie-strip import can set the scene rate from the movie; source/scene rate mismatch gives wrong perceived speed unless compensated | 573 | P1 | B12, B13; bundled manual video_editing | undated | live-read |
| FC-10 | Blender can write per-frame image files and the Video Sequencer can combine them with audio into a movie | 583 | P1 | B14; bundled manual render/output/animation | undated | live-read |
| FC-11 | H = 2 atan(Sx/(2f)); V = 2 atan(Sy/(2f)); preconditions as in N-18 | 541 | P2 | Recompute; connected Blender camera angle values for a known sensor and lens; B05 | undated | live-read |
| FC-12 | tan(H/2) = a tan(V/2); V = 2 atan(tan(H/2)/a); a = displayed width / height after pixel aspect and crop | 543 | P2 | Recompute from FC-11; B05, B06 | undated | live-read |
| FC-13 | x_image = f X/Z; y_image = f Y/Z; the dolly-plus-zoom perspective statement | 545 | P2 | Recompute; B05 | undated | live-read |
| FC-14 | Smoothstep speed (L/T)(6u - 6u²), peak 3L/(2T) at u = 1/2, zero endpoint velocity, nonzero endpoint acceleration | 559 | P2 | Recompute by differentiation | n/a | no |
| FC-15 | `t = (k-k0)/r`; frames 1 and 31 at 30 fps = 1 s; inclusive 1-31 = 31 samples = 31/30 s; 100/3 ms and 50/3 ms | 575 | P2 | Recompute | n/a | no |
| FC-16 | R_target = Q R_source Q^-1 for orientation; position needs scale and origin offset (the paper marks it OPINION algebra) | 565 | P2 | Recompute; test with connected Blender matrices | n/a | no |
| FC-17 | OpenAI announced ChatGPT Images 2.5 on 2026-09-08; vendor claims better reference preservation and multi-turn editing | 591 | P1 | B15 live | 2026-09-08 | yes |
| FC-18 | Image-generation docs still list recurring-character consistency and precise composition as limitations | 593 | P1 | B16 live | undated | live-read |
| FC-19 | ChatGPT guidance: identify references by order, explain roles, focused revisions | 593 | P1 | B17 live | 2026-04-10 | no |
| FC-20 | `CurrentCamera` is per client; `CameraType` `Scriptable` stops default camera control; `CFrame` sets pose | 611 | P1 | MIRROR/workspace/camera/index.md; MIRROR/_api-reference/classes/Camera.yaml; MIRROR/_api-reference/enums/CameraType.yaml; R01, R02 | undated | live-read |
| FC-21 | `Camera.Focus` needs updating in Scriptable use (visual-detail proximity); it neither loads a distant set nor replaces `DepthOfFieldEffect.FocusDistance` | 611 | P1 | Camera.yaml (`Focus`); DepthOfFieldEffect.yaml (`FocusDistance`); R01, R02 | undated | live-read |
| FC-22 | `FieldOfView` is vertical, clamp 1-120, default 70 | 619 | P1 | Camera.yaml; R02 | undated | live-read |
| FC-23 | `FieldOfViewMode` members `Vertical`, `Diagonal`, `MaxAxis` and which angle each holds constant (register quote backs only the vertical case) | 619 | P1 | MIRROR/_api-reference/enums/FieldOfViewMode.yaml; R03 | undated | live-read |
| FC-24 | Camera overview's wording about FOV direction differs from the API wording | 619, 697 | P1 | MIRROR/workspace/camera/index.md vs Camera.yaml; R01 vs R02 | undated | live-read |
| FC-25 | `BindToRenderStep`: ordering by priority (lower first), equal priority unspecified, removal by name, rendering waits for callbacks | 623 | P1 | MIRROR/_api-reference/classes/RunService.yaml; MIRROR/_api-reference/enums/RenderPriority.yaml; R04 | undated | live-read |
| FC-26 | Task scheduler page: camera movement fits render-step work; avoid unnecessary bindings | 623 | P1 | MIRROR/performance-optimization/microprofiler/task-scheduler.md; R05 | undated | live-read |
| FC-27 | `AnimationTrack:GetMarkerReachedSignal()` with optional string parameter; markers authored on the clip timeline | 629 | P1 | MIRROR/_api-reference/classes/AnimationTrack.yaml; MIRROR/animation/events.md; R06 | undated | live-read |
| FC-28 | Animation Graph events carry weights; zero-weight events silenced; blend/selection nodes can suppress non-primary events | 629 | P1 | MIRROR/animation/graph-editor.md; R07 | undated | live-read |
| FC-29 | Animation Graphs fully released for live games (July 2026) | 631 | P1 | R08 live | 2026-07-15 | yes |
| FC-30 | State Machine and Expression nodes: Studio beta (October 2026); FAQ says Studio only, not live games, during beta | 631 | P1 | R09 live; MIRROR/animation/graph-editor-state-machine.md | 2026-10-08 | yes |
| FC-31 | `Workspace:GetServerTimeNow()`: smoothed client approximation of server Unix time; within 0.6% of local clock rate | 635 | P1 | MIRROR/_api-reference/classes/Workspace.yaml; R10 | undated | live-read |
| FC-32 | `AudioPlayer` `IsReady`, `TimePosition`; scheduled `Play`/`Stop` with `atTime` from `SoundService:GetMixerTime()`; sample-accurate, frame-rate-independent | 637 | P1 | MIRROR/_api-reference/classes/AudioPlayer.yaml; SoundService.yaml; MIRROR/audio/objects.md; R11, R12 | undated | live-read |
| FC-33 | Mixer clock starts at an arbitrary value, differs across machines, unsuitable for cross-session/network sync | 637 | P1 | SoundService.yaml; R12 | undated | live-read |
| FC-34 | `IsReady` can become false under extreme memory pressure | 637 | P1 | AudioPlayer.yaml; R11 | undated | live-read |
| FC-35 | `ParticleEmitter:Emit()` bursts; `Clear()` removes emitted particles; disabling emission does not clear | 641 | P1 | MIRROR/_api-reference/classes/ParticleEmitter.yaml; R13 | undated | live-read |
| FC-36 | Post-processing parented to `Lighting` (shared) or `CurrentCamera` (per player); effect list incl. `ColorGradingEffect` | 647 | P1 | MIRROR/environment/post-processing-effects.md; Lighting.yaml; R14 | undated | live-read |
| FC-37 | `DepthOfFieldEffect` may render differently on low-end devices / quality settings | 647 | P1 | DepthOfFieldEffect.yaml; R15 | undated | live-read |
| FC-38 | Performance guidance: reduce unnecessary light/shadow work, inspect rendering scopes; no universal number | 651 | P1 | MIRROR/performance-optimization/improve.md; R29 | undated | live-read |
| FC-39 | `RequestStreamAroundAsync` transient prefetch; extra foci (`Player:AddReplicationFocus()`) retain areas; costs and memory limits; prefetch described by minimum radius | 657 | P1 | MIRROR/workspace/streaming/techniques.md; streaming/index.md; Player.yaml; R20, R21 | undated | live-read |
| FC-40 | Frustum streaming: additive, per player; `Player.FrustumStreaming` server-set; activation lag; churn on fast camera; disabled by reduced draw distance; no occlusion culling | 659 | P1 | MIRROR/workspace/streaming/frustum.md; Player.yaml; MIRROR/_api-reference/enums/FrustumStreamingMode.yaml (hint); R22 | undated | live-read |
| FC-41 | `ContentProvider:PreloadAsync()` loads referenced assets, not whole-world residency; failures via final `AssetFetchStatus`; no throw | 661 | P1 | MIRROR/_api-reference/classes/ContentProvider.yaml; R23 | undated | live-read |
| FC-42 | `ScreenGui.ScreenInsets` options; `None` meant for noninteractive background-like content | 667 | P1 | MIRROR/_api-reference/classes/ScreenGui.yaml; R16 | undated | live-read |
| FC-43 | `PreferredTextSize` affects text; `TextScaled` bypasses it; constraints may cap | 667 | P1 | MIRROR/_api-reference/enums/PreferredTextSize.yaml; GuiService.yaml (grep); production/publishing/accessibility.md; R17 | undated | live-read |
| FC-44 | `ReducedMotionEnabled` expresses a reduce-UI-motion preference; docs do not say it disables custom 3D camera motion | 667 | P1 | GuiService.yaml (grep); production/publishing/accessibility.md; R17 | undated | live-read |
| FC-45 | Input Action System: `InputContext` `Enabled`, `Priority`, `Sink`; higher priority first; sink affects lower matching bindings | 669 | P1 | MIRROR/input/input-action-system.md; MIRROR/_api-reference/classes/InputContext.yaml; R18, R19 | undated | live-read |
| FC-46 | Moon Animator 2 xsixx listing: Plugin, `V36000`, updated 2026-08-19 | 675 | P1 | R26 live | 2026-08-19 | yes |
| FC-47 | Runtime freecam works in solo playtest (register quote: `Left Shift + P`) | 677 | P1 | MIRROR/workspace/camera/free-camera.md; MIRROR/production/publishing/thumbnails.md; R27 | undated | live-read |
| FC-48 | `VideoFrame`: max two videos at once; upload workflow has beta toggle and eligibility/asset restrictions | 677 | P1 | MIRROR/ui/video-frames.md; MIRROR/_api-reference/classes/VideoFrame.yaml; R28 | undated | live-read |
| FC-49 | Server is authoritative; client requests must be validated | 613 | P1 | MIRROR/projects/client-server.md; MIRROR/scripting/security/client-server-boundary.md; R24, R25 | undated | live-read |
| FC-50 | Disney layout and story process statements | 513, 515 | P3 | A09, A10 live | undated | live-read |
| FC-51 | Edmund Optics: angular-field geometry and first-order limits | 541 | P3 | B05 live | undated | live-read |

## 12. Contradictions and limits

### 12.1 Limits the paper itself states

| ID | FP | Limit | Handling for skills |
| --- | --- | --- | --- |
| X-01 | 511, 683-693, 707 | Nothing in the pipeline or contract was executed. All tests are proposed. | Say "proposed", never "tested". |
| X-02 | 531, 573, 575 | Sources are undated living pages read 2026-10-21; B06/B07 use mutable "latest" URLs; B02-B04, B08 are localized pages with English text; B10, B13, B14 are staging mirrors. | Re-read the en/5.2 page before stating a menu name or property. |
| X-03 | 531, 619, 631, 613, 629, 659 | Inside VERIFIED paragraphs the paper adds its own advice or inference (BL-02, RT-05, RT-11, RT-20, RT-23, RT-47). | Treat as PROC or INFER, not documented fact. |
| X-04 | 559, 565, 575 | Maths is derived. Smoothstep is not Blender's default and says nothing about feel. The basis-conversion algebra is not a verified Roblox import feature, and no axis map is given. | Do not state a Blender-to-Roblox axis map from this note. |
| X-05 | 619, 697 | The overview's shorthand on FOV direction differs from the API wording; use the API's vertical-angle definition plus the mode's invariant-axis rule. The paper writes the property as `FOVMode` at FP:697 but `FieldOfViewMode` at FP:619. | Use `FieldOfViewMode` (the API and enum name at FP:619, FP:1715). |
| X-06 | 637, 639, 697 | Mixer clock and server time are different clocks with different guarantees; cross-client audio timing is UNKNOWN; the clock contract is not a demonstrated multiplayer solution. | Claim no cross-client sync accuracy. |
| X-07 | 631, 697 | `Animation Graphs` base release and the State Machine / Expression beta differ in status; the beta runs only in Studio per the paper's reading of its FAQ. | Check the deployment path before using beta nodes. |
| X-08 | 641, 643 | Disabling emission is not clearing. A text timestamp cannot prove cue-to-impact sync. | Verify by frame capture. |
| X-09 | 647-653 | Documentation sets no universal light count, phone budget, FPS target, camera-speed ceiling or shot-length limit. | Leave these as measured, per-device decisions. |
| X-10 | 659 | Frustum streaming: no occlusion culling; no reduction of the normal workload; may churn on rapid moves. | Do not rely on it for whip pans. |
| X-11 | 661 | `PreloadAsync` does not mean the world is resident, and a returned call does not mean assets loaded. | Test asset failure separately. |
| X-12 | 667 | `ReducedMotionEnabled` is a UI-motion preference; docs do not say it changes 3D camera motion. | Offer a separate reduced-camera variant. |
| X-13 | 675 | A plugin listing verifies a maintained listing, not exporter reliability. | Validate one export before relying on it. |
| X-14 | 591, 593, 605 | ChatGPT Images claims are vendor capability claims; docs still list consistency and composition limits; no deterministic guarantee. | Review every panel; treat as proposals. |
| X-15 | 697 | No source gives a universal shot duration, skip delay, lens preset, phone budget or cross-client audio error. | Keep these as production tests. |

### 12.2 Gaps and tensions found by the extractor (not stated by the paper)

| ID | FP | Item | Handling for skills |
| --- | --- | --- | --- |
| X-16 | 1699-1931 | Several register quotes back only part of the paper's claim: R03 (vertical case only), R09 (beta, not the "Studio only" FAQ line), R10 (not the 0.6% or smoothing), R11/R12 (not the scheduled `atTime` playback), R14, R17 (generic; does not name `PreferredTextSize` or `ReducedMotionEnabled`), R19 (URL is the `Priority` property page; `Enabled` and `Sink` are not in the quote), R20/R21 (not `RequestStreamAroundAsync`), R26 (version only). | Check each named API against its own docs page. |
| X-17 | 667 | The paper names `PreferredTextSize` and `ReducedMotionEnabled` without saying which class holds them. | Do not state a class until checked (the mirror hints at GuiService.yaml, unverified). |
| X-18 | 663 | "Restore the prior frustum mode" implies a mode setting; the paper names only `Player.FrustumStreaming`. | Check its type and values. |
| X-19 | 677, 1909 | R27 points at the Thumbnails page for freecam. The mirror also has `workspace/camera/free-camera.md`. | Check both pages. |
| X-20 | 619 | `FieldOfViewMode` members `Diagonal` and `MaxAxis` come from the paper body only. | Verify the enum. |
| X-21 | 1567 | B04 shares B03's manual; the paper says combined direct quotes were restricted, so sensor-fit and projection text are paraphrased. | Re-read the camera manual page. |
| X-22 | 637 | Paper writes scheduled `Play`/`Stop` with an `atTime` argument but gives no signature. | Check parameter name and types in AudioPlayer.yaml. |
| X-23 | 509-707 | This note extracts only the paper's section 11 and 12 text. Other sections (lines 1-507, 709+) may hold related rules not seen here. | Do not treat this note as the whole paper. |

## 13. Line coverage

Every line of text in 509-707 is covered. Lines not turned into lesson rows:

| FP | Content | Reason |
| --- | --- | --- |
| 509, 609 | Section headings (11, 12) | heading only |
| 519, 597, 699 | Table header "Rule / Number / Evidence / Source and date" | header only; rows in N-01 to N-11 |
| 529, 537, 551, 567, 581, 589 | Subheadings in section 11 | heading only |
| 617, 627, 645, 655, 665, 673, 681, 695 | Subheadings in section 12 | heading only |

Line-to-row map: 511 SB-01; 513 SB-02; 515 SB-03; 517 SB-04 to SB-07; 521-525 SB-08, N-01 to N-03; 531 BL-01, BL-02; 533 BL-03; 535 BL-04; 539 BL-05, BL-06; 541 BL-07, BL-08; 543 BL-09; 545 BL-10; 547 BL-11, BL-12; 549 BL-13, BL-14; 553 BL-15; 555 BL-16; 557 BL-17; 559 BL-18 to BL-20; 561 BL-21; 563 BL-22; 565 BL-23 to BL-25; 569 BL-26; 571 BL-27; 573 BL-28, BL-29; 575 BL-30 to BL-32; 577 BL-33, BL-34; 579 BL-35; 583 BL-36; 585 BL-37; 587 BL-38; 591 IG-01; 593 IG-02, IG-03; 595 IG-04 to IG-06; 599-605 N-04 to N-07; 611 RT-01 to RT-03; 613 RT-04, RT-05; 615 RT-06 to RT-08; 619 RT-09 to RT-11; 621 RT-12, RT-13; 623 RT-14, RT-15; 625 RT-16, RT-17; 629 RT-18 to RT-20; 631 RT-21 to RT-23; 633 RT-24, RT-25; 635 RT-26, RT-27; 637 RT-28 to RT-30; 639 RT-31, RT-32; 641 RT-33; 643 RT-34, RT-35; 647 RT-36, RT-37; 649 RT-38, RT-39; 651 RT-40; 653 RT-41, RT-42; 657 RT-43, RT-44; 659 RT-45 to RT-47; 661 RT-48; 663 RT-49 to RT-51; 667 RT-52 to RT-54; 669 RT-55; 671 RT-56 to RT-58; 675 RT-59, RT-60; 677 RT-61 to RT-63; 679 RT-64; 683 TC-01 to TC-03; 685 TC-04; 687 TC-05; 689 TC-06; 691 TC-07; 693 CP-01 to CP-17; 697 EG-01 to EG-06; 701-707 N-08 to N-11.
