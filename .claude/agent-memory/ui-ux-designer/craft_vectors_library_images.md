---
name: craft-vectors-library-images
description: Figma vector/opacity/clone pitfalls, VFX library alpha + 420 px stand-ins, and the ChatGPT-via-Codex image route (J002-T09 anime summon)
metadata:
  type: feedback
---

- `figma.createVector()` can render with a dark stroke: set `strokes = []` right after creating it, or shine bars read as outlined lines.
- Scrim opacity: after `setBoundVariableForPaint`, assigning `{...paint, opacity}` at creation still gave opacity 1; reassign `fills=[{...node.fills[0], opacity}]` on the existing node and read it back.
- Cloning a variant inside a set (to add an axis) drops `componentPropertyReferences`; relink TEXT/BOOLEAN after clone.
- A thrown `use_figma` script rolls back fully; re-read, then rerun the whole script.
- VFX library: check thumbnail alpha (`mode L`/`RGB` = grey on black = black square in UI). Use 420 px thumbnails (`vfxlib_catalog._fetch_thumbs(ids, 420, folder, {})`) for stand-ins over ~300 canvas px. No anime glow exists; glows are `soft` (SP-0129).
- Contrast: sample the real rendered background in the text column (Pillow on the screenshot), not the gradient stops; rune textures and sparkles behind text lowered it to 2.8.
- Gradient check before building: compute L* of both stops (≥ 20); shine bars 20 px past both edges, clipped only by the face mask.

**Why:** each of these produced a visible defect in the second test (J002-T09) before self-review caught it; owner flagged faint gradients and short shines in G2.
**How to apply:** any Figma build with depth blocks, popups over scrims, variant sets, or library effects. Images: owner decision 2026-10-21 (via lead) — use ChatGPT through Codex (`codex.exe exec -C <empty dir> --skip-git-repo-check -s read-only - < prompt`, image in `~/.codex/generated_images/<session id>/`), Figma `generate_image` only as fallback; magenta key for glowing / violet-free subjects.
