---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2)
supersedes: []
---
> Author: J018 maker marketing · claude-opus-5-5 · high · 2026-10-22; repair round 1 by J018 maker marketing · claude-opus-5-5 · high · 2026-10-22 (review `reviews/marketing-rev1-reviewer.md`); repair round 3 by the same author, 2026-10-22 (review `reviews/marketing-rev3-reviewer.md`, table i)

# Coverage: marketing (J018 stage 2, wave 2)

Books rebuilt (old state: `df13ff4`): `.agents/roles/marketing.md` (body only; frontmatter byte-identical, sha256 prefix ad3a7e28 before and after), `.agents/skills/marketing-design/` (SKILL.md; `references/discovery-promise.md`, `channels.md`; `cases.md` and `policy-rights.md` unchanged), `.agents/skills/marketing-craft/` (SKILL.md; `references/image-pipeline.md`, `channel-kits.md`, `handoffs.md`; new `references/image-review.md`; `testing-measurement.md` unchanged in content (line endings normalised to LF in repair round 1); `evals/` untouched).
SKILL.md lines: marketing-design 114, marketing-craft 87 (both ≤ 500). Descriptions: 388 and 380 characters.
Where the self-review lives: `marketing-craft/references/image-review.md` (MR-01..MR-33; which lines run at which stage: its §1), run from `marketing-craft` SKILL §6 and from the role file's "Before you hand back"; video checks in `channel-kits.md` §3. "Core principles for this craft": `marketing-design` §7 (§1 says to re-read §4 and §7 after a compaction; §7 starts near 14 KB, the steps, rules and self-check sit before it).

Legend for table a: DS = `marketing-design/SKILL.md`; CS = `marketing-craft/SKILL.md`; IP = `marketing-craft/references/image-pipeline.md`; IR = `marketing-craft/references/image-review.md`; HO = `marketing-craft/references/handoffs.md`; CK = `marketing-craft/references/channel-kits.md`; DP = `marketing-design/references/discovery-promise.md`; RF = `.agents/roles/marketing.md`. "DS §7 row N" = core principle N in `marketing-design` §7 (rows use the master's numbers: row 1 = UP-01).
Counts: 135 findings tagged marketing in `matrix.md`: 117 landed, 18 rejected with a reason; 18 untagged findings used. Library numbers marked [inference] are written as starting values (60/30/10 shares, the 0.8 frame-IoU value, 3-5 roughs, 2-3 light set-ups); no [unverified] engine claim was added.

## a. Findings

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CD-01 | Know the character, then decide on their behalf | IP §1 stage 1 (premise, sell list); DS §4 M-21; IR MR-09 (pose traces to the premise); IR MR-27 (no sexualised pose, costume or body) | step; standard; self-review check |  |
| CD-02 | Write the sell list before drawing | IP §1 stage 1; IR MR-01; RF work method 1; DS §7 row 10 | step; self-review check; core principle |  |
| CD-03 | Understand the archetype before evolving it | HO table art-director row (the 2-3 identity anchors per hero every crop keeps); DS §4 M-17; IR MR-08 (the outline names the subject) | step; standard; self-review check |  |
| CD-04 | Variants hold the identity anchors and change the rest | DS §4 M-17, M-22; HO table art-director row; IR MR-10 | standard; self-review check |  |
| CD-05 | If a variant drops a silhouette landmark, fill its slot |  |  | Variant design (filling a dropped landmark slot) is the art director's and modeler's work; marketing receives the anchor list (DS §4 M-17) and checks it is present in every crop (IR MR-08, MR-10) |
| CD-06 | Keep the likeness the same in every product | DS §4 M-17 (likeness in every product); IR MR-10; DS §7 row 11 | standard; self-review check; core principle |  |
| CD-09 | Every action shows who this character is | CK §3 "Character and brand in motion" (checked on the edit's key frames; feel at speed: owner on the preview) | standard; self-review check (video) |  |
| CD-13 | Twist the tone within bounds; darker still keeps the appeal | IR MR-27 (a darker twist keeps the hero's appeal) | self-review check |  |
| CD-14 | Keep the cool core, swap one iconic item, justify it by lore |  |  | Designing the variant twist (keep the core, swap one item, justified by lore) is the art director's and live-ops designer's work; marketing shows the launched variant as the hero (DS §4 M-15) |
| CD-15 | Re-theme the abilities, not only the costume | CK §3 "Character and brand in motion" (a variant is shown through its re-themed ability) | standard; self-review check (video) |  |
| CD-20 | Small accents carry the personality |  |  | Small personality accents do not survive the tile or icon size; in marketing art personality is carried by the pose and the premise (DS §4 M-21, IR MR-09) |
| CD-21 | Explore costumes on varied poses and body types |  |  | Costume exploration on varied poses is the art director's concept work; marketing varies the hook, layout and camera of its roughs (IP §1 stage 3) and takes the pose from the animator |
| CD-22 | Put the eyes and face in early | IR MR-10 (face fixed before anyone sees the image); IP §1 stage 8 (face at its best before any review); RF "Your place" (return path) | self-review check; step |  |
| CD-25 | Start promo and story art from a premise and the signature ability pose | DS §4 M-21; CS §4 K-05; IP §1 stages 1-2; HO table animator row and §7; IR MR-09 | standard; step; self-review check |  |
| CD-29 | Move a sensitive theme onto a prop motif | IR MR-27 (sensitive act carried by a prop motif; platform-policy for mature themes) | self-review check |  |
| CF-01 | Big to small: composition first, detail and effects last | IP §1 (stages big to small); CS §4 K-12; IR MR-28; DS §7 row 4 | stage; standard; self-review check; core principle |  |
| CF-02 | Design and pose for the side the game camera shows | IP §1 stage 5 (identifying shapes facing the camera); IR MR-09 (no limb points at the lens) | step; self-review check |  |
| CF-04 | Compose inside the real frame, crop and UI, at final scale | IP §1 stage 1 (crop plan), stage 5 (safe squares, real-layout mock), stage 10; CS §4 K-14; IR MR-22 | stage; standard; self-review check |  |
| CF-05 | Lock a safe square around the crop, then move anything else | IP §1 stage 5 (every crop's safe square marked before composing the rest); IR MR-22 | step; self-review check |  |
| CF-06 | In a small frame, the identifying parts fill it | DS §4 M-17; IR MR-08, MR-22; IP §5 example B (icon crop) | standard; self-review check; example |  |
| CF-07 | Judge composition on the integrated capture | IP §1 stage 5 (the tile in the real layout among real tiles); IR MR-16 (rebalance after effects and colour) | step; self-review check |  |
| CF-08 | Shape flow points to the focal point, at every scale | DS §4 M-18 (flow lines to the primary); IR MR-17 | standard; self-review check |  |
| CF-12 | A value gradient toward the hero | DS §4 M-19 (lower the surroundings, brightest value on the focal point); IP §1 stage 5 value; IR MR-12 (direction of the hero's value); IP §5 example A | standard; step; self-review check; example |  |
| CF-15 | Three depth groups: foreground frames, midground carries, background unifies | DS §4 M-18; IP §1 stages 5 and 10; IR MR-19; HO §8 (named FG, MG, BG groups); IR MR-27 (gore in every layer, foreground first, within the content maturity label) | standard; stage; self-review check |  |
| CF-16 | Negative space on purpose: calm room, no awkward gaps | DS §4 M-18 (calm room for the title); IR MR-20 | standard; self-review check |  |
| CF-17 | A giant figure behind small heroes sells scale and threat | IR MR-11 (scale ratio obvious in black-fill); IP §5 example A rough A | self-review check; example |  |
| CF-18 | Camera height states status | DS §4 M-21 (camera height states status); IR MR-09; IP §5 example B (eye level for a friendly hero) | standard; self-review check; example |  |
| CF-19 | Small secondary elements carry movement and colour pops along the eye path | IR MR-17 (small accents on the eye path, smaller and quieter than the focus) | self-review check |  |
| CF-20 | Background patterns are reversible and A/B tested | IP §1 stage 8; IR MR-16 (a background pattern layer stays only if the read order is the same with it on) | step; self-review check |  |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | IR MR-26 (next to an in-game capture at the same size); IP §1 stage 2 (captures of the moment at the game camera) | self-review check; step |  |
| CR-02 | Ask a goal question, never "do you like it?" | IR MR-05; CK §8 item 2; DS §7 row 16 | self-review check; step; core principle |  |
| CR-08 | Diagnose by layer; "not happy" may mean "not done" | IR §1 "Order of fixing" (by layer, re-run the layers after it); IR MR-32 (fix log: one problem per pass, its layer, lines re-run); CS §4 K-15 | step; standard; self-review check |  |
| CR-09 | Fresh eyes: flip the image, change the reviewer | IR MR-24 (mirror, then grey); CS §4 K-15; HO §3 C2 (the art director's cold read) | self-review check; standard |  |
| CR-11 | The project's needs come first; the lead curates the best solution | IP §1 stage 11; IR MR-32 (every reviewer note mapped to done or questioned) | step; self-review check |  |
| CR-12 | When every option meets the brief, choose and commit | IP §1 stage 4 (pick with reasons, closed options not reproposed); IR MR-31 (closed directions recorded); DS §7 row 16 | step; self-review check; core principle |  |
| CR-14 | Pitch the experience the player will have, with conviction | CK §8 item 2 (describe each image as the moment the player will have in play); IR MR-05 (what each option's player would expect) | step; self-review check |  |
| CC-05 | Share strong motifs across crafts; seek input from several roles | DS §4 M-22 (motif from the game's own UI, items or story); HO table art-director row (brand pattern); IR MR-26 | standard; self-review check |  |
| EX-01 | Larger than life: extend and sharpen what must read | DS §4 M-17 (pushed past real); DS §7 row 9; IR MR-09 | standard; core principle; self-review check |  |
| EX-02 | Make a pose specific by layering adjectives, then pull back if too far | IP §1 stage 5 (the pose carries 2-4 adjectives from the premise, pushed then pulled back); IR MR-09 (I name the adjectives from the pose) | step; self-review check |  |
| EX-03 | For comedy, pose against the character's known trait | IP §1 stage 3 (for a comic tone, one option poses the hero against its known trait); IR MR-09 (the contradiction reads in the whole body) | step; self-review check |  |
| GD-04 | Name the target experience, not "fun" | IP §1 stage 1 (the target experience the game names); IR MR-01 | step; self-review check |  |
| GD-08 | Art turns rules and numbers into a fantasy players build around |  |  | Giving systems a collectable fantasy is the game designer's and art director's work; marketing already shows a collection as one hook source (CS §4 K-03 progression payoff); nothing new for marketing |
| GD-16 | Cosmetics never change the gameplay read or cost gameplay |  |  | A rule for the cosmetic itself (game designer, art director); marketing's side, showing an item as it really is, is IR MR-25 |
| GD-17 | Cosmetics refresh repeated play without changing balance |  |  | A design rationale for cosmetics; marketing's update message names the real new thing (CK §4), which this finding does not change |
| GD-20 | Choose themes from data; combine proven themes and tune the maturity | DS §1 question 2 (what fans want, dated); IP §1 stage 1 ("fans want" line from the trend scout, Discord or the analyst); HO table trend-scout row; IR MR-01 | standard; step; self-review check |  |
| GD-25 | Build conflict into the objective; tie it to the world's story |  |  | Building conflict into a map objective is level and game design; marketing shows it only when it is the launched thing (DS §4 M-15) |
| GD-32 | Hide small secrets that reward discovery |  |  | In-world secrets are placed by level and live-ops designers; the marketing-side hidden layer is the brand-first, story-second rule (IR MR-27) |
| GD-33 | A map is never done; new worlds are an escape | IP §1 stage 1 (for a new world, what makes it a clear escape from the last one); IR MR-01 | step; self-review check |  |
| LC-04 | Few colours with roles: about 60 / 30 / 10, after the greys work | DS §4 M-20; IP §1 stage 7; IR MR-15 | standard; stage; self-review check |  |
| LC-07 | Shift hue for shadows and highlights; do not just add black or white | DS §4 M-20 (shadows shift hue); IP §1 stage 7; IR MR-15 | standard; self-review check |  |
| LC-11 | Block light and shadow first; test lighting options on the rough | IP §1 stage 5 (2-3 light set-ups on the rough, compared at tile size in grey); IR MR-14 | stage; self-review check |  |
| LC-12 | Light leads the eye: the brightest area is the focus | DS §4 M-19, M-20; IR MR-12 (direction of the hero's value against the ring) | standard; self-review check |  |
| LC-13 | Light motivated by the setting | DS §4 M-20 (one motivated key light); IR MR-14 | standard; self-review check |  |
| LC-14 | Light direction sets good or evil | DS §4 M-20 (light from below means threat); IR MR-14 | standard; self-review check |  |
| LC-15 | Rim light separates figures from the background | DS §4 M-20; IR MR-14 (rim where the hero meets a similar value) | standard; self-review check |  |
| LC-17 | Calm the field, pop small saturated accents | DS §4 M-19 (strongest colour pop on the focal point); IR MR-15 | standard; self-review check |  |
| LC-22 | Review with colour in, then rebalance | IP §1 stage 7 (re-run the read order and contrast numbers after colour); IR MR-16 | step; self-review check |  |
| LC-23 | Iterate colour globally; colourways are the same object | IP §1 stage 7 (2-3 global colourways, never local repainting); IR MR-13 (each colourway keeps the value ratio) | step; self-review check |  |
| LC-24 | Check colour on a phone before it ships | DS §4 M-20; IR MR-18 (sRGB profile; the owner on a phone at a named check-in); IP §4 colour-profile command | standard; self-review check |  |
| MD-02 | Budget detail by display size, camera distance and player speed | IP §1 stage 8 (detail clumped at the focal points; "the master may carry more detail than the game model (the page and large ad tiles show it), never at the cost of the read at tile size": clause added in repair round 1, R4); IR MR-17 | step; self-review check |  |
| MD-03 | Finish comes from crisp edges and planes, balanced with soft | IP §1 stage 8 (crisp edges on the hero); IR MR-14 (key edges crisp, organic transitions soft) | step; self-review check |  |
| PP-31 | Make final images at their final resolution | IP §1 stage 6; CS §4 K-14; IR MR-29; HO §8 rules | stage; standard; self-review check |  |
| PP-32 | One key art feeds a whole asset kit; deliver switchable layers | IP §1 stage 10; CS §4 K-14; IR MR-30; HO §8 (named toggleable groups) | stage; standard; self-review check |  |
| PP-33 | The icon and thumbnail are the box art: highest effort, tested at grid size | DS §3 step 3 (box art); RF opening paragraph; CS §4 K-01; IR MR-23 (the grid) | step; standard; self-review check |  |
| PI-02 | Gates freeze decisions: rough, approved direction, materials, polish | IP §1 (each stage freezes the one before; G1, G2); CS §4 K-12; IR MR-28 (frozen big shapes); DS §7 row 15 | stage; standard; self-review check; core principle |  |
| PI-05 | Work small early so only big shapes can be judged | IP §1 stage 3 (roughs judged only on their sheets at tile size); CS §4 K-01; IR MR-06 | step; standard; self-review check |  |
| PI-13 | Finish a concept only as far as the next maker needs | IP §1 stage 3 (roughs stop at the big read); IR MR-06 (roughs judged on the sheet at tile size) | step; self-review check |  |
| RI-01 | Concept work solves a problem; it is a functional vehicle, not a nice picture | IP §1 stage 1 (the brief states what the image must do); IR MR-01; DS §7 row 13 | step; self-review check; core principle |  |
| RI-02 | Show options at equal, low finish on a clean, labelled sheet | IR MR-04, MR-05 (equal finish, one sheet); CS §4 K-13; CK §8 item 2 | self-review check; standard |  |
| RI-04 | In marketing art, the launched thing is the hero | DS §4 M-15; IP §1 stage 1; IR MR-01; DS §1 question 1 | standard; step; self-review check |  |
| RI-05 | Research first; one narrow moodboard with pillars and key features | IP §1 stage 2 (research board); IR MR-02 | stage; self-review check |  |
| RI-06 | Each theme gets a library: shorthand motifs, iconography, a name and a logo | DS §4 M-22 (brand pattern, motifs); HO table art-director row (brand pattern); IR MR-26 | standard; self-review check |  |
| RI-07 | Turn each keyword into visual facts before prompting | IP §1 stage 1 (keyword table); IR MR-01; IR MR-04 (each rough's elements map to keyword rows, none missing) | step; self-review check |  |
| RI-08 | Reference order: our game first, then the real world, then mix; take ideas, never copy | IP §1 stage 2 (our game first, then outside reference with a purpose each); IR MR-02 | stage; self-review check |  |
| RI-09 | When a brief fuses two ideas, reference the overlap | IP §1 stage 2 (reference where the two fused ideas overlap); IR MR-02 | step; self-review check |  |
| RI-16 | Research, explore wide and loose, iterate on one or two, finish only what the next maker needs | IP §1 stages 2-4 (research, wide round, pick, then refine one); IR MR-03 to MR-05 | stage; self-review check |  |
| RI-18 | Each option gets its own hook from a different source | IP §1 stage 3 (each rough from a different hook source); IR MR-04 (shape and frame IoU) | stage; self-review check |  |
| RI-19 | Present options with your pick and the reasons; then iterate | IP §1 stage 4; IR MR-05; RF "Your place" (recommended one stated at G1) | stage; self-review check |  |
| RI-20 | For the final pick, compare four or five strong small options and choose the clearest | IP §1 stages 3-4 (3-5 roughs, the clearest picked against the sell list); IR MR-05 | stage; self-review check |  |
| RI-21 | The first output is a warm-up; reject the typical idea | IP §1 stage 3 (typical idea first, labelled warm-up); IR MR-03; CS §4 K-13; DS §4 M-23 | stage; self-review check; standard |  |
| RI-22 | Vary one element per option, label them, merge the best two | IP §1 stage 4 (merge on purpose: "B's strike + A's scale"); IR MR-05 (a merge names its sources); IP §5 example A | step; self-review check; example |  |
| RI-23 | Bring in one unexpected element from outside the genre | DS §4 M-23; IP §1 stage 2 (one source from outside games); IR MR-02 | standard; step; self-review check |  |
| RI-27 | Design a variant through a narrative lens |  |  | Designing a variant through a narrative lens is the art director's and live-ops designer's work; marketing's narrative tool for the image is the one-sentence premise (CD-25, IP §1 stage 1) |
| RI-28 | One message, one symbol, before drawing | DS §4 M-18 (one message, one symbol); IP §1 stage 1, stage 5 (symbol traced as a black shape); IR MR-01; IR MR-26 (symbol square, `thumb_check.py icon --key auto`, named from the 150×150 tile) | standard; step; self-review check |  |
| RI-29 | Find the hook that makes the subject compelling | IP §1 stage 1 (the hook line); IR MR-01 | step; self-review check |  |
| RH-05 | Put motion into a still with a few committed flow lines | DS §4 M-18 (2-3 flow lines); IR MR-17 | standard; self-review check |  |
| SS-01 | Silhouette first, then light that shows form, detail last | IP §1 stage 5 (silhouette, then value, then light; detail at stage 8); CS §4 K-12; IR MR-08 at the rough | stage; standard; self-review check |  |
| SS-02 | Judge the silhouette filled solid, small and squinted | IR MR-08 (black-fill of the real outline only: a mask traced in parts and checked on its overlay, or the magenta pass; a coarse polygon cannot pass or fail it); IP §2 subject row; IP §4 overlay command; IP §1 stage 5 | self-review check; step |  |
| SS-04 | Keep the few identifying elements, make them chunky, cut the rest | DS §4 M-17; IR MR-08 | standard; self-review check |  |
| SS-06 | One shape vocabulary for the whole game, down to the small shapes | IR MR-26 (reads as the same game; shape vocabulary comes through the art bible locks) | self-review check |  |
| SS-07 | Big, medium, small: never two shapes the same size | IP §1 stage 5 (sibling shapes in size steps); IR MR-20 | step; self-review check |  |
| SS-10 | Line of action and gesture before detail | DS §4 M-21; IR MR-09 | standard; self-review check |  |
| SS-11 | Give the jump apex a pose: legs tucked into a V | IR MR-09 (an airborne hero tucks the legs into a V) | self-review check |  |
| SS-17 | Repeat one motif at several scales | IR MR-26 (the event motif repeats at several scales across the kit) | self-review check |  |
| SS-19 | Design the group silhouette | IR MR-08 (a group reads as one shape, ringed by threats when danger is the point) | self-review check |  |
| SD-21 | Every weapon and the whole game get a signature sound | CK §3 "Character and brand in motion" (the game's signature sounds stay in the mix) | standard; self-review check (video) |  |
| SD-29 | Sources by texture, not by name: many takes, some odd ones |  |  | Sourcing sound by texture is the sound designer's craft; marketing edits keep the game's own sounds in sync (CK §3) and take no new sound sources |
| SI-01 | Style sets the emotional tone: set each lever on purpose |  |  | The style levers (saturation, proportion push, value structure) are set in the art bible by the art director; marketing art inherits them through the locks (`reference-images` I-01) and checks the family read (IR MR-26) |
| SI-03 | Theme fit can rule out an otherwise cool idea | IR MR-27 (reads as this game's genre and tone; a cool idea from another genre fails) | self-review check |  |
| SI-05 | Make it for a specific audience, and give fans what they want | DS §4 M-23; DS §1 question 2; IP §1 stage 1; HO table trend-scout row; IR MR-01, MR-05 (the pick cites the "fans want" line) | standard; step; self-review check |  |
| SI-09 | One palette per group so a roster reads as a team |  |  | Roster palettes per group are the art director's; marketing shows the group as the art bible paints it (IR MR-26) |
| SI-11 | An update keeps the kernel and trims what is dated |  |  | Remakes that keep the kernel are the art director's (art-direction §2); marketing shows the result truthfully |
| SI-12 | Each theme needs its own niche | IP §1 stage 1 (for a new world, its escape from the last one); IR MR-01 | step; self-review check |  |
| SI-13 | Refresh a tone by pushing to the extreme, then pulling back to the brand | CK §4 (event names and taglines: one extreme pass, one brand pass, the owner picks; the result keeps the naming pattern) | step; check |  |
| SI-14 | Names and logos: keep the brand pattern, change one thing | DS §4 M-22; IP §1 stage 9 (brand font and lock-up, one property changed); HO table art-director and ui-ux-designer rows; IR MR-26 | standard; step; self-review check |  |
| SI-15 | Draw graphic motifs from the game's own UI and story | DS §4 M-22 (event motif from the game's own UI, items or story); IR MR-26 | standard; self-review check |  |
| SI-16 | Style rules may bend for a format, as logged exceptions | IP §1 stage 8; IR MR-16 (soft effects in a clean style only as a listed format exception) | step; self-review check |  |
| SI-17 | Brand first, hidden story second | DS §4 M-22 (the theme reads first, a hidden detail rewards a close look); IR MR-27 | standard; self-review check |  |
| SI-18 | A variant changes the palette; the same character in a new scene keeps it | IP §1 stage 1 (the brief records new version or same character); IR MR-01; IR MR-10 (anchors of the version shown; `look_check.py palette --mask --roles` with that version's signature colours) | step; self-review check |  |
| SI-19 | A cohesive set, with a documented break for the top tier |  |  | A documented style break for the top tier is the art director's decision; marketing shows each tier as it really is (IR MR-25) |
| SI-20 | Premium tiers get separable finishes |  |  | Separable premium finishes are item design (art director, modeler); marketing shows the item's real finish and its secondary motion in video (CK §3) |
| UI-02 | Each element: one thing to understand, one action it leads to | DS §4 M-18 (one message); IR MR-06 | standard; self-review check |  |
| UI-03 | Design for the audience and the device: phone first | DS §7 row 2 (the tile on a phone); IR MR-18; IP §2 small-size row (the measured phone tile) | core principle; self-review check |  |
| UI-07 | A core thematic first, then explicit style rules |  |  | The UI thematic is set by the art director and the UI designer; the title treatment follows the brand pattern (DS §4 M-22) |
| UI-16 | Motion goal: a physical material that carries the brand | CK §3 "Character and brand in motion" (title cards move in the game's UI motion style) | standard; self-review check (video) |  |
| VC-02 | Values first, colour second; keep a grayscale proof at every step | IP §1 stages 5 and 7 (value study before colour; colour on approved values); IR MR-13 | stage; self-review check |  |
| VC-04 | Make one spot the focus by lowering contrast everywhere else | DS §4 M-19; IP §1 stage 5 (lower the surroundings before raising the hero); IR MR-12 | standard; step; self-review check |  |
| VC-09 | Form shadows make a still object read as 3D | IR MR-14 (every main form shows a light side and a shadow side) | self-review check |  |
| VC-14 | Group detail in close values; frame the group with the strongest colour |  |  | Grouping an asset's detail materials in close values is asset design (art director, modeler); marketing's value plan for the whole image is IR MR-13 |
| VC-16 | Balance visual weight on purpose | IR MR-20 (dark masses balanced where planned) | self-review check |  |
| VC-17 | High contrast for dramatic moments, lower for calm ones | DS §4 M-19 (wide range for drama, narrower for calm); IP §1 stage 1 (tone); IR MR-12 | standard; step; self-review check |  |
| VH-03 | Less is more: the fewest shapes and colours that give the strongest read | DS §7 row 6; IR MR-20 (remove-one-element test) | core principle; self-review check |  |
| VH-05 | Clump detail in a few places; leave areas of rest | DS §4 M-18 (detail clumped where the eye should go); IP §1 stage 8; IR MR-17 | standard; step; self-review check |  |
| VH-06 | The source of power is the primary read | DS §4 M-17 (the signature item breaks the outline); IR MR-08 | standard; self-review check |  |
| VH-07 | Recognisable in under a second beats unique | DS §4 M-16; IR MR-06; IP §5 example B | standard; self-review check; example |  |
| VH-08 | Silhouette is the first read, the face the second | DS §4 M-17 (silhouette first, face second); IR MR-08, MR-10 | standard; self-review check |  |
| VH-09 | Plan the read order: primary, secondary, tertiary | DS §4 M-18 (read order); IR MR-17 | standard; self-review check |  |
| VH-11 | Review in a fixed order: balance, proportion, weight, then contrast and detail | IR §1 "Order of fixing" (big layers before small); IR MR-32 (each fix names its layer) | step; self-review check |  |
| WT-07 | Centre of gravity over the feet, unless off-balance is the point | IR MR-09 (weight over the feet unless off-balance is the point) | self-review check |  |
| WT-08 | Held objects show weight by distance from the body | IR MR-09 (heavy held close, light held far) | self-review check |  |
| WT-24 | Secondary motion adds perceived value | CK §3 "Character and brand in motion" (a premium item shown with its secondary motion) | standard; self-review check (video) |  |
| WL-21 | Scale: a player-sized reference in every blockout and scene | IR MR-11 (a familiar-size object next to a giant subject) | self-review check |  |
| WL-25 | Distance lowers contrast and detail (atmospheric perspective) | IR MR-13 (a quiet, close-valued background) | self-review check |  |
| WL-26 | A small, low-contrast busy background adds life | IP §1 stage 8; IR MR-17 (a busy background reads as texture behind the hero) | step; self-review check |  |
| WL-28 | Work from far away; zoom out every round | IP §1 stage 3 (judge only at tile size); CS §4 K-01; IR MR-06 (the sheet each round); DS §7 row 2 | step; standard; self-review check; core principle |  |

Untagged findings used (tagged for other roles, valuable for marketing):

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| PI-01 | The cheapest stage goes first; expect big changes while it is rough | CS §4 K-12 (stages that freeze; change is cheap while rough); IR MR-03, MR-04 (several roughs before any polish) | standard; self-review check |  |
| PI-03 | Closing doors: from broad to narrow, never reopen | IP §1 stage 4 (closed options recorded, not reproposed without new owner words); IR MR-31 | step; self-review check |  |
| PI-07 | One named problem per pass; fix the worst first | IR §1 "Order of fixing" (worst problem first, one per pass); IR MR-32 (fix log); CS §4 K-15 | step; standard; self-review check |  |
| PI-12 | Know when it is done: written stop criteria, repeating notes | DS §7 row 18; IR MR-22 (every crop passes at real size), MR-32 (budget used) | core principle; self-review check |  |
| CR-03 | Solve the problem behind the note; separate goals from tactics | RF work method 8; IR MR-32 (the problem behind a note re-checked, not only the change) | step; self-review check |  |
| CR-04 | Answer every note with a concrete visible fix; protect the anchor | IP §1 stage 11; IR MR-32 (each note mapped), MR-10 (the anchor unchanged) | step; self-review check |  |
| CR-05 | Give and solve visual notes as paint-overs on a capture | HO §3 check C3 (the art director gives visual notes as paint-overs on the capture or sheet) | step; partner check (the reviewer's line in my brief) |  |
| CR-13 | Close with an honest recap of your own result | IR MR-32 (one named weakness and the next iteration) | self-review check |  |
| CR-17 | Say what each input can prove; end with a could-not-check list | IR §1 (label each line by what proved it), MR-32 (could-not-check list); RF "Before you hand back" | self-review check |  |
| LC-01 | Reserve the gameplay colours; keep them, and fast motion, out of decoration | DS §4 M-20 (gameplay colour meanings kept); IR MR-15 | standard; self-review check |  |
| VC-07 | Reserve white, black and the highest contrast for small focal spots | DS §4 M-19; IR MR-12 (near-white and most saturated pixels only on small focal spots) | standard; self-review check |  |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | IR MR-08 (the outline names the mood: sharp dangerous, round friendly) | self-review check |  |
| RI-17 | Take the big swings at concept stage | IR MR-04 (one atypical rough in every round); DS §7 row 12 | self-review check; core principle |  |
| MD-10 | Controlled imperfection makes it hand-made | DS §7 row 12; IR MR-20 (no machine-made sameness) | core principle; self-review check |  |
| GD-34 | Feedback follows the real outcome: a small cue on input, the big layer on confirmed success | DS §7 row 19; IR MR-25 (no reward burst for a result the action did not earn) | core principle; self-review check |  |
| GD-35 | Paid random reveals are honest | DS §7 row 19 (a reveal image shows a tier players really get); IR MR-25; checked against platform-policy (V4) | core principle; self-review check |  |
| CC-02 | One marker list is the timing contract for animation, VFX and sound | CK §3 "Sound stays in sync" (onsets from the cutter's WAV without music, by the onset command, against contact frame times from the frame command: from 17 ms before to about 40 ms after; no WAV, a WAV of another length or no onset near a hit: "not verified"); input commands in CK §3 "Inputs" | standard; self-review check (video) |  |
| VR-26 | Pulse and blink rates carry meaning: slow is safe, fast is urgent, never above 3 Hz | CK §3 "Flashes" and "Readable for everyone" (repair round 3: the studio's one flash counter, `vfx-craft/references/measure.md` §6, run on the frame command's folder: at most 3 onsets over 10 % of the frame in any 1 s, design for 2; the still at every listed onset and every frame-command change looked at; a saturated red flash "not verified" unless an analyser measures it) | standard; self-review check (video) |  |

## b. Universal principles

All 20 apply to marketing (the master lists marketing for every one). Each row in `marketing-design` §7 states the principle for marketing work, gives a marketing example and names its check (MR lines in `marketing-craft/references/image-review.md`).

| UP-ID | Applies | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: the promise read (what the player will do) is the tile's first job | DS §7 row 1; check MR-06, MR-07 |
| UP-02 | yes: tile on a phone with title and metadata band, icon at 150×150, among competing tiles | DS §7 row 2; MR-06, MR-21 to MR-23; owner on a phone at G1 |
| UP-03 | yes: the hero has the highest contrast and largest readable area; title calm room | DS §7 row 3; MR-12, MR-17, MR-20 |
| UP-04 | yes: brief → thumbnails → silhouette → value and light → colour → detail | DS §7 row 4; stage dates; MR-13, MR-28 |
| UP-05 | yes: identifying shapes fill the crop; black-fill of the real outline names subject and mood | DS §7 row 5; MR-08 (traced or magenta-pass mask only) |
| UP-06 | yes: one message, one symbol, clean backdrop, few identifiers | DS §7 row 6; MR-20 |
| UP-07 | yes: gameplay colour meanings and the brand pattern hold; one property per event | DS §7 row 7; MR-15, MR-26 |
| UP-08 | yes: a still shows the peak of a real action; a video opens on tell, build, beat, peak, result | DS §7 row 8; MR-09; CK §2 step 1 and §3 opening-beat check (the beat's start time listed) |
| UP-09 | yes: big hero, oversized signature item, pushed pose on a believable base | DS §7 row 9; MR-09, MR-11 |
| UP-10 | yes: premise sentence and sell list first; the character's own signature pose | DS §7 row 10; MR-01, MR-09 |
| UP-11 | yes: art bible locks and anchors, the same likeness in every product, one family | DS §7 row 11; MR-10, MR-26 |
| UP-12 | yes: the generic first output is a warm-up; one unexpected element; no machine-made sameness | DS §7 row 12; MR-03, MR-04, MR-20 |
| UP-13 | yes: the brief before the first prompt | DS §7 row 13; MR-01 |
| UP-14 | yes: our game's references first; 3-5 roughs from different hooks; reasoned pick | DS §7 row 14; MR-02, MR-04, MR-05 |
| UP-15 | yes: G1 thumbnail round, G2 green light freezes the big shapes; closed directions stay closed | DS §7 row 15; MR-28; G1 and G2 records |
| UP-16 | yes: goal questions, notes by layer, mirror and grey, ties to the owner with a recommendation | DS §7 row 16; MR-05, MR-24, MR-32 |
| UP-17 | yes: layered, crop-safe master; crop plan; briefs to animator and renderer with named groups | DS §7 row 17; MR-22, MR-30 |
| UP-18 | yes: done when every crop passes at real size, the budget is spent or notes repeat | DS §7 row 18; MR-22; budget line in MR-32 |
| UP-19 | yes (marketing art line of the master): no reward, rarity or celebration the action does not earn | DS §7 row 19; MR-25; `policy-rights.md` §1-2 |
| UP-20 | yes: the promise reads in grayscale at icon size; never colour alone; video readable muted | DS §7 row 20; MR-12, MR-13; CK §3 "Readable for everyone" |

## c. Old book changes (old state: `df13ff4`)

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by (new location) / moved / removed | Why |
| --- | --- | --- |
| `.agents/roles/marketing.md:26` "Job lead of the marketing art recipe: 3-5 rough thumbnails at the real slot size for G1, the green-lit thumbnail at G2 ..." | sharpened (role file "Your place in the job flow"): brief and board, labelled warm-up, roughs from different hooks with the recommended one, G2 sets silhouette, values, light and composition, then the stages | the stages and their order are now the agent's own route (IP §1) |
| `.agents/roles/marketing.md:30` "Craft practice from Riot's artists and designers: `knowledge/jobs/J016-orchestration/riot-extracts.md` §4 (row `marketing`); read it once per job type" | removed; replaced by the agent's own books (DS §4 M-15..M-23, IP §1, IR) | job card fixed list: role files point to their own books, not to the J016 extract; the craft now lives in the books |
| `.agents/roles/marketing.md:33` work method 1 "Restate the brief ..." | sharpened (method 1): image briefs add the hero, sell list, premise, message and symbol, fans want; missing tile size marks checks `not verified` | the brief is the first stage of the image route |
| `.agents/roles/marketing.md:35` work method 3 "Every image goes through `thumb_check.py` at its real small size, your own look ..." | sharpened (methods 3-5): the stages big to small, a hero mask, the self-review, light-check budgets | V1, V3: the subject input and the budget decide whether the numbers mean anything |
| `.agents/roles/marketing.md:38` "Check what you received against the brief before you build on it." | sharpened (method 8): restate the problem behind a note and re-check it | a note's suggested fix is often not the best fix |
| `.agents/roles/marketing.md:41` "From the first concept you work with the game-designer ..." | sharpened; new bullet for animator, environment designer or modeler, ui-ux-designer; captures asked at the brief | what to ask each partner and when (owner spec point 1) |
| `.agents/roles/marketing.md:50` "Return: recommendation in one line · the package file · per image: sheet, JSON, checklist, art director note ..." | sharpened: mask, self-review labels, images made and sheets looked at | V1 budget reporting; honest labels |
| (new) role file "Before you hand back" | added | what the agent checks before hand-back (owner spec point 1) |
| `.agents/skills/marketing-design/SKILL.md:12` question 1 "What does the game promise?" | sharpened: "... and what is being launched?" | the launched thing is the hero of every image |
| `.agents/skills/marketing-design/SKILL.md:13` question 2 "Who is it for, and what do they already want?" | sharpened: what fans of this game or genre want to see, dated | work made for a specific audience |
| `.agents/skills/marketing-design/SKILL.md:36` step 3 "Earn the click with the real moment." | sharpened: "made like box art", judged at tile size among competing tiles, pointer to M-15..M-23 | the icon and thumbnail are the box art |
| `.agents/skills/marketing-design/SKILL.md:43` table header "Evidence" | sharpened: "Evidence or why" | new rows carry their reason, not a source id (no citations in book bodies) |
| `.agents/skills/marketing-design/SKILL.md:69` self-check "The promise line, its moment and its promise-ledger row are named before any asset." | sharpened: plus hero, sell list, premise, fans want; new line for M-15..M-23 through `image-review.md` | the brief stage is checked |
| `.agents/skills/marketing-craft/SKILL.md:3` description | sharpened: "icons, thumbnails and key art (staged route, ...)" (380 characters) | the skill now covers key art; still says when to load it |
| `.agents/skills/marketing-craft/SKILL.md:18` read-when row "Icon and thumbnail route ..." | sharpened; new row for `image-review.md` | new reference |
| `.agents/skills/marketing-craft/SKILL.md:21` read-when row "Briefs to ..." | sharpened: animator, staged-render maker, what to ask each and when | new hand-offs |
| `.agents/skills/marketing-craft/SKILL.md:34` step 5 "Images. Art lock from the art director, then `image-pipeline.md` steps 1-11 ..." | replaced by step 5 "Images: the key-art route", a pointer to the stages in IP §1 (repair round 1: the a-k list removed, one place for the route) | the old step had no rough round, no green-light content, no order of passes, no crop family or layered master; V6 (review R2) |
| `.agents/skills/marketing-craft/SKILL.md:35` step 6 "Proof capture." | sharpened: ask for captures early (the research board needs them) | our game first in research |
| `.agents/skills/marketing-craft/SKILL.md:48` K-01 | sharpened: roughs judged only at tile size; the grid | work small, judge at the real size |
| `.agents/skills/marketing-craft/SKILL.md:49` K-02 | sharpened: hero mask; where the numbers lie silently | V3 runs: inverted masks, `--box` counts, overwritten sheets, upscales |
| `.agents/skills/marketing-craft/SKILL.md:50` K-03 | sharpened: peak of the action; each concept a different hook | options that differ only in colour are one option |
| `.agents/skills/marketing-craft/SKILL.md:52` K-05 | sharpened: the character's signature key pose from the animator | adopted animator proposal (CD-25) |
| (new) `marketing-craft` SKILL §4 K-12..K-16 | added | stages that freeze, warm-up, one master for the kit, fresh eyes, image budget |
| `.agents/skills/marketing-craft/SKILL.md:70` self-check "Every image: `thumb_check.py` sheet + JSON, checklist, art director note ..." | sharpened (hero mask) + three new lines (MR run and labels, options, budget) | the self-review the agent runs before hand-back |
| `.agents/skills/marketing-craft/references/image-pipeline.md:1` title "Icons and thumbnails: from brief to owner review" | sharpened: "Icons, thumbnails and key art ..." | scope |
| `image-pipeline.md:8` step 1 "Message first" | kept, moved into stage 1 "Brief" and extended (hero, sell list, premise, symbol, fans want, hook, experience, tone, keyword table, crop plan) | brief first |
| `image-pipeline.md:9` step 2 "Art lock" | kept, moved into stage 2 with the research board | reference order: our game first |
| `image-pipeline.md:10-11` steps 3-4 "Manifest", "Generate" | kept, moved into stage 3 (thumbnail round: warm-up, 3-5 hooks, one atypical, judged at tile size) | breadth before polish |
| `image-pipeline.md:12` step 5 "Your own look first: hands, object count, identity vs anchors, scale, fake UI, invented rewards, stray text ... Max 2 regenerations" | kept, split: identity MR-10, scale MR-11, fake UI and rewards MR-25; hands, object and character counts, stray text and merged parts restored in repair round 1 as IR MR-33 (first, once per generated image, on the full-size master); regenerations clarified ("Regeneration vs a new option") | a new idea is a new row, not a regeneration; round 1 had dropped the hands, count and stray-text look (review F4) |
| `image-pipeline.md:13` step 6 "Format ... never stretch (Roblox stretches non-16:9 uploads); record the final px size and whether it reaches 1920×1080; an upscale is recorded as one" | kept, moved: stage 6 (routes a/b: the largest crop of the model's output in the destination's aspect, px size recorded against the ideal, an upscale only as a recorded pass) and MR-29; stage 10 and MR-22 "never stretch", enforced by the crop command (stops on a wrong aspect or a box outside the image) | round 1 had lost "never stretch" and over-promised "at final size" (review F3, R1); restored in repair round 1 |
| `image-pipeline.md:14` step 7 "Title text" | kept as stage 9; brand font and lock-up, one property per event | brand pattern |
| `image-pipeline.md:15-18` steps 8-11 "Measure", "Checklist", "Art director review", "Owner package" | kept; measure runs in every stage; checklist and reviews in stage 11; owner package stage 12 | the route gained stages 4-5 and 7-8 between them |
| `image-pipeline.md:24-25` commands with `--box` | replaced by commands with `--mask` and per-variant `--out-dir` | V3: `--box` counts the boxes given and dilutes contrast; re-runs overwrite sheets |
| `image-pipeline.md:30` "The subject ... Full-scene thumbnails: give `--box` around the hero plus its action" | replaced: a hero mask from a polygon (or a magenta hero pass); `--box` only for a tight region | V3: `--box` gave `component_count` 2 for two boxes on one hero; a hand polygon mask gives real numbers |
| `image-pipeline.md:38` reading row `component_count` | sharpened: with a hero mask; pieces under 0.5 % of the frame are not counted; new row `subject_share_of_frame` read first | V3: an inverted mask is measured with no error |
| `image-pipeline.md:46` "2-5 active thumbnails ..." | sharpened: the live set comes from the round's distinct options | colourways are not concepts |
| `image-pipeline.md:49` "Do not restart within 7 days ..." | sharpened: each refresh keeps the brand pattern, one property changes | the family reads as one game |
| (new) `image-pipeline.md` §4 short commands, §5 worked examples | added | V2 short commands in references; owner spec: worked examples |
| (new) `marketing-craft/references/image-review.md` | added | the self-review list, one line per checkable finding |
| `.agents/skills/marketing-craft/references/channel-kits.md:10` page row "Icon, thumbnails" | sharpened: the family reads as one at real size | brand family |
| `channel-kits.md:17` native video step 1 | sharpened: open on one real action's tell, build, peak, result | cause and effect in the opening seconds |
| `channel-kits.md:24` short video work order | kept; four check bullets added (opening beats, character and brand in motion, sound sync, readable for everyone) | video self-review with named inputs |
| `channel-kits.md:33` events paragraph | kept; event names: one extreme pass, one brand pass | refresh a tone and keep the brand |
| `channel-kits.md:59` owner package item 2 | sharpened: equal finish, labelled, recommendation with reasons, goal questions, the moment in play | present options with a pick |
| `.agents/skills/marketing-design/references/discovery-promise.md:28-29` icon and thumbnail rows | sharpened: Roblox uniqueness and theme lines (docs read 2026-10-22), our standard pointer | docs facts plus the standards |
| `.agents/skills/marketing-design/references/channels.md:18` short-video practice | kept; pointer to the opening-beat check | one rule, one place |
| `.agents/skills/marketing-craft/references/handoffs.md:9-11` partner rows | sharpened (premise, fans want, study grid, anchors per crop, brand pattern, cold read, paint-over); new rows animator, environment-designer or modeler, ui-ux-designer | what to ask each partner and when |
| `handoffs.md:98, 109` art-director brief `fixed`, `open`, `checks` | sharpened: hero and premise fixed; anchors and value plan open; checks C2 (cold read) and C3 (paint-over) | partner review in the right order |
| (new) `handoffs.md` §7 (animator), §8 (staged render) | added | V10 partner consistency (`animation-design/references/game-timing.md` §6; magenta hero pass as in `modeling-craft` icon renders) |

Nothing in the old books was found wrong by the library; no rule was removed except the pointer to the J016 extract.

## d. Command runs (V3), proposals from other roles (V11), binding-skill diff (V4)

Samples (synthetic, the real input types): a two-tone rough on a flat light ground (1920×1080); a full scene with a sky gradient, ground and a mid-value hero (1920×1080); a full-bleed head-and-shoulders icon (1024×1024); a 4:3 master; a master drawn at 480×270 and upscaled to 1920×1080; hand-polygon and designed hero masks; a key-pose black-fill; a phone capture stand-in (1170×2532). Scratch: `<scratchpad>/marketing_v3/`. Tile stand-in 400×225 (no `surfaces.md` exists in the kit).

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| MR-06, MR-07, MR-12, MR-21 | `thumb_check.py thumbnail --size 400x225 --size-source ... --bottom-band 20 --title ...` (auto key) | two-tone rough, flat ground | runs; JSON and sheet written; `component_count` 1, largest share 0.93; three threats at 0.17 % of the frame each not counted (below the 0.5 % floor): right answer |
| MR-07 | same, no subject input | full scene | "not measured: no flat key-colour border": right (no guess) |
| MR-07 | same with one tight `--box` | full scene | measured, count 1, ratio 1.16 (rectangle includes sky) |
| MR-07 | same with two `--box` on one hero | full scene | `component_count` 2 = the number of boxes, no error: **wrong number silently** → book: never read counts from `--box` (IP §2, MR-07) |
| MR-07 | `--box --box-key` | full scene | "not measured: box border is not flat": right |
| MR-07, MR-12 | `--mask` (hand polygon) | full scene | measured; share 0.042; ratio 1.14 (the hero merges with the sky: right) |
| MR-07 | `--mask` inverted (white subject) | full scene | measured, share 0.958, ratio 1.39, no error: **wrong numbers silently** → read `subject_share_of_frame` first (IP §2, MR-07) |
| MR-07, MR-22 | `thumb_check.py icon --title ...` auto key | full-bleed icon | "not measured": right; with `--mask`: measured, share 0.64 (a large icon hero: mask panel decides) |
| MR-22 | `thumb_check.py icon --mask <master-size mask>` on a crop | 512 px crop | **fails, rc 1** (mask size differs) → crop the mask with the same box (IP §4); rerun measured |
| format | `thumb_check.py thumbnail` | 4:3 master | `aspect_16_9` false, stretch 1.333: right |
| MR-29 | `thumb_check.py thumbnail` | upscaled master | `all_met` true: the tool cannot see an upscale → manual 1:1 look + record (MR-29) + tool proposal |
| sheets | two runs, same input and size | full scene | the second run overwrites the first sheet → per-variant `--out-dir` (IP §2) |
| MR-04 | `look_check.py silhouette A --compare B` | two two-tone roughs | IoU 0.12 (different directions); A vs same-shape copy 1.0; full scene vs A: `invalid-mask` (loud): right |
| MR-04, MR-28 | `look_check.py silhouette <img> --mask a --compare-mask b` | hero vs hero minus weapon | aligned IoU 0.06 (the bbox alignment shifts): **misleading for frozen shapes** → MR-28 uses frame IoU instead |
| MR-04, MR-28 | frame IoU short command (IP §4) | the same two masks; hand polygon vs designed mask | 0.78; 0.83 → starting value about 0.8 (two masks of one hero land near 0.8-0.9) |
| MR-09 | `look_check.py silhouette <still> --mask <hero> --compare <key-pose black-fill>` | full scene + black-fill on white | measured, IoU 0.74 |
| MR-15 | `look_check.py palette --k 5 --roles '{...}'` | full scene | runs; the sky gradient splits into 3 clusters (0.22, 0.22, 0.20); the "hero" role matched a sky cluster at ΔE 7.7 → sum clusters by hue family; `--mask` for hero roles (IP §2, MR-15) |
| stage 3 | `art_refs.py --bible templates/skill/art-bible.md print <manifest>` with a "two-tone silhouette rough" identity | thumbnail manifest row | runs; the THUMBNAIL and WORLD STYLE locks ask for the full style, so a flat rough in the identity fights the lock → the book draws masks instead of asking the model for flat roughs; a rough family is proposed |
| IP §4 (all 8 commands) | each command extracted from the book text and run as written | full scene, masks, roughs, phone capture | all rc 0; files written: `.mask.png`, `.mirror.png`, `.grey.png`, `.3value.png`, crop, grid, mock; frame IoU 0.827; profile "none: treated as sRGB" |

Proposal rows from other roles (V11):
- `proposals/animator.md` row "marketing-craft thumbnail and key-art steps: a still states a one-sentence premise and asks the animator for the signature move's key pose": **adopted** (CS §4 K-05, IP §1 stages 1-2, HO table animator row and §7, IR MR-09, DS §4 M-21).
- `proposals/game-designer.md`: no row targets `marketing-design` or `marketing-craft` (read in full); its GD-35 library fix is consistent with my books (DS §7 row 19 shows only tiers players really get; odds stay in `platform-policy`).
- `proposals/modeler.md`: no row targets my books.

Binding-skill diff (V4): the library lines that touch money, paid random items, ads, younger players or player data and reached my books are UP-19 (no rewards or rarities the game does not give, MR-25), GD-35 (a reveal image shows a real tier, MR-25, DS §7 row 19) and CD-29 (a sensitive act carried by a prop motif, MR-27). SI-19 was rejected for marketing (MR-25 shows each tier as it is). CD-01 (non-sexualised designs) and CF-15 (gore in foreground elements) were claimed here in round 1 but had not reached the books (review R4); repair round 1 added them to MR-27: no sexualised pose, costume or body; blood, violence and gore in every layer within the game's content maturity label. Diffed against `platform-policy/references/rules.md` (paid random items, ads, younger players, and the restricted 18+ triggers row: strong violence, heavy realistic blood, romance) and the docs (`production/promotion/content-maturity.md:21`: uploaded images can be moderated whatever the label; `marketplace/marketplace-policy.md:331, 365` on sexually suggestive bodies): no contradiction; MR-27 defers to `platform-policy` ("it wins"); my books add no odds wording and keep `policy-rights.md` §2 and the policy skill as the authority. No library row needed: CD-01 and CF-15 already send their checks to `platform-policy`.

Docs read: `production/publishing/experience-icons.md` (lines 34, 55, 80, 105), `production/publishing/thumbnails.md` (lines 54, 86-117, 150, 215, 220, 239, 277), `knowledge/reference/roblox/docs-map.md` L32 (marketing row).

V5 pass (scripted, `<scratchpad>/marketing_v5_check.py`): every MR, M, K, UP and stage reference in table a exists in the books; every landed row whose library finding has a check names a self-review line (MR, or a check bullet in CK §3-4), or says whose check it is (CR-05: the art director's line in my brief). Worked examples A and B re-read after the subject-input and inverted-mask rules changed.

## e. Repair round 1 command runs (V3)

Scratch: `<scratchpad>/marketing_r1/` (`marketing_r1_make.py` builds the samples; `marketing_r1_cmds.py` extracts every IP §4 command from the book text and runs it as written). Samples: the reviewer's case rebuilt (1920×1080 full scene, dark foreground frame, quiet background of luma about 90 with noise sd 4, bright hero with a round head, thin body and a thin diagonal pickaxe), its true-outline mask, an 8-point coarse polygon, a 4-part traced polygon set, a black-fill symbol at master size, a two-stroke thin symbol, a flat two-value frame.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| MR-07, MR-08 (F1) | polygon-parts command, coarse 8 points vs traced 4 parts | full scene, small hero | both rc 0; frame IoU against the true outline: coarse 0.633, traced 0.894 |
| MR-08 (F1) | overlay command | the two masks on the scene | rc 0, `.overlay.png` written; looked once: the coarse overlay leaves the top of the head and the whole pickaxe untinted and tints background beside the neck; the traced overlay covers every part. A mask of another size stops with "images do not match" (loud) |
| MR-07 (F1) | `thumb_check.py thumbnail --mask` with coarse, traced and true masks | full scene | all rc 0; `component_count` 1 and largest share 1.0 for all three (one polygon, or touching parts, is always one piece, so the count says nothing about the outline: the overlay and the black-fill panel decide); `subject_share_of_frame` 0.0089 / 0.0118 / 0.0099; `subject_ring_ratio` 5.45-5.47 for all |
| MR-13 (F2) | 3-value command (fixed cuts, squinted) | full scene | rc 0, `.3value.png` written; shares dark 0.152, mid 0.838, light 0.010; inside the quiet background 100 % mid (the old percentile command cut at 86 / 89 and split it into three bands); "near a cut" 0.834 because the background sits at luma about 90, next to the 85 cut; re-run with cuts 70 170: same shares, near-cut 0.001, so the groups are real. Without the 4× squint the same background was 12 % dark speckle: the squint and the near-cut share are the guards |
| MR-13 (F2) | 3-value command | flat frame, half 40, half 200 | dark 0.5, mid 0, light 0.5, near-cut 0: right |
| MR-22 (F3) | crop command | full scene | box 800×700 → 512×512: rc 1 "box 800x700 is not 512:512: never stretch"; box 1500,0,2100,600 (leaves the image): rc 1 "box leaves the image" (before this guard PIL padded it with black, rc 0, no warning); 700×700 → 512: rc 0; 1600×900 → 1920×1080: rc 0; one pixel off (1599×900): rc 0 (allowed); 1920×1080 → 1200×900: rc 1 |
| MR-22 | `thumb_check.py icon --mask` on a crop and its mask cut with the same box | 512 crop | rc 0, measured |
| MR-26 (F5) | crop command on the symbol mask (square box), then `thumb_check.py icon <symbol> --key auto` | black-fill symbol on white | rc 0; key auto finds the flat white border (`#FFFFFF`, share 1.0); `component_count` 1, largest share 1.0; master square true |
| MR-26 (F5) | same | two 4 px strokes crossing (a thin symbol) | rc 0; `component_count` 1, share 0.0126 at 150×150: the numbers do not flag a sliver, so the line says the 150×150 tile on the sheet decides. A 1 px erosion share was tried as a sliver number and dropped: it mixes size and thinness (a chunky hero at tile size kept 0.90, the true outline 0.59, the coarse polygon 0.76) |
| MR-10 (R6) | `look_check.py palette <scene> --mask <traced> --k 3 --roles` (the hero colour, an absent variant blue) | full scene | rc 0; the hero colour role ΔE2000 0.0 to its cluster, the absent blue 19.3: a version's signature colour present or absent reads clearly; about 10 % of the traced mask's pixels are edge background (two small background clusters), so on small heroes read the roles, not the cluster shares |
| IP §4 (all 9 commands) | `marketing_r1_cmds.py`: each command taken from the book text and run as written | scene, masks, crop, grid, phone capture stand-in | all rc 0; files written: `.mask.png`, `.overlay.png`, `.mirror.png`, `.grey.png`, `.3value.png`, crop, grid, mock; frame IoU 0.894; profile "none: treated as sRGB" |

V5 pass after the repair (scripted, `<scratchpad>/marketing_r1/marketing_r1_v5.py`): every MR, M, K, UP and stage reference in table a exists in the books (MR-33 included); every row whose library finding has a runnable check names its self-review line (SS-02 → MR-08 on a traced mask, RI-28 → MR-26 symbol, RI-07 → MR-04, SI-18 → MR-10 palette roles). The landed-in locations of every row changed here were opened and read. Worked examples A and B re-read after the mask, value-study and crop rules changed, and updated.

## f. Repair round 1 (review `reviews/marketing-rev1-reviewer.md`, verdict fix-first)

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (MR-08 black-fill circular on a coarse polygon) | IP §2 subject row: full scenes get a hero mask traced as one polygon per part (head, body, limbs, signature item, headgear, each group member) to about one tile pixel, checked once on a new overlay before any number; a coarse polygon "can never pass or fail MR-07 or MR-08" (its count is the number of polygons). IP §4: the polygon command takes a list of part polygons; new overlay command (mask tinted magenta at 50 % over the master). IR MR-08 rewritten (real outline only, names its mask source); MR-07 and MR-11 name the traced mask; IR §1 budget adds one overlay look per newly traced mask; IP §1 stage 3 budget "per rough one sheet + one mask overlay"; stage 5 judges the silhouette on the traced black-fill; CS §6 and RF method 4 say the same in one clause. Worked examples A (the re-traced pickaxe handle shows as a 2 px sliver, fixed at the green light) and B (traced parts) re-written. V3 runs in table e |
| F2 (3-value study cut at percentiles) | IP §4 3-value command: fixed luminance cuts (85 / 170 default, or the bible's value ladder as arguments), computed on the image shrunk 4× (a squint), prints each group's share and a "near a cut" share; reading rule under §4 (a near-cut share above about 0.1: re-run with moved cuts). IR MR-13 reads the printed shares against the plan and the tone. Worked example A re-written with the shares. V3 runs in table e (the reviewer's quiet background is now one group) |
| F3 (crop stretches silently; "never stretch" lost) | IP §4 crop command stops with an error when the box aspect is not the destination's (within one destination pixel) and when the box leaves the image (PIL would pad it with black: found in this round's V3 run); IP §1 stage 10 and IR MR-22 say "never stretch". Table c row for the old step 6 updated |
| F4 (first look for hands, counts, stray text lost) | New IR MR-33, first row of IR §3: generation faults on the full-size master once per generated image (hands and fingers, object and character counts, stray letters, numbers, glyphs, fake logos, merged, doubled or missing parts); a fault is a regeneration (max 2). Placed before MR-06; a new id after the last one so no MR id moved. IP §1 stage 3 check names MR-33; IP "Regeneration vs a new option" points to it; CS §2 and §6 say MR-01..MR-33 |
| F5 (RI-28, RI-07 checks not carried) | RI-07: IR MR-04 adds "each rough's visible elements map to rows of the keyword table, and no row is missing" (input: the sheets already looked at for MR-06). RI-28: IR MR-26 adds the symbol check (traced as a black shape, cropped square with the crop command, `thumb_check.py icon --key auto`, one main piece, named from the 150×150 tile; the numbers do not see a sliver, so the tile decides); IP §1 stage 5 runs it at the green light (budget: symbol sheet 1). Worked example A records it. V3 runs in table e |
| R1 (final size wording) | IP §1 stage 6: routes a/b take the largest crop of the model's output in the destination's aspect, px size recorded against the destination's ideal (thumbnail 1920×1080, icon at least 512×512), an upscale only as a recorded pass with a 1:1 look; IR MR-29 rewritten to match |
| R2 (route written in three places; MR scope) | The route lives in IP §1 only: CS §3 step 5 is a pointer, CS §4 K-12 points to IP §1, RF "Your place" names only what G1 and G2 hold and points to IP §1, RF method 3 is a pointer. IR §1 gains "Which lines run when" (per brief, per round, per stage on every candidate and crop, MR-28 to MR-31 on the render, the full list once on the recommended final); CS §6 points to it. DS §7 rows 4 and 15 kept: they state the principle with an example, not the route |
| R3 (the beat missing) | DS §7 row 8 and CK §2 step 1: "tell, build, beat (the held instant of tension), peak and result"; CK §3 opening-beat check lists the beat's start time and says a re-cut keeps the beat before the peak. Proposals row for `short-video-plan.md` updated to the same five fields. Consistent with `animation-design/references/game-timing.md` §7 |
| R4 (coverage claims not in the books) | IR MR-27 adds "no sexualised pose, costume or body; blood, violence and gore in every layer, the foreground first, within the game's content maturity label" (diffed against platform-policy, which wins; V4 paragraph in table d corrected). MD-02 clause added to IP §1 stage 8; the MD-02, CD-01 and CF-15 rows in table a now say where they land |
| R5 (image cap below stage budgets) | IP §1, line under the stage table: spend a capped brief's images on the earliest open stage and stop at its gate; never thin a round below 3 roughs; masks, overlays, sheets and crops are measurement files, not generated images |
| R6 (MR-10 fails a skin) | IR MR-10: anchors and palette of the version shown (a skin: its own; the base character in a new scene: the base palette, as the brief records); `look_check.py palette --mask --roles` with that version's signature colours (V3 run in table e). IP §1 stage 1 and IR MR-01 add the brief field (new version or the same character) |
| Keep list | Kept: the staged route and its budgets (only stages 3 and 5 gained the overlay and the symbol sheet), hero masks instead of `--box`, the `subject_share_of_frame`-first reading and the inverted-mask warning, frame IoU for MR-28 and MR-04 (the command now uses `n.logical_or` instead of a pipe character so the markdown table does not split; same result in the run), per-variant `--out-dir`, the crop-mask rule, the real-layout mock and the grid, IR labels and "I see stills", DS §4 M-15..M-23 and §7, handoffs §7 and §8, worked examples A and B (re-read; updated only for the traced masks, the fixed-cut study and the symbol), CK §3 checks, RF method 8, the proposals file |
| V11 (rows from other roles) | `proposals/art-director.md` row "marketing: likeness set, recognition anchors, named as inputs from the bible §7" (written after round 1): **adopted**. IP §1 stage 2 names the bible §7 rows I measure against (identity anchors, palette roles, reserved colours, shape vocabulary, theme library with the "fans want" line, tier and format exceptions), each named with the bible revision in the brief, a missing row a ticket to the art director; IR MR-01 (rows used), MR-08 (identity anchors), MR-15 (palette roles, reserved colours), MR-16 (tier and format exceptions) read them. Animator row: still adopted (unchanged) |

## g. Repair round 2 command runs (V3)

Scratch: `<scratchpad>/marketing_r2/` (`marketing_r2_make.py` builds the samples; `marketing_r2_cmds.py` extracts the two CK §3 commands and the IP §4 3-value command from the book text and runs them as written). Samples: a 3 s, 30 fps mp4 (640×360, dark frame, a grey box moving to a contact at frame 45 = 1500 ms; full-screen flashes at frames 45-46 and 60, 64, 68, 72; a half-screen flash at frames 80-82); WAVs at 48 kHz: hits at 1520 and 2000 ms, the same hit 30 ms early (1470), the hits under a loud music bed with a beat every 250 ms, the hits under a quiet bed, a WAV 500 ms short; a 20 s WAV at 44.1 kHz with one hit at 15020 ms (mono, and a quiet stereo copy peaking near -30 dBFS); the reviewer's 3-value scene rebuilt (1920×1080, dark frame left, quiet background luma about 110 sd 4, bright hero).

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| CK §3 frames, flashes (F1) | frame command | 30 fps mp4 | rc 0; 90 stills `f0000_0ms.jpg` .. `f0089_2967ms.jpg` (the time is the frame's own: `f0045_1500ms.jpg` is the contact frame; the name matches the capture rig's, so `clip_metrics.py` could read the folder); changes at 1500, 1567 (the contact flash), 2000-2433 (four flashes), 2667, 2767 (the half-screen flash, mean rise about 105); most flashes in any 1 s 5.0: right (the contact flash + 4 in 1500-2500 ms) |
| CK §3 frames (F1) | frame command | a missing file; an output folder with a non-ASCII name | rc 1 "cannot read"; rc 1 "cannot write frames" (OpenCV on Windows returns False for a non-ASCII path; before the `or sys.exit` guard the failed write turned every frame's grey into 0, a silent wrong flash count) |
| CK §3 sync (F1) | onset command | hits at 1520 and 2000 ms, 48 kHz | rc 0; length 3000 ms (= last frame 2967 + one frame); onsets [1520, 2000]: +20 ms after the contact frame, inside the window |
| CK §3 sync (F1) | onset command | the hit 30 ms early | onsets [1470]: -30 ms, outside -17: right (the window is in ms, as the sound designer's, not "one frame" of a 30 fps edit, which would allow -33) |
| CK §3 sync, music (F1) | onset command | hits under a loud music bed | onsets [1555]: the first hit read 35 ms late and the second missing, no error; at a 6 dB rise the beats every 250 ms appear and one sits exactly on the contact frame (a false PASS). Hence sync only on the WAV without music; the full mix only for the masking check (each stem onset matched within about 10 ms): here 1520 vs 1555 and 2000 missing = masked: right |
| CK §3 sync, quiet bed | onset command | hits under a quiet bed | onsets [1520, 2000]: same as the stem, the masking check passes: right |
| CK §3 sync, timeline | onset command | WAV 500 ms short | length 2500 ms vs the video's 3000: the length rule gives "not verified" (the onsets alone look right: the length line is the guard) |
| CK §3 sync, sample rate | onset command, first draft with a fixed 5 ms step | 20 s at 44.1 kHz, hit at 15020 | the draft printed 15050 (the 220-sample window is 4.99 ms: 30 ms drift at 15 s, no error); the book command uses the real window length: 15016 (one 5 ms step before the onset): right |
| CK §3 sync, level | onset command | quiet stereo copy (peak near -30 dBFS) | onsets []: no onset near the hit, so "not verified", never PASS (loud, not wrong) |
| MR-13 (F2) | 3-value command with cuts: none; 170 85; 100; 15 85; 0 300 | 3-value scene | none and reversed: cuts [85, 170], dark 0.156, mid 0.826, light 0.018, near-cut 0.0 (reversed cuts now sorted); one cut: rc 1 "give two cuts or none"; 0 300: rc 1; 15 85 (the bible's environment band read as cuts): runs, prints cuts [15, 85] and light 0.844, the quiet background as the light group. A command cannot tell a band from a cut, so the reading rule says what the bible's bands are, and the printed cuts make the mistake visible in the record |

V5 pass after the repair: rows CC-02 and VR-26 in table a now name the CK §3 lines with their inputs; CD-09, CD-15, SD-21, UI-16, WT-24 and UP-08 point to CK §3 lines whose input is now the stills of the frame command (opened and read). Worked examples A and B re-read: A uses the default cuts (same result; the output only gained the printed cuts); B is a new game's icon designed on its own, which the stage 1 clause now states as the rule.

## h. Repair round 2 (review `reviews/marketing-rev2-reviewer.md`, verdict fix-first)

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (video checks without a route to their inputs) | CK §3 new "Inputs for the checks below": a frame command (cv2, installed) writes one still per frame named with its time and prints the large changes of mean grey and the most flashes in any 1 s; an onset command (soundfile) reads the cutter's WAV without music and prints its length and onsets; a stills budget (about 12 per edit, 2-3 around each beat and each checked hit). The four checks name their input; the sync line has the partner window in ms (-17 to about +40), a "not verified" path (no WAV, a WAV of another length, no onset near a hit), a measurable masking check (each stem onset matched in the full mix) and says device sync is the sound designer's. Flash line: at most 3 in any second, design for 2 (the effects' rule), red flashes looked at. Both commands run as written (table g); the sample-rate drift and the failed-write case were found there and fixed. Proposal row for a video-and-audio tool mode |
| F2 (3-value cuts not checked) | IP §4 command: stops unless it gets two cuts or none, sorts them, checks 0 < cut1 < cut2 < 255, prints the cuts used; the "art bible's value ladder" wording removed; reading rule: cuts are grey levels, the bible's value bands are per-layer ranges in percent, not cuts. Runs in table g |
| R1 (icon plan unstated) | Agreed. IP §1 stage 1 crop plan: a new game's icon (identity) gets its own brief and roughs in the thumbnail round; an update or event icon is a crop of the master, judged for identity at 150×150 (MR-22). The capped-brief line: icon and thumbnail roughs are two rounds of stage 3, at least 3 each, one shared warm-up under a cap (E1's 8: 1 + 3 + 3 + 1 spare). CS K-14 says it in one clause. The evals proposal row gains the icon plan |
| R2 (K-14 final size) | Agreed. CS K-14: finals at final size (route c) or the largest crop of the model's output with its size recorded (routes a/b, IP §1 stage 6) |
| R3 (light-check budget written three times) | Agreed. Kept in IR §1; RF method 5 and CS K-16 are pointers (to IR §1, the IP §1 stage budgets and the CK §3 stills budget) |
| Keep list | Kept unchanged: the staged route and its budgets (stage 1 and the cap line gained only the icon clause), traced masks and the overlay, the fixed-cut squinted study (now with checked cuts), the crop that refuses to stretch, MR-33, MR-04 keyword rows, MR-26 symbol, MR-10 variant palette, MR-27, hero masks, frame IoU, per-variant `--out-dir`, DS §4 and §7, HO §7 and §8, IR labels and "I see stills", worked examples A and B, the proposals file |
| V11 (rows from other roles) | Re-read every `proposals/*.md`: no new row targets my books since round 1 (the animator and art-director rows stay adopted; the art director's `thumbnail-rough` support row backs my own proposal) |
| V10 (partners) | The sync window and its "not verified" path now match `vfx-design` SKILL (sound line), `animation-design/references/game-timing.md` (sync rule) and `sound-design/references/review.md` R-54; the flash wording matches `vfx-design` (design for 2 or fewer, never more than 3, no saturated red) |

## i. Repair round 3 (review `reviews/marketing-rev3-reviewer.md`, verdict fix-first)

Scratch: `<scratchpad>/marketing_r3/` (`marketing_r3_make.py` builds the edits; `marketing_r3_cmds.py` takes the CK §3 frame command from the book text and the §6 script from the `vfx-craft/references/measure.md` text, saves it as `flash_pulse_vfx.py`, and runs both as written: the frame command on the mp4, the counter on the folder it wrote with the fps it printed; output in `marketing_r3_runs.log`). Edits are mp4 (mp4v) as cv2 writes them; A, B and E rebuild the reviewer's two edits.

| Finding | Fixed where | Test input and result |
| --- | --- | --- |
| F1 (flash count from the whole-frame mean misses red and part-screen flashes, no error) | CK §3: the frame command's flash count removed; its print labelled "whole-frame changes of mean grey, for finding cuts", and the text says it is never a flash count. New "Flashes" bullet: points to `vfx-craft/references/measure.md` §6 (no copy), run on the frame command's folder with its fps; the count over 10 % of the frame, at most 3 in any 1 s, design for 2; the still at every listed onset and every frame-command time looked at; a cut to a bright shot counts; a flash on the first frame is no onset (look at the first stills); red "not verified" unless an analyser measures it. Budget: about 12 stills plus the stills at every listed onset and change. "Readable for everyone" reads the counter. Coverage row VR-26 updated | A, 4 s 640×360 30 fps (dark ground 20; white contact flash at 1000 ms; 4 white flashes 2000-2400; 4 full-screen red flashes 3000-3400, about 8 Hz; a fading flash at 3667): frame command rc 0, 120 stills `f0000_0ms` .. `f0119_3967ms`; counter rc 0, onsets 1000, 2000, 2133, 2267, 2400, 3000, 3133, 3267, 3400, 3667, most in any 1 s 5 (over 3: fail): right. E, the red strobe alone on dark ground 38 (the reviewer's case): the frame command lists no change (the mean moves 38); counter onsets 3000, 3133, 3267, 3400, most 4: right (the old command read 0). B, 2 s, three quarter-screen 38→200 flashes in 1 s: the frame command lists nothing; counter onsets 333, 667, 1000, most 3 (at the limit): right (the old command read 0) |
| F1, other real input types | same lines | C, a vertical Short 1080×1920 at 60 fps, 3 s, textured dark shot, quarter-screen flashes at 0, 250, 500, 750 ms, a hard cut to a bright shot at 1500 and back at 2500: counter onsets 250, 500, 750, 1500, most 3; the flash on frame 0 is no onset (3 for 4 designed, no error), so the book now sends the agent to the first stills; the cut to bright counts once, the cut back none: right. D, three saturated red flashes on a grey-128 ground of the same luminance: counter 0 onsets (no luminance rise: wrong with no error); the frame command lists 333-1067 ms (its grey weights red more) and the still at 333 ms shows the red: hence "look at the stills at every onset and every frame-command time", and red stays "not verified" unless an analyser measures it |
| F1, same kind elsewhere | none found | Every other measuring command in my books re-read for a whole-image mean standing in for a local or colour event: the onset command (energy jump; "not verified" on a quiet WAV), the IP §4 commands (masks, IoU, 3-value cuts, crops: all per pixel, run right in rev3). No other flash or mean-based count in the role, the design books or `image-review.md` |
| R1 (frames land in the repo) | Agreed. CK §3 "Frames and cuts": the frames folder goes in the scratch folder or under `output/` (git ignores it); only the stills looked at are copied into the job folder | the test frames were written to the scratch folder (A 120, C 180 stills) |
| Proposals | Row "flash counter as a tested kit tool" added (supports the vfx-designer's `tools/vfx/flash_count.py` row; adds the marketing cases A-E, a saturated-red measure and a first-frame warning); the video-and-audio row's (a) no longer asks for a second flash count; the short-video template row reads the counter | `proposals/marketing.md` |

## Lead integration fix (2026-10-22, after wave 2 final repair)
| Change | Where | Why |
| --- | --- | --- |
| Flash count: read both counts per the shared counter's known-limits note, not the 10 % count alone | marketing-craft/references/channel-kits.md §3 | The vfx-designer final repair found that with rain or a pan past dark shapes the 10 % count can read too low; the shared counter (`vfx-craft/references/measure.md` §6) now says to read both counts. Consistency fix (brief V6), no craft decision. |

## Proposal sweep (J018 close)

Sweep by the marketing sweep agent · claude-opus-5-5 · high · 2026-10-22. Every row in `proposals/*.md` (other roles) that names `marketing-design`, `marketing-craft` or the marketing role was re-read against the current books; a last grep of every proposals file before hand-back found no further row. Paths relative to `.agents/skills/` (CS = `marketing-craft/SKILL.md`, IP = `marketing-craft/references/image-pipeline.md`, IR = `image-review.md`, HO = `handoffs.md`, CK = `channel-kits.md`, DS = `marketing-design/SKILL.md`).

| proposal file:line | decision (adopted / already in the book / declined) | where or why |
| --- | --- | --- |
| art-director.md:30 | already in the book | IP §1 stage 2 names the `art-review/references/art-bible.md` §7 rows I measure against (identity anchors, palette roles, reserved colours, shape vocabulary, theme library, tier and format exceptions); IR MR-01, MR-08, MR-15, MR-16 read them. The bible has no row called "likeness set": its Identity anchors row (anchors and recognition features) is that input |
| vfx-designer.md:20 | already in the book | CK §3 "Flashes" bullet: the count comes from `vfx-craft/references/measure.md` §6 run on the frame command's folder (no copy); the frame command's list is labelled "whole-frame changes of mean grey, for finding cuts", never a flash count; the still at every listed onset is looked at; red stays "not verified" unless an analyser measures it. "Readable for everyone" reads the counter |
| animator.md:29 | already in the book | CS §4 K-05 (the signature key pose from the animator, not a new pose); IP §1 stages 1-2; HO table animator row and §7; IR MR-09; DS §4 M-21 |
| reference-images.md:24 | adopted | Role body "Reference images": "§4 steps 1-3 (rounds R0-R3) and 'Who generates'" (matches `reference-images` SKILL §4 rounds table) |

Rows that name marketing but target other files (no change in these books): art-director.md:39 and reference-images.md:18 (the `thumbnail-rough` family in the art-bible template: they support my own proposal row); reference-images.md:29 (owner confirmation of medium roughs at G3, the same question as my I-13 row); vfx-designer.md:18 (`tools/vfx/flash_count.py`, which my proposal row supports). Checks after the sweep: role frontmatter md5 unchanged; no SKILL.md or description changed; LF endings.

## Master follow (J018 close)
> Author: J018 close master follow (ui-ux-designer, marketing books) · claude-opus-5-5 · high · 2026-10-22

Source: `library-fixes.md` §2, every row naming `marketing-design` or `marketing-craft` with status "must follow" or "should follow" (the UP-12 row `marketing-design/SKILL.md:104` says "agrees": no change). Paths relative to `.agents/skills/` (IP = `marketing-craft/references/image-pipeline.md`, IR = `marketing-craft/references/image-review.md`).

| master change | book row | done where |
| --- | --- | --- |
| UP-07 general check: reserved-hue pixel share by colour distance (authored and as rendered) outside the things that carry the meaning; a k-means `palette` cannot show it (should follow: reserved colours were judged from `palette` clusters) | `marketing-design/SKILL.md:99` row 7 (check MR-15; the row text and example "the enemy red never goes on the hero" unchanged) | IR §4 MR-15: for each reserved colour the reserved-colour share outside the things that carry the meaning is near 0 and on the hero 0 for the enemy colour, every marked spot looked at, a `palette` cluster never stands in; input adds the marked image when a share is above 0. IP §2: the `palette` sentence says it shows presence, never absence or place; a new "Reserved-colour share" paragraph (screening aid) names the input, the two mask cases, the swatches (bible hex and as painted), the false readings and the test, and points to the art director's one-liner (`art-review/references/look-check.md` §5 line 4), not a copy. IP §4: a hero-only count mask row (the hero mask inverted) |

Run (scratch `<scratchpad>/ui-ux-designer_marketing_up07/`; `ui-ux-designer_marketing_verbatim.py` takes the IP §4 invert line from the book text and the reserved-hue line from the `look-check.md` text and runs both as written). Input: a real generated key art, `content/art/refs/concept/dragonegg-a-nest.png` (1536 × 1024 PNG), with its egg mask `knowledge/jobs/J009-art-director/art/test-a/diag/dragonegg-a-nest-p90-eggmask.png` (dark = egg); its bible draft (`J009 .../art-bible-draft.md` Color roles) keeps the egg's gold for the egg ("never used for: decoration"). Swatches as painted, sampled inside the egg with `contrast --sample`: `#FDBF69` (crack light), `#F3A168` (body); the bible gives no hex. Distance 10.
| Case | Result |
| --- | --- |
| `#FDBF69`, egg mask as the mask argument (outside the egg) | 1.77 % (25,943 px), in torch flames, lanterns and the lantern-lit snow (marked image looked at) |
| `#F3A168`, outside the egg | 4.72 % (69,067 px) |
| hero-only mask (the egg mask inverted by the IP §4 line) | `#FDBF69` 39.4 %, `#F3A168` 49.4 % of the egg (the colour is on its carrier) |
| `palette --k 8 --exclude <egg mask>`, roles egg gold | one cluster `#F1A05B`, 4.6 %, ΔE 9.6 / 3.1: says the gold is present, not where |

Reading: the torches carry the bible's "interactable" gold-lit edge, so this is the false reading the paragraph names (allowed light in the reserved colour counts); the bible decides. Checks: role frontmatter unchanged (role files not touched); no SKILL.md or description changed; no library ID or franchise name added to the books; LF endings; the one-liners run as printed.
