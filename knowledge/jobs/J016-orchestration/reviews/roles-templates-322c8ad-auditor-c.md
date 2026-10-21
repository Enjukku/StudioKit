---
type: job   # brief said "review"; not a valid type in rules/knowledge.md §5, so kb_index --lint errors. Lead decides.
scope: universal
status: active
updated: 2026-10-21
source: J016 G3 audit
supersedes: []
---
> Author: auditor-c · claude-opus-5-5 · high · 2026-10-21

# Review: role files and job templates @322c8ad, by auditor-c

Read-only audit. Line numbers are at commit 322c8ad. Line numbers in `job-types.md` are for `.agents/skills/orchestration/references/job-types.md`. Workflow lines (`job-*.js`) are under `.agents/workflows/jobs/` and are cited as evidence only; workflows were not audited.

```text
<spec>
artifact: .agents/roles/*.md (24) + .agents/roles/README.md + templates/role.md + templates/jobs/* (13) @322c8ad
reviewer: auditor-c (general-purpose, opus, high)
looked_at_first: [job-types.md (all 7 recipes), rules/company.md, rules/messages.md, rules/knowledge.md, J016 decisions.md, riot-extracts.md §4, every role file in full, every template in full; then tools/sync_harness.py, tools/kb_index.py, tools/verify.py, kit.json, knowledge/inbox/README.md, knowledge/jobs/README.md, orchestration SKILL.md §2-§3 and the job workflows as cross-evidence. No CHANGELOG or summary read.]
findings:
  # ---------------- blocking ----------------
  - {id: B1, class: blocking, check: C7, where: ".agents/roles/art-director.md:25",
     expected: "The image maker of each direction stage is the one the recipe names: art-director in cutscene, character, stage and new-look effect; ui-ux-designer in UI screen (job-types.md:58 '2-3 target reference images'); marketing in marketing art (job-types.md:97 '3-5 rough thumbnails', marketing.md:26)",
     observed: "'In a direction stage you are the only agent making ChatGPT images (one browser user at a time).'",
     evidence: "job-ui-screen.js:238 'in this step only the ui-ux-designer generates images'; job-marketing-art.js:240 'the rough thumbnails come in the direction sheet, made by marketing alone'. An art-director that follows its role file makes images in UI and marketing direction stages. Then two agents use the one built-in browser, or the art-director's images replace the job lead's G1 options.",
     smallest_fix: "Change line 25 to: 'In the cutscene, character and stage direction stages, and in effects that set a new look, you are the only agent that makes ChatGPT images. In UI screen and marketing art, the job lead makes them; you give style notes in words, numbers and existing references.'"}
  - {id: B2, class: blocking, check: C1, where: ".agents/roles/environment-designer.md:30, :34",
     expected: "Stage proof (G2) = 'a playable greybox in Studio: walk-test and playtest captures, first view, landmark read, route times' (job-types.md:47); 'lighting and polish only after the space plays well' (job-types.md:48); gates G1, G2 (L), G3 (rules/company.md:27-33)",
     observed: ":34 'In the proof stage, deliver your part of the integrated proof ...: the blueprint plus a target slice, before the full build.' :30 'Owner gates: references reviewed, blueprint approved before any building, packet before G3.'",
     evidence: "job-stage.js:512-514 builds the greybox in proof: 'No art, dressing or final light: this is the cheap proof the owner judges at G2.' A target slice is finished art. An agent that follows :34 makes art and light before the greybox plays, against :48. The gate list at :30 uses gate names that are not in the rules and has no G2. An L-stage maker reads that the next owner look after the blueprint is G3.",
     smallest_fix: ":34 → 'the playable greybox in Studio (grey blocks at true scale, a player-size dummy in every space, zone volumes), walked and captured, before any art'. :30 → 'Owner gates: G1 (route graph, blueprint draft, pictured looks: no building before the blueprint is approved), G2 for L (the playable greybox), G3.'"}
  - {id: B3, class: blocking, check: C1, where: ".agents/roles/film-director.md:32",
     expected: "Cutscene proof (G2) = 'storyboards + a timed Blender animatic with temporary sound and effect cues' (job-types.md:14)",
     observed: "'deliver your part of the integrated proof the job recipe names: the board contact sheet or a rough animatic, before the full build.'",
     evidence: "The word 'or' lets the job lead give only boards at G2, or an untimed 'rough' animatic. The recipe requires both, timed and with temporary cues. The same step already builds both. Only the proof sentence is wrong.",
     smallest_fix: "'... names: the board contact sheet and the timed Blender animatic with temporary sound and effect cues (greybox set where the set is missing), before the full build.'"}
  - {id: B4, class: blocking, check: C7, where: ".agents/roles/vfx-designer.md:31-34 (work method order)",
     expected: "'VFX and sound co-design the envelope before either builds' (job-types.md:86; also :15, sound-designer.md:24, vfx-designer.md:24, job-effect.js:433)",
     observed: "Step 2 frame script → step 3 layer plan → step 4 textures → step 5 'Write spec.json, the sound brief ...'. Sound enters only at step 5, after the build.",
     evidence: "A vfx-designer that follows the work method builds the layer plan and spec.json, then gives a sound brief. Sound then fits a finished picture. This is the order that the recipe removes. Line 24 says co-design comes first, but only 'In cutscenes', so in effect jobs (where vfx is job lead) the numbered steps are the only order.",
     smallest_fix: "Add after step 2: 'Co-design each event's envelope (wind-up, peak, tail) with the sound-designer on the event ids (exchange notes, at most 2 rounds) and merge it into the event timeline before step 3.' At step 5, the sound brief restates the agreed envelope."}
  - {id: B5, class: blocking, check: C3, where: ".agents/roles/ui-ux-designer.md:48",
     expected: "Prices and odds belong to progression-designer (job-types.md:58 'shops and odds: progression-designer + platform-policy'; README.md:11 'replaces economy-designer, J011-D3')",
     observed: "'economy designer for prices and odds'",
     evidence: "No role named economy-designer exists (ls .agents/roles). A ticket to it cannot be routed. A ui-ux-designer may not bring in the progression-designer for a shop.",
     smallest_fix: "'economy designer' → 'progression-designer'."}
  - {id: B6, class: blocking, check: C6, where: ".agents/roles/reviewer.md:43",
     expected: "'One review file per review, reviews/<artifact>-rev<N>-<reviewer>.md' (rules/messages.md:148; templates/jobs/review.md:1)",
     observed: "'Review files only (`knowledge/jobs/<job-id>/review-<ticket>.md` or the path the brief names)'",
     evidence: "The default path is outside `reviews/` and keys the file to a ticket, not to the artifact revision. Readiness checks and the selective recheck look for reviews by artifact and revision.",
     smallest_fix: "'Review files only (`knowledge/jobs/<job-id>/reviews/<artifact>-rev<N>-reviewer.md`, or the path the brief names)'."}
  - {id: B7, class: blocking, check: C5, where: ".agents/roles/reviewer.md:34, :35, :46",
     expected: "Findings in the rules/messages.md §6 fields (id, class blocking|recommendation|new request, where, expected, observed, evidence, smallest_fix) + keep + verdict fix-first|ready for the next review|ready for the owner (messages.md:150-161). The role's own :26 says so.",
     observed: ":34 'blocking findings (Critical, High, Medium) ... then at most a few one-line notes'; :35 'Disposition: merge, or fix first'; :46 'blocking findings as rows `severity · file:line · scenario ... · rule broken · fix direction`; notes'",
     evidence: "Two formats in one file. A reviewer that follows the hand-back section writes no class, no expected/observed, no keep and no §6 verdict. Then the maker's protected list (keep) and the lead's readiness check have nothing to read.",
     smallest_fix: "At :46: 'Write each finding in the §6 fields; put severity (Critical/High/Medium) in `evidence`; notes are class recommendation; disposition maps to verdict (merge = ready for the next review).'"}
  - {id: B8, class: blocking, check: C3, where: ".agents/roles/reviewer.md:39",
     expected: "Trust rules are rules/messages.md §7 (messages.md:165-169)",
     observed: "'A builder's claim is a claim (`rules/messages.md` §5)'",
     evidence: "messages.md §5 (:134) is the contract-change notice. The reference points to the wrong rule.",
     smallest_fix: "§5 → §7."}
  - {id: B9, class: blocking, check: C3, where: ".agents/roles/researcher.md:6 vs :19-20",
     expected: "A role that must run the packet has a tool that can run it",
     observed: "tools: 'Read, Grep, Glob, WebFetch, WebSearch' (no Bash); :19 'run the packet first'; :20 'run the packet your brief names (`python tools/context_packet.py ...`)'",
     evidence: ".claude/agents/researcher.md (generated) has the same tools, without Bash. A researcher cannot do step 4 of the load order (rules/knowledge.md:38). It must skip the packet or report blocked.",
     smallest_fix: "Add Bash (read-only use) to the tools at :6, or change :19-20 to say that the briefer runs the packet and puts its output in the brief."}
  - {id: B10, class: blocking, check: C3, where: ".agents/roles/doc-keeper.md:6 vs :20, :32",
     expected: "As B9; also knowledge/jobs filing ends with `python tools/kb_index.py` (part of the gate, rules/knowledge.md:112, tools/verify.py:152-155)",
     observed: "tools: 'Read, Write, Edit, Glob'; :20 run the packet; :32 'After writing, run `python tools/kb_index.py`'",
     evidence: "With no Bash tool, the doc-keeper cannot run the packet or the index. The indexes are then stale after every job close, and `kb_index --check` fails the gate.",
     smallest_fix: "Add Bash to the tools at :6 (for the two kit tools only), or move the kb_index run to the lead's close-out checklist."}
  - {id: B11, class: blocking, check: C6, where: "templates/jobs/status-block.md:2",
     expected: "'First line: STATUS ...' (rules/messages.md:92); 'Every hand-back starts with its status' (rules/company.md:80)",
     observed: "'# Hand-back (end of every hand-back)'",
     evidence: "This is the old process (status block at the end). All 24 role files point to this template for the §3 format, so an agent can put STATUS at the end. The fields under it are correct.",
     smallest_fix: "'# Hand-back (STATUS is the first line of every hand-back)'."}
  - {id: B12, class: blocking, check: C6, where: "templates/jobs/job-card.md:1, crew.md:1, ledger.md:1, decision-digest.md:1, beat-sheet.md:1, review.md:1, exchange-note.md:1",
     expected: "Every note under knowledge/ starts with typed frontmatter (rules/knowledge.md:61-72). The job folder is copied from templates/jobs/ (orchestration SKILL.md:37; knowledge/jobs/README.md:5).",
     observed: "These 7 templates start with an HTML comment and have no frontmatter. direction-sheet.md, evidence.md and contract-header.md do have frontmatter on line 1.",
     evidence: "tools/kb_index.py:17 says missing frontmatter is an ERROR. :77 exempts only README.md and paths under templates/, so the copies in knowledge/jobs/<id>/ (job-card, crew, ledger, digest, beat sheet, reviews/*, exchange/*) fail `kb_index --lint`, and tools/verify.py:152-155 fails the gate. Past jobs added the frontmatter by hand: J016 crew.md:1-8, J003..J015 ledger.md:1.",
     smallest_fix: "Put the frontmatter block from contract-header.md:1-9 (type: job, scope: game, status, updated, source, supersedes) and the Author line on line 1 of each of the 7 templates. Move the template comment below them."}
  - {id: B13, class: blocking, check: C6, where: "templates/jobs/beat-sheet.md:4 (whole file)",
     expected: "A contract carries a revision and a change table (rules/knowledge.md:76; knowledge/jobs/README.md:11). A contract change 'adds a row to the contract's change table' (rules/messages.md:135). The beat sheet is the cutscene contract (job-types.md:13).",
     observed: "Only '> Revision: <n>, <date>'. There is no change table and no consumers list. contract-header.md:11 says 'The beat sheet and the rig sheet already carry a revision'. The rig sheet has a change log (templates/rig/rig-sheet.md:88-99). The beat sheet has none.",
     evidence: "In the cutscene pilot, the film-director that copies this template has no place to record a beat-time change and its consumers to recheck. The §5 notice and the stale marking then have no record in the contract.",
     smallest_fix: "Add at the end: '## Change table | Revision | Date | What changed | Consumers to recheck | Acknowledged by |' (as contract-header.md:23-25), plus a 'Consumers' line."}
  # ---------------- recommendations ----------------
  - {id: R1, class: recommendation, check: C1, where: ".agents/roles/art-director.md:27",
     expected: "Review positions per recipe: character: art-director first after K-checks, before game-designer (job-types.md:35); marketing art: art-director before game-designer (:101); UI: after ui-ux-designer, before game-designer (:64); proof reviews: cutscene 2nd (:14), character 1st (:32), stage 2nd (:47), UI 2nd (:61)",
     observed: "'Reviews: the integrated look in every visual recipe, after the domain lead (film-director for cutscenes, game-designer for stages and features).'",
     evidence: "In marketing and character, the game-designer reviews after the art-director. 'After the domain lead' can make the art-director wait for the game-designer. Proof reviews are not listed.",
     smallest_fix: "List the position per recipe in one line, proof and final."}
  - {id: R2, class: recommendation, check: C1, where: ".agents/roles/game-designer.md:26, :38",
     expected: "Final reviews: also UI screen (last, job-types.md:64) and marketing art (last, :101). Proof reviews: character 3rd (:32), stage 1st (:47), UI 1st (:61), feature (plays the prototype, :74).",
     observed: ":26 lists only stage playtest, feature play, character role read, effect readability. :38 gives proof examples for pitch and pre-production jobs only.",
     evidence: "As the feature job lead, the role file does not say that its proof is the playable grey-box prototype that the feature-builder builds and the game-designer judges.",
     smallest_fix: "Add 'UI screen (the decision works, last) and marketing art (truthful to play, last)' to :26. Add the feature proof to :38."}
  - {id: R3, class: recommendation, check: C1, where: "ui-ux-designer.md:43 and :39; marketing.md:36; art-director.md:39",
     expected: "UI proof (L) = 'clickable Figma prototype of every state at phone size' (job-types.md:61) with '2-3 target reference images' at direction (:58). Marketing proof = 'the chosen thumbnail ... tested at real size and in the real layout' (:98). The art-director's proof part in a character job = the reference set (job-character.js:274 'the reference set comes in the proof stage').",
     observed: "ui-ux:43 'one screen or one component family'; ui-ux:39 '2-4 whole-screen references'; marketing:36 '3 title candidates ... and 1 thumbnail concept'; art-director:39 '2-3 direction thumbnails, or one review on one scene' (these are G1 items)",
     evidence: "Each file has the correct text elsewhere (ui-ux:28, marketing:26), so these are conflicts inside each file, not missing rules.",
     smallest_fix: "Change each example to the proof that its recipe names."}
  - {id: R4, class: recommendation, check: C1/C7, where: "feature-builder.md:22; architect.md:22",
     expected: "UI direction lead 'feature-builder or architect (data and remotes available)' (job-types.md:58); UI proof review 'feature-builder (buildable)' (:61); character 'feature-builder when it is wired into gameplay' (:34); effect 'feature-builder or quick-builder wires the spec' (:88)",
     observed: "feature-builder:22 names feature, UI and cutscene player integration only, and has no 'When you review' bullet. architect:22 names feature and cutscene only.",
     evidence: "When the feature-builder reviews a UI proof, the review rules (look first, §6 format, never edit) are not in its own file.",
     smallest_fix: "Add these rows to the two flow sections, and add the standard review bullet to feature-builder."}
  - {id: R5, class: recommendation, check: C1/C7, where: "vfx-designer.md:24, :41; sound-designer.md:24, :39",
     expected: "Stage review 'sound and VFX ambience check' (job-types.md:51). Effect co-design (:86). Interface negotiation needs no ticket (templates/jobs/ledger.md:4; rules/company.md:77).",
     observed: "Neither file names the stage ambience check. vfx has no 'When you review' bullet. vfx:24 says co-design only for 'In cutscenes'. vfx:41 and sound:39 give the co-design partner as a new-work ticket.",
     evidence: "Each file says the same about the other on cutscene timing (keep). The effect and stage parts are not symmetrical.",
     smallest_fix: "vfx:24 'In cutscenes and effects ...'. Add the stage ambience check to both files. Add the review bullet to vfx. Say that the envelope is an exchange note, not a ticket."}
  - {id: R6, class: recommendation, check: C2, where: "vfx-designer.md:45; sound-designer.md:43",
     expected: "The effect integrator wires the spec (feature-builder or quick-builder, job-types.md:88); sideways work with the interface owner (rules/company.md:76)",
     observed: "'hand wiring notes to the orchestrator'",
     evidence: "This old relay wording sends interface facts through the lead instead of to the integrator in crew.md.",
     smallest_fix: "'put wiring notes in your deliverable for the integrator the brief names'."}
  - {id: R7, class: recommendation, check: C7, where: "modeler.md:24, :33",
     expected: "'art-director reviews the model at the game camera on the real background before texture polish' (job-types.md:33; job-character.js:543-553)",
     observed: "The flow section and the build step (blockout → shape → rig parts → clean → UVs and textures) do not say to stop for the check-in.",
     evidence: "In the workflow, the brief adds the stop. Outside a workflow, a modeler can polish textures before the art-director looks.",
     smallest_fix: "In :33, add 'stop before texture polish for the art-director's check-in (captures at the game camera)'."}
  - {id: R8, class: recommendation, check: C2, where: "character-rigger.md:40, :30-31",
     expected: "The modeler exists (modeler.md; README.md:17). The animator runs as a stand-in (orchestration SKILL.md:35).",
     observed: ":40 'While the modeler role does not exist, the lead runs a stand-in with the modeler brief (J005-D2).' :30-31 send K1/K2 to 'the animator' and do not say it is a stand-in.",
     evidence: "The modeler sentence is no longer true. The animator stand-in rule that film-director.md:33 has is missing here.",
     smallest_fix: "Remove the modeler sentence. Add 'the animator is a stand-in until J006; its id comes from peers/crew.md'."}
  - {id: R9, class: recommendation, check: C1, where: "qa-lead.md:22",
     expected: "qa-lead is in the cutscene, stage (last), UI and feature review orders (job-types.md:19, :51, :64, :77). It is not in the character, effect or marketing orders.",
     observed: "'The technical check in every review chain, beside the creative reviews'",
     evidence: "The sentence is not true for 3 recipes and for the stage position.",
     smallest_fix: "'in the cutscene, stage (after ambience), UI screen and feature review chains'."}
  - {id: R10, class: recommendation, check: C7, where: "film-director.md:39",
     expected: "The cutscene interfaces include feature-builder (player contract, endings) and modeler (new cast) (job-types.md:15, :18)",
     observed: "The ticket list does not name feature-builder or modeler",
     evidence: "film:38 says 'engineering writes the player code' but gives no route to it.",
     smallest_fix: "Add 'feature-builder (player contract, endings), modeler (new cast, through the rig-sheet steps)'."}
  - {id: R11, class: recommendation, check: C1, where: "marketing.md:34",
     expected: "Review order: scripts → art-director → game-designer (truthful to play) (job-types.md:101)",
     observed: "'... the checklist and the art director's review before the owner sees it'",
     evidence: "The game-designer's truth check is not named.",
     smallest_fix: "Add 'then the game-designer's truth-to-play check'."}
  - {id: R12, class: recommendation, check: C5, where: "architect.md:51; feature-builder.md:49; quick-builder.md:44; reviewer.md:48; qa-lead.md:47; performance-engineer.md:47; researcher, explore, doc-keeper, studio-operator (no lesson line)",
     expected: "'every agent writes a lesson draft with its cause and layer' (rules/company.md:144; rules/knowledge.md:105; knowledge/inbox/README.md:30-31)",
     observed: "Six engineering roles say only 'write a lesson draft to knowledge/inbox/' and do not name cause and layer. Four roles have no lesson step. researcher.md:32 'Write scope: None'.",
     evidence: "/improve routes drafts by cause. Drafts without a cause cannot be routed.",
     smallest_fix: "Use the standard sentence '(what worked, what failed, owner corrections word for word, cause and layer)'. For roles that cannot write, use the `lesson_draft:` fallback in the hand-back (art-director.md:55)."}
  - {id: R13, class: recommendation, check: C5, where: "reviewer.md:48; qa-lead.md:47; researcher.md:35; explore.md:26",
     expected: "coverage states done | not done | skipped (rules/messages.md:107; handback.schema.json:16 enum)",
     observed: "'checked or skipped'; 'tested, not tested or blocked'; 'answered or not'; 'found or not found'",
     evidence: "In a workflow agent() call the schema rejects these words. Outside a workflow, the asker's coverage check reads different words.",
     smallest_fix: "Keep the role's own words in `why` and use the three states."}
  - {id: R14, class: recommendation, check: C3, where: "architect.md:30 vs :46",
     expected: "The write scope includes every file that the work method tells the role to write",
     observed: ":30 'list them in `knowledge/design/open-questions.md`'; :46 the write scope does not include that file",
     evidence: "An architect must break the method or the scope.",
     smallest_fix: "Add 'rows in knowledge/design/open-questions.md' to :46."}
  - {id: R15, class: recommendation, check: C2, where: ".agents/roles/README.md:5, :40",
     expected: "The roster describes the kit at 0.6.0 (24 roles; README.md:36)",
     observed: ":5 'Roles move in from the first game in phase 3'; :40 'the kit ships only the orchestrator (the orchestration skill) and the system'",
     evidence: "This is old wording. It contradicts the table above it and the J016 note at :36.",
     smallest_fix: "':40 New roles are built with /build-agent from owner material'. Remove ':5 Roles move in ... phase 3'."}
  - {id: R16, class: recommendation, check: C6, where: "templates/role.md:4-7, :62-66",
     expected: "The template has the sections and keys that the role files actually use",
     observed: "There is no slot for the Riot pointer bullet (14 roles have it, e.g. film-director.md:26). The optional `tools` and `color` keys are missing (sync_harness.py:56; all 24 roles use `color`). The `lesson_draft:` fallback (5 roles) is missing.",
     evidence: "A role built from the template with /build-agent will not have these.",
     smallest_fix: "Add the Riot bullet with '<if the role has a row in riot-extracts.md §4>', and comment lines for the optional keys."}
  - {id: R17, class: recommendation, check: C6, where: "templates/jobs/beat-sheet.md:22",
     expected: "The contract fields that the recipe names: stable event ids, trigger, VFX cue, sound cue, player control, skip consequence (job-types.md:13); beat ids such as B04 (rules/messages.md:139)",
     observed: "Beats are numbered '1' and the beat row has no event-id or cue columns. Cues live in the shot list (templates/film/shotlist.example.json:110). Skip and control are in the state sheet (:29, :34).",
     evidence: "Most fields exist across the two files, but the beat id format is different from messages §5.",
     smallest_fix: "Use 'B01' beat ids and add an 'Event ids (shot list)' column."}
keep:
  - "Every role file has the same flow block: the packet with --role/--job, inputs with revisions + built_on (knowledge.md §3-4), the sideways bullet (exchange notes + SendMessage by crew.md id, recorded in contract/decision log), and for reviewers the §6 bullet (look first, never edit)."
  - "The hand-back paragraph in 21 roles: STATUS first, coverage done/not done/skipped, built_on, evidence per pass, no report*/summary* names."
  - "Frontmatter: the tier and effort of all 24 roles match README.md:9-34. All 77 skill entries (21 roles) exist under .agents/skills/. memory is project for all (20 explicit; 4 by the sync_harness.py:206 default)."
  - "All rules § references resolve except reviewer.md:39 (B8). All skill § and reference-file § references in role files resolve (25 checked)."
  - "Job lead and integrator lines match orchestration SKILL.md §2 and job-types.md for all 7 recipes (film, art, environment, ui-ux, game-designer + architect, vfx, marketing)."
  - "Cut decision rights are the same in modeler.md:40, character-rigger.md:39, company.md:47 and job-character.js:539 (one counter round, posed proxy render, look change to the owner)."
  - "Route ownership is the same in environment-designer.md:22,37 and game-designer.md:23, and matches job-types.md:43."
  - "Cutscene timing is the same in sound-designer.md:24 and vfx-designer.md:24 (temporary cues for the animatic, finish against the timing list, co-design before build)."
  - "The animator stand-in handling in film-director.md:33 and the 'give the brief to the lead' rule for planned roles (environment, game-designer, progression)."
  - "No old gate names (except B2), no hop counts, no '3 concurrent', no approval on the owner's behalf, no reviewer edits (C2 grep over all scope files)."
  - "These templates match the rules field for field: review.md = messages §6; exchange-note.md = §4; intent-brief.md = §2 (all 22 keys, in order); handback.schema.json = §3 (evidence before status/outcome); ledger.md statuses = company §8; contract-header.md change table = messages §5; direction-sheet.md signatures = company §4.2; job-card.md gates bound to revisions."
verdict: fix-first
questions:
  - {q: "job-types.md:51 'game-designer playtest' and :74 'the game-designer plays it (studio-operator for multi-client)' versus game-designer.md:44 'you do not drive Studio' and job-feature.js:344 (studio-operator plays, game-designer reviews captures). The role file agrees with the workflow; the recipe wording does not. Is the recipe or the workflow the intent?", default: "keep the role and workflow; reword the recipe as 'the game-designer judges the studio-operator's play captures'"}
  - {q: "analyst.md:26 puts the analyst in 'the feature recipe's direction stage'. job-types.md:71 does not name the analyst. Is this intended as 'when the lead adds it'?", default: "reword as 'when the lead adds you'"}
outside_scope:   # seen while checking; not in the files under review, so no finding id
  - "rules/company.md:61 'Proof: domain lead → art-director → architect review it' for every M/L job. This contradicts the proof review orders in job-types.md:32 (art → animator → gd), :47 (gd → art → perf) and :61 (gd → art → feature-builder)."
  - "rules/company.md:67 'rules/knowledge.md §5' for filing (should be §7); :144 '§5-6' for lesson drafts (should be §8)."
  - "kit.json codex_preamble 'End every hand-back with the status block from rules/company.md §4-5'. This is the old wording: statuses are in §8, and STATUS comes first."
  - "job-types.md:19 (cutscene review order) has no code reviewer for the player code that the feature-builder builds (:18). AGENTS.md §2 says 'before any merge: code-review'."
  - "job-stage.js:100 FINDING schema (id, class, maker_role, where, evidence, smallest_fix) has no expected/observed (messages §6)."
</spec>
```

## Role × recipe (from job-types.md; JL job lead · DL direction lead · PR proof reviewer · M maker · I integrator · CI check-in · FR final reviewer)

| Role | Cutscene §1 | Character §2 | Stage §3 | UI §4 | Feature §5 | Effect §6 | Marketing §7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| film-director | JL, DL, PR1, CI anim, I, FR1 | | | | | | |
| art-director | DL, PR2, CI set, FR2 | JL, DL, PR1, CI model, FR1 | DL, PR2, FR2 | DL, FR4 | FR last (visible) | DL if new look, FR2 | DL, FR1 |
| game-designer | consulted (state sheet) | DL, PR3, FR2 | DL, PR1, CI, FR1 | DL, PR1, FR last | JL, DL, PR (judges play), FR | DL, FR1 | DL, FR2 |
| environment-designer | M (sets) | | JL, DL, I | | | | |
| architect | DL, PR3 | | | DL (or feature-builder) | tech lead, DL | | |
| feature-builder | M (player) | I (wiring) | | DL (or architect), PR3, I | M (prototype), I | I (or quick-builder) | |
| ui-ux-designer | M (letterbox, subtitles, skip) | M (icon) | | JL, DL, FR3 | M | | |
| vfx-designer | M (co-design) | M | M, FR (ambience) | M (library) | M | JL, DL, M | |
| sound-designer | M (co-design), FR sync | M | M, FR (ambience) | M | M | DL, M, FR sync | |
| modeler | M (new cast) | M, proof blockout | M (kit) | | | | |
| character-rigger | M (new cast) | DL, M, proxy rig, FR (K-check) | | | | | |
| animator (stand-in) | M | DL, PR2, I | | | | M (timing) | |
| progression-designer | | | | DL (shops, odds) | DL, M | | |
| performance-engineer | FR ∥ qa | FR last | DL, PR3 | | FR (if heavy) | | |
| qa-lead | FR | | FR last | FR2 | M (tests), FR | | |
| reviewer | | | | FR1 | FR | | |
| quick-builder | | | | | | I (or feature-builder) | |
| studio-operator | (multi-client, devices) | | (walk tests) | | M (play captures) | M (capture) | |
| marketing | | | | | | | JL, DL, I |
| trend-scout | | | | | | | DL (optional) |

## Coverage per role

| Role | C1 flow vs recipe | C2 old wording | C3 refs | C4 frontmatter | C5 hand-back / lesson | C7 pairs | Findings | Blocking problem? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| film-director | proof part wrong | ok | ok | ok | ok | brief list short | B3, R10 | yes (B3) |
| art-director | review positions vague | ok | ok | ok | ok | image maker conflict | B1, R1, R3 | yes (B1) |
| environment-designer | proof + gates wrong | old gate names | ok | ok | ok | ok (gd routes) | B2 | yes (B2) |
| game-designer | review list short | ok | ok | ok | ok | ok | R2, R3 | no |
| ui-ux-designer | proof example | old role name | economy designer | ok | ok | ok (feature-builder) | B5, R3 | yes (B5) |
| vfx-designer | stage ambience review missing | relay to orchestrator | ok | ok | ok | co-design order | B4, R5, R6 | yes (B4) |
| sound-designer | stage ambience review missing | relay to orchestrator | ok | ok | ok | ok | R5, R6 | no |
| modeler | check-in missing | ok | ok | ok | ok | ok (rigger) | R7 | no |
| character-rigger | ok | stale modeler text | ok | ok | ok | ok | R8 | no |
| architect | UI DL missing | ok | ok | ok | no cause/layer | ok | R4, R12, R14 | no |
| feature-builder | UI DL/PR, wiring missing | ok | ok | ok | no cause/layer | ok (ui) | R4, R12 | no |
| quick-builder | ok | ok | ok | ok | no cause/layer | ok | R12 | no |
| reviewer | ok | ok | §5 wrong | ok | format, path, coverage words | ok | B6, B7, B8, R12, R13 | yes (B6-B8) |
| qa-lead | "every chain" | ok | ok | ok | coverage words, no cause/layer | ok | R9, R12, R13 | no |
| performance-engineer | ok | ok | ok | ok | no cause/layer | ok | R12 | no |
| progression-designer | ok | ok | ok | ok | ok | ok | — | no |
| studio-operator | ok | ok | ok | ok (memory default) | no lesson | ok | R12 | no |
| marketing | proof example; gd review missing | ok | ok | ok | ok | ok | R3, R11 | no |
| trend-scout | ok | ok | ok | ok | ok | ok | — | no |
| analyst | question | ok | ok | ok | ok | ok | question 2 | no |
| live-ops-designer | ok (not a recipe) | ok | ok | ok | ok | ok | — | no |
| researcher | ok | ok | no Bash for packet | ok (memory default) | no lesson; coverage words | — | B9, R12, R13 | yes (B9) |
| explore | ok | ok | ok | ok (memory default) | no lesson; coverage words | — | R12, R13 | no |
| doc-keeper | ok | ok | no Bash for packet / kb_index | ok (memory default) | no lesson | — | B10, R12 | yes (B10) |
| README.md | ok | old wording | ok | tiers/efforts are the reference | — | — | R15 | no |
| templates/role.md | — | ok | ok | ok (line 1) | ok | — | R16 | no |
| templates/jobs/* | — | status-block header | ok | 7 templates have no frontmatter | status-block fields ok | — | B11, B12, B13, R17 | yes |
