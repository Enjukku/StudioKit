> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-13. Rebuilt by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (inputs per check, the self-review lines by pass in §I, the blocking pass and the value and silhouette gates). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): PL-08.

# Effect review and self-review

Use for every review of an existing or proposed effect, and as your own self-review before every hand-back: §I holds the lines per pass. Run section B in order, label each check, fix in the section D order, write notes in the section F format, diagnose with the M-ids in section G.
Evidence: `knowledge/reference/vfx/06-mistakes-08-card-09-review.md` (Output 6 = M-ids, Output 9 = steps R0-R14),
`contradictions.md` (X-, PD- rows), sources `00-sources.md` (R-ids). Tags: [study] [preprint] [practice] [spec]
[inference] [P] (P = PROPOSAL start value, untested, owner may change).

## A. What each input lets you check

Label every check **checked / inferred / not checkable from this input**. Never report a step as passed when
the input cannot show it. List what you could not check at the end of every review (RV-03).
**Input codes used in §I:** S = spec numbers (`spec.json`, the frame script, the read card, arithmetic); M = clip numbers (`metrics.json` from `tools/vfx/clip_metrics.py` on a fixed-camera frame folder, `vfx-craft/references/measure.md` §2); K = key stills from that folder measured with the effect mask (`measure.md` §3); R = Blender renders of mesh shapes (`measure.md` §4); C = Studio MCP stills; D = a capture on the target device with audio (owner or studio-operator); O = the owner on a playable preview at a named gate; log = Output lines.

| input | can check | cannot check (say so) |
| --- | --- | --- |
| Config / code / card / spec values (S) | Footprint number vs server radius (M-02); `LightInfluence`, `LightEmission` per layer (M-22, M-24); sheet size and layout (M-69); cells / Lifetime vs 60 FPS (M-71); `FlipbookStartRandom`, `FlipbookBlendFrames`, `FlipbookMode` (M-66, M-72, M-73); Rate x Lifetime live count; emitter, light, Highlight counts; `Shadows` on effect lights (M-81); blink and pulse rates; authored sound offset; which axes are random (M-56); visual + sound pair per break type (M-10); reduced-mode contents (M-89); shake axes (M-47); `Emit` scaled by quality (M-79); pooled reset code (M-80); layer rank order; curve shapes (fast in, fades) | Any read (focus, value, clutter); real timing on device; output sync (M-62); GPU cost; how it looks on any stage |
| One still (K or C) | One dominant shape (black-fill at phone size); grayscale value separation (the luminance image); hue count (M-25); max-luminance pixel on the damaging or rewarding part (M-13); pickup findable (M-54); hard line at a surface (M-68); luminance band UI > effect > characters > world (M-23); visible clutter count; cell px vs on-screen px if both resolutions are known (M-64) | Timing, onsets, contact frame, pops, loop seams, flash rate, repetition, sound, perf, other viewers, other stages, other quality levels. A still is one moment: name the phase it shows |
| Frame folder at a known fps (M + K) | All still checks per frame, plus: contact cell on the contact frame (M-03); build rising; punch inside the first 5 frames; one peak; fast in, slow out; pop in/out (M-67); staggered onsets and exit order (M-34); destroyed state vs flash (M-36); linger and see-through time (M-33, M-51); flash count per second and area (M-84); rapid hits merging (M-39); loop wrap (M-66); jittery shake (M-46) | Sound; server truth unless a debug overlay of the server shape or a tick log is in frame (M-01, M-05, M-06); perf; device latency. Unknown capture fps: count frames only, convert nothing. Studio MCP stills are not a frame folder: particles may not update between them |
| Device capture with audio (D) | Frame-folder checks (if it can be stepped), plus: muted vs unmuted read (M-63); sound transient vs punch frame (M-60, M-61); 1x feel after slow checks; repetition if it holds many triggers | Server truth without overlay; perf without a stats overlay; other quality tiers |
| Any input | — | Player tests, owner ratings, colour-blind testers (M-29), real low-end phone perf over 10-15 min (M-83), worst-case composite flash analysis (M-90). These need a test plan, not a claim |

## B. Review method (run in order; the lines are in §I)

| step | do | input | pass | fail -> fix (M-ids) | evidence |
| --- | --- | --- | --- | --- | --- |
| R0 Card | Read card filled: communication job, importance per viewer, gameplay truth (§I1) | S | No null in those blocks | Get gameplay facts before art | R-283, R-368 [practice]; [inference] |
| R1 Block-in | Placeholder sprites, no glow or detail, real sizes and timing; frame folder at a known fps (§I2) | M, K | Primary silhouette and phase order read without polish | Retime core or coarser asset (M-91) | R-115, R-340 [practice] (X-87) |
| R2 Truth overlay | Debug shape of the server area at warning, contact and active end; self, ally, threatened, every quality tier (IG-04) | C, log | Edges coincide; visual contact = server contact; nothing hazard-coloured after active end | M-01..M-10 (rank 1) | R-060, R-080 [practice] |
| R3 Frame by frame | Step the frame folder and a reference frame script; log per-element timing (BL-02 to BL-08) | M, K | No pop or reversal; contact cell on contact frame; punch in first 5 frames | Change one responsible property, replay at 1x (M-03, M-32, M-36, M-67, M-73) | R-344, R-363 [practice, tier C]; [inference] |
| R4 Slow playback | `ParticleEmitter.TimeScale` 0.25 on all emitters or the rows read one by one; solo each layer | M | Windup, crescendo, punch, follow-through, dissipation deliberate and in order; onsets staggered | Retime core phase; re-check at 1x (owner preview) | R-211 [spec]; R-390 [practice, tier C] |
| R5 Greyscale | The luminance image of each key still with the effect mask (`look_check.py value`); in Studio `ColorCorrectionEffect.Saturation = -1` under the Camera gives the same view (VS-01, VS-04) | K, C | Focus is the highest-contrast patch; effect separates from stage; footprint edge reads | M-13, M-19, M-20 | R-184 [spec]; R-367, R-340 [practice]; step name [inference] |
| R6 Squint | The key stills at the phone viewport (`look_check.py thumb --size`), black-fill and value re-run small (VS-05) | K | One defined shape still reads | One dominant shape, cut detail (M-12, M-41, M-52) | R-181 [spec]; R-344 [practice, single tier C] |
| R7 Phone | Phone-viewport capture at the intended camera distance; Editor Quality Level lowest and highest (IG-13); the owner's device when the brief asks | C, O | Identity and footprint read at real size and lowest quality | Coarser variant; cell size (M-16, M-64, M-65, M-74) | R-209, R-231 [spec] |
| R8 Many at once | Worst plausible concurrency with pickups, players, UI (IG-01 to IG-03) | C | Local threat and nearest pickup still found; frame time in budget | Trim low-rank layers, residue, simultaneous onsets (M-49..M-54, M-57) | R-360, R-071 [practice] |
| R9 Bright / dark | Brightest, most saturated, darkest stage; inside dust (IG-13, CP-01) | C, K | No background erases the primary | M-21..M-24, M-28 | R-300 [practice]; R-355 [practice, single tier C] |
| R10 Sound off, on | Muted read; then transient vs punch on a device capture (IG-12, IG-16) | C, D | Muted read passes; offset inside RV-T05 | Split readability fault from sync fault (M-60..M-63) | R-015 [practice]; R-073 [preprint]; R-170 [spec] |
| R11 Repetition | 100 triggers at 1/s and a burst, saved seed (IG-09) | C, log, O | Meaning never changes; repeat not obvious to the owner | Vary decorative axes only (M-55, M-56) | R-386 [practice, tier C]; [inference] |
| R12 Comfort, safety | Reduced-effects on; count flashes and area on the worst composite; shake off (IG-06, IG-07) | C, M | Essentials kept; flash rule RV-T06 passes | Block release (M-84..M-90) | R-165, R-168 [spec]; R-074 [practice] |
| R13 Performance | Low-end phone, worst concurrency, 10-15 min; budget set before the test (`performance` skill) | owner or performance run | Budget met all session | Keep footprint and onset; cut overlap and tails first (M-76..M-83) | R-231, R-200, R-198 [spec] |
| R14 Record | Before/after: same seed, camera, competing effects; log capture fps and display fps | M, K | Comparable evidence on the card | Re-capture | R-348 [practice]; [inference] |

## C. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| RV-01 | Run R0 before any art note. A review with null communication job, importance or gameplay truth stops at R0 and asks for the facts. | R-283, R-368 [practice] |
| RV-02 | Label every check gate-verified / MCP-verified / owner-confirmed / not verified, and per input as in section A. | AGENTS.md §2 |
| RV-03 | End every review with a "could not check" list naming the step, the missing input and the capture that would close it. | [inference] |
| RV-04 | Truth (R2, R3) is judged against server numbers or an overlay, never by eye. Indicator radius = config radius exactly; an offset needs an owner decision (C-03). | R-060, R-080 [practice]; R-336 [tier C] |
| RV-05 | Fix in the section D order. Do not write a rank 3-4 note while a rank 1 fault is open; list it as "after rank 1". | R-060 [practice] |
| RV-06 | Slow playback (R4) never proves feel: every retime is re-checked at 1x, and feel at 1x is the owner's call on a playable preview. | [inference] |
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
| RV-17 | Change one phase at a time, replay at 1x, then move on: one named problem per pass, the worst first. | [inference]; R-348 |
| RV-18 | Lab and standard numbers stay in evidence fields; project values carry [P] and a test (M-93). | R-101 [study]; [inference] |
| RV-19 | Read `ParticleFlipbookTextureCompatible` after load for every sheet; `NotCompatible` fails R7. | R-214, R-211 [spec] |
| RV-20 | Before/after captures share seed, camera and competing effects (R14), or the comparison is "not verified". | R-348 [practice]; [inference] |
| RV-21 | Ask goal questions, never "do you like it?": "which tells the threatened player where it hurts at phone size?". A note that carries a solution ("make it bigger") hides a problem ("it reads weak"): restate the problem and solve that, then re-check the problem, not only the change. Say whether a note is about the goal or the tactic. | [practice] |
| RV-22 | Visual notes are marked captures (a paint-over or a marked still from `reference-images`), before and after, not words alone. For your own work, look again with fresh eyes: the mirrored still and the luminance image at each check-in. | [practice] |

### Tunable review thresholds

| ID | Value | default | range | move up when | move down when | hard cap | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RV-T01 | Capture fps | 30 for frame folders (stated in the folder); 60 [spec] for device clips | display fps | target display is faster | — | log it always | R-198; R1 |
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
| RV-T16 | Squint size | the smallest phone viewport from the game profile (`thumb --size`); a `BlurEffect.Size` used in Studio is recorded | — | — | — | — | R-181 [spec]; R-344 |
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

Studio practice publishes three tiers (accuracy; readability, noise, brightness; theme). The rank 2 / rank 3 split is ours [inference].

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

Work order: note 1, re-shoot; note 2, re-shoot; then note 3. Bad note: "make it pop" (M-94). The hand-back maps every note received to done or questioned (with the reason) and names at least one honest weakness with its next step.

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
| Value | Sinks or blows out; vanishes on some stages | 0/100% value; same value as stage; additive layers stacked at the core | greyscale per stage; near-white rows (`bright_pct`) | mid-value base, extremes for top-tier focus (C-04); value first; count additive stacks; a saturated halo behind the core | 19, 20 |
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
| Timing | Build pops in at full size, or fades before the hit | no rising build; build lifetime too short | build rows: coverage and peak luminance rise to the peak | grow size and brightness and ramp the rate toward the release; start the build earlier | 95 |
| Compose | Eye stays on the old spot after the hit | build layers keep spawning and stay bright | rows after the peak: the bright centre does not move | stop the build at the hit, darken it, light the result | 96 |
| Clutter | Effect hides other players, benches, targets | placed high or tall over characters | box top against the height line; effect mask against the information-area boxes (`vfx-craft/references/measure.md` §3) | keep it low and inside the footprint; lower the height | 97 |
| Value | Mass looks like flat cards, or popcorns | spread sprites with gaps; shrink-only exits; one recoloured layer | black-fill holes; births and deaths in two stills | overlap with larger size before more count; fade in and out; shared colours | 98 |

## H. Unsettled evidence

| item | status |
| --- | --- |
| M-85 says WCAG proxy 341x256 = 11.1% of a 1024x768 screen; X-44 resolves to ≈21,824 px ≈2.8% (06 not fixed at integration) | This file follows X-44; WCAG glossary re-read open (07 O-6) |
| Squint blur size | phone-viewport thumbnail is the default; record any blur value used (RV-T16) |
| Flipbook sizes other than 1024 (C-01) | unresolved; T-18 |
| Hit-stop frame counts (C-02, X-01) | unresolved; no ms conversion |
| "Main action in first quarter of lifetime" (C-05, X-32) | single tier C heuristic; review check only (T-19) |
| Rank 2 / 3 split | ours [inference] |
| "70-80 % of the size in the first 20-25 % of the burst" (BL-04) | starting value from practice; bracket it per effect type |

## I. Self-review lines by pass

Run the lines of the pass you are at before its hand-off or check-in; write each as PASS, FAIL, MEASURED, not verified or n/a (with the reason), with its evidence. A line passes or fails only against a tolerance (the read card's tier caps, the brief, the owner); without one it is MEASURED. **A fresh read:** write what you read from a still or a black-fill before you open the brief, the effect name or your notes, then compare; at the check-in the reviewer repeats it blind. For a second look, mirror the still. How to measure each line: `vfx-craft/references/measure.md`.

**Image budget (light checks, owner J005-D8):** numbers for every effect (spec arithmetic, clip rows, curve shapes). Stills only for a failing number plus at most 4 key stills per pass (build, peak, result, tail), each measured with the effect mask; the in-game pass at most 8 Studio stills per effect plus one grayscale and one reduced; two-client pairs only for effects with per-viewer variants. Options and brackets: text and numbers first; images only for the deciding frames (at most 1 per bracket value) and at most 1 `vfx` sheet per option shown at direction. Report renders, captures and stills made and looked at.

### I1. Plan (before the first layer)
| ID | Look for | In |
| --- | --- | --- |
| PL-01 | The read card quotes the direction sheet's target-experience line and has job, verb, the three read lines (shape, colour role, timing) and the three reads with the focus point; stage names and event ids equal the timeline's, so every visible stage has its cue on the sound card | S |
| PL-02 | Importance per viewer (self, other, threatened), the tier and its caps (footprint, near-white, visible length, camera channels); what it outranks and yields to | S |
| PL-03 | Each truth value names its data field; "visual only" has no radius ring; the danger signal ends on the last tick; a hazard's look matches its written rule (kill or damage, duration, end) on the hazard sheet | S |
| PL-04 | Information areas listed with the maximum height; at the frame script's peak the screen-math box stays below and outside them | S |
| PL-05 | Rate and burst written; frequent effects have a merge window, a live-copy cap and particles per copy | S |
| PL-06 | Per-viewer and reduced variants: every intense channel has an off path that keeps footprint, contact, outcome, threats and pickups; colour is paired with shape | S |
| PL-07 | Budget line, stop criteria and pass budget, dated before the first spec | S |
| PL-08 | Research: one observed property of the real phenomenon (or one method from the outside field the target-experience sentence points to) named and used; 1-3 pro frame scripts read (peak %, peak ms, tail); the reuse search result named (recoloured or retimed, or new and why) | job record |
| PL-09 | Options: 2-3 at equal finish, each with a hook from a different source, one atypical, the first labelled warm-up; each names the read it solves and its cost (budget line); an option outside the game's tone words is dropped; picked by a goal question; a reason per losing option; merges named | job record |
| PL-10 | Frame script at the game camera with the screen-size math (height % and area % at the game distance; projectiles at launch and impact), compared with ≥1 pro frame script: peak coverage, peak ms, tail ms side by side | S |
| PL-11 | The frame script tells a beginning, a middle and an end: tell or build → beat → one peak row on the contact event → result rows after their cause → tail; the gaps between the main beats are not all equal; exits are staggered (glow, flare, sparks, embers and smoke last) | S |
| PL-12 | Colour: one main hue (with lighter and darker versions) and at most one role accent; next to the caster's hue; no reserved colour as decoration; no hue with two meanings in the game's effect list. Shape: when the art bible names a motif, it shows in the effect's shapes at more than one scale | S |
| PL-13 | Variants (skins, tiers, re-themes): footprint (the radius from the same data field; at the same camera and ms, area and box within the `measure.md` §3 tolerance), shape (aligned IoU), contact time, tell and shape code equal the base; the ability is re-themed (shapes, motif), not only recoloured; the caster's anchors stay unhidden at held moments; a cosmetic effect (skin, trail, aura, pet) stays below combat effects in brightness and footprint, so nobody pays for a disadvantage | S, K |

### I2. Blocking pass (placeholder sprites, real sizes and timing)
| ID | Look for | In |
| --- | --- | --- |
| BL-01 | The capture is measurable: fixed game camera; frames `f###_<ms>ms.jpg` with ms from the capture start and the trigger's ms recorded; still frames with no effect for more than half the frames; frame 0 is effects-off. Otherwise re-capture before reading a number | M |
| BL-02 | The build rises: from the tell start to the peak, per-frame `coverage_pct` and `peak_luma` rise (no drop longer than one frame); a threat's tell lasts at least the reaction window; a timed or breakable state's end tell builds before the break; the player's own attempt changes the screen on the press frame or the next | M |
| BL-03 | One peak on the event: the brightest row (highest `bright_pct`; `peak_luma` for tiers without near-white) sits on the contact marker (± one frame) and no row more than 2 frames away comes close to it; `bright_pct` > 0 only where the tier allows near-white (`read-card.md` §2): none in T1; in T2 the contact flash rows (1-2 at 30 fps, about 0.5 % of the screen or less) and a target's brightness flash; in T3 the 1-2 flash frames; in T4 the white-core frames. Coverage may peak a few frames later as the shape reaches its size (BL-04); `peak_ms` is the coverage peak, not the hit frame | M |
| BL-04 | Fast in, slow out: for the growing shape after the contact (the rows after the flash frames to the last changed row), the first row whose box width reaches about 70 % of the segment's widest row falls in the first quarter of the segment (a size, never the coverage area; PROPOSAL 70-80 % in 20-25 %; bracket it); each growing layer's size curve passes the same test on its keypoints, and the layer fades or shrinks out over longer than it came in; never `linear grow` on a burst | M, S |
| BL-05 | Cause before effect: each result stage starts 3-6 frames at 30 fps (0.1-0.2 s, tuned in those steps) after its cause in the spec, confirmed in the rows; only the flash starts on the contact frame | S, M |
| BL-06 | The eye moves on: at the hit the build layers stop spawning and dim; in the rows after the peak the centre of the changed pixels moves to the result area; nothing busy stays at the old spot | S, M |
| BL-07 | A converging build (when the frame script asks for one): the changed-pixel box shrinks toward the focus across the build rows, or two build stills show inward motion | M (K) |
| BL-08 | Tail: the last row with `coverage_pct` > 0 is inside the tier's visible length; anything that blocks sight is see-through by about 2 s; nothing over about 8 s in play areas; a frequent effect ends before its next trigger | M |
| BL-09 | Footprint: `peak_coverage_pct` inside the tier cap; the top of every row's changed-pixel box stays below the maximum-height line; cover: the effect masks of the peak and tail stills hold 0 pixels inside the information-area boxes marked on the effects-off frame (never the row box: a ring around a character has a box that contains them) | M, K |
| BL-10 | Brackets: size, count, height and start time each tried too low, too high and picked (over-strong first, then dialled back), each with its clip numbers; a layer removed in a bracket with no change in the read numbers stays removed | M (≤1 K per value) |
| BL-11 | Cadence: multi-beat effects have unequal gaps between beats; paired elements (two hands, twin rings) are offset by 1-3 frames | S, M |
| BL-12 | Weight in the motion: heavy pieces accelerate and brake hard, dust drifts slow; projectiles and debris fly on arcs; a mass that changes direction carries through; a heavier hit has a longer release (follow-through and tail) than a light one; a giant's effect has slower beats and a longer settle than a person's | S, K |
| BL-13 | Check-in: the blocking capture, its numbers and the ≤4 stills go to the reviewer the brief names (or are recorded in the job folder when none is named); the animator's markers and the sound envelope are agreed; placeholder layers are marked as such in the spec until replaced; all before any texture pick. After it, footprint, peak time and stage starts move only by a recorded decision | job record |

### I3. Value and silhouette gates (on the blocking stills, before colour)
| ID | Look for | In |
| --- | --- | --- |
| VS-01 | Grey: in the peak still's luminance image (effect mask) the primary holds the top luminance at the named focus, the ring around the effect is calmer (subject/ring ratio recorded) | K |
| VS-02 | No blowout: near-white only at the focus and only on the flash or white-core frames (the `bright_pct` rows say when; the zoomed still's luminance image says where); the number of additive layers stacked at the core is written in the spec; the halo around the core is not white in the zoomed still | M, S, K |
| VS-03 | Rank order: the primary has the highest Brightness × LightEmission and sits at the focus; the secondary is narrower and dimmer than the head; the tertiary is never brighter or larger than the secondary and few (low Rate, small Size); in doubt, one still with the tertiary off reads the same | S (K) |
| VS-04 | The hit flash is a brightness jump in the luminance image, not a hue change alone | K |
| VS-05 | Black-fill: the peak and build masks at the phone viewport show one primary shape; a fresh read names the effect type by the shape code, its direction (head brighter, tail tapering) and the verb | K |
| VS-06 | Masses (clouds, smoke, piles) read solid: their black-fill with holes kept shows no background holes inside the mass | K |
| VS-07 | Size steps: sibling shapes (rings, chunks, crystals, debris) differ by at least about 15 %, about 3 : 2 : 1 | S, K |
| VS-08 | Mesh shapes (domes, rings, mesh slashes, rock rings): black-fill render at the game camera on `#FF00FF`; broad cuts survive at the phone viewport; a cut that vanishes is enlarged or removed | R |
| VS-09 | Contrast list for the primary (value, hue, saturation, size, shape, motion against its local background): at least one clearly wins; a weak read is fixed by calming the surroundings or one contrast, never by more layers | K |
| VS-10 | Critical markers (danger edges, pickups) reach about 3:1 luminance contrast (PROPOSAL, our tolerance, not a UI rule) against the lowest-contrast local background | K |

### I4. Colour and polish
| ID | Look for | In |
| --- | --- | --- |
| CP-01 | One main hue: the effect's palette clusters are one hue family plus at most one role accent; on the stage's most saturated same-hue area it still separates (otherwise add the role accent) | K |
| CP-02 | Colour role and caster: the main cluster is nearest its role swatch; the caster's main hue is analogous; no reserved colour in decorative layers; where the effect overlaps its own caster, a still shows a value or hue edge between them | K |
| CP-03 | Reused layers recoloured: no cluster outside the effect's palette; the mood reads from colour in the phone-size still | K |
| CP-04 | The additive core reads coloured: a saturated, darker halo (LightEmission 0) sits behind the bright core; the zoomed peak still shows a coloured ring around the centre | S, K |
| CP-05 | Energy looks alive: a bright core, a softer glow, and a shell or texture that moves (two consecutive stills differ in the shell, not only in size) | K |
| CP-06 | Colour moves through life by hue (hot → body → cool or dark), never toward grey; gold and fire stay saturated in their dark keys | S |
| CP-07 | No popcorning: masses, clouds, piles, floor bits and ambient layers fade in and out by Transparency (not only shrink); must-notice layers are full on their first frame; sparks and flares may shrink out; two consecutive stills of a mass show no particle born or dying at full strength | S, K |
| CP-08 | Flicker layers sit behind the focus at low opacity; the core is steady (its brightness in the build rows changes smoothly) | S, M |
| CP-09 | Variation only on decorative layers (Rotation on symmetric sprites, size about ±15 %, lifetime about ±20 %, FlipbookStartRandom on chips); semantic layers locked; repeated objects vary rotation and size; nothing spins once at rest | S |
| CP-10 | Textures opened with Read: glows are soft dots with small irregularities and no square edge (on dark and light), impact shapes solid, one style family per effect | texture viewed |
| CP-11 | Piles and spawned debris stay inside the play area (spawn width inside the floor bounds) and stack believably low | S, K |
| CP-12 | Ambient layers are slow, low-emission and partly hidden; the spec names each ambient effect's distance to the nearest sight line and route from the ambience map; in the stage still they are neither the brightest nor the fastest thing near a sightline; a map mechanic's effect draws the eye only at its planned moments (count the rows of a normal-round frame folder where it changes outside them) | C, M |
| CP-13 | Ground marks and cracks taper and stop at the affected area; a ground ring has a vertical or camera-facing edge where a low camera flattens it; far or foreshortened parts at the game camera: small bits that merge into lines in the phone-size still are removed or enlarged | S, K |
| CP-14 | Shape change by a Roblox route: an overshoot passes the target size once, then settles; squash on contact as a ring or dust, stretch on speed as streaks (Squash, VelocityParallel); never by scaling a character part | S |
| CP-15 | Detail indicated, clumped at the focus with rest areas between; one to three committed flow lines (trails, wind lines) lead into the focus, not across it | K |

### I5. Spec and budget
The spec lines SP-01 to SP-13 live in `vfx-craft` §5; run them before the in-game pass.

### I6. In-game pass (Studio and device)
| ID | Look for | In |
| --- | --- | --- |
| IG-01 | Busiest expected moment at the game camera on the phone viewport, with players, HUD and other effects: threat, own action, pickup and route named at a glance; the effect is not the brightest thing unless it is the top-ranked item; three questions answered: can the player read what it is and does, does it answer the player, does it look like the rest of the game (next to 2-3 approved effects) | C |
| IG-02 | Worst-case count (every player's effect at once): no effect pixel covers the information areas (a still with and one without the effects, the cover one-liner of `vfx-craft/references/measure.md` §3); nothing tall blocks the camera's view; each footprint inside its cap | C |
| IG-03 | Two-client (the owner starts the server; batch the requests): the bystander's camera never shakes, flashes or tints from another player's effect; toned layers hide neither the bystander's threat nor the nearest pickup; the threatened player sees the threat full and brightest near them. Without two clients: not verified | C |
| IG-04 | Truth overlay (the builder's debug part of the server shape) at warning, contact and active end, per tier and viewer: ring edge, flash edge and dust stop line on it (±5 %, never inside); nothing danger-coloured after the last tick; 20 fuse runs match the server time; two captures of the same attack show an identical tell, row by row up to the contact | C, M, log |
| IG-05 | Attempt and outcome: the attempt cue's first changed row is the press frame or the next (the first row with `coverage_pct` > 0, not `onset_ms`); a request the server rejects (the builder's hook) plays no outcome layer | M, C, log |
| IG-06 | Grayscale, sound off, reduced motion and reduced flashes on: every threat, pickup, team, tier and outcome still found; no camera motion and no large flashes remain; every channel in the spec names its off path | C |
| IG-07 | Flash count with `measure.md` §6 on the busiest-scene frame folder: both counts (flashes over 10 % and over 3 % of the screen) at most 2 per rolling second by design, never more than 3; every Bloom, ColorCorrection or other post-effect pulse and every pulsing layer over about 3 % of the screen in the spec added by its rate (the frames count too low where flashes overlap in one region, a flash lands on the frame of a larger darkening, lights flash in turn, or after a smaller lasting darkening: the list next to the command, with the box-per-light workaround; a count at or over the cap is checked on the stills of its listed onsets before a fix note); no saturated red flash in the spec (frames: not verified) | M, S |
| IG-08 | Pulses and blinks: each rate read from the spec first (sequence or tween period, server timer), then confirmed with the §6 box reading on a tight box around the layer, on the effect's own folder or a stretch of the busiest folder with no other change in the box (never from clip rows); lasting zones steady or ≤1 Hz; countdowns 1 → 2 → 3 Hz on the server timer; nothing above 3 Hz at full contrast; flicker above about 10 Hz from the spec only | S, M |
| IG-09 | Repetition at the real rate: 100 triggers at one per second and a burst (for example 20 per second) from the builder's rate trigger: no tail build-up hides the next contact; one label and one sound per merge window; live copies and particles within the caps (counted in Studio); the final count exact; whether the repeat tires is the owner's call on a playable preview | C, log, O |
| IG-10 | Camera channels match the tier; shake is rotation only on smoothed noise, falls off with distance and starts with the shockwave; a frequent effect never moves the camera; near a wall in third person the shake causes no clipping | S, C |
| IG-11 | Hit-stop: the freeze length rises with hit strength and stays well under 0.5 s; only the attacker, the target and the hit's own particles freeze (debris, other players and physics keep moving); the freeze frame is the animator's contact pose; none on explosions, projectile throwers, rapid fire or crowds | C, log |
| IG-12 | Sync on the target device: the sound onset 0 to about 40 ms after the first lit peak frame, never more than one frame early. Otherwise not verified (the Output log shows scheduling only) | D |
| IG-13 | Stage extremes: brightest, darkest, most saturated and busiest surfaces; the dark test place first, then the game's lighting; lowest and highest graphics quality: no background erases the primary; the information layers survive the lowest tier; a bright hazard effect (lava glow, fire wall) is tamed until a character in front of it still separates | C |
| IG-14 | Paid reveals: the lowest and highest results' windups identical row by row up to the result frame; no higher tier's layer on a lower result; each tier named in grayscale | M, C |
| IG-15 | Integrated frame with lighting, players and UI: the effect does not sit on faces or on the player's own key pose at a held moment; effects stay below threats; with Bloom and post effects off the read still holds | C |
| IG-16 | Muted first, then with sound: the meaning reads with sound off (a meaning that needs sound is a readability fault); then the full mix with music and other sounds | C, D |
| IG-17 | Feel at normal speed (timing, weight, the hit) is the owner's call on a playable preview at the named gate; until then the clip numbers and the bracket record stand as PROPOSAL | O |
| IG-18 | Escalation (combo, chain, streak, boss phase): each tier steps only at a real outcome threshold and adds one layer or one hit-stop step at the impact point, never over it; peak coverage per tier rises with the tier; the tier is named by a short text label that reads with particles off; it resets visibly after idle | M, C |

### I7. Honesty (every hand-back)
- Renders, captures and stills made and looked at, against the budget above.
- What each input could prove (§A); a line without its input is "not verified", never PASS; the could-not-check list names the step, the missing input and the capture that would close it.
- Notes given or answered: each names the problem it solves, carries a marked still (before and after), and the original problem is re-checked; one problem per pass is logged with its before and after numbers.
- Scope added mid-job appears as a ticket with its cost.
- One named weakness with its next step, or why there is none.
