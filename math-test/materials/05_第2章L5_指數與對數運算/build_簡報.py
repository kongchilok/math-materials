# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L5 指數律與對數運算。主設計 D2 手順卡（對數運算四步卡）
＋輔助 D13 弗雷爾概念模型（對數定義四象限）、D14 錯誤分析對比（log相加/係數/換底三個高頻錯法）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L5 指數律與對數運算"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

db.add_cover(prs, SUBJECT, "指數律與對數運算", "資源班課堂教學．對數運算四步卡", FOOTER)

db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "對數是甚麼？先弄清楚定義同邊界",
    "認識《對數運算四步卡》",
    "四個範例，把四步卡用足",
    "認清幾個最容易錯的寫法",
])

db.add_question_intro(prs, FOOTER, "先想一想",
    "唔用計算機，你點知邊個大？\n2 的 32 次方　定　4 的 31 次方？",
    ["2 的 32 次方較大", "4 的 31 次方較大", "一樣大"],
    "提示：可唔可以將兩個數化成同一個底，再比次方？")

# 三欄鷹架①：把 D13 弗雷爾概念模型（定義／特徵／例與非例）壓成三欄
db.add_cra(prs, FOOTER, "對數是甚麼：定義、特徵、例子",
    concrete={"label": "①定義（自己的話）", "desc": "log_a N=k 讀作\n「a 的幾多次方等於 N」\n\n例：log₂8 問\n「2 的幾多次方=8」\n答案 3，即 log₂8=3"},
    representational={"label": "②特徵（四條件）", "desc": "①底數 a>0 且 a≠1\n②真數 N>0（負數或\n0 都無對數）\n③結果 k 可正可負\n④log_aN=k ⇔ a^k=N"},
    abstract={"label": "③例與非例", "desc": "合法：log₂8=3、\nlog₂₅1=0\n\n不合法：log₂(-8)\n（違反②）、log₁5\n（違反①）"})

db.add_step_card(prs, FOOTER, "對數運算四步卡", [
    "1. 同底：log 化成同一個底，不同底用換底公式",
    "2. 合併：用運算律把幾個 log 併成一個",
    "3. 標準式：化成 log_a N=k，兩邊各剩一項",
    "4. 還原：改寫成 a^k=N，解出答案後驗真數",
], note="任何一條有 log 的題目，都由第 1 步做起。")

db.add_transition(prs, "接下來，比一比\n幾個容易寫錯的地方", FOOTER)

db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "log2+log5=log7（真數相加）", "right": "log2+log5=log10=1（真數相乘）"},
    {"wrong": "2log3=log6（係數乘入真數）", "right": "2log3=log9（係數變次方）"},
    {"wrong": "logM／logN=log(M／N)", "right": "logM／logN=log_N M（換底公式）"},
])

# 2x2 視覺鷹架：對數方程範例，四步全部用上，四格對應四步
db.add_scaffold_2x2(prs, FOOTER, "範例：對數方程四步全用上",
    problem="解方程 log(x-3)+log x=1",
    what="求出 x 的值\n（要滿足原方程的解）",
    given="兩個 log 都無寫底數，\n即都以 10 為底，已同底",
    strategy="合併：log[x(x-3)]=1\n標準式：log₁₀(x²-3x)=1\n還原：x²-3x=10",
    check="x²-3x-10=0\n(x-5)(x+2)=0，x=5或-2\nx=-2 使 x-3<0，捨去\n∴ x=5")

db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "檢查所有 log 是否同底，不同底就換底",
    "用運算律合併：相加→相乘、相減→相除、係數→次方",
    "化成標準式 log_a N=k，兩邊各剩一項",
    "還原成 a^k=N 解出答案，逐個代回驗真數",
], note="方程題的話，驗真數是解題的一部分，不是選做。")

db.add_transition(prs, "進入練習，\n老師陪你做第一題", FOOTER)

db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="判斷 log₃81、log₂(-8)、log₁5、log₄₀1 是否有意義，\n有意義的求出值",
    steps=[
        "(a) 3⁴=81，底數真數皆合法 → log₃81=4",
        "(b) 真數 -8<0，違反特徵②，無意義",
        "(c) 底數是 1，違反特徵①，無意義",
        "(d) 40⁰=1，底數真數皆合法 → log₄₀1=0",
    ],
    note="⚠ 答「無意義」仲要寫出違反第幾個特徵，先算完整。")

db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "計算 log4+log25 的值\n\n鷹架：四步卡印在\n題目旁邊，照住做"},
    {"star": 2, "label": "練習B", "problem": "設 log2=a、log3=b，\n用 a、b 表示 log12\n\n鷹架：四步卡只喺\n區塊開頭印一次"},
    {"star": 3, "label": "練習C", "problem": "解方程\n4^(x+4)-2×2^(x+4)=-1\n\n鷹架：卡片已收起，\n步驟要自己記"},
])

db.add_summary(prs,
    takeaway="對數只是指數的另一種寫法，\n四步做完記得驗真數。",
    floor_version="log 問「幾多次方」；\n四步：同底→合併→\n標準式→驗真數。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_指數對數_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
