# -*- coding: utf-8 -*-
"""
高三數學．第4章 數理邏輯(二)．L16 圖形規律推理　資源班課堂簡報
主設計：D5 圖文雙軌對照（逼學生將圖案視覺轉變逐格寫成一句文字描述）
輔助設計：D11 標記對應法（①②③④ 圖與文字描述扣連，避免「睇緊呢格、講緊嗰格」錯位）
選用理由：呢類題目唔屬於 S1~S10 既有數學結構，真正瓶頸係「睇得出圖但講唔出規律」——
　　學生可以憑直覺揀啱答案，但講唔出轉變邏輯，換一條類似題就撞唔中。
內容全部取材自同資料夾《講義_圖形規律推理_抽離小班共用版.html》同
《練習_圖形規律推理_抽離小班共用版.html》嘅實際文字（圖形題以文字描述呈現）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第4章 數理邏輯(二)．L16 圖形規律推理"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "L16 圖形規律推理",
             "資源班課堂簡報．D5 圖文雙軌對照＋D11 標記對應", FOOTER)

# 2. 流程預告（F5 課前流程預告：今日規則「一次淨係比較相鄰兩格」）
db.add_flow_preview(prs, FOOTER, "今日要做的四件事", [
    "睇一條規律題，唔靠感覺猜",
    "學識將圖案變化講成一句話",
    "跟雙軌表，一格一格自己試",
    "分層練習：A／B／C 三種難度",
])

# 3. 問題引入（取自講義範例：三角形→四邊形→五邊形→？，全部空心）
db.add_question_intro(
    prs, FOOTER, "先感覺一下：格④係咩？",
    "①三角形→②四邊形→③五邊形→④？\n（全部空心，邊數有規律？）",
    ["六邊形（空心）", "六邊形（實心）", "五邊形（空心，唔變）"],
    "唔使急揀，一陣間學識點樣有根據咁揀。",
)

# 4. CRA三欄鷹架①：分析步驟示範（D5 圖文雙軌對照的三步驟）
db.add_cra(
    prs, FOOTER, "分析步驟：由「感覺」到「講得出」",
    concrete=dict(label="① 逐格編號",
                  desc="四格圖案\n編號①②③④\n由第一格開始睇"),
    representational=dict(label="② 只比較相鄰兩格",
                           desc="由①到②\n邊度變咗\n一次淨係諗一步"),
    abstract=dict(label="③ 講成一句話",
                  desc="例如「邊數\n每格 +1」\n套用到④嘅答案"),
)

# 5. 步驟卡：圖案規律常見嘅變化類型（取材自練習A/B/C出現嘅四類變化）
db.add_step_card(
    prs, FOOTER, "圖案規律常見嘅變化類型",
    [
        "數量：每格幾多個，點樣加減",
        "方向：箭嘴／圖形每格轉幾多度",
        "邊數：三角形→四邊形→五邊形…",
        "填色：空心／實心，有冇交替",
    ],
    note="留意：有啲題目唔止一種變化同時發生！",
)

# 6. 過渡頁（轉換點1）
db.add_transition(prs, "睇得出唔代表講得出\n下一步：拆解常見嘅諗錯位", FOOTER)

# 7. 迷思澄清（取自參考答案「易錯點提示」）
db.add_misconception(prs, FOOTER, "呢啲諗法你有冇中過？", [
    dict(wrong="感覺啱就直接揀答案", right="逐格講出邊度變咗先揀"),
    dict(wrong="淨係跟到一種變化就收工", right="檢查仲有冇第二種變化"),
    dict(wrong="兩排圖案用同一條規律", right="上下兩排要分開睇規律"),
])

# 8. 2x2 視覺鷹架②：另一個完整例子（邊數＋填色同時變，練習B第3題型）
db.add_scaffold_2x2(
    prs, FOOTER, "邊數同填色可能同時變，格④係咩？",
    problem="四格圖案：邊數同填色都可能變，格④係咩？",
    what="問乜嘢：\n格④嘅邊數\n同填色分別\n係咩？",
    given="已知：\n邊數逐格+1\n填色空心／實心\n交替出現",
    strategy="策略：\n邊數：跟 +1\n填色：跟交替\n兩條分開跟",
    check="驗算：\n5+1=6條邊\n交替到實心\n答：實心六邊形",
)

# 9. 步驟卡：自己動手時的檢查動作（取自講義 selfcheck 清單）
db.add_step_card(
    prs, FOOTER, "自己動手時嘅4個檢查動作",
    [
        "逐格編號①②③④，由第一格開始睇",
        "淨係比較相鄰兩格，唔好一次睇成串",
        "如果有兩種變化，兩種都要分開講",
        "答案畫得出嚟，或者講得出係咩形狀",
    ],
)

# 10. 過渡頁（轉換點2）
db.add_transition(prs, "識規律、識檢查\n落嚟自己試三種難度", FOOTER)

# 11. 練習講解頁◆（練習A 第1題：實心圓點數量規律）
db.add_practice_explain(
    prs, FOOTER, "老師示範：練習A 第1題",
    problem="①1粒→②2粒→③3粒→④？粒　實心圓點",
    steps=[
        "逐格編號，由①睇到④",
        "①到②：1粒→2粒，多咗1粒",
        "②到③：2粒→3粒，都係多1粒",
        "規律：每格 +1（唔係 ×2）",
        "④＝3+1＝4粒實心圓點",
    ],
    note="易錯：以為係 ×2，其實係固定 +1",
)

# 12. 分層任務◆（練習A/B/C 各挑一題代表性題目）
db.add_tiered_task(prs, FOOTER, "分層任務：揀返你嘅難度", [
    dict(star=1, label="練習A",
         problem="箭嘴方向：\n①上②右③下④？\n提示：順時針轉\n雙軌表已填一半"),
    dict(star=2, label="練習B",
         problem="邊數＋填色\n可能同時變\n④係咩形狀？\n雙軌表得標題"),
    dict(star=3, label="練習C",
         problem="箭嘴數量同方向\n都可能變\n④有幾支、指邊？\n冇雙軌表，自己講"),
])

# 13. 總結頁
db.add_summary(
    prs,
    takeaway="識睇圖唔夠，仲要識埋一句話講出規律",
    floor_version="起碼要講到：呢格同上一格，邊度唔同、點樣唔同。",
    footer_text=FOOTER,
)

out_path = os.path.join(os.path.dirname(__file__), "簡報_圖形規律推理_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
