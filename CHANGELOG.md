# Changelog

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

## 0.6.1 (2026-10-21): J016 G3 audit fixes before the pilot

- Five independent audits (core rules, workflows, roles and templates, context system, a tabletop run of three requests) found 57 blocking defects at 0.6.0; all are closed or waiting on an owner decision (role tool lists). Reviews: `knowledge/jobs/J016-orchestration/reviews/`.
- Context: the packet and indexes never list held-out material (names containing `hidden`, or frontmatter `held_out: true`), other leads' direction proposals, `_` material from other games or skill eval briefs; `--role` ranks the role's own book first and lists its precedents; job reviews rank lower for crafts; eval cases carry `role`, `job` and `forbid`; retrieval back to 16/19 on the original cases, baseline in `knowledge/logs/improve/`.
- Workflows: required args with no silent defaults; scripts first and recapture after every repair; VFX then sound in sequence; code review whenever the candidate has code; code file owners from the contract; image steps write `image-prompts.md` and a pending batch stops the stage where later work builds on it; `docs_read` and `lesson` in every hand-back; at most 5 agents at once.
- Rules and roles: interfaces where the recipe places them; the recipe's proof reviewers; sizing; who spawns crafts; no agent ids inside workflows; must-consult column; cross-type rules; split requests with one owner job per shared interface; Codex gate path; role proofs match recipes; reviewer uses the §6 format; templates carry frontmatter.
- Capability check: C22 (a `tools:` list without `SendMessage` cannot send), C23 (`memory: project` adds file tools).

## 0.6.0 (2026-10-21): J016 orchestration and context redesign (owner approvals J016-D4, J016-D5)

- Flow: one accountable lead, a job lead per job, independent direction proposals and one direction sheet, a shared contract per job, an integrated cheap proof, sideways work between crafts, one integrator and Studio writer, an ordered review chain where reviewers never edit; gates G1 direction, G2 integrated proof, G3 final, bound to revisions. Rewritten: `rules/company.md`, `rules/messages.md`, `orchestration` skill (+ `references/job-types.md`), `rules/knowledge.md`; aligned: `AGENTS.md`, harness profiles.
- Seven saved job workflows in `.agents/workflows/jobs/` (synced to `.claude/workflows/`): cutscene, character, stage, UI screen, gameplay feature, effect, marketing art; one stage per call; tested with fake agents (`tools/workflows/wf_harness.mjs`, `tools/tests/test_job_workflows.py`).
- Context: five layers with writers; `context_packet.py --role --job`; `roles:` and `revision:` frontmatter keys; hook scripts in `tools/hooks/` (owner enables); vault starters `precedents.md`, `vocabulary.md`, `taste-log.md`; decisions get a revisit trigger; lesson drafts carry cause and layer; `/improve` routes causes to layers and re-runs capability probes after Claude Code updates.
- Templates: direction sheet, crew list, evidence ledger, exchange note, contract header, review file; job card, brief, hand-back (`built_on`) and ledger updated.
- All 48 skill descriptions ≤ 400 characters (new gate check `f`); every role file has "Your place in the job flow".
- Evidence: `knowledge/jobs/J016-orchestration/` (design, capability check on Claude Code 2.1.296 and 2.1.306, 14 Riot transcripts extracted).

## 0.5.1 (2026-10-20): models and effort per role

- `kit.json`: craft tier → Opus; new research tier → Sonnet. `tools/sync_harness.py` accepts `research`; test added.
- `.agents/roles/README.md`: owner-approved model and effort for all 25 roles; orchestration, company rules and harness profiles match.

## 0.5.0 (2026-10-20): J001 closed

- Skills: `architecture`, `code-review` (with `luau-current` and `testing` references).
- Rule: `rules/anti-overengineering.md` (Claude team guidance), wired into AGENTS.md, code review and briefs.
- Owner research papers digested (architecture, operations) and applied to the approved skills: performance budgets, save recovery and mixed writers, damage-ranked exploit tests, config refresh, multi-client test tools.

## 0.4.0 (2026-10-20): engineering skills (J001 steps 1-5, 8, 9)

- Skills: `studio-mcp`, `platform-policy`, `data-saving`, `performance`, `networking-security`, `ui-basics`, `analytics`, each with sourced references and eval briefs.
- Rules: `rules/packages.md` (choosing packages); AGENTS.md: source mode per game, `studio_id`, secrets rule, skill pointers.
- Reference: digest of the owner's architecture research paper.

## 0.3.1 (2026-10-20): Roblox docs in the kit (J001 step 0)

- The Roblox Creator Docs mirror now ships with the kit (`knowledge/external/roblox-creator-docs/`, upstream `7400643`), with its sync tool `tools/sync_roblox_docs.py` (ported from DestructionSimulator).
- New note `knowledge/reference/roblox/whats-new.md`: 2026 features, betas and rules from official Roblox posts, by skill area.
- Fixed the project-authored UI pages: base UIShadow and per-corner UICorner are live; Upgraded UIShadows and Upgraded UIGradients are beta and not publishable.

## 0.3.0 (2026-10-20): phase 3, orchestrator and agent-building system

- The kit ships only the orchestrator and the system; other roles are built from owner material (owner decision).
- `/build-agent` workflow; templates `templates/role.md` and `templates/skill/SKILL.md`.
- The lead loads the `orchestration` skill at the start of every owner request.
- Removed `/council` (outdated); `/agent-review` folded into `/improve` as a monthly step.

## 0.2.0 (2026-10-20): phase 2

- Knowledge rules (`rules/knowledge.md`): typed frontmatter, load-by-cost layers, scopes, superseding.
- Learning loop inside `/improve`: inbox drafts, weekly consolidation, promotion to lessons, skills, rules and overlays.
- Workflows: `/improve`, `/integrate`, `/kit-sync`, `/council`, `/agent-review`.
- Context tools: `context_packet`, `kb_index`, `eval_context`.
- Process tools: `improve_scan`, `agent_scorecard`.
- Gate: `python tools/verify.py`.
- New folders: `knowledge/lessons/`, `knowledge/overlays/`; inbox README updated.
- Research note: `knowledge/reference/studio/context-research-2026-10.md`.

## 0.1.0 (2026-10-20): phase 1

- Rules: company rulebook, owner profile, harness profiles (Claude Code, Codex).
- Orchestration skill and role roster.
- Job templates: job card, intent brief, beat sheet, ledger, decision digest, status block.
- Sync tool: `tools/sync_harness.py` generates `.claude/` and `.codex/`.
- Knowledge skeleton: index, game profile, ledgers, orchestration research.
