---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J006 (build animator), owner chat 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J006 lessons: animator agent

## What worked
- Reusing earlier extracts: the paper had been extracted in J005 and ep4 read in J016, so step 2 shrank to one gap read plus three fact-checks. A CL → RR map let the fact-checker skip about 66 claims and find real traps (a non-existent marker method named in one doc page; a doc sample typo).
- Running the installed Blender headless in the fact-check (J006-T04) turned API claims into tested facts (Cycles modifier must be first; bake defaults lose constraint results; batch `keyframe_points.add` is the fast path).
- Principles written as decisions (ask / sign in the clip / source) plus one worked example per kind of object answered the owner's "principles, not one fixed recipe".

## What failed or cost too much
- Python file rewrites on Windows turned LF files into CRLF; the saved-workflow tests then failed (`meta` not parsed). Fix: write with `newline=''` or bytes; check `git diff` warnings before the gate.
- Brief id prefixes clashed with an existing register (RT01-RT33): check the target id range before naming a prefix.
- A docs-map row with a parenthetical in its first cell was not found by `context_packet.py` (exact role-name match).

## Owner corrections (word for word)
- "Animation is open-ended: base it on principles, not one fixed recipe." (J006 brief)
- "Okay, don't do the testing right now. If you're done, just go ahead and commit and push." (J006-D2)

## Open gaps for /improve
- G2 never ran: the skills are untested on a real clip. First real use should record where `animation-design` / `animation-craft` were unclear (the T06 brief in the job folder is ready to reuse).
- Unprobed: whether Blender markers survive FBX import into Roblox markers (craft C-17); `PreloadAsync` on an Animation (RA34); per-copy cost of each ambient technique (SD01); skinned-mesh instancing (SD02); constraint determinism across clients (SD07).
- Blender 5.2 not run: the keying recipe was checked on 5.1.2 only.
- AI motion tool claims (paper §11) were not fact-checked; the skills name no tool versions.
- The tools line (no built-in browser) is a proposal the owner has not confirmed.
