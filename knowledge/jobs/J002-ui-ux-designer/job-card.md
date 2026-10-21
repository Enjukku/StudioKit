---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J002 — Build the UI/UX designer agent

| Field | Value |
| --- | --- |
| Job id | J002-ui-ux-designer |
| Size | L (new role, 6 skill books, research synthesis, first real test) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-20. Steps 2-5 done. Step 6 G2 test done 2026-10-20: cartoon egg shop in Figma (https://www.figma.com/design/gVgO2Ql80LUerCpQe02CtD), `content/ui/egg-shop/`, 27 skill gaps (`content/ui/egg-shop/skill-gaps.md`) fixed in the books; independent review `review-T08.md` (8 must-fix, 18 should-fix, 13 nits) fixed; VFX texture library linked (J002-D7). Second test T09 done 2026-10-21: anime summon (https://www.figma.com/design/Ob2rRbGBRlmP5JmGyVOlUG), `content/ui/anime-summon/`, 8 library textures, 23 skill gaps fixed in the books + 1 lead-found defect (clipped focus rings) fixed in Figma. Owner G2 review 2026-10-21: "B minus", some buttons "A"; fix = required ChatGPT target reference image before styling (J002-D12), done in the role and books. Next: G3 |

## Owner's words (2026-10-20, excerpts)
- "begin building the UI and UX design agent ... how to build four various UI styles within Figma, which is how we are mainly going to make UI unless I say otherwise."
- "synthesize down all that information into clean guides on how to do each style. So into different skill books."
- "take bits of all of the learnings and improve those skill books as well ... take some stuff that you've learned from the cartoon guide and also implement it into the stud guide ... stronger fundamentals. Or understanding of how to use Figma."
- "a research paper made by ChatGPT on what strong UI or UX looks like within the game industry ... capable of doing various UI styles, while also making them look good with great UI and great UX design."

## Goal
One `ui-ux-designer` agent that designs Roblox game screens in Figma in any of four styles (cartoon, stud, anime, pixel), with strong UX (clear decisions, every state, every device), and hands builders an exact, buildable spec.

## Material received (outside git, `C:\Users\Firew\Downloads\`)
| File | What | Tool used in video | Depth |
| --- | --- | --- | --- |
| Cartoon Guide.txt | Cartoon pet inventory (UI Genesis, Hamuri) | Figma | high: step by step, exact values |
| Stud Guide.txt | Stud shop + HUD (UI Genesis, Hamuri) | Figma | high: step by step, exact values |
| Anime Guide.txt | Anime TD unit inventory (UI Genesis, Kek) | Photoshop | low: experimental, few values, file lost mid-video |
| PixleArt Guide.txt | Pixel rogue-like HUD (Kakuza) | Photoshop | medium: first half narrated, second half music only |
| Game_UI_UX_Research_AI_Designer.txt | Game UI/UX research, 12 cases, 25 motion records, Roblox rules | n/a | high, evidence-tagged |

## Scope
| In | Out |
| --- | --- |
| Reference notes per source in `knowledge/reference/ui/` | Building UI in Roblox (that is `ui-basics` + builders) |
| Skill books (see brief) | Writing game code |
| Role file `ui-ux-designer`, eval briefs | New research on the web (only to check a Figma or Roblox fact the material leaves unclear) |
| One real test screen in Figma (G2) | Icon / render production (Blender) |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors (one per source; research paper split in 2) | Sonnet | high (owner J002-D2) | dense notes per source |
| lead (skill writing, role, evals) | Opus | high | skill books, role file, evals |
| ui-ux-designer (new, first test) | Opus | medium (roster) | one screen in Figma + spec |

## Mechanism
Subagents for extraction (independent, parallel, verbose output). Lead writes the skills (needs the whole picture to cross-pollinate). New agent runs the first test as a subagent.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 6 extract + 1 test = 7 | |
| Models / effort | Sonnet medium ×6; Opus high (lead); Opus medium ×1 | |

## Acceptance checks
- [ ] Every style book is followable by an agent with no transcript: each step names the Figma action and the value.
- [ ] Each style book has the shared fundamentals it needs (3D layered depth, flattened outline, group mask, blend modes, padding check, naming) with the best version found across all four sources.
- [ ] Every Figma effect is marked: native in Roblox (UIStroke, UIGradient, UICorner, UIShadow) or baked into an image. Nothing relies on blend modes at runtime (Roblox has no blend modes for UI).
- [ ] UX rules from the research keep their evidence tags (VERIFIED / EXPERIENCE / OPINION / UNSPECIFIED); no invented timings.
- [ ] Skills ≤ 500 lines each, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and the gate PASS.
- [ ] First real test screen shown next to the best source example.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-20 | "Okay, yeah, you can plan the 6 skill books." + Sonnet on high, use my Figma, add ChatGPT image generation |
| G2 first samples (L) | pending | shown 2026-10-20 |
| G3 final look | | |
