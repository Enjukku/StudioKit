---
type: reference
scope: game
status: proposed
updated: 2026-10-21
source: "J002-T09; content/vfx/library/catalog.json; tools/vfx/vfxlib_catalog.py shortlist; thumbnail alpha check (Pillow) 2026-10-21"
supersedes: []
---
> Author: ui-ux-designer · claude-opus-5-5 · high · 2026-10-21

# VFX library picks: anime summon

8 library textures are used (check C3 needs 4). All are **L** layers: in Roblox an ImageLabel with `Image = rbxassetid://<id>`, tint with `ImageColor3`, strength with `ImageTransparency`, Normal blend. In Figma each one is a rectangle named `fx/<code> (...)` with the Roblox thumbnail as a stand-in. I first placed the 150 px thumbnails (brief rule). At 700-1300 px on the canvas they showed hard pixel steps, so I swapped them for the **420 px** thumbnails, from the same Roblox thumbnails API that the catalog tool uses (`vfxlib_catalog._fetch_thumbs(ids, 420, ...)`). Both sets are on the Refs page (`figma-ids.json`). Neither is export art: the builder uses the asset id.

## 1. Picks
| Use (meaning) | Code | Asset id | Where | Opacity / tint (PROPOSAL) | Backup | Why this one |
| --- | --- | --- | --- | --- | --- | --- |
| Summon circle behind the hero (this banner is a summoning) | CI-0225 | rbxassetid://16878107410 | Banner card (10:112), reveal 1x, 10x summary (faint) | 0.55 on banner, 0.5 reveal, 0.10 summary; tint #C9C3F5 | CI-0173 | Detailed ritual circle; has alpha. Reads as "summon" with no text glyphs. Kept out of the text column (banner x ≤ 590) |
| Faint rune in the backdrop (place mood, not information) | CI-0173 | rbxassetid://14197282370 | Frame 01 backdrop | 0.10 | CI-0056 | Simpler star circle; it stays quiet behind content |
| Swirl behind the rune (energy, slow spin) | SW-0160 | rbxassetid://86401376598665 | Banner card, reveal 1x | 0.28 / 0.20; tint #9CF4FF | SW-0137 | Thick brush ring, alpha, empty centre, so the hero stays clean |
| Sparkles around the hero (rarity sparkle, decoration) | FL-0227 | rbxassetid://13908198788 | Banner card (3), reveal 1x (3) | 0.75-0.95; white | FL-0030 | Slender 4-point star, crisp at 44-130 px |
| Big sparkles (accents) | FL-0269 | rbxassetid://15452013947 | Banner card (2), reveal 1x (2) | 0.8-0.9; white | FL-0263 | Solid sharp 4-point; a second shape so the sparkles are not identical copies |
| Soft glow behind the hero and the Mythic / Legendary card art | SP-0129 | rbxassetid://9841273544 | Banner card, reveal 1x, Unit card (Mythic, Legendary only) | 0.7-0.8; tint rarity top colour | SP-0017 | Round glow with a strong core. Only `soft` style has glows (no anime glow-round A or B in the catalog) |
| Sunburst behind the confirmed reveal | FL-0532 | rbxassetid://79369083399182 | Reveal 1x (0.22), 10x summary behind the Mythic card (0.25) | slow spin; tint #FFE58A | FL-0091 | White wedge sunburst; alpha; tested in effect-assets §2 |
| Clipped ring texture in the info panel (TA "unusual texture clipped into the shape") | CI-0065 | rbxassetid://12362738407 | Frame 01 info panel (masked by the panel; it crosses the panel edge) | 0.14 | CI-0585 | Radial tick ring: tech-like texture, alpha, quiet at 14 % |

The builder needs the id only. The same ids should be reused by the VFX agent for the 3D summon effect, so they are one texture in memory (effect-assets §2 step 6).

## 2. Considered and rejected
| Code | Reason |
| --- | --- |
| CI-0099, CI-0097, CI-0096, CI-0564, CI-0538, SW-0024, SW-0153, SW-0217, SW-0136, FL-0334, CI-0633 | **No alpha channel**: the thumbnail is grey or RGB on solid black (`mode L` or `RGB`, alpha 255 everywhere). In a particle with LightEmission the black disappears. In a UI ImageLabel (Normal blend) it shows as a **black square**. Not usable for UI without a re-upload |
| CI-0168, CI-0002, CI-0014 | Circles with letter-like glyphs in the ring. They are decorative, but they come too close to "library glyphs as UI text" (brief avoid list). CI-0225 has smaller symbols |
| SW-0016, SW-0236, SW-0097 | Bright core in the centre. It would sit behind the hero's face |
| EN-0136, EN-0215, EN-0057 (energy wisps) | Planned for the Legendary / Mythic cards. Not used: 10 cards with wisps break the "glow only where it matters" rule. A candidate for the reveal motion instead (VFX agent) |
| FL-0648 | Thin rays; alpha max 104, so it is too faint on a dark panel |
| Any `Text` group row | Brief and effect-assets §1: never as UI text |

## 3. Shortlist commands run (2026-10-21)
```
python tools/vfx/vfxlib_catalog.py shortlist --group Circle --shape rune  --style anime --min-quality A --grid 1 --n 16 --out content/ui/anime-summon/refs/shortlists/Circle-rune.png
python tools/vfx/vfxlib_catalog.py shortlist --group Form   --shape rune  --style anime --min-quality A --grid 1 --n 16   # no match
python tools/vfx/vfxlib_catalog.py shortlist --group Form   --shape rune  --style anime --min-quality B --grid 1 --n 12 --out .../Form-rune-anime-B.png   # zodiac glyphs, rejected
python tools/vfx/vfxlib_catalog.py shortlist --group Swirl  --shape swirl --style anime --min-quality A --grid 1 --n 16 --out .../Swirl-swirl.png
python tools/vfx/vfxlib_catalog.py shortlist --group Swirl  --shape vortex --style anime --min-quality A --grid 1 --n 16 --out .../Swirl-vortex.png
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape star-4 --style anime --min-quality A --grid 1 --n 16 --out .../Flare-star-4.png
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape star-many --style anime --min-quality A --grid 1 --n 16 --out .../Flare-star-many.png
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape burst-rays --style anime --min-quality A --grid 1 --n 16 --out .../Flare-burst-rays.png
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape glow-round --style anime --min-quality A --grid 1   # no match
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape glow-round --style soft  --min-quality A --grid 1   # no match
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape glow-round --min-quality A --grid 1 --out .../Flare-glow-any.png   # 2 lens flares, rejected
python tools/vfx/vfxlib_catalog.py shortlist --group Spec   --shape glow-round --style soft  --min-quality A --grid 1 --n 12 --out .../Spec-glow-round-soft.png
python tools/vfx/vfxlib_catalog.py shortlist --group Energy --shape energy-wisp --style anime --min-quality B --grid 1   # no match
python tools/vfx/vfxlib_catalog.py shortlist --group Energy --shape energy-wisp --min-quality B --grid 1 --n 12 --out .../Energy-wisp-any-B.png
python tools/vfx/vfxlib_catalog.py shortlist --group Flare  --shape spark-dots --style anime --min-quality A --grid 1   # no match (also without --style)
python tools/vfx/vfxlib_catalog.py shortlist --group Circle --shape ring  --style anime --min-quality A --grid 1 --n 16 --out .../Circle-ring.png   # shape is a substring match: also returned ring-broken, ring-double
python tools/vfx/vfxlib_catalog.py shortlist --group Beam   --shape beam-strip --style anime --min-quality A --grid 1 --n 16 --out .../Beam-beam-strip.png   # not used: no shine sweep in a still
```
On Windows, run with `PYTHONIOENCODING=utf-8 python -X utf8` (the catalog JSON has non-cp1252 characters). Alpha check: the snippet in `skill-gaps.md` G-03. Pick sheets: `refs/shortlists/*.png`.

## 4. Owner action
Effect-assets §3: before the game ships, the owner confirms that the community library may be used in this game (one decision per game).
