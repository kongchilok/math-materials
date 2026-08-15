// build_L2.js — L2 區間記號與定義域（抽離小組 40 分鐘 · SOIL 融合班 deck）
// 三段式：動機 3 頁｜注意 4–11 頁｜行動 12–14 頁　　轉換點：P3、P8、P12
const path = require('path');
const { Deck } = require('../../../01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js');
const { numberLine } = require('./fn_draw.js');

const d = new Deck('區間記號與定義域');

// ── 動機段 ────────────────────────────────────────────────
d.cover({
  title: '區間記號\n與定義域',
  subtitle: '高一數學 · 抽離小組 · 第 2 課（40 分鐘）',
  hook: '帶走一句：睇到根號諗「≥ 0」，睇到分母諗「≠ 0」',
});

d.agenda({
  steps: [
    '「之間」到底包唔包兩頭？',
    '四個區間記號：[ ] 同 ( )',
    '睇到根號、睇到分母，點做',
    '分層練習：揀一層',
  ],
  note: '中間會停兩次，一齊做練習。',
});

d.problem({
  question: '「3 到 7 之間嘅數」，包唔包 3 同 7？',
  sub: '你講「之間」，有人以為包，有人以為唔包 —— 兩個都答得通。',
  caption: '數學唔可以有得拗，所以要有一套寫法：區間記號。',
  badge: '舉手：包定唔包',
});

// ── 注意段 ────────────────────────────────────────────────
d.symbolTiles({
  title: '四個區間記號',
  star: true,
  tiles: [
    { sym: '[3, 7]', symSize: 40, read: '閉區間', meaning: '兩頭都要', eg: '3 ≤ x ≤ 7' },
    { sym: '(3, 7)', symSize: 40, read: '開區間', meaning: '兩頭都唔要', eg: '3 < x < 7' },
    { sym: '[3, 7)', symSize: 40, read: '半開半閉', meaning: '左要，右唔要', eg: '3 ≤ x < 7' },
    { sym: '(3, 7]', symSize: 40, read: '半開半閉', meaning: '左唔要，右要', eg: '3 < x ≤ 7' },
  ],
});

d.figure({
  title: '端點，要定唔要？',
  draw: numberLine({
    from: 1, to: 9, ticks: [3, 7], band: { from: 3, to: 7 },
    marks: [{ x: 3, open: false, label: '要' }, { x: 7, open: true, label: '唔要' }],
    caption: '呢條線畫嘅係 [3, 7)',
  }),
  side: [
    '● 實心＝呢個端點',
    '　 取得到 → 用 [ ]',
    '',
    '○ 空心＝呢個端點',
    '　 取唔到 → 用 ( )',
    '',
    '粗線＝區間包住嘅範圍',
  ],
});

d.compareCards({
  title: '無窮嗰邊，用邊個括號？',
  cards: [
    { ok: false, text: '[2, +∞]', note: '+∞ 唔係一個數，永遠都「取唔到」，唔可以用中括號' },
    { ok: true,  text: '[2, +∞)', note: '2 取得到 → 中括號；+∞ 嗰邊 → 一定圓括號' },
  ],
  badge: '一齊讀一次',
});

d.tableSlide({
  title: '無窮區間五個寫法',
  headers: ['區間寫法', '不等式', '點讀'],
  colW: [3.2, 3.4, 5.5],
  rows: [
    ['[a, +∞)', 'x ≥ a', 'a 到正無窮，a 要'],
    ['(a, +∞)', 'x > a', 'a 到正無窮，a 唔要'],
    ['(−∞, b]', 'x ≤ b', '負無窮到 b，b 要'],
    ['(−∞, b)', 'x < b', '負無窮到 b，b 唔要'],
    ['(−∞, +∞)', '全部實數 R', '成條數線'],
  ],
});

d.layered({
  title: '練習一：區間 ↔ 不等式',
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: ['① 3 ≤ x ≤ 8', '　 寫成區間', '', '② (0, 5)', '　 寫成不等式'] },
    { stars: '★★☆', head: '練習 B', lines: ['① x > −2 寫成區間', '', '② (−∞, 4]', '　 寫成不等式', '', '③ −1 ≤ x < 6', '　 寫成區間'] },
    { stars: '★★★', head: '練習 C', lines: ['① [1, 5) 同 (3, 9]', '　 嘅公共部分，', '　 用區間寫出嚟。'] },
  ],
  note: '做得起 A 就跳上 B、C，三層都係同一個概念。',
  badge: '自己揀一層',
});

d.rows3({
  title: '求定義域：三條規則',
  rows: [
    { icon: '√', term: '有根號', desc: '被開方數要 ≥ 0', egParts: [{ sqrt: 'x+5' }, ' → x + 5 ≥ 0 → x ≥ −5'] },
    { icon: '÷', term: '有分母', desc: '分母唔可以係 0', egParts: ['', { n: '1', d: 'x−1' }, ' → x − 1 ≠ 0 → x ≠ 1'] },
    { icon: '∩', term: '兩樣都有', desc: '兩個條件要同時成立 → 取交集', eg: '兩邊都啱嘅 x 先數得' },
  ],
});

d.scaffold4({
  title: '求定義域四步',
  steps: [
    '睇有冇根號：被開方數 ≥ 0，寫低條件。',
    '睇有冇分母：分母 ≠ 0，寫低條件。',
    '兩個條件擺埋一齊，喺數線上取交集。',
    '用區間記號寫出答案。',
  ],
  note: '呢四步，之後每一題都照咁寫，唔使另外諗格式。',
});

d.figure({
  title: '示範：根號＋分母，兩個條件一齊要',
  star: true,
  eq: ['f(x) = ', { n: { sqrt: 'x+5' }, d: 'x−1' }],
  draw: numberLine({
    from: -7, to: 4, ticks: [-5, 0, 1], band: { from: -5, to: 4 },
    marks: [{ x: -5, open: false, label: '−5 要' }, { x: 1, open: true, label: '1 挖走' }],
    caption: '粗線＝x ≥ −5，喺 1 嗰度挖返個窿',
  }),
  side: [
    '① 根號：x + 5 ≥ 0',
    '　 → x ≥ −5',
    '',
    '② 分母：x − 1 ≠ 0',
    '　 → x ≠ 1',
    '',
    '③ 交集：≥ −5，但要挖走 1',
    '',
    '④ [−5, 1) ∪ (1, +∞)',
  ],
});

// ── 行動段 ────────────────────────────────────────────────
d.layered({
  title: '練習二：求定義域',
  cols: [
    { stars: '★☆☆', head: '練習 A', lines: [
        { eq: ['① f(x) = ', { sqrt: 'x−2' }] }, '',
        { eq: ['② f(x) = ', { n: '1', d: 'x+3' }] },
      ] },
    { stars: '★★☆', head: '練習 B', lines: [
        { eq: ['① f(x) = ', { n: { sqrt: 'x+1' }, d: 'x−4' }] }, '',
        { eq: ['② f(x) = ', { n: '1', d: { sqrt: 'x−5' } }] },
        '　（睇清楚根號喺邊）',
      ] },
    { stars: '★★★', head: '練習 C', lines: [
        { eq: ['① f(x) = ', { sqrt: '6−x' }, ' + ', { n: '1', d: 'x+2' }] }, '',
        '　 兩個條件都要，', '　 最後用區間寫。',
      ] },
  ],
  note: '每題都照四步寫，唔好跳步。',
  badge: '自己揀一層',
});

d.summary({
  takeaway: '睇到根號諗「≥ 0」，睇到分母諗「≠ 0」。',
  lines: [
    '① 兩個條件都有 → 喺數線上取交集',
    '② 端點取得到用 [ ]，取唔到用 ( )',
    '③ +∞ 同 −∞ 永遠用 ( )，因為佢哋唔係數',
  ],
});

d.closing({
  title: '下一課：函數嘅三種樣',
  line: '同一個函數，可以用式子寫、用表格寫、用圖象畫',
  iep: '教學調整（Accommodation）：本簡報加入數線表徵、步驟卡與分層任務，年級學習標準不變。',
});

const out = path.join(__dirname, '..', '簡報_L2_區間記號與定義域.pptx');
d.save(out).then(f => console.log('OK →', f, '| slides:', d.n));
