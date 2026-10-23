> Author: J018 maker reference-images · claude-opus-5-5 · high · 2026-10-22. Part of `reference-images`; built also from the owner's Riot transcripts (J018). The rounds of an image batch (SKILL §4): the brief, research, the rough round, the pick, iterate and final rounds, paint-overs, the image budget, worked examples. The lines that check each part: `self-review.md` (ids in brackets). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): outside method in direction rounds.

# Rounds: from brief to a reference the next maker can build from

## 1. The image brief (R0, before any prompt) [BR1-BR3, BR6-BR7]
Write it in the job folder, above the manifest. A field that does not apply says `n/a`; an unknown says `UNKNOWN` and is asked, never guessed.
| Field | What | Example (a pet game) |
| --- | --- | --- |
| Problem | the question the image answers, in one line; every image caption repeats it | "What does the fire world's starter pet look like, so the modeler can build it?" |
| Constraints | family; game camera and angle; the **size players see it** (the slot in px, or the subject's height in px on the phone viewport at the game camera, with its source); device; budget; quality; the rig it must fit; mechanics and numbers the look must show | `character`; third-person, behind and above; about 60 px tall on an 800x360 viewport (game profile camera, stand-in until the modeler's game-camera render exists); medium roughs, high final |
| End (success test) | what is true when the image works, checkable | "At 60 px a fresh reader says: a fire puppy, friendly, collectable" |
| Sell list | 2-4 numbered things the image must sell | 1 fire, 2 friendly, 3 belongs to the pet family |
| Read first | 1-2 parts that carry the read (often the source of power: the weapon, the casting hand, the core) | the flame tail |
| Card (characters, creatures, props, places) | 3-5 personality words and the tension; role from the game designer (what the roster lacks); how it moves; 3-4 identifying elements; 2-4 small accents that carry personality; for a known archetype, the traits that make it work | "bouncy, loyal, clumsy"; role: starter pet; moves in short hops; elements: flame tail, round body, big ears, ember eyes |
| Variant line (skins, tiers, remakes) | new version (own palette) or the same character in a new scene (base palette); the identity anchors kept; "keep core X, swap item Y for Z because W"; the tone shift and its limit; for a remake the loved traits kept and the dated ones trimmed | "winter version: own palette; keep tail, ears, eyes; swap the flame for a frost wisp because the world is frozen" |
| Story facts (places, hero props) | 1-3 facts: who uses it, what happened, how old; and the one-glance read separate from any hidden detail | "the forge is old, still in use, the smith is messy" |
| Message and symbol (icons, emblems, key art) | one message and its one sign | "a new world opens" = a crack of light |
| Camera height (icons, key art, previews) | eye level for friendly subjects, low and looking up for dominant ones | eye level |
| Keep / try | what every option keeps; what may change; one named unexpected element from outside the genre | keep: pet proportions; try: a lantern-glass belly (from glassblowing) |
| Budget and stop | images per round (§7), the quality per round, the stop criteria | stop when shape, values, colours and the focal point are settled |

## 2. Research board and keyword table (R0) [BR4-BR5]
- **Two halves.** (a) Our game: the approved anchors and art-bible images, for colour, composition and gesture. (b) The real world, per aspect (pose, material, place, phenomenon, motion), each entry with what it is for and one observed property you take ("ember: a dark crust with orange cracks, not a flat orange"). Reference made only of other games is a copy of a copy.
- **One source family from outside games** (a craft, fashion, architecture, nature, another medium), and one reference you dislike with what it teaches. In a direction round (a new look or new options), choose the outside family from the job's target-experience sentence and name the method taken, as an action that field's experts do, not a topic.
- **One narrow direction per board:** 3-5 pillar words, the 3-5 key features that make each subject read, and a one-line sensitivity note (culture, age, maturity, franchise risk: `platform-policy`).
- **Creatures:** a real source per body part ("lion face, bear hips, beetle shell"). **Fusions** (two ideas in one brief): reference the overlap: an object that is both, a costume piece of the new idea, a pose from both worlds.
- **Missing reference is made, not guessed:** a ChatGPT pose image, or a posed Blender mannequin in the game's proportions rendered from the game camera (ask the modeler or animator). Motion subjects get motion reference for their key poses. A style or light question may take painted key art for how its shadows and highlights are placed.
- **A UI or motion style** starts from a structural study of 2-3 strong references in the genre (structure only, never assets or branding), then changes toward our thematic.
- **A new theme** also proposes its library to the art director: 3-5 shorthand motifs, iconography, a name and a logo idea (`art-direction/references/identity-variants.md` §2).
- **Keyword table** before the first prompt: keyword → colour key, setting, pose or expression, prop. Every element of the first rough maps to a row, and no row is missing from it.
- References give ideas (shape language, colour, light, construction), never a design; no single reference may be recognisable in the result (`platform-policy` for franchise themes).

## 3. The rough round (R1) [RO1-RO6]
1. **Warm-up first.** The typical idea, the one that came to mind first, is one labelled row (`-warm`): it sits inside expectation and becomes the baseline every option must beat.
2. **Hooks in text first, then the strongest as roughs.** Write 6-12 one-line hooks (text, no images), each from a different source, each with a one-line fiction that explains its major parts. Sources: a material (crystal, paper, clay), an era (ancient, future), "what is this object really?" (a lamp that is a jellyfish), a place outside games, the gameplay verb (a pet that digs), a craft or fashion, an animal or plant, the subject's own lore. Keep the 3-5 strongest against the sell list for generation; the rest stay in the hook list with one line on why they were cut. One kept hook is **radical**: it changes a primary trait (silhouette, main material, the light), so a final close to the safe option is close because the radical lost.
3. **Equal finish.** Every option in one round uses the same family, quality, camera words and background, one chat each (I-12). Camera words: the game camera's angle where the family's lock leaves the camera open (`concept`, `environment`, `pose`, `creature`, `storyboard`, `thumbnail`); under a three-quarter lock (`character`, `prop`, `model`) none, so the rough keeps the lock's view and the game-camera read waits for R3 (FN13). A new subject in the game's settled style keeps the bible's anchors; a style-direction round sets `anchors` to `none` (`art-review/references/exploration.md`).
4. **Flat-ground families** (`character`, `creature`, `prop`, `model`, `pose`, `icon`, `vfx`) give a black-fill straight from the image. **Scene families** (`concept`, `environment`, `thumbnail`, `storyboard`, `ui`) do not: judge their big shapes on the grey row of the contact sheet and the 3-value study (`self-review.md` C7, measured from the full image), and trace a hero mask only for the pick (`self-review.md` §4).
5. **The locks ask for full rendering**, so a rough is a full image at the highest quality (I-13), judged by its black-fill and grey measured with the tools, never a flat drawing. There is no flat rough family and no generated value map; a rough that fails its value check is regenerated in full with a changed prompt, never edited (owner J018-D8).
6. **Per family:** a costume is explored in 2 attitude poses (hunched and aggressive, solemn), the clean turnaround comes only in R3; a signature move gets 2-3 key-pose options of the same moment, each a different reading, the approved character attached; a screen gets 2-3 whole-screen options inside the UI thematic; a concept is drawn from the game camera's angle.
7. Measure every rough, look at one real-size contact sheet (`self-review.md` §4 C2 then C6), open a rough on its own only when its number fails or it is the pick.

## 4. The pick sheet (end of R1) [PK1-PK2]
- One image: the options that passed RO4 and RO5 at equal finish, labelled A-E, at the size players see them (with the black-fill row for flat-ground families); options that failed are listed under it with what failed (the cold-read miss, the merge with the ground and its number), never shown as equals. The backdrop ratio of a flat-ground rough never decides who is on the sheet.
- **The goal question** uses the brief's goal word: "Which reads as a friendly fire pet at 60 px?", never "which do you like?".
- **One recommendation** with its reason tied to the sell list and the hook line; a reason why each other option lost; a good accident in a lost option ("B's ears read as flames") is named so it can be kept.
- Show the sheet to the partner craft before the final round (the modeler on a character, the animator on a pose), while change is cheap.
- **Record the pick:** who chose, their words, the date. A direction is closed only by the owner's or requester's words, written in the job's closed-doors list; it comes back only with new words. When every option meets the brief, choose and commit; ties go to the owner with a recommendation.
- After the pick the big shapes are frozen: later rounds change parts, colour, light and finish, not the silhouette.

## 5. Iterate (R2) and final (R3) [PK3, FN1-FN15, HO1-HO4]
- **Iterate** only on the pick: each variant changes one named element ("A with C's lantern belly"); merges are stated in the prompt ("A's silhouette + C's belly"), never averaged. Colour is tried as 2-3 colourways, each a new full generation with only the colour words of the prompt changed and the pick attached as reference, each re-checked in grey; never an edit that repaints the colours (owner J018-D8). Light for key art and places whose key light the bible leaves open: 2-3 light set-ups of the pick (edits that change only where the light comes from), compared in grey at real size; where the lock fixes the light, there are no light variants.
- **Ask the next maker** what the final must contain, then deliver exactly that:

| Next maker | Final deliverable (each a separate image unless said) | Notes in the text record (never drawn) |
| --- | --- | --- |
| modeler (hand) | the look target (three-quarter); front, side, back and game-camera-angle views from the approved image; a flat-colour material-ID version; close-ups of identity anchors when asked | material intent per region with its local (unlit) colour; gaps and the choices made; placeholders (PROPOSAL) |
| modeler (Tripo) | one clean subject on the `model` lock (I-04) | — |
| character-rigger | the back and side views above | what holds each costume piece on; rigid or bending per region; costly parts (capes, long hair, chains) with the reason each earns its cost |
| animator | the key-pose sheet, exactly N poses, the character attached | the moment of each pose, the line of action, what the weight does |
| vfx-designer | key frames, exactly N, in time order (build, peak, result) | the primary, secondary and tertiary read; the core is the brightest |
| ui-ux-designer, marketing, film-director | per their own route (`ui-figma`, `marketing-craft`, `film-craft`) | — |

- **A new material** that carries the look gets one swatch image approved before the asset image.
- **Stop** when shapes, values, colours and the focal point are settled; a reference is a blueprint, not the product. Parts designed later stay abstract and are marked PROPOSAL in the record and listed as open items.
- **Finals at final size:** generate the final in the destination's aspect; never enlarge a small image.

## 6. Paint-overs: a review note as a picture [PO1-PO2]
- **Input:** the exact review capture (Studio MCP or render) at the game camera, as image 1. The identity names one change only and lists what stays: "Edit image 1. Change only the light on the path: make the path to the portal the lightest area and darken the frame edges. Keep the layout, camera, characters and every object exactly."
- **Solve the problem behind the note:** a note that names a solution ("delete the trees") becomes its problem first ("the background is busier than the path"); the paint-over shows a fix for the problem, and names what must not change (the identity anchor, the approved silhouette, the light direction).
- **One change per paint-over**, worst problem first; shown as a before-and-after pair at the same size; the maker builds toward the approved picture. A 3D change after review traces to a note or a paint-over.
- **Budget:** a marked capture (arrows, circles, no generation) is the default; a generated paint-over only for the 1-2 worst visual notes of a review, inside the brief's cap and with the batch yes (`art-review/references/feedback-briefs.md` §6).

## 7. Image budget (light checks; starting values, PROPOSAL; the brief's cap wins)
| Round | Generated | Measured | Looked at |
| --- | --- | --- | --- |
| R0 | 0 (a missing reference: at most 2) | — | the board |
| R1 | hooks 6-12 in text (0 images); warm-up 1 + roughs 3-5, at most 6 including regenerations | every rough (§4 C1-C3, C12, or C7) | one contact sheet; each rough whose number fails; the pick |
| R2 | at most 3 | every variant | the variants on one sheet |
| R3 | one per view or panel, at most 2 regenerations each | every final | each final once at full size (FN2), once at real size |
| Paint-over | 1-2 per review | the after image (grey) | before and after pair |
Report per batch: generated, regenerated, measured, looked at, and any `images: pending` batch.

## 8. Worked examples
**A. A starter pet for the fire world of a pet game (character, for the modeler).**
- R0: the brief of §1. Board: (a) the pet family anchors; (b) a puppy's hop, embers (a dark crust with glowing cracks), lantern glass, glassblowing (the outside source); disliked: a "flaming dog" stock image (fire hides the body). Keyword table: fire → orange and yellow, never the reserved enemy red; friendly → round body, big eyes; collectable → the family's proportions.
- R1 hooks (text): eight written (ember coal, candle wax, lantern glass, a salamander's skin, a forge bellows, a sparkler, a hot-water bottle, a pup made of flame); kept four against the sell list; the other four were cut with a line each (bellows and hot-water bottle: no "fire" read at 60 px; salamander skin: drifts to a lizard, not a pet; sparkler: a thin stick with no body).
- R1 images, `character` lock with the bible's anchors, highest quality (I-13), the lock's three-quarter view (no camera words: the game-camera read waits for R3): warm-up "a puppy on fire" (labelled); A ember-coal body (material); B candle pup with a wax head (what is it really?); C lantern-glass belly with a flame inside (craft); D radical: a flame shaped like a pup with no solid body. Black-fills at 60 px tall (C1, C2, C5): A and C share one outline (aligned IoU 0.9), so they are one shape direction with two material readings, labelled A and A2, not two options; B's tall wax head and D's flame outline are the other two directions. D's black-fill reads "a flame", not "a dog". Grey: in A2 the glowing belly is the lightest part; in A the tail is. B's cream wax head measured 1.1 against the light-grey backdrop (information only) and 3.9 on the on-ground copy over the fire world's dark rock (C12): it separates. Looked at: the real-size contact sheet and D's black-fill.
- Pick sheet: "Which reads as a friendly fire pet at 60 px?" Recommendation: A2, A's outline with the lantern belly (sell items 1-3; the belly reads at 60 px in grey); B lost (the wax head reads as a candle, not a pet); D lost (no pet read). The modeler looked at the sheet before R3 and asked whether the tail flame is geometry: it is an effect, so the final shows the tail stub and the record says "flame = VFX, intent only".
- R2: one variant, A2 with A's larger ears (one named change). R3 (high): look target, the `model` image for Tripo, a material-ID version; the back and game-camera views were blocked by the three-quarter lock, so the art director was asked for a view family (SKILL §5 I-04), and FN13 was checked on the modeler's blockout render at the game camera at the check-in (the pet read from behind and above: the tail stub and ears hold). Record: belly = glass, rigid; body = matte coal, its local colour from the image's mid-tone; ears bend (rigger). Counts: generated 9, regenerated 1, measured 9, looked at 7 (the real-size sheet, D's black-fill, the pick sheet, the 3 finals once at full size, one real-size sheet of the finals).

**B. "Players can't find the portal" in the hub (paint-over for the environment designer).**
The art director's capture shows the path darker than the market stalls. The note becomes a problem ("the path is not the lightest route to the portal") and one paint-over: image 1 the capture, change only the light on the path and the frame edges. In grey at phone size the path is now the lightest band and leads to the portal; the stalls, layout and camera are unchanged (before and after pair). One generation; the environment designer lights toward it.

**C. Key-pose options for a hammer strike (pose, for the animator).**
The approved smith is image 1. One `pose` row: exactly 3 options of the contact moment, left to right: A grounded and wide, B leaping down onto the anvil, C twisting with the hammer behind. C1 counts 3 components (one per pose); at the game-camera size each black-fill shows one clear line of action; B's centre of gravity sits outside the feet on purpose (a leap) and the brief says so; the heavy hammer stays close to the body in A and C. The animator picks A with B's raised shoulder; the final sheet is exactly 3 key poses of the clip (wind-up, contact, recovery).
