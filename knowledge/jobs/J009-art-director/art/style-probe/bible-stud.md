---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009 style probe (J009-D13)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21
<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-20; direction-record sections added 2026-10-21 (J009); thumbnail and game-icon families added 2026-10-21 (J012). Kit template: copy to knowledge/design/art-bible.md in each game and fill in. Owner: the art director (with the game designer); the owner approves every lock and every anchor. How to write it: `art-review` skill, references/art-bible.md. -->
# Style probe bible: stud

> Revision: **rev 0, <date>** (every review, manifest and brief names the revision it used).
> Status: **PROPOSAL** until the owner approves each lock and anchor (decision ledger ID per lock and anchor).
> The families table and the fenced `text` blocks are machine-read by `tools/art/art_refs.py` (`reference-images` skill). Keep each block's first words as `<NAME> LOCK:` and keep exactly one copy of each lock. The direction-record sections after "Anchors" are for people and agents, not for the image model: never put their content inside a lock block.

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
Write each lock as one paragraph of exact visual rules: shapes, proportions, materials, palette, lighting, background, camera, what never appears. Fill the `<...>` parts. The text after each placeholder is a working start, not a rule.

```text
WORLD STYLE LOCK: Classic Roblox look: everything is built from simple plastic parts - blocks, wedges, cylinders and spheres - with smooth glossy plastic surfaces, bright saturated primary colours, blocky characters with cylindrical limbs and a simple painted smiley-style face, simple real-time game lighting with soft shadows. No painted textures, no realistic materials. No text, no logos, no watermark. Not resembling any existing franchise.
```

```text
CONCEPT LOCK: An in-game screenshot of a Roblox-style game, from the third-person gameplay camera: a high three-quarter view looking down at about 45 degrees from behind and above the players, wide landscape frame. Real-time game rendering, the whole play space around the focal point visible, one clear focal point in the middle. Not an illustration, not a painting, not a cinematic poster.
```

```text
CHARACTER LOCK: Character concept sheet. Every character shares one shape language: <shape rules>. Full body, front three-quarter view, neutral pose unless a pose is named. Plain light grey background.
```

```text
CREATURE LOCK: Creature concept. Bold original silhouette, clearly separate body parts (head, neck, torso, each limb, wings, tail) so it can be rigged. Neutral pose unless a pose is named. Plain light grey background.
```

```text
MODEL REF LOCK: Single reference image for modelling and image-to-3D (Tripo). Exactly one subject in one three-quarter view (about 40 degrees) so front, one side and anything on the back are visible, full body, centred, filling 85% of the frame. Characters in a clean T-pose or A-pose, hands open, nothing overlapping the body. No held props unless named, no extra views, no text. Plain light grey background, soft even lighting.
```

```text
PROP LOCK: One prop, weapon, tool or vehicle, three-quarter view, centred, readable as one silhouette at game distance. Plain light grey background.
```

```text
ENVIRONMENT LOCK: A building, landmark or environment piece at true scale against a player-sized character, <camera>. Modular, readable large shapes.
```

```text
POSE SHEET LOCK: Key-pose sheet for animation: the named character shown in the named key poses left to right (for example anticipation, contact, follow-through), same scale and camera for every pose, strong line of action, clear silhouettes. Plain light grey background. No motion blur, no text.
```

```text
VFX SHEET LOCK: Effect key frames for the named effect, left to right in time order (for example build-up, peak, dissipate), on a dark plain background, same scale per frame, flat 2D game-effect style <style words>. No text.
```

```text
UI LOCK: One game UI element or screen mood in the game's UI style <style words>, front-facing, crisp. No real text: blocks or placeholder shapes only.
```

```text
ICON LOCK: One object as a game icon, centred, plain flat magenta #FF00FF background (for cut-out), clean silhouette readable at 48 px, <style words>. No text, no letters, no numbers, no border.
```

```text
THUMBNAIL LOCK: Home-page thumbnail key art for the game: one real moment a player reaches in ordinary play, shown as one clear action by one hero subject and its visible consequence, <camera and framing>. Wide landscape composition made for a 16:9 crop: the subject and the action sit inside the central area, nothing essential near the lower edge (Roblox metadata can cover it). The hero separates from the background by value as well as colour. Same characters, objects and places as the game; nothing the game does not have. No text, letters, numbers or logos (approved title text is added afterwards in an editor, never drawn by the image model). No user-interface elements, buttons, Robux or currency symbols, prices, reward labels, timers or system controls. No watermark.
```

```text
GAME ICON LOCK: Square game icon for the game: one hero subject or one symbol of the core action, large and centred, filling most of the frame, readable as one shape when shown at 150x150 px, <style words>. Simple background in the game's palette, clearly lighter or darker than the subject. Same characters and objects as the game; nothing the game does not have. No text, letters or numbers (approved title text is added afterwards in an editor, never drawn by the image model). No user-interface elements, Robux or currency symbols, prices, reward labels, border or watermark.
```

## Anchors
Approved images that steer every new generation live in `content/art/anchors/<folder>/`. The owner's own images have no prefix; images we generated and the owner approved get `gen-` (`art_refs.py approve`).

| anchor id | file | purpose: what it controls | does not control | lighting / camera of the image | revision | decision id | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <a01> | `content/art/anchors/<folder>/<file>` | <shape and proportion of the hero> | <its palette, its light> | <neutral grey, 3/4 front> | 1 | <D-id> | current |

Status words: current, superseded (by which anchor, why), rejected (kept in `_rejected/` with its prompt record and reason). Anchors guide the whole look (shape, proportion, color, lighting, materials, rendering); where an anchor and a lock disagree, the lock wins (owner J009-D11). The `purpose` column says what the anchor was approved for, so reviewers know what to protect.

---

# Direction record (read by every agent; not sent to the image model)

## Identity and intent
| Field | Value |
| --- | --- |
| Fantasy line | <from the vision record> |
| Pillars (visual test per pillar) | <pillar → what the player must see> |
| World rule | <the one premise every craft must show> |
| Emotional register | <words + the moment that shows it> |
| Owner decisions | <D-ids that set this direction> |

## Scope and camera
| Field | Value |
| --- | --- |
| Gameplay camera(s) | <type, distance, FOV or ortho scale> |
| Capture states | normal gameplay distance; closest intended view; smallest presentation (<slot or viewport px>) |
| Devices and quality floor | <baseline phone, lowest supported quality> |
| Orientations and input | <landscape / portrait; touch, gamepad, keyboard> |
| Busiest supported scene | <encounter or crowd state used for reviews> |

## Hierarchy per moment
| Moment | Must notice now | Read next | Atmosphere |
| --- | --- | --- | --- |
| <moment> | <1-2 items> | <items> | <items> |

## Color roles
| Role | Treatment (swatch, material, light) | Non-color backup | Never used for |
| --- | --- | --- | --- |
| danger | <> | <shape / motion / sound> | <> |
| reward | <> | <> | <> |
| interactable | <> | <> | <> |
| ally / team | <> | <> | <> |
| disabled | <> | <> | <> |
| decoration | <> | n/a | <any role above> |

Tolerance for palette drift (CIEDE2000 per role), if any: <value + D-id, or "none set: diagnostics only">.

## Lock notes (purpose, test, allowed variation)
| Lock | Purpose (what it protects) | Approved example | Failure example | Test | Allowed variation |
| --- | --- | --- | --- | --- | --- |
| WORLD STYLE LOCK | <> | <anchor id> | <rejected id> | <look_check / review question> | <by biome, faction, rarity, event> |

## Exceptions
| Exception | Why | Locks still protected | How it reads as intended | Decision id |
| --- | --- | --- | --- | --- |

## Cross-craft contracts (recurring events)
| Event | Importance rank | Model / pose | Motion | VFX | UI | Sound | Shared state name |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Technical envelope
| Item | Value | Evidence |
| --- | --- | --- |
| Lighting style and quality priority | <> | <capture / doc> |
| Post effects allowed | <> | <> |
| Must survive at quality floor | <silhouettes, color roles, key values> | <capture> |
| Unresolved measurements | <> | <owner / engineering> |

## Change log
| Rev | Date | What changed | Why | Owner's words | Affected assets | Migration |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | <date> | first draft | <> | <> | — | — |
