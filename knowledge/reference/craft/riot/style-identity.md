---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, reference-images, modeler, environment-designer, vfx-designer, ui-ux-designer, sound-designer, character-rigger, animator, game-designer, marketing, live-ops-designer, progression-designer, orchestrator, level-design, reviewer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Style and identity

One deliberate style that sets the tone and makes everything look like one game, plus how themes, rosters, updates, tiers and brands keep their identity while changing.
SI-01 to SI-08 set and protect the style (tone levers, every choice serves the idea, theme fit, theme cues, audience, house look over personal habit, stylisation level, named sources). SI-09 and SI-10 make a roster read as one cast. SI-11 to SI-17 keep identity through updates, themes, tone shifts, names, motifs, format exceptions and hidden stories. SI-18 to SI-20 are variants and tiers.
Related: identity anchors in `character-design.md` (CD-04), shape vocabulary in `shape-silhouette.md` (SS-06), palette roles in `light-colour.md` (LC-04, LC-05), the UI system in `ui-ux.md` (UI-06, UI-07).

### SI-01 Style sets the emotional tone: set each lever on purpose
- principle: Every art style evokes a different emotion; the same gameplay in another style feels different. The levers are colour (saturation), character design, environments, how far proportions are pushed, and how values are structured (a designed "living painting" versus photoreal).
- why: Players read tone from colour and proportion before any rule: more colour and pushed proportions read light-hearted; less colour and real-world forms read serious; a designed value structure reads better than photoreal noise.
- apply: The art bible names the target emotion and sets each lever explicitly (palette saturation, proportion push, realism of props and environment, value structure); reference-image prompts state the levers, not just "stylised".
- check: A capture next to the art-bible anchors: `look_check.py palette` matches the bible's saturation range; head-to-body ratio matches the anchor character; grayscale shows the designed value groups.
- mistake: Mixing levers (pushed cartoony characters in a desaturated realistic world) so the tone is unclear [inference].
- examples:
  - R00a: PUBG versus Fortnite: similar gameplay, different tone from colour and proportion (R00a:175-219).
  - R01: League's style as a "living painting", not photoreal (R01:325-327).
- roblox_fit: Roblox audiences and the blocky avatar push many games toward bright, pushed styles; the choice must still be deliberate and consistent.
- roles: art-director, marketing, modeler, environment-designer, ui-ux-designer, vfx-designer, reference-images
- also: light-colour, character-design, value-contrast
- sources: R00a-F04 (R00a:175-219); R01-F22 (R01:325-327)

### SI-02 Every shape and colour has a job in conveying the idea
- principle: Shape language and colour must each convey the idea, and it shows the moment the work is seen. A design is done when every shape has a goal and no shape is random; in a clean style, no transparent overlays and little airbrush.
- why: Viewers read shape and colour first, so a mismatch shows instantly; purposeless shapes and soft overlays read as noise and unfinished work.
- apply: In review, write one line each on how the shape language and the colour say the idea; list each shape's job and remove shapes without one. Clean styles avoid semi-transparent overlays and soft gradients in textures and UI.
- check: The review has a line for shape and a line for colour linking each to the idea; the count of unexplained shapes is 0; scan for semi-transparent overlay layers and soft airbrush gradients in clean styles.
- mistake: Transparent overlays and airbrush that make key art look "unfinished" (R05:821-829).
- examples:
  - R00a: exploring visually reveals what the constraints allow; shape and colour show the idea at once (R00a:1002-1012).
  - R05: the VALORANT clean visual pillar (R05:817-829).
- roblox_fit: Semi-transparent parts also cost rendering [unverified].
- roles: art-director, modeler, vfx-designer, ui-ux-designer, environment-designer, reference-images, reviewer
- also: shape-silhouette, light-colour, visual-hierarchy
- sources: R00a-F28 (R00a:1002-1012); R05-F33 (R05:817-829)

### SI-03 Theme fit can rule out an otherwise cool idea
- principle: Lore, setting and tone limit which ideas fit; an option that reads as the wrong genre or tone is rejected even if it is cool.
- why: An idea that fits one game breaks another's tone; the world's promise must stay consistent.
- apply: The art bible and game profile state lore, setting and tone words; every option prompt and review rubric carries them; options outside are rejected at brief stage.
- check: Each option is placed next to 2-3 approved anchors and checked against the tone words; it fails if it reads as a neighbouring genre.
- mistake: A great idea in the wrong game; keeping a cool option that "doesn't really fit" (R13:52-54).
- examples:
  - R00a: a dubstep gun suits Saints Row but would be out of place elsewhere (R00a:620-630).
  - R13: option 1 felt too sci-fi for the whimsical Space Gods set (R13:52-56).
- roblox_fit: No change.
- roles: art-director, game-designer, vfx-designer, sound-designer, modeler, ui-ux-designer, environment-designer, marketing, reference-images, reviewer
- also: references-ideation
- sources: R00a-F15 (R00a:620-630); R13-F02 (R13:52-56)

### SI-04 Theme cues so a place is not generic
- principle: A themed setting carries signature cues across its surfaces so players read the theme, not an ordinary place (crystals in the sand and translucent crystal rocks for an "outer space desert").
- why: Plain sand and rock read as an ordinary desert.
- apply: For each setting list 2-3 signature materials or cues from the art bible and apply them across ground, rocks and debris [inference for Roblox materials].
- check: A fresh agent shown a capture without UI names the setting's theme correctly.
- mistake: "The scene looks too terrestrial" (R13:834).
- examples:
  - R13: crystals added to sand and rocks after "too Shurima, not spacey enough" feedback (R13:380-386, 813-814, 834-842).
- roblox_fit: Glass and Neon materials can give translucent or glowing crystal cues [unverified].
- roles: art-director, environment-designer, modeler, vfx-designer, reference-images, level-design, reviewer
- also: world-level-readability, materials-detail
- sources: R13-F16 (R13:380-386, 813-814, 834-842)

### SI-05 Make it for a specific audience, and give fans what they want
- principle: Not everyone will like every idea; the most appealing work is made for a specific audience, aiming for them to be thrilled rather than everyone being okay. Work to their need, not the maker's taste: find out what fans of that character or game want to see.
- why: Broad compromise produces bland work no one loves; the audience's excitement is the measure of success.
- apply: Briefs and pitches name the target player and a one-line "fans want" collected from player sources (Discord, comments, live-ops feedback, analytics); options are judged by that audience's likely excitement.
- check: The brief names the audience and the "fans want" line; the option choice cites it; the output shows the fan-expected trait at its strongest.
- mistake: Work "everyone is simply okay with"; making what you like instead of what the audience wants.
- examples:
  - R00a: some colleagues may come "with pitchforks" and that is acceptable (R00a:1036-1056).
  - R08: Kobuko fans want someone "joyful to almost an insane amount" (R08:364-409, 841-850).
- roblox_fit: Roblox audience segments (age, genre fans) are distinct; pick one [inference]; load `analysis-design` for evidence.
- roles: game-designer, art-director, marketing, live-ops-designer, animator, sound-designer, orchestrator
- also: character-design, game-design-fun
- sources: R00a-F29 (R00a:1036-1056); R08-F17 (R08:364-409, 841-850)

### SI-06 Match the game's look, not your own habit
- principle: Fight the instinct to make what you are comfortable with; assets must look like the game's aesthetic, not the maker's default.
- why: A cast made by many hands must feel like one world; personal habits break cohesion.
- apply: Check every new asset against the art-bible anchors, not against the maker's default; image prompts carry the art bible's style words, not generic ones. For AI makers the "habit" is the model's generic default look [inference].
- check: Place the new render next to 2-3 approved anchors at the same size: it looks like the same game.
- mistake: Characters that "look like your own aesthetic too much" (R03:394).
- examples:
  - R03: her habit of cute faces; a mentor pushing her to model a heavy male character (R03:390-400, 576-600).
- roblox_fit: Same; counters the generic AI look [inference].
- roles: modeler, art-director, reference-images, ui-ux-designer, vfx-designer, reviewer
- also: critique-feedback, character-design
- sources: R03-F17 (R03:390-400, 576-600)

### SI-07 Decide the stylisation level; hint at reality, do not copy it
- principle: Stylisation decides how much detail and material to show and must match between characters and environment; too little detail reads flat and unbelievable. A stylised object hints at its subject (a statue suggests the creature) rather than copying it.
- why: A character-environment mismatch reads as two games; stylisation adds magic and fits the game look.
- apply: The art bible states the detail level per material and per asset type; prompts ask for stylisations ("a stone idol stylisation of X"); modelers simplify anatomy to bold planes.
- check: A character-in-environment capture reads as one style family; black-fill reads as the subject while proportions are designed, not realistic.
- mistake: Rocks "becoming very flat, and cartoony and unbelievable" (R02:542-544); stylised characters in realistic environments.
- examples:
  - R02: questioning stylised characters on realistic environments; deciding detail per material (R02:530-544).
  - R02: old Indonesian statues that only hint at the animal (R02:222-228).
- roblox_fit: Simplified forms also save triangles.
- roles: art-director, environment-designer, modeler, reference-images, character-rigger
- also: materials-detail, shape-silhouette
- sources: R02-F28 (R02:530-544); R02-F12 (R02:222-228)

### SI-08 A deliberate blend of named sources makes a style
- principle: A recognisable style can come from deliberately blending two sources (Western and Eastern game art), taking named elements from each.
- why: A deliberate blend reads as an identity instead of a copy of one source.
- apply: The art bible names its 2 sources and what is taken from each (for example face simplification from one, material rendering from the other) [inference].
- check: The art bible lists sources and what comes from each; new anchors show both.
- mistake: An unnamed mix that drifts toward one source [inference].
- examples:
  - R03: World of Warcraft plus Final Fantasy: simplified face, line-art hair technique (R03:698-710).
- roblox_fit: Same.
- roles: art-director, reference-images, modeler
- also: references-ideation
- sources: R03-F30 (R03:698-710)

### SI-09 One palette per group so a roster reads as a team
- principle: When many characters share one board, give each group a dictated palette and fit every member to it, so they "feel like a team".
- why: Shared colour ties units into one universe and lets players group them at a glance.
- apply: The art bible defines a palette per faction or trait (named swatches with hex values); every character sheet prompt cites it.
- check: `look_check.py palette --roles` on the new sheet against the faction swatches; a capture of the new character next to 2-3 group members reads as one set.
- mistake: Each skin selling its own separate palette on a shared board.
- examples:
  - R08: Alune recoloured to the Anima Squad palette of light blues and pinks (R08:98-112).
- roblox_fit: Works with Color3 on parts, SurfaceAppearance tints and UI colours; keep group colour readable under the game's Lighting [inference].
- roles: art-director, modeler, vfx-designer, ui-ux-designer, marketing, environment-designer, reference-images
- also: light-colour, character-design
- sources: R08-F02 (R08:98-112)

### SI-10 Proportions are read against the cast
- principle: Body type tells story and is judged against the roster on screen: in a cast that grew beefier, a character reads thinner even with more muscle.
- why: Players compare characters on the same screen.
- apply: Compare every new character's proportions with the roster anchors and set its relative place (thinnest, average, bulkiest) on purpose.
- check: A lineup render of the new model next to the roster at the same scale shows the intended relative place.
- mistake: Proportions set in isolation [inference].
- examples:
  - R11: Katarina "will feel appropriately thinner" while getting more muscle (R11:209-211).
- roblox_fit: Same for avatars, NPCs and pets.
- roles: art-director, modeler, reference-images, game-designer, character-rigger
- also: character-design, shape-silhouette
- sources: R11-F18 (R11:209-211)

### SI-11 An update keeps the kernel and trims what is dated
- principle: A character or asset update brings what players love to the front, trims what feels dated, and aligns with the strongest canon.
- why: Players imagine a character beyond what is in the game; the update should meet that image without becoming "a parody of herself".
- apply: Before a remake, list loved traits and dated traits; anchor images come from the strongest canon.
- check: The remake review lists each loved trait as kept and each dated trait as trimmed or justified.
- mistake: A character feeling "like a parody of herself" (R01).
- examples:
  - R01: Caitlyn's update informed by the 2020 cinematic and Arcane (R01:441-478).
- roblox_fit: No change.
- roles: art-director, modeler, reference-images, marketing, live-ops-designer, game-designer
- also: character-design
- sources: R01-F30 (R01:441-478)

### SI-12 Each theme needs its own niche
- principle: Themes easily overlap ("bump elbows"); each new theme or event needs a distinct, expressive niche that does not cross too much with existing ones.
- why: Overlapping themes dilute each other and feel repetitive.
- apply: Before a new theme or event, list existing themes and state the new one's differentiator in one line.
- check: Side-by-side moodboards of the new theme and its nearest existing one: a fresh agent tells them apart.
- mistake: Themes with shared inspiration blurring together.
- examples:
  - R01: the Project and Mecha skin lines (R01:799-807).
- roblox_fit: No change.
- roles: art-director, game-designer, live-ops-designer, marketing, orchestrator
- also: references-ideation
- sources: R01-F45 (R01:799-807)

### SI-13 Refresh a tone by pushing to the extreme, then pulling back to the brand
- principle: Explore the extreme tone first ("let's go cheesy first"), then pull back and add the brand edge. Even popular lines get refreshed by pushing them in a new direction (darker, more aggressive) and exploring new corners of their world.
- why: The extreme shows the range; pulling back keeps identity; refreshes keep a line fresh while keeping its fans.
- apply: For event tone (names, taglines, sound, UI flair) make one extreme pass and one brand-aligned pass; the owner picks. Live-ops states the tone shift for each recurring event or line in its brief.
- check: The final still passes the brand checks (fonts, palette, shapes) while keeping the event tone; each iteration's brief names its tone shift against the last.
- mistake: Repeating the same tone until stale; a push with no pull-back that loses the brand [inference].
- examples:
  - R05: "never back down until you're dead again": bad in a good way (R05:293-295, 589-595, 896-900).
  - R01: Star Guardian 2019 pushed the magical-girl line darker (R01:841-854).
- roblox_fit: Live-ops cadence is weeks, not years [inference]; names and taglines the studio writes are not player text; any player-entered or generated text the event shows is filtered on the server (`platform-policy` `references/rules.md` §D; knowledge/external/roblox-creator-docs/ui/text-filtering.md:11-40) (lead fix 2026-10-22: the filtering rule covers text the game does not control).
- roles: marketing, art-director, game-designer, sound-designer, ui-ux-designer, live-ops-designer
- also: character-design, references-ideation
- sources: R05-F39 (R05:293-295, 589-595, 896-900); R01-F48 (R01:841-854)

### SI-14 Names and logos: keep the brand pattern, change one thing
- principle: Update names follow one pattern, and logo type stays in the brand fonts and lock-up with one modification unique to the event: "as close as possible to the brand but still feel unique".
- why: Players recognise the series instantly and still see that something is new.
- apply: The game profile holds the naming pattern and brand font set; each event varies one property (texture, colour, an ornament) on the logo component in Figma, never a new font.
- check: The new logo next to the previous two reads as the same game at thumbnail size and differs in exactly one visible property; the name follows the pattern.
- mistake: A new font or free-form name per event [inference].
- examples:
  - R05: "Resurrection" fits the "-tion" episode names; the bold lock-up gets grit for Halloween (R05:63-77, 293-301, 391-395).
- roblox_fit: Logos and titles on thumbnails and in-game UI must survive phone size [unverified].
- roles: marketing, live-ops-designer, ui-ux-designer, art-director
- also: ui-ux
- sources: R05-F02 (R05:63-77, 293-301, 391-395)

### SI-15 Draw graphic motifs from the game's own UI and story
- principle: Each release gets graphic shapes tied to its story or key art, taken from what players see in play (an in-game icon becomes the motif).
- why: Motifs from the game connect marketing to the play experience.
- apply: Event frames, banners and logos borrow a shape from the game's UI icons or the story's key object.
- check: The motif is traceable to an in-game icon or story element.
- mistake: Generic decorative shapes with no link to the game [inference].
- examples:
  - R05: the in-game defender icon as the motif for "defending yourself" (R05:766-775).
- roblox_fit: No change.
- roles: marketing, ui-ux-designer, art-director, live-ops-designer
- also: ui-ux, shape-silhouette
- sources: R05-F30 (R05:766-775)

### SI-16 Style rules may bend for a format, as logged exceptions
- principle: A piece that imitates a format (a movie poster) may use that format's conventions even when they break the house style (soft smoke and sparks in a flat, clean style).
- why: The format's expected conventions carry the joke or the energy.
- apply: Record exceptions per format in the art bible; event or parody pieces may use them; normal assets still follow the base rules.
- check: Every exception in a piece is listed in the bible with its format; normal assets pass the base rules.
- mistake: Exceptions leaking into normal assets [inference].
- examples:
  - R05: smoke and sparks on the poster: "we can get away with that" (R05:880-891).
- roblox_fit: No change.
- roles: marketing, vfx-designer, art-director
- also: vfx-reads-timing
- sources: R05-F34 (R05:880-891)

### SI-17 Brand first, hidden story second
- principle: The theme must read at once; a deeper story is a second layer that rewards those who look and never competes with the first read. "The brand is number one, the story is number two."
- why: Players read the main identity at a glance; a hidden layer adds depth and discovery without clutter.
- apply: Brief every themed asset with two lines: (1) the one-glance read (theme, rarity, role); (2) an optional hidden story element sized as a small or medium detail; prompts state the main read first. Progressive reveals (a part that opens after N uses) deliver the story over time [inference].
- check: At thumbnail size (`thumb_check.py`) and the game camera a reviewer names the theme without explanation; the story element is invisible at that size but findable close up.
- mistake: Making the story so obvious it becomes the main read.
- examples:
  - R12: a line-graph shape and a rose that opens after 24 kills behind the clear theme read (R12:19-34).
- roblox_fit: Hidden layers survive only as close-up or inspect details (shop preview, inventory view) [unverified].
- roles: art-director, modeler, vfx-designer, marketing, reference-images
- also: visual-hierarchy, game-design-fun
- sources: R12-F01 (R12:19-34)

### SI-18 A variant changes the palette; the same character in a new scene keeps it
- principle: A skin uses a different palette (and hair colours) to mark a different version; an in-canon scene of the base character keeps the base palette.
- why: Palette is a main identifier: changing it says "another version", keeping it says "the same one".
- apply: For any variant, record whether it is a new version (new palette) or the same character in a new situation (base palette).
- check: `look_check.py palette` of variant against base: the change matches the recorded type.
- mistake: A skin that looks like the base from a distance [inference].
- examples:
  - R10: Windfisher Yasuo keeps the base colours because it is "weekend Yasuo", not a skin (R10:528-541).
- roblox_fit: Small screens rely on palette even more [inference].
- roles: art-director, modeler, marketing, live-ops-designer, reference-images
- also: character-design, light-colour
- sources: R10-F18 (R10:528-541)

### SI-19 A cohesive set, with a documented break for the top tier
- principle: Standard items follow the guides that keep the product cohesive; the rarest tier may break the mould on purpose so it looks special beyond its rarity number.
- why: When everything is cohesive nothing stands out; a deliberate break signals rarity.
- apply: The art bible defines the standard look; a rarity tier may have a documented exception (style, finish, effect) decided by the art director and logged as an owner decision.
- check: Standard items pass the art-bible check; top-tier items are visibly different and the difference is written in the bible, not accidental.
- mistake: Every tier looking the same, so rare is only a bigger number (R10:259-263).
- examples:
  - R10: overnumbered alternate-art cards in each artist's own style (R10:30-36, 210-225, 253-263).
- roblox_fit: The owner decides any style exception; paid-random rarity also needs a `platform-policy` review.
- roles: art-director, live-ops-designer, progression-designer, marketing, game-designer, reviewer
- also: game-design-fun
- sources: R10-F10 (R10:30-36, 210-225, 253-263)

### SI-20 Premium tiers get separable finishes
- principle: For the highest tier, design elements that can each take a different finish (gloss, foil, matte, texture); mixed finishes make it feel premium.
- why: Distinct material treatments per element signal value and rarity.
- apply: Split premium cosmetics, cards or reward frames into separately treatable parts: separate MeshParts or materials (shiny against matte), a UIGradient shimmer on frames, a Highlight or particle sparkle on one element only.
- check: List each element and its finish: at least 2 finishes differ; the premium version reads differently from the standard at thumbnail size.
- mistake: One flat surface that can take only one treatment [inference].
- examples:
  - R10: glossy wet fish, foil scales, a high-gloss line (R10:136-146, 557-568).
- roblox_fit: No custom shaders, so finishes come from materials, SurfaceAppearance, UIGradient, Highlight (max 255 per client: knowledge/external/roblox-creator-docs/effects/highlighting.md:37) and particles.
- roles: marketing, art-director, ui-ux-designer, vfx-designer, modeler, live-ops-designer, progression-designer
- also: materials-detail, game-design-fun
- sources: R10-F06 (R10:136-146, 557-568)
