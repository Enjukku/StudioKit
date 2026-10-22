> Author: J018 maker modeler · claude-opus-5-5 · high · 2026-10-22. Part of `modeling-design`; built also from the owner's Riot transcripts (J018). The standards behind steps 1, 5, 7 and 8 of the skill; every check named here (SL, VL, CL, DT, MO, VA, GR, IM) is a line of the self-review in `review.md` §5. Numbers marked PROPOSAL are starting values a check may change; the art bible, game profile or owner wins.

# The read: what the model must say, and the form that says it

## 1. The read plan (written before the reference check, in the asset record)
Add a "Read plan" section to your copy of the asset record. One line per row; UNKNOWN when a fact is missing.

| Row | What to write | Example: one-handed sword, third person |
| --- | --- | --- |
| Job in play | the direction sheet's target-experience line; what the player must know from it at a glance: what it is, whose, what it does, how dangerous or valuable; its role and numbers from the game designer (a high-HP unit reads heavy, a fast one slim) | "the player's starter blade: light, fast, friendly" |
| Sell list | 2-4 numbered things the model must say, judged on every option | 1 starter tier, 2 quick slashes, 3 our world's bronze-and-leather look |
| Character | characters: two tension words, how it moves, what it would never wear; props and places: 3-5 personality words | "plain, trusty, well used" |
| Identity anchors | 3-4 chunky elements players will know it by, ranked; the 1-2 that must survive the icon crop | 1 leaf-shaped blade, 2 round bronze guard, 3 wrapped grip |
| Read order | first (silhouette, anchor 1), second (focal zone), third (material); 1-2 focal zones (IM2) | first the leaf blade, then the guard |
| Viewing conditions | game camera (type, distance, height, FOV from the game profile), on-screen height in px on the smallest phone, sides the camera reaches, other sizes (icon, shop card) | third person 12 studs behind and above; sword about 40 px tall; all sides; 150 px icon |
| Detail spots | 1-3 places where detail clusters; the rest is calm (DT10) | guard and pommel |
| Shape language | from the art bible, and why for this subject | rounded leaf: friendly starter |
| Value plan | brightest and most contrasted zone, quieter zone, the value breaks that separate parts, the ground it sits on | bright blade edge, mid bronze guard, dark grip |
| Palette roles | main / support / accent (about 60/30/10, PROPOSAL), reserved colours it must not use | steel / bronze / leather; no enemy red |
| Motion facts | moving models: what moves, weight class (light, medium, heavy), stress poses, contact points | grip contact for the right hand; light |
| Neighbours | 2-3 approved models it must look like and differ from | the shop's other starter tools |
| Stop criteria | what done means for this asset, and the pass budget (how many detail and polish passes) | anchors read at 40 px; steel reads as steel, leather as leather; budget passes |

A model with no approved anchors yet (a new hero, a new family) agrees the anchor list with the art director before the blockout. A known archetype (knight, ninja, dragon) lists the traits that make the archetype work and keeps them in every option (SL11). Simple models (medium effort) fill the rows Job in play, Identity anchors, Viewing conditions and Stop criteria; the rest only when the brief asks.

## 2. Silhouette: the first gate
Standards (check ids in brackets):
- **Fill it, shrink it, squint at it.** Judge shape as a solid black fill at the game camera and at phone size, never from wireframe or outlines (SL1).
- **3-4 chunky anchors.** Scale hook shapes up until they change the outline (thin spikes become chunky spikes); push the convex and concave forms past real; drop or move into texture every small part that does not improve the read (SL2).
- **Broad cuts, not notches.** Break the outline with a few large, sweeping cuts; a cut that vanishes in the phone-size fill is enlarged or removed (SL3).
- **Size steps.** Sibling shapes get clear steps, one big, one medium, one small (starting value about 3 : 2 : 1, PROPOSAL); two neighbours within about 15 % of each other in size compete (SL4).
- **Main lines first.** Find the one dominant top line and the bottom line that echoes it (side view) before any detail; panel lines, cuts and edges run parallel to it or converge on 1-2 points; one line continues across part joins (blade through guard into grip) (SL5).
- **Direction.** Objects meant to feel fast or aggressive lean their key shapes forward along the action; boxes read static (SL5).
- **The source of power reads first.** The weapon, casting hand or core keeps its size and thickness and is the clearest shape on the character (SL2, VL2).
- **Head and carried items in the outline.** Headpieces and carried items are the largest silhouette breaks; a removed landmark (a hat) has its slot filled with similar mass (a hairstyle, headgear) (SL2, VA2).
- **Asymmetry.** One asymmetric element large enough to see at the game camera, in geometry or a separate part (mirrored UVs would copy painted asymmetry) (SL6).
- **Body shape predicts movement.** A heavy body reads as stomping, a slim one as quick; the silhouette matches the motion set and the role (SL7).
- **Size signals importance.** Across a roster, screen size follows threat or value (a boss is clearly bigger than its minions; a rare pet is not smaller than a common one) (SL8).
- **Recognisable in under a second beats unique.** Compare with the nearest look-alikes (same role or palette) in black-fill; change shape where they overlap (SL8).
- **No awkward gaps.** A bare zone (an empty waist, a plain stock) is closed or filled with a story element; planned negative space stays (SL6).
- **Restated for our cameras.** Third person behind and above: the back, shoulders, head top and the held item's side profile carry identity; top-down: the top silhouette carries it; first-person arms only: the forearm and weapon top. Details on a side the camera rarely sees move to a seen side, even if the reference put them elsewhere. Focal detail goes where the game camera sees the surface largest and least foreshortened (the top and the side facing the camera); far or foreshortened parts keep big, simple shapes.
- **Options when the design is open.** 2-3 rough proportion or silhouette options at equal finish, one deliberately radical (a primary trait changed), rendered small and judged at phone size; compare in black-fill; an option that reads as another genre or tone is rejected however cool; pick with the reason tied to the sell list; record why the others lost.
- **Posed models** (a statue, an NPC sculpted in a pose, an icon pose): one clear line of action through the body before detail; no limb pointing straight at the camera (rotate it toward profile).
- **Faces.** Eye placeholders go in at the blockout (a face without eyes reads dead and skews every note); the face (or the focal feature of a faceless model) is at its best before each review; brow thickness, nose and face shape follow the character card and are pushed for phone size; expression faces and reaction props are pushed to the extreme because they are seen for about two seconds (SL10).
- **Hard cases.** A creature meant to scare is checked for threat in its black-fill (semi-human creatures turn silly easily); a character with several forms is several models in the plan and the budget.

## 3. Value and form: the second gate
- **Values before colour.** Flat material regions first (one flat colour per material); the grey version must read before textures, glow or Neon (VL1).
- **Head, shoulders, hands and held item carry the read.** In a third-person camera behind and above, the player sees their own head, shoulders, back and held item most, and others' heads and torsos at distance. Put the most value contrast, saturation and refinement there; push the lower body back (a little darker, cooler, weaker highlights; starting value: the lower-body line of the value-bands row of `art-review/references/art-bible.md` §7, the kit's one copy, PROPOSAL until the game's bible sets it); the lower body still separates from the ground (VL2).
- **Value breaks at the joints players track.** Neck, wrists, ankles and the weapon hand separate from their neighbours by value (skin against dark cloth, light metal against dark leather) (VL3).
- **Parts separate by value and shape, not by lines.** No outline or Highlight is needed for parts to separate; overlapping parts (gloves over hair, weapon across the torso) differ in value or hue (VL3, CL4).
- **Extremes are small.** Pure white, the darkest dark, the most saturated colour, emissive and Neon only on small focal accents against a calmer base (VL4).
- **Characters own a little more range than the world.** The character band is wider than the environment band; starting values: the value-bands row of `art-review/references/art-bible.md` §7, the kit's one copy (PROPOSAL until the game's bible sets them; `review.md` §5 converts grey-view value to the tool's luminance unit); no pure black on environment pieces (VL5).
- **Group detail in close values; frame the group.** Detail materials of one object sit in one close value family; the base colour frames them so the object reads as one thing (VL6).
- **Space high-contrast features like letters in a word.** Rivets, lights, studs and decals neither packed into a shimmering pattern nor left as one lonely bright spot (VL6).
- **Balance visual weight.** Dark heavy masses pull the read to their side; set the value centre where intended (VL6).
- **Form reads without rotating.** A small or still object reads as 3D only from shading that turns with its planes: a clear terminator on each major form, shadows only where the form turns away, contact shadows where parts touch, each part shaded as its basic form (cylinder, sphere, box, ribbon); large soft shading first, then committed sharp accents that never break the big value groups; ribbon, cloth and hair ends darker than their middles, and the parts the player always sees get the cleanest forms (VL7, VL8).

## 4. Colour and light
- **Palette after greys.** About 60/30/10 main, support and accent (PROPOSAL); new colours sampled from the palette already on the model and the bible's roles (CL1).
- **Saturation leads like value.** The most saturated colour sits on the focal zone, never on the lower body, a trim or the side away from the read; a balanced grey pass does not stay balanced after colour, so re-check after every colour change (CL7).
- **Reserved colours stay reserved.** Enemy, danger, team, rarity and interactable hues from the bible's colour roles never appear on decoration; team and rarity also differ by shape or trim (CL2).
- **One key light direction.** The art bible's sun direction (Lighting.ClockTime and GeographicLatitude in the place) for every asset; review renders use it; up- and light-facing planes are brightest. Painted light and baked AO stay soft so they never fight Roblox's live light or a day-night cycle (CL3).
- **Shift hue, not only value.** Shadows move to a darker hue (a red coat toward purple), highlights to a brighter hue (toward orange); light and shadow sit on opposite temperatures as the bible sets; no grey, muddy shadows. Gold stays saturated (warm orange-brown) in shadow. Skin keeps one temperature across face, hands and body (CL4).
- **No flat fills.** Small hue and value shifts inside each material (starting value: hue within a few degrees, value within 5-10 %, PROPOSAL) (CL5).
- **Colour where parts overlap.** Same-hue parts that overlap in common poses (red gloves over red hair) are re-valued or two-toned; mind associations (red with green reads festive) (CL4).
- **Judge final colour in Studio.** Studio lighting, tone mapping and post effects change values; the Studio capture decides, the Blender render only proposes (CL6).

## 5. Detail and surface
- **Indicate, do not spell out.** Hair and fur as 3-6 clumps with a few tapered dark marks; grass as soft clumps with a few blades; satin as three value blocks; a model must look right with or without its small details (DT1).
- **Budget detail by display size.** Detail only where the phone view shows it; marketing renders may carry more than the game model; areas the player runs past get macro forms only (DT2).
- **Finish comes from planes and edges.** Crisp bevel highlights and clean value breaks on hard materials, soft transitions on organic ones; not every edge sharp (stiff) nor every edge soft (mushy) (starting value: 20-40 % of hard edges dimmer, PROPOSAL) (DT3).
- **Functional parts and visible support.** Grips, buttons, pads, straps, clips: every attached piece shows how it is held on; a motif cut that removes mass gets braces or thickness so it reads heavy, not fragile (DT4).
- **Wear tells the story.** Wear where hands and feet go (handles, rails, steps, edges), grime where dirt gathers, condition by history (new and polished vs scrounged and worn), large enough to read at phone size (DT5).
- **Controlled imperfection.** Slight bevel and shape variation, chips, small colour accents; no sterile, perfectly even surfaces, no exact repeats, no visible tiling (DT5).
- **Stylisation level from the art bible.** Hint at the subject, do not copy reality; characters and environment pieces carry the same level of detail and material.
- **Personality in a few small accents.** Big areas say role and faction; 2-4 small accents (a pin, a charm, a patch) say who it is, sized to stay visible at the game camera. A hidden story detail is a second layer: small, findable close up, never competing with the one-glance read (DT7).
- **Vary only decoration.** Bevel, wear, chips and colour variation go on decorative surfaces; the anchors, contact points, gameplay colours, collision and the silhouette of gameplay shapes never vary.
- **Ornament late, small, with a reason.** One shaped motif instead of a plain trim; patterns only on functional zones (grip texture) at low contrast; one motif repeated at big, medium and small scale, built from a few basic shapes, abstracted, never pasted on: it reads as its subject in black-fill at mid distance and as part of the form, not a sticker (DT6).
- **Natural damage tapers.** Cracks vary in width and end in points, with a thin highlight edge; a few small glints on light-facing edges sharpen stone and metal (DT8).
- **One shape vocabulary.** Trims, ornaments and small shapes use the game's shape family; off-vocabulary shapes are rare and deliberate (DT6).

## 6. Design for motion (before the final model)
- **Believable anatomy and construction.** Joints and masses follow bones and muscles; creatures combine real animal parts (name a real source per part, MO7); every costume and prop piece shows its attachment (DT4).
- **Mass off the joints.** No static mass across a joint or cut (collars, scarves, armour edges, static hair near the neck, shoulders or wrists); hair bundled into one unit away from the nape; clearance around neck, shoulders and wrists for the animator's stress poses (MO1).
- **Nothing hangs in front of the shoulders and arms.** Pauldrons sit on the shoulder; drapes, cowls and capes do not cover the arm outline in idle, run or attack (MO2).
- **Costly features earn their place.** Capes, loose cloth, tassels, long hair and new joint chains each need a written reason and a rigid or bundled fallback; the rigger confirms the count (MO3).
- **Model what the rig moves.** A mouth that must open is modelled open-able, eyelids and teeth exist when the face animates; a new skin overlays the base armature so joints and fingers match the shared clips (MO4).
- **Moving parts have room.** Sliding barrels, opening blades, lids and doors are separate parts with pivots and nesting cross-sections that travel without hitting the body (MO4).
- **Contact points never move.** Grips, seat, stock-to-shoulder and hand positions stay identical in every variant, with clearance so hands do not clip (MO5).
- **Weight class shows.** Heavy held items keep their mass near the grip and read thick; light items read slim; the weight class is in the record for the animator (MO5).
- **Hook shapes face the held moments.** The signature shape shows in the key poses and hit pauses the animator lists, even when that is not physically exact (MO6).

## 7. Variants, tiers and families
- **Anchors hold, the rest changes.** A variant, skin or upgrade keeps every identity anchor as a big form, the base proportions and height; theme, material, colour and costume change; at most one anchor may be hidden by pose (VA1).
- **Fill a dropped landmark's slot** with similar mass; parts that do not exist in the new theme are replaced by a theme-fitting shape of similar mass (VA2).
- **One iconic swap, justified.** A twist swaps one iconic item, written as "keep X, swap Y for Z because W"; theme nods (1-3 per variant) are shape changes on existing anchors, not added clutter, and the theme is nameable from the props alone (VA3, VA6).
- **Palette says which version.** A new version gets a new palette; the same character in a new situation keeps the base palette (VA3).
- **Look follows real rank.** Rarity and power tiers differ in silhouette and finish by their real rank; the top tier may break the house style only by a recorded art-director and owner decision; premium tiers split into parts that take different finishes (gloss against matte) (VA4).
- **Cosmetics never cost gameplay.** A cosmetic keeps the role's silhouette class (a fragile ranged character stays slim), takes no extra screen room (starting value: black-fill area within about 10 % of the base, PROPOSAL) and never hides combat information (VA4).
- **The same character everywhere.** Face, posture and proportions match the anchor images in the model, its icon and any portrait or promo render; a darker or twisted variant keeps the character's poise and appeal (SL10).
- **Costume first, prop second.** A character's weapon or tool is designed after the costume, cites its approved revision and shares at least one costume motif (VA6).
- **Remakes keep the kernel.** Before updating an existing model, list the loved traits (kept, often strengthened) and the dated traits (trimmed).
- **Variant concepts on a mannequin.** For a new variant, render the base model (its least bulky version) at the game camera as the image-edit input for the variant references, so proportions and camera stay on model.
- **Group palettes.** Members of a faction, team or set take the bible's group palette.
- **A signature item looks skilled.** Hero items have more distinct parts and moving pieces than common items of the same class, shown in big parts, not micro-geometry (VA5).
- **Proportions read against the cast.** Place a new character on purpose in the roster (thinnest, average, bulkiest) and check it in a lineup at one scale (VA5).
- **Colourways are the same object.** Lock the silhouette, then re-check each colourway's value balance (VA5).

## 8. Grounding and the real place
- **Sit in the world.** Hero props get a base patch, plinth or buried skirt one value step from the open ground; no straight clean seam where a mesh meets the ground (bury it, cover it, or blend it with a skirt the environment designer can paint over) (GR1).
- **Scale is shown.** The player dummy is in every review; doors, seats, stairs and railings are sized to the player first; a large focal prop has a known-size object near it in its review (GR2).
- **Judge it in its set.** A prop or kit piece is approved only with one capture inside its stage (or on a capture of the stage's ground) at the game camera, never alone on a turntable (GR3).
- **Items read on the ground.** A pickup or item type is identifiable from its top and side profile even 30-50 % hidden by a box (GR3).
- **Materials follow gameplay rules.** One material per gameplay piece; a surface that plays differently (climbable, breakable, shootable) looks different; floors match their footstep material (GR4).
- **Walk areas stay flat and clean.** No bumpy rocks under feet, decoration outside the collision envelope, collision a few simple shapes matching the visible shape (GR4).

## 9. Worked examples
**A one-handed starter sword** (third person, about 40 px tall on a phone). Read plan as in §1. Blockout: leaf blade, round guard, grip, pommel at the size the player dummy holds; black-fill at 40 px: blade and guard read, pommel merges into the hand, so the pommel is enlarged by 30 %. Grey pass: brightest value on the blade edge, guard a step down, grip darkest; the hand-grip value break holds. Detail: guard and pommel only; leather wrap painted, not modelled; wear on the guard's front edge. Ships with grip pivot, `BladeTip` and `BladeBase` attachments, 512² texture (PROPOSAL), icon at 150 px with the leaf blade inside the crop.

**A hero pet, six on screen** (Tripo route, under about 7,000 triangles). Anchors: big round ears, curled tail, face mask. Raw Tripo check: ears softened, tail fused to the back; rebuild the tail, restore the ear tips past the reference. Black-fill from 12 studs behind and above: the tail curl must read from behind, so the curl is turned outward. Fur as five clumps with shadow strokes; brightest values on the face mask and ear tips, belly darker and cooler. Stress poses: the hop's squash needs clearance at the neck, so the cheek fluff is kept off the neck cut. Variant tiers: the legendary pet gains a crest and a gloss trim on the collar; the common pet never gets the crest.

**A shopkeeper NPC** (stands behind a counter; seen at 15-25 studs). Character card: "cheerful, stingy". Anchors: tall striped hat, round spectacles, money pouch. Lower body hidden by the counter, so the budget and detail go to the head, hat and hands; value: brightest on the face and hat band, apron mid, sleeves darker. Spectacles pushed to twice real size so they read at 30 px. Nothing drapes over the arms, which gesture across the counter.

**A timber wall kit piece** (village hub, players walk inside). Read plan: "old, mended, lived in"; detail spots at corners and the door frame; walls calm. One trim sheet with a normal map for planks and beams; head-height beam line on long walls; wear at the door handle height and the threshold; two plank variants so neighbours never repeat; collision a simple box per wall, doorway open at real player size; base buried 0.2 studs into the floor so no straight seam shows. Approved only after a capture of a corner assembly in the hub at the game camera.

**A rarity ladder for one sword** (common, rare, legendary). Same grip, guard position and contact points in all three. Common: base silhouette, matte. Rare: a broader guard and one inlaid gem (new silhouette break), a second finish. Legendary: a crest on the blade spine, three finishes (gloss blade, matte grip, emissive inlay on a small area), recorded as the tier's documented exception. Lineup check at the game camera: size of silhouette break and finish count rise with rank; the grey view still tells all three apart.
