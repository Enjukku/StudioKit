---
name: craft-ring-ratio-and-cap-look
description: Rigid ball roots cannot hide elongated cut rings; judge exposed caps by their textured look; flag-render counting tips
metadata:
  type: feedback
---

A cut ring with a radius ratio of about 1.5 or more (teddy shoulder 1.8:1, hip 2:1) always shows a joint surface at the extremes when the part is rigid with a sphere root. At S2, report the ratio as a risk with fallback options (deeper pivot, skinned joint, accept the joint look), and render the options. At S4, judge exposed caps on textured close-ups: flat swatch UVs and a flat annulus with a sharp edge read as broken even when the pixel count is small.

**Why:** J005-T10b. 62 of 79 poses showed sockets, and the textured close-ups showed glossy balls and knife edges in the walk stride and the wave. A crude skinned proxy looked smoother but smeared the bandage.

**How to apply:** at every S2 cut plan and S4 sweep. Count flag colours by hue (Workbench desaturates them), and check one output's size before a long render run. Related: [[craft-s2-posed-proxy]], [[craft-cut-definition]].
