---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J007-T01, Modeler_Research_Paper.txt lines 1-422"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Modeler paper part 1: evidence rules, 15 rules, great stylized models, ChatGPT references, blockout, hand modeling in Blender (lines 1-422)

Paraphrased notes. The paper (MP) stays outside git. Every row cites `MP:<line>` (one paragraph = one line; table rows = one line each). Nothing here is fact-checked: the paper's claims are listed in section 12. The paper's research date is 2026-10-21. The paper ran no Blender, Tripo, Roblox import or phone test (MP:17): every recipe, template and pseudocode in it is an untested proposal.

## 0. Headings covered (check C1)

| Paper heading | MP lines | Section here |
| --- | --- | --- |
| (intro: modeler's job, required path) | 1-9 | 1 |
| How to read the evidence | 11-17 | 1 |
| Fifteen rules for the modeler | 19-49 | 2 |
| 1 What makes a great stylized game model | 51-55 | 3.1 |
| Ten concrete cases (cases 1-10) | 57-147 | 3.2 |
| Modeling synthesis and useful disagreements (5 sub-parts) | 149-175 | 3.3 |
| Supplementary industry evidence and limits | 177-185 | 3.4 |
| Case table (rule / number / mark / source) | 187-197 | 3.5 |
| 2 Reference images with ChatGPT (7 sub-parts + table) | 199-303 | 4 |
| 3 From approved reference to a testable blockout (4 sub-parts + table) | 305-342 | 5 |
| 4 Deliberate hand modeling in Blender (incl. Python and MCP recipe + table) | 344-421 | 6 |
| (heading "5 Tripo generation and Blender finishing" at MP:423 is outside range) | 423 | not covered |

## 0.1 How to read

| Key | Meaning |
| --- | --- |
| Tag | The paper's own tag on that sentence. VERIFIED = an official document or described measurement backs the fact (for a vendor: only what the vendor says, not output quality). EXPERIENCE = a named studio or artist reports it, with its project context. OPINION = the paper's proposal, interpretation, template or untested advice. UNKNOWN = the paper says no source gives the value: row text starts "UNKNOWN:", tag column shows the paper's tag on that sentence (OPINION, evidence-gap assessment). Never promote UNKNOWN to a fact. |
| Src | Paper source id (resolved in section 14). `P00` = the paper's own proposed method. "acc" = access date, not publication date. |
| Roles | [for-rigger] [for-art-director] [for-ui] [for-vfx] [for-environment] = that role should also read or act on the row. `-` = modeler only. |
| Row IDs | EV evidence, RU rule, SG section-1 frame, CS1-CS10 cases, SY synthesis, SP supplementary, TB paper tables, RF section 2, BK section 3, HM section 4, NR numbers. |
| Scope | A number from another studio or product is a lesson with its scope, never a Roblox rule. Owner fixed budgets (not from the paper): 20,000 triangles per mesh is only the Roblox upload ceiling; creatures and characters stay under about 7,000 triangles (owner J007-D5). The owner runs Tripo; the modeler prepares inputs (owner J007-D4). |

## 1. Evidence rules and the modeler's job (MP:1-17)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| EV1 | 7 | An asset must pass three tests: it reads as the intended design; it supports the intended motion and interactions; it works in the target Roblox scene on the target phones. A beautiful reference image, a successful mesh-generation request and a successful upload are three different milestones. None alone shows the model is ready to ship. | OPINION | P00 | - |
| EV2 | 9 | Required path: a ChatGPT reference image for every model. Main construction route: deliberate modeling in Blender through Python and an MCP connection. Tripo is an alternative route for assets where generation is likely to help; it is followed by inspection and finishing in Blender. "Hero quality" is an acceptance requirement, not something that comes with choosing Tripo. Both branches end at the same rig, material, import and runtime checks. | OPINION (workflow set by the studio brief) | P00 | [for-rigger] |
| EV3 | 13 | Tag meaning. VERIFIED: an official product document or a described measurement supports the fact; a vendor's qualitative marketing is not independent proof of comparative quality. EXPERIENCE: a report by a studio, artist or developer, kept with its project context. OPINION: proposed workflow, interpretation, prompt template or untested advice. A mixed paragraph separates its factual premise from its recommendation. | OPINION | P00 | - |
| EV4 | 13 | Source ids resolve to a dated register at the end of the paper; each record has a short key quote and a direct URL. | OPINION | P00 | - |
| EV5 | 15 | Undated living documentation is marked "undated" with the access date. An access date is not a publication date. | OPINION | P00 | - |
| EV6 | 15 | Keep the product, API, model, asset-category and rollout scope when sources differ. A current help page and an older announcement can describe different stages instead of contradicting each other. | OPINION | P00 | - |
| EV7 | 15 | A limit for a marketplace avatar is not automatically a limit for an arbitrary environment MeshPart. A result measured on one phone and one scene is not a platform-wide budget. | OPINION | P00 | [for-environment] |
| EV8 | 17 | No Blender modeling, Tripo generation, Roblox import or device benchmark was done for the paper. API recipes and acceptance procedures are proposed patterns, not executed validation. | OPINION | P00 | - |
| EV9 | 17 | Unknown numeric budgets stay UNKNOWN. A studio may author a provisional project budget, but must label it a project choice and then test it. It must not be attributed to a source that never gave it. | OPINION | P00 | - |

## 2. The fifteen rules (MP:19-49)

| ID | MP | Rule in my words | Tag | Src | Detail rows | Roles |
| --- | --- | --- | --- | --- | --- | --- |
| RU01 | 21 | Start every asset from the approved ChatGPT reference, but fix impossible or inconsistent geometry in it before building. | OPINION | P00 | RF6, RF18-a..j, BK2 | [for-art-director] |
| RU02 | 23 | Protect identity-bearing silhouettes and the readable shape hierarchy before adding surface detail. | EXPERIENCE | C01, C04 | SG2, CS4-a, CS4-b | [for-art-director] |
| RU03 | 25 | Match the real gameplay camera as well as the construction views. A beauty render alone is not acceptance. | OPINION | P00 | CS9-b, SY8, BK1 | [for-art-director] [for-environment] |
| RU04 | 27 | Measure evaluated geometry (after modifiers) and keep an editable source. Do not count only the base mesh. | VERIFIED | B03, B09, B10 | HM5, HM6, HM19, HM23 | - |
| RU05 | 29 | Name which bevel-width meaning is used and test the visible result. There is no universal stylized bevel width. | VERIFIED (B04) ; OPINION | B04, P00 | HM9, HM10, SY9, SY10 | - |
| RU06 | 31 | Remeshing and loose-part separation do not by themselves give animation-ready topology. | VERIFIED ; OPINION | B07, B13, P00 | HM14, HM24 | [for-rigger] |
| RU07 | 33 | Decide with the rigger (before final topology and UVs) between continuous skin, rigid parts or a mix. | OPINION | P00 | RF25, BK14 | [for-rigger] |
| RU08 | 35 | Write down the Tripo surface and the exact version. Studio availability and API preview status differ. | VERIFIED | T02, T07 | RF22, RF23 | - |
| RU09 | 37 | A Tripo result is a candidate that needs Blender finishing. It is not a hero-quality guarantee. | OPINION | P00 | EV2 | - |
| RU10 | 39 | Use the limits of the right asset category. Generic meshes, avatar bodies and accessories have different constraints. | VERIFIED | R01, R05, R06 | CS5-d, NR19-NR21 | [for-environment] |
| RU11 | 41 | Keep three things apart: authored texture resolution, supported runtime resolution, actual phone residency. | VERIFIED (R03, R04) ; OPINION | R03, R04, P00 | SY5, NR20, NR22, NR23 | - |
| RU12 | 43 | Reuse the same canonical mesh and material resources on purpose. An atlas does not remove draw calls in every case. | VERIFIED (R13) ; OPINION | R13, P00 | CS10-b | [for-environment] |
| RU13 | 45 | Include Tunable collision and the new mesh-streaming behavior in current decisions. Do not use the old four-option collision or fixed-distance assumptions. | VERIFIED | R08, R14 | NR24, NR25, G10 | [for-environment] |
| RU14 | 47 | Set project budgets from representative phone scenes. An upload ceiling or another production's art limit is not a phone target. | OPINION | P00 | EV7, EV9, CS5-d | [for-environment] |
| RU15 | 49 | Ship only after reference, rig, material, collision, import and in-game checks. The owner keeps final design authority. | OPINION | P00 | BK14, RF25 | [for-rigger] [for-art-director] |

## 3. Section 1: what makes a great stylized game model (MP:51-197)

### 3.1 The frame (MP:51-55)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| SG1 | 53 | Judge a stylized asset as a designed reading at its intended camera and context, not as maximum sculpt detail. | OPINION | P00 | [for-art-director] |
| SG2 | 53 | Riot (League) names silhouette recognition, facing direction and the visible source of power. High Noon Senna keeps her signature weapon while the secondary body silhouette changes. This is Riot's competitive-art policy. It does not mean every decorative prop needs a unique silhouette. | EXPERIENCE (2021-03-12) | C01 | [for-art-director] [for-vfx] |
| SG3 | 53 | Valve's Dota guidance allows inventive departures from default designs when overall recognition survives. It is less strict than copying every outline and color of a base design. | VERIFIED (undated, acc 2026-10-21) | C05 | [for-art-director] |
| SG4 | 55 | Three proposed abstractions: (1) identity-bearing shape, (2) material and lighting-readable surface, (3) movement-ready construction. It is an agent method, not a measured three-factor theory. | OPINION | P00 | - |
| SG5 | 55 | UNKNOWN: the sources give no universal bevel radius, contrast ratio, limb proportion or texel-density target for Roblox phones. | OPINION (evidence-gap assessment) | P00 | [for-art-director] |

### 3.2 Ten cases (MP:57-147)

Each case: what the source says, then the transfer lesson, then what is UNKNOWN. Dates are the paper's.

**Case 1: Teemo and Beemo, Riot 2024 Art and Sustainability Update (MP:59-67)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS1-a | 61 | Riot's modelers added facial and limb geometry to support expression, built a reusable base mesh, and protected Teemo's likeness across themed skins. | EXPERIENCE (2024-09-23) | C12 | [for-rigger] |
| CS1-b | 61 | Beemo's old onesie face was designed for a head-down, forward-facing rig. The new model had to keep both faces readable under the new motion. Example of topology density that serves animation, not visual richness. | EXPERIENCE (2024-09-23) | C12 | [for-rigger] |
| CS1-c | 63 | Riot treats splash art and the modeling reference as separate: normally the splash follows the 3D model; an existing strong splash may inform a later update. Do not claim all industry assets start from finished promo art. The ChatGPT-reference-first rule is this project's mandated workflow, not a statement about Riot. | EXPERIENCE ; OPINION (application) | C12, P00 | [for-art-director] |
| CS1-d | 65 | Transfer: build a canonical base body under the costumes; list the forms that must survive at gameplay distance; ask the rigger for new joint or face needs before adding geometry; inspect costumes in the new poses, not only the rest pose. | OPINION | P00 | [for-rigger] [for-art-director] |
| CS1-e | 65 | UNKNOWN: published triangle count, number of added loops, limb-length ratio. | OPINION (evidence-gap assessment) | P00 | - |
| CS1-f | 67 | Jenna VanPelt's Beemo portfolio credits the model and the disciplines that worked on it. A portfolio is not a downloadable mesh measurement. | EXPERIENCE | C17 | - |

**Case 2: Icebox B site, VALORANT environment production (MP:69-75)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS2-a | 71 | Lydia Zanotti describes greybox, then art blockout, then art production. Icebox architecture follows exported gameplay greybox edges. Shapes are set before UVs and textures. | EXPERIENCE (2020-11-16) | C02 | [for-environment] |
| CS2-b | 71 | Large buildings mainly use tiling textures and trim sheets; special props get custom textures when fitting. Values and contrast are managed so the Agents stay readable. Much decorative detail sits above player height. | EXPERIENCE (2020-11-16) | C02 | [for-environment] [for-art-director] |
| CS2-c | 73 | Transfer: keep collision-relevant widths, occluding edges and traversal openings when interpreting a reference; build modular wall, trim and roof families; separate bespoke hero props from repeatable structure; review with player proxies in gameplay views; never copy all screenshot detail into collision or unique geometry. | OPINION | P00 | [for-environment] |
| CS2-d | 75 | The weekly playtest cadence is a historical practice, not a required small-team calendar. The UE4 instancing description is not evidence that Roblox batches the same way. | EXPERIENCE ; OPINION (boundary) | C02, P00 | [for-environment] |
| CS2-e | 75 | UNKNOWN: exact texel density, bevel size, universal module dimensions. | OPINION (evidence-gap assessment) | P00 | [for-environment] |

**Case 3: Honeydew Mei and the Bubbledew Blaster, Blizzard (MP:77-85)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS3-a | 79 | The boba-shop skin keeps Mei's silhouette without her winter clothes. The blaster keeps believable weapon mechanics; drink details carry the theme. The concept team uses prominent upper shapes for distant recognition and keeps smaller detail for close views. | EXPERIENCE (2020, day not shown) | C03 | [for-art-director] |
| CS3-b | 81 | Transfer: find the functional silhouette and the attachment or grip positions first; carry the new theme by material, secondary volume and a few distinctive cues. Gluing themed objects on a base does not make a coherent cosmetic. Test every change against the rig's mechanical limits. | OPINION | P00 | [for-rigger] |
| CS3-c | 83 | The same interview: Sniper Ana shows concept, model and rig working together to keep the coat silhouette and avoid camouflage clipping. The rejected Talon shield concept shows that a polished design can lose when gameplay role and recognition are unclear. | EXPERIENCE (2020) | C03 | [for-rigger] [for-art-director] |
| CS3-d | 85 | UNKNOWN: weapon dimensions, bevel radius, shoulder-clearance allowance, triangle budget (none published in that account). | OPINION (evidence-gap assessment) | P00 | - |

**Case 4: TF2 Pyro and the nine-class silhouette system, Valve (MP:87-93)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS4-a | 89 | Valve's 2007 paper pairs Pyro concept art with in-game art. Class silhouettes differ by proportions, weapons, footwear, hats and clothing shape. Interior clothing folds support the silhouette instead of adding unrelated noise. Environments show repeated structure without modeling every repeat; the shading supports the modeled shape. | EXPERIENCE (2007) | C04 | [for-art-director] [for-environment] |
| CS4-b | 91 | Transfer: make the grayscale or flat-silhouette render useful before detailed materials. Design folds and bevel highlights to support primary masses, not to make every face busy. For environments show a repeated construction rhythm with just enough evidence to read the structure, then test whether more geometry improves the final camera view. | OPINION | P00 | [for-art-director] [for-environment] |
| CS4-c | 93 | This is historical craft evidence. Do not recreate TF2's custom shader in Roblox. Its period GPU costs and render assumptions must not become 2026 mobile budgets. | OPINION | P00 | - |
| CS4-d | 93 | A sharp painted edge, a true geometric bevel and a normal-map edge are three different representations. Choose by the intended silhouette, deformation, view and the material path Roblox supports. | OPINION | P00 | [for-rigger] |

**Case 5: Axe's Dota 2 wearable system, Valve (MP:95-103)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS5-a | 97 | Current Axe resource page: a normal weapon slot has LOD0 2,500 triangles, LOD1 1,000 triangles and a 512x512 texture. The persona weapon has the same triangle limits but a 256x256 texture. These are slot submission limits for that hero, not whole-hero complexity, not measured shipped complexity, not Roblox phone advice. | VERIFIED (undated, acc 2026-10-21) | C06 | - |
| CS5-b | 99 | Dota's art guide ties outline, facing direction, upper-body focus, distinct value regions and rest areas together. It explicitly allows departures from the usual dark-below, light-above gradient when the design stays legible. | VERIFIED (undated, acc 2026-10-21) | C05 | [for-art-director] |
| CS5-c | 101 | Transfer: write a per-slot asset contract; inspect the whole equipped character; spend detail by the part's contribution at each display size. A weapon's polygon allowance is no reason to use it if the read is already met. | OPINION | P00 | [for-art-director] |
| CS5-d | 103 | The case matters because budgets differ by category. Copying one hero's slot limits to every Roblox pet, NPC or tool would remove that distinction. | OPINION | P00 | [for-environment] |

**Case 6: Splatana Stamper and Stringer, Nintendo Splatoon 3 (MP:105-111)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS6-a | 107 | Nintendo's developers: the Splatana Stamper comes from a staff date-stamp device; the Stringer from a fishing rod. They wanted the Stringer to belong to Splatoon without looking like a firearm. Fictional manufacturers explain the repurposed object families. | EXPERIENCE (2022-09-07) | C07 | [for-art-director] |
| CS6-b | 109 | Transfer: transform the recognizable operating principle of a real object, not only its surface. In a concept sheet show grip, load path, moving part and output direction. In blockout keep the feature that tells the object's metaphor. Ask whether the reference implies a mechanism that could move without fused geometry. | OPINION | P00 | [for-rigger] |
| CS6-c | 111 | Realistic engineering is not required; imaginative machinery is fine when it is coherent with the game world. | OPINION | P00 | [for-art-director] |
| CS6-d | 111 | UNKNOWN: proportions, material counts and textures of these Nintendo models (not published in the interview). | OPINION (evidence-gap assessment) | P00 | - |

**Case 7: Ravenwood costume and ship set, Rare (MP:113-121)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS7-a | 115 | Rare translated a raven-assassin concept across costume and ship parts. They started from an iridescent Kraken-ink material, then tuned prop and character material features and look together under game lighting. A grayscale metallic map gave a better value range than fully metallic or fully nonmetallic extremes in that look. | EXPERIENCE (2023-03-03) | C08 | [for-art-director] |
| CS7-b | 117 | The mask's first attempt to follow every pirate face shape failed visually. Keeping the concept across variable bodies was a real modeling limit, not automatic fidelity to every body variant. | EXPERIENCE (2023-03-03) | C08 | [for-rigger] |
| CS7-c | 119 | Transfer: compare related assets together in the target renderer; keep one material family across characters and props; test shape extremes, not only a median avatar. A deformation or conversion can be technically valid and still ruin the shape. | OPINION | P00 | [for-rigger] [for-art-director] |
| CS7-d | 121 | UNKNOWN: a universal metallic value (none given). Rare's custom shader is not Roblox SurfaceAppearance. The final mask-fitting solution and numeric tolerances are not established. | OPINION (evidence-gap assessment) | P00 | - |

**Case 8: Luca, Portorosso and the Paguro home, Pixar (MP:123-131)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS8-a | 125 | Pixar's notes: round organic underwater shapes against a rectilinear town; aged architecture follows designed lean, sag and twist rules, not random angle noise; characters get the widest value range while signs and environments stay more restrained; Luca's hair stresses one distinctive front curl, not equal detail everywhere. | EXPERIENCE (2021) | C09 | [for-art-director] [for-environment] |
| CS8-b | 127 | Transfer: write constructive shape rules another agent can apply: where masses lean, what causes sag, which edges stay structural, which accent owns the silhouette, where rest is intended. A random generator is not art direction. | OPINION | P00 | [for-environment] [for-art-director] |
| CS8-c | 129 | Borrow the hierarchy and the causally motivated exaggeration, not film mesh density or render complexity. A generated reference may suggest a leaning facade; the modeler still has to reconcile doors, floor levels, collision and modular mating edges. | OPINION | P00 | [for-environment] |
| CS8-d | 131 | UNKNOWN: a universal lean angle, bevel width, mobile texture budget or geometry cost. | OPINION (evidence-gap assessment) | P00 | - |

**Case 9: Village sample island, Epic (MP:133-139)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS9-a | 135 | Epic reports: structures cut by roughly 50% for Village's isometric view; cliffs at 50% scale; a -59 degree interior camera with the front walls removed to keep the player visible; prop layouts make gaps that look traversable actually traversable. These values describe one authored sample, not a game-art standard. | EXPERIENCE (2023-12-18) | C10 | [for-environment] |
| CS9-b | 137 | Transfer: model to the real camera and movement contract, not to a reference sheet alone. Check player visibility behind props, readable openings, interior occlusion, and jump height against ledges. A building may need a camera-driven cutaway or another approved visibility system, not literal completeness from every viewpoint. | OPINION | P00 | [for-environment] |
| CS9-c | 139 | Do not halve Roblox models to copy the sample. Reuse the test: compare candidate scale against the intended player, camera and collision. Do not delete unseen backs unless the game guarantees they stay unseen and irrelevant to collision, shadows and other cameras. | OPINION | P00 | [for-environment] |

**Case 10: Sable's modular outfits, hoverbikes and environment, Shedworks (MP:141-147)**

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| CS10-a | 143 | Shedworks' case study: low-poly, handcrafted-looking assets; color drives mood; interchangeable costume and vehicle parts; procedural terrain generated before runtime. Fineberg estimates nearly 80% of the environments used ProBuilder: a developer estimate, not a measured efficiency claim. | EXPERIENCE (2022-07-12) | C11 | [for-environment] |
| CS10-b | 145 | Transfer: build a small family of compatible silhouettes, attachment interfaces and materials, then make variety by composing controlled parts. Build generation-time tools that leave clean deliverable meshes; do not carry authoring scaffolding into the runtime asset. | OPINION | P00 | [for-environment] |
| CS10-c | 147 | The transferable idea is scope and modular construction, not Unity component behavior or a promise that the same share or tool works in Roblox. A small team's success and a simple style set no per-asset performance budget. | OPINION | P00 | - |

### 3.3 Synthesis and useful disagreements (MP:149-175)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| SY1 | 153 | Reference fidelity is not pixel servitude. Sort the approved drawing into design invariants, approximate visual guidance and unresolved geometry. Riot's Teemo case (concept versus splash order) and Rare's Ravenwood case (faithful translation versus fitting every face literally) do not justify silently changing the approved design. | OPINION (synthesis of C12, C08) | P00 | [for-art-director] |
| SY2 | 155 | Proposed invariants: asset identity; primary silhouette; approved proportions; palette roles; attachment positions; readable facing; essential theme cues; movement topology; gameplay envelope. Proposed negotiables: hidden-surface solution; minor edge treatment; internal support construction; texture versus geometry. Working categories only; never a license to override the art director. | OPINION | P00 | [for-art-director] [for-rigger] |
| SY3 | 157 | When front, side and back views disagree, write an issue record: conflicting landmarks, affected volumes, candidate fixes. Get an art-direction decision before detailed modeling. Never average contradictory views into an unapproved fourth design. | OPINION | P00 | [for-art-director] |
| SY4 | 161 | Stylization is not one shader. TF2's illustrative treatment and Rare's Ravenwood materials solve different problems. Neither means stylized assets must be flat unlit paint, and adding metallic or roughness maps does not guarantee quality. | OPINION (synthesis of C04, C08) | P00 | [for-art-director] |
| SY5 | 161 | Dota's shader doc treats textures as parts that cooperate with its own hero shader; texture budgets are hero- and slot-specific. Its example: 256x256 in game versus 1024x1024 source is a 4x scale on each edge, not four times the pixels (my arithmetic: 16x the pixels). | VERIFIED (undated, acc 2026-10-21) | C15 | - |
| SY6 | 163 | Pick a rendering contract before polishing: expected lighting range; materials Roblox supports; what each map channel means; whether painted shading is intended; presentation scale; texture ownership and reuse. Review in three passes: neutral material, final material, target-game lighting. These are review modes, not three required runtime materials. | OPINION | P00 | [for-art-director] |
| SY7 | 167 | Shape language is a vocabulary tied to context. Do not teach "circle = good, triangle = evil". Use shape relationships, references and world rules to express this game's tone, role and manufacturing logic. A heroic weapon may be angular; a threatening creature may be round. The art director picks the vocabulary. | OPINION | P00 | [for-art-director] |
| SY8 | 169 | A value gradient or a detailed head is not required for every camera angle. Review the approved in-game view. A landmark building, a tiny collectible pet, a first-person weapon and a cosmetic portrait can need different identity anchors. | OPINION | P00 | [for-art-director] [for-environment] |
| SY9 | 173 | UNKNOWN: no primary studio source gives a transferable fixed bevel width (meters or studs), standard bevel segment count, detail-to-rest percentage or texel density for this pipeline. Label such fields UNSPECIFIED until authored for the project. Do not fill them from internet convention. | OPINION (evidence-gap assessment) | P00 | [for-art-director] |
| SY10 | 175 | Bevel test (proposed): keep dimensions and camera fixed. Render (1) no bevel, (2) a silhouette-keeping bevel, (3) the baked or normal-map alternative where supported. Compare contour, specular stability, style and geometry cost. Approve one variant and reuse its construction rule within that material or object family. This is a check method, not proof any bevel is best. | OPINION | P00 | [for-art-director] |

### 3.4 Supplementary evidence and limits (MP:177-185)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| SP1 | 179 | Disney's public modeler-role page links Visual Development Artists, modelers and Character TDs; story needs and technical needs both shape the asset. It supports collaboration, not a phone budget derived from film. | VERIFIED (undated, acc 2026-10-21) | C13 | [for-rigger] [for-art-director] |
| SP2 | 181 | Supercell's Games First 2024 talk description names creative cohesion, humor, nostalgia and 1980s influences in Brawl Stars characters. Only the description was read: do not invent a transcript, a five-pillar list, model stats or a Gus case. | EXPERIENCE (2024-11-13 upload) | C14 | [for-art-director] |
| SP3 | 181 | Supercell Make (2019 launch) documents downloadable character assets: historical proof of official references. Whether the campaign or downloads exist today needs a separate check. | VERIFIED (2019-11-11) | C18 | - |
| SP4 | 183 | Disney's SIGGRAPH 2022 floral-modeling page says Encanto's Isabela room involved procedural-modeling challenges. The linked paper was not read: do not invent its method or counts. | VERIFIED (SIGGRAPH 2022) | C16 | - |
| SP5 | 185 | No primary Deadlock model-production breakdown and no transferable Wild Rift mobile asset budget were verified. Do not label TF2 or Dota methods as Deadlock facts. Do not read Wild Rift display-model screenshots as in-match complexity. | OPINION (evidence-gap assessment) | P00 | [for-art-director] |

### 3.5 Paper table after the cases (MP:187-197)

Columns as the paper: rule, number, mark, source and date.

| ID | MP | Rule | Number or limit | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| TB1 | 188 | Reuse a canonical base mesh while keeping identity and the needed expression | Added geometry count UNKNOWN | EXPERIENCE | C12 (2024-09-23) |
| TB2 | 189 | Greybox or art blockout before detailed architecture; tiling and trim materials for structures | Weekly playtests reported, not a mandate | EXPERIENCE | C02 (2020-11-16) |
| TB3 | 190 | Shape and material together make the read | 9 TF2 classes, not a Roblox asset quota | EXPERIENCE | C04 (2007) |
| TB4 | 191 | Budget by real category or slot | Axe weapon 2,500 / 1,000 triangles (LOD0 / LOD1); 512x512 for the regular slot versus 256x256 persona | VERIFIED | C06 (undated, acc 2026-10-21) |
| TB5 | 192 | Make spatial choices for the specific camera, not a universal scale | Village: structures about 50%; -59 degree interior camera | EXPERIENCE | C10 (2023-12-18) |
| TB6 | 193 | Review materials across related assets under game lighting | No published universal metallic value | EXPERIENCE | C08 (2023-03-03) |
| TB7 | 194 | Use deliberate deformation and aging rules, not random wonkiness | No published universal angle | EXPERIENCE | C09 (2021) |
| TB8 | 195 | Use modular assets for scoped variety | "Nearly 80%" ProBuilder is Sable-specific | EXPERIENCE | C11 (2022-07-12) |
| TB9 | 196 | Keep source texture and runtime texture separate | Example 256x256 runtime, 1024x1024 source | VERIFIED | C15 (undated, acc 2026-10-21) |
| TB10 | 197 | Accept style, rig and runtime separately | No invented approval-time target | OPINION | P00 (2026-10-21) |

## 4. Section 2: reference images with ChatGPT (MP:199-303)

### 4.1 Tool reality (MP:201-211)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| RF1 | 203 | OpenAI released ChatGPT Images 2.5 on 2026-09-08 with API models GPT-Image-2.5 Flare (faster) and Sunburst (higher precision, longer wait). Gains in reference fidelity and repeated editing are vendor-reported, not independently measured guarantees. Sketch and image comments are ChatGPT product controls, not Blender geometry tools. | VERIFIED (2026-09-08) | I01 | [for-art-director] |
| RF2 | 205 | ChatGPT can generate from a prompt, take an uploaded image to edit, and edit a selected region. The Help Center warns that an edit can change areas outside the selection. The UI allows arbitrary aspect-ratio requests; that does not allow arbitrary pixel sizes in the API. The page says templates are unavailable in Work mode and describes Sketch on mobile. Check the real surface; do not promise one control everywhere. | VERIFIED (live page, acc 2026-10-21; "updated yesterday", no absolute date) | I05 | [for-art-director] |
| RF3 | 207 | Images API: pick the image model directly. Responses API: use a supported mainline model and name the image model inside its image-generation tool. The 2.5 models take quality low, medium, high, xhigh, max, auto. Custom sizes: both edges divisible by 16, each edge at most 3,840 px, aspect ratio between 1:3 and 3:1, total pixels 655,360 to 8,294,400. Outputs above 2560x1440 are experimental. These limit image output, not Roblox textures. The guide still admits failures in recurring-character consistency and exact structured layout. | VERIFIED (live doc, acc 2026-10-21) | I02 | - |
| RF4 | 209 | Images edits endpoint: up to 16 input images, each PNG, WebP or JPG and under 50 MB; lists dated 2026-09-08 snapshots of both 2.5 models. This does not set a 16-image allowance in every ChatGPT interface, and 16 images do not improve any given asset. | VERIFIED (live reference, acc 2026-10-21) | I07 | - |
| RF5 | 211 | OpenAI advice: compare model candidates with the same prompt, references, size and output format; test full edit sequences. Equal quality labels do not mean equal results across models. For transparent output, inspect the real alpha channel. The guide documents leaving out input_fidelity for GPT Image 2 while older-model advice used it: do not reuse an old GPT Image 1 recipe on a current model without checking its supported parameters. | VERIFIED (live doc, acc 2026-10-21) | I03 | - |

### 4.2 Reference contract and prompting (MP:213-247)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| RF6 | 213 | Fixed workflow: ChatGPT concept or reference image before any mesh work. A plausible image is not an approved build spec. Owner picks the design; art director sets style fit; modeler checks that the shown solid can exist; rigger and animator check the movement assumptions. An image shows intended look, not hidden topology, mechanical construction, scale, collision shape or skinning quality. | OPINION | P00 | [for-art-director] [for-rigger] |
| RF7 | 217 | Open an asset record before generating: asset ID, function, expected camera distance, key silhouette, scale against the player, required movement, attachment points, material categories, palette, prohibited detail, authoritative image revision. If the brief gives no numeric scale, keep an UNRESOLVED field, not an invented studio standard. The modeler may propose a size for owner or art-director approval; an authored size is not an industry measurement. | OPINION | P00 | [for-art-director] |
| RF8 | 219 | OpenAI advice: state subject, style, framing and lighting; give each uploaded reference an explicit role; revise in small targeted steps and restate what must stay unchanged. | VERIFIED (2026-04-10) | I04 | - |
| RF9 | 219 | Apply it with separate roles: identity reference, style reference, scale reference, construction callout. Do not merge their geometry by accident. A palette reference must not replace the target's anatomy; a pose reference must not override the approved costume. | OPINION | P00 | [for-art-director] |
| RF10 | 221 | Make one anchor concept first, approve its primary forms, then ask for the turnaround from that anchor. A front, side, back and 3/4 sheet is a review deliverable, not four separate designs. Keep pose, scale and design revision fixed. Name the side shown, using the asset's own left and right. For asymmetric designs ask for both sides or a named asymmetry callout. A beauty image sets appeal; orthographic panels set dimensions; neither silently overrules the other. | OPINION | P00 | [for-art-director] [for-rigger] |
| RF11 | 223 | Keep real measurements in a text manifest; labels and drawn rulers in the image are illustrations to check, not instruments. Keep color values in the style guide, outside the image. Colors sampled from a concept are lit colors, not material base colors. | OPINION | P00 | [for-art-director] |
| RF12 | 227 | The prompt templates are the paper's own OPINION: not tested prompts, not OpenAI guarantees. Replace every bracket with an approved decision; never send unresolved placeholders. Numbers come only from the brief or an approved authored choice. Do not add arbitrary percentages, polygon budgets, bevel widths or a "universal neutral-pose angle". | OPINION | P00 | - |
| RF13 | 231 | FIXED STYLE BLOCK (fields): asset ID, revision, approved style name. Image 1 sets identity or geometry; image 2 sets only palette, material or shape style; image 3 (optional) sets only pose or scale. Preserve approved primary proportions, shape hierarchy, palette, material separation and signature silhouette cues. State approved edge or bevel language, detail density, texture treatment. Do not copy unwanted geometry from the style reference. List prohibited features. Plain background, even neutral light, no dramatic rim light, no cast shadows that hide form, no depth of field or atmosphere. It is a construction reference, not a promo shot. No added objects, decoration or redesign. | OPINION | P00 | [for-art-director] |
| RF14 | 235 | CHARACTER TEMPLATE (fields): the same character in front, labeled-side and back orthographic views plus a separate 3/4 volume view. All orthographic panels at one scale with an aligned foot baseline and head height. Approved rest pose (T, A or other) with identical limb positions in every panel. Hands and feet fully visible. Asymmetry on the correct anatomical side. List clothing and gear. Show where head, hair, jaw, shoulder and held item connect, without inventing exposed mechanical joints. Detail callouts separate from the main views. A player or scale marker only on request, not overlapping. No action pose and no perspective foreshortening in orthographic panels. | OPINION | P00 | [for-rigger] [for-art-director] |
| RF15 | 239 | CREATURE TEMPLATE (fields): front, labeled side, back, separate 3/4. A written inventory of legs, arms, wings, eyes, horns, tail kept identical across views. Approved neutral support pose. Near and far limbs both legible, never merged. Give tail root and wing roots and jaw construction. Extended, folded, underside or paw callouts are alternative states of the same anatomy, not extra limbs. Keep body ratios and landmarks. Fur, fins or ornament must not hide required joints. | OPINION | P00 | [for-rigger] |
| RF16 | 243 | PROP, TOOL, WEAPON, VEHICLE TEMPLATE (fields): front, side, back, separate 3/4; top or underside only to settle an ambiguity. Say who uses it and through which grip, seat or control. Keep approved functional parts, lengths and diameters, contact surfaces, attachment points. Separate moving parts from the fixed body. Open or closed, assembled or exploded callouts only on request, with the same part counts. Keep negative spaces, openings and thicknesses. No decorative screws, extra handles, stands or background objects unless specified. | OPINION | P00 | [for-rigger] |
| RF17 | 247 | BUILDING OR ENVIRONMENT PIECE TEMPLATE (fields): front, side, rear orthographic elevations plus a 3/4 massing view; a plan view if the approved footprint needs it. Grid or module size, dimensions and openings come from approved values. Keep roof pitch, floor heights, wall thickness and the count and position of windows and doors in all views. Mark traversable openings, decorative insets and sealed surfaces. Show modular boundaries and repeat connections in separate callouts without inventing a new kit. Same silhouette and asymmetry in every panel. Separate approved player scale marker. No perspective distortion to hide mismatched elevations. | OPINION | P00 | [for-environment] |

### 4.3 Reject or repair before modeling (MP:249-275)

Pass or fail checks. Record the failed panel and feature, not a subjective score (MP:251).

| ID | MP | Check | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| RF18-a | 253 | Inventory: every required limb, handle, wheel, window, wing, socket and ornament exists once, in the intended place. Near and far overlap does not prove a part is missing; look at a view that resolves it. | OPINION | P00 | - |
| RF18-b | 255 | Cross-view identity: eye and ear positions, belt height, roofline, grip shape, silhouette landmarks and material borders match between views. | OPINION | P00 | - |
| RF18-c | 257 | Geometric possibility: surfaces are plausibly continuous and have thickness; straps connect; holes stay holes; any floating part has an intended reason. | OPINION | P00 | - |
| RF18-d | 259 | Projection: orthographic panels do not shrink far features or show inconsistent side surfaces. The word "orthographic" in a label does not pass the check. | OPINION | P00 | - |
| RF18-e | 261 | Pose: the neutral pose is consistent; the rigger can find likely joint centers and movement clearance. | OPINION | P00 | [for-rigger] |
| RF18-f | 263 | Occlusion: the image shows the needed seams, attachment roots and negative spaces. Fix a hidden area with an extra view, not an invented confident guess. | OPINION | P00 | [for-rigger] |
| RF18-g | 265 | Style: primary forms and focal detail survive at the intended on-screen size. Reject a polished image that is off style. | OPINION | P00 | [for-art-director] |
| RF18-h | 267 | Color and material: color blocks stay on the same parts in every view; glare and painted shadow are not read as physical relief. | OPINION | P00 | [for-art-director] |
| RF18-i | 269 | Background and transparency: the object is isolated and contact shadows do not hide its edge. If alpha is requested, inspect the file; a painted checkerboard is not transparency. | OPINION | P00 | - |
| RF18-j | 271 | Scale: approved sizes are stored outside the pixels and checked against landmarks; the generator has not resized a limb, prop or floor by itself. | OPINION | P00 | - |

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| RF19 | 273 | OpenAI documents approximate counting, unreliable fine spatial localization, and possible image resizing in vision analysis. | VERIFIED (live doc, acc 2026-10-21) | I06 | - |
| RF20 | 273 | So an AI review must combine image inspection with measured pixel landmarks and later mesh data. Ask the vision model to flag uncertainty. "Looks correct" must not override a part inventory or a numeric size check. Image-similarity scores may rank revisions, but no universal pass threshold was found for this pipeline. | OPINION | P00 | [for-art-director] |
| RF21 | 275 | Repair method: attach the approved anchor and the faulty image; name the exact panel and mismatch; keep every accepted feature; inspect the whole revised sheet. If edits keep drifting, go back to the approved anchor instead of editing a damaged descendant. If views stay inconsistent, the owner or art director chooses the form; the modeler must not average views into an accidental design. | OPINION | P00 | [for-art-director] |

### 4.4 Hand-modeling guide versus Tripo input (MP:277-283)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| RF22 | 279 | Keep two exports of the approved reference pack. Hand-modeling package: labeled turnarounds, detail panels, dimensions, material notes, seam plans, rig needs. Image-to-3D input: one clean, unambiguous picture of the target solid in the format the chosen generator needs. A model sheet with labels, callouts and repeated subjects is not automatically a good single-image reconstruction input. Crop or generate the single subject and keep the approved design. (Owner J007-D4: the owner runs Tripo; the modeler prepares these inputs.) | OPINION | P00 | - |
| RF23 | 281 | If the chosen Tripo route accepts several views, give separately checked views in its documented slots and order, never an arbitrary collage. The paper promises no view order here; its version-specific Tripo rules are in its section 5 (outside this note's range). Check cross-view consistency before generation. A prettier image does not remove ambiguity about the back, undercuts, thin surfaces or joints. | OPINION | P00 | - |
| RF24 | 283 | Seesaw Man (Santiago Vivanco Morillo): ChatGPT image iteration, then Hunyuan 3D conversion, then Blender retopology and cleanup, then texture refinement. One artist's hybrid process, not a controlled Images 2.5 or Tripo test. The paper found no strong current independent benchmark measuring reference-sheet consistency, usable topology and Roblox phone performance together. Do not turn personal demos into a success rate. | EXPERIENCE (undated, acc 2026-10-21) | I08 | - |

### 4.5 Approval, handoff, boundaries (MP:285-303)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| RF25 | 287 | Roles: the modeler writes the brief and prompt, generates and screens candidates, and shows only viable designs with unresolved regions named. The art director checks visual language and set consistency. Rigger and animator check rest pose, clearances and whether motion needs a continuous deforming surface or rigid pieces. The owner approves the chosen reference and any material design change. Approval covers a named revision with its stated sizes and assumptions; it does not claim physical perfection. Later topology choices inside the approved design stay with the modeler; escalate if they change visible form or movement. | OPINION | P00 | [for-art-director] [for-rigger] |
| RF26 | 289 | After approval keep: the exact images, prompt, model identifier if shown, date, requested settings, image sizes, revision, role of each reference, and the approval record. Keep beauty and construction images separate. Give the approved pack to both the hand-modeling and Tripo branches. In Blender, compare aligned renders with it at blockout, at finished topology and at final material; do not wait for texture polish to find shape errors. | OPINION | P00 | [for-art-director] |
| RF27 | 293 | The generation guide says image and mask files match in format and size and stay under 50 MB. The Python SDK mask field says PNG, under 4 MB, same dimensions. | VERIFIED (live sources, acc 2026-10-21) | I02, I09 | - |
| RF28 | 293 | Build requests with the narrower mask rule and check the endpoint and model; do not assume the mismatch is settled. The paper ran no mask request. | OPINION | P00 | - |
| RF29 | 295 | OpenAI's better-consistency claim and its limitation warning do not contradict: better is not perfect. ChatGPT's aspect-ratio wording and the API's pixel limits belong to different interfaces. Do not paste API parameters or limits into a ChatGPT prompt as if they were UI controls. A model output is not a calibrated camera, a scene graph or a watertight mesh. | OPINION | P00 | - |

Paper table (MP:297-303), kept as rows:

| ID | MP | Rule | Number or limit | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| TB11 | 298 | Use current product and API names, not a legacy recipe | Images 2.5; Flare and Sunburst | VERIFIED | I01 (2026-09-08) |
| TB12 | 299 | Respect the edit-endpoint input limits, not every UI | Up to 16 images; each under 50 MB | VERIFIED | I07 (acc 2026-10-21) |
| TB13 | 300 | Treat reference geometry as unchecked until checked | No guaranteed error tolerance | OPINION | P00 (2026-10-21); motivated by I02, I06 |
| TB14 | 301 | Keep required orthographic panels plus a separate volume view | Front, side, back, 3/4 as the brief asks | OPINION | P00 (2026-10-21) |
| TB15 | 302 | Approve a named reference revision before building the mesh | No universal number of iterations | OPINION | P00 (2026-10-21) |
| TB16 | 303 | Tell mask limits apart from ordinary input-image limits | SDK mask under 4 MB, PNG | VERIFIED | I09 (acc 2026-10-21) |

## 5. Section 3: from approved reference to a testable blockout (MP:305-342)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| BK1 | 309 | Turn the approved reference into a model contract before any geometry: asset identity, camera distance, visible sides, gameplay role, approximate scale against the player, style reference revision, palette, expected motion, attachment points, collision needs, destination scene limits. A far decorative building and a climbable one can share a design but need different interior surfaces, collision and review cameras. A weapon seen only in an icon and the same weapon in first person have different review needs. | OPINION | P00 | [for-environment] [for-rigger] |
| BK2 | 311 | Split image evidence from inferred geometry. Mark every feature as shown, inferred, deliberately omitted or awaiting a decision. A hidden back is a design question, not permission for random detail. If views disagree on limb length, shoulder width or appendage count, resolve the reference before building the conflict into topology. Cosmetic doubt goes to the art director; doubt about movement, silhouette, scale or construction goes to the relevant owner before costly finishing. | OPINION | P00 | [for-art-director] [for-rigger] |
| BK3 | 313 | Make the contract machine-readable and human-reviewable, with named fields: reference image IDs, approved view, semantic part list, required symmetry and deliberate asymmetry, landmark descriptions, intended articulation, materials, target devices, budgets, provenance. Keep unknowns explicit. A generated sheet shows desired look; it is not a dimensioned drawing. | OPINION | P00 | - |
| BK4 | 317 | Block out the whole asset before polishing a part: large masses, then secondary shapes, then small features that survive the viewing conditions. Character: body proportions and limb relations before fingers or buckles. Vehicle: chassis, wheelbase, occupant or weapon relation before vents. Building: footprint, height, roof masses, entrances, player-scale circulation before roof tiles. Tool: grip, working head and leverage before surface decoration. | OPINION | P00 | [for-environment] |
| BK5 | 319 | The blockout must show the design is recognizable, proportionally coherent and feasible to animate. Use temporary flat materials and neutral light so texture and highlights do not hide weak geometry. Render the whole object and the key interactions, not the best angle. Keep the previous approved blockout so later "improvements" can be compared with it. | OPINION | P00 | [for-rigger] [for-art-director] |
| BK6 | 321 | Blender documents mesh modeling as primitive blockout first, then detail. | VERIFIED | B02 | - |
| BK7 | 321 | Blender documents orthographic projection as keeping parallel lines parallel, with no shrink by distance. | VERIFIED | B15 | - |
| BK8 | 321 | Blender's world_to_camera_view maps world points into camera-frame coordinates: (0,0) is bottom-left, (1,1) is top-right, negative depth is behind the camera. | VERIFIED | B21 | - |
| BK9 | 321 | Use those coordinates to compare approved landmarks on consistently cropped renders, but add a visibility mask, because projection alone does not prove a landmark is not hidden. | OPINION | P00 | - |
| BK10 | 325 | Compare like with like: match camera orientation and projection, framing, scale and pose. A perspective picture on a white background is not orthographic. If the projection cannot be told, record the doubt and compare stable landmarks and silhouettes under several plausible cameras; do not bend the mesh to fit one accidental camera. | OPINION | P00 | - |
| BK11 | 327 | Save four views: a neutral render, a silhouette mask, a material-ID view and a lit in-game-context view. Overlays show where views disagree. An aggregate similarity score is never the only approval test: a texture can fake a geometric feature in one view; a hidden intersection may not change the silhouette; a high score can hide the loss of the one feature that identifies the character. Also compare semantic landmarks and required functions. | OPINION | P00 | [for-art-director] |
| BK12 | 329 | Diagnose each mismatch before editing: geometry, camera, pose, material, lighting or reference inconsistency. Change one cause at a time. Example: a head that looks small only in the perspective view must not be rescaled (it may break the orthographic match). An edge that vanishes only under flat light may not need more geometry. A piece that reads only through a painted dark outline needs a check that the outline survives game lighting and screen size. | OPINION | P00 | - |
| BK13 | 331 | Tolerances for silhouette mismatch, landmark shift, overlap and color difference are project acceptance choices that depend on camera, style and feature importance. No universal percentage. Start from approved exemplar assets and ask the art director which differences are unacceptable. Keep the measurement and the render so the owner can review an exception. | OPINION | P00 | [for-art-director] |
| BK14 | 335 | Blockout approval package: reference comparison views; dimensions in authoring units and in Roblox units; named parts; the expected articulation method; a provisional collision volume; open questions. Explain the biggest remaining risks, not every edit. Ask approval for proportions, silhouette, functional layout and construction direction. Surface detail stays reversible and is no reason to hide a failed silhouette. | OPINION | P00 | [for-art-director] [for-rigger] |

Paper table (MP:337-342), kept as rows:

| ID | MP | Rule | Number or limit | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| TB17 | 338 | The contract separates appearance from function | One contract per asset revision (proposed workflow) | OPINION | P00 (2026-10-21) |
| TB18 | 339 | Match comparison camera and pose | No universal numeric tolerance | OPINION | P00 (2026-10-21) |
| TB19 | 340 | Record hidden or inconsistent geometry | UNKNOWN until resolved or explicitly approved | OPINION | P00 (2026-10-21) |
| TB20 | 341 | Inspect silhouette and landmarks beyond image score | Threshold is project-specific | OPINION | P00 (2026-10-21) |
| TB21 | 342 | Approve primary shape before surface finishing | No sourced fixed iteration count | OPINION | P00 (2026-10-21) |

## 6. Section 4: deliberate hand modeling in Blender (MP:344-421)

### 6.1 Version, FBX, stack, tools (MP:346-360)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| HM1 | 346 | Blender 5.2 LTS first released 2026-07-14; 5.2.2 came 2026-09-15 and is the latest production download the paper verified. 5.2 support ends July 2028. | VERIFIED | B01 | - |
| HM2 | 346 | Pin the executable and API version in the asset manifest. Do not treat /api/current or /api/main docs as stable references. A feature seen in development docs may be missing from the pinned production build. | OPINION | P00 | - |
| HM3 | 348 | Blender's current FBX manual describes a new importer and sends export to the FBX add-on. The page titled "FBX (Legacy)" holds importer and exporter text; "legacy" does not make every item there the current importer. | VERIFIED | B30, B22 | [for-rigger] |
| HM4 | 348 | The legacy page says export Scale defaults to 10; the 5.2 Python operator signature shows global_scale=1.0. The paper treats the signature as the version-specific default, does not turn the legacy prose into a Roblox export preset, and says neither default is an artistic scale decision. | VERIFIED (conflict) ; OPINION | B22, B23, P00 | [for-rigger] |
| HM5 | 350 | Modifiers run from the top of the stack down and keep the base mesh until applied; order changes the result. | VERIFIED | B03 | - |
| HM6 | 350 | Keep an editable authoring object separate from export-derived geometry. Build primary volumes from parameterized primitives, then secondary masses, then only details that survive the screen size. Use semantic parameters (blade length, handle clearance, roof overhang), not an untraceable vertex-coordinate script. Use deterministic named collections so a rerun does not create duplicates. | OPINION | P00 | - |
| HM7 | 352 | Mirror works around object-local axes or origin, or a given mirror object. Clipping holds edit-mode vertices at the mirror plane; merging depends on the merge distance. Vertex-group mirroring has naming rules and conditions about already-existing empty groups. | VERIFIED (2026-08-07) | B08 | [for-rigger] |
| HM8 | 352 | Symmetry is a construction aid, not a duty to erase approved asymmetry (costumes, scratches, silhouettes). Inspect the center seam and the rest-pose silhouette before freezing the modifier. Do not weld the whole mesh just because the center seam is open. | OPINION | P00 | [for-rigger] |
| HM9 | 354 | Bevel width can mean offset, width, depth, percent or absolute distance. Segments is the number of added loops. The profile shape has no effect below 2 segments. | VERIFIED | B04 | - |
| HM10 | 354 | Record which width meaning the script uses. Pick width from object scale, wanted edge highlight and screen-space silhouette, not one copied 0.02 for every object. The manual's sample widths 0.1, 0.3, 0.5 show behavior; they are not stylized-game advice. Add only enough segments for the approved shape, then check the evaluated triangle increase. A painted or baked edge accent cannot replace geometry where the outline itself must change. | OPINION | P00 | - |
| HM11 | 356 | Boolean combines volumes; only manifold inputs are guaranteed good results. Float solver does not support overlapping geometry. Exact handles overlap at higher compute cost. Manifold needs manifold inputs, except the documented plane-difference case. | VERIFIED | B05 | - |
| HM12 | 356 | After a cut, check shading, thin slivers, coplanar fragments, interior faces and bend regions. "Boolean succeeded" does not mean game-ready. If a cut crosses a deforming shoulder, redesign the topology; do not hope automatic triangulation will animate well. | OPINION | P00 | [for-rigger] |
| HM13 | 358 | Decimate Collapse works on a triangle-based ratio, so displayed polygon counts may not follow the naive ratio while polygons stay untriangulated. Ratio 1.0 keeps the mesh; 0.5 targets half the triangle-based complexity. These show behavior; they are not budget advice. | VERIFIED | B06 | - |
| HM14 | 358 | Voxel remesh rebuilds a uniform outer surface, ignores modifiers and shape keys, and is not advised for deformation topology. Automatic remeshing usually gives no topology flow that suits animation. | VERIFIED | B07 | [for-rigger] |
| HM15 | 358 | Use decimation for a static irregular rock when silhouette and texture stay sound. Use deliberate retopology for a face, a bending limb or a mechanical contact surface. Neither route proves quality without preview and runtime validation. Keep the original source and the material and texture inputs before changing topology. | OPINION | P00 | [for-rigger] |
| HM16 | 360 | Baking can move base color and normal information to texture targets; it needs UVs and an active image node or color attribute. Selected-to-Active casts from the active low-poly surface toward the high detail; a cage or ray distance sets the projection. Tangent-space normals can follow deformation. Margins protect UV seams under filtering and mipmaps. | VERIFIED | B12 | [for-rigger] |
| HM17 | 360 | Retopologize first, settle the triangulation and normals used for export, then bake. Check projection errors at cavities, contacts and close parallel surfaces. Do not bake a lit beauty image into base color. A high-poly sculpt gives authoring freedom, not runtime quality. No universal cage extrusion or pixel margin is claimed. | OPINION | P00 | - |

### 6.2 Python and MCP operating recipe (MP:362-414)

| ID | MP | Lesson | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| HM18 | 364 | Mesh data holds vertices, edges, polygon corners (loops), polygons, UVs and color attributes. UVs belong to corners, not simply to a spatial vertex. Mesh.validate() repairs or removes invalid geometry and returns whether it changed anything: it is not a harmless read-only test. from_pydata does not stop all invalid input. | VERIFIED | B09 | - |
| HM19 | 364 | Base and evaluated meshes differ. Measure modifier results on the evaluated (dependency-graph) object. A temporary to_mesh() result belongs to its object and must be cleared; keeping a result needs another route. | VERIFIED | B10 | - |
| HM20 | 364 | For a full UV and attribute inventory, call to_mesh with preserve_all_data_layers=True and the dependency graph. The default computes only a subset needed for viewport or render. | VERIFIED | B32 | - |
| HM21 | 364 | BMesh gives manifold, boundary, wire and connectivity inspection. | VERIFIED | B11 | - |
| HM22 | 364 | These APIs support a report. They cannot know "this face is the shoulder" without a semantic design or rig reading. | OPINION | P00 | [for-rigger] |
| HM23 | 366-412 | Pseudocode, labeled unexecuted (APIs B09-B11, B32), as a step list: (1) read the approved brief, style or reference revision and rig needs; (2) assert the running Blender version equals the pipeline manifest; (3) for each export-source object record a stable asset ID, parent, transforms and material assignments; (4) take the evaluated object from the current dependency graph; (5) make a temporary mesh with preserve_all_data_layers=True; (6) compute loop triangles; record evaluated triangle count, vertex count and UV-layer inventory; (7) turn evaluated vertices to world coordinates and record axis-aligned size in the chosen authoring units; (8) in a temporary BMesh list boundary, wire and non-manifold edges, connected islands, degenerate areas and self-intersection candidates; (9) compare flags with the approved list of intentional open surfaces; (10) always clear the temporary mesh (finally block); (11) run validate() on a COPY if repair diagnostics are wanted, and keep the original evidence; (12) render locked reference cameras plus gameplay-distance views; (13) compare shape, contacts, colors and motion-clearance previews; (14) export only the approved collection with an explicit saved settings manifest; (15) import in Roblox and re-measure size, materials, pivots and look. | OPINION (unexecuted) | P00, B09, B10, B11, B32 | [for-rigger] |
| HM24 | 414 | Connected islands are not the same as semantic parts: a character can have loose eyes and still be one character, and a fused mesh can wrongly glue a hand to a tool. A non-manifold flag is a diagnostic, not a universal reject: an intentionally open cloth surface differs from an accidental hole. Finite-coordinate, triangle-count and normal-direction checks need rendered proof beside them. Do not run repair operators automatically on every flag. | OPINION | P00 | [for-rigger] |

Paper table (MP:416-421), kept as rows:

| ID | MP | Rule | Number or limit | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| TB22 | 417 | Pin the current stable version | 5.2.2 LTS; 2026-09-15 | VERIFIED | B01 |
| TB23 | 418 | Count evaluated triangles | Decimate ratio uses triangles, not a naive polygon count | VERIFIED | B06, B09, B10 (acc 2026-10-21) |
| TB24 | 419 | Name the bevel parameter meaning | Profile needs at least 2 segments to change shape | VERIFIED | B04 (acc 2026-10-21) |
| TB25 | 420 | Boolean robustness depends on manifold inputs | No universal solver-time budget | VERIFIED | B05 (acc 2026-10-21) |
| TB26 | 421 | Remesh is not deformation retopology | No universal acceptable decimation ratio | VERIFIED / OPINION | B07 (acc 2026-10-21) |

## 7. Number register (lines 1-422, plus register values the rules lean on)

Rows with MP lines above 976 are values from the paper's source register quoted for rules 10-13, which the body (lines 1-422) never explains (see gap G10). "Scope" is the condition the number holds under.

| ID | Value | Unit and scope | MP | Src | Tag |
| --- | --- | --- | --- | --- | --- |
| NR1 | 2,500 / 1,000 | triangles, LOD0 / LOD1, Axe regular weapon slot (Dota 2 workshop, current page) | 97, 191 | C06 | VERIFIED |
| NR2 | 512x512 / 256x256 | texture, regular slot / persona weapon slot, Axe | 97, 191 | C06 | VERIFIED |
| NR3 | 256x256 vs 1024x1024 | in-game vs source texture example, Dota hero shader; 4x per edge, 16x pixels (my arithmetic) | 161, 196 | C15 | VERIFIED |
| NR4 | 9 | TF2 classes in the silhouette system; not a Roblox quota | 87, 190 | C04 | EXPERIENCE |
| NR5 | about 50% / 50% / -59 degrees | Village structure scale / cliff scale / interior camera angle; one sample | 135, 192 | C10 | EXPERIENCE |
| NR6 | nearly 80% | environments built with ProBuilder, Sable; developer estimate | 143, 195 | C11 | EXPERIENCE |
| NR7 | 2026-09-08 | ChatGPT Images 2.5 release; API models Flare, Sunburst | 203, 298 | I01 | VERIFIED |
| NR8 | 16 images; each under 50 MB; PNG, WebP or JPG | Images edits endpoint inputs | 209, 299 | I07 | VERIFIED |
| NR9 | edges divisible by 16; edge at most 3,840 px; aspect 1:3 to 3:1; 655,360 to 8,294,400 total px; above 2560x1440 experimental | custom output size, 2.5 models, Images API | 207 | I02 | VERIFIED |
| NR10 | low, medium, high, xhigh, max, auto | quality values, 2.5 models | 207 | I02 | VERIFIED |
| NR11 | image + mask under 50 MB (guide); mask PNG under 4 MB, same size (SDK) | mask limits; the two sources differ | 293, 303 | I02, I09 | VERIFIED |
| NR12 | 2026-04-10 | date of OpenAI Academy image advice | 219 | I04 | VERIFIED |
| NR13 | 5.2 LTS 2026-07-14; 5.2.2 2026-09-15; end of support July 2028 | Blender version dates | 346, 417 | B01 | VERIFIED |
| NR14 | 10 (legacy page) vs 1.0 (signature) | FBX export scale default, two Blender 5.2 sources | 348 | B22, B23 | VERIFIED |
| NR15 | 0.1 / 0.3 / 0.5 ; 0.02 | bevel sample widths in the manual; 0.02 named only as a value NOT to copy everywhere | 354 | B04, P00 | VERIFIED ; OPINION |
| NR16 | at least 2 | bevel segments before profile shape has any effect | 354, 419 | B04 | VERIFIED |
| NR17 | 1.0 / 0.5 | Decimate Collapse ratio examples (keep all / half of triangle-based complexity); not budgets | 358 | B06 | VERIFIED |
| NR18 | (0,0) bottom-left; (1,1) top-right; negative depth = behind camera | world_to_camera_view output | 321 | B21 | VERIFIED |
| NR19 | 4 bones or joints | maximum per vertex, Roblox (register quote for rule 10; the rule line itself gives no number) | 1444 | B31 (R01 points to it) | VERIFIED |
| NR20 | 2,048x2,048 | maximum texture, Marketplace assets, character-body page (register) | 1724 | R05 | VERIFIED |
| NR21 | 4k triangles | maximum, accessories, clothing specifications page (register) | 1732 | R06 | VERIFIED |
| NR22 | 2026-01-30 | 4K textures available in published experiences (devforum post date) | 1708 | R03 | VERIFIED |
| NR23 | under 3.5 GB (low-end Android): 4K textures disabled | texture-streaming platform table; post 2025-12-12, status updated 2026-03-23 | 1716 | R04 | VERIFIED |
| NR24 | 2026-09-17 | Tunable collision (CollisionPrecision slider) post date | 1748 | R08 | VERIFIED |
| NR25 | 2026-04-27 | mesh streaming opt-in phase post date; RenderFidelity ignored on all MeshParts | 1796 | R14 | VERIFIED |
| NR26 | P2-20260801 Preview; "P2.0 launched" (blog index 2026-10-10, covers September 2026) | Tripo P2 API model snapshot vs Studio launch | 1468, 1508 | T02, T07 | VERIFIED |
| NR27 | UNKNOWN | triangle count, loop count, limb ratio (Teemo/Beemo); bevel radius, shoulder clearance, triangle budget (Mei); texel density, module size (Icebox); metallic value (Ravenwood); lean angle, mobile texture budget (Luca); fixed bevel width, segment count, detail-to-rest %, texel density (whole pipeline); silhouette, landmark and color tolerance; iteration count | 65, 75, 85, 111, 121, 131, 173, 331, 340 | P00 | OPINION (evidence-gap) |
| NR28 | 20,000 triangles per mesh ; about 7,000 triangles for creatures and characters | NOT in this paper range. Owner J007-D5: 20,000 is only the upload ceiling; 7,000 is the project budget | - | owner | owner |

## 8. Lessons by role (index of the inline marks)

Row IDs only; read the row for the condition.

| Role | Rows |
| --- | --- |
| [for-rigger] | EV2, RU06, RU07, RU15, CS1-a, CS1-b, CS1-d, CS3-b, CS3-c, CS4-d, CS6-b, CS7-b, CS7-c, SP1, SY2, RF6, RF10, RF14, RF15, RF16, RF18-e, RF18-f, RF25, BK1, BK2, BK5, BK14, HM3, HM4, HM7, HM8, HM12, HM14, HM15, HM16, HM22, HM23, HM24 |
| [for-art-director] | RU01, RU02, RU03, SG1-SG3, SG5, CS1-c, CS1-d, CS2-b, CS3-a, CS3-c, CS4-a, CS4-b, CS5-b, CS5-c, CS6-a, CS6-c, CS7-a, CS7-c, CS8-a, CS8-b, SY1-SY4, SY6-SY10, SP1, SP2, SP5, RF1, RF2, RF6, RF7, RF9-RF11, RF13, RF14, RF18-g, RF18-h, RF20, RF21, RF25, RF26, BK2, BK5, BK11, BK13, BK14 |
| [for-environment] | EV7, RU03, RU10, RU12, RU13, RU14, CS2-a..e, CS4-a, CS4-b, CS5-d, CS8-a..c, CS9-a..c, CS10-a, CS10-b, SY8, RF17, BK1, BK4 |
| [for-vfx] | SG2 (visible source of power) |
| [for-ui] | none found in this range (the ChatGPT reference method may serve icons, but the paper does not say so) |

## 9. What not to do (collected from the paper's own warnings)

| ID | MP | Do not | Tag | Src |
| --- | --- | --- | --- | --- |
| NT1 | 17, 173, 227 | Fill an unknown number (bevel, texel density, tolerance, budget) from internet habit or credit it to a source that never gave it. | OPINION | P00 |
| NT2 | 93, 147, 75, 121 | Move another studio's shader, engine, batching or budget into Roblox as if it applied. | OPINION | P00 |
| NT3 | 103 | Copy one hero's slot limits to every Roblox pet, NPC or tool. | OPINION | P00 |
| NT4 | 157, 275 | Average contradicting views into an unapproved fourth design. | OPINION | P00 |
| NT5 | 213, 295 | Treat a plausible or polished image as a build spec, a dimensioned drawing or a mesh. | OPINION | P00 |
| NT6 | 273 | Let "looks correct" from a vision model override a part inventory or a measured size. | OPINION | P00 |
| NT7 | 327 | Approve on an aggregate image-similarity score alone. | OPINION | P00 |
| NT8 | 335 | Hide a failed silhouette behind a polished surface pass. | OPINION | P00 |
| NT9 | 352 | Weld the whole mesh because the center seam is open; erase approved asymmetry for symmetry. | OPINION | P00 |
| NT10 | 356, 358 | Call a boolean or an automatic remesh "game-ready" without preview and runtime checks. | OPINION | P00 |
| NT11 | 364, 414 | Call Mesh.validate() or repair operators as a plain read-only check on every flag. | VERIFIED (validate edits) ; OPINION | B09, P00 |
| NT12 | 211, 295 | Reuse an old GPT Image 1 recipe on a current model, or paste API limits into the ChatGPT UI. | VERIFIED ; OPINION | I03, P00 |

## 10. Rows other roles need (hand-offs implied by the paper)

| ID | MP | Hand-off | Tag | Src | Roles |
| --- | --- | --- | --- | --- | --- |
| HO1 | 287 | Rigger and animator check the approved reference's rest pose, clearances, and whether a continuous skin or rigid parts are needed before the modeler fixes topology. | OPINION | P00 | [for-rigger] |
| HO2 | 287 | Art director checks visual language and consistency across the set; owner approves the reference and any material design change. | OPINION | P00 | [for-art-director] |
| HO3 | 335 | Blockout package (comparison views, units, named parts, articulation guess, provisional collision, open questions) goes to the art director and rigger for approval before surface work. | OPINION | P00 | [for-art-director] [for-rigger] |
| HO4 | 289 | The approved reference pack (images, prompt, model id, date, settings, sizes, revision, reference roles, approval record) goes to both the hand and the Tripo branch. | OPINION | P00 | - |
| HO5 | 311, 157 | Conflicts that touch movement, silhouette, scale or construction go to the relevant owner; style conflicts go to the art director. | OPINION | P00 | [for-art-director] [for-rigger] |

## 11. Contradictions and gaps (inside lines 1-422, or with the owner budget)

| ID | MP | Item | How to treat it |
| --- | --- | --- | --- |
| G1 | 17, 47 vs owner | The paper never gives 20,000 or about 7,000 triangles in lines 1-422. Owner J007-D5 fixes 20,000 as the upload ceiling and about 7,000 as the creature and character budget. The paper agrees with the principle (rule 14: an upload ceiling is not a phone target; EV9: a project budget must be labeled a project choice and tested). | Cite the owner, not the paper, for 7,000. Label it an owner project budget, to be tested on phones. |
| G2 | 39, 1688-1694 | Rule 10 cites R01 for generic-mesh limits, but the register quote for R01 only says "see B31", and B31's quote gives 4 bones per vertex, not 20,000 triangles. The 20,000 figure is not in any register entry read here. | Fact-check R01 directly (claim 3 in section 12). Do not repeat 20,000 as a paper fact. |
| G3 | 348 | B22 (legacy FBX page) says export scale default 10; B23 (5.2 signature) says global_scale=1.0. The paper flags it. | Follow B23 for the 5.2 default; pin the Blender version; do not call either an art scale. |
| G4 | 293 | Mask limits differ: I02 (guide) vs I09 (SDK). The paper flags it and ran no mask request. | Use the narrower rule; check the live endpoint. |
| G5 | 211 | I03 documents omitting input_fidelity for "GPT Image 2", but the models named in the paper are GPT-Image-2.5 Flare and Sunburst. The paper does not say if the rule covers 2.5. | Check I03 for the 2.5 models before using the parameter either way. |
| G6 | 219, 203 | I04 is dated 2026-04-10, before Images 2.5 (2026-09-08). Its advice may describe an earlier model, yet the paper tags it VERIFIED for current practice. | Treat as general prompting advice; re-check against the 2.5 guide. |
| G7 | 97, 191 | Case 5 says "normal weapon slot ... 512x512 texture"; the table line says "512x512 normal versus 256x256 persona". "Normal" means the regular slot, not a normal map. The paper does not say what the texture type is (color, mask or other). | Read "normal" as "regular slot". Check C06 for what the 512 and 256 sizes apply to. |
| G8 | 161, 196 | The 256 vs 1024 example is credited to C15, but C15's register quote only says budgets differ per hero. The example itself is not shown in the quote. | Fact-check C15 for the 256 / 1024 example. |
| G9 | 190, 87 | The count of nine TF2 classes is credited to C04, but C04's quote does not show it. | Fact-check C04. |
| G10 | 41, 43, 45, 47 | Rules 8, 10-13 (Tripo surface, category limits, texture residency, draw calls, Tunable collision, mesh streaming) are only rule lines in lines 1-422. Their detail, and the old collision-option and fixed-distance claims, are not explained in this range. Only register quotes (R03-R06, R08, R13, R14, T02, T07) back them. | Treat the rules as pointers. Their numbers come from the register rows NR19-NR26. Detail lives in paper lines 423+ (not read). |
| G11 | 9 | The paper says Tripo is for "assets where generation is likely to improve the result" but gives no test for choosing Tripo over hand modeling in lines 1-422. | The lead or owner must set the choice rule. Do not invent one from this note. |
| G12 | 227-247 | The paper has templates for character, creature, prop/vehicle and building only. None is tested (MP:227). No template for icons, UI, textures or VFX. | Use as a starting scaffold; test before trusting. |
| G13 | 205, 207, 209 | The limits in I02 and I07 are API limits. The studio's reference-image route may be the ChatGPT browser UI (see the reference-images skill), where Work mode, templates and Sketch availability differ (I05). | Do not apply API sizes or the 16-image limit to the ChatGPT UI without checking (paper MP:295 says the same). |
| G14 | 346 | The paper's "latest production download" is Blender 5.2.2 on its research date. The version running in the owner's Blender MCP is unknown. | Read bpy.app.version at the start of each job and compare with the manifest. |
| G15 | 366-412 | The pseudocode is unexecuted, and uses to_mesh(preserve_all_data_layers=True, depsgraph=...) and calc_loop_triangles. Argument names and behavior are as the paper wrote them. | Run a Blender probe before building a tool on it. |
| G16 | 53, 99 | C05 (a Dota art guide) is tagged VERIFIED while C01, C04 (design articles) are EXPERIENCE. The paper's logic: living vendor guides and spec pages = VERIFIED; talks, interviews and articles = EXPERIENCE. | Keep the paper's tags; do not upgrade EXPERIENCE rows. |
| G17 | 55, 173, 331 | No numeric tolerance, bevel width, texel density, edge-loop count or silhouette threshold exists in range. They are open for the art director and owner. | List in the job's open questions; never fill from convention. |
| G18 | 15 | I05 says "updated yesterday" with no absolute date. | Date it by the access date only. |
| G19 | 181, 183 | C14 and C16 were read only as a talk description and a page; their detail was not retrieved. | Cite only what the description states. |
| G20 | 27, 350 | Rule 4 (MP:27) is tagged VERIFIED (B03, B09, B10), but "keep an editable source" is OPINION (MP:350). | Read rule 4's VERIFIED tag as covering the Blender behavior only. |

## 12. Claims to fact-check

Format: number. MP line · domain · exact claim (paraphrased, nothing dropped) · paper source id. Tags are in the rows above. Dates and numbers are as the paper gives them.

1. MP:39, 1688-1694 · Roblox · Generic Roblox meshes, avatar bodies and accessories have different constraints; "general specifications" is the base page. · R01
2. MP:1724 · Roblox · Textures for Marketplace assets cannot exceed 2048x2048 on the character-body page. · R05
3. MP:1732 · Roblox · Accessories cannot exceed 4k triangles on the clothing-specifications page. · R06
4. MP:1444 · Roblox · A vertex cannot be influenced by more than 4 bones or joints (general model specifications). · B31 (R01 shares it)
5. MP:41, 1708 · Roblox · 4K textures became available in published experiences (post dated 2026-01-30). · R03
6. MP:41, 1716 · Roblox · Texture streaming (post 2025-12-12, status updated 2026-03-23) disables 4K textures on low-end Android below 3.5 GB. · R04
7. MP:43, 1788 · Roblox · Multiple meshes with the same MeshContent are handled in a single draw call (so an atlas is not universal draw-call elimination). · R13
8. MP:45, 1748 · Roblox · Collision "Tunable" exposes a CollisionPrecision slider (post 2026-09-17), replacing an older four-option model. · R08
9. MP:45, 1796 · Roblox · Under the new mesh streaming opt-in phase (post 2026-04-27), MeshPart.RenderFidelity is ignored across all MeshParts; old fixed-distance assumptions no longer apply. · R14
10. MP:35, 1468, 1508 · Tripo · Tripo P2 has an API model snapshot P2-20260801 labeled Preview, while a blog post (index date 2026-10-10, covering September 2026) says P2.0 was officially launched; Studio availability and API preview status differ. · T02, T07
11. MP:203 · ChatGPT image · ChatGPT Images 2.5 was released 2026-09-08 with API models GPT-Image-2.5 Flare (faster) and Sunburst (more demanding precision, longer generation). · I01
12. MP:203 · ChatGPT image · Reference-fidelity and repeated-edit gains are vendor-reported. · I01
13. MP:205 · ChatGPT image · ChatGPT supports prompt generation, image upload for edit and region selection; the Help Center warns edits can extend beyond the selection. · I05
14. MP:205 · ChatGPT image · The ChatGPT UI describes arbitrary aspect-ratio requests; templates are unavailable in Work mode; Sketch is described on mobile. · I05
15. MP:207 · ChatGPT image · Images API selects the image model directly; Responses uses a supported mainline model with the image model inside the image-generation tool. · I02
16. MP:207 · ChatGPT image · 2.5 models support quality low, medium, high, xhigh, max and auto. · I02
17. MP:207 · ChatGPT image · Custom sizes: edges divisible by 16, no edge above 3,840 px, aspect ratio 1:3 to 3:1, total pixels 655,360 to 8,294,400; outputs above 2560x1440 are experimental. · I02
18. MP:207 · ChatGPT image · The guide acknowledges failures of recurring-character consistency and exact structured composition. · I02
19. MP:209 · ChatGPT image · The Images edits endpoint accepts up to 16 images, each PNG, WebP or JPG under 50 MB, and lists 2026-09-08 snapshots of both 2.5 models. · I07
20. MP:211 · ChatGPT image · OpenAI advises comparing candidates with identical prompt, references, size and output format, and testing full edit sequences. · I03
21. MP:211 · ChatGPT image · Equal quality labels do not mean equal image quality or response time across models. · I03
22. MP:211 · ChatGPT image · For transparent output the actual alpha channel must be inspected. · I03
23. MP:211 · ChatGPT image · The guide documents omitting input_fidelity for GPT Image 2, where older-model advice used it. · I03
24. MP:219 · ChatGPT image · OpenAI advises clear subject, style, framing and lighting constraints; explicit roles for uploaded references; targeted revisions that restate what stays unchanged (page dated 2026-04-10). · I04
25. MP:273 · ChatGPT image · OpenAI documents approximate counting, unreliable precise spatial localization and possible image resizing in vision analysis. · I06
26. MP:293 · ChatGPT image · The generation guide describes image and mask files as matching format and size and under 50 MB. · I02
27. MP:293, 303 · ChatGPT image · The Python SDK mask field requires a PNG under 4 MB with matching dimensions. · I09
28. MP:283 · other · Seesaw Man (Santiago Vivanco Morillo) documents ChatGPT image iteration, Hunyuan 3D conversion, Blender retopology and cleanup, and texture refinement. · I08
29. MP:346, 417 · Blender · Blender 5.2 LTS initial release 2026-07-14; 5.2.2 released 2026-09-15 and is the latest production download; 5.2 support ends July 2028. · B01
30. MP:348 · Blender · The current FBX manual describes a new importer and directs export to the FBX add-on. · B30
31. MP:348 · Blender · The page titled FBX (Legacy) contains importer and exporter material. · B22
32. MP:348 · Blender · The legacy page states export Scale defaults to 10. · B22
33. MP:348 · Blender · The 5.2 Python export operator signature shows global_scale=1.0. · B23
34. MP:350 · Blender · Modifiers are evaluated top to bottom and keep the base mesh until applied; order changes the result. · B03
35. MP:352 · Blender · Mirror works on object-local axes or a mirror object; clipping holds edit-mode vertices at the plane; merging depends on merge distance; vertex-group mirroring has naming and pre-existing-empty-group conditions (page dated 2026-08-07). · B08
36. MP:354 · Blender · Bevel width can mean offset, width, depth, percent or absolute distance; Segments is the count of added loops; profile shape has no effect below 2 segments. · B04
37. MP:354 · Blender · The Bevel manual's sample widths are 0.1, 0.3 and 0.5. · B04
38. MP:356 · Blender · Boolean: only manifold inputs are guaranteed proper results; Float lacks overlap support; Exact handles overlap at higher cost; Manifold needs manifold inputs except the plane-difference case. · B05
39. MP:358 · Blender · Decimate Collapse ratio is computed on triangles; ratio 1.0 preserves the mesh; 0.5 targets half of the triangle-based complexity. · B06
40. MP:358 · Blender · Voxel remesh regenerates a uniform outer surface, ignores modifiers and shape keys, and is not recommended for deformation topology; automatic remeshing generally does not give deformation-friendly topology. · B07
41. MP:360 · Blender · Baking transfers base color and normal information to texture targets; it needs UVs and an active image node or color attribute; Selected-to-Active casts from the active low-poly toward high detail; a cage or ray distance controls projection; tangent-space normals can accommodate deformation; margins protect UV seams under filtering and mipmaps. · B12
42. MP:364 · Blender · Mesh data has vertices, edges, loops, polygons, UVs and color attributes; UVs are corner-associated; Mesh.validate() repairs or removes invalid geometry and returns whether it changed data; from_pydata does not prevent all invalid input. · B09
43. MP:364 · Blender · Base and evaluated meshes differ; evaluated dependency-graph objects must be used to measure modifiers; a temporary to_mesh() result belongs to its object and must be cleared. · B10
44. MP:364 · Blender · preserve_all_data_layers=True with the dependency graph gives a full UV and attribute inventory; the default computes only a viewport or render subset. · B32
45. MP:364 · Blender · BMesh offers manifold, boundary, wire and connectivity inspection. · B11
46. MP:321 · Blender · Blender describes mesh modeling as primitive blockout followed by detail. · B02
47. MP:321 · Blender · Orthographic projection keeps parallel lines parallel, with no distance shrink. · B15
48. MP:321 · Blender · world_to_camera_view maps to normalized camera-frame coordinates, (0,0) bottom-left, (1,1) top-right, negative depth behind the camera. · B21
49. MP:53 · other · Riot says silhouette matters most for champion recognition; names facing direction and visible source of power; High Noon Senna keeps her signature weapon (2021-03-12). · C01
50. MP:53, 99 · other · Dota art guide: silhouette identifiable at first glance; outline, facing direction, upper-body focus, value regions, rest areas; deviation from dark-below, light-above gradient allowed when legible. · C05
51. MP:61, 63 · other · Riot Teemo/Beemo: facial and limb geometry added for expression; reusable base mesh; Beemo's old onesie face built for a head-down, forward-facing rig; splash art usually follows the 3D model; an existing splash can inform an update (2024-09-23). · C12
52. MP:67 · other · Jenna VanPelt's portfolio credits the Beemo model and collaborators. · C17
53. MP:71 · other · VALORANT Icebox: greybox, art blockout, art production; architecture follows exported greybox edges; shapes before UVs and textures; tiling textures and trim sheets for large structures; custom textures for special props; much decorative detail above player height (2020-11-16). · C02
54. MP:79, 83 · other · Blizzard Mei Honeydew and Bubbledew Blaster keep silhouette and weapon mechanics; Sniper Ana coat silhouette and camouflage clipping; rejected Talon shield concept (2020). · C03
55. MP:89 · other · TF2 (2007 paper): class silhouettes differ by proportions, weapons, footwear, hats and clothing shapes; folds support the silhouette; repeated structure conveyed without modeling every repeat; nine classes. · C04
56. MP:97 · other · Axe (Dota 2): regular weapon slot LOD0 2,500 and LOD1 1,000 triangles with a 512x512 texture; persona weapon same triangles with a 256x256 texture. · C06
57. MP:107 · other · Splatana Stamper comes from a staff date stamp; Stringer from a fishing rod; Stringer meant to avoid looking like a firearm; fictional manufacturers explain the objects (2022-09-07). · C07
58. MP:115, 117 · other · Ravenwood: Kraken-ink iridescent material reused as a start; grayscale metallic map gave a better value range than fully metallic or nonmetallic extremes; mask following every face shape failed aesthetically (2023-03-03). · C08
59. MP:125 · other · Luca: round organic underwater shapes vs rectilinear town; lean, sag and twist principles; characters get the widest value range; signs and environments restrained; distinctive front curl on Luca's hair (2021). · C09
60. MP:135 · other · Epic Village sample: structures reduced roughly 50% for isometric view; cliffs at 50% scale; -59 degree interior camera with front walls removed; props make gaps truly traversable (2023-12-18). · C10
61. MP:143 · other · Sable (Shedworks): low-poly handcrafted look, color drives mood, interchangeable parts, procedural terrain generated before runtime; nearly 80% of environments with ProBuilder, per Fineberg's estimate (2022-07-12). · C11
62. MP:161, 196 · other · Dota shader doc: each hero has different item texture budgets; example 256x256 in game vs 1024x1024 source. · C15
63. MP:179 · other · Disney's modeler-role page links Visual Development Artists, modelers and Character TDs. · C13
64. MP:181 · other · Supercell Games First 2024 description (upload 2024-11-13): creative cohesion, humor, nostalgia, 1980s influences for Brawl Stars characters. · C14
65. MP:181 · other · Supercell Make (2019-11-11) lets users download game character assets. · C18
66. MP:183 · other · Disney's SIGGRAPH 2022 page: Encanto's Isabela room involved procedural-modeling challenges. · C16

## 13. Check results (C1-C3)

| Check | Result |
| --- | --- |
| C1 every heading in lines 1-422 has a section | done, see section 0 |
| C2 every row has MP line + tag + source id | done (UNKNOWN rows show the paper's OPINION tag; rows with Src `owner` or `-` are the owner budget, row NR28) |
| C3 no sentence over 12 words copied verbatim | done by paraphrase; only source-table quotes are verbatim, 12 words or fewer |

## 14. Source table (ids used by the rows above)

Quotes are short locators (12 words or fewer). Evidence tag and date are the paper's own register values.

| ID | Source | Date | Tag | Key quote | URL |
| --- | --- | --- | --- | --- | --- |
| P00 | Proposed studio method (the paper's own synthesis) | 2026-10-21 | OPINION | none (not an external source) | none |
| C01 | Clarity in League (Riot) | 2021-03-12 | EXPERIENCE | "Silhouettes are the single most important thing for champion recognition" | https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ |
| C02 | The Art of VALORANT Map Environments | 2020-11-16 | EXPERIENCE | "tiling textures and trim sheets on our buildings" | https://playvalorant.com/en-us/news/dev/the-art-of-valorant-map-environments/ |
| C03 | What it's like to work on Overwatch as a concept artist (Blizzard) | 2020 (day not shown) | EXPERIENCE | "shouldn't radically change the silhouette of a character" | https://news.blizzard.com/en-us/article/23537427/what-its-like-to-work-on-overwatch-as-a-concept-artist |
| C04 | Illustrative Rendering in Team Fortress 2 (Valve) | 2007 | EXPERIENCE | "High frequency detail is omitted where possible" | https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf |
| C05 | Dota 2 Workshop, Character Art Guide | undated; acc 2026-10-21 | VERIFIED | "silhouette must be clearly identifiable at first glance" | https://help.steampowered.com/en/faqs/view/0688-7692-4D5A-1935 |
| C06 | Dota 2 Workshop, Technical Requirements, Axe | undated; acc 2026-10-21 | VERIFIED | "LoD0 Triangle Limit: 2500" | https://www.dota2.com/workshop/requirements/axe?l=english |
| C07 | Ask the Developer Vol. 7, Splatoon 3 Part 2 | 2022-09-07 | EXPERIENCE | "inspired by a date stamp" | https://www.nintendo.com/us/whatsnew/ask-the-developer-vol-7-splatoon-3-part-2/ |
| C08 | From Concept to Cosmetic, Ravenwood Set (Sea of Thieves) | 2023-03-03 | EXPERIENCE | "maintaining good colour was vital here" | https://www.seaofthieves.com/news/fctc-ravenwood-set |
| C09 | Luca official production notes (press kit) | 2021 (file revision 2021-06-04) | EXPERIENCE | "principles of lean, sag and twist" | https://lumiere-a.akamaihd.net/v1/documents/luca_press_kit_final_06-04-21_9b5cc33b.pdf |
| C10 | Learn how the Village sample island was built (Epic) | 2023-12-18 | EXPERIENCE | "reduce the size of all the structures by roughly 50%" | https://www.fortnite.com/news/learn-how-the-village-sample-island-was-built |
| C11 | How a modular design approach crafted Sable (Shedworks) | 2022-07-12 | EXPERIENCE | "using colors to create the moods" | https://unity.com/resources/shedworks-sable-modular-design-approach |
| C12 | [Dev] Scouting out Teemo (Riot) | 2024-09-23 | EXPERIENCE | "splash art is created after the 3D model" | https://www.leagueoflegends.com/en-us/news/dev/dev-scouting-out-teemo/ |
| C13 | Modeling, Disney Animation production team | undated; acc 2026-10-21 | VERIFIED | "Modelers bring concepts into dimensionality" | https://www.disneyanimation.com/team/modeler/ |
| C14 | Fernanda Oliveira, Games First 2024, Creating Characters for Brawl Stars | 2024-11-13 upload | EXPERIENCE | "keep the game's universe cohesive" | https://www.youtube.com/watch?v=KUgUTVy-l2I |
| C15 | Dota 2 Workshop, Item Shader Masks | undated; acc 2026-10-21 | VERIFIED | "different texture budgets for their items" | https://help.steampowered.com/en/faqs/view/299C-D7F9-09A5-98B6 |
| C16 | Modeling Animated Jumbo Floral Display on Disney's Encanto | SIGGRAPH 2022 | VERIFIED | "artistic technical solutions" | https://disneyanimation.com/publications/modeling-animated-jumbo-floral-display-on-disney-s-encanto/ |
| C17 | Beemo ASU, Jenna VanPelt (portfolio) | undated; 2024 ASU; acc 2026-10-21 | EXPERIENCE | "I created the new Beemo model" | https://jinyao.artstation.com/projects/AZyJqq |
| C18 | Supercell Launches Content Creation Platform Supercell Make | 2019-11-11 | VERIFIED | "users can download game character assets" | https://supercell.com/en/news/supercell-launches-make/ |
| I01 | Introducing ChatGPT Images 2.5 (OpenAI) | 2026-09-08 | VERIFIED | "two new models in the API" | https://openai.com/index/introducing-chatgpt-images-2-5/ |
| I02 | Image generation guide (OpenAI) | undated; acc 2026-10-21 | VERIFIED | "struggle to maintain visual consistency" | https://developers.openai.com/api/docs/guides/image-generation |
| I03 | Image prompting guide (OpenAI) | undated; acc 2026-10-21 | VERIFIED | "same quality label does not imply the same image quality" | https://developers.openai.com/api/docs/guides/image-prompting |
| I04 | Creating images with ChatGPT (OpenAI Academy) | 2026-04-10 | VERIFIED | "Refer to each image by order" | https://openai.com/academy/image-generation/ |
| I05 | Images in ChatGPT (OpenAI Help) | live page "updated yesterday" on acc 2026-10-21; no absolute date | VERIFIED | "edits may extend beyond the area you selected" | https://help.openai.com/en/articles/11084440-images-in-chatgpt |
| I06 | Images and vision guide (OpenAI) | undated; acc 2026-10-21 | VERIFIED | "approximate counts for objects in images" | https://developers.openai.com/api/docs/guides/images-vision |
| I07 | Create image edit API reference (OpenAI) | undated; acc 2026-10-21 | VERIFIED | "You can provide up to 16 images." | https://developers.openai.com/api/reference/ruby/resources/images/methods/edit |
| I08 | Seesaw Man, AI to 3D Character Development Pipeline WIP (S. Vivanco Morillo) | undated; acc 2026-10-21 | EXPERIENCE | "Retopology and cleanup in Blender" | https://santiagovivanco.artstation.com/projects/BkDO2l |
| I09 | OpenAI Python SDK images resource | undated main-branch snapshot; acc 2026-10-21 | VERIFIED | "Must be a valid PNG file, less than 4MB" | https://github.com/openai/openai-python/blob/main/src/openai/resources/images.py |
| B01 | Blender 5.2 LTS release | 2026-07-14; patch 5.2.2 2026-09-15 | VERIFIED | "Initial release: July 14, 2026" | https://www.blender.org/releases/5-2/ |
| B02 | Blender mesh modeling introduction | undated; acc 2026-10-21 | VERIFIED | "blocking out the shape using primitives" | https://docs.blender.org/manual/en/latest/modeling/meshes/introduction.html |
| B03 | Modifier stack introduction | undated; acc 2026-10-21 | VERIFIED | "calculated from top to bottom in the stack" | https://docs.blender.org/manual/en/5.2/modeling/modifiers/introduction.html |
| B04 | Bevel modifier | undated; acc 2026-10-21 | VERIFIED | "edge loops added along the bevel's face" | https://docs.blender.org/manual/id/5.2/modeling/modifiers/generate/bevel.html |
| B05 | Boolean modifier | undated; acc 2026-10-21 | VERIFIED | "Only Manifold meshes are guaranteed to give proper results." | https://docs.blender.org/manual/en/5.2/modeling/modifiers/generate/booleans.html |
| B06 | Decimate modifier | undated; acc 2026-10-21 | VERIFIED | "triangles are used when calculating the ratio" | https://docs.blender.org/manual/en/5.2/modeling/modifiers/generate/decimate.html |
| B07 | Remeshing and retopology | undated; acc 2026-10-21 | VERIFIED | "don't result in topology that lends itself to deformation" | https://docs.blender.org/manual/id/5.2/modeling/meshes/retopology.html |
| B08 | Mirror modifier | 2026-08-07 | VERIFIED | "Prevents vertices from moving through the mirror plane(s)" | https://docs.blender.org/manual/ko/5.2/modeling/modifiers/generate/mirror.html |
| B09 | Mesh Python API | undated; acc 2026-10-21 | VERIFIED | "return True when the mesh has had invalid geometry corrected/removed" | https://docs.blender.org/api/5.2/bpy.types.Mesh.html |
| B10 | Dependency graph Python API | undated; acc 2026-10-21 | VERIFIED | "all modifiers are taken into account" | https://docs.blender.org/api/5.2/bpy.types.Depsgraph.html |
| B11 | BMesh types Python API | undated; acc 2026-10-21 | VERIFIED | "True when this edge is manifold (read-only)." | https://docs.blender.org/api/5.2/bmesh.types.html |
| B12 | Render baking | undated; acc 2026-10-21 | VERIFIED | "Bake shading on the surface of selected objects" | https://docs.blender.org/manual/ka/5.2/render/cycles/baking.html |
| B13 | Separate mesh | undated; acc 2026-10-21 | VERIFIED | "an object for every independent (disconnected) piece" | https://docs.blender.org/manual/sr/5.2/modeling/meshes/editing/mesh/separate.html |
| B15 | Camera projection | undated; acc 2026-10-21 | VERIFIED | "parallel lines appear parallel" | https://docs.blender.org/manual/id/5.2/render/cameras.html |
| B21 | Camera projection Python utility | undated; acc 2026-10-21 | VERIFIED | "A negative 'z' value means the point is behind the camera." | https://docs.blender.org/api/5.2/bpy_extras.object_utils.html |
| B22 | FBX legacy manual | undated; acc 2026-10-21 | VERIFIED | "10 is the default because this fits best" | https://docs.blender.org/manual/en/5.2/files/import_export/fbx_legacy.html |
| B23 | FBX export Python API | undated; acc 2026-10-21 | VERIFIED | "global_scale=1.0" | https://docs.blender.org/api/5.2/bpy.ops.export_scene.html |
| B30 | Current FBX importer manual | undated; acc 2026-10-21 | VERIFIED | "To export FBX files use the FBX Add-on." | https://docs.blender.org/manual/en/latest/files/import_export/fbx.html |
| B31 | Roblox general model specifications | undated; acc 2026-10-21 | VERIFIED | "can not be influenced by more than 4 bones or joints" | https://create.roblox.com/docs/art/modeling/specifications |
| B32 | Object data and temporary mesh Python API | undated; acc 2026-10-21 | VERIFIED | "Preserve all data layers in the mesh" | https://docs.blender.org/api/current/bpy.types.Object.html?highlight=ray |
| T02 | Tripo P2 model card | undated; snapshot P2-20260801; acc 2026-10-21 | VERIFIED | "P2-20260801 Preview" | https://developers.tripo3d.ai/en/models/p2 |
| T07 | Tripo September update | 2026-10-10 per blog index; covers September 2026 | VERIFIED | "We officially launched P2.0" | https://www.tripo3d.ai/blog/tripo-september-update |
| R01 | Roblox General specifications | undated; acc 2026-10-21 | VERIFIED | register says "see B31 for the shared source excerpt" | https://create.roblox.com/docs/art/modeling/specifications |
| R03 | Roblox 4k Texture Rendering (DevForum) | 2026-01-30 | VERIFIED | "4k Textures are now available in published experiences!" | https://devforum.roblox.com/t/4k-texture-rendering/4316229 |
| R04 | Introducing Texture Streaming (DevForum) | 2025-12-12; platform status updated 2026-03-23 | VERIFIED | "Low-end Android [< 3.5GB] [4k textures disabled]" | https://devforum.roblox.com/t/introducing-texture-streaming/4144855 |
| R05 | Roblox Character body specifications | undated; acc 2026-10-21 | VERIFIED | "Textures for Marketplace assets can't exceed 2048x2048 resolution." | https://create.roblox.com/docs/avatar/character-bodies/specifications |
| R06 | Roblox Clothing specifications | undated; acc 2026-10-21 | VERIFIED | "Accessories can't exceed 4k triangles." | https://create.roblox.com/docs/art/accessories/clothing-specifications |
| R08 | Collision Geometry Workflow Improvements: Tunable Precision (DevForum) | 2026-09-17 | VERIFIED | "Tunable exposes a CollisionPrecision slider" | https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198 |
| R13 | Roblox Improve performance | undated; acc 2026-10-21 | VERIFIED | "handled in a single draw call" | https://create.roblox.com/docs/performance-optimization/improve |
| R14 | Introducing Mesh Streaming and Improved Cloud LoDs, Opt-in Phase (DevForum) | 2026-04-27 | VERIFIED | "RenderFidelity property across all your MeshPart instances will be ignored" | https://devforum.roblox.com/t/introducing-mesh-streaming-and-improved-cloud-lods-in-published-experiences-opt-in-phase/4601232 |
