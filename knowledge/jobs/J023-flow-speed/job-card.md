---
type: job
scope: universal
status: active
updated: 2026-10-24
source: owner chat 2026-10-24
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# Job card: J023-flow-speed — a faster job flow at the same quality

## Owner's words (verbatim)
- "Do you think we should also look at maybe shortening the workflows of tasks? Like, it goes through so many steps and stuff."
- "And maybe even shortening the principles behind our agent MDs or whatever."
- "I would like to know exactly what you plan to get rid of or shorten and how you're going to shorten the workflow. Like all the steps of it going back in between agents."
- "I feel like for Opus agents, it could be a session size rule of under 500K. And that's still very fresh. It could even be like 600K."
- "before crafts, I think it might be important for the four crafts to come back together to kind of say what they need. Because all the sound and VFX and models and stuff and animations all go together."
- "I think we might already be a good quality level, but it's more about increasing the speed, the efficiency, while still maintaining quality."
- "I think you need to fully understand the entire workflow before you recommend something. This could involve maybe deploying some Sonnet research agents"

## Four lines
| Line | Value |
| --- | --- |
| Problem | Jobs pass work between many agents; one real cutscene run used 24 agent runs and about 200 M tokens before the animatic |
| Constraints | Quality stays at today's level; the crafts' joint needs step stays (owner); design and gates are the owner's; no rule lost; no edit before the owner picks |
| Target experience | mastery: game work moves fast without the owner noticing a drop in quality |
| Success test | The owner understands every step of each job flow, why it exists and what it costs, and picks the changes; after they ship, the same job types use fewer tokens and less time with no rise in repair rounds or owner-found defects |

## Status
Built 2026-10-24 per J023-D5 (options A-G, design.md): 7 workflow scripts (3 Opus builders), recipes, rules and templates (writer), old tests updated; new tests tools/tests/test_j023_*.py (48). Minimum runs L/M: cutscene 56/56 -> 48/36, effect 35/35 -> 29/20, character 46/46 -> 43/35, stage 48/48 -> 41/33, feature 36/36 -> fewer (direction 8 -> 2-3), UI and marketing fewer (builder hand-backs). Gate RESULT: PASS (1216 tests; gate timeout raised 600 -> 1200 s). Not committed; no independent review yet. Open: reference-images/SKILL.md:56 one-batch wording (other chat's file); owner walkthrough of four flows done, next cuts pending.
