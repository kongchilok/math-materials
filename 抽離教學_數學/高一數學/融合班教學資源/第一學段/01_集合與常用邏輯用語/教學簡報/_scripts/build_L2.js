// build_L2.js — L2 集合間的基本關係（抽離小組 40 分鐘）
// 三段式：動機 P1–3｜注意 P4–11｜行動 P12–14　轉換點：P6、P12
const path = require('path');
const { Deck, drawSubset } = require('./soil_kit');
const d = new Deck('集合間的基本關係');
const IEP = '教學調整（Accommodation）：本簡報加入圖像表徵、步驟卡與分層任務，年級學習標準不變。';

d.cover({ title:'集合間的\n基本關係', subtitle:'高一數學 · 抽離小組 · 第 2 課（40 分鐘）',
  hook:'帶走一句：睇關係，就睇邊個圈包住邊個' });

d.agenda({ steps:['子集 ⊆','真子集 ⊊','兩個集合相等','空集 ∅'], note:'中間會停低兩次，一齊做練習。' });

d.problem({ question:'「班上所有女生」同「班上所有學生」，邊個包住邊個？',
  sub:'女生　　學生', caption:'一個集合成個喺另一個入面 — 呢個就係「子集」。', star:true });

d.cra({ title:'咩係子集？',
  concrete:{ text:'細籃放入大籃\n\n生果籃放入\n超市貨架' },
  rep:{ draw: drawSubset({ inner:'A', outer:'B', caption:'A 成個喺 B 入面' }) },
  abstract:{ text:'A ⊆ B\n\nA 每個元素\n都喺 B 入面' },
  takeaway:'細圈喺大圈入面 = 子集', star:true });

d.symbolTiles({ title:'兩個符號',
  tiles:[
    { sym:'⊆', read:'包含於',   meaning:'A 每個元素都喺 B', eg:'{1, 2} ⊆ {1, 2, 3}' },
    { sym:'⊊', read:'真包含於', meaning:'A ⊆ B 但 A ≠ B',   eg:'{1, 2} ⊊ {1, 2, 3}' },
  ], star:true });

d.compareCards({ title:'∈ 定 ⊆？睇左邊係乜',
  cards:[
    { ok:true,  text:'2 ∈ {1, 2, 3}',   note:'2 係一粒元素 — 元素用 ∈' },
    { ok:false, text:'2 ⊆ {1, 2, 3}',   note:'2 唔係集合，唔可以用 ⊆' },
    { ok:true,  text:'{2} ⊆ {1, 2, 3}', note:'{2} 係一個集合 — 集合用 ⊆' },
  ], badge:'一齊讀：∈ 屬於、⊆ 包含於', star:true });

d.rows3({ title:'三條要記嘅規則',
  rows:[
    { term:'自己', icon:'自', desc:'任何集合都係自己嘅子集', eg:'A ⊆ A' },
    { term:'空集', icon:'空', desc:'空集係任何集合嘅子集',   eg:'∅ ⊆ A' },
    { term:'相等', icon:'等', desc:'互相包含，即係相等',     eg:'A ⊆ B 而且 B ⊆ A，即 A = B' },
  ] });

d.compare2({ title:'子集 同 真子集，差喺邊？',
  left: { head:'子集 A ⊆ B',   lines:['A 每個元素都喺 B','','可以 A = B','','例：{1, 2} ⊆ {1, 2}'] },
  right:{ head:'真子集 A ⊊ B', lines:['A ⊆ B 但 A ≠ B','','B 至少多一個元素','','例：{1, 2} ⊊ {1, 2, 3}'] },
  note:'真子集 = 子集，而且唔相等', star:true });

d.compareCards({ title:'空集 ∅，最易撈亂',
  cards:[
    { ok:false, text:'{0} 係空集',   note:'{0} 有一個元素 0，唔算空' },
    { ok:true,  text:'∅ 冇任何元素', note:'一粒都冇，先叫空集' },
  ] });

d.scaffold4({ title:'判斷 A ⊆ B，四步走',
  steps:[
    '寫低 A 同 B 全部元素',
    '由 A 第一個元素開始，逐個 check',
    '每個都喺 B 入面 → A ⊆ B',
    '再睇 B 有冇多出 → 有就係 ⊊',
  ], note:'之後做練習，照住呢四步行。' });

d.tableSlide({ title:'{1, 2} 嘅所有子集',
  headers:['子集','係咪真子集？','點解'],
  rows:[
    ['∅',      '係',   '空集係任何集合嘅子集'],
    ['{1}',    '係',   '少過 {1, 2}'],
    ['{2}',    '係',   '少過 {1, 2}'],
    ['{1, 2}', '唔係', '同 {1, 2} 相等'],
  ], colW:[3.0, 3.3, 5.8], star:true });

d.layered({
  cols:[
    { stars:'★☆☆', head:'練習 A', lines:['判斷啱唔啱：','','{1, 2} ⊆ {1, 2, 3}','','{3} ⊆ {1, 2}'] },
    { stars:'★★☆', head:'練習 B', lines:['寫出 {a, b} 嘅','所有子集：','','（提示：有 4 個）'] },
    { stars:'★★★', head:'練習 C', lines:['{1, 2, 3} 有幾多個','子集？','','試搵出規律'] },
  ], note:'做完 A 想再試，就上 B、C — 自己揀就得。', badge:'揀一層，開始做', star:true });

d.summary({ takeaway:'睇關係，就睇邊個圈\n包住邊個圈',
  lines:['① ⊆ 讀「包含於」：細圈喺大圈入面','② ⊊ 真子集：包含，但唔相等','③ ∅ 係任何集合嘅子集'], star:true });

d.closing({ title:'你今日識咗睇集合嘅關係', line:'落堂前講一次：⊆ 讀「包含於」', iep:IEP });

d.save(path.join(__dirname, '..', '簡報_L2_集合間的基本關係.pptx')).then(f => console.log('OK →', f));
