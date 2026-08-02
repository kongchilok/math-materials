# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L7 一元二次方程與二次不等式。主設計 D2 手順卡（三張：解方程／判別式／解不等式）＋輔助 D5 圖文雙軌、D14 錯誤分析對比（見講義教師實施說明頁）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L7 一元二次方程與二次不等式"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1 封面
db.add_cover(prs, SUBJECT, "一元二次方程與二次不等式", "資源班課堂教學．手順卡解題法", FOOTER)

# 2 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "猜猜這題不等式解是兩點還是一段範圍",
    "學三張手順卡：解方程、判別式、解不等式",
    "看清楚兩個每年都有人中招的錯法",
    "老師陪你做第一題練習",
])

# 3 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "解 x²-x-6 > 0\n這一題的答案，應該是……",
    ["x=3 或 x=-2（兩個點）", "x<-2 或 x>3（一段範圍）", "-2<x<3（中間那段）"],
    "等一下用符號線，把「要取哪一段」畫出來就知道答案。")

# 4 三欄鷹架①：手順卡一完整走一次（解方程）
db.add_cra(prs, FOOTER, "範例：手順卡一完整走一次（解方程）",
    concrete={"label": "①化標準式", "desc": "題目：\nx²-5x+6=0\n\n已經是一邊為0\n的標準式，\n可以直接分解"},
    representational={"label": "②試因式分解", "desc": "找兩數：\n積為6、和為5\n→ 2 與 3\n\n(x-2)(x-3)=0\n令每個括號=0"},
    abstract={"label": "③寫兩根並檢核", "desc": "x=2 或 x=3\n\n代回原式：\n兩個根都使\n原式等於0 ✓"})

# 5 步驟卡：先認題型
db.add_step_card(prs, FOOTER, "先認題型，才知道拿哪張卡", [
    "問「解x」「求方程」→ 手順卡一：化標準式→分解→公式法",
    "問「幾個實根」→ 手順卡二：抄a,b,c→算Δ→判正負零",
    "式子有>、<、≥、≤ → 手順卡三：化正→求根→畫符號線",
], note="先認出題型，再把對應那張卡放旁邊。")

# 6 過渡（轉換點1）
db.add_transition(prs, "接下來，看兩個\n每年都有人中招的錯法", FOOTER)

# 7 迷思澄清
db.add_misconception(prs, FOOTER, "兩個每年都有人中招的錯法", [
    {"wrong": "x²-x-6>0 解成 x=3或x=-2", "right": "答案是範圍：x<-2 或 x>3"},
    {"wrong": "兩邊乘-1，不等號照抄不變", "right": "乘負數，不等號要轉向（≥變≤）"},
    {"wrong": "Δ=0 就是「無解／無實根」", "right": "Δ=0 是兩個相等實根（重根）"},
])

# 8 視覺鷹架：符號線完整走一次（不等式）
db.add_scaffold_2x2(prs, FOOTER, "範例：符號線完整走一次（不等式）",
    problem="解 x²-2x-3>0，並寫出 x²-2x-3≤0 的解",
    what="求兩個不等式的 x 範圍解",
    given="x²-2x-3\n開口向上（x²係數正）",
    strategy="先求根：\n(x-3)(x+1)=0\nx=3 或 x=-1\n符號線：兩根外正、中間負",
    check=">0取兩邊：x<-1或x>3\n≤0取中間：-1≤x≤3\n驗：x=4→5>0 ✓")

# 9 步驟卡：自己動手時的四個動作
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "先認出題型，拿對應那張卡放旁邊",
    "化成一邊為0（不等式順便讓x²係數變正）",
    "求出根，因式分解或公式法，比大小排好",
    "不等式畫符號線取區間；其餘直接寫答案",
], note="四張卡的共同起手式：先化成一邊為0。")

# 10 過渡（轉換點2）
db.add_transition(prs, "進入練習，\n老師陪你做第一題", FOOTER)

# 11 練習講解頁
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="解方程（因式分解）：(a) x²-7x+10=0　(b) x²-9=0",
    steps=[
        "(a) 已是標準式；找積10、和7 → 2 和 5",
        "(a) (x-2)(x-5)=0 → x=2 或 x=5",
        "(b) x²-9 是平方差 → (x-3)(x+3)=0",
        "(b) 令括號為0 → x=3 或 x=-3（兩根都要寫）",
    ],
    note="⚠ 兩個括號各給一個根，只寫一個x就是漏根。")

# 12 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "判斷根的情況：\nx²-4x+4=0\n\n（手順卡二在旁：\n抄a,b,c→算Δ→判正負零）"},
    {"star": 2, "label": "練習B", "problem": "公式法解：\nx²-6x+2=0\n（答案化到最簡）\n\n（只重印關鍵詞，\n自己認題型）"},
    {"star": 3, "label": "練習C", "problem": "解不等式：\nx²-x-6≤0\n\n（不印卡，自己求根、\n畫符號線取區間）"},
])

# 13 總結
db.add_summary(prs,
    takeaway="先化成一邊為0，\n認出題型拿對卡，\n不等式別忘畫符號線。",
    floor_version="大於取兩邊、小於取中間；\n乘負數，不等號要轉向。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_二次方程不等式_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
