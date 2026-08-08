// build_L4.js — L4 反函數：概念（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 呢一課刻意唔教求法，淨係做「撤銷」嘅體驗。求法留到 L5。
// 三段式：動機 3 頁｜注意 4–9 頁｜行動 10 頁　　轉換點：P7、P10
const path = require('path');
const { Deck } = require('../../../01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js');
const { axes, undoChain } = require('./exp_draw.js');

const d = new Deck('反函數：概念');

// ── 動機段 ────────────────────────────────────────────────
d.cover({
  title: '反函數\n（概念）',
  subtitle: '高一數學 · 抽離小組 · 第 4 課（40 分鐘）',
  hook: '帶走一句：反函數就係「撤銷」，唔係「一除」',
});

d.agenda({
  steps: [
    '著鞋同除鞋',
    'f 做一次，f^{-1} 撤銷返',
    '點對調：(2, 5) 變 (5, 2)',
    '分層練習：揀一層',
  ],
  note: '今日淨係認概念，下一課先教點求。中間停兩次。',
});

d.problem({
  question: '著鞋、除鞋，係咪一對「相反」嘅動作？',
  sub: '著咗再除，就返返赤腳 —— 等於乜都冇做過。',
  caption: '函數都有呢種一對：f 做一次，f^{-1} 撤銷返，就變返原本個 x。',
  badge: '想一想',
});

// ── 注意段 ────────────────────────────────────────────────
d.figure({
  title: 'f 做一次，f^{-1} 撤銷返',
  star: true,
  draw: undoChain({ inLabel: 'x', mid: 'y', outLabel: '返返 x',
    box1: 'f', box2: 'f^{-1}', caption: '兩部機串埋一齊，等於乜都冇做過' }),
  side: [
    '例：f(x) = 2x + 1',
    '',
    'x = 1 入去',
    '　→ f(1) = 3',
    '',
    '3 入 f^{-1}',
    '　→ 返返 1',
  ],
});

d.cra({
  title: '「撤銷」三個講法',
  concrete: { text: '著鞋 → 除鞋\n\n上鎖 → 開鎖\n\n加密 → 解密\n\n做完再撤銷，\n返到原點。' },
  rep: {
    draw: axes({
      xr: [-1, 6], yr: [-1, 6], xticks: [2, 5], yticks: [2, 5],
      segs: [{ x1: -1, y1: -1, x2: 6, y2: 6, dash: true, head: false }],
      pts: [{ x: 2, y: 5, label: '(2, 5)' }, { x: 5, y: 2, label: '(5, 2)' }],
      labels: [{ x: 4.6, y: 5.4, text: 'y = x' }],
    }),
    text: '兩點照鏡',
  },
  abstract: { text: 'f(2) = 5\n\n所以\n\nf^{-1}(5) = 2\n\n入同出，\n啱啱調轉。' },
  takeaway: '同一句嘢：f 入 2 出 5，f^{-1} 就係入 5 出 2。',
});

d.rows3({
  title: '反函數三條性質',
  rows: [
    { icon: '①', term: '點對調', desc: '(a, b) 喺 f 上 → (b, a) 喺 f^{-1} 上', eg: 'f(2) = 5　→　f^{-1}(5) = 2' },
    { icon: '②', term: '定義域值域互換', desc: 'f 嘅值域 = f^{-1} 嘅定義域', eg: '出去嗰堆數，變咗入嚟嗰堆' },
    { icon: '③', term: '圖象對稱', desc: '兩條線關於直線 y = x 對稱', eg: '摺住 y = x 對摺，兩條線會疊實' },
  ],
});

d.layered({
  title: '練習一：讀得出就得',
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['① 已知 f(1) = 3，', '　 求 f^{-1}(3)。', '', '② 已知 f(4) = 0，', '　 求 f^{-1}(0)。'] },
    { stars: '★★☆', head: '練習 B', lines: ['① (2, 5) 喺 f 上，', '　 咁 (5, 2) 係咪', '　 喺 f^{-1} 上？', '', '② f(x) = x/2，', '　 求 f^{-1}(4)。'] },
    { stars: '★★★', head: '練習 C', lines: ['① f(x) = x^{3}，', '　 求佢反函數', '　 嘅值域。', '', '② 講吓你點知。'] },
  ],
  note: '唔使求條式，淨係用「入同出調轉」就答得到。',
  badge: '自己揀一層',
});

d.figure({
  title: '兩條線關於 y = x 對稱',
  star: true,
  draw: axes({
    xr: [-2, 5], yr: [-2, 5], xticks: [1, 3], yticks: [1, 3],
    segs: [{ x1: -2, y1: -2, x2: 5, y2: 5, dash: true, head: false }],
    curves: [
      { f: (x) => 2 * x + 1, from: -1.5, to: 2 },
      { f: (x) => (x - 1) / 2, from: -2, to: 5 },
    ],
    labels: [
      { x: 1.4, y: 4.4, text: 'f' },
      { x: 4.3, y: 2.4, text: 'f 反' },
      { x: 3.4, y: 4.6, text: 'y = x' },   // 抬高離開虛線，唔好壓住
    ],
  }),
  side: [
    '虛線係 y = x',
    '',
    '兩條實線',
    '　照住虛線對摺，',
    '　會啱啱疊實。',
    '',
    '呢個就係「對調」',
    '喺圖上面嘅樣。',
  ],
});

d.compareCards({
  title: '全單元最易搞錯嗰個',
  cards: [
    { ok: false, text: 'f^{-1}(x) 即係 1 / f(x)', note: '個 −1 唔係次方，唔係「一除」。佢淨係一個記號，讀「f 反」' },
    { ok: true, text: 'f^{-1} 讀「f 反」，解「撤銷 f」', note: 'f 入 2 出 5，f^{-1} 就入 5 出 2' },
    { ok: false, text: 'f(2) = 5 所以 f^{-1}(2) = 5', note: '要調轉：f^{-1}(5) = 2 先啱' },
  ],
  badge: '一齊讀出聲',
});

// ── 行動段 ────────────────────────────────────────────────
d.layered({
  title: '練習二：講得出點解',
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['① f^{-1} 讀咩？', '', '② 佢係咪 1/f？'] },
    { stars: '★★☆', head: '練習 B', lines: ['① 點 (3, 7) 喺 f 上，', '　 f^{-1} 上有邊點？', '', '② f 嘅定義域係', '　 f^{-1} 嘅乜？'] },
    { stars: '★★★', head: '練習 C', lines: ['① y = a^{x} 同', '　 y = log_{a}x', '　 互為反函數。', '', '② 若 y = a^{x} 過 (1, 2)，', '　 求 a。'] },
  ],
  note: '答唔到就返去睇「著鞋除鞋」嗰張圖。',
  badge: '自己揀一層',
});

d.summary({
  takeaway: '反函數就係「撤銷」，唔係「一除」。',
  lines: [
    '① f 入 a 出 b → f^{-1} 入 b 出 a，啱啱調轉',
    '② f 嘅值域，變咗 f^{-1} 嘅定義域',
    '③ 兩條線關於 y = x 對稱，對摺會疊實',
  ],
});

d.closing({
  title: '下一課：點樣求反函數',
  line: '今日識咗佢係咩；下一課用四步，真係求返條式出嚟',
  iep: '教學調整（Accommodation）：本簡報加入生活撤銷情境、對稱圖象與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L4_反函數概念.pptx');
d.save(out).then(f => console.log('OK →', f, '| slides:', d.n));
