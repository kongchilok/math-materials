# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L12 三角函數 —— 課堂講義 build script

主設計 D7 提示卡（五張：六個三角比／象限符號盤／和角差角＋特殊角值表／
二倍角／三角方程通解。每張卡都有「什麼時候翻我」的觸發條件——
teaching-designs.md 明示：只有公式沒有觸發條件的卡片，學生不知道何時該用）；
輔助 D5 圖文雙軌（只用在真正有圖可對照的兩處：三角比的「對邊／鄰邊」隨角變，
以及四個象限的 x、y 正負；左右逐列橫向對齊）、
D2 手順卡（一張：求非特殊角三角值的四步，管和角差角那一段的程序）。
鷹架密度：抽離小班 (Tier 2)。

產出：講義_三角函數_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）

注意（前幾課踩過的坑，改本檔時照跟）：
1. 三角函數名一律用 `{fn(sin)}` 這種正體寫法，不要直接打 sin——
   直接打會變成 s×i×n 三個斜體變數。已實測 `{fn(sin)α fn(cos)β}` 兩版都正確。
2. 平方寫 `{fn(sin)^2 α}`（次方掛在函數名上），不要寫 `{(fn(sin)α)^2}`。
3. 負分數寫 `-frac(24,25)`，不要寫 `frac(-24,25)`（後者把負號塞進分子，
   印出來像「−24 分之 25」的排版事故）。
4. 不要用 `**markdown 粗體**`，docx 端會原樣印出星號。強調用「」或 ※。
5. 標記字元只用實測清單：①②③④／ⓐⓑⓒⓓ／☐／★☆／※／⚠／▍／→。
6. 圖一律由 figs.py 產，docx 與 HTML 共用同一個函式，確保兩版外觀一致。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omml_docx import *                      # noqa: E402,F403
# 特殊角值表是 4 欄，three_column_table 只吃 3 欄，所以直接用底層 _tbl 自組
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH, GREY_FILL   # noqa: E402
import design_svg as ds                      # noqa: E402
import figs                                  # noqa: E402


def grid_table(rows, headers, h=460):
    """任意欄數的置中小表（本課用於特殊角值表）。"""
    n = len(headers)
    w = _PAGE_CONTENT_WIDTH // n
    widths = [w] * (n - 1) + [_PAGE_CONTENT_WIDTH - w * (n - 1)]
    out = [{"hdr": True,
            "cells": [{"p": [para(x, bold=True, sz=22, jc="center")],
                       "shd": GREY_FILL} for x in headers]}]
    for r in rows:
        out.append({"cells": [{"p": [para(c, jc="center")]} for c in r], "h": h})
    return _tbl(out, widths)

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_三角函數_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L12 三角函數"
FOOT = "高三數學．" + UNIT

# ================================================================ 文字內容
INTRO = [
    "這一課的題目有一個共通點：算式本身都很短，短到兩三行就寫完；"
    "難的是「揀對那條公式」。三角函數的公式數量比之前任何一課都多——"
    "六個三角比、四個象限的正負、和角差角六條、二倍角三條、通解三條，"
    "全部加起來超過二十條。憑記憶去揀，揀錯的機會比揀對還高。",
    "所以這一課的主工具是五張「提示卡」。每張卡上除了公式，"
    "最重要的是第一行那句「什麼時候翻我」——"
    "卡片的價值不在於寫了什麼公式，而在於你看着題目就知道要翻哪一張。"
    "貼在牆上的公式海報之所以沒有人用，就是因為它們只有公式、沒有觸發條件。",
    "五張卡分別對付：直角三角形的六個比（卡一）、"
    "只知道一個值要判斷正負或象限（卡二）、"
    "15°、75°、105° 這些「不是特殊角」的角（卡三）、"
    "式子裡出現 {2α} 或者 {(fn(sin)α + fn(cos)α)^2}（卡四）、"
    "問「通解」（卡五）。",
    "另外兩件事會幫你把卡揀對："
    "① 卡一與卡二各配一張圖，右邊寫算式、左邊擺圖，逐行對照——"
    "「對邊」是哪一條、第三象限的 x 是正是負，這些是用眼睛看出來的，不是背出來的。"
    "② 卡三那一段的程序最長（要拆角、揀公式、代四個值、再化簡），"
    "所以額外配一張手順卡，把四個動作逐個列出來。",
]

# ---------------------------------------------------------------- 六個三角比
RATIO_TXT = [
    "先講一件最容易被跳過、但錯得最多的事：「對邊」和「鄰邊」不是三角形的固有名稱，"
    "而是「相對於你正在看的那個角」而言的。同一條邊，看 ∠A 的時候是對邊，"
    "看 ∠B 的時候就變成鄰邊。斜邊是唯一不變的——它永遠是直角對面那一條，"
    "也永遠是三條之中最長的。",
    "所以做這一類題的第一個動作，不是套公式，而是先在圖上圈出「題目問的是哪個角」。"
    "圈完之後再標三條邊，標完才寫式子。跳過圈角這一步，"
    "{frac(3,5)} 與 {frac(4,5)} 就會互相調轉——這是本節唯一的失分來源。",
]
D5_RATIO_H = ("圖上看到什麼", "算式上寫什麼")
RATIO_PAIRS = [
    ("A",
     "看 ∠A：對邊是底邊 {a}（＝CB），鄰邊是左邊那條 {b}（＝AC），斜邊是 {c}（＝AB）。"
     "於是 {fn(sin)A = frac(對邊,斜邊) = frac(a,c)}、"
     "{fn(cos)A = frac(鄰邊,斜邊) = frac(b,c)}、"
     "{fn(tan)A = frac(對邊,鄰邊) = frac(a,b)}。"),
    ("B",
     "同一個三角形，改看 ∠B：對邊變成 {b}、鄰邊變成 {a}，斜邊仍然是 {c}。"
     "{fn(sin)B = frac(b,c)}、{fn(cos)B = frac(a,c)}、{fn(tan)B = frac(b,a)}。"
     "留意 {fn(sin)B = fn(cos)A}——兩個銳角互餘，"
     "所以一個的 sin 等於另一個的 cos。"),
    ("N",
     "代進實際數字（{AC = 6}、{CB = 8}、{AB = 10}）："
     "看 ∠A 時 {fn(sin)A = frac(8,10) = frac(4,5)}、"
     "{fn(cos)A = frac(6,10) = frac(3,5)}、{fn(tan)A = frac(8,6) = frac(4,3)}。"
     "三個答案全部約到最簡才算完成。"),
]
RATIO_NOTE = ("※ 另外三個比只是把上面三個「倒轉」，不必另外背："
              "{fn(cot)A = frac(1,fn(tan)A) = frac(鄰邊,對邊)}、"
              "{fn(sec)A = frac(1,fn(cos)A) = frac(斜邊,鄰邊)}、"
              "{fn(csc)A = frac(1,fn(sin)A) = frac(斜邊,對邊)}。"
              "⚠ 最易記錯的是 sec 與 csc 的配對："
              "sec 配的是 cos（不是 sin），csc 配的是 sin。"
              "記法：兩個字的第三個字母——sec 的 c 對應 cos，csc 的 s 對應 sin。"
              "※ 只要知道兩條邊，第三條一定可以用畢氏定理 {a^2 + b^2 = c^2} 補回，"
              "所以「題目只給兩條邊」從來不是做不下去的理由。")

CARD1 = dict(
    title="卡一・直角三角形的六個三角比",
    trigger="題目給了一個直角三角形（或給了兩條邊長），問 sin、cos、tan 等於多少。",
    statement="先圈出題目問的是哪一個角，再標「對邊／鄰邊／斜邊」，最後才寫分數。"
              "斜邊永遠是直角對面那一條；對邊與鄰邊隨着你看的角而對調。",
    formula="{fn(sin)A = frac(對邊,斜邊)}　{fn(cos)A = frac(鄰邊,斜邊)}　"
            "{fn(tan)A = frac(對邊,鄰邊)}　"
            "{fn(csc)A = frac(斜邊,對邊)}　{fn(sec)A = frac(斜邊,鄰邊)}　"
            "{fn(cot)A = frac(鄰邊,對邊)}")

EX_A = ("【範例A・六個三角比】"
        "（a）直角 {△ABC} 中 {∠C = 90°}、{AB = 13}、{AC = 5}，"
        "求 {fn(sin)A}、{fn(cos)A}、{fn(tan)A}、{fn(cot)A}、{fn(sec)A}、{fn(csc)A}。　"
        "（b）{△ABC} 中 {∠C = 90°}、{BC = 3}、{AC = 4}，求 {fn(sin)B} 與 {fn(tan)A}。")
A_TXT = [
    "（a）第一步：補回第三條邊。{∠C = 90°} 所以 AB 是斜邊，"
    "{BC = sqrt(13^2 - 5^2) = sqrt(169 - 25) = sqrt(144) = 12}。",
    "（a）第二步：圈出要看的角是 ∠A，然後標邊。"
    "對邊 ＝ BC ＝ 12（∠A 對面那一條）、鄰邊 ＝ AC ＝ 5、斜邊 ＝ AB ＝ 13。",
    "（a）第三步：照卡一逐個寫。"
    "{fn(sin)A = frac(12,13)}、{fn(cos)A = frac(5,13)}、{fn(tan)A = frac(12,5)}；"
    "另外三個是它們的倒數："
    "{fn(cot)A = frac(5,12)}、{fn(sec)A = frac(13,5)}、{fn(csc)A = frac(13,12)}。",
    "（a）檢查：{fn(sin)^2 A + fn(cos)^2 A = frac(144,169) + frac(25,169) = frac(169,169) = 1} ✔ "
    "這條恆等式對任何角都成立，是本節最好用的自我檢查。",
    "（b）先補斜邊：{AB = sqrt(3^2 + 4^2) = sqrt(9 + 16) = 5}。"
    "看 ∠B 時，對邊是 AC ＝ 4（∠B 對面），斜邊是 AB ＝ 5，"
    "所以 {fn(sin)B = frac(4,5)}。",
    "（b）換看 ∠A：對邊是 BC ＝ 3、鄰邊是 AC ＝ 4，"
    "所以 {fn(tan)A = frac(3,4)}。"
    "同一題問兩個不同的角，兩次都要重新圈角、重新標邊——這正是本題的考點。",
]
NOTE_A = ("※ (b) 最常見的錯法：看到 {BC = 3} 就寫 {fn(sin)B = frac(3,5)}。"
          "錯在把「B 這個字母旁邊的邊」當成 ∠B 的對邊。"
          "對邊是「角對面那一條」，∠B 在右下角，它對面那一條是左邊的 AC ＝ 4。"
          "對策：圈完角之後，用筆由那個角向對面畫一箭頭，箭頭指到的才是對邊。"
          "※ 為什麼 {fn(sin)B = fn(cos)A}：兩個銳角加起來是 90°，"
          "∠B 的對邊剛好就是 ∠A 的鄰邊。"
          "所以互餘角的 sin 與 cos 會對調——{fn(sin)30° = fn(cos)60° = frac(1,2)} "
          "就是同一件事。這條關係在檢查答案時很好用。"
          "※ (a) 那條 {fn(sin)^2 A + fn(cos)^2 A = 1} 值得每題做一次："
          "把你算出的 sin 與 cos 各自平方再相加，"
          "加不到 1 就表示至少有一個寫錯了，比重新做一次快得多。")

# ---------------------------------------------------------------- 象限符號
QUAD_TXT = [
    "上一節的角都在直角三角形裡，一定是銳角，六個比全部是正數。"
    "一旦角可以超過 90°（例如 135°、210°），就要用坐標的方式重新定義："
    "在角的終邊上取一點 {P(x, y)}，它與原點的距離是 {r}（{r} 永遠是正數），"
    "那麼 {fn(sin)θ = frac(y,r)}、{fn(cos)θ = frac(x,r)}、{fn(tan)θ = frac(y,x)}。",
    "因為 {r} 永遠是正數，三個比的正負就完全由 {x} 與 {y} 的正負決定，"
    "而 {x}、{y} 的正負又完全由「P 落在哪個象限」決定。"
    "所以「判斷正負」這件事根本不需要背——看圖就看得出來。",
    "把四個象限逐個看一次，就得出下面這張表；"
    "看完之後你會發現只需要記一句：一全正、二 sin 正、三 tan 正、四 cos 正。",
]
D5_QUAD_H = ("圖上看到什麼", "算式上寫什麼")
QUAD_PAIRS = [
    (1, "第一象限：{x > 0}、{y > 0}。"
        "{fn(sin)θ = frac(y,r)} 正、{fn(cos)θ = frac(x,r)} 正、"
        "{fn(tan)θ = frac(y,x)} 正 → 三個全部是正。"),
    (2, "第二象限：{x < 0}、{y > 0}。"
        "{fn(sin)θ} 正（{y} 正）、{fn(cos)θ} 負（{x} 負）、"
        "{fn(tan)θ} 負（正 ÷ 負）→ 只有 sin 是正。"),
    (3, "第三象限：{x < 0}、{y < 0}。"
        "{fn(sin)θ} 負、{fn(cos)θ} 負、"
        "{fn(tan)θ} 正（負 ÷ 負）→ 只有 tan 是正。"),
    (4, "第四象限：{x > 0}、{y < 0}。"
        "{fn(sin)θ} 負、{fn(cos)θ} 正、"
        "{fn(tan)θ} 負（負 ÷ 正）→ 只有 cos 是正。"),
]
QUAD_NOTE = ("※ 由第一象限逆時針數過去，「是正的那一個」依次是："
             "全部 → sin → tan → cos。"
             "這四個字的次序就是整張表，記住次序就不必逐格背。"
             "※ 另一個常用方向：題目給了兩個條件（例如 {fn(sin)θ > 0} 且 "
             "{fn(tan)θ < 0}），要反過來求象限。"
             "做法是各自列出可能的象限再取交集："
             "{fn(sin)θ > 0} → 一或二；{fn(tan)θ < 0} → 二或四；"
             "兩者共同的只有第二象限。"
             "⚠ 不要只看其中一個條件就作答——那是本節最貴的錯。")

CARD2 = dict(
    title="卡二・象限符號盤（判斷正負／判斷象限）",
    trigger="題目只給了一個三角函數的值（尤其是負值），"
            "或者出現「θ 在第幾象限」「{fn(sin)θ * fn(tan)θ < 0}」這類符號條件。",
    statement="在角的終邊上取點 {P(x, y)}，{r} 是它到原點的距離（永遠是正數）。"
              "{fn(sin)θ = frac(y,r)}、{fn(cos)θ = frac(x,r)}、{fn(tan)θ = frac(y,x)}——"
              "正負只由 x、y 決定。"
              "由第一象限逆時針數：全正 → sin 正 → tan 正 → cos 正。",
    formula="{fn(sin)^2 θ + fn(cos)^2 θ = 1}　"
            "{fn(tan)θ = frac(fn(sin)θ,fn(cos)θ)}　"
            "已知一個值求另一個時用這兩條，正負由象限決定")

EX_B = ("【範例B・判斷象限】"
        "（a）若 {fn(cos)θ ÷ fn(tan)θ < 0}，θ 在哪些象限？　"
        "（b）若 {fn(sin)θ ÷ fn(tan)θ > 0}，θ 在哪些象限？　"
        "（c）已知 {fn(cos)α = -frac(3,5)}，且 {α} 在第二象限，求 {fn(sin)α} 與 {fn(tan)α}。")
B_TXT = [
    "（a）不要急着逐個象限試。先把式子化簡："
    "{fn(cos)θ ÷ fn(tan)θ = fn(cos)θ ÷ frac(fn(sin)θ,fn(cos)θ) "
    "= fn(cos)θ * frac(fn(cos)θ,fn(sin)θ) = frac(fn(cos)^2 θ,fn(sin)θ)}。",
    "（a）分子 {fn(cos)^2 θ} 是平方，必定大於 0（θ 不等於 90°、270° 時）。"
    "所以整個式子的正負只由分母 {fn(sin)θ} 決定。"
    "式子 < 0 就表示 {fn(sin)θ < 0} → 翻卡二：sin 是負的象限是第三與第四。",
    "（b）同樣先化簡："
    "{fn(sin)θ ÷ fn(tan)θ = fn(sin)θ * frac(fn(cos)θ,fn(sin)θ) = fn(cos)θ}"
    "（{fn(sin)θ ≠ 0} 時）。"
    "式子 > 0 就是 {fn(cos)θ > 0} → 翻卡二：cos 是正的象限是第一與第四。",
    "（c）第一步，用 {fn(sin)^2 α + fn(cos)^2 α = 1} 求出 sin 的大小："
    "{fn(sin)^2 α = 1 - (-frac(3,5))^2 = 1 - frac(9,25) = frac(16,25)}，"
    "所以 {fn(sin)α} 的絕對值是 {frac(4,5)}。",
    "（c）第二步，用卡二定正負：α 在第二象限，sin 是正的，"
    "所以 {fn(sin)α = frac(4,5)}（不是 {-frac(4,5)}）。"
    "第三步：{fn(tan)α = frac(fn(sin)α,fn(cos)α) = frac(4,5) ÷ (-frac(3,5)) = -frac(4,3)}。",
    "（c）檢查：第二象限應該只有 sin 是正 —— "
    "算出來 {fn(sin)α} 正、{fn(cos)α} 負、{fn(tan)α} 負 ✔ 完全對得上卡二。",
]
NOTE_B = ("※ (a)(b) 兩題長得很像，但答案完全不同（三或四 vs 一或四），"
          "原因是化簡之後剩下的東西不同：(a) 剩 {frac(fn(cos)^2 θ,fn(sin)θ)}、"
          "(b) 剩 {fn(cos)θ}。"
          "所以這一類題的關鍵動作是「先化簡再判斷」，"
          "不是逐個象限代數字去試——代數字要試四次，而且很易漏其中一個。"
          "※ (c) 開方之後一定要停下來想正負，這是本節最常漏的一步。"
          "{sqrt(frac(16,25))} 的結果本身只給你 {frac(4,5)} 這個大小，"
          "正負要另外由象限決定。"
          "對策：算出大小之後，先在旁邊寫「第幾象限」四個字，再翻卡二填正負。"
          "※ 為什麼 {fn(cos)^2 θ} 一定大於 0 而不是「大於等於 0」："
          "如果 {fn(cos)θ = 0}，原式的 tan 本身就沒有定義了，"
          "所以題目已經隱含 θ 不在那些位置。")

# ---------------------------------------------------------------- 和角差角
SUM_TXT = [
    "考試裡經常要求 {fn(sin)15°}、{fn(cos)75°}、{fn(tan)105°} 這些值。"
    "它們不是特殊角，計算機以外沒有辦法直接讀出來——"
    "但它們全部都可以拆成兩個特殊角的和或差："
    "{15° = 45° - 30°}、{75° = 45° + 30°}、{105° = 60° + 45°}。",
    "拆開之後用和角差角公式，就把一個不會的角換成兩個會的角。"
    "所以這一節真正要練的不是背公式（公式在卡三上），"
    "而是「看到一個角，想得出它可以怎樣拆」。"
    "能用的零件只有四個：30°、45°、60°、90°。",
    "反方向也要認得：題目有時直接給你一串"
    "{fn(cos)29° fn(cos)31° - fn(sin)29° fn(sin)31°}，"
    "要你認出這就是 {fn(cos)(29° + 31°) = fn(cos)60°}。"
    "認得出的話一行就完，認不出就只能逐個查表——但表上根本沒有 29°。",
]
CARD3 = dict(
    title="卡三・和角差角公式 ＋ 特殊角值表",
    trigger="題目要求的角不是 30°／45°／60°／90°（例如 15°、75°、105°），"
            "或者式子長成「{fn(sin)A fn(cos)B ± fn(cos)A fn(sin)B}」的樣子。",
    statement="先把角拆成兩個特殊角的和或差，再代公式。"
              "⚠ 最易錯的一點：cos 的公式中間那個符號跟括號裡的相反"
              "（括號加，中間減；括號減，中間加），sin 則是一樣。",
    formula="{fn(sin)(α+-β) = fn(sin)α fn(cos)β +- fn(cos)α fn(sin)β}　"
            "{fn(cos)(α+-β) = fn(cos)α fn(cos)β -+ fn(sin)α fn(sin)β}　"
            "{fn(tan)(α+-β) = frac(fn(tan)α +- fn(tan)β,1 -+ fn(tan)α fn(tan)β)}")

SPECIAL_HEAD = ("角度", "{fn(sin)}", "{fn(cos)}", "{fn(tan)}")
SPECIAL_ROWS = [
    ("30°", "{frac(1,2)}", "{frac(sqrt(3),2)}", "{frac(sqrt(3),3)}"),
    ("45°", "{frac(sqrt(2),2)}", "{frac(sqrt(2),2)}", "1"),
    ("60°", "{frac(sqrt(3),2)}", "{frac(1,2)}", "{sqrt(3)}"),
    ("90°", "1", "0", "沒有定義"),
]

CARD_D2 = dict(
    title="▍手順卡・求一個「不是特殊角」的三角值",
    trigger="題目要求 15°、75°、105° 這些角的 sin／cos／tan。",
    steps=[("把角拆成兩個特殊角的和或差",
            "能用的零件只有 30°、45°、60°、90° 四個。105° ＝ 60° ＋ 45°"),
           ("翻卡三，揀出對應那一條公式",
            "sin 揀 sin 那條、cos 揀 cos 那條。cos 的中間符號與括號裡相反"),
           ("四個特殊角的值逐個代進去",
            "一條 sin 或 cos 公式要代四個值，漏其中一個是本節最常見的失分"),
           ("通分、化簡；tan 的結果要有理化",
            "分母不可以留根號。{frac(1,sqrt(3))} 要寫成 {frac(sqrt(3),3)}")])

EX_C = ("【範例C・和角差角】"
        "（a）求 {fn(sin)15°}。　（b）求 {fn(cos)105°}。　"
        "（c）求 {fn(cos)29° fn(cos)31° - fn(sin)29° fn(sin)31°} 的值。")
C_TXT = [
    "（a）第一步（手順卡）：{15° = 45° - 30°}。"
    "第二步：要求的是 sin，而且是「差」，所以揀 "
    "{fn(sin)(α-β) = fn(sin)α fn(cos)β - fn(cos)α fn(sin)β}。",
    "（a）第三步：代四個值——{fn(sin)45° = frac(sqrt(2),2)}、"
    "{fn(cos)30° = frac(sqrt(3),2)}、{fn(cos)45° = frac(sqrt(2),2)}、"
    "{fn(sin)30° = frac(1,2)}。"
    "{fn(sin)15° = frac(sqrt(2),2) * frac(sqrt(3),2) - frac(sqrt(2),2) * frac(1,2)}。",
    "（a）第四步：{= frac(sqrt(6),4) - frac(sqrt(2),4) = frac(sqrt(6) - sqrt(2),4)}。"
    "檢查：{sqrt(6) ≈ 2.449}、{sqrt(2) ≈ 1.414}，"
    "所以答案 {≈ frac(1.035,4) ≈ 0.259}。"
    "15° 是很小的角，sin 應該接近 0 而且是正數 ✔ 合理。",
    "（b）第一步：{105° = 60° + 45°}。第二步：要求 cos，而且是「和」，"
    "所以揀 {fn(cos)(α+β) = fn(cos)α fn(cos)β - fn(sin)α fn(sin)β}——"
    "留意括號裡是加號，中間卻是減號。",
    "（b）第三、四步：{fn(cos)105° = frac(1,2) * frac(sqrt(2),2) "
    "- frac(sqrt(3),2) * frac(sqrt(2),2) = frac(sqrt(2),4) - frac(sqrt(6),4) "
    "= frac(sqrt(2) - sqrt(6),4)}。"
    "檢查：105° 在第二象限，卡二說第二象限的 cos 是負的；"
    "{sqrt(2) < sqrt(6)} 所以答案確實是負數 ✔",
    "（c）這一題是反方向用。式子的形狀是「{fn(cos)A fn(cos)B - fn(sin)A fn(sin)B}」，"
    "對照卡三就知道它等於 {fn(cos)(A + B)}（中間是減號 → 括號裡是加號）。"
    "所以 {= fn(cos)(29° + 31°) = fn(cos)60° = frac(1,2)}。",
]
NOTE_C = ("※ (b) 那句「括號加、中間減」是本課最貴的一條規則。"
          "把它寫錯的話，{fn(cos)105°} 會變成 "
          "{frac(sqrt(2) + sqrt(6),4) ≈ 0.966}——一個正數，"
          "但 105° 明明在第二象限、cos 一定是負的。"
          "所以做完 cos 的和角差角，順手用卡二檢查一次正負，"
          "符號寫反的話當場就攔得住。"
          "※ (c) 這種「反方向」的題目在考試中比正方向更常見，"
          "因為它一眼看上去像要逐個查表，其實一行就完。"
          "認法：見到兩個乘積相加或相減、而且四個因子剛好是「兩個角的 sin 與 cos」，"
          "就翻卡三反過來讀。"
          "※ 中間符號與括號符號的關係，三條公式各不相同，值得在卡三上劃線："
          "sin 是「一樣」（括號加，中間加）；cos 是「相反」；"
          "tan 的分子跟括號一樣、分母相反。"
          "只要記住「只有 cos 和 tan 的分母會反」，三條就都對了。")

# ---------------------------------------------------------------- 二倍角
DBL_TXT = [
    "二倍角公式其實不是新公式，是把和角公式裡的 β 換成 α 而已："
    "{fn(sin)2α = fn(sin)(α + α) = fn(sin)α fn(cos)α + fn(cos)α fn(sin)α "
    "= 2 fn(sin)α fn(cos)α}。"
    "cos 的一樣：{fn(cos)2α = fn(cos)^2 α - fn(sin)^2 α}。",
    "cos 的二倍角有三個等價寫法，因為可以用 "
    "{fn(sin)^2 α + fn(cos)^2 α = 1} 把其中一項換掉："
    "{fn(cos)2α = fn(cos)^2 α - fn(sin)^2 α = 1 - 2 fn(sin)^2 α = 2 fn(cos)^2 α - 1}。"
    "三條都對，揀哪一條看題目給了什麼——題目給 sin 就用中間那條，給 cos 就用最後那條，"
    "這樣可以完全避開開方與判斷正負。",
    "另外有一個變形，本課考得最多，一定要認得："
    "{(fn(sin)α + fn(cos)α)^2 = fn(sin)^2 α + 2 fn(sin)α fn(cos)α + fn(cos)^2 α "
    "= 1 + fn(sin)2α}。"
    "所以題目給你 {fn(sin)α + fn(cos)α} 的值、問 {fn(sin)2α}，"
    "動作只有一個：兩邊平方，然後減 1。",
]
CARD4 = dict(
    title="卡四・二倍角公式",
    trigger="式子裡出現 {2α}、{2θ}（例如問 {fn(sin)2α}），"
            "或者題目給了 {fn(sin)α + fn(cos)α} 的值。",
    statement="cos 的三條是同一條，用 {fn(sin)^2 α + fn(cos)^2 α = 1} 互換而已。"
              "題目給 sin 就用 {1 - 2 fn(sin)^2 α}、給 cos 就用 {2 fn(cos)^2 α - 1}，"
              "可以避開開方。",
    formula="{fn(sin)2α = 2 fn(sin)α fn(cos)α}　"
            "{fn(cos)2α = fn(cos)^2 α - fn(sin)^2 α = 1 - 2 fn(sin)^2 α "
            "= 2 fn(cos)^2 α - 1}　"
            "{(fn(sin)α + fn(cos)α)^2 = 1 + fn(sin)2α}")

EX_D = ("【範例D・二倍角】"
        "（a）已知 {fn(sin)α = frac(5,13)}，{α ∈ (frac(π,2), π)}，"
        "求 {fn(sin)2α} 與 {fn(cos)2α}。　"
        "（b）若 {fn(sin)α + fn(cos)α = frac(1,3)}，求 {fn(sin)2α}。")
D_TXT = [
    "（a）第一步：{fn(sin)2α} 需要 {fn(cos)α}，題目沒有給，要自己補。"
    "{fn(cos)^2 α = 1 - (frac(5,13))^2 = 1 - frac(25,169) = frac(144,169)}，"
    "所以大小是 {frac(12,13)}。",
    "（a）第二步（翻卡二）：{α ∈ (frac(π,2), π)} 即第二象限，cos 是負的，"
    "所以 {fn(cos)α = -frac(12,13)}。"
    "這一步不能省——省了的話下一步的答案會連正負都錯。",
    "（a）第三步：{fn(sin)2α = 2 fn(sin)α fn(cos)α "
    "= 2 * frac(5,13) * (-frac(12,13)) = -frac(120,169)}。",
    "（a）第四步：{fn(cos)2α} 揀「給 sin 用」那一條，就不必再用剛才那個負數："
    "{fn(cos)2α = 1 - 2 fn(sin)^2 α = 1 - 2 * frac(25,169) "
    "= 1 - frac(50,169) = frac(119,169)}。",
    "（b）認出這是 {(fn(sin)α + fn(cos)α)^2 = 1 + fn(sin)2α} 那個變形。"
    "兩邊平方：{(frac(1,3))^2 = frac(1,9)}，即 {1 + fn(sin)2α = frac(1,9)}。"
    "所以 {fn(sin)2α = frac(1,9) - 1 = -frac(8,9)}。",
]
NOTE_D = ("※ (a) 的第二步是本題的分水嶺。跳過象限判斷、直接寫 "
          "{fn(cos)α = frac(12,13)} 的話，"
          "會得出 {fn(sin)2α = frac(120,169)}——大小完全正確、正負完全相反，"
          "而且自己看不出有問題。"
          "對策：凡是「由一個三角值求另一個」，開方之後立刻寫下象限，再定正負。"
          "※ (a) 第四步示範了「揀公式可以省工夫」："
          "三條 cos 二倍角公式都答得出 {frac(119,169)}，"
          "但用 {fn(cos)^2 α - fn(sin)^2 α} 要先處理那個負數、"
          "用 {2 fn(cos)^2 α - 1} 也要，只有 {1 - 2 fn(sin)^2 α} 直接用題目給的 sin。"
          "揀公式之前先看題目給了什麼，這個習慣能省掉一半的計算錯誤。"
          "※ (b) 如果不認得那個變形，就要先解一條聯立方程求出 sin 與 cos 各自的值，"
          "而且會得出兩組答案、還要再判斷象限——長很多倍，"
          "還未必做得完。認得變形與否，是這一題的全部。"
          "⚠ (b) 順帶一提：{fn(sin)2α = -frac(8,9)} 是負數，"
          "而 {fn(sin)α + fn(cos)α = frac(1,3)} 是正數，兩者並不矛盾——"
          "{2α} 與 {α} 是兩個不同的角。")

# ---------------------------------------------------------------- 通解
GEN_TXT = [
    "前面幾節都是「給角求值」，這一節反過來：「給值求角」。"
    "麻煩的地方是這種題有無限多個答案——"
    "{fn(sin)x = frac(1,2)} 的解有 30°、150°、390°、510°⋯ 一直數不完，"
    "所以答案要寫成一條含 {n} 的公式，叫做「通解」。",
    "三條通解公式的形狀不一樣，要分開記，而分別的來源是圖："
    "sin 在一個 {2π} 週期裡有兩個解、而且它們對稱於 {frac(π,2)}，"
    "所以用 {(-1)^n} 這個「一次正一次負」的寫法把兩個解合成一條；"
    "cos 的兩個解對稱於 {x} 軸，所以用 {±}；"
    "tan 的週期只有 {π}，一個週期裡只有一個解，所以最簡單。",
    "考試多數是選擇題，四個選項的形狀就已經在提示你答案是哪一族："
    "見到 {(-1)^n} 就是 sin、見到 {2nπ ±} 就是 cos、"
    "見到 {nπ +} 而且沒有其他裝飾就是 tan。"
    "認清形狀之後，只需要算出那個 arc 值就完成了。",
]
CARD5 = dict(
    title="卡五・三角方程的通解",
    trigger="題目出現「通解」「一般解」，或者答案的選項裡有 {n}（例如 {2nπ ± frac(π,4)}）。",
    statement="{n} 是任意整數。先看是 sin、cos 還是 tan，揀出對應那一條，"
              "再把 {arc} 值算出來代入。"
              "{arc} 值就是「第一個想得到的那個角」——"
              "{fn(arcsin)frac(1,2) = frac(π,6)}、{fn(arccos)frac(1,2) = frac(π,3)}。",
    formula="{fn(sin)x = k → x = nπ + (-1)^n fn(arcsin)k}　"
            "{fn(cos)x = k → x = 2nπ ± fn(arccos)k}　"
            "{fn(tan)x = k → x = nπ + fn(arctan)k}")

EX_E = ("【範例E・通解】"
        "（a）求 {fn(sin)x = 0} 的通解。　"
        "（b）求 {fn(cos)x = frac(sqrt(2),2)} 的通解。　"
        "（c）求 {fn(sin)x = -0.5} 的通解。")
E_TXT = [
    "（a）是 sin，揀 {x = nπ + (-1)^n fn(arcsin)k}。"
    "{fn(arcsin)0 = 0}，代進去：{x = nπ + (-1)^n * 0 = nπ}。"
    "檢查：{n = 0, 1, 2} 依次給出 {0、π、2π}，"
    "這些角的 sin 確實全部是 0 ✔",
    "（b）是 cos，揀 {x = 2nπ ± fn(arccos)k}。"
    "{fn(arccos)frac(sqrt(2),2) = frac(π,4)}（因為 {fn(cos)45° = frac(sqrt(2),2)}），"
    "所以 {x = 2nπ ± frac(π,4)}。",
    "（b）檢查：{n = 0} 給出 {frac(π,4)} 與 {-frac(π,4)}，"
    "即 45° 與 −45°。兩者的 cos 都是 {frac(sqrt(2),2)} ✔ "
    "（cos 是偶函數，正負角的值相同，這正是公式用 {±} 的原因。）",
    "（c）是 sin，而且 {k} 是負數。"
    "{fn(arcsin)(-0.5) = -frac(π,6)}——arcsin 的值可以是負的，"
    "代表順時針量的角。"
    "代進去：{x = nπ + (-1)^n * (-frac(π,6))}。",
    "（c）把負號併進去：{(-1)^n * (-1) = (-1)^(n+1)}，"
    "所以 {x = nπ + (-1)^(n+1) frac(π,6)}。"
    "檢查：{n = 1} 給出 {π + frac(π,6) = frac(7π,6)}，即 210°；"
    "{fn(sin)210° = -frac(1,2)} ✔",
]
NOTE_E = ("※ (c) 那一步「把負號併進 {(-1)^n}」是選擇題的關鍵。"
          "四個選項通常會同時出現 {(-1)^n} 與 {(-1)^(n+1)} 兩種寫法，"
          "而 {x = nπ + (-1)^n(-frac(π,6))} 與 "
          "{x = nπ + (-1)^(n+1) frac(π,6)} 是同一個答案的兩種樣子。"
          "如果選項裡找不到你算出來的形狀，先試把負號搬進指數再看一次。"
          "※ 三條公式最容易混的是 sin 與 cos："
          "sin 用 {nπ} 配 {(-1)^n}、cos 用 {2nπ} 配 {±}。"
          "記法：cos 的兩個解「一正一負」，所以用 {±}；"
          "sin 的兩個解不是一正一負（是 30° 與 150°），"
          "所以要用 {(-1)^n} 這種交替的寫法。"
          "※ 這一節不必記 arcsin、arccos 的完整定義，"
          "只需要會用卡三的特殊角值表反過來查："
          "{fn(cos)? = frac(1,2)} → 表上 60° 那一行的 cos 是 {frac(1,2)} → "
          "{fn(arccos)frac(1,2) = frac(π,3)}。")

# ---------------------------------------------------------------- 速查表
SUM_HEAD = ("題目長成這樣", "翻哪一張卡", "一句話記法")
SUM_ROWS = [
    ("給了直角三角形或兩條邊，問 sin／cos／tan",
     "卡一・六個三角比",
     "先圈角、再標「對邊／鄰邊／斜邊」、最後才寫分數。斜邊永遠是直角對面那條"),
    ("只給一個三角值（尤其負值），或問「在第幾象限」",
     "卡二・象限符號盤",
     "一全正、二 sin 正、三 tan 正、四 cos 正。開方之後一定要先定象限再定正負"),
    ("要求 15°、75°、105° 這些角，或見到兩個乘積相加減",
     "卡三・和角差角",
     "拆成兩個特殊角。cos 的中間符號跟括號裡相反，sin 的一樣"),
    ("式子裡有 {2α}，或給了 {fn(sin)α + fn(cos)α}",
     "卡四・二倍角",
     "{fn(sin)2α = 2 fn(sin)α fn(cos)α}；給 sin 就用 {1 - 2 fn(sin)^2 α}"),
    ("問「通解」，或選項裡有 {n}",
     "卡五・通解",
     "sin 配 {nπ + (-1)^n}、cos 配 {2nπ ±}、tan 配 {nπ +}"),
]

# ================================================================ 教師實施說明
TN = dict(
    main_design="D7 提示卡——五張（六個三角比／象限符號盤／和角差角＋特殊角值表／"
                "二倍角／三角方程通解）。"
                "照 teaching-designs.md 對 D7 的規格施工：每張卡第一行必定是"
                "「什麼時候翻我」的觸發條件，卡一與卡二另外配圖，"
                "構成「文字敘述＋圖＋代數符號」三件套。"
                "版面上每張卡之後緊接一個用該卡走完的範例，"
                "卡不是印完就算，而是在正文裡實際被翻五次",
    aux_designs=("D5 圖文雙軌——只用在真正有圖可對照的兩處："
                 "第二節（同一個直角三角形，focus 由 ∠A 換成 ∠B，"
                 "三條邊的身份全部對調）與第三節（四個象限各一列，"
                 "左欄是終邊上一點 P 與 x、y 的正負，右欄是三個比的正負）。"
                 "左右逐列橫向對齊，QB-V5 會目視查這一項。"
                 "其餘三節（和角差角／二倍角／通解）沒有可對照的圖，"
                 "刻意不硬套——硬加一張示意圖只是裝飾，不是設計",
                 "D2 手順卡——只有一張，管第四節（求非特殊角的三角值）那一段程序。"
                 "這一段是本課唯一「步驟長到會在工作記憶中崩潰」的地方："
                 "拆角 → 揀公式 → 代四個值 → 通分有理化，"
                 "而且第三步一次要代四個數，漏其中一個是最常見的失分。"
                 "其餘四節每節只有一至兩個動作，不需要手順卡"),
    reason=(
        "本課取 A5 三角函數 39 題（去重後 20 個獨立題型），"
        "涵蓋五個題群：直角三角形六個三角比、象限符號判斷、"
        "和角差角公式（含逆用）、二倍角公式、三角方程通解。"
        "對照 MATH-031／043／044／050／069、"
        "MOCK2-027／028／037／038／039／049／063／064／065／074／087／089／"
        "097／098／108／119／120／121／122／139／142／143／145／146／147／177 等題。"
        "數學結構橫跨兩種：三角比與象限屬 teaching-designs.md §1 的 S5"
        "（幾何定理與推理，核心瓶頸是「需同時提取多個定理，記憶檢索失敗」），"
        "和角差角／二倍角／通解屬 S2（多步驟程序運算，"
        "§1 的典型單元欄明列「三角恆等變形」）。"
        "依 §1 表下的規則取瓶頸較前端的一個為主設計——"
        "本課學生真正卡住的地方在動筆之前：公式超過二十條，"
        "揀錯公式的失分遠多於算錯數，"
        "正是 S5 的 D7 提示卡所針對的「記憶檢索失敗」。"
        "S5 的建議輔助欄剛好就是 D5 圖文雙軌與 D2 手順卡，"
        "本課按題群的實際性質把兩者各自安放到合適的節次，"
        "而不是全課通用。"
        "三種設計＝主 D7 ＋ 輔 D5、D2，未超過「主1＋輔2」上限；"
        "刻意沒有加 D12 自我核對——本課的檢查動作已經內建在卡一"
        "（{fn(sin)^2 + fn(cos)^2 = 1}）與卡二（用象限覆核正負）裡面，"
        "再加一張核對清單就是第四套外部工具，違反上限"),
    density="抽離小班（Tier 2）",
    fading=(
        "提示卡（D7，主設計，褪除分四級）："
        "講義印五張完整卡（觸發條件＋敘述＋公式＋圖）並在範例中逐張示範 → "
        "練習A 每題下方重印該用的那張卡的公式列（觸發條件與圖不再印）→ "
        "練習B 只給卡號（「第 3 題用卡三」），公式要自己想得起來 → "
        "練習C 完全移除，工具卡收起 → 之後只留一句"
        "「先想清楚這題屬於哪一類」→ 完全移除。｜"
        "圖文雙軌（D5）：講義的雙軌表左右全滿 → "
        "練習A 左欄圖已給、右欄留空讓學生填算式 → "
        "練習B 只給圖不給表格欄位 → 練習C 兩者皆無，圖要自己畫。｜"
        "手順卡（D2）：講義印完整卡（動作＋※易錯點）→ "
        "練習A 第 3 題旁重印精簡版（只留四個動作）→ "
        "練習B 只寫「四步」→ 練習C 移除。"),
    flows=("F5 課前流程預告（今天五件事：卡一＋圖＋範例A → 卡二＋圖＋範例B → "
           "卡三＋手順卡＋範例C → 卡四＋範例D → 卡五＋範例E → 練習A／B／C）",
           "F2 番茄鐘分段（「看圖說話」（卡一、卡二，本課唯一有圖的兩節）、"
           "「拆角與代值」（卡三、卡四）、「通解」（卡五）三塊各自是一段；"
           "練習的兩個核對點與這三段對齊，配震動計時器使用）",
           "F1 師徒制對話四步（建議用在第二節與第三節："
           "「這條邊為什麼是對邊」「第三象限的 tan 為什麼是正」"
           "都是講得出才算懂的東西，適合用不准動筆的口述環節。"
           "尤其第二節的 ∠A → ∠B 對調，一定要學生用自己的話講一次）",
           "F4 過程導向回饋與分步計分（每題把「認出題型／翻對卡」「拆角或標邊」"
           "「代值」「化簡與檢查正負」分四步各給分。"
           "本課學生最常見的情況是卡揀對、大小算對、只錯正負，"
           "與完全不會做要分開評價，對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（五張提示卡即為此項；本課的失分集中在「揀錯公式」，"
               "若獲准帶入測考，建議把提示卡寫進 IEP 第 9 點——"
               "本課是本學年最需要公式卡的一課）",
               "a5 放大字體（卡一與卡二的圖放大不會破版，可單獨放大給視覺搜尋困難的學生）",
               "a6 增加行距／放大作答欄",
               "a7 調整計分標準（認題型／標邊或拆角／代值／化簡檢查分步給分；"
               "「只錯正負」建議給部分分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("符號寫法（本課定案，之後幾課沿用）",
            "①三角函數名一律正體（sin、cos、tan），不用斜體——"
            "斜體 sin 看起來像 s×i×n 三個變數相乘，"
            "對容易把符號讀成字母的學生特別致命。"
            "②角度制與弧度制兩種都會出現（題庫兩種都有）："
            "涉及特殊角時用角度制（15°、105°）較直觀，"
            "涉及通解與區間時用弧度制（{2nπ ± frac(π,4)}、{α ∈ (frac(π,2), π)}）"
            "因為考卷就是這樣印。講義兩種並用並在範例中互相對照"
            "（例如範例E(c) 明講 {frac(7π,6)} 即 210°），"
            "不要為了統一而把其中一種消滅——學生兩種都要認得。"
            "③負分數一律寫成 {-frac(24,25)}，不寫成分子帶負號的形式。"),
           ("與前幾課的銜接",
            "①卡一的畢氏定理與 L8 直線與圓的距離公式是同一件事，"
            "上課時值得指出來——{sqrt(3^2 + 4^2) = 5} 在兩課都出現過。"
            "②卡二「兩個條件取交集」的做法與 L7 二次不等式的解集取交集同一個動作，"
            "學生若在 L7 做得順，這裡可以直接借用。"
            "③本課的 {(-1)^n} 與 L11 二項式定理的 {(-1)^r} 是同一個東西，"
            "都是「一次正一次負」的開關。"),
           ("刻意避開的內容",
            "①MOCK2-148（{∠ABC = 90°}、求 {fn(sin)∠CAD}）："
            "標準解法要用向量外積或坐標法，超出本課範圍；"
            "而且原稿的圖已缺失，D、C 的相對位置只能由文字推斷。"
            "②MOCK2-149：原稿的角度範圍是 {45° < β < 90°}，"
            "但 {fn(sin)β = frac(sqrt(2),2)} 在此開區間內無解"
            "（唯一解 45° 落在邊界外），疑為 OCR 把 ≤ 讀成 <。"
            "③MATH-032（{fn(cos)α = -frac(3,5)} 求 {fn(sin)2α}）："
            "原題沒有給象限，{fn(cos)α < 0} 只確定 α 在第二或第三象限，"
            "兩種情況的答案正負相反，實際有兩解。"
            "題庫已補上「{α ∈ (0, π)}」的假設，但補假設的題目不適合當練習——"
            "本課改用有明確象限的 MOCK2-028。"
            "教學上這題其實很有價值（示範「沒有象限就沒有唯一答案」），"
            "建議留到綜合演練當討論題。"
            "④MOCK2-144（{fn(sin)159° fn(sin)21° + fn(cos)159° fn(cos)21°}）："
            "化簡後得 {fn(cos)138°}，138° 不是特殊角，"
            "答案只能寫成 {-fn(cos)42°} 或者查計算機取近似值，"
            "與本課「拆成特殊角」的訓練目標相反。"
            "⑤MATH-070／MOCK2-140（{fn(sin)α + fn(sin)β = 1}、"
            "{fn(cos)α + fn(cos)β = 0}，求 {fn(cos)(α+β)}）："
            "要先平方相加、再解聯立三角方程，步驟遠超本課的 1.25 小時，"
            "而且中間用到積化和差的思路。"
            "以上五項已列入交付摘要的剔除清單。"),
           ("題量說明",
            "本課練習共 6 題（練習A／B／C 各 2 題），合共 13 個小問，"
            "五張提示卡每張至少被用到兩次："
            "卡一（第 1 題三個小問）、卡二（第 2 題、第 4(a) 題、第 6(a) 題）、"
            "卡三（第 3 題、第 5(a) 題）、卡四（第 4 題、第 5(b) 題、第 6(a) 題）、"
            "卡五（第 6(b) 題）。"
            "第 5、6 兩題各自要在同一題內連續換兩至三張卡"
            "（第 5 題：卡三求出 {fn(sin)105°} 與 {fn(cos)105°}，"
            "再用卡四的二倍角求 {fn(sin)210°}；"
            "第 6 題：卡二定 {fn(sin)α} 的正負 → 卡四求二倍角 → 卡五求通解），"
            "這是練習C 的難度來源，不是靠數字變大。"),
           ("配套文件",
            "《第2章 L12 三角函數　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L12 三角函數　工具卡》"
            "（五張提示卡 ＋ 一張手順卡，剪下護貝放桌面）。"
            "本課的工具卡是全學年最值得長期保留的一張——"
            "三角函數的公式在之後的綜合演練仍然會用到。")),
)


# ================================================================ docx
def build_docx_file():
    figdir = os.path.join(HERE, "_figtmp")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    def img(svg, name, cm):
        png = os.path.join(figdir, name + ".png")
        ds.svg_to_png(svg, png, scale=3)
        return image_para(png, width_cm=cm)

    TRI = {"A": figs.tri_A(), "B": figs.tri_B(), "N": figs.tri_num()}

    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    # ---- 二、六個三角比（D5 ＋ 卡一 ＋ 範例A）
    P.append(heading("二、六個三角比：先圈角，再標邊", page_break_before=True))
    for t in RATIO_TXT:
        P.append(para(t))
    P.append(dual_track_table(
        [(img(TRI[k], "tri" + k, 6.0), v) for k, v in RATIO_PAIRS],
        media=MEDIA, headers=D5_RATIO_H))
    P.append(shaded_box(RATIO_NOTE))
    P.append(reference_card(CARD1["title"], CARD1["trigger"], CARD1["statement"],
                            formula=CARD1["formula"],
                            figure=img(figs.tri_blank(), "cbl", 5.2), media=MEDIA))
    P.append(blank())
    P.append(problem_box([para(EX_A)]))
    for t in A_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_A))

    # ---- 三、象限（D5 ＋ 卡二 ＋ 範例B）
    P.append(heading("三、角超過 90° 之後：象限決定正負", page_break_before=True))
    for t in QUAD_TXT:
        P.append(para(t))
    P.append(dual_track_table(
        [(img(figs.quad_point(q), "q%d" % q, 5.6), v) for q, v in QUAD_PAIRS],
        media=MEDIA, headers=D5_QUAD_H))
    P.append(shaded_box(QUAD_NOTE))
    P.append(reference_card(CARD2["title"], CARD2["trigger"], CARD2["statement"],
                            formula=CARD2["formula"],
                            figure=img(figs.quad_sign(), "cq", 7.4), media=MEDIA))
    P.append(blank())
    P.append(problem_box([para(EX_B)]))
    for t in B_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_B))

    # ---- 四、和角差角（卡三 ＋ D2 ＋ 範例C）
    P.append(heading("四、不是特殊角的角：拆開來算", page_break_before=True))
    for t in SUM_TXT:
        P.append(para(t))
    P.append(reference_card(CARD3["title"], CARD3["trigger"], CARD3["statement"],
                            formula=CARD3["formula"]))
    P.append(para("卡三配套的特殊角值表（拆角之後要代的四個值全部在這裡）："))
    P.append(grid_table(SPECIAL_ROWS, SPECIAL_HEAD))
    P.append(step_card(CARD_D2["title"], CARD_D2["steps"], trigger=CARD_D2["trigger"]))
    P.append(blank())
    P.append(problem_box([para(EX_C)]))
    for t in C_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_C))

    # ---- 五、二倍角（卡四 ＋ 範例D）
    P.append(heading("五、式子裡出現 2α：二倍角", page_break_before=True))
    for t in DBL_TXT:
        P.append(para(t))
    P.append(reference_card(CARD4["title"], CARD4["trigger"], CARD4["statement"],
                            formula=CARD4["formula"]))
    P.append(blank())
    P.append(problem_box([para(EX_D)]))
    for t in D_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_D))

    # ---- 六、通解（卡五 ＋ 範例E）
    P.append(heading("六、給值求角：通解", page_break_before=True))
    for t in GEN_TXT:
        P.append(para(t))
    P.append(reference_card(CARD5["title"], CARD5["trigger"], CARD5["statement"],
                            formula=CARD5["formula"]))
    P.append(blank())
    P.append(problem_box([para(EX_E)]))
    for t in E_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_E))

    # ---- 七、速查
    P.append(heading("七、五張卡速查（做每一題之前掃一眼）", page_break_before=True))
    P.append(para("先認出題目屬於哪一行，才決定翻哪一張卡。"
                  "認錯行的話，後面的計算做得再仔細都沒有用——"
                  "這一課的失分有一半在這裡。"))
    P.append(three_column_table(SUM_ROWS, headers=SUM_HEAD, row_h=1100))

    P.append(heading("八、接下來"))
    P.append(para("請拿出《第2章 L12 三角函數　課堂練習》，"
                  "並把《工具卡》剪下放在桌面。"
                  "練習A 每題下方會重印該用的那張卡的公式列（觸發條件與圖不再印）；"
                  "練習B 只告訴你翻第幾張卡；"
                  "練習C 兩者都不給，而且同一題裡要連續換兩至三張卡。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"),
                      footer_text=FOOT, media=MEDIA)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to",
            "+-": r"\pm", "-+": r"\mp", "*": r"\times"}


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
    # fn() 要在 frac/sqrt 之前處理（L7 踩過的次序坑）
    body = re.sub(r"fn\((\w+)\)", r"\\\1 ", body)
    body = _conv(body)
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    body = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", body)
    body = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", body)
    body = re.sub(r"\^(\w{2,})", r"^{\1}", body)
    body = re.sub(r"_(\w{2,})", r"_{\1}", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    body = body.replace("<", r" \lt ").replace(">", r" \gt ")
    body = re.sub(r"(?<![\\{\w.!])(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)(?![}\w.])",
                  r"\\frac{\1}{\2}", body)
    body = body.replace("%", r"\%")
    # 度數符號要寫成上標 circ，直接留 ° 的話 MathJax 會當成普通符號
    # 並在數字與它之間加一個空位（印出來像「cos 75 ˚」，與 docx 版不一致）
    body = body.replace("°", r"^{\circ}")
    # 中文（對邊／鄰邊／斜邊／沒有定義）要包 \text{}，否則 MathJax 逐字當變數排斜體
    body = re.sub(r"[\u4e00-\u9fff]+", lambda x: r"\text{%s}" % x.group(0), body)
    return r"\(%s\)" % body


def _h(s):
    """{} 內轉 TeX，其餘轉義。`**` 兩版都不支援，先剝走。"""
    import re
    s = s.replace("**", "")
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def _refcard_html(c, svg=None):
    fig = '<div class="cardfig">%s</div>' % svg if svg else ""
    return ('<div class="ref-card"><div style="font-weight:700;font-size:13pt">%s</div>'
            '<div class="trigger">什麼時候翻我：%s</div>%s'
            '<div>%s</div><div>%s</div></div>'
            % (_esc(c["title"]), _h(c["trigger"]), fig,
               _h(c["statement"]), _h(c["formula"])))


def _step_html(card):
    rows = ['<tr><th colspan="2">%s</th></tr>' % _h(card["title"])]
    rows.append('<tr><td colspan="2" style="font-weight:400">什麼時候用：%s</td></tr>'
                % _h(card["trigger"]))
    for i, (act, pit) in enumerate(card["steps"], 1):
        rows.append('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                    % (i, _h(act), _h(pit)))
    return '<table class="d-tbl step-card">%s</table>' % "".join(rows)


def _dual_html(pairs, headers):
    def side(x):
        return x if x.lstrip().startswith("<svg") else _h(x)
    head = ("<thead><tr><th>%s</th><th>%s</th></tr></thead>"
            % (_h(headers[0]), _h(headers[1])))
    body = "".join("<tr><td>%s</td><td>%s</td></tr>" % (side(l), side(r))
                   for l, r in pairs)
    return '<table class="d-tbl dual-track">%s<tbody>%s</tbody></table>' % (head, body)


def _tbl_html(rows, headers, cls="three-col"):
    return ('<table class="d-tbl %s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
            % (cls, "".join("<th>%s</th>" % _h(h) for h in headers),
               "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _h(c) for c in r)
                       for r in rows)))


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace(
        "[講義標題]", "講義：" + UNIT)
    head = head.replace("</head>", """<style>
  /* QB-20：範本的頁尾用固定定位＋白底，內文流到頁底會被它蓋住。
     解法是把 @page 的下邊界撐大（內文區因此提早結束），再把頁尾用負的 bottom
     推進那條新增的邊界裡。這裡刻意只覆寫 bottom，不重寫定位屬性——
     QB-15c 驗收整份文件的那條定位規則要恰好出現一次，
     連註解裡都不可以再寫一次那兩個關鍵字（範本本身也是這樣避開的）。 */
  @page { margin-bottom: 1.5cm; }
  .hint-card, .fig, .ref-card { break-inside: avoid; }
  .teacher-notes .d-tbl { break-inside: auto; page-break-inside: auto; }
  .teacher-notes .d-tbl tr { break-inside: avoid; page-break-inside: avoid; }
  .section-h { break-after: avoid; }
  /* 列數多的表放寬為可跨頁、每列不可切開（L8 實測：整張 avoid 會推去下一頁留半頁白）；
     提示卡與手順卡列數少，維持整張不切。 */
  .d-tbl.three-col, .d-tbl.dual-track { break-inside: auto; page-break-inside: auto; }
  .d-tbl.three-col tr, .d-tbl.dual-track tr,
  .d-tbl.step-card tr { break-inside: avoid; page-break-inside: avoid; }
  .d-tbl.step-card { break-inside: avoid; page-break-inside: avoid; }
  .dual-track td:first-child { text-align: center; }
  .dual-track svg, .cardfig svg { max-width: 100%; height: auto; }
  .cardfig { text-align: center; margin: 6px 0; }
  .cardfig svg { max-height: 5.4cm; width: auto; }
  .spec-tbl td, .spec-tbl th { text-align: center; }
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

    TRI = {"A": figs.tri_A(), "B": figs.tri_B(), "N": figs.tri_num()}
    parts.append('<div class="section-h page-break">二、六個三角比：先圈角，再標邊</div>')
    parts += ["<div>%s</div>" % _h(t) for t in RATIO_TXT]
    parts.append(_dual_html([(TRI[k], v) for k, v in RATIO_PAIRS], D5_RATIO_H))
    parts.append('<div class="hint-card">%s</div>' % _h(RATIO_NOTE))
    parts.append(_refcard_html(CARD1, figs.tri_blank()))
    parts.append('<div class="problem">%s</div>' % _h(EX_A))
    parts += ["<div>%s</div>" % _h(t) for t in A_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_A))

    parts.append('<div class="section-h page-break">'
                 '三、角超過 90° 之後：象限決定正負</div>')
    parts += ["<div>%s</div>" % _h(t) for t in QUAD_TXT]
    parts.append(_dual_html([(figs.quad_point(q), v) for q, v in QUAD_PAIRS],
                            D5_QUAD_H))
    parts.append('<div class="hint-card">%s</div>' % _h(QUAD_NOTE))
    parts.append(_refcard_html(CARD2, figs.quad_sign()))
    parts.append('<div class="problem">%s</div>' % _h(EX_B))
    parts += ["<div>%s</div>" % _h(t) for t in B_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_B))

    parts.append('<div class="section-h page-break">四、不是特殊角的角：拆開來算</div>')
    parts += ["<div>%s</div>" % _h(t) for t in SUM_TXT]
    parts.append(_refcard_html(CARD3))
    parts.append('<div>卡三配套的特殊角值表（拆角之後要代的四個值全部在這裡）：</div>')
    parts.append(_tbl_html(SPECIAL_ROWS, SPECIAL_HEAD, cls="spec-tbl"))
    parts.append(_step_html(CARD_D2))
    parts.append('<div class="problem">%s</div>' % _h(EX_C))
    parts += ["<div>%s</div>" % _h(t) for t in C_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_C))

    parts.append('<div class="section-h page-break">五、式子裡出現 2α：二倍角</div>')
    parts += ["<div>%s</div>" % _h(t) for t in DBL_TXT]
    parts.append(_refcard_html(CARD4))
    parts.append('<div class="problem">%s</div>' % _h(EX_D))
    parts += ["<div>%s</div>" % _h(t) for t in D_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_D))

    parts.append('<div class="section-h page-break">六、給值求角：通解</div>')
    parts += ["<div>%s</div>" % _h(t) for t in GEN_TXT]
    parts.append(_refcard_html(CARD5))
    parts.append('<div class="problem">%s</div>' % _h(EX_E))
    parts += ["<div>%s</div>" % _h(t) for t in E_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_E))

    parts.append('<div class="section-h page-break">'
                 '七、五張卡速查（做每一題之前掃一眼）</div>')
    parts.append('<div>先認出題目屬於哪一行，才決定翻哪一張卡。'
                 '認錯行的話，後面的計算做得再仔細都沒有用——'
                 '這一課的失分有一半在這裡。</div>')
    parts.append(_tbl_html(SUM_ROWS, SUM_HEAD))

    parts.append('<div class="section-h">八、接下來</div>')
    parts.append('<div>請拿出《第2章 L12 三角函數　課堂練習》，'
                 '並把《工具卡》剪下放在桌面。'
                 '練習A 每題下方會重印該用的那張卡的公式列（觸發條件與圖不再印）；'
                 '練習B 只告訴你翻第幾張卡；'
                 '練習C 兩者都不給，而且同一題裡要連續換兩至三張卡。</div>')

    parts.append('<div class="footer">' + _esc(FOOT) + '</div>')

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join("<tr><td>%s</td><td>%s</td></tr>" % (_esc(k), _h(v))
                 for k, v in tn_rows)
    parts.append('<div class="teacher-notes">'
                 '<div class="section-h">教師實施說明（本頁供教師參考，'
                 '列印給學生時可不印）</div>'
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
