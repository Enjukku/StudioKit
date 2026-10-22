---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2); repair rounds 1 and 2 (stage 3 reviews rev1, rev2)
supersedes: []
---
> Author: J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: environment-designer

Books rebuilt (old state `df13ff4`): `.agents/roles/environment-designer.md` (body only; frontmatter byte-identical), `.agents/skills/environment-design/` (SKILL.md + references; new `references/read-plan.md`, `references/worked-examples.md`), `.agents/skills/environment-craft/` (SKILL.md + references; new `references/measure-captures.md`; evals untouched).

Legend for "landed in": `D` = `environment-design/SKILL.md` (§7 Pn = core principle n), `RP` = `…/read-plan.md`, `PL` = `…/place-reading.md`, `LA` = `…/light-and-air.md`, `AB` = `…/ambience.md`, `RV` = `…/review.md` (§7 lines RD, VB, FL, AM, QV, PS are the self-review checklist), `DG` = `…/diagnosis.md`, `WE` = `…/worked-examples.md`; `C` = `environment-craft/SKILL.md`, `MC` = `…/measure-captures.md` (M1-M11), `SLA` = `…/studio-light-air.md`, `TW` = `…/terrain-and-water.md`, `BS` = `…/blender-to-studio.md`, `HO` = `…/handoffs.md`, `AC` = `…/audit-and-capture.md`, `PF` = `…/performance.md`, `AIP` = `…/ambience-in-place.md`; `R` = the role file.

## a. Findings

All 195 findings tagged `environment-designer` in `matrix.md` have a row (179 landed, 16 rejected with a reason); 12 untagged findings used are at the end. A text in the last column of a landed row is a scope note.

| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| CD-08 | The concept is a blueprint: keep its iconic qualities, decide its gaps, exceed it in 3D | D §3 steps 3-4 (references annotated as spatial targets; elevations against the reference silhouettes); PL PR-02, PR-06; RV §1 step 3 (renders beside the references); RV §7 FL12 | step / self-review check (review order) |  |
| CD-26 | Design a prop or a place as a character | RP §1 "Personality"; PL PR-49; D §7 P10; RV §7 FL5, FL8; WE §1, §3 | step / standard / core principle / self-review check / example |  |
| CF-01 | Big to small: composition first, detail and effects last | D §3 step 7 (passes: blockout → kit → dressing → mechanics → light last); D §7 P4; RV §7 PS2, PS3 | step / core principle / self-review check |  |
| CF-02 | Design and pose for the side the game camera shows | PL PR-22 (props near paths finished on all sides: the camera orbits); D E-01; RV §3 (key views at the game camera); RV §7 FL10 | standard / quality bar / self-review check |  |
| CF-03 | Put detail where the camera distorts least | PL PR-22 (measure the band the camera shows; big forms where the player runs past); RV §7 FL2 | standard / self-review check |  |
| CF-07 | Judge composition on the integrated capture | D §3 step 6 (target slice with characters, effects, UI); RV §3 busiest-moment row; RV §7 RD3 | step / self-review check |  |
| CF-08 | Shape flow points to the focal point, at every scale | PL PR-38; D E-07; RV §7 RD13; D §7 P5 | standard / self-review check / core principle |  |
| CF-09 | Lines on an object lead somewhere and agree with each other | PL PR-38 (lines lead to the goal; remove lines into dead ends); RV §7 RD13 | standard / self-review check |  |
| CF-10 | Converging motion pulls the eye to the focus | — | — | rejected: Converging particle motion is VFX build craft; in the place, ambient motion is kept small, slow and away from sight lines (AB-11), the opposite job |
| CF-11 | After the hit, move the eye on | — | — | rejected: Moving the eye after a hit is effect and shot timing (vfx-designer, film-director); no environment action |
| CF-12 | A value gradient toward the hero | LA LA-16 (ground darker toward the edges, light on the goal); LA §4 VB-b; RV §7 VB3 | standard / self-review check |  |
| CF-13 | A bright focal light can hide a surprise | PL PR-39; RV §7 RD12 | standard / self-review check |  |
| CF-14 | Make the focal point the tallest shape | PL PR-37; D E-07; RV §7 RD13 | standard / self-review check |  |
| CF-15 | Three depth groups: foreground frames, midground carries, background unifies | LA LA-21 (three depth planes; a dark foreground never between the player and play); checked through RV §7 VB7 | standard |  |
| CF-17 | A giant figure behind small heroes sells scale and threat | — | — | rejected: Staging a giant behind small heroes is a shot (film-director, marketing); in play huge parts block the camera; deliberate exaggeration of scale stays under PL PR-15 |
| CF-19 | Small secondary elements carry movement and colour pops along the eye path | PL PR-38 (small accents along the eye path, smaller and lower in contrast than the focus); LA §4 VB-d; RV §7 VB6 (stray saturated share outside the focal elements and eye-path accents, MC M3 second run) | standard / self-review check |  |
| CF-20 | Background patterns are reversible and A/B tested | — | — | rejected: A reversible background pattern is a 2D composition device (UI, marketing); places carry theme cues (PR-49) instead |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | D E-01; D §7 P2; RV §3 (key views at the game camera, lowest and highest setting); RV §7 RD3, QV1 | standard / quality bar / self-review check / core principle |  |
| CR-03 | Solve the problem behind the note; separate goals from tactics | RV §6 (a note that names a fix: restate the problem behind it, then choose the fix); RV §7 PS4 | step / self-review check |  |
| CR-04 | Answer every note with a concrete visible fix; protect the anchor | RV §6 (one record per issue: what must be kept); RV §7 PS4 | step / self-review check |  |
| CR-05 | Give and solve visual notes as paint-overs on a capture | PL PR-32 (visual note answered with a paint-over before the 3D change); RV §6; HO §2, §7 (art director paint-overs); RV §7 PS4 | standard / step / self-review check |  |
| CR-06 | Notes are direct and visual; the maker drives; conflicts go up | LA §3 (who decides; a real conflict goes to the owner); R "Working with other agents"; RV §7 PS4 | standard / self-review check |  |
| CR-08 | Diagnose by layer; "not happy" may mean "not done" | RV §6 (likely cause and its layer); LA §3 (classify the layer); DG (every row); RV §7 PS4 | step / self-review check |  |
| CR-10 | Keep the right mistakes: follow a happy misread | RP §3 (record what is kept from a rejected option); RV §7 PS1 | step / self-review check |  |
| CR-17 | Say what each input can prove; end with a could-not-check list | RV §2 (what each input can prove; every number names capture, setting, viewport); RV §7 header and PS5 (could-not-check list); MC §0, §2 | standard / self-review check |  |
| CC-05 | Share strong motifs across crafts; seek input from several roles | PL PR-50 (a strong motif found by another craft is recorded and reused in the place) | standard | Its check (the motif in every craft's output) is the art director's across crafts; my part is the standard |
| GD-01 | Every asset has jobs: clarity first, then feel, then style | D §1 (the rule above all: backdrop, read first, mood second); D E-08; D §7 P1; RV §7 RD3 | standard / core principle / self-review check |  |
| GD-07 | Art and mechanics must promise the same thing | PL PR-41, PR-33 (collision matches what players see); RV §7 RD6, RD7 | standard / self-review check |  |
| GD-15 | Prove the fun with the crudest prototype before art | D §3 step 5 (greybox walked before any art); C §3 step 3; RV §7 PS2 | step / self-review check |  |
| GD-22 | Find the genre's demands first | D §3 step 1 (intake: camera, devices, players, walk speed); D §7 P13; RV §7 RD1 | step / core principle / self-review check |  |
| GD-23 | The map is the board: map mechanics stay in the background | AB AB-11 (a map mechanic keeps a quiet look outside its planned moments); RV §7 AM1 | standard / self-review check |  |
| GD-25 | Build conflict into the objective; tie it to the world's story | D §3 step 1 (conflict sentence at intake); RP §1 "Job and conflict"; PL PR-30 (world premise); RV §7 RD1 | step / standard / self-review check |  |
| GD-29 | Turn a dead boundary into a risk and reward | PL PR-34 (the hazard is dressed from the game designer's sheet); RV §7 RD8 | standard (dressing only) / self-review check | Designing a risk-and-reward spot is the game designer's decision (game-design spaces.md §5); only its dressing lands here |
| GD-31 | Art stays inside the blockout's gameplay | D E-02; PL PR-01, PR-03; BS §7; RV §7 RD9; D §7 P15 | standard / step / self-review check |  |
| GD-32 | Hide small secrets that reward discovery | PL PR-51; RV §7 RD12 | standard / self-review check |  |
| GD-33 | A map is never done; new worlds are an escape | D E-11 (each new world clearly new); RV §7 FL8 (beside earlier stages reads as somewhere new) | standard / self-review check |  |
| LC-01 | Reserve the gameplay colours; keep them, and fast motion, out of decoration | D E-16; LA §4 VB-c; AB AB-11; HO §5; RV §7 VB4 (pixel share in environment boxes, MC M3), AM1; WE §2 | standard / self-review check / example |  |
| LC-02 | Keep a colour-role table: one hue never means both help and harm | LA §4 VB-c (the art bible's reserved-colour table); HO §7 (asked from the art director); RV §7 VB4 (MC M3) | standard / self-review check |  |
| LC-03 | Colour sets the mood; recolour every reused layer to it | LA §4 VB-e (a reused piece or material is recoloured to this stage's palette and mood); RV §7 VB11 | standard / self-review check |  |
| LC-04 | Few colours with roles: about 60 / 30 / 10, after the greys work | LA §4 VB-e (dominant theme hue, support, accent); RV §7 VB6 (saturation held to the focal elements and accents) | standard / self-review check |  |
| LC-05 | Take new colours from the palette already in the image | LA §4 VB-e (a new material takes its colour from the palette roles already in the place; "inside the family"); RV §7 VB11 (no palette cluster on the zoo's lit faces far from every bible palette role as rendered under the same light by its reference block, on each look's capture and a neutral-light capture, MC M12; repair round 3), VB12; D §7 P11 | standard / self-review check |  |
| LC-06 | Put the environment's bounce colour into character shadows | C C-16 (Ambient and ColorShift_Bottom carry a hint of the ground's colour); RV §7 VB8 | standard / self-review check |  |
| LC-07 | Shift hue for shadows and highlights; do not just add black or white | LA §4 VB-e (shadow areas shift hue through tinted ambients); C C-16; SLA §1 step 4; RV §7 VB8 (M11), VB12 (metal keeps chroma in shadow, M11) | standard / self-review check |  |
| LC-08 | Light and shadow get opposite temperatures | LA LA-17; C C-16; SLA §1 step 4; RV §7 VB8; MC M11 | standard / self-review check |  |
| LC-09 | No flat fills: small hue and value shifts inside a material | LA §4 VB-e; D E-20; RV §7 VB12 (passes only on `hue_spread`; value texture in one hue fails as `monochrome`, MC M3 §3); LA §4 VB-e (Roblox remedies: hue-shifted part Colors, MaterialVariant or SurfaceAppearance ColorMap, terrain patches of materials whose MaterialColors differ in hue); D §7 P12; WE §3 (silt and damp patches as hue shifts) | standard / self-review check |  |
| LC-10 | One fixed light direction for the whole game, judged at the game camera | LA LA-15; C C-15; SLA §1 step 2; RV §7 VB8 | standard / self-review check |  |
| LC-11 | Block light and shadow first; test lighting options on the rough | D §3 step 5 (grey pass: 2-3 sun positions on the greybox); C §3 step 4; RV §7 VB8; WE §1 | stage / step / self-review check / example |  |
| LC-12 | Light leads the eye: the brightest area is the focus | LA LA-16; D E-08; RV §7 VB3; D §7 P3 | standard / self-review check / core principle |  |
| LC-13 | Light motivated by the setting | LA LA-04 (sharpened: outdoors sky plus sun; sources motivate light); RV §7 VB8 (every local light has a visible source) | standard / self-review check |  |
| LC-14 | Light direction sets good or evil | LA LA-19 (a threatening place lit from below by a source it has; safe or sacred from above); RV §7 VB8 | standard / self-review check |  |
| LC-15 | Rim light separates figures from the background | — | — | rejected: Rim light on characters is cutscene and marketing craft; in play Highlight is capped and not a fix for a weak read (SLA §9) |
| LC-16 | Fix the light per level and tune shadows for readability | LA LA-18; LA §4 VB-a (character separation target); RV §7 VB9 (MC M6) | standard / self-review check |  |
| LC-17 | Calm the field, pop small saturated accents | LA §4 VB-d; RV §7 VB6 (stray limit, MC M3 second run); WE §2 | standard / self-review check |  |
| LC-18 | Keep the player band neutral; tame bright hazards | D E-16; LA §4 VB-a (character target), VB-c, VB-d (neutral limit); SLA §9 hazard glow; RV §7 VB5 (MC M4), VB13 (MC M6); WE §2 | standard / self-review check / example |  |
| LC-22 | Review with colour in, then rebalance | LA §4 VB-g; RV §7 VB3 (re-run after a change) | standard / self-review check |  |
| LC-23 | Iterate colour globally; colourways are the same object | SLA §9 (colour tries are global first; re-check focus and band); RV §7 VB3 | step / self-review check |  |
| LC-24 | Check colour on a phone before it ships | LA LA-07 ("and on a real phone"); HO §6 (studio operator device checks); RV §7 QV2 | standard / self-review check |  |
| MD-01 | Indicate detail; do not spell it out | PL PR-44, PR-47 (cover cut to a whisper; backdrop indicated, not spelled out); RV §7 FL2 | standard / self-review check |  |
| MD-02 | Budget detail by display size, camera distance and player speed | PL PR-22 (detail by display size and speed); RV §7 FL2 | standard / self-review check |  |
| MD-03 | Finish comes from crisp edges and planes, balanced with soft | BS §1 row (one-off Blender pieces follow `modeling-design` finish standards); RV §7 FL13 | standard (pointer) / self-review check |  |
| MD-05 | Start texturing from baked AO and curvature; drive variation by rules | PL PR-48; TW §4 (materials by slope and height from one script); BS §1 pointer (baked AO and curvature); RV §7 FL11 | standard / step / self-review check |  |
| MD-06 | Material maps sell the surface; push, then pull back | BS §1 pointer; LA §4 VB-f (materials judged under the stage's final light); RV §7 FL13, VB11 | standard (pointer) / self-review check |  |
| MD-07 | Choose materials and lighting together | LA §4 VB-f; C §3 step 7; SLA §9 material zoo; RV §7 VB11 | standard / step / self-review check |  |
| MD-08 | Test a new material on a small patch first | LA §4 VB-f; SLA §9 (material zoo = the test patch per material); C C-18; RV §7 VB11 | stage / standard / self-review check |  |
| MD-09 | Wear and condition tell the story | PL PR-43 (wear where hands and feet go); RV §7 FL5; WE §3 | standard / self-review check / example |  |
| MD-10 | Controlled imperfection makes it hand-made | D E-20; LA §4 VB-e; RV §7 VB12 (MC M3 §3: `hue_spread` above its limit; `monochrome` fails) | standard / self-review check |  |
| MD-12 | Functional parts and visible support make objects believable | — | — | rejected: Functional parts and visible support on props are the modeler's craft (modeling-design); I place the props |
| MD-13 | Ground every object: base, blended seams, colour bleed | D E-19; PL PR-45; C C-20; TW §4; RV §7 FL6 | standard / self-review check |  |
| MD-14 | Gold stays saturated in shadow | LA §4 VB-e (gold and warm metals stay saturated in shadow); RV §7 VB12 | standard / self-review check |  |
| MD-15 | Cracks taper; one width looks man-made | BS §1 pointer (one-off pieces follow the modeler's material standards); RV §7 FL13 | standard (pointer) / self-review check |  |
| MD-16 | A few small glints sharpen hard materials | BS §1 pointer; RV §7 FL13 | standard (pointer) / self-review check |  |
| MD-17 | One trim sheet with a normal map can dress a whole environment | BS §1 row (bespoke shells share one trim sheet); C C-21 (trim-sheet SurfaceAppearance as a package); D E-12; RV §7 FL13 | standard / self-review check |  |
| PP-01 | Set triangle and texture budgets before building; phones first | D E-14; RV §5 (budgets measured, never invented); RP §2 (rank decides where triangles go); RV §7 QV3 | standard / self-review check |  |
| PP-03 | Put detail in textures, not polygons | BS §1 pointer ("detail in textures"); RV §7 FL13 | standard (pointer) / self-review check |  |
| PP-04 | Keep texel density consistent across assets | BS §1 pointer ("texel density matching the kit"); RV §7 FL13 | standard (pointer) / self-review check |  |
| PP-05 | Mirror UVs on symmetric parts; unique UVs where story detail goes | BS §1 pointer (modeling-design UV rules); RV §7 FL13 | standard (pointer) / self-review check |  |
| PP-06 | When geometry changes, re-project; marry texture and geometry last | BS §1 pointer; RV §7 FL13 | standard (pointer) / self-review check |  |
| PP-07 | Project the concept onto the model as a starting texture | BS §1 pointer; RV §7 FL13 | standard (pointer) / self-review check |  |
| PP-08 | For stylised assets, a low-poly painted workflow keeps changes cheap | BS §1 pointer; BS §7 step 4 (packages update copies); RV §7 FL13 | standard (pointer) / self-review check |  |
| PP-09 | Keep separable parts separate, then judge them together | BS §4 "Named collections only" (kept); C C-21 (named, switchable folders); RV §7 FL13 | standard / self-review check |  |
| PP-10 | Paint across joined meshes so joins disappear | C C-20; TW §4 (seams disappear); RV §7 FL6 | standard / self-review check |  |
| PP-11 | Clean meshes, clean collision, organised UVs | C §3 step 3 (collision as simple boxes); C C-10; RV §7 RD7, RD9 | step / self-review check |  |
| PP-24 | Kits for repeated layouts, unique shells for bespoke ones; no visible duplicates | D E-12; BS §1 (kit vs bespoke shells row); PL PR-20; RV §7 FL3 | standard / self-review check |  |
| PP-25 | Reuse first: search the zoo and existing effects before making new | D E-12 ("a shared prop kit first"); C §3 step 6 (ask the modeler; import each asset once); RV §7 PS5 | standard / self-review check |  |
| PP-26 | Environment order: blockout, composition, kit, dressing, mechanics, then light and polish | D §3 step 7; C §3 steps 3-11 (zoo, dress, then look, then ambience); D §7 P4; RV §7 PS2 | step / core principle / self-review check |  |
| PP-27 | Block out on a grid; snap the art to the approved blockout | C §3 step 3 (fixed snap grid); BS §7; RV §7 RD9 | step / self-review check |  |
| PP-29 | One owner per file or area; clear names on every submission | R "Write scope"; C §5 (one Studio driver; test place); SLA §9 (zoo in its own named folder); RV §7 PS2 | standard / self-review check |  |
| PP-30 | Fix naming and folders before production | AIP §1 conventions (kept); SLA §9 (zoo folder named, outside the stage root); RV §7 AM2 | standard / self-review check |  |
| PP-32 | One key art feeds a whole asset kit; deliver switchable layers | C C-21 (lights, effects and dressing in named folders that can be switched off); RV §7 VB10 | standard / self-review check |  |
| PI-01 | The cheapest stage goes first; expect big changes while it is rough | D §3 order; D §7 P15; RV §1 step 2 (layout problems cheapest in the greybox); RV §7 PS2 | step / core principle / self-review check |  |
| PI-02 | Gates freeze decisions: rough, approved direction, materials, polish | D §3 gates; RV §7 PS2 | step / self-review check |  |
| PI-04 | Block out first, in the engine, and play it before detail | D §3 step 5; C §3 step 3 (walked with the real avatar at walk speed); RV §7 PS2 | stage / step / self-review check |  |
| PI-05 | Work small early so only big shapes can be judged | RP §3 (options at the same low finish and small size); RV §7 PS1 | step / self-review check |  |
| PI-06 | Work in passes over the whole; big things before small | D §3 step 7 (passes over the whole stage); RV §7 PS3 | step / self-review check |  |
| PI-08 | Find the right number by bracketing | D §3 step 5 and C §3 step 4 (2-3 sun positions); SLA §8 (bracket each key value); RV §7 VB8 | step / self-review check |  |
| PI-09 | Not precious: most attempts fail, so delete, redo and let go | RV §6 "Rebuild, do not patch"; RV §7 PS4 | step / self-review check |  |
| PI-10 | Park a stuck part and come back | — | — | rejected: Parking a stuck part adds little to a whole-stage pass order that already moves breadth first (RV §6); kept out to keep the book short |
| PI-11 | A time box forces the readable choice | RP §1 "Stop criteria and pass budget"; D §3 step 2; RV §7 PS5 | step / self-review check |  |
| PI-12 | Know when it is done: written stop criteria, repeating notes | RP §1; RV §7 PS5; D §7 P18 | quality bar / self-review check / core principle |  |
| PI-15 | Decisive marks: few bold decisions, not many small tweaks | — | — | rejected: A painting habit; in the place the same idea is "one named problem per pass" (RV §6) |
| RI-01 | Concept work solves a problem; it is a functional vehicle, not a nice picture | PL PR-02 (an image is an annotated target, not a picture); RP §3 (pick by the read plan); RV §7 PS1 | standard / step / self-review check |  |
| RI-03 | Know the problem, the constraints and the end before making anything | D §3 steps 1-2; RP §1; RV §7 RD1; D §7 P13 | stage / step / self-review check / core principle |  |
| RI-05 | Research first; one narrow moodboard with pillars and key features | D §3 step 3; RP §3 "Research first"; RV §7 PS1 | step / self-review check |  |
| RI-06 | Each theme gets a library: shorthand motifs, iconography, a name and a logo | PL PR-49 (theme cues); RP §1 "Theme cues"; RV §7 FL8 | standard / self-review check |  |
| RI-07 | Turn each keyword into visual facts before prompting | RP §3 "Keyword table"; D §3 step 3; RV §7 PS1 | step / self-review check |  |
| RI-08 | Reference order: our game first, then the real world, then mix; take ideas, never copy | RP §3 (real-world reference, then the game's anchors; take ideas, never a design); RV §7 PS1 | step / self-review check |  |
| RI-10 | Study the real thing closely for the details invention misses | RP §3 (note one specific detail per reference); D §3 step 3; RV §7 PS1 | step / self-review check |  |
| RI-14 | Learn light placement from painted art | — | — | rejected: Curating painted anchors for light placement is the art director's; my light follows the art bible's key direction (LA-15) |
| RI-16 | Research, explore wide and loose, iterate on one or two, finish only what the next maker needs | RP §3 (research, three directions, pick, refine only after the pick); RV §7 PS1 | step / self-review check |  |
| RI-18 | Each option gets its own hook from a different source | RP §3 (each direction from a different source or reading); RV §7 PS1; WE §1 | step / self-review check / example |  |
| RI-19 | Present options with your pick and the reasons; then iterate | RP §3 "Pick with reasons"; HO §7 (art director picks); RV §7 PS1; WE §1 | step / self-review check / example |  |
| RI-22 | Vary one element per option, label them, merge the best two | RP §3 (a second round varies one named element of the pick and merges the strongest two); RV §7 PS1 | step / self-review check |  |
| RI-23 | Bring in one unexpected element from outside the genre | RP §3 (one deliberately unexpected direction taking an idea from outside games); RV §7 PS1 | step / self-review check |  |
| SS-01 | Silhouette first, then light that shows form, detail last | D §3 step 5 (greybox shapes, then grey value and light pass, detail later); RV §7 PS2 | stage / self-review check |  |
| SS-03 | Break the silhouette with few broad cuts, not small notches | PL PR-27, PR-37 (organic landmark silhouette protected; unique landmark silhouette); RV §7 RD13 | standard / self-review check |  |
| SS-04 | Keep the few identifying elements, make them chunky, cut the rest | D E-07 (2-3 iconic traits that read at play distance); RV §7 FL12 | standard / self-review check |  |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | PL PR-38 (directional shapes), PR-50 (sharper where the place threatens, softer where safe); RV §7 FL8 | standard / self-review check |  |
| SS-06 | One shape vocabulary for the whole game, down to the small shapes | PL PR-50; RV §7 FL8; D §7 P11 | standard / self-review check / core principle |  |
| SS-07 | Big, medium, small: never two shapes the same size | PL PR-46; D E-20; RV §7 FL4 | standard / self-review check |  |
| SS-08 | Slopes make direction; tilt shapes along the action | PL PR-38 (slopes and tilted shapes lean toward the goal); RV §7 RD13 | standard / self-review check |  |
| SS-17 | Repeat one motif at several scales | PL PR-50 (motif reused), PR-49 (theme cues across ground, rocks, debris); RV §7 FL8 | standard / self-review check |  |
| SS-20 | Backdrop pieces: simple surfaces, elegant gesture | PL PR-47; TW §4 (cards few, at edges); RV §7 FL2 | standard / self-review check |  |
| SD-02 | Every cue names its emotion, not only its object | AB AB-13; HO §4 (`emotion` per zone); RV §7 AM2 | standard / self-review check |  |
| SD-03 | Ambience, foley and one signature element put the player in the world | AB AB-02 (kept), AB-14 (one signature element), AB-15 (footsteps); RV §7 AM2, FL9 | standard / self-review check |  |
| SD-09 | Set how far each sound carries by its importance | AB AB-04b (every positional source ends somewhere; the sound designer sets it), AB-17; RV §7 AM2 | standard / self-review check |  |
| SD-10 | Far sounds lose their highs first | AB AB-17; AB §2 request example; RV §7 AM2 | standard / self-review check |  |
| SD-13 | Reverb and delay place the sound and glue its layers | AB AB-08 (sharpened: never dry where the space is large); HO §4 avoid list; RV §7 AM2 | standard / self-review check |  |
| SD-18 | Pass-bys make travel; let the engine move real projectiles | — | — | rejected: Pass-bys and engine Doppler are the sound designer's craft; the map only names the moving source |
| SD-20 | Build long, varied beds from spliced takes | — | — | rejected: Building long varied beds is the sound designer's craft; AB-03 (not one global loop) is my side |
| SD-23 | Every floor material is a footstep callout | AB AB-15; D E-18; AIP §4 step 6; HO §4 (`floor_materials`, C3); RV §7 FL9 | standard / step / self-review check |  |
| SI-01 | Style sets the emotional tone: set each lever on purpose | PL PR-28 (the art bible's levers are a versioned input); PL PR-50 (one stylisation level); RV §7 FL8 | standard / self-review check |  |
| SI-02 | Every shape and colour has a job in conveying the idea | PL PR-17 (dressing is evidence: every cluster has a reason); RV §7 FL5 | standard / self-review check |  |
| SI-03 | Theme fit can rule out an otherwise cool idea | RP §3 (an option that reads as another genre or tone loses); WE §1 (option B); RV §7 PS1 | step / example / self-review check |  |
| SI-04 | Theme cues so a place is not generic | PL PR-49; D E-11; TW §4; RV §7 FL8 | standard / self-review check |  |
| SI-07 | Decide the stylisation level; hint at reality, do not copy it | PL PR-50; RV §7 FL8 | standard / self-review check |  |
| SI-09 | One palette per group so a roster reads as a team | — | — | rejected: Group palettes for rosters are the art director's; zones and team bases are told apart by identity symbols and landmarks (PR-37) |
| UI-06 | One UI ecosystem with written rules for meaning | LA §4 VB-c (the same reserved-colour table that UI and gameplay effects use); PL PR-36; RV §7 VB4 | standard / self-review check |  |
| VC-01 | Fix a weak read with contrast, not detail | RV §6 "Contrast before detail"; DG flat row; RV §7 PS4 | step / self-review check |  |
| VC-02 | Values first, colour second; keep a grayscale proof at every step | D §3 step 5 (grey value pass); C C-19 (grey view from the capture); MC M1; RV §7 VB3, VB10 | stage / standard / self-review check |  |
| VC-03 | Separate parts by value and shape, not by lines | SLA §9 (Highlight is not a fix for a weak read); RV §7 VB10 | standard / self-review check |  |
| VC-04 | Make one spot the focus by lowering contrast everywhere else | LA §4 VB-b; DG flat row; RV §7 VB3; D §7 P3 | standard / self-review check / core principle |  |
| VC-05 | Give each screen layer its own value and saturation band | D E-15; LA §4 VB-a (band values by pointer to `art-review/references/art-bible.md` §7), VB-f (material zoo); SLA §9; MC §0 (units); RV §7 VB1, VB11 | standard / quality bar / self-review check |  |
| VC-06 | Test every character against every background | PL PR-10 (typical avatar colours); AC §2 (dummies in light, dark, saturated colours); RV §7 VB2, VB9, FL1 | standard / self-review check |  |
| VC-07 | Reserve white, black and the highest contrast for small focal spots | LA §4 VB-a (no pure black, no large white); C C-17; RV §7 VB1 (M2) | standard / self-review check |  |
| VC-08 | Head, shoulders and hands carry the character read; quiet the lower body | LA §4 VB-a (the ground stays in the environment band; character separation target); RV §7 VB2 (lower body boxed apart against the ground, MC M6) | standard / self-review check | Spending contrast on head and shoulders is the modeler and art director craft; my share is a ground the legs separate from |
| VC-09 | Form shadows make a still object read as 3D | BS §1 pointer (form and finish of one-off pieces follow modeling-design); RV §7 FL13 | standard (pointer) / self-review check |  |
| VC-10 | Shade with a clear terminator, shadows only where the form turns away | BS §1 pointer; RV §7 FL13 | standard (pointer) / self-review check |  |
| VC-11 | Paint contact shadows where parts touch | PL PR-45 (thin dark contact shadow); RV §7 FL6 | standard / self-review check |  |
| VC-13 | Big soft shading first, then commit with sharp, high-contrast accents | BS §1 pointer; RV §7 FL13 | standard (pointer) / self-review check |  |
| VC-14 | Group detail in close values; frame the group with the strongest colour | BS §1 pointer (asset-level value grouping is the modeler's); RV §7 FL13 | standard (pointer) / self-review check |  |
| VC-15 | Space high-contrast features like letters in a word | LA §4 VB-b (bright marks in deliberate groups, no shimmering rows or lone outliers); RV §7 FL2 | standard / self-review check |  |
| VC-16 | Balance visual weight on purpose | — | — | rejected: Balancing visual weight is a fixed-frame composition rule; my views move with the camera, so the focus rank (VB3) does the job |
| VC-17 | High contrast for dramatic moments, lower for calm ones | LA LA-19; RV §7 VB7 | standard / self-review check |  |
| VR-02 | Rank every effect's layers: primary, secondary, tertiary | AB AB-11 (decorative motion is the lowest tier: small, slow, low in brightness); RV §7 AM1 | standard / self-review check |  |
| VR-07 | Never cover what the player needs to see; stay low | AB AB-11 (out of the route, hazard silhouettes and sight lines); HO §5; RV §7 AM1 | standard / self-review check |  |
| VR-10 | A volume reads solid: close the gaps between sprites | — | — | rejected: Building solid smoke and cloud volumes is VFX craft |
| VR-14 | Repeated objects: random rotation and size, no constant spin | PL PR-20 (repeats vary in rotation and scale); RV §7 FL3 (+ 3-4 captures along the camera path for a repeated facade) | standard / self-review check |  |
| VR-15 | Build piles from lifetime overlap, inside the play area | — | — | rejected: Particle piles are VFX craft |
| VR-16 | Ambient environment effects: tiny, slow, partly hidden | AB AB-11; C C-22; HO §5; RV §7 AM1 | standard / self-review check |  |
| VR-25 | Randomise decoration only; lock what carries meaning | D E-20 (variation never touches what carries meaning); RV §7 RD5, RD8 | standard / self-review check |  |
| VH-01 | Rank what must be seen; UI and VFX first, characters second, environment last | D E-15; RP §1 (ranked reads per key view); RV §7 VB2 | standard / step / self-review check |  |
| VH-03 | Less is more: the fewest shapes and colours that give the strongest read | D E-17; PL PR-47; D §7 P6; RV §7 FL2 | standard / core principle / self-review check |  |
| VH-04 | Judge noise in motion, with lighting and effects on | D §3 step 6 (target slice with effects and UI); RV §3 busiest-moment row (operator play capture); RV §7 RD3 | step / self-review check |  |
| VH-05 | Clump detail in a few places; leave areas of rest | PL PR-19; RP §1 "Detail spots"; RV §7 FL2 | standard / self-review check |  |
| VH-07 | Recognisable in under a second beats unique | PL PR-37 (landmark silhouettes unlike each other); RV §7 RD13 | standard / self-review check |  |
| VH-09 | Plan the read order: primary, secondary, tertiary | RP §1 (ranked reads and focal point per key view); RV §7 RD2, VB3 | step / self-review check |  |
| VH-11 | Review in a fixed order: balance, proportion, weight, then contrast and detail | RV §6 "Order" and "One named problem per pass, the worst first"; RV §7 PS4 | step / self-review check |  |
| WL-01 | Gameplay readability beats beauty; test it in the busiest moment | D §1 (the rule above all); D E-01; LA §4 VB-a (separation targets); RV §7 RD3 (MC M6); D §7 P1 | standard / self-review check / core principle |  |
| WL-03 | Every piece says "what I am" and "what you can do here" | PL PR-41; D E-18; RV §7 RD6 | standard / self-review check |  |
| WL-04 | One gameplay constraint, many fictional answers | PL PR-33; RP §4; D §3 step 4; RV §7 RD7 | standard / step / self-review check |  |
| WL-05 | Hazards explain themselves | PL PR-34; D E-18; RV §7 RD8; WE §2; DG hazard row | standard / self-review check / example |  |
| WL-06 | Rank the environment work: it is 90 % of the screen | RP §2; RP §1 "Ranked work list"; D §3 step 2; HO §7 (agreed with the game designer); RV §7 RD1, PS3 | stage / step / self-review check |  |
| WL-07 | The first view tells where you are and what to do | PL PR-35; D §3 step 4 (first view from spawn); RV §7 RD2; RV §3 first-frame row | standard / self-review check |  |
| WL-08 | Spawns first, then the route to the objective | C §3 step 3; D §3 step 5 (spawns, then the route to the objective, then side areas); RV §7 PS2 | step / self-review check |  |
| WL-09 | Paths face forward; no doubling back in multiplayer maps | — | — | rejected: Route direction is the game designer's decision (game-design spaces.md §3, level-design); my lines only follow the approved route |
| WL-11 | One orientation convention across all maps | D §3 step 1 (orientation conventions at intake); RV §7 RD2; D §7 P7 | step / self-review check / core principle |  |
| WL-12 | Mark objectives on the approach and in the floor | PL PR-36; RV §7 RD5 | standard / self-review check |  |
| WL-13 | Head-height cues and directional patterns guide the eye | PL PR-38 (eye-height trim where the game designer asks; directional patterns); RV §7 RD13 | standard / self-review check |  |
| WL-14 | Flat play spaces; every height change is intentional | D E-05; PL PR-48; TW §4; RV §7 FL11 | standard / self-review check |  |
| WL-15 | Predictable geometry: players lose to opponents, not to the map | C §3 step 3 (collision as simple boxes); C C-10; RV §7 RD7 | step / self-review check |  |
| WL-16 | Name dead space and oversized areas in self-review | D §3 step 5; C §3 step 4; RV §7 RD11; WE §1 | stage / self-review check / example |  |
| WL-17 | In a themed game, the blockout already reads as a place | C §3 step 3 (shapes that already read as the theme's structures); D §3 step 5; RV §7 PS2 | step / self-review check |  |
| WL-18 | Materials follow gameplay rules | PL PR-41; D E-18; RV §7 RD6, FL9 | standard / self-review check |  |
| WL-19 | Floors stay clean enough for the smallest gameplay object | D E-17; PL PR-44; TW §4; RV §7 FL1; MC M5; WE §1; DG lost-pickups row | standard / quality bar / self-review check / example |  |
| WL-20 | It must read at the lowest graphics setting | LA LA-07; RV §3; RV §7 QV1, VB10; MC M9 | standard / self-review check |  |
| WL-21 | Scale: a player-sized reference in every blockout and scene | D E-04; PL PR-42; RV §7 FL7; D §7 P9 | standard / self-review check / core principle |  |
| WL-22 | Environmental storytelling: someone lives here, time has passed | D E-10; PL PR-43; RP §1 "Story facts"; RV §7 FL5; WE §3; DG dead row | standard / step / self-review check / example |  |
| WL-23 | Give each zone or team an identity symbol | PL PR-37; RV §7 RD13 | standard / self-review check |  |
| WL-24 | Build and judge the whole space, not only the hero prop | HO §3 (in-set capture before a piece is accepted); C §3 step 6; RV §7 FL12 | step / self-review check |  |
| WL-25 | Distance lowers contrast and detail (atmospheric perspective) | LA LA-20; RV §7 VB7; MC M1 | standard / self-review check |  |
| WL-26 | A small, low-contrast busy background adds life | LA LA-20 (far life small and low in contrast); RV §7 VB7 | standard / self-review check |  |
| WL-27 | A few upright grass cards give the ground depth | PL PR-47; TW §4; RV §7 FL1 | standard / self-review check |  |
| WL-28 | Work from far away; zoom out every round | RV §3 (key views at the game camera); RV §7 QV2; MC M10 | quality bar / self-review check |  |
| WL-29 | Plan routes in player metrics: seconds at walk speed, ledges against jump height | D §3 step 1 (route table in seconds at intake); PL PR-40, PR-12 (jump measured); RV §7 RD10 | standard / self-review check |  |
| WL-30 | Score a level review on ten fixed checks | RV §4 (fixed list re-rated every round, no point totals); RV §7 | self-review check | The 0-2 score and total out of 20 are not adopted: the kit's reviews give no point totals (level-design §6) |
| VR-20 | The drawn danger area is the real hit area, from warning to last tick (untagged) | PL PR-34 (the drawn danger edge never overstates or understates the real one); RV §7 RD8 | standard / self-review check |  |
| VR-23 | Every intense channel has an off path that keeps the information (untagged) | AB AB-16; HO §5; RV §7 AM3 | standard / self-review check |  |
| VR-26 | Pulse and blink rates carry meaning: slow is safe, fast is urgent, never above 3 Hz (untagged) | AB AB-16 (at most 3 flashes a second over large areas); RV §7 AM3 | standard / self-review check |  |
| GD-30 | Every hazard has written rules (untagged) | PL PR-34 (the look follows the game designer's hazard sheet); D §3 step 1; RV §7 RD8 | standard / step / self-review check |  |
| PI-07 | One named problem per pass; fix the worst first (untagged) | RV §6 "One named problem per pass, the worst first"; WE §3; RV §7 PS4 | step / example / self-review check |  |
| CR-02 | Ask a goal question, never "do you like it?" (untagged) | HO §2 (ask the goal question, not "do you like it"); RV §7 PS1 | step / self-review check |  |
| CR-09 | Fresh eyes: flip the image, change the reviewer (untagged) | RV §7 QV4; MC M10 (mirrored and grey first view) | self-review check |  |
| CR-13 | Close with an honest recap of your own result (untagged) | RV §7 PS5 (3 weakest points, could-not-check list) | self-review check |  |
| RI-02 | Show options at equal, low finish on a clean, labelled sheet (untagged) | RP §3 (options at the same low finish, same camera, labelled); RV §7 PS1 | step / self-review check |  |
| RI-17 | Take the big swings at concept stage (untagged) | RP §3 (one deliberately unexpected direction); RV §7 PS1 | step / self-review check |  |
| RI-21 | The first output is a warm-up; reject the typical idea (untagged) | RP §3 (the first batch is a warm-up, labelled); RV §7 PS1 | step / self-review check |  |
| PI-14 | "It would be cooler" is new scope: log it (untagged) | R "Working with other agents" (a "make it cooler" idea after a gate is new scope); RV §7 PS5 | standard / self-review check |  |

## b. Universal principles

| UP-ID | Applies | Where in "Core principles for this craft" (`environment-design/SKILL.md` §7) |
| --- | --- | --- |
| UP-01 | yes: the place is the backdrop; routes, objectives, hazards and characters read first | P1 |
| UP-02 | yes: game camera, phone size, busiest moment, lowest and highest graphics | P2 |
| UP-03 | yes: value bands per layer; focus by lowering the surroundings | P3 |
| UP-04 | yes: blockout and routes, then composition and kit, then dressing, light last | P4 |
| UP-05 | yes: landmark tallest and unique; directional shapes; simple collision | P5 |
| UP-06 | yes: rest areas in the player band, clean floors, indicated masses | P6 |
| UP-07 | yes: reserved hues, one treatment per gameplay read, material per rule, orientation convention | P7 |
| UP-08 | yes, in part: the master does not list the environment designer, but its space line (rest and action along a route; opening seconds) lands in what I own: visual pacing, reveals after turns, look changes hidden behind fades. Routes and pacing stay the game designer's | P8 |
| UP-09 | yes: landmarks, doorways and markers pushed past real on a walkable, believable base | P9 |
| UP-10 | yes: the place as a character, personality words and story facts | P10 |
| UP-11 | yes: art bible shapes, palette, stylisation level matched to the characters | P11 |
| UP-12 | yes: no duplicates in one view, no flat fills, variation inside the family | P12 |
| UP-13 | yes: the read plan before any image | P13 |
| UP-14 | yes: research, three distinct directions, a reasoned pick | P14 |
| UP-15 | yes: greybox before art, gates, rebuild rather than patch | P15 |
| UP-16 | yes: one named problem per pass, by layer, before/after from the same camera | P16 |
| UP-17 | yes: zones and anchors for sound and VFX, kit briefs, measured budgets | P17 |
| UP-18 | yes: stop criteria and a pass budget in the read plan | P18 |
| UP-19 | yes, in part: the master does not list the environment designer; its space line (rewards and new views at real achievements and natural pauses) is mine; the feedback stack itself belongs to other crafts | P19 |
| UP-20 | yes: hazards and routes read by shape and value without colour; fog never hides them; intense ambient channels reducible, at most 3 flashes a second | P20 |

## c. Old book changes

Rows for every old rule removed, replaced, moved or materially changed (file:line at `df13ff4`). Rows kept word for word and the new rows (E-15 to E-20, PR-33 to PR-51, LA-15 to LA-21, AB-13 to AB-17, C-15 to C-22, the new references and sections) are not listed.

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by / moved / removed | Why |
| --- | --- | --- |
| roles/environment-designer.md:12 build comment | kept + J018 phrase and author tag | Spec rule |
| roles/environment-designer.md:14 opening paragraph | sharpened (the place is the backdrop; proven with numbers and captures) | The core rule of the rebuilt books |
| roles/environment-designer.md:18 skills order | sharpened (names the read plan, core principles, measuring commands) | New references |
| roles/environment-designer.md:21 on-demand list | sharpened: `platform-policy` added for dressing with blood, violence, alcohol, adult venues, brands | V4: content maturity and IP (`platform-policy/references/rules.md:56, 87`) |
| roles/environment-designer.md:24 job lead line | sharpened (also writes the read plan) | New stage |
| roles/environment-designer.md:29 "Craft practice from Riot's artists ... `J016-orchestration/riot-extracts.md` §4" | removed | Job card fixed list: role files point to their own books, not to the J016 extracts; the material now lives in the books |
| roles/environment-designer.md:33 work method step 2 | replaced by the new step order (intake → read plan → option round → blueprint → greybox and grey pass → slice → passes → self-review → hand-offs) | New stages from the library |
| roles/environment-designer.md:34 step 3 build | sharpened (key light chosen in grey; light and polish after the last route change) | LC-11, PP-26 |
| roles/environment-designer.md:36 step 5 self-review | moved to the new section "What you check before handing back" and sharpened (the §7 checklist, lowest and highest setting, feel and listening not judged from stills) | Brief v2 V1; the checklist is the review the agent runs |
| roles/environment-designer.md:37 step 6 proof | kept (now step 5) + known-size object and grey value pass | WL-21, VC-02 |
| roles/environment-designer.md:40 working with other agents | sharpened (what to ask each partner for, and when; pointer to handoffs §7) | Spec: the role body names partner asks |
| roles/environment-designer.md:46 write scope | sharpened (read plan, look sheet, measurement outputs, the material zoo) | New files |
| roles/environment-designer.md:49 hand-back | sharpened (read plan, option round, §7 lines, passes and captures used, could-not-check list) | CR-17, PI-12 |
| environment-design/SKILL.md:6 header | kept + J018 phrase and author tag | Spec rule |
| environment-design/SKILL.md:11-13 §1 | sharpened (the rule above all; who owns cover, sight lines, value bands; after-compaction line) | GD-01, WL-01; brief v2 V7 |
| environment-design/SKILL.md:15-26 §2 table | sharpened (read-plan, worked-examples, measure-captures rows; symptom list longer) | New references |
| environment-design/SKILL.md:29 step 1 intake | sharpened (route table in seconds, hazard sheets, read rank, material-to-rule table, value bands, reserved colours, key light) | Partner books: game-design spaces.md, preproduction handoffs.md:23 |
| environment-design/SKILL.md:30 step 2 set list and references | replaced by step 2 (read plan, new) and step 3 (research, set list, one option round, references) | UP-13, UP-14 |
| environment-design/SKILL.md:31 step 3 site plan and blueprint | kept (now step 4) + first view and constraints dressed as the world | WL-07, WL-04 |
| environment-design/SKILL.md:32 step 4 blockout and round trip | merged into step 5 with the greybox order and the grey value pass | WL-08, LC-11, VC-02 |
| environment-design/SKILL.md:33 step 5 target slice | kept (now step 6), sharpened (avatar colours, smallest object, lowest and highest setting) | VC-06, WL-20 |
| environment-design/SKILL.md:34 step 6 full build | replaced by step 7 (passes over the whole stage in a fixed order) | PP-26, PI-06 |
| environment-design/SKILL.md:35 step 7 review | moved to step 8 (the §7 checklist) | Brief v2 V1, V5 |
| environment-design/SKILL.md:36 step 8 hand-offs | kept (now step 9) + in-set capture back to the modeler | WL-24 |
| environment-design/SKILL.md:41 E-01 | sharpened (phone-size view) | UP-02 |
| environment-design/SKILL.md:42 E-02 | sharpened (cover, sight lines; art snaps to the greybox) | GD-31 |
| environment-design/SKILL.md:43 E-03 | sharpened (first view after spawn) | WL-07 |
| environment-design/SKILL.md:44 E-04 | sharpened (dummy and known-size object in every space) | WL-21 |
| environment-design/SKILL.md:45 E-05 | sharpened (play floors walkable, height changes on the game designer's list) | WL-14 |
| environment-design/SKILL.md:47 E-07 | sharpened (landmark tallest, unique silhouette, shape flow) | CF-08, CF-14, WL-23 |
| environment-design/SKILL.md:48 E-08 "Light and air serve mood and readability" | replaced: "readability first, mood second", one key direction, lightest area on the objective | GD-01, LC-10, LC-12; the old wording put mood first |
| environment-design/SKILL.md:49 E-09 | sharpened (nothing fast or bright near a sight line) | LC-01, VR-16 |
| environment-design/SKILL.md:50 E-10 "Dressing tells a story of use" | replaced by "Someone lives here; time has passed" (3 story facts with carriers) | WL-22, MD-09 |
| environment-design/SKILL.md:51 E-11 | sharpened (theme cues; each new world clearly new) | SI-04, GD-33 |
| environment-design/SKILL.md:52 E-12 | sharpened (bespoke shells with one trim sheet; no duplicate in one view) | PP-24, MD-17 |
| environment-design/SKILL.md:56-64 §5 rules | sharpened (+ band and reserved colours; colour alone; lowest setting; platform-policy for maturity and IP; tool number MEASURED) | VC-05, LC-01, UP-20, V4 |
| environment-design/SKILL.md:66-72 §6 self-check | replaced (points to review.md §7; read plan, option round, grey pass, budget used) | Brief v2 V1, V5 |
| environment-design/references/place-reading.md:8 PR-01 | sharpened (sight lines; collision diff check) | GD-31 |
| environment-design/references/place-reading.md:10 PR-03 | sharpened (art within one snap step) | PP-27 |
| environment-design/references/place-reading.md:21 PR-10 | sharpened (typical avatar colours; busiest-moment check) | VC-06, WL-01 |
| environment-design/references/place-reading.md:27 PR-12 | sharpened (jump measured in Studio, not remembered) | WL-29; partner book game-design spaces.md |
| environment-design/references/place-reading.md:29 PR-14 | sharpened (Roblox greybox sample as an example, not a preset) | WL-21 roblox_fit |
| environment-design/references/place-reading.md:38 PR-19 | sharpened (player band; detail above head height) | VH-05, LC-18 |
| environment-design/references/place-reading.md:39 PR-20 | sharpened (no piece twice at the same angle) | PP-24, VR-14 |
| environment-design/references/place-reading.md:41 PR-22 | sharpened (detail by display size and speed; orbit camera) | MD-02, CF-02 |
| environment-design/references/place-reading.md:55 PR-28 | sharpened (value bands, reserved colours) | VC-05, LC-01 |
| environment-design/references/place-reading.md:56 PR-29 | sharpened (lowest and highest setting) | WL-20 |
| environment-design/references/place-reading.md:59 PR-32 | sharpened (paint-over before the 3D change) | CR-05 |
| environment-design/references/light-and-air.md:5 intro | sharpened (readability named first) | GD-01 |
| environment-design/references/light-and-air.md:13 LA-04 | sharpened (sky plus sun outdoors; shadows agree) | LC-13 |
| environment-design/references/light-and-air.md:16 LA-07 "low and high quality" | sharpened to the lowest and highest setting; high not noisier | WL-20 |
| environment-design/references/light-and-air.md:23 LA-10 | sharpened (+ hazards) | UP-20 |
| environment-design/references/light-and-air.md:25 LA-12 | sharpened (+ the key view re-taken without post effects) | VC-02 |
| environment-design/references/light-and-air.md:30 §3 who decides | sharpened (the art director also sets value bands and reserved colours) | VC-05, LC-01 |
| environment-design/references/ambience.md:18 AB-08 | sharpened (never dry in a large space) | SD-13 |
| environment-design/references/ambience.md:21 AB-11 | sharpened (decorative motion small, slow, partly hidden; map mechanics quiet) | VR-16, LC-01, GD-23 |
| environment-design/references/ambience.md:25 §2 request | sharpened (feel and distance; footstep and reserved-colour tables go with it) | SD-02, SD-10, SD-23 |
| environment-design/references/ambience.md:37-45 §5 checks | sharpened (+ emotion, footstep entries, motion distances) | SD-02, SD-23, VR-16 |
| environment-design/references/review.md:6-9 §1 order | replaced (four steps with the greybox walk and grey value pass) | PI-04, VC-02 |
| environment-design/references/review.md:12-18 §2 table | sharpened (+ look_check numbers, place listing, partner check-ins) | CR-17 |
| environment-design/references/review.md:22-34 §3 camera set | sharpened (+ first frame after spawn, busiest moment, smallest object rows; key views and image budget) | WL-07, WL-01, WL-19; brief v2 V1 |
| environment-design/references/review.md:36-40 §4 checks | moved into the §7 lines; §4 keeps budget and hand-off completeness and the re-rate rule. Repair round 1: three topics that had lost their line are back: camera clearance (FL7), haze never hides a route cue, edge or hazard (VB7), repetition while moving (FL3) | Brief v2 V6 (one rule, one place); review F4 |
| environment-design/references/review.md:53-60 §6 fixing | sharpened (+ contrast before detail, one problem per pass, problem behind a note, rebuild not patch) | VC-01, PI-07, CR-03, PI-09 |
| environment-design/references/diagnosis.md:9 flat row | sharpened (lower the surroundings first; no added detail) | VC-04, VC-01 |
| environment-craft/SKILL.md:6 header | kept + J018 phrase and author tag | Spec rule |
| environment-craft/SKILL.md:11 §1 | sharpened (read plan input; after-compaction line) | Brief v2 V7 |
| environment-craft/SKILL.md:27-35 §3 steps 1-9 | replaced by 11 steps (greybox order, grey value and light-direction pass, material zoo, dress before the look as in the pass order of the design skill, clean floors and grounding); the old order put the look (old step 6) before dressing (old step 8) | WL-08, LC-11, VC-05, WL-19, MD-13 |
| environment-craft/SKILL.md:49 C-09 "RenderSettings" not scriptable | sharpened: RenderSettings is plugin-security; probe the `execute_luau` route before relying on it | `RenderSettings.yaml:66-84, 106-125` (PluginSecurity) |
| environment-craft/SKILL.md:53 C-13 | sharpened (lowest and highest) | WL-20 |
| environment-craft/SKILL.md:57-61 §5 rules | sharpened (undo review toggles; art never moves collision, cover, sight lines) | GD-31 |
| environment-craft/SKILL.md:63-69 §6 self-check | sharpened (+ grey pass, collision diff, floors, zoo, §7 lines, image budget) | Brief v2 V1, V5 |
| environment-craft/references/audit-and-capture.md:24 quality level "not scriptable" | replaced: scripts cannot set it, a plugin may: probe first, else by hand | `RenderSettings.yaml` PluginSecurity; game-designer proposal row on the same probe |
| environment-craft/references/audit-and-capture.md:22 camera list | sharpened (key views; dummies in avatar colours; busiest moment from the studio operator) | VC-06, WL-01 |
| environment-craft/references/audit-and-capture.md:32 packet assembly | sharpened (the §7 lines, could-not-check list, image budget) | CR-17 |
| environment-craft/references/studio-light-air.md:8 step 2 sun position | sharpened (chosen on the greybox in grey from 2-3 positions) | LC-11, LC-10 |
| environment-craft/references/studio-light-air.md:10 step 4 fill light | sharpened (shadow side gets the opposite temperature, never neutral grey) | LC-08, LC-07 |
| environment-craft/references/studio-light-air.md:74 §8 look lab | sharpened (bracket each key value) | PI-08 |
| environment-craft/references/blender-to-studio.md:10 one-off pieces row | sharpened (form and finish follow modeling-design) | Brief v2 V6: one rule in one place |
| environment-craft/references/blender-to-studio.md:12 assembling row | sharpened (+ packages; new bespoke-shells row) | PP-24, MD-17 |
| environment-craft/references/handoffs.md:30 §2 art director | sharpened (numbers, grey images, paint-overs, goal question, cold read at the check-in) | CR-02, CR-05, VC-02 |
| environment-craft/references/handoffs.md:35-40 §3 modeler | sharpened (personality and story fact; band and reserved colours; size steps; in-set capture back) | CD-26, WL-22, VC-05, SS-07, WL-24 |
| environment-craft/references/handoffs.md:43-70 §4 sound | sharpened (+ emotion, floor materials, C3; no dry large space) | SD-02, SD-23, SD-13 |
| environment-craft/references/handoffs.md:73 §5 VFX | sharpened (motion small and slow near sight lines; off paths; reserved colours) | VR-16, LC-01, VR-23 |
| environment-craft/references/handoffs.md:80 §6 studio operator checks | sharpened (busiest-moment capture; lowest-setting captures) | WL-01, WL-20 |
| environment-craft/references/ambience-in-place.md:40 step 6 | sharpened (footstep material list; sight lines to VFX) | SD-23, VR-16 |

## d. Command runs (V3) and proposals from other roles (V11)

Every command or tool mode a check names was run once on a synthetic sample of its real input (scratch files `envdes_*` in the session scratchpad), unless marked not run.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| VB1, VB3 (M1) | `look_check.py value <cap> --box <env boxes>` | in-scene 1280 × 720 game-camera frame with sky, ground, walls, a small character, a pickup, a landmark | runs; writes JSON and `<cap>.luminance.png`; subject p5 0.142, p95 0.329; right answer for the boxes given |
| VB1 (M1 limit) | same, on the frame with a 40 × 60 px pure-black patch | same frame type | p5 0.140 (unchanged): misses the black with no error → M2 added and a tool proposal (`--dark-below`) |
| VB1 (M2) | PIL near-black share in boxes (one-liner as written in MC) | clean frame and black-patch frame | runs; 0.0 vs 0.0044: right |
| VB7, RD2 (M1 compare) | `value <cap> --box far --name far --box near --name near --compare-subjects` | same frame | runs; per-subject p5-p95 and ranking; with the landmark inside the far box the far spread rises to p95 0.757 (wrong reading with no error) → M1 note: landmark measured apart |
| VB4 (M3) | `look_check.py palette <cap> --k 8/16 --roles {danger} --exclude-box <pickup>` | clean frame; frame with a red trim (1.3 %); frame with a small red patch (0.14 %) | runs; ΔE 30.0 (no red) vs 6.5 with share 0.013 and 0.0014 (found at k 8 and 16): right Superseded in repair round 1: the recipe ran on the whole frame (review F2) and k-means can merge a small accent; M3 is now the box-only pixel-share script (runs below) |
| VB5 (M4) | `palette <cap> --box <band>` + weighted-chroma one-liner as written | neutral walls vs walls orange above head height | runs; above 9.6 / player 9.6 vs above 60.4 / player 9.6: right Superseded in repair round 1: M4 now reads `mean_chroma` from the M3 script; a neutral limit added (review R2) |
| FL1 (M5 limit) | `look_check.py thumb <cap> --size 844x390 --box <pickup>` | frame with a 30 × 25 px pickup | `invalid-mask` (object under 0.1 % of the frame) → crop recipe + tool proposal |
| FL1 (M5) | thumb → tight box scaled → 120 px crop → `value --box --ring 4` | pickup on a mid-grey floor, then on a darker floor | runs; tight box 1.02 → 2.22 (right: the pickup read by hue only, then by value); a loose box gave 1.0 and 1.05 (wrong with no error) → "tight box" rule in MC M5 |
| VB8 (M11) | `palette <cap> --k 2 --box <lit>` and `--box <shadow>` | warm-lit and cool-shadow blocks of one material | runs; b* 26.8 vs −14.6: right Superseded in repair round 1: M11 now reads `mean_b` from the M3 script (review R6c) |
| QV4, QV2 (M10) | `look_check.py thumb --size 844x390`; PIL mirror one-liner | in-scene frame | runs; writes thumbnail, 4× sheet and the mirrored file |
| FL6, AM2, QV3 (M7) | `scene_audit.py probe --root Workspace/Stages/Falls --chunk-size 60000 --chunk 1`; `scene_audit.py audit --probe tools/tests/fixtures/env/probe_stage.json --map tools/tests/fixtures/env/ambience-map.md --floating-tol 0.5 --buried-tol 2 --oob-tol 0 --out …` | the tool's own probe fixture with planted defects | probe prints the Luau; audit exits 1, writes JSON and Markdown: floating 3, buried 2, out of bounds 1, map vs place 8 listed: matches the planted defects |
| RD13, FL4, FL7 (M8) | Python on the probe JSON: world top from `cf` and `size` | the same fixture | runs; tops listed (Tree 10.0 …); the rotation term matches the tool's own rotated-part test (half-height 5) |
| RD6, RD9, FL3, FL9 (M8 Luau listing) | read-only `execute_luau` listing of Material, CanCollide, MeshId | Studio place | not run: J018 is a files-only job (no Studio); marked "probe first" in MC; tool proposal to add the fields to the scene probe |
| QV1, VB9, VB10 (M9) | `execute_luau` setting `settings().Rendering` EnableFRM and EditQualityLevel | Studio place | not run (no Studio in J018); marked "probe first", fallback by hand; studio-mcp probe proposal co-signed |
| VB4, VB11 (M3, repair 1) | `env_lab.py` copied out of `measure-captures.md` §3 and run as written; spec with environment boxes (walls, ground), gameplay exclusions (two avatars, a pickup), reserved danger `#E61E1E` and team `#1E6EE6` | in-scene 1280 × 720 frames with sky, HUD, ground, walls, two avatars and a pickup: clean; + team-blue banner (0.34 % of the boxes); + red patch 32 × 20 px (0.07 % of the frame); + the red patch dimmed to 0.55 linear; a frame whose sky is near the team blue | runs; writes the JSON. Clean 0 / 0; banner team 0.00338; red patch danger 0.00108; dimmed patch 0.0 with the authored swatch (wrong with no error) and 0.00108 once the swatch sampled with `contrast --sample` (`#B01414`) is added; team-blue sky: environment boxes 0.0, a whole-frame box 0.338 (wrong with no error). Both traps are in the M3 cell |
| VB5, VB6, QV1 (M4 via M3, repair 1) | same script, box groups `player` (floor to eye height) and `above` | neutral walls; walls orange above head height | neutral: player 14.6, above 3.3 (the relative rule alone fails a neutral place: review R2 reproduced; the neutral limit, `PROPOSAL` 20, passes it); orange above: player 14.6, above 68.7, `share_chroma_above` 1.0 above and 0.0 in the player band: right |
| VB8, VB12 (M11 via M3, repair 1) | same script, `lit` and `shadow` boxes | warm-lit vs cool-shadow blocks of one material; gold lit, gold shadow keeping chroma, gold shadow gone muddy | `mean_b` 24.7 vs −12.5: right; gold chroma 65.0 lit, 40.4 kept (0.62 of lit), 6.7 muddy (0.10): the half-chroma starting value separates them |
| VB12 (M3 flat, repair 1) | same script, `flat` boxes | 8 panels 290 × 190 px under a 0.8-1.1 light gradient with σ 1.5 noise: flat brown, flat saturated red, flat grey, brown with hue patches, grey with value-only patches, grey with faint tint patches, flat brown split by warm light and cool shadow, flat brown with a cast-shadow step; the same panel set with σ 4 noise saved as JPEG q70 | PNG: flat 2.7 / 0.0087, 1.0 / 0.0082, 2.5 / 0.0087; hue patches 27.3 / 0.070; value patches 2.6 / 0.114; tint patches 11.0 / 0.026; split 32.5 / 0.258 and cast shadow 3.0 / 0.275 (both wrong with no error: box rule "one lit side, no cast shadow"). JPEG: flat brown 5.9 / 0.021 (noise raises the spread: PNG captures; limits set at 8 / 0.04 `PROPOSAL`), tint patches 10.1 / 0.032: right at those limits |
| RD3, VB2, VB9 (M6, repair 1) | `look_check.py value <cap> --box <avatar> --ring 8 --min-ratio 1.5 --tolerance-source "PROPOSAL ..."` | the in-scene frame: dark-blue avatar and light avatar on a warm-grey wall over a brown floor; a 30 × 25 px hue-only pickup | dark avatar 2.485 (subject p50 0.055 below ring 0.211), light 2.286 (0.547 above 0.211): verdict pass at 1.5, direction read from the medians; the pickup in the full frame: `invalid-mask` (under 0.1 %), so small objects go through M5 |
| FL1, RD5 (M5, repair 1) | M5 as written, at 844 × 390 and 1024 × 768 | the same frame, hue-only pickup | 844 × 390: scale 0.541, offsets x0 75 / y0 0, ratio 1.137; 1024 × 768: scale 0.8, offsets x0 0 / y0 96, ratio 1.139 with y0 added, 1.000 without it (the box lands on the wall: wrong with no error, review R6b reproduced). 1.14 fails both targets, as a hue-only pickup should |
| RD7-RD9, RD13, FL3, FL4, FL7 (M8, repair 1) | the M8 one-liner copied out of the reference and run as written | the probe fixture as plain JSON; the same probe cut into two `SCENE_PROBE k/n` lines in reverse order with a noise line | runs on both through `load_probe` (plain `json.loads` raises on the sliced text: review R6a reproduced); tops and largest sizes listed (Ground 0.0 / 100, Tree 10.0 / 10) |
| FL7 camera clearance, VB7 haze (repair 1) | Studio MCP play mode and character navigation captures; M6 on decision views with Atmosphere on | Studio place | not run: J018 is a files-only job (no Studio); FL7 names the studio operator's walk capture as a fallback input; VB7 reuses M6, run above |
| VB12 (M3 flat, repair 2) | `env_lab.py` copied out of `measure-captures.md` §3 after the repair and run as written; the new pass rule applied to its `flat` output | 7 panels 290 × 190 px under a 0.8-1.1 light gradient, σ 1.5 noise, PNG: flat grey; one-hue bricks (±15 % value, darker mortar); a built-in-material value texture under one Color; the bricks with a per-brick hue shift of ±2°, ±4°, ±8°, ±12°; faint tint patches; darker damp patches in the wall's own hue; green-brown silt and cool damp patches (worked example 3); the same panel set as JPEG q70 | PNG: flat 2.3 / 0.008 `flat`; one-hue bricks 2.8 / 0.207 and value texture 2.7 / 0.197 `monochrome` (review B1 reproduced: the old OR rule passed both); ±2° 5.6 (fails), ±4° 10.1, ±12° 29.2 (pass); faint tint 15.4 / 0.011 pass; damp in own hue 2.8 / 0.486 `monochrome`; silt and damp 34.7 / 0.181 pass: right. JPEG: one-hue bricks 11.8 (a false pass with no error: chroma noise on the mortar edges) → trap in the M3 cell; PNG rule in §0 kept |
| VB12 / LC-09 (library check, repair 2) | `look_check.py palette <flat panel> --box <one-hue bricks> --k 4` | the one-hue brick panel | 4 clusters, one hue (a*/b* ratio constant, L 37-52): "more than one cluster" passes a monochrome wall → library proposal row |
| VB6 (M3 second run, repair 2) | `env_lab.py` as written, spec with `max_de`; focal glow and pickup in `exclude` | in-scene 1280 × 720 frames with sky, HUD, ground, beige player-band wall and: calm upper wall; terracotta upper wall (chroma about 35); loud orange upper wall (about 75); calm walls with saturated green bunting along the wall | stray share 0.0, 0.0, 0.353, 0.037: the loud wall and the bunting fail the 0.02 starting limit, the terracotta passes (VB5 still passes: above 35.0 vs player 12.9). Worked example 2 re-written on these numbers. A spec with no `max_de` now stops with `KeyError: 'max_de'` (the default copy of the bible's distance removed from the script) |
| VB11 (M12, repair 2) | `look_check.py palette <zoo> --box <lit face> ×N --roles roles.json --k 8 --out …` (runs; JSON and swatch image written) + the M12 one-liner copied out of the reference | material zoo capture, sky and ground: 4 on-palette blocks (brown, moss, teal, stone; warm-lit face and cool shadow face); the same with an off-palette purple block | lit faces: on-palette clusters 1.2-3.8 from their nearest role, purple 32.7: right at the 15 starting distance; the tool's own `roles` block matched every role in both captures (it cannot see the purple: tool proposal row). Wrong with no error: boxes over the shadow faces read 16-21 (false fails); k 3 on five blocks merged three into one cluster at 11.6 → both in the M12 cell |

| Proposal row (other role) | Adopted / declined, and where |
| --- | --- |
| modeler row 4 (`job-stage.js` B2: in-set capture of each kit piece) | adopted on my side: `EC/references/handoffs.md` §3 checks, `EC/SKILL.md` §3 step 6, review line FL12; co-signed as a workflow proposal |
| modeler row 10 (`templates/skill/art-bible.md` rows) | co-signed and extended (reserved-colour table, temperature direction, palette roles); my books use `PROPOSAL` starting values until then |
| modeler row "VC-05 unit" (library) | adopted: the band is stated in grey value and luminance (`ED/references/light-and-air.md` §4 VB-a; `EC/references/measure-captures.md` §0) |
| modeler row `look_check.py --mirror` | not needed for my checks: the mirror is a PIL one-liner (M10); no change requested |
| modeler row studio-mcp flat-key capture / game-designer row flat-key | co-signed; my checks do not need it (in-scene captures are measured with named boxes) |
| game-designer recipe row (stage contract: route table and hazard sheets; lowest-setting capture in the packet) | adopted (intake in `ED/SKILL.md` §3 step 1; QV1, VB10) and co-signed in my recipe row |
| game-designer row "craft books read the game-designer's sheets" | adopted for the environment: hazard sheets, read rank, route table, material-to-rule table at intake (`ED/SKILL.md` §3 step 1; `EC/references/handoffs.md` §7) |
| game-designer row studio-mcp quality-level probe | adopted as M9 "probe first" and co-signed |
| game-designer row level-design (no point totals; re-rate every check) | adopted for my own list (`ED/references/review.md` §4) |
| game-designer row `tools/level/route_times.py` | declined as a dependency: I take the route table from the game designer; nothing in my books waits on the tool |
| Rows targeting `environment-design` or `environment-craft` directly | none exist in `proposals/modeler.md` or `proposals/game-designer.md` |
| art-director row "bible §7 rows named as inputs" (wave 2, `proposals/art-director.md`) | adopted in repair round 1: intake names the bible's craft-standard rows (value bands in both units, reserved colours with shape partner and allowed share, key light per place, shape vocabulary, palette roles, stylisation level): `ED/SKILL.md` §3 step 1; `EC/references/handoffs.md` §7 |
| art-director row LC-01 / UP-07 check (pixel share, not palette clusters; library) | co-signed and adopted: M3 is now a pixel share inside environment boxes (my own V3 runs agree: a whole-frame or cluster read gives wrong numbers with no error) |
| art-director G3 row (stage recipe: the art director reviews 2-3 grey lighting variants of the greybox before the light pass) | co-signed: matches my `job-stage.js` P4 row and the grey pass (`EC/SKILL.md` §3 step 4) |
| film-director row (`EC/SKILL.md`: the film director's value plan per beat and approved value strip as fixed inputs for a cinematic set; value lines re-run at the shot cameras) | adopted: role body "In cutscenes"; `EC/references/handoffs.md` §7 film-director row (M1 subject first and M6 at the shot cameras) |
| progression-designer row (the route table in seconds goes to the progression designer; targets `level-design` and `environment-design`) | declined for my books: the route table is the game designer's deliverable (`level-design`); I receive it and never issue it. A layout proposal of mine that changes walk time goes to the game designer (`EC/references/handoffs.md` §1), who re-issues the table to every reader |
| game-designer row studio-mcp quality-level probe (`RenderSettings.QualityLevel`) | adopted with a correction: M9 sets `EnableFRM = false` and `EditQualityLevel` (`RenderSettings.yaml:66-84, 106-125`); `QualityLevel` applies only while the frame-rate manager is on (`:256-261`), which can change the level mid-capture. Proposal row added so the studio-mcp probe uses one setting |
| sound-designer row (`templates/environment/ambience-map.md` floor-material table) | co-signed: my template row already asks for floor materials; the sound designer owns the material → footstep table |
| art-director row 38 (`light-and-air.md` VB-a takes the starting band values by pointer from `art-review/references/art-bible.md` §7) | adopted in repair round 2: VB-a, review VB1, the read plan's band field and the M3 `max_de` now point to the bible's value-band and reserved-colour rows; the separation targets stay in VB-a until the bible has a row for them (my proposal row asks for one); repair round 3: the bible now has the separation-targets row, so VB-a points to it and keeps only the two target names and their meaning; §0's grey-to-luminance line is marked as conversions only |
| sound-designer row 27 (G3 stage recipe: the floor-material list goes to the sound designer at the kit-list stage) | co-signed and adopted on my side: `EC/references/handoffs.md` §7 sound row now sends the floor-material list at the kit list, before materials are built |

V4 diff: no landed line concerns money, paid random items, ads, chat, player data, saves or remotes. Dressing with blood, violence, alcohol, adult venues, or real brands, logos and franchise designs is routed to `platform-policy` (`references/rules.md:56` content maturity, `:46` ad integrations, `:87` IP); the shared skill wins; one library row proposed for WL-24.

## Repair round 1

Review `reviews/environment-designer-rev1-reviewer.md` (fix-first). Every keep-list item is unchanged. Paths relative to `.agents/skills/` (`ED`, `EC` as above).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (separation lines could not fail) | Separation targets defined once in `ED/references/light-and-air.md` VB-a (characters and dummies 1.5:1; critical markers and the smallest gameplay object 3:1; both `PROPOSAL`); the ratio's meaning stated once in `EC/references/measure-captures.md` §0 (symmetric, never below 1, 1.0 = none; direction from the medians; `--min-ratio` once the bible gives the number); the M6 "wrong number" cell names the "above 1" trap. Lines now use the target: `ED/references/review.md` §7 header, RD3, VB2, VB7, VB9, VB13, FL1; `ED/SKILL.md` P1; `ED/references/worked-examples.md` §2; `EC/references/studio-light-air.md` §9 hazard glow; `EC/references/terrain-and-water.md` floors. V3 runs in table d (M6, M5) |
| F2 (reserved-colour check measured sky and HUD) | M3 replaced by a box-only pixel-share script (`EC/references/measure-captures.md` §3) inside environment boxes with gameplay exclusions; §0 corrected (value and silhouette give `invalid-mask` with no box; `palette` measures the whole frame and is not used for environment colour); the reserved hue is also tested as rendered (sampled with `contrast --sample`). VB4, VB11 and worked example 2 rewritten. V3 runs in table d (team-blue sky trap, dimmed-red trap) |
| F3 (flat-fill check never fired) | M3 script `flat` measures: `hue_spread` (chromaticity spread over 4 × 4 blocks, blind to a light gradient) and `value_spread` (log-luminance spread after a plane fit); flat limits 8 / 0.04 `PROPOSAL` from eight synthetic panels as PNG and noisy JPEG; box rule (one lit side, no cast shadow) in the M3 trap cell; VB12, P12 and worked example 3 rewritten (example 3 now measures above and below the water line separately). Tool proposal row for `look_check.py` |
| F4 (three old checks lost their line) | FL7: the default camera passes every tight opening and low ceiling without clipping or being pushed in (1 play-mode capture per tight opening, or the studio operator's walk capture); VB7: with the final Atmosphere on, route cues, edges and hazards still reach their separation target in their decision views (M1, M6, M5); FL3: a repeated facade judged on 3-4 captures along the camera path. P12 and P20 checks and LA-10 point to them; coverage §c row updated |
| R1 (UI-06 landed text missing) | `ED/references/light-and-air.md` VB-c now says "the same reserved-colour table that UI and gameplay effects use"; coverage row corrected |
| R2 (VB5 false fail on a neutral place) | VB5: below the band above, or under the neutral limit (`PROPOSAL` chroma 20); V3 run reproduces the false fail (14.6 vs 3.3) and the limit clears it |
| R3 (grey pass and greybox order written out in several places) | Full rule kept in `ED/references/light-and-air.md` LA-15 (what) and `EC/SKILL.md` §3 steps 3-4 (how, with the image budget); `ED/SKILL.md` §3 step 5, `EC/SKILL.md` C-15, `EC/references/studio-light-air.md` §1 step 2, review VB8 and PS2 now point there. The role's work method keeps one short clause (when the light is chosen), no parameters |
| R4 (no scope for fix jobs) | `ED/references/review.md` §7 header: fix job = the lines the change touches by dependency plus RD2, RD3, VB1, FL1, QV3, the others `n/a (fix job)`; the §4 re-rate rule, `ED/SKILL.md` §6 and the role's work method point to it |
| R5 (modeler brief lacked ground capture and origin) | `EC/references/handoffs.md` §3 `fixed`: the greybox origin and a capture of the stage's ground under its chosen light (or the art bible values) |
| R6 (M8 input, M5 y offset, M11 one-liner) | (a) M8 loads through `scene_audit.load_probe` (one-liner run on plain and sliced probe output); (b) M5 and M10 add both `content_box_px` offsets (4:3 run: 1.000 without y0, 1.139 with it); (c) M11 reads `mean_b` and `mean_chroma` from the M3 script |
| R7 ("Riot" in three evidence cells) | removed from `ED/references/place-reading.md` PR-01 and `ED/references/light-and-air.md` LA-05, LA-10; row ids kept. Only the required header phrase remains (grep) |
| R8 (wave-2 rows against my books; quality-level probe) | answered in table d's V11 rows: art-director bible-rows row and film-director row adopted; LC-01 pixel-share and G3 lighting-variant rows co-signed; progression-designer row declined (the route table is the game designer's); quality-level probe settled on `EnableFRM = false` + `EditQualityLevel`, with a proposal row |

V5 pass after the repair (scripted): every coverage row that names VB2, VB4, VB5, VB9, VB12, VB13, RD3 or FL1 was re-opened at its landed-in line; the worked examples that use a changed rule (§1 FL1, §2 VB4, VB5, VB13, §3 VB12) were re-read and updated; a grep for "above 1", "one cluster", "single-cluster" and "Riot" over the books returns only the required header phrase. Sizes: `ED/SKILL.md` 113 lines (§7 starts at 17.8 KB, re-read line in §1), `EC/SKILL.md` 84 lines; descriptions 393 and 390 characters; role frontmatter md5 unchanged.

## Repair round 2

Review `reviews/environment-designer-rev2-reviewer.md` (fix-first). Every keep-list item is unchanged (the rule above all, read plan, option round, grey pass written once, separation targets, the M3 script and its traps, review §7 and its fix-job scope, M5/M8/M9, partner asks, platform-policy routing, the 16 rejections). Paths relative to `.agents/skills/`.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| B1 (flat-fill line passed a one-hue textured wall) | `ED/references/review.md` VB12: passes only when `hue_spread` is above its flat limit; `value_spread` above with `hue_spread` under is `monochrome` and fails, both under is `flat`; both numbers recorded. `EC/references/measure-captures.md` §3 flat bullet (same rule, repair-2 runs) and M3 trap cell (coloured light pool; JPEG chroma noise: one-hue bricks 11.8 as JPEG q70). `ED/references/light-and-air.md` VB-e: a value texture alone is one hue, with the Roblox remedies (hue-shifted part Colors, MaterialVariant or SurfaceAppearance ColorMap, terrain patches of materials whose MaterialColors differ in hue; `MaterialVariant.ColorMap` checked in `_api-reference/classes/MaterialVariant.yaml:80`). `ED/SKILL.md` P12 check sharpened. Worked example 3 re-read and changed: the silt and damp patches are now hue shifts (green-brown, cooler grey), retest numbers from the synthetic wall (34.7 vs 2.8 for darker patches in the wall's own hue). V3 runs in table d. Library proposal for the LC-09 check |
| R1 (P7 and P11 named measures no line runs) | P7: "reserved-hue pixel share in the environment boxes ... (VB4 by M3)". P11: palette roles now run: new M12 (`palette` with `--box` on the zoo's lit faces and `--roles`, then a one-line nearest-role distance per cluster); VB11 adds "no palette cluster farther than the palette distance (starting `PROPOSAL` CIEDE2000 15) from every bible palette role"; §0 of measure-captures now says `palette` with `--box` is used for palette roles, never for reserved hues or saturated shares. Tool proposal for a per-cluster nearest-role output |
| R2 (second copy of the starting bands) | `ED/references/light-and-air.md` VB-a points to `art-review/references/art-bible.md` §7 value bands; review VB1 points to VB-a; VB4 and the M3 spec's `max_de` point to the bible's reserved-colours row, and the script's default 10 is removed (a spec without `max_de` stops with an error); `read-plan.md` band field points to the bible. Kept here: the separation targets (no bible row yet; proposal row extended) and the §0 unit conversions, marked as conversions only. V11 line for art-director row 38 added |
| R3 (VB6 had no number) | VB6: with the focal elements and the read plan's eye-path accents boxed into `exclude` (a second M3 run), `share_chroma_above` in the environment boxes is at most the stray limit, starting `PROPOSAL` 0.02; the M3 read text says how. VB-d's example is now "warm, not loud" (terracotta), and worked example 2 uses the measured numbers (chroma 35 above, 13 in the player band, stray 0; a loud orange 0.353). The art bible's accent share (60 / 30 / 10) was not used as the limit: it counts a palette role's area, not stray saturation outside the accents |

Also in this round (V10, V11): sound-designer row 27 adopted on my side (`EC/references/handoffs.md` §7 sound row: the floor-material list at the kit list). Proposals file: the look_check colour-mode row (monochrome label) and the bible craft-standards row (stray limit, palette distance) extended; new rows for `palette` per-cluster nearest role and for the LC-09 library check.

V5 pass after this repair (scripted): every coverage row naming VB1, VB4, VB6, VB11 or VB12 was re-opened at its landed-in lines; the worked examples using a changed rule (§2 VB5 and VB6, §3 VB12) were re-read and changed where needed. Grep over the books: no "M1-M11", no "cluster share", no pass rule on "the flat limits", no "Riot" beyond the header phrase, no library IDs added. Sizes: `ED/SKILL.md` 113 lines, `EC/SKILL.md` 84 lines; frontmatter untouched; LF endings.

## Repair round 3

Review `reviews/environment-designer-rev3-reviewer.md` (fix-first; rev1 and rev2 re-read for context). Every keep-list item is unchanged. Paths relative to `.agents/skills/` (`ED`, `EC` as above). Test captures are synthetic 1280 x 720 PNG in-scene frames (sky, ground, a row of blocks with a lit face and a shadow face; material blocks carry a +-12 % value texture, reference blocks are plain). Two light models: A = linear light (sun x cos + ambient, exposure, a tone curve), B = the reviewer's sRGB multipliers. Not Studio-verified: no Studio capture was taken this round. Scratch: `<scratchpad>/env-designer-r3/` (`env-designer_zoo_m12.py`, `env-designer_vb56.py`, `env-designer_zoo_reserved.py`, `env-designer_haze.py`).

| Finding | Fixed where | Test input and result |
| --- | --- | --- |
| B1 (M12 compared rendered lit faces with authored role hexes) | `EC/references/measure-captures.md` M12: step 1 samples one reference block per palette role with `contrast --sample` (`fg_sample.hex`) and writes `roles-rendered.json`; steps 2-3 run `palette --roles roles-rendered.json` and the nearest-role one-liner on it; run on each look's zoo capture and on a neutral-light capture, a material passes only when it passes on all. Wrong-number cell names the stage-light trap (authored hexes under a bright, warm, dim or coloured light) and the dim-light trap found this round (a dim or night look shrinks every distance and passes off-palette blocks; the neutral-light capture catches them). `EC/references/studio-light-air.md` §9 zoo bullet: reference blocks (one per palette role, one per reserved hue, one mid grey) in the stage's plain material, one capture per look plus one under a neutral light, M12 added to the measures. `ED/references/review.md` VB11 (roles as rendered, each look + neutral capture); `ED/SKILL.md` P11; `EC/SKILL.md` §3 step 7; `ED/references/light-and-air.md` VB-f | Zoo: 4 role reference blocks, 4 on-palette material blocks (stone, moss, terracotta, wood), 3 off-palette (blue 30.4, mauve 25.5, olive 17.3 from the nearest role as authored); limit 15. Model A, max on-palette / blue / mauve / olive, authored roles → roles as rendered: neutral sun 3.1 / 28.2 / 24.2 / 18.6 → 0.4 / 27.7 / 24.7 / 16.1; warm sun 4.0 / 26.6 / 22.9 / 20.0 → 1.2 / 29.9 / 24.0 / 16.3; warm dusk 10.9 / 29.7 / 20.4 / 17.4 → 0.2 / 28.5 / 17.3 / 15.9; dim interior 16.8 (false fail) / 32.8 / 21.8 / 14.2 → 0.3 / 23.8 / 17.8 / 12.6 (olive: false pass); night 25.5 (false fail) / 36.4 / 30.1 / 20.3 → 0.6 / 16.9 / 14.0 (false pass) / 9.2 (false pass). Model B (the reviewer's lights): neutral x1.05 2.5 → 0.5; bright x1.25 12.5 → 1.5; warm sun 13.9 → 1.6; warm dusk 9.6 → 2.1; dim x0.6 17.1 (false fail) → 0.3; blue and mauve fail in every B run with rendered roles (16.7-36.1), olive 12.4 under x0.6. Material texture darker than the plain reference (mean 0.85): on-palette 2.0-4.3 under all five A lights. So: the reference blocks remove every on-palette false fail (0.1-2.1, max 4.3 with a darker material); the dim and night false passes are caught by the neutral-light capture (olive 16.1, blue 27.7, mauve 24.7 there). The book's M12 commands, cut out of the reference by regex and run as written with `--out` files on the five model-A captures, run without error and give the same numbers |
| B1, same kind: reserved hues on the zoo (M3 as-rendered swatch had no gameplay object to sample from in the zoo) | `EC/references/measure-captures.md` M3 cell (as-rendered swatch from the same capture; on the zoo from the reserved hue's reference block); `studio-light-air.md` §9; VB11 | Zoo with a reserved red reference block, a red-ish banner (#C0302F) and a terracotta (#B5603A), `max_de` 10, model A: red-ish banner authored / as rendered: neutral 1.000 / 1.000, warm sun 1.000 / 1.000, warm dusk 1.000 / 1.000, dim interior 0.000 (false pass) / 1.000. Terracotta 0.000 everywhere except warm dusk as rendered 0.172: under that look it renders near the danger red, a real read problem the line should show |
| B1, same kind: chroma limits on rendered pixels (VB5 neutral limit 20, VB6 saturated limit 40) count the light's tint | `EC/references/measure-captures.md` §3: new optional spec key `grey` (a mid-grey block as rendered under the same light); the script white-balances to it before `mean_chroma` and `share_chroma_above`; `mean_a`/`mean_b` and the reserved share stay raw; new `grey` bullet with the runs and the rule (set it when the grey block's chroma is above 3); M3 and M4 cells name the trap; `ED/references/review.md` VB5, VB6 | Key view: beige floor (player band), muted terracotta upper wall, one loud orange stray sign, a grey block; player chroma / upper-wall chroma / upper-wall saturated share, raw → `grey`: neutral 7.6 / 32.0 / 0.039 unchanged; warm sun 13.5 / 37.5 → 7.7 / 31.9; warm dusk 17.4 / 39.8 → 7.2 / 28.4; deep sunset 23.2 / 44.9 / 1.000 (false fails: neutral limit and stray limit) → 7.5 / 28.0 / 0.039; dim interior 10.3 / 28.1 → 6.2 / 24.1. The sign's 0.039 (a true fail against 0.02) stays in every run. Regression: the new script without `grey` gives byte-identical JSON to the round-2 script on 4 captures (dusk, sunset, two haze walls) |
| R1 (a flat wall in haze passes the flat-fill line) | adopted: M3 cell, §3 spec key `flat` and flat-fill bullet, `ED/references/review.md` VB12: the `flat` boxes come from a key-view capture with Atmosphere and fog off. Not adopted: "box the near part" (my run shows it still passes at 20 % haze) and the chromaticity plane fit (it would change every calibrated flat number; left as a note on the tool proposal row) | Flat wall (150,120,90) under a 0.9-1.1 light gradient, blending toward haze (170,185,210) along its length, M3 as written: whole wall 1.8 / 8.0 / 14.6 / 25.7 / 52.3 at 0 / 5 / 10 / 20 / 60 % haze (false passes from 10 %); near-third box 1.9 / 3.6 / 6.1 / 11.1 / 27.3 (false pass from 20 %); haze off 1.8 `flat` |
| R2 (separation targets copied in VB-a and the bible) | adopted: `ED/references/light-and-air.md` VB-a points to the separation-targets row of `art-review/references/art-bible.md` §7 and keeps the two target names and their meaning; coverage V11 row for art-director row 38 updated | grep: "1.5:1" no longer in the environment books; "3:1" stays once, in worked example §1 as the example's number (it names the marker target) |
| R3 (MaterialColors routed to the Properties window) | adopted: `EC/SKILL.md` C-09, `EC/references/terrain-and-water.md` row (with `Terrain.yaml:1027-1051`), `EC/references/studio-light-air.md` §6: terrain material colours are set with `Terrain:SetMaterialColor` in `execute_luau`, read back with `GetMaterialColor`; Decoration and GrassLength stay Properties-window steps | docs read: `Terrain.yaml:95-109` (MaterialColors NotScriptable, "use SetMaterialColor"), `:1027-1051` (SetMaterialColor, security None), `:685` (GetMaterialColor). Not probed in Studio |

V5 pass after this repair: every coverage row naming VB5, VB6, VB11, VB12, M3, M12 or VB-a was re-read; LC-05 row and the art-director row 38 V11 row updated; worked example §2 (VB5, VB6 under a neutral light) still holds (no coloured look in it). Sizes: `ED/SKILL.md` 113 lines, `EC/SKILL.md` 84 lines; descriptions unchanged; role file not touched; LF endings; no library IDs or "Riot" added.

Proposals file (this round): the `look_check.py palette` row now asks for the M12 measure to move into the tool with tests (`--role-box` roles as rendered, per-cluster nearest role, a verdict); the colour-mode row adds the grey reference and a haze test case; new row for the art director's CL5 / K08 palette check (roles as rendered on lit captures).

## Proposal sweep (J018 close)

Sweep by the environment-designer sweep agent · claude-opus-5-5 · high · 2026-10-22. Every row in `proposals/*.md` (other roles) that names `environment-design`, `environment-craft` or the environment designer was re-read against the current books and the partners' rebuilt books; a last grep of every proposals file before hand-back found no further row. Paths relative to `.agents/skills/` (`ED` = `environment-design`, `EC` = `environment-craft`).

| proposal file:line | decision (adopted / already in the book / declined) | where or why |
| --- | --- | --- |
| art-director.md:30 | adopted | Round 1 had named the bible §7 rows at intake; this sweep completes the list with the two rows it lacked: the saturation band for environment materials (part of the bible's value-bands row) and the separation targets, in `ED/SKILL.md` §3 step 1 and `EC/references/handoffs.md` §7 art director row. `ED/references/review.md` VB11 now checks each zoo material against that saturation band when the bible sets one (`mean_chroma` of the lit face, M3 with `grey`), which `ED/references/light-and-air.md` VB-f already promised |
| art-director.md:38 | already in the book | `ED/references/light-and-air.md` §4 VB-a takes the value bands and separation targets by pointer from `art-review/references/art-bible.md` §7; review VB1 and VB4 point there; `EC/references/measure-captures.md` §0 holds unit conversions only |
| film-director.md:31 | already in the book | Role body "In cutscenes" (the film director's value plan per beat and approved value strip are fixed inputs; value lines re-run at the shot cameras) and `EC/references/handoffs.md` §7 film director row. Not repeated in `EC/SKILL.md` (one rule in one place; the role body is always loaded). Matches `film-craft/references/handoff-briefs.md` environment-designer row |
| level-design.md:22 | already in the book | Target is the library (the lead's). My books carry no 7.2-stud figure: `ED/references/place-reading.md` PR-12, `ED/SKILL.md` §3 step 1 and `EC/SKILL.md` §3 step 2 measure the jump in Studio. This sweep points `EC/SKILL.md` §3 step 2 to the level book's block ladder (`level-design/references/review-artifact.md` §6.6, once per game, into the game profile) so both crafts measure the jump one way |
| level-design.md:25 | adopted | Target file `preproduction/references/handoffs.md` is not mine (its owner added the node geometry). My side: `ED/SKILL.md` §3 step 1 intake names the blockout brief per node (stop or pass, sight lines to keep clear, key positions, floor types with the smallest gameplay object, events that must be heard: the node geometry of `level-design/references/review-artifact.md` §1); `EC/references/handoffs.md` §7 game designer row asks for it |
| level-design.md:30 | adopted | `ED/references/review.md` RD2: the goal wins the focus when its own contrast (box alone, competitors and HUD out of its ring) reaches the marker target and it is first among the goal and its 2-3 competitors by median or by own contrast; the p5-p95 spread is support only; RD2 is named as the one focus rule. Same kind, changed to the RD2 rule: RD12, VB3, `ED/references/light-and-air.md` VB-b check and LA-15, `ED/SKILL.md` P3 check, `EC/SKILL.md` §3 step 4 (light-direction pass), `ED/references/worked-examples.md` grey pass. `EC/references/measure-captures.md` M1: read `rank_by_median` only; own contrast by the level book's `--exclude-box` run and one-liner (`level-design/references/review-artifact.md` §6.3 step 2, the one copy); wrong-number cell adds the shared-ring trap (darkest box ranks highest against a sky) and the sky-edge spread trap. RD13 notes that "key forks only" is a subset of the level review's fork set (C4) |
| progression-designer.md:28 | declined | The route table is the game designer's deliverable (`level-design`); the level book now sends it to the progression designer when travel is part of an earning cycle (`level-design/references/review-artifact.md` §1, route-table paragraph). I receive the table and never issue it; a layout proposal of mine that changes walk time goes to the game designer (`EC/references/handoffs.md` §1), who re-issues it to every reader |
| reference-images.md:24 | adopted | Role body "Reference images": "§4 steps 1-3 (rounds R0-R3) and 'Who generates'" (matches `reference-images` SKILL §4 rounds table) |
| modeler.md:20 | already in the book | Target is the workflow (G3). My side: `EC/references/handoffs.md` §3 `checks` (one in-set capture of the placed piece at the game camera with a player in frame; accepted only on it), `EC/SKILL.md` §3 step 6, `ED/SKILL.md` §3 step 9, review FL12 |
| sound-designer.md:21 | already in the book | Target is the template. My side: `EC/references/handoffs.md` §4 `floor_materials` and check C3; §7 sound designer row (the floor-material list at the kit list, before materials are built) |

Rows that name the environment designer but target other files and ask nothing of these books (no change): art-director.md:17, :24, :32, :36, :37, :41, :42 (template, studio-mcp probe, G3 recipe, library, `look_check.py`); modeler.md:26 (art-bible template). Checks after the sweep: `ED/SKILL.md` 113 lines (§7 starts at about 18.1 KB), `EC/SKILL.md` 84 lines; descriptions unchanged; role frontmatter md5 unchanged; LF endings; no library IDs or "Riot" added; no new measuring code (M1 points to the level book's tested run).
