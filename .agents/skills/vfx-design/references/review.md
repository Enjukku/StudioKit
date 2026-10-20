> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-13

# Effect review

Use for every review of an existing or proposed effect. Run section B in order, label each check, fix in the
section D order, write notes in the section F format, diagnose with the M-ids in section G.
Evidence: `knowledge/reference/vfx/06-mistakes-08-card-09-review.md` (Output 6 = M-ids, Output 9 = steps R0-R14),
`contradictions.md` (X-, PD- rows), sources `00-sources.md` (R-ids). Tags: [study] [preprint] [practice] [spec]
[inference] [P] (P = PROPOSAL start value, untested, owner may change).

## A. What each input lets you check

Label every check **checked / inferred / not checkable from this input**. Never report a step as passed when
the input cannot show it. List what you could not check at the end of every review (RV-03).

| input | can check | cannot check (say so) |
| --- | --- | --- |
| Config / code / card values | Footprint number vs server radius (M-02); `LightInfluence`, `LightEmission` per layer (M-22, M-24); sheet size and layout (M-69); cells / Lifetime vs 60 FPS (M-71); `FlipbookStartRandom`, `FlipbookBlendFrames`, `FlipbookMode` (M-66, M-72, M-73); Rate x Lifetime live count; emitter, light, Highlight counts; `Shadows` on effect lights (M-81); blink and pulse rates; authored sound offset; which axes are random (M-56); visual + sound pair per break type (M-10); reduced-mode contents (M-89); shake axes (M-47); `Emit` scaled by quality (M-79); pooled reset code (M-80) | Any read (focus, value, clutter); real timing on device; output sync (M-62); GPU cost; how it looks on any stage |
| One screenshot | One dominant shape (blur the image); greyscale value separation (desaturate the image); hue count (M-25); max-luminance pixel on the damaging or rewarding part (M-13); pickup findable (M-54); hard line at a surface (M-68); luminance band UI > effect > characters > world (M-23); visible clutter count; cell px vs on-screen px if both resolutions are known (M-64) | Timing, onsets, contact frame, pops, loop seams, flash rate, repetition, sound, perf, other viewers, other stages, other quality levels. A screenshot is one moment: name the phase it shows |
| Frame sequence (stepped, fps known) | All screenshot checks per frame, plus: contact cell on the contact frame (M-03); punch inside the first 5 frames; pop in/out (M-67); staggered onsets and exit order (M-34); destroyed state vs flash (M-36); linger and see-through time (M-33, M-51); flash count per second and area (M-84); rapid hits merging (M-39); loop wrap (M-66); jittery shake (M-46) | Sound; server truth unless a debug overlay of the server shape or a tick log is in frame (M-01, M-05, M-06); perf; device latency. Unknown capture fps: count frames only, convert nothing |
| Video with audio | Frame-sequence checks (if it can be stepped), plus: muted vs unmuted read (M-63); sound transient vs punch frame (M-60, M-61); 1x feel after slow checks; repetition if it holds many triggers | Device output latency unless captured from the target phone (M-62); server truth without overlay; perf without a stats overlay; other quality tiers |
| Any input | — | Player tests, owner ratings, colour-blind testers (M-29), real low-end phone perf over 10-15 min (M-83), worst-case composite flash analysis (M-90). These need a test plan, not a claim |

## B. Review method (run in order)

| step | do | pass | fail -> fix (M-ids) | evidence |
| --- | --- | --- | --- | --- |
| R0 Card | Fill communication job, importance per viewer, gameplay truth | No null in those blocks | Get gameplay facts before art | R-283, R-368 [practice]; [inference] |
| R1 Block-in | Plain grey shapes, no glow or detail, real timing; record at 60 fps | Primary silhouette and phase order read without polish | Retime core or coarser asset (M-91) | R-115, R-340 [practice] (X-87) |
| R2 Truth overlay | Debug shape of the server area at contact and active end; self, ally, threatened, every quality tier | Edges coincide; visual contact = server contact; nothing hazard-coloured after active end | M-01..M-10 (rank 1) | R-060, R-080 [practice] |
| R3 Frame by frame | Step capture and a reference clip; log per-element timing | No pop or reversal; contact cell on contact frame; punch in first 5 frames | Change one responsible property, replay at 1x (M-03, M-32, M-36, M-67, M-73) | R-344, R-363 [practice, tier C]; [inference] |
| R4 Slow playback | `ParticleEmitter.TimeScale` 0.25 on all emitters or play capture at 0.25x; solo each layer | Windup, crescendo, punch, follow-through, dissipation deliberate and in order; onsets staggered | Retime core phase; re-check at 1x | R-211 [spec]; R-390 [practice, tier C] |
| R5 Greyscale | `ColorCorrectionEffect.Saturation = -1` on Camera; capture at punch and mid-dissipation on each stage | Focus is the highest-contrast patch; effect separates from stage; footprint edge reads | M-13, M-19, M-20 | R-184 [spec]; R-367, R-340 [practice]; step name [inference] |
| R6 Squint | `BlurEffect.Size` on Camera raised until fine detail is gone; record the value | One defined shape still reads | One dominant shape, cut detail (M-12, M-41, M-52) | R-181 [spec]; R-344 [practice, single tier C] |
| R7 Phone | Real phone at intended camera distance; Editor Quality Level lowest and highest | Identity and footprint read at real size and lowest quality | Coarser variant; cell size (M-16, M-64, M-65, M-74) | R-209, R-231 [spec] |
| R8 Many at once | Worst plausible concurrency with pickups, players, UI (T-05, T-10) | Local threat and nearest pickup still found; frame time in budget | Trim low-rank layers, residue, simultaneous onsets (M-49..M-54, M-57) | R-360, R-071 [practice] |
| R9 Bright / dark | Brightest, most saturated, darkest stage; inside dust | No background erases the primary | M-21..M-24, M-28 | R-300 [practice]; R-355 [practice, single tier C] |
| R10 Sound off, on | Muted read; then measure transient vs punch on a phone capture | Muted read passes; offset inside RV-T05 | Split readability fault from sync fault (M-60..M-63) | R-015 [practice]; R-073 [preprint]; R-170 [spec] |
| R11 Repetition | 100 triggers at 1/s, saved seed (T-17) | Meaning never changes; repeat not obvious to the owner | Vary decorative axes only (M-55, M-56) | R-386 [practice, tier C]; [inference] |
| R12 Comfort, safety | Reduced-effects on; count flashes and area on worst composite; shake off | Essentials kept; flash rule RV-T06 passes | Block release (M-84..M-90) | R-165, R-168 [spec]; R-074 [practice] |
| R13 Performance | Low-end phone, worst concurrency, 10-15 min; budget set before the test | Budget met all session | Keep footprint and onset; cut overlap and tails first (M-76..M-83) | R-231, R-200, R-198 [spec] |
| R14 Record | Before/after: same seed, camera, competing effects; log capture fps and display fps | Comparable evidence on the card | Re-capture | R-348 [practice]; [inference] |

## C. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| RV-01 | Run R0 before any art note. A review with null communication job, importance or gameplay truth stops at R0 and asks for the facts. | R-283, R-368 [practice] |
| RV-02 | Label every check gate-verified / MCP-verified / owner-confirmed / not verified, and per input as in section A. | AGENTS.md §2 |
| RV-03 | End every review with a "could not check" list naming the step, the missing input and the capture that would close it. | [inference] |
| RV-04 | Truth (R2, R3) is judged against server numbers or an overlay, never by eye. Indicator radius = config radius exactly; an offset needs an owner decision (C-03). | R-060, R-080 [practice]; R-336 [tier C] |
| RV-05 | Fix in the section D order. Do not write a rank 3-4 note while a rank 1 fault is open; list it as "after rank 1". | R-060 [practice] |
| RV-06 | Slow playback (R4) never proves feel: every retime is re-checked at 1x. | [inference] |
| RV-07 | Frames stay frames unless the capture fps is known. Convert only at the stated fps; default client cap is 60. | R-198 [spec] |
| RV-08 | Never fix a flat hit by raising intensity before truth, readability and timing pass. | R-101, R-043 [study]; R-005 [preprint] |
| RV-09 | Randomness may touch ornament only. Footprint, contact time, team colour and power rank are locked; compare range extremes. | R-043 [study]; [inference] |
| RV-10 | Review muted first. If the meaning needs sound, it is a readability fault (M-63), not a sync fault. | R-015 [practice] |
| RV-11 | Safety (R12) and performance (R13) block release at any rank. A warning screen or label is not a fix (M-87). | R-165 [spec]; R-396 [practice, tier C]; [inference] |
| RV-12 | Test flashes on the composite worst case, not one effect alone; record tool, standard and version. | R-155, R-016 [practice] |
| RV-13 | Judge in context: real stage, real camera distance, other players, debris and UI. A preview-only pass is "not verified". | R-355 [practice, tier C] |
| RV-14 | Perf is judged on a real low-end phone over 10-15 min; the emulator and short runs are "not verified". | R-231 [spec]; R-036 [practice] |
| RV-15 | Every note follows section F: one moment, one symptom with M-id, one concrete change, what it protects, the retest step. | R-344, R-348 [practice, tier C]; R-060 [practice] |
| RV-16 | Give a solution direction; the builder picks the final value. When the value is unknown, write "raise/lower until <step> passes (record value)". | R-348 [practice, tier C] |
| RV-17 | Change one phase at a time, replay at 1x, then move on. | [inference]; R-348 |
| RV-18 | Lab and standard numbers stay in evidence fields; project values carry [P] and a test (M-93). | R-101 [study]; [inference] |
| RV-19 | Read `ParticleFlipbookTextureCompatible` after load for every sheet; `NotCompatible` fails R7. | R-214, R-211 [spec] |
| RV-20 | Before/after captures share seed, camera and competing effects (R14), or the comparison is "not verified". | R-348 [practice]; [inference] |

### Tunable review thresholds

| ID | Value | default | range | move up when | move down when | hard cap | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RV-T01 | Capture fps | 60 [spec] | display fps | target display is faster | — | log it always | R-198; R1 |
| RV-T02 | Slow-playback `TimeScale` | 0.25 [inference] | 0..1 [spec] | — | phases still blur together at 0.25 | 0..1 | R-211; 09 R4 |
| RV-T03 | Punch window from contact | first 5 frames [practice, tier C] | brightest layer 1-2 f; flash stack 2-3 f (fps not stated) | — | — | no number found | R-344, R-387, R-388; C-08 |
| RV-T04 | Flash sprite | peak 2 f@60 (33 ms) inside Lifetime 0.05-0.1 s [P] | 1, 2, 6 f test | owner rates "no punch" | flash count fails | RV-T06 | PD-01; T-09 |
| RV-T05 | Sound offset vs punch frame | sound 0-40 ms late [P] | -3..+3 f at 60 test | — | — | never >1 f (16.7 ms) early | PD-14; R-070 [study], R-169, R-170 [spec]; T-07 |
| RV-T06 | Large-area flashes | design target 2/s [P] | 1-3/s | — | — | 3/s or 0.006 sr in any 10° field [spec]; leading edges ≥334 ms at 60 Hz pass | PD-11; R-165, R-168; X-44 |
| RV-T07 | Red / danger pulse | lasting zones steady or ≤1 Hz; countdown 1 -> 2 -> 3 Hz; low health 1 Hz [P] | tests to 2 Hz | — | — | never >3 Hz at full contrast; R/(R+G+B) ≥0.8 is a red trigger [spec] | PD-12, PD-13; R-165; T-22 |
| RV-T08 | Telegraph lead | 600 ms one direction; 1000 ms 2-4 safe spots [P] | 400/600/800/1200 ms test | misses on 30 fps phones | owner says "slow" | floor 0.25 s, one stimulus only [practice]; simple RT 230.8 ms [study] | PD-07; X-56; R-130, R-373; T-01 |
| RV-T09 | See-through time of sight-blocking dust | 2 s; impact dust 1.5-3 s; big clouds ≤5 s [P] | T-12 grid | owner says "too light" | target unreadable | nothing over 8 s in play areas [P] | PD-16; C-09; R-031 |
| RV-T10 | Simultaneously relevant effects per player | 4 [P] | 2/4/8/16 test | — | find time rises | no number found | M-49; R-139, R-145 [study, not effect studies]; T-05 |
| RV-T11 | Others' non-threat effects | `LocalTransparencyModifier` 0.5; no shake, flash or post effect [P] | 100/70/40/0% test | local threat or pickup still missed (more transparent) | owner says ally effects feel dead |  threats and pickups always full | PD-08; C-14; T-06 |
| RV-T12 | Full-detail blasts per client | 4; emitters per type recipe, live ≤~1000, textures reused (v2, SKILL.md §4) | 1/5/20 test | — | frame budget fails | 400/s per emitter, 100/s mobile is a cap, not a budget [spec] | PD-10; R-209; T-10 |
| RV-T13 | Live Highlights per client | 20 [P] | 10/20/50 test | — | mobile GPU cost | 255 [spec] | PD-09; R-196 |
| RV-T14 | Repetition run | 100 triggers at 1/s [inference] | variants 1/3/6; spread 0/10/25% test | — | — | variant count: no number found | 09 R11; T-17 |
| RV-T15 | Perf session | 10-15 min [practice] | — | thermal effects suspected | — | low-end = Android <2 GB [practice] | R-231, R-036; T-10 |
| RV-T16 | Squint `BlurEffect.Size` | no number found (record the value used) | — | — | — | — | R-181 [spec]; R-344 |
| RV-T17 | Hit-stop | weapon 50/100/150 ms light/heavy/crit; explosions 0 [P] | T-15 | owner says "weightless" | "lag" reports | pleasant/unpleasant boundary about 0.54-0.55 s, one VR game [study] | PD-02; R-035; C-02 unresolved |
| RV-T18 | Shake | rotation only, t³, +0.2/+0.5, max 3°, decay 1.0/s [P] | 1/3/6° test | — | comfort fails | no translation in 3D [practice] | PD-03; R-124; T-14 |

## D. Ranked fix order

| rank | area | gate before moving on | M-ids | evidence |
| --- | --- | --- | --- | --- |
| 1 | Truth of area and timing | R2, R3 pass: edges match, visual contact = server contact, no lingering hazard, telegraph ≥ RV-T08 | M-01..M-10 | R-060 [practice] |
| 2 | Right message at right importance | Viewers name event and consequence; importance order = prominence order; miss, hit, big hit distinct | M-11..M-18 | R-080, R-368 [practice]; R-043 [study] |
| 3 | Visibility, clutter, brightness | R5-R9 pass | M-19..M-30, M-49..M-54 | R-060 [practice] |
| 4 | Theme and polish | Re-run R2, R5, R8: theme breaks nothing above | rest | R-060 [practice] |
| gate | Safety and performance | Block release at any rank | M-76..M-90 | [inference] |

Riot publishes 3 tiers (accuracy; readability, noise, brightness; theme). The rank 2 / rank 3 split is ours [inference].

## E. Release gate (all pass)

| check | pass | step |
| --- | --- | --- |
| truth | footprint and contact match in every variant | R2 |
| importance | prominence order = card importance order | R0, R8 |
| readability | greyscale, squint, phone, bright/dark | R5-R7, R9 |
| sound | muted read passes; measured offset inside RV-T05 | R10 |
| safety | RV-T06 on the composite; reduced mode keeps footprint, outcome, pickups | R12 |
| performance | budget met on low-end phone 10-15 min | R13 |
| owner | every [P] listed; owner confirmation in `decisions.md` before the label goes | AGENTS.md §0 |

## F. Feedback format

One note = one moment, one symptom, one change. Numbered, highest rank first. Builder replies with what changed
and a new capture (R-344). Fields in order:

| rank | moment (phase, time or frame, viewer) | symptom + M-id | probable cause (layer.property) | change (`layer.property: from -> to` or "raise/lower until <step> passes") | protects | retest |
| --- | --- | --- | --- | --- | --- | --- |

Example (heavy charge on a block wall, card 8.3):

| # | rank | moment | symptom | probable cause | change | protects | retest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | punch, t = 1500 ms, frames 0-12, self | M-01: L6 dust ring stops past the debug sphere; blocks outside stay intact | L6 speed too high for its drag | Raise L6 drag until the stop line sits on `area_size_studs` (record value) | L4 timing, L1 size | R2 |
| 2 | 1 | punch, frames 0-3, self | M-03: L4 peaks frames after the detonate transient | built L4 offset differs from card | L4 `start_offset_ms`: built -> 0; re-measure | sound event, L5a timing | R3, R10 |
| 3 | 3 | dissipation, 2050-4550 ms, ally | M-51 / M-09: L8 hides the hole and loose blocks all tail | L8 lifetime too long | L8 `lifetime_s`: 2.0-3.0 -> 1.0-1.5, then T-12 | L6, L7 | R8, R9 |

Work order: note 1, re-shoot; note 2, re-shoot; then note 3. Bad note: "make it pop" (M-94).

## G. Mistakes (symptom -> cause -> spot -> fix -> M-id)

| group | symptom | cause | how to spot | fix | M |
| --- | --- | --- | --- | --- | --- |
| Truth | Edge of ring/flash/dust ≠ server area | art sized by eye; variant differs | server sphere overlay at contact and active end, every variant | match footprint in all variants; decoration never past it | 01, 02 |
| Truth | Hit reads late or soft | visual peak not on contact frame; windup on an instant event | log contact, first bright frame, transient | retime art, never the gameplay hit; start instant events at peak | 03, 04 |
| Truth | Players avoid a safe area / misjudge escape | hazard look outlives active end; fuse not server-driven | step to last active tick; 20 fuse runs vs server time | end hazard cue on the tick; drive fuse from server timer | 05, 06 |
| Truth | Unavoidable hit | telegraph < reaction + render | count frames first change -> damage | lengthen windup; add channels (RV-T08) | 07 |
| Truth | Hit drawn in wrong place | latency | Network Simulation, moving target | spawn locally on hit event, attach, reconcile | 08 |
| Truth | Hole and loose blocks unreadable; break visual without sound | dust over change; no paired record | pause at dissipation +1 s; data gate {visual, sound} | server-confirmed breaks only; dust clears hole first; one record per break type | 09, 10 |
| Message | Everything looks top-tier; no focus | prominence not ranked; no dominant shape | side-by-side tiers; freeze + blur | trim ordinary peaks; one primary shape | 11, 12 |
| Message | Eye follows trail, not head; own launch outshines threats | extremes on decoration | max-luminance pixel; "what did the muzzle flash look like?" | extremes on the damaging part; own cues below threat | 13, 14 |
| Message | Big swing, weak result; miss = hit | feedback on action, not outcome | compare miss/hit/big hit muted | big cue only on confirmed success; distinct outcomes | 15, 18 |
| Message | Fine in preview, lost in play; blinds others | judged alone, caster view only | real stage; target and bystander cameras | bolder value; per-viewer variant | 16, 17 |
| Value | Sinks or blows out; vanishes on some stages | 0/100% value; same value as stage | greyscale per stage | mid-value base, extremes for top-tier focus (C-04); value first | 19, 20 |
| Value | Glow wash; smoke vanishes on bright stage | low `BloomEffect.Threshold`; additive smoke | Bloom on/off; bright stage greyscale | raise Threshold, never pulse Bloom; `LightEmission` 0 for mass | 21, 22 |
| Value | Covers UI or weaker than characters; black on dark stage | wrong value band; `LightInfluence` default | luminance samples; darkest stage | UI > effect > characters; set `LightInfluence` in data | 23, 24 |
| Colour | Noise; meaning breaks | competing hues; one hue, two meanings | count full-saturation hues; colour-meaning table | 1 dominant + 1 secondary; one colour per category | 25, 26 |
| Colour | Colour-blind players miss it | colour only signal; simulator as proof | simulator + greyscale, real testers | add shape, pattern, motion; configurable | 27, 29 |
| Colour | Lost in a same-hue scene; cheap light | stage hue match; saturated orange | over most saturated area; lit scene | complementary secondary; desaturate light | 28, 30 |
| Timing | Mechanical; no punch | linear curves; dim or long flash | plot curves; step first 5 frames | ease with keypoints (≤20); RV-T04 | 31, 32 |
| Timing | Lingers, blocks next effect | late main action, long tail | count live particles 1 s after beat | dissipate early (first-quarter heuristic, C-05); RV-T09 | 33, 35 |
| Timing | One mass, no follow-through | all layers start/end together | solo layers | offset secondary starts ~2-3 f; ~150 ms separation [study] | 34 |
| Timing | Object vanishes before blast reads | detach before flash | step detach vs flash peak | swap at flash peak | 36 |
| Timing | Lag feel; flat weight; hits merge | hit-stop too long/uniform; impacts <5 f apart at 30 fps | many-at-once; light vs heavy; onset gaps | RV-T17; scale with strength; own flash per impact | 37, 38, 39 |
| Timing | Toy vs building scale wrong | dust speed vs scale | "toy or building?" (T-13) | decide scale; dust `TimeScale` 0.6 [P] (PD-17) | 40 |
| Compose | Muddy; fake even burst; blob sparks | jobless layers; spherical spawn; big sparks | mute each layer; zoom still | named job per layer; clumped cones; thin `VelocityParallel` streaks | 41, 42, 43 |
| Compose | Eye in wrong place; card switched off | windup away from payoff; plain fade | mark positions; watch tail | anticipation on payoff spot; break shape up | 44, 45 |
| Camera | Jitter; view through walls; numb shake | random offsets; translation; shake on all | 0.25x; near walls; shakes/min | RV-T18; big events only | 46, 47 |
| Camera | Effect steals control or sight | camera/screen layer | aim and move during it | reduce; per-effect off switch | 48 |
| Clutter | Threat or pickup not found | too many effects; others at full | 2/4/8/16 + pickup; 8 players | RV-T10, RV-T11; trim low rank first | 49, 50 |
| Clutter | Targets hidden; busy noise | lingering dust; needless detail; saturated ambient | target behind cloud; remove detail; saturation histogram | RV-T09; cut detail; colour for combat | 51, 52, 53 |
| Clutter | Pickups lost in debris | value below effects | stand in cloud | pickups above effects; `Highlight` within RV-T13 | 54 |
| Repeat | Repeat noticed; meaning shifts | identical playback; random core | RV-T14; range extremes | vary ornament (Rotation 0-360, size, lifetime, start cell) | 55, 56 |
| Repeat | Frame overload; covered impact; frequent flourish drags | no cap; escalation over contact; long frequent anim | worst concurrent copies; top tier screenshot; time 20 repeats | budget by max copies, drop by tier; escalate at edges; 100 ms frequent, 500 ms drags [practice] | 57, 58, 59 |
| Sync | Sound early or incoherent; gap on device | scheduling; authored timestamps trusted | phone capture, frame-step transient | RV-T05; one sound per landmark; measure on hardware, constant delay | 60, 61, 62 |
| Sync | Meaning lost muted | picture relies on sound | review muted | picture carries meaning | 63 |
| Flipbook | Blurry or shimmering sprite | cell px < screen px; texture too big for tiny bit | cell px vs screen px (1024: 2x2=512, 4x4=256, 8x8=128) | fewer cells or smaller on screen; plain textures for tiny bits | 64, 65 |
| Flipbook | Seam, pop, hard line | wrong `FlipbookMode`; no fade; card hits geometry | 3 loops; first/last frames; low angle | `OneShot` for events; fade Transparency; `ZOffset`, fade near contact | 66, 67, 68 |
| Flipbook | Static texture; bleeding; skipped cells | sheet not 1024 or not a grid multiple; no spacing; cells/Lifetime > 60 | RV-19; zoom cell edges; compute cells/s | 1024x1024 exact multiple (C-01); spacing; fewer cells or longer life | 69, 70, 71 |
| Flipbook | Ghosting or stutter; onset skipped | wrong `FlipbookBlendFrames`; `FlipbookStartRandom` on | step frames; first meaningful cell | blend off for stepped, on for slow smoke; random start off for one-shots | 72, 73 |
| Flipbook | Effect disappears on old phones; tint flat | many unique sheets; colour baked | count sheet ids; tint to 3 colours | reuse sheets, static fallback; neutral grey + `LightEmission` 1 | 74, 75 |
| Perf | GPU spikes | cap used as budget; overdraw | `Stats.RenderGPUFrameTime` low-end phone | budget by area x overlap x concurrency; fewer, smaller sprites | 76, 77 |
| Perf | Draw calls; bursts ignore quality; stale pooled bits | many emitters; per-frame property changes; `Emit` unscaled; no reset | Debug Stats; Emit 200 at Q1 vs Q10; reacquire fast | bake templates; scale `Emit` by `SavedQualityLevel`; `Clear()` and reset | 78, 79, 80 |
| Perf | Extra calls; drops; false pass | shadowed effect lights; uncapped debris, off-screen spawns; emulator | count lights, bodies; test log | `Shadows = false`; cap and cull; RV-14 | 81, 82, 83 |
| Safety | Seizure risk | >3 flashes/s large area; red pulse; area misread | count luminance pairs ≥10%/s and area on composite | RV-T06, RV-T07; count post-effect pulses | 84, 85, 86 |
| Safety | Unfixed risk shipped; discomfort; reduced mode blind | label instead of fix; no off switch; reduced mode deletes warnings | settings list; reduced mode muted | redesign; separate shake/flash/full-screen/density controls; keep essentials | 87, 88, 89 |
| Safety | False confidence | one analyser pass, one effect | test log | composite worst case; record tool and version | 90 |
| Process | Weak read hidden; flat hit pumped | polish before block-in; intensity first | grey swap; truth/readability check first | RV-08; block-in first | 91, 92 |
| Process | Lab number as default; vague notes | evidence in value fields; "make it pop" | each number shows source; note has moment/symptom/change | RV-18; section F | 93, 94 |

## H. Unsettled evidence

| item | status |
| --- | --- |
| M-85 says WCAG proxy 341x256 = 11.1% of a 1024x768 screen; X-44 resolves to ≈21,824 px ≈2.8% (06 not fixed at integration) | This file follows X-44; WCAG glossary re-read open (07 O-6) |
| Squint blur size | no number found; record the value used (RV-T16) |
| Flipbook sizes other than 1024 (C-01) | unresolved; T-18 |
| Hit-stop frame counts (C-02, X-01) | unresolved; no ms conversion |
| "Main action in first quarter of lifetime" (C-05, X-32) | single tier C heuristic; review check only (T-19) |
| Rank 2 / 3 split | not Riot wording [inference] |
