// 融合抽離小組 SOIL 教學簡報：正多邊形和圓、弧長與扇形面積（初三 · 單元 11 · 兩課時）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。幾何圖原生繪製。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE";
p.author = "初三數學抽離小組";
p.title = "正多邊形和圓、弧長與扇形面積 兩課時（融合抽離版）";

const UNIT = "正多邊形和圓、弧長與扇形面積";

const C = {
  bgLight: "EDF3F0", bgDark: "2E4A43", ink: "233A34", soft: "5C6F68",
  sage: "6FA48C", sageDeep: "4E8770", slate: "50808E",
  block: "DCEAE3", block2: "CFE0D8", cardLine: "B9CFC5",
  grid: "D3E1DA", white: "FFFFFF", starInk: "2E4A43",
};
const F = "Microsoft JhengHei";

function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("初三數學 · " + UNIT + "（抽離小組·融合版）", {
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
function badge(s, txt, x, y, w, h, fs) {
  const W = w || 2.2, H = h || 0.62;
  s.addShape(p.ShapeType.roundRect, { x, y, w: W, h: H, rectRadius: H / 2, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(txt, { x, y, w: W, h: H, align: "center", valign: "middle", fontFace: F, fontSize: fs || 22, bold: true, color: C.white });
}
function card(s, x, y, w, h, fill) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.12, fill: { color: fill || C.white }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
}
function hlBox(s, x, y, w, h) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: C.block }, line: { type: "none" } });
}
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
function lbl(s, txt, X, Y, o) {
  o = o || {};
  s.addText(txt, { x: X, y: Y, w: o.w || 1.4, h: o.h || 0.3, align: o.align || "left", valign: "middle",
    fontFace: F, fontSize: o.fs || 18, bold: o.bold !== false, color: o.color || C.ink });
}
let N = 0;
function newSlide(dark) { const s = p.addSlide(); bg(s, dark); N += 1; return s; }

// ---- 幾何工具 ----
function onC(cx, cy, R, deg) {
  const t = deg * Math.PI / 180;
  return [cx + R * Math.cos(t), cy - R * Math.sin(t)];
}
function circleOutline(s, cx, cy, R, o) {
  o = o || {};
  s.addShape(p.ShapeType.ellipse, {
    x: cx - R, y: cy - R, w: 2 * R, h: 2 * R,
    fill: { type: "none" }, line: { color: o.color || C.ink, width: o.width || 2 },
  });
}
// 角弧：涵蓋數學角 a1→a2（逆時針）。angleRange 收到負值會畫成整圓，必須正規化
function angArc(s, cx, cy, R, a1, a2, o) {
  o = o || {};
  const norm = (d) => ((d % 360) + 360) % 360;
  let st = norm(-a2), en = norm(-a1);
  if (en <= st) en += 360;
  s.addShape(p.ShapeType.arc, {
    x: cx - R, y: cy - R, w: 2 * R, h: 2 * R,
    angleRange: [st, en],
    line: { color: o.color || C.slate, width: o.width || 2 },
  });
}

// 圖①：正六邊形內接於圓，中心角 60°
function figHexagon(s, cx, cy, R) {
  circleOutline(s, cx, cy, R, { color: C.soft, width: 1.75 });
  const V = [];
  for (let i = 0; i < 6; i++) V.push(onC(cx, cy, R, 90 - i * 60));
  for (let i = 0; i < 6; i++) {
    const A = V[i], B = V[(i + 1) % 6];
    const isEdge = (i === 0);   // 高亮其中一條邊（= 半徑）
    seg(s, A[0], A[1], B[0], B[1], { color: isEdge ? C.sageDeep : C.ink, width: isEdge ? 3.5 : 2.2 });
  }
  // 兩條半徑構成中心角
  seg(s, cx, cy, V[0][0], V[0][1], { color: C.sage, width: 2.5 });
  seg(s, cx, cy, V[1][0], V[1][1], { color: C.sage, width: 2.5 });
  angArc(s, cx, cy, 0.42, 30, 90, { color: C.sage, width: 2.5 });
  dot(s, cx, cy, C.ink, 0.14);
  V.forEach((Q) => dot(s, Q[0], Q[1], C.soft, 0.12));
  lbl(s, "O", cx - 0.42, cy + 0.1, { fs: 16, color: C.soft, w: 0.4, align: "right" });
  lbl(s, "60°", cx + 0.12, cy - 0.56, { fs: 16, color: C.sage, w: 0.7 });
  lbl(s, "R", cx + R * 0.42, cy - R * 0.16, { fs: 17, color: C.sage, w: 0.4 });
  lbl(s, "邊長 a ＝ R", cx + R * 0.55, cy - R * 0.95, { fs: 15, color: C.sageDeep, w: 2.0 });
  lbl(s, "正六邊形：中心角 60°", cx - 1.9, cy + R + 0.36, { fs: 15, color: C.sageDeep, w: 3.8, align: "center" });
}

// 圖②：扇形 OAB（圓心角 n°、半徑 R、弧長 l）
function figSector(s, cx, cy, R, deg) {
  const A = onC(cx, cy, R, 0), B = onC(cx, cy, R, deg);
  // 整圓淡色作對照
  circleOutline(s, cx, cy, R, { color: C.grid, width: 1.5 });
  angArc(s, cx, cy, R, 0, deg, { color: C.sageDeep, width: 4 });   // 弧長 l
  seg(s, cx, cy, A[0], A[1], { color: C.sage, width: 2.8 });
  seg(s, cx, cy, B[0], B[1], { color: C.sage, width: 2.8 });
  angArc(s, cx, cy, 0.5, 0, deg, { color: C.slate, width: 2.5 });
  dot(s, cx, cy, C.ink, 0.14);
  dot(s, A[0], A[1], C.sageDeep, 0.14); dot(s, B[0], B[1], C.sageDeep, 0.14);
  lbl(s, "O", cx - 0.14, cy + 0.24, { fs: 17, w: 0.4, align: "center" });
  lbl(s, "A", A[0] + 0.12, A[1] - 0.02, { fs: 18, w: 0.4 });
  lbl(s, "B", B[0] - 0.5, B[1] - 0.06, { fs: 18, w: 0.4, align: "right" });
  lbl(s, "n°", cx + 0.16, cy - 0.5, { fs: 16, color: C.slate, w: 0.6 });
  lbl(s, "R", cx + R * 0.5, cy + 0.16, { fs: 17, color: C.sage, w: 0.4 });
  const M = onC(cx, cy, R + 0.34, deg / 2);
  lbl(s, "弧長 l", M[0] - 0.55, M[1], { fs: 16, color: C.sageDeep, w: 1.1, align: "center" });
}

// ---- 版型 ----
function lessonDivider(tag, name, goal) {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 2.15, w: 3.1, h: 1.0, rectRadius: 0.5, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(tag, { x: 0.9, y: 2.15, w: 3.1, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 34, bold: true, color: C.white });
  s.addText(name, { x: 4.3, y: 2.15, w: 8.3, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 36, bold: true, color: C.white });
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
  s.addText("先伸展 30 秒，再開始 🙂", { x: 3.4, y: 4.4, w: 6.5, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
  footer(s, N, false);
  s.addNotes("轉換點：起身伸展 30 秒。先預告下一段是自己動手做，讓 ADHD／ASD 學生有準備。");
  return s;
}
function tieredTasks(kicker, cols, note) {
  const s = newSlide(false);
  title(s, "挑戰練習 · 自選星星", kicker);
  const tiers = [{ t: "練習 A", star: "★☆☆" }, { t: "練習 B", star: "★★☆" }, { t: "練習 C", star: "★★★" }];
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
  s.addText("做得起 A，就往 B、C 跳一層 ↗   全部同一個概念，只是鷹架不同", { x: 0.65, y: 6.5, w: 12.7, h: 0.45, fontFace: F, fontSize: 17, color: C.sageDeep, align: "left" });
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

// ===================== S1 封面 =====================
(function () {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.45, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.45, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("正多邊形、弧長與扇形", { x: 0.85, y: 2.35, w: 11.6, h: 1.1, fontFace: F, fontSize: 46, bold: true, color: C.white, align: "left" });
  s.addText("兩課時通關", { x: 0.85, y: 3.45, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "課時① 把圓切成 n 份", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "      →      ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "課時② 拿走其中一塊", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.7, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著兩課時一步一步走", { x: 0.9, y: 5.45, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：兩節課都在做同一件事——把一整個圓（360°）按比例分。第一節分成 n 等份，第二節只取其中一塊。");
})();

// ===================== S2 流程預告 =====================
(function () {
  const s = newSlide(false);
  title(s, "這個單元，我們走兩節課");
  const rows = [
    ["課時①", "正多邊形和圓", "中心角 ＝ 360° ÷ n；正 n 邊形的內角；正六邊形的邊長 ＝ 半徑"],
    ["課時②", "弧長與扇形面積", "圓心角佔 360° 的幾分之幾，弧長和面積就佔同樣的比例"],
  ];
  let y = 2.05;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.5);
    badge(s, r[0], 0.95, y + 0.44, 1.9, 0.62, 20);
    s.addText(r[1], { x: 3.05, y: y + 0.16, w: 9.2, h: 0.56, align: "left", valign: "middle", fontFace: F, fontSize: 25, bold: true, color: C.ink });
    s.addText(r[2], { x: 3.05, y: y + 0.74, w: 9.2, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.soft, lineSpacingMultiple: 1.15 });
    y += 1.68;
  });
  s.addText("每一節都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 5.6, w: 11.9, h: 0.42, fontFace: F, fontSize: 19, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖。強調兩節課的共同想法：一整個圓是 360°，任何東西都按比例分。");
})();

// ===================== 課時① 正多邊形 =====================
lessonDivider("課時①", "正多邊形和圓", "會算中心角和內角，會用正六邊形的特例")
  .addNotes("進入課時①。核心只有一條除法：360 ÷ n。內角公式是舊知識（多邊形內角和），順帶複習。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "生活裡的正多邊形", "課時① · 引入");
  const data = [
    ["六角螺帽", "正六邊形", "扳手每轉 60° 就能再咬住"],
    ["蜂巢", "正六邊形", "同樣材料圍出最大空間"],
    ["交通「停」牌", "正八邊形", "遠遠看就認得出形狀"],
    ["長方形磁磚", "不是正多邊形", "四邊不等長"],
  ];
  let y = 2.05;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.0, d[1] === "不是正多邊形" ? C.white : C.block);
    s.addText(d[0], { x: 1.2, y: y, w: 3.4, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(d[1], { x: 4.7, y: y, w: 3.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: d[1] === "不是正多邊形" ? C.soft : C.sageDeep });
    s.addText(d[2], { x: 7.9, y: y, w: 4.4, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.soft });
    y += 1.13;
  });
  footer(s, N, false);
  s.addNotes("保底暖身：只判斷是不是「各邊相等、各角也相等」。可即場傳一顆六角螺帽讓學生看。");
})();

// 概念頁 + 圖
(function () {
  const s = newSlide(false);
  title(s, "每個正多邊形都住在一個圓裡", "課時① · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figHexagon(s, 3.85, 3.9, 1.75);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.85, w: 5.3, h: 1.15, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("正 n 邊形都有一個外接圓，\n圓心就是它的中心", { x: 7.6, y: 1.85, w: 4.8, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white, lineSpacingMultiple: 1.15 });
  const items = [
    ["中心角", "360° ÷ n"],
    ["內角", "(n−2) × 180° ÷ n"],
    ["正六邊形", "邊長 ＝ 半徑 R"],
  ];
  let y = 3.25;
  items.forEach((it) => {
    card(s, 7.3, y, 5.3, 0.92, C.white);
    hlBox(s, 7.55, y + 0.16, 1.85, 0.6);
    s.addText(it[0], { x: 7.55, y: y + 0.16, w: 1.85, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 9.65, y: y, w: 2.8, h: 0.92, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink });
    y += 1.05;
  });
  footer(s, N, false);
  s.addNotes("圖像先行：先讓學生數圖上有幾個等腰三角形（6 個），再導出中心角 360÷6＝60°。內角公式是舊知識，順帶複習。");
})();

// 步驟卡
stepCardSlide("課時① · 範例（步驟卡）", "正六邊形：中心角和內角各是多少？",
  "已知：正六邊形，n ＝ 6。求：中心角、內角。", [
  "中心角：把 360° 平均分成 n 份 → 360° ÷ 6 ＝ 60°",
  "內角和：(n−2) × 180° ＝ (6−2) × 180° ＝ 720°",
  "內角：內角和再平均分成 n 份 → 720° ÷ 6 ＝ 120°",
  "檢查：中心角 60° ＋ 內角 120° 的關係合理（都是 60 的倍數）✔",
], "兩個公式都是「先算總數、再平均分」。中心角分的是 360°，內角分的是內角和。請學生說出「分的是哪一個總數」。");

// 特例頁
(function () {
  const s = newSlide(false);
  title(s, "為什麼正六邊形邊長 ＝ 半徑？", "課時① · 特例（要記住）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.75, w: 11.7, h: 1.1, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("正六邊形的邊長，剛好等於它外接圓的半徑 R", { x: 1.1, y: 1.75, w: 11.1, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  const steps = [
    "從圓心連到相鄰兩個頂點，得到一個三角形",
    "兩條邊都是半徑 → 這是等腰三角形",
    "頂角（中心角）＝ 360° ÷ 6 ＝ 60°",
    "等腰＋頂角 60° → 三個角都是 60° → 正三角形",
    "正三角形三邊相等 → 邊長 ＝ 半徑 ✔",
  ];
  let y = 3.1;
  steps.forEach((st, i) => {
    stepCircle(s, 0.85, y + 0.05, i + 1, 0.5);
    s.addText(st, { x: 1.55, y: y, w: 10.9, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 0.7;
  });
  footer(s, N, false);
  s.addNotes("這是全單元最常考的特例。不要只叫學生背，走一次五步推理，他們才記得住。指圖上高亮的那條邊。");
})();

breakSlide("下一頁換你做：先寫 360 ÷ n");

tieredTasks("課時① · 分層練習",
  [
    ["1. 中心角 ＝ 360° ÷ n：\n   (1) 正三角形 ＝ ＿\n   (2) 正六邊形 ＝ ＿", "2. (1) 正六邊形的內角 ＝ ＿\n   (2) 正八邊形的\n       中心角 ＝ ＿"],
    ["3. 正六邊形內接於半徑 4\n   的圓。求邊長和周長", "4. 正十邊形的中心角和\n   內角各是多少？"],
    ["5. 正方形內接於半徑 √2\n   的圓。求邊長和面積", "6. 為什麼正六邊形的邊長\n   剛好等於半徑？\n   用中心角說明"],
  ],
  "解答核對｜A1: (1) 360÷3＝120° (2) 360÷6＝60°；A2: (1) 內角＝(6−2)×180÷6＝720÷6＝120° (2) 360÷8＝45°。 B3: 正六邊形邊長＝半徑＝4，周長＝6×4＝24；B4: 中心角＝360÷10＝36°，內角＝(10−2)×180÷10＝1440÷10＝144°。 C5: 正方形的對角線＝直徑＝2R＝2√2；邊長＝對角線÷√2＝2√2÷√2＝2；面積＝2²＝4；C6: 圓心連相鄰兩頂點成等腰三角形，頂角＝360÷6＝60°，等腰且頂角 60° → 正三角形 → 邊長＝半徑。"
);

summarySlide("課時① · 總結",
  "正多邊形就是把一個圓平均切成 n 份。",
  "中心角 ＝ 360° ÷ n；正六邊形的邊長 ＝ 半徑。")
  .addNotes("回收課時①。保底：能寫出 360÷n、能講出正六邊形的特例就達標。");

// ===================== 課時② 弧長與扇形 =====================
lessonDivider("課時②", "弧長與扇形面積", "會用「佔 360° 的幾分之幾」算弧長和面積")
  .addNotes("進入課時②。整節課只有一個想法：圓心角佔 360° 的幾分之幾，弧長和面積就佔同樣的比例。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "切一塊 pizza", "課時② · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.2, y: 2.05, w: 10.9, h: 1.35, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("角度佔幾分之幾，餅皮和餡料就佔同樣的幾分之幾", { x: 1.55, y: 2.05, w: 10.2, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  const rows = [
    ["切成一半", "180° ÷ 360° ＝ 1/2", "餅皮邊 1/2、面積 1/2"],
    ["切成四分一", "90° ÷ 360° ＝ 1/4", "餅皮邊 1/4、面積 1/4"],
    ["切 120°", "120° ÷ 360° ＝ 1/3", "餅皮邊 1/3、面積 1/3"],
  ];
  let y = 3.75;
  rows.forEach((r) => {
    card(s, 1.2, y, 10.9, 0.86, C.white);
    s.addText(r[0], { x: 1.5, y: y, w: 2.8, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
    s.addText(r[1], { x: 4.4, y: y, w: 3.8, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.sageDeep });
    s.addText(r[2], { x: 8.4, y: y, w: 3.6, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.soft });
    y += 0.98;
  });
  footer(s, N, false);
  s.addNotes("先用 pizza 建立比例直覺，再寫公式。「餅皮邊」＝弧長、「面積」＝扇形面積。這個比喻之後每題都可以回來用。");
})();

// 概念頁 + 圖
(function () {
  const s = newSlide(false);
  title(s, "兩條公式，同一個分數", "課時② · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figSector(s, 3.35, 4.3, 1.75, 115);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.85, w: 5.3, h: 1.15, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("關鍵分數：n ÷ 360\n（圓心角佔整個圓的幾分之幾）", { x: 7.6, y: 1.85, w: 4.8, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.white, lineSpacingMultiple: 1.15 });
  const items = [
    ["弧長", "l ＝ (n÷360) × 2πR", "整圈周長 2πR 的一部分"],
    ["扇形面積", "S ＝ (n÷360) × πR²", "整個圓面積 πR² 的一部分"],
    ["另一條", "S ＝ ½ × l × R", "知道弧長時更快"],
  ];
  let y = 3.25;
  items.forEach((it) => {
    card(s, 7.3, y, 5.3, 0.92, C.white);
    s.addText(it[0], { x: 7.55, y: y + 0.06, w: 1.9, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 7.55, y: y + 0.46, w: 4.8, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.ink });
    s.addText(it[2], { x: 9.5, y: y + 0.06, w: 2.9, h: 0.42, align: "right", valign: "middle", fontFace: F, fontSize: 14, color: C.soft, bold: false });
    y += 1.05;
  });
  footer(s, N, false);
  s.addNotes("兩條公式的前半截一模一樣，都是 n÷360。差別只在後面乘「周長」還是乘「圓面積」。請學生先寫分數，再決定乘什麼。");
})();

// 步驟卡
stepCardSlide("課時② · 範例（步驟卡）", "半徑 6、圓心角 120°：求弧長和面積",
  "已知：R ＝ 6、n ＝ 120°。求：弧長 l、扇形面積 S。（π 保留）", [
  "先寫分數：120 ÷ 360 ＝ 1/3",
  "弧長：l ＝ 1/3 × 2π × 6 ＝ 1/3 × 12π ＝ 4π",
  "面積：S ＝ 1/3 × π × 6² ＝ 1/3 × 36π ＝ 12π",
  "檢查：也可用 S ＝ ½ × l × R ＝ ½ × 4π × 6 ＝ 12π ✔",
], "第 1 步先把分數約簡，後面的乘法就容易很多。第 4 步用另一條公式互相驗算，是很好的自我檢查習慣。");

// 迷思澄清
(function () {
  const s = newSlide(false);
  title(s, "算面積，不要拿周長公式", "課時② · 迷思澄清");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.78, w: 11.7, h: 1.5, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "小明求半徑 5、圓心角 90° 的扇形面積，寫成 S ＝ (90÷360) × 2π × 5   ", options: { fontFace: F, fontSize: 20, color: C.ink } },
    { text: "✗", options: { fontFace: F, fontSize: 22, bold: true, color: C.soft } },
  ], { x: 1.1, y: 1.9, w: 11.1, h: 0.6, align: "left", valign: "middle" });
  s.addText("錯在：他用了周長公式 2πR。求面積要用 πR²。", { x: 1.1, y: 2.55, w: 11.1, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  const rows = [
    ["求弧長", "後面乘 2πR（周長）", "l ＝ (n÷360) × 2πR"],
    ["求面積", "後面乘 πR²（圓面積）", "S ＝ (n÷360) × πR²"],
  ];
  let y = 3.6;
  rows.forEach((r) => {
    card(s, 0.8, y, 11.7, 1.0, C.white);
    s.addText(r[0], { x: 1.1, y: y, w: 2.4, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 3.6, y: y, w: 4.4, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
    s.addText(r[2], { x: 8.1, y: y, w: 4.2, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink });
    y += 1.12;
  });
  hlBox(s, 0.8, 5.9, 11.7, 0.55);
  s.addText("正確答案：S ＝ (90÷360) × π × 5² ＝ 25π ÷ 4 ＝ 6.25π。", { x: 0.8, y: 5.9, w: 11.7, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("防錯提示：R 有沒有平方，就是弧長和面積的分界。寫式後回頭看一眼「有沒有 R²」。用灰色標錯，不用紅色。");
})();

breakSlide("下一頁換你做：先寫 n ÷ 360");

tieredTasks("課時② · 分層練習",
  [
    ["1. 半徑 9、圓心角 60°，\n   弧長 ＝ (60÷360)×2π×9\n   ＝ ＿", "2. 半徑 6、圓心角 90°，\n   求弧長"],
    ["3. 半徑 10、圓心角 72°。\n   求弧長和扇形面積", "4. 扇形半徑 6、弧長 2π。\n   求圓心角和面積"],
    ["5. 圓心角 120°、半徑 9，\n   (1) 求弧長 (2) 求面積\n   (3) 捲成圓錐求底面半徑", "6. 找錯：小明求半徑 5、\n   圓心角 90° 的扇形面積，\n   寫成 (90÷360)×2π×5。\n   錯在哪？正確答案？"],
  ],
  "解答核對｜A1: (60÷360)×2π×9＝(1/6)×18π＝3π；A2: (90÷360)×2π×6＝(1/4)×12π＝3π。 B3: l＝(72÷360)×2π×10＝(1/5)×20π＝4π；S＝(72÷360)×π×10²＝(1/5)×100π＝20π；B4: (n÷360)×2π×6＝2π → (n÷360)×12π＝2π → n÷360＝1/6 → n＝60°；S＝½×l×R＝½×2π×6＝6π。 C5: (1) l＝(120÷360)×2π×9＝(1/3)×18π＝6π (2) S＝½×6π×9＝27π (3) 捲成圓錐後弧長變底面圓周長：6π＝2πr → r＝3；C6: 錯在用了周長公式 2πR，求面積要用 πR²；正確 S＝(90÷360)×π×5²＝25π÷4＝6.25π。"
);

summarySlide("課時② · 總結",
  "先寫 n ÷ 360，再決定乘周長還是乘圓面積。",
  "弧長 l ＝ (n÷360) × 2πR；扇形面積 S ＝ (n÷360) × πR²。")
  .addNotes("回收課時②。保底：能寫出分數 n÷360、能分辨要乘 2πR 還是 πR² 就達標。");

// ===================== 收尾 =====================
(function () {
  const s = newSlide(false);
  title(s, "兩節課，兩句話");
  const data = [
    ["課時①", "正多邊形就是把圓平均切成 n 份。\n中心角 ＝ 360° ÷ n；正六邊形邊長 ＝ 半徑。"],
    ["課時②", "圓心角佔 360° 的幾分之幾，弧長和面積就佔同樣的比例。\nl ＝ (n÷360) × 2πR；S ＝ (n÷360) × πR²。"],
  ];
  let y = 2.1;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.72, C.white);
    badge(s, d[0], 0.95, y + 0.55, 1.9, 0.62, 20);
    s.addText(d[1], { x: 3.05, y: y, w: 9.3, h: 1.72, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink, lineSpacingMultiple: 1.2 });
    y += 1.92;
  });
  hlBox(s, 0.7, 6.1, 11.9, 0.55);
  s.addText("兩節課都在做同一件事：把一整個圓（360°）按比例分下去。", {
    x: 0.7, y: 6.1, w: 11.9, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("整體回收。連結：課時① 分的是角度，課時② 分的是弧長和面積，想法完全一樣。");
})();

(function () {
  const s = newSlide(true);
  s.addText("你已經走完兩節課！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("弧長與扇形，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次看到圓心角，先寫下 n ÷ 360。", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: "9FB8AE" });
  s.addNotes("正向收束，asset-based。肯定策略與過程。");
})();

(function () {
  const s = newSlide(false);
  title(s, "教師備註 · 融合層設計", "供科組 / IEP 會議說明");
  const left = [
    "路線：Accommodation（調整支援）",
    "內容不減、維持初三年級標準，",
    "只改「接觸方式」與「練習鷹架」。",
    "",
    "分層靠學生自選星星，不點名個案。",
    "",
    "節奏：2 課時 × 45 分鐘，",
    "每課時各含 1 個轉換點。",
  ];
  const right = [
    "◆ 統一思路：兩節課都是「按比例分 360°」",
    "◆ pizza 比喻建立比例直覺，下一行即給",
    "   白話對應（弧長＝餅皮邊、面積＝餡）",
    "◆ 原生幾何圖：正六邊形內接圓／扇形",
    "◆ 正六邊形特例走五步推理，不只叫學生背",
    "◆ 迷思澄清：R 有沒有平方＝弧長／面積分界",
    "◆ 步驟卡附互相驗算（兩條面積公式對照）",
    "◆ 保底成功句＋asset-based 用語",
  ];
  card(s, 0.7, 1.9, 5.85, 4.4, C.white);
  s.addText("調整定位", { x: 0.95, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(left.join("\n"), { x: 0.95, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.28 });
  card(s, 6.75, 1.9, 5.85, 4.4, C.white);
  s.addText("融合層做了什麼", { x: 7.0, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(right.join("\n"), { x: 7.0, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 17, color: C.ink, lineSpacingMultiple: 1.28 });
  footer(s, N, false);
  s.addNotes("此頁供教師／IEP 對接用，上課可略過。屬 Accommodation，未剪裁課程內容。");
})();

p.writeFile({ fileName: "簡報_正多邊形弧長與扇形面積_融合抽離版.pptx" }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
