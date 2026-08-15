// 融合抽離小組 SOIL 教學簡報：點、直線與圓、切線（初三 · 單元 09 · 兩課時）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。幾何圖原生繪製。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "點、直線與圓、切線 兩課時（融合抽離版）";

const UNIT = "點、直線與圓、切線";

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

// =====================================================================
// 幾何圖工具（原生繪製）
// =====================================================================
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
// 角弧：涵蓋數學角 a1→a2（逆時針）
// 注意：PptxGenJS 的 angleRange 收到負值會畫成完整橢圓，必須先正規化到 [0,360)
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
// 由點 P 到直線 AB 的垂足
function footOf(px, py, ax, ay, bx, by) {
  const dx = bx - ax, dy = by - ay;
  const t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy);
  return [ax + t * dx, ay + t * dy];
}

// 圖①：點和圓的位置關係（圓內／圓上／圓外）
function figPointCircle(s, cx, cy, R) {
  circleOutline(s, cx, cy, R);
  const P1 = onC(cx, cy, R * 0.5, 165);    // 圓內
  const P2 = onC(cx, cy, R, 45);           // 圓上
  const P3 = onC(cx, cy, R * 1.4, 305);    // 圓外
  [[P1, C.sage], [P2, C.sageDeep], [P3, C.slate]].forEach(([P, col]) => {
    seg(s, cx, cy, P[0], P[1], { color: col, width: 2, dash: "dash" });
    dot(s, P[0], P[1], col, 0.17);
  });
  dot(s, cx, cy, C.ink, 0.15);
  lbl(s, "O", cx - 0.44, cy + 0.12, { fs: 16, color: C.soft, w: 0.4, align: "right" });
  // 標籤只寫位置名（d 與 r 的對照由右欄卡片承擔），避免壓住圓周
  lbl(s, "圓內", P1[0] - 0.5, P1[1] - 0.34, { fs: 16, color: C.sage, w: 1.0, align: "center" });
  lbl(s, "圓上", P2[0] + 0.16, P2[1] - 0.18, { fs: 16, color: C.sageDeep, w: 1.2 });
  lbl(s, "圓外", P3[0] - 0.6, P3[1] + 0.3, { fs: 16, color: C.slate, w: 1.2, align: "center" });
}

// 圖②：直線和圓的三種位置關係（三個小圓並排）
function figLineCircle3(s, x0, cy, R, gap) {
  const cases = [
    { k: 1.55, t: "相離", sub: "d ＞ r ・ 0 個交點" },
    { k: 1.00, t: "相切", sub: "d ＝ r ・ 1 個交點" },
    { k: 0.48, t: "相交", sub: "d ＜ r ・ 2 個交點" },
  ];
  // 文字基線固定，不隨直線高度浮動（否則三欄標籤高低不一、且會掉出卡片）
  const yName = cy + R * 1.55 + 0.34, ySub = yName + 0.36;
  cases.forEach((c, i) => {
    const cxi = x0 + i * gap;
    circleOutline(s, cxi, cy, R);
    const ly = cy + c.k * R;
    seg(s, cxi - R * 1.5, ly, cxi + R * 1.5, ly, { color: C.slate, width: 2.5 });
    seg(s, cxi, cy, cxi, ly, { color: C.sage, width: 2, dash: "dash" });
    dot(s, cxi, cy, C.ink, 0.12);
    lbl(s, "d", cxi + 0.12, cy + 0.18, { fs: 15, color: C.sage, w: 0.35 });
    lbl(s, c.t, cxi - 0.9, yName, { fs: 19, color: C.ink, w: 1.8, align: "center" });
    lbl(s, c.sub, cxi - 1.25, ySub, { fs: 14, color: C.soft, w: 2.5, align: "center", bold: false });
  });
}

// 圖③：切線 l ⊥ 過切點的半徑 OA
function figTangentRadius(s, cx, cy, R) {
  circleOutline(s, cx, cy, R);
  const A = onC(cx, cy, R, 0);
  seg(s, cx, cy, A[0], A[1], { color: C.sageDeep, width: 3 });
  seg(s, A[0], A[1] - R * 0.95, A[0], A[1] + R * 0.95, { color: C.slate, width: 3 });
  rightMark(s, A[0], A[1], [-1, 0], [0, -1], 0.2);
  dot(s, cx, cy, C.ink, 0.15); dot(s, A[0], A[1], C.sageDeep, 0.16);
  lbl(s, "O", cx - 0.05, cy + 0.24, { fs: 17, w: 0.4 });
  lbl(s, "A", A[0] + 0.14, A[1] + 0.22, { fs: 18, w: 0.4 });
  lbl(s, "l（切線）", A[0] + 0.14, A[1] - R * 0.95 + 0.1, { fs: 15, color: C.slate, w: 1.5 });
  lbl(s, "半徑", cx + R * 0.35, cy - 0.26, { fs: 15, color: C.sageDeep, w: 1.0 });
  lbl(s, "切線 ⊥ 過切點的半徑", cx - 1.9, cy + R + 0.34, { fs: 15, color: C.sageDeep, w: 3.8, align: "center" });
}

// 圖④：從圓外一點 P 引兩條切線，PA ＝ PB
function figTwoTangents(s, cx, cy, R) {
  const dd = 2.25 * R;                       // OP
  const th = Math.acos(R / dd) * 180 / Math.PI;
  const A = onC(cx, cy, R, th), B = onC(cx, cy, R, -th);
  const P = [cx + dd, cy];
  circleOutline(s, cx, cy, R);
  seg(s, cx, cy, A[0], A[1], { color: C.sage, width: 2, dash: "dash" });
  seg(s, cx, cy, B[0], B[1], { color: C.sage, width: 2, dash: "dash" });
  seg(s, cx, cy, P[0], P[1], { color: C.soft, width: 1.5, dash: "dash" });
  seg(s, A[0], A[1], P[0], P[1], { color: C.sageDeep, width: 3 });
  seg(s, B[0], B[1], P[0], P[1], { color: C.sageDeep, width: 3 });
  rightMark(s, A[0], A[1], unit(A[0], A[1], cx, cy), unit(A[0], A[1], P[0], P[1]), 0.18);
  rightMark(s, B[0], B[1], unit(B[0], B[1], cx, cy), unit(B[0], B[1], P[0], P[1]), 0.18);
  dot(s, cx, cy, C.ink, 0.15); dot(s, P[0], P[1], C.ink, 0.15);
  dot(s, A[0], A[1], C.sageDeep, 0.15); dot(s, B[0], B[1], C.sageDeep, 0.15);
  lbl(s, "O", cx - 0.48, cy - 0.02, { fs: 17, w: 0.4, align: "right" });
  lbl(s, "P", P[0] + 0.12, P[1] - 0.02, { fs: 18, w: 0.4 });
  lbl(s, "A", A[0] - 0.06, A[1] - 0.3, { fs: 18, w: 0.4 });
  lbl(s, "B", B[0] - 0.06, B[1] + 0.28, { fs: 18, w: 0.4 });
  lbl(s, "PA ＝ PB", cx + R * 0.5, cy + R + 0.46, { fs: 16, color: C.sageDeep, w: 2.2, align: "center" });
}

// 圖⑤：△ABC 的內切圓，切點 D、E、F
function figIncircle(s, cx, cy, S) {
  const A = [cx - S, cy + S * 0.62], B = [cx + S, cy + S * 0.62], Cv = [cx - S * 0.18, cy - S * 0.78];
  const la = Math.hypot(B[0] - Cv[0], B[1] - Cv[1]);   // a = |BC|，對頂點 A
  const lb = Math.hypot(A[0] - Cv[0], A[1] - Cv[1]);   // b = |CA|，對頂點 B
  const lc = Math.hypot(A[0] - B[0], A[1] - B[1]);     // c = |AB|，對頂點 C
  const sum = la + lb + lc;
  const I = [(la * A[0] + lb * B[0] + lc * Cv[0]) / sum, (la * A[1] + lb * B[1] + lc * Cv[1]) / sum];
  const D = footOf(I[0], I[1], A[0], A[1], B[0], B[1]);   // 切 AB
  const E = footOf(I[0], I[1], B[0], B[1], Cv[0], Cv[1]); // 切 BC
  const Fp = footOf(I[0], I[1], Cv[0], Cv[1], A[0], A[1]);// 切 CA
  const r = Math.hypot(D[0] - I[0], D[1] - I[1]);
  seg(s, A[0], A[1], B[0], B[1], { color: C.ink, width: 2.5 });
  seg(s, B[0], B[1], Cv[0], Cv[1], { color: C.ink, width: 2.5 });
  seg(s, Cv[0], Cv[1], A[0], A[1], { color: C.ink, width: 2.5 });
  circleOutline(s, I[0], I[1], r, { color: C.sageDeep, width: 2 });
  dot(s, I[0], I[1], C.sageDeep, 0.12);
  [[D, "D"], [E, "E"], [Fp, "F"]].forEach(([P]) => dot(s, P[0], P[1], C.sage, 0.15));
  lbl(s, "I", I[0] + 0.12, I[1] - 0.02, { fs: 15, color: C.sageDeep, w: 0.4 });
  lbl(s, "A", A[0] - 0.36, A[1] + 0.14, { fs: 17, w: 0.4, align: "right" });
  lbl(s, "B", B[0] + 0.1, B[1] + 0.14, { fs: 17, w: 0.4 });
  lbl(s, "C", Cv[0] - 0.05, Cv[1] - 0.28, { fs: 17, w: 0.4 });
  lbl(s, "D", D[0] - 0.05, D[1] + 0.26, { fs: 16, color: C.sage, w: 0.4 });
  lbl(s, "E", E[0] + 0.16, E[1] - 0.06, { fs: 16, color: C.sage, w: 0.4 });
  lbl(s, "F", Fp[0] - 0.42, Fp[1] - 0.06, { fs: 16, color: C.sage, w: 0.4, align: "right" });
}

// =====================================================================
// 版型產生器
// =====================================================================
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

// =====================================================================
// S1 封面
// =====================================================================
(function () {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.45, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.45, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("點、直線與圓、切線", { x: 0.85, y: 2.35, w: 11.6, h: 1.1, fontFace: F, fontSize: 50, bold: true, color: C.white, align: "left" });
  s.addText("兩課時通關", { x: 0.85, y: 3.45, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "課時① 比大小：d 與 r", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "      →      ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "課時② 切線三招", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.7, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著兩課時一步一步走", { x: 0.9, y: 5.45, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：這個單元只有兩節課，而且第一節只需要「比大小」。每一節都是：學一招 → 看老師示範 → 自己挑星星練習。");
})();

// =====================================================================
// S2 流程預告頁
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "這個單元，我們走兩節課");
  const rows = [
    ["課時①", "點、直線與圓的位置關係", "只做一件事：把 d 和 r 比大小，判斷在圓內／圓上／圓外，相離／相切／相交"],
    ["課時②", "切線的判定、性質與切線長", "切線 ⊥ 過切點的半徑；從圓外一點引的兩條切線一樣長"],
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
  s.addNotes("先給地圖：只有兩節課，減少焦慮。強調課時① 的判準其實只有一句「比大小」，門檻很低。");
})();

// =====================================================================
// 課時① 位置關係
// =====================================================================
lessonDivider("課時①", "點、直線與圓", "會比較 d 與 r，判斷位置關係")
  .addNotes("進入課時①。整節課的核心只有一句：把 d 和 r 比大小。不用計算，只要判斷。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "日出：太陽和地平線", "課時① · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.2, y: 2.0, w: 10.9, h: 1.35, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("太陽升起的過程，剛好走過直線與圓的三種關係", { x: 1.55, y: 2.0, w: 10.2, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  const rows = [
    ["太陽還在地平線下", "沒有露出來", "相離"],
    ["太陽剛好碰到地平線", "只碰到一點", "相切"],
    ["太陽升上來一半", "地平線穿過太陽", "相交"],
  ];
  let y = 3.7;
  rows.forEach((r) => {
    card(s, 1.2, y, 10.9, 0.86, C.white);
    s.addText(r[0], { x: 1.5, y: y, w: 4.4, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
    s.addText(r[1], { x: 6.0, y: y, w: 3.6, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    s.addText(r[2], { x: 9.8, y: y, w: 2.0, h: 0.86, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    y += 0.98;
  });
  footer(s, N, false);
  s.addNotes("保底暖身：用日出畫面建立直覺，先不出現 d 和 r。請學生用手比劃三個階段。");
})();

// 概念頁：點和圓
(function () {
  const s = newSlide(false);
  title(s, "點在圓的哪裡？比 d 和 r", "課時① · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figPointCircle(s, 3.85, 4.0, 1.6);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.85, w: 5.3, h: 1.15, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("d ＝ 點到圓心的距離\nr ＝ 半徑", { x: 7.6, y: 1.85, w: 4.8, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white, lineSpacingMultiple: 1.15 });
  const items = [
    ["d ＜ r", "點在圓內"],
    ["d ＝ r", "點在圓上"],
    ["d ＞ r", "點在圓外"],
  ];
  let y = 3.3;
  items.forEach((it) => {
    card(s, 7.3, y, 5.3, 0.86, C.white);
    hlBox(s, 7.55, y + 0.14, 1.9, 0.58);
    s.addText(it[0], { x: 7.55, y: y + 0.14, w: 1.9, h: 0.58, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 9.7, y: y, w: 2.7, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 1.0;
  });
  footer(s, N, false);
  s.addNotes("口訣：小在內、等在上、大在外。請學生把三行讀出來一次。不用背，看圖就知道：離圓心越遠，越在外面。");
})();

// 概念頁：直線和圓
(function () {
  const s = newSlide(false);
  title(s, "直線和圓：同一套比大小", "課時① · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.7, w: 11.7, h: 0.92, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("這次 d ＝ 圓心到直線的距離（畫一條垂線量）", { x: 1.1, y: 1.7, w: 11.1, h: 0.92, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.white });
  card(s, 0.8, 2.85, 11.7, 3.5, C.white);
  figLineCircle3(s, 2.95, 4.25, 0.82, 3.7);
  footer(s, N, false);
  s.addNotes("和上一頁完全同一套判準，只是 d 換了意思。強調：直線和圓最多只有 2 個交點，沒有 3 個。三張圖從左到右，d 越來越小。");
})();

// 比較頁
(function () {
  const s = newSlide(false);
  title(s, "兩張表，其實是同一張", "課時① · 統整");
  const head = ["比大小", "點和圓", "直線和圓"];
  const rows = [
    ["d ＜ r", "點在圓內", "相交（2 個交點）"],
    ["d ＝ r", "點在圓上", "相切（1 個交點）"],
    ["d ＞ r", "點在圓外", "相離（0 個交點）"],
  ];
  const xs = [0.8, 4.7, 8.6], ws = [3.7, 3.7, 3.9];
  head.forEach((h, i) => {
    s.addShape(p.ShapeType.roundRect, { x: xs[i], y: 1.85, w: ws[i], h: 0.78, rectRadius: 0.1, fill: { color: C.sage }, line: { type: "none" } });
    s.addText(h, { x: xs[i], y: 1.85, w: ws[i], h: 0.78, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
  });
  let y = 2.78;
  rows.forEach((r) => {
    r.forEach((t, i) => {
      card(s, xs[i], y, ws[i], 1.0, i === 0 ? C.block : C.white);
      s.addText(t, { x: xs[i], y: y, w: ws[i], h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: i === 0, color: C.ink });
    });
    y += 1.12;
  });
  hlBox(s, 0.8, 6.2, 11.7, 0.55);
  s.addText("先量 d，再和 r 比大小 —— 兩題都是同一個動作。", { x: 0.8, y: 6.2, w: 11.7, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("減少記憶負荷：不是兩套規則，是一套。提醒 d 的意思會換（點到圓心／圓心到直線），但比大小的動作不變。");
})();

breakSlide("下一頁換你做：只要比大小");

tieredTasks("課時① · 分層練習",
  [
    ["1. ⊙O 半徑 r＝5，填圓內／\n   圓上／圓外：\n   (1) d＝3 (2) d＝5 (3) d＝7", "2. 半徑 r＝4，填相交／\n   相切／相離：\n   (1) d＝2 (2) d＝4 (3) d＝6"],
    ["3. ⊙O 半徑 3，圓心到直線 l\n   的距離是 3。l 與 ⊙O 有\n   幾個公共點？為什麼？", "4. ⊙O 半徑 6，圓心到直線 l\n   的距離是 6.5。兩者什麼\n   關係？有幾個公共點？"],
    ["5. 找錯：小明說「直線與圓\n   最多有 3 個公共點」。\n   對嗎？請說明", "6. 半徑 5 的圓，圓心到直線\n   的距離 d 在什麼範圍，\n   直線與圓才相交？"],
  ],
  "解答核對｜A1: (1) d＝3＜5 圓內 (2) d＝5＝5 圓上 (3) d＝7＞5 圓外；A2: (1) 2＜4 相交 (2) 4＝4 相切 (3) 6＞4 相離。 B3: d＝r＝3 → 相切，1 個公共點；B4: d＝6.5＞r＝6 → 相離，0 個公共點。 C5: 不對，直線與圓最多 2 個公共點（相交時）；C6: 相交 ⇔ d＜r，且距離不為負 → 0 ≤ d ＜ 5。"
);

summarySlide("課時① · 總結",
  "判斷位置關係，只做一件事：把 d 和 r 比大小。",
  "小在內、等在上（相切）、大在外（相離）；直線與圓最多 2 個交點。")
  .addNotes("回收課時①。保底：能講出「比大小」三個字並套對一題就達標。");

// =====================================================================
// 課時② 切線
// =====================================================================
lessonDivider("課時②", "切線三招", "會用切線 ⊥ 半徑、切線長相等解題")
  .addNotes("進入課時②。三招：判定、性質（⊥）、切線長相等。重點在第二、三招，做題時最常用。");

// 概念頁：切線判定與性質
(function () {
  const s = newSlide(false);
  title(s, "切線：碰一點，而且垂直", "課時② · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figTangentRadius(s, 3.4, 4.0, 1.55);
  const items = [
    ["判定", "經過半徑的外端、\n並且垂直這條半徑的直線，\n就是圓的切線"],
    ["性質", "圓的切線，\n垂直於過切點的半徑"],
  ];
  let y = 1.85;
  items.forEach((it, i) => {
    card(s, 7.3, y, 5.3, 2.15, C.white);
    s.addShape(p.ShapeType.roundRect, { x: 7.3, y: y, w: 5.3, h: 0.68, rectRadius: 0.12, fill: { color: i === 0 ? C.sage : C.sageDeep }, line: { type: "none" } });
    s.addText(it[0], { x: 7.3, y: y, w: 5.3, h: 0.68, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
    s.addText(it[1], { x: 7.6, y: y + 0.8, w: 4.8, h: 1.25, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.25 });
    y += 2.35;
  });
  footer(s, N, false);
  s.addNotes("做題時只用「性質」那一句：看到切線，馬上在切點畫直角。判定留給證明題，這節不深入。");
})();

// 步驟卡範例
stepCardSlide("課時② · 範例（步驟卡）", "PA 切 ⊙O 於 A，OA＝3、PA＝4，求 OP",
  "已知：PA 是切線、切點 A，半徑 OA＝3，切線段 PA＝4。求：OP。", [
  "看到切線，先在切點 A 畫直角：∠OAP ＝ 90°",
  "認出直角三角形 OAP：兩股是 OA＝3、PA＝4，斜邊是 OP",
  "勾股定理：OP² ＝ 3² ＋ 4² ＝ 9 ＋ 16 ＝ 25",
  "開方：OP ＝ 5。檢查：斜邊 OP 最長 ✔（5 ＞ 4 ＞ 3）",
], "第 1 步是關鍵：切線題的第一個動作永遠是「畫直角」。畫完之後，題目就變回熟悉的勾股定理題。");

// 概念頁：切線長定理
(function () {
  const s = newSlide(false);
  title(s, "從圓外一點，兩條切線一樣長", "課時② · 概念");
  card(s, 0.7, 1.72, 6.9, 4.6, C.white);
  figTwoTangents(s, 3.0, 4.0, 1.25);
  s.addShape(p.ShapeType.roundRect, { x: 7.9, y: 1.85, w: 4.7, h: 1.5, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("PA ＝ PB\n（切線長定理）", { x: 8.2, y: 1.85, w: 4.2, h: 1.5, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white, lineSpacingMultiple: 1.2 });
  card(s, 7.9, 3.6, 4.7, 1.3, C.white);
  s.addText("OP 平分 ∠APB", { x: 8.15, y: 3.6, w: 4.2, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
  card(s, 7.9, 5.15, 4.7, 1.15, C.white);
  s.addText("兩個切點各有一個直角", { x: 8.15, y: 5.15, w: 4.2, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
  footer(s, N, false);
  s.addNotes("圖像先行：請學生看圖說出「兩條粗線一樣長」。這個定理在幾何題最常用來換邊長。");
})();

// 範例頁：內切圓（原題 C7）
(function () {
  const s = newSlide(false);
  title(s, "三角形的內切圓：邊長怎麼換", "課時② · 範例（進階）");
  card(s, 0.7, 1.72, 5.7, 4.6, C.white);
  figIncircle(s, 3.5, 4.05, 1.65);
  s.addShape(p.ShapeType.roundRect, { x: 6.8, y: 1.8, w: 5.8, h: 1.15, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText("內切圓切三邊於 D、E、F。\nAD＝4、BE＝5、CF＝6，求周長。", { x: 7.05, y: 1.8, w: 5.3, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink, lineSpacingMultiple: 1.15 });
  const steps = [
    "同一頂點出發的兩條切線長相等",
    "AD＝AF＝4、BD＝BE＝5、CE＝CF＝6",
    "周長 ＝ 2 × (4 ＋ 5 ＋ 6) ＝ 30",
  ];
  let y = 3.2;
  steps.forEach((st, i) => {
    stepCircle(s, 6.8, y + 0.2, i + 1, 0.5);
    s.addText(st, { x: 7.5, y: y, w: 5.1, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
    y += 1.05;
  });
  footer(s, N, false);
  s.addNotes("三角形的每個頂點都是「圓外一點」，所以每個頂點都有兩條等長的切線。周長剛好是三對切線長，所以乘 2。");
})();

// 迷思澄清
(function () {
  const s = newSlide(false);
  title(s, "直線與圓，最多幾個公共點？", "課時② · 迷思澄清");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.78, w: 11.7, h: 1.5, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "小明說：「一條直線與一個圓最多有 3 個公共點。」  ", options: { fontFace: F, fontSize: 21, color: C.ink } },
    { text: "✗ 不對", options: { fontFace: F, fontSize: 22, bold: true, color: C.soft } },
  ], { x: 1.1, y: 1.9, w: 11.1, h: 0.6, align: "left", valign: "middle" });
  s.addText("直線與圓最多只有 2 個公共點（相交的時候）。", { x: 1.1, y: 2.55, w: 11.1, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  const rows = [
    ["相離", "0 個", "d ＞ r"],
    ["相切", "1 個", "d ＝ r"],
    ["相交", "2 個（最多）", "d ＜ r"],
  ];
  let y = 3.55;
  rows.forEach((r) => {
    card(s, 0.8, y, 11.7, 0.9, C.white);
    s.addText(r[0], { x: 1.1, y: y, w: 3.0, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 4.3, y: y, w: 4.0, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    s.addText(r[2], { x: 8.6, y: y, w: 3.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.slate });
    y += 1.02;
  });
  footer(s, N, false);
  s.addNotes("澄清方法：讓學生用尺在紙上畫圓，試試看能不能讓一條直線碰到 3 點——做不到。「最多 2 個」是判斷題常考點。");
})();

breakSlide("下一頁換你做：先在切點畫直角");

tieredTasks("課時② · 分層練習",
  [
    ["1. 填空：PA 切 ⊙O 於 A，\n   則 ∠OAP ＝ ＿°", "2. 填空：PA、PB 是 ⊙O 的\n   兩條切線，PA＝12，\n   則 PB ＝ ＿"],
    ["3. PA 切 ⊙O 於 A，\n   OA＝6、PA＝8，求 OP", "4. 從圓外一點 P 引兩條切線\n   PA、PB。若 PA＝12，\n   求 PB，並說明理由"],
    ["5. PA、PB 是 ⊙O 的兩條\n   切線，∠APB＝70°，\n   求 ∠AOB", "6. 內切圓切 △ABC 三邊於\n   D、E、F。AD＝4、\n   BE＝5、CF＝6，\n   求 △ABC 周長"],
  ],
  "解答核對｜A1: 切線 ⊥ 過切點的半徑 → ∠OAP＝90°；A2: 切線長定理 → PB＝PA＝12。 B3: ∠OAP＝90° → OP＝√(6²+8²)＝√(36+64)＝√100＝10；B4: PB＝12，理由是從圓外一點引的兩條切線長相等（切線長定理）。 C5: 四邊形 PAOB 中 ∠PAO＝∠PBO＝90°，四邊形內角和 360° → ∠APB＋∠AOB＝180°，∠AOB＝180−70＝110°；C6: AD＝AF＝4、BD＝BE＝5、CE＝CF＝6，周長＝2×(4+5+6)＝30。"
);

summarySlide("課時② · 總結",
  "看到切線，第一個動作就是在切點畫直角。",
  "切線 ⊥ 過切點的半徑；從圓外一點引的兩條切線一樣長。")
  .addNotes("回收課時②。保底：能在切點標出 90°、能講出「兩條切線一樣長」就達標。");

// =====================================================================
// 收尾
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "兩節課，兩句話");
  const data = [
    ["課時①", "判斷位置關係，只要把 d 和 r 比大小。\n小在內、等在上、大在外；直線與圓最多 2 個交點。"],
    ["課時②", "看到切線，先在切點畫直角。\n切線 ⊥ 過切點的半徑；兩條切線長相等。"],
  ];
  let y = 2.1;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.72, C.white);
    badge(s, d[0], 0.95, y + 0.55, 1.9, 0.62, 20);
    s.addText(d[1], { x: 3.05, y: y, w: 9.3, h: 1.72, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink, lineSpacingMultiple: 1.2 });
    y += 1.92;
  });
  hlBox(s, 0.7, 6.1, 11.9, 0.55);
  s.addText("兩節課都在做同一件事：把圖上的關係，換成一個會算的直角三角形或一句比大小。", {
    x: 0.7, y: 6.1, w: 11.9, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("整體回收。連結上一單元 08：垂徑定理也是「畫直角三角形」。連結下一單元 10：圓冪定理會再用切線。");
})();

(function () {
  const s = newSlide(true);
  s.addText("你已經走完兩節課！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("點、直線與切線，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次看到「切線」，記得先在切點畫直角。", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: "9FB8AE" });
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
    "◆ 降低記憶負荷：兩張位置關係表",
    "   統整成同一套「比大小」判準",
    "◆ 原生幾何圖：點與圓／直線與圓三態／",
    "   切線⊥半徑／兩切線／內切圓",
    "◆ 步驟卡：一步一行、編號、附自我檢查",
    "◆ 轉換點＋預告：照顧注意力節奏",
    "◆ 迷思澄清：最多 2 個公共點",
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

// ---- 輸出 ----
p.writeFile({ fileName: "簡報_點直線與圓及切線_融合抽離版.pptx" }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
