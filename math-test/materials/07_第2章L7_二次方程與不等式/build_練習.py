# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L7 一元二次方程與二次不等式 —— 課堂練習 ＋ 工具卡 build script
主設計 D2 手順卡（三張）；輔助 D5 圖文雙軌（練習C 不等式題褪成自己畫符號線）、
D14 錯誤分析對比（第 6 題找錯）。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：A 每題旁重印該卡關鍵詞 → B 只在區塊開頭印一次 → C 兩者都不給、自己畫符號線。
產出：練習_二次方程與不等式_抽離小班共用版.docx/.html、工具卡_二次方程與不等式.docx
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_二次方程與不等式_抽離小班共用版"
CARD = "工具卡_二次方程與不等式"
UNIT = "第2章 中學基礎數學應用．L7 一元二次方程與二次不等式"
FOOT = "高三數學．" + UNIT

HINT_TOP = ("動筆之前先認出題型：要解方程、求 x → 手順卡一（標準式／試分解／公式法）；"
            "問「根的情況」不要求解出根 → 手順卡二（抄 a、b、c／算 Δ／判正負零）；"
            "求 x 的範圍（>、<、≥、≤）→ 手順卡三（化正／求根／大於取兩邊、小於取中間）。")

STEP_TITLE = "三張手順卡（關鍵詞版）"
STEP_TRIGGER = "先認出題型，再照對應那一行做。"
STEP_COMPACT = [
    "解方程：化標準式（一邊為 0）→ 試因式分解 {(px+q)(rx+s)=0} → 分解不到用公式法",
    "判別式判根：抄 a、b、c → 算 {Δ=b^2-4ac} → 正兩根、零重根、負無根",
    "解二次不等式：化正（乘負數要轉向）→ 求兩根 → 大於取兩邊、小於取中間",
]
STEP_WARN = "※ 乘或除以負數，不等號一定要轉向；> / < 端點空心，≥ / ≤ 端點實心。"

# ================================================================ 題目
STEMS = {
    1: "解方程（因式分解法）：（a）{x^2-7x+10=0}　（b）{x^2-9=0}。",
    2: "只用判別式判斷根的情況（不必解出根）："
       "（a）{x^2-4x+4=0}　（b）{2x^2-3x+5=0}。",
    3: "用公式法解 {x^2-6x+2=0}（答案化到最簡）。",
    4: "方程 {x^2+6x+k=0}。（a）k 為何值時有兩個相等實根？"
       "（b）k 在甚麼範圍時有兩個相異實根？",
    5: "解二次不等式：（a）{x^2-x-6<=0}　（b）{x^2-x-6>0}。"
       "（先求根，再看拋物線；開口向上時大於取兩邊、小於取中間）",
    6: "（找錯題）某同學解 {-x^2+4x-3>=0} 如下，"
       "請圈出錯在哪一步、改正，並寫出正確解集："
       "「兩邊乘 −1：{x^2-4x+3>=0}；因式分解 {(x-1)(x-3)>=0}；"
       "取兩邊：{x<=1} 或 {x>=3}。」",
}

# 練習A：D2 褪除的第一級——標明用哪一張卡
CARD_HINT = {
    1: "▍用手順卡一（解方程）：先確認一邊為 0，再試因式分解"
       "——(a) 找兩數之積 10、之和 7；(b) 是平方差 {x^2-9}。",
    2: "▍用手順卡二（判別式）：抄 a、b、c，算 {Δ=b^2-4ac}，"
       "再看正負零判斷，不必解出根。",
}

SELFCHECK = {
    "A": ["方程已經化成一邊為 0 的標準式",
          "因式分解後，每個括號都令它為 0，兩個根都寫了出來",
          "判別式題有寫出 {Δ=b^2-4ac} 的計算，不是只寫結論",
          "每一題都有中間步驟，不是只寫一個答案"],
    "B": ["公式法有先算判別式 Δ，{-b} 的負號沒有漏",
          "根號有化到最簡（例如 {sqrt(28)} 寫成 {2sqrt(7)}），再與分母約簡",
          "求參數 k 的題，兩個解或整個範圍都寫齊了",
          "答案該帶根號的就帶根號，沒有硬湊成小數"],
    "C": ["二次不等式先求出兩根，再判斷拋物線開口方向",
          "用了「大於取兩邊、小於取中間」，而且看清楚含不含端點",
          "有沒有乘負數？有的話不等號轉向了沒有",
          "答案寫成 x 的範圍（區間），不是兩個點"],
}

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="（a）{x=2} 或 {x=5}　（b）{x=3} 或 {x=-3}",
        kp="因式分解解方程：化成一邊為 0，再把左邊分解成兩個括號的乘積，"
           "令每個括號分別為 0。每個括號各給一個根，所以有兩個答案。",
        fm="積為 c、和為 −b 的兩數 → {x^2-(和)x+(積)}；平方差 {x^2-a^2=(x-a)(x+a)}。",
        steps=["（a）第 1 步：已是標準式 {x^2-7x+10=0}。"
               "第 2 步：積 10、和 7 → 2 與 5，{x^2-7x+10=(x-2)(x-5)}。",
               "（a）令 {(x-2)(x-5)=0} → {x=2} 或 {x=5}。",
               "（b）{x^2-9} 是平方差：{x^2-9=(x-3)(x+3)}，令其為 0 → {x=3} 或 {x=-3}。",
               "檢核：{2^2-7*2+10=0}、{5^2-7*5+10=0}；{(+-3)^2-9=0}——都成立。"],
        pit="① 只寫一個根：{(x-2)(x-5)=0} 要寫齊 {x=2} 和 {x=5}。"
            "② （b）把 {x^2-9=0} 寫成 {x=9}——應先開方或分解，得 {x=+-3}。"
            "③ 平方差看成完全平方，硬拆成 {(x-3)^2}——{(x-3)^2=x^2-6x+9}，不是 {x^2-9}。"),
    2: dict(
        ans="（a）兩個相等實根　（b）沒有實數根",
        kp="判別式只判斷根的情況，不必把根解出來。"
           "{Δ=b^2-4ac}：正 → 兩相異實根；零 → 兩相等實根（重根）；負 → 無實根。",
        fm="{Δ=b^2-4ac}；{Δ>0} 兩相異、{Δ=0} 兩相等、{Δ<0} 無實根。",
        steps=["（a）{a=1}、{b=-4}、{c=4}。{Δ=(-4)^2-4*1*4=16-16=0} → 兩個相等實根。",
               "（a）佐證：{x^2-4x+4=(x-2)^2}，確實只得 {x=2} 一個重根，與 {Δ=0} 相符。",
               "（b）{a=2}、{b=-3}、{c=5}。{Δ=(-3)^2-4*2*5=9-40=-31<0} → 沒有實數根。"],
        pit="① 把 {Δ=0} 答成「無解／無根」——{Δ=0} 是有一個重根（兩個相等實根）。"
            "② 抄係數漏了負號：{b=-4} 時 {b^2=16}，不是 {-16}（負數平方變正）。"
            "③ （b）算成 {Δ=9-40=31}——{9-40} 是負數 {-31}，別把負號丟掉。"),
    3: dict(
        ans="{x=3+sqrt(7)} 或 {x=3-sqrt(7)}（即 {x=3+-sqrt(7)}）",
        kp="分解不到就用公式法。先算判別式確認有實根，再代公式，"
           "最後把根號化到最簡並與分母約簡。",
        fm="{x=frac(-b+-sqrt(b^2-4ac),2a)}；{sqrt(mn)=sqrt(m)*sqrt(n)}。",
        steps=["第 1 步（抄係數）：{a=1}、{b=-6}、{c=2}。",
               "第 2 步（判別式）：{Δ=(-6)^2-4*1*2=36-8=28>0}，兩相異實根。",
               "第 3 步（代公式）：{x=frac(-(-6)+-sqrt(28),2*1)=frac(6+-sqrt(28),2)}。"
               "化簡根號：{sqrt(28)=sqrt(4*7)=2sqrt(7)}。",
               "第 4 步（約簡）：{x=frac(6+-2sqrt(7),2)=3+-sqrt(7)}（分子兩項都除以 2）。",
               "檢核（韋達）：和 {=(3+sqrt(7))+(3-sqrt(7))=6=frac(-b,a)}；"
               "積 {=(3+sqrt(7))(3-sqrt(7))=9-7=2=frac(c,a)}——相符。"],
        pit="① {-b} 漏負號：{b=-6}，所以 {-b=6}，不是 {-6}。"
            "② {sqrt(28)} 不化簡就停手——要化成 {2sqrt(7)}。"
            "③ 只把分子一項除以 2：{frac(6+-2sqrt(7),2)} 要兩項都除，得 {3+-sqrt(7)}，"
            "不是 {3+-2sqrt(7)}。"),
    4: dict(
        ans="（a）{k=9}　（b）{k<9}",
        kp="含參數的方程，用判別式把「根的情況」翻譯成對 k 的條件："
           "兩相等實根 ⇔ {Δ=0}；兩相異實根 ⇔ {Δ>0}。",
        fm="{Δ=b^2-4ac}；兩相等 ⇔ {Δ=0}，兩相異 ⇔ {Δ>0}。",
        steps=["抄係數：{a=1}、{b=6}、{c=k}。{Δ=6^2-4*1*k=36-4k}。",
               "（a）兩相等實根 ⇔ {Δ=0}：{36-4k=0} → {4k=36} → {k=9}。"
               "佐證：{k=9} 時 {x^2+6x+9=(x+3)^2=0}，{x=-3} 重根。",
               "（b）兩相異實根 ⇔ {Δ>0}：{36-4k>0} → {4k<36} → {k<9}。",
               "檢核（b）：取 {k=0} → {x^2+6x=0} → {x(x+6)=0} → {x=0}、{-6} 兩相異根，"
               "而 {0<9} 在範圍內——相符。"],
        pit="① （a）(b) 混淆：相等用 {Δ=0}、相異用 {Δ>0}，不要對調。"
            "② 解 {36-4k>0} 時移項忘了變號：{-4k>-36} 兩邊除以 −4 要轉向，得 {k<9}。"
            "③ （b）把 {k<9} 寫成 {k<=9}——{k=9} 是相等（重根），不算相異，要用嚴格 {<}。"),
    5: dict(
        ans="（a）{-2<=x<=3}　（b）{x<-2} 或 {x>3}",
        kp="二次不等式：先解對應方程求兩根，判斷開口方向，再按不等號取區間。"
           "本題 {x^2-x-6=(x-3)(x+2)}，兩根 −2、3，開口向上。"
           "(a) 與 (b) 恰好互補，以兩根為分界。",
        fm="{x^2-x-6=(x-3)(x+2)}；開口向上時：大於取兩邊、小於取中間。",
        steps=["第 1 步（求根）：{x^2-x-6=(x-3)(x+2)=0} → 兩根 {x=-2}、{x=3}（{-2<3}）。",
               "第 2 步（看圖）：{x^2} 係數為正 → 開口向上；兩根之間在 x 軸下方（負），"
               "兩根外側在 x 軸上方（正）。",
               "（a）要 {<=0}（負或零）→ 取中間、含端點：{-2<=x<=3}。",
               "（b）要 {>0}（正、不含零）→ 取兩邊、不含端點：{x<-2} 或 {x>3}。",
               "檢核：{x=0} 代入得 {-6}（負），故屬 (a) 的解、不屬 (b)；"
               "{x=4} 代入得 {6}（正），故屬 (b) 的解——都相符。"],
        pit="① 把不等式當方程解，只答 {x=-2}、{x=3} 兩個點——答案是一段範圍。"
            "② 取錯區間：開口向上、要「小於 0」取中間，要「大於 0」取兩邊，不要弄反。"
            "③ 端點含不含搞錯：{<=} / {>=} 含端點，{<} / {>} 不含。"),
    6: dict(
        ans="錯在第一步（乘 −1 沒有把 {>=} 轉成 {<=}）；正確解集 {1<=x<=3}",
        kp="兩邊乘或除以負數，不等號必須轉向。這一步一錯，後面全錯。"
           "改正後照手順卡三求根、取區間即可。",
        fm="乘／除負數 → 不等號轉向；開口向上時大於取兩邊、小於取中間。",
        steps=["分歧步驟＝第一步。{-x^2+4x-3>=0} 兩邊乘 −1，"
               "要把 {>=} 轉成 {<=}，得 {x^2-4x+3<=0}（該同學漏了轉向）。",
               "改正：{x^2-4x+3<=0} → {(x-1)(x-3)<=0}，兩根 1、3，開口向上，"
               "取中間、含端點 → {1<=x<=3}。",
               "檢核（回代原式，不碰乘 −1）：{x=2} → {-4+8-3=1>=0} ✓（2 在 [1,3] 內）；"
               "{x=0} → {-3}，不 {>=0} ✓（0 在解集外）。"
               "該同學的錯答 {x<=1} 或 {x>=3} 會把 {x=0} 判為解，但 {x=0} 令原式 {=-3<0}，"
               "可見其錯。"],
        pit="① 只把式子乘 −1 而不轉向——這正是本題要抓的錯。"
            "② 改正後又取錯區間：{<=0} 開口向上要取中間，不是兩邊。"
            "③ 圈錯分歧步驟：錯的是第一步（乘負數不轉向），因式分解那一步本身沒錯。"),
}

A_ITEMS, B_ITEMS, C_ITEMS = (1, 2), (3, 4), (5, 6)
LINES = {5: 8, 6: 8}


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading("一、練習A（%s）" % star_label(1)))
    P.append(para("每一題下方標明了要用哪一張手順卡。作答時先寫標準式，再一步一步做。"))
    for n in A_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        P.append(shaded_box(CARD_HINT[n]))
        P += write_lines(6)
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
        # 練習B 用 6 行：7 行時第 3 頁尾行被 fixed 頁尾白底蓋住 −1.8pt（QB-20 FAIL）；
        # 範本層不可改（CLAUDE.md §4 已記兩種修法皆失敗），減一行避開，仍 ≥5+1。
        P += write_lines(6)
        P.append(blank())
    P.append(selfcheck_list(SELFCHECK["B"]))
    P.append(checkpoint_rule())

    P.append(heading("三、練習C（%s）" % star_label(3), page_break_before=True))
    P.append(para("本節收起工具卡。不等式題（第 5 題）要自己先求根，再畫一條符號線"
                  "（開口向上的拋物線草圖），標出兩根與正負，才寫解集；"
                  "第 6 題是找錯題，先圈出錯的那一步，再寫出正確做法。"))
    for n in C_ITEMS:
        P.append(problem_box([para("%d．%s" % (n, STEMS[n]))]))
        if n == 5:
            P.append(para("作答（先求根 → 畫符號線 → 按不等號取區間）："))
        else:
            P.append(para("作答（圈出分歧步驟 → 改正 → 寫出正確解集）："))
        P += write_lines(LINES[n])
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
# 速查卡的公式刻意用橫式 Unicode（−b ± √… ÷ 2a），不用 OMML 分數：
# 分數式會把卡片行距疊高（L4 實測，一條頂兩條），四張卡就排不進一頁。
CARDS = [
    ("▍手順卡一・解一元二次方程",
     "什麼時候翻我：要解方程、求 x。",
     ["1　化標準式：一邊為 0，{ax^2+bx+c=0}",
      "2　試因式分解 {(px+q)(rx+s)=0}，各括號 = 0",
      "3　分解不到就用公式法（見速查卡）",
      "※ 不要兩邊除以 x，會丟掉 x=0 的根。",
      "※ 兩個括號各給一個根，別漏。"]),
    ("▍手順卡二・判別式判根",
     "什麼時候翻我：問根的情況、不要求解出根。",
     ["1　抄 a、b、c（連正負號）",
      "2　算 {Δ=b^2-4ac}",
      "3　正→兩相異；零→兩相等（重根）；負→無實根",
      "※ Δ=0 是相等，不是無根。",
      "※ 求 k 的題常漏一個解。"]),
    ("▍手順卡三・解二次不等式",
     "什麼時候翻我：求 x 的範圍（>、<、≥、≤）。",
     ["1　化一邊為 0，使 x² 的係數為正",
      "2　求兩根 r₁ < r₂",
      "3　開口向上：大於取兩邊、小於取中間",
      "※ 乘除負數，不等號要轉向。",
      "※ >／< 端點空心，≥／≤ 端點實心。"]),
    ("▍速查卡・公式法與判別式",
     "什麼時候翻我：分解不到、或要算 Δ。",
     ["公式：x ＝（−b ± √(b² − 4ac)）÷ 2a",
      "判別式：Δ ＝ b² − 4ac",
      "Δ＞0 兩相異　Δ＝0 兩相等　Δ＜0 無實根",
      "※ −b 的負號、分母 2a 別漏。",
      "※ 根號先化到最簡再約分。"]),
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
    parts.append('<div>每一題下方標明了要用哪一張手順卡。作答時先寫標準式，再一步一步做。</div>')
    for n in A_ITEMS:
        parts.append('<div class="problem"><div>%d．%s</div>'
                     '<div class="hint-card">%s</div>%s</div>'
                     % (n, _h(STEMS[n]), _h(CARD_HINT[n]), _lines(6)))
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
                     % (n, _h(STEMS[n]), _lines(6)))
    parts.append(_selfcheck_html(SELFCHECK["B"]))
    parts.append(_checkpoint_html())

    parts.append('<div class="section-h page-break">三、練習C'
                 '（<span class="stars">★★★</span>）</div>')
    parts.append('<div>本節收起工具卡。不等式題（第 5 題）要自己先求根，再畫一條符號線'
                 '（開口向上的拋物線草圖），標出兩根與正負，才寫解集；'
                 '第 6 題是找錯題，先圈出錯的那一步，再寫出正確做法。</div>')
    for n in C_ITEMS:
        lead = ("作答（先求根 → 畫符號線 → 按不等號取區間）：" if n == 5
                else "作答（圈出分歧步驟 → 改正 → 寫出正確解集）：")
        parts.append('<div class="problem"><div>%d．%s</div><div>%s</div>%s</div>'
                     % (n, _h(STEMS[n]), lead, _lines(LINES[n])))
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
