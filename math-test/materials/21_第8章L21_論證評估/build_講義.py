# -*- coding: utf-8 -*-
"""
第8章 語文與邏輯推理(三)．L21 論證評估 —— 課堂講義 build script
主設計 D6 明確教學三階段（我做→我們做→你做，體現在講義示範/練習A/練習B-C的遞進結構）；
輔助 D13 弗雷爾模型（支持／削弱／無關 三類論證的定義與例子區分）。
鷹架密度：抽離小班 (Tier 2)。題目多數改編自題庫真實題目，逐題親自驗算，見驗算檔。
產出：講義_論證評估_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_論證評估_抽離小班共用版"
UNIT = "第8章 語文與邏輯推理(三)．L21 論證評估"
FOOT = "高三數學．第8章 語文與邏輯推理(三)．L21 論證評估"

INTRO = [
    "呢類題目（論證評估）淨係得 {4} 題原題，係全份題庫題量最少嘅類型之一，"
    "但係一種全新嘅題型——同之前學過嘅全部題型都唔同，所以呢一課用「我做→我們做→你做」"
    "三步走：先睇我完整示範一題，再一齊做一題，最後你自己做。",
    "核心概念：一段論證有「結論」同「論據」，題目問你揀邊個選項可以「支持」（令論證"
    "更可信）、「削弱」（令論證冇咁可信）、定係「無關」（同論證有冇道理完全冇關係）。",
]

FRAYER_LABELS = ("支持：點樣先算", "削弱：點樣先算", "無關：點樣先算", "分辨小訣竅")
FRAYER_CONTENT = [
    "提出一個新嘅理由或者機制，令結論更加可信；或者搭建論據同結論之間缺咗嘅橋樑。",
    "提出一個相反嘅事實，或者一個「其他解釋」，令結論冇咗以為咁可信。",
    "同結論表面上有啲關聯嘅字眼，但其實冇提供任何有力嘅理由去支持或者推翻個結論。",
    "問自己：「如果呢句係真嘅，個結論會唔會變得更可信 / 更唔可信 / 完全冇分別？」",
]

DEMO_STEM = ("【範例】一家剛開幕的大型超市決定進行降價促銷，部分商品售價低於成本價，"
            "銷售量越大、超市嘅經濟損失就越大。呢個決定遭到員工反對，但經理依然堅持。"
            "以下邊項最能支持經理嘅決定？\n"
            "A．薄利多銷嘅方式有利於提高超市銷售收入\n"
            "B．物美價廉嘅商品更容易受到消費者嘅歡迎\n"
            "C．擴大知名度對新開幕嘅超市至關重要\n"
            "D．許多超市在開業時都會進行降價促銷活動")

DEMO_WALK_TEACHER = [
    "第一步（我做）：搵出「結論」同「論據」。結論：經理堅持促銷。論據（題目已經話畀你聽）："
    "「賣得越多、虧得越多」。",
    "第二步（我做）：問自己——經理明知會虧損都仲要做，即係佢一定有啲「虧損以外」嘅理由。"
    "邊個選項可以講出呢個理由？",
    "第三步（我做）：逐個選項核對。A「薄利多銷提高收入」——同題目「賣越多虧越多」"
    "直接矛盾，唔可以支持。B「物美價廉受歡迎」——只係一般常識，冇解釋到「明知蝕本"
    "都要做」呢個關鍵。D「好多超市都咁做」——只係從眾事實，唔係理由。C「擴大知名度"
    "對新舖好重要」——提供咗一個「用短期蝕本換長期客源」嘅策略性理由，正正解釋到"
    "點解經理明知會虧都要撐落去。",
    "答案：C。",
]

TN = dict(
    main_design="D6 明確教學三階段（我做→我們做→你做）",
    aux_designs=("D13 弗雷爾模型（支持／削弱／無關）",),
    reason=(
        "本課處理題庫第8章 C3 論證評估，全份題庫僅4題，且係一種全新題型——瓶頸唔係"
        "承接返之前學過嘅任何一種結構，而係第一次接觸「論證有結論、有論據，選項"
        "分做支持／削弱／無關」呢個框架本身。D6 明確教學三階段（我做完整示範→"
        "我們做半扶半放→你做完全獨立）係處理「全新概念導入」嘅標準設計，避免"
        "學生喺仲未搞清楚基本框架嘅時候就被要求獨立作答；D13 弗雷爾模型將"
        "「支持／削弱／無關」三個類別各自嘅定義同分辨訣竅並排列出，"
        "幫學生喺揀選項嗰陣有一個清晰嘅分類框架可以對照。"),
    density="抽離小班（Tier 2）",
    fading=(
        "教學流程：講義範例由老師完整示範（我做）→ 練習A 提供部分鷹架、"
        "師生一齊核對（我們做）→ 練習B/C 學生獨立作答（你做）。｜"
        "弗雷爾模型：練習A/B 題目旁保留精簡三分類提示 → 練習C 完全唔提供，"
        "自己判斷邊類。"),
    flows=("D6 我做→我們做→你做（本課題量少，唔分多課，一課之內完成三階段）",),
    iep_codes=("a3 提示題目重點", "a6 增加行距", "a7 調整計分標準（分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("題目來源",
            "部分題目改編自題庫真實題目，部分為結構相同之自編題，逐題親自驗算，"
            "詳見《驗算_論證評估.md》。"),
           ("配套文件",
            "《第8章 L21 論證評估　課堂練習》（練習A／B／C ＋參考答案）。")),
)


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、三種論證關係（弗雷爾模型）"))
    P.append(para("見到選項，先問自己：呢句係支持、削弱，定係同結論完全無關？"))
    labels_content = list(zip(FRAYER_LABELS, FRAYER_CONTENT))
    P.append(quadrant_workspace(FRAYER_LABELS, cell_h=1500))
    P.append(para("（工作區用嚟自己填寫理解；下面係完整定義，先睇一次）"))
    for lab, content in labels_content:
        P.append(shaded_box(f"【{lab}】{content}"))

    P.append(heading("三、範例：完整走一次（我做——老師示範）"))
    P.append(problem_box([para(DEMO_STEM)]))
    for t in DEMO_WALK_TEACHER:
        P.append(para(t))
    P.append(shaded_box("留意：呢一步驟嘅重點唔係「揀啱」，而係「講得出點解其餘三個"
                        "選項唔啱」——支持題要逐個排除「無關」同「矛盾」嘅選項。"))

    P.append(heading("四、接下來"))
    P.append(para("請拿出《第8章 L21 論證評估　課堂練習》。練習A 會有老師一齊帶住做"
                  "（我們做），練習B、練習C 請自己獨立完成（你做）。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(r"\(%s\)" % m.group(1).strip())
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def build_html_file():
    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join(f"<tr><td>{_esc(k)}</td><td>{_esc(v)}</td></tr>" for k, v in tn_rows)
    intro = "".join(f"<div>{_h(t)}</div>" for t in INTRO)
    walk = "".join(f"<div>{_esc(t)}</div>" for t in DEMO_WALK_TEACHER)
    frayer_boxes = "".join(
        f'<div class="hint-card"><b>【{_esc(lab)}】</b>{_esc(content)}</div>'
        for lab, content in zip(FRAYER_LABELS, FRAYER_CONTENT))

    def _quadrant_html(labels):
        rows = ""
        for i in range(0, len(labels), 2):
            pair = labels[i:i + 2]
            cells = "".join(f'<td><div class="qlabel">{_esc(l)}</div></td>' for l in pair)
            rows += f"<tr>{cells}</tr>"
        return f'<table class="d-tbl quadrant">{rows}</table>'

    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", f"講義：{UNIT}")

    body = f"""
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：{_esc(UNIT)}</span><span>類型：課堂講義</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="section-h">一、這一課要做到的事</div>
  {intro}

  <div class="section-h">二、三種論證關係（弗雷爾模型）</div>
  <div>見到選項，先問自己：呢句係支持、削弱，定係同結論完全無關？</div>
  {_quadrant_html(FRAYER_LABELS)}
  <div>（工作區用嚟自己填寫理解；下面係完整定義，先睇一次）</div>
  {frayer_boxes}

  <div class="section-h page-break">三、範例：完整走一次（我做——老師示範）</div>
  <div class="problem">{_esc(DEMO_STEM).replace(chr(10), "<br>")}</div>
  {walk}
  <div class="hint-card">留意：呢一步驟嘅重點唔係「揀啱」，而係「講得出點解其餘三個選項唔啱」——支持題要逐個排除「無關」同「矛盾」嘅選項。</div>

  <div class="section-h">四、接下來</div>
  <div>請拿出《第8章 L21 論證評估　課堂練習》。練習A 會有老師一齊帶住做（我們做），練習B、練習C 請自己獨立完成（你做）。</div>

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
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(head + body)
    return path


if __name__ == "__main__":
    print(build_docx_file())
    print(build_html_file())
