# -*- coding: utf-8 -*-
"""
第2章 L8 解析幾何（一）直線與圓　資源班課堂簡報
主設計：D5 圖文雙軌對照（依 teaching-designs.md，S6 解析幾何結構）
輔助設計：D2 手順卡、D9 草稿分區
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L8 解析幾何（一）直線與圓"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(
    prs, SUBJECT, UNIT,
    "資源班課堂簡報．Tier 2 抽離小班",
    FOOTER,
)

# 2. 流程預告
db.add_flow_preview(
    prs, FOOTER, "今天要做的四件事",
    [
        "兩張手順卡：求直線方程／判斷位置關係",
        "範例A、B：點的基本量與斜率、截距",
        "範例C、D：求直線方程＋求圓方程",
        "範例E＋練習A／B／C：直線與圓的位置關係",
    ],
)

# 3. 問題引入
db.add_question_intro(
    prs, FOOTER,
    "先感覺一下：這條線跟這個圓，是什麼關係？",
    "已知圓 C：x²+y²=10（圓心O(0,0)，r=√10≈3.16）\n直線 L：x+y-4=0。你覺得 L 跟 C 是？",
    [
        "相交（兩個交點）",
        "相切（一個交點）",
        "相離（沒有交點）",
    ],
    "不急住計算——先在腦入面畫個圖，圓心到呢條線大概有幾遠？同 r 比一比。",
)

# 4. CRA① 範例A・點的基本量（圖文雙軌relabel）
db.add_cra(
    prs, FOOTER, "範例A・點的基本量（到軸距離、兩點距離、中點）",
    dict(label="① 圖上看到什麼",
         desc="A(-2,3)、B(4,-5)\n向x軸/y軸畫垂線\n量高度看y、寬度看x\n補直角三角形量斜邊\n中點在正中間，各半"),
    dict(label="② 代入算式點寫",
         desc="到x軸距離=|3|=3\n到y軸距離=|-2|=2\n|AB|=√(6²+8²)=10\n中點M=(1,-1)"),
    dict(label="③ 抽象公式",
         desc="到x軸距離=|y|\n到y軸距離=|x|\n|AB|=√(Δx²+Δy²)\n中點=(平均x,平均y)"),
)

# 5. 步驟卡：求直線方程 手順卡精簡版
db.add_step_card(
    prs, FOOTER, "手順卡一・求直線方程",
    [
        "認清三種給法：一點+斜率／兩點／一點+另一線",
        "求斜率m：兩點用差商；垂直用負倒數",
        "代點斜式整理成一般式 ax+by+c=0",
        "代回原本的點檢查，等式要成立",
    ],
    note="※ 垂直斜率是「負倒數」，不是只變號",
)

# 6. 過渡頁1
db.add_transition(
    prs,
    "公式都不難，難的是——\n這一步在圖上是什麼意思？",
    FOOTER,
)

# 7. 迷思澄清
db.add_misconception(
    prs, FOOTER, "最常見的三個錯法",
    [
        dict(wrong="到x軸距離看x坐標", right="到x軸距離看y坐標（量高度）"),
        dict(wrong="垂直斜率把原斜率變號", right="垂直斜率要取負倒數 -1/m"),
        dict(wrong="圓標準式右邊寫半徑r", right="圓標準式右邊要寫 r²"),
    ],
)

# 8. D9 四格草稿分區示範（範例C(c)）
db.add_scaffold_2x2(
    prs, FOOTER, "範例C(c)．四格草稿分區示範",
    "過 Q(4,1) 且垂直於 L：2x+3y-6=0 的直線方程（一般式）",
    "求：過Q垂直於L的\n直線方程（一般式）",
    "點 Q(4,1)\nL 斜率 m=-2/3",
    "垂直斜率=負倒數\nm'=3/2\n代點斜式：\ny-1=3/2(x-4)",
    "整理：3x-2y-10=0\n代Q驗證：12-2-10=0✓\n斜率積(-2/3)(3/2)=-1✓",
)

# 9. 步驟卡：自己動手時的動作
db.add_step_card(
    prs, FOOTER, "自己動手時的動作",
    [
        "先看題目屬於邊種：點的量／求直線／求圓／判位置",
        "有格就先畫圖：圓心半徑標出、直線方向畫出",
        "對照手順卡：認出給法→求斜率或圓心半徑→代公式",
        "代回原本的點或值檢查，等式應該成立",
    ],
    note="※ 冇畫圖就硬代，錯一個負號就全題報廢",
)

# 10. 過渡頁2
db.add_transition(
    prs,
    "畫完圖、代完公式——\n輪到你自己上場了",
    FOOTER,
)

# 11. 練習講解：練習A・第1題
db.add_practice_explain(
    prs, FOOTER, "練習A・第1題．示範詳解",
    "已知 A(-4,1)、B(2,9)。求 A 到 x/y 軸距離、|AB|、AB 中點 M",
    [
        "到x軸距離=|1|=1，到y軸距離=|-4|=4",
        "水平差=2-(-4)=6，垂直差=9-1=8",
        "|AB|=√(6²+8²)=√100=10",
        "中點M：坐標各自取平均=(-1,5)",
    ],
    note="檢查：|AM|=|MB|=5，兩段相加=10 ✓",
)

# 12. 分層任務
db.add_tiered_task(
    prs, FOOTER, "分層任務．練習A／B／C",
    [
        dict(star=1, label="練習A",
             problem="L: 4x-2y+6=0\n（a）求斜率\n（b）求y截距\n【附已畫好坐標圖】"),
        dict(star=2, label="練習B",
             problem="求直線方程(一般式)\n(a)過P(3,-2)\n斜率-1\n(b)過A(-1,2)\n與B(3,10)\n【只給空白坐標格】"),
        dict(star=3, label="練習C",
             problem="判斷 L:x-y+4=0\n與圓C:(x-1)²+(y-2)²=9\n的位置關係，求交點\n【不給格，自己畫草圖】"),
    ],
)

# 13. 總結頁
db.add_summary(
    prs,
    "看到圖先想算式，看到算式先想圖",
    "到x軸用y、到y軸用x；垂直斜率要負倒數；圓方程右邊是r²",
    FOOTER,
)

out_path = os.path.join(os.path.dirname(__file__), "簡報_直線與圓_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
