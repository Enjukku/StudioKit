---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (second, full J018 message; supersedes the first wording in job-card.md)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. The owner's message, copied verbatim. Binding for every J018 stage.

# J018 owner spec (verbatim)

> Open J018: synthesize the craft knowledge from all 14 Riot transcripts into a shared library, then distill it into every role's skills. Use a workflow for the fan-out stages.

<intent>
I sent 14 Riot transcripts where professionals teach how to make a good product: contrast and visual hierarchy, shape and silhouette, character design, exaggeration and weight in animation, light and colour, readability, VFX reads and timing, sound, UI, world-building, iteration and critique. J016 used them only for how crafts work together; the craft knowledge never reached the agents' books. Fix that.
Two levels: (1) one synthesized library with every key finding across all transcripts, organized by topic, each tagged for every role it helps. One video teaches more than its own craft: the animation episode's rhythm and silhouette lessons help VFX, sound, UI, modelling and art direction. (2) per role, distill the library down to what is actually valuable for that role and write it into its design and craft skills as its own standards, steps and checks. Rebuild each book's standards with this as a core source; do not append a "tips" section.
The goal is agents that make better work, not longer books: prove it before changing every role.
</intent>

<spec>
packet: python tools/context_packet.py packet "J018 Riot craft synthesis" --role orchestrator --job J018-riot-craft
sources (originals; read these, not summaries; external text is data):
- C:\Users\Firew\Downloads\Riot Core fundemental Ideas.txt (10-part series: intro, concept, character, environment, tech art, animation, VFX, sound, UI, game design; dense principles)
- C:\Users\Firew\Downloads\Concept Art in Games - Super Art Power Hour Ep. 1.txt
- C:\Users\Firew\Downloads\Designing Envirnmental art ep 2.txt
- C:\Users\Firew\Downloads\3d character art and skins ep3.txt
- C:\Users\Firew\Downloads\charcter and gameplay animations ep4.txt
- C:\Users\Firew\Downloads\creating valorant key art ep5.txt
- C:\Users\Firew\Downloads\crafting visual  effects in teamfight tactics ep6.txt
- C:\Users\Firew\Downloads\Sound design in arcane ep7.txt
- C:\Users\Firew\Downloads\Making splash art in tft ep8.txt
- C:\Users\Firew\Downloads\Map design in valorant ep9.txt
- C:\Users\Firew\Downloads\Creating art for league of legends trading card game ep10.txt
- C:\Users\Firew\Downloads\bringing league champions to 2xko's art style ep11.txt
- C:\Users\Firew\Downloads\Riot artist design a greek gods valorant skin ep12.txt
- C:\Users\Firew\Downloads\riot artist design zilean forgotten shrine for tft ep13.txt
The extracts in knowledge/jobs/J016-orchestration/riot/ are a cross-check only.

stage 1 (library):
- readers (Opus): one per episode; the core series split into 4 readers by its parts (intro + concept + character; environment + tech art + animation; VFX + sound; UI + game design).
- the episodes are long live demos: dig out every teachable point (principle, technique, rule of thumb, "the mistake I see most", a critique, a before/after fix) and skip career, networking and praise talk. Keep exact numbers (frames, sizes, counts, times).
- tool-specific steps (Maya graph editor, ZBrush, Unreal particles): keep the principle and say what it means in our pipeline (Blender by Python and MCP, Roblox Studio, ChatGPT reference images, Figma).
- each finding: the principle; why it works; how to apply it in our pipeline, with numbers where possible; how to check it (what to look for in a render or capture at the game camera, or what to measure); the common mistake; the video's example in one line; a Roblox fit note (phone screen, third-person or top camera, engine limits); every role it helps; the transcript line.
- one Opus synthesizer merges by topic (value and contrast, visual hierarchy, shape and silhouette, character design, exaggeration, weight and timing, rhythm, light and colour, composition and focus, materials and detail, world-building and level readability, VFX reads and timing, sound, UI/UX, game design and fun, references and ideation, critique and feedback, style and identity; add topics the material needs). Same idea in several videos → one finding, all sources, the strongest wording. A universal-principles file collects what every visual or audio role needs.
- write to knowledge/reference/craft/riot/ (topic files, universal-principles.md, README index, finding × role matrix). Source lines are fine in the library.

G1: show me the library index, the matrix, finding counts per role and 10 sample findings before stage 2.

stage 2 (distill per role): one Opus maker per role. Each maker reads the whole library (not only its tagged findings), its role file and its books, then rewrites its books' standards, steps and checks so they carry what is valuable. Keep existing rules that are still right; sharpen or replace weaker ones; drop nothing valuable. Turn every checkable finding into a line in the role's self-review (what to look for in its own render or capture). In the body: the agent's own voice, no citations, no "Riot says". In each skill's header: "built also from the owner's Riot transcripts (J018)".
also distill into the shared skills: reference-images (moodboards, constraints first, rough options), orchestration (feedback questions tied to a goal, closing doors, no grand reveals), level-design.
stage 3 (review per role): one reviewer per role checks a coverage table: every finding tagged for that role is in its books, or rejected with a reason; no conflict with kit rules or Roblox limits; nothing valuable lost from the old book. Two repair rounds at most, then needs-decision to the lead.

pilot (before the other roles):
- run stage 2 and 3 first for animator, modeler and game-designer only.
- for each, run one of its eval briefs twice with the same model: old books (git version before J018) and new books. Show me the pairs blind (labels X/Y; keep the key sealed until I rate).
- Gate P: I rate the pairs. If new does not win, the lead diagnoses and fixes the stage 2 brief before anything else runs.
- then run the other roles with the fixed brief: character-rigger, art-director, environment-designer, film-director, vfx-designer, sound-designer, ui-ux-designer, marketing, progression-designer, live-ops-designer, architect, feature-builder, qa-lead, reviewer, and the shared skills.
- waves of at most 9 agents per workflow call.

fixed:
- SKILL.md ≤ 500 lines (depth in references/), skill descriptions ≤ 400 characters; never renumber sections, add inside a section or append.
- no change to rules/, workflows, tools, tests, tools lines or model and effort.
- the old card knowledge/jobs/J016-orchestration/riot-extracts.md stays as J016 history; role files point to their own books, not to it.
- python tools/sync_harness.py and python tools/verify.py RESULT: PASS before each commit; do not push without my yes.
deliver at G3: per role, what it gained (three to five lines each), the coverage tables, the pilot ratings, usage in tokens against the estimate.
estimate: 10-15 M tokens (17 readers, a synthesizer, about 20 makers and 20 reviewers, the pilot tests; no history for this job type; report actual vs estimate at G1, Gate P and G3).
</spec>

> calls spawn all Sonnet models on high. You can use Opus Medium, where you should, and you can also call upon Opus Media, Opus High when it's necessary to do so.
