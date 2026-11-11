// build_deck_ch4.js — 初一數學 第四章〈整式的加減〉教學簡報（全班共用）
// 第 1 份：4.1-1 單項式；第 2 份：4.1-2 多項式與整式。
// 內容、例題、標記（ⓐⓑ、弗雷爾四象限、我做／我們做）逐項對齊同資料夾
// build_ch4.py 的 lesson1／lesson2 講義練習——同一課同一套視覺語言。
// 字級：全班共用，內文 ≥24pt（主體 26pt）、標題 34pt（65 吋螢幕 5 m 可讀）。
// 分數一律用 soil_kit.drawEq 原生畫，不打斜線。三欄以上自己落 \n，不靠自動換行。
// 用法：node build_deck_ch4.js [1 2]
const path = require('path');
const KIT = path.resolve(__dirname, '..', '..', '高一數學', '融合班教學資源', '第一學段',
  '01_集合與常用邏輯用語', '教學簡報', '_scripts');
const pptxgen = require(path.join(KIT, 'node_modules', 'pptxgenjs'));
const { C, F, rt, drawEq } = require(path.join(KIT, 'soil_kit.js'));

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

// ---- 小工具 ----
function T(s, str, x, y, w, h, o = {}) {
  s.addText(rt(str, { color: o.color || C.INK, bold: !!o.bold }), {
    x, y, w, h, fontFace: F, fontSize: o.size || BODY, align: o.align || 'left', valign: o.valign || 'middle',
    margin: o.margin === undefined ? 0 : o.margin, lineSpacingMultiple: o.ls || 1.2, wrap: o.wrap !== false });
}
function card(s, x, y, w, h, fill = C.WHITE) {
  s.addShape('roundRect', { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { color: C.EDGE, width: 1.25 } });
}
// 格內容：字串，或 { eq:[...] }（原生分數），或 { eq:[...], tail:'文字' }
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
// 手砌表格（表頭灰底；格內可放 drawEq）
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
// 步驟卡：左「做什麼」、右「寫下來」；底下一句放聲思考
function steps(s, rows, say) {
  const y0 = 1.3, rh = 0.98, wl = 6.3, wr = CW - wl;
  rows.forEach(([a, b], i) => {
    const y = y0 + i * (rh + 0.12);
    card(s, MX, y, wl, rh, C.BLOCK); card(s, MX + wl, y, wr, rh);
    s.addShape('ellipse', { x: MX + 0.15, y: y + 0.2, w: 0.58, h: 0.58, fill: { color: C.ACCENT }, line: { color: C.ACCENT } });
    T(s, String(i + 1), MX + 0.15, y + 0.2, 0.58, 0.58, { color: C.WHITE, bold: true, align: 'center', size: 24 });
    T(s, a, MX + 0.9, y, wl - 1.0, rh, { bold: true, color: C.HEAD, size: BODY });
    put(s, b, MX + wl + 0.25, y, wr - 0.4, rh, { size: BODY + 2 });
  });
  if (say) {
    const y = y0 + rows.length * (rh + 0.12) + 0.08;
    T(s, '我心裡說：' + say, MX, y, CW, 0.7, { size: 24, color: C.MUTED2, bold: true });
  }
}
function cover(d, title, sub, hook) {
  const s = d.slide(null, { dark: true });
  T(s, title, MX, 2.2, 9.5, 1.5, { size: 50, bold: true, color: 'F2F7F4' });
  T(s, sub, MX, 3.8, 11, 0.7, { size: 26, color: 'C9D6CE' });
  T(s, hook, MX, 5.0, 11.5, 0.9, { size: 28, color: 'F2F7F4', bold: true });
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
function recap(d, title, lines, badge) {
  const s = d.slide(title, { badge });
  lines.forEach((t, i) => {
    const y = 1.45 + i * 1.5;
    card(s, MX, y, CW, 1.25);
    T(s, t, MX + 0.35, y, CW - 0.7, 1.25, { size: 30 });
  });
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
    T(s, it.bad, MX + 0.25, y + 1.28, w - 0.5, 1.1, { size: BODY });
    T(s, '正確寫法（對）', MX + w + 0.55, y + 0.78, w - 0.5, 0.5, { size: 22, bold: true, color: C.OK });
    T(s, it.ok, MX + w + 0.55, y + 1.28, w - 0.5, 1.1, { size: BODY });
  });
}
function layered(d, colsData, note) {
  const s = d.slide('拿出講義，揀一層開始做', { badge: '動筆練習' });
  const w = (CW - 0.6) / 3;
  colsData.forEach((c, i) => {
    const x = MX + i * (w + 0.3);
    card(s, x, 1.3, w, 4.1);
    s.addShape('rect', { x, y: 1.3, w, h: 1.0, fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1.25 } });
    T(s, c.head, x + 0.2, 1.3, w - 0.4, 1.0, { size: 28, bold: true, color: C.HEAD });
    T(s, c.body, x + 0.2, 2.45, w - 0.4, 2.8, { size: 25, valign: 'top', ls: 1.35 });
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
const fr = (n, dd) => ({ n: String(n), d: String(dd) });
const pw = (b, e) => ({ base: b, exp: String(e) });

// =====================================================================
// 第 1 份　單項式
// =====================================================================
async function deck1() {
  const d = new Deck('4.1 整式（第 1 課時）單項式');
  cover(d, '單項式', '第四章 整式的加減　4.1 整式（第 1 課時）', '5n、a^{2} 這類式子，有名字嗎？');
  agenda(d, ['先重溫：列代數式', '新名字：單項式', 'ⓐ 係數　ⓑ 次數', '我做 → 我們做', '練習 A → B → C']);
  recap(d, '先重溫：用含字母的式子填空', [
    '① 每本練習簿 5 元，買 n 本共 ＿＿＿ 元',
    '② 邊長為 a 的正方形，面積是 ＿＿＿',
    '③ 底為 a、高為 h 的三角形，面積是 ＿＿＿'], '自己寫 1 分鐘');
  {
    const s = d.slide('這三個式子有什麼共同點？');
    const w = (CW - 0.8) / 3;
    [['5n'], ['a^{2}'], null].forEach((v, i) => {
      const x = MX + i * (w + 0.4);
      card(s, x, 1.4, w, 2.3);
      if (v) T(s, v[0], x, 1.4, w, 2.3, { size: 60, bold: true, align: 'center', color: C.HEAD });
      else drawEq([fr(1, 2), 'ah'], { size: 60, color: C.HEAD })(s, x, 1.4, w, 2.3);
    });
    card(s, MX, 4.1, CW, 1.2, C.BLOCK);
    T(s, '數和字母之間，只有「乘」。', MX + 0.4, 4.1, CW - 0.8, 1.2, { size: 34, bold: true, color: C.HEAD });
    T(s, '這一類式子叫做「單項式」。', MX + 0.4, 5.5, CW - 0.8, 0.8, { size: 30 });
  }
  {
    const s = d.slide('單項式');
    card(s, MX, 1.35, CW, 1.7, C.BLOCK);
    T(s, '數或字母的積。', MX + 0.5, 1.35, CW - 1, 1.7, { size: 44, bold: true, color: C.HEAD });
    card(s, MX, 3.3, CW, 1.3);
    T(s, '單獨一個數、單獨一個字母，也是單項式。', MX + 0.5, 3.3, CW - 1, 1.3, { size: 30 });
    T(s, '例：5n　　a^{2}　　−6　　x', MX + 0.5, 4.9, CW - 1, 1.0, { size: 36, bold: true });
  }
  frayer(d, '單項式', [
    ['數或字母的積。', '單獨一個數或字母也算。'],
    ['① 數和字母之間只有「乘」', '② 沒有被「＋」「−」分開', '③ 分母沒有字母'],
    ['7t　　−x　　a^{2}b', '5　　y'],
    ['x＋1：有加號，違反②', 'a−b：有減號，違反②', { eq: [fr(3, 'x')], tail: '：分母有字母，違反③', ew: 0.55 }]]);
  twoCards(d, '單項式的兩個「身份證」', {
    head: 'ⓐ 係數', lines: ['數字因數，', '連同前面的符號。', '', '例：3x^{2}y 的係數是 3', '　　−ab 的係數是 −1'] }, {
    head: 'ⓑ 次數', lines: ['所有字母的指數，', '加起來。', '', '例：3x^{2}y 的次數是', '　　2＋1，即 3'] });
  {
    const s = d.slide('我做：−4a^{2}b^{3}c 的係數和次數');
    steps(s, [['ⓐ 找數字因數（連符號）', '係數是 −4'],
      ['寫出每個字母的指數', 'a：2　　b：3　　c：1'],
      ['ⓑ 把指數加起來', '2＋3＋1，得 6'],
      ['寫結論', '係數 −4，次數 6']],
    '「c 沒有寫指數，就是 1，不是 0。」');
  }
  {
    const s = d.slide('幾個要留意的情況');
    grid(s, MX, 1.3, [2.6, 2.0, 2.0, CW - 6.6], 0.88, [
      ['單項式', 'ⓐ 係數', 'ⓑ 次數', '要留意'],
      ['x', '1', '1', '係數 1、指數 1 都省略不寫'],
      ['−ab', '−1', '2', '只有負號，係數是 −1'],
      ['πr^{2}', 'π', '2', 'π 是一個數，不是字母'],
      [{ eq: ['−', fr(3, 4), pw('x', 2), 'y'] }, { eq: ['−', fr(3, 4)] }, '3', '分數連負號都是係數'],
      ['5', '5', '0', '沒有字母，次數是 0']]);
  }
  {
    const s = d.slide('我們做：一起填', { badge: '全班一起答' });
    const cw = [2.4, 2.4, 2.4, 2.4, CW - 9.6];
    grid(s, MX, 1.5, cw, 1.25, [
      ['單項式', '7t^{2}', '−m', '2πr', { eq: [fr(2, 5), pw('x', 3), 'y'] }],
      ['ⓐ 係數', '', '', '', ''],
      ['ⓑ 次數', '2', '', '', '']], { size: 30, first: true });
    T(s, '提示：沒有寫出來的係數是 1 或 −1；沒有寫出來的指數是 1。', MX, 5.45, CW, 0.7, { size: 24, color: C.MUTED2, bold: true });
  }
  myth(d, '最容易錯的兩個地方', [
    { q: '3x^{2}y^{3} 的次數是多少？', bad: '只看最大的指數：3', ok: '指數全部相加：2＋3，即 5' },
    { q: '−x^{2}y 的係數是多少？', bad: '看不到數字，寫 1', ok: '負號是係數的一部分：−1' }]);
  layered(d, [
    { head: '練習A ★☆☆', body: '第 1–3 題\n判斷、填表、填空\n（有 ⓐⓑ 提示）' },
    { head: '練習B ★★☆', body: '第 4–6 題\n填表、判斷對錯、\n自己寫單項式' },
    { head: '練習C ★★★', body: '第 7–9 題\n求指數、\n寫生活情境' }],
  '由練習A 做起；做完一層，自己升上下一層。');
  summary(d, '單項式：數和字母相乘。\n係數連符號；次數是指數的和。',
    '看到 −4a^{2}b：\n數字 −4 是係數；指數 2＋1，次數是 3。');
  await d.save(path.join(__dirname, '簡報_4.1-1_單項式.pptx'));
}

// =====================================================================
// 第 2 份　多項式與整式
// =====================================================================
async function deck2() {
  const d = new Deck('4.1 整式（第 2 課時）多項式與整式');
  cover(d, '多項式與整式', '第四章 整式的加減　4.1 整式（第 2 課時）', 'a＋1 不是單項式，那它是什麼？');
  agenda(d, ['先重溫：單項式', '新名字：多項式', 'ⓐ 項　ⓑ 多項式的次數', '整式、降冪排列', '我做 → 我們做 → 練習']);
  recap(d, '先重溫：單項式', [
    '① −3x^{2}y 的係數是 ＿＿，次數是 ＿＿',
    '② 2πr 的係數是 ＿＿，次數是 ＿＿',
    '③ a＋1 是不是單項式？為什麼？'], '自己寫 1 分鐘');
  {
    const s = d.slide('a＋1 是什麼？');
    card(s, MX, 1.35, CW, 1.5);
    T(s, 'a＋1：單項式 a 和單項式 1 加起來。', MX + 0.5, 1.35, CW - 1, 1.5, { size: 34, bold: true });
    card(s, MX, 3.1, CW, 1.5, C.BLOCK);
    T(s, '多項式：幾個單項式的和。', MX + 0.5, 3.1, CW - 1, 1.5, { size: 40, bold: true, color: C.HEAD });
    T(s, '例：2n−10　　x^{2}＋2x＋8　　ab−πr^{2}', MX + 0.5, 4.95, CW - 1, 1.0, { size: 32, bold: true });
  }
  twoCards(d, '多項式的兩個「身份證」', {
    head: 'ⓐ 項', lines: ['每一個單項式，', '連同前面的符號。', '', '不含字母的項，', '叫做常數項。'] }, {
    head: 'ⓑ 多項式的次數', lines: ['次數最高的那一項', '的次數。', '', '（不是把各項的次數', '　加起來。）'] });
  frayer(d, '多項式', [
    ['幾個單項式的和。'],
    ['① 最少有兩項', '② 每一項都是單項式', '③ 項與項用「＋」「−」連接'],
    ['2n−10', 'x^{2}＋2x＋8', 'ab−πr^{2}'],
    ['5x：只有一項，違反①', { eq: [fr(1, 'x'), '＋2'], tail: '：有一項不是單項式，', ew: 1.35 }, '　　　違反②']]);
  {
    const s = d.slide('我做：−2a^{2}b＋3ab−5 是幾次幾項式？');
    steps(s, [['在每個「＋」「−」前面切開', '−2a^{2}b ｜ ＋3ab ｜ −5'],
      ['ⓐ 寫出各項', '−2a^{2}b，3ab，−5'],
      ['寫出每一項的次數', '3，2，0'],
      ['ⓑ 找最高次數，數有幾項', '三次三項式']],
    '「符號跟著後面那一項走。」');
  }
  {
    const s = d.slide('整式：單項式和多項式的總稱');
    card(s, W / 2 - 2.2, 1.35, 4.4, 1.2, C.DARK);
    T(s, '整式', W / 2 - 2.2, 1.35, 4.4, 1.2, { size: 40, bold: true, color: 'F2F7F4', align: 'center' });
    const w = (CW - 0.6) / 2;
    [['單項式', '數或字母的積', '4r^{2}　　3　　−t'], ['多項式', '幾個單項式的和', '2a＋1　　m^{3}−n']].forEach((c, i) => {
      const x = MX + i * (w + 0.6);
      s.addShape('line', { x: x + w / 2, y: 2.55, w: 0, h: 0.65, line: { color: C.ACCENT, width: 2.5 } });
      card(s, x, 3.2, w, 3.1);
      s.addShape('rect', { x, y: 3.2, w, h: 0.95, fill: { color: C.BLOCK }, line: { color: C.EDGE, width: 1.25 } });
      T(s, c[0], x + 0.3, 3.2, w - 0.6, 0.95, { size: 32, bold: true, color: C.HEAD });
      T(s, c[1], x + 0.3, 4.3, w - 0.6, 0.8, { size: BODY });
      T(s, c[2], x + 0.3, 5.15, w - 0.6, 0.9, { size: 30, bold: true });
    });
    s.addShape('line', { x: MX + w / 2, y: 2.55 + 0.32, w: w + 0.6, h: 0, line: { color: C.ACCENT, width: 2.5 } });
  }
  {
    const s = d.slide('我做：把 5x−3x^{3}＋2＋x^{2} 按 x 降冪排列');
    steps(s, [['切開各項（連符號）', '＋5x ｜ −3x^{3} ｜ ＋2 ｜ ＋x^{2}'],
      ['寫出 x 的指數', '1，3，0，2'],
      ['指數由大到小重排', '−3x^{3}＋x^{2}＋5x＋2']],
    '「搬項的時候，符號跟著一起搬。」');
    T(s, '降冪排列：按某個字母的指數，由大到小排。', MX, 5.55, CW, 0.7, { size: BODY, bold: true, color: C.HEAD });
  }
  {
    const s = d.slide('我們做：x^{3}−4x^{2}y^{2}＋y−1', { badge: '全班一起答' });
    ['ⓐ 項：x^{3}，＿＿＿＿，y，＿＿＿',
      '各項的次數：3，＿＿，1，＿＿',
      'ⓑ 它是 ＿＿ 次 ＿＿ 項式'].forEach((t, i) => {
      const y = 1.45 + i * 1.5;
      card(s, MX, y, CW, 1.25);
      T(s, t, MX + 0.35, y, CW - 0.7, 1.25, { size: 32 });
    });
  }
  myth(d, '最容易錯的兩個地方', [
    { q: 'x^{2}−3x−2 有哪些項？', bad: 'x^{2}，3x，2（漏了符號）', ok: 'x^{2}，−3x，−2（項連符號）' },
    { q: 'a^{3}b−4ab−6 的次數是多少？', bad: '看到 a^{3}，寫 3', ok: 'a^{3}b 的次數是 3＋1，所以是 4' }]);
  layered(d, [
    { head: '練習A ★☆☆', body: '第 1–3 題\n分類、填表、填空\n（各項已切開）' },
    { head: '練習B ★★☆', body: '第 4–6 題\n填表、降冪排列、\n判斷對錯' },
    { head: '練習C ★★★', body: '第 7–9 題\n求指數、\n自己寫多項式' }],
  '由練習A 做起；做完一層，自己升上下一層。');
  summary(d, '多項式：幾個單項式的和。\n項連符號；次數看最高的那一項。',
    '看到 x^{2}−3x−2：在符號前切開，\n三項是 x^{2}、−3x、−2；最高次是 2，二次三項式。');
  await d.save(path.join(__dirname, '簡報_4.1-2_多項式與整式.pptx'));
}

(async () => {
  const todo = process.argv.slice(2).map(Number);
  if (!todo.length || todo.includes(1)) await deck1();
  if (!todo.length || todo.includes(2)) await deck2();
  console.log('done');
})();
