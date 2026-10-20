---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: frame-script agent · claude-sonnet-5-5 · medium · 2026-10-20

# Unknown__Goal_VFX · ungraded · camera side, about 35 studs (no character; effect is a screen-sized UI-style burst in front of the camera)
Event: a goal celebration: a giant golden splash fills the screen, then the word GOAL appears in glowing orange block letters with sparks, then it dissolves.
Phases: idle 0-1150 ms · splash 1230-1450 · word hold 1450-2000 · letters melt 2000-2300 · empty after 2400
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0-1108 | 0 | - | empty | - | - | - |
| 1285 | 38.3 (peak 63 at 1228) | 0.26-0.94 x 0.01-0.78 | big liquid-shaped splash blobs with outlines, star-burst lines, white core | #FFFFFF, #FFE080, #E05020 centre | bright_pct 3-23 | explodes outward in 2-3 frames |
| 1468 | 60.4 | 0.10-1.0 x 0.01-1.0 | splash fills the screen, white-yellow shards and a curved arc on the left | #FFF0C0, #FFB040 | bright 11.6 | spreads past screen edges |
| 1658 | 31.7 | whole screen | splash shrinking, word GOAL appears blurry in the middle | #FFD080 | bright 3.9 | shards recede |
| 1835 | 18.6 | whole screen | blurry orange letters GOAL (~0.4 of screen wide), ~10 sparks and four-point stars around, 4 orange streaks | #FF8020 letters, #FFE080 sparks | bright 4.4 | sparks drift outward |
| 2185 | 14.1 | 0.32-0.85 x 0.01-0.86 | letters melt into dark-orange blobs, letter shapes lost | #8A3A20 | bright 0.5 | letters sink and blur |
| 2370 | 0.18 | 0.49-0.85 x 0.05-0.68 | 2-3 tiny dots | #BBC4C8 | none | gone |
Layers seen: splash blobs ~12, white core flash 1, streaks ~6, four-point star sparks ~8, text 1, glow haze 1
Size vs character: no character; the splash is larger than the screen, the text ~0.4 of screen width
What makes it look good:
- One huge near-white frame at the onset (bright_pct up to 23%) and then a sharp drop to a readable word: strong rhythm.
- Splash shapes are liquid and outlined (anime cartoon style), each with a white-hot centre.
- Sparks and streaks keep moving while the word holds.
Weak points:
- The word is blurry for most of its hold; it only reads sharply in the front view.
- At peak the splash covers the whole view; fine for a celebration, not for gameplay.
