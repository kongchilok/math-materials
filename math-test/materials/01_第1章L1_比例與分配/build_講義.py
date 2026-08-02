# -*- coding: utf-8 -*-
"""
第1章 特殊數學應用專題．L1 比例與分配 —— 課堂講義 build script
主設計 D1 條形模型；輔助 D8 關鍵字對譯表、D4 三欄式引導。鷹架密度：抽離小班 (Tier 2)。
產出：講義_比例與分配_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
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
BASE = "講義_比例與分配_抽離小班共用版"
UNIT = "第1章 特殊數學應用專題．L1 比例與分配"

# ---------------------------------------------------------------- 圖形（D1）
BARS = [
    {"label": "原子筆①", "cells": [("u", 1)] * 3},
    {"label": "鉛筆②", "cells": [("u", 1)] * 4},
    {"label": "合共", "cells": [("u", 1)] * 7, "brace": "63 支"},
]
# label_w 預設 54 會把「原子筆①」左邊切掉（實測），加寬到 78
svg = ds.bar_model(BARS, width=580, label_w=78, title="一格 = 同樣多的支數")
PNG = os.path.join(FIGS, "bar_example.png")
ds.svg_to_png(svg, PNG)
ds.save_svg(svg, os.path.join(FIGS, "bar_example.svg"))

# ---------------------------------------------------------------- 文字內容
INTRO = [
    "公職試的應用題，多數不是卡在計算，而是卡在「讀完題目之後，不知道要把哪一個數字跟哪一個數字放在一起」。"
    "這一課的做法是把文字先畫成長度：題目裡最小的那一份畫成一格，其餘的量都用同樣大小的格去堆。"
    "格數排好了，算式自己就會浮出來。",
    "條形圖有三種畫法，依題目的情境挑一種，不要混用：",
    "1. 部分—整體：一個整體被拆成幾份（例：全班分成男生與女生）。",
    "2. 比較：兩個量並排，長度差就是「相差」（例：原子筆比鉛筆少幾支）。",
    "3. 前後變化：同一個量在事情發生前、發生後各畫一條（例：打折前與打折後的價格）。",
]

KW_GENERAL = [
    ("甲和乙共有 63 支", "甲的格數加乙的格數，總和等於 63"),
    ("甲是乙的 {3/4}", "乙畫 4 格，甲畫 3 格"),
    ("甲與乙的比是 3：4", "甲畫 3 格，乙畫 4 格"),
    ("甲佔全部的 20%", "全部畫 5 格，甲取其中 1 格"),
    ("平均每人……", "總量 ÷ 份數"),
    ("相差／多多少／少多少", "長的格數 − 短的格數"),
]
KW_TRAPS = [
    ("甲比乙多 3 倍", "甲是乙的 4 倍（乙 1 格，甲 4 格）；「甲是乙的 3 倍」才是甲 3 格"),
    ("錄取率 25%", "分母是報考人數（全體），不是錄取人數"),
    ("先打 9 折，再打 85 折", "定價 {*0.9*0.85=} 定價 {*0.765}，不是打 (9＋8.5) 折"),
    ("依定價減價 20%", "售價 ＝ 定價 {*0.8}，不是定價 {*0.2}"),
    ("不超過 ／ 至少", "{<=} ／ {>=}，答案是一個範圍，不是單一個數"),
]

EXAMPLE_STEM = ("【範例】文具店某日賣出原子筆與鉛筆共 63 支。已知原子筆的支數是鉛筆的 {3/4}。"
                "問原子筆比鉛筆少賣了多少支？")

THREE_COL = [
    ([para("圈出「共 63 支」。"),
      para("圈出「原子筆是鉛筆的 {3/4}」。"),
      para("劃出所求：「少賣了多少支」。")],
     [para("設 1 格 ＝ {u} 支。"),
      para("原子筆① ＝ 3 格，鉛筆② ＝ 4 格。")],
     [para("（先不動手算，等關係式列完。）")]),

    ([para("「共」就是兩者相加。")],
     [para("{3u+4u=63}")],
     [para("{7u=63}"), para("{u=9}")]),

    ([para("「少賣多少」就是格數差。")],
     [para("{4u-3u=1u}")],
     [para("{1*9=9}（支）")]),

    ([para("回頭對照題意檢核。")],
     [para("原子筆 {3*9=27} 支"), para("鉛筆 {4*9=36} 支")],
     [para("{27+36=63}，與題目相符。"),
      para("{27/36} 約簡得 {3/4}，與題目相符。"),
      para("答：原子筆比鉛筆少賣 9 支。")]),
]

ACTIONS = [
    "動作 1　讀題，把「共」「比」「是……的幾倍」「相差」圈起來，關鍵字劃單底線、陷阱詞劃雙底線。",
    "動作 2　決定哪一個量畫最少格，先畫它；其餘的量照倍數關係堆同樣大小的格。",
    "動作 3　數出總格數，用總量 ÷ 總格數，求出一格等於多少。",
    "動作 4　看清楚問題問的是哪一段，乘回去，寫上單位。",
]

TN = dict(
    main_design="D1 條形模型（Bar Model）",
    aux_designs=("D8 關鍵字對譯表", "D4 三欄式引導工作紙"),
    reason=(
        "本課題源自題庫 A1 應用題文字題中的比例／分配類（約 35 題），屬 teaching-designs.md 的 "
        "S1 文字應用題結構：核心瓶頸是「語義解碼 → 數量關係」的轉換失敗，而非計算能力不足。"
        "D1 把文字直接轉成看得見的長度關係，學生不必先掌握移項規則就能看出關係；"
        "D8 專門處理本類題目的語言陷阱（「比……多幾倍」「先打 9 折再打 85 折」「錄取率」）；"
        "D4 把讀題、列式、計算三種互相干擾的認知活動在版面上物理分離。"),
    density="抽離小班（Tier 2）",
    fading=(
        "條形圖：講義範例給完整圖 → 練習A 給半成品圖只填數字 → 練習B 只給空白條框自行分段 → "
        "練習C 只給文字、圖自畫 → 第 2 課起只提示「請先畫圖」四個字 → 第 4 課完全不提示。｜"
        "關鍵字對譯表：本課講義內附並另發工具卡 → 第 2 課只留陷阱詞一欄 → 第 3 課只在課前發一次 → "
        "第 4 課移除，改由學生自行在題目上做記號。｜"
        "三欄式：範例三欄全填 → 練習A 第①②欄填一半 → 練習B 三欄全空但欄位還在 → 練習C 欄位由學生自畫。"),
    flows=("F5 課前流程預告（今天四件事：對譯表 → 範例 → 練習A → 核對）",
           "F1 師徒制對話四步（追問「這一格代表題目裡的什麼」，避免只會畫圖不會連回算式）"),
    iep_codes=("a3 提示題目重點", "a5 放大字體", "a6 增加行距",
               "a7 調整計分標準（分步給分；第一步筆誤而後續推理正確者，後續不重複扣分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度，未刪減內容。"),
           ("配套文件",
            "《第1章 L1 比例與分配　課堂練習》（練習A／B／C ＋參考答案）、"
            "《第1章 L1 比例與分配　工具卡》（關鍵字對譯卡，學生剪下護貝放桌面）。")),
)


# ---------------------------------------------------------------- docx
def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、關鍵字對譯表"))
    P.append(para("讀題時先在題目上做記號：一般關鍵字劃單底線，陷阱詞劃雙底線，再開始畫圖。"))
    P.append(keyword_table(KW_GENERAL, KW_TRAPS))

    P.append(heading("三、範例：把一題完整走一次"))
    P.append(problem_box([para(EXAMPLE_STEM)]))
    P.append(para("第 1 步　畫圖。鉛筆是被比較的對象，畫 4 格；原子筆是鉛筆的 {3/4}，畫 3 格。"
                  "兩者合起來共 7 格，對應題目的 63 支。"))
    P.append(image_para(PNG, width_cm=13.5, caption="範例的條形圖：每一格代表同樣多的支數"))
    P.append(para("第 2 步　把上面的圖填進三欄表，一欄一件事，不要跳欄。"))
    P.append(three_column_table(THREE_COL))
    P.append(shaded_box("※ 圖畫好之後，先數「一共有多少格」，再算「一格等於多少」——"
                        "這一步做對了，後面全部都只是乘法。"))

    P.append(heading("四、自己動手時的四個動作"))
    for t in ACTIONS:
        P.append(shaded_box(t))

    P.append(heading("五、接下來"))
    P.append(para("請拿出《第1章 L1 比例與分配　課堂練習》，依照上面四個動作完成練習A、練習B、練習C。"
                  "練習A 的條形圖已經畫好一半，只要填數字；練習B 只給空白條框，要自己分段；"
                  "練習C 只有文字，圖由自己畫。"))

    P += teacher_notes(**TN)
    out = build_docx(P, os.path.join(HERE, BASE + ".docx"),
                     footer_text="高三數學．第1章 特殊數學應用專題．L1 比例與分配")
    return out


# ---------------------------------------------------------------- HTML
def _h(s):
    """把 {} 標記轉成 MathJax 行內式，並轉義 HTML 特殊字元。"""
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm", "*": r"\times"}


def _tex(m):
    import re
    m = m.strip()
    frac = re.fullmatch(r"(\d+)/(\d+)", m)
    if frac:
        return r"\(\frac{%s}{%s}\)" % frac.groups()
    body = m
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    body = re.sub(r"(\d+)\s*\\times\s*(\d+)/(\d+)", r"\1 \\times \\frac{\2}{\3}", body)
    body = re.sub(r"(\d+)/(\d+)", r"\\frac{\1}{\2}", body)
    return r"\(%s\)" % body


def build_html_file():
    fig_svg = svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")
    kw_rows = "".join(
        f"<tr><td>{_h(k)}</td><td>{_h(v)}</td></tr>" for k, v in KW_GENERAL)
    kw_rows += ('<tr class="trap"><td colspan="2">⚠ 陷阱詞（要想一下，不能直接照字面翻）</td></tr>')
    kw_rows += "".join(f"<tr><td>{_h(k)}</td><td>{_h(v)}</td></tr>" for k, v in KW_TRAPS)

    # 三欄式：從 docx 用的同一份資料重建，兩版外觀一致
    TC_TEXT = [
        (["圈出「共 63 支」。", "圈出「原子筆是鉛筆的 {3/4}」。", "劃出所求：「少賣了多少支」。"],
         ["設 1 格 ＝ {u} 支。", "原子筆① ＝ 3 格，鉛筆② ＝ 4 格。"],
         ["（先不動手算，等關係式列完。）"]),
        (["「共」就是兩者相加。"], ["{3u+4u=63}"], ["{7u=63}", "{u=9}"]),
        (["「少賣多少」就是格數差。"], ["{4u-3u=1u}"], ["{1*9=9}（支）"]),
        (["回頭對照題意檢核。"], ["原子筆 {3*9=27} 支", "鉛筆 {4*9=36} 支"],
         ["{27+36=63}，與題目相符。", "{27/36} 約簡得 {3/4}，與題目相符。",
          "答：原子筆比鉛筆少賣 9 支。"]),
    ]
    tc_rows = "".join(
        "<tr>" + "".join("<td>" + "".join(f"<div>{_h(x)}</div>" for x in col) + "</td>"
                         for col in row) + "</tr>"
        for row in TC_TEXT)

    intro = "".join(f"<div>{_h(t)}</div>" for t in INTRO)
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
    head = tpl[:tpl.index("</head>") + len("</head>")]
    head = head.replace("[講義標題]", f"講義：{UNIT}")

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂講義</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="section-h">一、這一課要做到的事</div>
  {intro}

  <div class="section-h">二、關鍵字對譯表</div>
  <div>讀題時先在題目上做記號：一般關鍵字劃<span class="kw-key">單底線</span>，陷阱詞劃<span class="kw-trap">雙底線</span>，再開始畫圖。</div>
  <table class="d-tbl kw-table">
    <tr><th>題目說…</th><th>就寫成…</th></tr>
    {kw_rows}
  </table>

  <div class="section-h">三、範例：把一題完整走一次</div>
  <div class="problem">{_h(EXAMPLE_STEM)}</div>
  <div>第 1 步　畫圖。鉛筆是被比較的對象，畫 4 格；原子筆是鉛筆的 {_h('{3/4}')}，畫 3 格。兩者合起來共 7 格，對應題目的 63 支。</div>
  <div class="fig">{fig_svg}
    <div class="cap">範例的條形圖：每一格代表同樣多的支數</div>
  </div>
  <div>第 2 步　把上面的圖填進三欄表，一欄一件事，不要跳欄。</div>
  <table class="d-tbl three-col">
    <tr><th>① 語意擷取（圈已知、劃所求）</th><th>② 關係式建構</th><th>③ 運算與檢核</th></tr>
    {tc_rows}
  </table>
  <div class="hint-card">※ 圖畫好之後，先數「一共有多少格」，再算「一格等於多少」——這一步做對了，後面全部都只是乘法。</div>

  <div class="section-h">四、自己動手時的四個動作</div>
  {actions}

  <div class="section-h">五、接下來</div>
  <div>請拿出《第1章 L1 比例與分配　課堂練習》，依照上面四個動作完成練習A、練習B、練習C。練習A 的條形圖已經畫好一半，只要填數字；練習B 只給空白條框，要自己分段；練習C 只有文字，圖由自己畫。</div>

  <div class="footer">高三數學．第1章 特殊數學應用專題．L1 比例與分配</div>

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
