// build_L4.js — L4 補集與運算性質（抽離小組 40 分鐘）
// 注意：補集寫法用 `∁_{U}A`（真排版下標）。Unicode 下標字元 ᵤ 三大字型皆無，會出豆腐。
const path = require('path');
const { Deck, drawComplement } = require('./soil_kit');
const d = new Deck('補集與運算性質');
const IEP = '教學調整（Accommodation）：本簡報加入圖像表徵、步驟卡與分層任務，年級學習標準不變。';

d.cover({ title:'補集與\n運算性質', subtitle:'高一數學 · 抽離小組 · 第 4 課（40 分鐘）',
  hook:'帶走一句：補集 = 全集入面，唔係佢嘅嗰啲' });

d.agenda({ steps:['全集 U','補集 ∁_{U}A','補集嘅性質','綜合運算'], note:'中間會停低兩次，一齊做練習。' });

d.problem({ question:'唔識游水嘅有幾多人？',
  sub:'全班 30 人　　識游水 18 人',
  caption:'喺「全班」入面，唔係嗰堆 — 呢個就係「補集」。', star:true });

d.cra({ title:'咩係補集？',
  concrete:{ text:'全班 30 人\n\n識游水 18 人\n唔識嘅 12 人' },
  rep:{ draw: drawComplement({ a:'A', u:'U', caption:'塗色部分 = ∁_{U}A' }) },
  abstract:{ text:'∁_{U}A\n\n= U 入面\n唔屬於 A 嘅' },
  takeaway:'補集 = 全集減走 A，剩低嘅', star:true });

d.symbolTiles({ title:'兩個要識嘅字',
  tiles:[
    { sym:'U',        read:'全集', meaning:'而家討論緊嘅全部', eg:'U = {1, 2, 3, 4, 5, 6}' },
    { sym:'∁_{U}A', symSize:64, read:'補集', meaning:'U 入面唔係 A 嗰啲', eg:'A = {1, 2} 時\n∁_{U}A = {3, 4, 5, 6}' },
  ], star:true });

d.scaffold4({ title:'求補集，四步走',
  steps:[
    '寫低全集 U 全部元素',
    '寫低 A 全部元素',
    '喺 U 度劃走 A 嘅元素',
    '剩低嘅就係 ∁_{U}A',
  ], badge:'一齊做一次補集' });

d.tableSlide({ title:'例：U = {1, 2, 3, 4, 5, 6}',
  headers:['集合','元素','點得出'],
  rows:[
    ['A',        '{1, 2, 3}', '題目俾'],
    ['∁_{U}A',   '{4, 5, 6}', 'U 減走 A'],
    ['B',        '{2, 3, 4}', '題目俾'],
    ['∁_{U}B',   '{1, 5, 6}', 'U 減走 B'],
  ], colW:[2.8, 4.3, 5.0], star:true });

d.compareCards({ title:'冇全集，就求唔到補集',
  cards:[
    { ok:false, text:'∁_{U}A = 所有唔係 A 嘅嘢', note:'冇講明全集 U，範圍無限 — 答唔到' },
    { ok:true,  text:'先講明 U，再喺 U 入面減走 A', note:'同一個 A，U 唔同，補集就唔同' },
  ], star:true });

d.tableSlide({ title:'補集嘅性質',
  headers:['算式','結果','點解'],
  rows:[
    ['A ∪ ∁_{U}A', 'U', 'A 同佢嘅補集，合埋就係全部'],
    ['A ∩ ∁_{U}A', '∅', '冇嘢可以又係 A、又唔係 A'],
    ['∁_{U}U',     '∅', '全集嘅補集，乜都冇剩'],
    ['∁_{U}∅',     'U', '空集嘅補集，就係全部'],
  ], colW:[3.2, 1.8, 7.1], star:true });

d.problem({ title:'一齊做：綜合運算',
  question:'求 ∁_{U}(A ∪ B)',
  sub:'U = {1, 2, 3, 4, 5, 6}\nA = {1, 2, 3}　　B = {2, 3, 4}',
  caption:'提示：先做括號入面嘅 A ∪ B，再求補集。' });

d.scaffold4({ title:'綜合運算，四步走',
  steps:[
    '睇清楚括號：先做 A ∪ B',
    'A ∪ B = {1, 2, 3, 4}',
    '喺 U 度劃走呢四個',
    '答案：∁_{U}(A ∪ B) = {5, 6}',
  ], note:'之後做練習，照住呢四步行。', star:true });

d.layered({
  cols:[
    { stars:'★☆☆', head:'練習 A', lines:['U = {1, 2, 3, 4, 5}','A = {1, 2}','','求 ∁_{U}A'] },
    { stars:'★★☆', head:'練習 B', lines:['U = {1, 2, 3, 4, 5, 6}','A = {2, 4, 6}','','求 ∁_{U}A'] },
    { stars:'★★★', head:'練習 C', lines:['U = {1, 2, 3, 4, 5}','A = {1, 2}','B = {2, 3}','','求 ∁_{U}(A ∪ B)'] },
  ], note:'做完 A 想再試，就上 B、C — 自己揀就得。', badge:'揀一層，開始做', star:true });

d.summary({ takeaway:'補集 = 喺全集入面\n減走 A，剩低嘅',
  lines:['① 冇講明全集 U，就求唔到補集','② A ∪ ∁_{U}A = U（合埋就係全部）','③ A ∩ ∁_{U}A = ∅（冇重疊）'], star:true });

d.closing({ title:'你今日識咗喺全集入面搵剩低嘅', line:'落堂前講一次：補集 = 全集減走佢', iep:IEP });

d.save(path.join(__dirname, '..', '簡報_L4_補集與運算性質.pptx')).then(f => console.log('OK →', f));
