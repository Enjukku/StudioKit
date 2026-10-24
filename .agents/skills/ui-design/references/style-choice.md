---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J002; tutorials TC/TS/TA/TP (knowledge/reference/ui/); research paper RP T12, case lessons (05a §1, 05b §5); J018 (UI thematic, rule sheet, value bands and colour)"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Revised by J018 maker ui-ux-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (thematic first, §4 structure study, §5 UI rule sheet, §6 value bands and colour).

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

## 2. Thematic and visual thesis (C12-C14, O; J018)
Start from the game's **UI thematic**: one line in the art bible naming a material or world motif the UI is made of ("carved jungle wood and gold coins", "a ship captain's charts and brass"). If the art bible has none, propose one to the art director before styling. The thematic chooses among the style books and sets the five rule groups of the rule sheet (§5); every visual decision answers to it, so the UI cannot belong to any other game.

Then one sentence: *"<style> UI that feels <2-3 feelings>, where <the one thing players must always see> is loudest."* Then give each expressive device one job:
| Job | Example devices |
| --- | --- |
| identity | header silhouette, palette, font, the game's motif |
| grouping | panels, wells, dividers, spacing |
| selection | white outline, glow, scale |
| feedback | press depth, flash, count-up |
| warning | the reserved danger hue + icon + text |
| ornament | half-tones, studs, corner ornaments: never on the decision path |
Set each style lever on purpose (saturation, how far shapes are pushed, how flat or rendered the panels are); a pushed cartoon button on a muted realistic panel sends a mixed tone.

## 3. Style spec (T12, O)
| System | Decide | Check on |
| --- | --- | --- |
| Shape | action vs selection vs passive panel vs warning vs ornament shapes; one corner type and shape vocabulary from the thematic | components active + inactive |
| Colour | semantic roles (from the art bible), contrast pairs, non-colour backup | real backgrounds, all states |
| Type | display vs utility font, sizes, glyph coverage, scaling | smallest phone, longest locale |
| Icons | meaning, silhouette, label needed?, smallest size; one icon family from one prompt style line | in context at real size, black fill |
| Depth + materials | light direction, lip depth, shadow, texture rules | one component family side by side |
| Layout | decision order, grouping, spacing scale, phone vs PC variants | task route per input |
| Motion | information beat, repeat, reduced alternative, the motion material | normal + reduced recordings, owner preview |

Project values stay PROPOSAL until the owner approves them; approved values go to the rule sheet (§5) and the game's overlay.

## 4. What to learn from reference games (O, case lessons; study method J018)
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
Borrow the reason, never the art, density or business model (H02). **Structure study** (SKILL §3 step 4): pick 2-3 working screens of the same job in the genre (the brief's references, or screenshots the owner sends; none given: ask the lead for 2-3, or capture them in Claude in Chrome and log each source; a study from memory is labelled not verified), trace each as a grey wireframe (where the decision, price, close, currency and back sit), note what they share (the genre's conventions) and what each does better; then change the traced structure toward our thematic. The final design differs visibly in style while keeping what the study taught.

## 5. The UI rule sheet (one per game; `content/ui/_system/rule-sheet.md`)
Everything that carries meaning on any screen is written here once; every screen follows it and new screens extend it. The art director signs the colour and shape rows; the owner approves the sheet.
| Group | Rows |
| --- | --- |
| Thematic | points to the art bible's §7 "UI thematic" row (never re-typed); the style book |
| Colour roles | the art bible's "Colour roles" and "Reserved colours" rows named by role (danger, reward, interactable, ally, disabled, decoration), never re-typed, so a bible edit reaches every screen; plus the UI-only roles (primary action, currency, rarity tiers, positive, negative) with hex, non-colour backup and never used for. One hue never carries two meanings; reserved gameplay hues never decorate |
| Text styles | display, header, button, body, number, small: font, size ladder, stroke ladder, where each is used |
| Screen zones | where each information type lives on every screen (critical state, currency, menu rail, close, toasts), drawn on the no-go overlay frame |
| Shape vocabulary | corner type, button shape by role, panel and header silhouettes, the game's motif and its sizes |
| Motion | the motion material from the art bible's §7 "Motion line" row; the motion table lives in `content/ui/_system/motion-table.md` (`motion.md` §7) |
| Exceptions | a format or event that may break a rule (a top-tier frame, an event reskin), with the owner's decision id. An event reskin changes one visible property of the brand header or logo (texture, colour or an ornament), never its font or the controls' places; its tone gets one pass pushed to the extreme and one pulled back to the brand, and the owner picks |

Check: sample the colours of every button and label in a set of screens with `look_check.py palette --roles` against the role swatches (`review.md` §6 S-19); the same information sits in the same zone on every screen.

## 6. Value bands and colour on the screen
- **UI owns the extremes, sparingly.** The game world sits in its middle value band; characters a little wider; UI and gameplay effects own the darkest darks and lightest lights. Spend pure white, near-black and the most saturated colour on the small focal spots only: one brightest element per screen region, glow on the primary action only. Over a bright or busy backdrop, a scrim or a dark panel gives the UI its range back.
- **Calm field, small pops.** Large panels sit lower in saturation; saturated colour goes on the focal control, the reward and the warning.
- **About 60 / 30 / 10** (PROPOSAL): a main colour on the big panels, a support colour on the medium parts, an accent on the small focal spots, after the grey pass works. New colours are taken from the palette already on screen.
- **Hue-shifted shading.** A gradient's dark stop moves toward a darker neighbouring hue (red toward purple, green toward teal, blue toward violet) and keeps its saturation; the light stop moves toward a lighter one (red toward orange); never darken with black or lighten with white. Gold stays saturated in its dark stop (warm orange-brown), never grey.
- **Group, then frame.** Detail inside a card stays in close values so the card reads as one object; the frame or face around it carries the contrasting colour. High-contrast small marks (badges, dots, studs, rivets) sit in deliberate groups with even spacing: packed too tight they shimmer at phone fit, a lone one far from its group steals the eye.
- **Overlaps.** A badge, icon or label over a same-hue face needs a value step or a stroke.
- **Check on the phone.** Colours shift on phones: judge the phone-fit view and, at the gate, the owner's phone; export sRGB.
