# -*- coding: utf-8 -*-
"""
build_調適練習.py — 高三理大測二 40 分鐘相似題複習（學生版＋教師答案版）

使用者 2026-11-03 指定：只有一堂（40 分鐘）複習時間，要精簡，選容易的、保證合格便可以；
相似題，相似度要高。
做法：按特別卷分數落點揀最易拎分的 16 題，逐題仿原題（題幹寫法、選項形式、小題結構照原卷，
      只改數字）；題序跟原卷「選擇→填空→解答」；正確選項位置打散；
      學生版不印測驗題號，對照表只放教師答案版。
教學設計：主 D7 提示卡（卷首公式卡＋少量一行提示），不加輔助設計。
逐題驗算見《驗算_高三理數學大測二複習.md》。
"""
import os
from sheet_common import *  # noqa

OUT = HERE
UNIT = '大測二相似題複習（40 分鐘）'
FOOTER = '高三數學．理科大測二相似題複習'
BASE = '調適練習_高三理數學大測二複習'
P = []


# ============================ 組裝 helper ============================
def section(t):
    return tight(para([('t', t)], bold=True, sz=HEADING_SZ)).replace(
        '<w:pPr>', '<w:pPr><w:keepNext/>', 1)


def item(n, stem, options=None, tip=None, work=2, cols=None):
    """一題＝題幹＋選項＋（可選）一行提示＋作答線，整格一個框。"""
    body = [tight(para(f'{n}．' + stem))]
    if tip:
        body.append(hint(tip))
    if options:
        body.append(opts(options, cols=cols))
    if work:
        body += lines(work)
    P.append(box(body))


def long_item(n, stem, parts):
    """解答題：題幹＋各小題（小題題幹、作答線行數）。"""
    body = [tight(para(f'{n}．' + stem))]
    for sstem, w in parts:
        body.append(tight(para(sstem)))
        body += lines(w)
    P.append(box(body))


# ============================ 學生版 ============================
P += [masthead(SUBJECT, UNIT, '調適練習'),
      tight(student_info_row()),
      tight(para([('t', '本練習共 16 題，一堂課完成：選擇題約 15 分鐘，填空題約 7 分鐘，解答題約 18 分鐘。'
                   '先自己做，做不出來再看公式卡或題目下的「提示」。')], sz=22)),
      spacer(80)]

FORMULAS = [
    ['冪函數：{∫x^n dx=frac(x^{n+1},n+1)+C}（{n≠-1}）', '對數：{∫frac(1,x)dx=fn(ln )x+C}（{x>0}）'],
    ['指數：{∫e^{ax}dx=frac(1,a)e^{ax}+C}', '三角：{∫fn(cos )x dx=fn(sin )x+C}'],
    ['切線：{y-y_0=f′(x_0)(x-x_0)}', '定積分：{defint(a,b,f(x)dx)=F(b)-F(a)}'],
    ['面積：上方函數減下方函數，再積分', '極值：{f′(x)} 由正變負是極大，由負變正是極小'],
]
half = (INNER_W - 300) // 2
P.append(box([tight(para([('t', '公式卡')], bold=True, sz=22)),
              grid(FORMULAS, [half, half], sz=22, head_row=False, head_col=False, jc='left')]))

P.append(section('一、選擇題'))
item(1, '不定積分 {∫(4x^3-9x^2+7)dx} 等於（    ）。', [
    '{x^4-3x^3+7x+C}', '{12x^2-18x+C}', '{x^4-9x^3+7x+C}', '{x^4-3x^3+7+C}', '{4x^4-9x^3+7x+C}'], cols=3, work=1)
item(2, '不定積分 {∫e^{-4x}dx} 等於（    ）。', [
    '{-4e^{-4x}+C}', '{frac(1,4)e^{-4x}+C}', '{e^{-4x}+C}', '{-frac(1,4)e^{-4x}+C}', '{4e^{-4x}+C}'], work=1)
item(3, '不定積分 {∫frac(x^2+5x-3,x)dx}（{x>0}）等於（    ）。', [
    '{frac(x^2,2)+5x+frac(3,x^2)+C}', '{x^2+5x-3fn(ln )x+C}', '{frac(x^2,2)+5x-3fn(ln )x+C}',
    '{frac(x^2,2)+5x+3fn(ln )x+C}', '{frac(x^2,2)+5x-frac(3,x)+C}'],
     tip='先把分子每一項除以 {x}，拆開後逐項積分。', cols=3, work=1)
item(4, '定積分 {defint(1,2,(4x+frac(1,x))dx)} 的值為（    ）。', [
    '{8+fn(ln )2}', '{6+fn(ln )2}', '{6}', '{6fn(ln )2}', '{7+fn(ln )2}'])
item(5, '定積分 {defint(0,frac(π,2),(4x+fn(cos )x)dx)} 的值為（    ）。', [
    '{frac(π^2,2)+1}', '{frac(π^2,2)-1}', '{frac(π^2,4)+1}', '{frac(π,2)+1}', '{frac(π^2,2)}'])
item(6, '曲線 {y=x^3-2x+1} 在點 {(2,5)} 處的切線方程為（    ）。', [
    '{y=10x-25}', '{y=10x-15}', '{y=-10x+25}', '{y=10x+15}', '{y=12x-19}'], cols=3)
item(7, '函數 {f(x)=x^3+6x^2-5} 的圖形之反曲點為（    ）。', [
    '{(0,-5)}', '{(2,27)}', '{(-2,11)}', '{(-2,-11)}', '{(-1,0)}'],
     tip='令 {f″(x)=0}，再把所得的 {x} 代入 {f(x)}。')
item(8, '設 {g(x)=defint(1,x,(t^2+2)dt)}，則 {g′(2)} 等於（    ）。', [
    '{0}', '{4}', '{frac(13,3)}', '{6}', '{2}'], work=1)
item(9, '曲線 {y=x^2-2x}、{x} 軸及直線 {x=0}、{x=2} 所圍成的面積為（    ）。', [
    '{-frac(4,3)}', '{4}', '{frac(8,3)}', '{frac(2,3)}', '{frac(4,3)}'],
     tip='在 {0<x<2} 時曲線在 {x} 軸下方，要用 {-(x^2-2x)} 來積分。')
item(10, '曲線 {y=frac(1,x)} 與直線 {x=1}、{x=4} 及 {x} 軸所圍成的面積為（    ）。', [
    '{fn(ln )4}', '{frac(3,4)}', '{3}', '{fn(ln )3}', '{1+fn(ln )4}'], work=1)

P.append(section('二、填空題'))
item(11, '拋物線 {y=x^2+4} 與直線 {y=5x} 所圍成的封閉圖形面積為＿＿＿＿＿＿。', work=4)
item(12, '{∫x^2 sqrt(2+x^3)dx}＝＿＿＿＿＿＿。',
     tip='設 {u=2+x^3}，則 {x^2 dx=frac(1,3)du}。', work=3)
item(13, '{defint(1,2,(x-frac(1,x))^2 dx)}＝＿＿＿＿＿＿。',
     tip='{(x-frac(1,x))^2=x^2-2+x^{-2}}，{∫x^{-2}dx=-frac(1,x)+C}。', work=4)

P.append(section('三、解答題'))
P.append(box([tight(para('14．求不定積分 {∫(9x^2-frac(2,x)+5e^x)dx}，其中 {x>0}。'))] + lines(2)))
long_item(15, '已知函數 {f(x)=x^3+3x^2-9x+2}。', [
    ('(1) 求 {f′(x)}，並求使 {f′(x)=0} 的 {x} 值。', 3),
    ('(2) 求 {f(x)} 的單調遞增區間及單調遞減區間。', 3),
    ('(3) 求 {f(x)} 的局部極大值與局部極小值，並寫出相應的極值點坐標。', 3),
])
long_item(16, '已知拋物線 {y=x^2-x} 與直線 {y=x+3}。', [
    ('(1) 求兩者的交點坐標。', 3),
    ('(2) 判斷兩交點之間哪一條在上方，並列出所圍面積的定積分式。', 2),
    ('(3) 求所圍成的封閉圖形面積。', 4),
])

P.append(tail_stub())
build_docx(P, os.path.join(OUT, f'{BASE}_學生版.docx'), footer_text=FOOTER)


# ============================ 教師答案版 ============================
T = [masthead(SUBJECT, UNIT, '調適練習・教師答案版'),
     tight(para([('t', '本版供教師批改使用，不發給學生。每題仿特別卷對應題目（題幹與選項形式相同、數字全改）；'
                  '全部答案為獨立驗算所得，逐題紀錄見《驗算_高三理數學大測二複習.md》。')], sz=22)),
     section('一、選擇題答案（1–10）')]
MC = dict(zip(range(1, 11), 'ADCBABCDEA'))
T.append(box([tight(para([('t', '　　'.join(f'{n}．{MC[n]}' for n in r))]))
              for r in (range(1, 6), range(6, 11))], keep=False))

T.append(section('二、選擇題要點'))
KEY = [
    '1．逐項積分，{x^4-3x^3+7x+C}。',
    '2．{a=-4}，{-frac(1,4)e^{-4x}+C}。',
    '3．{frac(x^2+5x-3,x)=x+5-frac(3,x)}；積分得 {frac(x^2,2)+5x-3fn(ln )x+C}。',
    '4．原函數 {2x^2+fn(ln )x}；{(8+fn(ln )2)-(2+0)=6+fn(ln )2}。',
    '5．原函數 {2x^2+fn(sin )x}；代上限得 {frac(π^2,2)+1}，代下限得 {0}。',
    '6．{y′=3x^2-2}，{x=2} 時斜率 {10}；{y-5=10(x-2)}，即 {y=10x-15}（漏 {-2} 得 E）。',
    '7．{f″(x)=6x+12}，{x=-2}，{f(-2)=11}，反曲點 {(-2,11)}。',
    '8．{g′(x)=x^2+2}，{g′(2)=6}（{frac(13,3)} 是 {g(2)}，誘答）。',
    '9．{S=defint(0,2,(2x-x^2)dx)}，{S=4-frac(8,3)}，{S=frac(4,3)}。',
    '10．{S=evalat(fn(ln )x,1,4)}，{S=fn(ln )4}。',
]
T.append(box([tight(para(x)) for x in KEY], keep=False))

T.append(section('三、填空題及解答題（11–16）'))
ANS = [
    ['11．{x^2-5x+4=0}，{x=1} 或 {x=4}。', '　{S=defint(1,4,(5x-x^2-4)dx)}', '　{S=frac(9,2)}'],
    ['12．原式 {=frac(1,3)∫u^{frac(1,2)}du}', '　原式 {=frac(2,9)(2+x^3)^{frac(3,2)}+C}'],
    ['13．原式 {=evalat(frac(x^3,3)-2x-frac(1,x),1,2)}', '　原式 {=-frac(11,6)-(-frac(8,3))}', '　原式 {=frac(5,6)}'],
    ['14．{3x^3-2fn(ln )x+5e^x+C}'],
    ['15．(1) {f′(x)=3x^2+6x-9}', '　{f′(x)=3(x+3)(x-1)}', '　{x=-3} 或 {x=1}',
     '　(2) 遞增區間：{(-∞,-3)} 及 {(1,+∞)}；遞減區間：{(-3,1)}。',
     '　(3) 局部極大值 {f(-3)=29}，極大值點 {(-3,29)}。',
     '　局部極小值 {f(1)=-3}，極小值點 {(1,-3)}。'],
    ['16．(1) {x^2-x=x+3}', '　{(x-3)(x+1)=0}', '　{x=3} 或 {x=-1}', '　交點為 {(-1,2)} 及 {(3,6)}。',
     '　(2) 當 {-1<x<3} 時直線在上方；{S=defint(-1,3,(-x^2+2x+3)dx)}。',
     '　(3) {S=evalat(-frac(x^3,3)+x^2+3x,-1,3)}', '　{S=9-(-frac(5,3))}', '　{S=frac(32,3)}'],
]
for blk in ANS:
    T.append(box([tight(para(x)) for x in blk]))

T.append(section('四、對應特別卷').replace('<w:keepNext/>', '<w:keepNext/><w:pageBreakBefore/>', 1))
W3 = INNER_W - 300
COVER = [
    ['類別', '本練習→特別卷題號', '分數'],
    ['仿原題', '1→1、2→4、3→5、4→7、5→9、6→12、7→13、8→15、9→16、10→17、'
     '11→25、14→26(1)、15→27、16→28', '55'],
    ['同一技能（不另出題）', '特別卷第 2、8、14、24 題', '12'],
    ['跟提示做', '12→22、13→23；同法：3、11、18、19、20、21、26(2)', '28'],
    ['本堂不練', '特別卷第 6、10、29、30 題', '25'],
]
T.append(grid(COVER, [W3 * 3 // 10, W3 * 6 // 10, W3 // 10], sz=22, head_col=False))
T.append(spacer(80))
for t_ in [
    '合格線按 60%（72／120）估算：前兩類 67 分做對八成半約 57 分，跟提示做 28 分做對六成約 17 分，合共約 74 分。'
    '這是估算，不能保證；第 29、30 題有分步填空，亦可能再拿部分分數。',
    '時間（40 分鐘）：選擇題 15 分鐘；填空題 7 分鐘；解答題 18 分鐘。時間不夠時先保第 15、16 題（各對應 9 分解答題）。',
    '正確選項位置已打散，不與測驗答案位置對應。',
]:
    T.append(tight(para(t_, sz=22)))

build_docx(T, os.path.join(OUT, f'{BASE}_教師答案版.docx'), footer_text=FOOTER)
print('OK', BASE)
