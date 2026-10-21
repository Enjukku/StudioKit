---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J015 (lead, /build-agent film-director)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

| Lesson | What happened | Keep / avoid |
| --- | --- | --- |
| Check the job number against the folder list right before creating it | Three chats opened J013 within seconds; this job became J015 | Keep: re-list `knowledge/jobs/` at creation; the later chat renames |
| A real run finds gaps no reading finds | The G2 test found 18 skill and tool gaps (first-animatic push, honest diff, cue round trip, prop state on boards) | Keep: run the agent once on a real brief before closing |
| The lead must look at the frames, not only the review | The agent's self-review missed a near-black handoff shot (median WCAG luminance 0.0024) | Keep: lead measures key frames (`look_check.py value`) |
| Placeholder numbers in a template get copied | The tool builder put TEST VALUE lengths in the example template | Avoid: templates keep UNKNOWN; test values live in fixtures |
| Owner correction, word for word | "For now, the agent is just done. We're not going to do any testing right now. We will be doing a lot of testing with this kit in the future, making games." | Keep: close build jobs when the owner says so; collect agent mistakes from real game work |
