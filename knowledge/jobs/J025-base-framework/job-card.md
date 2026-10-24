---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# Job card: J025 universal base game framework

## The owner's words (verbatim, first)
> "a large part that we're missing is a base game framework that helps us develop games quicker... create some really high quality packages that can be reused... a universal one... a really high quality data storage or whatever that we can use for every game. Universal things like that where we just have a really strong foundation for anything we create."

> (2026-10-24, same session) "And when we create this, we really want to look at the Roblox documentation packages need to be like the best possible highest quality code that we can literally create. It needs to be fast, effective, bugless, clean, it needs to be like absolutely incredible. And to do that, we're going to need to deeply search the Roblox platform and we could do this looking through Roblox documentation. We could use old games as references. And then we need to see where we can, you know, implement this, you know, whether it's UI, do we create some sort of universal UI manager, animation manager, data storage manager, janitor whatever, you know what I'm saying? Like we want to create all these universal super useful packages for our future game development and then incorporate it into our studio kit so that all future games we build can be built super high quality and efficiently."

Earlier owner decisions this job continues (Destruction Simulator ledger, `C:\Users\Firew\Downloads\uterd\DestructionSimulator\knowledge\design\decisions.md`): D-111 (framework in its own repo, starts with the second game), D-112 (genre-agnostic single-purpose blocks "just like how the janitor is", adoptable piece by piece in existing games), D-136 (any genre).

| Field | Value |
| --- | --- |
| Job id | J025-base-framework |
| Title | Universal base game framework: reusable Luau packages for every game |
| Size | L: a new code product every future game depends on; saves and remotes in scope |
| Type (recipe) | other: kit job (no game recipe fits; the closest, feature, assumes one game). This session runs only the research and proposal (steps 1-4); build waits for the owner's pick |
| Job lead (agent) | orchestrator (this side session of the J024-era lead chat) |
| Direction leads | orchestrator; architect limits sheet at build time |
| Integrator | not yet |
| Studio place (`studio_id`) | none (files only in this stage) |
| Code file owners | not yet |
| Linked jobs | none |
| Risks (review slots) | saves, remotes, money (the data and transport layers carry them) |
| Status | direction: research and proposal |

## Four lines (goal)
| Line | Value |
| --- | --- |
| Problem | Every new game re-assembles the same base (saves, remotes, player state, UI state, cleanup, config) from scratch or by copy, at uneven quality; the owner wants one strong, reusable foundation. |
| Constraints | Rojo + Wally, Luau `--!strict`, server authority, one transport, content as data (`AGENTS.md` §2); `rules/packages.md` adopt test; `rules/anti-overengineering.md` (no framework for its own sake, no one-user abstraction); genre-agnostic (D-112, D-136); adoptable piece by piece in existing games (D-112); phones first. |
| Target experience | (builders, not players) mastery: an agent starts a new game and has saves, remotes, state and cleanup working and correct on day one, without writing or reviewing them again. |
| Success test | Owner picks a ranked plan: per layer, an existing package or our own, with reasons; then (build stage) a new game reaches "player joins, data loads with a session lock, a validated remote changes saved state, UI shows it, player leaves, data saves" from the template with no new base code. |
| Goal word | foundation |
| Belief check | none (no player-behaviour claim) |

## Scope
| In | Out |
| --- | --- |
| Find the old framework; study GreatWallSim and DestructionSimulator packages and shared code; research each layer; ranked proposal | Building any package; changing either game; committing |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| general-purpose (game study) | sonnet | medium | `research/games.md` |
| researcher × 4 | sonnet | medium | `research/<layer>.md` |

## Stop criteria and budget per stage
| Stage | Stop criteria | Passes | Image cap | Tokens estimate | Tokens actual |
| --- | --- | --- | --- | --- | --- |
| direction (this session) | floor: ranked proposal with every layer decided as PROPOSAL, reasons and sources · bar: every package claim carries a dated source (release, licence, strict types), every "write our own" names the risk it removes and its size | 1 | 0 | no history for this job type; lead under 500 k (J023-D1) | lead ~150 k; agents ~750 k (games 228 k, data 151 k, net 150 k, state/UI 107 k, shape 115 k). Result: `proposal.md`, BAR fail (four probes open) |

## Gates
| Gate | Date | Revision approved | Owner's words | Doors closed |
| --- | --- | --- | --- | --- |
| G1 direction | | | | |
