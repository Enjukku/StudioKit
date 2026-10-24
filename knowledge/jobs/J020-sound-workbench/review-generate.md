---
type: job
scope: game
status: active
updated: 2026-10-24
source: J020-sound-workbench
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-24

# Review: soundbench step 7, `generate` (5a1b5bb), by reviewer

**Depth:** deep. The command spends the owner's paid credits and handles the owner's key. This is round 1, against the frozen revision 5a1b5bb (`git show 5a1b5bb`). The working tree has no changes under `tools/audio/` or the generate tests relative to it. No real API call was made. The key file and `ELEVENLABS_API_KEY` were not read. Every run used the builder's `FakeAPI`, my own fakes, or local loopback HTTP servers with a fake `sk_FAKE...` key. Scripts: scratchpad `rev/scen.py` (S1-S6) and `rev/redir.py` (S7). No repository file was written except this review.

**Goal questions:**
1. Can the key or a key-like value reach any file, log, stdout, stderr, traceback, URL or another host? (AGENTS.md §3.4)
2. Does every call that may have been charged get counted against the budget and recorded, including crashes, retries and gateway errors? (§3 generate row, §8 "each take's credits go into its sidecar")
3. Is round 4 always refused (J020-D7), and are takes never overwritten or lost (G-1)?
4. Is the intake change limited to PCM, and does the format fallback stop with exit 2 when the refusal wording is unknown? (§8)

Feature verb: *spend credits to get takes*. The areas weighed most: money, the secret and file safety. Areas the change cannot reach (Roblox replication, presentation, player-facing PT rows): n/a, because this is an offline Python tool with no game runtime.

```text
<spec>
artifact: tools/audio/soundbench@5a1b5bb (generate.py, __main__.py, intake.py, rank.py, card.py; tools/tests/test_soundbench_generate.py, test_soundbench_render.py)
reviewer: reviewer
looked_at_first: [git show 5a1b5bb (all code files), generate.py whole, intake.py whole, tools/keys.py read_key_file, ffmpeg._run, core.read_float32, editor-design.md §1 §3 §8, decisions D7 D9 D14, test_soundbench_generate.py fixtures]
findings:
  - {id: F1, class: blocking, where: "tools/audio/soundbench/generate.py:144-151 (urllib_send), :363-371 (_call_take), :486-509 (generate)",
     expected: "Brief harm 2 and the module docstring §5: every possible spend is counted and logged; a call that got no complete answer counts at the prediction as possibly spent",
     observed: "S2: the server answers 200 with character-cost 6, and the body read then fails (http.client.IncompleteRead, a connection cut mid-body). IncompleteRead is an http.client.HTTPException. It is not an OSError, so urllib_send does not turn it into NetworkError. It escapes _call_take and generate. Result: the paid call is in no record (spent and possibly-spent are not updated, there is no attempt row, no sidecar and no take), and generate writes no run log at all ('run logs: []'). The run log for every earlier attempt in this run is lost too. The CLI prints 'ERROR (unexpected ...)' and exits 2. Any other non-SoundbenchError raised after a paid answer has the same outcome, because the run log is written only on the normal path (:504-508).",
     evidence: "High (harm 2: a charged call with no record). Proof: scen.py S2 patches urlopen to return a 200 whose read() raises IncompleteRead. Output: 'RAISED IncompleteRead -> not a NetworkError'; 'generate RAISED IncompleteRead ; run logs: []'. Label: not verified against the real service (a tool run on fakes, reproducible)",
     smallest_fix: "In urllib_send, also catch http.client.HTTPException as NetworkError (counted as possibly spent). In generate, write the run log in a finally block, so any exception after the first call still leaves the log with spent, possibly-spent and the stop reason",
     protect: "Exit codes 0/1/2; the redaction of every text in the log; one success stays one call",
     retest: "S2: exit 2 or 1, run log present, possibly_spent_credits = 6 and one attempt with charged 'unknown'. A planted fault (remove the HTTPException mapping) must fail the new test"}
  - {id: F2, class: blocking, where: "tools/audio/soundbench/generate.py:313-341 (plan checks the take paths), :422-426 (open 'xb', _dump mode 'x'), :486-497",
     expected: "Brief harm 3: two runs of the same cue at once never lose a take; G-1: takes never overwritten; harm 2: a paid take is never discarded unlogged",
     observed: "S1: run A plans r1 (no files yet), then calls the API. While A's paid call is in flight, run B (same cue) writes takes/SFX-G-HIT.r1.t1.wav. A's answer arrives (character-cost 6) and open(take, 'xb') raises FileExistsError. A's paid audio is dropped, it gets no sidecar and no attempt record, generate raises, and no run log is written. B's file survives, so nothing is overwritten. But A's credits and A's take are gone without a record. The existence check runs at plan time only, and nothing stops a second run of the same cue",
     evidence: "High (harm 2 and 3: a paid take lost with no record). Proof: scen.py S1, where the fake send writes the colliding file. Output: 'RAISED FileExistsError ... calls made: 1  run logs: []'. Label: not verified with two real processes (the race is simulated in one process; the code path is the same)",
     smallest_fix: "Take a per-cue lock before the first call (create cue_dir/takes/.generate.lock with open mode 'x', remove it in finally; a lock that already exists is refused with exit 2 before any call). The F1 finally block keeps the log on any other write error",
     protect: "Never overwrite (mode 'x' stays); refusal before any call when the lock exists; a stale lock after a crash names its file in the refusal",
     retest: "S1 with the lock: the second run is refused with exit 2 and zero calls. Kill-in-the-middle: the lock is removed by finally"}
  - {id: F3, class: blocking, where: "tools/audio/soundbench/generate.py:173-186 (attempt_record), :376-379, :386-388",
     expected: "Builder claim and docstring §5: every possible spend is counted, retries included; 'unknown' (no answer) is counted at the prediction",
     observed: "A 500/502/503/504 with no character-cost header is recorded as charged 'no' with 0 credits, and it is retried. A 504 means a gateway stopped waiting for the generator. That is the same uncertainty as the client timeout the code counts as possibly spent, and it is the brief's example 'a retry after a timeout where the server did charge'. S3 uses budget 6 (one 0.5 s call), takes 1, and the answers 504, 504, 200. Result: 3 calls are made, spent 6, possibly 0, exit 0. If the gateway's upstream finished and billed, 18 credits were spent against a budget of 6, and the log says 6. The same script with two network timeouts stops after one call: 'possibly 6, exit 1, stopped: budget'",
     evidence: "High (harm 2: the budget can be passed by up to (MAX_ATTEMPTS-1) x the prediction per take, with an under-reported log). Whether ElevenLabs bills on 5xx is not known. The defect is that the code's own rule is not applied to the same uncertainty. Proof: scen.py S3 output lines '504: calls=3 spent=6 possibly=0 exit=0' and 'timeout: calls=1 ... possibly=6 exit=1'. Label: not verified against the real service",
     smallest_fix: "In attempt_record, a 5xx without a character-cost header gets charged 'unknown' and counted_credits = predicted (possibly spent), like a network failure. A 429 stays 'no'",
     protect: "429 retries stay uncounted (a rate limit is refused before work); a 5xx that carries character-cost counts its header as spent",
     retest: "S3: the 504 run stops before the second attempt at budget 6 (exit 1, possibly 6). With budget 18, three calls run and possibly = 12 + spent 6"}
  - {id: F4, class: blocking, where: "tools/audio/soundbench/generate.py:452-497 (no decoder check before the first call); intake.py:46-49, :78",
     expected: "Docstring 'refusing before any call when something is wrong'; J020-D7 (3 rounds) and the owner's credits",
     observed: "S4: ffmpeg/ffprobe cannot be found, so require_ffmpeg raises SoundbenchError. generate makes all 3 calls (18 credits), and every paid take then fails intake with 'intake refused: ffmpeg not found'. All 3 move to takes/rejected/, and the exit is 1. Because rejected takes count as a used round, the next plan is round 2: a round of the cue's 3 is used up by a missing tool, and rank never sees those takes. An important round with no duration costs 6 x 55 = 330 credits. That is past the default budget, so 300 is the realistic bound for one run",
     evidence: "High (harm 2: credits and one D7 round spent on a failure that is known before any call). Proof: scen.py S4 with ffmpeg.require_ffmpeg patched to raise. Output: 'calls=3 spent=18 made=0 rejected=3 exit=1', 'next round planned: 2'. Label: not verified on a machine without ffmpeg (the patch reproduces the same SoundbenchError path)",
     smallest_fix: "In generate, after the dry-run return and before the first call, locate ffmpeg and ffprobe (ffmpeg.require_ffmpeg(); intake.ffprobe_path(...)) and refuse with SoundbenchError (exit 2). Skip the check when a test injects decode",
     protect: "--dry-run needs neither the key nor ffmpeg; the test path with an injected decode stays offline",
     retest: "S4: refused with exit 2, zero calls, no takes/ folder created"}
  - {id: F5, class: blocking, where: "tools/audio/soundbench/generate.py:290-300 (rounds_present keyed on the sound name), :320-325",
     expected: "J020-D7: 'At most 3 regenerate rounds per cue, then it goes to the owner'; spec §3: round 4 refused",
     observed: "The round is counted per sound name. The name comes from prompts.json, which the sound designer rewrites each round. S5 uses an important cue with SFX-G-HIT.r1-r3 present. Plain prompts are refused (correct). After prompts.json switches to layers [body], the plan is SFX-G-HIT.body round 1. After body r1-r3 exist, renaming the layer to body2 plans round 1 again. Each edit gives 3 more paid rounds of 6 takes on one cue, and the cue never reaches the owner",
     evidence: "Medium (an owner decision on spend can be bypassed by editing an input file; bounded by the budget per run). Proof: scen.py S5, with output 'layers [body]: rounds planned [(SFX-G-HIT.body, 1)]' and 'renamed body2: [(SFX-G-HIT.body2, 1)]'. Label: not verified (offline plan)",
     smallest_fix: "Count rounds over every take of the cue: any file matching ^<cue>(\\.<layer>)?\\.r(\\d+)\\.t, in takes/ and takes/rejected/. The next round for every sound is that maximum + 1. If the lead or architect decides that D7 counts per layer, then refuse a layer name (or a plain/layers switch) that differs from the cue's earlier rounds instead",
     protect: "Layer files keep their own names; a rejected take still uses its round",
     retest: "S5: both edits are refused with the D7 message and zero calls"}
  - {id: F6, class: recommendation, where: "tools/audio/soundbench/generate.py:140-146 (urllib_send uses the default opener)",
     expected: "AGENTS.md §3.4 and the builder's claim: the key is sent only to the API, only in its header",
     observed: "S7: the default urllib opener follows a 302 from the API URL to another host, including plain http. It re-sends the xi-api-key header there as a GET. The other host logged ('GET', 'sk_FAKEFAKEFAKEFAKEFAKE'). Over HTTPS this needs api.elevenlabs.io itself to answer with a cross-host redirect, so it is not blocking",
     evidence: "Low to medium (harm 1, needs a redirect from the real host). Proof: rev/redir.py with two loopback servers. Label: not verified against the real service",
     smallest_fix: "Build an opener whose redirect handler refuses (a subclass of HTTPRedirectHandler whose redirect_request returns None), so a 3xx comes back as a Response and stops the run with exit 2",
     retest: "redir.py: status 302 returned, and the other host receives nothing"}
  - {id: F7, class: recommendation, where: "tools/audio/soundbench/generate.py:372",
     expected: "No key-like value in any output",
     observed: "The error body is cut to 600 bytes before redaction. S6: a 400 body of 590 bytes followed by the key leaves 'sk_' + 7 key characters in the run log, because the regex needs 16 or more characters and the full key no longer matches. This needs a service that echoes the key",
     evidence: "Low (a 10-character prefix of a 51-character key). Proof: scen.py S6, 'key prefix in log: True'. Label: not verified against the real service",
     smallest_fix: "Redact the whole decoded body first, then cut it: redact(resp.body.decode('utf-8','replace'), run.key)[:600]",
     retest: "S6: the prefix is absent"}
keep:
  - "Key handling: read from ELEVENLABS_API_KEY only, sent only in the xi-api-key header; every _dump, the returned doc, every CLI print and the CLI's catch-all error print go through redact; the sidecar keeps only the named TRACE_HEADERS; tools/keys.py guarantees a one-line key, so no header-validation error can echo it (keys.py:40-43)"
  - "Budget: the whole plan (all layers summed, :464, :480) is checked before any call, and spent + possibly + prediction is checked before every attempt, including each retry and each format fallback (:355)"
  - "Network failures and 200s without a cost header are counted at the prediction as possibly spent"
  - "Round 4 is refused for an unchanged sound name, and rejected takes (including .bin) use their round"
  - "Existing take, master, sidecar and .bin paths are refused before any call; writes use mode 'x'"
  - "Format fallback fails closed: a 4xx whose body names neither the format nor (for a 403) the subscription or tier stops the run with exit 2 (:389-393, test_an_auth_error_is_not_a_format_refusal); a wrong positive only moves to the next format and ends with 'every format refused', exit 2; the received bytes, not the asked format, decide the file type"
  - "The intake change (intake.py:60) applies only when start_time is absent AND the codec starts with pcm_; an MP3 without start_time still raises KeyError and is refused, and the MP3 encoder-delay rule (:80) is unchanged; for PCM, start_s feeds only the log field, never the decode; the rate, channel and length checks still run. Checked with ffprobe on a 16-bit PCM WAV: no start_time stated, stream_info gives start_s 0.0"
  - "rank TAKE_RE / find_takes and card._take_path accept .wav takes and never the .master.wav (the regex needs .r<k>.t<n>.wav at the end; card refuses *.master.wav)"
  - "The test change in test_soundbench_render.py is legitimate: spec §8 now makes WAV the first format, so '.wav refused' encoded the old rule; the replacement keeps a non-take extension refused (.flac) and adds the master refusal, a new guard. It passes"
  - "Tests: test_soundbench_generate ran on 5a1b5bb (36 run, 1 skipped = the live test gated by SOUNDBENCH_LIVE_GENERATE, OK), including test_every_planted_fault_is_caught"
weakest_part: "F2 and F3 rest on a simulated race and an assumed gateway billing case. No two-process run and no real 5xx were observed, so their likelihood, but not their code path, is a judgement."
could_not_check:
  - {step: "Billing on 5xx and on a cut body (F1, F3 likelihood)", missing_input: "a real 5xx or truncated answer with the account counter before and after", closes_it: "the account counter delta after such an event, or ElevenLabs support's answer", who: "feature-builder (when one occurs; no forced spend)"}
  - {step: "Cost model for eleven_text_to_sound_v3 and loop: true", missing_input: "measured character-cost on v3 and on a looping request (README notes 1.0 s loop returned 1.5 s)", closes_it: "one 0.5 s call each, header vs prediction", who: "feature-builder"}
  - {step: "Format-refusal detection against the real service", missing_input: "a real refusal body (this Creator key is given every format)", closes_it: "the body from a lower-tier key, or the documented error schema", who: "feature-builder / researcher"}
  - {step: "Real-call figures (330 credits, header sum = account counter)", missing_input: "the account counter (I made no real calls)", closes_it: "owner-confirmed counter screenshot", who: "owner"}
  - {step: "Planted-fault result 7 of 7", missing_input: "a qa-lead planted-fault run; I read the in-suite planted-fault test pass (T) but planted none of my own", closes_it: "a planted fault per F1-F5 fix in the repair round", who: "feature-builder"}
verdict: fix-first
</spec>
```

Blocking: F1, F2, F3, F4, F5. Ranked by harm: F1 to F4 are money (a charged call with no record, or credits spent on a known failure), and F5 is the D7 cap. There are no key-leak findings at the blocking level: F6 and F7 are recommendations.

## Round 2: repair round 1 (69460b7), narrow re-review

> Author: reviewer · claude-opus-5-5 · medium · 2026-10-24

**Depth:** deep, re-review by the problem (V-17), against the frozen revision 69460b7. The working tree has no changes under `tools/audio/` or the soundbench tests relative to it. No real calls were made. The scenario script `rev/scen2.py` replaces `urllib.request.urlopen` and `socket.create_connection` with functions that raise, so any real network attempt would fail loudly. None did. S2 patches `generate._opener`, which is what the new code uses. S7 uses only loopback servers.

**About the builder's note on round 1 S2:** at 5a1b5bb, `urllib_send` called `urllib.request.urlopen`, and my S2 patched exactly that name. The round-1 output ("RAISED IncompleteRead") came from the patched object, so no real request was sent in round 1. The note is correct for the new code, and round 2 patches the opener.

```text
<spec>
artifact: tools/audio/soundbench@69460b7 (generate.py; tests test_soundbench_generate.py)
reviewer: reviewer
looked_at_first: [git diff 69460b7~1 69460b7 -- generate.py (whole), plan() at 69460b7, the changed orphan test]
earlier_findings:
  - {id: F1, state: fixed, retest: "S2 (opener patched): 200 + character-cost 6, body cut -> 3 attempts, each charged 'unknown' counted 6 (header cost), possibly 18, exit 2, run log written, lock released. Decode raising ImportError after a paid take: run log written (spent 6), lock released, take and sidecar kept on disk"}
  - {id: F2, state: fixed, retest: "S1: path taken during the paid call -> the paid bytes go to takes/rejected/SFX-G-HIT.r1.t1.wav with a sidecar, the run continues, spent 18, exit 1, one log, lock released. A held lock is refused before any call (exit 2)"}
  - {id: F3, state: fixed, retest: "S3: 504, 504, 200 at budget 6 -> 1 call, possibly 6, exit 1 (stopped by the budget); at budget 18 -> 3 calls, spent 6 + possibly 12, exit 0"}
  - {id: F4, state: fixed, retest: "S4: ffmpeg missing -> refused, 0 calls, no takes/ folder, no lock left; the check runs only when decode is the real intake (generate.py: 'if decode is intake.decode_take'), and the CLI path always uses the real intake"}
  - {id: F5, state: fixed, retest: "S5: plain r1-r2 then layers -> layer round 3; after body r3, renaming to body2 -> refused. cue_rounds counts rejected .keptN, .bin, layer .keptN and an orphan .json (all -> round 3); another cue's prefix (SFX-G-HITX) is not counted"}
  - {id: F6, state: fixed, retest: "redir.py: a 302 from loopback comes back as status 302, the other host receives nothing; the run stops with exit 2. A '200' HTML meta-refresh is not followed: its bytes go to rejected/ as not audio, counted at the prediction, exit 1"}
  - {id: F7, state: fixed, retest: "S6: key placed across byte 600 -> no prefix in the log"}
findings: []
changed_test: "test_an_orphan_file_uses_its_round_and_is_never_touched replaces 'an existing file is refused before spending'. This is right under the per-cue round rule (F5 fix): an orphan r1 file is evidence that round 1 started, so counting it is conservative for J020-D7 and spends nothing. The guarantee the old test protected (never overwrite) still holds: the orphan's bytes are checked unchanged, and plan() still refuses any existing path of the new round before any call"
stated_limits:
  - "A lock left by a hard kill (process killed, power loss) blocks the cue until someone deletes it. finally releases it on every exception, KeyboardInterrupt included (checked). The refusal names the file and says when to delete it"
  - "Redaction covers the key as text and the sk_ shape. A service that echoes the key in another encoding (UTF-16, checked: written as s\u0000k\u0000_..., or JSON- or percent-escaped) is not redacted. This needs the service to echo the key in an exotic form"
  - "A run stopped by the budget mid-round still uses its round with fewer takes (behaviour unchanged from rev 1; conservative for D7)"
  - "cue_rounds matches without regard to case, so a file with the cue id in other case counts (conservative; no spend)"
  - "From round 1, still open: the real-service billing on 5xx and cut bodies, the v3 and loop cost model, and the real format-refusal body"
tests: "test_soundbench_generate + test_soundbench_render on 69460b7: 71 run, 1 skipped (live), OK"
weakest_part: "The lock was checked in one process with a pre-made lock file, not with two real processes started at the same moment; open(mode 'x') being atomic on NTFS is assumed from the OS, not probed."
verdict: ready for the next review
</spec>
```
