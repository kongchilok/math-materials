// build_L8.js — L8 一元二次不等式（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 三段式：動機 1–3 頁｜注意 4–11 頁｜行動 12–14 頁　轉換點：P6、P9、P12
const path = require('path');
const { Deck, drawParabola, drawNumberLine } = require('./soil_kit');

const d = new Deck('一元二次不等式');

// ── 動機段 ───────────────────────────────────────────────
d.cover({
  title: '一元二次\n不等式',
  subtitle: '高一數學 · 抽離小組 · 第 8 課（40 分鐘）',
  hook: '帶走一句：大於取兩邊，細過取中間',
});

d.agenda({
  steps: [
    '由「等於 0」去到「大過 0」',
    '睇圖搵解集',
    '解題流程：五步',
    '自己揀一層做練習',
  ],
  note: '中間會停低三次，一齊做。',
});

d.problem({
  question: '上一課解 x^{2}−5x+6 = 0，答案係 x = 2 或 3。',
  sub: '咁 x^{2}−5x+6 > 0 呢？答案會係啲乜嘢樣？',
  caption: '唔再係幾個數 —— 而係一整段範圍。',
  star: true,
});

// ── 注意段 ───────────────────────────────────────────────
d.cra({
  title: '大過 0，即係圖象喺邊',
  concrete: { text: '想像條拋物線\n\n有啲位喺 x 軸\n上面，有啲喺下面' },
  rep:      { text: 'y > 0\n\n即係「喺 x 軸上面」\n\n用眼睇得出' },
  abstract: { text: 'x^{2}−5x+6 > 0\n\n即係搵晒\n所有令 y>0 嘅 x' },
  takeaway: '解不等式 = 睇圖象喺 x 軸邊一邊',
  star: true,
});

d.figure({
  title: 'y = x^{2}−5x+6 條線',
  draw: drawParabola({ mode: 'two', roots: ['2', '3'] }),
  caption: '根：2 同 3　開口向上',
  side: [
    'x < 2 嗰邊', '　條線喺 x 軸上面 → y > 0', '',
    '2 < x < 3', '　條線跌咗落 x 軸下面 → y < 0', '',
    'x > 3 嗰邊', '　又返到 x 軸上面 → y > 0',
  ],
  star: true,
  badge: '一齊指住幅圖講一次',
});

d.threeFig({
  title: '兩種問法，兩個答案',
  panels: [
    { head: '> 0（取兩邊）', draw: drawNumberLine({ marks: [{ t: 0.32, label: '2' }, { t: 0.68, label: '3' }], shade: 'outside' }),
      text: ['x < 2　或　x > 3'] },
    { head: '< 0（取中間）', draw: drawNumberLine({ marks: [{ t: 0.32, label: '2' }, { t: 0.68, label: '3' }], shade: 'middle' }),
      text: ['2 < x < 3'] },
    { head: '≥ 0（連根一齊）', draw: drawNumberLine({ marks: [{ t: 0.32, label: '2', filled: true }, { t: 0.68, label: '3', filled: true }], shade: 'outside' }),
      text: ['x ≤ 2　或　x ≥ 3'] },
  ],
  note: '大於取兩邊，細過取中間　·　空心圈唔包括個根，實心圈包括',
  star: true,
});

d.compareCards({
  title: '寫解集，邊個啱？',
  cards: [
    { ok: true,  text: '{x | x < 2，或 x > 3}', note: '兩邊分開寫，中間用「或」' },
    { ok: false, text: '{x | 3 < x < 2}',       note: '寫唔通 —— 冇數會同時大過 3 又細過 2' },
    { ok: true,  text: '{x | 2 < x < 3}',       note: '呢個係「< 0」嘅答案，唔好撈亂' },
  ],
  star: true,
  badge: '再一頁講流程',
});

d.scaffold4({
  title: '解不等式：四步走',
  steps: [
    '搬埋一邊\n右邊要係 0',
    '睇 a 嘅正負\na 係負數就成條乘 −1\n（不等號要反向！）',
    '解方程搵根\n因式分解或者公式',
    '睇問號揀範圍\n> 0 取兩邊，< 0 取中間',
  ],
  note: '第 2 步最易漏 —— 乘負數，不等號一定要調轉。',
  badge: '照住四步做一次',
});

d.problem({
  title: 'a 係負數嗰陣',
  question: '−x^{2}+4x−3 > 0',
  sub: 'a = −1，係負數 → 先成條式乘 −1',
  caption: '乘 −1 之後：x^{2}−4x+3 < 0（不等號由 > 變 <）',
  star: true,
});

d.tableSlide({
  title: '慢鏡：四步行一次',
  headers: ['步', '做咩', '結果'],
  rows: [
    ['1', '已經係一邊 = 0',     '−x^{2}+4x−3 > 0'],
    ['2', 'a<0 → 乘 −1、反向',  'x^{2}−4x+3 < 0'],
    ['3', '因式分解搵根',        '(x−1)(x−3) = 0 → 1、3'],
    ['4', '< 0 → 取中間',        '{x | 1 < x < 3}'],
  ],
  colW: [1.1, 4.6, 6.4],
  star: true,
});

d.rows3({
  title: '最容易錯嘅三個位',
  rows: [
    { term: '冇反向', icon: '1', desc: '乘或者除負數，不等號要調轉', eg: '呢一步錯，答案完全相反' },
    { term: '揀錯邊', icon: '2', desc: '睇清楚係 > 定 <',            eg: '大於兩邊、細過中間' },
    { term: '圈畫錯', icon: '3', desc: '≥ 同 ≤ 先包括個根',          eg: '> 同 < 用空心圈' },
  ],
  badge: '再一頁就落手做',
});

// ── 行動段 ───────────────────────────────────────────────
d.layered({
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['(x−1)(x−4) > 0', '', '（已經分解好）', '', '兩個根：__、__', '', '解集：________'] },
    { stars: '★★☆', head: '練習 B', lines: ['x^{2}−x−6 < 0', '', '先因式分解', '再揀範圍'] },
    { stars: '★★★', head: '練習 C', lines: ['−x^{2}+4x−3 > 0', '', 'a 係負數', '記得反向', '', '（同例題一樣做法）'] },
  ],
  note: '做完 A 想再試，就上 B、C —— 自己揀就得。',
  badge: '揀一層，開始做',
  star: true,
});

d.summary({
  takeaway: '大於取兩邊\n細過取中間',
  lines: [
    '① 先搬到一邊 = 0，再睇 a 嘅正負',
    '② a 係負數：乘 −1，不等號反向',
    '③ 解方程搵根，再對住幅圖揀範圍',
  ],
  star: true,
});

d.closing({
  title: '你今日識咗用幅圖解不等式',
  line: '落堂前，同隔離位講一次：大於取兩邊，細過取中間',
  iep: '教學調整（Accommodation）：本簡報加入圖象與數線表徵、步驟卡與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L8_一元二次不等式.pptx');
d.save(out).then(f => console.log('OK →', f));
