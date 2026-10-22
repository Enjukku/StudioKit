> Author: J018 maker architect · claude-opus-5-5 · high · 2026-10-22. Part of `architecture`: built also from the owner's Riot transcripts (J018); repair rounds 1 and 2 after the stage 3 reviews. Used when I review someone else's work: a builder's proof or wiring against my plan, the integrated proof for cost, or a craft's plan for feasibility. My own plan is checked with `SKILL.md` §6.

# Review checklist (architect)

## 1. Before I look
- Open the artifact, the captures and the logs **before** the maker's hand-back (`rules/messages.md` §6 `looked_at_first`), at the revision under review.
- Name what each input can prove. A plan or config shows values, not behaviour; one still shows one moment; a frame folder at a known rate adds timing; a device capture with audio adds sound and sync; real-phone numbers need a recipe (device, players, quality level, duration). A line whose input is missing is **not verified**, never passed.
- Ask what the maker was trying to solve before judging a fix they propose; a requested fix is a symptom until the problem behind it is named.

## 2. Lines (each names its input)
| ID | Check | Input | Pass |
| --- | --- | --- | --- |
| RV-01 | A request the server rejects shows no outcome layer, celebration or reward sound; the refusal shows its reason | qa-lead test log or the studio-operator's frame folder of a rejected request | nothing of the outcome rows appears; the refusal row does |
| RV-02 | The bystander's camera never moves, flashes or tints from another player's event; the bystander's own threat stays the strongest element near them | two-client capture (studio-operator or qa-lead multi-client run) | as stated; no capture → not verified |
| RV-03 | The cost fits the design budget at the worst case | performance-engineer's capture with its recipe (baseline device, players, quality level, minutes) | every budget row within target; Studio-only numbers stay not verified for phones |
| RV-04 | Every gameplay fact still reads in grayscale, with sound off, reduced motion on and the lowest graphics quality | studio-operator captures of the busiest moment | each threat, pickup, team, tier and outcome named from the captures |
| RV-05 | No asset id in logic (screening aid, below) | Grep over the candidate's logic folders (§3) | no hit outside data modules, or each hit explained |
| RV-06 | Event and marker names in code match the contract and the timing-list revision (screening aid, below) | Grep over the candidate's client code; the contract; the timing list | every literal name is a contract row; no "Hit" or invented names |
| RV-07 | Presentation code decides nothing: no damage, grant, hit area or state change from a marker, tween or effect | reading the presenter modules named in the contract | none found |
| RV-08 | Hit-stop runs only on the attacker's and the target's clients (bystanders only if the per-viewer column says so), pauses only the two characters' tracks and the hit's particles, and one owner per track and emitter sets the base speed back when the stop ends and on interruption; the server never waits on it | reading the presenter; the builder's offline overlap test (two stops 50 ms apart; one cut by death); a frame folder of a hit (a single hit cannot show the overlap defect) | both overlap cases end at base speed; no saved previous speed restored; server time unaffected |
| RV-09 | A frequent event at its real rate and at its burst rate keeps one label and one sound per merge window, holds its caps, and ends on the exact counter | qa-lead rate test log (100 triggers at the real rate, a burst) | as stated |
| RV-10 | Each drawn truth value is read from the same data field as the server rule | reading the presenter and the data module; the vfx-designer's truth overlay | one field, no copy |
| RV-11 | Lifecycles: connections, tasks and instances return to baseline after respawn, reset and reopen ×20 | qa-lead or performance-engineer counts (`testing` T-10, `performance` F-09) | back to baseline |
| RV-12 | Locality: the files changed match the plan's locality list; extra files have a reason | `git diff --stat` of the candidate against its base | no unexplained file |

## 3. Screening aids (Grep tool; each is a pointer to read, never a verdict)
Run once per logic folder as the Grep `path` (for example `src/server/Combat`, `src/client/Presenters`) with glob `*.{lua,luau}` (a project may hold both); do not point it at the data folders the plan names. (Excluding a data folder with glob `!**/<folder>/**` instead drops the file filter, so other file types then show up as false readings.) Never use the Grep file type `lua`: it skips `.luau` files and reports no match. In the table `\|` stands for `|` (markdown escape); type the plain bar in the pattern. Every hit is read in the code before any finding goes out.
| Aid | Pattern (Grep, glob `*.{lua,luau}`) | Finds | Known false readings | Known misses |
| --- | --- | --- | --- | --- |
| Asset ids in logic | `rbxasset(id)?://\|\b\d{7,}\b` | `rbxassetid://` strings, long numbers that may be ids | data modules inside the scanned folder (legitimate); seeds, timestamps, user ids, large constants | ids shorter than 7 digits; ids read from attributes or built from variables |
| Marker names | ``GetMarkerReachedSignal\(\s*["'`]([^"'`]+)["'`]`` (output only the match) | literal marker names in double, single or backtick quotes | an interpolated backtick name shows its template (`` `hit_{n}` ``): read the code | names passed through a table or variable (read that table instead) |
| Guessed timings | `task\.(delay\|wait)\(\s*[0-9.]+\|wait\(\s*[0-9.]+` | literal delays that may stand in for a marker or a timeline value | retry back-off around failing services; loop pacing such as `task.wait(1)` | durations in `TweenInfo.new`, constants, or data |
Run once on a synthetic sample when the aid changes (a `.luau` and a `.lua` presenter, double, single and backtick marker names, a server file with literal delays, a data module); record the run in the job's coverage or evidence file.

## 4. Findings
Format: `rules/messages.md` §6 (class, where, expected, observed, evidence, smallest fix). Each finding names the failure scenario a player would meet ("a bystander's camera shakes on every enemy hit at 12 players"), not a style preference. The review ends with `keep` (what works), a could-not-check list (the line, the missing input, the capture or test that would close it) and the verdict. A rare edge case in a screening aid is a recommendation to add to its known limits, not a blocking finding.
