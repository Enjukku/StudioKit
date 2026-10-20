> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit rule: universal. J001 step 7, revised the same day on owner request: sources from the last 3 months, Opus 5.5 first.
> **Primary sources (2026-09-22 to 2026-10-19):** Anthropic "Prompting Claude Opus 5.5" (platform.claude.com, model release 2026-09-22); "How the Claude Code team does code review" (claude.dev/blog/solving-code-review-at-anthropic, 2026-10-15) and the Code Review release (Claude Code 2.1.304, 2026-10-19); "Redesigning source control at Anthropic" (anthropic.com/engineering, 2026-10-13); Claude Code best practices (code.claude.com/docs/en/best-practices, current page). **Ideas only** (other models; the owner says they behave differently from Opus 5.5): Sonnet 5.5 and Haiku 5.5 prompting pages (2026-09-28, 2026-10-07), Fable 5.1 and Opus 5 pages, the general "Overeagerness" section. Anthropic research posts "Improving alignment and security efforts" (2026-08-31) and the cybersecurity-incidents alignment assessment (2026-09-09). Owner research paper: `knowledge/reference/architecture/strong-codebases-2026-10.md` A-08, A-11, A-21.

# Build what was asked, at the size it needs

Over-building is the most common failure of AI-written code: extra features, files and options; abstractions for one-time use; defensive code for cases that cannot happen; fixing nearby code; more tests than behaviours; review rounds that never end. Under-building (stubs, or stopping with work left) is the opposite failure. Both are defects.

## Scope
1. Change only what the brief or approved plan asks for, or what the request cannot work without. Do not quietly narrow, widen or swap the scope.
2. A bug, slow spot or better idea found along the way is **reported as a follow-up** (tagged pre-existing if it is in untouched code), not fixed in this change.
3. If the request is ambiguous, build the reading the wording and the existing code most directly support, and state the assumption. Ask only when readings lead to materially different work.
4. A better approach than the one asked: say so in one or two sentences, then continue as asked. For plans or ideas: give them and stop; build only when told.
4b. **Blocked or impossible:** stop and report `blocked` or `failed` with the reason. Do not find a route around the block, and do not hand in knowingly partial work as done (agents facing blocked tasks tend to seek other routes and go out of scope: Anthropic, 2026-08-31).

## Size
5. **No abstraction with one user.** No helper, base class, wrapper, event bus, registry, config option or plugin point for a single call site or a hypothetical future need. Add it when a second real user appears.
6. **Data tables are not over-building** when the game's roadmap already has many items of that kind (weapons, pets, levels): content as data is the default (`AGENTS.md` §2).
7. No new package or framework without `rules/packages.md`.
8. Surgical edits: no whole-file rewrites, renames, moves or reformatting the task does not need.

## Defensive code
9. Validate at **boundaries**: client requests, saved data on load, external HTTP, Roblox services that can fail (data stores, MarketplaceService, Teleport, HTTP). These really fail, so `pcall` and retries there are required, not over-building.
10. Inside our own code, trust our own contracts: no fallbacks, nil checks or type checks for states our types and owners already rule out. Reviews that chase hypothetical risks push in exactly this excess validation (Anthropic source-control post, 2026-10-13).

## Tests, comments, files
11. One focused test per stated behaviour and per stated failure case, sized like the neighbouring tests; plus the kinds `code-review` requires for saves, remotes and money. Scratch checks are not committed.
12. Tests check the general rule; never hard-code or special-case test inputs to pass. A wrong or impossible test is reported, not worked around.
13. Comments only where the logic is not obvious, plus contract blocks on important modules (`architecture` R-10). No comments or annotations added to code the task did not change.
14. Temporary files and scripts are deleted before hand-back.

## Effort and finishing (Opus 5.5)
15. **Set effort before adding prompt text.** Medium is Opus 5.5's default and matches Opus 5 at high on coding with fewer steps; use high for hard or long tasks; xhigh and max only where a measured gain justifies them (they think and spend more). Lowering or raising effort steers scope more reliably than extra instructions (Opus 5.5 guide).
16. **Done means checked, and nothing left running.** A text-only status update is a report, not completion. Keep the task's checklist; the work is done when every item is checked by a real test or run (a syntax check or a command that failed to start does not count; a skipped check is named with the reason) and no background command or agent is still running. One end-to-end check shows the feature works for a player. Never state an unverified inference as fact; a partial check is reported as partial (the Opus 5.5 system card, 2026-09-22, reportedly names this as the model's most frequent flagged behaviour: second-hand, the PDF was too large to read).
17. When the work and its checks pass: **stop and report.** No extra hardening or review rounds unless the brief asks; extras go in the report as suggestions.

## Review rounds (Claude Code team, 2026-10-15)
18. Reviewers report only what affects correctness, safety, money, saves, the stated requirements, or scope. No style, cleanup-only or "could be nicer" findings: agents act on every nit, and each nit becomes another commit and another round.
19. Review depth follows risk: quick for small low-risk changes, standard by default, deep for money, saves, security and wide changes.
20. **After 3 review rounds, stop patching:** reconsider the approach with the lead. Later rounds review only the new diff. (Anthropic measured: first-round passes rose from 65 % to 78 % and changes needing 5+ rounds fell from 8.9 % to 1.5 % with these limits; 59 % of repeat findings were about old code.)

## Checks a reviewer can apply
New files the plan did not name · an abstraction or option with one caller · `pcall` or fallbacks around our own pure code · changes outside the owned files · more tests than behaviours · comments on unchanged code · a "while I was here" fix · a stub that renders but does nothing · a fourth review round on the same approach.
