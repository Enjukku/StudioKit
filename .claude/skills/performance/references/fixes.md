> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Same sources as `measure.md`. "practice" = common practice not stated as a rule in the docs.

# Fixes by bottleneck

## Scripts (orange frames, `RunService.*`, `GC`)
- Event-driven over per-frame; one loop per system, not per object; spread long jobs over frames (e.g. ≤ 5 ms per frame); cap per-frame work. PO/design.md:57-65; PO/improve.md:19-45.
- `BindToRenderStep` only for work that must run after input and before render (camera). Set velocities in `PreSimulation`, read positions in `PostSimulation`; write `Motor6D.Transform` in `PreSimulation`. MP/task-scheduler.md:43-50.
- Disconnect connections; prune per-player tables on leave; avoid temporary tables in hot loops (GC). PO/improve.md:93-114; MP/tag-table.md:322.
- Parallel Luau: code inside `Actor`s runs in parallel only after `task.desynchronize()` or `ConnectParallel`; no instance writes until `task.synchronize()`; no `require` in the parallel phase; split work across many Actors by logic. Worth it when the server dashboard shows high CPU with few cores used. scripting/multithreading.md:41-338.
- Native code (`--!native`, `@native`): server scripts, number- and buffer-heavy Luau only (not API-call-heavy); type `Vector3` parameters; costs compile time and memory; compare in Script Profiler with and without. luau/native-code-gen.md:11-160.
- Concurrent calls batch automatically for `GetProductInfoAsync`, `UserOwnsGamePassAsync` and avatar item details: start them together with `task.spawn`. No data store call batches. scripting/transparent-batching.md:25-107.
- Many parts moving: `workspace:BulkMoveTo(parts, cframes, Enum.BulkMoveMode.FireCFrameChanged)`. _api-reference/classes/WorldRoot.yaml:123-156.
- Practice (not in docs): set properties before `Parent`; pool instances that are created and destroyed often (docs mention NPC pooling, PO/improve.md:275).

## Rendering (blue or red frames, `Perform`, `ShadowMapSystem`)
- Draw calls drop when meshes share the same mesh **and** the same texture or SurfaceAppearance (or same material): upload each mesh and texture once, reuse it, use Packages; do not import whole maps in one go. PO/improve.md:322-405.
- `RenderFidelity` Automatic or Performance, not Precise. PO/improve.md:375-379.
- Shadows: `CastShadow = false` on small, far, moving or transparent parts; `Light.Shadows` off where not needed; fewer, shorter-range lights. The engine turns shadows off below quality level 4. PO/improve.md:418-440.
- Transparency other than 0 or 1 overdraws; decals, textures, particles and beams batch poorly. PO/design.md:51-53.
- Textures: memory follows pixel count (1024² = 4 × 512²); most images ≤ 512², minor ones ≤ 256²; built-in materials and one tinted texture beat many custom textures. PO/improve.md:564-584.
- Particles: ≤ 400 particles/s per emitter (100 on mobile), lifetime capped at 20 s; size costs fill rate; avoid changing emitter properties at runtime. effects/particle-emitters.md:199-215.
- Static scenery far away: SLIM (`Model.LevelOfDetail = SLIM`; needs streaming, a published place and Team Create; static models only, no physics or raycasts on the merged copy). workspace/streaming/slim.md:43-251.

## Physics (`worldStep`, `stepContacts`)
- Anchor everything that need not move; fewer constraints; no ragdoll self-collision. PO/improve.md:170-181.
- `CollisionFidelity`: Box for small or non-interactive parts, Hull for small-medium shapes, PreciseConvexDecomposition only when needed (most CPU and memory). Big complex objects: invisible Box parts as collision. No collision needed: `CanCollide`, `CanTouch`, `CanQuery` false **and** Box. PO/improve.md:182-232.
- Sleeping parts cost nothing; any property change, impulse or constraint edit wakes them. physics/sleep-system.md.
- Network ownership: unanchored parts near a player are simulated by that client; frequent ownership flips cost. physics/network-ownership.md:13-19.
- Humanoids: disable unused states, `AnimationController` for static NPCs, animate NPCs on the client, spawn only near players. PO/improve.md:240-284.

## Memory
- Streaming is the biggest client memory lever; then smaller radii, fewer `Persistent` models, `Opportunistic` stream-out. PO/improve.md:547-560.
- Leaks: connections, per-player tables, characters (set `Workspace.PlayerCharacterDestroyBehavior` Enabled), animations kept after a model is destroyed (most common). PO/improve.md:93-139; PO/scene-analysis.md:59-67.
- Audio is memory-heavy; load only what is used. PO/improve.md:566.

## Network (`ProcessPackets`, `Data Senders`)
- Send deltas, only on change, throttled; chunk large trees; do VFX, view models and tweens on the client (server tweens replicate every frame). PO/improve.md:483-526.
- ReplicatedStorage downloads to every client at join: keep server-only and not-yet-needed content out; keep ReplicatedFirst tiny; `PreloadAsync` only the loading screen, key menu images and spawn area. PO/design.md:67; PO/improve.md:588-621.

## Streaming (what each needs and costs)
| Feature | Needs / costs | Source |
| --- | --- | --- |
| `StreamingEnabled` | client sees only streamed-in parts of Workspace: use `WaitForChild`, atomic models, server-side queries | workspace/streaming/index.md:18-80 |
| `ModelStreamingMode` Atomic / Persistent / PersistentPerPlayer | Atomic loads a model whole; Persistent never leaves memory (rare use) | index.md:196-244 |
| `ModelStreamingBehavior = Improved` | recommended | index.md:111 |
| Predictive streaming (`PredictiveStreamingMode = Enabled`) | pre-fetches spawn and return points; skipped on weak clients | index.md:165-194 |
| Frustum streaming (`Player.FrustumStreaming`, live 2026-09-29) | streams far objects in view; costs client memory; no occlusion | workspace/streaming/frustum.md; DF 4904553 |
| Extra replication foci | each ≈ one more player of server work; prefer `RequestStreamAroundAsync` for teleports | index.md:143-151 |

## UI and sound
- Fewer UI elements per ScreenGui; avoid frequent `Parent` or `ZIndex` changes (Z-order rebuild); do not tween `UIStroke.Thickness` on text; CanvasGroup saves render time at a memory cost; sprite sheets for many small images. MP/tag-table.md:183-455; PO/improve.md:584.
- Fewer active sounds; sounds parented to streamed parts stop when the part streams out. MP/tag-table.md:98-105; techniques.md:382.
