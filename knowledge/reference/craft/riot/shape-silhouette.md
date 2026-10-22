---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, modeler, reference-images, vfx-designer, ui-ux-designer, environment-designer, animator, character-rigger, marketing, film-director, game-designer, level-design, sound-designer, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Shape and silhouette

The outline and the big shapes: the first read of anything, before value, colour or detail.
SS-01 to SS-04 are the working order and the checks (silhouette first, fill it, cut broadly, keep only the iconic elements). SS-05 to SS-09 are shape language and shape design (meaning, one vocabulary, size steps, direction, profile lines). SS-10 to SS-15 are silhouette for bodies and poses. SS-16 to SS-20 are motifs, groups and backdrop shapes.
Related: value in `value-contrast.md`, identity anchors in `character-design.md`, the one-second read in `visual-hierarchy.md` (VH-07, VH-08), effect shape codes in `vfx-reads-timing.md`.

### SS-01 Silhouette first, then light that shows form, detail last
- principle: Lock the silhouette and pose with flat big shapes first and ignore detail. Only when the silhouette passes add rough lighting, and light for form (a clear light side and shadow side), not for prettiness. Detail and textures come last: "I can always add details later" (R05).
- why: Big decisions are cheap to change at the shape stage; detail spent on a wrong pose or proportion is wasted. Pretty, soft lighting flattens volume and loses the 3D read.
- apply: Reference-images: early option rounds ask for two-tone (dark and light) silhouette sketches or flat-shape roughs. Modelers: the first deliverable is a black-fill render of the blockout at the game camera; proportions are fixed here (for example Gekko made shorter because he was too tall, R05:459). Then one key light and a grayscale render; textures last. Test lighting on simple primitives first.
- check: A black-fill silhouette check (`look_check.py silhouette`) passes before any lighting or detail work is accepted; then a grayscale render shows one clear light direction and a distinct light and shadow side on each main form. Fail if detail exists on a pose or proportion that has not passed.
- mistake: Polishing detail before the pose is locked; overthinking small details early; prioritising pretty over form (R05:811-815).
- examples:
  - R05: shapes to lock Brimstone's pose, then a rough side light, the face still empty (R05:465-483); form before prettiness, studied by lighting clay shapes (R05:803-816, 926-935).
  - R10: a solid full silhouette first, painted inside its bounds (R10:269-277, 289).
  - R00a: two-tone sketches keep focus on big graphic shapes and make ideation fast (R00a:822-834).
- roblox_fit: The same order works with blockout Parts in Studio before MeshParts [inference]. Roblox lighting changes shadow quality per technology and device; verify form in-engine [unverified].
- roles: art-director, modeler, animator, character-rigger, reference-images, marketing, environment-designer, vfx-designer, ui-ux-designer, reviewer
- also: process-iteration, value-contrast, light-colour
- sources: R05-F15 (R05:465-483); R10-F11 (R10:269-277, 289); R00a-F22 (R00a:822-834); R05-F32 (R05:803-816, 926-935)

### SS-02 Judge the silhouette filled solid, small and squinted
- principle: Lines hide the silhouette; a solid fill shows it. Fill the figure with one dark value on the real background, step back (or shrink it) and squint to find where the shape should be pushed or pulled.
- why: The silhouette is the first read; filling and squinting remove detail so only the shape remains, and the eye judges mass by filled shape, not outlines.
- apply: Every model, concept and pose review includes a black-fill render at the game camera on the actual background, plus the same at thumbnail size. Reskins work inside a locked base silhouette and are filled to check.
- check: `look_check.py silhouette` on the black-fill render; the same at thumbnail size (`look_check.py thumb`); limbs, weapon and headpiece separate from the body; a fresh agent names the subject from the fill alone.
- mistake: Judging a design only from line drawings or only at full size, close up.
- examples:
  - R08: filling the space with a darker grey "to make sure that there's enough contrast to read it" (R08:501-508).
  - R12: the gun cleaned up and filled as a silhouette before colour; draw with big shapes while the silhouette is open (R12:218-225, 261, 268).
- roblox_fit: Same check at the gameplay camera distance; many players and effects on screen make silhouette more important [inference].
- roles: art-director, modeler, animator, vfx-designer, ui-ux-designer, marketing, reference-images, reviewer, qa-lead
- also: value-contrast, critique-feedback
- sources: R08-F20 (R08:501-508); R12-F20 (R12:218-225, 261, 268)

### SS-03 Break the silhouette with few broad cuts, not small notches
- principle: When everything is far and small, silhouette is the most important part of the design. Break it on purpose with a few broad, sweeping cuts; small shapes cutting the edge are invisible in game.
- why: Only large silhouette changes survive distance and small screens.
- apply: Make silhouette breaks large; remove tiny notches or move them into texture. PROPOSAL default [inference]: a cut must stay visible in the black-fill at phone game-camera size.
- check: Black-fill at the game camera and at thumbnail size (`look_check.py silhouette`, `thumb_check.py`): each intended cut is visible; any cut that disappears is enlarged or removed.
- mistake: "Little shapes cutting through the edge of the gun ... you wouldn't really be able to see it from in game" (R01:908-916).
- examples:
  - R01: extending the gun cuts to be broad and sweeping made them apparent (R01:908-916).
- roblox_fit: Phone screens are smaller than League's PC view, so cuts must be bigger still [inference].
- roles: modeler, art-director, reference-images, vfx-designer, environment-designer, reviewer, qa-lead
- also: exaggeration
- sources: R01-F51 (R01:908-916)

### SS-04 Keep the few identifying elements, make them chunky, cut the rest
- principle: A small on-screen character or item survives as 3-4 identifying elements. Choose the right ones (the danger is choosing wrong ones), make them big and clear, push the convex and concave form beyond realism, and remove or reduce every small thing that does not improve the read (rivets, buttons, buckles).
- why: At small size only a few big elements survive; they must be the ones that identify the character. Chunky shapes survive motion and let players track a limb; removing noise organises visual importance.
- apply: The brief lists 3-4 identifying elements per character or item, agreed with the art director before modelling. Modelers scale hook details up to silhouette size (thin spikes become chunky spikes) and drop small details or keep them in texture at low contrast. Review tests each small detail by removal: if the read stays, it goes. Same rule for props, UI icons and VFX shapes.
- check: Thumbnail-size and game-camera captures (`thumb_check.py`, `look_check.py thumb`): every listed element is visible; black-fill identifies the character; before/after captures with a detail removed show no lost read (then keep it removed); convex parts carry light, concave parts shadow.
- mistake: Reducing Garen to "his boots, hands, and hair" (R00a); form-fitting plates with thin spikes that vanish (R11); buttons that "added a lot of unnecessary noise" (R01).
- examples:
  - R00a: Garen simplified to sword, pauldrons and scarf for League's small size (R00a:1146-1176).
  - R11: Katarina's gauntlet spikes chunked up so the "dramatic metal shape" lets you track her arm (R11:187-195).
  - R01: buttons removed from the blouse; concept art relays visual information (R01:940-946).
  - R03: Caitlyn's identifying points are the hat, giant rifle, long legs and collar; over-emphasise what pops out and what is concave (R03:208-217).
- roblox_fit: Phone screens make this stronger; small details also cost triangles (knowledge/external/roblox-creator-docs/art/characters/specifications.md:378). Keep identifying elements readable from behind for third-person cameras [inference].
- roles: modeler, art-director, character-rigger, animator, ui-ux-designer, marketing, reference-images, environment-designer, vfx-designer, reviewer
- also: character-design, visual-hierarchy, materials-detail, exaggeration
- sources: R00a-F32 (R00a:1146-1176); R11-F15 (R11:187-195); R01-F52 (R01:940-946); R03-F09 (R03:208-217)

### SS-05 Shape language carries meaning: sharp is danger, round is friendly
- principle: Shapes carry temperament and meaning before detail or colour: sharp, straight, protruding shapes read aggressive and fast ("Kiki"); soft, sloped shapes read gentle ("Bouba"); squares read stable. Choose the shape language from the character's personality and the object's role, and use directional shapes as pointers to where to look, what is dangerous and what is safe.
- why: The link between shape and feeling is near universal; shape is read first. To make something more aggressive, stick shapes out further along the same line direction.
- apply: The art bible maps shape language to roles (threats, hazards and enemies sharp; friendly, safe and cute soft). Each character brief states its language (sharp, round, square) and it applies to costume, prop, VFX and UI frames of that character; place the personality shape on high-presence zones (shoulders, head). Factions reuse their shapes. Environment and UI use directional shapes to point at the route or objective. Sound follows the same mapping (sharp transients vs soft attacks) [inference].
- check: Black-fill review: a reviewer labels the mood (dangerous, friendly, stable) from the fill alone and it matches the brief; count dominant corner types in the silhouette; threats and harmless props are distinguishable by outline alone, without colour.
- mistake: Soft round shapes on a character meant to feel dangerous; spikes on friendly items; similar silhouettes for threats and harmless props.
- examples:
  - R12: Kiki and Bouba; added straight protruding lines and "it looks pretty aggressive already" (R12:114-121, 174, 189-190).
  - R01: Caitlyn "not necessarily aggressive but dangerous if crossed" gets sharp geometric cuts (R01:226-238).
  - R11: shoulder spikes fit a "very sharp and jagged personality" and echo a faction sibling (R11:285-286, 315-318).
  - R00a: shapes act as arrows: where to look, what is dangerous, what is safe (R00a:299-314).
- roblox_fit: Third-person and top-down cameras also see silhouettes from above; check the top silhouette, not only the side.
- roles: art-director, modeler, reference-images, animator, vfx-designer, ui-ux-designer, environment-designer, character-rigger, sound-designer, game-designer, level-design
- also: character-design, style-identity
- sources: R12-F11 (R12:114-121, 174, 189-190); R01-F13 (R01:226-238); R11-F22 (R11:285-286, 315-318); R00a-F08 (R00a:299-314)

### SS-06 One shape vocabulary for the whole game, down to the small shapes
- principle: The whole game shares one shape language, and the style lives as much in the small shapes (trims, ornaments, particle shapes, UI corners) as in the big ones.
- why: A consistent shape vocabulary makes every piece read as the same game and unifies the world's identity.
- apply: The art bible names the game's shape vocabulary (for example VALORANT: lines, rectangles, triangles, few circles; Rift: "grimsey" knife-like rocks and paths). Modelers' trims, environment props, VFX particle textures, UI ornaments and key-art details use it.
- check: Silhouette sheet of a set of props and details from one capture: one shape family dominates; count off-vocabulary shapes, which should be rare and deliberate.
- mistake: Mixing round, curvy details into an angular style (R05:722).
- examples:
  - R02: one shape language across the map, rocks like knives (R02:870-876).
  - R05: VALORANT style lives in lines, rectangles and triangles; triangles are "very important, very iconic" (R05:717-730).
- roblox_fit: Angular vocabularies suit Part and wedge building and low triangle counts [inference].
- roles: art-director, environment-designer, modeler, vfx-designer, ui-ux-designer, marketing, animator, reference-images, level-design
- also: style-identity
- sources: R02-F37 (R02:870-876); R05-F26 (R05:717-730)

### SS-07 Big, medium, small: never two shapes the same size
- principle: Give sibling shapes clear size steps: one big, one medium, one small. Equal "half and half" shapes compete, the viewer cannot tell where to look first, and the image looks dull. Humans default to equal sizes, so it must be fixed on purpose.
- why: Size contrast creates hierarchy and rhythm.
- apply: For any group (rocks, plants, crystals, debris, UI elements, particles), set size ratios before placing. PROPOSAL default: about 3 : 2 : 1 or larger steps [inference]. Few instances with clear steps; vary plant heights low and tall.
- check: Measure the bounding sizes of sibling elements in a capture or black-fill; fail when two neighbours are within about 15 % of each other in size [inference threshold].
- mistake: "half and half shapes always tend to compete against each other and make the painting look bad" (R13:223-225); "three of them are looking very similar in sizes? That is not good" (R13:947-949).
- examples:
  - R13: three similar rocks fixed to one big, one medium, one small; "one plant is boring" fixed with big, medium, small, low and tall plants (R13:221-247, 818-820, 945-959).
- roblox_fit: A few varied pieces beat many equal ones on phones and lower instance counts [inference].
- roles: art-director, modeler, environment-designer, vfx-designer, ui-ux-designer, marketing, character-rigger, reference-images, level-design, reviewer
- also: rhythm, composition-focus
- sources: R13-F09 (R13:221-247, 818-820, 945-959)

### SS-08 Slopes make direction; tilt shapes along the action
- principle: A box reads static; a triangle reads dynamic because its slopes show direction. Tilt the key shapes to create direction and support it with other lines that run the same way.
- why: Slopes imply motion; objects meant to feel fast or energetic need direction.
- apply: Tilt key shapes forward along the action direction (muzzle forward, character lean, UI arrows); keep supporting lines parallel or converging to that direction.
- check: Side render or capture: most diagonal lines point toward the front or action direction; flag box-like blocks without slope in key areas of an object meant to feel fast.
- mistake: Static, boxy forms on an object meant to feel fast.
- examples:
  - R12: box versus triangle; the thunderbolt tilted to create direction (R12:107-113, 122).
- roblox_fit: No change.
- roles: modeler, art-director, animator, vfx-designer, ui-ux-designer, environment-designer
- also: exaggeration, composition-focus
- sources: R12-F10 (R12:107-113, 122)

### SS-09 Find the main top line and bottom line first
- principle: Like a car designer's "shoulder line", find the one main line along the top of an object first, then the bottom "character line"; together they create most of the character and the right silhouette.
- why: The eye follows long edges; one strong line organises the whole form.
- apply: In the Blender blockout, define the main top and bottom profile curves (side view) before detailing. Reference-images: ask for a clear side-view profile line.
- check: Side-view black-fill or edge render: one continuous dominant top line and a bottom line that echoes it. Fail if detail exists before the lines.
- mistake: Detailing before the main line exists [inference].
- examples:
  - R12: a thunderbolt-flow shoulder line on the Phantom; the bottom line from trigger guard to stock repeats it (R12:84-91, 104-106).
- roblox_fit: Side profile is what a third-person camera shows of held items [unverified].
- roles: modeler, art-director, reference-images, character-rigger
- also: composition-focus
- sources: R12-F08 (R12:84-91, 104-106)

### SS-10 Line of action and gesture before detail
- principle: A pose is read through one simple line of action through the body; all parts flow with it. Nail the overall gesture loosely first; details (fingers, face, costume) come after. Broken or complex lines confuse the pose's purpose.
- why: One clear line reads instantly, even small; gesture sells the character's believability; detail done early is wasted when the pose moves.
- apply: For each key pose (animation keys, key art, thumbnails, lobby poses), state the line of action first, then align spine, limbs and weapon to it. Animators block whole-body key poses before fingers and face. Reference-images ask for loose pose options before detailed sheets.
- check: Black-fill of each key pose at game-camera size: one dominant curve or diagonal is visible; mark poses with competing lines. In `clip_check.py` sampled frames, the key poses exist before polish passes.
- mistake: "Broken or complex lines of action" (R00b); "nitty-gritty detail issues" before the overarching ones (R08).
- examples:
  - R00b: animation is a series of poses; a line of action diagram (R00b:3075-3103).
  - R08: loose figure sketches of Alune solving body motion only (R08:247-253, 263-269).
- roblox_fit: Blocky or stylised Roblox bodies have few joints, so the line must come from big parts (torso tilt, limbs); faces are small at the game camera [inference].
- roles: animator, character-rigger, reference-images, marketing, art-director, film-director, modeler
- also: character-design, weight-timing
- sources: R00b-F33 (R00b:3075-3103); R08-F10 (R08:247-253, 263-269)

### SS-11 Give the jump apex a pose: legs tucked into a V
- principle: The classic dynamic air pose tucks the legs under into a V shape, knees up, toes pointed down; it adds height and confidence. An apex with dangling legs has no pose.
- why: The V silhouette is strong and reads as lift and control.
- apply: Jump apex keys, emotes and key-art poses use the tucked V; ask reference-images for concept poses with it.
- check: Black-fill at the apex frame shows a clear V and pointed toes; legs are not hanging straight.
- mistake: "there's no pose in the air" (R04:524).
- examples:
  - R04: "tucking the legs up underneath so you get like a really beautiful kind of V-shape" (R04:526-538).
- roblox_fit: No change [inference]; R15 legs have enough joints for the V.
- roles: animator, marketing, reference-images, film-director
- also: exaggeration, character-design
- sources: R04-F24 (R04:526-538)

### SS-12 Body shape predicts movement
- principle: The silhouette tells who the character is and how it moves: a heavy body says "he likes to stomp around, not graceful". Learn which muscles stand out and accentuate those shapes.
- why: Body shape predicts movement and personality before any animation plays, so model and motion must agree.
- apply: Match body proportions to the intended movement style in the brief; the animator's weight choices follow the silhouette, and the modeler accentuates the muscles that define it.
- check: Black-fill of the model: a fresh agent describes how it would move (heavy, light, graceful) and it matches the brief and the animation set.
- mistake: A graceful motion set on a heavy silhouette, or the reverse [inference].
- examples:
  - R03: big "dad bod" characters; silhouette is central to anatomy (R03:570-575, 602-607, 690-696).
- roblox_fit: Same.
- roles: modeler, animator, art-director, character-rigger, reference-images
- also: character-design, weight-timing
- sources: R03-F28 (R03:570-575, 602-607, 690-696)

### SS-13 Players must track hands, head and feet
- principle: Players must be able to track hands, head and feet and tell head from torso, arms from body, legs and feet apart. On a dark costume use value breaks at the joints to keep parts separable.
- why: Action reads come from the extremities; separable parts make every move legible.
- apply: Plan a value break at each joint that matters (neck, wrists, ankles): skin against dark cloth, light metal against dark leather. Hands and feet get the strongest contrast on the body.
- check: Grayscale capture at the game camera: each extremity has a visible value edge against the neighbouring part (`look_check.py value` with the hand as subject); at thumbnail size the limbs still separate in the silhouette.
- mistake: An all-dark costume where limbs merge.
- examples:
  - R11: Katarina is mostly black leather; her skin tone "ends up being a way to save that element" (R11:112-115).
- roblox_fit: Small phone screens and third-person cameras make extremity contrast more important [inference].
- roles: art-director, modeler, animator, character-rigger, vfx-designer, reviewer, reference-images
- also: value-contrast, character-design
- sources: R11-F08 (R11:112-115)

### SS-14 Nothing hangs in front of the shoulders and arms
- principle: Avoid pieces that hang in front of the shoulders, arms and body (capes, cowls, drapes). Pauldrons mounted on the shoulder are fine; draped pieces are not.
- why: Hanging pieces cover the limbs players track and need delicate animation fixes for the life of the character.
- apply: Modelers keep the shoulder line and arm silhouette clear and mount shoulder pieces on the shoulder, not draped over chest or arm. Riggers flag any drape during rig planning.
- check: Black-fill in key poses (idle, run, attack): the arm's outline stays separate from the torso in each.
- mistake: Cowls and capes draping forward (Yasuo's was "problematic for the longest time").
- examples:
  - R11: Yasuo's cape and cowl (R11:106-111).
- roblox_fit: At phone size an arm hidden by a drape is lost entirely [inference]; also avoids Layered Clothing and cage problems at the shoulder [unverified].
- roles: modeler, character-rigger, animator, art-director, reference-images
- also: character-design, pipeline-production
- sources: R11-F07 (R11:106-111)

### SS-15 Show the hook shapes at the held moments of motion
- principle: About 99 % of the time a fighting character is moving; players see the silhouette at key poses and when the game lingers on a strong hit. Put the hook shapes where those moments show them, and keep a signature shape (a ponytail swoop) visible even when that is not physically exact.
- why: Only held moments are taken in; detail outside them is invisible. The iconic shape identifies the character at a glance.
- apply: Designers add "a little bit of extra silhouette, dynamic shape" at places that face the camera in key poses. Modelers and riggers make the signature element controllable. Animators hold key poses and hit-pauses where those shapes face the camera and keep the signature shape out of overlap with the body. VFX does not cover them on the held frame.
- check: Take the key-pose and hit-pause frames (from `clip_check.py` samples or captures), black-fill them at thumbnail size: the character type, hook shape and signature element read in each.
- mistake: Investing in detail that is never seen; letting physical correctness hide the signature shape.
- examples:
  - R11: "if we ever ... linger on a moment to make a certain hit feel stronger, those are the things that you really see" (R11:179-187).
  - R04: "seeing that that ponytail swoop is there is more important than it being perfectly on the correct side all the time" (R04:700-708).
- roblox_fit: Phone screens and busy servers shrink characters further [inference].
- roles: art-director, modeler, animator, vfx-designer, character-rigger, reviewer, reference-images
- also: character-design, weight-timing, vfx-reads-timing
- sources: R11-F14 (R11:179-187); R04-F32 (R04:700-708)

### SS-16 Break symmetry with one asymmetric element
- principle: Add an accessory or cut on one side to break a fully symmetric design.
- why: Asymmetry adds interest and helps read the character's orientation.
- apply: Character and prop briefs include at least one asymmetric element large enough to see at the game camera.
- check: Mirror the render horizontally and compare at the game camera: the difference is visible.
- mistake: A fully symmetric costume.
- examples:
  - R01: an accessory on one arm and an asymmetric cut in the jacket (R01:277, 305-306).
- roblox_fit: No change; an asymmetric texture also breaks mirrored-UV savings, so put asymmetry in geometry or a separate decal [inference].
- roles: modeler, art-director, reference-images
- also: rhythm, character-design
- sources: R01-F19 (R01:277, 305-306)

### SS-17 Repeat one motif at several scales
- principle: Carry one motif or story symbol across the design at big, medium and small scale (silhouette, part, detail) and across the set (costume and weapon, item, icon, effect). The audience reads the story subconsciously.
- why: Repetition makes parts feel like one design and builds a recognisable family.
- apply: Pick one motif and place it at big (silhouette), medium (grip, stock, trim) and small (trigger, decal) scale; prop briefs list the costume motifs to reuse; use the same motif in UI icons, VFX shapes and marketing for the set.
- check: Count motif uses per asset: target at least 3 scales; a reviewer finds the motif in the silhouette, a part and a small detail.
- mistake: The motif appears once, as a sticker [inference].
- examples:
  - R01: harlequin diamonds in the lapel and the gun barrel; gold filigree shared (R01:373-379, 502-504).
  - R12: Kia's tiger-nose grille, Bugatti's horseshoe, falcon wings; the thunderbolt in shoulder line, grip, stock and trigger (R12:92-103, 152-166, 184).
- roblox_fit: A motif repeated across a pet, weapon or item set makes collections read in the shop [inference].
- roles: art-director, modeler, reference-images, ui-ux-designer, vfx-designer, marketing, environment-designer
- also: style-identity, character-design
- sources: R01-F25 (R01:373-379, 502-504); R12-F09 (R12:92-103, 152-166, 184)

### SS-18 Build motifs from a few basic shapes, abstracted, never a 1:1 copy
- principle: Break a complex motif into a few basic shapes, fit them to the form's perspective, and abstract them: cut, use part of it, add weight, harden angles. It must still read as the motif without looking pasted on.
- why: Basic shapes read at distance and are fast to build; abstracted motifs integrate with the object and read as design, not as a sticker.
- apply: Modelers build ornaments from a short list of primitives; reference prompts ask for "a simple stylised lion head of few bold shapes" or use the motif's angle and rhythm; reject literal pasted symbols.
- check: Count the shapes in the motif; at the game camera the motif still reads as its subject in black-fill at mid distance; reviewer question: "integrated or sticker?"
- mistake: A literal copy of the symbol.
- examples:
  - R01: a lion head of nose, teeth, eyes, ears, mane and jaw, the barrel extending from its mouth (R01:620-622, 978-986).
  - R12: the thunderbolt trigger with weight added and a hard angle: "much stronger but still, it is a thunderbolt" (R12:175-180, 198-201, 238-242).
- roblox_fit: Few shapes fit low triangle counts [inference].
- roles: modeler, art-director, reference-images, vfx-designer, ui-ux-designer
- also: exaggeration, style-identity
- sources: R01-F53 (R01:620-622, 978-986); R12-F16 (R12:175-180, 198-201, 238-242)

### SS-19 Design the group silhouette
- principle: A group is its own silhouette, different from a single figure. Stage groups so the combined outer shape tells the story (survivors back to back, surrounded by small repeated threats).
- why: The group's outer shape carries the idea before any face does; encirclement reads as danger.
- apply: For group shots (marketing art, cutscene frames, lobby and podium poses), design the group's combined silhouette first; surround it with smaller repeated threat shapes where danger is the point.
- check: Black-fill the group at thumbnail size: the combined shape reads as a team, and the threat ring reads around it.
- mistake: Characters lined up with no group shape [inference].
- examples:
  - R05: "the sole survivors" silhouetted back to back fighting zombies, tiny zombies added coming toward them (R05:154-156, 246-259).
- roblox_fit: In gameplay, encirclement reads from shape and count; keep NPC and particle counts within the performance budget [unverified].
- roles: art-director, marketing, film-director, animator, level-design, game-designer
- also: composition-focus
- sources: R05-F07 (R05:154-156, 246-259)

### SS-20 Backdrop pieces: simple surfaces, elegant gesture
- principle: Players do not inspect plants and backdrop pieces; keep their texture and geometry simple but give them an elegant, clear gesture that reads from afar and in peripheral vision.
- why: Backdrop elements must not grab attention, but gesture is read even at a glance.
- apply: Vegetation and backdrop props: low triangle count, flat or simple textures; invest in curve and silhouette direction; any sway motion follows the same gesture [inference for motion].
- check: Black-fill of plants at the game camera: each gesture is a clear curve, not a blob; triangle count well below the hero prop's.
- mistake: Over-detailed plant textures; stiff plant shapes.
- examples:
  - R13: plants painted simply with a strong gesture (R13:404-420).
- roblox_fit: Cheap foliage helps phone budgets (meshes max 20,000 triangles each: knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34; backdrop pieces far below that).
- roles: environment-designer, modeler, art-director, animator, level-design, reference-images
- also: visual-hierarchy, world-level-readability
- sources: R13-F18 (R13:404-420)
