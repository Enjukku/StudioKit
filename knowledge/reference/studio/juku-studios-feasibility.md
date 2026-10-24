---
type: reference
scope: universal
status: draft
updated: 2026-10-24
source: https://github.com/pingdotgg/t3code (main, read 2026-10-24); juku-studios-ideas.md; tools/usage_report.py; J023 design.md
supersedes: []
---
> Author: orchestrator side session · claude-opus-5-5 · default · 2026-10-24

# Juku Studios: feasibility of a T3 Code fork, and a first design

Input: [[reference/studio/juku-studios-ideas]] (the owner's words and direction). Read-only study. Nothing built, cloned or run.
Evidence labels: **source** = read in the repo (link, `~L` = approximate line from the fetched text); **inference** = my conclusion, not stated in the repo; **local** = checked on the owner's PC.
T3 Code state on 2026-10-24: MIT, 29.7k stars, 7,476 commits on `main`, stable `v0.1.2` (2026-10-22), README says "very very early" and "(mostly) not accepting contributions". Stack: TypeScript monorepo, pnpm 12, Node 26.12.1, Effect, apps `server`, `web`, `desktop`, `mobile`, `marketing`, 24 packages.

## Direction after the owner's review (2026-10-24)
Owner, in chat: "I think it would be cool if the orchestrator loaded up a live like agent view mod with the flow map and the studio floor"; "We don't need the obsidian"; "we don't necessarily need T3, but it would be nice if we had that specifically for just creating images"; "the reason why we don't want to use the Codex CLI tool is because when you use that for image gen, it links you to the 2.0 ChatGPT image gen, and we want to use the 2.5."
| Item | Now | Replaces |
| --- | --- | --- |
| Harness | Stay in Claude Code. No T3 Code fork. | Overall recommendation steps 2-3 below |
| Live view | One Claude Code mod (a pane beside the lead chat) with the flow map and the studio floor, opened by the orchestrator | Part 2 views, now drawn in a mod pane |
| Knowledge tab | Dropped | Part 2 knowledge tab |
| Accounts | Switch by hand (a mod cannot change the login) | Item 4 account helper |
| Images | A route to ChatGPT Images 2.5 that saves the file without the owner's hands | Item 4 Codex images |

### How T3 connects Codex, and why it does not give Images 2.5
- Source: T3 runs the Codex binary as an app-server child (`CodexAdapterV2.ts`, package `effect-codex-app-server`) with `CODEX_HOME` set ([CodexManagedRuntime.ts](https://raw.githubusercontent.com/pingdotgg/t3code/main/apps/server/src/provider/CodexManagedRuntime.ts) ~L117). Login: T3 holds the ChatGPT login once and hands an access token to every Codex child through a private named pipe ([CodexManagedTokenBroker.ts](https://raw.githubusercontent.com/pingdotgg/t3code/main/apps/server/src/provider/CodexManagedTokenBroker.ts) ~L147-163), set as a `-c` auth command override (`model_provider="openai_token_sharing"`, CodexManagedRuntime.ts ~L24-29). That is the "connector": one login, many Codex processes.
- Inference: the image comes from the same Codex image tool that `codex exec` uses. T3 adds no image model of its own and no image picker (no image-generation code found in T3, item 4). So T3 gives the same image model as the kit's Codex route (`tools/art/art_refs.py run`, which already runs the Codex desktop app's `codex.exe exec` and copies the file from `CODEX_HOME/generated_images/<session>/`). T3 does not reach Images 2.5 if Codex does not.
- Secondary sources only (no OpenAI release note found): ChatGPT Images 2.5 (API ids `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`) shipped 2026-09-09; one report says the rollout covers Codex; another says Codex has no image model picker, switches on OpenAI's side, and its docs still name `gpt-image-2`. Test it suggests: ask for a transparent-background PNG (gpt-image-2 could not make one).
- The login pain has a local cause, not a T3 one: `codex login` stores the login in `CODEX_HOME` once; every `codex exec` on that home is signed in. The browser route keeps the ChatGPT sign-in in the built-in browser's profile.

### Routes to Images 2.5 with the file saved automatically
| Route | Model | Login | File back | Cost | Verdict |
| --- | --- | --- | --- | --- | --- |
| A. Codex route (`art_refs.py run`), if OpenAI has moved Codex to 2.5 | Whatever Codex uses (unknown) | `codex login` once | Automatic (existing code) | ChatGPT plan | **Test first**: 1 transparent-PNG row; if 2.5, done with no new code |
| B. ChatGPT in the built-in browser (today's default, J009-D16), with an automatic save | 2.5 (the owner chooses Work mode, model 6.1) | Built-in browser keeps the sign-in | Today a download and `art_refs.py save`. Change: the owner gives one standing yes for downloads from chatgpt.com into the job's refs folder, so agents stop asking per batch | ChatGPT plan | **Works today**; the only change is the standing permission, a decision row |
| C. OpenAI Images API with `gpt-image-2.5-*` | 2.5, chosen per call | API key through `tools/keys.py` | Automatic (the API returns the file) | Paid per image, not the plan | **Most reliable**; new script about 150 lines; owner decides on API spend |
| D. T3 Code's Codex connector | Same as A | One login | Automatic | Plan | **No gain over A** |

### Route A test result (2026-10-24, owner's yes in chat)
- Run: `python tools/art/art_refs.py --bible <scratch bible> run <scratch manifest> --limit 1`, one row, no anchors, prompt asks for a truly transparent PNG (a red cartoon treasure chest). Codex session `01a16d0a-c0cf-7362-b21f-57e28710439b`, 52 s, file saved automatically. Test files moved out of the repo afterwards (session scratchpad `codex-image-test/`).
- Measured: 1312 × 1199 RGBA; corners alpha 0; 57.6 % of pixels fully transparent; 97.0 % of the subject's pixels alpha ≥ 250. **Real transparency, not a drawn checkerboard.**
- Provenance (C2PA in the PNG): `softwareAgent` name "ChatGPT", version "gpt-image", claim by "OpenAI Media Service API". No model version number, so the file cannot name 2.0 or 2.5.
- History in `~/.codex/generated_images` (2,374 PNGs): May 2026: 17 images, none with alpha; from 2026-09-22 (the first images after May): real transparency on every day sampled (Sept 34, Oct 107). No images between May and 2026-09-22, so the change date cannot be placed against the 2026-09-09 launch.
- Verdict: **looks like 2.5** by the transparency test the secondary source gives (gpt-image-2 could not make transparent backgrounds); **not proven**, because that rule comes from a blog and the file carries no version. Next check that would settle it: the owner compares this image with a ChatGPT Work-mode image from the same prompt, or OpenAI's Codex changelog names the model.

### Side-by-side with ChatGPT (2026-10-24, owner's yes in chat)
- Same identity and lock pasted in ChatGPT, Work mode, **GPT-6.1 Sol · Medium** (owner: "just do 6.1 med"; page label read before sending: "GPT-6.1 Sol Medium ... Medium, 2 of 6"). Generated in about 1 min; downloaded as `chatgpt-6.1-medium.png` to the session scratchpad.
- Measured: 1374 × 1145 RGBA; corners alpha 0; 57.9 % fully transparent; 96.3 % of subject pixels alpha ≥ 250; C2PA identical to Codex (`softwareAgent` "ChatGPT", version "gpt-image").
- **Owner verdict: "this image that we just got is way higher quality"** (the ChatGPT one).
- Conclusion: Codex does not give the ChatGPT Work-mode image quality. The transparency test does not tell them apart (both make real alpha), and neither does the file's provenance. Route A is out for final references; route B (ChatGPT in the built-in browser) stays the default.
- New blocker (owner): "after you guys download it, I have to like confirm the download onto my PC." The Claude desktop app asks the owner to confirm each browser download; no setting for it exists in the Code tab settings (checked `get_settings`), and it is a safety prompt the owner controls, not the agent. Options: (a) the owner checks whether the prompt offers "always allow for chatgpt.com"; (b) agents use ChatGPT's "Copy image" button and a local script saves the clipboard PNG (no download prompt; untested; uses the owner's clipboard, so one image at a time); (c) route C (Images API) returns files with no browser.

### Clipboard test, option (b) (2026-10-24, owner's yes in chat): FAILED
- Clicked ChatGPT's "Copy image" twice in the built-in browser; the button showed its check mark. A local script (session scratchpad `save_clipboard_png.ps1`, reads the Windows clipboard "PNG" format, falls back to the bitmap) found only text formats: `System.String, UnicodeText, Text, Chromium internal source RFH token, Chromium internal source URL, Locale, OEMText`, and the clipboard still held the owner's earlier text. No image reached the Windows clipboard.
- Inference: the desktop app's browser pane does not pass web image-clipboard writes to the system clipboard. Option (b) is out.
- Side note: before sending, the composer read "GPT-6.1 Sol Medium"; after sending it read "GPT-6.1 Sol High". Which effort ran is not confirmed.
- Remaining ways around the download prompt: (a) a "remember" choice in the prompt, if the owner finds one; (d) the same route in the owner's own Chrome through Claude in Chrome, where downloads follow Chrome's settings and land in Downloads without the desktop app's prompt (untested); (c) the Images API.

### Claude in Chrome download test, option (d) (2026-10-24, owner's yes in chat): PASSED
- Owner: "Let's just do it using my Chrome browser then, because I don't want to be annoyed with having to constantly accept downloads."
- Setup found on the way: the extension first showed only a stale macOS browser; it connected after the owner signed in from the Claude side panel in Windows Chrome with the same account as the desktop app.
- Run: same ChatGPT chat opened in the owner's Chrome → image viewer → Download. The file was in `~/Downloads` within 6 s with no prompt from the agent's side; the owner reported no confirm step. SHA-256 identical to the built-in-browser download (`24f2eef6…`, 1,183,517 bytes): same full-size PNG with alpha. Tab closed afterwards; file moved to the session scratchpad.
- Consequence for the kit (proposal, not applied): the reference-images browser route moves from the built-in browser (`mcp__Claude_Browser__*`) to Claude in Chrome (`mcp__claude-in-chrome__*`) for generate-and-download; `art_refs.py save` already takes the newest file from Downloads. Files to change: `.agents/skills/reference-images/SKILL.md` step 4, `.agents/skills/ui-figma/references/image-generation.md`, the `tools:` lines of the 6 roles that list the built-in browser (art-director, film-director, marketing, modeler, ui-ux-designer, vfx-designer), the 6 job workflows that name it, then `python tools/sync_harness.py`. Needs a decision row with the owner's words.
- **Applied 2026-10-24** on the owner's yes: decision row `J009-D21` in `knowledge/jobs/J009-art-director/decisions.md`; 50 text replacements in 22 source files (reference-images SKILL.md step 4 plus the Codex-fallback note, ui-figma SKILL.md, `references/image-generation.md`, `references/figma-mcp.md`, 9 role files of which 6 swap `mcp__Claude_Browser__*` for `mcp__claude-in-chrome__*`, the 7 job workflows and their README, `rules/company.md` §9 shared-tools row); `sync_harness.py` regenerated `.claude/` and `.codex/` copies. The one-owner-yes-per-batch download rule is unchanged.

### The live-view mod (design, not built)
- Shape: one Claude Code mod, a pane titled "Studio", with two tabs: Floor and Flow. Desktop pane elements are Box, Text, Button, Svg, Markdown and Link; no canvas. Svg source is capped at 131,072 characters per draw, so the floor shows only running agents and the flow map shows one job.
- Data, all read-only: running subagents and workflow agents from the mod API (`$.agent.list()`, agent-spawn events); job folders through `$.fs`; `python tools/usage_report.py --json` through `$.process` on a timer (every 60 s, inference).
- Start: the `orchestration` skill gets one line, "open the Studio pane" (slash command from the mod), at the start of every owner request.
- Limit (inference): a mod sees the agents of its own session live; production chats appear through their transcripts with up to a timer's delay.

### Built (J028, 2026-10-24)
Job: [[jobs/J028-studio-pane/job-card]]. Source: `tools/mods/studio/` (marketplace `tools/mods/.claude-plugin/marketplace.json`).
| Part | What was built | Checked |
| --- | --- | --- |
| Pane | "Studio", tabs Floor and Flow; `/studio [floor\|flow] [job]` and the tool `mcp__studio__open_pane` (the lead cannot type a slash command, so it calls the tool) | `claude plugin validate` pass; `tsc -p` pass; `claude plugin test` 7/7; loaded in the J028 session, the tool opened the pane; the drawn pane not yet seen (owner G3) |
| Floor | One SVG figure per pending, running or waiting agent, in 8 craft rooms; role name, role-colour body, hat per role (feasibility table), model badge from the run or from the role's `tier:` through `kit.json`, effort pips; waiting = dimmed "zz"; a button per agent opens its transcript. Owner's desk: per active job, its Status row, gates with no date, every needs-decision line, an Open button per file | tests (desktop and terminal); real roles rendered |
| Flow | One job: lead sessions + a lane per role, a bar per run (width = wall time, shade = tokens read, red edge past 500k, dashed = running now), gates dashed, gaps over 90 min drawn as breaks; flags: one role 3+ runs in a stage, 3+ reviewer runs within 30 min, idle gaps over 30 min (with a gate in it = wait on the owner), runs past 500k | tests; real J025 data rendered (42 runs, 7 flags) |
| Kit side | `usage_report.py --json` adds per run `id`, `description`, `effort` (from the subagent meta file), `last`, and `job` (the brief's `--job` first, else the first job id; sessions: title first) | `test_usage_report.py` 7/7; gate PASS |

Left (not built): figure art (mascot, a reference-images job); hand-off arrows (job `ledger.md`, exchange notes); bar detail panel (brief, STATUS, `docs_read`); account meters; agents of other sessions show only through the 60 s usage report, not live. Inference: gates are placed in the longest idle gap on their date, because the cards record a date and no time; 66 of 641 runs in the last 7 days name no job id in their brief, so those runs are on no flow map.

## Part 1: verdict per item

| # | Item | Verdict | One line |
| --- | --- | --- | --- |
| 1 | License | **GO** | MIT: fork, rename, change, keep private. Keep the copyright and permission notice. |
| 2 | Windows 11 | **GO, with a limit** | Desktop app and `t3` server install on Windows. The background service does not run on Windows: the app must stay open. |
| 3 | Kit loading | **CONDITIONAL GO** | Claude runs through the Agent SDK with the `claude_code` preset. Skills load (doc). CLAUDE.md, agents, hooks and workflows: probable, not proven. One probe decides. |
| 4 | Accounts and images | **GO for logins, PARTIAL for switching, CONDITIONAL for images** | Uses CLI logins; 2 Claude accounts = 2 instances with 2 config folders; pooled limit view exists. No automatic switch; a Claude thread cannot move between 2 config folders. Codex protocol has image generation; T3 display not verified. |
| 5 | Agent data | **GO** | T3 already parses subagents, workflow agents (model, tokens, phase, transcript folder) and writes per-thread NDJSON event logs. |
| 6 | Upkeep | **RISK (high churn)** | About 15-35 commits a day, several nightlies a day. A deep fork drifts in days. Keep Juku code in its own package and routes. |
| 7 | Size | **L job** | First usable version about 8-10 k lines of new TypeScript plus 26 role figures. Inference. |

### 1. License: GO
- Source: [LICENSE](https://raw.githubusercontent.com/pingdotgg/t3code/main/LICENSE): MIT, "Copyright (c) 2026 T3 Tools Inc." Condition: "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."
- May: fork, rename to Juku Studios, change, use privately, never publish the changes (MIT has no share-back rule).
- Must keep: the `LICENSE` file with T3 Tools' notice in the fork and in any build you give to another person; the third-party notices the repo bundles (`licenses:sync` script in [package.json](https://raw.githubusercontent.com/pingdotgg/t3code/main/package.json)).
- Inference: MIT gives no trademark right. Remove "T3" names, logos and the `t3.codes` update and relay endpoints from the Juku build; add "Juku Studios is based on T3 Code (MIT)" to the About screen.

### 2. Windows 11: GO, with a limit
- Source: [README](https://github.com/pingdotgg/t3code) lists a Windows CLI install (`irm https://t3.codes/install.ps1 | iex`) and the desktop app through winget and scoop; `dist:desktop:win` script in package.json.
- Source: [docs/user/background-service.md](https://raw.githubusercontent.com/pingdotgg/t3code/main/docs/user/background-service.md) ~L76: "Windows background services are not supported." Linux (systemd) and macOS (login agent) only.
- Effect: the server lives only while the desktop app (or a `t3` terminal) is open. Phone access and unattended runs stop when the PC app closes. Inference: acceptable for the owner, who works at the PC; a Windows service (Task Scheduler at log-on) is a small fork add-on if wanted.
- Open Windows bugs today ([issues search](https://github.com/pingdotgg/t3code/issues?q=is%3Aissue+windows)): #24293 Claude provider fails when Claude Code is installed globally with pnpm; #24071 `t3 doctor` EBUSY on the old database; #24067 initial import misgroups conversations on Windows; #24367, #24332, #24165 (SSH, Android emulator, Muse).
- Local: Claude Code 2.1.309 is the native install at `~/.local/bin/claude` (not pnpm), so #24293 does not apply. Codex CLI is not on PATH (T3 installs Codex itself: providers-codex.md ~L7). Node is 24.19.0; building the fork needs Node 26.12.1 (`engines`).

### 3. Kit loading: CONDITIONAL GO
How T3 starts Claude Code (source: [ClaudeAdapterV2.ts](https://github.com/pingdotgg/t3code/blob/main/apps/server/src/orchestration-v2/Adapters/ClaudeAdapterV2.ts), 436 k characters; functions named because the fetch shows no line numbers):
- `@anthropic-ai/claude-agent-sdk ^0.3.276` ([apps/server/package.json](https://raw.githubusercontent.com/pingdotgg/t3code/main/apps/server/package.json)); `query()` in `layerQueryRunner`/`open`.
- `makeClaudeQueryOptions`: `systemPrompt` preset `claude_code` plus T3 runtime text; `cwd` = the thread folder; `pathToClaudeCodeExecutable` = the configured `claude` binary; `env` per instance (holds `CLAUDE_CONFIG_DIR`); `permissionMode`; `mcpServers`; `extraArgs`; `additionalDirectories`. **No `settingSources` in this function.**
- `settingSources: customHome ? ["project", "local"] : ["user", "project", "local"]` appears twice, in `resolveBypassAvailability` and `resolveSubagentPromptCacheTtl`: T3 reads the same three settings layers the CLI uses, to predict the session's permission and cache settings.

| Kit part | Loads in a T3 Claude thread? | Evidence |
| --- | --- | --- |
| `.claude/skills/` | **Yes** | [providers-claude.md](https://raw.githubusercontent.com/pingdotgg/t3code/main/docs/user/providers-claude.md): skills load from the config folder's `skills` and the project's `.claude/skills` (config copy wins a name clash); `userInvocableSkills(cwd)` in `startTurn`/`steerTurn`; `/` menu shows them ([composer.md](https://raw.githubusercontent.com/pingdotgg/t3code/main/docs/user/composer.md) ~L92-110). |
| `CLAUDE.md` + `@` imports (AGENTS.md, claude.md profile) | **Probable** | Project skills need the `project` settings source, and CLAUDE.md loads with the same source. Not stated in T3 docs. |
| `.claude/agents/` (kit roles) | **Probable** | Same `project` source. T3 handles subagent frames, `getSubagentMessages`, `task_started`/`task_notification`. |
| Hooks in `.claude/settings.json` | **Probable** | Same source. T3 reads "Stop hook feedback" from transcripts (`nextClaudeGoal`), so hooks run in its sessions. |
| `.claude/workflows/*.js` | **Probable** | [claudeWorkflowProgress.ts](https://github.com/pingdotgg/t3code/blob/main/apps/server/src/orchestration-v2/Adapters/claudeWorkflowProgress.ts) ~L10-127 parses Workflow tool runs (`local_workflow`). Saved scripts need the project source. |

- Conflict to resolve: the SDK changelog ([CHANGELOG 0.1.0](https://raw.githubusercontent.com/anthropics/claude-agent-sdk-typescript/main/CHANGELOG.md)) says settings files, CLAUDE.md, slash commands and subagents "are no longer loaded automatically" when `settingSources` is not given, and no later entry says this changed. T3's doc says project skills load. Inference: T3 sets the sources another way (for example `extraArgs` from launch arguments, or a part of the file I could not read), or the SDK default changed without a changelog line. **Not proven either way.**
- **Probe (stock T3, 30 min, no fork):** open a thread on the Studio Kit folder and check: (a) ask "quote AGENTS.md §0 row 1" (CLAUDE.md + import); (b) `/` menu shows `orchestration`, `job-feature` (skills, commands); (c) start one `explore` agent (roles) and look for the job pointer that `tools/hooks/subagent_context.py` adds (hooks); (d) run a saved workflow with a dry stage (workflows). If (a)-(d) pass: GO. If not: the fork passes `settingSources: ["user","project","local"]` in `makeClaudeQueryOptions` (one line; inference).
- Second account: with a custom `CLAUDE_CONFIG_DIR`, user-level settings come from that folder, and the project layers are unchanged. The kit keeps its hooks, skills and agents in the project, so both accounts load the same kit. The user-level auto-memory (`<config>/projects/<slug>/memory/`) and transcripts split per account (inference from how `CLAUDE_CONFIG_DIR` works).
- Codex: T3 drives Codex through its app-server protocol ([CodexAdapterV2.ts](https://github.com/pingdotgg/t3code/blob/main/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts); package `effect-codex-app-server`); it adds its own developer instructions (`CodexDeveloperInstructions.ts`). T3 docs do not mention `AGENTS.md` or `.codex/agents/`. Inference: Codex itself reads `AGENTS.md` from the thread folder and `.codex/` project config, as in its own CLI, because T3 only passes `cwd` and the home. Same probe for Codex: ask it to quote AGENTS.md §0 and to name the kit's agent roles.

### 4. Accounts and images
- **Subscription logins: confirmed.** README: "Install and authenticate at least one provider" with `claude auth login` and `codex login`; T3 stores no keys of its own for these. Codex can also sign in to ChatGPT inside T3 (providers-codex.md ~L5-20).
- **Two Claude logins: yes.** providers-claude.md: one Claude instance per account; the second runs `claude auth login` with its own `CLAUDE_CONFIG_DIR`. T3 sets only `CLAUDE_CONFIG_DIR` and leaves `HOME` and the keychain alone (`claudeConfigDirOf`).
- **Switching when one is maxed: partial.**
  - Exists: [docs/user/usage.md](https://raw.githubusercontent.com/pingdotgg/t3code/main/docs/user/usage.md) ~L62-78: Usage → Limits pools all subscription accounts per provider, one bar segment per account, plan and reset time per account; an account with no weekly quota shows 0%. Threads show usage-limit waits with the reset time (providers-claude.md); commit "keep usage-limit wake action visible" (2026-10-24).
  - Limit: "Existing threads can switch only between instances that share a config directory" (providers-claude.md). Two Claude logins need two config folders, so a running Claude thread cannot move to the other account. Codex can: a shared `CODEX_HOME` with a shadow home lets two accounts continue the same threads (providers-codex.md ~L26-70).
  - Missing (inference): an automatic "account A at limit → start the next thread on account B". Fork feature: when a turn ends with a usage-limit result, offer "continue on account B" that opens a new thread on B with a hand-over prompt pointing to the job files. The kit already keeps job state in files (`rules/assistants/claude.md`, session size row), so a new thread loses little.
- **Codex image generation: conditional.** Source: T3's generated Codex protocol ([schema.gen.ts](https://github.com/pingdotgg/t3code/blob/main/packages/effect-codex-app-server/src/_generated/schema.gen.ts)) has `ServerNotification__ImageGenerationFailure` with a `UsageLimitExceededImageGenerationFailure` type. So Codex has an image tool that counts against the plan. Not found: T3 code that shows a generated image (`CodexToolPresentation.ts` handles MCP, browser-use and computer-use tools only; no image-generation issue in the tracker). Probe: in stock T3, ask Codex for one image, check where the file lands and whether the thread shows it. Fork work if it does not show: a renderer for the image item plus a "save to `knowledge/.../refs/`" button (inference: small). Owner check: what the Codex plan allows per week.

### 5. Agent data T3 already records: GO
| Data | Where (source) | Use in Juku |
| --- | --- | --- |
| Subagent lifecycle: `task_started`, `task_progress`, `task_notification`, parent tool id, subagent nodes, `getSubagentMessages(sessionId, agentId)` | `ClaudeAdapterV2.ts` (`openSession`, `updateClaudeSubagentNode`, `handleSdkMessageFrame`, `takeReleasableSubagentFrames`) | Live figures and flow-map bars for hand-run agents |
| Workflow runs: per agent `label`, `state`, `agentId`, `phaseIndex`/`phaseTitle`, `model`, `attempt`, `totalTokens`, `toolCalls`, `durationMs`, `queuedAt`/`startedAt`/`completedAt`, prompt and result preview; run `runId`, `transcriptDir`, `scriptPath`; totals | `claudeWorkflowProgress.ts` ~L19-127 | The flow map for job-workflow stages almost for free |
| Per-thread event log: `[ISO time] NTIVE/ORCH/CANON: <json>`, one file per thread plus `_global`, rotating, deltas dropped, 64 KiB payload cap | [EventNdjsonLogger.ts](https://github.com/pingdotgg/t3code/blob/main/apps/server/src/provider/EventNdjsonLogger.ts) ~L178-188, L756-766; [providers.md](https://raw.githubusercontent.com/pingdotgg/t3code/main/docs/internals/providers.md) | Replay and history for the flow map |
| Token use per turn and per model; pooled limits | `ClaudeTurnTokenUsage.ts`, `claudeUsageLimits.ts`, usage.md | Account meter, bar widths |
| MCP server for outside agents: read projects and threads, start and message threads (read-only by default) | [outside-agents.md](https://raw.githubusercontent.com/pingdotgg/t3code/main/docs/user/outside-agents.md) | A lead chat can ask Juku what is running |
- Gap (inference): T3 sees live only the sessions it started. Sessions started in the Claude desktop app reach Juku through their transcripts (`<config>/projects/<slug>/*.jsonl` and subagent files), which `tools/usage_report.py` already reads.

### 6. Upkeep: RISK
- Source: commits per day sampled on the [commits page](https://github.com/pingdotgg/t3code/commits/main): 2026-08-24: 15, 08-25: 20, 09-25: 35+, 10-23: 8, 10-24: 27. Inference: about 1,000-2,000 commits in the last 2 months.
- Source: [releases](https://github.com/pingdotgg/t3code/releases): 73 pages (about 730 releases); 10 releases on 22-24 Oct alone (nightlies several a day, maintainer previews, stable `v0.1.2` on 22 Oct). A "pre-0.1.0 database" (#24071) and an `orchestration-v2` folder show recent large rewrites.
- Inference, how hard: a fork that edits upstream files (adapter, thread view, settings) gets merge conflicts every week. A fork that adds a separate package (`packages/juku`) and new web routes, and touches upstream files only at a few hook points (route table, sidebar entry, one adapter option, branding strings), can merge upstream weekly with small conflicts. Upstream does not take contributions, so fixes we need stay in our fork.
- Rule for the fork: Juku code in `packages/juku-*` and `apps/web/src/juku/`; a `JUKU-PATCHES.md` that lists every upstream file touched and why; weekly `git merge upstream/main` as a quick-builder task with the gate.

### 7. Size of the first usable version (inference)
| Piece | Rough size | Notes |
| --- | --- | --- |
| Rename and branding, remove T3 endpoints | 1-2 days, mechanical | Strings, icons, update channel, About credit |
| Kit settings fix (only if the probe fails) | 1 line + test | `settingSources` |
| Account helper: "continue on account B" | 0.5-1 k lines | Uses existing pooled limits |
| Kit data reader (read-only): job folders, `usage_report --json`, transcripts, T3 workflow state | 1.5-2 k lines | One Node service in `packages/juku-data` |
| Flow map view | 1.5 k lines | SVG |
| Studio floor view | 1.5-2 k lines | Canvas or SVG, sprites |
| Knowledge tab (note view, backlinks, search, local graph, full graph on request) | 2.5-3 k lines | sigma.js + graphology (WebGL) |
| Agent figures | 1 mascot + 26 hat/prop sets | reference-images pipeline, owner approves the mascot |
| Codex image display (only if the probe fails) | 0.3 k lines | |
- Total: about 8-10 k lines of new TypeScript. Kit size: **L** (G1 direction → G2 integrated proof → G3). Inference: 4-6 build sessions plus reviews.

## Part 2: first design

### Studio floor (front screen)
Purpose: in one look, who works, who waits, and what waits on the owner.
```
+-------------------------------------------------------------------------------+
| JUKU STUDIOS   [Floor] [Jobs] [Knowledge] [Threads]   Claude A ████░ 62%  B ██░░ 18%  Codex ███░ 41% |
+-------------------------------------------------------------------------------+
|  ART ROOM            |  CODE ROOM               |  SOUND & FX ROOM            |
|  art-director        |  architect   feature-b.  |  vfx-designer               |
|   (beret+brush) zz   |  (hard hat)  (wrench)    |  (goggles+spark)  idle      |
|  modeler (working)   |  reviewer (reading)      |  sound-designer (headset)   |
|---------------------+---------------------------+-----------------------------|
|  STAGE ROOM          |  DESIGN ROOM             |  QA & STUDIO ROOM           |
|  environment-d.      |  game-designer (cap)     |  qa-lead (clipboard)        |
|   -----> walking a hand-off note to CODE ROOM                                 |
|---------------------+---------------------------+-----------------------------|
|  OWNER'S DESK:  J024 G1 direction ready   [Open sheet] [Approve rev 3] [Ask]  |
|                 J023 needs-decision: reviewer limit   [Open digest]           |
+-------------------------------------------------------------------------------+
```
- One room per craft group (art, code, sound and effects, stage, design, QA and Studio, data and market). A figure appears only while its agent runs or waits; idle roles are not drawn, so the floor shows load, not the roster.
- Figure state: working (prop moves), reading (book), waiting on a peer (sits, a line to the peer), blocked (red mark), done (walks out). A hand-off is a figure carrying a note between rooms, about 2 s, once.
- Owner's desk: every open gate and every `needs-decision` from the job cards, each with the file link. The buttons open the file; "Approve" writes nothing in v1 (approval stays in chat, `AGENTS.md` §1: approval bound to a revision). Inference: a later version can paste "G1 approved rev 3" into the lead chat for the owner to send.
- Top bar: one meter per account (T3 pooled limits), click → that account's reset time.

### Flow map (job view)
Purpose: see repeated passes, reviewer pile-ups and waits in one job. Matches the J023 shape ([[jobs/J023-flow-speed/design]]: joint needs meeting, carried verdicts, one direction step).
```
J024 effect "lightning slash"   size M   tokens 1.9 M   wall 3 h 10 m   [stage: build r1]
time ─────────────────────────────────────────────────────────────────────────────▶
lead       ▓▓ direction ▓                ▓ merge ▓                      ▓ synth ▓
vfx        ·            ▓▓ needs r1 ▓▓  ▓▓▓▓▓▓▓ build ▓▓▓▓▓▓   ▓ repair ▓
sound      ·            ▓▓ needs r1 ▓   ▓▓▓▓ build ▓▓▓▓
animator   ·            ▓ needs r1 ▓    ▓▓ timing ▓
art-dir    ·                                             ▓ review ▓  ░ carried ░
qa-lead    ·                                             ▓ review ▓  ▓ review ▓
           ┆ G1 approved rev 2                                                ┆ G3
           arrows: vfx ──note──▶ sound (cue ids)      ⚠ wait: 41 min on owner
```
- Lane per role; bar per agent run; bar width = wall time; bar height or shade = tokens (from `usage_report --json` `read`/`out`, or T3 `totalTokens`); repair rounds stacked and labelled r1, r2.
- Dashed vertical lines = owner gates with the approved revision. A carried review verdict (J023 rule B4) is a hollow bar, so re-runs that were skipped are visible.
- Arrows = hand-off notes and tickets (job `ledger.md`, exchange notes). Flags: same role 3+ runs in one stage; 3+ reviewers in one round; gap > 30 min waiting on the owner; a run past the 500 k context mark (owner J023-D1).
- Click a bar → side panel: brief path, hand-back STATUS line, `docs_read` list (each a link into the Knowledge tab), transcript link, model and effort.

### Agent figures
- One original mascot: a small round "ink-drop" studio worker with stubby arms, big eyes and no mouth (inference: simple to read at 32 px, unlike Anthropic's logo or any Anthropic mascot; the art-director checks for any likeness before G1). Made with the kit's reference-images pipeline; the owner approves the base mascot first, then the hat sheet.
- Per role: a hat plus a prop (the identifier) and the body tint from the role's `color:` key. Local check: 25 of 26 roles in `.agents/roles/` have `color:`, but only 8 colours exist (green 6, cyan 4, orange 4, purple 3, yellow 3, blue 2, pink 2, red 1), so colour groups roles and hat plus prop tell them apart.

| Role | Hat | Prop |
| --- | --- | --- |
| orchestrator (lead) | conductor's cap | baton |
| game-designer | backwards cap | dice |
| art-director | beret | brush |
| architect | hard hat | blueprint roll |
| feature-builder | welding mask up | wrench |
| quick-builder | headband | screwdriver |
| reviewer | reading glasses on head | magnifier |
| qa-lead | safety helmet | clipboard |
| modeler | sculptor's cap | clay block |
| character-rigger | miner's lamp | bone |
| animator | flip-book visor | flip book |
| vfx-designer | goggles | spark wand |
| sound-designer | headphones | microphone |
| environment-designer | explorer hat | tree sapling |
| ui-ux-designer | pencil behind ear | phone frame |
| film-director | director's beret | clapperboard |
| (others: analyst, marketing, trend-scout, progression-designer, live-ops-designer, performance-engineer, studio-operator, researcher, doc-keeper, explore) | proposed at G1 | |
- Above the figure: role name (and the job id when two jobs run). Badge on the chest: model (O / S / H for Opus / Sonnet / Haiku, C for Codex models) and the effort as 1-4 pips. Data: role file `model:` and the actual model from the transcript (the transcript wins when they differ, and the badge shows a small warning).

### Knowledge tab (Obsidian-like)
```
+------------------+-------------------------------------------+--------------------+
| Search [......]  |  # J023 design: the shortened job flow    |  Local graph (1-2  |
| Filters:         |  type: job · scope: universal · active    |  hops)  ○──○       |
|  type  [job ▾]   |  ...rendered markdown, [[links]] live...  |        ○─●─○       |
|  scope [all ▾]   |                                           |          ○         |
|  job   [J023 ▾]  |                                           |  Backlinks (14)    |
| Tree / recent    |                                           |  - rules/company   |
|                  |  [Open full graph]                        |  - jobs/J022/...   |
+------------------+-------------------------------------------+--------------------+
```
- Scope: the kit's `knowledge/` only in v1 (1,611 notes, 14,249 `[[links]]`). Read-only: the tab never edits a note (kit rule: `knowledge/generated/` is tool-owned; authored notes have authors).
- Render plan (from the ideas file, with reasons):
  1. Default is the local graph: the open note plus 1-2 hops, usually under 100 nodes. SVG or canvas is fast at this size.
  2. Filters by `type`, `scope`, `status` (superseded hidden by default), job and role, from frontmatter.
  3. Full graph only on request, WebGL (sigma.js on graphology). Inference: 1.6 k nodes and 14 k edges is small for WebGL (it stays smooth well past 10 k nodes); the slow part in Obsidian is the live force layout, not the drawing.
  4. Layout computed once, not live: run ForceAtlas2 in a worker when the `tools/kb_index.py` output changes, cache x/y per note in a JSON file outside the repo, keyed by an index hash. Opening the full graph then only draws.
  5. Edges hidden below a zoom level; labels only for hubs and the hovered node.
- Link to the flow map: from a bar, "notes this run read" (`docs_read`) highlights those notes; from a note, "runs that read this" lists the agent runs.
- The owner's personal Obsidian vault: same reader can open a second folder as a separate vault, never mixed with the kit (open question Q4).

### Where each view gets its data (all read-only)
| View | Data | Source path or command |
| --- | --- | --- |
| Floor: who is running | Live subagents and workflow agents | T3 adapter state (section 5); for outside sessions, newest transcript lines |
| Floor: owner's desk | Open gates, needs-decision, digest | `knowledge/jobs/active.md`, each `knowledge/jobs/<job>/job-card.md`, `decisions.md` |
| Floor: account meters | Limits per account | T3 Usage → Limits |
| Flow map: lanes and bars | Agent runs, model, calls, context median and peak, tokens read and out, workflow id | `python tools/usage_report.py --json --root <repo>` (keys `sessions[]`, `agents[]` with `type`, `workflow`, `model`, `read`, `out`, `peak`, `flags`); T3 workflow state for live runs |
| Flow map: stages, gates, revisions | Gate rows, approved revisions | job `decisions.md`, `job-card.md`, `direction.md` |
| Flow map: arrows | Tickets and notes | job `ledger.md`, exchange notes, `crew.md` (role → agent id) |
| Flow map: bar detail | Brief, STATUS, `docs_read`, transcript | hand-back files in the job folder; `<config>/projects/<slug>/` transcripts for both accounts (`usage_report.py --projects-dir` per account) |
| Figures | Role, colour, pinned model | `.agents/roles/*.md` frontmatter (`color:`, `model:`) |
| Knowledge tab | Notes, frontmatter, links | `knowledge/**/*.md`; `python tools/kb_index.py` output; cached layout JSON |
- Needed on the kit side (inference, small): `usage_report.py` reads one projects folder per call, so Juku calls it once per account folder, or it gets a repeatable `--projects-dir`.

## Overall recommendation
**GO, in three steps; stop after step 1 if a probe fails badly.**
1. **Probes on stock T3 Code (no fork, about 1 hour of the owner's time with one agent):** install the Windows desktop app; add Claude account B with its own config folder; run the item 3 probe (kit loading, Claude and Codex) and the item 4 image probe. Result decides whether the fork needs the `settingSources` line and the image renderer.
2. **Thin fork, Juku code apart:** rename, the account helper, the kit data reader, then the flow map first (it gives the most value for J023-style tuning and uses data that already exists), the knowledge tab second, the studio floor third (it needs the figure art).
3. **Upkeep:** weekly upstream merge as a small task with the gate; `JUKU-PATCHES.md` lists every touched upstream file.
- Why not a deep fork: upstream changes 15-35 commits a day and rewrites core parts (`orchestration-v2`). Why not build from zero: T3 already solves the hard parts (SDK sessions, subagent and workflow parsing, two logins, pooled limits, Windows desktop packaging).

## Questions for the owner
| # | Question | Why it matters |
| --- | --- | --- |
| Q1 | May one agent run the 1-hour probe on stock T3 Code (install the Windows desktop app, add Claude account B)? | Decides item 3 and item 4 before any build. |
| Q2 | Is it OK that the Juku server runs only while the desktop app is open (no Windows background service)? | A log-on task is extra work; phone access needs the PC app open. |
| Q3 | When account A hits its limit: start a new thread on B with a hand-over prompt (possible), or must the same thread continue (not possible for Claude with two config folders)? | Shapes the account helper. |
| Q4 | Knowledge tab: only the kit's `knowledge/`, or also your personal Obsidian vault as a second vault? | Scope and graph size. |
| Q5 | Which first: flow map, knowledge tab or studio floor? (Proposal: flow map.) | Build order. |
| Q6 | Mascot: approve the "ink-drop worker" idea for reference images, or another base shape? | Starts the figure art. |
| Q7 | Will Juku stay private to you, or will you give builds to other people? | Private needs only the MIT notice; shared builds need the full rename away from T3 marks. |
| Q8 | What does your Codex plan allow for image generation per week? | Whether Codex can replace the browser route for reference images. |
| Q9 (2026-10-24) | May one agent run 1 transparent-PNG row through `art_refs.py run` to see whether Codex now gives Images 2.5? | Route A costs no new code if it passes. |
| Q10 (2026-10-24) | If Codex is still on 2.0: a standing yes for chatgpt.com downloads into refs (route B), or paid API calls (route C)? | Picks the image route. |
| Q11 (2026-10-24) | Build the Studio pane mod (floor + flow map) as a job now? | Starts the live view. |
