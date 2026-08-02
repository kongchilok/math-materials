# -*- coding: utf-8 -*-
"""
第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯 —— 課堂練習 ＋ 工具卡 build script
主設計 D1 條形模型（前後變化型／階梯分段型）；輔助 D8 陷阱詞、D14 錯誤分析對比。
鷹架密度：抽離小班 (Tier 2)。
褪除梯度（比 L1 再退一階）：
  A 只給空白格線＋基準量勾選（不再給半成品圖）→ B 連格線都不給，只留「請先畫圖」→
  C 純文字，且第 6 題改成 D14 找錯題（給別人的錯誤解法，自己找出分歧步驟並改正）。
產出：練習_利潤折扣與費率_抽離小班共用版.docx/.html/.pdf、工具卡_利潤折扣與費率.docx/.pdf
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
BASE = "練習_利潤折扣與費率_抽離小班共用版"
CARD = "工具卡_利潤折扣與費率"
UNIT = "第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯"
FOOT = "高三數學．第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯"

# ================================================================ 圖形
# 練習A：只給空白格線（L1 練習A 是半成品圖填數字，本課退一階）
SVG_GRID = ds.grid_paper(cols=12, rows=4, cell=38)
PNG_A1 = os.path.join(FIGS, "prac_grid1.png")
PNG_A2 = os.path.join(FIGS, "prac_grid2.png")
for p in (PNG_A1, PNG_A2):
    ds.svg_to_png(SVG_GRID, p)
ds.save_svg(SVG_GRID, os.path.join(FIGS, "prac_grid.svg"))

# ================================================================ 題目
STEMS = {
    1: "某電器店一部座地風扇的定價是 800 元。店慶期間全場先打八折，會員憑卡再減價 5%。"
       "問會員買一部風扇實付多少元？",
    2: "一件外套的進價是 240 元。店主想在每件外套上賺取進價 35% 的利潤。"
       "問售價應該定為多少元？",
    3: "某商品按進價加價 25% 定出標價，後來以標價打九折出售，結果每件仍賺 35 元。"
       "問這件商品的進價是多少元？",
    4: "某地住宅用電按階梯收費：每月首 200 度，每度 0.8 元；第 201 至第 400 度，每度 1.1 元；"
       "超過 400 度的部分，每度 1.5 元。某住戶某月用電 520 度，問該月電費共多少元？",
    5: "某商品每件進價 270 元。商店訂出標價之後，以標價的九折出售，"
       "結果每件的利潤仍然是進價的 20%。問每件的標價是多少元？",
    6: "一件商品的定價是 500 元，商店先打八折，再從打折後的價錢減價 10%。問售價是多少元？",
}

# 第 6 題（D14 找錯題）附上的錯誤解法
WRONG_6 = [
    "小明的解法：",
    "　第一步　八折就是減價 20%。",
    "　第二步　兩次減價合共 {20%+10%=30%}。",
    "　第三步　售價 ＝ {500*(1-0.3)=350}（元）。",
    "問：（a）小明從哪一步開始錯？（b）把它改正，並算出正確的售價。",
]

BASE_PICK = ("這一題的「一整條」（基準量）是哪一個？先勾一個再動筆：　"
             "☐ 定價（標價）　　☐ 進價（成本）　　☐ 變化前的量　　☐ 每一段各自的用量")

HINT_TOP = ("動手之前先做一件事：把題目裡每一個百分比圈起來，問自己「這個百分比是拿誰當 100%」。"
            "基準量判斷對了，這一課的題目就只剩下乘除法。不確定就翻《課堂講義》第二節的對照表。")

SELFCHECK = ["每一題都先寫出「這一題的 100% 是誰」。",
             "同一題出現兩個百分比時，有分別確認過它們的基準是不是同一個。",
             "兩次折扣是用相乘處理的，沒有相加。",
             "階梯題有把各段的用量加起來，核對等於題目給的總用量。",
             "答案有反推檢核過一次，也有寫單位（元／度）。"]

# ================================================================ 參考答案（v1.3 四段式）
ANS = {
    1: dict(
        ans="608 元",
        kp="連續折扣：第二次折扣的基準是「第一次打折之後的價」，不是原定價，所以兩次要相乘。",
        fm="實付 ＝ 定價 {*} 第一次的比例 {*} 第二次的比例；打八折就是乘 {0.8}，"
           "減價 5% 就是乘 {0.95}。",
        steps=["圈基準量。第一個百分比（八折）的 100% 是定價 800 元；"
               "第二個百分比（減價 5%）的 100% 是打八折之後的價。兩個基準不同。",
               "打八折之後：{800*0.8=640}（元）。",
               "再減價 5%，即付這 640 元的 95%：{640*0.95=608}（元）。",
               "反推檢核：{0.8*0.95=0.76}，{800*0.76=608}，與上面一致。"],
        pit="把兩次折扣加起來算成「共減 25%」而寫出 {800*0.75=600}。"
            "少算的 8 元就是「第二次的 5% 應該以 640 元為基準、卻誤用 800 元」造成的差額。"),
    2: dict(
        ans="324 元",
        kp="利潤率的基準是進價：利潤 ＝ 進價 {*} 利潤率，售價 ＝ 進價 ＋ 利潤。",
        fm="售價 ＝ 進價 {*(1+r)}，其中 {r} 是利潤率（本題 {r=0.35}）。",
        steps=["圈基準量。「賺取進價 35% 的利潤」→ 這個 35% 的 100% 是進價 240 元。",
               "畫圖：進價畫成一整條，利潤是接在它後面的一小段。",
               "利潤 ＝ {240*0.35=84}（元）。",
               "售價 ＝ {240+84=324}（元）；也可以一步寫成 {240*1.35=324}。",
               "反推檢核：{324-240=84}，{84/240=0.35}，即 35%，相符。"],
        pit="把利潤率的分母當成售價，寫成「售價 {*0.35=} 利潤」。"
            "只要記住利潤率的那一整條是進價，這個錯就不會發生。"),
    3: dict(
        ans="280 元",
        kp="逆推：兩次變化都以進價為統一基準表達，再用「利潤 ＝ 售價 － 進價」列一條方程。",
        fm="標價 ＝ 進價 {*1.25}；售價 ＝ 標價 {*0.9} ＝ 進價 {*1.125}；"
           "利潤 ＝ 售價 － 進價 ＝ 進價 {*0.125}。",
        steps=["設進價為 {c} 元（把進價畫成一整條，長度定為 100%）。",
               "加價 25% 定標價：標價 ＝ {1.25c}。",
               "標價打九折出售：售價 ＝ {1.25c*0.9=1.125c}。",
               "利潤 ＝ 售價 － 進價 ＝ {1.125c-c=0.125c}，題目說這等於 35 元：{0.125c=35}。",
               "{c=35/0.125=280}（元）。",
               "反推檢核：進價 280 → 標價 {280*1.25=350} → 打九折 {350*0.9=315} → "
               "利潤 {315-280=35}，與題目相符。"],
        pit="① 把打九折的基準當成進價（寫成 {c*0.9}）——打折的基準永遠是標價；"
            "② 直接用 {35/0.25=140} 求進價，那是把「加價 25%」當成最後的利潤率，"
            "但中間還打了一次九折，實際利潤率只有 12.5%。"),
    4: dict(
        ans="560 元",
        kp="階梯費率：整條按門檻切段，每段只用該段自己的單價，最後相加；不是全部用量乘同一個價。",
        fm="總費用 ＝ Σ（該段用量 {*} 該段單價）。",
        steps=["切段。520 度落在三段：首 200 度、第 201～400 度（共 200 度）、"
               "超過 400 度的部分（{520-400=120} 度）。",
               "核對用量：{200+200+120=520}（度），與題目相符。",
               "第一段：{200*0.8=160}（元）。",
               "第二段：{200*1.1=220}（元）。",
               "第三段：{120*1.5=180}（元）。",
               "總電費 ＝ {160+220+180=560}（元）。",
               "反推檢核：全部用最低價只需 {520*0.8=416} 元，全部用最高價要 {520*1.5=780} 元；"
               "560 落在兩者之間，合理。"],
        pit="① 用 {520*1.5=780}，把超過門檻那一段的單價套到全部用量；"
            "② 第二段的度數寫成 400 度（那是累計到 400 度，不是第二段本身的用量，"
            "第二段只有 {400-200=200} 度）。"),
    5: dict(
        ans="360 元",
        kp="一題兩個基準：利潤率以進價為 100%（先求售價），折扣以標價為 100%（再逆推標價）。",
        fm="售價 ＝ 進價 {*(1+r)}（{r} 為利潤率）；標價 ＝ 售價 除以 折數。",
        steps=["圈基準量。「利潤是進價的 20%」→ 基準是進價；「標價的九折」→ 基準是標價。",
               "先求售價（用進價這一條）：售價 ＝ {270*1.2=324}（元）。",
               "再逆推標價（用標價那一條）：標價 {*0.9=324}。",
               "標價 ＝ {324/0.9=360}（元）。",
               "反推檢核：{360*0.9=324}；利潤 {324-270=54}；{54/270=0.2}，即 20%，相符。"],
        pit="① 把 20% 直接加在標價上（寫成 標價 ＝ {270*1.2*0.9}），"
            "順序一顛倒就把兩個基準混在一起；② 求標價時用乘 0.9 而不是除以 0.9——"
            "打折是從標價「變小」到售價，逆推回去要除。"),
    6: dict(
        ans="（a）第二步開始錯　（b）正確售價 360 元",
        kp="錯在把兩次折扣的百分比相加。第二次的 10% 是拿「打折後的 400 元」當 100%，"
           "不是原定價 500 元；基準不同的百分比不能相加。",
        fm="售價 ＝ 定價 {*0.8*0.9}；兩次變化相乘，不是相加。",
        steps=["第一步「八折就是減價 20%」——這一步是對的，可以照用。",
               "第二步「兩次減價合共 30%」——錯在這裡。第一次的 20% 以 500 元為基準，"
               "第二次的 10% 以打折後的 400 元為基準，兩個百分比的「一整條」不一樣，不能相加。",
               "改正：打八折後 ＝ {500*0.8=400}（元）。",
               "再減價 10%，即付這 400 元的 90%：{400*0.9=360}（元）。",
               "反推檢核：{0.8*0.9=0.72}，{500*0.72=360}，與上面一致。",
               "小明的答案 350 元比正確答案少 10 元，差額正是 "
               "{500*(0.72-0.7)=10}（元）——就是基準看錯造成的。"],
        pit="這一題的第一步是對的，錯的是第二步；不少學生會把整個解法都劃掉重做，"
            "反而看不出錯在哪一個環節。找錯題要逐步比對，找出「從哪一步開始分歧」，"
            "而不是只判斷最後答案對不對。"),
}


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    # ---- 練習A ----
    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("本節只給空白格線，條要分幾格、每格代表什麼，全部由自己決定。"
                  "動筆之前先勾出這一題的基準量。"))
    for n, png in ((1, PNG_A1), (2, PNG_A2)):
        P.append(problem_box([para(f"{n}．{STEMS[n]}")]))
        P.append(shaded_box(BASE_PICK))
        P.append(para("條形圖作答區（請先畫圖）："))
        P.append(image_para(png, width_cm=13.5))
        P.append(para("作答："))
        P += write_lines(5)
        P.append(blank())

    # ---- 練習B ----
    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("本節連格線都沒有了。請先畫圖，圖畫在題目下方的空白處，再列式計算。"))
    for n in (3, 4):
        P.append(problem_box([para(f"{n}．{STEMS[n]}")]))
        P.append(para("請先畫圖，再作答："))
        P += write_lines(6)
        P.append(blank())

    # ---- 練習C ----
    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("本節不給任何鷹架。第 6 題是找錯題：別人的解法錯在哪一步，由你圈出來並改正。"))
    P.append(problem_box([para(f"5．{STEMS[5]}")] + write_lines(7)))
    P.append(blank())
    P.append(problem_box([para(f"6．{STEMS[6]}")]
                         + [para(t) for t in WRONG_6]
                         + write_lines(7)))
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
    ("▍基準量卡（誰是那一整條）",
     "什麼時候翻我：題目出現「折」「率」「%」「利潤」任何一個字的時候。",
     ["打折、折扣、減價 → 一整條 ＝ 定價（標價）",
      "加價、加成 → 一整條 ＝ 進價（成本）",
      "利潤、利潤率 → 一整條 ＝ 進價（成本）",
      "增加、增長率 → 一整條 ＝ 變化前的量",
      "首 N 度／首 N 小時 → 整條切段，每段各自算",
      "※ 一題有兩個百分比，就要問兩次「誰是 100%」。"]),
    ("⚠ 陷阱詞卡",
     "什麼時候翻我：寫下算式之前，先用這張卡對一次。",
     ["「打八折」→ 售價 ＝ 定價 {*0.8}（不是 {*0.2}）",
      "「減價 15%」→ 售價 ＝ 定價 {*0.85}",
      "「先打八折，再減價 10%」→ {0.8*0.9=0.72}，相乘不相加",
      "「按進價加價 40%」→ 標價 ＝ 進價 {*1.4}",
      "「利潤是進價的 20%」→ 分母是進價，不是售價",
      "「增長率 8%」→ 變化後 ＝ 變化前 {*1.08}"]),
    ("▍解題四個動作",
     "什麼時候翻我：每一題開始的時候，從動作 1 做起。",
     ["動作 1　圈基準量：這個百分比拿誰當 100%？",
      "動作 2　基準量畫成一整條；有門檻的就切段。",
      "動作 3　一次變化畫一條，兩次變化畫兩條，折數相乘。",
      "動作 4　反推檢核：把答案代回去算一次那個率。",
      "※ 先定基準再列式，順序不要顛倒。"]),
    ("▍階梯費率分段卡",
     "什麼時候翻我：題目出現「首 N 度」「超過的部分」「第 N 至第 M」的時候。",
     ["1　先按門檻把總量切成幾段。",
      "2　算出每一段各自的用量（不是累計數）。",
      "3　把各段用量加起來，核對等於總量。",
      "4　每段用量乘該段單價，再全部相加。",
      "※ 第二段的用量 ＝ 上限 － 下限，不是上限本身。"]),
]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    cards = []
    for title, trig, items in CARDS:
        c = [para(title, bold=True, sz=HEADING_SZ), para(trig, sz=21)]
        c += [para("・" + t, sz=21) for t in items]
        cards.append(c)
    P.append(toolcard_sheet(cards, cols=2, card_h=3900))
    return build_docx(P, os.path.join(HERE, CARD + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


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
    return "".join(out)


def _svg_inline(svg):
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")
    # 只補列印分頁規則（提示框／圖不得被切開、標題不得與內容拆散）；
    # 不動 @page 邊界與 .footer 的 position，QB-15c 的計數維持 1。
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
</style>
</head>""")

    secA = ""
    for n in (1, 2):
        secA += (f'<div class="problem"><div>{n}．{_h(STEMS[n])}</div>'
                 f'<div class="hint-card">{_esc(BASE_PICK)}</div>'
                 f'<div>條形圖作答區（請先畫圖）：</div>'
                 f'<div class="fig">{_svg_inline(SVG_GRID)}</div>'
                 f'<div>作答：</div>{_lines(5)}</div>')
    secB = ""
    for n in (3, 4):
        secB += (f'<div class="problem"><div>{n}．{_h(STEMS[n])}</div>'
                 f'<div>請先畫圖，再作答：</div>{_lines(6)}</div>')

    wrong = "".join(f"<div>{_h(t)}</div>" for t in WRONG_6)
    secC = (f'<div class="problem"><div>5．{_h(STEMS[5])}</div>{_lines(7)}</div>'
            f'<div class="problem"><div>6．{_h(STEMS[6])}</div>{wrong}{_lines(7)}</div>')

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
  <div>本節只給空白格線，條要分幾格、每格代表什麼，全部由自己決定。動筆之前先勾出這一題的基準量。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>本節連格線都沒有了。請先畫圖，圖畫在題目下方的空白處，再列式計算。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>本節不給任何鷹架。第 6 題是找錯題：別人的解法錯在哪一步，由你圈出來並改正。</div>
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
