# Writing and keeping the art bible

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-review`. Sources: `knowledge/reference/art-direction/02` §2, `03` §3, `04` §2, `05` §3; template `templates/skill/art-bible.md`; tool `tools/art/art_refs.py`. Revised by J018 maker art-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): every lock names its test (§4), the standards every craft measures against (§7); repair round 2: separation targets, the lower-body value, the one anchor count. Checks: `self-review.md` BB1-BB4.

## 1. What the bible is for
A decision tool, not a picture encyclopedia. Another maker (agent or image model) must be able to answer from it: what is fixed, what may vary, which image shows the rule, how approval is judged. Test it that way: could a new agent make a compatible asset without inventing a missing decision? An empty field is an open decision, never permission to fill it silently (02:BF-p1 to BF-p3).

## 2. Two layers in one file
| Layer | Where | Read by |
| --- | --- | --- |
| **Prompt locks** | the families table and the fenced `text` blocks whose first words are `<NAME> LOCK:` | `art_refs.py` (machine-read: keep exactly one copy of each lock, keep the first words) |
| **Direction record** | the other sections of the template (identity, camera, color roles, variation, exceptions, anchor register, cross-craft contracts, technical envelope, change log) | every agent and the owner |

New direction content never goes inside a lock block: the tool would send it to the image model. Run `python -m unittest discover -s tools/tests -p "test_art_refs.py" -t tools/tests` after editing the template's machine-read parts.

## 3. Fields (from the paper's template, mapped to the kit template)
| Field | Holds | Review consequence |
| --- | --- | --- |
| Identity and intent | fantasy line, pillars, owner decision ids, bible revision | reject work that promises another fantasy, however polished |
| Scope and camera | gameplay viewpoints, capture states (normal distance, closest view, smallest presentation), device classes, crowd states, supported orientations and input | compare under real use conditions |
| Locks | shape, proportion, value, palette roles, material, edge, light — each as relationship + purpose + scope + example + failure example + test | every change names the lock it touches |
| Allowed variation | what may differ by biome, faction, rarity, role, mood, event | keeps variety from being called drift |
| Color roles | role → treatment → non-color backup → where it must not appear | one meaning per treatment across world, VFX, UI, marketing |
| Anchor register | id, file, purpose (what it controls), what it does not control, revision, lighting/camera of the image, approval decision id, status (current / superseded / rejected) | only current anchors bind |
| Exceptions | the exception, why, which locks stay protected, how it is recognized as intended, decision id | later agents do not copy it as the new default (03:CM8) |
| Cross-craft contracts | per recurring event: importance rank, owner of each cue (model, motion, VFX, UI, sound), shared state name | test combinations, not pieces |
| Technical envelope | supported rendering modes and quality floor, device evidence, unresolved measurements | visually approved ≠ runtime approved |
| Change log | revision, date, what changed, why, owner's words, affected assets, migration plan | no silent change |
| Craft standards (§7) | screen order and value bands, reserved colours, key light per place, shape vocabulary and effect shape code, palette roles, motion line, UI thematic, identity anchors and recognition features, group palettes, theme libraries, tier and format exceptions | every craft measures against the same numbers; a missing row makes their checks fall back to PROPOSAL starting values |

The paper's filled example ("Lantern Workshop") is fictional: copy its writing pattern, never its content (02:§2.3).

## 4. Writing a lock
- Name an observable relationship, not an adjective. "Premium", "stylized", "polished" or "like <studio>" are not locks (03:CM6).
- Good pattern: "Interactable objects keep one graspable feature (handle, wheel, lid) that decorative clutter never repeats; interactables carry the warm accent, clutter never does; backup cue: a slow glint every few seconds." It names the relationship, the forbidden confusion and the backup channel (02:LK1, LK3).
- Lock identity and relationships; never freeze every pixel of one anchor (03:CM7).
- Put exclusions in the lock (no text, no logos, plain background, cut-out color) so briefs need not repeat them (05:AB02).
- Technical budgets (particles, triangles) belong in craft skills with measured sources, not in the bible (05:AB07).
- **Every lock names its test:** a `look_check.py` measure or a line of `self-review.md` with the input it runs on ("danger hue share outside gameplay objects near 0 on the busiest capture: CL1"). A lock nobody can check is a wish (BB1).
- **One world, one style:** the WORLD STYLE LOCK names the style levers (saturation range, proportion push, realism of props and places, value structure), the shape vocabulary, the key light direction and the reserved hues that never appear on decoration, so every image starts from the same game.

## 5. Revisions and drift
- Bible revision id in the header (`rev N, date`); every manifest row, review and brief names it.
- **Drift check** at every review and every owner decision that touches looks: lock text vs newest decision vs current anchor. Any disagreement: propose the fix to all three in one edit (05:AB04-AB05).
- Retire test locks after the test; one live lock per family (05:AB05).
- Each new environment gets its palette roles recorded in the bible when it is approved, not only in concept images (05:AB06).
- The studio always uses the newest image model (owner J009-D9). If a batch suddenly drifts from the anchors, re-run one approved manifest row and compare before changing any lock (03:CM5).

## 6. Changing the style (transition packet)
Name the problem the change solves (inconsistency, unreadability, new camera or audience, stronger fantasy, production limit). Then write one packet (04:EV1-EV3, TS2):
| Item | Content |
| --- | --- |
| Previous anchor(s) and lock text | as approved, with decision ids |
| Proposed replacement | new lock text and candidate anchors |
| Identity kept | the recognition cues that must survive |
| Rules changed | each changed relationship, why |
| Mixed-scene test | old and new assets in one scene at the gameplay camera |
| Affected assets | list, ordered by importance and dependency |
| Migration | new work adopts the new revision; old assets updated by priority; owner told the temporary mix will show |

Owner approves the packet; nothing is relabelled as approved under the new revision without review.

## 7. The standards every craft measures against
The kit template does not yet carry these sections (proposal J018); add them to the game's bible under the direction record, never inside a lock block. Each row: value, source (owner decision id, measured capture, or PROPOSAL), and the check that uses it. Missing value → write `PROPOSAL: <starting value>` or `UNKNOWN`, never leave it blank.
| Section | Holds | Starting value (PROPOSAL until the owner decides) | Read by |
| --- | --- | --- | --- |
| Screen order | the ranked layers for play (default: UI and gameplay VFX, characters, environment) and any moment that differs | default order | every craft; RD2 |
| Value bands | per layer, in grey-view value (the grey level of the luminance image) with the linear luminance `look_check.py value` reports: environment, characters, effects and UI; saturation band for environment materials. The kit's only copy of the starting values: other books point here | environment 15-85 % (0.020-0.69), characters 8-92 % (0.007-0.83), VFX and UI 0-100 %; no pure black in the environment (near-black px 0); a character's lower body 15-20 % below its upper body in grey-view value (lower ÷ upper luminance median about 0.6-0.7) | modeler, environment designer, VFX; RD3, RD5, RD13 |
| Separation targets | subject/ring median ratios (`look_check.py value` with a mask; 1.0 = no separation): a character or dummy against its environment ring; critical markers and the smallest gameplay object against their floor; the player band's neutral-chroma limit, the stray saturated share outside the focal elements and eye-path accents, and the flat-fill limits, in the environment designer's units (they propose, the owner decides) | character 1.5:1, marker 3:1; chroma, stray-share and flat-fill limits: the environment designer's starting values (`environment-design/references/review.md` VB5, VB6, VB12) | modeler, environment designer, VFX; RD6, RD13, CL15 |
| Reserved colours | per gameplay meaning (danger, enemy, team, interactable, route, reward): swatch hex (authored and as rendered in a capture), its shape or icon partner, the saturation limit in set dressing, the share allowed outside gameplay objects | share near 0 (owner sets the number); reserved-hue distance CIEDE2000 10 (the kit's only copy) | all crafts; CL1-CL3 |
| Colour roles | role → treatment → non-colour backup → never used for (the template's table), plus the effect colour rule (an effect's hue sits next to its caster's) | — | VFX, UI, modeler; CL2, CL10 |
| Key light per place | sun direction (Lighting.ClockTime, GeographicLatitude), fill and ambient tints, light and shadow temperatures, the chosen lighting style, which positions must never be in deep shadow. Lighting is one global service per Roblox place: one sun per place; areas inside one place differ by local lights, post effects under the camera, or a client-side Lighting change (probe in Studio before relying on it), all owned by the environment designer | one direction per place, light and shadow at opposite temperatures | modeler (renders), environment designer; CL7-CL8, CL15 |
| Shape vocabulary | the dominant shape family, the meaning per shape (danger, friendly, stable), the effect shape code (heal, shield, damage), the UI corner shape | sharp = danger, round = friendly, square = stable (hypothesis to test) | all crafts; SH5, EVT3 |
| Palette roles | per asset type and per place: dominant, support, accent, brand; group palettes per faction or team with hex values (authored, and as rendered by a role reference block in each place's light); the palette distance: how far (CIEDE2000) a material's lit face may sit from its nearest role as rendered | about 60 / 30 / 10 after the greys work; palette distance: the environment designer's starting value (`environment-design/references/review.md` VB11) | modeler, environment designer, marketing; CL4-CL5 |
| Motion line | the motion personality in a few words (snappy, heavy, floaty, bouncy) and the UI motion material (light paper flutter, heavy metal slam) | — | animator, VFX, UI; EVT1 |
| Sound pointer | the path of the game's sound identity sheet (default `output/sound/identity/sound-identity.md`): signatures, forbidden directions, sound tone words; the sound designer owns it | — | sound designer; EVT1 |
| UI thematic | one line you write: the material or world motif the UI is made of, and the chosen style book; the UI rule sheet (`content/ui/_system/rule-sheet.md`) copies the colour-roles table and never redefines it; you sign its colour-role and shape rows | — | UI designer; CP1 |
| Identity anchors | per character: the anchors (silhouette features, proportions, the source of power, signature colours) with the anchor images; the kit's only count: G1 shows 2-3 (the character recipe), the bible may hold up to 5; per item family: ranked recognition features and contact points | — | modeler, rigger, animator, marketing; ID1-ID2 |
| Theme libraries | per theme or event: 3-5 shorthand motifs, iconography, name and logo pattern, the "fans want" line, its niche against the nearest theme | — | all crafts, marketing, live-ops; ID8, DR6 |
| Tier and format exceptions | the item families' rank ladders and the rows allowed a top-tier break, taken from the progression designer's tier table; the top tier's documented break from the house style (you propose it, the owner decides); format conventions (a parody poster) allowed only in named pieces; each with its decision id | none without a decision | modeler, VFX, UI, marketing; ID6, BB4 |
| Stylisation level | detail and material level per asset type, matched between characters and places | — | modeler, environment designer; DR7 |
