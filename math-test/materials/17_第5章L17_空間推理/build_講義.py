# -*- coding: utf-8 -*-
"""
第5章 數理邏輯(三)．L17 空間推理 —— 課堂講義 build script
主設計 D7 提示卡（相對面法則、翻滾方向法則）；輔助 D5 圖文雙軌對照。鷹架密度：抽離小班 (Tier 2)。
題庫原稿 B3 空間摺紙推理／B6 立體旋轉推理（合共3題）images 欄位全空，且部分解答自承
「圖案解析度不足、未能獨立驗證視覺規律」，經使用者決定：自行重新設計同型全新題（見驗算檔 §0）。
產出：講義_空間推理_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import figs as f                             # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_空間推理_抽離小班共用版"
UNIT = "第5章 數理邏輯(三)．L17 空間推理"
FOOT = "高三數學．第5章 數理邏輯(三)．L17 空間推理"

INTRO = [
    "呢類題目（摺紙、正方體旋轉）唔靠死背，靠兩條「口訣」：一條處理「展開圖摺成正方體，"
    "邊兩個面相對」；另一條處理「正方體向邊度滾一下，頂面變咗邊個」。呢一課淨係得3題原題，"
    "但呢兩條口訣識用，同類型題目點變化都應付到。",
    "兩條口訣都寫喺提示卡，做練習嗰陣隨時可以翻返去對，唔使死記。",
]

media = MediaRegistry()

# ---------------------------------------------------------------- 圖形
NET_CELLS = {(0, 1): "頂B", (1, 0): "左A", (1, 1): "前C", (1, 2): "右D",
             (1, 3): "後E", (2, 1): "底F"}
NET_IMG = f.save("net_demo", f.net_grid(NET_CELLS, highlight={(1, 1)}), HERE)
NET_IMG_CE = f.save("net_demo_ce", f.net_grid(NET_CELLS, highlight={(1, 1), (1, 3)}), HERE)


TN = dict(
    main_design="D7 提示卡（相對面法則、翻滾方向法則）",
    aux_designs=("D5 圖文雙軌對照",),
    reason=(
        "本課題源自題庫第5章 B3 空間摺紙推理（2題）、B6 立體旋轉推理（1題），合共僅3題，"
        "屬全課題庫題量最少的一課。原稿 images 欄位全空、部分解答自承「未能獨立驗證視覺"
        "規律」，經使用者同意，本課自行重新設計同型全新題（詳見驗算檔 §0）。"
        "呢類題目嘅瓶頸唔係計算，而係「空間心像操作」——學生要喺腦入面摺紙或者轉正方體，"
        "呢個對好多學生（尤其空間能力較弱者）認知負荷極高。D7 提示卡將兩條可以直接查閱、"
        "毋須每次重新腦內模擬嘅「法則」白紙黑字寫低（相對面：同一直線相隔一格；"
        "翻滾：四個方向各自嘅頂/左/右/底/前/後對應表），學生做題時查卡代替腦內旋轉；"
        "D5 圖文雙軌逼學生將圖上嘅位置關係，同法則嘅文字推理逐步對照寫低，"
        "避免「睇個圖有感覺」但講唔出點推論。"),
    density="抽離小班（Tier 2）",
    fading=(
        "提示卡：兩張卡全程可查閱，本課題量極少（3題），唔設褪除——空間心像操作本身"
        "認知負荷高，屬於「長期可用嘅外部記憶輔助」而非需要拿走嘅暫時鷹架"
        "（同D2手順卡呢類「操作步驟」唔同性質）。｜"
        "圖文雙軌：講義範例全部展開 → 練習A/B 保留簡化版雙軌表 → 練習C 只給圖，"
        "推理步驟自己寫喺作答欄。"),
    flows=("F1 師徒制對話四步（追問「呢個面同嗰個面之間隔幾多格？」）",),
    iep_codes=("a3 提示題目重點", "a6 增加行距", "b5 容許使用實物（如紙盒／骰子）輔助操作"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("題目來源特別說明",
            "本課全部題目為自編（題庫原稿該類別缺圖，詳見《驗算_空間推理.md》§0）。"),
           ("配套文件",
            "《第5章 L17 空間推理　課堂練習》（練習A／B／C ＋參考答案）。"
            "建議課室準備實物紙盒／骰子，容許學生實際摺／轉來核對答案。")),
)


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、提示卡①：相對面法則"))
    P.append(reference_card(
        "相對面法則", "題目畀你睇「展開圖」，問摺成正方體之後邊兩個面相對",
        "喺展開圖入面，兩個方格如果喺同一條直線（橫排或直排）上、中間恰好相隔一格，"
        "摺成正方體之後呢兩個面就係相對面。",
        formula="例：橫排 A－C－D－E 對應位置 1,2,3,4。A(位1)同D(位3)位置差{3-1=2}→相對；"
                "C(位2)同E(位4)位置差{4-2=2}→相對。"))

    P.append(heading("三、提示卡②：翻滾方向法則"))
    P.append(shaded_box("正方體攤平喺桌面，頂／前／右／左／後／底六個面已經固定。"
                        "向某個方向「滾一下」（打側轉 90°），四個面會循環轉位，"
                        "垂直於滾動方向嘅兩個面（例如向右滾時嘅前／後）保持不變："))
    P.append(three_column_table([
        (["向右滾"], ["頂→右，右→底，底→左，左→頂"], ["（前／後不變）"]),
        (["向左滾"], ["頂→左，左→底，底→右，右→頂"], ["（前／後不變）"]),
        (["向前滾"], ["頂→前，前→底，底→後，後→頂"], ["（左／右不變）"]),
        (["向後滾"], ["頂→後，後→底，底→前，前→頂"], ["（左／右不變）"]),
    ], headers=("方向", "面嘅循環", "備註")))

    P.append(heading("四、範例：完整走一次（圖文雙軌對照）"))
    P.append(problem_box([para(
        "【範例】下面係一個十字形展開圖，六個面分別標住「頂B」「左A」「前C」「右D」"
        "「後E」「底F」。摺成正方體之後，邊個面同「前C」相對？")]))
    rows = [
        (image_para(NET_IMG, width_cm=9.0),
         "「前C」喺橫排 A－C－D－E 之中，係第 2 個位。"),
        (image_para(NET_IMG_CE, width_cm=9.0),
         "跟返相對面法則：橫排入面相隔一格嘅兩格係相對面。第 2 位（C）同第 4 位（E）"
         "之間隔咗一格（D），所以 C 同 E 相對。"),
    ]
    P.append(dual_track_table(rows, media=media, headers=("圖形上發生什麼", "推理")))
    P.append(shaded_box("核對答案：「前C」同「後E」相對。（呢個結果同物理常識一致——"
                        "前面同後面本來就係相對面。）"))

    P.append(heading("五、範例：翻滾方向"))
    P.append(problem_box([para(
        "承上題個正方體：頂＝B、前＝C、右＝D、左＝A、後＝E、底＝F。"
        "如果將個正方體向右滾一下，新嘅頂面係邊個？")]))
    P.append(para("查提示卡②「向右滾」一行：頂→右，右→底，底→左，左→頂。"))
    P.append(para("留意規律嘅方向：「左→頂」即係話，原本喺左邊嘅面，滾完之後變咗做頂面。"))
    P.append(para("原本嘅左面係 A，所以新嘅頂面係 A。"))
    P.append(shaded_box("答案：新嘅頂面係 A。"))

    P.append(heading("六、接下來"))
    P.append(para("請拿出《第5章 L17 空間推理　課堂練習》，善用兩張提示卡完成"
                  "練習A、練習B、練習C。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=media)


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

    roll_rows = "".join(
        f"<tr><td>{d}</td><td>{c}</td><td>{n}</td></tr>" for d, c, n in (
            ("向右滾", "頂→右，右→底，底→左，左→頂", "（前／後不變）"),
            ("向左滾", "頂→左，左→底，底→右，右→頂", "（前／後不變）"),
            ("向前滾", "頂→前，前→底，底→後，後→頂", "（左／右不變）"),
            ("向後滾", "頂→後，後→底，底→前，前→頂", "（左／右不變）")))

    dt_rows = "".join(
        f'<tr><td class="fig">{img}</td><td>{txt}</td></tr>' for img, txt in (
            (_svg_inline(NET_IMG), "「前C」喺橫排 A－C－D－E 之中，係第 2 個位。"),
            (_svg_inline(NET_IMG_CE), "跟返相對面法則：橫排入面相隔一格嘅兩格係相對面。"
                                     "第 2 位（C）同第 4 位（E）之間隔咗一格（D），"
                                     "所以 C 同 E 相對。")))

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

  <div class="section-h">二、提示卡①：相對面法則</div>
  <div class="ref-card">
    <div style="font-weight:700">▍相對面法則</div>
    <div>什麼時候翻我：題目畀你睇「展開圖」，問摺成正方體之後邊兩個面相對</div>
    <div>喺展開圖入面，兩個方格如果喺同一條直線（橫排或直排）上、中間恰好相隔一格，摺成正方體之後呢兩個面就係相對面。</div>
    <div>例：橫排 A－C－D－E 對應位置 1,2,3,4。A(位1)同D(位3)位置差 3−1＝2→相對；C(位2)同E(位4)位置差 4−2＝2→相對。</div>
  </div>

  <div class="section-h">三、提示卡②：翻滾方向法則</div>
  <div class="hint-card">正方體攤平喺桌面，頂／前／右／左／後／底六個面已經固定。向某個方向「滾一下」（打側轉 90°），四個面會循環轉位，垂直於滾動方向嘅兩個面保持不變：</div>
  <table class="d-tbl three-col">
    <tr><th>方向</th><th>面嘅循環</th><th>備註</th></tr>
    {roll_rows}
  </table>

  <div class="section-h">四、範例：完整走一次（圖文雙軌對照）</div>
  <div class="problem">【範例】下面係一個十字形展開圖，六個面分別標住「頂B」「左A」「前C」「右D」「後E」「底F」。摺成正方體之後，邊個面同「前C」相對？</div>
  <table class="d-tbl dual-track">
    <tr><th>圖形上發生什麼</th><th>推理</th></tr>
    {dt_rows}
  </table>
  <div class="hint-card">核對答案：「前C」同「後E」相對。（呢個結果同物理常識一致——前面同後面本來就係相對面。）</div>

  <div class="section-h">五、範例：翻滾方向</div>
  <div class="problem">承上題個正方體：頂＝B、前＝C、右＝D、左＝A、後＝E、底＝F。如果將個正方體向右滾一下，新嘅頂面係邊個？</div>
  <div>查提示卡②「向右滾」一行：頂→右，右→底，底→左，左→頂。</div>
  <div>留意規律嘅方向：「左→頂」即係話，原本喺左邊嘅面，滾完之後變咗做頂面。</div>
  <div>原本嘅左面係 A，所以新嘅頂面係 A。</div>
  <div class="hint-card">答案：新嘅頂面係 A。</div>

  <div class="section-h">六、接下來</div>
  <div>請拿出《第5章 L17 空間推理　課堂練習》，善用兩張提示卡完成練習A、練習B、練習C。</div>

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
