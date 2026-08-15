# -*- coding: utf-8 -*-
"""組③ 公式變換與圖像變換（5.5–5.6）：講義＋練習"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

UNIT = '三角函數（三）公式變換與圖像變換'
LEC_NAME = '講義_公式變換與圖像變換_融合版_高一數學.docx'
PRA_NAME = '練習_公式變換與圖像變換_融合版_高一數學.docx'
FOOTER = '高一數學．三角函數（三）公式變換與圖像變換'

# ============================================================ 講義
P = []
P.append(masthead('高一數學', UNIT, '課堂講義'))
P.append(student_info_row())

# ---- 概念一 兩角和差 ----
P.append(heading('一、兩角和與差的公式'))
P.append(problem_box([
    para([M(mr('cos(α − β) = cos α cos β + sin α sin β'))]),
    para([M(mr('cos(α + β) = cos α cos β − sin α sin β'))]),
    para([M(mr('sin(α + β) = sin α cos β + cos α sin β'))]),
    para([M(mr('sin(α − β) = sin α cos β − cos α sin β'))]),
    para([M(mr('tan(α + β) = '),
            F(mr('tan α + tan β'), mr('1 − tan α tan β')))]),
    para([M(mr('tan(α − β) = '),
            F(mr('tan α − tan β'), mr('1 + tan α tan β')))]),
]))
P.append(shaded_box([T('記法：cos 的展開是「同名相乘」（cos·cos、sin·sin），中間符號跟原式相反；'
                       'sin 的展開是「異名相乘」（sin·cos、cos·sin），中間符號跟原式相同。')],
                    kind='hint'))
P.append(para([T('用途一：算非特殊角。例如 75° = 45° + 30°、15° = 45° − 30°。')]))
P.append(para([T('用途二：把 sin 20° cos 40° + cos 20° sin 40° 這種展開式「收回去」'
                 '變成 sin(20° + 40°) = sin 60°。')]))

# ---- 概念二 二倍角 ----
P.append(heading('二、二倍角公式（令 β = α 就得到）'))
P.append(problem_box([
    para([M(mr('sin 2α = 2 sin α cos α'))]),
    para([M(mr('cos 2α = '), S2('cos'), mr(' α − '), S2('sin'), mr(' α = 2'),
            S2('cos'), mr(' α − 1 = 1 − 2'), S2('sin'), mr(' α'))]),
    para([M(mr('tan 2α = '), F(mr('2 tan α'), mr('1 − tan²α')))]),
]))
P.append(shaded_box([T('cos 2α 有三種寫法——題目給 sin α 就用「1 − 2sin²α」，'
                       '給 cos α 就用「2cos²α − 1」，兩個都給才用「cos²α − sin²α」。')],
                    kind='hint'))

# ---- 概念三 輔助角 ----
P.append(heading('三、輔助角公式（a sin x + b cos x 合成一個 sin）'))
P.append(para([M(mr('a sin x + b cos x = '),
                 R(sup(mr('a'), mr('2')) + mr(' + ') + sup(mr('b'), mr('2'))),
                 mr('·sin(x + φ)'))]))
P.append(para([T('常用的兩個結果（記住它們就夠應付大部分題目）：')]))
P.append(para([M(mr('sin x + cos x = '), R('2'), mr(' sin(x + '), F('π', '4'), mr(')'))]))
P.append(para([M(R('3'), mr(' sin x + cos x = 2 sin(x + '), F('π', '6'), mr(')'))]))
P.append(shaded_box([T('合成之後，最大值就是前面的係數 '), M(R(sup(mr('a'), mr('2')) + mr(' + ') + sup(mr('b'), mr('2')))),
                     T('，最小值是它加負號——這就是求「a sin x + b cos x 型」最值的固定套路。')],
                    kind='hint'))

# ---- 概念四 圖像變換 ----
P.append(heading('四、y = A sin(ωx + φ) + b 四個參數的作用'))
P.append(para([T('A（振幅）：圖像縱向拉伸，最大 A、最小 −A。')]))
P.append(para([T('ω：橫向壓縮或拉伸，週期變成 '), M(mr('T = '), F(mr('2π'), mr('ω')))]))
P.append(para([T('φ：左右平移——「左加右減」：x + φ 是向左移 φ，x − φ 是向右移 φ。')]))
P.append(para([T('b：整條曲線上下平移 b。')]))
P.append(image_para(fig('fig6_圖像變換.png'), width_cm=15.0,
                    caption='圖1：四種變換各自的效果（虛線是原來的 y = sin x）'))
P.append(shaded_box([T('平移量說的是「x 本身」的變化。y = sin(2x + π/3) 要看成 '
                       'sin 2(x + π/6)——先提出 2，才能讀出平移量是 π/6。')],
                    kind='hint'))

# ---- 範例 ----
P.append(heading('五、範例（跟著四個步驟做）'))
P.append(problem_box([
    para([T('求 cos 75° 的值。')], bold=True),
    para([T('步驟1　拆角：75° 不是特殊角，把它拆成兩個特殊角：75° = 45° + 30°。')]),
    para([T('步驟2　選公式：拆的是「和」，cos 的和公式中間變減號：'
            'cos(α + β) = cos α cos β − sin α sin β。')]),
    para([T('步驟3　代入計算：')]),
    para([M(mr('cos 75° = cos 45° cos 30° − sin 45° sin 30° = '),
            F(R('2'), mr('2')), mr('·'), F(R('3'), mr('2')),
            mr(' − '), F(R('2'), mr('2')), mr('·'), F('1', '2'),
            mr(' = '), F(R('6') + mr(' − ') + R('2'), mr('4')))]),
    para([T('步驟4　檢查：75° 接近 90°，cos 應該接近 0 而且是正的。'
            '算一下 (2.45 − 1.41) ÷ 4 ≈ 0.26，合理。')]),
]))
P.append(tail_to_practice('練習_公式變換與圖像變換_融合版'))

out = build_docx(P, os.path.join(OUT, LEC_NAME), footer_text=FOOTER)
print(out)

# ============================================================ 練習
Q = []
Q.append(masthead('高一數學', UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(head_from_lecture('講義_公式變換與圖像變換_融合版'))

# ---------------- 練習A ----------------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem([
    para([T('A-1．把公式填完整：')]),
    para([T('cos(α − β) = ＿＿＿＿＿＿ + ＿＿＿＿＿＿')]),
    para([T('sin(α + β) = ＿＿＿＿＿＿ + ＿＿＿＿＿＿')]),
    para([T('sin 2α = ＿＿＿＿＿＿')]),
    hint([T('回頭看講義第一、二節的公式框。')]),
], lines=2))
Q.append(problem([
    para([T('A-2．照著提示把計算補完：')]),
    para([T('sin 15° cos 15° = '), M(F('1', '2')),
          T(' × (2 sin 15° cos 15°) = '), M(F('1', '2')),
          T(' × sin ＿＿° = ＿＿＿＿')]),
    hint([T('2 sin α cos α 就是 sin 2α。')]),
], lines=2))
Q.append(problem([
    para([T('A-3．照著範例的拆法補完（15° = 45° − 30°）：')]),
    para([T('cos 15° = cos(45° − 30°) = cos 45° cos 30° + sin 45° sin 30° = ＿＿＿＿')]),
    hint([T('跟講義範例幾乎一樣，只是中間變成加號。分母都是 4。')]),
], lines=2))
Q.append(problem([
    para([T('A-4．要得到 '), M(mr('y = sin(x + '), F('π', '6'), mr(')')),
          T(' 的圖像，需將 y = sin x 的圖像怎樣移動？（圈出答案）')]),
    mc3(omath(mr('向左平移 '), F('π', '6')),
        omath(mr('向右平移 '), F('π', '6')),
        omath(mr('向上平移 '), F('π', '6'))),
    hint([T('口訣「左加右減」：x 加了，向左移。')]),
], lines=2))

# ---------------- 練習B ----------------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem([
    para([T('B-1．已知 tan α = 2，求 '),
          M(mr('tan(α + '), F('π', '4'), mr(')')), T(' 的值。')]),
    hint([M(mr('tan'), F('π', '4'), mr(' = 1')),
          T('，代入 tan 的和公式。')]),
], lines=5))
Q.append(problem([
    para([T('B-2．已知 '), M(mr('sin α = −'), F('3', '5')),
          T('，且 α 為第四象限角，求 cos 2α 和 sin 2α。')]),
    hint([T('cos 2α 直接用 1 − 2sin²α（不用先求 cos α）；'
            'sin 2α 才需要 cos α——第四象限 cos 為正。')]),
], lines=5))
Q.append(problem([
    para([T('B-3．求值：sin 20° cos 40° + cos 20° sin 40°')]),
    hint([T('「異名相乘、中間加號」——這是 sin 的和公式展開後的樣子，把它收回去。')]),
], lines=4))
Q.append(problem([
    para([T('B-4．把 '), M(mr('f(x) = '), R('3'), mr(' sin x + cos x')),
          T(' 寫成 A sin(x + φ) 的形式，並求 f(x) 的最大值。')]),
    hint([M(mr('A = '), R(sup(mr('a'), mr('2')) + mr(' + ') + sup(mr('b'), mr('2')))),
          T('；這一題講義第三節直接給過結果。')]),
], lines=4))
Q.append(problem([
    para([T('B-5．函數 '), M(mr('y = 3 sin(2x + '), F('π', '3'), mr(')')), T('：')]),
    para([T('(1) 寫出振幅和最小正週期；')]),
    para([T('(2) 說明它可由 y = sin x 經過哪些步驟變換得到。')]),
    hint([T('平移量要先提出 2：'),
          M(mr('2x + '), F('π', '3'), mr(' = 2(x + '), F('π', '6'), mr(')'))]),
], lines=6))

# ---------------- 練習C ----------------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem([
    para([T('C-1．已知函數 '),
          M(mr('f(x) = '), F('1', '2'), mr(' sin 2x − '),
            F(R('3'), mr('2')), mr(' cos 2x')), T('：')]),
    para([T('(1) 把 f(x) 寫成 A sin(2x + φ) 的形式；')]),
    para([T('(2) 求 f(x) 的最大值，以及取得最大值時 x 的值；')]),
    para([T('(3) 求 f(x) 的最小正週期。')]),
    hint([T('係數 '), M(F('1', '2')), T(' 和 '), M(F(R('3'), mr('2'))),
          T(' 正好是 cos 60° 和 sin 60°——它是 sin(2x − 60°) 的展開。')]),
], lines=7))
Q.append(problem([
    para([T('C-2．下圖是函數 '), M(mr('f(x) = A sin(ωx + φ)')),
          T('（A > 0，ω > 0，|φ| < '), M(F('π', '2')),
          T('）的部分圖像：最高點是 '), M(mr('('), F('π', '6'), mr('，2)')),
          T('，最小正週期是 π。求 f(x) 的解析式。')]),
]))
Q.append(image_para(fig('fig7_求解析式.png'), width_cm=13.0))
Q.append(problem([
    para([T('（接上題作答）')]),
    hint([T('三步：由最高點的 y 讀出 A → 由週期求 ω → 把最高點座標代入 '),
          M(mr('ωx + φ = '), F('π', '2')), T(' 解出 φ。')]),
], lines=6))
Q.append(problem([
    para([T('C-3．用兩種不同的方法求 sin 75° 的值，並確認兩個結果相同。'
            '（方法可選：45° + 30° 的和公式；90° − 15° 的誘導公式＋A-3 的結果；或其他）')]),
], lines=6))

# ---------------- 答案 ----------------
Q.append(pagebreak())
Q.append(heading('教師用參考答案'))
Q.append(para([T('A-1：cos α cos β + sin α sin β；sin α cos β + cos α sin β；2 sin α cos α')]))
Q.append(para([T('A-2：sin 30°；'), M(F('1', '2'), mr(' × '), F('1', '2'), mr(' = '), F('1', '4'))]))
Q.append(para([T('A-3：'), M(F(R('2'), mr('2')), mr('·'), F(R('3'), mr('2')),
               mr(' + '), F(R('2'), mr('2')), mr('·'), F('1', '2'),
               mr(' = '), F(R('6') + mr(' + ') + R('2'), mr('4')))]))
Q.append(para([T('A-4：A（向左平移 '), M(F('π', '6')), T('）')]))
Q.append(para([T('B-1：'),
               M(mr('tan(α + '), F('π', '4'), mr(') = '),
                 F(mr('2 + 1'), mr('1 − 2×1')), mr(' = '),
                 F(mr('3'), mr('−1')), mr(' = −3'))]))
Q.append(para([T('B-2：'),
               M(mr('cos 2α = 1 − 2×'), F('9', '25'), mr(' = '), F('7', '25')),
               T('；第四象限 cos α = '), M(F('4', '5')),
               T('，'),
               M(mr('sin 2α = 2×(−'), F('3', '5'), mr(')×'), F('4', '5'),
                 mr(' = −'), F('24', '25'))]))
Q.append(para([T('B-3：sin(20° + 40°) = sin 60° = '), M(F(R('3'), mr('2')))]))
Q.append(para([T('B-4：'), M(mr('f(x) = 2 sin(x + '), F('π', '6'), mr(')')),
               T('；最大值 2。')]))
Q.append(para([T('B-5：(1) 振幅 3；'), M(mr('T = '), F(mr('2π'), mr('2')), mr(' = π')),
               T('。(2) 一種答案：先把 y = sin x 向左平移 '), M(F('π', '3')),
               T(' 得 '), M(mr('y = sin(x + '), F('π', '3'), mr(')')),
               T('；再把橫坐標縮為原來的 '), M(F('1', '2')),
               T('（縱坐標不變）得 '), M(mr('y = sin(2x + '), F('π', '3'), mr(')')),
               T('；最後縱坐標伸長為 3 倍得 '),
               M(mr('y = 3 sin(2x + '), F('π', '3'), mr(')')),
               T('。（先縮後移也可：橫縮 '), M(F('1', '2')),
               T(' 後只需左移 '), M(F('π', '6')), T('）')]))
Q.append(para([T('C-1：(1) '),
               M(mr('f(x) = sin(2x − '), F('π', '3'), mr(')')),
               T('　(2) 最大值 1，此時 '),
               M(mr('2x − '), F('π', '3'), mr(' = '), F('π', '2'), mr(' + 2kπ')),
               T('，即 '),
               M(mr('x = '), F(mr('5π'), mr('12')), mr(' + kπ')),
               T('（k 為整數）　(3) T = π')]))
Q.append(para([T('C-2：A = 2；'),
               M(mr('ω = '), F(mr('2π'), mr('T')), mr(' = '), F(mr('2π'), mr('π')), mr(' = 2')),
               T('；把最高點代入：'),
               M(mr('2×'), F('π', '6'), mr(' + φ = '), F('π', '2')),
               T('，得 '), M(mr('φ = '), F('π', '6')),
               T('（滿足 |φ| < π/2）。所以 '),
               M(mr('f(x) = 2 sin(2x + '), F('π', '6'), mr(')'))]))
Q.append(para([T('C-3：兩種方法結果都是 '),
               M(F(R('6') + mr(' + ') + R('2'), mr('4'))),
               T('。方法一：sin 75° = sin 45° cos 30° + cos 45° sin 30°；'
                 '方法二：sin 75° = sin(90° − 15°) = cos 15°，即 A-3 的結果。')]))

out = build_docx(Q, os.path.join(OUT, PRA_NAME), footer_text=FOOTER)
print(out)
