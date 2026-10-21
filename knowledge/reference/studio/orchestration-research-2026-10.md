---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "kit phase 1"
supersedes: []
---
> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

# Orchestration research, October 2026

| Finding | Source | Date | What it means for the studio |
| --- | --- | --- | --- |
| Agent-team plan approvals are approved automatically by the lead without review; teammates' permission prompts bubble to the lead | code.claude.com/docs/en/agent-teams (v2.1.296) | read 2026-10-20 | Agent approval is never owner approval. Gates need an owner message. |
| Agent teams use about 7x tokens in plan mode; start with 3-5 teammates; 3 focused beat 5 scattered; experimental, off by default | agent-teams + code.claude.com/docs/en/costs | read 2026-10-20 | Teams stay off. Default 3 concurrent specialists per job. |
| A message delivered to an idle session starts a new turn that resends its full context | code.claude.com/docs/en/costs | read 2026-10-20 | Batch messages to idle chats. Use shared files. |
| Subagents nest up to three levels; SendMessage reaches named agents and other sessions | code.claude.com/docs/en/sub-agents, cross-session-messaging | read 2026-10-20 | Hop limit 3. Production chats message by name. |
| Projects guidance: ask Claude to propose threads and wait for the go-ahead; run a few at a time; drop limits once threads come back right | code.claude.com/docs/en/claude-projects | read 2026-10-20 | G1 before work. Concurrency limits. Loosen G2 after three good runs. |
| Shared files instead of repeated 1-to-1 messages cut output tokens about 42% at eight agents; naming a coordinator creates no hub and no reliable success gain | arXiv 2608.16801 | 2026-08-17 | Briefs, results and decisions live in the job folder. Messages are pointers. |
| Human-in-the-loop: gate on arguments, bind approvals to what was shown, write rejections as next steps; "the more often a reviewer is asked, the less each answer means" | DevelopersDigest | 2026-10-17 | Few gates; one digest per turn; record what was shown with each answer. |
| AI judges share the generator's blind spots in artifact creation | arXiv 2608.28122 (abstract) | 2026-08-28 | Agents check measurable rules only. The owner judges taste. |
| Start simple; split by context, not by role; 3-10x tokens; failure modes: telephone game, misrouting, early victory | claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them | 2026-01-23 (older background) | One agent per independent piece. No planner-builder-tester chains. Check hand-offs against the brief. |
| Plan mode prevents expensive re-work when the initial direction is wrong | code.claude.com/docs/en/costs | read 2026-10-20 | Plan and brief before building (G1). |

## Replaced conclusions (J016, 2026-10-21)
The findings above stay; some consequences changed after the owner's two orchestration papers and a live check on Claude Code 2.1.296 and 2.1.306 (`knowledge/jobs/J016-orchestration/design.md`, `knowledge/reference/studio/claude-code-capabilities.md`):
| Old consequence | Now | Why |
| --- | --- | --- |
| Hop limit 3 (from the nesting limit) | round, repair and depth limits (`rules/company.md` §9) | nesting limits spawning, not production stages (C04) |
| Default 3 concurrent specialists | parallel by the dependency graph, max 5 per stage | the "3 focused beat 5 scattered" advice is about agent teams, which stay off (C12) |
| Hub and spoke by default; report only to the asker | hybrid: one accountable lead, direct exchange between crafts that share an interface | both papers; subagents can message by id (C01-C03) |
| G2 = one sample per craft | G2 = one integrated proof | both papers; Riot and Valve practice |

## Gaps

- No 2026 study found on approval gates for creative or game-art work.
- No measurement of how often blocked or needs-decision statuses occur. Track them in ledgers.

## Tried and rejected in J016 (2026-10-21)
| tried | why it failed | evidence | retry only if |
| --- | --- | --- | --- |
| Agent teams for messages between crafts | experimental, interactive only, one team per session; SendMessage works without them | `knowledge/reference/studio/claude-code-capabilities.md` C01, C12 | teams leave preview and support nesting and resume |
| Peer ids inside saved workflows | a workflow's agent() exposes no agent id; parallel agents cannot hold each other's ids | J016 audit A F05 (`knowledge/jobs/J016-orchestration/reviews/core-rules-322c8ad-auditor-a.md`) | workflows expose agent ids |
| VFX and sound "read the other's note if it exists" inside one parallel() step | neither sees the other's note | J016 audit B F4 | never; use producer writes → consumer answers → producer merges |
| Silent default workflow args (size L, money false) | an M job skipped its proof; money rules never loaded | J016 audits A F02, E TT-05 | never; required args return blocked |
| "Closest type" for a mixed request | it drops part of the request (the gold skin's shop sale) | J016 audit E TT-09 | never; split into one job per type with one owner per shared interface |
| Withholding held-out material by file name only | grade and eval-answer notes with normal names repeated held-out rubrics | J016 recheck E N-01 | never; names containing "hidden" plus frontmatter `held_out: true` |
| Image downloads inside a workflow run without the owner's yes | a workflow cannot ask the owner mid-run | J016 audit E TT-02 | a workflow can pause for the owner |
| The lead editing role tool lists on its own | refused as self-modification; tool lists are agent permissions | J016 lesson 3 (`knowledge/inbox/2026-10-21-J016-G3-orchestrator.md`) | never; the owner decides, as in J016-D6 and J016-D7 |
