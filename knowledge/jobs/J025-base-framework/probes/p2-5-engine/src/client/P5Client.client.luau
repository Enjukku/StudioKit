--!strict
if not game:IsLoaded() then
	game.Loaded:Wait()
end
local Players = game:GetService("Players")
task.wait(1)
if workspace:GetAttribute("P5") then
	print(`[P5-CLIENT] {Players.LocalPlayer.Name} sees P5 flag, replicated players = {#Players:GetPlayers()}`)
end
