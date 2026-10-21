---
name: craft-cut-definition
description: How to define limb cut rings on merged generated meshes at S2 (landmarks + seeded flood fill, not plane optimisers)
metadata:
  type: feedback
---

Define shoulder/hip/neck cut surfaces from named crease landmarks (armpit valley, front/back crease points, outer top point; crotch fold, belly crease, seat fold; collar band fit) and label each part as the connected region beyond its cut that contains a seed inside the part. Measure crease cover (share of ring points on concave vertices) and any geometric lip only as a report.

**Why:** On the teddy (J005-T10) a crease-cover plane search picked planes that sliced the arm tube or reached the head, mirrored planes hit the head, and half-space labels pulled the outer thighs onto the arm (torn proxy). A "bandage cuff" was only a colour edge (lip 0.001-0.004).

**How to apply:** every S2 rig plan on a merged mesh; check per-part vertex counts before posing; state for each cut whether its cover is a crease, an overhang, a colour edge or nothing. See [[craft-s2-posed-proxy]].
