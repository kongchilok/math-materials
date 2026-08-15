# -*- coding: utf-8 -*-
"""線性規劃 組2：線性規劃求最值與應用 —— 講義＋練習（docx＋html）。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")

import dgm
import htmlkit as H
from omml_docx import *  # noqa

OUT = os.path.abspath(os.path.join(HERE, '..', '線性規劃'))
ASSET = os.path.join(HERE, 'lp2_assets')
os.makedirs(ASSET, exist_ok=True)
SUBJ, UNIT = '高二數學', '線性規劃求最值與應用'
FOOT = '高二數學．線性規劃求最值與應用'


def savepng(svg, name):
    path = os.path.join(ASSET, name)
    dgm.svg_to_png(svg, path)
    return path


# ---- 講義 範例：可行域 (0,0)(4,0)(3,1)(0,2)，z=2x+3y ----
g = dgm.Grid(-1, 6, -1, 5, s=26)
g.base()
g.shade_poly([(0, 0), (4, 0), (3, 1), (0, 2)])
g.line_abc(1, 1, 4)      # x+y=4
g.line_abc(1, 3, 6)      # x+3y=6
g.line_abc(2, 3, 9, dashed=True)  # 目標線 2x+3y=9（示意）
g.dot(0, 0, 'O', dx=-13, dy=14, r=2.6)
g.dot(4, 0, '(4,0)', dx=2, dy=-8)
g.dot(3, 1, '(3,1)', dx=6, dy=-6)
g.dot(0, 2, '(0,2)', dx=8, dy=-2)
SVG_WORK = g.svg()
PNG_WORK = savepng(SVG_WORK, 'work.png')

# ---- 練習A-1：已知可行域 A(0,0)B(5,0)C(3,3)D(0,4) ----
g = dgm.Grid(-1, 6, -1, 5, s=26)
g.base()
g.shade_poly([(0, 0), (5, 0), (3, 3), (0, 4)])
g.dot(0, 0, 'A(0,0)', dx=-4, dy=15)
g.dot(5, 0, 'B(5,0)', dx=2, dy=-8)
g.dot(3, 3, 'C(3,3)', dx=6, dy=-4)
g.dot(0, 4, 'D(0,4)', dx=8, dy=-2)
SVG_A1 = g.svg()
PNG_A1 = savepng(SVG_A1, 'a1.png')

# ---- 練習A-2：三角形 P(1,1)Q(4,1)R(1,3) ----
g = dgm.Grid(-1, 6, -1, 5, s=26)
g.base()
g.shade_poly([(1, 1), (4, 1), (1, 3)])
g.dot(1, 1, 'P(1,1)', dx=-6, dy=16)
g.dot(4, 1, 'Q(4,1)', dx=4, dy=16)
g.dot(1, 3, 'R(1,3)', dx=6, dy=-4)
SVG_A2 = g.svg()
PNG_A2 = savepng(SVG_A2, 'a2.png')

# ---- 練習C-6：已知可行域 O(0,0)A(4,0)B(2,3)C(0,4) ----
g = dgm.Grid(-1, 6, -1, 5, s=26)
g.base()
g.shade_poly([(0, 0), (4, 0), (2, 3), (0, 4)])
g.dot(0, 0, 'O', dx=-13, dy=14, r=2.6)
g.dot(4, 0, 'A(4,0)', dx=2, dy=-8)
g.dot(2, 3, 'B(2,3)', dx=6, dy=-4)
g.dot(0, 4, 'C(0,4)', dx=8, dy=-2)
SVG_C6 = g.svg()
PNG_C6 = savepng(SVG_C6, 'c6.png')

# ---- 空白方格（B/C 作答用）----
g = dgm.Grid(-1, 8, -1, 8, s=18)
g.base()
SVG_BLANK = g.svg()
PNG_BLANK = savepng(SVG_BLANK, 'blank.png')

# ================= 講義 docx =================
P = []
P.append(masthead(SUBJ, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、什麼是線性規劃'))
P.append(para('在幾個「二元一次不等式」（限制條件）之下，求一個式子 {z=ax+by}（目標函數）'
              '的最大值或最小值，這類問題叫「線性規劃」。'))
P.append(para('把所有限制條件的公共區域畫出來，就是「可行域」——通常是一個凸多邊形。'
              '我們的任務，是在可行域裡找出讓 {z} 最大（或最小）的那一點。'))

P.append(heading('二、關鍵事實與頂點法'))
P.append(shaded_box('關鍵事實：目標函數 {z=ax+by} 在凸多邊形可行域上的最大值與最小值，'
                    '一定在可行域的「頂點」上取得。'))
P.append(para('由這個事實，得到最穩妥的「頂點法」四步驟：'))
P.append(para('步驟①　畫可行域：把每個限制不等式的區域畫出來，取公共部分。'))
P.append(para('步驟②　找頂點：求出可行域每個頂點的坐標（相鄰兩界線的交點）。'))
P.append(para('步驟③　代入比較：把每個頂點坐標代入 {z=ax+by}，算出各自的 {z} 值。'))
P.append(para('步驟④　下結論：最大的就是最大值，最小的就是最小值，並記下在哪一點取得。'))

P.append(heading('三、範例'))
P.append(para('範例：設 {x}、{y} 滿足 {x>=0}、{y>=0}、{x+y<=4}、{x+3y<=6}，求 {z=2x+3y} 的最大值。',
              bold=True))
P.append(para('步驟①（畫可行域）：{x>=0}、{y>=0} 限第一象限；{x+y<=4} 取直線 {x+y=4} 的下方；'
              '{x+3y<=6} 取直線 {x+3y=6} 的下方。公共區域如下圖（陰影）。'))
P.append(image_para(PNG_WORK, width_cm=7.2, caption='可行域（陰影）與四個頂點；虛線為目標線 2x+3y=z'))
P.append(para('步驟②（找頂點）：四個頂點為 {(0,0)}、{(4,0)}、{(0,2)}，以及 {x+y=4} 與 {x+3y=6} '
              '的交點 {(3,1)}。'))
P.append(para('步驟③（代入比較）：'
              '{(0,0)}→{z=0}；{(4,0)}→{z=8}；{(3,1)}→{z=2×3+3×1=9}；{(0,2)}→{z=6}。'))
P.append(para('步驟④（下結論）：最大值 {z=9}，在頂點 {(3,1)} 取得。'))
P.append(shaded_box('另一種看法（平行線法）：把 {2x+3y=z} 看成一族平行線，{z} 越大線越往右上移；'
                    '平移到「快要離開可行域」時，最後碰到的頂點 {(3,1)} 就是最大值的位置。'))

P.append(heading('四、換你試'))
P.append(para('接下來請取出《線性規劃求最值與應用　課堂練習》，'
              '依「畫可行域 → 找頂點 → 代入比較 → 下結論」完成練習A、B、C。'))
print(build_docx(P, os.path.join(OUT, '講義_線性規劃求最值與應用.docx'), footer_text=FOOT))

# ================= 練習 docx =================
Q = []
Q.append(masthead(SUBJ, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('提示：頂點法四步驟——畫可行域 → 找頂點 → 各頂點代入 {z} → 比較大小。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．下圖陰影是可行域，四個頂點為 {A(0,0)}、{B(5,0)}、{C(3,3)}、{D(0,4)}。'
         '目標函數 {z=x+2y}。請把各頂點代入，填出 {z} 值，找出最大值。'),
]))
Q.append(image_para(PNG_A1, width_cm=6.6))
Q.append(shaded_box('鷹架：{A}：{z=0+2×0=0}；　{B}：{z=5+2×0=}（　）；　'
                    '{C}：{z=3+2×3=}（　）；　{D}：{z=0+2×4=}（　）。'
                    '最大值 {z=}（　），在點（　）取得。'))
Q.append(problem_box([
    para('2．下圖三角形可行域的頂點為 {P(1,1)}、{Q(4,1)}、{R(1,3)}，目標函數 {z=3x+y}。'
         '求 {z} 的最大值與最小值，並各寫出在哪一點取得。'),
]))
Q.append(image_para(PNG_A2, width_cm=6.6))
Q.extend(write_lines(2))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(para('請自己畫可行域、找頂點、代入比較。'))
Q.append(problem_box([
    para('3．設 {x>=0}、{y>=0}、{x+y<=6}、{x+2y<=8}，求 {z=x+3y} 的最大值與最小值。'),
]))
Q.append(image_para(PNG_BLANK, width_cm=6.8))
Q.append(problem_box([
    para('4．設 {x>=0}、{y>=0}、{2x+y<=10}、{x+y<=7}，求 {z=4x+3y} 的最大值。'),
]))
Q.append(image_para(PNG_BLANK, width_cm=6.8))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('5．（應用題）某工廠用 A、B 兩種原料生產甲、乙兩種產品。每件甲需 A 料 {2} kg、B 料 {1} kg，'
         '獲利 {4} 百元；每件乙需 A 料 {1} kg、B 料 {2} kg，獲利 {3} 百元。'
         '每日 A 料最多 {10} kg、B 料最多 {8} kg。問每日各生產甲、乙多少件，總獲利最大？最大獲利多少？'),
    shaded_box('鷹架：設每日生產甲 {x} 件、乙 {y} 件。'
               '限制：{2x+y<=10}（A 料）、{x+2y<=8}（B 料）、{x>=0}、{y>=0}；目標 {z=4x+3y}（百元）。'),
]))
Q.append(image_para(PNG_BLANK, width_cm=6.8))
Q.append(problem_box([
    para('6．已知可行域的頂點為 {O(0,0)}、{A(4,0)}、{B(2,3)}、{C(0,4)}（見下圖）。'
         '目標函數 {z=ax+y}（{a>0}）。若 {z} 的最大值在頂點 {A(4,0)} 取得，求 {a} 的取值範圍。'),
]))
Q.append(image_para(PNG_C6, width_cm=6.6))
Q.extend(write_lines(2))

Q.append(heading('參考答案與解析', page_break_before=True))
Q.append(para('練習A', bold=True))
Q.append(para('1．{B}：{z=5}；{C}：{z=3+6=9}；{D}：{z=8}。最大值 {z=9}，在點 {C(3,3)} 取得。'))
Q.append(para('2．{P}：{z=3×1+1=4}；{Q}：{z=3×4+1=13}；{R}：{z=3×1+3=6}。'
              '最大值 {z=13}（在 {Q(4,1)}）；最小值 {z=4}（在 {P(1,1)}）。'))
Q.append(para('練習B', bold=True))
Q.append(para('3．頂點 {(0,0)}、{(6,0)}、{(4,2)}、{(0,4)}。'
              '{z=x+3y}：{0}、{6}、{10}、{12}。最大值 {12}（在 {(0,4)}）；最小值 {0}（在 {(0,0)}）。'
              '（{(4,2)} 為 {x+y=6} 與 {x+2y=8} 的交點。）'))
Q.append(para('4．頂點 {(0,0)}、{(5,0)}、{(3,4)}、{(0,7)}。'
              '{z=4x+3y}：{0}、{20}、{24}、{21}。最大值 {24}，在點 {(3,4)} 取得。'
              '（{(3,4)} 為 {2x+y=10} 與 {x+y=7} 的交點。）'))
Q.append(para('練習C', bold=True))
Q.append(para('5．頂點 {(0,0)}、{(5,0)}、{(4,2)}、{(0,4)}。'
              '{z=4x+3y}：{0}、{20}、{4×4+3×2=22}、{12}。'
              '最大值 {22} 百元，在 {(4,2)} 取得：每日生產甲 {4} 件、乙 {2} 件，最大獲利 {2200} 元。'))
Q.append(para('6．各頂點的 {z=ax+y}：{O→0}、{A→4a}、{B→2a+3}、{C→4}。'
              '最大值在 {A} 取得，需 {4a>=2a+3} 且 {4a>=4}，即 {a>=frac(3,2)} 且 {a>=1}，'
              '故 {a>=frac(3,2)}。'))
print(build_docx(Q, os.path.join(OUT, '練習_線性規劃求最值與應用.docx'), footer_text=FOOT))

# ================= 講義 HTML =================
b = ''
b += H.section_h('一、什麼是線性規劃')
b += r'''  <p class="lead">在幾個「二元一次不等式」（限制條件）之下，求一個式子 \(z=ax+by\)（目標函數）的最大值或最小值，這類問題叫「線性規劃」。</p>
  <p class="lead">把所有限制條件的公共區域畫出來，就是「可行域」——通常是一個凸多邊形。我們的任務，是在可行域裡找出讓 \(z\) 最大（或最小）的那一點。</p>
'''
b += H.section_h('二、關鍵事實與頂點法')
b += r'''  <div class="hint-card"><b>關鍵事實：</b>目標函數 \(z=ax+by\) 在凸多邊形可行域上的最大值與最小值，一定在可行域的「頂點」上取得。</div>
  <ol class="steps-list">
    <li><b>步驟①　畫可行域：</b>把每個限制不等式的區域畫出來，取公共部分。</li>
    <li><b>步驟②　找頂點：</b>求出可行域每個頂點的坐標（相鄰兩界線的交點）。</li>
    <li><b>步驟③　代入比較：</b>把每個頂點代入 \(z=ax+by\)，算出各自的 \(z\) 值。</li>
    <li><b>步驟④　下結論：</b>最大的是最大值，最小的是最小值，記下在哪一點取得。</li>
  </ol>
'''
b += H.section_h('三、範例')
b += r'''  <div class="worked-example">
    <div class="st"><b>範例：</b>設 \(x\)、\(y\) 滿足 \(x \ge 0\)、\(y \ge 0\)、\(x+y \le 4\)、\(x+3y \le 6\)，求 \(z=2x+3y\) 的最大值。</div>
    <div class="st"><b>步驟①（畫可行域）：</b>\(x \ge 0\)、\(y \ge 0\) 限第一象限；\(x+y \le 4\) 取 \(x+y=4\) 下方；\(x+3y \le 6\) 取 \(x+3y=6\) 下方。公共區域如下圖。</div>
  </div>
'''
b += H.fig(SVG_WORK, '可行域（陰影）與四個頂點；虛線為目標線 2x+3y=z')
b += r'''  <div class="worked-example">
    <div class="st"><b>步驟②（找頂點）：</b>四個頂點為 \((0,0)\)、\((4,0)\)、\((0,2)\)，以及 \(x+y=4\) 與 \(x+3y=6\) 的交點 \((3,1)\)。</div>
    <div class="st"><b>步驟③（代入比較）：</b>\((0,0)\to z=0\)；\((4,0)\to z=8\)；\((3,1)\to z=2\times3+3\times1=9\)；\((0,2)\to z=6\)。</div>
    <div class="st"><b>步驟④（下結論）：</b>最大值 \(z=9\)，在頂點 \((3,1)\) 取得。</div>
  </div>
  <div class="hint-card"><b>平行線法：</b>把 \(2x+3y=z\) 看成一族平行線，\(z\) 越大線越往右上移；平移到「快要離開可行域」時，最後碰到的頂點 \((3,1)\) 就是最大值的位置。</div>
'''
b += H.section_h('四、換你試')
b += r'''  <p class="lead">接下來請取出《線性規劃求最值與應用　課堂練習》，依「畫可行域 → 找頂點 → 代入比較 → 下結論」完成練習A、B、C。</p>
'''
open(os.path.join(OUT, '講義_線性規劃求最值與應用.html'), 'w', encoding='utf-8').write(
    H.build('講義：線性規劃求最值與應用', SUBJ, UNIT, '課堂講義', b, FOOT))

# ================= 練習 HTML =================
b = r'''  <p class="lead">提示：頂點法四步驟——畫可行域 → 找頂點 → 各頂點代入 \(z\) → 比較大小。</p>
'''
b += H.section_h('一、練習A', '★☆☆')
b += H.problem(
    r'<div class="q">1．下圖陰影是可行域，四個頂點為 \(A(0,0)\)、\(B(5,0)\)、\(C(3,3)\)、\(D(0,4)\)。目標函數 \(z=x+2y\)。請把各頂點代入，填出 \(z\) 值，找出最大值。</div>'
    + H.fig(SVG_A1)
    + r'<div class="hint-card">鷹架：\(A\)：\(z=0+2\times0=0\)；　\(B\)：\(z=5+2\times0=\)（　）；　\(C\)：\(z=3+2\times3=\)（　）；　\(D\)：\(z=0+2\times4=\)（　）。最大值 \(z=\)（　），在點（　）取得。</div>')
b += H.problem(
    r'<div class="q">2．下圖三角形可行域的頂點為 \(P(1,1)\)、\(Q(4,1)\)、\(R(1,3)\)，目標函數 \(z=3x+y\)。求 \(z\) 的最大值與最小值，並各寫出在哪一點取得。</div>'
    + H.fig(SVG_A2) + H.wlines(2))

b += H.section_h('二、練習B', '★★☆')
b += r'''  <p class="lead">請自己畫可行域、找頂點、代入比較。</p>
'''
b += H.problem(r'<div class="q">3．設 \(x \ge 0\)、\(y \ge 0\)、\(x+y \le 6\)、\(x+2y \le 8\)，求 \(z=x+3y\) 的最大值與最小值。</div>' + H.fig(SVG_BLANK))
b += H.problem(r'<div class="q">4．設 \(x \ge 0\)、\(y \ge 0\)、\(2x+y \le 10\)、\(x+y \le 7\)，求 \(z=4x+3y\) 的最大值。</div>' + H.fig(SVG_BLANK))

b += H.section_h('三、練習C', '★★★')
b += H.problem(
    r'<div class="q">5．（應用題）某工廠用 A、B 兩種原料生產甲、乙兩種產品。每件甲需 A 料 2 kg、B 料 1 kg，獲利 4 百元；每件乙需 A 料 1 kg、B 料 2 kg，獲利 3 百元。每日 A 料最多 10 kg、B 料最多 8 kg。問每日各生產甲、乙多少件，總獲利最大？最大獲利多少？</div>'
    r'<div class="hint-card">鷹架：設每日生產甲 \(x\) 件、乙 \(y\) 件。限制：\(2x+y \le 10\)（A 料）、\(x+2y \le 8\)（B 料）、\(x \ge 0\)、\(y \ge 0\)；目標 \(z=4x+3y\)（百元）。</div>'
    + H.fig(SVG_BLANK))
b += H.problem(
    r'<div class="q">6．已知可行域的頂點為 \(O(0,0)\)、\(A(4,0)\)、\(B(2,3)\)、\(C(0,4)\)（見下圖）。目標函數 \(z=ax+y\)（\(a \gt 0\)）。若 \(z\) 的最大值在頂點 \(A(4,0)\) 取得，求 \(a\) 的取值範圍。</div>'
    + H.fig(SVG_C6) + H.wlines(2))

b += '  <div class="section-h page-break">參考答案與解析</div>\n<div class="ans">\n'
b += r'''  <p><b>練習A</b></p>
  <p>1．\(B\)：\(z=5\)；\(C\)：\(z=3+6=9\)；\(D\)：\(z=8\)。最大值 \(z=9\)，在點 \(C(3,3)\) 取得。</p>
  <p>2．\(P\)：\(z=3\times1+1=4\)；\(Q\)：\(z=3\times4+1=13\)；\(R\)：\(z=3\times1+3=6\)。最大值 \(z=13\)（在 \(Q(4,1)\)）；最小值 \(z=4\)（在 \(P(1,1)\)）。</p>
  <p><b>練習B</b></p>
  <p>3．頂點 \((0,0)\)、\((6,0)\)、\((4,2)\)、\((0,4)\)。\(z=x+3y\)：\(0\)、\(6\)、\(10\)、\(12\)。最大值 \(12\)（在 \((0,4)\)）；最小值 \(0\)（在 \((0,0)\)）。〔\((4,2)\) 為 \(x+y=6\) 與 \(x+2y=8\) 的交點。〕</p>
  <p>4．頂點 \((0,0)\)、\((5,0)\)、\((3,4)\)、\((0,7)\)。\(z=4x+3y\)：\(0\)、\(20\)、\(24\)、\(21\)。最大值 \(24\)，在點 \((3,4)\) 取得。〔\((3,4)\) 為 \(2x+y=10\) 與 \(x+y=7\) 的交點。〕</p>
  <p><b>練習C</b></p>
  <p>5．頂點 \((0,0)\)、\((5,0)\)、\((4,2)\)、\((0,4)\)。\(z=4x+3y\)：\(0\)、\(20\)、\(4\times4+3\times2=22\)、\(12\)。最大值 \(22\) 百元，在 \((4,2)\) 取得：每日生產甲 4 件、乙 2 件，最大獲利 2200 元。</p>
  <p>6．各頂點的 \(z=ax+y\)：\(O\to0\)、\(A\to4a\)、\(B\to2a+3\)、\(C\to4\)。最大值在 \(A\) 取得，需 \(4a \ge 2a+3\) 且 \(4a \ge 4\)，即 \(a \ge \tfrac{3}{2}\) 且 \(a \ge 1\)，故 \(a \ge \tfrac{3}{2}\)。</p>
</div>
'''
open(os.path.join(OUT, '練習_線性規劃求最值與應用.html'), 'w', encoding='utf-8').write(
    H.build('練習：線性規劃求最值與應用', SUBJ, UNIT, '課堂練習', b, FOOT))

print('lp2 done')
