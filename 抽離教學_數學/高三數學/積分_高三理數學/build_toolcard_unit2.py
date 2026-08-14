# -*- coding: utf-8 -*-
# 工具卡（D2 手順卡，可剪下放桌面）—— 定積分
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))

card = step_card(
    '求定積分的四個步驟',
    [
        ('求原函數——套不定積分公式卡，不用加C', 'C 在相減時會自動抵消，加了也沒意義，不用寫'),
        ('代入上限——把上限的數代入原函數，算出 {F(b)}', '代錯數字，尤其上下限是負數時'),
        ('代入下限——把下限的數代入原函數，算出 {F(a)}', '代錯數字，尤其上下限是負數時'),
        ('相減——{F(b)−F(a)}，就是答案（牛頓－萊布尼茲公式：{∫[a,b] f(x)dx=F(b)−F(a)}）', '減反了（下限減上限），或漏看負號'),
    ],
    trigger='題目要求「求定積分」或「求某圖形面積」時（13.3、13.4）',
    fading='完整版（本卡）→只留關鍵詞清單（求原函數/代上限/代下限/相減）→只留「這題有四步」提示→完全移除',
)

# 同一張卡印兩份，用虛線（裁切線）上下排列，方便剪下：一份自己用、一份可借同學或備用
# cols=1：step_card() 本身固定用整頁寬度排版，toolcard_sheet 若用 cols=2 會把它硬塞進半頁寬，
# 造成內容溢出、文字重疊（不定積分工具卡實測踩過的坑，這裡直接沿用修正後的做法）。
P = [toolcard_sheet([[card], [card]], cols=1)]

out = build_docx(P, os.path.join(OUT, '工具卡_定積分手順卡.docx'), footer_text='高三數學．定積分單元（工具卡）')
print(out)
