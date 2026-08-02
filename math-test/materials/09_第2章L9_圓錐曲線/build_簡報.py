# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L9 解析幾何（二）圓錐曲線。主設計 D7 提示卡（三張：橢圓／雙曲線／
拋物線，各附觸發語＋圖＋代數符號）＋輔助 D5 圖文雙軌（左圖右式四個範例）、
D2 手順卡（由橢圓方程求a/b/c/e/準線、求同漸近線雙曲線方程）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L9 解析幾何（二）圓錐曲線"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "解析幾何（二）圓錐曲線", "資源班課堂教學．三張圓錐曲線提示卡", FOOTER)

# 2. 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "先學識：一眼分辨橢圓、雙曲線、拋物線",
    "認識《三張圓錐曲線提示卡》",
    "五個範例，把提示卡同手順卡用足",
    "認清三個最容易撞板嘅混淆位",
])

# 3. 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "唔畫圖，淨係話你知一個數：\n離心率 e = 1.5，你講得出係邊種曲線嗎？",
    ["橢圓（0<e<1）", "拋物線（e=1）", "雙曲線（e>1）"],
    "提示：離心率將三種曲線分開三段，中間冇重疊。")

# 4. 三欄鷹架①：把 D7 三張提示卡壓成三欄（每欄一張卡的濃縮版）
db.add_cra(prs, FOOTER, "三張提示卡：一欄一張卡",
    concrete={"label": "①橢圓提示卡", "desc": "觸發語：相加=1\na²＝較大嗰個分母\n長軸跟大分母走\nc²=a²-b²（相減）\ne 界乎 0 與 1 之間"},
    representational={"label": "②雙曲線提示卡", "desc": "觸發語：相減=1\na²＝減號前嗰分母\n（唔使比大小）\nc²=a²+b²（相加）\ne 大過 1，有漸近線"},
    abstract={"label": "③拋物線提示卡", "desc": "觸發語：得一個\n變數係二次\n嗰個變數決定\n開口方向\n冇a、b、c；e＝1"})

# 5. 步驟卡：核心分類法
db.add_step_card(prs, FOOTER, "點樣一眼分辨三種曲線", [
    "先睇加減：兩項相加=1→橢圓；相減=1→雙曲線",
    "淨係一個變數係二次→拋物線（唔使諗a、b、c）",
    "兩個分母相等→圓（橢圓嘅特殊情況，e=0）",
    "有畀e：0<e<1橢圓、e=1拋物線、e>1雙曲線",
], note="動筆前，先用呢張表分類，先揀啱嗰張提示卡。")

# 6. 過渡頁
db.add_transition(prs, "接下來，拆解\n三個最常見嘅撞板位", FOOTER)

# 7. 迷思澄清
db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "a＝第一個分母（x²嗰項）", "right": "a²＝較大嗰個分母，唔理邊個字母"},
    {"wrong": "雙曲線 c²=a²-b²（同橢圓一樣）", "right": "雙曲線 c²=a²+b²（相加，同橢圓相反）"},
    {"wrong": "見到「相加=1」即刻答橢圓", "right": "先睇兩個分母是否相等，相等即係圓"},
])

# 8. 2x2 視覺鷹架：完整走一次雙曲線範例
db.add_scaffold_2x2(prs, FOOTER, "範例：雙曲線四個量全部求齊",
    problem="雙曲線 x²/16-y²/9=1\n求 a、b、c、e 同漸近線方程",
    what="求 a、b、c、\n離心率 e、\n漸近線方程",
    given="減號前面係x²項\n分母16喺x²下面\n分母9喺y²下面",
    strategy="a²=16→a=4\nb²=9→b=3\nc²=a²+b²=25\n→c=5，e=5/4",
    check="e=1.25>1 ✔\n漸近線 y=±¾x\n（b/a，唔係a/b）")

# 9. 步驟卡：自己動手時的動作
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "先分類：相加／相減／得一個二次／兩分母相等？",
    "揀返啱嗰張提示卡，記低a²、b²喺邊一項",
    "套返a、b、c關係式：橢圓減、雙曲線加",
    "check答案：e範圍啱唔啱？漸近線寫啱未？",
], note="唔識揀邊張卡？即刻問自己：呢條係加定減？")

# 10. 過渡頁
db.add_transition(prs, "最後，進入練習\n老師陪你做第一題", FOOTER)

# 11. 練習講解
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="判斷四條方程／條件 (a)-(d) 各屬邊種曲線",
    steps=[
        "(a) x²/36+y²/16=1：兩項相加=1 → 橢圓",
        "(b) y²-x²/4=1：兩項相減=1 → 雙曲線",
        "(c) y=3x²+2x-1：得 x 係二次 → 拋物線",
        "(d) e=1.5：e>1 → 雙曲線",
    ],
    note="四種判斷方法都揀啱，先至識揀返邊張提示卡。")

# 12. 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "求橢圓\nx²/100+y²/64=1\n的 a、b、c、e\n\n鷹架：提示卡喺手邊，\n跟卡逐步做"},
    {"star": 2, "label": "練習B", "problem": "雙曲線 x²/9-y²/16=1\n求a、b、c、漸近線\nP到一焦點=2，求另一個\n\n鷹架：手順卡開頭\n列返觸發語"},
    {"star": 3, "label": "練習C", "problem": "求經過P(3,4√2)、與\nx²/9-y²/16=1同漸近線\n嘅雙曲線方程\n\n鷹架：卡片已收起，\n自己記步驟"},
])

# 13. 總結
db.add_summary(prs,
    takeaway="睇到方程，先問自己：\n係加定減？定得一個二次？",
    floor_version="相加=1橢圓；相減=1\n雙曲線；一個變數\n二次=拋物線。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_圓錐曲線_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
