# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L6 根式、分式的化簡與有理化。主設計 D2 手順卡（三張）＋輔助 D9 草稿分區、D12 自我核對（見講義教師實施說明頁）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L6 根式、分式的化簡與有理化"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1 封面
db.add_cover(prs, SUBJECT, "根式、分式的化簡與有理化", "資源班課堂教學．手順卡＋四格草稿法", FOOTER)

# 2 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "認識三張手順卡：根式化簡、有理化、分式化簡",
    "看四個範例，每個都示範一次完整程序",
    "分四格草稿寫練習A、B、C",
    "每一區做完，先對照核對清單再往下",
])

# 3 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "計算 √48－√27＋√12，你覺得答案是？",
    ["√33（把根號內的數字直接加減）", "3√3（先化到最簡，再合併同類根式）", "沒辦法算，因為三個根號不同"],
    "等一下用手順卡一，一步步拆開就知道答案。")

# 4 三欄頁：三張手順卡總覽（主設計是D2手順卡，非CRA，故relabel為三張卡）
db.add_cra(prs, FOOTER, "三張手順卡：先認題型，再選卡",
    concrete={"label": "卡一．根式化簡", "desc": "1.拆：完全平方×剩餘\n2.開：搬出根號外\n3.併：合併同類根式\n\n※拆到剩餘沒有完全\n平方因數為止"},
    representational={"label": "卡二．分母有理化", "desc": "1.取共軛：只調中間\n符號\n2.平方差公式展開\n3.約簡：分子每項\n都要除\n\n※共軛前後兩項不動"},
    abstract={"label": "卡三．分式化簡", "desc": "1.分母先因式分解\n2.通分，分子加括號\n3.合併、約掉公因式\n4.寫出x的限制\n\n※限制不會因化簡\n而消失"})

# 5 步驟卡：怎麼認出用哪一張卡
db.add_step_card(prs, FOOTER, "怎麼認出用哪一張卡", [
    "根號內不是完全平方 → 卡一：根式化簡",
    "分母出現根號 → 卡二：分母有理化",
    "兩個以上分式相加減，或分母是多項式 → 卡三：分式化簡",
    "先看清楚結構再動筆，寫完一步回頭看上一步",
], note="三種程序完全不同，硬併成一張會變十步。")

# 6 過渡（轉換點1）
db.add_transition(prs, "三張卡都認熟了\n真正的戰場在草稿紙", FOOTER)

# 7 迷思澄清
db.add_misconception(prs, FOOTER, "三個最常見的錯法", [
    {"wrong": "√(4×5)寫成4√5，忘記開方", "right": "4開方是2，答案2√5"},
    {"wrong": "共軛連負號一起搬成－a－√b", "right": "共軛只調中間符號，前後不動"},
    {"wrong": "分式化簡完就不用寫限制", "right": "限制來自原式分母，不會消失"},
])

# 8 視覺鷹架（完整走一次：分式化簡，講義範例D）
db.add_scaffold_2x2(prs, FOOTER, "完整走一次：分式化簡",
    problem="化簡 1+x/(1-x)－2x/(x²-1)，並寫出x的限制",
    what="把三個分式合併化到\n最簡，並找出x不可\n以等於甚麼",
    given="分母有1-x與x²-1；\n1-x=-(x-1)（不同號\n要先統一）",
    strategy="因式分解找公分母\n(x-1)(x+1)，通分時\n分子要加括號",
    check="答案(-3x-1)/(x²-1)\nx≠1且x≠-1\n代x=2驗算：-7/3 ✓")

# 9 步驟卡：自己動手時的四個動作
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "①抄下原式，圈出要先處理的部分",
    "②拆開或通分，中間式寫出來",
    "③計算，合併同類項",
    "④檢查：根號/分母乾淨？限制寫了？",
], note="每一格只做一件事，寫在哪格就代表做緊邊一步。")

# 10 過渡（轉換點2）
db.add_transition(prs, "四個動作都會了\n換你上場：練習A、B、C", FOOTER)

# 11 練習講解頁
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="化簡√50、√75，求三邊為此三數的三角形周長",
    steps=[
        "√50=√(25×2)=5√2",
        "√75=√(25×3)=5√3",
        "√25=5（25本身是完全平方）",
        "三項根號內都不同，沒有同類項",
        "周長=5√2+5+5√3（厘米）",
    ],
    note="答案有三項是正常的——不能合併就是最簡形式。")

# 12 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "計算√48－√27＋√12\n\n鷹架：手順卡在旁，\n四格草稿區"},
    {"star": 2, "label": "練習B", "problem": "化簡1/(x-1)+1/(x+1)，\n並寫出x的限制\n\n鷹架：四格草稿區，\n關鍵詞開頭印一次"},
    {"star": 3, "label": "練習C", "problem": "化簡1/(x-2)-4/(x²-4)，\n並說明x=2為何無意義\n\n鷹架：無四格，自己\n分四步寫"},
])

# 13 總結
db.add_summary(prs,
    takeaway="先認題型、照程序做；\n化簡再順，都要回頭寫限制。",
    floor_version="根號內沒完全平方、分母沒根號、\n寫了x的限制——三件事沒漏，就對了大半。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_根式分式_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
