---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J005-T01, Roblox_Character_Rigger_Research.txt lines 1-264
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Rigging paper part 1: evidence rules, rig quality, Roblox runtime, planning, merged AI mesh (lines 1-264)

Paraphrased notes. The paper (RP) stays outside git. Every row cites `RP:<line>`. Nothing here is fact-checked yet: claims are the paper's, listed in section 11 for the fact-check pass. The paper's cutoff is 2026-10-20.

## 0. How to read

| Key | Meaning |
| --- | --- |
| RP:n | line n of `Roblox_Character_Rigger_Research.txt`. One paragraph = one line. Source list = RP:597-845. |
| Tag | VERIFIED (a primary source states it; for vendors only what the vendor documents, not output quality), EXPERIENCE (a named practitioner reports it), OPINION (the paper's proposal), OPINION-unresolved (paper says unknown; never turn into a fact). Tags are the paper's, not mine. |
| Src | paper source ID (resolved in section 13). "undated, chk 2026-10-20" = source shows no date, paper checked it on 2026-10-20. |
| Stage | workflow stage the lesson serves (note: paper source IDs S1-S3 appear only in Src columns, workflow stages S0-S8 only in Stage columns) (`knowledge/jobs/J005-character-rigger/workflow.md`): S0 intake, S1 animator motion needs, S2 rig plan, S3 modeler geometry, S4 geometry acceptance (rigger), S5 rig + tests, S6 animator rig acceptance, S7 animate, S8 owner G3. |
| [for-animator] / [for-modeler] | the animator or modeler must also know or act on it. |
| Row IDs | EC evidence contract, RU rule, then lesson IDs by paper section (1.1-a ... 4e-h), RS sheet field, DT decision-table row, N number, T Tripo op, C claim, X contradiction/limit. |

## 1. Evidence contract and governing principle (RP:6-12)

| ID | RP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| EC1 | 8 | VERIFIED = the named primary source directly backs the statement. When the claim is about a vendor tool, it shows only what the vendor publishes, not how good any result is. | contract | - | all |
| EC2 | 8 | EXPERIENCE = a named practitioner reports a result. Not a population estimate, and not the paper's own hands-on work. | contract | - | all |
| EC3 | 8 | OPINION = a proposed studio policy, inference, diagnostic, design or pass criterion. A source listed beside it is the motivation, not the proof. | contract | - | all |
| EC4 | 8 | UNKNOWN is not an extra grade. It is written OPINION-unresolved, and an agent must never promote it to a fact. | contract | - | all |
| EC5 | 10, 599 | A claim carries the date and limits of its source. Live pages with no date were read on the cutoff date. Page copyright years and crawl dates do not count as publication dates. | contract | - | all |
| EC6 | 10, 599 | Key quotations live only in the source list, each under 20 words. | contract | - | - |
| EC7 | 10 | Numbers the paper made up are never presented as facts. Project budgets and tolerances stay open fields, filled by measuring. Arithmetic identities, schema counts, frame indices and step numbers are not performance claims. | contract | - | S2, S5 |
| EC8 | 12 | Governing principle: pick the simplest articulation that exports and passes in-engine tests while holding the intended silhouette and contacts over the whole approved motion range. Extra controls are justified only when they make that easier to animate. Output from a generator, auto-segmentation, auto-weights, or a clean import is a candidate to test, never proof of acceptance. | OPINION | - | S2, S4, S5, S6 |

## 2. The fifteen rules (RP:16-30)

| Rule | RP | Rule in my words | Tag | Src | Stage | Who also | Detail rows |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 16 | Settle needed poses, contacts, removable parts and the runtime rig type first; only then finalize topology and weights. | OPINION | S1, R2 | S1, S2 | [for-animator] [for-modeler] | PL-a..PL-g |
| 02 | 17 | General Roblox meshes: 20,000 triangles per individual mesh at most. Marketplace body budgets are separate. | VERIFIED | R1, R2 | S2, S3 | [for-modeler] | N01, N05-N08 |
| 03 | 18 | At most 4 bone or joint influences per vertex. The documented Root carries no weights. | VERIFIED | R1 | S5 | | N02, C03 |
| 04 | 19 | Current avatar bodies use 15 named mesh objects. Advanced R15 allows up to 37 optional extra joints. | VERIFIED | R2 | S2 | | N03, N04, RT2.2-a |
| 05 | 20 | Rigid pieces for deliberate mechanical breaks, skinning for continuously bending surfaces, a mix for armor over flesh. | OPINION | - | S2 | [for-modeler] | DT01-DT12 |
| 06 | 21 | A merged object may not be one connected surface. Check connectivity before cutting or remeshing. | OPINION | B8 | S2 | [for-modeler] | 4a-a, 4a-d |
| 07 | 22 | Conceal rigid-piece cuts with approved overlaps, sockets, collars or intentional gaps, and test over the full motion range. | OPINION | - | S2, S3, S4 | [for-modeler] [for-animator] | 4a-g..4a-m |
| 08 | 23 | Fix topology and joint placement first. Do not try to cure structural faults with smoother weights. | OPINION | D1, R6 | S2, S3, S5 | [for-modeler] | 4b-a, 4b-b |
| 09 | 24 | Audit every vertex after weight cleanup. Normalizing and pruning influences are two separate operations. | OPINION | B2, R1 | S5 | | 4b-d |
| 10 | 25 | Tripo segmentation and Tripo rigging are different operations. Smart Segmentation also includes modeling. | VERIFIED | T1, T2, T4 | S2, S3 | [for-modeler] | T01-T05 |
| 11 | 26 | Ask for Tripo rig model v3.0-20260909 by name for the documented humanoid upgrade. It is not the API default. | VERIFIED | T1, T5 | S2, S5 | | N18-N20, X07 |
| 12 | 27 | Accept an automatic rig only once it has passed tests for joints, weights, topology, names and a Roblox round trip. | OPINION | T3, E1 | S5, S6 | | 4d-j |
| 13 | 28 | Evaluated constraint motion can be baked in Blender; the legacy FBX exporter drops the constraints themselves. | VERIFIED | B5 | S5, S7 | [for-animator] | C25 |
| 14 | 29 | Roblox bone animation changes the rendered geometry, not the physical collision shape. | VERIFIED | R7 | S2, S5 | [for-animator] | RT2.1-a |
| 15 | 30 | Hand off together: source model, export skeleton, control manifest, requirements sheet, clips, recorded Studio test results. | OPINION | - | S5, S6, S7 | [for-animator] | PL-h |

## 3. Section 1: what makes a great game rig (RP:32-67)

### 3.1 Subsection 1.1: observable qualities (RP:34-38)

| ID | RP | Lesson | Tag | Src | Stage | Who also |
| --- | --- | --- | --- | --- | --- | --- |
| 1.1-a | 36 | Check deformation while the rig moves, not in the bind pose. Targets: shoulders stay readable in volume, elbows do not cave in, hips allow walking and crouching, a neck turn leaves the chest alone, hard gear holds its form. | OPINION | - | S4, S5, S6 | [for-animator] |
| 1.1-b | 36 | Judge how predictable the controls are by six things: reset, local axes, selection, IK/FK hand-over, space switching, and whether contacts hold. | OPINION | - | S5, S6 | [for-animator] |
| 1.1-c | 36 | Judge speed by two things: can the animator hit each needed pose without fighting the rig, and does playback plus any scripted evaluation stay inside the budget measured for the project. | OPINION | - | S6, S7 | [for-animator] |
| 1.1-d | 36 | Do not substitute the number of controls, or how elaborate a well-known studio's skeleton is, for those results. | OPINION | - | S2, S5 | |
| 1.1-e | 38 | Joint layout follows the movement idea. A toy shoulder can be an exposed ball joint. A natural shoulder moves arm, clavicle and torso together. An eerie puppet may break normal anatomy on purpose. | OPINION | - | S1, S2 | [for-animator] |
| 1.1-f | 38 | Derive joint positions from body landmarks and the planned rotations, then confirm with mesh cross-sections and silhouette views. A head joint dropped at the middle of its bounding box is a shortcut to avoid. | OPINION | - | S2, S4 | [for-modeler] |

### 3.2 Subsection 1.2: studio evidence and transfer (RP:40-60)

| ID | RP | Studio and what the paper says | Transfer lesson for Roblox | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| 1.2-a | 42 | Riot, Fiddlesticks (published 2020-01-14): an animator asked for a head shake, built as a jiggle chain, with an extra arm-follow arrangement. The rig served natural and deliberately unnatural motion. Example of animation intent changing rig features. | - | VERIFIED | S1 | S1 [for-animator] |
| 1.2-b | 44 | - | Prototype the requested motion on the smallest possible chain and add only the controls needed to author it. Where secondary motion must look identical everywhere, bake it onto joints Roblox can export. Where it must run live, describe the Roblox-side implementation and its owner as a separate item. A Maya jiggle tool or Blender driver does not run in Roblox by itself. | OPINION | S1 | S1, S2, S5 [for-animator] |
| 1.2-c | 46 | Blizzard, GDC 2017 session (day not established): talk on the adaptable animation pipeline behind the 23 Overwatch heroes of that time (hero rigs, first-person animation). The public abstract shows scope only, not bone budgets, control design or deformation methods. | - | VERIFIED | S2 | - |
| 1.2-d | 48 | - | Keep control meaning consistent from character to character, with extra modules per body type. Author and test first-person weapon contacts through the actual first-person camera, not only world views. This is the paper's advice, not a statement about Blizzard's internal rig. | OPINION | - | S2, S6 [for-animator] |
| 1.2-e | 50 | Disney, Frozen production paper (SIGGRAPH 2013): dual-quaternion skinning avoids candy-wrapper twist but needs production extensions, not a universal drop-in for linear blending (LBS). Disney Research (2016) separately documents collapsing elbows, twist artifacts and joint bulging, and proposes optimized centers of rotation. | - | VERIFIED | D1, D2 | S4, S5 |
| 1.2-f | 52 | - | Think about which deformation algorithm is running, not just the weight colors. If a Blender rig depends on a volume-preserving mode, it is not accepted until the target renderer shows the same result. In Roblox, get the shape from topology, weights and exportable helper joints; Disney's solver cannot be assumed there. | OPINION | - | S2, S5 |
| 1.2-g | 54 | Pixar: the 2020 paper (indexed excerpt) lists pose-space sculpting among its corrective-rigging steps; the 2024 Inside Out 2 paper (indexed excerpt) covers special shaping and mouth-rig requirements. Only the excerpts were read; the original URLs redirect. | - | VERIFIED | P1, P2 | - |
| 1.2-h | 56 | - | Hold approved target shapes for the hard poses and compare the Roblox-compatible rig against them; the lesson is to correct toward a known shape. It does not follow that Pixar deformers or Blender shape-key drivers survive import into Roblox. | OPINION | P1, P2 | S4, S5, S6 [for-animator] |
| 1.2-i | 58 | Valve legacy Dota 2 NPC guide: separates named effect attachments from bone-related hitboxes; states a 52-bone limit for that workflow. Riot skeletal-compression article (2015-07-25): transform error piles up along descendant chains and can show as foot sliding. | - | VERIFIED | V1, S3 | S2, S5 |
| 1.2-j | 60 | - | Write sockets and contact tests into the rig contract, and after export measure the drift at the hands, feet, weapon ends and tail ends. The 52 belongs to an old Dota workflow, not Roblox. No current Deadlock rig budget is known. Do not attribute undocumented methods to Naughty Dog, Insomniac, Epic or Supercell because their animation is admired. | OPINION | V1, S3 | S2, S5, S6 [for-animator] |

Paper table (RP:62-67): rule / number / mark / source.

| RP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- |
| 64 | Build rig features from performance requests | no universal control count | VERIFIED example; OPINION transfer | S1, 2020-01-14 |
| 65 | Separate pipeline scope from implementation evidence | 23 heroes (session abstract) | VERIFIED | S2, GDC 2017 |
| 66 | Inspect end effectors after export | no universal error tolerance | VERIFIED mechanism; OPINION test | S3, 2015-07-25 |
| 67 | Do not copy another engine's budget | 52, legacy Dota NPC guide only | VERIFIED | V1, undated, chk 2026-10-20 |

## 4. Section 2: Roblox rigid, skinned and mixed rigs (RP:69-107)

### 4.1 Subsection 2.1: runtime representations (RP:71-81)

| ID | RP | Lesson | Tag | Src | Stage | Who also |
| --- | --- | --- | --- | --- | --- | --- |
| RT2.1-a | 73 | Motor6D joins two BaseParts so they can be animated. Bones take part in skeletal deformation, and skinning assignments live in MeshPart asset data. Bone motion changes only how the mesh looks, never its physical collision shape. | VERIFIED | R7, R8 | S2, S5 | [for-animator] |
| RT2.1-b | 75 | Rigid articulated rig = separate MeshParts joined by a deliberate joint tree (usually Motor6D). Fits blocky characters, robots, doors, weapon mechanisms. Each piece keeps its shape. Cost: object and assembly management, every boundary is visible. Set joint frames explicitly: a Blender object origin alone is not a full Motor6D setup. | OPINION | - | S2, S5 | [for-modeler] |
| RT2.1-c | 77 | Skinned rig = a surface that looks connected deforms through a bone hierarchy and vertex weights. Fits fur bodies, fleshy necks, tails, membrane wings, cloth-like props, organic characters. A skinned asset may hold separate surface islands with deliberate weights. Object count, connectivity and deformation method are three separate choices. | OPINION | - | S2 | [for-modeler] |
| RT2.1-d | 79 | Mixed rig = soft body carrying hard parts (armor, eyes, weapons, removable pieces). A hard part is either its own MeshPart joined at runtime, or geometry bound at weight 1 to a single export bone. Choose the MeshPart when physics, detaching, damage or separate ownership is needed; choose the single-bone bind when only the look must move. Record how sockets track the animated bones. | OPINION | - | S2, S5 | |
| RT2.1-e | 81 | AnimationController is the container for animating non-player objects. Its direct LoadAnimation is deprecated. Use an Animator under the controller; do not copy the deprecated call from old examples. | VERIFIED | R9 | S5, S7 | [for-animator] |

### 4.2 Subsection 2.2: R15 as a compatibility contract (RP:83-89)

| ID | RP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| RT2.2-a | 85 | R15 needs named body objects in a specific hierarchy. Advanced articulation adds optional joints with prescribed names and parents. HumanoidRigDescription and DigitsRigDescription hold advanced body and hand metadata. Counts and budgets are in section 2.3. | VERIFIED | R2, R12 | S2 |
| RT2.2-b | 87 | Sort the asset into one class before rigging: platform avatar body, custom playable character, custom NPC or pet, or prop. Renaming the bones of a custom quadruped does not make it R15. A humanoid with Mixamo or Tripo bone names can be a custom rig but fails avatar publishing rules. Copy the official template hierarchy whole instead of guessing which root nodes to remove. | OPINION | - | S0, S2 |
| RT2.2-c | 89 | Standard avatars: Roblox's current templates and validator decide the schema. Custom rigs: the studio writes its own schema and animation map. Treat Blender's Root and HumanoidRootNode as different things from the runtime HumanoidRootPart and the named animation joints. | OPINION | - | S2, S5 |

### 4.3 Subsection 2.3: documented numbers and unknown caps (RP:91-107)

| ID | RP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| RT2.3-a | 93 | The general specifications demand normalized transforms and the documented root origin; Marketplace bodies follow their own budgets. (The paper gives no values for these.) | VERIFIED | R1, R2 | S3, S5 |
| RT2.3-b | 95 | Apply Marketplace budgets to the whole asset group together, not as a separate allowance per part mesh. | OPINION | R2 | S3 |
| RT2.3-c | 97 | The paper found no current universal limit on custom-rig bones, Motor6D count or Studio model file size. Unsourced bone figures of 64, 128 or 256 must not be repeated. If an asset is rejected, log the importer's exact message at that time. An import that succeeds says nothing about crowd cost. | OPINION-unresolved | - | S2, S5 |
| RT2.3-d | 99 | Count runtime cost in these units: visible instances, deform bones, vertices, MeshParts, materials, physics proxies, animation tracks and scripted updates. The importer's hard limit is not a mobile goal. Set a studio budget only after measuring the planned pet or NPC count on the planned device. | OPINION | - | S2, S5 |

Paper table (RP:101-107): see numbers N01-N08, N11-N12.

## 5. Section 3: planning with modeler and animator (RP:109-162)

| ID | RP | Lesson | Tag | Src | Stage | Who also |
| --- | --- | --- | --- | --- | --- | --- |
| PL-a | 111 | Two collaboration examples: a technical artist reshaping the rig around animator requests (Fiddlesticks), and Roblox's Creature breakdown choosing neutral modeling poses and placing joints where motion needs them. They are illustrations, not proof that all studios follow this template. | VERIFIED | S1, R6 | S1, S2 | [for-animator] |
| PL-b | 113 | Hold a motion review before topology is final. Modeler supplies silhouettes from front, side and back, material borders, hidden geometry and where parts should split. Animator supplies reference poses, camera angles, contact points and timing needs. Rigger proposes the articulation and flags risky zones. Runtime engineer states the controller type, who owns movement, collisions, sockets and how many instances appear at once. Resolve conflicts by posing a quick proxy rather than guessing about a finished rig. | OPINION | - | S1, S2 | [for-animator] [for-modeler] |
| PL-c | 115 | Shoulder: locate the arm's pivot, the clavicle's share, armpit squash, deltoid outline and armor clearance. Hip: socket centers, pelvis width, how far legs spread, and crouch contact between thigh and belly. Neck: split skull turning from neck bending spread along its length, and mark the chest area to protect. Elbow and knee: hinge direction, the control for the bend plane, which side compresses, what supports the outline. Departures from anatomy for style are approved per pose, not per label. | OPINION | - | S1, S2 | [for-animator] [for-modeler] |
| PL-d | 117 | Do not hand a stylized rig a table of anatomical angles. For each joint write down minimum and maximum rotation, any allowed translation, the axis convention and coupled motion, all taken from what the animation needs. If the reference shows an extreme attack, test that extreme even though walking never reaches it. | OPINION | - | S1, S2, S6 | [for-animator] |
| PL-e | 117 | Treat three kinds of limit as separate: constraints used while authoring, IK constraints at runtime, and physics limits. A Blender Limit Rotation constraint does not turn into a Roblox joint limit automatically. | OPINION | - | S5 | |
| PL-f | 119 | Lock the motion range and the asset's role before final skinning. After animation starts, topology edits, joint moves, bone renames and rest-pose changes each require a versioned migration and a retest. | OPINION | - | S2, S5, S7 | [for-animator] [for-modeler] |
| PL-g | 119 | Approvals: animator = usability; modeler = silhouette and seam treatment; rigger = technical validity; runtime owner = Studio behavior. | OPINION | - | S3, S4, S6 | [for-animator] [for-modeler] |
| PL-h | 30 | See rule 15: the handoff bundle (source, export skeleton, control manifest, sheet, clips, Studio test results) travels together. | OPINION | - | S5-S7 | [for-animator] |

Paper table (RP:158-162).

| RP | Rule | Number | Mark | Src, date |
| --- | --- | --- | --- | --- |
| 160 | Test the requested performance before locking the rig | no universal ROM | VERIFIED example; OPINION policy | S1, 2020-01-14 |
| 161 | Neutral geometry and purposeful joint placement | asset-dependent | VERIFIED example | R6, undated, chk 2026-10-20 |
| 162 | Record joint ranges and budget ownership | must be filled per asset | OPINION | "Proposed workflow", 2026-10-20 |

### 5.1 Rig requirements sheet template: fields as data (RP:121-147)

Fill rules (RP:123, OPINION): the roles complete it jointly; an empty cell means not yet decided (never unlimited); each number carries a unit and a named owner; budget cells are studio choices unless a platform limit is cited. Stage column = my suggested filler (matches the workflow sheet sections), not stated in the paper.

| Field | RP | Content the field asks for | Suggested stage |
| --- | --- | --- | --- |
| RS01 | 125 | Asset ID / revision / source hash | S0 |
| RS02 | 126 | Purpose: avatar body / custom player / NPC / pet / weapon / vehicle / moving prop | S0 |
| RS03 | 127 | Visual style and approved silhouette references | S0 |
| RS04 | 128 | Camera distance and first-person / third-person requirements | S0 |
| RS05 | 129 | Source: hand-made / Tripo model ID and model version / other | S0 |
| RS06 | 130 | Source pose; Blender version; add-on versions; MCP server and tool-schema version | S0 |
| RS07 | 131 | Target: Roblox Studio version/build; target device; simultaneous visible instances | S0 |
| RS08 | 132 | Runtime representation: rigid / skinned / mixed; reason | S2 |
| RS09 | 133 | Animation driver: Humanoid + Animator / AnimationController + Animator / scripted articulation | S0, S2 |
| RS10 | 134 | Movement owner; in-place or root-translation policy | S0 |
| RS11 | 135 | Physics/visual ownership; collision proxies; detachable pieces | S2 |
| RS12 | 136 | Unit convention; expected dimensions in studs; export/import axis mapping | S2 |
| RS13 | 137 | Topology budgets: triangles per mesh; total triangles; materials; UV and texture requirements | S2 |
| RS14 | 138 | Rig budgets: deform joints; control joints; exported joints; physics joints; measured runtime cost | S2, S5 |
| RS15 | 139 | Official constraints that apply; source IDs and last-check date | S2 |
| RS16 | 140 | Approved actions; stress poses; required contacts; locomotion and attack references | S1 [for-animator] |
| RS17 | 141 | Face representation and required expressions | S1 [for-animator] |
| RS18 | 142 | Attachments: grip / muzzle / VFX / seat / interaction / hitbox; required orientation | S1, S2 |
| RS19 | 143 | Export schema; bone names and parent map; mesh names; attachment names | S2, S5 |
| RS20 | 144 | Allowed helper bones; correction strategy; unsupported-feature fallback | S2 |
| RS21 | 145 | Numerical acceptance tolerances and visual approval views | S2, S4 |
| RS22 | 146 | Known exceptions; responsible person; retest trigger | S5 |
| RS23 | 147 | Sign-offs: modeler / rigger / animator / runtime | S4, S6 |

Per-region table the sheet carries (RP:149-156). Columns: region or part | separate surface or continuous | parent and joint center | axis and motion range with units | deformation or overlap plan | required test. Rows are pre-labelled; cells are "Fill".

| Row | RP | Region | What each Fill cell must hold (hint from the paper) | Required test (given) |
| --- | --- | --- | --- | --- |
| RG1 | 151 | Head and neck | joint coordinates + coordinate space; yaw/pitch/roll and translations; protected torso region | head isolation + looking extremes |
| RG2 | 152 | Shoulder and arm | socket and clavicle role; arm lift/reach/twist; armpit loops or ball socket | raise + cross-body reach |
| RG3 | 153 | Elbow and wrist | bend plane and wrist center; flexion/twist; compression and twist span | fold + wrist rotation |
| RG4 | 154 | Hip and knee | pelvis and hinge centers; crouch/spread/flexion; hip crease and kneecap support | deep required crouch + step |
| RG5 | 155 | Tail, wing or ear | branch chain; bend/twist/fold; base and membrane | opposed bends + silhouette |
| RG6 | 156 | Weapon or machine | hinge/rail center; degrees or linear travel; rigid, clearance and detach rules | full reload or mechanism cycle |

## 6. Section 4: from merged AI mesh to rig (RP:164-263)

### 6.1 Subsection 4a: diagnose and cut into rigid parts (RP:166-182)

| ID | RP | Lesson | Tag | Src | Stage | Who also |
| --- | --- | --- | --- | --- | --- | --- |
| 4a-a | 168 | Look before touching. A single Blender object may contain several islands, while a sleeve that looks separate may be welded into the torso. Take counts of: objects, mesh datablocks, connected components, tiny floating fragments, intersecting shells, non-manifold boundaries, UV islands and materials. | OPINION | - | S2 | [for-modeler] |
| 4a-b | 168 | View wireframe over shaded orthographic renders. Decide for each painted detail whether it is real geometry or texture only. Preserve an untouched original and the transform from original to working copy. | OPINION | - | S0, S2 | [for-modeler] |
| 4a-c | 170 | Blender Separate can split by selection, material or connectivity. Bisect has Fill and Clear-side options. | VERIFIED | B8, B9 | S3 | [for-modeler] |
| 4a-d | 172 | When usable islands already exist, split them out and label them instead of slicing the whole mesh without need. | OPINION | - | S2, S3 | [for-modeler] |
| 4a-e | 172 | For welded parts, choose the boundary from the motion plan. Joint to concealer pairs: neck - collar; shoulder - sleeve or armor socket; elbow - cuff or ball joint; wrist - glove; hip - pelvis shell; knee - kneecap piece; ankle - boot. | OPINION | - | S2 | [for-modeler] [for-animator] |
| 4a-f | 172 | Slicing flat through a bare organic neck normally alters the design instead of hiding anything. (Workflow hook: route as needs-decision.) | OPINION | - | S2 | [for-modeler] |
| 4a-g | 174 | Store each cut boundary as a named face set or vertex group. Work in the correct local space and apply face splitting or Bisect to the target region alone. Convert cutting planes to mesh-local space the same way every time. A shared world-space plane must not slice every limb it happens to cross. Keep the part's world position when splitting it off. | OPINION | - | S3 | [for-modeler] |
| 4a-h | 176 | Close both halves of every cut. A flat, concealed boundary can take a flat fill followed by chosen triangulation. Where the surface curves or flow matters, use Grid Fill or hand-built patches. A large concave cap that triangulates across the outline is to be avoided. | OPINION | - | S3 | [for-modeler] |
| 4a-i | 176 | After capping: recalculate normals, count remaining boundary edges, check thickness and backfaces, UV-unwrap the cap or assign it a hidden-cap material, and check that texture carries across. A cap is only hidden if nothing exposes it during animation. | OPINION | - | S3, S4 | [for-modeler] |
| 4a-j | 178 | Conceal the cut using shells that overlap, recessed sockets, sleeves, collars or designed ball joints. Derive the overlap depth from the approved motion range rather than a fixed share of the limb's size. | OPINION | - | S2, S3 | [for-modeler] [for-animator] |
| 4a-k | 178 | Surfaces sitting on the same plane may flicker (z-fighting), and overly deep overlaps visibly clash. A gap left on purpose is acceptable if art direction wants it. When bare skin must move with no visible seam at all, a continuous skinned transition is the better choice. | OPINION | - | S2, S3 | [for-modeler] |
| 4a-l | 180 | Set each pivot at the true articulation center, not the piece's centroid, and keep world transforms intact when moving origins. | OPINION | - | S2, S5 | [for-modeler] |
| 4a-m | 180 | Motor6D route: export the joint coordinate frames and assemble the joint tree in Studio. Merely importing the split meshes does not produce the intended animated assembly. | OPINION | - | S5 | |
| 4a-n | 180 | Skeletal rigid route: bind all of the piece's deforming vertices to its own bone. Clearing weights and only parenting to the armature object does not equal deformation by a bone. | OPINION | - | S5 | |
| 4a-o | 182 | Test each rigid piece with its parent held still: the piece keeps its internal shape, the seam stays covered from every needed camera, and unrelated pieces stay put. Compare the rest silhouette and sizes with the source. Record deliberate geometry fixes separately from articulation changes. | OPINION | - | S4, S5, S6 | [for-animator] [for-modeler] |

### 6.2 Subsection 4b: skin the merged surface (RP:184-192)

| ID | RP | Lesson | Tag | Src | Stage | Who also |
| --- | --- | --- | --- | --- | --- | --- |
| 4b-a | 186 | Where continuity matters, keep the organic surface connected, but cut out false bridges: arm-to-torso, finger-to-finger, leg-to-leg, tail-to-body, layer-to-layer clothing. A generator can fuse these with real triangles, and weight painting cannot bring back separate geometry when a wrong bridge would have to tear or stretch in every valid pose. | OPINION | - | S2, S3 | [for-modeler] |
| 4b-b | 188 | Rebuild a bend zone when the current mesh cannot take the bend: run edge rings across the joint, give both the squeezed and stretched sides enough geometry, and keep sliver triangles and high-valence poles away from the deepest fold. Let density follow outline curvature and deformation instead of texture noise, and stop at the leanest mesh that passes the required poses. | OPINION | - | S3 | [for-modeler] |
| 4b-c | 188, 263 | No verified universal edge-loop count for elbow, shoulder or knee. Never say three loops guarantee good deformation. | OPINION-unresolved | B2, D1, R6 (synthesis) | S3 | [for-modeler] |
| 4b-d | 190 | Rebuild only the parts that need it, keep or re-bake the UVs and textures, and compare with the original. A quad result is not evidence of good anatomical flow. Count the triangles that will really be exported, including caps and split quads. If weights come from a proxy, restrict the transfer by body region, because nearest-surface matching mixes up an arm resting on the torso or neighboring legs. | OPINION | - | S3, S4, S5 | [for-modeler] |
| 4b-e | 192 | Bind to the approved skeleton only once joints and rest transforms are final. Treat auto-weights as an initial guess; check which bones influence each vertex, both by numbers and by moving one joint at a time. | OPINION | - | S5 | |
| 4b-f | 192 | Neck weights may fade into the upper torso only across the planned neck transition, so turning only the head never drags the chest. Arm weights must not spill onto the belly or the opposite arm. For rotation along a long segment, add helper or twist joints while staying under the influence limit. | OPINION | - | S5, S6 | [for-animator] |

### 6.3 Subsection 4c: decision table (RP:194-211)

Rule line (RP:196, OPINION): decide region by region, not from the asset's label; robots can have soft cables and animals can wear hard armor. The table is a proposed studio rule, not a vendor measurement. Stage S2. Last column = my mapping to the workflow routes R-cut / R-skin / R-mix / R-reject; not in the paper.

| Row | RP | Model type or requirement | Cut into parts | Skin | Mix, and the deciding test | Workflow route |
| --- | --- | --- | --- | --- | --- | --- |
| DT01 | 200 | Retro toy humanoid with visible joint breaks | Preferred, if the silhouette allows sockets | Optional, for soft accessories | Mixed if clothing must bend. Test: rotate every seam | R-cut |
| DT02 | 201 | Bare-skinned humanoid seen close | Only at boundaries that are hidden on purpose | Preferred: continuous neck, shoulders, hips | Rigid eyes, teeth, gear. Test: head isolation and reach | R-skin |
| DT03 | 202 | Plush or furry pet | Only where fur or design hides a break | Preferred for body and neck | Rigid eyes/feet when the style fits. Test: crouch and head turn | R-skin (R-mix for eyes/feet) |
| DT04 | 203 | Low-detail pet at small screen size | Often enough for a bobbing body/head | Use when the bend reads at that size | Choose by the game camera's silhouette, not the generator preview | R-cut or R-skin |
| DT05 | 204 | Armored humanoid or mechanical creature | Rigid plates and pistons | Soft body, cables, seals | Mixed is preferred. Test: clearance through extremes | R-mix |
| DT06 | 205 | Bird with rigid feather cards | Rigid feather groups where useful | Wing/body transitions and membranes | Mixed. Test: fold and full extension without collapse | R-mix |
| DT07 | 206 | Snake or tentacle | Articulated toy only | Preferred bending chain | Rigid end pieces if needed. Test: opposite-curvature bends | R-skin |
| DT08 | 207 | Rifle, sword, reload mechanism | Preferred for bolt, magazine, blade | Flexible strap only | Mixed. Test: reload and grip contact | R-cut/R-mix |
| DT09 | 208 | Vehicle with steering/suspension | Preferred for wheels, doors, linkages | Flexible hoses or stylized suspension boots | Mixed; physics rig separate from visual rig | R-mix |
| DT10 | 209 | Door, turret, machine, chest | Preferred hinge or rail articulation | Only for intentional soft deformation | Test: pivot, full travel, collisions, opening clearance | R-cut |
| DT11 | 210 | Mesh with fused limbs and unusable topology | Cut and rebuild if the design allows breaks | Retopologize if a continuous surface is mandatory | Reject or regenerate if neither repair meets scope | R-reject (else R-cut/R-skin) |
| DT12 | 211 | Marketplace R15 avatar | Follow the required separate body objects | Skin inside the applicable body parts | Use the template and validator; custom shortcuts do not qualify | n/a (avatar contract) |

### 6.4 Subsection 4d: Tripo segmentation and auto-rigging at the cutoff (RP:213-233)

Facts (all VERIFIED = vendor documents it; quality of any output is not shown, EC1):

| ID | RP | Operation | Fact | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | 215 | Mesh Segmentation | POST /v3/mesh/segment. Default model v1.0-20250506. v2.0-20260430 Beta adds semantic labeling. v2 offers granularity simple / balanced / detailed and connectivity splitting. Giving ref_image overrides the granularity and connectivity options. Input file ceiling 150 MB. | VERIFIED | T2 | S2, S3 |
| T02 | 217 | Smart Segmentation | Separate pipeline, POST /v3/mesh/smartsegment, includes modeling. Model input must be GLB, with a column-major 4x4 transform (16 floats). Supports text hints and granularity coarse / medium / fine. | VERIFIED | T4 | S2, S3 |
| T03 | 221 | Rig check | Tells whether the model can be rigged and suggests a rig type. | VERIFIED | T3 | S2 |
| T04 | 221 | Auto Rigging | Output GLB or FBX. Categories listed: biped, quadruped, hexapod, octopod, avian, serpentine, aquatic, others. v2.5-20260210 supports non-humanoids. v3.0-20260909 is recommended by Tripo for better humanoids and keeps v2.5 quality and speed for other types. API default stays v1.0-20240301. Input file ceiling 150 MB. | VERIFIED | T1, T3, T5 | S2, S5 |
| T05 | 225 | Retopology / Smart UV | Retopology v3.0: face_limit 500-20,000 for triangle output, 500-10,000 for quad output. Must be requested explicitly; default stays v2.0. Smart UV input ceiling 80,000 equivalent triangles. These limits belong to those operations, not to rigging, and are not Roblox budgets. | VERIFIED | T5, T6 | S3 |
| T06 | 223 | Rig naming | The paper reports no documented Roblox/R15 preset among v3.0 rig naming presets. Mixamo/Unity/Unreal naming is not Roblox avatar compliance. | OPINION | T1 | S2, S5 |

Lessons:

| ID | RP | Lesson | Tag | Src | Stage | Who also |
| --- | --- | --- | --- | --- | --- | --- |
| 4d-a | 219 | Prefer plain segmentation when approved geometry must stay as is, and still diff its result against that geometry. Prefer Smart Segmentation only when regenerated or completed parts are acceptable, and then review what changed in proportion, UVs, materials and outline. | OPINION | - | S2, S3 | [for-modeler] |
| 4d-b | 219 | A semantic label or a closed (watertight) part does not show that the seam suits rotation or that the topology is ready for a joint. | OPINION | - | S3, S4 | [for-modeler] |
| 4d-c | 223 | Tripo carries four unrelated version numbers: the API generation (v3), the geometry-generation model, the segmentation model and the rigging model. Never blur them; write each one down. | OPINION | - | S0, S2 | |
| 4d-d | 223 | Import the Tripo rig into Blender and run the same joint and weight audit as for a hand rig. | OPINION | - | S5 | |
| 4d-e | 227 | No polygon-count input limit for Tripo rigging or plain segmentation was found. The 150 MB figure limits bytes. The retopology output range and the Smart UV input limit must not be reused as rigging limits. Limits in the Tripo Studio web UI could differ from the API, so record which route was used and any error returned. | OPINION-unresolved | T1-T3 | S2, S5 | |
| 4d-f | 229 | StraySpark (2026-05-14) reports a Tripo workflow that exported fine but the result showed sagging shoulder/chest and poorly weighted jaw. Protocol: Blender, Unreal retargeting, movement tests. It does not show Roblox acceptance or the quality of the September rigging model. It calls Tripo biped-only, which disagrees with current official docs (X03). | EXPERIENCE | E1, T1 | S2, S5 | |
| 4d-g | 231 | Treat E1 as a hint about what can go wrong, not as a feature comparison or a ranking: it has no reproducible sample set, no precise model and version coverage, and the site markets its own mesh tools. Nothing reliable and independent exists on failure rate, quality order or time saved for the October v3.0 rig model, nor on segmentation quality for that version. Vendor previews and unsupported review-site numbers cannot stand in. | OPINION | E1 | S2 | |
| 4d-h | 233 | An automatic result passes only if it satisfies the asset's articulation contract: required regions split correctly, no surface missing, joints and axes right, motion usable, influence count legal, silhouette and textures preserved, and playback working in the engine. | OPINION | - | S4, S5, S6 | [for-animator] |
| 4d-i | 233 | Pick the repair by symptom: bad boundaries or pivots lead to manual segmentation; fused or badly bending surface leads to retopology; good geometry with bad motion leads to hand repair of bones and weights; a fix that would push the design outside the approved scope leads to regenerating or remodeling. | OPINION | - | S4, S5 | [for-modeler] |
| 4d-j | 27, 233 | Rule 12 applied: Tripo's rig is only a candidate and must pass the same tests as a hand-built rig (joints, weights, topology, names, Roblox round trip). | OPINION | T3, E1 | S5 | |

### 6.5 Subsection 4e: other auto-rigging choices (RP:235-251)

| ID | RP | Lesson | Tag | Src | Stage |
| --- | --- | --- | --- | --- | --- |
| 4e-a | 237 | Adobe Mixamo FAQ (last updated 2021-09-14, still the accessible official text): auto rigging works for bipedal humanoids only, and the FAQ cautions about odd proportions, extra limbs, posed or lopsided models, detached parts and dirty meshes. It is not evidence of any 2026 model. | VERIFIED | A1 | S2 |
| 4e-b | 239 | Mixamo is a reasonable humanoid baseline if the input fits its conditions, but a weak default for pre-split toy parts, birds, quadrupeds or unusual mechanisms. Do not weld or conceal a wanted design feature merely to satisfy an auto-rigger, unless the plan restores and re-checks it afterward. | OPINION | - | S2 [for-modeler] |
| 4e-c | 241 | Reallusion AccuRIG: guided body and hand setup. Its comparison separates free and advanced versions. Its Blender tutorial supports hands with zero to five fingers. | VERIFIED | A2, A3 | S2 |
| 4e-d | 243 | AccuRIG suits cases where guided landmark correction helps; confirm what the specific free or paid edition can export and edit. Auto-Rig Pro and Rigify offer controllable Blender workflows that stay useful once an AI-made skeleton has been fixed. Neither shows that generated geometry can skip cleanup. | OPINION | B3, B4 | S5 |
| 4e-e | 245 | UniRig (arXiv 2025-04-16) proposes skeleton and skinning prediction across categories. Puppeteer (arXiv 2025-08-14) describes skeleton prediction, weight inference and a following animation pipeline. Research results, not Roblox product integrations. | VERIFIED | A4, A5 | S2 |
| 4e-f | 247 | Skin Tokens (first submitted 2026-02-04, revised 2026-10-19) introduces a compact learned skin-weight form and a unified TokenRig skeleton-and-skin framework. Benchmark gains are author-reported research metrics, not Roblox acceptance. | VERIFIED | A6 | S2 |
| 4e-g | 249 | TokenRig can be tried as a research candidate if its code, weights, license and hardware requirements suit the studio. Nothing in the paper implies a commercial product, an MCP hookup or an R15 exporter exists for it. Score its saved output on the same local acceptance set as the other riggers. | OPINION | A6 | S2 |
| 4e-h | 251 | Run a local benchmark before adopting any research or new commercial rigger: one approved mesh, one required motion set, exported files kept, exact versions logged, repair effort and export success measured. A paper score or demo is no forecast that your Roblox pet will pass. A tool that only assists animation is not an auto-rigger unless its own current docs say so. | OPINION | - | S2, S5 |

## 7. Number register (RP:1-264)

Dates: "undated" = source shows no date; paper checked it on 2026-10-20. Unit is as the paper gives it; "not stated" = the paper gives none.

| ID | Value | Unit / meaning | RP | Src, date | Tag |
| --- | --- | --- | --- | --- | --- |
| N01 | 20,000 | triangles, maximum per individual general Roblox mesh | 17, 103 | R1, undated | VERIFIED |
| N02 | 4 | bone or joint influences per vertex, maximum | 18, 104 | R1, undated | VERIFIED |
| N03 | 15 | named mesh objects in current avatar bodies (appears only in rule 04, no table row) | 19 | R2, undated | VERIFIED |
| N04 | 37 | additional optional joints, advanced R15 ("up to") | 19, 106 | R2, undated | VERIFIED |
| N05 | 4000 | Marketplace head budget; unit not stated in the paper | 105 | R2, undated | VERIFIED |
| N06 | 1750 | Marketplace torso budget; unit not stated | 105 | R2, undated | VERIFIED |
| N07 | 1248 | Marketplace budget per limb asset; unit not stated | 105 | R2, undated | VERIFIED |
| N08 | 10,742 | Marketplace total body budget; unit not stated (my arithmetic, not in paper: 4000 + 1750 + 4 x 1248 = 10,742; the count of limb assets is not given) | 105 | R2, undated | VERIFIED |
| N09 | 52 | bones, legacy Dota 2 NPC workflow cap. Never a Roblox limit | 58, 60, 67 | V1, undated (legacy, chk 2026-10-20) | VERIFIED |
| N10 | 23 | heroes in the Overwatch session abstract (scope, not a rig number) | 46, 65 | S2, GDC 2017 (day not established) | VERIFIED |
| N11 | 64 / 128 / 256 | bones: unsourced folklore; do not repeat | 97 | none | OPINION-unresolved (as a topic) |
| N12 | not established | universal custom-rig bone/joint cap; universal Motor6D count; universal Studio model-file byte ceiling | 97, 107 | R1-R3 review, 2026-10-20 | OPINION-unresolved |
| N13 | 150 | MB, input file ceiling for Tripo segmentation | 215, 257 | T2, undated | VERIFIED |
| N14 | 150 | MB, input file ceiling for Tripo auto-rig | 221, 257 | T1, undated | VERIFIED |
| N15 | v1.0-20250506 | Tripo segmentation default model | 215, 255 | T2, undated | VERIFIED |
| N16 | v2.0-20260430 Beta | Tripo segmentation model with semantic labeling | 215, 255 | T2, undated | VERIFIED |
| N17 | 16 | floats = column-major 4x4 transform for SmartSegment (GLB input) | 217, 256 | T4, undated | VERIFIED |
| N18 | v2.5-20260210 | Tripo rig model, supports non-humanoids | 221 | T1, undated (version carries its own date) | VERIFIED |
| N19 | v3.0-20260909 | Tripo rig model, humanoid upgrade, must be requested; T5 entries are headed 2026-10 and 2026-09, exact days not supplied | 26, 221, 258 | T1; T5, 2026-10 | VERIFIED |
| N20 | v1.0-20240301 | Tripo rig API default | 221, 258 | T1, undated | VERIFIED |
| N21 | 500-20,000 | triangle face_limit, retopology v3.0 (triangle output) | 225, 259 | T5, 2026-10; T6 chk 2026-10-20 | VERIFIED |
| N22 | 500-10,000 | face_limit, retopology v3.0 (quad output) | 225, 259 | T5, 2026-10; T6 chk 2026-10-20 | VERIFIED |
| N23 | v2.0 | retopology default model (v3.0 must be requested) | 225 | T5, 2026-10 | VERIFIED |
| N24 | 80,000 | equivalent triangles, Smart UV input ceiling | 225 | T5, 2026-10; T6 | VERIFIED |
| N25 | not established | general polygon limit for Tripo rigging or plain segmentation | 227, 260 | T1-T3 review, 2026-10-20 | OPINION-unresolved |
| N26 | not established | universal edge-loop count for joints (and "three loops" is explicitly not a guarantee) | 188, 263 | B2/D1/R6 synthesis, 2026-10-20 | OPINION-unresolved |
| N27 | not established | universal control count; universal error tolerance; universal ROM | 64, 66, 160 | S1 2020-01-14; S3 2015-07-25 | VERIFIED example; OPINION policy/test |
| N28 | 0 to 5 | fingers per hand supported in AccuRIG's Blender tutorial | 241 | A3, 2022-11-11 | VERIFIED |
| N29 | 20 | words, upper bound for key quotations in the source list (paper convention) | 10 | paper | contract |
| N30 | 10,000 | triangles in R6's old text; conflicts with current docs (source-list note, outside range) | 739 | R6, undated legacy | see X04 |
| N31 | 22 | HumanoidRigDescription joint slots; not a universal cap (source-list note, outside range) | 769 | R12, undated | see source table |

## 8. Claims to check (for the fact-check agents)

Kinds: roblox / blender / tripo / other-tool / industry. The tag column is the paper's. "none" = the paper gives no source ID.

| ID | Claim | RP | Src | Kind | Tag |
| --- | --- | --- | --- | --- | --- |
| C01 | General Roblox meshes: 20,000 triangles at most per individual mesh | 17, 103 | R1 | roblox | VERIFIED |
| C02 | A vertex may have at most 4 bone/joint influences | 18, 104 | R1 | roblox | VERIFIED |
| C03 | The documented Root must carry no weights | 18 | R1 | roblox | VERIFIED |
| C04 | Current avatar bodies use 15 named mesh objects | 19 | R2 | roblox | VERIFIED |
| C05 | Advanced R15 supports up to 37 additional optional bones or joints | 19, 106 | R2 | roblox | VERIFIED |
| C06 | Marketplace body budgets: head 4000, torso 1750, limb asset 1248, total 10,742 (unit not stated) | 105 | R2 | roblox | VERIFIED |
| C07 | Marketplace budgets apply to the combined asset group, not per part mesh | 95 | R2 | roblox | OPINION |
| C08 | Motor6D joins two BaseParts in an animatable way | 73 | R8 | roblox | VERIFIED |
| C09 | Bone motion changes rendered geometry, not collision shape; skinning assignments are stored in MeshPart asset data | 29, 73 | R7, R8 | roblox | VERIFIED |
| C10 | AnimationController animates non-player objects; its direct LoadAnimation is deprecated; use an Animator | 81 | R9 | roblox | VERIFIED |
| C11 | R15 needs named body objects and a specific hierarchy; advanced adds optional joints with prescribed names and parents | 85 | R2 | roblox | VERIFIED |
| C12 | HumanoidRigDescription and DigitsRigDescription carry advanced body and hand metadata | 85 | R12 | roblox | VERIFIED |
| C13 | General specs require normalized transforms and a documented root origin | 93 | R1, R2 | roblox | VERIFIED |
| C14 | No universal custom-rig bone cap, Motor6D limit or Studio file byte ceiling exists in current docs; 64/128/256 is folklore | 97, 107 | R1-R3 | roblox | OPINION-unresolved |
| C15 | A Blender Limit Rotation constraint does not become a Roblox joint limit | 117 | none | roblox | OPINION |
| C16 | A Blender object origin alone is not a full Motor6D configuration; importing separated meshes does not build the animated assembly; joint frames must be serialized and the joint tree built in Studio | 75, 180 | none | roblox | OPINION |
| C17 | Blender Root / HumanoidRootNode are not the same as runtime HumanoidRootPart or named animation joints | 89 | none | roblox | OPINION |
| C18 | Roblox templates and validator are the schema authority for standard avatars | 89 | none | roblox | OPINION |
| C19 | A Marketplace R15 avatar must follow the required separate body objects and skin within body parts; custom shortcuts do not qualify | 211 | none | roblox | OPINION |
| C20 | A custom quadruped does not become R15 by renaming; Mixamo- or Tripo-named humanoids can be custom rigs but do not meet avatar publishing rules | 87 | none | roblox | OPINION |
| C21 | Roblox's Creature breakdown picks neutral modeling poses and concentrates joints where motion needs them | 111, 161 | R6 | roblox | VERIFIED |
| C22 | R6's 10,000-triangle and zero-influence statements conflict with current docs | 739 (source list) | R6 | roblox | paper note |
| C23 | Blender Separate can split by selection, material or connectivity (loose parts) | 170 | B8 | blender | VERIFIED |
| C24 | Blender Bisect has Fill and Clear Inner/Outer options | 170 | B9 | blender | VERIFIED |
| C25 | Blender constraint results can be baked; the constraint definitions are not saved by legacy FBX export | 28 | B5 | blender | VERIFIED |
| C26 | Normalize and influence pruning (Clean / Limit Total) are separate Blender weight operations | 24 | B2, R1 | blender | OPINION |
| C27 | Rigify and Auto-Rig Pro give controllable Blender rig workflows and remain usable after an AI skeleton is repaired | 243 | B3, B4 | blender | OPINION |
| C28 | Removing weights and merely parenting a mesh to the armature object is not the same as bone deformation | 180 | none | blender | OPINION |
| C29 | Nearest-surface weight transfer from a proxy can confuse a touching arm and torso or adjacent legs | 190 | none | blender | OPINION |
| C30 | Coincident surfaces can cause z-fighting | 178 | none | industry | OPINION |
| C31 | Tripo segmentation endpoint is POST /v3/mesh/segment | 215 | T2 | tripo | VERIFIED |
| C32 | Segmentation default model v1.0-20250506; v2.0-20260430 Beta adds semantic labeling | 215, 255 | T2 | tripo | VERIFIED |
| C33 | v2 segmentation supports granularity simple/balanced/detailed and connectivity splitting | 215 | T2 | tripo | VERIFIED |
| C34 | ref_image overrides the granularity and connectivity options | 215 | T2 | tripo | VERIFIED |
| C35 | Segmentation input file ceiling is 150 MB | 215, 257 | T2, T1 | tripo | VERIFIED |
| C36 | Smart Segmentation is POST /v3/mesh/smartsegment and includes modeling | 217 | T4 | tripo | VERIFIED |
| C37 | SmartSegment model input must be GLB with a column-major 4x4 transform of 16 floats | 217, 256 | T4 | tripo | VERIFIED |
| C38 | SmartSegment supports text hints and coarse/medium/fine granularity | 217 | T4 | tripo | VERIFIED |
| C39 | Rig check reports rig-ability and a recommended rig type | 221 | T3 | tripo | VERIFIED |
| C40 | Auto Rigging outputs GLB or FBX; categories: biped, quadruped, hexapod, octopod, avian, serpentine, aquatic, others | 221 | T1 | tripo | VERIFIED |
| C41 | Rig model v2.5-20260210 supports non-humanoids | 221 | T1 | tripo | VERIFIED |
| C42 | Rig model v3.0-20260909 is recommended by Tripo for humanoids and keeps v2.5 quality/speed for other types | 221 | T1, T5 | tripo | VERIFIED (vendor claim) |
| C43 | Rig API default is v1.0-20240301; v3.0 must be requested explicitly | 26, 221, 258 | T1 | tripo | VERIFIED |
| C44 | Auto-rig input file ceiling is 150 MB | 221, 257 | T1 | tripo | VERIFIED |
| C45 | Retopology v3.0 face_limit is 500-20,000 (triangle) and 500-10,000 (quad); must be requested; default v2.0 | 225, 259 | T5, T6 | tripo | VERIFIED |
| C46 | Smart UV input ceiling is 80,000 equivalent triangles | 225 | T5, T6 | tripo | VERIFIED |
| C47 | v3.0 rig naming presets include no documented Roblox/R15 preset; Mixamo/Unity/Unreal naming exists | 223 | T1 | tripo | OPINION |
| C48 | No general input-polygon cap for Tripo rigging/plain segmentation is documented; Studio UI limits may differ from API | 227, 260 | T1-T3 | tripo | OPINION-unresolved |
| C49 | Tripo segmentation and rigging are different operations | 25 | T1, T2, T4 | tripo | VERIFIED |
| C50 | Mixamo FAQ (2021-09-14): auto rigging for bipedal humanoids only; warns about extreme proportions, extra appendages, posed/asymmetric models, disconnected parts, dirty meshes | 237, 262 | A1 | other-tool | VERIFIED |
| C51 | AccuRIG offers guided body/hand setup; free and advanced versions differ; Blender tutorial supports hands with 0-5 fingers | 241 | A2, A3 | other-tool | VERIFIED |
| C52 | UniRig (arXiv 2025) proposes skeleton and skinning prediction across categories | 245 | A4 | other-tool | VERIFIED |
| C53 | Puppeteer (arXiv Aug 2025) describes skeleton prediction, weight inference and an animation pipeline | 245 | A5 | other-tool | VERIFIED |
| C54 | Skin Tokens / TokenRig (2026, revised 2026-10-19) introduces a compact learned skin-weight representation and unified skeleton-and-skin prediction | 247 | A6 | other-tool | VERIFIED |
| C55 | StraySpark (2026-05-14): Tripo workflow exported, shoulder/chest slumping, weak jaw weighting; protocol Blender + Unreal retargeting + movement tests; says Tripo is biped-only | 229 | E1 | other-tool | EXPERIENCE |
| C56 | StraySpark site promotes its own mesh tools; no reproducible corpus | 231 | E1 | other-tool | OPINION |
| C57 | Riot Fiddlesticks: animator-requested head shake via jiggle chain, plus special arm-follow setup | 42 | S1 | industry | VERIFIED |
| C58 | Blizzard GDC 2017 session covers 23 heroes then in Overwatch, hero rigs and first-person performance | 46 | S2 | industry | VERIFIED |
| C59 | Disney Frozen paper: dual-quaternion skinning avoids candy-wrapper but needs production extensions; not a drop-in for LBS | 50 | D1 | industry | VERIFIED |
| C60 | Disney Research: collapsing elbows, twist artifacts, joint bulging; proposes optimized centers of rotation | 50 | D2 | industry | VERIFIED |
| C61 | Pixar 2020: pose-space sculpting is part of the corrective-rig workflow | 54 | P1 | industry | VERIFIED |
| C62 | Pixar 2024 Inside Out 2: specialized shaping and mouth-rig needs | 54 | P2 | industry | VERIFIED |
| C63 | Valve Dota 2 NPC guide: named effect attachments, bone-related hitboxes, 52-bone limit | 58, 67 | V1 | industry | VERIFIED |
| C64 | Riot compression article: transform error accumulates along descendant chains, appears as foot sliding | 58 | S3 | industry | VERIFIED |
| C65 | No current Deadlock rig budget established; no unseen techniques credited to Naughty Dog, Insomniac, Epic, Supercell | 60 | none | industry | OPINION |

## 9. Contradictions and limits

| ID | RP | Item | Handling in skills |
| --- | --- | --- | --- |
| X01 | 97, 107 | Unknown: universal custom-rig bone cap, Motor6D limit, Studio file byte ceiling. Unsourced 64/128/256 floats around. | Never state a cap. On rejection, log the importer's exact message. Budgets come from measurement on the target phone. |
| X02 | 227, 260 | Unknown: input-polygon cap for Tripo rigging and plain segmentation. Byte limit 150 MB is known. | Do not borrow the 500-20,000 retopology range or 80,000 Smart UV limit. Record route and error text. |
| X03 | 229, 843 | E1 says Tripo is biped-only; T1 (current official docs) lists many rig categories. Paper sides with T1 for the current state and keeps E1 only as an older failure lead. | Cite T1 for capability. Use E1 only as a list of failure modes to test. |
| X04 | 739 | Roblox's legacy Beyond the Dark case study (R6) states a 10,000-triangle figure and a zero-influence statement that conflict with current docs (R1). The paper says "as discussed"; that discussion is outside lines 1-264. | Prefer R1 (20,000 triangles; 4 influences). Use R6 only for the neutral-pose and joint-economy lesson. Check the other extractor's range for the discussion. |
| X05 | 621, 18 | V1 tells modelers to skin a root bone; Roblox forbids weights on Root. | Never transfer V1 practices across platforms. |
| X06 | 58-60, 97 | V1's 52-bone cap is a legacy Dota number; Roblox has no established universal cap. | Do not use 52 as a budget. |
| X07 | 26, 258, 801 | The T5 key line about a default of v2.0 concerns retopology, not rigging. The rig default (v1.0-20240301) comes from T1. T5 entries are headed 2026-10 and 2026-09; exact entry days not supplied while the v3.0 rig model name carries 20260909. | Pin rig model by name in every request. Cite T1 for the default, T5 for the upgrade announcement. |
| X08 | 225 | Smart UV input ceiling is cited to T5 and T6, but T6 is the Retopology reference page. Which page states it is not shown. | Fact-check against the changelog first. |
| X09 | 19, 105-106 | The figure 15 (named mesh objects) appears only in rule 04 with no table row or key quote. Marketplace budget numbers have no stated unit. | Fact-check; do not write a unit until confirmed. |
| X10 | 628 | D2 has two official dates: 2016-07-11 and 2016-07-24. The paper keeps both. | Cite the year (2016) only. |
| X11 | 54, 634-642 | Pixar claims come from indexed excerpts only; original URLs redirected. D1 and S2 day not established. | Do not extend the claims beyond the stated excerpts. |
| X12 | 170, 28, 243 | B5, B8, B9, B3 were read through official indexed excerpts; full stable pages were blocked. B3: do not use indexed 5.4 development docs as 5.2 facts. | Re-check against the installed Blender version before relying on any option name. |
| X13 | 81, 754 | R9's example uses the old direct LoadAnimation call that the same paper calls deprecated. | Code examples in skills must use Animator, not the old call. |
| X14 | 229-231 | E1 is old (2026-05-14), covers unknown Tripo versions, has no Roblox test and a commercial interest. No failure rate, ranking or time saving for v3.0 is known. | Treat Tripo rig quality as untested in this studio until a local test (rule 12). |
| X15 | 249-251 | TokenRig and other research riggers: availability, license, hardware, MCP and R15 export all unknown. | Candidate only; local benchmark first. |
| X16 | 188, 263 | No verified loop count per joint. | Skills must say "as many as the pose test needs", never a number. |
| X17 | 8, 221 | Vendor statements (v3.0 "recommended for humanoids", "improved") are VERIFIED only as what the vendor says. | Label as vendor claim in skills. |
| X18 | 64, 66, 160, 161 | No universal control count, error tolerance or ROM. Per-asset values come from the requirements sheet, with units and owner. | Leave sheet cells blank until the animator or owner fills them. |
| X19 | 44, 56 | Maya jiggle features and Blender drivers are not Roblox runtime behavior. Same for Pixar deformers and shape-key drivers. | Bake to supported export joints or spec a separate Roblox implementation. |
| X20 | 10 | The paper has not run any Blender, MCP or Roblox round trip (RP:847). Every test in it is an instruction, not a result. | Skills mark tests as to-do; results come from this studio's runs. |

## 10. Source IDs used in lines 1-264 (resolved from RP:597-845)

| ID | Source | Date and limits | RP |
| --- | --- | --- | --- |
| S1 | Riot Games, dev article on Fiddlesticks VGU | published 2020-01-14; developer breakdown; no Roblox implementation | 603 |
| S2 | Jesse Davis, Blizzard, Animation Pipeline of Overwatch | GDC 2017, exact day not established; session abstract only | 608 |
| S3 | Riot Games, Compressing Skeletal Animation Data | published 2015-07-25; technical article; not a Roblox compression recipe | 613 |
| V1 | Valve, Dota 2 Workshop Couriers/NPC requirements | undated; legacy; chk 2026-10-20 | 618 |
| D1 | Walt Disney Animation, Enhanced Dual Quaternion Skinning for Production Use | SIGGRAPH 2013, day not established; abstract | 623 |
| D2 | Le and Hodgins, Disney Research, Skinning with Optimized Centers of Rotation | official pages 2016-07-11 and 2016-07-24 (SIGGRAPH 2016) | 628 |
| P1 | Pixar, Sculpt Processing for Character Rigging | SIGGRAPH 2020 Talks, 2020-08-17 as indexed; excerpt; URL redirected | 634 |
| P2 | Pixar, Inside Out 2 Character Rig Challenges | SIGGRAPH 2024, day not established; excerpt; URL redirected | 640 |
| B2 | Blender 5.2 LTS Manual, Editing Weight Paint | undated; chk 2026-10-20 via indexed excerpts | 658 |
| B3 | Blender 5.2 LTS Manual, Rigify | undated; indexed material; no 5.4 dev docs as 5.2 facts | 664 |
| B4 | Artell/Lucky3D, Auto-Rig Pro Game Engine Export | undated; bind-pose issue fixed in 3.78.49; engine settings are not Roblox settings | 671 |
| B5 | Blender 5.2 LTS Manual, FBX Legacy | undated; chk 2026-10-20; full page blocked | 676 |
| B8 | Blender 5.2 LTS Manual, Separate | undated; indexed excerpts | 692 |
| B9 | Blender 5.2 LTS Manual, Bisect | undated; indexed excerpts | 698 |
| R1 | Roblox Creator Hub, General Specifications | undated; chk 2026-10-20 | 711 |
| R2 | Roblox Creator Hub, Character Body Specifications | undated; chk 2026-10-20 | 716 |
| R3 | Roblox Creator Hub, Importer | undated; chk 2026-10-20; cited only in "R1-R3 review" | 721 |
| R6 | Roblox Creator Hub, Beyond the Dark Custom Characters | undated legacy case study; its 10,000-triangle and zero-influence statements conflict with current docs | 736 |
| R7 | Roblox Creator Hub, Rigging and Skinning | undated; chk 2026-10-20 | 741 |
| R8 | Roblox Creator Hub, Motor6D | undated; API reference; partly interactive page | 746 |
| R9 | Roblox Creator Hub, AnimationController | undated; example uses old LoadAnimation | 751 |
| R12 | Roblox Creator Hub, HumanoidRigDescription | undated; 22 description slots are not a universal exported-bone cap | 766 |
| T1 | Tripo Developers, Auto Rigging | undated live reference; model versions carry own dates; vendor quality claims stay vendor claims | 778 |
| T2 | Tripo Developers, Segmentation | undated; chk 2026-10-20 | 783 |
| T3 | Tripo Developers, Rig Check | undated; screening only, not a Studio quality check | 788 |
| T4 | Tripo Developers, Smart Segmentation | undated; chk 2026-10-20 | 793 |
| T5 | Tripo Developers, Changelog | entries headed 2026-10 and 2026-09; exact days not supplied | 798 |
| T6 | Tripo Developers, Retopology | undated; face counts and byte limits not interchangeable | 803 |
| A1 | Adobe, Mixamo Common Questions | last updated 2021-09-14; chk 2026-10-20 | 810 |
| A2 | Reallusion Magazine, Free vs CC Advanced AccuRIG | published 2025-06-30 | 815 |
| A3 | Reallusion Magazine, AccuRIG to Blender Pipeline | published 2022-11-11; vendor-hosted | 820 |
| A4 | Zhang et al., UniRig (arXiv) | first submitted 2025-04-16; research paper | 825 |
| A5 | Song et al., Puppeteer (arXiv) | first submitted 2025-08-14; research paper | 830 |
| A6 | Zhang et al., Skin Tokens (arXiv v2) | first submitted 2026-02-04; revised 2026-10-19; listed in ACM TOG 2026; abstract checked | 835 |
| E1 | StraySpark, AI Auto-Rigging Showdown 2026 | published 2026-05-14; first-party account; EXPERIENCE not a benchmark; promotes mesh tools | 840 |

## 11. Coverage map (check C1)

| Item | Where |
| --- | --- |
| Rules 01-15 | section 2 |
| Evidence contract + principle (RP:6-12) | section 1 |
| 1.1 | section 3.1 |
| 1.2 + table RP:62-67 | section 3.2 |
| 2.1, 2.2, 2.3 + table RP:101-107 | sections 4.1-4.3, numbers N01-N12 |
| 3 + template + region table + table RP:158-162 | section 5, 5.1 |
| 4a, 4b | sections 6.1, 6.2 |
| 4c decision table | section 6.3 |
| 4d + table facts | section 6.4, numbers N13-N26 |
| 4e | section 6.5 |
| Table RP:253-263 | numbers N13-N27, claims C31-C55, contradictions X02, X03, X07, X16 |
| Numbers with unit/source/tag (C2) | section 7 |
| Claims to check (C3) | section 8 |
| Contradictions and limits | section 9 |
