---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, vfx-designer, sound-designer, ui-ux-designer, film-director, environment-designer, modeler, marketing, reference-images, character-rigger, reviewer, qa-lead, game-designer, level-design]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Value and contrast

How light and dark (value) and every other kind of difference decide what the eye sees first, and how 3D form reads from shading.
VC-01 to VC-03 are the base rules (contrast, value before colour, value not line). VC-04 to VC-08 spend contrast on purpose across a screen, a layer or a character. VC-09 to VC-13 make form read from shading. VC-14 to VC-17 are composition-level value rules.
Related: hierarchy and restraint in `visual-hierarchy.md`; colour and light in `light-colour.md`.
Lines marked (DS) in VC-02, VC-04, VC-06 and VC-07 were added in stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### VC-01 Fix a weak read with contrast, not detail
- principle: Everything that makes something stand out is a contrast: value, hue, saturation, shape, size, position, layout, motion, and in sound loudness and timbre. When something does not read, find the missing contrast and add it; do not add detail.
- why: Perception notices differences, not absolute values. Added detail adds noise and usually lowers the contrast that was there.
- apply: For each focal item, name the contrasts it must win against its surroundings (for example: brighter than the ground, more saturated than the walls, the only round shape among boxes). If the read fails, change one of these, not the amount of detail. Sound designers use the same rule: a quiet moment before the loud cue, a unique timbre for the important cue.
- check: Write a "contrast list" for the focal item in the review: for each type (value, hue, saturation, shape, size, position, motion) say whether it wins, ties or loses against its surroundings at the game camera. At least one must clearly win [inference]; a fix that only adds detail fails.
- mistake: Fixing a weak read by adding more detail or more parts.
- examples:
  - R00a: the host lists shape, colour, saturation, size, layout and position as contrasts, and says sound, music and narrative use contrast too (R00a:236-252).
- roblox_fit: No custom shaders, so contrast comes from Color, Material, SurfaceAppearance, Lighting, Highlight, size and motion. Phones shrink everything, so size and value contrasts carry more of the read than fine colour shifts [inference].
- roles: art-director, vfx-designer, sound-designer, ui-ux-designer, film-director, environment-designer, modeler, level-design, reviewer
- also: visual-hierarchy, sound
- sources: R00a-F06 (R00a:236-252)

### VC-02 Values first, colour second; keep a grayscale proof at every step
- principle: Solve form and read in grayscale first. Add colour in a way that keeps the approved values. Glow, bloom and juicy highlights come last, on top of a value structure that already works.
- why: Value carries form and the read. Separating value from colour makes each problem simpler, and colour or glow cannot hide a weak structure. Without a solid value structure, highlights "will not hold up" (R13:424-426).
- apply: Every review step includes a grayscale capture at the game camera. Reference-images: ask first for a value or grayscale version of a chosen design, then colour it while keeping values. Modelers and environment designers: compare the grayscale of the coloured render with the approved grayscale before adding Neon, emissive, Bloom or ColorCorrection. VFX: judge the effect's grayscale peak frame before tuning colour.
- apply (DS): In Studio, a ColorCorrectionEffect with Saturation -1 under the Camera gives the grayscale view, and a BlurEffect with Size raised until fine detail disappears gives the squint view (record the Size used) (knowledge/external/roblox-creator-docs/_api-reference/classes/ColorCorrectionEffect.yaml:78-84; _api-reference/classes/BlurEffect.yaml:31-36; DS:vfx-design/references/review.md:33-34).
- check: `look_check.py value` on the grayscale of the coloured version against the approved value version: the subject/ring median ratio does not drop and the focal area still holds the strongest contrast. Re-take the capture with Bloom and ColorCorrection off: if the read only works with them on, fail.
- mistake: Picking colours that silently change the value structure; adding glow and dodge highlights to hide weak values.
- examples:
  - R10: forms in black and white, then colour on an overlay layer that keeps the values; loose values make colour exploration fast (R10:279-285, R10:506-527, R10:924-926).
  - R13: colour-dodge highlights are "a fancy statue on top"; a grayscale proof on one hotkey (F1), checked constantly (R13:424-440).
- roblox_fit: Studio tone mapping, Lighting and ColorCorrectionEffect change final values (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:78-84), so measure in-game captures, not textures or Blender renders alone.
- roles: art-director, reference-images, modeler, environment-designer, vfx-designer, ui-ux-designer, marketing, reviewer, qa-lead
- also: light-colour, process-iteration
- sources: R10-F12 (R10:279-285, 506-527, 924-926); R13-F19 (R13:424-440)

### VC-03 Separate parts by value and shape, not by lines
- principle: Think in bold shapes and value relationships. Lines are useful early to find shapes, but final designs separate parts by value structure and describe how form turns with value changes. A thick outline is a stand-in, not a solution.
- why: At game size, lines and fine detail disappear; shape and value survive. A modeler reads planes from value changes, not from outlines: "you are working on a 2D image, but you are trying to tell the story in 3D" (R13:249-273).
- apply: Reference-images: once a design is chosen, ask for "painted, form described by light and shadow, no outlines". Modelers: separate parts by material value, not by an outline or a Highlight. UI and VFX: separate elements by value blocks, not hairlines.
- check: View the reference or capture in grayscale with outlines removed or ignored: every main part and every main plane change is visible as a value step. If form exists only in outlines, request a value pass before modelling. In Studio, turn any Highlight off: parts must still separate.
- mistake: Getting bogged down in line and fine detail that "starts to muddy things" (R01:156, 188-190); keeping heavy line work into the 3D stage.
- examples:
  - R01: thumbnails without line; merge and paint instead of delineating; form and value are paramount at the far camera (R01:152-160, 384-390); a thick outline added only for lack of time (R01:555-559).
  - R13: a line on a rock suggests a face turning; it is repainted as a value change (R13:249-273).
- roblox_fit: Highlight outlines a whole model, never internal parts (knowledge/external/roblox-creator-docs/_api-reference/classes/Highlight.yaml:86). Phone screens make characters smaller than League's, so shape and value matter more [inference].
- roles: art-director, reference-images, modeler, environment-designer, vfx-designer, ui-ux-designer
- also: shape-silhouette, references-ideation
- sources: R01-F06 (R01:152-160, 384-390); R13-F10 (R13:249-273); R01-F34 (R01:555-559)

### VC-04 Make one spot the focus by lowering contrast everywhere else
- principle: To focus the eye, first lower the contrast of everything that is not the focus, then (if still needed) raise the focus. Name one or two focal zones; the space between them gets fewer details and lower contrast. Background detail is blocked in with values close to the background's own.
- why: In a field of equal high contrast nothing stands out (the checkerboard). Lowering the surroundings makes the focus win without making it louder.
- apply: Brief names 1-2 focal zones per asset, screen or shot. Environment, secondary props, background UI and the space between focal zones keep a narrow value range and lower saturation. Reference-images prompts ask for "a quiet, low-contrast background and one high-contrast focal point". Do not boost the hero until the surroundings have been calmed.
- apply (DS): Lower contrast in time as well: dim or pause competing effects just before a big payoff so the peak has a quiet baseline to beat (DS:vfx-design/references/scene-and-clutter.md:162).
- check: `look_check.py value` with the focal item as subject: the subject has the widest luminance spread (p5-p95) and the ring around it a clearly narrower one. Grayscale at thumbnail size: the eye lands on the named focal zone first. Fail if detail and contrast are spread evenly (for example along a whole arm).
- mistake: Raising contrast on everything (a full checkerboard); busy, high-contrast backgrounds that pull the eye.
- examples:
  - R00a: a checkerboard where every other square loses contrast, so the centre square becomes the focus (R00a:261-285).
  - R08: background detail as "very low contrast brush strokes" close to the background values (R08:525-528).
  - R11: bright silver shoulder spikes against a dark jacket as the focal point, the arm length simplified (R11:315-324).
- roblox_fit: Atmosphere Density and Offset lower distant contrast globally (knowledge/external/roblox-creator-docs/environment/atmosphere.md:29, 46). Gameplay backdrops on phones must stay calm the same way [inference].
- roles: art-director, environment-designer, vfx-designer, ui-ux-designer, marketing, film-director, reference-images, modeler, level-design
- also: composition-focus, visual-hierarchy
- sources: R00a-F07 (R00a:261-285); R08-F22 (R08:525-528); R11-F26 (R11:315-324)

### VC-05 Give each screen layer its own value and saturation band
- principle: Keep each layer in its own value and colour range. Environment avoids the darkest darks and lightest lights and sits in one controlled saturation band; characters get a little more range; UI and VFX own the extremes. No pure black in the environment.
- why: The layer with the widest value range wins attention, so UI and VFX read over characters, and characters over the environment. An uncontrolled environment palette raises noise everywhere and hides "a character coming out" (R09:634-635).
- apply: The art bible sets the bands per game. PROPOSAL defaults [inference; the sources give no numbers]: environment 15-85 % value, characters 8-92 %, UI and VFX 0-100 %; environment saturation clearly below character saturation. Environment designers build a material zoo (one sample block per material in one Studio place) and check every material against the band before use. Tune Lighting, materials and textures so the environment never reaches pure black or white.
- check: `look_check.py value` on game-camera captures with masks per layer (environment vs characters vs effects): environment p5/p95 inside its band, VFX and UI own the extremes. `look_check.py palette` on a capture of the material zoo: every material inside the set saturation range. Fail on any pure black in the environment.
- mistake: An environment that uses the full value range and competes, so players "just look at a mess" (R13:760); "if I start using black ... can't do that" (R02:818-820).
- examples:
  - R02: a hard Riot rule: VFX highest whites, then characters, then environment clamped, no pure black (R02:804-828).
  - R13: dozens of units, VFX, UI and cards scream for attention; environment keeps a "buttery, creamy" mid range (R13:749-790).
  - R09: one saturation and value band for all environment materials, checked in an asset zoo of material cubes (R09:624-635).
- roblox_fit: Tone mapping and ColorCorrection Contrast and Saturation change final values (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:83-84, 124), so measure in-game captures. MaterialVariant lets the zoo hold custom materials (knowledge/external/roblox-creator-docs/_api-reference/classes/MaterialVariant.yaml:5). Phone screens and outdoor glare compress contrast, so keep margin between bands [inference].
- roles: art-director, environment-designer, vfx-designer, modeler, character-rigger, ui-ux-designer, game-designer, level-design, reference-images, reviewer, qa-lead
- also: visual-hierarchy, light-colour, world-level-readability
- sources: R02-F34 (R02:804-828); R13-F31 (R13:749-790); R09-F32 (R09:624-635)

### VC-06 Test every character against every background
- principle: As the roster and the world grow, new characters can blend into old backgrounds and small gameplay objects get lost on detailed walls. Check every character against every environment, and every new environment against the existing characters.
- why: If a player blends into the background "you can't even track this person"; detail plus effects overload the eye (R09:988-1017).
- apply: The art director keeps a register of character and environment value and colour ranges [inference]. Modelers and riggers deliver character renders for the check; environment designers deliver game-camera captures of each area. Roblox players wear any avatar colours, so environments avoid matching common avatar colours at player height [inference].
- check: Capture each character (and a few common avatar colourings) in each environment at the game camera; `look_check.py value` subject/ring median ratio per pair; place the smallest gameplay object (pickup, projectile) on the busiest wall and floor: it must be found in a thumbnail-size view. Any pair that fails is a ticket.
- check (DS): Critical markers (danger edges, pickups, objective markers) reach at least about 3:1 luminance contrast against the lowest-contrast local background on every stage (the WCAG non-text contrast floor, per DS; its transfer to games is [inference]) (DS:vfx-design/references/scene-and-clutter.md:46, 115).
- mistake: Hunting a small dart on a "super realistic brick wall" (R09:1003-1005).
- examples:
  - R09: characters blending in make you "go cross-eyed"; a Sova dart lost on realistic brick (R09:988-1017).
- roblox_fit: Avatars are player-chosen and change every session, so test against a set of typical avatar colours, not only the game's own characters [inference].
- roles: art-director, environment-designer, character-rigger, modeler, vfx-designer, reviewer, qa-lead
- also: world-level-readability
- sources: R09-F48 (R09:988-1017)

### VC-07 Reserve white, black and the highest contrast for small focal spots
- principle: Save the value extremes. Pure white (and pure black) are the strongest accents; give them only to small, important spots. Highlights are "the smalls" at the biggest contrast; big shapes are the canvas. Effects must not blow out to white; full white everywhere is "like a flash bang" (R06).
- why: The eye goes to the highest contrast; kept small, it makes a focal point. Overused, white erases colour, hurts readability and tires the eye.
- apply: VFX: limit clipped white to the single focus point at the peak; additive layers sum toward white, so count the emitters stacked at the core. Modelers: brightest and most saturated accents (gold, emissive, Neon) on small areas only, against a calmer base. UI: one white or brightest element per screen region.
- check: Capture the peak frame or the hero view; `look_check.py value`: clipped-white pixels (and the top 5 % of luminance) cluster on the intended small accent only. Fail if the clipped area covers a large shape or if two places compete.
- check (DS): Set BloomEffect.Threshold so only focus-tier pixels bloom (1 blooms only pure white, 0 blooms everything) and capture with Bloom on and off: no ambient surface glows (knowledge/external/roblox-creator-docs/_api-reference/classes/BloomEffect.yaml:75-80; DS:vfx-design/references/scene-and-clutter.md:145).
- mistake: Six additive dots spawned on top of each other caused a white blowout (R06:170); highlight colour spread over large areas.
- examples:
  - R06: a teal additive glow over alpha clouds blew out to white; reduced to one dot (R06:163-170, 203, 262).
  - R12: gold highlights as the smalls on a dark blue body; "one of them it's like a canvas, another one, it's like your actual painting" (R12:298-303).
- roblox_fit: LightEmission 1 is additive and overlapping additive particles brighten toward white (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:257); Bloom and Neon spread highlights further [unverified for Neon], so keep them small.
- roles: vfx-designer, art-director, modeler, environment-designer, ui-ux-designer, reference-images, reviewer
- also: visual-hierarchy, light-colour, vfx-reads-timing
- sources: R06-F15 (R06:163-170, 203, 262); R12-F25 (R12:298-303)

### VC-08 Head, shoulders and hands carry the character read; quiet the lower body
- principle: Spend the most value contrast, saturation and refinement on the head, face, shoulders, hands and held item; push the lower body back (a little darker, less saturated, weaker highlights). A white costume keeps true white on top and a muted tint below. The lower body must still separate from the ground.
- why: Competing focal areas make a character "confusing and distracting" (R03); the head and shoulders carry identity, and legs that compete pull the eye away.
- apply: Restated for Roblox (R01 and R03 paint for League's high top-down camera; keep the principle, not the camera rule): in a third-person camera behind and above, the player sees their own head, shoulders, back and held item most, and other players' heads and torsos at distance [inference]. Material plan for every character: upper-body materials lighter or higher contrast; lower-body light colours shifted darker and cooler. PROPOSAL default: lower-body mean value 15-20 % below upper body [inference]. VFX briefs do not cover the head and shoulders [inference].
- check: Grayscale capture at the game camera over the real ground; `look_check.py value` with an upper-body mask and a lower-body mask: upper median brighter and higher contrast than lower; lower body still separates from the ground (subject/ring ratio for the legs above 1). Check a back view, since the third-person camera shows the back.
- mistake: Equal brightness top to bottom; a skirt "grabbing too much attention" from the face, shoulders and hair (R03:1064-1066).
- examples:
  - R01: gold epaulets, lapel and face bright, pants and boots darker on the ringmaster (R01:160-162, 363-371, 435-439, 561-568); Star Guardian Ezreal's lower-body "white" is a dark lilac blue (R01:563-568).
  - R03: shoulders, head, face and hair grab attention in League (R03:740-744, 958-962); push back below the waist, Cafe Cutie Soraka critique (R03:948-956, 1056-1070).
- roblox_fit: Ground colours vary per game; check against the game's real terrain. Avatars change per player, so this rule binds the game's own characters, NPCs and outfits it sells [inference].
- roles: art-director, modeler, reference-images, environment-designer, vfx-designer, reviewer, qa-lead
- also: visual-hierarchy, character-design
- sources: R01-F07 (R01:160-162, 363-371, 435-439, 561-568); R03-F41 (R03:948-956, 1056-1070); R03-F33 (R03:740-744, 958-962); R01-F35 (R01:563-568)

### VC-09 Form shadows make a still object read as 3D
- principle: A player who sees a small or still object cannot rotate it; it reads as 3D only if its shading turns with its planes. The first pass on flat colour is form shadow (ambient occlusion plus shadow and highlight that follow the planes). A quick pass is enough to make a concept feel holdable.
- why: We read depth from shading. Form shading also tells how an object is held and what it is made of.
- apply: In Blender, bake AO and multiply it softly into the base colour (SurfaceAppearance ColorMap) as a start; then add plane-following light and shadow (top light, darker undersides) on stylised assets; adjust by hand logic (VC-10, VC-11). Icon renders and thumbnails keep form shadows. Concept renders: one key light and soft shadows.
- check: Grayscale capture at game size with the model not moving, and one unlit (flat) render: can you tell round, convex and concave forms without rotating? Flat-looking areas fail.
- mistake: Relying on the turnable 3D view and leaving the texture flat (R03:182-186); flat-colour concepts that hide form.
- examples:
  - R03: an AO pass over Caitlyn's flat colours; a player at a glance cannot tell it is 3D without form shadows (R03:88-94, 178-186).
  - R02: shadows "punch up the forms"; turning the fox cheek (R02:240-246, 946-950).
  - R12: darken layer, mask, shadows on rounded parts, blur: enough to show how the gun is held (R12:366-382).
- roblox_fit: Roblox computes shadows live but not small-form AO; baked shading in the colour map still helps on phones and at low graphics quality [inference] [unverified].
- roles: modeler, environment-designer, art-director, character-rigger, ui-ux-designer, marketing, reference-images
- also: materials-detail, light-colour
- sources: R03-F06 (R03:88-94, 178-186); R02-F14 (R02:240-246, 946-950); R12-F33 (R12:366-382)

### VC-10 Shade with a clear terminator, shadows only where the form turns away
- principle: The terminator is the line where light turns to shadow; its shape describes the curvature. Show form by placing shadow only where the shape hides from the light, and keep that edge readable.
- why: Minimal, well-placed shadow reads cleaner than full rendering, and the terminator alone tells round from flat.
- apply: In painted shading and in Studio lighting, keep the light-to-shadow edge on major forms visible at game size: one key direction (see LC one light direction), shadows on the far side of forms only, no extra mid-tone noise across lit planes.
- check: Grayscale capture at the game camera: on every major form the light/shadow edge is visible and follows the form (curved on cylinders, straight on boxes). Fail where the edge is lost in noise or soft everywhere.
- mistake: Rendering every surface with gradients so no clear terminator remains [inference].
- examples:
  - R03: the letter A lit from one side; shadows only where the shape hides from the light (R03:542-558).
- roblox_fit: Same rule; Lighting's sun direction sets the live terminator, so check it at the game's real time of day.
- roles: modeler, art-director, environment-designer
- also: light-colour, materials-detail
- sources: R03-F25 (R03:542-558)

### VC-11 Paint contact shadows where parts touch
- principle: Where one part rests on another (strap on chest, plate on plate, prop on ground) put a thin dark shadow at the contact. It brings out forms remarkably.
- why: Contact shadows separate layers and tell the eye that one part sits on another.
- apply: Short-distance AO bake, or a painted dark seam under overlapping parts (belts, straps, armour plates, props on the ground). Environment designers do the same where props meet floors and walls.
- check: Grayscale capture at the game camera: every overlap and every object-ground contact has a thin dark seam. Fail on parts that look pasted on.
- mistake: "forgetting about contact shadows" (R03:534-536).
- examples:
  - R03: ribbons and armour pieces gain form from contact shadows (R03:532-541).
- roblox_fit: Live shadows do not show small contacts at distance [inference] [unverified]; bake or paint them.
- roles: modeler, environment-designer, art-director, vfx-designer
- also: materials-detail
- sources: R03-F24 (R03:532-541)

### VC-12 Shade parts as simple forms (cylinder, sphere, box, ribbon)
- principle: Read each part as a basic form and shade it that way: arms are cylinders with highlights on top; ribbons round toward the viewer with the sides pushed back; hair on the shoulder is highlighted and its ends pushed back.
- why: Simple forms read clearly at distance; complex shading that ignores the base form reads as noise.
- apply: Before shading a part, name its base form; shade the form, then add detail. Parts the player always sees (arms of a character holding a weapon in a third-person view) get the cleanest forms.
- check: Grayscale capture at game size: limbs read as cylinders, the head as a sphere, plates as planes; ribbon and hair ends are darker than their middles.
- mistake: Shading surface detail before the base form [inference].
- examples:
  - R03: Caitlyn's arms, ribbons and hair; arms matter for a character who always holds a gun (R03:1024-1043).
- roblox_fit: Same.
- roles: modeler, art-director, reference-images
- also: shape-silhouette, materials-detail
- sources: R03-F44 (R03:1024-1043)

### VC-13 Big soft shading first, then commit with sharp, high-contrast accents
- principle: Start soft: general shading with a big soft brush, forms kept flexible. Later commit to chosen shadows and creases with small, sharp, higher-contrast marks. Small creases sit on top of the big value groups, never break them.
- why: Large soft forms set the read and stay easy to change; committed contrast at the end gives punch.
- apply: Texture order: large-radius AO and broad form light first, then a short-radius crease or cavity layer, then raise contrast on chosen forms. Review passes: the early pass checks form only; the late pass checks that contrast was committed.
- check: Compare first-pass and final grayscale captures: the final has a wider value range (`look_check.py value` p5-p95 spread larger) and the big value groups are unchanged at thumbnail size.
- mistake: Staying soft and low-contrast at the end [inference]; small creases that break the big value groups.
- examples:
  - R03: general AO with a big soft brush, then a small brush for creases and wrinkles (R03:500-504); start soft with hair and body, later harsher values in her hair (R03:712-718).
- roblox_fit: Small creases may vanish at 1024 px textures (knowledge/external/roblox-creator-docs/art/characters/creating/texturing-setup.md:45); paint them bolder. Phones need more contrast at the end [inference].
- roles: modeler, art-director, environment-designer, reference-images
- also: materials-detail, process-iteration
- sources: R03-F21 (R03:500-504); R03-F31 (R03:712-718)

### VC-14 Group detail in close values; frame the group with the strongest colour
- principle: Materials close in value read as one object (glass, brass and white); a contrasting base colour frames that group, so the object does not break into parts and its borders are clear.
- why: Value grouping unifies; a framing value defines the boundary of the composition.
- apply: Put the detail materials of an asset into one close-value family; use the base colour as a contrasting frame around that family. Same for UI cards (content group inside a contrasting frame).
- check: Grayscale capture: the detail cluster sits inside a narrow value band (`look_check.py value` on the cluster mask), and the frame's median is clearly different. Fail if the asset reads as many separate pieces.
- mistake: Many contrasting parts that break the object apart [inference].
- examples:
  - R12: blue frames the glass, gold and white details of the skin (R12:338-347).
- roblox_fit: No change.
- roles: art-director, modeler, ui-ux-designer, environment-designer, marketing, reference-images
- also: light-colour, composition-focus
- sources: R12-F29 (R12:338-347)

### VC-15 Space high-contrast features like letters in a word
- principle: Contrast needs the right spacing. High-contrast features packed too close become a pattern you cannot read; one isolated outlier pulls the eye and clutters the composition.
- why: Grouping depends on spacing: too dense reads as texture, too sparse as unrelated pieces.
- apply: Space lights, emissive strips, decals, rivets and UI badges at deliberate intervals; avoid dense repeats of tiny high-contrast marks and single outliers far from the group.
- check: Thumbnail-size view (`look_check.py thumb`): high-contrast features read as distinct but grouped; no zone turns into a shimmering pattern; no single bright mark sits alone away from the focal zone.
- mistake: Too-dense contrast details that read as pattern; one outlier contrast that steals the eye.
- examples:
  - R12: letters A and B repeated close and far: too close is a pattern, too far is not a word (R12:328-337).
- roblox_fit: On phones dense small contrast becomes shimmer and aliasing [inference].
- roles: art-director, ui-ux-designer, modeler, environment-designer, vfx-designer, reviewer
- also: visual-hierarchy, rhythm
- sources: R12-F28 (R12:328-337)

### VC-16 Balance visual weight on purpose
- principle: Dark, heavy masses pull the composition to their side. Place a brighter mass on the other side so the balance sits where you planned (usually near the centre).
- why: Unbalanced weight feels off and distorts the read of proportions.
- apply: On a side render of a prop or weapon, a UI screen or a thumbnail, distribute dark and bright masses so the value centre sits where intended.
- check: Grayscale render: compare the darkness-weighted centre of mass with the object or frame centre [inference: measurement method]; flag a large offset that was not planned.
- mistake: All the dark mass on one end.
- examples:
  - R12: a dark stock pulled the weight right; the front was made a bit brighter and the back a bit darker (R12:308-316).
- roblox_fit: No change.
- roles: art-director, modeler, environment-designer, ui-ux-designer, marketing, film-director
- also: composition-focus
- sources: R12-F26 (R12:308-316)

### VC-17 High contrast for dramatic moments, lower for calm ones
- principle: Value contrast reads as intensity. Push it for dramatic, hardcore moments; keep calm scenes lower.
- why: Strong value contrast signals tension and weight; the same contrast everywhere loses that meaning.
- apply: Boss rooms, climax shots, reveal moments and dramatic promo art push value contrast (deep shadows and bright accents); hubs and calm scenes use a narrower range. Film directors plan contrast per beat.
- check: `look_check.py value` p5-p95 spread per shot or area: dramatic shots use both ends strongly; calm shots measurably narrower.
- mistake: Using the same contrast for every moment [inference].
- examples:
  - R05: high contrast for trained agents in a hardcore moment (R05:760-766).
- roblox_fit: ColorCorrectionEffect Contrast can shift a scene per moment (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:83).
- roles: art-director, film-director, marketing, environment-designer, vfx-designer
- also: light-colour, composition-focus
- sources: R05-F29 (R05:760-766)
