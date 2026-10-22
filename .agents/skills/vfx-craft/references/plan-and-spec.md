> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20. Revised by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (frame-script read lines and stage names, spec fields for rank, mark, tier, viewer and reduced, the sound brief's verb and sync line, the shortlist output).

# Plan and spec formats: frame script, screen-size math, spec file, sound brief, texture picks

## A. Frame script (the written picture; replaces 2D mock-ups)
Same format as the pro frame scripts in `knowledge/reference/vfx/training/frame-scripts/`, so ours can be compared with theirs line by line. An option at the thumbnail stage (`vfx-design` §2 step 4) is the same format cut to three rows (build, peak, result) plus its hook line.
```
# <effect-id> · camera <game camera: distance, height, FOV> · tier <T1-T4>
Event: <one sentence in game words> · verb: <slows | stuns | knocks back | heals | collects | ...>
Read: shape <help or harm> · colour <role> · primary <the gameplay core and its focus point> · secondary <theme> · tertiary <few bits>
Phases: tell/build a-b ms · beat · peak (on <event id>) · result · tail; stage names as the timeline: load, charge, release, travel, impact, tail (only those present)
| ms | Stage / event id | Coverage % (target) | Where (box) | Shapes on screen | Colours (hex) | Brightness | Motion | Made by layers |
<6-10 rows: onset, build, beat, peak, just after peak, result, follow-through, tail, end>
Layers seen: <job: count>
Size vs character: <in character heights>
Per viewer: <self / other / threatened> · Reduced: <what each intense channel becomes>
References: <pro frame scripts used> · their peak coverage / peak ms / tail ms vs ours
Why it reads: <3 bullets>
```
Rules: the peak row names the 1-3 frames of the punch and sits on the contact event id; the build rows rise (size, brightness, density); result rows start after their cause (holds in 0.1-0.2 s steps); the gaps between main beats are not all equal; every row lists the layers that make it; coverage comes from §B math, not taste.

## B. Screen-size math (do it, do not guess)
Roblox `Camera.FieldOfView` is vertical, default 70° [api card]. At distance d studs the visible height is `H = 2·d·tan(FOV/2)` = **1.40·d** at 70°; the visible width is H × aspect (16:9 → **2.49·d**; phones are wider, height is the safe measure).
| Want | Formula | Example |
| --- | --- | --- |
| object height as % of screen height | `100 · S / (1.40·d)` | a 1-stud fireball head at 30 studs = 2.4% (too small to read); 4 studs = 9.5% |
| round object area as % of screen (16:9) | `22.5 · S² / d²` | an 18-stud blast (radius 9) at 50 studs = 2.9% of the screen; at 25 studs = 11.7% |
| size needed for a target height % | `S = p/100 · 1.40·d` | 12% of screen height at 30 studs → S = 5 studs |
Use the **game camera** distance from the effect (read the game's camera setup; the Roblox default third-person zoom is ~12.5 studs [inference, check the game]). For projectiles, check the size at launch distance and at impact distance. Pro clips: S-tier peaks reach 54-79% coverage in close/follow cameras, one-shot bursts 3-21% at side view, tails 2-10% (frame scripts).

## C. Spec file `spec.json` (effect as data; format v1, PROPOSAL until VfxPlayer exists)
```json
{
  "id": "VFX-WEAPON-FIREBALL", "version": 1, "type": "projectile",
  "duration_ms": 3300,
  "anchors": { "hand": "caster hand", "head": "moving projectile", "hit": "contact point", "ground": "hit point on floor" },
  "layers": [
    {
      "id": "L04", "job": "core", "rank": "primary", "semantic": true, "class": "ParticleEmitter", "anchor": "head",
      "texture": "rbxassetid://<id from catalog>", "catalog": "<catalog row id>",
      "fire": { "mode": "stream", "from_ms": 500, "to_ms": 1300, "rate": 30 },
      "props": { "Lifetime": [0.35, 0.35], "Speed": [0, 0], "Drag": 0, "Acceleration": [0, 0, 0],
                 "Brightness": 5, "LightEmission": 1, "LightInfluence": 0, "ZOffset": 0.1,
                 "Orientation": "FacingCamera", "Rotation": [0, 0], "RotSpeed": [0, 0],
                 "SpreadAngle": [0, 0], "LockedToPart": true, "EmissionDirection": "Top",
                 "FlipbookLayout": "None" },
      "size": { "curve": "size/linear shrink", "peak": 0.9 },
      "transparency": { "curve": "transparency/opaque hold" },
      "color": { "keys": [[0, "#FFF4D6"], [1, "#FF6A1F"]] },
      "squash": null,
      "tier_low": true,
      "others_ltm": 0,
      "why": "hot core inside the body (pro-defaults core row; C-03)"
    }
  ],
  "beams": [], "trails": [], "lights": [], "meshes": [],
  "root": { "anchor": "hand", "scale": 1.0 },
  "tier": "T3",
  "screen": { "shake": null, "hitstop": null, "flash": null },
  "reduced": { "flash": "steady shape", "shake": "none" },
  "sound_cues": "brief.md#sound",
  "frame_script": "frame-script.md"
}
```
- `rank`: `primary` (the gameplay core), `secondary` (theme) or `tertiary` (few supporting bits); `semantic`: true when the layer carries meaning (truth edge, telegraph, flash, team colour) and must never be randomised or dropped at a low tier; `others_ltm`: the LocalTransparencyModifier other players see (0 for threats, pickups and own effects); `root.scale`: the one factor every size and offset follows (C-27); `tier` and `reduced` from the read card.
- `fire.mode`: `burst` (`at_ms`, `count` → EmitCount/EmitDelay attributes) or `stream` (`from_ms`, `to_ms`, `rate`).
- Curves by library name (`<kind>/<name>` from `content/vfx/curves.json`), scaled by `peak`; or literal `keys` [[t, value, envelope], ...] with a reason in `why`. ≤20 keypoints, t from 0 to 1.
- Enum values by name (api card §3). Every property you leave out takes the Roblox default: say so if it matters.
- Meshes: `{ "mesh": "<ring|dome|crescent|...>", "material": "Neon", "tween": [{ "at_ms", "ms", "props", "easing" }] }` (`knowledge/reference/vfx/mesh-vfx.md`).
- Budget block at the end: unique textures, emitters, est. live particles at peak, lights, low-tier drops.

## D. Sound brief (say what is there; the sound designer chooses the sounds)
One row per visible beat: `ms | event id and stage name | what the player sees (shape, size on screen, speed, material, weight) | importance | how often it repeats | what it means in the game`. Head it with the verb (the same word as the timing list and the cue card) and the attempt/outcome split (what plays on input, what waits for confirmation). Mark the frame where picture and sound must hit together (the punch) and state the sync rule (one trigger for both; the window in `vfx-design` §4 Sound). A build that rises in the picture says so (the sound may rise with it). Never name a sound file or a sound type.

## E. Texture picks
1. **Shared set first:** textures already used by shipped effects (reuse = less phone memory, one look).
2. **Library:** `python tools/vfx/vfxlib_catalog.py shortlist --group <Flare|Impact|Smoke|Fire|Spec|Circle|Slashes|Swirl|...> --style anime --min-quality A --out output/vfx/<effect-id>/checks/<group>.jpg` → prints code, asset id, quality, style and shape per pick and writes a labelled sheet image (`--out` must end in an image extension such as `.jpg`; `.md` crashes; the sheet needs the thumbnails in `output/vfx/library/thumbs/`); open it with Read, pick 1 main + 1 backup per layer.
3. Check fit: one style family per effect (anime with at most a faint realistic underlay); glow textures need soft edges; impact textures must be solid (no holes); fire textures need internal contrast (TU-18, TU-30).
4. Flipbooks: 1024×1024, grid exact; OneShot for bursts, Loop for fire; static variety = Loop at framerate ~0.01 + StartRandom (TU-24).
5. Record per layer: catalog id, asset id, why it fits. Never invent an asset id.
