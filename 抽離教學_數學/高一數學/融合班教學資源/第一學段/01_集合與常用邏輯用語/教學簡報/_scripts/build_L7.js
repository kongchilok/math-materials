// build_L7.js — L7 命題的否定（抽離小組 40 分鐘）
const path = require('path');
const { Deck } = require('./soil_kit');
const d = new Deck('命題的否定');
const IEP = '教學調整（Accommodation）：本簡報加入圖像表徵、步驟卡與分層任務，年級學習標準不變。';

d.cover({ title:'命題的否定', subtitle:'高一數學 · 抽離小組 · 第 7 課（40 分鐘）',
  hook:'帶走一句：否定 = 換量詞 ＋ 否定結論' });

d.agenda({ steps:['咩係否定','∀ 嘅否定變 ∃','∃ 嘅否定變 ∀','兩步走，寫否定'],
  note:'中間會停低兩次，一齊做練習。' });

d.problem({ question:'「班上所有同學都帶咗書」唔啱。噉即係點？',
  sub:'所有人都帶　→　唔啱',
  caption:'即係「至少有一個人冇帶」— 呢個就係否定。', star:true });

d.compare2({ title:'兩條否定規則',
  left: { head:'∀ 嘅否定 → ∃', lines:['原：∀x ∈ M, p(x)','','否定：∃x ∈ M, ¬p(x)','','「全部啱」→「有一個唔啱」'] },
  right:{ head:'∃ 嘅否定 → ∀', lines:['原：∃x ∈ M, p(x)','','否定：∀x ∈ M, ¬p(x)','','「有一個啱」→「全部都唔啱」'] },
  note:'兩步：① 換量詞　② 否定結論', star:true });

d.scaffold4({ title:'寫否定，四步走',
  steps:[
    '睇清楚原命題係 ∀ 定 ∃',
    '換量詞：∀ 換 ∃，∃ 換 ∀',
    '否定結論：p(x) 變 ¬p(x)',
    '讀一次，check 意思啱唔啱',
  ], badge:'一齊試一次', star:true });

d.tableSlide({ title:'結論點否定？',
  headers:['原本','否定','例'],
  rows:[
    ['係', '唔係', 'x 係偶數　→　x 唔係偶數'],
    ['>',  '≤',    'x > 3　→　x ≤ 3'],
    ['<',  '≥',    'x < 3　→　x ≥ 3'],
    ['=',  '≠',    'x = 2　→　x ≠ 2'],
  ], colW:[2.4, 2.4, 7.3], star:true });

d.problem({ title:'一齊做：例題',
  question:'寫出「所有素數都係奇數」嘅否定',
  sub:'原命題：∀x ∈ 素數, x 係奇數',
  caption:'提示：換量詞，再否定結論。' });

d.scaffold4({ title:'例題解答，四步走',
  steps:[
    '原命題係 ∀（所有）',
    '換量詞：∀ 換做 ∃',
    '否定結論：「係奇數」變「唔係奇數」',
    '否定：存在一個素數唔係奇數',
  ], note:'呢個否定係真命題 — 2 就係噉嘅例子。', star:true });

d.compareCards({ title:'最易寫錯嘅否定',
  cards:[
    { ok:false, text:'否定係「所有素數都唔係奇數」', note:'量詞冇換 — 變咗另一句，唔係否定' },
    { ok:true,  text:'否定係「存在一個素數唔係奇數」', note:'換咗量詞，又否定咗結論' },
    { ok:false, text:'x > 3 嘅否定係 x < 3', note:'漏咗 x = 3 — 應該係 x ≤ 3' },
  ], star:true });

d.tableSlide({ title:'完整例子',
  headers:['原命題','否定'],
  rows:[
    ['∀x ∈ R, x^{2} ≥ 0',   '∃x ∈ R, x^{2} < 0'],
    ['∃x ∈ R, x + 1 = 0',   '∀x ∈ R, x + 1 ≠ 0'],
    ['∀x ∈ N, x > 0',       '∃x ∈ N, x ≤ 0'],
  ], colW:[6.05, 6.05], star:true });

d.problem({ title:'一個重要特性',
  question:'原命題同佢嘅否定，可唔可以同時真？',
  sub:'例：∀x ∈ R, x^{2} ≥ 0（真）\n否定：∃x ∈ R, x^{2} < 0（假）',
  caption:'一個真，另一個一定假 — 呢個就係否定嘅特性。' });

d.layered({
  cols:[
    { stars:'★☆☆', head:'練習 A', lines:['寫出否定：','','∀x ∈ R, x > 0','','（換量詞 ＋ 否定）'] },
    { stars:'★★☆', head:'練習 B', lines:['寫出否定：','','∃x ∈ N, x^{2} = 4','','再判斷否定真假'] },
    { stars:'★★★', head:'練習 C', lines:['寫出否定並判真假：','','∀x ∈ R, x^{2} > x'] },
  ], note:'做完 A 想再試，就上 B、C — 自己揀就得。', badge:'揀一層，開始做', star:true });

d.summary({ takeaway:'否定 = 換量詞\n＋ 否定結論',
  lines:['① ∀ 嘅否定變 ∃，∃ 嘅否定變 ∀','② 結論要一齊否定（> 變 ≤）','③ 原命題係真，否定就一定係假'], star:true });

d.closing({ title:'你今日識咗寫命題嘅否定', line:'落堂前講一次：換量詞，再否定結論', iep:IEP });

d.save(path.join(__dirname, '..', '簡報_L7_命題的否定.pptx')).then(f => console.log('OK →', f));
