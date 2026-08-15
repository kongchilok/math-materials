# 四校聯考數學工作紙 — 產生工具

從澳門四校聯考歷屆試題，產生可列印的**學生版工作紙**與**教師版（含答案與詳解）**。

## 需求
- Node.js（已安裝）
- Google Chrome（用來把 HTML 轉 PDF；也可在瀏覽器手動「列印成 PDF」）

## 資料夾
```
worksheet-tools/
  extract.js          抽出題庫資料 → data/ALL.json
  gen.js              產生某年的學生版＋教師版 HTML → output/
  build.ps1           一鍵：產生 HTML 並轉 PDF
  gen_index.py        產生 16 單元分類索引（HTML＋PDF 四頁小冊）
  data/ALL.json       題庫（2017–2026，每年 15 選擇＋5 解答）
  solutions/
    sol2017.js…sol2026.js   各年教師版詳解（工序分析法），全 10 年已完成
  output/             產生的 HTML / PDF
```

## 用法

### 一鍵產生（建議）
PowerShell：
```powershell
cd C:\Users\KongChiLok\notebookLM\worksheet-tools
.\build.ps1 2024
```
輸出在 `output/`：`四校聯考數學工作紙_2024.pdf`（學生版）、`四校聯考數學教師版_2024.pdf`。

### 分步
```powershell
node gen.js 2024          # 只產生 HTML（學生版一定有；教師版需有 solutions/sol2024.js）
```
再用瀏覽器開 `output/*.html`，Ctrl+P →「另存為 PDF」。

### 更新題庫（來源 HTML 有變動時）
```powershell
node extract.js "C:\Users\KongChiLok\Desktop\四校聯考數學正卷_練習_2017-2026_測試版.html"
```

## 版面規格（已定案，沿用）
- 內文 12pt；標題 14pt「澳門四校聯考　{年} 年試題　數學正卷」；頁首精簡（邊距 0.5cm）
- 抬頭欄位：姓名／班別／學號
- 選項橫向流動（放不下換行）；圖片浮動到選項旁
- 書寫格線＝真實 div 邊框線堆疊（等距、不用 CSS 漸層）
- 學生版：選擇題加「相關公式＋方向提示」框＋3 行書寫＋答案欄；解答題每題各一整頁
- 教師版：每題＝相關公式＋正確答案＋「工序分析法」多區域詳解（一行一等號、等號對齊、數學式為主）
- 公式用 MathJax（與來源網頁一致），圖片內嵌 base64 → 公式與圖片完整顯示

## 新增其他年份的教師版
教師版詳解是**人工撰寫**的（比原解更細、數學式為主、依所求拆多區域）。
要做某年教師版，需新增 `solutions/solYYYY.js`，格式照 `sol2024.js`：
```js
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });
const choice = { 1: { ans: r`(B)　...`, parts: [ P("", [ reg(r`工序 1 · ...`, r`
  左式 &= ...
  &= ...
`) ]) ] }, /* ...到 15 */ };
const solution = { 1: { ans: r`(a) ... (b) ...`, parts: [ P(r`（a）...`, [ reg(...) ]), P(r`（b）...`, [...]) ] }, /* ...到 5 */ };
module.exports = { choice, solution };
```
- 每個 region 的 `math` 是多行字串，行內用 `&` 標等號對齊點；產生器會接成 `aligned` 環境。
- 缺 `solYYYY.js` 時，`gen.js` 仍會產生學生版（不需詳解）。

## 狀態（2026-07）
- 2017–2026 全 10 年完成：教師版詳解＋學生填空版（有 solYYYY.js 時 gen.js 自動出填空骨架版），`output/` 共 40 份 HTML/PDF。
- 16 單元重新分類已寫回 `data/ALL.json` 的 type 欄（原檔備份 `data/ALL.original.json`）；分類索引見 `output/四校聯考數學_歷屆試題分類索引.html/pdf`。
- 互動網頁版 `output/index.html` 對應 GitHub repo `kongchilok/four-school-math`（GitHub Pages）；本機改動需使用者自行 commit 才生效。
- 補圖機制：`imageoverrides.js` ＋ `images/`（題庫缺圖時補上；SVG 必須有 width/height）。
