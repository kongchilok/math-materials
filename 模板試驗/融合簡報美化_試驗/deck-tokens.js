// =====================================================================
// 融合班教學簡報・設計 Token（試驗版 v1）
// ---------------------------------------------------------------------
// 三層架構：Primitive（原始值）→ Semantic（用途別名）→ Component（組件專用）
// 組件層與 build script 一律「只准引用 semantic / component」，禁止 raw hex。
//
// 本檔同時把 inclusive-deck-checklist.md §D 的硬規則**常數化**，
// 並提供 audit()：build 時先跑一次，違規即拋錯（fail-fast），
// 令「字級 ≥20pt、對比達標、淺色底非純白」由人手檢查變成機器保證。
//
// ⚠ 試驗中，未併入 skill。原 skill 與現有 9 份 build_deck.js 一律不動。
// =====================================================================

// =====================================================================
// 第 0 層：色彩數學（對比度／亮度，供 audit 用）
// =====================================================================
function _lin(c) { return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
function luminance(hex) {
  const h = hex.replace("#", "");
  const v = [0, 2, 4].map((i) => _lin(parseInt(h.slice(i, i + 2), 16) / 255));
  return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
}
function contrast(a, b) {
  const [hi, lo] = [luminance(a), luminance(b)].sort((m, n) => n - m);
  return (hi + 0.05) / (lo + 0.05);
}

// =====================================================================
// 第 1 層：PRIMITIVE — 原始色階
// ---------------------------------------------------------------------
// Sage：主色階。原版只有 sage / sageDeep 兩級（ΔE 9.7，肉眼幾乎分不出），
//       改為 9 級單色階，亮度單調遞減，每一級只做一件事。
// Sand：警示／易錯欄用暖砂色。刻意不用紅色——§D「不以紅綠對比傳達語意」。
// Ink ：文字灰階，帶極輕微綠味令它落在同一家族。
// =====================================================================
const ramp = {
  // sage 是「介面色階」（UI tint scale），不是資料色階：
  // 100 本身就是頁面底，故不適用 dataviz 的 ordinal「淺端需離開表面 2:1」檢查。
  // 資料用的序列色階另見 ramp.seq（已通過 --ordinal 驗證）。
  sage: {
    100: "E6EFEA", // 頁面底（淺色非純白 ✓）
    200: "CFE1D8", // 淺色塊底，承深色字
    300: "AECBBD", // 卡片框線／分隔線
    400: "7DAB93", // 純裝飾填色（永不承白字）
    500: "57876F",
    600: "3E6E58", // 實色填底，承白字
    700: "2F5747", // 強調實色（步驟圓圈／主張橫幅）
    800: "24443A", // 深色頁底（封面／行動頁）
    900: "16302A",
  },
  sand: {
    50:  "F7F2E9", // 警示欄底
    200: "E4D6BA",
    300: "D2BE97", // 警示欄框線
    600: "836A3E",
    700: "6E5934", // 警示欄文字
    800: "54452A",
  },
  ink: {
    900: "1E3730", // 主文字
    700: "3A4F48",
    600: "4A5F58", // 次要文字
    500: "586C64", // 頁尾／註腳（小字仍須達 4.5:1，實測 4.78）
    0:   "FFFFFF", // 純白：只作卡片底，不作深底上的文字
    // 深底上的文字一律用微灰白，不用純白 —— 純白在亮面板上光暈（halation）最強，
    // 中文筆畫密，遠距離會糊成一團。降一點亮度可明顯收窄暈開範圍。
    offWhite: "F2F7F4",
  },
  // 圖表分類色（方向 3）：全簡報唯一容許較高彩度的地方。
  // 低刺激版面之所以在圖表破例，是因為此處色彩要「攜帶資訊」而非裝飾。
  // 已跑 dataviz validate_palette.js 實測（surface E6EFEA、--pairs all）：
  //   c1,c2,c3 → ALL CHECKS PASS（明度帶／彩度／CVD 分離／常視覺分離／對比 全過，零警告）
  //   最差相鄰對 00916A↔D55E00：protan ΔE 10.0、常視覺 ΔE 16.0
  // 色彩永不單獨承載語意——每個系列必配直接標籤（dataviz 不可協商規則）。
  chart: {
    c1: "006C9E", // 藍
    c2: "D55E00", // 橙
    c3: "00916A", // 綠
    // 第 4 色為「有條件可用」：加入後 CVD 最差對降至 ΔE 7.6（6–8 floor band），
    // 僅在有直接標籤／表格檢視時合法。教學圖表建議上限 3 類，多過就合併為「其他」或改小倍數圖。
    c4Conditional: "CC79A7", // 粉紫
  },
  // 圖表序列色階（量值編碼，單一色相）——已通過 --ordinal 驗證：
  // 明度單調、相鄰 ΔL ≥0.06、淺端 2.10:1 離開表面、色相散佈 4°
  seq: ["79B0A1", "559A87", "3A806D", "246654", "114C3D"],
};

// 字級階（modular scale，比例約 1.15）
// 基準由 §D 的 20pt 提升至 25pt —— 目標為 65" 螢幕、5 m 距離看得清：
// 20pt 只有 20.6 角分、24pt 24.7 角分，皆低於中文門檻 25。詳見 projection-check.js。
const size = {
  caption:  15, // 頁尾／頁碼（chrome，非內文，不受內文底線約束）
  bodySm:   25, // 內文底線（§D 20pt ∪ 投影情境 25pt）
  body:     26,
  headline: 30,
  subtitle: 34,
  title:    38, // 頁標題（§D 底線 32pt）
  display:  44, // 章節／站別大標
  hero:     56, // 封面主標
};

// 間距階（英寸；pptxgenjs LAYOUT_WIDE = 13.333 × 7.5 in）
const space = {
  xs: 0.1, sm: 0.15, md: 0.25, lg: 0.4, xl: 0.6, xxl: 0.9,
};

const radius = { sm: 0.08, md: 0.14, lg: 0.2, pill: 0.35 };

// 陰影：原版每張卡都掛陰影，畫面偏濁。改為兩級，預設「無」。
const elevation = {
  none: undefined,
  raised: { type: "outer", color: "9FB5AB", blur: 6, offset: 1.5, angle: 90, opacity: 0.28 },
};

const font = {
  sans: "Microsoft JhengHei", // §D：無襯線黑體
  mono: "Consolas",           // 算式等寬，利於對齊
};

// =====================================================================
// 第 2 層：SEMANTIC — 用途別名
// 組件層只認這一層的名字，改色只需改這裡。
// =====================================================================
const color = {
  surface: {
    page:    ramp.sage[100], // 淺色非純白
    card:    ramp.ink[0],
    sunken:  ramp.sage[200],
    dark:    ramp.sage[800], // 封面／站別分隔／行動頁
    darkBand: ramp.sage[900],
    caution: ramp.sand[50],
  },
  ink: {
    primary:     ramp.ink[900],
    secondary:   ramp.ink[600],
    muted:       ramp.ink[500],
    onSolid:     ramp.ink.offWhite, // 承在 accent.solid / strong 之上（非純白，抗光暈）
    onDark:      "EAF2ED",          // 承在 surface.dark 之上
    onDarkMuted: "B7CEC3",
    accent:      ramp.sage[700], // 淺底上的主色字（kicker／提示）
    caution:     ramp.sand[700],
  },
  accent: {
    solid:  ramp.sage[600], // 徽章／標題帶（承白字）
    strong: ramp.sage[700], // 步驟圓圈／主張橫幅（承白字）
    tint:   ramp.sage[200], // 淺色塊（承深色字）
    decor:  ramp.sage[400], // 純裝飾，永不承文字
  },
  line: {
    card:    ramp.sage[300],
    rule:    ramp.sage[300],
    caution: ramp.sand[300],
  },
  chart: ramp.chart,
  seq: ramp.seq,
};

const type = {
  hero:     { fontFace: font.sans, fontSize: size.hero,     bold: true },
  display:  { fontFace: font.sans, fontSize: size.display,  bold: true },
  title:    { fontFace: font.sans, fontSize: size.title,    bold: true },
  subtitle: { fontFace: font.sans, fontSize: size.subtitle, bold: true },
  headline: { fontFace: font.sans, fontSize: size.headline, bold: true },
  kicker:   { fontFace: font.sans, fontSize: size.bodySm,   bold: true },
  body:     { fontFace: font.sans, fontSize: size.body },
  bodySm:   { fontFace: font.sans, fontSize: size.bodySm },
  caption:  { fontFace: font.sans, fontSize: size.caption },
  math:     { fontFace: font.mono, fontSize: size.body,     bold: true },
  mathSm:   { fontFace: font.mono, fontSize: size.bodySm,   bold: true },
};

// 行距：§D 要求 1.3–1.5
const leading = { tight: 1.3, normal: 1.4, loose: 1.5 };

// ---------------------------------------------------------------------
// 深底文字補償（反白字 halation）
// 亮面板上的淺色字會向外暈開，中文筆畫密，遠距離時筆劃會黏在一起。
// 三項對策：① 用微灰白不用純白（見 ink.offWhite）
//           ② 級距加大 2pt   ③ 加字距，讓筆畫之間留出暈開的餘裕
// ---------------------------------------------------------------------
const darkAdjust = { plusPt: 2, charSpacing: 0.8, leading: leading.loose };

// 版面座標
const layout = {
  W: 13.333, H: 7.5,
  marginX: 0.6,
  get contentW() { return this.W - this.marginX * 2; },
  titleY: 0.5,
  kickerY: 0.42,
  titleWithKickerY: 0.86,
  contentTop: 1.9,
  footerY: 6.98,
};

// =====================================================================
// 第 3 層：COMPONENT — 組件專用 token
// =====================================================================
const comp = {
  card:         { fill: color.surface.card, line: color.line.card, lineWidth: 1, radius: radius.md, shadow: elevation.none },
  cardRaised:   { fill: color.surface.card, line: color.line.card, lineWidth: 1, radius: radius.md, shadow: elevation.raised },
  stationBadge: { fill: color.accent.solid, ink: color.ink.onSolid, radius: radius.pill, h: 0.62, w: 1.7, ...type.headline },
  stepBadge:    { fill: color.accent.strong, ink: color.ink.onSolid, dia: 0.5, ...type.bodySm, bold: true },
  bandHeader:   { fill: color.accent.solid, ink: color.ink.onSolid, h: 0.72, radius: radius.md },
  calloutBand:  { fill: color.accent.strong, ink: color.ink.onSolid, radius: radius.md, h: 0.95 },
  cautionBox:   { fill: color.surface.caution, line: color.line.caution, ink: color.ink.caution, lineWidth: 1.5, radius: radius.md },
  tierColumn:   { fill: color.surface.card, line: color.line.card, headFill: color.accent.tint, headInk: color.ink.primary, radius: radius.md },
  footer:       { ink: color.ink.muted, inkOnDark: color.ink.onDarkMuted, ...type.caption },
  // 圖表（方向 3，依 dataviz 規範）
  chart: {
    axis:      color.line.rule,
    gridline:  ramp.sage[200],
    label:     color.ink.secondary,  // 文字永遠穿文字色，不穿系列色
    value:     color.ink.primary,
    barRadius: 0.055,                // 4px 圓角資料端
    gap:       0.028,                // 2px 表面間隙
    lineWidth: 2,                    // 細筆觸
    markerMin: 0.11,                 // ≥8px 標記
    // 固定次序指派，永不循環；第 4 類需附直接標籤才合法
    series:    [ramp.chart.c1, ramp.chart.c2, ramp.chart.c3],
    seriesExtended: [ramp.chart.c1, ramp.chart.c2, ramp.chart.c3, ramp.chart.c4Conditional],
    seq:       ramp.seq,
    maxSeries: 3,                    // 超過就合併「其他」或改小倍數圖
  },
};

// =====================================================================
// 硬規則（inclusive-deck-checklist.md §D）— 常數化
// =====================================================================
// ---------------------------------------------------------------------
// 投影情境：§D 的「內文 ≥20pt」是印刷／近距離底線，並未考慮課室後排。
// 依 AVIXA DISCAS（文字高度 ≥ 距離/150）實測：50 m² 課室配 65–75" 螢幕，
// 20pt 只服務到約 4.5 m；6.5 m 後排需要 26–29pt。
// 故按用途分兩個 profile，audit() 會據此驗證。詳見 projection-check.js。
// ---------------------------------------------------------------------
// 螢幕一律以 65"（使用者環境的較差情況）計算，好過假設 75" 之後失準。
const PROJECTION = {
  抽離小組: {
    screenInches: 65, maxViewDistM: 5.0,
    minBodyPt: 25,
    note: "使用者指定目標：65\" @ 5 m 看得清。DISCAS 需字高 3.33 cm；24pt 雖過 DISCAS 但中文角分僅 24.7（門檻 25）仍會糊，故底線取 25pt",
  },
  全班共融: {
    screenInches: 65, maxViewDistM: 6.5,
    minBodyPt: 29,
    note: "後排 6.5 m；DISCAS 要求字高 4.33 cm → 65\" 螢幕需 29pt。三欄版面每行只剩約 7 個中文字，須改兩欄或大幅精簡",
  },
};
// 目前作用中的情境（改這一行即可切換整套字級底線）
const ACTIVE_PROJECTION = "抽離小組";

const RULES = {
  minBodyPt: 20,
  minTitlePt: 32,
  maxLinesPerSlide: 5,
  maxCharsPerLine: 18,
  leadingMin: 1.3,
  leadingMax: 1.5,
  pageBgMustNotBePureWhite: true,
  banned: ["italic", "underline", "wordart"], // 強調只用加粗＋色塊
  tierMarks: ["★☆☆", "★★☆", "★★★"],          // 難度只用星星，不用顏色
  wcagLargeText: 3.0,   // ≥18pt bold 或 ≥24pt
  wcagBodyText: 4.5,
};
// 實際生效的內文底線＝§D 底線與投影情境要求，取其大
RULES.projection = { name: ACTIVE_PROJECTION, ...PROJECTION[ACTIVE_PROJECTION] };
RULES.floorBodyPt = Math.max(RULES.minBodyPt, RULES.projection.minBodyPt);

// 所有「文字色 × 底色」的合法配對——audit 逐組驗
// large=true 代表 ≥18pt bold 或 ≥24pt（WCAG 大字門檻 3:1），否則 4.5:1
const PAIRINGS = [
  ["封面主標 / 深底",        color.ink.onDark,      color.surface.dark,    true],
  ["封面副標 / 深底",        color.ink.onDarkMuted, color.surface.dark,    true],
  ["深底內文 / 深底",        color.ink.onDark,      color.surface.dark,    true],
  ["深色橫幅內文 / darkBand", color.ink.onDark,      color.surface.darkBand, true],
  ["站別徽章白字 / 實色",     color.ink.onSolid,     color.accent.solid,    true],
  ["標題帶白字 / 實色",       color.ink.onSolid,     color.accent.solid,    true],
  ["步驟圓圈白字 / 強調色",   color.ink.onSolid,     color.accent.strong,   true],
  ["主張橫幅白字 / 強調色",   color.ink.onSolid,     color.accent.strong,   true],
  ["主文字 / 卡片白底",       color.ink.primary,     color.surface.card,    false],
  ["主文字 / 頁面底",         color.ink.primary,     color.surface.page,    false],
  ["主文字 / 淺色塊",         color.ink.primary,     color.accent.tint,     false],
  ["次要文字 / 卡片白底",     color.ink.secondary,   color.surface.card,    false],
  ["次要文字 / 頁面底",       color.ink.secondary,   color.surface.page,    false],
  ["主色字 kicker / 頁面底",  color.ink.accent,      color.surface.page,    true],
  ["警示文字 / 警示底",       color.ink.caution,     color.surface.caution, true],
  ["頁尾 / 頁面底",           comp.footer.ink,       color.surface.page,    false],
  ["頁尾 / 深色頁",           comp.footer.inkOnDark, color.surface.dark,    false],
  ["圖表標籤 / 頁面底",       comp.chart.label,      color.surface.page,    false],
  ["圖表數值 / 卡片白底",     comp.chart.value,      color.surface.card,    false],
  ["圖表系列1 / 頁面底",      ramp.chart.c1,         color.surface.page,    true],
  ["圖表系列2 / 頁面底",      ramp.chart.c2,         color.surface.page,    true],
  ["圖表系列3 / 頁面底",      ramp.chart.c3,         color.surface.page,    true],
  ["裝飾色標籤 / 深色橫幅",   color.accent.decor,    color.surface.darkBand, true],
  ["裝飾色分隔線 / 深色頁",   color.accent.decor,    color.surface.dark,    true],
];

// =====================================================================
// audit()：build 前自檢。回傳報告；opts.strict 時違規拋錯。
// =====================================================================
function audit(opts = {}) {
  const rows = [];
  let fails = 0;

  // 1. 對比度
  for (const [label, fg, bg, large] of PAIRINGS) {
    const need = large ? RULES.wcagLargeText : RULES.wcagBodyText;
    const got = contrast(fg, bg);
    const ok = got >= need;
    if (!ok) fails++;
    rows.push({ 檢查: "對比", 項目: label, 實測: got.toFixed(2), 門檻: need.toFixed(1), 結果: ok ? "PASS" : "FAIL" });
  }

  // 2. 字級底線（§D 底線 ∪ 投影情境要求）
  const bodyRoles = ["bodySm", "body", "kicker"];
  for (const r of bodyRoles) {
    const ok = type[r].fontSize >= RULES.floorBodyPt;
    if (!ok) fails++;
    rows.push({ 檢查: "字級", 項目: `內文 ${r}`, 實測: type[r].fontSize, 門檻: RULES.floorBodyPt, 結果: ok ? "PASS" : "FAIL" });
  }

  // 2b. 投影可讀性：DISCAS 文字高度 ≥ 距離/150
  const pj = RULES.projection;
  const screenHcm = pj.screenInches * (9 / Math.hypot(16, 9)) * 2.54;
  const glyphCm = (type.bodySm.fontSize / 72) / layout.H * screenHcm;
  const needCm = pj.maxViewDistM / 150 * 100;
  const pjOk = glyphCm >= needCm;
  if (!pjOk) fails++;
  rows.push({
    檢查: "投影", 項目: `${pj.name}：${pj.screenInches}" @ ${pj.maxViewDistM}m 字高`,
    實測: glyphCm.toFixed(2) + "cm", 門檻: needCm.toFixed(2) + "cm", 結果: pjOk ? "PASS" : "FAIL",
  });
  for (const r of ["title", "display", "hero"]) {
    const ok = type[r].fontSize >= RULES.minTitlePt;
    if (!ok) fails++;
    rows.push({ 檢查: "字級", 項目: `標題 ${r}`, 實測: type[r].fontSize, 門檻: RULES.minTitlePt, 結果: ok ? "PASS" : "FAIL" });
  }

  // 3. 頁面底不得純白
  const notWhite = color.surface.page.toUpperCase() !== "FFFFFF";
  if (!notWhite) fails++;
  rows.push({ 檢查: "底色", 項目: "頁面底非純白", 實測: color.surface.page, 門檻: "≠FFFFFF", 結果: notWhite ? "PASS" : "FAIL" });

  // 4. 主色階亮度需單調遞減（sequential ramp 才讀得出層級）
  const keys = [100, 200, 300, 400, 500, 600, 700, 800, 900];
  let mono = true;
  for (let i = 1; i < keys.length; i++) {
    if (luminance(ramp.sage[keys[i]]) >= luminance(ramp.sage[keys[i - 1]])) mono = false;
  }
  if (!mono) fails++;
  rows.push({ 檢查: "色階", 項目: "sage 亮度單調遞減", 實測: mono ? "單調" : "亂序", 門檻: "單調", 結果: mono ? "PASS" : "FAIL" });

  // 5. 相鄰強調級距要拉得開（原版 sage↔sageDeep 亮度比僅 1.47，讀不出層級）
  const gap = luminance(ramp.sage[600]) > 0 ? contrast(ramp.sage[600], ramp.sage[700]) : 0;
  const gapOk = gap >= 1.25;
  if (!gapOk) fails++;
  rows.push({ 檢查: "色階", 項目: "solid↔strong 可辨級距", 實測: gap.toFixed(2), 門檻: "1.25", 結果: gapOk ? "PASS" : "FAIL" });

  const report = { rows, fails, passed: fails === 0 };
  if (opts.print !== false) {
    console.log("\n=== 設計 Token 自檢（§D 硬規則）===");
    console.log("檢查  項目".padEnd(30) + "實測".padStart(8) + "門檻".padStart(8) + "  結果");
    console.log("-".repeat(62));
    for (const r of rows) {
      console.log(
        (r.檢查 + "  " + r.項目).padEnd(28) +
        String(r.實測).padStart(8) + String(r.門檻).padStart(8) + "  " +
        (r.結果 === "PASS" ? "PASS" : "**FAIL**")
      );
    }
    console.log("-".repeat(62));
    console.log(report.passed ? `全部 ${rows.length} 項通過 ✓` : `${fails} 項未通過 ✗`);
  }
  if (opts.strict && !report.passed) throw new Error(`設計 Token 自檢未通過：${fails} 項違反 §D 硬規則`);
  return report;
}

module.exports = {
  ramp, size, space, radius, elevation, font,
  color, type, leading, darkAdjust, layout, comp,
  RULES, PAIRINGS, PROJECTION, ACTIVE_PROJECTION, audit, contrast, luminance,
};

if (require.main === module) audit({ strict: false });
