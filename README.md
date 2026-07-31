# notebookLM 教材生產工作區

> **澳門初三融合班數學講義 + 練習批量產出系統**

---

## 🗺️ **文檔導航**

你是新手嗎？按這個順序讀：

### **第一次開工：理解專案背景**
1. **[PROJECT_BLUEPRINT.md](PROJECT_BLUEPRINT.md)** 📝
   - 用途：為什麼做這個專案、初期決策（6 個關鍵問題）
   - 讀完後你會懂：專案範圍、設計原則、工作流程框架

### **日常工作：查規則 & 操作方法**
2. **[CLAUDE.md](CLAUDE.md)** 📖
   - 用途：日常工作規則、請求路由表（哪個工作用哪個 skill）、22 條鐵律
   - 讀完後你會懂：怎麼提出需求、禁止做什麼、檔案命名慣例

### **遇到問題：查踩坑 & 解決方案**
3. **[CLAUDE-DETAILED.md](CLAUDE-DETAILED.md)** 🔧
   - 用途：環境事實（已裝什麼軟體）、已知踩坑、品質標準（QB 清單）
   - 讀完後你會懂：為什麼會卡住、怎麼避免、成品檢查清單

### **找檔案：定位資料夾**
4. **[FILE_STRUCTURE.md](FILE_STRUCTURE.md)** 🗂️
   - 用途：每個資料夾是什麼、在哪、狀態如何
   - 讀完後你會懂：講義去哪找、特別班在哪、工具在哪

---

## 🎯 **快速導航（按任務）**

| 我要... | 看這個 | 涉及 skill |
|--------|--------|-----------|
| **出融合班講義 + 練習** | CLAUDE.md §1（路由表第 2 行） | inclusive-math-worksheet-generator |
| **出相似題** | CLAUDE.md §1（路由表第 1 行） | similar-practice-generator |
| **出公式紙** | CLAUDE.md §1（路由表第 3 行） | jh-math-formula-sheet |
| **出 IEP 目標** | CLAUDE.md §1（路由表第 4 行） | macau-iep-math-goals |
| **上傳/更新 GoogleNotebookLM** | CLAUDE.md §1（路由表第 11 行） | notebooklm-sync |
| **檢查成品品質** | CLAUDE-DETAILED.md §3（QB 清單） | math-deliverable-qa |
| **轉 PDF** | CLAUDE.md §1（路由表第 10 行） | office-pdf-convert |
| **找初三講義** | FILE_STRUCTURE.md（檔案地圖） | - |
| **找特別班教材** | FILE_STRUCTURE.md（檔案地圖） | - |
| **看工具說明** | [工具/README.md](工具/README.md) | - |
| **查 NotebookLM 上傳計畫** | [_planning/](\_planning/) | - |

---

## 🔧 **工具與資源**

### **教材生產工具**
詳見 **[工具/README.md](工具/README.md)**
- worksheet-tools（四校聯考工作紙生成）
- math-inclusive-test-generator-new（融合班出題）
- math-visual-scaffold-generator-new（資訊圖表生成）
- inclusive-soil-teaching-deck（土壤教學簡報）

### **已完成的成品**
- ✅ **初三融合班講義練習**：18 單元完整 → `抽離教學_數學/初三數學/融合班講義練習/`
- 💼 **特別班教材**：獨立課程 → `math-test/`
- ⏸ **高一/二/三**：暫停（待需求補充）

### **業務規劃 & 記錄**
- **NotebookLM 上傳規劃** → `_planning/`
- **舊版檔案、歷史紀錄** → `_archive/`

---

## 📖 **開工步驟**

### **每次開工**
```bash
/startup       # 讀工作筆記，找上次進度
```

### **逐單元工作流**
1. 新單元 → 選教學設計（UDL/CRA/其他） → 問你確認
2. 產講義 + 練習（用 skill）
3. 驗算每題（存進 `驗算_<單元>.md`）
4. 上傳 NotebookLM
5. 備份到本機

### **每次收工**
```bash
/shutdown      # 更新工作筆記、git commit
```

詳見 PROJECT_BLUEPRINT.md（工作流程段）

---

## ❓ **常見問題**

**Q：我怎麼知道某個檔案是做什麼用的？**  
A：每個檔案開頭都有「文檔身份」標籤（用途、讀者、更新頻率、相關檔案）。

**Q：我新增一個單元，檔案要放哪？**  
A：看 FILE_STRUCTURE.md 或 CLAUDE.md §4（檔案地圖）。

**Q：我出了講義，怎麼檢查品質？**  
A：CLAUDE-DETAILED.md §3 的 QB 清單，或跑 skill `math-deliverable-qa`。

**Q：我卡住了，怎麼找解決方案？**  
A：先查 CLAUDE-DETAILED.md §2（踩坑筆記），沒有再問。

---

## 📅 **文檔維護**

| 檔案 | 更新頻率 | 最後更新 |
|------|---------|---------|
| PROJECT_BLUEPRINT.md | 幾乎不改 | 2026-08-01 |
| CLAUDE.md | 每學期檢視 | 2026-08-01 |
| CLAUDE-DETAILED.md | 每季更新 | 2026-08-01 |
| FILE_STRUCTURE.md | 新增資料夾時更新 | 2026-08-01 |
| README.md（本檔案） | 每學期更新 | 2026-08-01 |

---

🎯 **準備好了嗎？先讀 PROJECT_BLUEPRINT.md，然後開工！**
