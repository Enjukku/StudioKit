---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2)
supersedes: []
---
> Author: J018 maker reference-images · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: reference-images

Books rebuilt (old state: git `df13ff4`): `.agents/skills/reference-images/SKILL.md` (sections 1-7 kept by number, §8 "Core principles for this craft" appended), `references/prompt-patterns.md` (sections kept, §8 appended), new `references/rounds.md` and `references/self-review.md`. No role file exists for this shared skill: the roles that load it point to §4 steps 1-3 and "Who generates", which keep their numbers and meaning. Line count: SKILL.md 128 (after repair round 1: §6 starts at about 18.2 KB, §8 at 20.3 KB; §1 asks to re-read §4, §6, §7 and §8 after a compaction). Description 392 characters.

Legend for "landed in": SK = `SKILL.md` (§ sections, I-nn craft core rows, §8 Pn principles, numbered as the master UP-nn), RD = `references/rounds.md`, PP = `references/prompt-patterns.md`, SR = `references/self-review.md` (lines BR, RO, PK, FN, PO, HO; commands C1-C11 in §4).

Every one of the 176 findings tagged `reference-images` in `matrix.md` has a row (168 landed, 8 rejected with a reason); 14 untagged findings used are at the end (marked "untagged").

## a. Findings
| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| CD-01 | Know the character, then decide on their behalf | RD §1 Card; SK §8 P10; SR BR3 | step / core principle / self-review check | |
| CD-02 | Write the sell list before drawing | SK §4 step 1; RD §1 Sell list; SR BR2, PK1 | step / self-review check | |
| CD-03 | Understand the archetype before evolving it | RD §1 Card (archetype traits kept in every option); SR RO4 (archetype named from the black-fill) | standard / self-review check | |
| CD-04 | Variants hold the identity anchors and change the rest | PP §5 variant row; RD §1 Variant line; SK §8 P11; SR FN4 | standard / core principle / self-review check | |
| CD-05 | If a variant drops a silhouette landmark, fill its slot | PP §5 variant row (slot filled by similar mass); SR FN4 | standard / self-review check | |
| CD-06 | Keep the likeness the same in every product | SK I-10 (attach the subject); SR FN4 (same person; the face matches before it is shown) | standard / self-review check | |
| CD-07 | The fantasy must survive every real view | RD §5 final table (game-camera-angle view); SR FN13 | stage / self-review check | |
| CD-08 | The concept is a blueprint: keep its iconic qualities, decide its gaps, exceed it in 3D | SK I-18; RD §5 Stop; SR HO1 (iconic qualities, gaps) | standard / self-review check | |
| CD-10 | Believable anatomy and plausible construction | SR FN3 (attachment visible; could exist as a solid) | self-review check | |
| CD-11 | Invent creatures from real anatomy | RD §2 (a real source per creature body part); SR BR4 | step / self-review check | |
| CD-12 | Design for motion: test extreme poses, keep mass off the joints | PP §5 character row (no drape over shoulders and arms unless paid for); RD §5 final table (rigid or bending, costly parts, for the rigger); SR FN12, HO1 | standard / self-review check (pose tests on the model are the modeler's and rigger's) | |
| CD-13 | Twist the tone within bounds; darker still keeps the appeal | RD §1 Variant line (tone shift and its limit); SR BR6, FN10 | step / self-review check | |
| CD-14 | Keep the cool core, swap one iconic item, justify it by lore | RD §1 Variant line (keep core X, swap item Y for Z because W); PP §5 variant row | step / standard (checked: FN4 anchors present) | |
| CD-16 | Costume first, weapon second | SR BR3 (a held item cites the approved costume and shares a motif) | self-review check | |
| CD-17 | A complex signature item signals a skilled owner | PP §5 prop row (a hero item gets more distinct big parts) | standard (the part count on the mesh is the modeler's check) | |
| CD-18 | Drop inherited parts that do not fit the new fantasy | PP §5 variant row (parts that do not exist in the theme replaced); SR FN4 | standard / self-review check | |
| CD-19 | Tell the theme through small nods on the gear | PP §5 variant row (1-3 small theme nods on existing parts); SR FN4 | standard / self-review check | |
| CD-20 | Small accents carry the personality | RD §1 Card (2-4 small accents); PP §5 character row; SR BR3 | standard / self-review check | |
| CD-21 | Explore costumes on varied poses and body types | RD §3 item 6 (a costume in 2 attitude poses); SR RO6 | stage / self-review check | |
| CD-22 | Put the eyes and face in early | SR FN4 (the face matches before anyone sees the image) | self-review check | |
| CD-23 | Brows, face structure and nose carry identity | PP §5 character row (brow and nose shape from the card); SR FN4 | standard / self-review check | |
| CD-26 | Design a prop or a place as a character | RD §1 Card (props and places get personality words); SK §8 P10 example; SR BR3 | step / core principle / self-review check | |
| CD-28 | Represent ethnicity and culture accurately | SK §6 rule (a real culture represented accurately); RD §2 sensitivity line; SR BR4, FN10 | rule / self-review check | |
| CD-29 | Move a sensitive theme onto a prop motif | SK §6 rule (a theme that could read as cruelty carried by a prop motif); SR FN10 | rule / self-review check | |
| CF-01 | Big to small: composition first, detail and effects last | SK I-15, §4 step 5; SK §8 P4; SR RO4-RO5 | stage / core principle / self-review check | |
| CF-02 | Design and pose for the side the game camera shows | SK §3 game-designer row; SK I-11 (game-camera angle a must-have where the family's lock leaves the camera open; under a three-quarter lock the read is judged at R3); PP §5 concept and option rows; RD §3 item 3; RD §5 final table; SR RO4, FN13 | standard / self-review check | |
| CF-04 | Compose inside the real frame, crop and UI, at final scale | RD §1 Constraints (destination frame); SR FN11 | standard / self-review check | |
| CF-05 | Lock a safe square around the crop, then move anything else | SR FN11 (composed in the destination frame: circle, square, safe area) | self-review check | |
| CF-06 | In a small frame, the identifying parts fill it | SR FN11 (identifying parts fill a small frame; face readable) | self-review check | |
| CF-08 | Shape flow points to the focal point, at every scale | SR FN11 (main lines lead to the focal point) | self-review check | |
| CF-09 | Lines on an object lead somewhere and agree with each other | PP §5 prop row; SR FN5 (props and vehicles: edges and cuts toward 1-2 shared points or parallel to the main line, one line carried across parts) | standard / self-review check | |
| CF-12 | A value gradient toward the hero | PP §5 concept row (the focal point is the lightest area, the rest quieter); SR FN6 | standard / self-review check | |
| CF-15 | Three depth groups: foreground frames, midground carries, background unifies | SR FN11 (concept, thumbnail, storyboard: three planes on the grey, a darker foreground frame, the subject midground, a quieter background; C7 shares); SK §6 rule (gore in any foreground element only as the label allows) | self-review check / rule | |
| CF-16 | Negative space on purpose: calm room, no awkward gaps | SR FN11 (calm room planned) | self-review check | |
| CF-18 | Camera height states status | RD §1 Camera height; SR FN11 | step / self-review check | |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | SK §8 P2; SR RO4, FN13 (real size, game-camera angle); the in-game judgement of the built asset is the builder's and the art director's | core principle / self-review check | |
| CR-02 | Ask a goal question, never "do you like it?" | RD §4 goal question; SK §8 P16; SR PK1 | step / core principle / self-review check | |
| CR-04 | Answer every note with a concrete visible fix; protect the anchor | RD §6 (protect the named anchor); SR PO2 | step / self-review check | |
| CR-05 | Give and solve visual notes as paint-overs on a capture | SK I-17; RD §6; PP §3, §5 paint-over row; RD §8 example B; SR PO1 | standard / step / example / self-review check | |
| CR-07 | No grand reveals: show early and often, partner crafts first | RD §4 (pick sheet shown to the partner craft before R3); SR HO4 | step / self-review check | |
| CR-09 | Fresh eyes: flip the image, change the reviewer | SK §8 P16; SR FN5 (the mirror copy looked at on the pick and each final: nothing lopsided only in the mirror) + §4 C4 | core principle / self-review check | |
| CR-10 | Keep the right mistakes: follow a happy misread | RD §4 (a good accident named); SR PK1 | step / self-review check | |
| CC-03 | Build for the next craft: ask what they need first | SK I-18, §3 rows; RD §5 final table; SK §8 P17; SR HO4 | standard / stage / core principle / self-review check | |
| CC-04 | The concept leaves room for the next crafts' decisions | SK I-18; SK §4 step 7 (intent, never settings); SR HO1 | standard / self-review check | |
| EX-01 | Larger than life: extend and sharpen what must read | SK §8 P9; PP §8 Personality; SR FN5 (pushed features change the outline) | core principle / standard / self-review check | |
| EX-02 | Make a pose specific by layering adjectives, then pull back if too far | PP §8 Personality (adjectives turned into pose changes, pulled back); SR FN12 | standard / self-review check | |
| GD-16 | Cosmetics never change the gameplay read or cost gameplay | PP §5 variant row; SR FN14 | standard / self-review check | |
| GD-18 | A new character starts from the roster gap | RD §1 Card (role from the game designer: what the roster lacks); SR BR3 | step / self-review check | |
| LC-01 | Reserve the gameplay colours; keep them, and fast motion, out of decoration | SK §8 P7; SR FN7 + §4 C10 (reserved hue on scene images) | core principle / self-review check | |
| LC-03 | Colour sets the mood; recolour every reused layer to it | PP §3 (colourways as edits); SR FN7 | standard / self-review check | |
| LC-04 | Few colours with roles: about 60 / 30 / 10, after the greys work | SR FN7 (role shares from C8, clusters summed by hue family, main > support > accent near the bible's split, starting value 60/30/10; a scene may lean on one dominant hue) | self-review check | |
| LC-05 | Take new colours from the palette already in the image | SR FN7 + §4 C8 (palette --roles) | self-review check | |
| LC-06 | Put the environment's bounce colour into character shadows | | | a lighting rule the WORLD STYLE LOCK carries (art director, `art-review` art-bible.md); prompts never restate style (I-01); checked on game captures (art-review CL16) |
| LC-07 | Shift hue for shadows and highlights; do not just add black or white | SK §8 P12; SR FN7 (shadows shift hue: the lock asks, the image is checked) | core principle / self-review check | |
| LC-08 | Light and shadow get opposite temperatures | SR FN8 (light and shadow temperatures as the lock states) | self-review check | |
| LC-09 | No flat fills: small hue and value shifts inside a material | SR FN7 (no flat single-swatch material) | self-review check | |
| LC-10 | One fixed light direction for the whole game, judged at the game camera | SK §3 art-director row; SK I-11 (light direction from the lock); SR FN8 | standard / self-review check | |
| LC-11 | Block light and shadow first; test lighting options on the rough | RD §5 Iterate (2-3 light set-ups of the pick as edits, compared in grey); PP §3 | stage / standard (checked: PK3 grey re-check) | |
| LC-13 | Light motivated by the setting | SR FN8 (every light has a source) | self-review check | |
| LC-20 | Effect colour sits next to the caster's colour | PP §5 vfx row (caster attached); SR FN7 | standard / self-review check | |
| LC-21 | Test colours where parts overlap | SR FN6 (overlapping same-colour parts keep a value step) | self-review check | |
| LC-22 | Review with colour in, then rebalance | SR FN11 (saturation peaks at the focal point; no background element the most saturated; read order on the grey), PK3 (colourways re-checked in grey), FN6 | self-review check | |
| LC-23 | Iterate colour globally; colourways are the same object | RD §5 Iterate (2-3 colourways as edits); PP §3; SR PK3 | stage / self-review check | |
| MD-01 | Indicate detail; do not spell it out | SK §8 P6; PP §8 Detail; SR FN9 | core principle / standard / self-review check | |
| MD-02 | Budget detail by display size, camera distance and player speed | RD §1 Constraints (display size); SR FN9 (nothing asked for that vanishes at real size) | step / self-review check | |
| MD-03 | Finish comes from crisp edges and planes, balanced with soft | SR FN9 (edges crisp on hard materials and key planes, soft on organic ones; no zone all hard or all soft; no muddy overworked zone) | self-review check | |
| MD-04 | Block material regions before shading | SK §3 modeler row; RD §5 final table (material-ID version); PP §5 material-ID row | stage / standard (checked: FN12, HO4 with the modeler) | |
| MD-08 | Test a new material on a small patch first | RD §5 (a new material that carries the look gets one swatch approved first); SR FN9 (the swatch approved before this image) | stage / self-review check | |
| MD-09 | Wear and condition tell the story | RD §1 Story facts; PP §8 Use and age; SR FN9 | standard / self-review check | |
| MD-10 | Controlled imperfection makes it hand-made | SK §8 P12; SR FN9 (no uniform glossy finish) | core principle / self-review check | |
| MD-11 | Ornament: one shaped motif, added late, small, with a reason | PP §5 prop row (one motif from few bold shapes); SR FN9 (ornament one shaped motif) | standard / self-review check | |
| MD-12 | Functional parts and visible support make objects believable | PP §5 prop row (functional parts; how attached or held); SR FN3 | standard / self-review check | |
| MD-14 | Gold stays saturated in shadow | SR FN7 (gold stays saturated in shadow) | self-review check | |
| PP-07 | Project the concept onto the model as a starting texture | | | the projection is the modeler's Blender step (`modeling-craft`); our part, views from the angles the modeler projects from, is RD §5 |
| PP-09 | Keep separable parts separate, then judge them together | | | mesh and file structure for the modeler; a generated image is flat (we give the material-ID version and separate views instead, MD-04, RI-13) |
| PP-12 | Build to the shared rig: reuse its joints, match it, model what it moves | SK §3 rigger row; RD §5 final table (rigid or bending, costly parts); SR FN12, HO1 | standard / self-review check | |
| PP-15 | Spend expensive features only where they earn it | RD §5 final table (costly parts with the reason each earns its cost); SR HO1 | stage / self-review check | |
| PP-16 | Designs must work in 3D, in the round | RD §5 (front, side, back views); SR FN3 (views agree, could exist as solids) | stage / self-review check | |
| PP-17 | Explore variants over an in-game mannequin | SK §3 modeler row; PP §5 mannequin variant row; SR FN14 (footprint against the base, C5) | standard / self-review check | |
| PP-31 | Make final images at their final resolution | SK I-15 (finals at final size, never upscaled); RD §5; SR FN11 | standard / self-review check | |
| PI-01 | The cheapest stage goes first; expect big changes while it is rough | SK §4 rounds table; SK §8 P15; SR RO1 | stage / core principle / self-review check | |
| PI-02 | Gates freeze decisions: rough, approved direction, materials, polish | RD §4 (after the pick the big shapes are frozen); SR PK2 (final vs pick IoU, C5) | standard / self-review check | |
| PI-03 | Closing doors: from broad to narrow, never reopen | RD §4 (closed-doors list); SR PK2 | step / self-review check | |
| PI-05 | Work small early so only big shapes can be judged | SK I-15 (roughs judged at real size: the image model cannot draw small, so we view small); SR RO4 | standard / self-review check | |
| PI-09 | Not precious: most attempts fail, so delete, redo and let go | SK §8 P15; RD §3 (roughs disposable) | core principle / standard (checked: PK1 options tried, why the pick won) | |
| PI-13 | Finish a concept only as far as the next maker needs | SK I-18; RD §5 Stop; SR HO4 | standard / self-review check | |
| PI-15 | Decisive marks: few bold decisions, not many small tweaks | SR FN9 (no muddy overworked zone) | self-review check (bold, clean shape words are style: they live in the lock) | |
| RI-01 | Concept work solves a problem; it is a functional vehicle, not a nice picture | SK §4 step 1 (problem); RD §1 Problem (every caption repeats it); SR BR1 | step / self-review check | |
| RI-02 | Show options at equal, low finish on a clean, labelled sheet | SK I-16; RD §3 item 3, §4; SR RO3, PK1 | standard / self-review check | |
| RI-03 | Know the problem, the constraints and the end before making anything | SK §4 step 1; SK §8 P13; RD §1; SR BR1 | step / core principle / self-review check | |
| RI-04 | In marketing art, the launched thing is the hero | SR BR2 (for marketing art the launched thing is the read-first part); the marketing route is `marketing-craft` | self-review check | |
| RI-05 | Research first; one narrow moodboard with pillars and key features | RD §2 (one narrow direction, pillars, key features, sensitivity line); SR BR4 | step / self-review check | |
| RI-06 | Each theme gets a library: shorthand motifs, iconography, a name and a logo | RD §2 (a new theme proposes its library to the art director); SR BR4 | step / self-review check | |
| RI-07 | Turn each keyword into visual facts before prompting | RD §2 keyword table; PP §8 A keyword; SR BR5 | step / standard / self-review check | |
| RI-08 | Reference order: our game first, then the real world, then mix; take ideas, never copy | RD §2 (two halves; ideas, never a design); SK I-07; SR BR4, FN10 | step / standard / self-review check | |
| RI-09 | When a brief fuses two ideas, reference the overlap | RD §2 (fusions: reference the overlap); SR BR4 | step / self-review check | |
| RI-10 | Study the real thing closely for the details invention misses | RD §2 (one observed property per real entry); SR BR4 | step / self-review check | |
| RI-11 | Read the concept's intent and its materials; do not trace its strokes | RD §5 final table (material intent per region with its local colour); SR HO1 | stage / self-review check | |
| RI-12 | Get enough reference; make the missing one | RD §2 (a missing reference is made, not guessed); SR BR4 | step / self-review check | |
| RI-13 | Reference sheets include front, side, back and the game-camera view | SK I-04, §3 modeler row; RD §5 final table; PP §5 view row; SR FN12 | standard / stage / self-review check | |
| RI-14 | Learn light placement from painted art | RD §2 (a light question may take painted key art); SR BR4 | step / self-review check | |
| RI-15 | Learn by recreating work you love, then twist it | RD §2 (UI or motion style: a structural study of 2-3 references, structure only); SR FN10 (no copied reference) | step / self-review check | |
| RI-16 | Research, explore wide and loose, iterate on one or two, finish only what the next maker needs | SK §4 rounds; RD §3-§5 (wide in text hooks, few images, iterate on the pick); SR RO1, PK3 | stage / self-review check | |
| RI-17 | Take the big swings at concept stage | SK I-14 (one radical); RD §3 item 2; SR RO1 | standard / self-review check | |
| RI-18 | Each option gets its own hook from a different source | SK I-14; RD §3 item 2 (hook sources); PP §5 option row; SR RO1-RO2 | standard / self-review check | |
| RI-19 | Present options with your pick and the reasons; then iterate | SK I-16; RD §4; SR PK1 | standard / step / self-review check | |
| RI-20 | For the final pick, compare four or five strong small options and choose the clearest | RD §3 item 2 (6-12 hooks in text, the 3-5 strongest generated and compared on one sheet); SR RO1, PK1 | stage / self-review check | |
| RI-21 | The first output is a warm-up; reject the typical idea | SK I-14; RD §3 item 1; PP §5 option row; SR RO1 | standard / step / self-review check | |
| RI-22 | Vary one element per option, label them, merge the best two | RD §5 Iterate (one named element; merges stated); PP §3; SR PK3 | stage / self-review check | |
| RI-23 | Bring in one unexpected element from outside the genre | RD §1 Keep / try; RD §2 outside-games source; PP §8 The unexpected element; SR BR4, BR6 | step / self-review check | |
| RI-24 | Act it out: agents write the performance beat by beat | PP §5 pose and vfx rows (the moment and what the weight does); RD §5 final table (animator and vfx notes); SR FN12 | standard / self-review check (beat sheets are the animator's and film director's) | |
| RI-25 | Pose to pose from motion reference | RD §2 (motion reference for key poses); SR BR4 | step / self-review check | |
| RI-26 | The same key poses can tell different stories: try two | SK §3 animator row; RD §3 item 6 (2-3 readings of the same moment); RD §8 example C; SR RO6 | stage / example / self-review check | |
| RI-27 | Design a variant through a narrative lens | RD §1 Variant line (the variant's short story); SR BR3 | step / self-review check | |
| RI-28 | One message, one symbol, before drawing | RD §1 Message and symbol; SR FN11 (the symbol as a one-colour shape reads at 150x150, C9) | step / self-review check | |
| RI-29 | Find the hook that makes the subject compelling | SK §4 step 1, RD §1 (hook line); SR BR2, PK1 | step / self-review check | |
| RI-30 | Leave a marked placeholder for what is designed later | SK I-18; RD §5 Stop (placeholders PROPOSAL, open items); SR HO1 | standard / self-review check | |
| RH-02 | No twinning: offset paired parts for two reads | PP §5 pose row (paired limbs doing different things); SR FN12 | standard / self-review check | |
| SS-01 | Silhouette first, then light that shows form, detail last | SK I-15; SR RO4 (C1 black-fill before colour) | standard / self-review check | |
| SS-02 | Judge the silhouette filled solid, small and squinted | SR RO4, FN5; §4 C1-C2 | self-review check | |
| SS-03 | Break the silhouette with few broad cuts, not small notches | SR FN5 (cuts broad, no tiny notches) | self-review check | |
| SS-04 | Keep the few identifying elements, make them chunky, cut the rest | RD §1 Card (3-4 identifying elements); PP §5 character row; SK §8 P5; SR FN5 | step / standard / core principle / self-review check | |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | SK §8 P5; SR RO4 (mood named from the black-fill) | core principle / self-review check | |
| SS-06 | One shape vocabulary for the whole game, down to the small shapes | SR FN10 (shapes from the bible's vocabulary) | self-review check | |
| SS-07 | Big, medium, small: never two shapes the same size | SR FN5 (sibling shapes in clear size steps) | self-review check | |
| SS-09 | Find the main top line and bottom line first | PP §5 prop row (one clear top and bottom profile line); SR FN5 (props and vehicles: one continuous top line with a bottom line that echoes it) | standard / self-review check | |
| SS-10 | Line of action and gesture before detail | PP §5 pose row (one clear line of action); SK §8 P8; SR FN12 | standard / core principle / self-review check | |
| SS-11 | Give the jump apex a pose: legs tucked into a V | PP §5 pose row (jump apex with the legs tucked); SR FN12 (a jump apex tucks the legs into a V, toes pointed) | standard / self-review check | |
| SS-12 | Body shape predicts movement | RD §1 Card (how it moves); SR RO4 (how it would move, from the black-fill) | step / self-review check | |
| SS-13 | Players must track hands, head and feet | SR FN6 (extremities separate at the joints) | self-review check | |
| SS-14 | Nothing hangs in front of the shoulders and arms | PP §5 character row; SR FN12 | standard / self-review check | |
| SS-15 | Show the hook shapes at the held moments of motion | PP §5 pose row (hook shape facing the camera); SR FN12 | standard / self-review check | |
| SS-16 | Break symmetry with one asymmetric element | SK §8 P12; SR FN5 (the asymmetric element named and visible at real size, looked at; C4 mirror IoU only on front or side views) | core principle / self-review check | |
| SS-17 | Repeat one motif at several scales | PP §5 prop row (one costume motif at big, medium and small scale); SR FN9 | standard / self-review check | |
| SS-18 | Build motifs from a few basic shapes, abstracted, never a 1:1 copy | PP §5 prop row (built from a few bold basic shapes); SR FN9 | standard / self-review check | |
| SS-20 | Backdrop pieces: simple surfaces, elegant gesture | PP §5 environment row (backdrop pieces: simple shapes, one gesture); SR FN9 | standard / self-review check | |
| SD-29 | Sources by texture, not by name: many takes, some odd ones | PP §8 A material (by texture, not only by name); RD §3 item 2 (one atypical source); SR RO1 | standard / self-review check | |
| SI-01 | Style sets the emotional tone: set each lever on purpose | SR FN10 (lock levers kept); the levers live in the bible (art director) | self-review check | |
| SI-02 | Every shape and colour has a job in conveying the idea | SR FN9 (no shape without a job) | self-review check | |
| SI-03 | Theme fit can rule out an otherwise cool idea | RD §1 Card and keep lists; SR FN10 (tone words hold) | step / self-review check | |
| SI-04 | Theme cues so a place is not generic | PP §5 environment row (2-3 theme cues); SR FN10 | standard / self-review check | |
| SI-06 | Match the game's look, not your own habit | SK I-02 (the model's generic default is a fault); SR FN10 | standard / self-review check | |
| SI-07 | Decide the stylisation level; hint at reality, do not copy it | SR FN10 (lock clauses, the stylisation level among them) | self-review check | |
| SI-08 | A deliberate blend of named sources makes a style | | | the named source blend of a style is written in the art bible by the art director (`art-review` art-bible.md); prompts never restate style (I-01) |
| SI-09 | One palette per group so a roster reads as a team | SR FN7 (palette roles incl. faction swatches, C8) | self-review check | |
| SI-10 | Proportions are read against the cast | SR FN4 (proportions against the cast in a lineup) | self-review check | |
| SI-11 | An update keeps the kernel and trims what is dated | RD §1 Variant line (loved traits kept, dated ones trimmed); SR FN4 | step / self-review check | |
| SI-17 | Brand first, hidden story second | RD §1 Story facts (the one-glance read separate from a hidden detail); SR FN9 | step / self-review check | |
| SI-18 | A variant changes the palette; the same character in a new scene keeps it | RD §1 Variant line (new version or the same character); SR FN7 | step / self-review check | |
| UI-07 | A core thematic first, then explicit style rules | SK §3 ui-ux row (the UI LOCK carries the thematic line); SR FN10 | standard / self-review check | |
| VC-02 | Values first, colour second; keep a grayscale proof at every step | SK I-15; SR RO5, FN6, PK3 | standard / self-review check | |
| VC-03 | Separate parts by value and shape, not by lines | SR FN6 (parts separate by value, not outlines) | self-review check | |
| VC-04 | Make one spot the focus by lowering contrast everywhere else | PP §5 concept row (the rest quieter); SR FN6 | standard / self-review check | |
| VC-05 | Give each screen layer its own value and saturation band | | | layer bands are measured on game captures (art-review K19, RD3); a generated concept is a target, not a capture; the bands reach images through the lock |
| VC-07 | Reserve white, black and the highest contrast for small focal spots | SR FN6 (pure white and black only on small accents) | self-review check | |
| VC-08 | Head, shoulders and hands carry the character read; quiet the lower body | PP §5 character row; SR FN6 (head, shoulders, hands carry the most contrast; region masks per art-review look-check §5 line 1, run on a flat-ground sample) | standard / self-review check | |
| VC-09 | Form shadows make a still object read as 3D | SR FN9 (still objects read as 3D in grey) | self-review check | |
| VC-12 | Shade parts as simple forms (cylinder, sphere, box, ribbon) | | | a hand-painting technique for texture passes (modeler); generated images have no painting passes; the 3D read is checked under FN9 |
| VC-13 | Big soft shading first, then commit with sharp, high-contrast accents | | | a painting order for texture passes (modeler); a generated image is made in one pass |
| VC-14 | Group detail in close values; frame the group with the strongest colour | SR FN6 (the detail materials of one part in close values inside a contrasting frame; looked at on the C3 grey) | self-review check | |
| VR-02 | Rank every effect's layers: primary, secondary, tertiary | PP §5 vfx row (core brightest, theme layer weaker, a few small bits); RD §5 final table; SR FN12 | standard / self-review check | |
| VR-03 | Energy reads as a bright core, a glow and something moving | PP §5 vfx row; SR FN12 (the core is the brightest) | standard / self-review check | |
| VR-05 | Effects follow a game-wide shape code | PP §5 vfx row (the bible's effect shape table); SK §8 P7; SR FN10 | standard / core principle / self-review check | |
| VR-12 | A glow texture is a soft dot with small irregularities | PP §5 glow draft row (only where a lock allows; most glow dots are scripted in `vfx-craft`); SR FN12 | standard / self-review check | |
| VH-03 | Less is more: the fewest shapes and colours that give the strongest read | SK I-11; SK §8 P6; SR FN9 | standard / core principle / self-review check | |
| VH-04 | Judge noise in motion, with lighting and effects on | | | noise in motion needs moving game captures with lighting and effects (art-review RD14); a still reference cannot show it |
| VH-05 | Clump detail in a few places; leave areas of rest | PP §8 Detail; SK §8 P6; SR FN9 | standard / core principle / self-review check | |
| VH-06 | The source of power is the primary read | RD §1 Read first (the source of power); SR BR2, FN6 | step / self-review check | |
| VH-07 | Recognisable in under a second beats unique | SK §8 P1; SR RO4, PK1 (the option named correctly at a glance) | core principle / self-review check | |
| VH-08 | Silhouette is the first read, the face the second | SR FN5, FN11 (silhouette first, the face readable at crop size) | self-review check | |
| VH-09 | Plan the read order: primary, secondary, tertiary | SR FN11 (the read order primary, secondary, tertiary holds on the grey at real size; main lines lead to the focal point) | self-review check | |
| WT-07 | Centre of gravity over the feet, unless off-balance is the point | PP §5 pose row (balance over the feet unless off-balance is the point); RD §8 example C; SR FN12 | standard / example / self-review check | |
| WT-08 | Held objects show weight by distance from the body | PP §5 pose row; PP §8 Size and weight; SK §8 P9 example; SR FN12 | standard / core principle / self-review check | |
| WL-21 | Scale: a player-sized reference in every blockout and scene | PP §5 concept and environment rows (player-sized figure); SR FN12 | standard / self-review check | |
| WL-22 | Environmental storytelling: someone lives here, time has passed | RD §1 Story facts; PP §5 environment row; PP §8 Use and age; SR FN9 | step / standard / self-review check | |
| WL-28 | Work from far away; zoom out every round | SK §1 (you see stills; real size), I-15; SR RO4, FN13 | standard / self-review check | |
| UP-08 | Timing tells cause and effect: tell, build, beat, hit, result | SK §8 P8 (pose sheets, key frames, panels); SR FN12 | core principle (untagged for this role in the master; its picture/2D line applies) | |
| UP-19 | Feedback follows the real outcome | SK §8 P19; SK §6 rule; SR FN15 | core principle / rule / self-review check (untagged) | |
| GD-35 | Paid random reveals are honest | SK §6 rule; SR FN15 (reveal images show the real tier; platform-policy wins) | rule / self-review check (untagged) | |
| CR-17 | Say what each input can prove; end with a could-not-check list | SR §1 (inputs and labels; could-not-check list); SR HO3 | standard / self-review check (untagged) | |
| CR-12 | When every option meets the brief, choose and commit | RD §4 (when every option meets the brief, choose and commit); SR PK1 | step / self-review check (untagged) | |
| CR-13 | Close with an honest recap of your own result | SR HO3 (one honest weakness with a next step) | self-review check (untagged) | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | RD §6 (the problem behind the note); SR PO2 | step / self-review check (untagged) | |
| PI-07 | One named problem per pass; fix the worst first | RD §6 (one change per paint-over, worst first); SR §1 Order | step (untagged) | |
| PI-08 | Find the right number by bracketing | RD §5 Iterate (2-3 light set-ups and colourways compared); SR PK3 | stage / self-review check (untagged) | |
| VH-11 | Review in a fixed order: balance, proportion, weight, then contrast and detail | SR §1 Order (big to small; stop at the first failing layer) | standard (untagged) | |
| RH-05 | Put motion into a still with a few committed flow lines | SK §8 P8 (2-3 flow lines, never blur); SR FN11 | core principle / self-review check (untagged) | |
| EX-04 | Emotes and reactions: maximum expression for a two-second read | PP §5 pose row (emotes pushed to full expression); SR FN12 | standard / self-review check (untagged) | |
| LC-02 | Keep a colour-role table: one hue never means both help and harm | SK §8 P7; SR FN7 (one hue never means help and harm) | core principle / self-review check (untagged) | |
| SS-19 | Design the group silhouette | PP §5 concept row (the group's shape); SR FN11 | standard / self-review check (untagged) | |

## b. Universal principles
All twenty land in SKILL §8 "Core principles for this craft", each stated for image making with an example from our work and the self-review line that checks it. UP-08 and UP-19 do not list this role in the master's "applies to", but each has a picture/2D line that fits our work (pose sheets, key frames, panels; reveal and reward images), so they are stated here; nothing in them contradicts the master.
| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: an image states the read it supports; the option named correctly at a glance wins | SK §8 P1 (BR2, RO4, PK1) |
| UP-02 | yes: every image judged at the size players see it and from the game camera's angle | SK §8 P2 (BR2, RO4, FN5, FN13) |
| UP-03 | yes: 1-2 read-first parts get the strongest value step | SK §8 P3 (RO5, FN6) |
| UP-04 | yes: roughs judged as black-fill and grey before colour; detail after the pick | SK §8 P4 (RO4, RO5); I-14, I-15 |
| UP-05 | yes: 3-4 identifying elements, shape language from the card and the bible | SK §8 P5 (RO4, FN5, FN10) |
| UP-06 | yes: short identity, detail clumped, masses indicated | SK §8 P6 (FN9); I-11 |
| UP-07 | yes: reserved hues never on decoration, the bible's effect shape table | SK §8 P7 (FN7, FN10) |
| UP-08 | yes (untagged in the master): a still implies the moment; pose sheets, key frames and panels in time order | SK §8 P8 (FN12) |
| UP-09 | yes: hook shapes and poses pushed on a believable base | SK §8 P9 (FN3, FN5, FN12) |
| UP-10 | yes: the card first; every element traces to it | SK §8 P10 (BR3, PK1) |
| UP-11 | yes: style from lock and anchors; variants keep identity anchors | SK §8 P11 (FN4, FN10); I-01, I-02 |
| UP-12 | yes: wear and one asymmetric element in the subject; no uniform AI finish; meaning never varied | SK §8 P12 (FN5, FN9) |
| UP-13 | yes: R0 before any prompt | SK §8 P13 (BR1); §4 step 1 |
| UP-14 | yes: board, 6-12 hooks in text (the master's picture/2D count, a starting value), the 3-5 strongest generated beside the warm-up, one radical, reasoned pick. Generated options stay at 3-5 because each image uses the owner's usage limits 3-5 times faster than a text turn and the selection the material asks for happens among the 6-12 hooks; a project may raise it | SK §8 P14 (BR4, RO1-RO3, PK1); RD §3 item 2; SK §4 R1 row |
| UP-15 | yes: roughs disposable; the pick freezes the big shapes; closed doors | SK §8 P15 (PK2, FN4) |
| UP-16 | yes: goal question, paint-overs one change each, mirror and grey, honest weakness | SK §8 P16 (PK1, PO1-PO2, HO3); I-17 |
| UP-17 | yes: ask the next maker; separate views, intent notes, text-free | SK §8 P17 (HO1, HO4, FN12); I-18 |
| UP-18 | yes: budget and stop criteria in the brief; max 2 regenerations | SK §8 P18 (BR7, HO2) |
| UP-19 | yes (untagged in the master): reveal, reward and tier images show the real tier | SK §8 P19 (FN15); §6 rule |
| UP-20 | yes: tiers, teams and states differ in shape as well as hue and read in grey | SK §8 P20 (FN7) |

## c. Old book changes (old text at git `df13ff4`)
Nothing in the old books was shown wrong by the library; every old rule is kept or sharpened. Section numbers and I-ids are unchanged (the old I-ids keep their order; I-14 to I-19 are appended; §8 is appended).
| Old text (file:line at df13ff4) | Kept / sharpened / replaced by / moved / removed | Why |
| --- | --- | --- |
| SKILL.md:3 description | sharpened (rounds, options, paint-overs; when to load kept) | The skill now runs research, rough options and a pick before the final image; 392 characters |
| SKILL.md:6 author line | kept; J018 rebuild clause added | Header rule of the job |
| SKILL.md:11 §1 When this skill starts | kept; paint-over trigger and "You see stills" paragraph added (re-read §4, §7, §8 after compaction) | Real-size judgement; V7 |
| SKILL.md:16-20 §2 table | kept; rows added (rounds.md, self-review.md, exploration and marketing routes) | New reference files |
| SKILL.md:25 game-designer row | sharpened (from the game camera's angle) | CF-02; game-designer proposal |
| SKILL.md:26 art-director row | sharpened (key light and reserved hues in the WORLD STYLE LOCK; style-direction rounds; paint-overs); the old duty "checks that images from all roles look like one game" kept (dropped in round 1, restored in repair round 1) | LC-10, LC-01; art-director proposal |
| SKILL.md:27 modeler row | sharpened (build views as separate images, material-ID version, mannequin variants) | RI-13, MD-04, PP-17; modeler proposal |
| SKILL.md:28 animator row | sharpened ("key poses and silhouettes before keying" → 2-3 key-pose options per signature move, judged as black-fills, then the sheet) | RI-26, SS-10; animator proposal |
| SKILL.md:29 vfx-designer row | sharpened (frames of the picked frame script, the caster attached) | LC-20, VR-02 |
| SKILL.md:30 ui-ux-designer row | sharpened (UI LOCK carries the thematic line) | UI-07; ui-ux-designer proposal |
| SKILL.md:31 marketing row | sharpened (staged route in `marketing-craft`); the `thumb_check.py` pointer moved to self-review C9 and the marketing book | One rule, one place (V6) |
| SKILL.md:32 film-director row | sharpened (colour-strip vignettes on the approved value frame) | VC-02, LC-11; film-director proposal |
| (none) | added rows: character-rigger, environment-designer, any role (paint-over) | Rigger proposal; CR-05 |
| SKILL.md:35 step 1 Brief | sharpened: R0 brief and research (problem, constraints, size players see it, end, sell list, read-first, card, board, keyword table); fields moved to rounds.md §1-§2 | RI-03, CD-02, RI-05, RI-07 |
| SKILL.md:36 step 2 Manifest | kept; round labels and per-round identity rules added | RI-18, RI-22 |
| SKILL.md:37-38 step 3 Check the prompt / Who generates | kept; repo-root path rule, lock-conflict stop, round in `image-prompts.md`, "a rough round and its final are two batches" added | V3 run of `art_refs.py print` |
| SKILL.md:39 step 4 Generate | kept; the `.json` record also names the round | Traceability of rounds |
| SKILL.md:40 step 5 Review | replaced by step 5 with the round's self-review lines (numbers for all, eyes on a few; roughs as black-fill and grey at real size) | SS-01, VC-02, J005-D8 |
| SKILL.md:41 step 6 Approve | sharpened: Pick and approve (the pick sheet, who picked and their words); anchor approval kept | RI-19, CR-02 |
| SKILL.md:42 step 7 Hand over | sharpened (iconic qualities, gaps, placeholders, intent notes, material intent, counts) | CD-08, CC-04, RI-11, RI-30 |
| SKILL.md:44 "Every agent can get ChatGPT images" | kept | Still right |
| SKILL.md:49-51 I-01, I-02, I-03 | kept; I-02 adds "the model's generic glossy default is a fault"; I-03 adds "visible words (textures and shapes, not names alone)" | SI-06; SD-29 |
| SKILL.md:52 I-04 | sharpened: build views are separate single-view images; a view the lock forbids needs a family whose lock allows it | RI-13; V3 print run; template proposal |
| SKILL.md:53 I-05 | sharpened; its list moved to self-review FN1-FN15 (pointer kept) | One place for checks (V6) |
| SKILL.md:54-56 I-06, I-07, I-09 | kept; I-07 adds "take ideas, never a design" | RI-08 |
| SKILL.md:57 I-11 | sharpened: the read-first part is a must-have; the game-camera angle too where the family's lock leaves the camera open, else the read is judged at R3; light direction and reserved hues come from the lock; evidence shortened | CF-02, LC-10; art-director proposal; repair round 1 F1 |
| SKILL.md:58 I-12 | sharpened: a new subject in the settled style keeps the bible's anchors (`none` only for style directions) | SI-06, UP-11 |
| SKILL.md:59 I-13 | changed: R1 and R2 at medium for every family; R3 at high for the listed families (our reading of J009-D17, owner to confirm at G3) | Marketing proposal; proposals file row |
| SKILL.md:60 I-10 | kept; evidence shortened to a pointer to prompt-patterns §1b | The detail lives there |
| SKILL.md:61 I-08 | sharpened (options on one pick sheet with the recommendation) | RI-19 |
| (none) | added I-14 to I-19 | RI-21, RI-18, SS-01, PP-31, RI-02, CR-05, PI-13, CC-04, brief v3 V14 |
| SKILL.md:64-67 §6 rules | kept; two rules added (maturity, culture, cruelty to a prop motif, true tiers; no text unless the pattern allows) | CD-28, CD-29, CF-15, UP-19; V4 diff |
| SKILL.md:70-73 §7 self-check | replaced by the round-based checklist pointing to BR, RO, PK, FN, HO lines | The self-review moved to `self-review.md` |
| prompt-patterns.md:1 author line | kept; J018 clause added | Header rule |
| prompt-patterns.md:30-31 §1a table | kept; rows added for rough options and edits | RI-02, CR-05 |
| prompt-patterns.md:49 §3 Edits | kept; the paint-over, colourway, light-variant and merge forms added | CR-05, LC-23, LC-11, RI-22 |
| prompt-patterns.md:59-70 §5 patterns | kept (tested examples unchanged); concept, character, prop, environment, pose and vfx patterns sharpened; rows added (option, view, material-ID, variant, mannequin variant, paint-over, colour vignette, glow draft) | CF-02, SS-04, MD-12, WL-22, SS-10, VR-02 and others in table a |
| prompt-patterns.md:72 §6 step 1 | sharpened: check with the round's lines (`self-review.md` §2) instead of I-05 | Checks live in one place |
| (none) | added prompt-patterns §8 "Words that make the subject specific" | RI-07, EX-02, WT-08, MD-01, MD-09, RI-23, SD-29 |
| (none) | added `references/rounds.md`, `references/self-review.md` | New stages and the self-review |

## d. Command runs (V3), proposals from other roles (V11), binding-skill diff (V4)
Samples (synthetic stand-ins for generated reference images, scratch `<scratchpad>/reference-images_v3/`): a model reference on a light-grey gradient with a vignette, a soft floor shadow and a white collar near the backdrop grey (1024x1536); the same with two views (an I-04 fault); a 3-pose sheet and a copy whose poses touch (1800x1000); a 3-frame VFX sheet on dark with a faint smoke frame (1800x700); a magenta icon (1024); a full concept scene with a sky gradient, ground and a small mid-value hero (1920x1080) with a coarse traced hero polygon; a symmetric and an asymmetric figure; two rough options and a recolour of one; a model reference on a strong gradient.
| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| C1 / FN1 | `look_check.py silhouette` default tolerance (40) | model reference, light-grey gradient, white collar | runs, JSON and black-fill written; `component_count` 2: the collar keyed out and split head from body: **wrong count, no error** → `--key-tol 16` as the start value and "look at the black-fill when the count is unexpected" |
| C1 | same at `--key-tol 16` | same | figure whole; the soft floor shadow becomes a second wide, flat component (count 2): **wrong count, no error** → listed as a known false reading; template proposal (no floor shadow) |
| C1 | `--key-tol 8` | same, pose sheet, VFX sheet | `invalid-mask` (border not flat): loud |
| C1 / I-04 | `--key-tol 16` | two-view model sheet | 2 equal components (0.094, 0.094): right (the fault is caught) |
| C1 / FN1 | `--key-tol 16` | 3-pose sheet; poses touching | 3 (right); 2 when two poses touch: **wrong count, no error** → known false reading |
| C1 / FN1 | `--key-tol 40`, `16`, `24` | VFX sheet on dark | 2 at 40 (faint smoke frame dropped), 2 at 16 (halos merge two frames), 3 at 24: **unreliable on dark glows** → VFX and scene counts are looked at, not measured |
| C1 | `--key-tol 16`, then 40 | model reference on a strong gradient (232 to 176) | 16: `invalid-mask` (loud); 40: measured, one component → "re-run at 40 and look at the black-fill" |
| C1 | default | full concept scene | `invalid-mask`, "no flat key-colour border" (loud): scenes need a traced mask |
| C2 | `look_check.py thumb --key-tol 16 --size 61x91` (scale = 60 px ÷ the 793 px box) | rough option, flat ground | small image and sheet written; subject 61 px tall; `silhouette` gives area and box, no component count (noted in C2) |
| C2 | `thumb --size 640x360` with and without `--mask` | concept scene | with the traced mask: measured (ratio 1.14); without: `invalid-mask`, small image still written |
| C3 / RO5 | `look_check.py value --key-tol 16` | rough option, flat ground | measured; subject/ring 4.05 against the backdrop (a figure on light grey) |
| C3 | `value --mask <traced polygon>` | concept scene: red-shirted hero on green ground | 1.11: right (hue contrast, almost no value contrast: the hero merges in grey) |
| C4 / FN5 | mirror command from `marketing-craft/references/image-pipeline.md` §4, then `silhouette --compare <mirror>` | symmetric and asymmetric figures | 1.0 (symmetric: right); 0.23 for one arm out and a sword: the box widens and centring shifts the body, so the IoU drops far more than the element's area → read only "symmetric or not" |
| C5 / RO2 | `silhouette A --compare B` | two rough options; an option and its recolour | 0.46 (different directions: right); 1.0 for the recolour (same direction: right) |
| C6 | contact-sheet command, `art-review/references/look-check.md` §5 line 6 | two portrait roughs and a landscape scene | runs; narrow images padded grey to the widest cell |
| C7 | 3-value command, `marketing-craft/references/image-pipeline.md` §4 | concept scene | runs; dark 0.004, mid 0.883, light 0.112, near a cut 0.078 |
| C8 / FN7 | `look_check.py palette --key-tol 16 --k 6 --roles {...}` | model reference | measured; roles found (ΔE 0 on flat synthetic colours); the floor shadow keyed in became an 8 % cluster: **false colour, no error** → listed |
| C9 / FN11 | `thumb_check.py icon` | magenta icon | runs; magenta key snapped, 150x150 sheet and JSON written |
| C9 | `look_check.py thumb --size 48x48` | magenta icon | measured; subject/ring 2.07 at 48 px |
| C10 / FN7 | reserved-hue command, `art-review/references/look-check.md` §5 line 4 | concept scene, hero shirt in the reserved red | share 0.0070 without exclusion; 0.0020 with the coarse hero polygon excluded, because the polygon missed the arms: **wrong share, no error** → listed (exclude with a traced, overlay-checked mask) |
| FN6 | region masks, `art-review/references/look-check.md` §5 line 1, on the C1 black-fill | model reference, flat ground | upper p50 0.112, lower 0.033: runs on our input type |
| FN14 | C1 `area_frac` and `area_px ÷ bbox_px.h²` | an option, a half-size copy, the same figure reframed small on a wider canvas | `area_frac` 0.142, 0.144, 0.018: **wrong with no error when the frame differs** → FN14 uses the scale-free ratio (0.217, 0.219, 0.219) |
| RO4 / C6 | contact sheet (C6) run on three C2 small images (61x91) at a height of 360 | rough options at real size | runs; one image shows each rough enlarged from its real size, colour and grey; a skin-tone head close to the backdrop grey shows in the grey row |
| C11 | `art_refs.py --bible templates/skill/art-bible.md print` with warm-up, option, paint-over, pose-option and back-view rows | manifest | rc 0 with repo-relative inputs; an absolute path written in another shell's form fails "input image not found" (loud); the back-view identity prints beside "front three-quarter view" with no error → step 3 lock-conflict stop; template and tool proposals |
| C12 / RO5 (repair 1) | `contrast --sample` for the ground hex, the composite one-liner, `value <onground> --mask <silhouette.png>` exactly as written | cream pet rough on flat light grey (1024x1536) with a green ground capture (1600x720) | runs, writes `<id>.onground.png`, its luminance image and JSON; ground `#467832`; ratio 4.17 (separates: right); on sand `#D8C8A0` 1.31 (a true merge: right); C3 against the backdrop on the same image 1.09 (the old pass line would have failed it: the false fail of F2) |
| C12 (repair 1) | same, with a soft floor shadow keyed in at 16 | cream pet + shadow | C1 count 2 (the shadow); the shadow is pasted onto the ground as a grey blob and counted as subject; ratio unchanged 4.17 for this small shadow: **listed as a false reading, look at the copy** |
| C8 / FN7 role shares (repair 1) | `palette --key-tol 16 --k 6 --roles {main, support, accent}` | flat 3-colour figure; the same figure shaded top to bottom (areas 53/39/8 %) | flat: clusters 0.815/0.154/0.031 (the synthetic's own areas: right); shaded: six clusters, summed by hue family 0.525/0.392/0.084 (right); a role's `nearest_cluster` share alone read main 0.195: **wrong with no error** → FN7 sums by hue family; the shaded cream clustered as `#B2A78D` (grey-brown) → judged on the swatches image |
| C4 / FN5 (repair 1) | the marketing mirror one-liner, then `silhouette --key-tol 16 --compare <id>.mirror.png` | symmetric front view; the same with a shoulder block; the symmetric figure turned (three-quarter stand-in) | 1.0 (right); 0.459 (asymmetry found, box widened); 0.764 for the turned symmetric figure: **reads as asymmetric on a symmetric design, no error** → the IoU runs on front or side views only; the mirror writes `<id>.mirror.png` beside the image (round 1 named `<img>.mirror.png`) |
| C1 radial (repair 1) | `silhouette --key-tol 16` | figure (301 px wide) on radial falloffs centre 236 → border 206, 240 → 200, 232 → 220 | box 443, 589 and 301 px wide, count 1 each time, verdict `measured`: the first two **wrong with no error** → C1 false readings: look at the black-fill once per image before C2, C5, C12 or FN14 use the box |
| C11 / F1 (repair 1) | `art_refs.py --bible templates/skill/art-bible.md print` | the revised `character` option row (no camera words) and a `pose` option row "seen from behind and above as the game camera shows it" | rc 0; the character row sits under "front three-quarter view" with nothing that fights it; the pose row's angle sits under the POSE SHEET LOCK, which fixes no view: right |

Proposal rows from other roles (V11):
- `proposals/animator.md` (reference-images §3 animator row: 2-3 key-pose options per signature move at the game-camera angle, attached, judged as silhouettes): **adopted** (SK §3 animator row; RD §3 item 6; RD §8 example C; SR RO6, FN1).
- `proposals/art-director.md` row 1 (direction rounds: hooks first, warm-up, 3-4 kept with one radical, one per chat at medium, equal finish, grey and black-fill before the colour pick, one contact sheet; paint-over route on the review capture; key light and reserved hues from the WORLD STYLE LOCK): **adopted** (SK §4 R1 row, I-13 to I-17, §3 art-director row, I-11; RD §3 items 1-4 with the 6-12 text hooks in item 2, §6; SR RO1-RO5; the hooks step was missing in round 1 and landed in repair round 1). Kept count: 3-5 generated where the art director keeps 3-4; both books call the count a project choice and the rough round's 6-image cap holds. The `paintover` family it names does not exist in the template: a paint-over uses the capture's own family (`concept` for a game capture), tested in C11; no new family proposed.
- `proposals/art-director.md` row 2 and `proposals/marketing.md` row 1 (`thumbnail-rough` family): **adopted** as an endorsement in my proposals file and as RD §3 item 5 (used when the bible has it); the template change is theirs to land.
- `proposals/character-rigger.md` (model sheets show back and side views, attachments, material intent per region, costly parts): **adopted** (SK §3 rigger row; RD §5 final table; SR FN3, FN12, HO1). Back and side views need a family whose lock allows them: template proposal row 1.
- `proposals/film-director.md` (colour-strip vignettes take the approved value-strip frame as image 1, "keep the values; colour only"): **adopted** (SK §3 film-director row; PP §5 colour vignette row).
- `proposals/game-designer.md` (concept from the game camera's angle; equal finish; warm-up; a hook per option): **adopted** (SK §3 game-designer row, I-11, I-14, I-16; PP §5 concept and option rows).
- `proposals/marketing.md` row 2 (marketing row: warm-up first, a hook per row, equal finish, finals at final size; I-13 medium for rough rounds): **adopted** (SK §3 marketing row points to the staged route; I-14 to I-16; I-13 changed, owner confirmation row at G3).
- `proposals/modeler.md` (model sheets include the game-camera view and a flat-colour material-ID version; mannequin variants): **adopted** (SK §3 modeler row; RD §5 final table; PP §5 view, material-ID and mannequin variant rows).
- `proposals/ui-ux-designer.md` (family `ui`: options at equal finish, a hook each, warm-up, one recommendation; UI LOCK carries the thematic line): **adopted** (SK §3 ui-ux row and the line under the table; I-14, I-16; SR PK1).
- `proposals/vfx-designer.md`, `game-designer.md` row 2, `art-director.md` row 3: no change asked of these books (role skills lists): nothing to adopt.

Binding-skill diff (V4): the lines that touch younger players, paid random items, franchises and maturity are §6 rule 5 (maturity label, no sexualised bodies or poses, blood and gore as the label allows, a real culture represented accurately, cruelty moved to a prop motif, true tiers in reveal and reward images) and FN15. Diffed against `platform-policy/references/rules.md`: line 87 (no third-party copyright or trademarks; franchise themes need original designs) agrees with I-07 and §6 rule 2; lines 7-20 (paid random items: odds, windups) are UI and design rules that no reference image overrides; FN15 only keeps an image from showing a tier the player does not get; line 56 (restricted triggers: strong violence, heavy realistic blood) is why §6 says "as the label allows" and defers to the skill; line 77 (player-triggered generative AI) does not apply (we generate offline, never from a player's action). No contradiction; the rule text says `platform-policy` wins. No library row needed.

Docs read: `production/publishing/experience-icons.md` lines 34, 55; `production/publishing/thumbnails.md` line 54; `production/monetization/passes.md` line 28; `production/monetization/developer-products.md` line 30; `production/publishing/badges.md` line 32 (the frames FN11 and C9 name); `knowledge/reference/roblox/docs-map.md` L21 (art-director row; reference-images has no row of its own).

V5 pass (scripted, `<scratchpad>/reference-images_cov/`): all 176 tagged findings have a row; every BR, RO, PK, FN, PO, HO and C id named in table a exists in `self-review.md`; every `§` section, I-id and UP-id named exists in its file; every landed row names a self-review line or says whose check it is. The worked examples in `rounds.md` §8 were re-read after RO2 (the IoU rule) changed example A.

V5 pass, repair round 1 (scripted, `<scratchpad>/reference-images_rep1/`): every self-review id and command id named in tables a and b exists in `self-review.md` (C12 added); the rows changed in this round were opened at their landed-in locations; the worked examples that use a changed rule were re-read: `rounds.md` §8 A (hooks, the lock's view at R1, C12 in the grey, FN13 on the modeler's render), §8 C (pose rows keep the game-camera angle: the POSE SHEET LOCK fixes no view), and the `prompt-patterns.md` §5 option row (both examples printed with no conflict).

## Repair round 1 (review `reviews/reference-images-rev1-reviewer.md`, verdict fix-first)
| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 rough angle vs the three-quarter locks | SKILL §5 I-11 (game-camera angle only where the family's lock leaves the camera open; else the lock's view, the read judged at R3); §8 P2; `rounds.md` §3 item 3 (camera words per family), §8 A (R1 in the lock's view; at R3 the back and game-camera views blocked, FN13 on the modeler's blockout render); `prompt-patterns.md` §1a rough row and §5 option row (pattern bracket; the `character` example without camera words, a `pose` example with them); `self-review.md` RO4 (the round's view), FN13 (named inputs for the game-camera view, else NOT REVIEWED). The `view` family proposal row now also names this case |
| F2 RO5 backdrop pass line | `self-review.md` RO5 (C3's backdrop ratio recorded as information only; measured C12: the rough on the game's ground against the bible's character separation target, starting value 1.5; a failing or borderline ratio looked at on the copy; the read-first part looked at in the grey), PK1 (passed RO4 and RO5; failing ones listed with what failed), new §4 C12 with its false readings, C3 false readings (2.82 vs 1.41 for one character; 1.09 vs 4.17 for one pet); `rounds.md` §4 (the backdrop ratio never decides who is on the sheet), §7 R1 row, §8 A. One step past the review's smallest fix (a looked-at pass only): C12 measures what RO5 asks (separation from the game's ground) with existing tool modes and a one-line composite, tested both ways (4.17 on green, 1.31 on sand) |
| F3 FN5 asymmetry number cannot fail | `self-review.md` FN5 (the asymmetric element looked at: named and visible at real size; mirror IoU only on front or side views; the mirror copy as a fresh-eyes look on the pick and each final), §4 C4 (front or side views only; a symmetric design turned three-quarter reads 0.74-0.88 in the review's runs, 0.76 in mine; file name `<id>.mirror.png`); coverage rows SS-16, CR-09 |
| F4 hooks step missing; UP-14 count | `rounds.md` §3 item 2 (6-12 text hooks, the 3-5 strongest generated, cut ones with a reason), §7 R1 row, §8 A (eight hooks, four kept, the four cuts with reasons); SKILL §4 R1 row; `self-review.md` RO1 (hooks 6-12; roughs 3-5); SKILL §8 P14; coverage rows UP-14 (reason for 3-5 generated), RI-20, RI-16 and the art-director V11 row corrected |
| F5 CF-15, VC-14, LC-04 landings | `self-review.md` FN11 (concept, thumbnail, storyboard: three planes on the grey; C7), FN6 (detail materials of one part in close values inside a contrasting frame), FN7 (role shares from C8 summed by hue family, starting value 60/30/10, tested on a shaded figure); coverage rows CF-15, VC-14, LC-04 corrected |
| F6 five principles without an example | SKILL §8 P13, P14, P15, P18, P19 each have an example from the starter-pet and egg-reveal work |
| R1 radial falloff false reading | `self-review.md` §4 C1 false readings (a centre more than about 16 levels lighter than the border: wrong box, count 1, no error; look at the black-fill once per image before its box is used). Re-run: 443 and 589 px for a 301 px figure |
| R2 PK2 across a lock change | `self-review.md` PK2 (compare only the final in the pick's family and pose; a model reference, pose sheet or new view is not compared) |
| R3 partial landings | `self-review.md` FN5 (props and vehicles: top line with an echoing bottom line; lines toward 1-2 shared points, one line across parts), FN12 (jump apex legs tucked in a V), FN9 (a new look material's swatch approved first; edges crisp on hard, soft on organic, no all-hard or all-soft zone), FN11 (read order on the grey at real size; saturation peaks at the focal point); coverage rows SS-09, CF-09, SS-11, MD-08, MD-03, VH-09, LC-22 |
| R4 V7 re-read line | SKILL §1: re-read §4, §6, §7 and §8 after a compaction. §6 now starts at about 18.2 KB. The §5 Evidence column was not shortened: its lines carry the owner decision ids each practice rests on, and the re-read line already covers what falls past 18 KB |
| R5 one rule in many places | The rough-round rule lives in `rounds.md` §3 and RO1; SKILL §3 last line, I-14, I-16, §7 and P14 point to it; `prompt-patterns.md` §1a points to `rounds.md` §3 item 3. The SKILL §4 R1 row keeps its counts: it is the round table every role reads first |
| R6 art-director one-game duty | SKILL §3 art-director row ("checks that images from all roles look like one game (`art-review`)"); table c row corrected |
| keep list | all kept: R0-R3 with the pick between batches and "Who generates"; the brief fields; the two-half board; the per-next-maker final table; paint-overs; the edit forms and §5 rows; prompt-patterns §8; the budget table; C2's scale rule, C5 as shape change only, `--key-tol 16`; FN14's ratio; §6 rule 5 and FN15; the proposals file |
