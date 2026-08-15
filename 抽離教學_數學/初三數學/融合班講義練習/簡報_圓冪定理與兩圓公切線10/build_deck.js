// 融合抽離小組 SOIL 教學簡報：圓冪定理與兩圓的公切線（初三 · 單元 10 · 兩課時）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。幾何圖原生繪製。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE";
p.author = "初三數學抽離小組";
p.title = "圓冪定理與兩圓的公切線 兩課時（融合抽離版）";

const UNIT = "圓冪定理與兩圓的公切線";

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
function rightMark(s, vx, vy, u1, u2, size) {
  const d = size || 0.16;
  const P1 = [vx + u1[0] * d, vy + u1[1] * d];
  const P2 = [vx + u2[0] * d, vy + u2[1] * d];
  const Q = [vx + (u1[0] + u2[0]) * d, vy + (u1[1] + u2[1]) * d];
  seg(s, P1[0], P1[1], Q[0], Q[1], { color: C.slate, width: 1.5 });
  seg(s, P2[0], P2[1], Q[0], Q[1], { color: C.slate, width: 1.5 });
}
function unit(ax, ay, bx, by) {
  const dx = bx - ax, dy = by - ay, L = Math.hypot(dx, dy);
  return [dx / L, dy / L];
}
// 過點 P、方向 dirDeg（數學角）的直線與圓 (O,R) 的兩個交點
function chordThrough(P, dirDeg, cx, cy, R) {
  const t = dirDeg * Math.PI / 180;
  const u = [Math.cos(t), -Math.sin(t)];
  const w = [P[0] - cx, P[1] - cy];
  const b = w[0] * u[0] + w[1] * u[1];
  const c = w[0] * w[0] + w[1] * w[1] - R * R;
  const disc = Math.sqrt(b * b - c);
  const t1 = -b - disc, t2 = -b + disc;
  return [[P[0] + t1 * u[0], P[1] + t1 * u[1]], [P[0] + t2 * u[0], P[1] + t2 * u[1]]];
}

// 圖①：相交弦定理 PA·PB ＝ PC·PD
function figIntersectChords(s, cx, cy, R) {
  const P = [cx + R * 0.22, cy + R * 0.12];
  const [A, B] = chordThrough(P, 168, cx, cy, R);
  const [Dp, Cp] = chordThrough(P, 72, cx, cy, R);
  circleOutline(s, cx, cy, R);
  seg(s, A[0], A[1], B[0], B[1], { color: C.sageDeep, width: 2.8 });
  seg(s, Cp[0], Cp[1], Dp[0], Dp[1], { color: C.slate, width: 2.8 });
  dot(s, P[0], P[1], C.ink, 0.16);
  [[A, "A", -0.4, -0.06, "right"], [B, "B", 0.1, -0.06, "left"],
   [Cp, "C", 0.08, -0.24, "left"], [Dp, "D", -0.05, 0.24, "left"]].forEach(([Q, t, dx, dy, al]) => {
    dot(s, Q[0], Q[1], C.soft, 0.13);
    lbl(s, t, Q[0] + dx, Q[1] + dy, { fs: 18, w: 0.4, align: al });
  });
  lbl(s, "P", P[0] + 0.1, P[1] + 0.24, { fs: 17, w: 0.4 });
  // 圖內不再重複寫式子（右欄卡片已有），避免壓住 D 點標籤
}

// 圖②：切割線定理 PT² ＝ PA·PB
function figSecantTangent(s, cx, cy, R) {
  const dd = 2.2 * R;
  const P = [cx - dd, cy];
  const th = Math.acos(R / dd) * 180 / Math.PI;
  const T = onC(cx, cy, R, 180 - th);
  const A = [cx - R, cy], B = [cx + R, cy];
  circleOutline(s, cx, cy, R);
  seg(s, P[0], P[1], B[0], B[1], { color: C.slate, width: 2.8 });      // 割線 PAB
  seg(s, P[0], P[1], T[0], T[1], { color: C.sageDeep, width: 2.8 });   // 切線 PT
  seg(s, cx, cy, T[0], T[1], { color: C.sage, width: 2, dash: "dash" });
  rightMark(s, T[0], T[1], unit(T[0], T[1], cx, cy), unit(T[0], T[1], P[0], P[1]), 0.17);
  dot(s, cx, cy, C.ink, 0.13); dot(s, P[0], P[1], C.ink, 0.15);
  dot(s, T[0], T[1], C.sageDeep, 0.15);
  dot(s, A[0], A[1], C.soft, 0.13); dot(s, B[0], B[1], C.soft, 0.13);
  lbl(s, "P", P[0] - 0.36, P[1] - 0.02, { fs: 18, w: 0.4, align: "right" });
  lbl(s, "T", T[0] - 0.06, T[1] - 0.3, { fs: 18, w: 0.4 });
  lbl(s, "A", A[0] - 0.1, A[1] + 0.28, { fs: 17, w: 0.4, align: "center" });
  lbl(s, "B", B[0] + 0.1, B[1] - 0.02, { fs: 17, w: 0.4 });
  lbl(s, "O", cx - 0.08, cy + 0.26, { fs: 15, color: C.soft, w: 0.4 });
  lbl(s, "PT² ＝ PA · PB", cx - 1.6, cy + R + 0.42, { fs: 17, color: C.sageDeep, w: 3.2, align: "center" });
}

// 圖③：兩圓的五種位置關係（並排小圖）
function figTwoCircles5(s, x0, cy, gap) {
  const R = 0.4, r = 0.24;
  const cases = [
    { d: R + r + 0.26, t: "外離", cond: "d ＞ R＋r", n: "4 條" },
    { d: R + r, t: "外切", cond: "d ＝ R＋r", n: "3 條" },
    { d: R * 0.95, t: "相交", cond: "R−r ＜ d ＜ R＋r", n: "2 條" },
    { d: R - r, t: "內切", cond: "d ＝ R−r", n: "1 條" },
    { d: (R - r) * 0.35, t: "內含", cond: "d ＜ R−r", n: "0 條" },
  ];
  const yName = cy + R + 0.5, yCond = yName + 0.34, yNum = yCond + 0.32;
  cases.forEach((c, i) => {
    const bx = x0 + i * gap;
    circleOutline(s, bx - c.d / 2, cy, R, { width: 2 });
    circleOutline(s, bx + c.d / 2, cy, r, { color: C.sageDeep, width: 2 });
    lbl(s, c.t, bx - 0.85, yName, { fs: 19, color: C.ink, w: 1.7, align: "center" });
    lbl(s, c.cond, bx - 1.05, yCond, { fs: 13, color: C.soft, w: 2.1, align: "center", bold: false });
    lbl(s, "公切線 " + c.n, bx - 0.85, yNum, { fs: 14, color: C.sageDeep, w: 1.7, align: "center" });
  });
}

// ---- 版型 ----
function lessonDivider(tag, name, goal) {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 2.15, w: 3.1, h: 1.0, rectRadius: 0.5, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(tag, { x: 0.9, y: 2.15, w: 3.1, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 34, bold: true, color: C.white });
  s.addText(name, { x: 4.3, y: 2.15, w: 8.3, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 38, bold: true, color: C.white });
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
  s.addText("圓冪定理與兩圓公切線", { x: 0.85, y: 2.35, w: 11.6, h: 1.1, fontFace: F, fontSize: 46, bold: true, color: C.white, align: "left" });
  s.addText("兩課時通關", { x: 0.85, y: 3.45, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "課時① 積相等：圓冪定理", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "      →      ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "課時② 兩圓怎麼擺", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.7, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著兩課時一步一步走", { x: 0.9, y: 5.45, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：兩節課。第一節只有一句話「兩個乘積相等」，第二節只有一句話「比 d 和 R＋r、R−r」。");
})();

// ===================== S2 流程預告 =====================
(function () {
  const s = newSlide(false);
  title(s, "這個單元，我們走兩節課");
  const rows = [
    ["課時①", "圓冪定理", "相交弦、切割線：都是「兩個乘積相等」的同一句話"],
    ["課時②", "兩圓的位置與公切線", "比 d 與 R＋r、R−r：外離／外切／相交／內切／內含"],
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
  s.addNotes("先給地圖。強調兩節課各只有一個核心句子，內容看似多，其實只有兩招。");
})();

// ===================== 課時① 圓冪定理 =====================
lessonDivider("課時①", "圓冪定理", "會用「兩個乘積相等」求未知長度")
  .addNotes("進入課時①。名字聽起來嚇人，但做的事只有一件：把兩段乘起來，等於另外兩段乘起來。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "一句話，兩個定理", "課時① · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.2, y: 2.05, w: 10.9, h: 1.35, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("從同一點出發，兩邊「切下來的兩段」乘起來，一定相等", { x: 1.55, y: 2.05, w: 10.2, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  const rows = [
    ["點在圓內", "兩條弦交在裡面", "PA · PB ＝ PC · PD"],
    ["點在圓外", "一條切線、一條割線", "PT² ＝ PA · PB"],
  ];
  let y = 3.75;
  rows.forEach((r) => {
    card(s, 1.2, y, 10.9, 1.15, C.white);
    s.addText(r[0], { x: 1.5, y: y, w: 2.6, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 4.2, y: y, w: 3.6, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    s.addText(r[2], { x: 7.9, y: y, w: 4.0, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
    y += 1.32;
  });
  s.addText("兩個定理，其實是同一件事的兩種擺法。", { x: 1.2, y: 6.35, w: 10.9, h: 0.42, fontFace: F, fontSize: 19, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給大圖：兩個定理是同一句話。強調「積相等」三個字，之後每一題都回到這三個字。");
})();

// 概念頁：相交弦
(function () {
  const s = newSlide(false);
  title(s, "相交弦：裡面交叉", "課時① · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figIntersectChords(s, 3.85, 3.9, 1.7);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.85, w: 5.3, h: 1.35, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("兩條弦交於 P：\nPA · PB ＝ PC · PD", { x: 7.6, y: 1.85, w: 4.8, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.white, lineSpacingMultiple: 1.2 });
  card(s, 7.3, 3.45, 5.3, 1.3, C.white);
  s.addText("同一條弦上的兩段，\n相乘", { x: 7.55, y: 3.45, w: 4.8, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.2 });
  card(s, 7.3, 5.0, 5.3, 1.3, C.white);
  s.addText("四段裡知道三段，\n就能求第四段", { x: 7.55, y: 5.0, w: 4.8, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.2 });
  footer(s, N, false);
  s.addNotes("配對是關鍵：PA 和 PB 是同一條弦被 P 切出的兩段，PC 和 PD 是另一條。請學生先用手指描出兩條弦，再配對。");
})();

// 步驟卡：相交弦
stepCardSlide("課時① · 範例（步驟卡）", "弦 AB、CD 交於 P，PA＝2、PB＝6、PC＝3，求 PD",
  "已知：PA＝2、PB＝6（同一條弦），PC＝3。求：PD。", [
  "配對：PA、PB 在弦 AB 上；PC、PD 在弦 CD 上",
  "寫定理：PA · PB ＝ PC · PD",
  "代入：2 × 6 ＝ 3 × PD → 12 ＝ 3 × PD",
  "解出：PD ＝ 12 ÷ 3 ＝ 4。檢查：3 × 4 ＝ 12 ✔",
], "第 1 步「配對」防錯：常見錯誤是把不同弦的兩段乘在一起。寫式前先問「這兩段在同一條弦上嗎」。");

// 概念頁：切割線
(function () {
  const s = newSlide(false);
  title(s, "切割線：外面一點", "課時① · 概念");
  card(s, 0.7, 1.72, 6.6, 4.6, C.white);
  figSecantTangent(s, 4.5, 3.85, 1.35);
  s.addShape(p.ShapeType.roundRect, { x: 7.6, y: 1.85, w: 5.0, h: 1.35, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("PT 是切線、PAB 是割線：\nPT² ＝ PA · PB", { x: 7.85, y: 1.85, w: 4.6, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white, lineSpacingMultiple: 1.2 });
  card(s, 7.6, 3.45, 5.0, 1.3, C.white);
  s.addText("PA ＝ 近的一段\nPB ＝ 整條割線", { x: 7.85, y: 3.45, w: 4.6, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink, lineSpacingMultiple: 1.2 });
  card(s, 7.6, 5.0, 5.0, 1.3, C.white);
  s.addText("切線只有一段，\n所以自己乘自己", { x: 7.85, y: 5.0, w: 4.6, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.2 });
  footer(s, N, false);
  s.addNotes("最常錯：把 PB 當成「遠的那一段」。PB 是從 P 到遠端 B 的整條，包含 PA。請學生在圖上用手指從 P 一路劃到 B。");
})();

// 比較頁
(function () {
  const s = newSlide(false);
  title(s, "兩個定理，一句話", "課時① · 統整");
  const head = ["", "相交弦", "切割線"];
  const rows = [
    ["點在哪", "圓內", "圓外"],
    ["畫什麼", "兩條弦", "一切線、一割線"],
    ["式子", "PA · PB ＝ PC · PD", "PT² ＝ PA · PB"],
  ];
  const xs = [0.8, 4.2, 8.4], ws = [3.2, 4.0, 4.1];
  head.forEach((h, i) => {
    if (!h) return;
    s.addShape(p.ShapeType.roundRect, { x: xs[i], y: 1.85, w: ws[i], h: 0.78, rectRadius: 0.1, fill: { color: C.sage }, line: { type: "none" } });
    s.addText(h, { x: xs[i], y: 1.85, w: ws[i], h: 0.78, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
  });
  let y = 2.78;
  rows.forEach((r) => {
    r.forEach((t, i) => {
      card(s, xs[i], y, ws[i], 1.0, i === 0 ? C.block : C.white);
      s.addText(t, { x: xs[i] + 0.12, y: y, w: ws[i] - 0.24, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: i === 2 && r[0] === "式子" ? 20 : 21, bold: i === 0, color: C.ink });
    });
    y += 1.12;
  });
  hlBox(s, 0.8, 6.2, 11.7, 0.55);
  s.addText("共同點：從同一點 P 出發，兩邊的乘積一定相等。", { x: 0.8, y: 6.2, w: 11.7, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("減少記憶負荷：不用背兩條式，記住「P 出發、積相等」，再看點在圓內還是圓外，決定寫哪一條。");
})();

breakSlide("下一頁換你做：先配對，再寫式");

tieredTasks("課時① · 分層練習",
  [
    ["1. 弦 AB、CD 交於 P，\n   PA＝3、PB＝8、PC＝4，\n   求 PD", "2. PT 切 ⊙O 於 T，\n   割線 PAB：PA＝3、\n   PB＝12，求 PT"],
    ["3. 弦 AB、CD 交於 P，\n   PA＝4、PB＝9、PC＝3，\n   求 PD", "4. PT 切 ⊙O 於 T，\n   割線 PAB：PT＝6、\n   PA＝4，求 PB"],
    ["5. AB 是直徑，弦 CD⊥AB\n   於 P。AB＝10、AP＝2，\n   求 CD", "6. PT 切 ⊙O 於 T，割線\n   PAB 過圓心。PT＝8、\n   PA＝4，求半徑"],
  ],
  "解答核對｜A1: 3×8＝4×PD → 24＝4PD → PD＝6；A2: PT²＝3×12＝36 → PT＝6。 B3: 4×9＝3×PD → 36＝3PD → PD＝12；B4: PT²＝PA·PB → 36＝4×PB → PB＝9。 C5: AP＝2、PB＝10−2＝8；相交弦 CP·PD＝2×8＝16；CD⊥直徑 → P 平分 CD → CP＝PD → CP²＝16 → CP＝4 → CD＝8；C6: PT²＝PA·PB → 64＝4×PB → PB＝16；割線過圓心 → AB＝PB−PA＝12 是直徑 → 半徑＝6。"
);

summarySlide("課時① · 總結",
  "從同一點出發，兩邊的乘積一定相等。",
  "圓內用 PA·PB＝PC·PD；圓外用 PT²＝PA·PB（PB 是整條割線）。")
  .addNotes("回收課時①。保底：能講出「積相等」並正確配對兩段就達標。");

// ===================== 課時② 兩圓 =====================
lessonDivider("課時②", "兩圓怎麼擺", "會比 d 與 R＋r、R−r，判斷五種位置")
  .addNotes("進入課時②。和單元 09 的「比大小」是同一個動作，只是這次要跟兩個數比：R＋r 和 R−r。");

// 概念頁：五種位置
(function () {
  const s = newSlide(false);
  title(s, "兩圓的五種擺法", "課時② · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.7, w: 11.7, h: 0.92, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("d ＝ 兩個圓心之間的距離；拿它去跟 R＋r 和 R−r 比大小", { x: 1.1, y: 1.7, w: 11.1, h: 0.92, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
  card(s, 0.8, 2.85, 11.7, 3.5, C.white);
  figTwoCircles5(s, 2.05, 4.0, 2.35);
  footer(s, N, false);
  s.addNotes("由左到右 d 越來越小：從分開、碰到、穿過、內部碰到、完全包住。請學生用兩隻手比劃五個階段。公切線條數也跟著 4→3→2→1→0 遞減。");
})();

// 步驟卡：判斷
stepCardSlide("課時② · 範例（步驟卡）", "R＝5、r＝3，d＝5 時是什麼關係？",
  "已知：兩圓半徑 R＝5、r＝3，圓心距 d＝5。求：位置關係。", [
  "先算兩個界線：R＋r ＝ 5＋3 ＝ 8；R−r ＝ 5−3 ＝ 2",
  "把 d 放進去比：2 ＜ 5 ＜ 8",
  "d 在 R−r 和 R＋r 中間 → 相交",
  "答：相交，有 2 條公切線。檢查：兩圓確實有 2 個交點 ✔",
], "第 1 步一定要先算出 R＋r 和 R−r 兩個界線，寫在紙上，再把 d 擺進去。不要邊算邊猜。");

// 公切線條數
(function () {
  const s = newSlide(false);
  title(s, "公切線有幾條？", "課時② · 統整");
  const head = ["位置", "d 和界線", "公切線"];
  const rows = [
    ["外離", "d ＞ R＋r", "4 條"],
    ["外切", "d ＝ R＋r", "3 條"],
    ["相交", "R−r ＜ d ＜ R＋r", "2 條"],
    ["內切", "d ＝ R−r", "1 條"],
    ["內含", "d ＜ R−r", "0 條"],
  ];
  const xs = [0.8, 4.3, 9.0], ws = [3.3, 4.5, 3.5];
  head.forEach((h, i) => {
    s.addShape(p.ShapeType.roundRect, { x: xs[i], y: 1.8, w: ws[i], h: 0.68, rectRadius: 0.1, fill: { color: C.sage }, line: { type: "none" } });
    s.addText(h, { x: xs[i], y: 1.8, w: ws[i], h: 0.68, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white });
  });
  let y = 2.6;
  rows.forEach((r) => {
    r.forEach((t, i) => {
      card(s, xs[i], y, ws[i], 0.66, i === 0 ? C.block : C.white);
      s.addText(t, { x: xs[i] + 0.1, y: y, w: ws[i] - 0.2, h: 0.66, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: i !== 1, color: i === 2 ? C.sageDeep : C.ink });
    });
    y += 0.76;
  });
  hlBox(s, 0.8, 6.42, 11.7, 0.5);
  s.addText("由上到下，d 越來越小，公切線也越來越少：4、3、2、1、0。", { x: 0.8, y: 6.42, w: 11.7, h: 0.5, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("記憶鷹架：條數是 4、3、2、1、0 順序遞減，不用逐個背。只要排對位置關係的順序，條數自動對上。");
})();

breakSlide("下一頁換你做：先算 R＋r 和 R−r");

tieredTasks("課時② · 分層練習",
  [
    ["1. 兩圓 R＝5、r＝3。\n   R＋r ＝ ＿，\n   R−r ＝ ＿", "2. 填空：兩圓外切時\n   d ＝ ＿；\n   內切時 d ＝ ＿"],
    ["3. R＝5、r＝3，填外離／\n   外切／相交／內切：\n   (1) d＝10 (2) d＝8\n   (3) d＝5 (4) d＝2", "4. 兩圓半徑 2 和 3。\n   (1) 外切時圓心距？\n   (2) 內切時圓心距？"],
    ["5. 兩圓半徑 6 和 4，d＝10。\n   什麼位置關係？\n   有幾條公切線？", "6. 兩圓半徑 6 和 4，\n   d 在什麼範圍時\n   兩圓相交？"],
  ],
  "解答核對｜A1: R＋r＝8、R−r＝2；A2: 外切 d＝R＋r、內切 d＝R−r。 B3: 界線 8 和 2 →(1) 10＞8 外離 (2) 8＝8 外切 (3) 2＜5＜8 相交 (4) 2＝2 內切；B4: (1) 外切 d＝2＋3＝5 (2) 內切 d＝3−2＝1。 C5: R＋r＝10、R−r＝2；d＝10＝R＋r → 外切，3 條公切線；C6: 相交 ⇔ R−r＜d＜R＋r → 2 ＜ d ＜ 10。"
);

summarySlide("課時② · 總結",
  "先算 R＋r 和 R−r 兩個界線，再把 d 擺進去。",
  "外離 4 條、外切 3 條、相交 2 條、內切 1 條、內含 0 條公切線。")
  .addNotes("回收課時②。保底：能算出兩個界線、能判斷外切和內切就達標。");

// ===================== 收尾 =====================
(function () {
  const s = newSlide(false);
  title(s, "兩節課，兩句話");
  const data = [
    ["課時①", "從同一點出發，兩邊的乘積相等。\n圓內 PA·PB＝PC·PD；圓外 PT²＝PA·PB。"],
    ["課時②", "先算 R＋r 和 R−r，再把 d 擺進去比。\n公切線條數：4、3、2、1、0。"],
  ];
  let y = 2.1;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.72, C.white);
    badge(s, d[0], 0.95, y + 0.55, 1.9, 0.62, 20);
    s.addText(d[1], { x: 3.05, y: y, w: 9.3, h: 1.72, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink, lineSpacingMultiple: 1.2 });
    y += 1.92;
  });
  hlBox(s, 0.7, 6.1, 11.9, 0.55);
  s.addText("兩節課都在做同一件事：把圖上的關係，換成一條會算的算式或一句比大小。", {
    x: 0.7, y: 6.1, w: 11.9, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("整體回收。連結單元 09：切割線用到「切線」；兩圓比大小和「直線與圓」是同一個動作。");
})();

(function () {
  const s = newSlide(true);
  s.addText("你已經走完兩節課！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("圓冪定理，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次看到 P 點連出兩條線，記得：兩邊的乘積相等。", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: "9FB8AE" });
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
    "◆ 降低記憶負荷：兩條圓冪式收攏成",
    "   「P 出發、積相等」一句",
    "◆ 公切線條數用 4→3→2→1→0 排序記",
    "◆ 原生幾何圖：相交弦／切割線／",
    "   兩圓五種位置",
    "◆ 步驟卡：先配對、先算界線，防錯在前",
    "◆ 轉換點＋預告：照顧注意力節奏",
    "◆ 保底成功句＋asset-based 用語",
  ];
  card(s, 0.7, 1.9, 5.85, 4.4, C.white);
  s.addText("調整定位", { x: 0.95, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(left.join("\n"), { x: 0.95, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.28 });
  card(s, 6.75, 1.9, 5.85, 4.4, C.white);
  s.addText("融合層做了什麼", { x: 7.0, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(right.join("\n"), { x: 7.0, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 19, color: C.ink, lineSpacingMultiple: 1.25 });
  footer(s, N, false);
  s.addNotes("此頁供教師／IEP 對接用，上課可略過。屬 Accommodation，未剪裁課程內容。");
})();

p.writeFile({ fileName: "簡報_圓冪定理與兩圓公切線_融合抽離版.pptx" }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
