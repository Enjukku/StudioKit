---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J002-T09
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-21

# J002-T09 lessons: anime summon screen with the VFX library

| Field | Content |
| --- | --- |
| date | 2026-10-21 |
| job | J002-T09 |
| agent | ui-ux-designer |
| type | win + fail |
| what worked | L\* computed for every gradient before building (no faint faces); shine bars drawn 20 px past both edges and clipped by the face mask (no short shines); f 0.294 fixed before any size; tier odds and pity on the main screen, full list one labelled tap away and again in Review; frames cloned from the finished main frame; 420 px library thumbnails as stand-ins; local keying on magenta / green kept 4 character images clean. |
| what failed (found in self-review, fixed) | `createVector()` default dark stroke outlined every shine bar; scrim opacity still 1 after the documented bind-then-opacity step; cloned variants lost their TEXT / BOOLEAN property links; 150 px library stand-ins pixelated; 3 contrast failures on the banner and the disabled state; balance counter peeked over the odds panel; "SUMMONING…" overflowed its button. |
| library finding | 11 of the best A-quality anime runes / swirls have no alpha (grey on black): black squares in UI. Check alpha before picking. |
| owner corrections (word for word) | From the lead, owner decision: use ChatGPT through the Codex app for every image still needed; Figma `generate_image` only if ChatGPT fails ("the owner says ChatGPT's image model is better"). |
| evidence link | `content/ui/anime-summon/` (spec.md, library-picks.md, skill-gaps.md, screens/), Figma Ob2rRbGBRlmP5JmGyVOlUG |
| proposed home | effect-assets.md §2 (alpha check, 420 px stand-ins), figma-mcp.md §3 (vector strokes, opacity read-back, clone relink), ui-style-anime (gacha recipe), image-generation.md §1 (Codex route) |
