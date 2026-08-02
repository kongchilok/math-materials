# -*- coding: utf-8 -*-
"""
第1章 特殊數學應用專題．L1 比例與分配 —— 課堂練習 ＋ 工具卡 build script
主設計 D1 條形模型；輔助 D8 關鍵字對譯表、D4 三欄式引導。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：A 給半成品條形圖＋三欄填一半 → B 只給空白格線自己分段、三欄全空 → C 純文字、圖自畫。
產出：練習_比例與分配_抽離小班共用版.docx/.html/.pdf、工具卡_比例與分配.docx/.pdf
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import design_svg as ds                      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
os.makedirs(FIGS, exist_ok=True)
BASE = "練習_比例與分配_抽離小班共用版"
CARD = "工具卡_比例與分配"
UNIT = "第1章 特殊數學應用專題．L1 比例與分配"
FOOT = "高三數學．第1章 特殊數學應用專題．L1 比例與分配"

# ================================================================ 圖形
def _fig(name, svg):
    png = os.path.join(FIGS, name + ".png")
    ds.svg_to_png(svg, png)
    ds.save_svg(svg, os.path.join(FIGS, name + ".svg"))
    return png, svg


# 練習A：半成品條形圖——框已畫好，格子留白讓學生填數字
SVG_A1 = ds.bar_model([
    {"label": "原子筆", "cells": [("", 1)] * 5},
    {"label": "鉛筆", "cells": [("", 1)] * 7},
    {"label": "合共", "cells": [("", 1)] * 12, "brace": "72 支"},
], width=580, label_w=78, title="每一格填同一個數")
PNG_A1, _ = _fig("prac_a1", SVG_A1)

SVG_A2 = ds.bar_model([
    {"label": "甲箱", "cells": [("", 1)] * 3},
    {"label": "乙箱", "cells": [("", 1)] * 5},
    {"label": "合共", "cells": [("", 1)] * 8, "brace": "96 個"},
], width=580, label_w=78, title="每一格填同一個數")
PNG_A2, _ = _fig("prac_a2", SVG_A2)

# 練習B：只給空白格線，條要分幾格、怎麼標由學生自己決定
SVG_B = ds.grid_paper(cols=12, rows=4, cell=38)
PNG_B1, _ = _fig("prac_b1", SVG_B)
PNG_B2, _ = _fig("prac_b2", SVG_B)

# ================================================================ 題目
STEMS = {
    1: "文具店盤點文具，原子筆與鉛筆共 72 支。已知原子筆的支數是鉛筆的 {5/7}。"
       "問鉛筆有多少支？",
    2: "甲、乙兩箱蘋果共 96 個。已知甲箱的個數是乙箱的 {3/5}。"
       "問甲箱比乙箱少多少個？",
    3: "某機關把一筆獎金 84 000 元，按 2：3：7 分給甲、乙、丙三個部門。"
       "問分得最多的部門，比分得最少的部門多多少元？",
    4: "某機關招考約僱員工，錄取率為 25%，實際錄取 310 人。"
       "問（a）報考人數是多少人？（b）未獲錄取的有多少人？",
    5: "同一款計算機，兩間店的定價相同。A 店：定價先打 9 折，會員再打 85 折；"
       "B 店：先依定價減價 20% 作為售價，會員再打 9 折。"
       "問（a）到哪一間買比較便宜？（b）便宜了定價的百分之幾？",
    6: "水果店的蘋果、橙、梨數量比是 4：5：6。現在蘋果減少 25%，橙增加 20%，"
       "梨減少 {1/3}。問三者新的數量比是多少（化成最簡整數比）？",
}

# 練習A 的三欄式：第①②欄先填一半（褪除梯度第一階）
TC_A1 = [
    (["圈出「共 72 支」。", "圈出「原子筆是鉛筆的 {5/7}」。", "劃出所求：＿＿＿＿＿＿"],
     ["設 1 格 ＝ {u} 支。", "原子筆 ＝ ＿ 格，鉛筆 ＝ ＿ 格。"],
     []),
    (["「共」就是兩者相加。"], ["＿ {u} ＋ ＿ {u} ＝ 72"], []),
    (["問的是鉛筆，不是原子筆。"], [], []),
]
TC_A2 = [
    (["圈出「共 96 個」。", "圈出「甲箱是乙箱的 {3/5}」。", "劃出所求：＿＿＿＿＿＿"],
     ["設 1 格 ＝ {u} 個。", "甲箱 ＝ ＿ 格，乙箱 ＝ ＿ 格。"],
     []),
    (["「共」就是兩者相加。"], [], []),
    (["「少多少」＝格數差。"], [], []),
]
TC_BLANK = [([], [], []), ([], [], []), ([], [], [])]

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="42 支",
        kp="比例分配（部分—整體）：把「甲是乙的 {m/n}」轉成「甲 m 格、乙 n 格」，"
           "再用總量除以總格數求出一格。",
        fm="設 1 格 ＝ {u}，則 甲 ＝ {mu}、乙 ＝ {nu}，且 {mu+nu=} 總量。",
        steps=["原子筆是鉛筆的 {5/7} → 原子筆畫 5 格，鉛筆畫 7 格。",
               "兩者合共 {5+7=12} 格，對應 72 支：{12u=72}。",
               "{u=72/12=6}（支）。",
               "鉛筆 ＝ {7u=7*6=42}（支）。",
               "檢核：原子筆 {5*6=30} 支，{30+42=72}，且 {30/42=5/7}，與題意相符。"],
        pit="問的是「鉛筆」不是原子筆，也不是一格的值。算出 {u=6} 之後很多人就停手，"
            "或把 5 格的那一條當成答案。"),
    2: dict(
        ans="24 個",
        kp="比例比較（求差）：差就是「格數差 × 一格的值」，不必先分別算出兩個量。",
        fm="差 ＝（多的格數 − 少的格數）{*u}。",
        steps=["甲是乙的 {3/5} → 甲畫 3 格，乙畫 5 格。",
               "合共 {3+5=8} 格，對應 96 個：{8u=96}，{u=96/8=12}（個）。",
               "格數差 ＝ {5-3=2}（格）。",
               "少的個數 ＝ {2u=2*12=24}（個）。",
               "檢核：甲 {3*12=36} 個、乙 {5*12=60} 個，{36+60=96}，{60-36=24}，相符。"],
        pit="把「甲是乙的 {3/5}」誤讀成「甲比乙少 {3/5}」。前者是甲佔 3 格、乙佔 5 格；"
            "後者才是乙的 {3/5} 被扣掉。"),
    3: dict(
        ans="35 000 元",
        kp="連比分配：{a:b:c} 就是 a 格、b 格、c 格，總格數 ＝ {a+b+c}。",
        fm="每份 ＝ 總量 ÷（{a+b+c}）；某部門所得 ＝ 該部門格數 {*} 每份。",
        steps=["2：3：7 → 三條分別畫 2 格、3 格、7 格，合共 {2+3+7=12} 格。",
               "{12u=84000}，{u=84000/12=7000}（元）。",
               "最多的是丙（7 格），最少的是甲（2 格），格數差 {7-2=5} 格。",
               "多出的金額 ＝ {5*7000=35000}（元）。",
               "檢核：{2*7000=14000}、{3*7000=21000}、{7*7000=49000}；"
               "{14000+21000+49000=84000}，且 {49000-14000=35000}，相符。"],
        pit="用「84000 除以 3」平均分——連比不是平均分。另一個常見錯是把答案寫成"
            "最多的那一份 49 000 元，沒有看清楚問的是「多多少」。"),
    4: dict(
        ans="（a）1 240 人　（b）930 人",
        kp="百分率的分母判斷：錄取率的分母是「報考人數（全體）」，不是錄取人數。",
        fm="錄取率 ＝ 錄取人數 ÷ 報考人數 → 報考人數 ＝ 錄取人數 ÷ 錄取率。",
        steps=["錄取率 25% ＝ {1/4} → 全體畫 4 格，錄取佔其中 1 格。",
               "1 格 ＝ 310 人。",
               "（a）報考人數 ＝ {4*310=1240}（人）。",
               "（b）未獲錄取 ＝ 3 格 ＝ {3*310=930}（人）。",
               "檢核：{310/1240=0.25}，即 25%，相符。"],
        pit="把 310 當成全體去乘 25%（{310*0.25=77.5}），方向剛好相反。"
            "看到「率」先問一句：分母是誰。"),
    5: dict(
        ans="（a）B 店比較便宜　（b）便宜了定價的 4.5%",
        kp="連續折扣：兩次折扣要「相乘」，不是相加，也不是取平均。",
        fm="最後售價 ＝ 定價 {*} 第一次折數 {*} 第二次折數。",
        steps=["設定價為 1（畫成一整條，每次打折就是把整條按比例縮短一次）。",
               "A 店：{1*0.9*0.85=0.765}，即定價的 76.5%。",
               "B 店：減價 20% 表示售價是定價的 {0.8}，再打 9 折："
               "{1*0.8*0.9=0.72}，即定價的 72%。",
               "（a）{0.72<0.765}，所以 B 店比較便宜。",
               "（b）相差 {0.765-0.72=0.045}，即定價的 4.5%。"],
        pit="① 把「打 9 折再打 85 折」加起來當成打 {(9+8.5)} 折；"
            "② 把「減價 20%」直接寫成 {*0.2}（那是減掉之後剩 20%，錯得很遠）；"
            "③ 沒有把兩間換算成同一個基準（定價）就直接比較。"),
    6: dict(
        ans="3：6：4",
        kp="比的變化：先把比當成實際份數，各自乘上變化倍率，再重新化成最簡整數比。",
        fm="增加 p% → {*(1+p/100)}；減少 p% → {*(1-p/100)}；減少 {1/3} → {*2/3}。",
        steps=["取蘋果 4 份、橙 5 份、梨 6 份（三條分別畫 4、5、6 格）。",
               "蘋果減少 25%：{4*0.75=3}。",
               "橙增加 20%：{5*1.2=6}。",
               "梨減少 {1/3}：{6*2/3=4}。",
               "新的比 ＝ 3：6：4（三數的最大公因數為 1，已是最簡）。",
               "檢核：{3/4=0.75}（減 25%）、{6/5=1.2}（增 20%）、{4/6=2/3}（減 {1/3}），相符。"],
        pit="① 把「減少 25%」寫成 {*0.25}；② 把「減少 {1/3}」寫成 {-1/3}（那是減去 1/3 份，"
            "不是減去三分之一）；③ 算完忘記化成最簡整數比。"),
}

HINT_TOP = ("動手之前先翻開《課堂講義》第三節的範例，照「圈關鍵字 → 畫條形圖 → 填三欄表」"
            "的次序做。每一題都先畫圖再列式，不要心算。")

SELFCHECK = ["每一題都畫了條形圖（或標出格數）。",
             "每一格代表的數值有寫出來。",
             "答案回頭代入題目檢查過一次。",
             "答案有寫單位（支／個／元／人／％）。"]


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    # ---- 練習A ----
    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("條形圖的框已經畫好，只要在格子裡填數字；三欄表的第①②欄已經填了一半。"))
    for n, png, tc in ((1, PNG_A1, TC_A1), (2, PNG_A2, TC_A2)):
        P.append(problem_box([para(f"{n}．{STEMS[n]}")]))
        P.append(image_para(png, width_cm=13.5))
        P.append(three_column_table(tc))
        P.append(para("作答："))
        P += write_lines(4)
        P.append(blank())

    # ---- 練習B ----
    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("這一節只給空白格線：要分幾格、每格代表什麼，由自己決定；三欄表也全部留白。"))
    for n, png in ((3, PNG_B1), (4, PNG_B2)):
        P.append(problem_box([para(f"{n}．{STEMS[n]}")]))
        P.append(para("條形圖作答區（自己分段）："))
        P.append(image_para(png, width_cm=13.5))
        P.append(three_column_table(TC_BLANK))
        P.append(para("作答："))
        P += write_lines(6)
        P.append(blank())

    # ---- 練習C ----
    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("這一節不給圖也不給三欄表。請自己在空白處畫圖、列式，並把每一步為什麼這樣做寫出來。"))
    for n in (5, 6):
        P.append(problem_box([para(f"{n}．{STEMS[n]}")] + write_lines(7)))
        P.append(blank())

    P.append(selfcheck_list(SELFCHECK))

    # ---- 參考答案 ----
    P.append(heading("參考答案與詳解（教師用）", page_break_before=True))
    for n in range(1, 7):
        a = ANS[n]
        P.append(para(f"{n}．答案：{a['ans']}", bold=True))
        P.append(para(f"【考點】{a['kp']}"))
        P.append(para(f"【公式／定理】{a['fm']}"))
        P.append(para("【詳細步驟】"))
        for i, s in enumerate(a["steps"], 1):
            P.append(para(f"　（{i}）{s}"))
        P.append(shaded_box(f"【易錯點提示】{a['pit']}"))
        P.append(blank())

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ================================================================ 工具卡
CARDS = [
    ("▍關鍵字對譯卡（一般）",
     "什麼時候翻我：讀完題目、還沒動筆畫圖之前。",
     ["「甲和乙共有 N」→ 甲的格數 ＋ 乙的格數 ＝ N",
      "「甲是乙的 {m/n}」→ 乙畫 n 格，甲畫 m 格",
      "「甲與乙的比是 m：n」→ 甲 m 格，乙 n 格",
      "「甲佔全部的 p%」→ 全部畫 100/p 格，甲取其中 1 格",
      "「平均每人……」→ 總量 ÷ 份數",
      "「相差／多多少／少多少」→ 長的格數 − 短的格數"]),
    ("⚠ 陷阱詞卡",
     "什麼時候翻我：題目出現「倍」「率」「折」「%」任何一個字的時候。",
     ["「比乙多 3 倍」＝ 乙的 4 倍（不是 3 倍）",
      "「錄取率 25%」→ 分母是「報考人數」，不是錄取人數",
      "「先打 9 折再打 85 折」→ {*0.9*0.85}，兩次折扣要相乘",
      "「減價 20%」→ 售價 ＝ 定價 {*0.8}（不是 {*0.2}）",
      "「減少 {1/3}」→ {*2/3}（不是減去 1/3 這個數）",
      "「不超過／至少」→ {<=} ／ {>=}，答案是一個範圍"]),
    ("▍畫圖四個動作",
     "什麼時候翻我：每一題開始的時候，從動作 1 做起。",
     ["動作 1　圈出「共」「比」「是……的幾倍」「相差」。",
      "動作 2　哪一個量畫最少格，先畫它。",
      "動作 3　數總格數 → 總量 ÷ 總格數 ＝ 一格是多少。",
      "動作 4　看清楚問哪一段，乘回去，寫單位。",
      "※ 先數格再算一格，順序不要顛倒。"]),
    ("▍條形圖三種畫法",
     "什麼時候翻我：不確定這一題該畫成什麼樣子的時候。",
     ["部分—整體：一整條切成幾份（全班分成男生、女生）。",
      "比較：兩條並排，長度差 ＝ 相差（甲比乙少幾支）。",
      "前後變化：同一個量畫「前」「後」兩條（打折前／打折後）。",
      "※ 一題只挑一種，不要混用。"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in CARDS:
        c = [para(title, bold=True, sz=HEADING_SZ),
             para(trig, sz=21)]
        c += [para("・" + t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=3900))
    return build_docx(P, os.path.join(HERE, CARD + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm", "*": r"\times"}


def _tex(m):
    import re
    m = m.strip()
    f = re.fullmatch(r"(\d+)/(\d+)", m)
    if f:
        return r"\(\frac{%s}{%s}\)" % f.groups()
    body = m
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    body = re.sub(r"(\d+)/(\d+)", r"\\frac{\1}{\2}", body)
    body = body.replace("%", r"\%")
    return r"\(%s\)" % body


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out).replace("**", "")


def _svg_inline(svg):
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def _tc_html(rows):
    body = "".join(
        "<tr>" + "".join('<td class="fill">' + "".join(f"<div>{_h(x)}</div>" for x in col)
                         + "</td>" for col in row) + "</tr>"
        for rows_ in [rows] for row in rows_)
    return ('<table class="d-tbl three-col">'
            "<tr><th>① 語意擷取（圈已知、劃所求）</th><th>② 關係式建構</th>"
            "<th>③ 運算與檢核</th></tr>" + body + "</table>")


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    secA = ""
    for n, svg, tc in ((1, SVG_A1, TC_A1), (2, SVG_A2, TC_A2)):
        secA += (f'<div class="problem"><div>{n}．{_h(STEMS[n])}</div>'
                 f'<div class="fig">{_svg_inline(svg)}</div>'
                 f'{_tc_html(tc)}<div>作答：</div>{_lines(4)}</div>')
    secB = ""
    for n in (3, 4):
        secB += (f'<div class="problem"><div>{n}．{_h(STEMS[n])}</div>'
                 f'<div>條形圖作答區（自己分段）：</div>'
                 f'<div class="fig">{_svg_inline(SVG_B)}</div>'
                 f'{_tc_html(TC_BLANK)}<div>作答：</div>{_lines(6)}</div>')
    secC = ""
    for n in (5, 6):
        secC += (f'<div class="problem"><div>{n}．{_h(STEMS[n])}</div>{_lines(7)}</div>')

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for n in range(1, 7):
        a = ANS[n]
        steps = "".join(f"<div>　（{i}）{_h(s)}</div>" for i, s in enumerate(a["steps"], 1))
        ansec += (f'<div class="problem"><div style="font-weight:700">{n}．答案：'
                  f'{_h(a["ans"])}</div>'
                  f'<div>【考點】{_h(a["kp"])}</div>'
                  f'<div>【公式／定理】{_h(a["fm"])}</div>'
                  f'<div>【詳細步驟】</div>{steps}'
                  f'<div class="hint-card">【易錯點提示】{_h(a["pit"])}</div></div>')

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>條形圖的框已經畫好，只要在格子裡填數字；三欄表的第①②欄已經填了一半。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>這一節只給空白格線：要分幾格、每格代表什麼，由自己決定；三欄表也全部留白。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>這一節不給圖也不給三欄表。請自己在空白處畫圖、列式，並把每一步為什麼這樣做寫出來。</div>
  {secC}

  {chk}

  <div class="section-h page-break">參考答案與詳解（教師用）</div>
  {ansec}

  <div class="footer">{_esc(FOOT)}</div>

</div>
</body>
</html>
"""
    path = os.path.join(HERE, BASE + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_practice_docx())
    print(build_toolcard_docx())
    print(build_practice_html())
