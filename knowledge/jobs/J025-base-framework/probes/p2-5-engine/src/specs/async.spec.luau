--!strict
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local JestGlobals = require(ReplicatedStorage.DevPackages.JestGlobals)
local describe, it, expect = JestGlobals.describe, JestGlobals.it, JestGlobals.expect

describe("async", function()
	it("yields with task.wait inside a test", function()
		local t0 = os.clock()
		task.wait(0.25)
		expect(os.clock() - t0 >= 0.2).toBe(true)
	end)
end)
