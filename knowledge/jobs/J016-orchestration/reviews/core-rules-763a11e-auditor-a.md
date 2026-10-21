---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit recheck (selective, rules/company.md §7)
supersedes: []
---
> Author: auditor-a · claude-opus-5-5 · high · 2026-10-21

# Recheck: core rules and orchestration playbook @763a11e, by auditor-a

Scope of this recheck: blocking findings F01-F08 of `reviews/core-rules-322c8ad-auditor-a.md`, the keep list, and new contradictions inside the 9 scope files. I did not re-review the recommendations, except where a fix touched one (N02). I opened the files before the commit message.

```text
<spec>
artifact: AGENTS.md, CLAUDE.md, rules/company.md, rules/messages.md, rules/knowledge.md, rules/assistants/claude.md, rules/assistants/codex.md, .agents/skills/orchestration/SKILL.md, .agents/skills/orchestration/references/job-types.md @763a11e
reviewer: auditor-a
looked_at_first: [the 9 scope files at 763a11e; git diff 322c8ad..763a11e on them; .agents/workflows/jobs/*.js size handling; templates/jobs/crew.md; templates/role.md; tools/context_packet.py --role; capability-check.md C22 row]
prior_findings:
  - {id: F01, state: closed, evidence: "company.md:67 → 'rules/knowledge.md §7'; company.md:150 → '§7-8'. Both targets match knowledge.md §7 (filing) and §8 (learning loop)."}
  - {id: F02, state: closed, evidence: "SKILL.md:14 points to the args table in .agents/workflows/jobs/README.md, names gate and studioId, and says size and the rule-switching flags 'have no silent default'. claude.md:26 lists job, stage, size, gate, studioId, change and the type's flags. All 7 workflows now have 'const SIZE = A.size' (job-cutscene.js:31). job-cutscene.js:48 refuses a missing size, and :52 refuses stage proof for size M."}
  - {id: F03, state: closed, evidence: "company.md:60: 'Interfaces, where the recipe places them (a needs round ... before the proof; full craft planning after G2 ...)'. job-types.md:26 adds 'Interfaces before the proof'. The stage map job-types.md:10-11 places both rounds. SKILL.md:53 matches."}
  - {id: F04, state: closed, evidence: "company.md:61: 'the recipe's proof reviewers, in its order ... (when the recipe names none: domain lead → art-director → architect)'. SKILL.md:54 says the same and now cites company §4 step 5."}
  - {id: F05, state: closed, evidence: "company.md:78 limits crew.md, peers and resume-by-id to hand-spawned agents. company.md:79 says a saved workflow has no ids, uses files in a fixed order and repairs with fresh calls. The same appears at SKILL.md:16, :41, :58, :61, messages.md:69 (peers comment), claude.md:26 and templates/jobs/crew.md Rules. messages.md §9 flags peers inside a parallel workflow step."}
  - {id: F06, state: closed, evidence: "company.md:95: 'In a hand-run stage the lead's chat spawns every craft (depth 1; scouts at depth 2)'. A subagent job lead drafts briefs for the lead to send, spawns crafts only as a production chat's main chat, and workflow agents spawn no scouts. messages.md:40 and SKILL.md:58 match. AGENTS.md:22 adds 'or inside a saved workflow: grep the mirror yourself', which is consistent with company.md:95."}
  - {id: F07, state: closed, evidence: "AGENTS.md:45: 'python tools/verify.py, or the game's own gate if it has one'. codex.md:19: 'python tools/verify.py'. No scope file names verify.ps1 now."}
  - {id: F08, state: "open (owner decision pending); the interim text is consistent", evidence: "C22 is committed in capability-check.md. Every scope file says the same thing: only a role whose tools: list names SendMessage, or has no tools: list, can send. Others write exchange notes, the lead relays the contract-change notice, and receiving or resume needs no tool (company.md:77; messages.md:135, :139; SKILL.md:58, :60; claude.md:25; AGENTS.md:31; crew.md template Rules line 3; templates/role.md Sideways line). I found no scope line that still tells a non-sending role to send."}
findings:
  - id: N01
    class: blocking
    where: ".agents/skills/orchestration/SKILL.md:111 vs rules/company.md:107, :117; SKILL.md:67, :113"
    expected: "One routing for needs-decision. company.md:117: 'job lead → lead; the lead decides what is its own (§3) and puts only scope, taste or budget in the owner digest'. SKILL.md:67 and :113 say the same for the repair limit."
    observed: "SKILL.md:111 (§12 Statuses) still says: '`needs-decision`: into the owner digest with a recommendation and a default.' It has no exception. The fix widened needs-decision to include 'the repair round limit reached' (company.md:117), so this old line now covers that case too."
    evidence: "A lead that reads §12 as its status table sends every repair-limit return (a brief, tool or approach fault) to the owner. That contradicts the other two lines in the same section and company.md:107. Two careful leads will route the same status differently."
    smallest_fix: "SKILL.md:111: '`needs-decision`: decide what is yours (§7.3, rules/company.md §3); scope, taste or budget go into the owner digest with a recommendation and a default.'"
  - id: N02
    class: recommendation
    where: ".agents/skills/orchestration/SKILL.md:62 vs rules/company.md:64, :135; AGENTS.md:46"
    expected: "The same Studio term everywhere. The fix set it to 'one Studio driver (read or write) at a time' (company.md:64, :135; AGENTS.md:46)."
    observed: "SKILL.md:62 still says 'One Studio writer at a time'."
    evidence: "Before the fix, company.md also said 'writer', so the files agreed. Now the lead's playbook allows a parallel read-only capture, but company §9 forbids it (old F09 reading 1 vs reading 2, now split across files)."
    smallest_fix: "SKILL.md:62: 'One Studio driver (read or write) at a time (rules/company.md §9); name the driver and its studio_id in every Studio brief.'"
  - id: N03
    class: recommendation
    where: "AGENTS.md:21 vs rules/knowledge.md:38; tools/context_packet.py:133"
    expected: "One rule for the lead's packet call."
    observed: "AGENTS.md:21: 'the lead has no role file, so it drops --role'. knowledge.md:38: '--role orchestrator is the lead'. The tool supports the alias (context_packet.py:133 ROLE_ALIASES = {'orchestrator': ['orchestration']})."
    evidence: "A lead that follows AGENTS.md (always loaded) runs without --role. It then loses the boost the fix added for its own book (orchestration skill) and the lower rank for other roles' files."
    smallest_fix: "AGENTS.md:21: '... --role <your role> (the lead: --role orchestrator) --job <job-id> ...; add --job once the job folder exists'."
  - id: N04
    class: recommendation
    where: "references/job-types.md:16 vs job-types.md:99, :101 (and :31 'with sound')"
    expected: "Recipe rows ask only for captures the tools can make."
    observed: "New line :16: 'Studio MCP captures stills, not video or sound: sync is judged from the Output log ... listening is an owner-confirmed line in the gate packet'. Unchanged effect rows: Proof 'one capture with temporary sound at the game camera' (:99) and Review 'sound sync on the capture' (:101)."
    evidence: "A hand-run (or Codex) effect job that follows :99 asks the studio-operator for a sound capture. :16 says the tools cannot make one, so the proof check ends 'not verified' or blocked."
    smallest_fix: "job-types.md:99: 'stills at the game camera in a busy scene + the Output-log timing of event, VFX and cue starts; listening owner-confirmed'. :101: 'sound sync on the Output log'."
keep_check:
  - {item: "company.md §2 gate table; approval bound to a revision; agent approvals never count; loosening by the owner", state: "kept (company.md:24-36)"}
  - {item: "company.md §3 table and its three rules", state: "kept and improved: Must consult column added (company.md:39-54)"}
  - {item: "company.md §5 files-first, tickets for new work only, contract change names consumers, wake only when work changes", state: "kept (company.md:74-82)"}
  - {item: "company.md §7 review rules; §9 limits table", state: "kept (company.md:98-108, :125-138). §7 adds the code-reviewer rule (:100); §9 changes Studio writers to drivers (:135)"}
  - {item: "messages.md §2 brief example (inputs@rev, protected, consumers, peers), §3 coverage + built_on, §4 exchange note, §5 notice, §6 finding format, §7 trust, §9 checks", state: "kept; §3 adds docs_read and lesson; §7 unchanged"}
  - {item: "knowledge.md §1 layers, §3 load order and withheld table, §4 no chain of summaries, §7 filing, §8 causes and promotion rule", state: "kept; the withheld table is wider (names containing 'hidden', '_' folders, eval briefs)"}
  - {item: "SKILL.md §1.5 never start the next stage before the gate answer; §4 independent D1; §8 gate packet; §9 close list; §10 brief rules; §14 self-check", state: "kept (SKILL.md:16, :45, :72, :75-84, :86-92, :120-127)"}
  - {item: "job-types.md blueprint draft at G1 (J008), variant mode, stage decision rights, VFX ↔ sound envelope", state: "kept (job-types.md:57, :49, :55, :27, :98); J008 is stronger at :58"}
  - {item: "claude.md mechanisms: peers by id only, workflows cannot pause, agent teams off, settings are the owner's", state: "kept (claude.md:25-29, :45)"}
  - {item: "A6 always-loaded size", state: "kept: AGENTS.md 76 + CLAUDE.md 9 + claude.md 55 = 140 lines"}
questions:
  - {q: "knowledge.md §3 now withholds any name containing 'hidden' 'from every agent ... Never open'. Which agent then grades held-out keys during /build-agent (for example J008 grades-hidden.md)? This was not checked: the build-agent skill is outside my scope."}
verdict: fix-first (N01 only; F01-F07 closed; F08 waits on the owner, interim text consistent)
</spec>
```

## Coverage

| Item | Status | Evidence |
| --- | --- | --- |
| F01 | closed | company.md:67, :150 |
| F02 | closed | SKILL.md:14; claude.md:26; job-cutscene.js:31, :48, :52 |
| F03 | closed | company.md:60; job-types.md:10-11, :26 |
| F04 | closed | company.md:61; SKILL.md:54 |
| F05 | closed | company.md:78-79; SKILL.md:16, :58, :61; messages.md:69; crew.md template |
| F06 | closed | company.md:95; messages.md:40; AGENTS.md:22 |
| F07 | closed | AGENTS.md:45; codex.md:19 |
| F08 | open, owner decision; interim text consistent across 7 places | company.md:77 and the lines listed above |
| keep list | all 10 items still true; none broken | keep_check |
| new contradictions | 1 blocking (N01), 3 recommendations (N02-N04) | findings |
