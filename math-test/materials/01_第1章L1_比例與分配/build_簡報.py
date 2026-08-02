# -*- coding: utf-8 -*-
"""資源班簡報：第1章 L1 比例與分配。主設計 D1 條形模型＋輔助 D8/D4（見講義教師實施說明頁）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第1章 特殊數學應用專題．L1 比例與分配"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1 封面
db.add_cover(prs, SUBJECT, "比例與分配", "資源班課堂教學．條形模型解題法", FOOTER)

# 2 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "猜猜「先打9折再打85折」等於打幾折",
    "學條形圖的三種畫法",
    "找出題目裡的隱藏陷阱詞",
    "老師陪你做第一題練習",
])

# 3 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "同一款計算機，先打 9 折，再打 85 折。\n這樣總共等於打幾折？",
    ["74.5 折", "76.5 折", "5 折"],
    "等一下我們用條形圖，把「折上折」畫出來就知道答案。")

# 4 CRA 三階
db.add_cra(prs, FOOTER, "從實物到算式：怎麼「看見」比例",
    concrete={"label": "具體", "desc": "文具店裡，原子筆一疊、鉛筆一疊。\n\n原子筆的支數是鉛筆的 3/4，\n哪一疊比較多？多多少？"},
    representational={"label": "表徵（條形圖）", "desc": "鉛筆畫 4 格、原子筆畫 3 格。\n\n每一格代表同樣多的支數。\n\n合共 7 格＝63 支。"},
    abstract={"label": "抽象（算式）", "desc": "設 1 格 = u 支\n\n3u + 4u = 63\n7u = 63\nu = 9"})

# 5 步驟卡：條形圖三畫法
db.add_step_card(prs, FOOTER, "條形圖三種畫法", [
    "部分—整體：一個整體拆成幾份（例：全班分男生與女生）",
    "比較：兩個量並排，長度差就是相差（例：原子筆比鉛筆少幾支）",
    "前後變化：同一個量在事情前後各畫一條（例：打折前與打折後的價格）",
], note="依題目情境挑一種畫法，不要混用。")

# 6 過渡（轉換點1）
db.add_transition(prs, "接下來，學怎麼從題目\n找出關鍵字", FOOTER)

# 7 迷思澄清
db.add_misconception(prs, FOOTER, "三個容易踩錯的陷阱詞", [
    {"wrong": "「甲比乙多3倍」＝甲是乙的3倍", "right": "甲是乙的 4 倍（乙畫1格，甲畫4格）"},
    {"wrong": "先打9折再打85折＝打(9+8.5)折", "right": "要連乘：0.9×0.85＝0.765，即76.5折"},
    {"wrong": "錄取率25%，分母是錄取人數", "right": "分母是報考人數（全體），不是錄取人數"},
])

# 8 視覺鷹架（範例四格）
db.add_scaffold_2x2(prs, FOOTER, "範例：完整走一次",
    problem="文具店賣出原子筆與鉛筆共63支，原子筆是鉛筆的3/4，問原子筆比鉛筆少賣多少支？",
    what="原子筆比鉛筆少賣了多少支？",
    given="共 63 支；原子筆是鉛筆的 3/4",
    strategy="鉛筆4格、原子筆3格\n3u + 4u = 63 → u = 9",
    check="4u − 3u = 9（支）\n27+36=63 ✓　27/36=3/4 ✓\n答：少賣 9 支")

# 9 步驟卡：四個動作口訣
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "讀題，圈關鍵字（一般畫單底線、陷阱詞畫雙底線）",
    "決定哪個量畫最少格，其餘照倍數堆同樣大小的格",
    "數出總格數，用「總量 ÷ 總格數」求一格等於多少",
    "看清楚問題問哪一段，乘回去，寫上單位",
])

# 10 過渡（轉換點2）
db.add_transition(prs, "進入練習，\n老師陪你做第一題", FOOTER)

# 11 練習講解頁
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="文具店原子筆與鉛筆共72支，原子筆是鉛筆的5/7，問鉛筆有多少支？",
    steps=[
        "原子筆是鉛筆的 5/7 → 原子筆畫5格，鉛筆畫7格",
        "合共 5+7=12 格，對應72支：12u=72",
        "u = 72÷12 = 6（支）",
        "鉛筆 = 7u = 7×6 = 42（支）",
    ],
    note="⚠ 問的是「鉛筆」，不是原子筆，也不是一格的值 u。")

# 12 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "甲乙兩箱蘋果共96個，甲箱是乙箱的3/5，問甲箱比乙箱少多少個？\n\n（條形圖框已畫好，只要填數字）"},
    {"star": 2, "label": "練習B", "problem": "獎金84000元按2:3:7分給甲乙丙三部門，問分得最多的比最少的多多少元？\n\n（只給空白格線，自己分段）"},
    {"star": 3, "label": "練習C", "problem": "A店：定價先打9折再打85折；B店：先減價20%再打9折。哪間比較便宜？便宜定價的百分之幾？\n\n（不給圖，自己畫自己列式）"},
])

# 13 總結
db.add_summary(prs,
    takeaway="先畫圖數格數，\n再用「總量÷總格數」求一格，\n最後乘回去。",
    floor_version="看到「共」就加、看到「比多」就減，\n畫格子數一數就知道答案。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_比例與分配_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
