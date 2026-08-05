// 融合抽離小組 SOIL 教學簡報：一元二次方程（概念→判別式→應用）
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "初三數學抽離小組";
p.title = "一元二次方程 三站通關（融合抽離版）";

// ---- 配色 (Sage Calm 低刺激) ----
const C = {
  bgLight: "EDF3F0", // 淺灰綠，非純白
  bgDark: "2E4A43",  // 深松綠（封面/站牌/結語）
  ink: "233A34",     // 本文深墨綠
  soft: "5C6F68",    // 次要說明
  sage: "6FA48C",    // 主色 sage
  sageDeep: "4E8770",// 深 sage（步驟圓圈/重點）
  slate: "50808E",   // 輔色 slate
  block: "DCEAE3",   // 淺色塊底（強調）
  block2: "CFE0D8",  // 稍深色塊（卡片）
  cardLine: "B9CFC5",// 卡片邊
  white: "FFFFFF",
  starInk: "2E4A43",
};
const F = "Microsoft JhengHei"; // 微軟正黑體
const MONO = "Consolas";

// ---- 共用小工具 ----
function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("初三數學 · 一元二次方程（抽離小組·融合版）", {
    x: 0.5, y: 7.06, w: 9.5, h: 0.32, align: "left", valign: "middle",
    fontFace: F, fontSize: 11, color: dark ? "9FB8AE" : "8CA298",
  });
  s.addText(String(n), {
    x: 12.2, y: 7.06, w: 0.9, h: 0.32, align: "right", valign: "middle",
    fontFace: F, fontSize: 11, color: dark ? "9FB8AE" : "8CA298",
  });
}
// 標題（左上、無底線、無色條）
function title(s, txt, kicker) {
  if (kicker) {
    s.addText(kicker, { x: 0.6, y: 0.42, w: 12, h: 0.4, fontFace: F, fontSize: 18, bold: true, color: C.sageDeep, align: "left" });
    s.addText(txt, { x: 0.6, y: 0.82, w: 12.1, h: 0.8, fontFace: F, fontSize: 34, bold: true, color: C.ink, align: "left" });
  } else {
    s.addText(txt, { x: 0.6, y: 0.5, w: 12.1, h: 0.9, fontFace: F, fontSize: 34, bold: true, color: C.ink, align: "left" });
  }
}
// 圓圈步驟碼（motif）
function stepCircle(s, x, y, n, d) {
  const dia = d || 0.5;
  s.addShape(p.ShapeType.ellipse, { x, y, w: dia, h: dia, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText(String(n), { x, y, w: dia, h: dia, align: "center", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.white });
}
// 站牌徽章
function stationBadge(s, txt, x, y) {
  s.addShape(p.ShapeType.roundRect, { x, y, w: 1.7, h: 0.62, rectRadius: 0.31, fill: { color: C.sage }, line: { type: "none" } });
  s.addText(txt, { x, y, w: 1.7, h: 0.62, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
}
// 淺色卡片
function card(s, x, y, w, h, fill) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.12, fill: { color: fill || C.white }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
}
// 強調色塊（關鍵字底）— 由呼叫端放文字
function hlBox(s, x, y, w, h) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: C.block }, line: { type: "none" } });
}

// ---- 原生分數（分子／橫線／分母直式疊字，非 "/" 斜線寫法）----
// 置中於 (cx, cy)，回傳整個分數視覺寬度（方便呼叫端排下一個元素）
// 寬度刻意放寬（含足夠內邊距緩衝），避免文字框預設 margin 吃掉可用闊度令文字換行錯位
function fracW(num, den, fs) {
  return Math.max(String(num).length, String(den).length) * (fs * 0.62 / 72) + 0.34;
}
function frac(s, cx, cy, num, den, size, color) {
  const fs = size || 20;
  const w = fracW(num, den, fs);
  const hh = fs / 72 * 1.35; // 容納單行文字所需高度，避免溢出鄰行
  s.addText(String(num), { x: cx - w / 2, y: cy - hh - 0.04, w, h: hh, margin: 0, wrap: false, align: "center", valign: "bottom", fontFace: MONO, fontSize: fs, bold: true, color: color || C.ink });
  seg(s, cx - w / 2 + 0.08, cy, cx + w / 2 - 0.08, cy, { color: color || C.ink, width: 1.5 });
  s.addText(String(den), { x: cx - w / 2, y: cy + 0.04, w, h: hh, margin: 0, wrap: false, align: "center", valign: "top", fontFace: MONO, fontSize: fs, bold: true, color: color || C.ink });
  return w;
}
// 一行內「文字／分數」混排 segs=[{t:"文字"}] 或 [{n,d}]，靠左起於 (x,y)，列高 h
// 用於分數出現在一句話中間（如 x = (3±7)/4）時，取代 "/" 斜線寫法
// o.fracFontSize：分數字級可獨立細於前後文字（緊密表格列常用），預設同 fontSize
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
// 線段（分數橫線用）
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
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 1.5, w: 3.0, h: 0.7, rectRadius: 0.35, fill: { color: C.sage }, line: { type: "none" } });
  s.addText("初三數學 · 抽離小組", { x: 0.9, y: 1.5, w: 3.0, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 18, bold: true, color: C.white });
  s.addText("一元二次方程", { x: 0.85, y: 2.45, w: 11.6, h: 1.1, fontFace: F, fontSize: 54, bold: true, color: C.white, align: "left" });
  s.addText("三站通關", { x: 0.85, y: 3.5, w: 11.6, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: "CFE0D8", align: "left" });
  s.addText([
    { text: "站① 四種解法", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "   →   ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "站② 判別式與根", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
    { text: "   →   ", options: { fontFace: F, fontSize: 22, color: C.sage } },
    { text: "站③ 應用題", options: { fontFace: F, fontSize: 22, color: "E7F0EB" } },
  ], { x: 0.9, y: 4.75, w: 11.6, h: 0.6, align: "left", valign: "middle" });
  s.addText("融合版 · 同一份簡報，跟著三站一步一步走", { x: 0.9, y: 5.5, w: 11.6, h: 0.5, fontFace: F, fontSize: 18, italic: true, color: "9FB8AE", align: "left" });
  s.addNotes("開場定調：今天不趕進度，跟著三站走。每一站都是：學一招 → 看老師示範 → 自己挑星星練習。做得起就往上跳一層。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// =====================================================================
(function () {
  const s = newSlide(false);
  title(s, "今日課堂流程");
  const rows = [
    ["站①", "四種解法", "降次 → 配方 → 公式 → 因式分解"],
    ["站②", "判別式與根", "不解方程，看出有幾個根、根的和與積"],
    ["站③", "應用題", "文字題四步驟：設 → 列 → 解 → 驗"],
  ];
  let y = 1.95;
  rows.forEach((r, i) => {
    card(s, 0.7, y, 11.9, 1.28);
    stationBadge(s, r[0], 0.95, y + 0.33);
    s.addText(r[1], { x: 2.85, y: y + 0.14, w: 9.4, h: 0.55, fontFace: F, fontSize: 26, bold: true, color: C.ink, align: "left", valign: "middle" });
    s.addText(r[2], { x: 2.85, y: y + 0.66, w: 9.4, h: 0.5, fontFace: F, fontSize: 20, color: C.soft, align: "left", valign: "middle" });
    y += 1.5;
  });
  s.addText("每一站都一樣：學一招 → 看範例 → 挑星星練習 ★", { x: 0.7, y: 6.5, w: 11.9, h: 0.45, fontFace: F, fontSize: 18, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖：讓學生知道整節課的結構，減少焦慮。強調三站節奏一致，做完一站休息一下。");
})();

// =====================================================================
// 站牌 / 過渡頁 產生器（dark）
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

// =====================================================================
// 轉換點預告頁（極簡）
// =====================================================================
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

// =====================================================================
// 分層任務頁 產生器（三欄同版面）
// =====================================================================
function tieredTasks(kicker, cols, noteKey) {
  const s = newSlide(false);
  title(s, "挑戰練習 · 自選星星", kicker);
  const tiers = [
    { t: "練習 A", star: "★☆☆", tint: C.white },
    { t: "練習 B", star: "★★☆", tint: C.white },
    { t: "練習 C", star: "★★★", tint: C.white },
  ];
  const x0 = 0.65, gap = 0.28, w = (12.1 - 2 * gap) / 3, yTop = 1.95, h = 4.35;
  tiers.forEach((ti, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, ti.tint);
    s.addShape(p.ShapeType.roundRect, { x: x, y: yTop, w: w, h: 0.9, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(ti.t, { x: x + 0.2, y: yTop + 0.06, w: w - 0.4, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(ti.star, { x: x + 0.2, y: yTop + 0.46, w: w - 0.4, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.starInk });
    // 題目行
    const items = cols[i];
    let ty = yTop + 1.08;
    items.forEach((it) => {
      s.addText(it, { x: x + 0.24, y: ty, w: w - 0.46, h: 0.95, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
      ty += 1.02;
    });
  });
  s.addText("做得起 A，就往 B、C 跳一層 ↗   全部同一個概念，只是鷹架不同", { x: 0.65, y: 6.5, w: 12.1, h: 0.45, fontFace: F, fontSize: 17, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(noteKey);
  return s;
}

// =====================================================================
// 總結頁 產生器（帶走一句話 + 保底版）
// =====================================================================
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
// 站① 四種解法（同步單元01改版：降次 → 配方 → 公式 → 因式分解）
// =====================================================================
stationDivider("站①", "四種解法", "四種方法，各有最快的時機").addNotes("進入站①。強調：四種方法答案一定一樣，只是快慢不同。先建立信心。");

// S4 問題引入
(function () {
  const s = newSlide(false);
  title(s, "哪一條是「一元二次方程」？", "站① · 引入");
  const data = [
    ["x² − 2x + 1 = 0", "是 ✔", "一個未知數，最高次是 2", true],
    ["x² + 3 = 2 / x", "✗ 不是", "分母有 x，不是整式", false],
    ["x² − 2y + 4 = 0", "✗ 不是", "有 x、y 兩個未知數", false],
  ];
  let y = 2.1;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.15, d[3] ? C.block : C.white);
    s.addText(d[0], { x: 1.1, y: y, w: 5.2, h: 1.15, align: "left", valign: "middle", fontFace: MONO, fontSize: 28, bold: true, color: C.ink });
    s.addText(d[1], { x: 6.4, y: y, w: 1.9, h: 1.15, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: d[3] ? C.sageDeep : C.soft });
    s.addText(d[2], { x: 8.4, y: y, w: 4.0, h: 1.15, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.33;
  });
  footer(s, N, false);
  s.addNotes("低門檻暖身：只判斷「是不是」，人人答得出。口頭補充：一元＝一個未知數，二次＝最高次方是 2。");
})();

// S5 概念 + 保底
(function () {
  const s = newSlide(false);
  title(s, "一般式與辨識 a、b、c", "站① · 概念（保底）");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.85, w: 11.7, h: 1.15, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText([
    { text: "a x² + b x + c = 0", options: { fontFace: MONO, fontSize: 30, bold: true, color: C.white } },
    { text: "     （ a ≠ 0 ）", options: { fontFace: F, fontSize: 24, color: "CFE0D8" } },
  ], { x: 1.1, y: 1.85, w: 11.1, h: 1.15, align: "left", valign: "middle" });
  // 三步辨識
  const steps = [
    ["1", "先整理成「＝ 0」"],
    ["2", "x² 前的數 = a，x 前的數 = b"],
    ["3", "剩下的常數 = c"],
  ];
  let y = 3.25;
  steps.forEach((st) => {
    stepCircle(s, 0.9, y, st[0], 0.5);
    s.addText(st[1], { x: 1.6, y: y - 0.06, w: 6.6, h: 0.62, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    y += 0.78;
  });
  // 範例卡
  card(s, 8.5, 3.2, 4.0, 2.35, C.block);
  s.addText("例", { x: 8.7, y: 3.32, w: 3.6, h: 0.4, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  s.addText("2x² + 3x − 1 = 0", { x: 8.7, y: 3.75, w: 3.6, h: 0.5, fontFace: MONO, fontSize: 22, bold: true, color: C.ink, align: "left" });
  s.addText("a = 2　b = 3　c = −1", { x: 8.7, y: 4.35, w: 3.6, h: 0.5, fontFace: F, fontSize: 22, color: C.ink, align: "left" });
  s.addText("認得 a、b、c，你就開始了 👍", { x: 8.7, y: 4.95, w: 3.6, h: 0.5, fontFace: F, fontSize: 18, italic: true, color: C.soft, align: "left" });
  footer(s, N, false);
  s.addNotes("保底成功經驗：全班都要能認出 a、b、c。提醒 a≠0，若 x² 係數是 0 就變一元一次。");
})();

// S6 路線圖頁：四種方法的教學順序（同步講義「教學順序」段）
(function () {
  const s = newSlide(false);
  title(s, "四種方法，這樣一層層學上去", "站① · 路線圖");
  const rows = [
    ["1", "直接開平方法（降次）", "把 x² 變成兩條一次方程"],
    ["2", "配方法", "把任何方程變成 ① 的樣子"],
    ["3", "公式法", "把 ② 的過程一般化，直接代"],
    ["4", "因式分解法", "看得出因式，就抄捷徑"],
  ];
  let y = 1.88;
  rows.forEach((r) => {
    card(s, 0.7, y, 11.9, 1.02, C.white);
    stepCircle(s, 0.95, y + 0.26, r[0], 0.5);
    s.addText(r[1], { x: 1.75, y: y, w: 4.35, h: 1.02, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(r[2], { x: 6.2, y: y, w: 6.15, h: 1.02, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.18;
  });
  s.addText("前三種一層層疊上去；第四種是有把握時的快捷鍵", { x: 0.7, y: 6.55, w: 11.9, h: 0.42, fontFace: F, fontSize: 18, italic: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("先給地圖。重點講「為什麼是這個順序」：配方法是為了變回方法一；公式法是把配方一般化；因式分解排最後，是熟練後的捷徑，不是起點。");
})();

// S7 方法一 概念頁：x² = p 的三種情況
(function () {
  const s = newSlide(false);
  title(s, "x² = p：右邊的數決定有沒有根", "站① · 方法一 概念");
  const data = [
    ["p > 0", "兩個不等實根", "x = √p 或 −√p"],
    ["p = 0", "兩個相等實根", "x = 0"],
    ["p < 0", "沒有實數根", "平方不會是負數"],
  ];
  const x0 = 0.8, gap = 0.3, w = (11.7 - 2 * gap) / 3, yTop = 2.15, h = 3.6;
  data.forEach((d, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 1.0, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
    s.addText(d[0], { x, y: yTop, w, h: 1.0, align: "center", valign: "middle", fontFace: MONO, fontSize: 30, bold: true, color: C.white });
    s.addText(d[1], { x: x + 0.2, y: yTop + 1.25, w: w - 0.4, h: 1.1, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
    s.addText(d[2], { x: x + 0.2, y: yTop + 2.5, w: w - 0.4, h: 0.9, align: "center", valign: "middle", fontFace: MONO, fontSize: 20, color: C.soft });
  });
  s.addText("開平方之前，先看右邊是正、零，還是負", { x: 0.8, y: 6.0, w: 11.7, h: 0.45, fontFace: F, fontSize: 20, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes("這一頁擋住最常見的錯：x² = −9 寫成 x = ±3。負數沒有實數平方根，要直接答「無實數根」。");
})();

// 步驟卡頁 產生器
function stepCardSlide(kicker, head, eqn, steps, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.75, w: 11.7, h: 0.9, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText("解 " + eqn, { x: 1.1, y: 1.75, w: 11.1, h: 0.9, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });
  let y = 2.95;
  const rowH = (6.4 - 2.95) / steps.length;
  steps.forEach((st, i) => {
    stepCircle(s, 0.85, y + (rowH - 0.5) / 2, i + 1, 0.5);
    if (Array.isArray(st)) {
      // 一行內含分數：segs 陣列（{t:"文字"} 或 {n,d}）
      fracRow(s, 1.55, y, rowH, st, { fontFace: F, fontSize: 22, bold: false, color: C.ink });
    } else {
      s.addText(st, { x: 1.55, y: y, w: 10.9, h: rowH, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    }
    y += rowH;
  });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}

// 方法頁 產生器：左「手順卡」＋右「範例」，底部易錯提醒
// 手順措辭逐字沿用講義《手順卡①–④》（主設計 D2 同步）；
// 範例採講義版面規範：左算式／右說明，一行一個等號。
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
    const tx = lx + 0.85, tw = lw - 1.1;
    if (st && typeof st === "object" && st.line1) {
      // 一步含分數：第一行「文字＋分數」、第二行純文字
      fracRow(s, tx, ly + lRowH * 0.04, lRowH * 0.5, st.line1, { fontFace: F, fontSize: 20, bold: false, color: C.ink });
      s.addText(st.line2, { x: tx, y: ly + lRowH * 0.56, w: tw, h: lRowH * 0.4, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink });
    } else {
      s.addText(st, { x: tx, y: ly, w: tw, h: lRowH, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.3 });
    }
    ly += lRowH;
  });

  // ---- 右：範例（左算式／右說明）----
  const rx = 6.45, rw = 6.3;
  card(s, rx, yTop, rw, H, C.white);
  s.addShape(p.ShapeType.roundRect, { x: rx, y: yTop, w: rw, h: bandH, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
  s.addText("範例：解 " + exTitle, { x: rx + 0.25, y: yTop, w: rw - 0.5, h: bandH, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.white });
  let ry = yTop + bandH + 0.14;
  const rRowH = (yEnd - ry) / exRows.length;
  exRows.forEach((row, i) => {
    if (i % 2 === 1) s.addShape(p.ShapeType.rect, { x: rx + 0.13, y: ry, w: rw - 0.26, h: rRowH, fill: { color: C.block }, line: { type: "none" } });
    if (Array.isArray(row[0])) {
      fracRow(s, rx + 0.3, ry, rRowH, row[0], { fontFace: MONO, fontSize: 21, bold: true, color: C.ink, fracFontSize: 14 });
    } else {
      s.addText(row[0], { x: rx + 0.3, y: ry, w: 3.95, h: rRowH, align: "left", valign: "middle", fontFace: MONO, fontSize: 21, bold: true, color: C.ink });
    }
    s.addText(row[1], { x: rx + 4.3, y: ry, w: 1.75, h: rRowH, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    ry += rRowH;
  });

  s.addText(hint, { x: 0.6, y: 6.5, w: 12.15, h: 0.45, fontFace: F, fontSize: 18, bold: true, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}

// S8 方法一：直接開平方法（降次）
methodSlide("站① · 方法一", "直接開平方法（降次）", [
  "化成 x² = p 或 (x + k)² = c 的形式",
  "看右邊的數是正、零還是負",
  "右邊 > 0 就兩邊開平方，寫成 ±",
  "左邊還有 + k 就再移項，\n解出兩個根",
], "(x − 4)² − 9 = 0", [
  ["(x − 4)² − 9 = 0", "原方程"],
  ["(x − 4)² = 9", "移項"],
  ["x − 4 = ± 3", "開平方"],
  ["x = 4 ± 3", "再移項"],
  ["x = 7 或 x = 1", "兩個根"],
], "※「降次」＝把一條二次方程變成兩條一次方程；別漏寫 ±，只寫一個會漏解",
  "本課第一種方法。先講清楚「降次」這個詞：二次降成一次，就回到已經會解的東西。開平方那一步全班一齊寫 ±。");

// S9 方法二：配方法
methodSlide("站① · 方法二", "配方法", [
  "x² 前面的係數不是 1，\n兩邊先除以它",
  "把常數移到等號右邊",
  "兩邊同時加\n「一次項係數一半的平方」",
  "左邊配成 (x + k)²，\n套用手順卡①解出兩個根",
], "x² + 6x − 1 = 0", [
  ["x² + 6x − 1 = 0", "原方程"],
  ["x² + 6x = 1", "移項"],
  ["x² + 6x + 9 = 1 + 9", "兩邊加 9"],
  ["(x + 3)² = 10", "配成平方"],
  ["x + 3 = ± √10", "開平方"],
  ["x = −3 ± √10", "兩個根"],
], "※ 加的 9 ＝ (6 ÷ 2)²，即「一次項係數一半的平方」；兩邊都要加",
  "配方法的目的講白：把方程變成方法一的樣子。最後兩步就是手順卡①，讓學生看見銜接。");

// S10 轉換點
breakSlide("先動手：方法一、方法二各做一題");

// S11 方法三：公式法
methodSlide("站① · 方法三", "公式法", [
  "化成一般式，寫出 a、b、c",
  "算判別式 Δ = b² − 4ac",
  "看 Δ：Δ < 0 無解、\nΔ = 0 一個重根、Δ > 0 兩個根",
  "代入求根公式\n（見右邊範例），解出兩個根",
], "2(x² − 1) = 3x + 3", [
  ["2(x² − 1) = 3x + 3", "原方程"],
  ["2x² − 3x − 5 = 0", "化成一般式"],
  ["a = 2  b = −3  c = −5", "讀出係數"],
  ["Δ = (−3)² − 4(2)(−5)", "算判別式"],
  ["Δ = 49", "Δ > 0 兩根"],
  [[{ t: "x = " }, { n: "3 ± 7", d: "4" }], "代入公式"],
  [[{ t: "x = " }, { n: "5", d: "2" }, { t: " 或 x = −1" }], "兩個根"],
], "※ (−3)² = 9，先平方再算，不是 −9；有括號或分母，一定先整理成一般式才寫 a、b、c",
  "公式法是把配方法一般化——不用每次重新配方。強調兩件事：先化一般式；抄 a、b、c 時連正負號一起抄。");

// S12 CRA 三階頁：因式分解怎樣「看出來」
(function () {
  const s = newSlide(false);
  title(s, "看懂因式分解：具體 → 圖 → 式", "站① · CRA");
  s.addText("解 x² + 2x − 35 = 0", { x: 0.8, y: 1.7, w: 11.7, h: 0.5, fontFace: MONO, fontSize: 24, bold: true, color: C.ink, align: "left" });
  const cols = [
    ["具體", "找兩個數：\n相乘 = −35\n相加 = +2", "→ 7 和 −5"],
    ["表徵", "填方框：\n(x + ▢)(x + ▢)", "▢ 放 7、−5"],
    ["抽象", "寫成算式：\n(x + 7)(x − 5) = 0", "x = −7 或 5"],
  ];
  const x0 = 0.8, gap = 0.3, w = (11.7 - 2 * gap) / 3, yTop = 2.35, h = 3.7;
  cols.forEach((c, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 0.7, rectRadius: 0.12, fill: { color: C.sage }, line: { type: "none" } });
    s.addText(c[0], { x, y: yTop, w, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
    s.addText(c[1], { x: x + 0.2, y: yTop + 0.9, w: w - 0.4, h: 1.7, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.3 });
    hlBox(s, x + 0.2, yTop + 2.95, w - 0.4, 0.6);
    s.addText(c[2], { x: x + 0.2, y: yTop + 2.95, w: w - 0.4, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
    if (i < 2) s.addText("→", { x: x + w - 0.02, y: yTop + 1.3, w: gap + 0.04, h: 0.6, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.sageDeep });
  });
  footer(s, N, false);
  s.addNotes("先具體（湊數）、再圖（填方框）、最後才抽象算式。每階都示範→引導→學生做，不要跳步。湊數時提醒：相乘是負數，兩個數一正一負。");
})();

// S13 方法四：因式分解法
methodSlide("站① · 方法四", "因式分解法", [
  "化成一般式，右邊等於 0",
  "把左邊分解成兩個一次式的乘積",
  "令每個因式分別等於 0",
  "解出兩個根，代回原方程驗根",
], "x² + 2x − 35 = 0", [
  ["x² + 2x − 35 = 0", "原方程"],
  ["(x + 7)(x − 5) = 0", "因式分解"],
  ["x + 7 = 0 或 x − 5 = 0", "各自 = 0"],
  ["x = −7 或 x = 5", "兩個根"],
], "※ 右邊一定要先等於 0 才分解；兩邊都有 x 時先移項，不可以除以 x（會漏根）",
  "排最後，因為它是「看得出就抄捷徑」。學完前三種，學生知道方程一定解得出，因式分解只是省時間。");

// S14 比較頁：四種方法怎麼選（同步講義第六節對照表）
(function () {
  const s = newSlide(false);
  title(s, "四種方法，怎麼選？", "站① · 比較");
  s.addText("先看方程長成什麼樣子，再決定用哪一種——不要每題都從頭試", { x: 0.7, y: 1.55, w: 11.9, h: 0.4, fontFace: F, fontSize: 20, color: C.soft, align: "left" });
  const data = [
    ["已經是 x² = p 或 (x + k)² = c", "① 直接開平方法", "最快"],
    ["一眼看出能因式分解", "④ 因式分解法", "最快"],
    ["分解不出，但係數簡單", "② 配方法", "步步為營"],
    ["係數複雜、配方會出現分數", "③ 公式法", "一定解得出"],
  ];
  let y = 2.05;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.02, C.white);
    s.addText(d[0], { x: 1.0, y: y, w: 5.7, h: 1.02, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    s.addShape(p.ShapeType.roundRect, { x: 6.95, y: y + 0.16, w: 3.4, h: 0.7, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
    s.addText(d[1], { x: 6.95, y: y + 0.16, w: 3.4, h: 0.7, align: "center", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.sageDeep });
    s.addText(d[2], { x: 10.6, y: y, w: 1.85, h: 1.02, align: "left", valign: "middle", fontFace: F, fontSize: 19, italic: true, color: C.soft });
    y += 1.18;
  });
  footer(s, N, false);
  s.addNotes("這頁不再給手順卡——測試學生能否自行判斷（褪除路徑的最後一級）。口訣：先看樣子，再揀方法；揀錯只是慢，不是錯。");
})();

// S15 轉換點
breakSlide("下一頁換你做：挑一顆星開始");

// S16 分層任務頁 站①
tieredTasks("站① · 分層練習",
  [
    ["1. (x−4)²−9=0\n用直接開平方", "2. x²−5x+6=0\n用因式分解"],
    ["3. x²+4x−3=0\n用配方法", "4. 2x²−5x+2=0\n用公式法"],
    ["5. x²+3x−1=0\n自己揀方法", "6. 找錯：x²=−9\n寫成 x=±3，錯在哪？"],
  ],
  "解答核對｜A1: (x−4)²=9 → x=7 或 1；A2: (x−2)(x−3)=0 → x=2 或 3。 B3: (x+2)²=7 → x=−2±√7；B4: Δ=9 → x=2 或 1/2。 C5: 分解不出，用公式法，Δ=13 → x=(−3±√13)/2；C6: −9<0，負數不能開平方，應答「無實數根」。"
);

// S17 總結 站①
summarySlide("站① · 總結",
  "四種解法都通；先看方程長成什麼樣子，再選方法。",
  "分不出因式，就用公式法——公式法一定解得出。").addNotes("回收站①：四法答案一樣，只差快慢。保底句要全班能覆述。");

// =====================================================================
// 站② 判別式與根與係數
// =====================================================================
stationDivider("站②", "判別式與韋達定理", "不解方程，也能看出根的情況").addNotes("進入站②。賣點：不用解方程，就能知道有幾個根、根的和與積。");

// S15 問題引入
(function () {
  const s = newSlide(false);
  title(s, "不解方程，能知道有沒有解嗎？", "站② · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.6, y: 2.3, w: 10.1, h: 2.4, rectRadius: 0.18, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("可以！", { x: 1.6, y: 2.55, w: 10.1, h: 0.8, align: "center", valign: "middle", fontFace: F, fontSize: 36, bold: true, color: C.sageDeep });
  s.addText("只要看一個數的正負 —— 判別式 Δ", { x: 1.9, y: 3.5, w: 9.5, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 26, color: C.ink });
  footer(s, N, false);
  s.addNotes("製造好奇：先不解，只算一個數就知道結果。引出 Δ。");
})();

// S16 判別式 三情況
(function () {
  const s = newSlide(false);
  title(s, "判別式 Δ = b² − 4ac", "站② · 概念");
  const data = [
    ["Δ > 0", "兩個相異實根", "兩個不同的答案"],
    ["Δ = 0", "兩個相等實根", "重根，只有一個答案"],
    ["Δ < 0", "沒有實根", "解不出實數"],
  ];
  const x0 = 0.8, gap = 0.3, w = (11.7 - 2 * gap) / 3, yTop = 2.15, h = 3.6;
  data.forEach((d, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x, y: yTop, w, h: 1.0, rectRadius: 0.12, fill: { color: C.sageDeep }, line: { type: "none" } });
    s.addText(d[0], { x, y: yTop, w, h: 1.0, align: "center", valign: "middle", fontFace: MONO, fontSize: 30, bold: true, color: C.white });
    s.addText(d[1], { x: x + 0.2, y: yTop + 1.25, w: w - 0.4, h: 1.1, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
    s.addText(d[2], { x: x + 0.2, y: yTop + 2.5, w: w - 0.4, h: 0.9, align: "center", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
  });
  footer(s, N, false);
  s.addNotes("Δ 就像紅綠燈：正=兩根、零=重根、負=無實根。先算 Δ 再說。");
})();

// S17 案例頁 判根
(function () {
  const s = newSlide(false);
  title(s, "三題練判斷（不解方程）", "站② · 範例");
  const data = [
    ["x² − 3x + 1 = 0", "Δ = 9 − 4 = 5 > 0", "兩個相異實根"],
    ["4x² − 4x + 1 = 0", "Δ = 16 − 16 = 0", "兩個相等實根（重根）"],
    ["x² + x + 1 = 0", "Δ = 1 − 4 = −3 < 0", "沒有實根"],
  ];
  let y = 2.05;
  data.forEach((d) => {
    card(s, 0.8, y, 11.7, 1.35, C.white);
    s.addText(d[0], { x: 1.1, y: y, w: 4.0, h: 1.35, align: "left", valign: "middle", fontFace: MONO, fontSize: 23, bold: true, color: C.ink });
    s.addText(d[1], { x: 5.2, y: y, w: 3.9, h: 1.35, align: "left", valign: "middle", fontFace: MONO, fontSize: 22, color: C.sageDeep });
    s.addText(d[2], { x: 9.2, y: y, w: 3.2, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink });
    y += 1.5;
  });
  footer(s, N, false);
  s.addNotes("帶著全班一題一題算 Δ。強調步驟固定：找 a,b,c → 算 b²−4ac → 看正負。");
})();

// S18 韋達定理
(function () {
  const s = stepCardSlide("站② · 韋達定理", "根與係數的關係", "x² − 5x + 6 = 0", [
    [{ t: "兩根和 = " }, { n: "−b", d: "a" }, { t: " = −(−5) = 5" }],
    [{ t: "兩根積 = " }, { n: "c", d: "a" }, { t: " = 6" }],
    "驗證：兩根是 2、3 → 2+3=5、2×3=6 ✔",
  ], "不解方程也能求根的和與積。提醒符號：和是 −b/a，別漏負號。");
  s.addShape(p.ShapeType.roundRect, { x: 8.45, y: 1.75, w: 4.25, h: 0.9, rectRadius: 0.1, fill: { color: C.sageDeep }, line: { type: "none" } });
  fracRow(s, 8.7, 1.75, 0.9, [{ t: "和 = " }, { n: "−b", d: "a", color: C.white }, { t: "  積 = " }, { n: "c", d: "a", color: C.white }],
    { fontFace: F, fontSize: 16, fracFontSize: 15, bold: true, color: C.white, textPad: 0.06 });
})();

// S19 視覺鷹架頁 韋達模板（四格）
(function () {
  const s = newSlide(false);
  title(s, "韋達解題模板（照著填）", "站② · 鷹架");
  const cells = [
    ["① 問什麼", "求兩根的和／積"],
    ["② 已知", "找出 a、b、c"],
    ["③ 策略算式", [[{ t: "和 = " }, { n: "−b", d: "a" }], [{ t: "積 = " }, { n: "c", d: "a" }]]],
    ["④ 驗算", "代回檢查\n和、積對不對"],
  ];
  const x0 = 0.9, y0 = 2.05, w = 5.6, h = 2.1, gx = 0.4, gy = 0.35;
  cells.forEach((c, i) => {
    const x = x0 + (i % 2) * (w + gx);
    const y = y0 + Math.floor(i / 2) * (h + gy);
    card(s, x, y, w, h, C.white);
    s.addText(c[0], { x: x + 0.25, y: y + 0.18, w: w - 0.5, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
    if (Array.isArray(c[1])) {
      const lineH = 0.62;
      c[1].forEach((segs, li) => {
        fracRow(s, x + 0.25, y + 0.78 + li * lineH, lineH, segs, { fontFace: F, fontSize: 21, bold: false, color: C.ink, fracFontSize: 15 });
      });
    } else {
      s.addText(c[1], { x: x + 0.25, y: y + 0.78, w: w - 0.5, h: 1.15, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.3 });
    }
  });
  footer(s, N, false);
  s.addNotes("鷹架先撐後撤：前幾題照四格填，熟了就不用模板。");
})();

// S20 轉換點
breakSlide("下一頁換你做：先算 Δ 再說");

// S21 分層任務頁 站②
tieredTasks("站② · 分層練習",
  [
    ["1. 算 Δ 判斷根\nx²−6x+5 = 0", "2. 寫兩根和與積\nx²−7x+10 = 0"],
    ["3. k 為何值\nx²−4x+k 有重根？", "4. 一根是 2\nx²−5x+m，求 m 和另一根"],
    ["5. k 分三種情況\nx²−2x+k = 0", "6. 判對錯：任何二次\n方程都有兩實根？"],
  ],
  "解答核對｜A1: Δ=36−20=16>0，兩相異；A2: 和=7,積=10。 B3: Δ=16−4k=0→k=4；B4: m=6，另一根=3。 C5: Δ=4−4k → k<1兩相異 / k=1重根 / k>1無實根。 C6: 錯，Δ<0 無實根，如 x²+1=0。"
);

// S22 總結 站②
summarySlide("站② · 總結",
  "Δ 看幾個根，韋達看根的和與積。",
  "先算 Δ = b² − 4ac，看它是正、零，還是負。").addNotes("回收站②。保底：會算 Δ 並判正負，就達標。");

// =====================================================================
// 站③ 一元二次方程的應用
// =====================================================================
stationDivider("站③", "一元二次方程的應用", "文字題 → 方程 → 合理的答案").addNotes("進入站③。安撫：文字題不可怕，只要四步驟。");

// S24 問題引入
(function () {
  const s = newSlide(false);
  title(s, "文字題好難？其實只有四步", "站③ · 引入");
  s.addShape(p.ShapeType.roundRect, { x: 1.6, y: 2.4, w: 10.1, h: 2.2, rectRadius: 0.18, fill: { color: C.block }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
  s.addText("設 → 列 → 解 → 驗", { x: 1.6, y: 2.4, w: 10.1, h: 2.2, align: "center", valign: "middle", fontFace: F, fontSize: 40, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("先給整體框架，降低文字題焦慮。四步驟是全站的骨架。");
})();

// S25 步驟卡 四步驟
(function () {
  const s = newSlide(false);
  title(s, "解應用題的四步驟", "站③ · 步驟卡");
  const steps = [
    ["設未知數", "把要求的設成 x"],
    ["列方程", "照題意寫等式"],
    ["解方程", "用四種解法之一"],
    ["檢驗作答", "答案要合理"],
  ];
  let y = 1.9;
  steps.forEach((st, i) => {
    card(s, 0.8, y, 8.5, 0.98, C.white);
    stepCircle(s, 1.0, y + 0.24, i + 1, 0.5);
    s.addText(st[0], { x: 1.75, y: y, w: 2.6, h: 0.98, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    s.addText(st[1], { x: 4.4, y: y, w: 4.7, h: 0.98, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
    y += 1.12;
  });
  s.addShape(p.ShapeType.roundRect, { x: 9.6, y: 1.9, w: 3.0, h: 4.4, rectRadius: 0.14, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("⚠ 取捨提醒", { x: 9.8, y: 2.15, w: 2.6, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.white });
  s.addText("常有兩個解。\n\n長度、人數、時間\n都不能是負數，\n不合理就捨去。", { x: 9.8, y: 2.9, w: 2.6, h: 3.2, align: "left", valign: "top", fontFace: F, fontSize: 20, color: "E7F0EB", lineSpacingMultiple: 1.3 });
  footer(s, N, false);
  s.addNotes("四步驟是本站口訣。特別強調第四步：兩個解要按實際意義取捨。");
})();

// S26 CRA/鷹架 範例一 面積（含原生矩形圖）
(function () {
  const s = newSlide(false);
  title(s, "範例一：矩形面積問題", "站③ · 具體 → 抽象");
  // 左：矩形示意（原生圖）
  const rx = 1.55, ry = 2.4, rw = 4.5, rh = 2.6;
  s.addShape(p.ShapeType.rect, { x: rx, y: ry, w: rw, h: rh, fill: { color: C.block }, line: { color: C.sageDeep, width: 2 } });
  s.addText("面積 = 24", { x: rx, y: ry, w: rw, h: rh, align: "center", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  s.addText("寬 = x", { x: 0.15, y: ry, w: 1.3, h: rh, align: "center", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
  s.addText("長 = x + 2", { x: rx, y: ry + rh + 0.05, w: rw, h: 0.45, align: "center", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
  // 右：四步解
  const lines = [
    "① 設寬 x，長 x + 2",
    "② x(x + 2) = 24",
    "③ x² + 2x − 24 = 0",
    "    (x + 6)(x − 4) = 0 → x = 4",
    "④ 寬是長度取正 → 寬 4、長 6",
  ];
  let y = 2.35;
  lines.forEach((l) => {
    s.addText(l, { x: 6.4, y: y, w: 6.2, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
    y += 0.72;
  });
  hlBox(s, 6.4, 5.95, 6.2, 0.6);
  s.addText("x = −6 不合（長度不能是負）", { x: 6.5, y: 5.95, w: 6.0, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("先看圖（具體），再列式（抽象）。強調 x=−6 為何捨去，扣回第四步。");
})();

// S27 鷹架 範例二 變化率
(function () {
  const s = newSlide(false);
  title(s, "範例二：連續降價問題", "站③ · 變化率模板");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.8, w: 11.7, h: 0.95, rectRadius: 0.1, fill: { color: C.block }, line: { type: "none" } });
  s.addText("原價 100 元，連續兩次降價後變 81 元，求平均每次降價率。", { x: 1.1, y: 1.8, w: 11.1, h: 0.95, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.ink });
  const lines = [
    "① 設每次降價率 x",
    "② 100 (1 − x)² = 81",
    "③ (1 − x)² = 0.81 → 1 − x = 0.9",
    "④ x = 0.1 = 10%",
  ];
  let y = 3.05;
  lines.forEach((l) => {
    stepCircle(s, 0.9, y + 0.05, l.substring(1, 2) === " " ? l.charCodeAt(0) - 9311 : 0, 0.5);
    s.addText(l.substring(2), { x: 1.6, y: y, w: 10.8, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 23, color: C.ink });
    y += 0.82;
  });
  footer(s, N, false);
  s.addNotes("增長/降價率題型固定：起始×(1±x)^次數 = 結果。套模板即可。");
})();

// S28 轉換點
breakSlide("下一頁換你做：先寫「設 x」");

// S29 分層任務頁 站③
tieredTasks("站③ · 分層練習",
  [
    ["1. 兩連續正整數\n積是 56，求兩數", "2. 產量 100→144\n求平均年增長率"],
    ["3. 矩形長比寬多 7\n面積 60，求長寬", "4. 靠牆籬笆 32 米\n面積 120，求鄰邊"],
    ["5. 傳染病兩輪 121 人\n求每輪傳染 x 人", "6. 找錯：連續偶數積 48\n列 x(x+1)=48 錯在哪？"],
  ],
  "解答核對｜A1: x²+x−56=0→x=7，兩數 7、8；A2: (1+x)²=1.44→x=20%。 B3: x²+7x−60=0→寬5長12；B4: x(32−2x)=120→x=6 或 10。 C5: (1+x)²=121→x=10；C6: 偶數差 2，應列 x(x+2)=48→x=6，兩偶數 6、8。"
);

// S30 總結 站③
summarySlide("站③ · 總結",
  "應用題：設、列、解、驗四步，答案要合理。",
  "先寫「設 x」，再照範例把題意列成方程。").addNotes("回收站③。保底：能寫出「設 x」並列出方程，就達標。");

// =====================================================================
// 收尾
// =====================================================================
// S31 三站總複習
(function () {
  const s = newSlide(false);
  title(s, "三站帶走話，一次回顧");
  const data = [
    ["站①", "四種解法都通；先看樣子再選方法。"],
    ["站②", "Δ 看幾個根，韋達看根的和與積。"],
    ["站③", "設、列、解、驗四步，答案要合理。"],
  ];
  let y = 1.95;
  data.forEach((d) => {
    card(s, 0.7, y, 11.9, 1.35, C.white);
    stationBadge(s, d[0], 0.95, y + 0.36);
    s.addText(d[1], { x: 2.9, y: y, w: 9.4, h: 1.35, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
    y += 1.55;
  });
  footer(s, N, false);
  s.addNotes("整體回收。可請學生每站講一句自己的話覆述。");
})();

// S32 結語（asset-based）
(function () {
  const s = newSlide(true);
  s.addText("你已經走完三站！", { x: 0.9, y: 2.5, w: 11.6, h: 1.1, align: "left", valign: "middle", fontFace: F, fontSize: 46, bold: true, color: C.white });
  s.addText("一元二次方程，你做得到。", { x: 0.9, y: 3.75, w: 11.6, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 30, color: "CFE0D8" });
  s.addText("下次遇到二次方程，記得先問：它長成什麼樣子？該用哪一種方法？", { x: 0.9, y: 4.8, w: 11.6, h: 0.7, align: "left", valign: "middle", fontFace: F, fontSize: 20, italic: true, color: "9FB8AE" });
  s.addNotes("正向收束，asset-based。肯定努力與策略，不用「終於」「總算」等字眼。");
})();

// S33 教師備註頁
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
    "◆ 手順卡①–④：措辭與講義逐字同步",
    "◆ 視覺鷹架：韋達 / 應用四步模板",
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
p.writeFile({ fileName: "簡報_一元二次方程_概念到應用_融合抽離版.pptx" }).then((fn) => {
  console.log("WROTE " + fn + "  slides=" + N);
}).catch((e) => { console.error("ERR", e); process.exit(1); });
