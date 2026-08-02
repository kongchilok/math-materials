# -*- coding: utf-8 -*-
"""資源班簡報：第1章 L2 利潤折扣與費率。主設計 D1（前後變化型＋階梯分段型）＋輔助 D8/D14。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第1章 特殊數學應用專題．L2 利潤、折扣與費率階梯"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

db.add_cover(prs, SUBJECT, "利潤、折扣與費率階梯", "資源班課堂教學．基準量條形圖法", FOOTER)

db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "猜猜「先打8折再減10%」等於打幾折",
    "學條形圖的前後變化畫法",
    "找出這個百分比是拿誰當100%",
    "老師陪你做第一題練習",
])

db.add_question_intro(prs, FOOTER, "先想一想",
    "定價 500 元，先打 8 折，\n再從打折後的價錢減價 10%。\n這樣等於原價打幾折？",
    ["70 折", "72 折", "90 折"],
    "等一下我們用條形圖，把「基準換了」畫出來就知道答案。")

db.add_cra(prs, FOOTER, "從實物到算式：基準換了幾次",
    concrete={"label": "具體", "desc": "電風扇進價 250 元。\n\n店主按進價加價40%定出標價，\n再按標價打八折出售。\n\n問：店主每部賺多少元？"},
    representational={"label": "表徵（前後變化）", "desc": "進價畫一整條＝100%。\n\n標價＝進價再接長 40%。\n\n售價＝標價的80%，\n畫比標價短一點的一條。"},
    abstract={"label": "抽象（算式）", "desc": "標價 = 250×1.4 = 350\n\n售價 = 350×0.8 = 280\n\n賺 = 280−250 = 30（元）"})

db.add_step_card(prs, FOOTER, "先問一句：這個 % 是拿誰當100%？", [
    "題目說「打折」→ 基準是定價（標價）",
    "題目說「加價／加成」→ 基準是進價（成本）",
    "題目說「利潤率」→ 基準是進價，不是售價！",
], note="一題出現兩個百分比，就要問兩次、圈兩次基準。")

db.add_transition(prs, "接下來，看三個\n最容易寫錯的算式", FOOTER)

db.add_misconception(prs, FOOTER, "三個容易踩錯的陷阱", [
    {"wrong": "先打8折再減10% ＝ 打(20%+10%)＝70折", "right": "要連乘：0.8×0.9＝0.72，即72折"},
    {"wrong": "利潤是進價20% → 利潤＝售價×0.2", "right": "利潤率分母是進價：利潤＝進價×0.2"},
    {"wrong": "打八折 → 售價＝定價×0.2", "right": "八折＝付原價80%：售價＝定價×0.8"},
])

db.add_scaffold_2x2(prs, FOOTER, "範例：完整走一次",
    problem="電風扇進價250元，店主按進價加價40%定出標價，再按標價打八折出售。店主每部賺多少元？",
    what="店主每部賺多少元？",
    given="進價250元；加價40%定標價；標價打8折出售",
    strategy="標價 = 250×1.4 = 350\n售價 = 350×0.8 = 280",
    check="賺 = 280−250 = 30（元）\n驗算：1.4×0.8=1.12＝112%\n利潤率 30/250=12% ✓")

db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "圈基準量：問「這個%是拿誰當100%」（定價／進價／變化前）",
    "畫條：基準量畫一整條；有門檻（首N度）就切成幾段",
    "一次變化畫一條：兩次變化要相乘，不可以相加",
    "反推檢核：答案代回去求一次率或差，看是否等於題目給的數",
])

db.add_transition(prs, "進入練習，\n老師陪你做第一題", FOOTER)

db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="座地風扇定價800元，店慶全場先打八折，會員憑卡再減價5%。會員買一部實付多少元？",
    steps=[
        "打八折：800×0.8 = 640（元）",
        "會員再減5%（基準是打折後的640元）：640×0.95",
        "640×0.95 = 608（元）",
    ],
    note="⚠ 第二個5%的基準是「打折後的價」，不是原定價800元。")

db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "外套進價240元，店主想賺取進價35%的利潤，售價應定為多少元？\n\n（先圈基準量，再畫條形圖）"},
    {"star": 2, "label": "練習B", "problem": "定價500元，先打八折，再從打折後的價錢減價10%，售價是多少元？\n\n（自己畫兩次變化的條形圖）"},
    {"star": 3, "label": "練習C", "problem": "住宅用電階梯收費：首200度0.8元、201-400度1.1元、超過400度1.5元。用電520度，電費共多少？\n\n（自己切段計算）"},
])

db.add_summary(prs,
    takeaway="先問「這個%是拿誰當100%」，\n基準畫一整條，\n兩次變化要相乘。",
    floor_version="看到 % 先問「是誰的 %」，\n兩次折扣要相乘，不要相加。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_利潤折扣與費率_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
