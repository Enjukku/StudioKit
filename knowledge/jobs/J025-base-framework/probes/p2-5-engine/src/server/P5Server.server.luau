--!strict
-- P5 harness: only acts when StudioTestService test args start with "P5:"
local Players = game:GetService("Players")
local StudioTestService = game:GetService("StudioTestService")

local ok, args = pcall(function()
	return StudioTestService:GetTestArgs()
end)
if not ok or type(args) ~= "string" or string.sub(args, 1, 3) ~= "P5:" then
	return
end
local wantStr, holdStr = string.match(args, "^P5:(%d+):?(%d*)$")
local want = tonumber(wantStr) or 1
local hold = tonumber(holdStr) or 3
workspace:SetAttribute("P5", true)
print(`[P5-SERVER] test args = {args}, want {want} clients`)
local t0 = os.clock()
while #Players:GetPlayers() < want and os.clock() - t0 < 90 do
	task.wait(0.5)
end
print(`[P5-SERVER] players joined = {#Players:GetPlayers()} after {string.format("%.1f", os.clock() - t0)}s`)
for _, p in Players:GetPlayers() do
	print(`[P5-SERVER] player {p.Name}`)
end
task.wait(hold)
print("[P5-SERVER] calling EndTest")
StudioTestService:EndTest(`P5-OK players={#Players:GetPlayers()}`)
