---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J009-T03, Art_Director_Research_Paper.txt lines 603-754"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Art-direction paper part 3: light and mood, cohesion across crafts, consistency and anchors, direction and feedback (lines 603-754)

Paraphrased notes. The paper (AP) stays outside git. Every row cites `AP:<line>`. Nothing here is fact-checked yet: claims are the paper's, listed in section 11 for the fact-check pass. Paper date: 2026-10-21. The paper says it ran no image benchmark, no Roblox scene and no player study (AP:17), so every procedure below is a proposed check, not a measured result.

## 0. How to read

| Key | Meaning |
| --- | --- |
| AP:n | line n of `Art_Director_Research_Paper.txt`. One paragraph = one line. Source register = AP:1013-1695. |
| Tag | The paper's own marks. VERIFIED = published data, a measured study or an explicitly documented platform/tool capability (a capability is not proof of art quality). EXPERIENCE = a studio, artist or director describes its own process (not a rule for other games). OPINION = interpretation, proposed process or authored example; cited as `O00` = this paper itself, dated 2026-10-21, not an external study (AP:13, 15). |
| Src | paper source id plus its date. "undated, accessed 2026-10-21" = living page with no publication date; access date is not publication date (AP:15). |
| Kit | how the lesson relates to the kit as read for this ticket (`reference-images` SKILL, `references/prompt-patterns.md`, `tools/art/art_refs.py`, `templates/skill/art-bible.md`, `rules/messages.md`): **in kit** (already there, file named), **new** (not in the kit), **conflicts** (kit does something different; how). Only the files named were read. |
| Row IDs | LM light and mood, QT quality tiers, MS materials and streaming, CC cohesion, TF TFT, AF Arcane/Fortiche, CM consistency across makers, AN locked anchors, FB direction, FT template field, NO saying no, RB Roblox-only claim, SC studio claim, N number, C claim for fact-check, X contradiction or limit. |
| Order | Paper order. Paper section 7 = my section 1, 8 = 2, 9 = 3, 10 = 4. |

## 1. Paper section 7: lighting and mood (AP:603-641)

### 1.1 Mood must keep the information the player needs (AP:605-609)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| LM1 | 605 | Before approving a lighting direction, write down (a) the impression it must give and (b) the information that must survive it: material separation, route visibility, character identity, interaction, danger. Dark, foggy or saturated scenes are allowed when chosen on purpose. The pass question is "do the intended experience and the needed decisions still work under the supported conditions", never "is it bright". | OPINION | O00 | new |
| LM2 | 607 | Review material and light together. A painted highlight, a physically generated highlight and an emissive element can fight or contradict. An anchor made under one environment may not predict the material under another. Ask the specialist for isolating variants: neutral light, approved gameplay light, and the problem scenario. Keep the intent fixed and let the specialist change the implementation. | OPINION | O00 | new |
| LM3 | 609 | Never approve a direction only in the best-quality editor view. Decide which visual relationships must survive lower render quality and which may degrade. A decorative reflection can vanish. An essential indicator must not rely only on an effect that supported devices lack. The paper points to its platform section for real capabilities and says scene cost still needs measurement. | OPINION | O00 | new |

### 1.2 Lighting is an artistic contract across quality tiers (AP:611-619)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| QT1 | 613 | Write the current Roblox lighting properties into the bible. Do not tell agents to find an obsolete "Future" drop-down or to enable a beta that has finished. Facts behind it: RB1, RB2. | VERIFIED (facts); OPINION (advice) | P09 (2025-01-21; full release 2025-07-23); P08 (undated, accessed 2026-10-21); O00 | new |
| QT2 | 615 | Pick LightingStyle (Realistic or Soft) by tested art intent, not by the name. A softly shaded game can look premium. Realistic is a renderer option, not an aesthetic grade. Facts: RB3-RB6. | VERIFIED (facts); OPINION (advice) | P07, P08 (both undated, accessed 2026-10-21); O00 | new |
| QT3 | 617 | Write a lighting contract with these fields: global ambient relationships; outdoor/indoor transition; key/fill intent; colour-temperature roles; shadow importance; fog/atmosphere use; focal-light hierarchy; material response; permitted post effects (9 fields, my count). Numbers inside it are project choices until the owner approves them. | OPINION | O00 | new (template has no lighting contract) |
| QT4 | 617 | Capture two baselines with the chosen prioritisation setting: a near-object scene and a distant-navigation scene. Then compare the reduced-quality outcomes of both. | OPINION | O00 | new |
| QT5 | 617 | If a danger cue (the paper's example: a ledge shown only by a thin shadow edge) fails on the baseline device, fix geometry, value, signage or a redundant cue. Do not "fix" it by raising the beauty-render settings. | OPINION (authored example) | O00 | new |
| QT6 | 619 | Colour review records the tonemapper and the post-effect stack. A palette swatch, a Blender render and a post-processed Roblox screenshot are three different kinds of colour evidence, not interchangeable. Facts: RB7-RB9. | OPINION (advice); VERIFIED (facts) | P10, P11 (both undated, accessed 2026-10-21); O00 | new |
| QT7 | 619 | Test danger and interaction cues with post effects reduced or unavailable. Never use bloom alone to mark how important an object is. | OPINION | O00 | new |

### 1.3 Materials and streaming change the delivered image (AP:621-631)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| MS1 | 623 | Keep "this surface glows" apart from "this surface lights the room" in the bible. Ask for both only when the implementation gives both. Do not let faction-coloured emitters blow out to the same white. Facts: RB10. | VERIFIED (facts); OPINION (advice) | P21 (2026-02-12); O00 | new |
| MS2 | 625 | Tinting having no performance cost does not make a whole material pipeline free. Approve each material family in the engine under the intended light. A swatch lock holds the material and roughness treatment and the rendering context, not just a hex value. Give special treatments (such as emissive accents) only to the meaning they were declared for, so agents do not add competing accents. Facts: RB11. | VERIFIED (fact); OPINION (advice) | P22 (undated, accessed 2026-10-21); O00 | new (template locks hold no material or context field) |
| MS3 | 627 | An 8K upload is not 8K on a phone. Do not treat the dated support list as permanent. Review low-mip silhouettes and essential markings apart from optional close-up detail. Direction arrows and faction identity must not depend only on tiny texture features that stream away. Facts: RB12, RB13. | VERIFIED (facts); OPINION (advice) | P12 (2026-01-30); P13 (2025-12-12, update 2026-03-23); O00 | new |
| MS4 | 629 | Compare landmark, body-shape and group-composition readability between the full and the lightweight (SLIM) version of a model, not just the asset's close-up mesh. Note: "static only" is outdated for supported avatars, but "all animated characters are supported" is also false. Facts: RB14, RB15. | VERIFIED (facts); OPINION (advice) | P14 (2025-10-30; updates 2025-12-09, 2026-02-25); P15 (2026-05-12); O00 | new |
| MS5 | 631 | Use the SLIM debug tints to tell "art lost at distance" from "wrong representation is loading". Keep an untinted capture for real colour review. Debug colours are overlays, not the shipped palette. Facts: RB16. | VERIFIED (facts); OPINION (advice) | P16 (2026-10-09); O00 | new |

### 1.4 Roblox lighting, material and streaming claims (listed apart: check against the Roblox docs)

All are the paper's reading of the cited page at its date. None was verified by me. The local mirror is `knowledge/external/roblox-creator-docs/` (AGENTS.md section 0).

| ID | AP | Claim as the paper states it | Tag | Src and date |
| --- | --- | --- | --- | --- |
| RB1 | 613 | Unified Lighting became fully live in July 2025. Old Future settings map to LightingStyle Realistic with PrioritizeLightingQuality enabled. | VERIFIED | P09; original 2025-01-21, full release 2025-07-23 |
| RB2 | 613 | `Lighting.Technology` is deprecated. | VERIFIED | P08; undated, accessed 2026-10-21 |
| RB3 | 615, 635 | LightingStyle offers two values: Realistic and Soft. | VERIFIED | P07; undated, accessed 2026-10-21 |
| RB4 | 615 | PrioritizeLightingQuality chooses whether lighting/shading quality or view distance is kept first as render quality falls. True favours nearby advanced lighting, false favours distance. | VERIFIED | P07; undated, accessed 2026-10-21 |
| RB5 | 615, 637 | ShadowSoftness runs 0 to 1 and is documented as valid with Realistic. | VERIFIED | P07; undated, accessed 2026-10-21 |
| RB6 | 615 | Soft is not one fixed shadow implementation: its path also depends on PrioritizeLightingQuality. Soft with that setting on uses shadow maps, not voxel lighting. | VERIFIED | P08; undated, accessed 2026-10-21 |
| RB7 | 619 | Post effects: bloom, blur, colour correction, depth of field, sun rays, colour grading. Effects under Lighting are global. Effects under Camera show only to that player. Some do not appear at lower Studio quality settings. | VERIFIED | P10; undated, accessed 2026-10-21 |
| RB8 | 619 | ColorGradingEffect has two tonemapper presets, Default and Retro. They change the conversion to display colour. Retro imitates the pre-2019 look. | VERIFIED | P10; undated, accessed 2026-10-21 (sentence-to-page mapping not line-exact in the paper) |
| RB9 | 619 | `Bloom.Size` is a radius in pixels. Bloom rendering can differ with quality settings. | VERIFIED | P11; undated, accessed 2026-10-21 (same caveat) |
| RB10 | 623 | Emissive Masks work in published experiences, across clients, on SurfaceAppearance, MaterialVariant and TerrainDetail. A mask is grayscale intensity; only the red channel of an RGB mask sets intensity. Glow colour comes from the colour map and tint. The announcement says the glow is not a dynamic light on nearby geometry. | VERIFIED | P21; 2026-02-12 |
| RB11 | 625 | SurfaceAppearance gives PBR texture-driven appearance and supports tinting. The docs state tinting does not affect performance. | VERIFIED | P22; undated, accessed 2026-10-21 |
| RB12 | 627 | Roblox enabled up to 4K texture rendering through texture streaming, when the client has resources and the view justifies it. | VERIFIED | P12; 2026-01-30 |
| RB13 | 627 | Source images can be stored up to 8K; that is storage, not runtime resolution. The rollout update lists low-end Android below 3.5 GB with 4K disabled, and these unsupported texture classes at that snapshot: 2D UI/SurfaceGUI, Terrain/TerrainDetail, sky, bundled materials. | VERIFIED | P13; 2025-12-12, rollout update 2026-03-23 |
| RB14 | 629 | SLIM builds lightweight composite stand-ins for streamed-out models in streaming-enabled places. Available on all platforms in Client Beta. | VERIFIED | P14; 2025-10-30, updates 2025-12-09 and 2026-02-25 |
| RB15 | 629 | Later support covers R15 platform avatars with restrictions. Creator-controlled NPCs and later avatar modifications are not generically covered by that first release. | VERIFIED | P15; 2026-05-12 |
| RB16 | 631 | SLIM debug tints show streaming state, detail level and transcoder status. Players reach them through Developer Console debug visualisations (needs Edit permission). Studio needs a beta plus Visualization Modes. | VERIFIED | P16; 2026-10-09 |

### 1.5 Paper table AP:633-639

| AP | Rule | Number | Tag | Src, date |
| --- | --- | --- | --- | --- |
| 635 | Current LightingStyle choices | Realistic and Soft | VERIFIED | P07/P08; undated, accessed 2026-10-21 |
| 637 | ShadowSoftness documented range and scope | 0-1; Realistic | VERIFIED | P07; undated, accessed 2026-10-21 |
| 639 | Stored source resolution is not phone residency | up to 8K source; up to 4K rendering | VERIFIED | P12/P13; 2026-01-30 / update 2026-03-23 |

## 2. Paper section 8: cohesion across crafts (AP:643-673)

### 2.1 What the art director makes agree (AP:645-651)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| CC1 | 645 | Cohesion means shared decisions, not identical techniques. The art director fixes only what must agree: proportions where assets touch, semantic colours, material impressions, event importance, recurring motifs, emotional register. Each specialist owns its own implementation and should say when it has a better way to reach the direction. | OPINION | O00 | new (J009 brief already says reviews do not duplicate craft) |
| CC2 | 647 | Review the whole event, not approved pieces. For a major ability compare pose, prop silhouette, effect, camera, UI response and sound. Ask: do they announce the same event, agree on its importance, and keep the next player decision clear? Report the mismatch (the paper's example: a harmless set-up reads like the damaging hit). Do not dictate keyframes, emitters or audio envelopes. | OPINION | O00 | new |
| CC3 | 649 | Keep a cross-craft reference for each recurring event: a clip with marked moments, an image sequence, and a short meaning description. Record which agent owns each component and which shared state or event the components stand for. A visual review gives no right to change gameplay timing or damage rules; those need the relevant design owner and, where fitting, the creative director. | OPINION | O00 | new |
| CC4 | 651 | Sound cannot be judged from screenshots: mark it "unreviewed" when no audio is given. Stills also cannot show motion quality, transitions, clutter over time or flicker. Ask for clips and gameplay context. A visual agent with limited evidence requests the right artifact and does not pretend it perceived the whole game. | OPINION | O00 | new (J009 brief: missing capture = NOT REVIEWED) |

### 2.2 TFT K.O. Coliseum (AP:653-657)

| ID | AP | Content | Tag | Src and date | Who says it | Kit |
| --- | --- | --- | --- | --- | --- | --- |
| TF1 | 655 | The paper reports the 2025 TFT retrospective as follows. K.O. Coliseum was the first full style pass over every champion in one set. New shaders and outlines had to help abilities without hurting clarity. The Top Four ceremony carried the anime-tournament theme into feedback. Some players read the look as fighting-game rather than anime, or as too old-fashioned. The team liked the theme; audience reading did not fully match intent. | EXPERIENCE | R14, 2025-10-27 | documented by the studio (Riot TFT team's own retrospective) | new |
| TF2 | 657 | Lesson for AI-made images: matching the maker's style words is not enough. Ask reviewers what genre, mood and player role the image shows, without telling them the intended label. If the answer differs, name the cues that cause it. Do not keep raising stylisation until a classifier returns the wanted keyword. | OPINION | O00 | the paper's interpretation | new |

### 2.3 Arcane and Fortiche (AP:659-665)

| ID | AP | Content | Tag | Src and date | Who says it | Kit |
| --- | --- | --- | --- | --- | --- | --- |
| AF1 | 661 | Fortiche describes Piltover's Art Deco and Zaun's Art Nouveau as a story-driven visual contrast. Mucha shaped organic linework and imagined in-world murals; his wider painting also informed atmosphere. The sentence "rather than copying a single motif everywhere" is the paper's wording and may be its reading, not the studio's (see X5). | EXPERIENCE | R16, 2023 (page shows 08/11/2023) | documented by the studio (Fortiche blog); last clause = paper's interpretation | new |
| AF2 | 663 | The studio describes its signature as deliberately handmade-looking textures and a mix of painting, technology, comics, art history and live-action staging. It names adults and young adults as its main audience. The paper warns that neither the look nor the audience should be silently equated with young mobile Roblox players. | EXPERIENCE (studio account); OPINION (warning) | R17, undated, accessed 2026-10-21; O00 | documented by the studio (Fortiche FAQ); warning = the paper's | new |
| AF3 | 665 | Transfer the link between world identity and visual grammar, not "every asset heavily textured" or "every shot cinematic". A bible can give districts related but different materials, line rhythms and lighting motives under one rendering language. Gameplay needs stable readable cues across changing cameras; a film shot can pool detail and light for one planned frame. The paper calls this an application hypothesis, not a claim that copying Arcane's surfaces gives the same direction. | OPINION | O00 | the paper's interpretation | new |

### 2.4 Paper table AP:667-673

| AP | Rule | Number | Tag | Src, date |
| --- | --- | --- | --- | --- |
| 669 | Cross-craft changes share a clarity allowance | no numerical allocation supplied | EXPERIENCE | R01/R02; 2021-03-12 / 2021-04-09 |
| 671 | Review sound and motion through appropriate evidence | stills cannot prove temporal or audio outcomes | OPINION | O00; 2026-10-21 |
| 673 | Audience interpretation can differ from intent | the TFT K.O. Coliseum report is project-specific | EXPERIENCE | R14; 2025-10-27 |

## 3. Paper section 9: consistency across many makers (AP:677-703)

### 3.1 The task packet, the register and the style lock (AP:679-685)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| CM1 | 679 | Give each maker a task packet with a visible exception path: art-bible revision; relevant anchors; what the asset must communicate; what may vary; scale and camera context; expected review evidence. | OPINION | O00 | in kit in part: brief has `refs` (take/avoid), `fixed`, `open`, `checks` (`rules/messages.md` section 1-2). New: art-bible revision, scale and camera context, expected evidence as required items. |
| CM2 | 679 | Do not send the whole reference library. Say which image controls which decision, or the agent averages incompatible references into a generic result. | OPINION | O00 | in kit in part: max 3 anchors (`art_refs.py` MAX_ANCHORS) and `refs` with "what to take" (`messages.md` section 1). Conflicts in part: with no `anchors` column entry the tool picks owner anchors by a hash of the row id (`anchors_for`), not by relevance; naming them in the manifest's `anchors` column matches the paper. |
| CM3 | 681 | Keep an anchor register with immutable approved versions. A new anchor may supersede an old one, but record why and which assets are affected. | OPINION | O00 | in kit in part: never overwrite an approved reference (SKILL section 6); only the owner approves (`approve`). New: the supersede record (reason, affected assets). Conflicts in part: the tool attaches "our newest approved generation" last by file time (`anchors_for`, `approve` touches the file), so a newer approval takes the slot with no recorded reason or affected-asset list. |
| CM4 | 681 | Keep rejected explorations out of the approved set, but keep them as research when useful. | OPINION | O00 | in kit in part: only owner-approved images enter anchors. New: a rejected-research store. |
| CM5 | 681 | When the AI model or the prompt changes, regenerate a representative comparison set before assuming the old workflow still behaves the same. The paper calls this a proposed regression procedure, not a claim that prompt text gives reproducibility. | OPINION | O00 | new. (Kit saves a `.json` of prompt and inputs per image, SKILL step 4, which a comparison set could reuse.) |
| CM6 | 683 | A style lock must be reviewable. "Premium", "stylized", "polished" and "like a famous studio" are not locks. Replace them with observable relationships and references. | OPINION | O00 | in kit: template says "exact visual rules: shapes, proportions, materials, palette..."; `prompt-patterns.md` section 1 row 14 ("concrete visual language over reactions"); I-03 (no style words in identity). |
| CM7 | 683 | Do not freeze every pixel of one anchor. A front view of a standing character cannot define all poses, lights and cameras. Lock identity and relationships; allow task-fitting variation. | OPINION | O00 | new (template has no "allowed variation" field; the J009 brief already plans one). Does not conflict with I-04, which is a purpose-built single-view model reference. |
| CM8 | 685 | A style exception needs an accountable reason: say which rules stay protected and how the exception will be recognised as intended. Without that, later agents copy the exception as the new default. Examples given: a boss breaking the normal shape language, a special-event mood, a more dramatic marketing composition. | OPINION | O00 | new |

### 3.2 Locked anchors for AI image generation (AP:687-695)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| AN1 | 689 | Use current image-model capability with its limits: OpenAI launched ChatGPT Images 2.5 and the API models GPT-Image-2.5 Flare and Sunburst; the current image guide still warns about recurring-subject consistency and exact structured composition; quality labels do not mean the same across models. Record the real generation surface and model when shown. Do not assume a ChatGPT prompt maps onto every API control. Anchor plus repeated prompt helps consistency but is not a deterministic lock. | VERIFIED (A01, A02, A17); OPINION (advice) | A01 (2026-09-08); A02 (undated, accessed 2026-10-21); A17 (undated, accessed 2026-10-21); O00 | in kit in part: prompt record saved per image; SKILL names `gpt-image-2` through Codex; the I-02 and kit-test notes agree that anchors help but drift happens ("9 of 12 matched", `prompt-patterns.md` 1b). New: record model/surface per image. Check X8: kit names `gpt-image-2`, the paper names Images 2.5 models. |
| AN2 | 691 | Keep approved anchors by purpose, not as one big collage. Six purposes (my count): shape/proportion; material/edge treatment; palette roles; lighting/mood; gameplay composition; marketing framing. Each anchor has an ID, a revision, an approval state, the attributes it is authoritative for, and its allowed variation. The approved contract is the authority, not details the generator happened to add. | OPINION | O00 | conflicts in part: the kit keeps anchors per family folder (`content/art/anchors/<family>`), files have no ID, revision, attribute list or allowed variation (only the `gen-` prefix); and the tool tells the model to take only "silhouettes, proportions and details" from anchors and not their "shading, lighting, rendering" (`build()` note), so palette, lighting or material anchors cannot work through the current tool. Needs a tool or template change (the J009 brief says keep the machine-read format). |
| AN3 | 691 | Store negative examples, each with a specific reason for rejection. Do not let a rejected output become the next reference just because it is the newest image. | OPINION | O00 | new (negative examples). The second sentence is already met: only owner-approved images become anchors. |
| AN4 | 693 | A reusable request to the image model should: (a) say the supplied approved anchors apply only to the attributes assigned below; (b) say to keep the locked shape, proportion, palette-role, material, edge and lighting rules; (c) change only the requested asset or scene content; (d) not copy accidental details from an unrelated anchor; (e) report or expose conflicting requirements rather than resolve them with generic detail; (f) produce the named reference views; (g) say the result will be checked against the same locks. The paper says this is a proposed structure, not an official guarantee, and not a tested image. | OPINION | O00 | in kit in part: tool wrapper says inputs are referred to by the prompt and anchors are "design references" (`art_refs.py` build); `prompt-patterns.md` section 3 (edit: change one thing, keep the rest). New: per-anchor attribute assignment (a), the "do not copy accidental details" clause (d), the "report conflicts" clause (e) and the "checked against the same locks" statement (g). |
| AN5 | 695 | Version the fixed style block with the bible. Keep content variables (asset identity, function, pose, camera, mood variant, requested views) outside it. When a lock changes, publish the owner-approved reason, the affected anchor revisions, the exceptions and the migration scope. Do not regenerate the project's whole identity because a newer model has a different default look. Selective edits still need comparison against the original and the approved anchors. | OPINION | O00 | in kit in part: the split of style (lock) from content (identity) is I-01 and I-03; "a changed lock is an art-bible change the owner approves" (I-01). New: revision number on the bible, the migration record, and the compare-after-selective-edit step. |

### 3.3 Paper table AP:697-703

| AP | Rule | Number | Tag | Src, date |
| --- | --- | --- | --- | --- |
| 699 | Use current image model capability with limitations | Images 2.5; consistency not guaranteed | VERIFIED | A01/A02; 2026-09-08 and live docs accessed 2026-10-21 |
| 701 | Anchor changes require explicit revision | no universal anchor count | OPINION | O00; 2026-10-21 |
| 703 | A model similarity score is not brand fidelity | no validated universal score threshold | OPINION | O00; 2026-10-21 |

## 4. Paper section 10: giving clear direction without micromanaging (AP:707-751)

### 4.1 Principles (AP:709-713, 743)

| ID | AP | Check or step | Tag | Src | Kit |
| --- | --- | --- | --- | --- | --- |
| FB1 | 709 | The unit of feedback is a discrepancy that matters for a decision. Order: intended result, evidence, consequence, a checkable acceptance condition. | OPINION | O00 | in kit in part: `messages.md` section 1 ("a feeling gets a target and an observable sign, not a method"), `checks`. New: observation/inference split as a rule. |
| FB2 | 709 | Keep observation apart from inference. "The player silhouette merges with the doorway in this capture" is an observation. "The material is too dark" is one possible diagnosis. The specialist proposes whether shape, placement, light, value, material or camera changes. | OPINION | O00 | new |
| FB3 | 711 | Prioritise by consequence and dependency. Wrong fantasy, an unreadable important state, a broken scale relation or a missing identity come before texture-noise polish. No equal-priority lists. A camera or proportion change can void detail work, so settle it first. There is no universal feedback-item count; the limit is what the specialist can act on without conflicting orders. | OPINION | O00 | new (`messages.md` has no priority or dependency field) |
| NO1 | 743 | Saying no keeps a way forward: name the incompatible requirement and the evidence that could change the decision. If two reasonable directions conflict, give the trade-off to the owner; the director's taste is not an immutable fact. Do not hide a subjective call behind an invented metric, and do not claim a source requires a choice that it only illustrates. | OPINION | O00 | in kit in part: AGENTS.md section 4 (push back, `needs-decision`), `messages.md` section 5. New: "name the evidence that would change my no". |

### 4.2 Feedback template for another agent (AP:713-739): all 12 fields

The paper marks the whole template as a proposed workflow, not a published studio form (AP:715; OPINION O00). Field count 12 is my count. The "Maps to kit" column is my mapping; the paper does not make it.

| ID | AP | Field | What the field holds | Maps to kit (`rules/messages.md`) |
| --- | --- | --- | --- | --- |
| FT01 | 717 | Asset or scene and version | The exact item and the exact capture under review. | `id`, `refs` (path). Capture version: new. |
| FT02 | 719 | Decision and status | One of four: accept; accept with a recorded exception; revise; blocked by missing evidence. | New vocabulary. Hand-back `STATUS` is done/blocked/needs-decision/failed (work status, not a review verdict). "Blocked by missing evidence" = J009 brief's NOT REVIEWED. |
| FT03 | 721 | Intended player impression or decision | What the work must communicate. | `<intent>`. |
| FT04 | 723 | Governing reference | The art-bible revision and the relevant approved anchor or lock. | `refs`, `rules`. Revision number: new (see CM1, AN5). |
| FT05 | 725 | Observation | What is visible or measurable, with crop, frame or region where possible. | New field. |
| FT06 | 727 | Consequence | Why the gap matters for fantasy, hierarchy, clarity, consistency or platform support. | `<intent>` (reasons). |
| FT07 | 729 | Priority and dependencies | What changes first, and what must not be touched yet. | New field (`messages.md` has none). |
| FT08 | 731 | Requested outcome | The result wanted, not a needless recipe for the specialist's craft. | `<intent>`, `deliver`, craft left in `open` (section 1 precision rule). |
| FT09 | 733 | Protected qualities | What already works and must survive the revision. | New field (closest: `rules`, `avoid` is the opposite). |
| FT10 | 735 | Acceptance evidence | The comparison render, clip, screenshot or measurement that would show success. | `checks`, `deliver`. |
| FT11 | 737 | Specialist response | Invite a better implementation, or the specialist explains the trade-off if the request clashes with another constraint. | Hand-back `decisions_made`, `proposals`, `questions`. |
| FT12 | 739 | Escalation | Any owner or design decision needed before work continues. | `needs-decision`, `rules/company.md` decision digest, owner gates. |

### 4.3 Worked example in the paper (AP:741)

An authored, fictional example (the paper says it is not an observed defect; OPINION O00). In words of my own: a workshop game's interaction state shows a selected lever and background pipes with the same glow shape and local value, so the action target is unclear. Direction given: keep the warm repaired-workshop mood and the lever's silhouette; ask the specialist to propose a selection treatment or surrounding emphasis that sets the lever apart without brightening all machinery; return the same camera capture with selection on and off plus a lower-quality-device capture; leave interaction range and timing alone. What it shows about the form: it names a protected mood and shape (FT09), asks for a proposal rather than a fix (FT08, FT11), names the evidence pair (FT10) and lists what must not change (FT07).

### 4.4 Paper table AP:745-751

| AP | Rule | Number | Tag | Src, date |
| --- | --- | --- | --- | --- |
| 747 | Historical splash work includes paintovers and direction | 75-100 hours; average four-week schedule | EXPERIENCE | R10; 2018-07-26 |
| 749 | Feedback specifies outcome and evidence | no universal feedback-item count | OPINION | O00; 2026-10-21 |
| 751 | Owner resolves creative tradeoffs | decision authority retained | OPINION | O00; 2026-10-21 |

Scope of the 75-100 hours number (from AP:381, outside my range): a 2018 account of one kind of work (splash art), the schedule "including other duties", and the paper calls the schedule and staffing context historical and not an AI-agent completion-time estimate.

## 5. Kit comparison summary (anchor and consistency lessons)

| Class | Lessons |
| --- | --- |
| Already in the kit | CM6 (observable locks), parts of CM1/CM2 (brief `refs` with take/avoid; 3-anchor cap), CM3 first half (approved refs are never overwritten), CM4 second half (only owner-approved become anchors), AN5 split of style from content, FB1 target plus observable sign, NO1 push back / `needs-decision` |
| New | CM5 regression set on model change, CM7 allowed variation, CM8 style exceptions with protected rules, AN3 negative examples with reasons, AN4 clauses (a)(d)(e)(g), FB2 observation vs inference, FB3 priority and dependency, FT05/FT07/FT09 fields, LM/QT/MS lighting and material lessons, CC cohesion lessons, TF2 blind-reading test |
| Conflicts with the kit | AN2 (anchors by purpose with ID/revision/attributes vs per-family folders, silhouette-and-proportion-only wrapper note). CM2 (default anchor pick by row-id hash vs relevance). CM3 (newest approved generation takes the last anchor slot without a recorded reason). No conflict with the kit's 3-anchor cap as a tool limit: the paper says only that there is no universal anchor count (AP:701), so do not present 3 as a research number. |

## 6. Studio claims register (who says it)

| ID | AP | Claim | Src, date | Class |
| --- | --- | --- | --- | --- |
| SC1 | 655 | TFT K.O. Coliseum details (section 2.2 TF1) | R14, 2025-10-27 | documented by the studio (Riot TFT team retrospective) |
| SC2 | 661 | Piltover Art Deco / Zaun Art Nouveau; Mucha's role | R16, 2023 (shows 08/11/2023) | documented by the studio (Fortiche blog) |
| SC3 | 663 | Handmade-looking textures; mixed influences; adult/young-adult audience | R17, undated, accessed 2026-10-21 | documented by the studio (Fortiche FAQ) |
| SC4 | 669 | Clarity allowance: no number given | R01 2021-03-12; R02 2021-04-09 | documented by the studio (Riot dev articles); the "no number" part is the paper's report. R01 says: "the amount of attention an ability grabs should match its level of importance." |
| SC5 | 747, 381 | 75-100 hours for a splash; four-week average | R10, 2018-07-26 | artist/developer account of its own work (Riot, 2018) |
| SC6 | 657, 665, 663 (last sentence) | Lessons drawn from SC1-SC3 for AI prompts and Roblox | O00 | the paper's interpretation, not a studio statement |

## 7. Number register

| ID | Value | Unit / scope | AP | Src, date | Tag |
| --- | --- | --- | --- | --- | --- |
| N01 | 2 | LightingStyle values: Realistic, Soft | 615, 635 | P07, undated, accessed 2026-10-21 | VERIFIED |
| N02 | 0-1 | ShadowSoftness range; documented as valid with Realistic | 615, 637 | P07, same | VERIFIED |
| N03 | 4K | texture rendering ceiling through texture streaming, when the client has resources and the view justifies it | 627, 639 | P12, 2026-01-30 | VERIFIED |
| N04 | 8K | stored source image resolution, not runtime display | 627, 639 | P13, 2025-12-12 / 2026-03-23 | VERIFIED |
| N05 | below 3.5 GB | low-end Android memory class with 4K disabled, at the 2026-03-23 rollout snapshot only | 627 | P13, update 2026-03-23 | VERIFIED |
| N06 | 1 | colour channel (red) of an RGB emissive mask that sets glow intensity | 623 | P21, 2026-02-12 | VERIFIED |
| N07 | pixels | unit of `Bloom.Size` radius | 619 | P11, undated, accessed 2026-10-21 | VERIFIED |
| N08 | 2025-01-21 / 2025-07-23 | Unified Lighting: original post / full release | 613 | P09 | VERIFIED |
| N09 | 2025-10-30 / 2025-12-09 / 2026-02-25 / 2026-05-12 / 2026-10-09 | SLIM: client beta / platform update / status update / R15 avatars / debug tints | 629, 631 | P14, P15, P16 | VERIFIED |
| N10 | 75-100 h; 4 weeks | splash art, 2018, including paintovers and direction, schedule includes other duties; historical | 747 (scope 381) | R10, 2018-07-26 | EXPERIENCE |
| N11 | not supplied | numerical split of a clarity allowance between crafts | 669 | R01/R02, 2021 | EXPERIENCE |
| N12 | not established | universal anchor count | 701 | O00 | OPINION |
| N13 | not established | validated score threshold for model similarity / brand fidelity | 703 | O00 | OPINION |
| N14 | not established | universal feedback-item count | 711, 749 | O00 | OPINION |
| N15 | 12 / 9 / 6 / 3 | feedback-template fields / lighting-contract fields / anchor purposes / lighting review variants (neutral, approved gameplay, problem). My counts, not paper numbers. | 607, 617, 691, 713-739 | O00 | n/a |

## 8. Source ids used in lines 603-754 (resolved from AP:1013-1695)

Quotes are the paper's key quotations, each under 15 words. A quote is a locating excerpt, not the source's full scope (AP:1015).

| ID | Source | Date and limits | Quote | AP register line |
| --- | --- | --- | --- | --- |
| O00 | This paper's own recommendations, authored examples, workflow | 2026-10-21; not an external study | - | 1015 |
| R01 | Riot, "Clarity in League" | 2021-03-12; EXPERIENCE | "the amount of attention an ability grabs should match its level of importance." | 1105 |
| R02 | Riot, "Ask Riot: Let's Talk Clarity" | 2021-04-09; EXPERIENCE | "we had to pull back in other places." | 1113 |
| R10 | Riot Nexus, "New Champions" | 2018-07-26; EXPERIENCE | "Most splash artists are also responsible for art-directing outsource artists" | 1177 |
| R14 | Riot TFT, "K.O. Coliseum Learnings" | 2025-10-27; EXPERIENCE; project-specific | "This was our first-ever full style pass across every champion in a set." | 1209 |
| R16 | Fortiche blog, "Arcane in Paris" | 2023, page shows 08/11/2023; EXPERIENCE | "Piltover draws heavily on Art Deco, while Zaun is rooted in Art Nouveau." | 1225 |
| R17 | Fortiche FAQ | undated living page, accessed 2026-10-21; EXPERIENCE | "digital precision is swapped for organic, hand-crafted textures" | 1233 |
| A01 | OpenAI, "Introducing ChatGPT Images 2.5" | 2026-09-08; VERIFIED | "we're introducing two new models in the API" | 1377 |
| A02 | OpenAI, image generation guide | undated, accessed 2026-10-21; VERIFIED | "the model may occasionally struggle to maintain visual consistency" | 1385 |
| A17 | OpenAI, image prompting guide | undated, accessed 2026-10-21; VERIFIED | (quote is 16 words; paraphrase: the same quality label does not give the same quality or speed on different models) | 1505 |
| P07 | Roblox Creator Hub, Global lighting | undated, accessed 2026-10-21 | "LightingStyle indicates the artistic intent behind lighting in the game" | 1561 |
| P08 | Roblox Creator Hub, Lighting class | undated, accessed 2026-10-21 | "The actual shadowing path also depends on PrioritizeLightingQuality" | 1569 |
| P09 | Roblox DevForum, Unified Lighting is fully live | 2025-01-21; full release 2025-07-23 | "Unified Lighting has been fully released and is now live in all experiences!" | 1577 |
| P10 | Roblox Creator Hub, Post-processing effects | undated, accessed 2026-10-21 | "they only display to a specific player" | 1585 |
| P11 | Roblox Creator Hub, BloomEffect | undated, accessed 2026-10-21 | "Determines the radius of the bloom in pixels." | 1593 |
| P12 | Roblox DevForum, 4K texture rendering | 2026-01-30 | "We've enabled 4k texture rendering via the Texture Streaming system." | 1601 |
| P13 | Roblox DevForum, Introducing Texture Streaming | 2025-12-12; rollout update 2026-03-23; accessed 2026-10-21 | "We store your original image at up to 8k resolution" | 1609 |
| P14 | Roblox DevForum, Client Beta: SLIM | 2025-10-30; updates 2025-12-09, 2026-02-25 | "SLIM is now supported on all platforms in Client Beta." | 1617 |
| P15 | Roblox DevForum, platform avatars in SLIM | 2026-05-12 | "SLIM now supports R15 platform avatars" | 1625 |
| P16 | Roblox DevForum, SLIM debug tints | 2026-10-09 | "SLIM now has debug tints" | 1633 |
| P21 | Roblox DevForum, Emissive Masks live | 2026-02-12 | "only the Red channel will be used to determine the glow intensity." | 1673 |
| P22 | Roblox Creator Hub, PBR textures (SurfaceAppearance) | undated, accessed 2026-10-21 | "Tinting does not affect performance" | 1681 |

## 9. Claims for the fact-check

Kinds: roblox = check against the Roblox docs and the local mirror; image-ai = OpenAI pages; studio = Riot/Fortiche pages. "Why it matters" says what the art director would do wrong if the claim is false.

| ID | Claim | AP | Src | Date | Why it matters |
| --- | --- | --- | --- | --- | --- |
| C01 | Unified Lighting is fully live; old Future maps to Realistic + PrioritizeLightingQuality on (RB1) | 613 | P09 | 2025-01-21; 2025-07-23 | The bible would name wrong or missing lighting properties. |
| C02 | `Lighting.Technology` is deprecated (RB2) | 613 | P08 | undated, 2026-10-21 | Agents may be told to set a dead property. |
| C03 | LightingStyle has exactly Realistic and Soft (RB3) | 615, 635 | P07 | undated, 2026-10-21 | The lighting contract and style choice rest on this list. |
| C04 | PrioritizeLightingQuality true favours nearby lighting, false favours distance (RB4) | 615 | P07 | undated, 2026-10-21 | Baseline captures (QT4) depend on the right setting direction. |
| C05 | ShadowSoftness range 0-1, valid with Realistic only (RB5) | 615, 637 | P07 | undated, 2026-10-21 | Soft style might ignore or reject the property; locks could name a dead control. |
| C06 | Soft with PrioritizeLightingQuality on uses shadow maps, not voxel lighting (RB6) | 615 | P08 | undated, 2026-10-21 | Decides how shadow-dependent cues (QT5) behave at distance. |
| C07 | Post-effect list; Lighting effects global, Camera effects per player; some absent at lower Studio quality (RB7) | 619 | P10 | undated, 2026-10-21 | Danger cues must not rely on effects missing at lower quality (QT7). |
| C08 | ColorGradingEffect has Default and Retro tonemappers; Retro imitates pre-2019 look (RB8) | 619 | P10 | undated, 2026-10-21 | Colour review would record wrong tonemapper options. Sentence-to-source mapping is not line-exact. |
| C09 | `Bloom.Size` is a pixel radius; bloom can differ with quality settings (RB9) | 619 | P11 | undated, 2026-10-21 | Bloom-based importance cues (QT7). The quality-variance half may come from another page. |
| C10 | Emissive Masks live on SurfaceAppearance, MaterialVariant, TerrainDetail; red channel only; glow is not a dynamic light (RB10) | 623 | P21 | 2026-02-12 | The "glows vs lights the room" rule (MS1) rests on it. |
| C11 | SurfaceAppearance tinting does not affect performance (RB11) | 625 | P22 | undated, 2026-10-21 | Decides how freely tints may be used in locks. |
| C12 | 4K texture rendering via streaming when resources and view allow (RB12) | 627, 639 | P12 | 2026-01-30 | Phone texture-detail expectations. |
| C13 | 8K storage; 4K off for low-end Android below 3.5 GB; unsupported classes (UI/SurfaceGUI, Terrain/TerrainDetail, sky, bundled materials) (RB13) | 627 | P13 | 2025-12-12; 2026-03-23 | The paper itself says this list is a snapshot; may have changed by 2026-10-21. |
| C14 | SLIM gives composite stand-ins for streamed-out models in streaming-enabled places; Client Beta, all platforms (RB14) | 629 | P14 | 2025-10-30 to 2026-02-25 | Beta status at paper date is unknown; landmark and group readability checks (MS4) assume it. |
| C15 | SLIM supports R15 platform avatars, not generically NPCs or later modifications (RB15) | 629 | P15 | 2026-05-12 | Decides which characters need a full-vs-lightweight comparison. |
| C16 | SLIM debug tints exist; access via Developer Console (Edit permission) and Studio beta + Visualization Modes (RB16) | 631 | P16 | 2026-10-09 | Review capture method (MS5). Newest source, after the model's knowledge. |
| C17 | TFT K.O. Coliseum: first full style pass over every champion in a set; shader/outline goals; Top Four ceremony; some players read it as fighting-game or old-fashioned (SC1) | 655 | R14 | 2025-10-27 | Basis for the blind-reading test (TF2). Check each detail against the page. |
| C18 | Fortiche: Art Deco vs Art Nouveau; Mucha informed linework, murals and atmosphere (SC2). Check whether "not copying a single motif everywhere" is in the source. | 661 | R16 | 2023 | A paper inference must not be quoted as a studio rule. |
| C19 | Fortiche signature (handmade textures; mixed influences) and adult/young-adult audience (SC3) | 663 | R17 | undated, 2026-10-21 | The audience limit is why the look is not copied directly for young Roblox players. |
| C20 | OpenAI launched ChatGPT Images 2.5 plus API models GPT-Image-2.5 Flare and Sunburst | 689 | A01 | 2026-09-08 | Newer than the kit's `gpt-image-2` text; which model Codex really calls decides the record in AN1. |
| C21 | Image guide warns about recurring-subject consistency and exact structured composition | 689 | A02 | undated, 2026-10-21 | The register quote covers consistency only; the "structured composition" half needs the page. |
| C22 | Quality labels are not equivalent across models | 689 | A17 | undated, 2026-10-21 | Prompts that say "high quality" will not transfer between models. |
| C23 | R01/R02 give no numerical allocation of clarity between crafts | 669 | R01, R02 | 2021-03-12; 2021-04-09 | Confirms the skill must not invent a split. |
| C24 | 75-100 hours per splash; average four weeks incl. other duties (SC5) | 747, 381 | R10 | 2018-07-26 | Must never be used as an agent time estimate. |

## 10. Contradictions and limits

| ID | AP | Item | Handling for the skill writer |
| --- | --- | --- | --- |
| X1 | 17 | The paper ran no image benchmark, Roblox scene, player study or screenshot measurement. All procedures here (QT3-QT7, CM5, AN4, FB template) are proposals. | Label every check "proposed, not tested". Results come from this studio's own runs. |
| X2 | 615, 617 | Numbers in a lighting contract and in quality-tier captures are "project choices until approved". The paper gives no brightness, contrast or shadow values. | Leave all values as owner decisions; never state a threshold. |
| X3 | 701, 703, 711, 749, 669 | The paper explicitly has no universal anchor count, no model-similarity threshold, no feedback-item count, no clarity-allowance split. | Never present 3 anchors (a tool cap), 12 template fields (the paper's list) or any score as research-backed numbers. A similarity score is not brand fidelity. |
| X4 | 627, 629 | Roblox support lists are dated snapshots (P13 update 2026-03-23, P14 Client Beta, P15 2026-05-12). The paper says not to treat them as permanent. | Re-check against the docs mirror at use time; say "as of <date>" in the skill. |
| X5 | 661 | In AF1 the clause about not copying one motif everywhere may be the paper's interpretation placed inside an EXPERIENCE paragraph. | Cite only "Fortiche describes Art Deco / Art Nouveau contrast and Mucha's influence" as the studio's claim. |
| X6 | 663, 665 | The paper warns that Arcane's look and audience (adults, young adults) do not equal young mobile Roblox players, and calls the transfer an application hypothesis. | Do not use Arcane as a style target for a Roblox game without the owner's choice; treat as a reference of relationships. |
| X7 | 655, 673 | The TFT audience mismatch is project-specific (the paper says so in its table). | Use as a failure mode and test idea (TF2), not as a population finding. |
| X8 | 689 | The paper names Images 2.5 and API models Flare/Sunburst (A01, 2026-09-08). The kit says `gpt-image-2` via Codex (SKILL section 4; `prompt-patterns.md` header). The paper says to record the actual surface and model "when exposed". | Do not assume the two are the same. Add a model/surface field to the image record; check what Codex exposes. |
| X9 | 691, 693 | Kit tool and paper differ on anchor purpose and selection (see section 5, AN2/CM2/CM3). | Needs an owner or lead decision (tool change vs template change). Not for the skill writer to settle alone. |
| X10 | 683, 693 | Tension inside the paper: "do not freeze every pixel of an anchor" (CM7) against "preserve the locked shape, proportion... rules" in the request (AN4). It resolves only by locking relationships and naming what may vary; no threshold for how much. | State the allowed-variation list per lock; do not invent a tolerance. |
| X11 | 651, 647 | A stills-only reviewer cannot judge sound, motion, flicker or timing. Cohesion review of an event is therefore partly "not reviewed" until clips and audio arrive. | Hand-back marks audio and motion NOT REVIEWED without clips (matches the J009 brief). |
| X12 | 649 | Visual review does not authorise changes to gameplay timing or damage rules. | Route to the design owner and the creative director; the art director cannot approve. |
| X13 | 741 | The feedback example is fictional (the paper says so). | Use only as a format sample, never as precedent or as an observed defect. |
| X14 | 633-639, 613-631 | The paper's Roblox sentences are tagged to one or two sources per paragraph, not per sentence (for example RB8, RB9). | Fact-check each sentence against the page, not the paragraph. |
| X15 | 381, 747 | R10's hours and weeks are a 2018 account, historical, with other duties included. | Never reuse as an AI-agent schedule or cost figure. |
| X16 | 689 | The image guide quote in the register supports "consistency may fail" (A02). The "exact structured composition" warning in the body has no quote. | Fact-check C21 before relying on the second half. |
| X17 | 631 | SLIM debug tints are diagnostic overlays, not palette. | Keep an untinted capture for any colour decision. |

## 11. Coverage map

| Paper item | Where |
| --- | --- |
| Section 7 intro (AP:605-609) | 1.1 LM1-LM3 |
| Quality tiers (AP:611-619) | 1.2 QT1-QT7; RB1-RB9 |
| Materials and streaming (AP:621-631) | 1.3 MS1-MS5; RB10-RB16 |
| Section 7 table (AP:633-639) | 1.5 |
| Section 8 principles (AP:645-651) | 2.1 CC1-CC4 |
| TFT K.O. Coliseum (AP:653-657) | 2.2 TF1-TF2; SC1; C17 |
| Arcane and Fortiche (AP:659-665) | 2.3 AF1-AF3; SC2, SC3; C18, C19 |
| Section 8 table (AP:667-673) | 2.4 |
| Section 9 general (AP:679-685) | 3.1 CM1-CM8 |
| Locked anchors (AP:687-695) | 3.2 AN1-AN5 |
| Section 9 table (AP:697-703) | 3.3 |
| Section 10 principles and saying no (AP:709-713, 743) | 4.1 FB1-FB3, NO1 |
| Feedback template, 12 fields (AP:713-739) | 4.2 FT01-FT12 |
| Worked example (AP:741) | 4.3 |
| Section 10 table (AP:745-751) | 4.4 |
| Kit comparison | sections 3-4 Kit columns; section 5 |
| Numbers, claims, contradictions | sections 7, 9, 10 |
