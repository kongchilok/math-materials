// build_L7.js — L7 二次函數、方程與判別式（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 三段式：動機 1–3 頁｜注意 4–11 頁｜行動 12–14 頁　轉換點：P6、P9、P12
const path = require('path');
const { Deck, drawParabola } = require('./soil_kit');

const d = new Deck('二次函數與判別式');

// ── 動機段 ───────────────────────────────────────────────
d.cover({
  title: '二次函數\n與判別式',
  subtitle: '高一數學 · 抽離小組 · 第 7 課（40 分鐘）',
  hook: '帶走一句：Δ 決定條線切唔切到 x 軸',
});

d.agenda({
  steps: [
    '圖象、方程、零點：同一件事',
    '判別式 Δ 係乜',
    'Δ 嘅三種情況',
    '自己揀一層做練習',
  ],
  note: '中間會停低三次，一齊做。',
});

d.problem({
  question: 'y = x^{2}−5x+6 條線，喺邊度碰到 x 軸？',
  sub: '碰到 x 軸，即係 y = 0，即係 x^{2}−5x+6 = 0。',
  caption: '圖象嘅交點　=　方程嘅根　=　函數嘅零點 —— 三個講法，同一件事。',
  star: true,
});

// ── 注意段 ───────────────────────────────────────────────
d.cra({
  title: '三個講法，同一件事',
  concrete: { text: '畫幅圖\n\n條拋物線\n喺 x = 2 同 x = 3\n穿過 x 軸' },
  rep:      { text: '睇高度\n\ny = 0 嗰兩點\n\n就係交點' },
  abstract: { text: '解方程\n\nx^{2}−5x+6 = 0\n\n(x−2)(x−3) = 0\nx = 2 或 3' },
  takeaway: '交點 = 根 = 零點，永遠係同一組數',
  star: true,
});

d.rows3({
  title: '判別式 Δ 係乜',
  rows: [
    { term: '個式',   icon: '1', desc: 'Δ = b^{2}−4ac', eg: '由 ax^{2}+bx+c 攞係數' },
    { term: '做咩用', icon: '2', desc: '唔使解方程都知有幾多個根', eg: '睇正負就得' },
    { term: '睇圖',   icon: '3', desc: '即係條線碰到 x 軸幾多次', eg: '2 次、1 次、定係唔碰' },
  ],
  badge: '一齊讀一次 Δ 個式',
});

d.problem({
  title: '算一次 Δ',
  question: 'x^{2}−5x+6 = 0\n求 Δ',
  sub: 'a = 1　b = −5　c = 6',
  caption: 'Δ = (−5)^{2} − 4×1×6 = 25 − 24 = 1　>　0',
  star: true,
});

d.threeFig({
  title: 'Δ 嘅三種情況（a > 0）',
  panels: [
    { head: 'Δ > 0', draw: drawParabola({ mode: 'two',  roots: ['x_{1}', 'x_{2}'] }),
      text: ['穿過 x 軸兩次', '兩個唔同嘅根'] },
    { head: 'Δ = 0', draw: drawParabola({ mode: 'one',  roots: ['x_{0}'] }),
      text: ['啱啱好掂到一點', '一個重根'] },
    { head: 'Δ < 0', draw: drawParabola({ mode: 'none' }),
      text: ['完全唔碰 x 軸', '冇實根'] },
  ],
  note: 'Δ 大過 0 碰兩次、等於 0 碰一次、細過 0 唔碰',
  star: true,
});

d.tableSlide({
  title: '對照表（a > 0）',
  headers: ['Δ', '同 x 軸', '根', '例'],
  rows: [
    ['Δ > 0', '穿過兩點', '兩個唔同實根', 'x^{2}−5x+6'],
    ['Δ = 0', '掂到一點', '一個重根',     'x^{2}−4x+4'],
    ['Δ < 0', '唔碰',     '冇實根',       'x^{2}+x+1'],
  ],
  colW: [2.0, 3.0, 3.5, 3.6],
  star: true,
  badge: '一齊讀一次三行',
});

d.scaffold4({
  title: '判斷根嘅情況：四步走',
  steps: [
    '寫成標準式\nax^{2}+bx+c = 0',
    '認出 a、b、c\n連埋負號一齊認',
    '代入 Δ = b^{2}−4ac\n記得成個 b 括住先平方',
    '睇正負下結論\n>0 兩個、=0 一個、<0 冇',
  ],
  note: '呢四步之後每題都照用。',
  badge: '照住四步做一次',
});

d.compareCards({
  title: '最容易錯：b 係負數嗰陣',
  cards: [
    { ok: true,  text: 'b = −5 → b^{2} = (−5)^{2} = 25', note: '負數平方變正 —— 要括住先平方' },
    { ok: false, text: 'b = −5 → b^{2} = −25',           note: '冇括住，變咗 −(5^{2})' },
    { ok: true,  text: 'c = −6 → −4ac = −4×1×(−6) = +24', note: 'c 係負數，減負變加' },
  ],
  star: true,
  badge: '再一頁就落手做',
});

d.rows3({
  title: '三個提提你',
  rows: [
    { term: '先標準式', icon: '1', desc: '要等於 0 先可以認 a、b、c', eg: 'x^{2} = 3x−1 要搬埋一邊' },
    { term: '睇正負',   icon: '2', desc: 'Δ 唔使算到幾多，睇正負就夠', eg: '答「有兩個根」就得' },
    { term: 'a < 0',    icon: '3', desc: '開口向下，但 Δ 嘅睇法一樣',  eg: '交點數目唔變' },
  ],
});

// ── 行動段 ───────────────────────────────────────────────
d.layered({
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['x^{2}−6x+5 = 0', '', 'a=__ b=__ c=__', '', 'Δ = ______', '', '有幾多個根？'] },
    { stars: '★★☆', head: '練習 B', lines: ['判斷根嘅情況：', '', '① x^{2}−2x+1 = 0', '', '② x^{2}+2x+5 = 0'] },
    { stars: '★★★', head: '練習 C', lines: ['x^{2}+kx+9 = 0', '', '有兩個相等實根', '', '求 k'] },
  ],
  note: '做完 A 想再試，就上 B、C —— 自己揀就得。',
  badge: '揀一層，開始做',
  star: true,
});

d.summary({
  takeaway: 'Δ = b^{2}−4ac\n決定條線碰唔碰到 x 軸',
  lines: [
    '① 交點 = 根 = 零點，同一件事',
    '② Δ>0 兩個根、Δ=0 一個、Δ<0 冇實根',
    '③ b 係負數要括住先平方',
  ],
  star: true,
});

d.closing({
  title: '你今日識咗睇 Δ 就知有幾多個根',
  line: '落堂前，同隔離位講一次：Δ = b 平方 減 4ac',
  iep: '教學調整（Accommodation）：本簡報加入圖象表徵、步驟卡與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L7_二次函數與判別式.pptx');
d.save(out).then(f => console.log('OK →', f));
