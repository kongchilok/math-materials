# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L10 排列與組合 —— 課堂講義 build script

主設計 D8 關鍵字對譯表（兩張表：原理判斷／陷阱詞；範例題的關鍵字逐句對照）；
輔助 D1 樹狀圖（只在範例A 出現一次，把「為什麼相乘」看個明白，之後褪除）、
D7 提示卡（五招：特殊位置優先／捆綁／插空／重複元素／補集，是工具卡的本體）。
鷹架密度：抽離小班 (Tier 2)。

產出：講義_排列與組合_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）

注意（前幾課踩過的坑，改本檔時照跟）：
1. `{...!=...}` 會被 omml_core 的 _PREPROC 轉成 ≠ ——階乘後面的等號一定要留空格：
   寫 `{5! = 120}`，不要寫 `{5!=120}`。
2. 不要用 `**markdown 粗體**`，docx 端會原樣印出星號。強調用「」或 ※。
3. 標記字元只用 CLAUDE-DETAILED 實測清單：①②③④／ⓐⓑⓒⓓ／☐／★☆／※／⚠／▍／→。
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

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_排列與組合_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L10 排列與組合"
FOOT = "高三數學．" + UNIT

# ================================================================ 圖（D1 樹狀圖）
# 範例A(a) 的縮小版：甲→乙 3 條路、乙→丙 2 條路，數得完，看得見「相乘」怎樣來。
FIG_TREE = ds.tree_diagram(
    [{"label": "乙地", "p": "路 1",
      "children": [{"label": "丙地", "p": "路 A"}, {"label": "丙地", "p": "路 B"}]},
     {"label": "乙地", "p": "路 2",
      "children": [{"label": "丙地", "p": "路 A"}, {"label": "丙地", "p": "路 B"}]},
     {"label": "乙地", "p": "路 3",
      "children": [{"label": "丙地", "p": "路 A"}, {"label": "丙地", "p": "路 B"}]}],
    width=440, root="甲地", title="縮小版：甲→乙 3 條、乙→丙 2 條，共 3 × 2 ＝ 6 條路線")

# ================================================================ 文字內容
INTRO = [
    "排列組合的題目讀起來全部都像生活小事：排隊照相、選班代表、分蛋糕、"
    "揀便當配菜。真正難的地方不在計算——由頭到尾只是把幾個數相加或相乘——"
    "而在「認不出應該用哪一招」。",
    "所有判斷都藏在題目的用字裡面。「先…再…」與「或者…或者…」只差幾個字，"
    "一個要相乘、一個要相加；「選出正、副班長」與「選出兩位代表」同樣是"
    "十個人裡面揀兩個，答案卻剛好差一倍。認錯了，後面計得再準都是零分。",
    "所以本課的主工具是一張關鍵字對譯表：左邊是題目會出現的字眼，"
    "右邊是它對應的數學動作。做題的次序固定為三步——"
    "① 在題目上圈出關鍵字 → ② 對照表格決定用哪一招 → ③ 才動筆計算。"
    "圈關鍵字這一步不要省，本課九成的錯都是在這一步之前就已經注定。",
    "另外配一套五張提示卡，專門處理「必須／不能／至少／重複／圍圓桌」"
    "這些附加條件；還有一張樹狀圖，用來把「為什麼是相乘」看個明白，"
    "它只在第一個範例出現一次，之後就收起來。",
]

# ---------------------------------------------------------------- D8 對譯表
KW_GENERAL = [
    ("「先…再…」「接着」「然後」", "分步：兩件事都做完才算完成 → 各步的方法數相「乘」"),
    ("「或者…或者…」「四類裡面揀一部」", "分類：做完其中一類就完成 → 各類的方法數相「加」"),
    ("「排成一列」「照相」「排隊」「名次」", "位置有先後 → 用排列 {P(n,r)}"),
    ("「正、副班長」「三位數」「第一名、第二名」", "位置有先後 → 用排列 {P(n,r)}"),
    ("「選出 2 人做代表」「組成一隊」「揀 3 種配菜」", "沒有先後 → 用組合 {C(n,r)}"),
    ("「對角線」「握手」「兩點連一條線」", "兩點一條、調轉一樣 → 用組合 {C(n,r)}"),
    ("「數字可以重複使用」", "每一位都仍然有全部選擇 → 直接連乘，不是排列"),
    ("「每人各點一個」（人是分得開的）", "每個人獨立選一次 → 連乘"),
]
KW_TRAPS = [
    ("「至少有一個…」", "全部 −（一個都沒有）。不要逐個情況加起來，又漏又重"),
    ("「必須相鄰」「要坐在一起」", "捆綁法：先綁成一件排，排完再乘綁在一起那幾個的內部排法"),
    ("「不相鄰」「不能挨着」", "全部 −（相鄰的）；或者用插空法"),
    ("「甲不站在排頭」", "全部 −（甲站在排頭的）。「不」字幾乎一定用減"),
    ("「圍圓桌坐」", "圓桌沒有頭尾，轉一格算同一種 → n 人的圓排列 ＝ {(n-1)!}"),
    ("要排的東西有重複（同樣的字母）", "先當全部不同排好，再除以每種重複個數的階乘"),
]
KW_NOTE = ("※ 用法示範。讀「甲、乙、丙三人到速食店，該店只提供三種套餐，每人各點一套餐，"
           "共有多少種點餐方式？」時，圈出來的字是「每人各點一個」——"
           "查表得「每個人獨立選一次 → 連乘」，於是寫 3 × 3 × 3 ＝ 27，"
           "不必想是排列還是組合。"
           "⚠ 表的左欄是「題目說什麼」，不是「題目在講什麼」。"
           "不要看到「三人」就找 3、看到「三種」就找 3——要找的是那幾個關係詞。")

# ---------------------------------------------------------------- 範例A
EX_A = ("【範例A・分類還是分步】"
        "（a）甲地到乙地有陸路 3 條、水路 2 條；乙地到丙地有陸路 2 條、水路 2 條。"
        "某人由甲地經乙地「再」到丙地，總共有幾種不同走法？　"
        "（b）DVD 架上有恐怖類 5 片、愛情類 3 片、科幻類 2 片、搞笑類 4 片。"
        "只選一部影片，有多少種選法？")
A_TXT = [
    "（a）這一題有「兩個層次」，要分開處理，不可以把所有數字排成一行就算。",
    "第一層——甲地到乙地：走陸路「或者」走水路，走了其中一條就到了乙地。"
    "查表：或者 → 分類 → 相加。合共 3 ＋ 2 ＝ 5 條。"
    "同樣地，乙地到丙地合共 2 ＋ 2 ＝ 4 條。",
    "第二層——甲 → 乙「再」→ 丙：只走完前半段還未到丙地，兩段都要走完才算完成。"
    "查表：先…再… → 分步 → 相乘。答案 5 × 4 ＝ 20 種。",
    "（b）選恐怖類「或者」愛情類「或者」科幻類「或者」搞笑類，"
    "揀完一部就完成，不必再揀第二部。"
    "查表：或者 → 分類 → 相加。答案 5 ＋ 3 ＋ 2 ＋ 4 ＝ 14 種。",
]
TREE_CAP = ("下圖把 (a) 縮小成「甲→乙 3 條、乙→丙 2 條」來數。"
            "由甲地出發，無論選了哪一條路到乙地，之後仍然有 2 條路可以去丙地，"
            "所以 3 條各自再分岔成 2 條，數一數枝末端共 6 條完整路線——"
            "「相乘」就是這樣來的，不是死記的公式。"
            "真題的 5 條與 4 條完全同一個道理，只是畫出來線太多。")
NOTE_A = ("※ 分辨分類與分步只有一句話：做完這一步，事情完成了沒有？"
          "完成了就是分類（相加）；未完成、還要接着做下一步就是分步（相乘）。"
          "(b) 揀完一部影片就完成 → 相加；(a) 只到了乙地還未到丙地 → 相乘。"
          "※ (a) 最常見的兩個錯法：寫成 3 ＋ 2 ＋ 2 ＋ 2 ＝ 9，或寫成 "
          "3 × 2 × 2 × 2 ＝ 24。兩個都是把「層次之內」與「層次之間」混在一起了。"
          "正確次序永遠是：先在每個層次「之內」相加，再把層次「之間」相乘。")

# ---------------------------------------------------------------- 範例B
EX_B = ("【範例B・有先後，還是沒有先後】某班有 10 位同學。"
        "（a）選出正班長、副班長各一人，有多少種選法？　"
        "（b）選出 2 人做代表出席會議，有多少種選法？　"
        "（c）另一隊排球隊共有 10 位選手，任選 6 人上場比賽，有多少種不同方法？")
B_TXT = [
    "（a）正班長與副班長是兩個「不同」的職位：甲做正、乙做副，"
    "跟乙做正、甲做副，是兩件不同的事。有先後 → 用排列。"
    "{P(10,2)=10*9=90} 種。（第一個位置有 10 個人可選，選走一個之後第二個位置剩 9 個。）",
    "（b）兩位代表地位相同：代表是甲和乙，跟代表是乙和甲，是同一件事。"
    "沒有先後 → 用組合。{C(10,2)=frac(10*9,2*1)=45} 種。"
    "※ 剛好是 (a) 的一半——因為 (a) 把「甲正乙副」與「乙正甲副」數成兩次，"
    "(b) 只算一次，所以要除以 {2! = 2}。",
    "（c）六位上場球員之間沒有先後之分 → 用組合。"
    "{C(10,6)=C(10,4)=frac(10*9*8*7,4*3*2*1)=frac(5040,24)=210} 種。"
    "※ 這裡用了一條省時間的性質：{C(n,r)=C(n,n-r)}。"
    "選 6 個上場，等於選 4 個不上場，兩件事一一對應，所以兩個數必然相等。"
    "算 {C(10,4)} 比 {C(10,6)} 少寫兩個因數，答案一樣。",
]
NOTE_B = ("※ 判斷有序無序，只用這個測試：把答案裡的兩個對象調轉，看看是不是同一件事。"
          "「甲正乙副」↔「乙正甲副」是兩件事 → 有先後 → 用 {P(n,r)}；"
          "「代表是甲、乙」↔「代表是乙、甲」是同一件事 → 沒有先後 → 用 {C(n,r)}。"
          "※ 兩者的關係是 {C(n,r)=frac(P(n,r),r!)}。"
          "除掉的那個 {r!} 就是「把選中的 r 個排先後」的方法數；"
          "組合不理先後，所以要把重複數了的排法除走。"
          "※ 考卷上的寫法可能是 {C_10^6}（C 下面是總數、上面是選出的個數），"
          "也見過上下對調的寫法。看哪一個數大就知道那個是總數；"
          "自己寫的時候用 {C(10,6)} 這種括號寫法最不易搞亂。")

# ---------------------------------------------------------------- D7 五張提示卡
CARDS_D7 = [
    dict(title="提示卡一・特殊位置優先",
         trigger="題目說「必須站在排頭／排尾／中間」，或者「某人不站在某個位置」。",
         statement="有限制的位置最挑剔，所以先安排它，再排其餘的人。"
                   "如果限制是「不」字（不站在排頭），走反面更快："
                   "用全部的排法減去「站在排頭」的排法。",
         formula="指定某人在某位置：其餘 {(n-1)!}　｜　"
                 "某人不在某位置：{n!} − {(n-1)!}"),
    dict(title="提示卡二・捆綁法（必須相鄰）",
         trigger="題目說「甲、乙必須相鄰」「要坐在一起」「不能分開」。",
         statement="把要黏在一起的人用繩綁成「一件」，當成一個單位，"
                   "跟其餘的人一起排。排完之後，不要忘記綁在一起的那幾個人"
                   "自己也可以左右對調——這一步是全班最常漏的一步。",
         formula="k 個人綁在一起、其餘 m 個人：{(m+1)!} × {k!}　"
                 "（例：［甲乙］丙 丁 戊 ＝ 4 個單位）"),
    dict(title="提示卡三・插空法（不相鄰）",
         trigger="題目說「不相鄰」「不能挨着」「要隔開」。",
         statement="先把沒有限制的人排好，他們之間連同兩端會出現一排空位，"
                   "再把要隔開的人插進「不同」的空位，自然就不會挨在一起。"
                   "空位的數目是人數加一：☐ 甲 ☐ 乙 ☐ 丙 ☐ ＝ 3 人 4 個空位。",
         formula="先排 m 人 {m!}，出現 {(m+1)} 個空位，插入 k 人 {P(m+1,k)}"),
    dict(title="提示卡四・重複元素",
         trigger="要排的東西裡面有一模一樣的（重複的字母、同款的球）。",
         statement="先假裝它們全部不同，照普通排列排好；"
                   "但兩個一模一樣的東西互調位置，排出來的樣子沒有變，"
                   "剛才等於重複數了一次，所以要把重複的次數除走。",
         formula="共 n 件、其中甲類 p 件相同、乙類 q 件相同："
                 "{frac(n!,p!q!)}　（每一種重複各除一次階乘）"),
    dict(title="提示卡五・補集法（至少）",
         trigger="題目出現「至少一個」「不都是」「並非全部」。",
         statement="正面逐個情況數（恰好 1 個、恰好 2 個…）又長又容易漏；"
                   "反過來想，「至少一個」的相反只有一種情況——「一個都沒有」。"
                   "用全部減掉它，一行就寫完。",
         formula="至少一個 ＝ 全部 −（一個都沒有）"),
]

# ---------------------------------------------------------------- 範例C
EX_C = ("【範例C・排列的三招】"
        "（a）5 人排成一排照相，甲不站在排頭（左），有多少種排法？　"
        "（b）將 A、B、C、D、E 五人排成一列，A、C 必須相鄰，有多少種排法？　"
        "（c）同樣是這五人，B、E 不相鄰，有多少種排法？")
C_TXT = [
    "（a）關鍵字「不站在」→ 翻提示卡一，走反面。"
    "五人任意排列共 {5! = 5*4*3*2*1 = 120} 種；"
    "甲站在排頭時，其餘四人任意排 {4! = 24} 種；"
    "所以甲不站排頭 ＝ 120 − 24 ＝ 96 種。",
    "（a）另一條路（正面直接算）：排頭的位置只有甲以外的 4 個人可站，"
    "排頭定了之後，其餘四個位置由剩下的四人任意排 {4! = 24} 種 → "
    "4 × 24 ＝ 96 種。兩條路答案相同 ✔",
    "（b）關鍵字「必須相鄰」→ 翻提示卡二，捆綁。"
    "把 A、C 綁成一件，連同 B、D、E 一共 4 個單位排成一列：{4! = 24} 種；"
    "綁在一起的 A、C 自己還可以左右對調：{2! = 2} 種。"
    "答案 24 × 2 ＝ 48 種。",
    "（c）關鍵字「不相鄰」→ 翻提示卡三，插空。"
    "先排沒有限制的 A、C、D 三人：{3! = 6} 種；"
    "他們排好後出現 4 個空位（☐ A ☐ C ☐ D ☐）；"
    "把 B、E 插進其中兩個「不同」的空位，而且 B 前 E 後與 E 前 B 後是兩件事 → "
    "{P(4,2)=4*3=12} 種。答案 6 × 12 ＝ 72 種。",
    "（c）另一條路（補集）：全部 120 − B、E 相鄰的排法。"
    "相鄰用捆綁：{4! = 24} 乘內部 {2! = 2} ＝ 48 → 120 − 48 ＝ 72 種 ✔ "
    "兩條路答案相同。",
]
NOTE_C = ("※ (b) 全班最常漏的是最後那個「× 2」。綁在一起之後，"
          "A 在左 C 在右、與 C 在左 A 在右，是兩張不同的相片。"
          "對策：一綁完就立刻在旁邊寫低「內部 {2!}」四個字，計完再乘回去。"
          "※ (c) 兩條路都要學會。要隔開的只有兩個人時，用補集（全部減相鄰）比較快；"
          "但要隔開的人多過兩個時，「相鄰」本身會分成很多種情況，補集反而更亂，"
          "那時一定要用插空法。"
          "※ (a) 的兩條路提醒一件事：排列組合的答案只是一個數字，"
          "看不出對錯，所以「換另一條路再算一次」是本課唯一可靠的檢查方法。")

# ---------------------------------------------------------------- 範例D
EX_D = ("【範例D・組合的應用】"
        "（a）求正二十九邊形的對角線共有幾條？　"
        "（b）某自助餐店的 80 元便當，除白飯外包含一種主菜以及三種不同的配菜。"
        "今日的主菜有雞腿、排骨、魚排 3 種，另有 8 種不同的配菜，"
        "共可搭配出多少種不同的便當？")
D_TXT = [
    "（a）先想清楚對角線是什麼：連接「兩個不相鄰頂點」的線段。"
    "關鍵字「兩點連一條線」→ 沒有先後（由 A 連到 B 與由 B 連到 A 是同一條）→ 用組合。",
    "（a）第一步，數出所有連線：由 29 個頂點中任選 2 個連起來，"
    "{C(29,2)=frac(29*28,2*1)=frac(812,2)=406} 條。"
    "第二步，這 406 條裡面包括了多邊形本身的 29 條邊，邊不是對角線，要減走："
    "406 − 29 ＝ 377 條。"
    "（課本另一條公式 {frac(n(n-3),2)=frac(29*26,2)=377}，結果相同。）",
    "（b）這是本課最典型的「混合題」，要一層一層拆開，每層各自判斷。"
    "第一層：主菜 3 選 1 → 3 種。"
    "第二層：配菜從 8 種選 3 種，三種配菜放進同一個便當盒，沒有先後 → "
    "{C(8,3)=frac(8*7*6,3*2*1)=frac(336,6)=56} 種。",
    "（b）第三層：主菜與配菜「都要有」才成為一個便當 → 分步 → 相乘。"
    "答案 3 × 56 ＝ 168 種。",
]
NOTE_D = ("※ (b) 若把配菜寫成 {P(8,3)=336}，答案會變成 3 × 336 ＝ 1008，錯。"
          "判斷法還是那一句：把三種配菜調轉次序，還是同一個便當 → 沒有先後 → 用 C。"
          "※ (a) 提醒一件事：題目問的東西（對角線）與公式直接算到的東西（所有連線）"
          "不一定是同一樣。先算得到的那樣，再加或減修正到題目要的那樣，"
          "是排列組合很常用的一步。"
          "※ 混合題的處理次序：先把題目拆成幾層 → 每層各自判斷用加、用乘、用 P 還是用 C → "
          "最後才把各層的結果按分類或分步合起來。")

# ---------------------------------------------------------------- 範例E
EX_E = ("【範例E・三種特殊型】"
        "（a）將 m、h、c、h、c、m 這六個英文字母任意排列，共有幾種不同的排列方法？　"
        "（b）四個人圍着圓形檯坐，有幾種坐法？　"
        "（c）一條多選題有 A、B、C、D、E 五個答案，"
        "如果至少有一個答案是對的，共有多少種作答方式？")
E_TXT = [
    "（a）看到重複的字母 → 翻提示卡四。六個字母裡 m 有 2 個、h 有 2 個、c 有 2 個。"
    "先當六個全部不同：{6! = 720} 種。"
    "但兩個 m 互調之後排出來的字串完全一樣，等於每一種排法都被重複數了 {2!} 次；"
    "h 與 c 同理。所以 {frac(720,2!*2!*2!)=frac(720,8)=90} 種。",
    "（b）關鍵字「圍圓桌」→ 查對譯表的陷阱詞。"
    "圓桌沒有頭尾，四個人整體轉一格，誰坐在誰的左邊完全沒有變，應當算同一種坐法。"
    "做法：先固定其中一個人（就當他坐在靠門那一邊），"
    "其餘 3 人在他左右順序排開 → {3! = 6} 種。"
    "一般寫成 n 人的圓排列 ＝ {(n-1)!}。",
    "（c）關鍵字「至少有一個」→ 翻提示卡五，走反面。"
    "每個答案只有兩種命運：是對的、不是對的。"
    "五個答案各自兩種 → {2^5 = 32} 種情況。"
    "其中「五個都不是對的」這 1 種不符合「至少有一個是對的」，減走："
    "32 − 1 ＝ 31 種。",
]
NOTE_E = ("※ (c) 正面數也做得到，但寫得長：恰好 1 個對 {C(5,1)=5}、"
          "恰好 2 個 {C(5,2)=10}、恰好 3 個 10、恰好 4 個 5、五個全對 1，"
          "合共 5 ＋ 10 ＋ 10 ＋ 5 ＋ 1 ＝ 31 ✔ 答案一樣，但寫了五行，"
          "而且很容易漏其中一行。「全部 −（一個都沒有）」一行就完，這就是補集法的價值。"
          "※ (b) 直排與圓排差在哪：四人直排是 {4! = 24}，圓排是 {3! = 6}，"
          "剛好是 24 ÷ 4。因為圓桌轉四格才轉回原位，"
          "每一種坐法都被直排的算法重複數了 4 次。"
          "※ (a) 與 (b) 其實是同一個念頭：先照普通方法算，發現重複數了，就除走重複的倍數。")

# ---------------------------------------------------------------- 總結表
SUM_HEAD = ("動筆前先問自己", "看答案是哪一邊", "就用這一招")
SUM_ROWS = [
    ("① 做完這一步，事情完成了沒有？",
     "完成了 ＝ 分類｜未完成、還要接着做 ＝ 分步",
     "分類：各類方法數相「加」｜分步：各步方法數相「乘」"),
    ("② 把答案裡的兩個對象調轉，是不是同一件事？",
     "不是同一件事 ＝ 有先後｜是同一件事 ＝ 沒有先後",
     "有先後用 {P(n,r)}｜沒有先後用 {C(n,r)}"),
    ("③ 有沒有「必須／不能／至少／重複／圍圓桌」？",
     "有 ＝ 要加招｜沒有 ＝ 直接算",
     "卡一位置｜卡二捆綁｜卡三插空｜卡四重複｜卡五至少"),
]

# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D8 關鍵字對譯表——兩張表分開列（一般對譯 8 條／陷阱詞 6 條），"
                "照 teaching-designs.md 對 D8 的規範「兩類條目不可混列」施工。"
                "五個範例的解說一律由「圈出關鍵字 → 查表 → 才計算」三步展開，"
                "把對譯表在正文裡實際用五次，而不是印一張表就算",
    aux_designs=("D1 樹狀圖——只在範例A 出現一次（S7 的建議輔助「D1 條形模型／樹狀圖」）。"
                 "刻意把真題的 5×4 縮小成 3×2 才畫得完，讓學生「數得完枝末端」，"
                 "親眼見到 6 條路線＝3 個分枝各自再分 2 枝，"
                 "把乘法原理由公式還原成可數的事實；之後全課不再出現",
                 "D7 提示卡——五張（特殊位置優先／捆綁／插空／重複元素／補集），"
                 "每張都寫明觸發語「什麼時候翻我」，並且是工具卡的本體。"
                 "五張卡對應的正是對譯表「陷阱詞」那半張表：表負責認出、卡負責處理"),
    reason=(
        "本課取 A2 排列組合機率 86 題的上半（計數原理、排列、組合、"
        "分配與特殊型），機率與二項式定理留給 L11。"
        "對照 LOGIC1-028、LOGIC2-045／046／048、MATH-026、"
        "MOCK1-045／047／049／050／052、MOCK2-085／125／126／127／165／166、"
        "MOCK3-042、COMP1-048 等題。"
        "數學結構取 teaching-designs.md §1 的 S7（機率與統計族），"
        "瓶頸「冗長文字敘述＋語言陷阱」，建議主設計 D8——本課完全照表取用，未自創。"
        "選 D8 而不是 D2 手順卡的理由：排列組合的計算本身只有一兩步（乘幾個數、"
        "除一個階乘），程序長度不是瓶頸，D2 無用武之地；"
        "真正的失分點在動筆之前——「分類還是分步」「有先後還是沒有先後」"
        "「有沒有附加條件」三個判斷全部由題目的關係詞決定，"
        "這正是 D8 的問題陳述（文字→算式的詞彙層轉換）。"
        "同一批十個人選兩個，問法一變答案就差一倍，正是本課要學生親身踩一次的地方"
        "（範例B）。三種設計＝主 D8 ＋ 輔 D1、D7，未超過「主1＋輔2」上限；"
        "刻意沒有再加 D12 自我核對清單，以免超標。"),
    density="抽離小班（Tier 2）",
    fading=(
        "關鍵字對譯（D8）：講義正文每個範例都先圈關鍵字再查表 → "
        "練習A 題幹已把關鍵字用「」標好，並在下方寫明查到的是哪一條 → "
        "練習B 只在區塊開頭重印陷阱詞那半張表，題幹不再標 → "
        "練習C 完全不標，要自己圈 → 之後只留一句「先圈關鍵字」→ 完全移除。｜"
        "樹狀圖（D1）：講義範例A 給完整的樹 → 練習A 第 1 題只提示「不肯定就先畫兩層樹」 → "
        "練習B 起不再提 → 移除。｜"
        "提示卡（D7）：講義印五張完整卡（觸發語＋敘述＋公式），另出工具卡放桌面 → "
        "練習A 每題標明該翻哪一張 → 練習B 只列五個觸發語（必須／不能／至少／重複／圓桌）→ "
        "練習C 收起工具卡 → 之後只留一句「有沒有附加條件？」→ 完全移除。"),
    flows=("F5 課前流程預告（今天五件事：對譯表 → 範例A 分類與分步 → 範例B 排列與組合的分界 → "
           "五張提示卡＋範例C 三招 → 範例D、E 混合題與特殊型 → 練習A／B／C）",
           "F2 番茄鐘分段（「加還是乘」（對譯表＋範例A）、「P 還是 C」（範例B、D）、"
           "「五張卡」（範例C、E）三塊各自是一段，每段之間停一次）",
           "F4 過程導向回饋與分步計分（每題把「圈對關鍵字」「選對招式」「算式列對」"
           "「算出數值」分四步各給分——本課學生最常見的情況是招式選對而乘除算錯，"
           "或反過來算術無誤而一開始就選錯招，兩者要分開評價，對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（對譯表與五張提示卡即為此項；"
               "本課的判斷全靠關係詞，若獲准帶入測考，建議把對譯表寫進 IEP 第 9 點）",
               "a5 放大字體",
               "a6 增加行距／放大作答欄",
               "a7 調整計分標準（圈關鍵字／選招式／列算式／算數值分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("符號寫法的決定",
            "題庫原稿的組合符號本身不一致（LOGIC2-044 寫 C 下標 10 上標 R+4，"
            "MOCK2-175 卻寫成上標 33），學生照抄必然混亂。"
            "本課一律用括號寫法 {C(n,r)}、{P(n,r)} 作為書寫標準，"
            "並在範例B 的灰框明示考卷可能出現的上下標寫法與辨認方法"
            "（看哪一個數大，大的就是總數）。"
            "L11 機率與二項式定理沿用同一套寫法，不要中途改。"),
           ("與 L11 的分工",
            "A2 排列組合機率 86 題拆兩課。本課（L10）做計數原理、排列、組合、"
            "重複元素、圓排列與補集法；L11 做古典機率、獨立事件、"
            "「至少一科合格」型、二項機率與二項式定理展開。"
            "本課的 {C(n,r)} 與補集法是 L11 的直接先備知識，"
            "尤其補集法在 L11 會原封不動再用一次（「最少一科合格」＝1 −（全部不合格）），"
            "所以提示卡五在 L11 不要褪除，要留到 L11 結束。"),
           ("刻意避開的內容",
            "①隔板法（COMP1-075「30 顆糖分給 5 人每人至少 3 顆」）："
            "隔板法是另一個完整的招式，塞進本課會令提示卡變成六張，超出桌面卡的容量。"
            "②第二類 Stirling 數（MATH-019／MOCK2-015／MOCK2-079「書全部分完且每人至少一本」）："
            "超出課程範圍。③正方體塗色（MOCK2-124）要處理 24 種旋轉對稱，"
            "與本課的關鍵字判斷無關。④鴿籠原理（LOGIC2-019／020）不屬排列組合公式，"
            "建議另行處理或撥入綜合演練。以上四項已列入交付摘要的剔除清單。"),
           ("題量說明",
            "本課練習共 6 題（練習A／B／C 各 2 題），合共 13 個小問，"
            "涵蓋乘法原理（獨立選擇與順序安排兩種）、排列的三招（指定位置／不在某位置／"
            "相鄰／不相鄰）、有條件的三位數、組合的直接應用與「必選」型、"
            "重複分配的「至少」型、圓排列，以及組合數性質 {C(n,r)=C(n,n-r)} 的反解。"),
           ("配套文件",
            "《第2章 L10 排列與組合　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L10 排列與組合　工具卡》"
            "（五張招式提示卡 ＋ 一張「動筆前的三個問題」速查卡，剪下護貝放桌面）。")),
)


# ================================================================ docx
def build_docx_file():
    figdir = os.path.join(HERE, "_figtmp")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()

    png = os.path.join(figdir, "tree.png")
    ds.svg_to_png(FIG_TREE, png, scale=3)
    tree_img = image_para(png, width_cm=11.5)

    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、關鍵字對譯表（本課的主工具）", page_break_before=True))
    P.append(para("左欄是題目會出現的字眼，右欄是它對應的數學動作。"
                  "上半張是一般對譯，照字面翻就對；"
                  "下半張是陷阱詞，不可以照字面翻，要多想一步。"))
    P.append(keyword_table(KW_GENERAL, KW_TRAPS))
    P.append(shaded_box(KW_NOTE))

    P.append(heading("三、範例A・分類還是分步", page_break_before=True))
    P.append(problem_box([para(EX_A)]))
    for t in A_TXT:
        P.append(para(t))
    P.append(para(TREE_CAP))
    P.append(expand_image(tree_img, MEDIA))
    P.append(shaded_box(NOTE_A))

    P.append(heading("四、範例B・有先後，還是沒有先後", page_break_before=True))
    P.append(problem_box([para(EX_B)]))
    for t in B_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_B))

    P.append(heading("五、五張招式提示卡", page_break_before=True))
    P.append(para("對譯表下半張的陷阱詞負責「認出來」，這五張卡負責「怎樣做」。"
                  "每張卡最上面都寫了「什麼時候翻我」。"
                  "五張卡另外印成工具卡，剪下放在桌面，做題時用手指指住正在用的那一張。"))
    for c in CARDS_D7:
        P.append(reference_card(c["title"], c["trigger"], c["statement"],
                                formula=c["formula"]))
        P.append(blank())

    P.append(heading("六、範例C・排列的三招", page_break_before=True))
    P.append(problem_box([para(EX_C)]))
    for t in C_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_C))

    P.append(heading("七、範例D・組合的應用與混合題", page_break_before=True))
    P.append(problem_box([para(EX_D)]))
    for t in D_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_D))

    P.append(heading("八、範例E・三種特殊型", page_break_before=True))
    P.append(problem_box([para(EX_E)]))
    for t in E_TXT:
        P.append(para(t))
    P.append(shaded_box(NOTE_E))

    P.append(heading("九、動筆前的三個問題（做每一題之前掃一眼）",
                     page_break_before=True))
    P.append(para("這三個問題的次序不可以調亂：先定加還是乘，再定 P 還是 C，"
                  "最後才處理附加條件。"
                  "次序錯了會出現「用對了公式但整題架構錯」這種最難自己發現的錯。"))
    P.append(three_column_table(SUM_ROWS, headers=SUM_HEAD, row_h=1100))

    P.append(heading("十、接下來"))
    P.append(para("請拿出《第2章 L10 排列與組合　課堂練習》，"
                  "並把《工具卡》剪下放在桌面。"
                  "練習A 已經把關鍵字標好、也寫明查到哪一條；"
                  "練習B 只重印五個觸發語；練習C 完全不提示，要自己圈關鍵字。"
                  "無論哪一節，動筆之前都先走完上面那三個問題。"))

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
    # 純數字分數：a/b → \frac；階乘後的 ! 不可被吃掉，所以先擋住 `!` 開頭的情況
    body = re.sub(r"(?<![\\{\w.!])(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)(?![}\w.])",
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


def _kw_html(general, traps):
    rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (_h(k), _h(v))
                   for k, v in general)
    rows += ('<tr class="trap"><td colspan="2">'
             '⚠ 陷阱詞（要想一下，不能直接照字面翻）</td></tr>')
    rows += "".join("<tr><td>%s</td><td>%s</td></tr>" % (_h(k), _h(v))
                    for k, v in traps)
    return ('<table class="d-tbl kw-table"><thead><tr><th>題目說…</th>'
            '<th>就寫成…</th></tr></thead><tbody>%s</tbody></table>' % rows)


def _refcard_html(c):
    return ('<div class="ref-card"><div style="font-weight:700;font-size:13pt">%s</div>'
            '<div class="trigger">什麼時候翻我：%s</div>'
            '<div>%s</div><div>%s</div></div>'
            % (_esc(c["title"]), _h(c["trigger"]),
               _h(c["statement"]), _h(c["formula"])))


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  /* 範本的 .d-tbl 整張 break-inside:avoid，14 列的對譯表一放唔落剩餘空間就
     成張推去下一頁、前面留半頁白（L8 實測）。對譯表與總結表放寬為可跨頁、
     每列不可切開，表頭包 <thead> 讓 Chrome 跨頁時自動重印。 */
  .d-tbl.kw-table, .d-tbl.three-col { break-inside: auto; page-break-inside: auto; }
  .d-tbl.kw-table tr, .d-tbl.three-col tr { break-inside: avoid; page-break-inside: avoid; }
  .treefig { text-align: center; margin: 6px 0; }
  .treefig svg { max-width: 11.5cm; height: auto; }
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

    parts.append('<div class="section-h page-break">二、關鍵字對譯表（本課的主工具）</div>')
    parts.append('<div>左欄是題目會出現的字眼，右欄是它對應的數學動作。'
                 '上半張是一般對譯，照字面翻就對；'
                 '下半張是陷阱詞，不可以照字面翻，要多想一步。</div>')
    parts.append(_kw_html(KW_GENERAL, KW_TRAPS))
    parts.append('<div class="hint-card">%s</div>' % _h(KW_NOTE))

    parts.append('<div class="section-h page-break">三、範例A・分類還是分步</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_A))
    parts += ["<div>%s</div>" % _h(t) for t in A_TXT]
    parts.append("<div>%s</div>" % _h(TREE_CAP))
    parts.append('<div class="treefig">%s</div>' % FIG_TREE)
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_A))

    parts.append('<div class="section-h page-break">四、範例B・有先後，還是沒有先後</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_B))
    parts += ["<div>%s</div>" % _h(t) for t in B_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_B))

    parts.append('<div class="section-h page-break">五、五張招式提示卡</div>')
    parts.append('<div>對譯表下半張的陷阱詞負責「認出來」，這五張卡負責「怎樣做」。'
                 '每張卡最上面都寫了「什麼時候翻我」。'
                 '五張卡另外印成工具卡，剪下放在桌面，'
                 '做題時用手指指住正在用的那一張。</div>')
    for c in CARDS_D7:
        parts.append(_refcard_html(c))

    parts.append('<div class="section-h page-break">六、範例C・排列的三招</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_C))
    parts += ["<div>%s</div>" % _h(t) for t in C_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_C))

    parts.append('<div class="section-h page-break">七、範例D・組合的應用與混合題</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_D))
    parts += ["<div>%s</div>" % _h(t) for t in D_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_D))

    parts.append('<div class="section-h page-break">八、範例E・三種特殊型</div>')
    parts.append('<div class="problem">%s</div>' % _h(EX_E))
    parts += ["<div>%s</div>" % _h(t) for t in E_TXT]
    parts.append('<div class="hint-card">%s</div>' % _h(NOTE_E))

    parts.append('<div class="section-h page-break">'
                 '九、動筆前的三個問題（做每一題之前掃一眼）</div>')
    parts.append('<div>這三個問題的次序不可以調亂：先定加還是乘，再定 P 還是 C，'
                 '最後才處理附加條件。'
                 '次序錯了會出現「用對了公式但整題架構錯」這種最難自己發現的錯。</div>')
    parts.append('<table class="d-tbl three-col"><thead><tr>%s</tr></thead>'
                 '<tbody>%s</tbody></table>'
                 % ("".join("<th>%s</th>" % _esc(h) for h in SUM_HEAD),
                    "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _h(c) for c in r)
                            for r in SUM_ROWS)))

    parts.append('<div class="section-h">十、接下來</div>')
    parts.append('<div>請拿出《第2章 L10 排列與組合　課堂練習》，'
                 '並把《工具卡》剪下放在桌面。'
                 '練習A 已經把關鍵字標好、也寫明查到哪一條；'
                 '練習B 只重印五個觸發語；練習C 完全不提示，要自己圈關鍵字。'
                 '無論哪一節，動筆之前都先走完上面那三個問題。</div>')

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
