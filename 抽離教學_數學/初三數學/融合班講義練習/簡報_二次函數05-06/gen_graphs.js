// 產生二次函數拋物線圖 (Sage Calm 風格) → 輸出 SVG-in-HTML，交 Chrome 截 PNG。
// 解析幾何坐標圖 jh-math-geometry 不做，故自建 (CLAUDE.md §4 / 記憶：grid_svg+Chrome)。
const fs = require("fs");
const path = require("path");
const OUT = process.argv[2] || ".";

// Sage Calm 配色（與 build_deck.js 對齊）
const COL = {
  bg: "#FFFFFF",
  grid: "#D7E4DD",
  gridMajor: "#C2D6CC",
  axis: "#5C6F68",
  curve: "#4E8770",   // sageDeep
  curve2: "#50808E",  // slate（第二條曲線）
  dot: "#2E4A43",
  ink: "#233A34",
  soft: "#5C6F68",
  dash: "#9BB3A9",
};

// 生成一張拋物線圖的 SVG
// spec: {W,H, xmin,xmax,ymin,ymax, fns:[{f, color}], points:[{x,y,label,anchor}], axisSym, note}
function svg(spec) {
  const { W, H, xmin, xmax, ymin, ymax } = spec;
  const xStep = spec.xStep || 1, yStep = spec.yStep || 1;
  const ml = 46, mr = 26, mt = 22, mb = 40;
  const pw = W - ml - mr, ph = H - mt - mb;
  const X = (x) => ml + ((x - xmin) / (xmax - xmin)) * pw;
  const Y = (y) => mt + ((ymax - y) / (ymax - ymin)) * ph;
  const parts = [];
  parts.push(`<rect x="0" y="0" width="${W}" height="${H}" fill="${COL.bg}"/>`);

  // 網格線（依 step，降低視覺雜訊）
  for (let x = Math.ceil(xmin / xStep) * xStep; x <= xmax + 1e-9; x += xStep) {
    const major = Math.abs(x) < 1e-9;
    parts.push(`<line x1="${X(x)}" y1="${mt}" x2="${X(x)}" y2="${mt + ph}" stroke="${major ? COL.gridMajor : COL.grid}" stroke-width="${major ? 1.4 : 1}"/>`);
  }
  for (let y = Math.ceil(ymin / yStep) * yStep; y <= ymax + 1e-9; y += yStep) {
    const major = Math.abs(y) < 1e-9;
    parts.push(`<line x1="${ml}" y1="${Y(y)}" x2="${ml + pw}" y2="${Y(y)}" stroke="${major ? COL.gridMajor : COL.grid}" stroke-width="${major ? 1.4 : 1}"/>`);
  }

  // 對稱軸（虛線）
  if (spec.axisSym !== undefined) {
    parts.push(`<line x1="${X(spec.axisSym)}" y1="${mt}" x2="${X(spec.axisSym)}" y2="${mt + ph}" stroke="${COL.dash}" stroke-width="2" stroke-dasharray="6 5"/>`);
  }

  // 坐標軸 + 箭頭
  const y0 = Y(0), x0 = X(0);
  parts.push(`<line x1="${ml}" y1="${y0}" x2="${ml + pw}" y2="${y0}" stroke="${COL.axis}" stroke-width="2.2"/>`);
  parts.push(`<line x1="${x0}" y1="${mt + ph}" x2="${x0}" y2="${mt}" stroke="${COL.axis}" stroke-width="2.2"/>`);
  parts.push(`<polygon points="${ml + pw},${y0} ${ml + pw - 10},${y0 - 5} ${ml + pw - 10},${y0 + 5}" fill="${COL.axis}"/>`);
  parts.push(`<polygon points="${x0},${mt} ${x0 - 5},${mt + 10} ${x0 + 5},${mt + 10}" fill="${COL.axis}"/>`);
  parts.push(`<text x="${ml + pw - 4}" y="${y0 + 20}" font-size="18" fill="${COL.soft}" font-family="Microsoft JhengHei" font-style="italic" text-anchor="end">x</text>`);
  parts.push(`<text x="${x0 + 12}" y="${mt + 14}" font-size="18" fill="${COL.soft}" font-family="Microsoft JhengHei" font-style="italic">y</text>`);
  parts.push(`<text x="${x0 - 8}" y="${y0 + 18}" font-size="15" fill="${COL.soft}" font-family="Microsoft JhengHei" text-anchor="end">O</text>`);

  // x 軸刻度標籤（依 xStep；避開 0 與最邊兩格，免與軸字/邊緣相撞）
  for (let x = Math.ceil(xmin / xStep) * xStep; x <= xmax + 1e-9; x += xStep) {
    if (Math.abs(x) < 1e-9) continue;
    if (x <= xmin + 1e-9 || x >= xmax - 1e-9) continue;
    parts.push(`<text x="${X(x)}" y="${y0 + 20}" font-size="14" fill="${COL.soft}" font-family="Microsoft JhengHei" text-anchor="middle">${+x.toFixed(2)}</text>`);
  }

  // 曲線
  (spec.fns || []).forEach((fn) => {
    const pts = [];
    const steps = 400;
    for (let i = 0; i <= steps; i++) {
      const x = xmin + (i / steps) * (xmax - xmin);
      const y = fn.f(x);
      if (y < ymin - 1 || y > ymax + 1) { if (pts.length) pts.push("BREAK"); continue; }
      pts.push(`${X(x).toFixed(1)},${Y(y).toFixed(1)}`);
    }
    // 分段（避免超出範圍連線）
    let seg = [];
    const flush = () => { if (seg.length > 1) parts.push(`<polyline points="${seg.join(" ")}" fill="none" stroke="${fn.color || COL.curve}" stroke-width="4" stroke-linjoin="round" stroke-linecap="round"/>`); seg = []; };
    pts.forEach((p) => { if (p === "BREAK") flush(); else seg.push(p); });
    flush();
    if (fn.label) parts.push(`<text x="${X(fn.label.x)}" y="${Y(fn.label.y)}" font-size="17" font-weight="bold" fill="${fn.color || COL.curve}" font-family="Microsoft JhengHei" text-anchor="${fn.label.anchor || 'start'}">${fn.label.text}</text>`);
  });

  // 標示點
  (spec.points || []).forEach((pt) => {
    parts.push(`<circle cx="${X(pt.x)}" cy="${Y(pt.y)}" r="5.5" fill="${COL.dot}" stroke="#FFFFFF" stroke-width="2"/>`);
    if (pt.label) {
      const dx = pt.dx || 8, dy = pt.dy || -8;
      parts.push(`<text x="${X(pt.x) + dx}" y="${Y(pt.y) + dy}" font-size="15" font-weight="bold" fill="${COL.ink}" font-family="Microsoft JhengHei" text-anchor="${pt.anchor || 'start'}">${pt.label}</text>`);
    }
  });

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${parts.join("")}</svg>`;
}

function html(svgStr, W, H) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0;padding:0}html,body{width:${W}px;height:${H}px;overflow:hidden;background:#FFFFFF}</style></head><body>${svgStr}</body></html>`;
}

// ============ 定義每張圖 ============
const graphs = {
  // 站① 開口方向：y=x²（上） 與 y=−x²（下）
  p_updown: {
    W: 760, H: 640, xmin: -3, xmax: 3, ymin: -4.2, ymax: 4.2,
    fns: [
      { f: (x) => x * x, color: COL.curve, label: { x: 1.6, y: 3.2, text: "y = x²", anchor: "start" } },
      { f: (x) => -x * x, color: COL.curve2, label: { x: 1.6, y: -3.2, text: "y = −x²", anchor: "start" } },
    ],
    points: [{ x: 0, y: 0, label: "" }],
  },
  // 站① 配方範例：y=x²−4x+3 = (x−2)²−1
  p_vertex: {
    W: 760, H: 640, xmin: -1, xmax: 5, ymin: -2.2, ymax: 5.2, axisSym: 2,
    fns: [{ f: (x) => x * x - 4 * x + 3, color: COL.curve }],
    points: [
      { x: 2, y: -1, label: "頂點 (2, −1)", dx: 12, dy: -12 },
      { x: 1, y: 0, label: "(1, 0)", dx: -8, dy: -10, anchor: "end" },
      { x: 3, y: 0, label: "(3, 0)", dx: 8, dy: -10 },
      { x: 0, y: 3, label: "(0, 3)", dx: 8, dy: 4 },
    ],
  },
  // 站② 與方程關係：y=x²−2x−3 = (x−1)²−4
  p_roots: {
    W: 760, H: 640, xmin: -3, xmax: 4, ymin: -5.4, ymax: 3.2, axisSym: 1,
    fns: [{ f: (x) => x * x - 2 * x - 3, color: COL.curve }],
    points: [
      { x: -1, y: 0, label: "(−1, 0)", dx: -8, dy: -10, anchor: "end" },
      { x: 3, y: 0, label: "(3, 0)", dx: 8, dy: -10 },
      { x: 1, y: -4, label: "頂點 (1, −4)", dx: 14, dy: -10 },
    ],
  },
  // 站② 應用：面積 y=x(10−x) = −(x−5)²+25，最大 (5,25)
  p_area: {
    W: 760, H: 600, xmin: -0.6, xmax: 10.6, ymin: -4.5, ymax: 29, xStep: 1, yStep: 5, axisSym: 5,
    fns: [{ f: (x) => x * (10 - x), color: COL.curve }],
    points: [
      { x: 5, y: 25, label: "最大 (5, 25)", dx: 12, dy: -10 },
      { x: 0, y: 0, label: "" },
      { x: 10, y: 0, label: "" },
    ],
  },
};

Object.entries(graphs).forEach(([name, spec]) => {
  const s = svg(spec);
  const h = html(s, spec.W, spec.H);
  fs.writeFileSync(path.join(OUT, name + ".html"), h, "utf8");
  console.log("HTML " + name + "  " + spec.W + "x" + spec.H);
});
