# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L6 根式、分式的化簡與有理化 —— 課堂練習 ＋ 工具卡 build script
主設計 D2 手順卡（三張）；輔助 D9 草稿分區（練習A、B 的四格作答區）、
D12 自我核對清單＋核對點（每個區塊末尾）。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：A 每題旁重印該卡關鍵詞＋四格 → B 只在區塊開頭印一次＋四格 → C 兩者都不給。
產出：練習_根式與分式化簡_抽離小班共用版.docx/.html、工具卡_根式與分式化簡.docx
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_根式與分式化簡_抽離小班共用版"
CARD = "工具卡_根式與分式化簡"
UNIT = "第2章 中學基礎數學應用．L6 根式、分式的化簡與有理化"
FOOT = "高三數學．" + UNIT

HINT_TOP = ("動筆之前先認出題型：根號內不是完全平方 → 手順卡一（拆／開／併）；"
            "分母有根號 → 手順卡二（取共軛／平方差／約簡）；"
            "兩個分式相加減 → 手順卡三（分解／通分／合併約分／寫限制）。"
            "作答寫在四個格子裡，寫在哪一格就代表你在做哪一步。")

QUAD_LABELS = ("① 抄下原式，圈出要先處理的部分",
               "② 拆開／通分：寫出中間式",
               "③ 計算並合併同類項",
               "④ 檢查：根號內還有完全平方嗎？分母還有根號嗎？")

STEP_TITLE = "三張手順卡（關鍵詞版）"
STEP_TRIGGER = "先認出題型，再照對應那一行做。"
STEP_COMPACT = ["根式化簡：拆（完全平方 × 剩餘）→ 開 → 併同類根式",
                "分母有理化：取共軛（只調中間符號）→ 平方差 → 約簡",
                "分式化簡：分母因式分解 → 通分（分子加括號）→ 合併約分 → 寫限制"]
STEP_WARN = "※ 約分只可以約因式，不可以約項；分式題一定要寫限制。"

# ================================================================ 題目
STEMS = {
    1: "化簡下列各根式，並求該三角形的周長。"
       "（a）{sqrt(50)}　（b）{sqrt(75)}　"
       "（c）一個三角形的三邊長分別是 {sqrt(50)} 厘米、{sqrt(25)} 厘米、{sqrt(75)} 厘米，"
       "求它的周長。",
    2: "計算 {sqrt(48)-sqrt(27)+sqrt(12)}。",
    3: "（a）寫出 {4+sqrt(3)} 與 {13-sqrt(2)} 的有理化因式，並算出各自相乘之後的值。"
       "（b）化簡 {frac(1,2+sqrt(3))}。",
    4: "化簡 {frac(1,x-1)+frac(1,x+1)}，並寫出 x 的限制。",
    5: "（a）化簡 {frac(1,x-2)-frac(4,x^2-4)}，並寫出 x 的限制。"
       "（b）化簡之後的式子在 {x=2} 時算得出 {frac(1,4)}，但原式在 {x=2} 沒有意義。"
       "用一句話說明為甚麼。",
    6: "已知 {a+b=12} 及 {ab=22}。"
       "（a）求 {sqrt(a^2+b^2)} 的值。"
       "（b）求 {fn(log) sqrt[3](a^2+b^2)} 的值（接回 L5 的對數運算律）。",
}

# 練習A：D2 褪除的第一級——標明用哪一張卡
CARD_HINT = {
    1: "▍用手順卡一（根式化簡）：拆成「完全平方 × 剩餘」→ 開方搬出來 → 合併同類根式。",
    2: "▍用手順卡一（根式化簡）：三項先各自化到最簡，再看哪些是同類根式。",
}

SELFCHECK = {
    "A": ["根號內已經沒有完全平方因數",
          "同類根式已經合併，不同類的沒有硬加在一起",
          "係數與根號分開寫清楚（例如寫 {2sqrt(5)} 而不是 {sqrt(2*5)}）",
          "每一題都有寫中間步驟，不是只寫一個答案"],
    "B": ["分母已經沒有根號",
          "共軛只調轉了中間那個符號，前後兩項沒有動",
          "分子分母的公因式已經約掉，而且分子每一項都有除到",
          "分式題已經寫出 x 不可以等於甚麼"],
    "C": ["分母已經先因式分解才通分",
          "約掉的是因式（整個括號），不是項",
          "限制是由原式的分母寫出來的，不是由化簡後的式子寫出來",
          "有代一個數字回原式驗算過"],
}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）{5sqrt(2)}　（b）{5sqrt(3)}　（c）周長 {=5sqrt(2)+5+5sqrt(3)}（厘米）",
        kp="根式化簡三步：拆成「完全平方 × 剩餘」、開方搬出根號外、合併同類根式。"
           "本題三邊化簡後沒有兩項是同類根式，所以答案保留三項——"
           "「不能再合併」本身就是最簡形式。",
        fm="{sqrt(mn)=sqrt(m)*sqrt(n)}；只有根號內完全相同的才是同類根式，可以合併係數。",
        steps=["（a）第 1 步：{50=25*2}，25 是完全平方。"
               "第 2 步：{sqrt(50)=sqrt(25*2)=5sqrt(2)}。",
               "（b）第 1 步：{75=25*3}。第 2 步：{sqrt(75)=sqrt(25*3)=5sqrt(3)}。",
               "（c）第三邊 {sqrt(25)=5}（25 本身就是完全平方，開出來是整數，沒有根號）。",
               "（c）第 3 步：{5sqrt(2)}、5、{5sqrt(3)} 三項的根號內各不相同"
               "（分別是 2、沒有根號、3），沒有同類項，所以周長 {=5sqrt(2)+5+5sqrt(3)}（厘米）。",
               "檢核（取近似值）：{sqrt(50)≈7.071}、{sqrt(25)=5}、{sqrt(75)≈8.660}，"
               "三者相加 {≈20.731}；而 {5sqrt(2)+5+5sqrt(3)≈7.071+5+8.660=20.731}——相符。"],
        pit="① 把 {sqrt(50)} 拆成 {sqrt(5*10)} 之後開不出來就放棄"
            "——要拆成含完全平方的組合（{25*2}），不是隨便拆兩個因數。"
            "② {sqrt(25*2)} 寫成 {25sqrt(2)}——25 開方之後是 5。"
            "③ 把 {5sqrt(2)+5+5sqrt(3)} 硬合併成 {15sqrt(5)} 之類"
            "——根號內不同就加不起來，三項並列已經是答案。"),
    2: dict(
        ans="{3sqrt(3)}",
        kp="三項各自化到最簡之後，發現根號內全部是 3，即三項都是同類根式，"
           "可以只加減係數。這一題示範了「先化簡才看得出是不是同類」。",
        fm="{sqrt(mn)=sqrt(m)*sqrt(n)}；同類根式合併時，係數相加減，根號部分不變。",
        steps=["第 1、2 步（逐項拆與開）：{48=16*3}，{sqrt(48)=4sqrt(3)}；"
               "{27=9*3}，{sqrt(27)=3sqrt(3)}；{12=4*3}，{sqrt(12)=2sqrt(3)}。",
               "第 3 步（併）：三項的根號內都是 3，是同類根式。"
               "係數 {4-3+2=3}，所以答案是 {3sqrt(3)}。",
               "檢核（取近似值）：{sqrt(48)≈6.928}、{sqrt(27)≈5.196}、{sqrt(12)≈3.464}，"
               "{6.928-5.196+3.464=5.196}；而 {3sqrt(3)≈5.196}——相符。",
               "合理性：三項化簡後都變成 {sqrt(3)} 的倍數，"
               "所以答案一定也是 {sqrt(3)} 的倍數——形式上先合理。"],
        pit="① 未化簡就直接看根號內的 48、27、12 不同，判斷「不是同類、不能合併」"
            "——一定要先各自化到最簡才判斷。"
            "② {sqrt(48)-sqrt(27)} 算成 {sqrt(48-27)=sqrt(21)}"
            "——根號不能這樣拆，{sqrt(m)-sqrt(n)} 不等於 {sqrt(m-n)}。"
            "③ 係數算成 {4-3+2=1} 或 {4+3+2=9}——中間那一項是減號，只減一次。"),
    3: dict(
        ans="（a）{4-sqrt(3)}，乘積 13；{13+sqrt(2)}，乘積 167　（b）{2-sqrt(3)}",
        kp="有理化的核心是共軛與平方差：{(a+sqrt(b))(a-sqrt(b))=a^2-b}，"
           "乘完之後分母必定是有理數。"
           "「有理化因式」問的是那個要乘上去的式子，「化簡」才要把整個乘法做完。",
        fm="共軛：{a+sqrt(b)} 與 {a-sqrt(b)}；平方差 {(a+sqrt(b))(a-sqrt(b))=a^2-b}。",
        steps=["（a）{4+sqrt(3)} 的有理化因式是 {4-sqrt(3)}（只調中間的符號）。"
               "乘積 {=(4+sqrt(3))(4-sqrt(3))=16-3=13}。",
               "（a）{13-sqrt(2)} 的有理化因式是 {13+sqrt(2)}。"
               "乘積 {=(13-sqrt(2))(13+sqrt(2))=169-2=167}。",
               "（b）第 1 步：分母 {2+sqrt(3)} 是兩項，共軛是 {2-sqrt(3)}。",
               "（b）第 2 步：分子分母同乘 {2-sqrt(3)}。"
               "分母 {=(2+sqrt(3))(2-sqrt(3))=4-3=1}；分子 {=2-sqrt(3)}。",
               "（b）第 3 步：分母是 1，不必再約，答案 {=2-sqrt(3)}。",
               "檢核（a）：兩個乘積 13 與 167 都是整數，沒有根號，符合「有理化」的目的。",
               "檢核（b）：{frac(1,2+sqrt(3))≈frac(1,3.732)≈0.268}；"
               "{2-sqrt(3)≈0.268}——相符。"],
        pit="① 把共軛寫成 {-4-sqrt(3)} 或 {-4+sqrt(3)}"
            "——共軛只調中間那個符號，第一項不動。"
            "② （a）答了乘積 13 而沒有寫出有理化因式 {4-sqrt(3)}"
            "——題目兩樣都要。"
            "③ （b）分子分母只乘了分母一邊——分子分母必須同乘，否則值就變了。"),
    4: dict(
        ans="{frac(2x,x^2-1)}（或 {frac(2x,(x-1)(x+1))}），限制 {x!=1} 且 {x!=-1}",
        kp="兩個分式相加：先把分母因式分解找出公分母，通分之後合併分子，"
           "最後回頭由原式的分母寫出限制。本題公分母就是兩個分母的乘積。",
        fm="{frac(1,A)+frac(1,B)=frac(B+A,AB)}；限制：原式每一個分母都不可以等於 0。",
        steps=["第 1 步（找公分母）：兩個分母 {x-1} 與 {x+1} 沒有公因式，"
               "公分母就是 {(x-1)(x+1)}，即 {x^2-1}。",
               "第 2 步（通分）：{frac(1,x-1)=frac(x+1,(x-1)(x+1))}；"
               "{frac(1,x+1)=frac(x-1,(x-1)(x+1))}。",
               "第 3 步（合併分子）：分子 {=(x+1)+(x-1)=2x}。"
               "所以原式 {=frac(2x,(x-1)(x+1))=frac(2x,x^2-1)}。"
               "分子 {2x} 與分母沒有公因式，不能再約。",
               "第 4 步（限制）：原式的分母是 {x-1} 與 {x+1}，"
               "所以 {x!=1} 且 {x!=-1}。",
               "檢核：取 {x=3}——原式 {=frac(1,2)+frac(1,4)=frac(3,4)}；"
               "而 {frac(2*3,9-1)=frac(6,8)=frac(3,4)}——相符。"],
        pit="① 把 {frac(1,x-1)+frac(1,x+1)} 直接寫成 {frac(2,2x)} 或 {frac(1,2x)}"
            "——分式相加不是分子加分子、分母加分母。"
            "② 通分後分子寫成 {x+1+x-1} 卻算成 {2x+2}"
            "——{+1} 與 {-1} 相消，答案是 {2x}。"
            "③ 漏寫限制。本題兩個限制都要寫，只寫一個不算完整。"),
    5: dict(
        ans="（a）{frac(1,x+2)}，限制 {x!=2} 且 {x!=-2}　"
            "（b）因為限制來自原式的分母，化簡不會令它消失",
        kp="分母是多項式時，先因式分解才找得出公分母。"
           "本題化簡後分子分母有公因式 {x-2} 可以約掉，但約掉之後"
           "「{x!=2}」這個限制仍然存在——這正是第（b）問要說明的事。",
        fm="{x^2-4=(x-2)(x+2)}；約分只可以約因式；限制由原式的分母決定。",
        steps=["（a）第 1 步（分解）：{x^2-4=(x-2)(x+2)}。"
               "公分母是 {(x-2)(x+2)}。",
               "（a）第 2 步（通分）：{frac(1,x-2)=frac(x+2,(x-2)(x+2))}；"
               "第二項的分母已經是公分母，不用動。",
               "（a）第 3 步（合併並約分）：分子 {=(x+2)-4=x-2}。"
               "所以式子 {=frac(x-2,(x-2)(x+2))}；"
               "分子分母有公因式 {x-2}，約掉得 {frac(1,x+2)}。",
               "（a）第 4 步（限制）：原式的分母是 {x-2} 與 {x^2-4}，"
               "兩者為 0 的情況是 {x=2} 與 {x=-2}，所以 {x!=2} 且 {x!=-2}。",
               "檢核（a）：取 {x=3}——原式 {=frac(1,1)-frac(4,5)=frac(1,5)}；"
               "而 {frac(1,3+2)=frac(1,5)}——相符。",
               "（b）說明：{x=2} 會令原式的分母 {x-2} 變成 0，除以 0 沒有意義，"
               "所以原式在 {x=2} 根本不存在。"
               "化簡時把 {x-2} 約掉，只是把那個「洞」在寫法上藏起來，"
               "並沒有把它補回去——所以限制要照原式寫，而且一定要寫出來。"],
        pit="① 由化簡後的 {frac(1,x+2)} 去寫限制，只寫 {x!=-2}"
            "——限制永遠由原式的分母決定，{x!=2} 不可以漏。"
            "② 約分時把分子的 {x-2} 與分母的 {x+2} 一起「約掉 x」"
            "——那是約項不是約因式，完全錯。"
            "③ 第 3 步分子寫成 {x+2-4=x+2}——{2-4=-2}，分子是 {x-2}。"),
    6: dict(
        ans="（a）10　（b）{frac(2,3)}",
        kp="用恆等式 {(a+b)^2=a^2+2ab+b^2} 把 {a^2+b^2} 由已知的 {a+b} 與 {ab} 表示出來，"
           "不必求出 a、b 本身。（b）接回 L5 的對數運算律三："
           "根號可以寫成分數次方，次方可以搬到 log 前面當係數。",
        fm="{a^2+b^2=(a+b)^2-2ab}；{sqrt[3](N)=N^(1/3)}；"
           "{fn(log) M^p=p fn(log) M}；{fn(log) 100=2}。",
        steps=["（a）第 1 步：{(a+b)^2=a^2+2ab+b^2}，移項得 {a^2+b^2=(a+b)^2-2ab}。",
               "（a）第 2 步：代入已知 {a+b=12}、{ab=22}——"
               "{a^2+b^2=12^2-2*22=144-44=100}。",
               "（a）第 3 步：{sqrt(a^2+b^2)=sqrt(100)=10}。",
               "（b）第 1 步：{a^2+b^2=100}，所以要求的是 {fn(log) sqrt[3](100)}。",
               "（b）第 2 步：把立方根寫成分數次方——{sqrt[3](100)=100^(1/3)}。",
               "（b）第 3 步（運算律三）：{fn(log) 100^(1/3)=frac(1,3)fn(log) 100}；"
               "而 {fn(log) 100=2}，所以答案 {=frac(1,3)*2=frac(2,3)}。",
               "檢核（a）：解 {a+b=12}、{ab=22} 得 a、b 是 {x^2-12x+22=0} 的兩根，"
               "{x=6+-sqrt(14)}；"
               "則 {a^2+b^2=(6+sqrt(14))^2+(6-sqrt(14))^2=(36+12sqrt(14)+14)+"
               "(36-12sqrt(14)+14)=100}——與第 2 步相符。",
               "檢核（b）：{frac(2,3)≈0.667}；"
               "而 {fn(log) sqrt[3](100)≈fn(log) 4.642≈0.667}——相符。"],
        pit="① 想先解出 a、b 再代入——本題的 a、b 是無理數 {6+-sqrt(14)}，"
            "硬解會令計算變得很難；用恆等式可以完全避開。"
            "② {(a+b)^2} 展開時漏了中間項，寫成 {a^2+b^2=144}"
            "——{2ab=44} 一定要減掉。"
            "③ （b）把 {fn(log) sqrt[3](100)} 當成 {sqrt[3](fn(log) 100)}"
            "——立方根在 log 的裡面，要先用運算律三搬成係數 {frac(1,3)}。"),
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para("每一題下方標明了要用哪一張手順卡。作答寫在四個格子裡，"
                  "一格只做一件事。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(shaded_box(CARD_HINT[n]))
        P.append(quadrant_workspace(QUAD_LABELS, cell_h=1700))
        P.append(blank())
    P.append(selfcheck_list(SELFCHECK["A"]))
    P.append(checkpoint_rule())

    P.append(heading("二、練習B（%s）" % star_label(2), page_break_before=True))
    P.append(para("由這一節開始不再標明用哪一張卡，要自己認出題型。"
                  "三張卡的關鍵詞只在下面重印一次。"))
    P.append(step_card(STEP_TITLE, STEP_COMPACT, trigger=STEP_TRIGGER, compact=True))
    P.append(shaded_box(STEP_WARN))
    P.append(blank())
    for n in B_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(quadrant_workspace(QUAD_LABELS, cell_h=1700))
        P.append(blank())
    P.append(selfcheck_list(SELFCHECK["B"]))
    P.append(checkpoint_rule())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para("本節收起工具卡，四個格子也不再印。請自己在作答空間分四步寫："
                  "抄原式 → 拆或通分 → 計算合併 → 檢查與寫限制。"))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(para("作答（請自己分四步寫）："))
        # 9 行時第 5 頁最後一行與 fixed 頁尾只差 3.4pt（QB-20 WARN）；
        # 範本層不可改（CLAUDE.md §4 已記兩種修法皆失敗），減一行避開。
        P += write_lines(8)
        P.append(blank())
    P.append(selfcheck_list(SELFCHECK["C"]))

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
    ("▍手順卡一・根式化簡",
     "什麼時候翻我：根號內的數不是完全平方。",
     ["1　拆：完全平方 × 剩餘（4、9、16、25、36…）",
      "2　開：完全平方開出來搬到根號外",
      "3　併：根號內相同的才可以加減係數",
      "※ {sqrt(4*5)=2sqrt(5)}，不是 {4sqrt(5)}。",
      "※ {sqrt(5)} 與 {sqrt(10)} 不同類，加不起來。"]),
    ("▍手順卡二・分母有理化",
     "什麼時候翻我：分母出現根號。",
     ["1　取共軛：{a+sqrt(b)} → {a-sqrt(b)}",
      "2　分子分母同乘，用平方差 {a^2-b}",
      "3　約簡：分子每一項都要除到",
      "※ 共軛只調中間那個符號。",
      "※ 乘完分母仍有根號 ＝ 共軛寫錯了。"]),
    ("▍手順卡三・分式化簡",
     "什麼時候翻我：兩個或以上分式相加減。",
     ["1　每個分母因式分解，找公分母",
      "2　通分：分子是多項式先加括號",
      "3　合併同類項，再約公因式",
      "4　寫出限制（原式分母不可以是 0）",
      "※ {1-x=-(x-1)}，見到要先統一。",
      "※ 約分只可以約因式，不可以約項。"]),
    ("▍核對卡",
     "什麼時候翻我：每一區做完，交卷之前。",
     ["{CHECKBOX} 根號內沒有完全平方因數了",
      "{CHECKBOX} 同類根式已經合併",
      "{CHECKBOX} 分母沒有根號了",
      "{CHECKBOX} 分式題寫了 x 的限制",
      "{CHECKBOX} 有代一個數字回原式驗算過"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in CARDS:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        c += [para(("" if t.startswith("{CHECKBOX}") else "・")
                   + t.replace("{CHECKBOX}", CHECKBOX), sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=4200))
    return build_docx(P, os.path.join(HERE, CARD + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _split_args(s, start):
    """s[start] 必須是 '('。回傳 (頂層逗號分開的引數 list, 收括號後的位置)。"""
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
    """遞迴展開 frac(a,b)／sqrt(x)／sqrt[n](x)，引數可以含括號
    （frac(x+1,(x-1)(x+1)) 這種寫法用正則抓不到，2026-07-28 實錄）。"""
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


def _quadrant_html(labels):
    def cell(t):
        return '<td><div class="qlabel">%s</div></td>' % _esc(t)
    rows = "".join("<tr>%s%s</tr>" % (cell(labels[i]), cell(labels[i + 1]))
                   for i in range(0, len(labels), 2))
    return '<table class="d-tbl quadrant">%s</table>' % rows


def _selfcheck_html(items, title="做完先自己核對一次"):
    return ('<div class="selfcheck"><div style="font-weight:700">%s</div>%s</div>'
            % (_esc(title), "".join("<div>&#9744; %s</div>" % _h(t) for t in items)))


def _checkpoint_html():
    return ('<div class="checkpoint">【核對點】做到這裡先停，'
            '對照上面的清單檢查一次再往下</div>')


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
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .step-card.compact td:first-child { width: 100%; font-weight: 400; }
  .quadrant td { height: 3.0cm; }
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
    parts.append('<div>每一題下方標明了要用哪一張手順卡。作答寫在四個格子裡，'
                 '一格只做一件事。</div>')
    for n in A_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>'
                     '<div class="hint-card">%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _h(CARD_HINT[n]), _quadrant_html(QUAD_LABELS)))
    parts.append(_selfcheck_html(SELFCHECK["A"]))
    parts.append(_checkpoint_html())

    parts.append('<div class="section-h page-break">二、練習B'
                 '（<span class="stars">★★☆</span>）</div>')
    parts.append('<div>由這一節開始不再標明用哪一張卡，要自己認出題型。'
                 '三張卡的關鍵詞只在下面重印一次。</div>')
    parts.append(_step_compact_html())
    parts.append('<div class="hint-card">%s</div>' % _h(STEP_WARN))
    for n in B_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _quadrant_html(QUAD_LABELS)))
    parts.append(_selfcheck_html(SELFCHECK["B"]))
    parts.append(_checkpoint_html())

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>本節收起工具卡，四個格子也不再印。請自己在作答空間分四步寫：'
                 '抄原式 → 拆或通分 → 計算合併 → 檢查與寫限制。</div>')
    for n in C_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>'
                     '<div>作答（請自己分四步寫）：</div>%s</div>'
                     % (n, _h(STEMS[n]), _lines(8)))
    parts.append(_selfcheck_html(SELFCHECK["C"]))

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
