> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-craft`. Facts: `knowledge/reference/animation/fact-check-techniques.md` (TC, RT<q>-<n>, SD; mirror revision 7400643, read 2026-10-21), `fact-check-roblox-runtime.md` (RA). Measurement method and floor devices: `performance` skill (`references/budgets.md`, `measure.md`). Paper: AP:705, AP:835-870 (no public phone budget exists). Revised by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§3).

# Ambient loops and many copies

## 1. The rule
Cost per copy × copies on screen decides the technique, and **no documented per-copy cost exists** for a Tween, an Animator track, a Motor6D, a Bone, a flipbook or a PivotTo write (SD01; the paper found no public phone budget either, AP:705). So: pick the cheapest technique that reads, then measure it at the peak count on the floor phone before it is built a hundred times. Without a phone the result is BLOCKED.

## 2. Technique per decoration
| Decoration | First choice | Why | Fallback / far view |
| --- | --- | --- | --- |
| Grass, clouds, particles | `Workspace.GlobalWind` | wind moves terrain grass, clouds and particles (particles need WindAffectsDrag and Drag > 0) only (TC19, RT6-01) | — |
| Flags, banners, cloth | short looped clip on a few bones (skinned) on a client Animator, or a code sway of a rigid flag | bones deform one mesh, no collision change (TC11); client Animator tracks do not replicate, which is wanted (TC10) | a static flag or flipbook billboard far away; skinned copies near the camera are the first thing to measure (TC26, SD02: the "not instanced" warning is undated) |
| Windmills, water wheels, fans | constant-speed rotation in one client loop for all copies (`PivotTo` or `Motor6D.Transform` in PreSimulation) | one loop per system (TC08); constant speed has no ease inside the loop | slow or stop off screen if measured useful |
| Trees, plants, hanging signs | a gentle sway: code (identical for all, cheap) or a local hinge (reacts to players) | GlobalWind does not move parts or meshes (TC19) | static far away |
| Water, lava, belts | `Texture` offset scroll | cheapest surface motion, no rig (TC16) | — |
| Fire, torches, glow | flipbook particle (≤ 8×8 frames, ≤ 30 fps) | may be switched off on low-memory phones: the object must read without it (TC17) | a static emissive part |
| Crowds of cosmetic NPCs | client Animator, shared clips, LOD variants | documented choice for crowds (RA02, RA42); keep identity and major contacts in LOD clips | proxies or fewer bones far away, measured |

## 3. Variation without noise
- Copies must not move in step: a phase offset or a small speed range per copy (seeded by position so it is stable across sessions). Identical repeats lose punch fastest in the first few (an inference from one paper).
- Variation comes from a cause (wind strength, the object's size, its stiffness), not free randomness.
- Keep it calm: ambient motion must never pull the eye from gameplay (`animation-design` §6): slower and smaller than anything near a sightline, partly hidden where possible, and no fast motion in the play space. The art-director judges where the eye goes.
- Vary only what decorates (phase, speed, amplitude, which variant plays); lock what means something (a hazard's period, a pickup's pulse rate, any timing the player reads).
- The sway follows the object's own gesture: a plant bends along its curve, a banner from its pole; a sway that fights the shape reads as noise.
- Offer a still or slow variant for players who reduce motion (the player setting exists and grass honours it, TC29; the variant is a design choice).

## 4. Streaming, LOD, throttling
- Animated models get no SLIM or far LOD stand-in: they pop in at the streaming radius; keep the far view acceptable with a static stand-in if it matters (TC20).
- Client-set motion on server-made models is lost on stream-out; restart on stream-in at a believable phase, not frame 0 for every copy at once (TC23).
- Many copies = many small streamed models with low part counts and one shared mesh asset id (TC21, TC24).
- The engine throttles remote animation evaluation itself (`Workspace.ClientAnimatorThrottling`, `Animator.PreferLodEnabled`); code that adds offsets on top reads `EvaluationThrottled` (TC22, RA24). Whether a client-created decoration Animator is throttled, and at what distance, is undocumented (SD03): measure.

## 5. The measurement (SD01, adapted)
1. One decoration built with each candidate technique; N = 100, 300, 1,000 copies in the representative scene.
2. On the floor phone (`performance` skill `references/budgets.md`): frame time p95, MicroProfiler scopes `Render/PreRender/TweenService`, `stepAnimation`, `physicsStepped`, `Perform/Scene/UpdateView`; Dev Console memory (Animation, Instances, PhysicsParts, GraphicsTexture); draw calls.
3. 3+ runs, spread reported; one change at a time; the same capture recipe before and after (`performance-engineer` owns the recipe).
4. Record the per-copy result as a game budget in the game profile (an owner decision), never as a kit number.
