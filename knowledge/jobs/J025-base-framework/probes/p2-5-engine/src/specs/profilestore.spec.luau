--!strict
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerScriptService = game:GetService("ServerScriptService")
local JestGlobals = require(ReplicatedStorage.DevPackages.JestGlobals)
local describe, it, expect = JestGlobals.describe, JestGlobals.it, JestGlobals.expect

local ProfileStore = require(ServerScriptService.Vendor.ProfileStore)

describe("ProfileStore 1.0.3 mock", function()
	it("starts and ends a mock session", function()
		local store = ProfileStore.New("test_probe_p3", { coins = 0 })
		local profile = store.Mock:StartSessionAsync("test_key_1", {
			Cancel = function()
				return false
			end,
		})
		expect(profile ~= nil).toBe(true)
		assert(profile, "no profile")
		profile:Reconcile()
		expect(profile.Data.coins).toBe(0)
		expect(profile:IsActive()).toBe(true)
		profile.Data.coins = 5
		profile:EndSession()
		expect(profile:IsActive()).toBe(false)
	end)
end)
