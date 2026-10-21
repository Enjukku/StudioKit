---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J007-T03, Modeler_Research_Paper.txt lines 712-912, 927-975
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Modeler paper part 3: environment and building models, export and import, hand-offs, review, end-to-end process (lines 712-912, 927-975)

Paraphrased notes. The paper (MP) stays outside git. Every row cites `MP:<line>`. Nothing is fact-checked yet: the paper's checkable claims are in "Claims to fact-check". The paper's cutoff and access date is 2026-10-21. Lines 913-926 are held out by the brief and are not in these notes.

## 0. How to read

| Key | Meaning |
| --- | --- |
| MP:n | line n of `Modeler_Research_Paper.txt`. One paragraph = one line. Source register = MP:976-1974 (resolved in "Source table"). |
| Tag | The paper's own tag: VERIFIED (a primary source states it; for vendors only what they document), EXPERIENCE (a named practitioner reports it), OPINION (the paper's proposal or inference; a source beside it is motivation, not proof), UNKNOWN (paper says unmeasured; stays UNKNOWN). Never upgraded here. Where one paper line mixes tags, it is split into one row per tag. A VERIFIED tag in the paper covers every sentence up to the next tag; where such a sentence is an inference, the row says so. |
| Src | paper source id (P00 = the paper's own proposal, no external source). "based on X" in the paper = X is the motivation. |
| Who | `[for-rigger] [for-animator] [for-art-director] [for-ui] [for-vfx] [for-environment] [for-owner]`: roles that must also know or act on the row. Empty = the modeler only. |
| Light | In the pass/fail table and the 22 steps: how the check can be done under the light-check rule (owner J005-D8, J007-D7). N = scripted number, I = image only if the number fails, R = part of the one review render set per hand-off, D = a decision or record, no measurement. Not in the paper; extractor suggestion. |
| Row IDs | ENV (§9), EXP (§10), TRI (import triage), HND (§11), REV (§12), CHK (checklist), PRC (22 steps), DNT (do not do), OPQ (open questions), RT (rule-table rows, shown with the section they close). |

Paper headings in these ranges and where they are covered (check C1):

| Paper heading | MP lines | Section here |
| --- | --- | --- |
| 9 Environment and building models | 712-716 | 1 |
| Design the assembled kit not only the pieces | 718-728 | 1 |
| (rule table, §9) | 730-735 | 1 |
| 10 Export and import | 737-751 | 2 |
| Import failure triage | 753-762 | 3 |
| (rule table, §10) | 764-771 | 3 |
| 11 Handoffs between the modeler and other studio agents | 773 | 4 |
| Art direction input | 775-781 | 4 |
| Rigger and animator output | 783-789 | 4 |
| VFX and UI output | 791-795 | 4 |
| Handoff record | 797-806 | 4 |
| (rule table, §11) | 808-812 | 4 |
| 12 Reviewing a model from data renders and the game | 814 | 5 |
| Review the evidence not the best screenshot | 816-822 | 5 |
| Pass or fail checklist | 824-846 | 6 |
| Review conversation and repair loop | 848-854 | 5 |
| (rule table, §12) | 856-861 | 5 |
| 13 End to end process for the AI modeler | 863 | 7 |
| Production sequence and gates | 865-912 | 7 |
| Do not do | 927-957 | 8 |
| Open questions and decisions the studio must supply | 959-967 | 9 |
| (closing rule table) | 969-974 | 9 |

---

## 1. §9 Environment and building models (MP:712-735)

| ID | MP | Lesson | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| ENV01 | 714 | Pick the project grid from avatar clearance and gameplay dimensions. A unit conversion from a source is not a universal wall-module size. | OPINION | P00 | [for-environment] |
| ENV02 | 714 | Build a small test assembly before the whole kit: straight wall, corner, door or window opening, floor/ceiling, trim, transition. | OPINION | P00 | [for-environment] |
| ENV03 | 714 | Define before production: anchor/origin convention, module dimensions, attachment axes, UV and trim alignment. | OPINION | P00 | [for-environment] |
| ENV04 | 714 | Judge assembled outside and inside corners, not isolated pieces. | OPINION | P00 | [for-environment] |
| ENV05 | 714 | Large structural masses carry silhouette and readability. Small repeatable trim carries detail. | OPINION | P00 | [for-art-director] [for-environment] |
| ENV06 | 714 | Break repetition with planned variants and dressing. Do not make every wall a unique mesh or texture. | OPINION | P00 | [for-environment] |
| ENV07 | 714 | Measure reuse cost with the platform rules of paper §8 (outside this range). Do not assume Blender linked duplicates stay shared runtime resources after import. | OPINION | P00 (motivation R13) | [for-environment] |
| ENV08 | 716 | Blender lets an origin be placed relative to geometry or the 3D cursor, so a snap anchor need not sit at the mesh center. | VERIFIED | B17 | |
| ENV09 | 716 | Use corner or base anchors for grid kits when useful. Keep meaningful hinge origins on moving parts. | OPINION | P00 | [for-environment] [for-rigger] |
| ENV10 | 716 | Check openings against the actual approved player and camera, not a generic height. | OPINION | P00 | [for-environment] |
| ENV11 | 716 | The Blender docs substantiate no single budget for a building, kit, texture or unique-mesh count. | OPINION | P00 (B17 context) | [for-owner] |
| ENV12 | 720 | Give each kit family an interface contract: dimensions, snap origin, forward and up axes, compatible neighbors, material/trim orientation, intended interior or exterior view. | OPINION | P00 | [for-environment] |
| ENV13 | 720 | The first test assembly includes wall ends, corners, height transitions, roof joins and openings. | OPINION | P00 | [for-environment] |
| ENV14 | 720 | Two failure examples: a wall that tiles in a row fails at a corner because its thickness or trim takes the neighbor's space. A roof slope fine alone leaves a gap against a different module. | OPINION | P00 | |
| ENV15 | 722 | Model to real player movement and camera clearance. The visible doorway arch, the collision opening and the camera path must agree with the use. | OPINION | P00 | [for-environment] |
| ENV16 | 722 | Decide first: playable interior, closed shell, camera cutaway, or destructible parts. That decides which backs and support surfaces must exist. Do not delete hidden faces only because the beauty camera cannot see them. | OPINION | P00 | [for-environment] |
| ENV17 | 724 | Keep structure readable before dressing: entrances, floors, supports, hazards and walkable space must be telling-apart at the game camera. | OPINION | P00 | [for-art-director] [for-environment] |
| ENV18 | 724 | Surface detail supports style and function. If the reference leans or sags, keep one consistent reason and usable mating interfaces. Rotating every module at random is not the same as authored distortion. | OPINION | P00 (motivation C09) | [for-art-director] |
| ENV19 | 726 | Make a variant only when it changes silhouette, function or recognizable story. Share one family where only color or surface differs. | OPINION | P00 | [for-environment] |
| ENV20 | 726 | Keep canonical assets separate from placed instances, so a kit fix spreads on purpose. | OPINION | P00 | [for-environment] |
| ENV21 | 726 | Test mirrored variants for texture direction, asymmetric props and collision. Mirroring is not free. | OPINION | P00 | |
| ENV22 | 728 | Review a populated scene with neighboring families together. A building with the right palette can still overpower characters by contrast or micro-detail. A prop good at icon distance can look noisy when repeated. (heavy review: see Contradictions X1) | OPINION | P00 | [for-art-director] [for-environment] |
| ENV23 | 728 | Approve a kit under the lighting, camera, crowd and streaming conditions of its real use, and keep that context for later asset reviews. (heavy review: X1) | OPINION | P00 | [for-environment] |

§9 rule table (MP:730-735):

| ID | MP | Rule | Number or limit | Tag | Src and date |
| --- | --- | --- | --- | --- | --- |
| RT9-1 | 731 | Grid and module dimensions | Project-defined, not a universal stud count | OPINION | P00; 2026-10-21 |
| RT9-2 | 732 | Origins support chosen snap anchors | Geometry center not compulsory | VERIFIED | B17; undated, accessed 2026-10-21 |
| RT9-3 | 733 | Validate corners, openings, transitions | Finish the first assembly before growing the kit | OPINION | P00; 2026-10-21 |
| RT9-4 | 734 | Keep gameplay geometry readable | No universal wall or door size | OPINION | P00; 2026-10-21 |
| RT9-5 | 735 | Runtime reuse needs resource identity | Blender duplication alone is no proof | OPINION | P00 based on R13; accessed 2026-10-21 |

---

## 2. §10 Export and import (MP:737-751)

Order of the paper's argument: units, then FBX settings, then axes, then the Roblox importer, then permissions, then reimport.

| ID | MP | Lesson | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| EXP01 | 739 | Roblox's standard physical length is 1 stud = 28 cm. Its physics engine does no internal unit conversion and allows any consistent alternative reading. | VERIFIED | B26 | |
| EXP02 | 739 | Roblox's Blender guide uses an authoring convention: Unit System None, Rotation Degrees. It recommends FBX Unit Scale with the other scaling values at 1.0. | VERIFIED | B24 | |
| EXP03 | 739 | Metric reading (EXP01) and numeric authoring/export conversion (EXP02) are two layers. Do not multiply both unless the chosen pipeline demands it. Keep a reference measuring object of known size and verify it after import. | OPINION | P00 | [for-environment] |
| EXP04 | 741 | Two alternatives exist: FBX export Scale 0.01, or scene Unit Scale 0.01. The second can cause camera and modifier trouble, and a reimport may need rescaling. | VERIFIED | B24 | |
| EXP05 | 741 | The two alternatives are not additive recipes. (Sentence sits under the B24 tag in the paper; it is an inference from EXP04.) | VERIFIED | B24 (span) | |
| EXP06 | 741 | glTF is documented as needing none of these extra FBX scale settings. (Under the B24 tag span.) | VERIFIED | B24 (span) | |
| EXP07 | 741 | The MeshScaleUnit enum documents source units Stud, Meter, CM, MM, Foot, Inch. The enum existing does not prove every importer UI shows every choice (second half sits under the B27 tag span). | VERIFIED | B27 (span) | |
| EXP08 | 741 | Record the importer path and the unit choice actually used. | OPINION | P00 | |
| EXP09 | 743 | Roblox's general FBX guide asks for: Path Mode Copy with embedded textures, FBX Unit Scale, Add Leaf Bones off, Bake Animation off unless animations are needed. | VERIFIED | B25 | [for-rigger] |
| EXP10 | 743 | Export only the selected approved geometry and armature. Leave out cameras, reference planes and high-poly bake sources. | OPINION | P00 | |
| EXP11 | 743 | Per asset category, check whether custom properties, cages, attachments or facial animation need extra export options. | OPINION | P00 | [for-rigger] [for-vfx] |
| EXP12 | 743 | A file that parses is not an asset that works. Inspect in Studio: proportions, normals, material channels, pivot positions, skin deformation, collision. | OPINION | P00 | |
| EXP13 | 743 | Re-importing the export into a clean Blender scene is a useful transport test. It does not replace Roblox validation. | OPINION | P00 | |
| EXP14 | 745 | Blender's Python FBX exporter defaults include -Z Forward and Y Up. These are defaults, not a promise of correct facing for every asset. | VERIFIED | B23 | |
| EXP15 | 745 | Write the coordinate assumptions in the manifest. Verify a known front arrow and up axis in import preview. Do not apply mesh or armature transforms after skinning just to fix a wrong axis. | OPINION | P00 | [for-rigger] |
| EXP16 | 745 | Embedding textures does not make a procedural Blender shader become the intended Roblox material. Bake or export the supported maps and check them. | OPINION | P00 | [for-art-director] |
| EXP17 | 747 | Studio File > Import accepts FBX, OBJ and glTF. FBX and glTF can carry hierarchies, PBR, rigs, animation, cages and vertex colors. (date: accessed 2026-10-21) | VERIFIED | R20 | |
| EXP18 | 747 | glTF import makes one Model per mesh node with MeshParts per primitive, so its hierarchy need not equal the FBX hierarchy. | VERIFIED | R20 | [for-rigger] |
| EXP19 | 747 | Importer exposes Scale Unit (default Studs), WorldForward and WorldUp, and Set Pivot to Scene Origin (default on). | VERIFIED | R20 | |
| EXP20 | 747 | Before import, inspect the preview: hierarchy, measured size, origin, transforms, normals, material bindings. | OPINION | P00 | |
| EXP21 | 747 | The default scene-origin pivot is not automatically the elbow or door hinge the rigger needs. Avoid Merge Meshes when parts move on their own. Keep the rig-requirements sheet in naming and in the real hierarchy, not names only. | OPINION | P00 | [for-rigger] [for-animator] |
| EXP22 | 749 | Asset privacy fully released 2026-05-05. New individual and group accounts default to restricted for newly created images, meshes and decals. Existing accounts and assets are not changed retroactively. An asset at Open Use cannot go back to Restricted under this release. | VERIFIED | R30, 2026-05-05 | [for-owner] |
| EXP23 | 749 | Put owner and experience-use permission in the manifest. A model showing for its uploader in Studio does not prove its dependencies load for live players. Do not make assets public to fix a permission error. Grant the intended experience or account scope. | OPINION | P00 | [for-owner] |
| EXP24 | 751 | Reimport (full release 2026-05-06) keeps instance properties and hierarchy, syncs changed meshes and textures, and adds new elements. It keeps the selected upload inventory, file path and import preset. CollisionFidelity and RenderFidelity are preserved after release fixes. | VERIFIED | R23, 2026-05-06 | |
| EXP25 | 751 | Auto-Reimport is still a Studio beta in the reviewed announcement (2026-09-08). It watches source files with saved Reimport settings. | VERIFIED | R24, 2026-09-08 | |
| EXP26 | 751 | Rig reimport treats a skeleton as one unit and deletes bones missing from the new file. WrapTargets may be replaced, which may break object references. The same source warns against reimport with ACE open (paper does not expand ACE). Source 2025-12-02, updated 2026-05-20. | VERIFIED | R33 | [for-rigger] [for-animator] |
| EXP27 | 751 | Keep versioned source and export backups. Close animation editing. Reimport in a test place. Compare rig and attachment IDs and collision before accepting. Non-destructive does not promise every instance ID survives. | OPINION | P00 | [for-rigger] [for-animator] [for-vfx] |

---

## 3. Import failure triage and §10 rule table (MP:753-771)

| ID | MP | Observation | Test and correction | Tag | Src |
| --- | --- | --- | --- | --- | --- |
| TRI01 | 756 | Wrong size or orientation | Compare Blender transform and unit data with importer Scale Unit, WorldForward/WorldUp and the calibration object. Change one conversion at a time. | OPINION | P00 based on R20-R22 |
| TRI02 | 757 | Texture lost or material wrong | Confirm the baked image files and map bindings, texture ownership, and SurfaceAppearance versus MaterialVariant precedence. Look at a render, not file names. | OPINION | P00 based on R07, R20, R30 |
| TRI03 | 758 | Bumps look like dents, or a map does nothing | Check the OpenGL tangent-space convention, the green channel and exported tangents. | VERIFIED | R11 (source-fit doubt: Claim F20) |
| TRI04 | 759 | Wrong pivot or fused moving parts | Review Set Pivot to Scene Origin and Merge Meshes. Restore the agreed separate hierarchy. | OPINION | P00 based on R20 |
| TRI05 | 760 | Fine in Studio, broken live | Check dependency permissions, beta-only features and device scaling. Do not assume geometry damage. | OPINION | P00 based on R24, R25, R30 |
| TRI06 | 761 | Looks damaged only at distance or under load | Check the real mesh-streaming mode and generated LoDs, not only source geometry or RenderFidelity. | OPINION | P00 based on R14, R16 |
| TRI07 | 762 | Reimport breaks rig links | Compare skeleton changes and replaced WrapTarget references. Rerun attachment and deformation checks. | OPINION | P00 based on R33 |

§10 rule table (MP:764-771):

| ID | MP | Rule | Number or limit | Tag | Src and date |
| --- | --- | --- | --- | --- | --- |
| RT10-1 | 765 | Standard physical length | 1 stud = 28 cm | VERIFIED | R22; undated, accessed 2026-10-21 |
| RT10-2 | 766 | Standard physical mass | 1 RMU = 21.952 kg | VERIFIED | R22; undated, accessed 2026-10-21 |
| RT10-3 | 767 | General FBX settings | Unit Scale; leaf bones off; bake animation only when needed | VERIFIED | R21; undated, accessed 2026-10-21 |
| RT10-4 | 768 | Importer default scale interpretation | Studs; verify explicitly | VERIFIED | R20; undated, accessed 2026-10-21 |
| RT10-5 | 769 | Reimport full release | 2026-05-06 | VERIFIED | R23 |
| RT10-6 | 770 | Auto-Reimport status | Studio beta, 2026-09-08 | VERIFIED | R24 |
| RT10-7 | 771 | Missing bone handling | Missing skeleton bones may be deleted | VERIFIED | R33; 2025-12-02, update 2026-05-20 |

---

## 4. §11 Hand-offs between the modeler and other agents (MP:773-812)

### 4.1 Art director (input to the modeler, and proposals back)

| ID | MP | Lesson | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| HND01 | 777 | The art director supplies an approved style guide, exemplars and banned departures. The guide must describe silhouette families, proportion language, value hierarchy, palette, material vocabulary, edge treatment, detail density, and how these change by asset role or view distance. "Stylized" alone is not a usable spec. | OPINION | P00 | [for-art-director] |
| HND02 | 777 | The modeler asks which treatment the game wants: planar low-poly, smooth exaggerated sculpt, hand-painted surface detail, physically based stylization, or a deliberate hybrid. | OPINION | P00 | [for-art-director] |
| HND03 | 779 | Record what is fixed and what may vary. A fixed palette does not force every object to use every color. A shared bevel language does not mean one world-space bevel width for a giant building and a hand tool. One reference model's triangle count is not a budget for later models. | OPINION | P00 | [for-art-director] |
| HND04 | 779 | Keep the design system, and propose an exception when readability, deformation or material behavior needs one. | OPINION | P00 | [for-art-director] |
| HND05 | 781 | Return proposals as comparable alternatives with one clear reason. Example: a separate shoulder plate keeps the approved silhouette in the required overhead pose, the fused version cuts into the torso. Show both at the same camera and pose. | OPINION | P00 | [for-art-director] [for-owner] |
| HND06 | 781 | Never use an unmeasured performance claim as the reason for an art change. The owner picks product priorities. The modeler supplies evidence, costs and alternatives. | OPINION | P00 | [for-owner] |

### 4.2 Rigger and animator

| ID | MP | Lesson | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| HND07 | 785 | The modeler hands the rigger: approved rest pose, units, dimensions, object transforms, origins, intended deformation zones, material slots, topology notes, semantic part list, attachment points, agreed range of motion, model version, and any baked high-to-low relationship. The rigger must not have to guess if a floating plate is armor, a leftover modeling object or a missing weld. | OPINION | P00 | [for-rigger] |
| HND08 | 787 | The animator supplies the stress poses: maximum limb flexion, twist, jaw open, wing fold, tool grip, seated pose, recoil, camera-visible close-ups as they apply. The rigger tests whether topology and construction support them. | OPINION | P00 | [for-animator] [for-rigger] |
| HND09 | 787 | The modeler fixes mesh problems instead of leaving the rigger to hide them with extreme weights. A rig defect is not fixed by bending correct rest geometry without checking the real cause. | OPINION | P00 | [for-rigger] |
| HND10 | 789 | Keep render geometry, deformation structure, collision geometry and attachment data apart. They may share a design but not a topology. Example: a detailed weapon can use a much simpler collision proxy. An emitter attaches to a named socket, not a vertex index. A detached rigid accessory can follow a joint without each surface becoming its own gameplay object. | OPINION | P00 | [for-rigger] [for-vfx] |

### 4.3 VFX and UI

| ID | MP | Lesson | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| HND11 | 793 | VFX gets semantic attachment points with orientation: muzzle, blade edge, impact surface, exhaust, eye, magic focus, foot contact. Say which coordinate frame and model revision define each. Give emission direction, expected movement, and whether the point exists in rest pose or must follow a bone. | OPINION | P00 | [for-vfx] |
| HND12 | 793 | Never make a VFX agent recover direction from a plausible but undocumented object origin. | OPINION | P00 | [for-vfx] |
| HND13 | 795 | UI icons need: a stable presentation camera, lighting setup, material state, and a transparent or color background requirement. | OPINION | P00 | [for-ui] |
| HND14 | 795 | The icon shows the shipped model, not a concept render that promises missing features. A close-up may show detail that does not matter in the world view. If that detail is wanted, model and texture it on purpose or approve an icon-only treatment. Do not change the world asset by accident. | OPINION | P00 | [for-ui] [for-art-director] |

### 4.4 Hand-off record (MP:797-806) with brief fields

Brief fields = keys of the studio brief (`rules/messages.md` §2): intent, id, from, to, model, effort, skills, refs, fixed, open, avoid, owns, not_in_scope, rules, deliver, checks, return. The last column is the extractor's mapping, not the paper's.

| ID | MP | Recipient | Required artifact | Failure it catches | Tag | Src | Brief fields the receiver needs (extractor) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HND15 | 800 | Art director | Reference revision, comparison renders, proposed exceptions | Style or silhouette drift | OPINION | P00 | refs (approved reference image + revision), fixed (art-bible locks), checks (identity, proportions), deliver (comparison set path) |
| HND16 | 801 | Rigger | Rest mesh, units, semantic parts, joints, deformation requirements | Unriggable topology; missing articulation | OPINION | P00 | refs (mesh file + requirements sheet), fixed (units, model version, range of motion), rules (rig-quality rules), skills, checks, deliver |
| HND17 | 802 | Animator | Approved pose tests, contact and grip requirements | Motion that shows seams or intersections | OPINION | P00 | refs (pose set), fixed (contacts, grip points), checks (pose pass table) |
| HND18 | 803 | VFX agent | Named attachment frames and model revision | Misaligned or detached effects | OPINION | P00 | fixed (attachment names, parent frame, direction, revision), refs (manifest path) |
| HND19 | 804 | UI agent | Shipped-model icon camera and material state | Icon and gameplay asset mismatch | OPINION | P00 | fixed (camera, light, material state, background), refs (render set path), deliver |
| HND20 | 805 | Performance owner | Asset metrics and representative scene results | A lone asset passes while the scene fails | OPINION | P00 | fixed (project budget from owner), checks (scene results), refs (metric record). Not one of the six receivers named by the owner; kept for completeness. |
| HND21 | 806 | Creative director (owner) | Short alternatives with evidence, plus open decisions | Unapproved design changes | OPINION | P00 | intent, open (decisions needed), the digest format; every pass names its evidence |

### 4.5 Receiver view for the six agreed receivers (extractor-compiled from the rows above)

| Receiver | What the modeler must give | Rows |
| --- | --- | --- |
| rigger | rest mesh, units, dimensions, transforms, origins, deformation zones, material slots, topology notes, semantic parts, attachments, range of motion, model version, bake link; the rig-requirements sheet in names and in hierarchy; coordinate assumptions | HND07, HND09, HND10, HND16, EXP15, EXP21, ENV09 |
| animator | pose-test results, contact and grip requirements; the animator in turn gives stress poses | HND08, HND17 |
| art director | reference revision, comparison renders at matched camera and pose, proposed exceptions; art director gives style guide, exemplars, banned departures | HND01-HND06, HND15 |
| environment designer (places models in levels) | no row in the paper for this receiver (Contradictions X9). Derived from §9: kit interface contract (dimensions, snap origin, axes, neighbors, trim orientation, view), anchors, variants vs family, canonical vs placed, interior/shell/cutaway/destructible decision, opening sizes vs player and camera, mirrored-variant test, import parity and calibration object | ENV02-ENV04, ENV09-ENV16, ENV19-ENV23, EXP03, EXP20 |
| VFX (attach points) | named attachment frames with position, orientation, parent frame, model revision, emission direction, movement, rest-pose or bone-follow | HND10-HND12, HND18 |
| UI (icon renders) | stable icon camera, light, material state, background; icon of the shipped model | HND13, HND14, HND19 |

### 4.6 §11 rule table (MP:808-812)

| ID | MP | Rule | Number or limit | Tag | Src and date |
| --- | --- | --- | --- | --- | --- |
| RT11-1 | 809 | Version every accepted asset hand-off | No universal naming schema | OPINION | P00; 2026-10-21 |
| RT11-2 | 810 | Define semantic attachment frames | Position plus orientation and parent frame | OPINION | P00; 2026-10-21 |
| RT11-3 | 811 | Validate required motion before final delivery | Pose set is asset-specific | OPINION | P00; 2026-10-21 |
| RT11-4 | 812 | Keep owner decision authority | Final artistic and product decision stays with the owner | OPINION | Studio brief and P00; 2026-10-21 |

---

## 5. §12 Reviewing a model (MP:814-822, 848-861)

| ID | MP | Lesson | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| REV01 | 818 | Review at the intended player camera and at diagnostic cameras. A close beauty render shows defects but rewards detail the game never shows. A far shot proves readability but hides flipped faces and bad UVs. Use: the approved reference, a neutral inspection render, material views, motion tests where relevant, and Roblox screenshots from the real target scene. (heavy review: X1) | OPINION | P00 | [for-art-director] |
| REV02 | 820 | Sort defects before ranking them. Identity: wrong silhouette, proportions, palette, signature feature. Construction: disconnected parts, unintended internal faces, wrong normals, non-manifold areas where a closed surface is needed, accidental duplicates, unapplied transforms that break interchange. Motion: collapsed joints, exposed cuts, grip problems, intersections in required poses. Runtime: unsuitable collision, excess asset cost, unreadable materials, data missing after import. | OPINION | P00 | |
| REV03 | 820 | Fix the highest-impact defect first, not the one easiest to see in a close-up. | OPINION | P00 | |
| REV04 | 822 | Merge by Distance merges vertices inside a threshold. | VERIFIED | B19 | |
| REV05 | 822 | One global cleanup distance can close eyelids, merge clothing into the body or fuse intended gaps. | OPINION | P00 | [for-rigger] |
| REV06 | 822 | The cleanup tools each target specific problems (loose, degenerate, non-planar, holes), not all geometry quality. | VERIFIED | B20 | |
| REV07 | 822 | Diagnose each issue, keep before/after reports, never fill every open boundary. A cloth sheet or an intentionally removed hidden back differs from a hole that animation exposes. | OPINION | P00 | [for-rigger] |
| REV08 | 850 | A useful review names an observable defect, its consequence and the next comparison needed. "Make it better" is not testable. Example form: the silhouette merges axe head and forearm at the combat camera; compare a shorter grip and a wider head offset. Do not prescribe a topology operation before finding whether geometry, camera or material is the cause. | OPINION | P00 | [for-art-director] |
| REV09 | 852 | After a fix, rerun every check it could break. Retopology can change UVs, deformation and bake match. An atlas can change material grouping and mip behavior. Separating a limb can change pivots, collision and rigging. An export setting can change scale or normals. Record dependencies so a local repair does not skip checks. | OPINION | P00 | [for-rigger] |
| REV10 | 854 | The owner gets short decision evidence, not a log dump: the failed criterion, before/after images at matched cameras, revised metrics, open tradeoffs, recommended action. Keep the full machine-readable report for the downstream agent. (heavy review: X1) | OPINION | P00 | [for-owner] |
| REV11 | 854 | Art direction is judgment informed by measurement. It is not replaced by a numeric score with invented weights. | OPINION | P00 | [for-art-director] [for-owner] |

§12 rule table (MP:856-861):

| ID | MP | Rule | Number or limit | Tag | Src and date |
| --- | --- | --- | --- | --- | --- |
| RT12-1 | 857 | Use gameplay and diagnostic views | No universal camera count | OPINION | P00; 2026-10-21 |
| RT12-2 | 858 | Require evidence for a pass | UNKNOWN is not a pass | OPINION | P00; 2026-10-21 |
| RT12-3 | 859 | Recheck dependencies after repair | Scope follows the changed property | OPINION | P00; 2026-10-21 |
| RT12-4 | 860 | Compare matched before and after views | No arbitrary quality score | OPINION | P00; 2026-10-21 |
| RT12-5 | 861 | Separate artistic approval from technical compliance | Both required for release | OPINION | P00; 2026-10-21 |

---

## 6. Pass/fail checklist (MP:824-846)

Rules for the table (MP:826, OPINION P00): every row is a proposed studio gate, not a claim that any outside studio uses it. A pass needs stored evidence. UNKNOWN is not a pass. A numeric threshold that was not chosen must not be silently replaced by a convenient default. An approved exception names who approved it and why the asset's intended use still works. No threshold numbers are given for any row (Contradictions X4).

| ID | MP | Check | Pass evidence | Fail condition | Tag | Src | Light (extractor) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CHK01 | 829 | Approved reference | Exact approved image and revision attached | Modeled from an unapproved or mismatched image | OPINION | P00 | D: image id + hash recorded |
| CHK02 | 830 | Identity and silhouette | Recognizable from the intended gameplay cameras | Signature form lost, weak or hidden | OPINION | P00 | R (silhouette set); N only if a silhouette overlap number is chosen |
| CHK03 | 831 | Proportions | Landmarks match the approved design or an approved exception | Drift hidden by a different camera or pose | OPINION | P00 | N (landmark ratios from the mesh); I on fail |
| CHK04 | 832 | Scale | Player and known-size comparisons agree | Right-looking asset imports at wrong size | OPINION | P00 | N (bounding box in studs vs expected) |
| CHK05 | 833 | Part inventory | Required visible and functional parts accounted for | Extra, missing or unclear parts | OPINION | P00 | N (object list vs manifest) |
| CHK06 | 834 | Connectivity | Intended connected and separate regions verified | Accidental floating or fused geometry | OPINION | P00 | N (loose-part count vs expected) |
| CHK07 | 835 | Surface orientation | Relevant sides render correctly | Flipped normals or unwanted backface loss | OPINION | P00 | N (flipped-face count); I on fail |
| CHK08 | 836 | Intersections | None that break visible motion or intended construction | Hidden overlap becomes visible in play | OPINION | P00 | N (self-intersection count in pose set); I on fail |
| CHK09 | 837 | Deformation | Required pose tests pass | Collapse, stretching, exposed cuts, impossible grip | OPINION | P00 | R (pose set); I on fail |
| CHK10 | 838 | UV mapping | Seams and density inspected at shipped texture size | Stretching, wrong islands, obvious seams | OPINION | P00 | N (texel density, stretch value); I on fail |
| CHK11 | 839 | Materials | Intended material response survives Roblox lighting | Baked highlight fights lighting, or maps import wrong | OPINION | P00 | R (one in-Studio render); N for map presence |
| CHK12 | 840 | Mesh and texture metrics | Recorded against current import limits and project budget | Ceiling exceeded, or budget unmeasured | OPINION | P00 | N (triangles, texture size, material count) |
| CHK13 | 841 | Collision | Gameplay paths and contacts pass with the chosen proxy | Unexpected blocking, gaps, instability, wasted detail | OPINION | P00 | N (scripted path/contact test in Studio); I on fail |
| CHK14 | 842 | Reuse and hierarchy | Deliberate shared assets, meaningful names | Accidental duplicate resources or fragile hierarchy | OPINION | P00 | N (unique mesh/material counts, name pattern) |
| CHK15 | 843 | Import parity | Dimensions, orientation, parts and look compared | Blender result differs materially after import | OPINION | P00 | N (dimension and part-count diff); R (one matched pair) |
| CHK16 | 844 | Phone performance | Representative scene and device record meets the project target | Desktop result used in place of phone evidence | OPINION | P00 | N (frame time, memory); no device = not verified |
| CHK17 | 845 | Cleanup | Temporary objects and obsolete exports excluded | Debug or hidden construction geometry ships | OPINION | P00 | N (exported object list vs manifest) |
| CHK18 | 846 | Provenance | Image, generator version, source assets and licenses recorded | Unclear rights or an asset revision that cannot be reproduced | OPINION | P00 | D |

---

## 7. §13 End-to-end process: 22 steps (MP:863-912)

Preface (MP:867, OPINION P00): the 22 steps are the proposed studio method, not a claim that any studio uses these gates or that a generated model was tested. Technical limits are sourced in earlier sections. The "check" column is the stop condition the paper's step text implies; the paper gives no separate check column. Light = extractor suggestion (see section 0).

| Step | MP | What | Check | Tag | Src | Who | Light |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 869 | Parse the brief: category, role, player camera, style, motion, interactions, target devices, owner. Record missing decisions before choosing geometry. Reject conflicting requirements only with an explanation and alternatives. | No silent substitution of another design; missing decisions listed | OPINION | P00 | [for-owner] | D |
| 2 | 871 | Collect approved style references and record image and asset provenance. Separate the wanted shape language from another game's protected character identity. | Provenance recorded; result is an original asset in the studio style, not a copy | OPINION | P00 | [for-art-director] | D |
| 3 | 873 | Write the ChatGPT reference prompt from the fixed style block and the right template (character, creature, prop, building). State view purpose, pose, palette, material intent, separate functional parts, forbidden artifacts. | A prompt request is not a promise of consistent views | OPINION | P00 | [for-art-director] | D |
| 4 | 875 | Generate and inspect the reference: part count, symmetry, proportions, view agreement, hidden geometry, material reading, image readability. Repair the image or get a decision on ambiguity before modeling. Keep the accepted revision, not only the latest. | Accepted image revision stored | OPINION | P00 | [for-art-director] | R (reference review); D |
| 5 | 877 | Obtain reference approval: art director checks style and readability, rigger and animator check motion needs, owner approves direction. | A tool's ability to generate a model does not skip this gate | OPINION | P00 | [for-art-director] [for-rigger] [for-animator] [for-owner] | D |
| 6 | 879 | Choose the construction route. Prefer hand modeling when controllable topology, modularity, mechanical precision or simple stylized form is efficient. Consider Tripo when generation may give useful complex form or surface detail. Compare expected cleanup and redesign cost, not only generation speed. | No hero-quality promise from the generator alone | OPINION | P00 | | D |
| 7 | 881 | Set scene units and asset coordinates: a player-scale reference, intended origin and orientation, the authoring-to-Roblox unit relation. | A simple import tests the unit relation before a scale error is copied across a kit | OPINION | P00 | [for-environment] | N (calibration object size after import) |
| 8 | 883 | Build or generate a blockout. Hand: large controllable primitives and modifiers. Tripo: inspect the raw output before accepting its part structure. Render all required sides and compare primary forms. | A textured look is not proof that the shape exists | OPINION | P00 | | R (blockout sides; heavy: X1); N (dimensions) |
| 9 | 885 | Review the primary design: silhouette, proportions, scale, functional layout. Freeze the approved blockout revision. Record deviations from the image needed for animation or gameplay and get the right approval. | Frozen revision id; deviations logged and approved | OPINION | P00 | [for-art-director] [for-owner] | R; D |
| 10 | 887 | Plan articulation with the rigger and animator: continuous skin, separate rigid parts or a hybrid, by required motion. Place and test joints or pivots on paper before finishing surfaces. Decide where cuts and overlaps stay hidden through motion, not only in rest pose. | Joint plan agreed with rigger and animator | OPINION | P00 | [for-rigger] [for-animator] | D |
| 11 | 889 | Build secondary forms and controlled detail. Keep the large shape hierarchy. Use bevels, normals and surface detail for the expected camera. Spend no geometry on forms that change neither silhouette, deformation nor material response. | Detail justified by silhouette, deformation or material | OPINION | P00 | [for-art-director] | N (triangles); R |
| 12 | 891 | Clean topology and surfaces: connected components, duplicates, normals, degenerate faces, internal geometry, deformation zones. Retopologize where useful structure matters. Decimate only where the errors are acceptable. | A triangle count does not prove animation readiness | OPINION | P00 | [for-rigger] | N (components, duplicates, degenerate faces, flipped faces) |
| 13 | 893 | Create UVs and materials: hand-painted, physically based or hybrid, as the style contract says. Spend texture detail by visibility and importance. Judge seams and texture at the real uploaded and rendered size, not the high-resolution paint file. | Seams checked at shipped size | OPINION | P00 | [for-art-director] | N (texel density); I on fail |
| 14 | 895 | Bake or transfer surface data where needed. Keep a high-quality source and a known low-resolution target. Inspect projection errors, missed cavities, skewed detail, normal-map conventions. | A successful bake operation is not a visual pass | OPINION | P00 | | N (bake error metric if chosen); I on fail |
| 15 | 897 | Build collisions and attachments. Choose collision complexity for gameplay function, not visual fidelity alone. Give named VFX and tool attachment frames. Test moving parts, interiors and player passage at the intended scale. | Passage and contact tested at real scale | OPINION | P00 | [for-vfx] [for-environment] | N (scripted passage test) |
| 16 | 899 | Optimize against the scene budget. Record triangles, mesh instances, unique assets, texture sizes, material use, collision choices. Measure representative populations. | Do not replace a missing budget with an upload ceiling or another game's spec | OPINION | P00 | [for-owner] | N |
| 17 | 901 | Render and compare again: matched reference views, neutral diagnostic views, silhouette checks, game-context lighting. Recheck approved landmarks after cleanup, decimation and baking. | Landmarks still match after destructive steps | OPINION | P00 | [for-art-director] | N (landmark ratios); R (heavy: X1) |
| 18 | 903 | Export a deliberate artifact set: only required objects, supported transforms and materials. Record exporter version and settings. Keep an editable source file and a versioned export. | Sole accepted asset not overwritten | OPINION | P00 | | N (exported list vs manifest) |
| 19 | 905 | Import and inspect in Roblox: dimensions, orientation, hierarchy, surface appearance, deformation where it applies, collisions. Treat importer warnings as evidence to resolve. Compare with the approved Blender render. | Warnings resolved or explained; parity with Blender | OPINION | P00 | [for-rigger] | N; R (one matched pair) |
| 20 | 907 | Test in the real target scene: target phones, representative asset populations, lighting, effects, streaming, player cameras. Record frame-time behavior and memory with the platform profiling tools. | A solo asset preview is not enough for a crowded scene | OPINION | P00 | [for-environment] [for-owner] | N (frame time, memory); no device = not verified |
| 21 | 909 | Final review and hand-off: complete the pass/fail checklist, attach the metric record and open exceptions, give downstream agents semantic parts and attachment data. | Owner accepts the artistic result; technical acceptance follows recorded project criteria | OPINION | P00 | [for-rigger] [for-animator] [for-vfx] [for-ui] [for-owner] | R (one review render set per hand-off) |
| 22 | 911 | Keep lineage: approved reference, model source, generation task or version if used, cleanup notes, export settings, imported asset IDs, benchmark record. | A later agent can tell the shipped asset from a similar rejected revision | OPINION | P00 | | D |

---

## 8. "Do not do" list (MP:927-957)

| ID | MP | Do not | Tag | Src (motivation) | Who |
| --- | --- | --- | --- | --- | --- |
| DNT01 | 929 | Assume a generated reference is geometrically consistent. | OPINION | P00; limits I02, I06 | [for-art-director] |
| DNT02 | 931 | Replace a turnaround collage with the documented Tripo multi-view inputs. | OPINION | P00; input contract T04, T29 | |
| DNT03 | 933 | Treat a maximum-detail Tripo result as an approved phone asset. | OPINION | P00; ceilings T01, R01 | [for-owner] |
| DNT04 | 935 | Equate quads, semantic segmentation or a successful auto-rig with proven deformation quality. | OPINION | P00; B07, T11, T25 | [for-rigger] |
| DNT05 | 937 | Cut every moving limb just because it needs animation. | OPINION | P00; supported construction B28, B29 | [for-rigger] [for-animator] |
| DNT06 | 939 | Weld every nearby vertex, or fill every open boundary, without distinction. | OPINION | P00; B19, B20 | |
| DNT07 | 941 | Stack scale conversions, or copy legacy defaults, without a calibration import. | OPINION | P00; conflict B22, B23, B24 | |
| DNT08 | 943 | Use an old four-option collision list, or unconditional legacy LOD distances. | VERIFIED | R08, R14 | |
| DNT09 | 945 | Promise 8K runtime display, or 4K residency on every phone. | VERIFIED | R03, R04 | [for-art-director] |
| DNT10 | 947 | Treat an atlas or a Blender linked duplicate as proof of one Roblox draw call. | OPINION | P00; batching conditions R13 | [for-environment] |
| DNT11 | 949 | Fix every dark imported material by auto-brightening its texture. | OPINION | P00; unresolved report R36 | [for-art-director] |
| DNT12 | 951 | Make assets public as an automatic fix for experience permission failures. | OPINION | P00; R30 | [for-owner] |
| DNT13 | 953 | Copy Dota slot limits or film complexity into universal Roblox budgets. | OPINION | P00; scoped examples C06, C09 | [for-owner] |
| DNT14 | 955 | Present a vendor workflow demo, a small review or an older-model research benchmark as a measured success rate for this studio. | OPINION | P00; T20-T26 | [for-owner] |
| DNT15 | 957 | Claim a script, export or importer success log proves visual or runtime acceptance. | OPINION | P00 | |

---

## 9. Open questions and closing rule table (MP:959-974)

| ID | MP | Open item | Tag | Src | Who |
| --- | --- | --- | --- | --- | --- |
| OPQ01 | 961 | Studio decisions that no generic doc can give: minimum supported phones, expected scene populations, gameplay camera ranges, performance targets, project budgets, art exemplars, final approval tolerances. They stay UNKNOWN until supplied and tested. The agent may propose values with reasons, labelled provisional, and must not say Roblox or an industry studio endorsed them. | OPINION | P00 | [for-owner] |
| OPQ02 | 963 | How a chosen Tripo model performs on this studio's image style is unmeasured until representative inputs are generated and reviewed. Product docs give supported controls and limits, not a quality ranking by character, vehicle or building. Keep a local evaluation set of approved references and record cleanup effort, topology fitness and in-game result if the route is evaluated. | OPINION | P00 | [for-owner] |
| OPQ03 | 965 | How far an AI reference may differ from a buildable asset must be explicit. Some images have contradictory geometry or painted shading that cannot exist as one object. The modeler proposes a coherent reading and shows the change. It must not silently correct a signature feature, and must not ask the rigger to animate impossible construction. | OPINION | P00 | [for-art-director] [for-rigger] [for-owner] |
| OPQ04 | 967 | Source disagreements are resolved only for the product, version and asset scope in the paper. Later releases can change the answer. Store the checked date and recheck the official page when a tool or importer changes. | OPINION | P00 | |

Closing rule table (MP:969-974):

| ID | MP | Rule | Number or limit | Tag | Src and date |
| --- | --- | --- | --- | --- | --- |
| RTC-1 | 970 | Reference image comes before construction | Required for every asset by this brief | OPINION | Studio brief and P00; 2026-10-21 |
| RTC-2 | 971 | Hand and generated branches share the final gates | No automatic hero-quality exemption | OPINION | P00; 2026-10-21 |
| RTC-3 | 972 | Test the imported asset in its scene | Device and population must be recorded | OPINION | P00; 2026-10-21 |
| RTC-4 | 973 | Keep asset lineage | Reference, source, export and runtime revisions | OPINION | P00; 2026-10-21 |
| RTC-5 | 974 | Unknown numeric budget stays unknown | A project proposal is not a sourced fact | OPINION | P00; 2026-10-21 |

---

## 10. Claims to fact-check

Domain: Roblox, Blender, Tripo, other. Claim = what the paper says, paraphrased. "Src" = paper source id. Notes after a dash are the extractor's doubts.

| No | MP | Domain | Claim | Src |
| --- | --- | --- | --- | --- |
| F01 | 716 | Blender | An object origin can be placed relative to geometry or the 3D cursor, so it need not be at the mesh center. | B17 |
| F02 | 739, 765 | Roblox | Standard physical length: 1 stud = 28 cm. | B26 (line 739), R22 (line 765; same URL) |
| F03 | 739 | Roblox | The physics engine does no internal unit conversion and allows consistent alternative interpretations. | B26 |
| F04 | 766 | Roblox | Standard physical mass: 1 RMU = 21.952 kg. Arithmetic check: 0.28^3 m^3 x 1000 kg/m^3 = 21.952 kg, so it fits water density; the page itself must confirm. | R22 |
| F05 | 739 | Roblox / Blender | Roblox's Blender guide: Unit System None, Rotation Degrees; FBX Unit Scale with other scaling values 1.0. | B24 |
| F06 | 741 | Roblox / Blender | The guide gives two alternatives: export Scale 0.01 or scene Unit Scale 0.01; the latter can cause camera and modifier problems and reimport may need rescaling. | B24 |
| F07 | 741 | Roblox | glTF import needs none of the extra FBX scale settings. | B24 |
| F08 | 741 | Roblox | MeshScaleUnit documents the source units Stud, Meter, CM, MM, Foot, Inch. | B27 |
| F09 | 743, 767 | Roblox / Blender | General FBX settings: Path Mode Copy with embedded textures; FBX Unit Scale; Add Leaf Bones off; Bake Animation off unless needed. | B25 (line 743), R21 (line 767; same URL) |
| F10 | 745 | Blender | Blender's Python FBX exporter defaults include -Z Forward and Y Up. | B23 |
| F11 | 941 | Blender | The paper says scale defaults in the legacy FBX manual (B22), the Python API (B23) and Roblox's guide (B24) conflict. Register quotes: B22 names a default of 10; B23 shows global_scale=1.0; B24 uses 0.01 alternatives. Which sources apply to which exporter (legacy vs current) is not stated. | B22, B23, B24 |
| F12 | 747 | Roblox | Studio import accepts FBX, OBJ, glTF; FBX and glTF can carry hierarchies, PBR, rigs, animation, cages, vertex colors. | R20 |
| F13 | 747 | Roblox | glTF import creates a Model per mesh node with MeshParts per primitive. | R20 |
| F14 | 747 | Roblox | Importer exposes Scale Unit (default Studs), WorldForward/WorldUp, Set Pivot to Scene Origin (default on). | R20 |
| F15 | 749 | Roblox | Asset privacy release 2026-05-05: new accounts default to restricted for new images, meshes, decals; existing assets unchanged; Open Use cannot return to Restricted. | R30 |
| F16 | 751 | Roblox | Reimport (full release 2026-05-06) preserves instance properties and hierarchy, syncs changed meshes and textures, adds new elements, keeps upload inventory, file path and import preset. | R23 |
| F17 | 751 | Roblox | CollisionFidelity and RenderFidelity are preserved on reimport after release fixes. | R23 |
| F18 | 751, 770 | Roblox | Auto-Reimport is a Studio beta (announcement 2026-09-08) that watches source files with saved settings. Status on 2026-10-21 may have changed. | R24 |
| F19 | 751, 771 | Roblox | Rig reimport treats the skeleton as a unit and deletes bones missing from the new file; WrapTargets may be replaced; the source warns against reimport with ACE open. | R33 |
| F20 | 758 | Roblox | Bump-turns-into-dent is explained by the OpenGL tangent-space convention, the green channel and tangents. Source-fit doubt: R11 in the register is the MaterialVariant API page, whose quote is about MaterialService descendants. | R11 |
| F21 | 757 | Roblox | A SurfaceAppearance versus MaterialVariant precedence exists and can hide a baked texture. | R07, R20, R30 (paper "based on"); R11 relevant |
| F22 | 761 | Roblox | With mesh streaming on, RenderFidelity is ignored and generated cloud LoDs decide distant look; a production incident (rolled back, report 2026-09) stuck meshes at the lowest LoD. | R14, R16 |
| F23 | 714, 735, 947 | Roblox | Meshes with the same mesh content can share one draw call under conditions; Blender linked duplicates and atlases do not by themselves prove one draw call. | R13 |
| F24 | 822 | Blender | Merge by Distance merges vertices within a threshold. | B19 |
| F25 | 822 | Blender | Mesh cleanup tools target specific problems (loose, degenerate, non-planar, holes). | B20 |
| F26 | 931 | Tripo | Tripo's multi-view input contract: H series v3 needs at least 2 images; a P-series model P2-20260801 exists on the multi-view API. | T04, T29 |
| F27 | 933 | Tripo / Roblox | Tripo H3.1 model card (v3.1-20260211 default) sets detail ceilings, and Roblox specs set mesh limits, so a maximum-detail result is not a phone-ready asset. The paper does not state the numbers here. | T01, R01 (via B31) |
| F28 | 935 | Blender / Tripo | Automatic remesh tools do not generally give deformation-friendly topology (B07); Tripo mesh segmentation API is model v2.0-20260430 Beta (T11); a quad-mesh review says face type alone says nothing about pole placement (T25). | B07, T11, T25 |
| F29 | 937 | Roblox | Roblox documents rigged meshes made in third-party tools (B28) and says multi-mesh models need extra rig steps (B29); so not every limb must be cut. | B28, B29 |
| F30 | 943 | Roblox | The old four-option collision list is outdated: a Tunable precision option with a CollisionPrecision slider exists (post 2026-09-17), and legacy LOD distances are not unconditional. | R08, R14 |
| F31 | 945 | Roblox | 4K textures reached published experiences 2026-01-30; texture streaming 2025-12-12; low-end Android under 3.5 GB has 4K disabled. The paper concludes 8K display and universal 4K are not promised; no register row states an 8K limit. | R03, R04 |
| F32 | 949 | Roblox | A report (2026-10-19) says ColorMaps look slightly darker than MeshPart.TextureID; unresolved. | R36 |
| F33 | 953 | other | Dota 2 Workshop Axe page gives a LoD0 triangle limit of 2500 (item-specific); a film press kit names lean, sag and twist principles. Both are scoped examples. | C06, C09 |
| F34 | 955 | Tripo / other | T20 is a vendor blog (2026-10-14), T25 and T26 are small reviews, T21-T24 are arXiv papers (T23 uses GPT-4o agents); none is a success rate for this studio. | T20-T26 |
| F35 | 929 | other | An image-generation model may struggle with visual consistency and may give approximate counts. | I02, I06 |
| F36 | 745 | Blender / Roblox | Applying mesh or armature transforms after skinning is a bad way to fix a wrong axis. (Paper offers no source.) | P00 |
| F37 | 747 | Roblox | Merge Meshes on import fuses parts that must move independently; scene-origin pivot is not the hinge. (Paper offers no source beyond R20.) | P00 (R20) |

---

## 11. Contradictions and gaps

| No | Where | Issue |
| --- | --- | --- |
| X1 | MP:728, 781, 818, 854, step 8 (883), step 17 (901), step 20 (907), REV01, REV10, CHK02, CHK09, CHK11 | Heavy visual review conflicts with the studio light-check rule (owner J005-D8, J007-D7: scripted numbers for every check, images only when a number fails, plus one review render set per hand-off). The paper asks for: gameplay cameras plus diagnostic cameras, neutral render, material views, motion tests, Roblox screenshots from the real scene, "render all required sides", matched before/after images at every fix, same-camera same-pose alternatives, populated-scene reviews with neighboring families and crowd. The paper itself says there is no universal camera count (MP:857). Resolution for the lead: take the numeric rows as the default check; one review render set per hand-off; extra images only for a failed number. Matched before/after renders only when a number failed. |
| X2 | MP:844, 907 | The pass rule needs a phone record, and "UNKNOWN is not a pass" (MP:826, 858). If no phone is available the row can only be "not verified". Scripted numbers from Studio (frame time, memory) fit the light rule; the target-phone requirement itself does not. |
| X3 | MP:899, 961, 974 vs owner J007-D5 | The paper says the project budget is UNKNOWN and warns against using the upload ceiling as a budget. The owner has now fixed: 20,000 triangles per mesh is only the Roblox upload ceiling; creatures and characters stay under about 7,000. That owner decision fills the open field for creatures and characters only. No owner number exists for props, weapons, vehicles, buildings or environment pieces, texture sizes, material counts or scene populations: still open. |
| X4 | MP:826-846 | The checklist has no numeric thresholds. The paper forbids choosing one silently. The lead must obtain each threshold from the owner or label it provisional (OPQ01). Candidate numbers that the light-check rule needs: flipped-face count, loose-part count, intersection count, texel-density range, bounding-box tolerance, import-parity tolerance, frame time. |
| X5 | MP:739-745, 941 | No single studs-per-Blender-unit number or a single default export recipe is given. B26 (physical layer) and B24 (authoring layer) are kept apart on purpose; EXP02 (FBX Unit Scale) and EXP04 (export Scale 0.01) are both presented as valid. Which recipe the studio uses is a decision. B22, B23, B24 are said to conflict (F11) but the resolution is not in this range. Environment-craft needs one chosen scale chain plus a calibration object. |
| X6 | MP:758 | TRI03 cites R11 as VERIFIED, but R11 in the register is the MaterialVariant API page; the tangent-space statement may belong to another source. Fact-check F20. |
| X7 | MP:743, 767, 739, 765, 1688, 1848, 1856 | Register ids share URLs: R21 = B25, R22 = B26, R01 = B31 (the register says "see B25/B26/B31 for the shared excerpt"). The paper cites the same fact under both ids in different places (F02, F09). Not an error, but a counting trap. |
| X8 | MP:877 vs studio gates | The paper's reference approval (step 5) lists art director, rigger/animator, owner. The studio's owner gates are Gate 1 brief, Gate 2 first samples, Gate 3 final look. The paper does not map its steps 5, 9, 21 to those gates. The lead must map them (suggestion, not in the paper: step 5 = Gate 1 or the reference check inside it; step 9 or the first model look = Gate 2; step 21 = Gate 3). |
| X9 | MP:797-806 | The hand-off record has no row for the environment designer, the receiver that places models in levels. It has rows for a performance owner and the creative director, which are not among the owner's six receivers. The environment hand-off must come from §9 (section 4.5). |
| X10 | MP:809 | The paper gives no naming schema or hand-off file format. The studio's message format (`rules/messages.md`) gives the fields; the file names are a studio decision. |
| X11 | MP:741, 745, 751 | Some VERIFIED tags cover sentences that are inferences (EXP05, EXP07 second half, EXP06 span). Treat as the paper's grouping, not as separate verified facts. |
| X12 | MP:760 | TRI05 cites R25 (Scene Analysis page: its statistics may not match what players see on their devices) as motivation for "device scaling". That is a loose link: the page quote speaks of in-view statistics, not of device scaling. A fact-checker should confirm. |
| X13 | MP:751, 770 | Auto-Reimport status (beta, 2026-09-08) and the "ACE" term are not explained; a recheck is due before the skill relies on it (OPQ04). |
| X14 | MP:879, 963 | The paper gives no rule for choosing Tripo vs hand modeling beyond "compare cleanup and redesign cost" and an unmeasured Tripo result on the studio's style (OPQ02). A local evaluation set is suggested, not run. |
| X15 | MP:871-875 | The paper stresses a ChatGPT reference but gives no consistency fix beyond "inspect and repair" (DNT01); the multi-view requirement for Tripo (DNT02, F26) means a turnaround collage is not a valid input. The step from one reference to documented multi-view images is not described in this range. |
| X16 | MP:867 | Step 13 and 14 (UV, bake) rely on technical detail from earlier paper sections outside this range; nothing in the 22 steps gives a bake or UV number. |

---

## 12. Source table (ids used by rows above)

All "undated, accessed 2026-10-21" sources are live pages without a publication date (paper rule, MP:978). Evidence tag is the paper's own. Quotes are short locator excerpts from the register.

| Id | Title | Date | Tag | URL | Locator quote |
| --- | --- | --- | --- | --- | --- |
| P00 | Proposed studio method | 2026-10-21 | OPINION | none (the paper's own synthesis, not a measurement) | - |
| B07 | Blender: Remeshing and retopology | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/id/5.2/modeling/meshes/retopology.html | "The automatic remesh tools generally don't result in topology that lends itself to deformation." |
| B17 | Blender: Object origin | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/en/latest/scene_layout/object/origin.html | "assuming the mesh has a uniform density" |
| B19 | Blender: Merge mesh | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/en/5.2/modeling/meshes/editing/mesh/merge.html | "Vertices closer than this distance will be merged." |
| B20 | Blender: Clean up mesh | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/cleanup.html | "These operators can automatically clean up certain types of messy geometry." |
| B22 | Blender: FBX legacy manual | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/en/5.2/files/import_export/fbx_legacy.html | "10 is the default" (cut) |
| B23 | Blender: FBX export Python API | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/api/5.2/bpy.ops.export_scene.html | "global_scale=1.0" |
| B24 | Roblox: Blender guide | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/blender | "This is the recommended way to export .fbx files at the same scale." |
| B25 | Roblox: general export settings | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/export-requirements | "Under the Armature section, disable Add Leaf Bones." |
| B26 | Roblox: units | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/physics/units | "Internally, the Roblox physics engine does not use unit conversions." |
| B27 | Roblox: MeshScaleUnit enum | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/reference/engine/enums/MeshScaleUnit | "Treats the source mesh as authored in Roblox studs" (cut) |
| B28 | Roblox: rigging a simple mesh | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/rig-a-simple-mesh | "create a rigged mesh using a third party modeling tool" (cut) |
| B29 | Roblox: humanoid mesh rigging | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model | "Models made up of multiple meshes require additional steps to rig" |
| B31 | Roblox: general model specifications (shared source of R01) | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/specifications | "A vertex can not be influenced by more than 4 bones or joints." |
| C06 | Dota 2 Workshop: Technical Requirements, Axe | undated living guide, accessed 2026-10-21 | VERIFIED | https://www.dota2.com/workshop/requirements/axe?l=english | "LoD0 Triangle Limit: 2500" |
| C09 | Luca official production notes (press kit) | 2021 (file revision 2021-06-04) | EXPERIENCE | https://lumiere-a.akamaihd.net/v1/documents/luca_press_kit_final_06-04-21_9b5cc33b.pdf | "lean, sag and twist" (cut) |
| I02 | OpenAI: image generation guide | undated, accessed 2026-10-21 | VERIFIED | https://developers.openai.com/api/docs/guides/image-generation | "the model may occasionally struggle to maintain visual consistency" |
| I06 | OpenAI: images and vision guide | undated, accessed 2026-10-21 | VERIFIED | https://developers.openai.com/api/docs/guides/images-vision | "The model may give approximate counts for objects in images." |
| R01 | Roblox: general specifications (same page as B31) | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/specifications | see B31 |
| R03 | Roblox DevForum: 4K Texture Rendering | 2026-01-30 | VERIFIED | https://devforum.roblox.com/t/4k-texture-rendering/4316229 | "4k Textures are now available in published experiences!" |
| R04 | Roblox DevForum: Introducing Texture Streaming | 2025-12-12; platform status updated 2026-03-23 | VERIFIED | https://devforum.roblox.com/t/introducing-texture-streaming/4144855 | "Low-end Android [< 3.5GB] [4k textures disabled]" |
| R07 | Roblox: Meshes | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/parts/meshes | "PreciseConvexDecomposition" (cut) |
| R08 | Roblox DevForum: Collision Geometry Workflow Improvements (tunable precision) | 2026-09-17 | VERIFIED | https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198 | "Tunable exposes a CollisionPrecision slider" |
| R11 | Roblox: MaterialVariant API | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/reference/engine/classes/MaterialVariant | "MaterialVariant objects only work as descendants of MaterialService." |
| R13 | Roblox: Improve performance | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/improve | "multiple meshes with the same MeshContent are handled in a single draw call" |
| R14 | Roblox DevForum: Mesh Streaming and Improved Cloud LoDs, opt-in phase | 2026-04-27 | VERIFIED | https://devforum.roblox.com/t/introducing-mesh-streaming-and-improved-cloud-lods-in-published-experiences-opt-in-phase/4601232 | "The MeshPart.RenderFidelity property across all your MeshPart instances will be ignored" |
| R16 | Roblox DevForum: mesh streaming low-LoD production incident | 2026-09; fix report 2026-09-04 | EXPERIENCE | https://devforum.roblox.com/t/meshstreamingandimprovedlods-persistently-stuck-at-lowest-lod-level-for-all-meshes/4835534 | "The feature rolled back today" |
| R20 | Roblox: Importer | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/studio/importer | "Scale Unit" |
| R21 | Roblox: export settings (same page as B25) | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/export-requirements | see B25 |
| R22 | Roblox: units (same page as B26) | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/physics/units | see B26 |
| R23 | Roblox DevForum: Full Release, Reimport | 2026-05-06 | VERIFIED | https://devforum.roblox.com/t/full-release-reimport/4622567 | "CollisionFidelity and RenderFidelity are now preserved on reimport" |
| R24 | Roblox DevForum: Studio Beta, Auto Reimport | 2026-09-08 | VERIFIED | https://devforum.roblox.com/t/studio-beta-auto-reimport-automatically-reimport-external-files-on-changes/4859863/1 | "automatically reimports it whenever that file changes on disk" |
| R30 | Roblox DevForum: Full Release, privacy for newly created image, mesh, decal assets | 2026-05-05 | VERIFIED | https://devforum.roblox.com/t/full-release-privacy-for-newly-created-image-mesh-and-decal-assets/4620416 | "If an asset is set to Open Use, it cannot be set to Restricted." |
| R33 | Roblox DevForum: Reimport rig and cage limitations | 2025-12-02; full-release update 2026-05-20 | VERIFIED | https://devforum.roblox.com/t/reimport-beta-update-rigs-avatars-bones-joints-cages-dynamic-heads/4112031 | "it will delete bones that are missing." |
| R36 | Roblox DevForum: SurfaceAppearance rendering differences report | 2026-10-19 | EXPERIENCE | https://devforum.roblox.com/t/appearance-issues-with-surfaceappearance/4944376 | "ColorMaps appear slightly darker than MeshPart.TextureID" |
| T01 | Tripo: H3.1 model card | undated live docs, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/models/v3-1 | "v3.1-20260211 Default" |
| T04 | Tripo: multiview to 3D model, H series v3 | undated live docs, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/generation-multiview-to-model/standard | "at least 2 images are required" |
| T11 | Tripo: mesh segmentation API | undated live docs, model v2.0-20260430, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/mesh-segment | "v2.0-20260430 Beta" |
| T20 | Tripo blog: game character workflow using P2.0 | 2026-10-14 (official blog index) | EXPERIENCE | https://www.tripo3d.ai/blog/mesh-game-character-p-2 | "None of this removes the character artist from the process." |
| T21 | arXiv: Nexus, native mesh generation with diffusion | 2026-07-15 v1 | VERIFIED | https://arxiv.org/html/2607.13563v1 | "our approach ignores the face normals" |
| T22 | arXiv: ViSculpt, visual-centric agentic geometry editing | 2026-08-25 v1 | VERIFIED | https://arxiv.org/html/2608.24169v1 | "We curate 20 geometry-editing tasks" |
| T23 | arXiv: EZBlender, 3D editing with plan and ReAct agent | 2026-01-12 v1 | VERIFIED | https://arxiv.org/html/2601.07143v1 | "all agents use GPT-4o as the LLM backend" |
| T24 | arXiv: UltraTex, 2K multi-view diffusion for 3D texturing | 2026-09-19 v1 | VERIFIED | https://arxiv.org/html/2609.23169v1 | "Background Token Dropping" |
| T25 | Digital Production: Tripo P2.0 quad mesh review | 2026-09-29 | EXPERIENCE | https://digitalproduction.com/2026/09/29/tripo-p2-0-put-quad-mesh-generation-to-the-test/ | "Face type alone says nothing about pole placement" |
| T26 | GLBGPT review: Tripo H3.1 Standard vs Detailed, three inputs | 2026-09-10 | EXPERIENCE | https://www.glbgpt.com/hub/nl/tripo-h3-1-review-2/ | "Both modes missed important held-out underside and rear structure" |
| T29 | Tripo: P series multiview API | undated live docs, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/generation-multiview-to-model/p | "P2-20260801" |
| R25 | Roblox: Scene Analysis | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/scene-analysis | "The statistics in this view don't necessarily match what players see on their devices." |
