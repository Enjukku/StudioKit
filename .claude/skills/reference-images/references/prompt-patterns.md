> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Prompt patterns for `reference-images`. Sources: OpenAI Codex docs, "Image generation" page (built-in model `gpt-image-2`; text supplied by the owner 2026-10-20) = **OAI**; the DestructionSimulator art pipeline (locks, anchors, Tripo refs, 2026-09 to 2026-10) = **DS**. Patterns marked [P] are starting points until a test batch confirms them. Revised by J018 maker reference-images · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): rough-option, view, material-ID, variant, paint-over and colour-vignette patterns (§5), edits as rounds (§3), words that make a subject specific (§8).

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
| Rough options (R1, any family) | **light**, and identical across the round except the hook | the round label, the hook and its one-line fiction, the subject, the read-first part; the game-camera angle only where the family's lock leaves the camera open (SKILL I-11) | everything else: options must differ by the hook, not by how much each prompt says (`rounds.md` §3 item 3) |
| Edits: paint-overs, fixes, colourways, light variants | **exact** about the one change | "Edit image 1. Change only <X>." and the list of what stays exactly | nothing: the input image carries the rest |
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
The same form runs every edit round (`rounds.md` §5-§6): a **paint-over** edits the exact review capture to show one fix; a **colourway** changes only the colours (2-3 of them, each re-checked in grey); a **light variant** changes only where the light comes from; a **merge** names its parts ("Keep image 1's outline and pose; take only the belly from image 2"). Each edit row lists what stays, because the model otherwise redraws it.

## 4. Text in images (OAI)
Our reference images carry **no text** (every lock says so). If text is ever needed (a logo idea for marketing): exact words in quotation marks, the capitalisation wanted, font style, size, colour, placement, and "no other text"; spell unusual names letter by letter. Final text is set in a design tool, not trusted from the image.

## 5. Identity patterns per family [P]
Write `identity` as: **purpose** + **subject** + **pose or action** + **must-keep details** + **subject-specific "no" items**.

| Family | Pattern | Example identity |
| --- | --- | --- |
| `concept` | Key art of <moment or place> for <game fantasy>, seen from the game camera's angle; layout left to right (or foreground to background); the key relationship; focal point (the lightest area, the rest quieter); a player-sized character for scale; for a group, the group's shape (back to back, surrounded) | "Key art for a dam-building game. Layout, left to right: a huge flood wave rushing down the valley; in the middle, a half-finished stone dam blocking the valley, with a small player-sized builder on top facing the wave; on the right, safely behind the dam, a small town. The wave is about to hit the dam, not the town. The wave is the focal point." (tested 2026-10-21) |
| `character` | Concept sheet of <character>: <role>, <body type>, <costume parts>, <colour accents>; then, only where the card needs it: its 3-4 identifying elements large and clear; brow and nose shape from the card; small accents (a pin, a charm) for personality; "no" items for anything draped over the shoulders and arms unless the brief pays for it | "Concept sheet of a goblin blacksmith: short and wide, big hands, leather apron, soot on the face, one orange accent colour." |
| `creature` | Concept of <creature>: <body plan> with separate <parts>; <size against a player> | "Concept of a rock turtle: four stubby legs, a separate shell, a separate head on a short neck, a short tail; about twice a player's height." |
| `model` | Image 1 is the approved <subject> (attach it); model reference of it for <hand modelling or Tripo>; <pose>; <parts that must read separately>; no <props or effects> | "Model reference of the goblin blacksmith for Tripo: T-pose, hands open, apron straps and belt clearly separate from the body; no hammer, no sparks." (one view only: extra angles make Tripo build extra models, DS D-153) |
| `prop` | <prop> as <use>; <size and grip>; <moving parts>; where the brief needs it: its functional parts (grip, trigger, hinge) and how it is attached or held; one clear top and bottom profile line; one costume motif repeated at big, medium and small scale, built from a few bold basic shapes; a hero item gets more distinct big parts than a common one of its class | "A heavy two-handed forge hammer: long wooden handle, square iron head twice the width of the handle, a leather grip at the bottom third." |
| `storyboard` | Storyboard panel, shot <id> of <N>: <shot size>, <angle>; image 1 is the approved <character> (attach it), image 2 the previous approved panel (attach it); <who> at <left / middle / right>, facing or moving <left / right / toward / away>, looking at <target>; <the exact action moment>; <landmarks and their side of frame>; light from <side>; no <what would contradict the geography> | "Storyboard panel, shot B of 5: close view, slightly above. Image 1 is the approved explorer: keep the face, gloves and backpack exactly. Image 2 is the approved panel for shot A: keep the beacon, pedestal and light from the upper right. The explorer's right hand reaches from the left toward the beacon in the middle, fingers just short of it; the beacon has gone dark; a faint moving reflection shows in the water behind it. No statue face visible yet." (one panel per call; arrows and camera notes stay outside the image, J015) |
| `environment` | <building or place> at true scale beside a player-sized character; <camera>; <key shapes>; 1-3 story facts shown as visible things (wear, repairs, what is left behind); 2-3 theme cues from the bible so it is not a generic place; backdrop plants and rocks as simple shapes with one clear gesture | "A riverside watermill at true scale beside a player-sized character; three-quarter view from slightly above; a big wheel, a stone base, a wooden upper floor." |
| `pose` | Image 1 is the approved <character>: keep <face, proportions, costume> exactly. Exactly <N> key poses for <action>, left to right: <pose 1>, <pose 2>, <pose 3>; <what the weight does>. `inputs` = the approved character image. Name only what this moment needs from: one clear line of action; balance over the feet unless off-balance is the point; a heavy held object close to the body, a light one held out; paired limbs doing different things; the hook shape facing the camera; a jump apex with the legs tucked; emotes pushed to full expression | "Image 1 is the approved character: keep his face, head shape, ears, orange headband, body proportions, apron and boots exactly; do not redesign him. Show exactly 3 key poses of this character for a heavy hammer swing, left to right: wind-up with the hammer raised high behind the head, impact with the hammer head on an anvil and knees bent, recovery with the body leaning back; the hammer's weight pulls the arms." (tested 2026-10-21) |
| `vfx` | Exactly <N> key frames of <effect> for <gameplay moment>, left to right: <frame 1>, <frame 2>, <frame 3>; <shape and colour change over time>. The gameplay core is the brightest part, the theme layer weaker, a few small bits last; the shape follows the bible's effect shape table; the caster's image attached so the effect's hue sits next to its colour | "Key frames of a fireball impact on a stone wall: bright white core at contact, an orange ring of sparks spreading outward, grey smoke rising and thinning." |
| `ui` | Mood of <screen or element> for <player moment>; <hierarchy: what is biggest>; placeholder blocks for text | "Mood of a reward screen after a boss fight: a large chest in the centre, three item slots below, one big confirm button at the bottom; placeholder blocks for all text." |
| `icon` | Game icon of <object> meaning <meaning>; <silhouette feature that reads at 48 px> | "Game icon of a gold coin meaning soft currency: a thick coin tilted toward the viewer with one bright highlight on its rim." |
| option (R1, any family) | Rough option <letter> for <subject>, hook: <source>. <one-line fiction>. <subject in one line>; [seen from the game camera's angle: only where the family's lock leaves the camera open; never under the `character`, `prop` or `model` three-quarter locks]; <read-first part> is the focal point. Same wording, family and background for every option of the round; the warm-up row says "the typical idea" | `character`: "Rough option C for the fire world's starter pet, hook: glassblowing. A pet whose belly is a little lantern with a flame inside. A small round puppy with big ears; the glowing belly is the focal point." `pose`: "Rough option A for the smith's hammer strike, hook: a real blacksmith's full-body swing. Exactly 1 key pose at the contact moment, seen from behind and above as the game camera shows it; the hammer head is the focal point." (both printed with no conflict, J018) [P] |
| view (build view; needs a family whose lock allows the view) | Image 1 is the approved <subject>: keep everything exactly. Show it from <front / the left side / directly behind / the game camera's angle, behind and above>, same pose and scale, one view only | "Image 1 is the approved smith: keep everything exactly. Show him from directly behind, same pose and scale, one view only." [P] (under a three-quarter lock this fights the lock: SKILL I-04) |
| material-ID (for the modeler) | Image 1 is the approved <subject>. Same view and outline; every material region as one flat colour, no shading, no texture, no outline | "Image 1 is the approved lantern pet. Same view and outline; the glass belly, the coal body, the ears and the eyes each one flat colour, no shading." [P] |
| variant (skin, tier, event) | Image 1 is the base <subject>: keep <its identity anchors, proportions, height, grip and contact points> exactly. <new theme> version: <what changes>; <the slot of a dropped landmark filled by a theme part of similar mass>; 1-3 small theme nods on existing parts; parts that do not exist in the theme replaced by one that does | "Image 1 is the base knight: keep the pan-shield, the dented helmet, the orange plume, his proportions and his grip exactly. Winter version: fur trim, a frosted pan; the plume becomes a frost-crystal crest of the same size." [P] |
| mannequin variant (modeler) | Image 1 is a render of the base model at the game camera in its plainest costume: keep its body, proportions and pose exactly. Paint <the variant idea> over it | "Image 1 is a render of the base runner in the plain suit: keep the body, proportions and pose exactly. Dress her as a beach lifeguard: an orange float on the back, a whistle, a sun visor." [P] |
| paint-over (any family; the capture's family) | Edit image 1. Image 1 is the review capture of <place or asset> at the game camera. Change only <the one fix, as a visible result>. Keep <layout, camera, characters, every object> exactly | see `rounds.md` §6 [P] |
| colour vignette (film) | Image 1 is the approved value-strip frame of beat <id>: keep the values, shapes and layout exactly; colour only, <the beat's mood colours from the bible> | "Image 1 is the approved value frame of beat 3: keep the values, shapes and layout exactly; colour only, cold blue night with the beacon as the one warm light." [P] |
| glow draft (vfx texture; the `vfx` lock asks for frames, so this needs a texture family, or a script in `vfx-craft`) | A single soft glow dot, blurred twice, with a few small irregular edges, white on a plain black background, no hard edge, centred | "A single soft white glow dot with a few small irregular wisps at its edge, on plain black, centred." [P] (key by luminance, SKILL I-09) |

## 6. Refining (OAI, DS)
1. Start with the core idea; check it with its round's lines (`self-review.md` §2).
2. Fix one element per pass with an edit (§3); keep everything else named as unchanged.
3. When a family keeps failing on the same point, fix the **lock** in the art bible (the owner approves), not each prompt.
4. Max 2 regenerations per image, then report what fails.

## 7. Usage and cost (OAI)
Built-in generation counts toward the owner's Codex usage limits and uses them **3-5× faster** on average than turns without images, depending on quality and size. Plan batches with `--limit`, and name the image count in the brief. For large batches the API with `OPENAI_API_KEY` is an option at API prices: the key lives in the owner's environment only, never in the repo or a manifest, and the owner decides (needs-decision).

## 8. Words that make the subject specific
The style comes from the lock; these are the subject words that turn a generic image into this game's subject.
| Need | Write | Not |
| --- | --- | --- |
| A keyword | its visible facts from the keyword table: colour key, setting, expression, prop ("apocalypse: dust colours, an empty street") | the keyword alone |
| Personality | 2-4 card words each turned into a visible change (heavy: a wide, low stance; proud: chin up, chest out), pulled back if the weight stops being believable | "cool", "epic", "cute" |
| Where things are | left, middle, right, foreground, background, and the key relationship ("the wave is about to hit the dam, not the town") | "a wave behind the city" |
| Size and weight | against a player-sized figure; heavy things held close to the body | sizes in words alone |
| A material | what it is and how it behaves ("dry palm leaves", "frosted glass with a flame inside"), by texture, not only by name | "magic material" |
| Detail | where it clumps (the face, the weapon, the focal prop) and that the rest stays quiet; masses as a few big clumps (hair, grass, crowds) | every strand or blade |
| Use and age | wear where hands and feet go, repairs, what is left behind, from the story facts | "old" alone |
| The unexpected element | the one named outside-genre element from the brief, once | a list of twists |
| What it must not look like | the subject's own "no" items; style "no" items belong in the lock | style bans in the identity |
