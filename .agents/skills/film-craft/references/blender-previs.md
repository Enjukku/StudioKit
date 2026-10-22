> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Facts: `knowledge/reference/film/fact-check-blender-images.md` (FB; Blender 5.1.2 probed headless 2026-10-21, probes in `knowledge/reference/film/probes/`, re-run with `powershell -File run_all.ps1 -Blender <path>`; 5.2 docs read as extracts). Method (O): N2 BL rows. The studio's Blender is **5.1.2**; the paper pins 5.2.2 LTS. Record the version that ran. Revised by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§7 options, blocking, masks and value strip; §1 greybox light check now runs as review line B-06). Repair 3: the flash count script removed; §7 now says how to export the frames for the studio's counter in `vfx-craft/references/measure.md` §6.

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
- Check value separation of the key subjects on key frames (`tools/art/look_check.py value`): mood lighting that hides the player, the threat or the exit fails the shot (lead review of the G2 test: the handoff shot read too dark). The method and the line: §7 and `references/review.md` §6 B-06.

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


## 7. Options thumbnails, blocking stills, black-fill, masks and the value strip
Run in Blender by Python (MCP or headless); probed headless on Blender 5.1 (2026-10-22): each render below was written and measured.
- **Size and camera.** Render key frames at the review size from the game profile (PROPOSAL when it gives none: 1280x720 for measuring, and the phone viewport for `look_check.py thumb` from the profile's floor device, or PROPOSAL 1170x540 landscape as in the animator's renders), from each `CAM_<id>` with `sensor_fit = 'VERTICAL'` and the shot's vertical angle, the player-sized reference in frame. Options thumbnails use proxies and Workbench only: they are cheap on purpose.
- **Three renders from one pass, same camera, same frame.** (1) Shaded: Workbench `STUDIO` light, `OBJECT` or `TEXTURE` colour, Standard view transform (or EEVEE lamps for the value pass). (2) Black-fill per group: `scene.display.shading.light = 'FLAT'`, `color_type = 'SINGLE'`, `single_color = (0, 0, 0)`, world colour `(1, 0, 1)` (reads as `#FF00FF`, which `look_check.py` keys automatically), with only that group's objects visible for render (the heroes, the threat, the crowd). (3) Subject mask: `FLAT`, `color_type = 'OBJECT'`, subject objects coloured black, every other object and the world white; occluders in front stay white, so the mask keeps occlusion. Restore every changed setting and object colour in a `finally` block.
- **Measures.** `python tools/art/look_check.py silhouette <group-blackfill.png>` gives the group's box and area; heights for a scale ratio come from each group's `bbox_px.h`, never from the component list (components under 0.5 % of the frame are not listed, and overlapping figures merge into one component without an error). `look_check.py value <shaded.png> --mask <subject-mask.png>` gives subject/ring; `look_check.py thumb <shaded.png> --mask <subject-mask.png> --size <phone WxH>` gives the subject's box in px at phone size.
- **Rank the bright regions (B-06, B-18, R-09).** Name every region that might out-shine the subject (the subject, each lamp, sky patch, white prop, the threat's source of power). Read each region's luminance **p95**, never `rank_by_median`: a figure fills only part of its box, so a box median is the background's (a thin lit hero ranks below a mid-grey lamp; a small white-hot lamp ranks below a mid-grey hero, both with no error).
  - *Blender key frames:* render one object-colour mask per region in the same pass; the sky region's mask is the world black and every object white (it touches the border, so measure it with `value --mask`, never `silhouette`). A region covering 0.1 % of the frame or more: its p95 is the `subject` p95 of `value <shaded.png> --mask <region-mask.png>` (exact pixels). A smaller region (a far lamp) is refused by `--mask` (`invalid-mask`): take its box from `silhouette <region-mask.png>` (`bbox_px` is reported even then) and read its p95 from `value <shaded.png> --box <bbox> --name <region> ... --compare-subjects`.
  - *Roblox captures* (no masks): `--compare-subjects` with tight boxes. Get each part's screen box through the MCP (`Camera:WorldToViewportPoint` of the part's eight bounding-box corners; viewport pixels from the top left, no GUI inset, scaled by capture width ÷ `ViewportSize.X`; probe once on a known part before relying on it), all parts of one region under one `--name`, or draw a tight box by hand; record the box source. The region must fill well over 5 % of each of its boxes (under that, p95 is the background), and no brighter patch may sit inside a box (a sky corner in a loose hero box makes the hero rank first falsely): check the boxes on the capture you look at for R-09.
- **Flash count (R-10): the frames to export.** The count is the studio's one flash counter, the script in `vfx-craft/references/measure.md` §6. Save it as that section says and read its note (what it counts, which count to read, what it gets wrong with no error); this book keeps no copy. Export the frames it reads:
  - Render the whole animatic with every effect mark on in one pass, from the scene whose camera markers cut it (or from the sequencer that assembles it), at the shot-list rate with `frame_step = 1`.
  - Into a new, empty folder: PNG, `color_mode = 'RGB'`, colour depth 8 (16 also reads), the output path `<folder>/####` (names `0001.png`, numbers only), the review movie's view transform, recorded in the manifest.
  - Run `python flash_pulse_vfx.py <folder> <fps>` with the shot-list rate (29.97 for 30000/1001). Its first line must name the rendered frame count and range. Read both counts (over 10 % and over 3 % of the frame) as the counter's note says: with rain or a pan past dark shapes the 10 % count alone can read too low, and cuts and pans over-read the 3 % count; look at the frame of every listed onset, and use the counter's box workaround where its known-limits list says. Label: not verified (measured offline: script path, folder, rate, view transform). The limit is the `vfx-design` flash rule; a count over it is a fault in the edit or the effect marks, and the onset names show where.
  - Wrong with no error (tested on Blender renders): a render with `frame_step = 2` run at the scene rate doubles the count (a 5 Hz flicker read 10); per-shot renders copied into one folder interleave by frame number (shots of 4 and 5 flashes a second read 8); `look_check.py value` run inside the folder writes `<frame>.luminance.png` images that the counter reads as frames (value on every frame: 180 frames for 90, the 5 Hz flicker read 3). So run `value` on copies, and renumber per-shot renders into one sequence in edit order before counting.
- **Overlay zones.** Write the delivery overlay as rectangles in pixels at the review size (bars, subtitle area, skip control, the narrowest display's side margins at the fixed vertical angle, and the HUD on the handoff frame). A key subject's box from the mask or black-fill must not intersect them (arithmetic on the JSON boxes).
- **Value strip.** `look_check.py value` writes `<frame>.luminance.png` next to each frame (so never run it inside the flash-count folder): that is the grayscale view. Tile the luminance images in shot order into one strip, and the shaded or black-fill frames of each option into one contact sheet, with a few lines of Python (Pillow: open, resize to phone height, paste side by side, label with the shot id). Tiling is layout, not a measure.
- **Light variants.** For the key beat, 2-3 lighting setups on the same blocking (key direction, the brightest area, a rim where the figure meets a similar background); render the same key frame under each, measure with `value`, choose, record the setup in the shot table.
- **Stills for marketing.** Keep foreground, midground, background, lights and effects in named collections so each can be toggled; render the clean frame (effects collections hidden) first.
