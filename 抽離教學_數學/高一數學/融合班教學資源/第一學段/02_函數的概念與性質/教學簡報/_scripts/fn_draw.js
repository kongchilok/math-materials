// fn_draw.js — 高一單元二（函數）專用示意圖層
// 只放「函數主題」嘅圖：坐標系／曲線／數線／分段圖。
// 通用嘢（seg、drawMapping、drawMachine、Venn…）一律留喺共用 soil_kit.js，唔好喺度重複。
// 全部原生 PptxGenJS 圖形：曲線用短線段串（30–40 段已夠滑），唔使外部 PNG／Chrome。
const KIT = require('../../../01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js');
const { C, F, seg } = KIT;

// 坐標系。opts:
//   xr:[a,b] yr:[a,b]  數學範圍
//   curves: [{ f, from, to, dash, width, color, open:[起,終] 空心點 }]
//   pts:    [{ x, y, label, open, color }]
//   segs:   [{ x1,y1,x2,y2, dash, head }]   數學座標的直線／虛線
//   rects:  [{ x1,y1,x2,y2, label }]        數學座標的填色矩形（畫喺曲線之前，唔會遮住線）
//   labels: [{ x, y, text, size, color }]
//   xticks / yticks: [數值]
function axes({ xr = [-4, 4], yr = [-3, 4], curves = [], pts = [], segs = [], rects = [], labels = [],
                xticks = [], yticks = [], xlab = 'x', ylab = 'y' } = {}) {
  return (s, bx, by, bw, bh) => {
    const [x0, x1] = xr, [y0, y1] = yr;
    const u = Math.min(bw / (x1 - x0), bh / (y1 - y0));
    const MX = (m) => bx + bw / 2 + (m - (x0 + x1) / 2) * u;
    const MY = (m) => by + bh / 2 - (m - (y0 + y1) / 2) * u;
    const L = (a, b, c, d, o) => seg(s, MX(a), MY(b), MX(c), MY(d), { head: false, ...o });

    // 軸（箭嘴向正方向）
    seg(s, MX(x0), MY(0), MX(x1), MY(0), { color: C.INK, width: 1.5 });
    seg(s, MX(0), MY(y0), MX(0), MY(y1), { color: C.INK, width: 1.5 });
    s.addText(xlab, { x: MX(x1) - 0.30, y: MY(0) + 0.06, w: 0.4, h: 0.3, fontFace: F, fontSize: 14,
      italic: false, color: C.INK, align: 'center', valign: 'middle', margin: 0 });
    s.addText(ylab, { x: MX(0) + 0.10, y: MY(y1) - 0.04, w: 0.4, h: 0.3, fontFace: F, fontSize: 14,
      color: C.INK, align: 'left', valign: 'middle', margin: 0 });
    s.addText('O', { x: MX(0) - 0.36, y: MY(0) + 0.04, w: 0.3, h: 0.28, fontFace: F, fontSize: 13,
      color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });

    // 刻度
    xticks.forEach((t) => {
      L(t, -0.12, t, 0.12, { color: C.INK, width: 1.2 });
      s.addText(String(t).replace('-', '−'), { x: MX(t) - 0.25, y: MY(0) + 0.08, w: 0.5, h: 0.26, fontFace: F,
        fontSize: 13, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
    });
    yticks.forEach((t) => {
      L(-0.12, t, 0.12, t, { color: C.INK, width: 1.2 });
      s.addText(String(t).replace('-', '−'), { x: MX(0) - 0.55, y: MY(t) - 0.13, w: 0.42, h: 0.26, fontFace: F,
        fontSize: 13, color: C.MUTED2, align: 'right', valign: 'middle', margin: 0 });
    });

    // 矩形（半透明填色）：先畫，等曲線／點／刻度壓喺上面
    rects.forEach((r) => {
      const px = Math.min(MX(r.x1), MX(r.x2)), py = Math.min(MY(r.y1), MY(r.y2));
      s.addShape('rect', { x: px, y: py,
        w: Math.abs(MX(r.x2) - MX(r.x1)), h: Math.abs(MY(r.y2) - MY(r.y1)),
        fill: { color: r.color || C.ACCENT, transparency: r.transparency === undefined ? 62 : r.transparency },
        line: { color: r.color || C.ACCENT, width: 1.5 } });
      if (r.label) s.addText(r.label, {
        x: (MX(r.x1) + MX(r.x2)) / 2 - 0.7, y: (MY(r.y1) + MY(r.y2)) / 2 - 0.16,
        w: 1.4, h: 0.32, fontFace: F, fontSize: r.labelSize || 15, bold: true, color: C.HEAD,
        align: 'center', valign: 'middle', margin: 0 });
    });

    segs.forEach((g) => L(g.x1, g.y1, g.x2, g.y2,
      { dash: g.dash, color: g.color || C.MUTED2, width: g.width || 1.3, head: g.head }));

    // 曲線：切成 N 段短線
    curves.forEach((cv) => {
      const N = cv.n || 34, a = cv.from, b = cv.to, col = cv.color || C.ACCENT;
      let prev = null;
      for (let i = 0; i <= N; i++) {
        const mx = a + (b - a) * i / N;
        let my;
        try { my = cv.f(mx); } catch (e) { my = NaN; }
        const ok = Number.isFinite(my) && my >= y0 - 0.01 && my <= y1 + 0.01;
        if (prev && ok) L(prev[0], prev[1], mx, my, { color: col, width: cv.width || 2.4, dash: cv.dash });
        prev = ok ? [mx, my] : null;
      }
      if (cv.label) {
        // 標籤要離開條線夠遠，否則會壓住曲線；要精準擺位就改用 labels:[{x,y,text}]
        const lx = cv.labelAt !== undefined ? cv.labelAt : b;
        s.addText(cv.label, { x: MX(lx) - 0.55, y: MY(cv.f(lx)) - 0.62, w: 1.1, h: 0.3, fontFace: F,
          fontSize: 14, bold: true, color: col, align: 'center', valign: 'middle', margin: 0 });
      }
    });

    // 點：實心●＝取得到，空心○＝取唔到
    pts.forEach((pt) => {
      const d = 0.16, col = pt.color || C.HEAD;
      s.addShape('ellipse', { x: MX(pt.x) - d / 2, y: MY(pt.y) - d / 2, w: d, h: d,
        fill: { color: pt.open ? 'FFFFFF' : col }, line: { color: col, width: 1.6 } });
      if (pt.label) s.addText(pt.label, { x: MX(pt.x) - 0.6, y: MY(pt.y) - 0.52, w: 1.2, h: 0.3,
        fontFace: F, fontSize: 13, bold: true, color: C.INK, align: 'center', valign: 'middle', margin: 0 });
    });

    labels.forEach((lb) => s.addText(lb.text, { x: MX(lb.x) - 0.8, y: MY(lb.y) - 0.17, w: 1.6, h: 0.34,
      fontFace: F, fontSize: lb.size || 15, bold: true, color: lb.color || C.HEAD,
      align: 'center', valign: 'middle', margin: 0 }));
  };
}

// 數線（教區間：實心●＝端點取得到，空心○＝取唔到）
// marks: [{ x, open, label }]   band: { from, to }（粗線段＝區間範圍；±Infinity 可用）
function numberLine({ from = -6, to = 6, ticks = [], marks = [], band, caption } = {}) {
  return (s, bx, by, bw, bh) => {
    const ch = caption ? bh * 0.72 : bh;
    const cy = by + ch / 2;
    const pad = 0.35, span = bw - 2 * pad;
    const P = (m) => bx + pad + (Math.max(from, Math.min(to, m)) - from) / (to - from) * span;
    if (band) {
      const a = Number.isFinite(band.from) ? band.from : from;
      const b = Number.isFinite(band.to) ? band.to : to;
      seg(s, P(a), cy, P(b), cy, { color: C.ACCENT, width: 6, head: false });
    }
    seg(s, bx + 0.1, cy, bx + bw - 0.1, cy, { color: C.INK, width: 1.5 });
    ticks.forEach((t) => {
      seg(s, P(t), cy - 0.1, P(t), cy + 0.1, { color: C.INK, width: 1.2, head: false });
      s.addText(String(t).replace('-', '−'), { x: P(t) - 0.3, y: cy + 0.14, w: 0.6, h: 0.28, fontFace: F, fontSize: 14,
        color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
    });
    marks.forEach((mk) => {
      const d = 0.2;
      s.addShape('ellipse', { x: P(mk.x) - d / 2, y: cy - d / 2, w: d, h: d,
        fill: { color: mk.open ? 'FFFFFF' : C.HEAD }, line: { color: C.HEAD, width: 2 } });
      if (mk.label) s.addText(mk.label, { x: P(mk.x) - 0.5, y: cy - 0.62, w: 1.0, h: 0.32,
        fontFace: F, fontSize: 15, bold: true, color: C.INK, align: 'center', valign: 'middle', margin: 0 });
    });
    if (caption) s.addText(caption, { x: bx, y: by + ch + 0.02, w: bw, h: 0.4, fontFace: F,
      fontSize: 17, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
  };
}

// 兩台機器串聯（複合函數）：x → [g] → g(x) → [f] → f(g(x))
function machineChain({ inLabel = 'x', inner = 'g', midLabel = 'g(x)',
                        outer = 'f', outLabel = 'f(g(x))', caption } = {}) {
  return (s, bx, by, bw, bh) => {
    const ch = caption ? bh * 0.78 : bh;
    const cy = by + ch / 2;
    const tW = bw * 0.155, boxW = bw * 0.115, aL = bw * 0.05;
    const boxH = Math.min(ch * 0.42, 1.0);
    let cx = bx + (bw - (3 * tW + 2 * boxW + 4 * aL)) / 2;
    const txt = (t, w, big) => {
      s.addText(t, { x: cx, y: cy - 0.3, w, h: 0.6, fontFace: F, fontSize: big ? 22 : 19,
        bold: true, color: C.INK, align: 'center', valign: 'middle', margin: 0 });
      cx += w;
    };
    const arw = () => { seg(s, cx + 0.04, cy, cx + aL - 0.04, cy, { color: C.ACCENT, width: 2 }); cx += aL; };
    const box = (t) => {
      s.addShape('roundRect', { x: cx, y: cy - boxH / 2, w: boxW, h: boxH, rectRadius: 0.1,
        fill: { color: C.ACCENT }, line: { type: 'none' } });
      s.addText(t, { x: cx, y: cy - boxH / 2, w: boxW, h: boxH, fontFace: F, fontSize: 28,
        bold: true, color: C.WHITE, align: 'center', valign: 'middle', margin: 0 });
      cx += boxW;
    };
    txt(inLabel, tW, true); arw(); box(inner); arw();
    txt(midLabel, tW, true); arw(); box(outer); arw();
    txt(outLabel, tW, true);
    // 內外層標示：擺喺盒下面，唔好貼住箭嘴
    s.addText('內層', { x: bx, y: cy + boxH / 2 + 0.08, w: bw * 0.52, h: 0.32, fontFace: F,
      fontSize: 15, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
    s.addText('外層', { x: bx + bw * 0.48, y: cy + boxH / 2 + 0.08, w: bw * 0.52, h: 0.32, fontFace: F,
      fontSize: 15, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
    if (caption) s.addText(caption, { x: bx, y: by + ch + 0.02, w: bw, h: 0.4, fontFace: F,
      fontSize: 17, color: C.MUTED2, align: 'center', valign: 'middle', margin: 0 });
  };
}

module.exports = { axes, numberLine, machineChain, KIT };
