// build_L3.js — L3 交集與並集（抽離小組 40 分鐘）
// 三段式：動機 P1–3｜注意 P4–11｜行動 P12–14　轉換點：P6、P12
const path = require('path');
const { Deck, drawVenn } = require('./soil_kit');
const d = new Deck('交集與並集');
const IEP = '教學調整（Accommodation）：本簡報加入圖像表徵、步驟卡與分層任務，年級學習標準不變。';

d.cover({ title:'交集與並集', subtitle:'高一數學 · 抽離小組 · 第 3 課（40 分鐘）',
  hook:'帶走一句：「或」用並集 ∪，「且」用交集 ∩' });

d.agenda({ steps:['並集 ∪：兩邊合埋','交集 ∩：兩邊共同','「或」同「且」嘅分別','實際計算'],
  note:'中間會停低兩次，一齊做練習。' });

d.problem({ question:'兩樣都打嘅同學，係邊啲？',
  sub:'籃球：明、華、強　　羽毛球：華、強、美',
  caption:'兩邊都有嘅人 — 呢個就係「交集」。', star:true });

d.cra({ title:'並集 ∪：合埋',
  concrete:{ text:'兩隊合埋一齊\n\n所有參加過\n運動嘅人' },
  rep:{ draw: drawVenn('union', { caption:'塗色部分 = A ∪ B' }) },
  abstract:{ text:'A ∪ B\n\n= {x | x∈A 或 x∈B}' },
  takeaway:'並集 = 兩邊全部合埋，重複只寫一次', star:true });

d.cra({ title:'交集 ∩：共同',
  concrete:{ text:'兩隊都有份\n\n又打籃球\n又打羽毛球' },
  rep:{ draw: drawVenn('intersection', { caption:'深色部分 = A ∩ B' }) },
  abstract:{ text:'A ∩ B\n\n= {x | x∈A 且 x∈B}' },
  takeaway:'交集 = 兩邊共同嗰啲', star:true });

d.compare2({ title:'「或」同「且」',
  left: { head:'並集 ∪（或）', lines:['有一邊有，就要','','A ∪ B = {x | x∈A 或 x∈B}','','會變大（或一樣）'] },
  right:{ head:'交集 ∩（且）', lines:['兩邊都要有','','A ∩ B = {x | x∈A 且 x∈B}','','會變細（或一樣）'] },
  note:'「或」= 合埋（∪）　　「且」= 共同（∩）', badge:'一齊讀：∪ 或、∩ 且', star:true });

d.scaffold4({ title:'求交集並集，四步走',
  steps:[
    '寫低 A 同 B 全部元素',
    '並集：兩邊合埋，重複只寫一次',
    '交集：圈出兩邊都有嘅',
    '檢查：∩ 嘅元素一定喺 ∪ 入面',
  ], note:'之後做練習，照住呢四步行。' });

d.tableSlide({ title:'例：A = {1, 2, 3}，B = {2, 3, 4}',
  headers:['求','做法','答案'],
  rows:[
    ['A ∪ B', '兩邊合埋，重複寫一次', '{1, 2, 3, 4}'],
    ['A ∩ B', '圈出兩邊都有嘅',       '{2, 3}'],
    ['A ∪ ∅', '加個空嘅，冇變',       '{1, 2, 3}'],
    ['A ∩ ∅', '冇共同元素',           '∅'],
  ], colW:[2.6, 5.0, 4.5], star:true });

d.compareCards({ title:'寫答案時最易錯',
  cards:[
    { ok:false, text:'A ∪ B = {1, 2, 3, 2, 3, 4}', note:'重複寫咗 — 2 同 3 各寫兩次' },
    { ok:true,  text:'A ∪ B = {1, 2, 3, 4}',       note:'重複嘅只寫一次' },
    { ok:false, text:'A ∩ B = {1, 2, 3, 4}',       note:'呢個係並集，唔係交集' },
  ], star:true });

d.figure({ title:'淨係喺 A 嗰啲',
  draw: drawVenn('onlyA'),
  caption:'塗色部分 = 喺 A，但唔喺 B',
  side:['即係：A 減走','兩邊共同嗰部分','','A = {1, 2, 3}','B = {2, 3, 4}','','淨係喺 A = {1}'] });

d.problem({ title:'一齊做：應用題',
  question:'淨係打籃球嘅有幾多人？',
  sub:'全班 20 人　打籃球 12 人\n打羽毛球 9 人　兩樣都打 5 人',
  caption:'提示：用頭先個圖 — 打籃球嘅，減走兩樣都打嘅。' });

d.layered({
  cols:[
    { stars:'★☆☆', head:'練習 A', lines:['A = {1, 2, 3}','B = {3, 4}','','求 A ∪ B','求 A ∩ B'] },
    { stars:'★★☆', head:'練習 B', lines:['A = 細過 6 嘅','　　正整數','B = {2, 4, 6}','','求 A ∩ B'] },
    { stars:'★★★', head:'練習 C', lines:['已知 A ∩ B = {2}','A = {1, 2}','','寫出兩個可能','嘅 B'] },
  ], note:'做完 A 想再試，就上 B、C — 自己揀就得。', badge:'揀一層，開始做', star:true });

d.summary({ takeaway:'「或」用並集 ∪\n「且」用交集 ∩',
  lines:['① A ∪ B：兩邊合埋，重複只寫一次','② A ∩ B：兩邊共同嗰啲','③ 交集嘅元素，一定喺並集入面'], star:true });

d.closing({ title:'你今日識咗合埋同搵共同', line:'落堂前講一次：∪ 係「或」，∩ 係「且」', iep:IEP });

d.save(path.join(__dirname, '..', '簡報_L3_交集與並集.pptx')).then(f => console.log('OK →', f));
