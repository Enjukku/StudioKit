# J015-T06: re-run every probe headless with Blender 5.1.2 (or pass -Blender to use another build).
# Usage: powershell -File run_all.ps1 [-Blender "C:/path/blender.exe"]
param([string]$Blender = "C:/Program Files/Blender Foundation/Blender 5.1/blender.exe")
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$log = Join-Path $here "probe_output.txt"
Remove-Item $log -ErrorAction SilentlyContinue
foreach ($p in Get-ChildItem $here -Filter "*.py" | Where-Object { $_.Name -match "^p\d+_" } | Sort-Object Name) {
  if ($p.Name -eq "p08_maths.py") { $lines = & python $p.FullName }
  else { $lines = & $Blender -b --factory-startup --python $p.FullName 2>&1 }
  $lines | Select-String -Pattern "^PROBE|Traceback|Error" | ForEach-Object { $_.Line } | Add-Content -Path $log -Encoding utf8
}
Write-Output "wrote $log"
