# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L5 指數律與對數運算 —— 課堂講義 build script
主設計 D2 手順卡（對數運算四個步驟，每步附 ※ 易錯點）；
輔助 D13 弗雷爾概念模型（「對數」一個術語，四象限含非例並標明違反第幾個特徵）、
     D14 錯誤分析對比（兩個真高頻錯法：log 相加變真數相加、係數乘進真數）。
鷹架密度：抽離小班 (Tier 2)。
產出：講義_指數與對數運算_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_指數與對數運算_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L5 指數律與對數運算"
FOOT = "高三數學．" + UNIT

# ================================================================ 文字內容
INTRO = [
    "由這一課開始進入第2章「中學基礎數學應用」。第2章佔全部課時的三分之一，"
    "當中以代數運算的題目最多；而代數運算裡面，指數與對數又是出題最密的一組。",
    "對數不是一種新的運算，它只是指數的另一種寫法。"
    "{fn(log)_a N=k} 與 {a^k=N} 講的是同一件事——前者問「a 的幾多次方等於 N」，"
    "後者直接把那個次方寫出來。只要能在這兩種寫法之間來回轉換，一大半的題目就解得出。",
    "這一課的困難不在概念，而在程序：一條對數題往往要「化同底 → 用運算律合併 → "
    "化成標準式 → 還原成指數式 → 驗真數」五件事接力做，中間漏一步就前功盡廢。"
    "工作記憶一次記不住五個步驟，所以本課把程序物理化成一張《對數運算四步卡》，"
    "做題時放在桌面，用手指指住正在做的那一步。",
    "另外要先把「對數」這個名詞本身弄清楚。很多人記得住 {fn(log)} 三個字母，"
    "卻分不清 {fn(log)_2(-8)} 為什麼不合法。第二節用四個格子把它的邊界劃出來，"
    "特別是第④格「不是對數的例子」——那一格才是真正練出辨識力的地方。",
]

# ---------------------------------------------------------------- D13 弗雷爾：對數
FRAYER_DEF = [
    "{fn(log)_a N=k} 讀作「以 a 為底、N 的對數等於 k」。",
    "它問的是一句話：「a 的幾多次方等於 N？」答案就是 k。",
    "例：{fn(log)_2 8} 問「2 的幾多次方等於 8」，答案是 3，所以 {fn(log)_2 8=3}。",
    "用自己的話重寫一次（練習時填）：把 {fn(log)_a N} 讀成「＿＿＿的＿＿＿次方等於＿＿＿」。",
]
FRAYER_FEAT = [
    "① 底數 a 要大於 0，而且 {a!=1}。",
    "② 真數 N 一定要大於 0（負數與 0 沒有對數）。",
    "③ 結果 k 可以是任何實數（可以是負數、可以是小數）。",
    "④ {fn(log)_a N=k} 與 {a^k=N} 可以互相改寫，兩者完全等價。",
    "※ 沒有寫底數的 {fn(log)} 一律當作以 10 為底。",
]
FRAYER_YES = [
    "{fn(log)_2 8=3}（因為 {2^3=8}）",
    "{fn(log)_10 100=2}（因為 {10^2=100}）",
    "{fn(log)_25 1=0}（因為 {25^0=1}；任何底數的 1 都是 0）",
    "{fn(log)_3 frac(1,9)=-2}（因為 {3^(-2)=frac(1,9)}；結果是負數也可以，見特徵③）",
]
FRAYER_NO = [
    "{fn(log)_2(-8)}——真數是負數，違反特徵②。",
    "{fn(log)_2 0}——真數是 0，違反特徵②。",
    "{fn(log)_1 5}——底數是 1，違反特徵①"
    "（1 的任何次方都是 1，永遠去不到 5）。",
    "{fn(log)_(-2) 8}——底數是負數，違反特徵①。",
]

# ---------------------------------------------------------------- D2 手順卡
STEP_TITLE = "對數運算四步卡"
STEP_TRIGGER = "任何一條有 log 的題目，都由第 1 步做起。"
STEPS = [
    ("先看底數：把式中所有 log 化成同一個底。底數不同就用換底公式。",
     "沒有寫底數的 log 一律是以 10 為底，不要當成未知底。換底公式是 "
     "{fn(log)_a N=frac(fn(log) N,fn(log) a)}——分子是真數，分母是底數，不要寫反。"),
    ("用運算律把幾個 log 合併成一個 log。",
     "{fn(log)(a+b)} 不等於 {fn(log) a+fn(log) b}。加法沒有運算律，"
     "只有乘、除、次方三種才有——第 8 節會用正誤對照再講一次。"),
    ("化成標準式 {fn(log)_a N=k}：等號左邊只剩一個 log，右邊只剩一個數。",
     "如果 log 前面還有係數（例如 {2fn(log) 3}），要先用次方律搬進真數變成 "
     "{fn(log) 3^2}，不可以留在外面。"),
    ("還原成指數式 {a^k=N}，解出未知數，最後回頭驗真數。",
     "對數方程一定要驗真數：把答案代回原式，每一個 log 的真數都必須大於 0，"
     "不合的那個答案要捨棄。跳過這一步，多數題目會多出一個假答案。"),
]
STEP_FADING = ("完整四步卡（每步附易錯點）→ 只留四個關鍵詞（同底、合併、標準式、還原驗真數）"
               "→ 只留「這題有四步」→ 完全移除。")

LAWS = [
    "運算律一（積）：{fn(log)(MN)=fn(log) M+fn(log) N}"
    "　　兩個真數相乘 → 兩個 log 相加。",
    "運算律二（商）：{fn(log) frac(M,N)=fn(log) M-fn(log) N}"
    "　　兩個真數相除 → 兩個 log 相減。",
    "運算律三（次方）：{fn(log) M^p=p fn(log) M}"
    "　　真數的次方 → 可以搬到 log 前面當係數，反過來也成立。",
    "換底公式：{fn(log)_a N=frac(fn(log) N,fn(log) a)}"
    "　　底數不同時用它化到同一個底（通常化到以 10 為底）。",
]

# ---------------------------------------------------------------- 範例
EX, SOL, NOTE = {}, {}, {}

EX["A"] = ("【範例A・指數律】不用計算機，判斷下列各組哪一個較大："
           "（a）{6^3} 與 {3^6}　（b）{2^32} 與 {4^31}。")
SOL["A"] = [
    "（a）兩個數的底數與次方都不同，先各自算出來："
    "{6^3=216}，{3^6=729}，所以 {3^6} 較大。",
    "（b）數字太大，算不出來，改為化成同一個底。"
    "{4=2^2}，所以 {4^31=(2^2)^31=2^62}。",
    "同底之後只需比較次方：{62>32}，所以 {4^31} 較大。",
    "檢核：用細一點的數字驗證同一個做法——{4^2=(2^2)^2=2^4=16}，"
    "而直接算 {4^2=16}，兩者相同，可見 {(a^m)^n=a^(mn)} 這條指數律沒有用錯。",
]
NOTE["A"] = ("※ 指數題的第一個動作永遠是「能不能化成同一個底」。"
             "化到同底之後，比大小就只是比次方，完全不用計算。"
             "常用的同底改寫：{4=2^2}、{8=2^3}、{9=3^2}、{27=3^3}、{25=5^2}。")

EX["B"] = ("【範例B・對數定義】直接由定義求值："
           "（a）{fn(log)_2 8}　（b）{fn(log)_25 1}　（c）{fn(log)_4 256-fn(log)_4 4}。")
SOL["B"] = [
    "（a）問「2 的幾多次方等於 8」。{2^3=8}，所以 {fn(log)_2 8=3}。",
    "（b）問「25 的幾多次方等於 1」。任何不等於 0 的數的 0 次方都是 1，"
    "{25^0=1}，所以 {fn(log)_25 1=0}。",
    "（c）{fn(log)_4 256}：{4^4=256}，所以等於 4。"
    "{fn(log)_4 4}：{4^1=4}，所以等於 1。相減得 {4-1=3}。",
    "檢核（c）：也可以先用運算律二合併——"
    "{fn(log)_4 256-fn(log)_4 4=fn(log)_4 frac(256,4)=fn(log)_4 64}，"
    "而 {4^3=64}，同樣得 3。兩種做法一致。",
]
NOTE["B"] = ("※ 「底數的 1 的對數是 0」這一條在題庫裡出現過很多次"
             "（{fn(log)_25 1}、{fn(log)_40 1}、{fn(log)_101 1} 全部答 0）。"
             "見到真數是 1，不必計算，直接寫 0。")

EX["C"] = ("【範例C・運算律與換底】（a）設 {fn(log) 2=a}、{fn(log) 3=b}，"
           "用 a、b 表示 {fn(log) 15}。（b）求 {(fn(log)_3 8)(fn(log)_8 3)} 的值。"
           "（c）求 {frac(fn(log) 32,fn(log) 16)} 的值。")
SOL["C"] = [
    "（a）15 不能直接由 2 與 3 相乘得到，但 {15=frac(30,2)}，而 {30=3*10}。"
    "所以 {fn(log) 15=fn(log) frac(30,2)}。",
    "用運算律二：{fn(log) 30-fn(log) 2}；再用運算律一："
    "{fn(log) 30=fn(log)(3*10)=fn(log) 3+fn(log) 10}。",
    "沒有寫底數即以 10 為底，所以 {fn(log) 10=1}，"
    "得 {fn(log) 15=b+1-a}。",
    "（b）兩個 log 底數不同，用換底公式化到以 10 為底："
    "{fn(log)_3 8=frac(fn(log) 8,fn(log) 3)}，{fn(log)_8 3=frac(fn(log) 3,fn(log) 8)}。",
    "兩者相乘，分子分母剛好對消，得 1。",
    "（c）{fn(log) 32=fn(log) 2^5=5fn(log) 2}（運算律三）；"
    "同樣 {fn(log) 16=fn(log) 2^4=4fn(log) 2}。",
    "相除時 {fn(log) 2} 對消，得 {frac(5,4)}。",
    "檢核（a）：取 {fn(log) 2≈0.301}、{fn(log) 3≈0.477}，"
    "則 {b+1-a≈0.477+1-0.301=1.176}；而 {fn(log) 15≈1.176}——相符。",
]
NOTE["C"] = ("※ 見到 {frac(fn(log) M,fn(log) N)} 這種「log 除以 log」的形狀，"
             "不要當成運算律二（那條是 {fn(log) frac(M,N)}，分數在 log 裡面）。"
             "log 除以 log 是換底公式的形狀，要反過來寫成 {fn(log)_N M}。"
             "分數線在 log 外面還是裡面，是兩條完全不同的公式——這是本課最需要看清楚的一個細節。")

EX["D"] = "【範例D・對數方程】解方程 {fn(log)(x-3)+fn(log) x=1}。（四個步驟全部用上）"
SOL["D"] = [
    "第 1 步（同底）：兩個 log 都沒有寫底數，即都是以 10 為底，已經同底。",
    "第 2 步（合併）：用運算律一，{fn(log)(x-3)+fn(log) x=fn(log)[x(x-3)]}，"
    "所以方程變成 {fn(log)[x(x-3)]=1}。",
    "第 3 步（標準式）：左邊已經只剩一個 log，右邊只剩一個數 1，"
    "即 {fn(log)_10(x^2-3x)=1}。",
    "第 4 步（還原）：改寫成指數式 {x^2-3x=10^1=10}，"
    "移項得 {x^2-3x-10=0}，因式分解 {(x-5)(x+2)=0}，得 {x=5} 或 {x=-2}。",
    "第 4 步（驗真數，不可略）：代 {x=5}——真數 {x-3=2>0}、{x=5>0}，兩個都合格，保留。",
    "代 {x=-2}——真數 {x-3=-5}，是負數，違反對數的特徵②，捨棄。",
    "所以方程的解是 {x=5}。",
    "檢核：{fn(log)(5-3)+fn(log) 5=fn(log) 2+fn(log) 5=fn(log) 10=1}——與原方程相符。",
]
NOTE["D"] = ("※ 對數方程幾乎每次都會多出一個假答案，因為「還原成指數式」之後，"
             "原本 {N>0} 的限制就消失了。所以第 4 步的驗真數不是「有時間才做」，"
             "而是解題的一部分——沒有驗真數的答案，等於沒有做完。")

EX_ORDER = ["A", "B", "C", "D"]
EX_HEAD = {"A": "四、範例A・指數律：先化成同底才比得出大小",
           "B": "五、範例B・對數定義：由定義直接讀出答案",
           "C": "六、範例C・運算律與換底：分數線在 log 裡面還是外面",
           "D": "七、範例D・對數方程：四個步驟全部用上"}
EX_BREAK = {"A": True, "B": False, "C": True, "D": True}

# ---------------------------------------------------------------- D14 錯誤對比
ERR1_STEM = "【對比一】求 {fn(log) 2+fn(log) 5} 的值。"
ERR1_ROWS = [
    ("{fn(log) 2+fn(log) 5=fn(log)(2+5)}", "{fn(log) 2+fn(log) 5=fn(log)(2*5)}"),
    ("{=fn(log) 7≈0.845}", "{=fn(log) 10=1}"),
]
ERR1_NOTE = ("※ 差在這裡（第 1 列）：log 相加，對應的是真數相乘，不是相加。"
             "記法——log 的作用就是把「乘」降一級變成「加」，所以反過來看，"
             "兩個 log 相加時，真數要乘起來。加法本身沒有對數運算律，"
             "{fn(log)(a+b)} 是化簡不了的。")

ERR2_STEM = "【對比二】把 {2fn(log) 3} 寫成一個 log。"
ERR2_ROWS = [
    ("{2fn(log) 3=fn(log)(2*3)}", "{2fn(log) 3=fn(log) 3^2}"),
    ("{=fn(log) 6≈0.778}", "{=fn(log) 9≈0.954}"),
]
ERR2_NOTE = ("※ 差在這裡（第 1 列）：log 前面的係數，搬進去之後要變成真數的次方，"
             "不是乘進真數。這是運算律三 {fn(log) M^p=p fn(log) M} 反過來用。"
             "驗算方法：{2fn(log) 3=fn(log) 3+fn(log) 3=fn(log)(3*3)=fn(log) 9}"
             "——用運算律一拆開來看，就知道一定是 9 不是 6。")

# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D2 手順卡——《對數運算四步卡》（同底 → 合併 → 標準式 → 還原並驗真數），"
                "每一步下方附該步最易出錯的關鍵點（※ 前綴），另出工具卡讓學生放桌面",
    aux_designs=("D13 弗雷爾概念模型——「對數」一個術語的四象限"
                 "（定義／特徵／例／非例），非例格每一項都標明違反第幾個特徵",
                 "D14 錯誤分析對比——兩個真高頻錯法："
                 "log 相加誤寫成真數相加、係數誤乘進真數而非變成次方"),
    reason=(
        "本課取自題庫 A4 代數運算（103 題，進度表配 2.0 小時）當中最密集的一組"
        "——指數與對數共約 30 題，包括對數求值、運算律、換底、對數方程與指數方程。"
        "依 teaching-designs.md §1，本課屬 S2 多步驟程序運算："
        "一條對數題要「化同底 → 合併 → 標準式 → 還原 → 驗真數」接力完成，"
        "核心瓶頸是序列性步驟在工作記憶中崩潰、漏步驟，因此主設計取 S2 的建議主設計 D2 手順卡。"
        "輔助設計沒有取 S2 建議的 D9／D12，而是改取 D13 與 D14，理由是本課有兩個 S2 一般沒有的觸發條件："
        "①「對數」是典型的「會背名詞卻分不清邊界」的術語"
        "（學生記得 log，卻不知道 {fn(log)_2(-8)} 為何不合法），符合 D13 的觸發條件，"
        "而且本課是對數的第一課；②「{fn(log)(a+b)=fn(log) a+fn(log) b}」與"
        "「{p fn(log) M=fn(log)(pM)}」是兩個公認的高頻固定錯法，符合 D14 的觸發條件，"
        "且本課屬統考複習而非新授課，兩個對比都排在對應範例之後。"
        "D9 草稿分區與 D12 自我核對留給 L6（根式與分式化簡），那一課的失分主因才是草稿排版。"),
    density="抽離小班（Tier 2）",
    fading=(
        "手順卡（D2）：本課講義印出完整四步卡（每步附易錯點），另出工具卡放桌面 → "
        "練習A 每題旁重印精簡版步驟號（1 同底 2 合併 3 標準式 4 還原驗真數）→ "
        "練習B 只在區塊開頭印一次 → 練習C 不印 → L6 起只口頭提示「這題有四步」→ 完全移除。"
        "唯一保留到最後的是第 4 步的「驗真數」，那一項會併入 L6 的自我核對清單。｜"
        "弗雷爾（D13）：本課講義四格全部填好 → 練習A 第 1 題要學生自己判斷哪些式子不合法"
        "並指出違反第幾個特徵（即自己補非例格）→ 練習B 只在題幹出現不合法的真數而不提示 → "
        "練習C 不提示 → 之後改為口頭問「這個 log 合法嗎」→ 移除。｜"
        "錯誤分析對比（D14）：本課給完整正誤雙欄 → 練習B 第 3 題只提示「這題有一個常見陷阱」→ "
        "練習C 不提示 → 訂正課時由學生自己指出分歧在第幾行 → 移除。"),
    flows=("F5 課前流程預告（今天四件事：對數是甚麼 → 四步卡 → 四個範例 → 兩個最易錯的步驟）",
           "F1 師徒制對話四步（範例C 的（c）小題適合做口述練習："
           "徒弟讀題、師傅只用口講「分數線在 log 裡面還是外面」，雙方都不准動筆）",
           "F4 過程導向回饋與分步計分（四個步驟各自給分；"
           "特別是第 4 步的驗真數要單獨計分，做了就給分，不論前面算對算錯——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（四步卡與運算律卡即為此項，"
               "若獲准帶入測考需寫入 IEP 第 9 點）",
               "a5 放大字體", "a6 增加行距",
               "a7 調整計分標準（四個步驟分步給分，不以最後答案一刀切）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與第1章的銜接",
            "第1章四課（L1～L4）處理的是應用題文字題（S1 結構），"
            "鷹架在「讀題→列式」那一段。由本課起轉入純代數運算（S2 結構），"
            "鷹架改放在「列式之後的執行程序」。學生會發現題目短了很多，但步驟多了"
            "——要先講清楚這個轉變，否則會誤以為第2章比較簡單而略過寫步驟。"),
           ("為何主設計不是 D7 提示卡",
            "L4 用 D7 是因為五種題型各有一套固定設定式，瓶頸在「認題型 → 取設定式」。"
            "本課只有一種題型，設定式也只有三條運算律，記憶負荷不大；"
            "真正的困難是五個步驟的執行順序，那是 D2 處理的問題。"
            "三條運算律不另出提示卡，直接印在四步卡的第 2 步下面，"
            "避免疊出第四個設計（超過「主 1＋輔 2」的上限）。"),
           ("題量說明",
            "本課練習回到 Tier 2 的標準題量，共 6 題（練習A／B／C 各 2 題），"
            "多數題目附（a）（b）小問，合共 11 個小問，涵蓋定義求值、運算律、換底、"
            "對數方程與指數方程五種形態。"
            "L4 的 8 題是因為要覆蓋五個互不相干的題型，本課題型集中，不需要加量。"),
           ("配套文件",
            "《第2章 L5 指數律與對數運算　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L5 指數律與對數運算　工具卡》"
            "（對數定義卡、運算律卡、四步手順卡、驗真數卡，學生剪下護貝放桌面）。")),
)


# ================================================================ docx
def _mp(lines):
    return [para(t) for t in lines]


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、先弄清楚：「對數」是甚麼", page_break_before=True))
    P.append(para("下面四個格子把「對數」這個詞的邊界劃出來。"
                  "第④格特別重要——只有看得出甚麼「不是」對數，才算真的認識它。"))
    P.append(dual_track_table([(_mp(FRAYER_DEF), _mp(FRAYER_FEAT))],
                             headers=("① 定義（用自己的話重寫一次）",
                                      "② 特徵／必要條件（要編號，後面會引用）")))
    P.append(dual_track_table([(_mp(FRAYER_YES), _mp(FRAYER_NO))],
                             headers=("③ 例：這些是合法的對數",
                                      "④ 非例：這些不是，並註明違反第幾個特徵")))

    P.append(heading("三、對數運算的四個步驟", page_break_before=True))
    P.append(para("下面這張卡是本課的主線。做題時把它放在桌面，"
                  "用手指指住正在做的那一步，做完一步才做下一步。"))
    P.append(step_card(STEP_TITLE, STEPS, trigger=STEP_TRIGGER, fading=STEP_FADING))
    P.append(para("第 2 步會用到的三條運算律（連同換底公式）："))
    for t in LAWS:
        P.append(shaded_box(t))

    for k in EX_ORDER:
        P.append(heading(EX_HEAD[k], page_break_before=EX_BREAK[k]))
        P.append(problem_box([para(EX[k])]))
        for t in SOL[k]:
            P.append(para(t))
        P.append(shaded_box(NOTE[k]))

    P.append(heading("八、最容易錯的兩步", page_break_before=True))
    P.append(para("下面兩個對比，左欄是很多人會寫出來的做法，右欄是正確做法。"
                  "兩欄逐行對齊，只有第 1 列不同——請先自己看出差在哪裡，再讀下面的說明。"))
    for stem, rows, note in ((ERR1_STEM, ERR1_ROWS, ERR1_NOTE),
                             (ERR2_STEM, ERR2_ROWS, ERR2_NOTE)):
        P.append(problem_box([para(stem)]))
        P.append(dual_track_table([([para(a)], [para(b, bold=True)]) for a, b in rows],
                                  headers=("常見寫法", "正確寫法")))
        P.append(shaded_box(note))

    P.append(heading("九、接下來"))
    P.append(para("請拿出《第2章 L5 指數律與對數運算　課堂練習》，"
                  "並把《工具卡》剪下來放在桌面。練習A 的兩題旁邊重印了四個步驟；"
                  "練習B 只在區塊開頭印一次；練習C 完全不印，四個步驟要自己記住。"
                  "無論哪一區，只要題目是方程，最後都要驗真數。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _tex(m):
    """把 {} 標記轉成 MathJax 的 \\( \\)。要與 omml_core 的解析結果一致，
    否則會出現「docx 對而 HTML 錯」（2026-07-27 分數吃小數的實錄）。"""
    import re
    body = m.strip()
    # fn(log) → \log（正體函數名）。**一定要排在 sqrt／frac 之前**：
    # frac 的引數正則排除括號，若 fn(log) 還沒展開，frac(fn(log) N,fn(log) a) 會配不到，
    # 結果 HTML 印出字面 "frac(log N,log a)" 而 docx 正確（2026-07-28 實錄）。
    body = re.sub(r"fn\((\w+)\)", r"\\\1 ", body)
    # sqrt[n](x) → \sqrt[n]{x}；sqrt(x) → \sqrt{x}（由最內層往外，可巢狀）
    for _ in range(6):
        new = re.sub(r"sqrt\[([^\[\]]+)\]\(([^()]*)\)", r"\\sqrt[\1]{\2}", body)
        new = re.sub(r"sqrt\(([^()]*)\)", r"\\sqrt{\1}", new)
        if new == body:
            break
        body = new
    # frac(a,b) → \frac{a}{b}
    for _ in range(6):
        new = re.sub(r"frac\(([^(),]+),([^(),]+)\)", r"\\frac{\1}{\2}", body)
        if new == body:
            break
        body = new
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    # 上下標：多字元內容要包成 {}，否則 TeX 只吃第一個字元；
    # 括號要**保留**——omml_core 也是照印出來的，拿掉會令 docx 與 HTML 不一致。
    body = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", body)
    body = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", body)
    body = re.sub(r"\^(\w{2,})", r"^{\1}", body)
    body = re.sub(r"_(\w{2,})", r"_{\1}", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    # 分子分母都要吃小數點（omml_core 的 _NUM_RE 本來就吃小數）
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


def _cell(lines):
    return "".join("<div>%s</div>" % _h(t) for t in lines)


def _dual(headers, pairs, bold_right=False):
    style = ' style="font-weight:700"' if bold_right else ""
    rows = "".join("<tr><td>%s</td><td%s>%s</td></tr>" % (a, style, b) for a, b in pairs)
    return ('<table class="d-tbl dual-track"><tr><th>%s</th><th>%s</th></tr>%s</table>'
            % (_esc(headers[0]), _esc(headers[1]), rows))


def _step_card_html():
    rows = "".join('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                   % (i, _h(a), _h(p)) for i, (a, p) in enumerate(STEPS, 1))
    return ('<table class="d-tbl step-card"><tr><th colspan="2">%s</th></tr>'
            '<tr><td colspan="2">什麼時候用：%s</td></tr>%s'
            '<tr><td colspan="2">（教師）褪除：%s</td></tr></table>'
            % (_esc(STEP_TITLE), _esc(STEP_TRIGGER), rows, _esc(STEP_FADING)))


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    # 只補列印分頁規則；不動 @page 邊界與 .footer 的 position，QB-15c 的計數維持 1。
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .dual-track td { vertical-align: top; }
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

    parts.append('<div class="section-h page-break">二、先弄清楚：「對數」是甚麼</div>')
    parts.append('<div>下面四個格子把「對數」這個詞的邊界劃出來。'
                 '第④格特別重要——只有看得出甚麼「不是」對數，才算真的認識它。</div>')
    parts.append(_dual(("① 定義（用自己的話重寫一次）",
                        "② 特徵／必要條件（要編號，後面會引用）"),
                       [(_cell(FRAYER_DEF), _cell(FRAYER_FEAT))]))
    parts.append(_dual(("③ 例：這些是合法的對數",
                        "④ 非例：這些不是，並註明違反第幾個特徵"),
                       [(_cell(FRAYER_YES), _cell(FRAYER_NO))]))

    parts.append('<div class="section-h page-break">三、對數運算的四個步驟</div>')
    parts.append('<div>下面這張卡是本課的主線。做題時把它放在桌面，'
                 '用手指指住正在做的那一步，做完一步才做下一步。</div>')
    parts.append(_step_card_html())
    parts.append('<div>第 2 步會用到的三條運算律（連同換底公式）：</div>')
    parts += ['<div class="hint-card">%s</div>' % _h(t) for t in LAWS]

    for k in EX_ORDER:
        parts.append('<div class="section-h%s">%s</div>'
                     % (" page-break" if EX_BREAK[k] else "", _esc(EX_HEAD[k])))
        parts.append('<div class="problem">%s</div>' % _h(EX[k]))
        parts += ["<div>%s</div>" % _h(t) for t in SOL[k]]
        parts.append('<div class="hint-card">%s</div>' % _h(NOTE[k]))

    parts.append('<div class="section-h page-break">八、最容易錯的兩步</div>')
    parts.append('<div>下面兩個對比，左欄是很多人會寫出來的做法，右欄是正確做法。'
                 '兩欄逐行對齊，只有第 1 列不同——請先自己看出差在哪裡，再讀下面的說明。</div>')
    for stem, rows, note in ((ERR1_STEM, ERR1_ROWS, ERR1_NOTE),
                             (ERR2_STEM, ERR2_ROWS, ERR2_NOTE)):
        parts.append('<div class="problem">%s</div>' % _h(stem))
        parts.append(_dual(("常見寫法", "正確寫法"),
                           [(_h(a), _h(b)) for a, b in rows], bold_right=True))
        parts.append('<div class="hint-card">%s</div>' % _h(note))

    parts.append('<div class="section-h">九、接下來</div>')
    parts.append('<div>請拿出《第2章 L5 指數律與對數運算　課堂練習》，'
                 '並把《工具卡》剪下來放在桌面。練習A 的兩題旁邊重印了四個步驟；'
                 '練習B 只在區塊開頭印一次；練習C 完全不印，四個步驟要自己記住。'
                 '無論哪一區，只要題目是方程，最後都要驗真數。</div>')

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
