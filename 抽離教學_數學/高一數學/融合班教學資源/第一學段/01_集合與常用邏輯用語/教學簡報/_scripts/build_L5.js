// build_L5.js — L5 充分條件與必要條件（抽離小組 40 分鐘）
// 注意：避開 ⇏（三大字型皆無），改用文字「推唔返轉頭」。
const path = require('path');
const { Deck, drawSubset } = require('./soil_kit');
const d = new Deck('充分條件與必要條件');
const IEP = '教學調整（Accommodation）：本簡報加入圖像表徵、步驟卡與分層任務，年級學習標準不變。';

d.cover({ title:'充分條件與\n必要條件', subtitle:'高一數學 · 抽離小組 · 第 5 課（40 分鐘）',
  hook:'帶走一句：p ⇒ q，就係 P 圈喺 Q 圈入面' });

d.agenda({ steps:['咩係命題','p ⇒ q 點讀','充分同必要，點分','用圖去睇'], note:'中間會停低兩次，一齊做練習。' });

d.problem({ question:'地濕，係咪一定落過雨？',
  sub:'落雨　→　地濕　　　地濕　→　？',
  caption:'有啲關係係單向嘅 — 呢個就係充分同必要嘅分別。', star:true });

d.rows3({ title:'先講清楚三個字',
  rows:[
    { term:'命題', icon:'命', desc:'可以判斷真假嘅句子', eg:'「2 > 1」係命題；「今日好熱」唔係' },
    { term:'條件', icon:'p', desc:'寫成「若 p，則 q」', eg:'p 係條件，q 係結論' },
    { term:'推出', icon:'⇒', desc:'p 成立，q 就一定成立', eg:'記作 p ⇒ q' },
  ] });

d.cra({ title:'p ⇒ q 其實係咩樣？',
  concrete:{ text:'係香港人\n⇒ 係中國人\n\n但係中國人\n唔一定係香港人' },
  rep:{ draw: drawSubset({ inner:'P', outer:'Q', caption:'P 圈喺 Q 圈入面' }) },
  abstract:{ text:'p ⇒ q\n\n對應 P ⊆ Q' },
  takeaway:'p ⇒ q，就係 P 圈喺 Q 圈入面', star:true });

d.compare2({ title:'同一個 p ⇒ q，兩個叫法',
  left: { head:'p 係充分條件', lines:['有咗 p，就夠保證 q','','p ⇒ q','','「有 p 就夠」'] },
  right:{ head:'q 係必要條件', lines:['冇咗 q，就一定冇 p','','p ⇒ q','','「冇 q 就唔掂」'] },
  note:'前面嗰個叫充分，後面嗰個叫必要', badge:'一齊讀一次', star:true });

d.scaffold4({ title:'判斷條件，四步走',
  steps:[
    '寫清楚 p 同 q 分別係乜',
    '試 p ⇒ q：p 成立時 q 係咪一定成立',
    '試 q ⇒ p：試搵反例推翻',
    '下結論：充分／必要／充要',
  ], note:'兩個方向都要試，唔可以齋試一邊。' });

d.problem({ title:'一齊做：例題',
  question:'「x = 2」係「x^{2} = 4」嘅乜嘢條件？',
  sub:'p：x = 2　　　q：x^{2} = 4',
  caption:'提示：兩個方向都要試一次。' });

d.scaffold4({ title:'例題解答，四步走',
  steps:[
    'p：x = 2　　q：x^{2} = 4',
    'x = 2 時 x^{2} = 4 成立 → p ⇒ q 真',
    'x^{2} = 4 時，x 可以 = −2\n→ 推唔返轉頭',
    '結論：p 係 q 嘅充分不必要條件',
  ], star:true });

d.compareCards({ title:'方向唔可以掉轉',
  cards:[
    { ok:true,  text:'x = 2 ⇒ x^{2} = 4',   note:'呢個方向啱' },
    { ok:false, text:'x^{2} = 4 ⇒ x = 2',   note:'反例：x = −2 時 x^{2} = 4，但 x ≠ 2' },
    { ok:false, text:'p ⇒ q 即係 q ⇒ p',    note:'兩個方向係兩件事，要分開試' },
  ], star:true });

d.tableSlide({ title:'三種情況，三個叫法',
  headers:['情況','叫法','例'],
  rows:[
    ['p ⇒ q，但推唔返', '充分不必要',   'p：x = 2　q：x^{2} = 4'],
    ['q ⇒ p，但推唔返', '必要不充分',   'p：x^{2} = 4　q：x = 2'],
    ['兩個方向都推到',   '充要 p ⇔ q',  'p：x − 1 = 0　q：x = 1'],
  ], colW:[4.2, 3.0, 4.9], star:true });

d.layered({
  cols:[
    { stars:'★☆☆', head:'練習 A', lines:['判斷真假：','','x = 3 ⇒ x^{2} = 9','','（啱定錯？）'] },
    { stars:'★★☆', head:'練習 B', lines:['p：x = 1','q：x^{2} = 1','','p 係 q 嘅','乜嘢條件？'] },
    { stars:'★★★', head:'練習 C', lines:['搵一個 p，令','p ⇔ x > 2','','（即係充要條件）'] },
  ], note:'做完 A 想再試，就上 B、C — 自己揀就得。', badge:'揀一層，開始做', star:true });

d.summary({ takeaway:'p ⇒ q\n就係 P 圈喺 Q 圈入面',
  lines:['① p ⇒ q：p 係充分，q 係必要','② 方向唔可以掉轉，要另外試一次','③ 兩個方向都推到，就叫充要 p ⇔ q'], star:true });

d.closing({ title:'你今日識咗睇條件嘅方向', line:'落堂前講一次：p ⇒ q，P 圈喺 Q 圈入面', iep:IEP });

d.save(path.join(__dirname, '..', '簡報_L5_充分條件與必要條件.pptx')).then(f => console.log('OK →', f));
