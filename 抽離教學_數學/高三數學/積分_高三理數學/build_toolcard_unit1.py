# -*- coding: utf-8 -*-
# 工具卡（D2 手順卡，可剪下放桌面）—— 不定積分
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))

card = step_card(
    '求不定積分的四個步驟',
    [
        ('拆項——看清楚這是幾項相加減', '漏看負號，尤其減法的第二項'),
        ('提係數——用常數倍法則，把係數整個提出來', '係數包含負號時要連負號一起提出'),
        ('套公式——對每一項查公式卡（第2～7條）', '冪函數公式的 n+1 算錯，尤其 n 是負數或分數時'),
        ('合併——把所有項加起來，最後只加一個C', '不要每項各加一個C，也不要漏加C'),
    ],
    trigger='題目是多項相加減的函數時（含13.2運算法則）',
    fading='完整版（本卡）→只留關鍵詞清單（拆項/提係數/套公式/加C）→只留「這題有四步」提示→完全移除',
)

# 同一張卡印兩份，用虛線（裁切線）排在同一頁，方便剪下：一份自己用、一份可借同學或備用
# 注意：step_card() 內部固定用整頁寬度排版，toolcard_sheet 若用 cols=2 會把它硬塞進半頁寬，
# 造成內容溢出、文字重疊（實測踩過）——手順卡這類「本身就是整頁寬表格」的卡片一律用 cols=1，
# 兩張卡上下疊放裁切，不要並排。
P = [toolcard_sheet([[card], [card]], cols=1)]

out = build_docx(P, os.path.join(OUT, '工具卡_不定積分手順卡.docx'), footer_text='高三數學．不定積分單元（工具卡）')
print(out)
