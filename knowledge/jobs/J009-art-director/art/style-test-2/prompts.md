---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009-T14 style test 2 (art_refs.py prompt records)
supersedes: []
---
> Author: art-director · claude-opus-5-5 · high · 2026-10-21

# Style test 2: exact prompts

STATUS: done. Coverage: 4 of 4 final prompts below (done); 3 rejected first tries listed with their reason (done). Everything here is a PROPOSAL for a kit test; nothing is approved.

**How consistency was kept (all four):** one identical 79-word identity (subject, action, the one key relationship "roaring up at a meteor ... behind it", 3 must-haves: T-rex focal, meteor trail brightest light, awe and danger) and one identical 49-word CONCEPT LOCK in every bible. Only the WORLD STYLE LOCK changes. No anchors (`anchors=none`), no input images, one new Codex session per image (art_refs.py, I-12). Left open on purpose: camera, placement, counts, the number of pterosaurs, background features and the exact light set-up (I-11).

| image | style family | words (whole prompt / PROMPT part / identity + concept + world) | bible | manifest | Codex session |
| --- | --- | --- | --- | --- | --- |
| `content/art/refs/concept/st2-clay-r1.png` | clay or vinyl toy | 293 / 254 / 79 + 49 + 126 | `bible-clay-r1.md` | `manifest-clay-r1.csv` | `01a15dc9-7cfa-73a0-82c6-debb9c1b132a` |
| `content/art/refs/concept/st2-anime-r1.png` | cel-shaded anime | 258 / 219 / 79 + 49 + 91 | `bible-anime.md` | `manifest-anime-r1.csv` | `01a15dc9-7cfa-7930-b4c4-9173017f32e4` |
| `content/art/refs/concept/st2-lowpoly-r1.png` | low-poly flat-shaded | 310 / 271 / 79 + 49 + 143 | `bible-lowpoly-r1.md` | `manifest-lowpoly-r1.csv` | `01a15dc9-7cfa-7152-bfe1-1789053bdaf6` |
| `content/art/refs/concept/st2-blocky.png` | Roblox-native blocky plastic | 283 / 244 / 79 + 49 + 116 | `bible-blocky.md` | `manifest-blocky.csv` | `01a15dc6-3588-7673-96da-65f7f8a8ec69` |

Word counts: whitespace-split words. "Whole prompt" includes the tool's fixed 39-word instruction line.

## st2-clay-r1: Clay stop-motion miniature

Consistency without over-constraint: Same identity and concept lock as the other three; the only style input is a materials-and-photography lock (what things are made of, how it is lit and shot). Retry 1 moved the fire, smoke and water into that lock as handmade props, but did not add layout, counts or camera words.

Assembled prompt (exactly as sent; identical to `art_refs.py --bible <bible> print <manifest>`):

```text
Use your built-in image generation tool to create exactly one image from the prompt below. Do not edit any files, do not run shell commands and do not write code. After generating, reply with only the word DONE.

PROMPT:
Concept scene for a prehistoric adventure game. A Tyrannosaurus charges through a shallow jungle river, roaring up at a huge meteor streaking across the dusk sky behind it; water bursts up around its legs and a flock of small pterosaurs scatters from the trees. The Tyrannosaurus is the focal point; the meteor's fiery trail is the brightest light in the image and washes the scene in warm orange. Feeling: awe and danger, the end of an age. No people.

CONCEPT LOCK: Concept art of a game world, wide landscape frame. One clear focal subject; a readable foreground, middle ground and background; the focal subject stands apart from its surroundings by value as well as colour. No text, no letters, no logos, no user interface, no border, no watermark.

WORLD STYLE LOCK: Handmade stop-motion clay miniature set, photographed for real. Every creature, plant and rock is sculpted from matte plasticine with visible thumbprints, tool marks and slightly uneven edges; chunky, simplified forms with soft rounded volumes; creatures have small glossy bead eyes. The meteor, its fire trail, the smoke, the water and the splash are handmade props on the set too: sculpted clay, twisted orange cellophane, cotton-wool smoke and clear resin droplets on wire; nothing in the frame is computer-generated or real fire or water. Real miniature photography: shallow depth of field, soft studio lights with gentle falloff, true scale of a tabletop set. Warm earthy palette of moss green, terracotta, ochre and cream, with deep teal shadows. Not resembling any existing franchise or studio.
```

## st2-anime-r1: Cel-shaded anime film frame

Consistency without over-constraint: Same identity and concept lock; the lock names line, cel shadow, painted background and effect shapes, but no composition. Retry 1 is the same prompt run again (the first try had an ambiguous third leg; no prompt cause was found, so no rule was added).

Assembled prompt (exactly as sent; identical to `art_refs.py --bible <bible> print <manifest>`):

```text
Use your built-in image generation tool to create exactly one image from the prompt below. Do not edit any files, do not run shell commands and do not write code. After generating, reply with only the word DONE.

PROMPT:
Concept scene for a prehistoric adventure game. A Tyrannosaurus charges through a shallow jungle river, roaring up at a huge meteor streaking across the dusk sky behind it; water bursts up around its legs and a flock of small pterosaurs scatters from the trees. The Tyrannosaurus is the focal point; the meteor's fiery trail is the brightest light in the image and washes the scene in warm orange. Feeling: awe and danger, the end of an age. No people.

CONCEPT LOCK: Concept art of a game world, wide landscape frame. One clear focal subject; a readable foreground, middle ground and background; the focal subject stands apart from its surroundings by value as well as colour. No text, no letters, no logos, no user interface, no border, no watermark.

WORLD STYLE LOCK: Hand-drawn cel-shaded anime film frame. Creatures are drawn with clean, confident line art of varying weight, flat cel colour with one hard-edged shadow tone and one crisp highlight. Backgrounds are lush hand-painted gouache with soft visible brushwork, layered depth and atmospheric haze; big sculpted cumulus clouds. Fire, spray and light are drawn as bold graphic shapes with sharp edges and glowing cores. Rich, natural palette: deep jungle greens, cobalt and violet sky, molten orange and gold light. Strong perspective, dynamic framing. Not resembling any existing franchise or studio.
```

## st2-lowpoly-r1: Low-poly flat-shaded

Consistency without over-constraint: Same identity and concept lock; the lock describes construction (facets, one colour per facet) and palette, not placement. Retry 1 only widened "everything" to name the background parts that came back painted, and said "never fine dust".

Assembled prompt (exactly as sent; identical to `art_refs.py --bible <bible> print <manifest>`):

```text
Use your built-in image generation tool to create exactly one image from the prompt below. Do not edit any files, do not run shell commands and do not write code. After generating, reply with only the word DONE.

PROMPT:
Concept scene for a prehistoric adventure game. A Tyrannosaurus charges through a shallow jungle river, roaring up at a huge meteor streaking across the dusk sky behind it; water bursts up around its legs and a flock of small pterosaurs scatters from the trees. The Tyrannosaurus is the focal point; the meteor's fiery trail is the brightest light in the image and washes the scene in warm orange. Feeling: awe and danger, the end of an age. No people.

CONCEPT LOCK: Concept art of a game world, wide landscape frame. One clear focal subject; a readable foreground, middle ground and background; the focal subject stands apart from its surroundings by value as well as colour. No text, no letters, no logos, no user interface, no border, no watermark.

WORLD STYLE LOCK: Low-poly 3D game art. Everything in the frame, including the distant jungle, mountains, waterfall, clouds, meteor trail and water spray, is built from a small number of large, clearly visible flat facets, with no painted or soft-brushed areas; each facet is one solid colour (flat shading, no smoothing, no textures). Creatures are faceted sculptures with a bold simplified silhouette; trees are simple faceted cones and clusters; water is faceted planes of cyan and teal; fire, spray and smoke are a few big faceted shards, never fine dust, the fire glowing. Clean real-time render with soft ambient occlusion and a smooth gradient sky. Limited, harmonious palette, two or three tones per object: emerald and sage greens, sand, slate, sunset orange, coral and deep indigo. Detail comes from light changing across the facets, never from surface texture. Not resembling any existing franchise.
```

## st2-blocky: Blocky plastic toy world

Consistency without over-constraint: Same identity and concept lock; the lock describes the parts kit (primitives, bevels, plastic sheen, no studs) and toy palette. First try kept; no retry.

Assembled prompt (exactly as sent; identical to `art_refs.py --bible <bible> print <manifest>`):

```text
Use your built-in image generation tool to create exactly one image from the prompt below. Do not edit any files, do not run shell commands and do not write code. After generating, reply with only the word DONE.

PROMPT:
Concept scene for a prehistoric adventure game. A Tyrannosaurus charges through a shallow jungle river, roaring up at a huge meteor streaking across the dusk sky behind it; water bursts up around its legs and a flock of small pterosaurs scatters from the trees. The Tyrannosaurus is the focal point; the meteor's fiery trail is the brightest light in the image and washes the scene in warm orange. Feeling: awe and danger, the end of an age. No people.

CONCEPT LOCK: Concept art of a game world, wide landscape frame. One clear focal subject; a readable foreground, middle ground and background; the focal subject stands apart from its surroundings by value as well as colour. No text, no letters, no logos, no user interface, no border, no watermark.

WORLD STYLE LOCK: Blocky 3D game world made of smooth plastic parts. Every creature, tree and rock is assembled from a few chunky primitives (blocks, wedges, cylinders, balls) with slightly bevelled edges and a soft glossy plastic sheen; no studs, no brick seams. Creatures are toy figures with a big blocky head, simple solid eyes and sturdy limbs. Water is smooth translucent blue slabs with white blocky splash parts; fire is glowing orange neon blocks. Bright, saturated toy palette: grass green, sky blue, sunny yellow, bright orange, tomato red, with clean colour breaks between parts. Real-time game render: soft shadows, gentle bloom on bright lights, crisp readable shapes. Not resembling any existing franchise or toy brand.
```

## Rejected first tries (kept in `content/art/refs/concept/_rejected/` with their prompt records)

| file | words (whole / PROMPT part) | reason (exploration.md §5 check failed) | what changed for retry 1 |
| --- | --- | --- | --- |
| `st2-clay-try1.png` | 267 / 228 | Matches the lock: fails. Creature is clay, but the fire, smoke and splash are photoreal CG; the image reads as a clay filter on a CG scene | lock sentence on fire, smoke and water rewritten as handmade props on the set (+26 words) |
| `st2-anime-try1.png` | 258 / 219 | Construction: fails. A third leg-like mass sits under the belly between the two legs (crop of x 500-550, y 585-685) | none: same prompt run again |
| `st2-lowpoly-try1.png` | 285 / 246 | Matches the lock: fails. T-rex and rocks are faceted; jungle, waterfall and mountains are soft painted, and the spray breaks up into fine dust at the feet | "everything" widened to name the background parts; spray "a few big faceted shards, never fine dust" (+25 words) |
