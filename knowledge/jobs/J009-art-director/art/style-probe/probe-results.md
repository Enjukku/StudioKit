---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009 style probe (owner J009-D13), 8 images via tools/art/art_refs.py
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Style probe: why did the direction test look "fantasy"?

Same scene text in every image unless named; one thing changed per comparison. Images: `content/art/refs/concept/probe-*.png`; prompts: `bible-*.md`, `manifest-*.csv` here; sheets: `sheet-1.png`, `sheet-2.png`.

| Question | Compare | Result (lead's reading, not measured) |
| --- | --- | --- |
| Does the style text control the look? | stud, cartoon, anime, lowpoly, voxel, claytoy | Yes: six clearly different renderings (plastic blocks, outlined flat cartoon, cel-shaded anime, flat triangles, cubes, clay). The prompts are not stuck on one look |
| Does the subject drive "fantasy"? | stud (mountain, torches, spears, winged thieves) vs stud-modern (backyard, kiddie pool, hoodies, flashlights, hang-gliders) | Yes, strongly: same style, and the backyard version has no fantasy feel at all. Words like dragon egg, torches, spears, cloaks, storm mountain carry the genre into every style |
| Does "key art" wording push toward illustration? | test-A `dragonegg-b-nest` vs probe-b-screenshot (same style B lock, "in-game screenshot ... not an illustration") | Partly: smaller characters, wider play space, more game-like; still painterly because the B lock itself asks for sculpted painted planes |
| What stayed the same everywhere? | all 8 | The image model's night default: moonlit cloud sea, rim-lit cliffs, dramatic sky. "Night" alone brings this cinematic mood into every style |

**Why test A felt samey:** mostly the art director's choice. Both of its directions were the same family (premium painted stylized 3D with dramatic light), on a fantasy subject, under "key art" wording.

**Kit changes made:** exploration must span style families (`art-review/references/exploration.md` §3 step 0); game-camera images use "in-game screenshot" wording (template CONCEPT LOCK hint; exploration §4); keep genre words out of the subject unless the game's fantasy needs them, and name the mood of light explicitly so "night" does not default to cinematic drama (exploration §4).
