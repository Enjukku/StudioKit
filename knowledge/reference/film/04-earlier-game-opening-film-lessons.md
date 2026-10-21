---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J015-T04, first game's opening-film records (read-only), 2026-10-10..2026-10-13"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Lessons from the first game's opening-film planning (any game)

The first game planned an opening film from 2026-10-10 to 2026-10-13. Its records stop before any storyboard still, animatic, render, upload or listening test existed. So these rows hold owner decisions, owner corrections, agent proposals and open questions, and no measured result of a finished film. Game-specific content is removed on purpose; each row gives the general mechanism and a pointer.

## How to read

| Key | Meaning |
| --- | --- |
| certainty: owner decision | The owner chose it (a decision row exists). |
| certainty: owner correction | The owner rejected or reversed something an agent made, and the row states the rule behind it. |
| certainty: proposal, not approved | An agent proposal, or an agent's own observation in a log, that the owner never ruled on. Do not treat it as proven. |
| certainty: open | A question the records leave unanswered, or a risk nobody tested. |
| trace | `DS` = `C:\Users\Firew\Downloads\uterd\DestructionSimulator\knowledge\` (read-only). `D-nnn` = a row in `DS design/decisions.md`. Numbers after a colon are lines. |
| docs facts | Roblox facts quoted here were read in the first game's docs mirror on 2026-10-12 or 2026-10-21. Check them against the current mirror before relying on them. |

## 1. Plan and owner process

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| P-01 | The owner wanted the whole film at game start, not spread over several first-time moments: "No, I want the whole sequence of events" (D-148). Plan the full sequence; offer a split only as a priced option. | owner decision | D-148 (decisions.md:158) | plan, owner gate |
| P-02 | The story came from the owner in their own words over several chat rounds, and each later decision changed an earlier one (the key story object changed within a day). Keep one beat list and update it per decision id; do not re-plan from scratch. | owner decision | D-147, D-148, D-149, D-180, D-181 (decisions.md:157-159,190-191) | plan |
| P-03 | Length was sized by beat count with seconds per beat: first draft about 85 s, cut to about 55 s by faster cuts and merged shots with every beat kept. The record says going under about 45 s means dropping beats, not speeding up. The video-only part later sat at about 40 s. | proposal, not approved | DS design/story-opening-cutscene.md:36,60-61; DS design/story-film-plan.md:5 | plan, previs |
| P-04 | Proposed for a forced film: plays once for new players, with a skip button from second 1. Not ruled on. | proposal, not approved | DS design/story-opening-cutscene.md:60 | runtime, owner gate |
| P-05 | Proposed rule: no step starts for a scene until the owner approved the step before it. Changes are cheap while planning, designing, boarding and in the animatic; expensive in animation and look. | proposal, not approved | DS design/story-film-plan.md:23-24 | plan, owner gate |
| P-06 | The owner answered by picking among options that each carried a recommendation, and new designs went to the owner as a sheet first (a face sheet before any build). Ask in that shape. | owner decision | D-180, D-183, D-186 (decisions.md:190,193,196) | plan, boards, acting/rig |
| P-07 | The story world's set was designed and built as its own set before any storyboard, not borrowed from a gameplay stage. The owner picked the own-set option from the start. | owner decision | D-183 (decisions.md:193); DS design/story-film-plan.md:64 | plan, boards |
| P-08 | Platform limits go at the top of the beat list: relationship beats shown only as friendly closeness, with no romantic wording in any text, title or line (romantic themes are 18+ only on Roblox); loss shown without blood or visible injury. The owner accepted both and chose non-gory ways to show loss. | owner decision | D-148 (decisions.md:158); DS design/story-opening-cutscene.md:14-15 | plan, owner gate |
| P-09 | Each shot row listed camera, seconds, what is on screen and what it needs (assets). The asset list then marked each item rigged, partly there or missing. That table showed most of the cast, set and props missing before any board could start. | proposal, not approved | DS design/story-film-plan.md:38-70 | plan |
| P-10 | Order of work proposed: start boards with the shots that use only finished characters; start missing cast and set in parallel; build the animatic as soon as every shot has a still. | proposal, not approved | DS design/story-film-plan.md:83-87 | plan, boards |

## 2. Boards and cast references

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| B-01 | Boards were planned as Blender stills of the real models in rough poses, not AI images, so cast and scale stay consistent. The reason is recorded; no board was ever made, so the choice is untested. | proposal, not approved | DS design/story-film-plan.md:16 | boards |
| B-02 | Agent observation: chaining image-to-image from earlier generations drifts proportions. Always pass the owner-approved sheet as input and state the proportions in words. A full T-pose stretches short, round characters; a relaxed A-pose worked. | proposal, not approved | DS logs/2026-10-11-story-cast-refs.md:12 | boards, acting/rig |
| B-03 | For image-to-3D references the owner asked for exactly one character in one angle that shows as much as possible, because extra angles make the tool build extra models. The owner suggested a T-pose; B-02 found a T-pose stretches short characters. The two were never reconciled. | open | D-153 (decisions.md:163); B-02 | boards, acting/rig |
| B-04 | The owner rejected models that were each fine alone but "don't look like they exist in the same world" (D-153). Every character shares one style, one material language and one light. Check the whole cast side by side before showing it. | owner correction | D-153 (decisions.md:163) | boards, acting/rig, owner gate |
| B-05 | The style came from comparing several style tests side by side; the owner picked one. A three-quarter reference view (about 40 degrees) was used so back-worn parts (tails, capes) show. | owner decision | D-155 (decisions.md:165) | boards |
| B-06 | A concept sheet fixes shape and design; the owner restyles it in Blender, so the sheet is a reference, not the final art style. | owner decision | D-150 (decisions.md:160) | boards |
| B-07 | An antagonist must be readable: face visible, human-reading personality, complete body. The owner rejected drafts with a hidden face ("the player should hate this character") and a design whose lower body was missing. | owner correction | D-150, D-151 (decisions.md:160-161) | boards, acting/rig |
| B-08 | "Controlled or mindless" must read from the picture: flat, empty eyes with no highlight and a stiff, robot-like posture, plus an understated accessory. The owner rejected eyes that looked conscious and a showy accessory. | owner correction | D-152 (decisions.md:162) | boards, acting/rig |
| B-09 | Removing facial features to make a character less realistic read as lazy to the owner. Stylise the features instead (large eyes, one highlight, a simple closed smile worked). | owner correction | DS logs/2026-10-11-story-cast-refs.md:14 | boards, acting/rig |
| B-10 | Supporting characters must not be recolours of one another. They share the lead's species look but differ in fur tone, pattern, markings, build and personality; only the lead wears clothes, which marks the lead. The owner also chose to show a key story beat on screen rather than hide it. | owner decision | D-180 (decisions.md:190) | boards, acting/rig, plan |
| B-11 | AI-made hands stay unreliable on a design with many limbs; the owner agreed to fix them by hand in Blender. | owner decision | DS logs/2026-10-11-story-cast-refs.md:13 | boards, acting/rig |
| B-12 | Third-party reference art is mood only. The owner's reason: the image models ignore it. Never attach a reference to a generator when its source forbids AI use; describe it in words. | owner decision | DS design/story-opening-cutscene.md:16; DS logs/2026-10-11-story-cast-refs.md:15 | boards, plan |
| B-13 | Outside the film, same image tool: ChatGPT concept images of real-world places came out inaccurate (wrong colour banding, a wrong building). The owner put real references first and used the AI images as a style hint only. | owner correction | D-164 (decisions.md:174) | boards |
| B-14 | For effects, the owner dropped 2D AI mock-ups: the look comes from an approved reference clip, a motion blueprint and real captures. This is not a ruling on film boards; ask the owner before assuming AI storyboards are wanted for film. | open | D-284 (decisions.md:221) | boards, owner gate |

## 3. Acting: rigs, faces, eyes

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| R-01 | Image-to-3D models fuse limbs to the body, so a raised arm webbed the torso and posed arms clumped. The owner's fix: build the limbs, feet and tail as separate meshes, each skinned only to its own bones, with roots buried a little in the body like sewn-on limbs. | owner decision | D-160 (decisions.md:170) | acting/rig |
| R-02 | When a design has several fused limbs of one kind, build one clean limb and copy it to every position; each copy keeps its own jewellery or prop. The owner chose this over cutting the fused limbs apart or redoing them by hand. | owner decision | D-167 (decisions.md:177) | acting/rig |
| R-03 | The head is its own part too. Variants (bigger, rounder, smaller) must not come from bending the body mesh: the first variant set was rejected for shoulder lumps and a creased neck ("You can tell that the rigs are broken", D-185). A separate neck mesh also creased, and thickening limbs on an unchanged body made lumpy shoulders. The owner asked for a written rule backed by research. | owner correction | D-185 (decisions.md:195); DS reference/character-part-rigging.md:116-124 | acting/rig |
| R-04 | Each character needs its own face kit: separate mouth shape, eye type, nose colour and brows, so side characters are not one face recoloured. The mouth part also serves talking and crying shots. | owner correction | D-186 (decisions.md:196) | acting/rig, boards |
| R-05 | Eyes must be separate parts with a look-at target and rotation limits so a character can look at things. Where an existing painted eye look suits a character, keep it exactly and test any eye rig side by side before replacing it. | owner correction | D-184 (decisions.md:194); DS logs/2026-10-12-opening-film-rigs.md:11-13 | acting/rig |
| R-06 | Check that every speaking character has mouth shapes before planning voice. In the first game the lead's mouth was painted closed, so voice lines had no mouth. | proposal, not approved | DS design/story-film-plan.md:69 | acting/rig, sound/voice |
| R-07 | Owner-supplied rig brief for animators: animators key only control bones; IK/FK switch with snap; foot roll; head follow switch; eye target; blink sliders; mouth control; reset-to-rest; mirror. Tests run before the owner sees anything, including an animator test: block a 2 s walk and a wave using only controls. | owner decision | DS logs/2026-10-12-opening-film-rigs.md:14; DS pipelines/rig-for-animation-prompt.md:59-110 | acting/rig |
| R-08 | Rig tests (agent runs): body moved 0 under every limb pose; props followed their bones; each rig hand-back listed its pose limits (for example a tail that lifts only a few degrees under a cape). Design shots inside the listed limits. | proposal, not approved | DS logs/2026-10-11-story-cast-refs.md:22-23; DS logs/2026-10-12-opening-film-rigs.md:34 | acting/rig, plan |
| R-09 | The owner cut a planned moment because the character's short, rounded proportions could not show it on screen. The beat's story outcome stayed. Test every planned physical beat against the rig in a render before locking it. | owner decision | D-181 (decisions.md:191); reverses D-148 | plan, acting/rig |
| R-10 | When an accessory clips an animated body part, reshape the accessory and keep the body motion; the owner chose this over a shorter accessory, a hole or a still body part. Keep the clasp simple. | owner decision | D-161 (decisions.md:171) | acting/rig |
| R-11 | Cloth: Roblox has no mesh cloth simulation, so cloth keeps a bone rig that works everywhere. For pre-rendered shots, add a Blender cloth simulation per shot on top of the bone rig; live scenes use the bone rig only. | owner decision | DS design/story-opening-cutscene.md:67 | acting/rig, runtime |
| R-12 | Shared character files: link characters from one cast file into one file per scene so a rig fix reaches every scene. Do not save the shared cast file headless while the owner has it open. | proposal, not approved | DS design/story-film-plan.md:34; DS logs/2026-10-12-opening-film-rigs.md:28 | acting/rig |
| R-13 | Roblox rig facts still unverified in the first game: segmented parts joined by Motor6D (community says it breaks when welded), per-part squash and stretch at runtime, and draw cost of 8 to 11 parts per live character. Test before putting a segmented film rig into a live scene. | open | DS reference/character-part-rigging.md:90-92 | acting/rig, runtime |

## 4. Animatic and previs

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| A-01 | Proposed animatic: cameras, key poses, timing, grey lighting and temporary sound played as one video. The owner sets timing on it (longer here, cut there), before final animation and look. | proposal, not approved | DS design/story-film-plan.md:17 | previs, owner gate |
| A-02 | Proposed order: boards, rough animatic with the owner timing it, final render and one upload, then the live scene. | proposal, not approved | DS design/story-opening-cutscene.md:68 | plan, previs |
| A-03 | No animatic, storyboard still or render was made in the records. Everything here about timing, camera and previs is untested; the first game's time went to cast, rigs, faces and the sound plan. Inference: a rough blockout animatic first would have shown which shots need which rig limits sooner. | open | DS logs/2026-10-12-opening-film-rigs.md:25-34 | previs, plan |
| A-04 | Mood turns were planned with engine tools so they also work in live scenes: desaturate, then a colour-correction and atmosphere swap, a camera push and a low rumble. First-person waking was planned as blur plus vignette. | proposal, not approved | DS design/story-opening-cutscene.md:51-53 | previs, runtime |
| A-05 | Camera shake is occasional, not on every effect, explosions included: "not everything should have camera shake. Even explosions" (D-286, set for effects). | owner decision | D-286 (decisions.md:223) | previs, runtime |

## 5. Sound and voice

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| S-01 | Sound and voice are planned with the sound designer while the scenes are designed (steps 1 to 5 of the plan), not after. | owner decision | D-181 (decisions.md:191); DS design/story-film-plan.md:20 | sound/voice, plan |
| S-02 | Characters use a mix of sounds plus a few short words or short sentences, never much dialogue. The plan counted about 8 spoken words in a 41 s film. | owner decision | D-183 (decisions.md:193); DS design/story-film-sound.md:54 | sound/voice, plan |
| S-03 | Narrator: the sound plan recommends none (talks over music and faces, doubles the picture, adds a subtitle burden). The owner's reply covers dialogue but is not recorded as an answer on a narrator. | open | DS design/story-film-sound.md:53,147 | sound/voice, plan |
| S-04 | Lip-sync approach proposed: lines of 0.6 to 1.6 s, a loop of 2 or 3 mouth shapes plus a jaw flap, no phoneme-accurate sync; show a mouth only where the camera sees it, otherwise backs, closed mouths or blur. | proposal, not approved | DS design/story-film-sound.md:54,56-75 | sound/voice, acting/rig |
| S-05 | Voices are made by an adult on a paid ElevenLabs plan. Terms as read on 2026-10-12: free plan is non-commercial, under-18 users may not use the service, output must be reviewed before release, output may not be unique. Keep a licence record file with plan and dates. Re-read the terms before use. | owner decision | D-181, D-183 (decisions.md:191,193); DS design/story-film-sound.md:86 | sound/voice, delivery |
| S-06 | Per-shot cue sheet columns: music, effects, ambience, voice, and "player must feel". Add cumulative start times, an arousal arc and a priority order (voice first, then impacts, music, ambience). All were proposals tuned by ear, none auditioned. | proposal, not approved | DS design/story-film-sound.md:6,13-14,20-49 | sound/voice, previs |
| S-07 | Use silence on purpose and put hit sounds on the contact frame. At 24 fps one frame is 41.7 ms, so align sound to the frame, not to the second. Where a sound is the only cue (an ambience stopping), make the picture show it too. | proposal, not approved | DS design/story-film-sound.md:120,139,141 | sound/voice, previs |
| S-08 | Phone speaker first: low sounds carry harmonics above about 300 Hz; loudness target about -18 LUFS with true peak at or under -1 dBTP; check a mono sum for a drop over 3 dB. These are proposed values. | proposal, not approved | DS design/story-film-sound.md:132-135 | sound/voice, delivery |
| S-09 | Sound-off viewers: show each spoken word as large on-screen text (2 lines max). Whether subtitles are on was asked and the records show no answer. | open | DS design/story-film-sound.md:76,152 | sound/voice, runtime, owner gate |
| S-10 | Video-to-live seam: video audio and live audio run on separate clocks with unknown offset, so the join must not need beat alignment. End the video on a sustained, non-rhythmic cue; start a matching looping live cue when `VideoFrame.TimePosition` reaches `TimeLength` minus 1.2 s, and do not wait for `Ended`. Hand off to game music with a 2 s cross-fade. Untested. | proposal, not approved | DS design/story-film-sound.md:121-126 | sound/voice, runtime, delivery |
| S-11 | During the film mute the game music and ambience buses and play no UI sounds; skip fades the video volume to 0 over 0.3 s; restore the buses after. | proposal, not approved | DS design/story-film-sound.md:138 | sound/voice, runtime |
| S-12 | Use one key across the film's music themes so live pitched cues can match later. | proposal, not approved | DS design/story-film-sound.md:120 | sound/voice |
| S-13 | ElevenLabs notes as read on 2026-10-12: Voice Design from a text prompt (no sound-effect words in the prompt), text-to-speech with short takes picked by ear, sound effects of 0.1 to 30 s (layer 3 takes for a heavy hit), music from prompts. Its audio-tag list was not verified. | proposal, not approved | DS design/story-film-sound.md:80-85 | sound/voice |
| S-14 | A listening-test plan was written: phone, headphones, mono sum, loudness, A/B of voice models, hand-off played 10 times on a phone, and an owner tone check. None was run. | proposal, not approved | DS design/story-film-sound.md:159-169 | sound/voice, owner gate |
| S-15 | Brief sound with what is on screen and when (shapes, timing, weight); the sound designer chooses the sounds. The owner set this for effects; the same chain applies to a film brief. | owner decision | D-286 (decisions.md:223) | sound/voice, plan |

## 6. Runtime and delivery

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| V-01 | Proposed hybrid: scenes that do not need the player are pre-rendered in Blender as one video; scenes that must end on the player's own character stay live so play starts without a cut. It replaced "all live". D-183 assumes a video exists, but the split point and the fallback are still agent proposals. | proposal, not approved | DS design/story-opening-cutscene.md:66; D-147, D-183 (decisions.md:157,193) | runtime, plan |
| V-02 | The last shot lands on the player's own character and pulls back into the gameplay camera. The owner set the player's role (each player is one of the characters in the final group shot); the camera move was a proposal. | owner decision | D-148, D-149 (decisions.md:158-159); DS design/story-opening-cutscene.md:58 | runtime, plan |
| V-03 | Format proposed: 1920x1080, 16:9, 24 fps, `.mp4`, EEVEE with Standard view transform. Docs: `.mp4` or `.mov`, up to 4096x2160, up to 5 min, under 3.75 GB; alpha channels are ignored. 24 fps gives 20% fewer frames than 30. | proposal, not approved | DS design/story-film-plan.md:30-32; DS external/roblox-creator-docs/ui/video-frames.md:23-27 | delivery |
| V-04 | Upload facts: each video upload costs 2,000 Robux, up to 20 uploads a day; uploader must be 13+ ID verified; the video upload was a beta feature. The plan proposes one upload after final approval, done by the owner. | proposal, not approved | DS design/story-film-plan.md:21,35; DS external/roblox-creator-docs/ui/video-frames.md:17-29 | delivery, owner gate |
| V-05 | No paid test upload. The owner's reasoning: if video sound failed, the game could play the soundtrack itself. The sound plan's proposed 5 s test upload was declined. | owner correction | D-183 (decisions.md:193); DS design/story-film-sound.md:156-157 | delivery, sound/voice |
| V-06 | The docs list container, resolution, length and size but nothing on the audio codec; AAC-LC, 48 kHz stereo, 192 kbps was only a common default. With no test upload, whether video audio plays in Roblox stays unverified. | open | DS design/story-film-sound.md:136 | delivery, sound/voice |
| V-07 | Risk: a long video on low-end phones was not verified; fallback is all live. The plan says "test on a phone before upload", but Roblox VideoFrame playback needs an uploaded asset, so under V-05 only the file itself can be checked on a phone. This conflict is my inference. | open | DS design/story-film-plan.md:36,21; DS design/story-opening-cutscene.md:66 | delivery, runtime |
| V-08 | Playback facts: a `VideoFrame` must sit in a ScreenGui, SurfaceGui or BillboardGui; at most two videos play at once; in a ScreenGui the volume is the same everywhere; `Volume` is 0 to 100 with an undocumented default; audio is baked, with no stem control during playback. | proposal, not approved | DS external/roblox-creator-docs/ui/video-frames.md:34; DS design/story-film-sound.md:137 | runtime, delivery |
| V-09 | Set film assets at the game's real scale (a fixed Blender-units-per-stud import) so the game's own build style can be reused live, and plan sets for reuse in several scenes (for example the same set in a changed state). | proposal, not approved | DS design/story-film-plan.md:6,64 | plan, boards, runtime |

## 7. What blocked progress

| ID | Lesson | Certainty | Trace | Applies to |
| --- | --- | --- | --- | --- |
| X-01 | The boards could not start: most of the cast, set, props and face kit were missing, and the set had to be built first (D-183). Check asset readiness against the shot list on day one. | open | DS design/story-film-plan.md:57-70; D-183 | plan, boards |
| X-02 | Rig quality cost several rounds in two days: fused limbs, a creased neck, lumpy shoulders on variants, one face on every character, and wrinkled arms when posed. The owner rejected the output each time (R-01, R-03, R-04). | owner correction | D-160, D-185, D-186 (decisions.md:170,195,196) | acting/rig |
| X-03 | A long rig rebuild was lost when the agent hit its usage limit and nothing was saved. Split long rebuilds into saved steps. | proposal, not approved | DS logs/2026-10-12-opening-film-rigs.md:26 | acting/rig, plan |
| X-04 | Content left undecided held up voice, mouth shapes and shots: the key spoken line, all names, what one shot shows, and what a prop is. Put these in the brief as owner questions with a recommended default, and decide the key line early (it needs a mouth shape and a later live scene). | open | DS design/story-opening-cutscene.md:65; DS design/story-film-plan.md:80-81; DS design/story-film-sound.md:151 | plan, sound/voice, owner gate |

## Read, no universal lesson

| ID | Why not used as a row |
| --- | --- |
| D-149 (look part) | The material look of one story element is game-specific; only the player-role part is used (V-02). |
| D-145 to D-146, D-154, D-156 to D-159, D-162, D-165 to D-166, D-168 to D-179, D-182, D-187 to D-203, D-205, D-208, D-260 | Read in the range D-145 to D-290; they concern stages, economy or build rules and hold no film content. |
| D-283, D-285, D-287 to D-290 | Effects pipeline and the test place; no film content. D-284 and D-286 are used above. |
| D-280 to D-282 | Studio Kit name and new agents; no film content. |

## Counts

| Certainty | Rows |
| --- | --- |
| owner decision | 22 |
| owner correction | 10 |
| proposal, not approved | 28 |
| open | 10 |
| Total | 70 |
