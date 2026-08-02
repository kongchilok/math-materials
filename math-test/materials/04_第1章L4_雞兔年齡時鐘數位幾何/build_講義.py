# -*- coding: utf-8 -*-
"""
第1章 特殊數學應用專題．L4 雞兔同籠、年齡、時鐘、數位與幾何應用 —— 課堂講義 build script
主設計 D7 提示卡（五種題型各一張，觸發語＋設定式＋示意圖）；
輔助 D2 手順卡（五種題型共用的解題四動作）、D14 錯誤分析對比（時鐘／年齡兩個高頻錯法）。
鷹架密度：抽離小班 (Tier 2)。
產出：講義_雞兔年齡時鐘數位幾何_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import design_svg as ds                      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
os.makedirs(FIGS, exist_ok=True)
BASE = "講義_雞兔年齡時鐘數位幾何_抽離小班共用版"
UNIT = "第1章 特殊數學應用專題．L4 雞兔同籠、年齡、時鐘、數位與幾何應用"
FOOT = "高三數學．" + UNIT


# ================================================================ 圖形（D7 卡片內的示意圖）
def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def clock_svg(hour, minute, w=320, h=312, cx=150, cy=150, R=112):
    """鐘面示意圖。實線＝時針與分針的真實位置；虛線＝該整點的刻度方向，
    用來讓學生一眼看到「時針已經離開整點」——這正是本課時鐘題的高頻錯法。"""
    p = ['<circle cx="%d" cy="%d" r="%d" fill="#ffffff" stroke="%s" stroke-width="2"/>'
         % (cx, cy, R, ds.INK)]
    for i in range(12):
        x1, y1 = _pt(cx, cy, R, i * 30)
        x2, y2 = _pt(cx, cy, R - (14 if i % 3 == 0 else 9), i * 30)
        p.append(ds._line(x1, y1, x2, y2, sw=2.6 if i % 3 == 0 else 1.4))
    for i in range(12):
        x, y = _pt(cx, cy, R - 30, i * 30)
        # halo：指針會從數字上面壓過去（分針指住 6 時必然重疊），要白邊才讀得到
        p.append(ds._txt(x, y, 12 if i == 0 else i, size=15, halo=True))
    th = (hour % 12) * 30 + minute * 0.5
    tm = minute * 6
    xo, yo = _pt(cx, cy, 62, (hour % 12) * 30)
    p.append(ds._line(cx, cy, xo, yo, sw=1.5, dash="5 4"))
    xm, ym = _pt(cx, cy, 94, tm)
    p.append(ds._line(cx, cy, xm, ym, sw=2.4))
    xh, yh = _pt(cx, cy, 62, th)
    p.append(ds._line(cx, cy, xh, yh, sw=5.0))
    p.append('<circle cx="%d" cy="%d" r="4.5" fill="%s"/>' % (cx, cy, ds.INK))
    p.append(ds._txt(222, 130, "虛線＝%d 的刻度" % (hour % 12), size=12,
                     anchor="start", halo=True))
    p.append(ds._txt(200, 190, "時針", size=13, anchor="start", halo=True))
    p.append(ds._txt(cx, 288, "分針", size=13, halo=True))
    return ds._svg(w, h, "".join(p))


def plane_svg(w=560, h=210):
    """平面幾何卡的示意圖：梯形（上底／下底／高）與長方形（長／寬）。"""
    p = []
    # 梯形
    p.append('<polygon points="60,160 250,160 210,70 100,70" fill="#ffffff" '
             'stroke="%s" stroke-width="1.8"/>' % ds.INK)
    p.append(ds._line(155, 70, 155, 160, sw=1.3, dash="4 4"))
    p.append(ds._txt(155, 58, "上底 a", size=14))
    p.append(ds._txt(155, 176, "下底 b", size=14))
    p.append(ds._txt(163, 115, "高 h", size=14, anchor="start", halo=True))
    p.append(ds._txt(155, 198, "梯形面積 ＝（a ＋ b）÷ 2 × h", size=14))
    # 長方形
    p.append(ds._rect(340, 78, 180, 82, sw=1.8))
    p.append(ds._txt(430, 66, "長 a", size=14))
    p.append(ds._txt(532, 119, "寬 b", size=14, anchor="start"))
    p.append(ds._txt(430, 198, "周長 ＝ 2（a ＋ b）　面積 ＝ a × b", size=14))
    return ds._svg(w, h, "".join(p))


SVG_CLOCK = clock_svg(3, 30)
PNG_CLOCK = os.path.join(FIGS, "clock_330.png")
ds.svg_to_png(SVG_CLOCK, PNG_CLOCK)
ds.save_svg(SVG_CLOCK, os.path.join(FIGS, "clock_330.svg"))

SVG_PLANE = plane_svg()
PNG_PLANE = os.path.join(FIGS, "plane_shapes.png")
ds.svg_to_png(SVG_PLANE, PNG_PLANE)
ds.save_svg(SVG_PLANE, os.path.join(FIGS, "plane_shapes.svg"))


# ================================================================ 文字內容
INTRO = [
    "這一課把第1章餘下的五種經典應用題一次過收齊：雞兔同籠、年齡、時鐘角度、"
    "數位（兩位數的十位與個位）、幾何應用。它們的情境完全不同，考試時卻常常混在一起出現。",
    "前三課的困難在「讀不懂題目在講什麼」——題目長、情境厚，所以要畫圖、要填三欄表。"
    "這一課的困難不同：題目通常很短，也讀得懂，難在「認不出這是哪一種題，"
    "於是取不出那一種題固定要用的設定式」。",
    "所以本課不是再學五套解題方法，而是每一種題型配一張卡。卡上寫明兩件事："
    "什麼時候翻它（觸發語），以及這一種題固定要怎樣設未知數、怎樣列式。"
    "認出題型、翻對卡，題目就已經解決了一半。",
    "五張題型卡之外，另有一張《解題四個動作》，五種題型共用同一套流程："
    "認題型 → 設未知數 → 照卡上的設定式列方程 → 解出來再代回題目原文檢核。"
    "所有卡片都會另外印成《工具卡》，請剪下來放在桌面；做題時用手指指住正在做的那一步。",
]

# ---------------------------------------------------------------- D7 五張題型卡
CARD_CHICKEN = dict(
    title="雞兔同籠卡",
    trigger="題目給出兩種東西的「總個數」，同時給出另一個總量（腳的數目、票款總額、分數總和），"
            "問兩種東西各有多少。",
    statement="兩種東西、兩個總量，就列兩條式：一條數「個數」，一條數「量」。"
              "設較容易數的那一種為 x，另一種用「總數 減 x」表示，就只剩一個未知數。",
    formula="① 個數：{x+y=n}（n ＝ 總個數）　② 總量：{ax+by=T}"
            "（a、b ＝ 每一個的量，T ＝ 總量）。"
            "※ 快捷法：先當成全部都是「量較小」的那一種，"
            "算出來的總量比實際少多少，就除以兩者每個相差的量。",
)

CARD_AGE = dict(
    title="年齡卡",
    trigger="題目出現「幾年前」「幾年後」「是⋯的幾倍」「年齡之和」「年齡之差」。",
    statement="兩個人的年齡差永遠不變——今年差幾多歲，十年前、十年後都差同樣多。"
              "時間走了 n 年，兩個人的年齡都要同時加 n（或減 n），不可以只改其中一個。",
    formula="設今年甲 {x} 歲、乙 {y} 歲。n 年後是 {x+n} 與 {y+n}；n 年前是 {x-n} 與 {y-n}；"
            "年齡差 {x-y} 由頭到尾不變。",
)

CARD_CLOCK = dict(
    title="時鐘卡",
    trigger="題目出現「時針」「分針」「夾角」，或者「這個鐘每小時快／慢多少分鐘」。",
    statement="分針每分鐘走 6°（一圈 360° 分給 60 分鐘）；時針每分鐘走 0.5°"
              "（一小時 30° 分給 60 分鐘）。時針不會停在整點刻度上——只要分鐘數不是 0，"
              "它就已經離開了。",
    formula="h 時 m 分：分針 ＝ {6m}°，時針 ＝ {30h+0.5m}°，夾角 ＝ {|30h-5.5m|}°"
            "（若大於 180°，用 360° 減）。快慢鐘用比例："
            "實際分鐘 : 鐘面顯示的分鐘 ＝ 60 :（60 加上快的分鐘數，或減去慢的分鐘數）。",
)

CARD_DIGIT = dict(
    title="數位卡",
    trigger="題目出現「個位」「十位」「百位」「兩位數」「三位數」「把數字對調」。",
    statement="「數字」與「數」不是同一件事：兩位數的十位數字只是 0 到 9 當中的一個數字，"
              "整個兩位數才是那個數。一定要先把數寫成「10 × 十位數字 ＋ 個位數字」，才列得出方程。",
    formula="兩位數 ＝ {10a+b}（a ＝ 十位數字，1 到 9；b ＝ 個位數字，0 到 9）；"
            "對調後 ＝ {10b+a}。兩者之差 ＝ {9(a-b)}（一定是 9 的倍數）；"
            "兩者之和 ＝ {11(a+b)}。三位數 ＝ {100a+10b+c}。",
)

CARD_PLANE = dict(
    title="幾何應用卡（平面）",
    trigger="題目出現「周長」「面積」「邊長」「內角」，或者「長比寬多⋯」。",
    statement="先看單位就知道問的是甚麼：厘米＝長度，平方厘米＝面積，立方厘米＝體積。"
              "若題目給的是兩個量的「和」與「差」，先用和差公式求出兩個量，再代進面積公式。",
    formula="長方形：周長 ＝ {2(a+b)}，面積 ＝ {ab}。梯形面積 ＝ {frac(a+b,2)*h}。"
            "圓：周長 ＝ {2*pi*r}，面積 ＝ {pi*r^2}。三角形內角和 ＝ 180°。"
            "※ 和差公式：大 ＝ {frac(S+D,2)}，小 ＝ {frac(S-D,2)}（S ＝ 和，D ＝ 差）。",
)

CARD_SOLID = dict(
    title="幾何應用卡（立體）",
    trigger="題目出現「表面積」「體積」「長方體」「正方體」「稜長」「邊長」。",
    statement="立體題最常見的做法，是由表面積或體積其中一個反推出未知的那一條邊，"
              "再代進另一條公式。先把長、寬、高三個位置寫出來，把已知的填進去，就看得出缺哪一個。",
    formula="長方體（長 a、寬 b、高 c）：表面積 ＝ {2(ab+bc+ca)}，體積 ＝ {abc}。"
            "正方體（稜長 a）：表面積 ＝ {6a^2}，體積 ＝ {a^3}。",
)

CARDS_D7 = [CARD_CHICKEN, CARD_AGE, CARD_CLOCK, CARD_DIGIT, CARD_PLANE, CARD_SOLID]
CARD_FIG = {"時鐘卡": (PNG_CLOCK, SVG_CLOCK, "圖中是 3 時 30 分：分針指住 6，"
                                             "時針已經由 3 向 4 走了一半，不在虛線那條刻度上"),
            "幾何應用卡（平面）": (PNG_PLANE, SVG_PLANE, "梯形的高一定是垂直距離，不是斜邊")}

# ---------------------------------------------------------------- D2 解題四個動作
STEP_TITLE = "解題四個動作（五種題型共用）"
STEP_TRIGGER = "每一題都由動作 1 做起，做完一個動作才做下一個。"
STEPS = [
    ("認題型：讀完題目先問「這是五種當中的哪一種」，然後翻對應的那一張卡。",
     "沒有認題型就直接動筆，是本課失分最多的一步。卡上的觸發語就是用來認題型的，"
     "認不出就把五張卡的觸發語逐張讀一次。"),
    ("設未知數：把「設⋯為 x」整句寫出來，連單位一齊寫。",
     "設錯對象會令式子變複雜。雞兔題設「腳較多的那一種」、年齡題設「年紀較小的那一個」，"
     "通常最快。"),
    ("列方程：照卡上的設定式抄下來，再把題目的數字填進去，不要憑記憶改。",
     "數位題一定要寫成 10a ＋ b；把「十位數字」與「個位數字」直接相乘或相加就錯了。"),
    ("解出來之後，代回題目原文檢核，再看答案大小合不合常理。",
     "代回自己列的式一定對得上，錯了也看不出來。要用題目那句話重新數一次"
     "（例如重新數一次腳的總數）。"),
]
STEP_FADING = "詳細四動作卡 → 只留四個關鍵詞（認、設、列、檢）→ 只留「這題有四步」→ 完全移除。"

# ---------------------------------------------------------------- 五個範例
EX = {}
SOL = {}
NOTE = {}

EX["A"] = ("【範例A・雞兔同籠】一個籠裡關住雞和兔，數一數共有 12 個頭、40 隻腳。"
           "問雞、兔各有多少隻？")
SOL["A"] = [
    "動作 1（認題型）：題目給了「頭的總數」與「腳的總數」，問兩種動物各有多少"
    "——這是雞兔同籠題，翻《雞兔同籠卡》。",
    "動作 2（設未知數）：設兔有 {x} 隻、雞有 {y} 隻。",
    "動作 3（列方程）：照卡上兩條式——① 個數：{x+y=12}（頭）"
    "　② 總量：{4x+2y=40}（腳，兔 4 隻腳、雞 2 隻腳）。",
    "動作 4（解與檢核）：由①得 {y=12-x}，代入②："
    "{4x+2(12-x)=40}，即 {2x+24=40}，{2x=16}，{x=8}；雞 ＝ {12-8=4}（隻）。",
    "檢核（代回題目原文）：兔 8 隻、雞 4 隻，頭共 {8+4=12} 個；"
    "腳共 {8*4+4*2=40} 隻——與題目完全相符。",
    "另一條路（卡上的快捷法）：先當成 12 隻全部是雞，腳只有 {2*12=24} 隻，"
    "比實際的 40 隻少 16 隻；每把一隻雞換成一隻兔就多 2 隻腳，所以兔 ＝ 16 ÷ 2 ＝ 8（隻）。",
]
NOTE["A"] = ("※ 這一類題不一定講雞和兔。「成人票與學生票」「五元硬幣與兩元硬幣」"
             "「答對得 4 分、答錯扣 1 分」全部是同一張卡：兩種東西、兩個總量、兩條式。"
             "認題型時看的是結構，不是故事。")

EX["B"] = ("【範例B・年齡】16 年前，父親的年齡是阿達的 3 倍；現在父親的年齡是阿達的 2 倍。"
           "問阿達今年幾歲？")
SOL["B"] = [
    "動作 1（認題型）：題目出現「16 年前」與「是⋯的幾倍」——這是年齡題，翻《年齡卡》。",
    "動作 2（設未知數）：設阿達今年 {x} 歲。由「現在是 2 倍」，父親今年 {2x} 歲。",
    "動作 3（列方程）：16 年前，兩個人都要減 16——阿達 {x-16} 歲，父親 {2x-16} 歲。"
    "當時父親是阿達的 3 倍：{2x-16=3(x-16)}。",
    "動作 4（解與檢核）：{2x-16=3x-48}，{48-16=3x-2x}，{x=32}（歲）；父親今年 {2*32=64} 歲。",
    "檢核（代回題目原文）：16 年前阿達 {32-16=16} 歲、父親 {64-16=48} 歲，"
    "而 {48=3*16}——「3 倍」成立；現在 {64=2*32}——「2 倍」也成立。",
    "再用卡上的不變量核一次：年齡差今年是 {64-32=32} 歲，16 年前是 {48-16=32} 歲，"
    "兩者相同——年齡差確實沒有變。",
]
NOTE["B"] = ("※ 年齡題的檢核有一招特別好用：算一次年齡差。只要你的答案令「今年的年齡差」"
             "與「n 年前的年齡差」不相等，那條方程就一定列錯了。")

EX["C"] = "【範例C・時鐘角度】求 3 時 30 分時，時針與分針所夾的角是多少度？"
SOL["C"] = [
    "動作 1（認題型）：題目出現「時針」「分針」「夾角」——這是時鐘題，翻《時鐘卡》。",
    "動作 2（設未知數）：本題不必設未知數，直接用卡上的兩個速率算出兩根針的位置。"
    "位置一律由「12」量起，順時針方向。",
    "動作 3（列式）：分針 ＝ {30*6=180}°（每分鐘 6°，走了 30 分鐘）；"
    "時針 ＝ {30*3+0.5*30=105}°（3 個整點共 {3*30=90}°，再加 30 分鐘走的 {0.5*30=15}°）。",
    "動作 4（算與檢核）：夾角 ＝ {180-105=75}°。",
    "檢核（用卡上的公式再算一次）：{|30h-5.5m|}，代入 h ＝ 3、m ＝ 30："
    "{|30*3-5.5*30|=|90-165|=75}°——兩種算法一致。",
]
NOTE["C"] = ("※ 上圖的虛線是「3」那一條刻度。時針（實線）明顯已經離開了虛線，"
             "因為 30 分鐘裡它走了 15°。凡是題目給的分鐘數不是 0，時針就一定不在整點刻度上"
             "——這是本課最多人錯的一步，第九節會再用正誤對照講一次。")

EX["D"] = ("【範例D・數位】一個兩位數，它的十位數字與個位數字之和是 9。"
           "把這兩個數字對調之後，所得的新數比原數大 45。求原數。")
SOL["D"] = [
    "動作 1（認題型）：題目出現「兩位數」「十位數字」「個位數字」「對調」"
    "——這是數位題，翻《數位卡》。",
    "動作 2（設未知數）：設十位數字為 {a}、個位數字為 {b}。"
    "則原數 ＝ {10a+b}，對調後的新數 ＝ {10b+a}。",
    "動作 3（列方程）：① 兩個數字之和：{a+b=9}"
    "　② 新數比原數大 45：{(10b+a)-(10a+b)=45}，化簡成 {9(b-a)=45}，即 {b-a=5}。",
    "動作 4（解與檢核）：①＋②：{2b=14}，{b=7}；代回①：{a=9-7=2}。原數 ＝ {10*2+7=27}。",
    "檢核（代回題目原文）：27 的兩個數字之和 {2+7=9}——相符；"
    "對調之後是 72，而 {72-27=45}——也相符。",
]
NOTE["D"] = ("※ 卡上寫「兩者之差一定是 9 的倍數」，這一句可以拿來預先檢查題目："
             "本題的差是 45，而 {45=9*5}，所以 b 與 a 相差 5——寫下 {b-a=5} 之後，"
             "其實已經不必再展開一次。")

EX["E"] = ("【範例E・幾何應用】（a）一塊梯形田的面積是 90 平方米，上底 7 米、下底 11 米，"
           "求它的高。（b）一個長方形的長與寬之和是 18 厘米，長比寬多 2 厘米，求它的面積。")
SOL["E"] = [
    "動作 1（認題型）：（a）出現「面積」「上底」「下底」，（b）出現「長與寬之和」"
    "「長比寬多」——兩問都是幾何應用題，翻《幾何應用卡（平面）》。",
    "動作 2（設未知數）：（a）設高為 {h} 米。（b）不必設未知數，因為題目直接給了「和」與「差」，"
    "可以用卡上的和差公式。",
    "動作 3（列式）：（a）梯形面積 ＝ {frac(7+11,2)*h}，題目說它等於 90，"
    "即 {frac(18,2)*h=90}，也就是 {9h=90}。",
    "動作 4（算與檢核）：（a）{h=10}（米）。檢核：{frac(7+11,2)*10=90} 平方米——相符。",
    "（b）用和差公式：長 ＝ {frac(18+2,2)=10}（厘米），寬 ＝ {frac(18-2,2)=8}（厘米）；"
    "面積 ＝ {10*8=80}（平方厘米）。",
    "檢核（代回題目原文）：{10+8=18}——「和是 18」相符；{10-8=2}——「長比寬多 2」也相符。",
]
NOTE["E"] = ("※ 和差公式不必背成兩條，記住一句就夠：把「差」補上去再對半分，得大的那一個；"
             "把「差」扣掉再對半分，得小的那一個。這一招在幾何題、年齡題、雞兔題都用得上。")

EX_ORDER = ["A", "B", "C", "D", "E"]
EX_HEAD = {"A": "四、範例A・雞兔同籠：兩種東西、兩條式",
           "B": "五、範例B・年齡：年齡差永遠不變",
           "C": "六、範例C・時鐘角度：時針每分鐘也在走",
           "D": "七、範例D・數位：先寫成 10a ＋ b",
           "E": "八、範例E・幾何應用：先看單位，再看和差"}
# 範例D 不分頁時，第 6 頁最後一行與 fixed 頁尾只差 4.4pt（QB-20 WARN）——
# 範本層不可改（CLAUDE.md §4 已記兩種修法皆失敗），照規定在該處手動分頁避開。
EX_BREAK = {"A": False, "B": False, "C": True, "D": True, "E": True}

# ---------------------------------------------------------------- D14 錯誤分析對比
ERR1_STEM = "【對比一】求 3 時 30 分時，時針與分針所夾的角。"
ERR1_ROWS = [
    ("分針：{30*6=180}°", "分針：{30*6=180}°"),
    ("時針：指住 3，所以 {3*30=90}°", "時針：{30*3+0.5*30=105}°"),
    ("夾角：{180-90=90}°", "夾角：{180-105=75}°"),
]
ERR1_NOTE = ("※ 差在這裡（第 2 列）：時針不會停在整點刻度上。過了 30 分鐘，"
             "它已經由「3」向「4」走了 {0.5*30=15}°，所以是 105° 而不是 90°。"
             "只要題目給的分鐘數不是 0，時針就一定已經離開整點——先加那一小段，再算夾角。")

ERR2_STEM = "【對比二】16 年前父親的年齡是阿達的 3 倍，現在是 2 倍，求阿達今年幾歲。"
ERR2_ROWS = [
    ("設阿達今年 {x} 歲，父親 {2x} 歲", "設阿達今年 {x} 歲，父親 {2x} 歲"),
    ("16 年前：{2x-16=3x}", "16 年前：{2x-16=3(x-16)}"),
    ("解得 {x=-16}（年齡是負數，不合理）", "{2x-16=3x-48}，解得 {x=32}（歲）"),
]
ERR2_NOTE = ("※ 差在這裡（第 2 列）：時間倒退 16 年，父親與阿達兩個人都要減 16。"
             "只把父親那一邊減 16，等於偷偷把兩人的年齡差改掉了。"
             "左邊那個做法算出負數，正好就是「年齡差被改掉」的後果——"
             "答案一出現負數或者小數，先回頭看有沒有漏減。")

# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D7 提示卡——雞兔同籠、年齡、時鐘、數位、幾何應用（平面／立體）各一張，"
                "每張寫明「什麼時候翻我」（觸發語）＋該題型固定的設定式，另附示意圖",
    aux_designs=("D2 手順卡——五種題型共用的《解題四個動作》"
                 "（認題型 → 設未知數 → 照卡列式 → 代回題目原文檢核），每一動作附 ※ 易錯點",
                 "D14 錯誤分析對比——只針對本課兩個真實高頻錯法："
                 "時鐘題以為時針停在整點刻度、年齡題只把年數減在其中一個人身上"),
    reason=(
        "本課收齊題庫 A1 應用題文字題餘下的五類經典題型（雞兔同籠與同型的兩種東西分配、"
        "年齡、時鐘與快慢鐘、數位、幾何應用，合計約 30 題）。"
        "與 L1～L3 同屬 teaching-designs.md 的 S1 文字應用題結構，但認知瓶頸不同："
        "前三課的題目長、情境厚，卡在語義解碼；本課的題目短、學生讀得懂，"
        "卡在「認不出這是哪一種題，於是取不出那一種題固定要用的設定式」，屬記憶檢索失敗。"
        "teaching-designs.md §4 對 D7 的問題陳述正是這一點，並要求卡片必須寫觸發語"
        "（什麼時候翻我），因此主設計取 D7，而不是 S1 慣用的 D1 條形模型或 D4 三欄式。"
        "D2 作輔助，為五種題型提供同一條外部程序軌道，避免學生每換一種題型就要重學流程；"
        "D14 作輔助，把本課兩個真實高頻錯法外顯化——本課屬統考複習性質而非新授課，"
        "且兩個對比都排在對應範例之後，符合 D14「不可用於全新概念第一次教學」的使用條件。"),
    density="抽離小班（Tier 2）",
    fading=(
        "提示卡（D7）：本課講義印出六張完整卡，另出《工具卡》讓學生剪下放桌面 → "
        "練習A 在每題題框下方標明「這一題翻哪一張卡」→ 練習B 不再標，由學生自己認題型翻卡 → "
        "練習C 收起卡片，只在作答區留一句「先寫出你設的未知數是甚麼」→ "
        "第21節綜合演練只保留時鐘卡與數位卡（兩個設定式最容易忘）→ 之後完全移除。｜"
        "手順卡（D2）：本課講義給完整四動作＋易錯點 → 練習A 每題旁重印精簡版（1 認 2 設 3 列 4 檢）→ "
        "練習B 只在區塊開頭印一次 → 練習C 不印 → 之後只口頭提示「四步」→ 移除。｜"
        "錯誤分析對比（D14）：本課給完整正誤雙欄 → 練習B 第 4 題只提示「這題有一個常見陷阱」→ "
        "練習C 不提示 → 訂正課時改由學生自己指出分歧步驟在第幾行 → 移除。"),
    flows=("F5 課前流程預告（今天四件事：五張題型卡 → 五個範例 → 兩個最易錯的步驟 → 練習A／B／C）",
           "F2 番茄鐘分段（本課題型多，建議每做完一個練習區塊停一次，"
           "讓學生把用過的卡片放回桌面固定位置，下一題重新認題型再翻）",
           "F4 過程導向回饋與分步計分（「認出題型」與「設未知數」兩步單獨給分；"
           "題型認對而後續算術筆誤者不重複扣分——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（題型卡即為此項，若獲准帶入測考需寫入 IEP 第 9 點）",
               "a5 放大字體", "a6 增加行距",
               "a7 調整計分標準（認題型／設未知數／列式／計算分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L1～L3 的銜接",
            "本課是第1章的最後一課。L3 的三欄式（D4）依其褪除路徑，本課起不再印欄位；"
            "但《解題四個動作》的動作 1、2 保留了原第①欄的讀題與第②欄的列式動作，"
            "所以三欄式養成的習慣不會斷。L1、L2 的條形圖（D1）本課已完全移除。"),
           ("為何不沿用 D1 或 D4",
            "本課五種題型的數量關係本身很短，兩條式就列完；畫條形圖或填三欄表會比題目本身還長。"
            "teaching-designs.md 對 D4 明確寫「不要用在兩步以內就算完的短題」。"
            "真正的困難在題型辨識與設定式提取，那是 D7 處理的問題。"),
           ("題量說明",
            "本課練習做五個題型全覆蓋，共 8 題（練習A 3 題、練習B 3 題、練習C 2 題），"
            "比 Tier 2 的標準題量（各 2 題共 6 題）多 2 題，以免有題型「只講不練」。"
            "若課堂時間不足，可先做練習A 全部與練習B 第 4、5 題，練習C 留作課後。"),
           ("配套文件",
            "《第1章 L4 雞兔同籠、年齡、時鐘、數位與幾何應用　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第1章 L4 雞兔同籠、年齡、時鐘、數位與幾何應用　工具卡》"
            "（五張題型卡 ＋ 解題四動作卡，學生剪下護貝放桌面）。")),
)


# ================================================================ docx
def build_docx_file():
    MEDIA = MediaRegistry()
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、五種題型，六張卡", page_break_before=True))
    P.append(para("每一張卡的第一行都是「什麼時候翻我」。讀完題目之後，"
                  "先在這六行觸發語裡找出對得上的那一張，再看卡上的設定式。"))
    for c in CARDS_D7:
        fig = CARD_FIG.get(c["title"])
        P.append(reference_card(c["title"], c["trigger"], c["statement"],
                                formula=c["formula"],
                                figure=(image_para(fig[0], width_cm=8.5, caption=fig[2])
                                        if fig else None),
                                media=MEDIA if fig else None))

    P.append(heading("三、解題四個動作", page_break_before=True))
    P.append(para("五種題型共用同一套流程。做題時用手指指住正在做的那一個動作，"
                  "做完一個才做下一個，不要跳去先算。"))
    P.append(step_card(STEP_TITLE, STEPS, trigger=STEP_TRIGGER, fading=STEP_FADING))

    for k in EX_ORDER:
        P.append(heading(EX_HEAD[k], page_break_before=EX_BREAK[k]))
        P.append(problem_box([para(EX[k])]))
        if k == "C":
            P.append(image_para(PNG_CLOCK, width_cm=8.5,
                                caption="3 時 30 分：虛線是「3」的刻度，時針（實線）已經離開了它"))
        for t in SOL[k]:
            P.append(para(t))
        P.append(shaded_box(NOTE[k]))

    P.append(heading("九、最容易錯的兩步", page_break_before=True))
    P.append(para("下面兩個對比，左欄是很多人會寫出來的做法，右欄是正確做法。"
                  "兩欄逐行對齊，只有一行不同——請先自己找出是哪一行，再看下面的說明。"))
    P.append(problem_box([para(ERR1_STEM)]))
    P.append(dual_track_table([([para(a)], [para(b, bold=True)]) for a, b in ERR1_ROWS],
                              headers=("常見寫法", "正確寫法")))
    P.append(shaded_box(ERR1_NOTE))
    P.append(problem_box([para(ERR2_STEM)]))
    P.append(dual_track_table([([para(a)], [para(b, bold=True)]) for a, b in ERR2_ROWS],
                              headers=("常見寫法", "正確寫法")))
    P.append(shaded_box(ERR2_NOTE))

    P.append(heading("十、接下來"))
    P.append(para("請拿出《第1章 L4 雞兔同籠、年齡、時鐘、數位與幾何應用　課堂練習》，"
                  "並把《工具卡》剪下來放在桌面。練習A 的三題已經在題框下方標明要翻哪一張卡，"
                  "旁邊也重印了四個動作；練習B 的三題不再標，要自己認題型；"
                  "練習C 的兩題連四個動作的提示都沒有，全部自己來。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=MEDIA)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _tex(m):
    import re
    m = m.strip()
    body = m
    for _ in range(6):
        new = re.sub(r"frac\(([^(),]+),([^(),]+)\)", r"\\frac{\1}{\2}", body)
        if new == body:
            break
        body = new
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    # 分子分母都要吃小數點——寫成 (\d+)/(\d+) 會把 30/0.1 讀成 30/0 再多出一個 .1，
    # 與 omml_core 的 _NUM_RE（本來就吃小數）不一致，docx 對而 HTML 錯（2026-07-27 實錄）。
    body = re.sub(r"(?<![\\{\w.])(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)(?![}\w.])",
                  r"\\frac{\1}{\2}", body)
    body = body.replace("%", r"\%")
    return r"\(%s\)" % body


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def _svg_inline(svg):
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def _ref_card_html(c):
    fig = CARD_FIG.get(c["title"])
    figure = ('<div class="fig">%s<div class="cap">%s</div></div>'
              % (_svg_inline(fig[1]), _esc(fig[2]))) if fig else ""
    return ('<div class="ref-card"><div style="font-weight:700">▍%s</div>'
            '<div class="trigger">什麼時候翻我：%s</div>%s'
            '<div>%s</div><div>%s</div></div>'
            % (_esc(c["title"]), _esc(c["trigger"]), figure,
               _h(c["statement"]), _h(c["formula"])))


def _step_card_html():
    rows = "".join('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                   % (i, _esc(a), _esc(p)) for i, (a, p) in enumerate(STEPS, 1))
    return ('<table class="d-tbl step-card">'
            '<tr><th colspan="2">%s</th></tr>'
            '<tr><td colspan="2">什麼時候用：%s</td></tr>%s'
            '<tr><td colspan="2">（教師）褪除：%s</td></tr></table>'
            % (_esc(STEP_TITLE), _esc(STEP_TRIGGER), rows, _esc(STEP_FADING)))


def _err_html(stem, rows, note):
    body = "".join('<tr><td>%s</td><td style="font-weight:700">%s</td></tr>'
                   % (_h(a), _h(b)) for a, b in rows)
    return ('<div class="problem">%s</div>'
            '<table class="d-tbl dual-track"><tr><th>常見寫法</th><th>正確寫法</th></tr>'
            '%s</table><div class="hint-card">%s</div>' % (_h(stem), body, _h(note)))


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    # 只補列印分頁規則；不動 @page 邊界與 .footer 的 position，QB-15c 的計數維持 1。
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .ref-card, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .ref-card .fig { margin: 6px 0; }
  .ref-card .fig svg { max-width: 100%; height: auto; }
</style>
</head>""")

    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂講義</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')

    parts.append('<div class="section-h">一、這一課要做到的事</div>')
    parts += ["<div>%s</div>" % _h(t) for t in INTRO]

    parts.append('<div class="section-h page-break">二、五種題型，六張卡</div>')
    parts.append('<div>每一張卡的第一行都是「什麼時候翻我」。讀完題目之後，'
                 '先在這六行觸發語裡找出對得上的那一張，再看卡上的設定式。</div>')
    parts += [_ref_card_html(c) for c in CARDS_D7]

    parts.append('<div class="section-h page-break">三、解題四個動作</div>')
    parts.append('<div>五種題型共用同一套流程。做題時用手指指住正在做的那一個動作，'
                 '做完一個才做下一個，不要跳去先算。</div>')
    parts.append(_step_card_html())

    for k in EX_ORDER:
        parts.append('<div class="section-h%s">%s</div>'
                     % (" page-break" if EX_BREAK[k] else "", _esc(EX_HEAD[k])))
        parts.append('<div class="problem">%s</div>' % _h(EX[k]))
        if k == "C":
            parts.append('<div class="fig">%s<div class="cap">'
                         '3 時 30 分：虛線是「3」的刻度，時針（實線）已經離開了它</div></div>'
                         % _svg_inline(SVG_CLOCK))
        parts += ["<div>%s</div>" % _h(t) for t in SOL[k]]
        parts.append('<div class="hint-card">%s</div>' % _h(NOTE[k]))

    parts.append('<div class="section-h page-break">九、最容易錯的兩步</div>')
    parts.append('<div>下面兩個對比，左欄是很多人會寫出來的做法，右欄是正確做法。'
                 '兩欄逐行對齊，只有一行不同——請先自己找出是哪一行，再看下面的說明。</div>')
    parts.append(_err_html(ERR1_STEM, ERR1_ROWS, ERR1_NOTE))
    parts.append(_err_html(ERR2_STEM, ERR2_ROWS, ERR2_NOTE))

    parts.append('<div class="section-h">十、接下來</div>')
    parts.append('<div>請拿出《第1章 L4 雞兔同籠、年齡、時鐘、數位與幾何應用　課堂練習》，'
                 '並把《工具卡》剪下來放在桌面。練習A 的三題已經在題框下方標明要翻哪一張卡，'
                 '旁邊也重印了四個動作；練習B 的三題不再標，要自己認題型；'
                 '練習C 的兩題連四個動作的提示都沒有，全部自己來。</div>')

    parts.append('<div class="footer">' + _esc(FOOT) + '</div>')

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join("<tr><td>%s</td><td>%s</td></tr>" % (_esc(k), _esc(v)) for k, v in tn_rows)
    parts.append('<div class="teacher-notes">'
                 '<div class="section-h">教師實施說明（本頁供教師參考，列印給學生時可不印）</div>'
                 '<table class="d-tbl">%s</table></div>' % tn)

    body = ("\n<body>\n<div class=\"page\">\n\n" + "\n\n".join(parts)
            + "\n\n</div>\n</body>\n</html>\n")
    path = os.path.join(HERE, BASE + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_docx_file())
    print(build_html_file())
