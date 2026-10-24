> Author: kit-writer stand-in · claude-opus-5-5 · medium · 2026-10-24. J025 build-plan step 9. Source of every fact: the framework repo `C:\Users\Firew\Downloads\uterd\roblox-game-framework` (`contracts/*.md` incl. "Changes after freeze", `README.md`, `REQUIRES.md`, `CHANGELOG.md`, `vendor/ProfileStore/PATCHES.md`, `template/README.md`, `tools/`), J025 job folder (`knowledge/jobs/J025-base-framework/`). The contract file wins over this page; numbers marked PROPOSAL are starting values.

# Framework: use the blocks, never write base code again

The studio's base framework (`roblox-game-framework`, private, repo `Enjukku/roblox-game-framework`) gives every game saves with a session lock, checked remotes, replicated state, screens, motion, animation playback, live config, analytics, content checks and an admin panel, in Luau `--!strict`, each block with a contract, Lune specs and protected acceptance tests. A new game starts from its template and has "player joins, data loads with a session lock, a validated remote changes saved state, UI shows it, player leaves, data saves" with no new base code (J025 job card).

## 1. Rules

| ID | Rule | Why |
| --- | --- | --- |
| FW-01 | **Use the framework block before you write base code.** Saves, remotes, client state copies, screen stack, tween timing, animation tracks, live config, analytics calls, rate limits, safe amounts, applied-once ids, boot order and admin tools all have a block (§3). Base code that does one of these jobs is a review finding (`code-review` §8) | Both earlier games copy-pasted and forked the same base code (RateLimit 151 vs 98 lines; `research/games.md` P4) and fixed bugs twice |
| FW-02 | **Never edit a copied block.** `Framework/`, `vendor/`, `Framework-tools/` and the locked dev tools in a game are copies; the game gate's lock check fails on any edit. A block that is wrong or missing something: change it in the framework repo (tests first), tag, install again; until then write the game-side part in the game and record the deviation (§5) | `README.md` Install; `tools/check_lock.py` |
| FW-03 | **One way per concern.** No second transport, state library, save layer, cleanup class, signal class or Promise library next to the framework's (`rules/packages.md` "One package per concern") | `rules/packages.md`; `code-review` §8 |
| FW-04 | **The game owns its data, the block owns the mechanism.** Schema, migrations, products, message list, atoms, screens, motion rows, clips, config keys, analytics names, admin pages are game data passed in; the block never hard-codes a game fact | every contract, "Owner of each fact" |
| FW-05 | **Read the block's contract before you use it** when you need more than its card here: invariants, failure behaviour and budgets live there (`contracts/<Block>.md`) | contracts are frozen; changes only by a recorded decision |
| FW-06 | **Transport functions are passed in, never looked up.** Blocks get the generated Blink `On`/`Fire` functions from the game's systems (`contracts/README.md` rule 2) | swap point (Blink/Zap) and offline test seam |

## 2. Start, install, update, lock, require

| Task | How |
| --- | --- |
| **Start a new game** | In the framework repo: `python tools/new_game.py --name <Name> --out <path> [--ref <tag>]`. It copies `template/`, installs every block and the locked dev tools (`tools/install.py`), writes `framework.lock`, runs `rokit install` and `wally install` (network), then `python tools/gate.py --transport` in the new game. Then read the new game's `README.md` (where each part lives, "Add a second system") and fill the packages row of `knowledge/design/game-profile.md` from its last table |
| **Install or update blocks** | `python tools/install.py --game <game> --ref <tag> [--blocks Session,Net]` (framework repo). Writes `<game>/Framework/<Block>/`, `<game>/vendor/<Package>/` (only what the blocks need), `<game>/Framework-tools/<Block>/` (Net's Lune tools, outside the place tree) and `<game>/framework.lock` (ref, commit, sha256 per file). Required blocks come too; specs stay out. Update = same command with the newer tag, read `CHANGELOG.md` between the two tags, then the game gate. No tag exists yet (repo has no commit on 2026-10-24): leave `--ref` out (working tree) and re-install from the first tag |
| **Lock check** | The game gate runs `python Framework/check_lock.py .`; it fails naming each file that was edited, added or deleted. Never under `Packages/` (`wally install` wipes it) |
| **Game gate** | `python tools/gate.py` in the game: transport, format, lint, rules, types, specs, build, lock, engine list; `RESULT: PASS` or not done. After editing `net/game.blink`: `python tools/gate.py --transport` (regenerates and patches `Remotes`) |
| **Require rule** (`REQUIRES.md`) | Another block or framework code: `require("@game/<Service>/Framework/<Block>[/<File>]")`, service from `tools/placement.json` (§4 of `architecture`). Same block or folder: `./`, `../`. Vendored: `@game/ServerScriptService/vendor/ProfileStore`. Wally: `@game/ReplicatedStorage/Packages/<Name>`. Never `script.Parent...`, `game:GetService(...).X` or a variable path in framework code; the template's game code uses the same form. One string form resolves in Roblox, luau-lsp and Lune |
| **Never hand-edit** | `Framework/`, `vendor/`, `Framework-tools/`, `tools/spec`, `tools/types`, `tools/engine/jest.config.luau`, `roblox-std.yml` (locked); `Packages/`, `DevPackages/` (Wally); `src/server/Remotes.luau`, `src/shared/Remotes.luau` (generated) |
| **A new system** | A ModuleScript in `src/server/Systems/` or `src/client/Systems/`: `{ After = { ... } }`, `init` (no yield: build tables, register), `start` (connect, `Net.answer`). Steps for saved field, message, content, rules, handler, client: template `README.md` "Add a second system" |

## 3. Block index

| Block | Side | Use it for | Never instead | Contract |
| --- | --- | --- | --- | --- |
| Helpers (RateLimit, Amount, Ledger) + Types | shared | per-key rate and cooldown, NaN-safe whole amounts, applied-once ids; `Outcome`, `Reply` | `tostring(player)` rate keys, hand-written NaN checks, own receipt logs | `Helpers.md` |
| Loader | both | boot every system in `Systems/` by `After`, fail loud | hand-ordered system lists, warn-and-continue boot | `Loader.md` |
| Session | server | player saves, migrations, receipts, awards, Studio save edits | `DataStoreService`, `ProcessReceipt`, DataService, ProfileStore direct | `Session.md` |
| Net | server | checks in front of every client→server handler | raw `RemoteEvent`, `RemoteFunction`, `UnreliableRemoteEvent`, own validators | `Net.md` |
| State | both | server truth in Charm atoms, private per-player copy to its client | attributes or remotes that push tables, a second state library | `State.md` |
| Screens | client | 4 layers (Hud, Screen, Modal, Toast), back stack, gamepad focus, cleanup per open | own screen stacks, `ScreenGui.Enabled` toggles across modules | `Screens.md` |
| Motion | client | tweens from the game's motion table with a reduced variant | `TweenInfo.new` with literals in logic | `Motion.md` |
| Anim | both | one track per clip per Animator, markers by name, cleanup on Animator end | `LoadAnimation` in game code | `Anim.md` |
| Config | server | typed live config on ConfigService (defaults, limits) | `GetConfigAsync` direct, config tables edited by hand per event | `Config.md` |
| Analytics | server | AnalyticsService calls from declared name lists, budgeted | `AnalyticsService` direct | `Analytics.md` |
| ContentTests | dev (Lune) | one spec per content table: unique ids, references, ranges | own content lint tools, a content compiler (CD-5) | `ContentTests.md` |
| Admin | server (client cloned to admins) | built-in admin tools + the game's admin pages and actions | dev chat commands, Cmdr (CD-6), own admin remotes | `Admin.md` |

## 4. Contract cards (API, the rule that matters most, owners, test lanes, usage)
All contracts: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\contracts\`. Usage examples are the contracts' own, with the real require form (§2).

### 4.1 Helpers (`Helpers.md`)
- **API (8 + MAX):** `RateLimit.allowance(perSecond, burst, clock?)` → `{ take, reset, size }`; `RateLimit.cooldown(seconds, clock?)` → `{ ready, remaining, reset, size }`; `Amount.MAX` (2^53), `Amount.whole(v)`, `Amount.add(a, b)`, `Amount.isWhole(v, max?)`; `Ledger.seen(log, id)`, `Ledger.record(log, id, cap)` → new frozen array. Types: `Outcome = "done" | "denied" | "unavailable"`, `Reply = { outcome, reason? }`.
- **Rule:** every count a client sends or code computes goes through `Amount` (never NaN, inf, negative or fraction); keys are used directly (a `Player` is a key), and the creator calls `reset(key)` on the key's end.
- **Owners:** credit per key = the allowance object; `PurchaseIds`/`AwardIds` = Session (Ledger only computes). **Lanes:** Lune only.
```luau
local RateLimit = require("@game/ReplicatedStorage/Framework/Helpers/RateLimit")
local Amount = require("@game/ReplicatedStorage/Framework/Helpers/Amount")
local gifts = RateLimit.cooldown(30)                  -- a game cooldown on top of Net's rate
if not gifts.ready(player) then return { outcome = "denied", reason = "cooldown" } end
if not Amount.isWhole(count, 99) then return { outcome = "denied", reason = "bad_input" } end
-- inside a Session update fn:
local new = table.clone(old)
new.Coins = Amount.add(old.Coins, reward)             -- saturates at 2^53, never NaN
return new
```

### 4.2 Loader (`Loader.md`)
- **API (2):** `Loader.start(systemsFolder): Report`; `Loader.run(list): (Report?, Failure?)` (pure core for specs). `System = { After: { string }?, init: (() -> ())?, start: (() -> ())? }`.
- **Rule:** `init` and `start` never yield; order is topological by `After`, then by name; any failure stops the boot (server kicks every player with "This server failed to start. Please rejoin."; client shows one full-screen message, no kick).
- **Owners:** boot order = Loader; what a system needs before it = its own `After`. **Lanes:** Lune (order, cycles, yields); Studio engine (discovery L-T1); Studio multi-client (boot-failure kick L-T12, client screen L-T14).
```luau
-- src/server/Main.server.luau (Script, RunContext Server); the client entry is the same with its folder
local Loader = require("@game/ReplicatedStorage/Framework/Loader")
Loader.start(game:GetService("ServerScriptService").Server.Systems)

-- src/server/Systems/Shop.luau
local Shop = { After = { "Save" } }
function Shop.init() end                      -- build tables; no yield
function Shop.start() --[[ Net.answer(...) ]] end
return Shop
```

### 4.3 Session (`Session.md`; saves and purchases)
- **API (11):** `Session.start(def): Save<T>` (once, in a system's `init`); `Session.status(player)`; methods `get`, `wait`, `selector`, `update(player, fn)`, `award(player, awardId, fn)`, `studioReset`, `studioSet`; signals `StatusChanged(player, status)`, `Purchased(player, productId, purchaseId)`. `Definition = { store, template, version, migrations, validate, products }`. Status: `loading | ready | degraded | closing | closed`.
- **Rule:** saved data changes only through `save:update(player, fn)` (or `award`, or a product grant). `fn` gets the frozen current data, returns a new table (`table.clone` only the levels it changes) or `nil, reason`; it never yields and has no side effects; the check (can afford, owns it) sits inside `fn`. Never grant or count revenue from `Purchased` (CC-4).
- **Owners:** player data, status, receipts, award log, 120 s load timeout = Session; lock, autosave 300 s, retries, shutdown release = ProfileStore 1.0.3 (vendored, patch P-1); schema, migrations, template, `validate`, product grants = the game (`src/server/Save/Schema.luau`).
- **Lanes:** Lune on `src/Session/test/FakeWorld.luau` (every save, receipt, steal, crash, throttle and shutdown case; hard tests H-S1..H-S6 in `tests/acceptance/Session/`); Studio engine S-T17 (real DataStore, `test_` store prefix).
```luau
local Session = require("@game/ServerScriptService/Framework/Session")
local Save = {} :: { handle: Session.Save<Schema.Data>, init: () -> () }
function Save.init()
	Save.handle = Session.start({ store = "MyGame_v1", template = Schema.template, version = 1,
		migrations = { Schema.v1 }, validate = Schema.validate,
		products = { [12345] = function(d, _r) local n = table.clone(d); n.Coins += 100; return n end } })
end
-- elsewhere: Save.handle:update(player, function(old) if old.Coins < price then return nil, "not_enough_coins" end
--   local n = table.clone(old); n.Coins -= price; return n end)
```

### 4.4 Net (`Net.md`; the remote surface)
- **API (4):** `Net.guard(Remotes.SetGuard)` (once, server `init`); `Net.on(listen, policy, handler)`; `Net.answer(listen, policy, handler)` (the handler returns a `Reply`); `Net.stats()`. Both `on` and `answer` return a disconnect function. `Policy = { name, rate, burst, beforeReady }` (write `beforeReady` explicitly, CC-12). Sends call the generated `Fire`/`FireAll` directly.
- **Rule:** every client message is declared in `net/game.blink` (the schema lint enforces ranges and bounds) and handled through `Net.on`/`Net.answer` in a system's `start`. Net does steps present, ready, rate, finite numbers, valid UTF-8, size and error isolation; **the handler still does ownership, range against server state, game state and idempotency** (`networking-security` N-02 steps 4-7), and writes saves only through `Save.handle:update`.
- **Owners:** message list, types, ranges = the game's schema; decode and declared bounds = Blink + Net's patch; readiness, rate, walk, counts = Net; ownership, state, idempotency = each handler.
- **Lanes:** Lune (fake transport and the patched generated module: Net-T1..T23; hard tests in `tests/acceptance/Net/`); Studio multi-client H (Net-T12 spam and bad values, Net-T15 early events, Net-T18 bad-packet flood).
```luau
-- src/server/Systems/Coins.luau (template)
local Net = require("@game/ServerScriptService/Framework/Net")
local Remotes = require("../Remotes")              -- generated + patched Blink server module
local Coins = { After = { "Core" } }               -- Core calls Net.guard(Remotes.SetGuard) in init
function Coins.start()
	Net.answer(Remotes.CoinsCollect.On, { name = "CoinsCollect", rate = 4, burst = 8, beforeReady = false },
		function(player, sourceId)                 -- Blink checked string(1..32); the rule checks it exists
			local outcome, reason = Save.handle:update(player, function(old) return Rules.collect(old, sourceId) end)
			return { outcome = outcome, reason = reason }
		end)
end
```

### 4.5 State (`State.md`; client copies)
- **API (6):** server `State.server(atoms, send)`, `State.hydrate(player)`, `State.setPrivate(map, player, value?)`, `State.track(map, player, view)`; client `State.client(atoms, receive, hydrate)`, `State.mine(map)` → reactive getter. The game declares one shared `Atoms` module (`shared` atoms for everyone, `private` maps keyed by `tostring(UserId)`).
- **Rule:** server atoms are the only writers; a client receives only its own private entry; atoms get new tables, never in-place edits; a `track` view is pure and never yields. Small per-object flags stay Instance attributes (St8).
- **Owners:** each atom = the server system that writes it (named in `Atoms`); client copies = State; patch format = charm-sync. **Lanes:** Lune (St-T1..T10, fake transport); Studio multi-client (St-T8 bytes, St-T9 H: B never gets A's private entry).
```luau
-- src/shared/Atoms.luau: return { shared = { roundEndsAt = Charm.atom(0) }, private = { save = Charm.atom({}) } }
-- server (template Core.start):
State.server(Atoms, Remotes.Framework.StateSync.Fire)
Net.on(Remotes.Framework.StateHydrate.On, { name = "StateHydrate", rate = 1, burst = 2, beforeReady = true }, State.hydrate)
Save.handle.StatusChanged:Connect(function(player, status)
	if status == "ready" or status == "degraded" then
		local data = Save.handle:selector(player)
		State.track(Atoms.private.save, player, function() local d = data(); return if d then Schema.view(d) else nil end)
	end
end)
-- client: State.client(Atoms, Remotes.Framework.StateSync.On, function() Remotes.Framework.StateHydrate.Fire(nil) end)
```

### 4.6 Screens (`Screens.md`)
- **API (5):** `Screens.register(defs)`, `Screens.open(id, props?) → Handle { janitor, alive, close }`, `Screens.close(id)`, `Screens.back() → boolean`, `Screens.view() → () -> { top, blocking, open }`. `Def = { layer = "Hud" | "Screen" | "Modal" | "Toast", build(props, handle) → GuiObject, firstSelect?, input? }`.
- **Rule:** everything a screen creates goes in `handle.janitor`; after any yield (a server answer) check `handle.alive()` before touching the UI; gameplay systems read `view().blocking` to gate their own InputContexts (Screens never writes them). Look comes from the StyleSheet, motion from Motion: Screens holds no styling.
- **Owners:** open screens, order, `blocking` = Screens; registry = the game. **Lanes:** Lune (stack, blocking, alive, errors); Studio engine (Sc-T1 bands, Sc-T4 1,000 open/close, Sc-T7 gamepad focus, Sc-T8 ButtonB, Sc-T9 respawn).
```luau
Screens.register({ Shop = { layer = "Screen", firstSelect = "BuyButton", build = function(props, h)
	local itemId = if type(props) == "string" then props else error("Shop needs an item id")
	local root = ShopLayout.build()
	h.janitor:Add(root.BuyButton.Activated:Connect(function()
		local reply = Remotes.Buy.Invoke(itemId)           -- yields; show pending meanwhile
		if h.alive() then ShopView.show(root, reply) end   -- closed screens drop late answers
	end))
	return root
end } })
Screens.open("Shop", "sword_1")
```

### 4.7 Motion (`Motion.md`)
- **API (3):** `Motion.rows(rows)` (once, client init), `Motion.play(instance, rowId, goal, reducedGoal?) → Tween`, `Motion.reduced()`. `Row = Timing & { reduced: Timing | "instant" }`.
- **Rule:** every row names its reduced variant (the designer decides); no duration or easing literal in logic; the caller owns the Tween (put it in a janitor); a tween's `Completed` never decides gameplay (M6). Reduced = `GuiService.ReducedMotionEnabled`, read at each play.
- **Owners:** timings = the game's motion table (UI or animation craft). **Lanes:** Lune (M-T1, M-T4, M-T6); Studio engine (M-T2, M-T3, M-T5, M-T7).
```luau
-- src/shared/MotionRows.luau: annotate, then freeze (CC-2)
local Motion = require("@game/ReplicatedStorage/Framework/Motion")
local rows: { [string]: Motion.Row } = {
	toast_enter = { time = 0.25, style = Enum.EasingStyle.Back, direction = Enum.EasingDirection.Out,
		reduced = { time = 0.25, style = Enum.EasingStyle.Linear, direction = Enum.EasingDirection.Out } },
	panel_open = { time = 0.2, style = Enum.EasingStyle.Quad, direction = Enum.EasingDirection.Out, reduced = "instant" },
}
return table.freeze(rows)
-- client: Motion.rows(MotionRows); handle.janitor:Add(Motion.play(toast.UIScale, "toast_enter", { Scale = 1 }), "Cancel")
```

### 4.8 Anim (`Anim.md`)
- **API (10):** `Anim.new(animator, clips) → AnimPlayer` (`play(id, speed?)`, `stop`, `isPlaying`, `onMarker(id, marker, fn)`, `destroy`); `Anim.observe(animator, clips)` (listen to clips another side plays: `onMarker`, `destroy`); `Anim.preload(clips, ids)` (yields; call while loading). `Clip = { assetId, priority, looped, fadeIn, fadeOut, speed?, markers? }`.
- **Rule:** only Anim calls `LoadAnimation` (once per Animator and clip); marker names must be declared in `clip.markers` (a typo errors); markers drive presentation only, never damage or grants (A7); the caller picks the Animator (server's for NPCs and props, the local character's on its client).
- **Owners:** clip table = the animation craft; loaded tracks = the AnimPlayer. **Lanes:** Lune (fake); Studio engine (A-T1, A-T3, A-T6); Studio multi-client 1 client (A-T8, A-T11 observe).
```luau
local Anim = require("@game/ReplicatedStorage/Framework/Anim")
local Clips = require("@game/ReplicatedStorage/Shared/Clips")      -- game data
Players.LocalPlayer.CharacterAdded:Connect(function(character)
	local animator = character:WaitForChild("Humanoid"):WaitForChild("Animator") :: Animator
	local anim = Anim.new(animator, Clips)                           -- cleaned when the Animator is destroyed
	anim:onMarker("swing", "Contact", function() Vfx.spark(character) end)   -- presentation only
	anim:play("idle")
end)
```

### 4.9 Config (`Config.md`)
- **API (6):** `Config.start(keys)` (once, server init), `Config.number|boolean|string|json(key)`, `Config.override(key, value?)` (Studio and specs only). `Key` = number (default, min, max) | boolean | string (maxLength) | json (check).
- **Rule:** server only; reads never yield and never fail (default until the first load, default when a live value breaks its limits); never a config key for values tied to money or saves (prices bound to receipts, store names: C5). Clients see a value only through a State shared atom.
- **Owners:** live values = Creator Hub config (owner, live-ops); key list = the game. **Lanes:** Lune (fake ConfigService); Studio engine (C-T6, C-T7).
```luau
Config.start({
	coin_multiplier = { kind = "number", default = 1, min = 0, max = 10 },
	event_banner_on = { kind = "boolean", default = false },
})
local reward = Amount.whole(base * Config.number("coin_multiplier"))   -- never yields
```

### 4.10 Analytics (`Analytics.md`)
- **API (5):** `Analytics.start({ currencies (≤ 5), funnels (≤ 10), events (≤ 100) })`, `onboarding(player, step, stepName)`, `funnel(player, funnel, step, stepName, sessionId?)`, `economy(player, flow, currency, amount, endingBalance, transactionType, sku?)`, `custom(player, event, value?)`.
- **Rule:** names come only from the declared lists; log economy flows after the save update returned `done`; never user-entered text; analytics can never break gameplay (every call in `pcall`, budget `120 + 20 × players` per minute minus 10 %). What to log: `analytics` skill.
- **Owners:** name lists = the game (analytics craft). **Lanes:** Lune (An-T1..T6); Studio engine (An-T7).
```luau
Analytics.start({ currencies = { "Coins" }, funnels = { "FirstShop" }, events = { "RoundWon" } })
-- in the Buy handler, after update returned "done":
Analytics.economy(player, "Sink", "Coins", price, Save.handle:get(player).Coins,
	Enum.AnalyticsEconomyTransactionType.Shop, itemId)
Analytics.onboarding(player, 3, "OpenedShop")
Analytics.custom(player, "RoundWon")
```

### 4.11 ContentTests (`ContentTests.md`; a pattern + `Check`)
- **API (5):** `Check.unique(rows, field)`, `Check.refs(rows, field, targets)`, `Check.range(rows, field, min, max, integer?)`, `Check.each(rows, rule)`, `Check.none(problemLists)`. Each check returns problem lines; `none` fails listing all, sorted.
- **Rule:** one spec per content table, next to it (`src/shared/Content/<Table>.spec.luau`), on the real table; minimum: unique ids, every reference resolves, every number a rule reads has a range, asset ids are `rbxassetid://` or the documented empty value. A content table without its spec is a review finding.
- **Owners:** rows = the game's data files; rules = the table's spec (designer states, builder writes). **Lane:** Lune (gate).
```luau
-- src/shared/Content/Items.spec.luau
local Check = require("@game/ReplicatedStorage/Framework/ContentTests/Check")
local Items, Recipes = require("./Items"), require("./Recipes")
return { ["Items keeps its rules"] = function()
	Check.none({
		Check.unique(Items, "id"),
		Check.range(Items, "price", 0, 1e9, true),
		Check.refs(Recipes, "inputs", Items),
	})
end }
```

### 4.12 Admin (`Admin.md`)
- **API (3 server):** `Admin.start(def, Save.handle, remotes)` (once, a system's `start`), `Admin.isAdmin(player)`, `Admin.isExempt(player)` (movement checks skip while fly, noclip or a non-default speed or jump is on). `Def = { allow, group?, pages, frames?, actions, client? }`. Built-in tools (PROPOSAL list, J025-D2): fly, noclip, walk speed, jump, goto, bring, spawn, place, respawn, heal, kick (fixed reasons), info, save view; Studio only: reset own save, set a saved value.
- **Rule:** the server re-checks `isAdmin` and the value against its control on every action; Studio-only actions are locked twice (Admin and Session); the allow-list, pages, frames and the panel client stay in ServerScriptService or ServerStorage and are cloned only to admins.
- **Owners:** who is admin, exemptions, action log = Admin; pages and actions = the game (`src/admin/Pages.luau`, `src/server/AdminActions.luau`). **Lanes:** Lune (+ H in `tests/acceptance/Admin/`); Studio multi-client H (Ad-T4 non-admin refused, Ad-T8 non-admin never has the panel).
```luau
-- src/server/Systems/AdminSetup.luau (start)
Admin.start({
	allow = { 12345678 },
	pages = ServerStorage.AdminPages.Pages,   -- { { id = "eco", title = "Economy", controls = { { kind = "number",
	                                          --   id = "give_coins", label = "Give coins", min = 1, max = 1e6, integer = true } } } }
	actions = { give_coins = { target = true, run = function(_admin, value, target)
		if not target or type(value) ~= "number" then return { outcome = "denied", reason = "bad_input" } end
		return Rewards.grant(target, value)   -- Admin already checked 1..1e6, integer
	end } },
}, Save.handle, { action = Remotes.AdminAction.On, info = Remotes.AdminInfo.Fire, save = Remotes.AdminSave.Fire })
```

## 5. Deviations and gaps
- A game that skips a block or uses something else writes it in the `game-profile.md` packages row: block, what replaces it, why. A reviewer treats an unrecorded bypass as a finding (`code-review` §8).
- A block missing a feature the game needs: write the game-side part in the game's own module, record the deviation, and send a framework change request to the lead (a later framework steward agent improves blocks from games; proposal D-135). Never fork a block inside the game.
- Placement per block, ownership per fact: `architecture` §8. D-rules kept by Session: `data-saving` §5, §8. Remote checks per layer: `networking-security` §7. Test lanes: `testing` §8. Package notes: `knowledge/reference/libraries/`.
- Framework reason codes (all blocks): `not_ready`, `degraded`, `closing`, `rate`, `bad_input`, `error`, `invalid_data`, `not_admin`, `studio_only`, `unknown_action`, `no_target`; the game adds its own, snake_case, ≤ 32 chars, each with a UI line naming cause and fix.
