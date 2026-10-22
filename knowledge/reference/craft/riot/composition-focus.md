---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, environment-designer, modeler, reference-images, marketing, film-director, ui-ux-designer, vfx-designer, animator, level-design, character-rigger, game-designer, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Composition and focus

How everything in a frame (a level view, a shot, a thumbnail, an icon, an effect) is arranged so the eye goes where it should.
CF-01 is the working order. CF-02 and CF-03 design for the game camera. CF-04 to CF-07 compose for the real frame (crop, UI, safe area, the integrated capture). CF-08 to CF-14 lead the eye (shape flow, through-lines, motion, gradients, light tricks, height). CF-15 to CF-20 build depth, space, scale and secondary interest.
Related: read order in `visual-hierarchy.md` (VH-09), value focus in `value-contrast.md` (VC-04), light focus in `light-colour.md` (LC-12).
The line marked (DS) in CF-13 was added in stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### CF-01 Big to small: composition first, detail and effects last
- principle: Get the main impression fast: block in the composition, big shapes and primary colour zones over the whole piece first; medium shapes next; detail after the big read works; texture, smoke and sparks ("movie magic") only after the layout is locked. No amount of rendering saves a composition that does not work.
- why: Details cannot rescue a bad composition; they hide layout problems and cost time on the wrong thing. Effects added before the layout is stable must be redone.
- apply: Gate in every visual job: no material, texture, detail or VFX pass until a flat or grayscale blockout of the composition (scene, level shot, key art, asset) is approved. Modelers and environment designers: pass 1 = flat colour zones per material, rendered; pass 2 = medium forms; pass 3 = details. Reference-images: ask for a flat-colour blockout option before a detailed one. Promo shots and cutscene frames: clean render approved, VFX layers after.
- check: An approved blockout render exists and is dated before the first detail render; pass 1 at the game camera says what the thing is from colour zones alone (for example "grass, stone pedestal, fox"); the clean (no-VFX) frame passes composition and value review on its own, and later VFX do not cover focal faces.
- mistake: "It's very tempting to go into rendering in detail as soon as possible" (R10:168-170); beginners "perfecting the wheels on the car" (R09:556-564); "I want to get into those details because it's kind of fun" (R02:154-156).
- examples:
  - R10: he sketches and solves layout before painting (R10:168-176).
  - R09: get the main impression of the scene fast; the whole picture before detail (R09:556-564).
  - R02: big green blotches for grass and a basic grey for statue and pedestal before any detail (R02:56-58, 66-84, 154).
  - R05: crops and colourways tried, then smoke and sparks added to amplify the idea (R05:698-708).
- roblox_fit: Same for levels (blockout from the game camera first) and for Parts and MeshParts (material and colour per part first, then decals or SurfaceAppearance). Particle counts cost phone performance, so add only effects that amplify [unverified].
- roles: art-director, reference-images, marketing, environment-designer, film-director, modeler, level-design, character-rigger, vfx-designer, ui-ux-designer, animator, reviewer
- also: process-iteration, shape-silhouette, visual-hierarchy
- sources: R10-F07 (R10:168-176); R09-F30 (R09:556-564); R02-F01 (R02:56-58, 66-84, 154); R05-F24 (R05:698-708)

### CF-02 Design and pose for the side the game camera shows
- principle: The camera decides which parts of a design are ever seen and how big. Put identity details, design emphasis and pose clarity on the faces the game camera sees most, and judge everything through that camera, not a beauty angle. In poses, avoid limbs pointing straight at the lens.
- why: A defining detail on a hidden side is lost in a fast game ("each detail needs a moment to shine"); a leg aimed at the lens foreshortens into a boring stub.
- apply: Every model, effect, pose and environment brief names the game camera (angle, distance) from the game profile. Blender has a fixed camera matching it (third-person behind and above, or top-down) and all review renders and key poses use it. Identity details move to the seen faces, even if that differs from the source design; rotate feet or torso a few degrees toward profile when a limb would foreshorten.
- check: Render from the game camera at its usual angles (behind, side, top for player-controlled cameras): list the identity details and confirm each is visible in most frames; black-fill of each key pose shows both knees and the extended limb as separate shapes.
- mistake: Designing in a front view the camera never shows; keeping details where the original design had them; "the leg looking directly down the camera ... a little bit more boring and a little less dynamic" (R04:766).
- examples:
  - R00a: first-person, third-person and top-down each focus a design differently (R00a:632-642).
  - R11: 2XKO's side view shows mostly one side, so Katarina's scar and Vi's details moved; "a fighting game first and a League of Legends game second" (R11:146-163).
  - R04: the kicked leg moved back for "a nicer silhouette"; Akali's feet turned sideways because "we do see her from the side" (R04:156-161, 384-386, 758-766).
- roblox_fit: Most Roblox games use a third-person camera behind and above, or top-down, on phones: the player sees their own avatar's back, shoulders and head most, others at a distance [inference]. Put identity on back, shoulders and head; use this as the default review camera.
- roles: modeler, art-director, animator, vfx-designer, environment-designer, ui-ux-designer, reference-images, character-rigger, marketing, film-director, level-design, reviewer
- also: shape-silhouette, character-design, references-ideation
- sources: R00a-F16 (R00a:632-642); R11-F12 (R11:146-163); R04-F06 (R04:156-161, 384-386, 758-766)

### CF-03 Put detail where the camera distorts least
- principle: Put the most interesting part where the camera sees it largest and least distorted; foreshortened or far parts keep big, simple shapes, because fine detail there turns into lines or noise.
- why: Perspective compresses far parts; detail there is lost.
- apply: Decide the game camera first, then place focal detail in the zone with the largest screen area; keep far or foreshortened areas to big simple shapes.
- check: Capture at the actual game camera and zoom on the far or foreshortened parts: if small features merge into lines or noise, remove them.
- mistake: Two small cutouts on a muzzle that "will look like two lines" in first person (R12).
- examples:
  - R12: the glass visor at the rear-centre of a first-person gun; the silencer front is the most deformed, so it stays simple (R12:133-136, 243-248).
- roblox_fit: For third-person and top-down cameras the least-distorted, largest area is the top and the side facing the camera; tiny details on far sides are lost on phones [inference].
- roles: modeler, art-director, vfx-designer, environment-designer, reviewer
- also: materials-detail, shape-silhouette
- sources: R12-F13 (R12:133-136, 243-248)

### CF-04 Compose inside the real frame, crop and UI, at final scale
- principle: Compose from the first sketch inside the delivery frame: the crop players see most, the platform template, the UI over it, at the final size. Most player contact happens in a small crop seen many times, so define that crop first; still finish the full image for out-of-game use.
- why: Size and balance can be judged only in the final frame with its type and UI; elements under the UI, in the bleed or outside the crop are lost.
- apply: Before any key art, icon, shop card or thumbnail, load the frame as an overlay (Roblox thumbnail 16:9 with title, icon square (any corner rounding is [unverified]: the icon docs give a square 512x512 icon and 150x150 previews but no rounding, so measure it from a capture (lead fix 2026-10-22: rounding is not in the docs)), pass and product circles, the HUD at phone size for in-game shots) and keep face and focal object out of overlay zones. For every character or item image, define its in-game crop and compose the reference so the crop works; drop the art into the real layout early and judge scale there.
- check: Render with the overlay on: no focal element under UI, crop or rounding. Crop the render to each in-game frame and view at player size (`thumb_check.py icon` at 150x150, `thumb_check.py thumbnail --size` for tiles): it still says who it is.
- mistake: Composing on a blank canvas and fitting UI later; judging scale on bare art; composing only for the full image so the crop shows nothing useful.
- examples:
  - R10: a card template with UI, crop and bleed used from the start; the UI is part of the composition (R10:97-108, 184).
  - R05: "Last Revive" looked small until dropped into the poster layout (R05:483-487).
  - R08: the TFT crop is "basically just their face and a little bit of their weapon"; the full image is still finished (R08:133-148, 732-736).
- roblox_fit: Experience icon 512x512, shown at 150x150 (knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md:34, 55); thumbnails 16:9, 1920x1080 (production/publishing/thumbnails.md:54); pass and product icons keep key detail inside the circle (production/monetization/passes.md:28, developer-products.md:30); badges are cropped to a circle (production/publishing/badges.md:32); ScreenGui.ScreenInsets defines the HUD safe area (tutorials/use-case-tutorials/ui/create-hud-meters.md:60-70).
- roles: marketing, ui-ux-designer, art-director, film-director, reference-images, modeler, reviewer
- also: ui-ux, visual-hierarchy, pipeline-production
- sources: R10-F02 (R10:97-108, 184); R05-F16 (R05:483-487); R08-F05 (R08:133-148, 732-736)

### CF-05 Lock a safe square around the crop, then move anything else
- principle: Keep an invisible square around the crop (head to shoulder plus reserved space on one side). As long as it stays intact, everything else may move freely.
- why: It protects the in-game crop while leaving the rest open to change.
- apply: Mark the crop rectangle (or circle) on every key-art and icon file as a guide layer or render border and lock it before composing the rest.
- check: Overlay the crop square on the final: head, shoulder and the reserved space are inside; nothing important crosses the border.
- mistake: Moving elements and breaking the in-game crop.
- examples:
  - R08: a square from Alune's head to her shoulder with space kept to the left (R08:528-534).
- roblox_fit: Circular safe areas for pass, product and badge icons (knowledge/external/roblox-creator-docs/production/monetization/passes.md:28, production/publishing/badges.md:32); 16:9 for thumbnails (production/publishing/thumbnails.md:54).
- roles: art-director, marketing, ui-ux-designer, reference-images, reviewer, qa-lead
- also: pipeline-production
- sources: R08-F23 (R08:528-534)

### CF-06 In a small frame, the identifying parts fill it
- principle: Small frames show the character's "icons", the big indicators that say who it is (a cowl and giant collar), and faces large enough to identify. Movie posters use giant heads because "people need to know who's in the movie".
- why: One large indicator or a big face tells players who it is faster than any detail; small figures do not identify.
- apply: The anchor list (CD-04) marks the 1-2 anchors that must sit inside each crop; crop thumbnails and icons featuring characters to heads or upper bodies large enough to identify at player size; keep indicators near the centre of circular crops.
- check: Crop at player size (`thumb_check.py`): each featured character is identifiable and the marked indicators are inside and readable.
- mistake: Cropping out the defining shape; whole small figures in a tiny icon.
- examples:
  - R08: the cowl and collar kept inside Alune's crop since Spirit Blossom (R08:329-338).
  - R05: the second thumbnail uses "a lot of big heads" (R05:233-237).
- roblox_fit: Icons scale down to 150x150 (knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md:34), so faces must be bigger still; circular crops cut corners (production/monetization/passes.md:28).
- roles: art-director, marketing, ui-ux-designer, modeler, reference-images, film-director
- also: character-design, visual-hierarchy
- sources: R08-F15 (R08:329-338); R05-F11 (R05:233-237)

### CF-07 Judge composition on the integrated capture
- principle: Composition is how all elements in the frame work together (character, background, effects, values, colours and UI). One craft's change shifts every other craft's balance.
- why: The eye reacts to the whole frame; judging an asset alone misses how it fights the background or UI.
- apply: Review composition on a full capture at the game camera with effects, lighting, other players and HUD on, not on per-asset renders.
- check: Integrated capture with UI on at phone size: focal point and balance judged there; any craft's change triggers a new integrated capture.
- mistake: Judging a character or effect alone [inference].
- examples:
  - R10: composition is the layout of character, background and effects plus values and colours, the UI included (R10:178-186).
- roblox_fit: Phones show HUD, many players and effects at once; the integrated capture is the only honest view.
- roles: art-director, marketing, environment-designer, vfx-designer, ui-ux-designer, film-director, level-design, reviewer
- also: visual-hierarchy, critique-feedback, cross-craft
- sources: R10-F08 (R10:178-186)

### CF-08 Shape flow points to the focal point, at every scale
- principle: An environment or image is a collection of shapes that lead the eye. Orient big shapes (paths, walls, cliffs, roof lines) and secondary shapes (bushes, cracks, debris, light gradients) to frame and point at the one main focal point; the same flow continues inside forms (shadow shapes, reflections, highlights).
- why: The eye follows directional shapes; converging flow makes the focal point read first, and small consistent directions add energy and unity.
- apply: Choose the focal point first (goal, landmark, hero). In the greybox and kit layout, point paths and big lines toward it; keep one main focal shape per view; orient plants, rock edges and debris toward it; when painting textures, placing highlights or designing VFX sub-shapes, orient them with the main flow.
- check: Black-fill or grayscale capture at the game camera: trace the main lines; most converge on the focal point or the next route; blur test (heavy downscale): the goal area is still the main read. Zoom on a material: internal shapes follow the main direction. Fail if lines lead off-screen or to a minor element.
- mistake: Shapes that point everywhere or away from where the player must go.
- examples:
  - R00b: "an environment is a collection of shapes that lead the eye, just like any image" (R00b:1863-1885, 2117-2119).
  - R13: bushes all point at the golden sand disk (R13:273-291); shadow and reflection shapes on the disk also flow (R13:321-329).
- roblox_fit: Under a moving third-person camera the flow must work from the usual approach angles, not one view; check from the real game camera [inference].
- roles: art-director, environment-designer, level-design, film-director, marketing, modeler, vfx-designer, reference-images, reviewer
- also: visual-hierarchy, world-level-readability
- sources: R00b-F06 (R00b:1863-1885, 2117-2119); R13-F11 (R13:273-291); R13-F12 (R13:321-329)

### CF-09 Lines on an object lead somewhere and agree with each other
- principle: "All lines, they have to go somewhere and they have to create like a visual flow." Run panel lines, cuts and edges toward 1-2 shared points or parallel to the main line, and carry one continuous line across separate parts (barrel through grip into stock); replace a shape that fights the shape language.
- why: The brain likes correlated lines because it predicts them; continuous lines unify separate pieces and make an object feel designed and elegant.
- apply: In Blender and reference prompts, align panel lines, cuts and edges to shared directions; align curves across part boundaries. Same for environment kits and UI layouts (aligned edges); animators use the same idea as a line of action [inference].
- check: Edge-only side render: extend the main lines; they meet in 1-2 points or run parallel; trace the main line across part joins: it continues; count stray lines that go nowhere.
- mistake: Random cuts with no shared direction; a geometric bend "pretty at odds with the rest of the shape language" (R01).
- examples:
  - R12: lines on top of the Phantom converge to one point to find a new silhouette part (R12:130-142, 167-174, 194-197).
  - R01: a swoop from barrel bottom through grip continued into the stock; the odd bend replaced (R01:894-902, 932-937).
- roblox_fit: Applies to level layouts too (leading lines to goals) [inference].
- roles: modeler, art-director, environment-designer, ui-ux-designer, level-design, reference-images, animator
- also: shape-silhouette
- sources: R12-F12 (R12:130-142, 167-174, 194-197); R01-F50 (R01:894-902, 932-937)

### CF-10 Converging motion pulls the eye to the focus
- principle: Focus attention with motion, not only glow: elements swirl from outside in toward the centre.
- why: The eye follows movement direction; converging motion points at the focus.
- apply: Particles spawn on a ring and move inward (negative Speed, or attachments that orbit and contract); an inward spiral during the build-up. UI reward elements fly toward the counter they fill [inference].
- check: Frame sequence: tracked particles move toward the focus point; no strong motion points away during the build.
- mistake: Relying only on brightness for focus (R06:175).
- examples:
  - R06: clouds spin in toward the centre "to make our eyes go towards the center even more" (R06:175-176, 186-189).
- roblox_fit: Negative Speed makes particles travel in reverse (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:204); a Sphere shape with inward emission can converge (particle-emitters.md:273-275) [inference for the setup].
- roles: vfx-designer, animator, film-director, environment-designer, ui-ux-designer
- also: vfx-reads-timing, rhythm
- sources: R06-F17 (R06:175-176, 186-189)

### CF-11 After the hit, move the eye on
- principle: After the peak, guide the eye to the result: the old spot calms (stops moving, spreads out, darkens) and the result area lights up.
- why: Movement and brightness pull attention; leaving both at the old spot keeps the eye there and makes the result noisy.
- apply: At the hit, stop spawning the build layers and lower their brightness; raise brightness where the result plays.
- check: Value captures before and after the hit: the brightest region moves to the result area; no busy motion is left at the old spot.
- mistake: "things lingering up top" after the hit (R06:234).
- examples:
  - R06: clouds stop exactly at the hit; keep it darker up top and light up the bottom (R06:228, 234-238, 268-271).
- roblox_fit: Set Enabled false at the hit time; existing particles finish their lifetime (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:490), so keep that lifetime short.
- roles: vfx-designer, film-director, art-director, environment-designer
- also: vfx-reads-timing, rhythm
- sources: R06-F23 (R06:228, 234-238, 268-271)

### CF-12 A value gradient toward the hero
- principle: A gradient (cooler and darker at the edges, warmer and brighter at the subject) makes the hero read as lit by a beam, with the highest value on its head; surrounding detail is sacrificed for focus.
- why: All values lead to the subject.
- apply: Darken the surroundings and light the hero: local lights near the subject, darker edge materials, or a vignette-like ColorCorrection in cutscenes and promo renders.
- check: Value map of the capture: the brightest spot is on the hero's head or focal part; values fall off toward the edges.
- mistake: Equal values everywhere, so the hero "won't be the focus" (R02:836-840).
- examples:
  - R02: an overlay of dark blue, warmer near the fox (R02:834-858, 950-962).
- roblox_fit: ColorCorrectionEffect (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:76-85) is global; in gameplay prefer local lights and materials [inference].
- roles: environment-designer, art-director, modeler, marketing, film-director, reference-images, level-design
- also: light-colour, value-contrast
- sources: R02-F35 (R02:834-858, 950-962)

### CF-13 A bright focal light can hide a surprise
- principle: A bright light pulls attention so strongly that the area outside it goes unwatched; use it to stage a surprise.
- why: Attention goes to the light.
- apply: For a scare, ambush or hidden reward, put a bright focal light on one side and stage the surprise in the darker, low-contrast side or behind the player's line of sight.
- apply (DS): In a level, hide the next big thing behind a turn or a rise and show it framed as the player comes round (DS:level-design/SKILL.md:40).
- check: Grayscale capture: the surprise sits in a low-contrast area while the light is the top focus; in a playtest, testers do not spot it early.
- mistake: Surprises placed in the most lit or highest-contrast part of the screen.
- examples:
  - R00b: the "Hello..." gag: a creature appears while the eye is on the light (R00b:1923-1929).
- roblox_fit: Works the same; on phones peripheral detail is even less noticed.
- roles: level-design, environment-designer, game-designer, film-director
- also: light-colour, world-level-readability
- sources: R00b-F10 (R00b:1923-1929)

### CF-14 Make the focal point the tallest shape
- principle: Make the focal point stand out mainly by height; heights matter most.
- why: Tall shapes read first and from far away.
- apply: Raise the landmark well above player height and put the biggest marker on it [inference].
- check: Black-fill of the level view: the landmark is the tallest shape and is not occluded from the game camera.
- mistake: A landmark at the same height as its surroundings [inference].
- examples:
  - R09: the tower raised "really, really tall" with the B marker on it (R09:596-604, 1087-1088).
- roblox_fit: Tall landmarks are visible from a top-down camera only if not occluded [inference].
- roles: environment-designer, level-design, art-director, modeler
- also: world-level-readability, shape-silhouette
- sources: R09-F31 (R09:596-604, 1087-1088)

### CF-15 Three depth groups: foreground frames, midground carries, background unifies
- principle: Keep depth simple: foreground, midground, background. The background takes global tweaks for unity; the midground holds the main subject and gets the most care; a darker foreground element frames the subject and pushes it back into space, and can be removed at any time.
- why: Separate depth planes allow quick global changes and make depth readable; a dark near layer adds depth to a flat image.
- apply: Blender and Studio scenes for key art, thumbnails and cutscenes are organised into FG, MG and BG collections or folders; most detail budget goes to the midground; one dark foreground object sits at the frame edge between camera and subject [inference for placement].
- check: Toggle each group: the image still reads with FG off; BG can be darkened alone; detail concentrates in MG. Grayscale: three value planes are visible (dark FG, mid subject, low-contrast BG). Check gore level of any foreground element.
- mistake: Flat layer soup that blocks global changes; images with no foreground plane.
- examples:
  - R05: ribs and graves as a separable foreground layer; the midground gets "more love" (R05:776-797).
  - R08: the belly of a monster Alune bored through, with ribs, as a dark foreground (R08:509-524).
- roblox_fit: In gameplay a foreground object must not block the player's view [inference]; Atmosphere helps separate depth planes (knowledge/external/roblox-creator-docs/environment/atmosphere.md) [inference]. Gore needs a `platform-policy` check.
- roles: art-director, environment-designer, film-director, marketing, level-design, reference-images
- also: value-contrast, world-level-readability
- sources: R05-F31 (R05:776-797); R08-F21 (R08:509-524)

### CF-16 Negative space on purpose: calm room, no awkward gaps
- principle: Plan negative space: keep a clean backdrop with calm room around the hero and the title, and avoid accidental awkward gaps or bare zones (an empty waist, a bare prop), filling them with an element that also tells story.
- why: Planned negative space rests the eye and gives room; accidental gaps look unfinished or unbalanced.
- apply: Thumbnails and banners reserve calm areas for title and hero. On assets, review the silhouette for gaps and bare zones; fill with a story element (an ornament showing wealth) or close the gap.
- check: `look_check.py value` shows a calm, low-detail area behind and around title and hero; black-fill and grayscale renders of assets flag bare zones and awkward gaps.
- mistake: A plain gap making "the gun feel a little bare" (R01); clutter with no room for the title [inference].
- examples:
  - R01: cummerbund versus vest considered for the waist gap; a sculptural ornament added to the bare gun (R01:341-343, 972-976).
  - R05: the preferred layout keeps a clean backdrop with negative space (R05:854-858).
- roblox_fit: Phone safe areas also reserve space [unverified].
- roles: marketing, art-director, ui-ux-designer, modeler, reference-images
- also: visual-hierarchy, shape-silhouette
- sources: R01-F23 (R01:341-343, 972-976); R05-F36 (R05:854-858)

### CF-17 A giant figure behind small heroes sells scale and threat
- principle: A giant figure in the background (back turned, side view) above small fleeing heroes and a crowd makes the threat feel huge; the turned back adds mystery.
- why: Scale contrast between background and foreground reads as power.
- apply: For boss reveals, event art and cutscene shots, stage the threat oversized behind small heroes kept in the foreground.
- check: The height ratio of the background figure to the foreground heroes is large and obvious in a capture; both read in black-fill.
- mistake: Threat and heroes at similar size [inference].
- examples:
  - R05: a giant Viper with green smoke above zombies and running heroes (R05:213-231, 249-251).
- roblox_fit: In game, use a fixed camera or cutscene for this shot; avoid huge parts that block the play camera [inference].
- roles: film-director, marketing, environment-designer, art-director, level-design
- also: exaggeration, visual-hierarchy
- sources: R05-F10 (R05:213-231, 249-251)

### CF-18 Camera height states status
- principle: Choose the view angle from the character's status and the feeling of meeting it: a character "above us" looks down at the viewer; friendly characters meet the eye.
- why: Viewing from below makes a character feel powerful and distant.
- apply: Briefs for key art, icons, cinematics and showcase renders state the intended feeling and the camera height (low camera looking up for dominant characters, eye level for friendly ones) [inference for defaults].
- check: In the render, compare camera height with the character's eyes; a fresh agent names the feeling and it matches the brief.
- mistake: All characters shot at the same height regardless of status [inference].
- examples:
  - R08: Alune looks down at us because she is never on the same level as anyone (R08:338-358).
- roblox_fit: The gameplay camera is fixed, so this applies to icons, thumbnails, cutscenes and shop previews [inference].
- roles: film-director, art-director, marketing, animator, reference-images
- also: character-design
- sources: R08-F16 (R08:338-358)

### CF-19 Small secondary elements carry movement and colour pops along the eye path
- principle: Use small secondary elements (leaping fish, sparks, birds) for extra movement and colour pops, placed along the eye path, not at the focal point.
- why: Small accents in a contrasting colour keep the eye moving and add interest.
- apply: Place a few small accent elements in a pop colour along the flow toward the focus, smaller and lower in contrast than the focal point.
- check: Accents are smaller and lower contrast than the focal point; they sit on the traced eye path.
- mistake: Accents that outshine the focus [inference].
- examples:
  - R10: fish leaping around Yasuo (R10:553-555).
- roblox_fit: Count particle accents against phone budgets.
- roles: vfx-designer, art-director, marketing, environment-designer, animator
- also: light-colour, rhythm
- sources: R10-F19 (R10:553-555)

### CF-20 Background patterns are reversible and A/B tested
- principle: A background pattern that echoes the subject's shapes adds a finished, product feel, but only if it does not break the composition; try it and remove it if it fails.
- why: Echoed shapes unify; extra pattern can compete.
- apply: Add background motifs as a separate, reversible layer and compare captures with and without.
- check: A/B capture: the read order (VH-09) is unchanged with the pattern on.
- mistake: A pattern that competes with the subject [inference].
- examples:
  - R10: a Yasuo-shape pattern behind the card (R10:903-909).
- roblox_fit: No change.
- roles: ui-ux-designer, marketing, art-director, environment-designer
- also: style-identity
- sources: R10-F25 (R10:903-909)
