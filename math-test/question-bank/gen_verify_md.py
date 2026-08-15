# -*- coding: utf-8 -*-
import json

with open("questions_MOCK1.json", encoding="utf-8") as f:
    data = json.load(f)

# mapping MOCK1 sequence -> original question number in 綜合模擬試題1.md
orig_nums = [15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,
             32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,
             48,49,50,51,52,53,54,55,56,57,58,
             59,60,61,62,63,64,65,66,67,68,
             69,70,71,72,73,74,75,76,
             77,78,79,80,81,82,
             83,84,85,86,87,88,89,90,
             91,92,93,94,96]

assert len(orig_nums) == len(data), (len(orig_nums), len(data))

lines = []
lines.append("# 驗算_綜合模擬試題1")
lines.append("")
lines.append("> 逐題重算紀錄，對應 `question-bank/questions_MOCK1.json`。來源：`math-test/綜合模擬試題1.md`（IQ/公職邏輯推理題型為主，11頁）。")
lines.append("> id前綴 MOCK1-001~079，對應原稿題號見下方各題標題（原稿無題31、缺題18與95的題幹，已略過，詳見文末說明）。")
lines.append("> answer_status三態：有答案待校對(原稿已有答案,已重算核實)／無答案待生成(原稿只有題幹或本次重算與原稿不同,答案由本次驗算生成/訂正)。")
lines.append("")

discrepancies = []
gaps_visual = []
taxonomy_gaps = []
corrections = []

for q, on in zip(data, orig_nums):
    lines.append(f"## {q['id']}（原稿題{on}，{q['subtype']}，{q['source_page']}）")
    lines.append("")
    lines.append(f"題目：{q['question_stem']}")
    lines.append("")
    if q['options']:
        lines.append("選項：" + "　".join(q['options']))
        lines.append("")
    lines.append(f"**答案：{q['answer']}**　｜　狀態：{q['answer_status']}")
    lines.append("")
    lines.append(f"驗算：{q['solution']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    blob = q['answer_status'] + q['solution']
    if "不符" in blob:
        discrepancies.append((q['id'], on))
    if "圖形依賴" in blob or "未能獨立" in blob:
        gaps_visual.append((q['id'], on))
    if q['subtype'] in ("B6", "C4"):
        taxonomy_gaps.append((q['id'], on, q['subtype']))
    if "訂正" in q['solution'] or "OCR" in q['solution']:
        corrections.append((q['id'], on))

lines.append("## 附錄：原稿缺題與taxonomy缺口說明")
lines.append("")
lines.append("**原稿缺失題號（跳過，未生成對應MOCK1題目）：**")
lines.append("- 題31：原稿本身已於題30後、題32前註明「原稿題號由30跳至32，無題號31」，答案表對應欄亦空白，非缺失而是原稿本身不存在此題號。")
lines.append("- 題18：原稿題17（p00）與題19（p01）之間無題18的題幹內容（僅答案表列出「18.B」），研判為原稿掃描/轄錄時漏失該頁局部內容，無法在無題幹依據下合理重建整題，故未生成對應題目，僅在此提示教師如需題18內容須覆核原始掃描PDF（`math-test\\檔案_000` zip內對應頁面）。")
lines.append("- 題95：原稿題94（p10）與題96之間無題95的題幹內容（僅答案表列出「95.B」），情況與題18相同，未生成對應題目。")
lines.append("")
lines.append(f"**taxonomy缺口（新開代碼，共{len(set(t[2] for t in taxonomy_gaps))}個新代碼）：**")
lines.append("- 語文理解與邏輯推理 **C4 親屬關係推理**：原定案清單C1-C3未涵蓋純親屬稱謂鏈式推理題型（本卷題14、15、57、58即MOCK1-014、015、057、058），已依原定案「發現新題型自行開代碼」原則新增。")
lines.append("- 數理邏輯 **B6 一般常識/軟體操作**：本卷題82（MOCK1-066）為Microsoft PowerPoint操作常識題，不屬於數學運算或邏輯推理，亦不屬語文理解，已新開代碼標註，建議日後檢視是否需要獨立於三大domain之外的第四類別，或維持歸入數理邏輯之下作為特例。")
lines.append("")
lines.append(f"**圖形/表格版面依賴、文字轉錄無法唯一還原運算規則的題目（共{len(gaps_visual)}題，已依規則2標註限制並保留原稿答案）：**")
for i, on in gaps_visual:
    lines.append(f"- {i}（原稿題{on}）")
lines.append("")
lines.append(f"**自行補充/訂正原稿缺陷之題目（共{len(corrections)}題）：**")
for i, on in corrections:
    lines.append(f"- {i}（原稿題{on}）")
lines.append("")
lines.append(f"**親自重算後與原稿答案表不一致之題目（共{len(discrepancies)}題，已於各題solution詳列驗算過程，answer欄採本次重算結果）：**")
for i, on in discrepancies:
    lines.append(f"- {i}（原稿題{on}）")
lines.append("")

with open("../驗算_綜合模擬試題1.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("discrepancies:", len(discrepancies))
print("visual gaps:", len(gaps_visual))
print("corrections:", len(corrections))
print("taxonomy gap items:", len(taxonomy_gaps))
