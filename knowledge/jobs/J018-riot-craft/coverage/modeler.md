---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2
supersedes: []
---
> Author: J018 maker modeler · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: modeler

Books rebuilt: `.agents/roles/modeler.md` (body only; frontmatter byte-identical to df13ff4), `.agents/skills/modeling-design/` (SKILL.md + references; new `references/read-and-form.md`), `.agents/skills/modeling-craft/` (SKILL.md + references; evals untouched). Line counts after repair round 2: design SKILL.md 120, craft SKILL.md 101 (new in round 2: `modeling-craft/references/read-commands.md`).

Legend for "landed in": `design` = `.agents/skills/modeling-design/`, `craft` = `.agents/skills/modeling-craft/`, `role` = `.agents/roles/modeler.md`. `design/SKILL §7 Pn` = core principle n. Self-review check ids (RP, SL, VL, CL, DT, MO, VA, GR, IM) are lines of `design/references/review.md` §5. Abbreviations: RF = `design/references/read-and-form.md`, RV = `design/references/review.md`, RC = `design/references/reference-check.md`, BU = `design/references/budgets.md`, KE = `design/references/kits-and-environment.md`, TM = `craft/references/textures-materials.md`, BR = `craft/references/blender-recipes.md`, RPA = `craft/references/rig-parts.md`, HO = `craft/references/handoffs.md`, TF = `craft/references/tripo-finish.md`, EI = `craft/references/export-import.md`, RCM = `craft/references/read-commands.md`.

## a. Findings

All 230 findings tagged `modeler` in `matrix.md` have a row; untagged findings used are at the end of the table (marked "untagged").

| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| CD-01 | Know the character, then decide on their behalf | RF §1 "Character" row; design/SKILL §7 P9; RV §5 RP2 | step / core principle / self-review check | |
| CD-03 | Understand the archetype before evolving it | RF §1 (archetype traits kept in every option); RV §5 SL11 | step / self-review check | |
| CD-04 | Variants hold the identity anchors and change the rest | design/SKILL §4 M-08; RF §1 anchors row, §7; RV §5 VA1; design/SKILL §7 P10 | standard / self-review check / core principle | |
| CD-05 | If a variant drops a silhouette landmark, fill its slot | RF §2 (head and carried items), §7; RV §5 VA2 | standard / self-review check | |
| CD-06 | Keep the likeness the same in every product | RF §7 "The same character everywhere"; HO §4 (icon face at crop); RV §5 SL10 | standard / self-review check | |
| CD-07 | The fantasy must survive every real view | design/SKILL §1 camera rule; RC §3 "Real views" row; RF §1 viewing conditions | standard / quality bar | |
| CD-08 | The concept is a blueprint: keep its iconic qualities, decide its gaps, exceed it in 3D | RC §7; design/SKILL §3 step 3; TF §2-§3 (restore iconic qualities); RV §5 IM4 (the RC §7 check run again at hand-off) | step / standard / quality bar / self-review check | |
| CD-09 | Every action shows who this character is | — | — | Animation craft (how a character runs); the modeler's share, body shape that predicts movement, is under SS-12 (RF §2, RV §5 SL7) |
| CD-10 | Believable anatomy and plausible construction | RF §5 (functional parts, attachments), §6; RV §5 DT4 | standard / self-review check | |
| CD-11 | Invent creatures from real anatomy | RF §6 (a real source per body part); RV §5 MO7 | standard / self-review check | |
| CD-12 | Design for motion: test extreme poses, keep mass off the joints | design/SKILL §3 step 5; RF §6; RPA §6; RV §5 MO1-MO2 | step / standard / self-review check | |
| CD-13 | Twist the tone within bounds; darker still keeps the appeal | RF §7 (a darker variant keeps poise and appeal) | standard | |
| CD-14 | Keep the cool core, swap one iconic item, justify it by lore | RF §7 "One iconic swap"; RV §5 VA3 | standard / self-review check | |
| CD-16 | Costume first, weapon second | RF §7 "Costume first, prop second"; RV §5 VA6 (cites the costume revision, shares a motif) | standard / self-review check | |
| CD-17 | A complex signature item signals a skilled owner | RF §7; RV §5 VA5 | standard / self-review check | |
| CD-18 | Drop inherited parts that do not fit the new fantasy | RF §7 (replaced by a theme-fitting shape of similar mass); RV §5 VA2 | standard / self-review check | |
| CD-19 | Tell the theme through small nods on the gear | RF §7 (1-3 nods as shape changes on anchors, theme nameable from the props); RV §5 VA6 | standard / self-review check | |
| CD-20 | Small accents carry the personality | RF §5 "Personality in a few small accents"; RV §5 DT7 | standard / self-review check | |
| CD-21 | Explore costumes on varied poses and body types | — | — | Costume exploration is concept work owned by the art director and `reference-images`; the modeler's share (a mannequin render as the image-edit input, PP-17) is in RF §7 |
| CD-22 | Put the eyes and face in early | RF §2 "Faces" (eye placeholders at blockout, face best before review); RV §5 SL10 | step / standard / self-review check | |
| CD-23 | Brows, face structure and nose carry identity | RF §2 "Faces"; RV §5 SL10 | standard / self-review check | |
| CD-26 | Design a prop or a place as a character | RF §1 "Character" row (3-5 personality words); design/SKILL §7 P9 example | step / example | |
| CD-27 | Hard cases: scary creature-humanoids and multi-form characters | RF §2 "Hard cases" | standard | |
| CD-28 | Represent ethnicity and culture accurately | design/SKILL §5 rules (respect a stated culture; `platform-policy`) | rule | |
| CF-01 | Big to small: composition first, detail and effects last | design/SKILL §4 M-02, §7 P4; craft/SKILL §3 step 3 | standard / core principle / step | |
| CF-02 | Design and pose for the side the game camera shows | design/SKILL §1 camera rule; RF §2 "Restated for our cameras", "Posed models"; BR §6 (back game camera) | standard / stage | |
| CF-03 | Put detail where the camera distorts least | RF §2 "Restated for our cameras" (focal detail on the least foreshortened area) | standard | |
| CF-04 | Compose inside the real frame, crop and UI, at final scale | HO §4 (icon crop, check at display size) | step / self-review check | |
| CF-06 | In a small frame, the identifying parts fill it | HO §4 "What fills the frame" | standard | |
| CF-08 | Shape flow points to the focal point, at every scale | RF §2 "Main lines first" (lines converge or run parallel); RV §5 SL5 | standard / self-review check | |
| CF-09 | Lines on an object lead somewhere and agree with each other | RF §2 "Main lines first"; RV §5 SL5 | standard / self-review check | |
| CF-12 | A value gradient toward the hero | HO §4 "Light" (lightest on the anchor, darker toward edges) | standard | |
| CF-14 | Make the focal point the tallest shape | KE §6 "Identity symbols and landmarks"; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| CF-16 | Negative space on purpose: calm room, no awkward gaps | RF §2 "No awkward gaps"; RV §5 SL6 | standard / self-review check | |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | design/SKILL §4 M-01, §7 P2; EI §3 (game-camera capture after import); RV §5 IM1 | standard / core principle / self-review check | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | RV §3 "A note names a solution" | step | |
| CR-04 | Answer every note with a concrete visible fix; protect the anchor | RV §3 (keep the identity anchors while answering a note) | step | |
| CR-05 | Give and solve visual notes as paint-overs on a capture | RV §3 "Words are not enough"; HO §6 (ask the art director for a paint-over) | step | |
| CR-06 | Notes are direct and visual; the maker drives; conflicts go up | RV §3 "Conflicting notes" | step | |
| CR-07 | No grand reveals: show early and often, partner crafts first | design/SKILL §3 steps 7-8 (blockout and check-in gates); role work method 5-6; HO §6 | stage | |
| CR-08 | Diagnose by layer; "not happy" may mean "not done" | RV §3 step 1 (sort by layer, read layer order) | step | |
| CR-09 | Fresh eyes: flip the image, change the reviewer | craft/SKILL §7 mirror row; RV §5 SL6; design/SKILL §7 P15 | self-review check | |
| CC-01 | One target experience, signed by every craft | RF §1 "Job in play" (quote the target-experience line) | step | |
| CC-03 | Build for the next craft: ask what they need first | design/SKILL §7 P16; HO §6; role "What you ask for, and when" | core principle / step | |
| CC-04 | The concept leaves room for the next crafts' decisions | role (VFX gets agreed emissive areas); HO §6 (ask VFX which emissive areas and attach points it needs) | step | |
| EX-01 | Larger than life: extend and sharpen what must read | design/SKILL §7 P8; RF §2 "3-4 chunky anchors" | standard / core principle | |
| EX-04 | Emotes and reactions: maximum expression for a two-second read | RF §2 "Faces" (expression faces and reaction props pushed) | standard | |
| EX-05 | A believable base earns the extremes | design/SKILL §7 P8; RF §6 "Believable anatomy" | core principle / standard | |
| EX-09 | Always animate the shoulders and hips | — | — | Animation keying; the modeler's share (clearance at the shoulders for that motion) is under CD-12 (RF §6, RV §5 MO1) |
| EX-10 | Energy flows out to the fingertips; hands matter even when tiny | RF §3 (hands carry the read, value break at wrists); RV §5 VL2-VL3 | standard / self-review check | Finger and hand-pose motion rejected: animation craft |
| GD-01 | Every asset has jobs: clarity first, then feel, then style | design/SKILL §7 P1; RF §1 "Job in play" | core principle | |
| GD-07 | Art and mechanics must promise the same thing | design/SKILL §4 M-15; KE §6 (interactive surface reads its use, openings open); RV §5 GR4 | standard / self-review check | |
| GD-09 | Mechanics and numbers are design constraints for art | RF §1 "Job in play" (role and numbers: high HP reads heavy) | step | |
| GD-16 | Cosmetics never change the gameplay read or cost gameplay | RF §7 "Cosmetics never cost gameplay"; RV §5 VA4 | standard / self-review check | |
| GD-18 | A new character starts from the roster gap | RF §1 "Job in play"; HO §6 (role from the game designer) | step | |
| GD-31 | Art stays inside the blockout's gameplay | KE §6 first row (import the greybox, snap, no collision change without sign-off); RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| LC-01 | Reserve the gameplay colours | RF §4 "Reserved colours stay reserved"; RV §5 CL2; design/SKILL §7 P7 | standard / self-review check / core principle | |
| LC-04 | Few colours with roles: about 60/30/10, after the greys work | RF §1 palette roles, §4; RV §5 CL1 | standard / self-review check | |
| LC-05 | Take new colours from the palette already in the image | RF §4 "Palette after greys" | standard | |
| LC-06 | Put the environment's bounce colour into character shadows | TM §8 (environment colour may tint shadows when the bible asks) | standard | |
| LC-07 | Shift hue for shadows and highlights | RF §4; TM §8; RV §5 CL4 | standard / self-review check | |
| LC-08 | Light and shadow get opposite temperatures | RF §4; TM §8; RV §5 CL4 | standard / self-review check | |
| LC-09 | No flat fills | RF §4; TM §8; RV §5 CL5 | standard / self-review check | |
| LC-10 | One fixed light direction, judged at the game camera | RF §4 (restated for Roblox's live light); BR §6 key light; RV §5 CL3 | standard / stage / self-review check | |
| LC-11 | Block light and shadow first; test lighting options on the rough | BR §6 (lit grey view with the key light at the value gate, on the rough flat-region model; RV §1 value-gate row); TM §7 pass 3 | step | Testing 2-3 lighting variants rejected for the modeler: the key light is the art director's art-bible choice |
| LC-12 | Light leads the eye: the brightest area is the focus | RF §3 "Extremes are small"; RV §5 VL4; HO §4 "Light" | standard / self-review check | |
| LC-13 | Light motivated by the setting | RF §4 (key light from the place's sun) | standard | |
| LC-15 | Rim light separates figures from the background | HO §4 "Light" (rim light on icons when the background is close in value) | standard | |
| LC-17 | Calm the field, pop small saturated accents | RF §3 "Extremes are small"; RV §5 VL4 | standard / self-review check | |
| LC-20 | Effect colour sits next to the caster's colour | HO §2 VFX row (the model's main colours in hex) | step | |
| LC-21 | Test colours where parts overlap | RF §3, §4 "Colour where parts overlap"; RV §5 VL3, CL4 | standard / self-review check | |
| LC-22 | Review with colour in, then rebalance | RV §3 step 4 (a colour change shifts the value balance: re-run the grey view); TM §8 (re-run the grey view after every colour change); RF §4 "Saturation leads like value"; RV §5 CL7 (saturation peak on the focal zone; grey of the colour render still passes VL2, VL4); RCM §2 (channel S) | step / standard / self-review check | |
| LC-23 | Iterate colour globally; colourways are the same object | RF §7 "Colourways"; RV §5 VA5 | standard / self-review check | |
| LC-25 | Match skin temperature across face and body | RF §4; RV §5 CL4 | standard / self-review check | |
| MD-01 | Indicate detail; do not spell it out | RF §5; RV §5 DT1 | standard / self-review check | |
| MD-02 | Budget detail by display size, camera distance and player speed | BU §8; design/SKILL §3 step 6, §4 M-04; RV §5 DT2 | step / standard / self-review check | |
| MD-03 | Finish comes from crisp edges and planes, balanced with soft | RF §5; TM §7 pass 4; craft/SKILL §4 C-05; RV §5 DT3 | standard / self-review check | |
| MD-04 | Block material regions before shading | craft/SKILL §4 C-18; TM §7 pass 1; design/SKILL §3 step 7 | stage / standard | |
| MD-05 | Start texturing from baked AO and curvature; drive variation by rules | TM §7 pass 3 and the recipe-as-data note; craft/SKILL §4 C-26 | stage / standard | |
| MD-06 | Material maps sell the surface; push, then pull back | TM §7 pass 6 | stage | |
| MD-07 | Choose materials and lighting together | TM §7 pass 6, §8 "Judge colour in Studio"; EI §3 | stage / standard | |
| MD-08 | Test a new material on a small patch first | TM §7 (test patch before the full pass) | step | |
| MD-09 | Wear and condition tell the story | RF §5 "Wear tells the story"; TM §7 pass 5; RV §5 DT5; KE §6 story row | standard / self-review check | |
| MD-10 | Controlled imperfection makes it hand-made | design/SKILL §7 P11; RF §5 | standard / core principle | |
| MD-11 | Ornament: one shaped motif, added late, small, with a reason | RF §5; RV §5 DT6 | standard / self-review check | |
| MD-12 | Functional parts and visible support make objects believable | design/SKILL §4 M-05; RF §5; RV §5 DT4 | standard / self-review check | |
| MD-13 | Ground every object: base, blended seams, colour bleed | RF §8; KE §6 grounding row; RV §5 GR1 | standard / self-review check | Colour bleed onto the ground stays with the environment designer (ground paint) |
| MD-14 | Gold stays saturated in shadow | RF §4; RV §5 CL4 | standard / self-review check | |
| MD-15 | Cracks taper; one width looks man-made | RF §5 "Natural damage tapers"; TM §7 pass 5; RV §5 DT8 | standard / self-review check | |
| MD-16 | A few small glints sharpen hard materials | RF §5; TM §7 pass 5; RV §5 DT8 | standard / self-review check | |
| MD-17 | One trim sheet with a normal map can dress a whole environment | KE §6 trim-sheet row; TM §9; RV §5 GR5 (KE §6 checks in the self-review) | standard | |
| PP-01 | Set triangle and texture budgets before building; phones first | design/SKILL §3 step 6; BU §8 | step | |
| PP-02 | Rich form first, then a budgeted game mesh with loops where it bends | craft/SKILL §4 C-17, §3 step 3 | standard / step | |
| PP-03 | Put detail in textures, not polygons | craft/SKILL §4 C-19; BU §8 | standard | |
| PP-04 | Keep texel density consistent across assets | BU §8; TM §9; BR §6 texel-density recipe; RV §5 DT9 | standard / self-review check | |
| PP-05 | Mirror UVs on symmetric parts; unique UVs where story detail goes | craft/SKILL §4 C-20; TM §9 | standard | |
| PP-06 | When geometry changes, re-project; marry texture and geometry last | craft/SKILL §4 C-21; TM §9 | standard | |
| PP-07 | Project the concept onto the model as a starting texture | craft/SKILL §4 C-22; TM §9 | standard | |
| PP-08 | For stylised assets, a low-poly painted workflow keeps changes cheap | craft/SKILL §4 C-23; TM §9 | standard | |
| PP-09 | Keep separable parts separate, then judge them together | craft/SKILL §4 C-24 | standard | |
| PP-10 | Paint across joined meshes so joins disappear | TM §9 "One mesh, one paint layer"; KE §6 grounding row | standard | |
| PP-11 | Clean meshes, clean collision, organised UVs | craft/SKILL §4 C-24 (quads, readable UV layout); design/SKILL §4 M-15; KE §6 | standard | |
| PP-12 | Build to the shared rig: reuse its joints, match it, model what it moves | RF §6 "Model what the rig moves"; RPA §6; RV §5 MO4 | standard / self-review check | |
| PP-13 | Keep the contact points fixed in every variant | RF §6; RPA §6; RV §5 MO5 | standard / self-review check | |
| PP-14 | Design moving parts with room to move | RF §6; RPA §6; RV §5 MO4 | standard / self-review check | |
| PP-15 | Spend expensive features only where they earn it | design/SKILL §3 step 5; RF §6; RV §5 MO3 | step / self-review check | |
| PP-16 | Designs must work in 3D, in the round | RC §2 (side and back build views); RV §5 DT4 (no flat 2D part in four views) | step / self-review check | |
| PP-17 | Explore variants over an in-game mannequin | RF §7 "Variant concepts on a mannequin" | step | |
| PP-18 | Rigs are tested in extreme poses before animation | RPA §6 (the rigger's S4 sweep is the check; the modeler's design-for-motion share) | standard | Rig testing itself is the rigger's (rig-pipeline S4/S5) |
| PP-24 | Kits for repeated layouts, unique shells for bespoke ones; no visible duplicates | KE §6 "No visible duplicates"; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| PP-25 | Reuse first: search the zoo before making new | BU §5 (search the game's library first; name reuse in the hand-back) | step | |
| PP-26 | Environment order: blockout, composition, kit, dressing, mechanics, light | KE §6 first row (art built on the approved greybox) | standard | |
| PP-27 | Block out on a grid; snap the art to the approved blockout | KE §6 first row (import at origin and scale, same snap grid); RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| PP-28 | Automate every repeated step | craft/SKILL §4 C-26 | standard | |
| PP-30 | Fix naming and folders before production | craft/SKILL §4 C-02 (named collections, kept) and role write scope (kept) | standard (kept) | |
| PI-01 | The cheapest stage goes first; expect big changes while it is rough | design/SKILL §3 steps 7-8, §7 P14 | stage / core principle | |
| PI-02 | Gates freeze decisions | design/SKILL §3 (steps 7-8 are gates), §5 rules; craft/SKILL §5 | stage / rule | |
| PI-04 | Block out first, in the engine, and play it before detail | craft/SKILL §3 step 2 (Studio blockout next to the avatar) | stage | |
| PI-05 | Work small early so only big shapes can be judged | RF §2 options (rendered small, judged at phone size) | step | |
| PI-06 | Work in passes over the whole; big things before small | design/SKILL §4 M-02; craft/SKILL §3 step 3, step 6; TM §7 | standard / stage | |
| PI-07 | One named problem per pass; fix the worst first | RV §3 steps 1-2; design/SKILL §7 P15 | step / core principle | |
| PI-09 | Not precious: most attempts fail, so delete, redo and let go | craft/SKILL §4 C-25; RV §3 step 6; design/SKILL §7 P14 | standard | |
| PI-10 | Park a stuck part and come back | RV §3 step 6 (park and revisit) | step | |
| PI-11 | A time box forces the readable choice | RF §1 stop criteria (pass budget) | step | |
| PI-12 | Know when it is done | RV §6; design/SKILL §7 P17 | quality bar / core principle | |
| PI-13 | Finish a concept only as far as the next maker needs | RC §7 (the image is a blueprint; ask only for the views and callouts the build needs, now written in RC §7 item 2) | standard | |
| PI-15 | Decisive marks: few bold decisions, not many small tweaks | craft/SKILL §4 C-25 | standard | |
| RI-01 | Concept work solves a problem; a functional vehicle | role hand-back (clarity: self-review results; cost: triangles vs budget); design/SKILL §7 P1 | step | |
| RI-03 | Know the problem, the constraints and the end before making anything | RF §1; design/SKILL §3 step 1, §7 P12 | step / core principle | |
| RI-05 | Research first; one narrow moodboard with pillars and key features | RF §1 identity anchors (key features); RC §7 (a real reference per material) | step | Moodboards themselves are the art director's and `reference-images` |
| RI-06 | Each theme gets a library: shorthand motifs, iconography | KE §6 theme cues; RF §5 motif | standard | |
| RI-07 | Turn each keyword into visual facts before prompting | — | — | Prompt-writing method belongs to `reference-images` (tagged there), which the modeler loads whenever it writes prompts |
| RI-08 | Reference order: our game first, then the real world | design/SKILL §7 P13 | core principle | |
| RI-09 | When a brief fuses two ideas, reference the overlap | — | — | Concept-stage design (art director, `reference-images`); the modeler builds from an approved image |
| RI-10 | Study the real thing closely | RC §7 (a real-world reference per material); design/SKILL §7 P13 | step | |
| RI-11 | Read the concept's intent and its materials; do not trace its strokes | RC §7 (intent lines, material intent, local colour); design/SKILL §3 step 3 | step / quality bar | |
| RI-12 | Get enough reference; make the missing one | RC §7 (missing view made through `reference-images` or a posed Blender mannequin) | step | |
| RI-13 | Reference sheets include front, side, back and the game-camera view | RC §2 build views; design/SKILL §3 step 2 | step | |
| RI-14 | Learn light placement from painted art | TM §8 "Place light the way the painted anchors do" | standard | |
| RI-16 | Research, explore wide and loose, iterate on one or two | RF §2 options; design/SKILL §7 P13 | step / core principle | |
| RI-17 | Take the big swings at concept stage | RF §2 options (one radical option); RV §5 SL9 | step / self-review check | |
| RI-18 | Each option gets its own hook from a different source | RF §2 options (distinct in black-fill); RV §5 SL9 | step / self-review check | |
| RI-19 | Present options with your pick and the reasons; then iterate | RF §2 options; RV §4, §5 SL9 | step / self-review check | |
| RI-21 | The first output is a warm-up; reject the typical idea | design/SKILL §7 P13 | core principle | |
| RI-22 | Vary one element per option, label them, merge the best two | — | — | Single-element image exploration belongs to `reference-images`; the modeler's options are proportion and silhouette options at the blockout (RF §2) |
| RI-23 | Bring in one unexpected element from outside the genre | — | — | Direction choice owned by the art director and `reference-images`; the modeler's radical blockout option (RI-17) covers its share |
| RI-28 | One message, one symbol, before drawing | RF §5 (one motif at three scales); RV §5 DT6 | standard | |
| RI-30 | Leave a marked placeholder for what is designed later | RC §7 (marked PROPOSAL placeholder, open item) | step | |
| RH-02 | No twinning: offset paired parts for two reads | RF §2 asymmetry; RF §5 no exact repeats; design/SKILL §7 P11; RV §5 SL6, DT5 | standard / self-review check | Timing offsets rejected: animation craft |
| SS-01 | Silhouette first, then light that shows form, detail last | design/SKILL §3 steps 7-8, §4 M-03; RF §2-§3; craft/SKILL §3 step 2 | stage / standard | |
| SS-02 | Judge the silhouette filled solid, small and squinted | RF §2; craft/SKILL §7 black-fill and phone-size rows; RV §5 SL1 | standard / self-review check | |
| SS-03 | Break the silhouette with few broad cuts, not small notches | RF §2; RV §5 SL3 | standard / self-review check | |
| SS-04 | Keep the few identifying elements, make them chunky, cut the rest | RF §1 anchors, §2; RV §5 SL2 | standard / self-review check | |
| SS-05 | Shape language carries meaning | design/SKILL §4 M-06; RF §1 shape language row | standard | |
| SS-06 | One shape vocabulary for the whole game | RF §5; KE §6; RV §5 GR5 (KE §6 checks in the self-review) | standard | |
| SS-07 | Big, medium, small: never two shapes the same size | RF §2 size steps; KE §6; RV §5 SL4 | standard / self-review check | |
| SS-08 | Slopes make direction | RF §2 "Direction"; RV §5 SL5 | standard / self-review check | |
| SS-09 | Find the main top line and bottom line first | RF §2 "Main lines first"; craft/SKILL §3 step 2; RV §5 SL5 | stage / self-review check | |
| SS-10 | Line of action and gesture before detail | RF §2 "Posed models"; HO §4 (signature pose) | standard | |
| SS-12 | Body shape predicts movement | RF §2; RV §5 SL7 | standard / self-review check | |
| SS-13 | Players must track hands, head and feet | RF §3 value breaks at joints; RV §5 VL3 | standard / self-review check | |
| SS-14 | Nothing hangs in front of the shoulders and arms | RF §6; RPA §6; RV §5 MO2 | standard / self-review check | |
| SS-15 | Show the hook shapes at the held moments of motion | RF §6; RPA §6; RV §5 MO6 | standard / self-review check | |
| SS-16 | Break symmetry with one asymmetric element | RF §2; RV §5 SL6 | standard / self-review check | |
| SS-17 | Repeat one motif at several scales | RF §5; RV §5 DT6 | standard / self-review check | |
| SS-18 | Build motifs from a few basic shapes, abstracted | RF §5 (reads in black-fill at mid distance, not a sticker); RV §5 DT6 (shape count, black-fill read, integrated) | standard / self-review check | |
| SS-20 | Backdrop pieces: simple surfaces, elegant gesture | KE §6 "Backdrop gesture"; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| SD-23 | Every floor material is a footstep callout | KE §6 "Materials follow gameplay" (floors match the footstep material) | standard | |
| SI-01 | Style sets the emotional tone: set each lever on purpose | design/SKILL §7 P10; RF §5 "Stylisation level from the art bible" | core principle / standard | |
| SI-02 | Every shape and colour has a job | RV §5 RP2 | self-review check | |
| SI-03 | Theme fit can rule out an otherwise cool idea | RF §2 options (another genre or tone is rejected) | step | |
| SI-04 | Theme cues so a place is not generic | KE §6 "Theme cues"; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| SI-06 | Match the game's look, not your own habit | design/SKILL §7 P10; RC §3 "Style" row; RV §3 ("does not look like our game") | core principle / check | |
| SI-07 | Decide the stylisation level; hint at reality | RF §5 "Stylisation level from the art bible" | standard | |
| SI-08 | A deliberate blend of named sources makes a style | — | — | Style sources are an art-bible decision owned by the art director |
| SI-09 | One palette per group so a roster reads as a team | RF §7 "Group palettes" | standard | |
| SI-10 | Proportions are read against the cast | RF §7; RV §5 VA5 | standard / self-review check | |
| SI-11 | An update keeps the kernel and trims what is dated | RF §7 "Remakes keep the kernel" | step | |
| SI-17 | Brand first, hidden story second | RF §5 (hidden story detail is a second layer); RV §5 DT7 | standard / self-review check | |
| SI-18 | A variant changes the palette; the same character keeps it | RF §7; RV §5 VA3 | standard / self-review check | |
| SI-20 | Premium tiers get separable finishes | RF §7; TM §2 "Hero finish tiers" row; worked example (rarity ladder) | standard / example | |
| VC-01 | Fix a weak read with contrast, not detail | RV §3 step 2 | standard / step | |
| VC-02 | Values first, colour second; grayscale proof at every step | design/SKILL §3 step 8 (value gate); RF §3; TM §7 pass 2; RV §5 VL1 | stage / self-review check | |
| VC-03 | Separate parts by value and shape, not by lines | RF §3; RV §5 VL3 | standard / self-review check | |
| VC-04 | Make one spot the focus by lowering contrast everywhere else | design/SKILL §7 P3; RF §3 (lower body quieter, extremes small) | core principle / standard | |
| VC-05 | Give each screen layer its own value and saturation band | RF §3 band starting values; RV §5 VL5; KE §6 calm backdrop | standard / self-review check | |
| VC-06 | Test every character against every background | RV §5 VL2 (separates from its ground), IM1 (brightest and darkest ground at release) | self-review check | |
| VC-07 | Reserve white, black and the highest contrast for small focal spots | RF §3 "Extremes are small"; RV §5 VL4; TM §8 | standard / self-review check | |
| VC-08 | Head, shoulders and hands carry the character read | RF §3 (restated for the third-person camera); RV §5 VL2; worked example (shopkeeper) | standard / self-review check / example | |
| VC-09 | Form shadows make a still object read as 3D | RF §3 "Form reads without rotating"; TM §7 pass 3; RV §5 VL7 | standard / stage / self-review check | |
| VC-10 | Shade with a clear terminator | RF §3; TM §7 pass 3; BR §6 lit grey view; RV §5 VL7 | standard / self-review check | |
| VC-11 | Paint contact shadows where parts touch | RF §3; TM §8 "Contact shadows"; RV §5 VL7 | standard / self-review check | |
| VC-12 | Shade parts as simple forms | RF §3 "Form reads without rotating"; RV §5 VL8 | standard / self-review check | |
| VC-13 | Big soft shading first, then commit with sharp accents | RF §3; TM §7 pass 4 | standard / stage | |
| VC-14 | Group detail in close values; frame the group | RF §3; RV §5 VL6 | standard / self-review check | |
| VC-15 | Space high-contrast features like letters in a word | RF §3; RV §5 VL6 | standard / self-review check | |
| VC-16 | Balance visual weight on purpose | RF §3; RV §5 VL6 | standard / self-review check | |
| VR-03 | Energy reads as a bright core, a glow and something moving | HO §2 VFX row (shell and ring meshes); TM §8 (glow small) | step | Building the effect itself is the VFX designer's |
| VR-05 | Effects follow a game-wide shape code | TM §8 (a lasting glow reads as an active state) | standard | The effect shape table is the VFX designer's |
| VR-14 | Repeated objects: random rotation and size, no constant spin | KE §6 "No visible duplicates" (pieces read new when rotated, variants) | standard | |
| VR-18 | Know the whole toolbox: meshes with moving textures | HO §2 VFX row (simple meshes with UVs for scrolling textures) | step | |
| VR-25 | Randomise decoration only; lock what carries meaning | RF §5 "Vary only decoration" | standard | |
| VH-01 | Rank what must be seen; environment last | RF §3 bands; KE §6 calm backdrop | standard | |
| VH-03 | Less is more | design/SKILL §7 P6; RF §2 chunky anchors | core principle / standard | |
| VH-04 | Judge noise in motion, with lighting and effects on | RV §5 VL6 and IM1 (noise at phone size on the Studio capture); design/SKILL §7 P2 (motion and busy-scene read handed over, could-not-check list) | self-review check | The in-motion check with effects on belongs to the art director's integrated review; it goes on the modeler's could-not-check list (RV §1) |
| VH-05 | Clump detail in a few places; leave areas of rest | design/SKILL §4 M-04, §7 P6 check; RF §1 detail spots (DT10); RV §5 DT10; RCM §3 (detail-density image at phone size) | standard / step / self-review check | |
| VH-06 | The source of power is the primary read | RF §2; RV §5 SL2 | standard / self-review check | |
| VH-07 | Recognisable in under a second beats unique | RF §2; RV §5 SL8; HO §4 (icon among its family) | standard / self-review check | |
| VH-08 | Silhouette is the first read, the face the second | RF §2 (head and carried items in the outline); HO §4 (face readable at crop) | standard | |
| VH-10 | Size signals importance | RF §2; RV §5 SL8 | standard / self-review check | |
| VH-11 | Review in a fixed order | RV §3 step 1 (read layer order: silhouette, value, colour, material, detail) | step | |
| WT-08 | Held objects show weight by distance from the body | RF §6 "Weight class shows"; HO §2 animator row; RV §5 MO5 | standard / self-review check | The hold pose is the animator's |
| WT-25 | Animate hair as one mass, then offset down the chain | RF §6 (hair bundled into one unit); RPA §6 | standard | The offsets are animation craft |
| WL-01 | Gameplay readability beats beauty; test it in the busiest moment | design/SKILL §7 P1 | core principle | The busiest-moment capture is the art director's and level review |
| WL-02 | Items must be identifiable on the ground, even partly hidden | RF §8; RV §5 GR3 (occlusion render for item types) | standard / self-review check | |
| WL-03 | Every piece says "what I am" and "what you can do here" | KE §6 "Materials follow gameplay" (interactive surface reads its use) | standard | |
| WL-05 | Hazards explain themselves | KE §6 "Hazards explain themselves"; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| WL-12 | Mark objectives on the approach and in the floor | KE §6 (objective floor as its own piece with a border trim) | standard | Marker placement is the environment designer's |
| WL-13 | Head-height cues and directional patterns | KE §6 "Head-height cues"; RV §5 GR5 (KE §6 checks in the self-review) | standard | |
| WL-14 | Flat play spaces; every height change is intentional | KE §6 "Predictable geometry"; RF §8 | standard | |
| WL-15 | Predictable geometry | design/SKILL §4 M-15; KE §6 | standard | |
| WL-17 | In a themed game, the blockout already reads as a place | — | — | Level blockout craft (level design, environment designer); the modeler builds on the approved greybox (GD-31, KE §6) |
| WL-18 | Materials follow gameplay rules | KE §6; RF §8; RV §5 GR4 | standard / self-review check | |
| WL-19 | Floors stay clean enough for the smallest gameplay object | KE §6 (grass cards never over play floors); RF §8 | standard | |
| WL-21 | Scale: a player-sized reference in every blockout and scene | RF §8 "Scale is shown"; RV §5 GR2 | standard / self-review check | |
| WL-22 | Environmental storytelling | KE §6 story row; RF §5 wear; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| WL-23 | Give each zone or team an identity symbol | KE §6 "Identity symbols and landmarks"; RV §5 GR5 (KE §6 checks in the self-review) | standard / check | |
| WL-24 | Build and judge the whole space, not only the hero prop | RF §8 "Judge it in its set"; KE §6 last row; RV §5 GR3 | standard / self-review check | |
| WL-27 | A few upright grass cards give the ground depth | KE §6 "Backdrop gesture" (only a few, at edges) | standard | |
| WL-28 | Work from far away; zoom out every round | design/SKILL §4 M-01 | standard | |
| CD-02 (untagged) | Write the sell list before drawing | RF §1 "Sell list" row; design/SKILL §3 step 1 | step | |
| VH-09 (untagged) | Plan the read order: primary, secondary, tertiary | RF §1 "Read order" row; design/SKILL §7 P3; RV §5 IM2 (the reads come in the read plan's order) | step / core principle / self-review check | |
| CF-18 (untagged) | Camera height states status | HO §4 (eye level for friendly subjects, lower for dominant ones) | standard | |
| CR-10 (untagged) | Keep the right mistakes: follow a happy misread | RV §3 "A happy misread"; RV §5 IM2 (cold read) | step / self-review check | |
| CR-13 (untagged) | Close with an honest recap of your own result | RV §4; RV §5 IM3; role hand-back | step / self-review check | |
| CR-14 (untagged) | Pitch the experience the player will have | RV §4 (describe the model as the player meets it); HO §2 owner row | step | |
| CR-17 (untagged) | Say what each input can prove; end with a could-not-check list | RV §1 last bullet; RV §5 IM3; role hand-back | quality bar / self-review check | |
| PI-14 (untagged) | "It would be cooler" is new scope: log it | RV §6 (follow-ups with a cost) | rule | |
| RI-02 (untagged) | Show options at equal, low finish on a clean, labelled sheet | RF §2 options (equal finish); RV §4 | step | |
| SI-19 (untagged) | A cohesive set, with a documented break for the top tier | RF §7 "Look follows real rank" (top tier breaks only by a recorded decision); worked example (rarity ladder) | standard / example | |
| WL-20 (untagged) | It must read at the lowest graphics setting | RV §5 IM1 (quality level recorded); EI §3 (lowest supported level when the brief names one) | self-review check | |

## b. Universal principles

| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: the model carries role, ownership and threat at a glance | design/SKILL §7 P1 |
| UP-02 | yes: models are judged at the game camera, phone size, real ground | design/SKILL §7 P2 |
| UP-03 | yes: value and saturation spent on the focal zone | design/SKILL §7 P3 |
| UP-04 | yes: blockout and value gates before colour and detail | design/SKILL §7 P4 |
| UP-05 | yes: silhouette and anchors are the model's identity | design/SKILL §7 P5 |
| UP-06 | yes: few shapes, detail spots, indicated masses | design/SKILL §7 P6 |
| UP-07 | yes: reserved colours and gameplay materials on models | design/SKILL §7 P7 |
| UP-08 | no: the modeler owns no timing; its share in timing (moving parts with pivots, attach points the markers use) is under UP-17 (design/SKILL §7 P16) | — |
| UP-09 | yes: hook shapes pushed on a believable base | design/SKILL §7 P8 |
| UP-10 | yes: character card or personality words drive shape and material | design/SKILL §7 P9 |
| UP-11 | yes: anchors over habit; variants keep identity | design/SKILL §7 P10 |
| UP-12 | yes: controlled variation, asymmetry, wear, no flat fills | design/SKILL §7 P11 |
| UP-13 | yes: read plan, budgets and rig sheet before the first vertex | design/SKILL §7 P12 |
| UP-14 | yes: real reference, distinct blockout options, reasoned pick | design/SKILL §7 P13 |
| UP-15 | yes: gates freeze proportions; rebuild instead of patching | design/SKILL §7 P14 |
| UP-16 | yes: notes by layer, worst first, honest weakness | design/SKILL §7 P15 |
| UP-17 | yes: cuts, loops, pivots, attach points, reuse, scripts | design/SKILL §7 P16 |
| UP-18 | yes: written stop criteria and a pass budget | design/SKILL §7 P17 |
| UP-19 | yes (the master's model line, though not tagged modeler): tier look follows real rank | design/SKILL §7 P18 |
| UP-20 | yes: team and tier never on colour alone; grey view check | design/SKILL §7 P19 |

## c. Old book changes

Line numbers are at df13ff4. Additions with no old text (new sections, new rows, new references file) are not listed.

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by / moved / removed | Why |
| --- | --- | --- |
| modeling-design/SKILL.md:3 description | replaced (same triggers kept, adds read plan, silhouette and value) | New core of the book; trimmed to stay at most 400 characters |
| modeling-design/SKILL.md:6 author header | kept + J018 phrase and author tag | Spec rule |
| modeling-design/SKILL.md:8 "how much it may cost" title | sharpened ("and how it must read") | The read is now the core |
| modeling-design/SKILL.md:13 "A model is done only when three things hold" | sharpened (game camera, phone size, real ground, read order) | Library: judge where players meet it; read order |
| modeling-design/SKILL.md:18-21 "Read this file when" rows | sharpened; new row for `read-and-form.md` | New depth file and new sections |
| modeling-design/SKILL.md:28 step 1 asset record | sharpened (read plan) | Problem, sell list and anchors before modelling |
| modeling-design/SKILL.md:29 step 2 reference | sharpened (front, side, back plus game-camera view) | Missing views force guesses |
| modeling-design/SKILL.md:30 step 3 check the reference | sharpened (intent, iconic qualities, gaps, material intent) | The concept is a blueprint |
| modeling-design/SKILL.md:32 step 5 rig pipeline | sharpened (design for motion, costly parts with fallback) | Mass off joints; expensive features earn their place |
| modeling-design/SKILL.md:33 step 6 budget | sharpened (detail budget by display size) | Detail only where the phone view shows it |
| modeling-design/SKILL.md:34 step 7 "Blockout, then approve the big shapes" | replaced by step 7 "Silhouette gate" | Black-fill at the game camera and phone size; options; proportions fixed |
| modeling-design/SKILL.md:35 step 8 "Review with light checks" | moved to step 9; new step 8 value gate | Values before colour; value gate before polish |
| modeling-design/SKILL.md:40 M-01 (evidence "[E] Riot, Valve") | sharpened (phone size, real ground, zoom out); evidence text no longer names a studio | Body rule: no studio names |
| modeling-design/SKILL.md:41 M-02 "Three layers" | replaced by four layers (value structure added) | Value structure is its own layer |
| modeling-design/SKILL.md:42 M-03 "flat-colour or grey silhouette" | sharpened (black-fill and grey value version) | Named measurable views |
| modeling-design/SKILL.md:43 M-04 | sharpened (1-3 detail spots, rest areas) | Clump detail |
| modeling-design/SKILL.md:44 M-05 | sharpened (functional parts) | Functional parts make objects believable |
| modeling-design/SKILL.md:45 M-06 "not from 'round = good, sharp = evil'" | replaced: shape language from the art bible and the subject's character; sharp danger, round friendly, square stable only where the bible's world rules agree | The library shows these meanings read near-universally; the old point that the bible's world rules decide is kept |
| modeling-design/SKILL.md:47 M-08 | sharpened (variants keep anchors, proportions, contact points) | Identity anchors |
| modeling-design/SKILL.md:50 M-11 | sharpened (restore iconic shapes Tripo softened) | 3D softens the concept |
| modeling-design/SKILL.md:54 M-15 | sharpened (simple and predictable) | Predictable geometry |
| modeling-design/SKILL.md:62 "No invented numbers" | sharpened (value bands; starting values are PROPOSAL) | New numbers are starting values |
| modeling-design/SKILL.md:63 "Checks are light" | sharpened (read views are measurements of the one set) | Keeps the owner's light-check rule with the new read checks |
| modeling-design/SKILL.md:64 franchise rule | sharpened (non-sexualised, culture respected) | Young audience; accurate culture |
| modeling-design/SKILL.md:67-71 self-check | sharpened (read plan, gates, self-review, honest weakness) | New stages |
| modeling-design/references/review.md:7 "One review render set per hand-off" | sharpened (front and back game camera, Studio capture) | The third-person camera sees the back; Studio decides the look |
| modeling-design/references/review.md:8 "More images only when a number fails" | sharpened (conditional extras named: options, occlusion, posed proxy) | Keeps the rule explicit for the new checks |
| modeling-design/references/review.md:15 Identity and silhouette row | sharpened (phone size, anchors) | Silhouette at display size |
| modeling-design/references/review.md:22, 24-26 moving parts, materials, budget, collision rows | sharpened (mass across joints; material reads as itself; small features; simple and predictable) | Library standards |
| modeling-design/references/review.md:44 micro-detail rejection row | sharpened (points to DT2) | Now measured |
| modeling-design/references/review.md:54 "Sort the defect" | sharpened (read layer first, fixed order) | Diagnose by layer, big to small |
| modeling-design/references/review.md:55 "Fix the biggest effect first" | sharpened (contrast, not detail) | Fix a weak read with contrast |
| modeling-design/references/review.md:58 "Does not look like our game" | sharpened (the generic image or Tripo look as the usual cause) | Match the game's look, not a habit |
| modeling-design/references/review.md:59 "Re-run every check the fix can break" | sharpened (colour change re-runs the grey view) | Rebalance after colour |
| modeling-design/references/review.md:63 "What the owner sees" | sharpened (phone-size view, options with one recommendation, described as the player meets it, honest recap) | Honest recap, pitch the experience |
| modeling-design/references/reference-check.md:6 asset record fields | sharpened (read plan) | Read plan |
| modeling-design/references/reference-check.md:12 build views row | sharpened (game-camera view, anchor close-ups, material intent) | Views the 3D maker needs |
| modeling-design/references/reference-check.md:34 Style row | sharpened (not the image model's generic default); new rows Real views, Read plan | Generic AI look; real views |
| modeling-design/references/reference-check.md:63 blockout before detail | sharpened (silhouette gate, Studio next to the avatar, proportions fixed after the gate) | Gate |
| modeling-craft/SKILL.md:3 description | replaced (same triggers, adds the gate, texture passes, read checks; "make icon renders" shortened to "icon renders") | At most 400 characters |
| modeling-craft/SKILL.md:6 author header | kept + J018 phrase; `look_check.py` added to tools | Spec rule; new tool use |
| modeling-craft/SKILL.md:11 "When this skill starts" | sharpened (read plan; game-camera capture) | New inputs |
| modeling-craft/SKILL.md:25 step 1 set up | sharpened (game cameras, key light) | Judge at the game camera; one light direction |
| modeling-craft/SKILL.md:26 step 2 blockout | replaced by "Blockout: the silhouette gate" | Measured black-fill and phone-size views; options; Studio avatar |
| modeling-craft/SKILL.md:27 step 3 build | sharpened (passes over the whole; rich form first; restore iconic qualities) | Passes; concept as blueprint |
| modeling-craft/SKILL.md:28 step 4 rig parts | sharpened (no mass across a joint) | Design for motion |
| modeling-craft/SKILL.md:30 step 6 "UVs and textures to the texture plan" | replaced by texture passes with the value gate | Values first; form shading; hue shifts; wear |
| modeling-craft/SKILL.md:31-33 steps 7-9 | sharpened (predictable collision; back game camera and read measurements; game-camera capture) | New checks |
| modeling-craft/SKILL.md:34 step 10 "lesson draft" | sharpened (honest recap and lesson in the hand-back) | See next row |
| modeling-craft/SKILL.md:43 C-05 | sharpened (crisp edges on hard materials, soft on organic) | Finish from planes and edges |
| modeling-craft/SKILL.md:51-53 C-13, C-14, C-15 | sharpened (Studio capture judges the look; read views are measurements; self-review) | New checks |
| modeling-craft/SKILL.md:59 Studio MCP rule | sharpened (captures, restore the camera) | Captures are now routine |
| modeling-craft/SKILL.md:66 "One review render set made" | sharpened (back view, measurements, self-review) | New checks |
| modeling-craft/SKILL.md:68 "Lineage complete; lesson draft in `knowledge/inbox/`" | replaced: lesson in the hand-back; the lead writes the inbox draft | The old line contradicted the role file and `rules/messages.md` (agents do not write to `knowledge/inbox/`); not a library finding, fixed while rebuilding |
| modeling-craft/references/export-import.md:29 "After import, measure" | sharpened (game-camera capture on the real ground, phone size, quality level) | Judge in game |
| modeling-craft/references/handoffs.md:6 hand-back fields | sharpened (self-review, deviations, honest weakness, could-not-check) | Honest recap; what each input can prove |
| modeling-craft/references/handoffs.md:12-17 animator, art director, environment designer, VFX, UI, owner rows | sharpened (weight class; gate views; base for blending; main colours and effect meshes; display-size checks; the player's moment) | Build for the next craft |
| modeling-craft/references/handoffs.md:27 icon render set | sharpened (light, what fills the frame, checks at display size) | Small frames show the anchors |
| modeling-craft/references/tripo-finish.md:29 raw check step 3 | sharpened (list softened iconic qualities) | Concept as blueprint |
| modeling-craft/references/tripo-finish.md:36 finish step 4 | sharpened (restore iconic qualities) | Same |
| roles/modeler.md:12 build comment | kept + J018 phrase | Spec rule |
| roles/modeler.md:14 identity line | sharpened (at the game camera on a phone, right things first) | Read first |
| roles/modeler.md:20-21 skills and overlays | sharpened (what each skill now holds; key light and colour roles from the art bible) | New books |
| roles/modeler.md:30 "Craft practice from Riot's artists ... riot-extracts.md §4" | replaced by "Craft standards live in your own books" | Owner spec: role files point to their own books, not to the J016 card; no studio names in the body |
| roles/modeler.md:33-40 work method | sharpened and reordered (read plan step, silhouette gate, passes with value gate, read measurements, game-camera capture) | New stages |
| roles/modeler.md:43-47 working with other agents | sharpened (environment designer: in-set judging; VFX emissive areas; new "What you ask for, and when") | Ask the next craft first |
| roles/modeler.md:54 hand-back fields | sharpened (read plan, self-review, deviations, honest weakness, could-not-check) | Honest recap; deviations said out loud |

## d. Repair round 1

Review: `reviews/modeler-rev1-reviewer.md` (verdict fix-first). Every keep-list item is unchanged. The region-mask, mask-capture and top-5 % recipes were run on synthetic images (a render on a flat grey background and a capture with sky and ground) with `look_check.py`: the region masks gave the torso and leg medians (0.598 and 0.0074, where boxes had given the background's median), the mask from the backdrop capture made `silhouette`, `value` and `thumb` measure the sky-and-ground capture (it was `invalid-mask` before), and the top-5 % image marked the brightest pixels. Nothing in Studio was run: the Neon backdrop is a probe-first recipe.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) | craft/SKILL §7 new row "Mask capture (for every Studio capture)" (temporary `#FF00FF` Neon backdrop behind and under the model, CastShadow off, `silhouette` on it, its black-fill as `--mask` for `silhouette`, `value`, `thumb`, `palette`; restore; probe once per place; no usable mask means SL1, SL2 and VL2 on the capture are `not verified`); Studio capture row uses it; craft/SKILL §3 step 9; RV §5 IM1; RV §1 hand-off row; design/SKILL §7 P2 check; EI §3; role work method step 8. Proposal: the same recipe as a shared `studio-mcp` probe. |
| F2 (blocking) | craft/SKILL §7 new "Region" row (a region mask = black-fill ∩ a box, one PIL line, then `value --mask` or `palette --mask`; box edges from the projection recipe, or on a Studio capture from `Camera:WorldToViewportPoint`, never by eye; `--box` and `--compare-subjects` are never used on a render); Grey row no longer suggests `--compare-subjects`; joint-step row: sample boxes fully inside each part; RV §5 intro "Regions and units", VL2, VL3, CL5; design/SKILL §7 P3 check; BR §6 projection row gives the box in render pixels. Proposal: `look_check.py` `--mask` with `--box`. |
| F3 (blocking) | RV §5 new lines appended inside their groups (no renumbering): SL10 faces (eye placeholders, face at anchor quality, head and brows at phone size, likeness across model, icon and promo), DT7 accents and story detail, DT8 cracks and glints, DT9 texel density, MO6 hook shapes in key poses, MO7 real-animal source, GR5 every applicable KE §6 Check. Tags fixed: RF §2 Faces (SL10), RF §5 accents (DT7), RF §5 damage (DT8, was DT6), RF §6 anatomy (MO7; attachment DT4), RF §7 same character (SL10); BU §8 check (DT9); TM §7 pass 5 (DT5, DT7, DT8); TM §9 density (DT9); KE §6 intro sends the agent to GR5; BR §6 new texel-density recipe. Proposal: `model_audit.py --texel-density`. |
| F4 (rec.) | Fixed: rows M-17..M-28 deleted from design/SKILL §4 (each lives in §7 and RF; coverage rows repointed). The file is 120 lines and about 23.7 KB; steps (§3), rules (§5) and the self-check (§6) sit inside the first 5,000 tokens, and §7 is kept whole as the owner asked; P12-P19 may still fall outside the compaction window. Not cut further: shortening the principles would drop checks the reviewer kept. |
| F5 (rec.) | Fixed: design/SKILL §7 P2 check now says a still proves one moment; the read in motion and in the busiest scene with effects and UI on is judged by the rigger, animator and art director and goes on the could-not-check list. |
| F6 (rec.) | Fixed: RV §5 intro states the bands in grey-view value with the luminance equivalents (8 % ≈ 0.007, 15 % ≈ 0.020, 85 % ≈ 0.69, 92 % ≈ 0.83); VL5 gives both; VL2's 15-20 % is grey-view value (luminance ratio about 0.6-0.7); RF §3 says the unit; craft/SKILL §7 Grey row points to the conversion. Raised to the lead for the master (VC-05) as a proposal row; art-bible template row asks for both units. |
| F7 (rec.) | Fixed: RV §1 lists the images per stage once (blockout gate; value gate with one lit grey render; texture pass 3 with one flat unlit render; hand-off with the mask capture); conditional extras listed; TM §7 pass 1 check is now numbers plus the value-gate renders, pass 2 "in a Studio capture once one exists", pass 3 on the one flat render; BR §6 closing line, craft/SKILL step 8, design/SKILL §5 rule and the role's step 7 point to RV §1. |
| F8 (rec.) | Fixed: RV §5 "Simple models" line (RP1, SL1-SL3, VL1, VL4, DT2, GR1-GR2, GR5 for kit pieces, IM1-IM3); RF §1 four read-plan rows for simple models; TM §7 simple models may run passes 3-5 as one pass, checks still run; role effort paragraph names the short path. |
| F9 (rec.) | Fixed: craft/SKILL §3 step 6 "→ high-to-low bake when the route has a high source (§4 of that file)". |
| F10 (rec.) | Fixed: KE §6 first row: bespoke shells export at their world position (Set Pivot to Scene Origin off), reusable kit pieces at their snap origin (§2), placed by the environment designer. |
| F11 (rec.) | (a) design/SKILL §7 P13 "2-3 distinct rough options, one of them radical". (b) craft/SKILL §7 new "Top 5 %" row (one PIL line on the luminance image inside the mask; tested); RV §5 VL4 and P3 use it; proposal `--top-percent` for `look_check.py`. (c) BR §6 "`datamodel_type` Client: the server's camera is not the player's". (d) design/SKILL §3 step 4 "Tripo: set the budget (step 6) first". |
| C1 notes (LC-11, PI-13) | LC-11 landing note corrected (the lit grey view is at the value gate, RV §1); PI-13 now written in RC §7 item 2 ("ask only for the views and callouts the build needs"). |

## e. Repair round 2

Review: `reviews/modeler-rev2-reviewer.md` (verdict fix-first). Every keep-list item of rounds 1 and 2 is unchanged in substance; the region-mask command and the mirror line moved word for word from `modeling-craft/SKILL.md` §7 into the new `modeling-craft/references/read-commands.md` §1 and §5 (the §7 rows keep what to measure and the `--box` / `--compare-subjects` ban). Every command line in `read-commands.md` was run on synthetic images on 2026-10-22: region mask (torso 17,000 px, luminance mean 0.79 for sRGB 230), top 5 % L and S (a flat torso at one level plus a 10×10 accent: p95 share 0.625 → marked share 0.0037, the accent alone; a gradient torso without ties: 0.053 marked as before), detail density (detail clumped at the top: busy share 0.29, busy cells at the top; even stripes: busy share 0.0), phone-aspect crop (1000×700 → 1000×450 for 800×360; 315×700 for 360×800). Nothing was run in Studio: the FOV step and the in-hand capture are written probe-first.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) | RV §5 lines appended inside their groups (no renumbering): SL11 archetype nameable from every option's and variant's black-fill (CD-03); VL8 basic-form shading on the lit grey render, ribbon and hair ends darker, the always-seen parts cleanest (VC-12); CL7 saturation peak on the focal zone, grey of the colour render still passes VL2 and VL4 (LC-22; placed in the colour group, not in VL as the review suggested, because it runs on the colour render at the material pass); DT10 detail spots measured with the new detail-density image at phone size, even density fails (VH-05); VA6 theme nameable from the props in one close view, nods on existing anchors, held prop cites the costume revision and shares a motif (CD-19, CD-16); IM4 iconic qualities at least as strong and finish equal or better at hand-off (CD-08). Added to existing lines: DT6 motif from a few basic shapes, reads as its subject in black-fill at mid distance, integrated not a sticker (SS-18); IM2 the reads come in the read plan's order (VH-09). Tags: RF §1 Detail spots (DT10), Read order (IM2), archetype (SL11); RF §3 form (VL7, VL8); RF §4 new "Saturation leads like value" (CL7); RF §5 motif (DT6); RF §7 swap and costume (VA6); RC §7 check points to IM4. design/SKILL §7 P6 check now includes DT10; P3 check includes CL7. Coverage rows VH-05, VH-09, CD-03, CD-08, CD-16, CD-19, VC-12, SS-18, LC-22 repointed. Command: RCM §3; proposal for a `look_check.py` mode. |
| F2 (rec.) | Fixed: RCM §2 (and craft/SKILL §7 Top 5 % row): when the top 5 % would mark more than 10 % of the model (ties on flat regions), only the brightest level is marked; both shares are printed and recorded; the same line takes channel S for saturation (CL7). RV §5 VL4 says so. Tested (see above). |
| F3 (rec.) | Fixed: craft/SKILL §7 Studio capture row: set `workspace.CurrentCamera.FieldOfView` to the game profile's FOV before the capture and restore it after (docs: FieldOfView is the vertical FOV, default 70, `Camera.yaml`); first time in a place, check the FOV took, else record the FOV used; crop the capture and its mask capture to the phone aspect around the look-at point before `thumb` (RCM §4, tested). Proposal: a studio-mcp probe for both. |
| F4 (rec.) | Fixed: design/SKILL §3 step 1 check "(simple models: the four rows of `references/read-and-form.md` §1)"; RV §2 Read plan row: same parenthesis; RV §1 value-gate row: the lit grey render only when VL7 or VL8 runs (not on the simple-model path). |
| F5 (rec.) | Fixed: TM §8 now holds only the how (re-run grey after colour change, hue-shift method, noise-mask mix, AO strength, contact seam, glow mask and its state meaning, painted-anchor light placement, below-waist paint, Studio correction) with a pointer to RF §3-§4 for the standards and starting values; RPA §6 keeps the S3 how and the Check column with a pointer to RF §6; KE §6 rows Grounding, Materials follow gameplay, Predictable geometry and Judge it in the whole set point to RF §8 and keep only the environment-specific additions. design/SKILL §4 M-01..M-04, M-06, M-08 are one line each with "→ §7 Pn" (evidence column kept); §1, §3 and the other §4 rows tightened; §7 principle checks name their review line ids instead of restating the commands. design/SKILL.md 23,665 → 22,579 bytes; the first 20,000 bytes now end at P14 (round 1: inside P11). Not cut further: the remaining principle text is examples and checks the master asks every role to keep, and the full checks live in RV §5. craft/SKILL.md: the long command lines moved to RCM, so the whole file (18,539 bytes) fits the window, including the mask-capture row. |
| F6 (rec.) | Fixed: EI §3 new "Held items" bullet: a test `Tool` (one `Handle`, `Tool.Grip` from the grip pivot; docs `players/tools.md` §Set the handle, §Adjust the grip), equipped in a play-test with `Humanoid:EquipTool` (Server), captured from behind at the default play camera and once from the front (Client, Scriptable camera, restored), each with its mask capture; `screen_capture` time-out in Play: retry once, else the ground capture gives the numbers and the in-hand read is `not verified`; probe-first. RV §5 IM1, RV §1 hand-off row, RV §2a FM36 row, design/SKILL §7 P2 check, craft/SKILL §3 step 9 and §7 Studio capture row, role work method step 8 point to it. Proposal: eval brief 1 check and a studio-mcp probe. |

## f. Repair round 3

Review: `reviews/modeler-rev3-reviewer.md` (verdict fix-first; the lead ran one more focused round for F1-F3). F4 and F5 (recommendations) are not in this round's brief and stay open; F6 was a one-word fix in `proposals/modeler.md`. Test inputs, made in the maker's scratchpad on 2026-10-22: a synthetic test model built headless in Blender 5.1.2 (red torso, near-black brown legs, skin-tone head, a stud clump on the shoulders), its real `review_renders.py` set (1024x1024, flat sRGB 128 grey) and back and front game-camera renders at 1600x720 (12 studs, 6 studs high, FOV 70; model 189 px tall); PIL images: a flat-background render (torso sRGB 210,90,90, boots 25,14,8), a 1600x720 game-camera frame with a 200 px model, captures with sky, noisy ground, a tinted near-black shadow and a dark rock at 1000x700 and 1920x700 with magenta mask captures, an even-stripe model, a 10x20 px model, a magenta-background icon pair, a noisy white-background reference. Every command line in the books was run once on the input its line names; `read-commands.md` blocks were run verbatim from the file.

| Finding | Fixed where | Test input and result |
| --- | --- | --- |
| F1 detail density writes no image, fails on a game-camera frame | RCM §3 rewritten: input is a game-camera render or capture, its black-fill or mask, and the phone viewport height; the line crops to the model's box, box-averages by phone height ÷ frame height (vertical FOV), counts edges only 2 px or more inside the outline, writes `<name>.detail.png` (busy cells black) and prints the model's phone size, busy share and busy rows; part lines named as busy rows that are not detail spots; under about 30 px on the phone: `not verified`. Craft SKILL §7 Detail density row; RV §5 DT10; design SKILL P6 check | Old line on the 1600x720 frame: `cells 0 busy share nan`, no file. New line: game frame 200 px model → phone 38x102, busy rows 15, 25, 54 (head-torso line, shoulder studs, waist), image written; Blender front game frame and the 1024 square game render give the same 38x94 model and busy rows 24-34 (studs) and 62 (waist); back view (no studs) only part lines; even stripes: busy share 0.0 (fails as it should); capture with mask: 19x52, busy rows 14, 24, 53. Found and fixed on the way: PIL's FIND_EDGES copies border pixels (a tight crop made the whole border an edge: 2 px padding added), and the silhouette edge made the thin legs busy (busy rows 49-95 on the back view with LANCZOS and a 1 px shrink; box-average and a 2 px shrink removed it) |
| F2 HSV saturation marks near-black pixels | RCM §2 channel S = chroma (max minus min of R, G, B), mask shrunk 2 px so edge pixels mixed with sky or ground never count, thin-part note; tie rule refined (above 10 %: mark the pixels above the tied level unless under 0.1 % of the model); craft SKILL §7 Top 5 % row "(value or colour)"; RV §5 CL7; CL4 says its "saturation holds" is HSV-style colour against grey at the same darkness (correct there, unlike CL7); design SKILL P3 check | Real Blender back game-camera render: old HSV line marked the legs (rows 392-450), chroma line marks the torso (rows 340-376). Flat render: old line marked the boots (rows 566-962, 34 % of the model), new line torso rows 225-565, no boot pixel. Capture with sky, ground and tinted shadow: shoulder and torso rows 358-394 only. Tie test (flat torso plus 11x11 accent): the accent alone (121 px) |
| F3 phone-aspect crop enlarges the model; model-size WxH shrinks the frame | RCM §4: crop only a capture wider than the phone viewport, width only (FieldOfView is vertical), print whether it cropped; check `thumb`'s `scale` = phone height ÷ capture height. Craft SKILL §7 Phone size row: the whole game-camera frame at the phone viewport only (never the model's own size on a whole frame; not for orthographic or close views), `scale` check; Studio capture row; RV §5 IM1 | 1000x700 capture, 101 px model: old crop → scale 0.8, model 82 px; new line "not cropped", `thumb` scale 0.514, model 53 px (true 52). 1920x700 capture: new line crops to 1556x700, scale 0.514, model 53 px; uncropped it would give 0.417 (the check catches it). Old model-size option on the 1600x720 frame: scale 0.024. Whole frame: 1600x720 → 0.5, 1024 square game render → 0.352, both give the model 94-96 px |
| Same kind of fault, found by running every line: default key tolerance | Craft SKILL §7 intro: `--key-tol 4` on every review-set render call that keys (`silhouette`, `value`, `thumb`, `palette`), open the black-fill once per set; Black-fill, Phone size, Grey and Palette rows; BR §6 clean-keying row; proposal row 22 for the tool | `look_check.py` default `--key-tol 40` on the set's flat 127-128 grey dropped the lit skin-tone head (141,118,99) from every review render's black-fill with verdict `measured`: front bbox 768 px high, with `--key-tol 4` 932 (all eight views checked; head top matches the projection recipe's head box at 263) |
| Same kind: `--compare` against a reference image | Craft SKILL §7 Black-fill row: `--compare <other> --compare-mask <its black-fill>`, the reference keyed alone first; RV §2 identity row | `--compare` keys the other image with the call's tolerance: render (tol 4) vs a noisy white-background reference gave IoU 0.73 with no error; with `--compare-mask` of the reference's own black-fill, 0.93 |
| Same kind: icon checks | HND §4: `--key FF00FF` on a magenta background for `thumb` and `silhouette --compare` | A head-and-upper-body icon touches the frame edge: as written, `thumb` gave `invalid-mask`; with `--key FF00FF`: measured, scale 0.293; the family compare IoU 0.94 |
| F6 (rec.) | `proposals/modeler.md` intro: "Rows 1-4" | n/a |

Lines run with no change needed: RCM §1 region mask (upper and lower masks on the back render from the projection recipe's waist at y 374: 6,661 and 3,550 px, `value --mask` medians 0.076 and 0.0027; on the capture with its mask: 1,404 px, `palette --mask` 8 clusters, CL5 works); RCM §5 mirror (file written); `look_check.py value` (luminance image full frame, also on a capture with `--mask`), `silhouette --keep-holes`, mask-capture `silhouette` on magenta (default tolerance keys it; 102 px model), `contrast --sample` with boxes inside the torso and a leg (ratio 2.37), `palette --roles` (main ΔE 0.0, accent 0.1); BR §4 `model_audit.py` (verdict MEASURED, every check row present) and `review_renders.py --game-cam 12,6,70` (8 views); BR §6 back game-camera recipe at 1600x720 and the projected-size recipe (part boxes match the black-fill; a shoulder stud 2.0 px on the phone, so DT2 flags it); role `context_packet.py packet` (exit 0). Not run: Studio lines (`execute_luau`, `screen_capture`, the Neon mask capture, `WorldToViewportPoint` boxes, the in-hand Tool capture: no Studio in this round; they stay probe-first), the texel-density formula (the test model has no UVs), FBX export (BR §5 already says not yet run).


## Proposal sweep (J018 close)
Close-out sweep by J018 sweeper art-director, modeler · claude-opus-5-5 · high · 2026-10-22. Every row in `proposals/` that names `modeling-design`, `modeling-craft` or the modeler role body (abbreviations as in §c: RF `modeling-design/references/read-and-form.md`, RV `modeling-design/references/review.md`, RPA `modeling-craft/references/rig-parts.md`, HND `modeling-craft/references/handoffs.md`). Rows that only mention the modeler in a recipe or workflow (environment-designer.md:19, game-designer.md:30, character-rigger.md:27, orchestration.md:23) are not against these books.
| proposal file:line | decision (adopted / already in the book / declined) | where or why |
| --- | --- | --- |
| art-director.md:38 | adopted | Band values now come by pointer from the value-bands row of `art-review/references/art-bible.md` §7 (the kit's one copy): RF §3 lower-body bullet and "Characters own a little more range" bullet; RV §5 "Regions and units" keeps only the grey-value to luminance conversions (marked conversions only, as `environment-craft/references/measure-captures.md` §0 does); RV §5 VL2 (lower ÷ upper luminance median against the bible's lower-body line) and VL5. The checks themselves are unchanged. No other copy left (grep for 15-20, 8-92, 15-85: 0 hits in the modeler books). The environment half of the row (light-and-air VB-a) already points to BIB §7. |
| character-rigger.md:22 | adopted | RPA §2 step 1 reads the rig sheet's §C `design_for_motion` findings (each built or answered with a counter-proposal); RPA §3 table: new row "every design-for-motion finding built or answered", input the §C ids against the §D rows and the hand-back; the §3 heading now says the brief's wording wins (was "unchanged"). Matches `rig-pipeline/references/modeler-handoff.md` refs, fixed and checks. |
| character-rigger.md:33 | adopted | RPA §2 step 5 (one `cap_<cut id>` vertex group per cut at weight 1, cap and socket share the name, a socket group only where the child's cap covers it, else `socket n/a: closed parent face` in §D `build`); step 11 and §4 (part files handed back as a `.blend` working copy, because FBX drops vertex groups with no bone); §3 C4 row (6 review views and the back game-camera view) and C5 row (the groups; input the `.blend`'s vertex group list); HND §1 character-rigger row. Matches the brief's `deliver`, C4 and C5. |
| reference-images.md:24 | adopted | role body, Reference images line (`.agents/roles/modeler.md:28`): "`reference-images` §4 steps 1-3 (rounds R0-R3) and "Who generates"". |

## Master follow (J018 close)
By J018 master follower art-director, modeler · claude-opus-5-5 · high · 2026-10-22. Source: `library-fixes.md` §2, every row that names `modeling-design` (P7 and P11 rows) and the checks they name in `modeling-design` and `modeling-craft`. Abbreviations as in §c. Test inputs (scratchpad, 2026-10-22): a Blender 5.1.2 headless test model rendered with `review_renders.py` (1600x400 front view; panels with a flat brown, a one-hue brick texture painted in sRGB, the same bricks with ±3-6° hue patches, a smooth one-hue cylinder with a white studio highlight, a brown panel with a thin red stripe, a red gameplay orb); a 1600x720 synthetic capture with sky and noisy ground (walls under a 0.8-1.1 light gradient: one hue scaled in linear and in sRGB, per-brick hue shifts ±2°, ±4°, ±8°, a near-grey stone, a one-hue wall under a blue light pool) as PNG and JPEG q70; low-chroma walls (chroma 6-17) without and with noise σ 4. Every command was run verbatim from the book file it lives in.
| master change | book row | done where |
| --- | --- | --- |
| UP-07 general check: reserved-hue share by colour distance, not palette clusters | design SKILL §7 P7 | check rewritten: pixels within the bible's colour distance of each reserved swatch as rendered, on the colour render with gameplay parts excluded, count zero; palette clusters named as unable to show it |
| UP-07 | RV §5 CL2 | the measure added (colour render front and back, gameplay parts excluded, 0 px or the owner's number, marked image when not 0) |
| UP-07 | RV §2 Light and colour row; KE §6 Backdrop pieces row | RV row names the reserved-hue and hue-spread rows of craft §7 (palette only for the roles); KE row: CL2 on the colour render, the place's share is the art director's environment-only check (a capture with a character in front would count the character) |
| UP-07 (the measure) | craft SKILL §7 new Reserved hue row; Palette row read column; RCM new §6 | one copy of the command stays in `art-review/references/look-check.md` §5 line 4; RCM §6 holds the model inputs (as-rendered swatch sampled on the gameplay part's camera-facing face, quoted in a shell; the exclusion box; read `px`) and the false readings |
| UP-12 general check: chromaticity spread over small blocks, not cluster count | design SKILL §7 P11 | CL5 rewritten: hue spread over small blocks on each material's lit face above the flat limit; a one-hue value texture fails as monochrome |
| UP-12 | RV §5 CL5 | measure replaced (`palette --mask` cluster count → craft §7 Hue spread row, a screening aid); near-neutral materials judged by eye and recorded |
| UP-12 (the measure) | craft SKILL §7 new Hue spread row; Region row and RCM §1 (the "`palette --mask` for CL5" pointer removed); RCM §6 | one copy of the command in `look-check.md` §5 line 10; RCM §6: render input, box rules (16 px minimum, no part edge), model test numbers |
| UP-03 | design SKILL §7 P3 | agrees, no change |

Runs (V3, verbatim from the files):
| Command | Input | Result | Wrong with no error (recorded in RCM §6) |
| --- | --- | --- | --- |
| RCM §1 region mask (same code as `look-check.md` §5 line 1, run from there) | the render's black-fill (`silhouette --key-tol 4`) | orb mask, orb + panel mask, a too-tight orb mask written | — |
| `contrast --sample` (RCM §6) | orb camera-facing face; orb shadow side | `#883131`; `#701314` | an unquoted `#` in bash ends the command line (IndexError, not silent) |
| `look-check.md` §5 line 4 (verbatim) | render, swatch `#883131`, orb excluded / orb + panel excluded | 1,827 px (the stripe) / 0 px | — |
| line 4 | swatch authored `#c82828`, orb excluded | 0 px with the stripe present | false pass: authored hex on a lit render |
| line 4 | swatch from the shadow side `#701314`, orb excluded | 0 px with the stripe present | false pass: swatch sampled off the lit face |
| line 4 | swatch `#8c3b3b`, exclusion box smaller than the orb | 5,666 px | false fail: the uncovered rim; the marked image shows it |
| `look-check.md` §5 line 10 (verbatim) | render boxes | flat 0.28; one-hue sRGB bricks 0.65 (monochrome: fails); hue patches 7.34; smooth one-hue cylinder with a white highlight 1.4; panel + stripe 9.81 | two materials in one box: false pass |
| environment `hue_spread` (comparison only) | same boxes | 0.74 / 19.73 / 27.19 / 36.25 / 66.93 | white highlight and sRGB-painted texture read as hue: proposal row in `proposals/art-director.md` |
