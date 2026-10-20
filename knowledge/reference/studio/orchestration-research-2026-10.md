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

## Gaps

- No 2026 study found on approval gates for creative or game-art work.
- No measurement of how often blocked or needs-decision statuses occur. Track them in ledgers.
