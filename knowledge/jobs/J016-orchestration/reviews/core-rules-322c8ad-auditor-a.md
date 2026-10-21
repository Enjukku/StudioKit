---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit
supersedes: []
---
> Author: auditor-a · claude-opus-5-5 · high · 2026-10-21

# Review: core rules and orchestration playbook @322c8ad, by auditor-a

Spec: `knowledge/jobs/J016-orchestration/design.md`, `design-jobtypes.md`, `design-context.md`, `capability-check.md` (C01-C21 at 322c8ad), `decisions.md` (J016-D1..D5), owner rule J008 (blueprint before building).
Note on inputs: the working tree changed after 322c8ad. `capability-check.md` gained a C22 row (uncommitted). F09 uses role files, which are unchanged since 322c8ad; C22 is cited only as corroboration. Incidental: one grep for "blueprint" in `knowledge/jobs/J008-environment-designer/*.md` printed 2 lines of `grades-hidden.md`. I did not open the file and did not use those lines (see F21).

```text
<spec>
artifact: AGENTS.md, CLAUDE.md, rules/company.md, rules/messages.md, rules/knowledge.md, rules/assistants/claude.md, rules/assistants/codex.md, .agents/skills/orchestration/SKILL.md, .agents/skills/orchestration/references/job-types.md @322c8ad
reviewer: auditor-a
looked_at_first: [the 9 scope files, the 5 design/decision files, templates/jobs/*, knowledge/jobs/README.md, .agents/roles/*.md frontmatter, .agents/workflows/jobs/README.md, job-cutscene.js and job-stage.js (args, stages, review chain), tools/hooks/handback_check.py, kit.json]
findings:
  # ---------------- blocking ----------------
  - id: F01
    class: blocking
    check: A3
    where: "rules/company.md:67; rules/company.md:144"
    expected: "company.md:67 'file the job into the game vault' points to rules/knowledge.md §7 (Filing a job into the vault). company.md:144 'lesson draft with its cause and layer' points to §8 (The learning loop)."
    observed: "company.md:67 cites 'rules/knowledge.md §5'. company.md:144 cites 'rules/knowledge.md §5-6'. knowledge.md §5 is 'Notes' (frontmatter) and §6 is 'Where things go' (knowledge.md:60, :80). Filing is §7 (knowledge.md:101); the loop is §8 (knowledge.md:104)."
    evidence: "AGENTS.md:68 cites the correct target (§7). A lead at close that follows company.md:67 opens the frontmatter rules and finds no filing list, so it can skip filing precedents, vocabulary and the taste log. That is the vault-growth step of the approved context design (design-context.md §5)."
    smallest_fix: "company.md:67 → 'rules/knowledge.md §7'; company.md:144 → 'rules/knowledge.md §7-8'."
  - id: F02
    class: blocking
    check: A3, A2
    where: ".agents/skills/orchestration/SKILL.md:14; rules/assistants/claude.md:26"
    expected: "The lead's call shape matches the workflow contract: args {job, stage, size, studioId (build and repair), gate (owner's words), change (repair)} (.agents/workflows/jobs/README.md:10; job-cutscene.js:4)."
    observed: "SKILL.md:14 and claude.md:26 give 'args {job, stage}' only. Every job workflow except job-effect has 'const SIZE = A.size || \"L\"' (job-cutscene.js:29, job-character.js:31, job-feature.js:29, job-marketing-art.js:32, job-stage.js:31, job-ui-screen.js:32). Build and repair without studioId return blocked (job-cutscene.js:40)."
    evidence: "job-cutscene.js:586-590 runs the proof inside build only when SIZE === 'M'. A lead that follows SKILL.md:14 for an M job calls build without size. The workflow then treats the job as L and skips the proof completely. The owner then sees a G3 result that never had an integrated proof (company.md:27 says the M proof runs inside build). The owner's G1 words also do not reach the workflow, because 'gate' is not named."
    smallest_fix: "SKILL.md:14 and claude.md:26: 'args {job, stage, size, gate (owner's words verbatim), studioId for build/repair, change for repair}; see .agents/workflows/jobs/README.md'."
  - id: F03
    class: blocking
    check: A2, A7
    where: "rules/company.md:60-61 vs .agents/skills/orchestration/references/job-types.md:15 (cutscene)"
    expected: "One placement of the interface rounds for a cutscene, the same in the flow rule, the recipe and the workflow. The workflow does both: a needs round before the animatic (job-cutscene.js:241-279, 'Proof stage, interface round') and a craft-planning round after G2 (meta phase 'Craft planning')."
    observed: "company.md:60-61 puts 'Interfaces' (step 4) before 'Proof' (step 5) for every M and L job and names no post-G2 planning. job-types.md:15 has only 'Interfaces after G2' and no pre-proof needs round. Character (job-types.md:30) splits correctly: S1-S2 before the proof, S3-S6 after G2."
    evidence: "The pilot is a cutscene. A hand-run lead (Codex per codex.md:17, or Claude without the workflow) that follows job-types §1 makes the animatic with no needs from the animator, environment, VFX, sound and architect. That is the cooperation the owner asked for ('sound needs the VFX timing'). A lead that follows company §4 skips the post-G2 crafts planning, which the recipe calls 'before costly work' (design-jobtypes.md:41)."
    smallest_fix: "company.md:60: 'Interfaces, where the recipe places them (a needs round on the contract draft before the proof; full craft planning after G2 where the recipe says so)'. job-types.md §1: add a row 'Interfaces before the proof: animator, environment-designer, vfx-designer, sound-designer, architect state needs against beat sheet rev N; film-director merges; ≤ 2 rounds'."
  - id: F04
    class: blocking
    check: A2
    where: "rules/company.md:61; .agents/skills/orchestration/SKILL.md:52 vs job-types.md:31, :47, :61, :74"
    expected: "One rule for who reviews the proof before G2. The recipe's own order wins, as it does for the review chain ('in the recipe's order', company.md:95)."
    observed: "company.md:61 and SKILL.md:52 fix 'domain lead → art-director → architect' for every proof. The recipes name other reviewers: character art-director → animator → game-designer (job-types.md:31); stage game-designer → art-director → performance-engineer (:47); UI game-designer → art-director → feature-builder (:61); feature: the game-designer plays it (:74). SKILL.md:52 also cites company.md §7 for this order, but §7 (company.md:94-104) is the frozen-candidate review chain, not the proof."
    evidence: "company.md:5 says 'When this file and a brief disagree, this file wins'. A lead that follows company.md:61 on a stage proof adds an architect review and can drop the performance-engineer budget check (job-types.md:47). On a character proof it puts the art-director twice and drops the animator's 'usable' check. design.md:84 (generic) and design-jobtypes.md (per type) have the same split. The rules do not say which one wins."
    smallest_fix: "company.md:61 and SKILL.md:52: 'the recipe's proof reviewers, in its order (default when the recipe names none: domain lead → art-director → architect)'. Point SKILL.md:52 to company §4 step 5, not §7."
  - id: F05
    class: blocking
    check: A4
    where: ".agents/skills/orchestration/SKILL.md:16, :56, :59; rules/company.md:76; rules/assistants/claude.md:25; templates/jobs/crew.md"
    expected: "Rules for peer ids and resume-by-id apply only where the lead can know the ids: Agent-tool subagents it spawns itself (C01-C03 probed only these). Workflow-run stages use files and fresh repair calls, and the rules say so."
    observed: "SKILL.md:16 says 'update crew.md' between stages, SKILL.md:56 'Give each brief the peers ids it needs from crew.md', SKILL.md:59 'Repairs go back to the maker (resume it by id)'. company.md:76 and claude.md:25 say ids come from crew.md. No job workflow writes or reads crew.md or agent ids (grep 'crew|agentId|resume' in .agents/workflows/jobs/*.js finds nothing relevant). Workflow repairs are fresh call()s with the finding files (job-cutscene.js:536). Agents started in one parallel() cannot hold each other's ids, because the ids do not exist when the briefs are written."
    evidence: "On the pilot path (saved workflow), a lead that follows SKILL.md:16 has no ids to record. A craft that follows company.md:76 or templates/role.md:25 looks for a peer id in crew.md, finds an empty table and stalls or guesses. messages.md:69 shows 'peers: {vfx-designer: a1b2c3d4}' as a normal brief field. capability-check.md says nothing on whether workflow agent() exposes ids (question Q3)."
    smallest_fix: "SKILL.md §6 and company.md:76: 'In a saved-workflow stage, sideways work goes through exchange/ files and repairs are fresh calls with the finding files. crew.md and peers apply to agents the lead or job lead spawns by hand.' crew.md template: the same line."
  - id: F06
    class: blocking
    check: A2, A5
    where: "rules/company.md:19, :92, :124; rules/messages.md:40; AGENTS.md:22; .agents/skills/orchestration/SKILL.md:56"
    expected: "One answer to who spawns crafts in a hand-run stage, consistent with 'spawn depth at most two below the lead's chat'."
    observed: "company.md:19: 'The lead hands a job to its job lead; the job lead reports to the lead.' messages.md:40 has the brief path 'job lead → craft'. SKILL.md:56 (lead's playbook) has the lead brief crafts with peer ids. AGENTS.md:22 tells every agent to send the explore scout or the researcher when the docs do not fit."
    evidence: "Reading A: the lead spawns each craft (depth 1), and scouts are at depth 2. Reading B: the lead spawns the job lead as a subagent (depth 1), the job lead spawns crafts (depth 2), and a craft that follows AGENTS.md:22 spawns a scout at depth 3. The platform allows that (C04), but it breaks company.md:92 and :124 ('at most two below the lead's chat'). Two careful leads will build different trees. In reading B, crew.md (kept by the lead, company.md:76) also does not get the ids."
    smallest_fix: "company.md §6: 'In a hand-run stage the lead (or the workflow) spawns every craft. A job lead spawns crafts only as the main chat of a production chat. A subagent job lead briefs crafts through direction.md and the contract.'"
  - id: F07
    class: blocking
    check: A3
    where: "rules/assistants/codex.md:18; AGENTS.md:45"
    expected: "The gate command exists in the kit. The kit gate is 'python tools/verify.py' (claude.md:34, knowledge.md:114)."
    observed: "codex.md:18: 'Gate first (powershell -File tools/verify.ps1)', with no fallback. AGENTS.md:45: 'powershell -File tools/verify.ps1 or the game's equivalent'. tools/verify.ps1 does not exist, and git log --all -- tools/verify.ps1 is empty."
    evidence: "A Codex lead or worker that follows codex.md:18 runs a missing script. It cannot get 'RESULT: PASS', so it reports blocked or claims done without the gate. AGENTS.md (always loaded) names a file that does not exist as the default."
    smallest_fix: "codex.md:18 and AGENTS.md:45: 'python tools/verify.py (or the game's equivalent named in game-profile.md)'."
  - id: F08
    class: blocking
    check: A4
    where: "rules/company.md:76; rules/messages.md:131; rules/assistants/claude.md:25; templates/jobs/crew.md (role tools at 322c8ad)"
    expected: "Every role that the rules tell to send direct messages can call SendMessage."
    observed: "14 of 24 role files have a 'tools:' allowlist without SendMessage: analyst, art-director, doc-keeper, explore, game-designer, live-ops-designer, marketing, progression-designer, researcher, reviewer, sound-designer, studio-operator, trend-scout, vfx-designer (.agents/roles/*.md frontmatter). company.md:76: 'Sideways is allowed and expected ... direct SendMessage by agent id'. messages.md §5: the contract owner 'messages each consumer'."
    evidence: "vfx-designer (effect job lead), sound-designer, art-director (character job lead), game-designer (feature job lead) and marketing (marketing-art job lead) cannot send. On a by-hand stage, the effect job lead that follows messages.md §5 cannot send a contract-change notice. The working-tree C22 row (uncommitted) confirms this in a rehearsal. The fix is the owner's decision (an agent-permission change)."
    smallest_fix: "Until the owner decides: company.md:76 and messages.md:131 add 'only roles whose tools list SendMessage can send; others use exchange/ notes and the lead relays the id-level notice'. Owner digest item: add SendMessage to those 14 allowlists."
  # ---------------- recommendations ----------------
  - id: F09
    class: recommendation
    check: A2, A5
    where: "AGENTS.md:46; rules/company.md:16, :64, :131; rules/owner-profile.md:21; job-types.md:18, :34, :88"
    expected: "One Studio rule: either one driver (reads and writes) or one writer (reads in parallel allowed). Also say who holds the lease in production, and where the lease is recorded."
    observed: "AGENTS.md:46 says 'one driver per Studio instance', company.md:131 says 'Studio writers 1 per Studio instance', and owner-profile.md:21 says 'Studio work is sequential'. company.md:16 says one integrator per job holds 'the Studio writer lease'. But the recipes name two Studio users: cutscene film-director + feature-builder (job-types.md:18), character animator + feature-builder (:34), effect feature-builder or quick-builder + studio-operator (:88). No file records the current lease holder."
    evidence: "Reading 1 (company): a studio-operator capture while the environment-designer builds is allowed. Reading 2 (AGENTS, owner-profile): it is not. In hand-run production with up to 5 parallel agents (company.md:129), nothing serializes Studio. The workflows serialize it in code (job-cutscene.js:509-510), but company.md does not give a rule for hand-run stages."
    smallest_fix: "company.md:131: 'Studio drivers (read or write): 1 at a time per instance (owner-profile). The lead names the lease holder per stage in crew.md'. company.md:16: 'integrator (one per job; a recipe may name a second builder that takes the lease in turn)'."
  - id: F10
    class: recommendation
    check: A5
    where: "rules/company.md:26-28"
    expected: "A sizing test that gives one answer when an output is inside the approved style but needs several crafts."
    observed: "M: 'one specialist output inside an approved style (an asset, an effect, a screen, a system)'. L: 'several crafts or a new look (... feature with UI + VFX + sound)'."
    evidence: "An effect inside the approved style needs vfx + sound + game-designer (job-types.md:84) and so matches both rows. Lead 1 sizes it M (G1+G3, as job-effect.js:33 does). Lead 2 sizes it L (adds G2). The owner's gate count then depends on the reader."
    smallest_fix: "company.md:28 L: 'a new look, or several crafts that produce separate outputs (cutscene, character, stage, feature with UI + VFX + sound); one output with supporting crafts inside an approved style is M'."
  - id: F11
    class: recommendation
    check: A5
    where: "rules/company.md:95; SKILL.md:64 vs job-types.md:19, :51, :64, :77"
    expected: "The recipe review lines show which checks run in parallel with the creative order."
    observed: "company.md:95 and SKILL.md:64 run technical/QA in parallel with the creative order. The recipes chain them with arrows: cutscene 'qa-lead ∥ performance-engineer → film-director' (:19); UI 'qa-lead → ui-ux-designer' (:64); stage puts qa-lead last after the creative reviews (:51)."
    evidence: "The workflow runs them side by side (job-cutscene.js:509-514). A hand-run or Codex lead that reads the arrows runs QA first (cutscene, UI) or last (stage). The result is the same but the order differs, and the stage order contradicts company §7."
    smallest_fix: "job-types.md:5: 'Technical checks (qa-lead, performance-engineer, reviewer) run beside the creative order; arrows order only the creative reviews'."
  - id: F12
    class: recommendation
    check: A2
    where: "rules/company.md:103, :115; SKILL.md:111; .agents/workflows/jobs/README.md:18"
    expected: "One status for 'the repair round limit is reached'."
    observed: "company.md:103 and SKILL.md:111 say 'then diagnose the brief, tool, standard or approach'. company.md:115 says 'failed: gave up after the round limit → one level up'. The workflows return needs-decision (job-cutscene.js:522; README:18), and company.md:113 defines needs-decision as 'a choice only the owner can make'."
    evidence: "In a hand-run stage, one lead marks the item failed and diagnoses it itself. Another lead puts it in the owner's digest. The second lead spends the owner's attention on a tool or brief fault."
    smallest_fix: "company.md §7 Stop: 'after the limit the stage returns failed with the diagnosis; only a diagnosis that needs scope, taste or budget becomes needs-decision'. Align the workflow README."
  - id: F13
    class: recommendation
    check: A5
    where: "AGENTS.md:67; rules/company.md:144; rules/knowledge.md:105; SKILL.md:82; templates/role.md:43"
    expected: "One moment when each agent writes its lesson draft."
    observed: "templates/role.md:43 says at every hand-back. AGENTS.md:67 and knowledge.md:105 say 'a job ends or a gate is answered'. company.md:144 and SKILL.md:82 say 'at close ... every agent'."
    evidence: "At close, workflow agents and most subagents are finished. A lead that follows SKILL.md:82 must resume every agent by id (impossible for workflow agents, F05) or write the drafts itself. A craft that follows AGENTS.md:67 waits for a gate it never hears about."
    smallest_fix: "knowledge.md §8.1 and company.md §12: 'each agent writes its draft with its hand-back (templates/role.md); at a gate answer or close the lead adds the owner's words and drafts its own'."
  - id: F14
    class: recommendation
    check: A2
    where: "AGENTS.md:28 vs rules/company.md:27, :35"
    expected: "The same M job folder contents in both files."
    observed: "AGENTS.md:28 gives M and L jobs the job card, direction sheet, contract, crew list, exchange notes, reviews, evidence ledger and decision log. company.md:27 gives M only 'card, direction sheet, contract if crafts share one, evidence ledger'. company.md:35 records every gate answer 'in the job's decision log'."
    evidence: "A lead that follows company.md:27 creates no decisions.md or crew.md for an M job. Then it has nowhere to record G1 (company.md:35, SKILL.md:71) and no ids to brief with."
    smallest_fix: "company.md:27 M paperwork: 'job folder: card, decisions.md, crew.md, direction sheet, contract if crafts share one, evidence ledger'."
  - id: F15
    class: recommendation
    check: A2
    where: "AGENTS.md:33 vs AGENTS.md:34"
    expected: "STATUS is the first line (messages.md:92; tools/hooks/handback_check.py:43 checks the first non-empty line)."
    observed: "AGENTS.md:33: 'every hand-back starts with its status'. AGENTS.md:34: 'Every hand-back ends with a status'. kit.json codex_preamble, which is copied into all 24 .codex/agents/*.toml files, says 'End every hand-back with the status block from rules/company.md §4-5'. The status table is in §8."
    evidence: "An agent that follows line 34 or the Codex preamble puts STATUS last. The SubagentStop hook sends that hand-back back once, and Codex workers look up the status in the wrong section."
    smallest_fix: "AGENTS.md:34: 'Every hand-back's STATUS line names done, blocked, needs-decision or failed, with the reason'. kit.json preamble: 'Start every hand-back with STATUS (rules/messages.md §3)'; then run sync_harness."
  - id: F16
    class: recommendation
    check: A2
    where: "rules/company.md:30 vs job-types.md:97"
    expected: "G1 option count is the same in the gate rule and the recipe, or the rule allows the recipe to change it."
    observed: "company.md:30: 'the owner picks from 2-3 options'. Marketing G1 (job-types.md:97): '3-5 rough thumbnails'."
    evidence: "In the readiness check (SKILL.md:66), the lead finds that 3-5 options break company §2 and cuts them to 3, or it lets the recipe win silently."
    smallest_fix: "company.md:30: '2-3 options (a recipe may set another count, e.g. marketing art 3-5 thumbnails)'."
  - id: F17
    class: recommendation
    check: A1
    where: "design.md:49-64 (column 'Must consult') vs rules/company.md:39-50"
    expected: "The authority map keeps 'Must consult' per decision, or the omission is explained."
    observed: "company.md §3 has only 'Owner of the decision' and 'Escalates'. company.md:14 says 'others are consulted' but does not name them. Examples that are lost: film-director must consult the art-director, animator, VFX and sound (design.md:55); the art-director must consult the game-designer and film-director (:54); the environment-designer must consult the game-designer on routes (:63)."
    evidence: "A decision owner that follows company §3 alone decides the beat list without the animator or sound. The recipes partly cover this through exchange rounds, but only inside a job."
    smallest_fix: "Add the 'Must consult' column from design.md:49-64 to company.md §3."
  - id: F18
    class: recommendation
    check: A1
    where: "design-jobtypes.md:131-143 vs job-types.md (no cross-type section)"
    expected: "The approved cross-type rules are in the recipe reference or in company.md."
    observed: "Missing from every scope file: 'take a note for its problem, not its suggested fix' (only in job-stage.js:288); 'reuse shared libraries before making new' (design-context.md E19; knowledge.md §7 files the catalogs but no rule says to search them first); 'a craft may diverge from a reference for readability or budget and says so up front'; 'consensus is not the goal; judge against the target'; 'one written target experience shared before craft work'."
    evidence: "J016-D4 approved design-jobtypes.md as a whole. A craft that follows the core rules makes a new asset when a cataloged one exists, and applies a reviewer's suggested fix literally."
    smallest_fix: "Add a 'Cross-type rules' table to job-types.md (the 9 rows of design-jobtypes.md:134-142, without the evidence column)."
  - id: F19
    class: recommendation
    check: A1
    where: "design.md:187-190 (§10 workflow books) vs scope files; templates/role.md:16-45"
    expected: "The 10-item workflow-book standard (mission and great work, inputs and stop conditions, reference images first, numbered steps with collaboration points, docs rows with date checked, file conventions, self-review with positive and failure examples, evidence and hand-off, tool limits and escalation, lessons into steps) is written where /build-agent and /improve can check a book against it."
    observed: "No scope file or template lists it. AGENTS.md:22 (docs rows) and :48 (reference image first, multi-angle self-review) cover parts of it universally. templates/role.md has no docs-rows, stop-condition or tool-limit section. 'workflow book' appears only in company.md:95."
    evidence: "Owner goal 5 ('Every agent follows its workflow book ...'). Without a written standard, a new role from /build-agent can lack items 2, 5, 9 and 10 and still pass."
    smallest_fix: "Add the 10 items as a checklist to company.md §10 or templates/role.md, with a pointer from the build-agent skill."
  - id: F20
    class: recommendation
    check: A1, A3
    where: "rules/company.md:12, :72; rules/knowledge.md:15; knowledge/jobs/README.md:7-19"
    expected: "The dependency map (one of the four maps, design.md:41) has a file name and a template."
    observed: "company.md:12 (job lead owns 'the dependency map'), company.md:72 and knowledge.md:15 name it. templates/jobs/ has no dependency-map template, and jobs README has no row for it."
    evidence: "Selective recheck (company.md:104: 'only the failed layer and what depends on it') needs this map. Two job leads write it in different places, or not at all, and fall back to rechecking everything."
    smallest_fix: "Name it: the 'Consumers' row of each contract-header.md is the dependency map, or add templates/jobs/dependency-map.md and a README row."
  - id: F21
    class: recommendation
    check: A4
    where: "rules/knowledge.md:51; AGENTS.md:22"
    expected: "Withheld-context patterns cover every held-out key file. The scout that AGENTS.md:22 names gets the kit rules."
    observed: "knowledge.md:51 withholds 'hidden-*'. knowledge/jobs/J008-environment-designer/grades-hidden.md exists, and its name escapes the pattern (an rg over job folders printed its lines in this audit). AGENTS.md:22 says 'the explore scout', but Claude Code also has a built-in 'Explore', which skips AGENTS.md (C21) and so never sees the hidden-* rule."
    evidence: "A grep-based scout or the packet can show grading keys to an agent that is under evaluation. An agent that picks the built-in Explore has no withheld-context rules."
    smallest_fix: "knowledge.md:51: '`hidden-*` and `*-hidden.*`' (or rename the file). AGENTS.md:22: 'the kit's `explore` role (not the built-in Explore, which skips this file)'."
  - id: F22
    class: recommendation
    check: A1 (fixed rule J008)
    where: "job-types.md:46"
    expected: "Owner rule J008: the blueprint is approved before any building."
    observed: "'route graph + blueprint approved at G1 ..., refined in the proof stage'. The greybox is then built in the proof stage, and for M jobs inside build (job-types.md:5). company.md:34 says a departing revision 'is shown to the owner', but it does not say when."
    evidence: "A refinement that moves a route, footprint or landmark is built before the owner sees it. job-stage.js surfaces 'approved_items_changed' (line 113), but the core rule does not say that such changes stop the build."
    smallest_fix: "job-types.md:46: 'a refinement that changes an approved item (route, footprint, landmark, heights) goes to the owner before the greybox is built; other refinements are listed at G2/G3'."
  - id: F23
    class: recommendation
    check: A7
    where: "rules/assistants/codex.md:13, :17; job-types.md:5"
    expected: "A Codex lead can run each stage by hand from codex.md + job-types.md (+ SKILL.md)."
    observed: "These are missing or only in the .js files: (a) which recipe rows belong to which stage call (direction / proof / build / repair); (b) the cutscene needs round before the proof (F03); (c) 'recapture and refreeze after every repair round' (workflows README:11 only); (d) what the repair stage does beyond one line (SKILL.md:17); (e) M size: run the proof inside build (job-types.md:5 says it, but codex.md does not link to it); (f) no hooks on Codex, so the lead must check hand-back shape and give the job pointer itself (not stated); (g) codex.md:13 'Use the live tool limit' versus company.md:129 'max 5' per stage; (h) the gate path is broken (F07); (i) kit.json preamble (F15)."
    evidence: "codex.md:17: 'in Codex run the same stages by hand from the orchestration skill's references/job-types.md'. job-types.md lists the ingredients but not the stage sequence. A Codex lead can rebuild most of the flow from SKILL.md §3-§9. It misses (b), (c) and (d), and so drifts from the Claude Code flow, which makes the pilot comparison unequal."
    smallest_fix: "job-types.md: add a 'Stage' column (direction / proof / build / repair) to each recipe row, plus a 4-line 'Repair stage' paragraph and the refreeze rule. codex.md:13: 'parallel workers per stage max 5 (rules/company.md §9), within the live tool limit'. codex.md: one row 'Hooks: none; the lead checks STATUS/coverage and puts the job id in every brief'."
  - id: F24
    class: recommendation
    check: A4
    where: "rules/assistants/claude.md:44 vs rules/knowledge.md:114"
    expected: "Instructions given to agents name only actions an agent can take."
    observed: "claude.md:44 says 'Run /doctor prompt-audit weekly'. knowledge.md:114 says '/doctor (run by the owner)'. Built-in CLI commands are not skills that agents can call. capability-check.md does not mention 'prompt-audit'."
    evidence: "/improve (an agent) reads claude.md:44 and tries to run it, or reports it as done without running it."
    smallest_fix: "claude.md:44: 'The owner runs /doctor weekly; /improve asks for it in its tips'."
  - id: F25
    class: recommendation
    check: A3
    where: "rules/knowledge.md:29"
    expected: "Mechanism paths exist or are generated."
    observed: "'Path rules | .claude/rules/*.md with paths: load when matching files are touched'. .claude/rules/ does not exist at 322c8ad, and tools/sync_harness.py does not generate it."
    evidence: "An agent that looks for area rules there finds nothing. This is harmless today, but design-context.md:95 calls it 'exists'."
    smallest_fix: "Mark the row 'none yet; canonical source would be ... synced by sync_harness.py', or remove it."
  # ---------------- new requests ----------------
  - id: F26
    class: new request
    check: A2 (owner goal 6)
    where: "kit.json models.codex"
    expected: "Owner goal: 'cheaper models for mechanical work'."
    observed: "All four Codex tiers are 'gpt-6.1-sol', marked PROPOSAL in kit.json 'notes'."
    evidence: "A Codex run of the pilot puts mechanical work on the lead model. This is outside the scope files, so it is logged, not fixed in J016."
    smallest_fix: "Owner digest: pick Codex research and mechanical models before a Codex pilot arm."
questions:
  - {q: "claude.md:27 says 'A message to an idle chat resends its full context, so batch updates'. No capability-check row supports it (C13 covers text-only). Source?"}
  - {q: "Does `/doctor prompt-audit` exist on 2.1.306 (claude.md:44)? It is not in capability-check.md."}
  - {q: "Does a saved workflow's agent() expose an agent id that SendMessage can use? C01-C03 probed Agent-tool subagents only. The answer decides how F05 is fixed."}
  - {q: "company.md:130 'Concurrent L jobs: 2' is not in design.md §8. Is it an owner setting carried over from the old kit?"}
keep:
  - "company.md §2: the gate table, approval bound to a revision (:34), 'agent approvals never count' (:35), loosening only by the owner (:36)"
  - "company.md §3 table and its three rules (:52-54); §5 files-first, tickets for new work only, contract change names consumers, wake only when work changes (:74-79)"
  - "company.md §7 review rules (reviewers read, three classes, protected list, independent look first, light checks, selective recheck); §9 limits table"
  - "messages.md: the §2 brief example with inputs@rev, protected, consumers, peers; §3 coverage + built_on; §4 exchange note; §5 contract-change notice; §6 finding format; §7 trust; §9 reviewer checks"
  - "knowledge.md §1 five layers with one writer each; §3 load order and the withheld-context table; §4 'no chain of summaries'; §7 filing list; §8 cause classes and the promotion rule"
  - "SKILL.md §1 step 5 'never start the next stage before the gate answer'; §4 independent D1 without others' proposals; §8 gate packet; §9 close-out list; §10 brief rules; §14 self-check"
  - "job-types.md: stage blueprint draft at G1 (J008) (:45); variant mode (:37); stage decision rights (:43); VFX ↔ sound envelope co-design (:15, :86)"
  - "claude.md mechanisms table: peers by id only, no roster, workflows cannot pause, agent teams off, settings are the owner's"
verdict: fix-first
</spec>
```

## Coverage per check

| Check | Status | Result | Findings |
| --- | --- | --- | --- |
| A1 design elements | checked: design.md §0-12, design-jobtypes.md (7 types + cross-type), design-context.md §0-8 against the scope files | Flow, gates, reviews, sideways rules, limits, models, layers, load order, routing, withheld context, passing, filing and learning loop are all present and correct. Missing: the must-consult column, the cross-type rules, the workflow-book standard and a dependency-map file. J008 is kept at G1 but weakened after G1. | F17, F18, F19, F20, F22 |
| A2 contradictions | checked: sizes, gates per size, round limits, review order, statuses, decision rights, Studio writer, parallel limits, model tiers | Model tiers, spawn depth numbers, direction and interface round limits and the decision owners agree in every file. Conflicts: interface placement, proof reviewers, M folder contents, round-limit status, STATUS position, G1 option count, Studio driver vs writer. | F03, F04, F09, F12, F14, F15, F16 |
| A3 cross-references | checked: every § reference (40 found by grep) and every named path, template, role, skill and workflow, with ls/Glob | 2 wrong § targets, 1 missing gate script, 1 missing folder. All 7 workflows, 13 job templates, rig sheet, hooks, tools, roles (except the planned animator, which has stand-in rules) and skills exist. | F01, F02, F07, F25 |
| A4 Claude Code 2.1.306 | checked against C01-C21 (and role-file tools) | By-id messaging, no roster, nesting ≤ 3, workflows cannot pause, compaction 5k, hooks by the owner: all stated correctly. Not possible as written: crew ids or resume in workflow stages; SendMessage for 14 allowlisted roles; an agent running /doctor. | F05, F08, F21, F24 |
| A5 ambiguity | checked | Two readings each: who spawns crafts (depth), M vs L sizing, QA parallel vs ordered, lesson draft timing, Studio driver vs writer. | F06, F09, F10, F11, F13 |
| A6 always-loaded size | checked: wc -l, wc -c | PASS. CLAUDE.md 9 + AGENTS.md 76 + claude.md 55 = 140 lines (< 200). orchestration SKILL.md is 13,608 chars (about 3,400-3,900 tokens), so the whole file, steps and rules included, is inside the first 5,000 tokens. Description is 278 chars (≤ 400). No blocking problem. | — |
| A7 Codex by hand | checked: codex.md + job-types.md (+ SKILL.md, workflows README) | Partly. The flow can be rebuilt from SKILL.md §3-9. Missing: stage partition per recipe, the cutscene needs round, refreeze after repair, repair stage, hooks note, parallel cap; the gate path is broken. | F07, F15, F23 |

Areas with no blocking problem: `rules/messages.md` (formats complete and consistent with the hook and templates), `rules/knowledge.md` routing and learning (except the §-reference targets in company.md and the hidden-file pattern), A6 sizes, model tiers.
