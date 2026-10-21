---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent game-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J003 — Build the game-designer agent

| Field | Value |
| --- | --- |
| Job id | J003-game-designer |
| Size | L (new role, 4 skill books, two research papers to extract and fact-check, an earlier version to merge, first real test) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-20 (J003-D1..D4). Steps 2-5 done 2026-10-20 (notes + 2 fact-checks in `knowledge/reference/game-design/`; skills game-concept, preproduction, game-design, level-design; role game-designer; evals). Step 6 done 2026-10-21: hidden test 15/15 (grades-hidden.md); G2 pitch set 11/11 after one correction pass (grades-g2.md, g2/pitch-set.md). G2 sent to owner 2026-10-21. Closed 2026-10-21 (J003-D5): agent done, G2 review and G3 waived by owner |

## Owner's words (2026-10-20, excerpts)
- "generates and pitches ambitious, creative game concepts with a strong, marketable fantasy: titles players read and think 'I need to do that' or 'what would happen if I did that?' (for example: destroy the sun, build a dam to save the city, fly or die) ... giving a proven, trending core loop a new theme and a twist."
- "After I pick a concept, it leads pre-production with me ... fantasy, style direction, key characters and moments, world, core loop, features and content."
- "works with the other lead agents from the start: the art director, the architect, the marketing agent, the trend scout, and the craft leads (UI, VFX, sound, animation, levels)."
- "turns the decided game into clear documents that every other agent can build from, following rules/messages.md: exact where it must be exact, with the craft left open to the specialist."
- "reviews designs, loops, systems and level plans, catches problems early and proposes fixes."
- "I am the creative director and I usually know what is fun on Roblox. The agent proposes, with one clear recommendation; I decide."
- "Use them as strong evidence, but not as gospel. Check claims that matter, especially numbers and Roblox facts, and drop what you cannot back up."

## Goal
One `game-designer` agent that (1) pitches bold, marketable Roblox concepts built on a proven loop with a new theme and a twist, (2) grows the picked concept with the owner and the other leads into a full, cohesive design, (3) writes that design as documents every agent can build from (`rules/messages.md`), and (4) reviews designs, loops, systems and level plans with evidence and ranked fixes. It proposes with one recommendation; the owner decides.

## Material received (outside git, `C:\Users\Firew\Downloads\`)
| File | What | Size | Trust |
| --- | --- | --- | --- |
| Game_Designer_Part_1_Research.txt | Ideas to approved plan: AI ideation evidence (A01-A13), 18 breakout cases incl. 6 Roblox (C, R sources), hook test, preproduction, pillars, feature spec, tuning table, per-craft briefs, pitch template, working with a creative director | 982 lines, 105 KB | high: evidence-tagged (VERIFIED / EXPERIENCE / OPINION), dated source registry; many sources dated 2026 after the model cutoff, so numbers need a check |
| Game_Designer_Part_2_Research.txt | Craft of design review: loops at 3 scales, principles as tests, systems and economies, levels and encounters, multiplayer and social, playtests, critique and fix ranking, live content, AI review procedure (D01-D29, R01-R13+) | 630 lines, 74 KB | high, same tagging |
| DestructionSimulator `.claude/agents/game-designer.md`, `.agents/skills/game-design`, `.agents/skills/level-design` (read-only) | Earlier version: four parts of a game, name the fun, goals vs tactics, mechanics carry theme, fair frustration, luck vs skill, 16-point review; level job card, guidance, pacing, boundaries, 20-point review | 195 lines | medium: from Riot "So You Wanna Make Games??" transcripts (2026-10-15); game-specific parts to remove |

## Scope
| In | Out |
| --- | --- |
| Reference notes per source part in `knowledge/reference/game-design/` + fact-check table | Writing game code, tuning a live economy (economy-designer, planned) |
| 4 skill books (see brief) | Building the trend-scout and marketing agents (only roster rows + hand-off briefs) |
| Role file `game-designer`, eval briefs, hidden test set | Market data pulls (that is the trend-scout's job later) |
| Roster rows: game-designer (in kit), trend-scout (planned), marketing (planned) | New web research beyond checking the papers' numbers and Roblox facts |
| One real test task (G2) | Changing other skills (only pointers to them) |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×4 (Part 1 split in 2, Part 2 split in 2) | Sonnet | high (J002-D2 precedent) | dense notes per part |
| fact-checkers ×2 (Roblox facts and numbers; AI and industry numbers) | Sonnet | high | fact-check table: claim, source, checked against, verdict |
| lead (merge, skill writing, role, evals) | Opus | high | 4 skill books, role file, evals, roster |
| game-designer (new, first test) | Opus | high (roster) | the G2 test output |
| grader (evals, separate context) | Sonnet | high (J003-D2) | rubric scores against the hidden set |

## Mechanism
Subagents for extraction and fact-checks (independent, verbose output), in two waves of 3 (company limit: 3 concurrent). The lead writes the skills (needs the whole picture to merge both papers and the earlier version). The new agent runs the first test as a subagent; a separate grader scores it.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 4 extract + 2 fact-check + 1 test + 1 grader = 8 | 4 extract + 2 fact-check + 2 designer runs (G2 + hidden) + 1 correction pass + 2 graders = 11 |
| Models / effort | Sonnet high ×7 (J003-D2); Opus high (lead, test) | |

## Acceptance checks
- [ ] Every number and Roblox fact used in a skill has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-OPINION / dropped). Dropped claims are listed with the reason.
- [ ] Evidence tags (VERIFIED / EXPERIENCE / OPINION) kept on every rule; no invented targets (retention, session length, prices).
- [ ] Nothing specific to DestructionSimulator in the kit skills (grep for destruction, gear, stage.json, D-0..D-2xx = 0 hits outside the source table).
- [ ] The pitch method produces exactly 3 pitches + 1 recommendation, each with fantasy, title, first image, proven loop, twist, smallest test, risks.
- [ ] Every document template in the preproduction skill follows `rules/messages.md` (`<intent>` + `<spec>`, `fixed` with sources, `open`, `rules`, `checks`).
- [ ] Hand-off briefs exist for art-director, architect, marketing, trend-scout, ui-ux-designer, vfx-designer, sound-designer, animator, content-builder.
- [ ] Skills ≤ 500 lines each, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and the gate PASS.
- [ ] Hidden test: the agent passes ≥ 4 of 5 rubric items on held-out cases it was not built from (separate grader).
- [ ] First real test shown next to the owner's examples (destroy the sun, build a dam to save the city, fly or die).

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-20 | "I think we can begin creating the agent. This looks good." + "run all the Sonnet models on high" + game designer always Opus on high |
| G2 first samples (L) | 2026-10-21 | waived: "For now, the agent is just done." (J003-D5) |
| G3 final look | 2026-10-21 | waived (J003-D5); testing happens through real games |
