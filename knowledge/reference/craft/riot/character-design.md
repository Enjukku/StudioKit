---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, modeler, reference-images, animator, character-rigger, sound-designer, vfx-designer, game-designer, marketing, film-director, live-ops-designer, environment-designer, level-design, orchestrator, reviewer, qa-lead, ui-ux-designer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Character design

Designing characters (and props or places treated as characters) so players know who they are at a glance, believe them, and still recognise them in every variant.
CD-01 to CD-03 start from the character (card, sell list, archetype). CD-04 to CD-08 keep identity across variants, products, views and the concept-to-3D step. CD-09 to CD-12 are personality in motion and believable bodies that move. CD-13 to CD-21 shape variants, props and personality accents. CD-22 to CD-24 are faces. CD-25 to CD-29 are promo poses, props as characters, hard cases and sensitive content.
Related: silhouette rules in `shape-silhouette.md`, identity at style level in `style-identity.md`, rig-ready building in `pipeline-production.md`.

### CD-01 Know the character, then decide on their behalf
- principle: Know the character holistically before designing: core traits, history, how they react, who they might want to be next, and the tension in their personality (for example "elegant + deadly"). Every design choice (proportions, face, costume, pose, sound, idle) must express that core; anything that does not is cut.
- why: Players are invested in the character and read personality from proportions and features before any dialogue. Choices become consistent when they follow one personality; out-of-character choices break the investment.
- apply: Before images, write a short character card: temperament, history, the two-word tension, how they move, what they would never wear. Attach it to every reference-images prompt and to the modeler's, animator's and sound designer's briefs. Justify each added element against it ("how would she dress if she took this job?"). Avoid tropey or sexualised choices.
- check: Each design choice in the hand-back traces to a line of the card; a reviewer asks of each element "which trait does it express?" and cuts those with no answer. Show the game-size render to a fresh agent with no context: the two tension words come back.
- mistake: "Design choices that feel sort of out of place" (R01); a generic or cute face on a serious character (R03:974-976).
- examples:
  - R01: imagining how Caitlyn would style herself if she took a ringmaster job; keep the "kernel" players love (R01:178-184, 216-224).
  - R11: a darker Katarina as a meticulous, obsessive assassin who lost her sense of self; details that "help me understand who they are" (R11:77-86, 247-252).
  - R03: Caitlyn is elegant and deadly, so her features are striking and sharp, not cute (R03:188-196, 974-976).
- roblox_fit: Young audience: keep designs non-sexualised (load `platform-policy`) [inference]. On a phone, proportions carry more than face detail [inference].
- roles: art-director, reference-images, modeler, animator, sound-designer, film-director, game-designer, marketing
- also: style-identity, references-ideation
- sources: R01-F10 (R01:178-184, 216-224); R11-F04 (R11:77-86, 247-252); R03-F07 (R03:188-196, 974-976)

### CD-02 Write the sell list before drawing
- principle: Before any image, answer: what am I selling, what excites players, what does it say about the character, is it recognisable. Turn it into a short numbered list and solve the thumbnail and silhouette for that list.
- why: A stated fantasy keeps every choice serving it; players should project themselves into a story slightly beyond reality.
- apply: Every visual brief has a "sells" list of 2-4 items (for example 1 faction, 2 role, 3 personality); each candidate image is scored against it. For Roblox the same list drives the icon and thumbnail promise [inference].
- check: A reviewer reads each item and points to where the image shows it; a missing item fails the candidate.
- mistake: Starting without knowing the goal (R08:576-579).
- examples:
  - R08: Alune sells (1) Anima Squad, (2) caster, (3) an elegant, queenly figure (R08:269-292, 318-324).
- roblox_fit: Same.
- roles: art-director, game-designer, marketing, reference-images, film-director, orchestrator, reviewer
- also: references-ideation, game-design-fun
- sources: R08-F11 (R08:269-292, 318-324)

### CD-03 Understand the archetype before evolving it
- principle: Evolving a design starts with its history: what the archetype means and which traits make it work (knight, ninja, blade dancer). Keep those traits; change the rest.
- why: An evolution that drops the archetype's core loses recognition.
- apply: For a known archetype, list its defining traits from references before generating variants and keep them in every option.
- check: A viewer (or fresh agent) names the archetype from the black-fill silhouette of each option.
- mistake: Changing an archetype without knowing what made it work [inference].
- examples:
  - R00a: redesigning Irelia required understanding the blade-dancer archetype first (R00a:986-1000).
- roblox_fit: Roblox players read genre archetypes fast from thumbnails; keep them [inference].
- roles: art-director, modeler, game-designer, reference-images, marketing
- also: references-ideation
- sources: R00a-F27 (R00a:986-1000)

### CD-04 Variants hold the identity anchors and change the rest
- principle: Every character and item has 2-5 identity anchors that players know it by: silhouette features, signature proportions, primary reads, signature colours (red hair, scar, face paint, collar, giant weapon; for items, ranked recognition features). A variant, skin or upgrade keeps all anchors and the base proportions; theme, material, colour and costume change. Costume is an accessory; people are recognised by face and mannerisms.
- why: Recognition survives large changes when the anchors stay; players buy the variant because they love the original, and lose it if they think it is someone else.
- apply: The art bible holds an anchor list per character and a ranked recognition-feature list per item family (for example Vandal: banana magazine, gas tube, rear sight). Every variant brief and image prompt repeats the list and references the base model or images directly. Modelers keep the anchors as big forms (not texture detail) and keep base proportions and height; riggers and animators keep them unhidden in idle and key poses. If a pose hides one anchor, accept it only when all others are visible.
- check: Side-by-side base and variant at the game camera and in black-fill (`look_check.py silhouette --compare`): list the anchors visible in each; all present (at most one hidden by pose); height ratio equal to the base; a reviewer names the character or item type from the variant's silhouette instantly, and the new theme is obvious.
- mistake: A skin so different the character is lost; reskins that change an item's identifying parts; changing everything at once.
- examples:
  - R08: Battle Butterfly Alune keeps face paint, collar, giant weapon and elegance (R08:113-122, 724-729).
  - R10: Yasuo keeps the bushy ponytail, sword and wide pants; the pauldron hidden by the fishing pose is accepted because the rest hits (R10:117-130).
  - R11: red hair stays red, the scar stays, the costume is open (R11:212-233).
  - R03: "What makes them Garen?"; reference the current in-game version for likeness (R03:372-386, 980-984).
  - R01: Caitlyn stays tall and willowy, canon six feet, in every skin (R01:466-470).
  - R12: Vandal and Phantom keep their 2-3 recognition features and base proportions; free areas take the theme (R12:70-81).
- roblox_fit: Applies to skins, pets, tower tiers, building upgrades and limited cosmetics. Tool inventory icons (TextureId: knowledge/external/roblox-creator-docs/players/tools.md:23) must keep the same features. Phones keep only the biggest anchors, so prefer fewer, larger ones [inference].
- roles: art-director, modeler, character-rigger, animator, marketing, reference-images, live-ops-designer, game-designer, ui-ux-designer, vfx-designer, reviewer
- also: shape-silhouette, style-identity
- sources: R08-F03 (R08:113-122, 724-729); R10-F04 (R10:117-130); R11-F19 (R11:212-233); R03-F16 (R03:372-386, 980-984); R01-F31 (R01:466-470); R12-F07 (R12:70-81)

### CD-05 If a variant drops a silhouette landmark, fill its slot
- principle: A signature element (a top hat) is part of the silhouette. A variant may remove or replace it, but must fill that silhouette area with something of similar mass (headgear height, hairstyle), and must not bring it back in a silly, oversized form on a serious character.
- why: Players recognise the character by the outline; an empty slot makes the variant feel like someone else.
- apply: List the base silhouette landmarks in the concept prompt and the model check; for each, the variant states "kept" or "replaced by X".
- check: Black-fill of base and variant side by side at the game camera: every landmark area is occupied in both.
- mistake: Removing the hat without giving the head height elsewhere; "mad hattery" proportions.
- examples:
  - R01: Lunar Wraith Caitlyn has no hat, but vertical headgear and hairstyle "fill that element of her silhouette up"; the ringmaster gets a smaller fascinator hat (R01:118-135, 574-584).
- roblox_fit: At phone size the head silhouette is one of few readable landmarks [inference].
- roles: art-director, modeler, reference-images, marketing
- also: shape-silhouette
- sources: R01-F05 (R01:118-135, 574-584)

### CD-06 Keep the likeness the same in every product
- principle: Face, posture and how the character presents itself stay consistent in every product and version (model, splash, icon, UI portrait, cutscene). Check with the character's owner during the work and do a final "same person" check.
- why: Players love specific characters; drift makes them read as another character and breaks trust.
- apply: Each character has approved anchor images (front face, posture) in the art bible; every new image, model or icon is compared with them; the art director (as the character's owner) signs off.
- check: Side-by-side with the anchor images at the same size; final "same person" question before hand-back; fail on faces that drift toward another character.
- mistake: Faces drifting so the character looks like "Irelia ... Lux ... Ashe" (R08:738-764).
- examples:
  - R08: weekly check-ins with Alune's original concept artist; final "make sure they look like the same person" (R08:738-764, 891-894).
- roblox_fit: Applies to the model, icon, thumbnail and UI portrait of the same character [inference]; ChatGPT images drift between generations, so always attach the anchor images to the prompt [inference].
- roles: art-director, modeler, reference-images, marketing, animator, reviewer, qa-lead
- also: style-identity, critique-feedback
- sources: R08-F29 (R08:738-764, 891-894)

### CD-07 The fantasy must survive every real view
- principle: Capture the character's fantasy for the views players really get: tiny on screen, seen from above or behind, blurred in fast motion, or only arms visible.
- why: Players meet characters in game views, not in turnarounds.
- apply: Character briefs list the real viewing conditions (size in pixels on a phone, camera angle, speed, first-person arms if any); the model is designed and judged for them.
- check: Captures at each listed condition (thumbnail size, top or back view, a fast-motion frame): the character is still recognisable to a fresh agent.
- mistake: Judging the character only in a close front render [inference].
- examples:
  - R00a: tiny, top-down, blurred and arms-only views are the hard cases (R00a:1115-1129).
- roblox_fit: Phone screens and third-person or top-down cameras make "tiny, from behind or above" the common case.
- roles: modeler, art-director, animator, vfx-designer, character-rigger, reference-images
- also: shape-silhouette, world-level-readability
- sources: R00a-F30 (R00a:1115-1129)

### CD-08 The concept is a blueprint: keep its iconic qualities, decide its gaps, exceed it in 3D
- principle: The approved concept is the target for appeal and iconic qualities, not a finished spec. Stop polishing it once shapes, values, colours and focal point are settled; in 3D keep and strengthen its iconic qualities, decide its ambiguous parts as a designer, and push the final asset beyond the concept's finish.
- why: 3D translation tends to soften what made a concept appealing; polishing 2D wastes time because everything is rebuilt; concepts leave many smaller parts ambiguous.
- apply: Reference-images stops when shapes, values, colours and focal point are settled. Modelers list the concept's iconic qualities and its ambiguous parts before modelling; decide each ambiguity inside the art bible (or request a targeted paint-over) and note the decision. Tripo outputs often soften iconic shapes; Blender clean-up restores them [inference].
- check: Side-by-side of the approved reference and the game-camera render: each listed iconic quality is present and at least as strong; the hand-back lists ambiguous areas with the choice made; the final finish equals or exceeds the reference.
- mistake: Losing the concept's appeal in translation; copying ambiguity literally or stalling on it; spending too long in 2D.
- examples:
  - R00a: "I see the concept as the final target I'm aiming for" (R00a:1134-1144).
  - R13: the concept is "nothing but a blueprint", close enough after the grayscale check, then the 3D texture is pushed further (R13:440-443, 468-475).
  - R13: texture painting as "creating a concept using a 3D canvas" (R13:565-595).
- roblox_fit: No change.
- roles: modeler, art-director, environment-designer, character-rigger, reference-images, orchestrator, reviewer
- also: references-ideation, pipeline-production, process-iteration
- sources: R00a-F31 (R00a:1134-1144); R13-F20 (R13:440-443, 468-475); R13-F25 (R13:565-595)

### CD-09 Every action shows who this character is
- principle: Ask not how to make a character run, but how this character runs. Every common action (run, idle, attack, emote) shows personality and the brand's tone; in a stylish context flair beats practicality.
- why: Gameplay has little story time, so personality in common actions builds identity; a generic move wastes it.
- apply: Each character brief lists 2-3 personality adjectives and any attitude shift; the animator designs locomotion, idle and key actions to show them; sound and VFX follow the same adjectives. Reference images for key poses include the attitude.
- check: Play two characters' run or idle clips side by side in black-fill: a reviewer tells them apart and names each one's adjectives without being told.
- mistake: Generic shared runs; the plain lean that works but is not "cooler" (R04:102-104).
- examples:
  - R00b: League run animations; the animator is like an actor (R00b:2993-3009).
  - R04: Akali kneeling into a finger heart shows "two sides of her character"; "It's not about practicality. It's about being a badass" (R04:40-54, 102-104, 322-326, 526-540).
- roblox_fit: Default avatars share animations; custom characters, NPCs and pets need their own locomotion to show personality.
- roles: animator, character-rigger, sound-designer, vfx-designer, art-director, modeler, film-director, marketing
- also: weight-timing, style-identity
- sources: R00b-F31 (R00b:2993-3009); R04-F23 (R04:40-54, 102-104, 322-326, 526-540)

### CD-10 Believable anatomy and plausible construction
- principle: Anatomy, not the tool, is the main obstacle: joints and masses must follow bones and muscles to look alive and animate well. Make costume parts feel functional and buildable (every piece has a visible attachment).
- why: Believable joints and masses deform well; plausibility sells the fantasy.
- apply: Place joints and masses on anatomical logic; modeler and rigger agree joint positions before building. Every prop and costume piece has a visible means of attachment (strap, clip, buckle).
- check: Test poses in Blender (arm raise, bend, crouch): no weird deformation; proportions match references; every attached piece shows how it is held on.
- mistake: A weird sculpt that is hard to animate; floating parts with no attachment.
- examples:
  - R00a: "The most important thing is to learn anatomy" (R00a:1466-1489).
  - R01: a clip covers the whole thing so the costume could be built (R01:632-642).
- roblox_fit: Rigid R15 parts hide some anatomy problems, but joint placement still matters [inference].
- roles: modeler, character-rigger, animator, art-director, reference-images
- also: pipeline-production, materials-detail
- sources: R00a-F37 (R00a:1466-1489); R01-F39 (R01:632-642)

### CD-11 Invent creatures from real anatomy
- principle: Once anatomy is understood, combine parts of real animals (and humans) to make creatures that do not exist but still look believable.
- why: Real parts carry believability even in a strange combination.
- apply: Creature briefs name a real source per body part; reference-images prompts state them.
- check: Each body part maps to a named real source; the creature reads as a living beast to a fresh agent.
- mistake: Invented anatomy with no real basis [inference].
- examples:
  - R00a: Nunu's Willump: lion face, bear pelvis, six insect-like arms (R00a:1491-1523).
- roblox_fit: No change.
- roles: modeler, art-director, character-rigger, animator, reference-images
- also: references-ideation
- sources: R00a-F38 (R00a:1491-1523)

### CD-12 Design for motion: test extreme poses, keep mass off the joints
- principle: Parts that look great in a neutral pose may fail in motion. Collars, scarves, armour and long hair near a joint block poses or clip; static (unjointed) hair must not extend into areas that deform; long coattails and billowing sleeves need their own cloth rig. Fix the design with the rigger and animator before the final model.
- why: Players see the character moving almost all the time; dramatic motion collides with or deforms costume near joints, and every extra cloth chain costs rig time and performance.
- apply: Before the final model, pose-test extremes in Blender (arms up, head turn, crouch, attack). Leave clearance around neck, shoulders and wrists; bundle hair into one unit set away from the nape; keep unjointed hair off bending shoulders and chest; flag long cloth in concept as a cost and ask the rigger before keeping it (easy fix: shorter or removed).
- check: Pose renders at extreme poses and a fast clip (walk, attack, head turn): no intersection with face, body, legs or collar in frame captures; `clip_check.py` sampled frames reviewed at the extremes.
- mistake: Approving designs in neutral pose only (a character who cannot raise its arms without stabbing its face); long hair "right against the nape"; static hair extended into costume.
- examples:
  - R00a: collars, scarves and armour can limit animation (R00a:1530-1562).
  - R11: Katarina's hair moved to a ponytail away from the neck; Ahri's condensed braid (R11:305-314).
  - R01: a wavy strand on the temple joint; static hair over the shoulder kept short (R01:541-553).
  - R03: Caitlyn's coattails need their own cloth rig (R03:910-929).
- roblox_fit: R15 has a Neck joint between Head and UpperTorso and separate body meshes (knowledge/external/roblox-creator-docs/art/characters/specifications.md:29, 535); mass across that cut breaks, and rigid part rigs make clipping more visible.
- roles: modeler, character-rigger, animator, art-director, reference-images, reviewer
- also: pipeline-production, shape-silhouette
- sources: R00a-F39 (R00a:1530-1562); R11-F25 (R11:305-314); R01-F33 (R01:541-553); R03-F39 (R03:910-929)

### CD-13 Twist the tone within bounds; darker still keeps the appeal
- principle: A variant or new universe may push a character's tone (fun to frightening, light to dark), but only as far as the theme needs. Pushed darker, the character keeps its charisma, poise and aspirational quality.
- why: Surprise keeps variants fresh; staying in bounds keeps the character; players want to be or own the character, so losing appeal loses them.
- apply: The variant brief states the tone shift and its limit, plus "keep: poise, confidence" or the equivalent. Sound can carry the twist (processing of existing lines). Reviews check pose and face for appeal.
- check: Tone words in the brief match the concept, the pose capture and the sound cue card; the final pose capture still reads heroic or aspirational to a fresh agent.
- mistake: Making a fun-theme character "evil or scary" (R01); stripping away inherent charisma (R11).
- examples:
  - R01: Star Guardian Zoe's happy lines plus a twisted voice filter become frightening; ringmaster Caitlyn is dangerous but not evil (R01:287-301).
  - R11: "Katarina is still meant to feel heroic, still meant to feel aspirational" (R11:253-256, 298-301).
- roblox_fit: Darker themes need a `platform-policy` check [inference]. Roblox audio effects (pitch, distortion) can process voice lines [unverified].
- roles: art-director, sound-designer, animator, reference-images, marketing, modeler, live-ops-designer
- also: style-identity, sound
- sources: R01-F18 (R01:287-301); R11-F23 (R11:253-256, 298-301)

### CD-14 Keep the cool core, swap one iconic item, justify it by lore
- principle: A fresh variant juxtaposes the character's cool core with an offbeat twist by swapping one iconic item (a fly-fishing hat for the ronin hat, a fishing pole for the sword), and the twist is justified by what the character already does.
- why: The contrast is fun; the lore link makes it feel right, not random.
- apply: For skins, events and limited items write the twist as one line: "keep X core, swap item Y for Z because of ability or lore W".
- check: The brief has that line with a lore reason; the anchors (CD-04) are still present in the result.
- mistake: A random theme with no link to the character [inference].
- examples:
  - R10: "Ionia's version of a dynamite fisherman": Yasuo makes wind walls, so he can fish with wind (R10:57-61, 188-194, 549).
- roblox_fit: No change.
- roles: art-director, game-designer, live-ops-designer, marketing, modeler, reference-images
- also: style-identity, references-ideation
- sources: R10-F09 (R10:57-61, 188-194, 549)

### CD-15 Re-theme the abilities, not only the costume
- principle: How a variant re-visualises the character's abilities (the power fantasy) is more often what makes it succeed than the costume.
- why: Players feel the theme through what they do.
- apply: Each variant brief includes an ability re-theme for VFX and sound per ability (a shot becomes a laser pointer chased by lions; a "bang" flag for the joke).
- check: Every ability in the variant has a themed VFX and sound note in the brief and a themed effect in the capture.
- mistake: Costume-only variants.
- examples:
  - R01: the shot becomes a laser, lions chase it and hit the target; the ultimate as a lion (R01:11-15, 347-359, 870).
- roblox_fit: Effects through ParticleEmitter, Beam and Trail within the particle budget [inference].
- roles: vfx-designer, sound-designer, animator, art-director, game-designer, marketing
- also: vfx-reads-timing, sound, style-identity
- sources: R01-F24 (R01:11-15, 347-359, 870)

### CD-16 Costume first, weapon second
- principle: Design the costume first; it informs the weapon. "It's easier to design a weapon a character is holding than ... the character that is holding a weapon."
- why: The weapon must match the costume's motifs and proportions.
- apply: Concept order: body and costume, then the prop; the prop brief cites the approved costume and its motifs.
- check: The prop brief references the approved costume revision; the prop shares at least one costume motif (SS-17).
- mistake: Designing the prop in isolation [inference].
- examples:
  - R01: the ringmaster gun designed after the costume was locked (R01:428-433).
- roblox_fit: No change.
- roles: art-director, modeler, reference-images
- also: process-iteration
- sources: R01-F29 (R01:428-433)

### CD-17 A complex signature item signals a skilled owner
- principle: A mechanically complex signature item tells the viewer its owner is uniquely skilled; a simpler version feels like "anybody could pick it up". Variants may drop pieces, but past a point that costs quality.
- why: Viewers infer skill and uniqueness from the tool a character carries.
- apply: Hero and signature items get more distinct parts and moving pieces than common items of the same class; a variant drops a piece only when it does not fit the theme (CD-18). Show complexity through big parts, not micro-geometry.
- check: Count parts and moving pieces of hero versus common items of the same class: hero clearly higher; review whether a variant lost quality by a removal.
- mistake: Simplifying the hero item until it reads as generic.
- examples:
  - R01: Caitlyn's complex, almost magical Hextech rifle (R01:670-688).
- roblox_fit: Complexity must fit the mesh budget (max 20,000 triangles per mesh: knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34).
- roles: art-director, modeler, reference-images, game-designer
- also: materials-detail, game-design-fun
- sources: R01-F42 (R01:670-688)

### CD-18 Drop inherited parts that do not fit the new fantasy
- principle: Parts inherited from the base can be dropped or replaced when they make no sense in the new theme; replace them with a theme-fitting element of similar mass.
- why: An element that contradicts the theme breaks the fantasy; similar mass keeps the silhouette.
- apply: For each base part ask "does this exist in this theme's world?"; replace with an equivalent shape that does.
- check: The variant parts list justifies each part by the theme; the silhouette mass of replaced parts matches the base.
- mistake: Keeping glass lenses on a water gun.
- examples:
  - R01: the Pool Party gun's lenses replaced with thick tubes (R01:886-892).
- roblox_fit: No change.
- roles: modeler, art-director, reference-images
- also: shape-silhouette
- sources: R01-F49 (R01:886-892)

### CD-19 Tell the theme through small nods on the gear
- principle: Carry the variant's theme into its gear with small, readable nods (a weapon shaped like a chrysalis, gardener gloves because butterflies belong in a garden).
- why: Props tell the fantasy's story without words, and fans enjoy finding them.
- apply: Variant briefs list 1-3 theme nods; modelers build them as shape changes on existing anchors, not added clutter [inference].
- check: A reviewer names the theme from the props alone in a close render; the nods do not change the anchors' black-fill silhouette.
- mistake: Theme added as extra clutter that hides the anchors [inference].
- examples:
  - R08: a cocoon-shaped weapon and garden gloves on Battle Butterfly Alune (R08:122-127).
- roblox_fit: Small nods read only in close views (shop, inspect); do not spend triangles on them beyond the budget [inference].
- roles: modeler, art-director, vfx-designer, reference-images
- also: style-identity, world-level-readability
- sources: R08-F04 (R08:122-127)

### CD-20 Small accents carry the personality
- principle: On characters the big areas tell the role and faction; the small objects (pins, decals, a charm) tell who the person is inside. Spend personality on a few small accents.
- why: Small chosen accents feel personal and intentional.
- apply: Character briefs: big areas set role or faction; 2-4 small accessories or decals carry personality, sized to stay visible at the game camera.
- check: At the game camera the personality accents are still visible (not sub-pixel); count them against the brief.
- mistake: Putting personality only in large garments [inference].
- examples:
  - R12: pins and decals versus the hoodie print; the 60/30/10 relation works "in an opposite way" on characters (R12:288-296).
- roblox_fit: Accents must be sized up for phone third-person views; Roblox accessories are a natural slot [inference].
- roles: art-director, modeler, character-rigger, marketing, reference-images
- also: light-colour, materials-detail
- sources: R12-F24 (R12:288-296)

### CD-21 Explore costumes on varied poses and body types
- principle: The classic stiff three-quarter concept pose shows details but robs the character of personality. Explore each costume in several attitude poses and body types; some clothes do not fit some personalities.
- why: A costume in motion and attitude shows whether it fits the character.
- apply: Reference-images exploration prompts show each costume in 2-3 attitude poses (for example hunched and aggressive, solemn); the clean turnaround comes only at the end, for the modeler.
- check: The exploration sheet shows each costume in at least two attitudes; the chosen one reads its temperament from pose alone.
- mistake: Only stiff three-quarter turnarounds during exploration.
- examples:
  - R11: Katarina "more hunched, more aggressive" versus "more solemn ... depressed", dressed differently for each (R11:198-209).
- roblox_fit: Same.
- roles: art-director, reference-images, modeler, animator, marketing
- also: references-ideation
- sources: R11-F17 (R11:198-209)

### CD-22 Put the eyes and face in early
- principle: Bring the eyes (and the face, or whatever the focal feature is) in early, even as placeholders, and bring the face to final quality before a review round. If the face is off, every first note is about it.
- why: Faces are read through the eyes first; without them the character feels dead and judgement of the rest is off; reviewers cannot see past an off face.
- apply: Add eye placeholders in the first texture or blockout pass. Before each review, the face (or focal feature) is at its best quality.
- check: Early review render has placed eyes; at review, the face matches the anchor images before other notes are given.
- mistake: Showing work with a weak face, so feedback stalls on it.
- examples:
  - R03: temporary irises on Caitlyn make her read as a person (R03:286-292).
  - R08: "even if everything looks beautiful, but the face looks a little bit off, the first note you will always get is on the face" (R08:821-840).
- roblox_fit: At phone size eyes may need to be larger or higher contrast; for faceless or small-face characters the "face" is the focal feature at the camera [inference].
- roles: modeler, art-director, reference-images, marketing, animator, reviewer
- also: critique-feedback, process-iteration
- sources: R03-F14 (R03:286-292); R08-F31 (R08:821-840)

### CD-23 Brows, face structure and nose carry identity
- principle: Eyebrows and facial structure are among the most identifying parts of a character; brow thickness changes the face silhouette a lot. Face shapes encode personality: a sharp, serious character needs a sharper, downward nose, not a button nose.
- why: Brows are expressive and high-contrast; face shapes are read as personality.
- apply: The character sheet specifies brow thickness and angle and nose shape; brows are exaggerated for small screens.
- check: Close and game-size head renders: a reviewer identifies the character from the head silhouette and brows alone, and the face shapes match the character card's tension words.
- mistake: A cute default face (button nose) on a sharp character (R03:388-390).
- examples:
  - R03: Caitlyn's sharper nose versus Lux's button nose; Goku known by eyebrows and hair (R03:360-366, 388-390, 968-974).
- roblox_fit: On phones only big face shapes survive [inference]; on dynamic heads, FaceControls carry brow poses (knowledge/external/roblox-creator-docs/_api-reference/classes/FaceControls.yaml).
- roles: modeler, art-director, reference-images, animator
- also: shape-silhouette
- sources: R03-F15 (R03:360-366, 388-390, 968-974)

### CD-24 Eyes act in fast turns
- principle: People blink on fast head turns: close the eyes during a fast spin, widen them on a fall, look from under the brows for intensity.
- why: Small eye acting makes motion feel alive and in character.
- apply: Key a blink on fast spins and head turns; widen on falls; brow-down look on intense beats.
- check: Frames during a spin show closed eyes; a fall shows wider eyes.
- mistake: Eyes frozen open through every turn [inference].
- examples:
  - R04: "humans often blink as soon as they turn their head" (R04:688-694, 1024-1046).
- roblox_fit: Dynamic heads animate eyes through FaceControls (LeftEyeClosed and others: knowledge/external/roblox-creator-docs/_api-reference/classes/FaceControls.yaml:63, 414); decal faces cannot blink without swapping textures [inference].
- roles: animator, film-director
- also: weight-timing
- sources: R04-F42 (R04:688-694, 1024-1046)

### CD-25 Start promo and story art from a premise and the signature ability pose
- principle: Decide the story premise in one sentence before the picture, and pose the character in their signature ability gesture.
- why: The premise tells which moment to draw; the signature move makes the character instantly identifiable.
- apply: Each promo or cutscene brief has a one-sentence premise; character poses reuse the ability's key pose from the game's animation set.
- check: The pose matches the in-game ability key pose (compare with a frame from the clip); a fresh agent reads the premise from the image.
- mistake: A generic pose disconnected from gameplay [inference].
- examples:
  - R05: "Sage's Last Revive": she raises her arm for her ultimate on a full moon (R05:81, 261-276, 283).
- roblox_fit: Reuse the in-game KeyframeSequence key pose for promo renders in Blender [inference].
- roles: animator, marketing, film-director, vfx-designer, art-director
- also: composition-focus, references-ideation
- sources: R05-F12 (R05:81, 261-276, 283)

### CD-26 Design a prop or a place as a character
- principle: Do not see a diorama or prop as a pile of objects; give it a personality, as if it were a character. When stuck on a prop, imagine it as one.
- why: Personality gives every shape and material choice a direction and makes ideas come more easily.
- apply: Each environment or prop brief states a personality in 3-5 words (for example "rigid, old, timeless") and maps it to shape language and materials.
- check: A fresh agent describes the prop's personality from a capture; compare with the brief words.
- mistake: Getting stuck because you cannot "connect to a specific tree or chair" (R13:939-941).
- examples:
  - R13: Zilean's shrine carries a rigid old time-traveller's personality without his figure (R13:927-945).
- roblox_fit: No change.
- roles: environment-designer, modeler, art-director, game-designer, level-design, reference-images
- also: world-level-readability, style-identity
- sources: R13-F36 (R13:927-945)

### CD-27 Hard cases: scary creature-humanoids and multi-form characters
- principle: A semi-humanoid creature is easy to make silly instead of scary; a character with several forms is several characters of work.
- why: Threat depends on proportion; each form multiplies model, texture and rig work.
- apply: Creature briefs flag "keep it scary" with a reference; job sizing counts each extra form as a separate character.
- check: A reviewer reads threat in the creature's silhouette; the job card counts forms.
- mistake: Making a scary creature "look very silly" (R03:622).
- examples:
  - R03: Kha'Zix, Kayn and two-form Sun-Eater Kayle (R03:616-632).
- roblox_fit: Same.
- roles: modeler, art-director, animator, character-rigger, game-designer, orchestrator
- also: pipeline-production
- sources: R03-F29 (R03:616-632)

### CD-28 Represent ethnicity and culture accurately
- principle: Represent a character's ethnicity and culture accurately; it is one of the hardest and most important parts of the job.
- why: Players notice and care; misrepresentation harms them and the product.
- apply: Briefs state the character's background; reference images and models respect it; reviewers check it.
- check: A reviewer checks features and skin against the stated background and canon before approval.
- mistake: Defaulting features away from the stated background [inference].
- examples:
  - R03: Caitlyn's mixed heritage represented in her features (R03:720-734).
- roblox_fit: Same; load `platform-policy` when a design draws on a real culture [inference].
- roles: modeler, art-director, reference-images, reviewer
- also: style-identity
- sources: R03-F32 (R03:720-734)

### CD-29 Move a sensitive theme onto a prop motif
- principle: Express a theme that could read badly (animals in captivity) through a motif on a prop instead of an act or scene.
- why: It keeps the theme and avoids an offensive read.
- apply: The sensitivity check in review redirects such themes to prop motifs.
- check: A reviewer confirms no problematic act is shown; the theme still reads from the motif.
- mistake: Content that could be construed as animal abuse.
- examples:
  - R01: a lion head sculpted on the gun barrel instead of caged lions (R01:612-622).
- roblox_fit: Load `platform-policy` for any sensitive theme.
- roles: art-director, game-designer, reference-images, marketing, reviewer
- also: style-identity
- sources: R01-F40 (R01:612-622)
