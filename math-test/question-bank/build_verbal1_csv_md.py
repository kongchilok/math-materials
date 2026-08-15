# -*- coding: utf-8 -*-
import json, csv, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("questions_VERBAL1.json", encoding="utf-8") as f:
    data = json.load(f)

# ---------- CSV ----------
fields = ["id","domain","subtype","question_type","difficulty","question_stem",
          "options","answer","solution","answer_status","source_file","source_page","review_status"]
with open("questions_VERBAL1.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for q in data:
        row = dict(q)
        row["options"] = " | ".join(q["options"]) if q["options"] else ""
        w.writerow(row)

print("CSV written:", len(data), "rows")

# ---------- 驗算 markdown ----------
lines = []
lines.append("# 驗算_公職統考-中文邏輯題型1")
lines.append("")
lines.append("> 逐題重算紀錄，對應 `question-bank/questions_VERBAL1.json`。來源：`math-test/公職統考-中文邏輯題型1.md`（澳拓昇學/明昇教育中心公職統考中文邏輯推理題型，15頁，51題）。")
lines.append("> id前綴 VERBAL1-001~051，對應原稿題號1~51（連續無缺號）。domain全部為「語文理解與邏輯推理」，subtype見各題標題。")
lines.append("> answer_status二態：有答案待校對(原稿已有答案key或詳解，已逐題親自重算核實)／無答案待生成(原稿無答案，由本次驗算生成)——本卷51題原稿皆有答案（第1題見p14另附詳解，第2~51題見p14末「答案總表」僅列字母），故全部屬「有答案待校對」。")
lines.append("> **重要**：本卷每題均由本次驗算親自逐一推演邏輯過程（非抄答案表字母），詳見各題「驗算」欄；與原稿答案表不符者已在該題內詳列真值表/矛盾分析並記錄判斷，另彙整於文末「重算後與原稿不符」清單。")
lines.append("")

subtype_names = {
    "C1": "命題邏輯", "C2": "類比推理", "C3": "論證評估", "C4": "定義判斷（新增代碼）",
}

discrepancies = []
new_subtypes = set()
diff_counts = {}

for q in data:
    diff_counts[q["subtype"]] = diff_counts.get(q["subtype"], 0) + 1
    lines.append(f"## {q['id']}（原稿題{int(q['id'].split('-')[1])}，{q['subtype']} {subtype_names.get(q['subtype'],'')}，{q['source_page']}）")
    lines.append("")
    lines.append(f"題目：{q['question_stem']}")
    lines.append("")
    if q["options"]:
        lines.append("選項：" + "　".join(q["options"]))
        lines.append("")
    lines.append(f"**答案：{q['answer']}**　｜　狀態：{q['answer_status']}")
    lines.append("")
    lines.append(f"驗算：{q['solution']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    if "重算後與原稿不符" in q["answer_status"]:
        discrepancies.append(q["id"])
    if q["subtype"] == "C4":
        new_subtypes.add(q["id"])

lines.append("## 附錄一：taxonomy缺口與新增代碼")
lines.append("")
lines.append("原定案清單C1命題邏輯／C2類比推理／C3論證評估未能涵蓋「給定一段抽象定義、要求判斷哪個具體案例符合該定義」這類題型（本卷第31、33、35、45題，即VERBAL1-031、033、035、045），已依原定案「發現新題型自行開代碼」原則新增：")
lines.append("")
lines.append("- 語文理解與邏輯推理 **C4 定義判斷**：給定一段抽象/專業定義，要求判斷哪個具體案例符合（或不符合）該定義，屬公職考試常見的「定義判斷」大題型，與命題邏輯（真假話推理）、類比推理（詞語關係）、論證評估（削弱/支持）三者性質皆不同，故新開代碼。本卷共4題屬此類型：VERBAL1-031（政策性虧損）、VERBAL1-033（心理契約）、VERBAL1-035（印記學習）、VERBAL1-045（能力補償-輻射補償）。")
lines.append("")

lines.append("## 附錄二：domain/subtype分布統計")
lines.append("")
lines.append("全卷51題domain皆為「語文理解與邏輯推理」，subtype分布：")
lines.append("")
for st in sorted(diff_counts):
    lines.append(f"- {st}（{subtype_names.get(st,'')}）：{diff_counts[st]}題")
lines.append("")

lines.append(f"## 附錄三：親自重算後與原稿答案表不符之題目（共{len(discrepancies)}題）")
lines.append("")
lines.append("以下題目本次親自逐步推演命題邏輯（真值表/矛盾分析）後，得出的答案與原稿p14答案總表所列字母不一致。已在各題solution欄詳列完整推導過程與矛盾點，並基於邏輯推導的嚴謹性（可用真值表反例驗證）採用本次重算結果，同時保留原稿答案供教師覆核判斷：")
lines.append("")
for did in discrepancies:
    q = next(x for x in data if x["id"] == did)
    orig_map = {"VERBAL1-021":"B","VERBAL1-022":"A","VERBAL1-041":"D"}
    on = orig_map.get(did, "?")
    lines.append(f"- **{did}**（原稿題{int(did.split('-')[1])}）：本次重算答案＝**{q['answer']}**；原稿答案表列＝**{on}**。判斷：採信本次重算結果，理由詳見該題solution欄之真值表/等價轉換推導（三題性質相近，均涉及「除非…否則…」「只有…才…」等必要/充分條件句式的等價轉換，重算時特別注意避免「逆命題」「否定前件/肯定後件」等常見謬誤陷阱；原稿答案表僅為YOUTUBE影片解說對應之字母清單、未附推導過程，不排除原答案本身受此類陷阱影響，建議教師依教學需要自行覆核或以此作為課堂上「必要/充分條件轉換」的辨析教材）。")
lines.append("")

lines.append("## 附錄四：第1題特別說明")
lines.append("")
lines.append("原稿p14末「答案總表」明確標註範圍為「第2題至第51題」，第1題不在此表內；但原稿p14另段落已針對第1題給出完整詳解（矛盾句配對法）與答案D，本次重算已核對該詳解邏輯自洽且與重算結果一致，answer_status標註「原稿p14另頁有完整詳解，已重算驗證一致」。")
lines.append("")

lines.append("## 附錄五：本次未發現的缺陷類型")
lines.append("")
lines.append("本卷51題題幹與選項完整度良好，僅第24題（VERBAL1-024）文字段落有OCR重複/錯字瑕疵（「小票」疑為「小王」之重複衍字），已於該題solution欄註明並提出合理訂正解讀，不影響條件鏈推導與最終答案；其餘題目未發現需要另行合理補充/訂正的原稿缺陷。")
lines.append("")

with open("../驗算_公職統考-中文邏輯題型1.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("MD written. discrepancies:", discrepancies)
print("subtype distribution:", diff_counts)
