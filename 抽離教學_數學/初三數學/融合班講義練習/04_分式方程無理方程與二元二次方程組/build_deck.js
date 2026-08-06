// 融合抽離小組 SOIL 教學簡報：分式方程・無理方程・二元二次方程組
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。
// ⚠ 無斜體／底線／藝術字（inclusive-deck-checklist.md §52/60/88）——強調只用加粗＋色塊。
// ⚠ 分數一律用 frac()/fracRow() 疊字，禁止 "/" 斜線寫法（鐵律1：數學式必須原生）。
// 教學設計：D2 手順卡（主）＋ D12 自我核對、D14 錯誤分析對比（輔），與講義／練習同步。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "分式方程・無理方程・二元二次方程組（融合抽離版）";

// ---- 配色 (Sage Calm 低刺激) ----
const C = {
  bgLight: "EDF3F0", bgDark: "2E4A43", ink: "233A34", soft: "5C6F68",
  sage: "6FA48C", sageDeep: "4E8770",
  block: "DCEAE3", block2: "CFE0D8", cardLine: "B9CFC5",
  white: "FFFFFF", starInk: "2E4A43",
  warnBg: "F3EDE4", warnLine: "C9B79A", warnInk: "6B5836", // 「常見寫法」欄：低飽和暖灰，非紅色
};
const F = "Microsoft JhengHei";
const MONO = "Consolas";

// ---- 共用小工具 ----
function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("初三數學 · 分式方程・無理方程・二元二次方程組（抽離小組·融合版）", {
    x: 0.5, y: 7.06, w: 10.5, h: 0.32, align: "left", valign: "middle",
    fontFace: F, fontSize: 11, color: dark ? "9FB8AE" : "8CA298",
  });
  s.addText(String(n), {
    x: 12.2, y: 7.06, w: 0.9, h: 0.32, align: "right", valign: "middle",
    fontFace: F, fontSize: 11, color: dark ? "9FB8AE" : "8CA298",
  });
}
function title(s, txt, kicker) {
  if (kicker) {
    s.addText(kicker, { x: 0.6, y: 0.42, w: 12, h: 0.4, fontFace: F, fontSize: 18, bold: true, color: C.sageDeep, align: "left" });
    s.addText(txt, { x: 0.6, y: 0.82, w: 12.1, h: 0.8, fontFace: F, fontSize: 34, bold: true, color: C.ink, align: "left" });
  } else {
    s.addText(txt, { x: 0.6, y: 0.5, w: 12.1, h: 0.9, fontFace: F, fontSize: 34, bold: true, color: C.ink, align: "left" });
  }
}
function stepCircle(s, x, y, n, d) {
  const dia = d || 0.5;
  s.addShape(p.ShapeType.ellipse, { x, y, w: dia, h: dia, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText(String(n), { x, y, w: dia, h: dia, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.white });
}
function stationBadge(s, txt, x, y) {
  s.addShape(p.ShapeType.roundRect, { x, y, w: 1.7, h: 0.62, rectRadius: 0.31, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(txt, { x, y, w: 1.7, h: 0.62, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
}
function card(s, x, y, w, h, fill) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.12, fill: { color: fill || C.white }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
}

// ---- 原生分數（分子／橫線／分母直式疊字，非 "/" 斜線寫法）----
// margin:0 + wrap:false 缺一不可：預設內邊距會令長分子在框內換行、字元散開（實測踩過）。
// hh 要留 fontSize/72*1.35，太緊會令文字溢出蓋到鄰行。
function fracW(num, den, fs) {
  return Math.max(String(num).length, String(den).length) * (fs * 0.62 / 72) + 0.34;
}
function frac(s, cx, cy, num, den, size, color) {
  const fs = size || 20;
  const w = fracW(num, den, fs);
  const hh = fs / 72 * 1.35;
  s.addText(String(num), { x: cx - w / 2, y: cy - hh - 0.04, w, h: hh, margin: 0, wrap: false, align: "center", valign: "bottom", fontFace: MONO, fontSize: fs, bold: true, color: color || C.ink });
  seg(s, cx - w / 2 + 0.08, cy, cx + w / 2 - 0.08, cy, { color: color || C.ink, width: 1.5 });
  s.addText(String(den), { x: cx - w / 2, y: cy + 0.04, w, h: hh, margin: 0, wrap: false, align: "center", valign: "top", fontFace: MONO, fontSize: fs, bold: true, color: color || C.ink });
  return w;
}
// 一行內「文字／分數」混排：segs = [{t:"文字"}] 或 [{n:分子, d:分母}]
function fracRow(s, x, y, h, segs, o) {
  o = o || {};
  const fs = o.fontSize || 20, fontFace = o.fontFace || MONO, bold = o.bold !== false, color = o.color || C.ink;
  const ffs = o.fracFontSize || fs;
  const cw = fs * (fontFace === MONO ? 0.62 : 1.05) / 72;
  const cy = y + h / 2, textPad = o.textPad !== undefined ? o.textPad : 0.25;
  let cx = x;
  segs.forEach((sg) => {
    if (sg.t !== undefined) {
      const tw = sg.t.length * cw + 0.04;
      s.addText(sg.t, { x: cx, y, w: tw + textPad, h, margin: 0, wrap: false, align: "left", valign: "middle", fontFace, fontSize: fs, bold, color: sg.color || color });
      cx += tw;
    } else {
      const w = fracW(sg.n, sg.d, ffs);
      frac(s, cx + w / 2, cy, sg.n, sg.d, sg.size || ffs, sg.color || color);
      cx += w + 0.14;
    }
  });
  return cx;
}
function seg(s, x1, y1, x2, y2, o) {
  o = o || {};
  const x = Math.min(x1, x2), y = Math.min(y1, y2), w = Math.abs(x2 - x1) || 0.01, h = Math.abs(y2 - y1) || 0.01;
  const flipV = ((x2 - x1) * (y2 - y1) < 0);
  s.addShape(p.ShapeType.line, { x, y, w, h, line: { color: o.color || C.ink, width: o.width || 1.5 }, flipV });
}

let N = 0;
function newSlide(dark) { const s = p.addSlide(); bg(s, dark); N += 1; return s; }

// =====================================================================
// S1 封面
// =====================================================================
(function () {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.45, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.45, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("三種新方程", { x: 0.85, y: 2.35, w: 11.6, h: 1.1, fontFace: F, fontSize: 54, bold: true, color: C.white, align: "left" });
  s.addText("把未知數放出來", { x: 0.85, y: 3.4, w: 11.6, h: 0.9, fontFace: F, fontSize: 38, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "站① 分式方程", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "   →   ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "站② 無理方程", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "   →   ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "站③ 二元二次方程組", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.6, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 5.4, w: 8.4, h: 0.72, rectRadius: 0.1, fill: { color: "35564E" }, line: { type: "none" } });
  s.addText("三站共用同一條生死線：驗根", { x: 1.2, y: 5.4, w: 8.0, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: "E7F0EB" });
  s.addNotes("開場定調：今天學三種新方程，看似不同，其實同一個念頭——把未知數放出來。但放出來有代價，所以每一站最後都要驗根。三站節奏一致，做完一站休息一下。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "今日課堂流程");
  const rows = [
    ["站①", "分式方程", "未知數在分母裡 → 去分母 → 驗根（怕增根）"],
    ["站②", "無理方程", "未知數在根號裡 → 兩邊平方 → 驗根（怕假根）"],
    ["站③", "二元二次方程組", "兩條方程 → 代入消元 → 回代求另一個未知數"],
  ];
  let y = 1.95;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.28);
    stationBadge(s, r[0], 0.95, y + 0.33);
    s.addText(r[1], { x: 2.85, y: y + 0.14, w: 9.4, h: 0.55, fontFace: F, fontSize: 26, bold: true, color: C.ink, align: "left", valign: "middle" });
    s.addText(r[2], { x: 2.85, y: y + 0.66, w: 9.4, h: 0.5, fontFace: F, fontSize: 20, color: C.soft, align: "left", valign: "middle" });
    y += 1.5;
  });
  s.addText("每一站都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 6.5, w: 11.9, h: 0.45, fontFace: F, fontSize: 18, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖：讓學生知道整節課的結構，減少焦慮。三站的第一步都不同，但最後一步都是驗根——這句話今天要重複三次。");
})();

// =====================================================================
// S3 共同主線頁（本單元的靈魂）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "三種方程，同一個念頭", "全課主線");
  const boxes = [
    { lab: "分式方程", sub: "未知數在分母裡", segs: [{ n: "3", d: "x" }, { t: " = x - 2" }] },
    { lab: "無理方程", sub: "未知數在根號裡", txt: "√(x + 2) = x" },
    { lab: "方程組", sub: "被另一條方程綁住", txt: "y = x + 1\nx² + y² = 25" },
  ];
  const x0 = 0.65, gap = 0.3, w = (12.05 - 2 * gap) / 3;
  boxes.forEach((b, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, 1.9, w, 2.05);
    s.addShape(p.ShapeType.roundRect, { x, y: 1.9, w, h: 0.62, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(b.lab, { x: x + 0.15, y: 1.9, w: w - 0.3, h: 0.62, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
    s.addText(b.sub, { x: x + 0.15, y: 2.6, w: w - 0.3, h: 0.4, align: "center", valign: "middle", fontFace: F, fontSize: 18, color: C.soft });
    if (b.segs) fracRow(s, x + 0.85, 3.05, 0.75, b.segs, { fontFace: MONO, fontSize: 21, bold: true, color: C.ink, fracFontSize: 17 });
    else s.addText(b.txt, { x: x + 0.15, y: 3.05, w: w - 0.3, h: 0.8, align: "center", valign: "middle", fontFace: MONO, fontSize: 20, bold: true, color: C.ink, lineSpacingMultiple: 1.15 });
  });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 4.25, w: 11.7, h: 0.95, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("做法都一樣：想辦法把未知數放出來，變回會解的一元二次方程", { x: 1.15, y: 4.25, w: 11.0, h: 0.95, align: "left", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 5.4, w: 11.7, h: 1.0, rectRadius: 0.15, fill: { color: C.warnBg }, line: { color: C.warnLine, width: 1.5 } });
  s.addText([
    { text: "但放出來有代價：", options: { fontFace: F, fontSize: 22, bold: true, color: C.warnInk } },
    { text: "去分母、平方，都可能多生出「假的解」。所以三站的最後一步都是——驗根。", options: { fontFace: F, fontSize: 22, color: C.ink } },
  ], { x: 1.15, y: 5.4, w: 11.0, h: 1.0, align: "left", valign: "middle" });
  footer(s, N, false);
  s.addNotes("這一頁是全課的錨。三個方框只是「未知數被關在哪」的差別，做法同一個念頭。最後那句「放出來有代價」要講慢——它解釋了為什麼今天每題都要驗根，而不是老師囉嗦。");
})();

// =====================================================================
// 共用產生器
// =====================================================================
function stationDivider(badge, name, goal, note) {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 2.15, w: 2.4, h: 1.0, rectRadius: 0.5, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(badge, { x: 0.9, y: 2.15, w: 2.4, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.white });
  s.addText(name, { x: 3.6, y: 2.15, w: 9.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.95, y: 3.7, w: 11.4, h: 1.15, rectRadius: 0.12, fill: { color: "35564E" }, line: { type: "none" } });
  s.addText([
    { text: "目標：", options: { fontFace: F, fontSize: 24, bold: true, color: C.sage } },
    { text: goal, options: { fontFace: F, fontSize: 24, color: "E7F0EB" } },
  ], { x: 1.25, y: 3.7, w: 10.9, h: 1.15, align: "left", valign: "middle" });
  footer(s, N, true);
  s.addNotes(note);
  return s;
}

function breakSlide(msg) {
  const s = newSlide(false);
  s.addShape(p.ShapeType.roundRect, { x: 3.4, y: 2.2, w: 6.5, h: 3.0, rectRadius: 0.2, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("‖  換一換", { x: 3.4, y: 2.55, w: 6.5, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.sageDeep });
  s.addText(msg, { x: 3.7, y: 3.5, w: 5.9, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 24, color: C.ink });
  s.addText("先伸展 30 秒，再開始", { x: 3.4, y: 4.4, w: 6.5, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
  footer(s, N, false);
  s.addNotes("轉換點：起身伸展 30 秒。預告下一段做什麼，讓 ADHD/ASD 學生有準備。");
  return s;
}

// 方法頁：左「手順卡」＋右「範例」，底部易錯提醒（D2 主設計本體）
// 手順措辭逐字沿用講義的手順卡；範例照講義版面：一行一個等號、分兩支寫「或」、末行「∴」。
function methodSlide(kicker, head, howSteps, exTitle, exRows, hint, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  const yTop = 1.85, H = 4.5, bandH = 0.72, yEnd = yTop + H - 0.12;

  // ---- 左：手順卡 ----
  const lx = 0.6, lw = 5.6;
  card(s, lx, yTop, lw, H, C.white);
  s.addShape(p.ShapeType.roundRect, { x: lx, y: yTop, w: lw, h: bandH, rectRadius: 0.12, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("手順卡 · 照住做", { x: lx, y: yTop, w: lw, h: bandH, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white });
  let ly = yTop + bandH + 0.16;
  const lRowH = (yEnd - ly) / howSteps.length;
  howSteps.forEach((st, i) => {
    stepCircle(s, lx + 0.25, ly + (lRowH - 0.46) / 2, i + 1, 0.46);
    s.addText(st, { x: lx + 0.85, y: ly, w: lw - 1.1, h: lRowH, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
    ly += lRowH;
  });

  // ---- 右：範例（左算式／右說明）----
  const rx = 6.45, rw = 6.3;
  card(s, rx, yTop, rw, H, C.white);
  s.addShape(p.ShapeType.roundRect, { x: rx, y: yTop, w: rw, h: bandH, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("範例：解", { x: rx + 0.25, y: yTop, w: 1.15, h: bandH, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white });
  if (Array.isArray(exTitle)) {
    fracRow(s, rx + 1.4, yTop, bandH, exTitle, { fontFace: MONO, fontSize: 20, bold: true, color: C.white, fracFontSize: 15 });
  } else {
    s.addText(exTitle, { x: rx + 1.4, y: yTop, w: rw - 1.6, h: bandH, align: "left", valign: "middle", fontFace: MONO, fontSize: 20, bold: true, color: C.white });
  }
  let ry = yTop + bandH + 0.14;
  const rRowH = (yEnd - ry) / exRows.length;
  exRows.forEach((row, i) => {
    if (i % 2 === 1) s.addShape(p.ShapeType.rect, { x: rx + 0.13, y: ry, w: rw - 0.26, h: rRowH, fill: { color: C.block }, line: { type: "none" } });
    if (Array.isArray(row[0])) {
      fracRow(s, rx + 0.3, ry, rRowH, row[0], { fontFace: MONO, fontSize: 19, bold: true, color: C.ink, fracFontSize: 14 });
    } else {
      s.addText(row[0], { x: rx + 0.3, y: ry, w: 3.95, h: rRowH, align: "left", valign: "middle", fontFace: MONO, fontSize: 19, bold: true, color: C.ink });
    }
    s.addText(row[1], { x: rx + 4.35, y: ry, w: 1.75, h: rRowH, align: "left", valign: "middle", fontFace: F, fontSize: 18, color: C.soft });
    ry += rRowH;
  });

  s.addText(hint, { x: 0.6, y: 6.5, w: 12.15, h: 0.45, fontFace: F, fontSize: 18, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}

// D14 錯誤分析對比頁：左「常見寫法」／右「正確寫法」，逐步橫向對齊。
// 規範：正確欄視覺權重更重（灰底＋粗邊＋陰影）；只標一個分歧步驟；左欄必須是真實高頻錯誤。
function contrastSlide(kicker, head, titleSegs, rows, diffNote, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.7, y: 1.72, w: 11.95, h: 0.8, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText("題目：解", { x: 1.0, y: 1.72, w: 1.3, h: 0.8, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
  fracRow(s, 2.3, 1.72, 0.8, titleSegs, { fontFace: MONO, fontSize: 21, bold: true, color: C.ink, fracFontSize: 16 });

  const yTop = 2.68, H = 3.5, bandH = 0.6;
  const lx = 0.7, lw = 5.85, rx = 6.8, rw = 5.85;
  s.addShape(p.ShapeType.roundRect, { x: lx, y: yTop, w: lw, h: H, rectRadius: 0.12, fill: { color: C.white }, line: { color: C.warnLine, width: 1 } });
  s.addShape(p.ShapeType.roundRect, { x: lx, y: yTop, w: lw, h: bandH, rectRadius: 0.12, fill: { color: C.warnBg }, line: { type: "none" } });
  s.addText("常見寫法", { x: lx, y: yTop, w: lw, h: bandH, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.warnInk });
  s.addShape(p.ShapeType.roundRect, { x: rx, y: yTop, w: rw, h: H, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.sageDeep, width: 2.5 }, shadow: sh() });
  s.addShape(p.ShapeType.roundRect, { x: rx, y: yTop, w: rw, h: bandH, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("正確寫法", { x: rx, y: yTop, w: rw, h: bandH, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white });

  let y = yTop + bandH + 0.12;
  const rowH = (yTop + H - 0.14 - y) / rows.length;
  rows.forEach((r) => {
    if (r.diff) s.addShape(p.ShapeType.rect, { x: rx + 0.1, y: y, w: rw - 0.2, h: rowH, fill: { color: C.block2 }, line: { type: "none" } });
    if (r.l) s.addText(r.l, { x: lx + 0.3, y, w: lw - 0.55, h: rowH, align: "left", valign: "middle", fontFace: r.lm === false ? F : MONO, fontSize: 19, bold: true, color: C.ink });
    s.addText((r.diff ? "※ " : "") + r.r, { x: rx + 0.3, y, w: rw - 0.55, h: rowH, align: "left", valign: "middle", fontFace: r.rm === false ? F : MONO, fontSize: 20, bold: true, color: r.diff ? C.sageDeep : C.ink, lineSpacingMultiple: 1.1 });
    y += rowH;
  });

  s.addShape(p.ShapeType.roundRect, { x: 0.7, y: 6.35, w: 11.95, h: 0.62, rectRadius: 0.1, fill: { color: C.warnBg }, line: { color: C.warnLine, width: 1 } });
  s.addText("※ 差在這裡：" + diffNote, { x: 1.0, y: 6.35, w: 11.4, h: 0.62, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.warnInk });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}

// 分層任務頁（三欄同版面，星星分層）＋ D12 自我核對條
// cols[i] = { q: 題目（字串或 fracRow segs 陣列，自動換行）, hints: [提示…] }
// ⚠ 題目區與提示區用**固定分區**，不要讓多行題目把後面的項目往下推——
//    舊寫法每項固定 +0.72，三行題目會直接疊到下一項身上（QA 實測 p.8 糊成一團）。
function tieredTasks(kicker, cols, noteKey) {
  const s = newSlide(false);
  title(s, "挑戰練習 · 自選星星", kicker);
  const tiers = [{ t: "練習 A", star: "★☆☆" }, { t: "練習 B", star: "★★☆" }, { t: "練習 C", star: "★★★" }];
  const x0 = 0.65, gap = 0.28, w = (12.1 - 2 * gap) / 3, yTop = 1.9, h = 3.62;
  const qTop = yTop + 1.0, qH = 1.35, hTop = yTop + 2.45, hH = 0.55;
  tiers.forEach((ti, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x: x, y: yTop, w: w, h: 0.9, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(ti.t, { x: x + 0.2, y: yTop + 0.06, w: w - 0.4, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(ti.star, { x: x + 0.2, y: yTop + 0.46, w: w - 0.4, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.starInk });
    // 題目區（固定高，內容自己 wrap）
    const col = cols[i];
    if (Array.isArray(col.q)) {
      fracRow(s, x + 0.24, qTop, 0.62, col.q, { fontFace: MONO, fontSize: 18, bold: true, color: C.ink, fracFontSize: 13 });
    } else {
      s.addText(col.q, { x: x + 0.24, y: qTop, w: w - 0.46, h: qH, align: "left", valign: "top", fontFace: F, fontSize: 19, color: C.ink, lineSpacingMultiple: 1.25 });
    }
    // 提示區（固定起點，不受題目長度影響）
    col.hints.forEach((t, j) => {
      s.addText("· " + t, { x: x + 0.24, y: hTop + j * hH, w: w - 0.46, h: hH, align: "left", valign: "middle", fontFace: F, fontSize: 18, color: C.soft, lineSpacingMultiple: 1.15 });
    });
  });
  s.addShape(p.ShapeType.roundRect, { x: 0.65, y: 5.68, w: 12.1, h: 0.7, rectRadius: 0.1, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText("交卷前自己核對：☐ 每步都寫低　☐ 每個解都驗過根　☐ 捨去的有寫理由　☐ 最後一行有「∴」", { x: 1.0, y: 5.68, w: 11.5, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.ink });
  s.addText("做得起 A，就往 B、C 跳一層 ↗   全部同一個概念，只是鷹架不同", { x: 0.65, y: 6.48, w: 12.1, h: 0.45, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(noteKey);
  return s;
}

function summarySlide(kicker, takeaway, floor) {
  const s = newSlide(false);
  title(s, "帶走一句話", kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 2.15, w: 11.7, h: 1.7, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText(takeaway, { x: 1.2, y: 2.15, w: 10.9, h: 1.7, align: "left", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 4.15, w: 11.7, h: 1.5, rectRadius: 0.15, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "至少要記得：", options: { fontFace: F, fontSize: 22, bold: true, color: C.sageDeep } },
    { text: floor, options: { fontFace: F, fontSize: 24, color: C.ink } },
  ], { x: 1.2, y: 4.15, w: 10.9, h: 1.5, align: "left", valign: "middle" });
  footer(s, N, false);
  return s;
}

// =====================================================================
// 站① 分式方程
// =====================================================================
stationDivider("站①", "分式方程", "未知數在分母裡：去分母，然後一定要驗根",
  "進入站①。先問：分母有 x 跟分母冇 x，解法一唔一樣？帶出「去分母」這個動作。");

(function () {
  const s = newSlide(false);
  title(s, "哪一條是「分式方程」？", "站① · 引入");
  const data = [
    { segs: [{ n: "3", d: "x" }, { t: " = x - 2" }], yes: true, why: "分母有 x" },
    { segs: [{ n: "x", d: "2" }, { t: " + 1 = 5" }], yes: false, why: "分母是數字，不是分式方程" },
    { segs: [{ n: "1", d: "x - 1" }, { t: " = " }, { n: "3", d: "x + 2" }], yes: true, why: "兩邊分母都有 x" },
    { txt: "x² - 5x + 6 = 0", yes: false, why: "沒有分母，是一般的一元二次方程" },
  ];
  // 卡高與步進要留夠底部提示的位（QA 實測：1.12 高＋1.25 步進會令第 4 張壓到提示條）
  let y = 1.85;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.05);
    s.addShape(p.ShapeType.ellipse, { x: 0.95, y: y + 0.27, w: 0.5, h: 0.5, fill: { color: d.yes ? C.sageDeep : "B9B0A2" }, line: { type: "none" } });
    s.addText(d.yes ? "✓" : "✗", { x: 0.95, y: y + 0.27, w: 0.5, h: 0.5, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
    if (d.segs) fracRow(s, 1.75, y, 1.05, d.segs, { fontFace: MONO, fontSize: 21, bold: true, color: C.ink, fracFontSize: 16 });
    else s.addText(d.txt, { x: 1.75, y, w: 5.0, h: 1.05, align: "left", valign: "middle", fontFace: MONO, fontSize: 21, bold: true, color: C.ink });
    s.addText(d.why, { x: 7.3, y, w: 5.1, h: 1.05, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.18;
  });
  s.addText("判斷關鍵：分母裡面有沒有未知數", { x: 0.7, y: 6.52, w: 11.9, h: 0.45, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("四選二。重點是第二條——分母是數字的不算分式方程，這是最常見的混淆。讓學生講出判斷理由，不只是選。");
})();

methodSlide("站① · 方法", "分式方程 四步", [
  "把每個分母因式分解，\n找出最簡公分母",
  "兩邊同乘最簡公分母，去分母",
  "解這條整式方程",
  "驗根：把每個解代回原方程的分母",
], [{ n: "3", d: "x" }, { t: " = x - 2" }], [
  [[{ n: "3", d: "x" }, { t: " = x - 2" }], "原方程"],
  ["3 = x(x - 2)", "去分母"],
  ["x² - 2x - 3 = 0", "展開移項"],
  ["(x - 3)(x + 1) = 0", "因式分解"],
  ["x₁ = 3　或　x₂ = -1", "分兩支"],
  ["∴ x₁ = 3　或　x₂ = -1", "驗根後作答"],
], "※ 分母算出來是 0 的，叫增根，一定要捨去",
  "左邊手順卡逐字同講義。右邊範例照講義版面：一行一個等號、因式分解後分兩支寫「或」、最後一行「∴」。注意因式的左右次序要跟 x₁／x₂ 對得上（左支 x-3=0 → x₁=3）。這題兩根都合格，先建立信心；下一頁才給會捨根的。");

contrastSlide("站① · 最容易錯的一步", "同一題，兩種寫法",
  [{ n: "2", d: "x - 3" }, { t: " = " }, { n: "x - 1", d: "x - 3" }], [
  { l: "兩邊乘 (x - 3)", r: "兩邊乘 (x - 3)" },
  { l: "2 = x - 1", r: "2 = x - 1" },
  { l: "x = 3", r: "x = 3" },
  { l: "答：x = 3", r: "驗根：x = 3 令分母為 0", diff: true, rm: false },
  { l: "", r: "∴ 原方程無解" },
], "解出來的數字一定要代回分母檢查。令分母等於 0 的數叫「增根」，它不是原方程的解。",
  "D14 錯誤分析對比。先只放左欄，問學生「這樣做啱唔啱」——多數會覺得啱。再揭右欄。強調前三行一模一樣，分歧只在第四行。不要罵錯，要讓學生自己指出分歧點在哪一行。");

tieredTasks("站① · 分式方程", [
  { q: [{ n: "4", d: "x" }, { t: " = x - 3" }], hints: ["步驟號已印在練習紙", "填空式，跟住四步走"] },
  { q: [{ n: "x", d: "x-2" }, { t: " - " }, { n: "3", d: "x" }, { t: " = 1" }], hints: ["自己找最簡公分母", "留意：這題只有一個解"] },
  { q: "應用題：30 公里，單車比開車多用 1 小時，開車快 3 倍，求單車速度", hints: ["先寫「設……」", "答案要寫單位"] },
], "A 是練習紙第 1 題、B 是第 4 題、C 是第 7 題。巡堂重點：有沒有寫驗根那一行。做完提醒對自我核對清單。");

summarySlide("站① · 總結", "分式方程：去分母之後，一定要回頭看分母",
  "解出來的數，代回分母。分母變 0 的那個，捨去。");

breakSlide("下一站：未知數躲在根號裡");

// =====================================================================
// 站② 無理方程
// =====================================================================
stationDivider("站②", "無理方程", "未知數在根號裡：兩邊平方，然後一定要驗根",
  "進入站②。問：根號裡面的 x 點樣拿出來？帶出「平方」這個動作。跟站①對照——動作不同，但都要驗根。");

(function () {
  const s = newSlide(false);
  title(s, "為什麼平方之後會多出「假的解」？", "站② · 概念");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.85, w: 11.7, h: 1.05, rectRadius: 0.12, fill: { color: C.block }, line: { type: "none" } });
  s.addText("先看一條簡單的：", { x: 1.15, y: 1.85, w: 3.0, h: 1.05, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  s.addText("2 = -2　是錯的", { x: 4.3, y: 1.85, w: 8.0, h: 1.05, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });

  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 3.05, w: 11.7, h: 1.05, rectRadius: 0.12, fill: { color: C.warnBg }, line: { color: C.warnLine, width: 1.5 } });
  s.addText("但兩邊一平方：", { x: 1.15, y: 3.05, w: 3.0, h: 1.05, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.warnInk });
  s.addText("2² = (-2)²　→　4 = 4　變成對的了", { x: 4.3, y: 3.05, w: 8.0, h: 1.05, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });

  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 4.4, w: 11.7, h: 1.15, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("平方會把「本來不相等」變成「相等」——所以平方之後多出來的解，未必是原方程的解", { x: 1.2, y: 4.4, w: 10.9, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });

  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 5.75, w: 11.7, h: 0.62, rectRadius: 0.1, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText("還有一件事：根號算出來一定不是負數。右邊是負數的，一定捨。", { x: 1.2, y: 5.75, w: 10.9, h: 0.62, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("這一頁回答學生一定會問的「點解要驗根」。用 2 = -2 這個極簡例子，比講「不可逆運算」有效得多。最後一行給一個快速判斷法：右邊負數直接捨，不用代入。");
})();

methodSlide("站② · 方法", "無理方程 四步", [
  "移項，讓根號單獨留在一邊",
  "兩邊平方，去根號",
  "解這條整式方程",
  "驗根：把每個解代回原方程",
], "√(x + 2) = x", [
  ["√(x + 2) = x", "原方程"],
  ["x + 2 = x²", "兩邊平方"],
  ["x² - x - 2 = 0", "移項"],
  ["(x - 2)(x + 1) = 0", "因式分解"],
  ["x₁ = 2　或　x₂ = -1", "分兩支"],
  ["x = 2：左 √4 = 2，右 2", "相等，保留"],
  ["x = -1：左 √1 = 1，右 -1", "不等，捨去"],
  ["∴ x = 2", "作答"],
], "※ 右邊是負數的時候，根號一定追不上——直接捨",
  "這題天然示範捨根。驗根兩行要慢慢講：左邊右邊各自算一次，再比較。強調捨去的時候要寫理由，唔係寫個「捨」字就算。");

tieredTasks("站② · 無理方程", [
  { q: "√(x + 3) = x - 3", hints: ["驗根格已經印好", "一定有一個要捨"] },
  { q: "√(2x + 1) = x - 1", hints: ["自己寫驗根那兩行", "留意 x = 0 要唔要捨"] },
  { q: "找錯題：小美解 √(x+6) = x，算到 x = 3 或 x = -2 就收工", hints: ["她漏了哪一步？", "寫出正確完整過程"] },
], "A 是練習紙第 2 題、B 是第 5 題、C 是第 8 題。C 的找錯題可以叫學生兩人一組討論再答——講得出「漏了驗根」比自己做啱更重要。");

summarySlide("站② · 總結", "無理方程：平方之後，一定要代回原方程對一對",
  "左邊右邊各自算一次。不相等的那個，捨去。");

breakSlide("最後一站：兩條方程一齊解");

// =====================================================================
// 站③ 二元二次方程組
// =====================================================================
stationDivider("站③", "二元二次方程組", "兩條方程兩個未知數：代入消元，記得回代",
  "進入站③。這一站不用驗根（冇去分母亦冇平方），但有另一個容易漏的動作——回代求另一個未知數。");

methodSlide("站③ · 方法", "二元二次方程組 四步", [
  "找出那條一次方程",
  "從一次方程解出一個未知數",
  "代入二次方程，解出第一個未知數",
  "每個解都要回代，\n求出另一個未知數",
], "y = x + 1　與　x² + y² = 25", [
  ["y = x + 1　（一次）", "已解好 y"],
  ["x² + (x + 1)² = 25", "代入二次"],
  ["2x² + 2x - 24 = 0", "展開整理"],
  ["x² + x - 12 = 0", "除以 2"],
  ["(x - 3)(x + 4) = 0", "因式分解"],
  ["x₁ = 3　或　x₂ = -4", "分兩支"],
  ["y₁ = 4　或　y₂ = -3", "回代 y = x+1"],
  ["∴ (3, 4) 或 (-4, -3)", "成對寫"],
], "※ 有幾個 x，就有幾對 (x, y)——回代那一步最容易漏",
  "重點在最後兩行。好多學生解出 x 就收工，唔記得求 y。強調答案的形式係「一對數」，唔係一個數。可以問：如果只寫 x = 3，這個點在哪裡？");

(function () {
  const s = newSlide(false);
  title(s, "解出 x 之後，還未做完", "站③ · 最容易漏的一步");
  const rows = [
    { l: "x₁ = 3", m: "回代 y = x + 1", r: "y₁ = 4", pair: "(3, 4)" },
    { l: "x₂ = -4", m: "回代 y = x + 1", r: "y₂ = -3", pair: "(-4, -3)" },
  ];
  let y = 2.1;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.35);
    s.addText(r.l, { x: 1.1, y, w: 2.0, h: 1.35, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });
    s.addText("→", { x: 3.1, y, w: 0.6, h: 1.35, align: "center", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.sage });
    s.addText(r.m, { x: 3.8, y, w: 3.2, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    s.addText(r.r, { x: 7.1, y, w: 2.0, h: 1.35, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });
    s.addText("→", { x: 9.1, y, w: 0.6, h: 1.35, align: "center", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.sage });
    s.addShape(p.ShapeType.roundRect, { x: 9.8, y: y + 0.3, w: 2.5, h: 0.75, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
    s.addText(r.pair, { x: 9.8, y: y + 0.3, w: 2.5, h: 0.75, align: "center", valign: "middle", fontFace: MONO, fontSize: 22, bold: true, color: C.sageDeep });
    y += 1.55;
  });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 5.3, w: 11.7, h: 1.05, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("方程組的答案是「一對數」，不是一個數。有幾個 x，就要交幾對。", { x: 1.2, y: 5.3, w: 10.9, h: 1.05, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  footer(s, N, false);
  s.addNotes("視覺化回代流程。兩行結構完全一樣，讓學生睇到「每個 x 都要行同一條路」。最後強調答案形式。");
})();

tieredTasks("站③ · 二元二次方程組", [
  { q: "y = x - 1\nx² + y² = 13", hints: ["代入式已寫好", "記得回代求 y"] },
  { q: "x + y = 5\nxy = 6", hints: ["先從一次方程解出 y", "用代入消元就夠"] },
  { q: "自己出一條分式方程，要有一個增根要捨", hints: ["寫出完整解法", "解釋點解要捨"] },
], "A 是練習紙第 3 題、B 是第 6 題、C 是第 9 題。C 回到分式方程，是全課的收束——能自己造一個增根，代表真係明白增根係乜。");

summarySlide("站③ · 總結", "方程組：解出 x 只做了一半，回代求 y 才完整",
  "答案要成對寫：(x, y)。有幾個 x 就有幾對。");

// =====================================================================
// 收束：決策表 ＋ 驗根總表 ＋ 三句
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "看到什麼，就用哪一張卡", "全課收束 · 決策表");
  const rows = [
    ["分母裡有未知數", "分式方程 四步", "去分母 → 驗根（怕增根）"],
    ["未知數被關在根號裡", "無理方程 四步", "兩邊平方 → 驗根（怕假根）"],
    ["兩條方程、兩個未知數", "方程組 四步", "代入消元 → 回代求另一個"],
  ];
  s.addShape(p.ShapeType.roundRect, { x: 0.7, y: 1.9, w: 11.9, h: 0.72, rectRadius: 0.1, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("方程長成這樣", { x: 1.05, y: 1.9, w: 4.1, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.white });
  s.addText("就翻這張卡", { x: 5.4, y: 1.9, w: 3.0, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.white });
  s.addText("最後一步是什麼", { x: 8.6, y: 1.9, w: 3.7, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.white });
  let y = 2.78;
  rows.forEach((r, i) => {
    card(s, 0.7, y, 11.9, 1.12, i % 2 ? C.block : C.white);
    s.addText(r[0], { x: 1.05, y, w: 4.2, h: 1.12, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    s.addText(r[1], { x: 5.4, y, w: 3.1, h: 1.12, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
    s.addText(r[2], { x: 8.6, y, w: 3.8, h: 1.12, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.soft });
    y += 1.25;
  });
  s.addText("三張卡都在《工具卡》上，剪下來放喺枱面，做題時手指指住做緊嗰一步", { x: 0.7, y: 6.5, w: 11.9, h: 0.45, fontFace: F, fontSize: 18, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("決策表取代「四句條列」。學生真正需要的是「睇到乜→做乜」，唔係背三套流程。提醒工具卡的存在同用法（手指跟蹤）。");
})();

(function () {
  const s = newSlide(false);
  title(s, "驗根：三種方程各自怎麼驗", "全課收束 · 驗根總表");
  const rows = [
    ["分式方程", "把解代入原方程的分母", "分母算出來是 0 → 增根，捨去"],
    ["無理方程", "把解代入原方程，左右各算一次", "左右不相等 → 假根，捨去"],
    ["方程組", "把每一對 (x, y) 代入兩條方程", "兩條都成立才算對"],
  ];
  let y = 1.95;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.32);
    s.addShape(p.ShapeType.roundRect, { x: 0.95, y: y + 0.3, w: 2.35, h: 0.72, rectRadius: 0.1, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(r[0], { x: 0.95, y: y + 0.3, w: 2.35, h: 0.72, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
    s.addText(r[1], { x: 3.55, y, w: 4.6, h: 1.32, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
    s.addText(r[2], { x: 8.3, y, w: 4.1, h: 1.32, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.soft });
    y += 1.48;
  });
  s.addShape(p.ShapeType.roundRect, { x: 0.7, y: 6.28, w: 11.9, h: 0.7, rectRadius: 0.1, fill: { color: C.warnBg }, line: { color: C.warnLine, width: 1 } });
  s.addText("※ 捨去的時候要寫明理由，不要只寫一個「捨」字", { x: 1.05, y: 6.28, w: 11.4, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.warnInk });
  footer(s, N, false);
  s.addNotes("這是全課最該貼堂的一頁。三行對照，學生一眼睇到「驗根」喺三種方程裡具體做乜動作。最後一行係評分要求：寫理由。");
})();

(function () {
  const s = newSlide(true);
  s.addText("今日帶走三句", { x: 0.85, y: 1.2, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: C.white, align: "left" });
  const lines = [
    "① 三種方程，同一個念頭：把未知數放出來",
    "② 放出來有代價：去分母、平方，都可能多生出假的解",
    "③ 所以最後一步永遠是——驗根，而且要寫低理由",
  ];
  let y = 2.5;
  lines.forEach((t) => {
    s.addShape(p.ShapeType.roundRect, { x: 0.9, y, w: 11.5, h: 1.1, rectRadius: 0.12, fill: { color: "35564E" }, line: { type: "none" } });
    s.addText(t, { x: 1.3, y, w: 10.8, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: "E7F0EB" });
    y += 1.3;
  });
  s.addText("功課：練習紙 A / B / C，做得起就往上跳一層", { x: 0.9, y: 6.5, w: 11.5, h: 0.5, fontFace: F, fontSize: 20, color: "9FB8AE", align: "left" });
  footer(s, N, true);
  s.addNotes("收束。三句話對應三站，但主線係同一條。功課提醒：自選層級，做得起就跳。");
})();

p.writeFile({ fileName: "簡報_分式無理方程與二元二次方程組_融合抽離版.pptx" }).then((fn) => {
  console.log("已輸出：" + fn + "（共 " + N + " 頁）");
});
