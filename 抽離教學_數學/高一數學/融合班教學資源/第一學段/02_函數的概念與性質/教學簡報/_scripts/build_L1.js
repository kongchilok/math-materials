// 融合抽離小組 SOIL 教學簡報：高一數學．單元二 第 1 節「函數的概念」
// 生成 .pptx（PptxGenJS）。硬規則：微軟正黑體、內文≥20pt、標題≥32pt、
// 淺色非純白底、星星分層、色盲安全、Sage Calm 低刺激配色。
// 版型骨架沿用 初三\簡報_二次函數05-06\build_deck.js（同一套 house style）。
// 所有示意圖（機器圖、對應箭頭圖）皆用 PptxGenJS 原生圖形繪製，不外掛圖片。
const pptxgen = require("pptxgenjs");
const { drawEq } = require("../../../01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
p.author = "高一數學抽離小組";
p.title = "函數的概念（融合抽離版）";

// ---- 配色 (Sage Calm 低刺激) ----
const C = {
  bgLight: "EDF3F0", bgDark: "2E4A43", ink: "233A34", soft: "5C6F68",
  sage: "6FA48C", sageDeep: "4E8770", slate: "50808E", block: "DCEAE3",
  block2: "CFE0D8", cardLine: "B9CFC5", white: "FFFFFF",
};
const F = "Microsoft JhengHei";
const MONO = "Consolas";

// ---- 共用小工具 ----
function sh() { return { type: "outer", color: "AEBEB6", blur: 7, offset: 2, angle: 90, opacity: 0.45 }; }
function bg(s, dark) { s.background = { color: dark ? C.bgDark : C.bgLight }; }
function footer(s, n, dark) {
  s.addText("高一數學 · 函數的概念（抽離小組·融合版）", {
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
function card(s, x, y, w, h, fill) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.12, fill: { color: fill || C.white }, line: { color: C.cardLine, width: 1 }, shadow: sh() });
}
function hlBox(s, x, y, w, h, fill) {
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: fill || C.block }, line: { type: "none" } });
}
// 由 (x1,y1) 畫線／箭嘴到 (x2,y2)；pptxgenjs 只吃正寬高，向上要用 flipV
function arrow(s, x1, y1, x2, y2, opt) {
  const o = opt || {};
  const props = {
    x: Math.min(x1, x2), y: Math.min(y1, y2),
    w: Math.abs(x2 - x1), h: Math.abs(y2 - y1),
    line: { color: o.color || C.sageDeep, width: o.width || 2, endArrowType: o.head === false ? "none" : "triangle" },
  };
  if ((x2 - x1) * (y2 - y1) < 0) props.flipV = true;
  s.addShape(p.ShapeType.line, props);
}
function dot(s, cx, cy, color) {
  const d = 0.17;
  s.addShape(p.ShapeType.ellipse, { x: cx - d / 2, y: cy - d / 2, w: d, h: d, fill: { color: color || C.sageDeep }, line: { type: "none" } });
}
// 對應關係箭頭圖：左集合每點射向右集合
function mapping(s, x, y, w, h, nL, nR, edges) {
  const ovW = 1.45, padY = 0.18;
  const lx = x + 0.35, rx = x + w - 0.35 - ovW;
  [lx, rx].forEach((ox) => {
    s.addShape(p.ShapeType.ellipse, { x: ox, y: y + padY, w: ovW, h: h - 2 * padY, fill: { type: "none" }, line: { color: C.cardLine, width: 1.5 } });
  });
  const cxL = lx + ovW / 2, cxR = rx + ovW / 2;
  const spanY = (i, n) => y + padY + (h - 2 * padY) * (i + 1) / (n + 1);
  for (let i = 0; i < nL.length; i++) {
    const cy = spanY(i, nL.length);
    dot(s, cxL, cy);
    s.addText(nL[i], { x: cxL - 0.75, y: cy - 0.19, w: 0.52, h: 0.38, align: "right", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink, margin: 0 });
  }
  for (let i = 0; i < nR.length; i++) {
    const cy = spanY(i, nR.length);
    dot(s, cxR, cy, C.slate);
    s.addText(nR[i], { x: cxR + 0.23, y: cy - 0.19, w: 0.52, h: 0.38, align: "left", valign: "middle", fontFace: F, fontSize: 20, bold: true, color: C.ink, margin: 0 });
  }
  edges.forEach(([a, b]) => {
    arrow(s, cxL + 0.12, spanY(a, nL.length), cxR - 0.14, spanY(b, nR.length), { width: 1.75 });
  });
}
// 「機器」示意：x → [ f ] → y
function machine(s, x, y, scale, dark) {
  const k = scale || 1;
  const boxW = 1.9 * k, boxH = 1.15 * k, cy = y + boxH / 2;
  const inkC = dark ? "E7F0EB" : C.ink;
  s.addText("x", { x: x, y: cy - 0.28 * k, w: 0.5 * k, h: 0.56 * k, align: "center", valign: "middle", fontFace: MONO, fontSize: 26 * k, bold: true, color: inkC, margin: 0 });
  arrow(s, x + 0.52 * k, cy, x + 1.12 * k, cy, { color: dark ? C.sage : C.sageDeep });
  s.addShape(p.ShapeType.roundRect, { x: x + 1.2 * k, y: y, w: boxW, h: boxH, rectRadius: 0.12, fill: { color: dark ? C.sage : C.sageDeep }, line: { type: "none" } });
  s.addText("f", { x: x + 1.2 * k, y: y, w: boxW, h: boxH, align: "center", valign: "middle", fontFace: MONO, fontSize: 34 * k, bold: true, color: dark ? C.bgDark : C.white });
  arrow(s, x + 1.28 * k + boxW, cy, x + 1.88 * k + boxW, cy, { color: dark ? C.sage : C.sageDeep });
  s.addText("y", { x: x + 1.95 * k + boxW, y: cy - 0.28 * k, w: 0.5 * k, h: 0.56 * k, align: "center", valign: "middle", fontFace: MONO, fontSize: 26 * k, bold: true, color: inkC, margin: 0 });
}

let N = 0;
function newSlide(dark) { const s = p.addSlide(); bg(s, dark); N += 1; return s; }

// 分層任務頁（三欄同版面、星星標示、自選晉級）
function tieredTasks(kicker, head, cols, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  const tiers = [
    { t: "練習 A", star: "★☆☆" }, { t: "練習 B", star: "★★☆" }, { t: "練習 C", star: "★★★" },
  ];
  // 右邊界＝13.333；x0 + 總寬須 ≤ 12.83 才留得住 0.5" 邊界
  const x0 = 0.5, gap = 0.28, w = (12.33 - 2 * gap) / 3, yTop = 1.95, h = 4.35;
  tiers.forEach((ti, i) => {
    const x = x0 + i * (w + gap);
    card(s, x, yTop, w, h, C.white);
    s.addShape(p.ShapeType.roundRect, { x: x, y: yTop, w: w, h: 0.9, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(ti.t, { x: x + 0.2, y: yTop + 0.06, w: w - 0.4, h: 0.42, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(ti.star, { x: x + 0.2, y: yTop + 0.46, w: w - 0.4, h: 0.4, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    let ty = yTop + 1.08;
    cols[i].forEach((it) => {
      if (Array.isArray(it)) {
        // 逐行：字串（照舊）或 { eq:[...] }（drawEq 語法，原生分數／根號）
        // 行高要夠畀分數嘅分子／分母唔會疊落下一行（同 soil_kit.js colLines() 用同一條公式）
        const lh = (20 / 72) * 1.25 * 1.2;
        let cy = ty;
        it.forEach((ln) => {
          if (ln && typeof ln === "object" && ln.eq) {
            drawEq(ln.eq, { size: 20, color: C.ink, align: "left" })(s, x + 0.24, cy, w - 0.46, lh);
          } else if (ln !== "") {
            s.addText(ln, { x: x + 0.24, y: cy, w: w - 0.46, h: lh, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
          }
          cy += lh;
        });
        ty += Math.max(1.62, lh * it.length + 0.12);
      } else {
        s.addText(it, { x: x + 0.24, y: ty, w: w - 0.46, h: 1.5, align: "left", valign: "top", fontFace: F, fontSize: 20, color: C.ink, lineSpacingMultiple: 1.25 });
        ty += 1.62;
      }
    });
  });
  s.addText("做得起 A，就往 B、C 跳一層 ↗　三層都是同一個概念，只是鷹架不同", { x: 0.5, y: 6.5, w: 12.33, h: 0.45, fontFace: F, fontSize: 17, color: C.sageDeep, align: "left" });
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}
// 步驟卡頁（編號、一步一行、行距加大）
function stepCardSlide(kicker, head, lead, steps, tail, noteTxt) {
  const s = newSlide(false);
  title(s, head, kicker);
  let y0 = 1.95;
  if (lead) {
    hlBox(s, 0.8, y0, 11.7, 0.82);
    s.addText(lead, { x: 1.1, y: y0, w: 11.1, h: 0.82, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
    y0 += 1.05;
  }
  const bottom = tail ? 5.88 : 6.45;
  const rowH = (bottom - y0) / steps.length;
  let y = y0;
  steps.forEach((st, i) => {
    stepCircle(s, 0.85, y + (rowH - 0.5) / 2, i + 1, 0.5);
    s.addText(st, { x: 1.55, y: y, w: 10.9, h: rowH, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink, lineSpacingMultiple: 1.2 });
    y += rowH;
  });
  if (tail) {
    hlBox(s, 0.8, 6.12, 11.7, 0.72, C.block2);
    s.addText(tail, { x: 1.1, y: 6.12, w: 11.1, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
  }
  footer(s, N, false);
  s.addNotes(noteTxt);
  return s;
}

// ===================== 1. 封面頁 =====================
{
  const s = newSlide(true);
  s.addText("單元二．函數的概念與性質", { x: 0.9, y: 1.75, w: 8.4, h: 0.5, fontFace: F, fontSize: 20, bold: true, color: C.sage, align: "left" });
  s.addText("函數的概念", { x: 0.9, y: 2.3, w: 8.4, h: 1.1, fontFace: F, fontSize: 46, bold: true, color: C.white, align: "left" });
  s.addText("一個 x 放進去，只能有一個 y 出來", { x: 0.9, y: 3.5, w: 8.4, h: 0.6, fontFace: F, fontSize: 24, color: "C9DED5", align: "left" });
  s.addShape(p.ShapeType.roundRect, { x: 0.9, y: 4.55, w: 4.6, h: 0.72, rectRadius: 0.36, fill: { color: "35564E" }, line: { type: "none" } });
  s.addText("高一數學 · 抽離小組 · 40 分鐘", { x: 0.9, y: 4.55, w: 4.6, h: 0.72, align: "center", valign: "middle", fontFace: F, fontSize: 18, color: "C9DED5" });
  s.addText("第 1 節 / 全 10 節", { x: 5.75, y: 4.55, w: 3.2, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 18, color: "9FB8AE" });
  machine(s, 8.95, 2.85, 0.85, true);
  footer(s, N, true);
  s.addNotes("開場：不講定義，先講一個生活情境。整節課的主軸就是封面那句話。");
}

// ===================== 2. 流程預告頁 =====================
{
  const s = newSlide(false);
  title(s, "今日課堂流程", "流程預告");
  const rows = [
    ["快遞收費", "一個包裹重量，收多少錢？"],
    ["認識函數", "一個 x，只配一個 y"],
    ["三要素", "定義域、對應關係、值域"],
    ["分層練習", "A / B / C 三層，自己選"],
  ];
  let y = 2.05;
  rows.forEach((r, i) => {
    card(s, 0.8, y, 11.7, 0.98, C.white);
    stepCircle(s, 1.05, y + 0.24, i + 1, 0.5);
    s.addText(r[0], { x: 1.78, y: y, w: 2.6, h: 0.98, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.sageDeep });
    s.addText(r[1], { x: 4.45, y: y, w: 7.8, h: 0.98, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    y += 1.13;
  });
  hlBox(s, 0.8, 6.62, 11.7, 0.32, C.block);
  s.addText("中間會停兩次，一起做練習。", { x: 1.1, y: 6.55, w: 11.1, h: 0.45, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.ink });
  footer(s, N, false);
  s.addNotes("ASD 可預測性：逐項唸一次，告訴學生會停兩次做練習。這頁課末回來對照，確認四件事都做完。");
}

// ===================== 3. 問題引入頁（保底成功經驗・轉換點：全體作答）=====================
{
  const s = newSlide(false);
  title(s, "包裹重 1.5 公斤，收多少錢？", "情境：快遞計費");
  card(s, 0.8, 1.95, 6.6, 3.55, C.white);
  s.addText("快遞收費表", { x: 1.1, y: 2.1, w: 6.0, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.sageDeep });
  const fee = [["0 < x ≤ 1", "15 元"], ["1 < x ≤ 3", "25 元"], ["x > 3", "另議，不在表內"]];
  let fy = 2.72;
  fee.forEach((r) => {
    hlBox(s, 1.1, fy, 6.0, 0.78, C.block);
    s.addText(r[0], { x: 1.35, y: fy, w: 2.8, h: 0.78, align: "left", valign: "middle", fontFace: MONO, fontSize: 24, bold: true, color: C.ink });
    s.addText(r[1], { x: 4.25, y: fy, w: 2.7, h: 0.78, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.ink });
    fy += 0.9;
  });
  card(s, 7.75, 1.95, 4.75, 3.55, C.block2);
  s.addText("1.5 公斤\n落在哪一格？", { x: 8.05, y: 2.25, w: 4.15, h: 1.5, align: "left", valign: "middle", fontFace: F, fontSize: 28, bold: true, color: C.ink, lineSpacingMultiple: 1.3 });
  s.addText("收費是 ______ 元", { x: 8.05, y: 4.0, w: 4.15, h: 1.2, align: "left", valign: "middle", fontFace: F, fontSize: 24, color: C.sageDeep });
  hlBox(s, 0.8, 5.85, 11.7, 0.85);
  s.addText("答案只有一個 —— 這一點很重要。", { x: 1.1, y: 5.85, w: 11.1, h: 0.85, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("轉換點 1（約第 4 分鐘）：全體舉手作答，人人做得起的入口題（保底成功經驗）。答案 25 元。追問一句：如果同一個 1.5 公斤，有人說 15 元有人說 25 元，收費表還有用嗎？帶出「唯一」。");
}

// ===================== 4. CRA 具體頁 =====================
{
  const s = newSlide(false);
  title(s, "按一個按鈕，出一罐飲料", "具體：自動販賣機");
  const items = [["按 A", "可樂"], ["按 B", "汽水"], ["按 C", "礦泉水"]];
  const w = 3.7, gap = 0.5;
  items.forEach((it, i) => {
    const x = 0.95 + i * (w + gap);
    card(s, x, 2.0, w, 2.55, C.white);
    s.addShape(p.ShapeType.roundRect, { x: x + 0.85, y: 2.25, w: 2.0, h: 0.75, rectRadius: 0.37, fill: { color: C.sageDeep }, line: { type: "none" } });
    s.addText(it[0], { x: x + 0.85, y: 2.25, w: 2.0, h: 0.75, align: "center", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.white });
    arrow(s, x + w / 2, 3.15, x + w / 2, 3.6);
    s.addText(it[1], { x: x + 0.3, y: 3.68, w: w - 0.6, h: 0.65, align: "center", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.ink });
  });
  hlBox(s, 0.95, 4.85, 11.45, 0.85);
  s.addText("按同一個按鈕，出來的永遠是同一樣東西。", { x: 1.25, y: 4.85, w: 10.9, h: 0.85, align: "left", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.ink });
  s.addText("意思是：同一個輸入，答案不會改變。", { x: 1.25, y: 5.95, w: 10.9, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("比喻必須解釋（ASD 按字面理解）：說完販賣機，立刻用下一行白話把比喻翻譯回數學意思，不要留給學生自己聯想。");
}

// ===================== 5. CRA 表徵頁（★關鍵投影片）=====================
{
  const s = newSlide(false);
  title(s, "一個 x，配到幾個 y？", "★ 表徵：對應關係圖");
  const w = 5.75, y0 = 1.95, h = 3.7;
  // 左：是函數
  card(s, 0.8, y0, w, h, C.white);
  s.addText("是函數", { x: 1.05, y: y0 + 0.12, w: w - 0.5, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.sageDeep });
  mapping(s, 1.35, y0 + 0.72, w - 1.1, h - 1.0, ["1", "2", "3"], ["a", "b"], [[0, 0], [1, 1], [2, 1]]);
  // 右：不是函數
  card(s, 6.95, y0, w, h, C.white);
  s.addText("不是函數", { x: 7.2, y: y0 + 0.12, w: w - 0.5, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.slate });
  mapping(s, 7.5, y0 + 0.72, w - 1.1, h - 1.0, ["1", "2"], ["a", "b", "c"], [[0, 0], [1, 1], [1, 2]]);
  hlBox(s, 0.8, 5.9, 11.7, 0.85);
  s.addText("分別在：右邊那個 2，配到了兩個答案。", { x: 1.1, y: 5.9, w: 11.1, h: 0.85, align: "left", valign: "middle", fontFace: F, fontSize: 25, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("關鍵投影片。用手指逐個點數：左邊每個點只射出一支箭；右邊的 2 射出兩支。讓學生自己數，不要直接講結論。");
}

// ===================== 6. 迷思澄清頁（轉換點：舉手作答）=====================
{
  const s = newSlide(false);
  title(s, "兩個 x 配同一個 y，可以嗎？", "迷思澄清");
  const w = 5.75, y0 = 1.95, h = 2.95;
  card(s, 0.8, y0, w, h, C.white);
  s.addText("不可以", { x: 1.05, y: y0 + 0.15, w: w - 0.5, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.slate });
  s.addText("一個 x  →  兩個 y", { x: 1.05, y: y0 + 0.9, w: w - 0.5, h: 0.9, align: "left", valign: "middle", fontFace: MONO, fontSize: 30, bold: true, color: C.ink });
  s.addText("一個輸入，出現兩個答案", { x: 1.05, y: y0 + 1.9, w: w - 0.5, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.soft });
  card(s, 6.95, y0, w, h, C.block);
  s.addText("可以", { x: 7.2, y: y0 + 0.15, w: w - 0.5, h: 0.5, align: "left", valign: "middle", fontFace: F, fontSize: 24, bold: true, color: C.sageDeep });
  s.addText("兩個 x  →  一個 y", { x: 7.2, y: y0 + 0.9, w: w - 0.5, h: 0.9, align: "left", valign: "middle", fontFace: MONO, fontSize: 30, bold: true, color: C.ink });
  s.addText("兩個輸入，答案剛好一樣", { x: 7.2, y: y0 + 1.9, w: w - 0.5, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: C.soft });
  hlBox(s, 0.8, 5.25, 11.7, 1.45, C.block2);
  s.addText("回到快遞表：1.5 公斤和 2.5 公斤都收 25 元，\n兩個重量配同一個價錢 —— 它仍然是函數。", { x: 1.1, y: 5.25, w: 11.1, h: 1.45, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink, lineSpacingMultiple: 1.35 });
  footer(s, N, false);
  s.addNotes("轉換點 2（約第 12 分鐘）：先舉手投票「可以／不可以」，再揭曉。這是本節最常見的誤解，一定要停下來處理。");
}

// ===================== 7. CRA 抽象頁 =====================
{
  const s = newSlide(false);
  title(s, "寫成數學記號", "抽象");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 1.9, w: 7.9, h: 1.35, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("y = f(x)　，　x ∈ A", { x: 0.8, y: 1.9, w: 7.9, h: 1.35, align: "center", valign: "middle", fontFace: MONO, fontSize: 38, bold: true, color: C.white });
  // 角落保留具體階段的視覺線索
  card(s, 9.05, 1.9, 3.45, 1.35, C.white);
  machine(s, 9.35, 2.16, 0.72, false);
  const parts = [
    ["x", "自變量", "放進去的那個"],
    ["f", "對應關係", "機器做的那件事"],
    ["y = f(x)", "函數值", "出來的那個"],
  ];
  const w = 3.7, gap = 0.5;
  parts.forEach((it, i) => {
    const x = 0.95 + i * (w + gap);
    card(s, x, 3.62, w, 2.05, C.white);
    s.addText(it[0], { x: x + 0.25, y: 3.78, w: w - 0.5, h: 0.62, align: "left", valign: "middle", fontFace: MONO, fontSize: 28, bold: true, color: C.sageDeep });
    s.addText(it[1], { x: x + 0.25, y: 4.42, w: w - 0.5, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.ink });
    s.addText(it[2], { x: x + 0.25, y: 4.98, w: w - 0.5, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 20, color: C.soft });
  });
  hlBox(s, 0.95, 5.92, 11.45, 0.78, C.block2);
  s.addText("f(x) 讀作「f 作用於 x」，不是 f 乘以 x。", { x: 1.25, y: 5.92, w: 10.9, h: 0.78, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("抽象頁保留右上角機器縮圖，作為前一階段的視覺線索。f(x) 被讀成「f 乘 x」是高頻錯誤，這裡明講一次。預告：再一頁就一起做練習。");
}

// ===================== 8. 步驟卡頁：判斷是不是函數 =====================
stepCardSlide(
  "步驟卡",
  "判斷「是不是函數」三步",
  "先看清楚：誰是 x（輸入），誰是 y（輸出）。",
  [
    "看定義域裡的每一個 x。",
    "數清楚：這個 x 配到幾個 y。",
    "每個 x 都剛好配 1 個 → 是函數。\n只要有一個 x 配到 2 個或以上 → 不是函數。",
  ],
  "下一頁：一起做練習一。",
  "步驟卡是過渡鷹架，前三節照著用，第四節起改成學生自己口述三步（fade out）。一次一個指令，唸完一步再唸下一步。"
);

// ===================== 9. 分層任務頁一（轉換點）=====================
tieredTasks(
  "練習一 · 自選星星",
  "是不是函數？",
  [
    ["① 每個學生 → 他的身高", "② 每個人 → 他的生日"],
    ["① y = 2x + 1（x ∈ R）", "② x：1、2、3\n　 y：5、5、7"],
    ["① 每個正數 →\n　 它的平方根", "　 這是不是函數？\n　 說明你的理由。"],
  ],
  "轉換點 3（約第 20 分鐘）：三層同時發，學生自選，不點名分派。C 是 low floor high ceiling 的天花板題——平方根有正負兩個值，所以不是函數；能講出這一點的學生，請他向全班說明。"
);

// ===================== 10. 三要素頁 =====================
{
  const s = newSlide(false);
  title(s, "函數的三要素", "結構");
  const parts = [
    ["定義域", "x 可以取的範圍", "0 < x ≤ 3（公斤）"],
    ["對應關係", "由 x 算出 y 的規則", "0<x≤1 收 15\n1<x≤3 收 25"],
    ["值域", "所有 y 合起來的集合", "{ 15 , 25 }"],
  ];
  const w = 3.7, gap = 0.5;
  parts.forEach((it, i) => {
    const x = 0.95 + i * (w + gap);
    card(s, x, 1.95, w, 3.5, C.white);
    s.addShape(p.ShapeType.roundRect, { x: x, y: 1.95, w: w, h: 0.85, rectRadius: 0.12, fill: { color: C.block2 }, line: { type: "none" } });
    s.addText(it[0], { x: x + 0.25, y: 1.95, w: w - 0.5, h: 0.85, align: "left", valign: "middle", fontFace: F, fontSize: 26, bold: true, color: C.ink });
    s.addText(it[1], { x: x + 0.25, y: 3.0, w: w - 0.5, h: 0.85, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.soft, lineSpacingMultiple: 1.25 });
    hlBox(s, x + 0.25, 4.0, w - 0.5, 1.25, C.block);
    s.addText(it[2], { x: x + 0.42, y: 4.0, w: w - 0.84, h: 1.25, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink, lineSpacingMultiple: 1.25 });
  });
  s.addText("灰底格 = 快遞計費那個函數的三要素", { x: 0.95, y: 5.55, w: 11.45, h: 0.45, fontFace: F, fontSize: 19, color: C.sageDeep, align: "left" });
  hlBox(s, 0.95, 6.05, 11.45, 0.72, C.block2);
  s.addText("值域是算出來的結果，不用另外去「規定」它。", { x: 1.25, y: 6.05, w: 10.9, h: 0.72, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("定義域／值域都叫「域」，是本節最容易混的一組詞。固定講法：定義域看 x，值域看 y。三欄位置固定，之後每節沿用同一版型。");
}

// ===================== 11. 視覺鷹架頁 =====================
{
  const s = newSlide(false);
  title(s, "四格填空：把三要素寫出來", "視覺鷹架（示範）");
  const cells = [
    ["是不是函數？", "是。每個重量只對應一個收費。"],
    ["定義域", "0 < x ≤ 3"],
    ["對應關係", "0<x≤1 收 15 元；1<x≤3 收 25 元"],
    ["值域", "{ 15 , 25 }"],
  ];
  const x0 = 0.9, y0 = 1.95, w = 5.6, h = 1.95, gx = 0.4, gy = 0.32;
  cells.forEach((c, i) => {
    const x = x0 + (i % 2) * (w + gx);
    const y = y0 + Math.floor(i / 2) * (h + gy);
    card(s, x, y, w, h, C.white);
    s.addText(c[0], { x: x + 0.25, y: y + 0.18, w: w - 0.5, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 23, bold: true, color: C.sageDeep });
    s.addText(c[1], { x: x + 0.25, y: y + 0.78, w: w - 0.5, h: 1.1, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.ink, lineSpacingMultiple: 1.25 });
  });
  hlBox(s, 0.9, 6.32, 11.7, 0.6, C.block2);
  s.addText("之後每一題，都用這四格寫。", { x: 1.2, y: 6.32, w: 11.1, h: 0.6, align: "left", valign: "middle", fontFace: F, fontSize: 21, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("示範 → 引導 → 學生做。這一頁老師先把四格唸一次（示範），練習二的 B 題用同一個四格帶著填（引導），功課才讓學生自己填（學生做）。");
}

// ===================== 12. 迷思澄清頁：同一函數 =====================
{
  const s = newSlide(false);
  title(s, "式子化簡後一樣，就是同一函數嗎？", "迷思澄清");
  const w = 5.75, y0 = 1.95, h = 2.6;
  card(s, 0.8, y0, w, h, C.white);
  s.addText("y = x", { x: 1.05, y: y0 + 0.3, w: w - 0.5, h: 0.95, align: "left", valign: "middle", fontFace: MONO, fontSize: 34, bold: true, color: C.ink });
  s.addText("x 可以是任何實數，\n包括 0。", { x: 1.05, y: y0 + 1.3, w: w - 0.5, h: 1.05, align: "left", valign: "top", fontFace: F, fontSize: 21, color: C.soft, lineSpacingMultiple: 1.3 });
  card(s, 6.95, y0, w, h, C.block);
  drawEq(["y = ", { n: "x²", d: "x" }], { size: 34, color: C.ink, align: "left" })(s, 7.2, y0 + 0.3, w - 0.5, 0.95);
  s.addText("分母不能是 0，\n所以 x 不可以是 0。", { x: 7.2, y: y0 + 1.3, w: w - 0.5, h: 1.05, align: "left", valign: "top", fontFace: F, fontSize: 21, bold: true, color: C.ink, lineSpacingMultiple: 1.3 });
  hlBox(s, 0.8, 4.9, 11.7, 0.95);
  s.addText("化簡後都是 y = x，但定義域不同 —— 不是同一函數。", { x: 1.1, y: 4.9, w: 11.1, h: 0.95, align: "left", valign: "middle", fontFace: F, fontSize: 25, bold: true, color: C.ink });
  s.addText("先看定義域，才看式子。式子是後看的。", { x: 1.1, y: 6.05, w: 11.1, h: 0.65, align: "left", valign: "middle", fontFace: F, fontSize: 22, color: C.sageDeep });
  footer(s, N, false);
  s.addNotes("學生最直覺的做法是先化簡再比。這裡把順序反過來：先比定義域。強調「x 不可以是 0」這一句要寫進答案，不能只在心裡想。");
}

// ===================== 13. 步驟卡頁：判斷同一函數 =====================
stepCardSlide(
  "步驟卡",
  "判斷「是不是同一函數」兩步",
  "兩個都要一樣，才算同一函數。",
  [
    "比定義域：兩個 x 的可取範圍一樣嗎？",
    "比對應關係：由 x 算出 y 的規則一樣嗎？",
  ],
  "下一頁：一起做練習二。",
  "只有兩步，刻意比上一張步驟卡短——讓學生感覺得到「這個比較簡單」。值域不用比：定義域和對應關係一樣，值域一定跟著一樣。"
);

// ===================== 14. 分層任務頁二（轉換點）=====================
tieredTasks(
  "練習二 · 自選星星",
  "三要素與同一函數",
  [
    ["① y = 2x，x ∈ {1, 2, 3}\n　 寫出定義域和值域。"],
    [["① y = x + 1", "　 與", { eq: ["　 y = ", { n: "x² − 1", d: "x − 1" }] }, "　 是同一函數嗎？"]],
    ["① 自己設計一個\n　「不是函數」的\n　 對應關係。", "② 說明為什麼不是。"],
  ],
  "轉換點 4（約第 32 分鐘）：B 題用第 11 頁的四格帶著填（引導階段）。C 題完成的學生請他把自己設計的例子畫成第 5 頁那種箭頭圖，貼上白板。"
);

// ===================== 15. 總結頁 =====================
{
  const s = newSlide(false);
  title(s, "帶走一句話", "總結");
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 2.0, w: 11.7, h: 1.7, rectRadius: 0.15, fill: { color: C.sageDeep }, line: { type: "none" }, shadow: sh() });
  s.addText("一個 x 放進去，只能有一個 y 出來。", { x: 1.2, y: 2.0, w: 10.9, h: 1.7, align: "left", valign: "middle", fontFace: F, fontSize: 32, bold: true, color: C.white });
  s.addShape(p.ShapeType.roundRect, { x: 0.8, y: 4.0, w: 11.7, h: 1.5, rectRadius: 0.15, fill: { color: C.block }, line: { color: C.cardLine, width: 1 } });
  s.addText([
    { text: "至少要記得：", options: { fontFace: F, fontSize: 22, bold: true, color: C.sageDeep } },
    { text: "問自己「這個 x 配到幾個 y？」剛好 1 個，就是函數。", options: { fontFace: F, fontSize: 23, color: C.ink } },
  ], { x: 1.2, y: 4.0, w: 10.9, h: 1.5, align: "left", valign: "middle" });
  hlBox(s, 0.8, 5.8, 11.7, 0.9, C.block2);
  s.addText("三要素：定義域看 x　·　對應關係看規則　·　值域看 y", { x: 1.2, y: 5.8, w: 11.1, h: 0.9, align: "left", valign: "middle", fontFace: F, fontSize: 22, bold: true, color: C.ink });
  footer(s, N, false);
  s.addNotes("請學生用自己的話講一次那句話再下課。回頭翻第 2 頁流程預告，逐項確認四件事都做完（ASD 收束）。");
}

// ===================== 16. 下一節預告頁 =====================
{
  const s = newSlide(true);
  s.addText("下一節", { x: 0.9, y: 1.95, w: 8.4, h: 0.5, fontFace: F, fontSize: 20, bold: true, color: C.sage, align: "left" });
  s.addText("區間記號與定義域", { x: 0.9, y: 2.5, w: 11.5, h: 1.0, fontFace: F, fontSize: 40, bold: true, color: C.white, align: "left" });
  const nx = [
    "用 [ ] 和 ( ) 把一段範圍寫得更短",
    "看到根號、看到分母，定義域怎麼求",
  ];
  let y = 3.9;
  nx.forEach((t, i) => {
    s.addShape(p.ShapeType.roundRect, { x: 0.9, y: y, w: 11.5, h: 0.95, rectRadius: 0.12, fill: { color: "35564E" }, line: { type: "none" } });
    stepCircle(s, 1.15, y + 0.23, i + 1, 0.5);
    s.addText(t, { x: 1.88, y: y, w: 10.2, h: 0.95, align: "left", valign: "middle", fontFace: F, fontSize: 23, color: "E7F0EB" });
    y += 1.12;
  });
  s.addText("今天那句話會一直用下去：一個 x，只配一個 y。", { x: 0.9, y: 6.25, w: 11.5, h: 0.55, align: "left", valign: "middle", fontFace: F, fontSize: 21, color: "9FB8AE" });
  footer(s, N, true);
  s.addNotes("下課前 1 分鐘播這頁。ASD 學生需要知道下一次上課會發生什麼。");
}

// ⚠ L1 未用共用 soil_kit.js（見同層 build_L2 起）。L2–L10 一律 require 01 單元的 soil_kit.js。
const out = require("path").join(__dirname, "..", "簡報_L1_函數的概念.pptx");
p.writeFile({ fileName: out }).then(() => console.log("OK ->", out, "| slides:", N));
