# -*- coding: utf-8 -*-
"""資源班簡報：第2章 L11 機率與二項式定理。主設計 D2 手順卡（五張：古典機率三步／
多次事件連乘／「最少一個」補集／二項機率四步／二項式定理通項四步）＋輔助 D8 關鍵字
對譯（L10 褪除版，只留五條陷阱詞）、D12 自我核對（練習端，四項可觀察清單）。
本課取 S2（多步驟程序運算）為主設計，因為機率與通項都要連續完成四個動作，
序列性步驟在工作記憶中崩潰正是 D2 所針對的瓶頸；L10 已用 D8 做過一輪，
語言層辨識已建立，故本課把 D8 由主降為輔。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L11 機率與二項式定理"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "機率與二項式定理", "資源班課堂教學．五張手順卡通關", FOOTER)

# 2. 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "機率係一條分數：點寫、點檢查",
    "五張手順卡：由一次事件到二項式定理",
    "陷阱詞五條：最少、恰好、唔放回、第三項、係數",
    "練習A/B/C：提示一節比一節少，自己走",
])

# 3. 問題引入
db.add_question_intro(prs, FOOTER, "先諗一諗",
    "袋裡有9個波，3個係黃色，其餘係紅色或黑色。\n伸手摸一個，摸到黃波嘅機率係幾多？",
    ["3/9＝1/3（分母用晒9個）", "3/6＝1/2（分母淨係用6個非黃波）", "9/3＝3（分子分母調轉咗）"],
    "提示：機率嘅分母係「全部」，唔淨係符合嘅嗰啲。")

# 4. 三欄鷹架①：卡一・一次事件的機率
db.add_cra(prs, FOOTER, "手順卡一：一次事件點做",
    concrete={"label": "①具體情境", "desc": "紅黃黑球比5:3:1\n抽到黃球嘅機率？"},
    representational={"label": "②手順卡步驟", "desc": "1.分母=全部\n(5+3+1=9)\n2.分子=黃球份數(3)\n3.約簡=1/3\n4.check 0≤P≤1 ✓"},
    abstract={"label": "③一般公式", "desc": "P(事件)=\n符合數÷全部數\n0≤P≤1"})

# 5. 步驟卡：五張卡速查
db.add_step_card(prs, FOOTER, "五張卡，先認題型再落筆", [
    "做一次，問機率 → 卡一：分子÷分母",
    "做幾次都係⋯ → 卡二：全部相乘",
    "出現「最少一個」→ 卡三：1－（一個都冇）",
    "做n次恰好k次 → 卡四：C(n,k)p^k(1-p)^(n-k)",
    "展開式/第幾項/係數 → 卡五：C(n,r)a^(n-r)b^r",
])

# 6. 過渡頁
db.add_transition(prs, "五張卡認熟晒\n跟住要抓陷阱詞", FOOTER)

# 7. 迷思澄清
db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "相反寫成「全部都合格」", "right": "相反係「全部都唔合格」"},
    {"wrong": "漏咗C(10,3)就直接乘", "right": "要先乘C(10,3)，先至乘p、q"},
    {"wrong": "「第三項」當成r=3", "right": "r=項數-1，第三項r=2"},
])

# 8. 三欄鷹架②：卡四・恰好成功幾次（二項機率）
db.add_cra(prs, FOOTER, "手順卡四：恰好成功幾次",
    concrete={"label": "①具體情境", "desc": "擲骰10次\n恰好3次四點？"},
    representational={"label": "②手順卡步驟", "desc": "1.n=10,k=3,p=1/6\n2.C(10,3)=120種\n3.乘p³=(1/6)³\n4.乘(1-p)⁷=(5/6)⁷"},
    abstract={"label": "③一般公式", "desc": "C(n,k)×p^k×\n(1-p)^(n-k)"})

# 9. 步驟卡：自己動手時的動作（D12 自我核對四項）
db.add_step_card(prs, FOOTER, "自己動手時，四步都要check", [
    "答案有冇落喺0同1之間",
    "分子分母係咪用緊同一把尺",
    "「最少」有冇補返個「1－」",
    "a、b兩個次方加埋等於n",
])

# 10. 過渡頁
db.add_transition(prs, "五張卡都學晒\n到你自己嚟做練習", FOOTER)

# 11. 練習講解：練習A第1題
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="(a)兩硬幣同擲，兩面都正面？　(b)三硬幣同擲，3面都正面？",
    steps=[
        "認題型：「都係」→ 翻卡二・連乘",
        "(a) 兩枚獨立，各P(正)=1/2",
        "(a) 都要發生→相乘＝1/2×1/2＝1/4",
        "(b) 三枚都獨立，各1/2",
        "(b) 三次一樣→次方＝(1/2)³＝1/8",
        "check：1/4同1/8都喺0同1之間 ✓",
    ])

# 12. 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "紅黃藍球比4:3:2\n抽到紅球嘅機率？\n\n提示：翻卡一"},
    {"star": 2, "label": "練習B", "problem": "合格率0.8、0.75、0.6\n求最少一科合格機率\n\n提示：翻卡三，\n記得補返1－"},
    {"star": 3, "label": "練習C", "problem": "求(4－2x)⁵展開式\n入面x²嘅係數\n\n提示：b＝－2x，\n負號一齊搬"},
])

# 13. 總結
db.add_summary(prs,
    takeaway="機率＝符合÷全部，\n記得0≤P≤1；\n先認題型、翻啱卡，\n一步都唔跳得。",
    floor_version="保底：識用卡一\n計一次性機率，\n識「最少」要用1－。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_機率二項式_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
