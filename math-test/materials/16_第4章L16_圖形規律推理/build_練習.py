# -*- coding: utf-8 -*-
"""
第4章 數理邏輯(二)．L16 圖形規律推理 —— 課堂練習 build script
主設計 D5 圖文雙軌對照；輔助 D11 標記對應法。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：練習A 雙軌表已示範一半（規律填空提示）→ 練習B 雙軌表得返標題列（兩欄全空）→
         練習C 完全唔提供雙軌表。
全部題目為自編（題庫 B2 圖形規律推理原稿缺圖，詳見 驗算_圖形規律推理.md §0）。
產出：練習_圖形規律推理_抽離小班共用版.docx/.html/.pdf（本課設計無需獨立工具卡）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import figs as f                             # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_圖形規律推理_抽離小班共用版"
UNIT = "第4章 數理邏輯(二)．L16 圖形規律推理"
FOOT = "高三數學．第4章 數理邏輯(二)．L16 圖形規律推理"

HINT_TOP = "動手之前：一格一格編號，每次淨係比較相鄰兩格，寫低邊度變咗。"
SELFCHECK = ["我逐格編咗號（①②③④）。", "我每次淨係比較相鄰兩格，冇一次過睇成串圖案。",
             "如果有兩種變化（例如邊數＋填色），我兩種都分開講。",
             "答案畫返出嚟或者講得出係咩形狀／方向。"]

C = f.BOX / 2  # 每格中心座標（正方形，中心=一半）


# ================================================================ 圖形
def _mk(name, svg):
    return f.save(name, svg, HERE)


# A1：圓點數量遞增
A1_QIMG = _mk("a1_q", f.panel_row([
    (f.dot_row(C, C, 1), "①", False), (f.dot_row(C, C, 2), "②", False),
    (f.dot_row(C, C, 3), "③", False), (None, "④", True)]))
A1_GIVEN = _mk("a1_given", f.panel_row([
    (f.dot_row(C, C, 1), "①", False), (f.dot_row(C, C, 2), "②", False),
    (f.dot_row(C, C, 3), "③", False)]))
A1_Q = _mk("a1_q2", f.panel_row([(None, "④", True)]))
A1_ANS = _mk("a1_ans", f.panel_row([(f.dot_row(C, C, 4), "④", False)]))

# A2：箭嘴方向順時針轉 90°
A2_QIMG = _mk("a2_q", f.panel_row([
    (f.arrow(C, C, 34, 0), "①", False), (f.arrow(C, C, 34, 90), "②", False),
    (f.arrow(C, C, 34, 180), "③", False), (None, "④", True)]))
A2_GIVEN = _mk("a2_given", f.panel_row([
    (f.arrow(C, C, 34, 0), "①", False), (f.arrow(C, C, 34, 90), "②", False),
    (f.arrow(C, C, 34, 180), "③", False)]))
A2_Q = _mk("a2_q2", f.panel_row([(None, "④", True)]))
A2_ANS = _mk("a2_ans", f.panel_row([(f.arrow(C, C, 34, 270), "④", False)]))

# B1：邊數遞增 + 填色交替
B1_QIMG = _mk("b1_q", f.panel_row([
    (f.polygon(C, C, 40, 3, solid=False), "①", False),
    (f.polygon(C, C, 40, 4, solid=True), "②", False),
    (f.polygon(C, C, 40, 5, solid=False), "③", False),
    (None, "④", True)]))
B1_ANS = _mk("b1_ans", f.panel_row([(f.polygon(C, C, 40, 6, solid=True), "④", False)]))

# B2：兩排格仔（上排全給，下排缺一格）
B2_QIMG = _mk("b2_q", f.two_row_grid(
    [(f.dot_row(C, C, 1), False), (f.dot_row(C, C, 2), False), (f.dot_row(C, C, 3), False)],
    [(f.dot_row(C, C, 2), False), (f.dot_row(C, C, 4), False), (None, True)],
    row_label_top="上排", row_label_bottom="下排", label_w=90))
B2_ANS = _mk("b2_ans", f.two_row_grid(
    [(f.dot_row(C, C, 1), False), (f.dot_row(C, C, 2), False), (f.dot_row(C, C, 3), False)],
    [(f.dot_row(C, C, 2), False), (f.dot_row(C, C, 4), False), (f.dot_row(C, C, 6), False)],
    row_label_top="上排", row_label_bottom="下排", label_w=90))

# C1：箭嘴數量 + 方向同時變化
C1_QIMG = _mk("c1_q", f.panel_row([
    (f.arrow_row(C, C, 1, 0), "①", False), (f.arrow_row(C, C, 2, 90), "②", False),
    (f.arrow_row(C, C, 3, 180), "③", False), (None, "④", True)]))
C1_ANS = _mk("c1_ans", f.panel_row([(f.arrow_row(C, C, 4, 270), "④", False)]))

media = MediaRegistry()


def dt(given_img, q_img, given_text, blank_lines=2):
    """雙軌表2列：第1列（已知規律描述）、第2列（學生填空作答）。
    given_text 傳原始字串（含 {} 標記亦可）——dual_track_table 內部會自動 para() 包裝，
    唔可以喺呢度先手動 para() 一次，否則會被當成純文字再包一次、令 XML 標籤被轉義。"""
    rows = [
        (image_para(given_img, width_cm=10.0), given_text),
        (image_para(q_img, width_cm=4.0), write_lines(blank_lines)),
    ]
    return dual_track_table(rows, media=media, headers=("圖形上發生什麼", "文字描述規律／作答"))


ANS = dict(
    A1=dict(ans="4 粒實心圓點", rule="每一格嘅實心圓點數量比上一格多 1 粒。",
            steps=["①1粒→②2粒→③3粒，逐格 +1。", "④ ＝ {3+1=4} 粒。"],
            pit="淨係睇「多咗幾多粒」冇留意係咪固定 +1（唔係 ×2 或者 +2）。"),
    A2=dict(ans="箭嘴指向左邊", rule="每一格嘅箭嘴方向順時針轉 90 度。",
            steps=["①上→②右→③下，每次順時針轉 90 度。", "④ ＝ 下再轉 90° ＝ 左。"],
            pit="轉錯方向（逆時針轉）或者轉錯角度（轉埋 180°）。"),
    B1=dict(ans="實心六邊形（6 條邊）",
            rule="邊數每格 +1（3→4→5→6）；填色空心／實心交替出現。",
            steps=["邊數：3→4→5，跟返 +1 規律，④ ＝ {5+1=6} 條邊（六邊形）。",
                   "填色：①空心→②實心→③空心，交替出現，④應該轉返實心。"],
            pit="淨係跟到邊數規律，漏咗填色都要跟返「交替」嗰條規律。"),
    B2=dict(ans="6 粒圓點", rule="上排每格 +1（獨立於下排）；下排每格 +2。",
            steps=["上排：1→2→3，+1。", "下排：2→4，+2；跟落去 {4+2=6}。"],
            pit="誤將上排嘅「+1」規律搬去下排用；上下兩排係獨立嘅兩條規律，"
                "唔係同一條規律套用兩次。"),
    C1=dict(ans="4 支箭嘴，全部指向左邊",
            rule="箭嘴數量每格 +1（1→2→3→4）；方向每格順時針轉 90°（同 A2 一樣）。",
            steps=["數量：1→2→3，+1，④ ＝ 4 支。",
                   "方向：上→右→下，順時針 90°，④ ＝ 左。"],
            pit="呢題同時有兩條規律（數量、方向），淨係跟到其中一條就落答案。"),
    C2=dict(ans="（開放題，教師逐份核對）",
            rule="出題者要確保規律講法只得一個答案，唔可以模稜兩可。",
            steps=["建議：3～4格，變化 1～2 種（例如形狀邊數、填色、方向、數量）。",
                   "出題者要親自驗算：畀第二個人睇你嘅前面幾格，佢答唔答到出你心目中嘅答案。"],
            pit="規律講得太鬆散，一條數列可以砌出兩種唔同答案都啱。"),
)


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("雙軌表已經示範咗規律描述，你要諗最後一格嘅答案。"))
    P.append(problem_box([para("1．下面四格圖案有規律，格④應該係咩？")]))
    P.append(image_para(A1_QIMG, width_cm=15))
    P.append(dt(A1_GIVEN, A1_Q, "由①到③，實心圓點數量每格 ________（填 +1／+2／×2 其中一個）。"))
    P.append(blank())
    P.append(problem_box([para("2．下面四格圖案有規律，格④應該係咩？")]))
    P.append(image_para(A2_QIMG, width_cm=15))
    P.append(dt(A2_GIVEN, A2_Q, "由①到③，箭嘴方向每格順時針轉 ________ 度。"))
    P.append(blank())

    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("雙軌表得返標題列，兩欄都要自己填。"))
    P.append(problem_box([para("3．下面四格圖案有規律，格④應該係咩？（留意可能唔止一種變化）")]))
    P.append(image_para(B1_QIMG, width_cm=15))
    P.append(dual_track_table([([], write_lines(3))], media=media,
                              headers=("圖形上發生什麼", "文字描述規律／作答")))
    P.append(blank())
    P.append(problem_box([para("4．下面兩排圖案，上排規律已經完整、下排缺一格，求下排「？」。")]))
    P.append(image_para(B2_QIMG, width_cm=15))
    P.append(dual_track_table([([], write_lines(3))], media=media,
                              headers=("圖形上發生什麼", "文字描述規律／作答")))
    P.append(blank())

    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("完全冇雙軌表，規律自己諗、自己寫。第 6 題係開放題。"))
    P.append(problem_box([para("5．下面四格圖案有規律，格④應該係咩？")]))
    P.append(image_para(C1_QIMG, width_cm=15))
    P.append(para("作答：")); P += write_lines(4)
    P.append(blank())
    P.append(problem_box([
        para("6．【開放題】請你自己設計一條同類型嘅圖形規律題（3～4格，可以有 1～2 種變化："
             "邊數／填色／方向／數量），畫出前面幾格，寫低你嘅規律同答案，然後同同學交換做。")
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
    P.append(para("答案示意圖：", bold=True))
    for img, cap in ((A1_ANS, "1．格④＝4粒實心圓點"), (A2_ANS, "2．格④＝箭嘴指向左"),
                     (B1_ANS, "3．格④＝實心六邊形"), (B2_ANS, "4．下排格③＝6粒圓點"),
                     (C1_ANS, "5．格④＝4支箭嘴指向左")):
        P.append(image_para(img, width_cm=4.0, caption=cap))

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=media)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _tex(m):
    import re
    m = m.strip()
    p = re.fullmatch(r"(\d+)\+(\d+)=(\d+)", m)
    if p:
        return r"\(%s+%s=%s\)" % p.groups()
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


def _svg_inline(png_path):
    svg = open(png_path.replace(".png", ".svg"), encoding="utf-8").read()
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    def dt_html(given_svg, q_svg, text, lines=2):
        return (f'<table class="d-tbl dual-track"><tr><th>圖形上發生什麼</th>'
                f'<th>文字描述規律／作答</th></tr>'
                f'<tr><td class="fig">{given_svg}</td><td>{_esc(text)}</td></tr>'
                f'<tr><td class="fig">{q_svg}</td><td>{_lines(lines)}</td></tr></table>')

    def dt_blank(lines=3):
        return (f'<table class="d-tbl dual-track"><tr><th>圖形上發生什麼</th>'
                f'<th>文字描述規律／作答</th></tr>'
                f'<tr><td></td><td>{_lines(lines)}</td></tr></table>')

    secA = (f'<div class="problem"><div>1．下面四格圖案有規律，格④應該係咩？</div>'
            f'<div class="fig">{_svg_inline(A1_QIMG)}</div>'
            f'{dt_html(_svg_inline(A1_GIVEN), _svg_inline(A1_Q), "由①到③，實心圓點數量每格 ________（填 +1／+2／×2 其中一個）。")}'
            f'</div>'
            f'<div class="problem"><div>2．下面四格圖案有規律，格④應該係咩？</div>'
            f'<div class="fig">{_svg_inline(A2_QIMG)}</div>'
            f'{dt_html(_svg_inline(A2_GIVEN), _svg_inline(A2_Q), "由①到③，箭嘴方向每格順時針轉 ________ 度。")}'
            f'</div>')

    secB = (f'<div class="problem"><div>3．下面四格圖案有規律，格④應該係咩？'
            f'（留意可能唔止一種變化）</div>'
            f'<div class="fig">{_svg_inline(B1_QIMG)}</div>{dt_blank(3)}</div>'
            f'<div class="problem"><div>4．下面兩排圖案，上排規律已經完整、下排缺一格，'
            f'求下排「？」。</div>'
            f'<div class="fig">{_svg_inline(B2_QIMG)}</div>{dt_blank(3)}</div>')

    secC = (f'<div class="problem"><div>5．下面四格圖案有規律，格④應該係咩？</div>'
            f'<div class="fig">{_svg_inline(C1_QIMG)}</div><div>作答：</div>{_lines(4)}</div>'
            f'<div class="problem"><div>6．【開放題】請你自己設計一條同類型嘅圖形規律題'
            f'（3～4格，可以有 1～2 種變化：邊數／填色／方向／數量），畫出前面幾格，'
            f'寫低你嘅規律同答案，然後同同學交換做。</div>{_lines(6)}</div>')

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for i, key in enumerate(("A1", "A2", "B1", "B2", "C1", "C2"), 1):
        a = ANS[key]
        steps = "".join(f"<div>　（{j}）{_h(s)}</div>" for j, s in enumerate(a["steps"], 1))
        ansec += (f'<div class="problem"><div style="font-weight:700">{i}．答案：{_esc(a["ans"])}</div>'
                  f'<div>【規律】{_esc(a["rule"])}</div>'
                  f'<div>【詳細步驟】</div>{steps}'
                  f'<div class="hint-card">【易錯點提示】{_esc(a["pit"])}</div></div>')
    ans_figs = "".join(
        f'<div class="fig">{_svg_inline(img)}<div class="cap">{_esc(cap)}</div></div>'
        for img, cap in ((A1_ANS, "1．格④＝4粒實心圓點"), (A2_ANS, "2．格④＝箭嘴指向左"),
                        (B1_ANS, "3．格④＝實心六邊形"), (B2_ANS, "4．下排格③＝6粒圓點"),
                        (C1_ANS, "5．格④＝4支箭嘴指向左")))

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>雙軌表已經示範咗規律描述，你要諗最後一格嘅答案。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>雙軌表得返標題列，兩欄都要自己填。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>完全冇雙軌表，規律自己諗、自己寫。第 6 題係開放題。</div>
  {secC}

  {chk}

  <div class="section-h page-break">參考答案與詳解（教師用）</div>
  {ansec}
  <div style="font-weight:700">答案示意圖：</div>
  {ans_figs}

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
