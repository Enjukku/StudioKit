--!strict
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerScriptService = game:GetService("ServerScriptService")
local JestGlobals = require(ReplicatedStorage.DevPackages.JestGlobals)
local describe, it, expect = JestGlobals.describe, JestGlobals.it, JestGlobals.expect

local Counter = require(ReplicatedStorage.ProbeShared.Counter)
local Wallet = require(ServerScriptService.ProbeServer.Wallet)

describe("modules", function()
	it("requires a ReplicatedStorage module", function()
		expect(Counter.add(2, 3)).toBe(5)
	end)
	it("requires a ServerScriptService module", function()
		local w = Wallet.new()
		Wallet.grant(w, 7)
		expect(w.coins).toBe(7)
	end)
end)
