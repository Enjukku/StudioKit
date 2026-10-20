> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit rule: universal. J001 step 7. Sources: Anthropic prompting guides (platform.claude.com, current pages read 2026-10-20: "Overeagerness"; Sonnet 5.5 "Steer initiative and scope"; Fable 5.1 "Keep changes and tests to what the task asks for", "Delivering work"; Opus 5 "Task scope and over-verification"), Claude Code best practices (code.claude.com/docs/en/best-practices), Anthropic engineering "Harness design for long-running application development" (2026-03-24); owner research paper (`knowledge/reference/architecture/strong-codebases-2026-10.md` A-08, A-11, A-21).

# Build what was asked, at the size it needs

Over-building is the most common failure of AI-written code. Anthropic names the causes: extra features, files and options; abstractions for one-time use; defensive code for cases that cannot happen; fixing nearby code; more tests than behaviours; extra review rounds after the work is done. Under-building (stubs that look done) is the opposite failure; both are defects.

## Scope
1. Change only what the brief or approved plan asks for, or what the request cannot work without. The brief's scope is not narrowed, widened or swapped quietly.
2. A bug, slow spot or better idea found along the way is **reported as a follow-up**, not fixed in this change.
3. If the request is ambiguous, build the reading the wording and the existing code most directly support, and state the assumption. Ask only when readings lead to materially different work.
4. A better approach than the one asked: say so in one or two sentences, then continue as asked.

## Size
5. **No abstraction with one user.** No helper, base class, wrapper, event bus, registry, config option or plugin point for a single call site or a hypothetical future need. Add it when a second real user appears.
6. **Data tables are not over-building** when the game's roadmap already has many items of that kind (weapons, pets, levels): content as data is the default (`AGENTS.md` §2).
7. No new package or framework without `rules/packages.md`.
8. Surgical edits: no whole-file rewrites, renames, moves or reformatting the task does not need.

## Defensive code
9. Validate at **boundaries**: client requests, saved data on load, external HTTP, Roblox services that can fail (data stores, MarketplaceService, Teleport, HTTP: these really fail, so `pcall` and retries there are required, not over-building).
10. Inside our own code, trust our own contracts: no fallbacks, nil checks or type checks for states our types and owners already rule out.

## Tests, comments, files
11. One focused test per stated behaviour and per stated failure case, sized like the neighbouring tests; plus the kinds `code-review` requires for saves, remotes and money. Scratch checks are not committed.
12. Tests check the general rule; never hard-code or special-case test inputs to pass. A wrong or impossible test is reported, not worked around.
13. Comments only where the logic is not obvious, plus contract blocks on important modules (`architecture` R-10). No comments or annotations added to code the task did not change.
14. Temporary files and scripts are deleted before hand-back.

## Finishing
15. When the work and its checks pass: **stop and report.** No extra hardening or review rounds unless the brief asks; extras go in the report as suggestions.
16. "Done" needs one end-to-end check that the feature really works for a player, not just that the code exists.
17. Reviewers report only what affects correctness, safety, money, saves, the stated requirements, or scope. A review is not a list of everything that could be nicer.

## Checks a reviewer can apply
New files the plan did not name · an abstraction or option with one caller · `pcall` or fallbacks around our own pure code · changes outside the owned files · more tests than behaviours · comments on unchanged code · a "while I was here" fix · a stub that renders but does nothing.
