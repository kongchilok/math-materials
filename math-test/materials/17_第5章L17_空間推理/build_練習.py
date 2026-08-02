# -*- coding: utf-8 -*-
"""
第5章 數理邏輯(三)．L17 空間推理 —— 課堂練習 build script
主設計 D7 提示卡；輔助 D5 圖文雙軌對照。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：練習A/B 保留簡化版雙軌表提示 → 練習C 只給圖，推理步驟自己寫。
全部題目為自編（題庫 B3/B6 原稿缺圖，詳見 驗算_空間推理.md §0）。
產出：練習_空間推理_抽離小班共用版.docx/.html/.pdf（本課設計無需獨立工具卡，
兩張提示卡已在講義出現，練習時翻返講義即可）。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import figs as f                             # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_空間推理_抽離小班共用版"
UNIT = "第5章 數理邏輯(三)．L17 空間推理"
FOOT = "高三數學．第5章 數理邏輯(三)．L17 空間推理"

HINT_TOP = "動手之前：翻開《課堂講義》嘅兩張提示卡（相對面法則／翻滾方向法則），照住查。"
SELFCHECK = ["我有將展開圖入面嘅方格編返位置(1,2,3,4)先搵相對面。",
             "翻滾題我有逐步查提示卡②嘅循環方向，冇靠感覺估。",
             "答案講得出「點解」，唔淨係靠直覺。"]

media = MediaRegistry()

# ---------------------------------------------------------------- 圖形
NET1 = {(0, 1): "2", (1, 0): "1", (1, 1): "3", (1, 2): "4", (1, 3): "5", (2, 1): "6"}
NET1_IMG = f.save("net1", f.net_grid(NET1), HERE)
NET1_H14 = f.save("net1_h14", f.net_grid(NET1, highlight={(1, 0), (1, 2)}), HERE)
NET1_H26 = f.save("net1_h26", f.net_grid(NET1, highlight={(0, 1), (2, 1)}), HERE)

media = MediaRegistry()


def dt(img, text, lines=2):
    return dual_track_table([(image_para(img, width_cm=7.5), text),
                             (None, write_lines(lines))], media=media,
                            headers=("圖形上發生什麼", "推理／作答"))


ANS = dict(
    A1=dict(ans="4", rule="橫排 1－3－4－5 對應位置1,2,3,4。1(位1)同4(位3)位置差{3-1=2}，相對。",
            steps=["橫排：1(位1)、3(位2)、4(位3)、5(位4)。", "位1同位3位置差{3-1=2}，即1同4相對。"],
            pit="誤將相鄰嘅3當成相對面（3只係1隔籬，位置差只得1，唔係2）。"),
    A2=dict(ans="6", rule="直排 2－3－6 對應位置1,2,3。2(位1)同6(位3)位置差{3-1=2}，相對。",
            steps=["直排：2(位1)、3(位2，同橫排共用嘅樞紐格)、6(位3)。",
                   "位1同位3位置差{3-1=2}，即2同6相對。"],
            pit="淨係識用橫排嗰條，冇諗到直排都要用同一條法則。"),
    B1=dict(ans="4", rule="設頂=2,前=3,右=4,左=1,後=5,底=6。向左滾：頂→左，左→底，底→右，右→頂。",
            steps=["查提示卡②「向左滾」：右→頂。", "原本嘅右面係4，所以新嘅頂面係4。"],
            pit="查錯行（用咗「向右滾」嗰行嘅對應），方向要對準題目講嘅先。"),
    B2=dict(ans="5", rule="設頂=2,前=3,右=4,左=1,後=5,底=6。向前滾：頂→前，前→底，底→後，後→頂。",
            steps=["查提示卡②「向前滾」：後→頂。", "原本嘅後面係5，所以新嘅頂面係5。"],
            pit="以為「向前滾」同「向右滾」規律一樣，冇留意向前滾影響嘅係『頂/前/底/後』"
                "四個面，唔係『頂/右/底/左』。"),
    C1=dict(ans="5", rule="設頂=2,前=3,右=4,左=1,後=5,底=6。先向右滾一下，再向前滾一下"
                        "（兩次翻滾疊加，逐步更新六個面）。",
            steps=["第一步（向右滾）：頂→右，右→底，底→左，左→頂；前／後不變。"
                   "新狀態：頂=1,前=3,右=2,底=4,左=6,後=5。",
                   "第二步（向前滾）：頂→前，前→底，底→後，後→頂；左／右不變。"
                   "用第一步嘅結果再滾一次：頂=5(原本嘅後)，前=1(原本嘅頂)，"
                   "底=3(原本嘅前)，後=4(原本嘅底)，左=6，右=2 不變。",
                   "最終頂面＝5。"],
            pit="兩次翻滾之間冇更新六個面嘅新狀態，直接用返最初嘅頂/前/右去查第二次，"
                "應該用第一次滾完之後嘅新狀態嚟做第二次嘅起點。"),
    C2=dict(ans="（開放題，教師逐份核對）",
            rule="出題者自訂6個面代號，畫十字形展開圖，用相對面法則寫低邊兩對面相對；"
                "再設計一個翻滾情境自己作答。",
            steps=["建議：展開圖用十字形（跟返講義範例形狀），先確保有標準答案可以驗算。",
                   "出題者要親自驗算：查提示卡兩次獨立核對，答案一致先算完成。"],
            pit="展開圖畫錯形狀（唔係合法嘅正方體展開圖），或者未親自驗算就當完成。"),
)


def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("雙軌表已經畫好圖，推理欄要自己填。"))
    P.append(problem_box([para(
        "1．下面十字形展開圖，六個面分別標住 1～6。摺成正方體之後，邊個面同「1」相對？")]))
    P.append(dt(NET1_H14, "提示：「1」喺邊一條直線（橫排／直排）上？相隔一格嗰個係邊個？"))
    P.append(blank())
    P.append(problem_box([para(
        "2．承上面同一個展開圖。摺成正方體之後，邊個面同「2」相對？")]))
    P.append(dt(NET1_H26, "提示：呢次要睇直排，唔係橫排。"))
    P.append(blank())

    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("雙軌表得返圖，推理欄自己諗，翻查提示卡②幫手。"))
    P.append(problem_box([para(
        "3．承第1、2題個展開圖：頂＝2、前＝3、右＝4、左＝1、後＝5、底＝6。"
        "如果將正方體向左滾一下，新嘅頂面係邊個？")] + write_lines(3)))
    P.append(blank())
    P.append(problem_box([para(
        "4．同上個正方體（未滾動前：頂＝2、前＝3、右＝4、左＝1、後＝5、底＝6）。"
        "如果向前滾一下，新嘅頂面係邊個？")] + write_lines(3)))
    P.append(blank())

    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("完全冇雙軌表，自己一步步查提示卡、寫低推理。第 6 題係開放題。"))
    P.append(problem_box([para(
        "5．同上個正方體（未滾動前：頂＝2、前＝3、右＝4、左＝1、後＝5、底＝6）。"
        "如果先向右滾一下，再向前滾一下（兩次翻滾），最終嘅頂面係邊個？")] + write_lines(6)))
    P.append(blank())
    P.append(problem_box([
        para("6．【開放題】請你自己設計一個十字形展開圖（自訂6個面代號），"
             "寫低邊兩對面相對；再設計一個翻滾情境，寫低你嘅答案，然後同同學交換核對。")
    ] + write_lines(6)))

    P.append(selfcheck_list(SELFCHECK))

    P.append(heading("參考答案與詳解（教師用）", page_break_before=True))
    for i, key in enumerate(("A1", "A2", "B1", "B2", "C1", "C2"), 1):
        a = ANS[key]
        P.append(para(f"{i}．答案：{a['ans']}", bold=True))
        P.append(para(f"【規律】{a['rule']}"))
        P.append(para("【詳細步驟】"))
        for j, s in enumerate(a["steps"], 1):
            P.append(para(f"　（{j}）{s}"))
        P.append(shaded_box(f"【易錯點提示】{a['pit']}"))
        P.append(blank())

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=media)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _svg_inline(png_path):
    svg = open(png_path.replace(".png", ".svg"), encoding="utf-8").read()
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def _tex(m):
    import re
    m = m.strip()
    p = re.fullmatch(r"(\d+)-(\d+)=(\d+)", m)
    if p:
        return r"\(%s-%s=%s\)" % p.groups()
    return r"\(%s\)" % m


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    def dt_html(svg, text, lines=2):
        return (f'<table class="d-tbl dual-track"><tr><th>圖形上發生什麼</th>'
                f'<th>推理／作答</th></tr>'
                f'<tr><td class="fig">{svg}</td><td>{_esc(text)}</td></tr>'
                f'<tr><td></td><td>{_lines(lines)}</td></tr></table>')

    secA = (f'<div class="problem"><div>1．下面十字形展開圖，六個面分別標住 1～6。'
            f'摺成正方體之後，邊個面同「1」相對？</div>'
            f'{dt_html(_svg_inline(NET1_H14), "提示：「1」喺邊一條直線（橫排／直排）上？相隔一格嗰個係邊個？")}'
            f'</div>'
            f'<div class="problem"><div>2．承上面同一個展開圖。摺成正方體之後，'
            f'邊個面同「2」相對？</div>'
            f'{dt_html(_svg_inline(NET1_H26), "提示：呢次要睇直排，唔係橫排。")}</div>')

    secB = (f'<div class="problem"><div>3．承第1、2題個展開圖：頂＝2、前＝3、右＝4、'
            f'左＝1、後＝5、底＝6。如果將正方體向左滾一下，新嘅頂面係邊個？</div>{_lines(3)}</div>'
            f'<div class="problem"><div>4．同上個正方體（未滾動前：頂＝2、前＝3、右＝4、'
            f'左＝1、後＝5、底＝6）。如果向前滾一下，新嘅頂面係邊個？</div>{_lines(3)}</div>')

    secC = (f'<div class="problem"><div>5．同上個正方體（未滾動前：頂＝2、前＝3、右＝4、'
            f'左＝1、後＝5、底＝6）。如果先向右滾一下，再向前滾一下（兩次翻滾），'
            f'最終嘅頂面係邊個？</div>{_lines(6)}</div>'
            f'<div class="problem"><div>6．【開放題】請你自己設計一個十字形展開圖'
            f'（自訂6個面代號），寫低邊兩對面相對；再設計一個翻滾情境，'
            f'寫低你嘅答案，然後同同學交換核對。</div>{_lines(6)}</div>')

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for i, key in enumerate(("A1", "A2", "B1", "B2", "C1", "C2"), 1):
        a = ANS[key]
        steps = "".join(f"<div>　（{j}）{_h(s)}</div>" for j, s in enumerate(a["steps"], 1))
        ansec += (f'<div class="problem"><div style="font-weight:700">{i}．答案：{_esc(a["ans"])}</div>'
                  f'<div>【規律】{_h(a["rule"])}</div>'
                  f'<div>【詳細步驟】</div>{steps}'
                  f'<div class="hint-card">【易錯點提示】{_esc(a["pit"])}</div></div>')

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>雙軌表已經畫好圖，推理欄要自己填。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>雙軌表得返圖，推理欄自己諗，翻查提示卡②幫手。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>完全冇雙軌表，自己一步步查提示卡、寫低推理。第 6 題係開放題。</div>
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
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(head + body)
    return path


if __name__ == "__main__":
    print(build_practice_docx())
    print(build_practice_html())
