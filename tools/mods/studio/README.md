# Studio pane (Studio Kit mod)

A pane titled "Studio" beside the lead chat, with two tabs (job J028):

- **Floor**: one figure per running agent of this session, in its craft room (role name above, model badge O/S/H, effort pips; a waiting agent is dimmed with "zz"). Below: a button per agent that shows its transcript, and the owner's desk: each active job's Status row, open gates and needs-decision lines from `knowledge/jobs/active.md`, each job's `job-card.md` and `decisions.md`, with an Open button.
- **Flow**: one job at a time. A lane per role (the lead's sessions first), a bar per agent run (width = wall time, shade = tokens read), gates as dashed lines, and flags: one role 3+ times in a stage, 3+ reviewers in one round, waits over 30 minutes, runs past 500k context.

Data is read-only: `$.agent.list()` and agent-spawn events for live runs, the job folders through `$.fs`, and `python tools/usage_report.py --json` every 60 s while the pane is open.

Open it with `/studio [floor|flow] [job id]`, or the model calls the `mcp__studio__open_pane` tool.

Install (the owner, once, from a terminal): `claude plugin marketplace add <repo>/tools/mods`, then `claude plugin install studio@studio-kit-mods`.
