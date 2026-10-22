> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-design`. Paper notes: `knowledge/reference/modeling/01-*.md` (RF, BK, SY ids; MP = paper line). Image making itself: `reference-images` skill. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the read plan in the record (§1), the game-camera view (§2), real views (§3), the concept as a blueprint (§7).

# From an approved image to a buildable model

## 1. The asset record (open it before any image is made)
One record per asset revision: `templates/model/asset-record.md`. Fields (RF7, BK1, BK3 [O]): asset id and revision; kind and role; who uses it and how (grip, seat, walk-through, pick-up); game camera and distance; visible sides; size against the player (UNRESOLVED until approved, never an invented standard); motion (link to the rig sheet, or "static"); attach points; collision need; material families and palette roles (from the art bible); budget with its source; approved image ids; route and why; open questions; the read plan (`read-and-form.md` §1: job, sell list, identity anchors, read order, viewing conditions, detail spots, value plan, stop criteria). Unknowns stay written as UNKNOWN.

## 2. Two image packages, not one (RF22 [O])
| Package | For | Contents | Family (`reference-images`) |
| --- | --- | --- | --- |
| Look target | everyone; the approval | one approved image of the subject (three-quarter view), plus a beauty or in-game image if the brief asks | `character`, `creature`, `prop`, `environment` |
| Build views | hand modeling | separate front, side and back images made from the approved image (attach it, I-10), same pose and scale, plus one view from the game camera; detail callouts as their own images (each identity anchor close up; material intent: what is metal, cloth, skin, fur, glow; what is modelled and what is painted) | same family, subject attached |
| Tripo input | the owner runs Tripo (J007-D4) | one clean single subject (or separate checked views if the Tripo route uses several), no labels, no sheet, plain background | `model` (MODEL REF LOCK) |

A turnaround collage is an approval aid, not a Tripo input: cut it into separate clean views (TR-24 [O]; reference-images I-04).

First-game practice (FM ids, `knowledge/reference/modeling/04-first-game-experience.md`):
- Extra views in one image made the image-to-3D tool build extra models; the owner asked for one subject, open stance, plain background (FM05, owner, first game: "the extra angles just make it make other models"). Turn the subject about 40 degrees so anything on its back shows (FM06; a first-game value).
- Refine an image by locking it: attach the last good image, say what stays exactly the same, change one thing per pass, proportions before face and detail (FM10).
- A real-world subject (a real building, vehicle or animal) starts from real photos and drawings; an AI image of a real place was inaccurate (FM12, owner, first game: "I would prioritize our real references").
- A large structure gets a measured plan (floor plans, views, a player figure) approved before building; a first set built without plans came out as miniatures (FM15, owner, first game). The size factor over real life is the owner's choice, recorded once and applied to every model (FM16).
- Say what the model must NOT look like; a style described only by what it is drifted to the nearest cliché (FM02). That belongs in the art bible's locks, not in each prompt (`reference-images` I-01).

## 3. Check the image before building (RF18 a-j [O]; reference-images I-05)
Record the failed panel and feature, never a score.
| Check | Pass when |
| --- | --- |
| Inventory | every limb, handle, wheel, window, wing, socket and ornament exists once, in its place |
| Same design in every view | eyes, belt height, roofline, grip shape, colour borders match across views |
| Can exist as a solid | surfaces have thickness, straps connect, holes stay holes, floating parts have a reason |
| Projection | "front" or "side" images are not perspective shots with shrunk far parts |
| Pose | neutral pose; the rigger can see joint centres and clearance |
| Hidden areas | roots of limbs, tail, wings and handles are visible; a hidden area gets an extra view, not a guess |
| Style | the main forms read at the game screen size; on style for the art bible; looks like the anchors, not the image model's generic default |
| Real views | the fantasy survives the views players get: tiny on a phone, from behind and above, from the top for top-down games; the identity anchors sit on the sides the camera sees |
| Read plan | each sell-list item and each identity anchor is visible somewhere in the image set |
| Colour and material | colour blocks on the same parts in every view; painted shadow is not read as relief |
| Scale | the size is stored in the record, not read from pixels |

Images can count parts wrong and place small parts loosely [V] I06 (RF19). So pair the image check with counts later on the mesh. A failed check → regenerate from the approved anchor (max 2 tries, `reference-images` §4) or ask the art director / owner which form is right. **Never average two views into a fourth design** (SY3, RF21 [O]).

## 4. What must match the image, and what may change (SY2 [O])
| Must match (invariants) | May change (the modeler decides, says so) |
| --- | --- |
| identity, primary silhouette, proportions, palette roles, attach and grip positions, facing, theme cues, how it moves, the gameplay envelope (doorways, reach, hitbox) | hidden-surface build, small edge treatment, inside supports, what is geometry vs texture |

A change to an invariant needed for motion or gameplay is shown as two options at the same camera and goes to the art director, then the owner (HND05 [O]). Never use an unmeasured performance claim as the reason for an art change (HND06 [O]).

Mark every feature as **shown, inferred, left out on purpose, or awaiting a decision** (BK2 [O]). A hidden back is a design question, not room for random detail.

## 5. Choosing the route: by hand or Tripo (MP:879, TR-17 [O]; owner 2026-10-21)
| Prefer hand modeling in Blender when | Prefer Tripo + Blender finish when |
| --- | --- |
| the model is simple, stylized and mostly primitives | the model must look especially good (owner) **and** has organic or intricate form that is slow to build by hand |
| it is a modular kit piece that must fit a grid exactly | sculpted surface detail matters at the game camera |
| it has mechanical pivots, exact sizes or many moving parts | the reference is one clear subject Tripo can read |
| it must match other kit pieces precisely | the rig plan can accept cutting a merged mesh, or the body may stay one skinned surface |

- Hero quality is an acceptance result, not a property of the route (P00, RU09 [O]). Both routes end at the same checks.
- Image-to-3D softens what made the concept appealing (sharp tips, crisp planes, pushed proportions): plan the Blender finish to restore the iconic qualities listed in §7, not only to clean the mesh.
- Compare the expected clean-up and redesign work, not the generation speed. Drop or rebuild a Tripo candidate when keeping its identity or its bends costs more than building by hand (TR-17 [O]).
- No measured Tripo success rate or time saving exists for this studio (TR-35 [UNKNOWN]); never quote one.
- Write the route and the reason in the asset record. The route may change at blockout.

## 6. Blockout comes before detail (BK4-BK5, BK14 [O])
Whole asset first: big masses, then secondary shapes, then small features that survive the game screen size. Character: body proportions before fingers. Vehicle: chassis and wheelbase before vents. Building: footprint, height, roof, doors at player scale before tiles. Tool: grip and head before decoration. Flat colours (one per material region) and even light at blockout so texture cannot hide weak shape. The blockout is the silhouette gate (`read-and-form.md` §2; `review.md` §5 SL): judged in black-fill at the game camera and at phone size, next to the player dummy, and in Studio next to the default avatar when the model is a character or a large prop. Proportions are fixed here; after the gate they change only with a new decision. Freeze the approved blockout revision and compare later steps with it.

## 7. The concept is a blueprint: keep its iconic qualities, decide its gaps
A reference image is the target for appeal, not a finished spec; 3D tends to soften it. Before the blockout write in the record:
1. **Iconic qualities** (3-5): what makes the image appealing and recognisable (a pushed proportion, a sharp silhouette break, a colour block, a material contrast). Each one must be at least as strong in the game-camera render as in the image.
2. **Gaps**: parts the image leaves ambiguous (the back, the inside of a sleeve, how a strap attaches, what a glowing part is made of). Decide each inside the art bible and the read plan and record the choice; when the choice changes the look, ask the art director for a targeted paint-over or an extra view, and ask only for the views and callouts the build needs. Never copy an ambiguity literally, never stall on it. A missing view or pose is made, not guessed: an extra image through `reference-images`, or a posed Blender mannequin render at the game camera. A part meant to be designed later stays a marked placeholder (PROPOSAL) listed as an open item.
3. **Material intent per region**: what each region is (gold armour or shiny cloth? silk or velvet?) with one real-world reference and its **local colour** (the colour with no light on it: the image's mid-tone, never its shadow or highlight). Unclear → ask the art director before modelling; a wrong material guess changes the read and the rig.
4. **Intent lines** (3-5): who or what it is, the mood, the key reads. A 3D model seen from many angles cannot match a 2D image pixel for pixel: translate the intent, do not trace the strokes.
Check: the game-camera render next to the image at the same size: every iconic quality is present and at least as strong; each region reads as its named material; each flat base colour matches the image's mid-tone; the hand-back lists the gaps with the choice made. The finish of the shipped model equals or exceeds the image. The same check runs again on the finished model at hand-off (`review.md` §5 IM4).
