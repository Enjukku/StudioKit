---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, environment-designer, vfx-designer, ui-ux-designer, game-designer, modeler, reference-images, marketing, film-director, level-design, character-rigger, animator, live-ops-designer, sound-designer, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Light and colour

What colour means and how light shapes form, mood and focus.
LC-01 to LC-06 are colour roles and palettes (reserved gameplay colours, meaning, mood, palette proportions, shared palette, bounce). LC-07 to LC-09 make colour rich (hue-shifted shading, opposite temperatures, no flat fills). LC-10 to LC-16 are light (one direction, light first, light leads the eye, motivated light, good and evil, rim light, fixed shadows). LC-17 to LC-21 spend saturation and colour in effects and characters. LC-22 to LC-25 are the colour review steps.
Related: value rules in `value-contrast.md` (VC-02: value before colour), effect colour technique in `vfx-reads-timing.md`, style in `style-identity.md`.
Lines marked (DS) in LC-01 and LC-19 were added in stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### LC-01 Reserve the gameplay colours; keep them, and fast motion, out of decoration
- principle: Some colours carry gameplay meaning (red = enemy, danger, "you can shoot this"; the route colour; the team colours). Reserve them: decoration and environment do not use them, and environments also avoid fast motion near sightlines. Pair every reserved colour with a shape or outline cue for colour-blind players, and check saturation numerically, not by eye.
- why: A hue no other object uses becomes a code the player learns instantly; red or moving set dressing competes with the danger signal, and a player shot by someone they could not see loses unfairly. An artist's own eye can oversaturate.
- apply: The art bible holds a reserved-colour table (enemy, danger, team, interactable, route) with the hues and the saturation limit allowed in set dressing. Environment and modeling keep large surfaces neutral; reference-images prompts state "neutral environment, no red accents" when red is reserved. A bright hazard that must be red is tamed (LC-18).
- apply (DS): For two sides, pair orange with blue, not red with green; plan for about 8 % of male players with a colour-vision deficiency, to whom red often looks darker (DS:vfx-design/references/scene-and-clutter.md:116; DS:vfx-design/references/elements.md:104, 111).
- check: On an environment-only capture at the game camera (UI, effects and characters off; gameplay objects that may wear the hue excluded by a mask): the share of pixels within a CIEDE2000 distance of each reserved swatch, authored and as rendered in the same capture (target near 0; the owner sets the number; `art-review` `references/look-check.md` §5 line 4); not a `look_check.py palette` cluster, since k-means merges small accents into neighbours (lead fix 2026-10-22: palette clusters passed a small reserved accent; composed captures counted HUD and avatars as decoration); saturation of environment greens and reds measured against the bible. View a capture in a deuteranopia and protanopia simulation [inference]: the danger still reads by shape. Watch a 10 s capture for moving set pieces near sightlines [inference].
- mistake: The signal colour on decoration so it loses meaning; "red is normally a color we try to avoid, and then fast movement is also something we wanna avoid" (R09:60-62); "when I get shot by someone I can't see, that can be rough" (R02:212-214).
- examples:
  - R00a: red enemies in Superhot, red jump spots in Mirror's Edge (R00a:326-336).
  - R02: red is reserved for enemies; he measures how far out his greens are in saturation and tones them back; advocate colour-blind settings (R02:192-216, 438-444).
  - R09: lava is "bright red and it's on fire which is really fast", the hardest element to fit into a VALORANT site (R09:59-63, 820-829).
- roblox_fit: Whatever colour the game uses for enemy or danger Highlights is a reserved hue (Highlight is limited to 255 instances per client: knowledge/external/roblox-creator-docs/effects/highlighting.md:37). No global colour-blind filter was confirmed [unverified], so build paired cues (shape plus colour). Small phone screens give reserved signals fewer pixels, so clashes cost more [inference].
- roles: art-director, environment-designer, vfx-designer, ui-ux-designer, game-designer, modeler, reference-images, level-design, reviewer, qa-lead
- also: world-level-readability, ui-ux, game-design-fun
- sources: R02-F11 (R02:192-216, 438-444); R09-F03 (R09:59-63, 820-829); R00a-F10 (R00a:326-336)

### LC-02 Keep a colour-role table: one hue never means both help and harm
- principle: Choose a colour for what it must say (team, damage type, element, heal, shield, rare, mood), never because it looks nice. One hue must not carry two opposite meanings: poison could be green, but it is purple because green is healing.
- why: Colour is a fast code once learned; players decide in a split second whether to stay or move.
- apply: The art bible holds a colour-role table (heal, damage, poison, shield, buff, rarity tiers, teams). Every effect spec, UI cue and pickup cites the role, not a free colour choice. Add a shape or icon cue for colour-blind players [inference].
- check: List all effects and UI cues by colour role; flag any hue used for both a good and a bad meaning. `look_check.py palette` on captures: effects of the same role share the role hue; team colours stay distinct under the real Lighting.
- mistake: Colours picked because they look nice; green poison next to green healing (R06:192-193).
- examples:
  - R00c: red versus green lasers for teams, element spells for damage type, oversaturated violent fire for tone (R00c:3728-3760).
  - R06: green healing, red damage; poison shifted to purple to avoid confusion (R06:191-193).
- roblox_fit: Team colours must stay readable on small screens and under the game's Lighting and Atmosphere; test there [inference].
- roles: vfx-designer, art-director, ui-ux-designer, game-designer, environment-designer, sound-designer
- also: vfx-reads-timing, ui-ux, game-design-fun
- sources: R00c-F10 (R00c:3728-3760); R06-F18 (R06:191-193)

### LC-03 Colour sets the mood; recolour every reused layer to it
- principle: The same shapes read as a threatening storm in dark navy and as happy "cotton candy" in warm pinks and oranges. A reused layer keeps its old colour and its old mood, so every layer of a combined asset is recoloured to the target mood.
- why: Viewers read emotion from hue and warmth before shape; one off-palette layer reads as a different effect.
- apply: Brief the mood in colour words from the art bible (for example happy = warm pink and orange, menace = dark blue); the reference image states the palette. After combining assets, list each layer's colour against the palette and recolour (thicken a layer if it must read).
- check: Thumbnail and squint view of the capture: the mood reads from colour alone; `look_check.py palette` against the brief's colours flags hues outside the effect palette.
- mistake: Keeping a reused asset's colour ("it doesn't feel very happy. It feels very like lightning storm", R06:107); leaving the reused rain blue (R06:350).
- examples:
  - R06: navy clouds recoloured pink and orange start to feel "cotton candy" (R06:107-110, 124-125, 188-190).
  - R06: the rain changed to purple to match and thickened to 20 (R06:350-353).
- roblox_fit: ParticleEmitter Color is a ColorSequence; Lighting tints particles unless LightInfluence is 0 (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:462-467).
- roles: vfx-designer, art-director, environment-designer, reference-images, ui-ux-designer
- also: style-identity, vfx-reads-timing
- sources: R06-F10 (R06:107-110, 124-125, 188-190); R06-F29 (R06:350-353)

### LC-04 Few colours with roles: about 60 / 30 / 10, after the greys work
- principle: Find the volumes in grey first, then use mostly three colours: a main colour on the big silhouette (about 60 %), supporting colours on mediums (about 30 %), accents on small highlights (about 10 %). For a scene or event, build the palette from the theme words (a dominant hue), keep the brand colour, and bring the complementary accent in through design elements; a scene may commit to one dominant hue.
- why: A clear proportion of colour areas gives hierarchy and reads fast; a dominant hue sets the mood at a glance, the brand colour keeps identity, the complement gives contrast.
- apply: The art bible names palette roles per asset and per scene: dominant (theme), support, accent (complement), brand. Blender material slots are assigned by role. For an event, the whole scene can lean to one hue; Studio's ColorCorrectionEffect TintColor and Saturation can push it (keep gameplay reads intact).
- check: `look_check.py palette` on the render: area share of the top three colours near 60/30/10 (or one dominant hue family covering most of a scene, with brand colour and complement present but unequal); the grayscale still separates the volumes.
- mistake: Picking colours before volumes are settled; equal amounts of many hues so no mood reads.
- examples:
  - R12: a grey block, then mediums, then gold highlights and blue, about 60/30/10 (R12:282-288, 297).
  - R05: Halloween orange and grey, zombie grey-green, VALORANT red kept, the Viper scene "really green", the orange complement "comes in from the design elements" (R05:79, 107-113, 139-141, 231).
- roblox_fit: Roblox lighting shifts colours, so check proportions in a Studio capture, not only in Blender; post effects are global per camera (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:83-85).
- roles: art-director, modeler, environment-designer, ui-ux-designer, vfx-designer, marketing, reference-images
- also: value-contrast, style-identity, visual-hierarchy
- sources: R12-F23 (R12:282-288, 297); R05-F04 (R05:79, 107-113, 139-141, 231)

### LC-05 Take new colours from the palette already in the image
- principle: New colours are picked from those already placed; materials affect each other (red bouncing into gold), so the whole reads as one palette.
- why: A shared palette feels coherent; colours that bounce into each other sit in the same light.
- apply: Each character and environment has a palette in the art bible; new parts sample it; reflective materials pick up neighbouring colours.
- check: `look_check.py palette` with `--roles` set to the bible palette: no cluster far from every role swatch (the delta-E tolerance is set by the art director).
- mistake: Off-palette colours added for a new part [inference].
- examples:
  - R01: red bouncing into the golds (R01:626-631).
- roblox_fit: No change.
- roles: art-director, modeler, reference-images, ui-ux-designer, vfx-designer, environment-designer
- also: style-identity
- sources: R01-F38 (R01:626-631)

### LC-06 Put the environment's bounce colour into character shadows
- principle: Tint shadows on a character with the dominant environment colour (green on Summoner's Rift) so it looks at home in the world.
- why: Shared bounce light integrates character and world.
- apply: Concept and painted shadows take a slight tint of the main environment colour; in Studio, the ambient and bottom colour shift reflect the ground colour.
- check: Capture in game: character shadow pixels carry the environment tint (hue sample against a neutral grey).
- mistake: Neutral grey shadows that make the character look pasted on [inference].
- examples:
  - R01: green bounce painted into costume shadows (R01:602-604).
- roblox_fit: Lighting.ColorShift_Bottom tints surfaces facing away from the sun and Lighting.Ambient tints areas occluded from the sky (knowledge/external/roblox-creator-docs/_api-reference/classes/Lighting.yaml:39-50, 129-140).
- roles: art-director, environment-designer, modeler, reference-images
- also: materials-detail
- sources: R01-F37 (R01:602-604)

### LC-07 Shift hue for shadows and highlights; do not just add black or white
- principle: Shadows are not a darker version of the local colour and highlights are not a whiter one. Shift the hue: some hues are naturally darker (purple) and some brighter (yellow, cyan). A red coat's shadows go toward purple, its highlights toward orange; it still reads red.
- why: Going to black or white kills saturation and makes shading "very boring" and muddy; several hues in one material keep it fresh and are part of a stylised game's charm.
- apply: In materials, palettes, UI gradients and VFX colour ramps: shadow = local colour shifted toward a darker hue; highlight = shifted toward a brighter hue. Reference-image prompts ask for "coloured shadows" or name the shift. In Studio, tint Ambient and OutdoorAmbient instead of leaving them neutral grey.
- check: `look_check.py palette` on lit and shadow samples of the same material: the shadow hue differs from the lit hue by a visible step (not only value), saturation is kept, no greyed shadows.
- mistake: "always going towards white or black" (R03:758-762); "picking the local color and going for a darker version of it" (R13:111-113).
- examples:
  - R03: a red velvet coat with purple shadows and orange highlights (R03:746-789).
  - R13: shrine shadows painted with different hues, not monochrome (R13:111-116).
- roblox_fit: Lighting.Ambient tints sky-occluded areas and OutdoorAmbient outdoor areas (knowledge/external/roblox-creator-docs/_api-reference/classes/Lighting.yaml:39-50, 448-458); ParticleEmitter Color sequences and UI gradients take the same shift.
- roles: modeler, art-director, environment-designer, vfx-designer, ui-ux-designer, reference-images, marketing
- also: value-contrast, style-identity
- sources: R03-F34 (R03:746-789); R13-F06 (R13:111-116)

### LC-08 Light and shadow get opposite temperatures
- principle: Give light and shadow opposite colour temperatures: warm light with cool shadows, or cool (teal) sunlight with warm, juicy shadows. Pick one direction per scene and keep it.
- why: Temperature contrast gives depth, separates light from shadow and breaks monochrome ("everything is just green").
- apply: The art bible sets the direction per scene (for example outdoor: cool light, warm shadows; interior: warmer light). In Studio: tint the sun with ColorShift_Top and the shadow side with Ambient, OutdoorAmbient or ColorShift_Bottom; in materials, push shadow areas toward the opposite temperature; reference prompts name it ("cool light, warm shadows").
- check: Sample lit and shadow pixels of the same material on a capture: the shadow hue sits on the opposite temperature side of the lit hue, as the bible specifies.
- mistake: The same temperature in light and shadow; "everything is just green" (R02:446-448).
- examples:
  - R02: warm light and cooler blue and cyan shadows in greens; the Encanto tree shot (R02:442-450, 594-604, 980-982).
  - R13: teal sunlight with warm shadows on the shrine, as in plein-air painting (R13:646-660).
- roblox_fit: ColorShift_Top tints sun-facing surfaces, ColorShift_Bottom the opposite surfaces, Ambient sky-occluded areas (knowledge/external/roblox-creator-docs/_api-reference/classes/Lighting.yaml:39-50, 129-140, 167-178).
- roles: art-director, environment-designer, modeler, vfx-designer, reference-images
- also: style-identity
- sources: R02-F24 (R02:442-450, 594-604, 980-982); R13-F29 (R13:646-660)

### LC-09 No flat fills: small hue and value shifts inside a material
- principle: Do not fill a material with one colour. Shift hue and value slightly in random patches, because nature is not uniform.
- why: Slight shifts make forms pop and give "happy accidents"; flat fills read sterile and fake.
- apply: In Blender materials mix 2-4 near hues by a noise texture (PROPOSAL default: hue within a few degrees, value within 5-10 % [inference]); in Studio vary Color slightly across neighbouring Parts of the same material, or use MaterialVariant or a SurfaceAppearance ColorMap.
- check: On a PNG capture of one lit side of the surface: the chromaticity spread over small pixel blocks (blind to a smooth light gradient) is above its starting limit and stays inside the colour family; value texture in one hue fails as monochrome and a single flat swatch fails (`environment-craft` `references/measure-captures.md` flat-fill measure) (lead fix 2026-10-22: k-means clusters split by value as well as hue, so a one-hue brick wall gave four clusters and passed).
- mistake: "they are pretty monochromatic ... people don't tend to shift their color wheel ... ever so slightly" (R02:86-94).
- examples:
  - R02: a little red added into the grey stonework (R02:68-74, 84-96, 152-154, 230).
- roblox_fit: Built-in materials are uniform per part; variation comes from per-part Color, MaterialVariant or SurfaceAppearance (knowledge/external/roblox-creator-docs/art/modeling/surface-appearance.md). Keep shifts subtle on phones, where small patches merge.
- roles: modeler, environment-designer, art-director, reference-images
- also: materials-detail
- sources: R02-F02 (R02:68-74, 84-96, 152-154, 230)

### LC-10 One fixed light direction for the whole game, judged at the game camera
- principle: Set one key light direction for the game and never move it during the work; paint and judge every asset as lit from it, at the camera players use. Surfaces facing the light and nearer the camera are brighter; surfaces turned away are darker.
- why: One light "gives the player a good sense of physicality and a good sense of orientation" (R02:134-136), lets the eye read each form, and makes every asset sit in one world. Moving the light means repainting everything.
- apply: Restated for Roblox (R02 and R03 paint for League's high top-down camera; keep the principle): the art bible fixes the sun direction (Lighting.ClockTime and GeographicLatitude) per place; Blender review renders use the same key direction and the real game camera (third-person behind and above, or top-down). Baked highlights and painted AO follow that direction and stay soft, so they do not fight Roblox's dynamic light [inference]. Reference prompts state the light direction.
- check: Render or capture a set of assets together at the game camera: highlights on every object face the same way; up-facing and light-facing planes are the brightest values, undersides darker. Fail any asset with painted light from another side.
- mistake: Shifting the light mid-work: "you're gonna just repaint the whole thing" (R02:750-752); judging only the front view (R03:994-996).
- examples:
  - R02: one top-down light over the whole Rift as the "North Star" (R02:130-136, 248-250, 748-760).
  - R03: "everything facing upwards is gonna be lit" (R03:96-99, 1058-1061).
  - R03: for the game camera, the hat top and nearer golds are brightest (R03:994-1022).
- roblox_fit: Roblox lighting is dynamic; sun height comes from Lighting.ClockTime (knowledge/external/roblox-creator-docs/environment/lighting.md:175-179). A day/night cycle conflicts with baked highlights, so keep painted light soft in games with a moving sun [inference]. Third-person cameras see backs and sides more than League's camera [inference].
- roles: modeler, environment-designer, art-director, vfx-designer, reference-images
- also: value-contrast, materials-detail, composition-focus
- sources: R02-F07 (R02:130-136, 248-250, 748-760); R03-F03 (R03:96-99, 1058-1061); R03-F43 (R03:994-1022)

### LC-11 Block light and shadow first; test lighting options on the rough
- principle: Once the pose or layout is set, the first lighting step is to choose one light direction and block in light, shadow and cast shadows quickly, without caring about clean edges. Test a few lighting scenarios and contrast ratios on the rough before painting or detailing further; special-material lighting (gold, bloom) comes second.
- why: Light decides form, mood and focus, and changing it later is expensive; edges can be cleaned later.
- apply: Make 2-3 lighting variants of the blockout (Blender fixed camera, or Studio Lighting presets) and compare [inference for count]; record the chosen key and fill direction in the brief; only then detail.
- check: Grayscale capture of each variant at the game camera with `look_check.py value`: one clear light direction, readable cast shadows, the focal area holds the highest contrast. Fail a detail pass that starts before the light is chosen.
- mistake: Trying "to get to the perfect edge, the perfect line" at this stage (R13:89-93).
- examples:
  - R13: light from the upper side, cast shadows blocked on the shrine, then airbrush bloom on the golden plates (R13:85-93, 191-199).
  - R08: the sketch moved on for "a lighting test" and "different contrast ratios" (R08:446-450, 472-478).
- roblox_fit: Studio Lighting has one sun or moon direction set by time of day and latitude; choose it early per scene; test at phone-like resolution [inference].
- roles: art-director, environment-designer, modeler, vfx-designer, reference-images, marketing, level-design
- also: process-iteration, value-contrast
- sources: R13-F04 (R13:85-93, 191-199); R08-F18 (R08:446-450, 472-478)

### LC-12 Light leads the eye: the brightest area is the focus
- principle: Light and shadow create focal points. From the first pass, put the lighter values and the strongest local light toward the subject (goal, door, pickup, path) and keep surroundings a little darker toward the edges.
- why: The eye goes to the lightest, highest-contrast area first.
- apply: Environment: ground slightly darker toward the edges, lighter near the landmark or objective; a SpotLight or PointLight with shadows on the key focal point, lower ambient elsewhere. Thumbnails: the lightest area on the hero.
- check: Grayscale capture at the game camera, blurred: the lightest blob sits on the intended focus; `look_check.py value` gives the focus region the top contrast.
- mistake: Even, flat light so nothing leads the eye.
- examples:
  - R00b: spotlights and shadows as compositional elements that lead the player (R00b:1901-1921).
  - R02: lighter greens toward the centre to focus on the fox (R02:74-80).
- roblox_fit: Local lights have Color, Brightness and Shadows (knowledge/external/roblox-creator-docs/effects/light-sources.md:29); many shadow-casting lights cost phone performance [unverified], so use few, at focal points.
- roles: environment-designer, art-director, level-design, film-director, vfx-designer, modeler, marketing
- also: composition-focus, value-contrast, world-level-readability
- sources: R00b-F08 (R00b:1901-1921); R02-F03 (R02:74-80)

### LC-13 Light motivated by the setting
- principle: Decide the light from the setting: outdoors means sky light from above plus a directional sun; a cave, torch or screen glow motivates its own light.
- why: Motivated light feels believable and makes forms consistent.
- apply: Studio: sky light through Ambient and OutdoorAmbient, the sun through ClockTime and GeographicLatitude, local lights only where a source exists. Key art and cutscenes reuse the game scene's light setup.
- check: Every light in the scene has a visible or implied source; shadows across characters and props point the same way; in an outdoor scene top planes are lit.
- mistake: Lights placed only for looks, with no source and conflicting shadows [inference].
- examples:
  - R10: sky top light plus sun for Yasuo fishing outdoors (R10:301-309).
- roblox_fit: Lighting property behaviour: knowledge/external/roblox-creator-docs/_api-reference/classes/Lighting.yaml:39-50, 448-458.
- roles: environment-designer, art-director, marketing, film-director, modeler, reference-images, level-design
- also: composition-focus
- sources: R10-F14 (R10:301-309)

### LC-14 Light direction sets good or evil
- principle: Light from below makes a character look dangerous or evil; light from the side or above reads heroic, like "summoning holy light".
- why: Underlighting is unnatural and threatening; light from above reads natural and divine.
- apply: Villain reveals and boss intros: a low key light from below; heroes and rewards: top or side key.
- check: In the render or capture, name the key light direction on the face and match it to the intended alignment in the brief.
- mistake: Lighting a villain reveal like a hero shot [inference].
- examples:
  - R05: Sage pushed toward the bad guy with bottom light (R05:671-679).
- roblox_fit: The global sun cannot come from below; use a placed PointLight or SpotLight under the character in cutscenes (knowledge/external/roblox-creator-docs/effects/light-sources.md) [inference].
- roles: art-director, environment-designer, film-director, marketing, vfx-designer, level-design
- also: composition-focus, character-design
- sources: R05-F22 (R05:671-679)

### LC-15 Rim light separates figures from the background
- principle: A rim light on foreground characters gives clean shapes and edges, separates them from the background and makes blocky shapes pop.
- why: A bright edge lifts a figure from a similar-value background and confirms its outline.
- apply: Blender promo renders: a back or rim light on foreground characters. In Studio: a placed light behind key characters in cutscenes, or Highlight sparingly as the cheap in-game substitute.
- check: Grayscale capture: foreground silhouettes have a continuous light edge where they overlap a darker background.
- mistake: Blocky shapes left without an edge, losing visual interest (R05:520-521).
- examples:
  - R05: rim light added to Brimstone and others to pop the foreground (R05:520-521, 680-683, 754-760).
- roblox_fit: Highlight is capped at 255 instances per client (knowledge/external/roblox-creator-docs/effects/highlighting.md:37).
- roles: art-director, environment-designer, film-director, marketing, modeler, vfx-designer
- also: value-contrast, visual-hierarchy
- sources: R05-F19 (R05:520-521, 680-683, 754-760)

### LC-16 Fix the light per level and tune shadows for readability
- principle: A fixed sun lets shadows be tuned for gameplay: no key position sits in deep shadow where a player could hide by accident. Shadows are "a big part of gameplay readability".
- why: A shadow that moves or falls badly can hide a player; fixed light also helps performance.
- apply: Fix the time of day per competitive map; place shadows so they do not cover key positions; re-capture readability after every lighting change. Readability must not depend on shadows alone, because phones lower shadow quality.
- check: Grayscale capture of each key position with a character standing in it: the character separates from its background in value (`look_check.py value` subject/ring ratio); repeat at a low graphics-quality setting.
- mistake: A lighting change shipped without a readability re-check [inference].
- examples:
  - R09: VALORANT's static lighting with tuned shadows, re-baked after changes (R09:660-667).
- roblox_fit: Roblox lighting is real-time with no bake step [inference: none found in the mirror]; keep Lighting.ClockTime fixed (knowledge/external/roblox-creator-docs/_api-reference/classes/Lighting.yaml:99), choose Lighting.Technology (Lighting.yaml:585); shadow quality drops with client graphics quality (knowledge/external/roblox-creator-docs/performance-optimization/improve.md:419).
- roles: environment-designer, art-director, level-design
- also: world-level-readability
- sources: R09-F35 (R09:660-667)

### LC-17 Calm the field, pop small saturated accents
- principle: Saturation is relative. Desaturate the large areas a little and let small saturated pops sit on the focal spots; even a small saturated accent on a background figure pulls the eye to it.
- why: A calmer field makes small saturated spots draw the eye, even far back.
- apply: Large areas (ground, sky, background crowd) at lower saturation; saturated colour only on focal spots, pickups, effects, and one small accent on a background figure or landmark you want found.
- check: `look_check.py palette`: saturated pixels are a small share and sit on focal elements; at thumbnail size each intended accent is visible and leads to its figure.
- mistake: Saturation spread evenly, so nothing pops [inference].
- examples:
  - R05: greens desaturated with "different little pops of green" (R05:493-497); Sage's earrings made saturated green to pop her from the background (R05:906-910).
- roblox_fit: ColorCorrectionEffect Saturation lowers the whole frame (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:84); per-part colour or Neon gives the pops [unverified for Neon].
- roles: art-director, environment-designer, vfx-designer, marketing, modeler, character-rigger
- also: visual-hierarchy, value-contrast
- sources: R05-F18 (R05:493-497); R05-F38 (R05:906-910)

### LC-18 Keep the player band neutral; tame bright hazards
- principle: When a hazard or warm material is too bright, tame it (shift red toward orange, lower its emission). To fit strong colour into a play space, run a gradient: neutral at ground and player height, more saturated higher up.
- why: Saturation near player height competes with enemies; higher up it adds colour without hurting the fight read.
- apply: The most saturated environment colour sits above head height; the player band (floor to head height) stays neutral; hazard brightness is tuned until characters in front of it still separate [inference on the band].
- check: On an environment-only capture (UI, effects and characters off), with boxes below the horizon so the sky stays out of the upper band: saturation (chroma) in the player-band box lower than in the box above head height (`art-review` `references/look-check.md` §5 line 5) (lead fix 2026-10-22: on composed captures 12 avatars moved the player band from 12.0 to 47.2 with no error); `look_check.py value` with a character in front of the hazard: the character still separates.
- mistake: "Oh my God, whoa, it's so bright" (R09:806): a hazard emissive overpowering the scene.
- examples:
  - R09: lava made "a little bit more orange"; the brick goes from neutral beige to saturated orange higher up (R09:806-819, 830-835).
- roblox_fit: Neon material and particle Brightness (knowledge/external/roblox-creator-docs/_api-reference/classes/ParticleEmitter.yaml:78) drive glow, and Bloom amplifies it [inference].
- roles: environment-designer, art-director, vfx-designer, level-design
- also: world-level-readability, value-contrast
- sources: R09-F42 (R09:806-819, 830-835)

### LC-19 One main hue per effect
- principle: In a game with hundreds of effects, do not put too much colour into any single effect; "it is easy to go crazy with the colors".
- why: Multi-colour effects lose the colour code and add noise across the screen.
- apply: PROPOSAL default: one main hue plus lighter and darker versions of it per effect; a second hue only for a defined role in the colour table [inference].
- check: `look_check.py palette` on the effect capture: the count of distinct hue families is within the spec.
- check (DS): Clash test: place the effect on the brightest, most saturated stage area that shares its hue; if it fades, add a contrasting secondary hue (an all-orange shot in fire scenes got a blue secondary) (DS:vfx-design/references/elements.md:100).
- mistake: Rainbow effects with no role.
- examples:
  - R00c: League's hundreds of effects need colour discipline (R00c:3762-3770).
- roblox_fit: Many players' effects overlap on one phone screen, so colour discipline per effect matters more.
- roles: vfx-designer, art-director, reviewer
- also: vfx-reads-timing, visual-hierarchy
- sources: R00c-F11 (R00c:3762-3770)

### LC-20 Effect colour sits next to the caster's colour
- principle: Choose an effect colour analogous to (next to on the colour wheel) the caster's main colour, so players see who cast it.
- why: Colour links an effect to its source.
- apply: The VFX spec takes the character's main colours from the model and the art bible and picks an adjacent hue (within the colour-role table); the effect's reference image includes the character for matching. A recoloured skin recolours its effects [inference].
- check: Capture caster plus effect together; `look_check.py palette`: the effect's main hue sits close to a main model hue.
- mistake: Effects whose colour has no link to the caster, so it is unclear who did it.
- examples:
  - R00c: Yasuo's wind wall in light blue; pink wind for Star Guardian and Sacred Sword Janna (R00c:3770-3788).
- roblox_fit: Same for skins and pets.
- roles: vfx-designer, art-director, modeler, character-rigger, reference-images
- also: vfx-reads-timing, character-design
- sources: R00c-F12 (R00c:3770-3788)

### LC-21 Test colours where parts overlap
- principle: Overlapping limbs and parts are where most noise lives. If the palette overlaps itself (red gloves in front of red hair), the character is nearly impossible to read in motion. Fix by darkening one, two-toning, recolouring another part, or dropping the idea; mind colour associations (red + green "immediately looks like Christmas").
- why: Same-hue parts merge when they overlap.
- apply: Review every character in an overlapping pose (hands in front of hair and body, weapon across torso); colour-block so overlapping parts differ in value or hue. Same for an effect over its own caster.
- check: Capture an overlap pose at the game camera; grayscale; every overlapping pair keeps a value edge (`look_check.py value` with the front part as subject).
- mistake: Picking an accent colour without testing overlap.
- examples:
  - R11: red gloves against red hair; dull camo green pants considered and their association checked (R11:364-382, 451-452).
- roblox_fit: Same; also same-colour VFX over a character [inference].
- roles: art-director, modeler, reference-images, vfx-designer, animator, ui-ux-designer, reviewer, qa-lead
- also: value-contrast, shape-silhouette
- sources: R11-F29 (R11:364-382, 451-452)

### LC-22 Review with colour in, then rebalance
- principle: A design is judged with colour and value in, not as line art or untextured grey: colour and value push things back in space and sell the idea. Colours draw the eye differently, so after colour, effects or lighting change, rebalance the whole image again.
- why: Saturation and hue change attention independently of value; a balanced value pass does not stay balanced after colour.
- apply: Reviews always include a colour capture and its grayscale. After every colour, effect or lighting change, re-run the read-order check (VH-09) on the full capture.
- check: Saturation and hue peaks sit at the focal point; no background element is the most saturated item; the grayscale still passes VC-02.
- mistake: Judging uncoloured concepts; assuming a balanced value pass stays balanced after colour.
- examples:
  - R11: he forces himself to colour because it helps sell the idea (R11:356-363).
  - R10: rebalancing after adding colour and pop colours (R10:569-579, 926-930).
- roblox_fit: No change.
- roles: art-director, marketing, environment-designer, vfx-designer, ui-ux-designer, reference-images, modeler, reviewer
- also: visual-hierarchy, critique-feedback
- sources: R10-F20 (R10:569-579, 926-930); R11-F28 (R11:356-363)

### LC-23 Iterate colour globally; colourways are the same object
- principle: Try colour fast with global moves (shift all darks or all lights, apply saved palette gradients) and make several colourways. Silhouette leads and colour is partly taste; a colourway is the same object in new colours, but it can change the value balance, so re-check it.
- why: Global changes test the whole composition's colour in seconds; recolours (too many yellows) change volumes and feel.
- apply: Lock the silhouette first. Make 3-5 colourways of a capture with ColorCorrectionEffect presets or image tools, or by material swaps in Blender; keep a palette library in the art bible. Re-check value balance per colourway. Colourway variants are cheap live-ops content: Roblox's content-cadence guide names simple variants with slight colour changes as ideal recurring content (knowledge/external/roblox-creator-docs/production/game-design/content-updates.md:34) (lead fix 2026-10-22: documented, not an inference).
- check: Grayscale of each colourway side by side: the value structure and balance hold (VC-16), palette proportions still pass (LC-04).
- mistake: Repainting locally when a global change would answer; spending a day on colours instead of silhouette.
- examples:
  - R05: selective colour on the darks, gradient maps such as a Gekko palette; "would do a lot more iterations on color" (R05:635-655, 902-904).
  - R12: blue, red and "toy water blaster" chromas of the same gun (R12:432-446).
- roblox_fit: ColorCorrectionEffect TintColor and Saturation for quick global tests (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:83-85).
- roles: art-director, marketing, environment-designer, reference-images, modeler, live-ops-designer, reviewer
- also: process-iteration, style-identity
- sources: R05-F20 (R05:635-655, 902-904); R12-F36 (R12:432-446)

### LC-24 Check colour on a phone before it ships
- principle: Colours look different on every screen. Compare the work on a phone next to the work screen before sending, and export with the right colour profile; wrong profiles have shipped wrong colours.
- why: The audience sees it on their device, not the artist's.
- apply: Every final marketing image, icon and UI colour is viewed on a phone or a phone-size capture; export sRGB [inference].
- check: Compare the work image with the phone view: flag a large hue or value shift; verify the export colour profile in the file.
- mistake: Exporting in the wrong colour profile and posting (R05:669-671).
- examples:
  - R05: send the image to a phone and compare next to the screen (R05:657-671).
- roblox_fit: Most Roblox players are on phones, so the phone view is the main test.
- roles: art-director, marketing, ui-ux-designer, environment-designer, vfx-designer, qa-lead
- also: pipeline-production, critique-feedback
- sources: R05-F21 (R05:657-671)

### LC-25 Match skin temperature across face and body
- principle: Check the face's warmth against the body and base textures; a face that is too warm against a cooler base looks disconnected.
- why: Mismatched temperature makes parts look like they belong to different images.
- apply: Compare the hue temperature of skin across face, hands and body in the same light.
- check: Sample skin pixels on face, hands and body in one capture: same temperature family.
- mistake: A face painted separately in a warmer range [inference].
- examples:
  - R03: Caitlyn's face "too warm" against the base (R03:974-978).
- roblox_fit: Same.
- roles: modeler, art-director
- also: character-design
- sources: R03-F42 (R03:974-978)
