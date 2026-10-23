> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-concept`. Sources: N1 §10 (hook and promise), N2 §2 (promise ledger, marketing), FR (Roblox discovery facts, fact-checked). Tags as in SKILL.md. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (tile-size first-image check, HC11-HC12).

# Hook and promise: what the title says, ordinary play must deliver

## 1. Words
| Term | Meaning | Source |
| --- | --- | --- |
| Fantasy | who the player becomes, what they do, what can change, why it matters | H2 O |
| Dramatic promise | the surprising situation, conflict or consequence that makes trying the game appealing | H3 O |
| Theme vs hook | a theme gives context; a hook gives a reason to act | H4 O |
| Signature moment | a causal sequence: visible setup → player decision → readable consequence → emotional payoff | H6 O |
| Shareable moment | a betrayal, a clever build, a reversal, a discovery or a comic reaction; not necessarily costly spectacle. Keep the ordinary inputs that make it possible | H8 O |

A one-line fantasy need not list every system, but it must not promise a different game (H5 O). Riot separates the wanted player outcome from the audience thesis and the innovation that serves it; that makes a concept testable (H1 E).

## 2. Promise ledger (with marketing)
Every title, image, thumbnail and trailer claim links to a playable feature or to an explicitly unbuilt concept. Marketing evidence may change audience assumptions; it never authorizes mechanics the team cannot deliver (N2 §2 O). House House reports trailer viewers expected reactive music before it existed, and the team then built it: a trailer can reveal an attractive promise and also create a debt the build must pay (H9 E).

| Claim id | Where shown (title, thumbnail, icon, video, description) | Promised action | Feature id that delivers it | Status (playable / planned / cut) |
| --- | --- | --- | --- | --- |

## 3. Testing the title, the image and the playable promise (O)
1. **Interpretation before preference.** Show the title or first image with no coaching. Ask: what will you be, what will you do, what happens? Record misreadings and competing readings (TS1).
2. A preference question compares appeal. It does not show understanding, play or retention (TS2).
3. Comparable variants; report audience, exposure, sample, instructions and uncertainty. No universal viewing time or response threshold exists (TS3).
4. **Promise delivery in play.** Do players do the advertised action by themselves, notice its consequence, and find a reason to continue? Record the actual time and path; never swap in a generic target (TS4-TS5).
5. Five different causes need five different fixes: weak hook · unclear controls · delayed delivery · absent payoff · shallow repetition (TS6).
6. Read acquisition and first-play behaviour together. High clicks with high first-play bounce fits a promise mismatch, but loading, device performance, audience targeting or a confusing opening can do it too. Diagnose before rewriting the game (TS7). A thumbnail test that changes who arrives is not a clean gameplay experiment (TS8).
7. **The first image at tile size.** Before a first image goes to the owner, run `python tools/art/thumb_check.py thumbnail <image> --size <WxH> --size-source "<capture id, device>" --mask <hero mask> --bottom-band <percent>` (and `icon` for a square crop, 150x150 by default). The tile size and the bottom band come from the phone capture in `knowledge/design/marketing/surfaces.md` (marketing measures it; no Roblox doc gives it): with no row there, ask marketing for it and report the tile check `not measured`, never invent a size. A concept image is a full scene, so the subject is a hero mask traced from the image and checked on its overlay (`marketing-craft/references/image-pipeline.md` §2); `--box` includes background and counts only the boxes given, so it never stands for the subject. Without a mask the subject fields say "not measured". The sheet shows the image at the size players meet it, its grayscale and the subject mask. Read it as measured, not as a click score: one clear subject (the action and the outsized object), the action readable in grayscale, nothing important in the bottom band Roblox may cover. The image is drawn from the game camera's angle, so the fantasy survives the real view; the outsized object is clearly bigger than the player (size reads as importance and threat); one message, one symbol.

## 4. Hook check (12 items, O)
PASS only with the named evidence; otherwise FAIL with a reason. A missing test is **FAIL FOR READINESS**, not proof the game is bad.
| # | Pass when |
| --- | --- |
| HC01 | The title and first image show a concrete action or curiosity without explaining the pitch |
| HC02 | The one-line promise says what the player does and why the consequence matters |
| HC03 | The signature moment is reachable in ordinary play, not only with a trailer camera or a developer command |
| HC04 | The opening playable sequence teaches the action the promise needs |
| HC05 | The repeat loop changes a decision, relationship, challenge or expression; it does not only repeat the advertisement |
| HC06 | Title, thumbnail and prototype were tested on the same target audience, or the difference is reported |
| HC07 | Acquisition, first-play bounce, qualified engagement and returning cohorts are judged separately |
| HC08 | The minimum build still supports the fantasy, including its critical visual, audio or social part |
| HC09 | The owner can name the intended tradeoff and the open risk before approving production |
| HC10 | Rights, content maturity and current platform-policy questions are resolved, or are listed as blocking release |
| HC11 | The first image is from the game camera's angle and reads at tile size: one clear subject, the action and scale readable in grayscale (`thumb_check.py` sheet attached) |
| HC12 | What things look like in the first image matches what they do in the loop (the big thing really is the goal or the threat; nothing shown that play does not have) |

## 5. Roblox discovery facts (fact-checked; recheck before launch)
Checked 2026-10-20 against the Roblox docs mirror and live pages (`knowledge/reference/game-design/fact-check-roblox.md`, RC ids). Live docs change: recheck before launch.

| Fact | Source (RC) | Use it as |
| --- | --- | --- |
| Recommended For You looks across 28 days (day 1, days 2-7, days 8-28), widened from 7 days (2026-06-15); a new game gets distribution at once, it need not wait 28 days | RC16, RC17 | design for return play, not only the first click |
| Leading signals: play-through rate, first-play bounce (negative), play days, playtime. Play-through and first-play bounce measure only the first session from Home recommendations | RC35, FR "changed since" | the first session must deliver the promise |
| Only organically acquired Recommended users count; ad-acquired users' later play never counts for ranking | RC36, RC37 | ads buy players, not ranking |
| The playtime signal caps at 60 minutes per user per game per day; it is a ranking cap, not a session limit | RC17 | no reason to stretch sessions |
| Benchmarks have no effect on ranking | RC18 | read benchmarks for diagnosis only |
| Intentional co-play days is a second-tier signal; discovery is increasingly age-aware (2026-09-11) | RC32, RC33 | friends playing together is visible to the platform |
| Roblox says overweighting early engagement had favoured eye-catching thumbnails; mismatched metadata ranks lower | RC55 | a thumbnail that lies is punished, not rewarded |
| A custom thumbnail is needed for Home recommendation impressions; giveaway or Robux-claim leads, mismatched metadata and non-unique games limit exposure | FR "changed since" | |
| Video thumbnails must show authentic gameplay; the first description sentence says what the game is; keyword stuffing can demote | RC39, RC40 | |
| Thumbnail personalization: +8.5 % average qualified play-through, up to +50 % for some games, no method given; needs 2+ active thumbnails | RC38 (partly) | a reason to test variants, not a promised lift |
| Roblox removes infringing IP and prohibits duplicative or confusingly similar content; non-unique games rank lower | RC41, RC42 | borrow loops, never expression |

## 6. Rules
- No promise in a title, thumbnail or video that ordinary play cannot deliver. Roblox thumbnail and video assets must show the real game (FR).
- Click appeal alone is not proof of a lasting loop (D9 O).
- No number from §5 is a target. Ranking signals are named so the designer knows what the platform watches, not to game them.
