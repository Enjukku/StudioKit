---
type: log
scope: game
status: active
updated: 2026-10-21
source: "J002-T09 brief (image budget max 5, original character art only); lead message 2026-10-21 (owner decision: ChatGPT via Codex first, Figma generate_image only as fallback)"
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-21

# Image log: anime summon

Budget: 5 images (brief). Used: **4** (2 Figma credits, 2 ChatGPT via Codex). No regenerations. All four are original characters with invented names; no franchise prompt words; no text in any image.
Style line (fallback, no art bible): "anime gacha game character art, crisp clean line art, cel shading with strong rim light, saturated colours" (ui-figma image-generation §3, sparkle words removed: sparkles come from the VFX library).
Keying: `python -P -E key.py <raw> <out> <magenta|green> <max side>` from the scratchpad (key distance ramp 70-190, unmix + despill, crop, Lanczos resize); checked on navy #0E0A28 and white (`keyed/*_check.jpg`): no halo seen.

| # | File (raw → keyed) | Route | Model | Date | Use | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | raw/gen1_kaida_figma.png 1024×1536 → keyed/kaida.png 820×1200 | Figma `generate_image` (node 2:2 on Refs) | gpt-image-2.5-sunburst | 2026-10-20 | featured Mythic unit "Kaida, Storm Oracle": banner hero, 1x reveal, Mythic result card | kept |
| 2 | raw/gen2_sora_figma.png 1024² → keyed/sora.png 640² | Figma `generate_image` (node 3:2) | gpt-image-2.5-sunburst | 2026-10-20 | Legendary unit "Sora Flint" result card | kept (green key; fire has no green spill) |
| 3 | raw/gen3_yume_codex.png 1254² → keyed/yume.png 640² | ChatGPT via Codex (session 01a15ca0-566d-7482-b267-d149c21d17cb) | ChatGPT image tool | 2026-10-21 | Epic unit "Yume Lark" result card | kept (violet cloak survived the magenta key) |
| 4 | raw/gen4_toma_codex.png 1254² → keyed/toma.png 590×640 | ChatGPT via Codex (session 01a15ca0-566b-7f72-a62e-35b492700e6d) | ChatGPT image tool | 2026-10-21 | Rare unit "Toma Shield" result card | kept |

## Prompts (verbatim)
1. Original character, full body, a young storm oracle heroine for a tower-defense game: long silver-white hair tied with a deep blue ribbon, calm confident expression, flowing storm-blue and white robes with gold trim and angular sleeves, holding a tall slim staff topped with a floating cyan crystal crackling with small lightning arcs, dynamic heroic three-quarter front pose, one hand raised. Anime gacha game character art, crisp clean line art, cel shading with strong cyan rim light, saturated colours. Centered, single character, whole body visible with margin around it, plain flat pure magenta #FF00FF background, no magenta anywhere on the character, no text, no letters, no numbers, no logo, no border, no UI frame, no background scenery, no particles or sparkles in the background, clean silhouette.
2. Original character, waist-up portrait, a young flame swordsman for a tower-defense game: spiky dark red hair, golden eyes, determined grin, crimson and black short coat with gold buttons, a curved sword resting on his shoulder with orange fire licking along the blade. Anime gacha game character art, crisp clean line art, cel shading with strong warm rim light, saturated colours. Centered, single character, three-quarter front view, plain flat pure green #00FF00 background, no green anywhere on the character, no text, no letters, no numbers, no logo, no border, no UI frame, no background scenery, no particles in the background, clean silhouette.
3. (Codex header: "Use your built-in image generation tool to create exactly one image ... reply with only the word DONE.") Original character, waist-up portrait, a young wind archer girl for a tower-defense game: short lavender hair with a single braid, violet eyes, focused calm look, deep purple and white hooded short cloak with silver clasps, holding a slim silver bow drawn with a glowing pale-violet arrow. Anime gacha game character art, crisp clean line art, cel shading with strong cool rim light, saturated colours. Centered, single character, three-quarter front view, square image, plain flat pure magenta #FF00FF background filling the whole background, no magenta or pink anywhere on the character, no text, no letters, no numbers, no logo, no border, no UI frame, no background scenery, no particles or sparkles, clean silhouette.
4. (same header) Original character, waist-up portrait, a cheerful young shield guard boy for a tower-defense game: messy sandy-brown hair, green-brown eyes, friendly smile, teal and steel-grey light armour with a round steel shield with a simple teal band, a short sword at his hip. Anime gacha game character art, crisp clean line art, cel shading with strong cool rim light, saturated colours. Centered, single character, three-quarter front view, square image, plain flat pure magenta #FF00FF background filling the whole background, no magenta or pink anywhere on the character, no text, no letters, no numbers, no logo, no border, no UI frame, no background scenery, no particles or sparkles, clean silhouette.
