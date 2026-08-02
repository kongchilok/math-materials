# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L13 數列與級數 —— 課堂練習 ＋ 工具卡 build script

主設計 D2 手順卡，褪除照研究原文的四級：
  講義＝完整卡（動作＋※易錯點）→ A＝精簡卡（只留動作）→ B＝只留步驟數量與卡號 → C＝移除。
輔助 D13 弗雷爾（A 給只填了定義與公式的半成品卡，例／非例由學生補 →
  B 只留一句「先判斷是等差還是等比」→ C 不提）、
D12 自我核對（A 完整四項 → B 兩項 → C 一句話；工具卡第六張是本體）。
鷹架密度：抽離小班 (Tier 2)。

產出：練習_數列與級數_抽離小班共用版.docx/.html、工具卡_數列與級數.docx/.html

注意：
1. 下標寫 `{a_n}`、`{a_1}`；`_` 之後一定要有內容，空格填充要用全形 ＿ 並放在 {} 之外
   （L12 實測：`{frac(__,__)}` 會直接拋 MathParseError）。
2. 參考答案的 steps 由迴圈自動編「　（1）（2）…」，所以 steps 字串本身
   不可以用「（1）」開頭——小問一律寫「小問 (a)：」。
3. QB-20：HTML 端一定要保留 `@page { margin-bottom: 1.5cm; }` 的覆寫。
4. 不要用 `**markdown 粗體**`，docx 端會原樣印出星號。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omml_docx import *                      # noqa: E402,F403
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH, GREY_FILL   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_數列與級數_抽離小班共用版"
CARDF = "工具卡_數列與級數"
UNIT = "第2章 中學基礎數學應用．L13 數列與級數"
FOOT = "高三數學．" + UNIT

# ================================================================ 引導語
HINT_TOP = ("這一課的計算都很短，錯的地方幾乎全部是兩個："
            "① 認錯了數列的種類（把等比題套進等差公式）；"
            "② 項數少數了一個（漏了那個「＋1」）。"
            "所以每一題動筆之前先做同一件事：拿相鄰兩項相減，"
            "再拿另外相鄰兩項相減——兩個差相同就是等差；不同就改成相除。"
            "認出種類之後才翻卡。"
            "本份練習的提示會一節比一節少："
            "練習A 每題下方重印該用的那張卡（只留動作）；"
            "練習B 只告訴你這題有幾步、翻第幾張卡；"
            "練習C 兩者都不給，而且同一題裡要換兩張卡。")

A_LEAD = ("第 1 題下方那張弗雷爾卡只填了「定義」與「公式」兩格，"
          "「是的例」與「不是的例」兩格由你自己填——"
          "可以抄講義的，也可以自己想一個。"
          "每題下方另有該用的那張手順卡的精簡版（只留動作，易錯點要自己回想）。")

B_LEAD = ("由這一節開始不再印步驟內容，只給步驟數量與卡號，"
          "卡上寫什麼要自己想得起來（想不起就翻工具卡，但先自己試一次）。"
          "▍第 3 題：先用卡一定 {d}，再用卡二（或直接把四項寫成 {a_1} 與 {d}）求 {a_1}，"
          "合共四步。"
          "▍第 4 題：屬卡三，四步；第三步（兩式相除）是本題的關鍵。"
          "※ 兩題都先做同一件事：判斷是等差還是等比。")

C_LEAD = ("本節收起工具卡，也不再給卡號。"
          "兩題都要在同一題裡連續用兩件工具——"
          "第 5 題先求項數再求和，第 6 題先證出公式再用它去計算。"
          "動筆之前先問自己三句：這是等差還是等比？"
          "項數有沒有加回那個「＋1」？指數是 {n-1} 還是 {n}？")

# ================================================================ 題目
STEMS = {
    1: "（a）數列 3, 7, 11, 15, ⋯ 是等差還是等比？"
       "公差（或公比）是多少？求它的第 20 項。　"
       "（b）數列 2, 6, 18, 54, ⋯ 是等差還是等比？求它的第 6 項。",
    2: "試求 {5 + 9 + 13 + ⋯ + 101} 的和。"
       "（先數清楚有多少項，再用求和公式。）",
    3: "有四個數成等差數列，它們的和為 52，"
       "而第四項比第一項大 18。求這四個數。",
    4: "在等比數列中，第二項和第五項分別是 1 和 {-frac(1,8)}，"
       "求它的首項與公比。",
    5: "（a）等比數列 2, 6, 18, ⋯, 1458 共有多少項？　"
       "（b）求這個數列所有項的和，並用另一個方法覆核你的答案。",
    6: "（a）試用數學歸納法證明：對所有自然數 {n}，"
       "{1 * 2 + 2 * 3 + 3 * 4 + ⋯ + n(n+1) = frac(n(n+1)(n+2),3)} 成立。　"
       "（b）利用 (a) 證出來的公式，求 {1 * 2 + 2 * 3 + ⋯ + 20 * 21} 的值。",
}

# ---------------------------------------------------------------- D13 半成品（練習A）
FR_HALF_TITLE = "▍把這張卡補完（「定義」與「公式」已經填好，下面兩格由你填）"
FR_HALF = [
    ("等差數列", "定義：每一項減去前一項，差都是同一個數（公差 {d}）。",
     "公式：{a_n = a_1 + (n-1)d}；{S_n = frac(n(a_1 + a_n),2)}",
     "是的例（自己寫一個）：", "不是的例（自己寫一個）："),
    ("等比數列", "定義：每一項除以前一項，商都是同一個數（公比 {r}）。",
     "公式：{a_n = a_1 r^(n-1)}；{S_n = frac(a_1(r^n - 1),r - 1)}",
     "是的例（自己寫一個）：", "不是的例（自己寫一個）："),
]

# ---------------------------------------------------------------- D2 精簡卡（練習A）
CARDS_A = {
    1: dict(title="▍第 1 題用卡一（等差）或卡三（等比）・精簡版",
            steps=[("先相減再相除，判斷是等差還是等比", None),
                   ("定 {a_1} 與 {d}（或 {r}）", None),
                   ("等差寫 {a_n = a_1 + (n-1)d}；等比寫 {a_n = a_1 r^(n-1)}", None),
                   ("代一個已知項回去檢查", None)]),
    2: dict(title="▍第 2 題用卡二・等差級數（精簡版）",
            steps=[("先數項數：{n = frac(末項 - 首項,d) + 1}", None),
                   ("寫出 {S_n = frac(n(a_1 + a_n),2)}", None),
                   ("代數字、計算（先算括號，再乘，最後除 2）", None),
                   ("用「平均數 × 項數」覆核", None)]),
}
HINT_A = {
    1: "▍(a) {7 - 3 = 4}、{11 - 7 = 4} → 兩個差相同。"
       "▍(b) {6 ÷ 2 = 3}、{18 ÷ 6 = 3} → 兩個商相同。"
       "▍第 20 項的指數（或係數）是 {20 - 1 = 19}，不是 20。",
    2: "▍{d = 9 - 5 = 4}，首項 5、末項 101。"
       "▍算項數時 {frac(101 - 5,4) = 24} 只是「走了多少步」，"
       "項數要再加回起點那一項。",
}

# ---------------------------------------------------------------- D12
SELF_A = ["有沒有先判斷是等差還是等比（相減之後再相除）？",
          "通項公式的指數／係數用的是 {n-1}，不是 {n}？",
          "項數有沒有加回那個「＋1」？",
          "有沒有代一個已知項回去檢查（例如代 {n = 1} 應該得回首項）？"]
SELF_B = ["第 3 題的四個數加起來是不是真的等於 52？",
          "第 4 題的公比是負數——首項算出來之後，第五項對不對得上 {-frac(1,8)}？"]
SELF_C = "做完兩題之後，拿工具卡第六張出來，四行逐行對一次再交。"

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
LINES = {1: 7, 2: 6, 3: 8, 4: 8, 5: 8, 6: 11}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）等差，{d = 4}，{a_20 = 79}　（b）等比，{r = 3}，{a_6 = 486}",
        kp="先判斷數列種類，再套對應的通項公式（卡一／卡三）。"
           "本題的考點就是「判斷」這個動作本身——兩小問的數字都很乾淨，"
           "唯一會失分的地方是套錯公式或者指數寫成 {n}。",
        fm="等差 {a_n = a_1 + (n-1)d}；等比 {a_n = a_1 r^(n-1)}",
        steps=[
            "小問 (a) 判斷：{7 - 3 = 4}、{11 - 7 = 4}、{15 - 11 = 4}，"
            "三個差都是 4 → 等差數列，{d = 4}。"
            "（覆核：相除 {frac(7,3)} 與 {frac(11,7)} 不同 → 確實不是等比。）",
            "小問 (a)：{a_1 = 3}、{d = 4}，"
            "所以 {a_20 = a_1 + 19d = 3 + 19 * 4 = 3 + 76 = 79}。"
            "※ 係數是 {20 - 1 = 19}，不是 20。",
            "小問 (a) 檢查：代 {n = 1} 得 {3 + 0 * 4 = 3} ✔ 等於首項。"
            "代 {n = 4} 得 {3 + 3 * 4 = 15} ✔ 等於題目給的第四項。",
            "小問 (b) 判斷：{6 - 2 = 4}、{18 - 6 = 12}，差不同 → 不是等差。"
            "{6 ÷ 2 = 3}、{18 ÷ 6 = 3}、{54 ÷ 18 = 3}，"
            "三個商都是 3 → 等比數列，{r = 3}。",
            "小問 (b)：{a_1 = 2}、{r = 3}，"
            "所以 {a_6 = a_1 r^5 = 2 * 3^5 = 2 * 243 = 486}。"
            "※ 指數是 {6 - 1 = 5}，不是 6。",
            "小問 (b) 檢查：逐項寫出 2、6、18、54、162、486——"
            "第 6 項確實是 486 ✔"],
        pit="①(a) 把第 20 項寫成 {3 + 20 * 4 = 83}：係數是 {n-1}。"
            "由第 1 項走到第 20 項只走了 19 步。"
            "②(b) 把第 6 項寫成 {2 * 3^6 = 1458}：同一個錯，指數應該是 5。"
            "（順帶一提 1458 正是本份練習第 5 題的末項——"
            "那一題的數列一模一樣，只是問到第 7 項。）"
            "③只相減一次就下判斷：至少要算兩個差（或兩個商）才作準，"
            "而且最好算到第三項為止。"),
    2: dict(
        ans="{S_25 = 1325}",
        kp="等差級數求和（卡二）。考點是先算對項數——本題的 25 項是全題的關鍵，"
           "數成 24 的話答案會變成 1272，而且看不出有問題。",
        fm="{n = frac(a_n - a_1,d) + 1}；{S_n = frac(n(a_1 + a_n),2)}",
        steps=[
            "第一步（數項數）：{a_1 = 5}、末項 {a_n = 101}、{d = 9 - 5 = 4}。"
            "{n = frac(101 - 5,4) + 1 = frac(96,4) + 1 = 24 + 1 = 25}。共 25 項。",
            "第二步：{S_25 = frac(25(5 + 101),2) = frac(25 * 106,2)}。",
            "第三步：先約簡——{frac(106,2) = 53}，所以 {S_25 = 25 * 53 = 1325}。"
            "（先除 2 再乘，比先算 {25 * 106 = 2650} 再除 2 少一次進位。）",
            "第四步（覆核）：平均數 ＝ {frac(5 + 101,2) = 53}，"
            "項數 25，{53 * 25 = 1325} ✔",
            "另一條路覆核：用 {S_n = frac(n[2a_1 + (n-1)d],2)} —— "
            "{frac(25[2 * 5 + 24 * 4],2) = frac(25(10 + 96),2) = frac(25 * 106,2) = 1325} ✔"],
        pit="①項數算成 24（漏了 ＋1）：答案變成 {frac(24 * 106,2) = 1272}，"
            "與正確答案只差 53，看不出有問題。"
            "對策：算完 {n} 之後用一個小例子驗一次——"
            "「5 到 9，每次加 4」是 2 項，公式給 {frac(9-5,4) + 1 = 2} ✔"
            "②把公式寫成 {frac(n(a_1 + d),2)}：括號裡是「首項加末項」，不是公差。"
            "③沒有先約簡就硬乘：{25 * 106} 心算容易錯，先把 106 除 2 得 53 再乘。"),
    3: dict(
        ans="四個數是 4、10、16、22（{a_1 = 4}、{d = 6}）",
        kp="等差數列的兩條件聯立（卡一 ＋ 卡二）。"
           "考點是「兩項相減得幾個 {d}」——第四項減第一項是 {3d} 不是 {4d}。",
        fm="{a_n = a_1 + (n-1)d}；四項之和 {= 4a_1 + 6d}",
        steps=[
            "第一步：先用「第四項比第一項大 18」。"
            "{a_4 = a_1 + 3d}、{a_1 = a_1}，"
            "相減：{a_4 - a_1 = 3d}。"
            "※ 由第 1 項走到第 4 項走了 {4 - 1 = 3} 步，所以是 {3d}。",
            "第二步：{3d = 18}，得 {d = 6}。",
            "第三步：再用「和為 52」。四項是 "
            "{a_1}、{a_1 + d}、{a_1 + 2d}、{a_1 + 3d}，"
            "加起來 {= 4a_1 + (0+1+2+3)d = 4a_1 + 6d}。"
            "代入 {d = 6}：{4a_1 + 36 = 52}。",
            "第四步：{4a_1 = 16}，{a_1 = 4}。"
            "四個數依次是 4、{4+6=10}、{10+6=16}、{16+6=22}。",
            "檢查：{4 + 10 + 16 + 22 = 52} ✔ "
            "第四項減第一項 {= 22 - 4 = 18} ✔ 兩個條件都對得上。"],
        pit="①把 {a_4 - a_1} 寫成 {4d}：走的步數是編號之差 {4-1=3}。"
            "這個「相減得幾個 d」的想法，跟卡三「兩式相除得 {r} 的幾次方」"
            "是同一個結構。"
            "②把「第四項比第一項大 18」讀成「公差是 18」：先把兩項各自用 "
            "{a_1} 與 {d} 寫出來再相減，不要心算。"
            "③四項之和寫成 {4a_1 + 4d}：{d} 的係數是 {0+1+2+3 = 6}。"
            "不確定的話就把四項逐個寫出來再加，比背係數可靠。"),
    4: dict(
        ans="{a_1 = -2}、{r = -frac(1,2)}",
        kp="等比數列的兩項求首項與公比（卡三第三步）。"
           "考點是「兩式相除之後指數是編號之差」，以及開奇次方時負號要保留。",
        fm="{a_n = a_1 r^(n-1)}；{frac(a_5,a_2) = r^3}",
        steps=[
            "第一步（相除）：{a_2 = a_1 r}、{a_5 = a_1 r^4}，"
            "所以 {frac(a_5,a_2) = frac(a_1 r^4,a_1 r) = r^3}。"
            "※ 指數 3 就是編號之差 {5 - 2}。",
            "第二步：代數字 {r^3 = frac(-frac(1,8),1) = -frac(1,8)}。"
            "{-frac(1,8) = (-frac(1,2))^3}（{2^3 = 8}，3 是奇數所以負號保留），"
            "得 {r = -frac(1,2)}。",
            "第三步（求首項）：{a_2 = a_1 r = 1}，"
            "所以 {a_1 = frac(1,r) = 1 ÷ (-frac(1,2)) = -2}。",
            "檢查：數列是 −2、1、{-frac(1,2)}、{frac(1,4)}、{-frac(1,8)}。"
            "第二項是 1 ✔ 第五項是 {-frac(1,8)} ✔ "
            "而且公比為負，各項正負交替 ✔"],
        pit="①把 {frac(a_5,a_2)} 寫成 {r^5} 或 {r^4}：指數是編號之差 {5-2=3}。"
            "②開三次方時把負號丟掉，得 {r = frac(1,2)}："
            "那樣首項會變成 2、數列全部是正數，第五項變成 {frac(1,8)} 而不是負數。"
            "口訣：負數的奇次方是負、偶次方是正——這裡是三次方（奇數），負號保留。"
            "③用 {a_2 = a_1 r^2} 求首項：第 2 項的指數是 {2-1=1}。"),
    5: dict(
        ans="（a）共 7 項　（b）{S_7 = 2186}",
        kp="同一題內用兩次卡三：(a) 用通項公式反解項數，"
           "(b) 用求和公式。留意兩條公式的指數不同——通項是 {n-1}、求和是 {n}。",
        fm="{a_n = a_1 r^(n-1)}；{S_n = frac(a_1(r^n - 1),r - 1)}",
        steps=[
            "小問 (a) 第一步：{a_1 = 2}，"
            "{r = frac(6,2) = 3}（覆核：{frac(18,6) = 3} ✔）。",
            "小問 (a) 第二步：{a_n = 2 * 3^(n-1) = 1458}，"
            "即 {3^(n-1) = frac(1458,2) = 729}。",
            "小問 (a) 第三步：{729 = 3^6}（3、9、27、81、243、729），"
            "所以 {n - 1 = 6}，{n = 7}。共 7 項。",
            "小問 (a) 檢查：逐項寫出 2、6、18、54、162、486、1458——"
            "確實是 7 項，而且最後一項正是 1458 ✔",
            "小問 (b)：{S_7 = frac(a_1(r^7 - 1),r - 1) = frac(2(3^7 - 1),3 - 1)}。"
            "{3^7 = 2187}，所以 {= frac(2(2187 - 1),2) = frac(2 * 2186,2) = 2186}。"
            "※ 求和公式的指數是 {n = 7}（不是 {n - 1 = 6}），這一點與通項公式不同。",
            "小問 (b) 覆核（逐項相加）："
            "{2 + 6 = 8}、{8 + 18 = 26}、{26 + 54 = 80}、{80 + 162 = 242}、"
            "{242 + 486 = 728}、{728 + 1458 = 2186} ✔ 與公式相同。"],
        pit="①(b) 把求和公式的指數寫成 {n-1 = 6}："
            "會得出 {frac(2(729-1),2) = 728}，剛好是前 6 項的和，"
            "數字看上去很正常，完全看不出漏了最後一項。"
            "這是本題最貴的錯——通項用 {n-1}、求和用 {n}，兩條公式的指數不同。"
            "②(a) 把 {2 * 3^(n-1) = 1458} 直接寫成 {3^(n-1) = 1458}（忘記先除 2）："
            "1458 不是 3 的整次方（{3^6 = 729}、{3^7 = 2187}），"
            "解不出整數 {n}——解不出來時先回頭看有沒有漏了首項那個係數。"
            "③(b) 分母寫成 {r + 1}：公式的分母是 {r - 1}。"
            "{r = 3} 時分母是 2；寫成 4 的話答案會少一半。"),
    6: dict(
        ans="（a）恆等式成立（基礎步驟與歸納步驟均已驗證）　（b）3080",
        kp="數學歸納法三步（卡四），加上「證出來的公式可以直接拿來用」。"
           "(b) 是本題的用意——歸納法不是純粹的證明練習，"
           "證出來的公式可以把 20 項的加法變成一次乘除。",
        fm="{1 * 2 + 2 * 3 + ⋯ + n(n+1) = frac(n(n+1)(n+2),3)}",
        steps=[
            "小問 (a) 第一步（基礎步驟）：代 {n = 1}。"
            "左邊只有一項：{1 * 2 = 2}。"
            "右邊：{frac(1 * 2 * 3,3) = frac(6,3) = 2}。"
            "左邊 ＝ 右邊 ＝ 2 ✔ {n = 1} 時成立。",
            "小問 (a) 第二步（歸納假設）：設 {n = k} 時成立，即"
            "{1 * 2 + 2 * 3 + ⋯ + k(k+1) = frac(k(k+1)(k+2),3)}。",
            "小問 (a) 第三步（先寫出目標）：{n = k+1} 時應該是"
            "{frac((k+1)(k+2)(k+3),3)}"
            "（把公式裡的 {n} 全部換成 {k+1}）。",
            "小問 (a) 第三步（加第 {(k+1)} 項）：通項 {n(n+1)} 的 {n} 換成 {k+1}，"
            "即 {(k+1)(k+2)}。在假設兩邊加上它——"
            "左邊 {= frac(k(k+1)(k+2),3) + (k+1)(k+2)}。",
            "小問 (a) 第四步（提取公因式）：兩項都有 {(k+1)(k+2)}——"
            "{= (k+1)(k+2)[frac(k,3) + 1] = (k+1)(k+2) * frac(k + 3,3) "
            "= frac((k+1)(k+2)(k+3),3)}。",
            "小問 (a)：這與第三步寫下的目標完全相同 ✔ "
            "即 {n = k+1} 時也成立。"
            "由基礎步驟與歸納步驟，依數學歸納法原理，"
            "原式對所有自然數 {n} 成立。",
            "小問 (b)：要求的是 {1 * 2 + 2 * 3 + ⋯ + 20 * 21}，"
            "對照通項 {n(n+1)}，末項 {20 * 21} 對應 {n = 20}。",
            "小問 (b)：代入公式 "
            "{frac(20 * 21 * 22,3) = frac(9240,3) = 3080}。"
            "※ 先約簡更快：{frac(21,3) = 7}，"
            "所以 {20 * 7 * 22 = 140 * 22 = 3080} ✔",
            "小問 (b) 覆核（用小數目驗公式）：{n = 3} 時，"
            "左邊 {= 1*2 + 2*3 + 3*4 = 2 + 6 + 12 = 20}，"
            "右邊 {= frac(3 * 4 * 5,3) = 20} ✔ 公式沒有抄錯。"],
        pit="①(a) 第一步只寫「代 {n = 1} 成立」而沒有把左右兩邊各自算出來："
            "考試會扣分，因為看不出你有沒有真的驗過。"
            "②(a) 第三步加錯項——第 {(k+1)} 項要由通項 {n(n+1)} 換 {n} 得出，"
            "是 {(k+1)(k+2)}；寫成 {(k+1)(k+1)} 或 {k(k+1)} 都不對。"
            "③(a) 提取公因式之後忘記通分：{frac(k,3) + 1} 要寫成 "
            "{frac(k+3,3)}，寫成 {frac(k+1,3)} 就湊不出目標。"
            "④(b) 代 {n = 21}（因為看到 21）：末項是 {20 * 21}，"
            "對照通項 {n(n+1)} 應該取 {n = 20}。"
            "對策是把末項與通項並排寫一次再決定。"),
}

# ================================================================ 工具卡
TC_TEXT = [
    ("▍卡一・等差數列", "相減之後差固定；出現「等差數列」「公差」。",
     ["① 定 {a_1} 與 {d}（後項減前項）",
      "② {a_n = a_1 + (n-1)d}",
      "③ 題目要哪一項就代哪個 {n}",
      "④ 代 {n = 1} 回去應該得回首項",
      "※ 括號裡是 {n-1}：由第 1 項走到第 n 項只走 {n-1} 步"]),
    ("▍卡二・等差級數（求和）", "要把一串等差數加起來。",
     ["① 先數項數 {n = frac(末 - 首,d) + 1}",
      "② {S_n = frac(n(a_1 + a_n),2)}",
      "③ 先算括號，再乘 {n}，最後除 2",
      "④ 用「平均數 × 項數」覆核",
      "※ 那個「＋1」最易漏：30 到 235 每次加 5 是 42 項不是 41 項"]),
    ("▍卡三・等比數列", "相除之後商固定；出現「等比數列」「公比」。",
     ["① 定 {a_1} 與 {r}（後項除前項）",
      "② 通項 {a_n = a_1 r^(n-1)}",
      "③ 已知兩項求 {r}：兩式相除，指數＝編號之差",
      "④ 求和 {S_n = frac(a_1(r^n - 1),r - 1)}",
      "※ 通項用 {n-1}、求和用 {n}，兩條指數不同",
      "※ 負的 {r} 要連負號放進括號：{(-frac(1,2))^9}"]),
    ("▍卡四・數學歸納法", "出現「試用數學歸納法證明」。",
     ["① 基礎：代 {n = 1}，左右兩邊各自算一次",
      "② 假設：寫「設 {n = k} 時成立」並把該式抄一次",
      "③ 歸納：在假設兩邊加上第 {(k+1)} 項",
      "④ 提公因式、因式分解，湊成目標",
      "※ 先寫出「目標長什麼樣」再去湊",
      "※ 第 {(k+1)} 項＝通項的 {n} 換成 {k+1}"]),
    ("▍對照卡・等差 vs 等比", "落筆之前先用這張卡判斷種類。",
     ["・相減兩次：差相同 → 等差",
      "・相除兩次：商相同 → 等比",
      "・都不同 → 兩種都不是，看分子分母各自的規律",
      "・等差：每次「加 {d}」；等比：每次「乘 {r}」",
      "※ 一定要看到第三項才落筆",
      "※ {frac(1,2)},{frac(1,4)},{frac(1,8)} 是等比；"
      "{frac(1,2)},{frac(1,4)},{frac(1,6)} 兩種都不是"]),
    ("▍卡六・交卷前自己核對", "每做完一題，四行逐行掃一次再往下。",
     ["☐ 有沒有先判斷是等差還是等比？",
      "☐ 指數／係數用的是 {n-1} 還是 {n}，有沒有用對？",
      "☐ 項數有沒有加回那個「＋1」？",
      "☐ 有沒有代一個已知項回去檢查？",
      "☐ 歸納法三步（基礎／假設／歸納）齊不齊？"]),
]


# ================================================================ docx
def frayer_half_docx(entries):
    """D13 半成品卡：定義與公式已填，「是的例／不是的例」留空給學生。"""
    half = _PAGE_CONTENT_WIDTH // 2
    widths = [half, _PAGE_CONTENT_WIDTH - half]
    rows = [{"cells": [{"p": [para(FR_HALF_TITLE, bold=True, sz=22)],
                        "span": 2, "shd": GREY_FILL}]}]
    for name, dfn, fml, ex, nex in entries:
        rows.append({"cells": [{"p": [para("▍" + name, bold=True, sz=22)],
                                "span": 2, "shd": GREY_FILL}]})
        rows.append({"cells": [[para(dfn, sz=21)], [para(fml, sz=21)]]})
        rows.append({"cells": [{"p": [para(ex, sz=21), blank()]},
                               {"p": [para(nex, sz=21), blank()]}], "h": 900})
    return _tbl(rows, widths)


def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para(A_LEAD))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        if n == 1:
            P.append(frayer_half_docx(FR_HALF))
        P.append(step_card(CARDS_A[n]["title"], CARDS_A[n]["steps"], compact=True))
        P.append(shaded_box(HINT_A[n]))
        P += write_lines(LINES[n])
        P.append(blank())
    P.append(selfcheck_list(SELF_A))
    P.append(checkpoint_rule())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(shaded_box(B_LEAD))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P += write_lines(LINES[n])
        P.append(blank())
    P.append(selfcheck_list(SELF_B, title="做完先自己核對一次（只剩兩項）"))
    P.append(checkpoint_rule())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para(C_LEAD))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P += write_lines(LINES[n])
        P.append(blank())
    P.append(para(SELF_C))

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

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


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


def _frayer_half_html(entries):
    rows = ['<tr><th colspan="2">%s</th></tr>' % _h(FR_HALF_TITLE)]
    for name, dfn, fml, ex, nex in entries:
        rows.append('<tr><th colspan="2" style="font-size:12pt">▍%s</th></tr>'
                    % _esc(name))
        rows.append("<tr><td>%s</td><td>%s</td></tr>" % (_h(dfn), _h(fml)))
        rows.append('<tr><td class="fill">%s</td><td class="fill">%s</td></tr>'
                    % (_h(ex), _h(nex)))
    return '<table class="d-tbl frayer">%s</table>' % "".join(rows)


def _selfcheck_html(items, title="做完先自己核對一次"):
    return ('<div class="selfcheck"><div style="font-weight:700">%s</div>%s</div>'
            % (_esc(title), "".join("<div>☐ %s</div>" % _h(t) for t in items)))


_EXTRA_CSS = """
  /* QB-20：範本的頁尾用固定定位＋白底，內文流到頁底會被它蓋住。
     把 @page 的下邊界撐大，內文區就會提早結束（L12 實測定案）。 */
  @page { margin-bottom: 1.5cm; }
  .hint-card, .selfcheck { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .d-tbl.step-card, .d-tbl.step-card tr,
  .d-tbl.frayer, .d-tbl.frayer tr { break-inside: avoid; page-break-inside: avoid; }
  .frayer td { width: 50%; vertical-align: top; }
"""


def _head(tpl, title, extra_css):
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", title)
    return head.replace("</head>", "<style>\n%s\n</style>\n</head>" % extra_css)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = _head(tpl, "練習：" + UNIT, _EXTRA_CSS)

    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂練習</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')
    parts.append('<div class="hint-card">%s</div>' % _h(HINT_TOP))

    parts.append('<div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>')
    parts.append('<div>%s</div>' % _h(A_LEAD))
    # 題幹自己一個 .problem 框，鷹架與作答線放在框外——全部塞進同一個
    # break-inside:avoid 的框裡，一題就會獨佔一頁、下面留一大片白（L12 實測）
    for n in A_ITEMS:
        fr = _frayer_half_html(FR_HALF) if n == 1 else ""
        parts.append('<div class="problem">%d．%s</div>%s%s'
                     '<div class="hint-card">%s</div>%s'
                     % (n, _h(STEMS[n]), fr, _step_html(CARDS_A[n]),
                        _h(HINT_A[n]), _lines(LINES[n])))
    parts.append(_selfcheck_html(SELF_A))
    parts.append('<div class="checkpoint">【核對點】做到這裡先停，'
                 '對照上面的清單檢查一次再往下</div>')

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div class="hint-card">%s</div>' % _h(B_LEAD))
    for n in B_ITEMS:
        parts.append('<div class="problem">%d．%s</div>%s'
                     % (n, _h(STEMS[n]), _lines(LINES[n])))
    parts.append(_selfcheck_html(SELF_B, "做完先自己核對一次（只剩兩項）"))
    parts.append('<div class="checkpoint">【核對點】做到這裡先停，'
                 '對照上面的清單檢查一次再往下</div>')

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>%s</div>' % _h(C_LEAD))
    for n in C_ITEMS:
        parts.append('<div class="problem">%d．%s</div>%s'
                     % (n, _h(STEMS[n]), _lines(LINES[n])))
    parts.append('<div>%s</div>' % _h(SELF_C))

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
