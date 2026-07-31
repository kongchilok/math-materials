# 📚 [工具索引] 工具/README.md

> **用途**：列舉所有教材生產工具、快速連結到各工具說明
> **讀者**：找工具、看工具用法時查
> **相關檔案**：← README.md（導航）、CLAUDE.md §1（路由表）

---

# 教材生產工具索引

這個資料夾包含 5 個輔助工具，用來生成各類教材、簡報、出題等。

---

## 🔍 **工具快速查表**

| # | 工具名稱 | 用途 | 輸入 | 輸出 | 說明檔 |
|---|--------|------|------|------|--------|
| 1️⃣ | **worksheet-tools** | 四校聯考工作紙生成 | 年份、題庫 JSON | .docx + .pdf | [README.md](../worksheet-tools/README.md) |
| 2️⃣ | **math-inclusive-test-generator-new** | 融合班融合出題 | 課本段落、難度層級 | 三層難度題組 | [說明](../math-inclusive-test-generator-new/math-inclusive-test-generator.md) |
| 3️⃣ | **math-visual-scaffold-generator-new** | 資訊圖表生成 | 數學概念、關鍵詞 | 視覺支架圖表 | [說明](../math-visual-scaffold-generator-new/math-visual-scaffold-generator.md) |
| 4️⃣ | **inclusive-soil-teaching-deck** | 土壤教學簡報生成 | 課題、內容綱要 | PowerPoint 簡報 | [SKILL.md](../inclusive-soil-teaching-deck/SKILL.md) |
| 🔗 | **（通過 skill）** | 融合班講義 + 練習生成 | 單元主題、教學設計 | .docx + .pdf（三層） | skill `inclusive-math-worksheet-generator` |

---

## 📖 **詳細說明**

### **1️⃣ worksheet-tools**
**路徑**：`worksheet-tools/`  
**用途**：批量生成四校聯考工作紙

**何時用**：
- 需要某一年的四校聯考工作紙分類
- 想快速索引題庫

**使用方法**：
```bash
cd worksheet-tools
.\build.ps1 2026          # 生成 2026 年工作紙
```

**輸出**：`worksheet-tools/output/` 底下的 .docx 和 .pdf

**詳見**：[worksheet-tools/README.md](../worksheet-tools/README.md)

---

### **2️⃣ math-inclusive-test-generator-new**
**路徑**：`math-inclusive-test-generator-new/`  
**用途**：融合班融合出題（按難度層級生成）

**何時用**：
- 需要給融合班設計差異化習題
- 同一份題組要出三層難度版本

**使用方法**：
詳見 [`math-inclusive-test-generator-new/math-inclusive-test-generator.md`](../math-inclusive-test-generator-new/math-inclusive-test-generator.md)

**輸出**：按難度分層的題組（可配合 inclusive-math-worksheet-generator skill）

---

### **3️⃣ math-visual-scaffold-generator-new**
**路徑**：`math-visual-scaffold-generator-new/`  
**用途**：為數學概念生成視覺支架圖表

**何時用**：
- 講義中需要插入概念圖表
- 上傳到 GoogleNotebookLM 做資訊圖表
- 學生理解難的地方想用視覺輔助

**使用方法**：
詳見 [`math-visual-scaffold-generator-new/math-visual-scaffold-generator.md`](../math-visual-scaffold-generator-new/math-visual-scaffold-generator.md)

**輸出**：SVG / PNG 圖表

**未來計畫**：整合到 GoogleNotebookLM 同步流程

---

### **4️⃣ inclusive-soil-teaching-deck**
**路徑**：`inclusive-soil-teaching-deck/`  
**用途**：生成土壤教學簡報（非數學）

**何時用**：
- 跨科合作（自然科學、綜合領域等）
- 製作通用教學簡報

**使用方法**：
詳見 [`inclusive-soil-teaching-deck/SKILL.md`](../inclusive-soil-teaching-deck/SKILL.md)

**輸出**：PowerPoint 簡報

---

### **🔗 融合班講義 + 練習（通過 skill）**
**Skill 名稱**：`inclusive-math-worksheet-generator`  
**用途**：批量產出三層難度融合班講義 + 練習

**何時用**：
- 每次新增一個單元
- 需要講義 + 練習雙檔

**使用方法**：
1. 準備原始教材（課本節錄 PDF）
2. 確認教學設計（UDL / CRA / 差異化等）
3. 呼叫 skill `inclusive-math-worksheet-generator`
4. 產出 .docx（可編輯）+ .pdf（列印版）

詳見：[CLAUDE.md](../CLAUDE.md) §1 路由表（第 2 行）

**輸出**：
- `講義_<單元>.docx` / `.pdf`
- `練習_<單元>.docx` / `.pdf`
- `驗算_<單元>.md`（核算紀錄）

---

## 🛠️ **工具維護說明**

每個工具資料夾都有自己的規則文檔：

| 工具 | 規則檔 | 說明 |
|------|--------|------|
| worksheet-tools | README.md | 規格、題庫結構、運行步驟 |
| math-inclusive-test-generator-new | math-inclusive-test-generator.md | 出題邏輯、難度定義 |
| math-visual-scaffold-generator-new | math-visual-scaffold-generator.md | 圖表類型、使用場景 |
| inclusive-soil-teaching-deck | SKILL.md | 簡報流程、客製化選項 |
| 講義練習生成 | （在 skill 層） | 詳見 `~\.claude\skills\inclusive-math-worksheet-generator\SKILL.md` |

---

## 📋 **工具流程圖**

```
原始教材（課本 PDF）
    ↓
    ├─→ [出題工具] 生成題組
    │       ↓
    │   [講義生成 skill]
    │       ↓
    │   講義 (.docx / .pdf)
    │
    └─→ [視覺支架工具] 生成圖表
            ↓
        資訊圖表
            ↓
        上傳到 GoogleNotebookLM
```

---

## ❓ **工具選擇指南**

**Q：我要快速出一份練習題，用哪個工具？**  
A：`similar-practice-generator` skill（專門出相似題），不是這裡的工具。

**Q：我要出融合班講義，怎麼用？**  
A：用 skill `inclusive-math-worksheet-generator`（見 CLAUDE.md §1），整合了出題 + 排版。

**Q：我要批量做圖表上傳到 NotebookLM，用哪個？**  
A：用 `math-visual-scaffold-generator-new`，詳見該資料夾說明。

**Q：這些工具都要學嗎？**  
A：不是。按需求選：大多數時候只用講義生成 skill；特殊題型才用出題工具；有餘力再玩圖表。

---

**更新日期**：2026-08-01
