// 融合抽離小組 SOIL 教學簡報：圓的有關性質（初三 · 單元 08 · 四課時）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。幾何圖原生繪製。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "圓的有關性質 四課時（融合抽離版）";

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
  s.addText("初三數學 · 圓的有關性質（抽離小組·融合版）", {
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
// 數學角度（自 x 正向逆時針）→ 畫布座標
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
// 直角記號：頂點 V，沿兩單位方向 u1、u2 畫小方角
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

// 圖①：圓的基本概念（圓心、半徑、弦、直徑、弧）
function figCircleBasic(s, cx, cy, R) {
  circleOutline(s, cx, cy, R);
  const A = onC(cx, cy, R, 62);
  const Fp = onC(cx, cy, R, 180), G = onC(cx, cy, R, 0);
  const B = onC(cx, cy, R, 222), Cp = onC(cx, cy, R, 318);
  angArc(s, cx, cy, R, 0, 62, { color: C.sage, width: 5 });           // 弧 AG（加粗高亮）
  seg(s, cx, cy, A[0], A[1], { color: C.sageDeep, width: 2.5 });      // 半徑
  seg(s, Fp[0], Fp[1], G[0], G[1], { color: C.slate, width: 2.5 });   // 直徑
  seg(s, B[0], B[1], Cp[0], Cp[1], { color: C.ink, width: 2.5 });     // 弦
  dot(s, cx, cy, C.ink, 0.15);
  [[A, "A"], [Fp, "F"], [G, "G"], [B, "B"], [Cp, "C"]].forEach(([P, t]) => dot(s, P[0], P[1], C.soft, 0.13));
  lbl(s, "O（圓心）", cx + 0.1, cy + 0.22, { fs: 15, color: C.soft, w: 1.6 });
  lbl(s, "A", A[0] + 0.08, A[1] - 0.16, { fs: 17, w: 0.4 });
  lbl(s, "F", Fp[0] - 0.38, Fp[1] - 0.02, { fs: 17, w: 0.4, align: "right" });
  lbl(s, "G", G[0] + 0.08, G[1] - 0.02, { fs: 17, w: 0.4 });
  lbl(s, "B", B[0] - 0.42, B[1] + 0.1, { fs: 17, w: 0.4, align: "right" });
  lbl(s, "C", Cp[0] + 0.1, Cp[1] + 0.1, { fs: 17, w: 0.4 });
  lbl(s, "半徑 r", cx + 0.36, cy - 0.52, { fs: 15, color: C.sageDeep, w: 1.2 });
  lbl(s, "直徑 FG", cx - 1.0, cy - 0.24, { fs: 15, color: C.slate, w: 1.3 });
  lbl(s, "弦 BC", cx - 0.45, cy + R * 0.72, { fs: 15, color: C.ink, w: 1.1 });
  lbl(s, "弧 AG", cx + (R + 0.2) * Math.cos(31 * Math.PI / 180) - 0.28,
      cy - (R + 0.2) * Math.sin(31 * Math.PI / 180), { fs: 15, color: C.sage, w: 1.1 });
}

// 圖②：垂徑定理（直徑 CD ⊥ 弦 AB 於 M，直角三角形 OMA）
function figChordPerp(s, cx, cy, R) {
  const k = 0.55;                       // 弦離圓心 = 0.55R（在圓心上方）
  const half = R * Math.sqrt(1 - k * k);
  const My = cy - k * R;
  const A = [cx - half, My], B = [cx + half, My];
  const Ctop = [cx, cy - R], Dbot = [cx, cy + R];
  // 直角三角形 OMA 淺色底（右角在右上角 → rtTriangle 需 flipH + flipV）
  s.addShape(p.ShapeType.rtTriangle, {
    x: cx - half, y: My, w: half, h: cy - My,
    flipH: true, flipV: true,
    fill: { color: C.block }, line: { type: "none" },
  });
  circleOutline(s, cx, cy, R);
  seg(s, Ctop[0], Ctop[1], Dbot[0], Dbot[1], { color: C.slate, width: 2 });    // 直徑 CD
  seg(s, A[0], A[1], B[0], B[1], { color: C.ink, width: 2.5 });                // 弦 AB
  seg(s, cx, cy, A[0], A[1], { color: C.sageDeep, width: 3 });                 // 半徑 OA
  seg(s, cx, My, cx, cy, { color: C.sage, width: 4 });                         // 距離 OM = d（疊在 CD 上）
  rightMark(s, cx, My, [-1, 0], [0, 1], 0.19);
  dot(s, cx, cy, C.ink, 0.15); dot(s, cx, My, C.slate, 0.13);
  dot(s, A[0], A[1], C.soft, 0.13); dot(s, B[0], B[1], C.soft, 0.13);
  dot(s, Ctop[0], Ctop[1], C.soft, 0.12); dot(s, Dbot[0], Dbot[1], C.soft, 0.12);
  lbl(s, "O", cx + 0.1, cy + 0.2, { fs: 17, w: 0.4 });
  lbl(s, "M", cx + 0.12, My - 0.2, { fs: 17, w: 0.4, color: C.slate });
  lbl(s, "A", A[0] - 0.38, A[1] - 0.02, { fs: 17, w: 0.4, align: "right" });
  lbl(s, "B", B[0] + 0.1, B[1] - 0.02, { fs: 17, w: 0.4 });
  lbl(s, "C", Ctop[0] + 0.1, Ctop[1] - 0.16, { fs: 17, w: 0.4 });
  lbl(s, "D", Dbot[0] + 0.1, Dbot[1] + 0.14, { fs: 17, w: 0.4 });
  lbl(s, "AM ＝ MB", cx - half / 2 - 0.8, My - 0.34, { fs: 15, color: C.ink, w: 1.6, align: "center" });
  lbl(s, "d", cx + 0.14, (My + cy) / 2 - 0.02, { fs: 17, color: C.sageDeep, w: 0.4 });
  lbl(s, "r", cx - half / 2 - 0.6, (My + cy) / 2 + 0.14, { fs: 17, color: C.sageDeep, w: 0.4, align: "right" });
}

// 圖③：圓周角定理 ∠AOB = 2∠ACB
function figInscribed(s, cx, cy, R) {
  const A = onC(cx, cy, R, 205), B = onC(cx, cy, R, 335), Cp = onC(cx, cy, R, 82);
  circleOutline(s, cx, cy, R);
  seg(s, cx, cy, A[0], A[1], { color: C.sageDeep, width: 2.5 });
  seg(s, cx, cy, B[0], B[1], { color: C.sageDeep, width: 2.5 });
  seg(s, Cp[0], Cp[1], A[0], A[1], { color: C.slate, width: 2.5 });
  seg(s, Cp[0], Cp[1], B[0], B[1], { color: C.slate, width: 2.5 });
  angArc(s, cx, cy, 0.45, 205, 335, { color: C.sageDeep, width: 3 });
  const u1 = unit(Cp[0], Cp[1], A[0], A[1]), u2 = unit(Cp[0], Cp[1], B[0], B[1]);
  const a1 = Math.atan2(-(A[1] - Cp[1]), A[0] - Cp[0]) * 180 / Math.PI;
  const a2 = Math.atan2(-(B[1] - Cp[1]), B[0] - Cp[0]) * 180 / Math.PI;
  angArc(s, Cp[0], Cp[1], 0.5, Math.min(a1, a2), Math.max(a1, a2), { color: C.slate, width: 2.5 });
  dot(s, cx, cy, C.ink, 0.15);
  dot(s, A[0], A[1], C.soft, 0.13); dot(s, B[0], B[1], C.soft, 0.13); dot(s, Cp[0], Cp[1], C.soft, 0.14);
  lbl(s, "O", cx - 0.52, cy - 0.04, { fs: 17, w: 0.4, align: "right" });
  lbl(s, "A", A[0] - 0.4, A[1] + 0.06, { fs: 18, w: 0.4, align: "right" });
  lbl(s, "B", B[0] + 0.12, B[1] + 0.06, { fs: 18, w: 0.4 });
  lbl(s, "C", Cp[0] - 0.05, Cp[1] - 0.3, { fs: 18, w: 0.4 });
  lbl(s, "圓心角", cx - 0.6, cy + 0.68, { fs: 15, color: C.sageDeep, w: 1.2, align: "center" });
  lbl(s, "圓周角", Cp[0] - 0.6, Cp[1] + 0.82, { fs: 15, color: C.slate, w: 1.2, align: "center" });
  void u1; void u2;
}

// 圖④：直徑所對的圓周角是直角
function figDiameterRight(s, cx, cy, R) {
  const A = onC(cx, cy, R, 180), B = onC(cx, cy, R, 0), Cp = onC(cx, cy, R, 63);
  circleOutline(s, cx, cy, R);
  seg(s, A[0], A[1], B[0], B[1], { color: C.slate, width: 2.5 });
  seg(s, A[0], A[1], Cp[0], Cp[1], { color: C.sageDeep, width: 2.5 });
  seg(s, Cp[0], Cp[1], B[0], B[1], { color: C.sageDeep, width: 2.5 });
  rightMark(s, Cp[0], Cp[1], unit(Cp[0], Cp[1], A[0], A[1]), unit(Cp[0], Cp[1], B[0], B[1]), 0.2);
  dot(s, cx, cy, C.ink, 0.13);
  dot(s, A[0], A[1], C.soft, 0.13); dot(s, B[0], B[1], C.soft, 0.13); dot(s, Cp[0], Cp[1], C.soft, 0.14);
  lbl(s, "O", cx - 0.06, cy + 0.22, { fs: 15, color: C.soft, w: 0.4 });
  lbl(s, "A", A[0] - 0.38, A[1] - 0.02, { fs: 18, w: 0.4, align: "right" });
  lbl(s, "B", B[0] + 0.1, B[1] - 0.02, { fs: 18, w: 0.4 });
  lbl(s, "C", Cp[0] + 0.02, Cp[1] - 0.3, { fs: 18, w: 0.4 });
  lbl(s, "AB 是直徑 → ∠ACB = 90°", cx - 1.85, cy + R + 0.3, { fs: 15, color: C.sageDeep, w: 3.8, align: "center" });
}

// 圖⑤：圓內接四邊形 ∠A + ∠C = 180°
function figCyclicQuad(s, cx, cy, R) {
  const A = onC(cx, cy, R, 118), B = onC(cx, cy, R, 202), Cp = onC(cx, cy, R, 305), D = onC(cx, cy, R, 38);
  circleOutline(s, cx, cy, R);
  seg(s, A[0], A[1], B[0], B[1], { color: C.ink, width: 2.5 });
  seg(s, B[0], B[1], Cp[0], Cp[1], { color: C.ink, width: 2.5 });
  seg(s, Cp[0], Cp[1], D[0], D[1], { color: C.ink, width: 2.5 });
  seg(s, D[0], D[1], A[0], A[1], { color: C.ink, width: 2.5 });
  [[A, "A"], [B, "B"], [Cp, "C"], [D, "D"]].forEach(([P]) => dot(s, P[0], P[1], C.sageDeep, 0.14));
  lbl(s, "A", A[0] - 0.34, A[1] - 0.2, { fs: 18, w: 0.4, align: "right" });
  lbl(s, "B", B[0] - 0.38, B[1] + 0.08, { fs: 18, w: 0.4, align: "right" });
  lbl(s, "C", Cp[0] + 0.08, Cp[1] + 0.16, { fs: 18, w: 0.4 });
  lbl(s, "D", D[0] + 0.1, D[1] - 0.16, { fs: 18, w: 0.4 });
  lbl(s, "∠A ＋ ∠C ＝ 180°", cx - 1.6, cy + R + 0.3, { fs: 16, color: C.sageDeep, w: 3.2, align: "center" });
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
  s.addText("先伸展 30 秒，再開始 🙂", { x: 3.4, y: 4.4, w: 6.5, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 20, italic: false, color: C.soft });
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
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.4, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.4, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("圓的有關性質", { x: 0.85, y: 2.3, w: 11.6, h: 1.1, fontFace: F, fontSize: 52, bold: true, color: C.white, align: "left" });
  s.addText("四課時通關", { x: 0.85, y: 3.4, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "① 圓的詞", options: { fontFace: F, fontSize: 20, color: "E7F0EB" } },
    { text: "  →  ", options: { fontFace: F, fontSize: 20, color: C.sage } },
    { text: "② 垂徑定理", options: { fontFace: F, fontSize: 20, color: "E7F0EB" } },
    { text: "  →  ", options: { fontFace: F, fontSize: 20, color: C.sage } },
    { text: "③ 圓周角", options: { fontFace: F, fontSize: 20, color: "E7F0EB" } },
    { text: "  →  ", options: { fontFace: F, fontSize: 20, color: C.sage } },
    { text: "④ 圓內接四邊形", options: { fontFace: F, fontSize: 20, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.65, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著四課時一步一步走", { x: 0.9, y: 5.45, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：這個單元分四節課走完，不趕進度。每一節都是：學一招 → 看老師示範 → 自己挑星星練習。做得起就往上跳一層。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "這個單元，我們走四節課");
  const rows = [
    ["課時①", "圓的基本詞", "圓心、半徑、弦、直徑、弧、圓心角、圓周角"],
    ["課時②", "垂徑定理", "垂直弦的直徑會平分弦：半徑、半弦、距離組成直角三角形"],
    ["課時③", "圓周角定理", "圓周角＝圓心角的一半；直徑所對的圓周角是 90°"],
    ["課時④", "圓內接四邊形", "四點都在圓上時，對角相加是 180°"],
  ];
  let y = 1.82;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.08);
    badge(s, r[0], 0.95, y + 0.24, 1.9, 0.6, 20);
    s.addText(r[1], { x: 3.05, y: y + 0.08, w: 3.5, h: 0.48, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(r[2], { x: 3.05, y: y + 0.56, w: 9.2, h: 0.44, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.2;
  });
  s.addText("每一節都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 6.55, w: 11.9, h: 0.42, fontFace: F, fontSize: 19, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖：四節課的結構一致，減少焦慮。每節課開始都回到這一頁指一次「今日在這裡」。");
})();

// =====================================================================
// 課時① 圓的基本詞
// =====================================================================
lessonDivider("課時①", "圓的基本詞", "看圖說得出圓心、半徑、弦、直徑、弧")
  .addNotes("進入課時①。這一節只做「認詞、指圖」，不做計算，建立信心。");

// 引入（低門檻保底）
(function () {
  const s = newSlide(false);
  title(s, "生活裡的圓，圓心在哪？", "課時① · 引入");
  const data = [
    ["單車輪", "圓心＝車軸", true],
    ["披薩切一刀", "切出來的直線段＝弦", true],
    ["時鐘錶面", "圓心＝指針的固定點", true],
    ["長方形窗框", "不是圓，沒有圓心", false],
  ];
  let y = 2.05;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.0, d[2] ? C.block : C.white);
    s.addText(d[0], { x: 1.2, y: y, w: 5.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(d[2] ? "有圓 ✔" : "不是 ✗", { x: 6.3, y: y, w: 2.0, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: d[2] ? C.sageDeep : C.soft });
    s.addText(d[1], { x: 8.4, y: y, w: 4.0, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.13;
  });
  footer(s, N, false);
  s.addNotes("保底暖身：只做判斷，人人答得出。口頭補充：圓上每一點到圓心的距離都一樣，這個距離就是半徑。");
})();

// 概念頁（圖像先行）
(function () {
  const s = newSlide(false);
  title(s, "一張圖，五個詞", "課時① · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figCircleBasic(s, 3.85, 4.0, 1.85);
  const items = [
    ["半徑", "圓心到圓上任一點"],
    ["弦", "連接圓上兩點的線段"],
    ["直徑", "過圓心的弦（最長）"],
    ["弧", "圓上兩點之間的一段圓周"],
    ["圓心角", "頂點在圓心的角"],
  ];
  let y = 1.85;
  items.forEach((it) => {
    hlBox(s, 7.3, y, 2.1, 0.66);
    s.addText(it[0], { x: 7.3, y: y, w: 2.1, h: 0.66, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 9.6, y: y, w: 3.4, h: 0.66, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
    y += 0.9;
  });
  footer(s, N, false);
  s.addNotes("圖像先行：先指圖上的線，再唸詞。請學生輪流上前指出「哪一條是弦、哪一條是直徑」。頂點在圓上的角叫圓周角，下一節會用到。");
})();

// 迷思澄清頁
(function () {
  const s = newSlide(false);
  title(s, "半徑是不是弦？", "課時① · 迷思澄清");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.75, w: 11.7, h: 1.45, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "小明說：「圓中最長的弦是半徑。」  ", options: { fontFace: F, fontSize: 22, color: C.ink } },
    { text: "✗ 不對", options: { fontFace: F, fontSize: 23, bold: true, color: C.soft } },
  ], { x: 1.1, y: 1.85, w: 11.1, h: 0.6, align: "left", valign: "middle" });
  s.addText("弦要連接圓上「兩點」；半徑一端在圓心，所以半徑不是弦。", { x: 1.1, y: 2.5, w: 11.1, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  const rows = [
    ["半徑", "圓心 → 圓上一點", "不是弦"],
    ["弦", "圓上一點 → 圓上另一點", "是弦"],
    ["直徑", "圓上一點 → 過圓心 → 圓上一點", "是弦，而且最長"],
  ];
  let y = 3.5;
  rows.forEach((r) => {
    card(s, 0.8, y, 11.7, 0.86, C.white);
    s.addText(r[0], { x: 1.1, y: y, w: 2.0, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 3.2, y: y, w: 5.6, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    s.addText(r[2], { x: 8.9, y: y, w: 3.4, h: 0.86, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.slate });
    y += 0.98;
  });
  s.addText("記住：直徑 ＝ 2 × 半徑，也是最長的弦。", { x: 0.8, y: 6.5, w: 11.7, h: 0.42, fontFace: F, fontSize: 20, bold: true, color: C.ink, align: "left" });
  footer(s, N, false);
  s.addNotes("用灰色標「不是」，不用紅色（色盲友善）。關鍵判準只有一句：兩端是不是都在圓上。");
})();

breakSlide("下一頁換你做：先在圖上指出來");

tieredTasks("課時① · 分層練習",
  [
    ["1. 在圖上指出：圓心、\n   一條半徑、一條弦、\n   一條直徑", "2. 填空：直徑 ＝ ＿ × 半徑。\n   ⊙O 半徑 6，直徑 ＝ ＿"],
    ["3. ⊙O 半徑 6，圓中最長的\n   弦有多長？它叫什麼？", "4. 判斷並說理由：\n   （1）直徑是弦嗎？\n   （2）半徑是弦嗎？"],
    ["5. 找錯：小明說「圓中最長\n   的弦是半徑」。對嗎？\n   請說明理由", "6. 自己畫一個圓，標出\n   圓心、弦、直徑、弧，\n   說明弦與直徑的關係"],
  ],
  "解答核對｜A1: 指圖即可（圓心 O、半徑 OA、弦 BC、直徑 FG）；A2: 直徑＝2×半徑，半徑 6 → 直徑 12。 B3: 最長的弦＝直徑＝2×6＝12；B4:(1) 直徑是弦（兩端都在圓上，且過圓心）(2) 半徑不是弦（一端在圓心，不在圓上）。 C5: 不對，最長的弦是直徑（＝2×半徑），半徑本身不是弦；C6: 開放，只看是否標對四個元素、並說出「直徑是最長的弦、等於 2 個半徑」。"
);

summarySlide("課時① · 總結",
  "圓上每一點到圓心都一樣遠，那個距離就是半徑。",
  "弦＝連接圓上兩點；直徑＝過圓心的弦＝2×半徑，是最長的弦。")
  .addNotes("回收課時①。保底句要全班能覆述：直徑是最長的弦，等於兩個半徑。");

// =====================================================================
// 課時② 垂徑定理
// =====================================================================
lessonDivider("課時②", "垂徑定理", "會用半徑、半弦、圓心到弦的距離組直角三角形")
  .addNotes("進入課時②。這一節第一次出現計算，重點是「看出直角三角形」而不是背公式。");

// 引入
(function () {
  const s = newSlide(false);
  title(s, "弦離圓心有多遠？", "課時② · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.4, y: 2.15, w: 10.5, h: 1.35, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("把一條弦對摺，摺痕會通過圓心 —— 而且剛好把弦分成兩半", { x: 1.75, y: 2.15, w: 9.8, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
  card(s, 1.4, 3.85, 10.5, 2.4, C.white);
  s.addText("動手 30 秒", { x: 1.75, y: 4.0, w: 4.0, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText("① 在紙上畫一個圓，剪下來\n② 隨便畫一條弦，沿弦的中點對摺\n③ 看看摺痕有沒有經過圓心", {
    x: 1.75, y: 4.5, w: 9.8, h: 1.6, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.35 });
  footer(s, N, false);
  s.addNotes("CRA 具體階：讓學生真的摺一次。摺痕＝垂直於弦的直徑。這個動作是整節課的錨點，之後畫圖時叫學生「想返摺紙」。");
})();

// CRA 三階頁
(function () {
  const s = newSlide(false);
  title(s, "垂徑定理：摺 → 圖 → 式", "課時② · CRA");
  s.addText("以「半徑 5、弦 AB＝8」為例", { x: 0.8, y: 1.62, w: 11.7, h: 0.45, fontFace: F, fontSize: 22, bold: true, color: C.ink, align: "left" });
  const cols = [
    ["具體", "把圓摺一摺，\n摺痕通過圓心，\n弦被分成一樣長\n的兩段", "摺痕 ⊥ 弦"],
    ["表徵", "畫出半徑 r、\n半弦、圓心到弦\n的距離 d，\n合成一個直角三角形", "三兄弟：r、半弦、d"],
    ["抽象", "用勾股定理：\n\nd² ＋ 半弦² ＝ r²", "d ＝ √(25 − 16) ＝ 3"],
  ];
  const x0 = 0.8, gap = 0.3, w = (11.7 - 2 * gap) / 3, yTop = 2.2, h = 3.95;
  cols.forEach((c, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 0.7, rectRadius: 0.12, fill: { color: C.sage }, line: { type: "none" } });
    s.addText(c[0], { x, y: yTop, w, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
    s.addText(c[1], { x: x + 0.2, y: yTop + 0.9, w: w - 0.4, h: 2.1, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
    hlBox(s, x + 0.2, yTop + 3.15, w - 0.4, 0.62);
    s.addText(c[2], { x: x + 0.2, y: yTop + 3.15, w: w - 0.4, h: 0.62, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.sageDeep });
    if (i < 2) s.addText("→", { x: x + w - 0.02, y: yTop + 1.4, w: gap + 0.04, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.sageDeep });
  });
  footer(s, N, false);
  s.addNotes("三階都要走「示範 → 引導 → 學生做」。抽象階仍保留「三兄弟」這個表徵詞，不完全抽走視覺線索。");
})();

// 概念頁 + 圖
(function () {
  const s = newSlide(false);
  title(s, "直角三角形三兄弟", "課時② · 性質");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figChordPerp(s, 3.85, 4.05, 1.85);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.8, w: 5.3, h: 1.25, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("垂直於弦的直徑，\n會平分這條弦", { x: 7.6, y: 1.8, w: 4.8, h: 1.25, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white, lineSpacingMultiple: 1.2 });
  const items = [
    ["r", "半徑（斜邊，最長）"],
    ["半弦", "弦的一半 ＝ AM ＝ MB"],
    ["d", "圓心到弦的距離"],
  ];
  let y = 3.35;
  items.forEach((it, i) => {
    stepCircle(s, 7.3, y, i + 1, 0.5);
    hlBox(s, 8.0, y, 1.35, 0.5);
    s.addText(it[0], { x: 8.0, y: y, w: 1.35, h: 0.5, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: 9.55, y: y, w: 3.2, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 19, color: C.ink });
    y += 0.78;
  });
  hlBox(s, 7.3, 5.72, 5.3, 0.62);
  s.addText("d² ＋ 半弦² ＝ r²", { x: 7.3, y: 5.72, w: 5.3, h: 0.62, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("圖像先行：先在圖上用手指描出直角三角形 OMA，再講式。強調 M 是弦的中點，這是垂徑定理給我們的禮物。");
})();

// 步驟卡範例
stepCardSlide("課時② · 範例（步驟卡）", "⊙O 半徑 5，弦 AB＝8，求圓心到 AB 的距離 d",
  "已知：r＝5、AB＝8。求：d（圓心 O 到弦 AB 的距離）。", [
  "畫圖：從 O 畫一條垂線到 AB，交點叫 M",
  "用垂徑定理：M 是中點 → 半弦 ＝ 8 ÷ 2 ＝ 4",
  "看出直角三角形 OMA：斜邊 r＝5、一股 4、另一股 d",
  "勾股定理：d² ＝ 5² − 4² ＝ 25 − 16 ＝ 9",
  "開方：d ＝ 3。檢查單位與合理性（d 應小於 r ✔）",
], "六步提示卡：讀題 → 畫圖 → 找中點 → 認直角三角形 → 算 → 檢查。提醒 d 一定比 r 小，這是自我檢查的方法。");

breakSlide("下一頁換你做：先畫圖，再算");

tieredTasks("課時② · 分層練習",
  [
    ["1. 直徑 CD ⊥ 弦 AB 於 M。\n   若 AB＝12，\n   則 AM＝＿，MB＝＿", "2. 半徑＝10，OM＝6，\n   求半弦＝＿，AB＝＿"],
    ["3. ⊙O 半徑 5，弦 AB＝8。\n   求圓心 O 到弦 AB\n   的距離", "4. 半徑 13、弦 AB＝24，\n   求圓心到 AB 的距離"],
    ["5. ⊙O 半徑 13，兩條平行弦\n   AB＝24、CD＝10。\n   求兩弦的距離\n   （分同側、異側）", "6. 為什麼圓心到弦的距離\n   一定比半徑短？\n   用三兄弟的圖說明"],
  ],
  "解答核對｜A1: 垂徑定理，M 是中點 → AM＝MB＝6；A2: 半弦＝√(100−36)＝8，AB＝2×8＝16。 B3: 半弦＝4，d＝√(25−16)＝3；B4: 半弦＝12，d＝√(169−144)＝5。 C5: AB 到圓心 √(169−144)＝5，CD 到圓心 √(169−25)＝12；同側 12−5＝7，異側 12+5＝17，答 7 或 17；C6: 開放，須說出 d 是直角三角形的股、r 是斜邊，斜邊最長所以 d＜r。"
);

summarySlide("課時② · 總結",
  "垂直弦的直徑會平分弦，於是出現一個直角三角形。",
  "半徑、半弦、圓心到弦的距離：d² ＋ 半弦² ＝ r²。")
  .addNotes("回收課時②。保底：能把弦除以 2、能寫出勾股關係就達標。");

// =====================================================================
// 課時③ 圓周角定理
// =====================================================================
lessonDivider("課時③", "圓周角定理", "會用「圓周角＝圓心角的一半」求角度")
  .addNotes("進入課時③。這是全單元抽象度最高的一節，先花時間在「認角」，再講倍半關係。");

// 引入：認角
(function () {
  const s = newSlide(false);
  title(s, "同一條弧，兩種角", "課時③ · 引入");
  const rows = [
    ["圓心角", "頂點在 圓心", "∠AOB"],
    ["圓周角", "頂點在 圓上", "∠ACB"],
  ];
  let y = 2.0;
  rows.forEach((r) => {
    card(s, 0.8, y, 11.7, 1.35, C.white);
    hlBox(s, 1.1, y + 0.32, 2.4, 0.7);
    s.addText(r[0], { x: 1.1, y: y + 0.32, w: 2.4, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 3.9, y: y, w: 5.2, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 23, color: C.ink });
    s.addText(r[2], { x: 9.3, y: y, w: 3.0, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 25, bold: true, color: C.slate });
    y += 1.55;
  });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 5.15, w: 11.7, h: 1.2, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText("判斷方法只有一句：看角的頂點在哪裡。", { x: 1.1, y: 5.15, w: 11.1, h: 1.2, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("先只做「認角」，不做計算。請學生在圖上用手指點出頂點，再說是哪一種角。認錯角是本節最常見的錯。");
})();

// 概念頁 + 圖
(function () {
  const s = newSlide(false);
  title(s, "圓周角 ＝ 圓心角的一半", "課時③ · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figInscribed(s, 3.85, 4.05, 1.8);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.85, w: 5.3, h: 1.5, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("同一條弧 AB 所對的：\n∠AOB ＝ 2 × ∠ACB", { x: 7.6, y: 1.85, w: 4.8, h: 1.5, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.white, lineSpacingMultiple: 1.2 });
  card(s, 7.3, 3.6, 5.3, 1.25, C.white);
  s.addText("圓心角 ＝ 圓周角 × 2", { x: 7.55, y: 3.6, w: 4.8, h: 1.25, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  card(s, 7.3, 5.05, 5.3, 1.25, C.white);
  s.addText("圓周角 ＝ 圓心角 ÷ 2", { x: 7.55, y: 5.05, w: 4.8, h: 1.25, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("保底：全班要能講出「在圓心的那個角比較大，是兩倍」。用手勢示範：圓心角張得大，圓周角張得小一半。兩個方向的式都寫出來，避免學生只會單向。");
})();

// 分類頁：三個推論
(function () {
  const s = newSlide(false);
  title(s, "三個很好用的推論", "課時③ · 推論");
  const rows = [
    ["①", "同弧所對的圓周角相等", "同一條弧上的圓周角，不管頂點移到哪，都一樣大"],
    ["②", "直徑所對的圓周角是 90°", "只要看到直徑，馬上想到直角"],
    ["③", "90° 的圓周角所對的弦是直徑", "反過來也成立"],
  ];
  let y = 1.88;
  rows.forEach((r) => {
    card(s, 0.75, y, 11.85, 1.32, C.white);
    s.addText(r[0], { x: 1.0, y: y, w: 0.8, h: 1.32, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 1.95, y: y + 0.12, w: 10.4, h: 0.58, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(r[2], { x: 1.95, y: y + 0.7, w: 10.4, h: 0.48, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.48;
  });
  hlBox(s, 0.75, 6.32, 11.85, 0.55);
  s.addText("最常考的是 ②：看到直徑，先寫下 90°。", { x: 0.75, y: 6.32, w: 11.85, h: 0.55, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("三個推論一次列出，但只要求記住 ②。①③ 讓學生知道存在即可，做題時再回來查。");
})();

// 步驟卡範例
stepCardSlide("課時③ · 範例（步驟卡）", "圓心角 ∠AOB＝100°，求同弧的圓周角 ∠ACB",
  "已知：∠AOB＝100°（頂點在圓心）。求：∠ACB（頂點在圓上）。", [
  "看頂點：O 在圓心 → ∠AOB 是圓心角",
  "看頂點：C 在圓上 → ∠ACB 是圓周角",
  "確認兩個角對著同一條弧 AB",
  "圓周角 ＝ 圓心角 ÷ 2 ＝ 100° ÷ 2",
  "答：∠ACB ＝ 50°。檢查：圓周角比圓心角小 ✔",
], "每一步都先問「頂點在哪」。自我檢查法：圓周角一定比圓心角小，如果算出來比較大，一定做反了。");

// 範例頁：直徑對直角（原題 B5）
(function () {
  const s = newSlide(false);
  title(s, "看到直徑，先寫 90°", "課時③ · 範例（推論②）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figDiameterRight(s, 3.85, 3.95, 1.75);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.8, w: 5.3, h: 1.15, rectRadius: 0.12, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText("AB 是直徑，C 在圓上，\n∠A＝30°。求 ∠ACB、∠ABC。", { x: 7.55, y: 1.8, w: 4.8, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink, lineSpacingMultiple: 1.15 });
  const steps = [
    "AB 是直徑 → ∠ACB ＝ 90°",
    "三角形內角和 ＝ 180°",
    "∠ABC ＝ 180° − 90° − 30° ＝ 60°",
  ];
  let y = 3.2;
  steps.forEach((st, i) => {
    stepCircle(s, 7.3, y + 0.16, i + 1, 0.5);
    s.addText(st, { x: 8.0, y: y, w: 4.6, h: 0.82, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 1.0;
  });
  footer(s, N, false);
  s.addNotes("這題把「圓的推論」和「三角形內角和」接起來。提醒：先寫 90°，題目就變回熟悉的三角形題。");
})();

breakSlide("下一頁換你做：先寫「頂點在哪」");

tieredTasks("課時③ · 分層練習",
  [
    ["1. 圓心角 ∠AOB＝80°，\n   同弧圓周角 ∠ACB＝＿", "2. 圓周角 ∠ACB＝35°，\n   同弧圓心角 ∠AOB＝＿。\n   直徑所對的圓周角＝＿"],
    ["3. AB 是 ⊙O 的直徑，C 在\n   圓上，∠A＝30°。\n   求 ∠ACB 和 ∠ABC", "4. 同弧的圓心角比圓周角\n   大 45°，求這兩個角"],
    ["5. AB 是直徑，C 在圓上移動\n   （不與 A、B 重合）。\n   ∠ACB 會不會變？為什麼？", "6. 出一題「用圓周角定理」\n   的題目給同學做，\n   並附上你的答案"],
  ],
  "解答核對｜A1: 80÷2＝40°；A2: 35×2＝70°，直徑所對的圓周角＝90°。 B3: AB 是直徑 → ∠ACB＝90°，∠ABC＝180−90−30＝60°；B4: 設圓周角 x，圓心角 2x，2x−x＝45 → x＝45，圓周角 45°、圓心角 90°。 C5: 不會變，永遠 90°（直徑所對的圓周角是直角），與 C 的位置無關；C6: 開放，評分看題目是否用得上倍半關係、答案是否自洽。"
);

summarySlide("課時③ · 總結",
  "同一條弧上，圓心角是圓周角的兩倍。",
  "看到直徑，就寫 ∠＝90°；圓周角 ＝ 圓心角 ÷ 2。")
  .addNotes("回收課時③。保底：能講出「圓周角細一半」＋「直徑對直角」就達標。");

// =====================================================================
// 課時④ 圓內接四邊形
// =====================================================================
lessonDivider("課時④", "圓內接四邊形", "會用對角互補求角，並把四節課接起來")
  .addNotes("進入課時④。內容最短，留時間做整個單元的綜合練習。");

// 概念頁 + 圖
(function () {
  const s = newSlide(false);
  title(s, "四點都在圓上：對角互補", "課時④ · 概念（保底）");
  card(s, 0.7, 1.72, 6.3, 4.6, C.white);
  figCyclicQuad(s, 3.85, 3.95, 1.8);
  s.addShape(p.ShapeType.roundRect, { x: 7.3, y: 1.85, w: 5.3, h: 1.4, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("四個頂點都在圓上 →\n對角相加是 180°", { x: 7.6, y: 1.85, w: 4.8, h: 1.4, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.white, lineSpacingMultiple: 1.2 });
  card(s, 7.3, 3.5, 5.3, 1.3, C.white);
  s.addText("∠A ＋ ∠C ＝ 180°", { x: 7.55, y: 3.5, w: 4.8, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
  card(s, 7.3, 5.0, 5.3, 1.3, C.white);
  s.addText("∠B ＋ ∠D ＝ 180°", { x: 7.55, y: 5.0, w: 4.8, h: 1.3, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("「對角」＝隔一個的角，不是相鄰的角。請學生先在圖上用手指連 A→C、B→D，確認配對，再算。這是本節最常見的錯。");
})();

// 步驟卡範例
stepCardSlide("課時④ · 範例（步驟卡）", "圓內接四邊形 ABCD，∠A＝95°、∠B＝70°，求 ∠C、∠D",
  "已知：∠A＝95°、∠B＝70°，四點都在圓上。求：∠C、∠D。", [
  "配對：A 的對角是 C，B 的對角是 D",
  "∠A ＋ ∠C ＝ 180° → ∠C ＝ 180° − 95° ＝ 85°",
  "∠B ＋ ∠D ＝ 180° → ∠D ＝ 180° − 70° ＝ 110°",
  "檢查：95 + 70 + 85 + 110 ＝ 360° ✔（四邊形內角和）",
], "第 1 步「先配對」是防錯關鍵。第 4 步的檢查法要教：四個角加起來一定是 360°，加不到就一定有錯。");

breakSlide("下一頁是最後一關：四節課一起用");

tieredTasks("課時④ · 分層練習",
  [
    ["1. 圓內接四邊形 ABCD，\n   ∠A＝80°，則 ∠C＝＿", "2. 圓內接四邊形 ABCD，\n   ∠B＝110°，則 ∠D＝＿"],
    ["3. 圓內接四邊形 ABCD，\n   ∠A＝95°、∠B＝70°，\n   求 ∠C、∠D", "4. 圓內接四邊形 ABCD，\n   ∠A : ∠C ＝ 2 : 3，\n   求 ∠A 和 ∠C"],
    ["5. ⊙O 半徑 13，兩條平行弦\n   AB＝24、CD＝10，\n   求兩弦的距離\n   （兩種情況）", "6. 出一題同時用到垂徑定理\n   和圓周角的題目，\n   並寫出你的解法"],
  ],
  "解答核對｜A1: 180−80＝100°；A2: 180−110＝70°。 B3: ∠C＝180−95＝85°、∠D＝180−70＝110°（檢查 95+70+85+110＝360 ✔）；B4: ∠A+∠C＝180，按 2:3 分 → ∠A＝180×2/5＝72°、∠C＝180×3/5＝108°。 C5: AB 到圓心 √(169−144)＝5、CD 到圓心 √(169−25)＝12；同側 12−5＝7、異側 12+5＝17，答 7 或 17；C6: 開放，評分看是否真的兩個定理都用上、解法是否自洽。"
);

// =====================================================================
// 收尾
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "四節課，四句話");
  const data = [
    ["課時①", "直徑是最長的弦，等於 2 個半徑。"],
    ["課時②", "垂直弦的直徑會平分弦：d² ＋ 半弦² ＝ r²。"],
    ["課時③", "圓周角 ＝ 圓心角 ÷ 2；直徑所對的圓周角是 90°。"],
    ["課時④", "圓內接四邊形，對角相加是 180°。"],
  ];
  let y = 1.85;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.05, C.white);
    badge(s, d[0], 0.95, y + 0.23, 1.9, 0.6, 20);
    s.addText(d[1], { x: 3.05, y: y, w: 9.3, h: 1.05, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
    y += 1.17;
  });
  hlBox(s, 0.7, 6.46, 11.9, 0.5);
  s.addText("四節課其實只做一件事：把圓上的線和角，換成會算的直角三角形和度數。", {
    x: 0.7, y: 6.46, w: 11.9, h: 0.5, align: "center", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("整體回收。可請學生每節課講一句自己的話覆述。連結下一單元：09 會再用一次「d 與 r 比大小」的想法。");
})();

(function () {
  const s = newSlide(true);
  s.addText("你已經走完四節課！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("圓的性質，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次看到「直徑」，記得先寫下 90°。", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: "9FB8AE" });
  s.addNotes("正向收束，asset-based。肯定策略與過程，不用「終於」「總算」等字眼。");
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
    "節奏：4 課時 × 45 分鐘，",
    "每課時各含 1 個轉換點。",
  ];
  const right = [
    "◆ CRA 三階：摺紙 → 圖 → 勾股式",
    "◆ 原生幾何圖：基本詞／垂徑／圓周角／",
    "   直徑對直角／圓內接四邊形",
    "◆ 步驟卡：一步一行、編號、附自我檢查",
    "◆ 轉換點＋預告：照顧注意力節奏",
    "◆ 迷思澄清：半徑不是弦、對角要先配對",
    "◆ 保底成功句＋asset-based 用語",
  ];
  card(s, 0.7, 1.9, 5.85, 4.4, C.white);
  s.addText("調整定位", { x: 0.95, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(left.join("\n"), { x: 0.95, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.28 });
  card(s, 6.75, 1.9, 5.85, 4.4, C.white);
  s.addText("融合層做了什麼", { x: 7.0, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(right.join("\n"), { x: 7.0, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
  footer(s, N, false);
  s.addNotes("此頁供教師／IEP 對接用，上課可略過。屬 Accommodation，未剪裁課程內容。");
})();

// ---- 輸出 ----
p.writeFile({ fileName: "簡報_圓的有關性質_融合抽離版.pptx" }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
