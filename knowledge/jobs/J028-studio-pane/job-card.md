---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J028; knowledge/reference/studio/juku-studios-feasibility.md
supersedes: []
---
> Author: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24

# Job card: J028 the Studio pane (live floor and flow map)

Owner words (verbatim, 2026-10-24, from `juku-studios-feasibility.md` "Direction after the owner's review"): "I think it would be cool if the orchestrator loaded up a live like agent view mod with the flow map and the studio floor"; "We don't need the obsidian". Agents never edit settings; the owner enables mods when Claude Code asks.

| Key | Value |
| --- | --- |
| Problem | The owner cannot see in one look who works, who waits, and what waits on the owner, nor where a job lost time (repeated runs, reviewer pile-ups, waits) |
| Constraints | Stay in Claude Code (no T3 fork). One mod, pane titled "Studio", tabs Floor and Flow. Desktop pane elements only (Box, Text, Button, Svg, Markdown, Link); Svg source at most 131,072 characters per draw; no canvas. Read-only data. Agents never edit settings; the owner enables the mod |
| Target experience | Awareness: the owner glances at the pane and knows what runs and what waits on them, without asking the lead |
| Type, size | Kit change (no game recipe), M. Direction is the owner's, recorded on the feasibility page (live-view mod design), so no G1. G3 = the owner opens the pane |
| Success test | `claude plugin validate`, `tsc -p` and `claude plugin test` pass; the pane opens in the lead chat and shows this session's agents live and one real job's flow; the kit gate passes for the changed kit files |
| Bar | Floor: a running agent appears within 5 s, with role name, model badge and room; the owner's desk names every open gate and needs-decision of the active jobs with its file. Flow: bars line up with the usage report's numbers (wall time from first to last record, shade from tokens read); every flag has a stated rule |
| Job lead, crew | lead (orchestrator side session) builds it; no craft role owns studio tooling (craft-owner table: none fits) |
| Code file owners | lead: the mod (`tools/mods/studio/`), `tools/usage_report.py` (new fields `last`, `job`, `id`, `description`, `effort`), `tools/tests/test_usage_report.py` |
| Budget | One session; no image generation (figures are simple SVG shapes; the mascot art is a later reference-images job) |
| Status | build |

## Stages
| # | Stage | Gate |
| --- | --- | --- |
| 1 | Build the mod, the usage report fields, tests | — |
| 2 | Open the pane in the session; check live agents and one job's flow | **G3** the owner opens the pane |

## Progress (2026-10-24)
| Step | State |
| --- | --- |
| Mod built: `tools/mods/studio/` (loaded this session from the session's mods folder) | done; validate pass, `tsc -p` pass on the engine's laid types, plugin tests 7/7 |
| Loaded in the lead chat (owner turned mods on) | done: `mcp__studio__open_pane` answered "The Studio pane is open beside the chat"; a background probe agent ran 48 s during it |
| Fix from the probe: role files have `tier:`, not `model:` | done: the badge takes the tier's model from `kit.json` `models.claude` |
| `usage_report.py` fields `id`, `description`, `effort`, `last`, `job` | done; tests 7/7; gate PASS |
| Seeing the drawn pane | not verified by me: this session was open in no window during the check (app layout empty), and screen capture hides the Claude window. Owner check at G3 |

## Proposed `orchestration` line (not applied; owner decides)
In §1 step 1 (**Read**), first sentence: "Open the Studio pane first (tool `mcp__studio__open_pane`, or `/studio`) when the mod is on, so the owner sees the floor while you work."

## Owner steps to keep the mod in every lead session
From a terminal, once: `claude plugin marketplace add <repo>/tools/mods`, then `claude plugin install studio@studio-kit-mods` (user scope). The session's own mods folder is per session; the repo copy is the source.
