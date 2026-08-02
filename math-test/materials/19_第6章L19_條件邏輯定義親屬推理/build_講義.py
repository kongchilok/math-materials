# -*- coding: utf-8 -*-
"""
第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係 —— 課堂講義 build script
（本課處理 C1 命題邏輯嘅「條件式邏輯」子結構——若P則Q/只有…才…等，
 加埋 C4 定義判斷、C5 親屬關係推理；排列組合式邏輯謎題另立 L18 處理。）
主設計 D8 關鍵字對譯（邏輯連接詞：若則／只要／只有／除非／並非／所有）；
輔助 D11 標記對應法（①②③④標示要件或人物代號）。鷹架密度：抽離小班 (Tier 2)。
題目多數改編自題庫真實題目，逐題親自驗算，見驗算檔。
產出：講義_條件邏輯定義親屬推理_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_條件邏輯定義親屬推理_抽離小班共用版"
UNIT = "第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係"
FOOT = "高三數學．第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係"

INTRO = [
    "呢三種題型（條件推理、定義判斷、親屬關係）睇落好唔同，但有一個共通動作："
    "將一句長長的中文句子，翻譯成短短嘅符號或者標記，先至睇得出裡面嘅結構。",
    "呢一課用嘅方法係「關鍵字對譯表」：見到「若……則」「只要……就」「只有……才」"
    "「除非……否則」呢啲固定句式，即刻翻做符號；見到定義題嘅「要件」就用①②③④"
    "編號；見到親屬關係嘅稱謂就一步步代人。",
]

KW_GENERAL = [
    ("若P，則Q　／　只要P，就Q", "{P->Q}"),
    ("只有P，才Q", "{Q->P}　（注意：主詞客詞掉轉咗）"),
    ("並非（P或Q）", "{~P} 且 {~Q}"),
    ("並非（P且Q）", "{~P} 或 {~Q}"),
    ("所有A都是B", "{A->B}（三段論嘅大前提句式）"),
    ("有些A是B", "A同B有交集，唔可以逆推做「所有A都係B」"),
]
KW_TRAPS = [
    ("除非P，否則Q", "{~P->Q}　（唔係 {P->Q}，「除非」要接否定）"),
    ("P→Q 嘅逆命題「Q→P」", "同原命題唔等價！唔可以將若則句隨便掉轉主客詞"),
    ("P→Q 嘅逆否命題「¬Q→¬P」", "同原命題「恆等價」，可以自由使用嚟推理"),
    ("「至少一人」嘅否定", "「一個都冇」，唔係「唔止一人」"),
]

DEMO_STEM = ("【範例】如果你犯了法，你就會受到法律制裁；如果你受到法律制裁，別人就會"
            "看不起你；如果別人看不起你，你就無法受到尊重；而只有得到別人的尊重，"
            "你才能過得舒心。從上述敘述，可以推出以下邊個結論？\n"
            "A．你不犯法，日子就會過得舒心。\n"
            "B．你犯了法，日子就不會過得舒心。\n"
            "C．你日子過得不舒心，證明你犯了法。")

DEMO_WALK = [
    "第①句：犯法 → 受制裁。", "第②句：受制裁 → 被睇唔起。", "第③句：被睇唔起 → 唔受尊重。",
    "第④句「只有尊重，才舒心」係「只有…才…」句式，要對調：舒心 → 受尊重。",
    "第④句要用嚟做推理，要用佢嘅逆否命題（同原命題等價）：唔受尊重 → 唔舒心。",
    "而家將①②③④嘅逆否命題全部串埋一齊：犯法 → 受制裁 → 被睇唔起 → 唔受尊重 → 唔舒心。",
    "四個箭嘴連成一條鏈，中間冇斷位，所以「犯法 → 唔舒心」呢個結論成立，對應選項B。",
]

TN = dict(
    main_design="D8 關鍵字對譯（邏輯連接詞）",
    aux_designs=("D11 標記對應法",),
    reason=(
        "本課處理題庫 C1 命題邏輯入面嘅「條件式邏輯」子結構（若P則Q、只有…才…等），"
        "加埋 C4 定義判斷（4題）、C5 親屬關係推理（3題採用）。呢三種題型表面上唔同，"
        "但瓶頸都係「將一句長中文句子轉做結構化符號」：條件推理要將「若則／只有…才」"
        "轉做箭嘴符號；定義判斷要將定義拆做逐項「要件」；親屬關係要將稱謂逐步代入。"
        "D8 關鍵字對譯將呢啲固定句式嘅轉譯規則白紙黑字寫低，尤其標明陷阱"
        "（「只有…才」主客詞要調轉、「除非…否則」要接否定、逆命題唔等價但逆否命題"
        "等價）；D11 標記對應（①②③④）用嚟標示定義題嘅逐項要件，或者親屬關係嘅"
        "人物代號，令核對更清楚。"),
    density="抽離小班（Tier 2）",
    fading=(
        "關鍵字對譯表：講義範例全部展開並示範完整代入 → 練習A/B 題目旁印精簡對譯表 → "
        "練習C 唔提供對譯表，自己回想規則。｜"
        "標記①②③④：全程保留（定義要件／人物代號用嚟核對，唔設褪除）。"),
    flows=("F1 師徒制對話四步（追問「呢句係邊種句式？翻譯完之後箭嘴指邊個方向？」）",),
    iep_codes=("a3 提示題目重點", "a6 增加行距", "a8 提供關鍵字對譯表作為長期參考工具"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("題目來源",
            "部分題目改編自題庫真實題目，逐題親自驗算，詳見"
            "《驗算_條件邏輯定義親屬推理.md》。"),
           ("配套文件",
            "《第6章 L19 條件邏輯／定義判斷／親屬關係　課堂練習》（練習A／B／C ＋參考答案）、"
            "《工具卡》（關鍵字對譯精簡版，學生剪下護貝放桌面）。")),
)


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、關鍵字對譯表"))
    P.append(para("讀到條件句式，先喺句子上面做記號，翻做符號先開始推理。"))
    P.append(keyword_table(KW_GENERAL, KW_TRAPS))

    P.append(heading("三、範例：完整走一次"))
    P.append(problem_box([para(DEMO_STEM)]))
    for t in DEMO_WALK:
        P.append(para(t))
    P.append(shaded_box("答案：B。留意第④句「只有…才…」一定要調轉先啱，"
                        "同埋成條鏈用嘅係逆否命題，唔係逆命題。"))

    P.append(heading("四、定義判斷同親屬關係，一樣要「拆件」"))
    P.append(para("定義判斷題：將定義句拆做逐項「要件」，編上①②③④，"
                  "四個選項逐一核對是否「全部」要件都符合——漏一項都唔算。"))
    P.append(para("親屬關係題：由外層開始，一步步代入（「我媽媽的女兒」先睇「我媽媽」"
                  "係邊個、佢嘅「女兒」係邊個），唔好一次過睇成句。"))

    P.append(heading("五、接下來"))
    P.append(para("請拿出《第6章 L19 條件邏輯／定義判斷／親屬關係　課堂練習》，"
                  "善用關鍵字對譯表完成練習A、練習B、練習C。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


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
    intro = "".join(f"<div>{_esc(t)}</div>" for t in INTRO)
    walk = "".join(f"<div>{_h(t)}</div>" for t in DEMO_WALK)

    kw_rows = "".join(f"<tr><td>{_esc(k)}</td><td>{_h(v)}</td></tr>" for k, v in KW_GENERAL)
    kw_rows += '<tr class="trap"><td colspan="2">⚠ 陷阱詞（要想一下，不能直接照字面翻）</td></tr>'
    kw_rows += "".join(f"<tr><td>{_esc(k)}</td><td>{_h(v)}</td></tr>" for k, v in KW_TRAPS)

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

  <div class="section-h">二、關鍵字對譯表</div>
  <div>讀到條件句式，先喺句子上面做記號，翻做符號先開始推理。</div>
  <table class="d-tbl kw-table">
    <tr><th>題目說…</th><th>就寫成…</th></tr>
    {kw_rows}
  </table>

  <div class="section-h page-break">三、範例：完整走一次</div>
  <div class="problem">{_h(DEMO_STEM)}</div>
  {walk}
  <div class="hint-card">答案：B。留意第④句「只有…才…」一定要調轉先啱，同埋成條鏈用嘅係逆否命題，唔係逆命題。</div>

  <div class="section-h">四、定義判斷同親屬關係，一樣要「拆件」</div>
  <div>定義判斷題：將定義句拆做逐項「要件」，編上①②③④，四個選項逐一核對是否<b>全部</b>要件都符合——漏一項都唔算。</div>
  <div>親屬關係題：由外層開始，一步步代入（「我媽媽的女兒」先睇「我媽媽」係邊個、佢嘅「女兒」係邊個），唔好一次過睇成句。</div>

  <div class="section-h">五、接下來</div>
  <div>請拿出《第6章 L19 條件邏輯／定義判斷／親屬關係　課堂練習》，善用關鍵字對譯表完成練習A、練習B、練習C。</div>

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
