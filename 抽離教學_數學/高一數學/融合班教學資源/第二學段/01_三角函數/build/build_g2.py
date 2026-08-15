# -*- coding: utf-8 -*-
"""組② 誘導公式與三角函數的圖像性質（5.3–5.4）：講義＋練習"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

UNIT = '三角函數（二）誘導公式與圖像性質'
LEC_NAME = '講義_誘導公式與圖像性質_融合版_高一數學.docx'
PRA_NAME = '練習_誘導公式與圖像性質_融合版_高一數學.docx'
FOOTER = '高一數學．三角函數（二）誘導公式與圖像性質'

HALF_PI = F('π', '2')

# ============================================================ 講義
P = []
P.append(masthead('高一數學', UNIT, '課堂講義'))
P.append(student_info_row())

# ---- 概念一 為什麼需要誘導公式 ----
P.append(heading('一、誘導公式在做什麼？'))
P.append(para([T('我們只背熟了 30°、45°、60° 這些銳角的三角函數值。'
                 '誘導公式的工作，就是把「任意角」一步步變回「銳角」——'
                 '靠的是單位圓上的對稱。')]))
P.append(image_para(fig('fig3_誘導公式對稱.png'), width_cm=8.5,
                    caption='圖1：π−α、π+α、−α 的終邊，都是 α 終邊的對稱翻版'))

# ---- 概念二 公式表 ----
P.append(heading('二、誘導公式（分組記）'))
P.append(para([T('第1組（轉整圈，值不變）：'),
               M(mr('sin(2kπ + α) = sin α　cos(2kπ + α) = cos α　tan(2kπ + α) = tan α'))]))
P.append(para([T('第2組（π + α，關於原點對稱）：'),
               M(mr('sin(π + α) = −sin α　cos(π + α) = −cos α　tan(π + α) = tan α'))]))
P.append(para([T('第3組（−α，關於 x 軸對稱）：'),
               M(mr('sin(−α) = −sin α　cos(−α) = cos α　tan(−α) = −tan α'))]))
P.append(para([T('第4組（π − α，關於 y 軸對稱）：'),
               M(mr('sin(π − α) = sin α　cos(π − α) = −cos α　tan(π − α) = −tan α'))]))
P.append(para([T('第5組：'),
               M(mr('sin('), HALF_PI, mr(' − α) = cos α　　cos('), HALF_PI, mr(' − α) = sin α'))]))
P.append(para([T('第6組：'),
               M(mr('sin('), HALF_PI, mr(' + α) = cos α　　cos('), HALF_PI, mr(' + α) = −sin α'))]))
P.append(shaded_box([T('口訣「奇變偶不變，符號看象限」：看角前面是 π/2 的幾倍——'
                       '奇數倍就 sin、cos 互換（變），偶數倍不換（不變）；'
                       '正負號則把 α 當成銳角，看整個角落在哪個象限、原函數在那裡是正是負。')],
                    kind='hint'))

# ---- 概念三 特殊角值表 ----
P.append(heading('三、特殊角的值（必背）'))
P.append(problem_box([
    para([T('角度：　0°　　30°　　45°　　60°　　90°')]),
    para([T('sin：　'), M(mr('0　　'), F('1', '2'), mr('　　'),
          F(R('2'), mr('2')), mr('　　'), F(R('3'), mr('2')), mr('　　1'))]),
    para([T('cos：　'), M(mr('1　　'), F(R('3'), mr('2')), mr('　　'),
          F(R('2'), mr('2')), mr('　　'), F('1', '2'), mr('　　0'))]),
    para([T('tan：　'), M(mr('0　　'), F(R('3'), mr('3')), mr('　　1　　'),
          R('3'), mr('　　不存在'))]),
    para([T('記法：sin 由左到右遞增、cos 由左到右遞減；分母都是 2，'
            '分子依次是 √0、√1、√2、√3、√4。')]),
]))

# ---- 概念四 化簡三步流程 ----
P.append(heading('四、任意角求值三步流程'))
P.append(para([T('第1步　負角 → 正角：用第3組公式去掉負號。')]))
P.append(para([T('第2步　大角 → 一圈以內：減 360°（或 2π）直到落在 0° ~ 360°。')]))
P.append(para([T('第3步　鈍角 → 銳角：寫成 180° ± α 或 360° − α，用第2、4組公式。')]))

# ---- 概念五 圖像與性質 ----
P.append(heading('五、y = sin x 與 y = cos x 的圖像與性質'))
P.append(image_para(fig('fig4_sin_cos曲線.png'), width_cm=14.0,
                    caption='圖2：正弦曲線與餘弦曲線（cos 曲線就是 sin 曲線左移 π/2）'))
P.append(problem_box([
    para([T('兩個函數共同點：定義域都是 R；值域都是 [−1, 1]；最小正週期都是 2π。')]),
    para([T('y = sin x 是奇函數（圖像關於原點對稱）；y = cos x 是偶函數（圖像關於 y 軸對稱）。')]),
    para([T('y = sin x 在 '), M(mr('[−'), HALF_PI, mr(' + 2kπ，'), HALF_PI, mr(' + 2kπ]')),
          T(' 遞增，在 '), M(mr('['), HALF_PI, mr(' + 2kπ，'), F('3π', '2'), mr(' + 2kπ]')),
          T(' 遞減。')]),
    para([T('y = cos x 在 [−π + 2kπ，2kπ] 遞增，在 [2kπ，π + 2kπ] 遞減。（k 為整數）')]),
]))
P.append(para([T('週期公式：'), M(mr('y = A sin(ωx + φ) + b')), T(' 的最小正週期 '),
               M(mr('T = '), F(mr('2π'), mr('ω')))]))

# ---- 概念六 五點法 ----
P.append(heading('六、五點法畫圖'))
P.append(para([T('畫一個週期的正弦型圖像，只需描五個關鍵點——x 依次取：')]))
P.append(para([M(mr('0，　'), HALF_PI, mr('，　π，　'), F('3π', '2'), mr('，　2π'))]))
P.append(para([T('（最高點、最低點和三個與中線的交點），再用平滑曲線連起來。')]))

# ---- 範例 ----
P.append(heading('七、範例（跟著四個步驟做）'))
P.append(problem_box([
    para([T('求 cos(−120°) 的值。')], bold=True),
    para([T('步驟1　負角 → 正角：cos 是偶函數（第3組），cos(−120°) = cos 120°。')]),
    para([T('步驟2　鈍角 → 銳角：120° = 180° − 60°，用第4組，'
            'cos 120° = cos(180° − 60°) = −cos 60°。')]),
    para([T('步驟3　代特殊角值：'),
          M(mr('−cos 60° = −'), F('1', '2'))]),
    para([T('步驟4　檢查：120° 的終邊在第二象限，第二象限 cos 應為負——'
            '答案是負的，合理。')]),
]))
P.append(tail_to_practice('練習_誘導公式與圖像性質_融合版'))

out = build_docx(P, os.path.join(OUT, LEC_NAME), footer_text=FOOTER)
print(out)

# ============================================================ 練習
Q = []
Q.append(masthead('高一數學', UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(head_from_lecture('講義_誘導公式與圖像性質_融合版'))

# ---------------- 練習A ----------------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem([
    para([T('A-1．填空（每格填 sin α、cos α、tan α 之一，可加負號）：')]),
    para([T('sin(π + α) = ＿＿＿＿　　cos(−α) = ＿＿＿＿')]),
    para([T('tan(π − α) = ＿＿＿＿　　'),
          M(mr('sin('), HALF_PI, mr(' − α)')), T(' = ＿＿＿＿')]),
    hint([T('回頭看講義「二、誘導公式」的第2、3、4、5組。')]),
], lines=2))
Q.append(problem([
    para([T('A-2．照著已完成的第一行，求特殊角的值：')]),
    para([T('sin 120° = sin(180° − 60°) = sin 60° = '),
          M(F(R('3'), mr('2'))), T('（已完成）')]),
    para([T('cos 150° = cos(180° − 30°) = −cos 30° = ＿＿＿＿')]),
    para([T('tan 225° = tan(180° + 45°) = tan 45° = ＿＿＿＿')]),
    hint([T('先把角寫成 180° ± 銳角，再抄公式、代值。')]),
], lines=2))
Q.append(problem([
    para([T('A-3．看講義圖2的正弦曲線填空：')]),
    para([T('y = sin x 的最大值是 ＿＿＿，最小值是 ＿＿＿，最小正週期是 ＿＿＿。')]),
    para([T('y = cos x 是（奇函數 / 偶函數），把答案圈起來。')]),
], lines=2))
Q.append(problem([
    para([T('A-4．y = sin x 的值域是？（圈出答案）')]),
    mc3('[0, 1]', '[−1, 1]', '全體實數 R'),
    hint([T('看圖：曲線最高到多少、最低到多少？')]),
], lines=2))

# ---------------- 練習B ----------------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem([
    para([T('B-1．求值：sin(−30°) + cos 225° + tan 405°')]),
    hint([T('三個角分開處理：負角先變正角；225° = 180° + 45°；405° = 360° + 45°。')]),
], lines=5))
Q.append(problem([
    para([T('B-2．求值：'),
          M(mr('sin'), F(mr('13π'), mr('6')), mr(' + cos'), F(mr('23π'), mr('3')))]),
    hint([M(F(mr('13π'), mr('6')), mr(' = 2π + '), F('π', '6')),
          T('；'),
          M(F(mr('23π'), mr('3')), mr(' = 6π + '), F(mr('5π'), mr('3'))),
          T('，再把 '), M(F(mr('5π'), mr('3'))), T(' 寫成 '),
          M(mr('2π − '), F('π', '3'))]),
], lines=5))
Q.append(problem([
    para([T('B-3．化簡：'),
          M(F(mr('cos(π − α)·sin(2π − α)'), mr('sin(π + α)·cos(−α)')))]),
    hint([T('一項一項換：cos(π − α) = −cos α；sin(2π − α) = sin(−α) = −sin α；'
            'sin(π + α) = −sin α；cos(−α) = cos α。換完再約分。')]),
], lines=5))
Q.append(problem([
    para([T('B-4．用五點法作出 y = 1 + sin x（0 ≤ x ≤ 2π）的圖像。先填表，再描點連線：')]),
    para([T('x：　　0　　　π/2　　　π　　　3π/2　　　2π')]),
    para([T('sin x：＿＿　　＿＿　　＿＿　　＿＿　　＿＿')]),
    para([T('y = 1 + sin x：＿＿　　＿＿　　＿＿　　＿＿　　＿＿')]),
]))
Q.append(image_para(fig('fig5_五點法格線.png'), width_cm=14.0,
                    caption='（在格線上描出五個點，再用平滑曲線連接）'))
Q.append(problem([
    para([T('B-5．求下列函數的最小正週期：')]),
    para([T('(1) '), M(mr('f(x) = cos(2x + '), F('π', '8'), mr(')')),
          T('　　(2) '), M(mr('g(x) = sin'), F('x', '2'))]),
    hint([M(mr('T = '), F(mr('2π'), mr('ω'))), T('，ω 是 x 前面的係數。')]),
], lines=4))
Q.append(problem([
    para([T('B-6．求函數 y = 2 − sin x 的最大值和最小值，並說出各在 sin x 等於多少時取得。')]),
    hint([T('sin x 的範圍是 −1 到 1。sin x 前面是負號——sin x 越小，y 越大。')]),
], lines=4))

# ---------------- 練習C ----------------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem([
    para([T('C-1．化簡：'),
          M(F(mr('sin(π − α)·sin(') + F(mr('3π'), mr('2')) + mr(' − α)'),
              mr('cos(2π − α)·sin(−α − 2π)')))]),
    hint([M(mr('sin('), F(mr('3π'), mr('2')), mr(' − α) = −cos α')),
          T('（用口訣：3 是奇數倍 → 變 cos；把 α 當銳角時 '),
          M(F(mr('3π'), mr('2')), mr(' − α')),
          T(' 在第三象限，sin 為負）。')]),
], lines=6))
Q.append(problem([
    para([T('C-2．寫出 y = sin x 的所有單調遞增區間（用含 k 的一般式表示，k 為整數）。')]),
    hint([T('先看圖找出一個遞增區間，再每隔一個週期 2π 複製一次。')]),
], lines=4))
Q.append(problem([
    para([T('C-3．自己出一題「誘導公式化簡題」：要求至少用到兩條不同組的誘導公式，'
            '寫出題目和完整解答，並讓化簡結果是一個常數或單一函數。')]),
    hint([T('可以模仿 B-3 的樣子：分子放兩個因子、分母放兩個因子，設計成能約分。')]),
], lines=6))

# ---------------- 答案 ----------------
Q.append(pagebreak())
Q.append(heading('教師用參考答案'))
Q.append(para([T('A-1：−sin α；cos α；−tan α；cos α')]))
Q.append(para([T('A-2：cos 150° = '), M(mr('−'), F(R('3'), mr('2'))),
               T('；tan 225° = 1')]))
Q.append(para([T('A-3：最大值 1、最小值 −1、最小正週期 2π；cos x 是偶函數。')]))
Q.append(para([T('A-4：B')]))
Q.append(para([T('B-1：'),
               M(mr('−'), F('1', '2'), mr(' − '), F(R('2'), mr('2')), mr(' + 1 = '),
                 F(mr('1 − ') + R('2'), mr('2')))]))
Q.append(para([T('B-2：'),
               M(mr('sin'), F('π', '6'), mr(' + cos'), F(mr('5π'), mr('3')),
                 mr(' = '), F('1', '2'), mr(' + '), F('1', '2'), mr(' = 1'))]))
Q.append(para([T('B-3：'),
               M(F(mr('(−cos α)(−sin α)'), mr('(−sin α)(cos α)')), mr(' = −1'))]))
Q.append(para([T('B-4：sin x 一行：0、1、0、−1、0；y 一行：1、2、1、0、1。圖像如下：')]))
Q.append(image_para(fig('fig5ans_y=1+sinx.png'), width_cm=12.0))
Q.append(para([T('B-5：(1) '), M(mr('T = '), F(mr('2π'), mr('2')), mr(' = π')),
               T('　(2) '), M(mr('T = '), F(mr('2π'), mr('1/2')), mr(' = 4π'))]))
Q.append(para([T('B-6：最大值 3（sin x = −1 時）；最小值 1（sin x = 1 時）。')]))
Q.append(para([T('C-1：'),
               M(F(mr('sin α·(−cos α)'), mr('cos α·(−sin α)')), mr(' = 1'))]))
Q.append(para([T('C-2：'),
               M(mr('[−'), F('π', '2'), mr(' + 2kπ，'), F('π', '2'), mr(' + 2kπ]')),
               T('，k 為整數。')]))
Q.append(para([T('C-3：開放題。檢查要點——每一步用的公式組正確、符號正確、結果確實化到最簡。')]))

out = build_docx(Q, os.path.join(OUT, PRA_NAME), footer_text=FOOTER)
print(out)
