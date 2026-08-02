# -*- coding: utf-8 -*-
"""
第3章 數理邏輯(一)．L15 數字與符號規律推理 —— 課堂練習 ＋ 工具卡 build script
主設計 D2 手順卡；輔助 D12 自我核對。鷹架密度：抽離小班 (Tier 2)。
褪除梯度：練習A 手順卡精簡版印喺題目旁 → 練習B 手順卡移到工具卡、題目唔再附 →
         練習C 完全唔提供手順卡，只喺自我核對清單提示。
題目來源：題庫 B1數字規律推理／B4文字符號規律推理／B5常識性排序／B7分類歸納推理，
         逐題核對題庫原答案；B5 原題 MOCK1-027 選項與條件有 OCR 缺陷（詳見驗算檔），
         已用結構相同、條件清晰嘅自編題取代（見 B4 題）。
產出：練習_數字與符號規律推理_抽離小班共用版.docx/.html/.pdf、工具卡_數字與符號規律推理.docx/.pdf
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_數字與符號規律推理_抽離小班共用版"
CARD = "工具卡_數字與符號規律推理"
UNIT = "第3章 數理邏輯(一)．L15 數字與符號規律推理"
FOOT = "高三數學．第3章 數理邏輯(一)．L15 數字與符號規律推理"

COMPACT_STEPS = ["觀察相鄰項（加減乘除、平方立方）", "唔得就試分組（隔一個／連續幾個一組）",
                 "揀一個假設", "代返去驗證晒全部已知項先落答案"]

STEMS = {
    "A1": "4　3　1　12　9　3　17　5　＿＿＿，求空格數字。〔B1 數字規律推理〕",
    "A2": "13　21　34　55　＿＿＿，求空格數字。〔B1 數字規律推理〕",
    "A3": "下列選項其中一個和其餘四個並不同類，試選出這個不同類的項：\n"
          "A．香蕉　B．蘋果　C．冬瓜　D．雪梨　E．西瓜〔B7 分類歸納推理〕",
    "A4": "「庚」字常用作表示順序的第（　）位？\nA．五　B．六　C．七　D．八〔B5 常識性排序〕",
    "B1": "625　49　576　47　＿＿＿　45　484，求空格數字。〔B1 數字規律推理〕",
    "B2": "12　10　＿＿＿　12　6　14　3，求空格數字。〔B1 數字規律推理〕",
    "B3": "「648：拾：4」相對下列哪組？\nA．846：千：4　B．754：百：4　C．496：百：4　D．485：拾：4〔B4 文字符號規律推理〕",
    "B4": "甲、乙、丙、丁四人參加棋賽，賽後排名沒有並列。已知：①甲的名次排在丙前面；"
          "②乙的名次不比丁後。根據以上兩個條件，哪一個組合一定不會奪得第一名？\n"
          "A．甲和乙　B．丙和丁　C．甲和丙　D．乙和丁〔B5 常識性排序・自編題〕",
    "C1": "0　1　2　4　4　9　6　16　8　＿＿＿，求空格數字。〔B1 數字規律推理〕",
    "C2": "1　1　8　2　＿＿＿　3　64　4　125　5，求空格數字。〔B1 數字規律推理〕",
    "C3": "下列方格內三組數字互有關係，問漏去的數字：\n"
          "第一欄（由上至下）：12、4、3\n第二欄（由上至下）：15、？、5\n第三欄（由上至下）：28、7、4"
          "〔B1 數字規律推理〕",
    "C4": "下列選項其中一個和其餘四個並不同類，試選出這個不同類的項：\n"
          "A．西遊記　B．紅樓夢　C．水滸傳　D．三國演義　E．阿Q正傳〔B7 分類歸納推理〕",
    "C5": "【開放題】請你自己出一條同類型嘅數字規律題（4～8個數字，中間留一個空格），"
          "寫低你自己設計嘅規律同答案，然後拎去同同學交換做。",
}

ANS = {
    "A1": dict(ans="C．12", kp="連續三個一組，組內第一數減第二數等於第三數。",
               fm="每組 (a, b, c) 符合 {a-b=c}。",
               steps=["分組：(4,3,1)、(12,9,3)、(17,5,?)。",
                      "驗證第一組：{4-3=1}✓；第二組：{12-9=3}✓。",
                      "套用去第三組：{17-5=12}。"],
               pit="以為規律係「三個一組加埋」（4+3=7≠1），冇試埋減法。"),
    "A2": dict(ans="B．89", kp="斐波那契式規律：每項＝前兩項之和。",
               fm="{a_n=a_(n-1)+a_(n-2)}。",
               steps=["驗證：{13+21=34}✓；{21+34=55}✓。",
                      "套用：{34+55=89}。"],
               pit="淨係睇差值（8,13,21……）冇發現差值本身都係加返兩項，"
                   "其實直接加返前兩項最快。"),
    "A3": dict(ans="C．冬瓜", kp="分類要搵返「共通屬性」，例外項通常違反其中一個屬性。",
               fm="—",
               steps=["香蕉、蘋果、雪梨、西瓜皆屬「一般認知中嘅水果」。",
                      "冬瓜屬瓜類蔬菜，唔係水果，故為不同類項。"],
               pit="按「有籽 / 有核」呢類次要特徵分類（例如西瓜多籽），"
                   "冇搵最大公因嘅「水果 vs 蔬菜」呢個分類。"),
    "A4": dict(ans="C．七", kp="十天干順序要背熟：甲乙丙丁戊己庚辛壬癸＝1至10。",
               fm="—",
               steps=["十天干：甲1、乙2、丙3、丁4、戊5、己6、庚7、辛8、壬9、癸10。",
                      "「庚」係第 7 位。"],
               pit="同十二地支（子丑寅卯……）混淆，或漏數/多數一個字。"),
    "B1": dict(ans="B．529", kp="交錯數列：奇數位與偶數位分別各自成一條規律，唔可以當成一條數列睇。",
               fm="奇數位（第1、3、5、7位）：{25^2,24^2,?,22^2}（底數遞減1）；"
                  "偶數位（第2、4、6位）：公差 −2 等差數列。",
               steps=["位置標號：625(1) 49(2) 576(3) 47(4) ?(5) 45(6) 484(7)。",
                      "奇數位：{25^2=625}、{24^2=576}、{22^2=484}——底數 25,24,?,22 遞減1，"
                      "所以第5位底數＝23，即 {23^2=529}。",
                      "偶數位：49,47,45 公差 −2，獨立成立、唔影響答案，但可用嚟確認"
                      "「交錯」呢個假設冇錯。"],
               pit="淨係將成串數字當一條數列去試相鄰關係，8條位置摻埋一齊試極都試唔出規律。"),
    "B2": dict(ans="C．9", kp="交錯數列，兩條規律都係等差，但公差方向唔同。",
               fm="奇數位（1,3,5,7位）：公差 −3；偶數位（2,4,6位）：公差 +2。",
               steps=["位置標號：12(1) 10(2) ?(3) 12(4) 6(5) 14(6) 3(7)。",
                      "奇數位：12, ?, 6, 3——公差 −3：{12-3=9}，驗證 {9-3=6}✓、{6-3=3}✓。",
                      "偶數位：10, 12, 14——公差 +2，獨立驗證通過，確認交錯假設成立。"],
               pit="見到 12 喺第1位又喺第4位出現，誤以為成串數字循環重複，"
                   "冇留意兩個 12 分別屬於奇數位同偶數位、係兩條唔同嘅規律。"),
    "B3": dict(ans="C．496：百：4", kp="規律係「[數字] : [位名] : 該位嘅數字」，要逐個選項核對三個位。",
               fm="—",
               steps=["648 嘅拾位（十位）數字係 4，符合原式。",
                      "A．846 只係三位數，冇「千位」，不成立。",
                      "B．754 嘅百位係 7，唔係 4，不成立。",
                      "C．496 嘅百位係 4，符合，成立。",
                      "D．485 嘅拾位係 8，唔係 4，不成立。"],
               pit="淨係睇最後嗰個數字「4」岩唔岩，冇連埋位名（千／百／拾）一齊核對；"
                   "648 係三位數但問嘅係「拾位」（十位），要留意題目本身唔要求判斷"
                   "有冇「千位」，位名同位數要分開睇。"),
    "B4": dict(ans="B．丙和丁", kp="排名比較題：先將文字條件轉做「較前 / 較後」關係，"
                                  "用反證法逐一檢查邊個唔可能係第一。",
               fm="設名次數字越細代表越前。條件①：{甲<丙}；條件②：「乙不比丁後」"
                  "即 {乙<丁}（賽果冇並列，故為嚴格較前）。",
               steps=["假設丙攞第一（丙＝1）：由條件①{甲<丙}，甲嘅名次要細過 1，"
                      "冇可能，矛盾。所以丙唔可能第一。",
                      "假設丁攞第一（丁＝1）：由條件②{乙<丁}，乙嘅名次要細過 1，"
                      "冇可能，矛盾。所以丁唔可能第一。",
                      "甲、乙兩人冇任何條件話佢哋唔可能排第一，故唔可以排除。",
                      "結論：一定唔會攞第一嘅組合係「丙和丁」。"],
               pit="淨係將「甲喺丙前面」理解成「甲一定係第一」，"
                   "冇考慮甲前面仲有冇其他人（本題冇話甲同乙邊個更前）；"
                   "答案問嘅係「肯定唔係第一」，唔係「肯定係第一」。"),
    "C1": dict(ans="B．25", kp="交錯數列：一條係等差，另一條係完全平方數。",
               fm="奇數位（1,3,5,7,9位）：公差 +2 等差；偶數位（2,4,6,8,10位）：{1^2,2^2,3^2,4^2,?}。",
               steps=["位置標號：0(1) 1(2) 2(3) 4(4) 4(5) 9(6) 6(7) 16(8) 8(9) ?(10)。",
                      "奇數位：0,2,4,6,8——公差 +2，獨立成立。",
                      "偶數位：1,4,9,16,?＝{1^2,2^2,3^2,4^2,?}——底數 1,2,3,4,?遞增1，"
                      "第10位底數＝5，即 {5^2=25}。"],
               pit="見到 4 呢個數字出現咗兩次（第4、5位），以為係抄錯或者要對齊，"
                   "其實係兩條唔同規律岩岩喺呢兩個位置撞埋一齊，屬巧合唔係錯誤。"),
    "C2": dict(ans="A．27", kp="交錯數列：一條係序數（1,2,3,4,5），另一條係立方數。",
               fm="偶數位（2,4,6,8,10位）：1,2,3,4,5（序數）；"
                  "奇數位（1,3,5,7,9位）：{1^3,2^3,?,4^3,5^3}。",
               steps=["位置標號：1(1) 1(2) 8(3) 2(4) ?(5) 3(6) 64(7) 4(8) 125(9) 5(10)。",
                      "偶數位：1,2,3,4,5——就係序數本身，獨立成立。",
                      "奇數位：1,8,?,64,125＝{1^3,2^3,?,4^3,5^3}——底數 1,2,?,4,5，"
                      "第5位（即整條數列第5位）底數＝3，即 {3^3=27}。"],
               pit="睇到序數 1,2,3,4,5 就以為空格都係序數（估答案係 3），"
                   "冇留意空格所在嘅位置（第5個位）其實屬於「立方」嗰條規律，唔係「序數」嗰條。"),
    "C3": dict(ans="D．3", kp="逐欄（直行）觀察關係，唔係逐列（橫行）。",
               fm="每欄：上 ÷ 中 ＝ 下。",
               steps=["第一欄核對：{12/4=3}，與第三數 3 相符 ✓。",
                      "第三欄核對：{28/7=4}，與第三數 4 相符 ✓。",
                      "套用去第二欄：{15/?=5} → {?=15/5=3}。"],
               pit="逐列（橫向）搵關係（12,15,28 之間、4,?,7 之間），"
                   "呢條題嘅規律其實喺直欄入面，橫向搵極都搵唔到。"),
    "C4": dict(ans="E．阿Q正傳", kp="分類要搵返「共通屬性」——呢度係「中國古典四大名著」。",
               fm="—",
               steps=["西遊記、紅樓夢、水滸傳、三國演義為中國古典四大名著。",
                      "阿Q正傳係魯迅所著嘅現代短篇小說，唔屬於四大名著，故為不同類項。"],
               pit="按「有冇改編電視劇」「係咪長篇小說」呢類次要特徵分類，"
                   "阿Q正傳都係長篇小說改編過，但關鍵分類屬性係「是否四大名著之一」。"),
    "C5": dict(ans="（開放題，教師逐份核對）", kp="出題者要親自驗算自己條規律至少兩次先算完成。",
               fm="—",
               steps=["建議格式：4～8個數字，中間留一個空格。",
                      "出題者要寫低（a）規律講法、（b）正確答案、（c）驗證用咗嘅方法"
                      "（相鄰／分組／假設驗證）。"],
               pit="出嘅規律唔夠精確，同一串數字可以砌出兩種唔同答案都啱——"
                   "呢種情況要退返去改到規律得一個答案先算過關。"),
}

HINT_TOP = "動手之前想返四個步驟：觀察相鄰 → 分組 → 假設 → 驗證晒全部已知項。"
SELFCHECK = ["我試過相鄰項嘅加減乘除同平方立方。",
             "我試過兩種分組法（隔一個／連續幾個一組）。",
             "我嘅假設代返去，全部已知項都啱。",
             "答案有揀返對應嘅選項。"]


# ================================================================ docx
def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    # ---- 練習A：手順卡精簡版印喺題目旁 ----
    P.append(heading(f"一、練習A（{star_label(1)}）"))
    P.append(para("每一題旁邊都印住精簡版手順卡，跟住做。"))
    for key in ("A1", "A2", "A3", "A4"):
        P.append(problem_box([para(STEMS[key])]))
        P.append(step_card("規律偵測四步（精簡版）",
                           [(s, None) for s in COMPACT_STEPS], compact=True))
        P.append(para("作答："))
        P += write_lines(4)
        P.append(blank())

    # ---- 練習B：手順卡移到工具卡，題目唔再附 ----
    P.append(heading(f"二、練習B（{star_label(2)}）", page_break_before=True))
    P.append(para("呢一節題目唔再附手順卡——唔記得步驟就翻工具卡。"))
    for key in ("B1", "B2", "B3", "B4"):
        P.append(problem_box([para(STEMS[key])] + write_lines(5)))
        P.append(blank())

    # ---- 練習C：完全唔提供手順卡 ----
    P.append(heading(f"三、練習C（{star_label(3)}）", page_break_before=True))
    P.append(para("呢一節完全唔提供手順卡，自己決定點試。C5 係開放題，冇固定答案。"))
    for key in ("C1", "C2", "C3", "C4"):
        P.append(problem_box([para(STEMS[key])] + write_lines(5)))
        P.append(blank())
    P.append(problem_box([para(STEMS["C5"])] + write_lines(6)))

    P.append(selfcheck_list(SELFCHECK))

    # ---- 參考答案 ----
    P.append(heading("參考答案與詳解（教師用）", page_break_before=True))
    for key in ("A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "C5"):
        a = ANS[key]
        P.append(para(f"{key}．答案：{a['ans']}", bold=True))
        P.append(para(f"【考點】{a['kp']}"))
        if a["fm"] != "—":
            P.append(para(f"【規律／關係式】{a['fm']}"))
        P.append(para("【詳細步驟】"))
        for i, s in enumerate(a["steps"], 1):
            P.append(para(f"　（{i}）{s}"))
        P.append(shaded_box(f"【易錯點提示】{a['pit']}"))
        P.append(blank())

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ================================================================ 工具卡
def build_toolcard_docx():
    P = [masthead("高三數學", UNIT, "工具卡（剪下沿虛線，護貝後放桌面）")]
    card1 = [para("▍規律偵測四步（精簡版）", bold=True, sz=HEADING_SZ)]
    card1 += [para(f"{i}. {s}", sz=21) for i, s in enumerate(COMPACT_STEPS, 1)]

    card2 = [para("▍兩種分組法睇一睇", bold=True, sz=HEADING_SZ),
             para("什麼時候翻我：相鄰關係試極都試唔出嘅時候", sz=21),
             para("・隔一個分兩組：奇數位一組、偶數位一組（例：兩條規律交錯出現）", sz=21),
             para("・連續幾個一組：每 3～4 個分一組，睇組內關係（例：{a-b=c} 或 {a/b=c}）", sz=21),
             para("・方格/直欄題：留意規律可能喺「直欄」入面，唔一定喺「橫列」", sz=21)]

    card3 = [para("⚠ 常見錯誤提醒卡", bold=True, sz=HEADING_SZ),
             para("什麼時候翻我：試咗一種方法就想放棄嘅時候", sz=21),
             para("・淨試相鄰加減，冇試埋乘除、平方、立方", sz=21),
             para("・淨試一種分組法就放棄，兩種都要試過", sz=21),
             para("・只驗證一兩個已知數字就落答案，冇驗證晒全部", sz=21),
             para("・分類題：搵緊嘅係「大分類」，唔係細節特徵", sz=21)]

    card4 = [para("▍做完自己核對一次", bold=True, sz=HEADING_SZ)]
    card4 += [para(f"☐ {t}", sz=21) for t in SELFCHECK]

    P.append(toolcard_sheet([card1, card2, card3, card4], cols=2, card_h=4200))
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
    p = re.fullmatch(r"(\d+)\^(\d+)=?(-?\d+)?", m)
    if p:
        base, exp, val = p.groups()
        s = r"%s^{%s}" % (base, exp)
        if val is not None:
            s += "=" + val
        return r"\(%s\)" % s
    sub = re.fullmatch(r"a_n=a_\(n-1\)\+a_\(n-2\)", m)
    if sub:
        return r"\(a_n=a_{n-1}+a_{n-2}\)"
    body = m
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    body = re.sub(r"(\d+)/(\d+)", r"\\frac{\1}{\2}", body)
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


def _step_card_html(title, steps, trigger=None):
    rows = "".join(f"<tr><td>{i}. {_esc(s)}</td></tr>" for i, s in enumerate(steps, 1))
    trig = f"<div>什麼時候用：{_esc(trigger)}</div>" if trigger else ""
    return (f'<div class="step-card"><div style="font-weight:700">{_esc(title)}</div>'
            f'{trig}<table class="d-tbl">{rows}</table></div>')


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    secA = ""
    for key in ("A1", "A2", "A3", "A4"):
        secA += (f'<div class="problem"><div>{key}．{_h(STEMS[key])}</div>'
                 f'{_step_card_html("規律偵測四步（精簡版）", COMPACT_STEPS)}'
                 f'<div>作答：</div>{_lines(4)}</div>')
    secB = "".join(f'<div class="problem"><div>{key}．{_h(STEMS[key])}</div>{_lines(5)}</div>'
                   for key in ("B1", "B2", "B3", "B4"))
    secC = "".join(f'<div class="problem"><div>{key}．{_h(STEMS[key])}</div>{_lines(5)}</div>'
                   for key in ("C1", "C2", "C3", "C4"))
    secC += f'<div class="problem"><div>{_h(STEMS["C5"])}</div>{_lines(6)}</div>'

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for key in ("A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "C5"):
        a = ANS[key]
        steps = "".join(f"<div>　（{i}）{_h(s)}</div>" for i, s in enumerate(a["steps"], 1))
        fm = f'<div>【規律／關係式】{_h(a["fm"])}</div>' if a["fm"] != "—" else ""
        ansec += (f'<div class="problem"><div style="font-weight:700">{key}．答案：'
                  f'{_h(a["ans"])}</div>'
                  f'<div>【考點】{_h(a["kp"])}</div>{fm}'
                  f'<div>【詳細步驟】</div>{steps}'
                  f'<div class="hint-card">【易錯點提示】{_h(a["pit"])}</div></div>')

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>
  <div>每一題旁邊都印住精簡版手順卡，跟住做。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）</div>
  <div>呢一節題目唔再附手順卡——唔記得步驟就翻工具卡。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）</div>
  <div>呢一節完全唔提供手順卡，自己決定點試。C5 係開放題，冇固定答案。</div>
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
