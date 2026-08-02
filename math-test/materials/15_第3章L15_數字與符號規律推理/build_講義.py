# -*- coding: utf-8 -*-
"""
第3章 數理邏輯(一)．L15 數字與符號規律推理 —— 課堂講義 build script
主設計 D2 手順卡（規律偵測四步）；輔助 D12 自我核對清單。鷹架密度：抽離小班 (Tier 2)。
題型不屬 teaching-designs.md 既有 S1-S10 數學結構——瓶頸是「規律歸納」而非代數/幾何轉換，
教學設計依 CLAUDE.md 融合班講義流程步驟2.5另行判斷（見教師實施說明的「選用理由」）。
產出：講義_數字與符號規律推理_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_數字與符號規律推理_抽離小班共用版"
UNIT = "第3章 數理邏輯(一)．L15 數字與符號規律推理"
FOOT = "高三數學．第3章 數理邏輯(一)．L15 數字與符號規律推理"

# ---------------------------------------------------------------- 文字內容
INTRO = [
    "呢一類題目（數列填空、符號規律、排序、分類）睇落好唔同，但卡住嘅位其實只有一個："
    "唔知由邊度開始試。見到一串數字，好多人亂咁試，試唔啱就放棄，或者靠估。",
    "呢一課用嘅方法係「規律偵測四步」：唔係一睇就要診出規律，而係跟住固定次序逐步試"
    "（相鄰關係 → 分組 → 假設 → 驗證），試唔啱就返上一步換第二個假設，唔係亂咁試。",
]

STEPS = [
    ("抄一次已知數字，依原順序排好，方便標記邊個位置係空格。",
     "抄漏一個字或抄錯次序，後面全部白費"),
    ("試「相鄰項」關係：後一項減前一項？除以前一項？有冇平方／立方關係？",
     "淨係試加減、唔試乘除同次方，會漏咗好多規律"),
    ("相鄰關係唔明顯，就試「分組」：可以係隔一個分兩組（單數位、雙數位），"
     "或者連續幾個分一組（例如三個一組睇組內關係）。",
     "見到唔止一條規律先諗分組，唔係一開始就分；兩種分組法都要試過先可以放棄"),
    ("揀一個假設，代返去驗證晒全部已知數字，唔係得一兩個岩就收貨；"
     "全部啱先計空格嘅答案，唔啱就返步驟2、3換過假設。",
     "只驗證咗頭一兩個數字就落結論，尾嗰幾個冇對過"),
]

EXAMPLE_STEM = "【範例】27　8　1　9　＿＿＿　1　3　1，求空格數字。"

WALKTHROUGH = [
    "步驟1　抄一次：27, 8, 1, 9, ?, 1, 3, 1（空格在第 5 個位置）。",
    "步驟2　試相鄰關係：27 到 8、8 到 1 都唔係固定嘅加減或乘除，相鄰法行唔通，轉步驟3。",
    "步驟3　試「連續幾個一組」，每 3 個分一組：第一組 (27, 8, 1)、第二組 (9, ?, 1)、"
    "第三組 (3, 1)（數列到呢度完結，得返兩個）。留意第一組啱啱好係 3、2、1 嘅立方："
    "{3^3=27}、{2^3=8}、{1^3=1}。",
    "步驟4　用同一套「3、2、1」試第二組，估係平方：{3^2=9}（對應第 1 個位，✓）、"
    "{2^2=?}、{1^2=1}（對應第 3 個位，✓）。兩個已知位都啱，所以 ? ＝ {2^2=4}。",
    "覆核　第三組 (3, 1) 應該係 3、2、1 嘅一次方：{3^1=3}（✓）、{1^1=1}（✓，中間嘅 "
    "{2^1=2} 因為數列到呢度完結而冇出現）。全部已知位都對得上，答案確定為 4。",
]

SELFCHECK = [
    "我試過相鄰項嘅加、減、乘、除、平方、立方。",
    "我試過「隔一個分兩組」同「連續幾個一組」兩種分組法。",
    "我嘅假設代返去，全部已知數字都啱，唔係得一兩個岩。",
    "答案有揀返對應嘅選項（唔係淨係計出個數）。",
]

TN = dict(
    main_design="D2 手順卡（規律偵測四步）",
    aux_designs=("D12 自我核對清單",),
    reason=(
        "本課題源自題庫第3章數字與符號規律類（B1數字規律推理41題、B4文字符號規律推理4題、"
        "B5常識性排序3題、B7分類歸納推理4題）。呢批題型唔屬於 teaching-designs.md 既有嘅 "
        "S1~S10 數學結構（果啲係代數/幾何嘅結構轉換瓶頸）——真正嘅瓶頸係「規律歸納」："
        "學生唔係唔識加減乘除，而係唔知由邊度開始試、試極唔啱就放棄。D2 手順卡將「偵測規律」"
        "呢個含糊嘅動作拆做四個具體步驟（相鄰→分組→假設→驗證），令學生有固定程序可以跟，"
        "唔使靠直覺；D12 自我核對清單確保學生驗證咗全部已知項先落答案，唔係揀啱一半就收工。"),
    density="抽離小班（Tier 2）",
    fading=(
        "手順卡：講義範例四步全寫出並示範 → 練習A 手順卡精簡版印喺題目旁（compact，"
        "只有步驟無易錯點）→ 練習B 手順卡只印喺工具卡、題目唔再附 → 練習C 完全唔提供手順卡，"
        "淨係喺自我核對清單度提示「你用咗邊種分組方法？」。｜"
        "自我核對清單：全程保留（呢個設計本身唔需要褪除，係長期習慣）。"),
    flows=("F5 課前流程預告（今日四件事：手順卡 → 範例 → 練習A → 自己核對）",),
    iep_codes=("a3 提示題目重點", "a6 增加行距", "a7 調整計分標準（分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度。"),
           ("配套文件",
            "《第3章 L15 數字與符號規律推理　課堂練習》（練習A／B／C ＋參考答案）、"
            "《第3章 L15 數字與符號規律推理　工具卡》（規律偵測四步卡，學生剪下護貝放桌面）。")),
)


# ---------------------------------------------------------------- docx
def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、規律偵測手順卡"))
    P.append(step_card("規律偵測四步", STEPS,
                       trigger="見到一串數字，中間有一個空格要填嘅時候",
                       fading="第2課起手順卡改精簡版、第3課起只喺工具卡出現、第4課完全唔提供"))

    P.append(heading("三、範例：完整走一次"))
    P.append(problem_box([para(EXAMPLE_STEM)]))
    for t in WALKTHROUGH:
        P.append(para(t))
    P.append(shaded_box("※ 「連續幾個一組」同「隔一個分兩組」係兩種唔同嘅分組法，"
                        "睇題目形狀先決定試邊種——條數列有規律咁重複出現，多數係連續分組；"
                        "睇落好似有兩條交錯嘅規律，先試隔一個分組。"))

    P.append(heading("四、做練習前，自己核對一次"))
    P.append(selfcheck_list(SELFCHECK))

    P.append(heading("五、接下來"))
    P.append(para("請拿出《第3章 L15 數字與符號規律推理　課堂練習》，跟返上面四個步驟完成"
                  "練習A、練習B、練習C。練習A 手順卡仍然印喺題目旁；練習B 起手順卡要自己"
                  "睇工具卡；練習C 完全唔提供手順卡。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ---------------------------------------------------------------- HTML
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
    return "".join(out)


def build_html_file():
    steps_html = "".join(
        f'<tr><td>{i}. {_esc(act)}</td><td>※ {_esc(pit)}</td></tr>'
        for i, (act, pit) in enumerate(STEPS, 1))
    intro = "".join(f"<div>{_h(t)}</div>" for t in INTRO)
    walk = "".join(f"<div>{_h(t)}</div>" for t in WALKTHROUGH)
    chk = "".join(f"<div>☐ {_esc(t)}</div>" for t in SELFCHECK)

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join(f"<tr><td>{_esc(k)}</td><td>{_esc(v)}</td></tr>" for k, v in tn_rows)

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

  <div class="section-h">二、規律偵測手順卡</div>
  <div class="step-card">
    <div style="font-weight:700">規律偵測四步</div>
    <div>什麼時候用：見到一串數字，中間有一個空格要填嘅時候</div>
    <table class="d-tbl">{steps_html}</table>
  </div>

  <div class="section-h">三、範例：完整走一次</div>
  <div class="problem">{_h(EXAMPLE_STEM)}</div>
  {walk}
  <div class="hint-card">※ 「連續幾個一組」同「隔一個分兩組」係兩種唔同嘅分組法，睇題目形狀先決定試邊種——條數列有規律咁重複出現，多數係連續分組；睇落好似有兩條交錯嘅規律，先試隔一個分組。</div>

  <div class="section-h">四、做練習前，自己核對一次</div>
  <div class="selfcheck"><div style="font-weight:700">做完先自己核對一次</div>{chk}</div>

  <div class="section-h">五、接下來</div>
  <div>請拿出《第3章 L15 數字與符號規律推理　課堂練習》，跟返上面四個步驟完成練習A、練習B、練習C。練習A 手順卡仍然印喺題目旁；練習B 起手順卡要自己睇工具卡；練習C 完全唔提供手順卡。</div>

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
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_docx_file())
    print(build_html_file())
