# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L10 排列與組合 —— 課堂練習 ＋ 工具卡 build script

主設計 D8 關鍵字對譯（褪除：A 題幹已把關鍵字用「」標好並寫明查到哪一條 →
B 只重印五個觸發語 → C 完全不標，要自己圈）；
輔助 D1 樹狀圖（只在練習A 第 1 題提一句「不肯定就先畫兩層樹」，之後移除）、
D7 提示卡（A 每題標明翻哪一張 → B 只列觸發語 → C 收起工具卡）。
鷹架密度：抽離小班 (Tier 2)。

產出：練習_排列與組合_抽離小班共用版.docx/.html、工具卡_排列與組合.docx/.html

注意：`{...!=...}` 會被 omml_core 轉成 ≠，階乘後的等號一定要留空格（`{5! = 120}`）。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_排列與組合_抽離小班共用版"
CARDF = "工具卡_排列與組合"
UNIT = "第2章 中學基礎數學應用．L10 排列與組合"
FOOT = "高三數學．" + UNIT

# ================================================================ 題目
HINT_TOP = ("動筆之前永遠先做同一件事：在題目上圈出關鍵字，再查對譯表。"
            "次序固定三步——① 圈關鍵字 → ② 決定用哪一招 → ③ 才計算。"
            "本份練習的提示會一節比一節少："
            "練習A 已用引號把關鍵字標出，並寫明查到哪一條；"
            "練習B 只重印五個觸發語；練習C 完全不提示。")

TRIG_LIST = ("由這一節開始不再標明該翻哪一張卡，要自己圈關鍵字。五張卡的觸發語重印一次："
             "▍卡一：「必須站在頭／尾／中間」，或「不站在某位置」。"
             "▍卡二：「必須相鄰」「坐在一起」「不能分開」。"
             "▍卡三：「不相鄰」「不能挨着」「要隔開」。"
             "▍卡四：要排的東西裡面有一模一樣的。"
             "▍卡五：「至少一個」「不都是」「並非全部」。"
             "※ 沒有踩到以上五條的題目，就是普通的加、乘、{P(n,r)}、{C(n,r)}，"
             "回到《動筆前的三個問題》那三步就夠。")

C_LEAD = ("本節收起工具卡，題幹也不再標關鍵字，要自己圈出來。"
          "動筆之前先走完《動筆前的三個問題》："
          "① 加還是乘 → ② {P(n,r)} 還是 {C(n,r)} → ③ 有沒有附加條件。")

STEMS = {
    1: "（a）甲、乙、丙三人到速食店用餐。該店只提供三種套餐，"
       "三人「每人各點一套餐」，共有多少種點餐方式？　"
       "（b）有一樂團計畫到甲、乙兩國巡迴表演。甲國有三個城市要表演、"
       "乙國有四個城市要表演。若「先」完成甲國的演出，「再」到乙國完成演出，"
       "則巡迴路線的規劃有多少種可能？",
    2: "將甲、乙、丙、丁四人排成一列，試求下列的排列數："
       "（1）四人任意排列　（2）「甲排首位」　（3）「乙不排末位」。",
    3: "從 1、2、3、4、5 中任選三個數字，排成三位數，數字不可重複，則："
       "（1）可得幾個不同的三位數？　（2）其中有幾個是奇數？",
    4: "（a）某青年創業開餐廳，擬設計一份有 5 種菜色的菜單。"
       "若在原始構思的 7 種菜色中有 2 種為必選，則有幾種不同菜單？　"
       "（b）6 人排成一排照相，甲不站在頭（左），有多少種排法？",
    5: "把 5 塊不同的蛋糕，任意分給 A、B、C 三人，試求下列方法數："
       "（1）任意分（蛋糕一定要分完）　（2）C 至少拿到一塊蛋糕。",
    6: "（a）從 6 人中選 4 人圍圓桌而坐，方法有幾種？　"
       "（b）已知 {C(10,R+4)=C(10,R-2)}，求 R 的值。",
}

# 練習A：D8／D7 褪除第一級——寫明圈到的是哪個關鍵字、查到表上哪一條
CARD_HINT = {
    1: "▍(a) 圈到的是「每人各點一個」→ 查表得「每個人獨立選一次 → 連乘」。"
       "三個人各自有 3 種選擇，互不影響。"
       "不肯定就先畫兩層樹：甲有 3 個分枝，每個分枝下面乙再分 3 枝。"
       "▍(b) 圈到的是「先…再…」→ 查表得「分步 → 相乘」。"
       "另外留意「巡迴路線」＝去城市的先後次序不同就是不同的規劃，"
       "所以每一國「內部」還要排先後。",
    2: "▍(2) 圈到「排首位」→ 翻提示卡一（特殊位置優先）："
       "先把甲固定在第一位，其餘的人才排。"
       "▍(3) 圈到「不排末位」→ 同樣是提示卡一，但走反面："
       "全部 −（乙排末位的排法）。「不」字幾乎一定用減。",
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
# 第 2 題三個小問、獨佔第 2 頁，作答行給到 16 行才填得滿該頁（8 行時下半頁全白）；
# 第 5、6 題同頁，各加 2 行把第 4 頁下半的留白收窄。
LINES = {1: 7, 2: 16, 3: 8, 4: 8, 5: 10, 6: 11}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）27 種　（b）144 種",
        kp="乘法原理（分步計數）的兩種形態：(a) 是「每個人各自獨立選一次」，"
           "(b) 是「兩個階段先後完成，而且每個階段內部還要排先後」。"
           "同樣用相乘，但相乘的是什麼並不一樣。",
        fm="分步 → 各步的方法數相乘；n 件不同的東西全部排成一列 ＝ {n!}。",
        steps=["（a）三個人是分得開的，每人各自從 3 種套餐中選 1 種，互不影響。"
               "甲有 3 種選擇、乙有 3 種、丙有 3 種 → 3 × 3 × 3 ＝ {3^3 = 27} 種。",
               "（a）檢核：把三人的選擇寫成（甲, 乙, 丙）三個位置，每個位置填 1 至 3，"
               "數一數合共 {3^3 = 27} 組 ✔",
               "（b）「巡迴路線」是指去城市的先後次序，次序不同就是不同的規劃。"
               "甲國三個城市的次序有 {3! = 6} 種。",
               "（b）乙國四個城市的次序有 {4! = 24} 種。"
               "甲國全部演完才到乙國，兩段都要完成 → 分步相乘 ＝ 6 × 24 ＝ 144 種。"],
        pit="① (a) 誤以為是排列 {P(3,3)=6}——那是「三人各點不同套餐」才對，"
            "題目沒有這個限制，三人可以都點同一款。"
            "② (b) 只寫 3 × 4 ＝ 12：那是「甲國揀一個城市、乙國揀一個城市」，"
            "但題目說三個與四個城市「都要去」，要排次序。"
            "③ (b) 寫成 {7! = 5040}：七個城市不是自由排列，甲國三個一定排在乙國四個之前。"),
    2: dict(
        ans="（1）24　（2）6　（3）18",
        kp="直線排列，加上「指定位置」與「不在某位置」兩種限制（提示卡一）。"
           "(3) 是本課「『不』字走反面」的最基本一題。",
        fm="n 人排成一列 ＝ {n!}；指定某人在某位置 → 其餘 {(n-1)!}；"
           "某人不在某位置 ＝ {n!} − {(n-1)!}。",
        steps=["小問 (1)：四人任意排成一列 ＝ {4! = 4*3*2*1 = 24} 種。",
               "小問 (2)：「甲排首位」是指定位置：甲固定在第一位，"
               "其餘三人（乙、丙、丁）任意排 ＝ {3! = 6} 種。",
               "小問 (3)：「乙不排末位」走反面：全部 24 種，減去「乙排末位」的排法。"
               "乙固定在末位，其餘三人任意排 ＝ {3! = 6} 種 → 24 − 6 ＝ 18 種。",
               "小問 (3) 檢核（正面直接算）：末位有 3 個人可站（乙以外），"
               "末位定了之後其餘三個位置由剩下三人任意排 {3! = 6} → "
               "3 × 6 ＝ 18 ✔ 兩條路吻合。"],
        pit="① (3) 算成 24 − 1 ＝ 23 或 24 − 3 ＝ 21：要減的是「乙排末位」的"
            "完整排法數 {3! = 6}，不是 1 種，也不是 3 種。"
            "② (2) 答成 {4! = 24}：甲已經固定在首位，不可以再參與排列。"
            "③ 以為 (2) 與 (3) 的答案加起來會等於 (1)：兩者不是互補關係，"
            "與 (3) 互補的是「乙排末位」的 6 種。"),
    3: dict(
        ans="（1）60 個　（2）36 個",
        kp="有位置意義的排列（三位數，換位置就是另一個數），"
           "以及「限制落在個位」時要先排有限制的那個位置。",
        fm="{P(n,r)} ＝ 由 n 開始連乘 r 個因數；有限制的位置先排。",
        steps=["小問 (1)：從 5 個數字中選 3 個排成三位數，百位、十位、個位是三個不同的位置，"
               "換了位置就是另一個數 → 用排列。{P(5,3)=5*4*3=60} 個。",
               "小問 (2)：「奇數」的限制落在個位：個位必須是 1、3、5 其中一個 → 3 種選擇。",
               "小問 (2) 續：個位定了之後，百位與十位由剩下的 4 個數字選 2 個排列 ＝ "
               "{P(4,2)=4*3=12} 種。分步相乘：3 × 12 ＝ 36 個。",
               "檢核：偶數（個位是 2 或 4）＝ 2 × {P(4,2)} ＝ 2 × 12 ＝ 24 個；"
               "36 ＋ 24 ＝ 60，與 (1) 的總數吻合 ✔"],
        pit="① (1) 用了組合 {C(5,3)=10}：三位數換了位置就是另一個數，必須用排列。"
            "② (2) 先排百位、十位，最後才排個位：有限制的位置要先排，"
            "否則會出現「剩下的數字剛好沒有奇數」這種算不下去的情況。"
            "③ (2) 直接把 60 除以 2 得 30：5 個數字裡奇數有 3 個、偶數只有 2 個，"
            "不是一半一半。"),
    4: dict(
        ans="（a）10 種　（b）600 種",
        kp="(a) 是「必選」型組合——已定的部分先扣走，只算真正要決定的那幾個；"
           "(b) 是「不在某位置」的排列（提示卡一的反面走法）。",
        fm="{C(n,r)=frac(P(n,r),r!)}；某人不在某位置 ＝ {n!} − {(n-1)!}。",
        steps=["（a）菜單要 5 種菜色，其中 2 種已經必選、沒有選擇餘地。"
               "真正要決定的只是「剩下的 3 個名額由哪些菜色補上」。",
               "（a）從其餘 7 − 2 ＝ 5 種菜色中選 3 種；菜單上的菜色沒有先後之分 → "
               "用組合。{C(5,3)=frac(5*4*3,3*2*1)=frac(60,6)=10} 種。",
               "（b）六人任意排成一列 ＝ {6! = 720} 種；"
               "甲站在排頭時，其餘五人任意排 ＝ {5! = 120} 種。",
               "（b）甲不站排頭 ＝ 720 − 120 ＝ 600 種。"
               "檢核（正面）：排頭有 5 個人可站，其餘五個位置 {5! = 120} → "
               "5 × 120 ＝ 600 ✔"],
        pit="① (a) 算成 {C(7,5)=21}：那是「7 種隨便選 5 種」，"
            "完全沒有用上「2 種必選」這個條件。"
            "② (a) 在 10 之上再乘 2 或加 2：必選的兩種只有一種擺法，"
            "不會產生額外的選擇。"
            "③ (b) 答成 {5! = 120}：那是「甲站排頭」的排法，題目問的是相反。"
            "④ (b) 寫成 {6!} − 5 ＝ 715：要減的是完整排法數 {5! = 120}。"),
    5: dict(
        ans="（1）243 種　（2）211 種",
        kp="(1) 是「每件物品各自獨立選一個去向」的分配（不是排列也不是組合）；"
           "(2) 是「至少一件」，用補集（提示卡五）。",
        fm="m 件不同的東西分給 n 個人（容許有人分不到）＝ {n^m}；"
           "至少一個 ＝ 全部 −（一個都沒有）。",
        steps=["小問 (1)：每一塊蛋糕各自有 3 個去向（給 A、給 B 或給 C），"
               "五塊蛋糕互不影響 → 3 × 3 × 3 × 3 × 3 ＝ {3^5 = 243} 種。",
               "小問 (2)：「C 至少拿到一塊」的相反只有一種情況——「C 一塊都拿不到」，"
               "即五塊蛋糕全部只分給 A、B 兩人。",
               "小問 (2) 續：此時每塊蛋糕只有 2 個去向 → {2^5 = 32} 種。"
               "相減：243 − 32 ＝ 211 種。",
               "檢核：211 比 243 略少，合理——「C 完全拿不到」本來就是少數情況。"
               "另一條路（正面）：C 恰好拿 1 塊 {C(5,1)*2^4=5*16=80}、"
               "恰好 2 塊 {C(5,2)*2^3=10*8=80}、恰好 3 塊 {C(5,3)*2^2=10*4=40}、"
               "恰好 4 塊 {C(5,4)*2=5*2=10}、五塊全拿 1，"
               "合共 80 ＋ 80 ＋ 40 ＋ 10 ＋ 1 ＝ 211 ✔ 答案相同，但寫了五行。"],
        pit="① (1) 算成 {3! = 6} 或 {C(5,3)}：蛋糕不同、人也不同，"
            "而且一個人可以拿多塊，這既不是排列也不是組合，"
            "是「每件物品各自選一個去向」。"
            "② (1) 底數與指數對調寫成 {5^3 = 125}：底數是「去向數 3」，"
            "指數是「物品數 5」。"
            "③ (2) 減錯數：要減的是「只分給 A、B」的 {2^5 = 32}，不是 {3^4} 也不是 2 × 5。"
            "④ (2) 逐項相加時漏了「乘上其餘蛋糕的去向」——"
            "詳細步驟第 4 點示範了正面走法為何比補集長很多。"),
    6: dict(
        ans="（a）90 種　（b）R ＝ 4",
        kp="(a) 是「先組合、後圓排列」的兩步題；"
           "(b) 考組合數的對稱性質 {C(n,r)=C(n,n-r)}（講義範例B (c) 出現過）。",
        fm="n 人的圓排列 ＝ {(n-1)!}；{C(n,r)=C(n,n-r)}。",
        steps=["（a）第一步：從 6 人中選出 4 個人。誰跟誰一組沒有先後之分 → 用組合。"
               "{C(6,4)=C(6,2)=frac(6*5,2*1)=15} 種。",
               "（a）第二步：選中的 4 人圍圓桌坐。圓桌沒有頭尾，整體轉一格算同一種 → "
               "圓排列 ＝ {(4-1)!} ＝ {3! = 6} 種。",
               "（a）兩步都要做完才坐得成 → 分步相乘：15 × 6 ＝ 90 種。",
               "（b）兩邊的總數都是 10，選出的個數分別是 R ＋ 4 與 R − 2。"
               "兩個組合數相等只有兩種可能：選出的個數相同，"
               "或者兩個選出的個數「相加等於總數 10」。"
               "前者 R ＋ 4 ＝ R − 2 得 4 ＝ −2，不成立；"
               "所以（R ＋ 4）＋（R − 2）＝ 10 → 2R ＋ 2 ＝ 10 → R ＝ 4。",
               "（b）檢核：R ＝ 4 時 R ＋ 4 ＝ 8、R − 2 ＝ 2，"
               "{C(10,8)=C(10,2)=45}，兩邊相等 ✔ "
               "而且 8 與 2 都落在 0 至 10 之間，是合法的選取個數。"],
        pit="① (a) 只算了 {C(6,4)=15} 或只算了 {3! = 6}：兩步都要做才坐得成。"
            "② (a) 把圓排列當成直排 {4! = 24}，答案變成 360——"
            "圓桌轉一格是同一種坐法，要用 {(n-1)!}。"
            "③ (b) 只寫「兩個選出的個數相等」一條路就收工："
            "一定要同時檢查「相加等於總數」那一條，本題正是靠它。"
            "④ (b) 求出 R 之後沒有回頭檢查 R ＋ 4 與 R − 2 是否落在 0 至 10 之間；"
            "超出範圍的解要捨去。"),
}


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para("題幹裡已用引號把關鍵字標出，每題下方寫明了查到對譯表哪一條、"
                  "該翻哪一張提示卡。先照着做一次，感受一下三步的節奏。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(shaded_box(CARD_HINT[n]))
        P += write_lines(LINES[n])
        P.append(blank())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(shaded_box(TRIG_LIST))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
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

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ================================================================ 工具卡
# 前五張＝講義那五張 D7 提示卡的桌面版；第六張是「動筆前的三個問題」速查。
# 卡片不用 OMML 分數（分數會疊高行距，六張卡就入不到一頁，L4 實測），
# 但一定要留幾條 {} 標記的短式，否則 m:oMath ＝ 0 會 QB-2 FAIL（L8 實測）。
TC_TEXT = [
    ("▍卡一・特殊位置優先", "題目說「必須站在頭／尾／中間」或「不站在某位置」。",
     ["有限制的位置先安排，其餘的人後排",
      "指定某人在某位置：其餘 {(n-1)!}",
      "某人不在某位置：{n!} 減 {(n-1)!}",
      "※「不」字幾乎一定用減法走反面"]),
    ("▍卡二・捆綁法（必須相鄰）", "題目說「必須相鄰」「坐在一起」「不能分開」。",
     ["要黏在一起的綁成「一件」，當一個單位排",
      "k 人綁埋、其餘 m 人：{(m+1)!} 乘 {k!}",
      "例：［甲乙］丙 丁 戊 ＝ 4 個單位",
      "※ 最常漏：綁在一起那幾個自己也要排"]),
    ("▍卡三・插空法（不相鄰）", "題目說「不相鄰」「不能挨着」「要隔開」。",
     ["先排沒限制的人，再把要隔開的插進空位",
      "☐ 甲 ☐ 乙 ☐ 丙 ☐ ＝ 3 人 4 個空位",
      "先排 m 人 {m!}，再插 k 人 {P(m+1,k)}",
      "※ 只隔開兩個人時，「全部減相鄰」更快"]),
    ("▍卡四・重複元素", "要排的東西裡面有一模一樣的（重複字母、同款球）。",
     ["先當全部不同排好，再除走重複的倍數",
      "n 件、p 件相同、q 件相同：n! ÷ (p! × q!)",
      "例：mhchcm → 6! ÷ (2! × 2! × 2!) ＝ 90",
      "※ 每一種重複各除一次，不要只除一次"]),
    ("▍卡五・補集法（至少）", "題目出現「至少一個」「不都是」「並非全部」。",
     ["至少一個 ＝ 全部 −（一個都沒有）",
      "正面逐個情況數，又長又容易漏",
      "例：5 個答案至少一個對 ＝ {2^5} 減 1 ＝ 31",
      "※ 另記：n 人圍圓桌 ＝ {(n-1)!}"]),
    ("▍速查・動筆前的三個問題", "每一題動筆之前掃一次，三個問題的次序不可調亂。",
     ["① 這一步做完，事情完成了？完成＝加；未完成＝乘",
      "② 兩個對象調轉是同一件事？是＝C；不是＝P",
      "③ 有「必須／不能／至少／重複／圓桌」？有＝翻卡",
      "※ 換另一條路再算一次，是唯一的檢查方法"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in TC_TEXT:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        c += [para("・" + t, sz=21) for t in items]
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


def _head(tpl, title, extra_css):
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", title)
    return head.replace("</head>", "<style>\n%s\n</style>\n</head>" % extra_css)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = _head(tpl, "練習：" + UNIT, """
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
""")

    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂練習</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')
    parts.append('<div class="hint-card">%s</div>' % _h(HINT_TOP))

    parts.append('<div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>')
    parts.append('<div>題幹裡已用引號把關鍵字標出，每題下方寫明了查到對譯表哪一條、'
                 '該翻哪一張提示卡。先照着做一次，感受一下三步的節奏。</div>')
    for n in A_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>'
                     '<div class="hint-card">%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _h(CARD_HINT[n]), _lines(LINES[n])))

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div class="hint-card">%s</div>' % _h(TRIG_LIST))
    for n in B_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _lines(LINES[n])))

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>%s</div>' % _h(C_LEAD))
    for n in C_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s</div>'
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
           "".join('<div class="i">・%s</div>' % _h(t) for t in items))
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
