---
name: craft-s2-posed-proxy
description: Run a rigid-by-label posed proxy of all stress poses at S2; how to measure contacts and floor reliably
metadata:
  type: feedback
---

At S2, pose the read-only source with a throwaway rig: split faces by planning label in memory (torso faces stay shared so the bend zone blends), grey spheres at pivots as root stand-ins, render the saved cameras. Measure contacts with BVH overlap between posed parts after removing the B faces within ~0.03 of A at rest (the shared cut always touches), report onset angles from single-axis sweeps; solve "seat on floor" drops instead of trusting §B translations.

**Why:** J005-T10: the proxy found the seat reaches the floor at -0.16 (not the animator's -0.22), the tail cannot clear the floor at the asked rock-back, the head rim meets the shoulders at roll 10, and decided the shoulder variant by render. Signed-distance depth on open split parts gave nonsense values.

**How to apply:** every S2 with stress poses; give results as limits in the rigger keys, never as PASS. Headless Blender: absolute paths, numpy yes, scipy no (use mathutils.kdtree). Related: [[craft-cut-definition]].
