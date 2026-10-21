---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J016 transcript extraction (R00 core fundamentals series); owner-supplied Riot transcripts in Downloads, not in git"
supersedes: []
---
> Author: research reader · claude-opus-5-5 · default · 2026-10-21 (J016 transcript extraction; lead spot-read)
# Riot "So You Wanna Make Games??" — core extraction (A-core)

> Author: researcher · claude-opus-5-5 · default · 2026-10-21
> Source: `C:\Users\Firew\Downloads\Riot Core fundemental Ideas.txt` (5983 lines, all read). Cited as `R:<line>` or `R:<a>-<b>`. Caption text sits on the odd lines; timestamps sit on the lines between them.
> The source is data. Everything below is paraphrase. Quotes are short and few.
> Weight caveat: the series calls itself a springboard, not complete, and says it may be wrong in places (R:51-55). It is aimed at beginners. Its principles are clear, but it says little about formal process and almost nothing about sign-off.

---

## 1. Speakers and disciplines covered

| # | Video / craft | Lines | Who speaks (only what the transcript shows) | Notes |
| --- | --- | --- | --- | --- |
| 1 | Intro: what game art is; clarity, satisfaction, style; visual hierarchy, contrast, shape/size, color, detail | R:1-514 | Narrator plus a comic "learner" voice; career advice from Lisa, Sean, Tyson, Moby, Evan and Santtu (R:394) | The 10-part outline is at R:23-33 |
| 2 | Concept art | R:515-1056 | Riot concept artists; one says they designed the new Irelia (R:996) | Includes a live staff-design exercise (R:766-800) |
| 3 | 3D character art | R:1058-1663 | Riot character artists (no names given) | Garen and Nunu examples |
| 4 | Environment art | R:1664-2283 | Riot environment artists; one used to work at Insomniac on Ratchet & Clank (R:1887-1889) | |
| 5 | Tech art (rigging, tools, pipeline, shaders, simulation) | R:2284-2895 | Riot tech artists (one moved from Philadelphia, R:2763-2765) | |
| 6 | Character animation | R:2896-3420 | Riot animators (one trained at a CG masterclass and an online school, R:3392-3394) | Garen pose and Teemo ball-bounce demos |
| 7 | VFX | R:3421-4014 | Riot VFX artists; one made Yasuo's wind wall and Janna's skin effects (R:3772-3782) | Fireball breakdown |
| 8 | Sound design | R:4016-4497 | Riot sound designers; one built the "Creaker" foley prop for Ivern (R:4366-4370) | Many audio demos have no words, so the transcript is thin there (R:4123-4125, R:4160) |
| 9 | UI / UX / visual design / motion graphics | R:4498-5103 | Riot UI and visual designers; the League Client Update is the example (R:4741-4777) | |
| 10 | Game design | R:5104-5983 | Riot game designers; one worked on League champion kits (R:5805-5817) | Running joke: this video should have come first (R:5136-5144) |

The transcript has no speaker labels, so no quote can be tied to a named person.

---

## 2. Core principles of good game art (each one is a rule an agent can check)

| # | Rule | Line |
| --- | --- | --- |
| P1 | "Art" means everything the player sees **and hears**: characters, effects, enemies, environment, UI, animation and sound. The visual direction has to cover sound too. | R:72-78 |
| P2 | Art is not decoration. The artist's job has three parts: **clarity, satisfaction, style**. | R:86-94 |
| P3 | **Clarity:** critical facts are clear at once: where to go, where I am, who is an ally and who is an enemy, how much health I have. They stay clear when a lot happens at the same time (a team fight). | R:101-131 |
| P4 | **Satisfaction:** every player action gets clear, responsive feedback. A button press changes something at once, success feels good and failure feels bad. Possible forms: hit pause, a big ceremony, flowing momentum, or simply running and jumping. | R:136-164 |
| P5 | **Style:** one cohesive style that sets an emotional tone. The levers are color, character design, environments and how far proportions are pushed. The same gameplay in a different style feels different (PUBG vs Fortnite). | R:175-219 |
| P6 | **Visual hierarchy:** the most important information is the easiest to see. Every game needs it, because thousands of art pieces will clash without it. | R:221-230 |
| P7 | **Contrast** sets both focus and mood. To make one thing the focus, lower the contrast of everything else (the checkerboard example). | R:232-240, R:271-285 |
| P8 | Contrast channels: shape, color, saturation, size, layout, position. Sound, music and narrative also work through contrast. | R:242-252 |
| P9 | Light against dark (value) is the base contrast. The UI keeps values consistent across the whole game. | R:261-269, R:4969-4973 |
| P10 | **Shape:** clear silhouettes. Shapes act as arrows that show where to look, what is dangerous and what is safe. | R:302-314 |
| P11 | **Size:** the most important enemy is the biggest. | R:316-320 |
| P12 | **Color:** keep stark color contrast for the things players must see (Superhot's enemies, Mirror's Edge's jump points). | R:329-335 |
| P13 | **Detail** is a hierarchy tool. Put areas of rest next to areas of high detail, and do not fill every object with detail. | R:346-362 |
| P14 | Realistic styles imply detail too. Detail drops with distance (atmospheric perspective), which leads the eye and adds depth. | R:368-378 |
| P15 | A character must read at the size it really appears on screen. Cut it down to its iconic elements, and choose the right ones. | R:1115-1170 |
| P16 | **Restraint:** if every effect is huge, none stands out. In the series' words, "nothing will be epic and loud" (R:3654). | R:3626-3654 |
| P17 | **One shape language:** each shape means the same thing everywhere in the game. | R:3692-3726 |
| P18 | **One set of meaning rules** for color, text and screen position across every screen. Everything affects everything else. | R:4721-4737 |
| P19 | Motion and physics stay consistent, so players can predict what their actions will do. | R:2977-2983 |
| P20 | The wind-up before an attack must read. It is among the most important things a player needs to know. | R:2965-2971 |
| P21 | Mechanics and art say the same thing. When they do not, the game feels unnatural (bushes that stop bullets, open doorways you cannot walk through). | R:5393-5415 |
| P22 | Fairness comes from clear expectations and consistent design, and it is separate from difficulty. | R:5630-5650 |
| P23 | Visual design makes the message understood; motion makes it felt. | R:4855-4861 |
| P24 | Function comes first, and art supports the information. Polish cannot rescue a bad design. | R:4867-4885 |
| P25 | Aim at a specific target audience, not at work that everyone merely tolerates. | R:1040-1056 |

---

## 3. Per craft

### 3.1 Concept art (R:515-1056)

**(a) What great work looks like (checkable signs)**
- It solves a named team problem with a visual answer. Drawing is only the tool for communicating it (R:536-558).
- It stays inside the stated constraints: lore, setting and tone (R:620-630), camera perspective (R:632-642), mechanics (R:644-652), even stats such as HP (R:656-662).
- The moodboard is narrow and carries short pillars (R:702-708).
- The shape language and coloring carry the idea (R:1006-1012).
- A sketch gets the essence across well enough that the team understands it and gets excited (R:752-760).
- It is specific and made for a target audience. Some people disliking it is acceptable (R:1040-1056).
- An evolved archetype shows that the artist understood the archetype's history first (Irelia as a blade dancer, R:986-1000).

**(b) Steps, in order** (the series' own recap: R:920-936)
1. Find out what problem you are solving (R:600-608).
2. Set the constraints: theme, perspective, mechanics, numbers (R:616-662).
3. Research: play games in the genre, collect images, visit the real place if you can (R:664-682).
4. Build a moodboard with pillars and get team feedback on it before drawing (R:684-716).
5. Ideate fast and loose: many ideas, nothing precious (R:740-760). Two-tone sketches keep the focus on big graphic shapes (R:822-834).
6. Show a broad set of ideas to the team (R:846).
7. Feedback round: ask a specific question tied to the goal, for example "which feels the scariest?" (R:860-874).
8. "Closing Doors": each cycle drops what did not work and expands what the team liked, so ideas go from broad to narrow. Do not reopen closed doors (R:840-858).
9. Present the work with conviction, because the concept artist is often the team's inspiration (R:888-892; the weak pitch at R:894-900 and the strong pitch at R:902-918).

**(c) References and research**
- Research comes after the constraints and before any drawing (R:664-682).
- The moodboard is the reference product, and it is the first thing shown (R:684-700).
- A standing "visual library": draw from life and from screens everywhere, all the time (R:958-978).
- Practice sheets of 50-100 variations under a stated constraint, e.g. magical, steampunk or necromancy staffs (R:980-985).

**(d) Self-review before showing**
- Does this push the team toward its goal, or is it only "cool"? (R:602-604)
- Use the moodboard as a gut-check on direction (R:700).
- Do the shape language and color carry the idea? (R:1006-1012)

**(e) Common mistakes they name**
- Exploring for its own sake (R:586-590).
- A scattered or too-general moodboard, which leads to confusion and pivots later (R:710-716).
- Chasing originality until it paralyzes you (R:732-738).
- Being precious about the work (R:742, R:1034).
- Overthinking small details early (R:830-832).
- Reopening closed doors (R:858).
- Broad questions such as "do you like this?" (R:866-868).
- Grand reveals (R:878-884).
- A timid presentation (R:894-900).
- Being "obsessed with making good art" instead of talking ideas through with the team (R:944-956).

### 3.2 Character art, 3D (R:1058-1663)

**(a) Signs of great work**
- It captures the character's fantasy even when the character is tiny, seen from above, blurred by speed, or only its arms show (R:1115-1129).
- It keeps the concept's iconic qualities and, where possible, makes them stronger (R:1142-1144).
- It is cut down to the *right* core elements. Garen becomes sword, pauldrons and scarf, not boots, hands and hair (R:1146-1170).
- Key proportions and silhouette are right (R:1189-1191). Detail and contrast sit on the focal points (R:1197-1199).
- The anatomy is believable, so the model also animates well (R:1481-1489).
- Invented creatures combine real anatomy (Nunu: a lion's face, a bear's pelvis, six insect arms) and still feel alive (R:1497-1523).
- The design still works when the character moves, not only in a neutral pose (R:1540-1554).

**(b) Steps, in order** (recap: R:1448-1460)
1. Get the concept from the concept artist, or make one. Treat it as the final target (R:1134-1138).
2. Name the iconic elements (R:1146-1152).
3. Build a quick proxy model from big blocks of shape and color (R:1183-1187).
4. Check proportions and silhouette with the proxy as early as possible (R:1189-1191).
5. Adjust from how the model looks *in the game*: push readability, add detail and contrast at the focal points (R:1193-1199).
6. High-poly sculpt (detail and polish) (R:1233-1241).
7. Low-poly mesh, because the engine draws every polygon in real time and millions of them kill performance (R:1260-1284).
8. UV unwrap (R:1309-1319).
9. Bake the high-poly detail onto the low-poly mesh (R:1321-1327).
10. Texture painting (R:1329-1335), or shaders: color, transparency and metal inputs, plus color, normal and height maps (R:1340-1436).
11. If the design blocks motion, adjust the model with the tech artists and animators (R:1556-1562).

**(c) References**
- The concept is the target (R:1138).
- Anatomy matters more than learning the software (R:1470-1478).
- Find reference, and study nature and how things work (R:1629-1641).
- Online communities (Polycount, ArtStation): find people to look up to and emulate (R:1599-1615).

**(d) Self-review**
- The proxy is checked in the game for silhouette and proportion (R:1189-1199).
- Is the essence still there after simplifying? (R:1162-1170)
- Can the character raise its arms without hitting its own face? (R:1550-1554)

**(e) Mistakes**
- Losing the essence, or keeping the wrong core elements (R:1162-1170).
- Weak anatomy, which looks odd and is hard to animate (R:1485-1489).
- Collars, scarves or armor that limit animation (R:1546-1554).
- High-poly meshes in the game (R:1266-1278).
- Over-cranked maps; the height map gets "too much" (R:1430-1432, a passing remark).
- Fixating on technique over artistic vision (R:1617-1627).

### 3.3 Environment art (R:1664-2283)

**(a) Signs of great work**
- It shows a believable setting *and* the gameplay-critical information (R:1831-1835). The joke "talking environments" make the point: an obvious cliff that is also clearly climbable (R:1837-1859).
- A gameplay constraint takes an in-world form: a boundary can be a wall, a building or a cliff over the sea. The best form is the most beautiful and believable one (R:1815-1829).
- Its shapes lead the eye into a clear hierarchy of focus (R:1875-1885).
- An establishing composition at the start of a level tells players where they are and what they will do (R:1887-1899).
- Light and shadow create focal points. Materials and how light hits them set the mood (R:1901-1921). A bright light can pull the eye away from a surprise (R:1923-1927).
- Large areas of rest alternate with detailed areas (R:1931-1939).
- It tells a story through layout and props: climate, age, culture, signs that people live there (R:1943-1987). Wear sits where hands go, and grime gathers around door handles (R:2229-2235).
- Scale is right. Scale cues are things the character touches: chairs, doorknobs, railings, stairs (R:2017-2025).
- It is efficient: low polygon counts, reused models and textures (R:2045-2067). Modular kits vary enough to make different looks but never read as copies; a crate turned around looks like a new crate (R:2069-2097).

**(b) Steps, in order** (R:1753-1785; recap R:2099-2131)
1. The concept artists set the environment's theme and tone (R:1753-1755).
2. The game designers build a grey-block blockout: obstacles, the player's path, where enemies come from (R:1757-1765).
3. The environment artists rough out art that carries both the concept vision and the designer's constraints (R:1767-1773).
4. Refine the models, then add textures and color (R:1775-1777).
5. Playtest a lot and gather feedback (R:1777-1779).
6. Only once the level has been playtested and works: lighting, post-processing, polish notes (R:1781-1785).
- Throughout: set priorities by what matters most to the game experience, decided with the game designers and concept artists (R:1731-1751). Keep up the back-and-forth paintovers with concept (R:1803-1813).

**(c) References**
- Research never stops. Watch how real places are laid out and look for their unique details; one artist's holiday photos are of pipes, grates, dark corners and old kitchens (R:1995-2011).
- Research tells you how to tell the place's story (R:2121-2125).

**(d) Self-review**
- Put a character in the blockout for scale. Without one, an artist ended up with a twenty-foot desk (R:2027-2035).
- Playtest (R:1777-1779).

**(e) Mistakes**
- Wrong scale (R:2017-2035).
- Flat, hard-edged, sterile props with no story (R:2217-2227).
- Building only showpiece props, never a whole environment ("make the whole bar", R:2237-2245; R:2203-2215).
- Following a reviewer's suggested fix literally, instead of finding the problem behind it (R:2175-2201; see section 5).
- Modular pieces that read as copies (R:2083-2085).

### 3.4 Tech art: rigging, tools, pipeline, shaders, simulation (R:2284-2895)

**(a) Signs of great work**
- Its main job is to make how art is made and put into the game smoother (R:2365-2369).
- Rigs bend without odd results (R:2405-2411). Controls let animators move many bones easily, like puppet strings (R:2413-2425). They handle the foot staying planted while the body moves, and a switch that lets the whole leg follow the body (swimming) (R:2427-2437).
- Tools solve the real need, not the literal request (the fish-count example, R:2481-2497).
- Implementation tools remove repeated clicks and confirmations (R:2499-2541).
- The pipeline has clear channels for handing files between people (R:2543-2567).
- Version control can show who changed what and who is working on a file (R:2583-2611).
- Naming conventions and folder structure are kept up, with mass-rename tools (R:2613-2641).
- Shader parameters are used creatively: vertex color drives terrain textures, dirt or rock collects on steep slopes, a toon look comes from clamping the light direction (R:2655-2701).

**(b) Steps**
- Rigging: (1) receive the mesh, which is stuck in its creation pose (R:2381-2385); (2) place bones inside it (R:2389-2391); (3) weight-paint each bone's influence (R:2399-2403); (4) check the bends for odd results (R:2405-2411); (5) build the animator controls (R:2413-2425); (6) solve the special cases, such as planted feet and follow-switching (R:2427-2437).
- Tool request: (1) the artist asks for a specific tool (R:2451-2455); (2) the tech artist asks "What are you trying to do?" (R:2457-2471); (3) they build the tool that serves the real goal (R:2481-2497).
- Implementation steps they automate: remove unneeded parts, set settings, name the file, split it into pieces, connect it to existing files (R:2499-2519).
- Shaders: the tech artist writes the code, or agrees with an engineer what the shader must do; then teaches artists the parameters (R:2705-2717).

**(c) References**
- Learn a free engine to learn how games are made (R:2849-2883).
- Learn programming fundamentals rather than one language's syntax (R:2781-2797).

**(d) Self-review**
- Check every bend for odd results (R:2405-2411). Not much more is said.

**(e) Mistakes**
- Building the literal request (R:2473-2479).
- Manual, repeated confirmations (R:2521-2541).
- Files deleted or overwritten when there is no version control (R:2571-2581).
- Unmanaged naming that becomes "a huge problem" (R:2633-2637).

### 3.5 Character animation (R:2896-3420)

**(a) Signs of great work**
- Three goals: actions are clearly shown, motion and physics are believable, and the character has personality (R:2941-2949).
- The wind-up before an attack reads (R:2965-2971).
- Consistent physics lets the player predict results (R:2977-2983). Motion sets the emotional tone; a huge character's movement brings fear, wonder and epic scale (R:2985-2991).
- Every action shows who this character is. The question is how *this specific* character runs (R:2993-3009).
- Poses: a simple, clear line of action that the body flows along (R:3085-3103). The center of gravity is over the feet unless being off-balance is the point (R:3105-3119). The closer a prop is held to the center of gravity, the heavier it looks (R:3121-3133).
- Personality comes from layering character-fit adjectives onto the pose. Garen: heavy, so a wider stance; defiant and proud, so chin up and chest out; noble, so heroic wind in the scarf (R:3147-3181).
- Motion: spacing and eases sell gravity (R:3199-3217). Squash and stretch sell inertia and impact (R:3219-3227).
- In a game, a character is hundreds of animations that interrupt and blend. A state machine decides how they combine under game conditions: walk, jog and run by speed; turning toward nearby characters; aim poses by mouse; handholds while climbing (R:3237-3301).

**(b) Steps, in order** (assembled from the video's own sequence)
1. Prepare: sketch, research online, and above all act the move out or film yourself (R:3012-3046).
2. Brainstorm with other animators, who give each other notes (R:3058-3072).
3. Find the key storytelling poses and plot them on the timeline (pose-to-pose, not straight ahead) (R:3354-3362).
4. Make each pose clear: line of action, balance, prop weight (R:3085-3133).
5. Make it specific with personality adjectives, and pull back if you push too far (R:3147-3181, "a little bit too far" at R:3161).
6. Add motion: spacing and eases, squash and stretch (R:3193-3227).
7. Compare against the earlier version (R:3229-3231).
8. Build the state machine logic for blends and interruptions (R:3275-3301).
9. Expect 3-5 tries at the same animation (R:3334-3336).

**(c) References**
- Acting it out is the fastest accurate reference (R:3016-3024).
- Motion reference shows body mechanics and how the silhouette changes (R:3338-3352).
- The 12 principles from "The Illusion of Life" (R:2927-2939).
- Practice variations of one exercise (heavy, light, fire, happy and sad ball) to find your weak spots (R:3380-3390).

**(d) Self-review**
- Check the line of action (R:3091-3103) and the center of gravity (R:3109-3111).
- Compare with the previous version (R:3229-3231).
- Check for overshoot (R:3161).

**(e) Mistakes**
- Even spacing, which feels wrong (R:3197-3201).
- Broken or complex lines of action, which hide the action (R:3099-3103).
- Being off balance when you did not mean it (R:3113-3115).
- Straight-ahead animation with no planned key poses (R:3354-3362).
- Showy, complex moves instead of strong basics (R:3368-3378).
- Holding on to precious ideas (R:3316-3332).

### 3.6 VFX (R:3421-4014)

**(a) Signs of great work**
- Effects run in real time, so they are built far more efficiently than film effects (R:3458-3470).
- Layered reads: **primary** (it catches the eye first), **secondary** (thematic detail), **tertiary** (low-priority support). The eye follows them in that order (R:3552-3618).
- Restraint, so each effect stands out from the others. The VFX artist's role is to communicate gameplay (R:3626-3654).
- A consistent shape language: plus signs for healing, protective circles for shields, spiky angular shapes for damage. It matters most when colors are similar (R:3692-3726).
- Color is chosen for what it must say: team (red vs green lasers), damage type (element spells), emotional tone (oversaturated fire) (R:3736-3760). Do not over-color (R:3762-3770). Use a color next to the caster model's color on the color wheel (analogous), so players can tell who cast it (R:3772-3788).
- Timing: an explosion grows very fast at first and slows as it reaches full size, rather than growing at a linear rate. The build-up before it can be timed too (R:3790-3832).

**(b) Steps** (the fireball example, explicitly "just one way", R:3620)
1. Primary read: a bright glow texture on a camera-facing card, wrapped in a half-sphere mesh with an animated fire texture scrolling across it (R:3558-3580).
2. Secondary read: a ribbon trail behind the head, with a tiling texture scrolling along it (R:3582-3598).
3. Tertiary read: a few sparks, and not too many, or they steal focus and muddy the effect (R:3600-3618).
4. Tune the speed and timing of each part (R:3790-3794).
- Context: there is no standard approach. Cards, meshes and trails are all valid; what counts is the finished result (R:3478-3502). Effects are mostly built from particle systems in the engine (R:3518-3542).

**(c) References**
- Find a lot of reference and look at it very closely (R:3884-3888).
- To learn timing, throw rocks into a still lake: there is a delay, then the splash, the beat every explosion uses (R:3890-3910).
- Joseph Gilland's "Elemental Magic" (R:3936-3950); the RealtimeVFX community (R:3922-3934).

**(d) Self-review**
- Do the tertiary parts steal focus? (R:3604-3612)
- Does this effect still stand out among all the others? (R:3640-3654)
- Is the timing linear (flat) or eased? (R:3812-3828)

**(e) Mistakes**
- Too many sparks (R:3604-3612).
- Making everything big and flashy (R:3628-3654).
- Too much color (R:3766-3770).
- Linear timing (R:3812).
- Effects that share a color and have no shape difference (R:3722-3726).

### 3.7 Sound design (R:4016-4497)

**(a) Signs of great work**
- Three jobs: **gameplay cues**, **player feedback**, **core emotion** (R:4059-4065).
- Cues make clear what is happening to you or near you: an ability is ready, you are taking damage, an enemy has spotted you (R:4067-4077).
- Feedback tells the player whether a decision was good or bad (R:4084-4090).
- Sound is an emotional driver that pulls the player in (Papers, Please; Outlast 2; Project CARS 2) (R:4093-4105).
- One sound can be re-tuned for a different mood; the same door sounds happy, sad or terrifying (R:4032-4042).
- Dynamics (attack, decay, sustain, release) are tuned for feel. A longer attack adds wind-up; a longer release makes a punch seem to go through a brick wall (R:4162-4222).
- Attenuation fits the sound: gunshots and roars carry far, footsteps and breathing do not (R:4245-4259). One sound can attenuate differently per frequency band (highs fade fast, lows carry) so near and far sound different (R:4261-4275).
- EQ cuts noise or adds intensity (R:4279-4295). Reverb glues sounds together or shows the space (hallway, bathroom, elevator, canyon) (R:4298-4326).
- Sounds are tied to game events: dialogue when entering water, the music changes on entering combat, special reactions (R:4329-4349).
- Characters sound distinct, and a sound can carry gameplay. Ivern creaks to set him apart from Maokai, and the creak on his shield warns that it is about to break (R:4366-4382).

**(b) Steps** (the video presents a toolbox, not a strict order; the order below follows the presentation and is inferred)
1. Decide which job the sound does: cue, feedback or emotion (R:4059-4065).
2. Find the parts in sound libraries (R:4351-4353).
3. If nothing fits, record foley (R:4355-4364).
4. Shape the dynamics (ADSR) (R:4167-4222).
5. Set attenuation, including per-frequency curves (R:4229-4275).
6. EQ (R:4279-4291).
7. Reverb (R:4298-4314).
8. Attach the sound to its game events (R:4329-4349).

**(c) References**
- Listen to top-quality sound libraries early, to learn what "good" sounds like (BOOM Libraries, The Recordist, HISSandaROAR) (R:4431-4447).
- Practice by stripping the sound from a film or game clip and making your own (R:4449-4477).
- Mentors and people in the industry (R:4403-4429).

**(d) Self-review**
- Listen near and far (the attenuation demo, R:4265-4273). Little else is said.

**(e) Mistakes / friction**
- Feedback on sound is hard to put into words ("more whooshiness"). Sound designers often answer without words. Learn the technical terms so you can talk about it (R:4107-4129).
- Rules held too tightly. It is fine to break them if the result sounds good (R:4483-4489).

### 3.8 UI / UX / visual design / motion (R:4498-5103)

**(a) Signs of great work**
- UX is the information architecture: where information lives and how the player reaches it, with the fewest necessary actions (R:4559-4589).
- UI is the visual layer, and it makes that flow more intuitive (R:4591-4599).
- Complex information is shown simply enough that the audience understands it and acts on it (R:4623-4629).
- It is built for the audience: what they connect with, where and how they play, what information they need and when. PC differs from mobile (R:4631-4665). Genre sets how dense the UI is; a trading card game is about 90% UI, a narrative game needs very little (R:4667-4691).
- It covers far more than the HUD: maps, character select, inventory, editors, skill trees, quest windows (R:4693-4709).
- It works as one ecosystem: one high-level flow and fixed meanings for colors, text and screen position (R:4713-4737).
- A core theme is set first (League's hextech), then strict style rules for typography, iconography, color, shape language and animation (R:4741-4777).
- Layout carries meaning through proximity: a bar next to an enemy's name is that enemy's health (R:4793-4813). Layout also sets how fast players find things, which matters for critical information (R:4815-4821).
- It balances the familiar and intuitive with creative arrangement (R:4832-4839).
- Motion follows five goals (R:4893-4949):
  - **responsiveness:** interactions are fast and fluid;
  - **intention:** motion leads focus to key actions;
  - **awareness:** elements react from where they are;
  - **consistency:** each element type repeats the same motion pattern;
  - **physical intuition:** motion is styled to the brand and feels natural, with friction and scale (paper-like vs grand parallax).

**(b) Steps, in order** (the workflow recap: R:4957-4983)
1. Understand the audience, platform and genre (R:4631-4691).
2. The UX designer maps the information flow first (R:4573-4589, R:4959-4965).
3. Define the core theme (R:4743-4747).
4. Write the style rules (R:4747-4765).
5. The UI designers build the visuals, keeping shape, color, layout and values consistent everywhere (R:4965-4975).
6. Motion graphics run alongside, to strengthen the message, guide players and give feedback (R:4975-4983).

**(c) References**
- Copy the work of artists you love to learn their techniques, then add your own twist (R:5007-5035).
- Recreate the HUDs and menus of your favorite games (R:5043-5050).
- Play games and look for the pain points (R:4993-5000).

**(d) Self-review**
- Not stated as a separate step. The rules above (meaning consistency, proximity, the five motion goals) work as the checklist.

**(e) Mistakes**
- Trying to polish a bad design until it works ("you can't polish a bad design", R:4867-4869).
- Treating UI as only the HUD (R:4693-4709).
- Ignoring the differences between platforms (R:4653-4665).

### 3.9 Game design (R:5104-5983)

**(a) Signs of great work**
- It has the four parts of a game: a goal, opposition, decisions, rules (R:5171-5193).
- It names a specific type of fun, not just "fun": fantasy, thrill, fellowship, mastery, exploration, creativity and so on (R:5213-5241).
- Mechanics alone set the tone. A cube that damages the area around it and then vanishes reads as a bomb, and a bigger area adds danger and power (R:5337-5363). Movement patterns imply a character: a jump suggests a frog; ninja, zombie, robot, snake and tornado patterns are shown (R:5365-5392).
- Mechanics and art imply the same theme (R:5393-5423).
- Every side can see its progress toward the goal; Overwatch's payload checkpoints tell both teams (R:5436-5484).
- There is a climactic arc: the boss "brings the heat" at low health, and the last kill feels like a hunt (R:5488-5522).
- Opposition causes the right kind of frustration, and the designer also supplies the tools to overcome it, working both for and against the player (R:5545-5567).
- It is fair: clear expectations and consistency, so players learn from failure. Do not blindside them (R:5630-5666).
- The luck/skill balance is a deliberate choice. Battle royales mix random starts with skill-based moment-to-moment play, so skilled players can come back and new players can still win (R:5669-5743).

**(b) Steps** (the order is inferred from the video plus its advice section)
1. Pick a specific target experience (R:5243-5257).
2. Share it with art and engineering, so everyone aims at the same target (R:5280-5308).
3. Design the mechanics (rules and interactions) and check the theme they imply (R:5323-5399).
4. Make the goals and progress readable (R:5436-5448).
5. Build climactic arcs (R:5488-5500).
6. Design the opposition and the tools to beat it (R:5559-5563).
7. Check fairness and consistency (R:5630-5650).
8. Choose the luck/skill mix (R:5669-5743).
9. Prototype in the simplest form (paper, cards) and play it with someone to see whether they enjoyed it (R:5767-5785).

**(c) References**
- Play games and make games (R:5755-5757).
- Ideas come from the whole team; almost every ability in one designer's champion kits started with someone else (R:5805-5817).

**(d) Self-review**
- Keep goals (the experience) apart from tactics (rules, choices) in every debate (R:5827-5855).
- Playtest with another person (R:5783-5785).

**(e) Mistakes**
- Using "fun" as the target (R:5213-5217).
- Different people building toward different types of fun (R:5255-5257).
- Adding unneeded story to a game whose core is not story (R:5259-5271).
- Treating art as downstream of design (R:5286-5296).
- Mechanics and art that do not match (R:5401-5423).
- Progress the player cannot see (R:5442-5448).
- Inconsistent, unpredictable obstacles (R:5644-5666).
- Believing the best designers simply have the best ideas (R:5787-5795).

---

## 4. Collaboration: what each craft needs, gives and must agree on

| From → To | What is exchanged | When | Why | Line |
| --- | --- | --- | --- | --- |
| Game design → Concept | Rules and mechanics (e.g. "pull enemies to you"), numbers such as HP, camera perspective; lore, setting and tone | Before drawing starts | These are the constraints that focus the work and stop endless spinning. The concept artist works out what a mechanic *looks like* | R:616-662 |
| Concept → whole team | A moodboard with pillars | Before drawing | Feedback without much work; a gut-check on direction | R:684-716 |
| Concept → team | A broad set of quick sketches, then narrower ones | Every iteration cycle | Big changes cost least at the sketch stage | R:812-858 |
| Team → Concept | Answers to one goal-specific question | Every cycle | Keeps feedback on track | R:860-874 |
| Concept → Character | The concept as the final target | When 3D work starts | The model must keep and strengthen its iconic qualities | R:1134-1144 |
| Character ↔ Concept | Agreement on which iconic traits survive simplification | While simplifying for the small on-screen size | Picking the wrong core elements loses the essence | R:1162-1176 |
| Character → Tech art (rigger) | The finished mesh, still in its creation pose | After modeling | Rigging gives it the ability to move | R:2381-2387 |
| Tech art → Animator | Skeleton, weights, intuitive controls, foot-plant and follow switches | Before animating | Raw bones are hard to animate | R:2413-2437 |
| Animator + Tech art → Character | Notes on design parts (collars, scarves, armor) that block motion | Late, once the character moves | So the animator can reach the expression the character needs | R:1540-1562 |
| Character → Animation (indirect) | Believable anatomy | While sculpting | Weak anatomy is hard to animate | R:1485-1489 |
| Any artist → Tech art | Tool requests, bug reports (animator), feature requests (modeler) | Any time; constant context switching | The tech artist re-asks the goal, because requests are often not well informed | R:2451-2497, R:2829-2847 |
| Tech art ↔ Engineer | What a shader must do to support the art | Shader development | The tech artist writes the shader, or specs it with the engineer | R:2705-2711 |
| Tech art → Artists | How to use the shader parameters | After the shader exists | Artists can then control the look | R:2713-2717 |
| Tech art → everyone | Pipeline channels, version-control tools, naming and folder rules, export/import automation | All the time | Many people hand files to each other; there is a risk of deleting or overwriting work and of not knowing who is editing what | R:2499-2641 |
| Concept → Environment | Theme and tone | First | Sets the look and feel | R:1753-1755 |
| Game design → Environment | A grey-block blockout: obstacles, player path, enemy sources | Before environment art | The art must carry both the concept vision and the designer's constraints | R:1757-1773 |
| Design + Concept → Environment | What to prioritize for the overall experience | At planning | There is far more to build than time allows | R:1731-1751 |
| Environment ↔ Concept | Paintovers and jamming on ideas | From rough-out through refinement | To push the design | R:1803-1813 |
| Playtests → Environment | Feedback | After refinement, before lighting and polish | Polish only what works | R:1777-1785 |
| Character → Environment | A character placed in the blockout for scale | Blockout | Otherwise scale errors (the twenty-foot desk) | R:2027-2035 |
| Character model → VFX | The model's color; the effect uses a color next to it on the color wheel (analogous) | Effect design | Players can tell who cast the spell | R:3772-3788 |
| VFX ↔ all other effects | Agreement on shape meanings and a color budget across the game | Effect design | Effects must contrast with each other; similar colors need shape differences | R:3640-3654, R:3700-3726, R:3762-3770 |
| Gameplay → Sound | Game states to cue (ability ready, damage taken, spotted) and events to hook sounds on (entering water, starting combat) | Design and implementation | Sound clarifies and reinforces what is happening | R:4067-4077, R:4329-4349 |
| Sound → Gameplay readability | A sound that warns of a coming state change (Ivern's shield creak before it breaks) | Ability design | Tension, anticipation, information | R:4378-4382 |
| Sound ↔ Environment | Reverb that shows the space | Mix | Expresses the environment the sound is in | R:4308-4326 |
| Sound ↔ UI | Some stealth games show sound attenuation in the UI | Design | Makes noise readable | R:4241-4243 |
| VFX ↔ Sound / Animation | Timing ideas shared: anticipation, then impact. An explosion's build-up is noted as "a good sound example"; a longer ADSR attack adds wind-up; animators telegraph attacks | Effect, sound and animation design | Picture, sound and motion should hit the same beat (*my link*; each craft states the idea separately) | R:3830-3834, R:3890-3910, R:4214-4218, R:2965-2971 |
| UX → UI | The mapped information flow | UX first | UI builds visuals on top of that flow | R:4573-4599 |
| UI ↔ Motion graphics | Motion that strengthens the message and gives feedback | All through UI visual design | The message must be *felt* as well as understood | R:4855-4861, R:4975-4983 |
| UI → whole game | The ecosystem rules: meaning of color, text and position; typography, iconography, shape language, animation | After the core theme, before the screens | Everything affects everything else | R:4713-4777 |
| Design ↔ Art ↔ Engineering | One target experience | Before work, and kept all the way through | Aim in the same direction and set each other up for "easy wins" | R:5280-5308 |
| Design ↔ Art | Mechanics imply a theme and the art must match, both ways | Design | Mismatches feel unnatural. Original Shen: designers built a tank, artists drew a stealth assassin | R:5393-5423 |
| Everyone → Game design | Ability ideas | Ongoing | The designer curates them into one cohesive kit | R:5805-5825 |
| Animator ↔ Animator | Acting out together and giving each other notes | Preparation | Riot's animators brainstorm as a group | R:3058-3072 |
| Gameplay conditions → Animation | Speed, distance, aim input, climbing state, used to drive blends | Animation-system build | The state machine reacts to game conditions | R:3275-3301 |
| Feedback giver → any artist | A suggested fix | Any review | Find the problem behind the fix (see section 5) | R:2175-2201 |

---

## 5. Review and approval

**What the transcript says**
- **Concept: frequent, structured team feedback.**
  - Moodboard review comes first (R:696-700).
  - Show early and often, with no grand reveals (R:878-884).
  - Each cycle closes doors and expands what the team liked (R:846-856).
  - Ask goal-tied questions, not "do you like it?" (R:864-874).
  - Expect changes; they are normal (R:802-810).
  - Not everyone will like every idea, and that is acceptable (R:1036-1038).
  - Present with conviction (R:888-892).
- **Character: self-review in the game, continuously.** The proxy is checked as early as possible, then adjusted from how it looks in the game (R:1189-1199). Late reviews by animation and tech art can send the model back (R:1540-1562).
- **Environment: playtest-driven.** Playtest "a lot" and gather feedback during refinement. Lighting and polish come only after the level is playtested and working (R:1777-1785).
- **How to take feedback** (environment advice, R:2167-2201):
  - Ask what problem the reviewer is trying to solve.
  - Fix that problem in your own way.
  - Example: the note was "delete the trees". The real problem was that the forest was busy and noisy, so the artist cleaned up the textures and the composition instead.
  - Their words: understand "the problem, and not the solution they're giving you" (R:2199-2201).
- **Tech art: the same pattern for tool requests.** Ask "What are you trying to do?" before building (R:2457-2471).
- **Animation: peer notes and many tries.**
  - Animators give each other notes while brainstorming (R:3068-3072).
  - Compare the new version with the old one side by side (R:3229-3231).
  - Expect 3-5 tries at the same animation (R:3334-3336).
  - Be ready to throw out your own ideas for better ones, from others or from yourself (R:3316-3332).
- **Sound: review is hard to put into words.** Give the reviewer and the designer shared terms (frequency, ADSR, attenuation, EQ, reverb) (R:4107-4129).
- **Game design: debate the goal or the tactic, never mix them.** Before arguing, agree whether you are talking about what the player should feel and do, or how to achieve it (R:5847-5855). The test is to play it with someone and see whether they liked it (R:5783-5785).
- **Iteration counts given:** animation 3-5 tries (R:3334-3336). One environment artist says more than 80% of what they make is "garbage" no one else sees (R:2269-2273). Concept: as many Closing-Doors cycles as needed (R:846-856). No other numbers are given.

**What the transcript does NOT say**
- It never names a sign-off role (art director, lead, producer), a gate, or who has the final say. "The team" is the only reviewer named in concept art (R:804-806, R:846-852).
- Every agent mapping of approval authority therefore comes from our own rules, not from this source.

---

## 6. Order of work across crafts

1. **Target experience first.** A specific type of fun, shared by design, art and engineering (R:5243-5308). The series jokes that the game-design video should have come first (R:5136-5144).
2. **Concept goes first among the art crafts.** It shapes what the game will be and how it will look (R:570-576). It goes first because big changes cost least as quick drawings (R:812-816). Inside concept: constraints, research and moodboard, ideation, narrowing (R:920-936).
3. **Environment track** (R:1753-1785):
   1. concept sets theme and tone;
   2. designers build the grey blockout;
   3. environment roughs out art;
   4. models, textures and color are refined;
   5. playtests run;
   6. lighting, post-processing and polish come **last**.
4. **Character track:**
   1. concept;
   2. proxy, then an in-game silhouette check;
   3. high-poly, low-poly, UVs, bake, textures or shaders (R:1134-1460);
   4. rig: bones, weights, controls (R:2381-2437);
   5. animation (R:2896 ff.).
   Motion problems can send the model back upstream (R:1540-1562).
5. **Animation inside its own track:** reference and acting first (R:3012-3046), key poses on the timeline (R:3354-3362), pose quality (R:3085-3181), motion (R:3193-3227), the state machine for in-game behavior (R:3237-3301).
6. **VFX build order:** primary read, then secondary, then tertiary (R:3552-3618), then timing (R:3790-3832).
7. **UI track:**
   1. audience and platform;
   2. the UX flow first (R:4573-4575);
   3. the core theme;
   4. the style rules (R:4743-4765);
   5. the visual build.
   Motion graphics run **in parallel** "throughout" (R:4975-4983). Function always comes before art (R:4873-4885).
8. **Sound:** parts come from libraries (or foley), are shaped (ADSR, attenuation, EQ, reverb), then attached to game events (R:4351-4364, R:4167-4349). The order is inferred.

**What runs in parallel:**
- Art, design and engineering push at the same target together (R:5302-5308).
- Environment and concept trade paintovers back and forth (R:1809-1813).
- UI and motion graphics run together (R:4975-4983).

**What gets locked, and when:**
- Closed concept doors stay closed (R:858).
- The concept becomes the character's final target (R:1138).
- Lighting and polish are applied only after the level plays well (R:1781-1785).
- The UI core theme and style rules are fixed before the screens, and every later decision answers to them (R:4743-4777).
- Shape language for effects is fixed game-wide (R:3692-3696).

---

## 7. Lessons for our AI agents

Strength: **stated** = a principle the video states; **example** = shown through a case; **passing** = an aside or a single piece of career advice.

| # | Lesson | Our roles | Line | Strength |
| --- | --- | --- | --- | --- |
| L1 | Every brief names the problem and its constraints before anyone makes anything. A "cool" result that does not serve the goal fails. | orchestrator, game-designer, art-director, all crafts | R:584-608 | stated |
| L2 | Constraint checklist for any visual brief: theme (lore, setting, tone), camera perspective, mechanics, gameplay numbers (HP etc.). | game-designer, art-director, modeler, vfx-designer, ui-ux-designer, environment-designer | R:616-662 | stated |
| L3 | A narrow moodboard with short pillars comes before any final image. It is a cheap direction check. A scattered board causes pivots later. Maps to our reference-images step. | art-director, environment-designer, marketing, ui-ux-designer, film-director | R:684-716 | stated |
| L4 | Make many fast, low-fidelity variants before polishing anything. Two-tone sketches keep attention on big shapes. Practice sheets of 50-100 designs under one constraint. | art-director, marketing (icons, thumbnails), ui-ux-designer, vfx-designer, modeler | R:740-760, R:822-834, R:980-985 | stated |
| L5 | "Closing Doors": go broad to narrow over iterations and never reopen a closed door. Our decision ledger is the record of closed doors. | orchestrator, game-designer, art-director | R:840-858 | stated |
| L6 | Ask the owner a specific question tied to the goal ("which feels scariest?"), never "do you like it?". | orchestrator, every role that reports to the owner | R:860-874 | stated |
| L7 | No grand reveals. Show early and often, because change costs less early. | all roles; orchestrator sets the cadence | R:812-816, R:878-884 | stated |
| L8 | Present work with the reasons that drove it, connecting each choice to the idea. The presenter is the team's inspiration. | art-director, game-designer, marketing, film-director | R:888-892, R:1014-1028 | stated / example |
| L9 | Design for a specific target audience. Wild excitement from that audience beats mild approval from everyone. | game-designer, marketing, art-director, trend-scout | R:1040-1056 | stated |
| L10 | Before evolving an archetype or genre trope, learn its history and what it means. | game-designer, art-director, modeler, trend-scout | R:986-1000 | passing |
| L11 | Check readability at the real on-screen size. Cut down to the iconic elements, and make sure they are the *right* ones. This applies directly to small Roblox characters, phone screens and thumbnails. | modeler, art-director, marketing, ui-ux-designer | R:1115-1170 | stated / example |
| L12 | Blockout or proxy first. Check silhouette and proportion *in the game* as early as possible, then add detail at the focal points. | modeler, environment-designer, character-rigger, art-director | R:1183-1199 | stated |
| L13 | Detail is a budget for hierarchy. Alternate areas of rest with areas of detail; do not fill everything. | modeler, environment-designer, vfx-designer, ui-ux-designer, marketing | R:346-362, R:1931-1939 | stated |
| L14 | Test designs *in motion*. Collars, scarves and armor that block arm movement go back to the modeler, through the rigger and animator. | modeler, character-rigger, animator (planned) | R:1540-1562 | stated |
| L15 | Base creatures on real anatomy (combining several animals) so they feel alive and animate well. | modeler, character-rigger, art-director | R:1478-1523 | stated / example |
| L16 | Keep polygon budgets low and bake detail into textures. | modeler, environment-designer, performance-engineer | R:1260-1327 | stated |
| L17 | The game designer's grey blockout (obstacles, path, enemy sources) comes before environment art. Environment art must keep both the concept vision and the designer's constraints. | game-designer, environment-designer | R:1757-1773 | stated |
| L18 | Solve a gameplay constraint with the most believable in-world form: a boundary becomes a cliff, a wall or a building. | environment-designer, game-designer | R:1815-1829 | stated / example |
| L19 | Open each level with an establishing composition that shows where the player is and what comes next. | environment-designer, film-director, game-designer | R:1887-1899 | example |
| L20 | Use light as a focal point to guide the player, and also as a decoy before a surprise. | environment-designer, film-director, vfx-designer | R:1901-1927 | stated |
| L21 | Scale check: put a character in every blockout. Scale cues are things the player touches (doors, rails, stairs, chairs). | environment-designer, modeler, studio-operator (review captures) | R:2017-2035 | stated / example |
| L22 | Tell the story through climate, age and culture, with wear where hands go and signs that someone lives there. Build the whole bar, not one hero bottle. | environment-designer, modeler | R:1951-1987, R:2229-2245 | stated |
| L23 | Modular kits: pieces vary enough to build different looks, but never read as copies. Rotate and reshape them. | environment-designer, modeler, performance-engineer | R:2069-2097 | stated |
| L24 | Lighting, post-processing and polish come only after the space plays well in playtests. | environment-designer, orchestrator, qa-lead | R:1781-1785 | stated |
| L25 | When feedback arrives as a solution, ask what problem it solves, and fix the problem. This applies to owner notes, review findings and peer notes alike. | all roles; especially orchestrator, art-director, reviewer | R:2175-2201 | stated / example |
| L26 | "What are you trying to do?" Rebuild every tool or feature request around its goal (the fish counter instead of hiding all the water). This matches our rule that briefs say what and why. | architect, feature-builder, quick-builder, orchestrator | R:2457-2497 | stated / example |
| L27 | Automate repeated implementation steps: naming, settings, splitting files, links between files. | architect, studio-operator, modeler (export/import), environment-designer | R:2499-2541 | stated |
| L28 | The pipeline needs clear hand-off channels, version history, a way to see who is editing a file, and kept-up naming and folder rules. | orchestrator, architect, all roles | R:2543-2641 | stated |
| L29 | Rigs: bends with no odd results, intuitive controls for the animator, planted feet and follow-the-body switches. | character-rigger | R:2399-2437 | stated |
| L30 | Shader or material choices are agreed between the engineer and the art side, and the result is taught to the people who use the parameters. | environment-designer, modeler, architect | R:2705-2717 | passing |
| L31 | Three goals for animation: actions read clearly, physics is believable and consistent, personality shows. | animator (planned), vfx-designer, film-director | R:2941-2999 | stated |
| L32 | The wind-up is critical information. Show it in animation, sound (a longer attack) and VFX build-up, and agree the timing across the three crafts. | animator, vfx-designer, sound-designer, game-designer | R:2965-2971, R:3830-3832, R:4214-4218 | stated (each part); the link across crafts is mine |
| L33 | Consistent physics lets players predict results. Do not break it per effect or per clip. | animator, vfx-designer, feature-builder, game-designer | R:2977-2983 | stated |
| L34 | Ask "how does *this* character do it?" (run, cast, sound), not "how does anyone do it?". | animator, sound-designer, vfx-designer | R:2993-3009, R:4372-4374 | stated |
| L35 | Get real motion reference before animating: act it out or film it. For an AI agent, this means video or motion reference, not guessing. | animator, film-director | R:3012-3046, R:3338-3352 | stated |
| L36 | Pose checks: a clear line of action, the center of gravity over the feet, prop weight shown by how far the prop is from the body. These also apply to key-art poses. | animator, character-rigger, marketing, art-director | R:3085-3133 | stated |
| L37 | Turn personality into 2-4 character adjectives (heavy, defiant, noble), map each to a visible change, and pull back on overshoot. This works as a brief format for any craft. | animator, art-director, marketing, ui-ux-designer, sound-designer | R:3147-3181 | example |
| L38 | Spacing and eases, squash and stretch. Never use even spacing for natural motion. This applies to UI tweens as well. | animator, ui-ux-designer, vfx-designer | R:3197-3227 | stated |
| L39 | A game character is a system of interrupting, blending clips driven by game conditions. Plan the state machine with the builders. | animator, feature-builder, architect | R:3237-3301 | stated |
| L40 | Plot the key storytelling poses before the in-betweens (pose-to-pose). Storyboards and animatics use the same idea. | animator, film-director | R:3354-3362 | passing |
| L41 | Expect 3-5 tries at one piece. Be ready to drop your own idea for a better one. | all craft roles | R:3316-3336 | passing |
| L42 | Primary, secondary and tertiary reads: one element wins the eye first, and supporting layers never steal focus. This works for effects, screens, thumbnails and key art. | vfx-designer, ui-ux-designer, marketing, art-director | R:3552-3618 | stated |
| L43 | Restraint and contrast between features: if every effect, sound or screen is loud, none is. Set a loudness budget across the whole game. | vfx-designer, sound-designer, ui-ux-designer, art-director | R:3626-3654 | stated |
| L44 | A game-wide shape language with fixed meanings (plus for heal, circle for shield, spikes for damage). It matters most when colors collide. | vfx-designer, ui-ux-designer, art-director | R:3692-3726 | stated |
| L45 | Choose effect colors for what they must say (team, damage type, tone), keep the color budget small, and use a color next to the caster's own on the color wheel. | vfx-designer, art-director | R:3736-3788 | stated / example |
| L46 | Impact timing: a fast start, an ease into full size, a timed build-up (the rock-in-the-lake beat). Never linear. | vfx-designer, sound-designer, ui-ux-designer (motion), animator | R:3790-3832, R:3890-3910 | stated |
| L47 | Every sound has one of three jobs: gameplay cue, feedback, or emotion. Name the job on each cue card. | sound-designer, game-designer, ui-ux-designer | R:4059-4105 | stated |
| L48 | Give sound reviews shared terms (frequency, ADSR, attenuation, EQ, reverb), because people struggle to describe sound in words. | sound-designer, reviewer, orchestrator (owner digests) | R:4107-4129 | stated |
| L49 | Small changes to dynamics change the emotion: a longer attack adds wind-up, a longer release adds weight. | sound-designer | R:4204-4222 | stated |
| L50 | Set attenuation per sound type and per frequency band. Far sounds keep their lows and lose their highs. | sound-designer, environment-designer (ambience map) | R:4245-4275 | stated |
| L51 | Reverb shows the space. The environment's materials and size should drive it. | sound-designer, environment-designer | R:4298-4326 | stated |
| L52 | Sounds hang on named game events (entering water, starting combat), so builders must provide those event hooks. | sound-designer, feature-builder, architect | R:4329-4349 | stated |
| L53 | Use sound to signal a coming state change and to set similar characters apart (Ivern's creaking shield). | sound-designer, game-designer | R:4366-4382 | example |
| L54 | Calibrate "good" against top-tier reference before judging your own output. | sound-designer, all craft roles | R:4431-4447 | passing |
| L55 | UX before UI: map the information architecture and the fewest-action path first, then style it. | ui-ux-designer, game-designer | R:4559-4599 | stated |
| L56 | Audience, platform and genre set the UI's density and layout; PC differs from mobile. Roblox is phone-first. | ui-ux-designer, marketing | R:4631-4691 | stated |
| L57 | Set the core theme first, then strict rules (type, icons, color, shape, animation), then build screens. Every decision answers to the theme. | ui-ux-designer, art-director | R:4741-4777 | stated / example |
| L58 | Layout carries meaning by proximity. A bar sits next to the thing it measures. | ui-ux-designer, marketing | R:4793-4821 | stated |
| L59 | Function first. Polish cannot rescue a bad design, so do not send a broken flow to the style stage. | ui-ux-designer, all crafts, reviewer | R:4867-4885 | stated |
| L60 | Five motion goals work as a UI motion checklist: responsiveness, intention, awareness, consistency, physical intuition. | ui-ux-designer, vfx-designer | R:4893-4949 | stated |
| L61 | "Fun" is not a target. Name the type of fun (fantasy, thrill, fellowship, mastery, exploration, expression). | game-designer, orchestrator, progression-designer, live-ops-designer | R:5213-5271 | stated |
| L62 | One target experience aligns art, design and engineering. Art is not downstream of design. | orchestrator, game-designer, art-director, architect | R:5280-5308 | stated |
| L63 | Mechanics carry theme. Check for mismatches between art and mechanics (bushes that stop bullets, the tank drawn as an assassin) in both design review and QA. | game-designer, art-director, reviewer, qa-lead | R:5323-5423 | stated / example |
| L64 | Progress toward the goal is visible to every side, the opposing team included. | game-designer, progression-designer, ui-ux-designer | R:5436-5484 | stated |
| L65 | Build climactic arcs toward the end of a goal (the boss heats up at low health, the last-kill hunt). | game-designer, progression-designer, film-director, sound-designer | R:5488-5522 | stated |
| L66 | The right frustration: supply both the opposition and the tools to beat it. | game-designer, progression-designer | R:5545-5567 | stated |
| L67 | Fairness: clear expectations and consistency make failure learnable. Never blindside the player. | game-designer, qa-lead, environment-designer (level layout) | R:5630-5666 | stated |
| L68 | Choose the luck/skill mix on purpose. A random start plus skill-based play allows comebacks and lets newcomers win. Read this next to our paid-random rules. | game-designer, progression-designer, live-ops-designer | R:5669-5743 | stated |
| L69 | Prototype the simplest version and play it with a real person before building it up. | game-designer, quick-builder, qa-lead | R:5767-5785 | passing |
| L70 | The designer's job is curation: gather the available information and ideas, and pick the most cohesive solution, not the designer's own idea. | game-designer, orchestrator | R:5787-5825 | passing |
| L71 | In every debate, say whether you mean the goal (what the player feels and does) or the tactic (how). This matches our "what and why, never how" brief rule. | orchestrator, game-designer, all roles | R:5827-5855 | passing (strong fit) |
| L72 | Learn by recreating admired work (HUDs, menus, mograph), then add your own twist. For us this is internal study only; shipping work must respect copyright and IP rules. | ui-ux-designer, marketing, all craft roles | R:5007-5050 | passing |
| L73 | Every action gives immediate visible and audible feedback. | ui-ux-designer, vfx-designer, sound-designer, animator, feature-builder | R:136-146, R:4897-4901 | stated |
| L74 | Atmospheric perspective: cut detail and contrast with distance to make depth and lead the eye. | environment-designer, art-director | R:368-378 | stated |
| L75 | Set environment priorities by their value to the experience, agreed with design and concept, not one rock at a time. | environment-designer, orchestrator, game-designer | R:1731-1751 | stated |
| L76 | Volume beats perfectionism when learning a skill (drawing many hands over one perfect hand). This suits agent self-practice and eval sets. | art-director, modeler, all crafts | R:438-464 | passing |
| L77 | Sound is part of the art style ("everything you can see and hear"). The art bible should hold sound meanings too. | art-director, sound-designer | R:72-78 | stated |

---

## 8. What contradicts or complicates a simple pipeline

1. **Upstream work is never truly final.** Concept work may change completely at any moment, so work as if it will (R:818-820). Big changes are only *cheaper* early, not forbidden later (R:812-816).
2. **Late loops go back up the pipeline.** A finished character model can return from rigging and animation when its design blocks motion (R:1540-1562). Weak anatomy shows up as an animation problem (R:1485-1489).
3. **Two-way traffic, not hand-offs.** Environment and concept trade constant paintovers (R:1809-1813). Art and mechanics must imply each other's theme "and vice versa" (R:5393-5399). The series rejects the "art is downstream of design" model outright (R:5286-5300).
4. **Parallel work without a shared target diverges.** Original Shen was a tank to the designers and a stealth assassin to the artists (R:5417-5423). Two crafts working in parallel need one written target experience (R:5280-5308).
5. **Playtesting decides when polish starts.** Environment polish waits for "playtested and working" (R:1781-1785). That is a loop, not a fixed step.
6. **Reviewers' fixes are often wrong even when their problem is right** (the trees anecdote, R:2175-2201). Tool requesters are often not well informed (R:2473-2479). A pipeline that executes notes literally will build the wrong thing.
7. **Iteration is expected.**
   - Animation takes 3-5 tries at the same piece (R:3334-3336).
   - 80% of one artist's output is discarded (R:2269-2273).
   - Concept work moves through repeated broad-to-narrow cycles (R:846-856).
   - A team may replace your own ideas with better ones (R:3324-3332).
8. **A tension in "show early".** Concept says show everything early and often (R:878-884). The environment artist says most of their output is "not necessarily for anyone else to see" (R:2269-2273). My reading: show early *candidates*, not every failed experiment. That matches self-review before owner gates.
9. **No fixed recipe in some crafts.** VFX has "no standard approach", and every effect is a new problem (R:3478-3502). The fireball recipe is "just one way" (R:3620). UI layout has "no single right answer" (R:4832-4839). Sound designers are told rules can be broken (R:4483-4489). Craft books should give principles and checks, not one mandatory recipe.
10. **Animation is a system, not a list of clips.** You cannot predict which animation will play. Characters are thousands of interrupting, blending clips driven by a state machine (R:3237-3301). That needs the builders involved from the start, not at the end.
11. **Support roles are interrupt-driven.** Tech art switches context constantly between animator bugs, modeler features and engineer talks (R:2823-2847). That role serves every track at once and does not sit at one stage.
12. **Consensus is not the goal.** Work aimed at a specific audience may draw "pitchforks" from others (R:1048-1056). Not everyone has to like every idea (R:1036-1038). Review loops should judge against the target, not against majority taste.
13. **Ideas come from everyone.** The designer curates rather than authors (R:5805-5825). Ideas flow in from all roles, not only down from design.
14. **"Fun" cannot be the brief** (R:5213-5217). Without a named type of fun, crafts build toward conflicting targets (R:5255-5257).
15. **Mistakes have value too.** "Real art is knowing which mistakes to keep" (R:5103). Rejecting every deviation in review may cut good accidents.
16. **What the source does not say:** who approves, how many review rounds there are, budgets, or schedules (section 5). Any gate structure we build is our own design, not Riot's practice as shown here.
