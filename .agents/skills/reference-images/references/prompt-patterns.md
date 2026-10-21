> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Prompt patterns for `reference-images`. Sources: OpenAI Codex docs, "Image generation" page (built-in model `gpt-image-2`; text supplied by the owner 2026-10-20) = **OAI**; the DestructionSimulator art pipeline (locks, anchors, Tripo refs, 2026-09 to 2026-10) = **DS**. Patterns marked [P] are starting points until a test batch confirms them.

# Prompt patterns

## 1. Rules for every prompt (OAI)
| Rule | How it shows up in our prompts |
| --- | --- |
| 1-3 clear sentences usually suffice | `identity` stays short; the lock carries the style |
| Say the image's **purpose** and audience | first words of `identity`: "Model reference for…", "Key-pose sheet for…" |
| Name the **main subject and what is happening** | one subject (or the named set), its action or pose |
| Describe setting, composition, style | composition in `identity`; style only in the lock (I-01) |
| Framing, dimensions, lighting, colours, materials **when they matter** | camera, crop and lighting are in each family's lock; add only what this image changes |
| State **constraints**, including what must not appear | each lock ends with its "no …" list; add subject-specific ones ("no held weapon") |
| **Concrete visual language** over reactions | "light from the upper left", not "beautiful lighting"; "chunky, short legs", not "cute" |
| **Repeat any requirement that must stay fixed** | the lock repeats on every call; repeat a must-keep detail of this subject in `identity` |
| Ask for an **original** treatment, not a brand, product, artist or artwork | never name a franchise or artist; describe the qualities instead (I-07) |

## 0. How to prompt GPT Image 2.5 (OpenAI's guide, owner-supplied 2026-10-21; synthesized)
Start from the image you need (what it is for, the subject, the few things that must be visible), then:
- Describe **visible** things (materials, light, colours, medium, scale, atmosphere), not mood words alone; to avoid the glossy default, say "not cinematic, no dramatic colour grading".
- Number every attached image and give it one role (subject, style, palette, background).
- Keep a character consistent by reusing its reference image and repeating its defining details.
- UI images: describe the screen as a shipped product (layout, hierarchy, spacing, real elements), never as concept art.
- Edits: "change only X", list what must stay, one change per pass.
- Quality is a setting, not prompt words: try a higher quality setting before rewriting a prompt (API route only).

## 1a. Prompt budget (owner J009-D14)
| Image kind | How exact | Say | Leave to the model |
| --- | --- | --- | --- |
| Look, mood, concept, key art, style exploration | **light**: 1-3 short sentences of subject | what it is for; the subject; 1-3 must-haves (what reads first, the feeling); the style via lock and anchors | camera details, lighting details, placement, counts of decorative things, background detail |
| Working references: model reference, pose sheet, VFX key frames, icon, UI element | **exact** where a builder depends on it | views, pose, exact counts of panels or poses, parts that must exist, background color for cut-out | everything that is not a build input |
**Style sets (one subject, several styles):** keep the shared subject text identical and short, and keep colour and light out of it ("washes the scene in warm orange" overrode four styles' palettes; only "X is the brightest light" belongs in shared text). Each style paragraph carries its own palette, light, materials and construction, and names what must not slip into another medium (photoreal fire in a clay world, painted backgrounds in a low-poly world). Separate sessions still pick the model's default staging; if the set needs variety, give each style its own one-line framing (style test J009-T14, 2026-10-21).

Signs of an over-specified image: mirrored or grid-like layout, repeated identical elements, everything at the same distance, odd joins, a stiff "AI" finish. Fix by deleting rules, then regenerate once.

## 1b. Lessons from the kit test batch (2026-10-21, 10 + 2 images, `gpt-image-2`)
| Lesson | What happened | Rule |
| --- | --- | --- |
| **Same subject across images: attach it** | A pose sheet of an already-designed character, written in words only, drew a different, bigger character with goggles. With the approved sheet attached as `inputs` ("Image 1 is the approved character: keep … exactly"), it drew the same character | any image of an existing character, creature or prop attaches its approved image |
| **Say where things are and how they relate** | "a wave rises behind the city" put the wave on the town side of the dam, so the dam protected nothing. Naming the order left to right and "the wave is about to hit the dam, not the town" fixed it | concept and layout images name positions (left, middle, right, foreground) and the key relationship |
| **Name exact counts (working references only, see §1a)** | "key frames … left to right" gave 7 panels instead of 3; "exactly 3 key poses" gave 3 | write "exactly N" for panels, poses, views and items |
| Sheets add extras | a character concept sheet came back with turnarounds, expressions and props, and the subject holding a tool nobody asked for | fine for concept; for model references keep the single-view lock and list unwanted items in "no …" |
| Style held across families | 9 of 12 images matched the world lock; drift came from missing inputs, not from the lock | keep style in the lock (I-01) |

## 2. Several images in one call (OAI)
Number the images and give each one a role, with spatial words where elements combine. The tool already says "the first N attached images are inputs … the last N are design references"; in `identity`, refer to inputs by number: "Image 1 is the character to redraw; keep its colours and costume."

## 3. Edits: change one thing, keep the rest (OAI)
Use an `inputs` image and write the change: "Edit image 1. Change only <element>. Keep <subject, pose, layout, lighting, colours, crop> exactly. Do not add text or logos." Change **one element per pass**, so the rest does not drift; small targeted passes beat one big rewrite.

## 4. Text in images (OAI)
Our reference images carry **no text** (every lock says so). If text is ever needed (a logo idea for marketing): exact words in quotation marks, the capitalisation wanted, font style, size, colour, placement, and "no other text"; spell unusual names letter by letter. Final text is set in a design tool, not trusted from the image.

## 5. Identity patterns per family [P]
Write `identity` as: **purpose** + **subject** + **pose or action** + **must-keep details** + **subject-specific "no" items**.

| Family | Pattern | Example identity |
| --- | --- | --- |
| `concept` | Key art of <moment or place> for <game fantasy>; layout left to right (or foreground to background); the key relationship; focal point; a player-sized character for scale | "Key art for a dam-building game. Layout, left to right: a huge flood wave rushing down the valley; in the middle, a half-finished stone dam blocking the valley, with a small player-sized builder on top facing the wave; on the right, safely behind the dam, a small town. The wave is about to hit the dam, not the town. The wave is the focal point." (tested 2026-10-21) |
| `character` | Concept sheet of <character>: <role>, <body type>, <costume parts>, <colour accents> | "Concept sheet of a goblin blacksmith: short and wide, big hands, leather apron, soot on the face, one orange accent colour." |
| `creature` | Concept of <creature>: <body plan> with separate <parts>; <size against a player> | "Concept of a rock turtle: four stubby legs, a separate shell, a separate head on a short neck, a short tail; about twice a player's height." |
| `model` | Image 1 is the approved <subject> (attach it); model reference of it for <hand modelling or Tripo>; <pose>; <parts that must read separately>; no <props or effects> | "Model reference of the goblin blacksmith for Tripo: T-pose, hands open, apron straps and belt clearly separate from the body; no hammer, no sparks." (one view only: extra angles make Tripo build extra models, DS D-153) |
| `prop` | <prop> as <use>; <size and grip>; <moving parts> | "A heavy two-handed forge hammer: long wooden handle, square iron head twice the width of the handle, a leather grip at the bottom third." |
| `storyboard` | Storyboard panel, shot <id> of <N>: <shot size>, <angle>; image 1 is the approved <character> (attach it), image 2 the previous approved panel (attach it); <who> at <left / middle / right>, facing or moving <left / right / toward / away>, looking at <target>; <the exact action moment>; <landmarks and their side of frame>; light from <side>; no <what would contradict the geography> | "Storyboard panel, shot B of 5: close view, slightly above. Image 1 is the approved explorer: keep the face, gloves and backpack exactly. Image 2 is the approved panel for shot A: keep the beacon, pedestal and light from the upper right. The explorer's right hand reaches from the left toward the beacon in the middle, fingers just short of it; the beacon has gone dark; a faint moving reflection shows in the water behind it. No statue face visible yet." (one panel per call; arrows and camera notes stay outside the image, J015) |
| `environment` | <building or place> at true scale beside a player-sized character; <camera>; <key shapes> | "A riverside watermill at true scale beside a player-sized character; three-quarter view from slightly above; a big wheel, a stone base, a wooden upper floor." |
| `pose` | Image 1 is the approved <character>: keep <face, proportions, costume> exactly. Exactly <N> key poses for <action>, left to right: <pose 1>, <pose 2>, <pose 3>; <what the weight does>. `inputs` = the approved character image | "Image 1 is the approved character: keep his face, head shape, ears, orange headband, body proportions, apron and boots exactly; do not redesign him. Show exactly 3 key poses of this character for a heavy hammer swing, left to right: wind-up with the hammer raised high behind the head, impact with the hammer head on an anvil and knees bent, recovery with the body leaning back; the hammer's weight pulls the arms." (tested 2026-10-21) |
| `vfx` | Exactly <N> key frames of <effect> for <gameplay moment>, left to right: <frame 1>, <frame 2>, <frame 3>; <shape and colour change over time> | "Key frames of a fireball impact on a stone wall: bright white core at contact, an orange ring of sparks spreading outward, grey smoke rising and thinning." |
| `ui` | Mood of <screen or element> for <player moment>; <hierarchy: what is biggest>; placeholder blocks for text | "Mood of a reward screen after a boss fight: a large chest in the centre, three item slots below, one big confirm button at the bottom; placeholder blocks for all text." |
| `icon` | Game icon of <object> meaning <meaning>; <silhouette feature that reads at 48 px> | "Game icon of a gold coin meaning soft currency: a thick coin tilted toward the viewer with one bright highlight on its rim." |

## 6. Refining (OAI, DS)
1. Start with the core idea; check it (SKILL §5 I-05).
2. Fix one element per pass with an edit (§3); keep everything else named as unchanged.
3. When a family keeps failing on the same point, fix the **lock** in the art bible (the owner approves), not each prompt.
4. Max 2 regenerations per image, then report what fails.

## 7. Usage and cost (OAI)
Built-in generation counts toward the owner's Codex usage limits and uses them **3-5× faster** on average than turns without images, depending on quality and size. Plan batches with `--limit`, and name the image count in the brief. For large batches the API with `OPENAI_API_KEY` is an option at API prices: the key lives in the owner's environment only, never in the repo or a manifest, and the owner decides (needs-decision).
