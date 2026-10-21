<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit template: copy to knowledge/design/art-bible.md in each game and fill in. Owner: the art director (with the game designer); the owner approves every lock. -->
# Art bible: <game>

> Status: **PROPOSAL** until the owner approves each lock (decision ledger ID per lock).
> The table and the fenced `text` blocks are machine-read by `tools/art/art_refs.py` (`reference-images` skill). Keep each block's first words as `<NAME> LOCK:` and keep exactly one copy of each lock.

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

## Locks
Write each lock as one paragraph of exact visual rules: shapes, proportions, materials, palette, lighting, background, camera, what never appears. Fill the `<...>` parts. The text after each placeholder is a working start, not a rule.

```text
WORLD STYLE LOCK: <the game's art style in exact words: rendering (e.g. stylized hand-painted, toy plastic, cel-shaded), shape language, proportions, material look, palette (named colours or hex), lighting>. No text, no logos, no watermark. Not resembling any existing franchise.
```

```text
CONCEPT LOCK: Key art for a game moment or place: <camera and framing>. Shows the player fantasy clearly in one image, with a readable focal point and scale against a player-sized character.
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
ICON LOCK: One object as a game icon, centred, plain flat background, clean silhouette readable at 48 px, <style words>. No text, no letters, no numbers, no border.
```

## Anchors
Approved images that steer every new generation live in `content/art/anchors/<folder>/`. The owner's own images have no prefix; images we generated and the owner approved get `gen-` (`art_refs.py approve`).
