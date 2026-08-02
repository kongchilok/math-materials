# -*- coding: utf-8 -*-
"""
第2章 L12 三角函數　資源班課堂簡報
主設計：D7 提示卡（五張：六個三角比／象限符號盤／和角差角＋特殊角值表／二倍角／三角方程通解）
輔助設計：D5 圖文雙軌（直角三角形∠A→∠B對照、四象限符號表）、D2 手順卡（求非特殊角三角值的拆角程序）
選用理由：本課數學結構橫跨 S5（三角比／象限，瓶頸是記憶檢索失敗——公式超過二十條，揀錯公式
比算錯數更常見）與 S2（和角差角／二倍角／通解，多步驟程序運算）。依規則取瓶頸較前端者為主設計，
故用 D7 提示卡處理「揀啱公式」，D5、D2 按題群性質分別安放在有圖可對照與步驟最長的節次。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第2章 中學基礎數學應用．L12 三角函數"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(
    prs, SUBJECT, "三角函數",
    "資源班課堂教學．五張提示卡",
    FOOTER,
)

# 2. 流程預告
db.add_flow_preview(
    prs, FOOTER, "今天要做的四件事",
    [
        "認識五張提示卡：什麼時候翻哪一張",
        "範例A、B：六個三角比與象限符號判斷",
        "範例C、D：和角差角拆角與二倍角公式",
        "範例E＋分層任務：通解與整合應用",
    ],
)

# 3. 問題引入（呼應核心觀念：開根號只給大小，正負要另外定象限）
db.add_question_intro(
    prs, FOOTER, "先想一想",
    "已知 cos θ = 4/5，你能不能直接算出 sin θ 的值？",
    [
        "一定是 3/5",
        "一定是 -3/5",
        "要看 θ 在哪個象限，可能是 3/5 或 -3/5",
    ],
    "提示：開根號只給你大小，正負要另外用卡二查象限。",
)

# 4. CRA①：卡一・六個三角比（文字敘述＋圖＋代數符號三件套）
db.add_cra(
    prs, FOOTER, "卡一・六個三角比（三件套呈現）",
    concrete=dict(label="①什麼時候翻我",
                  desc="題目給了直角\n三角形\n（或兩條邊長）\n問 sin、cos、tan\n等於多少"),
    representational=dict(label="②圖上看什麼",
                           desc="先圈出問的\n是哪個角\n再標對邊／鄰邊\n／斜邊\n斜邊永遠是直角\n對面那一條"),
    abstract=dict(label="③公式",
                  desc="sinA=對邊/斜邊\ncosA=鄰邊/斜邊\ntanA=對邊/鄰邊\n其餘三個是\n它們的倒數"),
)

# 5. 步驟卡：五張提示卡的觸發條件（一句話記法）
db.add_step_card(
    prs, FOOTER, "五張提示卡：看到什麼就翻哪一張",
    [
        "給直角三角形或兩邊長 → 卡一・六個三角比",
        "只給一個值或問第幾象限 → 卡二・象限符號盤",
        "求15°/75°/105°等非特殊角 → 卡三・和角差角",
        "式子有2α或sinα+cosα → 卡四・二倍角",
        "題目問通解、選項有n → 卡五・通解",
    ],
    note="先分類、再動筆——選對卡才開始計算。",
)

# 6. 過渡頁1
db.add_transition(
    prs,
    "五張卡都認識了\n接下來看三個最容易出錯的地方",
    FOOTER,
)

# 7. 迷思澄清
db.add_misconception(
    prs, FOOTER, "最常見的三個錯法",
    [
        dict(wrong="開根號後直接當作正數", right="開根號只得大小，正負要另查象限"),
        dict(wrong="cos(α±β)正負跟sin公式一樣", right="cos中間符號與括號相反，sin才一樣"),
        dict(wrong="sin與cos通解公式寫法一樣", right="sin配(-1)ⁿ、cos配±，兩者不同"),
    ],
)

# 8. 2x2 視覺鷹架：卡三完整範例（求cos105°）
db.add_scaffold_2x2(
    prs, FOOTER, "範例：求 cos105° 完整解一次",
    "求 cos105° 的值（105°不是特殊角）",
    what="求cos105°的值\n（拆成兩個\n特殊角）",
    given="105°=60°+45°\n用cos(α+β)公式",
    strategy="cos60°cos45°\n-sin60°sin45°\n=½×√2/2-√3/2×√2/2\n=(√2-√6)/4",
    check="105°在第二象限\ncos應該是負的\n√2<√6，答案確\n實是負數 ✔",
)

# 9. 步驟卡：自己動手時的動作
db.add_step_card(
    prs, FOOTER, "自己動手時的四個動作",
    [
        "先讀題，判斷屬於五類中的哪一類",
        "翻對提示卡，找出對應的觸發條件與公式",
        "代入數值：留意正負號要另外用卡二核對",
        "檢查結果：套用sin²+cos²=1或看象限",
    ],
    note="選對提示卡是這一課的關鍵，不是計算本身難。",
)

# 10. 過渡頁2
db.add_transition(
    prs,
    "熟習五張卡之後\n輪到你自己動手做練習",
    FOOTER,
)

# 11. 練習講解：練習A・第1題
db.add_practice_explain(
    prs, FOOTER, "練習A・第1題．老師示範",
    "直角△ABC，∠C=90°，AC=6、BC=8，求AB與sinA/cosA/tanA",
    [
        "看∠A：對邊BC=8，鄰邊AC=6",
        "先求斜邊AB=√(6²+8²)=√100=10",
        "sinA=8/10=4/5，cosA=6/10=3/5",
        "tanA=8/6=4/3（對邊/鄰邊）",
    ],
    note="sinB=3/5=cosA，因為∠B的對邊=∠A的鄰邊。",
)

# 12. 分層任務
db.add_tiered_task(
    prs, FOOTER, "分層任務．練習A／B／C",
    [
        dict(star=1, label="練習A",
             problem="求cos75°的值\n提示：75°=45°+30°\n翻卡三代公式\n手順卡在旁邊備查"),
        dict(star=2, label="練習B",
             problem="已知cosθ=-3/5\nθ∈(π/2,π)\n求sinθ與tanθ\n提示：卡二定正負\n再代sin²+cos²=1"),
        dict(star=3, label="練習C",
             problem="求sin105°、cos105°\n再用二倍角求sin210°\n並用另一方法驗證\n提示：卡三→卡四\n連續換兩張卡"),
    ],
)

# 13. 總結頁
db.add_summary(
    prs,
    "看到三角函數題，先問：\n這是哪一類？該翻哪張卡？",
    "五張卡：六個比、象限、\n和角差角、二倍角、通解。\n開根號後記得定正負。",
    FOOTER,
)

out_path = os.path.join(os.path.dirname(__file__), "簡報_三角函數_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
