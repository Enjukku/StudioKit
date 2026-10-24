-- Pasted into MCP execute_luau (Edit, or Server during play). Returns a one-line summary.
local rs = game:GetService("ReplicatedStorage")
local sss = game:GetService("ServerScriptService")
local ctx = game:GetService("RunService"):IsEdit() and "Edit" or (game:GetService("RunService"):IsServer() and "Server" or "Client")
local t0 = os.clock()
local Jest = require(rs.DevPackages.Jest)
local okRun, ok, value = pcall(function()
	return Jest.runCLI(rs, { verbose = false, ci = true }, { sss.Specs }):await()
end)
local dt = os.clock() - t0
if not okRun then return `[{ctx}] runCLI threw: {tostring(ok)}` end
if not ok then return `[{ctx}] promise rejected: {tostring(value)} ({dt}s)` end
local r = value.results
return `[{ctx}] wall={string.format("%.2f", dt)}s suites={r.numTotalTestSuites} suitesFailed={r.numFailedTestSuites} tests={r.numTotalTests} passed={r.numPassedTests} failed={r.numFailedTests} success={tostring(r.success)}`
