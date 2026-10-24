---
type: decision
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# J025 decisions

| Id | Date | Decision | Approves | Owner's words |
| --- | --- | --- | --- | --- |
| J025-G1 | 2026-10-24 | Defaults of `proposal.md` §8 accepted: D-1 option 1 (thin own layer on proven packages), D-2 keep ProfileStore with a recorded exception to `rules/packages.md` item 2 (own pinned copy), D-3 framework code private (kit copy tool), D-4 UI on plain instances + StyleSheet | `proposal.md` rev 2026-10-24 (first version) | "Okay, yeah, these are all fine, and acceptable for the framework." |

| J025-D2 | 2026-10-24 | Add a universal admin panel block (proposal L19) instead of developer commands: built-in tools (e.g. fly) in every game, plus buttons and frames each game programs. Built-in list and security limits are PROPOSAL | `proposal.md` L19 | "I'd much rather just have some sort of universal admin panel that already comes pre-equipped with basic things like fly and whatnot. But then each project, it also has programmable like buttons and frames and whatnot. So each game can also edit it to fit the project." |

## Closed doors
| Id | Door | May return only if |
| --- | --- | --- |
| CD-1 | Option 2 (keep DataService + Networker) and option 3 (write everything) | a §6 probe fails for the chosen package |
| CD-2 | Our own session lock | ProfileStore shows a data-loss bug we cannot patch |
| CD-3 | Public Wally packages for our blocks | the owner wants to share them |
| CD-4 | Vide as the UI library | list-heavy screens cost too much code on plain instances |
| CD-5 | A content compiler (JSON/CSV → generated Luau; `research/gaps.md` gap 1 as written) | a game's content comes from tools or spreadsheets. Owner 2026-10-24: "we want to build in Lua U to use the proper Roblox document like what the Roblox documentation recommends"; content stays Luau with content tests (proposal L18) |
| CD-6 | Developer commands block (`Dev` on TextChatCommand, or Cmdr; `research/gaps.md` gap 2) and the log + state dump that went with it | the owner asks for it. Owner 2026-10-24: "No, leave developer commands out of the framework." |
