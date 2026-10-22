---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [ui-ux-designer, game-designer, feature-builder, art-director, vfx-designer, sound-designer, animator, marketing, film-director, reference-images, environment-designer, level-design, orchestrator, reviewer, qa-lead, progression-designer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# UI and UX

Game interfaces: the flow first, then the look, then motion; one system of meaning across every screen; motion with a purpose.
UI-01 to UI-05 set scope and order (flow before style, one job per element, audience and device, genre load, every screen). UI-06 to UI-08 are the UI system (rules for meaning, a thematic, familiar layouts). UI-09 and UI-10 are layout reads. UI-11 to UI-16 are motion (felt versus understood, and the five motion goals).
Related: the most important information first in `visual-hierarchy.md` (VH-01), colour roles in `light-colour.md` (LC-01, LC-02), composition in the real frame in `composition-focus.md` (CF-04), feedback in `game-design-fun.md`.
Stage 1c (DestructionSimulator cross-check) added UI-17 to UI-19 (starting motion durations, errors that say the fix, truthful counters); lines marked (DS) in UI-03, UI-05 and UI-10 come from the same check.

### UI-01 Flow first, then style, then motion; polish cannot save a bad flow
- principle: UX maps where every piece of information lives and the player's path to it with the fewest actions; UI builds the visuals on that map; motion reinforces the message and gives feedback. You cannot polish a bad design into working: functionality comes first and art and motion complement the information.
- why: A beautiful screen on a bad path still costs extra steps; effects on a confusing screen add noise, not clarity.
- apply: For every screen, write the flow first (entry, decision, steps to each item, exit) and count taps before any Figma styling. PROPOSAL default: frequent actions (equip, buy, claim) within 2 taps of the HUD [inference]. Review flow and layout as a wireframe (Figma frames or plain Studio frames) and pass it before gradients, glows or tweens; then specify motion and sound per interaction.
- check: The wireframe works on its own in a play-test; walking the flow in a capture, taps per task match the flow sheet and every extra tap has a reason; each added effect names the information it supports.
- mistake: Styling screens before the flow exists; treating motion as polish that will fix a weak layout ("you can't polish a bad design into functioning", R00d:4867-4871).
- examples:
  - R00d: UX maps information flow, UI builds shape, colour and layout, motion graphics reinforce messaging and give feedback (R00d:4559-4605, 4958-4983).
  - R00d: functionality and experience first; art and motion complement the information (R00d:4863-4885).
- roblox_fit: Phone players tap with thumbs on small screens, so each extra tap and small target costs more; touch is the default input on touch devices (knowledge/external/roblox-creator-docs/input/index.md:27). Every animated element costs phone performance [unverified].
- roles: ui-ux-designer, game-designer, feature-builder, orchestrator, sound-designer, vfx-designer, art-director, reviewer
- also: process-iteration, critique-feedback
- sources: R00d-F01 (R00d:4559-4605, 4958-4983); R00d-F12 (R00d:4863-4885)

### UI-02 Each element: one thing to understand, one action it leads to
- principle: Visual design presents complex information simply, so the player understands it intuitively and can act on it.
- why: Players decide in moments; anything they must decode delays the action.
- apply: For every UI element, icon, thumbnail or HUD meter, write the one thing the player must understand and the action it leads to; remove what does not serve it.
- check: Show the capture at player size (`thumb_check.py` for icons) and state in one sentence what the player learns and does; if two reviewers say different things, simplify.
- mistake: Decoration that adds information the player cannot use [inference].
- examples:
  - R00d: logos, typography, packaging, web and game UI share this core (R00d:4609-4629).
- roblox_fit: Phone screens hold less, so simplification must be stronger than on PC [inference].
- roles: ui-ux-designer, art-director, marketing, game-designer, vfx-designer
- also: visual-hierarchy
- sources: R00d-F02 (R00d:4609-4629)

### UI-03 Design for the audience and the device: phone first
- principle: Know who plays, how they think, where and how they see the UI, and what they need when. PC, console and phone play differently, and the UI changes with them.
- why: Layout, target size and density that work with a mouse fail under a thumb on a small screen.
- apply: Each screen brief names the target devices (Roblox: phone first) and the moment each item is needed. Make separate Figma frames for phone and PC or console where the layout must change, not a scaled copy. Use ScreenInsets safe areas and adapt to the preferred input.
- apply (DS): Touch targets at least about 44 pt with clear gaps (Apple practice; Roblox gives no number), the primary action bigger; nothing important in the reserved bottom-left (thumbstick) and bottom-right (jump) zones (knowledge/external/roblox-creator-docs/ui/position-and-size.md:131-139); no hover-only information; capture at least a small phone in landscape (about 800x360), a 4:3 tablet (1024x768) and 1920x1080 [inference on sizes] (DS:gui-ui/SKILL.md:16, 26, 29).
- check: Capture the screen in Studio device emulation at a phone size and a PC size: every needed item is visible, reachable by thumb and clear of the top bar and notches.
- mistake: One PC layout scaled down for phones [inference].
- examples:
  - R00d: Fortnite's PC versus mobile interface (R00d:4631-4665).
- roblox_fit: ScreenGui.ScreenInsets keeps UI clear of the top bar and cutouts (knowledge/external/roblox-creator-docs/_includes/ui/screen-insets.md:9-13); UserInputService.PreferredInput adapts to touch, gamepad or keyboard (input/index.md:27-31); mobile input: input/mobile.md. Load `ui-basics` for the build.
- roles: ui-ux-designer, feature-builder, game-designer, marketing, qa-lead
- also: world-level-readability
- sources: R00d-F03 (R00d:4631-4665)

### UI-04 The genre sets how much UI the game needs
- principle: Information-heavy genres need robust UI that keeps a lot of information easy to reach; narrative and action games may need very little live UI.
- why: The UI load must match how much live information the player needs to decide.
- apply: In preproduction the game designer lists the information the player needs per moment; the UI designer sizes the HUD from that list. Card, tycoon and simulator games plan for many screens; obby and story games keep the HUD minimal.
- check: Count HUD elements visible during core play and map each to a listed need; remove any with none.
- mistake: A HUD sized by habit instead of by need [inference].
- examples:
  - R00d: a trading card game is "90% UI"; 4X and simulation need a lot; narrative games little (R00d:4666-4691).
- roblox_fit: On phones extra HUD covers the play view; keep it as small as the genre allows [inference].
- roles: ui-ux-designer, game-designer, art-director
- also: game-design-fun
- sources: R00d-F04 (R00d:4666-4691)

### UI-05 UI is every screen and state, not only the HUD
- principle: UI covers maps, select screens, inventories, editors, skill trees, quest windows, lore pages and popups, not only the gameplay overlay.
- why: Every screen is part of one experience; forgotten screens get built ad hoc and break consistency.
- apply: At job start, list every screen and popup the feature needs, including empty, error, loading and reward states, before designing any of them.
- apply (DS): Every button covers idle, pressed, disabled with the reason shown, loading, cooldown and error (DS:gui-ui/SKILL.md:25).
- check: Compare the screen list with the feature flow; any screen or state reached in a play-test but missing from the list is a finding.
- mistake: Designing only the HUD and improvising the rest [inference].
- examples:
  - R00d: maps, select screens, inventories, editors, skill trees, quest windows (R00d:4693-4709).
- roblox_fit: In-world UI (BillboardGui, SurfaceGui) belongs to the same list (knowledge/external/roblox-creator-docs/ui/in-experience-containers.md:18, 95).
- roles: ui-ux-designer, game-designer, orchestrator, feature-builder
- also: game-design-fun
- sources: R00d-F05 (R00d:4693-4709)

### UI-06 One UI ecosystem with written rules for meaning
- principle: The UI is one ecosystem for the whole game: a shared flow and written rules for what each colour, text style and screen position means. Everything affects everything else.
- why: Consistent meaning lets the player learn the code once; an inconsistent colour or position sends a false signal.
- apply: A UI rule sheet in the art bible: colour roles (currency, danger, rarity, confirm, cancel), text styles per level, fixed screen zones per information type. Figma shared components; Roblox style tokens. VFX and in-world markers reuse the same colour roles.
- check: Sample colours of every button and label in captures and compare with the role table: a colour used for two meanings, or one meaning shown in two colours, fails; the same information type sits in the same zone on every screen.
- mistake: Each screen choosing its own colours and positions [inference].
- examples:
  - R00d: "there needs to be rules for the meaning behind different colors, text, position on screen" (R00d:4711-4737, 4969-4973).
- roblox_fit: Roblox UI styling supports tokens and themes as global variables (knowledge/external/roblox-creator-docs/ui/styling/index.md:11-19).
- roles: ui-ux-designer, art-director, vfx-designer, feature-builder, environment-designer, reviewer
- also: style-identity, light-colour
- sources: R00d-F06 (R00d:4711-4737, 4969-4973)

### UI-07 A core thematic first, then explicit style rules
- principle: Start a UI design from one core thematic, then set specific rules for typography, iconography, colour, shape language and motion; every visual decision serves the thematic.
- why: A thematic gives one test for every choice and makes the UI feel like the game's world.
- apply: The art director states the UI thematic in one line in the art bible (a material or world motif); reference-images makes UI mood frames from it; the UI designer derives the five rule groups (type, icons, colour, shape, motion) and the Figma style book from them, choosing among the kit's UI style skills.
- check: For each new UI piece, name the thematic rule it follows; review it side by side with the anchor UI frame at player size.
- mistake: Generic UI that could belong to any game [inference].
- examples:
  - R00d: the League client update built around "hextech magic" (R00d:4739-4777).
- roblox_fit: The kit's style books (`ui-style-cartoon`, `ui-style-anime`, `ui-style-pixel`, `ui-style-stud`) are rule sets of this kind; the thematic chooses among them [inference].
- roles: ui-ux-designer, art-director, reference-images, marketing, vfx-designer
- also: style-identity
- sources: R00d-F07 (R00d:4739-4777)

### UI-08 Familiar first, creative second
- principle: There is no single right layout; balance familiarity with creative arrangement. Core controls stay where players expect them; creativity goes into style and secondary screens.
- why: Familiar placement uses habits the player already has; creativity gives identity.
- apply: Keep genre conventions for core controls (shop, inventory, jump, currency); spend creativity on style and secondary screens.
- check: Compare the layout with two or three successful games in the genre; any departure for a core control has a written reason.
- mistake: Novel placement of core controls that players cannot find [inference].
- examples:
  - R00d: layout as an open-ended puzzle (R00d:4787-4791, 4833-4839).
- roblox_fit: Roblox core UI already occupies the top bar; game UI must work around it (knowledge/external/roblox-creator-docs/_includes/ui/screen-insets.md:9-13).
- roles: ui-ux-designer, art-director
- also: game-design-fun
- sources: R00d-F10 (R00d:4787-4791, 4833-4839)

### UI-09 Proximity creates meaning
- principle: The brain links elements that sit together: what is placed next to what tells the player how they relate.
- why: A bar next to an enemy name reads as that enemy's health; a counter next to a bar reads as progress.
- apply: Place every value next to the thing it describes (health over the unit, cost on the buy button, timer on the objective); keep unrelated elements apart with clear spacing.
- check: In a capture, cover the labels and ask what each bar or number belongs to; if the nearest object is the wrong one, move it.
- mistake: A value near the wrong object, creating a false link [inference].
- examples:
  - R00d: a bar next to an enemy name is its health; an XP counter next to a bar reads "far from level 6" (R00d:4792-4813).
- roblox_fit: A BillboardGui keeps a bar attached to its world unit (knowledge/external/roblox-creator-docs/ui/in-experience-containers.md:95); with many players and effects, keep these short and close.
- roles: ui-ux-designer, vfx-designer, game-designer, feature-builder, level-design
- also: visual-hierarchy, composition-focus
- sources: R00d-F08 (R00d:4792-4813)

### UI-10 Layout sets reading speed: critical information in fixed, prominent places
- principle: Layout decides how fast the player finds information, and games often need critical information in a glance.
- why: In action the player only glances at the UI; what is not found then is missed.
- apply: Rank HUD information by urgency; put the most critical items in fixed, prominent positions near the play focus and less urgent items at the edges or in menus. PROPOSAL default: critical state (health, ability ready, objective) readable in under 1 second [inference].
- apply (DS): A panel reads in a fixed order: header, main content, details, one primary action, secondary actions, close (DS:gui-ui/SKILL.md:21).
- check: Show a phone-size capture for about 1 second and ask what the health, ability state and objective are; a miss means a layout change.
- mistake: Critical information buried among secondary information [inference].
- examples:
  - R00d: a live esports cast as the fast-reading case (R00d:4814-4821).
- roblox_fit: Thumbs cover the bottom corners on phones; critical information must not sit under the touch controls [inference].
- roles: ui-ux-designer, game-designer, qa-lead
- also: visual-hierarchy
- sources: R00d-F09 (R00d:4814-4821)

### UI-11 The static state explains; motion and sound make it felt
- principle: Visual design aims for the message to be understood; motion aims for it to be felt.
- why: Movement adds weight and emotion to a state change (a reward, an error, a level up).
- apply: For each UI event specify both: the static state that tells (label, icon, colour) and the motion plus sound that makes it felt (scale pop, shake, glow).
- check: Mute and freeze: the static frame alone explains the event; then play it: the motion matches the intended feeling.
- mistake: Events explained only by motion, or felt by nothing [inference].
- examples:
  - R00d: UI is "always moving, and changing, and updating" (R00d:4840-4861).
- roblox_fit: UI motion uses TweenService on position, size, rotation, transparency, colour and stroke (knowledge/external/roblox-creator-docs/ui/animation.md:19-251).
- roles: ui-ux-designer, vfx-designer, animator, sound-designer
- also: game-design-fun, vfx-reads-timing
- sources: R00d-F11 (R00d:4840-4861)

### UI-12 Motion goal: responsiveness
- principle: Interactions are fast; tapping feels fluid and effortless.
- why: A delay between tap and response makes the UI feel broken or laggy.
- apply: Every button gives immediate feedback (press state, sound) on input, before any server answer. PROPOSAL defaults: press feedback on the same frame; open and close tweens about 0.1-0.25 s [inference].
- check: Frame-by-frame capture at 30 fps from the tap: feedback visible within 1-2 frames; count tween frames against the motion table.
- mistake: Long transitions that block input [inference].
- examples:
  - R00d: goal one of five (R00d:4893-4901).
- roblox_fit: Show client-side feedback at once and keep the server authoritative for the result [inference].
- roles: ui-ux-designer, feature-builder, sound-designer, qa-lead
- also: weight-timing, game-design-fun
- sources: R00d-F13 (R00d:4893-4901)

### UI-13 Motion goal: intention, one attention motion at a time
- principle: Motion leads focus to the key action or pathway when needed.
- why: Movement draws the eye first; use it to point, not to decorate.
- apply: Animate only the element the player should act on now (pulse the claim button, slide in the next step); keep the others still.
- check: In a capture with motion, the moving element is the intended next action; count animated elements per screen (PROPOSAL default: one attention motion at a time [inference]).
- mistake: Everything moving at once, so nothing leads [inference].
- examples:
  - R00d: goal two (R00d:4903-4907).
- roblox_fit: No change.
- roles: ui-ux-designer, vfx-designer, game-designer
- also: composition-focus, visual-hierarchy
- sources: R00d-F14 (R00d:4903-4907)

### UI-14 Motion goal: awareness, from the source to the destination
- principle: Elements appear from and return to where they relate.
- why: Motion that starts at the source shows the player where something came from and where it went.
- apply: Popups grow from the button that opened them; rewards fly to the counter they increase. Specify the start and end anchor of each tween.
- check: Frame captures: the first frame starts at the source element and the last frame ends at the destination.
- mistake: Popups that appear from nowhere [inference].
- examples:
  - R00d: goal three (R00d:4909-4913).
- roblox_fit: Use AnchorPoint and positions to set the start point [unverified].
- roles: ui-ux-designer, feature-builder, vfx-designer
- also: composition-focus
- sources: R00d-F15 (R00d:4909-4913)

### UI-15 Motion goal: consistency, one motion table
- principle: Each element type and action uses a repeated motion pattern so behaviour becomes familiar.
- why: The player learns the motion meaning once ("this slides in = notification").
- apply: A short motion table per element type (button press, popup open, toast, reward) with easing and duration, kept in shared data; every screen reuses it.
- check: Compare tween parameters across screens in code or data: different values for the same element type fail.
- mistake: Each screen inventing its own transitions [inference].
- examples:
  - R00d: goal four (R00d:4915-4921).
- roblox_fit: Easing style is set per tween (default Quad) (knowledge/external/roblox-creator-docs/ui/animation.md:406-412); keep it in shared data, not per script.
- roles: ui-ux-designer, feature-builder, vfx-designer, reviewer
- also: style-identity, pipeline-production
- sources: R00d-F16 (R00d:4915-4921)

### UI-16 Motion goal: a physical material that carries the brand
- principle: UI movement obeys a material and scale (friction, weight) that fits the game's brand; the motion style tells the tone before anything is read.
- why: Movement like paper, metal or something huge sets the feeling instantly.
- apply: Choose one motion "material" per game or event in the art bible (light paper flutter, heavy metal slam, grand parallax) and apply it to UI, login and title screens; parallax layers for big moments.
- check: Watch the transition and name the material it suggests; it matches the art bible line.
- mistake: Generic linear tweens that fit no brand [inference].
- examples:
  - R00d: Enter the Gungeon's Ammonomicon opened by a bullet; a Rift Rivals login that moves like paper; a World Championship login with sweeping parallax (R00d:4923-4949).
- roblox_fit: Easing styles (Back, Elastic, Bounce) give a material feel (knowledge/external/roblox-creator-docs/ui/animation.md:406-474).
- roles: ui-ux-designer, animator, vfx-designer, marketing, film-director, art-director
- also: style-identity, weight-timing
- sources: R00d-F17 (R00d:4923-4949)

### UI-17 Seed the motion table with tested durations
- principle: UI motion feels instant under about 100 ms, deliberate at 200-300 ms for a major change and slow at about 500 ms. A press responds on the press, the same way on every button; things leave faster than they arrive.
- why: Players feel delay before they see it; uneven press timing makes buttons feel broken; slow exits block the next action.
- apply: PROPOSAL starting table [inference; DS cites Material Design and practice sources]: press sinks in about 50 ms and the input is accepted on the press; release 120-150 ms with a small overshoot; nothing over 100 ms before the first visible change. Panels and badges enter in about 225 ms and exit in about 195 ms. Toasts enter in about 225 ms, hold about 3 s plus 1 s per 10 words, exit in about 195 ms, at most 3 stacked, outside the play focus area. No bounce that delays the next tap. Write the table once in shared data (UI-15) and let every screen read it.
- check: Frame-by-frame capture at 60 fps from the tap: the first change comes within 100 ms, the same on every button; tween durations in data match the table; no exit is longer than its entrance.
- mistake: A press animation that must finish before the next tap counts; 500 ms open tweens on frequent panels; toast spam over the combat area.
- examples:
  - DS: a UI moment table for button press, purchase success, error, toast and currency change (DS:gui-ui/references/ui-effects.md:7-15).
- roblox_fit: TweenService drives UI tweens; under reduced motion set the tween time to 0 or fade instead (knowledge/external/roblox-creator-docs/production/publishing/accessibility.md:186-188).
- roles: ui-ux-designer, feature-builder, sound-designer, vfx-designer, reviewer, qa-lead
- also: rhythm, weight-timing
- sources: DS:gui-ui/references/ui-effects.md:10, 13, 15; DS:gui-ui/SKILL.md:15; DS:vfx-design/references/juice-repetition-sync.md:64, 141; DS:vfx-design/references/review.md:168

### UI-18 Errors and denials say what is wrong and how to fix it, at the control
- principle: A refused action answers on the control that was pressed: what went wrong and what the player needs ("need 40 more gold"), in text with an icon and the danger colour, never colour alone and never a joke that hides the fix. Disabled controls show their reason.
- why: A silent or vague "no" makes players retry and blame the game; a whole-screen reaction to a small error punishes the wrong thing.
- apply: On an error, shake only the control (PROPOSAL about ±4 px, 3 cycles in about 280 ms [inference]); the message appears near it and stays at least about 2 s or until the next tap; a soft, rate-limited "no" sound plays. Every disabled button states why (cost, level, cooldown) and what unlocks it. Refusals in the world (a blocked hit, a full backpack) show a "why" cue too (an icon or a short label) and a distinct, rate-limited sound, not silence.
- check: Trigger each refusal in a capture: the message names the cause and the fix; it reads in grayscale; the screen does not shake; spamming the action plays the sound at most about once per 0.5 s [inference].
- mistake: A red flash only; a whole-screen shake for a UI error; a disabled button with no reason; silent refusals.
- examples:
  - DS: a blocked hit shows a "too strong" icon and a clink, never silence; a full backpack shows FULL plus an icon and a soft, rate-limited thud per refused item (DS:vfx-design/references/moment-recipes.md:90, 139).
- roblox_fit: Tween the control's Position offset for the shake so the layout stays untouched [inference]; colour roles come from the UI rule sheet (UI-06). Sales wording stays calm for younger players ("View Item", "See Price", never "GET IT NOW"), and a declined or cancelled purchase prompt returns quietly, since a parent's spend limit can decline it for a reason the game cannot see (`platform-policy` `references/rules.md` §D, younger players row) (lead fix 2026-10-22: the binding policy rows were missing from the UI findings).
- roles: ui-ux-designer, feature-builder, sound-designer, game-designer, reviewer, qa-lead
- also: game-design-fun, light-colour
- sources: DS:gui-ui/references/ui-effects.md:12, 24; DS:gui-ui/SKILL.md:25; DS:vfx-design/references/moment-recipes.md:90, 139

### UI-19 Counters tell the truth; their animation is decoration
- principle: Animated numbers (count-ups, flying coins, "+N" labels) are a show on top of a true value. Logic and affordability use the true balance at once; the count-up is short; the final number is exact; gains are signed and spends are neutral; big numbers are abbreviated.
- why: A rolling counter that lags the real balance lets a player think they cannot afford something they can, or the reverse; long count-ups and a sound per digit tire the player.
- apply: On a confirmed change a "+N" label pops (about 150 ms), floats and fades; the counter bumps; the count-up takes at most about 600 ms [inference]; flying coins are a few representative sprites (about 20 on screen at most) on curved paths that meet at the counter, landing with a bump and a tick; ticks on the first few arrivals and one closing sound on the last; same-kind gains inside the merge window share one label (VR-24). Buttons check affordability against the true balance the moment it changes. Gains use the reward colour; spends stay neutral (red stays for danger).
- check: Buy something right after a gain, while the count-up still runs: affordability uses the new true balance; the counter's final value equals the server value; the measured count-up stays under the cap; no sound per digit.
- mistake: Rolling digits that hide the balance; a separate label per coin; red for ordinary spending.
- examples:
  - DS: a coins-to-counter recipe: burst 200 ms, flight 500 ms eased, count-up at most 600 ms, layer offsets 0, +80 and +140 ms (DS:vfx-design/references/moment-recipes.md:138).
- roblox_fit: Tween a NumberValue and write the label on Changed [inference]; the fly-to-HUD start point is the world point converted with Camera:WorldToViewportPoint, which does not account for the GUI inset (knowledge/external/roblox-creator-docs/_api-reference/classes/Camera.yaml:1308-1312).
- roles: ui-ux-designer, feature-builder, vfx-designer, sound-designer, progression-designer, reviewer, qa-lead
- also: vfx-reads-timing, game-design-fun
- sources: DS:gui-ui/references/ui-effects.md:14, 23, 25; DS:gui-ui/SKILL.md:15; DS:vfx-design/references/moment-recipes.md:137-138; DS:vfx-design/references/juice-repetition-sync.md:148
