# -*- coding: utf-8 -*-
"""組① 角與三角函數的概念（5.1–5.2）：講義＋練習"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

UNIT = '三角函數（一）角與三角函數的概念'
LEC_NAME = '講義_角與三角函數的概念_融合版_高一數學.docx'
PRA_NAME = '練習_角與三角函數的概念_融合版_高一數學.docx'
FOOTER = '高一數學．三角函數（一）角與三角函數的概念'

# ============================================================ 講義
P = []
P.append(masthead('高一數學', UNIT, '課堂講義'))
P.append(student_info_row())

# ---- 概念一 任意角與象限 ----
P.append(heading('一、任意角與象限'))
P.append(para([T('角可以想像成一條射線繞著頂點旋轉：'
                 '逆時針旋轉得到正角，順時針旋轉得到負角。')]))
P.append(para([T('把角放在坐標系裡：頂點放在原點，始邊放在 x 軸正方向。'
                 '終邊落在哪個象限，這個角就是哪個象限的角。')]))
P.append(image_para(fig('fig1_象限與終邊.png'), width_cm=8.0,
                    caption='圖1：始邊、終邊與四個象限（例：150° 是第二象限角）'))
P.append(para([T('終邊相同的角：繞多一圈（±360°）終邊不變，所以與角 α 終邊相同的角可寫成')]))
P.append(para([M(mr('α + k·360°　(k 是整數)'))], jc='left'))
P.append(shaded_box([T('提示：判斷兩個角終邊是否相同，把它們相減，看差是不是 360° 的整數倍。'
                       '例：390° − 30° = 360°，所以 390° 與 30° 終邊相同。')], kind='hint'))

# ---- 概念二 弧度制 ----
P.append(heading('二、弧度制'))
P.append(para([T('弧度是角的另一種單位。關鍵只有一條：'), M(mr('180° = π rad'))]))
P.append(para([T('度 → 弧度：乘 '), M(F('π', '180°')),
               T('；　弧度 → 度：乘 '), M(F('180°', 'π'))]))
P.append(para([T('常用對照：'),
               M(mr('30° = '), F('π', '6'), mr('　45° = '), F('π', '4'),
                 mr('　60° = '), F('π', '3'), mr('　90° = '), F('π', '2'),
                 mr('　180° = π'))]))
P.append(para([T('半徑 r、圓心角 α（弧度）的扇形：')]))
P.append(para([T('弧長 '), M(mr('l = αr')),
               T('；　面積 '), M(mr('S = '), F('1', '2'), mr('lr = '),
                 F('1', '2'), mr('α'), sup(mr('r'), mr('2')))]))

# ---- 概念三 三角函數的定義 ----
P.append(heading('三、三角函數的定義'))
P.append(para([T('設角 α 的終邊與單位圓（半徑為 1 的圓）交於點 P(x, y)，規定：')]))
P.append(para([M(mr('sin α = y　　cos α = x　　tan α = '), F('y', 'x'),
                 mr('　(x ≠ 0)'))]))
P.append(image_para(fig('fig2_單位圓定義.png'), width_cm=7.5,
                    caption='圖2：單位圓上的定義——y 是正弦、x 是餘弦'))
P.append(para([T('如果終邊經過的點不在單位圓上，例如 P(x, y)，先算出它到原點的距離')]))
P.append(para([M(mr('r = '), R(sup(mr('x'), mr('2')) + mr(' + ') + sup(mr('y'), mr('2'))))]))
P.append(para([T('然後：'), M(mr('sin α = '), F('y', 'r'),
               mr('　cos α = '), F('x', 'r'),
               mr('　tan α = '), F('y', 'x'))]))
P.append(para([T('各象限的正負號：')]))
P.append(image_para(fig('fig8_符號口訣.png'), width_cm=8.0,
                    caption='圖3：符號口訣——「一全正、二正弦、三正切、四餘弦」'))

# ---- 概念四 同角關係 ----
P.append(heading('四、同角三角函數的關係'))
P.append(para([T('同一個角的三個三角函數之間有兩條固定關係：')]))
P.append(para([T('平方關係：'), M(S2('sin'), mr(' α + '), S2('cos'), mr(' α = 1'))]))
P.append(para([T('商數關係：'), M(mr('tan α = '), F(mr('sin α'), mr('cos α')))]))
P.append(shaded_box([T('提示：知道其中一個函數值＋角所在的象限，就能求出另外兩個。'
                       '先用平方關係求出第二個，再用商數關係求第三個。')], kind='hint'))

# ---- 範例 ----
P.append(heading('五、範例（跟著四個步驟做）'))
P.append(problem_box([
    para([T('已知角 α 的終邊經過點 P(3, −4)，求 sin α、cos α、tan α。')], bold=True),
    para([T('步驟1　圈出重點：終邊經過 P(3, −4)，所以 x = 3，y = −4。')]),
    para([T('步驟2　選公式：點不在單位圓上，先求 '),
          M(mr('r = '), R(sup(mr('x'), mr('2')) + mr(' + ') + sup(mr('y'), mr('2'))))]),
    para([T('步驟3　計算：'),
          M(mr('r = '), R(sup(mr('3'), mr('2')) + mr(' + ') + sup(mr('(−4)'), mr('2'))),
            mr(' = '), R('25'), mr(' = 5'))]),
    para([M(mr('sin α = '), F('y', 'r'), mr(' = −'), F('4', '5'),
            mr('　　cos α = '), F('x', 'r'), mr(' = '), F('3', '5'),
            mr('　　tan α = '), F('y', 'x'), mr(' = −'), F('4', '3'))]),
    para([T('步驟4　檢查：P(3, −4) 在第四象限，第四象限只有 cos 為正——'
            '算出來 sin 負、cos 正、tan 負，符合，答案合理。')]),
]))
P.append(tail_to_practice('練習_角與三角函數的概念_融合版'))

out = build_docx(P, os.path.join(OUT, LEC_NAME), footer_text=FOOTER)
print(out)

# ============================================================ 練習
Q = []
Q.append(masthead('高一數學', UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(head_from_lecture('講義_角與三角函數的概念_融合版'))

# ---------------- 練習A ----------------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem([
    para([T('A-1．把空格填完整（照著第一行做）：')]),
    para([T('與 60° 終邊相同的角：60° + 360° = 420°（已完成）')]),
    para([T('60° − 360° = ＿＿＿＿＿＿')]),
    para([T('在 90°、−300°、480° 三個角中，與 60° 終邊相同的是 ＿＿＿＿＿＿。')]),
    hint([T('相差 360° 的整數倍，終邊就相同。用「該角 − 60°」檢查。')]),
], lines=2))
Q.append(problem([
    para([T('A-2．照著已完成的一格，把換算表填完：')]),
    para([M(mr('30° = '), F('π', '6')), T('（已完成）　　45° = ＿＿＿　　60° = ＿＿＿　　90° = ＿＿＿')]),
    para([M(mr('π = 180°')), T('（已完成）　　'),
          M(F('π', '3')), T(' = ＿＿＿°　　'),
          M(F('π', '4')), T(' = ＿＿＿°')]),
    hint([T('度 → 弧度：乘 '), M(F('π', '180°')), T('；弧度 → 度：乘 '), M(F('180°', 'π'))]),
], lines=2))
Q.append(problem([
    para([T('A-3．已知角 α 的終邊與單位圓交於點 '),
          M(mr('P('), F('3', '5'), mr('，'), F('4', '5'), mr(')')), T('，填空：')]),
    para([T('sin α = ＿＿＿　　cos α = ＿＿＿　　tan α = ＿＿＿')]),
    hint([T('單位圓上，sin α 就是 y 坐標，cos α 就是 x 坐標，tan α = y ÷ x。')]),
], lines=2))
Q.append(problem([
    para([T('A-4．已知 sin α > 0 且 cos α < 0，則 α 是第幾象限角？（圈出答案）')]),
    mc3('第一象限', '第二象限', '第三象限'),
    hint([T('回頭看講義圖3的符號口訣：sin 為正 → 第一或第二象限；cos 為負 → 第二或第三象限。')]),
], lines=2))

# ---------------- 練習B ----------------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem([
    para([T('B-1．在 0° ~ 360° 範圍內，找出與 750° 終邊相同的角，並說出它是第幾象限角。')]),
    hint([T('先一直減 360°，減到落在 0° ~ 360° 為止。')]),
], lines=3))
Q.append(problem([
    para([T('B-2．一個扇形半徑 r = 3，圓心角 '), M(mr('α = '), F('π', '6')),
          T('，求弧長 l 和扇形面積 S。')]),
    hint([M(mr('l = αr')), T('；'), M(mr('S = '), F('1', '2'), mr('lr'))]),
], lines=4))
Q.append(problem([
    para([T('B-3．已知角 α 的終邊經過點 P(−4, 3)，求 sin α、cos α、tan α。')]),
    hint([T('照講義範例四步驟：找 x、y → 求 r → 代公式 → 檢查象限符號。')]),
], lines=5))
Q.append(problem([
    para([T('B-4．已知 '), M(mr('sin α = '), F('5', '13')),
          T('，且 α 為第二象限角，求 cos α 和 tan α。')]),
    hint([T('先用 '), M(S2('sin'), mr(' α + '), S2('cos'), mr(' α = 1')),
          T(' 求 cos α（注意第二象限 cos 是負的），再用商數關係求 tan α。')]),
], lines=5))
Q.append(problem([
    para([T('B-5．已知 tan α = 2，求 '),
          M(F(mr('sin α + 2cos α'), mr('2sin α − 3cos α'))), T(' 的值。')]),
    hint([T('分子、分母同時除以 cos α，整條式子就只剩下 tan α。')]),
], lines=5))

# ---------------- 練習C ----------------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem([
    para([T('C-1．已知 tan α = 3，求 '),
          M(S2('sin'), mr(' α − 2sin α cos α')), T(' 的值。')]),
    hint([T('把式子除以 '), M(S2('sin'), mr(' α + '), S2('cos'), mr(' α')),
          T('（它等於 1，除了不改變值），再分子分母同除 '), M(S2('cos'), mr(' α'))]),
], lines=5))
Q.append(problem([
    para([T('C-2．一個扇形的周長是 20 cm。半徑取多少時，扇形面積最大？'
            '此時圓心角是多少弧度？')]),
    hint([T('周長 = 兩條半徑 + 弧長，所以 l = 20 − 2r。把面積寫成 r 的二次函數再配方。')]),
], lines=6))
Q.append(problem([
    para([T('C-3．自己出一題：仿照練習B第3題，自選一個點 P(a, b)，'
            '使 r 是整數（可選 3 與 4、6 與 8、5 與 12、8 與 15 等組合，正負號自定），'
            '寫出題目並完成解答。')]),
    hint([T('出題後記得用步驟4檢查：你的點在第幾象限？三個函數值的正負號對不對？')]),
], lines=6))

# ---------------- 答案 ----------------
Q.append(pagebreak())
Q.append(heading('教師用參考答案'))
Q.append(para([T('A-1：60° − 360° = −300°；三個角之中，與 60° 終邊相同的只有 −300°。'
                 '（90° − 60° = 30°、480° − 60° = 420°，都不是 360° 的整數倍；'
                 '480° 減去 360° 得 120°，其實與 120° 終邊相同）')]))
Q.append(para([T('A-2：45° = '), M(F('π', '4')), T('；60° = '), M(F('π', '3')),
               T('；90° = '), M(F('π', '2')), T('；'),
               M(F('π', '3')), T(' = 60°；'), M(F('π', '4')), T(' = 45°')]))
Q.append(para([T('A-3：sin α = '), M(F('4', '5')), T('；cos α = '), M(F('3', '5')),
               T('；tan α = '), M(F('4', '3'))]))
Q.append(para([T('A-4：B（第二象限）')]))
Q.append(para([T('B-1：750° − 360° − 360° = 30°，第一象限角。')]))
Q.append(para([T('B-2：'), M(mr('l = αr = '), F('π', '6'), mr(' × 3 = '), F('π', '2')),
               T('；'), M(mr('S = '), F('1', '2'), mr('lr = '), F('1', '2'),
                 mr(' × '), F('π', '2'), mr(' × 3 = '), F('3π', '4'))]))
Q.append(para([T('B-3：r = 5；sin α = '), M(F('3', '5')),
               T('；cos α = '), M(mr('−'), F('4', '5')),
               T('；tan α = '), M(mr('−'), F('3', '4')),
               T('。（P 在第二象限：sin 正、cos 負、tan 負 ✓）')]))
Q.append(para([T('B-4：cos α = '), M(mr('−'), F('12', '13')),
               T('；tan α = '), M(mr('−'), F('5', '12'))]))
Q.append(para([T('B-5：分子分母同除 cos α：'),
               M(F(mr('tan α + 2'), mr('2tan α − 3')), mr(' = '),
                 F(mr('2 + 2'), mr('4 − 3')), mr(' = 4'))]))
Q.append(para([T('C-1：'),
               M(F(mr('sin²α − 2sin α cos α'), mr('sin²α + cos²α')), mr(' = '),
                 F(mr('tan²α − 2tan α'), mr('tan²α + 1')), mr(' = '),
                 F(mr('9 − 6'), mr('9 + 1')), mr(' = '), F('3', '10'))]))
Q.append(para([T('C-2：l = 20 − 2r，'),
               M(mr('S = '), F('1', '2'), mr('lr = '), F('1', '2'),
                 mr('(20 − 2r)r = 10r − r² = 25 − (r − 5)²')),
               T('，所以 r = 5 cm 時面積最大（25 cm²），此時 l = 10，圓心角 '),
               M(mr('α = '), F('l', 'r'), mr(' = 2')), T(' 弧度。')]))
Q.append(para([T('C-3：開放題。檢查要點——r 計算正確、三個比值正確、象限符號一致。')]))

out = build_docx(Q, os.path.join(OUT, PRA_NAME), footer_text=FOOTER)
print(out)
