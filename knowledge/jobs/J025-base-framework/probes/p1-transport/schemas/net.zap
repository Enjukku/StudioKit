-- P1 probe schema (Zap 0.6.29). Same payloads as net.blink.
opt server_output = "../gen/zap/Server.luau"
opt client_output = "../gen/zap/Client.luau"
opt types_output = "../gen/zap/Types.luau"
opt casing = "PascalCase"

type DamPhase = enum { Building, Won, Flooded }

type Cell = struct {
	Owner: string.utf8(..20),
	Hp: u8(0..100),
}

type DamDelta = struct {
	Seq: u32,
	Phase: DamPhase,
	Quota: u16,
	Placed: u16,
	GymMultiplier: f32(0..100),
	EndsAt: f64,
	Cells: map { [u16]: Cell }, -- Zap 0.6.29 grammar.lalrpop:124: maps take no size bound
	Labels: string.utf8(..32)[..8],
}

event DamState = {
	from: Server,
	type: Reliable,
	call: SingleAsync,
	data: DamDelta
}

event EchoDelta = {
	from: Client,
	type: Reliable,
	call: SingleAsync,
	data: DamDelta
}

event RedeemCode = {
	from: Client,
	type: Reliable,
	call: SingleAsync,
	data: string.utf8(1..24)
}

type Fire = struct {
	GearId: string.utf8(1..32),
	Origin: vector(f32(-10000..10000), f32(-10000..10000), f32(-10000..10000)),
	Direction: vector(f32(-1.01..1.01), f32(-1.01..1.01), f32(-1.01..1.01)),
	ShotId: u32,
	Distance: f32(0..200),
	Target: Instance.BasePart,
	Aim: CFrame,
}

event RequestFire = {
	from: Client,
	type: Reliable,
	call: SingleAsync,
	data: Fire
}

event Blob = {
	from: Client,
	type: Reliable,
	call: SingleAsync,
	data: buffer(..256)
}

event ReportView = {
	from: Client,
	type: Unreliable,
	call: SingleSync,
	data: (Position: vector(f32(-10000..10000), f32(-10000..10000), f32(-10000..10000)), Look: vector(f32(-1.01..1.01), f32(-1.01..1.01), f32(-1.01..1.01)))
}

event Pick = {
	from: Client,
	type: Reliable,
	call: SingleAsync,
	data: (Target: Instance.BasePart, Aim: CFrame, Point: vector)
}
