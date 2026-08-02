# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L13 數列與級數。主設計 D2 手順卡（四張：等差通項／等差求和／
等比通項與求和／數學歸納法三步）＋輔助 D13 弗雷爾概念模型（等差／等比四象限，
主攻「兩種都唔係」嗰個反例）、D12 自我核對（融入步驟卡嘅check動作同總結保底版）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L13 數列與級數"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "數列與級數", "資源班課堂教學．四張數列手順卡", FOOTER)

# 2. 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "先分清楚：呢串數係加嘅定係乘嘅",
    "認識《四張數列手順卡》",
    "五個範例，逐張卡用一次",
    "認清「漏咗+1」呢個最貴嘅陷阱",
])

# 3. 問題引入
db.add_question_intro(prs, FOOTER, "先諗一諗",
    "唔好心算，睇清楚呢串數：\n1/2, 1/4, 1/6, 1/8, ⋯ 係邊一種數列？",
    ["等差數列（差固定）", "等比數列（商固定）", "兩種都唔係"],
    "提示：連續計兩次相減，再計兩次相除，睇到第三項先落判斷。")

# 4. 三欄鷹架①：把兩張弗雷爾卡＋三十秒判斷法壓成三欄
db.add_cra(prs, FOOTER, "先分清楚：等差 定 等比",
    concrete={"label": "①等差數列", "desc": "後項減前項\n差都一樣＝d\na_n=a₁+(n-1)d\nS_n=n(a₁+a_n)/2\n例：3,7,11,15…"},
    representational={"label": "②等比數列", "desc": "後項除前項\n商都一樣＝r\na_n=a₁×r^(n-1)\nS_n=a₁(r^n-1)/(r-1)\n例：2,6,18,54…"},
    abstract={"label": "③三十秒判斷法", "desc": "先相減：差都同→等差\n唔同就試埋相除\n商都同→等比\n兩個都唔同：兩種都唔係\n睇到第三項先落筆"})

# 5. 步驟卡：核心分類法
db.add_step_card(prs, FOOTER, "點樣揀啱嗰張手順卡", [
    "相減幾次，差都一樣 → 揀卡一或卡二（等差）",
    "相除幾次，商都一樣 → 揀卡三（等比）",
    "見到「用數學歸納法證明」→ 揀卡四",
    "兩種都唔啱？分開睇分子同分母，規律通常喺度",
], note="認錯咗種類，後面計得幾啱都無用——睇清楚先好落筆。")

# 6. 過渡頁
db.add_transition(prs, "接下來，睇清楚\n三個最貴嘅計算陷阱", FOOTER)

# 7. 迷思澄清
db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "1/2,1/4,1/6…照答係等比數列", "right": "商唔一致就唔係等比，睇分母嘅規律"},
    {"wrong": "n=(末項-首項)/d，答案唔加1", "right": "n=(末-首)/d +1，唔該加返起點嗰項"},
    {"wrong": "(-1/2)⁹計漏負號，答1/512", "right": "奇數次方留負號，正確答案係負數"},
])

# 8. 2x2 視覺鷹架：另一個範例完整走一次（等比數列兩項求首項）
db.add_scaffold_2x2(prs, FOOTER, "範例：兩項求首項（等比）",
    problem="等比數列第三項=1，\n第八項=-1/32，求首項",
    what="求首項 a₁\n（等比數列）",
    given="第三項 a₃=1\n第八項 a₈=-1/32",
    strategy="a₈/a₃=r^5=-1/32\nr=-1/2（五次方留負號）\na₃=a₁r²=1→a₁=4",
    check="數列：4,-2,1,-1/2…\n第三項=1 ✔\n第八項=-1/32 ✔")

# 9. 步驟卡：自己動手時的動作
db.add_step_card(prs, FOOTER, "自己動手時嘅四個動作", [
    "先相減、再相除，定係邊一種數列",
    "揀啱嗰張手順卡，定a₁同d（或r）",
    "寫返公式，指數／係數用n-1，唔係n",
    "計完番去驗，代個已知項check啱唔啱",
], note="唔記得用邊條公式？睇返速查表嗰行「題目長成點」。")

# 10. 過渡頁
db.add_transition(prs, "最後，入返練習\n老師陪你做第一題", FOOTER)

# 11. 練習講解
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="(a) 3,7,11,15…係等差定等比？求第20項\n(b) 2,6,18,54…係等差定等比？求第6項",
    steps=[
        "(a) 7-3=4=11-7，差都一樣 → 等差，d=4",
        "(a) a₂₀=a₁+19d=3+76=79",
        "(b) 6÷2=18÷6=3，商都一樣 → 等比，r=3",
        "(b) a₆=a₁r⁵=2×243=486",
    ],
    note="指數／係數用n-1：第20項係19、第6項係5，唔係20同6。")

# 12. 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "求 5+9+13+⋯+101\n嘅和\n\n鷹架：手順卡二\n擺喺手邊跟住做"},
    {"star": 2, "label": "練習B", "problem": "四個數成等差，和=52，\n第四項比第一項大18，\n求呢四個數\n\n鷹架：手順卡收埋一半，\n自己諗埋步驟"},
    {"star": 3, "label": "練習C", "problem": "等比數列2,6,18,⋯,1458\n(a)共幾項？\n(b)求全部項嘅和\n\n鷹架：卡片已收埋，\n自己記步驟"},
])

# 13. 總結
db.add_summary(prs,
    takeaway="睇到數列，先諗：\n係加同一個數，\n定係乘同一個數？",
    floor_version="等差加d，等比乘r；\n指數／係數用n-1；\n代番已知項check啱。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_數列級數_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
