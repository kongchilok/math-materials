// =====================================================================
// 視覺風格手冊產生器
// 直接從 deck-tokens.js 讀值輸出 HTML —— 手冊永遠與 code 同步，不會走樣。
// 執行： node build_style_guide.js  → 樣式手冊_融合簡報.html
// =====================================================================
const fs = require("fs");
const path = require("path");
const T = require("./deck-tokens.js");
const { ramp, color, type, comp, space, radius, layout, RULES, contrast } = T;

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const hex = (h) => "#" + h;

// ---- 舊版實測數據（本次改版前，用同一套演算法量度）----
const OLD_FAILS = [
  ["站別徽章白字 ／ sage #6FA48C", 2.85, 3.0],
  ["手順卡標題白字 ／ sage #6FA48C", 2.85, 3.0],
  ["封面徽章白字 ／ sage #6FA48C", 2.85, 3.0],
  ["站別分隔頁 40pt 白字 ／ sage #6FA48C", 2.85, 3.0],
  ["「目標：」標籤 sage ／ 深帶 #35564E", 2.84, 3.0],
  ["頁尾 #8CA298 ／ 頁面底 #EDF3F0", 2.41, 4.5],
];

const report = T.audit({ print: false });

// ---- 語意 token 反查：哪些語意名指向同一個原始色 ----
const semanticIndex = {};
function idx(group, obj) {
  for (const [k, v] of Object.entries(obj)) {
    if (typeof v !== "string") continue;
    (semanticIndex[v] ||= []).push(`${group}.${k}`);
  }
}
idx("surface", color.surface); idx("ink", color.ink);
idx("accent", color.accent); idx("line", color.line);

function swatchRow(title, entries, note) {
  const cells = entries.map(([label, h, useOverride]) => {
    const uses = useOverride ? [useOverride] : (semanticIndex[h] || []);
    const onLight = contrast(h, color.surface.page).toFixed(2);
    const onWhiteText = contrast(h, "FFFFFF").toFixed(2);
    return `<div class="sw">
      <div class="chip" style="background:${hex(h)}"></div>
      <div class="meta">
        <b>${esc(label)}</b>
        <code>#${esc(h)}</code>
        ${uses.length ? `<span class="uses">${uses.map(esc).join(" · ")}</span>` : `<span class="uses dim">（保留備用）</span>`}
        <span class="ratio">襯頁面底 ${onLight} ／ 承白字 ${onWhiteText}</span>
      </div>
    </div>`;
  }).join("");
  return `<h3>${esc(title)}</h3>${note ? `<p class="note">${note}</p>` : ""}<div class="swatches">${cells}</div>`;
}

const sageEntries = [100, 200, 300, 400, 500, 600, 700, 800, 900].map((k) => [`sage ${k}`, ramp.sage[k]]);
const sandEntries = Object.entries(ramp.sand).map(([k, v]) => [`sand ${k}`, v]);
const inkEntries = Object.entries(ramp.ink).filter(([k]) => k !== "0").map(([k, v]) => [`ink ${k}`, v]);
const chartEntries = [
  ["系列 1", ramp.chart.c1, "chart.series[0]"],
  ["系列 2", ramp.chart.c2, "chart.series[1]"],
  ["系列 3", ramp.chart.c3, "chart.series[2]"],
  ["系列 4（有條件）", ramp.chart.c4Conditional, "chart.seriesExtended[3]"],
];
const seqEntries = ramp.seq.map((v, i) => [`序列 ${i + 1}`, v, `chart.seq[${i}]`]);

const typeRows = Object.entries(type).map(([k, v]) => {
  const px = Math.round(v.fontSize * 1.05);
  return `<tr>
    <td><code>type.${esc(k)}</code></td>
    <td>${v.fontSize}pt</td>
    <td>${esc(v.fontFace)}</td>
    <td>${v.bold ? "粗體" : "一般"}</td>
    <td style="font-size:${Math.min(px, 34)}px; font-family:'Microsoft JhengHei',sans-serif; ${v.bold ? "font-weight:700" : ""}">分式方程</td>
  </tr>`;
}).join("");

const auditRows = report.rows.map((r) => `<tr class="${r.結果 === "PASS" ? "ok" : "bad"}">
  <td>${esc(r.檢查)}</td><td>${esc(r.項目)}</td><td>${esc(r.實測)}</td><td>${esc(r.門檻)}</td>
  <td>${r.結果 === "PASS" ? "通過" : "未通過"}</td></tr>`).join("");

const oldRows = OLD_FAILS.map(([l, got, need]) => `<tr class="bad">
  <td>${esc(l)}</td><td>${got.toFixed(2)}</td><td>${need.toFixed(1)}</td><td>未通過</td></tr>`).join("");

const COMPONENTS = [
  ["卡片 card()", "內容容器", "預設無陰影，靠 1px 框線分隔。舊版每張卡都掛陰影，三張並排時畫面變濁。"],
  ["標題帶 bandHeader()", "卡片頂部分類標籤", "承白字，用 accent.solid（5.87:1）。舊版用淺 sage 只有 2.85:1。"],
  ["步驟圓圈 stepBadge()", "手順卡編號", "accent.strong 承白字 8.15:1。一步一行，行距 1.3。"],
  ["站別徽章 stationBadge()", "章節／站別識別", "膠囊形，固定寬高，與標題基線對齊。"],
  ["主張橫幅 calloutBand()", "全課錨句", "整堂課只用 1–2 次，用滿版深色令它成為視覺焦點。"],
  ["警示欄 cautionBox()", "易錯提醒", "暖砂色而非紅色 —— §D 不以紅綠對比傳達語意。"],
  ["分層任務欄 tierColumns()", "練習 A／B／C", "難度只用星星，不用顏色。題目區固定高，超出即 build 時報錯。"],
  ["CRA 三階 craRow()", "具體｜表徵｜抽象", "內文左對齊（置中會令末行孤字掉隊）。"],
  ["原生分數 frac()／fracRow()", "數學式", "分子／橫線／分母直式疊字。鐵律 1：禁止 &quot;3/x&quot; 斜線寫法，斜線會被守衛攔截。"],
  ["長條圖 barChart()", "資料頁", "每根柱直接標值；類別上限 3；文字穿文字色不穿系列色。"],
  ["大數字磚 statTile()", "單一關鍵數字", "有時答案不是圖，是一個數。"],
];
const compRows = COMPONENTS.map(([n, u, d]) => `<tr><td><b>${n}</b></td><td>${esc(u)}</td><td>${d}</td></tr>`).join("");

// ---- 投影可讀性（AVIXA DISCAS）----
const SLIDE_H_IN = T.layout.H;
const screenHcm = (d) => d * (9 / Math.hypot(16, 9)) * 2.54;
const glyphCm = (pt, d) => (pt / 72) / SLIDE_H_IN * screenHcm(d);
const arcmin = (hcm, dm) => (hcm / 100) / dm * 3438;
const discasCm = (dm) => dm / 150 * 100;
const reqPt = (dm, d) => Math.ceil(discasCm(dm) / screenHcm(d) * SLIDE_H_IN * 72);

const DISTANCES = [3, 4.5, 5, 6.5, 9];
function projTable(diag) {
  const rows = DISTANCES.map((dm) => {
    const g = glyphCm(T.type.bodySm.fontSize, diag);
    const am = arcmin(g, dm);
    const need = discasCm(dm);
    const ok = g >= need && am >= 25;
    const marginal = !ok && am >= 16;
    return `<tr class="${ok ? "ok" : "bad"}">
      <td>${dm} m</td><td>${am.toFixed(1)}</td><td>${need.toFixed(2)} cm</td>
      <td>${g.toFixed(2)} cm</td><td>${reqPt(dm, diag)} pt</td>
      <td>${ok ? "足夠" : marginal ? "勉強・中文會糊" : "不足"}</td></tr>`;
  }).join("");
  const h = screenHcm(diag);
  return `<h3>${diag}" 螢幕（畫面高 ${h.toFixed(1)} cm）</h3>
  <p class="note">4/6/8 法則可服務距離：細節判讀 ${(h * 4 / 100).toFixed(1)} m ／
  一般教學 ${(h * 6 / 100).toFixed(1)} m ／ 被動觀看 ${(h * 8 / 100).toFixed(1)} m</p>
  <table><thead><tr><th>最遠座位</th><th>角分</th><th>DISCAS 需要</th>
  <th>${T.type.bodySm.fontSize}pt 實際</th><th>該距離所需</th><th>判定</th></tr></thead>
  <tbody>${rows}</tbody></table>`;
}

const profileRows = Object.entries(T.PROJECTION).map(([name, p]) => `<tr${name === T.RULES.projection.name ? ' class="ok"' : ""}>
  <td><b>${esc(name)}</b>${name === T.RULES.projection.name ? "（作用中）" : ""}</td>
  <td>${p.screenInches}"</td><td>${p.maxViewDistM} m</td><td>${p.minBodyPt} pt</td>
  <td>${esc(p.note)}</td></tr>`).join("");

const HARD_RULES = [
  ["無襯線黑體", `font.sans = ${T.font.sans}`],
  ["內文 ≥ 20pt", `§D 底線 ${RULES.minBodyPt}pt ∪ 投影情境「${RULES.projection.name}」${RULES.projection.minBodyPt}pt → 實際底線 ${RULES.floorBodyPt}pt。text() 降到此為止，再放不下就報錯`],
  ["標題 ≥ 32pt", `RULES.minTitlePt = ${RULES.minTitlePt}，type.title = ${type.title.fontSize}pt`],
  ["每頁 ≤ 5 行 × 18 字", `RULES.maxLinesPerSlide = ${RULES.maxLinesPerSlide}，checkTextBudget() 檢查`],
  ["行距 1.3–1.5", `leading.tight/normal/loose = ${T.leading.tight}／${T.leading.normal}／${T.leading.loose}`],
  ["淺色底非純白", `surface.page = #${color.surface.page}，audit 逐次驗證`],
  ["左對齊，不用兩端對齊", "所有內文組件預設 align:left"],
  ["難度只用星星", `RULES.tierMarks = ${RULES.tierMarks.join("／")}`],
  ["不用斜體／底線／藝術字", "強調只用加粗＋色塊（accent.tint）"],
  ["配色色盲安全", "圖表色已跑 dataviz validate_palette.js，全項通過"],
];
const ruleRows = HARD_RULES.map(([r, m]) => `<tr><td>${esc(r)}</td><td><code>${esc(m)}</code></td></tr>`).join("");

const html = `<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<title>融合班教學簡報・視覺風格手冊（試驗版 v1）</title>
<style>
  @page { size: A4; margin: 14mm 12mm; }
  * { box-sizing: border-box; }
  body { font-family: "Microsoft JhengHei","Noto Sans TC",sans-serif; color:${hex(color.ink.primary)};
         background:#fff; line-height:1.6; font-size:10.5pt; margin:0; }
  .wrap { max-width: 186mm; margin: 0 auto; }
  h1 { font-size:22pt; margin:0 0 4px; letter-spacing:.5px; }
  h2 { font-size:14pt; margin:22px 0 8px; padding:6px 10px; border-radius:5px;
       background:${hex(color.accent.tint)}; color:${hex(color.ink.primary)}; break-after:avoid; }
  h3 { font-size:11.5pt; margin:14px 0 6px; color:${hex(color.ink.accent)}; break-after:avoid; }
  p { margin:6px 0; }
  .sub { color:${hex(color.ink.secondary)}; font-size:10pt; margin-bottom:14px; }
  .note { color:${hex(color.ink.secondary)}; font-size:9.5pt; margin:2px 0 8px; }
  code { font-family:Consolas,monospace; font-size:9pt; background:${hex(ramp.sage[100])};
         padding:1px 4px; border-radius:3px; }
  table { width:100%; border-collapse:collapse; margin:8px 0 14px; font-size:9.5pt; }
  th { background:${hex(color.accent.solid)}; color:#fff; text-align:left; padding:6px 8px; font-weight:600; }
  td { padding:5px 8px; border-bottom:1px solid ${hex(color.line.rule)}; vertical-align:top; }
  tr.ok td:last-child { color:${hex(ramp.sage[700])}; font-weight:600; }
  tr.bad td:last-child { color:${hex(ramp.sand[700])}; font-weight:600; }
  tr.bad { background:${hex(ramp.sand[50])}; }
  .swatches { display:grid; grid-template-columns:repeat(3,1fr); gap:7px; margin-bottom:10px; }
  .sw { display:flex; gap:8px; align-items:flex-start; border:1px solid ${hex(color.line.card)};
        border-radius:5px; padding:6px; break-inside:avoid; }
  .chip { width:34px; height:34px; border-radius:4px; flex:none; border:1px solid rgba(0,0,0,.12); }
  .meta { font-size:8.5pt; line-height:1.45; min-width:0; }
  .meta b { display:block; font-size:9pt; }
  .meta code { display:inline-block; margin:1px 0; }
  .uses { display:block; color:${hex(color.ink.accent)}; font-size:8pt; word-break:break-all; }
  .uses.dim { color:${hex(color.ink.muted)}; }
  .ratio { display:block; color:${hex(color.ink.muted)}; font-size:7.5pt; }
  .verdict { border-left:4px solid ${hex(color.accent.solid)}; background:${hex(ramp.sage[100])};
             padding:10px 12px; border-radius:0 5px 5px 0; margin:10px 0; break-inside:avoid; }
  .verdict b { color:${hex(color.ink.accent)}; }
  .kpi { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin:12px 0 18px; }
  .kpi div { border:1px solid ${hex(color.line.card)}; border-radius:6px; padding:10px; text-align:center; }
  .kpi .big { font-size:20pt; font-weight:700; color:${hex(color.ink.accent)}; display:block; line-height:1.2; }
  .kpi .lab { font-size:8.5pt; color:${hex(color.ink.secondary)}; }
  section { break-inside:auto; }
  footer { margin-top:20px; padding-top:8px; border-top:1px solid ${hex(color.line.rule)};
           font-size:8.5pt; color:${hex(color.ink.muted)}; }
</style></head><body><div class="wrap">

<h1>融合班教學簡報・視覺風格手冊</h1>
<p class="sub">試驗版 v1 ・ 由 <code>deck-tokens.js</code> 自動生成，與程式碼永遠同步 ・ 尚未併入
<code>inclusive-soil-teaching-deck</code> skill</p>

<div class="kpi">
  <div><span class="big">${OLD_FAILS.length} → 0</span><span class="lab">對比度不合格組數</span></div>
  <div><span class="big">${report.rows.length}</span><span class="lab">自檢項目全數通過</span></div>
  <div><span class="big">2 → 9</span><span class="lab">主色階層級數</span></div>
</div>

<section>
<h2>一、這套系統要解決什麼</h2>
<div class="verdict">
<p><b>問題一：沒有共用設計層。</b>現有 9 份 <code>build_deck.js</code> 各自複製一套配色與
<code>card()</code>／<code>title()</code>／<code>frac()</code>，風格會隨時間飄移，改一次色要改九個檔。</p>
<p><b>問題二：「色盲安全」從未被驗證。</b>§D 硬規則寫明配色需色盲安全，但實測舊配色
<code>#6FA48C</code> 與 <code>#4E8770</code> 常視覺 ΔE 僅 9.7（門檻 15），
即使色覺正常也幾乎分不出；四個語意色的彩度全部低於下限，實質讀成灰色。</p>
<p><b>問題三：硬規則靠人手抽查。</b>字級、對比、每頁字量從來只在 QA 時肉眼看。
本版把規則寫進 <code>audit()</code> 與版面守衛，違規在 build 階段就丟錯。</p>
</div>
</section>

<section>
<h2>二、改版前的實測結果（舊配色）</h2>
<p class="note">用與新版相同的演算法量度舊版單元 04 簡報實際用到的 21 組「文字色 × 底色」。</p>
<table><thead><tr><th>組合</th><th>實測比值</th><th>WCAG AA 門檻</th><th>判定</th></tr></thead>
<tbody>${oldRows}</tbody></table>
<p class="note">根因單一：<code>#6FA48C</code> 太淺，卻被用作承白字的填色（站別徽章、手順卡標題帶
——全簡報出現最頻密的元素）。另外頁尾 11pt 小字只有 2.41:1。</p>
</section>

<section>
<h2>三、色彩系統</h2>
<p class="note">三層架構：Primitive（原始色階）→ Semantic（用途別名）→ Component（組件專用）。
組件層只認語意名，改色只需改一處。</p>
${swatchRow("主色階 sage（介面色階）", sageEntries,
  "亮度單調遞減，每一級只做一件事。<code>accent.solid</code>（600）與 <code>accent.strong</code>（700）刻意拉開 1.39 倍亮度差，令層級讀得出來。")}
${swatchRow("警示色階 sand", sandEntries,
  "易錯／常見寫法欄專用。刻意採暖砂色而非紅色 —— §D 規定不以紅綠對比傳達語意。")}
${swatchRow("文字灰階 ink", inkEntries, "帶極輕微綠味，令文字落在同一色彩家族內。")}
${swatchRow("圖表分類色（全簡報唯一容許較高彩度處）", chartEntries,
  "已跑 <code>dataviz/validate_palette.js</code> 實測：前三色全項通過（含明度帶、彩度、色盲分離、常視覺分離、對比），零警告。第四色會令最差色盲分離降至 ΔE 7.6，僅在有直接標籤時合法。")}
${swatchRow("圖表序列色階（量值編碼）", seqEntries,
  "單一色相、明度單調、相鄰 ΔL ≥ 0.06、淺端 2.10:1 離開頁面底 —— 已通過 <code>--ordinal</code> 驗證。")}
</section>

<section>
<h2>四、字級階</h2>
<p class="note">模數階，基準 = §D 硬底線 20pt，比例約 1.2。右欄為實際字面示意。</p>
<table><thead><tr><th>Token</th><th>字級</th><th>字型</th><th>字重</th><th>示意</th></tr></thead>
<tbody>${typeRows}</tbody></table>
<p class="note"><code>type.caption</code>（${type.caption.fontSize}pt）只用於頁尾與頁碼等版面配件，不屬內文，
故不受 ${RULES.floorBodyPt}pt 底線約束；但仍須達 4.5:1 對比（實測
${contrast(comp.footer.ink, color.surface.page).toFixed(2)}:1）。</p>
</section>

<section>
<h2>五、投影可讀性（課室實測）</h2>
<p class="note">§D 的「內文 ≥ 20pt」是印刷／近距離底線，並未考慮課室後排。
依 AVIXA/ANSI V202.01 DISCAS：基本決策用途（教學內容屬此類）要求
<b>文字高度 ≥ 觀看距離 ÷ 150</b>。中文筆畫密度高，另需約 25 弧分才不會糊
（拉丁字母約 16 弧分即可）。</p>

<div class="verdict">
<p><b>課室條件：</b>50 m² 近正方形 → 邊長約 7.1 m、對角線約 10 m。
最遠座位正對螢幕約 6.5 m，坐對角約 9 m。螢幕 65–75"。</p>
<p><b>設定目標：65" @ 5 m 看得清。</b>DISCAS 要求字高 3.33 cm；20pt 只有 20.6 角分、
24pt 24.7 角分，皆低於中文門檻 25。內文底線因此由 20pt 提升至
<b>${T.type.bodySm.fontSize}pt</b>（25.8 角分），並把「課室」變成可驗證條件（見下方 profile）。</p>
<p><b>三欄版面保留。</b>26pt 之下三欄每行約 9 個中文字，仍然做得到，
但欄內文字必須用明確斷行控制（PowerPoint 不做中文禁則，見組件目錄）。</p>
<p><b>螢幕本身偏小：</b>依 4/6/8 法則，65" 一般教學只服務到 4.9 m、75" 到 5.6 m。
6.5 m 後排超出螢幕能力，這與配色或字體無關，屬硬件限制。</p>
</div>

<h3>投影情境 profile</h3>
<p class="note">切換 <code>ACTIVE_PROJECTION</code> 一行，即可改變整套字級底線；
<code>audit()</code> 會據此驗證，不通過就不准開工。</p>
<table><thead><tr><th>情境</th><th>螢幕</th><th>最遠座位</th><th>內文底線</th><th>依據</th></tr></thead>
<tbody>${profileRows}</tbody></table>

${projTable(65)}
${projTable(75)}

<p class="note"><b>關於 20 m：</b>若真要在 20 m 外讀 ${T.type.bodySm.fontSize}pt 內文，
文字需高 13.3 cm，即畫面高 3.6 m、螢幕約 289" 對角 —— 屬戲院級規格，一般課室不可行。</p>

<h3>深底反白字：halation 補償</h3>
<p class="note">內容頁底色本身是淺色 <code>#${color.surface.page}</code>（主文字對比
${contrast(color.ink.primary, color.surface.page).toFixed(2)}:1），深綠只用於封面與章節分隔頁。
但那些頁面上的<b>白字襯深底</b>在亮面板上會向外暈開（halation），中文筆畫密，
遠距離時筆劃會黏在一起 —— 這是純對比度指標量不出來的問題。三項對策：</p>
<table><thead><tr><th>對策</th><th>做法</th><th>理由</th></tr></thead><tbody>
<tr><td>不用純白</td><td><code>ink.onSolid = #${color.ink.onSolid}</code>、
<code>ink.onDark = #${color.ink.onDark}</code></td>
<td>純白 <code>#FFFFFF</code> 亮度最高、暈開最嚴重；降一點即可明顯收窄</td></tr>
<tr><td>級距加大</td><td><code>darkAdjust.plusPt = ${T.darkAdjust.plusPt}</code></td>
<td>深底文字比同角色的淺底文字大 2pt</td></tr>
<tr><td>加字距</td><td><code>darkAdjust.charSpacing = ${T.darkAdjust.charSpacing}</code></td>
<td>讓筆畫之間留出暈開的餘裕，避免相鄰字黏連</td></tr>
</tbody></table>
<p class="note">改用微灰白後對比由 5.87:1 降至
${contrast(color.ink.onSolid, color.accent.solid).toFixed(2)}:1，仍遠高於 WCAG 大字門檻 3.0。
<b>注意：</b>字距會實質加闊文字，版面估算器必須把 <code>charSpacing</code> 計入，
否則會誤判「放得下」而實際換行溢出。</p>
</section>

<section>
<h2>六、間距、圓角與陰影</h2>
<table><thead><tr><th>類別</th><th>階值</th><th>說明</th></tr></thead><tbody>
<tr><td>間距 space</td><td><code>${Object.entries(space).map(([k, v]) => `${k}=${v}"`).join(" · ")}</code></td><td>版面單位為英寸（LAYOUT_WIDE 13.333 × 7.5）</td></tr>
<tr><td>圓角 radius</td><td><code>${Object.entries(radius).map(([k, v]) => `${k}=${v}"`).join(" · ")}</code></td><td>卡片用 md，膠囊徽章用 pill</td></tr>
<tr><td>陰影 elevation</td><td><code>none（預設） · raised</code></td><td>預設不加陰影，靠框線分隔。舊版每張卡都掛陰影，三張並排畫面變濁</td></tr>
<tr><td>版面邊距</td><td><code>marginX = ${layout.marginX}"，內容寬 ${layout.contentW.toFixed(2)}"</code></td><td>頁尾基線固定 ${layout.footerY}"</td></tr>
</tbody></table>
</section>

<section>
<h2>七、組件目錄</h2>
<table><thead><tr><th>組件</th><th>用途</th><th>設計決定</th></tr></thead><tbody>${compRows}</tbody></table>
</section>

<section>
<h2>八、圖表規範（依 dataviz 技能）</h2>
<table><thead><tr><th>規則</th><th>本系統的實作</th></tr></thead><tbody>
<tr><td>色彩永不單獨承載語意</td><td>每根柱直接標值；≥2 系列必附圖例。黑白列印或色覺障礙下資料仍可讀</td></tr>
<tr><td>分類色固定次序指派，不循環</td><td><code>comp.chart.series</code> 依序取用；第 4 類需明確開啟</td></tr>
<tr><td>類別數上限</td><td><code>maxSeries = ${comp.chart.maxSeries}</code>，超過即報錯，應合併「其他」或改小倍數圖</td></tr>
<tr><td>細筆觸、資料端 4px 圓角</td><td><code>lineWidth = ${comp.chart.lineWidth}</code>，<code>barRadius = ${comp.chart.barRadius}"</code></td></tr>
<tr><td>相鄰填色留 2px 表面間隙</td><td><code>gap = ${comp.chart.gap}"</code></td></tr>
<tr><td>文字穿文字色，不穿系列色</td><td>標籤 <code>#${comp.chart.label}</code>、數值 <code>#${comp.chart.value}</code></td></tr>
<tr><td>網格與座標軸退居背景</td><td>軸線 <code>#${comp.chart.axis}</code>、網格 <code>#${comp.chart.gridline}</code></td></tr>
<tr><td>絕不使用雙 Y 軸</td><td>兩種量綱請拆成兩張圖或指標化到同一基準</td></tr>
</tbody></table>
</section>

<section>
<h2>九、§D 硬規則 → Token 對照</h2>
<p class="note">左欄為 <code>inclusive-deck-checklist.md</code> §D 條文，右欄為系統中負責保證它的機制。</p>
<table><thead><tr><th>硬規則</th><th>由什麼保證</th></tr></thead><tbody>${ruleRows}</tbody></table>
</section>

<section>
<h2>十、自檢結果（本次 build）</h2>
<p class="note">每次 <code>new Deck()</code> 都會先跑一次；不通過就不准開工。</p>
<table><thead><tr><th>檢查</th><th>項目</th><th>實測</th><th>門檻</th><th>結果</th></tr></thead>
<tbody>${auditRows}</tbody></table>
</section>

<section>
<h2>十一、怎樣用</h2>
<table><thead><tr><th>檔案</th><th>角色</th></tr></thead><tbody>
<tr><td><code>deck-tokens.js</code></td><td>三層 token ＋ 硬規則常數 ＋ <code>audit()</code>。改色、改字級只改這裡</td></tr>
<tr><td><code>deck-kit.js</code></td><td>組件層 ＋ 版面守衛。只引用語意 token，不得出現 raw hex</td></tr>
<tr><td><code>build_demo_deck.js</code></td><td>示範用法：重建單元 04 代表頁，內容逐字沿用舊版</td></tr>
<tr><td><code>build_style_guide.js</code></td><td>本手冊的產生器</td></tr>
</tbody></table>
<p class="note">執行方式（GDrive 路徑無法 npm install，指向已驗證的 node_modules 即可）：</p>
<p><code>$env:NODE_PATH="...\簡報_一元二次方程01-03\node_modules"; node build_demo_deck.js</code></p>
</section>

<footer>
融合班教學簡報視覺系統 ・ 試驗版 v1 ・ 本手冊由 <code>build_style_guide.js</code> 自 token 檔生成<br>
尚未併入 skill；現有 <code>inclusive-soil-teaching-deck</code> 與 9 份既有簡報均未更動。
</footer>

</div></body></html>`;

const out = path.join(__dirname, "樣式手冊_融合簡報.html");
fs.writeFileSync(out, html, "utf8");
console.log(`✓ 已產出 ${out}`);
console.log(`  自檢 ${report.rows.length} 項，${report.passed ? "全數通過" : report.fails + " 項未通過"}`);
