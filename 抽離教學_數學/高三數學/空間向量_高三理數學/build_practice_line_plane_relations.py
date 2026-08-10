# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 向量法判斷直線與平面的位置關係
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '向量法判斷直線與平面的位置關係'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(shaded_box('公式卡：線線垂直 {vec(v_1)·vec(v_2)=0}　　法向量求法：{vec(n)·vec(a)=0} 且 {vec(n)·vec(b)=0}（a,b是平面內兩個不共線向量）　　{vec(v)∥vec(n)} ⟺ 直線垂直平面'))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 基本判斷'))
P.append(problem_box([
    para('1．直線 l 的方向向量 {vec(v)=(1,2,-2)}，直線 m 的方向向量 {vec(u)=(2,-2,-1)}，求 {vec(v)·vec(u)}，並判斷 l 與 m 是否垂直。'),
] + write_lines(4)))
P.append(problem_box([
    para('2．平面 α 的法向量 {vec(n)=(1,-2,2)}，直線 l 的方向向量 {vec(v)=(2,-4,4)}，判斷 l 是否垂直於 α。'),
] + write_lines(4)))
P.append(problem_box([
    para('3．已知向量 {vec(a)=(1,-1,0)}、{vec(b)=(0,1,-1)} 是平面 α 內兩個向量，判斷 {vec(n)=(1,1,1)} 是否可能是 α 的法向量。'),
] + write_lines(4)))

P.append(heading(f'練習B（{star_label(2)}）—— 求法向量、線面角前置'))
P.append(problem_box([
    para('4．直線 l 的方向向量 {vec(v)=(1,1,0)}，直線 m 的方向向量 {vec(u)=(-1,0,1)}，求 l 與 m 所成角的餘弦值。'),
    shaded_box('提示：先求 {vec(v)·vec(u)}——留意結果係負數，記住線線角公式要加絕對值。'),
] + write_lines(5)))
P.append(problem_box([
    para('5．求經過三點 {A(1,0,0)}、{B(0,1,0)}、{C(0,0,1)} 的平面的一個法向量。'),
] + write_lines(6)))
P.append(problem_box([
    para('6．平面 α 的法向量 {vec(n)=(2,-1,3)}，{A(1,2,0)}、{B(3,1,2)}，判斷 AB 是否垂直於 α。'),
    shaded_box('提示：求出 {vec(AB)} 嘅坐標，睇下同 {vec(n)} 是否平行（各分量比例要全部相等）。'),
] + write_lines(5)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('7．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系（同講義一樣）。求平面 {A_1BC_1} 的一個法向量，並判斷體對角線 {DB_1} 是否垂直於平面 {A_1BC_1}。'),
    shaded_box('提示：先寫出 {A_1}、B、{C_1} 的坐標，用兩個平面內向量列方程求法向量；再睇下 {vec(DB_1)} 是否同法向量平行。'),
] + write_lines(9)))
P.append(problem_box([
    para('8．已知空間三點 {A(0,0,0)}、{B(1,0,1)}、{C(0,1,1)}（不共線），直線 l 的方向向量 {vec(v)=(1,1,-1)}，判斷 l 是否垂直於平面 {ABC}。'),
    shaded_box('提示：先求平面ABC的一個法向量，再同 {vec(v)} 比較。'),
] + write_lines(6), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{vec(v)·vec(u)=2-4+2=0}，所以 {l⊥m}。'))
P.append(para('2．{vec(v)=2*vec(n)}，兩者平行，所以 {l⊥α}。'))
P.append(para('3．{vec(n)·vec(a)=1-1+0=0}，{vec(n)·vec(b)=0+1-1=0}，兩個都成立，所以 {vec(n)} 可能是 α 的法向量。'))
P.append(para('4．{fn(cos)θ=frac(1,2)}（{vec(v)·vec(u)=-1+0+0=-1}，{|vec(v)|=sqrt(2)}，{|vec(u)|=sqrt(2)}，{fn(cos)θ=frac(|-1|,sqrt(2)*sqrt(2))=frac(1,2)}，即60°——留意夾角本身係120°，但線線角要取絕對值變60°）'))
P.append(para('5．{vec(n)=(1,1,1)}（{vec(AB)=(-1,1,0)}，{vec(AC)=(-1,0,1)}，列方程 {-x+y=0} 同 {-x+z=0}，解得 {x=y=z}，設x=1）'))
P.append(para('6．不垂直。{vec(AB)=(2,-1,2)}，同 {vec(n)=(2,-1,3)} 比較：{frac(2,2)=1}，{frac(-1,-1)=1}，{frac(2,3)≠1}，三個比值不相等，所以 {vec(AB)} 不平行於 {vec(n)}，AB不垂直於α。'))
P.append(para('7．{vec(n)=(1,1,1)}；{vec(DB_1)=(2,2,2)=2*vec(n)}，平行，所以體對角線 {DB_1} 垂直於平面 {A_1BC_1}。（呢個係經典結果：正方體嘅體對角線垂直於「相隔一個頂點」嘅三點所成嘅平面，詳見驗算記錄）'))
P.append(para('8．{vec(v)=(1,1,-1)} 剛好等於平面ABC的法向量 {vec(n)=(1,1,-1)}（詳見驗算記錄的求法過程），兩者平行，所以直線 {l} 垂直於平面 {ABC}。'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_向量法判斷直線與平面的位置關係_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
