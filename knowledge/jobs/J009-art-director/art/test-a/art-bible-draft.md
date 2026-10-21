---
type: job
scope: game
status: draft
updated: 2026-10-21
source: "J009-T13 direction test; templates/skill/art-bible.md; test-a/direction-b-bible.md (explore-B rev 0); test-a/direction-packets.md"
supersedes: []
---
> Author: art-director · claude-opus-5-5 · high · 2026-10-21

<!-- Draft for the owner's pick in J009-T13. Not knowledge/design/art-bible.md: the game has no approved bible. Copy there only after the owner picks a direction and approves locks (decision ids below). -->
# Art bible: Guard the Dragon Egg (draft, direction B "Stormcut")

> Revision: **rev 0, 2026-10-21** (every review, manifest and brief names the revision it used).
> Status: **PROPOSAL** until the owner approves each lock and anchor (decision ledger ID per lock and anchor). No lock and no anchor here is approved.
> The families table and the fenced `text` blocks are machine-read by `tools/art/art_refs.py` (`reference-images` skill). Keep each block's first words as `<NAME> LOCK:` and keep exactly one copy of each lock. The direction-record sections after "Anchors" are for people and agents, not for the image model: never put their content inside a lock block.
> Changes from the exploration bible (explore-B rev 0), each from the test images: the egg shell carries no facet lines (try 2 kept faint facets); storm clouds are flat layered shapes (both tries drew soft volumes); faces are stylized in a few planes (the keeper drew a generic realistic face); thieves never share the keepers' hood-and-cape outline (try 2 thieves were hooded).

## Families
One row per kind of reference image. `world lock: yes` adds the WORLD STYLE LOCK to the prompt; flat 2D art (UI, icons, VFX sheets) usually says `no`. `anchors` names the anchor folder under `content/art/anchors/` (empty = the family name).

| family | lock | world lock | anchors |
| --- | --- | --- | --- |
| concept | CONCEPT LOCK | yes | |
| character | CHARACTER LOCK | yes | |
| creature | CREATURE LOCK | yes | character |
| model | MODEL REF LOCK | yes | character |
| prop | PROP LOCK | yes | |
| environment | ENVIRONMENT LOCK | yes | |
| pose | POSE SHEET LOCK | yes | character |
| vfx | VFX SHEET LOCK | no | |
| ui | UI LOCK | no | |
| icon | ICON LOCK | no | |
| thumbnail | THUMBNAIL LOCK | yes | marketing |
| game-icon | GAME ICON LOCK | yes | marketing |

## Locks

```text
WORLD STYLE LOCK: Stylized 3D game art with a chiselled, faceted look, like hand-carved and painted sculpture: every rock, cliff, garment, prop and creature is built from large, deliberate flat planes with crisp edges, and each plane carries a smooth, subtle colour gradient, never a noisy texture. Shape language: angular and tall, with wedges, diamonds and long diagonals; capes and scarves fly in sharp pointed shapes in the wind. The dragon egg is the one exception: it is the only perfectly smooth, curved form in the world, its shell has no facets, plates or plane lines at all, so it stands apart from every faceted shape. Materials: cut slate and granite, heavy cloth folded into planes, dark iron and bronze; the egg shell is like polished pearl with a molten gold heart glowing through it. Palette: deep indigo, slate blue and violet for the night and the stone; a cold white-cyan only for lightning; warm gold only for the egg's glow and the flames lit from it. Lighting: graphic and high contrast with two temperatures: warm gold light from the egg falls in hard-edged shapes on the front faces of the nest and the characters; cold cyan lightning and moonlight rim their back edges; shadows are deep indigo, never black. Value: the egg is the brightest shape in the image; characters read as strong dark silhouettes edged with light against lit stone; the sky is built from large, flat, layered storm-cloud shapes with crisp edges, not soft fluffy volumes. Sparse detail, with big calm areas of empty sky and bare stone. No text, no logos, no watermark, no user interface. Not resembling any existing franchise.
```

```text
CONCEPT LOCK: Key art of a game moment shown from the gameplay camera: a high three-quarter view looking down at about 45 degrees from behind and above the players, as in a third-person game camera, wide landscape frame. Shows the player fantasy clearly in one image, with one readable focal point in the middle of the frame and scale against player-sized characters. Composed like a real game screen, not a cinematic close-up: the whole play space around the focal point is visible.
```

```text
CHARACTER LOCK: Character concept. Every character shares one shape language: lean, upright, heroic proportions about five heads tall, long legs, a narrow waist, broad angular shoulders, a tall pointed hood, a long cape cut into sharp pointed tails; the clothing is folded into flat planes with crisp edges. Faces are stylized, not realistic: carved in a few simple planes like the rest of the world, calm and determined, with small features and no realistic skin detail. Full body, front three-quarter view, neutral standing pose unless a pose is named. Exactly one character; no turnaround, no extra views, no expression sheet. Plain light grey background, soft even studio light with a warm rim light on one side and a cool rim light on the other.
```

```text
CREATURE LOCK: Creature concept. Bold original silhouette, clearly separate body parts (head, neck, torso, each limb, wings, tail) so it can be rigged. Sky thieves and other storm creatures are built from faceted planes and never share the keepers' outline: no pointed hood, no long cape; they read by wide ragged wings and a masked face. A dragon hatched from the egg is the exception: it keeps the egg's smooth, curved forms and pearl-and-gold colouring. Neutral pose unless a pose is named. Plain light grey background.
```

```text
MODEL REF LOCK: Single reference image for modelling and image-to-3D (Tripo). Exactly one subject in one three-quarter view (about 40 degrees) so front, one side and anything on the back are visible, full body, centred, filling 85% of the frame. Characters in a clean T-pose or A-pose, hands open, nothing overlapping the body. No held props unless named, no extra views, no text. Plain light grey background, soft even lighting.
```

```text
PROP LOCK: One prop, weapon, tool or vehicle, three-quarter view, centred, readable as one silhouette at game distance, built from faceted planes with crisp edges. Plain light grey background.
```

```text
ENVIRONMENT LOCK: A building, landmark or environment piece at true scale against a player-sized character, high three-quarter view from the gameplay camera. Modular, readable large shapes: cliffs, ledges and walls are big faceted slabs with flat tops players can stand on; the drop beyond every edge is clearly darker than the walkable stone.
```

```text
POSE SHEET LOCK: Key-pose sheet for animation: the named character shown in the named key poses left to right (for example anticipation, contact, follow-through), same scale and camera for every pose, strong line of action, clear silhouettes. Plain light grey background. No motion blur, no text.
```

```text
VFX SHEET LOCK: Effect key frames for the named effect, left to right in time order (for example build-up, peak, dissipate), on a dark plain background, same scale per frame, flat 2D game-effect style built from sharp shard and wedge shapes with crisp edges; warm gold only for the egg and fire, cold white-cyan only for lightning and storm. No text.
```

```text
UI LOCK: One game UI element or screen mood in the game's UI style: carved slate panels cut in clean faceted shapes, thin warm gold edge highlights, deep indigo fills, front-facing, crisp. No real text: blocks or placeholder shapes only.
```

```text
ICON LOCK: One object as a game icon, centred, plain flat magenta #FF00FF background (for cut-out), clean silhouette readable at 48 px, faceted carved shapes with crisp plane edges and one strong rim light. No text, no letters, no numbers, no border.
```

```text
THUMBNAIL LOCK: Home-page thumbnail key art for the game: one real moment a player reaches in ordinary play, shown as one clear action by one hero subject and its visible consequence, from a slightly lower and closer camera than gameplay, the glowing egg or the keepers in the middle third. Wide landscape composition made for a 16:9 crop: the subject and the action sit inside the central area, nothing essential near the lower edge (Roblox metadata can cover it). The hero separates from the background by value as well as colour. Same characters, objects and places as the game; nothing the game does not have. No text, letters, numbers or logos (approved title text is added afterwards in an editor, never drawn by the image model). No user-interface elements, buttons, Robux or currency symbols, prices, reward labels, timers or system controls. No watermark.
```

```text
GAME ICON LOCK: Square game icon for the game: one hero subject or one symbol of the core action, large and centred, filling most of the frame, readable as one shape when shown at 150x150 px, the smooth glowing egg against faceted indigo stone and storm. Simple background in the game's palette, clearly lighter or darker than the subject. Same characters and objects as the game; nothing the game does not have. No text, letters or numbers (approved title text is added afterwards in an editor, never drawn by the image model). No user-interface elements, Robux or currency symbols, prices, reward labels, border or watermark.
```

## Anchors
Approved images that steer every new generation live in `content/art/anchors/<folder>/`. The owner's own images have no prefix; images we generated and the owner approved get `gen-` (`art_refs.py approve`).

| anchor id | file | purpose: what it controls | does not control | lighting / camera of the image | revision | decision id | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a01 (candidate) | `content/art/refs/concept/dragonegg-b-nest.png` | gameplay composition, two-temperature light, faceted ledge and nest, egg value rank | the egg's faint facet lines (lock wins: no facets), soft cloud volumes, the thieves' hooded design, torch design | night, egg key light + cyan rim; high 3/4 gameplay camera | 0 | none (needs owner) | proposed, not approved |
| — | `content/art/refs/character/dragonegg-b-keeper.png` | not proposed as an anchor: realistic generic face (graded C+); regenerate under rev 0 CHARACTER LOCK first | — | grey, 3/4 front | 0 | — | not proposed |

Status words: current, superseded (by which anchor, why), rejected (kept in `_rejected/` with its prompt record and reason). Anchors guide the whole look (shape, proportion, color, lighting, materials, rendering); where an anchor and a lock disagree, the lock wins (owner J009-D11). The `purpose` column says what the anchor was approved for, so reviewers know what to protect. Because an anchor carries its whole look, approve a01 only if the owner accepts its soft clouds and painterly finish being repeated.

---

# Direction record (read by every agent; not sent to the image model)

## Identity and intent
| Field | Value |
| --- | --- |
| Fantasy line | As a keeper, I guard a giant dragon egg on a storm-swept mountain through the nights so that it hatches into our own dragon, while sky thieves try to carry it away (J003 pitch-set.md §3) |
| Pillars (visual test per pillar) | PROPOSAL, no approved pillars yet. (1) The egg is the heart → the egg is the brightest and only smooth shape in every gameplay frame. (2) Small but brave → keepers are small dark silhouettes edged with light, in ready stances, between the egg and the dark. (3) Night is dangerous but readable → threats come from the cold side as winged shapes darker than the sky, never lit by the egg's gold. |
| World rule | PROPOSAL: the storm breaks everything into hard facets; only the egg, and the dragon that hatches from it, is whole and smooth. Every craft shows it: models (facets vs the smooth egg), VFX (shards for storm and hits, smooth curves for egg and hatch), UI (faceted panels, round egg meter), sound (hard, cracking storm vs a warm, round egg hum, sound-designer's call) |
| Emotional register | mythic defiance: tiny heroes holding a line around the one warm light against a vast cold storm; peak = the hatch, the first smooth living shape after the egg |
| Owner decisions | J009-D10 (concept), J009-D12 (test scope). No direction decision yet |

## Scope and camera
| Field | Value |
| --- | --- |
| Gameplay camera(s) | PROPOSAL: high three-quarter third-person, about 45 degrees down, Roblox default vertical FOV 70 (`_api-reference/classes/Camera.yaml:265-269`); distance not set (game-designer and engineering) |
| Capture states | normal gameplay distance at the nest; closest intended view (keeper over the shoulder); smallest presentation: phone landscape, compared at 1170x540 and 844x390 fit by height (vertical FOV kept) |
| Devices and quality floor | phone first (Roblox FY2025 mobile 83 % of DAU, platform-evolution-marketing.md §1.1); baseline phone and lowest quality not chosen: needs-decision with engineering |
| Orientations and input | landscape, touch first (assumed; Roblox default landscape) |
| Busiest supported scene | last night: storm at peak, all thieves attacking, every torch lit, effects on; not captured yet |

## Hierarchy per moment
| Moment | Must notice now | Read next | Atmosphere |
| --- | --- | --- | --- |
| Night defence | the egg and its state (glow, cracks); the nearest thief's approach | other keepers, torches, wall gaps | mountains, sky, lightning flashes |
| Day gathering | the resource being gathered; the path back to the nest (egg glow visible as a beacon) | other resources | sea of clouds, far peaks |
| Hatch | the egg cracking and the hatchling | keepers' reactions | the storm clearing |

## Color roles
| Role | Treatment (swatch, material, light) | Non-color backup | Never used for |
| --- | --- | --- | --- |
| life / egg (reward) | warm gold glow from inside pearl; the brightest value in frame | the only smooth curved form; warm hum (sound, PROPOSAL) | thieves, storm, decoration |
| danger (thieves, storm) | dark indigo-violet shapes, darker than the sky; lightning white-cyan edges | wide ragged wings, masks, wing-beat sound; never a hood and cape | the egg, keepers, friendly UI |
| interactable | gold-lit faceted edge on the near face (torches, walls, resource nodes) | one graspable feature (handle, socket) | background rock |
| ally / team (keepers) | dark slate cloth with gold front rim and cyan back rim | pointed hood and cape-tail outline | thieves |
| disabled | desaturated slate, no rim light | flat, unlit outline | any live state |
| decoration | slate, indigo, violet stone; low contrast | n/a | any role above |

Tolerance for palette drift (CIEDE2000 per role), if any: none set: diagnostics only.

## Lock notes (purpose, test, allowed variation)
| Lock | Purpose (what it protects) | Approved example | Failure example | Test | Allowed variation |
| --- | --- | --- | --- | --- | --- |
| WORLD STYLE LOCK | egg reads first by shape and value; one carved world | none (a01 candidate) | `_rejected/dragonegg-b-nest-try1.png` (faceted egg) | `look_check value` egg mask vs 8 px ring at the phone viewport; non-egg pixels at or above the egg median (`diag/competitors.py`); no facet lines on the egg in a crop | palette shifts by time (dusk, dawn after the hatch) as long as gold stays egg-only |
| CHARACTER LOCK | keeper identity: pointed hood and cape-tail outline | none | `dragonegg-b-keeper.png` face (realistic, generic) | `look_check silhouette`: hood point and cape tails survive at 96 px | cloth colour per player, gear add-ons inside the outline |
| CREATURE LOCK | thieves never read as keepers or as dragons | none | `_rejected/dragonegg-a-nest-try1.png` and `-b-nest-try1.png` (thieves drawn as dragons); `dragonegg-b-nest.png` (hooded thieves) | silhouette contact sheet keepers vs thieves at the gameplay camera | thief variants by night, inside the wing-and-mask outline |
| CONCEPT LOCK | comparable gameplay-camera images | a01 candidate | — | camera angle and egg in the middle third | — |

## Exceptions
| Exception | Why | Locks still protected | How it reads as intended | Decision id |
| --- | --- | --- | --- | --- |
| the hatchling is smooth | the world rule: what hatches inherits the egg's wholeness | silhouette separation from thieves | smooth pearl-gold forms against faceted storm | PROPOSAL, none |

## Cross-craft contracts (recurring events)
| Event | Importance rank | Model / pose | Motion | VFX | UI | Sound | Shared state name |
| --- | --- | --- | --- | --- | --- | --- | --- |
| thief grabs the egg | 1 | thief wings spread, egg lifted | wind-up readable at night on a phone (J003 record field 7) | dark shard trail, no gold | egg-state warning | PROPOSAL | `egg_grabbed` |
| egg cracks a step | 2 | one more crack on the smooth shell | short pulse | gold light leaking from the crack | egg meter step | PROPOSAL | `egg_crack_n` |
| hatch | 1 (peak) | smooth hatchling | first fire breath | the biggest gold effect in the game | — | the loudest moment | `hatched` |

## Technical envelope
| Item | Value | Evidence |
| --- | --- | --- |
| Lighting style and quality priority | not set; faceted flat planes need no fine texture to read (texture streaming may lower texture detail on phones, platform-evolution-marketing.md §1.3) | no capture yet |
| Post effects allowed | not set; the egg must read first without bloom (art-direction C-12) | no capture yet |
| Must survive at quality floor | egg smooth outline and value rank; keeper hood-and-cape silhouette; thief wing silhouette darker than the sky | no capture yet |
| Unresolved measurements | egg/ring value ratio tolerance; baseline phone; whether players appear as their own avatars or in a keeper body (changes CHARACTER LOCK scope) | owner + engineering |

## Change log
| Rev | Date | What changed | Why | Owner's words | Affected assets | Migration |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-10-21 | first draft from the J009-T13 direction test (direction B) | owner asked for 2 directions to pick from (J009-D12) | "Sure, you can run the small direction test" (J009-D12) | — | — |
