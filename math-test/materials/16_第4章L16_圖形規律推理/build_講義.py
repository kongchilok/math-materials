# -*- coding: utf-8 -*-
"""
第4章 數理邏輯(二)．L16 圖形規律推理 —— 課堂講義 build script
主設計 D5 圖文雙軌對照；輔助 D11 標記對應法。鷹架密度：抽離小班 (Tier 2)。
題庫原稿 B2 圖形規律推理（26題）images 欄位全空、僅有文字描述，且部分解答自承
「未能獨立驗證視覺規律」，經使用者決定：自行重新設計同型全新題（見驗算檔 §0）。
產出：講義_圖形規律推理_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import figs as f                             # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_圖形規律推理_抽離小班共用版"
UNIT = "第4章 數理邏輯(二)．L16 圖形規律推理"
FOOT = "高三數學．第4章 數理邏輯(二)．L16 圖形規律推理"

INTRO = [
    "呢類題目（圖形規律推理）好多同學一睇就有「感覺」，但一叫佢哋講出「點解揀呢個答案」，"
    "就講唔出，變咗靠直覺撞。呢一課嘅做法係逼自己將每一步嘅變化講成一句話——"
    "「由呢格到嗰格，邊度變咗、點樣變」，講得出嚟先揀答案。",
    "睇圖案序列嘅時候，一格一格編號（①②③④），每次只比較相鄰兩格，"
    "唔好一次過睇成串圖案，會眼花。",
]

# ---------------------------------------------------------------- 圖形（D5 示範）
def _demo_panel(n_sides):
    return f.polygon(f.BOX / 2, f.BOX / 2, 40, n_sides)


IMG1 = f.save("demo_1", f.panel_row([(_demo_panel(3), "①", False)]), HERE)
IMG12 = f.save("demo_12", f.panel_row([(_demo_panel(3), "①", False), (_demo_panel(4), "②", False)]), HERE)
IMG123 = f.save("demo_123", f.panel_row(
    [(_demo_panel(3), "①", False), (_demo_panel(4), "②", False), (_demo_panel(5), "③", False)]), HERE)
IMG_Q = f.save("demo_q", f.panel_row([(None, "④", True)]), HERE)
IMG_FULL = f.save("demo_full", f.panel_row(
    [(_demo_panel(3), "①", False), (_demo_panel(4), "②", False),
     (_demo_panel(5), "③", False), (None, "④", True)]), HERE)
IMG_ANS = f.save("demo_ans", f.panel_row(
    [(_demo_panel(3), "①", False), (_demo_panel(4), "②", False),
     (_demo_panel(5), "③", False), (_demo_panel(6), "④", False)]), HERE)

TN = dict(
    main_design="D5 圖文雙軌對照",
    aux_designs=("D11 標記對應法",),
    reason=(
        "本課題源自題庫第4章 B2 圖形規律推理（26題）。題庫原稿該類別 images 欄位全部"
        "為空、只有文字描述圖形，且部分解答自承「圖案解析度不足／未能獨立驗證視覺規律」"
        "——原題無法安全直接印給學生，已徵得使用者同意，本課自行重新設計同型全新題"
        "（保留「圖案序列找規律」呢個題型結構同難度分層，題目本身唔源自題庫）。"
        "呢類題目唔屬於 S1~S10 既有數學結構，真正瓶頸係「睇得出圖但講唔出規律」——"
        "學生可以憑直覺揀啱答案，但講唔出轉變邏輯，換一條類似題就撞唔中。"
        "D5 圖文雙軌逼學生將圖案嘅視覺轉變逐格寫成一句文字描述，唔可以淨係「感覺」；"
        "D11 標記對應（①②③④）將圖入面第幾格同描述入面講緊嘅第幾格扣連，"
        "避免「睇緊呢格、講緊嗰格」錯位。"),
    density="抽離小班（Tier 2）",
    fading=(
        "圖文雙軌表：講義範例四行全部展開，每一步都示範好文字描述 → 練習A 雙軌表只填一半"
        "（圖案已畫好，文字描述欄要學生自己填）→ 練習B 雙軌表得返標題列，兩欄都要自己填 → "
        "練習C 完全唔提供雙軌表，得返圖案序列，規律要由學生自己講出嚟並寫喺作答欄。｜"
        "標記①②③④：全程保留（呢個設計本身唔需要褪除，係固定嘅溝通符號）。"),
    flows=("F5 課前流程預告（今日規則：一次淨係比較相鄰兩格）",),
    iep_codes=("a3 提示題目重點", "a5 放大字體", "a6 增加行距"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("題目來源特別說明",
            "本課全部題目為自編（題庫原稿該類別缺圖，不適合直接使用），"
            "詳見《驗算_圖形規律推理.md》§0。"),
           ("配套文件",
            "《第4章 L16 圖形規律推理　課堂練習》（練習A／B／C ＋參考答案）。本課設計"
            "無需獨立桌面工具卡，雙軌表已內嵌於練習紙。")),
)


# ---------------------------------------------------------------- docx
def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、範例：完整走一次（圖文雙軌對照）"))
    P.append(para("【範例】下面四格圖案有規律，格④應該係咩？"))
    P.append(image_para(IMG_FULL, width_cm=15))

    media = MediaRegistry()
    # 注意：呢度傳純文字字串，唔可以自己先包一層 para()——dual_track_table 內部嘅
    # _as_paras() 會對 str 自動呼叫 para()，先包一次會令段落 XML 被當成純文字再轉義一次
    # （實測踩過：docx 打開變成成版 OOXML 標記碼），仝一個坑喺 build_練習.py 嘅 dt() 已修過。
    rows = [
        (image_para(IMG1, width_cm=4.2), "格①：三角形，3 條邊，空心。"),
        (image_para(IMG12, width_cm=7.2), "由①到②：邊數 3→4，多咗 1 條邊，變咗做四邊形；"
                                          "填色冇變，仍然空心。"),
        (image_para(IMG123, width_cm=10.2), "由②到③：邊數 4→5，再多 1 條邊，變咗五邊形；"
                                            "填色再冇變。"),
        (image_para(IMG_Q, width_cm=4.2), "跟返「邊數每格 +1」嘅規律，格④嘅邊數應該係"
                                          "{5+1=6}，即六邊形；填色跟返前面全部都係空心，"
                                          "所以答案係「空心六邊形」。"),
    ]
    P.append(dual_track_table(rows, media=media, headers=("圖形上發生什麼", "文字描述規律")))
    P.append(para("核對答案："))
    P.append(image_para(IMG_ANS, width_cm=15, caption="格④＝空心六邊形（6 條邊）"))
    P.append(shaded_box("※ 每次淨係比較「上一格」同「呢一格」，寫低邊度變咗（邊數／填色／"
                        "方向……），唔好一次過睇成串圖案。"))

    P.append(heading("三、接下來"))
    P.append(para("請拿出《第4章 L16 圖形規律推理　課堂練習》，用返「一次淨係比較相鄰兩格」"
                  "嘅方法完成練習A、練習B、練習C。練習A 雙軌表已經填咗一半；練習B 雙軌表得返"
                  "標題，兩欄都要自己諗；練習C 完全冇雙軌表，規律要自己講出嚟。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=media)


# ---------------------------------------------------------------- HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _svg_inline(path):
    svg = open(path.replace(".png", ".svg"), encoding="utf-8").read()
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


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

    dual_rows = [
        (_svg_inline(IMG1), "格①：三角形，3 條邊，空心。"),
        (_svg_inline(IMG12), "由①到②：邊數 3→4，多咗 1 條邊，變咗做四邊形；填色冇變，仍然空心。"),
        (_svg_inline(IMG123), "由②到③：邊數 4→5，再多 1 條邊，變咗五邊形；填色再冇變。"),
        (_svg_inline(IMG_Q), "跟返「邊數每格 +1」嘅規律，格④嘅邊數應該係 \\(5+1=6\\)，"
                            "即六邊形；填色跟返前面全部都係空心，所以答案係「空心六邊形」。"),
    ]
    dt_rows = "".join(
        f'<tr><td class="fig">{img}</td><td>{txt}</td></tr>' for img, txt in dual_rows)

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

  <div class="section-h">二、範例：完整走一次（圖文雙軌對照）</div>
  <div class="problem">下面四格圖案有規律，格④應該係咩？</div>
  <div class="fig">{_svg_inline(IMG_FULL)}</div>

  <table class="d-tbl dual-track">
    <tr><th>圖形上發生什麼</th><th>文字描述規律</th></tr>
    {dt_rows}
  </table>

  <div>核對答案：</div>
  <div class="fig">{_svg_inline(IMG_ANS)}<div class="cap">格④＝空心六邊形（6 條邊）</div></div>

  <div class="hint-card">※ 每次淨係比較「上一格」同「呢一格」，寫低邊度變咗（邊數／填色／方向……），唔好一次過睇成串圖案。</div>

  <div class="section-h">三、接下來</div>
  <div>請拿出《第4章 L16 圖形規律推理　課堂練習》，用返「一次淨係比較相鄰兩格」嘅方法完成練習A、練習B、練習C。練習A 雙軌表已經填咗一半；練習B 雙軌表得返標題，兩欄都要自己諗；練習C 完全冇雙軌表，規律要自己講出嚟。</div>

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
