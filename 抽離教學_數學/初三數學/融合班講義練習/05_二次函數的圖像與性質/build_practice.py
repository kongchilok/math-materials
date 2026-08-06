# -*- coding: utf-8 -*-
"""重建《練習_二次函數的圖像與性質_融合版》：忠實保留原有 8 題（含原有嵌入圖）
＋新增 3 題（練習A：平移辨識／練習C：一般式、交點式待定係數法），全部題號
與答案重新編號（原 1,2|3,4,5|6,7,8 → 新 1,2,3|4,5,6|7,8,9,10,11）。"""
import sys, os
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))
ORIG_IMG = os.path.join(HERE, '_orig_practice_img1.png')

P = []
P.append(masthead('初三數學', '二次函數的圖像與性質', '課堂練習'))
P.append(student_info_row())
P.append(para('提示：頂點式 {y=a(x-h)^2+k} 的頂點是 (h, k)、對稱軸 x=h。一般式先配方。'))

# ==================== 一、練習A ====================
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para('1．直接看頂點式，說出開口方向、對稱軸、頂點。（填空）'),
    para('（1）{y=2(x-1)^2+3}：開口＿＿，對稱軸 x=＿，頂點(＿, ＿)'),
    para('（2）{y=-(x+2)^2-1}：開口＿＿，對稱軸 x=＿，頂點(＿, ＿)'),
] + write_lines(2)))

P.append(problem_box([
    para('2．配方填空：把 {y=x^2-6x+5} 化頂點式。'),
    para('　{y=x^2-6x+＿-＿+5=(x-＿)^2-＿}，頂點(＿, ＿)'),
] + write_lines(2)))

P.append(problem_box([
    para('3．不用畫圖，直接寫出下列拋物線的頂點：'),
    para('（1）{y=x^2-5}　頂點(＿, ＿)'),
    para('（2）{y=(x+3)^2}　頂點(＿, ＿)'),
] + write_lines(2)))

# ==================== 二、練習B ====================
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para('4．把 {y=x^2+2x-3} 化頂點式，寫出開口方向、對稱軸、頂點，並求與 x 軸、y 軸的交點。'),
] + write_lines(5)))

P.append(image_para(ORIG_IMG, width_cm=7.5, caption='圖：某二次函數的圖像'))
P.append(problem_box([
    para('5．（如上圖）寫出這個二次函數圖像的頂點、對稱軸，並估計它與 x 軸的交點。'),
] + write_lines(4)))

P.append(problem_box([
    para('6．已知拋物線 {y=ax^2+bx+c} 的頂點是 (1, −4)，且經過點 (3, 0)，求 a、b、c。'),
] + write_lines(4)))

# ==================== 三、練習C ====================
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para('7．二次函數 {y=x^2-2x-3}。（1）化頂點式（2）畫草圖（標頂點、對稱軸、與坐標軸交點）'
         '（3）x 取何值時 y 有最小值？最小值是多少？'),
] + write_lines(5)))

P.append(problem_box([
    para('8．拋物線 {y=a(x-h)^2+k} 經過 (0, 3)、(2, 3)，且頂點的縱坐標是 1。求這條拋物線的解析式。'),
] + write_lines(4)))

P.append(problem_box([
    para('9．找錯題：小明把 {y=x^2-4x+3} 配方寫成 {y=(x-2)^2+3}。錯在哪裡？正確的頂點式是什麼？'),
] + write_lines(3)))

P.append(problem_box([
    para('10．過 (0, 2)、(1, 3)、(2, 8) 三點，求 {y=ax^2+bx+c}。'),
] + write_lines(5)))

P.append(problem_box([
    para('11．拋物線與 x 軸交於 (−1, 0)、(2, 0)，且過 (0, −4)，求解析式。'),
] + write_lines(4)))

# ==================== 參考答案（教師用） ====================
P.append(heading('參考答案（教師用）', page_break_before=True))

P.append(heading('練習A', sz=BODY_SZ))
P.append(para('1．(1) 開口向上，x=1，頂點(1, 3)　(2) 開口向下，x=−2，頂點(−2, −1)'))
P.append(para('2．{y=(x-3)^2-4}，頂點(3, −4)。'))
P.append(para('3．(1) 頂點(0, −5)　(2) 頂點(−3, 0)'))

P.append(heading('練習B', sz=BODY_SZ))
P.append(para('4．{y=(x+1)^2-4}；開口向上，對稱軸 x=−1，頂點(−1, −4)；與 x 軸 {(x+3)(x-1)=0} → '
              '(−3, 0)、(1, 0)；與 y 軸 (0, −3)。'))
P.append(para('5．頂點 (1, 4)，對稱軸 x=1，與 x 軸交點約 (−1, 0)、(3, 0)。'))
P.append(para('6．{y=a(x-1)^2-4}，過 (3, 0)：4a−4=0 → a=1；展開 {y=x^2-2x-3}，a=1, b=−2, c=−3。'))

P.append(heading('練習C', sz=BODY_SZ))
P.append(para('7．(1) {y=(x-1)^2-4}　(2) 頂點(1, −4)、對稱軸 x=1、與 x 軸 (−1, 0)(3, 0)、與 y 軸 (0, −3)'
              '　(3) x=1 時 y 有最小值 −4。'))
P.append(para('8．兩等高點 (0,3)、(2,3) 對稱，軸 x=1，h=1；頂點縱坐標 k=1；過 (0,3)：a+1=3 → a=2。{y=2(x-1)^2+1}。'))
P.append(para('9．配方時漏了常數：{(x-2)^2=x^2-4x+4}，要 −4+3=−1，正確 {y=(x-2)^2-1}。'))
P.append(para('10．c=2；a+b+c=3→a+b=1……①；4a+2b+c=8→2a+b=3……②；②−①：a=2；代回①：b=−1。{y=2x^2-x+2}。'))
P.append(para('11．設 {y=a(x+1)(x-2)}，代入(0,−4)：−4=a(1)(−2)=−2a → a=2。{y=2(x+1)(x-2)=2x^2-2x-4}。'))

out = build_docx(P, os.path.join(HERE, '練習_二次函數的圖像與性質_融合版.docx'),
                 footer_text='初三數學．二次函數的圖像與性質單元')
with open(os.path.join(HERE, '_build_out.txt'), 'w', encoding='utf-8') as f:
    f.write(out)
