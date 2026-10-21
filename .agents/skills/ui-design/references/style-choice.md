---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "J002; tutorials TC/TS/TA/TP (knowledge/reference/ui/); research paper RP T12, case lessons (05a §1, 05b §5)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Picking a style and writing the visual thesis

## 1. The four style books
The game profile's UI style wins. When it is empty, propose one (PROPOSAL, owner decides).

| Style book | Reads as | Fits | Watch out |
| --- | --- | --- | --- |
| `ui-style-cartoon` | rounded, chunky, thick black outline, bright gradients, glossy highlights, bouncy (TC) | simulators, pets, tycoons, young audience, casual | everything equally loud; outline weight drift |
| `ui-style-stud` | Roblox toy bricks: stud texture, 3D blocks, role colours, hard shadows (TS) | obbies, tycoons, "classic Roblox", building games | stud texture noise behind text; tiny HUD buttons on phones |
| `ui-style-anime` | sharp angular headers, glow and shine, crystalline buttons, oversized character art, rarity gradients (TA) | anime TD, gacha, fighting, RPG | glow on everything kills hierarchy; borrowed franchise art |
| `ui-style-pixel` | dark translucent panels, 1-2 px hard lines, corner ornaments, fading edges, pixel font (TP) | rogue-likes, dungeon RPGs, retro | tiny text, low contrast on textured scenes, blurry scaling |

Mixing: one style per game. A second style is allowed only for a clearly separate context (e.g. a pixel mini-game), named in the game profile.

## 2. Visual thesis (C12-C14, O)
One sentence: *"<style> UI that feels <2-3 feelings>, where <the one thing players must always see> is loudest."* Then give each expressive device one job:
| Job | Example devices |
| --- | --- |
| identity | header silhouette, palette, font |
| grouping | panels, wells, dividers |
| selection | white outline, glow, scale |
| feedback | press depth, flash, count-up |
| warning | the reserved danger hue + icon |
| ornament | half-tones, studs, corner ornaments: never on the decision path |

## 3. Style spec (T12, O)
| System | Decide | Check on |
| --- | --- | --- |
| Shape | action vs selection vs passive panel vs warning vs ornament shapes | components active + inactive |
| Colour | semantic roles, contrast pairs, non-colour backup | real backgrounds, all states |
| Type | display vs utility font, sizes, glyph coverage, scaling | smallest phone, longest locale |
| Icons | meaning, silhouette, label needed?, smallest size | in context at real size |
| Depth + materials | light direction, lip depth, shadow, texture rules | one component family side by side |
| Layout | decision order, grouping, spacing scale, phone vs PC variants | task route per input |
| Motion | information beat, repeat, reduced alternative | normal + reduced recordings |
Project values stay PROPOSAL until the owner approves them; approved values go to the game's overlay.

## 4. What to learn from reference games (O, case lessons)
| Lesson | From |
| --- | --- |
| separate move / aim / special shapes; keep the screen centre for the game | Brawl Stars (C01-C03) |
| stable object identity across collection, battle, rewards; show the next goal, not a vague total | Clash Royale (C05-C07) |
| test icon meaning; put claimable state where players already look | Candy Crush (C04) |
| make it work in grey boxes before ornament | Monument Valley II (C08) |
| expressive frame, disciplined aligned data inside | Persona 5 (C12-C14) |
| timer-first status rows, priority channels, shape + colour | Destiny 2 (U05) |
| clean look must keep fast navigation | VALORANT (U06-U07) |
| group actions by player decision; reserve red for urgent | Fortnite (U02-U03, U26) |
| accessibility presets plus fine control, reachable at first launch | The Last of Us Part II (U04) |
Borrow the reason, never the art, density or business model (H02).
