// build_L6.js — L6 全稱量詞與存在量詞（判真假）（抽離小組 40 分鐘）
const path = require('path');
const { Deck } = require('./soil_kit');
const d = new Deck('全稱量詞與存在量詞');
const IEP = '教學調整（Accommodation）：本簡報加入圖像表徵、步驟卡與分層任務，年級學習標準不變。';

d.cover({ title:'全稱量詞與\n存在量詞', subtitle:'高一數學 · 抽離小組 · 第 6 課（40 分鐘）',
  hook:'帶走一句：∀ 要全部啱，∃ 有一個就夠' });

d.agenda({ steps:['全稱量詞 ∀','存在量詞 ∃','判斷全稱命題真假','判斷存在命題真假'],
  note:'中間會停低兩次，一齊做練習。' });

d.problem({ question:'邊一句比較難成立？',
  sub:'①「班上所有同學都帶咗書」\n②「班上有同學帶咗書」',
  caption:'「所有」同「有啲」，要求差好遠。', star:true });

d.symbolTiles({ title:'兩個量詞',
  tiles:[
    { sym:'∀', read:'所有', meaning:'任意一個、每一個', eg:'∀x ∈ M, p(x)' },
    { sym:'∃', read:'存在', meaning:'至少有一個',       eg:'∃x ∈ M, p(x)' },
  ], star:true });

d.compare2({ title:'兩種命題',
  left: { head:'全稱量詞命題 ∀', lines:['「所有」「任意」「每一個」','','∀x ∈ M, p(x)','','M 入面每個都要啱'] },
  right:{ head:'存在量詞命題 ∃', lines:['「存在」「有啲」「至少一個」','','∃x ∈ M, p(x)','','有一個啱就得'] },
  note:'∀ 要全部　　∃ 要一個', badge:'一齊讀：∀ 所有、∃ 存在', star:true });

d.tableSlide({ title:'點判真假？',
  headers:['要判斷','點做','結論'],
  rows:[
    ['∀ 命題係真', '逐個 x 檢查，全部都啱', '先可以話真'],
    ['∀ 命題係假', '搵到一個反例',         '即刻判假'],
    ['∃ 命題係真', '搵到一個例子',         '即刻判真'],
    ['∃ 命題係假', '逐個檢查，全部都唔啱', '先可以話假'],
  ], colW:[3.2, 4.9, 4.0], star:true });

d.scaffold4({ title:'判斷全稱命題，四步走',
  steps:[
    '睇清楚範圍 M 同性質 p(x)',
    '試搵一個反例',
    '搵到反例 → 命題係假',
    '搵唔到，逐個都啱 → 命題係真',
  ], note:'全稱命題最快嘅做法：先試搵反例。' });

d.problem({ title:'一齊做：例題',
  question:'「所有素數都係奇數」係真定假？',
  sub:'素數：2, 3, 5, 7, 11, …',
  caption:'提示：試搵一個反例。' });

d.scaffold4({ title:'例題解答，四步走',
  steps:[
    'M = 所有素數，p(x)：x 係奇數',
    '試反例：2 係素數',
    '但 2 唔係奇數 → 搵到反例',
    '結論：原命題係假命題',
  ], star:true });

d.compareCards({ title:'一個例子，證到啲乜？',
  cards:[
    { ok:false, text:'搵到一個例子，就證到 ∀ 命題係真', note:'∀ 要全部都啱，一個唔夠' },
    { ok:true,  text:'搵到一個反例，就證到 ∀ 命題係假', note:'∀ 只要一個唔啱就冧' },
    { ok:true,  text:'搵到一個例子，就證到 ∃ 命題係真', note:'∃ 一個就夠' },
  ], star:true });

d.problem({ title:'再試一題',
  question:'「∃x ∈ R, x^{2} < 0」係真定假？',
  sub:'即係：存在一個實數 x，令 x^{2} < 0',
  caption:'提示：∃ 要係假，就要每一個 x 都唔啱。' });

d.layered({
  cols:[
    { stars:'★☆☆', head:'練習 A', lines:['判斷真假：','','∀x ∈ R, x^{2} ≥ 0','','（真定假？）'] },
    { stars:'★★☆', head:'練習 B', lines:['判斷真假：','','∃x ∈ R, x + 1 = 0','','真嘅話寫出 x'] },
    { stars:'★★★', head:'練習 C', lines:['判斷真假並解釋：','','∀x ∈ N, x^{2} > x','','（提示：試細數）'] },
  ], note:'做完 A 想再試，就上 B、C — 自己揀就得。', badge:'揀一層，開始做', star:true });

d.summary({ takeaway:'∀ 要全部啱\n∃ 有一個就夠',
  lines:['① ∀ 讀「所有」，∃ 讀「存在」','② 全稱要判假：搵一個反例就夠','③ 存在要判真：搵一個例子就夠'], star:true });

d.closing({ title:'你今日識咗分「所有」同「有啲」', line:'落堂前講一次：∀ 全部，∃ 一個', iep:IEP });

d.save(path.join(__dirname, '..', '簡報_L6_全稱量詞與存在量詞.pptx')).then(f => console.log('OK →', f));
