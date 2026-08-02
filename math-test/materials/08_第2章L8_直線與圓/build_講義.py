# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L8 解析幾何（一）直線與圓 —— 課堂講義 build script
主設計 D5 圖文雙軌（左欄坐標圖／右欄同一步的代數，逐列橫向對齊）；
輔助 D2 手順卡（兩張：求直線方程／判斷直線與圓的位置關係）、
D9 草稿分區（範例C 示範四格草稿，練習A／B 的作答區就是四格）。
鷹架密度：抽離小班 (Tier 2)。
產出：講義_直線與圓_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
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
from coord_svg import coord_svg, hstack      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_直線與圓_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L8 解析幾何（一）直線與圓"
FOOT = "高三數學．" + UNIT

U = 20          # 坐標圖每格像素；三種範例共用同一個，圖與圖之間格子大小才一致
FIG_CM = 7.2    # D5 左欄圖寬（docx）


# ================================================================ 圖
# 範例A：A(−2,3)、B(4,−5)。三張圖對應三個基本量，格子大小相同、只加東西不換場景
# ——這是 D5「同一張圖逐步長出來」的做法，換場景學生就要重新定位。
# y 只留到 4：跨 11 格時三列圖共 21.3cm，NOTE_A 就差 0.2cm 擠不進同一頁
# （實測會落單成只有 120 字的一頁）。收成 10 格剛好放得下。
# 範例A 三張圖用 19 而非全域的 20：這一頁排完三列圖＋易錯點灰框後，最後一行
# 離頁尾只剩 5.7pt（QB-20 WARN）。每張矮 10px，三張就拉開 22pt。
A_RANGE = dict(xlo=-4, xhi=6, ylo=-6, yhi=4, unit=19)
PT_A = {"t": "point", "x": -2, "y": 3, "label": "A(−2, 3)", "lp": "nw"}
PT_B = {"t": "point", "x": 4, "y": -5, "label": "B(4, −5)", "lp": "se"}

FIG_A1 = coord_svg([
    PT_A,
    {"t": "seg", "x1": -2, "y1": 3, "x2": -2, "y2": 0, "dash": "4,3",
     "label": "3", "dx": -12, "dy": 0},
    {"t": "seg", "x1": -2, "y1": 3, "x2": 0, "y2": 3, "dash": "4,3",
     "label": "2", "dy": 15},   # 標下方：標上方會跟 y 軸刻度 3、4 混成一排
    {"t": "ra", "x": -2, "y": 0, "open": "ru"},
], **A_RANGE)

FIG_A2 = coord_svg([
    PT_A, PT_B,
    {"t": "seg", "x1": -2, "y1": 3, "x2": 4, "y2": -5, "sw": 2.0},
    {"t": "seg", "x1": -2, "y1": 3, "x2": 4, "y2": 3, "dash": "4,3",
     "label": "6", "dy": -9},
    {"t": "seg", "x1": 4, "y1": 3, "x2": 4, "y2": -5, "dash": "4,3",
     "label": "8", "dx": 14, "dy": 0},
    {"t": "ra", "x": 4, "y": 3, "open": "ld"},
    {"t": "note", "x": 0.45, "y": -1.5, "text": "10", "bold": True},
], **A_RANGE)

FIG_A3 = coord_svg([
    PT_A, PT_B,
    {"t": "seg", "x1": -2, "y1": 3, "x2": 4, "y2": -5, "sw": 2.0},
    {"t": "point", "x": 1, "y": -1, "label": "M(1, −1)", "lp": "se"},
    {"t": "note", "x": -1.7, "y": 0.6, "text": "5"},
    {"t": "note", "x": 3.2, "y": -3.4, "text": "5"},
], **A_RANGE)

# 範例B：L: 2x+3y−6=0
B_RANGE = dict(xlo=-3, xhi=6, ylo=-3, yhi=5, unit=U)
LINE_B = {"t": "line", "a": 2, "b": 3, "c": -6, "label": "2x+3y−6=0", "at": -1.5}

FIG_B1 = coord_svg([
    LINE_B,
    {"t": "point", "x": 0, "y": 2, "label": "(0, 2)", "lp": "nw"},
    {"t": "point", "x": 3, "y": 0, "label": "(3, 0)", "lp": "se"},
], **B_RANGE)

FIG_B2 = coord_svg([
    LINE_B,
    {"t": "point", "x": 0, "y": 2},
    {"t": "point", "x": 3, "y": 0},
    {"t": "seg", "x1": 0, "y1": 2, "x2": 3, "y2": 2, "dash": "4,3",
     "label": "右 3", "dy": -9},
    {"t": "seg", "x1": 3, "y1": 2, "x2": 3, "y2": 0, "dash": "4,3",
     "label": "下 2", "dx": 22, "dy": 0},
    {"t": "ra", "x": 3, "y": 2, "open": "ld"},
], **B_RANGE)

# 範例C(c)：Q(4,1) 且垂直於 L: 2x+3y−6=0 → 3x−2y−10=0
FIG_C = coord_svg([
    {"t": "line", "a": 2, "b": 3, "c": -6, "label": "L", "at": -1.5},
    {"t": "line", "a": 3, "b": -2, "c": -10, "label": "L′", "at": 5.4,
     "ldy": 4},
    {"t": "point", "x": 4, "y": 1, "label": "Q(4, 1)", "lp": "ne"},
    {"t": "ra", "x": 1.846, "y": 0.769, "open": "ru"},
], xlo=-2, xhi=7, ylo=-4, yhi=5, unit=U)

# 範例D：三個圓
FIG_D1 = coord_svg([
    {"t": "circle", "cx": 2, "cy": -1, "r": 3, "label": "C(2, −1)",
     "lx": 2, "ly": -1.35},
    {"t": "seg", "x1": 2, "y1": -1, "x2": 5, "y2": -1, "dash": "4,3",
     "label": "r = 3", "dy": -9},
], xlo=-3, xhi=7, ylo=-5, yhi=4, unit=U)

FIG_D2 = coord_svg([
    {"t": "circle", "cx": 1, "cy": 2, "r": 5, "label": "C(1, 2)",
     "lx": 1, "ly": 1.65},
    {"t": "point", "x": 4, "y": 6, "label": "P(4, 6)", "lp": "ne"},
    {"t": "seg", "x1": 1, "y1": 2, "x2": 4, "y2": 6, "dash": "4,3",
     "label": "r", "dx": -10, "dy": -4},
], xlo=-5, xhi=7, ylo=-4, yhi=8, unit=U)

FIG_D3 = coord_svg([
    {"t": "circle", "cx": 2, "cy": 1, "r": 2.828, "label": "C(2, 1)",
     "lx": 2, "ly": 0.65},
    {"t": "point", "x": 0, "y": 3, "label": "A(0, 3)", "lp": "nw"},
    {"t": "point", "x": 4, "y": -1, "label": "B(4, −1)", "lp": "se"},
    {"t": "seg", "x1": 0, "y1": 3, "x2": 4, "y2": -1, "sw": 2.0},
], xlo=-3, xhi=7, ylo=-3, yhi=5, unit=U)

# 範例E：圓 x²+y²=10 與三條直線
E_RANGE = dict(xlo=-5, xhi=7, ylo=-5, yhi=5, unit=U)
CIR_E = {"t": "circle", "cx": 0, "cy": 0, "r": 3.1623}

FIG_E1 = coord_svg([
    CIR_E,
    {"t": "line", "a": 1, "b": 1, "c": -4, "label": "L₁", "at": 4.6, "ldy": 15},
    {"t": "point", "x": 1, "y": 3, "label": "(1, 3)", "lp": "n"},
    {"t": "point", "x": 3, "y": 1, "label": "(3, 1)", "lp": "ne"},
], **E_RANGE)

FIG_E2 = coord_svg([
    CIR_E,
    {"t": "line", "a": 1, "b": 3, "c": -10, "label": "L₂", "at": -4.2, "ldy": -6},
    {"t": "point", "x": 1, "y": 3, "label": "(1, 3)", "lp": "ne"},
], **E_RANGE)

FIG_E3 = coord_svg([
    CIR_E,
    {"t": "line", "a": 1, "b": 1, "c": -6, "label": "L₃", "at": 5.6, "ldy": 15},
], **E_RANGE)

# 位置關係總覽（三合一）：圓 r=2 固定，只把水平線往上推，d 由小變大跨過 r
_OV = dict(xlo=-3, xhi=3, ylo=-3, yhi=4, unit=17, tick=2)


def _ov(k, extra=()):
    it = [{"t": "circle", "cx": 0, "cy": 0, "r": 2},
          {"t": "line", "a": 0, "b": 1, "c": -k},
          {"t": "seg", "x1": 0, "y1": 0, "x2": 0, "y2": k, "dash": "3,3",
           "label": "d", "dx": 9, "dy": 0}]
    return coord_svg(it + list(extra), raw=True, **_OV)


FIG_OV = hstack([
    _ov(1, [{"t": "point", "x": -1.732, "y": 1},
            {"t": "point", "x": 1.732, "y": 1}]),
    _ov(2, [{"t": "point", "x": 0, "y": 2}]),
    _ov(3),
], captions=("d ＜ r：相交（兩點）", "d ＝ r：相切（一點）", "d ＞ r：相離（無交點）"))


# 延伸段：兩圓的位置關係。範圍刻意避開 0（x、y 都由 1 起）——coord_svg 只在
# 範圍跨過 0 時才畫坐標軸，這樣就得到一組沒有軸的純圖形，不會讓學生以為
# 圓心一定要放在某個特定坐標。
def _two(c1, r1, c2, r2):
    return coord_svg([
        {"t": "circle", "cx": c1, "cy": 4, "r": r1},
        {"t": "circle", "cx": c2, "cy": 4, "r": r2},
        {"t": "seg", "x1": c1, "y1": 4, "x2": c2, "y2": 4, "dash": "3,3",
         "label": "d", "dy": -10},
    ], xlo=1, xhi=7, ylo=2, yhi=6, unit=20, grid=False, tick=0,
        axis_label=False, raw=True)


# 半徑 1.2／1.6 對 6 格寬——圓要夠大才看得出「碰到」與「沒碰到」的差別
# （unit=11、r=1 那一版圓只有 11px，三個小圈擠成一排看不出關係）。
FIG_TWO = hstack([_two(2.4, 1.2, 5.6, 1.6),      # d=3.2 > 1.2+1.6=2.8 外離
                  _two(2.6, 1.2, 5.4, 1.6),      # d=2.8 = 2.8 外切
                  _two(3.0, 1.6, 5.0, 1.6)],     # d=2.0，介於 0 與 3.2 之間 相交
                 captions=("外離", "外切", "相交"))

TWO_ROWS = [
    ("外離（分開，沒有交點）", "{d>r_1+r_2}"),
    ("外切（碰到一點，各在對方外面）", "{d=r_1+r_2}"),
    ("相交（兩個交點）", "{|r_1-r_2|<d<r_1+r_2}"),
    ("內切（碰到一點，一個在另一個裡面）", "{d=|r_1-r_2|}"),
    ("內含（一個完全在另一個裡面，沒有交點）", "{d<|r_1-r_2|}"),
]
TWO_INTRO = ("兩圓之間也有位置關係，判斷方法一樣是比距離——只是這次比"
             "「兩個圓心的距離 d」跟兩半徑的和 {r_1+r_2}、差 {|r_1-r_2|}。")
TWO_EX = ("例：兩圓半徑 1 cm 和 5 cm、圓心距 6 cm。{r_1+r_2=1+5=6} 剛好等於 d，"
          "所以兩圓外切。※ 這類題只考一步：把 d 跟 {r_1+r_2}、{|r_1-r_2|} 比一比。")


# ================================================================ 文字內容
INTRO = [
    "由這一課開始轉去解析幾何。它的本體只有一句話：把幾何圖形放進坐標系，"
    "圖上的每一件事都可以寫成一條算式；反過來，每一條算式也都畫得出來。"
    "所以本課的每一題都有兩條軌道——「圖上看到什麼」和「算式上寫什麼」，"
    "兩條要對得上。",
    "難點不在算術。斜率、距離、中點這些公式都不長，套進去就有答案；"
    "真正卡住的是「這一步在圖上是什麼意思」。"
    "最典型的是點到 x 軸的距離：明明題目給了兩個坐標，要用哪一個？"
    "背口訣會忘，但只要在圖上把那條垂線畫出來，一次就看得懂——它量的是上下高度，"
    "所以用 y。",
    "因此本課的主工具是圖文雙軌：每個範例都用一張表，左欄是坐標圖、右欄是同一步的算式，"
    "左右同一列對齊。看的時候左右一起看，不要只看右邊抄算式。",
    "另外配兩張手順卡（求直線方程、判斷直線與圓的位置關係），"
    "因為這兩種題都是「先認出題目給了什麼，再選公式」的多步驟程序；"
    "以及一張四格草稿分區——解析幾何的失分很多不是不會，"
    "是坐標抄錯、正負號在草稿裡跟丟了。四格把「抄已知／求斜率／代公式／檢查」分開放，"
    "各歸各位就不容易亂。",
]

# ---------------------------------------------------------------- D2 兩張手順卡
CARD1 = dict(
    title="手順卡一・求直線方程",
    trigger="題目說「求過某點的直線方程」「求某直線的方程」。",
    steps=[
        ("先認出題目給了什麼：①一點＋斜率　②兩點　③一點＋另一條直線（平行或垂直）。",
         "三種給法只差在「斜率怎樣拿到手」，後面完全一樣。先分類，不要見到數字就代。"),
        ("把斜率 m 弄到手：②用 {m=frac(y_2-y_1,x_2-x_1)}；"
         "③平行則同斜率，垂直則 {m'=frac(-1,m)}（兩斜率相乘 = −1）。",
         "垂直不是把斜率變號就算，是取「負倒數」：{m=-frac(2,3)} 的垂直斜率是 "
         "{frac(3,2)}，不是 {frac(2,3)}。"),
        ("代點斜式 {y-y_1=m(x-x_1)}，再整理成一般式 {ax+by+c=0}。",
         "代進去的 {x_1}、{y_1} 是那個點的坐標，負坐標記得連負號一起代："
         "點 {(-2,3)} 代出來是 {y-3=m(x+2)}。"),
        ("把原來那個點代回答案檢查，等式應該成立。",
         "這一步 10 秒，能抓出九成的抄錯。兩點式的題目兩個點都代一次。"),
    ],
    fading="完整四步卡 → 只留三種給法的分類與「先求 m」→ 只留一句"
           "「點斜式 {y-y_1=m(x-x_1)}」→ 完全移除。",
)
CARD2 = dict(
    title="手順卡二・判斷直線與圓的位置關係",
    trigger="題目問「交點個數」「是否相交／相切／相離」，或要你求直線與圓的交點。",
    steps=[
        ("由圓方程抄出圓心 {(h,k)} 與半徑 {r}（標準式 {(x-h)^2+(y-k)^2=r^2} 直接讀）。",
         "括號內是減號，所以 {(x+2)^2} 的圓心坐標是 {-2} 不是 {2}；"
         "等號右邊是 {r^2}，{r} 要開方（右邊是 9，{r=3} 不是 9）。"),
        ("路線一（要求交點就走這條）：由直線方程解出一個變數代入圓方程，"
         "化成一個一元二次方程，算 {Δ=b^2-4ac}。",
         "代入後一定要整理成「一邊為 0」才數 {a}、{b}、{c}；"
         "常見錯是把 {2x^2+2x-4=0} 沒約簡就硬算，數字大容易錯（可先兩邊除以 2）。"),
        ("路線二（只問位置關係就走這條，較快）：算圓心到直線的距離 "
         "{d=frac(|ax_0+by_0+c|,sqrt(a^2+b^2))}，再跟 {r} 比。",
         "分子有絕對值，算出負數要取正；分母是 {sqrt(a^2+b^2)}，"
         "{a}、{b} 是直線方程的係數，不是點的坐標。"),
        ("下判斷：{Δ>0} 或 {d<r} → 相交（兩個交點）；{Δ=0} 或 {d=r} → 相切（一個）；"
         "{Δ<0} 或 {d>r} → 相離（沒有交點）。",
         "兩條路線的結論一定相同。有時間就兩條都走一次互相檢核——這是本課最可靠的自我檢查。"),
    ],
    fading="完整四步卡 → 只留「代入求 Δ／算 d 比 r」兩條路線名稱 → "
           "只留一句「先找圓心與半徑」→ 完全移除。",
)
CARDS_D2 = [CARD1, CARD2]

# ---------------------------------------------------------------- 範例
D5_H = ("圖形上看到什麼", "算式上怎樣寫")

EX_A = ("【範例A・點的基本量】已知 {A(-2,3)}、{B(4,-5)}。"
        "（a）A 到 x 軸、y 軸的距離各是多少？（b）求 {|AB|}。（c）求 AB 的中點 M。")
A_PAIRS_TXT = [
    "（a）由 A 向 x 軸畫一條垂線，量的是「上下高度」，所以取 y 的絕對值："
    "到 x 軸的距離 {=|3|=3}。同理向 y 軸畫垂線量的是「左右寬度」，取 x："
    "到 y 軸的距離 {=|-2|=2}。",
    "（b）把 A、B 補成一個直角三角形：水平邊 {=4-(-2)=6}，垂直邊 {=3-(-5)=8}。"
    "斜邊就是 AB，用畢氏定理："
    "{|AB|=sqrt(6^2+8^2)=sqrt(36+64)=sqrt(100)=10}。",
    "（c）中點在 AB 的正中間，左右各走一半、上下各走一半，"
    "所以兩個坐標各自取平均：{M=(frac(-2+4,2),frac(3+(-5),2))=(1,-1)}。"
    "檢核：{|AM|=sqrt(3^2+4^2)=5}，{|MB|=sqrt(3^2+4^2)=5}，兩段相等。",
]
# 壓成兩行：三行時這一頁的最後一行離頁尾只剩 5.7pt（QB-20 WARN）。
NOTE_A = ("※ 全課最高頻的錯就在 (a)：到 x 軸的距離用 y、到 y 軸用 x，很多人對調。"
          "記法不是背，是看圖——量高度當然看 y。距離一定是正數，{|-2|=2}。")

EX_B = "【範例B・斜率與截距】已知直線 {L: 2x+3y-6=0}。求 L 的斜率與 y 截距。"
B_PAIRS_TXT = [
    "先找兩個好畫的點：令 {x=0} 得 {3y=6}，{y=2} → 交 y 軸於 {(0,2)}，"
    "所以 y 截距是 2；令 {y=0} 得 {2x=6}，{x=3} → 交 x 軸於 {(3,0)}。"
    "兩點一連，整條線就畫出來了。",
    "斜率 = 「向右走多少、向上走多少」。由 {(0,2)} 走到 {(3,0)}："
    "向右 3、向下 2，所以 {m=frac(-2,3)=-frac(2,3)}（向下就是負）。"
    "用公式檢核：{m=-frac(a,b)=-frac(2,3)}，或化成斜截式 {y=-frac(2,3)x+2} 直接讀。",
]
NOTE_B = ("※ 斜截式 {y=mx+k} 的 {k} 就是 y 截距——這也是「y 截距」要令 {x=0} 的原因"
          "（線與 y 軸相交的地方，x 一定是 0）。"
          "另外 {m=-frac(a,b)} 這條公式的負號常被漏：{4x-2y+6=0} 的斜率是 "
          "{-frac(4,-2)=2}，兩個負號相消變正，不是 {-2}。")

EX_C = ("【範例C・求直線方程】（a）過 {P(-2,3)} 且斜率為 2；"
        "（b）過 {A(1,3)} 與 {B(5,1)}；"
        "（c）過 {Q(4,1)} 且垂直於範例B 的 {L: 2x+3y-6=0}。"
        "（答案都寫成一般式 {ax+by+c=0}）")
SOL_C = [
    "（a）給法①：一點＋斜率，斜率已經有了，直接代點斜式。"
    "{y-3=2(x-(-2))=2(x+2)} → {y-3=2x+4} → {y=2x+7} → {2x-y+7=0}。"
    "檢查：代 {(-2,3)}：{2(-2)-3+7=-4-3+7=0} ✔",
    "（b）給法②：兩點，先算斜率 {m=frac(1-3,5-1)=frac(-2,4)=-frac(1,2)}。"
    "再代點斜式（用 A）：{y-3=-frac(1,2)(x-1)} → {2y-6=-(x-1)} → {x+2y-7=0}。"
    "檢查：代 {A(1,3)}：{1+6-7=0} ✔；代 {B(5,1)}：{5+2-7=0} ✔（兩點都要代）",
    "（c）給法③：一點＋垂直的直線。L 的斜率 {=-frac(2,3)}，"
    "垂直的斜率是它的負倒數 {frac(3,2)}。下面用四格草稿把這一題走一次。",
]
NOTE_C = ("※ (c) 的垂直斜率是「負倒數」：把 {-frac(2,3)} 上下倒轉再變號，得 {frac(3,2)}。"
          "檢查方法是相乘看是不是 {-1}：{(-frac(2,3))*frac(3,2)=-1} ✔。"
          "只把負號拿掉（變 {frac(2,3)}）或只倒轉不變號，都是錯的。")

# D9 草稿分區示範（範例C(c)）——格名放表頭，內容放格內，兩者同一個表，
# 分頁時 hdr 會重印，不會出現「格名留在上一頁」。
QUAD_C = [
    ("① 抄下已知（連正負號一起抄）",
     "點 {Q(4,1)}；已知直線 {L: 2x+3y-6=0}；關係：垂直。",
     "② 先把斜率弄到手",
     "L 的斜率 {m=-frac(a,b)=-frac(2,3)}；"
     "垂直 → {m'=frac(-1,m)=frac(3,2)}。"),
    ("③ 代點斜式，整理成一般式",
     "{y-1=frac(3,2)(x-4)} → 兩邊乘 2：{2y-2=3(x-4)=3x-12} → {3x-2y-10=0}。",
     "④ 代回檢查",
     "代 {Q(4,1)}：{3(4)-2(1)-10=12-2-10=0} ✔；"
     "兩斜率相乘 {(-frac(2,3))*frac(3,2)=-1} ✔ 確為垂直。"),
]

EX_D = ("【範例D・圓方程】求下列圓的方程（寫成標準式 {(x-h)^2+(y-k)^2=r^2}）："
        "（a）圓心 {C(2,-1)}、半徑 3；（b）圓心 {C(1,2)} 且圓過 {P(4,6)}；"
        "（c）以 {A(0,3)}、{B(4,-1)} 為直徑的兩端。")
D_PAIRS_TXT = [
    "（a）圓心與半徑都直接給了，代進標準式就完。"
    "{h=2}、{k=-1}、{r=3} → {(x-2)^2+(y-(-1))^2=3^2}，即 {(x-2)^2+(y+1)^2=9}。"
    "圓心的負坐標代進括號會變加號（{y-(-1)=y+1}）。",
    "（b）圓心有了、半徑沒有。圖上 P 在圓上，所以 {r} 就是圓心到 P 的距離："
    "{r=|CP|=sqrt((4-1)^2+(6-2)^2)=sqrt(9+16)=5}。"
    "→ {(x-1)^2+(y-2)^2=25}。（先用兩點距離求 r，再代標準式，兩步。）",
    "（c）AB 是直徑，所以圓心＝AB 的中點 {C=(frac(0+4,2),frac(3-1,2))=(2,1)}，"
    "半徑＝直徑的一半。{|AB|=sqrt(4^2+(-4)^2)=sqrt(32)=4sqrt(2)}，"
    "{r=2sqrt(2)}，{r^2=8} → {(x-2)^2+(y-1)^2=8}。",
]
NOTE_D = ("※ 標準式右邊要的是 {r^2}，不是 {r}。(c) 的 {r=2sqrt(2)} 看起來很醜，"
          "但 {r^2=8} 很乾淨——遇到開不盡的根號，不必把 {r} 寫出來，"
          "直接用 {r^2=(frac(|AB|,2))^2} 算就好。"
          "另外圓心的坐標代進括號要變號，{C(2,-1)} 寫成 {(x-2)^2+(y+1)^2}。")

EX_E = ("【範例E・直線與圓】已知圓 {C: x^2+y^2=10}（圓心 {O(0,0)}，{r=sqrt(10)}）。"
        "判斷下列各直線與 C 的位置關係，有交點的求出交點："
        "（a）{L_1: x+y-4=0}　（b）{L_2: x+3y-10=0}　（c）{L_3: x+y-6=0}。")
E_PAIRS_TXT = [
    "（a）圖上直線穿過圓，切出兩個交點。"
    "代入法：{y=4-x} 代進 {x^2+y^2=10} → {x^2+(4-x)^2=10} → {2x^2-8x+6=0} → "
    "{x^2-4x+3=0}。{Δ=(-4)^2-4(1)(3)=16-12=4>0} → 兩個交點。"
    "{(x-1)(x-3)=0} → {x=1} 或 {x=3} → 交點 {(1,3)}、{(3,1)}。"
    "距離法檢核：{d=frac(4,sqrt(2))=2sqrt(2)≈2.83<sqrt(10)≈3.16} ✔",
    "（b）圖上直線碰到圓邊就走，只碰一點。"
    "代入法：{x=10-3y} 代進去 → {(10-3y)^2+y^2=10} → {10y^2-60y+90=0} → "
    "{y^2-6y+9=0}。{Δ=36-36=0} → 相切，只有一個交點。"
    "{(y-3)^2=0} → {y=3}，{x=1} → 切點 {(1,3)}。"
    "距離法檢核：{d=frac(10,sqrt(10))=sqrt(10)=r} ✔ 剛好等於半徑。",
    "（c）圖上直線整條在圓外面，碰都碰不到。"
    "代入法：{y=6-x} 代進去 → {x^2+(6-x)^2=10} → {2x^2-12x+26=0} → "
    "{x^2-6x+13=0}。{Δ=36-52=-16<0} → 沒有實數解，即沒有交點（相離）。"
    "距離法檢核：{d=frac(6,sqrt(2))=3sqrt(2)≈4.24>sqrt(10)≈3.16} ✔",
]
NOTE_E = ("※ 比較 (a) 與 (c)：{L_1} 和 {L_3} 是平行的（都是 {x+y=k}），"
          "只有常數項由 4 變成 6。圖上看就是同一條線往右上平移，"
          "圓心到它的距離由 2.83 增到 4.24，一跨過 {r≈3.16}，關係就由相交變相離。"
          "這就是「代數上只改一個數字，幾何上整條線在移動」——"
          "解析幾何要練的正是這種左右對照的眼力。")


# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D5 圖文雙軌對照——範例A（點的基本量）、範例B（斜率與截距）、"
                "範例D（圓方程三種給法）、範例E（直線與圓的位置關係）"
                "四個範例全部用左欄坐標圖／右欄同一步代數的雙欄表，逐列橫向對齊；"
                "左欄的圖是「同一個場景逐步長出來」（範例A 三張圖格子大小相同、"
                "只是逐次補上垂線、直角三角形、中點），不換場景，"
                "學生不必每一列重新定位",
    aux_designs=("D2 手順卡——兩張：《求直線方程》（認出三種給法／先把斜率弄到手／"
                 "代點斜式整理成一般式／代回檢查）、《判斷直線與圓的位置關係》"
                 "（抄圓心半徑／代入求 Δ 或算 d 比 r／下判斷），"
                 "每步下方附該步最易出錯的關鍵點（※ 前綴），另出工具卡讓學生放桌面",
                 "D9 草稿分區——範例C(c) 示範四格草稿（① 抄下已知 ② 先把斜率弄到手 "
                 "③ 代點斜式整理 ④ 代回檢查），練習A、B 的作答區直接就是這四格；"
                 "解析幾何的失分很大一部分不是不會做，是坐標抄錯、負號在草稿裡跟丟，"
                 "四格把三種認知活動在版面上物理分離"),
    reason=(
        "本課取自題庫 A6 解析幾何的直線與圓組（點到坐標軸距離、兩點距離、中點、斜率、"
        "y 截距、點斜式／兩點式／垂直求直線方程、圓標準式、直線與圓的交點個數，"
        "對照 MATH-045／046／047／048／056／058／064／065、MATH-015／016、"
        "MOCK2-101／103／135／136／172／173、MOCK2-013／030／091 等題）。"
        "依 teaching-designs.md §1，解析幾何屬 S6 結構，核心瓶頸是"
        "「代數與幾何雙軌並行超出工作記憶容量」，建議主設計即 D5 圖文雙軌、"
        "建議輔助即 D2 手順卡與 D9 草稿分區——本份完全照該行取用，未自創組合。"
        "與 L5～L7 的差別在主設計換了：那三課同屬 S2 多步驟程序運算，主設計是 D2 手順卡；"
        "本課的程序其實比二次方程還短（代公式而已），失分不在步驟長度，"
        "而在「這一步在圖上是什麼意思」——例如點到 x 軸的距離要用 y、"
        "直線與圓的 Δ 對應交點個數。所以 D2 由主設計降為輔助（只管兩種真正多步的題型），"
        "由 D5 接手當主設計。三種設計＝主 D5 ＋ 輔 D2、D9，未超過「主1＋輔2」上限。"),
    density="抽離小班（Tier 2）",
    fading=(
        "圖文雙軌（D5）：講義範例左圖右式全給、逐列對齊 → 練習A 題目旁附已畫好的坐標圖"
        "（只要學生把點標上去）→ 練習B 只給空白坐標格（圖自己畫）→ "
        "練習C 連格都不給，要自己畫草圖（第 5 題明寫「請先畫草圖」）→ "
        "之後改成口頭講出「這條線跟圓大概什麼關係」→ 移除。｜"
        "手順卡（D2）：講義印兩張完整卡（每步附易錯點），另出工具卡放桌面 → "
        "練習A 每題旁重印該題用得著的那一張的關鍵詞 → 練習B 只在區塊開頭印一次 → "
        "練習C 不印 → 之後只留「先認出題目給了什麼」一句 → 完全移除。｜"
        "草稿分區（D9）：講義範例C(c) 示範填好的四格 → 練習A、B 的作答區是印好格名的空四格 → "
        "練習C 回到一般作答行（但仍建議學生自己在旁邊分四塊）→ 移除。"),
    flows=("F5 課前流程預告（今天五件事：兩張手順卡 → 範例A、B 認識坐標平面上的量 → "
           "範例C 求直線方程＋四格草稿 → 範例D 圓方程 → 範例E 直線與圓 → 練習A／B／C）",
           "F2 番茄鐘分段（「點與直線」（範例A～C）、「圓」（範例D、E）兩塊各自是一段，"
           "做完一塊對照核對清單再進入下一塊）",
           "F4 過程導向回饋與分步計分（求直線方程把「認出給法」「求對斜率」「代點斜式」"
           "「整理成一般式」分四步各給分；直線與圓把「抄對圓心半徑」「代入化簡」"
           "「算對 Δ」「下對判斷」分開給分——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（兩張手順卡即為此項，若獲准帶入測考需寫入 IEP 第 9 點）",
               "a5 放大字體",
               "a6 增加行距／放大作答欄（四格草稿分區即為此項的具體做法）",
               "a7 調整計分標準（認出給法／求斜率／代公式／檢查分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L5～L7 的銜接",
            "前三課（指數對數、根式分式、二次方程與不等式）都是 S2 多步驟程序運算，"
            "主設計是 D2 手順卡。本課換成 D5 圖文雙軌，是因為數學結構換了（S6 解析幾何），"
            "不是因為前一套失效。D2 仍以輔助身分留在課上（兩張卡），"
            "學生熟悉的「一步一步、每步附易錯點」節奏不變，"
            "只是主戲改為「左右對照」。範例E 的 Δ 判斷直接沿用 L7 的判別式，"
            "可以在課上明說：同一個 Δ，在 L7 是判根的個數，在這裡是判交點的個數，"
            "其實是同一件事——交點就是方程的實根。"),
           ("為何兩張卡而不是一張",
            "本課只有兩種題型真正需要多步程序：求直線方程、判斷直線與圓的位置關係。"
            "其餘（到軸距離、兩點距離、中點、斜率、截距）都是一步代公式，"
            "不該做成卡片——teaching-designs.md 對 D2 的規範是「每張卡只呈現一個核心動作」，"
            "把五條公式塞成一張卡就變成公式表，回到研究裡那種沒人用的牆上海報。"
            "那五條公式改放工具卡的速查卡（D7 形態），與手順卡分開。"),
           ("題量與範圍說明",
            "本課練習共 6 題（練習A／B／C 各 2 題），合共 11 個小問，"
            "涵蓋到坐標軸距離、兩點距離、中點、斜率、y 截距、點斜式、兩點式、"
            "垂直求直線方程、圓標準式（圓心半徑／直徑兩端）、直線與圓的位置關係與交點。"
            "題庫 A6 的圓錐曲線部分（橢圓半長軸、準線、雙曲線焦半徑與漸近線、"
            "離心率判別曲線、拋物線草圖，約 30 題）不在本課，留給 L9。"
            "兩圓的位置關係（MOCK1-031）題庫只有 1 題，做成第八節的延伸段"
            "（一張三圖對照＋一張條件表＋一個例題），只作認識、不出練習題——"
            "它的判斷方式跟直線與圓同源（都是比距離），"
            "放在範例E 之後學生一看就懂，另開一課並不划算。"),
           ("配套文件",
            "《第2章 L8 解析幾何（一）直線與圓　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L8 解析幾何（一）直線與圓　工具卡》"
            "（兩張手順卡 ＋ 坐標平面速查卡 ＋ 圓與距離速查卡，學生剪下護貝放桌面）。")),
)


# ================================================================ docx
def build_docx_file():
    figdir = os.path.join(HERE, "_figtmp")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    def img(svg, name, cm=FIG_CM):
        png = os.path.join(figdir, name + ".png")
        ds.svg_to_png(svg, png, scale=3)
        return image_para(png, width_cm=cm)

    a_pairs = list(zip([img(FIG_A1, "a1"), img(FIG_A2, "a2"), img(FIG_A3, "a3")],
                       A_PAIRS_TXT))
    b_pairs = list(zip([img(FIG_B1, "b1"), img(FIG_B2, "b2")], B_PAIRS_TXT))
    d_pairs = list(zip([img(FIG_D1, "d1"), img(FIG_D2, "d2"), img(FIG_D3, "d3")],
                       D_PAIRS_TXT))
    e_pairs = list(zip([img(FIG_E1, "e1"), img(FIG_E2, "e2"), img(FIG_E3, "e3")],
                       E_PAIRS_TXT))
    fig_c = img(FIG_C, "c1", cm=6.4)
    fig_ov = img(FIG_OV, "ov", cm=15.5)

    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、兩張手順卡", page_break_before=True))
    P.append(para("本課只有兩種題型真正要走多步程序，就是下面兩張卡。"
                  "其餘的量（到坐標軸的距離、兩點距離、中點、斜率、截距）"
                  "都是一步代公式，公式放在工具卡的速查卡上，不做成手順卡。"))
    for c in CARDS_D2:
        P.append(step_card(c["title"], c["steps"],
                           trigger=c["trigger"], fading=c["fading"]))
        P.append(blank())

    P.append(heading("三、範例A・點的基本量（到軸距離、兩點距離、中點）",
                     page_break_before=True))
    P.append(problem_box([para(EX_A)]))
    P.append(para("左邊是圖、右邊是同一步的算式，一列一列橫著看。"))
    P.append(dual_track_table(a_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_A))

    P.append(heading("四、範例B・直線的斜率與 y 截距", page_break_before=True))
    P.append(problem_box([para(EX_B)]))
    P.append(dual_track_table(b_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_B))

    P.append(heading("五、範例C・求直線方程的三種給法", page_break_before=True))
    P.append(problem_box([para(EX_C)]))
    for t in SOL_C:
        P.append(para(t))
    P.append(expand_image(fig_c, MEDIA))
    P.append(para("（圖：L 與所求的 L′ 在交點處成直角；Q 在 L′ 上。）", sz=21))
    P.append(para("四格草稿分區（把「抄已知／求斜率／代公式／檢查」分開放，"
                  "各歸各位就不容易亂）：", bold=True))
    for h1, c1, h2, c2 in QUAD_C:
        P.append(dual_track_table([(c1, c2)], headers=(h1, h2)))
    P.append(shaded_box(NOTE_C))

    P.append(heading("六、範例D・圓方程的三種給法", page_break_before=True))
    P.append(problem_box([para(EX_D)]))
    P.append(dual_track_table(d_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_D))

    P.append(heading("七、範例E・直線與圓：Δ 與位置關係", page_break_before=True))
    P.append(para("先看三種位置關係的全貌：圓不動，把直線一步一步往外推，"
                  "圓心到直線的距離 d 越來越大，一跨過半徑 r，關係就換一種。"))
    P.append(expand_image(fig_ov, MEDIA))
    P.append(blank())
    P.append(problem_box([para(EX_E)]))
    P.append(dual_track_table(e_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_E))

    P.append(heading("八、延伸：兩圓的位置關係（只作認識，本課不出題）"))
    P.append(para(TWO_INTRO))
    P.append(expand_image(img(FIG_TWO, "two", cm=12.5), MEDIA))
    P.append(dual_track_table(TWO_ROWS,
                              headers=("兩圓的位置", "圓心距 d 與兩個半徑的關係")))
    P.append(shaded_box(TWO_EX))

    P.append(heading("九、接下來"))
    # 這一段刻意壓到兩行：三行時最後一行會被 fixed 頁尾的白底蓋住（QB-20 實測）。
    P.append(para("請拿出《第2章 L8 解析幾何（一）直線與圓　課堂練習》，"
                  "並把《工具卡》剪下放桌面。練習A 標明用哪張卡、附已畫好的坐標圖；"
                  "練習B 只重印卡的關鍵詞；練習C 不印卡也不給格。先畫圖再算。"))

    P += teacher_notes(**TN)
    out = build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=MEDIA)
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
    """frac/sqrt/absv 的引數可能含括號，一律用平衡括號遞迴切（抄 L6 _conv）。"""
    out, i = [], 0
    while i < len(s):
        if s.startswith("frac(", i):
            args, end = _split_args(s, i + 4)
            if args and len(args) == 2:
                out.append("\\frac{%s}{%s}" % (_conv(args[0]), _conv(args[1])))
                i = end
                continue
        # 絕對值不用轉：omml_core 與 TeX 都直接寫 |…|（omml_core 沒有 absv() 語法，
        # 見 _parse_atom 的 '|' 分支），所以 {|AB|} 兩邊都原樣通過。
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
    # 嚴格不等號：轉成 \lt \gt，令 HTML 原始碼不留裸 < >（避免被當標籤，QB-14）
    body = body.replace("<", r" \lt ").replace(">", r" \gt ")
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


def _step_card_html(c):
    rows = "".join('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                   % (i, _h(a), _h(p)) for i, (a, p) in enumerate(c["steps"], 1))
    # trigger／fading 都用 _h（不是 _esc）：本課兩張卡的褪除句都含 {} 數學式，
    # 用 _esc 會把大括號原樣印出來（docx 版的 step_card 走 para() 會 parse，兩版才一致）。
    return ('<table class="d-tbl step-card"><tr><th colspan="2">%s</th></tr>'
            '<tr><td colspan="2">什麼時候用：%s</td></tr>%s'
            '<tr><td colspan="2">（教師）褪除：%s</td></tr></table>'
            % (_esc(c["title"]), _h(c["trigger"]), rows, _h(c["fading"])))


def _dual_html(pairs, headers):
    def side(x):
        return x if x.lstrip().startswith("<svg") else _h(x)
    head = ("<thead><tr><th>%s</th><th>%s</th></tr></thead>"
            % (_h(headers[0]), _h(headers[1])))
    body = "".join("<tr><td>%s</td><td>%s</td></tr>" % (side(l), side(r))
                   for l, r in pairs)
    return '<table class="d-tbl dual-track">%s<tbody>%s</tbody></table>' % (head, body)


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  /* 範本的 .d-tbl 是整張 break-inside:avoid，對本課的三列坐標圖表就變成
     「放不進剩餘空間 → 整張推到下一頁」，前面留半頁空白（實測 p4／p8）。
     雙軌表放寬為可跨頁，但每一列仍不可切開（左圖右式一定要留在同一列），
     表頭包 <thead> 讓 Chrome 跨頁時自動重印——等同 docx 的 hdr。 */
  .d-tbl.dual-track { break-inside: auto; page-break-inside: auto; }
  .d-tbl.dual-track tr { break-inside: avoid; page-break-inside: avoid; }
  .dual-track td:first-child { text-align: center; }
  .dual-track svg { max-width: 100%; height: auto; }
  .ovfig { text-align: center; margin: 8px 0; }
  .ovfig svg { max-width: 100%; height: auto; }
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

    parts.append('<div class="section-h page-break">二、兩張手順卡</div>')
    parts.append('<div>本課只有兩種題型真正要走多步程序，就是下面兩張卡。'
                 '其餘的量（到坐標軸的距離、兩點距離、中點、斜率、截距）'
                 '都是一步代公式，公式放在工具卡的速查卡上，不做成手順卡。</div>')
    parts += [_step_card_html(c) for c in CARDS_D2]

    parts.append('<div class="section-h page-break">'
                 '三、範例A・點的基本量（到軸距離、兩點距離、中點）</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_A))
    parts.append('<div>左邊是圖、右邊是同一步的算式，一列一列橫著看。</div>')
    parts.append(_dual_html(list(zip([FIG_A1, FIG_A2, FIG_A3], A_PAIRS_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_A))

    parts.append('<div class="section-h page-break">四、範例B・直線的斜率與 y 截距</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_B))
    parts.append(_dual_html(list(zip([FIG_B1, FIG_B2], B_PAIRS_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_B))

    parts.append('<div class="section-h page-break">五、範例C・求直線方程的三種給法</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_C))
    parts += ["<div>%s</div>" % _h(t) for t in SOL_C]
    parts.append('<div class="ovfig">%s<div style="font-size:10.5pt">'
                 '（圖：L 與所求的 L′ 在交點處成直角；Q 在 L′ 上。）</div></div>' % FIG_C)
    parts.append('<div style="font-weight:700;margin-top:8px">四格草稿分區'
                 '（把「抄已知／求斜率／代公式／檢查」分開放，各歸各位就不容易亂）：</div>')
    for h1, c1, h2, c2 in QUAD_C:
        parts.append(_dual_html([(c1, c2)], (h1, h2)))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_C))

    parts.append('<div class="section-h page-break">六、範例D・圓方程的三種給法</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_D))
    parts.append(_dual_html(list(zip([FIG_D1, FIG_D2, FIG_D3], D_PAIRS_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_D))

    parts.append('<div class="section-h page-break">'
                 '七、範例E・直線與圓：Δ 與位置關係</div>')
    parts.append('<div>先看三種位置關係的全貌：圓不動，把直線一步一步往外推，'
                 '圓心到直線的距離 d 越來越大，一跨過半徑 r，關係就換一種。</div>')
    parts.append('<div class="ovfig">%s</div>' % FIG_OV)
    parts.append('<div class="problem">%s</div>' % _h(EX_E))
    parts.append(_dual_html(list(zip([FIG_E1, FIG_E2, FIG_E3], E_PAIRS_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_E))

    parts.append('<div class="section-h">'
                 '八、延伸：兩圓的位置關係（只作認識，本課不出題）</div>')
    parts.append('<div>%s</div>' % _h(TWO_INTRO))
    parts.append('<div class="ovfig">%s</div>' % FIG_TWO)
    parts.append(_dual_html(TWO_ROWS, ("兩圓的位置", "圓心距 d 與兩個半徑的關係")))
    parts.append('<div class="hint-card">%s</div>' % _h(TWO_EX))

    parts.append('<div class="section-h">九、接下來</div>')
    parts.append('<div>請拿出《第2章 L8 解析幾何（一）直線與圓　課堂練習》，'
                 '並把《工具卡》剪下放桌面。練習A 標明用哪張卡、附已畫好的坐標圖；'
                 '練習B 只重印卡的關鍵詞；練習C 不印卡也不給格。先畫圖再算。</div>')

    parts.append('<div class="footer">' + _esc(FOOT) + '</div>')

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join("<tr><td>%s</td><td>%s</td></tr>" % (_esc(k), _h(v)) for k, v in tn_rows)
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
