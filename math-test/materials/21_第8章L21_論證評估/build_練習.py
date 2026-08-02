# -*- coding: utf-8 -*-
"""
第8章 語文與邏輯推理(三)．L21 論證評估 —— 課堂練習 build script
主設計 D6 明確教學三階段（練習A=我們做，練習B/C=你做）；輔助 D13 弗雷爾模型。
鷹架密度：抽離小班 (Tier 2)。
題目來源：A1為自編題，A2/B1/C1改編自題庫真實題目（MOCK3-016、VERBAL1-048、
VERBAL1-051），逐題親自驗算，見 驗算_論證評估.md。
產出：練習_論證評估_抽離小班共用版.docx/.html/.pdf（本課設計無需獨立工具卡，
弗雷爾模型已在講義出現，練習時翻返講義即可）。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "練習_論證評估_抽離小班共用版"
UNIT = "第8章 語文與邏輯推理(三)．L21 論證評估"
FOOT = "高三數學．第8章 語文與邏輯推理(三)．L21 論證評估"

HINT_TOP = "動手之前：搵出結論同論據，逐個選項問「支持／削弱／無關」。"
SELFCHECK = ["我搵出咗結論同論據，唔係得個大概印象。", "我逐個選項都判斷咗係支持/削弱/無關。",
            "我講得出點解淨返嗰個選項先啱，其餘點解唔啱。"]

STEMS = {
    "A1": "茶餐廳老闆話：「今個月生意額上升咗兩成，證明我哋間鋪嘅出品越嚟越受歡迎。」"
          "以下邊項如果為真，最能削弱佢嘅講法？\n"
          "A．呢個月茶記啲食物全部加咗價一成\nB．老闆每日都準時開鋪\n"
          "C．呢條街嘅其他舖頭裝修翻新咗\nD．老闆用緊嘅食材同上個月一樣",
    "A2": "有兩個電訊計劃：A電訊，每日上限500MB，不能累積使用；B電訊，數據無限。"
          "以下邊句廣告最符合A電訊？\nA．每日最低12蚊\nB．30蚊10日有5GB任用\n"
          "C．五種計劃總有一個啱你\nD．7日全城最低",
    "B1": "某市某繁華街道「十字路口可見度改善工程」竣工後，有兩份調查報告："
          "第一份話工程減少咗交通事故；第二份話工程完工後每週交通事故反而增加咗，"
          "所以工程增加咗事故發生嘅機率。以下邊項對評估第二份報告最有用？\n"
          "A．工程完工後，值勤交警平均值勤時間係幾多\nB．工程完工後，呢個十字路口"
          "嘅車流量改變情況如何\nC．鄰近城鎮喺改善路段可見度方面採取咗咩措施\n"
          "D．工程完工後，該十字路口係咪唔便於行人通行",
    "C1": "研究人員話搵到一種用咖啡因控制糖尿病人血糖濃度嘅新方法。佢哋對患糖尿病嘅"
          "小鼠做實驗，攝取咖啡因嘅小鼠血糖控制能力較好。研究人員認為，未來注射"
          "胰島素嘅方法可以被攝取咖啡因取代。以下邊項最能支持呢個結論？\n"
          "A．呢個研究成果發表喺全球頂尖醫學期刊上\nB．每日注射胰島素對病人嚟講比較麻煩\n"
          "C．研究證明咖啡因可以降低直腸癌同黑色素瘤嘅發病風險\n"
          "D．小鼠同人類體內嘅腎臟細胞吸收咖啡因會促進胰島素嘅產生",
    "C2": "【開放題】請你自己設計一條支持／削弱論證題：寫一句包含「結論」同「論據」嘅"
          "陳述，再設計4個選項（1個真正支持、1個真正削弱、2個無關），"
          "寫低你嘅答案同理由，然後同同學交換做。",
}

ANS = dict(
    A1=dict(ans="A．食物全部加咗價一成",
            rel="削弱——提供咗一個「其他解釋」：營業額上升可以純粹係加價造成，"
                "唔一定係顧客量增加或者出品變得更受歡迎。",
            elim="B、C、D都同「營業額上升嘅原因」冇直接關係，唔提供任何"
                "支持或削弱嘅理由，屬於「無關」選項。"),
    A2=dict(ans="A．每日最低12蚊",
            rel="評估（符合特徵）——A電訊嘅核心特徵係「按日計、每日500MB上限、"
                "唔可以累積」，「每日最低12蚊」正正扣連「按日」計費呢個特點。",
            elim="B「10日5GB任用」——平均每日 {5000/10=500} MB數值啱，但「任用」暗示10日內"
                "可以跨日彈性運用（即可以累積），同「不能累積使用」呢個核心限制矛盾；"
                "C、D都係空泛廣告詞，無法對應A電訊嘅具體特徵。"),
    B1=dict(ans="B．車流量改變情況如何",
            rel="評估（搵出混淆變數）——第二份報告淨係憑「事故數增加」就話"
                "「工程令事故機率上升」，但忽略咗車流量呢個混淆變數：如果車流量本身"
                "大幅上升，事故總數自然可能上升，未必係工程嘅過錯（甚至事故率／每車次"
                "事故機率可能其實下降咗）。",
            elim="A交警值勤時間、C鄰近城鎮嘅措施、D是否便於行人通行，都同"
                "「工程是否真係導致事故機率上升」呢個因果判斷關聯薄弱。"),
    C1=dict(ans="D．小鼠同人類嘅腎臟細胞吸收咖啡因會促進胰島素產生",
            rel="支持（搭橋）——論點同論據之間缺嘅係「咖啡因點樣喺人體內實際發揮"
                "類似胰島素嘅降血糖機制」呢座橋樑。D直接搭建咗「咖啡因」同「胰島素"
                "分泌」之間嘅因果橋樑，並將小鼠實驗結果類推去人類生理機制，"
                "具體加強咗論點嘅可信度。",
            elim="A訴諸期刊權威，唔能夠證明結論本身成立；B淨係話注射麻煩，同"
                "「可唔可以被取代」冇關；C咖啡因降低其他癌症風險，同血糖控制、"
                "取代胰島素無關；三項皆屬「無關」。"),
    C2=dict(ans="（開放題，教師逐份核對）",
            rel="出題者要確保四個選項入面，真正支持同真正削弱嘅各得一個，"
                "唔可以模稜兩可。",
            elim="出題者要親自驗算：畀第二個人做，睇佢揀嘅同你心目中嘅答案"
                "是否一致。"),
)


def build_practice_docx():
    P = [masthead("高三數學", UNIT, "課堂練習"), student_info_row()]
    P.append(shaded_box(HINT_TOP))

    P.append(heading(f"一、練習A（{star_label(1)}）——我們做"))
    P.append(para("同老師一齊核對，做完一齊對答案先入第二題。"))
    for n, key in ((1, "A1"), (2, "A2")):
        P.append(problem_box([para(f"{n}．{STEMS[key]}")] + write_lines(3)))
        P.append(blank())

    P.append(heading(f"二、練習B（{star_label(2)}）——你做", page_break_before=True))
    P.append(para("獨立完成，唔使再一齊核對。"))
    P.append(problem_box([para(f"3．{STEMS['B1']}")] + write_lines(4)))
    P.append(blank())

    P.append(heading(f"三、練習C（{star_label(3)}）——你做", page_break_before=True))
    P.append(para("最後兩題，第5題係開放題。"))
    P.append(problem_box([para(f"4．{STEMS['C1']}")] + write_lines(4)))
    P.append(blank())
    P.append(problem_box([para(f"5．{STEMS['C2']}")] + write_lines(6)))

    P.append(selfcheck_list(SELFCHECK))

    P.append(heading("參考答案與詳解（教師用）", page_break_before=True))
    for i, key in enumerate(("A1", "A2", "B1", "C1", "C2"), 1):
        a = ANS[key]
        P.append(para(f"{i}．答案：{a['ans']}", bold=True))
        P.append(para(f"【判斷】{a['rel']}"))
        P.append(shaded_box(f"【剔除其餘選項】{a['elim']}"))
        P.append(blank())

    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


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


def build_practice_html():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"練習：{UNIT}")

    secA = ""
    for n, key in ((1, "A1"), (2, "A2")):
        secA += f'<div class="problem"><div>{n}．{_stem_html(STEMS[key])}</div>{_lines(3)}</div>'

    secB = f'<div class="problem"><div>3．{_stem_html(STEMS["B1"])}</div>{_lines(4)}</div>'

    secC = (f'<div class="problem"><div>4．{_stem_html(STEMS["C1"])}</div>{_lines(4)}</div>'
            f'<div class="problem"><div>5．{_stem_html(STEMS["C2"])}</div>{_lines(6)}</div>')

    chk = ('<div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>'
           + "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK) + "</div>")

    ansec = ""
    for i, key in enumerate(("A1", "A2", "B1", "C1", "C2"), 1):
        a = ANS[key]
        ansec += (f'<div class="problem"><div style="font-weight:700">{i}．答案：{_esc(a["ans"])}</div>'
                  f'<div>【判斷】{_esc(a["rel"])}</div>'
                  f'<div class="hint-card">【剔除其餘選項】{_h(a["elim"])}</div></div>')

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂練習</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="hint-card">{_esc(HINT_TOP)}</div>

  <div class="section-h">一、練習A（<span class="stars">★☆☆</span>）——我們做</div>
  <div>同老師一齊核對，做完一齊對答案先入第二題。</div>
  {secA}

  <div class="section-h page-break">二、練習B（<span class="stars">★★☆</span>）——你做</div>
  <div>獨立完成，唔使再一齊核對。</div>
  {secB}

  <div class="section-h page-break">三、練習C（<span class="stars">★★★</span>）——你做</div>
  <div>最後兩題，第5題係開放題。</div>
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
