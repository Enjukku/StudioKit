> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13

# Juice, repetition and picture-sound sync

Evidence: `knowledge/reference/vfx/05-juice-repetition-sync.md` (rows cited as "05 5a", "05 P6" = Part 6, "05 P7" =
Part 7, "05 P-xx" = its PROPOSAL rows) and `contradictions.md` (X-, PD- rows). Sources by R-id (`00-sources.md`).
Tags: [study] peer-reviewed; [preprint]; [practice] named studio, artist, vendor or Roblox docs; [spec] standard or
engine API; [inference] reasoning; [P] PROPOSAL start value, untested, owner may change. "abs" = abstract only,
direction only. Sound itself is owned by the sound-design skill; this file only fixes the trigger link.

## A. Procedure (use on every hit, break, pickup, reward or UI cue)

1. Name the confirmed outcome the effect reports (hit, break, pickup accepted, sale confirmed). No outcome, no big layer (JU-01).
2. Give it an importance tier (tiny / normal / big / rare) and the channel count for that tier (JU-08, T-02).
3. Lay the timing shape: windup → punch on contact → follow-through → dissipation (JU-06).
4. Estimate rate (per s, max burst). Every-second effects get the repetition plan (§E) and caps (§F).
5. Any escalation or intensity raise runs the amplification check (§D) first.
6. Schedule picture punch and sound transient from one event (§G). Write the sync target on the card.
7. Run the failure-mode table (§C) as a review pass; then the tests in §I.

## B. What the juice studies say

| Finding | Effect size | Tier / source |
| --- | --- | --- |
| Success-dependent feedback (fires on the achieved outcome) raises competence, effectance, curiosity; no direct effect on enjoyment or playtime | n=1,699, Model B: competence b=+.45 [.30, .60]; effectance +.26 [.15, .36]; curiosity +.29 [.17, .41], all p<.001 (effectance, curiosity paths exploratory) | [study] pre-registered; R-043; 05 5a |
| Amplified (more intense) feedback not tied to success lowers competence and effectance; amplified swing covered later hit and kill feedback | Model A n=678: effectance b=-.19 [-.36, -.03]; competence b=-.43 [-.68, -.19]; no direct effect on enjoyment or playtime; curiosity effect unconfirmed (X-09) | [study] R-043; 05 5a |
| Random variety per trigger: small enjoyment gain, no curiosity gain | enjoyment b=+.11 [.01, .22]; curiosity b=-.01 ns | [study] R-043; X-19 |
| Curiosity is the strongest predictor of enjoyment and of voluntary playtime | curiosity → enjoyment b=+.75 / +.76; → playtime .88 or .99 (both printed, X-07); never quote playtime minutes (X-06, X-08) | [study] R-043 |
| Medium beats extreme: four builds None / Medium / High / Extreme; Extreme lost on enjoyment, None and Extreme lower on playtime; effects small | n=3,018; η²p .003-.006; F(3,3014)=5.83 / 5.87 | [study] R-101; X-10, X-11 |
| Raising intensity alone (amplitude, duration, volume, density none→high) changed nothing | n=26: engagement 3.38/3.31/3.42/3.38, p=.784 | [preprint] R-005 Study 3 |
| Juicy vs plain UI raises engagement and aesthetics | n=47: engagement 3.647 vs 3.224, aesthetics 5.155 vs 4.284, p<.001 | [preprint] R-005 Study 1 |
| Feedback after the action is the only single slot that helps; more phases also help | n=46: post engagement 3.713 vs 3.504 p=.004; +.110 engagement per phase | [preprint] R-005 Study 2; X-15 |
| Text labels carry graded progress better than particles; particles carry appeal | n=45: progress Text 5.62 > Particles 4.43 > None 2.81 (W=.44) | [study] R-045; X-14 |
| Juicy rated higher, played worse | direction only, n not found | [study] abs, R-123 |
| Hand-tuned juice beats baseline; generated sets mostly not | N=113: expert vs baseline p<.001; 2 of 6 generated sets beat baseline | [study] R-079 |
| Haptics: low and high both beat none; high did not beat low | n=38, no stats read | [study] abs, R-086 |
| Shake on hit raises felt agency (mediated by exhilaration); upper limit untested | n, sizes not obtained | [study] abs, R-004 |
| No hit-stop ranks bottom for impact feel; hit-stop, sound coherence, camera control separate top from bottom | 2 no-stop games ranked 39th, 40th of 44; correlational | [preprint] R-073; 05 5b |
| Long hit-stop turns uncomfortable | VR, n=15-16: favourite 0.37-0.39 s; pleasant/unpleasant boundary 0.537-0.55 s | [study] R-035; X-02 |
| Kao 2020 and CHI 2024 are not one dose curve; neither sets an optimum for Roblox, phones, children, multiplayer | n/a | [inference] X-13 |

## C. Design rules: juice

| ID | Rule | Test (fails when) | Evidence |
| --- | --- | --- | --- |
| JU-01 | The big layer fires only on a confirmed success (contact, break, accepted pickup, server-confirmed sale). Input, swing, launch get a small cue. Hierarchy action < success < big success. | the full layer plays on a miss or before server confirmation | [study] R-043; 05 5a, 5e |
| JU-02 | Do not raise intensity to fix a flat effect. Fix outcome link and readability first, then tune amount. | the only change in a fix is size, brightness, count or length | [study] R-043, R-101; [preprint] R-005 S3 |
| JU-03 | Default to a medium build for frequent effects; amplified layers only on the top 2 importance tiers and only on success. | a frequent effect reaches top-tier size, brightness or screen area | [study] R-101; [P] 05 P-03 |
| JU-04 | Grade feedback by a real cause the player can learn (material, force, weak point, chain size). Never grade at random. Grading, not random variety, is the curiosity lever. | two equal causes give visibly different tiers, or a tier changes with no cause | [study] R-043 (authors' interpretation); X-19 |
| JU-05 | Windup, launch and swing layers never cover the impact point or the next contact. | a frame capture shows the contact point hidden by a pre-contact layer | [study] R-043 Fig. 5 |
| JU-06 | Put the reward beat on or after the confirmed result (punch, then follow-through). Build expectation in the windup; surprise only on rare tiers. | a reward layer starts before the outcome frame | [preprint] R-005 S2; [study] abs R-020 |
| JU-07 | Graded progress (combo x3, CRIT, streak) uses a short text label plus particles; meaning survives with particles off. | tier unreadable with particles disabled | [study] R-045 |
| JU-08 | One job per channel (shape, brightness flash, sound, shake/camera, haptic). Normal hit ≤4 channels (T-02); more only on the top tier. | a layer has no named job, or a normal hit uses >4 channels | [practice] R-144, R-110; [P] PD-10 |
| JU-09 | Hit flash on the target is a brightness (value) jump, not a hue change alone. | flash invisible in a greyscale capture | [preprint] R-073; [study] R-117 |
| JU-10 | Weapon contact gets local hit-stop by tier (T-01): weapon animation, `ParticleEmitter.TimeScale` 0, camera hold. Never physics bodies. Explosions and charges 0 by default; none on chain secondaries, rapid fire, crowds; throwers of projectiles get none. | debris or other players freeze; stop on a charge blast or a chain secondary | [preprint] R-073; [practice] R-134, R-156, R-154; [spec] R-211; [P] PD-02 |
| JU-11 | Shake and camera moves only on success events, scaled by event size; frequent events none. | shake on pickups or on every small block | [study] abs R-004; [practice] R-124, R-282 |
| JU-12 | Haptic: one short pulse on success tiers on mobile; do not scale strength up for "more". | haptic on input or on every pickup | [study] abs R-086 |
| JU-13 | Judge a change on readability and competence (miss / hit / blocked / break / big break identified), not liking. Compare complete builds. Keep a "fewer effects" build for tense moments. | the evidence for a change is "looks better" | [study] R-123, R-079; [preprint] R-005 S3 |
| JU-14 | Each event ends in a stable readable state (debris settled, counter final, item shown). | the capture ends mid-motion or with the counter still moving | [inference]; no source |

**What satisfying effects share** (review checklist; all must pass): outcome-bound (JU-01) · graded by real
importance, same tier = same visual weight (R-110, R-120, R-080) · several channels on one event (R-073, R-110) ·
windup / punch / follow-through / dissipation (R-120, R-005) · contrast and restraint: quiet baseline, peaks rare
(R-101, R-044) · first response within 100 ms (R-153, R-370) · eased curves for pops, flights, counters; constant
speed where speed matters (R-110) · clean ending (JU-14).

## C2. Failure modes (diagnose, then fix in this order)

| Symptom | Cause | Fix | Evidence |
| --- | --- | --- | --- |
| Mushy | no concentrated contact: no hit-stop, diffuse edges, uniform speeds | add a hit-stop tier (T-01), sharp brightness flash at contact, split fast mass from slow decorative tails | [preprint] R-073 + [inference] |
| Floaty | heavy pieces move like dust; perfectly clean arcs | heavy debris accelerates and stops hard; dust drifts slow; break perfect arcs slightly | [practice] R-302 (characters) + [inference] |
| Cheap / disconnected | big flourish on a minor outcome; late or wrong sound | rebuild contact cue first. Test: mute sound, drop tertiary layers; event must still read | [inference] + R-073 |
| Noisy | every effect top-tier; redundant layers; action layers cover outcomes | keep the hierarchy, trim ordinary peaks (never enlarge the top), cap channels (T-02) | [study] R-043, R-123; [practice] R-110 |
| Delayed | variable latency; visual swell before an instant impact | first response on the input or confirm frame; flipbook starts on an energetic frame; any unavoidable delay constant across weapons and devices | [study] R-064 (jitter: flow η²=.28; 12 switches vs 0 d=1.329), R-062 (expected lag: competence η²=.313); [inference] |
| Annoying / fatiguing | long freezes, slow counters, lingering tails, identical repeats, repeated large flashes | short tails (T-03), no hit-stop in crowds, fast counters (T-11), variants (§E), flash cap (T-10) | [study] R-035; [spec] R-167; [practice] R-120, R-370 |

## D. Amplification check (run before any escalation step, repeat boost or intensity raise)

| # | Check | Fails when | Source |
| --- | --- | --- | --- |
| 1 | Tied to outcome | extra intensity fires on input or attempt | R-043 |
| 2 | Impact point visible | new layer covers the contact or the next contact | R-043 Fig. 5 |
| 3 | States still distinct | observers cannot tell miss / hit / blocked / break / big break apart | R-043, R-110 |
| 4 | Measured on readability, not liking | only evidence is "looks better" | R-123, R-005 S3 |
| 5 | Below the extreme build | a frequent effect moves toward top-tier size | R-101 |

## E. Repetition rules

| ID | Rule | Test (fails when) | Evidence |
| --- | --- | --- | --- |
| JU-15 | Variants hide repetition; they do not add satisfaction. Never use variety in place of graded, outcome-tied feedback. | a "make it more satisfying" fix only adds variants | [study] R-043; X-19 |
| JU-16 | Randomise decoration only. Lock the contact frame, hitbox or danger boundary, team colour, warning deadline and the start frame of semantic one-shots (telegraph, explosion). | `FlipbookStartRandom` or size jitter on a telegraph or blast core | [inference] on R-043 |
| JU-17 | Build variants by recombining layers (e.g. 3 cores x shared secondaries) and one grey texture + colour ramp, not unique assets per variant. | each variant is a separate full-effect asset | [practice] R-383 (sound method, transfer = inference), R-326 |
| JU-18 | Per-particle variation through engine randomisation: `FlipbookStartRandom` (start + range ≤ frame count; about 16 frames usually enough), `Rotation` 0-360 for radially symmetric sprites only, `RotSpeed` range. ParticleEmitter has no UV scroll: flipbooks + randomisation; Beam texture scroll where a path fits. | rotation randomised on a directional sprite | [spec] R-211; [practice] R-342 (single tier C); X-66 |
| JU-19 | More frequent = shorter and subtler. Tails ≤0.5 s on every-second effects; long tails only for rare big events (T-03). | tail build-up hides the next contact in a 1 Hz capture | [practice] R-120, R-360, R-370; [study] R-044 |
| JU-20 | Merge same-kind events inside the merge window into one burst, one sound trigger, one count label (T-05). | 20 pickups in 1 s show 20 bursts or 20 labels | [practice] R-153, R-370, R-383; [P] 05 P-04 |
| JU-21 | Cap live copies per client, cull oldest; cap particles per frequent copy (T-07, T-08). Above the full-detail blast cap, extra blasts play the primary layer only. | live copies or particles exceed the cap in a 20-burst test | [practice] R-248, R-326; [P] PD-10, 05 P-11 |
| JU-22 | Culling priority: P1 essential look, P2 supporting flavour, P3 environment; drop lowest first; fade with distance, never pop. Threat and pickup cues are P1. | a P1 layer drops while a P3 layer survives, or an effect pops out | [practice] R-299 |
| JU-23 | Steady-state live count ≈ `Rate` x mean `Lifetime` + bursts; budget from copies at once x particles per copy. | budget sheet ignores simultaneous copies | [spec] R-211; [practice] R-248 |
| JU-24 | Assume punch fades with repeats (largest drop in the first repeats, plateau about the 4th, transfer from face data) and test over hundreds of shots, not one. | sign-off based on first-view reactions only | [study] R-094 (faces); [inference] |

Cooldown / retrigger interval for VFX: no number found (05 P6). Use the merge window (T-05) and caps (T-07).

## F. Combo and streak escalation

| ID | Rule | Test (fails when) | Evidence |
| --- | --- | --- | --- |
| JU-25 | Each escalation tier is gated by a real outcome threshold (break count, chain size), never by input count or time held. | tier rises while missing | [study] R-043; [P] 05 P-12 |
| JU-26 | Each step adds one layer or one hit-stop tier at the impact point; it never covers the impact point and passes §D. | step adds a full-screen layer or covers contact | [study] R-043 |
| JU-27 | Tier is named by a text label (x2, x3) and readable without UI colour; reset after a fixed idle time with a visible drop, no silent reset. | testers cannot name the tier without the UI | [study] R-045; [P] 05 P-12 |

Step sizes, step counts and reset times: no tier A-C number (leads only: R-438, R-445, R-408, tier D).

## G. Picture-sound sync

Sign: positive = sound ahead of picture. Values in ms.

| ID | Rule | Test (fails when) | Evidence |
| --- | --- | --- | --- |
| JU-28 | One trigger event schedules both the visual punch and the sound transient; never two independent timers or two network messages. | flash and sound are triggered from different code paths | [practice] R-387, R-344, R-363; [inference] |
| JU-29 | Target physical sync; measured output sound 0 to +40 ms late, never more than 1 frame (16.7 ms at 60 fps) early (T-09). No deliberate sound lead on hits. | capture shows sound onset before the first lit frame by >1 frame | [spec] R-170, R-169; [study] R-121, R-070, R-048; [P] PD-14; X-17 |
| JU-30 | Brightest flash 1-2 frames on the transient frame; swap to the destroyed mesh at the flash peak; delay small shake by distance to match the shockwave. | mesh swap lands after the flash peak | [practice] R-387, R-344, R-388, R-363 (fps not stated) |
| JU-31 | Any intended offset (distant explosion delay, anticipation sound) is labelled "intended" on the effect card with its ms. | an offset appears in capture with no card label | [inference] R-078, R-170 |
| JU-32 | Keep latency constant: varying delay is worse than steady delay. Measure output on device (phone speaker and Bluetooth); code-simultaneous is not output-simultaneous. | sync only checked in Studio on PC | [study] R-064, R-076; [inference] |
| JU-33 | Sound carries weight and transient, picture carries shape, size and direction (design split, not evidence); when shake is cut, compensate with sound and animation. Detail of the sound: sound-design skill. | picture alone tries to carry weight with shake | [preprint] R-073; [practice] R-282, R-453; [inference] |

Tolerance references (none is a plug-in game budget, X-18): broadcast detect +45 / -125, accept +90 / -185, chain
+22.5 / -30 (R-170 [spec]); EBU end-to-end +40 / -60 (R-169 [spec]); sound-lead detected better, d' 1.58 vs 0.98
(R-121 [study]); game audio delay 40 no effect, 270 tension up, 500 positive affect down (R-070 [study]); audio
latency JND 49 at base 0 (R-048 [study] abs); causal action JND 143 vs 219 (R-078 [study]); touch tap JND 69
(R-053 [study], second-hand); 60 fps frame = 16.7, 30 fps = 33.3 (arithmetic).

## H. Tunable values

| ID | Value | default | range | move up when | move down when | hard cap | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-01 | Hit-stop, weapon contact (local) | 50 / 100 / 150 ms light / heavy / crit-finisher; explosions 0 [P] | test 0-250 ms | heavier weapon, finisher | multi-hit, rapid fire, crowds, chains (→0) | well under 0.54 s (VR discomfort boundary 0.537-0.55 s) [study] | PD-02; R-154 [practice] 0.05 / 0.1 s; R-035; R-134, R-156 |
| T-02 | Channels per normal hit | type recipe (v2; was ≤4 [P]) | 2-4; top tier more | top importance tier | frequent event, crowded scene | [superseded v2: SKILL.md §4] [P] | PD-10; R-110, R-144 [practice] |
| T-03 | Tail, every-second effects | ≤0.5 s [P] | test at 1 Hz | rare big event (≥2 s allowed) | rate rises, next contact hidden | no number found | 05 P-15; R-120, R-370 [practice] |
| T-04 | First visible response | same frame as input or confirm | ≤100 ms | n/a | n/a | 100 ms reads instant [practice] | R-153, R-370 |
| T-05 | Same-kind merge window | 100 ms [P] | test 20 events/s | counter unreadable | merged events read as lost | no number found | 05 P-04; R-153, R-383 |
| T-06 | Variants per every-second effect | 3, by layer recombination [P] | test 1 / 3 / 6 | repeat spotted at 1 Hz | variants change meaning | no VFX number found | 05 P-08; R-383 [practice, sound] |
| T-07 | Live copies of one frequent effect per client | ≤8, cull oldest [P] | test 1 / 5 / 20 bursts | frame time headroom on low-end phone | frame time over budget | full-detail blasts ≤4 per client [P] | 05 P-11; PD-10; R-326 [practice] |
| T-08 | Particles per copy, every-second effect | ≤10 [P] | 3-10 [practice] | n/a | many copies at once | no Roblox number | R-248 (mobile RTS, single source); 05 P-11 |
| T-09 | Sound offset vs first lit punch frame | 0 to +40 ms late [P] | -16.7 to +40 ms | n/a | measured drift on device | never >1 frame early [P]; EBU +40 / -60 [spec] | PD-14; R-170, R-169, R-070 |
| T-10 | Large-area flashes, all effects | 2 per rolling 1 s [P] | n/a | n/a | busy scene | 3 per 1 s or area rule (WCAG) [spec]; flash layer ≤1% screen [P] | PD-11; R-167; X-43 |
| T-11 | Coin flight / count-up | burst 0.2 s, flight 0.5 s eased, count-up ≤0.6 s [P] | flight 0.4-0.8, count-up 0.4-1.0 | n/a | slow-counter complaints | >400 ms reads slow [practice] | 05 P-05; R-158, R-370; X-61 |
| T-12 | Reward layer stagger | 0 / +80 / +140 ms spark / coins / count [P] | 2-3 frames between emitter starts | layers blur together | reads delayed | no number found | 05 P-06; R-411 (D), R-388 |
| T-13 | Random spread, decorative layers | size ±15%, brightness ±10%, lifetime ±20% [P] | test 0 / 10 / 25% | repeat spotted | shape illegible at phone size | none on semantic parts | 05 P-09; R-211 [spec] |
| T-14 | Escalation tiers / reset | 3 tiers, reset 3 s after last qualifying break [P] | 3-5 tiers; 1.5-5 s | testers miss tier changes | tiers blur, impact hidden | no number found | 05 P-12; leads R-438, R-445 (D) |

## I. Conflicts not settled and tests

| Item | Status | Test |
| --- | --- | --- |
| Guilty Gear hit-stop 7 / ~10 f (R-073) vs 11-15 f (R-431, D) | unresolved, no fps; never convert to ms | not needed; T-01 A/B |
| CHI 2024 curiosity → playtime .88 vs .99; playtime means | unresolved (X-07, X-08) | OSF data of R-043 |
| Why excess feedback hurts: cognitive load vs blocked outcome binding | unresolved (X-20); JU-05 holds either way | none needed |
| Who leads (sound vs picture) | partly resolved (X-17): physical sync | T-AV capture at -3 / 0 / +3 frames, speaker + Bluetooth |
| Hit-stop per tier, variants, spread, caps, escalation, flight times | all [P] | 05 Open: Studio A/B on a phone; 1 Hz x 100 shots; 1 / 5 / 20 bursts with MicroProfiler; testers name tier without UI |
| Shake comfort limit on phones | no 2020+ flat-screen study | 3 strengths x 2 durations, comfort after 10 blasts |
