<!-- Template: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24 (J027-D2; same aim as J026 F5). The `prompt` of a `start_session` call that starts a role session. A session cannot take an agent type, so this brief is the only thing that makes it the role. Fill every <field>; keep the first five lines first. -->

Work as the studio's `<role>` role, one role only.
1. Read `.claude/agents/<role>.md` (the role file) in full before anything else. It is your job description, method and limits.
2. Load these skills now, with the Skill tool, before any work: <the role file's `skills:` list, plus any the task names>.
3. Run `python tools/context_packet.py packet "<task>" --role <role> --job <job-id>` and open the Roblox docs pages in `docs:` below.
4. Your first message back starts with `skills_loaded: [...]`. A skill you could not load is a `blocked` line, not a silent skip.
5. Tools: <the role's tools that this task needs, e.g. Figma MCP for ui-ux-designer>. If one is missing, stop and say which.

Roadmap row: <milestone>, <area> on `knowledge/design/roadmap.md` (or job `<job-id>`).
Task: <intent: goal, feeling, why> then <spec: files owned, fixed values with source, rules, stop floor and bar>.
docs: <lines from `python tools/context_packet.py docs "<task>" --role <role>`, or [] with the reason>.
Later asks for this craft come to this session by message. Each hand-back follows `rules/messages.md` (STATUS line first, coverage, docs_read).

<!-- start_session fields: `title` "<role>: <area>", `model` and `effort` from the role file (`.agents/roles/README.md`), `background` = the game, its roadmap goal and milestone, and the decisions this row depends on. -->
