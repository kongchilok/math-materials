# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L8 解析幾何（一）直線與圓 —— 課堂練習 ＋ 工具卡 build script
主設計 D5 圖文雙軌（褪除：A 附已畫好的坐標圖 → B 只給空白坐標格 → C 自己畫草圖）；
輔助 D2 手順卡（A 每題標明用哪張卡 → B 只在區塊開頭重印一次 → C 不印）、
D9 草稿分區（A、B 的作答區就是印好格名的四格，C 回到一般作答行）。
鷹架密度：抽離小班 (Tier 2)。

本份**不放 D12 自我核對清單**：四格的第 ④ 格「代回檢查」已經是逐題的自我核對，
再加一層就會變成主 1 ＋ 輔 3，違反 teaching-designs.md §0 的鐵律上限。

產出：練習_直線與圓_抽離小班共用版.docx/.html、工具卡_直線與圓.docx
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
BASE = "練習_直線與圓_抽離小班共用版"
CARDF = "工具卡_直線與圓"
UNIT = "第2章 中學基礎數學應用．L8 解析幾何（一）直線與圓"
FOOT = "高三數學．" + UNIT

# ================================================================ 圖
# 練習A：圖已經畫好，學生只要讀圖＋套公式（D5 褪除第一級）
FIG_Q1 = coord_svg([
    {"t": "point", "x": -4, "y": 1, "label": "A(−4, 1)", "lp": "nw"},
    {"t": "point", "x": 2, "y": 9, "label": "B(2, 9)", "lp": "ne"},
], xlo=-6, xhi=4, ylo=-2, yhi=10, unit=19)

FIG_Q2 = coord_svg([
    {"t": "line", "a": 4, "b": -2, "c": 6, "label": "L", "at": 1.4, "ldy": 14},
], xlo=-5, xhi=3, ylo=-3, yhi=6, unit=19)

# 練習B：只給空白坐標格，圖由學生自己畫（D5 褪除第二級）
FIG_BLANK = coord_svg([], xlo=-6, xhi=6, ylo=-6, yhi=6, unit=20)

# ================================================================ 題目
HINT_TOP = ("動筆之前先認出題型：求直線方程（給了一點＋斜率／兩點／一點＋平行或垂直的線）"
            "→ 手順卡一；問直線與圓的交點個數或位置關係 → 手順卡二；"
            "其餘的量（到坐標軸距離、兩點距離、中點、斜率、截距）→ 翻速查卡直接代公式。"
            "本課的第一個動作永遠是「先看圖」。")

STEP_TITLE = "兩張手順卡（關鍵詞版）"
STEP_TRIGGER = "先認出題型，再照對應那一行做。"
STEP_COMPACT = [
    "求直線方程：認出給法（點＋斜率／兩點／垂直） → 先求 m → 代點斜式 "
    "{y-y_1=m(x-x_1)} → 整理成 {ax+by+c=0} → 把點代回檢查",
    "直線與圓：抄圓心 {(h,k)} 與 {r} → 代入消元求 {Δ}（或算 "
    "{d=frac(|ax_0+by_0+c|,sqrt(a^2+b^2))}）→ "
    "{Δ>0}／{d<r} 相交，{Δ=0}／{d=r} 相切，{Δ<0}／{d>r} 相離",
]
STEP_WARN = ("※ 垂直的斜率是負倒數（相乘 = −1），不是把負號拿掉。"
             "※ 圓標準式括號內是減號，{(x+2)^2} 的圓心坐標是 −2；右邊是 {r^2} 不是 {r}。")

STEMS = {
    1: "已知 {A(-4,1)}、{B(2,9)}（圖已畫好，兩點都標了出來）。"
       "（a）A 到 x 軸、y 軸的距離各是多少？（b）求 {|AB|}。（c）求 AB 的中點 M。",
    2: "已知直線 {L: 4x-2y+6=0}（圖已畫好）。（a）求 L 的斜率。（b）求 L 的 y 截距。",
    3: "求下列直線方程（答案寫成一般式 {ax+by+c=0}）："
       "（a）過點 {P(3,-2)} 且斜率為 −1；（b）過點 {A(-1,2)} 與 {B(3,10)}。",
    4: "求下列圓方程（答案寫成標準式）："
       "（a）圓心 {C(-2,3)}、半徑 4；（b）以 {A(1,-2)} 與 {B(7,6)} 為直徑的兩端。",
    5: "判斷直線 {L: x-y+4=0} 與圓 {C: (x-1)^2+(y-2)^2=9} 的位置關係"
       "（相交／相切／相離），並求出交點（若有）。"
       "※ 請先在作答區畫一張草圖（圓心與半徑先標出來），再動筆計算。",
    6: "已知直線 {L_1: 2x+y-5=0} 與點 {P(1,4)}。"
       "（a）求過 P 且垂直於 {L_1} 的直線 {L_2} 的方程。"
       "（b）判斷 {L_2} 與圓 {C: x^2+y^2=5} 的位置關係。",
}

# 練習A：D2 褪除第一級——標明用哪一張卡／哪一張速查卡
CARD_HINT = {
    1: "▍翻速查卡一（坐標平面的五個量）：到 x 軸的距離看 y、到 y 軸看 x；"
       "兩點距離先算兩個差再平方；中點是兩個坐標各自取平均。"
       "每算一個，回到圖上看一眼對不對。",
    2: "▍翻速查卡一：斜率可以用 {m=-frac(a,b)}，也可以把方程化成 {y=mx+k} 直接讀 m；"
       "y 截距就是令 {x=0}（線與 y 軸相交的地方，x 一定是 0）。",
}

# D9 四格的格名（按題型換第②③格，第①④格固定）
QUAD = {
    1: ("① 抄下已知（兩點坐標，連負號）", "② 這一小題要用哪一條公式",
        "③ 計算（一小題一塊）", "④ 回到圖上對一眼：答案合理嗎"),
    2: ("① 抄下已知（直線方程的 a、b、c）", "② 化成 {y=mx+k}，或用 {m=-frac(a,b)}",
        "③ 計算斜率與 y 截距", "④ 代回原方程檢查"),
    3: ("① 抄下已知（點的坐標／斜率）", "② 先把斜率 m 弄到手",
        "③ 代點斜式，整理成一般式", "④ 把點代回答案檢查（兩點題兩個都代）"),
    4: ("① 抄下已知（圓心／半徑／兩端點）", "② 求出圓心 {(h,k)} 與 {r^2}",
        "③ 代標準式 {(x-h)^2+(y-k)^2=r^2}", "④ 把已知的點代回檢查"),
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
LINES = {5: 9, 6: 8}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）到 x 軸 1、到 y 軸 4　（b）{|AB|=10}　（c）{M(-1,5)}",
        kp="坐標平面上的三個基本量。到 x 軸的距離量的是上下高度（看 y），"
           "到 y 軸的距離量的是左右寬度（看 x）；兩點距離是把兩點補成直角三角形後的斜邊；"
           "中點是兩個坐標各自取平均。",
        fm="到 x 軸 {=|y|}、到 y 軸 {=|x|}；{|AB|=sqrt((x_2-x_1)^2+(y_2-y_1)^2)}；"
           "中點 {=(frac(x_1+x_2,2),frac(y_1+y_2,2))}。",
        steps=["（a）{A(-4,1)}：到 x 軸的距離 {=|1|=1}；到 y 軸的距離 {=|-4|=4}。"
               "圖上檢核：由 A 往下垂到 x 軸只走 1 格，往右垂到 y 軸走 4 格 ✔",
               "（b）水平差 {=2-(-4)=6}，垂直差 {=9-1=8}。"
               "{|AB|=sqrt(6^2+8^2)=sqrt(36+64)=sqrt(100)=10}（又是 6-8-10 直角三角形）。",
               "（c）{M=(frac(-4+2,2),frac(1+9,2))=(frac(-2,2),frac(10,2))=(-1,5)}。",
               "檢核：{|AM|=sqrt((-1+4)^2+(5-1)^2)=sqrt(9+16)=5}，"
               "{|MB|=sqrt((2+1)^2+(9-5)^2)=sqrt(9+16)=5}，兩段相等且合共 10 ✔"],
        pit="① (a) 對調：到 x 軸用 y、到 y 軸用 x，不要反。"
            "② 距離抄成負數：{|-4|=4}，距離永遠是正的。"
            "③ (b) 只把坐標相減不平方，或平方後忘記開方。"
            "④ (c) 把中點寫成兩坐標相減除以 2——是相加取平均。"),
    2: dict(
        ans="（a）斜率 {=2}　（b）y 截距 {=3}",
        kp="由一般式 {ax+by+c=0} 讀斜率有兩條路：化成斜截式 {y=mx+k} 直接讀，"
           "或用 {m=-frac(a,b)}。y 截距就是令 {x=0} 求出的 y。",
        fm="{m=-frac(a,b)}（{b!=0}）；斜截式 {y=mx+k} 中 {k} 即 y 截距；"
           "y 截距：令 {x=0}；x 截距：令 {y=0}。",
        steps=["（a）化斜截式：{4x-2y+6=0} → {-2y=-4x-6} → {y=2x+3}，所以 {m=2}。",
               "（a）公式檢核：{m=-frac(a,b)=-frac(4,-2)=2} ✔ 兩個負號相消，答案是正的。",
               "（b）令 {x=0}：{-2y+6=0} → {y=3}，即交 y 軸於 {(0,3)}，y 截距 = 3。"
               "由斜截式 {y=2x+3} 直接讀常數項也是 3 ✔",
               "附帶檢核：令 {y=0} 得 {4x+6=0}，{x=-frac(3,2)}；"
               "由 {(-frac(3,2),0)} 到 {(0,3)} 的斜率 {=frac(3-0,0+frac(3,2))=2} ✔"],
        pit="① {m=-frac(a,b)} 漏掉外面那個負號，答成 {-2}。"
            "② {b=-2} 抄成 {2}（一般式的 b 要連負號一起抄）。"
            "③ 把 y 截距答成點 {(0,3)} 沒關係，但答成 {x=3} 就錯了——截距是那個數值 3。"),
    3: dict(
        ans="（a）{x+y-1=0}　（b）{2x-y+4=0}",
        kp="求直線方程的三種給法，本題考前兩種。不論哪一種，"
           "拿到斜率之後都是代點斜式再整理成一般式。",
        fm="點斜式 {y-y_1=m(x-x_1)}；兩點求斜率 {m=frac(y_2-y_1,x_2-x_1)}。",
        steps=["（a）給法①：一點＋斜率。{y-(-2)=-1(x-3)} → {y+2=-x+3} → {x+y-1=0}。",
               "（a）檢核：代 {P(3,-2)}：{3+(-2)-1=0} ✔；斜率 {=-frac(1,1)=-1} ✔",
               "（b）給法②：兩點。先求斜率 {m=frac(10-2,3-(-1))=frac(8,4)=2}。"
               "代點斜式（用 A）：{y-2=2(x+1)} → {y=2x+4} → {2x-y+4=0}。",
               "（b）檢核：代 {A(-1,2)}：{-2-2+4=0} ✔；代 {B(3,10)}：{6-10+4=0} ✔。"
               "改用 B 點列式也得同一條：{y-10=2(x-3)} → {y=2x+4} ✔"],
        pit="① (a) 負坐標代錯：{y_1=-2}，所以左邊是 {y-(-2)=y+2}，不是 {y-2}。"
            "② (b) 斜率上下顛倒，寫成 {frac(x_2-x_1,y_2-y_1)}。"
            "③ 停在 {y=2x+4} 沒有整理成一般式（題目要求一般式）。"
            "④ 兩點題只代一個點檢查——兩個都要代，才抓得出斜率算錯。"),
    4: dict(
        ans="（a）{(x+2)^2+(y-3)^2=16}　（b）{(x-4)^2+(y-2)^2=25}",
        kp="圓標準式 {(x-h)^2+(y-k)^2=r^2}：圓心 {(h,k)} 代進括號要變號，"
           "等號右邊放的是 {r^2}。直徑兩端的題，圓心是中點、半徑是直徑的一半。",
        fm="{(x-h)^2+(y-k)^2=r^2}；直徑兩端 → 圓心 = 中點、{r=frac(|AB|,2)}。",
        steps=["（a）{h=-2}、{k=3}、{r=4}。{x-(-2)=x+2}，{r^2=16}"
               " → {(x+2)^2+(y-3)^2=16}。"
               "檢核：取圓上一點 {(2,3)}（圓心右移 4）：{(2+2)^2+0=16} ✔",
               "（b）圓心 = AB 中點 {=(frac(1+7,2),frac(-2+6,2))=(4,2)}。",
               "（b）{|AB|=sqrt((7-1)^2+(6-(-2))^2)=sqrt(36+64)=10}，"
               "所以 {r=5}、{r^2=25} → {(x-4)^2+(y-2)^2=25}。",
               "（b）檢核：代 {A(1,-2)}：{(1-4)^2+(-2-2)^2=9+16=25} ✔；"
               "代 {B(7,6)}：{(7-4)^2+(6-2)^2=9+16=25} ✔"],
        pit="① 圓心符號不變號：{C(-2,3)} 寫成 {(x-2)^2}——應該是 {(x+2)^2}。"
            "② 右邊寫成 {r} 不是 {r^2}：半徑 4 → 右邊是 16。"
            "③ (b) 把 {|AB|=10} 當成半徑——那是直徑，半徑是 5。"
            "④ (b) 圓心用了 A 或 B 的坐標——圓心是它們的中點。"),
    5: dict(
        ans="相交；交點 {(-2,2)} 與 {(1,5)}",
        kp="直線與圓的位置關係有兩條路：代入消元算 {Δ}（要求交點就走這條），"
           "或算圓心到直線的距離 d 跟 r 比（只問關係就走這條）。本題要求交點，"
           "所以走代入法，再用距離法檢核。",
        fm="{Δ=b^2-4ac}：{Δ>0} 相交、{Δ=0} 相切、{Δ<0} 相離；"
           "{d=frac(|ax_0+by_0+c|,sqrt(a^2+b^2))}，{d<r} 相交、{d=r} 相切、{d>r} 相離。",
        steps=["草圖：圓心 {C(1,2)}、{r=3}；直線 {y=x+4} 過 {(0,4)}、{(-4,0)}，"
               "由左下往右上。畫出來就看得到它穿過圓。",
               "代入法：{y=x+4} 代進 {(x-1)^2+(y-2)^2=9} → {(x-1)^2+(x+2)^2=9} → "
               "{x^2-2x+1+x^2+4x+4=9} → {2x^2+2x-4=0} → {x^2+x-2=0}"
               "（兩邊先除以 2，數字小些不易錯）。",
               "{Δ=1^2-4(1)(-2)=1+8=9>0} → 相交於兩點。"
               "{(x+2)(x-1)=0} → {x=-2} 或 {x=1}；代回 {y=x+4} 得交點 "
               "{(-2,2)} 與 {(1,5)}。",
               "距離法檢核：{d=frac(|1-2+4|,sqrt(1^2+(-1)^2))=frac(3,sqrt(2))≈2.12<3=r} "
               "✔ 兩法結論一致。",
               "驗點：{(-2-1)^2+(2-2)^2=9+0=9} ✔（圓的最左點）；"
               "{(1-1)^2+(5-2)^2=0+9=9} ✔（圓的最上點）。"],
        pit="① 沒畫圖就硬代，代錯一個括號整題報廢——本題明寫要先畫草圖。"
            "② 代入後沒有整理成「一邊為 0」就數 {a}、{b}、{c}。"
            "③ 求出 x 之後忘記代回求 y，只答 {x=-2}、{x=1}。"
            "④ 圓心讀錯：{(x-1)^2+(y-2)^2} 的圓心是 {(1,2)} 不是 {(-1,-2)}。"),
    6: dict(
        ans="（a）{x-2y+7=0}　（b）相離（沒有交點）",
        kp="兩步整合題：先用「垂直斜率是負倒數」求出 {L_2}，"
           "再用距離法（或判別式）判斷 {L_2} 與圓的關係。"
           "本題不必求交點，所以距離法比代入法快。",
        fm="垂直 ⇔ {m_1*m_2=-1}；點斜式 {y-y_1=m(x-x_1)}；"
           "{d=frac(|ax_0+by_0+c|,sqrt(a^2+b^2))}，{d>r} 相離。",
        steps=["（a）{L_1: 2x+y-5=0} 的斜率 {m_1=-frac(a,b)=-frac(2,1)=-2}。"
               "垂直 → {m_2=frac(-1,-2)=frac(1,2)}。",
               "（a）點斜式：{y-4=frac(1,2)(x-1)} → 兩邊乘 2：{2y-8=x-1} → "
               "{x-2y+7=0}。"
               "檢核：代 {P(1,4)}：{1-8+7=0} ✔；{m_1*m_2=(-2)(frac(1,2))=-1} ✔",
               "（b）圓 {x^2+y^2=5} 的圓心 {O(0,0)}、{r=sqrt(5)≈2.24}。"
               "{d=frac(|0-0+7|,sqrt(1^2+(-2)^2))=frac(7,sqrt(5))≈3.13>sqrt(5)} "
               "→ 相離，沒有交點。",
               "（b）判別式檢核：{x=2y-7} 代入 → {(2y-7)^2+y^2=5} → "
               "{5y^2-28y+44=0}，{Δ=(-28)^2-4(5)(44)=784-880=-96<0} ✔ 無實根，"
               "與距離法一致。"],
        pit="① 垂直斜率只變號不取倒數（答成 2）或只取倒數不變號（答成 {-frac(1,2)}）。"
            "② {d} 的分母用了點的坐標——分母是 {sqrt(a^2+b^2)}，"
            "{a}、{b} 是直線方程的係數。"
            "③ 分子忘記加絕對值，算出負數就直接拿去跟 r 比。"
            "④ 把 {r} 讀成 5——{x^2+y^2=5} 的右邊是 {r^2}，{r=sqrt(5)}。"),
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
    P.append(para("圖已經畫好了，先看圖再動筆。作答區是四格草稿："
                  "把「抄已知／選公式／計算／檢查」各放一格，不要混在一起寫。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(img(FIG_Q1 if n == 1 else FIG_Q2, "q%d" % n,
                     6.2 if n == 1 else 5.8))
        P.append(shaded_box(CARD_HINT[n]))
        P.append(quadrant_workspace(QUAD[n]))
        P.append(blank())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(para("由這一節開始不再標明用哪一張卡，要自己認出題型；"
                  "坐標圖也不再畫好，只給空白格，圖要自己畫上去。"
                  "兩張卡的關鍵詞只在下面重印一次。"))
    P.append(step_card(STEP_TITLE, STEP_COMPACT, trigger=STEP_TRIGGER, compact=True))
    P.append(shaded_box(STEP_WARN))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(img(FIG_BLANK, "blank%d" % n, 5.6))
        P.append(para("（上面的空白格自己畫圖用；下面四格是草稿。）", sz=21))
        P.append(quadrant_workspace(QUAD[n]))
        P.append(blank())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para("本節收起工具卡，也不給坐標格。第 5 題要自己畫草圖"
                  "（圓心、半徑、直線各標出來）再計算；"
                  "第 6 題兩小題環環相扣，(a) 算錯 (b) 一定跟着錯，"
                  "所以 (a) 做完先用「兩斜率相乘 = −1」檢查一次再往下。"))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        lead = ("作答（先畫草圖 → 代入或算 d → 下判斷 → 求交點）："
                if n == 5 else "作答（(a) 求斜率 → 代點斜式 → 檢查；(b) 算 d 跟 r 比）：")
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
# 速查卡的公式刻意用橫式 Unicode（÷、√、上下標字元），不用 OMML 分數：
# 分數式會把卡片行距疊高（L4 實測，一條頂兩條），四張卡就排不進一頁。
CARDS = [
    ("▍手順卡一・求直線方程",
     "什麼時候翻我：要求某條直線的方程。",
     ["1　認出給法：①點＋斜率　②兩點　③點＋平行／垂直的線",
      "2　先把斜率 m 弄到手（②m ＝(y₂−y₁)÷(x₂−x₁)；③垂直取負倒數）",
      "3　代點斜式 {y-y_1=m(x-x_1)}",
      "4　整理成 {ax+by+c=0}，再把點代回檢查",
      "※ 垂直＝負倒數，相乘要等於 −1。",
      "※ 負坐標連負號一起代：(−2, 3) → y − 3 ＝ m(x + 2)。"]),
    ("▍手順卡二・直線與圓的位置關係",
     "什麼時候翻我：問交點個數、相交／相切／相離，或要求交點。",
     ["1　抄出圓心 {(h,k)} 與半徑 {r}",
      "2　要交點 → 代入消元，化成一元二次，算 {Δ=b^2-4ac}",
      "3　只問關係 → 算 d ＝ |ax₀+by₀+c| ÷ √(a²+b²)，跟 r 比",
      "4　Δ＞0／d＜r 相交　Δ＝0／d＝r 相切　Δ＜0／d＞r 相離",
      "※ 兩條路線的結論一定相同，有時間就互相檢核。",
      "※ 括號內是減號：(x+2)² 的圓心坐標是 −2。"]),
    ("▍速查卡一・坐標平面的五個量",
     "什麼時候翻我：題目問距離、中點、斜率、截距。",
     ["到 x 軸的距離 ＝ |y|　　到 y 軸的距離 ＝ |x|",
      "兩點距離 ＝ √((x₂−x₁)² + (y₂−y₁)²)",
      "中點 ＝ ((x₁+x₂)÷2 , (y₁+y₂)÷2)",
      "斜率 m ＝ (y₂−y₁)÷(x₂−x₁) ＝ −a÷b",
      "y 截距：令 x ＝ 0　　x 截距：令 y ＝ 0",
      "※ 到 x 軸看 y，別對調。距離永遠是正數。",
      "※ m ＝ −a÷b 那個負號別漏。"]),
    ("▍速查卡二・圓與距離",
     "什麼時候翻我：題目出現圓，或要算點到直線的距離。",
     ["圓標準式：{(x-h)^2+(y-k)^2=r^2}，圓心 {(h,k)}",
      "直徑兩端 → 圓心 ＝ 中點，r ＝ 直徑 ÷ 2",
      "點到直線距離 d ＝ |ax₀ + by₀ + c| ÷ √(a² + b²)",
      "直線與圓：d ＜ r 相交　d ＝ r 相切　d ＞ r 相離",
      "兩圓：d 跟 r₁+r₂、|r₁−r₂| 比",
      "※ 圓心代進括號要變號。",
      "※ 等號右邊是 r²，不是 r。"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in CARDS:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        c += [para("・" + t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=4400))
    return build_docx(P, os.path.join(HERE, CARDF + ".docx"), footer_text=FOOT)


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
    """{} 內轉 TeX，其餘轉義。**粗體** 這種 markdown 語法兩版都不支援
    （docx 的 para() 會原樣印出星號），所以先剝走星號再處理。"""
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


def _quad_html(labels):
    def cell(t):
        return ('<td><div class="qlab">%s</div><div class="qspace"></div></td>'
                % _h(t))
    return ('<table class="d-tbl quadrant"><tr>%s%s</tr><tr>%s%s</tr></table>'
            % (cell(labels[0]), cell(labels[1]), cell(labels[2]), cell(labels[3])))


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
  .quadrant td { width: 50%; vertical-align: top; padding: 0; }
  /* 格名與作答空間必須在同一個 td——拆成「標題列＋空白列」兩列時，
     分頁會把格名留在上一頁、空間丟到下一頁（omml_docx 那邊踩過同樣的坑）。 */
  .qlab { background: #f0f0f0; font-size: 10.5pt; padding: 3px 8px; }
  .qspace { height: 2.9cm; }
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
    parts.append('<div>圖已經畫好了，先看圖再動筆。作答區是四格草稿：'
                 '把「抄已知／選公式／計算／檢查」各放一格，不要混在一起寫。</div>')
    for n in A_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div></div>' % (n, _h(STEMS[n])))
        parts.append('<div class="qfig">%s</div>' % (FIG_Q1 if n == 1 else FIG_Q2))
        parts.append('<div class="hint-card">%s</div>' % _h(CARD_HINT[n]))
        parts.append(_quad_html(QUAD[n]))

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div>由這一節開始不再標明用哪一張卡，要自己認出題型；'
                 '坐標圖也不再畫好，只給空白格，圖要自己畫上去。'
                 '兩張卡的關鍵詞只在下面重印一次。</div>')
    parts.append(_step_compact_html())
    parts.append('<div class="hint-card">%s</div>' % _h(STEP_WARN))
    for n in B_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div></div>' % (n, _h(STEMS[n])))
        parts.append('<div class="qfig">%s<div style="font-size:10.5pt">'
                     '（上面的空白格自己畫圖用；下面四格是草稿。）</div></div>' % FIG_BLANK)
        parts.append(_quad_html(QUAD[n]))

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>本節收起工具卡，也不給坐標格。第 5 題要自己畫草圖'
                 '（圓心、半徑、直線各標出來）再計算；第 6 題兩小題環環相扣，'
                 '(a) 算錯 (b) 一定跟着錯，所以 (a) 做完先用「兩斜率相乘 = −1」'
                 '檢查一次再往下。</div>')
    for n in C_ITEMS:
        lead = ("作答（先畫草圖 → 代入或算 d → 下判斷 → 求交點）：" if n == 5
                else "作答（(a) 求斜率 → 代點斜式 → 檢查；(b) 算 d 跟 r 比）：")
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
