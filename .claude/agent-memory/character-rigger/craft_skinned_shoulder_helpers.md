---
name: craft-skinned-shoulder-helpers
description: Skinned shoulder/hip design that tested best on the teddy proxy; how to judge skinned zones (visible-fold flag pass)
metadata:
  type: feedback
---

For a short, fat plush limb skinned into the torso: clavicle-like helper with about 10% of raise/swing, a 50% half-bone at the limb pivot, a blend band about 0.10 into the torso, twist moved to the next rigid joint, bandage/cuff kept on a rigid piece. Judge with a visible-fold flag pass (flipped faces painted red, counted from the 6 views), plus area ratios as MEASURED.

**Why:** J005-T10c. On the source topology this setup bent cleanly up to an arm raise of 110 deg; 20% clavicle or no clavicle folded more. The crude single-blend skin smeared the bandage. A voxel-remesh test bridged the limbs to the body (FG01), so do not use one.

**How to apply:** at S2 for any skinned shoulder or hip; state the topology needs (rings around the limb axis, folds on rings, gaps kept open) and leave the loop count to the modeler. Related: [[craft-ring-ratio-and-cap-look]], [[craft-s2-posed-proxy]].

S4b update (J005-T10d): on the rebuilt mesh the winners were surface-measured (geodesic) zones and a hip half-bone share of 0.2 (not 0.5); a hard or faded zone edge at the armpit flank made kinks. Sweep zone metric and helper shares on the real mesh before asking the modeler for geometry.
