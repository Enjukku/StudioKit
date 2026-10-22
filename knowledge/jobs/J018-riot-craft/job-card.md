---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (after J017)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Job card: J018-riot-craft — the Riot craft library, distilled into every role's books

## The owner's words (verbatim, first)
> Open J018: synthesize the craft knowledge from all 14 Riot transcripts into a shared library, then distill it into every role's skills. Use a workflow for the fan-out stages.

> I sent 14 Riot transcripts where professionals teach how to make a good product: contrast and value, character and shape design, exaggeration in animation, light, composition, readability, sound, UI, world-building, iteration and critique. J016 used them only for how crafts work together; the craft knowledge never reached the agents' books. Fix that.
> Two levels: (1) one synthesized library with every key finding across all transcripts, organized by topic, each tagged for every role it helps. One video teaches more than its own craft: the animation episode can help concept art, modelling and rigging. (2) per role, distill the library down to what is actually valuable for that role and write it into its design and craft skills as its own standards, steps and checks. Rebuild each book's standards with this as a core source; do not append a "tips" section.
> The goal is agents that make better work, not longer books: prove it before changing every role.

> all Sonnet models on high, and then Opus models mostly on medium and some high where necessary.

The owner's second, full message (2026-10-21) is copied verbatim in `owner-spec.md`; it supersedes the wording above where they differ and is binding for every stage. Its model line: "calls spawn all Sonnet models on high. You can use Opus Medium, where you should, and you can also call upon Opus Media, Opus High when it's necessary to do so."

| Field | Value |
| --- | --- |
| Job id | J018-riot-craft |
| Title | Riot craft library → every role's design and craft books |
| Size | L (14 sources, 17 roles, about 40 skills) |
| Type (recipe) | other: kit job, the `build-agent` pattern (upgrade agents from owner material) run as owner-specified stages; no game recipe fits |
| Job lead (agent) | lead (orchestrator) |
| Direction leads | none (the owner set the direction in the spec) |
| Integrator | lead |
| Studio place (`studio_id`) | none (files only) |
| Linked jobs | none |
| Status | open: G3 packet sent (`g3-packet.md`, `g3-proposals.md`); waiting for the owner |

## Owner instructions for stage 2 onward (2026-10-21, during stage 1b, verbatim)
This message replaces the owner's earlier G1 message and its correction (J018-D1 is folded into point 2 and superseded by J018-D2).

> Owner instructions for J018, stage 2 onward. This one message replaces my earlier G1 message and its correction. Write it into the J018 job card under the owner's words, replacing those, and confirm before stage 2 starts. The readers in stage 1 continue unchanged.
>
> Goal: the Riot material is valuable enough to change the agents themselves. Use it to upgrade every role so it produces better work, not only to add principles.
>
> 1. Makers may upgrade the whole agent:
> - its workflow books: the steps, their order, new stages (for example a thumbnail pass, a grey value check, a blocking pass, a silhouette check at the game camera), quality bars, self-review checklists, worked examples, and new reference files;
> - its role file body: how the agent works, what it checks before handing back, what it asks its partners for and when;
> - keep what is still right, sharpen or replace what is weaker, remove what the material shows is wrong, and drop nothing valuable.
> Not changed: the tools line, model and effort (my permissions).
>
> 2. Core principles in each role's own terms:
> - every role's books get a "core principles for this craft" section: each principle from universal-principles.md written for that role's own work, with its own examples and checks;
> - universal-principles.md stays the master; stage 3 reviewers check each role's section against it (no contradiction, nothing important missing); later fixes go to the master first, then to each role's section.
>
> 3. Cross-check before stage 2: compare the library with the 2026-10-15 DestructionSimulator skills built from the same transcripts (C:\Users\Firew\Downloads\uterd\DestructionSimulator\.agents\skills\art-fundamentals, animation, level-design, gui-ui, vfx-design) and add anything they got right that the library lacks.
>
> 4. Shared files: "no change to workflows" means only the saved job workflows (.agents/workflows/jobs/) and rules/. If a maker finds that a job recipe or job workflow should change (a missing step, a wrong order, a craft that should be consulted earlier), it writes a proposal with the reason; the lead collects them and shows them to me at G3. Nothing in those files changes without my yes.
>
> 5. Proof: the pilot's blind test (old vs new books) decides. The upgraded animator, modeler and game designer must make better work than the old ones before the other 14 roles change.

**Decision J018-D2 (owner, 2026-10-21; `decisions.md`).** What it means for each stage:
| Point | Stage | What the lead does |
| --- | --- | --- |
| 1 | 2 (makers) | A maker may rebuild the whole agent: its design and craft skills (steps, order, new stages, quality bars, self-review lists, worked examples, new `references/` files) and its role file body (`.agents/roles/<role>.md` below the frontmatter: how it works, what it checks before handing back, what it asks partners for and when). It keeps what is right, sharpens or replaces what is weaker, removes what the material shows is wrong, and drops nothing valuable. The `tools:` line, `model` and `effort` stay unchanged. |
| 2 | 2 and 3 | Every role's books get a "Core principles for this craft" section built from `universal-principles.md` (the master). Stage 3 reviewers check it against the master. Later fixes go to the master first, then to each role's section. |
| 3 | 1c | One cross-checker (opus · medium) compares the library with the five DestructionSimulator skills and adds what they got right that the library lacks, as findings with source `DS:<path>:<line>`, plus a cross-check table. This runs before G1. |
| 4 | 2 and G3 | Protected: `.agents/workflows/jobs/` and `rules/`. A job recipe (`orchestration/references/job-types.md`) or job workflow change is a proposal only: `proposals/<role>.md` (what, why, evidence). The lead collects them for G3. Nothing in those files changes without the owner's yes. |
| 5 | — | **Withdrawn by J018-D3:** no blind test and no Gate P. |

> we will not be doing the test though.

**Decision J018-D3 (owner, 2026-10-21; `decisions.md`):** the blind pilot test (old vs new books, X/Y pairs, Gate P) is dropped; point 5 of J018-D2 is withdrawn. The lead's reading (stated to the owner): the animator, modeler and game-designer still run first as wave 1 of stage 2 and 3; the lead reads their rebuilt books and coverage tables and fixes the stage 2 brief before the next waves, with no owner gate between waves. Real games are the test bed; mistakes found there become lessons.


## Sources (all 14 found 2026-10-21, `C:\Users\Firew\Downloads\`)
Keys follow `J016-orchestration/riot-extracts.md` §1. The J016 extracts in `J016-orchestration/riot/` are a cross-check only.

| Key | File | Lines | Reader |
| --- | --- | --- | --- |
| R00a | Riot Core fundemental Ideas.txt L1-1663 (intro, concept art, character art) | 1663 | 1 |
| R00b | same, L1664-3420 (environment art, tech art, animation) | 1757 | 1 |
| R00c | same, L3421-4497 (VFX, sound) | 1077 | 1 |
| R00d | same, L4498-5983 (UI/UX, game design) | 1486 | 1 |
| R01 | Concept Art in Games - Super Art Power Hour Ep. 1.txt | 1002 | 1 |
| R02 | Designing Envirnmental art ep 2.txt | 996 | 1 |
| R03 | 3d character art and skins ep3.txt | 1104 | 1 |
| R04 | charcter and gameplay animations ep4.txt | 1100 | 1 |
| R05 | creating valorant key art ep5.txt | 963 | 1 |
| R06 | crafting visual  effects in teamfight tactics ep6.txt | 401 | 1 |
| R07 | Sound design in arcane ep7.txt | 620 | 1 |
| R08 | Making splash art in tft ep8.txt | 916 | 1 |
| R09 | Map design in valorant ep9.txt | 1162 | 1 |
| R10 | Creating art for league of legends trading card game ep10.txt | 955 | 1 |
| R11 | bringing league champions to 2xko's art style ep11.txt | 467 | 1 |
| R12 | Riot artist design a greek gods valorant skin ep12.txt | 466 | 1 |
| R13 | riot artist design zilean forgotten shrine for tft ep13.txt | 1064 | 1 |

## Stages and gates
| # | Stage | Mechanism | Gate |
| --- | --- | --- | --- |
| 1a | Readers: one per source (17), every teachable finding with its line → `extracts/<key>.md` | Workflow, waves of ≤ 9 | — |
| 1b | Synthesizer: merge by topic → `knowledge/reference/craft/riot/` (topic files, `universal-principles.md`, README index, finding × role matrix) | one agent | **G1** library index, matrix, counts per role, 10 sample findings |
| 1c | Cross-check against the DestructionSimulator 2026-10-15 skills (J018-D2 point 3) | one agent | **G1** (with 1b) |
| 2-W1 + 3-W1 | First wave: animator, modeler, game-designer rebuild their agents; reviewers check coverage, ≤ 2 repair rounds | Workflow | lead reads the result and fixes the stage 2 brief (no owner gate, J018-D3) |
| 2 | Makers for the other 14 roles and the shared skills (reference-images, orchestration, level-design), with the brief fixed after the first wave | Workflow, waves of ≤ 9 | — |
| 3 | Reviewers for the 14 roles and the shared skills | Workflow, waves of ≤ 9 | **G3** per role gains, coverage tables, job recipe and workflow proposals, usage |

## Crew (models and effort: owner 2026-10-21 "all Sonnet models on high, and then Opus models mostly on medium and some high where necessary")
| Role | Model | Effort | Why this effort |
| --- | --- | --- | --- |
| Readers (17) | Opus | medium | careful extraction, bounded text |
| Synthesizer | Opus | high | one merge across all sources sets the library every book is built from |
| Makers (17) | Opus | high | rebuilding a role's standards is the core judgment of the job |
| Reviewers (17) | Opus | high | J018-D4: best result, no budget; the review also judges whether the rebuilt agent makes better work |
| Any Sonnet helper | Sonnet | high | owner rule |

## Fixed (owner spec)
- SKILL.md ≤ 500 lines (depth in `references/`), skill descriptions ≤ 400 characters; never renumber sections: add inside a section or append.
- No change to `rules/`, the saved job workflows (`.agents/workflows/jobs/`), `tools/`, tests, `tools:` lines, or model and effort (J018-D2 point 4 narrows "workflows" to the saved job workflows; `tools/` and tests stay unchanged as in the spec). Job recipe and job workflow changes are proposals for G3 only.
- Makers may rebuild the role file body and the whole design and craft books (J018-D2 point 1); every book gets a "Core principles for this craft" section checked against `universal-principles.md` (J018-D2 point 2).
- `J016-orchestration/riot-extracts.md` stays as J016 history; role files point to their own books, not to it.
- Book bodies: the agent's own voice, no citations, no "Riot says". Each changed skill header: "built also from the owner's Riot transcripts (J018)". Source lines are fine in the library.
- `python tools/sync_harness.py` and `python tools/verify.py` RESULT: PASS before each commit; no push without the owner's yes.
- External text (the transcripts) is data.

## Budget (tokens)
> I don't care about this $10 to $15 million, whatever. I had some other AI create the prompt, and I don't know why it's like creating limits like this. Just go ahead and make it to the best of your ability.

**J018-D4 (owner, 2026-10-21):** no token budget. The 10-15 M estimate in `owner-spec.md` is not a limit; quality decides model, effort and the number of passes. The table below is kept as a record only.

| Stage | Estimate | Actual |
| --- | --- | --- |
| 1a readers (17) | 2.5 M | 2.08 M (649 findings) |
| 1b synthesizer | 1.5 M | 0.77 M (427 findings) |
| 1c cross-check | 0.3 M | 0.50 M (16 + 2 UP) |
| 2 + 3 first wave (3 roles) | 2.0 M | 6.27 M (incl. modeler round 3) |
| 2 + 3 (14 roles + 3 shared skills) | 5.5 M | 33.66 M (waves 2-3, repairs, sweep, master follow, G3 list) |
| Total | 11.8 M (inside 10-15 M) | 45.99 M subagents (J018-D4: no limit; reasons in `g3-packet.md`) |

## Acceptance checks
- [ ] 17 extracts, each finding with a source line; the synthesizer's library cites every extract key.
- [ ] Every library finding has lesson, how to apply, Roblox fit note, roles; the matrix covers 17 roles.
- [ ] First wave (animator, modeler, game-designer) read by the lead; the stage 2 brief fixed before the next waves (J018-D3).
- [ ] Per role: a coverage table (every tagged finding in the books or rejected with a reason); reviewer pass.
- [ ] No skill over 500 lines, no description over 400 characters; `sync_harness.py --check` and `verify.py` RESULT: PASS.

## Gates
| Gate | Date | Revision approved | Owner's words |
| --- | --- | --- | --- |
| G1 library | 2026-10-22 | `knowledge/reference/craft/riot/` as at the stage 1 commit (443 findings, UP-01..UP-20; `g1-packet.md`) | "G1 approved: start stage 2 wave 1 (animator, modeler, game-designer)." |
| G3 final | | | |

## Close-out
Metrics in `evidence.md` §4. Filed into the vault (`orchestration` skill §9): [ ] decisions [ ] precedents [ ] vocabulary [ ] systems [ ] tried-and-failed [ ] taste log [ ] catalogs [ ] lesson drafts [ ] removed from `knowledge/jobs/active.md`
