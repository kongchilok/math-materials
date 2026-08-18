# -*- coding: utf-8 -*-
"""修正《練習_二次函數與方程及應用_融合版.docx》第 C7、C8 題教師答案的推導方法。

背景：C7 原答案用「交點式」y=a(x−x₁)(x−x₂) 直接寫出 y=(x−1)(x+3)；C8 原答案用最值
捷徑公式 c−b²/4a 直接代數值。兩者都是本單元講義未教過的工具（教案已預留退讓方案：
「C7 可用交點式、C8 可用最值公式，未教過則改用配方硬做」）。

本補丁改用：
  C7 → 韋達定理（單元02 已教：x1+x2=−b/a，x1x2=c/a）
  C8 → 完整配方法（不用捷徑公式，逐步展示 a(x−2/a)²−4/a+c 的推導）

數值答案不變：b=2，c=−3，頂點(−1,−4)；a=1，c=−1。
只替換這兩段 <w:p>，其餘段落一個字不改。
"""
import os
import re
import shutil
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch_common import *      # noqa: F401,F403
from patch_common import para_start, guard

DOCX = os.path.join(HERE, '練習_二次函數與方程及應用_融合版.docx')

NEW_MARKER = '兩根和'
guard(DOCX, NEW_MARKER)

# ==================== 新答案文字（{} markup，鐵律1：一律 OMML） ====================
TXT_C7 = (
    '7．{(1,0)}、{(-3,0)} 是拋物線與 x 軸的交點，即 {1}、{-3} 是方程 {x^2+bx+c=0} 的兩根。'
    '兩根和 {1+(-3)=-2=-b}，得 {b=2}；兩根積 {1×(-3)=-3=c}，得 {c=-3}。'
    '頂點：{x=-b/2=-2/2=-1}，{y=(-1)^2+2×(-1)-3=-4}；頂點 {(-1,-4)}。'
)

TXT_C8 = (
    '8．圖像過 {(0,-1)}：{x=0} 時 {y=c}，得 {c=-1}。'
    '配方：{y=ax^2-4x+c=a(x^2-(4/a)x)+c}，繼續配方得 {y=a(x-2/a)^2-4/a+c}；'
    '{a>0} 時頂點即最小值，最小值 {=c-4/a}。'
    '代入已知：{c-4/a=-1-4/a=-5}，得 {-4/a=-4}，即 {a=1}。'
    '驗算：{a=1}、{c=-1} 時 {y=x^2-4x-1=(x-2)^2-5}，頂點 {(2,-5)}，'
    '且 {x=0} 時 {y=-1}，與題目條件相符。所以 {a=1}，{c=-1}。'
)

new_p7 = para(TXT_C7)
new_p8 = para(TXT_C8)

# ==================== 定位舊的 C7／C8 段落並整段替換 ====================
with zipfile.ZipFile(DOCX) as z:
    entries = {n: z.read(n) for n in z.namelist()}
xml = entries['word/document.xml'].decode('utf-8')

start7 = para_start(xml, '7．')                 # C7 答案段的唯一錨點（學生題目那邊的
                                                  # 「7．」跟其他文字同一個 run，不會撞號）
end7 = xml.index('</w:p>', start7) + len('</w:p>')
# C8 緊接在 C7 之後（沒有其他段落夾在中間）
assert xml.startswith('<w:p>', end7), 'C7 之後不是緊接 <w:p>，錨點假設有誤，要重新核對'
start8 = end7
end8 = xml.index('</w:p>', start8) + len('</w:p>')

old_span = xml[start7:end8]
assert '頂點 (−1, −4)' in old_span, \
    f'C7 舊答案錨點抓錯段落（沒有找到「頂點 (−1, −4)」）：{old_span[:200]!r}'
assert '所以 a=1，c=−1' in old_span, \
    f'C8 舊答案錨點抓錯段落（沒有找到「所以 a=1，c=−1」）：{old_span[-200:]!r}'

new_xml = xml[:start7] + new_p7 + new_p8 + xml[end8:]
entries['word/document.xml'] = new_xml.encode('utf-8')

bak = os.path.splitext(DOCX)[0] + '._tmp_before_c7c8fix.docx'
shutil.copy2(DOCX, bak)

with zipfile.ZipFile(DOCX, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, data in entries.items():
        z.writestr(name, data)

print('OK', DOCX)
print('備份：', bak)
