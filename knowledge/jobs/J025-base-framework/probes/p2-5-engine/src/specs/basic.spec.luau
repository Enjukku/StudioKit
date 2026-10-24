--!strict
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local JestGlobals = require(ReplicatedStorage.DevPackages.JestGlobals)
local describe, it, expect = JestGlobals.describe, JestGlobals.it, JestGlobals.expect

describe("basic", function()
	it("adds numbers and compares tables", function()
		expect(1 + 1).toBe(2)
		expect({ a = 1, b = { 2, 3 } }).toEqual({ a = 1, b = { 2, 3 } })
	end)
end)
