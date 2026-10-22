---
name: ui-style-pixel
description: Roblox game UI in the pixel / retro rogue-like style in Figma - dark translucent panels, hard 1 px lines, corner ornaments, pixel font, integer scaling. Use when the UI style is pixel, retro, 8-bit, 16-bit, dungeon or rogue-like, or the owner says "pixel UI", "retro HUD", "old-school". Gives tokens, component recipes and the Roblox build. Read ui-design and ui-figma first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit skill: universal. J002. Main source: TP (Kakuza pixel rogue-like HUD, Photoshop, narrated to ~1:02:35; `knowledge/reference/ui/04-pixel-photoshop.md`). Owner decision J002-D5: pixel UI is made in Figma with the pixel grid. TP says Figma is weak for pixel art (no pencil, TP@5:51); this book covers the gap. Values are TP's by-eye picks or PROPOSALs. Revised by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (pulse rates, the transparency setting, measured self-check).

# Pixel UI

## 1. When this skill starts
The game profile (or the owner) picks pixel. Visual thesis default (PROPOSAL): *"Dark, restrained pixel UI that feels old-school and dangerous, where health, the hotbar and loot read instantly over the world."*

Before styling: make the screen's target reference image with ChatGPT and build to it (`ui-figma/references/image-generation.md` §2, owner J002-D12); effects from the VFX texture library (`ui-figma/references/effect-assets.md`).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Technique details (F-ids; F-17 mirrored ornaments, F-18 edge fades) | `ui-figma` SKILL.md §4 |
| Pixelated export, fonts, native vs baked | `ui-figma/references/roblox-handoff.md` |
| TP steps and values with timestamps | `knowledge/reference/ui/04-pixel-photoshop.md` |
| Pixel icons | `ui-figma/references/image-generation.md` (pixel style line; always redraw on the grid) |

## 3. The art-pixel rule (do this first)
A 1920 × 1080 design shrinks to ≈ 0.33-0.35 × on a small phone (ui-design screen-contract §5). TP's 1 canvas-px lines would fall below one device pixel and blur or vanish. So:
- Pick an **art scale** `S` = canvas px per art pixel. PROPOSAL: **S = 3** (one art pixel ≈ 0.9 pt on a small phone at f 0.294, 2-3 device pixels); S = 2 if the game is PC-first.
- Draw pixel parts (ornaments, icons, bar caps) as **components at 1 art px = 1 Figma px** in a small frame on the `Components` page, using 1 × 1 rectangles (or unioned rects) on integer positions. Owner turns on View → Pixel grid, Snap to pixel grid and Pixel preview (MCP cannot; figma-mcp §7).
- Place them on screens as instances **scaled by S** (Scale tool K by hand; `instance.rescale(S)` through the API), so every art pixel stays a crisp square block.
- Native lines (UIStroke, Frames) use multiples of S: 1 art px line = S canvas px; the 2 px outline = 2S.
- Export pixel art at **1 art px** and show it with `ResampleMode = Pixelated`; never smooth-scale it. Expect slightly uneven pixels when Roblox's fit scale is not an integer: check on a phone.

## 4. Tokens (in art px unless noted; ×S on the canvas)
| Token | Value | Source |
| --- | --- | --- |
| Light line | 1 art px, white or a pale tint | TP@5:46, @18:00 |
| Outline | 2 art px black around every drawn line, box and text | TP@7:36 |
| Panel | black at 60 % (frames), 50 % (containers, search, wells); players who set Background Transparency get more opaque panels (ui-figma handoff §1), so contrast is measured at these default values, the weakest case | TP@17:41, @26:48, @31:29 |
| Slot | white at 12 % (10-20 %); offset from the container edge: TP 14 canvas px → use 5 art px (15 canvas px at S 3) | TP@33:02-34:24 |
| Title bar | white 20 % with a 1 art px light outline; capitals | TP@22:01 |
| Shine | rotated white rectangles at 7 %, one masked to fade | TP@1:00:15 |
| Toolbar | 5 slots; gaps: TP 5 px → use 2 art px (6 canvas px at S 3); whole toolbar at 70 % | TP@13:06, @1:00:45 |
| Rows | leaderstats rows 4-5 canvas-px apart; bars 5-6 apart | TP@40:12, @50:42 |
| Bars | health red, mana blue, 1 art px outline + 2 art px black, light-to-dark gradient on top | TP@48:57-51:27 |
| Font | TP's Alagard is **not** in Roblox. PROPOSAL: **Press Start 2P** (Figma + Roblox built-in); it is wide, so use it for short labels and numbers at sizes that are multiples of 8 × S canvas px (24, 48 at S 3; PROPOSAL: the font is drawn on an 8-unit grid; TextLabel glyphs are anti-aliased, not Pixelated, so judge readability on the phone), and a clean sans in both Figma and Roblox (e.g. Roboto or Nunito) for long text if contrast or width fails | TP@27:36; handoff §2 |
| Text | white, 2 art px black outline (UIStroke), no depth shadow | TP@12:43 |
| Glow | Normal blend only, very soft, 10 % (TP: subtle in the editor, visible in Roblox) | TP@16:21-16:53 |

## 5. Component recipes
1. **Presentation board** (TP §2; not shipped): dark textured frame + vignette so the HUD is judged on darkness.
2. **Toolbar slot** (TP §4.1): square, black 60-70 % → 2 art px black outline → 1 art px light inner line with corner notches (mirrored component, F-17) → linear gradient overlay at 15 % → number label in a cleared corner. Five instances in auto layout. Backing strip: black bar with edge fades (F-18) at 50 % behind the row. **Active slot** gets a brighter line + 20 % white fill.
3. **Inventory frame** (TP §4.2): black 60 % → outline → corner-only ornaments, 4 mirrored instances (keep edges plain, TP@18:14) → title bar (white 20 %, 1 art px outline, caps title) with small fading marks at its ends → 2 shine rectangles 7 %.
4. **Search well** (TP §4.3): black 50 %, label 40-50 % opacity, a 1 art px divider line with fades at both ends.
5. **Slot grid** (TP §4.4): container black 50 %, padding equal on all sides (TP measured 23 px and fixed the bottom by 8 px: Alt-check, F-13), slots white 12 % in auto layout wrap, last row cut by the container to signal scrolling, plus a pixel scrollbar.
6. **Leaderstats list** (TP §4.5): top-right **below** Roblox's top-right buttons; strip fading left and down; rows = bold name + roleplay name, 20 % white row box fading left; pixel scrollbar at the right; two thin lines at the top (second shorter, 50 %).
7. **Party tab** (TP §4.6): circle portrait black 50 % with 1 art px ring + ornaments → coloured player icon (bevel: 1 art px light top-left, dark bottom-right) → name strip fading right → health bar and mana bar (1 art px outline, 2 art px black, gradient top, "100%" label) → recolour per player with colour variables.
8. **Close hint** (TP §4.7): faded strip + "CLOSE" + key hint; the hint shows the right glyph per input (keyboard key / gamepad button / a tappable × on touch) (TP gap).

## 6. States in pixel
| State | Look (PROPOSAL) |
| --- | --- |
| Hover / focus | light line goes full white + 1 art px outer white ring |
| Pressed | fill +10 %, content moves down 1 art px |
| Selected / active slot | 20 % white fill + bright line; equipped = small corner mark |
| Disabled / empty | lines at 40 %, no fill; empty slot keeps its frame |
| Low health | bar edge pulses at about 1 Hz with a small brightness swing, small area only (ui-design motion.md §8 pulse classes), **and** shows a number / icon (not colour only); players can turn the pulse off (RB-18); no pulse in reduced motion; flashing is checked over time, not from a still (ui-design review #16) |

## 7. Borrowed fundamentals
| From | Technique | Why |
| --- | --- | --- |
| TC / TS | components + variants instead of copy-paste layer styles | TP fixes seams by clearing and pasting styles; instances avoid it |
| TS | Alt-hover padding, spacing readout, auto layout | TP measures with Shift+arrow counts |
| TC | colour variables for per-player and per-rarity recolours | replaces hue/saturation passes |
| TA | white selection outline; rarity tier label | pixel slots need selection and rarity cues |
| ui-design | art-pixel scale + phone check | TP's 1 px lines do not survive phones |

## 8. Roblox build
| Part | Build |
| --- | --- |
| Panels, slots, title bar, rows | **N**: Frame + BackgroundTransparency (60 % → 0.4) + UIStroke (Thickness 2S, black); no UICorner |
| Light inner lines | **N** nested Frame with UIStroke S, or **B** with the ornament |
| Corner ornaments, icons, bar caps, scrollbar | **B**: PNG at 1 art px, `ResampleMode = Pixelated`; one image per corner flipped by rotation, or one 9-slice frame with the ornaments in the slice corners |
| Edge fades | **N**: UIGradient Transparency (0 → 1 at the ends) |
| Soft glows, shadows | **B** smooth image, UIShadow, or **L** a VFX library glow; **not** Pixelated |
| Pixel sparkles, flares | **L**: VFX library with `--style pixel` (`ui-figma/references/effect-assets.md`), Pixelated |
| Group 70 % | **N**: CanvasGroup GroupTransparency 0.3 (keep size static; it always clips, so pad it past the outermost stroke and glow); also fixes overlap alpha on fading rows (TP@40:57) |
| Text | **N**: TextLabel Press Start 2P (or the chosen font) + UIStroke 2S |

## 9. Pitfalls (TP gaps fixed here)
- 1 px lines on phones (§3). Half-pixel positions anti-alias: integers only.
- Contrast: 12 % white slots on 50 % black over a textured world can fail; measure on the weakest background.
- Tiny text: pixel fonts are hard to read small; check the text rubric on the smallest phone.
- Keyboard-only hints ("press G"): show per-input glyphs and a tappable control.
- No states in the video: §6.
- Overlay / multiply on the board do not ship (Normal only, TP@16:28).

## 10. Self-check
- [ ] Art scale S declared; every pixel part is an integer-placed component scaled by S.
- [ ] Exports at 1 art px with Pixelated noted; smooth parts not Pixelated.
- [ ] Phone-fit view (`look_check.py thumb`, S-23): lines crisp, text readable; contrast measured over the most textured backdrop at the default panel transparency (S-18).
- [ ] HUD clear of Roblox top-right buttons and default touch controls; tap targets pass the hit-target check (S-49).
- [ ] States in §6 for slots, rows and buttons.

Project overlay: if `knowledge/overlays/ui-style-pixel.md` exists, read it after this file; it wins for this game.
