---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J002; owner 2026-10-20 (J002-D7); content/vfx/library/catalog.json (7,906 tagged Roblox image ids from the VFX Studio plugin's public library); tools/vfx/vfxlib_catalog.py; vfx-craft references/plan-and-spec.md §E"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Effect textures for UI: use the shared VFX library before drawing

Owner decision J002-D7 (2026-10-20): "the VFX agent has access to this large pool of assets ... it would be incredibly useful for your workflow." Glows, sunbursts, sparkles, rings, shines, magic circles and pattern tiles already exist as uploaded, tagged Roblox images. Use them instead of drawing or generating new ones: they cost no upload, already look like the game's effects, and one id reused across UI and VFX is one texture in memory.

## 1. Which group for which UI job
| UI job | Catalog `group` / `shape` | Style books |
| --- | --- | --- |
| Sunburst behind an icon, reward or "featured" card | `Flare` / `burst-rays`; `Grid` / `burst-rays` | cartoon, stud, anime |
| Soft glow behind a button, item or rarity | `Flare` or `Spec` / `glow-round` | all (pixel: only soft glows, not Pixelated) |
| Sparkles and twinkles on rare items and rewards | `Flare` / `star-4`, `star-many`, `spark-dots`; `Star` / `star-4` | cartoon, anime |
| Ring pulse, selection halo, cooldown ring | `Circle` / `ring`, `ring-double`, `ring-broken`; `Swirl` / `ring` | all |
| Shine sweep band (moved by UIGradient or position) | `Beam` / `beam-strip`, `gradient` | cartoon, stud, anime |
| Magic circles and runes (anime frames, summon screens) | `Circle` / `rune`, `symbol`; `Form` / `rune`, `symbol` | anime |
| Swirl / vortex behind a summon or portal button | `Swirl` / `swirl`, `vortex`, `spiral` | anime |
| Energy wisps around legendary cards | `Energy` / `energy-wisp`, `aura-flame` | anime |
| Pattern / noise tiles (texture overlays) | `Grid` / `noise-tile` | cartoon, stud |
| Pixel sparkles and flares | any group with `--style pixel` (84 rows) | pixel |
Groups `Text` (glyphs) and `Impact` are VFX-only: never use library text glyphs as UI text.

## 2. Steps
1. Write what the effect must mean first (rarity, reward, ready, selected): ui-design D-14.
2. Shortlist: `python tools/vfx/vfxlib_catalog.py shortlist --group <G> --shape <shape> --style <anime|soft|realistic|pixel> --min-quality A --n 16` → a numbered pick sheet; open it with Read. Prefer quality A, then B; style `anime` or `soft` for cartoon / stud / anime UI, `pixel` for pixel UI. One style family per screen; **glows are exempt** (the catalog has no `anime` glow: Flare / Spec `glow-round` exist only as `soft`, e.g. SP-0129). `--shape` also matches related shapes (`ring` returns `ring-broken`, `rune`, …): read each row's real shape. On Windows run it as `python -X utf8 tools/vfx/vfxlib_catalog.py …` (cp1252 decode error otherwise). For a still UI image add `--grid 1` (rows with grid 2 / 4 / 8 are flipbook sheets, e.g. FL-0691). Tested 2026-10-20: `--group Flare --shape burst-rays --min-quality A` gives white, tintable sunbursts (FL-0532, FL-0091, FL-0021 anime; FL-0165 soft).
   - First run on a machine: `python tools/vfx/vfxlib_catalog.py fetch` downloads the 150 px thumbnails into `output/vfx/library/` (git-ignored; needs `output/vfx/library/` to exist).
3. **Alpha check (UI only).** Many A-quality runes, swirls and rings are grey on solid black with no alpha (11 of the J002-T09 anime picks). They work in additive particles; in a UI ImageLabel (Normal blend) they draw a **black square**, and the dark pick sheet hides it. Check every candidate before picking:
   `python -c "import sys; from PIL import Image; [print(p, Image.open(p).mode, Image.open(p).convert('RGBA').getchannel('A').getextrema()) for p in sys.argv[1:]]" output/vfx/library/thumbs/<id>.png …`
   Keep only rows with mode `LA` / `RGBA` and an alpha range that starts at 0.
4. Pick 1 main + 1 backup per use; record **catalog code + asset id** (e.g. `FL-0042`, `rbxassetid://<id>`) in the spec's layer table. Never invent an id.
5. **In Figma:** place the thumbnail (via `upload_assets`) as the stand-in layer, name the layer `fx/<catalog code>`, and mark it **L** (library) in the layer table. It is a placement and colour stand-in, not export art.
   - Size: the 150 px thumbnail (`output/vfx/library/thumbs/<id>.png`) pixelates above ≈ 300 canvas px. For bigger layers (summon circles, sunbursts: 600-1300 px) fetch the 420 px version: `python -X utf8 -c "import sys; sys.path.insert(0,'tools/vfx'); import vfxlib_catalog as v; v._fetch_thumbs(sys.argv[1:], 420, v.WORK/'thumbs420', {})" <id> <id> …` → `output/vfx/library/thumbs420/<id>.png` (stopgap until the catalog tool has its own command).
   - Tint: Figma cannot tint an image fill, so the stand-in shows white where the game shows `ImageColor3`. Either preview the tint (a group, bottom to top: a copy of the image with `isMask = true`, the image, a solid rectangle in the tint colour at Normal 60 %; the mask clips the colour to the texture's alpha) or write the intended tint per layer in the layer table and tell the owner the screenshot shows untinted textures.
6. **In Roblox (builder):** ImageLabel with `Image = rbxassetid://<id>`, `ImageColor3` to tint (tint multiplies: white or light textures recolour best), `ImageTransparency` for strength, `Rotation` for slow spins. Blend is Normal (no Add): glows rely on soft alpha, so check them on the real background. Flipbook sheets (`grid` 2 / 4 / 8): `ImageRectOffset` / `ImageRectSize` per frame.
7. Reuse: the same id for every sunburst / sparkle in the game; check the VFX shared set first (`vfx-craft` plan-and-spec §E.1).

## 3. Rules
- Library first; generate (image-generation.md) or draw only when no library texture fits, and say why in the spec.
- Effects stay behind content and never cover text, prices or the primary button; motion of these layers follows ui-design motion records (reduced motion: static or off).
- Many layers on always-on HUD cost (ui-basics U-11): ≤ 2 effect layers per HUD element, more only on short-lived reward screens.
- Licence: the library is the VFX Studio plugin's public community list (source data has a credits field; the catalog does not track licences). The VFX agent already uses it. Before a game ships, the owner confirms the library may be used there (one decision per game).
