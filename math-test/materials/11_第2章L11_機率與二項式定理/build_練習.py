# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L11 機率與二項式定理 —— 課堂練習 ＋ 工具卡 build script

主設計 D2 手順卡，褪除照研究原文的四級：
  講義＝完整卡（動作＋※易錯點）→ A＝精簡卡（只留動作）→ B＝只留步驟數量與卡號 → C＝移除。
輔助 D8 陷阱詞（A 題幹已用「」標出 → B 只在區塊開頭重印三個 → C 不提）、
D12 自我核對（A 完整四項 → B 兩項 → C 一句話；工具卡第六張是本體）。
鷹架密度：抽離小班 (Tier 2)。

產出：練習_機率與二項式定理_抽離小班共用版.docx/.html、工具卡_機率與二項式定理.docx/.html

注意：
1. `{...!=...}` 會被 omml_core 轉成 ≠，階乘後的等號一定要留空格（`{5! = 120}`）。
2. 參考答案的 steps 由迴圈自動編「　（1）（2）…」，所以 steps 字串本身
   不可以用「（1）」開頭（會印成「（1）（1）」，L10 踩過）——小問一律寫「小問 (1)：」。
3. 分數用 `frac(a,b)`；帶次方的分數寫 `(frac(1,2))^4`。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_機率與二項式定理_抽離小班共用版"
CARDF = "工具卡_機率與二項式定理"
UNIT = "第2章 中學基礎數學應用．L11 機率與二項式定理"
FOOT = "高三數學．" + UNIT

# ================================================================ 引導語
HINT_TOP = ("本課的題目計算都很短，錯的地方幾乎全部是「跳了一步」。"
            "所以做每一題之前先做同一件事：認出這題屬於哪一類，翻出對應的手順卡，"
            "把卡放在題目旁邊，用手指指住正在做的那一步。"
            "本份練習的提示會一節比一節少："
            "練習A 每題下方重印該用的那張卡（只留動作，不再印易錯點）；"
            "練習B 只告訴你這題有幾步、翻第幾張卡；"
            "練習C 兩者都不給，而且同一題裡要換兩張卡。")

B_LEAD = ("由這一節開始不再印步驟內容，只給步驟數量與卡號，"
          "卡上寫什麼要自己想得起來（想不起就翻工具卡，但先自己試一次）。"
          "▍第 3 題：(a) 屬卡三，四步；(b) 屬卡二，三步。"
          "▍第 4 題：兩小問都屬卡五；(a) 只用到卡五第二步那句「共有 n ＋ 1 項」，"
          "(b) 要走完四步。"
          "※ 三個陷阱詞重印一次，題幹不再標出來，要自己圈："
          "「最少一個」→ 1 −（一個都沒有）；"
          "「恰好 k 次」→ 要乘 {C(n,k)}；"
          "「第三項」→ r ＝ 2，不是 3。")

C_LEAD = ("本節收起工具卡，也不再給卡號。"
          "兩題都是同一題裡面要換兩張卡——先認清楚每個小問各自屬於哪一類，"
          "再逐個走完該卡的步驟。"
          "動筆之前先問自己三句：這題只做一次還是做很多次？"
          "有沒有「最少」「恰好」這些字？分子與分母是不是用同一把尺？")

# ================================================================ 題目
STEMS = {
    1: "（a）同時投擲一枚伍元硬幣和一枚一元硬幣，"
       "出現「兩面都是正面」的機率是多少？　"
       "（b）一次拋擲 3 枚硬幣，出現「3 面都是正面」的機率是多少？",
    2: "一個袋中放有紅色、黃色、藍色三種球，除顏色外其他部分都相同，"
       "紅球、黃球、藍球的個數之比為 4 : 3 : 2。"
       "（1）任意抽出一個球，抽到紅球的機率是多少？　"
       "（2）任意抽出一個球，抽到「不是紅球」的機率是多少？　"
       "（3）若袋中的藍球有 6 個，袋中共有多少個球？",
    3: "（a）小吉有物理、化學和生物三科測驗，"
       "他在這三科測驗合格的機率分別為 0.8、0.75 和 0.6。"
       "求他最少一科測驗合格的機率。　"
       "（b）小明的球隊打入 16 強，他每一場勝出的機率都是 0.1。"
       "由 16 強起計，他的球隊最終打入決賽的機率是多少？",
    4: "（a）展開 {(5x+14y)^15}，共有多少項？　"
       "（b）求 {(1+x)^8} 展開式的第三項。",
    5: "（a）5 人之中有三男兩女，從中抽兩次、每次抽 1 人（抽出後不放回），"
       "抽出的兩人性別相同的機率是多少？　"
       "（b）投擲一顆六面的骰子 5 次，恰好擲得兩次六點的機率是多少？"
       "（答案取三位小數）",
    6: "（a）一個邊長 30 cm 的正方體，每一面都塗上顏色，"
       "然後切成邊長 10 cm 的小正方體。"
       "從所有小正方體中任意抽 1 塊，抽到「只有一面有顏色」的機率是多少？　"
       "（b）求 {(4-2x)^5} 展開式中 {x^2} 的係數。",
}

# ---------------------------------------------------------------- D2 精簡卡（練習A）
CARDS_A = {
    1: dict(title="▍第 1 題用卡二・做很多次",
            steps=[("確認每一次互不影響（獨立）", None),
                   ("寫出每一次各自的機率", None),
                   ("全部相乘", None),
                   ("每次都一樣時，指數就是次數", None)]),
    2: dict(title="▍第 2 題用卡一・算一條機率（(2) 順便用卡三）",
            steps=[("先寫分母：全部可能的結果有幾個", None),
                   ("再寫分子：符合題目要求的有幾個", None),
                   ("寫成分數，約到最簡", None),
                   ("檢查：答案有沒有落在 0 與 1 之間", None)]),
}
HINT_A = {
    1: "▍題幹已用「」把要圈的字標出：「兩面都是正面」「3 面都是正面」——"
       "「都是」是卡二的觸發語，兩件（或三件）事全部要發生 → 相乘。",
    2: "▍(2) 的「不是紅球」是卡三的同一個念頭：一件事的機率，"
       "加上它「不發生」的機率，等於 1。"
       "▍(3) 題目只給了比，沒有給個數，所以先找出「一份等於幾個」。",
}

# ---------------------------------------------------------------- D12
SELF_A = ["答案有沒有落在 0 與 1 之間？",
          "分子與分母是不是用同一把尺（同樣是「球的個數」或同樣是「份數」）？",
          "分數有沒有約到最簡？",
          "第 2(3) 題答的是「共有多少個球」，不是「紅球有多少個」？"]
SELF_B = ["第 3(a) 題最後有沒有補回那個「1 −」？",
          "第 4(b) 題用的是 r ＝ 2，不是 r ＝ 3？"]
SELF_C = "做完兩題之後，拿工具卡第六張出來，四行逐行對一次再交。"

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
# 行數同時決定分頁，實測後定案（見下）：
#   第 3、4 題各 8 行 → 練習B 的核對清單與核對點才收得返同一頁，
#     否則兩個框獨佔一頁、全頁 95% 空白（首版 10／9 行時實測）。
#   第 5、6 題 10／9 行 → 練習C 兩題同頁；13／12 行時兩頁各留 40%～50% 白，
#     而 11／10 行時第 6 題之後那句「做完兩題之後⋯」會被 fixed 頁尾白底蓋住
#     （QB-20：PyMuPDF 抽字抽得到、印出來見唔到，只有目視／列印先發現）。
LINES = {1: 8, 2: 12, 3: 8, 4: 8, 5: 10, 6: 9}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）{frac(1,4)}　（b）{frac(1,8)}",
        kp="獨立事件的連乘（卡二）。兩小問是同一件事的兩個規模："
           "(a) 兩枚硬幣、(b) 三枚硬幣，指數就是硬幣的數目。",
        fm="幾件事全部要發生 → 各自的機率相乘；每次都一樣時寫成次方。",
        steps=["（a）兩枚硬幣互不影響，其中一枚的結果不會改變另一枚 → 獨立。"
               "每一枚出現正面的機率都是 {frac(1,2)}。",
               "（a）「兩面都是正面」表示兩件事都要發生 → 相乘："
               "{frac(1,2)*frac(1,2) = frac(1,4)}。",
               "（a）用卡一覆核：兩枚硬幣的全部結果是"
               "（正正）（正反）（反正）（反反）共 {2^2 = 4} 種，"
               "符合的只有（正正）1 種 → {frac(1,4)} ✔ 兩條路相同。",
               "（b）三枚硬幣同理，三件事都要發生 → "
               "{(frac(1,2))^3 = frac(1,8)}。",
               "（b）覆核：全部結果 {2^3 = 8} 種，符合的 1 種 → {frac(1,8)} ✔ "
               "兩小問都通過「0 與 1 之間」的檢查。"],
        pit="① 把相乘寫成相加：{frac(1,2) + frac(1,2) = 1}，"
            "得出「一定會出現兩面正面」這種明顯不合理的答案——"
            "卡一第四步當場就攔得住。"
            "② (b) 答 {frac(1,6)}：那是「三枚硬幣一共有 6 種結果」的誤解，"
            "實際是 {2^3 = 8} 種。"
            "③ 指數寫錯：硬幣有幾枚，指數就是幾。"),
    2: dict(
        ans="（1）{frac(4,9)}　（2）{frac(5,9)}　（3）27 個",
        kp="用「比」當結果數的古典機率（卡一），加上互補事件"
           "（一件事與它的相反，機率相加等於 1）。"
           "(3) 是把卡一倒過來用：由機率與其中一個實際個數，反推總數。",
        fm="P ＝ 符合的數目 ÷ 全部的數目；P(不發生) ＝ 1 − P(發生)。",
        steps=["小問 (1)：題目只給了比，把比當成份數看——"
               "紅 4 份、黃 3 份、藍 2 份，全部合共 4 ＋ 3 ＋ 2 ＝ 9 份（分母）。"
               "符合「抽到紅球」的是紅球那 4 份（分子）。"
               "P(紅球) ＝ {frac(4,9)}，已是最簡。",
               "小問 (2)：「不是紅球」是「是紅球」的相反 → "
               "{1 - frac(4,9) = frac(5,9)}。",
               "小問 (2) 檢核（正面直接算）：不是紅球的是黃 3 份加藍 2 份 ＝ 5 份 → "
               "{frac(5,9)} ✔ 兩條路相同。",
               "小問 (3)：藍球佔 2 份，而題目說藍球有 6 個 → 1 份 ＝ 6 ÷ 2 ＝ 3 個。"
               "全部 9 份 → 9 × 3 ＝ 27 個。",
               "小問 (3) 檢核：紅 4 × 3 ＝ 12 個、黃 3 × 3 ＝ 9 個、藍 6 個，"
               "合共 27 個 ✔ 而且 P(紅球) ＝ {frac(12,27) = frac(4,9)}，"
               "與 (1) 吻合 ✔"],
        pit="① (1) 分母寫成 7（4 ＋ 3，漏了藍球）或者寫成 4："
            "分母是「全部」，包括不符合的那些。"
            "② (2) 重新數一次而數錯：這一題用 1 減最快，也最不易錯。"
            "③ (3) 答 12（紅球數）或答 3（一份的個數）：題目問的是「共有多少個球」，"
            "答案要回頭對一次題目問什麼。"
            "④ (3) 直接寫 6 × 9 ＝ 54：藍球是 2 份不是 1 份，"
            "要先除以 2 才知道一份是多少。"),
    3: dict(
        ans="（a）0.98　（b）0.001",
        kp="(a) 是「最少一科」的補集（卡三）；(b) 是連續事件的連乘（卡二）。"
           "兩小問並排，正是要練習「見到『最少』就走反面、"
           "沒有『最少』就直接乘」這個分岔。",
        fm="P(最少一個) ＝ 1 − P(一個都沒有)；獨立事件連乘。",
        steps=["（a）圈到「最少一科」→ 用補集。"
               "相反事件是「三科全部不合格」，不是「三科全部合格」。",
               "（a）三科各自的不合格機率：1 − 0.8 ＝ 0.2、1 − 0.75 ＝ 0.25、"
               "1 − 0.6 ＝ 0.4。三科都不合格 → 連乘："
               "{0.2*0.25 = 0.05}，{0.05*0.4 = 0.02}。",
               "（a）最後用 1 減：{1 - 0.02 = 0.98}。"
               "檢查：0.98 落在 0 與 1 之間，而且很接近 1——"
               "三科合格率都不低，「一科都不合格」本來就難發生 ✔",
               "（b）由 16 強打入決賽要贏幾場？"
               "16 強 → 8 強（第 1 場）→ 4 強（第 2 場）→ 決賽（第 3 場），"
               "共 3 場。這一步想清楚了，題目就做完一半。",
               "（b）三場都要贏 → 連乘：{0.1^3 = 0.001}。"
               "檢查：0.001 落在 0 與 1 之間，而且極小——"
               "每場只有一成勝算還要連贏三場，合理 ✔"],
        pit="① (a) 把相反寫成「三科全部合格」，算出 1 − {0.8*0.75*0.6} ＝ 1 − 0.36 ＝ 0.64。"
            "「最少一科」的相反只有一種情況：一科都沒有。"
            "② (a) 算完 0.02 就當成答案——漏了卡三第四步的「1 −」。"
            "③ (a) 忘記先把合格率轉成不合格率，直接乘 0.8 × 0.75 × 0.6。"
            "④ (b) 場數數錯，寫成 4 場（{0.1^4 = 0.0001}）或 2 場："
            "16 → 8 → 4 → 決賽，是三步。"),
    4: dict(
        ans="（a）16 項　（b）{28x^2}",
        kp="二項式定理的兩個最基本問法（卡五）："
           "項數只看次方；第幾項要走完通項四步。"
           "(b) 的關鍵是「第 (r ＋ 1) 項對應 r」。",
        fm="{(a+b)^n} 展開共 n ＋ 1 項；通項（第 r ＋ 1 項）"
           "＝ {C(n,r)*a^(n-r)*b^r}。",
        steps=["（a）項數只看次方，與 5x、14y 這兩個係數無關。"
               "n ＝ 15 → 項數 ＝ 15 ＋ 1 ＝ 16 項。",
               "（a）為什麼要加 1：b 的次方由 0 數到 15，"
               "0、1、2、⋯、15 合共 16 個數，所以有 16 項。",
               "（b）第一步：n ＝ 8、a ＝ 1、b ＝ x。",
               "（b）第二步：「第三項」→ r ＝ 3 − 1 ＝ 2。"
               "第三步：{C(8,2)=frac(8*7,2*1)=frac(56,2)=28}。",
               "（b）第四步：乘 {a^(n-r)} ＝ {1^6 = 1}，再乘 {b^r} ＝ {x^2}。"
               "第三項 ＝ {28x^2}。"
               "檢查次方：a 的次方 6 ＋ b 的次方 2 ＝ 8 ＝ n ✔"],
        pit="① (a) 答 15 項：{(a+b)^n} 有 n ＋ 1 項，不是 n 項。"
            "② (b) 用 r ＝ 3，算出 {C(8,3)x^3 = 56x^3}——"
            "那是第四項。第 (r ＋ 1) 項才對應 r。"
            "③ (b) 答「係數是 28」：題目問的是「第三項」，"
            "整項要連 {x^2} 一起寫。"
            "④ (b) 漏了 {a^(n-r)}：本題 a ＝ 1，{1^6 = 1} 剛好不影響答案，"
            "但下一題 a 不是 1 時漏掉就會錯（見第 6 題）。"),
    5: dict(
        ans="（a）{frac(2,5)}　（b）{frac(1250,7776)} ≈ 0.161",
        kp="(a) 是組合型的古典機率（卡一），本課「分子分母同一把尺」"
           "這條規則最重要的一題；(b) 是二項機率（卡四）。"
           "同一題內要換兩張卡。",
        fm="P ＝ 符合的數目 ÷ 全部的數目（兩邊同用組合或同用排列）；"
           "恰好 k 次 ＝ {C(n,k)*p^k*(1-p)^(n-k)}。",
        steps=["（a）分母：從 5 人中抽 2 人。"
               "先後抽出的兩人誰先誰後不影響「性別是否相同」這件事，"
               "所以用組合：{C(5,2)=frac(5*4,2*1)=10}。",
               "（a）分子：兩人性別相同分兩種情況——"
               "兩個都是男：{C(3,2)=3}；兩個都是女：{C(2,2)=1}。"
               "兩種情況只會發生其中一種 → 相加 ＝ 3 ＋ 1 ＝ 4。"
               "P ＝ {frac(4,10) = frac(2,5)}。",
               "（a）檢核（改用另一把尺，兩邊都用排列）："
               "分母 {P(5,2)=5*4=20}，"
               "分子 {P(3,2)+P(2,2)=6+2=8}，"
               "得 {frac(8,20) = frac(2,5)} ✔ 兩把尺答案相同——"
               "重點是「兩邊同時換」，不可以分母用組合、分子用排列。",
               "（b）卡四第一步：n ＝ 5、k ＝ 2，一次擲出六點的機率 {p = frac(1,6)}。"
               "第二步：{C(5,2)=10}（5 次之中揀 2 次成功）。",
               "（b）第三步：{(frac(1,6))^2 = frac(1,36)}。"
               "第四步：其餘 5 − 2 ＝ 3 次都不是六點，"
               "每次 {frac(5,6)} → {(frac(5,6))^3 = frac(125,216)}。",
               "（b）三者相乘："
               "{10*frac(1,36)*frac(125,216) = frac(1250,7776) = frac(625,3888)} ≈ 0.161。"
               "檢核：分母 {36*216 = 7776 = 6^5}，正好是擲 5 次骰子的全部結果數 ✔"],
        pit="① (a) 分母用組合、分子用排列（或反過來），得出 {frac(8,10)} 這種錯答案。"
            "兩邊必須用同一把尺。"
            "② (a) 兩種情況相乘（3 × 1 ＝ 3）：「兩個都是男」與「兩個都是女」"
            "不會同時發生，是分類 → 相加。"
            "③ (b) 漏了 {C(5,2)}，只寫 {(frac(1,6))^2*(frac(5,6))^3} ≈ 0.016——"
            "那是「頭兩次是六點、之後三次都不是」這一種特定情形。"
            "④ (b) 把 {(frac(5,6))} 的次方寫成 5：失敗的次數是 n − k ＝ 3。"),
    6: dict(
        ans="（a）{frac(6,27) = frac(2,9)}　（b）2560",
        kp="(a) 是要先把立體切割想清楚才數得出分子的古典機率（卡一）；"
           "(b) 是 a 不等於 1、b 帶負號的通項（卡五），"
           "是本課「負號連 b 一起搬」與「a 的次方是 n − r」兩個易錯點的總結題。",
        fm="P ＝ 符合的數目 ÷ 全部的數目；通項 ＝ {C(n,r)*a^(n-r)*b^r}。",
        steps=["（a）分母：30 ÷ 10 ＝ 3，所以每邊切成 3 段，"
               "共 {3^3 = 27} 粒小正方體。",
               "（a）分子：只有一面有顏色的，是每一面正中央那一粒"
               "（四邊都被其他小方塊包住，只有朝外那一面著色）。"
               "正方體有 6 個面，每面 1 粒 → 6 粒。"
               "P ＝ {frac(6,27) = frac(2,9)}。",
               "（a）檢核（把 27 粒全部分類）：三面著色的是 8 個角、"
               "兩面著色的是 12 條稜的中間各 1 粒、一面著色的 6 粒、"
               "完全沒有著色的是最中心 1 粒。"
               "8 ＋ 12 ＋ 6 ＋ 1 ＝ 27 ✔ 分類沒有遺漏，分子 6 正確。",
               "（b）卡五第一步：n ＝ 5、a ＝ 4、b ＝ −2x（負號連 b 一起搬）。",
               "（b）第二步：要求 {x^2} 的係數，x 只在 b 裡面，"
               "所以 r ＝ 2。第三步：{C(5,2)=frac(5*4,2*1)=10}。",
               "（b）第四步：乘 {a^(n-r)} ＝ {4^3 = 64}，"
               "再乘 {b^r} ＝ {(-2)^2*x^2 = 4x^2}。"
               "整項 ＝ {10*64*4*x^2 = 2560x^2}，係數是 2560。"
               "檢查次方：3 ＋ 2 ＝ 5 ＝ n ✔ "
               "檢查正負：(−2) 的偶次方為正，所以係數是正數 ✔"],
        pit="① (a) 分子答 6 × 4 ＝ 24 或答 8：只有一面著色的是「面的正中央」，"
            "每面只有 1 粒（因為每邊只切成 3 段）。"
            "② (a) 忘記約分：{frac(6,27)} 要約成 {frac(2,9)}。"
            "選擇題的選項若同時印出 {frac(6,27)} 與 {frac(1,3)}，"
            "後者是把 9 誤看成分母的陷阱。"
            "③ (b) 把 b 寫成 2x，漏了負號——本題剛好因為偶次方而答案不變，"
            "但奇次方時就會差一個負號，習慣要一開始就把負號連 b 搬過去。"
            "④ (b) 把 a 的次方寫成 5（{4^5 = 1024}）："
            "a 與 b 的次方加起來一定等於 n，所以 a 的次方是 5 − 2 ＝ 3。"),
}


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para("題幹已用「」把該圈的字標出，每題下方重印了該用的那張手順卡"
                  "（只留動作，易錯點請自己回想，想不起才翻講義）。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
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


# ================================================================ 工具卡
# 前五張＝講義那五張 D2 手順卡的桌面版；第六張是 D12 自我核對。
# 卡片不用 OMML 分數以外的高構件（分數會疊高行距，六張卡就入不到一頁，L4 實測），
# 但一定要留幾條 {} 標記的短式，否則 m:oMath ＝ 0 會 QB-2 FAIL（L8 實測）。
TC_TEXT = [
    ("▍卡一・算一條機率", "只做一次（摸一個球、抽一塊），問「機率是多少」。",
     ["① 分母：全部可能的結果有幾個",
      "② 分子：其中符合題目的有幾個",
      "③ 寫成分數，約到最簡：{frac(6,27) = frac(2,9)}",
      "※ 分母包括不符合的；分子分母要用同一把尺"]),
    ("▍卡二・做很多次", "題目說「都是⋯」「連續⋯」「同時⋯」。",
     ["① 確認每次互不影響（放回才獨立）",
      "② 寫出每一次各自的機率",
      "③ 全部相乘",
      "※ 每次一樣就寫成次方，指數＝次數：{(frac(1,2))^4}"]),
    ("▍卡三・「最少一個」", "題目出現「最少／至少一個」「不都是」「並非全部」。",
     ["① 圈出「最少」，不要正面逐個數",
      "② 相反是「一個都沒有」，不是「全部都有」",
      "③ 算相反事件的機率（多數是卡二的連乘）",
      "④ 用 1 減：{1 - 0.006 = 0.994}　※ 最易漏"]),
    ("▍卡四・做 n 次恰好 k 次", "同一動作重複 n 次，問「其中恰好有 k 次⋯」。",
     ["① 定 n（總次數）與 k（成功次數）",
      "② 乘 {C(n,k)}：揀邊幾次成功　※ 最易漏",
      "③ 乘 {p^k}：成功那幾次",
      "④ 乘 {(1-p)^(n-k)}：失敗的是 n − k 次"]),
    ("▍卡五・二項式定理", "題目出現「展開式」「共有幾項」「第三項」「係數」。",
     ["① 定 n、a、b　※ 負號要連 b 一起搬",
      "② 第 (r ＋ 1) 項對應 r；全式共 n ＋ 1 項",
      "③ 寫 {C(n,r)}（就是 L10 的組合數）",
      "④ 乘 {a^(n-r)} 再乘 {b^r}　※ 兩個次方加起來＝n"]),
    ("▍卡六・交卷前自己核對", "每做完一題，四行逐行掃一次再往下。",
     ["☐ 答案有沒有落在 0 與 1 之間？",
      "☐ 分子與分母是不是用同一把尺？",
      "☐ 見到「最少」，有沒有補回那個「1 −」？",
      "☐ 展開式：a 與 b 的次方加起來等於 n 嗎？"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in TC_TEXT:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        # ☐ 與 ※ 開頭的行本身已有標記，不再加「・」
        c += [para(t if t[0] in "☐※" else "・" + t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=4000))
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
    body = re.sub(r"(?<![\\{\w.!])(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)(?![}\w.])",
                  r"\\frac{\1}{\2}", body)
    body = body.replace("%", r"\%")
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


def _step_html(card, compact=False):
    rows = ['<tr><th colspan="2">%s</th></tr>' % _h(card["title"])]
    if card.get("trigger") and not compact:
        rows.append('<tr><td colspan="2" style="font-weight:400">什麼時候用：%s</td></tr>'
                    % _h(card["trigger"]))
    for i, (act, pit) in enumerate(card["steps"], 1):
        if compact or not pit:
            rows.append('<tr><td colspan="2">%d. %s</td></tr>' % (i, _h(act)))
        else:
            rows.append('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                        % (i, _h(act), _h(pit)))
    return '<table class="d-tbl step-card">%s</table>' % "".join(rows)


def _selfcheck_html(items, title="做完先自己核對一次"):
    return ('<div class="selfcheck"><div style="font-weight:700">%s</div>%s</div>'
            % (_esc(title), "".join("<div>☐ %s</div>" % _h(t) for t in items)))


def _head(tpl, title, extra_css):
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", title)
    return head.replace("</head>", "<style>\n%s\n</style>\n</head>" % extra_css)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = _head(tpl, "練習：" + UNIT, """
  .hint-card, .fig, .selfcheck { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .d-tbl.step-card, .d-tbl.step-card tr { break-inside: avoid; page-break-inside: avoid; }
""")

    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂練習</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')
    parts.append('<div class="hint-card">%s</div>' % _h(HINT_TOP))

    parts.append('<div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>')
    parts.append('<div>題幹已用「」把該圈的字標出，每題下方重印了該用的那張手順卡'
                 '（只留動作，易錯點請自己回想，想不起才翻講義）。</div>')
    for n in A_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s'
                     '<div class="hint-card">%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _step_html(CARDS_A[n], compact=True),
                        _h(HINT_A[n]), _lines(LINES[n])))
    parts.append(_selfcheck_html(SELF_A))
    parts.append('<div class="checkpoint">【核對點】做到這裡先停，'
                 '對照上面的清單檢查一次再往下</div>')

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div class="hint-card">%s</div>' % _h(B_LEAD))
    for n in B_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _lines(LINES[n])))
    parts.append(_selfcheck_html(SELF_B, "做完先自己核對一次（只剩兩項）"))
    parts.append('<div class="checkpoint">【核對點】做到這裡先停，'
                 '對照上面的清單檢查一次再往下</div>')

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>%s</div>' % _h(C_LEAD))
    for n in C_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s</div>'
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
    """工具卡的 HTML 版：本機 Word COM 轉檔不穩，改由 Chrome 出 PDF（見專案 CLAUDE.md）。
    版面對齊 docx 的 2 欄 × 3 列虛線裁切格。"""
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = _head(tpl, "工具卡：" + UNIT, """
  .tc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; margin-top: 8px; }
  .tc { border: 1px dashed #444; padding: 10px 12px; min-height: 6.6cm;
        break-inside: avoid; page-break-inside: avoid; }
  .tc .t { font-weight: 700; font-size: 14pt; }
  .tc .g { font-size: 10.5pt; color: #333; margin: 2px 0 6px; }
  .tc .i { font-size: 10.5pt; line-height: 1.55; }
""")
    cards = "".join(
        '<div class="tc"><div class="t">%s</div><div class="g">%s</div>%s</div>'
        % (_esc(title), _h(trig),
           "".join('<div class="i">%s</div>'
                   % _h(t if t[0] in "☐※" else "・" + t) for t in items))
        for title, trig, items in TC_TEXT)
    parts = ['<div class="masthead"><span>科目：高三數學</span><span>單元：'
             + _esc(UNIT) + '</span><span>類型：工具卡（剪下沿虛線，護貝後放桌面）</span></div>',
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
