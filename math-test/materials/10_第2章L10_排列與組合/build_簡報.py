# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L10 排列與組合。主設計 D8 關鍵字對譯表（一般對譯＋陷阱詞兩張表，
「圈關鍵字→查表→計算」三步）＋輔助 D1 樹狀圖（僅範例A 出現一次）、
D7 五張提示卡（特殊位置／捆綁／插空／重複元素／補集，見講義教師實施說明頁）。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L10 排列與組合"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1 封面
db.add_cover(prs, SUBJECT, "排列與組合", "資源班課堂教學．關鍵字對譯表＋五張提示卡", FOOTER)

# 2 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "認識關鍵字對譯表：一般對譯＋陷阱詞",
    "範例：先定分類定分步，再判P定C",
    "認識五張提示卡：處理附加條件",
    "老師陪你做第一題練習",
])

# 3 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "某班有10位同學。選出「正、副班長」各一人，\n同選出「2位代表」出席會議，\n這兩種選法的方法數是不是一樣多？",
    ["一樣多，都是45種", "正副班長90種、代表45種——差一倍", "代表比較多，因為比較容易選"],
    "等一下用「調轉順序是不是同一件事」這個測試，就知道為什麼差一倍。")

# 4 三欄鷹架①：D8 的三步（圈關鍵字→查表→計算），套用範例A(a)
db.add_cra(prs, FOOTER, "範例：三步完整走一次",
    concrete={"label": "①圈關鍵字", "desc": "「先…再…」\n是兩個動作\n接續完成\n\n甲→乙→丙\n兩段都要走"},
    representational={"label": "②查表定招式", "desc": "查表：\n「先…再…」\n＝分步\n\n分步→\n方法數相乘"},
    abstract={"label": "③列式計算", "desc": "甲→乙：3+2=5種\n乙→丙：2+2=4種\n\n5×4=20種"})

# 5 步驟卡：核心判斷法（動筆前的三個問題）
db.add_step_card(prs, FOOTER, "動筆前，先問自己三個問題", [
    "動作完成了嗎？完成＝分類相加，未完成＝分步相乘",
    "調轉兩個對象，是同一件事嗎？是＝組合C，不是＝排列P",
    "有沒有必須／不能／至少／重複／圓桌？有就要加一招",
], note="次序不能反：先分類分步，再判P定C，最後才加招數。")

# 6 過渡頁（轉換點1）
db.add_transition(prs, "接下來，認識\n五張提示卡點樣用", FOOTER)

# 7 迷思澄清
db.add_misconception(prs, FOOTER, "三個容易撞板的地方", [
    {"wrong": "「至少一個」逐個情況數，又長又易漏兩三種", "right": "至少一個＝全部－一個都沒有（補集法）"},
    {"wrong": "捆綁後忘記：綁在一起的人也要排", "right": "綁完要再×k!（他們自己也能互換）"},
    {"wrong": "圓桌坐法當直排計算，寫成 n!", "right": "圓桌沒有頭尾，要用(n-1)!"},
])

# 8 2x2 視覺鷹架：另一個範例完整走一次（範例D(b) 混合題）
db.add_scaffold_2x2(prs, FOOTER, "範例：混合題完整走一次",
    problem="自助餐店80元便當：主菜3款選1，配菜8款選3，共有多少種便當？",
    what="共有多少種\n不同的便當？",
    given="主菜3款選1\n配菜8款選3\n主菜配菜都要有",
    strategy="主菜：3種\n配菜：C(8,3)=56\n(沒有先後，用C)\n分步相乘：3×56",
    check="3×56=168種\n配菜若用P(8,3)\n=336就錯——\n配菜之間沒有先後")

# 9 步驟卡：自己動手時的動作
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "讀題目，圈出關鍵字（陷阱詞要多想一步）",
    "查對譯表，決定分類定分步、P定C",
    "有沒有必須／不能／至少／重複／圓桌？挑對提示卡",
    "列式計算，答案代回去檢查是否合理",
], note="先圈關鍵字，勝過亂猜公式。")

# 10 過渡頁（轉換點2）
db.add_transition(prs, "進入練習，\n老師陪你做第一題", FOOTER)

# 11 練習講解頁
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="甲乙丙三人到速食店，每人各點一套餐（共3種），共有多少種點法？",
    steps=[
        "圈到「每人各點一個」→ 查表：獨立選一次→連乘",
        "甲有3種選擇，乙有3種，丙有3種",
        "彼此互不影響，三人分步都要做：3×3×3",
        "3³＝27種",
    ],
    note="⚠ 不是排列！三人可以都點同一款套餐。")

# 12 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "甲乙丙丁排成一列：\n(1)任意排列\n(2)甲排首位\n(3)乙不排末位\n\n提示：查提示卡一"},
    {"star": 2, "label": "練習B", "problem": "餐廳設計菜單：\n7種菜色選5種，\n其中2種必選，\n有幾種不同菜單？\n\n提示：先扣走已選2種"},
    {"star": 3, "label": "練習C", "problem": "5塊不同蛋糕分給\nA、B、C三人，\nC至少拿到一塊，\n方法數是多少？\n\n（不提示，自己判斷）"},
])

# 13 總結
db.add_summary(prs,
    takeaway="先圈關鍵字，再查表定招式，\n最後才計算。",
    floor_version="有先後用P，沒先後用C；\n有陷阱詞就翻提示卡。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_排列組合_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
