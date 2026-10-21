> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Facts: `knowledge/reference/film/fact-check-blender-images.md` (FB; Blender 5.1.2 probed headless 2026-10-21, probes in `knowledge/reference/film/probes/`, re-run with `powershell -File run_all.ps1 -Blender <path>`; 5.2 docs read as extracts). Method (O): N2 BL rows. The studio's Blender is **5.1.2**; the paper pins 5.2.2 LTS. Record the version that ran.

# Blender previs: a timed animatic that answers staging questions

Previs rebuilds only enough geometry, proxy acting and camera to answer the directing question (N3 PM-05). It must show that transitions and moves are coherent in space and time; a board can only suggest that.

## 1. Scene setup
- New file per sequence (or link the cast from a shared cast file; never save a shared file headless while the owner has it open, N4 R-12).
- Scale: the game's Blender-units-per-stud rule (`environment-craft` scale chain); place a player-sized reference and the smallest and tallest supported avatar heights.
- Proxies: landmarks the shots must show (exit, threat, goal), set walls, actor stand-ins with a facing marker. Real models replace proxies as they arrive.
- Rate: set from the shot list by the push script (`shotlist.py blender`): `fps = num`, `fps_base = den` (29.97 = 30000 / 1001.0; `fps` is an int 1-32767; a rounded base like 1.001 is inexact in Blender's 32-bit float) (FB FC-08, correction 5).
- Record in a manifest next to every review movie: Blender version (`bpy.app.version_string`), scene file and revision, output size, pixel aspect, fps and fps_base, frame range, colour management, camera ids, audio revision, shot-list revision (N2 BL-03; FB correction 12).

### Greybox light (J015 G2 gaps G14: three rebuilds)
- An emissive material does not cast light shadows like a lamp, and a point light inside an emissive proxy sphere is blocked by it: put the lamp outside or make the proxy non-occluding.
- Give emissive panels a black base colour, or the sun lights them too and they clip.
- Record the view transform (`Standard`, `AgX`) in the manifest; it changes every value judgement.
- Check value separation of the key subjects on key frames (`tools/art/look_check.py value`): mood lighting that hides the player, the threat or the exit fails the shot (lead review of the G2 test: the handoff shot read too dark).

## 2. Cameras
- One camera per shot named `CAM_<id>`; the push script binds the shot marker `shot:<id>` to it. A camera marker is active from its own frame; frames before the first camera marker use that marker's camera; unbound markers change nothing; read markers sorted by frame (FB correction 3).
- Separate controls for the path (the camera or its parent) and the interest point (an empty the camera tracks). `Track To` for cameras: track `-Z`, up `Y` (the defaults); the two axes must differ. Near straight above or below the target the roll becomes unstable (about 10° of roll per small orbit step in the probe); use `Damped Track` there when roll control is not needed (FB FC-04, correction 10; N2 BL-15..17).
- Animate the interest point when attention shifts; never let the target pass over the camera.
- F-curves: `Auto Clamped` handles prevent overshoot between keys but not speed changes; Linear keeps no speed continuity across keys. After authoring, measure the peak translation and rotation speed; no source gives a "good" speed (N2 BL-18..20; FB FC-05).
- Camera record per shot (goes into the shot list `lens` object and `fov_deg`): projection (perspective; orthographic only for deliberate layout views), pose, target, focal length, sensor size, sensor fit, output aspect, shift/crop, derived angles (N2 BL-13).

## 3. Lens → Roblox field of view
Roblox `Camera.FieldOfView` is the **vertical** angle in degrees (1-120); with `FieldOfViewMode = Vertical` it stays fixed and the horizontal angle follows the device aspect (FR FC-22..24). So the Roblox value is the vertical angle the Blender camera renders at the review aspect.

Pinhole maths (V, N2 BL-07..09; FB FC-11..13): for gate width `Sx`, height `Sy`, focal length `f` (mm): `H = 2·atan(Sx / 2f)`, `V = 2·atan(Sy / 2f)`; with display aspect `a = width / height`: `tan(H/2) = a·tan(V/2)`.

| Sensor fit | Which output side the sensor size sets | Vertical angle |
| --- | --- | --- |
| `HORIZONTAL` | the width | `V = 2·atan((s / a) / 2f)` |
| `VERTICAL` | the height | `V = 2·atan(s / 2f)` |
| `AUTO` | **the larger output side** (landscape: width; portrait: height) | landscape as HORIZONTAL; portrait as VERTICAL |

Probed, 50 mm lens, 36 mm sensor (FB sensor-fit table): HORIZONTAL 1920x1080 → 22.8952°, 1080x1920 → 65.2385°; AUTO 1920x1080 → 22.8952°, 1080x1920 → 39.5978°; VERTICAL → 26.9915° at both. **Trap:** `camera.data.angle_y` always returns `2·atan(sensor_height / 2f)` (26.9915° here) whatever the fit and resolution: never read it as the rendered vertical angle; use the table or the projection matrix (FB correction 2). `shotlist.py check` computes `V` from a lens object.

- Framing checks in Roblox use the narrowest supported display (portrait phones if the game supports them): with a fixed vertical angle a narrower screen loses width, so keep the subject, the gaze target and the interaction destination inside the narrowest frame (N2 RT-13).
- A focal length changes magnification; moving the camera changes perspective. Matching a close subject's size from farther back with a longer lens is a different shot (N2 BL-10; FB FC-13).

## 4. Timing and cuts
- Hard cuts inside one scene: camera-bound timeline markers (whole frames only). Assembling reviewed shot outputs with audio: the Video Sequencer (N2 BL-25, BL-26).
- The shot list is the timing truth: `shotlist.py blender` pushes markers and range; re-time in Blender; `blender-export` then `shotlist.py diff --write` takes the lengths back (`references/shot-list-format.md`).
- Time arithmetic: frame `k` with start `k0` at rate `r` is at `t = (k - k0) / r`; frames 1-31 rendered = 31 images = 31/30 s at 30 fps; use `[start, next-start)` (FB FC-15).
- Importing a movie strip sets the scene rate from the file by default: set `use_framerate` and `adjust_playback_rate` on purpose and log them (FB correction 11).
- To read which camera is live at a frame: `scene.frame_set(f)` then `scene.camera`, or a `render_post` handler; `render_pre` lags one frame at a cut (FB correction 4).

## 5. Review artifacts (cheapest that answers the question, N2 BL-36)
| Question | Artifact | How |
| --- | --- | --- |
| Intent, screen direction | boards / contact sheet | `references/storyboards.md` |
| Staging, cuts, occlusion, movement, timing | timed greybox animatic with temp sound | GUI (Blender MCP): `View > Render Playblast` (the same label in 5.1.2 and 5.2; `bpy.ops.render.opengl`, needs a GUI). Headless: `bpy.ops.render.render(animation=True)` with the Workbench engine; this is a render, not a playblast (FB corrections 7, 8) |
| Contrast, atmosphere | a few lit frames per beat | EEVEE or the game's look; judged again in Roblox |

- Movie output in 5.1.2: set `render.image_settings.media_type = 'VIDEO'` before `file_format = 'FFMPEG'` (otherwise a TypeError); re-probe on 5.2 before relying on it there (FB correction 6). Keep an image sequence when frame audit or resuming matters; encode the review movie separately (N2 BL-37).
- A/B versions: same rate, crop, display size and audio revision; change one directing decision at a time; watch silent, then with sound (N2 BL-38).
- The owner may direct timing on the animatic ("longer here, cut there"); record the decision and the revision (N4 A-01).

## 6. Camera export to Roblox
Every authored shot needs a pose in Roblox, static shots too. Until a conversion is proven, keep each shot's Blender pose in the shot list's `camera` field and label it "Blender axes, unconverted"; the generated Luau module carries `fovDeg` but no pose. Before the Roblox step, run the axis-and-landmark probe below and hand engineering the converted poses (J015 G2 gaps G5). Not built into the tool (J015-D7). For moving shots:
- Export **evaluated** poses per frame: `scene.frame_set(f)`, then `cam.evaluated_get(depsgraph).matrix_world`; raw `location` / `rotation_euler` are wrong under a parent or constraint (FB FC-06, correction 9).
- Write the conversion explicitly: units (Blender units per stud), basis change `R_roblox = Q · R_blender · Q⁻¹` plus a local correction `C` on the right when the cameras look down different local axes, origin offset, handedness (N2 BL-22, BL-23; FB FC-16; the Roblox side is not verified).
- Prove `Q` and `C` with an axis-and-landmark test scene (three coloured markers at known positions) captured in both tools before trusting any path.
- The data goes to engineering with the shot list; the director checks the capture against the animatic frame by frame at the cut points.
