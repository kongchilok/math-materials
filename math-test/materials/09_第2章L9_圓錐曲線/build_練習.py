# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L9 解析幾何（二）圓錐曲線 —— 課堂練習 ＋ 工具卡 build script
主設計 D7 提示卡（褪除：A 每題標明翻哪一張 → B 只列三個觸發語 → C 不提示）；
輔助 D5 圖文雙軌（A 的橢圓題附已畫好的圖，只要在圖上讀 a、b → B 不給圖 → C 自己畫草圖）、
D2 手順卡（B 區塊開頭印一次關鍵詞 → C 不印）。
鷹架密度：抽離小班 (Tier 2)。

第 1 題刻意「不附圖」——那一題考的正是「由方程認出是哪一種」，給了圖等於給答案；
D5 的第一級褪除改放在第 2 題（橢圓的量在圖上量得到）。

產出：練習_圓錐曲線_抽離小班共用版.docx/.html、工具卡_圓錐曲線.docx
"""
import os
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omml_docx import *                      # noqa: E402,F403
import design_svg as ds                      # noqa: E402
from coord_svg import coord_svg              # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_圓錐曲線_抽離小班共用版"
CARDF = "工具卡_圓錐曲線"
UNIT = "第2章 中學基礎數學應用．L9 解析幾何（二）圓錐曲線"
FOOT = "高三數學．" + UNIT

# ================================================================ 圖
# 練習A 第 2 題：橢圓已畫好，a、b 在圖上量得到（D5 褪除第一級）
FIG_Q2 = coord_svg([
    {"t": "ellipse", "a": 10, "b": 8, "center": False},
], xlo=-12, xhi=12, ylo=-10, yhi=10, unit=8, tick=2)

# 工具卡的三張小圖
TC_R = dict(xlo=-6, xhi=6, ylo=-4, yhi=4, unit=9, tick=2)
FIG_TC_E = coord_svg([
    {"t": "ellipse", "a": 5, "b": 3, "center": False},
    {"t": "point", "x": 4, "y": 0}, {"t": "point", "x": -4, "y": 0},
], **TC_R)
FIG_TC_H = coord_svg([
    {"t": "hyper", "a": 4, "b": 3, "asym": True, "center": False},
    {"t": "point", "x": 5, "y": 0}, {"t": "point", "x": -5, "y": 0},
], **TC_R)
FIG_TC_P = coord_svg([
    {"t": "parab", "k": 0.35, "vy": -2, "dir": "up"},
], **TC_R)

# ================================================================ 題目
HINT_TOP = ("動筆之前永遠先做同一件事：認出這是哪一種曲線。"
            "兩項相加 = 1 → 橢圓（翻提示卡一）；兩項相減 = 1 → 雙曲線（提示卡二）；"
            "只有一個變數是二次 → 拋物線（提示卡三）。"
            "認出來之後，該用哪一條式、a 是誰、c 是加還是減，卡上都寫齊了。")

STEP_TITLE = "兩張手順卡（關鍵詞版）"
STEP_TRIGGER = "先認出是哪一種曲線，再照對應那一行做。"
STEP_COMPACT = [
    "橢圓求各量：化標準式（右邊 = 1）→ 大分母是 {a^2}、長軸跟着它走 → "
    "{c=sqrt(a^2-b^2)}（「減」）→ {e=frac(c,a)}、兩準線距離 {frac(2a^2,c)}",
    "共同漸近線：右邊的 1 換成 k → 代入題目給的點求 k → 兩邊除以 k 化回標準式 → "
    "檢查點代得返、新舊漸近線相同",
]
STEP_WARN = ("※ 橢圓 {c^2=a^2-b^2}（相減、{c<a}）、雙曲線 {c^2=a^2+b^2}（相加、{c>a}），"
             "兩條不要對調；算完用離心率檢查：橢圓 {e<1}、雙曲線 {e>1}。"
             "※ 橢圓的 a 看分母「大小」，雙曲線的 a 看減號「位置」。")

STEMS = {
    1: "判斷下列各方程（或條件）代表哪一種曲線，並寫出你的理由："
       "（a）{frac(x^2,36)+frac(y^2,16)=1}　（b）{y^2-frac(x^2,4)=1}　"
       "（c）{y=3x^2+2x-1}　（d）某曲線的離心率 {e=1.5}。",
    2: "已知橢圓 {frac(x^2,100)+frac(y^2,64)=1}（圖已畫好，可以在圖上量）。"
       "（a）求 a、b 與長軸的方向。（b）求 c。（c）求離心率 e。",
    3: "已知橢圓 {25x^2+9y^2=225}。（a）求半長軸 a 與長軸的方向。"
       "（b）求 c 與離心率 e。（c）求兩準線間的距離。",
    4: "已知雙曲線 {frac(x^2,9)-frac(y^2,16)=1}。（a）求 a、b、c 與漸近線方程。"
       "（b）若 P 在雙曲線上、到一個焦點的距離是 2，求 P 到另一個焦點的距離。",
    5: "寫出下列各曲線的種類、開口方向（如果是拋物線）與頂點／圓心，並在空白處畫出草圖："
       "（a）{y=-x^2+2}　（b）{y^2=-8x}　（c）{frac(x^2,4)+frac(y^2,4)=1}。",
    6: "求經過點 {P(3,4sqrt(2))}、且與 {frac(x^2,9)-frac(y^2,16)=1} "
       "有共同漸近線的雙曲線方程。",
}

# 練習A：D7 褪除第一級——標明該翻哪一張卡
CARD_HINT = {
    1: "▍(a) 相加 → 翻提示卡一；(b) 相減 → 提示卡二（注意 {y^2} 的分母是 1，沒有寫出來）；"
       "(c) 只有 x 是二次 → 提示卡三；(d) 只給離心率 → 三張卡的離心率那一欄比一比。",
    2: "▍翻提示卡一（橢圓）：{a^2} 是較大的分母，長軸跟着大分母那個變數走；"
       "{c^2=a^2-b^2}（「相減」）；{e=frac(c,a)}。圖上量一量再算，兩邊要對得上。",
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
LINES = {1: 7, 2: 6, 3: 7, 4: 7, 5: 11, 6: 8}   # B 用 7 行：8 行時第 4 題會溢頁

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）橢圓　（b）雙曲線（縱向）　（c）拋物線　（d）雙曲線",
        kp="由方程或離心率認出曲線種類。看三件事：兩項是相加還是相減、"
           "是不是只有一個變數是二次、離心率落在哪一段。",
        fm="相加 = 1 → 橢圓（{0<e<1}）；相減 = 1 → 雙曲線（{e>1}）；"
           "一個變數二次 → 拋物線（{e=1}）；兩個分母相同的「相加 = 1」→ 圓。",
        steps=["（a）兩項相加等於 1、兩個分母都是正數 → 橢圓。"
               "（36 > 16 且大分母在 x 下面 → 長軸沿 x 軸，{a=6}、{b=4}。）",
               "（b）把分母寫齊就是 {frac(y^2,1)-frac(x^2,4)=1}：兩項相減等於 1 → 雙曲線。"
               "減號前面是 {y^2}，所以是縱向的（開口上下），{a=1}、{b=2}。",
               "（c）x 是二次、y 是一次 → 拋物線；{x^2} 係數 3 > 0 → 開口向上。",
               "（d）{e=1.5>1} → 雙曲線。（{0<e<1} 才是橢圓，{e=1} 是拋物線。）"],
        pit="① (b) 因為看不到分母就認不出是雙曲線——{y^2} 的分母是 1，補寫出來就清楚。"
            "② (b) 答成「橫向雙曲線」：減號「前面」是 y，所以是縱向。"
            "③ (d) 記錯離心率的分段：橢圓 {0<e<1}、拋物線 {e=1}、雙曲線 {e>1}，"
            "三段沒有重疊，不要背混。"),
    2: dict(
        ans="（a）{a=10}、{b=8}、長軸沿 x 軸　（b）{c=6}　（c）{e=0.6}",
        kp="由橢圓標準式讀出四個量。a² 是較大的分母、長軸跟着它走；"
           "c 由 a、b 相減求出；離心率 {e=frac(c,a)}。",
        fm="{frac(x^2,a^2)+frac(y^2,b^2)=1}；{c^2=a^2-b^2}；{e=frac(c,a)}。",
        steps=["（a）分母 100 > 64，大分母在 x 下面 → 長軸沿 x 軸；"
               "{a^2=100} → {a=10}；{b^2=64} → {b=8}。"
               "圖上檢核：橢圓與 x 軸交於 {(+-10,0)}、與 y 軸交於 {(0,+-8)} ✔",
               "（b）{c^2=a^2-b^2=100-64=36} → {c=6}，焦點 {(+-6,0)} 在長軸上。",
               "（c）{e=frac(c,a)=frac(6,10)=frac(3,5)=0.6}，"
               "落在 0 與 1 之間 ✔ 確實是橢圓。",
               "檢核：6-8-10 是 3-4-5 的兩倍，直角三角形 ✔；"
               "{c=6<10=a}，焦點確實落在橢圓內部 ✔"],
        pit="① 把 {a=100} 寫下去——分母是 {a^2}，要開方。"
            "② {c^2} 用了相加（{100+64}）：那是雙曲線的式，橢圓是相減。"
            "③ 離心率算成 {frac(a,c)=frac(10,6)}——是 {frac(c,a)}，而且橢圓的 e 一定小於 1。"),
    3: dict(
        ans="（a）{a=5}、長軸沿 y 軸　（b）{c=4}、{e=0.8}　（c）12.5",
        kp="題目給的不是標準式，第一步一定是化成「右邊 = 1」。"
           "化完之後大分母在 y 下面，長軸就沿 y 軸——這一題考的正是"
           "「長軸方向不一定是 x」。",
        fm="化標準式：整條式除以常數項；{c^2=a^2-b^2}；{e=frac(c,a)}；"
           "兩準線距離 {=frac(2a^2,c)}。",
        steps=["先化標準式：{25x^2+9y^2=225} 兩邊除以 225 → "
               "{frac(25x^2,225)+frac(9y^2,225)=1} → {frac(x^2,9)+frac(y^2,25)=1}。",
               "（a）分母 25 > 9 且大分母在 y 下面 → 長軸沿 「y 軸」；"
               "{a^2=25} → {a=5}（{b^2=9} → {b=3}）。",
               "（b）{c^2=25-9=16} → {c=4}，焦點 {(0,+-4)}；{e=frac(4,5)=0.8}。",
               "（c）準線 {y=+-frac(a^2,c)=+-frac(25,4)}，"
               "兩準線間的距離 {=frac(2a^2,c)=frac(50,4)=12.5}。",
               "檢核：原式代 {(0,5)}：{25(0)+9(25)=225} ✔（長軸端點在 y 軸上）；"
               "代 {(3,0)}：{25(9)+0=225} ✔（短軸端點在 x 軸上）。"
               "另：準線一定在橢圓外面，{frac(a^2,c)=6.25>5=a} ✔"],
        pit="① 不化標準式就直接讀係數，把 25 當成 {a^2}。"
            "② 化的時候把係數搬去分母搬錯：{frac(25x^2,225)=frac(x^2,9)}，不是 {frac(x^2,25)}。"
            "③ 看到 x 在前面就寫「長軸沿 x 軸」——要看「大分母」在哪一個變數下面。"
            "④ 準線距離只寫了一半（{frac(a^2,c)=6.25}）——題目問的是兩條之間的距離，要乘 2。"),
    4: dict(
        ans="（a）{a=3}、{b=4}、{c=5}、漸近線 {y=+-frac(4,3)x}　（b）8",
        kp="雙曲線的 a 看減號位置（不看大小），c 由 a、b 「相加」求出；"
           "焦半徑用定義：到兩焦點距離之差的絕對值等於 2a。",
        fm="{frac(x^2,a^2)-frac(y^2,b^2)=1}；{c^2=a^2+b^2}；"
           "漸近線 {y=+-frac(b,a)x}；{|d_1-d_2|=2a}。",
        steps=["（a）減號前面是 x → 橫向雙曲線；{a^2=9} → {a=3}；{b^2=16} → {b=4}。"
               "（注意：{b>a} 完全正常，雙曲線的 a 不是「較大的」。）",
               "（a）{c^2=a^2+b^2=9+16=25} → {c=5}（「相加」）；"
               "漸近線 {y=+-frac(b,a)x=+-frac(4,3)x}。順帶 {e=frac(5,3)≈1.67>1} ✔",
               "（b）由定義 {|d_1-d_2|=2a=6}。{d_1=2} → {d_2=2+6=8}，"
               "或 {d_2=2-6=-4}（距離不能是負數，捨去）。所以 {d_2=8}。",
               "檢核（第二條路）：焦點到最近頂點的距離 {=c-a=5-3=2}，"
               "剛好等於題目給的 {d_1=2}，即 P 就是頂點 {(3,0)}。"
               "那麼 P 到另一個焦點 {(-5,0)} 的距離 {=3-(-5)=8} ✔ "
               "而且 {8=c+a=5+3} ✔ 兩條路完全吻合。"],
        pit="① {c^2} 用了相減（{9-16}）——開不出方根就該發現用錯式，雙曲線是相加。"
            "② 因為 {b=4>3=a} 就把 {a} 當成 4：雙曲線的 a 看減號「前面」那一項，不看大小。"
            "③ 漸近線寫成 {y=+-frac(a,b)x}——橫向雙曲線是 {frac(b,a)}。"
            "④ (b) 答成 {d_2=-4} 或者兩個都寫：距離不能是負數。"),
    5: dict(
        ans="（a）拋物線、開口向下、頂點 {(0,2)}　（b）拋物線、開口向左、頂點 {(0,0)}　"
            "（c）圓、圓心 {(0,0)}、半徑 2",
        kp="拋物線先看哪個變數是二次（x 二次 → 上下、y 二次 → 左右），"
           "再看係數正負（正 → 上／右，負 → 下／左）。"
           "(c) 是陷阱題：兩項相加等於 1，但「兩個分母相同」，化簡後是圓不是橢圓。",
        fm="{y=ax^2+k} 上下開口；{x=ay^2} 左右開口；"
           "{frac(x^2,r^2)+frac(y^2,r^2)=1} ⇔ {x^2+y^2=r^2}（圓）。",
        steps=["（a）x 是二次 → 上下開口；係數 {-1<0} → 開口向下；頂點 {(0,2)}。"
               "檢核：令 {y=0} 得 {x^2=2}，{x=+-sqrt(2)≈+-1.41}，"
               "圖上與 x 軸交於 {(+-sqrt(2),0)} ✔",
               "（b）y 是二次 → 左右開口；係數 {-8<0} → 開口向左；頂點 {(0,0)}。"
               "檢核：取 {y=2} → {4=-8x} → {x=-0.5}；取 {y=4} → {16=-8x} → {x=-2}。"
               "兩點都在 y 軸左邊 ✔",
               "（c）兩個分母相同（都是 4），乘開得 {x^2+y^2=4} → 圓，"
               "圓心 {(0,0)}、半徑 2。（此時 {a=b}，{c=0}、{e=0}。）"
               "檢核：{(+-2,0)}、{(0,+-2)} 四點到原點的距離都是 2 ✔"],
        pit="① (b) 看到 {y^2} 仍然畫成上下開口——是 y 二次，開口在左右。"
            "② (b) 只看到負號就答「開口向下」：左右開口的負號是「向左」。"
            "③ (c) 見到「相加 = 1」就寫橢圓——先看兩個分母是不是相同。"
            "④ (a) 頂點答成 {(0,-2)}：{y=-x^2+2} 的常數項是 {+2}。"),
    6: dict(
        ans="{frac(y^2,16)-frac(x^2,9)=1}",
        kp="共同漸近線 ⇔ 左邊兩個分母不變、只有右邊的常數不同。"
           "所以設 {frac(x^2,9)-frac(y^2,16)=k}，代點求 k，再除以 k 化回標準式。"
           "本題 k 是負數，曲線會由橫向轉成縱向。",
        fm="同漸近線族 {frac(x^2,A)-frac(y^2,B)=k}（{k!=0}）；"
           "橫向漸近線 {y=+-frac(b,a)x}，縱向漸近線 {y=+-frac(a,b)x}。",
        steps=["第 1 步：設同漸近線族 {frac(x^2,9)-frac(y^2,16)=k}（左邊分母不動）。",
               "第 2 步：代入 {P(3,4sqrt(2))}："
               "{frac(3^2,9)-frac((4sqrt(2))^2,16)=frac(9,9)-frac(32,16)=1-2=-1}，"
               "所以 {k=-1}。（{(4sqrt(2))^2=16*2=32}，根號先平方掉。）",
               "第 3 步：{frac(x^2,9)-frac(y^2,16)=-1} 兩邊除以 −1，"
               "「每一項都要變號」 → {-frac(x^2,9)+frac(y^2,16)=1}，"
               "整理成 {frac(y^2,16)-frac(x^2,9)=1}。",
               "第 4 步（檢查）：① 代 P：{frac(32,16)-frac(9,9)=2-1=1} ✔ "
               "② 新曲線是縱向（減號前面是 y），{a=4}、{b=3}，"
               "漸近線 {y=+-frac(a,b)x=+-frac(4,3)x}；"
               "原曲線橫向、{a=3}、{b=4}，漸近線 {y=+-frac(b,a)x=+-frac(4,3)x} ✔ 相同。"],
        pit="① 見到 {k=-1} 就以為做錯——k 是負數很正常，只代表曲線轉了 90 度。"
            "② 除以 −1 時只變其中一項的號。"
            "③ 代入時 {(4sqrt(2))^2} 算成 {4*2=8} 或 {8}——要 {16*2=32}。"
            "④ 檢查漸近線時用錯式：縱向雙曲線是 {frac(a,b)}，橫向才是 {frac(b,a)}。"),
}


# ================================================================ docx
def build_practice_docx():
    figdir = os.path.join(HERE, "_figtmp2")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    def img(svg, name, cm):
        png = os.path.join(figdir, name + ".png")
        ds.svg_to_png(svg, png, scale=3)
        return expand_image(image_para(png, width_cm=cm), MEDIA)

    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para("每題下方標明了該翻哪一張提示卡。第 2 題附了已畫好的圖，"
                  "先在圖上量一量，再用公式算，兩邊要對得上。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        if n == 2:
            P.append(img(FIG_Q2, "q2", 7.0))
        P.append(shaded_box(CARD_HINT[n]))
        P += write_lines(LINES[n])
        P.append(blank())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(para("由這一節開始不再標明翻哪一張卡，要自己認出是哪一種曲線；"
                  "圖也不再畫好，建議先在旁邊畫個大概再算。"
                  "兩張手順卡的關鍵詞只在下面重印一次。"))
    P.append(step_card(STEP_TITLE, STEP_COMPACT, trigger=STEP_TRIGGER, compact=True))
    P.append(shaded_box(STEP_WARN))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P += write_lines(LINES[n])
        P.append(blank())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para("本節收起工具卡。第 5 題三個小題都要自己畫草圖"
                  "（先定頂點或圓心，再定開口方向或半徑），"
                  "草圖畫在作答區的上半部；第 6 題代入後算出的 k 是負數，"
                  "不要以為自己做錯——照手順卡二第 3 步做下去就對。"))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        lead = ("作答（上半畫三個小草圖 → 下半寫種類、開口方向與頂點／圓心）："
                if n == 5 else "作答（設 k 族 → 代點求 k → 除以 k 化標準式 → 檢查）：")
        P.append(para(lead))
        P += write_lines(LINES[n])
        P.append(blank())

    P.append(heading("參考答案與詳解（教師用）", page_break_before=True))
    for n in range(1, 7):
        a = ANS[n]
        P.append(para("%d．答案：%s" % (n, a["ans"]), bold=True))
        P.append(para("【考點】" + a["kp"]))
        P.append(para("【公式／定理】" + a["fm"]))
        P.append(para("【詳細步驟】"))
        for i, s in enumerate(a["steps"], 1):
            P.append(para("　（%d）%s" % (i, s)))
        P.append(shaded_box("【易錯點提示】" + a["pit"]))
        P.append(blank())

    out = build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=MEDIA)
    shutil.rmtree(figdir, ignore_errors=True)
    return out


# ================================================================ 工具卡
# 前三張＝講義那三張 D7 提示卡的桌面版（含小圖）；第四張是橫向比較速查。
# 速查卡刻意用橫式 Unicode（÷、上標），不用 OMML 分數——分數會把卡片行距疊高。
TC_TEXT = [
    ("▍提示卡一・橢圓", "兩項相加 ＝ 1，或 0 ＜ e ＜ 1。",
     ["標準式 {frac(x^2,a^2)+frac(y^2,b^2)=1}（{a>b}）",
      "a² ＝ 較大的分母；長軸跟着大分母走",
      "c² ＝ a² − b²（減）　e ＝ c ÷ a（0＜e＜1）",
      "兩準線距離 ＝ 2a² ÷ c",
      "※ 焦點在長軸上、c ＜ a；到兩焦點的距離之和 ＝ 2a。"]),
    ("▍提示卡二・雙曲線", "兩項相減 ＝ 1，或 e ＞ 1，或提到漸近線。",
     ["標準式 {frac(x^2,a^2)-frac(y^2,b^2)=1}",
      "a² ＝ 減號前面那一項的分母（不看大小）",
      "c² ＝ a² + b²（加）　e ＝ c ÷ a（e＞1）",
      "漸近線：橫向 y ＝ ±(b÷a)x；縱向 y ＝ ±(a÷b)x",
      "※ c ＞ a；到兩焦點距離之差的絕對值 ＝ 2a。"]),
    ("▍提示卡三・拋物線", "只有一個變數是二次，或 e ＝ 1。",
     ["{y=ax^2+k}：x 二次 → 上下開口，頂點 (0, k)",
      "{x=ay^2}：y 二次 → 左右開口，頂點在原點",
      "係數正 → 朝正方向（上／右）",
      "係數負 → 朝負方向（下／左）",
      "※ 沒有 a、b、c；先整理成 y＝ 或 x＝ 才看係數正負。"]),
    ("▍速查卡・三種曲線比一比", "算完之後用這張檢查有沒有用錯式。",
     ["相加 ＝ 1 → 橢圓　相減 ＝ 1 → 雙曲線",
      "只有一個變數二次 → 拋物線",
      "兩個分母相同的相加 → 圓（不是橢圓）",
      "c²：橢圓「減」（c＜a）／雙曲線「加」（c＞a）",
      "e：橢圓 0～1　拋物線 ＝1　雙曲線 ＞1",
      "※ a：橢圓看分母大小、雙曲線看減號位置。"]),
]


def build_toolcard_docx():
    figdir = os.path.join(HERE, "_figtmp3")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    def img(svg, name):
        png = os.path.join(figdir, name + ".png")
        ds.svg_to_png(svg, png, scale=3)
        return expand_image(image_para(png, width_cm=3.5), MEDIA)

    figs = [img(FIG_TC_E, "te"), img(FIG_TC_H, "th"), img(FIG_TC_P, "tp"), None]
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for (title, trig, items), f in zip(TC_TEXT, figs):
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        if f is not None:
            c.append(f)
        c += [para("・" + t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=5200))
    out = build_docx(P, os.path.join(HERE, CARDF + ".docx"), footer_text=FOOT, media=MEDIA)
    shutil.rmtree(figdir, ignore_errors=True)
    return out


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _split_args(s, start):
    depth, args, cur, i = 0, [], [], start
    while i < len(s):
        c = s[i]
        if c == "(":
            depth += 1
            if depth == 1:
                i += 1
                continue
        elif c == ")":
            depth -= 1
            if depth == 0:
                args.append("".join(cur))
                return args, i + 1
        elif c == "," and depth == 1:
            args.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(c)
        i += 1
    return None, start


def _conv(s):
    out, i = [], 0
    while i < len(s):
        if s.startswith("frac(", i):
            args, end = _split_args(s, i + 4)
            if args and len(args) == 2:
                out.append("\\frac{%s}{%s}" % (_conv(args[0]), _conv(args[1])))
                i = end
                continue
        if s.startswith("sqrt[", i):
            j = s.find("]", i)
            if j > 0 and j + 1 < len(s) and s[j + 1] == "(":
                args, end = _split_args(s, j + 1)
                if args and len(args) == 1:
                    out.append("\\sqrt[%s]{%s}" % (s[i + 5:j], _conv(args[0])))
                    i = end
                    continue
        if s.startswith("sqrt(", i):
            args, end = _split_args(s, i + 4)
            if args and len(args) == 1:
                out.append("\\sqrt{%s}" % _conv(args[0]))
                i = end
                continue
        out.append(s[i])
        i += 1
    return "".join(out)


def _tex(m):
    import re
    body = m.strip()
    body = re.sub(r"fn\((\w+)\)", r"\\\1 ", body)
    body = _conv(body)
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    body = body.replace("Δ", r"\Delta ")
    body = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", body)
    body = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", body)
    body = re.sub(r"\^(\w{2,})", r"^{\1}", body)
    body = re.sub(r"_(\w{2,})", r"_{\1}", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    body = body.replace("<", r" \lt ").replace(">", r" \gt ")
    body = re.sub(r"(?<![\\{\w.])(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)(?![}\w.])",
                  r"\\frac{\1}{\2}", body)
    body = body.replace("%", r"\%")
    return r"\(%s\)" % body


def _h(s):
    """{} 內轉 TeX，其餘轉義。`**` 兩版都不支援（docx 的 para() 會原印星號），先剝走。"""
    import re
    s = s.replace("**", "")
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def _step_compact_html():
    rows = "".join("<tr><td>%d. %s</td></tr>" % (i, _h(t))
                   for i, t in enumerate(STEP_COMPACT, 1))
    return ('<table class="d-tbl step-card compact"><tr><th>%s</th></tr>'
            '<tr><td>什麼時候用：%s</td></tr>%s</table>'
            % (_esc(STEP_TITLE), _esc(STEP_TRIGGER), rows))


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "練習：" + UNIT)
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .step-card.compact td:first-child { width: 100%; font-weight: 400; }
  .qfig { text-align: center; margin: 6px 0; }
  .qfig svg { max-width: 100%; height: auto; }
</style>
</head>""")

    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂練習</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')
    parts.append('<div class="hint-card">%s</div>' % _h(HINT_TOP))

    parts.append('<div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>')
    parts.append('<div>每題下方標明了該翻哪一張提示卡。第 2 題附了已畫好的圖，'
                 '先在圖上量一量，再用公式算，兩邊要對得上。</div>')
    for n in A_ITEMS:
        fig = ('<div class="qfig">%s</div>' % FIG_Q2) if n == 2 else ""
        parts.append('<div class="problem"><div>%d．%s</div>%s'
                     '<div class="hint-card">%s</div>%s</div>'
                     % (n, _h(STEMS[n]), fig, _h(CARD_HINT[n]), _lines(LINES[n])))

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div>由這一節開始不再標明翻哪一張卡，要自己認出是哪一種曲線；'
                 '圖也不再畫好，建議先在旁邊畫個大概再算。'
                 '兩張手順卡的關鍵詞只在下面重印一次。</div>')
    parts.append(_step_compact_html())
    parts.append('<div class="hint-card">%s</div>' % _h(STEP_WARN))
    for n in B_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _lines(LINES[n])))

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>本節收起工具卡。第 5 題三個小題都要自己畫草圖'
                 '（先定頂點或圓心，再定開口方向或半徑），草圖畫在作答區的上半部；'
                 '第 6 題代入後算出的 k 是負數，不要以為自己做錯——'
                 '照手順卡二第 3 步做下去就對。</div>')
    for n in C_ITEMS:
        lead = ("作答（上半畫三個小草圖 → 下半寫種類、開口方向與頂點／圓心）：" if n == 5
                else "作答（設 k 族 → 代點求 k → 除以 k 化標準式 → 檢查）：")
        parts.append('<div class="problem"><div>%d．%s</div><div>%s</div>%s</div>'
                     % (n, _h(STEMS[n]), lead, _lines(LINES[n])))

    parts.append('<div class="section-h page-break">參考答案與詳解（教師用）</div>')
    for n in range(1, 7):
        a = ANS[n]
        steps = "".join("<div>　（%d）%s</div>" % (i, _h(s))
                        for i, s in enumerate(a["steps"], 1))
        parts.append('<div class="problem"><div style="font-weight:700">%d．答案：%s</div>'
                     '<div>【考點】%s</div><div>【公式／定理】%s</div>'
                     '<div>【詳細步驟】</div>%s'
                     '<div class="hint-card">【易錯點提示】%s</div></div>'
                     % (n, _h(a["ans"]), _h(a["kp"]), _h(a["fm"]), steps, _h(a["pit"])))

    parts.append('<div class="footer">' + _esc(FOOT) + '</div>')

    body = ("\n<body>\n<div class=\"page\">\n\n" + "\n\n".join(parts)
            + "\n\n</div>\n</body>\n</html>\n")
    path = os.path.join(HERE, BASE + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_practice_docx())
    print(build_toolcard_docx())
    print(build_practice_html())
