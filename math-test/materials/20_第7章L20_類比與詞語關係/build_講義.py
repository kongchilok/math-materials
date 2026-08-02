# -*- coding: utf-8 -*-
"""
第7章 語文與邏輯推理(二)．L20 類比與詞語關係 —— 課堂講義 build script
主設計 D8 關鍵字對譯（常見詞語關係類型對照表）；輔助 D12 自我核對清單。
鷹架密度：抽離小班 (Tier 2)。題目多數改編自題庫真實題目，逐題親自驗算，見驗算檔。
產出：講義_類比與詞語關係_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_類比與詞語關係_抽離小班共用版"
UNIT = "第7章 語文與邏輯推理(二)．L20 類比與詞語關係"
FOOT = "高三數學．第7章 語文與邏輯推理(二)．L20 類比與詞語關係"

INTRO = [
    "呢類題目（類比推理、詞語關係）好多同學靠「感覺似唔似」去揀答案，撞中率好睇彩數。"
    "真正嘅方法係：先講得出「已知嗰對詞係咩關係」，先至去揀「同一種關係」嘅選項——"
    "唔係揀「感覺有啲關聯」嗰個。",
    "常見嘅關係類型唔多，見到就對照返嚟，唔使每次由零諗。",
]

KW_GENERAL = [
    ("反義", "意思相反，例：黑↔白、峰迴路轉↔山窮水盡"),
    ("近義", "意思相似，例：建造≈建設"),
    ("類別：實例", "前者係後者所屬嘅大類，例：金屬：鐵（鐵是一種金屬）"),
    ("工具：目的／功能", "前者係達成後者嘅工具或手段，例：羅盤：航海（用羅盤嚟導航）"),
    ("新舊替代（技術升級）", "後者取代前者、功能相同但技術提升，例：傳呼機→移動電話"),
    ("窮盡互斥", "兩者係同一類別下「僅有」嘅 {2} 個選項，例：男／女之於「性別」"),
]
KW_TRAPS = [
    ("表面相似 vs 結構相同", "「戲劇：舞台」表面關聯到「購物：商場」（都係地點），"
                          "但如果原本嘅關係其實係「工具」，就要揀「購物：購物車」"
                          "先啱——要睇比較清楚已知那對嘅關係本質，唔淨係表面聯想"),
    ("部件 vs 類別", "「劍：劍鋒」係部件關係，同「金屬：鐵」嘅類別關係唔同型，"
                     "唔可以將呢兩種關係當做同一種"),
    ("類別要窮盡先叫「窮盡互斥」", "「顏色：黑／白」唔算窮盡互斥，因為顏色仲有好多種；"
                                "「性別：男／女」先算（呢個類別得返兩個值）"),
]

DEMO_STEM = "【範例】羽毛：鋼筆　與　火炬：？\nA．燃燒　B．書寫　C．燈籠　D．火焰"

DEMO_WALK = [
    "第一步：睇清楚已知嗰對「羽毛：鋼筆」係咩關係。「羽毛」係舊式書寫工具（羽毛筆），"
    "俾「鋼筆」呢種功能相同但技術升級嘅工具取代咗——關係類型：新舊替代（技術升級）。",
    "第二步：檢查選項，搵邊個一樣係「火炬」被同功能、升級咗嘅工具取代。",
    "A「燃燒」係火炬嘅動作，唔係另一件工具，剔除。",
    "B「書寫」係動作／用途，唔係工具，剔除。",
    "C「燈籠」係照明工具，功能同火炬一樣（照明），但更方便、更安全——"
    "同「羽毛→鋼筆」嘅「舊工具→升級工具」關係一致。",
    "D「火焰」係火炬產生嘅現象，唔係另一件工具，剔除。",
]

TN = dict(
    main_design="D8 關鍵字對譯（常見詞語關係類型對照表）",
    aux_designs=("D12 自我核對清單",),
    reason=(
        "本課處理題庫 C2 類比推理（12題）、C6 詞語關係（1題）。呢類題目嘅瓶頸唔係"
        "唔識個別詞語嘅意思，而係唔識講出「已知嗰組詞語之間係咩關係」，變成靠"
        "「感覺似唔似」撞答案。D8 關鍵字對譯將常見嘅關係類型（反義、近義、類別：實例、"
        "工具：目的、新舊替代、窮盡互斥）列成對照表，學生見到題目先分類「呢對係邊種"
        "關係」，先去揀「同一種關係」嘅選項；D12 自我核對確保揀答案前有講得出關係"
        "類型，唔係純憑直覺。"),
    density="抽離小班（Tier 2）",
    fading=(
        "關鍵字對譯表：講義範例完整展開 → 練習A/B 題目旁印精簡關係類型表 → "
        "練習C 唔提供，自己回想關係類型。｜"
        "自我核對清單：全程保留（講得出關係類型呢個習慣唔設褪除）。"),
    flows=("F1 師徒制對話四步（追問「呢對詞係咩關係？可以用一句話講出嚟嗎？」）",),
    iep_codes=("a3 提示題目重點", "a6 增加行距", "a8 提供關鍵字對譯表作為長期參考工具"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("題目來源",
            "部分題目改編自題庫真實題目，逐題親自驗算，詳見《驗算_類比與詞語關係.md》。"),
           ("配套文件",
            "《第7章 L20 類比與詞語關係　課堂練習》（練習A／B／C ＋參考答案）、"
            "《工具卡》（關係類型對照表精簡版）。")),
)


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、關鍵字對譯表：常見詞語關係類型"))
    P.append(para("見到類比題，先問自己：已知嗰對詞係邊一種關係？"))
    P.append(keyword_table(KW_GENERAL, KW_TRAPS))

    P.append(heading("三、範例：完整走一次"))
    P.append(problem_box([para(DEMO_STEM)]))
    for t in DEMO_WALK:
        P.append(para(t))
    P.append(shaded_box("答案：C。做呢類題唔係揀「感覺有關」嗰個，"
                        "而係揀「同一種關係類型」嗰個。"))

    P.append(heading("四、做練習前，自己核對一次"))
    P.append(selfcheck_list(["我講得出已知嗰對詞係咩關係類型。",
                            "我逐個選項核對係咪同一種關係，唔係揀「感覺似」嗰個。",
                            "如果表面睇落有兩個選項都似，我有再諗清楚邊個先係"
                            "結構完全一致。"]))

    P.append(heading("五、接下來"))
    P.append(para("請拿出《第7章 L20 類比與詞語關係　課堂練習》，善用關係類型對照表"
                  "完成練習A、練習B、練習C。"))

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
    intro = "".join(f"<div>{_esc(t)}</div>" for t in INTRO)
    walk = "".join(f"<div>{_esc(t)}</div>" for t in DEMO_WALK)

    kw_rows = "".join(f"<tr><td>{_esc(k)}</td><td>{_h(v)}</td></tr>" for k, v in KW_GENERAL)
    kw_rows += '<tr class="trap"><td colspan="2">⚠ 陷阱詞（要想一下，不能直接照字面翻）</td></tr>'
    kw_rows += "".join(f"<tr><td>{_esc(k)}</td><td>{_esc(v)}</td></tr>" for k, v in KW_TRAPS)

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

  <div class="section-h">二、關鍵字對譯表：常見詞語關係類型</div>
  <div>見到類比題，先問自己：已知嗰對詞係邊一種關係？</div>
  <table class="d-tbl kw-table">
    <tr><th>關係類型</th><th>說明／例子</th></tr>
    {kw_rows}
  </table>

  <div class="section-h page-break">三、範例：完整走一次</div>
  <div class="problem">{_esc(DEMO_STEM).replace(chr(10), "<br>")}</div>
  {walk}
  <div class="hint-card">答案：C。做呢類題唔係揀「感覺有關」嗰個，而係揀「同一種關係類型」嗰個。</div>

  <div class="section-h">四、做練習前，自己核對一次</div>
  <div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>
    <div>☐ 我講得出已知嗰對詞係咩關係類型。</div>
    <div>☐ 我逐個選項核對係咪同一種關係，唔係揀「感覺似」嗰個。</div>
    <div>☐ 如果表面睇落有兩個選項都似，我有再諗清楚邊個先係結構完全一致。</div>
  </div>

  <div class="section-h">五、接下來</div>
  <div>請拿出《第7章 L20 類比與詞語關係　課堂練習》，善用關係類型對照表完成練習A、練習B、練習C。</div>

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
