--!nonstrict
-- (Lune script: luau-lsp with Roblox definitions cannot resolve @lune requires, so it is not held to --!strict.)
-- P1 offline receive harness (Lune 0.11.1). Loads a generated server module with stub services
-- and real @lune/roblox datatypes, then feeds each crafted packet to the server's OnServerEvent
-- handler exactly as the engine would call it (player, buffer, instances). One line per case:
--   P1 <tool> <case> <accepted|rejected> <detail>
-- Usage (from probes/p1-transport/scratch, where rokit.toml pins lune):
--   lune run ../offline/run_receive.luau blink
--   lune run ../offline/run_receive.luau zap
-- Not engine evidence: Lune's Vector3/CFrame/Instance stand in for the engine's. The Studio
-- harness in ../runtime is the engine check.

local fs = require("@lune/fs")
local luau = require("@lune/luau")
local process = require("@lune/process")
local roblox = require("@lune/roblox")

local tool = process.args[1] or "blink"
local root = "../gen/" .. tool .. "/Server.luau"
local source = fs.readFile(root)

type Handler = (...any) -> ()

local function fakeSignal()
	local s = { fns = {} :: { Handler } }
	function s.Connect(self: any, fn: Handler)
		table.insert(self.fns, fn)
		return { Disconnect = function() end }
	end
	return s
end

local function fakeRemote(className: string)
	local r = { ClassName = className, OnServerEvent = fakeSignal(), Name = "" }
	function r.IsA(_self: any, c: string): boolean
		return c == className or c == "Instance"
	end
	function r.FireClient() end
	function r.FireAllClients() end
	return r
end

local reliable = fakeRemote("RemoteEvent")
local unreliable = fakeRemote("UnreliableRemoteEvent")
local folder = {}
function folder.FindFirstChild(_self: any, name: string): any
	if string.find(name, "UNRELIABLE", 1, true) then
		return unreliable
	end
	return reliable
end

local replicatedStorage = {}
function replicatedStorage.FindFirstChild(_self: any, name: string): any
	if name == "ZAP" then
		return folder
	end
	return folder:FindFirstChild(name)
end

local runService = { Heartbeat = fakeSignal() }
function runService.IsServer() return true end
function runService.IsClient() return false end
function runService.IsRunning() return true end
function runService.IsStudio() return true end

local players = { PlayerRemoving = fakeSignal() }
local services: { [string]: any } = {
	ReplicatedStorage = replicatedStorage,
	RunService = runService,
	Players = players,
}
local game = {}
function game.GetService(_self: any, name: string): any
	return assert(services[name], name)
end

local warnings = 0
local env: { [string]: any } = {
	game = game,
	Vector3 = roblox.Vector3,
	CFrame = roblox.CFrame,
	Instance = roblox.Instance,
	task = { spawn = function(f: Handler, ...: any) f(...) end },
	warn = function() warnings += 1 end,
	_G = {},
	assert = assert, error = error, pcall = pcall, print = print, typeof = typeof, type = type,
	tostring = tostring, tonumber = tonumber, select = select, setmetatable = setmetatable,
	getmetatable = getmetatable, rawget = rawget, rawset = rawset, pairs = pairs, ipairs = ipairs,
	next = next, newproxy = newproxy, buffer = buffer, math = math, string = string, table = table,
	utf8 = utf8, bit32 = bit32, vector = vector, coroutine = coroutine, os = os,
}

local chunk = luau.load(source, { debugName = root, environment = env })
local api = chunk()

-- listeners -------------------------------------------------------------------------------
local accepted: { string } = {}
local function listen(event: string)
	local function onValue(_player: any, ...: any)
		local parts = {}
		for i = 1, select("#", ...) do
			local v = select(i, ...)
			parts[i] = if type(v) == "table" then "table" else tostring(v)
		end
		table.insert(accepted, event .. "(" .. table.concat(parts, ",") .. ")")
	end
	local e = api[event]
	if e.On then e.On(onValue) else e.SetCallback(onValue) end
end
for _, ev in { "EchoDelta", "RedeemCode", "RequestFire", "Blob", "ReportView", "Pick" } do
	listen(ev)
end

-- event ids, read from the generated dispatcher ------------------------------------------
local ids: { [string]: number } = {}
if tool == "blink" then
	for idx, name in string.gmatch(source, "Index == (%d+) then\n[^\n]*ReadEVENT_(%w+)") do
		ids[name] = tonumber(idx) :: number
	end
else
	for idx, name in string.gmatch(source, "id == (%d+) then %-%- (%w+)") do
		ids[name] = tonumber(idx) :: number
	end
end
for _, ev in { "EchoDelta", "RedeemCode", "RequestFire", "Blob", "Pick" } do
	assert(ids[ev], "no id for " .. ev)
end

-- byte writer -----------------------------------------------------------------------------
type W = { b: buffer, n: number }
local function W(): W return { b = buffer.create(70000), n = 0 } end
local function u8(w: W, v: number) buffer.writeu8(w.b, w.n, v); w.n += 1 end
local function u16(w: W, v: number) buffer.writeu16(w.b, w.n, v); w.n += 2 end
local function u32(w: W, v: number) buffer.writeu32(w.b, w.n, v); w.n += 4 end
local function f32(w: W, v: number) buffer.writef32(w.b, w.n, v); w.n += 4 end
local function f64(w: W, v: number) buffer.writef64(w.b, w.n, v); w.n += 8 end
local function str(w: W, s: string) buffer.writestring(w.b, w.n, s); w.n += #s end
local function v3(w: W, x: number, y: number, z: number) f32(w, x); f32(w, y); f32(w, z) end
local function done(w: W): buffer
	local out = buffer.create(w.n)
	buffer.copy(out, 0, w.b, 0, w.n)
	return out
end

local NAN, INF = 0 / 0, math.huge
local part = roblox.Instance.new("Part")
local wrongClass = roblox.Instance.new("Folder")

-- packet builders, one per tool layout (layouts read from the generated deserializers) ---
local P = {}

function P.redeem(w: W, text: string)
	u8(w, ids.RedeemCode)
	if tool == "blink" then
		u8(w, #text) -- Blink: u8 length, then bytes
	else
		u8(w, math.max(#text - 1, 0)) -- Zap: u8 (length - 1), then bytes
	end
	str(w, text)
end

type Delta = { gym: number, endsAt: number, phase: number, cells: number, labels: number }
local function delta(o: { [string]: number }?): Delta
	local d: any = { gym = 1.5, endsAt = 1000, phase = 0, cells = 1, labels = 1 }
	for k, v in (o or {}) :: any do d[k] = v end
	return d
end

function P.echo(w: W, d: Delta)
	u8(w, ids.EchoDelta)
	if tool == "blink" then
		-- 24-byte block, then map entries, then the label length table, then label bytes
		u32(w, 7); u8(w, d.phase); u16(w, 10); u16(w, 3); f32(w, d.gym); f64(w, d.endsAt)
		u16(w, d.cells); u8(w, d.labels)
		for i = 1, d.cells do u16(w, i); u8(w, 3); str(w, "abc"); u8(w, 50) end
		for _ = 1, d.labels do u8(w, 2) end
		for _ = 1, d.labels do str(w, "hi") end
	else
		-- bit byte (enum bits 0-2, empty-map bit 3), fields, map (count - 1), labels
		local bits = if d.phase <= 2 then bit32.lshift(1, d.phase) else 0
		if d.cells == 0 then bits = bit32.bor(bits, 8) end
		u8(w, bits); u32(w, 7); u16(w, 10); u16(w, 3); f32(w, d.gym); f64(w, d.endsAt)
		if d.cells > 0 then
			u16(w, d.cells - 1)
			for i = 1, d.cells do u16(w, i); u8(w, 3); str(w, "abc"); u8(w, 50) end
		end
		u8(w, d.labels)
		for _ = 1, d.labels do u8(w, 2); str(w, "hi") end
	end
end

type Fire = { ox: number, dx: number, dist: number, gear: string, aimx: number }
local function fire(o: { [string]: any }?): Fire
	local f: any = { ox = 5, dx = 1, dist = 50, gear = "rocket", aimx = 0 }
	for k, v in (o or {}) :: any do f[k] = v end
	return f
end

function P.fire(w: W, f: Fire)
	u8(w, ids.RequestFire)
	if tool == "blink" then
		u8(w, #f.gear); v3(w, f.ox, 0, 0); v3(w, f.dx, 0, 0); u32(w, 9); f32(w, f.dist)
		v3(w, f.aimx, 0, 0); v3(w, 0, 0, 0); str(w, f.gear)
	else
		u8(w, #f.gear - 1); str(w, f.gear); v3(w, f.ox, 0, 0); v3(w, f.dx, 0, 0); u32(w, 9); f32(w, f.dist)
		v3(w, f.aimx, 0, 0); v3(w, 0, 0, 0)
	end
end

function P.pick(w: W, aimx: number, pointx: number)
	u8(w, ids.Pick); v3(w, aimx, 0, 0); v3(w, 0, 0, 0); v3(w, pointx, 0, 0)
end

function P.blob(w: W, size: number)
	u8(w, ids.Blob); u16(w, size); for _ = 1, size do u8(w, 1) end
end

-- runner ----------------------------------------------------------------------------------
local fakePlayer = { Name = "probe", UserId = 1 }
local function oneLine(s: string): string
	s = string.gsub(s, "^[^\n]-:%d+: ", "")
	return (string.gsub(s, "\n.*", ""))
end

local function run(name: string, handler: Handler, ...: any)
	table.clear(accepted)
	local ok, err = pcall(handler, fakePlayer, ...)
	local verdict = if #accepted > 0 then "accepted" else "rejected"
	local detail = if #accepted > 0 then table.concat(accepted, " ")
		elseif ok then "no listener call, no error (silent drop)"
		else "error: " .. oneLine(tostring(err))
	if #accepted > 0 and not ok then
		detail ..= " | then error: " .. oneLine(tostring(err))
	end
	print(string.format("P1 %s %s %s %s", tool, name, verdict, detail))
end

local rel = reliable.OnServerEvent.fns[1]
local unrel = unreliable.OnServerEvent.fns[1]

local function case(name: string, build: (W) -> (), inst: any?)
	local w = W(); build(w)
	run(name, rel, done(w), if inst == nil then {} else inst)
end

-- text (b)
case("redeem_ok", function(w) P.redeem(w, "ABC123") end)
case("redeem_empty", function(w) P.redeem(w, "") end)
case("redeem_25_ascii", function(w) P.redeem(w, string.rep("A", 25)) end)
case("redeem_96_ascii", function(w) P.redeem(w, string.rep("A", 96)) end)
case("redeem_bad_utf8", function(w) P.redeem(w, "\xff\xfe\xfd") end)
case("redeem_truncated", function(w) u8(w, ids.RedeemCode); u8(w, 20); str(w, "abc") end)
-- state delta (a)
case("delta_ok", function(w) P.echo(w, delta()) end)
case("delta_gym_nan", function(w) P.echo(w, delta({ gym = NAN })) end)
case("delta_gym_inf", function(w) P.echo(w, delta({ gym = INF })) end)
case("delta_gym_ninf", function(w) P.echo(w, delta({ gym = -INF })) end)
case("delta_gym_over", function(w) P.echo(w, delta({ gym = 101 })) end)
case("delta_endsAt_nan_unranged", function(w) P.echo(w, delta({ endsAt = NAN })) end)
case("delta_endsAt_inf_unranged", function(w) P.echo(w, delta({ endsAt = INF })) end)
case("delta_bad_enum", function(w) P.echo(w, delta({ phase = 7 })) end)
case("delta_labels_9", function(w) P.echo(w, delta({ labels = 9 })) end)
case("delta_cells_5000_unbounded_map", function(w) P.echo(w, delta({ cells = 5000 })) end)
-- buffer
case("blob_256", function(w) P.blob(w, 256) end)
case("blob_257", function(w) P.blob(w, 257) end)
-- Instance + vector + CFrame (c)
case("fire_ok", function(w) P.fire(w, fire()) end, { part })
case("fire_origin_nan", function(w) P.fire(w, fire({ ox = NAN })) end, { part })
case("fire_origin_inf", function(w) P.fire(w, fire({ ox = INF })) end, { part })
case("fire_origin_ninf", function(w) P.fire(w, fire({ ox = -INF })) end, { part })
case("fire_dir_nan", function(w) P.fire(w, fire({ dx = NAN })) end, { part })
case("fire_dist_nan", function(w) P.fire(w, fire({ dist = NAN })) end, { part })
case("fire_gear_33", function(w) P.fire(w, fire({ gear = string.rep("g", 33) })) end, { part })
case("fire_missing_instance", function(w) P.fire(w, fire()) end, {})
case("fire_wrong_class", function(w) P.fire(w, fire()) end, { wrongClass })
case("pick_ok", function(w) P.pick(w, 0, 0) end, { part })
case("pick_cframe_nan", function(w) P.pick(w, NAN, 0) end, { part })
case("pick_cframe_inf", function(w) P.pick(w, INF, 0) end, { part })
case("pick_vector_nan_unranged", function(w) P.pick(w, 0, NAN) end, { part })
case("pick_missing_instance", function(w) P.pick(w, 0, 0) end, {})
case("pick_wrong_class", function(w) P.pick(w, 0, 0) end, { wrongClass })
-- wrong types at the remote boundary (a client can fire the raw RemoteEvent with anything)
run("wrongtype_string_not_buffer", rel, "hello", {})
run("wrongtype_number_not_buffer", rel, 5, {})
do
	local w = W(); P.pick(w, 0, 0)
	run("wrongtype_instances_nil", rel, done(w), nil)
	local w2 = W(); P.pick(w2, 0, 0)
	run("wrongtype_instances_number", rel, done(w2), 5)
end
case("unknown_event_id_200", function(w) u8(w, 200); u8(w, 0) end)
-- batching: ok, bad, ok in one packet
case("batch_ok_bad_ok", function(w)
	P.redeem(w, "ONE"); P.redeem(w, ""); P.redeem(w, "THREE")
end)
case("batch_ok_nan_ok", function(w)
	P.redeem(w, "ONE"); P.echo(w, delta({ gym = NAN })); P.redeem(w, "THREE")
end)
-- unreliable (d)
local function view(name: string, px: number, lx: number)
	local w = W()
	if tool == "blink" then u8(w, 0) end
	v3(w, px, 0, 0); v3(w, lx, 0, 0)
	run(name, unrel, done(w), {})
end
view("view_ok", 5, 1)
view("view_pos_nan", NAN, 1)
view("view_pos_inf", INF, 1)
view("view_look_ninf", 5, -INF)

-- spam: 1000 valid RedeemCode packets, decode cost only (not engine timing)
do
	local w = W(); P.redeem(w, "ABC123")
	local b = done(w)
	local t0 = os.clock()
	table.clear(accepted)
	for _ = 1, 1000 do
		pcall(rel, fakePlayer, b, {})
	end
	print(string.format("P1 %s spam_1000_redeem accepted %d listener calls in %.2f ms (Lune decode cost; generated code has no rate limit)",
		tool, #accepted, (os.clock() - t0) * 1000))
end
print(string.format("P1 %s warnings %d", tool, warnings))
