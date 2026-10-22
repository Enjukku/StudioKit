> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20. Revised by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (one root, the toolbox before code, no mesh rain).

# Build techniques per tool (what the vfx-design chooser picked → how to build it in Roblox)

Values: `pro-defaults.md`. Exact properties and limits: `knowledge/reference/vfx/roblox-vfx-api-card.md`. Meshes in depth: `knowledge/reference/vfx/mesh-vfx.md`. Tutorial recipes: `knowledge/reference/vfx/tutorials.md`.
Every technique: all layers under one root Attachment or Part, sizes and offsets from one scale factor (C-27). Use an emitter setting before writing code: a held image is Rate 0 and one `Emit` (or a long Lifetime with Speed 0); gravity is Acceleration plus Drag; a swirl or ring can be a simple mesh with a moving texture.

## T1. Particles (many small, soft or chaotic bits)
- One emitter per job; all burst at 0 ms with `EmitCount`; order by Lifetime and ZOffset (C-06). Streams only for flight, loops and auras.
- Particles are 2D images only. Many 3D meshes spawned like particles (falling candy, rubble rain) cost real Parts each: keep them to a few pooled hero pieces and make the many from flat sprites.
- Bodies (fire, smoke) are flipbooks; billboards (flare, impact, ring, glow) have Speed 0.
- Every emitter: LightInfluence 0, Brightness set, LightEmission 1 (glow, core) or 0 (smoke, sparks, dark).
- Clone, wait one frame, then `Emit` (ZO-04). Clean up with Debris after the longest lifetime.

## T2. Meshes (one big solid shape that keeps its form while it moves or grows)
- Model in Blender (Blender MCP), FBX, origin where it should scale or pivot (ring/dome centre, spike/pillar base, slash at the swing pivot), UVs 0-1, no vertex colours, under ~300 tris for small shapes.
- Animate with TweenService: Size (scales about the centre: move CFrame for a base pivot), CFrame (sweeps), Transparency (one value per part). Material Neon for glow.
- Not possible: texture scroll or dissolve on a MeshPart, soft edges, vertex wobble, screen distortion (Glass refraction exists but not on mobile). Workarounds: bake gradients into the texture alpha, rotate a streaked texture, stack 2-4 copies with staggered fade.
- Big moving shapes (wave, tornado): several mesh stages swapped at flash or cover moments, or a skinned mesh with bones (4 influences max). Always add particles on top for detail (spray, foam, dust) and a ground mark.
- Pros use meshes rarely for small effects: prefer particles for rings, slashes and streaks under ~10 studs.

## T3. Beams and trails (a line between two points, a ribbon behind something)
- Beam: Segments = keypoints − 1 when straight; more (≤~50) when curved. Semicircle: CurveSize = diameter × 2/3, rotate the attachments 90°. TextureSpeed differs per layer (1.3-3). Tween Width0/Width1 in and out; FaceCamera on unless it must lie flat.
- Trail: stack 2-4 on one attachment pair (soft, textured bright, outline); WidthScale tapers; Lifetime ~0.5 s; `Clear()` when disabling (api card).
- Sweeping arcs: put beams under one attachment and tween that attachment's CFrame (~175°, not 180°).

## T4. Object changes (an existing object changes: wall completes, building upgrades, freeze, charge)
- **Hide the swap in the flash:** white flash 0.03-0.05 s + glow; swap the old model for the new one on the flash peak frame (the eye cannot see the cut).
- Then the new object **pops**: scale 1.0 → ~1.08 → 1.0 in ~150-250 ms (ask the animator for the curve), a **shine sweep** (a thin bright beam or a Highlight fill tween crossing the object in ~300 ms), sparkle specs, a ground ring.
- Charge or state glow: Highlight (FillTransparency tween; ≤255 per client, delete when done), material or colour tween on the object, PointLight.
- Toy-block objects: real breaking is gameplay (block path). For a cosmetic change the effect may hide the real object for the moment and show its own copy or debris (T8), then restore it; it never edits the real object's data.

## T5. World events (rare, big, everyone sees it: tsunami, meteor shower, stage boss)
- Build from T2 (hero mesh) + T1 (detail) + ground marks; the hero silhouette must read at the farthest normal player distance (screen-size math in `plan-and-spec.md` §B).
- Budget allows more (it is rare) but phones still count: level of detail by distance (far players see the mesh + few particles), ≤1 such event at a time.
- One server event starts it; every client plays its own copy in sync (shared start time).
- Camera shake allowed (rare), distance-scaled; sound brief marks the big beats.

## T6. Cutscenes (camera is ours, plays once, nothing else on screen)
- Plan on one shared beat list with the animator and sound designer (one timeline in ms; feedback "crafts collaborate"). For cutscenes the film director's shot list (`<sequence>.shots.json`, `film-craft`) is that timeline: take shot ids, cue ids and times from it.
- Heavier assets are fine: more particles, big meshes, mesh flipbooks **only here** with load/unload around the shot (ZO-03); preload textures before the shot (ContentProvider:PreloadAsync).
- Effects are framed for the planned camera, not for all angles: frame scripts per shot.
- Keep flash safety and the reduced-motion option.

## T8. Fake destruction (cosmetic parts that look like damage)
- Allowed and expected: rock or block ring bursting out of the ground, crater rim, floor crumble (tiles drop and sink), flying chunks with trails, ground cracks, rubble that settles. Pros do it (TV6 debris parts with trails flung by AssemblyLinearVelocity; meteor craters).
- **Only the effect's own parts**, created on the client: `CanCollide` false (or a collision group that touches nothing gameplay), `CanQuery` false, `CanTouch` false, `CastShadow` off for small bits, `Anchored` for rings/craters (tweened), unanchored for flung chunks. Never edit, move, hide-forever or delete real map parts, players or gameplay objects.
- Look: our block style (studs, block palette, toy proportions) or rock in the stage material; sample the colour of the ground under the hit point (raycast `Instance.Color`/`Material`) so debris matches it.
- Motion recipes: **rock ring** = 8-16 wedges/rocks placed on a circle, rise from below the floor in 80-150 ms (Back Out), hold 0.6-1.5 s, sink 300-500 ms; **crumble** = grid pieces drop in a wave from the centre (stagger 20-40 ms), tilt, fade; **flung chunks** = 5-12 random sizes 0.5-2.5, random rotation, upward velocity 50-70 + outward 20-40, trail on each, fall and fade by ~1.5 s; **crater** = dark decal + raised rim rocks.
- Clean up with the Debris service after the longest piece; cap 30 parts per effect (low tier 10); pool for frequent effects.
- Pair with particles: dust at the base, sparks at contact, a ground decal for the mark.

## T7. Camera and screen channels
- Shake, FOV punch, hit-stop, post pulses: rules and values in vfx-design `camera-and-screen.md`; occasional only . Per-player post effects go under `workspace.CurrentCamera`.
