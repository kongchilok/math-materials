# -*- coding: utf-8 -*-
"""
第7章 語文與邏輯推理(二)．L20 類比與詞語關係 —— 課堂練習 ＋ 工具卡 build script
主設計 D8 關鍵字對譯；輔助 D12 自我核對。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：練習A/B 題目旁印精簡關係類型表 → 練習C 唔提供，自己回想。
題目來源：全部改編自題庫真實題目（MOCK3-002/004/005/037、VERBAL1-030、MOCK3-014），
逐題親自驗算，見 驗算_類比與詞語關係.md。
產出：練習_類比與詞語關係_抽離小班共用版.docx/.html/.pdf、工具卡.docx/.pdf
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_類比與詞語關係_抽離小班共用版"
CARD = "工具卡_類比與詞語關係"
UNIT = "第7章 語文與邏輯推理(二)．L20 類比與詞語關係"
FOOT = "高三數學．第7章 語文與邏輯推理(二)．L20 類比與詞語關係"

HINT_TOP = "動手之前：先講得出已知嗰對詞係咩關係類型，先至揀選項。"
SELFCHECK = ["我講得出已知嗰對詞係咩關係類型。", "我逐個選項核對係咪同一種關係。",
            "如果有兩個選項都似，我有再諗清楚邊個先係結構完全一致。",
            "答案代返去題目讀一次，通唔通順。"]

COMPACT_KW = [("反義／近義", "意思相反／相似"), ("類別：實例", "大類 vs 個別例子"),
             ("工具：目的", "用嚟做啲咩"), ("新舊替代", "後者升級取代前者"),
             ("窮盡互斥", "同一類別下僅有嘅兩個值")]

STEMS = {
    "A1": "若航海對羅盤，則生命對？\nA．靈魂　B．夢想　C．經驗　D．活力",
    "A2": "金屬：鐵　與　？：單車\nA．交通工具　B．車輪　C．摩托車　D．以上皆不是",
    "B1": "羽毛：鋼筆　與　火炬：？\nA．燃燒　B．書寫　C．燈籠　D．火焰",
    "B2": "峰迴路轉　山窮水盡；以下邊一句與上述意思相同？\n"
          "A．安居樂業　四海為家\nB．比比皆是　一成不變\nC．沉默寡言　豪言壯語\n"
          "D．囫圇吞棗　融匯貫通",
    "C1": "男：女：性別，同下面邊項係同等關係？\n"
          "A．北磁極，南磁極，磁極　B．北，南，方向　C．黑，白，顏色　D．以上不是",
    "C2": "錯誤：『？』／『？』：建設（分別為「錯誤」同「建設」各配一個相關詞）\n"
          "A．正確／建造　B．過失／設置　C．紕漏（只得一個詞）　D．謬誤／毀壞",
}

ANS = dict(
    A1=dict(ans="B．夢想", rel="工具／方向指引：目的", why="航海需要羅盤指引方向；生命同樣"
                                                       "需要一個方向指引——「夢想」正正扮演呢個角色。",
            elim="A靈魂、C經驗、D活力都唔係「方向指引」嘅角色，同羅盤嘅功能唔對應。"),
    A2=dict(ans="A．交通工具", rel="類別：實例", why="「金屬：鐵」係「大類：個別例子」關係"
                                               "（鐵是一種金屬）；同理，「單車」所屬嘅大類係"
                                               "「交通工具」。",
            elim="B車輪、C摩托車都唔係「單車」所屬嘅大類（車輪係部件，摩托車係另一種"
                "交通工具，唔係單車嘅類別）。"),
    B1=dict(ans="C．燈籠", rel="新舊替代（技術升級）", why="羽毛筆（舊式書寫工具）被鋼筆"
                                                       "（升級版書寫工具）取代；同理，火炬"
                                                       "（原始照明工具）被燈籠（更方便安全嘅"
                                                       "照明工具）取代。",
            elim="A燃燒、D火焰係火炬產生嘅現象，B書寫係動作，都唔係「另一件工具」。"),
    B2=dict(ans="D．囫圇吞棗　融匯貫通", rel="反義對照（成語配對）",
            why="「峰迴路轉」（漸見轉機）對「山窮水盡」（陷入絕境），係「困頓↔清晰」"
                "嘅反義對照。「囫圇吞棗」（食而不化）對「融匯貫通」（透徹理解），"
                "同樣係「不解↔透徹」嘅反義對照，結構一致。",
            elim="A著重居住穩定與否、C著重言語風格，都唔係「困惑—清晰」呢組對照；"
                "B兩詞無明顯反義關係。"),
    C1=dict(ans="A．北磁極，南磁極，磁極", rel="窮盡互斥（類別僅有兩個值）",
            why="「男、女」係「性別」呢個類別下僅有嘅 {2} 個值。「北磁極、南磁極」同樣係"
                "「磁極」呢個類別僅有嘅 {2} 個值（磁鐵只有兩極）。",
            elim="「方向」唔止得南北（仲有東西），「顏色」唔止得黑白（仲有好多種），"
                "呢兩個類別唔係「僅有兩個值」，同「性別」呢種窮盡互斥性質唔同。"),
    C2=dict(ans="A．正確／建造", rel="關係類型要一致（反義配反義，或近義配近義）",
            why="「正確」係「錯誤」嘅反義詞，「建造」係「建設」嘅近義詞——雖然兩個配對"
                "類型唔同（一反義一近義），但每一組本身都準確、清晰。",
            elim="D「謬誤（錯誤嘅近義）／毀壞（建設嘅反義）」——兩個配對嘅關係類型"
                "（近義vs反義）自相矛盾唔工整；B「過失」同「錯誤」意思有落差、"
                "「設置」同「建設」意思唔夠貼近，冇A咁準確。"),
)


def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("每題旁邊都印住精簡關係類型表。"))
    for n, key in ((1, "A1"), (2, "A2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")]))
        P.append(keyword_table(COMPACT_KW))
        P.append(para("作答：")); P += write_lines(2)
        P.append(blank())

    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("關係類型表唔再逐題附，唔記得就自己諗返。"))
    for n, key in ((3, "B1"), (4, "B2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")] + write_lines(3)))
        P.append(blank())

    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("完全冇關係類型表提示，自己判斷。"))
    for n, key in ((5, "C1"), (6, "C2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")] + write_lines(4)))
        P.append(blank())

    P.append(selfcheck_list(SELFCHECK))

    P.append(heading("參考答案與詳解（教師用）", page_break_before=True))
    for i, key in enumerate(("A1", "A2", "B1", "B2", "C1", "C2"), 1):
        a = ANS[key]
        P.append(para(f"{i}．答案：{a['ans']}", bold=True))
        P.append(para(f"【關係類型】{a['rel']}"))
        P.append(para(f"【解釋】{a['why']}"))
        P.append(shaded_box(f"【剔除其餘選項】{a['elim']}"))
        P.append(blank())

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    card1 = [para("▍常見詞語關係類型", bold=True, sz=HEADING_SZ)]
    card1 += [para(f"・{k}：{v}", sz=21) for k, v in COMPACT_KW]

    card2 = [para("⚠ 陷阱提醒卡", bold=True, sz=HEADING_SZ),
             para("・表面相似（都係地點／都係物件）唔代表結構相同", sz=21),
             para("・部件關係（劍：劍鋒）同類別關係（金屬：鐵）唔同型", sz=21),
             para("・「窮盡互斥」要係類別僅有 {2} 個值先算（性別得男女；顏色唔止黑白）", sz=21)]

    card3 = [para("▍做法卡", bold=True, sz=HEADING_SZ),
             para("什麼時候翻我：見到「A：B　與　C：？」呢類類比題", sz=21),
             para("1. 先講出已知嗰對（A：B）係邊種關係", sz=21),
             para("2. 逐個選項檢查係咪同一種關係", sz=21),
             para("3. 表面似唔算，要結構一致先算", sz=21),
             para("4. 揀完代返去讀一次，通順先確定", sz=21)]

    card4 = [para("▍自我核對", bold=True, sz=HEADING_SZ)]
    card4 += [para(f"☐ {t}", sz=21) for t in SELFCHECK]

    P.append(toolcard_sheet([card1, card2, card3, card4], cols=2, card_h=4200))
    return build_docx(P, os.path.join(HERE, CARD + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def _stem_html(s):
    return _esc(s).replace("\n", "<br>")


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(r"\(%s\)" % m.group(1).strip())
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def _kw_html(rows):
    return "".join(f"<tr><td>{_esc(k)}</td><td>{_esc(v)}</td></tr>" for k, v in rows)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    kw_table = (f'<table class="d-tbl kw-table"><tr><th>關係類型</th><th>說明</th></tr>'
                f'{_kw_html(COMPACT_KW)}</table>')

    secA = ""
    for n, key in ((1, "A1"), (2, "A2")):
        secA += (f'<div class="problem"><div>{n}．{_stem_html(STEMS[key])}</div>'
                 f'{kw_table}<div>作答：</div>{_lines(2)}</div>')

    secB = ""
    for n, key in ((3, "B1"), (4, "B2")):
        secB += f'<div class="problem"><div>{n}．{_stem_html(STEMS[key])}</div>{_lines(3)}</div>'

    secC = ""
    for n, key in ((5, "C1"), (6, "C2")):
        secC += f'<div class="problem"><div>{n}．{_stem_html(STEMS[key])}</div>{_lines(4)}</div>'

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for i, key in enumerate(("A1", "A2", "B1", "B2", "C1", "C2"), 1):
        a = ANS[key]
        ansec += (f'<div class="problem"><div style="font-weight:700">{i}．答案：{_esc(a["ans"])}</div>'
                  f'<div>【關係類型】{_esc(a["rel"])}</div>'
                  f'<div>【解釋】{_h(a["why"])}</div>'
                  f'<div class="hint-card">【剔除其餘選項】{_esc(a["elim"])}</div></div>')

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>每題旁邊都印住精簡關係類型表。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>關係類型表唔再逐題附，唔記得就自己諗返。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>完全冇關係類型表提示，自己判斷。</div>
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
    print(build_toolcard_docx())
    print(build_practice_html())
