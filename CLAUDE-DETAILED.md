# notebookLM 工作區詳細指南

> 此檔案包含環境事實、踩坑、品質標準等詳細參考。正常開工時無需載入；遇到特定問題時才 Read。

## 1. 本機環境事實（2026-07 實測）
- Windows 11＋PowerShell 5.1：沒有 `&&`；`.ps1` 檔必須 **UTF-8 BOM**；不要經 Bash 呼叫 `.ps1`。
- **本機 Word COM 轉 PDF 屢次卡死**。標準梯級（已封裝進 skill `office-pdf-convert`）：清殭屍 → Python DispatchEx 每檔新實例 → 逾時 kill 重試 → 改道 HTML→Chrome headless。
- Word 的 SaveAs 目標**不可**在 `AppData\Local\Temp\claude\...`（沙盒目錄 Word 寫不進去）。
- PowerPoint COM：`WithWindow:=$true` 才能成功 SaveAs；隱藏視窗開檔必失敗。
- 已裝：Python 3.13、PyMuPDF、pywin32、Node.js、Chrome；未裝：LibreOffice、poppler。
- HTML→PDF：Chrome `--headless --print-to-pdf --virtual-time-budget=18000`＋獨立 `--user-data-dir`。
- NotebookLM MCP：認證錯→請使用者 `nlm login`；以 `notebook_list` 的 source_count 為準。

## 2. 本工作區最易踩的坑

### 讀原稿
- 直接抽 `.docx` 純文字＝公式全漏。→ 轉 PDF 再讀；COM 卡死→解壓 `document.xml` 用 lxml 抽 `m:oMath`。
- OCR 來源會黏連選項、讀錯符號。→ 出現矛盾用 PyMuPDF `dpi=200` 裁圖核對。
- 來源測驗題超綱。→ 逐題對照使用者指定課本節次，超綱題列清單請裁決。

### 寫 docx（omml_core／omml_docx）
- `('m', 裸片段)` 沒包 `omath()` → Word 報「檔案毀損」。
- 已建好的片段再包 `mr()` → 文件印出原始碼。→ `x.lstrip().startswith('<m:')` 直通。
- `shaded_box()` 一次只吃一段；塞 para 清單＝無聲的空白灰框。
- `image_para()` 不能放進 `problem_box`。→ 圖放題框前面＋caption。
- 最後一個題框後接 `pagebreak()` → 多一頁空白。→ `trailing_blank=False`。
- 表格儲存格塞純字串 list → Word 報毀損。→ `_tc()` 已加自動包 `para()` 的防呆。
- 表格跨頁無表頭 → 第二頁看不懂。→ 表頭列加 `hdr: True`。

### 寫 HTML 列印版
- 正文的 `<`／`>` 沒轉義→被當標籤，吞掉整段。→ 不等號一律 `&lt;`／`&gt;`；產出後跑 QB-14 檢查。
- 公式內中文變豆腐。→ MathJax `svg:{mtextInheritFont:true}`＋中文包 `\text{}`。
- 每頁手放頁尾→出現空白頁。→ 整份**一個** `position:fixed;bottom:0` 的 `.footer`。
- Fixed 頁尾未預留空間→最後一行被白底蓋住。→ 產出後跑 QB-20；撞到就手動分頁避開。已試「加大邊界＋負 bottom」和 `transform` 皆失敗。
- 表格多、灰底框多：漏 `break-inside:avoid` 會被分頁切開；漏 `.section-h{break-after:avoid}` 出現孤兒標題。
- 格線用 `repeating-linear-gradient`→列印擠成不均勻。→ 真 `<div>` 邊框堆疊。

### 符號與圖形
- 標記符號自創＝踩字型雷。`○□●■` 在微軟正黑體是**半形**，跟 `△◇` 並排大小不一；`⌛⏱⏸` 會渲染成彩色 emoji（黑白列印變灰坨）。→ 實測通過的只有 `①②③④`／`ⓐⓑⓒⓓ`／`☐`／`★☆`／`※`／`⚠`／`▍`／`→`。
- SVG 側邊直排標註用 `rotate(-90)`→Chrome 把中文渲染成筆畫崩壞的糊團。→ 逐字堆疊 `<tspan>`（`design_svg._vtext()`）。

### PowerShell 迴圈跑 COM
- 用 PowerShell 批次 COM 操作→隨機 OutOfMemory。→ 一律 Python DispatchEx 每檔新實例。

### NotebookLM
- 「替換檔案」＝先 `source_add` 新檔，`source_delete` 舊檔前必先問使用者。
- 上傳結果以 source_count 核實。
- 任何上傳前先 `notebook_list` 驗證認證；401/403 即停。

## 3. 品質標準（QB 清單）

執行器＝skill `math-deliverable-qa`（跑 `scripts/qa_check.py`＋目視層＋重算層）。**任何 FAIL 不得交付。**

### 自動檢查層（qa_check.py 判）
| 編號 | 規則 | 適用 | 檢查方法 |
|---|---|---|---|
| QB-1 | docx 結構完好 | 所有 .docx | zipfile 解壓＋minidom 解析 document.xml |
| QB-2 | 公式原生且無洩漏 | 數學類檔案 | document.xml 計 `<m:oMath`；PDF 抽字無洩漏 |
| QB-3 | 禁 `.doc` | 全部 | 副檔名檢查 |
| QB-4 | 頁尾有頁碼欄位 | docx（IEP 除外） | footer*.xml 含 `PAGE` |
| QB-5 | 有同名 `.pdf` | docx（IEP 除外） | 檔案系統＋大小 >10KB |
| QB-6 | 檔名慣例 | 交付檔 | 前綴 ∈ {講義,練習,功課,複習,測驗,公式紙,簡報,工具卡,整合教材,IEP} |
| QB-7 | 黑白 | docx（IEP 除外） | document.xml 無彩色碼 |
| QB-8 | 學生資訊列 | 講義/練習/功課/複習/測驗 PDF | 第 1 頁含 姓名、班別、學號 |
| QB-9 | 星星三層 | 融合／抽離小班練習 PDF | 全文含 ★☆☆、★★☆、★★★ |
| QB-10 | 題答對應 | 練習/功課/測驗 PDF | 題號集合相等且非空 |
| QB-11 | 驗算紀錄 | 練習/功課/測驗 | `驗算*.md` 的題號 ⊇ 文件題號 |
| QB-12 | 無空白頁 | 所有 PDF | 字數 <40 的頁列為 WARN |
| QB-13 | 公式紙專項 | 公式紙 PDF | 含「允許攜帶」；≤2 頁；無「姓名」欄 |
| QB-14 | HTML 標籤白名單 | .html | 無未轉義的 `<` |
| QB-15 | HTML 印刷三件套 | .html | `mtextInheritFont`；`.problem` 有 `break-inside`；`position:fixed` footer 恰一個 |
| QB-16 | 無暫存殘留 | 交付資料夾 | 無 `_src*.pdf`/`_verify*.pdf`/`_tmp*` |
| QB-19 | 教師實施說明頁 | **所有**講義 PDF | 末頁含設計代號 D1~D14 與「褪除」 |
| QB-19b | 無禁用彩色字元 | 所有 PDF | 無 `⌛⏳⏰⏱⏲⏸✅❌❎⭐🔴📌📝` |
| QB-20 | 頁尾未蓋內文 | 直向 PDF | 每頁間距 ≥2pt（2~6pt＝WARN） |

### 流程層檢查（人工或腳本判）
| 編號 | 規則 | 檢查方法 |
|---|---|---|
| QB-17 | NotebookLM 核數 | `notebook_list` 讀 source_count ＝原數−刪除＋新增 |
| QB-18 | IEP 專項 | 指定外欄位為空、表格結構未變；未上傳外部 |
| QB-V1 | 公式渲染目視 | PyMuPDF 轉 PNG 後檢查分數線/根號/上下標正確 |
| QB-V2 | 逐題重算 | 重算每題比對文件答案，100% 一致 |
| QB-V3 | 作答行數 | 選擇/簡答≥2、計算≥5、應用≥3 |
| QB-V4 | 版面首頁 | masthead 後緊接學生資訊列，無另行大標題 |
| QB-V5 | 教學設計落地 | 設計真的長在題目上；A/B/C 有褪除梯度；疊加 ≤主1＋輔2 |

### QB 規則說明

**QB-19（教師實施說明頁）** — 2026-07-27 立，之前的 59 份講義沒有。掃舊資料夾時用 `--legacy-ok` 降為 WARN。

**QB-20（頁尾未蓋內文）** — HTML 管線的 `.footer` 是 `position:fixed`，但 `@page` 沒預留空間，內文流到底時最後一行被白底蓋住（PyMuPDF 抽字仍抽得到，所以 QB-2／QB-12 不會響——只有列印或目視看得出）。已試「加大邊界＋負 bottom」和 `transform: translateY(100%)` 皆失敗——Chrome 都會把頁尾推去下一頁頁頂。目前的處置是「QA 設閘＋撞到就手動分頁避開」。

## 4. 附註
- 交付檔與其 build 腳本放同一單元資料夾；**build 腳本是成品的源頭，要保留**，只清暫存。
- 詳細 SOP：`~\.claude\skills\<skill>\SKILL.md`。
- 教學設計研究依據：`G:\我的雲端硬碟\2ndBrain\每日筆記\2.0\`（平常不用讀，teaching-designs.md 已濃縮）。
