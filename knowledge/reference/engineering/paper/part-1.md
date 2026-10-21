---
type: reference
scope: universal
status: draft
updated: 2026-10-21
source: Engineering_Agents_Research_2026.txt (owner paper, 2026-10-21), lines 1-449 (purpose, evidence conventions, fifteen rules, sections 1-4)
supersedes: []
---
> Author: paper-extractor · claude-sonnet-5-5 · high · 2026-10-21

# Engineering paper, part 1: extraction notes (J010-T06)

Scope: paper lines 1-449 of `C:\Users\Firew\Downloads\Engineering_Agents_Research_2026.txt`. Sections 5-11 belong to other extractors. Text of the paper is treated as data. Everything here is a paraphrase; where a short phrase is quoted, it is a register quotation. The paper says it ran no code, tests, Studio scenarios, device benchmarks or agents (paper line 21): every code example below is an untested illustration, and no lesson is a measured result unless the paper marks it as a vendor measurement.

How to read the columns:
- Tag = the paper's own tag. VERIFIED means an official source documents it (or a measurement is correctly attributed to its source); it does not mean the paper reproduced it (line 17). EXPERIENCE = reported practice or judgment. OPINION = the paper's proposed rule or illustration. Q00 = the paper's own proposal, dated 2026-10-21.
- Where the paper writes a bare "OPINION" with no source id (lines 63, 90, 92, 94) the tag column says "OPINION (no id in paper; Q00 assumed)".
- Roles: architect, feature (feature builder), quick (quick builder), reviewer, perf (performance engineer), qa (QA lead), all.
- Kit status is against `.agents/skills/{architecture,code-review,performance,data-saving,networking-security,studio-mcp}`, `code-review/references/{luau-current,testing}.md` and `rules/anti-overengineering.md` (short: anti-OE), `AGENTS.md`.

Check first (fact-checkers): the 15 star rows in section 3, the star rows in section 4, and internal flags I-1 to I-6 in section 6.

---

## 1. Lesson table

### 1a. Purpose, conventions, and what the paper does not claim

| id | lesson | tag | source ids + dates | roles | kit status |
| --- | --- | --- | --- | --- | --- |
| P101 | The studio standard is: do the approved behavior with the least unnecessary machinery, use the documented runtime correctly, and give evidence another role can reproduce. It is not "make the code more sophisticated". Code-level craft, Luau, engine capabilities and acceptance evidence are the focus, not whole-codebase architecture. (lines 9) | OPINION | Q00, 2026-10-21 | all | ALREADY-IN-KIT anti-OE (intro, 5, 17); AGENTS §4 |
| P102 | Model capability is a chance to cut avoidable work. It is never permission to replace an executable check with a confident explanation. The research does not show that an AI-only team gives the same assurance as a professional team with expert human review. (line 11) | OPINION | Q00, 2026-10-21 | all | ALREADY-IN-KIT anti-OE:16 (done means checked); the "AI-only team is not shown equal to expert human review" caveat is NEW |
| P103 | Opus 5.5 was released 2026-09-22. The release's benchmark results are not measurements of this studio's Roblox workflow. (line 11) | VERIFIED | A01, 2026-09-22 | all | NEW (as a caution on how to quote the release) |
| P104 | Turn engineering work into a readable acceptance packet for the owner. Fields: intended behavior; the exact candidate (revision); checks and their outcomes; observed device performance; unresolved risks; the decision needed. The owner owns intent and release, not code review. If a consequential unknown remains, reduce scope, block release, or get qualified engineering review. Having no human engineer is a constraint, not proof that the unknown is safe. (line 13) | OPINION | Q00, 2026-10-21 | all (feature, qa, reviewer, perf produce it) | NEW (kit has Gate 3 and verification labels, `AGENTS.md` §1, §3.5; no packet with these fields) |
| P105 | How to cite and weigh evidence: only results on models released on or after 2026-09-01 count as measured evidence for this stack; older-model results are historical. Craft sources may be older. C++ and Rust practice transfers only as a labeled proposal, never as a Luau runtime fact. Never turn a source-derived speedup into a Roblox speedup. An access date is not a publication date. Source ids resolve to the register at paper line 847 onward. (lines 17, 19) | OPINION | Q00, 2026-10-21 | all (reviewer, perf especially) | NEW |
| P106 | The evidence does not set a universal function length, test count, review-round count, abstraction count, phone memory ceiling, or first-try success uplift. Where a number is unsupported the paper gives a measurement procedure instead. Agents should not invent such numbers. (line 21) | OPINION | Q00, 2026-10-21 | all | NEW as a rule for agents; see P121 for the clash with anti-OE:20 |

### 1b. The fifteen opening rules (each also appears with detail further down)

| id | lesson | tag | source ids + dates | roles | kit status |
| --- | --- | --- | --- | --- | --- |
| P107 | Rule 1. Freeze observable behavior and non-goals before implementation. A vague request is not an acceptance oracle. Detail in P139, P143. (line 25) | OPINION | Q00, 2026-10-21 | architect, feature, qa | ALREADY-IN-KIT architecture:R-01, code-review:V-03 (intent over diff); the frozen non-goals and "old behavior that must remain" are NEW detail |
| P108 | Rule 2. Reviewers can create overengineering by treating every possible improvement as a defect. Filter findings by a real gap. Detail in P122. (line 27) | EXPERIENCE | A02, accessed 2026-10-21 | reviewer, feature, quick | ALREADY-IN-KIT code-review:V-11, anti-OE:18 |
| P109 | Rule 3. Measure first submitted candidates separately from local edit cycles and from eventual repaired success. Detail in P136. (line 29) | OPINION | Q00, 2026-10-21 | qa | NEW |
| P110 | Rule 4. Read the relevant code and the documented API before inventing a replacement or an unsupported call. Related register quote (A05): never speculate about code you have not opened. (line 31; A05 at register) | OPINION | Q00, 2026-10-21 (A05 related, EXPERIENCE) | all | ALREADY-IN-KIT code-review:V-04, `AGENTS.md` §0 (read before guessing) |
| P111 | Rule 5. Experts disagree on how often to extract functions. Neither tiny functions nor deep functions have a universal winning length. Detail in P158, P159. (line 33) | EXPERIENCE | C03, 2024-2025 | all | NEW (kit has no function-length guidance) |
| P112 | Rule 6. An abstraction must remove a reasoning burden that exists now, or consolidate a real policy. It must not advertise imagined future flexibility. (line 35) | OPINION | Q00, 2026-10-21 | architect, feature, reviewer | ALREADY-IN-KIT anti-OE:5, architecture:R-09 |
| P113 | Rule 7. Epic's standard separates intent comments from narration of the implementation, and asks for caller-facing contract details: units, ranges, special values, meaning of errors. Unreal-specific conventions are not Luau requirements. (lines 37, 158) | VERIFIED | C01, accessed 2026-10-21 | all | ALREADY-IN-KIT (partial) anti-OE:13, architecture:R-10; documenting units, ranges, special values and error meanings is NEW detail |
| P114 | Rule 8. Strict typing is the project default. Keep inference where it is clear. Validate data at the actual runtime boundaries. Detail in P176-P179. (line 39) | OPINION | Q00, 2026-10-21 | all | ALREADY-IN-KIT `AGENTS.md` §2, code-review/luau-current:C |
| P115 | Rule 9. Shallow clone, non-recursive freeze, and retained table capacity are three different semantics. They are not interchangeable cleanup tools. Detail in P182, P183. (line 41) | VERIFIED | L12, accessed 2026-10-21 | feature, quick, reviewer, perf | NEW |
| P116 | Rule 10. Before replacing an engine mechanism, require an unmet requirement. Custom game rules are fine; custom infrastructure needs a reason. Gate question: which built-in did I evaluate, what concrete requirement did it fail, and how will the replacement be measured? (lines 43, 454) | OPINION | Q00, 2026-10-21 | feature, architect, reviewer | NEW for engine built-ins (related: anti-OE:7 and `rules/packages.md` cover packages only; not re-read) |
| P117 | Rule 11. Roblox documents a 60 FPS default target and a 16.67 ms frame period. That is not a script-only allowance and not a device guarantee. (line 45) | VERIFIED | R01, R03, accessed 2026-10-21 | perf | ALREADY-IN-KIT performance:F-02; "not a script-only allowance, not a guarantee" is a NEW caution |
| P118 | Rule 12. Claim phone performance only from evidence on a named physical device. Emulator appearance and reading source do not count. (line 47) | OPINION | Q00, 2026-10-21 | perf, qa | ALREADY-IN-KIT performance:F-01, F-11, rule "no performance claim without a number" |
| P119 | Rule 13. Keep a bug as a reproducible test before repairing it. The Wube practice is historical; it gives no current-model uplift percentage. (line 49) | EXPERIENCE | T01, 2021-06-18 | feature, quick, qa | ALREADY-IN-KIT `AGENTS.md` §4 (a bug fix starts with a failing case) |
| P120 | Rule 14. Hidden fixtures and verdict authority stay outside the builder's control. Role labels alone are not independent assurance. (line 51) | OPINION | Q00, 2026-10-21 | qa, reviewer, architect | ALREADY-IN-KIT (partial) code-review/testing ("tests that can fail": briefer writes acceptance examples, builder does not change expected results); hidden fixtures and verdict authority outside the builder are NEW |
| P121 | Rule 15. End review on frozen acceptance evidence and resolved material findings. Do not end on a comment quota or an arbitrary number of rounds. The paper also says the evidence does not support any particular review-round count. (lines 53, 21) | OPINION | Q00, 2026-10-21 | reviewer | CONFLICTS-WITH-KIT anti-OE:20 and code-review:V-11: the kit stops patching after 3 rounds and escalates, citing an Anthropic measurement that is not in this paper. Tension, not contradiction: the paper's rule is about what ends a review; the kit's cap is about when to reconsider the approach. Both can hold if the cap is phrased as "escalate", not "approve". |

### 1c. Section 1: why agents overengineer and repeat work

| id | lesson | tag | source ids + dates | roles | kit status |
| --- | --- | --- | --- | --- | --- |
| P122 | Current Claude Code guidance warns that gap-seeking reviewers often report gaps even when the work is sound, and that implementing every suggestion creates unnecessary abstraction and defensive code. Limits: no comparative study, no incidence rate, no Opus 5.5 effect size; it cannot be called the biggest cause. (line 58) | EXPERIENCE | A02, accessed 2026-10-21 | reviewer, feature, quick | ALREADY-IN-KIT anti-OE:18, code-review:V-11 |
| P123 | Opus 5 could widen task scope and over-verify when old mandatory-verification scaffolding stayed in the prompt. A03 recommends its own patterns as a starting point for 5.5. Pre-cutoff model evidence, not a measured 5.5 result. (line 59) | EXPERIENCE | A04 (model-specific living docs), A03, accessed 2026-10-21 | lead, all (prompt authors) | NEW; mild tension with anti-OE:16 (done means checked, one end-to-end check) if those rules were ever copied as mandatory verification steps into agent prompts |
| P124 | Older models (the paper names Opus 4.5 and 4.6 in the A05 overengineering paragraph) were documented making unnecessary abstractions and speculative flexibility. Historical mechanism, not proof of equal frequency on 5.5. (line 60) | EXPERIENCE | A05, accessed 2026-10-21 | all | ALREADY-IN-KIT anti-OE (intro) says over-building is "the most common failure of AI-written code"; the paper says no ranking is established, see section 6 contradiction K-1 |
| P125 | Overly broad investigation, irrelevant conversation and bloated instruction files are documented failure patterns. No ranking or isolated causal effect. (line 61) | EXPERIENCE | A02, accessed 2026-10-21 | all | ALREADY-IN-KIT (partial) `rules/assistants/claude.md` (keep CLAUDE.md plus imports under 200 lines); broad investigation and stale conversation are NEW |
| P126 | Treat ambiguous requirements, missing knowledge of existing code, weak oracles, scope creep and review incentives as hypotheses to sort in your own rework log. Do not publish a ranked list of causes without comparison data. Count defects per accepted change, not lines added: a valid safety check adds code and lowers risk. (line 63) | OPINION (no id in paper; Q00 assumed) | none cited | qa, lead | NEW |
| P127 | Pick the intervention that matches the failure. Underspecified expected result: needs a design decision. Unfamiliar API: needs a reference or an executable probe. Wrong computation: needs a failing example. Speculative abstraction: needs scope control. False-positive review: needs a stronger finding standard. More reasoning effort does not supply a missing product decision; more reviewers do not repair a weak oracle. These are diagnostic distinctions, not measured effect sizes. (line 67) | OPINION | Q00, 2026-10-21 | all | NEW |
| P128 | Necessary defense versus clutter: ask who can violate the assumption and how the caller handles the failure. A public boundary needs the checks its contract requires. Repeating the same checks through trusted internal helpers hides the real boundary and adds upkeep. Deleting validation only to cut lines is omission, not simplicity. Make the agent state the concrete failure a check prevents and how that failure is tested. (line 69) | OPINION | Q00, 2026-10-21 | feature, quick, reviewer | ALREADY-IN-KIT anti-OE:9, 10, network N-02; "state the failure it prevents and how it is checked" is NEW |
| P129 | Which rework cause is biggest is unknown for this studio. Build a local rework record with consistent denominators (the paper's section 10, extracted by another agent). A vendor warning shows a plausible mechanism, not its frequency or causal weight in Roblox work. (line 71) | OPINION | Q00, 2026-10-21 | qa, lead | NEW (pointer to part with section 10) |

### 1d. Section 2: first-try success with current Claude models

| id | lesson | tag | source ids + dates | roles | kit status |
| --- | --- | --- | --- | --- | --- |
| P130 | Current model guidance: set effort explicitly, start at medium, compare levels locally, and keep xhigh and max for work where a quality gain was measured. This is not advice to lower effort on every safety-critical task. (line 82) | VERIFIED prefix at line 82 (A03 is EXPERIENCE in the register and line 146); see I-1 | A01, A03, accessed 2026-10-21 | all (lead sets effort) | ALREADY-IN-KIT anti-OE:15. Nuance: the paper says "explicitly start at medium"; the kit says "medium is Opus 5.5's default" and "with fewer steps"; neither "default" nor "fewer steps" appears in the paper |
| P131 | The 39-of-40 result: Anthropic reports success in 39 of 40 attempts at improving load time on every page of a web app (Opus 5.5, release 2026-09-22). Number of apps, independence of trials, exact success rule, repair iterations, effort and evaluator are not disclosed in the passage. It is not 39 of 40 first patches and it is not Roblox. (line 85) | VERIFIED (vendor report) | A01, 2026-09-22 | all, lead | NEW (guard against citing it as a first-try rate) |
| P132 | FrontierCode v1.1 (merge-worthiness benchmark): main result at medium effort is 54.6%; the table result at max effort is 54.4%. Task count not disclosed; no uncertainty given. Do not read the 0.2-point gap as medium being better; the benchmark run may include many agent edits. (line 86) | VERIFIED (vendor report) | A01, 2026-09-22 | lead, perf | NEW; consistent with anti-OE:15 |
| P133 | The current guide says medium matched or beat Opus 5 at high on coding and knowledge-work evaluations. Counts and effect size are not disclosed, and it is not an ablation of specs, tests-first or reviewers. (line 87) | EXPERIENCE | A03, accessed 2026-10-21 | lead | ALREADY-IN-KIT anti-OE:15 (adds "fewer steps", not in the paper) |
| P134 | The guide says time signals shortened completion time for small agent teams. The task type was research, not coding or Roblox; no public count. Time pressure can reduce searching and verification, so do not add deadlines to build or review prompts on this basis. (line 88) | EXPERIENCE | A03, accessed 2026-10-21 | lead | NEW |
| P135 | No post-2026-09-01 primary study was found that isolates the Roblox first-try gain from tests-first, more detailed specs, reading before writing, more reviewers or a six-role team. Never invent percentages. Docs support trying these practices, not promising a success rate. (line 90) | OPINION | Q00, 2026-10-21 | all | NEW |
| P136 | Definition of first try: the builder's first submitted commit passes the protected acceptance job with no reviewer-requested repair. The builder's normal local edit and test loop may run inside the trial, but report its edits, time and test runs separately so a long repair session is not called one shot. Publish (successful first submissions) / (all assigned eligible tasks) together with the blocked and infrastructure-failed counts; do not drop hard tasks. (line 92) | OPINION (no id in paper; Q00 assumed) | none cited | qa | NEW |
| P137 | Evaluate practices with paired, reset-repository experiments on representative Luau tasks, one factor at a time. Factors named: terse versus executable spec; contract fixtures before versus after implementation; medium versus high effort; one builder versus writer plus reviewer; fresh context packet versus accumulated conversation. Hold constant: task mix, tool access, runtime limits, acceptance grader. Randomize order, keep raw counts and uncertainty, compare cost per accepted patch and escaped defects, not only pass rate. A local pilot is a proposal, not a published benchmark. (line 94) | OPINION (no id in paper; Q00 assumed) | none cited | qa, lead | NEW |
| P138 | Checklist use is proportional. It is a proposed procedure, not a measured Opus 5.5 improvement. Use the steps that apply and record why a material check was skipped. It must not become a planning ritual longer than the patch. (line 98) | OPINION | Q00, 2026-10-21 | all | ALREADY-IN-KIT (spirit) anti-OE:3, 8; the "record why a check does not apply" is NEW |
| P139 | Before code: restate the player-visible behavior in testable terms, with a positive example, a meaningful boundary, and the old behavior that must stay. Resolve a design ambiguity instead of inventing the owner's answer. (line 102) | OPINION | Q00, 2026-10-21 | feature, quick, architect | ALREADY-IN-KIT anti-OE:3 (state the assumption); "positive example, boundary, old behavior" NEW |
| P140 | Before code: read the real implementation and the affected callers; find existing helpers, conventions, data shapes and test entry points. Do not infer the repo from file names or a stale summary. (line 104) | OPINION | Q00, 2026-10-21 | all | ALREADY-IN-KIT `AGENTS.md` §0 (read before guessing) |
| P141 | Before code: check the current API, language support and solver/runtime configuration. Separate upstream Luau availability from Roblox rollout. Keep a source reference for any unfamiliar member. (line 106) | OPINION | Q00, 2026-10-21 | feature, quick, reviewer | ALREADY-IN-KIT code-review:V-04; separating upstream from Roblox rollout is NEW (luau-current:B partly does it) |
| P142 | Before code: state what is out of scope. For any new abstraction, dependency or custom replacement, write the concrete requirement; if there is none, use the existing mechanism. (line 108) | OPINION | Q00, 2026-10-21 | feature, quick, architect | ALREADY-IN-KIT anti-OE:1, 5, 7 |
| P143 | Before code: freeze the acceptance criteria and protect withheld fixtures. Record a baseline for the behavior and for any performance-sensitive workload. Record a pre-existing failure as such, so it is not blamed on the candidate later. (line 110) | OPINION | Q00, 2026-10-21 | qa, feature, perf | ALREADY-IN-KIT (partial) performance:F-07 (baseline), code-review/testing; "record pre-existing failure" and withheld fixtures NEW |
| P144 | Before code: choose the responsible integrator and the smallest useful analysis effort. Start specialist or parallel work only for a real uncertainty, not because six roles exist. (line 112) | OPINION | Q00, 2026-10-21 | lead, all | NEW (kit orchestration is by job size; this is a per-task caution) |
| P145 | While coding: do the narrow behavior first, keep the existing vocabulary and local style, prefer a direct built-in with the needed semantics over a handwritten substitute or a forwarding wrapper. (line 116) | OPINION | Q00, 2026-10-21 | feature, quick | ALREADY-IN-KIT anti-OE:5, 8 |
| P146 | While coding: names carry domain meaning and units. Make absence, failure and valid values explicit at the interface. Never hide an unexpected internal error behind a plausible default. (line 118) | OPINION | Q00, 2026-10-21 | feature, quick | NEW (see P160, P164) |
| P147 | While coding: run the relevant analyzer and the smallest applicable behavior checks on the actual changed code, and read the output. A generated test file or a suggested command is not a test run. (line 120) | OPINION | Q00, 2026-10-21 | feature, quick, qa | ALREADY-IN-KIT anti-OE:16, code-review/testing (a result counts only if it ran) |
| P148 | While coding: keep acceptance-test changes distinguishable from implementation changes. Never edit protected fixtures or expected results only to make the candidate pass. (line 122) | OPINION | Q00, 2026-10-21 | feature, quick, reviewer | ALREADY-IN-KIT anti-OE:12; code-review/testing |
| P149 | While coding: when a claimed optimization adds complexity, keep the old baseline and measure the candidate in the same environment. With no measured bottleneck, postpone intrusive optimization. (line 124) | OPINION | Q00, 2026-10-21 | feature, perf | ALREADY-IN-KIT performance:F-07, rule "no performance claim without a number" |
| P150 | While coding: when the API or a design assumption turns out false, stop that part and return the smallest decision needed. Do not widen scope silently. (line 126) | OPINION | Q00, 2026-10-21 | feature, quick | ALREADY-IN-KIT anti-OE:4b, `AGENTS.md` §4 (needs-decision) |
| P151 | After coding: run the required checks against the exact candidate revision. Record PASS, FAIL, BLOCKED or NOT RUN with environment and logs. Rebuild any artifact whose source changed after its earlier check. (line 130) | OPINION | Q00, 2026-10-21 | qa, feature | ALREADY-IN-KIT (partial) `AGENTS.md` §3.5 labels, code-review:V-10; the four-state vocabulary and "rebuild after source change" are NEW |
| P152 | After coding: write a short change manifest and run the simplicity checklist (section 5). Remove accidental debug output, dead modes and speculative extension points that are not accepted behavior. (line 132) | OPINION | Q00, 2026-10-21 | feature, quick | ALREADY-IN-KIT anti-OE:14 (temporary files); change manifest NEW |
| P153 | After coding: the reviewer must substantiate each material finding. Fix demonstrated defects; investigate hypotheses; treat preferences as non-blocking unless they break a settled project rule. (line 134) | OPINION | Q00, 2026-10-21 | reviewer, feature | ALREADY-IN-KIT code-review:V-06; mild difference: kit says style items are "not reported" at all (V-11, anti-OE:18), the paper keeps them as non-blocking |
| P154 | After coding: QA runs the protected acceptance job and the required engine scenario. For performance-sensitive changes, attach baseline and candidate traces from the declared device or runtime so they can be compared. (line 136) | OPINION | Q00, 2026-10-21 | qa, perf | ALREADY-IN-KIT (partial) code-review/testing lanes, performance:F-07 |
| P155 | After coding, when repair was needed: keep the failed candidate, add the right regression test or a scoped rule, and classify the cause as requirement change, code defect, evaluator defect or infrastructure failure. (line 138) | OPINION | Q00, 2026-10-21 | qa, feature | NEW (links to the rework record in the paper's section 10) |
| P156 | After coding: present the owner with behavior, evidence and residual uncertainty. A patch is not released because the model ended its turn or a tool accepted a job. (line 140) | OPINION | Q00, 2026-10-21 | all | ALREADY-IN-KIT anti-OE:16 (text-only status is a report, not completion) |

### 1e. Section 3: professional code craft

| id | lesson | tag | source ids + dates | roles | kit status |
| --- | --- | --- | --- | --- | --- |
| P157 | Nystrom (2014): prefer a direct solution; start from suitable data structures and algorithms; short code can still hide expensive loops or recursion. Simplicity is about reasoning cost and run cost, not code golf. (line 152) | EXPERIENCE | C02, 2014 (chapter accessed 2026-10-21) | all | NEW |
| P158 | Ousterhout and Martin (published discussion, 2024-09 to 2025-02): Ousterhout likes functions that hide a lot of work behind an easy interface; Martin likes meaningful decomposition with descriptive extracted operations. Both accept that code can be over-decomposed; they differ on how readily extraction helps the reader. Ousterhout flags code that makes the reader jump back and forth between pieces. (line 154) | EXPERIENCE | C03, September 2024-February 2025 | all | NEW |
| P159 | Make the agent show what knowledge an abstraction removes. A helper earns its place if (a) callers can trust a clear contract without reading the body, (b) it consolidates a real shared policy, or (c) it isolates a testable transformation. A wrapper that only renames a call or forwards options buys little unless it makes a real boundary. A long coherent calculation should not be split to satisfy a line count. No researched source sets a Luau function-length cap or a maximum nesting depth. (line 156) | OPINION (synthesis) | C02, C03 | architect, feature, reviewer | ALREADY-IN-KIT (partial) anti-OE:5, architecture:R-09; the three tests (a)-(c) and "do not split a coherent calculation" are NEW |
| P160 | Names show domain meaning and units: cooldownSeconds not delay, rewardCoins not amount, targetUserId not id. A boolean parameter must not silently pick between unrelated operations. Comment why a surprising branch exists, the contract that makes a shortcut valid, and the measured reason an odd optimization stays. Do not narrate assignments. Where types and names cannot carry a condition, a short contract comment beats making readers rebuild it. (line 160) | OPINION (adaptation) | C01, C03 | feature, quick, reviewer | ALREADY-IN-KIT (partial) anti-OE:13, architecture:R-10; unit-bearing names and the boolean-parameter rule are NEW |
| P161 | Cooldown example (untested): rename an opaque three-parameter helper to a unit-named one, add a comment that all timestamps use one monotonic clock in seconds, keep the one-line max(0, duration - elapsed) result. The gain is a readable contract, not fewer lines. No clock-provider interface, factory or generic cooldown framework. (lines 166-192) | OPINION (illustration, unexecuted) | C01, C02, C03 | feature, quick | ALREADY-IN-KIT architecture:R-04 (name the clock), anti-OE:5 |
| P162 | Reward example (untested): fold three single-use helpers (get base, apply multiplier, floor) into one rewardCoins function. Valid only because the helpers add no independent meaning here. If rounding, caps or reward calculation are genuinely shared policies, consolidating those stays valuable. (lines 194-222) | OPINION (illustration, unexecuted) | C02, C03 | feature, reviewer | ALREADY-IN-KIT anti-OE:5 |
| P163 | Epic's Lore error policy (a Rust storage and version-control project, not an Unreal or Roblox rule): typed errors that propagate instead of production panics; expected user-caused errors are told apart from unexpected faults and do not deserve warning logs. (line 226) | VERIFIED | C09, accessed 2026-10-21 | architect, feature | ALREADY-IN-KIT architecture:R-13 (done / denied / unavailable), networking-security:N-14 (quiet logs for denials) |
| P164 | Sort errors into three kinds: rejection of untrusted input, recoverable service failure, violated internal assumption. An internal helper with trusted typed input must not quietly turn a programmer error into zero. A boundary parser must reject bad input explicitly, not cast and hope. Type annotations do not excuse skipping validation where data enters from outside the contract. Do not stack identical runtime checks through every helper unless the data can change or re-enter by an untrusted route. (line 228) | OPINION (adaptation) | C01, C09 | feature, reviewer, quick | ALREADY-IN-KIT anti-OE:9, 10, networking-security:N-02; the three-way split is NEW |
| P165 | parseCount example (untested): reject non-numbers, NaN (self-inequality), values below 1 or above a caller-supplied maximum, and non-whole values; return nil. The maximum is a product rule, not a Roblox limit. The core calculation can then take plain number. A returned nil is not a successful zero-value transaction, and broad error suppression is not a way to find a broken internal assumption. (lines 230-250) | OPINION (illustration, unexecuted) | C09 | feature, quick | ALREADY-IN-KIT networking-security:N-02 (same intent; uses math.isfinite instead of self-inequality) |
| P166 | Acton's CppCon 2014 talk frames programs as data transformations, aimed at performance-critical console C++. The accessible abstract shows that scope; it is not evidence of a Luau speedup. (line 254) | EXPERIENCE | C05, 2014-07-23 announcement / 2014-09-29 video | perf, architect | NEW |
| P167 | Nystrom's data-locality chapter: do locality work when a real performance problem involves cache misses, and it can be confined to a few core structures instead of everywhere. His C++ benchmark is not a Roblox benchmark. (line 256) | EXPERIENCE | C04, 2014 | perf | NEW |
| P168 | Data-oriented thinking, applied: first ask which data this operation reads, how much, how often, and which of it is needed. Remove needless traversal and repeated work before asking for an ECS or structure-of-arrays rewrite. In Luau, do not assume C++ contiguous-memory or cache-layout guarantees from a similar-looking table layout. The performance engineer compares the real alternatives in the real runtime with the real workload. Data-oriented design does not mean "keep designer settings in tables". (line 258) | OPINION (synthesis) | C04, C05, C07 | perf, architect | ALREADY-IN-KIT (partial) architecture:R-15 (ECS only after a benchmark of a real slice); the rest NEW. C07 is cited but the paper never says what it contributes (see U-4) |
| P169 | For exact-equality membership in a dense array, use the built-in table.find rather than building an intermediate set or hand-writing a search. A custom loop is right for a different predicate or traversal. Whether to keep an index is a separate choice that needs lookup and update frequency and a measurement. No speedup is claimed. (lines 260-268) | OPINION | Q00, 2026-10-21; language basis L12, L13 | feature, quick, reviewer, perf | NEW |
| P170 | The simplicity checklist for an AI reviewer needs concrete answers, not a numeric style score. Nine questions are in section 5. (line 272) | OPINION (synthesis) | C01, C02, C03, C04, C08 | reviewer | ALREADY-IN-KIT (partial) anti-OE "Checks a reviewer can apply"; several questions are NEW (units at call site, same policy vs look-alike, comment still true, what grows with player count) |
| P171 | Section 3 summary rows. Prefer less reasoning over tiny functions, with no universal line cap (OPINION, C03, 2024-2025). State units and meaningful contracts, with no comment-count target (VERIFIED standard, OPINION Luau adaptation; C01). Optimize the relevant data transformation, with no portable C++ to Luau speedup (EXPERIENCE and scoped OPINION; C04, C05, 2014). (lines 293-295) | mixed, as listed | C01, C03, C04, C05 | all | covered by P111, P113, P159, P160, P167, P168 |

### 1f. Section 4: writing current Luau

| id | lesson | tag | source ids + dates | roles | kit status |
| --- | --- | --- | --- | --- | --- |
| P172 | The upstream Luau repo lists 0.743 as its latest release (2026-10-16). Its notes mention a faster table.find (especially for small arrays and values with no __eq metamethod), clearer diagnostics for read-only and write-only properties, and improved local-register lifetimes. This is upstream, not proof that every Roblox client or server runs that revision. (line 301) | VERIFIED | L01 (= T04), 2026-10-16 | all | NEW |
| P173 | Solver status: Roblox announced general release of the new solver for nocheck and nonstrict users on 2025-11-20; strict users opt in. The old solver was promised to stay available through 2026. Strict beta users had to set Workspace.UseNewLuauTypeSolver explicitly when the beta toggle was removed in January 2026. The property is still in the current Workspace reference and is Not Scriptable (so it is not set from a script). The current default for every project was not independently established. (line 303) | VERIFIED | L02, 2025-11-20; L03, accessed 2026-10-21 | all | ALREADY-IN-KIT code-review/luau-current:C (same facts); the "Not Scriptable" detail and "default not established" hedge are NEW |
| P174 | With each submitted change, record the Studio version, solver choice, analyzer version and any enabled language betas. A builder must not switch the solver or weaken checks to make an error go away. Reproduce a suspicious diagnostic with a minimal example before adding casts. Pin external analysis tools separately from the engine, because Roblox controls engine rollout. (line 305) | OPINION | Q00, 2026-10-21; basis L01-L03 | feature, reviewer, qa | ALREADY-IN-KIT (partial) code-review/testing ("record the Studio build with every engine test run"); solver, analyzer and beta recording and the no-silent-solver-change rule are NEW |
| P175 | const: upstream 0.711 (2026-03-06) added const bindings; const blocks reassigning the binding, not mutating the value it holds. Roblox's if local / if const syntax is labeled Studio Beta (2026-10-06). Do not copy a blanket "Luau has no const" rule from old prompts; equally, do not assume every upstream feature is on in the project. Keep production examples on syntax verified for the project. An RFC alone is not rollout evidence. The paper does not say whether plain const bindings are live in Roblox. (line 307) | VERIFIED (L04, L05, L06); OPINION (policy) | L04, 2026-03-06; L05, accessed 2026-10-21; L06, 2026-10-06; Q00 | all | NEW. luau-current:B lists if local / if const as beta (do not ship) but does not mention const bindings at all |
| P176 | Luau is gradually and structurally typed, with strict, nonstrict and nocheck modes. A cast changes only what the checker believes; casting an expression that returns several values keeps only the first. Policy: new production modules start strict; annotate public inputs, outputs and important record shapes; let obvious locals infer. A proposed policy, not a measured optimum and not a proof of runtime correctness. (line 311) | VERIFIED (L07); OPINION (policy) | L07, accessed 2026-10-21 | all | ALREADY-IN-KIT `AGENTS.md` §2, luau-current:C (exported function types). Paper is wider than `AGENTS.md` §2 ("strict in shared and server code"): it says all new production modules. Cast-on-multiple-results is NEW |
| P177 | any allows arbitrary use with no further checks; unknown must be narrowed before it is used as something specific. Generics keep the relation between input and output types that any discards. Use unknown at untrusted boundaries and narrow it; use a generic only when a reusable operation really preserves a type relation; do not build type-level machinery to avoid a plain record type. (line 313) | VERIFIED (L08, L09); OPINION (policy) | L08, L09, accessed 2026-10-21 | all | ALREADY-IN-KIT (partial) luau-current:C (`:: any` only at true boundaries with a comment); unknown plus narrowing is NEW |
| P178 | Type tests, equality, truthiness and assert can narrow types. Prefer a runtime check that narrows over `:: any` or a cast that tells the checker to trust. Checks should reflect the domain, not only the primitive shape. (line 315) | VERIFIED (L10); OPINION (policy) | L10, accessed 2026-10-21 | feature, quick, reviewer | NEW |
| P179 | Roblox requires the server to validate all client data and separates checks on type and structure, values, and context. Static annotations do not replace boundary validation. A quantity from a client should be a finite, bounded integer, not just a number. A purchase still needs authorization, balance and transactional checks beyond this. (line 317) | VERIFIED (L11); OPINION (example) | L11, accessed 2026-10-21 | feature, reviewer | ALREADY-IN-KIT networking-security:N-02 |
| P180 | parseQuantity example (untested): same shape as parseCount, under `--!strict`, input typed unknown. Comment: the bounds reject infinities and self-inequality rejects NaN. The trusted caller must pass a positive, finite maximum; the checker cannot prove it. Do not "fix" it by returning `value :: number` before validating. (lines 319-349) | OPINION (illustration, unexecuted) | L08, L10, L11; Q00 | feature, quick | ALREADY-IN-KIT networking-security:N-02 |
| P181 | Generic first<T> example (untested): returns the first item or nil. Its value is the input to output type relation and the explicit absent case, not speed; no speed claim is made. (lines 351-361) | OPINION (illustration, unexecuted) | L09; Q00 | feature | NEW |
| P182 | Table semantics. table.create reserves array capacity only (not dictionary capacity), and with no fill value the table stays empty. table.clear keeps capacity. table.clone is shallow and returns an unfrozen copy. table.freeze works in place and is not recursive. string.find with plain=true searches literally. table.concat joins an array range. (line 365) | VERIFIED | L12, accessed 2026-10-21 | feature, quick, reviewer, perf | NEW |
| P183 | Policy on those operations: preallocate arrays of known size; clear only buffers that one owner reuses; say out loud when shallow aliasing is assumed; never reuse a buffer while its consumer still needs the old contents; do not turn every temporary into a global pool. (line 367) | OPINION | Q00, 2026-10-21; basis L12 | feature, perf, reviewer | NEW |
| P184 | Iteration semantics. Generalized iteration visits the contiguous array part in order, then the remaining entries in no guaranteed order. Changing keys other than the current one during iteration has unspecified behavior, except a documented exception for appending to a dense array. Policy: do not depend on dictionary order for reproducible results (collect and sort explicit keys); do not mutate the traversed dictionary from inside the loop; gather pending changes in a second collection. (line 369) | VERIFIED (L05); OPINION (policy) | L05, accessed 2026-10-21 | feature, quick, reviewer | NEW. Fact-check this: the "keys other than the current key" statement is stronger than the usual reading of the Luau docs |
| P185 | Luau performance docs say generalized iteration, pairs and ipairs are about equally fast when optimized; ipairs stops at the first nil. They describe optimized imported global chains, colon method calls and specialized builtins, discourage old method-localization tricks, warn that getfenv, setfenv and loadstring can invalidate environment optimizations, and advise avoiding temporary table or userdata allocations in tight loops. Policy: review loop meaning and measured allocation first; do not demand blanket pairs to ipairs rewrites, local aliases for every math function, or handwritten replacements of builtins. (line 371) | VERIFIED (L13); OPINION (policy) | L13, accessed 2026-10-21 | reviewer, perf, feature | ALREADY-IN-KIT (partial) luau-current:A (getfenv/setfenv disable optimization); the rest NEW |
| P186 | scaled example (untested): create the result with table.create sized to the input and fill by index, returning a new caller-owned table. It is not necessarily the right policy for a measured per-frame hot path. (lines 373-391) | OPINION (illustration, unexecuted) | L12; Q00 | feature, perf | NEW |
| P187 | The Luau runtime recap (2025-12-19) documents compile-time constant folding for string.char, string.sub, string concatenation and interpolation where constants allow, plus inlining gains. It does not show that all string work is optimized away. (line 395) | VERIFIED | L14, 2025-12-19 | perf, reviewer | NEW |
| P188 | Strings: Roblox documents string patterns, interpolation and lexicographic comparison, so numeric-looking strings do not sort numerically. Policy: interpolation for readable fixed messages; table.concat for an assembled list of fragments when that shape fits; profile large builders instead of declaring either fastest; literal search for user-supplied literal text; parse numeric fields before comparing numbers; never make a display string the stored numeric state. (line 397) | VERIFIED (L15); OPINION (policy) | L15, accessed 2026-10-21; basis L12, L14 | feature, quick, reviewer | NEW |
| P189 | Native code generation is documented as a server-side script feature. It uses --!native or per-function @native, suits arithmetic-heavy Luau and not heavy engine or library calls, and must be judged by profiler results with and without it. Costs: compile and startup time, extra code memory, and a game-wide compiled-code limit. The page publishes no universal speed factor and no exact limit. Wrong argument types or environment manipulation can cause fallback or deoptimization. (line 401) | VERIFIED | L16 (= R11), accessed 2026-10-21 | perf, feature | ALREADY-IN-KIT performance:F-10, luau-current:C (annotate Vector3 for native); the cost list and "no published multiplier or limit" are NEW |
| P190 | Android native generation: upstream's runtime recap reports an Android-capable native backend with production testing (2025-12-19); Roblox's spring roadmap (2026-05-08) still listed Android native generation as a scheduled item (register line: Ongoing, Mid 2026). Different scopes. Do not promise native speedups for all clients. Before budgeting on client native generation, confirm a current Roblox shipping announcement and profile the target device. (line 403) | VERIFIED (L14, L17); OPINION (synthesis) | L14, 2025-12-19; L17, 2026-05-08; L16 | perf | NEW |
| P191 | Native acceptance procedure: pick one measured server hotspot; keep identical inputs and outputs; run repeated enabled and disabled runs under the same load; record CPU time, server startup time and memory; keep native only if it improves the project's actual acceptance criteria. No universal minimum gain, sample count or native memory budget was found. Do not mark every module native "just in case". (line 405) | OPINION | Q00, 2026-10-21; basis L16 | perf | ALREADY-IN-KIT (partial) performance:F-10 ("measured both ways"); the recorded-metrics procedure is NEW |
| P192 | The native-code page contradicts itself: the enable section mentions top-level native compilation if profitable, while best practices says only functions are compiled. Do not promise top-level speedup; target an explicit function and read the profiler. (line 407) | VERIFIED (L16 contradiction); OPINION (rule) | L16; Q00, 2026-10-21 | perf | NEW |
| P193 | Luau's separate linter covers unknown globals, unused functions and locals, duplicate conditions, misleading and/or expressions and wrong table operations. It singles out `#t` as a test for an empty dictionary as a common bug. The type checker is separate from the linter. Policy: resolve relevant diagnostics instead of mass-suppressing; a narrow suppression needs a reason; prefer an if-expression to a truthiness-based pseudo-ternary when the chosen value can be false or nil. (line 411) | VERIFIED (L18); OPINION (policy) | L18, accessed 2026-10-21 | reviewer, feature, quick | NEW (testing.md lists "lint" in the gate but not these rules) |
| P194 | Roblox names deep-cloning or serializing large tables and expensive per-frame work as performance problems. Look first for repeated work, oversized traversals and allocation at event frequency. Do not spend review rounds on punctuation-level micro-optimizations while those remain. (line 413) | VERIFIED (L19 = R06); OPINION (policy) | L19, accessed 2026-10-21 | reviewer, perf | ALREADY-IN-KIT (partial) performance:F-07, F-03; "no review rounds on micro-optimizations" is NEW |
| P195 | Luau checklist of ten items (listed in section 5): record engine, analyzer, solver and beta settings; strict new modules; unknown plus narrowing; generics only to keep relations; choose iteration by order and nil semantics; state shallow-copy, freeze and buffer ownership; keep builtins idiomatic; do not confuse numbers with numeric strings; native only after measured benefit on a supported target; fix meaningful lint findings and measure costly repeated work first. (lines 415-435) | OPINION | Q00, 2026-10-21; sources L01-L19 | all | NEW as one list; items overlap P174-P194 |
| P196 | Not established by the sources: a universal Luau function-size target, the best annotation density, a blanket allocation count, a minimum native speedup, a safe number of casts. The answer is project-specific acceptance evidence, not invented industry numbers. (line 437) | OPINION | Q00, 2026-10-21 | all | NEW (extends P106) |
| P197 | Section 4 closing-rule rows (lines 441-448): record the language and solver target (VERIFIED; L01 2026-10-16, L02 2025-11-20); new production code strict (OPINION; L07); narrow unknown, justify any and casts, no safe cast count (OPINION; L08-L11); state copy, freeze and buffer semantics (VERIFIED / OPINION; L12); choose iteration by semantics (VERIFIED; L05, L13); profile native candidates, no universal multiplier (VERIFIED / OPINION; L16); fix meaningful lint warnings, no universal suppression allowance (OPINION; L18). | mixed, as listed | L01, L02, L05, L07-L13, L16, L18 | all | covered by P172-P194 |

---

## 2. Numbers table

| # | value | unit | job | source | scope and hedge | paper line |
| --- | --- | --- | --- | --- | --- | --- |
| N1 | 39 successes of 40 attempts | count | measurement (vendor report) | A01, 2026-09-22 | Opus 5.5; optimizing load time of every page of a web app. Not first patches. Not Roblox. Apps, independence, success rule, repairs, effort, evaluator undisclosed | 85 |
| N2 | 54.6 | percent | measurement (vendor report) | A01 | FrontierCode v1.1 main result at medium effort; task count undisclosed | 86 |
| N3 | 54.4 | percent | measurement (vendor report) | A01 | FrontierCode table result at max effort; no uncertainty disclosed | 86 |
| N4 | 0.2 | percentage points | derived (N2 minus N3) | A01 | Paper warns it must not be read as medium beating max | 86 |
| N5 | 2026-09-22 | date | fact | A01 | Opus 5.5 release | 11, 82 |
| N6 | 2026-09-01 | date | proposed rule | Q00 | Results on models released before this date are not measured evidence for this stack | 19 |
| N7 | medium; high; xhigh; max | effort levels | guidance | A03 | Start at medium, compare locally; xhigh and max only where a gain was measured | 82 |
| N8 | 60 | frames per second | API default | R01, accessed 2026-10-21 | Roblox games target 60 FPS by default; not a guarantee | 45 |
| N9 | 16.67 | milliseconds | derived frame period | R01, R03 | Paper's wording. The R03 register quote says CPU time must be below 16 ms for a 60 FPS client. Not a script-only budget | 45 |
| N10 | 0.743 | Luau version | measurement (upstream latest) | L01, 2026-10-16 | Not proof of the version Roblox runs | 301 |
| N11 | 0.711 | Luau version | fact | L04, 2026-03-06 | Added const bindings upstream | 307 |
| N12 | 2025-11-20 | date | fact | L02 | New solver general release; January 2026 = beta toggle removal; old solver promised through 2026 | 303 |
| N13 | 2026-10-06 | date | fact | L06 | if local / if const announced as Studio Beta | 307 |
| N14 | 2025-12-19; 2026-05-08 | dates | facts | L14; L17 | Upstream runtime recap; Roblox spring roadmap listing Android native generation | 395, 403 |
| N15 | 1; maximum (caller supplied); % 1 ~= 0 | integer bounds | illustration only | Q00 | Count and quantity parsers reject below 1, above a caller-supplied maximum, and non-whole values. The maximum is a product rule, not a Roblox limit | 240, 333-339 |
| N16 | successful first submissions / all eligible assigned tasks | ratio | proposed metric | Q00 (no id in paper) | Report with blocked and infrastructure-failed counts; no hard tasks dropped | 92 |
| N17 | defects per accepted change | ratio | proposed metric | Q00 (no id in paper) | Preferred over lines added | 63 |
| N18 | cost per accepted patch; escaped defects | metrics | proposed metrics | Q00 (no id in paper) | For comparing experiment arms, with raw counts and uncertainty | 94 |

Numbers the paper says it could NOT find (agents must not supply a figure): universal function length; maximum nesting depth; comment-count target; test count; review-round count; abstraction count; phone memory ceiling; first-try success uplift; native speedup factor or minimum gain; native sample count; native memory budget or compiled-code limit; annotation density; safe cast count; blanket allocation budget; universal suppression allowance (lines 21, 156, 295, 405, 437, 441-448). No Luau speedup figure for table.find is given (line 301, 268).

---

## 3. Luau and engine claims

Star = one of the 15 that would most change code an agent writes. Fact-check these first.

| # | star | claim | paper line | source |
| --- | --- | --- | --- | --- |
| E1 | ★ | const (upstream 0.711) stops reassignment of a binding but not mutation of the value; if local / if const is Studio Beta; plain const rollout in Roblox is not stated | 307 | L04, L05, L06 |
| E2 | ★ | table.create reserves array capacity only and stays empty without a fill value; table.clear keeps capacity; table.clone is shallow and unfrozen; table.freeze is in place and not recursive | 365 | L12 |
| E3 | ★ | Generalized iteration visits the array part in order, then the rest unordered; changing keys other than the current one is unspecified, with an append exception for dense arrays | 369 | L05 |
| E4 | ★ | Generalized iteration, pairs and ipairs perform comparably when optimized; ipairs stops at the first nil | 371 | L13 |
| E5 | ★ | Method-localization tricks are discouraged; getfenv, setfenv and loadstring can invalidate environment optimizations; imported global chains, colon calls and specialized builtins are optimized | 371 | L13 |
| E6 | ★ | Temporary table or userdata allocations in tight loops still cost allocation and GC time; deep-cloning large tables and heavy per-frame work hurt performance | 371, 413 | L13, L19 |
| E7 | ★ | Native code generation applies to server-side scripts; --!native and @native; best for arithmetic-heavy code, poor for heavy engine or library calls | 401 | L16 |
| E8 | ★ | Native costs (compile and startup time, code memory, a game-wide compiled-code limit) and fallback on wrong argument types or environment manipulation; compare profiler results with and without; no published multiplier or limit | 401, 405 | L16 |
| E9 | ★ | The linter flags `#t` used as a dictionary emptiness test | 411 | L18 |
| E10 | ★ | The linter flags misleading and/or; prefer an if-expression to an and/or pseudo-ternary when the value can be false or nil | 411 | L18 |
| E11 | ★ | any permits arbitrary use; unknown must be refined first; generics preserve type relations | 313 | L08, L09 |
| E12 | ★ | A cast on an expression that returns several values keeps only the first value | 311 | L07 |
| E13 | ★ | New solver is generally released for nocheck/nonstrict, strict opts in; Workspace.UseNewLuauTypeSolver is Not Scriptable; current default not established | 303 | L02, L03 |
| E14 | ★ | table.find is the built-in for exact-equality membership in a dense array; 0.743 notes report it faster, especially for small arrays and values without __eq | 301, 264 | L01, L12, L13 |
| E15 | ★ | NaN is detected by self-inequality, infinities by bound checks against a finite maximum, whole numbers by modulo 1 (illustration, unexecuted) | 240, 331-339 | L08, L10, L11 (Q00 example) |
| E16 |  | Upstream 0.743 also reports clearer read-only/write-only property diagnostics and local-register lifetime gains | 301 | L01 |
| E17 |  | Luau is gradually and structurally typed; strict, nonstrict, nocheck modes | 311 | L07 |
| E18 |  | Type tests, equality, truthiness and assert refine types | 315 | L10 |
| E19 |  | Roblox requires the server to validate client data (type/structure, values, context) | 317 | L11 |
| E20 |  | string.find plain=true is literal; table.concat joins an array range | 365 | L12 |
| E21 |  | Constant folding exists for string.char, string.sub, concatenation and interpolation | 395 | L14 |
| E22 |  | Roblox documents string patterns, interpolation and lexicographic comparison | 397 | L15 |
| E23 |  | Native-code page says top-level compilation in one section and function-only in another | 407 | L16 |
| E24 |  | Upstream native backend has Android support (2025-12-19); Roblox roadmap listed Android native generation for mid 2026 (2026-05-08) | 403 | L14, L17 |
| E25 |  | Luau linter is separate from the type checker | 411 | L18 |
| E26 |  | Roblox default target 60 FPS; 16.67 ms frame period | 45 | R01, R03 |
| E27 |  | Upstream release 0.743 dated 2026-10-16 is the latest listed; 0.711 added const | 301, 307 | L01, L04 |
| E28 |  | Old solver stays available through 2026; strict beta users had to enable the property explicitly when the toggle left in January 2026 | 303 | L02 |

---

## 4. Practice claims (Anthropic and Claude behavior, review, testing, evals, other studios)

| # | star | claim | paper line | source and tag |
| --- | --- | --- | --- | --- |
| Q1 | ★ | Claude Code guidance warns that gap-seeking reviewers report gaps even when work is sound; implementing all suggestions adds needless abstraction and defense; "report gaps, not style preferences" | 27, 58 | A02 EXPERIENCE |
| Q2 | ★ | Opus 5 widened scope and over-verified when legacy mandatory-verification scaffolds were kept; A03 recommends its patterns as a starting point for 5.5 | 59 | A04 EXPERIENCE, A03 |
| Q3 | ★ | Start effort at medium and compare locally; reserve xhigh and max for measured gains | 82 | A03 EXPERIENCE (prefixed VERIFIED at line 82) |
| Q4 | ★ | Medium on Opus 5.5 matched or beat Opus 5 at high on coding and knowledge-work evaluations | 87 | A03 EXPERIENCE |
| Q5 | ★ | Opus 5.5 succeeded in 39 of 40 attempts at web-app page load-time optimization | 85 | A01 VERIFIED vendor report |
| Q6 | ★ | No post-2026-09-01 primary study isolates a Roblox first-try uplift for tests-first, specs, reading first, more reviewers or a six-role team (a claim about absence; the checker may try to find one) | 90 | Q00 OPINION |
| Q7 | ★ | Wube (Factorio, 2021-06-18) reproduces a bug in a test before fixing it and uses coverage to find untested or dead branches; tests may depend on tested subsystems, not mocks | 49 | T01 (= C06) EXPERIENCE; see I-5 |
| Q8 | ★ | Ousterhout and Martin both accept over-decomposition can happen; they differ on how readily extraction helps | 33, 154 | C03 EXPERIENCE |
| Q9 |  | FrontierCode v1.1: 54.6% at medium vs 54.4% at max | 86 | A01 VERIFIED vendor report |
| Q10 |  | Time signals shortened completion time for small agent teams on research tasks | 88 | A03 EXPERIENCE |
| Q11 |  | Older models, named Opus 4.5 and 4.6, produced unnecessary abstractions and speculative flexibility | 60 | A05 EXPERIENCE |
| Q12 |  | Broad investigation, irrelevant conversation and bloated instruction files are documented failure patterns | 61 | A02 EXPERIENCE |
| Q13 |  | Opus 5.5 was released 2026-09-22; its benchmarks do not measure this studio | 11 | A01 VERIFIED |
| Q14 |  | The research does not establish that an AI-only team equals a professional team with expert human review | 11 | Q00 OPINION |
| Q15 |  | Nystrom: direct solutions; short code may hide expensive loops | 152 | C02 EXPERIENCE |
| Q16 |  | Epic's C++ standard: intent comments, caller-facing contract details | 37, 158 | C01 VERIFIED |
| Q17 |  | Epic Lore error policy: typed errors, no production panics, user errors not warn-logged (a Rust project) | 226 | C09 VERIFIED |
| Q18 |  | Acton (Insomniac, CppCon 2014): programs are data transformations; scoped to console C++ | 254 | C05 EXPERIENCE |
| Q19 |  | Nystrom: locality work only for real cache-miss problems, confinable to core structures | 256 | C04 EXPERIENCE |
| Q20 |  | A Riot (League) profiling source is cited in a synthesis line; the paper does not say what it supplies | 258 | C07 EXPERIENCE (register date 2018-08-07) |
| Q21 |  | An Epic Lore code-review standard is cited as a basis for the simplicity checklist (register quote: report each finding with its location and a concrete failure) | 272 | C08 VERIFIED |

---

## 5. Checklists and templates in this range

### 5a. Acceptance packet for the owner (line 13)
Intended behavior. The exact candidate (revision). Checks and their outcomes. Observed device performance. Unresolved risks. The decision needed. If consequential uncertainty remains: reduce scope, block release, or get qualified engineering review.

### 5b. First-try success checklist (lines 98-140; proportional, not a ritual)
Before writing code:
1. Restate player-visible behavior in testable terms: a positive example, a meaningful boundary, the old behavior that stays. Ask the owner about a design ambiguity.
2. Read the real implementation and affected callers; find helpers, conventions, data shapes, test entry points.
3. Verify the current API, language support and solver or runtime configuration; separate upstream Luau from Roblox rollout; keep a source reference for each unfamiliar member.
4. State out-of-scope items. Any new abstraction, dependency or custom replacement needs a concrete requirement; without one, use the existing mechanism.
5. Freeze acceptance criteria and protect withheld fixtures; take baselines (behavior and any performance workload); record existing failures as existing.
6. Pick the responsible integrator and the smallest useful analysis effort; add specialists or parallel work only for a real uncertainty.

While writing code:
1. Narrow behavior first; keep local vocabulary and style; use direct built-ins with the right semantics instead of handwritten substitutes or forwarding wrappers.
2. Domain-meaning, unit-bearing names; explicit absence, failure and valid values; do not hide an internal error behind a plausible default.
3. Run the relevant analyzer and the smallest behavior checks on the changed code and read the output; a generated test file or a suggested command is not a run.
4. Keep acceptance-test edits separate from implementation edits; never change protected fixtures or expectations only to pass.
5. For an optimization that adds complexity: keep the old baseline, measure the new one in the same environment; no bottleneck means defer.
6. When the API or a design assumption is contradicted: stop that part and return the smallest decision needed.

After writing code:
1. Run required checks on the exact revision; record PASS, FAIL, BLOCKED or NOT RUN with environment and logs; rebuild artifacts if source changed after their check.
2. Write a short change manifest; run the simplicity checklist; remove stray debug output, dead modes, speculative extension points.
3. The reviewer substantiates material findings; fix demonstrated defects; investigate hypotheses; preferences stay non-blocking unless they break a settled project rule.
4. QA runs the protected acceptance job and the required engine scenario; performance-sensitive changes carry baseline and candidate traces from the declared device or runtime.
5. If repair was needed: keep the failed candidate; add the matching regression or scoped rule; record the class: requirement change, code defect, evaluator defect, infrastructure failure.
6. Show the owner behavior, evidence and residual uncertainty; do not call it released because the model finished or a tool accepted the job.

### 5c. Simplicity checklist for an AI reviewer (lines 272-290; concrete answers, no numeric style score)
1. Are purpose, units, valid values and result clear at the call site?
2. Does each helper remove an independent reasoning burden, or force another body lookup?
3. Can a dead option, unused mode, pass-through function or unreachable branch be removed without changing required behavior?
4. Is duplicated code the same policy, or only look-alike code that must evolve separately?
5. Does a new abstraction serve an observed requirement rather than an imagined feature?
6. Does the code follow existing vocabulary and format, or add a second convention?
7. Does each comment keep a rationale or contract the code cannot express, and is it still true?
8. What grows with player count, item count, frame frequency or lifetime?
9. Is an optimization backed by a workload and measurement, and can it be removed if the benefit goes away?

### 5d. Luau checklist (lines 415-435)
1. Record engine, analyzer, solver and beta settings (L01-L06).
2. Strict new modules; type the boundary contracts, not every obvious local (L07).
3. Prefer unknown plus narrowing; justify every any and cast (L08, L10, L11).
4. Generics keep useful relations, not abstraction ambitions (L09).
5. Choose iteration by ordering and nil semantics (L05, L13).
6. State shallow-copy, freeze and buffer-ownership assumptions (L12).
7. Keep builtins idiomatic; reject blanket local-cache folklore (L13, L14).
8. Do not confuse numeric values with numeric strings (L15).
9. Native only after a measured benefit on the supported target (L16, L17).
10. Fix meaningful lint findings; measure costly repeated work first (L18, L19).

### 5e. Other procedures defined in this range
- Defensive-check test: who can violate the assumption, how does the caller handle failure, what concrete failure does the check prevent, how is that failure tested (P128).
- Abstraction test: callers trust the contract without reading the body; or it consolidates a real shared policy; or it isolates a testable transformation (P159).
- Failure-to-intervention map: underspecified result to a design decision; unfamiliar API to a reference or probe; wrong computation to a failing example; speculative abstraction to scope control; false-positive review to a stronger finding standard (P127).
- Experiment design: factors, constants and metrics (P137).
- First-try measurement definition and reporting (P136).
- Native acceptance procedure (P191).
- Result states: PASS, FAIL, BLOCKED, NOT RUN (P151).
- Repair classes: requirement change, code defect, evaluator defect, infrastructure failure (P155).
- Not in this range (sections 5-11, other extractors): task contract, review comment shape, rework record, test-count guidance. No such template appears in lines 1-449 beyond the pointers above.

### 5f. Illustrative examples (all unexecuted; none is a passing implementation)
Cooldown rename (P161), reward helper fold (P162), parseCount (P165), parseQuantity (P180), generic first (P181), table.find membership (P169), scaled with table.create (P186). The paper states the examples show craft choices, not complete gameplay code (lines 21, 164).

---

## 6. Contradictions, unknowns, and decisions

### Inside the paper
- I-1. Line 82 begins "VERIFIED" for a sentence that cites A01 and A03; A03 is EXPERIENCE in the register (line 869) and in the summary table (line 146). Treat the effort advice as EXPERIENCE.
- I-2. Four statements are tagged bare "OPINION" with no source id (lines 63, 90, 92, 94). They are the paper's proposals; I treat them as Q00.
- I-3. Rule 11 says a 16.67 ms frame period (R01/R03), while the R03 register quote says CPU time must be below 16 ms. Minor numeric difference; the 16.67 figure is derived by the paper (1000/60).
- I-4. L16 contradicts itself on top-level native compilation (line 407). The paper's own response: target explicit functions.
- I-5. Rule 13 relies on T01 (Wube Friday Facts #366, 2021-06-18) for "reproduce the bug as a test first". The register's only quotation for this source concerns thousands of lines being removed. Checker: confirm the article contains the bug-reproduction-in-test practice.
- I-6. The iteration claim in line 369 (changing keys other than the current one is unspecified) cites L05, a "syntax by example" page; checker: confirm the wording and the append exception.
- I-7. Evidence from Opus 5, 4.5 and 4.6 (lines 59-60) is labeled historical, while the evidence conventions (line 19) say only post-2026-09-01 results count as measured evidence. Consistent, but the lead must not use Section 1 as measured proof for 5.5.
- I-8. Forward reference: line 71 points to "section 10" (rework record), outside my range.

### Paper versus kit
- K-1. anti-OE intro says over-building is "the most common failure of AI-written code". The paper says the biggest cause is unknown for this studio and no ranking is supported (lines 58, 71). CONFLICTS-WITH-KIT (wording). Suggested fix: soften to "a common failure".
- K-2. anti-OE:20 and code-review:V-11 set a 3-round cap, with Anthropic numbers (65% to 78% first-round passes, 8.9% to 1.5% with 5+ rounds) that this paper does not contain. The paper says no review-round count is established and review ends on frozen evidence (P121). Both can stand if the cap means "escalate to the lead", and the review's end condition is evidence.
- K-3. anti-OE:15 says Opus 5.5's default effort is medium and that medium gives "fewer steps"; the paper says only "explicitly start at medium" and gives no step counts (P130, P133).
- K-4. code-review:V-11 and anti-OE:18 drop style findings entirely; the paper keeps preferences as non-blocking notes (P153). Minor.
- K-5. luau-current:B has no row for plain `const` bindings (P175). A gap, not a conflict.
- K-6. `AGENTS.md` §2 asks for strict in shared and server code; the paper asks for strict in all new production modules (P176).
- K-7. anti-OE:16 (done means checked) next to A04's over-verification warning (P123): safe as written, but do not copy it into agent prompts as a mandatory verification loop.
- K-8. networking-security:N-02 uses math.isfinite; the paper's examples use self-inequality plus a finite maximum (P165, P180). Equivalent in intent.

### Unknowns the paper leaves open (lines 21, 437)
Universal function length, annotation density, allocation budget, minimum native speedup, safe cast count, first-try uplift, rework cause ranking, phone memory ceiling. Defaults for the lead:
1. Q: keep the 3-round escalation cap? Default: keep, rewording it as "escalate" not "approve" and cite its separate source.
2. Q: may agents ship plain `const`? Default: no until a fact-checker confirms Roblox rollout; if confirmed, add a row to luau-current:B.
3. Q: what to do with unnumbered OPINION lines? Default: tag them Q00 and keep as proposals.
4. Q: should "strict everywhere in new production modules" replace "shared and server"? Default: yes for new modules, no mass rewrite of old ones (anti-OE:8).

---

## 7. Source digest (only the entries my sections cite)

| id | what it is | date | tag | URL |
| --- | --- | --- | --- | --- |
| A01 | Anthropic Opus 5.5 release (39 of 40; FrontierCode) | 2026-09-22 | VERIFIED | https://www.anthropic.com/claude-opus-5-5 |
| A02 | Claude Code best practices (report gaps, not style) | living, accessed 2026-10-21 | EXPERIENCE | https://code.claude.com/docs/en/best-practices |
| A03 | Prompting Claude Opus 5.5 (effort advice) | living, accessed 2026-10-21 | EXPERIENCE | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 |
| A04 | Prompting Claude Opus 5 (over-verification) | living, accessed 2026-10-21 | EXPERIENCE | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 |
| A05 | Prompting best practices (do not speculate about unopened code) | living, accessed 2026-10-21 | EXPERIENCE | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| C01 | Epic C++ Coding Standard for Unreal Engine | undated, accessed 2026-10-21 | VERIFIED | https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine?lang=en-US |
| C02 | Nystrom, Architecture, Performance, and Games | 2014 | EXPERIENCE | https://gameprogrammingpatterns.com/architecture-performance-and-games.html |
| C03 | Ousterhout and Martin discussion | 2024-09 to 2025-02 | EXPERIENCE | https://github.com/johnousterhout/aposd-vs-clean-code |
| C04 | Nystrom, Data Locality | 2014 | EXPERIENCE | https://gameprogrammingpatterns.com/data-locality.html |
| C05 | Acton CppCon keynote | 2014-07-23 / 2014-09-29 | EXPERIENCE | https://cppcon.org/2014/07/ |
| C06 = T01 | Wube Friday Facts #366 | 2021-06-18 | EXPERIENCE | https://factorio.com/blog/post/fff-366 |
| C07 | Riot, Profiling: Real World Performance in League | 2018-08-07 | EXPERIENCE | https://www.riotgames.com/en/news/profiling-real-world-performance-league |
| C08 | Epic Lore code review standards | undated, accessed 2026-10-21 | VERIFIED | https://epicgames.github.io/lore/developing/code-standards/code-review/ |
| C09 | Epic Lore error handling standards | undated, accessed 2026-10-21 | VERIFIED | https://epicgames.github.io/lore/developing/code-standards/errors/ |
| L01 = T04 | Luau release 0.743 | 2026-10-16 | VERIFIED | https://github.com/luau-lang/luau/releases/tag/0.743 |
| L02 | Luau new type solver general release | 2025-11-20 | VERIFIED | https://devforum.roblox.com/t/general-release-luau%E2%80%99s-new-type-solver/4084991/1 |
| L03 | Workspace.UseNewLuauTypeSolver | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/reference/engine/classes/Workspace#UseNewLuauTypeSolver |
| L04 | Luau release 0.711 | 2026-03-06 | VERIFIED | https://github.com/luau-lang/luau/releases/tag/0.711 |
| L05 | Luau syntax by example | accessed 2026-10-21 | VERIFIED | https://luau.org/syntax/ |
| L06 | [Beta] if local statements and expressions | 2026-10-06 | VERIFIED | https://devforum.roblox.com/t/beta-if-local-statements-and-expressions/4918297 |
| L07 | An introduction to Luau types | accessed 2026-10-21 | VERIFIED | https://luau.org/types/ |
| L08 | Primitives and simple types | accessed 2026-10-21 | VERIFIED | https://luau.org/types/basic-types/ |
| L09 | Generics and polymorphism | accessed 2026-10-21 | VERIFIED | https://luau.org/types/generics/ |
| L10 | Type refinements | accessed 2026-10-21 | VERIFIED | https://luau.org/types/type-refinements/ |
| L11 | Securing the client-server boundary | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/scripting/security/client-server-boundary |
| L12 | Luau standard library | accessed 2026-10-21 | VERIFIED | https://luau.org/library/ |
| L13 | How we make Luau fast | accessed 2026-10-21 | VERIFIED | https://luau.org/performance/ |
| L14 | Luau Recap for 2025: Runtime | 2025-12-19 | VERIFIED | https://luau.org/news/2025-12-19-luau-recap-runtime-2025/ |
| L15 | Roblox Strings | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/luau/strings |
| L16 = R11 | Native code generation | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/luau/native-code-gen |
| L17 | Creator Roadmap 2026: Spring Update | 2026-05-08 | VERIFIED | https://devforum.roblox.com/t/creator-roadmap-2026-spring-update/4625473 |
| L18 | Luau Lints | accessed 2026-10-21 | VERIFIED | https://luau.org/lint/ |
| L19 = R06 | Improve performance | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/improve |
| R01 | Performance optimization (60 FPS default target) | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization |
| R03 | Performance analytics (CPU time below 16 ms for 60 FPS) | accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/performance |
| Q00 | The paper's own proposals | 2026-10-21 | OPINION | not external |

---

## 8. Coverage check (brief checks C1, C2)

C1. Every numbered rule and table row in lines 1-449:
- Rules 1-15 (lines 25-53): P107-P121.
- Section 1 claim table, four rows (lines 58-61): P122, P123, P124, P125.
- Section 1 evidence summary, three rows (lines 76-78): P108/P122 (filter by gap), P123/P124 (older mechanisms stay historical), P126/P129 (diagnose rework before more agents). Prose at lines 63, 67, 69, 71: P126-P129.
- Section 2 evidence table, four rows (lines 85-88): P131, P132, P133, P134. Evidence-gap and definition paragraphs (90-94): P135-P137. Checklist (98-140): P138-P156.
- Section 2 summary, four rows (lines 145-148): P131 (39/40), P130 (medium guidance), P136 (first-try separate), P138 (checklist proportional).
- Section 3 summary, three rows (lines 293-295): P171 (maps to P111, P113, P159, P160, P167, P168). All prose and examples: P157-P170.
- Section 4 closing rows, seven (lines 442-448): P197. Prose: P172-P196.
- Dropped: none. Condensed, not dropped: the two near-duplicate parser examples (P165, P180) and the Section 2 first-try checklist (compressed into P139-P156 plus section 5b, all items retained).

C2. Every lesson row has a tag and either a source id or Q00 (rows with no id in the paper say "none cited" and are marked as Q00 assumed). Row P171 and P197 summary rows list mixed tags, each with its source.

Counts: 97 lesson ids (P101-P197; P171 and P197 are summary-row maps, the rest are single lessons), 18 number rows (N1-N18), 28 Luau/engine claims of which 15 are starred, 21 practice claims of which 8 are starred.
