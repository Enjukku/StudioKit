---
name: craft-blender-bake-export
description: Blender rig build pitfalls for baked Roblox clips - rotation_mode after sweeps, FBX +1 frame on re-import, take name = scene name, weights must be diffed against accepted evidence
metadata:
  type: feedback
---

Craft rules learned building the teddy rig (J005-T18, 2026-10-21):

- After any test that sets pose bones to Euler, restore `rotation_mode` and assert QUATERNION before evaluating baked clips. Otherwise the quaternion curves are ignored silently (false drift, IK looks broken).
  **Why:** T05 showed 15° of false foot drift.
  **How to apply:** store and restore modes in every sweep helper.
- Key the authoring controls, save and reopen, then `nla.bake` with visual keying. Mute the constraints and reset `matrix_basis` before rest/reset tests.
- FBX: Blender re-import starts clips 1 frame later. The take name is the scene name, so set `scene.name = clip` before each clip export. In round trips, match vertices by index (coincident cut rings make nearest-vertex matches ambiguous).
- When a build script reimplements an accepted weight recipe, dump the accepted script's weights and diff them vertex by vertex.
  **Why:** a 0.04 vs 0.05 bandage band slipped through.
- Fold metrics: use the metric the sheet names for PASS. The blended-normal metric is stricter and is MEASURED only. Exclude stitch faces.
- On Windows, edit shared Markdown with `encoding="utf-8", newline=""` and diff against a backup.

Related: [[owner-budget-renders]]
