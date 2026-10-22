# Channel kits: the work for each surface

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `marketing-craft`. The facts and limits behind each step are in `marketing-design/references/discovery-promise.md` (page, video, images) and `channels.md` (video, creators, ads, events, community), with fact-check ids and read dates. Re-read the live page on the day; a value seen only in a logged-in form is "owner to confirm". Revised by J018 maker marketing · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the opening-beat check for videos (§2-3; tell, build, beat, peak, result), the brand family on the page (§1), options in the owner package (§8); after the stage 3 review (repair round 2): the §3 checks get their inputs (frames named with their time and the flash count from one command, sound onsets from the cutter's WAV, a stills budget, a "not verified" path for sync); after review round 3 (repair round 3): flashes counted with the studio's one flash counter (`vfx-craft/references/measure.md` §6) on the frame command's folder, the frame command kept for stills and cut times, frames written outside the job folder.

## 1. Game page
| Item | Work | Check |
| --- | --- | --- |
| Title | `templates/marketing/title-checklist.md` | T1-T12 |
| Description | first sentence = what the player does and why it is fun; then the loop, then what is new; relevant words used naturally, never repeated lists; genre matches | a new reader says the action back from the first sentence |
| Icon, thumbnails | `image-pipeline.md` | checklist + sheet per image; the icon, the thumbnails and the title treatment read as one family at real size (MR-26) |
| Gallery (up to 10 images or videos) | core action first, then social moment, then progression payoff, then secondary features; each item a claim id | order recorded with ids |
| Native video | §2 | |
| Badges, events | only rewards that exist; a real event or return reason | promise ledger |
| Eligibility | devices (native video not on Xbox, PlayStation, VR), age rating, regions | recorded |

## 2. Native gameplay video (Roblox page and Home RFY)
1. Capture from the shipping build: the signature moment within the first seconds, real controls, real UI. Open on one real action told as a short story: its tell, the build, the beat (a held instant of tension), the peak (the contact or the reveal) and the result, in that order; no loading, walking or logo first.
2. Allowed: real-gameplay camera work, a logo, in-game UI text, sparse factual text, catalog music without lyrics. Not allowed: outside footage, narration, voice-chat audio, lyrical music. No cinematic trailer (FD-34, FD-48).
3. Check the live upload page for length, size and format on the day (the paper could not establish them, OQ-09). 3 free uploads a month; a rejection still uses one (FD-31..32).
4. Upload and approval = owner action. Afterwards, check a live page: is it shown, where.
5. Read with the Acquisition / Engagement / Retention video annotations; label "observational".

## 3. Short video (Shorts, TikTok, Reels)
`templates/marketing/short-video-plan.md` per edit. Work order: hook from a real moment → payoff timestamp → shot list → captions (muted review) → sound and music license → platform edit → disclosure if any → share link per platform. Variants differ in one thing. Measurement names each platform's view definition (YouTube public view = first frame since 2026-08-24; engaged views separate, FS-09, FS-11). Posting and channel accounts = owner.

**Inputs for the checks below.** The input is the edit file; I see stills, so the feel at normal speed is the owner's call on the preview.
- *Frames and cuts:* step the edit into one still per frame, each named with its index and time (`f0045_1500ms.jpg`), into a folder in your scratch folder or under `output/` (git ignores it); copy only the stills you looked at into the job folder:
  ```text
  python -c "import sys,os,cv2;v,o=sys.argv[1:3];os.makedirs(o,exist_ok=True);c=cv2.VideoCapture(v);c.isOpened() or sys.exit('cannot read '+v);R=[(t,(cv2.imwrite(os.path.join(o,'f%04d_%dms.jpg'%(i,t)),f) or sys.exit('cannot write frames to '+o)) and cv2.cvtColor(f,cv2.COLOR_BGR2GRAY).mean()) for i,(k,f) in enumerate(iter(c.read,(False,None))) for t in [round(c.get(cv2.CAP_PROP_POS_MSEC))]];R or sys.exit('no frames read');J=[R[i][0] for i in range(1,len(R)) if abs(R[i][1]-R[i-1][1])>=50];print('fps',c.get(cv2.CAP_PROP_FPS),'frames',len(R),'first and last frame ms',R[0][0],R[-1][0]);print('whole-frame changes of mean grey, for finding cuts, at ms',J)" <edit.mp4> <frames dir>
  ```
  It prints the frame rate, the frame count, the first and last frame times, and every frame-to-frame change of the whole frame's mean grey of 50 levels or more (a starting value, about a fifth of the range). The list is for finding cuts and the stills to open, never a flash count: a full-screen saturated red flash on a dark shot or a white flash on a quarter of the screen moves the mean by about 40 levels and is not listed.
- *Flashes:* the studio's one flash counter is the kit tool `tools/vfx/flash_count.py` (its note: `vfx-craft/references/measure.md` §6). Run `python tools/vfx/flash_count.py <frames dir> <fps>` on the folder the frame command wrote, with the frame rate it printed (the times come from the names). Read its count over 10 % of the frame against the limit (at most 3 onsets in any 1 s, design for 2), and also its 3 % count and box workaround where §6's known-limits list says (rain or a pan past dark shapes can make the 10 % count read too low). Look at the still at every onset it lists and at every time the frame command lists; a cut from a dark to a bright shot is an onset too, and it counts. Its wrong-with-no-error cases are in §6 (a flash during a camera pan over strong light and dark shapes can read 0): in a pan, look at the stills. The first frame is its starting point, so a flash on it is no onset: an edit that opens on a bright frame gets a look at its first stills. It is a count, not a photosensitivity analyser: a saturated red flash stays "not verified" unless an analyser measures it.
- *Sound onsets:* the edit's audio as a WAV from whoever cut it, exported from the same timeline start with the music muted (or the game-sound stem), plus the full mix as a second WAV. The kit cannot take the sound out of a video file (no ffmpeg), so without the WAV every sound line is "not verified".
  ```text
  python -c "import sys,soundfile as s,numpy as n;a,r=s.read(sys.argv[1],always_2d=True);a=a.mean(1);w=max(1,r//200);m=len(a)//w;e=10*n.log10((a[:m*w].reshape(m,w)**2).mean(1)+1e-12);C=[round(k*w*1000/r) for k in range(10,m) if e[k]>=-30 and e[k]-e[k-10:k].min()>=12];print('length ms',round(len(a)*1000/r),'onsets ms',[t for i,t in enumerate(C) if i==0 or t-C[i-1]>100])" <edit.wav>
  ```
  It prints the WAV's length and every time the sound jumps 12 dB or more above the quietest point of the 50 ms before it (5 ms steps). The length must equal the video's (last frame time plus one frame, within one frame): otherwise the WAV is not from the same timeline and the sync line is "not verified". Music moves or hides onsets with no error (a music beat on the contact frame reads as a perfect hit), so sync is read only on the WAV without music.
- *Budget:* every frame is written, but I look at about 12 stills per edit: 2-3 around each beat of the opening action and around each hit I check, plus the still at each flash onset the counter lists and at each time the frame command lists. The numbers cover the rest.

- **Opening-beat check** (the stills around the opening action; times from their names): list the start time of the tell, build, beat, peak and result of the opening action; the peak lands inside the first seconds the plan names; a re-cut keeps the beat before the peak (a trimmed beat makes the hit arrive unannounced); the result starts after its cause, never with it; the gaps between beats are not all equal; the clip's hero is the launched thing and is the clearest shape on the peak frame.
- **Character and brand in motion** (the edit's key frames among the stills; the owner judges the feel on the preview): a character's run, idle or attack in the edit is its own (its personality reads, not a shared generic move); a skin or event variant is shown through its re-themed ability, not only its costume; a premium item is shown with its secondary motion (it reads as more valuable than its siblings, never less); the game's signature sounds stay in the mix; title cards move in the game's UI motion style.
- **Sound stays in sync** (the onsets of the WAV without music; each hit's contact frame time from the stills): keep the game audio as captured; each checked hit has one onset from 17 ms before its contact frame's time to about 40 ms after it (the sound designer's window); a hit with no onset near it is "not verified", never PASS. Music does not mask the signature sounds: every hit onset of the WAV without music also shows in the full mix within about 10 ms. This proves the edit file only; sync on a phone is the sound designer's device check.
- **Readable for everyone:** captions carry the message muted (review muted, then with sound); no meaning in colour alone; flashes from the flash counter: at most 3 onsets over 10 % of the frame in any second (design for 2 or fewer, as the effects do); the plan holds no saturated red flash, the stills at every listed onset and change are looked at for one (a red flash on a ground of the same brightness is no onset), and the red line stays "not verified" unless an analyser measures it.

## 4. Update announcements, events, notifications
| Kind | Draft | Limits to check (V) |
| --- | --- | --- |
| Update announcement | ≤ 60 characters, names the real new thing, points to it | once per 3 days; opted-in players (FD-55..56) |
| Event | title, real start and end in the game's time zone, what players do, spawn path checked, thumbnail through the image pipeline | up to 10 ongoing or upcoming; Trending needs ≥ 1,000 RSVPs and a start within 7 days, public (FD-53..54) |
| Off-platform featuring request | the event, art per the live form; submit with a 14-day studio buffer (docs say 7) | not automatic, no feedback (FD-57..58) |
| Personalized notification | one string per variant, `category` set; no urgent or pushy wording; PolicyService-gated content only for eligible players | 13+ only; one per user per day per experience; delivery not guaranteed; 100 impressions before stats (FD-61..64) |
Posting, scheduling and sending = owner (or a tool the owner runs). The live-ops designer's calendar is the source of dates (handoffs §5).
Event names and taglines: write one pass pushed to the extreme of the event's tone and one pulled back to the brand pattern (name pattern, fonts, lock-up); the owner picks; the result keeps the series' naming pattern and changes one property.

## 5. Creator brief and outreach package
Write, never send. Fields (CR-01..08): the real promise and claim ids, target language / region / platform, why this creator (recent relevant videos, median views on comparable recent videos, audience geography), deliverables and dates, disclosure wording per platform (YouTube paid-promotion setting, TikTok commercial content setting, visible and audible in video, FS-12..14, FS-20, FS-32..33), allowed edits, usage and paid-amplification rights (tagging a brand partner on TikTok can grant ad authorization, FS-21), approval limits, measurement access (aggregate only), one share link, a bounded first deliverable, "honest reactions welcome". Minor creators: flag for the owner's legal review and an authorized adult. Fee: "written quote requested", split into production, licensing, paid amplification, agency, performance; never a guessed rate.

## 6. Roblox ads test plan
| Field | Content |
| --- | --- |
| objective | Plays (acquisition test) / Earnings (if eligible, monetization) / Engagement (beta, its own purpose only) |
| audience and targeting | All / New / Recent (≥ 10,000 players) / Lapsed (≥ 20,000 players); targeting within audience eligibility; no personalization to under-18 (FA-04..05, FA-33) |
| creatives | 16:9 images through the image pipeline; count per the live form (10 vs 25 conflict, FA-10); no fake UI, free-Robux bait or urging children to buy (FA-35, FA-37) |
| spend | budget options only (for example three sizes with what each could show and could not), total loss ceiling, duration, currency, funding; auto-reload off; no minimum asserted (FA-23) |
| measurement | analyst spec; attribution windows from the docs (FA-06); 48 h reporting delay (FA-13); label "attributed"; holdout if available; two ledgers |
| fixed after publish | payment method, goal, audience, budget type (FA-61, FA-63) |
| pause owner | named, with triggers (spend anomaly, misleading creative, moderation failure, player harm) |
All account actions (account, card, Robux conversion, publish, pause, Open Cloud key) = owner (`policy-rights.md` §6).

## 7. Community plan
Channels (few), rules, human escalation owner, AutoMod setup to test in each language (coverage unconfirmed, FS-39..41), anti-scam notice, incident log, feedback form fields (bug, category; never personal data), the in-game route for every essential. No data flow between Roblox and Discord ships without its own policy and privacy review (FA-55..57). Server creation and moderation staffing = owner.

## 7b. Ad integrations (brand deals, own merch)
Only with the owner's deal in hand: register in Ads Manager with invoicing, submit assets 5 business days ahead, `GetCampaignEligibilityAsync` gating built by the feature builder (ticket), "Ad" labels per format, fallback for ineligible players; one rejected asset voids the campaign (FA-39..43). Pricing for campaigns from 2027-01-01 is a platform charge (FA-44..48).

## 8. The owner package
One file `knowledge/jobs/<job>/marketing/package-<date>.md`:
1. The promise line and its proof (captures, claim ids).
2. Recommended assets per surface + rejected candidates with one-line reasons; sheets and checklists linked. Options are shown together at equal finish and at real size, labelled, one recommended with reasons tied to the brief; each question to the owner names the goal, never "which do you like?"; describe each image as the moment the player will have in play.
3. Channel plan: what, where, when, why this channel.
4. Tests: spec, method label, earliest read date.
5. Budget options (if any), each with loss ceiling and what it can and cannot show; default: no spend.
6. Release-gate table (seven items) with evidence and an empty decision-id column.
7. Owner actions list, in order.
8. Rollback: the current live assets and how to restore them.
9. Open questions with a recommendation and a default.
