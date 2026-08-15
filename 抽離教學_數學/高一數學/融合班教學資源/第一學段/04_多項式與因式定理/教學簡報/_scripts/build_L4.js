// build_L4.js — L4 因式定理（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 三段式：動機 1–3 頁｜注意 4–11 頁｜行動 12–14 頁　轉換點：P6、P9、P12
const path = require('path');
const { Deck } = require('./soil_kit');

const d = new Deck('因式定理');

// ── 動機段 ───────────────────────────────────────────────
d.cover({
  title: '因式定理',
  subtitle: '高一數學 · 抽離小組 · 第 4 課（40 分鐘）',
  hook: '帶走一句：f(c) = 0，即係 (x−c) 係因式',
});

d.agenda({
  steps: [
    '餘數啱啱好係 0 嘅時候',
    '因式定理：三句同一件事',
    '反過嚟用：求未知係數',
    '自己揀一層做練習',
  ],
  note: '中間會停低三次，一齊做。',
});

d.problem({
  question: '上一課：f(x) ÷ (x−a) 嘅餘數 = f(a)。',
  sub: '咁如果餘數啱啱好係 0 呢？',
  caption: '餘數 0 = 整除 = 除得盡。呢個情況特別有用。',
  star: true,
});

// ── 注意段 ───────────────────────────────────────────────
d.cra({
  title: '餘數係 0，代表咩',
  concrete: { text: '12 ÷ 3 = 4 餘 0\n\n所以 3 係 12\n嘅一個因數' },
  rep:      { text: '12 = 3 × 4\n\n完全冇剩\n\n拆得開，冇尾巴' },
  abstract: { text: 'f(c) = 0\n\nf(x) = (x−c)·q(x)\n\n(x−c) 係因式' },
  takeaway: '餘數係 0，就代表除得盡、拆得開',
  star: true,
});

d.rows3({
  title: '因式定理：三句其實同一件事',
  rows: [
    { term: '講法一', icon: '1', desc: '(x−c) 係 f(x) 嘅因式', eg: '拆得出 (x−c) 呢嚿' },
    { term: '講法二', icon: '2', desc: 'f(x) 被 (x−c) 整除',   eg: '餘數 = 0' },
    { term: '講法三', icon: '3', desc: 'f(c) = 0',             eg: '代 c 入去計到 0' },
  ],
  badge: '一齊讀一次三句',
});

d.compare2({
  title: '餘式定理 vs 因式定理',
  left:  { head: '餘式定理', lines: ['問：餘數係幾多？', '', '答：f(a)', '', '任何數都得', '', '例：f(2) = −5 → 餘 −5'] },
  right: { head: '因式定理', lines: ['問：係唔係因式？', '', '睇 f(c) 係咪 0', '', '要啱啱好係 0', '', '例：f(2) = 0 → (x−2) 係因式'] },
  note: '因式定理 = 餘式定理入面「餘數 = 0」嗰個特殊情況',
  star: true,
  badge: '一齊講一次分別',
});

d.compareCards({
  title: '(x−1) 係唔係 f(x) 嘅因式？',
  cards: [
    { ok: true,  text: 'f(x) = x^{2}−3x+2，f(1) = 0', note: '1−3+2 = 0　→　係因式' },
    { ok: false, text: 'f(x) = x^{2}+3x+2，f(1) = 6', note: '1+3+2 = 6，唔係 0　→　唔係因式' },
  ],
  star: true,
  badge: '再一頁就反過嚟用',
});

d.problem({
  title: '反過嚟用',
  question: 'f(x) = x^{3}+px^{2}+qx−6\n有因式 (x−1) 同 (x−2)，求 p、q',
  sub: '今次唔係問你係唔係因式 —— 而係已經知係因式，反過嚟求未知數。',
  caption: '兩個因式 → 兩條式 → 兩個未知數，啱啱好夠解。',
  star: true,
});

d.scaffold4({
  title: '求未知係數四步走',
  steps: [
    '每個因式寫一條式\n(x−1) → f(1) = 0\n(x−2) → f(2) = 0',
    '代入，化簡第一條\n1+p+q−6 = 0\n→ p+q = 5',
    '代入，化簡第二條\n8+4p+2q−6 = 0\n→ 2p+q = −1',
    '兩條相減，解方程\n−p = 6 → p = −6\n代返：q = 11',
  ],
  note: '有幾多個因式，就寫幾多條式 —— 未知數有幾多個就要幾多條。',
  badge: '照住四步做一次',
});

d.tableSlide({
  title: '慢鏡：兩條式點嚟',
  headers: ['因式', '代入', '化簡'],
  rows: [
    ['(x−1)', 'f(1) = 1+p+q−6 = 0',   'p + q = 5'],
    ['(x−2)', 'f(2) = 8+4p+2q−6 = 0', '2p + q = −1'],
  ],
  colW: [2.2, 5.5, 4.4],
  star: true,
});

d.compareCards({
  title: '答案檢查：代返入去係咪 0？',
  cards: [
    { ok: true, text: 'p = −6，q = 11',        note: 'f(x) = x^{3}−6x^{2}+11x−6' },
    { ok: true, text: 'f(1) = 1−6+11−6 = 0',   note: '✓ (x−1) 真係因式' },
    { ok: true, text: 'f(2) = 8−24+22−6 = 0',  note: '✓ (x−2) 真係因式' },
  ],
  badge: '再一頁就落手做',
});

d.rows3({
  title: '最容易錯嘅三個位',
  rows: [
    { term: '搞錯號', icon: '1', desc: '(x+2) 要代 −2，唔係 2',   eg: '永遠令括號入面 = 0' },
    { term: '未化簡', icon: '2', desc: '代完要整理成 p、q 嘅式',  eg: '唔化簡好難相減' },
    { term: '冇檢查', icon: '3', desc: '解完要代返入去驗',        eg: '應該計到 0' },
  ],
});

// ── 行動段 ───────────────────────────────────────────────
d.layered({
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['f(x) = x^{2}−3x+2', '', 'f(1) = ___', '', '(x−1) 係唔係因式？'] },
    { stars: '★★☆', head: '練習 B', lines: ['f(x) = x^{3}−4x^{2}+x+6', '', '驗證 (x−2)', '係唔係因式'] },
    { stars: '★★★', head: '練習 C', lines: ['f(x) = x^{3}+ax^{2}−4x+b', '', '有因式 (x−1)', '同 (x+2)', '', '求 a、b'] },
  ],
  note: '做完 A 想再試，就上 B、C —— 自己揀就得。',
  badge: '揀一層，開始做',
  star: true,
});

d.summary({
  takeaway: 'f(c) = 0\n即係 (x−c) 係因式',
  lines: [
    '① 因式定理 = 餘式定理嘅「餘 0」情況',
    '② 一個因式寫一條式，代入令佢 = 0',
    '③ 解完一定要代返入去檢查',
  ],
  star: true,
});

d.closing({
  title: '你今日識咗點樣拆多項式',
  line: '落堂前，同隔離位講一次：f(c) = 0，即係 (x−c) 係因式',
  iep: '教學調整（Accommodation）：本簡報加入具體表徵、步驟卡與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L4_因式定理.pptx');
d.save(out).then(f => console.log('OK →', f));
