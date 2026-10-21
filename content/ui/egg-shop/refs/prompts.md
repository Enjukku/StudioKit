---
type: reference
scope: game
status: active
updated: 2026-10-20
source: "J002-T07; Figma MCP generate_image, model gpt-image-2.5-sunburst (owner J002-D4)"
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-20

# Egg shop: generated image log

Budget: 5 images max (brief J002-T07). Used: **5 of 5**. Route A (Figma MCP `generate_image`, owner's Figma AI credits). File `gVgO2Ql80LUerCpQe02CtD`, page `Refs`.
Shared style line (ui-figma image-generation.md §3, cartoon): `chunky cartoon game icon, thick dark outline, glossy highlight top-left, saturated colours, soft cel shading`.
Each egg was generated on a flat key colour that is absent from the egg, then keyed to alpha locally (Pillow, `key_eggs.py` logic: distance-to-key alpha 60..150, key colour unmixed from edge pixels), cropped square, saved 512 px and 256 px. Edge check: composited on #282828 at full size, no visible halo (looked at it).

| # | File (raw → kept) | Figma node | Requested / returned size | Prompt (verbatim) | Kept? |
| --- | --- | --- | --- | --- | --- |
| 1 | `raw/egg_meadow_raw.png` → `../export/egg_meadow.png`, `_256.png` | 2:2 (raw), 7:2 (keyed) | 1024² / 1024² | a single egg with a cream-white shell covered in soft rounded mint-green spots and a thin band of small leaves around its middle, meaning: the friendly starter nature egg, chunky cartoon game icon, thick dark outline, glossy highlight top-left, saturated colours, soft cel shading, centered, single object, plain flat #FF00FF magenta background, no text, no letters, no numbers, no border, no UI frame, no shadow on the background, 3/4 front view, soft studio light from top-left, clean silhouette readable at 48 px, original design | kept: reads as "starter / nature" at 48 px; no text |
| 2 | `raw/egg_ocean_raw.png` → `../export/egg_ocean.png` | 3:2, 7:3 | 1024² / 1024² | a single egg with a bright ocean-blue shell, white curling wave stripes and tiny round bubble dots, meaning: the water egg, (same style line and suffix as #1, magenta background) | kept |
| 3 | `raw/egg_lava_raw.png` → `../export/egg_lava.png` | 4:2, 7:4 | 1024² / 1024² | a single egg with a dark red-orange rocky shell split by glowing yellow-orange lava cracks, meaning: the hot fire egg, (style line), plain flat #00FFFF cyan background, no text, no letters, no numbers, no border, no UI frame, no glow on the background, no shadow on the background, 3/4 front view, soft studio light from top-left, clean silhouette readable at 48 px, original design | kept |
| 4 | `raw/egg_galaxy_raw.png` → `../export/egg_galaxy.png` | 5:2, 7:5 | 1024² / 1024² | a single egg with a deep purple and midnight-blue shell full of tiny white stars, small pink nebula clouds and one golden swirl band, meaning: the special cosmic egg, (style line), plain flat #00FF00 green background, (same suffix as #3) | kept: the gold band makes it read "special" next to the three coin eggs |
| 5 | `raw/backdrop_island_raw.png` (context only) | 6:2 | 2048×1152 / **1536×864** (model chose a smaller size) | third-person view of an original cartoon pet simulator game world, a sunny grassy floating island with rounded bubbly trees, flower patches, a small wooden market stall with an empty counter, a path of round stepping stones, bright blue sky with soft puffy clouds, saturated friendly colours, soft cel shading, wide 16:9 game screenshot, no characters, no people, no animals, no text, no letters, no logos, no user interface | kept as the blurred context background behind the screens (ui-figma step 2: never judge UI on white). Not UI, never exported |

Not done (budget): the 2-candidates-per-icon test from image-generation.md §4. One candidate per egg; each passed the 48 px and grayscale check in `screens/01-inspect-main-phone-grayscale.png` (four different silhouettes/patterns, no colour needed to tell them apart).
Rejected: none.
Originality: no named game, artist or franchise in any prompt. Generated images are data; none contained text.
