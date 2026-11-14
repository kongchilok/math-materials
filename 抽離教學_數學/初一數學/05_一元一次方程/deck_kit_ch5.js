// deck_kit_ch5.js — 初一數學第五章簡報的版面小工具。
// 由 04_整式的加減/build_deck_ch4.js 的 helper 抽出（版面、字級、配色完全相同），另加：
//   steps() 可放 5 列；recap() 格內可放原生分數；img() 放 _tmp_fig 的天平／條形圖；
//   threeCol()＝講義 D4 三欄式的簡報版；kw()＝關鍵字對譯表。
// 字級：全班共用，內文 ≥24pt（主體 26pt）、標題 34pt。分數一律用 soil_kit.drawEq 原生畫，不打斜線。
const path = require('path');
const fs = require('fs');
const KIT = path.resolve(__dirname, '..', '..', '高一數學', '融合班教學資源', '第一學段',
  '01_集合與常用邏輯用語', '教學簡報', '_scripts');
const pptxgen = require(path.join(KIT, 'node_modules', 'pptxgenjs'));
const { C, F, rt, drawEq } = require(path.join(KIT, 'soil_kit.js'));
const MAN = JSON.parse(fs.readFileSync(path.join(__dirname, '_tmp_fig', 'manifest.json'), 'utf8'));

const W = 13.33, MX = 0.6, CW = W - 2 * MX;
const BODY = 26, TBL = 24, TITLE = 34;

class Deck {
  constructor(foot) { this.p = new pptxgen(); this.p.layout = 'LAYOUT_WIDE'; this.foot = foot; this.n = 0; }
  save(f) { return this.p.writeFile({ fileName: f }); }
  slide(title, { dark = false, badge } = {}) {
    const s = this.p.addSlide(); this.n++;
    s.background = { color: dark ? C.DARK : C.LIGHT };
    if (!dark) {
      s.addText(`初一數學 · ${this.foot}`, { x: MX, y: 7.06, w: 9, h: 0.3, fontFace: F, fontSize: 11, color: C.MUTED, margin: 0 });
      s.addText(String(this.n), { x: 12.2, y: 7.06, w: 0.55, h: 0.3, fontFace: F, fontSize: 11, color: C.MUTED, align: 'right', margin: 0 });
    }
    if (title) {
      s.addShape('ellipse', { x: MX, y: 0.5, w: 0.3, h: 0.3, fill: { color: C.ACCENT }, line: { color: C.ACCENT } });
      s.addText(rt(title, { bold: true, color: C.HEAD }), { x: 1.05, y: 0.33, w: CW - 0.5, h: 0.66, fontFace: F, fontSize: TITLE, valign: 'middle', margin: 0 });
    }
    if (badge) {
      s.addShape('roundRect', { x: 7.4, y: 6.36, w: 5.33, h: 0.56, rectRadius: 0.1, fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1 } });
      s.addText('▶ 轉換點：' + badge, { x: 7.4, y: 6.36, w: 5.33, h: 0.56, fontFace: F, fontSize: 18, bold: true, color: C.HEAD, align: 'center', valign: 'middle', margin: 0 });
    }
    return s;
  }
}

function T(s, str, x, y, w, h, o = {}) {
  s.addText(rt(str, { color: o.color || C.INK, bold: !!o.bold }), {
    x, y, w, h, fontFace: F, fontSize: o.size || BODY, align: o.align || 'left', valign: o.valign || 'middle',
    margin: o.margin === undefined ? 0 : o.margin, lineSpacingMultiple: o.ls || 1.2, wrap: o.wrap !== false });
}
function card(s, x, y, w, h, fill = C.WHITE) {
  s.addShape('roundRect', { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { color: C.EDGE, width: 1.25 } });
}
// 格內容：字串，或 { eq:[...] }（原生分數），或 { eq:[...], tail:'文字', ew:寬 }
function put(s, v, x, y, w, h, o = {}) {
  if (v && typeof v === 'object' && v.eq) {
    const size = o.size || BODY;
    if (v.tail) {
      const ew = v.ew || 1.2;
      drawEq(v.eq, { size, color: o.color || C.INK, align: 'left' })(s, x, y, ew, h);
      T(s, v.tail, x + ew, y, w - ew, h, o);
    } else {
      drawEq(v.eq, { size, color: o.color || C.INK, align: o.align === 'center' ? 'center' : 'left' })(s, x, y, w, h);
    }
  } else T(s, v, x, y, w, h, o);
}
function grid(s, x, y, colW, rowH, rows, { head = true, size = TBL, first = false } = {}) {
  let cy = y;
  rows.forEach((r, ri) => {
    let cx = x;
    r.forEach((v, ci) => {
      const hd = (head && ri === 0) || (first && ci === 0);
      s.addShape('rect', { x: cx, y: cy, w: colW[ci], h: rowH, fill: { color: hd ? C.BLOCK : C.WHITE }, line: { color: C.EDGE, width: 1.25 } });
      put(s, v, cx + 0.15, cy, colW[ci] - 0.3, rowH, { size, bold: hd, color: hd ? C.HEAD : C.INK });
      cx += colW[ci];
    });
    cy += rowH;
  });
}
// 步驟卡：左「做什麼」、右「寫下來」；底下一句放聲思考。5 列時自動收窄行高。
function steps(s, rows, say, { y0 = 1.3, wl = 5.6, rh: rhIn } = {}) {
  const many = rows.length >= 5 || !!rhIn, rh = rhIn || (many ? 0.8 : 0.98), gap = many ? 0.1 : 0.12, wr = CW - wl;
  rows.forEach(([a, b], i) => {
    const y = y0 + i * (rh + gap);
    card(s, MX, y, wl, rh, C.BLOCK); card(s, MX + wl, y, wr, rh);
    s.addShape('ellipse', { x: MX + 0.15, y: y + (rh - 0.56) / 2, w: 0.56, h: 0.56, fill: { color: C.ACCENT }, line: { color: C.ACCENT } });
    T(s, String(i + 1), MX + 0.15, y + (rh - 0.56) / 2, 0.56, 0.56, { color: C.WHITE, bold: true, align: 'center', size: 24 });
    T(s, a, MX + 0.88, y, wl - 0.98, rh, { bold: true, color: C.HEAD, size: 25 });
    put(s, b, MX + wl + 0.25, y, wr - 0.4, rh, { size: BODY + 2 });
  });
  if (say) {
    const y = y0 + rows.length * (rh + gap) + 0.06;
    T(s, '我心裡說：' + say, MX, y, CW, 0.6, { size: 24, color: C.MUTED2, bold: true });
  }
}
function cover(d, title, sub, hook) {
  const s = d.slide(null, { dark: true });
  T(s, title, MX, 2.2, 11.5, 1.5, { size: 50, bold: true, color: 'F2F7F4' });
  T(s, sub, MX, 3.8, 11.5, 0.7, { size: 26, color: 'C9D6CE' });
  T(s, hook, MX, 5.0, 12, 0.9, { size: 28, color: 'F2F7F4', bold: true });
}
function agenda(d, items) {
  const s = d.slide('今日課堂流程');
  items.forEach((t, i) => {
    const y = 1.35 + i * 1.04;
    card(s, MX, y, CW, 0.9, i % 2 ? C.WHITE : C.BLOCK);
    s.addShape('ellipse', { x: MX + 0.2, y: y + 0.16, w: 0.58, h: 0.58, fill: { color: C.ACCENT }, line: { color: C.ACCENT } });
    T(s, String(i + 1), MX + 0.2, y + 0.16, 0.58, 0.58, { color: C.WHITE, bold: true, align: 'center', size: 24 });
    T(s, t, MX + 1.0, y, CW - 1.2, 0.9, { size: 28, bold: true, color: C.HEAD });
  });
}
// 一行一卡；行內可放 { eq }；4 行以上自動收窄
function recap(d, title, lines, badge) {
  const s = d.slide(title, { badge });
  const sp = lines.length >= 4 ? 1.18 : 1.5, h = sp - 0.22;
  lines.forEach((t, i) => {
    const y = 1.4 + i * sp;
    card(s, MX, y, CW, h);
    put(s, t, MX + 0.35, y, CW - 0.7, h, { size: 30 });
  });
  return s;
}
function frayer(d, term, q) {
  const s = d.slide(`「${term}」的邊界在哪裡？`);
  const x0 = MX, y0 = 1.25, w = CW / 2, h = 2.72;
  const lab = ['定義', '特徵（三個都要符合）', '例（是）', '非例（不是）'];
  [[0, 0], [1, 0], [0, 1], [1, 1]].forEach(([cx, cy], i) => {
    const x = x0 + cx * w, y = y0 + cy * h;
    card(s, x, y, w, h, i === 3 ? C.BADBG : (i === 2 ? C.OKBG : C.WHITE));
    T(s, lab[i], x + 0.25, y + 0.1, w - 0.5, 0.5, { size: 22, bold: true, color: C.HEAD });
    q[i].forEach((ln, k) => put(s, ln, x + 0.25, y + 0.62 + k * 0.66, w - 0.5, 0.66, { size: 25 }));
  });
}
function twoCards(d, title, L, R) {
  const s = d.slide(title);
  const w = (CW - 0.4) / 2;
  [L, R].forEach((c, i) => {
    const x = MX + i * (w + 0.4);
    card(s, x, 1.3, w, 5.3);
    s.addShape('rect', { x, y: 1.3, w, h: 0.95, fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1.25 } });
    T(s, c.head, x + 0.3, 1.3, w - 0.6, 0.95, { size: 32, bold: true, color: C.HEAD });
    c.lines.forEach((ln, k) => put(s, ln, x + 0.3, 2.45 + k * 0.82, w - 0.6, 0.82, { size: BODY }));
  });
}
function myth(d, title, items) {
  const s = d.slide(title);
  items.forEach((it, i) => {
    const y = 1.3 + i * 2.75;
    T(s, it.q, MX, y, CW, 0.62, { size: 28, bold: true, color: C.HEAD });
    const w = (CW - 0.3) / 2;
    card(s, MX, y + 0.72, w, 1.75, C.BADBG); card(s, MX + w + 0.3, y + 0.72, w, 1.75, C.OKBG);
    T(s, '常見寫法（錯）', MX + 0.25, y + 0.78, w - 0.5, 0.5, { size: 22, bold: true, color: C.BAD });
    put(s, it.bad, MX + 0.25, y + 1.28, w - 0.5, 1.1, { size: BODY });
    T(s, '正確寫法（對）', MX + w + 0.55, y + 0.78, w - 0.5, 0.5, { size: 22, bold: true, color: C.OK });
    put(s, it.ok, MX + w + 0.55, y + 1.28, w - 0.5, 1.1, { size: BODY });
  });
}
function layered(d, colsData, note = '由練習A 做起；做完一層，自己升上下一層。') {
  const s = d.slide('拿出講義，揀一層開始做', { badge: '動筆練習' });
  const w = (CW - 0.6) / 3;
  colsData.forEach((c, i) => {
    const x = MX + i * (w + 0.3);
    card(s, x, 1.3, w, 4.1);
    s.addShape('rect', { x, y: 1.3, w, h: 1.0, fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1.25 } });
    T(s, ['練習A ★☆☆', '練習B ★★☆', '練習C ★★★'][i], x + 0.2, 1.3, w - 0.4, 1.0, { size: 28, bold: true, color: C.HEAD });
    T(s, c, x + 0.2, 2.45, w - 0.4, 2.8, { size: 25, valign: 'top', ls: 1.35 });
  });
  T(s, note, MX, 5.55, CW, 0.6, { size: 24, bold: true, color: C.MUTED2 });
}
function summary(d, take, base) {
  const s = d.slide(null, { dark: true });
  T(s, '今日帶走', MX, 0.6, CW, 0.7, { size: 30, bold: true, color: 'C9D6CE' });
  T(s, take, MX, 1.5, CW, 2.3, { size: 36, bold: true, color: 'F2F7F4', ls: 1.35 });
  s.addShape('roundRect', { x: MX, y: 4.2, w: CW, h: 2.4, rectRadius: 0.08, fill: { color: '3E5349' }, line: { color: '3E5349' } });
  T(s, '最少要能說出：', MX + 0.35, 4.3, CW - 0.7, 0.6, { size: 24, bold: true, color: 'C9D6CE' });
  T(s, base, MX + 0.35, 4.9, CW - 0.7, 1.6, { size: 28, color: 'F2F7F4', ls: 1.35 });
}
// 圖（天平、條形圖）：按 PNG 長寬比放，回傳圖底的 y
function img(s, name, x, y, w) {
  const m = MAN[name];
  const h = w * m.ar;
  s.addImage({ path: m.path, x, y, w, h });
  return y + h;
}
// D4 三欄式（簡報版）：三張卡，各有欄名；每格一行，可放 { eq }
function threeCol(s, y, h, cols, size = 24) {
  const heads = ['① 語意擷取', '② 關係式建構', '③ 運算與檢核'];
  const w = (CW - 0.3) / 3;
  cols.forEach((lines, i) => {
    const x = MX + i * (w + 0.15);
    card(s, x, y, w, h);
    s.addShape('rect', { x, y, w, h: 0.62, fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1.25 } });
    T(s, heads[i], x + 0.2, y, w - 0.4, 0.62, { size: 22, bold: true, color: C.HEAD });
    const lh = Math.min(0.72, (h - 0.75) / Math.max(lines.length, 1));
    lines.forEach((ln, k) => put(s, ln, x + 0.2, y + 0.7 + k * lh, w - 0.4, lh, { size }));
  });
}
// 關鍵字對譯表（D8）
function kw(d, title, rows, note) {
  const s = d.slide(title);
  grid(s, MX, 1.3, [4.6, CW - 4.6], 0.78, [['題目說…', '就寫成…'], ...rows], { size: 26 });
  if (note) T(s, note, MX, 1.3 + 0.78 * (rows.length + 1) + 0.2, CW, 0.7, { size: 24, bold: true, color: C.BAD });
  return s;
}
const fr = (n, dd) => ({ n: String(n), d: String(dd) });

module.exports = { Deck, C, F, rt, drawEq, W, MX, CW, BODY, TBL, T, card, put, grid, steps, cover, agenda, recap,
  frayer, twoCards, myth, layered, summary, img, threeCol, kw, fr };
