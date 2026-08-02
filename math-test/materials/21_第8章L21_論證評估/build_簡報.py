# -*- coding: utf-8 -*-
"""
第8章 L21 論證評估　資源班教學簡報
主設計：D6 明確教學三階段（我做→我們做→你做）｜輔助設計：D13 弗雷爾模型（支持／削弱／無關）
本課係公職考試「邏輯推理」類型課題（論證評估），核心係判斷一個新選項對
一段論證嘅「結論」係支持、削弱、定係無關——唔係傳統代數/幾何計算。
全份題庫呢個題型只有4題，係全新題型，用D6三階段避免學生喺仲未搞清楚
基本框架就被要求獨立作答。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第8章 語文與邏輯推理(三)．L21 論證評估"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(
    prs,
    subject=SUBJECT,
    unit_title="L21　論證評估",
    mode_label="資源班課堂簡報｜D6 我做→我們做→你做",
    footer_text=FOOTER,
)

# 2. 流程預告
db.add_flow_preview(
    prs, FOOTER, "今日要做嘅4件事",
    [
        "拆解論證：搵結論、搵論據",
        "認識三種關係：支持／削弱／無關",
        "老師示範一題，一齊核對練習A",
        "自己挑戰練習B、C三層任務",
    ],
)

# 3. 問題引入（用講義範例做鉤子）
db.add_question_intro(
    prs, FOOTER, "先估估：邊項最能支持佢？",
    question="超市大減價，賣越多蝕越多，經理仍然堅持要做。邊項最能支持佢嘅決定？",
    options=[
        "薄利多銷有利於提高超市銷售收入",
        "物美價廉嘅商品更受消費者歡迎",
        "擴大知名度對新開幕嘅超市好重要",
    ],
    hint="提示：邊句解釋到『明知蝕本都要做』呢個關鍵？",
)

# 4. CRA三欄：一個共通動作
db.add_cra(
    prs, FOOTER, "一個共通動作：搵結論、搵論據、判選項",
    concrete=dict(
        label="①搵結論",
        desc="結論係：\n經理決定\n堅持促銷\n（明知會\n蝕本）",
    ),
    representational=dict(
        label="②搵論據",
        desc="論據係：\n賣得越多\n蝕得越多\n（題目已\n經話低）",
    ),
    abstract=dict(
        label="③判選項",
        desc="問自己：\n邊個解釋\n到『明知\n蝕都做』？\n答案：C\n擴大知名度\n換長期客源",
    ),
)

# 5. 步驟卡：三種論證關係（弗雷爾模型）
db.add_step_card(
    prs, FOOTER, "三種論證關係（弗雷爾模型）",
    steps=[
        "支持：畀新理由，令結論更可信",
        "削弱：畀相反事實，令結論減可信",
        "無關：睇落有關，其實冇提供理由",
        "訣竅：問『呢句令結論更/更唔可信？』",
    ],
    note="呢張表全程可以睇，唔使死記",
)

# 6. 過渡頁1
db.add_transition(
    prs, "識咗三種關係，\n而家一齊核對第一題。", FOOTER,
)

# 7. 迷思澄清
db.add_misconception(
    prs, FOOTER, "3個常見中招位",
    items=[
        dict(wrong="見到字眼有關就當支持", right="要諗係咪令結論更可信"),
        dict(wrong="淨係揀『聽落最合理』嗰個", right="要逐個排除，講得出點解唔啱"),
        dict(wrong="唔理有冇第二個解釋原因", right="因果題要諗吓混淆變數先落結論"),
    ],
)

# 8. 2x2 視覺鷹架：深堂示範（第二個例子）
db.add_scaffold_2x2(
    prs, FOOTER, "深堂示範：仲有冇第二個解釋？",
    problem="同學話：『尋晚溫書到夜晚兩點，今日測驗實考得好。』",
    what="邊項最\n能削弱\n佢嘅講法？",
    given="結論:測驗\n考得好\n論據:溫到\n夜晚兩點",
    strategy="諗:淨係『溫\n得耐』係咪\n就一定考得好？",
    check="例如:瞓少\n過4粒鐘,\n專注力低,\n屬於削弱",
)

# 9. 步驟卡：自己動手時的動作（取自練習卷自我核對清單）
db.add_step_card(
    prs, FOOTER, "自己動手時嘅4個動作",
    steps=[
        "搵出結論同論據，唔淨係睇印象",
        "逐個選項判斷：支持/削弱/無關",
        "講得出點解其餘選項唔啱先算識",
        "因果題額外問：仲有冇第二個解釋？",
    ],
    note="每題做完，返嚟核對呢張清單先過",
)

# 10. 過渡頁2
db.add_transition(
    prs, "睇完規則\n而家嚟做一條真題", FOOTER,
)

# 11. 練習講解：練習A第1題
db.add_practice_explain(
    prs, FOOTER, "示範：練習A 第1題",
    problem="老闆話：生意升兩成，證明出品更受歡迎。邊項最能削弱？",
    steps=[
        "第一步:搵結論—出品更受歡迎",
        "第二步:搵論據—生意額升兩成",
        "第三步:問—仲有冇第二個解釋？",
        "A.食物全部加價一成——正是解釋",
        "答案:A，削弱(升幅可能只係加價)",
    ],
    note="B、C、D都同『升幅原因』無關，屬無關選項",
)

# 12. 分層任務
db.add_tiered_task(
    prs, FOOTER, "輪到你：練習A／B／C",
    tasks=[
        dict(star=1, label="練習A",
             problem="A電訊:每日\n500MB,唔\n可以儲低。\n邊句廣告\n最啱佢？\n提示:諗『每日』呢點"),
        dict(star=2, label="練習B",
             problem="十字路口工\n程後，事故\n反而增加，\n係咪工程嘅\n錯？提示:諗\n吓仲有咩因素"),
        dict(star=3, label="練習C",
             problem="研究話:咖啡\n因可控制血\n糖，未來可\n取代胰島素\n注射。邊項\n最支持呢個結論？"),
    ],
)

# 13. 總結頁
db.add_summary(
    prs,
    takeaway="見到選項，問自己：呢句令結論更可信、更唔可信，定完全冇關？",
    floor_version="支持=畀新理由；削弱=畀相反事實；無關=睇落有關其實冇理由。",
    footer_text=FOOTER,
)

out_path = os.path.join(os.path.dirname(__file__), "簡報_論證評估_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
