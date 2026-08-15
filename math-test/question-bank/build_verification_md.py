# -*- coding: utf-8 -*-
"""產生 驗算_綜合題型1.md，逐題列出題目/選項/答案/驗算過程，對應 questions_COMP1.json。"""
import json

JSON_PATH = r"C:\Users\KongChiLok\notebookLM\math-test\question-bank\questions_COMP1.json"
OUT_PATH = r"C:\Users\KongChiLok\notebookLM\math-test\驗算_綜合題型1.md"

HEADER = """# 驗算_綜合題型1

> 逐題重算紀錄，對應 `question-bank/questions_COMP1.json`。來源：`綜合題型1（a）.md`（題目67–150，第72、73、96–98題原稿未轄錄）＋`綜合題型1（b）.md`（119–150題解答）。
> 已知缺口：題號1–66僅在解答總表出現、無題目文字，本輪全部跳過。第72、73、96–98、100、119、135、138題連題目文字都搵唔到（100、119、135、138為本輪處理時新發現嘅缺口，原稿備註只列出72、73、96–98）。
> 每題答案已由本人重新獨立驗算，唔盲信原稿手寫圈選或解答總表；驗算後發現原稿解答有誤之處已在對應題目下方註明並訂正（合共4題：對應原題號112、131、142、149）。
> 圖形規律推理題（原稿以圖片呈現）已按轉錄文字描述之圖案關係重新推導，惟本質上仍為視覺判斷，信心略低於純數字/代數題目。

---

"""


def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    lines = [HEADER]
    for q in data:
        lines.append(f"## {q['id']}（{q['subtype']}，{q['source_page']}）\n\n")
        lines.append(f"題目：{q['question_stem']}\n\n")
        if q["options"]:
            lines.append("選項：" + "　".join(q["options"]) + "\n\n")
        lines.append(f"**答案：{q['answer']}**　｜　狀態：{q['answer_status']}\n\n")
        lines.append(f"驗算：{q['solution']}\n\n")
        lines.append("---\n\n")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Wrote {len(data)} entries to {OUT_PATH}")


if __name__ == "__main__":
    main()
