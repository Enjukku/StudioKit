---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J005-T04, Animator_Research_Paper.txt lines 1-541
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Animation paper part 1: evidence rules, 15 operating rules, great animation, the body, game timing, loops, combat contract, face, cutscenes

Paraphrased notes on paper lines 1-541 (evidence rules, 15 operating rules, sections 1-8). Source IDs and dates are resolved from the paper's source register (AP:1146-1456 and the D/R entries it cites). The paper stays outside git. Nothing here was fact-checked: every number and every Roblox or Blender fact is listed in table CL; every conflict and scope limit is in table LM. Paper lines 542-1145 (Blender/MCP workflow, timing library and the rest) belong to another note.

## 0. How to read

| Key | Meaning |
| --- | --- |
| AP:n | Line n of `Animator_Research_Paper.txt` (AP = animation paper). A range means the lesson spans those lines. |
| Tag | Evidence tag copied from the paper: VERIFIED, EXPERIENCE, OPINION, UNSPECIFIED, UNKNOWN, NOT APPLICABLE. Combined tags are kept as the paper wrote them. |
| Src | Paper source ID. P00 is the paper's own protocol (OPINION, dated 2026-10-21), not an outside source. Resolved list in section 1. |
| Stage | Workflow stage from `knowledge/jobs/J005-character-rigger/workflow.md`: S0 intake, S1 motion needs (animator), S2 rig plan (rigger), S3 geometry (modeler), S4 geometry acceptance (rigger), S5 rig + tests (rigger), S6 rig acceptance (animator), S7 animate and export (animator), S8 owner final. |
| [for-rigger] | The rigger must know it or must supply or support something. A column "rig read" or text after the flag says what. Rig-read entries marked (inf.) are the extractor's reading of the row, not paper text. |
| IDs | EV evidence rules, OR operating rule, GA great animation, PR principle, CA case, BO body, BP body-part row, SP species family, TP motion-profile field, PF filled profile, RF reference protocol, GT game timing, SY stylization, SL sets and loops, CT combat contract, FS face and secondary, CS cutscenes, RG rigger digest, CL claim to check, LM contradiction or limit. |

Global caveats the paper states about itself: no embedded video was played or frame-counted (AP:79); the complete foundation books were not read (AP:171); no animation or performance benchmark was created (AP:1148). "Undated" in the register means no trustworthy date was found; it does not mean 2026.

Number discipline used in this file: values are copied with unit, source, date and tag; fractions such as 100/3 ms stay as written; no UNSPECIFIED field was filled.

---

## 1. Source register extract (IDs used in AP:1-541)

All register entries were checked by the paper on 2026-10-21 (AP:1148). Where the register tag differs from the tag the body text gives, the row says so and the conflict is in LM.

| Src | What it is (short) | Date (register) | Register tag | Used for |
| --- | --- | --- | --- | --- |
| P00 | Paper's own studio protocol | 2026-10-21 | OPINION | all protocol rules |
| C01 | Frank and Ollie author site, principles page | undated | EXPERIENCE (body text calls it VERIFIED, see LM01) | twelve principle names |
| C02 | Ollie's animation notes (Frank and Ollie site) | 1994 | EXPERIENCE | 4-frame and 6-8-frame advice |
| C03 | Principles of emotion in animation (same site) | 2003-06 | EXPERIENCE | "can the audience tell what the character thinks" |
| C04 | Riot art-education page, character animation | undated | EXPERIENCE | strong poses as the base |
| C05 | Riot, "Clarity in League" | 2021-03-12 | EXPERIENCE | silhouette, facing, hitbox consistency |
| C06 | Riot, VALORANT weapon-skin craft | 2020-05-18 | EXPERIENCE | skins mirror base weapon beats |
| C07 | Riot, how the VALORANT arsenal was built | 2020-05-12 | EXPERIENCE | beats show weapon state |
| C08 | SyncSketch interview, Alexis Wanneroy (Arcane, Fortiche) | 2021-12-08 | EXPERIENCE (vendor-hosted first-person testimony, AP:1200) | boards, layout, restrained acting |
| C09 | Valve, illustrative rendering in TF2 | 2007 | VERIFIED | nine-class silhouette test |
| C10 | Blizzard, WoW patch 7.3 combat animations | 2017-08-16 | EXPERIENCE | caster overhaul |
| C11 | Pixar, hair emoting with style guides, Turning Red (SIGGRAPH) | 2022-08 (SIGGRAPH Aug 7-11, 2022; a May 2022 version is also indexed) | VERIFIED (partial paper) | art-directed fur |
| C12 | Naughty Dog, Uncharted 4 5-year retrospective | 2021-05-10 | EXPERIENCE | duel without prompts |
| C13 | Nintendo, Ask the Developer vol. 11 (Mario Wonder) | 2023-10-17 | EXPERIENCE | sound sync, view-dependent distortion |
| C14 | GDC 2013 slides, Fortnite shader-based procedural animation (Lindquist) | 2013-03 | VERIFIED | procedural wall build |
| C15 | GDC 2019 slides, Spider-Man faces | 2019-03 | VERIFIED | neck jiggle, jowl blendshape, engine check |
| C16 | Blizzard, Hearthstone developer insights | 2018-10-26 | EXPERIENCE | effects had to fit fixed timing |
| C17 | GDC 2016, Overwatch "Play by Sound" | 2016-03 | VERIFIED | gameplay-priority audio |
| C18 | GDC 2017 bootcamp abstract, first-person Overwatch animation | 2017 | VERIFIED in register; body text calls it EXPERIENCE abstract only (LM02). Register: page fetch timed out | McCree 45-frame question |
| C19 | Substance magazine, Supercell Helsinki | 2019-11-22 | EXPERIENCE | visual development only |
| C20 | Disney Animation, Encanto process page | undated | VERIFIED | 24 fps basis |
| C21 | Williams, The Animator's Survival Kit, expanded Faber paperback | 2009-11-05 | VERIFIED | book metadata |
| C22 | Cooper, Game Anim, 2nd ed., CRC | 2021 (copyright year) | VERIFIED | book metadata |
| C23 | Thomas and Johnston, The Illusion of Life, Disney edition | 1995-10-19 (original work 1981 per author bibliography) | VERIFIED | book metadata |
| B01 | Animation Mentor, body-mechanics shot tips | 2014-07-14 | EXPERIENCE | "what moves first, why, what next" |
| B02 | Animation Mentor, follow through and overlapping action | 2017-06-19 | EXPERIENCE | passive tail exercise |
| B03 | Animation Mentor, weight and force, lifting a heavy object | 2025-11-14 | EXPERIENCE | heavy-lift teaching |
| B05 | Gecko active tails | 2008-03-17 | VERIFIED | active tail |
| B06 | Pigeon takeoff and landing kinematics | 2010-05-15 | VERIFIED | whole-body flight transitions |
| B07 | Bat aerial rotations by wing inertia | 2015-11-16 | VERIFIED | asymmetric retraction |
| B08 | Bat upstroke wing flexion, inertial cost | 2012-04-11 | VERIFIED | fold cost (six species spanning a 40-fold body-mass range, register key line) |
| B09 | Honeybee short-amplitude high-frequency wing strokes | 2005-12-05 | VERIFIED | insect wing is its own system |
| B10 | Common swift gliding | 2011 | VERIFIED | wing shape changes with airspeed |
| B11 | Horse gait classification | 2007-01-15 | VERIFIED | symmetric / asymmetric gaits |
| B12 | Drosophila tripod gait | 2021-02-03 | VERIFIED | modified tripod, fixed-speed forward only |
| B13 | Spider Grammostola mollicoma octopedal locomotion | 2011-10-15 | VERIFIED | anterior pairs alternate, posterior do not |
| B14 | Mechanics of slithering locomotion | 2009-06-08 | VERIFIED | snake friction model |
| B15 | African lungfish, viscosity and axial pattern | 2008 | VERIFIED | undulation depends on medium |
| B16 | Cat pinna movements during sound localization | 1998-06-01 | VERIFIED | ears move independent of head |
| B17 | Stick-insect antennae, active tactile exploration | 2011 | VERIFIED | antenna context dependence |
| B18 | Bluegill sunfish dorsal and anal fins | 2005-07-15 | VERIFIED | fin ray curvature differs base to tip |
| B19 | Disney technical animation, character effects | undated | EXPERIENCE | secondary animation is authored |
| B20 | Disney, choreography of hair and cloth | 2025 | EXPERIENCE | continuity, planning, iteration |
| B21 | Hammer mass and upper-extremity joint moments | 2017-04 | VERIFIED | nail-driving study |
| B22 | NASA STEMonstrations, moment of inertia | undated | VERIFIED | mass distribution and rotation |
| B23 | Body size and lower-limb posture in walking | 2017-02-13 | VERIFIED | phase-dependent gait relations |
| B24 | The condition for dynamic stability | 2005-01 | VERIFIED | inverted-pendulum stability model |
| B25 | NASA, what is microgravity | undated | VERIFIED | weightless is not massless |
| D04 | Blender 5.0 Python API release notes | Blender 5.0 released 2025-11-18; notes page undated | VERIFIED | legacy Action API removed |
| D35 | Blender manual, Output Format | undated, shows 5.2, accessed 2026-10-21 | VERIFIED | scene fps = fps / fps_base |
| R18 | Roblox docs, MicroProfiler | undated | VERIFIED | profile on the mobile client |
| R28 | Roblox docs, Animation capture | undated | VERIFIED | capture limits |
| R29 | Roblox docs, dynamic head tutorial | undated | VERIFIED | fewer than 50 face joints |

---

## 2. Evidence and number rules (AP:5-17)

| id | rule (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| EV01 | Purpose: train an animator agent to understand the whole articulated subject, build purposeful motion in Blender, move it to Roblox, and reject a good-looking result that fails gameplay, rig integrity or device cost. The owner is creative director; the animator proposes, measures, revises. A numerical score never replaces creative approval. Evidence stated as current through 2026-10-21. | all | | OPINION P00 | AP:5-7 |
| EV02 | Main conclusion: good animation rests on cause and effect the viewer can follow (what is intended, what pushes, what supports, what happens, what results). Adding keys, bones, procedural noise or generated clips does not build that chain by itself. Work in this order: motion model first, performance second, verified runtime asset last. | S1, S7 | | OPINION P00 | AP:9 |
| EV03 | Tag meanings. VERIFIED = an official spec, a direct measurement, or an exact conversion of named source data; a platform limit that is VERIFIED is still not a suitable production budget. EXPERIENCE = a studio, animator or tool maker describes its own practice or result; a vendor's own benchmark is not an independent comparison. OPINION = this paper's protocol or an artistic recommendation. Source IDs resolve to dated URLs with short key lines in the register. | all | | OPINION P00 | AP:13 |
| EV04 | UNSPECIFIED = source publishes no such number. UNKNOWN = the production has not measured it. NOT APPLICABLE = field does not describe the action. They differ on purpose. A missing research number (UNSPECIFIED) does not stop production. Within the approved brief the animator can: author timing and say so, measure a fitting reference, render alternatives side by side, and log what was accepted. The owner signs off on creative direction and costly trade-offs, not on each key or joint offset. A choice made for this project is never to be passed off as an industry fact. Four different quantities are never exchanged: animal observation ranges, cinematic shot lengths, engine capacities, and a character's own gameplay window. | S1, S7 | | OPINION P00 | AP:15 |
| EV05 | Exact frame arithmetic. Seconds = source frames / source frame rate. Frames at 30 fps = seconds x 30; at 60 fps = seconds x 60; milliseconds = seconds x 1000. A single 30 fps interval equals 100/3 ms, which is also two 60 fps intervals; do not write it as 33 ms. Poses on frames 1 and 31 are 30 intervals apart. Fractions stay as fractions; rounding is a separate, logged editorial decision. A count such as 45 frames with no stated rate has no seconds or 30 fps equivalent. | S7 | | VERIFIED exact arithmetic; OPINION reporting protocol P00 | AP:17 |
| EV06 | Foundation books: use lawful copies; record exact edition and page before adopting an exercise. The public author source C01 independently backs the twelve principle names. No page-specific exercise or timing is attributed to unseen books. | S1 | | OPINION P00 | AP:171 |
| EV07 | The register's general limit: official documentation establishes the documented claim, not that it runs on this studio's assets. EXPERIENCE reports are attributed, not reproduced. Videos were not frame-measured. | all | | OPINION P00 | AP:1148 |

---

## 3. The fifteen operating rules (AP:19-49)

| id | rule (paraphrased) | stage | rigger | tag / src | AP | rig read / note |
| --- | --- | --- | --- | --- | --- | --- |
| OR01 | Before adding detail, make sure a viewer can read the intention, the support, the force and the consequence. | S1, S7 | | OPINION P00 | AP:21 | |
| OR02 | Creative sign-off belongs to the owner; no model score stands in for it. | S8 | | OPINION P00 | AP:23 | |
| OR03 | Name what every body part is before it is moved. A bone's name hints at anatomy but does not prove it. | S1, S2 | [for-rigger] | OPINION P00 | AP:25 | Rigger supplies identity of parts and answers the animator's questions on ambiguous or absent structure (see BO01, BO02). |
| OR04 | Rig geometry may be measured; physical mass and species may not be deduced from shape alone. | S1 | [for-rigger] | OPINION P00 | AP:27 | Rig sheet records measured lengths in a declared unit; mass stays UNKNOWN unless supplied (BO03). |
| OR05 | Keep actively driven motion apart from passive follow-through; geckos show that a tail can really steer and re-orient the body. | S1, S2, S5 | [for-rigger] | VERIFIED B05; OPINION protocol P00 | AP:29 | A tail or other appendage may need to be driven as a primary part, not only trail the body (BP06, BP07, SP03). |
| OR06 | Show contacts and weight shifts explicitly in the animation instead of masking foot slide by cutting the camera. | S1, S6, S7 | [for-rigger] | OPINION P00 | AP:31 | Rig must let the animator hold and release each contact (foot, hand, grip) so contact state is reviewable (BP05, RG09). |
| OR07 | Judge the animation in the view the player will really have, and protect silhouette recognition. | S1, S6, S7 | | EXPERIENCE C05; OPINION review P00 | AP:33 | |
| OR08 | Gameplay windows live in authoritative time; animation, effects, audio and UI all read the same event contract. | S7 | | OPINION P00 | AP:35 | Matches `workflow.md` section 5 timing list. |
| OR09 | Keep the original frame rate and the phase definitions on record before any timing conversion. | S7 | | VERIFIED exact arithmetic; OPINION P00 | AP:37 | |
| OR10 | Do not promote an unpublished anticipation length or joint delay to an industry norm. | S1, S7 | [for-rigger] | OPINION P00 | AP:39 | Any rig-side delay, spring or lag setting is a project choice labeled OPINION (SP03, FS05). |
| OR11 | Pin tool versions. In Blender use the current slot / channelbag action structure; Action.fcurves access is gone. | S5, S7 | [for-rigger] | VERIFIED D04; OPINION versioning P00 | AP:41 | Rig tooling and the rig sheet record the Blender version; scripts must not use the removed API. Fact-check CL05. |
| OR12 | Ship only the motion the engine needs: not the full control rig, not every in-between key. | S5, S7 | [for-rigger] | OPINION P00 | AP:43 | Export skeleton stays separate from the control layer (fits `workflow.md` S5 control manifest + export skeleton). |
| OR13 | A platform importer ceiling is one thing, a measured phone budget another; profile on the mobile client. | S2, S5, S7 | [for-rigger] | VERIFIED R18; OPINION budget protocol P00 | AP:45 | A platform limit is not a phone budget (`workflow.md` section 6). |
| OR14 | Generated motion counts as reference or a candidate take only, until it clears contact, retargeting and runtime reviews. | S7 | | OPINION P00 | AP:47 | |
| OR15 | Deliver a single traceable asset together with its profile, timing sheet, review evidence, budget measurements and open questions. | S7, S8 | [for-rigger] | OPINION P00 | AP:49 | The rig sheet is the rigger's part of that trace. |

---

## 4. Section 1: what makes great animation (AP:51-178)

### 4.1 Frame of the section

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| GA01 | Good animation puts one specific intention across using shape, timing and force. The twelve principles name things to diagnose with; they are not a setting to turn up everywhere. These must agree in the camera the player gets: pose, silhouette, line of action, attention, weight, contrast, personality. The owner picks the intended reading; the cases below record how other studios handled specific problems. | S1, S6, S7 | | OPINION P00 | AP:53 |
| GA02 | Two review questions are complementary: is the pose strong (poses are the base of the animation, C04), and does it show what the character is thinking (C03)? Readable and meaningful are separate tests. | S6, S7 | | EXPERIENCE C04, C03 | AP:55 |
| GA03 | The twelve names come from the authors' site (C01). The application column is the paper's own modern training synthesis, neither a quotation nor a studio rule. Pushing all twelve hard in every shot is wrong. The site's index adds a parenthetical to Solid Drawing equating it with Weight; that is an explanation, not a thirteenth principle. These are craft choices, not a numeric preset. | S1, S7 | | VERIFIED C01 (names, tag conflict LM01); OPINION P00 (application) | AP:59, 75 |

### 4.2 Twelve principles, conditional application (AP:61-73)

| id | principle | conditional application (paraphrased) | rig note | AP |
| --- | --- | --- | --- | --- |
| PR01 | Squash and stretch | Use to clarify force or emotion, never to break contact truth. | [for-rigger] only where the rig and asset contract allow it (SY03). | AP:62 |
| PR02 | Anticipation | Signals intent; keep any authorized input-response constraints. | | AP:63 |
| PR03 | Staging | Make the current decision or thought legible. | | AP:64 |
| PR04 | Straight ahead and pose to pose | Mix free exploratory passes with planned key poses. | | AP:65 |
| PR05 | Follow through and overlapping action | Let subordinate masses settle after the main action. | [for-rigger] needs parts that can lag (chains, accessories). | AP:66 |
| PR06 | Slow in and slow out | Shape spacing deliberately; leave out softness when snap matters. | | AP:67 |
| PR07 | Arcs | Inspect trajectories, including camera-projected paths. | | AP:68 |
| PR08 | Secondary action | Must support the main idea; remove competing business. | | AP:69 |
| PR09 | Timing | Spend emphasis and contrast around the protected events. | | AP:70 |
| PR10 | Exaggeration | Strengthen the intended reading, not every amplitude. | | AP:71 |
| PR11 | Solid drawing | In 3D keep volume, balance and convincing form. | [for-rigger] deformation must keep volume. | AP:72 |
| PR12 | Appeal | Distinctive, readable character; cuteness is not required. | | AP:73 |

### 4.3 Ten production cases (AP:79-161)

The paper warns the cases have different evidence depth (production accounts, technical talks, rigging demos); none was frame-counted. Each row keeps the transfer lesson and the "do not copy" point; franchise detail that teaches nothing is dropped. All case timings below are UNSPECIFIED except where a structural count or presentation parameter is listed.

| id | case / src / date / tag | what the source reports (short) | transfer lesson (OPINION P00) | do not copy | timing status | stage / flag | AP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CA01 | Lee Sin vs Ivern; C05; 2021-03-12; EXPERIENCE | Recognition in some characters comes mostly from shape, in others animation must carry more: a lanky model with a characteristic walk versus a comparatively generic shape. The article also counts facing direction and agreement with gameplay hitboxes as clarity jobs. No gait timing or joint curves published. | Identity can live in movement: give an original character a clear body-weight placement, stance width, limb rhythm and a habitual lean toward one direction. Test recognition as a silhouette at the real camera distance and size. Carry those cues through turns, transitions and cosmetic variants. | Specific poses or walk. | UNSPECIFIED (clarity account, not locomotion measurement) | S1, S6, S7. [for-rigger]: rest stance, facing axis and hitbox-consistent forward axis must support these cues (inf.). | AP:81-87 |
| CA02 | Reaver Vandal reload (weapon skin); C06 2020-05-18, C07 2020-05-12; EXPERIENCE | A skin keeps the base weapon's animation beats and perceived readiness. Key sound events (such as ammunition insertion) stay aligned with gameplay; added cosmetic sound must not hide essential cues. Playtests check feel and obstruction. Arsenal article: two- or three-beat equip/reload patterns tell the player the weapon state. | Lock the protected readiness and ammunition events before designing flourish. Test base and variant under the same input, camera and audio. A float, snap or fancy hand path may add personality but must not suggest the weapon is ready sooner or later than it is. | The signature treatment. | Beat timestamps and durations UNSPECIFIED; two/three beats are structural counts only | S7 | AP:89-97 |
| CA03 | Arcane Jinx; C08; 2021-12-08; EXPERIENCE (vendor-hosted interview) | Season 1 keyframed from substantial live-action reference, not motion capture. Detailed boards set composition, camera and poses; layout preserves them so animators focus on acting and mechanics. Expression is toned down, head and body angles carry the thought. Subjective scratches are 2D over CG plates. Expression and pose libraries plus before/after comparison protect consistency. | Separate intention, bodily performance and the subjective graphic layer. First test that pose and gaze carry the thought without decoration. Add graphic interruptions only where they make the viewpoint or an emotional break clearer. Keep the reference's intention, not every incidental move. | Jinx's scratch vocabulary mistaken for the acting discipline. | UNSPECIFIED (process account, no shot breakdown) | S1, S7. [for-rigger]: pose and expression libraries are a face/body vocabulary the rig should be able to hold (inf.). | AP:99-105 |
| CA04 | TF2 nine-class silhouette system; C09; 2007; VERIFIED document | The nine classes were checked as plain black shapes with no interior detail. Proportions, weapons and clothing keep them apart, and inner shapes support the outer contour. Evidence about recognition and rendering, not animation curves. | A pose can wipe out a body distinction that mattered: a weapon laid across the torso, a mirror-symmetric idle or a hard twist may merge the outline into a blob. Compare pose families, transitions and attack extremes with one another, not only one showcase stance. | A supposed universal gait, smear or timing formula. | UNSPECIFIED (silhouette figure discussed in text, pixels not measured) | S6, S7. [for-rigger]: extreme twists and weapon-crossing poses are the rig-limit stress cases. | AP:107-113 |
| CA05 | WoW 7.3 caster overhaul; C10; 2017-08-16; EXPERIENCE | Designers kept gameplay and improved feel. Cast animations of different races now reach the casting pose in more evenly matched time yet keep their identity. Precasts gather energy instead of looping. Instant casts gain one-handed variants usable during movement. A straight-armed cast and a wrist-flick curse read as different amounts of effort. Arcane Missiles keeps five bursts of four missiles. | Anticipation is information and perceived effort, not automatically input delay. Separate cast preparation, authoritative release, locomotion compatibility and recovery. Move visible effort around protected gameplay events instead of stretching the action. Keep class personality apart from event timing. | The exact gesture or visual signature. | Cast-pose interval and phase durations UNSPECIFIED; 5 bursts x 4 missiles = event structure, not cadence or duration | S7 | AP:115-121 |
| CA06 | Turning Red fur; C11; 2022-08; VERIFIED (partial paper) | Art-directed fur reflects emotion. Sparse style guides let artists sculpt expressive groom poses and propagate them to the whole hair system; animation, simulation and constraints cooperate. Shows controllable emotional fur exists; says nothing about exact dynamics settings. | Decide what a fur or cloth change says before simulating. A secondary silhouette can support expansion, withdrawal or tension but must not hide the face or contradict the main body beat. Review the emotional pose and the return to rest. | The panda shape or an assumed noise recipe. | UNSPECIFIED (full paper and film shots not frame-inspected) | S1, S7. [for-rigger]: fur/cloth that acts must be controllable (bones or driven shape), see FS05. | AP:123-129 |
| CA07 | Uncharted 4 final duel; C12; 2021-05-10; EXPERIENCE | On-screen quick-time prompts were swapped for blocking in a direction the player works out from the opponent's motion; the scene also shows the hero out of his depth. A different passage of the same retrospective notes that animation-driven AI traversal has to pick its following action early so the current one can end cleanly. | Make the attack's relevant direction visible ahead of the player's decision point, without making up where that point is. Show intent, skill and effort differently (same contact, different performer). Review with the UI hidden to see if the cue still works. | Character mannerisms, or a fabricated cancel window. | Startup, block window, impact, recovery UNSPECIFIED; no frame-accurate breakdown | S7 | AP:131-137 |
| CA08 | Mario entering a pipe (Wonder); C13; 2023-10-17; EXPERIENCE | Once a new action was added before entering a pipe, the old sound tied to the button press felt out of step, so the sound was retimed. Face and body are bent on purpose for the play camera so travel direction and expression both stay readable. Enemy Goombas pull a biting face at the moment of damage. | Attach a sound to the meaning-bearing event it represents; an old input timestamp may no longer be right. A cheat that works only from the real camera is fine if it helps that view and does not misrepresent gameplay. Judge action, sound and damage feedback as one package. | Mario's distortion or jump pose. | Pipe-entry offset and bite duration UNSPECIFIED (development examples, clips not measured) | S7. [for-rigger]: view-dependent distortion is a rig/asset-contract question (see SY03). | AP:139-145 |
| CA09 | Fortnite 2013 assembling plank wall; C14; 2013-03; VERIFIED presentation | Construction pieces are animated by a spline-driven material. Artists wanted to set the order in which pieces show up. Eased rotation plus a separate drag effect shape the movement. The sample wall has 46 pieces. The GPU only bends the visuals; collision is left untouched. | Procedural motion still needs chosen sequencing, a readable arrival and a clear end state. Drag should explain travel and settling, not add ornamental wobble. Check real collision on its own, apart from what a shader appears to move. Keep art-directed choreography and gameplay geometry separate. | The 2013 wall's build effect. | Spline sampled at 1 X-unit per second = that slide system's parameterization, not a modern Fortnite build time, sim rate or network tick; other phases UNSPECIFIED | S7. Links to prop checklist (SL06). | AP:147-153 |
| CA10 | Spider-Man Kingpin; C15; 2019-03; VERIFIED presentation | Face-rig slides include neck jiggle and a jowl blendshape for the Kingpin. The pipeline matches facial poses to scans, then looks at the result in the engine; mesh or triangulation changes can spoil it after export. These are rig and review examples, not a shot-by-shot account. | Set the intended head, jaw and neck pose first; then layer secondary motion that sells mass but does not cover speech or where the character looks. Review the asset as delivered in the engine, not just the playblast from the animation tool. A working technical rig gives acting vocabulary; it does not prove a good performance. | Kingpin's face or proprietary deformation settings. | Jiggle parameters, facial offsets, shot durations UNSPECIFIED | S5, S6, S7. [for-rigger] yes: engine round trip, triangulation after export, bone plus shape support for neck/jowl. | AP:155-161 |

### 4.4 Coverage gaps, books, section summary

| id | item | detail (paraphrased) | tag / src | AP |
| --- | --- | --- | --- | --- |
| GA04 | Overwatch GDC 2017 abstract | Poses the McCree revolver-reload problem as 45 frames; gives no frame rate and no phase breakdown; not proof of a shipped duration. Register: direct page fetch timed out. | EXPERIENCE (body) / VERIFIED (register), C18, 2017 | AP:165, 1260-1264 |
| GA05 | Supercell interview | Covers stylized look development and team feedback; it measures no attack timing. | EXPERIENCE C19, 2019-11-22 | AP:165 |
| GA06 | Deadlock | The paper found no solid first-party action breakdown for it; TF2 is an earlier Valve example and says nothing about Deadlock's own pipeline. | OPINION P00 | AP:165 |
| GA07 | Book: Animator's Survival Kit | Williams; expanded Faber paperback 2009-11-05; ISBN 9780571238347; publisher notes added animal action, invention, realism material. | VERIFIED C21 | AP:169 |
| GA08 | Book: Game Anim | Cooper; CRC 2nd ed.; copyright 2021; 350 pages; ISBN 9780367707651; expanded motion-capture and motion-matching coverage. | VERIFIED C22 | AP:169 |
| GA09 | Book: Illusion of Life | Thomas and Johnston; Disney edition 1995-10-19; 576 pages; ISBN 9780786860708; bibliography dates the original work to 1981. | VERIFIED C23 | AP:169 |
| GA10 | Books not read | Only publisher/author metadata is verified. | OPINION P00 | AP:171 |

Paper's own summary table for section 1 (AP:173-178):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Foundational principle vocabulary | 12 conventional principles | VERIFIED names; OPINION application | C01; undated author site; checked 2026-10-21 |
| Distinct production cases | 10, evidence-depth differences disclosed | EXPERIENCE and VERIFIED documents | C05-C15; register dates |
| Readability and weapon readiness | protected event beats; exact durations UNSPECIFIED | EXPERIENCE | C05-C07; 2020-2021 |
| Caster event structure | 5 bursts x 4 missiles; cadence UNSPECIFIED | EXPERIENCE | C10; 2017-08-16 |
| McCree reload design problem | 45 source frames; source FPS UNSPECIFIED | EXPERIENCE abstract only | C18; GDC 2017 |

---

## 5. Section 2: understand the body before setting keys (AP:180-345)

### 5.1 Inventory, balance, views (AP:182-198)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| BO01 | Before touching channels the animator builds a model of the subject from the brief, approved design, rig contract, deformation limits and intended camera. For each visible part note what it is, what carries it, whether it bends, and what movement is meant. Unclear or missing structure goes to the rigger as a question before any motion is made. Three similar shapes (decorative fin, steering fin, rigid armor plate) may need three different behaviors. | S1 | [for-rigger] rigger answers these questions; supports K1 "every visible part has a row, also 'does not move'". | OPINION P00 | AP:184 |
| BO02 | Each rig element keeps its original ID plus its own meaning label. Fields to store: parent, children, rest transform, local axes, deform status, constraints, IK participation, mesh influence, geometry extent, intended pivot, allowed motion, confidence. An item named tail_03 stays a guess at a tail segment until hierarchy, rest geometry, bindings and several camera views all agree. Helper bones and control shapes are not by default body parts, and the root control is not by default the pelvis. | S1, S2 | [for-rigger] | OPINION P00 | AP:186 |
| BO03 | Length is a geometry fact: take endpoint positions in a stated coordinate system and unit. Mass is a physical quantity that needs given material density and volume assumptions or reference/rig metadata. A bounding box is not mass, a long bone is not automatically heavy, and the count of vertices weighted to a joint is not inertia. Write UNKNOWN rather than guess kilograms. A felt sense of weight is acceptable only as a stated artistic choice in the profile. | S1 | [for-rigger] | OPINION P00 | AP:188 |
| BO04 | Support and balance are working guesses. Mark the planted contacts, outline the support area, and project a center-of-mass stand-in into the scene. A pelvis stand-in is useful in review but is not the real whole-body center of mass, particularly when a large tail, wings or tool is present. A pose outside the support area can be explained by momentum, a second contact, lift, or a chosen stylized break. Not every airborne pose is off balance. | S1, S6, S7 | [for-rigger] large tail, wings and tools shift the true center of mass (inf.) | OPINION P00 | AP:190 |
| BO05 | Views to inspect: front, back, both sides, raised three-quarter, underside where it matters, the gameplay camera, and joint-limit poses. Tools: a turntable with labeled rig overlays, a silhouette render without lighting, and a clear view of the bare mesh. Save the camera transforms so later checks match framing. Render the extremes of shoulder raise, hip bend, spine twist, wing fold, jaw opening, tail curl and grip, wherever the subject has those parts. The list follows the anatomy and is not a required skeleton for everything. | S1, S6 | [for-rigger] these are the range-of-motion (ROM) extremes the rig must reach or declare as not reachable | OPINION P00 | AP:192 |
| BO06 | Two body-mechanics studies: a level-treadmill study of 49 non-obese adults found that how mass, limb length and posture relate depends on the gait phase, and that proportions did not account for all gait differences (B23, 2017-02-13). A stability model that includes center-of-mass velocity (B24, 2005-01) means a static projection over a planted foot cannot serve as a general locomotion test. Neither validates arbitrary creature balance. | S1 | | VERIFIED B23, B24 | AP:196 |
| BO07 | Ask which force starts and redirects the action and what leads next (B01, 2014-07-14). The takeaway is to work out the order for the action at hand, not to assert that hips always go first and the head always trails. | S1, S7 | | EXPERIENCE B01 | AP:198 |

### 5.2 Body-part behaviour table (AP:200-220), complete

Intro rule (AP:202): "typical frames" means a transferable production prescription; UNKNOWN there is intentional because the reviewed evidence gives no universal value. A measured latency, a gait phase and a camera capture rate are different quantities. The timing library (another note, lines 542-1145) holds measured context and exact conversions. Every "typical frames" cell below is UNSPECIFIED as the paper writes it, with the extra qualifiers kept.

| id | part | what drives it | delay / follow-through rule (paraphrased) | typical frames | tag / src | rig read [for-rigger] (inf.) |
| --- | --- | --- | --- | --- | --- | --- |
| BP01 | Whole-body / root motion | Intended travel, acceleration, braking, support, external impulses | The root path and the contact schedule have to match. The root control cannot be assumed to be the physical center of mass. | UNSPECIFIED | OPINION; dynamic-stability distinction B24 | Root control and a CoM proxy are different things. |
| BP02 | Pelvis, trunk, shoulders | Actuation, balance correction, load transfer, expressive pose | No blanket "hips first, head after" order for all actions. | UNSPECIFIED | EXPERIENCE B01 | No fixed lead order built into the rig. |
| BP03 | Neck and head | Gaze target, orientation, stabilization, deliberate reaction | Let the task drive the head instead of making it a lagging copy of the body at all times. | UNSPECIFIED | OPINION; no universal delay established | Head needs orientation freedom independent of the trunk. |
| BP04 | Arms, hands, carried prop | Reach, grip, leverage, intentional release, prop orientation | A fixed grip ties hands and object together, so check both hands and the object as one system. | UNSPECIFIED | OPINION; weight craft B03 | Prop sockets and grip anchors; both hands plus object solved together. |
| BP05 | Legs and feet | Stance, unloading, swing, touchdown, recovery | Note for each contact whether it is planted, rolling, sliding or let go. A skid done on purpose is not a foot-lock error. | UNSPECIFIED | OPINION; species gait evidence B11-B13 | Foot contact states and pivots that allow rolling and sliding. |
| BP06 | Passive tail or strap | Base acceleration, flexibility, damping, gravity, collisions | Lags and settles relative to the base it hangs from; what it is attached with changes the result. | UNSPECIFIED per joint | EXPERIENCE B02 | Chain with enough segments to follow through. |
| BP07 | Active tail | Counterbalance, support, steering, signaling, propulsion | A tail may initiate an action and alter how the body moves; it does not always just trail behind. | UNSPECIFIED per joint; whole-tail events are measured in the timing library | VERIFIED B05 | Needs controls that drive the tail as a primary part while the body responds. |
| BP08 | Bird-like wing and tail | Takeoff, cruise, braking, landing, folding, gliding | Stroke plane, body attitude and tail set-up must be handled together; flapping alone is not enough. | UNSPECIFIED generic cycle | VERIFIED B06, B10 | Wing, body and tail controllable together; fold and glide poses reachable. |
| BP09 | Bat-like wing | Wing extension, membrane geometry, flap, maneuver | Pulling in one wing more than the other can turn the body; folding changes the inertia. | UNSPECIFIED generic cycle | VERIFIED B07, B08 | Left and right wings need independent retraction. |
| BP10 | Insect-like wing | Species- and task-specific stroke amplitude, pitch, frequency | Very fast wingbeats call for a sampling or rendering plan, not an arbitrary slowed-down bird flap. | UNSPECIFIED generic cycle; honeybee example in timing library | VERIFIED B09 | Wing joint must allow stroke pitch and amplitude (stroke family chosen first). |
| BP11 | Mobile ears | Intentional orientation, sensory response, passive tissue motion | Ears can move before the head does; check whether left and right act separately. | UNSPECIFIED generic delay | VERIFIED cat experiment B16 | Separate left/right ear controls independent of the head. |
| BP12 | Antennae | Active search, object contact, passive deflection | Contact with an obstacle can change how the antenna samples and where the next leg lands. | UNSPECIFIED generic delay | VERIFIED stick-insect experiment B17 | Active and passive modes may both be needed. |
| BP13 | Hair, cloth, soft tissue, accessories | Attachment, stiffness, damping, wind, water, collision, art direction | Keep contact and silhouette intact; a single delay value for all materials does not fit. | UNSPECIFIED | EXPERIENCE B19, B20 | Per-material treatment; see FS05. |
| BP14 | Fish fins | Propulsion, maneuvering, braking, stabilization | Separate fins may do separate jobs, and the rays do not have to bend together like one stiff paddle. | UNSPECIFIED generic cycle | VERIFIED bluegill experiment B18 | Fins as separate control surfaces; ray curvature differs base to tip. |
| BP15 | Long axial body | Ground traction or fluid interaction plus a task-specific traveling wave | Treat body curve, travel of the body and muscle activation as three different things. | UNSPECIFIED generic wave / per-bone delay | VERIFIED snake and lungfish studies B14, B15 | Many segments; curvature and travel controlled separately. |
| BP16 | Mechanical hinge / piston / gear | Actuator, linkage, hard stop, structural flexibility | Hold the designed linkage; give it flex only if that was designed or observed. | UNSPECIFIED | OPINION, engineering design constraint | Hard stops and linkage in the rig. |

### 5.3 Species-conditioned motion families (AP:222-264)

| id | family | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- | --- |
| SP01 | Tail, passive regime | The article's pendulum exercise makes the tail passive on purpose, while the same text singles out a squirrel's tail as acting on its own. What the tail is made of and how tightly it is attached change the response. The exercise's "never lead" advice must not be promoted to a law about animals. | S1, S7 | [for-rigger] | EXPERIENCE B02 (2017-06-19) | AP:226 |
| SP02 | Tail, active regime | Flat-tailed house geckos (Cosymbotus platyurus in the study) braced on their tails against a wall after slipping, righted themselves in the air with them, and steered with them while descending. Rotating the tail actively could turn the body the opposite way without a required head-to-hips twist order. | S1 | [for-rigger] | VERIFIED B05 (2008-03-17) | AP:228 |
| SP03 | Tail implementation | Keep tail intent in a different record from the passive response. Passive tail: check the base path, continuity, how the bend is spread, the tip's arc and collision clearance. Active tail: plan the target direction and the body's coupled reaction first. A wave is a shape changing along the length and over time; it does not prove every bone trails the previous one by an equal number of frames. Many bones and uneven segment lengths make a fixed per-bone delay fragile. Use measured phase curves, or an openly authored style setting tagged OPINION if no reference exists. | S1, S2, S7 | [for-rigger] bone count and segment lengths of the tail chain; an intent control separate from the passive chain | OPINION P00 | AP:230 |
| SP04 | Bird wing | Pigeons flying between perches shifted body, tail and wing-plane orientation between takeoff and landing, and the rotations were correlated. Study takeoff and braking as whole-body actions. Not proof of the same angles or timing for other birds or dragons. | S1, S7 | [for-rigger] | VERIFIED B06 (2010-05-15) | AP:234 |
| SP05 | Bat wing | A landing study combined measured kinematics with a mass-distribution model: asymmetric wing articulation could account for much of the reorientation during low-speed landing / fall recovery, through inertia. A six-species study estimated that folding and unfolding costs energy but lowers the total inertial cost compared with an always-extended rigid wing. Bat wings are not interchangeable with near-massless insect wings. | S1, S7 | [for-rigger] | VERIFIED B07 (2015-11-16), B08 (2012-04-11) | AP:236 |
| SP06 | Gliding | Common-swift glide experiment: wingspan and wing shape changed with airspeed. Only one bird supplied the steady-glide data, a stated scope limit. A glide is not a frozen flapping pose. | S1, S7 | | VERIFIED B10 (2011) | AP:238 |
| SP07 | Flight planning states | Proposed state chain: ground/perch preparation, launch and contact release, accelerating flight, cruise or glide, approach and braking, contact and load acceptance, fold and rest. A bat-like creature has two separate reference tasks: landing on ground and roosting from a ceiling. An insect-like creature needs a real stroke family chosen before stylizing. A mixed dragon needs notes on which animal supplies which reference and where invention takes over. Never blend pigeon angles, bat roosting and bee frequency into one profile presented as measured. | S1 | [for-rigger] wing anatomy (feathered vs membrane vs insect) must be named before rigging | OPINION P00 | AP:240 |
| SP08 | Four legs | Footfall timing was measured over ground on eight ridden Icelandic horses in walk, trot, pace, tölt, canter and gallop, separating symmetric from asymmetric footfall patterns and left from right leads. The transverse canter and gallop results do not stand in for every four-legged animal or for rotary gallopers. | S1 | [for-rigger] | VERIFIED B11 (2007-01-15) | AP:244 |
| SP09 | Six legs | Drosophila walking straight at steady speed mostly used a modified tripod: R1-L2-R3 and L1-R2-L3, with small within-group offsets. The authors limit it to fixed-speed forward walking; turning and acceleration are not established. | S1 | [for-rigger] | VERIFIED B12 (2021-02-03) | AP:246 |
| SP10 | Eight legs | Spider (Grammostola mollicoma) shows speed-dependent coordination and different behavior for anterior and posterior leg pairs. A stylized alternating tetrapod is a starting hypothesis, not evidence that all eight-legged creatures use four perfectly synchronous feet. | S1 | [for-rigger] | VERIFIED B13 (2011-10-15) | AP:248 |
| SP11 | Multi-leg training record | Log, for every limb: contact state, touchdown position, stance fraction and normalized cycle phase. Also log the organism, speed range, surface and turn direction. While the body moves forward, check that stance feet stay put in world space; a walk cannot come from waving limb angles with no link between them. Machines with many legs may follow authored step schedules, as long as support and contact logic is spelled out. | S1, S6, S7 | [for-rigger] each leg needs its own contact record and a stable stance foot | OPINION P00 | AP:250 |
| SP12 | Slither | Friction of snake skin was measured and ground slithering modeled: how the body meets the ground and how its weight is spread both drive progress, so a moving sine-shaped outline alone does not account for the travel. | S1 | [for-rigger] | VERIFIED B14 (2009-06-08) | AP:254 |
| SP13 | Swim | African lungfish (Protopterus annectens) changed axial activation and kinematic relationships with viscosity; environment matters, so do not reuse the same swimming and ground wave assumptions. Muscle activation timing is not the visible bending curve. | S1 | | VERIFIED B15 (2008) | AP:256 |
| SP14 | Fins | In bluegill sunfish the dorsal and anal fin movement changed with maneuver and speed, with fin-ray curvature varying as well. Treat fins as possible steering surfaces, not as default decorative trailing. | S1 | [for-rigger] | VERIFIED B18 (2005-07-15) | AP:258 |
| SP15 | Weightless vs massless | NASA: microgravity is weightlessness, not loss of mass; a space-station demonstration shows changed mass distribution changes rotational response. | S1 | | VERIFIED B22, B25 (both undated) | AP:260 |
| SP16 | Float / hover | Four separate cases: buoyant floating in fluid, orbit/free fall, unsupported ballistic motion, magical hovering. Water brings drag, buoyancy, propulsion; zero gravity keeps inertia; magical hover needs an authored force rule. A generic up/down sine wave is not physical realism for all four. | S1 | | OPINION P00 | AP:262 |
| SP17 | Heavy tool, lab evidence | In a nail-driving experiment with ten male participants, a 1-lb and a 2-lb hammer led to different upper-limb joint moments and different mean trial durations (B21, 2017-04). It does not measure two-handed sledgehammer fighting. | S1 | | VERIFIED B21 | AP:264 |
| SP18 | Heavy tool, teaching | Heavy-lift teaching stresses motivation, reference, load-bearing poses and recovery, not a fixed anticipation count (B03, 2025-11-14; author named Dvoryankin in the body). | S1, S7 | | EXPERIENCE B03 | AP:264 |

### 5.4 Motion profile template (AP:266-282), complete

Fill the profile before authoring. An empty value does not allow a guess. A source can be a reference clip with capture metadata, a primary study, an owner decision, or the rig owner's confirmation. A confidence label expresses how sure the identification is, not a probability calibrated on data. Tag OPINION P00 (AP:268). In `workflow.md` S1 this is `motion-profile.md`, the animator's own file.

| id | field | required content | rejection condition | AP |
| --- | --- | --- | --- | --- |
| TP01 | Identity and purpose | Subject, action family, intended camera, style, gameplay role | Identity or task is ambiguous | AP:271 |
| TP02 | Topology | Complete semantic part inventory, hierarchy, controls and deform bones | Unmapped moving part or broken parent chain | AP:272 |
| TP03 | Scale and axes | Units, rest dimensions, forward/up, pivot convention | Conflicting coordinate or scale assumptions | AP:273 |
| TP04 | Mass and inertia | Supplied measurements or UNKNOWN; qualitative perceived weight kept separate | Unjustified kilograms, or mass from bone length | AP:274 |
| TP05 | Support and contacts | Ground, perch, grip, hinge, attachment, flight, buoyancy | A contact has no declared driver | AP:275 |
| TP06 | Active drivers | Intention, gaze, locomotion, force-producing joints | A part's motion cannot be explained causally | AP:276 |
| TP07 | Secondary response | Passive, active, mixed or rigid; constraint and recovery behavior | Every appendage treated as a delayed sine wave | AP:277 |
| TP08 | Personality | Approved pose language, posture, energy, attention, asymmetry | Motion contradicts the approved characterization | AP:278 |
| TP09 | Timing | Phase definitions, sourced durations, event positions, editable decisions | An unsupported number shown as evidence | AP:279 |
| TP10 | Limits and exceptions | Joint range, deformation envelope, stylized exceptions | An extreme pose exceeds verified rig capacity | AP:280 |
| TP11 | Runtime | Target rig type, attachment policy, priority, blending, replication, budget test | Export or runtime requirements are missing | AP:281 |
| TP12 | Review evidence | Reference IDs, previews, tests, owner decisions, unresolved fields | No reproducible comparison or decision trail | AP:282 |

[for-rigger] TP02 (parent chain, deform bones), TP03 (units, axes, pivots), TP05 (contact drivers), TP10 (joint range, deformation envelope) and TP11 (rig type, attachment policy) are the fields that need rig facts; the rigger supplies or confirms them at S2/S5 (inf. from field content).

### 5.5 Three filled profiles (AP:284-330), complete

All three are hypothetical specifications (OPINION P00), not measured datasets or approved characters; they contain no invented dimensions or timings.

**PF1 Biped hero** (AP:284-298)

| field | filled record (paraphrased) |
| --- | --- |
| Identity and role | Agile, friendly biped hero; third-person gameplay; attentive idle, decisive locomotion |
| Part map | Root, pelvis, torso, neck, head, paired upper and lower limbs, hands, feet, face; exact rig names wait for an inventory |
| Geometry and mass | Rest dimensions read from the rig; physical mass UNKNOWN; perceived weight light and grounded |
| Support | Alternating feet while moving; both feet or a declared single support at idle; airborne jump has no planted foot |
| Primary drivers | Facing/intent drives gaze and preparation; pelvis and support changes organize travel; free arms counterbalance |
| Secondary parts | Head stabilizes or deliberately leads attention; clothing is mixed passive response held to the gameplay silhouette |
| Personality | Open chest, clear line of action, a readable glance before a chosen change of direction; owner may reject or revise |
| Timing | Startup, contact, airborne, land and recovery boundaries defined; durations and per-part delays UNSPECIFIED until approved reference measurement |
| Constraints | No planted-foot drift; no knee reversal; hand interaction uses the prop's socket and contact frame |
| Review and budget | Silhouette and contact renders, real gameplay capture, per-character mobile profiling; numeric pass tolerances UNKNOWN until set |

**PF2 Winged creature with a tail** (AP:300-314). The paper adds: pick the reference anatomy deliberately; feather wings and membrane wings cannot be merged into one unexplained mechanism.

| field | filled record (paraphrased) |
| --- | --- |
| Identity and role | Curious airborne companion with a deliberate tail; must stay recognizable at distance |
| Part map | Body, neck/head, paired wings with a confirmed joint sequence, paired feet, tail chain, optional ears or crest |
| Geometry and mass | Measure rest spans and tail length; physical mass and inertia UNKNOWN; artistic perceived weight moderate |
| Support | Feet give perch, takeoff and landing contacts; flight support is aerodynamic; gliding differs from flapping |
| Primary drivers | Body trajectory, wing articulation and gaze follow the intended maneuver; the tail may steer actively rather than merely lag |
| Secondary parts | Feather or membrane response depends on the rig; the distal tail can follow local bending while the base is actively controlled |
| Personality | Curious head attention, deliberate banking, a distinct settled perch pose; no constant random flutter |
| Timing | Pick a named species or an approved stylization; wingbeat cycle, takeoff and landing measurements stay UNSPECIFIED until reference is chosen |
| Constraints | No wing/body intersection, inverted elbow, ground penetration, unexplained body lift, or identical flapping during a glide |
| Review and budget | Side and front flight previews, gameplay silhouette, perch contact, underside wing check, mobile crowd test for companion populations |

**PF3 Heavy tool swing** (AP:316-330). The paper adds: "heavy" describes the feel wanted, not an invented mass; tool size, grip positions and permitted acceleration come from the prop and approved reference.

| field | filled record (paraphrased) |
| --- | --- |
| Identity and role | Deliberate two-handed strike with a heavy hammer-like tool; one visible committed impact |
| Part map | Biped inventory plus tool root, head, handle, primary and secondary grip anchors, impact surface |
| Geometry and mass | Measure handle and head geometry; mass/inertia UNKNOWN; tool perceived as heavy relative to the character |
| Support | Feet organize force and braking; the primary hand defines the tool attachment policy; the secondary hand follows a solved contact |
| Primary drivers | Intent and support shift prepare the swing; torso and arms together accelerate the tool; impact and recovery change the body |
| Secondary parts | Hands, elbows, torso and accessories respond to impact; tool follow-through must not detach the grip or pass through the floor |
| Personality | Deliberate preparation, visible effort, committed recovery; heavy does not mean globally slow playback |
| Timing | Windup, acceleration, contact, deceleration, recovery and cancel rules exist; durations UNSPECIFIED pending reference and gameplay approval |
| Constraints | Keep both grips where required; define whether impact stops, rebounds or continues; verify collision and effect surface |
| Review and budget | Trace the tool-head arc, both hand contacts and foot support; check impact at gameplay scale; profile the character and any animated tool separately |

[for-rigger] from the profiles: PF1 needs hand sockets and prop contact frames and foot contact states; PF2 needs a confirmed wing joint sequence, tail chain, optional ear/crest parts and joint limits that prevent inverted elbows and wing/body intersection; PF3 needs tool root, head, handle, primary and secondary grip anchors and an impact surface, with a tool attachment policy defined by the primary hand.

### 5.6 Reference capture and measurement protocol (AP:332-338)

| id | lesson (paraphrased) | stage | flag | tag | AP |
| --- | --- | --- | --- | --- | --- |
| RF01 | Choose reference for matching anatomy, action, speed, camera, load and intention rather than for looks. Keep: original file, URL or permission, source date, nominal and real frame rate if known, whether the rate varies, timebase, any speed changes, edits and occlusions. A re-encoded social-media clip is not automatically usable as a timing measurement. Analyze only reference the studio may use; extracting motion does not grant rights to copy a performance or character. | S1 | | OPINION P00 | AP:334 |
| RF02 | Decide what counts as the event before measuring (first visible preparation, first motion of the striking surface, first contact, contact lost, highest body point, return to rest). Count the intervals between event times. Note uncertainty where frames are blurred, hidden, edited or repeated. With a variable frame rate use presentation timestamps instead of frame_index divided by fps. Store measured data apart from any retiming proposal. | S1, S7 | | OPINION P00 | AP:336 |
| RF03 | Make a contact sheet of the event frames and a time plot of the measured landmarks. Compare pelvis, head, feet, hands, tail base and tip, wing tips and tool head, but only those that are visible and relevant. A path seen in 2D is not a 3D path. Note perspective, camera motion and foreshortening before computing speed or joint angles. | S1 | | OPINION P00 | AP:338 |

Paper's own summary table for section 2 (AP:340-345):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Active versus passive appendages | no universal per-joint frame delay | VERIFIED biology; EXPERIENCE craft | B05 2008-03-17; B02 2017-06-19 |
| Separate geometry from physical mass | no invented mass values | OPINION | P00 2026-10-21 |
| Inventory every moving part and its cause | complete semantic mapping | OPINION | P00 2026-10-21 |
| Generic body-part frame delays | UNSPECIFIED unless source and context give them | OPINION | P00 2026-10-21 |
| Preserve reference timebase | t = frame intervals / fps when rate is constant | VERIFIED arithmetic | measurement protocol 2026-10-21 |

---

## 6. Section 3: game vs film timing and responsiveness (AP:347-375)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| GT01 | Riot's skin rule protects base readiness beats; Blizzard's caster work raises perceived effort without changing the gameplay contract. Shared lesson: anticipation need not vanish; the visible performance must fit what the game actually allows. | S7 | | EXPERIENCE C06, C10 | AP:349 |
| GT02 | Film timing can be built around a controlled cut and audience focus. Interactive motion also has to cope with input, movement, aiming, interruption, collision, who owns the state, and whether other players can read it. Treat these as separate: the visible reaction, the authoritative start of the action, the active window, when canceling is allowed, and when control returns. A recovery pose can keep playing after control comes back, and a blend can cover a state change; neither shows where the game's cancel window is. | S7 | | OPINION P00 | AP:351 |
| GT03 | Working definitions: startup runs from the approved action start to the start of the active part; active is when the gameplay effect may happen; recovery is the later stretch before a named next action is allowed. They are tools for analysis and do not show that a game has three exclusive, sequential states. Note whether buffering, hit confirmation, changes of animation rate or state transitions alter them. | S7 | | OPINION P00 | AP:353 |
| GT04 | Input delay is made of several clocks: input collection, the game accepting the state, network and authority, animation scheduling, and display. Measure the end-to-end delay the player actually feels. A long visible windup is not network lag. The paper found no safe general value for input delay, cancel window, startup or blend length for the requested Roblox games; design must supply them or approve a measuring exercise. | S7 | | OPINION P00 | AP:355 |
| GT05 | The Uncharted 4 duel supports reviewing the decision cue before adding UI. It gives no numeric reaction deadline. | S7 | | EXPERIENCE C12 | AP:357 |
| GT06 | Conversion: N source intervals at known source rate F last N/F seconds; that equals 30N/F frames at 30 fps and 60N/F frames at 60 fps. Capture rate, animation sampling rate, simulation step, render rate and display refresh are five separate things. Blender's effective scene rate is render.fps / render.fps_base. | S7 | | VERIFIED exact arithmetic; VERIFIED D35 | AP:361 |
| GT07 | Keep the original source events beside any authored retiming. If an approved duration is scaled by k, check each dependent event at t x k. Even so, uniform scaling may look wrong: a tool's speed-up, a grip change and the recovery may each need their own retiming while gameplay windows remain protected. | S7 | | OPINION P00 | AP:363 |
| GT08 | Ollie Johnston's notes: a 4-frame body-attitude lead before dialogue modulation; the first 6 to 8 frames of a new scene discussed. Frame rate not stated. Craft observations, not human perception thresholds or game offsets. Do not borrow 24 fps from another Disney source to convert them. | S7 | | EXPERIENCE C02 (1994) | AP:365 |
| GT09 | Encanto process page: 24 fps film presentation basis; "Welcome to the Family Madrigal" = 82 shots in 4 min 3 s. These describe the sequence, not action phases. One 24 fps interval = 1/24 s = 125/3 ms. The sequence = 243 s = 7290 equivalent 30 fps intervals or 14580 at 60 fps. Never divide the total by 82 and call it an observed shot duration. | S7 | | VERIFIED C20 (undated, checked 2026-10-21) | AP:367 |

Paper's own summary table for section 3 (AP:369-375):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Universal input and cancel limits | UNSPECIFIED | OPINION evidence limit | P00 2026-10-21 |
| Source-to-output conversion | 30N/F and 60N/F frames | VERIFIED arithmetic | defined timebase 2026-10-21 |
| Blender effective scene rate | render.fps / render.fps_base | VERIFIED | D35; current manual, undated; checked 2026-10-21 |
| Historical dialogue attitude advice | 4 frames; FPS unstated | EXPERIENCE | C02; 1994 |
| Historical scene-opening observation | 6-8 frames; FPS unstated | EXPERIENCE | C02; 1994 |
| Disney sequence metadata | 24 fps; 82 shots; 4 min 3 s | VERIFIED document | C20; undated; checked 2026-10-21 |

---

## 7. Section 4: stylization for readable playful motion (AP:377-396)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| SY01 | View-dependent distortion keeps Mario's face readable while travel direction stays clear (C13, 2023-10-17); Fortiche reports restrained head/body angles instead of bigger expressions (C08, 2021-12-08). Exaggeration and restraint are both valid; purpose matters more than amplitude. | S1, S7 | | EXPERIENCE C13, C08; OPINION P00 | AP:379 |
| SY02 | Stylization is controlled departure from reference, not permission to drop cause and contact. Approve pose language, silhouette priorities, shape changes and permitted physical violations before polishing. Judge exaggeration in the real phone viewport and gameplay camera; a strong close-up can blur when reduced. Young players are no reason to invent an attention-span threshold. | S1, S6, S7 | | OPINION P00 | AP:381 |
| SY03 | Squash and stretch to clarify force or emotion belongs only where the rig and asset contract permit it. Keep four things distinct: bending the body, scaling a control, a cheat that works from one camera, and a smear mesh. After export, recheck the volume impression and how attachments behave. The paper found no general stretch percentage, smear length, hold length or child-readable angular size; these are style choices to approve, not scientific constants. | S1, S2, S6, S7 | [for-rigger] says whether the rig supports scale, stretch or smear meshes; those capabilities are asked for in the brief, not assumed | OPINION P00 | AP:383 |
| SY04 | A crisp, readable move pairs a clear pose change with uneven spacing, a held idea and a brief settle. Snap does not come from applying one easing to every channel or from trimming a clip until contact vanishes. Put the visible accent at the moment of the gameplay action, then check that the lead-in and the aftermath still explain it. | S7 | | OPINION P00 | AP:385 |
| SY05 | A smear is a camera-dependent link between two readable poses. Look at it at the rate it is delivered, with motion blur off to diagnose and on if the delivered build uses it. It fails if it crosses an opponent's outline, hides the real tool contact, or looks like an extra limb that stays. | S6, S7 | [for-rigger] smear geometry needs a rig/asset answer (inf.) | OPINION P00 | AP:387 |
| SY06 | Holds keep the intended idea. A complete freeze, a breathing hold, a moving camera over a still pose and a small gaze shift produce different effects. Do not add secondary motion only to avoid stillness. An idle with every part perfectly synchronized reads as a mechanism; vary causally, not randomly. | S7 | | OPINION P00 | AP:389 |

Paper's own summary table for section 4 (AP:391-396):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Camera-specific exaggeration and restraint | exact deformation amounts UNSPECIFIED | EXPERIENCE | C13 2023-10-17; C08 2021-12-08 |
| Stretch and squash amount | UNSPECIFIED universal percentage | OPINION | P00 2026-10-21 |
| Smear and hold duration | UNSPECIFIED universal frame count | OPINION | P00 2026-10-21 |
| Readability approval view | actual gameplay framing and target viewport | OPINION | P00 2026-10-21 |
| Stylized exceptions | explicit owner-approved list | OPINION | P00 2026-10-21 |

---

## 8. Section 5: complete animation sets and reliable loops (AP:398-467)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| SL01 | Keep identifying cues (recognition, facing direction, outer-form distinction) across the entire set, not only a hero pose. | S6, S7 | | EXPERIENCE C05; VERIFIED C09; OPINION P00 | AP:400 |
| SL02 | Build sets from the gameplay states and transitions. A named clip is not complete without entry pose, exit pose, blend ownership, interruption behavior, attachment policy and event contract. Mark an unavailable action as intentionally absent instead of silently using a generic idle. The lists below are scope checklists, not a demand to build all of it for every game. | S1, S7 | | OPINION P00 | AP:402 |

Four clip checklists (all OPINION P00), complete:

| id | list | items (paraphrased) | AP |
| --- | --- | --- | --- |
| SL03 | Playable character | (1) idle base, approved variations, attentive/interaction idle, return from variations; (2) start, stop, walk, run, sprint if present, turns, strafes, backward movement, direction changes the controller needs; (3) jump preparation if permitted, takeoff, ascent, apex transition if needed, fall, soft/hard landing if gameplay distinguishes them, recovery into locomotion; (4) equip/unequip, hold, aim, use, reload or resource action if used, pickup/drop, interact, interrupted interaction; (5) attack families, misses, blocked impacts, hit reactions, stagger, knockback, stun, recovery, death, respawn as gameplay supports; (6) emotes and social actions with enter, loop if needed, exit, cancellation, locomotion policy; (7) seated, climbing, swimming, crawling, carrying or vehicle states only where implemented; (8) transition tests: idle to every locomotion mode; locomotion to attack; airborne to hit; attack interrupted by death; equipment swap in permitted states. | AP:404-420 |
| SL04 | Creature and pet | (1) species-appropriate rest, alertness, attention shifts, gait changes, starts/stops/turns, support transitions; (2) flight, glide, wing fold, perch, takeoff, landing, swim, burrow, climb or slither only when anatomy and mechanics call for it; (3) pet follow, catch-up, settle, owner attention, interaction, celebration, sleep/wake, and correction when pathing teleports or changes state; (4) feed, sniff, vocalize, play, attack or flee only if the product needs them, not to fill a library; (5) LOD alternatives that keep the behavior's identity and major contact events without every small secondary detail. | AP:422-432 |
| SL05 | Weapon or tool | (1) neutral hold, equip, ready, aim, action, recoil/rebound, recovery, stow, canceled action; (2) reload/charge/reset where it applies, plus empty, blocked, misfire or failed-use states only if gameplay supports them; (3) primary/secondary grip constraints, attachment transfer, visibility, magazine/component state; (4) first-person and third-person views are separate review targets, and one may need its own viewmodel rig; (5) melee miss, environment contact and target contact when they need different recovery or effects. | AP:434-444 |
| SL06 | Prop and moving object | (1) rest states, action start, moving loop where needed, endpoint, return/reset, interrupted movement; (2) door or lever pivot, moving-platform occupancy, machine phase, vehicle wheel/suspension dependencies, interaction sockets; (3) authoritative collision/occupancy state kept apart from purely cosmetic motion; (4) LOD or disabled state, initialization and late-join behavior, destruction or removal cleanup. | AP:446-454 |

[for-rigger] from the checklists: SL03 item 4 and SL05 item 3 (equip, attachment transfer, grip constraints), SL05 item 4 (a viewmodel rig may be separate), SL04 items 2 and 5 (creature-specific parts and LOD), SL06 item 2 (pivots, wheels and suspension, sockets).

| id | lesson (paraphrased) | stage | flag | tag | AP |
| --- | --- | --- | --- | --- | --- |
| SL07 | Loop interval is defined explicitly. If the end pose duplicates the start pose, decide whether the exported clip keeps the duplicate and check the engine's playback so no extra pause appears. Compare pose, velocity and, where it matters, acceleration across the seam; matching poses alone do not give smooth motion. For a traveling cycle, split local periodic motion from root displacement and confirm the controller supplies the intended speed. | S7 | [for-rigger] export of looping clips (root vs local motion split) | OPINION P00 | AP:458 |
| SL08 | Foot slide comes from a mismatch between gait travel distance, runtime movement, playback speed, contact timing, retarget scale or blend mixing. More keys do not cure it. Idle variations keep their approved entry and exit conditions, and interruptions that would break contacts are left out. Variation should come from meaning, not free randomness: a jittery subject, a sleeping pet and a machine each allow a different amount of irregularity. | S6, S7 | [for-rigger] retarget scale and contact timing are rig-side suspects too | OPINION P00 | AP:460 |

Paper's own summary table for section 5 (AP:462-467):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Identity across poses | silhouette and direction must stay readable | EXPERIENCE; VERIFIED document | C05 2021-03-12; C09 2007 |
| Required clips | derived from implemented states and transitions | OPINION | P00 2026-10-21 |
| Loop seam | pose and velocity checked; acceleration when important | OPINION | P00 2026-10-21 |
| Idle variation probability | UNSPECIFIED universal value | OPINION | P00 2026-10-21 |
| Foot-slide tolerance | UNKNOWN until scale and camera test define it | OPINION | P00 2026-10-21 |

---

## 9. Section 6: combat and ability animation as a shared timing contract (AP:469-498)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| CT01 | Hearthstone effects had to fit existing timing because timing could not change (C16, 2018-10-26). Overwatch audio presents threats and recognizable gameplay cues first (C17, GDC 2016). Cross-craft work is a state-communication problem as well as an aesthetic one. | S7 | | EXPERIENCE C16; VERIFIED C17; OPINION P00 | AP:471 |
| CT02 | Gameplay effect and authority sit with the combat designer; the animator supplies a readable physical performance within those rules. VFX, sound, camera and UI use the same event definitions as both. An impact that looks good but falls outside the true damage window is not a finished attack. Damage must never rest only on an animation marker or on how nice a rendered contact looks. | S7 | | OPINION P00 | AP:473 |
| CT03 | Timeline fields: request accepted, presentation start, anticipation complete, active start, contact candidate, active end, cancel-open/cancel-close, recovery complete, attachment change, VFX trigger, audio trigger, camera accent, UI cue, cleanup. Not every action uses every field. Each event stores: action revision, stable name, semantic meaning, time in seconds or exact rational form, source frame basis, owner, authority, replay policy, interruption behavior, consumers. | S7 | | OPINION P00 | AP:475 |
| CT04 | Never pack several meanings into one marker named Hit: a trail may start before contact, a whoosh may follow acceleration, a contact sound may need a confirmed surface, damage may arrive after prediction. Separate forecast presentation from confirmed outcome and define miss, block, interruption, latency and replay. | S7 | | OPINION P00 | AP:477 |
| CT05 | Hit-stop manipulates time; it is more than repeated poses. Choose what freezes: attacker, victim, weapon, animation track, particles, camera, audio, controller or the authoritative simulation, each possibly on its own clock. If the game has no explicit time scaling, author a held pose or a local presentation pause and leave essential simulation running. General values for hit-stop, shake size, shake length and sound offset are UNSPECIFIED. | S7 | | OPINION P00 | AP:479 |
| CT06 | Impact readability comes from approach, contact geometry, force direction, allowed deformation and consequence. Trace the striking surface through time; check the target response follows the force; keep both readable with effects hidden. If removing the flash hides the impact, the animation may be covering an unclear pose or timing error with VFX. | S6, S7 | | OPINION P00 | AP:481 |

Shared event contract example (AP:483-491), complete, no fabricated timing:

| event | timing value | producer to consumer | invariant (paraphrased) |
| --- | --- | --- | --- |
| ActionAccepted | gameplay-defined | gameplay to presentation | A rejected input never triggers authoritative damage. |
| ActiveStart | UNSPECIFIED until design approval | gameplay to animator and VFX | The window agrees with the visible threat. |
| ContactCandidate | measured from reference/pose; not automatically damage | animator to VFX and sound | Surface and direction are known when confirmed. |
| ContactConfirmed | runtime outcome | gameplay to effects/audio/UI | A miss never plays confirmed-hit feedback. |
| RecoveryComplete | UNSPECIFIED until design approval | gameplay and animation controller | The next permitted action matches the state rules. |
| CancelCleanup | interruption time | state owner to all consumers | Trails, loops, grip overrides and connections are cleared. |

Paper's own summary table for section 6 (AP:493-498):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Effects and sound respect gameplay | exact offsets UNSPECIFIED | EXPERIENCE; VERIFIED document | C16 2018-10-26; C17 GDC 2016 |
| One semantic event contract | one authoritative revision per action | OPINION | P00 2026-10-21 |
| Hit-stop duration | UNSPECIFIED universal value | OPINION | P00 2026-10-21 |
| Damage authority | separate from presentation-only callbacks | OPINION | P00 2026-10-21 |
| Impact review | with and without effects and sound | OPINION | P00 2026-10-21 |

Link to `workflow.md` section 5: this section is the source of the rule that the animator keeps a timing list of named events and never retimes gameplay to fit a clip.

---

## 10. Section 7: facial performance and secondary motion (AP:500-521)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| FS01 | Disney's hair and cloth accounts stress art direction, planning for continuity and repeated refinement, Moana 2 among the examples (B19 undated, B20 2025). Pixar's fur system lets artists set expressive groom poses (C11, 2022-08). Together they back authored secondary performance; they offer no general spring or joint-delay recipe. | S7 | | EXPERIENCE B19, B20; VERIFIED C11 | AP:502 |
| FS02 | Begin face work with intention and attention: what the character notices, wants, hides or responds to. Then bring eyes, lids, brows, mouth, head, neck and body into line with that. A set of face-rig channels is not a plan for acting. Review asymmetry, eye line, why a blink happens, lip closure while speaking, and whether the face reads at the size shown. A stylized face need not carry every human anatomical control. | S1, S2, S6, S7 | [for-rigger] face rig choices: control set sized to intention, not to anatomy | OPINION P00 | AP:504 |
| FS03 | At gameplay distance, major gaze and head attitude can matter more than fine lip or cheek motion. In close-ups, inspect eyes and mouth together with the body so face acting does not fight posture. Keep the approved range; do not maximize every expression. Blink rates, eye-lead delays and mouth-to-audio offsets are not given as universal numbers. | S1, S6, S7 | [for-rigger] what the face must show at which distance sets the face rig scope (inf.) | OPINION P00 | AP:506 |
| FS04 | Key the motion when timing, an authored silhouette, contact, comedy, dialogue or gameplay information has to come out the same every time. Go procedural when the input keeps changing and the result can be limited and tested. A hybrid also works: authored intent sets a base pose and a bounded procedural layer adds reaction. A tail that balances, points, grips or shows intent cannot be modeled by a free spring. | S1, S2, S7 | [for-rigger] | OPINION P00 | AP:508 |
| FS05 | A procedural layer needs this on record: target, local frame, rest state, how damping and stiffness are expressed, dependence on timestep, collision scope, rotation limits, reset on teleport, reset on interruption, behavior off screen or throttled, determinism needs, authority. Test it at several runtime frame rates and after a pause. State no frequency or damping ratio until one has been chosen and tested on this rig; the paper has no sourced tail-spring setting that fits all cases. | S2, S5, S7 | [for-rigger] | OPINION P00 | AP:510 |
| FS06 | For cloth, capes, hair and hanging accessories check the rest shape, the attachment, the lag, collisions and the settle. Simplify or replace them if they bury the action, cost too much or break on import. Hand-keyed secondary motion is acceptable, and simulation is not needed for quality. Avoid applying the effect twice: a lag baked into a clip plus a matching runtime spring doubles it. | S5, S6, S7 | [for-rigger] | OPINION P00 | AP:512 |
| FS07 | Roblox dynamic-head guidance (basic head) recommends fewer than 50 face joints where possible. It is advice for one scope (face rigging): not a limit for the whole character, not a number of poses, and not a measured phone budget. | S2, S5 | [for-rigger] | VERIFIED R29 | AP:514 |
| FS08 | Roblox face capture supports up to 60 seconds; video-to-body capture needs a continuous shot shorter than 15 seconds. Neither limit is a duration limit for authored animation. | S7 | | VERIFIED R28 | AP:514 |

Paper's own summary table for section 7 (AP:516-521):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Authored hair, cloth and fur | no universal delay constant | EXPERIENCE; VERIFIED document | B20 2025; C11 2022 |
| Universal blink or eye-lead timing | UNSPECIFIED | OPINION | P00 2026-10-21 |
| Authored versus procedural choice | deterministic intent vs continuous response | OPINION | P00 2026-10-21 |
| Spring constants | UNKNOWN until selected and measured for the rig | OPINION | P00 2026-10-21 |
| Secondary layers | check for double application | OPINION | P00 2026-10-21 |

---

## 11. Section 8: cutscenes and cinematic shots (AP:523-540)

| id | lesson (paraphrased) | stage | flag | tag / src | AP |
| --- | --- | --- | --- | --- | --- |
| CS01 | Fortiche used detailed boards and a layout step that held composition, camera and pose, leaving animation free to concentrate on performance (C08, 2021-12-08). Review question from the Disney authors: can the audience tell what the character is thinking (C03, 2003-06). | S7 | | EXPERIENCE C08, C03 | AP:525 |
| CS02 | Define the story beat before posing: whose viewpoint, what shifts, what the viewer should catch, and which emotional conclusion the shot should allow. Establish layout of space and eye lines. Stage the shot so that gestures, expressions and contacts stay uncovered by other bodies, props or effects. Any camera move should have a stated story or information reason. | S7 | | OPINION P00 | AP:527 |
| CS03 | Block the shot with the main acting poses and the camera placed together. A pose that reads from the gameplay camera may fail in profile or close up, so store shot-only cheats separately from reusable gameplay motion. Check screen direction, prop and hand continuity, the focal subject, how well silhouettes separate, and whether a cut covers or explains the event. | S7 | | OPINION P00 | AP:529 |
| CS04 | Log for the shot: timebase, entry and exit state, camera, lens or field-of-view convention, subject positions, dialogue and event sync, and the hand-back to player control. Even when skipped or cut short, a cutscene has to give back camera control, character attachments, animation state and UI. Where skipping is allowed, canceling counts as a full animation state in its own right. | S7 | [for-rigger] attachments and rig state must be restorable after a skip (inf.) | OPINION P00 | AP:531 |
| CS05 | Render the blocking without expensive lighting first, then a representative final look. Watch at normal speed before stepping frame by frame (a clumsy-looking still may be a good transition, and a handsome contact sheet can hide a dull rhythm). Whether an acting choice works is the director's call; automated metrics only bring up evidence and defects. | S7, S8 | | OPINION P00 | AP:533 |

Paper's own summary table for section 8 (AP:535-540):

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Acting and shot planning | detailed boards/layout; readable thought | EXPERIENCE | C08 2021-12-08; C03 2003-06 |
| Required story change | explicit before blocking | OPINION | P00 2026-10-21 |
| Universal shot or reaction duration | UNSPECIFIED | OPINION | P00 2026-10-21 |
| Skip and interruption | restore gameplay state and cleanup | OPINION | P00 2026-10-21 |
| Review modes | normal playback, event frames, continuous sequence | OPINION | P00 2026-10-21 |

---

## 12. Rigger digest: what motion asks of a rig

Consolidated from the rows above. The animator states needs and the rigger decides how (`workflow.md` section 1). Items marked (inf.) are the extractor's reading.

| id | topic | what the rigger must know or supply (paraphrased) | rows | stage |
| --- | --- | --- | --- | --- |
| RG01 | Part inventory | The animator will build a row for every visible part (also "does not move") and will ask the rigger about ambiguous or absent structure. Names are not proof of anatomy; a decorative fin, steering fin and rigid plate can look alike. Per element the paper wants: parent, children, rest transform, local axes, deform status, constraints, IK participation, mesh influence, geometry extent, intended pivot, allowed motion, confidence. Root control is not pelvis; helpers are not anatomy. | OR03, BO01, BO02, TP02 | S1, S2 |
| RG02 | Scale, axes, mass | Units, rest dimensions, forward/up axes and pivot convention are required; mass and inertia are UNKNOWN unless supplied. Do not derive kilograms from bone length, bounding box or weighted vertex count. | OR04, BO03, TP03, TP04 | S1, S2 |
| RG03 | Active vs passive appendages | Decide per appendage: active (drives or steers the body), passive (follows the base), mixed or rigid. An active tail needs controls that act as a primary driver; a passive tail needs a chain that can follow through. No universal per-bone delay; unequal segment lengths and bone count make equal delays brittle. | OR05, BP06, BP07, SP01-SP03, TP07 | S1, S2, S5 |
| RG04 | Wings | Wing type (feathered, membranous, insect) must be named before rigging; the three are different systems. Birds: stroke plane, wing planes, body attitude and tail configuration move together, so wing, body and tail must be controllable together. Bats: asymmetric retraction rotates the body, so left and right retract independently; folding has inertial consequences. Insects: stroke amplitude, pitch and frequency by species. Glide differs from flap. Profile PF2 needs a confirmed wing joint sequence and limits against wing/body intersection, inverted elbow and ground penetration; the underside must be reviewable. | BP08-BP10, SP04-SP07, PF2 | S1, S2, S6 |
| RG05 | Ears, antennae, fins, long bodies | Ears: left/right independent of the head. Antennae: active search plus passive deflection. Fin rays need not move as one paddle (curvature varies base to tip); fins can be control surfaces. Long axial bodies: curvature, displacement and activation are separate things. | BP11, BP12, BP14, BP15, SP12-SP14 | S1, S2 |
| RG06 | Extra legs | Per leg: contact state, touchdown location, stance fraction, normalized cycle phase. Stance feet must hold in world space while the body moves. Gait patterns for 4, 6 and 8 legs are hypotheses tied to one species, speed and substrate. Mechanical multi-leg schedules are allowed if contact logic is explicit. | BP05, SP08-SP11 | S1, S6, S7 |
| RG07 | Held tools and props | Need: tool root, head, handle, primary and secondary grip anchors, impact surface; attachment policy set by the primary hand; secondary hand follows a solved contact. Hand interaction uses the prop's socket and contact frame. Grips must not detach in follow-through; tool must not pass through floor. First-person viewmodel may be a separate rig. Door/lever pivots, platform occupancy, wheel and suspension dependencies, interaction sockets. | BP04, PF3, SL05, SL06 | S1, S2, S6 |
| RG08 | Contacts | Every contact (ground, perch, grip, hinge, attachment, flight, buoyancy) has a declared driver. Record planted, rolling, sliding, released. A deliberate skid is allowed. Foot sliding is a mismatch to diagnose, not to cover with camera cuts or more keys. | OR06, BP05, TP05, SL08 | S1, S6, S7 |
| RG09 | Range of motion and stress | Declare joint range, deformation envelope and stylized exceptions. The animator renders extremes: shoulder elevation, hip flexion, spine twist, wing fold, jaw opening, tail curl, grip, from saved cameras. A pose beyond verified rig capacity is a rejection condition, so the rig must state its reach. Extreme twists and weapon-crossing poses are silhouette risks. | BO05, TP10, CA04 | S1, S5, S6 |
| RG10 | Deformation and stretch | Squash and stretch, control scale, camera cheats and smear meshes are different tools; use only those the rig and asset contract allow. Volume impression and attachment are checked after export. No universal stretch percentage. | PR01, PR11, SY03, SY05, CA08 | S2, S6 |
| RG11 | Face | Fewer than 50 face joints where possible (Roblox basic dynamic head; not a hard cap). A face rig is a vocabulary, not an acting plan; stylized faces need not carry all human controls. Review asymmetry, eye line, blink purpose, lip closure. At gameplay distance gaze and head attitude may dominate. Neck jiggle and jowl blendshape are a documented example of secondary face motion; check it in the engine, not only the DCC. | FS02, FS03, FS07, CA10 | S2, S5, S6 |
| RG12 | Secondary motion that needs bones or controls | Hair, cloth, capes, dangling accessories, tails, straps, ears, soft tissue: decide key / procedural / hybrid per part. A procedural layer needs the listed fields (target, local frame, rest state, damping and stiffness form, timestep dependence, collision scope, rotation limits, teleport and interruption reset, off-screen behavior, determinism, authority). No sourced spring setting exists; treat any value as OPINION until tested at several frame rates and after a pause. Avoid double response (baked lag plus runtime spring). Reduce or replace cloth that hides action, costs too much or fails import. | BP13, FS04-FS06, CA06, CA09 | S2, S5, S7 |
| RG13 | Export and tooling | Export the engine's motion, not the full control rig or all intermediate keys. Pin software versions; use Blender slots/channelbags not removed Action.fcurves (fact-check CL05). Importer ceilings are not phone budgets; profile on the mobile client. Looping clips: decide whether the duplicate end pose is exported; split local cycle from root travel. Retarget scale is a foot-slide suspect. | OR11-OR13, SL07, SL08 | S5, S7 |
| RG14 | Creature LOD and pets | LOD versions keep behavior identity and major contacts without every small secondary detail. Pets need correction behavior when pathing teleports or changes state. | SL04 | S2, S7 |
| RG15 | Cutscene state | After skip or interruption the rig must give back camera control, attachments, animation state and UI. | CS04 | S5, S7 |
| RG16 | What the animator reviews at S6 (rigger should expect) | Turntable with labeled rig overlays, unlit silhouette render, unobscured mesh view, saved camera transforms, joint-limit renders, planted-contact markers with support region and center-of-mass proxy, silhouette in the gameplay view at phone size. | BO04, BO05, SY02 | S6 |
| RG17 | Do not invent | No mass, per-bone delay, anticipation length, spring constant, stretch percentage, foot-slide tolerance, or gait pattern without source or an owner decision; label authored choices OPINION. | EV04, OR10, TP04, FS05 | all |

## 13. Lesson index by stage

| Stage | IDs |
| --- | --- |
| S1 motion needs | EV02, EV04, EV06, OR01, OR03-OR07, OR10, GA01, GA03, PR01-PR12, CA01, CA03, CA06, BO01-BO07, BP01-BP16, SP01-SP18, TP01-TP12, PF1-PF3, RF01-RF03, SY01-SY03, SL02, FS02-FS04, RG01-RG09 |
| S2 rig plan (rigger) | OR03, OR05, OR13, BO02, SP03, SP07, FS02, FS04, FS05, FS07, SY03, RG01-RG07, RG10-RG14 |
| S5 rig and tests (rigger) | OR05, OR11-OR13, CA10, FS05-FS07, RG03, RG09, RG11-RG13, RG15 |
| S6 rig acceptance (animator) | OR06, OR07, GA02, CA01, CA04, CA10, BO04, BO05, SP11, SY02, SY03, SY05, SL01, SL08, CT06, FS02, FS03, FS06, RG16 |
| S7 animate and export | OR08-OR15, CA02, CA05, CA07-CA09, GT01-GT09, SY04-SY06, SL02-SL08, CT01-CT06, FS01, FS04-FS06, FS08, CS01-CS05, RG13 |
| S8 owner final | OR02, OR15, CS05 |

---

## 14. Claims to check (table CL, for step 2)

Kinds: roblox, blender, science, industry, other (arithmetic or editorial). "Dated" values are as the register gives them. IDs use CL because C01-C23 are source IDs.

| id | claim (value, date, tag as the paper gives them) | AP | src | kind |
| --- | --- | --- | --- | --- |
| CL01 | Roblox basic dynamic-head guidance: use fewer than 50 face joints where possible. | AP:514 | R29 | roblox |
| CL02 | Roblox face capture supports up to 60 seconds. (Register key line shows only the 15 s item, so the 60 s figure is not visible in the register.) | AP:514 | R28 | roblox |
| CL03 | Roblox video-to-body capture needs a continuous single shot shorter than 15 seconds. | AP:514 | R28 | roblox |
| CL04 | Roblox MicroProfiler guidance: the mobile client is the best place to profile; importer ceilings differ from measured mobile budgets. | AP:45 | R18 | roblox |
| CL05 | Blender 5.0 (released 2025-11-18) removed the legacy Action API and Action.fcurves access; the current route is slots and channelbags. (Register key line states only that the legacy Action API was removed; "slots/channelbags" naming is not in the key line.) | AP:41 | D04 | blender |
| CL06 | Blender effective scene frame rate = render.fps / render.fps_base (Output Format manual, shown as 5.2, accessed 2026-10-21). | AP:361, 372 | D35 | blender |
| CL07 | Twelve conventional principle names appear on the authors' site; the index adds a parenthetical "(same or different as Weight)" to Solid Drawing. | AP:59, 75 | C01 | industry |
| CL08 | Riot art-education page: strong poses are the foundation of an animation. | AP:55 | C04 | industry |
| CL09 | Thomas and Johnston emotional-animation questions: can viewers tell what the character thinks (2003-06). | AP:55 | C03 | industry |
| CL10 | League clarity article (2021-03-12): recognition from shape vs movement; Ivern lanky model with characteristic walk; Lee Sin generic shape; facing and hitbox consistency are clarity duties. | AP:83 | C05 | industry |
| CL11 | VALORANT skins (2020-05-18): skin animation mirrors base weapon beats; ammunition-insertion sound stays aligned; cosmetic sound must not mask key cues. | AP:91 | C06 | industry |
| CL12 | VALORANT arsenal (2020-05-12): two- or three-beat equip/reload patterns communicate weapon state. | AP:93 | C07 | industry |
| CL13 | Arcane Season 1 (interview, 2021-12-08): keyframed from substantial live-action reference, not motion capture; boards fix composition/camera/poses; Jinx subjective scratches are 2D over CG plates; expression and pose libraries used. | AP:101 | C08 | industry |
| CL14 | TF2 rendering paper (2007): nine classes tested as black silhouettes without internal detail. | AP:109 | C09 | industry |
| CL15 | WoW 7.3 (2017-08-16): racial casting animations reach the casting pose in a more consistent time; precasts gather energy; instant casts get one-handed variants for movement. | AP:117 | C10 | industry |
| CL16 | WoW Arcane Missiles keeps five bursts of four missiles (5 x 4). | AP:117, 121, 177 | C10 | industry |
| CL17 | Turning Red SIGGRAPH 2022: art-directed fur reflects emotion; sparse style guides propagate sculpted groom poses to the full hair system. (Partial paper only.) | AP:125 | C11 | industry |
| CL18 | Uncharted 4 retrospective (2021-05-10): final duel replaced quick-time prompts with directional blocking; AI traversal picks next action in advance. | AP:133 | C12 | industry |
| CL19 | Mario Wonder interview (2023-10-17): pipe-entry sound retimed after a new action was added; view-dependent face/body distortion; Goomba bite expression at the damage event. | AP:141 | C13 | industry |
| CL20 | Fortnite GDC 2013 slides: spline-driven material animation; artists choose piece order; example wall has 46 pieces; GPU deformation does not alter collision. | AP:149 | C14 | industry |
| CL21 | Fortnite 2013 slide system samples its spline at one X-unit per second (parameterization of that presentation only). | AP:153 | C14 | industry |
| CL22 | Spider-Man GDC 2019 slides: Kingpin neck jiggle and jowl blendshape; pipeline compares poses with scans and checks engine appearance; triangulation differences can damage the result after export. | AP:157 | C15 | industry |
| CL23 | Overwatch GDC 2017 abstract poses a McCree revolver reload in 45 frames, no frame rate given. | AP:165, 178 | C18 | industry |
| CL24 | Supercell article (2019-11-22) covers stylized visual development, not attack timing. | AP:165 | C19 | industry |
| CL25 | Hearthstone (2018-10-26): effects had to fit existing timing and mixed client/server information. | AP:471 | C16 | industry |
| CL26 | Overwatch GDC 2016: audio prioritizes threats and recognizable gameplay cues. | AP:471 | C17 | industry |
| CL27 | Book metadata: Animator's Survival Kit expanded Faber paperback 2009-11-05, ISBN 9780571238347. | AP:169 | C21 | other |
| CL28 | Book metadata: Game Anim 2nd ed., copyright 2021, 350 pages, ISBN 9780367707651, expanded motion capture and motion matching. | AP:169 | C22 | other |
| CL29 | Book metadata: Illusion of Life Disney edition 1995-10-19, 576 pages, ISBN 9780786860708; original work 1981. | AP:169 | C23 | other |
| CL30 | Ollie Johnston notes (1994): 4-frame body-attitude lead before dialogue modulation; first 6 to 8 frames of a new scene; no frame rate stated. | AP:365, 373-374 | C02 | industry |
| CL31 | Encanto: 24 frames per second presentation basis. | AP:367, 375 | C20 | industry |
| CL32 | Encanto "Welcome to the Family Madrigal": 82 shots in 4 min 3 s. (Not in the register key line.) | AP:367, 375 | C20 | industry |
| CL33 | Disney hair/cloth work including Moana 2 (continuity, planning, iteration). (Moana 2 not in register key lines.) | AP:502 | B19, B20 | industry |
| CL34 | Animation Mentor tail exercise (2017-06-19): pendulum tail is passive; same article distinguishes a squirrel tail acting independently; author named Drew Adams in body. | AP:226 | B02 | industry |
| CL35 | Animation Mentor (2014-07-14): ask what moves first and why; author named Wayne Gilbert in body. | AP:198 | B01 | industry |
| CL36 | Animation Mentor (2025-11-14): heavy-lift teaching stresses motivation, reference, load-bearing poses, recovery; author named Dvoryankin in body. | AP:264 | B03 | industry |
| CL37 | Flat-tailed house geckos (Cosymbotus platyurus): tails used for wall support after a slip, righting in the air, steering on descent; active tail rotation counter-rotates the body without a head-to-hips twist (2008-03-17). | AP:228 | B05 | science |
| CL38 | Pigeons flying between perches: stroke plane, wing planes and tail rotations strongly correlated between takeoff and landing (2010-05-15). | AP:234 | B06 | science |
| CL39 | Bats: asymmetric wing articulation can account for large reorientation in low-speed landing / fall recovery via inertia (2015-11-16). | AP:236 | B07 | science |
| CL40 | Six bat species: folding costs energy but lowers total inertial cost against an always-extended rigid wing (2012-04-11; register key line adds a 40-fold body-mass range). | AP:236 | B08 | science |
| CL41 | Common swifts: wingspan and wing shape change with airspeed; only one of two initially tested birds glided in the tunnel (2011). | AP:238 | B10 | science |
| CL42 | Eight ridden Icelandic horses measured over ground: walk, trot, pace, tölt, canter, gallop; symmetric/asymmetric footfalls and leads (2007-01-15). Register key line says accelerometers. | AP:244 | B11 | science |
| CL43 | Drosophila straight steady forward walking: modified tripod R1-L2-R3 and L1-R2-L3 with small within-group offsets; fixed-speed forward only (2021-02-03). | AP:246 | B12 | science |
| CL44 | Spider Grammostola mollicoma: speed-dependent coordination; anterior pairs tend to alternate, posterior pairs do not (2011-10-15). | AP:248 | B13 | science |
| CL45 | Snake-skin friction measured and slithering modeled: ground interaction and weight distribution contribute to progression (2009-06-08). | AP:254 | B14 | science |
| CL46 | African lungfish (Protopterus annectens): axial activation and kinematics change with viscosity (2008). | AP:256 | B15 | science |
| CL47 | Bluegill sunfish median fins: maneuver- and speed-dependent kinematics, fin-ray curvature varies base to tip (2005-07-15). | AP:258 | B18 | science |
| CL48 | Cat pinnae can be oriented independently of head position (1998-06-01). | AP:215 | B16 | science |
| CL49 | Stick-insect antennae: exploratory pattern depends on context; touch can change sampling and later leg placement (2011). | AP:216 | B17 | science |
| CL50 | NASA: microgravity is weightlessness, not loss of mass; changing mass distribution changes rotational response (both undated). | AP:260 | B22, B25 | science |
| CL51 | Nail-hammering experiment, ten male subjects: 1-lb vs 2-lb hammers gave different upper-limb joint moments and mean trial durations (2017-04). | AP:264 | B21 | science |
| CL52 | Level-treadmill study, 49 non-obese adults: phase-dependent relationships among body mass, limb length and posture (2017-02-13). | AP:196 | B23 | science |
| CL53 | Dynamic-stability model includes center-of-mass velocity (inverted-pendulum basis) (2005-01). | AP:196 | B24 | science |
| CL54 | Arithmetic: one 30 fps interval = 100/3 ms = two 60 fps intervals; frames 1 and 31 span 30 intervals. | AP:17 | EV05 | other |
| CL55 | Arithmetic: one 24 fps interval = 1/24 s = 125/3 ms. | AP:367 | C20 | other |
| CL56 | Arithmetic: 4 min 3 s = 243 s = 7290 intervals at 30 fps = 14580 at 60 fps. | AP:367 | C20 | other |
| CL57 | Arithmetic: 30N/F frames at 30 fps and 60N/F at 60 fps for N source intervals at F fps; seconds = N/F. | AP:361 | EV05 | other |
| CL58 | Counts stated as fixed numbers: 12 principles, 10 cases, 15 operating rules, 9 TF2 classes. | AP:19, 59, 79, 109 | C01, C09 | other |

---

## 15. Contradictions and limits (table LM)

| id | item | detail | AP | handling |
| --- | --- | --- | --- | --- |
| LM01 | Tag conflict, C01 | Body text and the section-1 table tag C01 VERIFIED (names) but the register tags C01 EXPERIENCE. The names are probably checkable; the site is an author page. | AP:59, 174 vs 1154 | Fact-check; keep both tags until resolved. |
| LM02 | Tag conflict, C18 | Body text and summary table: EXPERIENCE (abstract only). Register: VERIFIED, with a note that the page fetch timed out and the shipped value is unverified. | AP:165, 178 vs 1260-1264 | Treat the 45 frames as an unconvertible design question. |
| LM03 | Provenance gap, C20 | The 82 shots and 4 min 3 s figures are not in the register key line (only the 24 fps line is). | AP:367 vs 1276 | CL32. |
| LM04 | Provenance gap, names and extras | Author names (Drew Adams, Wayne Gilbert, Dvoryankin), Moana 2, and the 60 s face-capture figure are not visible in the register key lines. | AP:198, 226, 264, 502, 514 | CL02, CL33-CL36. |
| LM05 | Frame rate missing | 4-frame and 6-8-frame advice (C02) and 45 frames (C18) have no frame rate. They cannot be converted to seconds, 30 fps or 60 fps. The 24 fps of C20 must not be borrowed. | AP:17, 365 | Keep as stated; never convert. |
| LM06 | Structure, not cadence | 5 x 4 missiles (C10) and two/three beats (C07) are structural counts, not durations or cadences. | AP:93, 121 | Do not derive timing. |
| LM07 | Presentation parameter | One X-unit per second (C14) belongs to a 2013 slide system, not to a current Fortnite build time, simulation rate or tick. | AP:153 | Do not reuse. |
| LM08 | Passive-only exercise | B02's pendulum tail exercise is passive by design; the same article names an independent squirrel tail. Not an animal law. | AP:226 | Do not extract "never lead". |
| LM09 | Single-species or single-animal scope | B05 one gecko species; B10 one swift supplied the steady glide; B13 one spider species; B15 one lungfish species; B16 cat; B17 stick insect; B18 bluegill; B06 pigeons perch to perch. No result transfers to other animals, to dragons or to stylized creatures. | AP:228-258 | Pick one reference and label authored deviations OPINION. |
| LM10 | Gait scope | B11: eight ridden Icelandic horses; transverse canter/gallop not universal. B12: modified tripod only for straight, fixed-speed forward walking (the paper title for B12 says tripod across speeds; the paper's own scope limit is narrower). B13: alternating-tetrapod is a hypothesis only. | AP:244-248, 1370-1372 | Do not generalize; fact-check B12 title vs scope. |
| LM11 | Study scope | B21 is a nail-hammering study (ten male subjects), not two-handed sledgehammer combat. B23 is 49 non-obese adults. B24 and B23 do not validate arbitrary creature balance. | AP:196, 264 | Heavy-tool timing needs own reference. |
| LM12 | Evidence depth | No embedded video was played or frame-counted; C11 is a partial paper; C15 shows rig and review examples, not shots; C08 is a vendor-hosted first-person interview; C09 is silhouette evidence, not animation curves; C19 is visual development only. | AP:79, 109, 125, 157, 1200 | Use cases for lessons, never for numbers. |
| LM13 | Books | Only metadata verified; edition years differ from original dates (C23 1995 listing vs 1981 original; C21 2009 paperback not original). | AP:169-171 | Record edition and page before using. |
| LM14 | Undated sources | C01, C04, C20, B19, B22, B25, R18, R28, R29 are undated in the register. Undated does not mean 2026. | AP:1148 | Keep "undated". |
| LM15 | VERIFIED is not a budget | VERIFIED R29 (face joints) and R18 are documentation; a platform recommendation is not a measured phone budget, not a whole-character cap. | AP:13, 514 | Budgets come from the rig sheet / measured on target phone. |
| LM16 | Roblox-facing limits are not animation limits | R28 capture durations (60 s face, under 15 s body) do not limit authored animation. | AP:514 | Do not use as clip-length rules. |
| LM17 | UNSPECIFIED: body-part frames | All 16 "typical frame numbers" cells in BP01-BP16 are UNSPECIFIED (some qualified: per joint, generic cycle, generic delay, generic wave / per-bone delay; whole-tail events and honeybee example sit in the timing library). | AP:205-220 | Measure reference or author and label OPINION. |
| LM18 | UNSPECIFIED: case timings | CA01-CA10 timing fields are UNSPECIFIED (CA02 beat counts, CA05 5 x 4, CA09 one X-unit/s are structure or parameters only). | AP:87-161 | |
| LM19 | UNSPECIFIED: gameplay timing | Universal input delay, cancel window, startup, active and recovery lengths, blend duration; hit-stop duration; shake amplitude and duration; sound offset; ActiveStart and RecoveryComplete (until design approval). | AP:355, 479, 487, 490 | Gameplay owner supplies; animator never retimes gameplay to fit a clip. |
| LM20 | UNSPECIFIED: style | Stretch and squash percentage, smear duration, hold length, child-readable angular size, exact deformation amounts for camera-specific exaggeration, idle variation probability, universal shot or reaction duration. | AP:383, 392-396, 466, 538 | Owner-approved style decisions. |
| LM21 | UNSPECIFIED: face | Blink rates, eye-lead delays, mouth-to-audio offsets, no universal delay for hair, cloth, fur. | AP:506, 518 | |
| LM22 | UNKNOWN fields | Foot-slide tolerance (until scale and camera test), spring constants (until selected and measured), numeric pass tolerances in PF1 (until set), physical mass and inertia in PF1-PF3. | AP:298, 467, 520, 291, 307, 323 | Set per project, then record. |
| LM23 | Quantities that must not be swapped | Animal observation ranges, cinematic shot durations, engine capacities and character gameplay windows are four different quantities. A latency, a gait phase and a capture rate are also different. | AP:15, 202 | |
| LM24 | Generated paper states no benchmark | No animation or performance benchmark was created for the paper; every runtime or cost statement is procedure, not measurement. | AP:1148 | Measure on target phones. |
| LM25 | Hypothetical profiles | PF1-PF3 are not measured datasets or approved characters. PF2 does not model any real bird, bat or dragon. | AP:286, 302, 318 | Use as format examples only. |
| LM26 | Rule 11 detail | OR11 names "slots / channelbags" and "Action.fcurves"; the register key line for D04 only says the legacy Action API was removed. | AP:41 vs 1476 | CL05. |
| LM27 | Hit-stop and time scaling | Paper gives no engine-specific Roblox method for hit-stop; it only advises a held pose or local presentation pause when time scaling is not explicitly supported. | AP:479 | Roblox-specific method not in this range. |
| LM28 | Section gap | Timing library values referenced from the body-part table (measured whole-tail events, honeybee frequency) sit in lines 542-1145, covered by another note; this file holds no such numbers. | AP:211, 214 | |
