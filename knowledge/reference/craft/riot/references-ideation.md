---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [reference-images, art-director, modeler, environment-designer, vfx-designer, ui-ux-designer, animator, character-rigger, sound-designer, game-designer, marketing, film-director, live-ops-designer, orchestrator, reviewer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# References and ideation

How ideas are found and chosen before anything is built: the problem first, research and reference, many options, distinct hooks, reasoned picks. In our pipeline reference images come from ChatGPT's image model through the `reference-images` skill (one art bible, approved anchors); "drawing", "photographing" and "acting out" become prompts, Blender renders and written beat sheets.
RI-01 to RI-04 set what concept work is for. RI-05 to RI-15 are research and reference. RI-16 to RI-23 are exploration, options and choosing. RI-24 to RI-26 are motion reference. RI-27 to RI-30 give ideas a story, a symbol, a hook and room.
Related: closing doors and gates in `process-iteration.md`, feedback on options in `critique-feedback.md`, the concept-to-3D step in `character-design.md` (CD-08).

### RI-01 Concept work solves a problem; it is a functional vehicle, not a nice picture
- principle: Concept art is visual problem solving: drawings are tools to communicate an idea, not the goal. "Design is not about making good art, it's about making these functional vehicles for other things" (R11). Judge a design by what it adds to or takes from the player experience and what it costs to build.
- why: The team needs decisions, not finished pictures; a flashy design players must "fight in order to understand" fails.
- apply: Each reference-images request states the problem it answers. Every design hand-back has two required lines: its effect on play clarity and its build cost. ChatGPT images are targets, never final assets.
- check: The image caption names the problem and how the image answers it (a reviewer can say yes or no); the review form has the clarity and cost lines filled; "looks cool" alone is rejected as a reason.
- mistake: A beautiful image that solves nothing; treating a concept task as "a nice looking character that is just meant to be cool".
- examples:
  - R00a: "concept art isn't about making beautiful, detailed drawings" (R00a:536-558).
  - R11: being good at art "is not good enough for what design demands of you" (R11:122-145, 383-390, 409-412).
- roblox_fit: Same.
- roles: art-director, reference-images, orchestrator, modeler, vfx-designer, environment-designer, ui-ux-designer, game-designer, marketing, reviewer
- also: critique-feedback, game-design-fun
- sources: R00a-F13 (R00a:536-558); R11-F10 (R11:122-145, 383-390, 409-412)

### RI-02 Show options at equal, low finish on a clean, labelled sheet
- principle: At thumbnail stage show the idea as fast as possible, with all options at the same low finish; polish on one option makes reviewers prefer it for the wrong reasons. The idea comes first; a clean, consistent presentation comes second but still matters.
- why: Uneven polish biases the choice; decision makers judge what they see.
- apply: Owner-facing option sheets: same camera, same background, same finish, labelled A, B, C; no messy work files.
- check: Options shown together have similar finish and layout; reviewer feedback is about idea, story and read, not rendering.
- mistake: Over-drawing one option so it wins by finish; good ideas in messy form.
- examples:
  - R08: "if we get to focus on those nitty-gritty details, people are gonna have a bias towards certain ones" (R08:554-568).
  - R12: a "luxury look" presentation helps sell ideas (R12:277-280).
- roblox_fit: No change.
- roles: art-director, reference-images, orchestrator, marketing, game-designer, reviewer
- also: critique-feedback
- sources: R08-F25 (R08:554-568); R12-F22 (R12:277-280)

### RI-03 Know the problem, the constraints and the end before making anything
- principle: Before any image, know what you are solving, the constraints (theme, camera, mechanics, numbers, budget) and what the end result should look like. A prompt or concept is a suggestion of intent; constraints decide what is built, and deviations are said out loud.
- why: Exploration without a target does not move the team; if you do not know what the final looks like, nobody else will; concept paintings ignore engine cost.
- apply: Every visual brief opens with problem, constraints and success test; no image generation before these are written. Every direction has an approved target image (art-bible anchor) before production. Builders treat the reference as intent, not a frame to copy, and list each deviation (budget, tech, time) with its reason in the hand-back.
- check: The brief has the three items and each option can be checked against each constraint; an approved anchor exists before render; the hand-back lists deviations with reasons.
- mistake: "Just drawing something cool doesn't necessarily push the team toward its goals" (R00a); "not knowing what you want your piece to look like at the very end" (R08); copying a concept and breaking budget, or deviating silently (R06:36-37).
- examples:
  - R00a: always be solving; constraints narrow focus (R00a:584-618, 921-926).
  - R08: a rough that already shows "what it's gonna end up as" (R08:568-586).
  - R06: "a happy storm" from the Teemo hat became clouds, lightning and raining candy within budget (R06:34-38).
- roblox_fit: Roblox constraints include the phone camera, triangle and texture budgets, particle caps (100 per second per emitter on mobile: knowledge/external/roblox-creator-docs/effects/particle-emitters.md:212) and no custom shaders; list them in the brief.
- roles: art-director, reference-images, orchestrator, game-designer, modeler, vfx-designer, environment-designer, ui-ux-designer, film-director
- also: critique-feedback, process-iteration
- sources: R00a-F14 (R00a:584-618, 921-926); R08-F26 (R08:568-586); R06-F03 (R06:34-38)

### RI-04 In marketing art, the launched thing is the hero
- principle: Key art serves what the product is doing (a new map, character, skin). Start from that strategy and make the launched thing the hero of the composition; when options are hard to pick, go back to the strategy.
- why: The picture's job is to make the player want the new thing; a beautiful picture that hides it fails.
- apply: Every marketing brief (icon, thumbnail, update art) names the one thing being launched and makes it the largest, clearest element; prompts state the hero object first. With no brief, agents write one ("we are our own brand managers").
- check: In the 16:9 thumbnail at player size (`thumb_check.py thumbnail`), a fresh agent asked "what is this update about?" names the hero first, and it is the largest readable element.
- mistake: Choosing between equally good options by taste instead of by the brief (R05:162-164).
- examples:
  - R05: for a new map, "that map has got to be almost like the hero of the composition" (R05:55-61, 162-164, 834-838).
- roblox_fit: Thumbnails are 16:9, ideally 1920x1080 (knowledge/external/roblox-creator-docs/production/publishing/thumbnails.md:54).
- roles: marketing, art-director, orchestrator, live-ops-designer, film-director, reference-images
- also: composition-focus, pipeline-production
- sources: R05-F01 (R05:55-61, 162-164, 834-838)

### RI-05 Research first; one narrow moodboard with pillars and key features
- principle: The first step of any concept is research: compile reference, check cultural fit and sensitivity, then build one narrow moodboard with a few pillar words. For an open tone, moodboard the genre the piece imitates and read its recurring traits. List the 3-5 key features that make the subject read.
- why: A narrow board gets cheap early feedback and keeps everyone on one target; scattered boards cause pivots; reference makes creations more compelling.
- apply: Before anchors, the art director makes a moodboard with reference-images (collected references plus generated mood images), one direction, 3-5 pillar words [inference: count], a one-line sensitivity note and a key-features list per subject; owner feedback before any asset work. Include Roblox games on the same camera to see what reads [inference].
- check: The board shows one consistent direction (palette and shapes consistent); pillars, sensitivity note and key features exist; each key feature is visible in the later game-camera capture; no single reference is recognisable in the output.
- mistake: "A moodboard that's too general or scattered will make it hard to stay focused" (R00a); skipping research (done only "in the interest of time", R01:74).
- examples:
  - R00a: research, then a narrow moodboard with pillars for cheap early feedback (R00a:664-716, 1629-1639).
  - R01: "Lion Tamer Caitlyn" from a mug, widened to a big-top ringmaster theme after research (R01:52-56).
  - R05: retro horror posters set a cheesy B-movie tone and lots of orange (R05:115-141).
  - R09: lava's key features: colour, oozy texture, smoke for heat, glow (R09:536-550).
- roblox_fit: Young audiences make the sensitivity note feed `platform-policy` for mature or franchise themes.
- roles: art-director, reference-images, environment-designer, modeler, vfx-designer, ui-ux-designer, marketing, film-director, sound-designer, orchestrator
- also: style-identity, critique-feedback
- sources: R01-F01 (R01:52-56); R00a-F18 (R00a:664-716, 1629-1639); R05-F05 (R05:115-141); R09-F28 (R09:536-550)

### RI-06 Each theme gets a library: shorthand motifs, iconography, a name and a logo
- principle: A new theme gets a visual library before character work: shorthand motifs the audience already links to it (diamonds and playing cards for a circus), shape language, iconography, a name and a logo.
- why: Familiar motifs give instant recognition with few shapes; shared iconography makes every asset feel from one world.
- apply: The art bible holds per theme 3-5 shorthand motifs [inference: count], shape language, icons and a logo; costume, prop, UI and VFX draw on them.
- check: A fresh agent names the theme from a thumbnail; assets use library motifs and icons.
- mistake: Inventing new symbols per asset so the theme never reads as one world [inference].
- examples:
  - R01: diamond buttons and a harlequin pattern for the circus (R01:277-281); the circus would get a name and a logo for her hat (R01:592-600).
- roblox_fit: No change.
- roles: art-director, reference-images, modeler, ui-ux-designer, vfx-designer, environment-designer, marketing, orchestrator
- also: style-identity, shape-silhouette
- sources: R01-F17 (R01:277-281); R01-F36 (R01:592-600)

### RI-07 Turn each keyword into visual facts before prompting
- principle: Exploration starts by writing what each keyword gives visually: "apocalypse" = dust colours and an abandoned city; "survivors" = serious, worn faces; "zombie" = grey and green.
- why: Keywords alone are vague; concrete colour keys, settings and expressions make the idea drawable and shared.
- apply: Before the first image prompt, write a keyword table: keyword, colour key, setting, expression or pose, prop. Build prompts from it; existing game maps and assets can be the setting.
- check: Every element in the first rough maps to a row of the keyword table, and no row is missing from the image.
- mistake: Generic first compositions with no visual research (R05:91-95).
- examples:
  - R05: apocalypse = dust colours; survivors = serious faces; zombies = grey and green; the Fracture map as setting (R05:83-113).
- roblox_fit: Reuse existing game maps and assets as settings for marketing art.
- roles: reference-images, art-director, marketing, environment-designer, modeler, vfx-designer
- also: light-colour
- sources: R05-F03 (R05:83-113)

### RI-08 Reference order: our game first, then the real world, then mix; take ideas, never copy
- principle: Start with the best existing art of the same line (the game's own anchors) for colour, composition and gesture, never stop there: add real-world reference and combine both into something new. Gather much more than you show; take ideas (shape language, colour, light), never a design.
- why: Existing art alone is "derivative of derivative of derivative"; only real sources add new information; the head's visual library is too small to invent from.
- apply: Reference-images builds a two-part board: (a) approved anchors and art-bible images, (b) real-world photos or descriptions per aspect (pose, material, colour, place); each entry notes what it is for. Prompts cite the aspects taken, not a design.
- check: The board has both parts and a stated purpose per entry; the result reproduces no single reference design.
- mistake: Ending reference with "what is already created"; going "off our brain"; too few references; copying a design.
- examples:
  - R08: Anima Squad splashes for crop focus, plus Pinterest sitting references for queenly poses (R08:149-200).
  - R13: a Wild Rift Shurima Zilean skin chosen because its sand and gold ties to the set; what he shows is under 10 % of what he gathers (R13:331-353).
- roblox_fit: Copying designs also risks IP problems (`platform-policy`) [inference].
- roles: art-director, reference-images, modeler, animator, environment-designer, vfx-designer, marketing, film-director
- also: style-identity, critique-feedback
- sources: R08-F06 (R08:149-200); R13-F14 (R13:331-353)

### RI-09 When a brief fuses two ideas, reference the overlap
- principle: When a brief merges ideas (samurai plus fly fisher plus wind), gather reference for where they overlap: an object that feels like both (katana and fishing pole), costume pieces of the new idea, poses from both worlds. If the exact pose does not exist, make your own reference.
- why: The fusion is the design; reference for each idea alone gives a costume swap; own reference avoids painting "the exact same thing someone else is painting" (R10:89-91).
- apply: The reference-images brief lists three overlap columns (object, costume, pose) and asks for a moodboard per column before key art; for a unique pose, pose the rig or a mannequin in Blender from the game camera and render it [inference: our stand-in for photos].
- check: At least one board image per column shows both ideas at once; the chosen pose is not a stock pose from the first search results.
- mistake: Referencing each idea separately and stacking them.
- examples:
  - R10: where a fishing pole and a katana "feel" alike, plus fishing and sword-fighting poses (R10:63-91).
- roblox_fit: Blender pose renders replace photos.
- roles: reference-images, art-director, modeler, animator, marketing, vfx-designer
- also: character-design
- sources: R10-F01 (R10:63-91)

### RI-10 Study the real thing closely for the details invention misses
- principle: Research real places, materials and phenomena and look at them closely: layouts and odd details of real places, how a material really behaves, the true shape and timing of fire, storms and impacts.
- why: Real sources supply specific, believable detail; without research "you'll just keep creating the same types of textures" (R02); direct observation builds a model you keep.
- apply: For each new setting, material or natural effect, gather real-world reference (photos, footage descriptions, frames) and note the specific details, shapes and timing phases to use; feed them into prompts, kit lists and effect specs.
- check: The hand-back names the references used and at least one observed property (a detail, shape or timing) it took; each listed detail appears in the build or is marked rejected.
- mistake: Generic, invented details; building from memory only.
- examples:
  - R00b: vacation photos of "weird pipes, dark weird corners, dirty grates, and old kitchens" (R00b:1989-2011).
  - R02: birch bark, moss and wood researched before painting (R02:358-366).
  - R03: a brother in a red blanket to understand a cape (R03:674-690).
  - R00c: find a lot of reference and look at it very closely (R00c:3884-3888).
  - R06: watch a real campfire, go out in a storm; a board of flames and lightning (R06:387-391).
- roblox_fit: No change.
- roles: environment-designer, modeler, art-director, reference-images, vfx-designer, animator, sound-designer
- also: materials-detail, vfx-reads-timing
- sources: R00b-F13 (R00b:1989-2011); R02-F18 (R02:358-366); R03-F27 (R03:674-690); R00c-F16 (R00c:3884-3888); R06-F31 (R06:387-391)

### RI-11 Read the concept's intent and its materials; do not trace its strokes
- principle: Do not copy a concept stroke by stroke; understand what it says and translate that. Ask what each material really is (gold armour or shiny cloth? silky or velvety?), and start each material from its local colour (its colour with no light on it).
- why: A 3D model seen from many angles cannot match a 2D image pixel for pixel; intent survives, pixels do not; the same colour can be very different materials, and a wrong guess changes the read and the rig.
- apply: Before modelling, write 3-5 lines of concept intent (who, mood, key reads, materials) and a material list with type and a real reference each; ask the art director when a material is unclear; set each material's base colour to its unlit local colour.
- check: A game-camera render next to the concept at the same size: the intent lines hold; each region reads as its named material; each flat base colour matches the concept's mid-tone, not its shadow or highlight.
- mistake: Copying surface detail back and forth (R03:82-86); guessing material intent.
- examples:
  - R03: base colours laid down "without any lighting" (R03:80-86, 782-789).
  - R03: "did they really want it to be gold armor or ... a shiny cloth"; "is this material more silky? ... more velvety?" (R03:270-276, 818-825).
- roblox_fit: MaterialVariant and SurfaceAppearance choices follow the same decision [inference].
- roles: modeler, art-director, character-rigger, reference-images, vfx-designer
- also: materials-detail, character-design, light-colour
- sources: R03-F02 (R03:80-86, 782-789); R03-F13 (R03:270-276, 818-825)

### RI-12 Get enough reference; make the missing one
- principle: Collect a breadth of reference (a day or two is normal); if none shows the needed pose or angle, make it: "there's literally no reason not to have enough reference".
- why: Breadth gives options to combine into something new; made-to-order reference removes guessing.
- apply: When no reference exists, generate it: a ChatGPT pose image, a posed Blender mannequin with the Roblox rig's proportions, or a keyed test pose in Studio; budget reference time before production [inference for tools].
- check: The brief cites at least one reference for every key pose and material; none is marked "from memory".
- mistake: Drawing a pose with no reference because none was found.
- examples:
  - R08: the speaker photographs her own pose reference (R08:190-218).
- roblox_fit: A Blender mannequin with Roblox rig proportions gives pose reference true to the avatar [inference].
- roles: reference-images, art-director, animator, modeler, orchestrator
- also: process-iteration
- sources: R08-F07 (R08:190-218)

### RI-13 Reference sheets include front, side, back and the game-camera view
- principle: Concepts are often drawn from the game angle only; without orthographic views (front, side, back) the 3D maker must guess, and guesses drift from intent.
- why: Missing views force guesses.
- apply: Reference-image sheets for any model include front, side and back views plus the game-camera view.
- check: Before modelling, all three orthographic views exist; the final render is compared with each.
- mistake: Modelling from one angle and guessing the rest [inference].
- examples:
  - R03: in-game concept versus orthographic sheet (R03:834-854).
- roblox_fit: The back view matters most for third-person cameras [inference].
- roles: reference-images, modeler, art-director
- also: pipeline-production, character-design
- sources: R03-F36 (R03:834-854)

### RI-14 Learn light placement from painted art
- principle: Study concept, splash and comic artists to learn why shadows and highlights go where they go.
- why: 2D artists place light by choice, so their decisions are visible and teachable.
- apply: Art-bible anchors and reference images include painted key art whose shadow and highlight placement the 3D work follows.
- check: Compare highlight and shadow placement on a render with the anchor painting.
- mistake: Only studying other 3D work (R03:522-524).
- examples:
  - R03: splash-art hair rendering; Mignola's Hellboy (R03:516-530).
- roblox_fit: Same.
- roles: modeler, art-director, environment-designer, vfx-designer, reference-images
- also: light-colour
- sources: R03-F23 (R03:516-530)

### RI-15 Learn by recreating work you love, then twist it
- principle: Recreating loved work teaches faster than a blank canvas; recreate the structure, then add your own twist.
- why: Recreating forces you to understand why the reference works.
- apply: Before a new UI or motion style, collect 2-3 successful references in the genre, make a quick structural study (wireframe or paint-over), then change it toward our thematic. References are study material, never final assets; copy structure, never assets or branding.
- check: The final design differs visibly from the references in style while keeping the learned structure.
- mistake: Starting from nothing; stopping at the copy [inference].
- examples:
  - R00d: recreating favourite games' HUDs and menus (R00d:5007-5045).
- roblox_fit: Copying others' assets or branding is not allowed [inference].
- roles: ui-ux-designer, reference-images, art-director, animator
- also: ui-ux, style-identity
- sources: R00d-F19 (R00d:5007-5045)

### RI-16 Research, explore wide and loose, iterate on one or two, finish only what the next maker needs
- principle: Concept work runs research, exploration (as many loose ideas as possible), iteration on the strongest one or two, then finish to what the next maker needs. Chasing originality paralyses; quantity beats polish while exploring; a real exploration is "about five times the amount of art" of a one-hour demo (R11).
- why: Breadth first means the chosen direction won against real alternatives; a rough sketch is often enough for the team to understand and get excited.
- apply: Reference-images plans rounds: (1) research moodboard, (2) exploration sheet of many distinct rough options (PROPOSAL default: 6-12 thumbnails across clearly different directions [inference]), (3) variants of the 1-2 picks, (4) one final sheet for the modeler. No final-quality render in round 2; polish only after a recorded pick. Source scale: research about a week, concepting 2-3 months (R11).
- check: Count distinct directions in the exploration round (silhouettes differ in black-fill, not only colour); the job record shows the four stages; no refined render exists without a recorded pick.
- mistake: Spending long on one polished piece; jumping from one idea straight to finish; being "obsessed with making good art" (R00a).
- examples:
  - R00a: many hands in one weekend; sheets of 50-100 staff designs under constraints (R00a:438-464, 730-760, 944-946, 980-984, 1030-1034).
  - R11: Katarina: base, darker variants A, B, C, a vampire-hunter last bid, then an A+B merge to finish (R11:24-30, 287-293, 441-448).
  - R12: Zeus Phantom: research, line sketch, cleanup, colour and shading (R12:40-44).
- roblox_fit: The image model makes breadth cheap, so the risk is too little selection, not too little output [inference].
- roles: art-director, reference-images, modeler, vfx-designer, ui-ux-designer, marketing, environment-designer, character-rigger, orchestrator
- also: process-iteration, critique-feedback
- sources: R00a-F19 (R00a:438-464, 730-760, 944-946, 980-984, 1030-1034); R11-F01 (R11:24-30, 287-293, 441-448); R12-F03 (R12:40-44)

### RI-17 Take the big swings at concept stage
- principle: Concept is the only stage for large changes, so try them: "if we can change it we should, just to see". If the final stays close to the base, it must be because the tested alternatives lost.
- why: Later crafts cannot make big swings; untried directions are lost for good.
- apply: Each exploration round includes at least one radical option that changes a primary trait (hair shape, silhouette, main material); everything is "up for grabs until proven otherwise", then decide what is core.
- check: The exploration sheet shows at least one option changing a primary trait; the hand-back says why the chosen one won.
- mistake: Doing "just what came before".
- examples:
  - R11: a short bob on Katarina; a full mask on a character who never hides her face (R11:57-58, 69-76, 233, 240-241, 294-297).
- roblox_fit: Same.
- roles: art-director, reference-images, modeler, game-designer, vfx-designer, ui-ux-designer
- also: process-iteration
- sources: R11-F03 (R11:57-58, 69-76, 233, 240-241, 294-297)

### RI-18 Each option gets its own hook from a different source
- principle: Under the same problem and constraints, each option takes its idea from a different source (candy crystals, a snake staff, a frog staff), or a different reading of the theme (past, future, "what is this object really?"). Make two or three solid, distinct directions first; variations come only after the pick.
- why: Options that differ only in detail give nothing to choose between; a fiction gives every later part a reason.
- apply: When generating options, assign each a different source or fiction one-liner in the prompt ("a gun made by cyclopes", "a small lab producing thunderbolts"); about 3 distinct directions (different layout, story or camera, not colour variants) before any polish (R05).
- check: Black-fill the options: silhouettes or layouts differ clearly (two alike are one direction); each option has a one-line fiction that explains its major parts.
- mistake: Many near-identical options; variations of one idea presented as different options [inference].
- examples:
  - R00a: a wizard's staff topped by a crystal: candy-mancer, snake staff, frog staff (R00a:766-800).
  - R12: Zeus power locked in a gun that is "a small laboratory"; the magazine becomes a battery (R12:45-56, 192-193).
  - R05: three thumbnails (classic survivors, big heads with a giant silhouette, survivors fighting), then variants (R05:144-156, 166-172, 286-291).
- roblox_fit: Same for icons, thumbnails, UI moods and level layouts.
- roles: reference-images, art-director, modeler, vfx-designer, game-designer, marketing, environment-designer, ui-ux-designer
- also: shape-silhouette, style-identity
- sources: R00a-F20 (R00a:766-800); R12-F04 (R12:45-56, 192-193); R05-F06 (R05:144-156, 166-172, 286-291)

### RI-19 Present options with your pick and the reasons; then iterate
- principle: Scribble several options, present them, the director picks with feedback, then iterate. Always state the makers' own preference with a reason tied to the brief, and record why each rejected option lost. Stakeholders choose twice: at silhouette or thumbnail stage, and at the finished treatment.
- why: Comparing options is cheaper than fixing a polished wrong idea; a stated preference helps people who find every option good; reasons make the choice reviewable.
- apply: Generate about 3 rough, clearly different options with one line of intent each and the maker's pick; at owner gates, every options sheet has exactly one marked recommendation with a reason; the job notes record each rejection reason. Polish starts only after a recorded pick.
- check: The hand-back has several options differing in layout (not only colour), one recommendation with a reason tied to the brief, a rejection reason per option, and polish dated after the pick.
- mistake: "Good luck, choose the best one" (R05:162, 840); going straight from the first idea to polish (R10:158-166).
- examples:
  - R10: messy scribbles presented as options; the director picks; back and forth (R10:109-115, 158-166, 198-209, 476-482).
  - R13: a one-line story prompt, three sketches, option 3 chosen with reasons (R13:21-34, 46-50, 1024-1027).
  - R05: sketches chosen by silhouette, treatments chosen at the end, always with "personally, we think this one is gonna work better" (R05:164-176).
- roblox_fit: No change.
- roles: art-director, reference-images, orchestrator, marketing, environment-designer, modeler, game-designer, reviewer
- also: critique-feedback, process-iteration
- sources: R10-F03 (R10:109-115, 158-166, 198-209, 476-482); R13-F03 (R13:21-34, 46-50, 1024-1027); R05-F08 (R05:164-176)

### RI-20 For the final pick, compare four or five strong small options and choose the clearest
- principle: For a key image, make at least four or five thumbnails that feel finished at their small size, compare them, eliminate, and pick the clearest direction; seeing them together may spark further ideas.
- why: Comparison makes the choice rational and reveals ideas one option would hide.
- apply: PROPOSAL default from the source: 4-5 options per visual direction, labelled A-E, the pick recorded with "clearest" measured against the sell list (CD-02).
- check: The job folder holds the options; the pick record says why it beat the others.
- mistake: Settling on one option without comparison.
- examples:
  - R08: options A-D; A chosen as "the clearest", though the speaker liked C's pose (R08:292-299, 634-642).
- roblox_fit: Same.
- roles: art-director, reference-images, marketing, ui-ux-designer, film-director, orchestrator
- also: critique-feedback
- sources: R08-F12 (R08:292-299, 634-642)

### RI-21 The first output is a warm-up; reject the typical idea
- principle: The first drawing of a day and the first thumbnail of a task are usually the weakest: they default to the expected idea. Get them out of the way, make more, and look for the surprising option, even a tiny sketch in the corner.
- why: First attempts sit "in the range of expectation"; understanding the theme speeds up later options; the unusual idea is memorable.
- apply: Never stop at the first image result: the first batch is a warm-up and further variants use changed prompts; every concept brief asks for one deliberately atypical option; plan at least two option rounds, with a slow first one.
- check: The record shows how many options were made before the pick (a pick from one fails); the set holds at least one non-obvious idea; the first option is labelled warm-up.
- mistake: "We'll just draw one thing" (R08); going with "what we think Alune would do"; treating the first concept as the answer.
- examples:
  - R08: "our first thumbnail is never going to be the best one" (R08:220-232, 620-634).
  - R12: one sketch on day one, six on day two (R12:202-207, 451-455).
  - R08: Alune riding the moon like a swing won over weapon variants (R08:854-875).
- roblox_fit: Roblox discovery rewards distinct ideas, but the twist must still read at icon size [inference].
- roles: reference-images, art-director, marketing, game-designer, modeler, vfx-designer, orchestrator, reviewer
- also: process-iteration, critique-feedback
- sources: R08-F08 (R08:220-232, 620-634); R12-F18 (R12:202-207, 451-455); R08-F32 (R08:854-875)

### RI-22 Vary one element per option, label them, merge the best two
- principle: Explore by changing one named element at a time (jacket, pants, hair, makeup), including trends that may not fit; label options A, B, C; merge the strongest two; use a last bid to test an extreme.
- why: Single-change variants show what each element does; merging keeps the best of both.
- apply: Reference-images prompts vary one named element per option; options are labelled; the iteration prompt states "A's X + B's Y".
- check: Each option differs from the base in a named element; the final cites the options it merged.
- mistake: Variants that change everything at once so nothing is learned [inference].
- examples:
  - R11: "I'm gonna mix A and B together"; a vampire-hunter full mask as a last bid (R11:266-283, 290-301).
- roblox_fit: Same.
- roles: art-director, reference-images, modeler, ui-ux-designer, vfx-designer, environment-designer, marketing
- also: critique-feedback
- sources: R11-F21 (R11:266-283, 290-301)

### RI-23 Bring in one unexpected element from outside the genre
- principle: Keep what is expected (an assassin stays light and agile) and find one unexpected element; list what the subject has and lacks. New ideas come from outside the genre and outside your own taste; when something repels you, find out why.
- why: Without curiosity work becomes "derivatives of derivatives"; one unexpected element makes a design feel evolved, not copied.
- apply: Moodboards include (a) the subject's current reads, (b) the faction or world style to keep, (c) at least one source family from outside games (fashion, architecture, another medium). Briefs carry "keep:" and "try:" lists, one named unexpected element, and pitches name one outside-genre source; note one disliked reference and what it teaches.
- check: The board spans at least one non-game discipline; the brief names the unexpected element in one line; the pitch names its outside source.
- mistake: Moodboards made only of other game art; doing your take on something already done; liking design only "when it confirmed my own taste".
- examples:
  - R11: Katarina's research was mostly fashion while she stays "a citizen of Noxus" (R11:40-54).
  - R11: his early designs "felt not interesting enough" until curiosity widened his sources (R11:325-350).
  - R10: practise by moving a known story into another genre (Pinocchio as a Soulsborne) (R10:813-850, 852-861).
- roblox_fit: Counters generic AI output [inference].
- roles: art-director, reference-images, game-designer, marketing, ui-ux-designer, environment-designer, modeler, sound-designer, live-ops-designer, film-director, orchestrator
- also: style-identity
- sources: R11-F02 (R11:40-54); R11-F27 (R11:325-350); R10-F27 (R10:813-850, 852-861)

### RI-24 Act it out: agents write the performance beat by beat
- principle: The best way to plan motion and effects is often to act them out (with props of the right weight, making the sound effects) and to know the character's subtext; performance must "hit the back wall". Agents cannot act, so they write the performance and gather real motion reference.
- why: Acting gives timing and motion direction a body sense; it is hard to see an effect only in your head.
- apply: Before keying or building, write a beat-by-beat sheet: per beat the motion direction, timing in seconds or frames, a sound word, and the character subtext; gather real motion references (performers, weapon weights) or generate a key-pose sheet; run a short notes exchange with another agent on the plan.
- check: The plan lists reference sources, key poses and per-beat motion, sound word and time before any keys are set or emitters built; a subtext line exists.
- mistake: Animating or building "in your head" without reference or felt timing.
- examples:
  - R00b: animators film themselves and brainstorm a death animation together (R00b:3011-3072).
  - R06: "swirling things in and exploding them out" acted at the desk; it "almost feels like animation" (R06:218-222).
  - R04: wooden sticks of similar weight to ask how Akali would swing her swords (R04:618-646).
- roblox_fit: Big readable performance suits small phone screens [inference].
- roles: animator, film-director, vfx-designer, sound-designer, game-designer, reference-images
- also: weight-timing, character-design, rhythm
- sources: R00b-F32 (R00b:3011-3072); R06-F22 (R06:218-222); R04-F30 (R04:618-646)

### RI-25 Pose to pose from motion reference
- principle: Motion reference shows body mechanics and how the silhouette changes; from it, identify the key storytelling poses, place them on the timeline, then fill in, instead of working straight ahead.
- why: Key poses fix story and timing early and keep the clip manageable.
- apply: The animator lists key poses with frame numbers (30 fps) from reference before in-betweens; reference-images can make the key-pose sheet.
- check: The plan shows key poses and frames; key poses are reviewed as stills before interpolation.
- mistake: Straight-ahead animation without reference.
- examples:
  - R00b: the animator's own change after starting to use motion reference (R00b:3338-3362).
- roblox_fit: No change.
- roles: animator, film-director, reference-images
- also: weight-timing, shape-silhouette
- sources: R00b-F40 (R00b:3338-3362)

### RI-26 The same key poses can tell different stories: try two
- principle: The same two key poses can yield different stories and moods through timing and in-betweens; make alternatives and compare.
- why: Exploration finds the better option.
- apply: For key clips, make two timing or performance alternatives on the same key poses and let the director or owner compare.
- check: Two alternatives exist with a recorded choice.
- mistake: Shipping the first timing pass unexamined [inference].
- examples:
  - R04: a rehearsal version versus the live version of the same poses (R04:1050-1070).
- roblox_fit: No change.
- roles: animator, film-director, reference-images, orchestrator
- also: process-iteration, rhythm
- sources: R04-F43 (R04:1050-1070)

### RI-27 Design a variant through a narrative lens
- principle: A variant is the character seen through a new story, not "it's Olaf, but he's in a shirt": fit the archetype into the new universe.
- why: Narrative gives every choice a reason and makes the variant meaningful.
- apply: Each variant brief has a short story: the character's role in the new world and how the archetype maps.
- check: A reviewer states the character's in-world role from the brief and the image.
- mistake: Costume swaps with no narrative.
- examples:
  - R01: Blood Moon Evelynn: the succubus archetype reimagined as a yokai blood-moon cultist deity (R01:823-841).
- roblox_fit: No change.
- roles: art-director, game-designer, reference-images, marketing, live-ops-designer, sound-designer
- also: character-design, style-identity
- sources: R01-F47 (R01:823-841)

### RI-28 One message, one symbol, before drawing
- principle: Before drawing, decide what the design says: one clean message and its best visual sign; look at the letterforms of the name for shapes (the Z and S of "Zeus" look like thunderbolts).
- why: A single clear sign is remembered and repeats across object and brand.
- apply: Write the message and the symbol in the brief ("Zeus = thunderbolt"); test the name's letterforms for a logo or motif; use the symbol as the repeated motif (SS-17).
- check: The motif drawn as a one-colour black icon still reads at icon size (`thumb_check.py icon` on a black-fill motif).
- mistake: Starting to draw with no message.
- examples:
  - R12: the thunderbolt chosen as Zeus's sign; Z and S read as thunderbolts (R12:59-70, 88, 102).
- roblox_fit: The motif also serves the game icon, badges and UI glyphs at phone size [unverified].
- roles: art-director, ui-ux-designer, marketing, reference-images, modeler
- also: style-identity, shape-silhouette
- sources: R12-F05 (R12:59-70, 88, 102)

### RI-29 Find the hook that makes the subject compelling
- principle: Find a personal connection to each subject; with it you can feel whether the work is good; without it the work becomes a chore.
- why: Engagement gives judgement.
- apply: Agents write one line on what is compelling about the subject before making options, and judge options against it [inference].
- check: The brief has a "hook" line and option choices cite it.
- mistake: Repetitive detail with no joy (grass painted blade by blade, R10:706-712).
- examples:
  - R10: advice to find a personal connection to each subject (R10:682-704, 714-720).
- roblox_fit: No change.
- roles: art-director, marketing, game-designer, reference-images, film-director
- also: style-identity
- sources: R10-F23 (R10:682-704, 714-720)

### RI-30 Leave a marked placeholder for what is designed later
- principle: At exploration, interiors or later systems can stay abstract: show the room for something to be designed later instead of resolving it early.
- why: Keeps exploration fast and leaves later decisions open.
- apply: Mark placeholders as PROPOSAL in reference sheets and list them as open items for a later task.
- check: Every placeholder appears in the open-items list.
- mistake: Over-resolving secondary parts too early [inference].
- examples:
  - R12: an abstract energy generator inside the glass (R12:348-353).
- roblox_fit: No change.
- roles: art-director, modeler, vfx-designer, orchestrator, reference-images
- also: process-iteration
- sources: R12-F30 (R12:348-353)
