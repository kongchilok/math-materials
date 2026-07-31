# -*- mode: powershell; coding: utf-8 -*-
# 批量上傳高一高二教材到 NotebookLM

param(
    [string]$Unit = ""  # 可選: 指定單元，留空則全部
)

# 高一高二單元與筆記本 ID 的對應
$unitMap = @{
    "高一\融合班教學資源\第一學段\01_集合與常用邏輯用語" = "13564236-e41b-4dc6-aa5c-d618a147233e"
    "高一\融合班教學資源\第一學段\02_函數的概念與性質" = "1590dc99-ca39-4902-ba42-a28cde9682a3"
    "高一\融合班教學資源\第一學段\03_指數與對數" = "410544c4-9508-46d2-bd22-b7a600a1676d"
    "高一\融合班教學資源\第二學段\01_三角函數" = "ed589a78-927a-4910-908e-dc863144ddd2"
    "高一\融合班教學資源\第二學段\02_平面向量與正餘弦定理" = "f7c75aa4-f2b2-438b-b068-5e34e7746175"
    "高一\融合班教學資源\第二學段\03_立體幾何初步" = "a88b4200-e742-428e-8f79-3d5fd253216b"
    "高一\融合班教學資源\第一學段\04_多項式與因式定理" = "cd53c5b6-8104-4746-b949-f6e8d0723035"
    "高二\融合班教學資源\第一學段\01_直線的傾斜角與斜率" = "a01e782a-5746-4bf5-b72f-fe105e86f301"
    "高二\融合班教學資源\第一學段\02_圓的方程與直線圓位置關係" = "19ccc58d-09a2-4edf-b21f-a30b9fc45abf"
    "高二\融合班教學資源\第一學段\03_圓錐曲線" = "690635ab-8504-4583-a3dd-5d043311eef7"
    "高二\融合班教學資源\第二學段\01_數列" = "6daa6562-75f5-4e02-b922-11a7faf68733"
    "高二\融合班教學資源\第一學段\04_不等式的性質與基本不等式" = "c3101402-0a44-4d4a-9245-5a051389abbe"
    "高二\融合班教學資源\第二學段\02_排列組合與概率" = "ba1d8f54-1f99-4941-b17b-f1645c946bfe"
}

$basePath = "C:\Users\KongChiLok\notebookLM\抽離教學_數學"
$total = 0
$uploaded = 0

foreach ($unit in $unitMap.Keys) {
    if ($Unit -and $unit -notlike "*$Unit*") {
        continue
    }

    $unitPath = Join-Path $basePath $unit
    $notebookId = $unitMap[$unit]

    if (-not (Test-Path $unitPath)) {
        Write-Host "❌ $unit 資料夾不存在" -ForegroundColor Red
        continue
    }

    # 列出所有 docx 和 pdf，排除鎖檔
    $files = @(Get-ChildItem $unitPath -Include *.docx, *.pdf -Depth 0 | Where-Object { -not $_.Name.StartsWith("~$") })

    Write-Host "`n【$unit】$($files.Count) 個檔案 → $notebookId" -ForegroundColor Cyan

    foreach ($file in $files) {
        $total++
        try {
            # 調用 nlm source add 命令
            $result = nlm sources add --notebook $notebookId --file "$($file.FullName)" 2>&1
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  ✅ $($file.Name)" -ForegroundColor Green
                $uploaded++
            } else {
                Write-Host "  ⚠️ $($file.Name)" -ForegroundColor Yellow
            }
        } catch {
            Write-Host "  ❌ $($file.Name) - $_" -ForegroundColor Red
        }
    }
}

Write-Host "`n========== 上傳摘要 ==========" -ForegroundColor Magenta
Write-Host "預計: $total, 成功: $uploaded"
