---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J015-T09 G2 test"
supersedes: []
---
> Author: film-director · claude-opus-5-5 · high · 2026-10-21. Written for the vfx-designer; not sent (J015-T09 rule: briefs go into g2/ as files). Format: `rules/messages.md` §2.

<intent>
Four small effects carry the information of the boss reveal in the flooded observatory; none of them is decoration. The beacon's collapse is the moment the player learns the prize is not free: it must read as "it refused me", not "I broke it", and it happens before the hand touches it. The ripples are the first sign that something behind the beacon moved; after the collapse they are the only bright motion in the frame, so the eye goes to them. The guardian's eyes ignite in the beacon's own amber: this sequence's local convention is that the guardian holds the beacon's light. In the greybox the eyes are too small to read in the wide shot D (both eyes together are 0.083 of frame height at the end of D) and the director has kept the static wide for its scale and geography, so the eye glow has to do the work the tilt alternative would have done. The splash marks the moment the guardian closes the route; it must never hide the hand, the beacon or the exit, because that frame becomes the player's play view.
Look through the refs and the nearby files in g2/ before you act: the animatic and the boards show the frames you are designing for.
</intent>
<spec>
id: J015-T09-VFX                                   # not a ledger ticket yet; the lead files it if the job continues
from: film-director
to: vfx-designer
model: opus
effort: high
skills: [vfx-design, vfx-craft]
refs:
  - output/J015-g2/movie/boss-reveal_r5_animatic_TEMPsound.mp4   # take: timing, cameras, where each effect sits; ignore: proxy look, temp light values
  - knowledge/jobs/J015-film-director/g2/boards/contact-sheet.png  # take: mood, value plan (cool moon, warm beacon, cool exit); avoid: panel D's four-point eye cluster (two eyes are planned)
  - knowledge/jobs/J015-film-director/g2/previs/shotD_static_vs_tilt.png   # take: how small the eyes are in the static D; the tilt row shows the read we need without the tilt
  - knowledge/jobs/J015-film-director/g2/cue-sheet.md   # take: cue ids, frames, sync types, the sound each effect pairs with
fixed:
  sequence: boss-reveal rev 5, 30/1 fps, frame 1 = sequence start   # boss-reveal.shots.json rev 5
  beacon_collapse: shot B frames 21-27 (collapse starts B+20 = frame 21, ember by B+26 = frame 27)   # shot list B, animatic
  beacon_states: B start = pulse (last peak at frame 6); after frame 27 = ember; vfx.beacon.ember at frame 158 (E+20) = faint slow pulse resumes; flexible sync   # cue sheet
  ripple_first: frame 29 (B+28), from the front edge of the guardian's plinth, reaching the pedestal foot at frame 38 (the B->C cut)   # measured in Blender, animatic-manifest.md
  eyes: vfx.guardian.eyes at frame 106 (D+32), locked; must come after the head is in the moonlight (head enters at frame 90, measured)   # cue sheet
  eye_colour: the beacon's amber (same hue family as the beacon)   # sequence colour convention, beat-sheet.md
  splash: vfx.water.splash at frame 144 (E+6), locked, the frame the hand reaches the floor   # measured in Blender
  must_not_cover: [the guardian's head and eyes in D, the beacon in D and E, the planted hand in E, the exit arch in E (screen x about 0.30-0.38)]   # shot list continuity; measure_r5.json
  cameras: CAM_B..CAM_E poses and vertical FOV in boss-reveal.shots.json (`camera`, `fov_deg`)
open: [effect technique, particles vs mesh vs light, colours inside the stated families, shapes, curves, how the collapse looks, eye glow construction, splash size inside the must_not_cover rule]
avoid: [a flash or sting at the collapse (the moment is a removal: light and pulse stop), an explosion or sparks from the beacon (reads as "broken"), eye glow that blooms over the whole head, a splash that hides the hand or reaches the exit side, camera shake (none planned in this sequence)]
owns: [content/vfx/boss-reveal/]                    # PROPOSAL path; the lead confirms
not_in_scope: [the guardian model and rig, camera changes, sound, game code, timings (a timing change needs a shot-list revision through the film director)]
rules:
  - Flash and shake follow the vfx-design safety rules; this sequence has no shake and no flash.
  - Every effect must read with expensive effects reduced (phones): the information may not depend on bloom or depth of field.
  - Timings come only from boss-reveal.shots.json; never retime inside the effect.
  - Images only through tools/art/art_refs.py (reference-images skill); no franchise looks.
  - No asset uploads; the owner uploads.
deliver: content/vfx/boss-reveal/frame-script.md and the effect spec with exact Roblox values
checks:
  - C1: in a capture from CAM_D at 640x360, the two eyes are visible as two separate amber points at frame 124
  - C2: in a capture from CAM_B, the beacon change between frame 21 and frame 27 is visible without sound, and nothing bright appears at the beacon in those frames
  - C3: in captures from CAM_E at frames 144-175, the hand, the beacon and the exit arch stay unhidden in every frame
  - C4: effect start frames match the cue frames above within a tolerance the owner sets (no tolerance is set yet; report the measured offsets)
return: hand-back to film-director (rules/messages.md §3); frame script and key frames first (G2 sample)
</spec>
