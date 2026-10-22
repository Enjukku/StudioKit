---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J017-T01 (URLs below)
supersedes: []
---

> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-21

# What Anthropic says about prompting Opus 5.5, Sonnet 5.5, Haiku 5.5, and what a Claude Code subagent loads

Scope: facts from Anthropic pages, read 2026-10-21. No comparison with the kit (the lead does that). "Inference" marks my own reading. Quotes are under 15 words.

URL keys (all fetched 2026-10-21; pages carry no per-page date):
- BP = https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- OPUS55 = .../prompt-engineering/prompting-claude-opus-5-5
- SON55 = .../prompt-engineering/prompting-claude-sonnet-5-5
- HAI55 = .../prompt-engineering/prompting-claude-haiku-5-5
- OPUS5 = .../prompt-engineering/prompting-claude-opus-5
- EFF = https://platform.claude.com/docs/en/build-with-claude/effort
- STEER = https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost
- CC-SUB = https://code.claude.com/docs/en/sub-agents
- CC-MEM = https://code.claude.com/docs/en/memory
- CC-COST = https://code.claude.com/docs/en/costs
- CC-CTX = https://code.claude.com/docs/en/context-window
- CC-MCP = https://code.claude.com/docs/en/mcp
- CC-SKILL = https://code.claude.com/docs/en/skills

BP structure (verified): model-specific guidance first (table linking one page per model), then techniques for all current models, then migration. BP says a technique that names one model is "measured on that model" and should be re-checked on your own evals before use on another (BP, "General principles").

## 1. General guidance (all current models)

| # | Advice | Quote | Source |
| --- | --- | --- | --- |
| 1.1 | Be explicit; say it if you want extra beyond the task. Use a "new colleague" test: if a colleague with no context would be confused, so will Claude. | "brilliant but new employee who lacks context" | BP, "Be clear and direct" |
| 1.2 | Give the reason behind a rule; Claude generalizes from it. Example: not "NEVER use ellipses" but say the text goes to a text-to-speech engine. | "Claude can generalize from the explanation." | BP, "Add context to improve performance" |
| 1.3 | Examples are among the most reliable steering tools. Make them relevant, diverse, and wrapped in `<example>` tags. 3-5 examples. | "Include 3-5 examples for best results." | BP, "Use examples effectively" |
| 1.4 | XML tags separate instructions, context, examples, inputs. Use consistent, descriptive tag names; nest for hierarchy. | "reduces misinterpretation" | BP, "Structure prompts with XML tags" |
| 1.5 | A one-sentence role in the system prompt focuses behavior and tone. | "Even a single sentence makes a difference" | BP, "Give Claude a role" |
| 1.6 | Say what to do, not what not to do (formatting example: ask for flowing prose instead of "no markdown"). | "Tell Claude what to do instead of what not to do" | BP, "Control the format of responses" |
| 1.7 | Prompt style leaks into output style: a prompt with less markdown gets less markdown back. | (paraphrase) | BP, "Control the format of responses" item 3 |
| 1.8 | Newer models are precise instruction-followers on tools: "can you suggest changes" gets suggestions, not edits. Say "change this function". For default action, add a `<default_to_action>` block. | "benefit from explicit direction to use specific tools" | BP, "Tool usage" |
| 1.9 | Independent tool calls run in parallel by default; a short `<use_parallel_tool_calls>` block raises it to about 100 percent. | "boost this to about 100 percent" | BP, "Optimize parallel tool calling" |
| 1.10 | Subagent orchestration is native; watch for overuse and add a when/when-not paragraph if needed. | "do so proactively without requiring explicit instruction" | BP, "Subagent orchestration" |
| 1.11 | Tell Claude about compaction or file-based memory so it does not stop early near the context limit; save state to files. | "do not stop tasks early due to token budget concerns" | BP, "Context awareness and multiwindow workflows" |
| 1.12 | Multi-window work: different prompt for the first window, tests in a structured file, init script, git for state. A fresh window can beat compaction because models find state in the filesystem; be prescriptive about how to start ("Review progress.txt, tests.json, and the git logs"). | (paraphrase) | BP, "Workflows across multiple context windows" |
| 1.13 | For overeagerness (extra files, abstractions, flexibility) add a minimal-scope block: no features, docs, validation or helpers beyond the task. Page ties this to Opus 4.5/4.6. | "Avoid over-engineering." | BP, "Overeagerness" |
| 1.14 | Ground code answers: read the file before claiming anything about it (`<investigate_before_answering>`). | "Never speculate about code you have not opened." | BP, "Minimizing hallucinations in agentic coding" |
| 1.15 | Confirm before destructive or shared-state actions; page gives a sample block (force-push, rm -rf, posting externally). Page ties it to Opus 4.6. | "ask the user before proceeding" | BP, "Balancing autonomy and safety" |
| 1.16 | Self-check ("verify your answer against test criteria") catches errors, except on Opus 5 (see 2.1). | "catches errors reliably, especially for coding and math" | BP, "Leverage thinking..." bullet list |
| 1.17 | Prefer general instructions ("think thoroughly") over a hand-written step plan; Claude's reasoning often exceeds what a human would prescribe. | "Prefer general instructions over prescriptive steps." | BP, "Leverage thinking..." |
| 1.18 | Prefilled last assistant turn is no longer supported from the 4.6 models on (400 error); use direct instructions, structured outputs or tools. | "return a 400 error" | BP, "Migrating away from prefilled responses" |
| 1.19 | Do not ask the model to write its reasoning in the reply on Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5; it "may be declined" (refusal category `reasoning_extraction`). Use thinking instead. Short explanations of the answer are still fine. | "may be declined" | BP, "Leverage thinking..." manual-CoT bullet; OPUS55 "Safeguard refusals"; SON55 "Safeguard refusals" |
| 1.20 | Keep thinking blocks and history append-only on Opus 5.5, Sonnet 5.5, Haiku 5.5: editing earlier turns or rebuilding `system`/`tools` mid-conversation errors or drops thinking. Put new instructions in a mid-conversation system message or the newest turn. | "results in an error" | BP, "Migration considerations" item 7; HAI55 intro Note |

## 2. Per model

### 2.1 Opus 5.5 (OPUS55; plus OPUS5 where OPUS55 says "remain a reasonable starting point")

Intro facts (OPUS55, intro): output more than 30 percent faster than Opus 5, usually fewer tokens. "Existing Claude Opus 5 prompts should perform well without changes."

| # | Advice | Quote | Source |
| --- | --- | --- | --- |
| 2.1.1 | Effort is the main control. Default is `medium` (Opus 5 default was `high`). Set it explicitly and sweep on your own evals; level names do not match across models. Anthropic's test: 5.5 at `medium` matches or beats Opus 5 at `high` on coding. | "Start at `medium`, the default on Claude Opus 5.5" | OPUS55, "Calibrate effort"; EFF, "Recommended effort levels for Claude Opus 5.5" |
| 2.1.2 | At a given level 5.5 thinks more per turn than Opus 5, especially at `xhigh` and `max`. Reserve those for measured gains. To get less thinking, lower effort first; it works "more reliably than prompt instructions". | "Reserve `xhigh` and `max`" | OPUS55, "Calibrate effort" |
| 2.1.3 | Thinking is always on and cannot be disabled (400 error at every effort level). | "thinking is always on" | BP, "Leverage thinking..."; EFF, Opus 5.5 section |
| 2.1.4 | If you ran with thinking off: start at `low`; delete prompt lines that make it write reasoning in the reply; delete any "do not think" rule; read response by block type. A line like "Answer directly without deliberating." can cut thinking further; measure quality. | "Start at `low` effort and measure." | OPUS55, "Prompts written for thinking disabled" |
| 2.1.5 | Chat system prompts: consider removing "think carefully before answering" lines; in the page's chat test, replies started sooner with no clear quality loss. | "consider removing them for Claude Opus 5.5" | OPUS55, "Thinking instructions in chat system prompts" |
| 2.1.6 | Optional two-sentence block makes it treat earlier answers as settled on later turns (less thinking). Skip it where re-examination is wanted (long analyses, agentic tasks). | "treat that answer as done" | OPUS55, same section |
| 2.1.7 | Long tasks: a text-only end of turn (`end_turn`) after a progress update can stop an unattended loop. Treat it as a report, keep a checklist, send a short continue message, cap at two or three automatic continuations. | "Treat a text-only end of turn as a report" | OPUS55, "Unattended agentic runs" |
| 2.1.8 | A system-prompt paragraph naming the early stops to avoid (summary that announces the next step, offer to continue, decision list, "good place to report") reduces them. Add it from the first request; adding later invalidates thinking blocks. Leave out for human-in-the-loop apps. Expect more tool calls and tokens. | "responsive to instructions that name the specific kinds of early stop" | OPUS55, "Unattended agentic runs" |
| 2.1.9 | Progress updates come back as `thinking` blocks, empty at default `display`; a client rendering only `text` looks silent. Set `display: "updates"` (beta). Ask for updates at set points in the system prompt if wanted. | "can look silent during a long agentic turn" | OPUS55, "User-facing progress updates" |
| 2.1.10 | Multiagent harnesses: it responds strongly to elapsed-time signals (`elapsed 340s / 1200s`) and finishes sooner with better parallelization. Budget is advisory; keep your own timeout; quality may drop slightly under time pressure. | "highly responsive to information about elapsed time" | OPUS55, "Time signals for multiagent harnesses" |
| 2.1.11 | Multiapp work: it "tends to get to work quickly"; one sentence telling it to explore broadly before acting raised success in the page's tests. Keep untrusted content out of searched records. | "explore broadly with tool calls" | OPUS55, "Explore context in multiapp workflows" |
| 2.1.12 | Mark pasted text with tags carrying a random ID, plus one system-prompt note, so pasted instructions are not followed. May make it slightly more cautious. | (paraphrase) | OPUS55, "Mark pasted text in user messages" |
| 2.1.13 | Frontend: general "avoid generic AI look" mostly swaps one default for another; name the specific patterns to avoid. | "responds well to instructions that name specific patterns" | OPUS55, "Frontend design defaults" |
| 2.1.14 | Visual input: re-test old scaffolding; crop/zoom tools still add accuracy on the densest inputs. | (paraphrase) | OPUS55, "Tools for complex visual inputs" |
| 2.1.15 | From OPUS5 (the 5.5 page points back to it): do not write verification instructions ("include a final verification step", "use a subagent to verify"); they cause over-verification. "Remove these instructions rather than rewriting them" (BP). Same for "double-check your answer". | "remove them" | OPUS5, "Task scope and over-verification" and "Self-correction"; BP, "Leverage thinking..." |
| 2.1.16 | From OPUS5: it delegates to subagents more readily than prior models. Give explicit when-to-delegate guidance or deterministic caps (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, `max_budget_usd`). Sample: do not delegate what you can finish in a handful of tool calls; do not use subagents to double-check. | "delegates to subagents more readily" | OPUS5, "Controlling subagent spawning"; BP, "Subagent orchestration" |
| 2.1.17 | From OPUS5: it can widen scope; for narrow tasks add a scope paragraph (deliver what was asked, make routine calls yourself, say so in one sentence if the request looks mistaken). | "constrain scope explicitly" | OPUS5, "Task scope and over-verification" |
| 2.1.18 | From OPUS5: narration and written files run long; effort does not reliably shorten visible replies. Prompt for length and cadence; positive examples of the style beat "don't" lists. | "prompt for it explicitly" | OPUS5, "Response length and verbosity", "User-facing progress updates", "Written deliverable length" |
| 2.1.19 | From OPUS5: give the complete task spec up front; it "performs best when given the complete task specification up front and left to run". Ask for all findings, then filter; "only report high-severity" is followed literally. | (paraphrase) | OPUS5, "Capability improvements" |

Page silent for Opus 5.5 on: CAPS/MUST wording, prompt length, XML tags, few-shot counts (it defers to BP).

### 2.2 Sonnet 5.5 (SON55)

Intro (SON55): "Existing Claude Sonnet 5 prompts should perform well without changes." For the hardest long-horizon work "an Opus model is the better choice."

| # | Advice | Quote | Source |
| --- | --- | --- | --- |
| 2.2.1 | Effort is recalibrated vs Sonnet 5; run a fresh sweep. Default `high` on the API. Agentic coding and multistep tool use: start `medium` for well-specified tasks, `high` for harder or longer ones. Chat/latency-sensitive: `medium` or `low`. | "Start at `high`, the default on the Claude API" | SON55, "Calibrate effort"; EFF, Sonnet 5.5 section |
| 2.2.2 | `xhigh`/`max` only where measured gain. At `low` it can skip verifying a change; at `low` and `medium` on long agentic tasks it is more likely to stop and check in. | "more likely to stop and check in with the user" | SON55, "Calibrate effort" |
| 2.2.3 | To think less, lower effort. Asking in the system prompt to think less "doesn't reliably reduce its thinking". From `medium` up it thinks briefly before almost every reply, even a greeting. | "Asking it in the system prompt to think less" | SON55, "Calibrate effort"; STEER, "Steering how often Claude thinks" Note |
| 2.2.4 | Lowest thinking setting is `thinking: {"type": "between_tools"}` (effort `high` or lower; 400 at `xhigh`/`max`; no mid-conversation effort change with it). With it, remove any "do not think" instruction (raises chance of internal XML tags in output). | "remove any instruction that tells the model not to think" | SON55, "Running without up-front thinking" |
| 2.2.5 | Two-paragraph system prompt to keep it working at `low`/`medium` ("Keep working until everything the user asked for is done...") and to stop and report without extras. Raises cost at those levels. Does not replace your own rules on risky actions. | "only stop to ask when you can't go on" | SON55, "Steer initiative and scope" |
| 2.2.6 | It tends to add tests, docs and small files on its own at every effort level. Second paragraph alone ("Don't add features, tests, files, docs or refactors that weren't asked for") limits this. | "Don't add features, tests, files, docs or refactors" | SON55, "Steer initiative and scope" |
| 2.2.7 | At `xhigh`/`max` it starts its own review rounds, sometimes with reviewer subagents. A paragraph forbidding that cut session cost by about a third at `max` in the page's coding test, no quality change. | "don't launch reviewer sub-agents unless the user asked" | SON55, "Steer initiative and scope" |
| 2.2.8 | Open-ended asks ("show me what you can do") can start building; add a rule: ideas/options/plan means give that and stop. | "give them that and stop" | SON55, "Steer initiative and scope" |
| 2.2.9 | JSON answers to multistep reasoning tasks: add "Think the problem through before you answer." at the end of the system prompt with adaptive thinking; or use `xhigh`. Do not use `between_tools` for tool-less reasoning. | "Think the problem through before you answer." | SON55, "Reasoning tasks with JSON output" |
| 2.2.10 | Verification at `low`: if changes are reported done with no test or build output, add the "run a real check that exercises the change" paragraph. Slightly higher cost. | "run a real check that exercises the change" | SON55, "Verification on coding tasks" |
| 2.2.11 | Chat/knowledge work: remove "minimize tool calls" language; add a rule to search for specifics that may have changed, even when confident. | "even when you feel confident" | SON55, "Tool use in chat and knowledge work" |
| 2.2.12 | Mid-turn user input: never put user text inside `tool_result`; deliver it as a user turn; keep harness reminders in a separate system message; do not add your own token countdown after every tool result (the model may treat it as injection). Frequent harness text after tool results can be misread as injection. | "Never put user text inside a `tool_result` block." | SON55, "Mid-turn user messages" |
| 2.2.13 | Tool names: it occasionally calls `bash` for `Bash` or renames a parameter. Harness should accept an unambiguous match or return `is_error: true` with the exact name. | "Accept the call when the match is unambiguous" | SON55, "Tolerant tool-call handling" |
| 2.2.14 | Progress updates and visual inputs: same pattern as Opus 5.5 (2.1.9, 2.1.14). A one-turn reminder ("The user hasn't heard from you in a while") after about five silent steps shortened silent stretches. | (paraphrase) | SON55, "User-facing progress updates", "Tools for complex visual inputs" |

Page silent for Sonnet 5.5 on: CAPS/MUST wording, prompt length, XML tags, role prompts (defers to BP).

### 2.3 Haiku 5.5 (HAI55)

Intro (HAI55): "Existing Claude Haiku 4.5 prompts should perform well without changes." Haiku 5.5 is "the first Haiku model with effort levels."

| # | Advice | Quote | Source |
| --- | --- | --- | --- |
| 2.3.1 | Effort replaces the 4.5 thinking budget. Default `medium` (start there, including agentic coding). `low` = cheapest, for chat, short tool tasks, simple high-volume requests; in long agent prompts it more likely skips a search, stops early or skips a check. `high` for knowledge work, longer agent tasks, strict instruction following. `xhigh`/`max` only for measured gain, and compare against Sonnet 5.5. | "Start here for most work, including agentic coding." | HAI55, "Use effort to control thinking"; EFF, Haiku 5.5 section |
| 2.3.2 | Thinking is on by default and counts toward `max_tokens` (up to 128,000). "Answer directly" in the prompt did not stop it from thinking in Anthropic's test; lower effort instead. `thinking: {"type": "disabled"}` works at `low`/`medium`/`high` only. | "didn't stop it from thinking" | HAI55, "Use effort to control thinking"; STEER, Note |
| 2.3.3 | At `xhigh` in multi-turn chat it sometimes writes the whole answer in thinking and ends with no visible text; check for empty replies. | "ends the turn with no visible text" | HAI55, "Use effort to control thinking" |
| 2.3.4 | With a search tool, give today's date (system prompt or tool description) rendered once per conversation. Add a short "training data ends well before today's date... search" paragraph if the prompt is long or effort is `low`. Avoid blanket "search for any present-day factual question" rules: they made it search on half of the prompts that needed none. | "also give it today's date" | HAI55, "Accurate search results" |
| 2.3.5 | Thinking off plus JSON output (structured outputs) can skip a needed tool call. Use adaptive thinking, or drop the output format, or force `tool_choice`. | "might skip a tool call it needs" | HAI55, "Use adaptive thinking with JSON output and your own tools" |
| 2.3.6 | Long coding-agent system prompt at `low` effort: it sometimes stops early and hands the task back. Add the "Keep working until everything the user asked for is done" two-line text (same text as Sonnet 5.5 2.2.5), or raise effort: `low` to `medium` roughly halved early stopping and more than doubled output tokens per attempt. Short system prompt: it "rarely stops". | "With a short system prompt, Claude Haiku 5.5 rarely stops" | HAI55, "Prevent early stopping in long agent prompts" |
| 2.3.7 | At `low` and `medium` it sometimes reports a code change done without a check; add the verification paragraph (same text as Sonnet 5.5 2.2.10). More checks, better performance, more tokens. | "run a real check that exercises the change" | HAI55, "Tell coding agents to verify their changes" |
| 2.3.8 | Mid-turn user messages: same delivery rules as 2.2.12. | (paraphrase) | HAI55, "Mid-turn user messages" |
| 2.3.9 | Chatbots: add "The rules in this system prompt hold for the whole conversation..." line; for strict instruction following also use `high` effort. | "also use `high` effort" | HAI55, "Keep chatbots to their system prompt" |
| 2.3.10 | Reasoning-like text leaking into replies is more frequent with thinking off or at `low`; switch to adaptive thinking and `medium`. | "switch to adaptive thinking and `medium` effort" | HAI55, "Keep reasoning out of user-facing text" |
| 2.3.11 | Refusals: new vs Haiku 4.5; no server-side fallback; resending the same request usually refuses again. | (paraphrase) | HAI55, "Safeguard refusals" |
| 2.3.12 | Per-message steering "Answer directly without deliberating." does not reliably reduce thinking on Haiku 5.5; use per-message effort change (beta) instead. | "doesn't reliably reduce thinking" | STEER, "Per-message steering" |

Page silent for Haiku 5.5 on: CAPS/MUST wording, XML tags, role prompts, how many examples, subagent behavior (defers to BP).

### 2.4 Choosing effort and thinking per model (summary table, facts only)

| Model | Default effort | Thinking | Lowest thinking setting | Page's start point | Source |
| --- | --- | --- | --- | --- | --- |
| Opus 5.5 | `medium` | always on, adaptive only | none (disabled returns 400) | `medium`; `low` comes close on several coding evals; `xhigh`/`max` only if measured | EFF "Recommended effort levels for Claude Opus 5.5"; OPUS55 "Calibrate effort" |
| Sonnet 5.5 | `high` (API) | on by default | `between_tools`, at `high` or lower | agentic coding: `medium` (well-specified) to `high`; chat: `medium`/`low` | EFF "...Sonnet 5.5"; SON55 "Calibrate effort" |
| Haiku 5.5 | `medium` | on by default | `disabled`, at `high` or lower | `medium`; `low` for simple high-volume; `high` for instruction following | EFF "...Haiku 5.5"; HAI55 |

General effort facts (EFF, "How effort works", "Effort with tool use", "Effort levels"):
- Effort affects all output tokens, including tool calls; lower effort means fewer, terser tool calls and less preamble ("Lower effort also means fewer and terser tool calls.").
- `low` is described as for "Simpler tasks that need the best speed and lowest costs, such as subagents." (EFF effort table; this is the page's own subagent example.)
- Effort is "a behavioral signal, not a strict token budget."
- Changing top-level effort between requests invalidates the prompt cache; per-message effort (beta, header `mid-conversation-output-config-2026-07-01`) keeps it.
- Thinking is decided per request; follow-up requests that only process tool results can skip thinking at any level (STEER, "Effort levels").
- Order of levers: set effort first, add prompt guidance only if needed (STEER, "Steering how often Claude thinks"). Prompt steering "might reduce quality" on reasoning tasks (STEER, Warning).
- BP, "Leverage thinking...": "which can occur with large or complex system prompts" thinking triggers more often than wanted; the page gives a "respond directly when in doubt" line. (For Sonnet 5.5 and Haiku 5.5 that line is not reliable, see 2.2.3 and 2.3.2; inference.)

## 3. Advice that bears on context size

| # | Topic | What the pages say | Quote (under 15 words) | Source |
| --- | --- | --- | --- | --- |
| 3.1 | Instruction length (Claude Code files) | Target under 200 lines per CLAUDE.md; longer files cost context and reduce adherence. Specific and concise instructions are followed more consistently. | "Longer files consume more context and reduce adherence." | CC-MEM, "Write effective instructions"; "CLAUDE.md vs auto memory" |
| 3.2 | Instruction length (API prompts) | No stated line or token limit for API system prompts on the 5.5 pages. They say large or complex system prompts can raise how often adaptive thinking triggers, and that a long coding-agent system prompt raises early stopping on Haiku 5.5 at `low`. | "which can occur with large or complex system prompts" | BP, "Leverage thinking..."; HAI55, "Prevent early stopping in long agent prompts" |
| 3.3 | Long documents | Put long inputs (20k+ tokens) at the top, query and instructions after. Queries at the end improve quality by up to 30 percent in tests. Wrap each in `<document>` with `<source>`; ask for quotes first. | "Put long-form data at the top" | BP, "Long context prompting" |
| 3.4 | Examples | 3-5 relevant, diverse, tagged examples; examples also shape how Claude reasons inside thinking. Cost angle not stated. | "Include 3-5 examples for best results." | BP, "Use examples effectively"; "Leverage thinking..." |
| 3.5 | Repetition | OPUS5 says a conciseness instruction in a long system prompt can be paired with a short reminder near the end. HAI55 says a per-conversation rules line can be added. Page gives no general advice to repeat rules. | "pair the instruction with a short reminder near the end" | OPUS5, "Response length and verbosity" |
| 3.6 | Emphasis words (CAPS, MUST, NEVER, CRITICAL) | For Opus 4.5 and 4.6 (more responsive to the system prompt) aggressive language can now overtrigger tools; soften "CRITICAL: You MUST use this tool when..." to "Use this tool when...". Related: "Replace blanket defaults", "Remove over-prompting", "If in doubt, use [tool]" causes overtriggering. The 5.5 model pages do not repeat this. The page's own sample blocks still use MUST/NEVER/DO NOT in places (inference: emphasis is not banned, only tuned per model). | "The fix is to soften any aggressive language." | BP, "Tool usage"; "Overthinking and excessive thoroughness" |
| 3.7 | Over-specification and model-literal following | Opus 5: "only report high-severity" or "be conservative" is followed literally and reports less. Opus 5: verification and double-check instructions cause over-verification and waste tokens, "remove" them. Haiku 5.5: blanket "search regardless of confidence" made it search on half the prompts needing no search. Sonnet 5.5: telling it to think less does not work. | "instructions like these cause over-verification" | OPUS5, "Task scope and over-verification", "Capability improvements"; HAI55, "Accurate search results"; SON55 "Calibrate effort" |
| 3.8 | Prescriptive steps vs goals | General instruction beats a prescribed step plan for thinking models. For multi-window starts the page is the opposite: be prescriptive about how a fresh window starts. | "Prefer general instructions over prescriptive steps." | BP, "Leverage thinking..."; "Workflows across multiple context windows" item 4 |
| 3.9 | XML tags | Use them to separate instructions, context, examples, inputs; consistent names. No size claim. Flat prompt style matches flat output style. | "reduces misinterpretation" | BP, "Structure prompts with XML tags" |
| 3.10 | Role prompts | One sentence is enough. No claim about longer role text. | "Even a single sentence makes a difference" | BP, "Give Claude a role" |
| 3.11 | Positive framing | Say what to do. Opus 5 narration: positive examples work better than "don't". | "Positive examples ... tend to be more effective" | BP, "Control the format of responses"; OPUS5, "User-facing progress updates" |
| 3.12 | Stale instructions | Remove instructions written for earlier models: Opus 4.6-era anti-laziness prompts overtrigger ("Tune anti-laziness prompting"); Opus 5 verification lines; Opus 5.5 "do not think" and "write your reasoning" lines; Sonnet 5.5 "hold all findings for the final response". Claude Code offers `/doctor prompt-audit` to find "instructions written for older models". | "instructions written for older models" | BP, "Migration considerations" item 6; OPUS55 "Prompts written for thinking disabled"; SON55 "User-facing progress updates"; CC-MEM, "Audit your instruction files" |
| 3.13 | Prompt caching | Changing `system`, `tools`, history or top-level effort between requests invalidates caches and thinking blocks on Opus 5.5, Sonnet 5.5, Haiku 5.5. Add sample blocks "from the first request of the session". Relevance to the kit: inference; the pages are about API conversations. | "invalidates every later thinking block" | BP, "Migration considerations" item 7; OPUS55 "Unattended agentic runs" |
| 3.14 | Evidence rule | Every sample block is "measured on that model"; re-check on your evals before applying to another. | "re-check it against your own evals" | BP, "General principles" |

## 4. Claude Code start-up loading facts

### 4.1 What a non-fork subagent has at start (CC-SUB, "What loads at startup")

| Item | Fact | Cost stated? |
| --- | --- | --- |
| Context | Fresh, isolated window; does not see conversation history, invoked skills, or files already read. | No |
| System prompt | The agent's own prompt (markdown body) plus appended environment details; not the Claude Code system prompt. | No |
| Task message | The delegation prompt. "everything in the spawn prompt adds to their context from the start" (CC-COST, agent teams). | No |
| CLAUDE.md | Every level of the hierarchy the main session loads (user, project, local, managed), plus `AGENTS.md` loaded as project instructions. Built-in Explore and Plan skip it. A definition with `omitClaudeMd: true` loads only managed policy files. | No (200-line target per file: CC-MEM) |
| Git status | Snapshot read at subagent start. Explore and Plan skip it. | No |
| Preloaded skills | `skills:` field injects the full skill content, not only the description. Built-in agents preload none. Unlisted skills can still be invoked via the Skill tool. | No |
| Sibling roster | A system reminder listing other named agents, only when the agent's tools include `SendMessage` and another named agent exists. | No |
| Auto memory | The main session's auto memory is NOT loaded. A `memory:` field gives the agent its own: first 200 lines or 25 KB of its `MEMORY.md` plus memory instructions, and Read/Write/Edit are enabled automatically. | Yes: 200 lines / 25 KB cap |
| Output style | Not applied to subagents (except forks). | n/a |
| Tools | `tools` omitted = inherits every tool available to subagents; a `tools` list limits it. `mcpServers` field scopes MCP servers per agent. | No |
| Model | `model` field; context window sized by the subagent's own model. | n/a |
| Fork vs non-fork | A fork inherits full history, system prompt and tools, shares the parent's prompt cache, and "costs less than a fresh subagent for tasks that need the same context". A non-fork has a separate cache. | Qualitative |

Not stated on the pages I read: whether MCP tool definitions or deferred tools are listed inside a subagent at start, and a total token figure for a subagent start. (Inference: the MCP page's tool-search rules are session-wide, but CC-SUB does not say how they apply to subagents; check with `/context` or a probe.)

### 4.2 What is deferred or on demand

| Item | Fact | Source |
| --- | --- | --- |
| MCP tool definitions | Deferred by default (tool search); "only tool names and server instructions load at session start". `ENABLE_TOOL_SEARCH`: unset/`true` = defer all; `auto` = load upfront while definitions total under 10 percent of the window; `auto:N` = custom percent; `false` = load all upfront. Models earlier than the 4-generation load all upfront. Server instructions and an upfront tool description are cut at 4,096 characters; a tool-searched description at 16,384. `alwaysLoad: true` exempts a server and "each upfront tool consumes context". | CC-MCP, "Scale with MCP tool search", "Configure tool search"; CC-COST, "Reduce MCP server overhead" |
| MCP output | Warning above 10,000 tokens; default cap 25,000 tokens (`MAX_MCP_OUTPUT_TOKENS`). | CC-MCP, output section |
| Skill descriptions | Listing of every skill name plus description loads into context at start; full body only on invoke. Listing budget is 1 percent of the model's context window; overflow drops descriptions of least-used skills first. Each entry's `description` + `when_to_use` is capped at 1,536 characters. `disable-model-invocation: true` removes the description from context. | CC-SKILL, "Skill descriptions are cut short", frontmatter reference, invocation-control table |
| Skill body | Enters the conversation as one message when invoked and stays; "every line is a recurring token cost". Keep `SKILL.md` under 500 lines. After compaction: first 5,000 tokens per skill, 25,000 total, oldest dropped first; put key instructions near the top. | CC-SKILL, "Skill content lifecycle" text; CC-CTX, "What survives compaction" |
| Subagent descriptions | Descriptions of custom subagents sit in the main session's context; a warning shows above 15,000 tokens combined. | CC-SUB, "Understand automatic delegation" |
| Path-scoped rules | `.claude/rules/*.md` with `paths:` frontmatter load only when a matching file is read or edited. Rules without `paths` load at launch like CLAUDE.md. | CC-MEM, "Organize rules", "Path-specific rules" |
| Imports | `@path` imports "help you organize a long file but don't reduce its context cost, because imported files also load at launch." Max depth four hops. Each CLAUDE.md, rules file and import counts as a separate file for the size warning. | CC-MEM, "Write effective instructions"; "Import additional files"; troubleshooting |
| HTML comments | Block-level `<!-- -->` comments in CLAUDE.md are stripped before injection (no context cost). | CC-MEM, "Import additional files" section end |
| MEMORY.md | First 200 lines or 25 KB load at start; the rest does not. | CC-MEM, "Auto memory"; CC-SUB "Enable persistent memory" |
| Instructions to skills | "Move instructions from CLAUDE.md to skills": CLAUDE.md is in context at session start; skills load on demand. "Aim to keep CLAUDE.md under 200 lines". | CC-COST, "Move instructions from CLAUDE.md to skills" |

### 4.3 Other cost facts

- CLAUDE.md is delivered as a user message after the system prompt, not as part of the system prompt; "no guarantee of strict compliance, especially for vague or conflicting instructions" (CC-MEM, troubleshooting). Rules that must run every time belong in hooks.
- Project-root CLAUDE.md and unscoped rules are re-injected from disk after compaction (CC-CTX).
- No fixed total token figure for a subagent or session start-up is given on any page I read. CC-CTX says the simulation uses "representative token counts" and points to `/context` for real numbers; CC-SKILL points to `/doctor` for skill-listing cost.
- Plan-usage recommendation example on CC-COST: "Trim ~/code/api/CLAUDE.md · 49k tokens per request" (an example row, not a norm).
- Sonnet for teammates and Haiku for simple subagents are the page's cost suggestions: "specify `model: haiku` in your subagent configuration" (CC-COST, "Choose the right model"). Note: the cheapest-model advice is tied to simple subagent tasks.
- Delegation: "Running many subagents that each return detailed results can consume significant context, and each subagent spends tokens of its own" (CC-SUB).
- Agent teams: "approximately 7x more tokens than standard sessions" when teammates run in plan mode; teammates load CLAUDE.md, MCP servers and skills automatically (CC-COST). Teams are OFF in this kit (rules/assistants/claude.md).
- Extended thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 inside Claude Code ("always use extended thinking"); lower `/effort` instead (CC-COST, "Adjust extended thinking"). Thinking tokens are billed as output.
- Opus 5 in Claude Code: Claude Code adds a delegation instruction only with the `claude_code` system prompt preset; with a custom or omitted prompt add your own (OPUS5, "Controlling subagent spawning").

## 5. Conflicts and changes from older advice that the pages call out

| # | Change | Quote | Source |
| --- | --- | --- | --- |
| 5.1 | Manual extended thinking (`budget_tokens`) is gone: 400 error on 4.7 and later; adaptive thinking plus effort replaces it. Older "thinking budget" advice is obsolete. | "setting `budget_tokens` returns a 400 error" | BP, "Thinking and reasoning"; "Migration considerations" item 4 |
| 5.2 | Prefill is gone from 4.6 models on. | "no longer supported" | BP, "Migrating away from prefilled responses" |
| 5.3 | Verification instructions: general advice says append "verify before you finish"; for Opus 5 this causes over-verification and should be removed. Haiku 5.5 and Sonnet 5.5 at low effort are the opposite: they skip checks and a verify paragraph is recommended. So the same sentence is right for one model and wrong for another. | "Claude Opus 5 is the exception" | BP, "Leverage thinking..."; SON55 and HAI55 verification sections |
| 5.4 | Thinking-less-by-prompt: BP gives a "respond directly when in doubt" line, but Sonnet 5.5 and Haiku 5.5 do not honor it reliably; lower effort. | "doesn't reliably reduce its thinking" | BP vs SON55 "Calibrate effort", HAI55, STEER |
| 5.5 | "Think" wording: Opus 4.5 with thinking disabled was sensitive to the word "think"; Sonnet 5.5 reasoning-JSON advice now uses "Think the problem through before you answer." Different model, different effect. | "particularly sensitive to the word \"think\"" | BP, Note after "Leverage thinking..."; SON55 "Reasoning tasks with JSON output" |
| 5.6 | Anti-laziness and "use the tool whenever in doubt" prompts from earlier models now overtrigger on 4.5/4.6-and-later; reduce them. | "reduce that guidance" | BP, "Migration considerations" item 6 |
| 5.7 | Asking the model to write out its reasoning (manual CoT, `<thinking>` tags) used to be the fallback; on Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5 it may be declined; rely on thinking. | "rely on thinking instead" | BP, "Leverage thinking..." |
| 5.8 | Effort defaults differ: Opus 5.5 and Haiku 5.5 default `medium`; most others `high`. A request that omits `effort` runs one level lower on Opus 5.5 than on Opus 5. | "runs one level lower than it did on Claude Opus 5" | EFF, Opus 5.5 section |
| 5.9 | Output verbosity differs by model: Opus 5 runs long and effort does not shorten it; Fable 5.1 writes fewer updates (remove "keep it brief" text). | "does not reliably change visible response length" | BP, "Communication style and verbosity" |
| 5.10 | Context awareness (token-budget tracking) is listed for Sonnet 5, Sonnet 4.6, Haiku 4.5 on the BP page; Sonnet 5.5 and Haiku 5.5 are not named there. Page silent whether they have it. | (paraphrase) | BP, "Context awareness and multiwindow workflows" |
| 5.11 | Subagent default: general advice says Claude delegates "without requiring explicit instruction"; Opus 4.6 and Opus 5 over-delegate and need damping text or caps. | "Watch for overuse" | BP, "Subagent orchestration" |
| 5.12 | CLAUDE.md imports: the kit-style pattern "import to organize" does not lower context cost; only path-scoped rules, skills and shorter files do. | "don't reduce its context cost" | CC-MEM, "Write effective instructions" |

## Coverage and limits

- Pages read in full: BP; OPUS55; SON55; HAI55; OPUS5 (sections quoted); EFF; STEER; CC-COST; CC-CTX; CC-MEM (key sections via search plus lines 78-97); CC-SUB (startup, frontmatter, memory; tail read); CC-MCP (tool-search section); CC-SKILL (listing budget, lifecycle).
- WebFetch returns text through a small model for some pages; direct quotes were checked against the BP, OPUS55, SON55, HAI55, OPUS5 and STEER text that came back verbatim. CC-SUB and CC-SKILL quotes come from model extracts; re-read the line before relying on a number.
- Not read: the "What's new" and migration pages for each model; "Prompting Claude Fable 5/5.1"; prompt-caching page; skill authoring best-practices page; Claude Code `best-practices` and `features-overview` pages.
- Dates: no page shows a last-updated date. All read on 2026-10-21; Claude Code docs mention versions up to v2.1.305 (CC-COST).
