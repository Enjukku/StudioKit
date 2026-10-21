---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J016 transcript extraction (R04 animation, R06 VFX, R07 sound); owner-supplied Riot transcripts in Downloads, not in git"
supersedes: []
---
> Author: research reader · claude-opus-5-5 · default · 2026-10-21 (J016 transcript extraction; lead spot-read)
# E: Animation, VFX and sound (Riot "Super Art Power Hour" ep4, ep6, ep7)

> Author: research reader · claude-opus-5-5 · default · 2026-10-21. The transcripts are data. I read every line of all three files: A 1100 lines, V 401 lines, S 620 lines.

**Source keys** (a reference like A:172 means line 172 of file A; ranges look like A:162-190):

- A = `C:\Users\Firew\Downloads\charcter and gameplay animations ep4.txt`
- V = `C:\Users\Firew\Downloads\crafting visual  effects in teamfight tactics ep6.txt`
- S = `C:\Users\Firew\Downloads\Sound design in arcane ep7.txt`

**What this evidence can and cannot support.** All three episodes are live challenges done in 1 to 3 hours. None of the work ships (A:56, A:1080-1082; V:25, V:63-64, V:251-252; S:11, S:27-29). They show one person's craft (two people in S) much more than team process. Cross-craft timing comes up in only a few passages: A:162-190, V:218-222, S:195-215. Where a transcript says nothing on a topic, this file marks it **absent**. Statements marked **[inference]** are my synthesis across the cited lines.

---

## A. Character and gameplay animation (ep4)

### A1. Speaker, role, team, what the episode covers
- Lana Bachynski, senior animator in Riot R&D (A:14). She animates characters and monsters. She calls herself a gameplay animator because she rarely does cinematics (A:16-22). Credits: Bewitching Miss Fortune recall; Spirit Blossom Ahri, including the human-to-fox transformations and quadruped motion; Dark Cosmic Lux; Spirit Blossom Thresh; K/DA Seraphine (A:24-32).
- The episode: a weight and pose shift between two key poses of K/DA Akali, made in Maya in about 3 hours (A:38-40, A:56, A:74, A:976). The model is by Jason Namgung and the rig by tech artist Omar Garcia (A:58-62). She ends by showing a rehearsal version that uses the same two poses to tell a different story (A:1052-1068).

### A2. What great work looks like (checkable signs)
- **She overrides the computer's in-betweens.** Two poses played back with computer interpolation look bad, and the body twists into itself. The animator must take control to get the intended motion (A:64-76).
- **Weight.**
  - She plans the centre of gravity first. Weight must come off a foot before that foot can move (A:92-100).
  - A clear transfer of weight from one limb to another is her most frequent demo-reel note (A:456-468).
  - Even a fast, "bursty" move needs a small sign of contact that shows where the weight went (A:468-474).
  - Mass must not vanish from a place between frames. Energy has to visibly go somewhere (A:246-254).
- **Enough physics for the audience to accept extreme moves** such as hang time (A:476-480). A parabolic toe path keeps gravity present (A:754-758).
- **Timing.**
  - Fewer frames between keys make a move feel faster (A:446-448).
  - On a landing, the foot contact is quick and the catch follows (A:438-446).
  - A short hold before a spring is the tightening of energy, that is, anticipation (A:450-454).
  - A cartoony jump has hang time at the top and then a fast fall (A:342-352).
  - She adds a small overshoot on standing up (A:376-382).
  - Deleting one frame made a fall feel snappier and more impactful (A:808-816).
- **Rhythm.** She wants an uneven, jazz-like cadence. An even cadence feels predictable to viewers (A:360-366).
- **Asymmetry.** Avoid "twinning", where limbs are identical or move at the same moment (A:540-552, A:698-700). Offset the feet so the eye catches two separate reads: hitting the ground, then catching the weight (A:716-724).
- **Character.**
  - Motion choices come from the character. Akali is nimble, so she gets a leg swoop and a martial jump (A:102-104, A:324-326).
  - For K/DA, style and flair matter more than practicality (A:536-540).
  - A landing must read as confident, not afraid (A:712-716).
- **Silhouette from the game camera.**
  - She moves the kicking leg to get a better silhouette (A:158-162).
  - She turns the feet sideways so both knees show and the leg does not point straight down the camera (A:760-766).
  - The ponytail's iconic swoop in silhouette matters more than which side it is on (A:702-708).
- **Body parts that beginners forget.**
  - Clavicles (the shrug) supply energy and range. She calls them "the eyebrows of the body" (A:394-410).
  - Hips let poses sink in (A:652-654).
  - Fingers and hands matter even in a top-down game where hands are tiny (A:916-928).
  - Elbows drag behind the motion (A:904-906).
  - Arms push up to sell a high jump (A:892-904).
  - Elbows sink to ground a landing (A:930-938).
- **Secondary motion and face.**
  - She animates hair as one mass, then offsets each bone by a frame. A heavy ponytail stays springy rather than flowing (A:984-1024).
  - The eyes close during a fast spin, because people blink when they turn their head. They widen on the way down for a character moment (A:1028-1046).
  - The head stays locked during turns, as a ballerina's does (A:944-948).
- **Good versus great.** She puts the difference at about 10%. The bulk of quality comes from the root's cadence, strong poses, flow and offset. Hair and face add the final appeal (A:970-982).

### A3. The steps she follows, in order
1. Learn the character's two sides and choose poses that show both (A:42-52). She always wants to know a character's subtext (A:620-622).
2. Block in the two key poses (A:78-82).
3. Work in the "layering" method, not pose-to-pose with stepped keys. The animation looks bad for a long time and then comes together (A:84-90).
4. Animate the root (centre of gravity) first (A:92-100). Hold the first pose for a few frames (A:106-108).
5. Rough out the big move, here a spin. She keeps head and shoulders in world space, which gives balance for free (A:132-146). She fixes knees and feet by hand (A:126-132, A:150-156).
6. Make holds as "copied pairs" (a duplicated key), not stepped keys, so she can feel the real timing (A:268-284).
7. Rough out timing for the whole animation. She keys the whole body on the same frames so timing stays easy to move (A:434-438). She adjusts by sliding keys and feeling the rhythm (A:354-356).
8. Replace the rough rest moments with real poses. The in-air pose comes from concept art and the character's in-game actions (A:520-536).
9. Break up the keys so that actions start at different times. For example, the feet stay down 1 to 2 frames longer and the push-off gets sharper (A:594-606).
10. Polish in the graph editor using weighted tangents and eases (A:194-210, A:558-590).
11. Loop: play, find what feels wrong, fix it, play again. She calls this stage "noodly" (A:726-734).
12. Add details: arms, fingers, head (A:892-948).
13. Add the finishing layer: hair and face (A:978-1046).

Her terms: keyframes are the main story beats, and breakdowns are how you get from one to the next. A breakdown can be ugly on its own and still make the motion flow; she calls it the "storytelling pose" (A:950-968).

### A4. References and research
- Concept art and the character's in-game actions shape the in-air pose (A:530-532).
- **Acting it out.** In serious meetings, two people stand up holding wooden sticks weighted like the weapon and test how the character would swing (A:632-636). Her theatre childhood made her willing to look silly and to exaggerate in posture and voice (A:624-646).
- **Body test.** Stand on both feet and try to lift one. You cannot (A:460-466).
- **Anatomy.** She studied anatomy and drew figure models holding action poses (A:286-306). Anatomy tells her which joints can be stretched or smeared without looking wrong (A:296-300). When stuck on a hard motion, she goes back to anatomy (A:308-312).
- Video reference: **absent**.

### A5. Self-review before showing anyone
- She checks in the scene (render) camera, not only the working view (A:158-160, A:384-386), and from the game camera's angle (A:760-764).
- She uses the graph editor to find curves that are going wrong (A:196-198).
- She watches for mass that vanishes, weight that does not transfer, and twinning (A:246-254, A:456-468, A:540-552).
- When something will not fix, she deletes the keys and redoes it without regret (A:420-432).
- She rehearsed the piece beforehand with the same poses (A:1052-1060).
- She notices small pops that most viewers will not see. Producers decide when the work is done (A:818-828, A:848-856).

### A6. Collaboration
- **Pipeline position.** Animation sits between tech art and audio. Effects is partnered with animation but runs "a little bit staggered" (A:162-168).
- **Inputs.** The rig comes from tech art and the model from a modeler (A:58-62).
- **Engineering:** getting the work into the engine, and the tools to do it (A:170-172).
- **Design:** which animations are required, and "the right frame lengths" (A:172-174). Design owns the gameplay duration, and animation fits inside it.
- **Effects:** effects often lift an animation beyond what animation alone can do (A:174-178).
- **Audio:** when animation changes, animation works with audio to get the impact ("oomph") into the move (A:178-180).
- **Hub role.** Animation is often the go-between for other departments. Ideally all crafts work in the same room (A:180-184).
- **Bring animators in early.** Early on, they can say what can and cannot be done. That means showing that more is possible, or reining an idea in (A:184-190).
- **Concept art.** A concept artist might correct her ponytail placement. She holds that the silhouette read matters more (A:704-708).
- **Producers** end the polishing to keep the schedule (A:852-856).
- **Timing dependencies.**
  - Design sets the length (A:172-174).
  - VFX follows animation, staggered behind it (A:166-168).
  - Audio comes after animation and must hear about changes (A:164-166, A:178-180).
  - The animator pushes back early, on feasibility (A:184-190).
  - Frame markers, hand-off formats and sign-off are **absent**.

### A7. Review and approval
- Producers decide when work is done (A:852-856).
- A trusted community or peers act as "your eyes" when you cannot see your own work, and they help you practise giving and taking feedback (A:782-796).
- She describes industry nitpicking as friendly and shared, not hostile (A:838-848).
- Formal review stages, named reviewers and the number of rounds: **absent**.

### A8. Order of work
- **Pipeline:** tech art (rig), then animation, then audio. VFX runs alongside animation, staggered behind it (A:162-168). Animators join early in the idea stage (A:184-190).
- **Inside one clip:** rough timing for the whole body comes first and stays adjustable. Poses come next and details last (A:434-438, A:520-524, A:978-982).
- **Going back upstream:** none named, apart from raising feasibility early (A:184-190).

### A9. Mistakes she names, and the fixes
- Leaving linear interpolation alone twists the body. Fix: control the motion by hand (A:64-76).
- A foot moves without a weight shift. This is her top demo-reel fault. Fix: add a weight shift or a contact (A:456-474, A:662-666).
- Clavicles stay still, so a jump's energy has no source. She says this is about as common as the weight fault (A:390-404, A:490-492).
- Twinning and an even cadence (A:360-366, A:540-552).
- A soft landing where the feet slowly scoot. Fix: make the contact faster (A:438-446). A smudgy landing that sinks too far. Fix: tighten it (A:656-660).
- Arms twisted by gimbal problems. Fix: key every frame until it is fixed (A:906-912), or delete the keys and start over (A:420-424).
- A leg foreshortened toward the camera reads as boring (A:764-766).
- Endless polishing. Fix: the producer calls it done (A:848-856).

### A10. Lessons for our agents (animation)
| lesson | applies to | file:line | strength |
| --- | --- | --- | --- |
| The animator gets the required clip list and gameplay lengths from design, and fits motion inside them | animator, game-designer | A:172-174 | stated principle |
| Involve the animator (and rigger) at concept time to say what is feasible, or what more is possible | orchestrator, game-designer, animator, character-rigger | A:184-190 | stated principle |
| Plan the centre of gravity first. Every limb lift needs a visible weight shift or contact. Use this as a review check | animator, art-director (motion review) | A:92-100, A:456-474 | stated principle |
| Check rhythm and symmetry: no even cadence, no twinning, offset limbs for two reads | animator; vfx-designer (spawn timing) | A:360-366, A:540-552, A:716-724 | stated principle |
| Judge silhouette from the real game camera. An iconic shape beats physical correctness | animator, art-director, character-rigger, modeler | A:158-162, A:702-708, A:760-766 | stated principle |
| Keep timing editable: key the whole body together while blocking, retime by moving keys, cut a frame for impact | animator | A:434-438, A:446-448, A:808-816 | example |
| Rig requirements implied by her workflow: world-space head and shoulder option, IK hand mode, finger controls, eye bones, hair chain | character-rigger, animator | A:136-146, A:912-928, A:984-1034 | example |
| Priority order: root cadence, poses, flow and offset first; hair and face last. Budget effort this way | animator, orchestrator | A:970-982 | stated principle |
| Character subtext drives every motion choice. Read the character brief before keying | animator, film-director, game-designer | A:42-52, A:102-104, A:620-622 | stated principle |
| The same key poses can tell different stories. Offering two variants is cheap | animator, film-director | A:1052-1068 | example |
| A fast "bursty" move can let the engine interpolate between nearly adjacent keys, but still shows a contact | animator, feature-builder | A:468-474 | passing remark |
| Do not get attached to keys. Delete and redo when stuck | animator | A:420-432 | stated principle |

---

## V. VFX (ep6)

### V1. Speaker, role, team, what the episode covers
- Jonathan Shishido, VFX artist on Teamfight Tactics (V:19). As an intern on League's skins team he made the Tellstones ward and then the whole Elderwood Rakan kit (V:146-154). He then joined TFT (V:154). He is proudest of the Set 11 Encounters and the Set 9.5 Gangplank ship explosion (V:178-185).
- The episode: a trait "celebration" effect, which plays when a trait threshold is met (Invoker trait, two units on the board), from the drawn prompt "happy storm" (V:28-33). He works through shape language, colour and timing (V:24), in 3 hours instead of his usual 3 days (V:25). For the show he deliberately breaks TFT's limits (V:54, V:63-64, V:251-252, V:329-330, V:354-355). The engine is Riot's own (V:57-61).

### V2. What great work looks like (checkable signs)
- **Gameplay clarity at all times.** Celebrations stay inside one hex, with noise and brightness kept down (V:49-53). Several large effects at once can distract a player into losing a round (V:51-52).
- **No vertical space.** A high effect can block the enemy bench during scouting, which is unfair (V:70-80). His normal height is about 400 units, with a short duration (V:73-74).
- **Lead the eye.**
  - Show a clear source of power. Put the brightest part on the unit's chest, or wherever the player should look (V:131-136).
  - Motion also leads the eye: clouds swirl inward to the centre (V:175-176, V:186-189).
  - After the hit, move attention down, with a darker top and a brighter bottom (V:228, V:234-238).
- **Value.** Do not blow out to white. Save pure white and black for what must pop (V:163-170). Put a saturated alpha layer around a bright additive core so the colour survives (V:171-174).
- **Colour.**
  - Mood: dark navy reads as a lightning storm, and warm pink and orange read as happy (V:107-110).
  - Meaning: green is healing and red is damage. Poison uses purple so it is not mistaken for healing (V:191-193).
  - Shape language tells the player whether something protects or hurts them (V:191, V:367).
- **Story.**
  - An effect needs "a beginning, a middle, and an end" (V:204-206).
  - The hit is the cause-and-effect moment (V:207-208), with ramp-up energy before it (V:155-157, V:255-259).
  - His story: clouds swirl in, electricity builds, a burst, candy rain, candy piles up (V:292-294).
- **No "popcorning"**, where each particle shows as a separate pop. Fix it with blended background layers and opacity fades, not scale alone (V:113-114, V:342-346).
- **Variation.** Random spawn rotation, a scale range and random death times (V:315-321, V:339-341).
- **Believable bounds.** Particles stay on the stage (V:333-336).
- **Within budget.** Tech limits, texture memory and time all apply (V:37). Meshes are expensive; never spawn many (V:306-308, V:337).
- **Flashing.** A strobe behind the core is acceptable at reduced opacity, but the core itself must not strobe (V:198-203).

### V3. The steps he follows, in order
1. Read what the effect means in gameplay (V:30-33).
2. Treat the prompt or concept as a suggestion (V:34-38).
3. Pull existing assets: League effects, his own and colleagues' effects (V:41-45, V:126-128, V:275-276, V:282-286).
4. Block the volume, size and board placement (hex size, height) (V:45-82, V:96-106).
5. Test in game early and often (V:65-68, V:128-129).
6. Do a colour pass for mood and fix popcorning (V:107-124).
7. Add a focal point: paint a glow texture, then ramp its size and brightness up (V:131-160).
8. Fix value (additive versus alpha) (V:162-174).
9. Add motion toward the focus (V:175-176, V:186-189).
10. Build energy (V:196-203).
11. Lay out the story beats: place the hit frame, then the aftermath of rain and candy (V:204-229, V:275-279, V:282-326).
12. Tune timing by feel, in game:
    - the hit moved 0.1 s later, to 1.6 s (V:232-233);
    - the rain moved from 2.0 s to 1.8 s (V:277-278);
    - the floor candy starts at 2.2 s, after the falling candy (V:324-326);
    - the clouds should stop spawning at the hit (V:266-270), which he skipped for lack of time (V:273).
13. Polish: variation, fades, colour match (V:315-351).

In this rushed run he places the hit without much thought to timing (V:226-227). In his advice he still calls timing very important (V:367-368).

### V4. References and research
- **Always use reference.** Watch a campfire video, or go outside to watch a storm. Observation is key. He keeps a Pinterest board of flames and lightning (V:387-391).
- **Act it out** with your hands while making the sound effects with your voice, the way animators act in a room (V:218-222).
- Riot's earlier educational videos (V:220, V:369).
- Concept art from a concept artist (V:36).

### V5. Self-review before showing anyone
- Check in game, not only in the viewport (V:65-68, V:129).
- Check against the gameplay rules: footprint, height, the enemy bench (V:49-80). Does the effect block items, benches, gold or units (V:354-355)?
- Check for white blowout (V:163-170), popcorning (V:113-114, V:342-344) and spawns off the stage (V:333-336), and catch timing that is off by a small amount (V:277-278).
- For a portfolio, be able to explain why you made each choice and what you would improve (V:382).

### V6. Collaboration
- **Inputs:** the gameplay trigger and purpose (V:30-33), and a prompt (V:28) or concept art (V:36). He tells the concept artist up front that he will probably diverge because of tech limits, texture memory and time (V:36-37).
- **Reuse of others' work:** League skin effects, colleagues' effects, someone else's candy meshes (V:41-44, V:306).
- **Assignment:** his manager asks who wants a piece, and artists volunteer (V:180).
- **Size limits:** normally someone stops oversized effects. He says that today nobody is there to say no (V:54) [inference: a reviewer normally enforces the limits].
- **Other skills:** he also makes meshes, scrolling textures and texture paint, may animate, and handles composition (V:182-183, V:383-386).
- **Sound:** he only voices sounds himself while acting out (V:218-219). Work with a sound designer: **absent**.
- **Animation:** no unit animation drives this celebration's timing. Animation-to-VFX timing: **absent**.
- **Timing ownership:** he times the effect's internal beats himself (V:232-233, V:277-278, V:324-326).

### V7. Review and approval
- No review happens in the episode. A gatekeeper on size is implied (V:54). A portfolio review expects reasons for each choice (V:382). Stages and rounds: **absent**.

### V8. Order of work
- Purpose, concept, reuse, shape and placement, in-game test, colour, focus, energy, story and timing, polish (V:30-351, as in V3). The work is trial and error (V:99).
- Going back: after going too big at the start, he restarted small (V:122-123).

### V9. Mistakes he names, and the fixes
- He checked only in the viewport, so the cloud rendered on the units' bodies. Then he raised it too high (V:65-70).
- Too high blocks the enemy bench (V:70-80).
- He started too big, which caused popcorning. Fix: start small again (V:113-114, V:122-123).
- Bad colour choices (V:120).
- Six cores stacked on each other blew out to white (V:170).
- Fading by scale only caused popcorning (V:342-344).
- Candy spawned off the stage (V:333-336).
- Too many meshes or particles (V:264-265, V:306-308, V:337).
- Moving the pivot means changing every emitter by hand (V:249-250).
- Elements lingered after the hit (V:234-236, V:279).

### V10. Lessons for our agents (VFX)
| lesson | applies to | file:line | strength |
| --- | --- | --- | --- |
| Size the effect to the importance of its event. A routine celebration stays small, short and low | vfx-designer, game-designer | V:49-53, V:73-74 | stated principle |
| An effect must never hide information the player or an opponent needs (benches, items, units). Make this a review check | vfx-designer, game-designer, reviewer, ui-ux-designer | V:70-80, V:354-355 | stated principle |
| Put the brightest point where the player must look. Save pure white and black. Use a saturated alpha around an additive core | vfx-designer, art-director, ui-ux-designer, environment-designer | V:131-136, V:163-174 | stated principle |
| Use colour meaning consistently, and avoid colours one meaning could be mistaken for (poison as purple, not green) | vfx-designer, art-director, ui-ux-designer | V:191-193 | stated principle |
| Structure every effect as build-up, hit, aftermath, and name the hit frame | vfx-designer, sound-designer, animator | V:155-157, V:204-210, V:228-229 | stated principle |
| Verify in game from the player camera, not in an editor viewport | vfx-designer, studio-operator, environment-designer | V:65-68, V:128-129 | stated principle |
| Tune beat timing in small steps (about 0.1 to 0.4 s) by watching in game. Secondary layers start after the hit | vfx-designer | V:232-233, V:277-278, V:324-326 | example |
| Prevent popcorning: blend layers, fade opacity (not only scale), vary rotation, scale and lifetime | vfx-designer | V:113-116, V:315-346 | example |
| A concept is a suggestion inside tech, memory and time limits. Tell the concept's author about planned changes up front | vfx-designer, art-director, modeler, orchestrator | V:36-37 | stated principle (his practice) |
| Reuse existing effects and assets before building new ones | vfx-designer, modeler, orchestrator | V:41-44, V:306 | stated principle |
| Mesh particles cost a lot. Cap spawn counts | vfx-designer, performance-engineer | V:306-308, V:337 | stated principle |
| A flashing layer sits at low opacity behind the focus; the focus itself must not strobe | vfx-designer | V:198-203 | passing remark |
| Act the effect out with hands and voiced sounds before building | vfx-designer, sound-designer, animator | V:218-222 | stated principle |
| Use observed real reference and keep a reference board per material | vfx-designer | V:387-391 | stated principle |

---

## S. Sound design (ep7)

### S1. Speakers, roles, team, what the episode covers
- **Brad Beaumont:** senior manager of Sound Design at Riot and co-sound supervisor on Arcane (S:8-9). Before that he was League's audio director and worked on champion updates and cinematics (S:119-130).
- **Eliot Connors:** principal sound designer and co-supervising sound editor on Arcane (S:9-10), with a film background (S:255-271).
- **The episode:** a one-hour blind challenge. Jinx's Zapper (Arcane episode 204) is redone with "ice", drawn from a hat. They record props, turn them into "building blocks", edit to markers and combine the results (S:11-18, S:37-49). None of it ships (S:27-29).

### S2. What great work looks like (checkable signs)
- **Storytelling across all the audio.** Music, dialogue, sound design, backgrounds and foley each tell only part of the story. Edited and mixed together, they carry it and put the director's vision in place (S:30-35).
- **Music and sound designed together:** hitting beats together and hitting the cuts (S:198-202).
- **The theme matches a gameplay attribute.** The Zapper slows enemies, so the ice spreads and slows. Crumpled foil gives a slow crumble for the slow (S:19-21, S:99-101).
- **A signature tone** for League weapons (S:41-44).
- **Every stage of the action has a sound:** load, charge, second charge, shot, travel, impact. The travel stage is "OML", short for "On Missile Launch" (S:219-222, S:273-275).
- **A layered weapon shot** (S:384-396, S:426-428, S:505-507):
  - low-end body (a small drum);
  - high-frequency transient tick (a metal ball on glass);
  - concussive crunch (palm fronds);
  - report, the echo off the environment (pompoms);
  - a high "ting" for the gun's firing pin.
  
  A tail ends the impact (S:576-577).
- **Space.** A reverb tail makes a sound live in its space. Elements are pushed to the back of the room as needed (S:249-252, S:580-583).
- **Clean, pure tonal layers** are kept separate from mechanical and explosive layers, so each can be processed on its own (S:322-325, S:334-335, S:345-347).
- **Ambience and foley sell the world:** wind, snow (a rain stick), coat rustle, icy footsteps (S:550-562).
- **Not everything needs processing** (S:454-455, S:507).
- **Higher fidelity** would use real gunshot transients and natural wind recordings (S:597-601).

### S3. The steps they follow, in order
1. Get the scene and the theme (S:11-18). Tie the theme to the weapon's gameplay (S:19-21).
2. Watch the scene (S:22-26).
3. Make a rough plan: setting, action sequence, signature tone, mechanism, magic source, impact (S:37-47).
4. Collect props and record them (S:48, S:56-111). They use an X/Y stereo pair and a 100 kHz microphone whose recordings are pitched down (S:65-69). Normally they record for much longer (S:77).
5. Cut the recordings into pieces, remove talk and put them in the shared library (S:49, S:113-118). Normally they also clean and master the recordings (S:283-284).
6. Split the work by aspect (S:50-53, S:139-141).
7. Make building blocks:
   - process raw recordings through pitch, low-cut EQ, compression, granular echo, transient shaping, reverb, delay, compression again, exciter and saturation (S:142-177, S:224-254, S:292-317);
   - stack synthesisers for the tonal parts (S:327-347).
8. Set up the editor session: a template with grouped tracks (S:186-209), frame-accurate markers at sync points and scene cuts (S:211-215), and markers named for each stage (S:273-275).
9. Pick the best takes, perform them through a sampler, splice samples into each other, apply phase effects and Doppler (S:280-290, S:353-376, S:438-492).
10. Place layers on the markers: mechanism, shot, charge, impact, ambience, foley (S:493-562).
11. Bring in the partner's material and review it together. Add a tail and place it in the space (S:564-583).
12. Listen to the shot alone with the backgrounds muted, then to the whole scene (S:587-590).

On the show itself, they mixed as they went and pre-mixed in stems ("pre-dub") before the final mix (S:199-204).

### S4. References and research
- Watch the scene first (S:22-26).
- **IP history.** Years on League informed what Arcane should and should not sound like, and some original Jayce and Vi kit sounds went into the show (S:131-137).
- **Record props and everyday things.** Carry a recorder everywhere (S:56-111, S:607-608).
- **Shared library** with more than a decade of recordings (S:602-606). A device built to record rope creaks for one champion (Ivern) was reused for vines in the show (S:106-107).
- **Study films and games,** and try to recreate what you hear (S:612).

### S5. Self-review before showing anyone
- Look at the waveforms of what was recorded (S:311-314).
- Compare the raw recording against the processed one (S:318-321).
- Hear the hero sound alone, then in full context (S:587-590).
- Name what is still weak (S:597-601).
- Do not be precious about your work; some of it will be bad (S:615).

### S6. Collaboration
- **Director:** sound serves the director's vision (S:33).
- **Dialogue and music inputs.** Brad edited the dialogue and passed it to Eliot. Music came from Riot's in-house music team. Eliot mixed as he went (S:195-199).
- **Music and sound:** a lot of time went into making them work together on beats and cuts (S:198-202).
- **Picture to sound:** they place frame-accurate markers at picture sync points (for example a gauntlet hit) and at scene changes (S:211-215).
- **Two designers, parallel work.** They split by component: Brad did the tonal parts and the shot; Eliot did the ice, the mechanism and the environment. They worked in separate rooms and handed off through the shared library tool and clean exports (S:139-141, S:316-317, S:345, S:494, S:522-526, S:565).
- **Redundant attempt:** both made a gunshot, and the best parts were used (S:527-538, S:569-571).
- **Merge session:** Brad brought reversed recordings for a charge-up and Eliot pitched them. Both shaped the decision (S:572-577).
- **Library sharing across Riot** is what they call the studio's "secret sauce" (S:114-118, S:605-606).
- **Timing.**
  - Sound follows picture timing, through markers on picture events (S:211-215).
  - Sound and music time themselves to each other's beats and to the cuts (S:201-202).
  - The picture edit sets the timing and sound is designed to it [inference from S:211-215].
  - Asking picture to change for sound: **absent**.

### S7. Review and approval
- The target is the director's vision (S:33).
- Mixing early produces notes early, so problems get fixed before the final mix. The final mix can then focus on the big items (S:199-204). Who gives those notes: **absent**.
- The two designers review each other's work (S:564-592), and their advice is to ask for feedback (S:614).
- The number of rounds: **absent**.

### S8. Order of work
- Watch, plan, record, edit, library, building blocks in parallel, edit to markers, merge, mix (S:22-49, S:139-141, S:211-215, S:564-590).
- **Show level:**
  - pre-mix and mix during production, not only at the end (S:199-204);
  - dialogue is edited before it reaches the mix (S:195-196);
  - music arrives from the music team and is mixed with the sound design as scenes are built (S:197-199).
- **Going back:** early notes feed fixes (S:200).

### S9. Mistakes they name, and the fixes
- Few are named. Over 20 years they learned what not to do as much as what to do (S:299-301).
- They skipped recording cleanup for time (S:283-284).
- Wind made from whistles lowered fidelity (S:601). A gunshot made from a kid's drum lacked a real transient (S:599).
- One sound was too loud for the room (S:533).
- A dry sound got a rendered reverb tail (S:514-518).

### S10. Lessons for our agents (sound)
| lesson | applies to | file:line | strength |
| --- | --- | --- | --- |
| Before designing, place frame-accurate markers on every picture sync point and every cut | sound-designer, film-director | S:211-215 | stated principle (their method) |
| Name the stages of an action (for example load, charge, shot, travel, impact) and give each its own sound | sound-designer, vfx-designer, animator | S:219-222, S:273-275 | example |
| Mix early and pre-mix before the final mix: problems surface early and get fixed | sound-designer, orchestrator, film-director | S:199-204 | stated principle |
| Music and sound must agree on beats and cuts. Plan them together | sound-designer, film-director | S:198-202 | stated principle |
| Each audio element tells only part of the story. Judge them together, against the director's intent | sound-designer, film-director | S:30-35 | stated principle |
| Layer weapon sounds by job: low-end body, transient, crunch, report and tail, high "ting" | sound-designer | S:384-396, S:505-507, S:576-577 | example |
| Keep clean tonal layers separate from mechanical and explosive layers | sound-designer | S:322-325, S:345-347 | stated principle |
| Tie sound to a gameplay attribute (slow means a spreading crumble) and give weapons a signature tone | sound-designer, game-designer | S:19-21, S:41-44, S:99-101 | stated principle |
| Split a big sound job by component, work in parallel, hand off clean exports via a shared library, then merge and review together | orchestrator, sound-designer | S:50-53, S:139-141, S:345, S:564-592 | example |
| Judge the hero sound alone, then in full context | sound-designer | S:587-590 | example |
| Keep a growing shared library of building blocks for every project | sound-designer, orchestrator | S:113-118, S:602-606 | stated principle |
| Respect the IP's sound history. Reuse or echo iconic older sounds where they fit | sound-designer, art-director | S:131-137 | example |

---

## C. Combined

### C1. Speakers, roles, what the set covers
| Ep | Craft | Speaker(s) | Product | Challenge | Evidence |
| --- | --- | --- | --- | --- | --- |
| 4 | Gameplay and character animation | Lana Bachynski, senior animator, R&D | League | Akali pose-to-pose weight shift, about 3 h | A:14, A:38-40, A:976 |
| 6 | VFX | Jonathan Shishido, VFX artist | TFT | "Happy storm" trait celebration, 3 h (normally 3 days) | V:19, V:25, V:28-33 |
| 7 | Sound design and editing | Brad Beaumont and Eliot Connors, co-supervisors | Arcane (film) | Ice version of Jinx's Zapper, 1 h | S:8-18 |

Ep7 is film sound, not game sound. Its timing model (sound follows a picture edit) carries over to cutscenes directly. For gameplay it applies only by analogy [inference].

### C2. What great work looks like, across crafts
- **Clarity and hierarchy first.**
  - VFX keeps the board readable and puts the brightest point on the focus (V:49-80, V:131-136).
  - Animation reads from the game camera's silhouette and uses offset to create separate reads (A:760-766, A:716-724).
  - Sound judges the hero sound with the backgrounds muted (S:587-590).
- **The same beat structure, in three vocabularies [inference].**
  - Animation: hold and tighten before a spring, then push, hang, contact, catch, settle (A:450-454, A:342-352, A:438-446).
  - VFX: ramp up, hit, aftermath (V:155-157, V:204-210, V:292-294).
  - Sound: load, charge, shot, travel, impact, tail (S:219-222, S:273-275, S:576-577).
- **Variation and no machine regularity.** No twinning and no even cadence in animation (A:360-366, A:540-552). Varied rotation, scale and lifetime in VFX (V:315-341). In sound, samples spliced into each other to make long varied versions (S:438-443).
- **Believability inside stylization.** Animation keeps just enough physics (A:476-480). VFX keeps particles on the stage (V:333-336).
- **Theme and character drive choices.** Character subtext in animation (A:42-52). Mood colour in VFX (V:107-110). IP history and the gameplay attribute in sound (S:131-137, S:19-21).

### C3. Common step pattern
Purpose and brief, then reference and existing material, then a rough block-out, then a check in the real context, then timing, then layered polish, then detail last.
- Animation: A:42-52, A:78-82, A:434-438, A:978-982.
- VFX: V:30-33, V:41-45, V:65-68, V:232-233, V:339-351.
- Sound: S:11-26, S:113-118, S:211-215, S:587-590.

### C4. References and research, across crafts
- **Acting it out** is shared by all three crafts: animators act with sticks (A:632-636); the VFX artist acts with hands and voiced sounds (V:218-222); the sound designers perform samples like an instrument and use their own voices (S:397, S:539-546).
- **Real-world observation or recording:** anatomy and figure study (A:286-306); a storm or campfire (V:387-391); props and an always-on recorder (S:607-608).
- **Existing studio assets:** concept art (A:530-532, V:36), the League effects library (V:41-44), the shared sound library (S:113-118).

### C5. Self-review, across crafts
- Check in the real viewing context: the render or game camera (A:158-160, A:384-386, A:760-764), in game (V:65-68), the hero sound alone and then in context (S:587-590).
- Delete and restart without attachment (A:420-432, V:122-123, S:615).
- Name what is still weak before handing over (A:818-828, S:597-601).

### C6. Collaboration and timing dependencies (the key question)
| From | To | What passes | Who sets timing | Evidence |
| --- | --- | --- | --- | --- |
| Design | Animation | Required clips and their gameplay frame lengths | Design | A:172-174 |
| Tech art (rig) | Animation | The rig | (none) | A:58-62, A:164-166 |
| Concept art | Animation, VFX | Pose and look guidance. The craft may diverge for readability or budget and says so up front | (none) | A:530-532, A:704-708, V:36-37 |
| Gameplay event | VFX | The trigger and meaning (trait threshold reached) | Gameplay | V:30-33 |
| Animation | VFX | VFX runs partnered with animation, "a little bit staggered" | Animation leads | A:166-168, A:174-178 |
| Animation | Audio | Animation changes, so audio can add impact | Animation leads | A:164-166, A:178-180 |
| Picture (edit or animation) | Sound | Frame-accurate sync markers and cut points | Picture | S:211-215 |
| Music | Sound | Beats and cuts are matched | Joint | S:198-202 |
| Dialogue editor | Sound editor and mixer | Edited dialogue | (none) | S:195-196 |
| Sound designer | Sound designer | Building blocks via the shared library and clean exports | (none) | S:139-141, S:345, S:565 |
| VFX (inside one effect) | VFX | Internal beat times (hit, rain, pile-up) | VFX | V:232-233, V:277-278, V:324-326 |

- **Who can push back:**
  - the animator, early, on feasibility in both directions (A:184-190);
  - the VFX artist, on a concept, for tech, memory and time reasons (V:36-37);
  - a concept artist, on an animator's silhouette choice (A:704-708);
  - the producer, who ends polishing (A:852-856).
- **Absent** in all three files:
  - an explicit sync negotiation between VFX and sound;
  - animation event markers handed to VFX or sound in a game;
  - sound or VFX asking animation to retime;
  - any sign-off chain.
- **[inference] A single timing spine.** Design sets the gameplay length (A:172-174). The animator sets the beats inside it (keyframes as story beats, A:950-958). VFX follows, staggered (A:166-168). Sound places frame-accurate markers on the same picture events (S:211-215) and names the stages (S:273-275). The lesson for us: one owner writes a named beat list with frame times per action, and VFX and sound key to it. Any change to it must be sent downstream (A:178-180). How Roblox carries such markers is not covered in these transcripts; check the docs.

### C7. Review and approval, across crafts
- Formal gates, named reviewers and round counts: **absent** in all three.
- What exists:
  - producers end the work (A:852-856);
  - an implied gatekeeper on VFX size (V:54);
  - the director's vision as the target (S:33);
  - early mixes that produce notes (S:199-204);
  - peer merge and review (S:564-592);
  - "ask for feedback" (S:614; A:782-796).

### C8. Order of work, across crafts
- **First:** design length and purpose (A:172-174, V:30-33). Animators and other crafts join early to check feasibility (A:184-190).
- **Then:** the rig, then animation (A:58-62, A:164-166).
- **Then:** VFX, staggered behind animation (A:166-168); audio after (A:164-166).
- **In parallel:** sound designers split by component (S:139-141); music and sound are built and mixed together as scenes come in (S:197-204).
- **Locked when:** **absent**. The only lock-like point is the final mix, after early pre-mixing (S:199-204).
- **Going back upstream:**
  - animation changes are sent on to audio (A:178-180);
  - early mixes create notes to fix (S:199-204);
  - VFX diverges from the concept with stated reasons (V:36-37).

### C9. Mistakes, across crafts
- **Judging outside the real context:** viewport versus game (V:65-68); work view versus render camera (A:384-386).
- **Too big or too loud:** effect footprint and height (V:49-80), white blowout (V:163-170), a sound too loud for the room (S:533).
- **Mechanical sameness:** twinning (A:540-552), popcorning (V:113-114, V:342-344).
- **Attachment to work:** the cure is deleting and restarting (A:420-432; S:615).
- **Over-polishing:** stopped by the producer (A:848-856).

### C10. Cross-craft lessons for our agents
| lesson | applies to | file:line | strength |
| --- | --- | --- | --- |
| Design owns each action's gameplay length. The animator fits beats inside it, VFX follows staggered behind animation, and sound keys to the picture events. Run the job in that order | orchestrator, game-designer, animator, vfx-designer, sound-designer | A:166-168, A:172-174, S:211-215 | stated principle (A), example (S); the ordering is inference |
| Keep one named beat list per action (anticipation, hit or release, impact, tail) with frame times. VFX and sound key to it; changes go downstream | animator, vfx-designer, sound-designer, film-director, feature-builder | A:950-958, A:178-180, V:204-210, S:273-275 | inference from stated practices |
| When upstream timing changes, tell audio and VFX | animator, orchestrator | A:178-180 | passing remark |
| Bring motion, VFX and sound crafts in at concept to flag feasibility and wider possibilities | orchestrator, game-designer | A:184-190 | stated principle |
| A concept or brief is a target, not a contract. A craft may diverge for readability or budget but must say so up front | vfx-designer, animator, modeler, art-director | V:36-37, A:704-708 | stated principle |
| Every craft checks its work in the real player context before showing it: game camera, in game, in the full mix | animator, vfx-designer, sound-designer, studio-operator | A:384-386, A:760-764, V:65-68, S:587-590 | stated principle |
| Clarity outranks spectacle for routine gameplay feedback. Effects and sounds must not hide what players need | vfx-designer, sound-designer, game-designer, ui-ux-designer | V:49-80, S:587-590 | stated principle (V); example (S) |
| Act the moment out (body, hands, voice) before building, across motion, VFX and sound | animator, vfx-designer, sound-designer, film-director | A:632-636, V:218-222, S:539-546 | stated principle |
| Reuse a shared, growing library (effects, sounds, meshes) before making new assets | orchestrator, vfx-designer, sound-designer, modeler | V:41-44, S:113-118, S:602-606 | stated principle |
| Mix early to get notes early. For our studio, review a combined animation, VFX and sound pass early rather than each craft alone at the end | orchestrator, film-director, art-director, sound-designer | S:199-204 | stated principle (S); applying it across crafts is inference |
| Effort goes to the bulk first (timing, poses, layers), then details. Someone outside the craft calls "done" | orchestrator, all crafts | A:970-982, A:848-856 | stated principle |
| Do not be precious. Delete and redo, and ask for feedback | all crafts | A:420-432, S:614-615, V:122-123 | stated principle |
