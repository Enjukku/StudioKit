> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-design`. Paper notes: `knowledge/reference/modeling/03-*.md` (REV, CHK ids), `01-*.md` (BK10-BK13). Check budget: owner J005-D8, J007-D7. Rebuilt by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the read checks on the one review set (§1, §2), diagnosis by layer (§3), the self-review (§5), stop criteria (§6).

# Reviewing a model

## 1. Light checks (owner rule, wins over the paper's heavy review)
- **Numbers for every check** (the audit tool): triangles, loose parts, open edges, flipped faces, size in studs, materials, UV sets, texture sizes, part list vs the record.
- **One review set per hand-off**: the reference views next to matching renders, one render next to the player dummy, the game-camera views (front and back: the third-person camera sees your own character's back), and, once the model is imported, one Studio capture at the game camera on the real ground. That is the self-review the owner asked for ("renders from several angles compared with the reference image, scale against a player"). Commands: `modeling-craft` §3 step 8 and §7. The images per stage, and no others:

| Stage | Images |
| --- | --- |
| Blockout gate | front and back game-camera renders (blockout options only when the design is open; characters and large props with no proof capture planned: one Studio capture next to the default avatar) |
| Value gate | the front and back game-camera renders of the flat regions, plus one lit grey render (key light) at the main game camera (back for third person) when VL7 or VL8 runs (not on the simple-model path); on a Studio capture too only when one already exists |
| Texture pass 3 (form) | one flat unlit render at the main game camera (VL7) |
| Hand-off | the `review_renders.py` set, the back game-camera render, one Studio capture on the real ground and its mask capture (`modeling-craft` §7; held items: in the avatar's hand, back and front), the pass-3 flat render if the textures changed since |

When the blockout is itself the hand-off (a proof), the hand-off row is its set.

- **The read checks are measurements of that set, not new renders**: the black-fill (`look_check.py silhouette`), the grey view (`look_check.py value` writes the luminance image), the phone-size view (`look_check.py thumb`), the mirrored view (a one-line flip). Run them on the same files.
- **More images only when a number fails**, and only of the failing area. Conditional extras, named in the record when used: an occlusion render for a pickup type (GR3), a posed proxy render to settle a cut disagreement, the brightest- and darkest-ground captures at release (IM1), one in-set capture for a kit piece or prop (GR3). No before/after image sets unless a number failed. Report how many renders were made and looked at.
- **One full check per hand-off, by the receiver** (rig-pipeline §4a). The sender's self-check is numbers plus the one review set.
- **Label what each check could prove**: a still shows one moment (no motion, no sound); a Blender render proposes the look, a Studio capture decides it; a check whose input is missing is `not verified` and goes on the could-not-check list, never passed.

## 2. The pass/fail list (CHK01-CHK18 [O]; a pass needs stored evidence, UNKNOWN is not a pass)
| Check | Pass evidence | How (light) |
| --- | --- | --- |
| Approved reference | image id and revision in the record | record |
| Read plan | job, sell list, anchors, read order, viewing conditions, stop criteria filled before the blockout (simple models: the four rows of `read-and-form.md` §1) | record |
| Identity and silhouette | recognizable at the game camera and at phone size; every identity anchor visible; signature features present | review set; black-fill and phone-size view; silhouette overlap with the reference at the same camera (`tools/art/look_check.py silhouette --compare` with `--compare-mask`, `modeling-craft` §7) |
| Value structure | the grey view reads; focal zone has the widest luminance spread; extremes only on small accents; separates from its ground | `look_check.py value` on the game-camera view and the Studio capture |
| Light and colour | one key light direction; palette roles; no reserved hue on decoration; no flat or one-hue material; shadows shift hue | review set; `look_check.py palette --roles` for the roles; the reserved-hue and hue-spread rows of `modeling-craft` §7 |
| Proportions | landmarks match the approved image or an approved exception | review set; numbers if a ratio is named |
| Scale | size in studs matches the record; next to the player dummy | number + one render |
| Part inventory | every required part exists once; no extras | number (object list vs record) |
| Connectivity | loose-part count matches the plan; no floating or fused parts | number |
| Hidden parts | no faces fully inside other faces that ship by accident | number |
| Surface orientation | 0 flipped faces where a closed surface is required | number |
| Moving parts (if rigged) | the rigger's S4 sweep passes; no mass across a joint or cut | receiver's check; §5 MO |
| UVs | one UV set, inside 0-1, no stretched islands at shipped size | number; image on fail |
| Materials | one material per mesh; maps present; every material reads as itself at game size under Roblox light | number + the Studio capture |
| Budget | evaluated triangles and texture sizes within the budget and its source; no small feature that vanishes at phone size | number |
| Collision | chosen fidelity per part; openings stay open; simple and predictable | Studio check |
| Reuse | shared meshes on purpose; meaningful names | number |
| Grounding | no floating, no straight clean ground seam on props; judged inside its set | audit + Studio capture |
| Variants and tiers | anchors held, contact points equal, look follows real rank | §5 VA |
| Import parity | size, orientation, part count and look match Blender after import | numbers + one matched render |
| Phone cost | measured only when the brief asks; no phone → `not verified` | `performance` skill |
| Clean export | no helpers, dummies, high-poly sources or hidden objects exported | number (exported list) |
| Lineage | reference, route, Tripo version and settings, export settings recorded | record |

## 2a. What the owner rejected before (check these in the review set before any hand-off; FM87)
| Rejected | Check |
| --- | --- |
| Built without an approved reference: "it's poorly built" (FM01, owner, first game) | approved image id in the record |
| Too small, a "miniature" with cramped insides (FM15, FM32, owner, first game) | size in studs vs the record; player dummy render; doors, stairs, seats at player scale (FM31) |
| Boxy shapes where the art is organic; furniture too coarse; directional pieces facing the wrong way (FM32) | review set by eye, facing listed in the record |
| Held prop that does not read from the front at game view (FM36) | game-camera render; the in-hand Studio capture, back and front (IM1) |
| Head accessory that looks wrong from the side (FM37) | side render |
| Limb that comes off the body when it turns (FM38) | joint covers centred on pivots; rigger's S4 sweep |
| Rideable model with no seat or rider cut-out (FM39) | seated test figure, high and side views |
| Props clipping the body in key poses, props not scaling with the form (FM40) | clearance in the animator's key poses |
| Micro-detail that costs triangles but adds no read: "a lot of triangles that aren't necessarily needed" (FM18, owner, first game) | triangles spent vs silhouette change; §5 DT2 |
| Generic ornament that ignores the theme or material (FM19, FM21) | ornament comes from the subject's own theme |
| Variants that are only recolours when the owner asked for different designs (FM20, owner, first game) | variant list: what changes in shape |
| A flat blockout or procedurally painted boxes shown as the finished look (FM53: "I want details, and I want it to look really nice.") | label blockouts as blockouts; texture pass planned |
| A plain, untextured look (FM61, owner, first game) | texture pass in the plan |
| Gaps between pieces, misplaced pieces: "incredibly sloppy" (FM85, owner, first game) | assembled kit render at player scale |

Keep an approved simple placeholder when the owner likes it; do not replace it unasked (FM22).

## 3. When something fails
1. **Sort the defect by layer** (REV02 [O]): read (silhouette, anchors, proportion, value, colour role, light direction), construction (loose or fused parts, inside faces, normals, holes, duplicates, unapplied transforms), surface (material read, detail noise, wear, texel density), motion (collapsed joints, open cuts, grip, mass across a joint), runtime (collision, cost, materials, missing data after import). Read-layer problems come in this order: silhouette, then value, then colour, then material, then detail; never fix detail while a silhouette or value finding is open.
2. **Fix the biggest effect first**, not the most visible close-up (REV03). A weak read is fixed with contrast (value, size, shape, saturation) or by removing noise, never by adding detail or parts.
3. **Find the cause before editing** (BK12 [O]): geometry, camera, pose, material, light, or a bad reference. Change one cause at a time. A head that looks small only in a perspective render is a camera question.
   - **Drift from the reference:** render every saved revision (raw, each clean-up, final) in the **same camera, projection and lens as each reference view** (orthographic front with orthographic front, the same 3/4 lens), then read counts and ratios per revision. Repair at the first revision where a difference appears; never compare revisions shot with different cameras (BK10 [O], J007 hidden test).
   - **"Does not look like our game":** compare with the approved neighbouring models axis by axis, each with a number: value grouping and palette (`tools/art/look_check.py` value and palette), silhouette (`look_check silhouette`), edge treatment (bevel size as a share of height), surface roughness (mean of the roughness map), detail scale (smallest readable feature at the game camera). The range comes from the approved models, never from an outside threshold; fix the axes that fall outside it (J007 hidden test). The generic look of an image or Tripo model is the usual cause: the anchors win over it.
   - **A note names a solution** ("make it bigger", "delete the spikes"): restate the problem behind it in one line, fix that problem the best way, and re-check the problem (not only that the suggested change was made). Keep the named identity anchors while answering a general note.
   - **Words are not enough:** ask the art director for a paint-over on the game-camera capture, approve it, then change the model; every 3D change after a review traces to a note or a paint-over.
   - **A happy misread:** when the cold read of a shape is something else that also works, propose keeping it; a bad misread is fixed.
   - **Conflicting notes** are not averaged: send the conflict to the art director or the owner with both readings shown at the same camera; one owner decides.
4. **Re-run every check the fix can break** (REV09 [O]): retopology changes UVs, bakes and bends; an atlas changes material groups; separating a part changes pivots, collision and rigging; an export option changes scale or normals; a colour change shifts the value balance (re-run the grey view).
5. **Repair tools are not fixes by default** (REV05-REV07 [O]): one global merge distance can close eyelids or fuse clothing to the body; never fill every open edge (an intended open cloth edge differs from a hole that motion exposes).
6. **A broken section is rebuilt, not patched**: when a region keeps failing after one fix (tangled topology, a fused limb, a muddy texture area), clear it and rebuild it from the frozen blockout or the raw source. A part that will not come right (a face, a likeness) is parked, the rest moves one pass on, and the part is revisited with fresh eyes.

## 4. What the owner sees (REV10, REV11 [O])
Short evidence: the reference next to the model at the same angle, the player-scale render, the game-camera render, the phone-size view, the numbers against the budget, open trade-offs, one recommendation. Options go at equal finish, labelled, with one recommendation and its reason tied to the read plan. Describe the model as the player meets it ("the pet hops beside you; its curled tail reads from behind"), not as an asset list. Close with an honest recap: what works, what is too tame or too big, what needs another pass. Taste is judged by people; numbers inform it, never replace it with an invented score. Label every check gate-verified, MCP-verified, owner-confirmed or not verified.

## 5. Self-review before hand-back (run on the one review set)
Run the lines for the stage you are in; at a hand-off, run every line that applies. Tools: `modeling-craft` §7. A line with no tolerance from the brief, art bible or owner is recorded as MEASURED and judged on the image; starting values are PROPOSAL. Write the result per line in the asset record (pass / fail / not applicable / not verified, with the file).

**Simple models** (medium effort: a plain prop, a kit variant built on an approved piece, a fix of an approved model): run RP1, SL1-SL3, VL1, VL4, DT2, GR1-GR2 (GR5 for kit pieces), IM1-IM3; the other lines only when the brief or a failing number calls for them.

**Regions and units.** Every per-region number (upper vs lower body, focal zone, one material) is measured with a region mask cut from the black-fill, never with a box that holds background pixels (`modeling-craft` §7 region row). Value bands are grey-view value (the luminance image's grey level ÷ 255); `look_check.py value` reports linear luminance, so compare its p-values against the converted numbers (conversions only; the band values are the value-bands row of `art-review/references/art-bible.md` §7, the kit's one copy): 8 % ≈ 0.007, 15 % ≈ 0.020, 85 % ≈ 0.69, 92 % ≈ 0.83.

**Read plan (before the blockout)**
- RP1 Read plan rows filled; anchors agreed with the art director for characters, heroes and variant families; viewing conditions taken from the game profile (on-screen height in px recorded).
- RP2 Every design choice in the hand-back traces to a read-plan line; no element exists without a job.

**Silhouette (blockout gate; again at hand-off)**
- SL1 Black-fill of the front and back game-camera views and their phone-size versions: you can name what it is, its role and its mood from the fill; limbs, weapon and headpiece separate from the body.
- SL2 Every identity anchor shows in the phone-size fill of the views the camera uses; the source of power is the clearest shape; aligned IoU with the reference at the same camera recorded.
- SL3 Every intended silhouette cut is still visible at phone size; a cut that vanished is enlarged or removed.
- SL4 Sibling shapes step in size (no two neighbours within about 15 %, PROPOSAL).
- SL5 Side view fill: one dominant top line and an echoing bottom line; key lines run parallel or converge; stray lines counted; fast or aggressive objects lean forward.
- SL6 Mirrored game-camera view: the asymmetric element shows; nothing looks lopsided only in the mirror; no unplanned bare gap in the fill.
- SL7 The body shape matches the motion words in the record (heavy, light, graceful).
- SL8 Next to its nearest neighbours' game-camera renders: lower aligned IoU with them than with its own reference; screen size follows threat or value rank.
- SL9 Blockout options (only when the design is open): 2-3 options differ in black-fill, one radical; the pick and the rejection reasons are recorded; none was polished before the pick.
- SL10 Faces: the blockout render has eye placeholders; the face (or a faceless model's focal feature) is at anchor quality before each review; head shape and brows still read in the phone-size view; face, posture and proportions match the anchor images at the same camera and size (model, icon and any promo render).
- SL11 Known archetype (when the read plan lists its traits): you can name the archetype from the black-fill of every option and variant, and each listed trait shows in it.

**Value (value gate, before texture polish; again on the Studio capture)**
- VL1 The grey view reads: parts and major planes separate as value steps; it still reads with Bloom and post effects off.
- VL2 The focal zone (head, shoulders, hands, held item, or anchor 1) holds the widest luminance spread; upper vs lower body medians (one region mask each, split at the waist) show the lower body quieter (starting value: the lower-body line of the bible's value-bands row, `art-review/references/art-bible.md` §7, read as the lower ÷ upper luminance median, PROPOSAL); the lower body still separates from the ground.
- VL3 A value step at each tracked joint (neck, wrists, ankles, weapon hand) and between overlapping parts (two sampled boxes, each fully inside its part, `look_check.py contrast --sample`; ratio recorded).
- VL4 The top-5 % image (the brightest 5 % of the model's pixels; on flat-region renders, where ties mark more than 10 %, only the brightest grey level: record both shares), any clipped white and every emissive or Neon area sit on the named small accents only.
- VL5 The model's p5-p95 luminance sits inside the art bible's character band; environment pieces inside the environment band, no pure black (starting values: the bible's value-bands row, `art-review/references/art-bible.md` §7, PROPOSAL; in luminance by the conversions above).
- VL6 At phone size: detail groups sit in a narrow value band inside a framing colour; no shimmering pattern of tiny bright marks; no lonely bright outlier; the value centre sits where intended.
- VL7 A lit grey render shows a clear terminator on each major form and a contact seam where parts overlap; the unlit flat render still shows form from the texture once AO is in.
- VL8 The same lit grey render (and later the grey of the Studio capture): each part shades as its basic form (limbs as cylinders lit on top, the head as a sphere, plates as planes, ribbons rounding toward the camera); ribbon, cloth and hair ends are darker than their middles; the parts the player always sees (arms holding the item, in third person) have the cleanest forms.

**Colour and light (material pass)**
- CL1 `look_check.py palette --roles` with the bible's swatches: main, support and accent near 60/30/10 (PROPOSAL); no cluster far from every role.
- CL2 No reserved hue on a decorative region: on the colour render (front and back), with the parts that may wear the hue excluded, the reserved-hue count (`modeling-craft` §7 Reserved hue row, a screening aid) is 0 px or the owner's number; open its marked image when it is not 0. Team, faction and rarity also differ by shape or trim (the grey view tells them apart).
- CL3 Every highlight faces the bible's key light; no painted light from another side; baked shading soft.
- CL4 Sampled lit and shadow pixels of one material: the hue shifts and saturation holds (here saturation is colour against grey at the pixel's own darkness, as HSV S; CL7's peak uses chroma instead); gold shadows stay saturated; skin one temperature; same-hue overlapping parts separated.
- CL5 Each material: on a box inside its lit face, the hue spread (`modeling-craft` §7 Hue spread row, a screening aid) is above the flat limit, the variation inside one family: no flat single-swatch fill and no value texture in one hue (monochrome). A near-neutral material (steel, grey stone) is judged by eye on the colour render and recorded so.
- CL6 The Studio capture next to the Blender render: any colour or value shift noted; the Studio capture decides.
- CL7 The top-5 % colour image of the colour render (`modeling-craft` §7 top-5 % row, channel S = chroma: how colourful a pixel looks, so a tinted near-black boot or shadow never ranks high) sits on the focal zone; no lower-body, trim or background-side region holds the colour peak; after every colour change the grey of the colour render still passes VL2 and VL4.

**Detail and surface (detail pass)**
- DT1 Hair, fur and foliage read as clumps at phone size; the grey phone view has no high-frequency stripe noise.
- DT2 Features under about 4 px at phone size (projection recipe, PROPOSAL) are listed and removed or moved into texture; triangles go where the silhouette, a bend or a material edge needs them.
- DT3 Grey game-camera view: light and shadow edges defined on main forms; edge brightness varies; no zone where every edge is hard or every edge soft.
- DT4 One render shows how the object is held and used; every attached piece shows its attachment; no thin unsupported neck in the fill; no part looks like a flat 2D shape in any of the four side views.
- DT5 Touch points show wear at a size the game camera reads; no perfectly uniform flat area on a hero model; no exact repeats, mirrored text or visible tiling.
- DT6 Trims read as one shape at the game camera; functional patterns vanish at phone size and show close; the motif appears at big, medium and small scale, is built from a few basic shapes (count them) and still reads as its subject in the black-fill at mid distance, integrated into the form, not a pasted sticker; off-vocabulary shapes counted.
- DT7 The 2-4 personality accents each project above the small-feature size at the game camera (DT2 recipe); a story detail is invisible in the phone-size view and findable in the close `review_renders.py` views.
- DT8 Cracks vary in width and end in points; glints are few, small, on light-facing edges only, and visible at the game camera.
- DT9 Texel density (px per stud, `modeling-craft/references/blender-recipes.md` §6) of every asset seen with this one sits inside the range of its approved neighbours; a higher focal zone is recorded as intended; in a capture with them no asset looks sharper or blurrier.
- DT10 Detail spots at phone size: the detail-density image of the game-camera view (`modeling-craft` §7 detail row; the model cropped and scaled to its phone size; big part lines also show busy) shows the busy cells on the read plan's 1-3 detail spots with quiet areas between; even density (no busy cells, or busy cells spread over the whole model) fails; check the image against the phone-size view by eye.

**Motion (moving models; the rigger's S4 sweep is the full check)**
- MO1 No static mass inside a deformation zone or across a cut on the rigger's marked plan renders (count 0, or each has a route the rigger approved); clearance at neck, shoulders and wrists kept.
- MO2 In the rest views and any proxy pose captures, the arm outline stays separate from the torso; nothing drapes in front of the shoulders.
- MO3 Every costly part (cape, loose cloth, long hair, new chain) has a reason and a fallback; the rigger confirmed the count.
- MO4 Every moving part is a named object with its pivot; parts the rig must move exist (open-able mouth, eyelids); a skin on a shared body keeps joint positions within the rig sheet's tolerance.
- MO5 Contact and attach positions equal the base in every variant (numbers in studs); the weight class is in the record.
- MO6 The hook shapes face the camera in the animator's listed key poses and hit pauses (on the rigger's posed captures when they exist; else `not verified`, on the could-not-check list).
- MO7 Creatures: each body part names its real-animal source in the record.

**Variants, tiers and families**
- VA1 Base vs variant at the same camera (`silhouette --compare`): every anchor ticked (at most one hidden by pose); height ratio equal.
- VA2 Every dropped landmark slot is filled with similar mass; replaced parts fit the theme.
- VA3 The twist line ("keep X, swap Y for Z because W") is written; the palette change matches the recorded type (new version or same character).
- VA4 Tier lineup at the game camera: silhouette breaks and finish count rise with real rank; a cosmetic's black-fill area stays within about 10 % of the base (PROPOSAL) and covers no combat information.
- VA5 Hero items have more distinct parts than common items of the class; a new character's place in the roster lineup is the intended one; each colourway's grey view keeps the value balance.
- VA6 Theme nods and props: in one close `review_renders.py` view, the theme is nameable from the props and gear alone; the nods are shape changes on existing anchors (VA1's black-fill compare unchanged), not added clutter; a held prop cites the approved costume revision and shares at least one costume motif.

**Grounding and place**
- GR1 The audit shows nothing floating; the Studio capture shows no straight clean seam where the model meets the ground; hero props have a base.
- GR2 The player dummy is in the review set; doors, seats and stairs are sized to it (studs recorded).
- GR3 Props and kit pieces: one capture inside their set (or on a capture of its ground) at the game camera. Pickups: the type reads with 30-50 % hidden by a box (one occlusion render, only for item types).
- GR4 Each gameplay surface has its role's material; walk floors flat; collision a few simple shapes matching the visible shape.
- GR5 Kit pieces, environment pieces and props that live in a place: every row of the Check column in `kits-and-environment.md` §6 that applies, each result in the record.

**In game and honest close**
- IM1 The Studio capture at the game camera on the real ground (MCP-verified), measured at phone size (the whole capture resampled to the phone viewport; only a capture wider than the phone is cropped, in width) with the mask from its mask capture (`modeling-craft` §7): SL1, SL2 and VL2 hold there too (no usable mask: those three are `not verified` on the capture, never passed); the graphics quality level used is recorded (it is not scriptable). Held items (weapons, tools) are captured in the avatar's hand, back and front (`modeling-craft/references/export-import.md` §3), not lying on the ground. At release, a character or NPC that appears in several stages is also captured on the brightest and the darkest ground it meets, and the noise and value read hold on both.
- IM2 Cold read first: before looking at the colour render, write what each main shape reads as in the phone-size black-fill and grey views; compare with the intent; the reads come in the read plan's order (first, second, third); keep a good misread, fix a bad one.
- IM3 The hand-back lists what works, at least one honest weakness with its next step, every deviation from the reference with its reason, the could-not-check list, and renders made / looked at.
- IM4 Hand-off: the game-camera render (and the Studio capture) next to the approved image at the same size: every iconic quality in the record is present and at least as strong as in the image; each region reads as its named material; the finish equals or exceeds the image (`reference-check.md` §7 run again on the finished model).

## 6. When it is done
Stop when the read plan's stop criteria hold: every anchor reads at phone size; every material reads as itself at game size (gold reads gold, not bronze); the finish matches the approved neighbours; one close render shows no unfinished area; budgets pass. A note round that only repeats earlier notes ends the loop. New ideas past the gate ("it would be cooler with...") become follow-ups with a cost, never silent scope.
