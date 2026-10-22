---
name: art-direction
description: What and why of one visual direction for a Roblox game - fantasy in pictures, read order and value bands, shape language, colour roles and reserved colours, light, identity across variants. Use when the look is set or changed, for "it doesn't look like one game", "it looks generic / like AI", "the screen is busy", "I can't see the attack", "make it look great". Art director reads first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J009 from the owner's art-director research paper (2026-10-21, fact-checked), the owner-supplied Riot "So You Wanna Make Games??" transcripts (via the first game's art-fundamentals skill) and the first game's art history. Evidence ids point to `knowledge/reference/art-direction/` notes: `01:` precedents, `02:` direction/bible/readability, `03:` light/cohesion/anchors/feedback, `04:` platform/evolution/marketing/process, `05:` first game, `FC-S`/`FC-A` fact-checks. Rebuilt by J018 maker art-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the stages in §3 (research board, rough options, grey and silhouette pass, cheap proof in the engine), practices C-19 to C-25, the core principles (§7); repair round 1: the owner sheet shows only options that passed the grey pass; repair round 2: one image cap per round including regenerations, environment measures on the environment-only capture, the anchor count in one place.

# Art direction: one world, read at a glance

## 1. When this skill starts
It answers four questions, in this order, for any game or feature:
1. **What must the player feel and decide?** The fantasy, the repeated decisions, the camera, the devices (from the game designer).
2. **What is the world's grammar?** The few relationships every craft must show (shape, value, color roles, material, light, motion, sound) and what may vary.
3. **What reads first, right now?** The hierarchy for each moment, from the player's current decision.
4. **Does the combined frame still work?** On a phone, at the real camera, in the busiest supported scene, at the lowest supported quality.

**Game art has three jobs, in this order:** clarity (the player reads the game state at a glance: where to go, friend or enemy, what is dangerous, what just happened), satisfaction (every action is answered), style (one look that sets the emotion). A beautiful piece that weakens the read has failed.

**A direction is done only when** the read-first items win at the game camera on a phone in the busiest scene at the lowest quality; every craft's piece placed next to 2-3 approved anchors reads as the same game; and the owner approved the locks and anchors (J009-D3). The art director owns the answers as **proposals**. How to write the bible, run the checks and brief specialists: `art-review`.

After a compaction, re-read §5-§7 of this file (rules, self-check, core principles) and `art-review` §6 before you continue.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The standards: reads by task, hierarchy and value bands, shape, colour roles, light, cohesion, materials and detail, composition in the real frame, places | `references/clarity-cohesion.md` |
| Characters, props and places with a personality; identity anchors, likeness, variants, skins, tiers, cosmetics, themes and updates | `references/identity-variants.md` |
| Three worked examples in our pipeline (a new direction, a busy hub, a variant) | `references/worked-examples.md` |
| Phones and Roblox rendering, evolving a style, marketing art, the don'ts | `references/platform-evolution-marketing.md` |
| The owner's reference studios and 10 other studio cases (J009-D2): what to learn, what not to copy (the only place studio and game names are used) | `references/precedents.md` |
| How to explore directions, write the art bible, measure, run the self-review and the review checklist, brief the crafts | `art-review` skill |
| Reference images, locks format, anchors tool | `reference-images` skill |
| The craft owners' own rules | `ui-design`, `vfx-design`, `sound-design`, `rig-pipeline`, `modeling-design`, `animation-design`, `environment-design`, `level-design` |
| The source notes and fact-checks | `knowledge/reference/art-direction/` |

## 3. Steps
Each step has a check; the next starts only when it passes. Steps 4-6 are the direction stages: no style is locked before rough options were compared in grey and black-fill.
1. **Restate the moment and the problem.** What the player does, the 1-2 things they must notice first, the feeling, the target experience, camera, device (phone first), the constraints that decide what can be built (mechanics and numbers, budget, quality floor, rig), and the success test. Missing input that would change the direction: ask the game designer; never fill it with another game's convention (04:PS01, 05:AD03). *Check:* the brief lines exist before the first image.
2. **Know the subject.** Name the world rule (one causal premise every craft can derive its choices from; a pretty place with unrelated icons and generic effects fails, 01:DL-13). Write the character card, or a prop's or place's personality in 3-5 words, and the sell list (2-4 things the image must sell); set the style levers on purpose: saturation, proportion push, realism of props and places, value structure (`references/identity-variants.md` §1-2). Turn each pillar into observable visual relationships (masses, states, what looks causal), never a particle count or polygon budget; specialists propose the implementation (02:D3-D4). *Check:* every later choice can be traced to a line of these.
3. **Research board.** Our own anchors and approved images first, then real-world reference per aspect (material, pose, place, phenomenon), one source from outside games, and a keyword table (keyword → colour key, setting, pose, prop). One narrow direction per board with 3-5 pillar words, a one-line sensitivity note, the 3-5 key features that make each subject read (`art-review/references/exploration.md` §7). *Check:* both halves present, each entry says what it is for; no single reference is copied.
4. **Rough options (the thumbnail pass).** Write 6-12 one-line hooks, each from a different source or style family; the first idea you had is labelled warm-up and set aside; keep 3-4 that differ in proportion, material, density, light, camera reading or emotion, one of them radical. Generate them rough, at equal low finish, same subjects and same game camera. Image budget (PROPOSAL; a brief's cap wins): hooks are text; at most 9 images per round including regenerations (max 2 per image), one per chat; you look at one colour-and-grey contact sheet per round plus any image whose numbers fail (`art-review/references/exploration.md` §3, §8). *Check:* the black-fills differ, not only the colours (`art-review/references/self-review.md` DR3).
5. **Grey and silhouette pass.** Judge every option first in grey and black-fill at phone size: the read-first item holds the strongest value contrast, the subject is named from its fill, the layers keep their bands; colour is judged only on options that pass (DR4). *Check:* `look_check.py value` and `thumb` JSON paths per option.
6. **Owner pick.** One labelled sheet of the 2-3 options that passed step 5 (the recipe's G1 count) at equal finish; the failing options listed under it with their numbers, never shown as equals; a goal question ("which reads as most dangerous at phone size?"), one recommendation with reasons tied to the brief, a rejection reason per option, appeal and risks (what Roblox may not render cheaply). Record the owner's words as a decision; a direction is logged as closed only after the owner's words, and not proposed again without new ones (02:D5-D12). *Check:* DR5.
7. **Lock little, lock well.** Write the bible revision (`art-review/references/art-bible.md`): locks as relationships with purpose, scope, example, failure example, test and allowed variation, plus the standards the crafts measure against: screen order and value bands per layer, reserved colours and colour roles, shape vocabulary, key light direction per place, palette roles, the motion line, the UI thematic, identity anchors. Everything is PROPOSAL until the owner's decision id is recorded (01:EC4, 02:RD3, 02:BF4). *Check:* every lock has a runnable test (BB1-BB2).
8. **Set the hierarchy per moment.** Rank what must be noticed now, read next, and left as atmosphere; give each craft its screen job (C-05) and its contrast budget (C-19); place rest areas next to the detail spots. *Check:* the hierarchy table names 1-2 read-first items per moment.
9. **Prove it cheaply in the engine.** Before anyone polishes, ask for representative tests at the game camera next to a player-size avatar: a blockout or proxy of the hero subject, one key place in greybox with 2-3 lighting variants, one shared event (modeler, environment designer, animator, VFX, UI) (04:PS06). Gates freeze decisions: after the direction gate, proportions, layout and light direction move only with a new decision. *Check:* captures of the tests pass the self-review read lines before any polish is asked (DR11).
10. **Review in context, then in combination, big to small.** Gameplay camera, busiest scene, phone size, lowest quality, effects and UI on; in a fixed order: gameplay read, composition and balance, silhouette, value, light and colour, material and detail, finish (`art-review` §3). Motion and sound by their own evidence or NOT REVIEWED. *Check:* the review file follows the order.
11. **Direct by outcome.** One named problem at a time, worst first; a paint-over on the capture when words are not enough; what must survive; acceptance evidence; the specialist picks the craft (`art-review` §3 step 8).
12. **Keep the direction alive.** Versioned bible, anchors and exceptions; drift checks at every review; owner-approved changes with a transition plan (`references/platform-evolution-marketing.md` §2).

## 4. Craft core (what separates great art direction from weak)
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | **Coherent decisions, not attractive assets.** Good art can be wrong for this game: a beautiful effect hides a threat, an impressive place flattens the character read, a polished thumbnail promises a game that does not exist. Judge each piece by what it adds to or takes from play and what it costs to build | 01:EC1-EC2; owner: "the models look fine, but they don't look like they exist in the same world" (05:OR16) |
| C-02 | **Three jobs, in order:** clarity, satisfaction, style (§1). Style is a tool for emotion, not decoration | 05:AF01 |
| C-03 | **A world grammar, not a rendering recipe.** Shared construction rules plus a contrast in how each faction or district relates to them; signature objects and motifs organise the action vocabulary (names, icons, animation accents, roles), not only decoration | 01:DL-05 to DL-19 |
| C-04 | **Attention matches importance.** Rank effects, cues and celebrations by consequence (damage, control, dodgeability, what it changes) and give size, brightness, duration and loudness by rank; only the top tier may fill the screen. A telegraph that promises a dodge the mechanic does not give miscommunicates | 01:LL-04, LL-05 (FC-S) |
| C-05 | **Screen ownership.** Default order: UI and gameplay VFX first, characters second, the environment always the backdrop. Level = navigable structure and calm regions; character = identity; VFX = event information; UI = persistent state and controls; animation = action and intent. Negotiate per game; it is not a fixed law | 02:HI2; 01:LL-10, LL-12 |
| C-06 | **One clarity budget per thing.** A costume, skin or variant shares one budget of change across model, motion, VFX and sound; parity is two-sided (never less, never more readable than the base); name the cues spent and the cues that stay | 01:LL-06, LL-08 (FC-S) |
| C-07 | **Identity contract per character or tool:** the silhouette feature that must survive, the facing cue, the source of power as the primary read, the identity anchors pushed when small (count: `art-review/references/art-bible.md` §7; `references/identity-variants.md` §3) | 01:LL-02; 05:AF11-AF12; 01:TF-01 |
| C-08 | **Lower everything else** to make one thing stand out (§7 P3) | 05:AF03, AF09 |
| C-09 | **Detail is a contrast channel.** Clump detail in a few spots, leave rest areas; indicate masses with a few strong marks; spend complexity where it changes recognition or emotion, at the size players see it (§7 P6) | 05:AF05; 04:SP1; 01:DO-01 |
| C-10 | **Value first, colour by role.** Check hierarchy with hue removed; write colour as roles, one meaning per treatment, a non-colour backup for every essential state; no universal palette size (C-19, C-20) | 02:SH2-SH3, M4; Xbox guideline 103 (FC-A) |
| C-11 | **Shape meaning is learned per game.** Sharp = danger, round = friendly, square = stable is a starting hypothesis; fix this game's vocabulary down to the small shapes (trims, particle shapes, UI corners) and test it with its audience | 02:SH1; 05:AF08 |
| C-12 | **Light keeps the information.** A lighting direction states the impression it must give and the information that must survive it (route, character, interaction, danger) on the supported quality settings; never let bloom or a thin shadow carry importance alone | 03:LM1-LM3, QT5, QT7; 03:RB1-RB9 (FC-A) |
| C-13 | **Review the event, not the pieces.** Pose, prop silhouette, effect, camera, UI response and sound announce the same event, agree on its importance and keep the next decision clear. You see stills: judge frame strips at a known rate; feel at normal speed is the owner's call on a playable preview; missing clip or audio = NOT REVIEWED | 03:CC2, CC4; 01:LL-06 |
| C-14 | **Design for the real camera.** Composition, proportion and even geometry may bend for what the player sees; identity goes on the sides the camera shows (back, shoulders, head, top for third-person and top-down); test every reachable viewpoint | 01:SC-MW; 01:TS-LU-L |
| C-15 | **Phones are the target, not a shrunk desktop.** Protect identity silhouettes, semantic cues and key value relationships first; microdetail goes first. No universal phone triangle budget, light count or palette size | 04:SP2, PF3; 04:AU1 (FC-A) |
| C-16 | **Match how the owner judges.** Look and finish at a pro bar (kit screens graded C- and B-, J009-D6); a correct, readable screen can still be a C. Show options of the same subject at one camera; what the owner already likes is locked; test changes side by side | 05:OR03, OR20; 05:AB10 |
| C-17 | **Art and rules agree.** Soft-looking things do not stop a truck; weak-looking materials break; a doorway that looks open is walkable; a hazard shows where it comes from | 05:AF19 |
| C-18 | **Copy relationships, never a franchise.** Name the relationship to transfer and keep source characters, logos, UI and silhouettes out | 01:CO-3; 05:OR32; `platform-policy` |
| C-19 | **Value bands per screen layer.** The environment sits in the narrowest band, never pure black or white; characters a little wider; VFX and UI own the extremes. The bible states each band in grey-view value with its luminance equivalent (starting values: `art-review/references/art-bible.md` §7) and every craft measures against it | J018 |
| C-20 | **Reserved gameplay colours.** The hues that mean danger, enemy, team, interactable or route stay out of decoration and set dressing (share near zero), fast motion stays out of sightlines, and every reserved hue has a shape, outline or icon partner | J018; J009 colour roles |
| C-21 | **One key light per place, chosen on the rough.** Light motivated by the setting, direction fixed per place (Lighting.ClockTime, GeographicLatitude; Lighting is global, so one sun per Roblox place: `references/clarity-cohesion.md` §4) before detail; the brightest area is the focus; no key position in deep shadow; nothing important rides on a shadow phones drop | J018; 03:LM1-LM3 |
| C-22 | **The same gates for every visual job:** rough → grey and black-fill → light → colour → material and detail → effects and polish. No detail rescues a failed big read; work in passes over the whole piece, never one part finished while the rest is blank | J018 |
| C-23 | **One likeness everywhere.** A character keeps its face, posture and anchors in model, icon, portrait, cutscene and key art; image models drift between generations, so the anchor images ride along with every prompt and every new image is checked against them | J018 |
| C-24 | **Finish is planes, edges and controlled imperfection, not more detail.** Crisp key edges balanced with soft ones, hue-shifted shading, wear where hands go; a flat fill, an even gradient or a perfectly repeated piece reads machine-made ("AI-looking") | J018; J002-D9; 05:OR21 |
| C-25 | **Compose in the real frame.** The crop players meet most (the game camera with HUD and safe areas, the 150x150 icon, the shop card, the thumbnail tile) is designed first, at final scale, with its overlay | J018; FR28-FR29 (FC-A) |

## 5. Rules (final check, short)
- The owner decides every lock, anchor, direction and exception. The art director proposes, compares and records; it never changes the creative brief silently.
- No universal thresholds: palette size, DeltaE, silhouette pixels, value bands, reserved-hue shares, exploration and review counts are project choices the owner approves or the project measures. Starting values in these books are PROPOSAL; the bible's value or the owner's wins. Only scoped standards (WCAG / Xbox) apply to UI text and UI components, with the standard named.
- A measurement is evidence, not taste. Missing capture, clip or audio = NOT REVIEWED, never a pass. Light checks: numbers for every case, images only for a failing number plus a few key cases; every image-making stage states its budget (J005-D8).
- No detail, polish or effects pass is asked for or approved before the big read (rough, grey, black-fill) passed at the game camera.
- Studio precedents: say who said it (studio-published, developer account, the paper's reading); studio names appear only in `references/precedents.md`.
- The art director reviews and directs; it never edits another craft's files or final assets.
- Franchise characters, logos, lettering and real brands stay out of every image and asset; sensitive themes and real cultures get a `platform-policy` check.

## 6. Self-check before returning
- [ ] The moment, the problem, the read-first items, the constraints and the success test are stated before any judgment or image.
- [ ] Direction work: research board, hooks with the warm-up labelled, 3-4 distinct rough options with one radical, grey and silhouette pass, the 2-3 that passed on the owner sheet with one recommendation and reasons; image budget reported; cheap proof before polish (`art-review/references/self-review.md` DR1-DR11).
- [ ] Every lock or direction proposed has purpose, scope, example, failure example, test and allowed variation; the bible carries the standards the crafts measure (BB1-BB4).
- [ ] Hierarchy is ranked for the moment; each craft's screen job and contrast budget is named.
- [ ] Combined frame, phone size, lowest quality and busiest scene were reviewed or marked NOT REVIEWED; every check names its input.
- [ ] Each precedent cited carries its provenance; no studio rule was invented.
- [ ] Owner approvals cited by decision id with the owner's words; nothing is called approved without one.

Project overlay: if `knowledge/overlays/art-direction.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's shared principles, stated for the art director's own work. Each has an example from our games and a check you run; line ids are in `art-review/references/self-review.md`. Numbers follow the studio's master list; 8 and 19 are not yours: timing (tell, build, beat, hit, result) and feedback that follows the confirmed outcome belong to the motion, effect, sound, UI and design owners; you check only that their pieces agree on one event (self-review EVT1).

**P1 The gameplay read comes first; beauty never costs it.** Every direction, lock and review starts from what the player must read now. *Example:* in a lava obby the lava's glow is lowered and the safe platforms get the brightest tops, even though a hotter lava looked better in the key art. *Check:* RD1: from the phone-size grey of the busiest capture, before reading the brief again, name route, threat, objective and own state.

**P2 Judge it where players meet it.** Game camera, phone size, real place, effects, other players and UI on, lowest quality; never a beauty shot or an editor view. *Example:* a hub fountain approved from the Blender render hid the shop door at the spawn camera. *Check:* EV4: every verdict cites a manifest row of a game-camera capture at phone size; turnarounds alone give NOT REVIEWED.

**P3 Decide what is read first; spend contrast only there.** Rank 1-2 read-first items per moment, lower everything else first, keep the value extremes for small focal spots, keep each layer in its band. *Example:* a boss arena's floor and pillars drop to the environment band so the boss's glowing core is the only near-white. *Check:* RD2-RD5: the focal item has the highest local contrast pair; layer bands measured on the environment-only capture and mask captures, never on a layer cut (`art-review/references/look-check.md` §1).

**P4 Big before small.** Rough, grey and black-fill, then light, colour, material, detail, effects; in passes over the whole frame. *Example:* a tycoon's factory direction is chosen from four grey roughs before anyone paints conveyor rust. *Check:* DR4: the grey and black-fill pass is dated before the colour pick; review notes never fix detail while a big-read note is open (FB5).

**P5 Shape and silhouette carry identity and meaning.** A few big identifying shapes, one shape vocabulary from big forms to UI corners, shape meanings tested per game. *Example:* every enemy in a tower-defense game carries a forward wedge; every friendly tower is round-topped. *Check:* SH1, SH5: subject, role and mood named from black-fill at phone size; off-vocabulary shapes counted.

**P6 Less is more.** The fewest shapes, colours and layers for the strongest read; detail clumped with rest areas; masses indicated. *Example:* a pet shop's back wall drops from 40 shelf props to 6 clustered at the counter. *Check:* RD8: in the squint view busy zones sit only on the named detail spots; MD2: detail invisible at phone size is cut.

**P7 One code for meaning across the whole game.** A colour, shape, motion pattern, material or screen position means one thing everywhere; reserved hues stay out of decoration. *Example:* the danger red is removed from flower beds and banners after the reserved-hue share showed it in 3 % of the hub. *Check:* CL1-CL2: reserved-hue share outside gameplay objects near zero; no hue with two meanings in the colour-role table.

**P9 Push what must read past real, on a believable base.** Hook shapes, heads, signature items and landmarks bigger and clearer than life; construction, contacts and scale believable underneath. *Example:* the courier's satchel is doubled in size and buckled on with visible straps. *Check:* SH2, ID1: each pushed feature changes the black-fill at phone size; attachments and scale references are present (MD5).

**P10 The subject's character drives every choice.** A character card, a prop's or place's 3-5 personality words, a sell list; every shape, colour and light traces to them. *Example:* a "grumpy, old, proud" lighthouse gets a leaning stance, chipped paint and one warm window. *Check:* DR8 and ID7: each choice traces to a card line; your cold read of the capture gives back the card's words.

**P11 One world, one style; identity survives every variant.** The bible's anchors over any maker's habit (the image model's generic default is a habit); variants keep every identity anchor. *Example:* a winter event reskins the hub with snow, but the landmark silhouettes and colour roles do not change. *Check:* ID1, ID4: the piece beside 2-3 anchors at the same size reads as the same game; every listed anchor is present.

**P12 Controlled variation, never exact repetition.** Hue shifts inside a material, wear where hands go, one asymmetric element, kit pieces rotated, never a flat fill or a twin. *Example:* market stalls built from one kit get three roof tints and rotated awnings so no two read the same in one view. *Check:* CL6, MD4: more than one colour cluster inside each material family; no piece repeated at the same angle in one capture.

**P13 Problem, constraints and target before making anything.** The brief names the problem, the constraints and the success test before the first prompt; deviations are said out loud. *Example:* a direction brief for a phone runner states "read the next lane in 0.5 s at 800x360" before style words. *Check:* DR1.

**P14 Research, then many distinct options, then a reasoned pick.** Our anchors first, then the real world, one outside source; many hooks; a warm-up set aside; one radical option; the pick with reasons. *Example:* hooks for a spooky school came from a museum night, a ship's hull and a clock workshop; the clock workshop won for its silhouette read. *Check:* DR2-DR5.

**P15 Cheap stages first; gates freeze decisions; do not be precious.** Rough images and engine blockouts before polish; after the direction gate nothing big moves without a decision; a direction that fails is dropped, not patched. *Example:* the second lighting variant of a greybox replaced the approved concept's sunset because the route read better. *Check:* DR4, FB6: the gate record shows a capture per stage; later changes are tickets.

**P16 Critique against the goal, one named problem at a time.** Goal questions, the layer named, the worst problem first, a paint-over when words fail, fresh eyes (mirror, grey, a cold read). *Example:* "the shop does not read first: lower the fountain's spray contrast" with a paint-over on capture c03, not "make it pop". *Check:* FB1-FB5.

**P17 Build for the next craft and the engine.** Ask what each craft needs, give it measurable standards (bands, roles, light, anchors, vocabulary) and room for its own decisions; stay inside phone budgets. *Example:* the VFX designer gets the danger role and the effect shape code, never particle counts. *Check:* BB2, FB7: briefs carry sourced values and open fields; the receivers' hand-backs list no unanswered look question.

**P18 Know when it is done.** Stop criteria written before work: the read-first items win, every material reads at game size, the finish matches the anchors; notes that repeat end the round. *Example:* a direction round stops after the owner picks; a fourth "slightly better" option is a follow-up, not a delay. *Check:* HB2: budget used and each stop criterion shown passing.

**P20 Every player can read it.** Meaning never rides on colour alone; the busiest scene still reads in grey and with sound off; intense channels have reduced versions that keep the information. *Example:* team colours also differ by helmet crest and banner shape. *Check:* CL3: the grey capture tells every team, tier and state apart.
