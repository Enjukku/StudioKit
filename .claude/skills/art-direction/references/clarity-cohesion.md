# Clarity, hierarchy, shape, value, color, light and cohesion

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-direction`. Sources: `knowledge/reference/art-direction/02` §3-5, `03` §1-2, `05` §2. Tags: S = studio account or published guide, R = owner-supplied transcripts (first game), P = the paper's proposal (OPINION), O = owner ruling. Rebuilt by J018 maker art-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): value bands per layer, reserved colours, one key light, read order, sections 6-8; repair round 1: band numbers kept only in the bible's §7, the one-sun scope; repair round 2: the anchor count by pointer. The standards live here; the checks that prove them are lines of `art-review/references/self-review.md` (ids in brackets). Studio names: `precedents.md` only.

## 1. Clarity starts from the player's decision
| Task | What the capture must show | Src |
| --- | --- | --- |
| Targeting | the target separated from its surroundings; its facing | P (02:RD14) |
| Navigation | the route, the destination cue, a landmark from every fork | P |
| Interaction | the affordance and its current state; what the piece is and what you can do there | P |
| Combat | source, path, area and result of the action; the threat's tell | P |
| Collection | identity and rarity of a pickup on the ground, even partly hidden, without making every object loud | P |
| Choosing (turn, card, menu or build decision) | every option's real state, side by side; emphasis shows state, never advice: a cue's strength is read as "this is the right move" unless the rules make it so | P (02:RD13; 01:LL-05) |

Ask for every moment: what must be noticed, told apart or predicted now; what competes; what confusion costs. A calm collector game and a threat-heavy game need different emphasis even with the same cast; never push competitive-combat urgency onto a calm game (02:D2, RD13, RD15). The strictest priority goes where the most intense play happens: test the read in the busiest expected moment, never in an empty scene [RD1].

**Weak read → missing contrast, never missing detail.** When something does not read, list the contrasts it must win against its surroundings (value, hue, saturation, shape, size, position, motion) and change one that ties or loses; added detail adds noise and usually lowers the contrast that was there [RD2].

**Fragile cues.** Very thin lines alias or vanish at phone resolution; check the real raster width of every critical line at the declared device size (02:M14). There is no universal minimum width; set it from the project's own captures (02:RD7). Grayscale or one color-vision simulation alone does not prove a cue works for color-blind players; add a non-color channel and, when practical, test with affected players (02:M6) [CL3].

**Primitive check.** If a character cannot be drawn recognizably as a crude placeholder, its silhouette is weak (02:RD9). AI version: remove texture and light, keep the gameplay camera, ask which identity features survive; a model's confident label is not a human recognition rate (02:RD11-RD12) [SH1].

**Recognisable in under a second beats unique.** Among options pick the one players identify correctly at a glance (subject, owner, function), then add uniqueness inside that read; a new design that resembles a roster neighbour fails even when its shape is more interesting [SH7].

## 2. Hierarchy
1. **Rank what must be seen** for this moment: must notice now / read next / atmosphere. Only the top 1-2 get high contrast (R 05:AF02). Default screen order: UI and gameplay VFX first, characters second, environment last; an environment element that out-contrasts a character or an effect is a finding [RD2].
2. **Contrast channels:** value, saturation, hue, shape, size, detail density, motion, timing. Critical items use more than one; colour alone fails colour-blind players and phones in sunlight (R 05:AF04).
3. **Lower the neighbours instead of only raising the target** (R 05:AF03). The space between two focal zones gets fewer details and lower contrast; background detail is blocked in values close to the background's own [RD4].
4. **Value bands per layer** (numbers: the bible's band, starting values in `art-review/references/art-bible.md` §7): the environment takes the narrowest band, never pure black, one controlled saturation band; characters a little wider; VFX and UI own the extremes. The widest band wins attention, so the order of the bands is the screen order. Phones in sunlight compress contrast: keep margin between bands [RD3].
5. **Extremes are small.** Pure white, pure black, the most saturated colour and glow go only to small focal spots (highlights are "the smalls" on a calm canvas); a large clipped area or two competing peaks is a finding [RD5].
6. **Read order.** Every key art, shot, scene or screen states its primary, secondary and tertiary reads; flow lines (a path, a rope, a light shaft) point to the primary; on phones plan two reads where you can [RD2].
7. **Light points:** a bright spot draws the eye, darkness hides; the brightest area is the focus (R 05:AF07). A bright focal light can also hide a staged surprise in the darker side.
8. **Distance reads simpler:** less detail, contrast and saturation far away, unless the bible chooses a flat look (R 05:AF06); a small, low-contrast busy background (a distant crowd, far activity) adds life while it reads as texture in the squint view [RD9, RD8].
9. **Layer cut:** compare the scene without UI, without effects and composed; if removing a layer makes the action readable, that layer competes (P 02:HI3) [K09].
10. **Calm space is a resource** (a quiet wall behind a character, quiet area near key UI, a pause between bursts); richness is fine where it does not compete with the current task (P 02:HI4) [RD8].
11. **Protected interaction space vs expressive staging:** keep critical geometry, readable materials and a calm, neutral player band (floor to head height); decoration and the most saturated colour go above head height or at the edges; story may extend into spaces players cannot reach (S 02:HI5; `precedents.md` §2) [CL9]. Test hierarchy at the lowest supported quality too; a cue that exists only in the premium render is not a style (P 02:HI7) [RD12].
12. **Contrast carries intensity.** Push value contrast for dramatic moments (boss reveal, climax, promo), keep calm places narrower; the same contrast everywhere loses the meaning [RD10].
13. **Size signals importance:** the most dangerous enemy, the biggest reward, the main objective are the biggest on screen; size consistent with rank across the roster [SH6].

## 3. Shape, value, color
| Topic | Practice | Src |
| --- | --- | --- |
| Shape language | Fix this game's shape meanings in the bible and test them; spiky = danger, round = friendly, square = stable is a hypothesis, not a law; the personality shape sits on high-presence zones (head, shoulders) | P 02:SH1; R 05:AF08 |
| One vocabulary | The style lives as much in the small shapes (trims, ornaments, particle shapes, UI corners) as in the big ones; off-vocabulary shapes are rare and deliberate | J018 |
| Iconic elements | a few elements (the identity anchors; count: `art-review/references/art-bible.md` §7) make a thing recognizable; when small, simplify to them, make them chunky and push them; remove every small thing that does not improve the read | R 05:AF11 |
| Silhouette | solid shape at the real camera distance and angle; a few broad cuts, never small notches; two different things never share one; size ranks importance | R 05:AF12-AF13 |
| Size steps | sibling shapes in a group step big, medium, small (starting value about 3 : 2 : 1); two neighbours within about 15 % of each other compete (PROPOSAL) | J018 |
| Motifs | one motif repeated at big, medium and small scale and across the set (costume, weapon, icon, effect), built from a few basic shapes, never a pasted 1:1 copy | J018 |
| Proxy first | big blocks of shape and color tested in game before detail; test extreme poses before polish | R 05:AF14-AF15 |
| Value | check hierarchy with hue removed, with a named conversion (WCAG luminance in `look_check.py`); compare the key object against its local surround, not the frame average; parts separate by value and shape, never only by lines or outlines | P 02:SH3, M1-M2 |
| Value grouping | the detail materials of one object sit in one close-value family, framed by a contrasting base colour, so it reads as one object; high-contrast features are spaced like letters in a word (too dense is a shimmer, a lone outlier steals the eye) | J018 |
| Character value | head, shoulders, hands and the held item carry the most contrast and refinement; the lower body a little darker and cooler, still separate from the ground; joints that matter get a value break so limbs track | J018 |
| Color roles | write roles first (background, identity, interaction, team, danger, reward, disabled, narrative emphasis), counts never; one hue never means both help and harm; non-color backup for essential states | P 02:SH2, M4; Xbox guideline 103 (FC-A) |
| Reserved colours | the bible's reserved hues (danger, enemy, team, interactable, route) carry a saturation limit for set dressing and a share near zero outside gameplay objects; a hazard that must be red is tamed (toward orange, lower emission) so characters still separate in front of it | J018 |
| Palette roles | after the greys work, mostly three colours: dominant on the big shapes (about 60 %), support on the mediums (about 30 %), accent on small highlights (about 10 %); a scene or event may commit to one dominant hue; new colours are taken from the palette already there | J018 |
| Rich colour | shadows and highlights shift hue (a red coat's shadow goes toward purple, its highlight toward orange), never just toward black or white; light and shadow take opposite temperatures, one direction per scene; no flat fills: small hue and value shifts inside a material; gold stays saturated in shadow | J018 |
| Saturation field | calm the large areas a little, let small saturated accents sit on focal spots; a saturated accent on a background figure pulls the eye to it on purpose | J018 |
| Colourways | once the silhouette is locked, colour is tried with global moves and 3-5 colourways (post effects in Studio, material swaps in Blender); each colourway is the same object and its grey is re-checked | J018 |
| Overlaps | same-hue parts merge where they overlap (red gloves in front of red hair; an effect over its own caster): they differ in value or hue, or the idea is dropped | J018 |
| Gamut | pick a dominant gamut per area and reserve out-of-gamut colors for deliberate emphasis; the nine-swatch exercise is a teaching tool, not a palette limit | 01:TS-GU; P |
| Lit color | a swatch, a render and a post-processed screenshot are three kinds of evidence; check the lit result; a balanced grey pass does not stay balanced after colour, effects or light change: rebalance | P 02:SH4, 03:QT6 |
| Character vs world | environment and signage contrast stays below character contrast; test every reachable view | S 01:TS-LU |

## 4. Light and mood
- State the impression a lighting direction must give and the information it must keep (material separation, route, character identity, interaction, danger). Dark, foggy or saturated is allowed on purpose; the test is whether the decisions still work on supported settings (P 03:LM1).
- **One key light direction per place**, set in the bible (Lighting.ClockTime and GeographicLatitude for the sun) and never moved during the work. Lighting is global: one sun per Roblox place, so two areas of one place differ by local lights, post effects under the camera or a client-side Lighting change (probe in Studio first), never by two suns (the bible's key light row); every asset is painted, rendered and judged as lit from it, at the game camera. Up-facing and light-facing planes are the brightest. A day-night cycle keeps painted light soft so it never fights the live sun (J018) [CL8].
- **Light is motivated:** sky light and sun outdoors; a torch, window or screen motivates its own local light; every light has a visible or implied source and shadows agree (J018) [CL8].
- **Choose light on the rough.** Compare 2-3 lighting variants of the blockout or rough at the game camera (grey captures) before anyone details; record the chosen key and fill (J018).
- **Light leads the eye:** lighter values and the strongest local light toward the goal, door, pickup or hero; surroundings a little darker toward the edges; a few shadow-casting local lights at focal points, low ambient elsewhere. Rim light separates figures from a background of similar value; light from below reads threatening, from above or the side heroic (cutscenes and reveals use placed lights for this) (J018).
- **Shadows serve readability:** no key position sits in deep shadow where a player hides by accident; re-capture readability after every lighting change; nothing important relies on a shadow, because phones lower shadow quality (J018) [CL15, RD12].
- **Materials and light are chosen together:** key materials are judged under the place's final light at the game camera, not default light (J018) [MD6].
- Review material and light together; ask for neutral light, gameplay light and the problem scenario as isolating variants (P 03:LM2).
- Never approve in the best editor view only; decide what must survive lower quality and what may degrade. Bloom alone never carries importance; a danger edge shown only by a thin shadow is fixed with geometry, value or a redundant cue, not with higher settings (P 03:LM3, QT5, QT7).
- Roblox facts (lighting styles, quality priority, post effects, emissive masks, texture streaming, SLIM): `platform-evolution-marketing.md` §1 (checked in FC-A).
- Each place gets its own light mood; a first area usually reads bright and inviting, but the mood target is the game's (O 05:OR08). Use the engine's own lighting first; do not invent custom systems (O 05:OR09).

## 5. Cohesion across crafts
| Rule set | Must agree across |
| --- | --- |
| Color meaning (team, rarity, damage, reward, danger) | world, VFX, UI, icons, marketing |
| Shape meaning (heal, shield, damage, go) | VFX, UI, icons, telegraphs |
| Motion personality (snappy, heavy, floaty, bouncy) | animation, UI motion, VFX timing, camera (the bible's motion line) |
| Sound personality and loudness rank | SFX, UI sounds, music, ambience (the bible's sound section, owned by the sound designer) |
| Material and age language | structures, props, terrain, UI frames |
Source: synthesis of the transcripts in the first game (R 05:AF20).

- Cohesion = shared decisions, not identical techniques. Fix only what must agree (proportions where assets touch, color roles, material impressions, event importance, motifs, emotional register); each specialist owns its implementation and may propose a better one (P 03:CC1).
- **One target experience, signed by every craft:** each brief quotes the same target line from the direction sheet; a motif found in one craft (an illustration, a UI icon) is recorded in the bible so the others reuse it (J018).
- Per recurring event keep a cross-craft reference: clip with marked moments, image sequence, one-line meaning, owner of each component (P 03:CC3). A visual review never changes gameplay timing or damage; the timing contract is the animator's timing list, which VFX and sound key from.
- An effect's colour sits next to its caster's main colour on the wheel, with one main hue per effect, so players see who did it (J018) [CL10].
- Audience reading can differ from intent (S 03:TF1). Ask reviewers what genre, mood and role an image shows without telling them the intended label; name the cues that cause a mismatch (P 03:TF2) [ID7].
- World identity → visual grammar: districts or factions can share one rendering language with related but different materials, line rhythms and light motifs (P 03:AF3; the studio case is in `precedents.md` §2). Film can pool detail for one frame; games need cues that hold across changing cameras.

## 6. Materials and detail
- **Indicate, do not spell out.** Hair, fur, grass, crowds and materials read from a few clumps and tapered marks inside a correct value structure; the image must look good with or without the small details; a piece that only works zoomed in fails [MD1].
- **Budget detail by display size, camera distance and player speed.** In-game assets are functional; key art may be intricate. Areas players run past get macro forms only; stop points and landmarks get more; every side an orbiting camera reaches is finished [MD2].
- **Finish comes from crisp planes and edges, balanced with soft:** edge highlights on hard materials, not on every edge; organic transitions stay soft; a soft airbrush everywhere looks mushy, every edge hard looks stiff [MD3].
- **Block material regions before shading** so "which part is which material" stays clean; every material is identifiable at game size (gold reads gold, not bronze) [MD1].
- **Wear and condition tell the story:** wear where hands and feet go, grime where dirt gathers, condition chosen for the history (polished and new vs scrounged and worn), at the bible's stylisation level; controlled imperfection (small dents, uneven edges, one asymmetric element) keeps work from looking machine-made [MD4].
- **Functional parts and visible support:** a viewer can tell from one render how an object is held and used; cut motifs get braces or thickness so nothing reads fragile [MD7].
- **Ornament** is one shaped motif with a reason, added late and small; patterns sit on functional zones only and vanish at thumbnail size [MD8].
- **Ground every object:** a base or footprint, blended seams where meshes meet terrain, a hint of the object's colour on the ground; nothing floats or clips with a straight seam [MD5].
- **Stylisation level matches** between characters and environment; a stylised object hints at its subject, it does not copy reality (`identity-variants.md` §2).

## 7. Composition and the real frame
- **Big to small:** composition, big shapes and primary colour zones over the whole frame first; detail, smoke and sparks only after the layout is locked; the clean frame (no effects) must pass on its own [CP9].
- **Design for the side the camera shows** and judge through the game camera; detail goes where the camera sees it largest and least distorted; foreshortened or far parts keep big simple shapes (C-14).
- **Compose inside the real frame:** load the delivery overlay first (HUD and safe areas at phone size, the icon square, pass and badge circles, the 16:9 thumbnail with its bottom band); keep faces and focal objects out of overlay zones; lock a safe square around the crop, then move anything else [CP1].
- **In a small frame the identifying parts fill it:** heads and upper bodies big enough to identify, 1-2 marked anchors inside every crop, indicators near the centre of circular crops [CP2].
- **Shape flow points to the focal point** at every scale: paths, walls, roof lines, debris and light gradients converge on it; lines on one object run to shared points or parallel and continue across part joins [CP3].
- **Three depth groups:** a dark foreground frames, the midground carries the subject and most of the detail budget, the background takes global tweaks for unity; in gameplay a foreground object never blocks the play view [CP4].
- **Negative space on purpose:** calm room around the hero and the title; no accidental bare gaps [CP5].
- **The focal point is the tallest shape** in a place and is not occluded from the game camera [CP6].
- **Balance visual weight:** dark heavy masses pull to their side; place a brighter mass opposite so balance sits where planned [CP7].
- **Value gradient to the hero** in key art, thumbnails and cutscene frames: cooler and darker toward the edges, the brightest value on the hero's head or focal part [RD4].
- **Camera height states status** in icons, thumbnails, shop previews and cutscenes: looking up at a dominant character, eye level for a friendly one [CP8].
- **Judge on the integrated capture:** effects, lighting, other players and HUD on; any craft's change triggers a new integrated capture [CP9].
- **Motion in a still:** 2-3 committed flow lines through the focal point; small secondary accents (sparks, birds) along the eye path, smaller and quieter than the focus [CP3].

## 8. Places (what the art director asks of every environment)
- Every piece says what it is and what you can do there; a gameplay surface keeps one consistent treatment everywhere; materials follow the gameplay rule (one material per gameplay property) [WO1].
- The first view after spawn frames the goal or the main landmark as the strongest focal point [CP11].
- Each zone has an identity symbol or landmark with a unique black-fill silhouette, visible from its entry and from every route fork [WO1].
- A player-size reference in every blockout and scene; interaction props sized to the player first; a known-size object near every large focal prop [WO2].
- Someone lives here and time has passed: 3 story facts per place shown through props, wear and layout at backdrop contrast [WO3].
- Hazards explain where they come from and are contained by believable structure; boundaries are believable world pieces, never an obvious invisible wall [WO4].
- Floors in play areas stay clean enough for the smallest gameplay object; decorative ground cover is cut back to "a whisper" [RD7].
- Objectives are marked on the approach and in the floor; a head-height cue on long sightline walls where height matters [WO5].
- Build and judge the whole space, not the hero prop on a turntable [WO6].
- In a themed game the greybox already uses shapes that could be real structures of the theme, so art builds on a place, not on abstract boxes [WO7].
- The map is the board: a map mechanic's look (jump pads, doors, teleporters) stays quiet except at the moments design planned [EVT6].
