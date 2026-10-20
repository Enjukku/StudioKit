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

# Unknown__Hakari_Aura · ungraded · camera side, about 12 studs (character ~15% of screen height, centre; the effect fills the screen)
Event: a looping power-up aura: a white-cyan glowing disc with rings at the feet, a tall column of jagged green lightning shards above, and huge green brush-stroke ribbons and white streaks sweeping across the screen.
Phases: looping, no windup or end. Always at full intensity; coverage swings 20-40% frame to frame.
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
| 0 | 24 | whole screen | floor disc ~0.45 of screen width with ~4 thin concentric rings; jagged green shard column ~0.5 wide above it; 3 big green ribbons left; ~20 four-point sparkles and dots | #FFFFFF-#C0FFF0 disc, #20D060 shards, #60FF90 ribbons | bright_pct 2.3 | ribbons sweep, shards shimmer |
| 720 | 32 | whole screen | same, one ribbon crossing the whole screen, white streaks | #30E070, #FFFFFF | bright 6 | ribbons cross in ~0.3 s |
| 1428 | 25 | whole screen | column of shards, ~30 small dots, 3 sparkles | #20C060 | bright 2.6 | dots drift out |
| 1953 | 40 (peak 42 at 2072) | whole screen | big curved ribbon over the top, disc brighter | #50FF90, #FFFFFF | bright 7.5 | swoosh |
| 2489 | 33 | whole screen | ribbons on the left and right, disc bright, ~15 round white-green orbs | #40E080 | bright 3.2 | orbs float |
| 2853 | 31 | whole screen | as 0 ms | same | bright 4.1 | loop |
Layers seen: floor disc 1, rings ~4, shard column 1 (many small jagged pieces), big ribbons 3-4, white streaks ~6, orbs ~15, four-point sparkles ~6
Size vs character: column ~3 heights tall; disc ~3 character widths wide; ribbons up to a full screen width
What makes it look good:
- Clear base-column-ribbon structure, white core to green edge colour ramp.
- Ribbons have dark outline and lit inner stripe: anime style.
- Many layers move at different speeds, so no frame looks like another.
Weak points:
- Metrics unreliable: looping aura, parts sit in the median background; coverage 20-40% is a swing, not a build.
- Very busy; the character is small and hard to see, ribbons cover the view.
