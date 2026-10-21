# Clarity, hierarchy, shape, value, color, light and cohesion

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-direction`. Sources: `knowledge/reference/art-direction/02` §3-5, `03` §1-2, `05` §2. Tags: S = studio account or published guide, R = owner-supplied Riot transcripts, P = the paper's proposal (OPINION), O = owner ruling.

## 1. Clarity starts from the player's decision
| Task | What the capture must show | Src |
| --- | --- | --- |
| Targeting | the target separated from its surroundings; its facing | P (02:RD14) |
| Navigation | the route and the destination cue | P |
| Interaction | the affordance and its current state | P |
| Combat | source, path, area and result of the action | P |
| Collection | identity and rarity without making every object loud | P |
| Choosing (turn, card, menu or build decision) | every option's real state, side by side; emphasis shows state, never advice: a cue's strength is read as "this is the right move" unless the rules make it so | P (02:RD13; 01:LL-05) |

Ask for every moment: what must be noticed, told apart or predicted now; what competes; what confusion costs. A calm collector game and a threat-heavy game need different emphasis even with the same cast; never push competitive-combat urgency onto a calm game (02:D2, RD13, RD15).

**Fragile cues.** Very thin lines alias or vanish at phone resolution; check the real raster width of every critical line at the declared device size (02:M14). There is no universal minimum width; set it from the project's own captures (02:RD7). Grayscale or one color-vision simulation alone does not prove a cue works for color-blind players; add a non-color channel and, when practical, test with affected players (02:M6).

**Primitive check.** If a character cannot be drawn recognizably as a crude placeholder, its silhouette is weak (Riot artist account, S 02:RD9). AI version: remove texture and light, keep the gameplay camera, ask which identity features survive; a model's confident label is not a human recognition rate (02:RD11-RD12).

## 2. Hierarchy
1. Rank what is on screen for this moment: must notice now / read next / atmosphere. Only the top 1-2 get high contrast (R 05:AF02).
2. Contrast channels: value, saturation, hue, shape, size, detail density, motion, timing. Critical items use more than one; color alone fails color-blind players and phones in sunlight (R 05:AF04; the order is a heuristic, check with grayscale).
3. Lower the neighbors instead of only raising the target (R 05:AF03).
4. Light points: a bright spot draws the eye, darkness hides (R 05:AF07). Lines and wedges lead the eye (R).
5. Distance reads simpler: less detail, contrast and saturation far away, unless the bible chooses a flat look (R 05:AF06).
6. Layer cut: compare the scene without UI, without effects and composed; if removing a layer makes the action readable, that layer competes (P 02:HI3).
7. Calm space is a resource (quiet wall behind a character, quiet area near key UI, a pause between bursts); richness is fine where it does not compete with the current task (P 02:HI4).
8. Protected interaction space vs expressive staging: keep critical geometry, readable materials and decorative detail above player height where players fight; story may extend into spaces players cannot reach (VALORANT environment account, S 02:HI5). Test hierarchy at the lowest supported quality too; a cue that exists only in the premium render is not a style (P 02:HI7).

## 3. Shape, value, color
| Topic | Practice | Src |
| --- | --- | --- |
| Shape language | Fix this game's shape meanings in the bible and test them; spiky = danger is a hypothesis, not a law | P 02:SH1; R 05:AF08 |
| Iconic elements | 2-3 elements make a thing recognizable; when small, simplify to them and push them | R 05:AF11 |
| Silhouette | solid shape at the real camera distance and angle; two different things never share one; size ranks importance | R 05:AF12-AF13 |
| Proxy first | big blocks of shape and color tested in game before detail; test extreme poses before polish | R 05:AF14-AF15 |
| Value | check hierarchy with hue removed, with a named conversion (WCAG luminance in `look_check.py`); compare the key object against its local surround, not the frame average | P 02:SH3, M1-M2 |
| Color roles | write roles first (background, identity, interaction, team, danger, reward, disabled, narrative emphasis), counts never; one meaning per treatment; non-color backup for essential states | P 02:SH2, M4; Xbox guideline 103 (FC-A) |
| Gamut | pick a dominant gamut per area and reserve out-of-gamut colors for deliberate emphasis; Gurney's nine swatches are a teaching exercise, not a palette limit | artist account (01:TS-GU), P |
| Lit color | a swatch, a render and a post-processed screenshot are three kinds of evidence; check the lit result | P 02:SH4, 03:QT6 |
| Character vs world | keep environment and signage contrast below character contrast (Pixar's Luca notes; a film with a fixed frame, so test every reachable view) | S 01:TS-LU |

## 4. Light and mood
- State the impression a lighting direction must give and the information it must keep (material separation, route, character identity, interaction, danger). Dark, foggy or saturated is allowed on purpose; the test is whether the decisions still work on supported settings (P 03:LM1).
- Review material and light together; ask for neutral light, gameplay light and the problem scenario as isolating variants (P 03:LM2).
- Never approve in the best editor view only; decide what must survive lower quality and what may degrade. Bloom alone never carries importance; a danger edge shown only by a thin shadow is fixed with geometry, value or a redundant cue, not with higher settings (P 03:LM3, QT5, QT7).
- Roblox facts (lighting styles, quality priority, post effects, emissive masks, texture streaming, SLIM): `platform-evolution-marketing.md` §1 (checked in FC-A).
- Each place gets its own light mood; a first area usually reads bright and inviting, but the mood target is the game's (O 05:OR08). Use the engine's own lighting first; do not invent custom systems (O 05:OR09).

## 5. Cohesion across crafts
| Rule set | Must agree across |
| --- | --- |
| Color meaning (team, rarity, damage, reward, danger) | world, VFX, UI, icons, marketing |
| Shape meaning (heal, shield, damage, go) | VFX, UI, icons, telegraphs |
| Motion personality (snappy, heavy, floaty, bouncy) | animation, UI motion, VFX timing, camera |
| Sound personality and loudness rank | SFX, UI sounds, music, ambience |
| Material and age language | structures, props, terrain, UI frames |
Source: synthesis of the Riot transcripts in the first game (R 05:AF20).

- Cohesion = shared decisions, not identical techniques. Fix only what must agree (proportions where assets touch, color roles, material impressions, event importance, motifs, emotional register); each specialist owns its implementation and may propose a better one (P 03:CC1).
- Per recurring event keep a cross-craft reference: clip with marked moments, image sequence, one-line meaning, owner of each component (P 03:CC3). A visual review never changes gameplay timing or damage.
- An effect or sound tied to its source's color or material tells the player who caused it (R).
- Audience reading can differ from intent: Riot's TFT team reports players read one set's look as a different genre than intended (S 03:TF1). Ask reviewers what genre, mood and role an image shows without telling them the intended label; name the cues that cause a mismatch (P 03:TF2).
- World identity → visual grammar: Fortiche says Arcane's Piltover draws on Art Deco and Zaun on Art Nouveau, with Mucha as the main reference (S 03:AF1, corrected FC-S SF40). The transfer is the paper's: districts or factions can share one rendering language with related but different materials, line rhythms and light motifs (P 03:AF3). Film can pool detail for one frame; games need cues that hold across changing cameras.
