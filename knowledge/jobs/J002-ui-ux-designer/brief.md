---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J002 intent brief — UI/UX designer agent

<intent>
The owner wants an agent that makes Roblox UI look like the best UI Genesis tutorials, in four styles, and that also has strong UX: the player always knows where they are, what they can do, what just happened and what to do next. Each style gets its own skill book, so an agent asked for "stud UI" reads one book and can do the whole job. The books share the best Figma technique from all four videos (the cartoon and stud videos teach Figma well; the anime and pixel videos teach style), so every book stands on strong fundamentals. The research paper gives the UX rules and the evidence discipline (no invented timings, test meaning before polish, every state specified).
</intent>

<spec>
id: J002
from: owner
to: lead
skills: [orchestration, ui-basics, platform-policy, ste-writing]
refs:
  - C:\Users\Firew\Downloads\Cartoon Guide.txt   # take: Figma basics, 3D layer, flatten outline, group mask, half-tones, selection colors; avoid: copying the sold file
  - C:\Users\Firew\Downloads\Stud Guide.txt      # take: tiled stud texture, overlay blend, scale tool, padding with Alt, copy fill, HUD layout; avoid: same
  - C:\Users\Firew\Downloads\Anime Guide.txt     # take: sharp header silhouette, glows, inverted text stroke, glowy = clickable, long-name space; avoid: copied renders from other games
  - C:\Users\Firew\Downloads\PixleArt Guide.txt  # take: 1 px line art, symmetry, corner-only ornament, motion-blur fades, dark presentation; avoid: Photoshop-only blend modes at runtime
  - C:\Users\Firew\Downloads\Game_UI_UX_Research_AI_Designer.txt  # take: decision record, attention inventory, state contracts, shop state machine, motion records, accessibility; avoid: treating OPINION as rule
fixed:
  default_tool: Figma   # owner 2026-10-20 "mainly going to make UI unless I say otherwise"
  one_book_per_style: true   # owner 2026-10-20
  cross_pollinate: true   # owner 2026-10-20
open: [book structure inside the agreed skill list, recipes, default values]
not_in_scope: [Roblox UI code, icon production, web research beyond fact checks]
rules:
  - Paraphrase sources; never copy transcript text; transcripts stay outside git.
  - Every number cites its source; values from one video are marked "single source".
  - Roblox has no blend modes, inner glow or layer styles for UI: mark every Figma effect native (UIStroke, UIGradient, UICorner, UIShadow) or baked (exported image).
  - Design numbers stay PROPOSAL until the owner confirms them.
  - Paid random items, prices and shops follow the platform-policy skill.
  - Skills ≤ 500 lines, kit template, project-overlay line.
deliver: knowledge/reference/ui/*, .agents/skills/<ui skills>/*, .agents/roles/ui-ux-designer.md
checks: see job-card.md acceptance checks
return: G1 to owner now; G2 first test screen; G3 approval
</spec>

## Proposed skill books
| Skill | Kind | Holds |
| --- | --- | --- |
| `ui-design` | design | UX: decision record, hierarchy and attention inventory, HUD contract, states, shops and purchase states, onboarding, motion contracts (no invented timings), accessibility, how to pick a style; read by other roles too |
| `ui-figma` | craft (shared) | Figma fundamentals from all four videos: canvas, frames, naming, groups, depth stack, flattened outline, group masks, blend modes, textures, padding check, copy styles, components and variants, export to Roblox (native vs baked, 9-slice, sizes) |
| `ui-style-cartoon` | craft (style) | Cartoon look, recipes per component, plus the fundamentals it needs inline |
| `ui-style-stud` | craft (style) | Stud look, same shape |
| `ui-style-anime` | craft (style) | Anime look, same shape |
| `ui-style-pixel` | craft (style) | Pixel look in Figma (pixel grid), same shape |
