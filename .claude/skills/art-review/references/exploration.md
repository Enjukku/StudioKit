# Exploring visual directions with ChatGPT reference images

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-review`. Sources: `knowledge/reference/art-direction/02` §1, `03` §3, `04` §4.1, `05` §3; `reference-images` skill. Rebuilt by J018 maker art-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): hooks before images, the warm-up and the radical option, the grey and silhouette pass, the research board (§7), the image budget (§8); repair round 2: the six concept-art questions in the packet, one cap per round including regenerations. Checks: `self-review.md` DR1-DR11.

## 1. Inputs before any image
| Input | From | Missing → |
| --- | --- | --- |
| Player fantasy, repeated decisions, camera, movement speed, simultaneous actors, tone, key state changes, target devices, the target experience | game designer (preproduction step 1-3) | ask; list the visual consequences the brief leaves open (02:D1) |
| What must read first; which silhouettes carry role; what color means (reserved gameplay colours); how scale supports the fantasy; excluded references; the mechanics and numbers the look must show | game designer's art-director brief (`preproduction/references/handoffs.md`) | ask |
| The problem the images answer, the constraints (camera, device, budget, quality floor), the success test | you write them (`art-direction` §3 step 1) | no image before they exist |
| Owner's taste log and art decisions; closed directions | `knowledge/design/decisions.md`, game taste log, the job's closed-doors list | none yet: say so |
| Owner's own references | `content/art/references/` (local-only, never attached to prompts unless the owner says so) | none |

## 2. Reference buckets (keep apart, label every image)
| Bucket | What it is | Binding? |
| --- | --- | --- |
| Studio evidence | a documented precedent (`art-direction/references/precedents.md`) | teaches a relationship, never a look to copy |
| Observation | a screenshot, photo or owner reference | teaches a named point only ("take: rim light separates the hero"); real photos win for real subjects (05:OR15) |
| Exploration | generated candidates | not binding; may conflict on purpose |
| Approved target / anchor | owner-approved image with its anchor record | binds only the attributes its record names |

Write `take:` and `avoid:` for every image you hand on (02:D7; `rules/messages.md` §1).

## 3. Direction candidates (the rough-options stage)
0. **Span style families first.** Image models and agents both drift to one default: premium stylized painted 3D with dramatic fantasy lighting. Before choosing candidates, place each on the family map and take them from different families unless the owner fixed one: Roblox-native blocky plastic · flat outlined cartoon · cel-shaded anime · low-poly flat-shaded · voxel or pixel · clay or vinyl toy · painted stylized 3D · realistic. Two candidates from the same family are one direction (owner J009-D13: "Why is it that we keep getting these like fantasy-looking images?").
1. **Hooks before images.** Write 6-12 one-line hooks, each from a different source or reading of the theme (past, future, "what is this object really?", a material, a place outside games), each with a one-line fiction that explains its major parts ("islands folded from old parcel paper"). The first idea you had is labelled **warm-up** and set aside: it sits in the range of expectation. Hooks are text and cost no images.
2. **Keep 3-4, genuinely different** (count is a project choice; 02:D6). Each differs in at least one of: proportion, material language, detail density, light, camera reading, emotional register. A palette swap is not a direction. One is **radical**: it changes a primary trait (silhouette, main material, the light) so the final can be close to the safe option only because the radical lost.
3. **Same subjects, same cameras, equal low finish.** One cast (hero character, key place, one icon or prop) rendered in each direction at the gameplay camera; the cheapest proven way to pick a style is one page, same subjects, same pose, 3-4 styles (05:AB10). Uneven polish makes the polished option win for the wrong reason; if one candidate has a kinder camera or light, say so (02:D9).
4. **Grey and silhouette pass before colour.** For every option: the grey (`look_check.py value` luminance image) and the black-fill at phone size (`look_check.py thumb`); the read-first item holds the strongest local contrast; the subject is named from its fill; layers keep their bands. Colour is judged only on options that pass: values first, colour second (DR4).
5. **Packet per candidate** (02:D8): the gameplay problem it solves; its hook and fiction line; the 2-3 images; a gameplay-camera composition; the phone-size thumbnail and grey JSON paths; a line each on shape, value, color roles, material, light, hierarchy; answers to the six concept-art questions the game designer asks for (`preproduction` P-03: silhouette and role, scale, readability at the game camera, key materials, character relationships, the signature moment); appeal; risks (what Roblox may not render cheaply, what may fight readability).
6. **Owner picks.** One sheet with the 2-3 options that passed item 4 (the recipe's G1 count), labelled, same finish and layout; the options that failed are listed under it with their failing numbers, never shown as equals; the goal question; one recommendation with its reason tied to the brief; a rejection reason per option; a good accident from a rejected option is named so it can be kept. Record the owner's words as a decision; a direction goes to the job's closed-doors list only after the owner's words close it. Only one option passed: say so and show it with the best failing one and its numbers, or run one more round inside the budget. Options merge only on purpose ("A's silhouette + B's materials"), stated in the next prompt.

## 4. Making the images
- Write a temporary bible for exploration (one `WORLD STYLE LOCK` per candidate in separate files, e.g. `knowledge/jobs/<job>/art/direction-a-bible.md`) and run `python tools/art/art_refs.py --bible <file> print <manifest>` then `run` (manifest ids: lowercase letters, digits, `-` and `_` only; the tool refuses others). Never write candidate styles into the game's real bible.
- Identity = subject only; style words live in the lock (`reference-images` I-03).
- **Prompt budget** (`reference-images` I-11, owner J009-D14): for direction images keep the subject to one or two lines and the must-haves to 1-3; put the effort into a rich style lock (palette with named colors, light and its direction, materials, edges and lines, proportions, where detail goes, what never appears: the reserved hues on decoration) and into anchors. Do not fix layout, counts or camera details while exploring a look.
- **Subject words carry genre.** Torches, spears, cloaks, dragons and storm peaks pull every style toward fantasy; hoodies, flashlights and a backyard pulled the same blocky style to everyday play (style probe 2026-10-21, `knowledge/jobs/J009-art-director/art/style-probe/probe-results.md`). Use genre words only where the game's fantasy needs them.
- **Gameplay views say "in-game screenshot"** (real-time game rendering, not an illustration, not a poster); "key art" pulls toward polished illustration and belongs to marketing.
- **Name the light's mood and direction.** "Night" alone gives the model's cinematic default in every style; say what the night should feel like (bright and playful, cozy, scary), how dark it may get, and where the key light comes from.
- One image = one new chat (the tool does this; `reference-images` I-12). For directions, set `anchors` to `none` or to that direction's own anchors only, so no other direction's style leaks in. Otherwise name anchors explicitly in the `anchors` column for every row; the tool otherwise picks owner anchors by row id and always adds the newest approved generation (J009 lead-notes N2-N3).
- Anchors guide the whole look (shape, proportion, color, light, materials, rendering); the lock wins where they disagree (owner J009-D11). So an approved anchor's lighting carries into new images: approve anchors whose whole look you want repeated.
- Record per image: model/route used, lock revision, anchors attached (the tool's `.json` record holds prompt and inputs).
- Max 2 regenerations per image, then report (kit cost cap, not a research number). Generating and downloading needs the owner's yes for the batch (`reference-images` §4 "Who generates"); without it, write `image-prompts.md` and list `images: pending`.

## 5. Review a generated image before it can become an anchor
| Check | Fail sign |
| --- | --- |
| Views agree, construction is possible | a part exists in one view only; impossible joints; hidden geometry implied; a costume piece with no attachment |
| Counts and positions as asked | extra or missing limbs, panels, items; left/right swapped (kit test 2026-10-21, `reference-images` I-10) — count with your eyes, then confirm with a crop |
| Light is consistent | two suns; shadows that disagree with highlights; light from another side than the bible's key light |
| No generic substitution | the subject drifted to a stock version ("a generic knight"); the likeness drifted from the anchor images |
| Proportion drift | head, hands or props changed between images of the same subject |
| Text, logos, franchise traits | any lettering, logo or recognizable franchise design (`platform-policy`) |
| Reads small | `look_check.py thumb` at the real slot: identity features survive. Full scenes have no flat background: mask the focal subject (a mask from its black-fill, `look-check.md` §2) and test at a stress size of 480x270 for a landscape concept |
| Matches the lock | each lock clause visibly kept; list any clause broken; no reserved hue on decoration |

Fix the identity or the lock, not the image by hand. A rejected image goes to `_rejected/` with its prompt record and a one-line reason (05:AB11; 03:AN3).

## 6. From pick to anchors
1. Owner picks a direction → write the first bible revision (`references/art-bible.md`), with the standards of its §7.
2. Propose anchors: one per purpose that matters (shape/proportion, material/edge, palette roles, light/mood, gameplay composition, marketing framing), each with what it controls and what it does not (03:AN2).
3. Owner approves each anchor → decision row with the owner's words → `python tools/art/art_refs.py approve <family> <id>`.
4. **A reference is a blueprint, not the product:** it stops when shapes, values, colours and the focal point are settled. Sheets for a model include front, side, back and the game-camera view; parts left abstract on purpose are marked PROPOSAL placeholders and listed as open items. The modeler lists the image's gaps; you decide each inside the bible or with a targeted paint-over; the built asset must keep the image's iconic qualities at least as strong (ID12).
5. Ask specialists for representative tests at the game camera next to a player-size avatar before calling the direction proven (modeler: a blockout or proxy of the hero subject; environment designer: one key place in greybox with 2-3 lighting variants; UI: controls; VFX and animator: one shared event) (04:PS06). No polish is asked for before these pass.

## 7. Research board and keyword table
The board and the keyword table follow `reference-images/references/rounds.md` §2 (two halves, one outside-games source family and one disliked reference, one narrow direction with pillar words, key features and a sensitivity note, fusions, missing reference made, keyword table): the one copy. A style-direction round adds:
- **One named unexpected element** per board, beside the outside-games source family.
- **A new theme's library** (shorthand motifs, iconography, a name and a logo idea: `art-direction/references/identity-variants.md` §2) is built from the board and recorded in the Theme libraries row of `art-bible.md` §7.

## 8. The image budget for a direction round
Under the light-check rule (owner J005-D8: numbers for every case, images only for a failing number plus a few key cases). A brief's own cap always wins. A style-direction round is its own round type, not the rough round of one subject (`reference-images` R1, at most 6 images): it shows the same cast of 2-3 subjects in each of 3-4 directions (§3 item 3), so a style is judged apart from any one subject, and it has the cap below; each image keeps `reference-images`'s rules (one per chat, at most 2 regenerations, highest quality, `reference-images` I-13).
| Item | Starting budget (PROPOSAL) |
| --- | --- |
| Hooks | 6-12 written lines; no images |
| Generated roughs per round | at most 9 images per round including regenerations |
| Measured | every rough: `value` (grey) and `thumb` (phone size) JSON; `silhouette` where the subject can be masked |
| Looked at | one colour-and-grey contact sheet per round (`look-check.md` §5), each rough whose number fails, the pick; nothing else |
| Owner sheet | one image per option that passed the grey pass (2-3, the recipe's G1 count) on one labelled sheet; failing options as a numbers list |
| Report | images generated, regenerated, measured, looked at |
