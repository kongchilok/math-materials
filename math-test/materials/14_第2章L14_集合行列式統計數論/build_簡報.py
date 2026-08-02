# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L14 集合、行列式、統計與數論。主設計 D7 提示卡（五張：集合運算與容斥／
行列式求值／統計圖表判讀／統計量／數論，一種小題型一張，觸發條件即為本課核心技能「認題」）
＋輔助 D8 關鍵字對譯（一般對譯＋陷阱詞分開列）、D2 手順卡（只用於行列式餘因子展開五步）。
本課合併四個互不相關的子主題，逐頁刻意輪流覆蓋集合／行列式／統計／數論，不集中單一子題。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L14 集合、行列式、統計與數論"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "集合、行列式、統計與數論", "資源班課堂教學．五張提示卡＋關鍵字對譯表", FOOTER)

# 2. 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "集合：∪／∩／容斥原理，一次過學識",
    "行列式：2×2 公式＋3×3 或以上餘因子展開",
    "統計：睇圖表、比較標準差，唔使死背",
    "數論：質因數分解，數正因數個數",
])

# 3. 問題引入（集合，取自範例A的「只差一個字母」懸念）
db.add_question_intro(prs, FOOTER, "先想一想",
    "R={a,b,c,d}、M={b,e,f}、N={c,f,g}\n求 (R∪M)∩N＝？",
    ["{c,f}", "{f}", "{a,b,c,d,e,f,g}"],
    "提示：見到括號，一定要先做返入面嗰個先。")

# 4. 三欄總覽：五張卡濃縮成三組（集合／行列式／統計＋數論）
db.add_cra(prs, FOOTER, "五種題型，濃縮做三組",
    concrete={"label": "①集合＆容斥", "desc": "觸發：見到｛｝\n∪＝或，收得多\n∩＝且，收得少\n有括號，先做入面\n人數題套容斥公式"},
    representational={"label": "②行列式求值", "desc": "觸發：兩線夾住方陣\n2×2：ad－bc\n3×3或以上：\n餘因子展開\n揀0最多嗰行／列"},
    abstract={"label": "③統計＆數論", "desc": "統計：睇清兩條軸\n標準差三規則\n數論：先質因數分解\n正因數：指數加1\n再相乘"})

# 5. 步驟卡：核心分類法（跨全部五種，先認題）
db.add_step_card(prs, FOOTER, "第一步，永遠都係：認一認係邊種", [
    "見到｛｝、∪、∩ → 集合，翻卡一",
    "兩條直線夾住方陣 → 行列式，翻卡二",
    "有折線／長條圖問「幾多個月」→ 統計圖表，翻卡三",
    "見到平均數／中位數／眾數／標準差 → 統計量，翻卡四",
    "見到因數／倍數／質數／整除 → 數論，翻卡五",
], note="認啱先識揀啱張卡；認錯，計得幾啱都冇用。")

# 6. 過渡頁
db.add_transition(prs, "接下來，睇下\n邊幾個位最容易撞板", FOOTER)

# 7. 迷思澄清（集合／統計／數論，三個唔同子主題）
db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "(R∪M)∩N 由左至右做", "right": "有括號先做入面嗰個 ∪"},
    {"wrong": "6~10 標準差大過 1~5", "right": "整組平移，標準差唔變"},
    {"wrong": "1 係質數", "right": "1 唔係質數，由 2 開始先算"},
])

# 8. 2x2 視覺鷹架：統計量完整範例（比較標準差）
db.add_scaffold_2x2(prs, FOOTER, "範例：三組數據，邊組標準差最大？",
    problem="A: 1,2,3,4,5　B: 3,6,9,12,15　C: 6,7,8,9,10",
    what="邊組標準差\n最大？",
    given="A同C：\n只係整組平移\nB：全部×3",
    strategy="平移，標準差\n唔變 → A=C\n乘3，標準差\n變3倍 → B大",
    check="答案：B\n（平移唔變，\n乘k就變k倍）")

# 9. 步驟卡：自己動手時的動作（行列式手順卡，取自講義原文）
db.add_step_card(prs, FOOTER, "自己動手時：餘因子展開五個動作", [
    "① 掃一次，揀 0 最多嗰行或列",
    "② 寫低嗰行／列嘅棋盤符號",
    "③ 逐項劃走成行成列，剩低子行列式",
    "④ 棋盤符號×元素×子行列式，逐項計",
    "⑤ 全部加埋，換第二行再做覆核",
], note="呢五步淨係用喺 3×3 或以上；2×2 直接 ad－bc。")

# 10. 過渡頁
db.add_transition(prs, "跟住，到你哋\n跟老師一齊做第一題", FOOTER)

# 11. 練習講解（練習A①，集合）
db.add_practice_explain(prs, FOOTER, "練習A①．老師示範",
    problem="R={a,b,c,d,e}、M={c,f}、N={b,f,g}\n求 (R∪M)∩N",
    steps=[
        "先做括號入面：R∪M={a,b,c,d,e,f}",
        "攞 N={b,f,g} 逐個核對",
        "b✘　f✔　g✘",
        "所以答案 ＝ {f}",
    ],
    note="M改做{c,f,g}，答案就會唔同——記得核對括號。")

# 12. 分層任務（練習A數論／練習B統計／練習C行列式，三個唔同子主題）
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "180有幾多個\n正因數？\n（提示：先質因數\n分解）\n\n鷹架：卡五喺手邊，\n跟卡逐步做"},
    {"star": 2, "label": "練習B", "problem": "邊組標準差最大？\nA:5,6,7,8,9\nB:2,4,6,8,10\nC:10,11,12,13,14\n鷹架：諗返平移／\n乘k規則"},
    {"star": 3, "label": "練習C", "problem": "行列式＝68，求x：\n第一列 2,3,1\n第二列 x-1,x+2,2x\n第三列 4,1,3\n鷹架：卡已收，\n自己諗步驟"},
])

# 13. 總結
db.add_summary(prs,
    takeaway="睇到題目，先問自己：\n呢題屬邊一種？",
    floor_version="認唔出係邊種，就翻\n嗰張速查表，一定啱。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_集合行列式統計數論_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
