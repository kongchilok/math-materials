# -*- coding: utf-8 -*-
"""資源班簡報：第1章 L3 行程、工程效率與濃度。主設計 D4 三欄式引導＋輔助 D1（僅相遇/稀釋）、D8。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第1章 特殊數學應用專題．L3 行程、工程效率與濃度"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

db.add_cover(prs, SUBJECT, "行程、工程效率與濃度", "資源班課堂教學．三欄式讀題法", FOOTER)

db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "猜猜兩車幾小時後相遇",
    "學三欄式讀題法：語意→關係式→運算",
    "認識三種情境各自的「不變量」",
    "老師陪你做第一題練習",
])

db.add_question_intro(prs, FOOTER, "先想一想",
    "甲乙兩地相距480公里，快車時速90公里、\n慢車時速70公里，同時相向而行。\n幾小時後兩車相遇？",
    ["3 小時", "6 小時", "4 小時"],
    "等一下我們用三欄表，把「不變的東西」找出來就知道答案。")

# 三欄鷹架①：行程（相遇）
db.add_cra(prs, FOOTER, "範例：三欄式完整走一次（行程）",
    concrete={"label": "①語意擷取", "desc": "已知：全程360公里。\n客車80km/h、貨車100km/h。\n同時相向而行。\n\n不變的是：\n兩車路程和 = 全程"},
    representational={"label": "②關係式建構", "desc": "路程 = 速度 × 時間\n\n相向而行，速度相加：\n合速度 = 80+100 = 180\n\n設相遇需時 t：\n80t + 100t = 360"},
    abstract={"label": "③運算與檢核", "desc": "180t = 360\nt = 2（小時）\n\n距甲地 = 80×2 = 160km\n\n驗算：160+200=360 ✓"})

db.add_step_card(prs, FOOTER, "三種情境，各自的「不變量」", [
    "相遇／追及：兩車路程「和」或「差」＝定值（全程／原本距離）",
    "工程效率：整項工程當作 1，各自效率＝1÷單獨完成天數",
    "濃度：加水或蒸發，溶質（鹽／糖）的質量始終不變",
], note="先找出這一題不變的是什麼，關係式就列得出來。")

db.add_transition(prs, "接下來，看三個\n最容易混淆的觀念", FOOTER)

db.add_misconception(prs, FOOTER, "三個容易混淆的觀念", [
    {"wrong": "追及問題也是「速度相加」", "right": "追及是同向：速度要相減；相遇才是相向，速度相加"},
    {"wrong": "兩隊合做天數＝兩人天數直接相加", "right": "效率（1÷天數）才能相加，天數不能直接加"},
    {"wrong": "濃度＝溶質質量 ÷ 溶劑（水）質量", "right": "濃度＝溶質 ÷（溶質＋溶劑），即溶質÷總溶液重量"},
])

# 三欄鷹架②：濃度
db.add_cra(prs, FOOTER, "範例：三欄式完整走一次（濃度）",
    concrete={"label": "①語意擷取", "desc": "已知：鹽水200克，濃度15%。\n加入50克清水。\n\n加入的是清水——\n沒有加鹽，也沒拿走鹽。\n\n不變的是：\n鹽（溶質）的質量"},
    representational={"label": "②關係式建構", "desc": "溶質 = 溶液 × 濃度\n\n鹽 = 200×0.15 = 30（克）\n這30克在加水後不變。\n\n新溶液 = 200+50 = 250\n新濃度 = 30÷250"},
    abstract={"label": "③運算與檢核", "desc": "30÷250 = 0.12\n即 12%\n\n檢核：250×0.12=30克 ✓\n\n加水只會讓濃度下降，\n15%→12%，合理"})

db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "圈已知、劃所求（第①欄）：把數字與問題分開圈出來",
    "找出這一題「不變的是什麼」，寫在①欄最下面",
    "列出三量關係式，代入已知數（第②欄）",
    "算出答案後代回檢核，看是否與題意相符（第③欄）",
])

db.add_transition(prs, "進入練習，\n老師陪你做第一題", FOOTER)

db.add_practice_explain(prs, FOOTER, "追及問題．老師示範",
    problem="小杰每分鐘走60公尺，小美每分鐘走80公尺。小杰先出發，5分鐘後小美從同一地點出發追他。多少分鐘追上？",
    steps=[
        "小杰先走5分鐘：60×5 = 300（公尺）——這是原本的距離",
        "追及問題，同向要用速度差：80−60 = 20（公尺/分）",
        "追及時間 = 300÷20 = 15（分鐘）",
        "追上時距出發點 = 80×15 = 1200（公尺）",
    ],
    note="⚠ 同向追及用速度「差」，相向相遇才用速度「和」。")

db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "有糖水300克，濃度20%，加入清水稀釋成12%。應加入多少克清水？\n\n（先算糖的質量，糖不會變）"},
    {"star": 2, "label": "練習B", "problem": "一項工程，甲隊15天完成，乙隊10天完成，兩隊一起做，多少天完成？\n\n（效率相加，不是天數相加）"},
    {"star": 3, "label": "練習C", "problem": "甲鹽水9%共5千克，與乙鹽水10千克混合成15%。乙鹽水的濃度是多少？\n\n（自己列式，鹽的總量不變）"},
])

db.add_summary(prs,
    takeaway="三量關係式先列出來，\n再找「什麼東西沒有變」。",
    floor_version="相遇看路程和、\n工程看效率、\n濃度看鹽不變。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_行程工程與濃度_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
