# -*- coding: utf-8 -*-
"""
第6章 語文與邏輯推理(一)．L18 命題排列邏輯 —— 課堂練習 build script
主設計 D9 草稿分區卡；輔助 D12 自我核對。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：練習A/B 印有工作區格仔跟住填 → 練習C 唔提供工作區格仔，自己畫。
題目來源：A1(改編自 MOCK1-028)、B1(改編自 LOGIC1-048)、C1+C2(改編自 LOGIC1-023+024)
為題庫真實題目；A2、B2 為結構相同之自編題。逐題親自驗算，見 驗算_命題排列邏輯.md。
產出：練習_命題排列邏輯_抽離小班共用版.docx/.html/.pdf（本課設計無需獨立工具卡）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_命題排列邏輯_抽離小班共用版"
UNIT = "第6章 語文與邏輯推理(一)．L18 命題排列邏輯"
FOOT = "高三數學．第6章 語文與邏輯推理(一)．L18 命題排列邏輯"

HINT_TOP = "動手之前：讀一個條件，即刻喺工作區填一格，唔好留喺腦入面。"
SELFCHECK = ["每一個條件我都有喺工作區度記低。", "答案代返去逐條件檢查，全部仍然成立。",
            "如果排位圖有缺格，我有再讀一次題目睇漏咗邊個條件。"]

WS_A1 = ("甲嘅左鄰", "甲嘅右鄰", "甲嘅對角", "檢查：三個位置填晒未？")
WS_A2 = ("第1(最快)", "第2", "第3", "第4(包尾)")
WS_B1 = ("最細(排第1)", "第2", "第3", "第4", "第5", "最大(排第6)")
WS_B2 = ("第1(最快)", "第2", "第3", "第4", "第5(最慢)", "檢查：3個條件用晒未？")
WS_C = ("屋1(紅，日本)", "屋2(綠)", "屋3(藍)", "屋4(黃，美國)", "屋5(白)", "屋6(橙，中國)")

STEMS = {
    "A1": "甲、乙、丙、丁四人手拉手圍成一圈。已知甲不在乙的旁邊。下列邊個陳述一定正確？\n"
          "A．乙在丁的旁邊　B．丙在丁的旁邊　C．以上皆是　D．無法判斷",
    "A2": "甲、乙、丙、丁四人賽跑，名次無並列。已知：①乙快過丙。②甲快過乙。③丙快過丁。"
          "邊個包尾（排第4）？",
    "B1": "某公司調查發現：①經理的年紀比科長大。②襄理的年紀比課長小。③廠長的年紀小於經理，"
          "但比課長大。④主任的年紀比科長小，但比廠長大。若董事長年紀比主任大，"
          "這6人中，比董事長年紀小的有幾人？",
    "B2": "甲、乙、丙、丁、戊五人賽跑，名次無並列。已知：①丙快過丁。②戊比甲快，但比丙慢。"
          "③乙比丁快，但比戊慢。求前三名（由快至慢）？",
    "C1": "有紅、綠、藍、黃、白及橙等六種顏色的小木屋依次由左至右排成一列，分別住著中國人、"
          "日本人、美國人、法國人、德國人及義大利人。已知：①日本人住在第一間紅色小木屋。"
          "②美國人住在義大利人右邊。③法國人住在日本人與義大利人中間。④美國人住在第四間"
          "黃色小木屋。⑤中國人住在第六間橙色小木屋。德國人住在什麼顏色的小木屋？",
    "C2": "承上題，以下住屋順序（由左至右）何者正確？\n"
          "A．日本、德國、法國、義大利、美國、中國\n"
          "B．日本、法國、美國、德國、義大利、中國\n"
          "C．日本、法國、義大利、美國、德國、中國\n"
          "D．以上皆非",
}

ANS = dict(
    A1=dict(ans="A．乙在丁的旁邊", rule="圍圈4人，每人有2個鄰居、1個對角。「甲唔喺乙隔籬」"
                                      "即乙係甲嘅對角。",
            steps=["甲嘅對角=乙，故甲嘅兩個鄰居必為丙、丁。",
                   "排列：甲－丙－乙－丁－甲（或鏡像：甲－丁－乙－丙－甲）。",
                   "呢個排列入面，乙嘅鄰居係丙同丁——「乙喺丁隔籬」恆成立。",
                   "丙嘅鄰居係甲同乙，唔包括丁——「丙喺丁隔籬」唔一定成立。"],
            pit="以為「甲唔喺乙隔籬」等於「乙丙唔喺埋一齊」，冇搞清楚4人圍圈"
                "入面「對角」同「鄰居」嘅關係。"),
    A2=dict(ans="丁", rule="三個條件連成一條鏈：甲>乙>丙>丁。",
            steps=["②甲>乙。①乙>丙。③丙>丁。", "接連：甲>乙>丙>丁——4人之間有 {4-1=3} 個"
                   "「>」關係，同3個條件數目脗合，冇缺、冇多。", "包尾（排第4）嘅係丁。"],
            pit="條件次序打亂咗（①②③喺題目入面唔係跟排名次序寫），照抄題目次序填工作區"
                "會兜錯圈，要留意邊個條件先接得落邊個。"),
    B1=dict(ans="D．4人", rule="4個條件連成鏈：襄理<課長<廠長<主任<科長<經理。",
            steps=["②襄理<課長。③課長<廠長，廠長<經理。④廠長<主任，主任<科長。",
                   "接連：襄理<課長<廠長<主任<科長，且科長<經理（由①）。",
                   "已知董事長>主任，故襄理、課長、廠長、主任四人都<主任<董事長，"
                   "四人確定<董事長。",
                   "科長、經理與董事長嘅大小關係題目冇講，唔可以假設，故唔計入。"],
            pit="誤將科長、經理都當成細過董事長（冇睇清楚題目淨係話「董事長>主任」，"
                "冇話董事長點同科長／經理比較）。"),
    B2=dict(ans="丙、戊、甲", rule="三個條件連成一條鏈：丙>戊>甲>乙>丁。",
            steps=["②戊比甲快，比丙慢：丙>戊>甲。", "③乙比丁快，比戊慢：戊>乙>丁。",
                   "①丙快過丁：用嚟核對——由鏈 丙>戊>甲>乙>丁，"
                   "傳遞性推出丙>丁，同條件①相符，無矛盾。",
                   "完整鏈：丙>戊>甲>乙>丁。前三名：丙、戊、甲。"],
            pit="淨係用返②③兩條建鏈，冇用條件①做覆核，漏咗核對步驟。"),
    C1=dict(ans="C．白色", rule="逐一定位六間屋，剩低嘅位置用排除法。",
            steps=["位置1=日本(紅)（①）；位置4=美國(黃)（④）；位置6=中國(橙)（⑤）。",
                   "③法國夾喺日本(1)與義大利之間，義大利必須<4（由②美國喺義大利右邊，"
                   "美國=4）。若義大利=2，法國冇位可放（要夾喺1同2之間）；故義大利=3，法國=2。",
                   "剩返位置5，只可以係德國。",
                   "六色順序（紅綠藍黃白橙）對應位置1-6，位置5=白，故德國住白色。"],
            pit="漏咗「義大利必須細過4」呢個由條件②推出嚟嘅隱含限制，"
                "誤將義大利放喺位置2，令法國冇位置擺得落。"),
    C2=dict(ans="C．日本、法國、義大利、美國、德國、中國",
            rule="承C1嘅推導，六個位置全部定位。",
            steps=["位置1=日本、位置2=法國、位置3=義大利、位置4=美國、位置5=德國、"
                   "位置6=中國。", "對應選項C。"],
            pit="只計到德國個別位置就以為完成，冇將六個位置全部串連做返完整答案，"
                "揀答案時漏睇某一個位置。"),
)


def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("工作區已經印好，讀一個條件填一格。"))
    P.append(problem_box([para(f"1．{STEMS['A1']}")]))
    P.append(quadrant_workspace(WS_A1, cell_h=1400))
    P.append(para("作答：")); P += write_lines(2)
    P.append(blank())
    P.append(problem_box([para(f"2．{STEMS['A2']}")]))
    P.append(quadrant_workspace(WS_A2, cell_h=1400))
    P.append(para("作答：")); P += write_lines(2)
    P.append(blank())

    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("工作區格數配合人數，自己判斷點填。"))
    P.append(problem_box([para(f"3．{STEMS['B1']}")]))
    P.append(quadrant_workspace(WS_B1, cell_h=1300))
    P.append(para("作答：")); P += write_lines(2)
    P.append(blank())
    P.append(problem_box([para(f"4．{STEMS['B2']}")]))
    P.append(quadrant_workspace(WS_B2, cell_h=1300))
    P.append(para("作答：")); P += write_lines(2)
    P.append(blank())

    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("完全冇工作區格仔，自己喺下面空白處畫。第5、6題共用同一個情境。"))
    P.append(problem_box([para(f"5．{STEMS['C1']}")] + write_lines(6)))
    P.append(blank())
    P.append(problem_box([para(f"6．{STEMS['C2']}")] + write_lines(4)))

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

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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


def _quadrant_html(labels, cell_h="3.4cm"):
    rows = ""
    for i in range(0, len(labels), 2):
        pair = labels[i:i + 2]
        cells = "".join(f'<td style="height:{cell_h}"><div class="qlabel">{_esc(l)}</div></td>'
                        for l in pair)
        rows += f"<tr>{cells}</tr>"
    return f'<table class="d-tbl quadrant">{rows}</table>'


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    def _stem_html(s):
        return _esc(s).replace("\n", "<br>")

    secA = (f'<div class="problem"><div>1．{_stem_html(STEMS["A1"])}</div>'
            f'{_quadrant_html(WS_A1)}<div>作答：</div>{_lines(2)}</div>'
            f'<div class="problem"><div>2．{_stem_html(STEMS["A2"])}</div>'
            f'{_quadrant_html(WS_A2)}<div>作答：</div>{_lines(2)}</div>')

    secB = (f'<div class="problem"><div>3．{_stem_html(STEMS["B1"])}</div>'
            f'{_quadrant_html(WS_B1)}<div>作答：</div>{_lines(2)}</div>'
            f'<div class="problem"><div>4．{_stem_html(STEMS["B2"])}</div>'
            f'{_quadrant_html(WS_B2)}<div>作答：</div>{_lines(2)}</div>')

    secC = (f'<div class="problem"><div>5．{_stem_html(STEMS["C1"])}</div>{_lines(6)}</div>'
            f'<div class="problem"><div>6．{_stem_html(STEMS["C2"])}</div>{_lines(4)}</div>')

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

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>工作區已經印好，讀一個條件填一格。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>工作區格數配合人數，自己判斷點填。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>完全冇工作區格仔，自己喺下面空白處畫。第5、6題共用同一個情境。</div>
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
