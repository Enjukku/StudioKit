--!strict
-- P1 runtime probe, server side. Connects a listener to every client-fired Blink event and,
-- for each case the client brackets with P1Case "begin"/"end", prints one Output line:
--   P1 <case> <accepted|rejected> <detail>
-- "rejected" detail is the error the generated deserializer raised (captured from LogService),
-- or "silent" when nothing reached a listener and no error was logged.
-- Probe-only code: not framework code, never shipped.

local LogService = game:GetService("LogService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerScriptService = game:GetService("ServerScriptService")

local Blink = require(ServerScriptService.Net.BlinkServer)
local caseRemote = ReplicatedStorage:WaitForChild("P1Case") :: RemoteEvent

local current: string? = nil
local calls: { string } = {}
local lastError: string? = nil
local spamMode: string? = nil
local spamCount = 0
local spamStart = 0
local spamLast = 0

local function note(event: string, detail: string)
	if spamMode ~= nil then
		spamCount += 1
		spamLast = os.clock()
		return
	end
	table.insert(calls, event .. "(" .. detail .. ")")
end

Blink.EchoDelta.On(function(_player: Player, value)
	local cells = 0
	for _ in value.Cells do
		cells += 1
	end
	note("EchoDelta", `gym={value.GymMultiplier} endsAt={value.EndsAt} phase={value.Phase} cells={cells}`)
end)
Blink.RedeemCode.On(function(_player: Player, text: string)
	note("RedeemCode", `len={#text} utf8={utf8.len(text) ~= nil}`)
end)
Blink.RequestFire.On(function(_player: Player, value)
	note("RequestFire", `origin={value.Origin} target={value.Target:GetFullName()}`)
end)
Blink.Blob.On(function(_player: Player, blob: buffer)
	note("Blob", `len={buffer.len(blob)}`)
end)
Blink.Pick.On(function(_player: Player, target: BasePart, aim: CFrame, point: Vector3)
	note("Pick", `target={target.Name} aimPos={aim.Position} point={point}`)
end)
Blink.ReportView.On(function(_player: Player, position: Vector3, look: Vector3)
	note("ReportView", `pos={position} look={look}`)
end)

LogService.MessageOut:Connect(function(message: string, messageType: Enum.MessageType)
	if current ~= nil and messageType == Enum.MessageType.MessageError and lastError == nil then
		lastError = message
	end
end)

local function oneLine(text: string): string
	return (string.gsub(text, "\n.*", ""))
end

caseRemote.OnServerEvent:Connect(function(player: Player, kind: unknown, name: unknown)
	if type(kind) ~= "string" or type(name) ~= "string" then
		return
	end
	if kind == "begin" then
		current = name
		table.clear(calls)
		lastError = nil
	elseif kind == "end" then
		task.wait(0.1) -- let LogService deliver the deserializer's error line
		local verdict = if #calls > 0 then "accepted" else "rejected"
		local detail = if #calls > 0 then table.concat(calls, " ")
			elseif lastError ~= nil then "error: " .. oneLine(lastError)
			else "silent"
		if #calls > 0 and lastError ~= nil then
			detail ..= " | then error: " .. oneLine(lastError)
		end
		print(`P1 {name} {verdict} {detail}`)
		current = nil
		caseRemote:FireClient(player, "ack", name)
	elseif kind == "spam_begin" then
		spamMode = name
		spamCount = 0
		spamStart = os.clock()
		spamLast = spamStart
	elseif kind == "spam_end" then
		task.wait(3) -- reliable excess is delayed, not dropped (remote.md:378); give it time to land
		print(string.format("P1 %s received %d/1000 last_arrival_after_s %.2f", name, spamCount, spamLast - spamStart))
		spamMode = nil
		caseRemote:FireClient(player, "ack", name)
	elseif kind == "finish" then
		workspace:SetAttribute("P1Done", true)
		print("P1 done")
	end
end)

print("P1 server ready (Blink " .. "0.18.9" .. ")")
