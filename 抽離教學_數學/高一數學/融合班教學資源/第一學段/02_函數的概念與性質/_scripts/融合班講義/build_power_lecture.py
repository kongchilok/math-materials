# -*- coding: utf-8 -*-
"""講義_冪函數的性質_高一數學.docx"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))
DIAG = os.path.join(HERE, 'svgs_power', 'diagram_power_functions.png')


def grid_table(header, rows, widths):
    """簡易多欄表格（照 problem_box 的有效 XML 樣式擴充成多列多欄）。
    header/rows 的每格是 {} 標記字串；widths 為各欄 twips，總和應=版面寬。"""
    total = sum(widths)
    b = ''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
                for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)

    def cell(markup, w, is_header=False):
        tcpr = f'<w:tcW w:w="{w}" w:type="dxa"/>'
        if is_header:
            tcpr += f'<w:shd w:val="clear" w:color="auto" w:fill="{GREY_FILL}"/>'
        tcpr += ('<w:tcMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
                 '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
                 '<w:vAlign w:val="center"/>')
        p = para(markup, bold=is_header, sz=22)
        return f'<w:tc><w:tcPr>{tcpr}</w:tcPr>{p}</w:tc>'

    trs = ('<w:tr><w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>'
           + ''.join(cell(header[k], widths[k], True) for k in range(len(widths))) + '</w:tr>')
    for r in rows:
        trs += ('<w:tr><w:trPr><w:cantSplit/></w:trPr>'
                + ''.join(cell(r[k], widths[k]) for k in range(len(widths))) + '</w:tr>')
    tbl = (f'<w:tbl><w:tblPr><w:tblW w:w="{total}" w:type="dxa"/>'
           f'<w:tblBorders>{b}</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr>'
           f'<w:tblGrid>{grid}</w:tblGrid>{trs}</w:tbl>')
    return tbl + blank()


P = []
P.append(masthead('高一數學', '冪函數的性質', '課堂講義'))
P.append(student_info_row())

# ---------------- 一、什麼是冪函數 ----------------
P.append(heading('一、什麼是冪函數'))
P.append(para('先看幾個熟悉的關係：正方形面積 {S=a^2}（面積是邊長的平方）、'
              '正方體體積 {V=b^3}（體積是稜長的立方）、正方形邊長 {c=sqrt(S)}（邊長是面積的算術平方根）。'
              '把自變量統一寫成 x，這些關係都長成同一個樣子——底數是 x、指數是一個常數。'))
P.append(shaded_box('一般地，形如 {y=x^α} 的函數叫做冪函數，其中 x 是自變量，α 是常數。'))
P.append(shaded_box('關鍵辨識：冪函數的樣子一定是「y ＝ x 的某個常數次方」，x 前面的係數必須是 1。'
                    '像 {y=2x^2}（係數是 2，不是 1）不是冪函數；{y=2^x}（x 跑到指數位置）是指數函數，也不是冪函數。'))

P.append(heading('範例一：判斷哪些是冪函數', sz=BODY_SZ))
P.append(problem_box([
    para('判斷下列三個函數哪些是冪函數：（1）{y=x^3}　（2）{y=2x^2}　（3）{y=x^{frac(1,2)}}'),
    para('①看形式：冪函數一定是 {y=x^α}，係數為 1、指數為常數。'),
    para('②（1）{y=x^3}：係數 1、指數 3 是常數 → 是冪函數。'),
    para('③（2）{y=2x^2}：係數是 2 不是 1 → 不是冪函數。'),
    para('④（3）{y=x^{frac(1,2)}}：係數 1、指數 {frac(1,2)} 是常數 → 是冪函數（就是 {y=sqrt(x)}）。'),
], trailing_blank=True))

# ---------------- 二、五個常見冪函數的圖象與性質 ----------------
P.append(heading('二、五個常見冪函數的圖象與性質'))
P.append(para('把 α 取 1、2、3、{frac(1,2)}、−1 這五個值，畫在同一個坐標系裡，就得到最常用的五條冪函數圖象：'))
P.append(image_para(DIAG, width_cm=9,
                    caption='圖：五個常見冪函數的圖象（它們都經過同一個點 (1, 1)）'))
P.append(para('把它們的性質整理成一張表：'))
P.append(grid_table(
    ['函數', '定義域', '值域', '奇偶性', '單調性'],
    [
        ['{y=x}', 'R', 'R', '奇函數', '在 R 上遞增'],
        ['{y=x^2}', 'R', '[0, +∞)', '偶函數', '(−∞, 0] 遞減，[0, +∞) 遞增'],
        ['{y=x^3}', 'R', 'R', '奇函數', '在 R 上遞增'],
        ['{y=x^{frac(1,2)}}', '[0, +∞)', '[0, +∞)', '非奇非偶', '在 [0, +∞) 上遞增'],
        ['{y=x^{-1}}', 'x ≠ 0', 'y ≠ 0', '奇函數', '(−∞, 0)、(0, +∞) 上都遞減'],
    ],
    [1900, 1900, 1700, 1738, 4100],
))
P.append(shaded_box('記憶橋：這五個冪函數的圖象都經過同一個點 (1, 1)。判斷單調性、比較大小時，'
                    '先在腦中把對應那條曲線的形狀想出來，會快很多。'))

# ---------------- 三、分數指數冪的運算 ----------------
P.append(heading('三、分數指數冪的運算'))
P.append(para('冪函數的指數可以是分數或負數，先掌握幾條換算規則（下面都假設 a > 0）：'))
P.append(shaded_box('{a^{frac(1,2)}=sqrt(a)}　；　{a^{frac(1,n)}=sqrt[n](a)}　；　'
                    '{a^{frac(m,n)}=sqrt[n](a^m)}　；　{a^{-1}=frac(1,a)}　；　{a^{-n}=frac(1,a^n)}'))
P.append(para('用具體數字感受一下：{9^{frac(1,2)}=sqrt(9)=3}；{8^{frac(1,3)}=sqrt[3](8)=2}；'
              '{4^{-1}=frac(1,4)}。'))

P.append(heading('範例二：把根式化成分數指數冪再求值', sz=BODY_SZ))
P.append(problem_box([
    para('求 {sqrt[3](8^2)} 的值。'),
    para('①化成分數指數冪：{sqrt[3](8^2)=8^{frac(2,3)}}。'),
    para('②用規則 {a^{frac(m,n)}=sqrt[n](a^m)}，也可以先開立方根再平方：{8^{frac(2,3)}=(sqrt[3](8))^2}。'),
    para('③計算：{sqrt[3](8)=2}，所以 {(2)^2=4}。'),
    para('④結論：{sqrt[3](8^2)=4}。'),
], trailing_blank=True))
P.append(shaded_box('提示：遇到分數指數，先分清「分母是開幾次方根、分子是幾次方」，'
                    '再挑「先開根號」還是「先乘方」順手就好，兩種算出來一樣。'))

P.append(para('接下來請拿《冪函數的性質 課堂練習》，依這些規則與性質表完成練習A、B、C。'))

out = build_docx(P, os.path.join(HERE, '講義_冪函數的性質_高一數學.docx'),
                 footer_text='高一數學．冪函數的性質')
print('OK', out)
