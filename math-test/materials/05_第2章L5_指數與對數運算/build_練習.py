# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L5 指數律與對數運算 —— 課堂練習 ＋ 工具卡 build script
主設計 D2 手順卡；輔助 D13 弗雷爾（練習A 第1題＝自己補非例格）、D14 錯誤分析對比
（練習B 第3題只提示「有一個常見陷阱」）。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：A 每題旁重印精簡四步 → B 只在區塊開頭印一次 → C 完全不印。
產出：練習_指數與對數運算_抽離小班共用版.docx/.html、工具卡_指數與對數運算.docx
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_指數與對數運算_抽離小班共用版"
CARD = "工具卡_指數與對數運算"
UNIT = "第2章 中學基礎數學應用．L5 指數律與對數運算"
FOOT = "高三數學．" + UNIT

HINT_TOP = ("動筆之前先看一眼《四步卡》：1 同底　2 合併　3 標準式 {fn(log)_a N=k}　"
            "4 還原成 {a^k=N} 並驗真數。凡是方程題，第 4 步的驗真數不可以省——"
            "沒有驗真數的答案等於沒有做完。")

STEP_TITLE = "對數運算四步"
STEP_TRIGGER = "任何一條有 log 的題目，都由第 1 步做起。"
STEP_COMPACT = ["同底：把所有 log 化到同一個底",
                "合併：用運算律併成一個 log",
                "標準式：寫成 {fn(log)_a N=k}",
                "還原成 {a^k=N}，解出來再驗真數"]

# ================================================================ 題目
STEMS = {
    1: "下列各式當中，哪些是有意義的對數？如果沒有意義，請寫出它違反了《對數卡》上的"
       "第幾個特徵；有意義的，請求出它的值。"
       "（a）{fn(log)_3 81}　（b）{fn(log)_2(-8)}　（c）{fn(log)_1 5}　（d）{fn(log)_40 1}",
    2: "計算下列各式的值。"
       "（a）{fn(log) 4+fn(log) 25}　（b）{fn(log)_2 8+fn(log)_2 4}",
    3: "（a）設 {fn(log) 2=a}、{fn(log) 3=b}，用 a 與 b 表示 {fn(log) 12}。"
       "（b）求 {(fn(log)_2 9)(fn(log)_3 2)} 的值。",
    4: "解方程 {fn(log)(x+3)+fn(log) x=1}。",
    5: "解方程 {4^(x+4)-2*2^(x+4)=-1}。",
    6: "（a）求 {fn(log) frac(5,9)-fn(log) frac(3,14)+fn(log) frac(27,7)} 的值。"
       "（b）如果把（a）式中的 {fn(log) frac(3,14)} 改成 {fn(log) frac(3,7)}，"
       "其餘不變，答案會變成多少？請先用一句話說出你的判斷理由，再算出來核對。",
}

B_HINT = {3: "⚠ 第（b）小題有一個常見陷阱：留意分數線是在 log 的裡面還是外面，"
             "兩者是完全不同的公式。"}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）有意義，值是 4　（b）沒有意義，違反特徵②　（c）沒有意義，違反特徵①　"
            "（d）有意義，值是 0",
        kp="對數的定義與合法範圍。{fn(log)_a N} 要成立，底數與真數都有限制："
           "底數 {a>0} 且 {a!=1}（特徵①），真數 {N>0}（特徵②）。"
           "求值時回到定義問「底數的幾多次方等於真數」。",
        fm="{fn(log)_a N=k} 等價於 {a^k=N}；特徵①底數 {a>0} 且 {a!=1}；特徵②真數 {N>0}。",
        steps=["（a）底數 3 合格、真數 81 大於 0，合法。問「3 的幾多次方等於 81」："
               "{3^4=81}，所以 {fn(log)_3 81=4}。",
               "（b）真數是 {-8}，小於 0，違反特徵②——負數沒有對數，本式沒有意義。",
               "（c）底數是 1，違反特徵①。理由：1 的任何次方都等於 1，"
               "永遠得不到 5，所以找不到那個次方。",
               "（d）底數 40 合格、真數 1 大於 0，合法。問「40 的幾多次方等於 1」："
               "{40^0=1}，所以 {fn(log)_40 1=0}。",
               "檢核：把（a）（d）改寫成指數式核對——{3^4=81} 成立、{40^0=1} 成立。"],
        pit="① 見到 {fn(log)_2(-8)} 就想「{2^(-3)=frac(1,8)}，所以答 {-3}」"
            "——{2^(-3)} 是正的 {frac(1,8)}，不是 {-8}；2 的任何次方都是正數，"
            "所以真數為負時根本無解，這正是特徵②的來源。"
            "② 把 {fn(log)_40 1} 答成 1（把真數當成答案）——真數是 1 時答案一律是 0。"
            "③ 只答「沒有意義」而沒有寫違反第幾個特徵——本題要求指出特徵編號。"),
    2: dict(
        ans="（a）2　（b）5",
        kp="對數運算律一（積）：兩個 log 相加，等於真數相乘之後的那一個 log。"
           "合併之後多數會出現 100、1000、32 這類「剛好是整次方」的真數，再回到定義求值。",
        fm="{fn(log)(MN)=fn(log) M+fn(log) N}；沒有寫底數的 log 以 10 為底。",
        steps=["（a）第 1 步同底：兩個都沒有寫底數，都是以 10 為底。",
               "（a）第 2 步合併：{fn(log) 4+fn(log) 25=fn(log)(4*25)=fn(log) 100}。",
               "（a）第 3、4 步：{fn(log)_10 100=k} 即 {10^k=100}，得 {k=2}。",
               "（b）第 2 步合併：{fn(log)_2 8+fn(log)_2 4=fn(log)_2(8*4)=fn(log)_2 32}。",
               "（b）第 4 步：{2^k=32}，而 {2^5=32}，所以答案是 5。",
               "檢核（b）：也可以分開求——{fn(log)_2 8=3}、{fn(log)_2 4=2}，"
               "{3+2=5}，與合併的做法一致。"],
        pit="① 把 {fn(log) 4+fn(log) 25} 算成 {fn(log)(4+25)=fn(log) 29}"
            "——log 相加對應真數相乘，不是相加（見講義第八節對比一）。"
            "② （b）兩個 log 的底數都是 2，合併之後底數仍然是 2，不要寫成以 10 為底。"
            "③ 合併之後忘記求值，把 {fn(log) 100} 當成最終答案——題目問的是「值」。"),
    3: dict(
        ans="（a）{fn(log) 12=2a+b}　（b）2",
        kp="（a）用運算律把 12 拆成已知的 2 與 3：{12=4*3=2^2*3}，"
           "再用積與次方兩條運算律拆開。"
           "（b）兩個 log 底數不同，要用換底公式化到同一個底再約簡。"
           "本題的陷阱在於「log 除以 log」與「log 裡面是分數」是兩條不同的公式。",
        fm="{fn(log)(MN)=fn(log) M+fn(log) N}；{fn(log) M^p=p fn(log) M}；"
           "換底 {fn(log)_a N=frac(fn(log) N,fn(log) a)}。",
        steps=["（a）把 12 拆成已知的因數：{12=4*3}，而 {4=2^2}。",
               "（a）用運算律一：{fn(log) 12=fn(log) 4+fn(log) 3}。",
               "（a）用運算律三：{fn(log) 4=fn(log) 2^2=2fn(log) 2=2a}；"
               "而 {fn(log) 3=b}。所以 {fn(log) 12=2a+b}。",
               "（b）換底，兩個都化到以 10 為底："
               "{fn(log)_2 9=frac(fn(log) 9,fn(log) 2)}，"
               "{fn(log)_3 2=frac(fn(log) 2,fn(log) 3)}。",
               "（b）相乘時 {fn(log) 2} 對消，剩 {frac(fn(log) 9,fn(log) 3)}。",
               "（b）再用運算律三：{fn(log) 9=fn(log) 3^2=2fn(log) 3}，"
               "所以 {frac(2fn(log) 3,fn(log) 3)=2}。",
               "檢核（a）：取 {fn(log) 2≈0.301}、{fn(log) 3≈0.477}，"
               "則 {2a+b≈0.602+0.477=1.079}；而 {fn(log) 12≈1.079}——相符。"],
        pit="① （b）把 {frac(fn(log) 9,fn(log) 2)} 當成 {fn(log) frac(9,2)}"
            "——分數線在 log 外面是換底公式，在 log 裡面才是運算律二，兩者完全不同。"
            "② （a）把 {fn(log) 12} 寫成 {fn(log) 2*fn(log) 6} 或 {a*fn(log) 6}"
            "——真數相乘對應的是兩個 log 相「加」，不是相乘。"
            "③ （a）把 {fn(log) 4} 寫成 {a^2}——係數搬出來是 {2fn(log) 2}，"
            "即 {2a}，不是 a 的平方。"),
    4: dict(
        ans="{x=2}",
        kp="對數方程的完整四步，重點在第 4 步的驗真數。"
           "還原成指數式之後，原來「真數大於 0」的限制就消失了，"
           "所以解出來的答案必須逐個代回原式檢查。",
        fm="{fn(log)(MN)=fn(log) M+fn(log) N}；"
           "{fn(log)_10 N=k} 等價於 {N=10^k}；真數必須大於 0。",
        steps=["第 1 步（同底）：兩個 log 都沒有寫底數，都是以 10 為底，已經同底。",
               "第 2 步（合併）：{fn(log)(x+3)+fn(log) x=fn(log)[x(x+3)]}，"
               "方程變成 {fn(log)[x(x+3)]=1}。",
               "第 3 步（標準式）：左邊一個 log、右邊一個數，"
               "即 {fn(log)_10(x^2+3x)=1}。",
               "第 4 步（還原）：{x^2+3x=10^1=10}，移項得 {x^2+3x-10=0}，"
               "因式分解 {(x+5)(x-2)=0}，得 {x=-5} 或 {x=2}。",
               "第 4 步（驗真數）：代 {x=2}——真數 {x+3=5>0}、{x=2>0}，兩個都合格，保留。",
               "代 {x=-5}——真數 {x+3=-2} 與 {x=-5} 都小於 0，違反特徵②，捨棄。",
               "所以解是 {x=2}。檢核："
               "{fn(log)(2+3)+fn(log) 2=fn(log) 5+fn(log) 2=fn(log) 10=1}，與原方程相符。"],
        pit="① 兩個根都寫上去當答案——{x=-5} 會令真數變成負數，一定要捨棄。"
            "② 只驗其中一個 log 的真數——原式有兩個 log，兩個真數都要大於 0 才算合格。"
            "③ 把右邊的 1 直接搬去左邊寫成 {fn(log)[x(x+3)]-1=0} 之後不知怎樣做"
            "——1 要看成 {10^1} 的指數，用第 4 步還原，不是繼續在 log 裡面搬。"),
    5: dict(
        ans="{x=-4}",
        kp="指數方程的換元法。{4^(x+4)} 與 {2^(x+4)} 底數不同，"
           "但 {4=2^2}，所以前者是後者的平方——化成同底之後設 {t=2^(x+4)}，"
           "整條方程就變成一元二次方程。",
        fm="{(a^m)^n=a^(mn)}；{a^0=1}；換元後解一元二次方程再代回。",
        steps=["第 1 步（同底）：{4=2^2}，所以 "
               "{4^(x+4)=(2^2)^(x+4)=2^(2(x+4))=[2^(x+4)]^2}。",
               "第 2 步（換元）：設 {t=2^(x+4)}，則原方程變成 {t^2-2t=-1}。",
               "第 3 步（解 t）：{t^2-2t+1=0}，即 {(t-1)^2=0}，所以 {t=1}（重根）。",
               "第 4 步（代回）：{2^(x+4)=1}。而 {1=2^0}，所以 {x+4=0}，得 {x=-4}。",
               "檢核：代 {x=-4} 入原式——{4^0-2*2^0=1-2=-1}，與右邊相同。",
               "合理性：{(t-1)^2=0} 只有一個重根，所以 x 也只有一個答案，"
               "不會像對數方程那樣多出一個要捨棄的根。"],
        pit="① 把 {4^(x+4)} 化成 {2^(2x+4)}——指數要整個乘 2，"
            "正確是 {2^(2x+8)}，也就是 {[2^(x+4)]^2}。"
            "② 換元之後忘記代回，答成 {t=1} 就交卷——題目問的是 x。"
            "③ 由 {2^(x+4)=1} 直接寫 {x+4=1}——右邊的 1 要先寫成 {2^0}，"
            "同底之後才可以比較指數。"),
    6: dict(
        ans="（a）1　（b）{fn(log) 5}（約 0.699）",
        kp="運算律一、二的綜合運用：先把整條式合併成一個 log，"
           "再看真數約簡之後是否剛好是 10 的整次方。"
           "第（b）問考的是「先判斷再驗算」——改動一個真數之後，"
           "整體真數會怎樣變，可以在動筆之前先講出來。",
        fm="{fn(log) M+fn(log) N=fn(log)(MN)}；{fn(log) M-fn(log) N=fn(log) frac(M,N)}。",
        steps=["（a）第 2 步（合併）：相減的那一項變成除法，相加的變成乘法，"
               "整條式合併成一個 log，真數是 "
               "{frac(5,9)÷frac(3,14)*frac(27,7)}。",
               "（a）除以一個分數等於乘它的倒數："
               "真數 {=frac(5,9)*frac(14,3)*frac(27,7)}。",
               "（a）分子 {5*14*27=1890}，分母 {9*3*7=189}，"
               "真數 {=frac(1890,189)=10}。",
               "（a）所以原式 {=fn(log) 10=1}。",
               "（b）先判斷：被減的真數由 {frac(3,14)} 變成 {frac(3,7)}，"
               "數值大了一倍；它是除數，除數大一倍，商就少一半，"
               "所以整個真數會由 10 變成 5，答案應該是 {fn(log) 5}，比 1 小。",
               "（b）再驗算：真數 {=frac(5,9)*frac(7,3)*frac(27,7)}；"
               "分子 {5*7*27=945}，分母 {9*3*7=189}，{frac(945,189)=5}。"
               "所以答案是 {fn(log) 5}，與判斷相符。",
               "檢核（b）：{fn(log) 5=fn(log) frac(10,2)=fn(log) 10-fn(log) 2"
               "≈1-0.301=0.699}，確實小於（a）的 1。"],
        pit="① 把中間的減號當成真數相減（寫成 {frac(5,9)-frac(3,14)}）"
            "——log 相減對應真數相除。"
            "② 除以分數時忘記倒過來乘，直接把 {frac(3,14)} 乘上去。"
            "③ （b）只算不判斷——本題明確要求先寫出理由再計算，"
            "先判斷方向（會變大還是變小）可以在算錯時即時發現。"),
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para("每一題旁邊都重印了四個步驟。第 1 題先判斷合不合法，"
                  "不合法的要寫出違反《對數卡》上的第幾個特徵。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(step_card(STEP_TITLE, STEP_COMPACT, compact=True))
        P.append(para("作答（把最後的答案寫在下面）："))
        P += write_lines(6)
        P.append(blank())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(para("四個步驟只在下面重印一次，題目旁邊不再放。"))
    P.append(step_card(STEP_TITLE, STEP_COMPACT, compact=True))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        if n in B_HINT:
            P.append(shaded_box(B_HINT[n]))
        P.append(para("作答："))
        P += write_lines(7)
        P.append(blank())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para("本節收起工具卡，四個步驟也不再印。請自己由第 1 步做起；"
                  "方程題最後仍然要驗真數（第 6 題不是方程，不必驗）。"))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(para("作答："))
        P += write_lines(9)
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
CARDS = [
    ("▍對數定義卡",
     "什麼時候翻我：見到 log 而不肯定它是甚麼意思，或者要判斷合不合法。",
     ["{fn(log)_a N=k} 即是 {a^k=N}",
      "讀法：「a 的幾多次方等於 N」",
      "① 底數 {a>0} 且 {a!=1}",
      "② 真數 {N>0}（負數與 0 沒有對數）",
      "③ 結果 k 可以是任何實數",
      "※ 沒有寫底數的 log ＝ 以 10 為底。"]),
    ("▍運算律卡",
     "什麼時候翻我：要把幾個 log 併成一個，或者要拆開一個 log。",
     ["積：{fn(log)(MN)=fn(log) M+fn(log) N}",
      "商：{fn(log) frac(M,N)=fn(log) M-fn(log) N}",
      "次方：{fn(log) M^p=p fn(log) M}",
      "換底：{fn(log)_a N=frac(fn(log) N,fn(log) a)}",
      "※ 加法沒有運算律：{fn(log)(a+b)} 拆不開。",
      "※ 分數線在 log 外面 ＝ 換底，在裡面 ＝ 商。"]),
    ("▍四步手順卡",
     "什麼時候翻我：任何一條有 log 的題目，由第 1 步做起。",
     ["1　同底：所有 log 化到同一個底",
      "2　合併：用運算律併成一個 log",
      "3　標準式：{fn(log)_a N=k}",
      "4　還原成 {a^k=N}，解出來再驗真數",
      "※ 做完一步才做下一步，不要跳去先算。"]),
    ("▍驗真數卡",
     "什麼時候翻我：解完對數方程，交答案之前。",
     ["把每一個答案代回原式。",
      "原式裡每一個 log 的真數都要 {>0}。",
      "有一個不合格，那個答案就要捨棄。",
      "※ 還原成指數式之後，{N>0} 的限制會消失，",
      "　所以多數會多出一個假答案。",
      "※ 沒有驗真數的答案 ＝ 沒有做完。"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in CARDS:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        c += [para("・" + t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=4200))
    return build_docx(P, os.path.join(HERE, CARD + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _tex(m):
    import re
    body = m.strip()
    # fn(log) → \log。**一定要排在 sqrt／frac 之前**，否則 frac(fn(log) N,fn(log) a)
    # 因為引數含括號而配不到，HTML 會印出字面 "frac(...)"（2026-07-28 實錄）。
    body = re.sub(r"fn\((\w+)\)", r"\\\1 ", body)
    for _ in range(6):
        new = re.sub(r"sqrt\[([^\[\]]+)\]\(([^()]*)\)", r"\\sqrt[\1]{\2}", body)
        new = re.sub(r"sqrt\(([^()]*)\)", r"\\sqrt{\1}", new)
        if new == body:
            break
        body = new
    for _ in range(6):
        new = re.sub(r"frac\(([^(),]+),([^(),]+)\)", r"\\frac{\1}{\2}", body)
        if new == body:
            break
        body = new
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    # 括號要保留，omml_core 也是照印出來的（拿掉會令 docx 與 HTML 不一致）
    body = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", body)
    body = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", body)
    body = re.sub(r"\^(\w{2,})", r"^{\1}", body)
    body = re.sub(r"_(\w{2,})", r"_{\1}", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
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


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


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
  .hint-card, .fig, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .step-card.compact td:first-child { width: 100%; font-weight: 400; }
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
    parts.append('<div>每一題旁邊都重印了四個步驟。第 1 題先判斷合不合法，'
                 '不合法的要寫出違反《對數卡》上的第幾個特徵。</div>')
    for n in A_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s'
                     '<div>作答（把最後的答案寫在下面）：</div>%s</div>'
                     % (n, _h(STEMS[n]), _step_compact_html(), _lines(6)))

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div>四個步驟只在下面重印一次，題目旁邊不再放。</div>')
    parts.append(_step_compact_html())
    for n in B_ITEMS:
        hint = ('<div class="hint-card">%s</div>' % _h(B_HINT[n])) if n in B_HINT else ""
        parts.append('<div class="problem"><div>%d．%s</div>%s'
                     '<div>作答：</div>%s</div>' % (n, _h(STEMS[n]), hint, _lines(7)))

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>本節收起工具卡，四個步驟也不再印。請自己由第 1 步做起；'
                 '方程題最後仍然要驗真數（第 6 題不是方程，不必驗）。</div>')
    for n in C_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>'
                     '<div>作答：</div>%s</div>' % (n, _h(STEMS[n]), _lines(9)))

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
