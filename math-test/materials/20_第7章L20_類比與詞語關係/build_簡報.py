# -*- coding: utf-8 -*-
"""資源班簡報：第7章 L20 類比與詞語關係。主設計 D8 關鍵字對譯（常見詞語關係類型
對照表）＋輔助 D12 自我核對清單。呢一課係語文推理類型（類比推理、詞語關係），
瓶頸唔係唔識個別詞語嘅意思，而係唔識講出「已知嗰對詞係咩關係」，淨係靠
「感覺似唔似」撞答案。簡報用同一張關鍵字對譯表貫穿全課，兩個完整範例
（物件類比／雙空格配對）示範點樣「先分類關係，後核對答案」；鷹架沿褪除
路徑遞減（練習A題目旁有精簡對照表，B／C唔再附）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第7章 語文與邏輯推理(二)．L20 類比與詞語關係"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "類比與詞語關係", "資源班課堂教學．先辨關係，後選答案", FOOTER)

# 2. 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "先想一想：一條類比題考起你",
    "認識關鍵字對譯表：六種關係類型",
    "範例完整走一次：先辨關係、後核對",
    "換你做：練習A／B／C，鷹架逐層減",
])

# 3. 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "醫生：病人　與　老師：？",
    ["醫院", "學生", "課本"],
    "提示：醫生嘅工作對象係病人；老師嘅工作對象係邊個？")

# 4. CRA①：完整範例（羽毛：鋼筆／火炬：？——講義原本範例）
db.add_cra(prs, FOOTER, "範例完整走一次：羽毛：鋼筆／火炬：？",
    concrete={"label": "①先睇已知對", "desc": "羽毛：鋼筆\n羽毛係舊式\n書寫工具，\n鋼筆功能相同\n但技術升級"},
    representational={"label": "②逐項核對選項", "desc": "A燃燒＝動作\n剔除\nB書寫＝用途\n剔除\nC燈籠＝升級\n照明工具\nD火焰＝現象\n剔除"},
    abstract={"label": "③確認同一關係", "desc": "火炬（舊）→\n燈籠（新）\n都係新舊\n替代關係\n答案：C"})

# 5. 步驟卡：詞語關係類型分類
db.add_step_card(prs, FOOTER, "常見詞語關係類型", [
    "反義：意思相反，例如黑↔白",
    "近義：意思相似，例如建造≈建設",
    "類別：實例，大類與其中一個例子",
    "工具：目的，用嚟做咩、達成咩",
    "新舊替代／窮盡互斥：升級取代或僅得兩值",
], note="見到『感覺似』唔算，要講得出邊一種關係")

# 6. 過渡頁
db.add_transition(prs, "接下來，拆解\n最常見嘅撞板位", FOOTER)

# 7. 迷思澄清
db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "睇到都係『地點』就當同關係", "right": "要睇清關係本質，唔淨睇表面聯想"},
    {"wrong": "『劍：劍鋒』當『金屬：鐵』同型", "right": "部件關係同類別關係唔係同一種"},
    {"wrong": "顏色：黑／白都當窮盡互斥", "right": "類別要淨得兩個值先算窮盡互斥"},
])

# 8. 2x2 視覺鷹架：另一個範例（錯誤：？／？：建設——雙空格配對）
db.add_scaffold_2x2(prs, FOOTER, "另一個範例：雙空格點做",
    problem="錯誤：『？』／『？』：建設　分別填一個相關詞",
    what="錯誤同建設，\n分別要配一個\n相關詞，兩組\n關係要一致",
    given="A正確／建造\nB過失／設置\nC紕漏(得一個)\nD謬誤／毀壞",
    strategy="『正確』＝錯誤\n嘅反義詞；\n『建造』＝建設\n嘅近義詞",
    check="兩組關係類型\n各自準確清晰，\nD兩組自相矛盾\n答案：A")

# 9. 步驟卡：自己動手時的四個動作
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "讀清楚已知嗰對詞，講出關係類型",
    "逐個選項核對，是咪同一種關係",
    "兩個選項都似？諗清邊個結構一致",
    "揀咗答案，代返去題目讀一次",
], note="純粹憑感覺揀，同冇做呢一步一樣")

# 10. 過渡頁
db.add_transition(prs, "最後，進入練習\n老師陪你做第一題", FOOTER)

# 11. 練習講解：練習A 第1題
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="A1．航海：羅盤　與　生命：？\nA．靈魂　B．夢想　C．經驗　D．活力",
    steps=[
        "已知：羅盤指引航海嘅方向",
        "生命同樣需要一個方向指引",
        "A靈魂／C經驗／D活力都唔係方向指引",
        "得B夢想扮演方向指引角色，答案B",
    ],
    note="易錯：淨係揀『感覺有關』嗰個，唔係目標")

# 12. 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "2．金屬：鐵　與？：單車\nA交通工具　B車輪\nC摩托車　D以上皆不是\n\n鷹架：題目旁附\n關係類型對照表"},
    {"star": 2, "label": "練習B", "problem": "4．峰迴路轉山窮水盡\n邊句意思相同？\nA安居樂業四海為家\nB比比皆是一成不變\nC沉默寡言豪言壯語 D囫圇吞棗融匯貫通\n鷹架：冇提示，自己諗"},
    {"star": 3, "label": "練習C", "problem": "5．男：女：性別\n邊項係同等關係？\nA北磁極南磁極磁極\nB北南方向\nC黑白顏色 D以上不是\n鷹架：完全冇提示"},
])

# 13. 總結
db.add_summary(prs,
    takeaway="唔係揀『感覺似』，\n係揀『同一種關係』\n嘅嗰個選項。",
    floor_version="見到類比題，\n先問：呢對詞\n係咩關係？",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_類比與詞語關係_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
