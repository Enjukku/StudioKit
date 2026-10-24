--!strict
-- P1 runtime probe, client side. Waits for workspace attribute P1Run = true, then fires every
-- malformed case at the Blink remotes with hand-crafted buffers (the same bytes an exploiter can
-- send with FireServer), bracketed by P1Case "begin"/"end" so the server can print one verdict
-- line per case. Byte layouts and event indices are read from gen/blink/Server.luau (Blink
-- 0.18.9): reliable EchoDelta=1, RedeemCode=2, RequestFire=3, Blob=4, Pick=5; unreliable
-- ReportView=0. Regenerating the schema can renumber them: re-check before a re-run.
-- Probe-only code: not framework code, never shipped.

local ReplicatedStorage = game:GetService("ReplicatedStorage")

local BlinkClient = require(ReplicatedStorage:WaitForChild("Net"):WaitForChild("BlinkClient")) :: any
local reliable = ReplicatedStorage:WaitForChild("BLINK_RELIABLE_REMOTE") :: RemoteEvent
local unreliable = ReplicatedStorage:WaitForChild("BLINK_UNRELIABLE_REMOTE") :: UnreliableRemoteEvent
local caseRemote = ReplicatedStorage:WaitForChild("P1Case") :: RemoteEvent

local ID = table.freeze({ EchoDelta = 1, RedeemCode = 2, RequestFire = 3, Blob = 4, Pick = 5, ReportView = 0 })
local NAN, INF = 0 / 0, math.huge

local target: Instance = workspace:WaitForChild("P1Target")
local wrongClass = workspace:WaitForChild("P1WrongClass")
local clientOnly: Part = Instance.new("Part") -- exists only on this client: arrives as nil on the server
clientOnly.Name = "P1ClientOnly"
clientOnly.Anchored = true
clientOnly.Parent = workspace

-- byte writer ------------------------------------------------------------------------------
type W = { b: buffer, n: number }
local function newW(): W
	return { b = buffer.create(70000), n = 0 }
end
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

-- packet builders (Blink 0.18.9 layouts) ---------------------------------------------------
local function redeem(w: W, text: string)
	u8(w, ID.RedeemCode); u8(w, #text); str(w, text)
end

type Delta = { gym: number, endsAt: number, phase: number, cells: number, labels: number }
local function delta(o: { [string]: number }?): Delta
	local d: any = { gym = 1.5, endsAt = 1000, phase = 0, cells = 1, labels = 1 }
	for k, v in (o or {}) :: any do
		d[k] = v
	end
	return d
end
local function echo(w: W, d: Delta)
	u8(w, ID.EchoDelta)
	u32(w, 7); u8(w, d.phase); u16(w, 10); u16(w, 3); f32(w, d.gym); f64(w, d.endsAt)
	u16(w, d.cells); u8(w, d.labels)
	for i = 1, d.cells do u16(w, i); u8(w, 3); str(w, "abc"); u8(w, 50) end
	for _ = 1, d.labels do u8(w, 2) end
	for _ = 1, d.labels do str(w, "hi") end
end

type Fire = { ox: number, dx: number, dist: number, gear: string }
local function fire(o: { [string]: any }?): Fire
	local f: any = { ox = 5, dx = 1, dist = 50, gear = "rocket" }
	for k, v in (o or {}) :: any do
		f[k] = v
	end
	return f
end
local function fireBytes(w: W, f: Fire)
	u8(w, ID.RequestFire)
	u8(w, #f.gear); v3(w, f.ox, 0, 0); v3(w, f.dx, 0, 0); u32(w, 9); f32(w, f.dist)
	v3(w, 0, 5, 12); v3(w, 0, 0, 0); str(w, f.gear)
end
local function pick(w: W, aimx: number, pointx: number)
	u8(w, ID.Pick); v3(w, aimx, 0, 0); v3(w, 0, 0, 0); v3(w, pointx, 0, 0)
end
local function blob(w: W, size: number)
	u8(w, ID.Blob); u16(w, size)
	for _ = 1, size do u8(w, 1) end
end

-- case runner ------------------------------------------------------------------------------
local acked: string? = nil
caseRemote.OnClientEvent:Connect(function(kind: unknown, name: unknown)
	if kind == "ack" and type(name) == "string" then
		acked = name
	end
end)

local function waitAck(name: string, seconds: number)
	local deadline = os.clock() + seconds
	while acked ~= name and os.clock() < deadline do
		task.wait()
	end
	if acked ~= name then
		warn(`P1 {name} no ack from server`)
	end
end

local function send(name: string, fireIt: () -> ())
	caseRemote:FireServer("begin", name)
	fireIt()
	caseRemote:FireServer("end", name)
	waitAck(name, 5)
end

local function case(name: string, build: (W) -> (), instances: { Instance }?)
	local w = newW()
	build(w)
	local packet = done(w)
	send(name, function()
		reliable:FireServer(packet, instances or {})
	end)
end

local function view(name: string, px: number, lx: number)
	local w = newW()
	u8(w, ID.ReportView); v3(w, px, 0, 0); v3(w, lx, 0, 0)
	local packet = done(w)
	send(name, function()
		unreliable:FireServer(packet, {})
	end)
end

local function spam(name: string, fireOne: () -> ())
	caseRemote:FireServer("spam_begin", name)
	for i = 1, 1000 do
		fireOne()
		if i % 17 == 0 then
			task.wait() -- about 1000 per second at 60 fps
		end
	end
	caseRemote:FireServer("spam_end", name)
	waitAck(name, 15)
end

local function runAll()
	-- text (b)
	case("redeem_ok", function(w) redeem(w, "ABC123") end)
	case("redeem_empty", function(w) redeem(w, "") end)
	case("redeem_25_ascii", function(w) redeem(w, string.rep("A", 25)) end)
	case("redeem_bad_utf8", function(w) redeem(w, "\xff\xfe\xfd") end)
	case("redeem_truncated", function(w) u8(w, ID.RedeemCode); u8(w, 20); str(w, "abc") end)
	-- state delta (a)
	case("delta_ok", function(w) echo(w, delta()) end)
	case("delta_gym_nan", function(w) echo(w, delta({ gym = NAN })) end)
	case("delta_gym_inf", function(w) echo(w, delta({ gym = INF })) end)
	case("delta_gym_ninf", function(w) echo(w, delta({ gym = -INF })) end)
	case("delta_endsAt_nan_unranged", function(w) echo(w, delta({ endsAt = NAN })) end)
	case("delta_bad_enum", function(w) echo(w, delta({ phase = 7 })) end)
	case("delta_labels_9", function(w) echo(w, delta({ labels = 9 })) end)
	case("delta_cells_5000_unbounded_map", function(w) echo(w, delta({ cells = 5000 })) end)
	-- buffers
	case("blob_256", function(w) blob(w, 256) end)
	case("blob_257", function(w) blob(w, 257) end)
	-- Instance + vector + CFrame (c)
	case("fire_ok", function(w) fireBytes(w, fire()) end, { target })
	case("fire_origin_nan", function(w) fireBytes(w, fire({ ox = NAN })) end, { target })
	case("fire_origin_inf", function(w) fireBytes(w, fire({ ox = INF })) end, { target })
	case("fire_origin_ninf", function(w) fireBytes(w, fire({ ox = -INF })) end, { target })
	case("fire_dir_nan", function(w) fireBytes(w, fire({ dx = NAN })) end, { target })
	case("fire_dist_inf", function(w) fireBytes(w, fire({ dist = INF })) end, { target })
	case("fire_gear_33", function(w) fireBytes(w, fire({ gear = string.rep("g", 33) })) end, { target })
	case("fire_missing_instance_client_only", function(w) fireBytes(w, fire()) end, { clientOnly :: Instance })
	case("fire_wrong_class", function(w) fireBytes(w, fire()) end, { wrongClass })
	case("pick_ok", function(w) pick(w, 0, 0) end, { target })
	case("pick_cframe_nan", function(w) pick(w, NAN, 0) end, { target })
	case("pick_cframe_inf", function(w) pick(w, INF, 0) end, { target })
	case("pick_vector_nan_unranged", function(w) pick(w, 0, NAN) end, { target })
	-- wrong types at the remote boundary
	send("wrongtype_string_not_buffer", function() reliable:FireServer("hello", {}) end)
	send("wrongtype_instances_missing", function()
		local w = newW(); pick(w, 0, 0)
		reliable:FireServer(done(w))
	end)
	case("unknown_event_id_200", function(w) u8(w, 200); u8(w, 0) end)
	case("batch_ok_bad_ok", function(w) redeem(w, "ONE"); redeem(w, ""); redeem(w, "THREE") end)
	-- unreliable (d)
	view("view_ok", 5, 1)
	view("view_pos_nan", NAN, 1)
	view("view_look_ninf", 5, -INF)
	-- spam, about 1000 per second for one second
	local good = newW(); redeem(good, "ABC123")
	local goodPacket = done(good)
	spam("spam_raw_reliable_1000", function() reliable:FireServer(goodPacket, {}) end)
	spam("spam_api_reliable_1000", function() BlinkClient.RedeemCode.Fire("ABC123") end)
	spam("spam_api_unreliable_1000", function() BlinkClient.ReportView.Fire(Vector3.new(5, 0, 0), Vector3.new(1, 0, 0)) end)
	caseRemote:FireServer("finish", "all")
end

if workspace:GetAttribute("P1Run") ~= true then
	workspace:GetAttributeChangedSignal("P1Run"):Wait()
end
runAll()
