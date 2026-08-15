// build_L6.js — 初三 13 反比例函數．L6「總複習與分層綜合」
const path = require('path');
const { KIT } = require('./inv_draw.js');
const { Deck } = KIT;

const d = new Deck('L6　總複習與分層綜合', '初三數學');

d.cover({
  title: '五課合埋\n記住兩個字：睇 k',
  subtitle: 'L6　總複習與分層綜合',
  hook: 'k 決定象限、決定增減、決定面積',
});

d.agenda({
  steps: [
    '五課重點，一頁過',
    '三大陷阱，逐個拆',
    '綜合題：同一次函數交點',
    '揀一層，做綜合練習',
  ],
  note: '今日唔教新嘢，係把五課串返埋一齊。',
});

d.rows3({
  title: '重點回顧（一）',
  rows: [
    { icon: '1', term: '概念', desc: 'y ＝ k/x，x 喺分數線下面，k ≠ 0',
      eg: 'L1　又可以寫成 xy ＝ k' },
    { icon: '2', term: '圖像', desc: '雙曲線兩支，睇 k 嘅正負判象限',
      eg: 'L2　k ＞ 0 一、三象限；k ＜ 0 二、四象限' },
    { icon: '3', term: '增減', desc: '每一支上，y 隨 x 點變',
      eg: 'L3　k ＞ 0 減小；k ＜ 0 增大' },
  ],
});

d.compare2({
  title: '重點回顧（二）',
  left:  { head: 'L4　求解析式', lines: ['設 y ＝ k/x', '把點嘅 x、y 代入', '解出 k', '寫返落條式度'] },
  right: { head: 'L5　矩形面積', lines: ['圖像上任一點', '向兩條軸畫垂線', '面積 ＝ |x × y|', '＝ |k|'] },
  note: '一個係「由點求式」，一個係「由式求面積」。',
  badge: '下一頁：三大陷阱',
});

d.compareCards({
  title: '三大陷阱，逐個拆',
  cards: [
    { ok: false, text: 'y ＝ 12/x：y 隨 x 增大而減小', note: '漏咗「每一支上」四個字' },
    { ok: true,  text: 'y ＝ 12/x：每一支上，y 隨 x 增大而減小', note: '講齊先至啱' },
    { ok: false, text: '雙曲線會經過原點', note: 'x ≠ 0、y ≠ 0，永遠唔掂原點同坐標軸' },
    { ok: false, text: 'y ＝ x/5 係反比例函數', note: 'x 走咗上分子，呢個係正比例' },
  ],
});

d.eqJudge({
  title: '快速辨識：係唔係？k 幾多？',
  rows: [
    { parts: ['y ＝ ', { n: '7', d: 'x' }],  ok: true,
      note: 'k ＝ 7 ＞ 0　→　第一、三象限' },
    { parts: ['y ＝ ', { n: 'x', d: '7' }],  ok: false,
      note: 'x 喺分子　→　唔係反比例函數' },
    { parts: ['xy ＝ −5'],                    ok: true,
      note: '改寫成 y ＝ −5/x，k ＝ −5　→　第二、四象限' },
    { parts: ['y ＝ ', { n: '0', d: 'x' }],  ok: false,
      note: 'k ＝ 0，唔符合 k ≠ 0' },
  ],
  badge: '下一頁：綜合題',
});

// ── 綜合題：同一次函數交點 ──────────────────────────
d.problem({
  title: '綜合題：兩條線交埋',
  question: 'y ＝ k/x 同 y ＝ x ＋ 2 交於點 (1, m)。求 k 同 m。',
  sub: '交點 ＝ 兩條線都經過嘅點，\n所以 (1, m) 兩條式都要成立。',
  caption: '先用簡單嗰條求 m，再用 m 求 k。',
  badge: '一齊試：m 應該係幾多？',
});

d.scaffold4({
  title: '交點四步',
  steps: [
    '交點喺兩條線上面，兩條式都要成立',
    '揀簡單嗰條先代（通常係一次函數）',
    '計出未知嘅坐標',
    '再代入另一條，求 k',
  ],
  note: '呢四步同 L4 嘅「設 → 代入 → 解 → 寫返」係同一套思路。',
});

d.problem({
  title: '找錯題',
  question: '小明話：「y ＝ 12/x，x 越嚟越細，最後會掂到原點。」',
  sub: 'x ＝ 1　→　y ＝ 12\nx ＝ 0.1　→　y ＝ 120',
  caption: 'x 越細，y 反而越衝越大，離原點越嚟越遠。x ＝ 0 更加計唔到。',
});

d.layered({
  title: '綜合練習：揀一層',
  cols: [
    { stars: '★☆☆', head: '練習 A',
      lines: ['y ＝ −4/x', '', '(1) k ＝ ？', '(2) 第幾象限？', '(3) 每一支上，', '　　y 隨 x 增大', '　　而＿＿？'] },
    { stars: '★★☆', head: '練習 B',
      lines: ['圖像過 (−2, 6)。', '', '(1) 求解析式。', '(2) 矩形面積 ＝ ？', '(3) 點 (3, −4)', '　　喺圖像上嗎？'] },
    { stars: '★★★', head: '練習 C',
      lines: ['y ＝ k/x 同', 'y ＝ x − 1', '交於點 (3, m)。', '', '(1) 求 m 同 k。', '(2) 矩形面積 ＝ ？'] },
  ],
  note: '三層都係同一個單元嘅嘢，唔同嘅只係要接幾多步。',
});

d.summary({
  takeaway: '睇 k：k 決定象限、決定增減、決定矩形面積',
  lines: [
    '1　y ＝ k/x（k ≠ 0），x 一定喺分數線下面',
    '2　k ＞ 0 一、三象限；k ＜ 0 二、四象限',
    '3　講增減先講「每一支上」；矩形面積 ＝ |k|',
  ],
});

d.closing({
  title: '成個單元完成',
  line: '記住兩個字：睇 k。',
  iep: '本單元 L1–L6 為調整支援（Accommodation）：年級標準不變，只調整呈現方式與練習層次。',
});

d.save(path.join(__dirname, '..', '簡報_L6_總複習與分層綜合.pptx'))
  .then((f) => console.log('OK', f));
