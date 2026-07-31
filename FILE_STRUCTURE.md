# notebookLM 檔案結構地圖

> 2026-07-31 版本。明確標識每個資料夾的用途、狀態和維護負責。

## 📂 核心結構

```
notebookLM/
├─ 抽離教學_數學/                    ← 主要教材庫（按學年組織）
│  ├─ 初三數學/融合班講義練習/        ✅ 18 單元完整成品（講義+練習+簡報）
│  ├─ 高一數學/                      ⏸ 備用（待實際需求補充）
│  ├─ 高二數學/                      ⏸ 備用（待實際需求補充）
│  ├─ 高三數學/                      ⏸ 備用（待實際需求補充）
│  └─ 新任務/                        📥 原始材料收件匣
│
├─ math-test/                        💼 特別班教材（獨立課程體系）
│
├─ 工具/                             🔧 教材生產工具（各類腳本+生成器）
│  ├─ worksheet-tools/               四校聯考工作紙產生器
│  ├─ math-inclusive-test-generator-new/   融合班出題工具
│  ├─ math-visual-scaffold-generator-new/  資訊圖表生成（配合 NotebookLM）
│  └─ inclusive-soil-teaching-deck/        土壤教學簡報工具（非數學）
│
├─ notebookLM/                       ☁️ Google NotebookLM 同步資料夾
│  └─ 工作筆記.md                    核心：單元進度、規格確認
│
├─ 模板試驗/                         🎨 排版實驗場（不交付）
│
├─ _archive/                         📦 歷史檔案歸檔
│  ├─ bulk_upload_*.py               (舊版上傳腳本)
│  ├─ upload_log.txt                 (舊版上傳日誌)
│  └─ QA報告_全庫_*.md               (舊版QA報告)
│
├─ CLAUDE.md                         📋 專案規則、操作手冊
├─ CLAUDE-DETAILED.md                📚 詳細踩坑指南
└─ FILE_STRUCTURE.md                 🗺️ 本檔案（現在讀）
```

## ⚠️ 清理紀錄（2026-07-31）

| 項目 | 動作 | 原因 |
|------|------|------|
| q121_zoom.png、q128129_full2.png | 🗑️ 刪除 | 孤兒圖片，無用 |
| bulk_upload.ps1 等暫存工具 | 📦 歸檔 → `_archive/` | 已由 skill 取代 |
| _tmp_convert.py | 🗑️ 刪除 | 一次性暫存腳本 |

## 💡 使用指南

### 新增單元流程
1. **來源材料** → 放進 `抽離教學_數學/新任務/`
2. **生成成品** → 用 skill `inclusive-math-worksheet-generator` 或 `similar-practice-generator`
3. **成品位置** → `抽離教學_數學/<年級數學>/` 下的 `<單元名>/`
4. **GoogleNotebookLM 同步** → 手動或透過 `notebooklm-sync` skill
5. **資訊圖表** → 用 `math-visual-scaffold-generator-new` 生成後同步

### 特別班（math-test）
- 獨立課程體系，成品也在同資料夾
- 如需與初三類似流程，遵同上，但改路徑為 `math-test/<單元>/`

### 工具維護
- **不要** 把工具輸出檔放進 `工具/` 下
- 工具的 `.py`、`.js`、`package.json` 要保留（build 腳本是源頭）
- 工具的暫存輸出（`_src*.pdf` 等）收工時刪除

### 暫存紀律
- 交付前必刪：`_src*.pdf`、`_verify*.pdf`、`_tmp*`
- 交付檔永不放 Claude scratchpad
- 大文件（>5MB）優先用 subagent 讀取

## 🔄 與 Google NotebookLM 的同步流程

> 詳細：skill `notebooklm-sync`

1. **講義 + 練習** 定期同步（source add）
2. **資訊圖表**（未來）通過 `math-visual-scaffold-generator-new` 生成後上傳
3. 驗證：每次上傳後用 `notebook_list` 核實 source_count

---

最後更新：2026-07-31
