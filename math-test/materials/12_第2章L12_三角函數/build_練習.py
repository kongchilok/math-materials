# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L12 三角函數 —— 課堂練習 ＋ 工具卡 build script

主設計 D7 提示卡，褪除分四級：
  講義＝完整卡（觸發條件＋敘述＋公式＋圖）→ A＝只重印公式列 → B＝只給卡號 → C＝移除。
輔助 D5 圖文雙軌（A 左欄圖已給、右欄留空讓學生填 → B 只給空白象限圖 → C 無圖）、
D2 手順卡（A 第 2 題旁印精簡版四個動作 → B 只寫「四步」→ C 移除）。
鷹架密度：抽離小班 (Tier 2)。

產出：練習_三角函數_抽離小班共用版.docx/.html、工具卡_三角函數.docx/.html

注意：
1. 三角函數名一律 `{fn(sin)}` 正體；平方寫 `{fn(sin)^2 α}`；
   負分數寫 `-frac(24,25)` 不寫 `frac(-24,25)`。
2. 參考答案的 steps 由迴圈自動編「　（1）（2）…」，所以 steps 字串本身
   不可以用「（1）」開頭（會印成「（1）（1）」，L10 踩過）——小問一律寫「小問 (a)：」。
3. QB-20：HTML 端一定要保留 `@page { margin-bottom: 1.5cm; }` 的覆寫，
   否則內文最後一行會被頁尾白底蓋住（L12 實測定案的解法，比逐頁調行數可靠）。
4. 不要用 `**markdown 粗體**`，docx 端會原樣印出星號。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omml_docx import *                      # noqa: E402,F403
import design_svg as ds                      # noqa: E402
import figs                                  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_三角函數_抽離小班共用版"
CARDF = "工具卡_三角函數"
UNIT = "第2章 中學基礎數學應用．L12 三角函數"
FOOT = "高三數學．" + UNIT

# ================================================================ 引導語
HINT_TOP = ("這一課的計算都不長，錯的地方幾乎全部是「揀錯了公式」或者「正負寫反」。"
            "所以每一題動筆之前先做同一件事：認出這題屬於哪一類，翻出對應的提示卡，"
            "看一眼卡上的第一行「什麼時候翻我」確認自己沒有揀錯，才開始算。"
            "本份練習的提示會一節比一節少："
            "練習A 每題下方重印該用的那張卡的公式列；"
            "練習B 只告訴你翻第幾張卡；"
            "練習C 兩者都不給，而且同一題裡要連續換兩至三張卡。")

A_LEAD = ("第 1 題左邊的圖已經畫好、數字也標好了，右邊那欄留空——"
          "把「對邊是哪一條」寫出來，再寫算式。"
          "第 2 題下方是那張手順卡的精簡版（只留四個動作，易錯點要自己回想）。")

B_LEAD = ("由這一節開始不再印公式，只給卡號，公式要自己想得起來"
          "（想不起就翻工具卡，但先自己試一次）。"
          "▍第 3 題：翻卡二。(a) 兩個條件各自列出可能的象限再取交集；"
          "(b) 先用恆等式求大小，再用象限定正負。"
          "▍第 4 題：翻卡四，四步。"
          "(a) 題目給的是 sin，缺的 cos 要自己補，補完先定象限。"
          "▍第 3 題附了一個空白象限圖：四個象限的正負由你自己標上去，不再印給你。")

C_LEAD = ("本節收起工具卡，也不再給卡號。"
          "兩題都要在同一題裡連續換兩至三張卡——"
          "先認清楚每個小問各自屬於哪一類，再逐個走完該卡的步驟。"
          "動筆之前先問自己三句：這個角是不是特殊角？"
          "式子裡有沒有出現 {2α}？有沒有給我象限？")

# ================================================================ 題目
STEMS = {
    1: "直角 {△ABC} 中 {∠C = 90°}，{AC = 6}、{BC = 8}。"
       "（1）求 {AB}。　"
       "（2）求 {fn(sin)A}、{fn(cos)A}、{fn(tan)A}。　"
       "（3）求 {fn(sin)B}，並說明它為什麼等於 {fn(cos)A}。",
    2: "（a）求 {fn(cos)75°} 的值。　"
       "（b）求 {fn(tan)15°} 的值（分母不可以留根號）。　"
       "（c）求 {fn(sin)72° fn(cos)42° - fn(cos)72° fn(sin)42°} 的值。",
    3: "（a）已知 {fn(sin)θ > 0} 且 {fn(tan)θ < 0}，θ 在第幾象限？　"
       "（b）已知 {fn(cos)θ = -frac(3,5)}，{θ ∈ (frac(π,2), π)}，"
       "求 {fn(sin)θ} 與 {fn(tan)θ}。",
    4: "（a）已知 {fn(sin)θ = -frac(4,5)}，且 θ 在第三象限，求 {fn(sin)2θ}。　"
       "（b）若 {fn(sin)α + fn(cos)α = 1}，求 {fn(sin)2α}。",
    5: "（a）求 {fn(sin)105°} 與 {fn(cos)105°} 的值。　"
       "（b）利用 (a) 的兩個結果求 {fn(sin)210°}，"
       "並用另一個方法驗證你的答案。",
    6: "（a）已知 {fn(cos)α = frac(3,5)}，且 α 在第四象限，"
       "求 {fn(sin)2α}、{fn(cos)2α} 與 {fn(tan)2α}。　"
       "（b）求方程 {fn(sin)x = -frac(1,2)} 的通解。",
}

# ---------------------------------------------------------------- D7 公式列（練習A）
FORMULA_A = {
    1: "▍第 1 題用卡一・六個三角比　"
       "{fn(sin)A = frac(對邊,斜邊)}　{fn(cos)A = frac(鄰邊,斜邊)}　"
       "{fn(tan)A = frac(對邊,鄰邊)}　（畢氏定理：{a^2 + b^2 = c^2}）",
    2: "▍第 2 題用卡三・和角差角　"
       "{fn(sin)(α+-β) = fn(sin)α fn(cos)β +- fn(cos)α fn(sin)β}　"
       "{fn(cos)(α+-β) = fn(cos)α fn(cos)β -+ fn(sin)α fn(sin)β}　"
       "{fn(tan)(α+-β) = frac(fn(tan)α +- fn(tan)β,1 -+ fn(tan)α fn(tan)β)}　"
       "特殊角：{fn(sin)30° = frac(1,2)}、{fn(cos)30° = frac(sqrt(3),2)}、"
       "{fn(tan)30° = frac(sqrt(3),3)}、{fn(sin)45° = fn(cos)45° = frac(sqrt(2),2)}、"
       "{fn(tan)45° = 1}、{fn(sin)60° = frac(sqrt(3),2)}、{fn(cos)60° = frac(1,2)}、"
       "{fn(tan)60° = sqrt(3)}",
}

# ---------------------------------------------------------------- D5 半成品（練習A 第 1 題）
D5_A_H = ("圖已經給你（左欄）", "把右欄填完")
# 空格一律用全形底線並放在 {} 之外——`_` 在數學標記裡是下標符號，
# 寫成 `{frac(__,__)}` 會直接拋 MathParseError（本課實測踩過）。
D5_A_PAIRS = [
    ("A", "看 ∠A：對邊是 ＿＿＿、鄰邊是 ＿＿＿、斜邊是 ＿＿＿。"
          "先求斜邊：{AB = sqrt(AC^2 + BC^2)} ＝ ＿＿＿。"
          "然後 {fn(sin)A} ＝ ＿＿＿、{fn(cos)A} ＝ ＿＿＿、"
          "{fn(tan)A} ＝ ＿＿＿（三個都要約到最簡）。"),
    ("B", "改看 ∠B：對邊是 ＿＿＿、鄰邊是 ＿＿＿、斜邊是 ＿＿＿。"
          "{fn(sin)B} ＝ ＿＿＿。"
          "最後一句：{fn(sin)B} 之所以等於 {fn(cos)A}，"
          "是因為 ＿＿＿＿＿＿＿＿＿＿。"),
]

# ---------------------------------------------------------------- D2 精簡卡（練習A 第 2 題）
CARD_A2 = dict(
    title="▍第 2 題的手順卡（精簡版：只留動作）",
    steps=[("把角拆成兩個特殊角的和或差", None),
           ("翻卡三，揀出對應那一條公式", None),
           ("四個特殊角的值逐個代進去", None),
           ("通分、化簡；tan 的結果要有理化", None)])

HINT_A = {
    1: "▍(3) 不要重新由頭數一次。先看 ∠B 的對邊是哪一條，"
       "再對照 ∠A 的鄰邊是哪一條——你會發現是同一條。",
    2: "▍(a) {75° = 45° + 30°}（或 {30° + 45°}，兩種拆法答案一樣）。"
       "▍(b) {15° = 45° - 30°}；算到 {frac(sqrt(3) - 1,sqrt(3) + 1)} 之後還未完，"
       "要上下同乘 {sqrt(3) - 1} 把分母的根號消掉。"
       "▍(c) 這一題是反方向用：先認出式子的形狀對應哪一條公式，"
       "再讀出括號裡應該是加還是減。",
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
LINES = {1: 5, 2: 13, 3: 7, 4: 6, 5: 10, 6: 10}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（1）{AB = 10}　（2）{fn(sin)A = frac(4,5)}、{fn(cos)A = frac(3,5)}、"
            "{fn(tan)A = frac(4,3)}　（3）{fn(sin)B = frac(3,5)}，"
            "因為 ∠B 的對邊就是 ∠A 的鄰邊（兩銳角互餘）",
        kp="直角三角形的六個三角比（卡一）。考點是「對邊／鄰邊由你看的角決定」，"
           "同一個三角形換一個角，三條邊的身份就對調。",
        fm="{fn(sin)A = frac(對邊,斜邊)}、{fn(cos)A = frac(鄰邊,斜邊)}、"
           "{fn(tan)A = frac(對邊,鄰邊)}；畢氏定理 {a^2 + b^2 = c^2}",
        steps=[
            "小問 (1)：{∠C = 90°} 所以 AB 是斜邊。"
            "{AB = sqrt(AC^2 + BC^2) = sqrt(6^2 + 8^2) = sqrt(36 + 64) = sqrt(100) = 10}。"
            "（這是 6-8-10 三角形，即 3-4-5 的兩倍。）",
            "小問 (2)：圈出 ∠A。∠A 在左上角，它對面那一條是底邊 {BC = 8}（對邊）；"
            "夾着它的另一條非斜邊是 {AC = 6}（鄰邊）；斜邊是 {AB = 10}。",
            "小問 (2)：代進卡一。"
            "{fn(sin)A = frac(8,10) = frac(4,5)}、"
            "{fn(cos)A = frac(6,10) = frac(3,5)}、"
            "{fn(tan)A = frac(8,6) = frac(4,3)}。三個都要約到最簡。",
            "小問 (2) 檢查："
            "{fn(sin)^2 A + fn(cos)^2 A = frac(16,25) + frac(9,25) = frac(25,25) = 1} ✔",
            "小問 (3)：改圈 ∠B。∠B 在右下角，它對面那一條是 {AC = 6}（對邊），"
            "斜邊仍然是 10，所以 {fn(sin)B = frac(6,10) = frac(3,5)}。",
            "小問 (3)：{fn(sin)B = fn(cos)A} 的理由——"
            "∠B 的對邊（AC）剛好就是 ∠A 的鄰邊（AC），是同一條邊；"
            "而兩者的斜邊也是同一條。兩個分數的分子分母完全相同，所以相等。"
            "背後的原因是 {∠A + ∠B = 90°}，兩個銳角互餘。"],
        pit="①把 {fn(sin)B} 寫成 {frac(8,10)}：那是把「B 旁邊那條邊」當成對邊。"
            "對邊是「角對面那一條」，∠B 對面的是 AC ＝ 6。"
            "②忘記約簡，答 {frac(8,10)}——不算錯但會被扣分，養成算完就約的習慣。"
            "③(3) 只答「因為互餘」而沒有指出「是同一條邊」："
            "本題問的是為什麼，要講得出哪兩條邊重合。"),
    2: dict(
        ans="（a）{frac(sqrt(6) - sqrt(2),4)}　（b）{2 - sqrt(3)}　（c）{frac(1,2)}",
        kp="和角差角公式（卡三）＋手順卡四步。"
           "(a)(b) 是正方向用（拆角再代值），(c) 是反方向用（由形狀認出公式）。",
        fm="{fn(cos)(α+β) = fn(cos)α fn(cos)β - fn(sin)α fn(sin)β}；"
           "{fn(tan)(α-β) = frac(fn(tan)α - fn(tan)β,1 + fn(tan)α fn(tan)β)}；"
           "{fn(sin)(α-β) = fn(sin)α fn(cos)β - fn(cos)α fn(sin)β}",
        steps=[
            "小問 (a) 第一步：{75° = 45° + 30°}。第二步：求 cos、而且是和，"
            "所以中間用減號（括號加、中間減）。",
            "小問 (a) 第三、四步："
            "{fn(cos)75° = fn(cos)45° fn(cos)30° - fn(sin)45° fn(sin)30° "
            "= frac(sqrt(2),2) * frac(sqrt(3),2) - frac(sqrt(2),2) * frac(1,2) "
            "= frac(sqrt(6),4) - frac(sqrt(2),4) = frac(sqrt(6) - sqrt(2),4)}。",
            "小問 (a) 檢查：{≈ frac(2.449 - 1.414,4) ≈ 0.259}。"
            "75° 是第一象限的角，cos 應該是正而且小於 1 ✔",
            "小問 (b) 第一、二步：{15° = 45° - 30°}，求 tan、而且是差，"
            "所以分子用減、分母用加。",
            "小問 (b) 第三步：{fn(tan)15° = frac(fn(tan)45° - fn(tan)30°,"
            "1 + fn(tan)45° fn(tan)30°) = frac(1 - frac(sqrt(3),3),"
            "1 + 1 * frac(sqrt(3),3))}。"
            "上下同乘 3 清走小分數：{= frac(3 - sqrt(3),3 + sqrt(3))}。",
            "小問 (b) 第四步（有理化）：上下同乘 {3 - sqrt(3)}——"
            "{= frac((3 - sqrt(3))^2,(3 + sqrt(3))(3 - sqrt(3))) "
            "= frac(9 - 6sqrt(3) + 3,9 - 3) = frac(12 - 6sqrt(3),6) = 2 - sqrt(3)}。",
            "小問 (b) 檢查：{sqrt(3) ≈ 1.732}，所以答案 {≈ 0.268}。"
            "15° 很小，tan 應該接近 0 而且是正數 ✔",
            "小問 (c)：式子的形狀是「{fn(sin)A fn(cos)B - fn(cos)A fn(sin)B}」，"
            "對照卡三就是 {fn(sin)(A - B)}（中間減 → 括號減）。"
            "所以 {= fn(sin)(72° - 42°) = fn(sin)30° = frac(1,2)}。"],
        pit="①(a) 把中間的符號寫成加號：那是 sin 的規則，cos 相反。"
            "寫錯的話答案變成 {frac(sqrt(6) + sqrt(2),4) ≈ 0.966}，"
            "而 {fn(cos)75°} 明明應該很接近 0（75° 接近 90°）。"
            "②(b) 算到 {frac(3 - sqrt(3),3 + sqrt(3))} 就交卷——"
            "分母有根號就是未完成，一定要有理化。"
            "③(c) 誤以為要逐個查 72°、42° 的值：這一題根本不需要，"
            "而且表上也沒有這兩個角。見到「兩個乘積相加減」就先想反方向。"
            "④(c) 把括號裡寫成 {72° + 42°}：中間是減號，括號裡就是減號（sin 的規則是一樣）。"),
    3: dict(
        ans="（a）第二象限　（b）{fn(sin)θ = frac(4,5)}、{fn(tan)θ = -frac(4,3)}",
        kp="象限符號盤（卡二）。(a) 是「兩個條件取交集」，"
           "(b) 是「先求大小、再由象限定正負」——本課最常漏的就是後面那一步。",
        fm="一全正、二 sin 正、三 tan 正、四 cos 正；"
           "{fn(sin)^2 θ + fn(cos)^2 θ = 1}；{fn(tan)θ = frac(fn(sin)θ,fn(cos)θ)}",
        steps=[
            "小問 (a)：{fn(sin)θ > 0} → 翻卡二，sin 是正的象限是第一與第二。",
            "小問 (a)：{fn(tan)θ < 0} → tan 是正的象限是第一與第三，"
            "所以 tan 是負的象限是第二與第四。",
            "小問 (a)：取交集——「一或二」與「二或四」共同的只有第二象限。",
            "小問 (b) 第一步（求大小）："
            "{fn(sin)^2 θ = 1 - fn(cos)^2 θ = 1 - (-frac(3,5))^2 "
            "= 1 - frac(9,25) = frac(16,25)}，所以大小是 {frac(4,5)}。",
            "小問 (b) 第二步（定正負）：{θ ∈ (frac(π,2), π)} 就是第二象限，"
            "卡二說第二象限只有 sin 是正，所以 {fn(sin)θ = frac(4,5)}（取正）。",
            "小問 (b) 第三步："
            "{fn(tan)θ = frac(fn(sin)θ,fn(cos)θ) = frac(4,5) ÷ (-frac(3,5)) "
            "= frac(4,5) * (-frac(5,3)) = -frac(4,3)}。",
            "小問 (b) 檢查：算出 sin 正、cos 負、tan 負，"
            "完全對得上卡二的「第二象限只有 sin 正」✔"],
        pit="①(a) 只看其中一個條件就作答（答「一或二」）："
            "題目給了兩個條件就一定要取交集，這是本題的全部考點。"
            "②(b) 開方之後直接寫 {fn(sin)θ = ±frac(4,5)} 交卷："
            "題目已經給了象限，答案是唯一的，不可以留 {±}。"
            "③(b) 忘記定正負、寫成 {-frac(4,5)}：大小對、正負反，"
            "而且會連累 tan 也錯。對策是算出大小之後先在旁邊寫「第二象限」四個字。"),
    4: dict(
        ans="（a）{fn(sin)2θ = frac(24,25)}　（b）{fn(sin)2α = 0}",
        kp="二倍角（卡四）。(a) 要先補 cos 並用卡二定正負；"
           "(b) 考的是認不認得 {(fn(sin)α + fn(cos)α)^2 = 1 + fn(sin)2α} 這個變形。",
        fm="{fn(sin)2θ = 2 fn(sin)θ fn(cos)θ}；"
           "{(fn(sin)α + fn(cos)α)^2 = 1 + fn(sin)2α}；"
           "{fn(sin)^2 θ + fn(cos)^2 θ = 1}",
        steps=[
            "小問 (a) 第一步：{fn(sin)2θ} 需要 {fn(cos)θ}，題目沒有給，要自己補。"
            "{fn(cos)^2 θ = 1 - (-frac(4,5))^2 = 1 - frac(16,25) = frac(9,25)}，"
            "大小是 {frac(3,5)}。",
            "小問 (a) 第二步（定正負）：θ 在第三象限，卡二說第三象限只有 tan 正，"
            "所以 cos 是負的：{fn(cos)θ = -frac(3,5)}。",
            "小問 (a) 第三步："
            "{fn(sin)2θ = 2 * (-frac(4,5)) * (-frac(3,5)) = frac(24,25)}。",
            "小問 (a) 檢查：兩個負數相乘得正，所以 {fn(sin)2θ} 是正數 ✔ "
            "這一題的答案是正的，不要因為題目給的 sin 是負數就以為答案一定是負數。",
            "小問 (b)：認出這是那個變形。兩邊平方："
            "{(fn(sin)α + fn(cos)α)^2 = 1^2 = 1}。",
            "小問 (b)：而左邊展開 "
            "{= fn(sin)^2 α + 2 fn(sin)α fn(cos)α + fn(cos)^2 α = 1 + fn(sin)2α}。"
            "所以 {1 + fn(sin)2α = 1}，得 {fn(sin)2α = 0}。"],
        pit="①(a) 跳過第二步、直接用 {fn(cos)θ = frac(3,5)}："
            "答案會變成 {-frac(24,25)}，大小對、正負完全相反。"
            "凡是「由一個三角值求另一個」，開方之後立刻寫下象限。"
            "②(a) 以為「sin 是負 → 答案是負」：{fn(sin)2θ} 是 {2θ} 這個角的 sin，"
            "跟 θ 的正負沒有直接關係。"
            "③(b) 不認得變形，去解聯立方程求 sin 與 cos 各自的值："
            "做得出但長很多倍，而且會多出一組要排除的解。"),
    5: dict(
        ans="（a）{fn(sin)105° = frac(sqrt(6) + sqrt(2),4)}、"
            "{fn(cos)105° = frac(sqrt(2) - sqrt(6),4)}　"
            "（b）{fn(sin)210° = -frac(1,2)}",
        kp="同一題內換兩張卡：(a) 用卡三（和角差角）求出兩個值，"
           "(b) 用卡四（二倍角）把它們接起來——{210° = 2 * 105°}。",
        fm="{fn(sin)(α+β) = fn(sin)α fn(cos)β + fn(cos)α fn(sin)β}；"
           "{fn(cos)(α+β) = fn(cos)α fn(cos)β - fn(sin)α fn(sin)β}；"
           "{fn(sin)2α = 2 fn(sin)α fn(cos)α}",
        steps=[
            "小問 (a)：{105° = 60° + 45°}。"
            "{fn(sin)105° = fn(sin)60° fn(cos)45° + fn(cos)60° fn(sin)45° "
            "= frac(sqrt(3),2) * frac(sqrt(2),2) + frac(1,2) * frac(sqrt(2),2) "
            "= frac(sqrt(6),4) + frac(sqrt(2),4) = frac(sqrt(6) + sqrt(2),4)}。",
            "小問 (a)：{fn(cos)105° = fn(cos)60° fn(cos)45° - fn(sin)60° fn(sin)45° "
            "= frac(1,2) * frac(sqrt(2),2) - frac(sqrt(3),2) * frac(sqrt(2),2) "
            "= frac(sqrt(2),4) - frac(sqrt(6),4) = frac(sqrt(2) - sqrt(6),4)}。"
            "留意 cos 中間是減號（括號加、中間減）。",
            "小問 (a) 檢查：105° 在第二象限 → sin 應為正、cos 應為負。"
            "{sqrt(6) > sqrt(2)} 所以 {fn(sin)105°} 正、{fn(cos)105°} 負 ✔",
            "小問 (b)：認出 {210° = 2 * 105°}，所以翻卡四："
            "{fn(sin)210° = 2 fn(sin)105° fn(cos)105°}。",
            "小問 (b)：代入 (a) 的兩個結果——"
            "{= 2 * frac(sqrt(6) + sqrt(2),4) * frac(sqrt(2) - sqrt(6),4) "
            "= frac(2(sqrt(6) + sqrt(2))(sqrt(2) - sqrt(6)),16)}。",
            "小問 (b)：分子的乘積用平方差來算會更快——"
            "{(sqrt(6) + sqrt(2))(sqrt(2) - sqrt(6)) = -(sqrt(6) + sqrt(2))(sqrt(6) - sqrt(2)) "
            "= -(6 - 2) = -4}。"
            "所以 {fn(sin)210° = frac(2 * (-4),16) = -frac(8,16) = -frac(1,2)}。",
            "小問 (b) 另一個驗證方法：{210° = 180° + 30°} 在第三象限，"
            "卡二說第三象限的 sin 是負的，而它與 30° 的參考角相同，"
            "所以 {fn(sin)210° = -fn(sin)30° = -frac(1,2)} ✔ 兩條路相同。"],
        pit="①(b) 看不出 {210° = 2 * 105°}，於是重新拆 {210° = 180° + 30°} 從頭算："
            "答案一樣對，但題目明講「利用 (a) 的兩個結果」，"
            "考的就是認不認得二倍角這一步。"
            "②(a) cos 的中間符號寫成加號 → {fn(cos)105°} 變成正數，"
            "與「105° 在第二象限」矛盾。做完 cos 順手用卡二檢查正負。"
            "③(b) 分子硬乘四項而漏了其中一項："
            "用平方差 {(x + y)(x - y) = x^2 - y^2} 只需兩步，"
            "但要先把 {(sqrt(2) - sqrt(6))} 提一個負號變成 {-(sqrt(6) - sqrt(2))}。"),
    6: dict(
        ans="（a）{fn(sin)2α = -frac(24,25)}、{fn(cos)2α = -frac(7,25)}、"
            "{fn(tan)2α = frac(24,7)}　"
            "（b）{x = nπ + (-1)^(n+1) frac(π,6)}（n 為任意整數）",
        kp="同一題內換三張卡：(a) 卡二定 {fn(sin)α} 的正負 → 卡四求三個二倍角值；"
           "(b) 卡五求通解。(a) 最後還要留意 {2α} 落在哪個象限來覆核。",
        fm="{fn(sin)2α = 2 fn(sin)α fn(cos)α}；{fn(cos)2α = 2 fn(cos)^2 α - 1}；"
           "{fn(tan)2α = frac(fn(sin)2α,fn(cos)2α)}；"
           "{fn(sin)x = k → x = nπ + (-1)^n fn(arcsin)k}",
        steps=[
            "小問 (a) 第一步：{fn(sin)^2 α = 1 - (frac(3,5))^2 = 1 - frac(9,25) "
            "= frac(16,25)}，大小是 {frac(4,5)}。",
            "小問 (a) 第二步（卡二）：α 在第四象限，只有 cos 是正，"
            "所以 sin 是負：{fn(sin)α = -frac(4,5)}。",
            "小問 (a) 第三步："
            "{fn(sin)2α = 2 * (-frac(4,5)) * frac(3,5) = -frac(24,25)}。",
            "小問 (a) 第四步：{fn(cos)2α} 揀「給 cos 用」那一條，"
            "就完全不必用到剛才那個負數——"
            "{fn(cos)2α = 2 fn(cos)^2 α - 1 = 2 * frac(9,25) - 1 "
            "= frac(18,25) - frac(25,25) = -frac(7,25)}。",
            "小問 (a) 第五步："
            "{fn(tan)2α = frac(fn(sin)2α,fn(cos)2α) = (-frac(24,25)) ÷ (-frac(7,25)) "
            "= frac(24,7)}。",
            "小問 (a) 檢查：{fn(sin)2α} 負、{fn(cos)2α} 負 → {2α} 在第三象限；"
            "卡二說第三象限的 tan 是正 —— 算出來的 {frac(24,7)} 確實是正數 ✔",
            "小問 (b) 第一步：是 sin，翻卡五的第一條 "
            "{x = nπ + (-1)^n fn(arcsin)k}。",
            "小問 (b) 第二步：{fn(arcsin)(-frac(1,2)) = -frac(π,6)}"
            "（因為 {fn(sin)frac(π,6) = frac(1,2)}，取負角）。"
            "代入：{x = nπ + (-1)^n * (-frac(π,6))}。",
            "小問 (b) 第三步：把負號併進指數——{(-1)^n * (-1) = (-1)^(n+1)}，"
            "所以 {x = nπ + (-1)^(n+1) frac(π,6)}。",
            "小問 (b) 檢查：取 {n = 1} 得 {x = π + frac(π,6) = frac(7π,6)}，即 210°；"
            "{fn(sin)210° = -frac(1,2)} ✔ 取 {n = 0} 得 {x = -frac(π,6)}，"
            "即 −30°，{fn(sin)(-30°) = -frac(1,2)} ✔"],
        pit="①(a) 忘記第二步、把 sin 寫成正：三個答案的正負會全部連鎖出錯。"
            "②(a) {fn(cos)2α} 用 {fn(cos)^2 α - fn(sin)^2 α} 也對，但要先處理那個負數；"
            "揀「給 cos 用」那一條可以完全避開，這是揀公式的價值。"
            "③(a) 最後不做象限覆核：本題的三個答案彼此有關係，"
            "sin 負、cos 負卻算出 tan 負的話，一定是中間某一步錯了。"
            "④(b) 停在 {x = nπ + (-1)^n(-frac(π,6))} 就交卷："
            "答案本身沒有錯，但選擇題的選項多數已經把負號併好，"
            "找不到自己的形狀時要先搬負號再看一次。"
            "⑤(b) 誤用 cos 的公式寫成 {2nπ ±}：sin 配 {(-1)^n}、cos 才配 {±}。",
        ),
}

# ================================================================ 工具卡
# 前五張＝講義那五張 D7 提示卡的桌面版；第六張是 D2 手順卡。
# 卡片不用高構件（分數會疊高行距，六張卡就入不到一頁，L4 實測），
# 但一定要留幾條 {} 標記的短式，否則 m:oMath ＝ 0 會 QB-2 FAIL（L8 實測）。
TC_TEXT = [
    ("▍卡一・六個三角比", "給了直角三角形或兩條邊，問 sin／cos／tan。",
     ["① 先圈出題目問的是哪一個角",
      "② 標「對邊／鄰邊／斜邊」：斜邊永遠是直角對面",
      "③ {fn(sin) = frac(對,斜)}　{fn(cos) = frac(鄰,斜)}　{fn(tan) = frac(對,鄰)}",
      "④ 倒數：csc 配 sin、sec 配 cos、cot 配 tan",
      "※ 換一個角就要重新標邊；缺邊用 {a^2 + b^2 = c^2} 補"]),
    ("▍卡二・象限符號盤", "只給一個三角值（尤其負值），或問「在第幾象限」。",
     ["① 一：全部正",
      "② 二：只有 sin 正",
      "③ 三：只有 tan 正",
      "④ 四：只有 cos 正",
      "※ 開方求出大小之後，先寫下象限再定正負",
      "※ 給兩個條件 → 各自列象限再取交集"]),
    ("▍卡三・和角差角", "要求 15°、75°、105°，或見到兩個乘積相加減。",
     ["① {fn(sin)(α+-β) = fn(sin)α fn(cos)β +- fn(cos)α fn(sin)β}",
      "② {fn(cos)(α+-β) = fn(cos)α fn(cos)β -+ fn(sin)α fn(sin)β}",
      "③ {fn(tan)(α+-β) = frac(fn(tan)α +- fn(tan)β,1 -+ fn(tan)α fn(tan)β)}",
      "④ 特殊角 30°：{frac(1,2)}、{frac(sqrt(3),2)}、{frac(sqrt(3),3)}",
      "⑤ 45°：{frac(sqrt(2),2)}、{frac(sqrt(2),2)}、1；60°：{frac(sqrt(3),2)}、"
      "{frac(1,2)}、{sqrt(3)}",
      "※ cos 的中間符號跟括號裡相反；sin 的一樣"]),
    ("▍卡四・二倍角", "式子裡有 {2α}，或給了 {fn(sin)α + fn(cos)α}。",
     ["① {fn(sin)2α = 2 fn(sin)α fn(cos)α}",
      "② {fn(cos)2α = fn(cos)^2 α - fn(sin)^2 α}",
      "③ 給 sin 就用 {1 - 2 fn(sin)^2 α}",
      "④ 給 cos 就用 {2 fn(cos)^2 α - 1}",
      "⑤ {(fn(sin)α + fn(cos)α)^2 = 1 + fn(sin)2α}",
      "※ 算完用卡二覆核 {2α} 落在哪個象限"]),
    ("▍卡五・通解", "題目出現「通解」，或選項裡有 n。",
     ["① {fn(sin)x = k → x = nπ + (-1)^n fn(arcsin)k}",
      "② {fn(cos)x = k → x = 2nπ +- fn(arccos)k}",
      "③ {fn(tan)x = k → x = nπ + fn(arctan)k}",
      "④ arc 值用卡三的特殊角表反過來查",
      "※ k 是負數時，負號可以併進 {(-1)^n} 變成 {(-1)^(n+1)}"]),
    ("▍手順卡・求非特殊角的三角值", "要求 15°、75°、105° 這些角的值。",
     ["① 拆成兩個特殊角的和或差",
      "② 翻卡三，揀出對應那一條公式",
      "③ 四個特殊角的值逐個代進去",
      "④ 通分、化簡；tan 要有理化",
      "※ 第三步一次要代四個值，漏一個是最常見的失分",
      "※ 分母留了根號就是未做完"]),
]


# ================================================================ docx
def build_practice_docx():
    figdir = os.path.join(HERE, "_figtmp")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    def img(svg, name, cm):
        png = os.path.join(figdir, name + ".png")
        ds.svg_to_png(svg, png, scale=3)
        return image_para(png, width_cm=cm)

    TRI = {"A": figs.tri_qA(), "B": figs.tri_qB()}

    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para(A_LEAD))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        if n == 1:
            P.append(dual_track_table(
                [(img(TRI[k], "pt" + k, 5.6), v) for k, v in D5_A_PAIRS],
                media=MEDIA, headers=D5_A_H))
        else:
            P.append(step_card(CARD_A2["title"], CARD_A2["steps"], compact=True))
        P.append(shaded_box(FORMULA_A[n]))
        P.append(shaded_box(HINT_A[n]))
        P += write_lines(LINES[n])
        P.append(blank())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(shaded_box(B_LEAD))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        if n == 3:
            P.append(para("（下圖是空白的象限圖，四個象限哪幾個三角函數是正，"
                          "自己標上去再作答。）"))
            P.append(img(figs.quad_blank(), "pq", 5.4))
        P += write_lines(LINES[n])
        P.append(blank())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para(C_LEAD))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
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

    return build_docx(P, os.path.join(HERE, BASE + ".docx"),
                      footer_text=FOOT, media=MEDIA)


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in TC_TEXT:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        c += [para(t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=4000))
    return build_docx(P, os.path.join(HERE, CARDF + ".docx"), footer_text=FOOT)


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
    body = re.sub(r"[\u4e00-\u9fff]+", lambda x: r"\text{%s}" % x.group(0), body)
    return r"\(%s\)" % body


def _h(s):
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


def _step_html(card):
    rows = ['<tr><th colspan="2">%s</th></tr>' % _h(card["title"])]
    for i, (act, _p) in enumerate(card["steps"], 1):
        rows.append('<tr><td colspan="2">%d. %s</td></tr>' % (i, _h(act)))
    return '<table class="d-tbl step-card">%s</table>' % "".join(rows)


def _dual_html(pairs, headers):
    def side(x):
        return x if x.lstrip().startswith("<svg") else _h(x)
    head = ("<thead><tr><th>%s</th><th>%s</th></tr></thead>"
            % (_h(headers[0]), _h(headers[1])))
    body = "".join("<tr><td>%s</td><td>%s</td></tr>" % (side(l), side(r))
                   for l, r in pairs)
    return '<table class="d-tbl dual-track">%s<tbody>%s</tbody></table>' % (head, body)


_EXTRA_CSS = """
  /* QB-20：範本的頁尾用固定定位＋白底，內文流到頁底會被它蓋住。
     把 @page 的下邊界撐大，內文區就會提早結束，頁尾自然落在內文之下。
     （L12 實測定案；比逐頁調行數可靠，而且不影響 QB-15c。） */
  @page { margin-bottom: 1.5cm; }
  .hint-card, .fig, .selfcheck { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .d-tbl.dual-track { break-inside: auto; page-break-inside: auto; }
  .d-tbl.dual-track tr,
  .d-tbl.step-card tr { break-inside: avoid; page-break-inside: avoid; }
  .d-tbl.step-card { break-inside: avoid; page-break-inside: avoid; }
  .dual-track td:first-child { text-align: center; }
  .dual-track svg, .fig svg { max-width: 100%; height: auto; }
"""


def _head(tpl, title, extra_css):
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", title)
    return head.replace("</head>", "<style>\n%s\n</style>\n</head>" % extra_css)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = _head(tpl, "練習：" + UNIT, _EXTRA_CSS)

    TRI = {"A": figs.tri_qA(), "B": figs.tri_qB()}
    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂練習</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')
    parts.append('<div class="hint-card">%s</div>' % _h(HINT_TOP))

    parts.append('<div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>')
    parts.append('<div>%s</div>' % _h(A_LEAD))
    # 題幹自己一個 .problem 框，鷹架與作答線放在框外——
    # 全部塞進同一個 break-inside:avoid 的框裡，一題就會獨佔一頁、下面留 1/3 白
    # （本課實測；docx 版本身就是這個平鋪結構，兩版因此也對得上）
    for n in A_ITEMS:
        inner = (_dual_html([(TRI[k], v) for k, v in D5_A_PAIRS], D5_A_H)
                 if n == 1 else _step_html(CARD_A2))
        parts.append('<div class="problem">%d．%s</div>%s'
                     '<div class="hint-card">%s</div>'
                     '<div class="hint-card">%s</div>%s'
                     % (n, _h(STEMS[n]), inner, _h(FORMULA_A[n]),
                        _h(HINT_A[n]), _lines(LINES[n])))

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div class="hint-card">%s</div>' % _h(B_LEAD))
    for n in B_ITEMS:
        extra = ('<div>（下圖是空白的象限圖，四個象限哪幾個三角函數是正，'
                 '自己標上去再作答。）</div><div class="fig">%s</div>'
                 % figs.quad_blank()) if n == 3 else ""
        parts.append('<div class="problem">%d．%s</div>%s%s'
                     % (n, _h(STEMS[n]), extra, _lines(LINES[n])))

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>%s</div>' % _h(C_LEAD))
    for n in C_ITEMS:
        parts.append('<div class="problem">%d．%s</div>%s'
                     % (n, _h(STEMS[n]), _lines(LINES[n])))

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


def build_toolcard_html():
    """工具卡的 HTML 版：版面對齊 docx 的 2 欄 × 3 列虛線裁切格。"""
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = _head(tpl, "工具卡：" + UNIT, """
  @page { margin-bottom: 1.5cm; }
  .tc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin-top: 8px; }
  .tc { border: 1px dashed #444; padding: 10px 12px; min-height: 6.4cm;
        break-inside: avoid; page-break-inside: avoid; }
  .tc .t { font-weight: 700; font-size: 14pt; }
  .tc .g { font-size: 10.5pt; color: #333; margin: 2px 0 6px; }
  .tc .i { font-size: 10.5pt; line-height: 1.5; }
""")
    cards = "".join(
        '<div class="tc"><div class="t">%s</div><div class="g">%s</div>%s</div>'
        % (_esc(title), _h(trig),
           "".join('<div class="i">%s</div>' % _h(t) for t in items))
        for title, trig, items in TC_TEXT)
    parts = ['<div class="masthead"><span>科目：高三數學</span><span>單元：'
             + _esc(UNIT)
             + '</span><span>類型：工具卡（剪下沿虛線，護貝後放桌面）</span></div>',
             '<div class="tc-grid">%s</div>' % cards,
             '<div class="footer">' + _esc(FOOT) + '</div>']
    body = ("\n<body>\n<div class=\"page\">\n\n" + "\n\n".join(parts)
            + "\n\n</div>\n</body>\n</html>\n")
    path = os.path.join(HERE, CARDF + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_practice_docx())
    print(build_toolcard_docx())
    print(build_practice_html())
    print(build_toolcard_html())
