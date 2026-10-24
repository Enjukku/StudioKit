---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · medium · 2026-10-24

# State, UI, motion and animation playback: what to keep, switch, or write ourselves

Checked 2026-10-24. All picks are PROPOSALs for the owner (J025 G1). Labels: **[doc]** documented fact (source named), **[inf]** my inference, **[nv]** not verified. Package facts come from GitHub pages and the GitHub REST API read on 2026-10-24 (`pushed_at` is the last push, any branch). The API rate-limited me (HTTP 403) partway, so some rows say [nv]. No package source was run or benchmarked; no phone measurement exists for any package here.

Context: every game since 2026-05 uses the same five packages: DataService, signal, charm 0.10.0, janitor, Networker; UI libraries (React, ReactCharm, ripple) appear only in the older Starter-Kit/BallXPit line (`research/old-framework.md:30-37`). The `rules/packages.md` adopt test applies: maintained (release or commit in 12 months, dates written), MIT-compatible, small and readable, replaceable through one adapter, typed.

## 1. Short answer

| Layer | Pick (ranked 1) | Alternative (2) | Own module? |
| --- | --- | --- | --- |
| State (server truth + client copy) | Charm + charm-sync, pinned; server atoms are the only writers, client atoms are read-only copies | Plain Instance attributes for small per-instance flags; Reflex/Rodux not recommended | No: a thin kit adapter (~40 lines) so games call one `State` module |
| UI library | Vide 0.4.x with the first-party `vide-charm` binding; engine StyleSheet for look | Plain instances + StyleSheet for static screens; React-lua only as a fallback | Yes: screen manager (§6) |
| Motion | TweenService via one motion-table helper (already required by `ui-basics` U-13); springs: Vide's built-in or ripple | Ripple 0.10.2 as the imperative spring/tween library | Yes: motion helper, ~80-120 lines |
| Animation playback | Own module on Animator (§7) | `wrello/Animations` (20 stars) only as a code reference | Yes, ~150-200 lines |

## 2. State layer

Needs: server owns the fact; the client holds a read-only copy that UI binds to; deltas, not full state; per-player data; works with our Networker transport (`AGENTS.md` §2: one transport). Architecture rules this must satisfy: R-02 (one writer per fact; a client copy is not ownership) and R-05 (UI renders, never decides) in `.agents/skills/architecture/SKILL.md:43,46`; `ui-basics` U-07 (UI never grants).

| Candidate | Owner | Latest release / last push (checked 2026-10-24) | Licence | Types, size, deps | Server→client sync | Phone perf | Agent-friendliness [inf] | Known users |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Charm** `littensy/charm` | littensy | release v0.11.1 (Oct 2026; page shows day and month only), push 2026-10-01, repo updated 2026-10-23; 272 stars; not archived | MIT (GitHub API) | Luau + TS; core `init.luau` 28.6 KB + `system.luau` 5.2 KB (API, contents of `packages/charm/src`); reactivity built on alien-signals since 0.11.0 (release notes); no dependency list shown | **charm-sync** is in the same repo (`packages/charm-sync`, Wally `littensy/charm-sync`): delta patches, per-client signals, you fire your own remote in `server.connect` (README) | No published phone numbers. README says full sync history "comes at the cost of performance"; repo has a `benches` folder (5 files). [nv] on-device | Small API (atom, computed, effect, subscribe, batch); little training data and a breaking 0.10→0.11 change (see below) | Our own games (pinned 0.10.0). No shipped third-party game found by search [nv] |
| **Reflex** `littensy/reflex` | littensy | push 2025-12-21, 109 stars; no release listed | MIT | TS-first; also on Wally; README says its React bindings are TS-only, "no support for Luau projects" | Broadcaster not found on the README page [nv] | [nv] | Redux style: more boilerplate | [nv] |
| **Rodux** `Roblox/rodux` | Roblox | push 2026-06-30 (reason unknown), 336 stars; release date [nv] | Apache-2.0 | Luau | None built in | [nv] | Plenty of Redux training data, but action/reducer boilerplate and no replication | Older Roblox games and the Lua App [nv] |
| **Fusion state** (`Value`, `Computed`) | dphfox | v0.3-beta 2024-08-30; push 2026-02-02; 807 stars; 66 open issues | MIT | Luau; tied to Fusion's UI scope model | None | [nv] | API changed between 0.2 and 0.3 (scopes), so older examples mislead | [nv] |
| **Vide sources** | centau | 0.4.1 on 2026-07-11; push 2026-10-22 | MIT | Luau; UI-local reactive values | None | [nv] | see §3 | [nv] |
| **Attributes / ValueObjects** | Roblox | live engine feature | n/a | primitives, vectors, colours etc. only (types list `studio/properties.md:72`) | Replicate server→client automatically; `GetAttributeChangedSignal` exists (`Instance.yaml:1338`) | engine-native | Very easy | everywhere |

Evidence for the pick:
- Charm is the only candidate with atoms **and** a server→client delta sync in one maintained, MIT repo. Its repo also ships `react-charm` and `vide-charm` adapters (`packages/` listing, GitHub API 2026-10-24), so state and UI do not need glue we write.
- It keeps our rule "client state is a copy": `charm-sync` sends patches; the client side only has `addSignals`/`patch`, and UI writes nothing (README API list).
- It already runs in every current game, so there is zero migration for the games and agents already know the version (`old-framework.md:35-37`).

Footguns the owner and agents must know (all from the Charm README unless marked):
- **0.10 → 0.11 is breaking** (README migration section, release notes 2026-06): `peek()` → `untracked()`; `atom()`'s second argument is now an equality function, not an options table; `computed()` lost its second argument; effect callbacks no longer receive a cleanup argument; CharmSync became a singleton (`CharmSync.server`/`.client`); nested effects dispose with their parent. Our games pin 0.10.0. A 0.11.1 move should be its own change with the gate passing (`rules/packages.md` Rules). 0.11.1 (Oct 2026) fixes type errors for a new Luau version, so staying on 0.10.0 may hit type errors on newer Luau [nv which version].
- In Studio, `strict` and `frozen` are on by default: yielding inside an effect throws and tables passed to atoms are deep-frozen. Mutating a table in place fails in Studio, and may silently work in a published server [inf]. Write whole new tables.
- In sync, deleted keys arrive as a `None` marker; `fixArrays` (default true) must be turned off when the transport serialises arguments itself (README). Our Networker's behaviour: [nv].
- Sync is delta-compressed against the last-synced state, so a joining client needs the full snapshot first. The README describes `addSignalsToClient`; the exact join/hydrate sequence [nv], so test it.
- `charm-sync` version that pairs with `charm@0.10.0`: [nv]. The games' lock files do not list charm-sync (`old-framework.md:35-37`), so their client copy is hand-written today.

Weakest part of the pick: one maintainer, 272 stars, 11 open issues; no public on-device benchmark. Mitigation per `rules/packages.md` §5: hide it behind one kit `State` module so a swap touches one file.

**Why not the others.** Rodux: reducers and actions are the boilerplate Charm removes and it has no replication (reasoning from its README description "inspired by Redux"). Reflex: TS-first, Luau UI bindings absent (README). Fusion/Vide state: tied to a UI library, no network layer. Attributes: only for small leaf values on one instance (a door's `Open`, an NPC's `Hp` bar), because the type list is primitives only; they cost nothing and replicate for free, so keep them for world objects, not for inventories or currency.

## 3. UI library

Needs: bind to Charm atoms; list rows updated in place (`ui-basics` U-11 pooling); cleanup owned (U-12); strict types; small on phones. Look and feel already belong to the engine: the 2026 StyleSheet system gives tokens, themes, queries (screen size, input device, reduced motion, text size) and hover/press transitions with TweenInfo (`ui/styling/index.md:11-21`; `whats-new.md:37-38`, both live since 2026-05-11 and 2026-07-27). So the UI library's job is only structure and data binding.

| Candidate | Owner | Latest release / last push (2026-10-24) | Licence | Types, size, deps | Phone perf (source) | Agent-friendliness [inf] | Known users |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Vide** `centau/vide` | centau | 0.4.1 (2026-07-11), 0.4.0 (2026-01-17), 0.3.1 (2024-10-09); push 2026-10-22; 345 stars, 13 open issues | MIT | README: "fully Luau typecheckable"; Wally `centau/vide` v0.4.1, shared realm, no listed deps (wally.toml); source size [nv] | Fine-grained: a source change updates only the property that reads it (README example `Text = function() ... end`). No benchmark published (README, docs landing). [nv] on-device | Small API like Solid; **API moved in 0.4**: new `create()` syntax, old overloads deprecated in 0.4.1 (release notes), so an agent trained on 0.3 examples writes deprecated calls | Third-party tooling exists (Vigets plugin, DevForum 4760321). No named games [nv] |
| **React-lua** `jsdotlua/react-lua` (+ `react-roblox`) | jsdotlua community fork of Roblox's port | v17.2.1 (2024-12-04); push 2025-05-23; 578 stars | MIT | Port of React 17.x with Luau annotations "when possible" (README); heavy: reconciler + scheduler | Re-renders and diffs; `Bindings` skip re-render for animated values (Roblox/react-luau README). No phone number. [nv] | Most training data of any option (React), but Roact-era differences (hooks vs bindings) trip agents [inf] | Roblox's own Lua App; DevForum post 2026-07-29 says engine scripts use a port of React |
| **Roblox/react-luau** | Roblox | "read-only mirror"; 583 stars; dates [nv] | MIT | same code base as above | same | same | same |
| **Fusion** `dphfox/Fusion` | dphfox | v0.3-beta 2024-08-30 (release); push 2026-02-02; 807 stars; 66 open issues | MIT | Luau; scopes with leak warnings (release notes) | [nv] | Version split (0.2 vs 0.3) in training data | [nv] |
| **Roact** `Roblox/roact` | Roblox | **archived**; last push 2023-12-13 | Apache-2.0 | Legacy | n/a | n/a | Do not use |
| **Plain instances + StyleSheet + one small helper** | engine | live | n/a | engine-native | no library cost | no library to mis-remember; but each agent writes its own list and cleanup code | all engine UI |

Evidence for the pick:
- **Maintained test (`rules/packages.md` §2):** Vide passes (push 12 days ago). React-lua fails: latest release 2024-12-04 and last push 2025-05-23 are both more than 12 months old on 2026-10-24. Roblox's own repo is a read-only mirror.
- **Adapter exists:** `vide-charm` exports `useSignalState`/`useAtom` (same function): `Vide.source(getter())` + `Charm.listen(getter, source)` + `Vide.cleanup` (`packages/vide-charm/src/init.luau`, read 2026-10-24). That is a ~10-line file, so swapping the UI library later costs one adapter (§5 of the adopt test); `react-charm` has the same hooks for React.
- **Fits the rules:** fine-grained updates map to U-11 (update rows in place), Vide's cleanup scopes map to U-12 (one cleanup owner per screen), and the engine StyleSheet already provides the shared look, so Vide never needs a theming layer.

Weakest part: churn and thin training data. 0.4.0 and 0.4.1 deprecated earlier call forms, and a single maintainer owns it. An agent writing Vide from memory will often write React-style or 0.3-style code [inf]. Mitigation: a kit `references/vide.md` with 10-15 checked patterns (screen, list with pooled rows, button with Activated, bind an atom, cleanup), and a gate grep for deprecated forms. That reference is part of the cost of the pick.

Open risk that I could not close: whether Vide beats React-lua on phones. No source I found measures it. A 30-minute probe is cheap (`engineering-craft` `references/probes.md`): 200 rows updating at 10 Hz on the floor phone, both libraries. Per `architecture` AR-05, do not reject or accept on a desk estimate.

Fallback if the owner prefers certainty and training data over the 12-month rule: React-lua 17.2.1 with `react-charm`, accepting an out-of-policy package (needs a recorded exception in the package note). The older games already used it.

## 4. Motion: tweens and springs

Needs: motion from the game's motion table, never literals (U-13); reduced-motion variant per row; cheap on phones; springs for follow/overshoot.

| Candidate | Owner | Latest release / last push (2026-10-24) | Licence | Notes | Known users |
| --- | --- | --- | --- | --- | --- |
| **TweenService** | engine | live | n/a | The docs teach UI motion with it (`ui/animation.md:27-45`). The engine has no Spring easing style (grep of `EasingStyle.yaml` for "Spring": 0 matches, 2026-10-24). Server-side tweens replicate property changes per step; tween on the client (`performance-optimization/improve.md:502,526`) | everywhere |
| **StyleSheet transitions** | engine | live 2026-07-27 | n/a | Hover/pressed motion declared in StyleRules with TweenInfo, no script (`whats-new.md:37`) | engine |
| **Ripple** `littensy/ripple` | littensy | v0.10.2 (2026-07-18), v0.10.1 (2026-02-26), v0.10.0 (2025-12-12); 134 stars; 5 open issues | MIT | Springs (tension/friction/mass or frequency/dampingRatio), tweens (~35 easings), `createMotion` which builds both (README warns of waste); Wally `littensy/ripple` | Our Starter-Kit line |
| **Vide spring** | centau | "spring setter" added in 0.4.0 (release notes); details of the API [nv] | MIT | Free if Vide is chosen; one fewer package | [nv] |
| **Flipper** `Reselim/Flipper` | Reselim | last push 2021-11-25; 144 stars | MIT | Fails the maintained test | [nv] |
| **Spr** (Fraktality) | Fraktality | repo not reachable (HTTP 404/403) | [nv] | [nv] | [nv] |
| Community tween wrappers (Tween+, BetterTweenService, SpringV2) | single authors | DevForum 2025 to 2026 | various | Self-reported speed, no benchmarks; one reply argues a wrapper can be less efficient than TweenService itself (DevForum search results) | [nv] |

Pick: **TweenService behind one motion helper (our module)**, plus **springs only where a value follows a moving target** (camera-follow UI, draggable, a number chasing a counter). Springs come from Vide if it is chosen (check the exact API when building), else ripple 0.10.2. Reason: the engine already runs tweens natively, the StyleSheet covers hover/press with no code, and a library adds a dependency for the one thing the engine lacks.

Own module `Motion` (a data-driven helper, not a library): the motion-table row → `TweenInfo` + reduced variant.

```
Motion.play(instance, rowId, goal) -> handle   -- builds TweenInfo from the table row; reduced motion picks row.reduced
handle:cancel() ; handle.Completed             -- Janitor-friendly
Motion.setReduced(bool)                        -- one switch, reads ReducedMotionEnabled
```
Size ~80-120 lines + the data table + 4 tests (row lookup, reduced swap, cancel, unknown row errors). Risk it removes: literal durations/easings in screen scripts (a `ui-basics` §5 final-check failure) and missing reduced-motion variants. It has several users on day one (every screen), so it passes `anti-overengineering` §5.

Weakest part: springs are the one place we depend on a third party; ripple's maintenance has been steady (5 releases in 2025-2026) but it is one author.

## 5. Questions answered: strongest state + UI pair

**Proposal: Charm + charm-sync (state) with Vide + `vide-charm` (UI), engine StyleSheet for look, one `State` adapter and one `Screens` manager.** Ranking by the owner's criteria:
- *Strongest:* the only pair with a first-party binding and server delta sync, both MIT and active (pushes 2026-10-01 and 2026-10-22).
- *Fastest:* fine-grained updates avoid re-render diffing [inf from README design; not measured]. The probe in §3 settles it before it is locked.
- *Simplest for agents:* few concepts (atom, source, effect, cleanup). The cost is thin training data and recent API change, so the kit must ship checked patterns and a deprecated-call grep [inf].

Second-best pair: Charm + React-lua + react-charm (best-known by models, heavier, fails the 12-month test). Third: plain instances + StyleSheet + Charm `subscribe` callbacks (no UI library; agents hand-write list/cleanup code per game, which is the repeated work the framework removes).

## 6. UI manager: is it worth our own module?

Yes, small. No library covers it: a search of GitHub for Roblox screen/navigation managers returned 0 results on 2026-10-24 and a DevForum search showed only one-off "UI module" posts. Every game needs the same five behaviours, which agents currently rewrite per game, so it passes `anti-overengineering` §5 (many real users) and `rules/packages.md` §1 (repeated work now).

What the engine already gives (so the module stays thin):
- Layering: `ScreenGui.DisplayOrder` (`ui-basics` §3 step 3).
- Gamepad focus: `GuiService:Select`, `SelectedObject`, `AutoSelectGuiEnabled` (`GuiService.yaml:24,289,801`).
- Input routing: `InputContext.Priority` and `Sink` make a modal take input from gameplay contexts without a custom router (`input/input-action-system.md:422`; `InputContext.yaml:47,67`).
- Safe areas: `ScreenInsets` (U-01).

What the manager holds and nothing else:

| Concern | Rule |
| --- | --- |
| Registry | `id → { gui (template or instance), layer, modal, inputContext?, firstSelect? }`; data table, no logic per game |
| Layers | `Hud`, `Screen`, `Modal`, `Toast` → fixed `DisplayOrder` bands |
| Stack | open/close/back; one visible `Screen`, modals above it, HUD can hide while a `Screen` is open (a rule in the table) |
| Input | enable the screen's `InputContext` on open (Priority/Sink for modals); restore the previous on close |
| Focus | on open, `GuiService:Select(firstSelect)`; on close, reselect the opener |
| Lifetime | per-open Janitor; generation token so late server answers are dropped (U-12); respawn-safe (`ResetOnSpawn=false`) |
| Observable | the stack is a Charm atom (`Screens.top()`), so HUD and tutorials can react to it |

It must NOT hold: styling, themes (StyleSheet does), motion (Motion does), game screen content, a router DSL, or any "UI event bus" (`rules/packages.md` Rules: no frameworks for their own sake).

Minimal API (~150-220 lines + tests; estimate [inf]):
```
Screens.register(defs)                  -- the data table above
Screens.open(id, props?) -> handle      -- pushes, focuses, enables input context
Screens.close(id?) / Screens.back()
Screens.top() -> id?                    -- atom getter
Screens.isOpen(id) -> boolean
handle.janitor ; handle.alive()         -- generation token
Screens.destroyAll()                    -- player leaving / game reset
```
Tests offline: stack order, modal over screen, back, late answer dropped after close, open/close 20× leaves the janitor empty (U-S11). Studio check: focus lands and returns on gamepad (U-S02).

## 7. Animation manager (playback)

Facts that decide it (all [doc], `_api-reference/classes/Animator.yaml` and `AnimationTrack.yaml`, mirror read 2026-10-24):
- `LoadAnimation` **always creates a new track**, may hurt performance if overused; use `GetTrackByAnimationId` to find an existing one (`Animator.yaml:208-213`, `155-169`). The Humanoid/AnimationController versions are deprecated (`animation-craft` C-01).
- The Animator must be in Workspace before `LoadAnimation` (`Animator.yaml:202-204`).
- Replication: a player's own client may start tracks on its Character's Animator; NPCs and props must load and start on the server; an Animator created on the client never replicates (`Animator.yaml:217-232`; `animation-craft` C-02).
- `GetPlayingAnimationTracks` includes fading-out tracks (`Animator.yaml:128-140`).
- `AnimationTrack:GetMarkerReachedSignal`, `Priority`, `IsPlaying`, `Ended`, `DidLoop` exist (`AnimationTrack.yaml`, lines 409, 141, 48, 698, 680). Preloading goes through `ContentProvider:PreloadAsync` (`ContentProvider.yaml:21`).
- A marker or track end must never deal damage or grant (architecture R-05).

Existing modules: no widely used playback controller found. GitHub search 2026-10-24: `wrello/Animations` ("module for playing and pre-loading animations", MIT, 20 stars, push 2026-02-23), `Khaomi/Animator` (archived), `ffrostfall/crunchyroll` (98 stars; a custom animation solver, not a playback cache). None passes "known users" and "small and known". Not adopting; wrello's code is a reference only.

Own module `Anim`, a thin cache around the engine, worth writing because the pattern (load once, find by id, markers by name, clean up) is the same in every game and is where agents most often call `LoadAnimation` in a loop or leak connections:

| Concern | Rule |
| --- | --- |
| Catalog | data table `animId → { assetId, priority, looped, fadeIn, fadeOut, speed, markers? }`; the compiled content, never numbers in code |
| Cache | per Animator: `GetTrackByAnimationId` first, `LoadAnimation` once, store in a weak map; drop on `Destroying` |
| Preload | `Anim.preload(ids)` → `ContentProvider:PreloadAsync`, once per place load, with a timeout |
| Play | `play(id, opts) -> track`; reuse a playing track instead of stacking; return the track so callers can read `Length` |
| Markers | `onMarker(id, name, fn) -> disconnect`; connections owned by the module's Janitor; presentation only |
| Server vs client | the caller names the Animator (server for NPCs/props, client for own character and cosmetic crowds); the module never creates an Animator |
| Stop/destroy | `stop(id, fade)`, `destroy()` disconnects and clears |

Minimal API (~150-200 lines; estimate [inf]):
```
local a = Anim.new(animator: Animator, catalog: Catalog)
Anim.preload(ids: {string})                       -- yields; call at load
a:play(id: string, opts: {speed: number?, fade: number?, weight: number?}?) -> AnimationTrack
a:stop(id: string, fade: number?)
a:isPlaying(id: string) -> boolean
a:onMarker(id: string, marker: string, fn: () -> ()) -> () -> ()
a:destroy()
```
Tests offline are limited, because the engine objects are needed. Use fakes for the cache and catalog logic (reuse, no double-load, disconnect on destroy), and one Studio probe for markers and replication (`engineering-craft` `references/probes.md`). Risk it removes: repeated `LoadAnimation` (a documented performance warning), leaked marker connections, and priority/fade numbers scattered in scripts.

Weakest part: marker timing and replication behaviour depend on the engine; the animation craft already lists these as probe items (`animation-craft` C-02, C-15). The module stays small by not owning rigs, IK or procedural layers.

## 8. What is not in this file
- Data saving, transport and cleanup (Janitor) are covered by other J025 research files.
- Phone performance of any package: no measurement exists in my sources. The two probes worth running before locking the pair: (a) Vide vs React-lua row updates, (b) Charm sync with 50 players' atoms, on the floor phone.
- Items marked [nv]: Wally version pairing for charm/charm-sync, Reflex broadcaster, Rodux release date, Spr status, Vide source size, known games for Charm/Vide/Fusion.

## 9. Recommended next action
Owner picks at G1: (1) accept Charm + Vide + `vide-charm` + StyleSheet as the proposal, or choose the React-lua fallback with a recorded exception; (2) approve three small kit modules (`State` adapter, `Screens`, `Motion`) and one `Anim`; (3) approve two cheap probes (§8) before the build. Everything else in the existing stack stays.

## Sources (all read 2026-10-24 unless noted)
- GitHub API repos: littensy/charm, littensy/ripple, littensy/reflex, centau/vide, dphfox/Fusion, jsdotlua/react-lua, Roblox/rodux, Roblox/roact, Reselim/Flipper; GitHub API releases: centau/vide, dphfox/Fusion, jsdotlua/react-lua, littensy/ripple; GitHub pages: littensy/charm (README, releases), Roblox/react-luau, centau/vide (README, wally.toml), littensy/reflex; raw: `littensy/charm/packages/vide-charm/src/init.luau`, `packages/react-charm/src/init.luau`.
- Mirror: `knowledge/external/roblox-creator-docs/ui/styling/index.md`, `ui/animation.md`, `input/input-action-system.md`, `performance-optimization/improve.md`, `_api-reference/classes/{Animator,AnimationTrack,GuiService,InputContext,ContentProvider,Instance}.yaml`, `studio/properties.md`; `knowledge/reference/roblox/whats-new.md:34-43,93`.
- DevForum: "Luau vs. TypeScript (roblox-ts) for Production Roblox Games" (4757257, posts 2026-07-27/29); web search summaries on springs and tween wrappers (2026-10-24).
- Kit: `rules/packages.md`, `rules/anti-overengineering.md`, `.agents/skills/ui-basics/SKILL.md`, `.agents/skills/architecture/SKILL.md:43-46`, `.agents/skills/animation-craft/SKILL.md:44-45`, `knowledge/jobs/J025-base-framework/research/old-framework.md`.
