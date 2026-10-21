---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J005-T10b (character-rigger S4 on the teddy S3 delivery)
supersedes: []
---
> Author: character-rigger · claude-opus-5-5 · high · 2026-10-21

# Lessons: rigger S4 on a cut plush (teddy)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | Pixel counts of exposed caps (flag renders) showed only how much cap was visible; the textured close-ups showed why it read as broken: flat swatch-coloured balls and knife-edge rims seen edge-on | Judge seam cover on textured close-ups as well as counts; check what an exposed cap looks like (texture, shading, edge), not only whether it shows | output/rigs/teddy/s4/work/_extremes_zoom.png |
| 2 | My S2 cut plan had elongated shoulder (1.8:1) and hip (2:1) rings; a rigid sphere root cannot fill the long side at any rotation | At S2, report each ring's radius ratio as a risk, and tell the owner up front that a joint surface will show at the extremes; name the fallback options (deeper pivot, skinned joint, accept the look) before S3 | s2/inventory.json cuts.*.ring_radius_min_max; fix-note-r1 known_limit |
| 3 | A crude linear-blend skin proxy of the shoulder looked better than the rigid build in close views, but it smeared the bandage | Render both options with the posed proxy before deciding a route that is costly to change; give the owner both images | s4/options/socket_options.png |
| 4 | Workbench's view transform desaturates flat flag colours, so exact-value pixel counts read 0 | Count flag colours by hue margin, not by exact value | s4/scripts/s4_count_flags.py |
| 5 | A sed edit that silently matched nothing left the gameplay renders at the wrong size | After a scripted edit, grep for the new text and check one output (image size) before a long run | s4 run log (first gameplay pass at 1066 x 337) |
| 6 | The modeler's own K3 numbers and mine matched (audit, onsets, socket px) | Independent re-measurement is cheap with scripts and gives confidence to the fix note | s4/s4_checks.json vs geometry/k3_checks.json |

## Addendum J005-T10c (S2b, owner chose skinned shoulders and hips)
| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 7 | A clavicle-like helper with 10% of the raise plus a 50% half-bone and a 0.10 band gave the cleanest source-topology proxy (raise ≤ 110 no visible fold); 20% clavicle or no clavicle folded more | Test helper shares on the proxy with a visible-fold flag pass (red faces counted from the 6 views), not only flipped-triangle counts: folds hidden inside a crease do not matter | output/rigs/teddy/s2b/proxy_skin_measures_c0b6.json, _c10b10.json, _c20b10.json |
| 8 | A voxel remesh used as a "regular topology" stand-in bridged the arm to the torso and gave huge stretch | Never test skinning on a remesh that can close the gaps between limbs and body; it recreates the fused-bridge failure (FG01) | s2b/proxy_skin_measures_rm12.json |
| 9 | Moving the short upper arm's twist to the rigid wrist joint removed the candy-wrapper risk but added twist extremes to the wrist cut | When a limb segment is too short to carry a twist, put the twist on the next rigid joint and add its extremes to that cut's checks | rigger keys P08-P11 (S2b) |

## Addendum J005-T10d (S4b on the rebuilt skinned zones)
| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 10 | Measuring the blend zones along the surface (geodesic) instead of straight-line distance cut visible folds from 31 poses / 1,816 px to 19 / 278 on the same set | Measure skin zones along the surface; straight-line distance pulls skin across gaps (armpit, crotch) | output/rigs/teddy/s4b/weight_variants.json |
| 11 | Lowering the hip half-bone share from 0.5 to 0.2 removed the remaining sit and mid-swing hip folds (only the combined SP6 stayed) | Sweep the helper share before asking for geometry; the best share was far from the default 0.5 | s4b_checks_lh*.json |
| 12 | Cutting or fading the armpit flank out of the shoulder zone stopped the flank following the arm but made a kink at the boundary and more swing folds | A smooth stretch reads better than a hard zone edge; judge the flank on side-view renders, not on a displacement number alone | s4b/evidence/armpit_flank_SP3_side_*.png |
