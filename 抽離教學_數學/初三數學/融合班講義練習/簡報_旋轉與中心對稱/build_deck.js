// 融合抽離小組 SOIL 教學簡報：旋轉與中心對稱（初三）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。幾何圖原生繪製。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "旋轉與中心對稱 兩站通關（融合抽離版）";

// ---- 配色 (Sage Calm 低刺激) ----
const C = {
  bgLight: "EDF3F0", bgDark: "2E4A43", ink: "233A34", soft: "5C6F68",
  sage: "6FA48C", sageDeep: "4E8770", slate: "50808E",
  block: "DCEAE3", block2: "CFE0D8", cardLine: "B9CFC5",
  grid: "D3E1DA", white: "FFFFFF", starInk: "2E4A43",
};
const F = "Microsoft JhengHei";
const MONO = "Consolas";

// ---- 共用小工具 ----
function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("初三數學 · 旋轉與中心對稱（抽離小組·融合版）", {
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

let N = 0;
function newSlide(dark) { const s = p.addSlide(); bg(s, dark); N += 1; return s; }

// =====================================================================
// 幾何圖（原生）
// =====================================================================
// 坐標對稱示意圖：cx,cy=原點(吋)；u=每格吋；points=[{mx,my,label,color,lx,ly}]
function coordFig(s, cx, cy, u, xr, yr, points, symLine) {
  const MX = m => cx + m * u;
  const MY = m => cy - m * u;
  // 淺格線
  for (let gx = xr[0]; gx <= xr[1]; gx++) seg(s, MX(gx), MY(yr[0]), MX(gx), MY(yr[1]), { color: C.grid, width: 0.75 });
  for (let gy = yr[0]; gy <= yr[1]; gy++) seg(s, MX(xr[0]), MY(gy), MX(xr[1]), MY(gy), { color: C.grid, width: 0.75 });
  // 對稱線（虛線，先畫於點下層）
  if (symLine) {
    const a = symLine[0], b = symLine[1];
    seg(s, MX(a[0]), MY(a[1]), MX(b[0]), MY(b[1]), { color: C.sage, width: 2, dash: "dash" });
  }
  // 軸（含箭頭）
  seg(s, MX(xr[0]), cy, MX(xr[1]), cy, { color: C.soft, width: 1.75, begin: "triangle", end: "triangle" });
  seg(s, cx, MY(yr[0]), cx, MY(yr[1]), { color: C.soft, width: 1.75, begin: "triangle", end: "triangle" });
  s.addText("x", { x: MX(xr[1]) - 0.05, y: cy + 0.06, w: 0.4, h: 0.3, fontFace: F, fontSize: 16, italic: true, color: C.soft, align: "left" });
  s.addText("y", { x: cx + 0.12, y: MY(yr[1]) - 0.12, w: 0.4, h: 0.3, fontFace: F, fontSize: 16, italic: true, color: C.soft, align: "left" });
  // 原點
  s.addText("O", { x: cx - 0.42, y: cy + 0.04, w: 0.36, h: 0.3, fontFace: F, fontSize: 16, color: C.soft, align: "right" });
  // 點
  points.forEach(pt => {
    dot(s, MX(pt.mx), MY(pt.my), pt.color || C.sageDeep, 0.16);
    s.addText(pt.label, { x: MX(pt.mx) + (pt.lx || 0.12), y: MY(pt.my) + (pt.ly || -0.34), w: 2.2, h: 0.32,
      fontFace: F, fontSize: 17, bold: true, color: pt.tc || C.ink, align: "left" });
  });
}
// 旋轉示意圖：以 (cx,cy) 為旋轉中心 O，示範 A→A′（OA=OA′、夾角=旋轉角）
function rotationFig(s, cx, cy) {
  const r = 1.7;
  const degA = 28, degAp = 92; // A 與 A′ 的方位角（自 x 正向逆時針，畫布 y 向下故取負）
  const P = d => [cx + r * Math.cos(d * Math.PI / 180), cy - r * Math.sin(d * Math.PI / 180)];
  const A = P(degA), Ap = P(degAp);
  // 半徑弧（旋轉軌跡，淺色）
  s.addShape(p.ShapeType.arc, { x: cx - r, y: cy - r, w: 2 * r, h: 2 * r,
    angleRange: [-degAp, -degA], line: { color: C.sage, width: 1.5, dashType: "dash" } });
  // OA、OA′
  seg(s, cx, cy, A[0], A[1], { color: C.sageDeep, width: 2.25 });
  seg(s, cx, cy, Ap[0], Ap[1], { color: C.sageDeep, width: 2.25 });
  // 點與標記
  dot(s, cx, cy, C.ink, 0.16);
  dot(s, A[0], A[1], C.slate, 0.18);
  dot(s, Ap[0], Ap[1], C.slate, 0.18);
  s.addText("O", { x: cx - 0.05, y: cy + 0.1, w: 0.5, h: 0.3, fontFace: F, fontSize: 18, bold: true, color: C.ink, align: "left" });
  s.addText("A", { x: A[0] + 0.12, y: A[1] - 0.12, w: 0.6, h: 0.3, fontFace: F, fontSize: 20, bold: true, color: C.ink, align: "left" });
  s.addText("A′", { x: Ap[0] - 0.15, y: Ap[1] - 0.42, w: 0.7, h: 0.3, fontFace: F, fontSize: 20, bold: true, color: C.ink, align: "left" });
  // 旋轉角標示
  s.addText("旋轉角", { x: cx - 0.35, y: cy - 1.28, w: 1.5, h: 0.3, fontFace: F, fontSize: 15, color: C.sageDeep, align: "center" });
  // 等長提示
  s.addText("OA = OA′", { x: cx + 0.7, y: cy + 0.55, w: 2.0, h: 0.32, fontFace: F, fontSize: 16, bold: true, color: C.slate, align: "left" });
}

// =====================================================================
// S1 封面
// =====================================================================
(function () {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.45, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.45, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("旋轉與中心對稱", { x: 0.85, y: 2.4, w: 11.6, h: 1.1, fontFace: F, fontSize: 52, bold: true, color: C.white, align: "left" });
  s.addText("兩站通關", { x: 0.85, y: 3.5, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "站① 圖形的旋轉", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "      →      ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "站② 中心對稱", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.75, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著兩站一步一步走", { x: 0.9, y: 5.5, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, italic: true, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：今天不趕進度，跟著兩站走。每一站都是：學一招 → 看老師示範 → 自己挑星星練習。做得起就往上跳一層。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "今日課堂流程");
  const rows = [
    ["站①", "圖形的旋轉", "繞一點轉角度：旋轉中心、方向、旋轉角"],
    ["站②", "中心對稱", "轉 180° 能重合；點對原點都變相反數"],
  ];
  let y = 2.05;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.42);
    stationBadge(s, r[0], 0.95, y + 0.4);
    s.addText(r[1], { x: 2.85, y: y + 0.18, w: 9.4, h: 0.6, fontFace: F, fontSize: 27, bold: true, color: C.ink, align: "left", valign: "middle" });
    s.addText(r[2], { x: 2.85, y: y + 0.78, w: 9.4, h: 0.5, fontFace: F, fontSize: 20, color: C.soft, align: "left", valign: "middle" });
    y += 1.62;
  });
  s.addText("每一站都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 5.75, w: 11.9, h: 0.5, fontFace: F, fontSize: 19, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖：讓學生知道整節課的結構，減少焦慮。兩站節奏一致，做完一站休息一下。");
})();

// =====================================================================
// 產生器
// =====================================================================
function stationDivider(badge, name, goal) {
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
  return s;
}
function breakSlide(msg) {
  const s = newSlide(false);
  s.addShape(p.ShapeType.roundRect, { x: 3.4, y: 2.2, w: 6.5, h: 3.0, rectRadius: 0.2, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("‖  換一換", { x: 3.4, y: 2.55, w: 6.5, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.sageDeep });
  s.addText(msg, { x: 3.7, y: 3.5, w: 5.9, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 24, color: C.ink });
  s.addText("先伸展 30 秒，再開始 🙂", { x: 3.4, y: 4.4, w: 6.5, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 20, italic: true, color: C.soft });
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
  const x0 = 0.65, gap = 0.28, w = (12.7 - 2 * gap) / 3, yTop = 1.95, h = 4.35;
  tiers.forEach((ti, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 0.9, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(ti.t, { x: x + 0.2, y: yTop + 0.06, w: w - 0.4, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(ti.star, { x: x + 0.2, y: yTop + 0.46, w: w - 0.4, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.starInk });
    let ty = yTop + 1.05;
    cols[i].forEach((it) => {
      s.addText(it, { x: x + 0.24, y: ty, w: w - 0.46, h: 1.5, align: "left", valign: "top", fontFace: F, fontSize: 19, color: C.ink, lineSpacingMultiple: 1.22 });
      ty += 1.62;
    });
  });
  s.addText("做得起 A，就往 B、C 跳一層 ↗   全部同一個概念，只是鷹架不同", { x: 0.65, y: 6.5, w: 12.7, h: 0.45, fontFace: F, fontSize: 17, italic: true, color: C.sageDeep, align: "left" });
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

// =====================================================================
// 站① 圖形的旋轉
// =====================================================================
stationDivider("站①", "圖形的旋轉", "看懂旋轉三要素，會用旋轉的性質").addNotes("進入站①。先建立信心：旋轉只是換位置，圖形一模一樣（全等）。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "生活裡，哪些在「旋轉」？", "站① · 引入");
  const data = [
    ["時鐘的指針", "繞鐘面中心轉", true],
    ["電風扇葉片", "繞中軸轉", true],
    ["摩天輪座艙", "繞輪心轉", true],
    ["電梯上上下下", "只是平移，不是旋轉", false],
  ];
  let y = 2.05;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.0, d[2] ? C.block : C.white);
    s.addText(d[0], { x: 1.2, y: y, w: 5.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(d[2] ? "旋轉 ✔" : "不是 ✗", { x: 6.3, y: y, w: 2.0, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: d[2] ? C.sageDeep : C.soft });
    s.addText(d[1], { x: 8.4, y: y, w: 4.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.soft });
    y += 1.13;
  });
  footer(s, N, false);
  s.addNotes("低門檻暖身：只判斷是不是繞一點轉。口頭補充：旋轉一定有一個固定不動的中心點。");
})();

// 概念 + 保底：定義 + 三要素
(function () {
  const s = newSlide(false);
  title(s, "什麼是旋轉？三個要素", "站① · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.8, w: 11.7, h: 1.05, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("把一個圖形繞著一個點，轉一個角度 —— 就是旋轉", { x: 1.1, y: 1.8, w: 11.1, h: 1.05, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  const items = [
    ["旋轉中心", "繞著哪一點轉（固定不動）"],
    ["旋轉方向", "順時針 或 逆時針"],
    ["旋轉角", "轉了多少度"],
  ];
  let y = 3.2;
  items.forEach((it, i) => {
    stepCircle(s, 0.9, y, i + 1, 0.55);
    hlBox(s, 1.65, y, 3.4, 0.55);
    s.addText(it[0], { x: 1.65, y: y, w: 3.4, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 5.3, y: y, w: 7.2, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 0.92;
  });
  s.addText("記住三個詞：中心、方向、角度，就掌握了旋轉 👍", { x: 0.9, y: 6.15, w: 11.6, h: 0.45, fontFace: F, fontSize: 19, italic: true, color: C.soft, align: "left" });
  footer(s, N, false);
  s.addNotes("保底成功經驗：全班都要能講出三要素。用時鐘手勢示範順時針/逆時針。");
})();

// 性質頁（原生旋轉示意圖）
(function () {
  const s = newSlide(false);
  title(s, "旋轉的三個性質", "站① · 性質");
  // 左：文字三性質
  const props = [
    ["①", "對應點到旋轉中心\n距離相等"],
    ["②", "每對對應點與中心\n連線的夾角＝旋轉角"],
    ["③", "旋轉前後的圖形\n完全一樣（全等）"],
  ];
  let y = 2.0;
  props.forEach((pr) => {
    card(s, 0.7, y, 6.2, 1.3, C.white);
    s.addText(pr[0], { x: 0.9, y: y, w: 0.9, h: 1.3, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.sageDeep });
    s.addText(pr[1], { x: 1.8, y: y, w: 4.9, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.15 });
    y += 1.48;
  });
  // 右：旋轉示意圖
  card(s, 7.2, 2.0, 5.5, 4.26, C.bgLight);
  rotationFig(s, 9.7, 4.35);
  footer(s, N, false);
  s.addNotes("圖像先行：右圖示範 A→A′，OA=OA′（性質①）、∠AOA′＝旋轉角（性質②）。強調圖形沒變大變小（性質③全等）。");
})();

// 步驟卡範例：用性質求邊角
stepCardSlide("站① · 範例（用性質）", "△ABC 繞 O 旋轉 70° 得 △A′B′C′",
  "已知 OA = 5、∠AOA′ = 70°、OB = 3。求 OA′、∠BOB′、OB′。", [
  "OA′：對應點到中心等距 → OA′ = OA = 5",
  "∠BOB′：夾角都等於旋轉角 → ∠BOB′ = 70°",
  "OB′：對應點到中心等距 → OB′ = OB = 3",
], "不用量、不用算複雜式子，只要套三個性質。提醒：旋轉角對每一對對應點都一樣，所以 ∠BOB′ 也是 70°。");

// 轉換點
breakSlide("下一頁換你做：挑一顆星開始");

// 分層任務頁 站①
tieredTasks("站① · 分層練習",
  [
    ["1. △ 繞 O 旋轉，OA = 4，\n   旋轉後 OA′ =？", "2. 分針每分鐘轉 6°，\n   12:00 → 12:15 轉幾度？"],
    ["3. △ABC 繞 O 轉 70°，\n   OB = 3、∠AOA′ = 70°，\n   求 OB′、∠BOB′", "4. 分針 12:00 → 12:20\n   轉幾度？繞哪一點？"],
    ["5. 風扇葉片繞軸轉，轉幾\n   度後看起來一樣？\n   （試 3 葉、4 葉）", "6. 說一個生活中『旋轉』\n   的例子，指出它的中心\n   和大約轉的角度"],
  ],
  "解答核對｜A1: OA′=OA=4；A2: 15×6=90°。 B3: OB′=OB=3、∠BOB′=70°（旋轉角相等）；B4: 20×6=120°，繞鐘面中心。 C5: 360÷葉數 → 3葉=120°、4葉=90°；C6: 開放，須指出中心與角度（如摩天輪繞輪心）。"
);

// 站① 總結
summarySlide("站① · 總結",
  "旋轉＝繞中心轉角度，圖形全等不變形。",
  "旋轉三要素：中心、方向、角；對應點到中心一樣長。").addNotes("回收站①。保底句要全班能覆述：中心、方向、角。");

// =====================================================================
// 站② 中心對稱
// =====================================================================
stationDivider("站②", "中心對稱", "轉 180° 能重合；坐標關於原點都變相反數").addNotes("進入站②。賣點：中心對稱其實就是『轉 180°』這一個特別的旋轉。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "撲克牌的祕密：轉 180° 還一樣", "站② · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.6, y: 2.25, w: 10.1, h: 2.5, rectRadius: 0.18, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("把圖形繞一點轉 180°", { x: 1.9, y: 2.5, w: 9.5, h: 0.8, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.ink });
  s.addText("如果能和原來重合 —— 就是中心對稱", { x: 1.9, y: 3.45, w: 9.5, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("用撲克牌 K/Q（點對稱設計）示範轉 180° 還一樣，製造好奇。中心對稱＝一種特別的旋轉（180°）。");
})();

// 概念 + 保底
(function () {
  const s = newSlide(false);
  title(s, "中心對稱是什麼？", "站② · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.8, w: 11.7, h: 1.1, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("兩個圖形繞一點轉 180° 能重合 → 關於這點成中心對稱，這點叫「對稱中心」", { x: 1.1, y: 1.8, w: 11.1, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
  const items = [
    ["性質", "對稱點的連線都經過對稱中心，而且被中心平分"],
    ["坐標特例", "點 (x, y) 關於原點的對稱點是 (−x, −y)"],
  ];
  let y = 3.25;
  items.forEach((it) => {
    card(s, 0.8, y, 11.7, 1.28, C.white);
    hlBox(s, 1.05, y + 0.36, 2.6, 0.56);
    s.addText(it[0], { x: 1.05, y: y + 0.36, w: 2.6, h: 0.56, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 3.95, y: y, w: 8.4, h: 1.28, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    y += 1.5;
  });
  footer(s, N, false);
  s.addNotes("保底：全班要能背『關於原點 → (−x, −y)』。強調兩個坐標都要變號，不是只變一個。");
})();

// CRA 三階頁
(function () {
  const s = newSlide(false);
  title(s, "關於原點對稱：具體 → 圖 → 式", "站② · CRA");
  s.addText("以點 A(3, 2) 為例", { x: 0.8, y: 1.65, w: 11.7, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.ink, align: "left" });
  const cols = [
    ["具體", "把點 A 穿過原點\n推到「正對面」\n一樣遠的位置", "像翻到背面"],
    ["表徵", "在坐標格上畫：\nA(3, 2) 與\nA′(−3, −2)", "連線過 O、等長"],
    ["抽象", "兩個坐標\n都變相反數：", "(3, 2) → (−3, −2)"],
  ];
  const x0 = 0.8, gap = 0.3, w = (11.7 - 2 * gap) / 3, yTop = 2.3, h = 3.75;
  cols.forEach((c, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 0.7, rectRadius: 0.12, fill: { color: C.sage }, line: { type: "none" } });
    s.addText(c[0], { x, y: yTop, w, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
    s.addText(c[1], { x: x + 0.2, y: yTop + 0.9, w: w - 0.4, h: 1.85, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.3 });
    hlBox(s, x + 0.2, yTop + 2.95, w - 0.4, 0.6);
    s.addText(c[2], { x: x + 0.2, y: yTop + 2.95, w: w - 0.4, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.sageDeep });
    if (i < 2) s.addText("→", { x: x + w - 0.02, y: yTop + 1.3, w: gap + 0.04, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.sageDeep });
  });
  footer(s, N, false);
  s.addNotes("先具體（穿過原點推到對面）、再圖（畫在格上看到等長）、最後抽象（都變號）。每階示範→引導→學生做。");
})();

// 坐標範例頁（原生坐標圖）
(function () {
  const s = newSlide(false);
  title(s, "在坐標格上看中心對稱", "站② · 範例");
  // 左：坐標圖
  card(s, 0.7, 1.75, 6.4, 4.55, C.white);
  coordFig(s, 3.9, 4.02, 0.5, [-5, 5], [-4, 4],
    [
      { mx: 3, my: 2, label: "A(3, 2)", color: C.sageDeep, tc: C.ink, lx: 0.14, ly: -0.36 },
      { mx: -3, my: -2, label: "A′(−3, −2)", color: C.slate, tc: C.ink, lx: -1.9, ly: 0.06 },
    ],
    [[3, 2], [-3, -2]]);
  // 右：兩個範例步驟
  s.addText("關於原點對稱：x、y 都變號", { x: 7.4, y: 1.95, w: 5.5, h: 0.5, fontFace: F, fontSize: 21, bold: true, color: C.sageDeep, align: "left" });
  card(s, 7.4, 2.55, 5.3, 1.55, C.block);
  s.addText("例① A(3, 2)", { x: 7.65, y: 2.68, w: 4.9, h: 0.45, fontFace: F, fontSize: 21, bold: true, color: C.ink, align: "left" });
  s.addText("x：3 → −3    y：2 → −2", { x: 7.65, y: 3.12, w: 4.9, h: 0.4, fontFace: F, fontSize: 20, color: C.ink, align: "left" });
  s.addText("→ A′(−3, −2)", { x: 7.65, y: 3.55, w: 4.9, h: 0.45, fontFace: F, fontSize: 21, bold: true, color: C.sageDeep, align: "left" });
  card(s, 7.4, 4.35, 5.3, 1.9, C.block);
  s.addText("例② P(−1, 4) 繞原點轉 180°", { x: 7.65, y: 4.48, w: 4.9, h: 0.45, fontFace: F, fontSize: 21, bold: true, color: C.ink, align: "left" });
  s.addText("轉 180° = 關於原點對稱", { x: 7.65, y: 4.95, w: 4.9, h: 0.4, fontFace: F, fontSize: 19, color: C.soft, align: "left" });
  s.addText("x：−1 → 1    y：4 → −4", { x: 7.65, y: 5.35, w: 4.9, h: 0.4, fontFace: F, fontSize: 20, color: C.ink, align: "left" });
  s.addText("→ P′(1, −4)", { x: 7.65, y: 5.78, w: 4.9, h: 0.45, fontFace: F, fontSize: 21, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("圖上指出：A 與 A′ 的連線穿過 O，兩段一樣長。口訣：關於原點對稱、繞原點轉 180°，都是 x、y 一起變號。");
})();

// 迷思澄清頁
(function () {
  const s = newSlide(false);
  title(s, "哪些是中心對稱圖形？", "站② · 迷思澄清");
  // 上：找錯
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.75, w: 11.7, h: 1.5, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "小明說：「正三角形是中心對稱圖形。」  ", options: { fontFace: F, fontSize: 21, color: C.ink } },
    { text: "✗ 不對", options: { fontFace: F, fontSize: 22, bold: true, color: C.soft } },
  ], { x: 1.1, y: 1.85, w: 11.1, h: 0.6, align: "left", valign: "middle" });
  s.addText("正三角形要轉 120° 才和自己重合，轉 180° 不能重合 → 不是中心對稱圖形", { x: 1.1, y: 2.5, w: 11.1, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.sageDeep });
  // 下：分類
  const yes = ["平行四邊形", "矩形", "圓"];
  const no = ["正三角形", "正五邊形"];
  card(s, 0.8, 3.5, 5.75, 2.75, C.white);
  s.addText("是中心對稱 ✔（轉 180° 會重合）", { x: 1.05, y: 3.65, w: 5.3, h: 0.5, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  s.addText(yes.map(t => "· " + t).join("\n"), { x: 1.25, y: 4.2, w: 5.1, h: 1.9, align: "left", valign: "top", fontFace: F, fontSize: 22, color: C.ink, lineSpacingMultiple: 1.35 });
  card(s, 6.75, 3.5, 5.75, 2.75, C.white);
  s.addText("不是中心對稱 ✗", { x: 7.0, y: 3.65, w: 5.3, h: 0.5, fontFace: F, fontSize: 20, bold: true, color: C.soft, align: "left" });
  s.addText(no.map(t => "· " + t).join("\n"), { x: 7.2, y: 4.2, w: 5.1, h: 1.9, align: "left", valign: "top", fontFace: F, fontSize: 22, color: C.ink, lineSpacingMultiple: 1.35 });
  footer(s, N, false);
  s.addNotes("澄清：軸對稱 ≠ 中心對稱。判斷法：心裡把圖形轉 180°，能不能剛好蓋回自己。用中性灰標『不是』，不用紅色。");
})();

// 轉換點
breakSlide("下一頁換你做：先寫對稱點");

// 分層任務頁 站②
tieredTasks("站② · 分層練習",
  [
    ["1. 寫關於原點的對稱點：\n   A(2, 5) → (＿, ＿)\n   B(−3, 1) → (＿, ＿)", "2. 是不是中心對稱圖形？\n   平行四邊形／正三角形\n   ／矩形／圓／正五邊形"],
    ["3. A(a, 3) 與 B(−2, b)\n   關於原點對稱，\n   求 a、b", "4. P(−1, 4) 繞原點\n   旋轉 180°，\n   寫出 P′ 的坐標"],
    ["5. △ABC：A(1,1)、B(4,1)、\n   C(1,3) 繞原點轉 180°，\n   求三頂點在第幾象限", "6. 找錯：小明說『正三角形\n   是中心對稱圖形』，\n   對嗎？請說明理由"],
  ],
  "解答核對｜A1: A→(−2,−5)、B→(3,−1)；A2: 平四(是)、正三角(否)、矩形(是)、圓(是)、正五邊(否)。 B3: 坐標互為相反數 → a=2、b=−3；B4: 轉180°即關於原點對稱 → P′(1,−4)。 C5: A′(−1,−1)、B′(−4,−1)、C′(−1,−3)，都在第三象限；C6: 不對，正三角形要轉120°才重合，180°不重合。"
);

// 站② 總結
summarySlide("站② · 總結",
  "轉 180° 能重合就是中心對稱；對原點都變相反數。",
  "點 (x, y) 關於原點對稱 → (−x, −y)：x、y 都加負號。").addNotes("回收站②。保底：能寫出 (x,y)→(−x,−y) 就達標。");

// =====================================================================
// 收尾
// =====================================================================
// 兩站總複習
(function () {
  const s = newSlide(false);
  title(s, "兩站帶走話，一次回顧");
  const data = [
    ["站①", "旋轉＝繞中心轉角度，圖形全等；\n三要素：中心、方向、角。"],
    ["站②", "轉 180° 能重合就是中心對稱；\n關於原點對稱 → (x, y) 變 (−x, −y)。"],
  ];
  let y = 2.1;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.75, C.white);
    stationBadge(s, d[0], 0.95, y + 0.56);
    s.addText(d[1], { x: 2.9, y: y, w: 9.4, h: 1.75, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink, lineSpacingMultiple: 1.2 });
    y += 1.95;
  });
  footer(s, N, false);
  s.addNotes("整體回收。可請學生每站講一句自己的話覆述。連結：中心對稱就是旋轉 180° 的特例。");
})();

// 結語（asset-based）
(function () {
  const s = newSlide(true);
  s.addText("你已經走完兩站！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("旋轉與中心對稱，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次看到「關於原點對稱」，記得：x、y 都變相反數。", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, italic: true, color: "9FB8AE" });
  s.addNotes("正向收束，asset-based。肯定努力與策略，不用『終於』『總算』等字眼。");
})();

// 教師備註頁
(function () {
  const s = newSlide(false);
  title(s, "教師備註 · 融合層設計", "供科組 / IEP 會議說明");
  const left = [
    "路線：Accommodation（調整支援）",
    "內容不減、維持初三年級標準，",
    "只改「接觸方式」與「練習鷹架」。",
    "",
    "分層靠學生自選星星，不點名個案。",
  ];
  const right = [
    "◆ CRA 三階：具體 → 圖 → 抽象",
    "◆ 原生幾何圖：旋轉示意 / 坐標對稱",
    "◆ 步驟卡：套性質一步一行、編號",
    "◆ 轉換點＋預告：照顧注意力節奏",
    "◆ 保底成功句＋asset-based 用語",
  ];
  card(s, 0.7, 1.9, 5.85, 4.4, C.white);
  s.addText("調整定位", { x: 0.95, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(left.join("\n"), { x: 0.95, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
  card(s, 6.75, 1.9, 5.85, 4.4, C.white);
  s.addText("融合層做了什麼", { x: 7.0, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(right.join("\n"), { x: 7.0, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.35 });
  footer(s, N, false);
  s.addNotes("此頁供教師/IEP 對接用，上課可略過。屬 Accommodation，未剪裁課程內容。");
})();

// ---- 輸出 ----
p.writeFile({ fileName: "簡報_旋轉與中心對稱_融合抽離版.pptx" }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
