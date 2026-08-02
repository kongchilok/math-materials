# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L9 解析幾何（二）圓錐曲線 —— 課堂講義 build script
主設計 D7 提示卡（三張：橢圓／雙曲線／拋物線，每張＝觸發語＋示意圖＋文字敘述＋代數符號）；
輔助 D5 圖文雙軌（四個範例都左圖右式逐列對齊）、
D2 手順卡（兩張：橢圓四個量的求法／共同漸近線求雙曲線，分別排在用得着的範例前面）。
鷹架密度：抽離小班 (Tier 2)。
產出：講義_圓錐曲線_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
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
BASE = "講義_圓錐曲線_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L9 解析幾何（二）圓錐曲線"
FOOT = "高三數學．" + UNIT

U = 14          # 坐標圖每格像素（18 太大：四列雙軌表就撐爆一頁，實測講義變 14 頁）
FIG_CM = 6.0    # D5 左欄圖寬（docx）
D5_H = ("圖形上看到什麼", "算式上怎樣寫")

# ================================================================ 圖
# ---- D7 三張提示卡的示意圖（卡片窄，用小 unit）
CARD_R = dict(xlo=-6, xhi=6, ylo=-4, yhi=4, unit=11, tick=2)

FIG_CARD_E = coord_svg([
    {"t": "ellipse", "a": 5, "b": 3, "center": False},
    {"t": "point", "x": 4, "y": 0, "label": "F₂", "lp": "n"},
    {"t": "point", "x": -4, "y": 0, "label": "F₁", "lp": "n"},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 5, "y2": 0, "sw": 2.6,
     "label": "a", "dy": -11},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 0, "y2": 3, "sw": 2.6,
     "label": "b", "dx": 13, "dy": 0},
], **CARD_R)

FIG_CARD_H = coord_svg([
    {"t": "hyper", "a": 4, "b": 3, "orient": "h", "asym": True, "center": False},
    {"t": "point", "x": 5, "y": 0, "label": "F₂", "lp": "n"},
    {"t": "point", "x": -5, "y": 0, "label": "F₁", "lp": "n"},
    {"t": "note", "x": 5.6, "y": 3.4, "text": "漸近線", "size": 12},
], **CARD_R)

FIG_CARD_P = hstack([
    coord_svg([{"t": "parab", "k": 0.3, "dir": "up"}], raw=True,
              xlo=-4, xhi=4, ylo=-2, yhi=5, unit=10, tick=2),
    coord_svg([{"t": "parab", "k": 0.3, "dir": "right"}], raw=True,
              xlo=-2, xhi=5, ylo=-4, yhi=4, unit=10, tick=2),
], captions=("x 二次 → 上下", "y 二次 → 左右"), cap_size=12)

# ---- 範例A：三種曲線並排（認形狀）
A_R = dict(xlo=-6, xhi=6, ylo=-5, yhi=5, unit=12)
FIG_A1 = coord_svg([{"t": "ellipse", "a": 5, "b": 3, "center": False}], **A_R)
FIG_A2 = coord_svg([{"t": "hyper", "a": 4, "b": 3, "asym": True, "center": False}], **A_R)
FIG_A3 = coord_svg([{"t": "parab", "k": 0.5, "vx": 1, "vy": -1, "dir": "up"}], **A_R)
FIG_A4 = coord_svg([{"t": "circle", "cx": 0, "cy": 0, "r": 4}], **A_R)

# ---- 範例B：同樣的數值、只調轉分母
B_R = dict(xlo=-6, xhi=6, ylo=-6, yhi=6, unit=12, tick=2)
FIG_B1 = coord_svg([
    {"t": "ellipse", "a": 5, "b": 3, "center": False},
    {"t": "point", "x": 4, "y": 0},
    {"t": "point", "x": -4, "y": 0},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 5, "y2": 0, "sw": 2.4,
     "label": "a = 5", "dy": -11},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 0, "y2": 3, "sw": 2.4,
     "label": "b = 3", "dx": -30, "dy": 0},   # −20 時右半會壓到 y 軸刻度 2
], **B_R)
FIG_B2 = coord_svg([
    {"t": "ellipse", "a": 3, "b": 5, "center": False},
    {"t": "point", "x": 0, "y": 4},
    {"t": "point", "x": 0, "y": -4},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 0, "y2": 5, "sw": 2.4,
     "label": "a = 5", "dx": 20, "dy": 0},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 3, "y2": 0, "sw": 2.4,
     "label": "b = 3", "dy": -11},
], **B_R)

# ---- 範例C：雙曲線
C_R = dict(xlo=-8, xhi=8, ylo=-5, yhi=5, unit=13, tick=2)
FIG_C1 = coord_svg([
    {"t": "hyper", "a": 4, "b": 3, "asym": True, "center": False},
    {"t": "point", "x": 5, "y": 0, "label": "(5, 0)", "lp": "n"},
    {"t": "point", "x": -5, "y": 0, "label": "(−5, 0)", "lp": "n"},
    {"t": "seg", "x1": 0, "y1": 0, "x2": 4, "y2": 0, "sw": 2.4,
     "label": "a = 4", "dy": -11},
], **C_R)
FIG_C2 = coord_svg([
    {"t": "hyper", "a": 4, "b": 3, "asym": True, "center": False},
    {"t": "point", "x": 5, "y": 0}, {"t": "point", "x": -5, "y": 0},
    {"t": "point", "x": 5.66, "y": 3.18, "label": "P", "lp": "ne"},
    {"t": "seg", "x1": 5, "y1": 0, "x2": 5.66, "y2": 3.18, "dash": "4,3",
     "label": "d₁", "dx": 14, "dy": 4},
    {"t": "seg", "x1": -5, "y1": 0, "x2": 5.66, "y2": 3.18, "dash": "4,3",
     "label": "d₂", "dy": -10},
], **C_R)

# ---- 範例D：拋物線三種
D_R = dict(xlo=-6, xhi=6, ylo=-6, yhi=6, unit=U, tick=2)
FIG_D1 = coord_svg([
    {"t": "parab", "k": 1, "vy": -4, "dir": "up"},
    {"t": "point", "x": 0, "y": -4, "label": "(0, −4)", "lp": "se"},
], **D_R)
FIG_D2 = coord_svg([
    {"t": "parab", "k": 0.125, "dir": "down"},
    {"t": "point", "x": 0, "y": 0, "label": "(0, 0)", "lp": "ne"},
], **D_R)
FIG_D3 = coord_svg([
    {"t": "parab", "k": 0.25, "dir": "right"},
    {"t": "point", "x": 0, "y": 0, "label": "(0, 0)", "lp": "nw"},
], **D_R)

# ---- 範例E：兩條同漸近線的雙曲線疊在一起
FIG_E = coord_svg([
    {"t": "hyper", "a": 4, "b": 3, "asym": True, "center": False},
    {"t": "hyper", "a": 8, "b": 6, "asym": False, "center": False},
    {"t": "point", "x": 11.3, "y": 6, "label": "P", "lp": "nw"},
    {"t": "note", "x": -6, "y": 5, "text": "兩條共用同一對漸近線", "size": 12},
], xlo=-13, xhi=13, ylo=-8, yhi=8, unit=8, tick=4)

# ================================================================ 文字內容
INTRO = [
    "上一課把直線與圓放進坐標系；這一課換三位新成員：橢圓、雙曲線、拋物線。"
    "它們合稱圓錐曲線（用一個平面去切圓錐，切法不同就得到不同的曲線）。"
    "課程要求的不深：認得出是哪一種、由標準式讀出幾個量、畫得出草圖。",
    "難的地方不是算，是「記混」。三種曲線的標準式長得很像，"
    "但橢圓是相加、雙曲線是相減；更要命的是 a、b、c 的關係剛好相反——"
    "橢圓 {c^2=a^2-b^2}，雙曲線 {c^2=a^2+b^2}。"
    "每年都有人把兩條式對調，之後每一步都跟着錯。",
    "所以本課的主工具是三張提示卡：一張管一種曲線，"
    "每張都寫明「什麼時候翻我」，並且把文字敘述、示意圖、代數符號三樣並排。"
    "卡片另外印成工具卡，做題時放在桌面，用手指指住正在用的那一張。",
    "配合的是圖文雙軌：每個範例左邊是圖、右邊是同一步的算式。"
    "圓錐曲線的量（a、b、c、離心率、漸近線）在圖上都看得見長度或位置，"
    "看得見就不必死背——這是本課最重要的學習策略。",
]

# ---------------------------------------------------------------- D7 三張提示卡
CARD_E = dict(
    title="提示卡一・橢圓",
    trigger="方程是「兩項相加 ＝ 1」，或題目給的離心率在 0 與 1 之間。",
    statement="圖上任何一點到兩個焦點的距離之和是固定的，等於 {2a}。"
              "a² 是兩個分母中「較大」那一個，長軸跟着大分母那個變數走"
              "（大分母在 x 下面 → 長軸沿 x 軸）。"
              "c 由 a、b 相減求出，焦點永遠落在長軸上。",
    formula="{frac(x^2,a^2)+frac(y^2,b^2)=1}（{a>b}）　"
            "{c^2=a^2-b^2}　{e=frac(c,a)}（{0<e<1}）　兩準線距離 {=frac(2a^2,c)}",
)
CARD_H = dict(
    title="提示卡二・雙曲線",
    trigger="方程是「兩項相減 ＝ 1」，或離心率大於 1，或題目提到「漸近線」。",
    statement="圖上任何一點到兩個焦點的距離之差的絕對值是固定的，等於 {2a}。"
              "a² 是「減號前面」那一項的分母——不看大小，只看位置"
              "（減號前面是 x → 橫向、開口左右；是 y → 縱向、開口上下）。"
              "c 由 a、b 相加求出，所以 c 一定比 a 大。",
    formula="{frac(x^2,a^2)-frac(y^2,b^2)=1}　{c^2=a^2+b^2}　"
            "{e=frac(c,a)}（{e>1}）　漸近線 {y=+-frac(b,a)x}",
)
CARD_P = dict(
    title="提示卡三・拋物線",
    trigger="式子裡只有一個變數是二次（另一個是一次），或離心率剛好等於 1。",
    statement="兩步判斷完：①哪個變數是二次——x 二次就上下開口、y 二次就左右開口；"
              "②係數的正負——正的朝正方向（上／右）、負的朝負方向（下／左）。"
              "拋物線沒有 a、b、c，也沒有漸近線，只有開口方向與頂點。",
    formula="{y=ax^2+k}（上下開口，頂點 {(0,k)}）　"
            "{x=ay^2}（左右開口，頂點在原點）",
)
CARDS_D7 = [CARD_E, CARD_H, CARD_P]

# ---------------------------------------------------------------- D2 兩張手順卡
STEP_B = dict(
    title="手順卡一・由橢圓方程求 a、b、c、e 與準線",
    trigger="題目給一條橢圓方程，問半長軸、焦點、離心率或準線距離。",
    steps=[
        ("先化成標準式：等號右邊要是 1（例如 {25x^2+9y^2=225} 兩邊除以 225，"
         "得 {frac(x^2,9)+frac(y^2,25)=1}）。",
         "是整條式子除以 225，不是把係數搬去分母。除完之後兩個分母都要是正數。"),
        ("比較兩個分母：「大」的那個是 {a^2}，小的是 {b^2}；"
         "長軸沿着大分母那個變數的軸。",
         "先寫低方向再算：{frac(x^2,9)+frac(y^2,25)=1} 的大分母在 y 下面 → "
         "長軸沿 y 軸、{a=5}。a、b 一對調，後面全錯。"),
        ("算 {c=sqrt(a^2-b^2)}（橢圓是「減」），焦點在長軸上、距中心 c。",
         "唔好寫成 {a^2+b^2}——嗰條係雙曲線。算完可以檢查 {c<a} 係咪成立。"),
        ("要離心率就 {e=frac(c,a)}；要準線距離就 {frac(2a^2,c)}。",
         "橢圓的 e 一定喺 0 同 1 之間，算出 {e>1} 即係前面錯咗。"),
    ],
    fading="完整四步卡 → 只留「化標準式 → 大分母是 a² → c 相減 → e=c/a」→ "
           "只留一句「a 跟着大分母走」→ 完全移除。",
)
STEP_E = dict(
    title="手順卡二・求「有共同漸近線」的雙曲線方程",
    trigger="題目說「與某雙曲線有共同漸近線」，並給一個點要你求新的雙曲線方程。",
    steps=[
        ("把原方程等號右邊的 1 換成 k，寫成 {frac(x^2,A)-frac(y^2,B)=k}。",
         "只改右邊，左邊兩個分母原封不動——正因為左邊不變，漸近線才會相同。"),
        ("把題目給的點代進去，算出 k。",
         "代入時記得先把根號平方掉：{(8sqrt(2))^2=64*2=128}，唔係 {8*2}。"),
        ("把整條式除以 k，化回右邊是 1 的標準式。",
         "k 是負數時，每一項都要變號，結果會變成 {frac(y^2,B')-frac(x^2,A')=1}"
         "——雙曲線由橫向轉成縱向，但漸近線不變。"),
        ("檢查兩件事：點代得返落去、新舊漸近線相同。",
         "漸近線用 {frac(b,a)} 比一比就得；兩者唔同即係中間除錯。"),
    ],
    fading="完整四步卡 → 只留「右邊換 k → 代點求 k → 除以 k」→ "
           "只留一句「同漸近線＝左邊不變、右邊換數」→ 完全移除。",
)

# ---------------------------------------------------------------- 範例
EX_A = ("【範例A・認出是哪一種曲線】判斷下列各方程（或條件）代表哪一種曲線："
        "（a）{frac(x^2,25)+frac(y^2,9)=1}　（b）{frac(x^2,16)-frac(y^2,9)=1}　"
        "（c）{y=2x^2-4x+1}　（d）{x^2+y^2=16}　（e）某曲線的離心率 {e=0.6}。")
A_TXT = [
    "（a）兩項相「加」等於 1，兩個分母都是正數 → 橢圓。"
    "分母 25 > 9、大的在 x 下面，所以長軸沿 x 軸，{a=5}、{b=3}。",
    "（b）兩項相「減」等於 1 → 雙曲線。減號前面是 x 那一項，"
    "所以是橫向的（開口向左右），{a^2=16} → {a=4}。圖上兩條虛線是漸近線。",
    "（c）x 是二次、y 是一次 → 拋物線。{x^2} 的係數 2 是正的 → 開口向上。"
    "（配方得 {y=2(x-1)^2-1}，頂點 {(1,-1)}。）",
    "（d）{x^2} 與 {y^2} 的係數相同 → 圓，半徑 4。"
    "也可以看成 {frac(x^2,16)+frac(y^2,16)=1}，即 {a=b} 的橢圓（此時 {c=0}、{e=0}）。",
]
NOTE_A = ("※ 離心率各佔一段、中間沒有重疊：{0<e<1} 橢圓、{e=1} 拋物線、{e>1} 雙曲線，"
          "所以 (e) 不必畫圖也判斷得出。另外 (d) 提醒：見到「相加 = 1」不要立刻寫橢圓，"
          "先看兩個分母是不是相同。")

EX_B = ("【範例B・橢圓的四個量】求下列橢圓的 a、b、長軸方向、c、離心率與兩準線間的距離："
        "（1）{frac(x^2,25)+frac(y^2,9)=1}　（2）{frac(x^2,9)+frac(y^2,25)=1}。"
        "（兩題的分母只是調轉，比較一下差在哪裡。）")
B_TXT = [
    "（1）大分母 25 在 x 下面 → 長軸沿 「x 軸」（圖上橫向較長）。"
    "{a^2=25} → {a=5}；{b^2=9} → {b=3}。"
    "{c^2=a^2-b^2=25-9=16} → {c=4}，焦點 {(+-4,0)} 在長軸上。"
    "{e=frac(c,a)=frac(4,5)=0.8}；兩準線距離 {=frac(2a^2,c)=frac(50,4)=12.5}。",
    "（2）大分母 25 這次在 y 下面 → 長軸沿 「y 軸」（圖上直向較長）。"
    "四個數值完全一樣：{a=5}、{b=3}、{c=4}、{e=0.8}、準線距離 12.5，"
    "只有方向不同——焦點變成 {(0,+-4)}，準線變成兩條水平線。"
    "※ 所以：分母的數值決定 a、b、c、e 是多少，分母的位置決定長軸朝哪個方向。"
    "只記住「a 是第一個分母」的人，這一題會寫 {a=3}，"
    "然後 {c^2=9-25} 開不出方根才發現不對。口訣是「a 跟着大分母走」。",
]
EX_C = ("【範例C・雙曲線】已知 {frac(x^2,16)-frac(y^2,9)=1}。"
        "（a）求 a、b、c 與離心率。（b）求漸近線方程。"
        "（c）若 P 在雙曲線上、到一個焦點的距離是 3，求 P 到另一個焦點的距離。")
C_TXT = [
    "（a）減號前面是 x → 橫向雙曲線，{a^2=16} → {a=4}；{b^2=9} → {b=3}。"
    "{c^2=a^2+b^2=16+9=25} → {c=5}（「相加」，跟橢圓相反），焦點 {(+-5,0)}。"
    "{e=frac(5,4)=1.25>1} ✔ 確實是雙曲線。"
    "（b）漸近線 {y=+-frac(b,a)x=+-frac(3,4)x}，就是圖上那兩條虛線。",
    "（c）用定義：圖上 P 到兩個焦點的距離 {d_1}、{d_2} 滿足 {|d_1-d_2|=2a=8}。"
    "已知 {d_1=3} → {d_2=3+8=11}，或 {d_2=3-8=-5}（距離不能是負數，捨去）。"
    "所以 {d_2=11}。"
    "合理性檢查：焦點到最近那個頂點的距離 {=c-a=5-4=1}，"
    "曲線上任何一點到焦點至少 1，題目給的 3 合理。",
]
NOTE_C = ("※ 全課最容易對調的一條：橢圓 {c^2=a^2-b^2}（相減，所以 {c<a}）、"
          "雙曲線 {c^2=a^2+b^2}（相加，所以 {c>a}）。"
          "記法：橢圓是封閉的、焦點在裡面所以 c 較小；雙曲線是張開的、焦點在外面所以 c 較大。"
          "檢查方法：算完看 e——橢圓的 e 一定小於 1，雙曲線的 e 一定大於 1。")

EX_D = ("【範例D・拋物線草圖】畫出下列拋物線的草圖，指出開口方向與頂點："
        "（a）{y=x^2-4}　（b）{x^2+8y=0}　（c）{y^2=4x}。")
D_TXT = [
    "（a）x 是二次 → 上下開口；{x^2} 係數 1 > 0 → 「開口向上」；頂點 {(0,-4)}。"
    "檢核：令 {y=0} 得 {x^2=4}，{x=+-2}，圖上與 x 軸交於 {(+-2,0)} ✔",
    "（b）先整理：{x^2+8y=0} → {y=-frac(x^2,8)}。x 是二次 → 上下開口；"
    "係數 {-frac(1,8)<0} → 「開口向下」；頂點 {(0,0)}。"
    "檢核：取 {x=4} 得 {y=-2}，圖上 {(4,-2)} 在曲線上 ✔",
    "（c）這次是 「y」 二次 → 左右開口；係數 4 > 0 → 「開口向右」；頂點 {(0,0)}。"
    "檢核：取 {y=2} 得 {x=1}；取 {y=4} 得 {x=4}，兩點都在曲線上 ✔",
]
NOTE_D = ("※ 拋物線只要問兩句就答得出：哪個變數是二次？係數是正還是負？"
          "x 二次 → 上下（正上負下）；y 二次 → 左右（正右負左）。"
          "(b) 這種要先移項整理成「{y=} 」或「{x=} 」的形式才看得清楚係數的正負，"
          "不要看着 {x^2+8y=0} 就說係數是正的。")

EX_E = ("【範例E・共同漸近線】求經過點 {P(8sqrt(2),6)}、"
        "且與 {frac(x^2,16)-frac(y^2,9)=1} 有共同漸近線的雙曲線方程。")
SOL_E = [
    "第 1 步：把右邊的 1 換成 k，寫出同漸近線族 {frac(x^2,16)-frac(y^2,9)=k}"
    "（左邊兩個分母不動，所以這一族每一條的漸近線都是 {y=+-frac(3,4)x}）。"
    "第 2 步：代入 {P(8sqrt(2),6)}："
    "{frac((8sqrt(2))^2,16)-frac(6^2,9)=frac(128,16)-frac(36,9)=8-4=4}，得 {k=4}。"
    "（{(8sqrt(2))^2=64*2=128}，根號要先平方掉。）",
    "第 3 步：把 {frac(x^2,16)-frac(y^2,9)=4} 兩邊除以 4，化回標準式 "
    "{frac(x^2,64)-frac(y^2,36)=1}。"
    "第 4 步（檢查）：① 代 P：{frac(128,64)-frac(36,36)=2-1=1} ✔ "
    "② 新曲線 {a=8}、{b=6}，漸近線 {y=+-frac(6,8)x=+-frac(3,4)x}，與原曲線相同 ✔",
]
NOTE_E = ("※ k 若算出是負數（練習第 6 題就是），除以 k 時每一項都要變號，"
          "結果會由 {frac(x^2,A)-frac(y^2,B)=1} 變成 {frac(y^2,B)-frac(x^2,A)=1}"
          "——兩項換邊、分母不動，即雙曲線由橫向轉成縱向，但漸近線一動不動。")

# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D7 提示卡——三張（橢圓／雙曲線／拋物線），每張照 teaching-designs.md "
                "對 D7 的規範做足三件套：文字敘述＋示意圖＋代數符號並列，"
                "並且each張都寫明觸發語「什麼時候翻我」（相加=1／相減=1／只有一個變數是二次；"
                "或由離心率 0<e<1／e>1／e=1 判斷）。三張卡另外印成工具卡讓學生放桌面",
    aux_designs=("D5 圖文雙軌——範例A（四種曲線的形狀）、範例B（同樣數值只調轉分母的兩個橢圓）、"
                 "範例C（雙曲線的 a、c 與焦半徑）、範例D（拋物線三種開口）"
                 "全部用左坐標圖／右同一步代數的雙欄表逐列橫向對齊；"
                 "a、b、c 在圖上都是看得見的線段長度，看得見就不必死背",
                 "D2 手順卡——兩張，分別排在用得着的範例前面而不是集中在開頭："
                 "《由橢圓方程求 a、b、c、e 與準線》放範例B 前、"
                 "《求有共同漸近線的雙曲線方程》放範例E 前，每步下方附該步最易出錯的關鍵點"),
    reason=(
        "本課接住 L8，做完 A6 解析幾何剩下的圓錐曲線組（由方程或離心率判別曲線種類、"
        "橢圓半長軸與準線、雙曲線焦半徑與漸近線、拋物線草圖、共同漸近線求雙曲線方程，"
        "對照 MATH-008／009／010／011／020／027／028／029／042／049／062／063、"
        "MOCK2-019／024／025／044／045／053／080／083／086／104／133／134 等題）。"
        "數學結構仍是 teaching-designs.md 的 S6 解析幾何，但「主設計沒有沿用 S6 預設的 D5、"
        "改用 D7 提示卡」，理由是本課的瓶頸位置跟 L8 不同："
        "L8 只有直線與圓兩種對象、記憶負荷小，卡在「這一步在圖上是什麼意思」（D5 對症）；"
        "本課一次來三種曲線，每種各有標準式、a／b／c 關係、離心率範圍、漸近線，"
        "學生第一關就卡在「認不出這是哪一種、記不起這一種用哪條式」"
        "——這是記憶檢索在限時下失敗，正是 §1 S5 列的瓶頸與 D7 的問題陳述。"
        "研究並且明確指出支援要「個人化、桌面化」（牆上公式海報使用率極低），"
        "所以三張卡一定要出成工具卡。D5 降為輔助但份量仍重（四個範例都用），"
        "因為圓錐曲線的每一個量在圖上都對應得到具體線段。"
        "三種設計＝主 D7 ＋ 輔 D5、D2，未超過「主1＋輔2」上限。"),
    density="抽離小班（Tier 2）",
    fading=(
        "提示卡（D7）：講義印三張完整卡（觸發語＋圖＋敘述＋符號），另出工具卡放桌面 → "
        "練習A 每題旁標明該翻哪一張 → 練習B 只在區塊開頭列三個觸發語（相加／相減／一個二次）→ "
        "練習C 完全不提示 → 之後只留一句「先認出是哪一種」→ 完全移除。｜"
        "圖文雙軌（D5）：講義範例左圖右式全給 → 練習A 附已畫好的曲線圖（只要讀出 a、b）→ "
        "練習B 不給圖但保留「先在草稿畫個大概」的指示 → 練習C 第 5 題要求自己畫草圖 → 移除。｜"
        "手順卡（D2）：講義給完整四步（附易錯點）→ 練習B 只在區塊開頭印關鍵詞 → "
        "練習C 不印 → 移除。"),
    flows=("F5 課前流程預告（今天五件事：三張提示卡 → 範例A 認曲線 → 範例B、C 橢圓與雙曲線的量 → "
           "範例D 拋物線草圖 → 範例E 共同漸近線 → 練習A／B／C）",
           "F2 番茄鐘分段（「認曲線」（範例A）、「橢圓與雙曲線」（範例B、C）、"
           "「拋物線與漸近線」（範例D、E）三塊各自是一段）",
           "F4 過程導向回饋與分步計分（橢圓題把「化標準式」「判長軸方向」「算對 c」"
           "「求 e 或準線」分四步各給分；共同漸近線題把「寫出 k 族」「代點求 k」"
           "「除以 k 化標準式」「檢查漸近線」分開給分——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（三張提示卡與兩張手順卡即為此項；"
               "圓錐曲線公式多，若獲准帶入測考，建議把三張提示卡寫進 IEP 第 9 點）",
               "a5 放大字體",
               "a6 增加行距／放大作答欄",
               "a7 調整計分標準（化標準式／判方向／算 c／求 e 分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L8 的銜接",
            "L8 與本課同屬 A6 解析幾何，合起來把該 subtype 的 65 題做完。"
            "L8 的 D5 圖文雙軌在本課降為輔助但仍是四個範例的骨架，"
            "學生熟悉的「左圖右式、一列一列橫着看」節奏不變；"
            "新增的是 D7 桌面卡。可以在課上明說：L8 判斷直線與圓的位置關係靠「比距離」，"
            "本課判斷是哪一種曲線靠「看相加還是相減」，"
            "兩者都是先分類、再套對應的那一條公式。"),
           ("為何三張卡而不是一張總表",
            "teaching-designs.md 對 D7 的規範是「一張只做一個概念」，"
            "研究並指出做成公式總表就會回到「視覺搜尋負荷太高、沒人用」的狀態。"
            "所以橢圓、雙曲線、拋物線各一張，各自有獨立的觸發語；"
            "三者的橫向比較放在講義正文與練習的核對，不做成第四張卡。"),
           ("刻意避開的內容",
            "①雙曲線的準線：題庫只考橢圓準線（MATH-027、MOCK2-024／086），"
            "雙曲線準線不出現，故本課只教橢圓準線，卡二不列準線公式。"
            "②準線距離刻意選除得盡的數（本課 2a²/c = 12.5）；"
            "題庫 MOCK2-086 那種答案是 7√2 的，計算負荷蓋過概念，"
            "留給程度較好的學生或課後延伸。"
            "③圓錐曲線的統一定義（焦點—準線距離比）不教，只用離心率的數值範圍判別。"),
           ("題量說明",
            "本課練習共 6 題（練習A／B／C 各 2 題），合共 13 個小問，"
            "涵蓋由方程與由離心率認曲線、橢圓 a／b／c／e、橢圓化標準式與準線距離、"
            "雙曲線 a／b／c／漸近線／焦半徑、拋物線三種開口（含 y 二次那種）、"
            "以及 k 為負數的共同漸近線題。"),
           ("配套文件",
            "《第2章 L9 解析幾何（二）圓錐曲線　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L9 解析幾何（二）圓錐曲線　工具卡》"
            "（三張圓錐曲線提示卡 ＋ 一張認曲線速查卡，學生剪下護貝放桌面）。")),
)


# 三種曲線的橫向比較（本課總結；三張提示卡各管一種，這張管「它們差在哪」）
CMP_HEAD = ("橢圓", "雙曲線", "拋物線")
CMP_ROWS = [
    ("{frac(x^2,a^2)+frac(y^2,b^2)=1}（相加）",
     "{frac(x^2,a^2)-frac(y^2,b^2)=1}（相減）",
     "{y=ax^2+k} 或 {x=ay^2}（一個變數二次）"),
    ("a² ＝ 較大的分母；長軸跟着大分母走",
     "a² ＝ 減號前面那一項的分母（不看大小）",
     "沒有 a、b、c，只有開口方向與頂點"),
    ("{c^2=a^2-b^2}（相減，所以 {c<a}）",
     "{c^2=a^2+b^2}（相加，所以 {c>a}）", "—"),
    ("{0<e<1}", "{e>1}", "{e=1}"),
    ("沒有漸近線；兩準線距離 {frac(2a^2,c)}",
     "漸近線 {y=+-frac(b,a)x}", "沒有漸近線"),
    ("到兩焦點的距離之「和」 ＝ {2a}",
     "到兩焦點的距離之差的絕對值 ＝ {2a}", "—"),
]


# ================================================================ docx
def build_docx_file():
    figdir = os.path.join(HERE, "_figtmp")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    def img(svg, name, cm=FIG_CM):
        png = os.path.join(figdir, name + ".png")
        ds.svg_to_png(svg, png, scale=3)
        return image_para(png, width_cm=cm)

    card_figs = [img(FIG_CARD_E, "ce", 5.4), img(FIG_CARD_H, "ch", 5.4),
                 img(FIG_CARD_P, "cp", 6.8)]
    a_pairs = list(zip([img(FIG_A1, "a1"), img(FIG_A2, "a2"), img(FIG_A3, "a3"),
                        img(FIG_A4, "a4")], A_TXT))
    b_pairs = list(zip([img(FIG_B1, "b1"), img(FIG_B2, "b2")], B_TXT))
    c_pairs = list(zip([img(FIG_C1, "c1"), img(FIG_C2, "c2")], C_TXT))
    d_pairs = list(zip([img(FIG_D1, "d1"), img(FIG_D2, "d2"), img(FIG_D3, "d3")],
                       D_TXT))
    fig_e = img(FIG_E, "e1", 10.0)

    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、三張圓錐曲線提示卡", page_break_before=True))
    P.append(para("一張卡管一種曲線，最上面都寫了「什麼時候翻我」。"
                  "三張卡另外印成工具卡，剪下放桌面。"))
    for c, f in zip(CARDS_D7, card_figs):
        P.append(reference_card(c["title"], c["trigger"], c["statement"],
                                formula=c["formula"], figure=f, media=MEDIA))
        P.append(blank())

    P.append(heading("三、範例A・認出是哪一種曲線", page_break_before=True))
    P.append(problem_box([para(EX_A)]))
    P.append(para("左邊是圖、右邊是判斷的理由，一列一列橫着看。"))
    P.append(dual_track_table(a_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_A))

    P.append(heading("四、範例B・橢圓：a 跟着大分母走", page_break_before=True))
    P.append(step_card(STEP_B["title"], STEP_B["steps"],
                       trigger=STEP_B["trigger"], fading=STEP_B["fading"]))
    P.append(blank())
    P.append(problem_box([para(EX_B)]))
    # 這一題的易錯點寫在第二列右欄末尾，不另開灰框——獨立灰框會被擠成單獨一頁
    P.append(dual_track_table(b_pairs, media=MEDIA, headers=D5_H))

    P.append(heading("五、範例C・雙曲線：c 是相加，還有漸近線", page_break_before=True))
    P.append(problem_box([para(EX_C)]))
    P.append(dual_track_table(c_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_C))

    P.append(heading("六、範例D・拋物線：先看哪個變數是二次", page_break_before=True))
    P.append(problem_box([para(EX_D)]))
    P.append(dual_track_table(d_pairs, media=MEDIA, headers=D5_H))
    P.append(shaded_box(NOTE_D))

    P.append(heading("七、範例E・共同漸近線求雙曲線方程", page_break_before=True))
    P.append(step_card(STEP_E["title"], STEP_E["steps"],
                       trigger=STEP_E["trigger"], fading=STEP_E["fading"]))
    P.append(blank())
    P.append(problem_box([para(EX_E)]))
    for t in SOL_E:
        P.append(para(t))
    P.append(expand_image(fig_e, MEDIA))
    P.append(para("（圖：原曲線與答案兩條雙曲線疊在一起，共用同一對漸近線；"
                  "P 在外面那一條上。）", sz=21))
    P.append(shaded_box(NOTE_E))

    P.append(heading("八、三種曲線橫向比較（做題前先掃一眼）"))
    P.append(para("三張提示卡各管一種曲線，這張表管「它們差在哪」。"
                  "最容易記混的是第三列（c 是相減還是相加）——"
                  "算完之後用第四列的離心率檢查一次：橢圓的 e 一定小於 1、"
                  "雙曲線的 e 一定大於 1，對不上就是前面用錯式。"))
    P.append(three_column_table(CMP_ROWS, headers=CMP_HEAD, row_h=700))

    P.append(heading("九、接下來"))
    P.append(para("請拿出《第2章 L9 圓錐曲線　課堂練習》，並把《工具卡》剪下放桌面。"
                  "練習A 標明該翻哪一張卡、附已畫好的圖；練習B 只列三個觸發語；"
                  "練習C 不再提示。動筆前永遠先認出這是哪一種曲線。"))

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


def _refcard_html(c, svg):
    return ('<div class="ref-card"><div style="font-weight:700;font-size:13pt">%s</div>'
            '<div style="font-size:11pt">什麼時候翻我：%s</div>'
            '<div class="cardfig%s">%s</div><div>%s</div><div>%s</div></div>'
            % (_esc(c["title"]), _h(c["trigger"]),
               " wide" if c is CARD_P else "", svg,
               _h(c["statement"]), _h(c["formula"])))


def _step_card_html(c):
    rows = "".join('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                   % (i, _h(a), _h(p)) for i, (a, p) in enumerate(c["steps"], 1))
    # trigger／fading 都用 _h：本課兩張卡的褪除句與觸發語都含 {} 數學式
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
  /* 範本的 .d-tbl 整張 break-inside:avoid，三列以上的坐標圖表會整張推去下一頁、
     前面留半頁白（L8 實測）。雙軌表放寬為可跨頁、每列不可切開，
     表頭包 <thead> 讓 Chrome 跨頁時自動重印。 */
  .d-tbl.dual-track { break-inside: auto; page-break-inside: auto; }
  .d-tbl.dual-track tr { break-inside: avoid; page-break-inside: avoid; }
  .dual-track td:first-child { text-align: center; }
  .dual-track svg, .cardfig svg, .ovfig svg { max-width: 100%; height: auto; }
  .cardfig, .ovfig { text-align: center; margin: 6px 0; }
  .cardfig svg { max-width: 5.4cm; }
  .cardfig.wide svg { max-width: 6.8cm; }
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

    parts.append('<div class="section-h page-break">二、三張圓錐曲線提示卡</div>')
    parts.append('<div>一張卡管一種曲線，最上面都寫了「什麼時候翻我」。'
                 '三張卡另外印成工具卡，剪下放桌面。</div>')
    for c, f in zip(CARDS_D7, [FIG_CARD_E, FIG_CARD_H, FIG_CARD_P]):
        parts.append(_refcard_html(c, f))

    parts.append('<div class="section-h page-break">三、範例A・認出是哪一種曲線</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_A))
    parts.append('<div>左邊是圖、右邊是判斷的理由，一列一列橫着看。</div>')
    parts.append(_dual_html(list(zip([FIG_A1, FIG_A2, FIG_A3, FIG_A4], A_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_A))

    parts.append('<div class="section-h page-break">四、範例B・橢圓：a 跟着大分母走</div>')
    parts.append(_step_card_html(STEP_B))
    parts.append('<div class="problem">%s</div>' % _h(EX_B))
    parts.append(_dual_html(list(zip([FIG_B1, FIG_B2], B_TXT)), D5_H))

    parts.append('<div class="section-h page-break">'
                 '五、範例C・雙曲線：c 是相加，還有漸近線</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_C))
    parts.append(_dual_html(list(zip([FIG_C1, FIG_C2], C_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_C))

    parts.append('<div class="section-h page-break">'
                 '六、範例D・拋物線：先看哪個變數是二次</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_D))
    parts.append(_dual_html(list(zip([FIG_D1, FIG_D2, FIG_D3], D_TXT)), D5_H))
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_D))

    parts.append('<div class="section-h page-break">七、範例E・共同漸近線求雙曲線方程</div>')
    parts.append(_step_card_html(STEP_E))
    parts.append('<div class="problem">%s</div>' % _h(EX_E))
    parts += ["<div>%s</div>" % _h(t) for t in SOL_E]
    parts.append('<div class="ovfig">%s<div style="font-size:10.5pt">'
                 '（圖：原曲線與答案兩條雙曲線疊在一起，共用同一對漸近線；'
                 'P 在外面那一條上。）</div></div>' % FIG_E)
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_E))

    parts.append('<div class="section-h">八、三種曲線橫向比較（做題前先掃一眼）</div>')
    parts.append('<div>三張提示卡各管一種曲線，這張表管「它們差在哪」。'
                 '最容易記混的是第三列（c 是相減還是相加）——'
                 '算完之後用第四列的離心率檢查一次：橢圓的 e 一定小於 1、'
                 '雙曲線的 e 一定大於 1，對不上就是前面用錯式。</div>')
    parts.append('<table class="d-tbl three-col"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
                 % ("".join("<th>%s</th>" % _esc(h) for h in CMP_HEAD),
                    "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _h(c) for c in r)
                            for r in CMP_ROWS)))

    parts.append('<div class="section-h">九、接下來</div>')
    parts.append('<div>請拿出《第2章 L9 圓錐曲線　課堂練習》，並把《工具卡》剪下放桌面。'
                 '練習A 標明該翻哪一張卡、附已畫好的圖；練習B 只列三個觸發語；'
                 '練習C 不再提示。動筆前永遠先認出這是哪一種曲線。</div>')

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
