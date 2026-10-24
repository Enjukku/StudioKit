---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# Step 1: where is the owner's old framework?

Searched: `C:\Users\Firew\Downloads`, `Documents`, `OneDrive` (Desktop, Documents) to depth 6, `C:\work`, `C:\c`, `C:\jt`, `C:\town_fisher`, `C:\tmp`, `C:\art`; no D: or E: drive. Name search: folders `*crew*`, `*krew*`, `*kru*`, `*core*`, `*framework*`; every `wally.toml` (345 files, grouped below); `.git/config` remotes; the owner's GitHub repos (`gh repo list`); Claude Code transcripts.

**Result: no code framework named crew, krew or kru exists on this machine or on GitHub.** The only "crew" hits are a monster model (`model_crew.rbxm` in `Downloads/RB/*`), the `crew-progress` Claude mod, and CrewAI in research text.

## Candidates

| # | Path | Date | What it is | Code? |
| --- | --- | --- | --- | --- |
| C1 | `C:\Users\Firew\Downloads\uterd\DestructionSimulator\knowledge\design\game-framework.md` | 2026-10-08, edited 2026-10-10 | The framework **plan** (PROPOSAL): two halves (game code as Wally packages in a separate repo; the AI studio kit), a candidate list tagged in Destruction Simulator (bootstrap, player session + save wrapper, transport conventions, economy ledger, telemetry, content compiler, verify gate), "extract when the second game starts". Owner rules D-111, D-112, D-135, D-136 in the same game's `decisions.md:121-146`. | plan only |
| C2 | GitHub `Enjukku/roblox-game-framework` ("Proprietary genre-agnostic Roblox game framework") | created 2026-10-09 | The repo D-111 named for the framework. | **empty** (no commits) |
| C3 | `C:\Users\Firew\Downloads\Roblox-Starter-Kit` (+ GitHub `Enjukku/Roblox-Starter-Kit---Copy`, 2026-06-09) | 2026-05-23 | Clone-and-rename starter: agent roster, rules, docs mirror, toolchain (`rokit.toml`), Rojo tree, `wally.toml` "locked stack". | empty `src/` (only `.gitkeep`); packages only |
| C4 | `C:\Users\Firew\Downloads\Roblox-BallXPit - BASE SETUP` | 2026-05-22 | An agent-kit copy (rules, skills, agents). | no Luau |

My best guess: the owner remembers C1 + C2 (the plan and its repo; "crew" may mix with the `crew-progress` mod name). C3 is the oldest "starter" and holds the package stack every later game kept.

## The package stack in every game (one stack since May 2026)

| Project group | `wally.toml` name | Dates | Packages |
| --- | --- | --- | --- |
| Roblox-Starter-Kit | template | 2026-05-23 | DataService, signal, charm, janitor, Networker, React, ReactRoblox, ReactCharm, ripple |
| Painting Incremental | firew/100-players-paint-incremental | 2026-05-26 | same minus ripple |
| Roblox-BallXPit, BX/* | firew/roblox-ballxpit | 2026-09-25 | same (some with ripple) |
| Roblox-Blocks, RB/*, RB-lanes/* (38 copies) | firew/roblox-blocks | 2026-09-16..25 | DataService 1.0.0, signal 2.0.3, charm 0.10.0, janitor 1.18.3, Networker 0.3.1 |
| DestructionSimulator (+197 worktrees) | firew/destruction-simulator | 2026-09-30..10-16 | same five |
| GreatWallSim (+101 copies), NewGame | firew/new-game | 2026-10-13..24 | same five |

So the real "old framework" in practice is this five-package stack plus each game's own glue code (studied in `games.md`).
