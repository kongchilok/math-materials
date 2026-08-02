# -*- coding: utf-8 -*-
"""
第6章 語文與邏輯推理(一)．L18 命題排列邏輯 —— 課堂講義 build script
（本課處理 C1 命題邏輯嘅「排列組合式邏輯謎題」子結構——人物名次/座位/顏色屋等，
 條件式命題邏輯(若P則Q一類)另立 L19 處理，見教學進度表分課說明。）
主設計 D9 草稿分區卡（排位工作區）；輔助 D12 自我核對清單。鷹架密度：抽離小班 (Tier 2)。
題目多數改編自題庫 C1 命題邏輯（排列子類），逐題親自驗算，見驗算檔。
產出：講義_命題排列邏輯_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_命題排列邏輯_抽離小班共用版"
UNIT = "第6章 語文與邏輯推理(一)．L18 命題排列邏輯"
FOOT = "高三數學．第6章 語文與邏輯推理(一)．L18 命題排列邏輯"

INTRO = [
    "呢類題目（邊個排第幾、邊個坐邊度、邊間屋係咩顏色）唔難喺「計算」，難喺「多個條件"
    "同時要記住」——讀完第3個條件，已經唔記得返第1個講咩，要由頭讀多次。",
    "呢一課嘅方法係唔靠腦記，靠「排位工作區」：讀一個條件，即刻喺工作區度畫低／寫低，"
    "讀晒所有條件先至一次過睇晒個排位圖，唔使成個腦記住晒。",
]

WORKSPACE_LABELS = ("第1(最快)", "第2", "第3", "第4", "第5(最慢)",
                    "檢查：5個條件全部用咗未？")

DEMO_CLUES = [
    "① 小明贏咗小華。",
    "② 小芳贏咗小明，但輸咗小強。",
    "③ 小強輸畀小玲。",
]

DEMO_WALK = [
    "條件①：小明 > 小華（用「>」表示名次較前）。工作區暫時寫：小明－小華（小明喺前）。",
    "條件②：小芳 > 小明，同時小強 > 小芳。將呢兩個關係接落去原本嘅鏈："
    "小強 > 小芳 > 小明 > 小華。",
    "條件③：小玲 > 小強。接埋去鏈嘅最前面：小玲 > 小強 > 小芳 > 小明 > 小華。",
    "五個人嘅名次已經全部連成一條鏈——5個人之間有 {5-1=4} 個「>」關係，"
    "冇缺位、冇矛盾，可以直接讀出排位：",
]

SELFCHECK = ["每一個條件我都喺工作區度記低咗，冇淨係喺腦入面諗。",
             "五個（或幾個）人嘅名次連成一條鏈，冇兩個人卡住定唔到邊個前邊個後。",
             "我讀返晒全部條件，一個都冇漏用。",
             "答案代返去逐個條件檢查，全部條件都仍然成立。"]

TN = dict(
    main_design="D9 草稿分區卡（排位工作區）",
    aux_designs=("D12 自我核對清單",),
    reason=(
        "本課處理題庫 C1 命題邏輯入面嘅「排列組合式邏輯謎題」子結構（人物名次、座位、"
        "顏色屋等），同 C1 入面另一種「條件式命題推理」（若P則Q）性質完全不同——"
        "後者另立 L19 處理。呢類排列謎題嘅瓶頸係工作記憶負荷：條件通常有3至5個，"
        "讀到後面已經唔記得前面，唔係唔識邏輯推理本身。D9 草稿分區卡將「排位」"
        "呢個過程外部化——讀一個條件就即刻寫落工作區，唔使淨係靠腦記住成串條件，"
        "讀晒先一次過睇晒個結果；D12 自我核對確保學生冇漏用任何一個條件、"
        "答案有代返去驗證。"),
    density="抽離小班（Tier 2）",
    fading=(
        "草稿分區：講義範例完整示範點樣逐條件填工作區 → 練習A/B 印有工作區格仔，"
        "跟住填 → 練習C 唔提供工作區格仔，自己喺白紙度畫。｜"
        "自我核對清單：全程保留（確保條件冇漏用嘅習慣，唔設褪除）。"),
    flows=("F2 番茄鐘分段（一個條件一次停頓，寫低先再讀下一個）",),
    iep_codes=("a3 提示題目重點", "a6 增加行距", "a7 調整計分標準（分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("題目來源",
            "部分題目改編自題庫 C1 命題邏輯（排列子結構），部分為結構相同之自編題，"
            "逐題親自驗算，詳見《驗算_命題排列邏輯.md》。"),
           ("配套文件",
            "《第6章 L18 命題排列邏輯　課堂練習》（練習A／B／C ＋參考答案）。")),
)


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、範例：完整走一次（排位工作區）"))
    P.append(problem_box([para(
        "【範例】小明、小華、小芳、小強、小玲五人測驗，名次無並列。已知：")] +
        [para(t) for t in DEMO_CLUES] +
        [para("邊個排第三（由高至低計）？")]))

    for t in DEMO_WALK[:-1]:
        P.append(para(t))
    P.append(para(DEMO_WALK[-1]))
    P.append(quadrant_workspace(WORKSPACE_LABELS, cell_h=1100))
    P.append(shaded_box("答案：由高至低 小玲、小強、小芳、小明、小華——排第三嘅係「小芳」。"))
    P.append(para("覆核：條件①小明>小華 ✓；條件②小芳>小明 ✓ 且 小強>小芳 ✓；"
                  "條件③小玲>小強 ✓。全部條件仍然成立，答案確定。"))

    P.append(heading("三、做練習前，自己核對一次"))
    P.append(selfcheck_list(SELFCHECK))

    P.append(heading("四、接下來"))
    P.append(para("請拿出《第6章 L18 命題排列邏輯　課堂練習》，用返「讀一條、填一格」"
                  "嘅方法完成練習A、練習B、練習C。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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
    clues = "".join(f"<div>{_esc(t)}</div>" for t in DEMO_CLUES)
    walk = "".join(f"<div>{_h(t)}</div>" for t in DEMO_WALK)
    chk = "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK)

    def _quadrant_html(labels):
        rows = ""
        for i in range(0, len(labels), 2):
            pair = labels[i:i + 2]
            cells = "".join(f'<td><div class="qlabel">{_esc(l)}</div></td>' for l in pair)
            rows += f"<tr>{cells}</tr>"
        return f'<table class="d-tbl quadrant">{rows}</table>'

    ws_table = _quadrant_html(WORKSPACE_LABELS)

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

  <div class="section-h">二、範例：完整走一次（排位工作區）</div>
  <div class="problem">
    <div>【範例】小明、小華、小芳、小強、小玲五人測驗，名次無並列。已知：</div>
    {clues}
    <div>邊個排第三（由高至低計）？</div>
  </div>
  {walk}
  {ws_table}
  <div class="hint-card">答案：由高至低 小玲、小強、小芳、小明、小華——排第三嘅係「小芳」。</div>
  <div>覆核：條件①小明&gt;小華 ✓；條件②小芳&gt;小明 ✓ 且 小強&gt;小芳 ✓；條件③小玲&gt;小強 ✓。全部條件仍然成立，答案確定。</div>

  <div class="section-h">三、做練習前，自己核對一次</div>
  <div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>{chk}</div>

  <div class="section-h">四、接下來</div>
  <div>請拿出《第6章 L18 命題排列邏輯　課堂練習》，用返「讀一條、填一格」嘅方法完成練習A、練習B、練習C。</div>

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
