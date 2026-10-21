---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: previs runs 2026-10-21 (Blender 5.1.2 headless), command log output/J015-g2/checks/commands.log
supersedes: []
---
> Author: film-director · claude-opus-5-5 · high · 2026-10-21

# Animatic manifest: `boss-reveal` rev 5

A timed greybox (proxies, temp light, TEMP sound), not a beautiful render. It answers staging, cut and timing questions; it proves nothing about Roblox runtime, phones or final look (film-craft C-08).

## Record (film-craft blender-previs §1)
| Item | Value |
| --- | --- |
| Blender | 5.1.2 (`bpy.app.version_string`, printed by every render and export run), headless; Blender MCP not used (headless is reproducible from the scripts) |
| Scene file | `output/J015-g2/previs/boss-reveal_previs_r5.blend` (new file; built by `g2/previs/build_boss_reveal.py` as `..._v14.blend`, then rev 5 pushed by `shotlist.py blender` and saved as a new file). No pre-existing .blend was opened |
| Shot-list revision | 5 (scene props `film_sequence = boss-reveal`, `film_revision = 5`, set by the push) |
| Rate | 30/1 fps (`fps = 30`, `fps_base = 1.0`) |
| Frame range | 1-175 (175 frames = 35/6 s = 5.833 s) |
| Output | 960 x 540, pixel aspect 1:1, PNG sequence `output/J015-g2/frames/r5/f_0001..0175.png` with burn-in (frame, marker, camera, lens, note) |
| Render | EEVEE (`BLENDER_EEVEE`), 16 samples; a headless render, not a viewport playblast |
| Colour management | view transform `Standard` |
| Cameras | `CAM_B`, `CAM_C`, `CAM_D`, `CAM_E` bound to markers `shot:B..E`; non-shot cameras `ALT_D_tilt`, `PLAYCAM_beat1`, `MAPCAM_top` (never bound) |
| Audio | TEMP tones rev 5: `output/J015-g2/audio/r5/TEMP_<cue>.wav` (9 files) placed at the shot-list cue frames by `previs/make_temp_audio.py` |
| Movies | `output/J015-g2/movie/boss-reveal_r5_animatic_TEMPsound.mp4` and `..._silent.mp4`: H.264 MP4, 205 frames at 30 fps, 960x540 (probed with Blender `movieclips.load`); frames 176-205 hold frame 175 so the handoff cues can be heard; they are **not** part of the sequence. Edit files: `output/J015-g2/movie/animatic_edit_r5*.blend` |
| Key-frame sheet | `g2/previs/animatic_r5_frames.png` (24 frames with burn-in) |
| Scale | 1 Blender unit = 1 stud (kit-test assumption). Explorer proxy 5.75 studs; avatar-range ghosts 4.75 and 6.5 studs (Roblox body scales: `knowledge/external/roblox-creator-docs/art/accessories/body-scale.md:24-36`) |

## Why the rate is 30/1
A project decision did not exist (game profile empty). 30/1 is an integer rate, so every frame is an exact 1/30 s and the Luau module's seconds have no NTSC fraction; it is the kit example's rate, so `diff` and the templates need no change; one previs frame is exactly two frames of a 60 Hz display. It is a timing convention, not a claim about feel. The owner can change it; a rate change is a new revision.

## How each length was measured
The cut is placed on the event that ends the shot; `shotlist.py diff --write` took the lengths from the markers. Acting durations inside the shots are my authored PROPOSALS (they are what the owner should direct on this animatic); three events were measured geometrically rather than authored:
| Measured in Blender | Frame | Used for |
| --- | --- | --- |
| first ripple radius reaches the pedestal foot (4.708 studs from the plinth edge) | 38 | the B→C cut |
| guardian head centre enters the moon shaft | 90 (D +16) | check: the head is lit 16 frames before the eyes ignite (D +32) |
| strike hand reaches the floor | 144 (E +6) | `sfx.guardian.slam`, `vfx.water.splash`, music option: one frame earlier than the pose key (E +7); the splash marker was moved to the contact frame in v10 |

| Shot | Frames | Start-end (s) | Cut event |
| --- | --- | --- | --- |
| B | 37 | 0.000-1.233 | first ripple at the pedestal foot (measured) |
| C | 36 | 1.233-2.433 | 2 frames after the step back lands |
| D | 64 | 2.433-4.567 | 2 frames into the strike anticipation (arm draw back starts +52) |
| E | 38 | 4.567-5.833 | control returns on the last frame; no hold after the settle (+30): nothing develops there |

No length, lens or speed comes from a film, a mood or the paper (the paper gives none). The total is this version's measurement, not a target.

## Moves: each considered against a static version
| Shot | Chosen | Alternative considered | Reason |
| --- | --- | --- | --- |
| B | static | push toward contact (paper EX-B-06) | the hand already carries the approach; the light collapse is the only news and a moving frame competes with it. Not rendered |
| C | static | none useful | the change of attention carries the beat (paper kept) |
| D | static | tilt that follows the head (`ALT_D_tilt`, rendered: `output/J015-g2/frames/r5_altD/`, sheet `g2/previs/shotD_static_vs_tilt.png`) | measured over 22 sampled frames: static keeps the beacon and the explorer in frame 22/22 and inside the 4:3 centre 22/22; the tilt keeps the beacon in frame 6/22 (4:3: 0/22) and the explorer 0/22, peak rotation 1.123 deg/frame (33.7 deg/s). The tilt shows the eyes much larger. Static recommended; the eye read goes to VFX |
| E | static, no camera move at the handoff | an authored ease into the play camera | the player inherits a frame that already shows the choice; nothing to re-orient. Engineering must confirm the play camera can take over this pose |

All cameras are static, so the reduced-motion version is the same sequence (no shake, roll or whip is planned; film-direction D-27).

## Version history (what each previs build changed and why)
| Build | Change | Why (evidence) |
| --- | --- | --- |
| v1-v2 | first layout; guardian arms longer, strike solved numerically (error 2.84 → 0.39 studs) | the hand could not reach the strike mark |
| v3 | guardian moved back 2 studs, oculus over the risen head | B was filled by the bowed torso; the bowed head must stay out of the light until D |
| v4 | B from above; exit dimmed | the exit glow sat behind the beacon and stole attention after the collapse |
| v5 | floor flooded (dais under water); B cut measured from the ripple | ripples could not reach a dry pedestal (geometry conflict the boards would have hidden) |
| v6-v8 | beacon/eyes/exit stopped casting shadows; exit glow unlit; fill raised | the point light inside the beacon sphere was blocked by the sphere itself |
| v9 | `frame_end` set after the ripple measurement | **bug**: v8 kept frame_end 184, so E ran 9 frames long; `diff` against the rev-1 plan (all UNKNOWN) printed "no drift" and `--write` took 47 frames; the next diff showed `E length -9 f (-300 ms)` and rev 3 corrected it |
| v10 | splash marker on the contact frame | one timing truth with the slam cue |
| v11 | C re-aimed | the beacon was outside the 4:3 centre (x 0.786-0.887) |
| v12 | E higher | rejected: the avatar still merged with the guardian's silhouette, the bottom half was black water |
| v13 | exit moved to the north-north-west wall; E over the right shoulder | in the behind-the-player view the exit, the avatar and the guardian were bunched and overlapping; now exit left (x 0.30-0.38), avatar centre (0.46-0.54), guardian right (0.53-0.78) |
| v14 | exit glow below the moon shaft in value | the exit was the brightest area in D |

## Readability measurements (Blender projection; not a phone)
From `output/J015-g2/checks/measure_r5.json` (`g2/previs/measure_frames.py`): every 3rd frame per shot plus its last frame; "inside 4:3" = inside the middle 75 % of the 16:9 frame, which is what a 4:3 landscape screen shows at a fixed vertical FOV; "unhidden" = a ray from the camera to the object's centre hits it first (ghosts and effect proxies skipped).
| Shot | Object | In frame | Inside 4:3 | Unhidden | Last-frame screen height |
| --- | --- | --- | --- | --- | --- |
| B | beacon | 13/13 | 13/13 | 13/13 | 0.263 |
| B | guardian head | 0/13 (planned: out of frame) | — | — | — |
| C | beacon | 13/13 | 13/13 | 13/13 | 0.146 |
| C | explorer | 13/13 | legs cut by design | 13/13 | 0.74 |
| D | explorer / beacon / head / eyes | 22/22 each | 22/22 each | 22, 22, 20, 22 | 0.371 / 0.059 / 0.233 / 0.083 |
| E | explorer / beacon / guardian / eyes / strike hand / exit | 14/14 each | 14/14 each | 14, 13, 14, 13, 14, 14 | 0.268 / 0.048 / 0.494 / 0.050 / 0.097 / 0.245 |

Avatar range (`output/J015-g2/checks/ghosts/ghosts_sheet.png`, ghosts 4.75 and 6.5 studs): C keeps all three heads in frame; in E the 6.5-stud avatar overlaps the guardian's left edge (silhouette merge risk for tall avatars); D unaffected.
