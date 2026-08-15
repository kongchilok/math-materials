// build_L3.js — L3 餘式定理（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 三段式：動機 1–3 頁｜注意 4–11 頁｜行動 12–14 頁　轉換點：P6、P9、P12
const path = require('path');
const { Deck } = require('./soil_kit');

const d = new Deck('餘式定理');

// ── 動機段 ───────────────────────────────────────────────
d.cover({
  title: '餘式定理',
  subtitle: '高一數學 · 抽離小組 · 第 3 課（40 分鐘）',
  hook: '帶走一句：除以 x−a，餘數就係 f(a)',
});

d.agenda({
  steps: [
    '如果淨係想知餘數呢？',
    '餘式定理：代入就得',
    '除式係 ax−b 點算',
    '自己揀一層做練習',
  ],
  note: '中間會停低三次，一齊做。',
});

d.problem({
  question: '如果我淨係想知「餘數」，使唔使做成條除法？',
  sub: '上兩課：長除法慢，綜合除法快啲 —— 但都仲要一格格行。',
  caption: '今日呢招：唔使做除法，代一個數入去就知。',
  star: true,
});

// ── 注意段 ───────────────────────────────────────────────
d.cra({
  title: '點解代入就得？',
  concrete: { text: '除法原理話我哋：\n\nf(x) = (x−a)·q(x) + r' },
  rep:      { text: '將 x = a 代入\n\n(a−a) 變咗 0\n\n前面成嚿嘢消失' },
  abstract: { text: 'f(a) = 0·q(a) + r\n\nf(a) = r\n\n餘數就係 f(a)' },
  takeaway: '揀 x=a，係因為佢啱啱好殺死 q(x)',
  star: true,
});

d.rows3({
  title: '餘式定理，三句講完',
  rows: [
    { term: '定理', icon: '1', desc: 'f(x) 除以 (x−a)，餘數 = f(a)', eg: '一個常數，唔會有 x' },
    { term: '要求', icon: '2', desc: '除式一定要係一次式',           eg: '除以 x^{2}−1 唔可以咁做' },
    { term: '好處', icon: '3', desc: '唔使做除法，代入計數就得',      eg: '快好多，又唔易錯' },
  ],
  badge: '一齊讀一次定理',
});

d.problem({
  title: '例題（一）',
  question: 'f(x) = x^{3}−3x^{2}+2x−5\n求 f(x) ÷ (x−2) 嘅餘式',
  sub: '除式係 x−2 → 令 x−2 = 0 → 代 x = 2',
  star: true,
});

d.scaffold4({
  title: '例題（一）：四步算',
  steps: [
    '令除式 = 0\nx−2 = 0 → x = 2',
    '代入 f(x)\nf(2) = 2^{3}−3×2^{2}+2×2−5',
    '逐項計\n= 8 − 12 + 4 − 5',
    '加埋\n= −5　→ 餘式係 −5',
  ],
  note: '答案係一個數，唔會有 x —— 有 x 就一定計錯咗。',
  badge: '照住四步做一次',
});

d.compareCards({
  title: '代邊個數？',
  cards: [
    { ok: true,  text: '除以 (x−2) → 代 x = 2',  note: '令 x−2 = 0，解到 x = 2' },
    { ok: false, text: '除以 (x−2) → 代 x = −2', note: '睇錯號 —— 要令除式等於 0，唔係抄個數落嚟' },
    { ok: true,  text: '除以 (x+3) → 代 x = −3', note: 'x+3 = 0 → x = −3' },
  ],
  star: true,
  badge: '再一頁就轉難少少',
});

d.problem({
  title: '例題（二）',
  question: 'g(x) = 2x^{3}−x^{2}+3x−1\n求 g(x) ÷ (2x−1) 嘅餘式',
  sub: '今次除式係 2x−1，x 嘅係數唔係 1。',
  caption: '做法一樣：令 2x−1 = 0 → x = ½，代 ½ 入去。',
  star: true,
});

d.tableSlide({
  title: '例題（二）：逐項計',
  headers: ['項', '代 x = ½', '值'],
  rows: [
    ['2x^{3}',  '2 × (½)^{3} = 2 × ⅛', '¼'],
    ['−x^{2}',  '−(½)^{2}',            '−¼'],
    ['3x',      '3 × ½',               '3/2'],
    ['−1',      '常數',                '−1'],
  ],
  colW: [2.3, 5.2, 4.6],
  star: true,
});

d.compareCards({
  title: '加埋，得幾多？',
  cards: [
    { ok: true, text: '¼ − ¼ + 3/2 − 1 = ½', note: '頭兩項啱啱好抵消，剩返 3/2 − 1 = ½' },
    { ok: true, text: '餘式 = ½',            note: '答案可以係分數 —— 餘式唔一定係整數' },
  ],
});

d.rows3({
  title: 'f(a) 有兩個身分',
  rows: [
    { term: '函數值', icon: '1', desc: 'f(x) 喺 x=a 嗰點嘅高度', eg: '圖象上一點' },
    { term: '餘數',   icon: '2', desc: 'f(x) 除以 (x−a) 剩返幾多', eg: '今日學嘅' },
    { term: '同一個數', icon: '3', desc: '兩個講法，答案完全一樣',  eg: '所以先可以代入求餘式' },
  ],
  badge: '再一頁就落手做',
});

// ── 行動段 ───────────────────────────────────────────────
d.layered({
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['f(x) = x^{2}+3x+2', '', '求 f(1) = ___', '', '所以 ÷(x−1) 餘 ___'] },
    { stars: '★★☆', head: '練習 B', lines: ['f(x) = x^{3}+2x^{2}−x+4', '', '求 f(x) ÷ (x+1)', '嘅餘式'] },
    { stars: '★★★', head: '練習 C', lines: ['f(x) = 2x^{3}+ax^{2}−5', '', '÷ (x−1) 餘 3', '', '求 a'] },
  ],
  note: '做完 A 想再試，就上 B、C —— 自己揀就得。',
  badge: '揀一層，開始做',
  star: true,
});

d.summary({
  takeaway: '除以 x−a，餘數就係 f(a)\n唔使做除法',
  lines: [
    '① 令除式 = 0，解到 x 應該代乜',
    '② 除以 (ax−b) 就代 x = b/a',
    '③ 餘式係一個數，有 x 就係計錯',
  ],
  star: true,
});

d.closing({
  title: '你今日識咗一招唔使做除法嘅方法',
  line: '落堂前，同隔離位講一次：除以 x−a，餘數係 f(a)',
  iep: '教學調整（Accommodation）：本簡報加入具體表徵、步驟卡與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L3_餘式定理.pptx');
d.save(out).then(f => console.log('OK →', f));
