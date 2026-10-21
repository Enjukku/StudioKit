---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009-T14 style test 2; images content/art/refs/concept/st2-*.png; diagnostics ./diag/
supersedes: []
---
> Author: art-director · claude-opus-5-5 · high · 2026-10-21

# Style test 2: image review (exploration.md §5) and grades (feedback-briefs.md §1b)

STATUS: done. Coverage: 4 final images reviewed (done); 3 rejected first tries reviewed (done); letter grade per final image (done); phone or real-slot check: not reviewed (no slot exists for a concept image, and look_check cannot mask a subject in a full scene; see "Could not check"). Everything is a PROPOSAL; nothing is approved and no anchor was made.

## Brief, restated
| Field | Value |
| --- | --- |
| Moment | A Tyrannosaurus charges through a shallow jungle river, roaring up at a huge meteor across the dusk sky; pterosaurs scatter |
| Reads first | 1. the T-rex (focal); 2. the meteor trail (brightest light) |
| Feeling | awe and danger, the end of an age |
| Camera / device | left to the model (concept scene, not a gameplay camera); landscape 1672x941 |
| Standard used | the four temporary bibles in this folder (PROPOSAL standard, no owner approval); no anchors; owner calibration set in feedback-briefs.md §1b |
| Constants | identical identity (79 words) and CONCEPT LOCK (49 words); only the WORLD STYLE LOCK differs |

## Evidence
| Image | File | Session | Try | Notes |
| --- | --- | --- | --- | --- |
| Clay stop-motion | `content/art/refs/concept/st2-clay-r1.png` | 01a15dc9-7cfa-73a0-... | retry 1 (lock fix) | try 1 in `_rejected/st2-clay-try1.png` |
| Cel-shaded anime | `content/art/refs/concept/st2-anime-r1.png` | 01a15dc9-7cfa-7930-... | retry 1 (re-roll) | try 1 in `_rejected/st2-anime-try1.png` |
| Low-poly | `content/art/refs/concept/st2-lowpoly-r1.png` | 01a15dc9-7cfa-7152-... | retry 1 (lock fix) | try 1 in `_rejected/st2-lowpoly-try1.png` |
| Blocky plastic | `content/art/refs/concept/st2-blocky.png` | 01a15dc6-3588-7673-... | try 1 | kept |
Diagnostics: `sheet.png` (labelled sheet), `diag/sheet-value.png` (hue removed), `diag/sheet-480.png` (each image at 480x270, a stress test, not a real slot), `diag/<id>-top0.5pct.png` + `diag/brightest.json` (where the brightest 0.5% of relative luminance sits).

## §5 checks per final image
| Check | Clay r1 | Anime r1 | Low-poly r1 | Blocky |
| --- | --- | --- | --- | --- |
| Construction possible | pass: 2 legs, 2 arms, 2-finger hands (crop) | pass: 2 legs in splash, 2 arms (crop; try 1 failed with a third leg-like mass) | pass: 2 legs, 2 arms, feet planted (crop) | pass: 2 legs, 2 arms, block feet |
| Counts and positions as asked | pass: none fixed; T-rex in river, meteor behind and above, pterosaurs from trees | pass | pass | pass |
| Light consistent | pass: meteor + low sun glow, both warm from the right | pass: meteor + setting sun right; rim light agrees | pass | pass |
| No generic substitution | pass, but the T-rex and pteranodons are stock designs (expected: none was designed) | same | same | same |
| Text, logos, franchise traits | pass: none seen | pass | pass | watch: smooth brick-built toy dinosaur, no studs or seams; reads as a generic premium toy, not a named product. Owner call if this direction is used |
| Meteor is the brightest light (measured) | pass: top 0.5% centroid at (0.71, 0.41) of the frame, meteor region | pass: (0.74, 0.36) | pass: (0.68, 0.39) | partial: top 0.5% split between meteor rim and white splash cubes, centroid (0.60, 0.62) (`diag/st2-blocky-top0.5pct.png`) |
| T-rex reads first | visual only: yes in colour; in `sheet-value.png` the body merges with the mid-value jungle, the head reads against the sky | visual only: yes; strong dark mass against a lighter sky | visual only: yes | visual only: yes; strongest hue and value break of the four |
| Reads small (480x270 stress test) | yes, T-rex + meteor survive | yes | yes | yes, clearest |
| Matches the lock | mostly: clay creature, cotton-wool smoke, clay meteor, resin droplets; broken: the flame and sky are still photographic; droplets show their support wires (charming at full size, odd if noticed) | yes: line art, one cel shadow tone, gouache background, graphic splash and fire | mostly: facets on the creature, rocks, mountains, clouds and splash; broken: the distant jungle and the waterfall are still soft-painted | yes: primitives, bevels, sheen, no studs, cube splash, neon-block fire |

## Grades (look and finish against the owner's bar; when unsure, the lower letter)
| Image | Grade | One line |
| --- | --- | --- |
| Clay stop-motion | **C+** | Convincing handmade creature and smoke, but photoreal flame and sky plus a stock orange "epic sunset" grade make it a clay-filtered CG scene, not a real miniature set |
| Cel-shaded anime | **B-** | The most finished frame: confident line, painted clouds, graphic water; generic in staging and saturation, with equal detail everywhere (no calm areas) and a heavy, chubby T-rex body |
| Low-poly flat-shaded | **C+** | The foreground facet work is good, but mixing it with soft-painted background areas reads as a "low-poly filter"; its palette was drowned by the orange wash |
| Blocky plastic toy | **B-** | Own grammar, the cleanest read at small size and the most Roblox-relevant; the splash competes with the meteor for brightest, and the toy face trades danger for fun |
No image reaches B: each has a familiar AI-image finish (the same composition and sunset grade; detail spread evenly). Calibration: kit screens C- and B- (J009-D6); there is no owner-graded concept image yet, so these grades are uncalibrated for this kind of image.

## Cohesion across the set
| Item | Observation | Consequence |
| --- | --- | --- |
| Subject | Same T-rex pose and action in all four (mouth open up-right, mid-stride, river splash) | consistency goal met |
| Composition | All four sessions chose the same layout: T-rex left of centre facing right, meteor top right, pterosaurs top left, waterfall and peaks right, low camera at the waterline. No layout was in the prompt | strong consistency at no prompt cost, but it is the model's default staging; the set can read as one template in four filters |
| Light and palette | Identity line "washes the scene in warm orange" dominated: every image is orange-on-violet; the low-poly coral and indigo and the clay teal shadows mostly disappeared | the shared light must-have overrode the per-style palettes; style difference now comes from rendering only |
| Style separation | Four clearly different renderings at sheet size (clay, drawn cel, facets, plastic parts) | owner goal "4 clearly different styles" met |

## What works (keep)
- One identical identity + concept lock, only the world lock varying, no anchors: four different styles, one recognisable scene, first try for blocky.
- Rich world locks about materials and construction (not layout) changed the rendering without stiffness.
- Fixing a broken lock clause by naming the parts that drifted (low-poly background, clay effects) worked in one retry each, without layout rules.

## Ranked findings (for a next round; no tickets, kit test)
| # | Finding | Evidence | Consequence | Next step (PROPOSAL) |
| --- | --- | --- | --- | --- |
| 1 | Set shares one default composition and sunset grade | `sheet.png` | owner may read "AI-made / samey" | either accept it as the consistency price, or let each style choose its own camera (drop nothing, add nothing; vary only the light line per style) |
| 2 | Light must-have overrides style palettes | `sheet.png`, `sheet-value.png` | styles differ less than their locks ask | move the light colour into each world lock ("the meteor light as the style renders it") and keep only "the meteor is the brightest light" in the identity |
| 3 | Clay: photoreal flame and sky | `st2-clay-r1.png` top right | clay-filter look | second lock pass: the sky is a painted backdrop card; the flame is cellophane (brief allowed only 1 retry, so not run) |
| 4 | Low-poly: soft-painted distant jungle and waterfall | `st2-lowpoly-r1.png` middle right | low-poly-filter look | same as above for distance layers |
| 5 | Blocky: splash ties with the meteor for brightest | `diag/st2-blocky-top0.5pct.png` | hierarchy slightly split | lower the splash value in the identity or lock if this direction is chosen |

## Could not check
- Real slot or phone read: a concept image has no slot; `look_check.py thumb` returned `invalid_reason: "no subject mask found ..."` on a full scene (run on st2-blocky). A 480x270 resample was viewed by eye only.
- Motion, sound: not applicable (stills).
