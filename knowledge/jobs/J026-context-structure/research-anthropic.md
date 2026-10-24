---
type: reference
scope: universal
status: active
updated: 2026-10-24
source: "J026 research"
supersedes: []
---

> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# Anthropic and Anthropic-staff evidence on agent context (J026)

Labels: OFFICIAL = Anthropic docs or engineering post; STAFF = named employee talk or post; THIRD-PARTY = reports a staff statement (source named). "Inference" = my reading, not a source claim. Quotes are under 15 words; "-" = none. Not repeated here: `knowledge/reference/studio/prompting-guide-2026-10.md`, `knowledge/reference/studio/context-research-2026-10.md`. Fetch results are model extracts of the pages (not verbatim reads), so re-open a page before relying on an exact wording or number.

Short names for sources used below:
- ECE = https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025-09-29)
- MAR = https://www.anthropic.com/engineering/multi-agent-research-system (2025-06-13)
- BEA = https://www.anthropic.com/engineering/building-effective-agents (2024-12-19)
- WET = https://www.anthropic.com/engineering/writing-tools-for-agents (2025-09-11)
- SKL = https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (2025-10-16)
- SKB = https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (undated, read 2026-10-24)
- CCB = https://code.claude.com/docs/en/best-practices (undated, read 2026-10-24; the 2025-04-18 engineering post redirects here)
- SLA = https://claude.dev/blog/seeing-like-an-agent/ (Thariq Shihipar, 2026-04-10)
- HAR = https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (2025-11-26)
- HDL = https://www.anthropic.com/engineering/harness-design-long-running-apps (Prithvi Rajasekaran, 2026-03-24)
- CCC = https://www.anthropic.com/engineering/building-c-compiler (Nicholas Carlini, 2026-02-05)

## 1. Size and kind of subagent/system instruction; where the key instructions sit

| # | Finding | Label | Source URL | Date | Quote |
|---|---|---|---|---|---|
| 1.1 | System prompts should sit at the "right altitude": not brittle hardcoded if-else logic, not vague guidance. Aim for the smallest set of high-signal tokens. | OFFICIAL | ECE | 2025-09-29 | "The right altitude is the Goldilocks zone" |
| 1.2 | Do not stuff a prompt with a long list of edge-case rules. Give a small set of diverse canonical examples instead. | OFFICIAL | ECE | 2025-09-29 | "examples are the 'pictures' worth a thousand words" |
| 1.3 | Bloated CLAUDE.md makes the agent ignore real instructions. Test for each line: would removing it cause mistakes? If not, cut. If a rule is still skipped, the file is probably too long. | OFFICIAL | CCB | undated, read 2026-10-24 | "Bloated CLAUDE.md files cause Claude to ignore your actual instructions" |
| 1.4 | CLAUDE.md should hold only what applies broadly each session; situational domain knowledge goes in skills loaded on demand. Exclude what can be read from code, detailed API docs ("link to docs instead"), long tutorials, file-by-file descriptions. | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 1.5 | If Claude skips one instruction, add emphasis ("IMPORTANT") to that line only; emphasising many lines means none stands out. | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 1.6 | Skill authoring: "Claude is already very smart", only add what it lacks; challenge each paragraph for its token cost. Example: 50-token version vs 150-token padded version of the same skill text. | OFFICIAL | SKB | undated, read 2026-10-24 | "Does this paragraph justify its token cost?" |
| 1.7 | Match specificity to fragility ("degrees of freedom"): exact commands where operations are fragile, general direction where many paths work. Narrow bridge vs open field. | OFFICIAL | SKB | undated, read 2026-10-24 | - |
| 1.8 | Test instructions on every model you will run: Haiku may need more detail, Opus may need less over-explaining. | OFFICIAL | SKB | undated, read 2026-10-24 | - |
| 1.9 | Claude Code team cut its main system prompt by about 80% for the newest models; heavy prescriptions constrain more capable models. Prompt stages: small+examples, large+many tools, then small+tool search with no examples. | STAFF (Thariq Shihipar, talk at AI Engineer World's Fair 2026; summary page) | https://ai.engineer/talks/field-guide-to-fable | 2026 (page undated; July 2026 per Willison) | "the examples tend to constrain it" |
| 1.10 | Same team prefers context over constraints and fewer "do not do this" lines; "don't" lists were needed for earlier models and can conflict with user instructions. Removing examples "was extremely helpful". | STAFF (Thariq Shihipar, Cat Wu; Simon Willison write-up of fireside chat) | https://simonwillison.net/2026/Jul/21/cat-and-thariq/ | 2026-07-21 | "give it context and not just constraints" |
| 1.11 | Cat Wu: the 80% cut applies only to the most frontier models; each model now gets its own system prompt. Absolute words like "always verify" were replaced with a stated condition (run the app locally for larger UX changes) because the "always" claim was only about 90% true. | STAFF (Cat Wu, via Willison) | https://simonwillison.net/2026/Jul/21/cat-and-thariq/ | 2026-07-21 | - |
| 1.12 | Token numbers for that cut (about 800 to 164) come from a secondary post, not Anthropic. | THIRD-PARTY (dev.to, citing Thariq's July 2 2026 announcement) | https://dev.to/davekurian/claude-codes-system-prompt-shrinks-80-without-performance-loss-10f | 2026-07 | - |
| 1.13 | Tools are part of the prompt: tool definitions deserve as much prompt engineering as the main prompt; include example usage, edge cases, input format, and boundaries from other tools. | OFFICIAL | BEA (Appendix 2) | 2024-12-19 | "just as much prompt engineering attention" |
| 1.14 | Position: long documents go near the top of the prompt, above query, instructions and examples (already in the known prompting-guide note). I found no newer Anthropic statement on where role/rules go beyond that. | OFFICIAL | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | undated, read 2026-10-24 | "Put long-form data at the top" |
| 1.15 | Context rot / diminishing returns: recall falls as context grows, so context is a finite resource; aim for the smallest set of tokens giving the desired behaviour. | OFFICIAL | ECE | 2025-09-29 | "finite resource with diminishing marginal returns" |
| 1.16 | Inference: 1.3, 1.9 and 1.10 agree across three Anthropic sources (docs, engineering post, staff): longer or more prohibitive instructions can lower rule-following. None gives a threshold in lines or tokens, except SKB (under 500 lines per SKILL.md body). | Inference | - | - | - |

## 2. Pre-loading vs pointers and just-in-time fetch

| # | Finding | Label | Source URL | Date | Quote |
|---|---|---|---|---|---|
| 2.1 | Keep lightweight identifiers (paths, links, queries) and load data at runtime with tools; this mirrors human use of file systems and indexes. Metadata (folder names, names, timestamps) also guides the agent. | OFFICIAL | ECE | 2025-09-29 | - |
| 2.2 | Trade-off: runtime exploration is slower than pre-loaded retrieval and needs good tools and heuristics, or the agent wastes context. Most effective agents use a hybrid: some data up front, more on demand. | OFFICIAL | ECE | 2025-09-29 | "hybrid strategy" |
| 2.3 | Skills use 3 levels: name+description always loaded; SKILL.md body when the skill seems relevant; linked files only when needed. Called the core design principle. | OFFICIAL | SKL | 2025-10-16 | "keep the core of the skill lean" |
| 2.4 | Bundled reference files cost no context until read; large API docs, examples and datasets can sit beside a skill. | OFFICIAL | SKB (Runtime environment) | undated, read 2026-10-24 | "No context penalty for large files" |
| 2.5 | Keep references one level deep from SKILL.md: with nested links Claude may only preview a file (`head -100`) and get partial information. Reference files over 100 lines need a table of contents at the top. | OFFICIAL | SKB | undated, read 2026-10-24 | - |
| 2.6 | Name files descriptively and organise by domain (`reference/finance.md`), not `doc2.md`; SKILL.md should say which file covers what and show a grep line per file. | OFFICIAL | SKB | undated, read 2026-10-24 | - |
| 2.7 | Claude Code first used RAG (pre-indexed snippets pushed to the model), then switched to a Grep tool so the model finds context itself. RAG meant Claude was handed context rather than finding it; fragile across environments. | STAFF (Thariq Shihipar) | SLA | 2026-04-10 | "was given this context instead of finding the context itself" |
| 2.8 | Docs question: a bare link to docs worked but pulled big chunks into context; putting docs in the system prompt would add context rot. Fix: a dedicated "Claude Code Guide" subagent that searches docs in its own context and returns only the answer. | STAFF (Thariq Shihipar) | SLA | 2026-04-10 | "The subagent does the doc-searching in its own context" |
| 2.9 | Progressive disclosure is how the team adds functionality without adding a tool; Claude now does nested search across several file layers. Tool bar is high (~20 tools) because each tool is another option to weigh. | STAFF (Thariq Shihipar) | SLA | 2026-04-10 | "The bar to add a new tool is high" |
| 2.10 | Code execution with MCP: present tools as files in a directory the agent explores, or give a `search_tools` tool with detail levels (name, name+description, full schema). Example: 150,000 tokens down to 2,000. | OFFICIAL | https://www.anthropic.com/engineering/code-execution-with-mcp | 2025-11-04 | "read tool definitions on-demand" |
| 2.11 | Context-editing and memory features exist so stale tool results leave the window while key facts persist in files. See "Measured numbers". | OFFICIAL | https://claude.com/blog/context-management | 2025-09-29 | - |

## 3. Making an agent actually consult a reference corpus (docs) instead of answering from memory

Anthropic has no single post titled for this. The items below are what the sources say that bears on it.

| # | Finding | Label | Source URL | Date | Quote |
|---|---|---|---|---|---|
| 3.1 | Point to the source that answers the question: "look through X's git history" beat "why is X weird?". Name the source in the prompt. | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 3.2 | Tell the agent to fetch: give URLs for docs, reference files with `@`, and say "pull context yourself". | OFFICIAL | CCB | undated, read 2026-10-24 | "Let Claude fetch what it needs" |
| 3.3 | Skill triggering depends entirely on `name` and `description` (third person; what it does AND when to use it, with key terms). Vague descriptions ("Helps with documents") fail discovery among 100+ skills. | OFFICIAL | SKB | undated, read 2026-10-24 | "Always write in third person" |
| 3.4 | Observe real runs: if Claude never opens a bundled file, it may be unnecessary or poorly signalled; if it misses links, make them more explicit or prominent. | OFFICIAL | SKB; SKL | undated; 2025-10-16 | - |
| 3.5 | A rule that is skipped may need stronger wording or more prominence ("MUST filter" instead of "always filter"), found by testing with a second Claude on real tasks. | OFFICIAL | SKB (iterate with Claude A/B) | undated, read 2026-10-24 | - |
| 3.6 | Advisory text (CLAUDE.md) is not a guarantee; hooks are deterministic for actions that must happen every time. | OFFICIAL | CCB | undated, read 2026-10-24 | "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic" |
| 3.7 | Without explicit prompting Claude skipped end-to-end verification and used shortcuts (unit tests, curl). Fixed by giving it a browser tool that tests like a user and by a step list at session start. | OFFICIAL | HAR | 2025-11-26 | - |
| 3.8 | Tool descriptions steer behaviour: Claude appended "2025" to searches until the description was fixed. Write descriptions as for a new hire; make implicit context explicit. | OFFICIAL | WET | 2025-09-11 | - |
| 3.9 | Error and truncation messages can steer the agent to the right next step (use filters, narrower search). Helpful errors say how to fix the input. | OFFICIAL | WET | 2025-09-11 | - |
| 3.10 | Give the agent a check it can run (tests, build, screenshot); "have Claude show evidence rather than asserting success". | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 3.11 | Inference: no Anthropic source says "load the docs at the top of the role file" as the fix for not reading docs. The sources favour a clear trigger (description or brief names the source), an easy-to-find indexed corpus (one-level, TOC, descriptive names), a check on the output, and (for a heavy corpus) a docs-lookup subagent as in 2.8. | Inference | - | - | - |

## 4. How a lead should brief subagents

| # | Finding | Label | Source URL | Date | Quote |
|---|---|---|---|---|---|
| 4.1 | Each subagent brief needs: an objective, an output format, guidance on tools and sources, and clear task boundaries. Without them subagents duplicated work or left gaps (one searched 2021 chips while two repeated 2025 supply chains). | OFFICIAL | MAR | 2025-06-13 | - |
| 4.2 | Teach the lead to delegate with detailed task descriptions; "short, vague" instructions were the early failure. | OFFICIAL | MAR | 2025-06-13 | - |
| 4.3 | Embed effort-scaling rules in the prompt: 1 agent and 3-10 tool calls for simple lookups, 2-4 subagents with 10-15 calls each for comparisons, 10+ for complex research. Early agents over-invested in simple queries. | OFFICIAL | MAR | 2025-06-13 | - |
| 4.4 | "Think like your agents": build a simulation with the exact prompts and tools and watch step by step to find failure modes. Heuristics were favoured over rigid rules. | OFFICIAL | MAR | 2025-06-13 | - |
| 4.5 | "Start wide, then narrow down": short broad queries first; agents defaulted to long over-specific ones. | OFFICIAL | MAR | 2025-06-13 | - |
| 4.6 | Subagents write outputs to external storage (files) and pass lightweight references to the lead, which cuts information loss and token overhead versus passing text through the lead. | OFFICIAL | MAR | 2025-06-13 | - |
| 4.7 | Subagents return a condensed summary (often 1,000-2,000 tokens) of work done in a clean window. | OFFICIAL | ECE | 2025-09-29 | "condensed, distilled summary" |
| 4.8 | Subagent prompts in Claude Code workflows: Claude writes "a detailed prompt for each" subagent; Willison also tells it which (cheaper) model to use. | STAFF (Thariq Shihipar, via Willison) | https://simonwillison.net/2026/Jul/21/cat-and-thariq/ | 2026-07-21 | - |
| 4.9 | A good spec/brief is self-contained: names the files and interfaces involved, states what is out of scope, and ends with an end-to-end verification step. | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 4.10 | Reviewer in a fresh subagent sees only the diff and the criteria you give it. Tell it to flag only gaps that affect correctness or the stated requirements; a reviewer told to find gaps will find some and drive over-engineering. | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 4.11 | Planner/generator/evaluator split: the planner was told to be ambitious on scope but avoid granular technical detail, so spec errors do not cascade. Generator and evaluator agreed a "sprint contract" (definition of done, testable behaviours) before building. | OFFICIAL | HDL | 2026-03-24 | - |
| 4.12 | Evaluator out of the box approved flawed work; the team tuned its prompt over several rounds by reading logs; few-shot examples with score breakdowns cut score drift. | OFFICIAL | HDL | 2026-03-24 | - |
| 4.13 | "Orchestrator-workers": subtasks are chosen by the lead from the input. The post gives no briefing detail (MAR does). Use frameworks only if you understand the prompts under them. | OFFICIAL | BEA | 2024-12-19 | "obscure the underlying prompts" |
| 4.14 | Specialised roles used beside the main workers in a 16-agent build: dedup, performance, design critique, documentation. Each fresh agent got no prior context, so prompts demanded READMEs and progress files. | OFFICIAL | CCC | 2026-02-05 | - |

## 5. Role identity: does a long role file help

| # | Finding | Label | Source URL | Date | Quote |
|---|---|---|---|---|---|
| 5.1 | Anthropic's own subagent example is a short role prompt (a one-line "You are a senior security engineer" plus 4 review bullets and an output instruction), with `description`, `tools`, `model` in frontmatter. | OFFICIAL | CCB (Create custom subagents) | undated, read 2026-10-24 | - |
| 5.2 | Subagent definitions are for "isolated tasks" and "specialized focus" in their own context and tool set. | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 5.3 | Role-calibrated behaviour came from tuning against real transcripts, not from a long persona: the evaluator needed several prompt rounds; criteria weights (design, originality) steered output away from generic. | OFFICIAL | HDL | 2026-03-24 | - |
| 5.4 | Role files are instructions like any other: the over-specified CLAUDE.md warning (1.3) and the 80% prompt cut (1.9) apply. No Anthropic source states a recommended length for a role file. | Inference | - | - | - |
| 5.5 | Define the agent's job by environment, tools and system prompt; iterate those three before anything else. | STAFF (Barry Zhang, AI Engineer Summit NYC 2025; summary) | https://ai.engineer/talks/effective-ai-agents | 2025 | - |
| 5.6 | Put yourself in the agent's context window: it sees a narrow slice (summary says 10-20k tokens) and acts "in the dark" between tool results. | THIRD-PARTY (overview of Barry Zhang's talk, as returned by search; not verified against transcript) | https://ai.engineer/talks/effective-ai-agents | 2025 | - |
| 5.7 | Use a fresh context for review so the reviewer is not biased toward code it just wrote (writer/reviewer sessions). | OFFICIAL | CCB | undated, read 2026-10-24 | - |

## 6. Memory and notes

| # | Finding | Label | Source URL | Date | Quote |
|---|---|---|---|---|---|
| 6.1 | Structured note-taking: the agent writes notes outside the context window (to-do lists, NOTES.md) and reads them back later. | OFFICIAL | ECE | 2025-09-29 | - |
| 6.2 | Compaction: summarise a conversation nearing the limit into a new window; clearing old tool results is a light-touch form. Tune for recall first, then precision. | OFFICIAL | ECE | 2025-09-29 | - |
| 6.3 | Long-running harness: initializer session creates `init.sh`, a progress file and a git commit; a JSON feature list where coding agents may change only the `passes` field (model less likely to overwrite JSON than Markdown). | OFFICIAL | HAR | 2025-11-26 | - |
| 6.4 | Session-start routine: check directory, read git log and progress file, read feature list, pick one feature, run a basic end-to-end test. End each session with a commit and progress update. | OFFICIAL | HAR | 2025-11-26 | - |
| 6.5 | Context resets (fresh agent plus structured handoff) vs compaction: compaction keeps continuity but does not remove "context anxiety" (wrapping up early). Opus 4.5 largely lost this, so resets were dropped. Agents talked through files. | OFFICIAL | HDL | 2026-03-24 | - |
| 6.6 | Agents that start with no context: ask for extensive READMEs and progress files updated often; keep a running file of failed approaches. | OFFICIAL | CCC | 2026-02-05 | - |
| 6.7 | Harness output discipline: print a few lines, write details to log files, put "ERROR" and reason on one line for grep, precompute summary stats. | OFFICIAL | CCC | 2026-02-05 | - |
| 6.8 | The lead saves its plan to memory because context past 200,000 tokens is truncated; fresh subagents continue via handoffs. | OFFICIAL | MAR | 2025-06-13 | - |
| 6.9 | CLAUDE.md maintenance: treat like code, review when things go wrong, prune regularly, test by watching whether behaviour shifts. Customise compaction in it ("always preserve modified files"). | OFFICIAL | CCB | undated, read 2026-10-24 | - |
| 6.10 | Boris Cherny reportedly keeps CLAUDE.md small (about 2.5k tokens), adds a line each time Claude errs, and urged deleting an overgrown one. Only secondhand; no direct quote found. | THIRD-PARTY (Nauti 2026-08-01 citing AI Automators/Geeky Gadgets; Medium tips list) | https://news.ainauten.com/en/story/claude-code-erfinder-boris-cherny-raet-loesch-deine-claudemd | 2026-08-01 | - |
| 6.11 | An Anthropic team member spoke on context engineering and memory at AI Native DevCon London 2026 (CLAUDE.md, memory tool, skills, filesystem memory, "dreaming" curation). Only an outline of uncertain accuracy was found. | THIRD-PARTY (Tessl-hosted outline, labelled partly inferred) | https://tessl.io/registry/ainativedev/aidevcon-2026-ldn/0.100.14/files/talk-lamis-context-engineering-dreaming/outline.md | 2026 | - |
| 6.12 | After two failed corrections in one session, `/clear` and rewrite the prompt with what you learned; failed attempts stay in context and pollute it. | OFFICIAL | CCB | undated, read 2026-10-24 | - |

## 7. Measured numbers (all as reported by the source; none re-run)

| # | Number | Label | Source URL | Date |
|---|---|---|---|---|
| 7.1 | Lead Opus 4 + Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on Anthropic's internal research eval. | OFFICIAL | MAR | 2025-06-13 |
| 7.2 | Token usage alone explained 80% of the variance in BrowseComp performance; three factors explained 95%. | OFFICIAL | MAR | 2025-06-13 |
| 7.3 | Agents use about 4x the tokens of chat; multi-agent systems about 15x. | OFFICIAL | MAR | 2025-06-13 |
| 7.4 | A tool-description rewrite by a Claude model cut later task-completion time by 40%. Parallel tool calls cut research time by up to 90%. Evals began with about 20 queries. | OFFICIAL | MAR | 2025-06-13 |
| 7.5 | Memory tool + context editing: 39% better than baseline; context editing alone: 29%; a 100-turn web-search eval used 84% fewer tokens. Internal agentic search eval. | OFFICIAL | https://claude.com/blog/context-management | 2025-09-29 |
| 7.6 | Code execution with MCP: 150,000 tokens down to 2,000 on one Drive-to-Salesforce task. | OFFICIAL | https://www.anthropic.com/engineering/code-execution-with-mcp | 2025-11-04 |
| 7.7 | Concise vs detailed tool response: 72 vs 206 tokens. Claude Code caps tool responses at 25,000 tokens by default. | OFFICIAL | WET | 2025-09-11 |
| 7.8 | Skill body under 500 lines; description up to 1,024 characters; name up to 64. Example: 50 vs 150 tokens for the same instruction. | OFFICIAL | SKB | undated, read 2026-10-24 |
| 7.9 | Full harness (planner, generator, evaluator) vs solo run on one task: 6 hr and $200 vs 20 min and $9; solo output did not work, harness output was playable (Opus 4.5). Later run: 3 hr 50 min, $124.70. | OFFICIAL | HDL | 2026-03-24 |
| 7.10 | 16 parallel agents, about 2,000 sessions, about $20,000 for a 100,000-line compiler. | OFFICIAL | CCC | 2026-02-05 |
| 7.11 | Eval harness bugs mattered: Opus 4.5 scored 42% on CORE-Bench until grading fixes raised it to 95%. | OFFICIAL | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | 2026-01-09 |
| 7.12 | Claude Code system prompt cut by about 80% (about 800 to 164 tokens) with benchmarks reported steady. Numbers are secondhand. | THIRD-PARTY | https://dev.to/davekurian/claude-codes-system-prompt-shrinks-80-without-performance-loss-10f | 2026-07 |
| 7.13 | Claude Code has about 20 tools; reminder inserted every 5 turns for the old todo tool, later replaced because it constrained newer models. | STAFF (Thariq Shihipar) | SLA | 2026-04-10 |

## Not found

| Looked for | Result |
|---|---|
| Measured gain from "documents at top, query at end" (the older 30% figure) | Not in the current page text I fetched; the long-context tips URL now returns the prompting best-practices page, which only says it "improves performance". |
| Any Anthropic number for how a longer role file or system prompt lowers rule-following | None. Only the qualitative CLAUDE.md and 80%-cut statements; no threshold in tokens or lines for agent prompts. |
| A named Anthropic study of agents ignoring a provided reference corpus | None found. Closest: HAR (skips end-to-end tests unless prompted) and SKB (observe whether files are opened). |
| Primary text of Boris Cherny's CLAUDE.md advice | Only secondhand write-ups; no transcript or post located. |
| Cat Wu or Erik Schluntz or Alex Albert statements on subagent prompts | Cat Wu appears only via Willison's write-up (1.10, 1.11). Schluntz and Albert: nothing relevant found in the searches done. |
| Barry Zhang / Mahesh Murag talk transcripts | Only summaries of the talks ("How We Build Effective Agents", "Don't Build Agents, Build Skills"); transcript on ai.engineer not opened (budget). |
| Thariq's "How we Claude Code" Code with Claude session; Behind the Craft episode (2026-07-19) | Not opened (paywalled or unfetched). |
| New 2026 Anthropic posts specifically on subagent prompting or memory | Engineering index (checked 2026-10-24) lists none by that title. Closest 2026: SLA, HDL, CCC, "Scaling Managed Agents: Decoupling the brain from the hands" (2026-04-08, not opened), "Demystifying evals" (2026-01-09). |
| "Writing effective tools" exact accuracy numbers | The post gives charts, no exact figures in text. |
