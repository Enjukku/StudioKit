---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-20 (saved by orchestrator · claude-opus-5-5; the researcher had no write tool)

# Stylized mesh VFX: craft and Roblox translation
Labels: [DOC] Roblox Creator Docs mirror; [DATA] our training dumps; [PRACTICE] community or practitioner; [INF] inference, test in Studio. Web craft evidence was thin: no breakdown with hard numbers was found, so timings are [INF] starting points. Docs mirror root: `knowledge/external/roblox-creator-docs/` (D/). Blender MCP not used; no export test run.

## 0. Hard facts that decide everything
| Fact | Label | Source |
| --- | --- | --- |
| Texture is documented only for Parts and Unions (repeats; OffsetStudsU/V, StudsPerTileU/V tweenable). MeshPart is not listed as a parent | DOC | D/parts/textures-decals.md:11,52,142; D/_api-reference/classes/Texture.yaml:9-17,39-140 |
| MeshPart takes MeshId + TextureID; MeshId cannot be changed by script (CreateMeshPartAsync/ApplyMesh) | DOC | MeshPart.yaml:133-141 |
| MeshPart.DoubleSided renders both faces (card meshes) | DOC | MeshPart.yaml:26-32 |
| SpecialMesh/FileMesh: Scale, Offset, VertexColor (Vector3 TINT, not per-vertex alpha), TextureId | DOC | DataModelMesh.yaml:32,77,144-156 |
| Mesh limits: max 20,000 tris, one material per mesh, 256 px textures for ~5-stud objects | DOC | D/art/modeling/specifications.md:34-37; texture-specifications.md:25-30 |
| Imported per-vertex colour is flagged invalid; remove vertex colours | DOC | D/art/validation-errors.md:131 |
| SurfaceAppearance.AlphaMode Transparency: MeshPart.Transparency ≥0.02 switches to smooth-gradient blending, "does not support all effects" | DOC | SurfaceAppearance.yaml:47-57 |
| EditableMesh (SetUV, SetColorAlpha, SetPosition) is disabled in published games unless 13+, ID-verified and "Enable Mesh / Image APIs" on | DOC | EditableMesh.yaml:10-22 |
| Glass refraction is not supported on mobile | DOC | D/parts/materials.md:568 |
| Beam: TextureSpeed/TextureLength/FaceCamera/Segments; Trail: TextureMode Stretch/Wrap/Static | DOC | roblox-vfx-api-card.md:59-88 |
| Texture offset on MeshPart heads may have regressed in one release | PRACTICE, single-source, undated | devforum.roblox.com/tag/textures |

## 1. Mesh catalogue (ASIS = works as-is; WORK = workaround; NO = not possible)
| Mesh | Shape + modelling | UV / pivot | Animation (engine-agnostic) | Textures | Roblox translation | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| Shock ring | flat annulus, 24-48 segments, ~48-96 tris; optional upward flare | U around, V inner→outer; pivot at centre on the ground | XZ 0→1 ease-out ~250-350 ms, thickness shrinks, alpha holds then fades [INF] | soft radial gradient with alpha, or noise ring | ASIS: Neon MeshPart, tween Size + Transparency. Vertex-alpha softening NO: bake into texture alpha. Dissolve WORK (stepped copies). Particle alternative: VelocityPerpendicular, size 12-15 (TU-23) | superhivemarket VFX Mesh Generator docs; tutorials.md |
| Half dome / blast | hemisphere 12x8 (~190 tris), open bottom, or inverted-normal copy | U around, V base→apex; pivot base centre | 0→1 fast-out ~150-250 ms, fade ~200 ms; Fresnel rim in shader [INF] | gradient (bright rim, dark centre) | ASIS: Neon MeshPart size + transparency. Fresnel NO: fake with two shells (outer bright, inner dark). Refraction bubble WORK: Glass, not on mobile | superhivemarket docs |
| Crescent slash | curved tapered strip, 8-16 x 2-4 segments, ~60-100 tris | U along arc, V across; pivot at swing origin | rotate about pivot (~175°, TV4), life 0.2-0.3 s, hold then fade; UV erode in shader | gradient streak, bright leading edge | ASIS: MeshPart + TextureID, Neon, CFrame sweep tween. Scroll/erode NO: bake head-bright gradient, animate rotation + Transparency, or 2-3 copies with staggered fade. Layer with slash particles | tutorials.md; devforum "Animated Slashes 2.0" (2022-07-15) |
| Swirl / tornado | stacked open cylinders or helix strip, wide top, 12-16 x 4-8; ~100-300 tris | U around, V bottom→top; pivot base | continuous Y rotation, V scroll up, masked top/bottom, scale in then fade | streaky spiral alpha | WORK: rotate a mesh whose texture has spiral streaks to mimic scroll [INF]; bake the masks into alpha. Pair with wind particles (TU-21) | realtimevfx.com/t/fire-tornado-effect/25604 (2024-02) |
| Spike / cone | 6-8-sided cone, ~12-16 tris, or crystal | U around, V base→tip; pivot at BASE | Y 0→1 in ~80-120 ms with overshoot, hold 300-600, sink/fade ~200 [INF]; random tilt | flat colour or hard gradient | ASIS. MeshPart scales about its centre: offset CFrame by half height while scaling [INF] | [INF] |
| Cylinder beam / pillar | open tube 8-16 sides, glow core + wider shell | U around, V along | width 0→1 in ~50-80 ms, hold ~150, shrink + fade ~250 | vertical streaks | ASIS: Neon Cylinder Part, no mesh needed. Scroll WORK: Beam with TextureSpeed layered on it, or Texture OffsetStudsV tween on a flat Part [DOC] | tutorials.md; textures-decals.md:142 |
| Ribbon trail | strip, tapering | U along | samples path, fades per segment by age | streak gradient | ASIS substitute: Trail or Beam. Procedural mesh ribbon needs gated EditableMesh. Per-segment vertex-colour fade NO | realtimevfx slash-trail tool thread (single-source) |
| Ground crack | flat jagged plane or quad | planar; pivot impact centre | grow fast then stop, hold, fade; radial reveal in shader | dark crack alpha, bright core | ASIS: Decal/Texture on a thin Part. Radial reveal WORK: scale the part then tween Transparency. TV6 used particles | tutorials.md |
| Distortion bubble | sphere/ring, refraction material | pivot blast centre | scale up, fade | none | WORK: Glass MeshPart (not on mobile). Screen-space distortion NO | §3 |

## 2. Roblox mesh-VFX toolkit
| Property / technique | What it does | Limits | Doc |
| --- | --- | --- | --- |
| Material Neon | glow look on parts/meshes | reads best with Bloom; additive blending on meshes not documented; lowest quality in ViewportFrames | D/parts/materials.md:454 |
| Transparency tween | whole-mesh alpha fade | one value per part, no per-vertex alpha | MeshPart.yaml; SurfaceAppearance.yaml:47-57 |
| MeshPart.Size tween | scale-up/shrink (rings, domes, spikes) | scales about centre; offset CFrame for base pivot [INF] | MeshPart.yaml |
| MeshPart.TextureID | image on the mesh UVs | one material per mesh; keep UVs in 0-1 | texture-specifications.md:30 |
| SpecialMesh Scale / Offset / VertexColor | per-mesh scale tween (pros use it), tint | VertexColor is tint, not alpha | DataModelMesh.yaml |
| Texture on a Part: OffsetStudsU/V, StudsPerTileU/V | UV-scroll fake via TweenService | documented on Parts/Unions, not MeshPart; MeshPart behaviour untested | D/parts/textures-decals.md:140-162 |
| Decal / Texture Transparency | fade ground cracks, sprites | one value per decal | textures-decals.md:16 |
| DoubleSided | both faces of card meshes | framed for leaves/cloth; fine for rings/slashes [INF] | MeshPart.yaml:26-32 |
| Beam (TextureSpeed, Width tween) | scrolling ribbon | segment rules | api card |
| Trail | ribbon on an attachment pair | not hand-shaped | api card |
| Glass | refraction "distortion" | not on mobile | materials.md:568 |
| EditableMesh | runtime vertex/UV/alpha edits | gated; not for us now | EditableMesh.yaml |
| Stacked copies, staggered transparency | dissolve/erode fake | N copies = N parts; keep 2-4 [INF] | [INF] |

## 3. What pros in our training data do with meshes [DATA]
Scanned 30 study outlines (hidden 8 excluded). 16 contain MeshPart/SpecialMesh (75 lines), ~44 Texture-class lines in 13 files. Most hits are not VFX shapes: accessories, weapons, heads.
| Pattern | Where | Props | Reading |
| --- | --- | --- | --- |
| Neon Parts as emitter hosts | aTier__Ayato_Showcase 5/24 parts | Material 288, Transparency 1 | invisible hosts |
| Start/End Part pairs with Decal + SpecialMesh | Unknown__ProjectilePractice: 16 SpecialMesh, one MeshId, TextureId empty | Parts Transparency 1; Scale tweened ~0 → ~0.3-0.7 (negative in dump, meaning unverified) | grow-in pair for trail / ground hit |
| "Distortion" MeshPart | aTier__Ayato_Showcase (single) | Material 1568 (Glass), no texture, no collision/shadow | Glass mesh as distortion bubble |
| Meteor | Unknown__Meteor_VFX_Open_Source | imported rock MeshPart + shards | not an anime shape |
| VertexColor | all sampled SpecialMesh | always [1,1,1] | nobody uses the tint |
**Takeaway: pros make ring/slash/streak shapes with particle sprites and Beams; VFX-shaped meshes are rare in our sample.**

## 4. Timing and curve recipes (starting points; tune by eye; TV = tutorials.md, rest [INF])
| Effect | Scale / size | Transparency / colour | Notes |
| --- | --- | --- | --- |
| Shock ring | XZ 0→1 in 250-350 ms, Quad/Exponential Out | hold ~0.3 for ~40% of life, then →1 | particle ring alternative size 12-15 (TU-23) |
| Dome blast | 0→1 in 150-250 ms, Out | fade ~200 ms | dark second shell 30 ms later |
| Slash mesh | rotate 175° in 200-300 ms (TV4) | hold 0 then fade | dark twin under, bright thin over; no fade-in on impacts (TU-02) |
| Spike | 0→1 in 80-120 ms, Back Out, hold 300-600, sink 200 | none or fade last 100 ms | random tilt and height |
| Pillar / beam core | width 0→1 in 50-80 ms, hold ~150, shrink ~250 | alpha with shrink | TV4: widths tweened from 1.25x to 0 |
| Impact flash | 0.03-0.05 s (TU-12) | instant on | 0.1-0.2 s for the shape |
| Tornado | continuous rotate; fade in 150, out 250 ms | masked top/bottom | — |

## 5. Blender build notes for our pipeline
| Topic | Rule | Label |
| --- | --- | --- |
| Format | FBX; Apply Scalings = FBX Unit Scale; Add Leaf Bones off | DOC: D/art/modeling/export-requirements.md:34-44 |
| Import | Studio Importer; arrives as MeshPart | DOC: D/parts/meshes.md:40 |
| Scale | test with a 1-unit cube vs a 1-stud part first | INF, not verified |
| Origin | ring/dome at centre; spike/cone/pillar at base; slash at swing pivot; apply transforms | INF + DOC |
| Poly budget | docs max 20,000; target <~300 tris per VFX mesh | DOC + INF |
| UVs | one map, all in 0-1; U along/around, V across; texel margin against edge bleed | DOC + PRACTICE |
| Vertex colours | remove; bake gradients and alpha into the texture | DOC |
| Sides | cards: DoubleSided in Studio | DOC |
| Texture | 256x256 for small effects; PNG with alpha; check Neon + Transparency in Studio | DOC + INF |
| Animated meshes | skinned meshes supported (4 influences max); baked bone ribbon possible [INF] | DOC + PRACTICE |
| Shape kit | build once: ring, dome, crescent, cone, tube, tornado stack, crack plane | PRACTICE |

## 6. Sources
| Source | Date | Notes |
| --- | --- | --- |
| Local Creator Docs mirror (paths above) | undated mirror | primary Roblox truth |
| knowledge/reference/vfx/tutorials.md (TV1-TV6) | 2026-10-20 | owner-supplied practitioner videos |
| output/vfx/training-dumps (30 study outlines; per-game working output, optional, not shipped) | project data | §3 |
| devforum.roblox.com/t/how-to-make-animated-slashes-20/1880010 | 2022-07-15 | old, vague |
| realtimevfx.com/t/fire-tornado-effect/25604 | 2024-02 | Unreal, no numbers, single-source |
| superhivemarket.com/products/vfx-mesh-generator-pro/docs | fetched 2026-10-20 | product docs, no numbers |
| realtimevfx.com slash-trail tool thread (31306) | not retrieved | single-source |
| devforum.roblox.com/t/why-roblox-breaks-my-uvs/3916781 | not retrieved | single-source |
| devforum.roblox.com/t/texture-not-moving/479099 | older | Texture offsets tweened |
Gaps: no Riot / Genshin / 80.lv / Gabriel Aguiar breakdown with hard timing numbers found. Next Studio tests: (a) Texture OffsetStudsV on a MeshPart vs a flat Part; (b) Neon ring with Transparency 0.3 and an alpha texture.
