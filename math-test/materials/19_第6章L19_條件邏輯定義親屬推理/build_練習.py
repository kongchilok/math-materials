# -*- coding: utf-8 -*-
"""
第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係 —— 課堂練習 ＋ 工具卡 build script
主設計 D8 關鍵字對譯；輔助 D11 標記對應。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：練習A/B 題目旁印精簡對譯表 → 練習C 唔提供，自己回想規則。
題目來源：A1(改編LOGIC1-064)、A2(改編MOCK1-058)、B1(改編VERBAL1-025)、
B2(改編VERBAL1-031)、C1(改編MOCK3-008)、C2(改編MOCK1-015)，逐題親自驗算，
見 驗算_條件邏輯定義親屬推理.md。
產出：練習_條件邏輯定義親屬推理_抽離小班共用版.docx/.html/.pdf、工具卡.docx/.pdf
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_條件邏輯定義親屬推理_抽離小班共用版"
CARD = "工具卡_條件邏輯定義親屬推理"
UNIT = "第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係"
FOOT = "高三數學．第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係"

HINT_TOP = "動手之前：先判斷句式（若則／只有才／除非否則／定義要件／親屬稱謂），再翻做符號。"
SELFCHECK = ["條件句我有翻譯做符號，冇淨係讀字面。", "定義題我逐項要件核對，冇漏一項。",
            "親屬關係我由外層一步步代入，冇一步跳幾層。", "答案代返去題目檢查過一次。"]

COMPACT_KW = [("若P則Q／只要P就Q", "P→Q"), ("只有P才Q", "Q→P（調轉）"),
             ("除非P否則Q", "¬P→Q（接否定）"), ("逆否命題", "¬Q→¬P（同原命題等價）")]

STEMS = {
    "A1": "考慮三句話：①公園裡所有的樹都是會開花的樹。②公園裡某些樹是山茱萸。"
          "③公園裡所有山茱萸都是會開花的樹。如果①②為真，③是？\nA．真的　B．假的　C．無法判斷",
    "A2": "一名女士指著甲說：「她的母親是我的母親的獨生女。」請問呢名女士係甲嘅乜關係？\n"
          "A．母親　B．妹妹　C．女兒　D．姨媽",
    "B1": "天文學家說：「如果太陽毀滅，則銀河系中有外星人。」以下邊項同呢句意思相同？\n"
          "A．如果銀河系中有外星人，則太陽毀滅。\nB．如果銀河系中有外星人，則太陽不會毀滅。\n"
          "C．太陽不會毀滅，或者銀河系有外星人。",
    "B2": "「政策性虧損」定義：企業喺實現政府規定嘅社會公益目標、生產經營某商品嘅過程中，"
          "因國家限價等原因產生虧損，並由財政部門審核後給予合理補償。下列邊項屬於"
          "政策性虧損？\nA．政府直接補貼農民種糧成本（對象係個人，非企業）\n"
          "B．某糧食企業經營政府規定嘅平價糧食，因保護價高、售價低而虧損，"
          "財政部門定額補貼",
    "C1": "已知：①只有律師才可以申請甲信用卡。②凡是律師都可以出入法院。"
          "③有妨礙司法嘅唔可以成為律師。以下邊個必然成立？\n"
          "A．有甲信用卡的人都是律師　B．能進法院的人都是律師　C．能進法院的人都不是妨礙司法的",
    "C2": "甲、乙、丙、丁、戊五人：乙是甲的老公，丙與乙是兄弟，丁是丙的太太，"
          "丁是甲的妹妹，戊是丁的爸爸。乙該是戊的乜關係？\n"
          "A．爸爸的哥哥　B．女兒的丈夫　C．媽媽的妹妹　D．沒有足夠資料",
}

ANS = dict(
    A1=dict(ans="A．真的", rule="三段論：山茱萸⊆樹（②），樹→會開花（①），故山茱萸→會開花。",
            steps=["②話「山茱萸係樹」，即山茱萸屬於「樹」呢個類別。",
                   "①話「所有樹都會開花」，即 樹→會開花。",
                   "串連：山茱萸→樹→會開花，故「所有山茱萸都會開花」為真。"],
            pit="以為「某些」同「所有」係同一件事，其實②只係話部分樹係山茱萸，"
                "但呢個唔影響「所有山茱萸都符合①嘅條件」呢個結論。"),
    A2=dict(ans="A．母親", rule="「我的母親的獨生女」＝我本人（因為我正正係我母親唯一嘅女兒）。",
            steps=["設呢名女士＝W。「W的母親的獨生女」，即W母親唯一嘅女兒。",
                   "W自己就係W母親嘅女兒，而且係「獨生女」（唯一一個），所以呢個人就係W本人。",
                   "題目話「甲的母親」就係呢個人，即甲的母親＝W。",
                   "所以W係甲嘅母親。"],
            pit="讀到「獨生女」諗埋去第三代，其實呢度淨係兩代（W同W嘅媽媽），"
                "「獨生女」形容緊W自己。"),
    B1=dict(ans="C", rule="{P->Q} 恆等價於「¬P 或 Q」（笛摩根律相關恆等式）。",
            steps=["設P＝太陽毀滅，Q＝有外星人。原句：{P->Q}。",
                   "恆等式：{P->Q} ≡ ¬P 或 Q，即「太陽不會毀滅，或者銀河系有外星人」。",
                   "對應選項C。A係逆命題（Q→P）、B方向錯誤，兩者都同原句唔等價。"],
            pit="將「若P則Q」誤當成「若Q則P」（逆命題），兩者邏輯上唔等價。"),
    B2=dict(ans="B", rule="定義四要件：①企業（非個人）②執行政府社會公益目標③因國家限價"
                        "產生虧損④財政部門審核後補償。四項要全部符合先算。",
            steps=["A：補貼對象係「農民個人」，唔係「企業」，不符要件①，剔除。",
                   "B：主體係「糧食企業」✓要件①；經營嘅係「政府規定嘅平價糧食」✓要件②；"
                   "「保護價高、售價低」正正係國家限價造成嘅虧損✓要件③；"
                   "「財政部門定額補貼」✓要件④。四項全部符合。"],
            pit="淨係核對到一兩項要件覺得「幾似」就選咗，冇逐一核對晒四項要件。"),
    C1=dict(ans="A", rule="設K=有甲卡,L=律師,F=可進法院,M=妨礙司法。"
                        "已知：①{K->L}②{L->F}③{M->~L}。",
            steps=["A即「{K->L}」，直接就係條件①本身，必然成立。",
                   "B即「{F->L}」，係條件②嘅逆命題，唔一定成立。",
                   "C即「{F->~M}」，冇條件直接支持，唔一定成立。"],
            pit="將②「律師→可進法院」逆轉做「可進法院→律師」，當成逆命題自動成立"
                "（逆命題唔等價於原命題）。"),
    C2=dict(ans="B．女兒的丈夫", rule="由「丁是甲的妹妹」同「戊是丁的爸爸」，"
                                    "推出戊都係甲嘅爸爸（同一個爸爸）。",
            steps=["丁是甲的妹妹 → 丁同甲係姊妹，共同爸爸＝戊。",
                   "所以戊也是甲的爸爸。",
                   "乙是甲的老公，即係戊個女（甲）嘅丈夫，即「女婿」。",
                   "答案：乙係戊嘅「女兒的丈夫」。"],
            pit="淨係處理到「丙與乙是兄弟」「丁是丙的太太」呢兩層關係，"
                "冇留意「丁是甲的妹妹」先係解題嘅關鍵一步（將戊同甲連埋一齊）。"),
)


def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("每題旁邊都印住精簡對譯表。"))
    for n, key in ((1, "A1"), (2, "A2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")]))
        P.append(keyword_table(COMPACT_KW))
        P.append(para("作答：")); P += write_lines(3)
        P.append(blank())

    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("對譯表唔再逐題附，唔記得就自己諗返規則。"))
    for n, key in ((3, "B1"), (4, "B2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")] + write_lines(4)))
        P.append(blank())

    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("完全冇對譯表提示，自己判斷句式類型。"))
    for n, key in ((5, "C1"), (6, "C2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")] + write_lines(5)))
        P.append(blank())

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


COMPACT_KW_MARKED = [("若P則Q／只要P就Q", "{P->Q}"), ("只有P才Q", "{Q->P}（調轉）"),
                     ("除非P否則Q", "{~P->Q}（接否定）"), ("逆否命題", "{~Q->~P}（同原命題等價）")]


def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    card1 = [para("▍條件句對譯卡", bold=True, sz=HEADING_SZ)]
    card1 += [para(f"{k}　→　{v}", sz=21) for k, v in COMPACT_KW_MARKED]

    card2 = [para("⚠ 陷阱提醒卡", bold=True, sz=HEADING_SZ),
             para("・「只有P才Q」要調轉做 Q→P，唔係 P→Q", sz=21),
             para("・逆命題(Q→P)同原命題唔等價；逆否命題(¬Q→¬P)先至等價", sz=21),
             para("・「除非P否則Q」譯做 ¬P→Q", sz=21),
             para("・「至少一人」嘅否定係「一個都冇」", sz=21)]

    card3 = [para("▍定義判斷做法卡", bold=True, sz=HEADING_SZ),
             para("什麼時候翻我：見到「XX是指……」呢類定義句", sz=21),
             para("1. 將定義拆做①②③④逐項要件", sz=21),
             para("2. 四個選項逐一核對，要全部要件都符合先算", sz=21),
             para("3. 漏一項都唔算，唔可以「幾似就當啱」", sz=21)]

    card4 = [para("▍親屬關係做法卡", bold=True, sz=HEADING_SZ),
             para("什麼時候翻我：見到「我的……的……的……」呢類稱謂鏈", sz=21),
             para("1. 由最外層開始，一步步代入邊個係邊個", sz=21),
             para("2. 「獨生子／獨生女」提示呢一步得返一個人選", sz=21),
             para("3. 每代一步就寫低個名，唔好一次過諗成句", sz=21)]

    P.append(toolcard_sheet([card1, card2, card3, card4], cols=2, card_h=4200))
    return build_docx(P, os.path.join(HERE, CARD + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"->": r"\to", "~": r"\neg "}


def _tex(m):
    m = m.strip()
    body = m
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    return r"\(%s\)" % body


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out).replace("\n", "<br>")


def _lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + "</div>"


def _kw_html(rows):
    return "".join(f"<tr><td>{_esc(k)}</td><td>{_h(v)}</td></tr>" for k, v in rows)


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    kw_table = (f'<table class="d-tbl kw-table"><tr><th>題目說…</th><th>就寫成…</th></tr>'
                f'{_kw_html(COMPACT_KW)}</table>')

    secA = ""
    for n, key in ((1, "A1"), (2, "A2")):
        secA += (f'<div class="problem"><div>{n}．{_h(STEMS[key])}</div>'
                 f'{kw_table}<div>作答：</div>{_lines(3)}</div>')

    secB = ""
    for n, key in ((3, "B1"), (4, "B2")):
        secB += f'<div class="problem"><div>{n}．{_h(STEMS[key])}</div>{_lines(4)}</div>'

    secC = ""
    for n, key in ((5, "C1"), (6, "C2")):
        secC += f'<div class="problem"><div>{n}．{_h(STEMS[key])}</div>{_lines(5)}</div>'

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for i, key in enumerate(("A1", "A2", "B1", "B2", "C1", "C2"), 1):
        a = ANS[key]
        steps = "".join(f"<div>　（{j}）{_h(s)}</div>" for j, s in enumerate(a["steps"], 1))
        ansec += (f'<div class="problem"><div style="font-weight:700">{i}．答案：{_esc(a["ans"])}</div>'
                  f'<div>【規律】{_h(a["rule"])}</div>'
                  f'<div>【詳細步驟】</div>{steps}'
                  f'<div class="hint-card">【易錯點提示】{_h(a["pit"])}</div></div>')

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>每題旁邊都印住精簡對譯表。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>對譯表唔再逐題附，唔記得就自己諗返規則。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>完全冇對譯表提示，自己判斷句式類型。</div>
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
