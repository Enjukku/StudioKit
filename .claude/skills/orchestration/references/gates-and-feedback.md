> Author: J018 maker orchestration · claude-opus-5-5 · high · 2026-10-22 (repair rounds 1 and 2 the same day). Part of `orchestration`: built also from the owner's Riot transcripts (J018). The lead's side of feedback with the owner: goal questions, gate packets, options, closed doors, owner notes, showing early, when a job is done. Binding rules: `rules/company.md` §2, §7, §11; formats: `rules/messages.md`. The checks you run before a report: `orchestration` SKILL §14. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021): outside method from the target-experience sentence, BAR and belief lines, floor and bar. Revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design): no G2, G1 shows the agreed plan, built work first at G3, no rough reviews.

# Gates and feedback with the owner

## 1. The goal question
- Take the goal word from the job card: the target experience, the sell list or the success test ("loyal", "dangerous", "a cosy place to come back to", "reads in one second on a phone").
- The question's shape (one decision, labelled options, one recommendation, the default) is SKILL §8.
- Good: "Which pet reads as the most loyal friend at phone size? I recommend B: its ears and tail point at the player in the idle pose. Default: B." Bad: "Do you like these?", "Thoughts?", "Which is cooler?".
- Record which option the owner chose, the owner's words and the reason given. A reason that names a new goal goes back into the job card's four lines.
- When every option meets the goal, the rest is taste: recommend one and let the owner choose; never invent the owner's taste to break the tie. After the choice, commit: the pick is not reopened without a new reason.

Screening aid: `grep -n -i -E "do you like|like it\?|thoughts|what do you think|prefer|good\?|cooler\?" <packet.md>` lists likely taste questions (exit 0 = a line to read). False hits: "thoughts" or "prefer" in prose ("my thoughts on cost", "players prefer short routes"), a goal question that uses "prefer". Misses: other wordings ("Happy with this?", "Good to go?"); it cannot tell whether the goal word is present. Read every hit, and the question line itself, against the job card before you send.

## 2. Gate packets
| Gate | Shows first | The question | Evidence beside it | Closes |
| --- | --- | --- | --- | --- |
| G1 direction | What the recipe's "G1 shows" row names, with the agreed plan (plan revision 2, J024). Where it shows pictured options (L): one option sheet, the recipe's count (2-3; marketing art 3-5) at equal finish (full images at the highest quality), same subject and camera, labelled, grey and black-fill next to colour where the job lead made them. Options that failed the read checks are listed under the sheet as numbers with the reason. A feature shows the behaviour in player words and the risky claims, with pictures only where the contract has visible parts | The goal question, one recommendation | Per option: what it adds to play, what it costs (rig, sound time, tech, budget), its risk; the research board path; the warm-up is not shown as an option | The options not picked |
| G2 proof | Removed in J024: no job type has a proof stage or G2. The big shapes (layout, proportions, timing beats, key light) are frozen at G1 with the agreed plan | — | — | — |
| G3 final | The real result in Roblox: game-camera captures at phone size in the busiest supported scene; the playable build | "Does this deliver <success test>?" | Every acceptance check with its label and input; the could-not-check list; owner-confirmed lines; the animator's two timing takes of each signature, tell or emote clip as playable previews when the clip has them (`animation-design` §3 step 6) | The job (close) |

**Image budget** (light-check rule, J005-D8; PROPOSAL counts a brief or the owner may change): G1, one option sheet per question plus at most one diagnostic image per failing number the owner should see; G3, at most 6 key stills plus the playable previews (one per take the owner picks between). Everything else goes as numbers with their file paths. Name the images the owner is asked to look at (the artifact, the option sheet, each diagnostic still) in one line under the goal question, `Shown: a.png, b.png`; that line is what the budget counts, and a contact sheet counts as one.

Screening aids, then count by eye: `grep -n "^Shown:" <packet.md> | awk -F: '{l=tolower($0); n=gsub(/\.(png|jpe?g|webp)/,"",l); print "line " $1 ": " n " images"}'` prints one line per `Shown:` line (one per question) with its image count; each count must sit inside that question's budget. No output means no line starts with `Shown:` (missing, bulleted, bold or inline in a sentence): the packet is not ready. It misses images sent outside the file, named without an extension or in another format (gif, svg); a contact sheet counts as one, as the budget does. `grep -n -o -i -E "\.(png|jpe?g|webp)\b" <packet.md>` lists every image name in the file, including evidence paths next to numbers, rejected images and log rows: a ceiling, never the count. Before you send, open the packet and check by eye that every image path outside the `Shown:` line is one of the shown images named again, sits next to a number as evidence, or is under the rejected list.

**Every packet carries:**
- checks in the order gameplay read, then feel, then look (clarity before satisfaction before style);
- a label on each check (gate-verified, MCP-verified, owner-confirmed, not verified) that names its input;
- stand-ins by name: temp sound, placeholder sprites, proxy rig, PROPOSAL numbers, placeholders left for later design;
- the could-not-check list: the step, the missing input, the capture or test that would close it, who can provide it;
- the owner-confirmed lines on the playable preview: "Feel at normal speed: play <place or link> and judge <goal>." "Listening: the key event alone, then the full mix, on a phone speaker and on headphones."
- each craft's `BAR` line (bar met, or floor only with the reason; floor only is never a blocking finding, J021-D5);
- at G1, the belief check result when the job card has one (supported / not supported / cannot tell yet, how sure, path), or "untested: no player data" with the cheapest test;
- for visible work, the grayscale, sound-off and reduced-motion checks, or each named "not verified"; a safety or comfort fault (flashes over 3 per second, an intense channel with no reduced path) blocks the gate.

**What each input can prove** (so no check claims more than its input shows):
| Input | Shows | Cannot show |
| --- | --- | --- |
| Spec, contract, config | values, names, ranges | any read on screen |
| One still or capture | one moment: read order, value, composition, silhouette | timing, sound, repetition, cost |
| Frame folder at a known rate | timing, order of events, onsets | sound, feel at speed |
| Studio Output-log times | scheduled cue times on one clock | heard sync on a device |
| Studio play capture | behaviour in the build | phone performance |
| Real phone run at the expected player count | performance, heat, input feel on touch | taste |
| Playable preview judged by the owner | feel at normal speed, listening | (owner-confirmed) |

## 3. Options and the pick (what the direction stage brings to G1)
- Research first: the game's own anchors and approved images, then real-world reference per aspect (material, pose, place, phenomenon), one source from outside games, chosen from the job's target-experience sentence (which field already makes people feel, do or believe this?); each entry says what it is for. The outside entry names the method taken, as an action that field's experts do ("hold on the reaction, withhold the creature"), not a topic ("horror films") and not only a look. Borrow a method, never a voice. The role's caps, safety, truth and platform rules win over any borrowed method; never a pressure method (false scarcity, countdowns, streaks, chance tricks).
- Hooks: each option takes its idea from a different source or reading of the theme. The first, typical idea is labelled warm-up and set aside. At least one option is radical (it changes a primary trait: silhouette, mechanism, main material, camera).
- Distinct, not variants: options differ in the big read (layout, silhouette, mechanism, camera), not in colour. Two that look alike in black-fill are one option.
- Equal finish: polish on one option makes the owner pick it for the wrong reason.
- Each option states what it adds to play and what it costs to build, and the recommended one is told as the moment the player gets (what they see, hear and do), in one or two sentences. "Looks cool" is not a reason.
- One recommendation with reasons tied to the goal; a rejection reason for each other option; polish starts only after a recorded pick.
- Each round has fewer, more specific options than the last.

## 4. Closing doors
Keep a "Closed doors" table in the job's `decisions.md`:

| ID | Date | Gate | Closed option or direction | Owner's words | Reason (goal, cost, tone, policy) | May return only if |
| --- | --- | --- | --- | --- | --- | --- |
| CD-1 | 2026-11-04 | G1 | B "neon arcade" pet shop | "too loud for a cosy farm" | tone | the owner asks for a night event |

- Write a row at every gate answer, and for options the direction synthesis dropped (its reason). Carrying the names into `avoid`, and re-proposing only with new owner words cited in the brief: SKILL §1 step 5 and §8. Filing at close: SKILL §9 step 5.

Screening aid: for each closed name, `grep -rn -i "<closed name>" knowledge/jobs/<job-id>/` lists every mention. Read only the files written after the gate: the door's own `decisions.md` row, the gate packet and the proposals written before the gate are history. In the later files, a mention on an `avoid:` line, or in an avoid list written one item per line, is correct; any other mention is a re-proposal unless it cites new owner words. The grep misses synonyms ("cyber neon" for "neon arcade"): read each new option against the closed list.

## 5. Owner notes and repair
1. Keep the owner's words verbatim in `decisions.md`.
2. Find the problem behind the note. "Make the sword bigger" may mean "the hit does not read as landing". Write the problem in one line; tag the note goal (what the player should feel or do) or tactic (how).
3. Name the layer: gameplay read, composition, silhouette, value, light and colour, material and detail, timing, sound, finish. Big before small.
4. "Not happy" may mean "not done": check the stage. A G1 option is a picture of the direction, not the build; a G3 build has no temp cue left unless the packet names it as a stand-in. Say so before you reopen anything.
5. One named problem per repair brief, worst first, with what must not change (the identity anchor, the approved silhouette, the timing beats) in its `protected`. The fix is accepted when the problem is gone in the same capture, not when the suggested change was made; after the fix, the other layers are checked again.
6. Name the door it reopens. A G3 note that moves a G1 decision (a timing beat, the layout in the agreed plan) reopens that gate's work: list the outputs that go stale and the cost, and offer the follow-up (next update) when the change is structural. The owner chooses `repair` or follow-up.
7. Route the note in the craft's terms, next to the owner's words: visual notes as a marked capture or a paint-over of the same capture (`art-review/references/feedback-briefs.md` §6); sound notes as a term with a direction ("shorter attack", "longer tail", "less low end").
8. Conflicting notes are never averaged. Owner vs reviewer: the owner's note stands; when the reviewer has evidence that the note breaks the goal, a safety or comfort rule or a platform rule, put both readings at the same camera in the digest and let the owner choose. Two reviewers: the decision owner decides (`rules/company.md` §3); a tie where every option meets the goal stays with the decision owner, unless it is a gate pick (the owner picks at gates).

## 6. Showing early (the plan, not roughs)
The rule is SKILL §6; this is how it runs (J024).
- Early agreement happens on the plan, not on roughs: the needs and limits tables meet the job lead's plan before G1, and the owner sees the direction and the agreed plan together at G1. No craft hands a rough to its consumers, and no check-in runs between a rough and a final; a rough stays inside the maker's own run.
- Status reports to the owner carry the newest built capture, labelled with its revision, or none, with no question unless one is due (one digest per turn).
- When the owner wants to see more often, give status pictures, not extra gates (an extra gate opens only when scope, intent, rights, spend or release risk changes: `rules/company.md` §2), unless the owner asks for a gate.

## 7. When it is done
- The job card states stop criteria per stage (the success test passing at the game camera on a phone; every acceptance check with evidence) and a budget (passes, image cap, tokens). Stop criteria have a floor (the success test) and a bar (observable signs a top professional needs; `rules/messages.md` §2). The work aims at the bar inside the budget; a missed bar is reported on the `BAR` line, never another round.
- A review round ends when it brings no new notes or only repeats them; after two repair rounds, diagnose (SKILL §7.3).
- "It would be cooler" after G1 is new scope (additions are tickets: SKILL §6).
- A structural idea at polish becomes a follow-up job or an item for the next update.
- A reference image or concept is finished as far as the next maker needs; never commission polish on a reference.
- "Done" is said only when the evidence exists (SKILL §12-13).

## 8. Worked examples
### 8.1 G1 for a pet companion in a cosy farm game (character job, L)
Four lines: problem "new players have no friend to follow around the farm"; constraints: phone first, third-person camera at about 12 studs, the shared pet rig (12 joints), art bible rev 4; target experience "companionship"; success test "at the spawn camera on a phone, a new player says the pet is theirs and friendly in one second". The art director's D1 brought 8 hooks (the first, a generic puppy, labelled warm-up), 4 roughs, one radical (a walking watering can). The grey pass dropped D: its black-fill read as the shop mascot.

Packet, top of the screen:
```text
(1) option-sheet.png: options A-C (reference images, grey beside colour, placed on a spawn-camera capture at phone size)
    Not shown: D, "its black-fill reads as the shop mascot" (art director)
(2) Which pet reads as the most loyal friend at phone size?
Shown: option-sheet.png
```
Then: (3) A fox, B watering-can sprite, C round chick, each with its play value (B's spout can point at the next crop) and cost (B needs one extra joint for the spout). (4) Recommend B: it points the way, which also teaches the farm; its weakest part: from behind, the spout can read as a tool, not a face; the alternative is C (cheapest, no new joint); A loses on cost, a tail chain the rig lacks. (6) Grayscale and phone-size reads of the images; the spawn capture MCP-verified; not verified at the game camera until the build; motion not verified (no clips yet). (7) Closes A, C, D. (8) Usage: 310 k tokens estimated, 280 k used. The owner answered "B, but less shiny"; the lead recorded B, the words, closed A, C and D, and put "less shiny" into the art brief as a problem ("the metal reads brighter than the pet's face") with its layer (value).

### 8.2 A G3 note on an effect (effect job, M)
The owner says: "the sword hit feels weak, make it bigger". The lead restates: problem "the hit does not read as landing"; tactic noted ("bigger"); layer: timing and sound first, size last. Stage check: the cue in the build is the temp cue (a named stand-in in the G3 packet), so part of "weak" is "not done". One repair brief, one problem: "the hit must read as landing on the contact frame", to the vfx-designer and sound-designer on the same marker; the approved timing beats stay (no door reopened). Acceptance: the same capture at the same camera; the owner listens on the playable preview (key event alone, then the full mix). Size stays a later option only if the read still fails.

### 8.3 A retime during build (feature job, L)
The game-designer shortens the boss slam's wind-up from 0.5 s to 0.4 s after a play-test. The lead checks it against the threat's reaction window in the feature contract (0.4 s is still inside it), has the animator publish timing list rev 6 with a change-table row, and the notice goes to the vfx-designer and sound-designer that turn; their rev 5 outputs are marked stale, not deleted. The change stays inside the window approved at G1 in the agreed plan, so it is a tuning change, not a beat change; outside that window the digest gets the change first (SKILL §5.4). The next report says "slam timing changed; VFX and sound recheck pending", not "done".
