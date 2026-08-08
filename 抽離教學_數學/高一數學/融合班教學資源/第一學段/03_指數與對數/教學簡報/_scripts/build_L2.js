// build_L2.js — L2 分數指數冪（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 三段式：動機 3 頁｜注意 4–10 頁｜行動 11 頁　　轉換點：P6、P11
// 2026-08-08：全份 deck 嘅根式／分數指數冪改用 soil_kit.js 嘅 drawEq 原生畫
// （真根號、真分數線），取代之前打純文字 `^{3}√(a^2)`、`a^{2/3}` 嘅寫法。
const path = require('path');
const { Deck } = require('../../../01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js');
const { rootPower } = require('./exp_draw.js');

const d = new Deck('分數指數冪');

// ── 動機段 ────────────────────────────────────────────────
d.cover({
  title: '分數指數冪',
  subtitle: '高一數學 · 抽離小組 · 第 2 課（40 分鐘）',
  hook: '帶走一句：根指數落分母，次方上分子',
});

d.agenda({
  steps: [
    '根式相乘，點解咁難計？',
    { eq: [{ sqrt: { base: 'a', exp: 'm' }, deg: 'n' }, ' 點樣變成 ', { base: 'a', exp: { n: 'm', d: 'n' } }] },
    '轉咗做指數之後，法則好簡單',
    '分層練習：揀一層',
  ],
  note: '中間會停兩次，一齊做練習。',
});

d.problem({
  question: { eq: [{ sqrt: 'a', deg: '4' }, ' × ', { sqrt: 'a', deg: '12' }, ' 等於幾多？'] },
  sub: '兩個根指數唔同，用根式冇得直接乘埋，卡住。',
  caption: '但係轉成分數指數，就變返做「指數相加」—— 一行搞掂。',
  badge: '一齊試吓',
});

// ── 注意段 ────────────────────────────────────────────────
d.figure({
  title: '根式 → 分數指數：邊個數去邊',
  star: true,
  draw: rootPower({ a: 'a', root: '3', pow: '2', caption: '下面開方，上面次方' }),
  side: [
    { eq: [{ sqrt: { base: 'a', exp: '2' }, deg: '3' }, ' 讀做：'] },
    '「a 嘅平方，開 3 次方」',
    '',
    '根指數 3 → 做分母',
    '',
    '次方 2 → 做分子',
    '',
    { eq: ['所以寫成 ', { base: 'a', exp: { n: '2', d: '3' } }] },
  ],
});

d.eqTable({
  title: '五個對照，睇熟佢',
  star: true,
  headers: ['根式', '分數指數冪', '點記'],
  colW: [3.4, 3.5, 5.2],
  rows: [
    [{ eq: [{ sqrt: 'a' }] }, { eq: [{ base: 'a', exp: { n: '1', d: '2' } }] }, '冇寫根指數 = 2'],
    [{ eq: [{ sqrt: 'a', deg: '3' }] }, { eq: [{ base: 'a', exp: { n: '1', d: '3' } }] }, '根指數 3 → 分母 3'],
    [{ eq: [{ sqrt: { base: 'a', exp: '2' }, deg: '3' }] }, { eq: [{ base: 'a', exp: { n: '2', d: '3' } }] }, '再加次方 2 → 分子 2'],
    [{ eq: [{ sqrt: { base: 'a', exp: '3' } }] }, { eq: [{ base: 'a', exp: { n: '3', d: '2' } }] }, '根指數 2、次方 3'],
    [{ eq: ['1 / ', { sqrt: { base: 'a', exp: '5' }, deg: '3' }] }, { eq: [{ base: 'a', exp: ['−', { n: '5', d: '3' }] }] }, '喺分母 → 指數加負號'],
  ],
});

d.layered({
  title: '練習一：根式 ↔ 分數指數',
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: [
      '寫成分數指數：', '',
      { eq: ['① ', { sqrt: { base: 'a', exp: '2' }, deg: '3' }, ' = ?'] }, '',
      { eq: ['② ', { sqrt: 'a' }, ' = ?'] },
    ] },
    { stars: '★★☆', head: '練習 B', lines: [
      { eq: ['① ', { sqrt: { base: 'a', exp: '3' } }, ' = ?'] }, '',
      { eq: ['② 1 / ', { sqrt: { base: 'a', exp: '5' }, deg: '3' }, ' = ?'] }, '',
      { eq: ['③ ', { base: { n: '4', d: '9' }, exp: { n: '1', d: '2' } }, ' = ?'] },
    ] },
    { stars: '★★★', head: '練習 C', lines: [
      { eq: ['① ', { sqrt: 'a', deg: '4' }, ' × ', { sqrt: 'a', deg: '12' }] }, '',
      '　 化成一個', '　 分數指數冪。',
    ] },
  ],
  note: '每題先問：根指數係幾多？次方係幾多？',
  badge: '自己揀一層',
});

d.rows3({
  title: '轉咗做指數，法則好簡單',
  rows: [
    { icon: '①', term: '乘', desc: '底數一樣 → 指數相加',
      egParts: [{ base: 'a', exp: { n: '1', d: '6' } }, ' × ', { base: 'a', exp: { n: '2', d: '3' } }, ' = ', { base: 'a', exp: { n: '5', d: '6' } }] },
    { icon: '②', term: '除', desc: '底數一樣 → 指數相減',
      egParts: [{ base: 'a', exp: { n: '2', d: '3' } }, ' ÷ ', { base: 'a', exp: { n: '1', d: '3' } }, ' = ', { base: 'a', exp: { n: '1', d: '3' } }] },
    { icon: '③', term: '次方再次方', desc: '兩個指數相乘',
      egParts: [{ base: ['(', { base: '2', exp: '3' }, ')'], exp: { n: '2', d: '3' } }, ' = ', { base: '2', exp: '3 × 2/3' }, ' = ', { base: '2', exp: '2' }] },
  ],
});

d.scaffold4({
  title: '示範：求 8^{2/3}',
  star: true,
  steps: [
    { eq: ['底數寫成同一個數嘅次方：8 = ', { base: '2', exp: '3' }] },
    { eq: ['代入：', { base: '8', exp: { n: '2', d: '3' } }, ' = ', { base: ['(', { base: '2', exp: '3' }, ')'], exp: { n: '2', d: '3' } }] },
    { eq: ['次方再次方 → 指數相乘：3 × ', { n: '2', d: '3' }, ' = 2'] },
    { eq: ['算出答案：', { base: '2', exp: '2' }, ' = 4'] },
  ],
  note: '呢四步，之後每一題都照咁寫，唔使另外諗格式。',
});

d.compareCards({
  title: '三條最易錯',
  cards: [
    { ok: false,
      text: { eq: ['3', { base: 'a', exp: '-2' }, ' = 1 / (3', { base: 'a', exp: '2' }, ')'] },
      note: '負指數淨係搬 a，個 3 唔跟住落分母 → 應該係 3 / a^{2}' },
    { ok: false,
      text: { eq: [{ sqrt: { base: '2', exp: '4' }, deg: '3' }, ' = ', { base: '2', exp: { n: '3', d: '4' } }] },
      note: '根指數 3 落分母、次方 4 上分子 → 應該係 2^{4/3}' },
    { ok: true,
      text: { eq: [{ base: 'a', exp: { n: '2', d: '3' } }, ' ÷ ', { base: 'a', exp: { n: '1', d: '3' } }, ' = ', { base: 'a', exp: { n: '1', d: '3' } }] },
      note: '底數一樣，指數相減：2/3 − 1/3 = 1/3' },
  ],
  badge: '逐張讀一次',
});

// ── 行動段 ────────────────────────────────────────────────
d.layered({
  title: '練習二：計出個值',
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: [
      { eq: ['① ', { base: 'a', exp: { n: '1', d: '2' } }, ' × ', { base: 'a', exp: { n: '1', d: '2' } }, ' = ?'] }, '',
      { eq: ['② ', { base: ['(', { base: '2', exp: '3' }, ')'], exp: { n: '1', d: '3' } }, ' = ?'] },
    ] },
    { stars: '★★☆', head: '練習 B', lines: [
      { eq: ['① ', { base: '8', exp: { n: '2', d: '3' } }, ' = ?'] },
      '　（照四步寫）', '',
      '② a = 4，求',
      { eq: ['　 ', { base: 'a', exp: { n: '1', d: '6' } }, ' · ', { base: 'a', exp: { n: '2', d: '3' } }, ' ÷ ', { base: 'a', exp: { n: '1', d: '3' } }] },
    ] },
    { stars: '★★★', head: '練習 C', lines: [
      '① 化簡：',
      { eq: ['　 4', { base: 'a', exp: { n: '2', d: '3' } }, { base: 'b', exp: ['−', { n: '1', d: '3' }] }] },
      { eq: ['　 ÷ (−', { n: '2', d: '3' }, ' · ', { base: 'a', exp: ['−', { n: '1', d: '3' }] }, { base: 'b', exp: ['−', { n: '1', d: '3' }] }, ')'] },
    ] },
  ],
  note: '唔好跳步：先整理指數，最後先計數。',
  badge: '自己揀一層',
});

d.summary({
  takeaway: '根指數落分母，次方上分子 —— 根式即刻變成分數指數。',
  lines: [
    { eq: ['① ', { sqrt: { base: 'a', exp: 'm' }, deg: 'n' }, ' = ', { base: 'a', exp: { n: 'm', d: 'n' } }, '：下面開方，上面次方'] },
    { eq: ['② 喺分母 → 指數加負號：1 / ', { base: 'a', exp: 'n' }, ' = ', { base: 'a', exp: '-n' }] },
    '③ 轉咗做指數：乘就加、除就減、次方就相乘',
  ],
});

d.closing({
  title: '下一課：指數函數',
  line: '指數唔再淨係數字，變成變數 x —— y = 2^{x}',
  iep: '教學調整（Accommodation）：本簡報加入部件對應圖、對照表與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L2_分數指數冪.pptx');
d.save(out).then(f => console.log('OK →', f, '| slides:', d.n));
