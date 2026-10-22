---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, environment-designer, vfx-designer, ui-ux-designer, modeler, game-designer, level-design, reviewer, qa-lead, orchestrator, sound-designer, reference-images, marketing, animator, character-rigger, film-director]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Visual hierarchy

What the player sees first, second and third, and how a game with thousands of assets keeps them from clashing.
VH-01 and VH-02 rank importance across the whole screen and across a set of assets; VH-03 to VH-05 limit noise and place detail; VH-06 to VH-10 set the read order of one character, image or enemy roster; VH-11 is the review order.
Related: the value tools in `value-contrast.md` (VC-04, VC-05), eye paths in `composition-focus.md`, silhouette in `shape-silhouette.md`.
The line marked (DS) in VH-02 was added in stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### VH-01 Rank what must be seen; UI and VFX first, characters second, environment last
- principle: The most important information must be the easiest to see. Write a ranked list of what must be seen in each scene and give contrast in that order. Default screen order: UI and gameplay VFX first, characters second, environment always the backdrop.
- why: Attention is limited and goes to the strongest contrast. A game has thousands of art pieces; without a ranked order they clash and the player misses gameplay information.
- apply: The art bible states the screen order. Each scene or level brief ranks its items (for example: 1 threat, 2 player, 3 objective, 4 background) and assigns the contrast budget to match (value bands: VC-05). Environment and props get lower contrast and saturation than characters; characters lower than VFX and UI.
- check: Gameplay capture at the game camera with typical effects and UI on, plus its grayscale: rank what the eye goes to first and compare with the brief's list; `look_check.py value` confirms the top-ranked item has the strongest local contrast. Fail if any environment element out-contrasts a character or an effect.
- mistake: Every asset made "cool" at full contrast, so the screen clashes; environment art that grabs attention.
- examples:
  - R00a: thousands of pieces in one game must not clash; hierarchy is made by manipulating contrast (R00a:221-234).
  - R13: on the TFT board, UI and spell VFX read over units, units over the arena (R13:131-135).
- roblox_fit: Mixed-style imported assets are common on Roblox, and many players and effects share a small phone screen, so the order must be enforced at every review [inference].
- roles: art-director, environment-designer, vfx-designer, ui-ux-designer, modeler, game-designer, level-design, reviewer
- also: value-contrast, composition-focus
- sources: R00a-F05 (R00a:221-234); R13-F07 (R13:131-135)

### VH-02 Rank loudness across a set: if everything is loud, nothing is
- principle: Rank every effect (and sound and celebration) in the game by importance and give size, brightness, duration and loudness by rank. Only the top tier may fill the screen. The job is to communicate gameplay, not to make every effect big.
- why: Importance is felt by contrast with what is around it; uniform spectacle flattens the hierarchy: "if you make every effect epic and loud, nothing will be epic and loud" (R00c:3650-3654).
- apply: Keep a tier table in the effect and sound spec (for example basic attack, ability, ultimate, rare reward) with caps per tier on screen area, peak brightness, duration and loudness [inference: the cap numbers are set per game]. UI celebrations follow the same tiers.
- apply (DS): Default prominence order for effects on one screen: a threat to the local player, then the player's own action feedback, then pickups and objectives, then other players' effects, then ambient. Own-weapon feedback stays below threats (review from the target's camera; if testers remember the muzzle flash, it is too strong). When two effects collide, the lower-rated one dims or shortens (DS:vfx-design/references/scene-and-clutter.md:87; DS:vfx-design/references/elements.md:37, 151).
- check: Play effects of different tiers together in one Studio capture (and one audio mix): the top-ranked one clearly dominates, low tiers do not compete. Compare each effect's measured screen area and duration with its tier cap.
- mistake: "It can be tempting to make every effect big and flashy" (R00c:3630-3632).
- examples:
  - R00c: the VFX artist's role is to communicate gameplay; it comes down to clear contrast (R00c:3626-3654).
- roblox_fit: Many players and effects on a phone make this critical; restraint also saves particle and audio budget.
- roles: vfx-designer, art-director, game-designer, sound-designer, ui-ux-designer, reviewer, orchestrator
- also: vfx-reads-timing, sound, game-design-fun
- sources: R00c-F08 (R00c:3626-3654)

### VH-03 Less is more: the fewest shapes and colours that give the strongest read
- principle: Keep designs as simple as possible: the minimum shapes and colours for the strongest visual. Extra random shapes and colours make an image weaker, not richer. "As readable your art, your art is better art" (R12).
- why: Fewer elements give a clearer read and stronger impact. Beginners overcomplicate to show skill; the hard part is keeping it clean. A simple process also saves time.
- apply: Every asset brief caps detail: big shapes first, a few mediums, a few smalls. Count distinct shapes and colours per asset; remove any that do not serve the read. The art bible sets a palette size per asset type. Applies to characters, environments, VFX, UI and thumbnails.
- check: `look_check.py palette` cluster count against the palette size; black-fill silhouette is simple; at thumbnail size, list each small detail and remove any that adds noise or is invisible at the game camera.
- mistake: Introducing more "random shapes and colors" (R13:963-966); "I overcomplicated everything" (R12:269-276).
- examples:
  - R13: products with one button or none have a strong graphic read; fewer shapes and colours for character, environment and VFX (R13:961-980).
  - R12: the final Phantom "already looks so readable"; simple and clean is the hard part (R12:269-276, 408).
- roblox_fit: Fewer elements also lower part, draw and texture counts on phones [inference].
- roles: art-director, ui-ux-designer, vfx-designer, modeler, environment-designer, marketing, reference-images, reviewer
- also: shape-silhouette, style-identity
- sources: R13-F37 (R13:961-980); R12-F21 (R12:269-276, 408)

### VH-04 Judge noise in motion, with lighting and effects on
- principle: Lines, shadows and many colours together make "a visual noise generating machine"; motion, shifting light and effects multiply it. A design that looks simple on the sheet can lose the character completely in play. Judge at a glance, in game, with effects on, and ask in order: does it look like the character, does it support the theme, can players engage without extra thinking.
- why: Every edge, shadow and colour change is a signal; in motion they compete and the form is lost. Noise costs the attention players need for gameplay.
- apply: Keep a small number of colour blocks and details per character; decide which forms need outline or strong shadow and leave the rest flat. In Roblox the noise sources are textures, many small parts, Highlight outlines, strong shadows and effects on top. Every art review asks the three questions.
- check: Capture the character moving at the game camera with lighting and a typical ability effect on; grayscale it. A tester (or a fresh agent) names the character in one glance; body parts can be told apart; `look_check.py value` and `silhouette` on that capture. Fail if the read only works on the still sheet.
- mistake: "Full send every detail" because it looks "not that complicated on the concept sheet" (R11:92-105); "a lot of visual noise and extra thinking" (R01).
- examples:
  - R11: simple 2XKO designs became noisy once moving, lit and with effects (R11:92-105).
  - R01: zoom out often; skins must not get in the way of abilities being flung around (R01:186-200, 700-702).
- roblox_fit: Many players and effects on screen make noise worse. Highlight is capped at 255 instances on the client (knowledge/external/roblox-creator-docs/_api-reference/classes/Highlight.yaml:49-52), so outlines are not a universal fix.
- roles: art-director, modeler, vfx-designer, environment-designer, ui-ux-designer, reviewer, qa-lead, reference-images
- also: value-contrast, materials-detail, critique-feedback
- sources: R11-F06 (R11:92-105); R01-F11 (R01:186-200, 700-702)

### VH-05 Clump detail in a few places; leave areas of rest
- principle: Where detail goes is a hierarchy tool. Group detail in a few chosen spots (face, weapon, interactable, landmark, objective) and leave large areas of rest between them. "If everything is special, then nothing is special" (R02). Keep the player space calm.
- why: Contrast between busy and calm guides the eye and creates stylisation; uniform detail is noise and hides players.
- apply: Brief each asset or area with its 1-3 detail spots [inference on count]; large surfaces stay plain. Environment: concentrate texture and prop detail at goals, routes and landmarks; keep the player band (floor to head height) low in detail and put clusters above head height or at edges [inference]. UI: dense information only where the decision is.
- check: Downscale a capture to thumbnail size (`look_check.py thumb`): detail clusters sit at the focal points with clear quiet areas between. Mark detail spots on a render; count props per zone against the focus map. Fail if detail density is even.
- mistake: "I'm putting grass blades everywhere again. And that's not a good thing" (R02:492-494); cramming detail "in a world of copy and paste" (R00a).
- examples:
  - R00a: Journey and INSIDE use large areas of rest (R00a:344-366).
  - R00b: shifting between large areas of rest and areas with more detail guides where the player looks (R00b:1931-1939).
  - R02: grass blades clumped near the pedestal, moss only in a few areas, one broken side (R02:424-430, 488-502, 724-728, 772-778).
  - R09: VALORANT set dressing clusters detail and keeps player space readable (R09:946-951).
- roblox_fit: Rest areas also save parts, triangles and texture memory on phones (per-mesh 20,000 triangle cap: knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34; 1024x1024 max texture: art/modeling/texture-specifications.md:131).
- roles: environment-designer, modeler, art-director, level-design, vfx-designer, ui-ux-designer, marketing, reference-images, character-rigger, reviewer
- also: materials-detail, composition-focus, world-level-readability
- sources: R02-F22 (R02:424-430, 488-502, 724-728, 772-778); R00a-F11 (R00a:344-366); R00b-F11 (R00b:1931-1939); R09-F45 (R09:946-951)

### VH-06 The source of power is the primary read
- principle: The character's or effect's source of power (weapon, casting hand, core) is its most visible part. On a character it keeps its size and thickness; in an effect it is the brightest point, placed where the player must look.
- why: Players identify who is who and what they do from the primary read; shrink the weapon and "they might mistake her for someone else" (R01). With no bright centre, an effect has "nothing for them to really focus on" (R06).
- apply: Weapons and signature tools keep their size and thickness in every variant and carry the highest value contrast on the character. Every effect brief names its focus point (default for characters: chest or the casting hand [inference]); the brightest layer sits there.
- check: Thumbnail-size and game-camera captures: the weapon or focus point is the first thing seen; black-fill silhouette shows it clearly; `look_check.py value` places the top luminance at the named point; compare the weapon's screen area with the base version.
- mistake: Thinning or shrinking the signature item in a variant; effects with even brightness and no focal point (R06:132-135).
- examples:
  - R01: Caitlyn's "comically overstated" sniper rifle is her primary read (R01:162-166, 425-428, 644-656).
  - R06: a centre glow dot added in the middle of the clouds; in TFT the focus is usually the unit's chest (R06:131-136).
- roblox_fit: On phones the held tool is often the only readable cue of role [inference]. Emit from an Attachment at the focus; LightEmission makes it additive (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:257).
- roles: art-director, modeler, reference-images, animator, vfx-designer, game-designer, film-director, ui-ux-designer, marketing, reviewer
- also: shape-silhouette, character-design, vfx-reads-timing, composition-focus
- sources: R01-F08 (R01:162-166, 425-428, 644-656); R06-F12 (R06:131-136)

### VH-07 Recognisable in under a second beats unique
- principle: A character, item or icon must register in about 0.5-1 second through shape, colour and palette, and must not resemble a neighbour in the roster. Among options, pick the one players identify correctly at a glance, even if another has a more unique shape; then add uniqueness inside that read.
- why: Players meet characters in fast shop clicks and gameplay glances and memorise colour and shape; two look-alikes cause wrong buys and wrong reads. A shape that "could be Senna's gun, or Galio's wing" fails (R13).
- apply: The first acceptance line of every character, item and icon brief is the one-second read. Compare each new design with its nearest look-alikes (same palette or role) and change shape or colour where they overlap. When choosing among reference-image options, score each for "a player names subject, owner and function in 1 s".
- check: Place the new icon among the roster icons at real size (`thumb_check.py icon`, 150x150) and in black-fill; flash or blur it: a fresh agent asked "what is this and whose is it?" answers correctly. `look_check.py silhouette --compare` and `palette` against the nearest neighbours: flag high overlap.
- mistake: A new character that blends with an existing one (Alune vs Aurora, R08); picking the most interesting shape that "doesn't register immediately" (R13:56-58).
- examples:
  - R08: "How do we completely register the character to the person in literally, like 0.5 seconds?" (R08:234-247).
  - R13: option 2 had the best shape but read as another champion's item; option 3 read instantly as Zilean and was chosen (R13:48-74).
- roblox_fit: Icons show at 150x150 (knowledge/external/roblox-creator-docs/production/publishing/experience-icons.md:34); phone shop grids are small and touch players tap fast; distant cameras shrink props to a few dozen pixels.
- roles: art-director, modeler, environment-designer, character-rigger, vfx-designer, ui-ux-designer, marketing, game-designer, reference-images, reviewer, qa-lead
- also: shape-silhouette, character-design, critique-feedback
- sources: R08-F09 (R08:234-247); R13-F01 (R13:48-74)

### VH-08 Silhouette is the first read, the face the second
- principle: Recognition comes in order: silhouette first, face second. Put the items a character always carries (weapon, headpiece) into the silhouette, and make the face readable at the crop size players see.
- why: In a small view only the big shape and the face carry identity; small details do not.
- apply: Modelers and art directors make the weapon and headpiece the largest silhouette breaks. Face features are pushed enough to read at the smallest crop [inference for the amount].
- check: Black-fill shows the weapon and headpiece clearly; a crop at the real display size (icon, shop card) shows the face readable.
- mistake: Relying on small details for recognition.
- examples:
  - R08: Alune's weapon and headpiece prioritised; TFT shows "basically just their face and a little bit of their weapon" (R08:724-740).
- roblox_fit: Roblox faces are often small or a decal; at the gameplay camera the silhouette carries more and the face less, but shop icons and portraits still show the face [inference].
- roles: art-director, modeler, character-rigger, animator, marketing, ui-ux-designer, reviewer, reference-images
- also: shape-silhouette, character-design
- sources: R08-F28 (R08:724-740)

### VH-09 Plan the read order: primary, secondary, tertiary
- principle: An image or scene with many goals must choose its focal point and its primary, secondary and tertiary reads, then use purposeful flow lines to move the eye in that order, with small story details placed along the path.
- why: Without a set order every goal competes and nothing reads.
- apply: Each key art, shot, scene or screen brief lists its reads in order; flow lines (rope, path, trail, light shaft, wind lines) point toward the primary. On phones plan fewer reads [inference].
- check: Blur or shrink the capture to thumbnail size: the first thing seen is the stated primary, and the reads appear in the stated order when a fresh agent describes the image.
- mistake: Trying to "say a lot of things" equally in one still (R10:496).
- examples:
  - R10: fishing line and wind lines circle the eye around Yasuo (R10:484-506).
- roblox_fit: Small screens hold fewer reads; cut to two where possible [inference].
- roles: art-director, marketing, environment-designer, vfx-designer, ui-ux-designer, film-director, level-design, reviewer, reference-images
- also: composition-focus
- sources: R10-F17 (R10:484-506)

### VH-10 Size signals importance
- principle: Size alone can tell which enemy matters most. Bigger reads as more powerful and more threatening at a glance.
- why: Size is read before detail or colour.
- apply: Scale the most dangerous or important enemy (or reward, or objective) noticeably larger than common ones, and keep size consistent with threat across the roster.
- check: Capture the enemy lineup at the game camera; rank by screen size and compare with the design's threat ranking; any mismatch is a ticket.
- mistake: Size that contradicts threat (a tiny boss, a huge harmless mob) [inference].
- examples:
  - R00a: altering only size establishes which enemy is the most important (R00a:316-324).
- roblox_fit: On a phone small enemies shrink to a few pixels, so size gaps must be larger than on PC [inference].
- roles: modeler, game-designer, art-director, character-rigger, level-design
- also: shape-silhouette, game-design-fun
- sources: R00a-F09 (R00a:316-324)

### VH-11 Review in a fixed order: balance, proportion, weight, then contrast and detail
- principle: The graphic-design fundamentals (contrast, balance, alignment, hierarchy, proximity, scale and proportion, movement) apply to every image: object, character, screen or illustration. Settle them big first: balance of big, medium and small shapes and colours, then proportions, then the weight of elements, then usability and contrast, then detail.
- why: Later steps depend on earlier ones; fixing small contrast while the big balance is wrong wastes the fix.
- apply: Use the fundamentals as the shared review checklist across art, UI and marketing reviews; order review notes by these stages and do not fix contrast or detail before balance passes.
- check: The review sheet names each fundamental per capture and the notes are ordered by stage; a note on detail while a balance note is open is sent back.
- mistake: Fixing small contrast while the big balance is wrong [inference]; treating object design as separate from visual design.
- examples:
  - R12: "every time ... I'm worried about like major parts first" (R12:323-327); graphic-design fundamentals made any image balanced (R12:208-213).
- roblox_fit: No change.
- roles: art-director, modeler, environment-designer, ui-ux-designer, marketing, vfx-designer, reviewer
- also: critique-feedback, composition-focus
- sources: R12-F27 (R12:323-327); R12-F19 (R12:208-213)
