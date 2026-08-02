# -*- coding: utf-8 -*-
"""資源班簡報：第5章 L17 空間推理。主設計 D7 提示卡（相對面法則／翻滾方向法則）
＋輔助 D5 圖文雙軌對照。本課題庫原題僅3條且缺圖，經使用者同意全部自編同型新題
（詳見同資料夾《驗算_空間推理.md》§0）。呢類題目嘅瓶頸唔係計算，係「空間心像
操作」——腦入面摺紙／轉正方體，認知負荷極高。簡報用兩張可長期查閱嘅提示卡
代替腦內模擬，兩個完整範例分別示範相對面法則同翻滾方向法則點套用。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_deck_shared"))
import deck_builder as db

SUBJECT = "高三數學"
UNIT = "第5章 數理邏輯(三)．L17 空間推理"
FOOTER = f"{SUBJECT}．{UNIT}．資源班課堂簡報"

prs = db.new_presentation()

# 1. 封面
db.add_cover(prs, SUBJECT, "空間推理", "資源班課堂教學．相對面／翻滾提示卡", FOOTER)

# 2. 流程預告
db.add_flow_preview(prs, FOOTER, "今天要做的四件事", [
    "先想一想：一個摺紙謎題考起你",
    "認識兩張提示卡：相對面／翻滾方向",
    "完整範例，圖文對照走一次",
    "換你做：練習A／B／C，鷹架逐層減",
])

# 3. 問題引入
db.add_question_intro(prs, FOOTER, "先想一想",
    "十字形展開圖，六個面標住\n頂／左／前／右／後／底。\n摺成正方體，邊個面同「前」相對？",
    ["左面", "後面", "底面"],
    "提示：諗吓摺紙嗰陣，邊兩個面永遠見唔到對方。")

# 4. CRA①：完整範例（相對面法則）
db.add_cra(prs, FOOTER, "範例完整走一次：相對面法則",
    concrete={"label": "①睇展開圖", "desc": "頂B\n左A前C右D後E\n底F\n橫排：A-C-D-E"},
    representational={"label": "②數位置", "desc": "橫排 A-C-D-E\n對應位置1,2,3,4\n前C係第2位"},
    abstract={"label": "③套用法則", "desc": "位置差＝2嘅\n兩格係相對面\n第2位同第4位\n(C同E)相對\n答案：後E"})

# 5. 步驟卡：題型分類
db.add_step_card(prs, FOOTER, "呢類題目點分類：揀邊張卡", [
    "見到「展開圖」摺正方體 → 查提示卡①相對面",
    "見到正方體「滾一下」→ 查提示卡②翻滾方向",
    "滾多過一次 → 逐步更新六面狀態，一步步嚟",
], note="唔識揀邊張卡？睇題目有冇「展開圖」定「滾」呢個字。")

# 6. 過渡頁
db.add_transition(prs, "接下來，拆解\n最常見嘅撞板位", FOOTER)

# 7. 迷思澄清
db.add_misconception(prs, FOOTER, "常見錯法對照", [
    {"wrong": "諗住相鄰嘅格就係相對面", "right": "相隔一格先係相對面，唔係貼住嗰格"},
    {"wrong": "滾嘅時候前後兩面都跟住變", "right": "向左右滾，前／後兩面唔會變"},
    {"wrong": "滾兩次諗埋一齊，跳過中間果步", "right": "滾兩次要分兩步，逐步更新先啱"},
])

# 8. 2x2 視覺鷹架：另一個範例（翻滾方向法則）
db.add_scaffold_2x2(prs, FOOTER, "另一個範例：翻滾方向點做",
    problem="頂B 前C 右D 左A 後E 底F\n向右滾一下，新頂面係邊個？",
    what="問乜？\n向右滾一下\n之後嘅\n新頂面係邊個",
    given="已知六面：\n頂B 前C 右D\n左A 後E 底F",
    strategy="查提示卡②\n「向右滾」：\n左→頂\n原本左面＝A",
    check="新頂面＝A\n核對：前後不變，\n前仍係C，\n同原本一致✓")

# 9. 步驟卡：自己動手時的四個動作
db.add_step_card(prs, FOOTER, "自己動手時的四個動作", [
    "睇清楚題目係「展開圖」定「滾方向」",
    "展開圖題：數清楚橫排／直排邊格相隔一格",
    "滾方向題：揭提示卡②，跟住循環表填",
    "滾多過一次：填一次狀態表，先再滾下一次",
], note="唔識分？記住：有摺紙圖用卡①，講「滾」用卡②。")

# 10. 過渡頁
db.add_transition(prs, "最後，進入練習\n老師陪你做第一題", FOOTER)

# 11. 練習講解
db.add_practice_explain(prs, FOOTER, "練習A 第1題．老師示範",
    problem="A1．頂2/左1-前3-右4-後5/底6\n邊個面同「1」相對？",
    steps=[
        "橫排係 1－3－4－5，對應位置1,2,3,4",
        "「1」喺第1位，位置差2 → 睇第3位",
        "第3位係「4」",
        "答案：4",
    ],
    note="易錯：唔可以淨係睇邊，要數返實際位置差")

# 12. 分層任務
db.add_tiered_task(prs, FOOTER, "換你做：練習A／B／C", [
    {"star": 1, "label": "練習A", "problem": "A2．同一十字形展開圖\n頂2/左1-前3-右4-後5/底6\n邊個面同「2」相對？\n\n鷹架：提示卡①可查閱"},
    {"star": 2, "label": "練習B", "problem": "B2．頂2 前3 右4\n左1 後5 底6\n向前滾一下，新頂面？\n\n鷹架：提示卡②循環表"},
    {"star": 3, "label": "練習C", "problem": "C1．同一正方體，先向右\n滾一下，再向前滾一下，\n最終嘅頂面係邊個？\n\n鷹架：自己填狀態表，\n冇額外提示"},
])

# 13. 總結
db.add_summary(prs,
    takeaway="摺紙睇相隔格，\n滾動查循環表，\n心入面唔使諗晒。",
    floor_version="見到展開圖，\n數位置差；見到\n「滾」，查提示卡。",
    footer_text=FOOTER)

out_path = os.path.join(os.path.dirname(__file__), "簡報_空間推理_資源班版.pptx")
db.save(prs, out_path)
print("OK", out_path)
