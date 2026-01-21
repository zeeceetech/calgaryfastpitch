# Simple smoke test: verify critical files exist.
$root = (Get-Location).Path
$checks = @(
  'index.html',
  'styles.css'
)

# logo can be a few different filenames; accept any present
$logoPaths = @('assets\CFL-BK-BGWhite.svg','assets\logo.svg','assets\logo.png','public\assets\CFL-BK-BGWhite.svg')
$logoFound = $false
foreach ($l in $logoPaths) { if (Test-Path (Join-Path $root $l)) { $logoFound = $true; break } }

# favicon can be png, svg, or ico; accept any present
$faviconPaths = @('assets\favicon.png','assets\favicon.svg','assets\favicon.ico','assets\CFL-BK-BGWhite.svg','public\assets\favicon.png','public\assets\favicon.svg','public\assets\favicon.ico')
$faviconFound = $false
foreach ($f in $faviconPaths) { if (Test-Path (Join-Path $root $f)) { $faviconFound = $true; break } }
$faviconFound = $false
foreach ($f in $faviconPaths) { if (Test-Path (Join-Path $root $f)) { $faviconFound = $true; break } }

$missing = @()
foreach ($c in $checks) {
  if (-not (Test-Path (Join-Path $root $c))) { $missing += $c }
}
if (-not $logoFound) { $missing += 'assets\CFL-BK-BGWhite.svg (logo not found)' }
if (-not $faviconFound) { $missing += 'assets\favicon.(png|svg|ico) (none found)' }
if ($missing.Count -eq 0) {
  Write-Host "SMOKE TEST PASS: all files present"
  exit 0
} else {
  Write-Host "SMOKE TEST FAIL: missing files:`n  $($missing -join "`n  ")"
  exit 1
}
