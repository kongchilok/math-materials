# -*- coding: utf-8 -*-
"""
第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯 —— 課堂講義 build script
主設計 D1 條形模型（前後變化型＋階梯分段型）；輔助 D8 關鍵字對譯表（本課只留陷阱詞一欄，
褪除路徑第 2 階）、D14 錯誤分析對比（正誤雙欄）。鷹架密度：抽離小班 (Tier 2)。
產出：講義_利潤折扣與費率_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
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
BASE = "講義_利潤折扣與費率_抽離小班共用版"
UNIT = "第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯"
FOOT = "高三數學．第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯"

# ---------------------------------------------------------------- 圖形（D1）
# 範例A：前後變化型——三條上下對齊，一眼看出「加價的基準是進價、打折的基準是標價」
BARS_A = [
    {"label": "進價", "cells": [("進價 250 元", 10)]},
    {"label": "標價", "cells": [("進價的 100%", 10), ("加 40%", 4)], "brace": "350 元"},
    {"label": "售價", "cells": [("進價 250 元", 10), ("賺", 1.2)], "brace": "280 元"},
]
SVG_A = ds.bar_model(BARS_A, width=580, label_w=78,
                     title="一整條 ＝ 進價（100%）；加價與打折各有各的基準")
PNG_A = os.path.join(FIGS, "ex_a_bar.png")
ds.svg_to_png(SVG_A, PNG_A)
ds.save_svg(SVG_A, os.path.join(FIGS, "ex_a_bar.svg"))

# 範例B：階梯分段型——整條按門檻切段，每段各乘自己的價
BARS_B = [
    {"label": "8 小時", "cells": [("2h×8元", 2), ("3h×12元", 3), ("3h×15元", 3)],
     "brace": "共 97 元"},
]
SVG_B = ds.bar_model(BARS_B, width=580, label_w=78,
                     title="整條 ＝ 停車 8 小時；按門檻切三段，每段乘自己的收費")
PNG_B = os.path.join(FIGS, "ex_b_bar.png")
ds.svg_to_png(SVG_B, PNG_B)
ds.save_svg(SVG_B, os.path.join(FIGS, "ex_b_bar.svg"))

# ---------------------------------------------------------------- 文字內容
INTRO = [
    "上一課的題目，數字之間是「幾比幾」的關係。這一課的題目換成百分比：打折、加價、利潤、"
    "利率、階梯收費——算式看起來只是乘一個小數，真正會做錯的地方只有一個，"
    "就是「這個百分比，是拿誰當 100%」。",
    "同一題裡的兩個百分比，基準往往不是同一個。範例A 的商品「按進價加價 40%」，"
    "那個 40% 的 100% 是進價；接著「按標價打八折」，那個 80% 的 100% 已經換成標價了。"
    "把基準看錯，後面每一步都對不了。",
    "所以這一課的做法是：先把基準量畫成一整條，長度定為 100%；變化之後的量另外畫一條，"
    "長短照百分比。兩條並排一看，差多少、賺多少，全部都看得見。",
    "階梯費率（電費、水費、稅、停車費）是同一個做法的變形：整條先按門檻切成幾段，"
    "每一段各自乘上該段的價，再把幾段加起來。",
]

# D8（本課只留陷阱詞一欄——一般對譯已在 L1 的工具卡上，本課不重印）
KW_TRAPS = [
    ("打八折", "售價 ＝ 定價 {*0.8}（付原價的 80%），不是 {*0.2}"),
    ("減價 15%", "售價 ＝ 定價 {*0.85}；「減價」要先用 {1-0.15} 換成剩下的比例"),
    ("先打八折，再減價 10%", "兩次的基準不同，要相乘：{0.8*0.9=0.72}；不可以寫成減 30%"),
    ("按進價加價 40%", "標價 ＝ 進價 {*1.4}；這裡的 100% 是進價"),
    ("利潤是進價的 20%", "利潤 ＝ 進價 {*0.2}；利潤率的分母是進價，不是售價"),
    ("每度 1.1 元（第二段）", "只有落在該段門檻之內的用量才乘 1.1，不是全部用量"),
    ("增長率 8%", "變化後 ＝ 變化前 {*1.08}；這裡的 100% 是變化前的量"),
]

# 基準量對照（D1 的判讀規則，用雙欄表呈現）
BASE_PAIRS = [
    ("題目說「打折」「折扣」「減價 p%」", "一整條 ＝ 定價（標價）\n售價 ＝ 定價 {*} 折數"),
    ("題目說「按進價加價 p%」「加成 p%」", "一整條 ＝ 進價（成本）\n標價 ＝ 進價 {*(1+p%)}"),
    ("題目說「利潤是進價的 p%」「利潤率 p%」", "一整條 ＝ 進價（成本）\n利潤 ＝ 售價 － 進價 ＝ 進價 {*p%}"),
    ("題目說「增加 p%」「增長率 p%」", "一整條 ＝ 變化前的量\n變化後 ＝ 變化前 {*(1+p%)}"),
    ("題目說「首 N 度……超過的部分……」", "整條按門檻切段，每段各乘自己的率\n總費用 ＝ 各段費用相加"),
]

EXAMPLE_A = ("【範例A】一部電風扇的進價是 250 元。店主按進價加價 40% 定出標價，"
             "再按標價打八折出售。問（a）售價是多少元？（b）店主每部賺多少元？")

STEPS_A = [
    "第 1 步　圈基準量。「按進價加價 40%」→ 這個 40% 的 100% 是進價；"
    "「按標價打八折」→ 這個 80% 的 100% 是標價。全題有兩個不同的基準。",
    "第 2 步　畫條。進價畫成一整條（10 格代表 100%），標價在它後面再接 40%，"
    "售價是標價的 80%，畫成比標價短、比進價長的一條。",
    "第 3 步　算標價。標價 ＝ {250*1.4=350}（元）。",
    "第 4 步　算售價。售價 ＝ {350*0.8=280}（元）。這是（a）的答案。",
    "第 5 步　算利潤。賺的就是圖上售價條超出進價條的那一小段："
    "{280-250=30}（元）。這是（b）的答案。",
    "第 6 步　反推檢核。利潤率 ＝ {30/250=0.12}，即進價的 12%；"
    "而 {1.4*0.8=1.12}，售價正好是進價的 112%，兩邊吻合。",
]

# D14 錯誤分析對比——只針對本課最高頻的那一組錯（基準量拿錯／折扣相加）
ERR_PAIRS = [
    ("「先打八折，再減價 10%」\n→ {20%+10%=30%}\n→ 售價 ＝ 定價 {*0.7}",
     "第二次的 10% 是拿「打折後的價」當 100%，不是定價。\n"
     "兩次要相乘：{0.8*0.9=0.72}，售價 ＝ 定價 {*0.72}。"),
    ("「利潤是進價的 20%」\n→ 利潤 ＝ 售價 {*0.2}",
     "利潤率的 100% 是進價。\n利潤 ＝ 進價 {*0.2}；售價 ＝ 進價 {*1.2}。"),
    ("「打八折」\n→ 售價 ＝ 定價 {*0.2}",
     "八折 ＝ 付原價的十分之八。\n售價 ＝ 定價 {*0.8}；被減掉的才是 {*0.2}。"),
    ("階梯電費用了 520 度\n→ {520*} 最高一段的每度價",
     "只有超過門檻的那一段才用最高價。\n前面每一段各用自己的價，最後相加。"),
]

EXAMPLE_B = ("【範例B】某停車場按時段收費：首 2 小時每小時 8 元；第 3 至第 5 小時每小時 12 元；"
             "第 6 小時起每小時 15 元。問停 8 小時要付多少元？")

STEPS_B = [
    "第 1 步　切段。8 小時落在三段裡：首 2 小時、第 3～5 小時（共 3 小時）、"
    "第 6～8 小時（共 3 小時）。先把時數加起來核一次：{2+3+3=8}，與題目相符。",
    "第 2 步　每段各自乘。首段 {2*8=16}（元）；第二段 {3*12=36}（元）；"
    "第三段 {3*15=45}（元）。",
    "第 3 步　相加。{16+36+45=97}（元）。",
    "第 4 步　反推檢核。若全部 8 小時都用最低價，只需 {8*8=64} 元；"
    "全部用最高價要 {8*15=120} 元。答案 97 落在 64 與 120 之間，合理。",
]

ACTIONS = [
    "動作 1　圈基準量。先問一句：「這個百分比，是拿誰當 100%？」把那個量圈起來"
    "（定價／進價／變化前的量）。一題出現兩個百分比，就要圈兩次。",
    "動作 2　畫條。基準量畫成一整條；有門檻的（首 N 度、首 N 小時），"
    "就按門檻把整條切成幾段。",
    "動作 3　一次變化畫一條。兩次變化就畫兩條，折數相乘，不可以把兩個百分比相加。",
    "動作 4　反推檢核。把算出來的答案代回去求一次那個率或那個差，"
    "看是不是等於題目給的數。",
]

TN = dict(
    main_design="D1 條形模型（Bar Model）——本課用「前後變化型」與「階梯分段型」兩種畫法",
    aux_designs=("D8 關鍵字對譯表（本課只保留陷阱詞一欄）", "D14 錯誤分析對比（正誤雙欄）"),
    reason=(
        "本課題源自題庫 A1 應用題文字題中的利潤／折扣／費率類（約 24 題），與 L1 同屬 "
        "teaching-designs.md 的 S1 文字應用題結構，故主設計沿用 D1，讓上一課建立的畫圖習慣"
        "直接遷移過來，不必再學一套新工具。"
        "但本課的認知瓶頸與 L1 不同：L1 卡在「讀不懂比例關係」，本課卡在「基準量（誰是 100%）"
        "在同一題內會換人」。因此 D1 的用法由 L1 的「部分—整體型」換成「前後變化型」，"
        "並新增「階梯分段型」處理電費／稅／停車費這一類分段收費。"
        "D8 保留但只留陷阱詞一欄（一般對譯已在 L1 工具卡上，屬褪除路徑第 2 階）。"
        "新增 D14 的依據是 teaching-designs.md 對 D14 的觸發條件——本課有一個已知高頻的固定錯法："
        "把兩次折扣相加、以及把利潤率的分母當成售價。D14 依規定排在範例A（正確版）之後、"
        "練習之前，不在學生見到正確版之前先給錯版。"),
    density="抽離小班（Tier 2）",
    fading=(
        "條形圖（D1）：L1 練習A 給半成品圖填數字 → 本課練習A 只給空白格線＋「請先畫圖」提示 → "
        "本課練習B、C 連格線都不給，只留文字提示 → L3 起完全不提示。｜"
        "關鍵字對譯（D8）：L1 講義附完整表＋工具卡 → 本課只留陷阱詞一欄（一般對譯不再重印） → "
        "L3 只在課前口頭發一次 → L4 移除，改由學生自行在題目上做記號。｜"
        "錯誤分析（D14）：本課講義給完整正誤雙欄 → 練習C 第 6 題只給錯誤解法，"
        "由學生自己找出分歧步驟並改正 → L3 只留一句「這題有一個常見陷阱，是什麼」 → L4 移除。"),
    flows=("F5 課前流程預告（今天四件事：陷阱詞 → 範例A → 錯法對照 → 範例B）",
           "F1 師徒制對話四步（追問「你這個百分比是拿誰當 100%」，"
           "這是本課唯一要學生講得出口的一句話）"),
    iep_codes=("a3 提示題目重點", "a5 放大字體", "a6 增加行距",
               "a7 調整計分標準（分步給分；基準量判斷正確但後續算術筆誤者，不重複扣分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L1 的銜接",
            "本課假設學生已完成《L1 比例與分配》，會畫條形圖並習慣「先畫圖再列式」。"
            "若學生未上過 L1，請先補畫圖的四個動作，再進入本課的基準量判斷。"),
           ("配套文件",
            "《第1章 L2 利潤、折扣與費率階梯　課堂練習》（練習A／B／C ＋參考答案）、"
            "《第1章 L2 利潤、折扣與費率階梯　工具卡》（基準量卡、陷阱詞卡，學生剪下護貝放桌面）。")),
)


# ---------------------------------------------------------------- docx
def _mp(text):
    """把含 \n 的儲存格文字拆成多個段落（表格內用）。"""
    return [para(t) for t in text.split("\n")]


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、先認出「一整條」是誰"))
    P.append(para("下表左欄是題目的說法，右欄是那一題的基準量與算式。讀題時先對照這張表，"
                  "把基準量圈起來，再開始畫圖。"))
    P.append(dual_track_table([(_mp(a), _mp(b)) for a, b in BASE_PAIRS],
                              headers=("題目這樣說…", "那「一整條」是誰 → 怎麼算")))

    P.append(heading("三、陷阱詞"))
    P.append(para("這幾個說法不能照字面直接翻成算式，讀到時要在題目上劃雙底線，停一停再寫。"))
    P.append(keyword_table([], KW_TRAPS))

    P.append(heading("四、範例A：同一題裡有兩個不同的基準"))
    P.append(problem_box([para(EXAMPLE_A)]))
    P.append(image_para(PNG_A, width_cm=13.5,
                        caption="進價是加價的基準，標價是打折的基準——兩個基準不同"))
    for t in STEPS_A:
        P.append(para(t))
    P.append(shaded_box("※ 圖上「售價條超出進價條」的那一小段，就是利潤。"
                        "看得見這一段，就不會把利潤率的分母寫成售價。"))

    P.append(heading("五、最常見的錯法（先看清楚，再做練習）"))
    P.append(para("左欄是學生最常寫出來的式子，右欄是它錯在哪裡、正確要怎麼寫。"
                  "四組錯法的病因其實是同一個：基準量拿錯了。"))
    P.append(dual_track_table([(_mp(a), _mp(b)) for a, b in ERR_PAIRS],
                              headers=("⚠ 常見的錯寫法（不要學）", "▍正確的寫法")))

    P.append(heading("六、範例B：階梯費率——整條切成幾段"))
    P.append(problem_box([para(EXAMPLE_B)]))
    P.append(image_para(PNG_B, width_cm=13.5,
                        caption="整條是 8 小時，按門檻切三段，每段各乘自己的收費"))
    for t in STEPS_B:
        P.append(para(t))
    P.append(shaded_box("※ 階梯題先做一件事：把各段的用量加起來，核對是否等於題目給的總用量。"
                        "這一步做了，分段就不會多算或少算。"))

    # 手動分頁：四個動作是學生解題時要一眼看齊的一組，不可被分頁拆開；
    # 同時避開頁尾白底覆蓋內文的危險帶（見 build_html_file 的註）。
    P.append(heading("七、自己動手時的四個動作", page_break_before=True))
    for t in ACTIONS:
        P.append(shaded_box(t))

    P.append(heading("八、接下來"))
    P.append(para("請拿出《第1章 L2 利潤、折扣與費率階梯　課堂練習》，依照上面四個動作完成"
                  "練習A、練習B、練習C。練習A 只給空白格線，條要怎麼畫由自己決定；"
                  "練習B 連格線都沒有，圖自己畫在空白處；"
                  "練習C 的最後一題是找錯題——別人的解法錯在哪一步，由你圈出來並改正。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ---------------------------------------------------------------- HTML
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
    return "".join(out)


def _cell(text):
    return "".join(f"<div>{_h(t)}</div>" for t in text.split("\n"))


def _svg_inline(svg):
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def build_html_file():
    base_rows = "".join(f"<tr><td>{_cell(a)}</td><td>{_cell(b)}</td></tr>"
                        for a, b in BASE_PAIRS)
    err_rows = "".join(f"<tr><td>{_cell(a)}</td><td>{_cell(b)}</td></tr>"
                       for a, b in ERR_PAIRS)
    kw_rows = ('<tr class="trap"><td colspan="2">⚠ 陷阱詞（要想一下，不能直接照字面翻）</td></tr>'
               + "".join(f"<tr><td>{_h(k)}</td><td>{_h(v)}</td></tr>" for k, v in KW_TRAPS))

    intro = "".join(f"<div>{_h(t)}</div>" for t in INTRO)
    steps_a = "".join(f"<div>{_h(t)}</div>" for t in STEPS_A)
    steps_b = "".join(f"<div>{_h(t)}</div>" for t in STEPS_B)
    actions = "".join(f'<div class="hint-card">{_h(t)}</div>' for t in ACTIONS)

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join(f"<tr><td>{_esc(k)}</td><td>{_esc(v)}</td></tr>" for k, v in tn_rows)

    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"講義：{UNIT}")
    # 列印分頁補強（只補分頁規則，不動 @page 邊界與 .footer 的 position，
    # QB-15c 的 position:fixed 計數維持 1）：
    #   灰底提示框／圖／表列不得被分頁切開；區塊標題不得與其表格拆散成孤兒標題。
    # 註：共用範本的 .footer 是 position:fixed＋白底，@page 沒有替它預留空間，
    #     內文一旦流到內容框底部，最後一行會被頁尾白底蓋住。已試過「加大 @page 下邊界＋
    #     負 bottom」與「translateY(100%)」兩種預留寫法，Chrome 都會把頁尾推到下一頁頁頂，
    #     兩種都不可用。本份改以第七節手動分頁避開危險帶（見 build 內的 page-break），
    #     範本層的修法待使用者裁決。
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .d-tbl tr { break-inside: avoid; }
  .keep { break-inside: avoid; }
  .section-h { break-after: avoid; }
</style>
</head>""")

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂講義</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="section-h">一、這一課要做到的事</div>
  {intro}

  <div class="section-h">二、先認出「一整條」是誰</div>
  <div>下表左欄是題目的說法，右欄是那一題的基準量與算式。讀題時先對照這張表，把基準量圈起來，再開始畫圖。</div>
  <table class="d-tbl dual-track">
    <tr><th>題目這樣說…</th><th>那「一整條」是誰 → 怎麼算</th></tr>
    {base_rows}
  </table>

  <div class="section-h">三、陷阱詞</div>
  <div>這幾個說法不能照字面直接翻成算式，讀到時要在題目上劃<span class="kw-trap">雙底線</span>，停一停再寫。</div>
  <table class="d-tbl kw-table">
    <tr><th>題目說…</th><th>就寫成…</th></tr>
    {kw_rows}
  </table>

  <div class="section-h">四、範例A：同一題裡有兩個不同的基準</div>
  <div class="problem">{_h(EXAMPLE_A)}</div>
  <div class="fig">{_svg_inline(SVG_A)}
    <div class="cap">進價是加價的基準，標價是打折的基準——兩個基準不同</div>
  </div>
  {steps_a}
  <div class="hint-card">※ 圖上「售價條超出進價條」的那一小段，就是利潤。看得見這一段，就不會把利潤率的分母寫成售價。</div>

  <div class="section-h">五、最常見的錯法（先看清楚，再做練習）</div>
  <div>左欄是學生最常寫出來的式子，右欄是它錯在哪裡、正確要怎麼寫。四組錯法的病因其實是同一個：基準量拿錯了。</div>
  <table class="d-tbl dual-track">
    <tr><th>⚠ 常見的錯寫法（不要學）</th><th>▍正確的寫法</th></tr>
    {err_rows}
  </table>

  <div class="section-h">六、範例B：階梯費率——整條切成幾段</div>
  <div class="problem">{_h(EXAMPLE_B)}</div>
  <div class="fig">{_svg_inline(SVG_B)}
    <div class="cap">整條是 8 小時，按門檻切三段，每段各乘自己的收費</div>
  </div>
  {steps_b}
  <div class="hint-card">※ 階梯題先做一件事：把各段的用量加起來，核對是否等於題目給的總用量。這一步做了，分段就不會多算或少算。</div>

  <div class="section-h page-break">七、自己動手時的四個動作</div>
  {actions}

  <div class="section-h">八、接下來</div>
  <div>請拿出《第1章 L2 利潤、折扣與費率階梯　課堂練習》，依照上面四個動作完成練習A、練習B、練習C。練習A 只給空白格線，條要怎麼畫由自己決定；練習B 連格線都沒有，圖自己畫在空白處；練習C 的最後一題是找錯題——別人的解法錯在哪一步，由你圈出來並改正。</div>

  <div class="footer">{_esc(FOOT)}</div>

  <div class="teacher-notes">
    <div class="section-h">教師實施說明（本頁供教師參考，列印給學生時可不印）</div>
    <table class="d-tbl">
      {tn}
    </table>
  </div>

</div>
</body>
</html>
"""
    path = os.path.join(HERE, BASE + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_docx_file())
    print(build_html_file())
