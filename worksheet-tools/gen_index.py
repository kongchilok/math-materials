# -*- coding: utf-8 -*-
# 產生「歷屆試題分類索引」頁（HTML），風格與 output 一致。
import sys, io, json, re, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = 'C:/Users/KongChiLok/notebookLM/worksheet-tools'
d = json.load(open(ROOT + '/data/ALL.json', encoding='utf-8'))

# 16 類正名（依考試大綱圖片）
NAMES = {
 1:'基本概念', 2:'百分數', 3:'變分', 4:'多項式及有理分式',
 5:'二次方程及二次函數', 6:'指數及根式', 7:'代數不等式', 8:'對數與指數函數',
 9:'非線性方程', 10:'排列與組合', 11:'數列', 12:'直線圖形及圓',
 13:'三角', 14:'解析幾何', 15:'函數圖形', 16:'概率與統計'}
CN = '一二三四五六七八九十十一十二十三十四十五十六'  # 用 index map 下面另算
CNNUM = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',
 10:'十',11:'十一',12:'十二',13:'十三',14:'十四',15:'十五',16:'十六'}

# 中文數字 → int（解析 type 字串中的「第X類型」）
CMAP = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,
 '十一':11,'十二':12,'十三':13,'十四':14,'十五':15,'十六':16}
def type_num(s):
    m = re.search(r'第([一二三四五六七八九十]+)類型', s)
    return CMAP[m.group(1)]

# === 校對後的重新分類（key=(年,'C'/'S',題號) → (原類號, 新類號, 原因)）===
# 註：ALL.json 的 type 欄位已就地更新為「新類號」，此表保留原類號僅供「調整說明」對照。
OVR = {
 ('2017','C',3):(3,2,'複利息屬「百分數」單元，非變分'),
 ('2017','C',14):(12,14,'橢圓為圓錐曲線，屬解析幾何'),
 ('2017','S',2):(12,14,'坐標平面的圓方程與直線關係，屬解析幾何'),
 ('2018','C',7):(5,9,'分式方程求解，屬非線性方程（原標二次函數無二次式）'),
 ('2018','C',11):(12,14,'橢圓焦點屬解析幾何'),
 ('2018','C',15):(12,14,'以中點坐標求三角形頂點，為坐標幾何方法'),
 ('2018','S',2):(15,3,'f(x) 為部分變（隨 x 與 x² 正變），核心屬變分'),
 ('2018','S',3):(12,14,'拋物線於坐標平面，屬解析幾何'),
 ('2019','C',13):(12,14,'橢圓焦點屬解析幾何'),
 ('2020','C',2):(3,2,'人口按固定百分率增長，屬百分數（增長）'),
 ('2020','C',10):(12,14,'坐標給定直徑端點求圓上點，屬解析幾何'),
 ('2020','C',14):(13,12,'圓的弦切角／圓周角，屬平面幾何（直線圖形及圓）'),
 ('2020','S',5):(12,14,'坐標圓方程與直線，屬解析幾何'),
 ('2022','C',11):(3,10,'帶限制的座位計數，屬排列與組合（計數）'),
 ('2026','C',3):(3,5,'原標「一次方程」非16類正名，依使用者歸二次方程及二次函數'),
 ('2026','C',11):(6,9,'含根號的無理方程求解，屬非線性方程'),
}

# 收集：cat -> list of (year, sec, n, moved_bool)
cat = collections.defaultdict(list)
changes = []
for y in sorted(d.keys()):
    for sec,key in (('C','choices'),('S','solutions')):
        for q in d[y][key]:
            n = q['n']
            cur = type_num(q['type'])          # ALL.json 已是校對後類號
            moved = (y,sec,n) in OVR
            cat[cur].append((y,sec,n,moved))
            if moved:
                oldt,newt,reason = OVR[(y,sec,n)]
                changes.append((y,sec,n,oldt,newt,reason))

# 排序 entries：年→ 選先於解 → 題號
def entry_key(e):
    y,sec,n,_ = e
    return (y, 0 if sec=='C' else 1, n)
for k in cat: cat[k].sort(key=entry_key)

def code(sec,n):
    return ('選' if sec=='C' else '解') + str(n)

# === 產生 HTML ===
total = sum(len(cat[t]) for t in range(1,17))
nyears = len(d)

CSS = '''
 @page { size:A4; margin:0.5cm 1cm; }
 * { box-sizing:border-box; }
 html { font-size:11.5pt; }
 body { font-family:"Noto Serif TC","Times New Roman","Songti TC",serif; color:#111; line-height:1.45; margin:0; padding:0; background:#fff; }
 .book { max-width:880px; margin:0 auto; }

 /* 共用：學術雙線外框 */
 .frame { border:2px solid #1d1c1a; padding:7px; min-height:27.6cm; display:flex; }
 .frame-in { border:1px solid #b6532c; flex:1 1 auto; display:flex; flex-direction:column; padding:1.1cm 1.2cm; }

 /* 封面 */
 .cover { page-break-after:always; }
 .cv-top { text-align:center; font-size:12pt; letter-spacing:0.5em; color:#2a5560; font-weight:700; padding-left:0.5em; }
 .cv-line { height:2px; background:#1d1c1a; margin:14px auto 0; width:62%; }
 .cv-mid { flex:1 1 auto; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:18px; }
 .cv-title { font-size:34pt; font-weight:700; letter-spacing:0.10em; color:#1d1c1a; padding-left:0.10em; }
 .cv-sub { font-size:13pt; color:#555; letter-spacing:0.30em; padding-left:0.30em; }
 .cv-years { font-size:20pt; color:#b6532c; font-weight:700; letter-spacing:0.18em; padding-left:0.18em; margin-top:4px; }
 .cv-sym { font-size:17pt; color:#c9c4b8; letter-spacing:0.55em; padding-left:0.55em; margin-top:8px; }
 .cv-bot { text-align:center; color:#444; font-size:11pt; line-height:1.9; }
 .cv-bot .em { color:#2a5560; font-weight:700; }
 .cv-bot .rule { height:1px; background:#d8d2c4; width:46%; margin:0 auto 10px; }

 /* 索引內頁 */
 .idx-head { border-bottom:2px solid #111; padding-bottom:6px; margin-bottom:9px; }
 .idx-title { font-size:15pt; font-weight:700; letter-spacing:0.03em; }
 .idx-sub { font-size:10pt; color:#555; margin-top:3px; }
 .grid { column-count:2; column-gap:22px; }
 .cat { break-inside:avoid; margin-bottom:11px; }
 .sec-head { font-size:11pt; font-weight:700; margin:0 0 5px; padding:3px 10px; background:#1d1c1a; color:#fff; border-radius:3px; }
 .sec-head .sec-sub { font-size:8.5pt; font-weight:400; color:#d8d2c4; margin-left:6px; }
 .rows { padding:0 2px; }
 .yr { display:flex; gap:8px; align-items:baseline; font-size:10pt; padding:1.6px 0; border-bottom:1px dotted #e6e3d8; }
 .yr:last-child { border-bottom:none; }
 .y { flex:0 0 40px; font-weight:700; color:#2a5560; }
 .qs { flex:1 1 auto; color:#222; }
 .empty { color:#aaa; font-size:9.5pt; }

 /* 封底 */
 .back { page-break-before:always; }
 .bk-title { font-size:16pt; font-weight:700; letter-spacing:0.10em; padding-left:0.10em; color:#1d1c1a; text-align:center; }
 .bk-rule { height:2px; background:#1d1c1a; width:46%; margin:12px auto 22px; }
 .bk-h { font-size:11pt; font-weight:700; color:#fff; background:#1d1c1a; border-radius:3px; padding:3px 11px; display:inline-block; margin:0 0 7px; }
 .bk-use { font-size:10.5pt; color:#333; line-height:1.85; }
 .bk-use b { color:#b6532c; }
 .bk-counts { display:grid; grid-template-columns:repeat(4,1fr); gap:6px 10px; margin-top:8px; }
 .cell { border:1px solid #d8d6cd; border-radius:4px; padding:4px 8px; font-size:9.5pt; display:flex; justify-content:space-between; align-items:baseline; }
 .cell .nm { color:#222; } .cell .ct { color:#b6532c; font-weight:700; }
 .bk-note { font-size:9pt; color:#666; line-height:1.6; margin-top:14px; }
 .bk-foot { margin-top:auto; text-align:center; color:#888; font-size:9.5pt; letter-spacing:0.06em; border-top:1px solid #d8d2c4; padding-top:10px; }
 .spacer { flex:1 1 auto; }
'''

H = []
H.append('<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="UTF-8">'
 '<title>澳門四校聯考 數學 歷屆試題分類索引</title><style>%s</style></head><body><div class="book">' % CSS)

# ---------- 封面 ----------
SYM = '∑　√　π　∫　θ　≤　∞'
H.append(
 '<div class="cover"><div class="frame"><div class="frame-in">'
 '<div class="cv-top">澳門四校聯考</div><div class="cv-line"></div>'
 '<div class="cv-mid">'
 '<div class="cv-title">數學正卷</div>'
 '<div class="cv-sub">歷屆試題</div>'
 '<div class="cv-sym">%s</div>'
 '</div>'
 '<div class="cv-bot"><div class="rule"></div>'
 '附分類索引　·　試題主題速查<br>'
 '從考試大綱 <span class="em">十六單元</span> 編成</div>'
 '</div></div></div>' % SYM)

# ---------- 索引內頁 ----------
H.append('<div class="index"><div class="idx-head"><div class="idx-title">澳門四校聯考　數學　歷屆試題分類索引</div>'
 '<div class="idx-sub">2017 – 2026 年（每屆 選擇 15 題＋解答 5 題）。各單元下左為年份、右為題號；'
 '<b>選</b>＝選擇題、<b>解</b>＝解答題（如「選1」即該年選擇第 1 題、「解3」即解答第 3 題）。</div></div>')
H.append('<div class="grid">')
for t in range(1,17):
    entries = cat.get(t,[])
    H.append('<div class="cat"><div class="sec-head">%s、%s<span class="sec-sub">共 %d 題</span></div><div class="rows">'
             % (CNNUM[t], NAMES[t], len(entries)))
    if not entries:
        H.append('<div class="empty">（暫無）</div>')
    else:
        byyear = collections.OrderedDict()
        for (y,sec,n,_moved) in entries:
            byyear.setdefault(y,[]).append((sec,n))
        for y,lst in byyear.items():
            parts = [code(sec,n) for (sec,n) in lst]
            H.append('<div class="yr"><span class="y">%s</span><span class="qs">%s</span></div>'%(y,'、'.join(parts)))
    H.append('</div></div>')
H.append('</div>')  # grid
H.append('</div>')  # index

# ---------- 封底 ----------
counts = ''.join('<div class="cell"><span class="nm">%s、%s</span><span class="ct">%d</span></div>'
                 % (CNNUM[t], NAMES[t], len(cat.get(t,[]))) for t in range(1,17))
H.append(
 '<div class="back"><div class="frame"><div class="frame-in">'
 '<div class="bk-title">使用說明</div><div class="bk-rule"></div>'
 '<div class="bk-h">查表方式</div>'
 '<div class="bk-use">本索引按考試大綱十六個單元，收錄 2017–2026 共十屆、合計 <b>%d</b> 題之分類。'
 '在內頁找到欲複習的單元，循「年份 → 題號」即可定位原卷題目。'
 '<b>選</b> 表選擇題、<b>解</b> 表解答題；例「2019　選8、解2」即 2019 年選擇第 8 題與解答第 2 題。</div>'
 '<div style="height:16px"></div>'
 '<div class="bk-h">各單元題數</div>'
 '<div class="bk-counts">%s</div>'
 '<div class="bk-note">分類凡例：圓錐曲線（橢圓／雙曲線／拋物線）及坐標平面上的圓與直線歸「十四、解析幾何」；'
 '無坐標的純平面幾何（三角形、相似全等、圓的弦／角／弧／扇形、面積度量）歸「十二、直線圖形及圓」。</div>'
 '<div class="spacer"></div>'
 '<div class="bk-foot">澳門四校聯考　數學科　·　歷屆試題分類索引　·　2017 – 2026</div>'
 '</div></div></div>' % (total, counts))

H.append('</div></body></html>')

out = ROOT + '/output/四校聯考數學_歷屆試題分類索引.html'
open(out,'w',encoding='utf-8').write(''.join(H))
print('題目總數：', total)
for t in range(1,17):
    print('%2d %s：%d'%(t,NAMES[t],len(cat[t])))
print('輸出：', out)
