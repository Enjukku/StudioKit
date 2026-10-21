--!strict
--[[
scene_probe.luau: read-only scene probe for tools/env/scene_audit.py.

Kit tool: universal (Studio Kit). Run it through Studio MCP execute_luau (datamodel_type "Edit").
Get the source with the config filled in from:
  python tools/env/scene_audit.py probe --root Workspace/<StageFolder> [--chunk-size N --chunk K]
It prints one JSON document as line(s) "SCENE_PROBE <k>/<n> <slice>" and returns the same text.
Save the output to a file; `scene_audit.py audit --probe <file>...` joins the slices.

It only reads. It creates no Instances; RaycastParams and OverlapParams are query datatypes, not
Instances, and never enter the data model. Unreadable properties are left out of the record
(JSON has no key), which the Python side reports as UNKNOWN, never as a default.

Place conventions (contract with environment-craft):
  zone volume  BasePart tagged "AmbienceZone" with string attribute "ZoneId"
  play area    BasePart tagged "PlayArea" (optional)
  source       any Instance with string attribute "AmbienceId"; audio and effect objects at or under it belong to it

APIs used (docs mirror knowledge/external/roblox-creator-docs/_api-reference/):
  game, workspace, Enum               globals/RobloxGlobals.yaml:26, :76, :16
  ServiceProvider:GetService          classes/ServiceProvider.yaml:66
  HttpService:JSONEncode              classes/HttpService.yaml:295 (empty table -> [], inf/nan not valid JSON)
  CollectionService:HasTag            classes/CollectionService.yaml:391
  Instance:GetDescendants             classes/Instance.yaml:1524
  Instance:FindFirstChild             classes/Instance.yaml:1056
  Instance:GetFullName                classes/Instance.yaml:1552
  Instance:GetAttribute               classes/Instance.yaml:1294 (nil when not set)
  Instance:IsDescendantOf             classes/Instance.yaml:1733
  Instance.Parent                     classes/Instance.yaml:519
  Object:IsA, Object.ClassName        classes/Object.yaml:141, :33
  Workspace.Terrain                   classes/Workspace.yaml:1234
  WorldRoot:Raycast                   classes/WorldRoot.yaml:1075 (direction max 15,000 studs, :1093)
  WorldRoot:GetPartBoundsInBox        classes/WorldRoot.yaml:667 (bounding boxes, not true shapes)
  RaycastParams.new/.FilterType/.FilterDescendantsInstances/.IgnoreWater
                                      datatypes/RaycastParams.yaml:29, :190, :175, :78
  RaycastFilterType.Include/Exclude   enums/RaycastFilterType.yaml:26, :19
  RaycastResult.Distance/.Instance/.Position  datatypes/RaycastResult.yaml:22, :32, :54
  OverlapParams.new/.FilterType/.FilterDescendantsInstances
                                      datatypes/OverlapParams.yaml:28, :154, :140
  BasePart.CFrame/.Size/.Position/.Anchored/.Transparency/.CastShadow
                                      classes/BasePart.yaml:704, :1828, :1509, :64, :2085, :653
  Light.Shadows                       classes/Light.yaml:80 (PointLight, SpotLight, SurfaceLight inherit Light)
  Attachment.WorldPosition            classes/Attachment.yaml:303
  PVInstance:GetPivot                 classes/PVInstance.yaml:97 (used for Model parents)
  CFrame:GetComponents/:PointToWorldSpace/:PointToObjectSpace
                                      datatypes/CFrame.yaml:1033, :936, :967
  CFrame.Position/.RightVector/.UpVector/.LookVector  datatypes/CFrame.yaml:628, :712, :734, :684
  Vector3.new/.X/.Y/.Z                datatypes/Vector3.yaml:39, :286, :297, :308
  task.wait                           libraries/task.yaml:196 (yield so Studio stays responsive)
  string.gmatch/.sub/.format, table.clone/.insert/.concat, math.abs/.min/.max/.ceil,
  pcall, print, typeof, ipairs         libraries/*.yaml, globals/LuaGlobals.yaml
Not documented, so not measured: MeshPart triangle count (no such property in classes/MeshPart.yaml).
]]

-- config (scene_audit.py probe rewrites these four lines)
local ROOT_PATH = "Workspace"
local RAY_LENGTH = 5000
local CHUNK_SIZE = 0
local CHUNK_INDEX = 0

local HttpService = game:GetService("HttpService")
local CollectionService = game:GetService("CollectionService")
local Lighting = game:GetService("Lighting")
local SoundService = game:GetService("SoundService")
local Workspace = game:GetService("Workspace")

-- Geometric epsilon (studs): float32 spacing is <= 0.002 studs for coordinates up to 16,384 studs,
-- so 0.01 absorbs rounding but no gap a player can see (0.01 stud is about 3 mm). Not a tolerance.
local EPS = 0.01
local MAX_RAY = 15000 -- WorldRoot.yaml:1093
local YIELD_EVERY = 500

local LIGHT_CLASSES = { "PointLight", "SpotLight", "SurfaceLight" }
local EFFECT_CLASSES = { "ParticleEmitter", "Beam", "Trail", "Fire", "Smoke", "Sparkles" }
local AUDIO_CLASSES = { "AudioEmitter", "AudioPlayer", "Sound" }

type Rec = { [string]: any }

local function emit(doc: string): string
	local size = if CHUNK_SIZE > 0 then CHUNK_SIZE else math.max(#doc, 1)
	local n = math.max(1, math.ceil(#doc / size))
	local lines = {}
	for k = 1, n do
		if CHUNK_INDEX == 0 or CHUNK_INDEX == k then
			local line = string.format("SCENE_PROBE %d/%d %s", k, n, string.sub(doc, (k - 1) * size + 1, k * size))
			print(line)
			table.insert(lines, line)
		end
	end
	return table.concat(lines, "\n")
end

local function read(inst: Instance, prop: string): any
	local ok, value = pcall(function()
		return (inst :: any)[prop]
	end)
	return if ok then value else nil
end

local function classIn(inst: Instance, list: { string }): string?
	for _, c in ipairs(list) do
		if inst:IsA(c) then
			return c
		end
	end
	return nil
end

local function vec(v: Vector3): { number }
	return { v.X, v.Y, v.Z }
end

local function anchorOf(inst: Instance): string?
	local node: Instance? = inst
	while node ~= nil do
		local id = node:GetAttribute("AmbienceId")
		if typeof(id) == "string" then
			return id
		end
		node = node.Parent
	end
	return nil
end

local function positionOf(inst: Instance): Vector3?
	local parent = inst.Parent
	if parent == nil then
		return nil
	elseif parent:IsA("Attachment") then
		return (parent :: Attachment).WorldPosition
	elseif parent:IsA("BasePart") then
		return (parent :: BasePart).Position
	elseif parent:IsA("PVInstance") then
		return (parent :: PVInstance):GetPivot().Position
	end
	return nil
end

-- world half-height of a part's axis-aligned bounding box
local function halfY(cf: CFrame, size: Vector3): number
	return (math.abs(cf.RightVector.Y) * size.X + math.abs(cf.UpVector.Y) * size.Y + math.abs(cf.LookVector.Y) * size.Z) / 2
end

-- true when all 8 corners of the box (cf, size) lie inside other's box (bounding-box estimate)
local function encloses(other: BasePart, cf: CFrame, size: Vector3): boolean
	local ocf, half = other.CFrame, other.Size / 2
	for _, sx in ipairs({ -1, 1 }) do
		for _, sy in ipairs({ -1, 1 }) do
			for _, sz in ipairs({ -1, 1 }) do
				local p = ocf:PointToObjectSpace(cf:PointToWorldSpace(Vector3.new(sx * size.X / 2, sy * size.Y / 2, sz * size.Z / 2)))
				if math.abs(p.X) > half.X + EPS or math.abs(p.Y) > half.Y + EPS or math.abs(p.Z) > half.Z + EPS then
					return false
				end
			end
		end
	end
	return true
end

local root: Instance? = game
for seg in string.gmatch(ROOT_PATH, "[^/]+") do
	root = if root then root:FindFirstChild(seg) else nil
end
if root == nil then
	return emit(HttpService:JSONEncode({ probe = "scene_probe", version = 1, error = "root not found: " .. ROOT_PATH }))
end
local stageRoot = root :: Instance

local zones, areas, parts, objects, anchors = {}, {}, {}, {}, {}
local markers: { Instance } = {}
local stageParts: { BasePart } = {}

for _, inst in ipairs(stageRoot:GetDescendants()) do
	if inst:IsA("BasePart") and not inst:IsA("Terrain") then
		local part = inst :: BasePart
		local isZone = CollectionService:HasTag(part, "AmbienceZone")
		local isArea = CollectionService:HasTag(part, "PlayArea")
		if isZone or isArea then
			local rec: Rec = { path = part:GetFullName(), cf = { part.CFrame:GetComponents() }, size = vec(part.Size) }
			if isZone then
				local zid = part:GetAttribute("ZoneId")
				if typeof(zid) == "string" then
					rec.zone_id = zid
				end
				table.insert(zones, rec)
			else
				table.insert(areas, rec)
			end
			table.insert(markers, part)
		else
			table.insert(stageParts, part)
		end
	end
end

local function scanObjects(container: Instance, scope: string, visual: boolean)
	for _, inst in ipairs(container:GetDescendants()) do
		local aid = inst:GetAttribute("AmbienceId")
		if typeof(aid) == "string" then
			table.insert(anchors, { path = inst:GetFullName(), class = inst.ClassName, ambience_id = aid, scope = scope })
		end
		local kind: string? = nil
		local class: string? = classIn(inst, AUDIO_CLASSES)
		if class then
			kind = "audio"
		elseif visual then
			class = classIn(inst, LIGHT_CLASSES)
			if class then
				kind = "light"
			else
				class = classIn(inst, EFFECT_CLASSES)
				kind = if class then "effect" else nil
			end
		end
		if kind then
			local rec: Rec = { kind = kind, class = inst.ClassName, path = inst:GetFullName(), scope = scope }
			local pos = positionOf(inst)
			rec.positioned = pos ~= nil
			if pos then
				rec.pos = vec(pos)
			end
			rec.anchor_id = anchorOf(inst)
			if kind == "light" then
				rec.shadows = read(inst, "Shadows")
			end
			table.insert(objects, rec)
		end
	end
end
scanObjects(stageRoot, "stage", true)
if stageRoot ~= Lighting and not stageRoot:IsDescendantOf(Lighting) then
	scanObjects(Lighting, "Lighting", false)
end
if stageRoot ~= SoundService and not stageRoot:IsDescendantOf(SoundService) then
	scanObjects(SoundService, "SoundService", false)
end

local down = RaycastParams.new()
down.FilterType = Enum.RaycastFilterType.Exclude
local terrainRay = RaycastParams.new()
terrainRay.FilterType = Enum.RaycastFilterType.Include
terrainRay.FilterDescendantsInstances = { Workspace.Terrain }
terrainRay.IgnoreWater = true -- water is not ground; a part under water is not buried
local overlap = OverlapParams.new()
overlap.FilterType = Enum.RaycastFilterType.Exclude
local grow = Vector3.new(2 * EPS, 2 * EPS, 2 * EPS)

for i, part in ipairs(stageParts) do
	local cf, size = part.CFrame, part.Size
	local rec: Rec = { path = part:GetFullName(), class = part.ClassName, cf = { cf:GetComponents() }, size = vec(size) }
	rec.anchored = read(part, "Anchored")
	rec.transparency = read(part, "Transparency")
	rec.cast_shadow = read(part, "CastShadow")
	local filter = table.clone(markers)
	table.insert(filter, part)
	local hy = halfY(cf, size)

	-- floating: ray down from the centre, ignoring the part itself and the marker volumes
	down.FilterDescendantsInstances = filter
	local hit = Workspace:Raycast(cf.Position, Vector3.new(0, -math.min(hy + RAY_LENGTH, MAX_RAY), 0), down)
	if hit then
		rec.down_dist = hit.Distance
		rec.down_hit = hit.Instance:GetFullName()
	else
		rec.down_hit = "NO_HIT"
	end

	-- buried: first terrain surface met by a ray from above the part's top, at its centre
	local above = math.min(RAY_LENGTH, MAX_RAY - 2 * hy)
	local t = Workspace:Raycast(cf.Position + Vector3.new(0, hy + above, 0), Vector3.new(0, -(above + 2 * hy), 0), terrainRay)
	rec.terrain_y = if t then t.Position.Y else "NO_HIT"

	-- contact and enclosure: other parts whose bounding boxes touch this part's box
	overlap.FilterDescendantsInstances = filter
	local contacts = 0
	for _, other in ipairs(Workspace:GetPartBoundsInBox(cf, size + grow, overlap)) do
		if not other:IsA("Terrain") then
			contacts += 1
			if rec.enclosed_by == nil and read(other, "Transparency") == 0 and encloses(other, cf, size) then
				rec.enclosed_by = other:GetFullName()
			end
		end
	end
	rec.contacts = contacts
	table.insert(parts, rec)
	if i % YIELD_EVERY == 0 then
		task.wait()
	end
end

return emit(HttpService:JSONEncode({
	probe = "scene_probe",
	version = 1,
	root = stageRoot:GetFullName(),
	ray_length = RAY_LENGTH,
	eps = EPS,
	parts = parts,
	zones = zones,
	play_areas = areas,
	objects = objects,
	anchors = anchors,
	triangles = "UNKNOWN",
}))
