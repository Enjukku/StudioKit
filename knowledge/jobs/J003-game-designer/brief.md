---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent game-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J003 intent brief — game-designer agent

<intent>
The owner wants a game designer that starts games, not only one that checks them. Its first job is the pitch: a bold, marketable fantasy a player reads in the title and thinks "I need to do that" or "what would happen if I did that?". It gets there by taking a proven, trending Roblox loop and giving it a new theme and a twist, then shows the owner 3 pitches with 1 recommendation. After the owner picks, it leads pre-production with the owner, step by step (fantasy, style direction, key characters and moments, world, core loop, features, content), and pulls in the art director, architect, marketing, trend scout and craft leads from the start so the game is cohesive and well built. It then writes the decided game as documents every agent can build from, exact where exact matters, craft left open. Last, it reviews designs, loops, systems and level plans early and proposes ranked fixes. The owner is the creative director and usually knows what is fun on Roblox: the agent proposes, the owner decides.

The two research papers are strong evidence but not gospel. Numbers and Roblox facts get checked; what cannot be backed up is dropped or kept only as OPINION. The earlier DestructionSimulator designer gives tested review checklists; keep what is game-agnostic.
</intent>

<spec>
id: J003
from: owner
to: lead
skills: [orchestration, ste-writing, platform-policy, analytics, ui-design, architecture]
refs:
  - C:\Users\Firew\Downloads\Game_Designer_Part_1_Research.txt   # take: ideation method, hook test, 18 cases, pillars, preproduction reviews, feature spec, tuning table, per-craft briefs, pitch template, creative-director rules; avoid: AI-paper numbers as studio targets
  - C:\Users\Firew\Downloads\Game_Designer_Part_2_Research.txt   # take: loop scales and coupling, principles as tests, systems and economy checks, level review, social design, playtest record, finding template, fix ranking, live content; avoid: retention or session numbers as targets
  - ..\DestructionSimulator\.agents\skills\game-design\SKILL.md   # take: four parts, name the fun, goals vs tactics, mechanics carry theme, fairness, luck vs skill, scored review; avoid: §9 project parts
  - ..\DestructionSimulator\.agents\skills\level-design\SKILL.md  # take: level job card, guidance, pacing, walk times, boundaries, 20-point review; avoid: §8 project parts, destruction specifics
  - ..\DestructionSimulator\.claude\agents\game-designer.md       # take: work method, evidence per finding, marked-up maps; avoid: "never pitches" stance (the new role leads concepts)
fixed:
  role_name: game-designer                 # owner 2026-10-20
  tier: craft → opus, effort high          # roster .agents/roles/README.md
  pitch_count: 3 pitches + 1 recommendation  # owner "one clear recommendation"; paper Part 1 rule 15
  concept_formula: proven trending loop + new theme + twist, fantasy first   # owner 2026-10-20
  messages_format: rules/messages.md        # owner 2026-10-20
  new_roster_rows: [trend-scout (planned), marketing (planned)]   # owner 2026-10-20
open: [book structure inside the skill list below, recipes, templates, rubric wording]
not_in_scope: [game code, building trend-scout or marketing, market data pulls, editing other skills beyond pointers]
rules:
  - Paraphrase sources; never copy paper text; the papers stay outside git.
  - Every number and Roblox fact cites its source and its fact-check verdict; unverifiable claims are dropped or marked OPINION.
  - Keep evidence tags; never invent retention, session, price or conversion targets.
  - Design numbers, names and content stay PROPOSAL until the owner confirms.
  - Anything players buy, roll or trade follows platform-policy; funnels and quit points follow analytics.
  - No DestructionSimulator specifics in kit files.
  - Skills ≤ 500 lines, kit template, project-overlay line.
deliver: knowledge/reference/game-design/*, .agents/skills/<4 skills>/*, .agents/roles/game-designer.md, roster rows, evals
checks: see job-card.md acceptance checks
return: G1 to owner now; G2 first real test; G3 approval
</spec>

## Proposed skill books
| Skill | Kind | Holds | Read by |
| --- | --- | --- | --- |
| `game-concept` | design | Making ideas: fantasy first (role, action, outcome), proven loop + new theme + twist, diverge then select, learning the owner's taste without narrowing, the hook test (title, thumbnail, first minute delivers the promise), idea scoring rubric, 3 pitches + 1 recommendation, pitch template, breakout cases as a reference library, what to ask the trend-scout and marketing | game-designer, marketing, trend-scout |
| `game-design` | design | Judging a design: four parts, name the fun, goals vs tactics, loops at 3 scales and how they couple, principles as observable tests, systems, progression, economy sources and sinks, rewards, luck vs skill, fairness, social and multiplayer, Roblox audience and discovery facts (checked), playtest record, review procedure, finding template, fix ranking, live content | every role that reviews a feature |
| `preproduction` | craft | Growing a picked concept into a full design with the owner, in order: fantasy, pillars, style direction (with art-director), key characters and moments, world, core loop, features, content. Lead reviews and when each lead joins. Document templates: game profile, pillars sheet, feature spec, tuning table, per-craft briefs in `rules/messages.md` format. Hand-offs to art-director, architect, marketing, trend-scout, ui-ux-designer, vfx-designer, sound-designer, animator, content-builder | game-designer, lead |
| `level-design` | design + craft | Kept from the earlier version (game-agnostic parts) + Part 2 levels and encounters: level job card, blockout first, guidance without words, pacing and walk times, encounters, boundaries, scale, 20-point review, marked-up maps | game-designer, content-builder |

## Hidden test set (evals)
Roblox cases 16-18 of Part 1 (Dead Rails, Dress to Impress, Blue Lock Rivals) are held out of the skills. The eval gives the agent only each game's loop and asks for fantasy, hook, twist and smallest test; a separate grader compares with the paper's analysis.

## First real test (G2), proposed
The new agent pitches 3 concepts + 1 recommendation for a new Roblox game, with no theme given. Shown next to the owner's examples (destroy the sun, build a dam to save the city, fly or die).
