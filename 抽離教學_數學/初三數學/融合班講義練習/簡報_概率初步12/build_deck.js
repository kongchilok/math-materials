// 融合抽離小組 SOIL 教學簡報：概率初步（初三）— 三課時三站
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。統計圖表原生繪製。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "概率初步 三站通關（融合抽離版）";

// ---- 配色 (Sage Calm 低刺激) ----
const C = {
  bgLight: "EDF3F0", bgDark: "2E4A43", ink: "233A34", soft: "5C6F68",
  sage: "6FA48C", sageDeep: "4E8770", slate: "50808E",
  block: "DCEAE3", block2: "CFE0D8", cardLine: "B9CFC5",
  grid: "D3E1DA", white: "FFFFFF", starInk: "2E4A43",
};
const F = "Microsoft JhengHei";

// ---- 共用小工具 ----
function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("初三數學 · 概率初步（抽離小組·融合版）", {
    x: 0.5, y: 7.06, w: 9.5, h: 0.32, align: "left", valign: "middle",
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
function hlBox(s, x, y, w, h) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: C.block }, line: { type: "none" } });
}
// 直線段：由 (x1,y1)→(x2,y2)，自動處理 flipV
function seg(s, x1, y1, x2, y2, o) {
  o = o || {};
  const x = Math.min(x1, x2), y = Math.min(y1, y2), w = Math.abs(x2 - x1), h = Math.abs(y2 - y1);
  const flipV = ((x2 - x1) * (y2 - y1) < 0);
  s.addShape(p.ShapeType.line, {
    x, y, w, h, flipV,
    line: { color: o.color || C.ink, width: o.width || 1.5, dashType: o.dash || "solid",
      beginArrowType: o.begin || "none", endArrowType: o.end || "none" },
  });
}
function dot(s, X, Y, color, d) {
  const dia = d || 0.14;
  s.addShape(p.ShapeType.ellipse, { x: X - dia / 2, y: Y - dia / 2, w: dia, h: dia, fill: { color: color || C.sageDeep }, line: { type: "none" } });
}
// 分數（直式：分子／橫線／分母），置中於 (cx, cy)
function frac(s, cx, cy, num, den, size, color) {
  const fs = size || 26, w = 1.0, hh = fs / 72 * 1.25;
  s.addText(num, { x: cx - w / 2, y: cy - hh - 0.03, w, h: hh, align: "center", valign: "bottom", fontFace: F, fontSize: fs, bold: true, color: color || C.ink });
  seg(s, cx - 0.3, cy, cx + 0.3, cy, { color: color || C.ink, width: 1.75 });
  s.addText(den, { x: cx - w / 2, y: cy + 0.03, w, h: hh, align: "center", valign: "top", fontFace: F, fontSize: fs, bold: true, color: color || C.ink });
}

let N = 0;
function newSlide(dark) { const s = p.addSlide(); bg(s, dark); N += 1; return s; }

// =====================================================================
// 原生圖形
// =====================================================================
// 概率數線：0 —— 1，標不可能／隨機／必然
function probLineFig(s, x0, y0, w) {
  const x1 = x0 + w;
  seg(s, x0, y0, x1, y0, { color: C.soft, width: 2.5 });
  [[0, "0", "不可能事件"], [0.5, "", ""], [1, "1", "必然事件"]].forEach(t => {
    const X = x0 + t[0] * w;
    seg(s, X, y0 - 0.14, X, y0 + 0.14, { color: C.soft, width: 2.5 });
    if (t[1]) {
      s.addText(t[1], { x: X - 0.5, y: y0 + 0.16, w: 1.0, h: 0.4, align: "center", fontFace: F, fontSize: 24, bold: true, color: C.ink });
      s.addText(t[2], { x: X - 1.3, y: y0 + 0.62, w: 2.6, h: 0.4, align: "center", fontFace: F, fontSize: 20, color: C.sageDeep });
    }
  });
  // 中段標「隨機事件」
  s.addShape(p.ShapeType.roundRect, { x: x0 + w * 0.24, y: y0 - 0.72, w: w * 0.52, h: 0.52, rectRadius: 0.26, fill: { color: C.block2 }, line: { type: "none" } });
  s.addText("隨機事件（0 和 1 之間）", { x: x0 + w * 0.24, y: y0 - 0.72, w: w * 0.52, h: 0.52, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink });
}
// 摸球袋：3 紅 2 白（球內寫字，不靠顏色辨識）
function bagFig(s, cx, cy) {
  s.addShape(p.ShapeType.roundRect, { x: cx - 1.75, y: cy - 1.05, w: 3.5, h: 2.1, rectRadius: 0.5, fill: { color: C.white }, line: { color: C.soft, width: 2 } });
  const balls = [["紅", 1], ["紅", 1], ["紅", 1], ["白", 0], ["白", 0]];
  balls.forEach((b, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const bx = cx - 1.15 + col * 0.82 + (row === 1 ? 0.41 : 0);
    const by = cy - 0.52 + row * 0.86;
    s.addShape(p.ShapeType.ellipse, { x: bx - 0.31, y: by - 0.31, w: 0.62, h: 0.62,
      fill: { color: b[1] ? C.sageDeep : C.white }, line: { color: C.ink, width: 1.5 } });
    s.addText(b[0], { x: bx - 0.31, y: by - 0.31, w: 0.62, h: 0.62, align: "center", valign: "middle",
      fontFace: F, fontSize: 18, bold: true, color: b[1] ? C.white : C.ink });
  });
}
// 樹狀圖：拋兩枚硬幣
function treeFig(s, x0, y0) {
  const xA = x0, xB = x0 + 1.9, xC = x0 + 3.9, xL = x0 + 5.0;
  const yMid = y0 + 1.75;
  const y1 = y0 + 0.85, y2 = y0 + 2.65;                 // 第一層分支點
  const leaf = [y0 + 0.35, y0 + 1.35, y0 + 2.15, y0 + 3.15];
  s.addText("第一枚", { x: xB - 0.9, y: y0 - 0.55, w: 1.8, h: 0.36, align: "center", fontFace: F, fontSize: 18, bold: true, color: C.sageDeep });
  s.addText("第二枚", { x: xC - 0.9, y: y0 - 0.55, w: 1.8, h: 0.36, align: "center", fontFace: F, fontSize: 18, bold: true, color: C.sageDeep });
  s.addText("結果", { x: xL - 0.1, y: y0 - 0.55, w: 1.6, h: 0.36, align: "left", fontFace: F, fontSize: 18, bold: true, color: C.sageDeep });
  // 第一層
  seg(s, xA, yMid, xB, y1, { color: C.ink, width: 2 });
  seg(s, xA, yMid, xB, y2, { color: C.ink, width: 2 });
  s.addText("正", { x: xA + 0.55, y: (yMid + y1) / 2 - 0.42, w: 0.6, h: 0.34, align: "center", fontFace: F, fontSize: 19, bold: true, color: C.slate });
  s.addText("反", { x: xA + 0.55, y: (yMid + y2) / 2 + 0.06, w: 0.6, h: 0.34, align: "center", fontFace: F, fontSize: 19, bold: true, color: C.slate });
  dot(s, xA, yMid, C.ink, 0.16);
  dot(s, xB, y1, C.ink, 0.16);
  dot(s, xB, y2, C.ink, 0.16);
  // 第二層
  const pairs = [[y1, leaf[0], "正", "正正"], [y1, leaf[1], "反", "正反"], [y2, leaf[2], "正", "反正"], [y2, leaf[3], "反", "反反"]];
  pairs.forEach(pr => {
    seg(s, xB, pr[0], xC, pr[1], { color: C.ink, width: 2 });
    s.addText(pr[2], { x: xB + 0.65, y: (pr[0] + pr[1]) / 2 - 0.38, w: 0.6, h: 0.34, align: "center", fontFace: F, fontSize: 19, bold: true, color: C.slate });
    dot(s, xC, pr[1], C.ink, 0.16);
    const hit = (pr[3] === "正反" || pr[3] === "反正");
    if (hit) s.addShape(p.ShapeType.roundRect, { x: xL - 0.12, y: pr[1] - 0.24, w: 1.35, h: 0.48, rectRadius: 0.1, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(pr[3] + (hit ? " ✔" : ""), { x: xL - 0.12, y: pr[1] - 0.24, w: 1.6, h: 0.48, align: "left", valign: "middle",
      fontFace: F, fontSize: 20, bold: hit, color: hit ? C.sageDeep : C.ink });
  });
}
// 兩骰之和 6×6 列表；和為 target 的格加深底
function sumTableFig(s, x0, y0, cell, target) {
  const lab = { fontFace: F, fontSize: 15, bold: true, color: C.sageDeep, align: "center", valign: "middle" };
  s.addText("第二顆 →", { x: x0 + cell, y: y0 - 0.42, w: cell * 6, h: 0.34, align: "center", fontFace: F, fontSize: 16, bold: true, color: C.sageDeep });
  s.addText("第\n一\n顆\n↓", { x: x0 - 0.52, y: y0 + cell, w: 0.45, h: cell * 6, align: "center", valign: "middle", fontFace: F, fontSize: 14, bold: true, color: C.sageDeep, lineSpacingMultiple: 0.9 });
  for (let i = 0; i <= 6; i++) {
    for (let j = 0; j <= 6; j++) {
      const x = x0 + j * cell, y = y0 + i * cell;
      if (i === 0 && j === 0) continue;
      const head = (i === 0 || j === 0);
      const val = head ? String(i === 0 ? j : i) : String(i + j);
      const hit = !head && (i + j === target);
      s.addShape(p.ShapeType.rect, { x, y, w: cell, h: cell,
        fill: { color: head ? C.block2 : (hit ? C.sageDeep : C.white) },
        line: { color: hit ? C.ink : C.cardLine, width: hit ? 2 : 1 } });
      s.addText(val, { x, y, w: cell, h: cell, align: "center", valign: "middle", fontFace: F,
        fontSize: head ? 15 : 16, bold: head || hit, color: hit ? C.white : (head ? C.sageDeep : C.ink) });
    }
  }
  void lab;
}
// 頻率趨穩折線圖：x=試驗次數，y=正面頻率，趨近 0.5
function freqFig(s, x0, y0, w, h) {
  const yBase = y0 + h;
  // 格線
  for (let k = 0; k <= 4; k++) seg(s, x0, y0 + h * k / 4, x0 + w, y0 + h * k / 4, { color: C.grid, width: 0.75 });
  // 軸
  seg(s, x0, yBase, x0 + w, yBase, { color: C.soft, width: 1.75, end: "triangle" });
  seg(s, x0, yBase, x0, y0, { color: C.soft, width: 1.75, end: "triangle" });
  // 0.5 參考線
  seg(s, x0, y0 + h * 0.5, x0 + w, y0 + h * 0.5, { color: C.sage, width: 2, dash: "dash" });
  s.addText("0.5", { x: x0 - 0.62, y: y0 + h * 0.5 - 0.17, w: 0.55, h: 0.34, align: "right", valign: "middle", fontFace: F, fontSize: 16, bold: true, color: C.sageDeep });
  s.addText("1", { x: x0 - 0.62, y: y0 - 0.17, w: 0.55, h: 0.34, align: "right", valign: "middle", fontFace: F, fontSize: 15, color: C.soft });
  s.addText("0", { x: x0 - 0.62, y: yBase - 0.17, w: 0.55, h: 0.34, align: "right", valign: "middle", fontFace: F, fontSize: 15, color: C.soft });
  // 資料（前段震盪、後段趨穩）
  const vals = [0.20, 0.75, 0.40, 0.65, 0.44, 0.58, 0.47, 0.545, 0.485, 0.525, 0.495, 0.508, 0.50];
  const pt = i => [x0 + w * i / (vals.length - 1), yBase - h * vals[i]];
  for (let i = 0; i < vals.length - 1; i++) {
    const a = pt(i), b = pt(i + 1);
    seg(s, a[0], a[1], b[0], b[1], { color: C.slate, width: 2.25 });
  }
  vals.forEach((v, i) => { const q = pt(i); dot(s, q[0], q[1], C.slate, 0.12); void v; });
  s.addText("試驗次數 越來越多 →", { x: x0, y: yBase + 0.14, w, h: 0.36, align: "center", fontFace: F, fontSize: 17, bold: true, color: C.sageDeep });
}

// =====================================================================
// S1 封面
// =====================================================================
(function () {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.45, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.45, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("概率初步", { x: 0.85, y: 2.4, w: 11.6, h: 1.1, fontFace: F, fontSize: 52, bold: true, color: C.white, align: "left" });
  s.addText("三站通關 · 三節課", { x: 0.85, y: 3.5, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "站① 概率的意思", options: { fontFace: F, fontSize: 21, color: "E7F0EB" } },
    { text: "   →   ", options: { fontFace: F, fontSize: 21, color: C.sage } },
    { text: "站② 列表與樹狀圖", options: { fontFace: F, fontSize: 21, color: "E7F0EB" } },
    { text: "   →   ", options: { fontFace: F, fontSize: 21, color: C.sage } },
    { text: "站③ 用頻率估計", options: { fontFace: F, fontSize: 21, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.75, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 一節課一站，跟著走就到終點", { x: 0.9, y: 5.5, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, italic: true, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：概率不是靠估，是有方法數出來的。三節課三站，每站都是：學一招 → 看示範 → 自己挑星星練習。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "三節課的流程");
  const rows = [
    ["站①", "概率的意思（第 1 節）", "一定／不可能／說不準；等可能時怎樣算"],
    ["站②", "列表與樹狀圖（第 2 節）", "兩步試驗：把全部結果排好隊，再數"],
    ["站③", "用頻率估計（第 3 節）", "算不出的時候，就試很多次去估"],
  ];
  let y = 1.95;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.32);
    stationBadge(s, r[0], 0.95, y + 0.35);
    s.addText(r[1], { x: 2.85, y: y + 0.14, w: 9.4, h: 0.58, fontFace: F, fontSize: 26, bold: true, color: C.ink, align: "left", valign: "middle" });
    s.addText(r[2], { x: 2.85, y: y + 0.72, w: 9.4, h: 0.48, fontFace: F, fontSize: 20, color: C.soft, align: "left", valign: "middle" });
    y += 1.52;
  });
  s.addText("每一站都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 6.6, w: 11.9, h: 0.5, fontFace: F, fontSize: 19, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖：三節課的整體結構。今日只走一站，讓學生知道不會一次塞完，減少焦慮。");
})();

// =====================================================================
// 產生器
// =====================================================================
function stationDivider(badge, name, goal, lesson) {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 2.15, w: 2.4, h: 1.0, rectRadius: 0.5, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(badge, { x: 0.9, y: 2.15, w: 2.4, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.white });
  s.addText(name, { x: 3.6, y: 2.15, w: 9.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.white });
  s.addText(lesson, { x: 0.95, y: 1.5, w: 9.0, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: "9FB8AE" });
  s.addShape(p.ShapeType.roundRect, { x: 0.95, y: 3.7, w: 11.4, h: 1.15, rectRadius: 0.12, fill: { color: "35564E" }, line: { type: "none" } });
  s.addText([
    { text: "目標：", options: { fontFace: F, fontSize: 24, bold: true, color: C.sage } },
    { text: goal, options: { fontFace: F, fontSize: 24, color: "E7F0EB" } },
  ], { x: 1.25, y: 3.7, w: 10.9, h: 1.15, align: "left", valign: "middle" });
  footer(s, N, true);
  return s;
}
function breakSlide(msg) {
  const s = newSlide(false);
  s.addShape(p.ShapeType.roundRect, { x: 3.4, y: 2.2, w: 6.5, h: 3.0, rectRadius: 0.2, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("‖  換一換", { x: 3.4, y: 2.55, w: 6.5, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.sageDeep });
  s.addText(msg, { x: 3.7, y: 3.5, w: 5.9, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 24, color: C.ink });
  s.addText("先伸展 30 秒，再開始", { x: 3.4, y: 4.4, w: 6.5, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 20, italic: true, color: C.soft });
  footer(s, N, false);
  s.addNotes("轉換點：起身伸展 30 秒。預告下一段是自己動手做，讓 ADHD/ASD 學生有準備。");
  return s;
}
function tieredTasks(kicker, cols, note) {
  const s = newSlide(false);
  title(s, "挑戰練習 · 自選星星", kicker);
  const tiers = [
    { t: "練習 A", star: "★☆☆" },
    { t: "練習 B", star: "★★☆" },
    { t: "練習 C", star: "★★★" },
  ];
  const x0 = 0.65, gap = 0.28, w = (12.7 - 2 * gap) / 3, yTop = 1.83, h = 4.75;
  tiers.forEach((ti, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 0.9, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(ti.t, { x: x + 0.2, y: yTop + 0.06, w: w - 0.4, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(ti.star, { x: x + 0.2, y: yTop + 0.46, w: w - 0.4, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.starInk });
    // 行高依實際行數計算，避免長題目壓到下一題
    let ty = yTop + 1.02;
    cols[i].forEach((it) => {
      const lines = it.split("\n").length;
      const hh = lines * 0.322 + 0.16;
      s.addText(it, { x: x + 0.24, y: ty, w: w - 0.46, h: hh, align: "left", valign: "top", fontFace: F, fontSize: 19, color: C.ink, lineSpacingMultiple: 1.22 });
      ty += hh + 0.30;
    });
  });
  s.addText("做得起 A，就往 B、C 跳一層 ↗   全部同一個概念，只是鷹架不同", { x: 0.65, y: 6.64, w: 12.7, h: 0.42, fontFace: F, fontSize: 17, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(note);
  return s;
}
function summarySlide(kicker, takeaway, floor) {
  const s = newSlide(false);
  title(s, "帶走一句話", kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 2.15, w: 11.7, h: 1.7, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText(takeaway, { x: 1.2, y: 2.15, w: 10.9, h: 1.7, align: "left", valign: "middle", fontFace: F, fontSize: 28, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 4.15, w: 11.7, h: 1.5, rectRadius: 0.15, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "至少要記得：", options: { fontFace: F, fontSize: 22, bold: true, color: C.sageDeep } },
    { text: floor, options: { fontFace: F, fontSize: 24, color: C.ink } },
  ], { x: 1.2, y: 4.15, w: 10.9, h: 1.5, align: "left", valign: "middle" });
  footer(s, N, false);
  return s;
}
function stepCardSlide(kicker, head, topLabel, steps, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.75, w: 11.7, h: 0.9, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText(topLabel, { x: 1.1, y: 1.75, w: 11.1, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  let y = 2.95;
  const rowH = (6.4 - 2.95) / steps.length;
  steps.forEach((st, i) => {
    stepCircle(s, 0.85, y + (rowH - 0.5) / 2, i + 1, 0.5);
    s.addText(st, { x: 1.55, y: y, w: 10.9, h: rowH, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    y += rowH;
  });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}
// 迷思澄清頁：❌ 錯誤想法 vs ✅ 正確理解
function mythSlide(kicker, head, wrongTitle, wrongBody, rightTitle, rightBody, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  const w = 5.85, y = 1.95, h = 4.2;
  card(s, 0.7, y, w, h, C.white);
  s.addShape(p.ShapeType.roundRect, { x: 0.7, y, w, h: 0.85, rectRadius: 0.12, fill: { color: "D9D9D4" }, line: { type: "none" } });
  s.addText("✗  " + wrongTitle, { x: 0.95, y, w: w - 0.5, h: 0.85, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: "4A4A46" });
  s.addText(wrongBody, { x: 0.98, y: y + 1.02, w: w - 0.55, h: h - 1.2, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.3 });
  const x2 = 0.7 + w + 0.35;
  card(s, x2, y, w, h, C.white);
  s.addShape(p.ShapeType.roundRect, { x: x2, y, w, h: 0.85, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
  s.addText("✓  " + rightTitle, { x: x2 + 0.25, y, w: w - 0.5, h: 0.85, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
  s.addText(rightBody, { x: x2 + 0.28, y: y + 1.02, w: w - 0.55, h: h - 1.2, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.3 });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}

// =====================================================================
// 站① 概率的意思（第 1 節）
// =====================================================================
stationDivider("站①", "概率的意思", "分得出三類事件，會用等可能公式算單步概率", "第 1 節課")
  .addNotes("進入站①。先建立信心：概率只是把「有多容易發生」寫成一個數字，用數的，不是靠估。");

// 引入：低門檻暖身
(function () {
  const s = newSlide(false);
  title(s, "一定？不可能？還是說不準？", "站① · 引入");
  const data = [
    ["太陽從東邊升起", "一定會發生", "必然"],
    ["擲一顆骰子出現 7 點", "一定不會發生", "不可能"],
    ["明天會下雨", "說不準", "隨機"],
    ["這個星期會放假", "說不準", "隨機"],
  ];
  let y = 2.0;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.0, d[2] === "隨機" ? C.white : C.block);
    s.addText(d[0], { x: 1.2, y: y, w: 5.4, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(d[1], { x: 6.7, y: y, w: 3.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    s.addText(d[2], { x: 10.0, y: y, w: 2.2, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    y += 1.13;
  });
  footer(s, N, false);
  s.addNotes("保底成功經驗：人人做得起。只判斷三選一，不出現任何算式。口頭補充：數學把「說不準」叫做隨機事件。");
})();

// 概念保底：三類事件 + 0–1 數線
(function () {
  const s = newSlide(false);
  title(s, "概率就是一個 0 到 1 之間的數", "站① · 概念（保底）");
  card(s, 0.8, 1.85, 11.7, 2.9, C.white);
  probLineFig(s, 2.4, 3.35, 8.5);
  const rows = [
    ["必然事件", "一定發生", "概率 = 1"],
    ["不可能事件", "一定不發生", "概率 = 0"],
    ["隨機事件", "說不準", "概率在 0 和 1 之間"],
  ];
  let y = 5.0;
  rows.forEach((r) => {
    hlBox(s, 0.85, y, 3.3, 0.52);
    s.addText(r[0], { x: 0.85, y: y, w: 3.3, h: 0.52, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 4.4, y: y, w: 3.0, h: 0.52, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.soft });
    s.addText(r[2], { x: 7.6, y: y, w: 4.9, h: 0.52, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
    y += 0.64;
  });
  footer(s, N, false);
  s.addNotes("圖像先行：先看數線，再看文字。強調概率不會是負數，也不會大過 1。手勢：左手 0、右手 1，隨機事件在中間。");
})();

// CRA 三欄：摸球
(function () {
  const s = newSlide(false);
  title(s, "從摸球，到算式", "站① · 具體 → 表徵 → 抽象");
  const cols = [
    ["具體", "真的摸一次"],
    ["表徵", "把結果排出來"],
    ["抽象", "寫成算式"],
  ];
  const w = 3.95, gap = 0.3, x0 = 0.65, yTop = 1.85, h = 4.5;
  cols.forEach((c, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 0.78, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(c[0], { x: x + 0.22, y: yTop, w: 1.4, h: 0.78, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(c[1], { x: x + 1.55, y: yTop, w: w - 1.75, h: 0.78, align: "right", valign: "middle", fontFace: F, fontSize: 19, color: C.soft });
  });
  // 具體：球袋
  bagFig(s, x0 + w / 2, yTop + 2.05);
  s.addText("袋裡 3 紅 + 2 白", { x: x0 + 0.2, y: yTop + 3.45, w: w - 0.4, h: 0.5, align: "center", fontFace: F, fontSize: 20, bold: true, color: C.ink });
  s.addText("摸一個出來", { x: x0 + 0.2, y: yTop + 3.92, w: w - 0.4, h: 0.45, align: "center", fontFace: F, fontSize: 18, color: C.soft });
  // 表徵：五個位置
  const xr = x0 + w + gap;
  ["紅", "紅", "紅", "白", "白"].forEach((t, i) => {
    const bx = xr + 0.35 + i * 0.66;
    const red = t === "紅";
    s.addShape(p.ShapeType.roundRect, { x: bx, y: yTop + 1.35, w: 0.58, h: 0.58, rectRadius: 0.1,
      fill: { color: red ? C.sageDeep : C.white }, line: { color: C.ink, width: 1.5 } });
    s.addText(t, { x: bx, y: yTop + 1.35, w: 0.58, h: 0.58, align: "center", valign: "middle", fontFace: F, fontSize: 17, bold: true, color: red ? C.white : C.ink });
  });
  s.addText("一共 5 格 = 5 種結果", { x: xr + 0.2, y: yTop + 2.15, w: w - 0.4, h: 0.45, align: "center", fontFace: F, fontSize: 19, bold: true, color: C.ink });
  s.addText("「紅」佔 3 格", { x: xr + 0.2, y: yTop + 2.72, w: w - 0.4, h: 0.45, align: "center", fontFace: F, fontSize: 20, bold: true, color: C.sageDeep });
  s.addText("每一格機會一樣大", { x: xr + 0.2, y: yTop + 3.3, w: w - 0.4, h: 0.45, align: "center", fontFace: F, fontSize: 18, italic: true, color: C.soft });
  // 抽象：公式 + 縮圖線索
  const xa = x0 + 2 * (w + gap);
  s.addText("P(紅) =", { x: xa + 0.3, y: yTop + 1.5, w: 1.9, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.ink });
  frac(s, xa + 2.55, yTop + 1.8, "3", "5", 30, C.sageDeep);
  s.addText("P(白) =", { x: xa + 0.3, y: yTop + 2.65, w: 1.9, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.ink });
  frac(s, xa + 2.55, yTop + 2.95, "2", "5", 30, C.sageDeep);
  hlBox(s, xa + 0.25, yTop + 3.55, w - 0.5, 0.75);
  s.addText("上面＝要的格數\n下面＝全部格數", { x: xa + 0.3, y: yTop + 3.55, w: w - 0.6, h: 0.75, align: "center", valign: "middle", fontFace: F, fontSize: 17, bold: true, color: C.sageDeep, lineSpacingMultiple: 1.1 });
  footer(s, N, false);
  s.addNotes("真的帶一個袋、五個球入課室，先讓學生摸。三欄由左讀到右：摸 → 排 → 寫。抽象欄底部保留「格數」字眼，接住表徵階段的視覺線索。");
})();

// 迷思澄清：等可能前提
mythSlide("站① · 迷思澄清", "「兩種結果」不等於「各佔一半」",
  "常見的想法",
  "「明天下雨或不下雨，\n兩種結果，\n所以 P(下雨) = 1/2。」\n\n「買彩票中或不中，\n所以中獎機會是一半。」",
  "要先問一句",
  "公式只在「每個結果\n機會一樣大」時才能用。\n\n下雨和不下雨機會不一樣，\n中獎和不中獎也不一樣，\n所以不能寫 1/2。",
  "這是本站最大的坎。口訣：先問「每種結果機會一樣嗎？」一樣才數格數。骰子、硬幣、摸球是一樣的；天氣、彩票不是。"
);

// 步驟卡
stepCardSlide("站① · 解題步驟卡", "求概率，三步就夠",
  "例：擲一枚均勻骰子，求出現偶數的概率。", [
  "數全部：1、2、3、4、5、6 → 一共 6 種",
  "數要的：偶數是 2、4、6 → 有 3 種",
  "寫成分數再約簡：3 ÷ 6 = 1/2",
], "一次一個步驟，寫喺黑板逐步出。強調第 1 步永遠先數「全部」，第 2 步先數「要的」——次序固定，減少工作記憶負荷。");

// 轉換點
breakSlide("下一頁換你做：挑一顆星開始");

// 分層任務 站①
tieredTasks("站① · 分層練習",
  [
    ["1. 判斷是必然／不可能／\n   隨機：\n   (1) 太陽從東邊升起\n   (2) 骰子擲出 7 點\n   (3) 明天會下雨",
     "2. 袋裡 3 紅 2 白，摸一個。\n   P(紅) = ？  P(白) = ？"],
    ["3. 擲一枚均勻骰子，求：\n   (1) P(擲出 3)\n   (2) P(點數大於 4)\n   (3) P(擲出奇數)",
     "4. 袋裡紅白球共 6 個。\n   要令 P(紅) = 1/3，\n   紅球要有幾個？"],
    ["5. 承上題：除了 6 個球，\n   還有哪些球總數可以做到\n   P(紅) = 1/3？找出規律。",
     "6. 各說一件生活中的必然、\n   不可能、隨機事件，\n   並解釋為甚麼。"],
  ],
  "解答核對｜A1: (1)必然 (2)不可能 (3)隨機。A2: P(紅)=3/5、P(白)=2/5。 B3: (1)1/6 (2)大於4是5、6兩個→2/6=1/3 (3)奇數是1、3、5→3/6=1/2。B4: 6×1/3=2，紅球2個（白4個）。 C5: 紅:總=1:3，總數要是3的倍數→3(紅1)、6(紅2)、9(紅3)、12(紅4)…。C6: 開放，只看是否分類正確並講得出理由。"
);

// 站① 總結
summarySlide("站① · 總結",
  "概率＝要的結果數 ÷ 全部結果數（每種機會要一樣大）。",
  "先數全部有幾種，再數要的有幾種，寫成分數。")
  .addNotes("回收站①。保底句要全班能覆述。下一節課會處理「兩步」的試驗，結果會多好多，所以要有方法去排。");

// =====================================================================
// 站② 列表與樹狀圖（第 2 節）
// =====================================================================
stationDivider("站②", "列表與樹狀圖", "兩步試驗會有系統列出全部結果，再求概率", "第 2 節課")
  .addNotes("進入站②。本站是整個單元的重心。賣點：結果多到數唔掂的時候，我們有兩件工具——樹狀圖和列表。");

// 引入：先估，製造認知衝突
(function () {
  const s = newSlide(false);
  title(s, "先猜一猜：拋兩枚硬幣", "站② · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.3, y: 1.95, w: 10.7, h: 1.5, rectRadius: 0.18, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("拋兩枚硬幣，「一正一反」的機會有幾大？", { x: 1.6, y: 1.95, w: 10.1, h: 1.5, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.white });
  const guesses = ["1/2", "1/3", "1/4"];
  guesses.forEach((g, i) => {
    const x = 2.35 + i * 3.1;
    card(s, x, 3.85, 2.6, 1.5, C.white);
    s.addText(g, { x, y: 3.85, w: 2.6, h: 1.5, align: "center", valign: "middle", fontFace: F, fontSize: 34, bold: true, color: C.ink });
  });
  s.addText("先舉手投票，再一齊拋 10 次看看", { x: 1.3, y: 5.65, w: 10.7, h: 0.5, align: "center", fontFace: F, fontSize: 21, italic: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("先投票再驗證：製造好奇，也讓答錯的人不覺得尷尬（人人都要猜）。真的拿兩枚硬幣拋 10 次記錄。多數人會猜 1/3——正好帶入下一頁的迷思澄清。");
})();

// 迷思澄清：3 種 vs 4 種
mythSlide("站② · 迷思澄清", "「正反」和「反正」是兩種，不是一種",
  "常見的想法",
  "「結果只有 3 種：\n  兩個正、兩個反、一正一反。\n\n 所以 P(一正一反) = 1/3。」",
  "正確的數法",
  "要分清楚是哪一枚：\n  正正、正反、反正、反反\n\n 共 4 種，「一正一反」佔 2 種，\n 所以 P = 2/4 = 1/2。",
  "關鍵：兩枚硬幣要當成有分別（第一枚、第二枚）。可以用兩隻不同顏色的硬幣，或一隻放左手一隻放右手，讓「分得出」這件事變得具體。"
);

// 表徵：樹狀圖
(function () {
  const s = newSlide(false);
  title(s, "工具一：樹狀圖", "站② · 表徵");
  card(s, 0.7, 1.8, 7.5, 4.6, C.white);
  treeFig(s, 1.35, 2.35);
  card(s, 8.5, 1.8, 4.15, 4.6, C.white);
  s.addText("怎樣畫", { x: 8.75, y: 1.95, w: 3.7, h: 0.5, align: "left", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
  const how = ["先畫第一枚：\n分成正、反兩支", "每一支再分第二枚：\n又是正、反", "數尾巴：一共 4 條", "數 ✔：一正一反有 2 條"];
  let y = 2.5;
  how.forEach((t, i) => {
    stepCircle(s, 8.75, y + 0.05, i + 1, 0.42);
    s.addText(t, { x: 9.3, y: y, w: 3.15, h: 0.8, align: "left", valign: "top", fontFace: F, fontSize: 18, color: C.ink, lineSpacingMultiple: 1.15 });
    y += 0.78;
  });
  hlBox(s, 8.75, 5.78, 3.7, 0.55);
  s.addText("P(一正一反) = 2/4 = 1/2", { x: 8.75, y: 5.78, w: 3.7, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("樹狀圖的價值：逼你有系統地分岔，就不會漏。強調「每個分岔都要問：這一步有幾種選擇」。左圖已標好 ✔ 的兩條，回應上一頁投票結果。");
})();

// 表徵：列表法
(function () {
  const s = newSlide(false);
  title(s, "工具二：列表", "站② · 表徵");
  card(s, 0.7, 1.75, 5.6, 4.75, C.white);
  sumTableFig(s, 1.55, 2.28, 0.55, 7);
  s.addText("兩顆骰子的點數之和", { x: 0.8, y: 6.12, w: 5.4, h: 0.34, align: "center", fontFace: F, fontSize: 17, bold: true, color: C.sageDeep });
  card(s, 6.6, 1.75, 6.05, 4.75, C.white);
  s.addText("結果太多的時候，用列表", { x: 6.85, y: 1.9, w: 5.6, h: 0.5, align: "left", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
  const pts = [
    "橫、直各寫 1 到 6",
    "格內填「兩個點數之和」",
    "全部格數：6 × 6 = 36 格",
    "深色格＝和為 7，一共 6 格",
  ];
  let y = 2.6;
  pts.forEach((t, i) => {
    stepCircle(s, 6.85, y, i + 1, 0.44);
    s.addText(t, { x: 7.42, y: y - 0.03, w: 5.0, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.ink });
    y += 0.78;
  });
  hlBox(s, 6.85, 5.85, 5.6, 0.55);
  s.addText("P(和為 7) = 6/36 = 1/6", { x: 6.85, y: 5.85, w: 5.6, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("列表適合「兩步、每步結果多」的情況（兩顆骰子畫樹狀圖會有 36 條尾巴，太亂）。深色格沿對角線排列，可以指出這個規律：和為 7 的格排成一條斜線。");
})();

// 步驟卡：兩步試驗
stepCardSlide("站② · 解題步驟卡", "兩步試驗，四步做完",
  "先問自己：這個試驗有幾多步？每步有幾多種選擇？", [
  "選工具：每步 2、3 種 → 樹狀圖；每步 6 種 → 列表",
  "列全部：把所有結果排好，不漏不重複",
  "數總數：一共有幾多個結果",
  "數要的：符合條件的有幾多個 → 寫成分數",
], "步驟固定、每次都一樣，這是給工作記憶減負。第 1 步「選工具」要示範判斷過程，不要直接講答案。");

// 範例
(function () {
  const s = newSlide(false);
  title(s, "袋中 1、2、3 三個球，摸一個放回再摸一個", "站② · 範例");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.7, w: 11.7, h: 0.8, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText("求「兩次號碼之和為 4」的概率。", { x: 1.1, y: 1.7, w: 11.1, h: 0.8, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  // 3×3 列表
  card(s, 0.8, 2.75, 5.3, 3.55, C.white);
  const cell = 0.62, x0 = 2.21, y0 = 3.30;
  for (let i = 0; i <= 3; i++) {
    for (let j = 0; j <= 3; j++) {
      if (i === 0 && j === 0) continue;
      const x = x0 + j * cell, y = y0 + i * cell;
      const head = (i === 0 || j === 0);
      const val = head ? String(i === 0 ? j : i) : String(i + j);
      const hit = !head && (i + j === 4);
      s.addShape(p.ShapeType.rect, { x, y, w: cell, h: cell,
        fill: { color: head ? C.block2 : (hit ? C.sageDeep : C.white) },
        line: { color: hit ? C.ink : C.cardLine, width: hit ? 2 : 1 } });
      s.addText(val, { x, y, w: cell, h: cell, align: "center", valign: "middle", fontFace: F,
        fontSize: 18, bold: true, color: hit ? C.white : (head ? C.sageDeep : C.ink) });
    }
  }
  s.addText("格內＝兩次號碼之和", { x: 0.95, y: 5.88, w: 5.0, h: 0.35, align: "center", fontFace: F, fontSize: 17, color: C.soft });
  // 右：四步
  card(s, 6.4, 2.75, 6.1, 3.55, C.white);
  const st = [
    ["選工具", "每步 3 種 → 用列表（3 × 3）"],
    ["列全部", "放回 → 第二次仍可選 1、2、3"],
    ["數總數", "3 × 3 = 9 種"],
    ["數要的", "和為 4：(1,3)(2,2)(3,1) → 3 種"],
  ];
  let y = 2.95;
  st.forEach((t, i) => {
    stepCircle(s, 6.62, y + 0.06, i + 1, 0.44);
    s.addText(t[0], { x: 7.18, y: y, w: 1.2, h: 0.56, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
    s.addText(t[1], { x: 8.32, y: y, w: 4.08, h: 0.56, align: "left", valign: "middle", fontFace: F, fontSize: 17, color: C.ink });
    y += 0.66;
  });
  hlBox(s, 6.62, 5.62, 5.7, 0.58);
  s.addText("P(和為 4) = 3/9 = 1/3", { x: 6.62, y: 5.62, w: 5.7, h: 0.58, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("「放回」是關鍵詞，要加重語氣：放回＝第二次的選擇不變，所以是 3×3 不是 3×2。示範時逐格填，讓學生看到 9 格是怎樣來的。");
})();

// 轉換點
breakSlide("下一頁換你做：挑一顆星開始");

// 分層任務 站②
tieredTasks("站② · 分層練習",
  [
    ["1. 拋兩枚硬幣。用樹狀圖\n   列出所有結果，\n   求 P(一正一反)。",
     "2. 上題中，\n   P(兩個都是正面) = ？"],
    ["3. 袋中 1、2、3 三個球，\n   摸一個放回再摸一個。\n   求 P(兩次之和為 4)。",
     "4. 同時擲兩枚均勻骰子。\n   求 P(兩個點數之和為 7)。"],
    ["5. 兩顆骰子的和，\n   哪一個和最容易出現？\n   用列表說明理由。",
     "6. 拋三枚硬幣，一共有\n   幾多種結果？\n   求 P(剛好兩個正面)。"],
  ],
  "解答核對｜A1: 正正、正反、反正、反反共4種，一正一反有2種→2/4=1/2。A2: 兩正只有1種→1/4。 B3: 3×3=9種，和為4有(1,3)(2,2)(3,1)共3種→3/9=1/3。B4: 6×6=36種，和為7有(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)共6種→6/36=1/6。 C5: 和為7最多（6格），因為和7的格在列表中排成最長的一條斜線；和6、和8各5格。C6: 2×2×2=8種，剛好兩正有正正反、正反正、反正正共3種→3/8。"
);

// 站② 總結
summarySlide("站② · 總結",
  "兩步試驗：先把全部結果排好隊，再數要的。",
  "每步 2–3 種用樹狀圖，每步 6 種用列表；先數總數，再數要的。")
  .addNotes("回收站②。強調工具選擇不是死背，而是看「每步有幾多種」。下一節處理「數唔到全部結果」的情況。");

// =====================================================================
// 站③ 用頻率估計概率（第 3 節）
// =====================================================================
stationDivider("站③", "用頻率估計概率", "算不出等可能時，用大量試驗的頻率去估計", "第 3 節課")
  .addNotes("進入站③。轉折點：前兩站都能「數格數」，但現實好多事數唔到格。這一站教另一條路。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "這位射手，射一次中靶的機會有幾大？", "站③ · 引入");
  card(s, 1.5, 1.95, 10.3, 1.85, C.white);
  s.addText("某射手射擊 100 次，中靶 85 次。", { x: 1.8, y: 1.95, w: 9.7, h: 1.85, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.ink });
  s.addShape(p.ShapeType.roundRect, { x: 1.5, y: 4.15, w: 10.3, h: 1.9, rectRadius: 0.15, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText("這裡沒有「等可能的格」可以數 ——\n中靶和不中靶的機會，本來就不一樣大。", { x: 1.9, y: 4.15, w: 9.5, h: 1.9, align: "center", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.sageDeep, lineSpacingMultiple: 1.35 });
  footer(s, N, false);
  s.addNotes("接住站①的迷思澄清：這正是「機會不一樣大」的例子，所以不能數格數。問學生：咁點算？引出用實際數據去估。");
})();

// 概念 + 趨穩圖
(function () {
  const s = newSlide(false);
  title(s, "試得夠多，頻率就會穩定下來", "站③ · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.72, w: 11.7, h: 0.95, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText([
    { text: "頻率 = ", options: { fontFace: F, fontSize: 25, bold: true, color: C.white } },
    { text: "發生的次數 ÷ 試驗的總次數", options: { fontFace: F, fontSize: 25, bold: true, color: "CFE0D8" } },
  ], { x: 1.1, y: 1.72, w: 11.1, h: 0.95, align: "left", valign: "middle" });
  card(s, 0.8, 2.9, 7.4, 3.5, C.white);
  s.addText("拋硬幣：正面出現的頻率", { x: 0.9, y: 2.98, w: 7.2, h: 0.32, align: "center", fontFace: F, fontSize: 16, color: C.soft });
  freqFig(s, 1.85, 3.45, 5.9, 2.05);
  card(s, 8.5, 2.9, 4.15, 3.5, C.white);
  const pts = ["試幾次：上上落落，很不穩", "試很多次：慢慢靠近 0.5", "就用這個穩定的數，\n去估計概率"];
  let y = 3.05;
  pts.forEach((t, i) => {
    stepCircle(s, 8.75, y + 0.03, i + 1, 0.44);
    s.addText(t, { x: 9.32, y: y - 0.02, w: 3.1, h: 0.8, align: "left", valign: "top", fontFace: F, fontSize: 18, color: C.ink, lineSpacingMultiple: 1.15 });
    y += 0.88;
  });
  hlBox(s, 8.75, 5.70, 3.7, 0.58);
  s.addText("射手：85 ÷ 100 = 0.85", { x: 8.75, y: 5.70, w: 3.7, h: 0.58, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("圖像先行：先讓學生看折線頭段亂、尾段平。可以全班一齊拋硬幣累計次數，即場畫上去。虛線 0.5 是理論值，折線是實際頻率。");
})();

// 比較頁：算出來 vs 試出來
(function () {
  const s = newSlide(false);
  title(s, "兩條路，用哪一條？", "站③ · 比較");
  const w = 5.85, y = 1.9, h = 4.3;
  [["算出來", "站①、站②的方法", ["每個結果機會一樣大", "數得出全部結果", "例：骰子、硬幣、摸球", "答案是準確值"], 0.7],
   ["試出來", "站③的方法", ["機會不一樣大", "數不出全部結果", "例：射擊、圖釘、天氣", "答案是估計值"], 0.7 + w + 0.35]].forEach(col => {
    const cx = col[3];
    card(s, cx, y, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x: cx, y, w, h: 1.0, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(col[0], { x: cx + 0.3, y: y + 0.05, w: w - 0.6, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 27, bold: true, color: C.ink });
    s.addText(col[1], { x: cx + 0.3, y: y + 0.55, w: w - 0.6, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 18, color: C.soft });
    let ty = y + 1.25;
    col[2].forEach(t => {
      s.addText("・" + t, { x: cx + 0.35, y: ty, w: w - 0.7, h: 0.62, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
      ty += 0.72;
    });
  });
  s.addText("先問：每種結果的機會一樣大嗎？　一樣 → 算　不一樣 → 試", { x: 0.7, y: 6.45, w: 12.1, h: 0.5, align: "left", fontFace: F, fontSize: 19, italic: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("這頁是全單元的分流器。同一句判斷（機會一樣嗎）在站①出現過，這裡再用一次，形成固定的提問習慣。");
})();

// 迷思澄清：找錯題
mythSlide("站③ · 迷思澄清", "概率不會保證每次的結果",
  "小明說",
  "「拋硬幣只有正、反兩種，\n所以連續拋 10 次，\n一定剛好有 5 次正面。」",
  "他說得不對",
  "概率講的是大量重複試驗的\n整體規律，不是保證次數。\n\n每次正面的概率是 0.5，\n但實際拋 10 次，\n可能 4 次、6 次、7 次都會發生。",
  "延伸追問（若時間夠）：連續 5 次正面之後，下一次一定是反面嗎？不是——硬幣沒有記憶，下一次仍然是 0.5。這是常見的第二個迷思。"
);

// 轉換點
breakSlide("下一頁換你做：挑一顆星開始");

// 分層任務 站③
tieredTasks("站③ · 分層練習",
  [
    ["1. 某射手射擊 100 次，\n   中靶 85 次。用頻率\n   估計他射一次中靶\n   的概率。",
     "2. 拋圖釘 200 次，針尖\n   朝上 62 次。針尖朝上\n   的頻率是多少？"],
    ["3. 下面哪一題要用「算」，\n   哪一題要用「試」？\n   (1) 擲骰子出 6 點\n   (2) 明天塞車\n   (3) 摸出紅球",
     "4. 甲拋 20 次得 12 次正面，\n   乙拋 2000 次得 1004 次。\n   誰的頻率更可信？"],
    ["5. 找錯題：小明說拋硬幣\n   連續拋 10 次一定剛好\n   有 5 次正面。對嗎？\n   請說明理由。",
     "6. 你想估計「圖釘針尖\n   朝上」的概率。設計一個\n   實驗：要拋幾多次？\n   為甚麼？"],
  ],
  "解答核對｜A1: 85/100=0.85，估計概率約0.85。A2: 62/200=0.31。 B3: (1)算（六面等可能）(2)試（機會不一樣大、數不出全部結果）(3)算（球數已知、等可能）。B4: 乙更可信——試驗次數越多頻率越穩定；乙 1004/2000=0.502 比甲 12/20=0.6 更接近 0.5。 C5: 不對。概率是大量重複試驗的統計規律，不保證每10次恰好5次；每次正面的概率是0.5，實際次數會有波動。C6: 開放，只要點出「次數要夠多（如數百次以上）」＋理由「次數越多頻率越穩定」即可。"
);

// 站③ 總結
summarySlide("站③ · 總結",
  "算不出的時候，就試很多次，用頻率去估計概率。",
  "頻率＝發生次數 ÷ 試驗次數；試得越多就越準。")
  .addNotes("回收站③。強調「估計」兩個字：這是估計值，不是準確值，所以會有波動。");

// =====================================================================
// 全單元回顧
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "三站回顧：一句話帶走");
  const rows = [
    ["站①", "概率＝要的結果數 ÷ 全部結果數（機會要一樣大）"],
    ["站②", "兩步試驗：樹狀圖或列表，先排好再數"],
    ["站③", "算不出就試很多次，用頻率去估計"],
  ];
  let y = 2.05;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.25);
    stationBadge(s, r[0], 0.95, y + 0.32);
    s.addText(r[1], { x: 2.85, y: y, w: 9.5, h: 1.25, fontFace: F, fontSize: 23, bold: true, color: C.ink, align: "left", valign: "middle" });
    y += 1.45;
  });
  s.addShape(p.ShapeType.roundRect, { x: 0.7, y: 6.15, w: 11.9, h: 0.68, rectRadius: 0.12, fill: { color: C.block }, line: { type: "none" } });
  s.addText("每次做題先問一句：每種結果的機會一樣大嗎？", { x: 0.7, y: 6.15, w: 11.9, h: 0.68, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("三節課之後用這一頁做總回顧。底部那句是全單元的通用提問，貼堂或寫在筆記本封面。");
})();

// 結語
(function () {
  const s = newSlide(true);
  s.addText("你已經走完三站了", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, fontFace: F, fontSize: 46, bold: true, color: C.white, align: "left" });
  s.addShape(p.ShapeType.roundRect, { x: 0.95, y: 3.95, w: 11.4, h: 1.3, rectRadius: 0.12, fill: { color: "35564E" }, line: { type: "none" } });
  s.addText("由「說不準」，到寫得出一個數 —— 這就是概率。", { x: 1.3, y: 3.95, w: 10.8, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: "E7F0EB" });
  s.addText("課後：完成《課堂練習》練習 A、B、C", { x: 0.95, y: 5.6, w: 11.4, h: 0.5, fontFace: F, fontSize: 20, italic: true, color: "9FB8AE", align: "left" });
  footer(s, N, true);
  s.addNotes("收尾用 asset-based 語氣：肯定「走完三站」這件事本身。派回本單元課堂練習作鞏固。");
})();

// =====================================================================
const OUT = require("path").join(__dirname, "簡報_概率初步_融合抽離版.pptx");
p.writeFile({ fileName: OUT }).then(() => {
  console.log("OK slides=" + N + " -> " + OUT);
});
