# build.ps1 — 產生某年的 HTML 並轉成可列印 PDF（學生版＋教師版，若有詳解）
# 用法（在 PowerShell）： .\build.ps1 2024
param([Parameter(Mandatory=$true)][string]$Year)

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$outDir = Join-Path $root "output"

# 1) 產生 HTML
node (Join-Path $root "gen.js") $Year
if ($LASTEXITCODE -ne 0) { throw "gen.js 失敗" }

# 2) 找 Chrome
$chrome = @(
  "C:\Program Files\Google\Chrome\Application\chrome.exe",
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $chrome) { throw "找不到 Chrome，請改用瀏覽器手動『列印成 PDF』" }

$profile = Join-Path $env:TEMP "wsheet-chrome-profile"

# 3) 逐份 HTML → PDF
$variants = @("工作紙", "教師版")
foreach ($v in $variants) {
  $html = Join-Path $outDir "四校聯考數學$($v)_$Year.html"
  if (-not (Test-Path $html)) { continue }
  $pdf  = Join-Path $outDir "四校聯考數學$($v)_$Year.pdf"
  $uri  = ([System.Uri]$html).AbsoluteUri
  Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
  & $chrome --headless --disable-gpu --no-sandbox --disable-dev-shm-usage `
    --user-data-dir="$profile" --no-pdf-header-footer --virtual-time-budget=18000 `
    --run-all-compositor-stages-before-draw --print-to-pdf="$pdf" $uri | Out-Null
  if (Test-Path $pdf) { Write-Host "已輸出 PDF： $pdf" } else { Write-Host "PDF 產生失敗： $v" }
}
Write-Host "完成。檔案在： $outDir"

