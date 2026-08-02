# -*- coding: utf-8 -*-
"""
第6章 L19 條件邏輯／定義判斷／親屬推理　資源班教學簡報
主設計：D8 關鍵字對譯（邏輯連接詞）｜輔助設計：D11 標記對應法
本課涵蓋三個子主題：條件邏輯（若則／只有才／除非否則／逆否命題）、
定義判斷（逐項要件核對）、親屬推理（由外層一步步代入）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第6章 語文與邏輯推理(一)．L19 條件邏輯／定義判斷／親屬關係"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(
    prs,
    subject=SUBJECT,
    unit_title="L19　條件邏輯・定義判斷・親屬推理",
    mode_label="資源班課堂簡報｜D8 關鍵字對譯法",
    footer_text=FOOTER,
)

# 2. 流程預告
db.add_flow_preview(
    prs, FOOTER, "今日要做嘅4件事",
    [
        "拆解條件句：畫箭嘴、認陷阱詞",
        "定義判斷：逐項核對「要件」",
        "親屬關係：由外層一步步代入",
        "動手做：練習A、B、C三層任務",
    ],
)

# 3. 問題引入（用講義範例的邏輯鏈作鉤子）
db.add_question_intro(
    prs, FOOTER, "先估估：呢個結論啱唔啱？",
    question="犯法→受制裁→被睇唔起→唔受尊重；只有受尊重，先至舒心。邊個結論一定啱？",
    options=[
        "你不犯法，日子就會過得舒心。",
        "你犯了法，日子就不會過得舒心。",
        "你日子過得不舒心，證明你犯了法。",
    ],
    hint="提示：第4句係「只有…才…」，要調轉先可以連落去。",
)

# 4. 三主題總覽（CRA 借用三欄呈現）
db.add_cra(
    prs, FOOTER, "三種題型，一個共通動作：轉符號",
    concrete=dict(
        label="條件邏輯",
        desc="若P則Q\n寫成P→Q\n只有P才Q\n主客要調轉\n除非P否則Q\n要接否定\n逆否命題\n先可以用",
    ),
    representational=dict(
        label="定義判斷",
        desc="定義拆件\n編號①②③④\n四個選項\n逐項核對\n漏一項\n就不算\n全部符合\n先算啱",
    ),
    abstract=dict(
        label="親屬推理",
        desc="由外層開始\n一步步代入\n先搞清\n呢個人係邊個\n再問佢嘅\n某某係邊個\n唔好一次\n跳幾層",
    ),
)

# 5. 步驟卡：核心規則
db.add_step_card(
    prs, FOOTER, "關鍵字對譯規則（背呢6條）",
    steps=[
        "若P則Q、只要P就Q → 寫成P→Q",
        "只有P才Q → Q→P（主客詞調轉）",
        "除非P否則Q → ¬P→Q（要接否定）",
        "逆命題唔等價，逆否命題先等價",
        "定義題：逐項要件核對，唔漏一項",
        "親屬題：由外層開始，一步步代入",
    ],
    note="呢張表全程可以睇，唔使死記",
)

# 6. 過渡頁1
db.add_transition(
    prs, "呢啲規則入面\n有幾條陷阱最易中招", FOOTER,
)

# 7. 迷思澄清（三個子主題各一組）
db.add_misconception(
    prs, FOOTER, "3個常見中招位",
    items=[
        dict(wrong="以為逆命題同原命題一樣啱", right="逆否命題¬Q→¬P先同原命題等價"),
        dict(wrong="見到一兩項符合就快手選咗", right="要逐項核對晒全部要件先算啱"),
        dict(wrong="一次過睇成句，唔知邊個係邊個", right="由外層開始，一步步代入先搞清"),
    ],
)

# 8. 2x2 視覺鷹架：深堂示範（換條件邏輯的等價判斷子主題）
db.add_scaffold_2x2(
    prs, FOOTER, "深堂示範：判斷邊句意思相同",
    problem="「如果太陽毀滅，就有外星人」邊個選項意思相同？",
    what="邊個選項\n同原句\n意思相等？",
    given="原句：P→Q\n(P=太陽毀滅\nQ=有外星人)",
    strategy="P→Q 恆等於\n「¬P 或 Q」\n即「唔毀滅\n或有外星人」",
    check="對應選項C\nA係逆命題\n(唔等價)　答案：C",
)

# 9. 步驟卡：自己動手時的動作（取自練習卷自我核對清單）
db.add_step_card(
    prs, FOOTER, "自己動手時嘅4個動作",
    steps=[
        "條件句：翻譯做符號，唔淨係讀字面",
        "定義題：逐項要件核對，冇漏一項",
        "親屬題：由外層一步步代入，唔跳層",
        "答案代返去題目，檢查一次啱唔啱",
    ],
    note="唔記得？睇返《工具卡》關鍵字對譯精簡版",
)

# 10. 過渡頁2
db.add_transition(
    prs, "睇完規則\n而家嚟做一條真題", FOOTER,
)

# 11. 練習講解：練習A第1題
db.add_practice_explain(
    prs, FOOTER, "示範：練習A 第1題",
    problem="1．若①所有樹都會開花、②某些樹是山茱萸，③『所有山茱萸都會開花』岩唔岩？",
    steps=[
        "②話：山茱萸屬於「樹」呢類",
        "①話：樹→會開花（所有樹都係）",
        "串連：山茱萸→樹→會開花",
        "所以③「山茱萸都會開花」為真",
        "答案：A．真的",
    ],
    note="易錯點：「某些」≠「所有」，但唔影響呢個結論",
)

# 12. 分層任務（三個子主題各一題）
db.add_tiered_task(
    prs, FOOTER, "輪到你：練習A／B／C",
    tasks=[
        dict(star=1, label="練習A", problem="2．女士話：「佢嘅母親係\n我母親嘅獨生女」。\n呢名女士係甲嘅\n乜關係？\nA母親 B妹妹\nC女兒 D姨媽"),
        dict(star=2, label="練習B", problem="4．『政策性虧損』：因國家\n限價虧損＋財政部門\n審核後補償。邊個\n糧食企業例子啱？\n（逐項核對要件）"),
        dict(star=3, label="練習C", problem="5．①只有律師先可以\n申請甲卡②凡律師都\n可入法院。邊個結論\n必然成立？"),
    ],
)

# 13. 總結頁
db.add_summary(
    prs,
    takeaway="見到固定句式，即刻翻譯做符號——先睇得出結構，先識得推理。",
    floor_version="只有…才…、除非…否則、逆否命題——三個詞記住，考試已經贏一半。",
    footer_text=FOOTER,
)

out_path = os.path.join(os.path.dirname(__file__), "簡報_條件邏輯定義親屬推理_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
