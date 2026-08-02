# 📚 [操作手冊] CLAUDE.md

> **用途**：日常工作規則、請求路由表、鐵律、升級規則
> **讀者**：AI 模型（開工規則）、教師（查規則衝突）
> **更新頻率**：每學期檢視一次
> **相關檔案**：← PROJECT_BLUEPRINT.md（背景）、→ CLAUDE-DETAILED.md（踩坑）

---

# notebookLM 工作區操作手冊

> 讀者：在此工作區開工的任何 AI 模型。這裡不是程式專案，是澳門中學數學教師（融合教育）的教材
> 生產工作區：產出會直接印給學生、交到學校、寫進 IEP——排版錯是小事，數學錯是教學事故。
> 本手冊優先於你的預設習慣；與個別 SKILL.md 衝突時，以較具體的 SKILL.md 為準。

## 0. 溝通
- 對話用繁體中文（使用者常用廣東話口語，跟隨其語氣）；所有文件產出一律書面語 zh-TW。
- 使用者只是描述問題或提問時：報告分析就停，未獲指示不要動手改檔。
- 回報先講結論（產出了什麼、驗收通過沒有），再講細節。
- 批量任務開跑後主動講明「呢輪唔使使用者陪」；收尾一律出收貨摘要（產出清單／QA 結果／剔除或存疑清單／等使用者決定的事項）。

## 1. 請求路由表（動手前先查；有 skill 就用 skill，不要自由發揮）

| 使用者說… | 用什麼 | 關鍵預設 |
|---|---|---|
| 出相似題／照這份出題 | skill `similar-practice-generator` | 每型 3 題；檔名 `功課_<單元>_抽離小班共用版` |
| 融合班講義／練習／調適版 | skill `inclusive-math-worksheet-generator` | 講義、練習分兩檔；無學生資料只出三層共用版；**動筆前先按數學結構選教學設計並問使用者**（SKILL.md 步驟 2.5） |
| 公式紙／考試附件 | skill `jh-math-formula-sheet` | 純公式無例題；≤2 頁；無學生資訊列 |
| IEP 第 8／9 點 | skill `macau-iep-math-goals` | 先審藍圖再填範本；預設通用草稿；不上傳 |
| 四校聯考工作紙／分類索引 | `worksheet-tools\build.ps1 <年>`（工具，非 skill） | 規格見該資料夾 README；題庫＝`data/ALL.json` |
| 段考卷／審題／細目表 | plugin skill `jh-math-exam` | |
| 幾何示意圖 | plugin skill `jh-math-geometry` | 解析幾何坐標圖它不會→自建 grid_svg 模式 |
| 驗收／檢查產出 | skill `math-deliverable-qa` | 詳見 CLAUDE-DETAILED.md §5 |
| 轉 PDF | skill `office-pdf-convert` | 內建本機備援梯級；不要手寫 Word COM |
| 上傳／更新 NotebookLM | skill `notebooklm-sync` | 上傳後必核 source_count |
| 開工／收工 | skill `startup`／`shutdown` | Obsidian 工作筆記＋git |

## 2. 鐵律（除非使用者當次明說偏離）
1. **數學式必須原生**：docx 用 OMML（優先 `{}` 標記語法），HTML 用 MathJax。禁止公式截圖、純文字硬湊、`.doc` 舊格式。
2. **交付雙格式**：`.docx`（教師可編輯）＋`.pdf`（列印版），兩者都是正式交付檔、都要保留。
2.5. **融合班教材要先選教學設計**：設計庫＝`~\.claude\skills\inclusive-math-worksheet-generator\references\teaching-designs.md`。**主設計 1 個＋輔助最多 2 個**；選定前問使用者，批量時開工一次過問齊。
3. **版面唯一真相**＝`~\.claude\skills\inclusive-math-worksheet-generator\references\house-style.md`：黑白列印優先、三層難度只用星星（★☆☆／★★☆／★★★）、12pt 本文／14pt 小標、Calibri＋微軟正黑體。
4. **共用底層只有一份**：OMML 建構器、圖片內嵌、.docx 封裝一律改 `~\.claude\skills\_shared-math-docx\omml_core.py`；各 skill 的 `scripts/` 只放版面層。
5. **每題親自命題、親自驗算**，逐題寫進同資料夾的 `驗算_<單元>.md`。
6. **私隱**：檔名與 NotebookLM 標題不出現學生真名（用代號／學號）；IEP 及含學生資料檔案預設不上傳外部服務。
7. **大文件外包 subagent**（讀原稿 PDF、驗證 PDF），主線只留摘要；超過 5 頁用 Read 的 `pages` 參數。
8. **暫存紀律**：COM 轉檔暫存放專案資料夾；收尾刪 `_src*.pdf`／`_verify*.pdf`／`_tmp*`；交付檔永不放 Claude scratchpad。
9. **無學生資料→出三層共用版**即可，不要追問「有沒有學生資料」卡住流程。
10. **命名跟現例**：交付檔＝`類型_單元名[_版本].docx/pdf`；`原材料\` 是唯讀收件匣。
11. **批量授權慣例**：預計 >30 分鐘的批量生產，開工即視同已授權「中途不問、錯誤自動重試一次、完成或連續卡死兩輪才停」；工作單位＝一課一組（講義＋練習）。
12. **收件匣只有一個**：`notebookLM\新任務\`。

## 3. 升級規則
### 先停下來問（等使用者答覆才做）
1. 任何刪除或覆寫：NotebookLM `source_delete`、覆寫內容不同的同名交付檔、刪除任何非 `_tmp/_src/_verify` 檔案。
2. 任何偏離 house-style 的視覺決定（顏色、字體、行距、分層方式、邊界）。
3. IEP：藍圖未經使用者確認前不得填範本；任何含學生可識別資料的檔案要離開本機前。
4. 範圍衝突：來源題目超出指定課本範圍→列清單請裁決。
5. 讀取結果矛盾（OCR 黏連、驗算不合、兩來源不一致）且高解析核對後仍無法確定。
6. 缺必要資訊（校名／學年／考試名／範圍）→ 一次過問齊。
7. 要求的產出類型超出現有 skill 覆蓋→ 先說明現況再問怎樣做。
8. 同一步驟的主方法＋備援方法都失敗兩輪 → 停手，報告已試過什麼。

### 直接做，不要問
1. 路由表內標準管線的每一步（讀原稿、出題、產檔、驗收、教材上傳 NotebookLM——IEP 除外）。
2. `Stop-Process WINWORD/POWERPNT` 清殭屍、逾時後重試一次。
3. 清理暫存檔（`_src*.pdf`/`_verify*.pdf`/`_tmp*`）。
4. 無學生資料時直接出三層共用版。
5. 按命名慣例建新 NotebookLM 筆記本。
6. 在 `模板試驗\` 做排版實驗。

## 4. 檔案地圖

詳細地圖見 `FILE_STRUCTURE.md`。簡化版：

```
notebookLM/
├─ 抽離教學_數學/                         主要教材庫（按學年）
│  ├─ 初三數學/融合班講義練習/            ✅ 18 單元完整成品
│  ├─ 新任務/                            📥 原材料收件匣
│  └─ 高一/高二/高三數學/                ⏸ 備用（待需求補充）
├─ math-test/                           💼 特別班教材
├─ worksheet-tools/                     🔧 工具：四校聯考工作紙
├─ math-inclusive-test-generator-new/   🔧 工具：融合班出題
├─ math-visual-scaffold-generator-new/  🔧 工具：資訊圖表生成
├─ inclusive-soil-teaching-deck/        🔧 工具：土壤教學簡報
├─ notebookLM/                          ☁️ Google NotebookLM 同步
├─ 模板試驗/                            🎨 排版實驗場
├─ _archive/                            📦 舊版檔案歸檔
└─ CLAUDE.md / CLAUDE-DETAILED.md / FILE_STRUCTURE.md
```

## 5. 相關文件
- 詳細文件（環境事實、踩坑、品質標準）：`CLAUDE-DETAILED.md`
- 完整檔案地圖：`FILE_STRUCTURE.md`
- 版面規格：`~\.claude\skills\inclusive-math-worksheet-generator\references\house-style.md`
- 教學設計庫：同資料夾 `teaching-designs.md`
- 跨 session 經驗：`~\.claude\projects\C--Users-KongChiLok-notebookLM\memory\`
