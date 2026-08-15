// 融合抽離小組 SOIL 教學簡報：二次函數（圖像與性質 → 方程與應用）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。
// 拋物線圖以 assets/ 內 PNG 內嵌（gen_graphs.js 產生，已逐張目視確認）。
const pptxgen = require("pptxgenjs");
const path = require("path");
const A = (f) => path.join(__dirname, "assets", f); // 圖片絕對路徑
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "二次函數 兩站通關（融合抽離版）";

// ---- 配色 (Sage Calm 低刺激) ----
const C = {
  bgLight: "EDF3F0", bgDark: "2E4A43", ink: "233A34", soft: "5C6F68",
  sage: "6FA48C", sageDeep: "4E8770", slate: "50808E", block: "DCEAE3",
  block2: "CFE0D8", cardLine: "B9CFC5", white: "FFFFFF", starInk: "2E4A43",
};
const F = "Microsoft JhengHei";
const MONO = "Consolas";

// ---- 共用小工具（沿用 01-03 骨架）----
function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("初三數學 · 二次函數（抽離小組·融合版）", {
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
let N = 0;
function newSlide(dark) { const s = p.addSlide(); bg(s, dark); N += 1; return s; }

// 站牌 / 過渡頁 産生器（dark）
function stationDivider(badge, name, goal) {
  const s = newSlide(true);
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 2.15, w: 2.4, h: 1.0, rectRadius: 0.5, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(badge, { x: 0.9, y: 2.15, w: 2.4, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.white });
  s.addText(name, { x: 3.6, y: 2.15, w: 9.4, h: 1.0, align: "left", valign: "middle", fontFace: F, fontSize: 36, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.95, y: 3.7, w: 11.4, h: 1.15, rectRadius: 0.12, fill: { color: "35564E" }, line: { type: "none" } });
  s.addText([
    { text: "目標：", options: { fontFace: F, fontSize: 24, bold: true, color: C.sage } },
    { text: goal, options: { fontFace: F, fontSize: 24, color: "E7F0EB" } },
  ], { x: 1.25, y: 3.7, w: 10.9, h: 1.15, align: "left", valign: "middle" });
  footer(s, N, true);
  return s;
}
// 轉換點預告頁
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
// 分層任務頁 産生器（三欄同版面）
function tieredTasks(kicker, cols, noteKey) {
  const s = newSlide(false);
  title(s, "挑戰練習 · 自選星星", kicker);
  const tiers = [
    { t: "練習 A", star: "★☆☆" }, { t: "練習 B", star: "★★☆" }, { t: "練習 C", star: "★★★" },
  ];
  const x0 = 0.65, gap = 0.28, w = (12.7 - 2 * gap) / 3, yTop = 1.95, h = 4.35;
  tiers.forEach((ti, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x: x, y: yTop, w: w, h: 0.9, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(ti.t, { x: x + 0.2, y: yTop + 0.06, w: w - 0.4, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(ti.star, { x: x + 0.2, y: yTop + 0.46, w: w - 0.4, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.starInk });
    const items = cols[i];
    let ty = yTop + 1.08;
    items.forEach((it) => {
      s.addText(it, { x: x + 0.24, y: ty, w: w - 0.46, h: 1.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.22 });
      ty += 1.6;
    });
  });
  s.addText("做得起 A，就往 B、C 跳一層 ↗   全部同一個概念，只是鷹架不同", { x: 0.65, y: 6.5, w: 12.7, h: 0.45, fontFace: F, fontSize: 17, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(noteKey);
  return s;
}
// 總結頁 産生器（帶走一句話 + 保底版）
function summarySlide(kicker, takeaway, floor) {
  const s = newSlide(false);
  title(s, "帶走一句話", kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 2.15, w: 11.7, h: 1.7, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText(takeaway, { x: 1.2, y: 2.15, w: 10.9, h: 1.7, align: "left", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 4.15, w: 11.7, h: 1.55, rectRadius: 0.15, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "至少要記得：", options: { fontFace: F, fontSize: 22, bold: true, color: C.sageDeep } },
    { text: floor, options: { fontFace: F, fontSize: 23, color: C.ink } },
  ], { x: 1.2, y: 4.15, w: 10.9, h: 1.55, align: "left", valign: "middle" });
  footer(s, N, false);
  return s;
}
// 步驟卡頁 産生器
function stepCardSlide(kicker, head, eqn, steps, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.75, w: 11.7, h: 0.9, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText(eqn, { x: 1.1, y: 1.75, w: 11.1, h: 0.9, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });
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
// 圖像頁（表徵）産生器：左圖 + 右側說明卡
function graphSlide(kicker, head, img, imgRatio, notesList, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  // 左：拋物線圖（白卡承載）
  const iw = 5.5, ih = iw / imgRatio;
  const iy = 2.05;
  card(s, 0.7, iy, iw + 0.3, ih + 0.3, C.white);
  s.addImage({ path: img, x: 0.85, y: iy + 0.15, w: iw, h: ih });
  // 右：讀圖重點
  const rx = 7.25, rw = 5.4;
  card(s, rx, iy, rw, ih + 0.3, C.block);
  let ty = iy + 0.28;
  notesList.forEach((ln) => {
    s.addText(ln, { x: rx + 0.28, y: ty, w: rw - 0.56, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.1 });
    ty += 0.82;
  });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}
// 四格視覺鷹架頁 産生器
function scaffoldSlide(kicker, head, cells, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  const x0 = 0.9, y0 = 2.05, w = 5.6, h = 2.1, gx = 0.4, gy = 0.35;
  cells.forEach((c, i) => {
    const x = x0 + (i % 2) * (w + gx);
    const y = y0 + Math.floor(i / 2) * (h + gy);
    card(s, x, y, w, h, C.white);
    s.addText(c[0], { x: x + 0.25, y: y + 0.18, w: w - 0.5, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    s.addText(c[1], { x: x + 0.25, y: y + 0.78, w: w - 0.5, h: 1.15, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.25 });
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
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.5, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.5, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("二次函數", { x: 0.85, y: 2.45, w: 11.6, h: 1.1, fontFace: F, fontSize: 54, bold: true, color: C.white, align: "left" });
  s.addText("兩站通關", { x: 0.85, y: 3.5, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "站① 圖像與性質", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "     →     ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "站② 方程與應用", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.75, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著兩站一步一步走", { x: 0.9, y: 5.5, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, italic: true, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：今天不趕進度，跟著兩站走。站①看懂拋物線的樣子，站②把它用在方程和最值問題。每一站都是：學一招 → 看老師示範 → 自己挑星星練習。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "今日課堂流程");
  const rows = [
    ["站①", "圖像與性質", "認識拋物線 → 開口、頂點、對稱軸、配方"],
    ["站②", "方程與應用", "交點就是方程的根 → 用頂點求最大最小值"],
  ];
  let y = 2.15;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.5, C.white);
    stationBadge(s, r[0], 0.95, y + 0.44);
    s.addText(r[1], { x: 2.85, y: y + 0.2, w: 9.4, h: 0.6, fontFace: F, fontSize: 27, bold: true, color: C.ink, align: "left", valign: "middle" });
    s.addText(r[2], { x: 2.85, y: y + 0.82, w: 9.4, h: 0.5, fontFace: F, fontSize: 20, color: C.soft, align: "left", valign: "middle" });
    y += 1.75;
  });
  s.addText("每一站都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 6.4, w: 11.9, h: 0.45, fontFace: F, fontSize: 18, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖：讓學生知道整節課的結構，減少焦慮。兩站節奏一致，做完一站休息一下。");
})();

// =====================================================================
// 站① 二次函數的圖像與性質
// =====================================================================
stationDivider("站①", "二次函數的圖像與性質", "看得懂拋物線——開口、頂點、對稱軸").addNotes("進入站①。這一站的主角是「圖」：先讓學生對拋物線的樣子有畫面，再談性質。");

// S4 問題引入：哪一條是二次函數
(function () {
  const s = newSlide(false);
  title(s, "哪一條是「二次函數」？", "站① · 引入");
  const data = [
    ["y = x² − 4x + 3", "是 ✔", "最高次是 2", true],
    ["y = 2x²", "是 ✔", "只有 x² 項也算", true],
    ["y = 3x + 1", "✗ 不是", "最高次只有 1", false],
  ];
  let y = 2.1;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.15, d[3] ? C.block : C.white);
    s.addText(d[0], { x: 1.1, y: y, w: 5.2, h: 1.15, align: "left", valign: "middle", fontFace: MONO, fontSize: 26, bold: true, color: C.ink });
    s.addText(d[1], { x: 6.4, y: y, w: 1.9, h: 1.15, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: d[3] ? C.sageDeep : C.soft });
    s.addText(d[2], { x: 8.4, y: y, w: 4.0, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.33;
  });
  footer(s, N, false);
  s.addNotes("低門檻暖身：只判斷「是不是」，人人答得出。口頭補充：二次＝最高次方是 2；它的圖像一定是拋物線。");
})();

// S5 概念 + 保底：一般式，圖像是拋物線
(function () {
  const s = newSlide(false);
  title(s, "一般式：看到 x²，就是拋物線", "站① · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.85, w: 11.7, h: 1.15, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText([
    { text: "y = a x² + b x + c", options: { fontFace: MONO, fontSize: 30, bold: true, color: C.white } },
    { text: "     （ a ≠ 0 ）", options: { fontFace: F, fontSize: 24, color: "CFE0D8" } },
  ], { x: 1.1, y: 1.85, w: 11.1, h: 1.15, align: "left", valign: "middle" });
  const steps = [
    ["1", "最高次方是 2（有 x² 項）"],
    ["2", "a 是 x² 前的數，a 不能是 0"],
    ["3", "它的圖像是一條「拋物線」"],
  ];
  let y = 3.25;
  steps.forEach((st) => {
    stepCircle(s, 0.9, y, st[0], 0.5);
    s.addText(st[1], { x: 1.6, y: y - 0.06, w: 6.6, h: 0.62, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    y += 0.78;
  });
  card(s, 8.5, 3.2, 4.0, 2.35, C.block);
  s.addText("例", { x: 8.7, y: 3.32, w: 3.6, h: 0.4, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  s.addText("y = x² − 4x + 3", { x: 8.7, y: 3.75, w: 3.6, h: 0.5, fontFace: MONO, fontSize: 22, bold: true, color: C.ink, align: "left" });
  s.addText("a = 1　b = −4　c = 3", { x: 8.7, y: 4.35, w: 3.6, h: 0.5, fontFace: F, fontSize: 21, color: C.ink, align: "left" });
  s.addText("認得 a、b、c，你就開始了 👍", { x: 8.7, y: 4.95, w: 3.6, h: 0.5, fontFace: F, fontSize: 18, italic: true, color: C.soft, align: "left" });
  footer(s, N, false);
  s.addNotes("保底成功經驗：全班都要能認出這是二次函數、圖像是拋物線。提醒 a≠0，若 x² 係數是 0 就變一次函數（直線）。");
})();

// S6 開口方向（CRA 表徵：p_updown 圖）
(function () {
  const s = newSlide(false);
  title(s, "開口方向，看 a 的正負", "站① · 看圖");
  const iw = 5.5, ih = iw / 1.1875, iy = 1.95;
  card(s, 0.7, iy, iw + 0.3, ih + 0.3, C.white);
  s.addImage({ path: A("p_updown.png"), x: 0.85, y: iy + 0.15, w: iw, h: ih });
  const rx = 6.9, rw = 5.75;
  const rows = [
    ["a > 0", "開口向上，像笑臉 ∪"],
    ["a < 0", "開口向下，像哭臉 ∩"],
    ["|a| 越大", "開口越窄"],
  ];
  let y = iy + 0.15;
  rows.forEach((r) => {
    card(s, rx, y, rw, 1.32, C.block);
    s.addText(r[0], { x: rx + 0.3, y: y, w: 1.9, h: 1.32, align: "left", valign: "middle", fontFace: MONO, fontSize: 26, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: rx + 2.15, y: y, w: rw - 2.35, h: 1.32, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 1.5;
  });
  footer(s, N, false);
  s.addNotes("先看圖建立畫面：y=x² 開口向上、y=−x² 開口向下。口訣：a 正笑、a 負哭。|a| 越大開口越窄（夾得越緊）。");
})();

// S7 頂點式與平移
(function () {
  const s = newSlide(false);
  title(s, "頂點式：一眼看出頂點", "站① · 頂點式");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.85, w: 11.7, h: 1.15, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("y = a(x − h)² + k", { x: 1.1, y: 1.85, w: 11.1, h: 1.15, align: "left", valign: "middle", fontFace: MONO, fontSize: 30, bold: true, color: C.white });
  const rows = [
    ["頂點", "(h, k)"],
    ["對稱軸", "直線 x = h"],
    ["怎麼來", "由 y = ax² 平移得到"],
  ];
  let y = 3.3;
  rows.forEach((r) => {
    s.addText(r[0], { x: 0.9, y: y, w: 2.4, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 3.3, y: y, w: 5.0, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    y += 0.75;
  });
  card(s, 8.5, 3.2, 4.0, 2.3, C.block);
  s.addText("例", { x: 8.7, y: 3.32, w: 3.6, h: 0.4, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  s.addText("y = 2(x − 1)² + 3", { x: 8.7, y: 3.78, w: 3.6, h: 0.5, fontFace: MONO, fontSize: 21, bold: true, color: C.ink, align: "left" });
  s.addText("頂點 (1, 3)\n對稱軸 x = 1", { x: 8.7, y: 4.35, w: 3.6, h: 1.0, fontFace: F, fontSize: 21, color: C.ink, align: "left", lineSpacingMultiple: 1.2 });
  footer(s, N, false);
  s.addNotes("頂點式的好處：h、k 直接就是頂點座標。提醒括號裡是 (x − h)，所以 (x−1) 對應 h=1（號要反過來看）。");
})();

// S8 步驟卡：一般式化頂點式（配方）
(function () {
  const s = stepCardSlide("站① · 配方（步驟卡）", "一般式 → 頂點式（配方）", "把 y = x² − 4x + 3 化頂點式", [
    "看 x 的係數 −4，取一半 = −2，平方 = 4",
    "湊完全平方：x² − 4x + 4 = (x − 2)²",
    "補回常數：y = (x − 2)² − 4 + 3",
    "整理：y = (x − 2)² − 1 → 頂點 (2, −1)、軸 x = 2",
  ], "配方口訣：一次係數的一半，平方，加了要補回。慢慢做，重點在「加多少就要減多少」。");
  s.addShape(p.ShapeType.roundRect, { x: 8.6, y: 1.75, w: 3.9, h: 0.9, rectRadius: 0.1, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("對稱軸也可用 x = −b / 2a", { x: 8.7, y: 1.75, w: 3.7, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 16, bold: true, color: C.white });
})();

// S9 圖像頁（表徵）：y=x²−4x+3 的圖
graphSlide("站① · 看圖對照", "配方後，畫得出這條拋物線", A("p_vertex.png"), 1.1875, [
  "y = x² − 4x + 3 = (x − 2)² − 1",
  "開口向上（a = 1 > 0）",
  "頂點 (2, −1)、對稱軸 x = 2",
  "與 x 軸：(1, 0)、(3, 0)",
  "與 y 軸：(0, 3)",
], "把配方結果和圖對起來：頂點在最低點，對稱軸把拋物線分成左右對稱兩半。與 x 軸交點就是 y=0 的解。");

// S10 視覺鷹架頁：讀拋物線四格
scaffoldSlide("站① · 讀圖鷹架", "讀一條拋物線（照著填四格）", [
  ["① 開口", "看 a：正向上、負向下"],
  ["② 對稱軸", "x = h（或 x = −b/2a）"],
  ["③ 頂點", "(h, k)，配方後看得出"],
  ["④ 交點", "y=0 解 x；x=0 得 y"],
], "鷹架先撐後撤：前幾題照四格一格一格填，熟了就不用模板。每條拋物線都問同樣四件事。");

// S11 轉換點
breakSlide("下一頁換你做：挑一顆星開始");

// S12 分層任務頁 站①
tieredTasks("站① · 分層練習",
  [
    ["1. 看頂點式讀開口/軸/頂點\ny = 2(x−1)²+3；y = −(x+2)²−1", "2. 配方填空\ny = x² − 6x + 5 → (x−□)²−□"],
    ["3. 化頂點式並求交點\ny = x² + 2x − 3", "4. 看圖寫頂點、對稱軸\n並估 x 軸交點"],
    ["5. 頂點 (1,−4) 且過 (3,0)\n求 a、b、c", "6. 找錯：把 x²−4x+3\n配成 (x−2)²+3，錯在哪？"],
  ],
  "解答核對｜A1: (1)上,x=1,頂點(1,3)；(2)下,x=−2,頂點(−2,−1)。A2: (x−3)²−4,頂點(3,−4)。 B3: (x+1)²−4;上;軸x=−1;頂點(−1,−4);與x軸(−3,0)(1,0);與y軸(0,−3)。B4: 頂點(1,4),軸x=1,x軸約(−1,0)(3,0)。 C5: y=(x−1)²−4=x²−2x−3,a=1,b=−2,c=−3。C6: 配方漏了常數,(x−2)²=x²−4x+4,要 −4+3=−1,正確 y=(x−2)²−1。"
);

// S13 總結 站①
summarySlide("站① · 總結",
  "二次函數的圖像是拋物線；配方後就能讀出頂點和對稱軸。",
  "看到 x² 就是拋物線；a > 0 開口向上，a < 0 開口向下。").addNotes("回收站①：配方 → 頂點式 → 讀圖。保底句要全班能覆述。");

// =====================================================================
// 站② 二次函數與方程、應用
// =====================================================================
stationDivider("站②", "二次函數與方程、應用", "交點就是方程的根；最值在頂點").addNotes("進入站②。兩個賣點：拋物線和 x 軸的交點＝方程的根；生活裡的「最大／最小」用頂點求。");

// S15 問題引入：交點是什麼
(function () {
  const s = newSlide(false);
  title(s, "拋物線和 x 軸的交點，是什麼？", "站② · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.4, y: 2.3, w: 10.5, h: 2.4, rectRadius: 0.18, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("交點的 x 坐標，", { x: 1.4, y: 2.55, w: 10.5, h: 0.8, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.ink });
  s.addText("就是方程 ax² + bx + c = 0 的根！", { x: 1.7, y: 3.45, w: 9.9, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 30, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("把站①的「圖」接到「方程」：令 y=0，就是解方程。圖上的交點 ↔ 方程的根，是同一件事。");
})();

// S16 判別式 Δ 三情況
(function () {
  const s = newSlide(false);
  title(s, "看 Δ，就知道有幾個交點", "站② · 概念");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.7, w: 11.7, h: 0.8, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText("判別式 Δ = b² − 4ac", { x: 1.1, y: 1.7, w: 11.1, h: 0.8, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });
  const data = [
    ["Δ > 0", "兩個交點", "兩個相異的根"],
    ["Δ = 0", "一個交點", "頂點正好在 x 軸上"],
    ["Δ < 0", "沒有交點", "方程無實根"],
  ];
  const x0 = 0.8, gap = 0.3, w = (11.7 - 2 * gap) / 3, yTop = 2.75, h = 3.35;
  data.forEach((d, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 1.0, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
    s.addText(d[0], { x, y: yTop, w, h: 1.0, align: "center", valign: "middle", fontFace: MONO, fontSize: 30, bold: true, color: C.white });
    s.addText(d[1], { x: x + 0.2, y: yTop + 1.2, w: w - 0.4, h: 1.0, align: "center", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(d[2], { x: x + 0.2, y: yTop + 2.35, w: w - 0.4, h: 0.85, align: "center", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
  });
  footer(s, N, false);
  s.addNotes("Δ 就像紅綠燈：正=兩個交點、零=一個（相切）、負=不相交。先算 Δ 再說。");
})();

// S17 案例頁：三題算 Δ
(function () {
  const s = newSlide(false);
  title(s, "三題練算 Δ（不用解方程）", "站② · 範例");
  const data = [
    ["y = x² − 4x + 1", "Δ = 16 − 4 = 12 > 0", "兩個交點"],
    ["y = x² − 6x + 9", "Δ = 36 − 36 = 0", "一個交點（相切）"],
    ["y = x² + x + 1", "Δ = 1 − 4 = −3 < 0", "沒有交點"],
  ];
  let y = 2.05;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.35, C.white);
    s.addText(d[0], { x: 1.1, y: y, w: 4.0, h: 1.35, align: "left", valign: "middle", fontFace: MONO, fontSize: 23, bold: true, color: C.ink });
    s.addText(d[1], { x: 5.2, y: y, w: 4.1, h: 1.35, align: "left", valign: "middle", fontFace: MONO, fontSize: 22, color: C.sageDeep });
    s.addText(d[2], { x: 9.4, y: y, w: 3.0, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink });
    y += 1.5;
  });
  footer(s, N, false);
  s.addNotes("步驟固定：找 a,b,c → 算 b²−4ac → 看正負。帶全班一題一題算，強調符號（負負得正）。");
})();

// S18 圖像頁（表徵）：y=x²−2x−3 與 x 軸交點
graphSlide("站② · 看圖對照", "交點就是根：看這條拋物線", A("p_roots.png"), 1.1875, [
  "y = x² − 2x − 3",
  "Δ = 4 + 12 = 16 > 0 → 兩個交點",
  "解 (x − 3)(x + 1) = 0",
  "→ 交點 (−1, 0)、(3, 0)",
  "頂點 (1, −4)",
], "圖上兩個交點，就是方程 x²−2x−3=0 的兩個根 x=3、−1。把「圖的交點」和「方程的根」畫上等號。");

// S19 步驟卡：用二次函數求最值
(function () {
  const s = stepCardSlide("站② · 求最值（步驟卡）", "用二次函數求最大／最小值", "實際問題：先列函數，再配方求頂點", [
    "設未知數：把要求的量設成 x",
    "列出二次函數 y = …（照題意）",
    "配方求頂點：頂點的 y 就是最值",
    "檢驗作答：長度、面積不能是負數",
  ], "口訣：開口向上有最小值、開口向下有最大值，都在頂點取得。第四步一定要檢查答案合不合理。");
  s.addShape(p.ShapeType.roundRect, { x: 8.6, y: 1.75, w: 3.9, h: 0.9, rectRadius: 0.1, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("最值都在「頂點」", { x: 8.7, y: 1.75, w: 3.7, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
})();

// S20 範例（CRA/鷹架）：籬笆最大面積（p_area 圖）
(function () {
  const s = newSlide(false);
  title(s, "範例：籬笆圍出最大面積", "站② · 具體 → 抽象");
  s.addShape(p.ShapeType.roundRect, { x: 0.7, y: 1.72, w: 11.95, h: 0.72, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText("用長 20 米的籬笆圍成矩形（不靠牆），面積最大是多少？", { x: 1.0, y: 1.72, w: 11.4, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
  // 左：面積拋物線圖
  const iw = 5.15, ih = iw / 1.26667, iy = 2.55;
  card(s, 0.7, iy, iw + 0.3, ih + 0.3, C.white);
  s.addImage({ path: A("p_area.png"), x: 0.85, y: iy + 0.15, w: iw, h: ih });
  // 右：四步
  const rx = 6.85;
  const lines = [
    "① 設寬 x，長 = 10 − x（長+寬=10）",
    "② 面積 y = x(10 − x)",
    "③ 配方：y = −(x − 5)² + 25",
    "④ x = 5 時面積最大 = 25 平方米",
  ];
  let y = iy + 0.05;
  lines.forEach((l) => {
    s.addText(l, { x: rx, y: y, w: 5.9, h: 0.78, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 0.82;
  });
  hlBox(s, rx, y + 0.05, 5.9, 0.72);
  s.addText("即邊長 5 的正方形（頂點 (5, 25)）", { x: rx + 0.15, y: y + 0.05, w: 5.6, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("先看圖（開口向下、頂點是最高點＝最大面積），再看四步列式。強調頂點的 y=25 就是最大面積。");
})();

// S21 視覺鷹架頁：應用四格
scaffoldSlide("站② · 應用鷹架", "應用題模板（照著填四格）", [
  ["① 問什麼", "求最大值 / 最小值"],
  ["② 已知", "列出關係（如 長+寬=定值）"],
  ["③ 策略算式", "寫出 y = … → 配方求頂點"],
  ["④ 解答驗算", "頂點 y 就是最值；答案要合理"],
], "應用題不可怕，套四格模板就有骨架。鷹架先撐後撤：熟了以後心裡有這四步就好。");

// S22 轉換點
breakSlide("下一頁換你做：先算 Δ，或先設 x");

// S23 分層任務頁 站②
tieredTasks("站② · 分層練習",
  [
    ["1. 算 Δ 判交點個數\nx²−4x+1、x²−6x+9、x²+x+1", "2. 求與 x 軸交點\ny = x² − x − 6"],
    ["3. 求交點、頂點、最大值\ny = −x² + 4x − 3", "4. 籬笆 24 米圍矩形\n求長寬與最大面積"],
    ["5. 進價 40，售 x 元賣 (100−x) 件\n求售價定多少利潤最大", "6. 最小值 −5 且過 (0,−1)\ny = ax²−4x+c，求 a、c"],
  ],
  "解答核對｜A1: Δ=12>0(2個)、Δ=0(1個)、Δ=−3<0(0個)。A2: (x−3)(x+2)=0 → (3,0)(−2,0)。 B3: y=−(x−2)²+1,頂點(2,1),最大值1,與x軸(1,0)(3,0),與y軸(0,−3)。B4: 長+寬=12,y=−(x−6)²+36,x=6(邊長6正方形),最大面積36平方米。 C5: y=(x−40)(100−x)=−(x−70)²+900,售價70元最大利潤900元。C6: 過(0,−1)→c=−1;最小值 c−4/a=−1−4/a=−5 → a=1;答 a=1,c=−1。"
);

// S24 總結 站②
summarySlide("站② · 總結",
  "拋物線與 x 軸的交點就是方程的根；最大最小值都在頂點。",
  "先算 Δ = b² − 4ac 看幾個交點；求最值先配方找頂點。").addNotes("回收站②。保底：會算 Δ 判交點、會用頂點找最值，就達標。");

// =====================================================================
// 收尾
// =====================================================================
// S25 兩站總複習
(function () {
  const s = newSlide(false);
  title(s, "兩站帶走話，一次回顧");
  const data = [
    ["站①", "二次函數圖像是拋物線；配方讀出頂點與對稱軸。"],
    ["站②", "交點就是方程的根（看 Δ）；最大最小值都在頂點。"],
  ];
  let y = 2.25;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.55, C.white);
    stationBadge(s, d[0], 0.95, y + 0.46);
    s.addText(d[1], { x: 2.9, y: y, w: 9.4, h: 1.55, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    y += 1.8;
  });
  footer(s, N, false);
  s.addNotes("整體回收。可請學生每站講一句自己的話覆述。");
})();

// S26 結語（asset-based）
(function () {
  const s = newSlide(true);
  s.addText("你已經走完兩站！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("二次函數的圖像和應用，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次遇到拋物線，記得先問：開口向哪？頂點在哪？", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, italic: true, color: "9FB8AE" });
  s.addNotes("正向收束，asset-based。肯定努力與策略，不用「終於」「總算」等字眼。");
})();

// S27 教師備註頁
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
    "◆ 看圖先行：拋物線圖建立畫面（CRA 表徵）",
    "◆ 步驟卡：配方 / 求最值一步一行、編號",
    "◆ 視覺鷹架：讀圖四格 / 應用四格模板",
    "◆ 轉換點＋預告：照顧注意力節奏",
    "◆ 保底成功句＋asset-based 用語",
  ];
  card(s, 0.7, 1.9, 5.85, 4.4, C.white);
  s.addText("調整定位", { x: 0.95, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(left.join("\n"), { x: 0.95, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
  card(s, 6.75, 1.9, 5.85, 4.4, C.white);
  s.addText("融合層做了什麼", { x: 7.0, y: 2.05, w: 5.4, h: 0.5, fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  s.addText(right.join("\n"), { x: 7.0, y: 2.6, w: 5.4, h: 3.5, align: "left", valign: "top", fontFace: F, fontSize: 19, color: C.ink, lineSpacingMultiple: 1.35 });
  footer(s, N, false);
  s.addNotes("此頁供教師/IEP 對接用，上課可略過。屬 Accommodation，未剪裁課程內容；未含任何學生可識別資料。");
})();

// ---- 輸出 ----
p.writeFile({ fileName: path.join(__dirname, "簡報_二次函數_圖像到應用_融合抽離版.pptx") }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
