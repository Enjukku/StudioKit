---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer marketing · claude-opus-5-5 · high · 2026-10-22

# Review: marketing books, round 4 (J018 stage 3, focused on rev3 F1)

```text
<spec>
artifact: .agents/roles/marketing.md (body) + .agents/skills/marketing-design/ + .agents/skills/marketing-craft/ (not evals/), working tree on top of df13ff4 after repair round 3, 2026-10-22; only channel-kits.md changed among the books since rev3 (file times: all other book files older than marketing-rev3-reviewer.md)
reviewer: J018 reviewer marketing (opus, high)
looked_at_first: [
  reviews/marketing-rev3-reviewer.md (F1, R1),
  marketing-craft/references/channel-kits.md read in full; every flash, frame and red mention in the role body, both SKILL.md, image-review.md, image-pipeline.md, handoffs.md and the marketing-design books (grep: the only ones are channel-kits.md:3, 27-32, 38, 43),
  vfx-craft/references/measure.md §6 (the script and its Flash bullet, including the wrong-with-no-error list); repo-wide grep for stale copies ("most flashes in any", "mean grey", "flash_pulse_vfx"): only channel-kits.md (labelled cut finder), measure.md, film-craft blender-previs.md (the partner's pointer) and the coverage files,
  my own runs (scratch mk_r4/): the CK §3 frame command and the §6 script taken from the book text by a script and run as written, frame command then counter on the folder it wrote with the fps it printed; samples: A (the rev3 4 s edit: white contact flash, 4 white flashes 2000-2400 ms, 4 full-screen red flashes 3000-3400 ms on ground 20, a fading flash), A again as MJPG .avi, B (three quarter-screen 38->200 flashes in 1 s), E (red strobe alone on ground 38), F (darker saturated red 150,0,0 strobe on black), L (letterboxed vertical 540x960 60 fps, the 16:9 band flashing 4 per s), P (a textured stripe pan with three +60-level quarter-screen flashes in 1 s), V (1080x1920 60 fps, opens on a white frame, 3 quarter-screen flashes, a cut to bright and back), G and G2 (a clean re-cut at 30 and at 29.97 fps written into the folder of an earlier edit), timing of the counter at 1080x1920
  ]   # coverage table i and the proposals rows were read after this
findings:
  - {id: R1, class: recommendation, check: "repair broke nothing else (new wrong-number path) + C3",
     where: ".agents/skills/marketing-craft/references/channel-kits.md:27 (frames folder), :32 (counter run on 'the folder the frame command wrote')",
     expected: "The flash count reads only the frames of the edit being checked",
     observed: "The counter now reads every image in the frames folder, but the frame command neither empties the folder nor asks for a new one (os.makedirs exist_ok). A re-cut or variant written into the folder of an earlier edit leaves the old frames in it: a shorter re-cut keeps the old tail, a re-cut at another rate interleaves both edits with rising times, and the counter takes all of them with no error. Before this round the count came from the frames the command itself read, so this path is new",
     evidence: "my runs: G, a clean 2 s re-cut at 30 fps into A's folder: frame command 'frames 60', counter '120 frames', onsets 2000-3700 ms, most in any 1 s 5 (a clean edit fails); G2, a clean 4 s re-cut at 29.97 fps into a copy of A's folder: '225 frames', most in any 1 s 6. In every case I built the stale frames only added onsets (a false fail, not a false pass), and the stills listed are the old edit's. Failure scenario: the owner asks for a re-cut that trims the opening; the agent re-runs both commands on the same folder, reports 'flashes FAIL 5 in 1 s' on a clean edit and sends the cutter to fix flashes that are not there",
     smallest_fix: "At :27, 'into a new, empty folder per edit and per re-cut'; at :32, 'its frame count equals the frame command's (else the folder holds another edit's frames)'"}
  - {id: R2, class: recommendation, check: "C7 (practical)",
     where: ".agents/skills/marketing-craft/references/channel-kits.md:32",
     expected: "The run cost of the counter on the common edit is known before the run",
     observed: "The counter takes about 0.18 s per 1080x1920 frame (measured on noise and on smooth frames alike), so a 60 s vertical Short at 60 fps (3,600 frames) runs about 11 min and at 30 fps about 5.5 min, past a 2 min default command timeout. The timeout is loud, so no wrong number, but the first run is lost",
     evidence: "my runs: 180 frames of V in 32.6 s; 60 smooth frames in 11.1 s",
     smallest_fix: "One clause at :32: 'a 60 s vertical edit takes several minutes: run it in the background or with a long timeout'"}
keep: [
  rev3 F1 fixed at every place it lived: the frame command no longer prints a flash count and its list is labelled 'for finding cuts', never a flash count (:29, :31); one 'Flashes' bullet points to measure.md §6 with no copy (:32); budget (:38) and 'Readable for everyone' (:43) read the counter; coverage VR-26 and table i, proposals rows (a) and the flash-counter row match,
  the counter's input contract met: the frame command's f####_<ms>ms.jpg names are read in order with times from the names (also past 9999 frames: the sort is numeric) and measure.md §6 names this input,
  the honest red line: 'not verified' unless an analyser measures it; F (a dark saturated red strobe) reads 0 on both commands, so no PASS is ever written for red,
  the first-frame warning and the cut-to-bright rule (V: no onset on the white opening frame, the frame command lists 17 ms; the cut to bright counts once, the cut back none),
  the pan warning pointing to §6's documented case,
  frames written outside the job folder (rev3 R1 fixed)
  ]
verdict: pass
</spec>
```

## Earlier findings: status

| Id | Status | Evidence |
| --- | --- | --- |
| rev3 F1 flash count from the whole-frame mean | fixed | A: counter onsets 1000, 2000, 2133, 2267, 2400, 3000, 3133, 3267, 3400, 3700, most in any 1 s 5 (fail, right; rev3's command read 4 and missed the red); same on MJPG .avi. E: frame command lists nothing, counter 3000-3400, most 4 (right; old 0). B: frame command lists nothing, counter 333, 667, 1000, most 3 (right; old 0). No stale copy of the old count in any book; the old print survives only as the labelled cut finder |
| rev3 R1 frames in the repo | fixed | CK:27 scratch folder or `output/`; only the looked-at stills go into the job folder |

## Results by check

| Check | Result | Notes |
| --- | --- | --- |
| Fix in every listed place | pass | CK:29, :31, :32, :38, :43; coverage VR-26 (line 181) and table i; proposals row (a) and the new flash-counter row; no other book mentions flashes |
| Pointer to measure.md §6, used right | pass | Run as `python flash_pulse_vfx.py <frames dir> <fps>`; reads the 10 % count, at most 3 in any 1 s, design for 2, the same rule and words as §6 and vfx-design; the §6 wrong-with-no-error cases named, not copied |
| Own runs, real input types | pass, with R1 | A, A.avi, B, E, L (letterboxed 60 fps vertical: 4, right), P (pan with +60 flashes: 3, right), V (1080x1920 60 fps: 3, right, first frame handled by the stated look) all right. Wrong with no error: a reused frames folder (R1, over-counts only in my runs); a dark saturated red (F: 0), covered by the 'not verified' red line; pans with a small lift, covered by §6 |
| Fixed list | pass | Only channel-kits.md changed among the books since rev3, plus the two job files; role frontmatter identical to df13ff4; SKILL.md 114 and 87 lines; descriptions 388 and 380 characters; CK headings identical to HEAD (no renumbering); no citations, library ids or 'Riot' in the changed body (only the required header phrase); LF only |
| Generated copies | not this round | `sync_harness.py --check` reports the whole job's roles as different; the job card runs sync before the commit |

The repair does what rev3 asked and gives right counts on every flash type rev3 used, with the one honest gap (red) stated. Both findings above are clauses; neither blocks.
