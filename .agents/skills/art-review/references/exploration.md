# Exploring visual directions with ChatGPT reference images

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `art-review`. Sources: `knowledge/reference/art-direction/02` §1, `03` §3, `04` §4.1, `05` §3; `reference-images` skill.

## 1. Inputs before any image
| Input | From | Missing → |
| --- | --- | --- |
| Player fantasy, repeated decisions, camera, movement speed, simultaneous actors, tone, key state changes, target devices | game designer (preproduction step 1-3) | ask; list the visual consequences the brief leaves open (02:D1) |
| What must read first; which silhouettes carry role; what color means; how scale supports the fantasy; excluded references | game designer's art-director brief (`preproduction/references/handoffs.md`) | ask |
| Owner's taste log and art decisions | `knowledge/design/decisions.md`, game taste log | none yet: say so |
| Owner's own references | `content/art/references/` (local-only, never attached to prompts unless the owner says so) | none |

## 2. Reference buckets (keep apart, label every image)
| Bucket | What it is | Binding? |
| --- | --- | --- |
| Studio evidence | a documented precedent (`art-direction/references/precedents.md`) | teaches a relationship, never a look to copy |
| Observation | a screenshot, photo or owner reference | teaches a named point only ("take: rim light separates the hero"); real photos win for real subjects (05:OR15) |
| Exploration | generated candidates | not binding; may conflict on purpose |
| Approved target / anchor | owner-approved image with its anchor record | binds only the attributes its record names |

Write `take:` and `avoid:` for every image you hand on (02:D7; `rules/messages.md` §1).

## 3. Direction candidates
0. **Span style families first.** Image models and agents both drift to one default: premium stylized painted 3D with dramatic fantasy lighting. Before choosing candidates, place each on the family map and take them from different families unless the owner fixed one: Roblox-native blocky plastic · flat outlined cartoon · cel-shaded anime · low-poly flat-shaded · voxel or pixel · clay or vinyl toy · painted stylized 3D · realistic. Two candidates from the same family are one direction (owner J009-D13: "Why is it that we keep getting these like fantasy-looking images?").
1. **2-3 genuinely different directions** (count is a project choice; the paper found no evidence for an ideal number, 02:D6). Each differs in at least one of: proportion, material language, detail density, light, camera reading, emotional register. A palette swap is not a direction.
2. **Same subjects, same cameras.** One cast (hero character, key place, one icon or prop) rendered in each direction; the cheapest proven way to pick a style is one page, same subjects, same pose, 3-4 styles (05:AB10). If one candidate has a kinder camera or light, say so (02:D9).
3. **Packet per candidate** (02:D8): the gameplay problem it solves; the 2-3 images; a gameplay-camera composition; a phone-size thumbnail (`look_check.py thumb`); a grayscale version (`look_check.py value`); a line each on shape, value, color roles, material, light, hierarchy; appeal; risks (what Roblox may not render cheaply, what may fight readability).
4. **Thumbnail first.** Resolve composition, light and values small and cheap before spending detail (Riot splash practice, 02:D16-D18).
5. **Owner picks.** Present the packets side by side; one recommendation with its reason; record the owner's words as a decision.

## 4. Making the images
- Write a temporary bible for exploration (one `WORLD STYLE LOCK` per candidate in separate files, e.g. `knowledge/jobs/<job>/art/direction-a-bible.md`) and run `python tools/art/art_refs.py --bible <file> print <manifest>` then `run`. Never write candidate styles into the game's real bible.
- Identity = subject only; style words live in the lock (`reference-images` I-03).
- **Prompt budget** (`reference-images` I-11, owner J009-D14): for direction images keep the subject to one or two lines and the must-haves to 1-3; put the effort into a rich style lock (palette with named colors, light, materials, edges and lines, proportions, where detail goes) and into anchors. Do not fix layout, counts or camera details while exploring a look.
- **Subject words carry genre.** Torches, spears, cloaks, dragons and storm peaks pull every style toward fantasy; hoodies, flashlights and a backyard pulled the same blocky style to everyday play (style probe 2026-10-21, `knowledge/jobs/J009-art-director/art/style-probe/probe-results.md`). Use genre words only where the game's fantasy needs them.
- **Gameplay views say "in-game screenshot"** (real-time game rendering, not an illustration, not a poster); "key art" pulls toward polished illustration and belongs to marketing.
- **Name the light's mood.** "Night" alone gives the model's cinematic default (moonlit cloud sea, rim-lit cliffs) in every style; say what the night should feel like (bright and playful, cozy, scary) and how dark it may get.
- One image = one new chat (the tool does this; `reference-images` I-12). For directions, set `anchors` to `none` or to that direction's own anchors only, so no other direction's style leaks in. Otherwise name anchors explicitly in the `anchors` column for every row; the tool otherwise picks owner anchors by row id and always adds the newest approved generation (J009 lead-notes N2-N3).
- Anchors guide the whole look (shape, proportion, color, light, materials, rendering); the lock wins where they disagree (owner J009-D11). So an approved anchor's lighting carries into new images: approve anchors whose whole look you want repeated.
- Record per image: model/route used, lock revision, anchors attached (the tool's `.json` record holds prompt and inputs).
- Max 2 regenerations per image, then report (kit cost cap, not a research number).

## 5. Review a generated image before it can become an anchor
| Check | Fail sign |
| --- | --- |
| Views agree, construction is possible | a part exists in one view only; impossible joints; hidden geometry implied |
| Counts and positions as asked | extra or missing limbs, panels, items; left/right swapped (kit test 2026-10-21, `reference-images` I-10) — count with your eyes, then confirm with a crop |
| Light is consistent | two suns; shadows that disagree with highlights |
| No generic substitution | the subject drifted to a stock version ("a generic knight") |
| Proportion drift | head, hands or props changed between images of the same subject |
| Text, logos, franchise traits | any lettering, logo or recognizable franchise design (`platform-policy`) |
| Reads small | `look_check.py thumb` at the real slot: identity features survive. Full scenes have no flat background: mask the focal subject with `--box` (from the image's measured bounds) and test at a stress size of 480x270 for a landscape concept |
| Matches the lock | each lock clause visibly kept; list any clause broken |

Fix the identity or the lock, not the image by hand. A rejected image goes to `_rejected/` with its prompt record and a one-line reason (05:AB11; 03:AN3).

## 6. From pick to anchors
1. Owner picks a direction → write the first bible revision (`references/art-bible.md`).
2. Propose anchors: one per purpose that matters (shape/proportion, material/edge, palette roles, light/mood, gameplay composition, marketing framing), each with what it controls and what it does not (03:AN2).
3. Owner approves each anchor → decision row with the owner's words → `python tools/art/art_refs.py approve <family> <id>`.
4. Ask specialists for representative tests (modeler: shape and material; environment designer: composition and traversal; UI: controls; VFX and animator: one shared event) before calling the direction proven (04:PS06).
