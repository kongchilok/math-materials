// exp_draw.js — 高一單元三（指數與對數）專用示意圖層
// 只放「指對數主題」嘅圖：指對互換三數關係／根式↔分數指數對應／f 同 f⁻¹ 互相撤銷。
// 坐標系（axes）同數線（numberLine）單元二已經有，直接借嚟用，唔好重複實作。
// 全部原生 PptxGenJS 圖形，唔使外部 PNG。
const KIT = require('../../../01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js');
const FN = require('../../../02_函數的概念與性質/教學簡報/_scripts/fn_draw.js');
const { C, F, rt, seg, drawEq } = KIT;

// 指數式 ↔ 對數式：同樣三個數，換個位擺。成個單元最關鍵嘅一張圖。
// 唔用箭嘴指住式入面嘅字（對唔準），改為兩張式卡 + 底下逐個數講佢喺兩邊做乜。
function expLogSwap({ base = '2', exp = '3', val = '8', caption } = {}) {
  return (s, x, y, w, h) => {
    const ch = caption ? h * 0.86 : h;
    const gap = 0.55, cw = (w - gap) / 2, cardH = ch * 0.44, cy = y;
    const card = (cx, tag, eq) => {
      s.addShape('roundRect', { x: cx, y: cy, w: cw, h: cardH, rectRadius: 0.08,
        fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1 } });
      s.addText(tag, { x: cx, y: cy + 0.07, w: cw, h: 0.3, fontFace: F, fontSize: 16,
        bold: true, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
      s.addText(rt(eq, { bold: true, color: C.HEAD }), { x: cx, y: cy + 0.36, w: cw, h: cardH - 0.44,
        fontFace: F, fontSize: 32, align: 'center', valign: 'middle', margin: 0 });
    };
    card(x, '指數式', `${base}^{${exp}} = ${val}`);
    card(x + cw + gap, '對數式', `log_{${base}}${val} = ${exp}`);
    s.addText('⟷', { x: x + cw, y: cy, w: gap, h: cardH, fontFace: F, fontSize: 26,
      bold: true, color: C.ACCENT, align: 'center', valign: 'middle', margin: 0 });

    // 底下：同一個數，喺兩邊分別叫咩、做乜
    const roles = [
      [base, '底數', '兩邊都喺底，由頭到尾唔郁'],
      [exp, '指數', '左邊係「次方」，右邊變咗「答案」'],
      [val, '真數', '左邊係「結果」，右邊入咗 log 括號'],
    ];
    const ry = cy + cardH + 0.22, rh = (ch - cardH - 0.28) / 3;
    roles.forEach(([num, name, desc], i) => {
      const yy = ry + i * rh;
      s.addShape('ellipse', { x: x + 0.05, y: yy + (rh - 0.42) / 2, w: 0.42, h: 0.42,
        fill: { color: C.ACCENT } });
      s.addText(num, { x: x + 0.05, y: yy + (rh - 0.42) / 2, w: 0.42, h: 0.42, fontFace: F,
        fontSize: 18, bold: true, color: C.WHITE, align: 'center', valign: 'middle', margin: 0 });
      s.addText([...rt(name + '　', { bold: true, color: C.HEAD, fontSize: 18 }),
                 ...rt(desc, { color: C.MUTED2, fontSize: 16 })],
        { x: x + 0.60, y: yy, w: w - 0.65, h: rh, fontFace: F, align: 'left', valign: 'middle', margin: 0 });
    });
    if (caption) s.addText(rt(caption, { color: C.MUTED2 }), { x, y: y + ch + 0.04, w, h: 0.36,
      fontFace: F, fontSize: 17, align: 'center', valign: 'middle', margin: 0 });
  };
}

// 根式 ↔ 分數指數冪：根指數落分母、次方上分子。
// 2026-08-08 起改用 soil_kit.js 嘅 drawEq 通用 sqrt(deg)／exp 節點畫（真根號、
// 真分數線），取代舊版嘅手砌一次性寫法。
function rootPower({ a = 'a', root = '3', pow = '2', caption } = {}) {
  return (s, x, y, w, h) => {
    const ch = caption ? h * 0.80 : h;
    const cy = y + ch * 0.34;

    drawEq([
      { sqrt: { base: a, exp: pow }, deg: root },
      ' ＝ ',
      { base: a, exp: { n: pow, d: root } },
    ], { size: 40, color: C.HEAD })(s, x, cy - 0.5, w, 1.0);

    // 底下兩張對應卡
    const ny = y + ch * 0.66, nh = ch * 0.30, ngap = 0.35, nw = (w - ngap) / 2;
    [[`根指數 ${root}`, '落去分母'], [`次方 ${pow}`, '上去分子']].forEach(([t1, t2], i) => {
      const nx = x + i * (nw + ngap);
      s.addShape('roundRect', { x: nx, y: ny, w: nw, h: nh, rectRadius: 0.08,
        fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1 } });
      s.addText([...rt(t1 + '　→　', { bold: true, color: C.HEAD, fontSize: 19 }),
                 ...rt(t2, { bold: true, color: C.ACCENT, fontSize: 19 })],
        { x: nx + 0.1, y: ny, w: nw - 0.2, h: nh, fontFace: F, align: 'center', valign: 'middle', margin: 0 });
    });
    if (caption) s.addText(rt(caption, { color: C.MUTED2 }), { x, y: y + ch + 0.04, w, h: 0.36,
      fontFace: F, fontSize: 17, align: 'center', valign: 'middle', margin: 0 });
  };
}

// f 同 f⁻¹ 互相撤銷：x →[f]→ y →[f⁻¹]→ 返返原本嘅 x
function undoChain({ inLabel = 'x', mid = 'y', outLabel = '返返 x',
                     box1 = 'f', box2 = 'f^{-1}', caption } = {}) {
  return (s, x, y, w, h) => {
    const ch = caption ? h * 0.78 : h;
    const cy = y + ch / 2;
    const tW = w * 0.155, boxW = w * 0.135, aL = w * 0.048;
    const boxH = Math.min(ch * 0.40, 1.05);
    let cx = x + (w - (3 * tW + 2 * boxW + 4 * aL)) / 2;
    const txt = (t) => {
      s.addText(rt(t, { bold: true, color: C.INK }), { x: cx, y: cy - 0.3, w: tW, h: 0.6,
        fontFace: F, fontSize: 22, align: 'center', valign: 'middle', margin: 0 });
      cx += tW;
    };
    const arw = () => { seg(s, cx + 0.04, cy, cx + aL - 0.04, cy, { color: C.ACCENT, width: 2 }); cx += aL; };
    const box = (t) => {
      s.addShape('roundRect', { x: cx, y: cy - boxH / 2, w: boxW, h: boxH, rectRadius: 0.1,
        fill: { color: C.ACCENT }, line: { type: 'none' } });
      s.addText(rt(t, { bold: true, color: C.WHITE }), { x: cx, y: cy - boxH / 2, w: boxW, h: boxH,
        fontFace: F, fontSize: 26, align: 'center', valign: 'middle', margin: 0 });
      cx += boxW;
    };
    txt(inLabel); arw(); box(box1); arw(); txt(mid); arw(); box(box2); arw(); txt(outLabel);
    s.addText('做一次', { x: x + w * 0.14, y: cy + boxH / 2 + 0.10, w: w * 0.34, h: 0.32,
      fontFace: F, fontSize: 16, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
    s.addText('撤銷返', { x: x + w * 0.52, y: cy + boxH / 2 + 0.10, w: w * 0.34, h: 0.32,
      fontFace: F, fontSize: 16, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
    if (caption) s.addText(rt(caption, { color: C.MUTED2 }), { x, y: y + ch + 0.04, w, h: 0.4,
      fontFace: F, fontSize: 17, align: 'center', valign: 'middle', margin: 0 });
  };
}

module.exports = { expLogSwap, rootPower, undoChain, axes: FN.axes, numberLine: FN.numberLine, KIT };
