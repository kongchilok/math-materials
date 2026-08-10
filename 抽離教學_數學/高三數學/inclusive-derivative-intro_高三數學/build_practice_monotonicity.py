# -*- coding: utf-8 -*-
# 練習（練習A/B/C＋教師用答案）—— 導數在研究函數中的應用（單調性與極值）
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

P = []

P.append(masthead('高三數學', '導數在研究函數中的應用（單調性與極值）', '課堂練習'))
P.append(student_info_row())
P.append(shaded_box([('t', '請先讀《導數在研究函數中的應用（單調性與極值）——課堂講義》的「範例」，練習B會用到同一套四步驟框架。')], kind='hint'))

# 練習A（初階）
P.append(heading(f'一、練習A（{star_label(1)}）—— 判斷單調性（選擇題，3選項）'))
P.append(problem_box([
    para([('t', '1．f(x) = −2x+1，f\'(x) = −2。這個函數在定義域上的單調性是（　　）')]),
    para([('t', 'A．單調遞增')]),
    para([('t', 'B．單調遞減')]),
    para([('t', 'C．無法判斷')]),
] + write_lines(2)))
P.append(problem_box([
    para([('t', '2．'), ('m', omath(mr('f(x)='), sup(mr('x'), mr('2')), mr('−2x+4'))), ('t', '，f\'(x) = ______（先求導數）。')]),
    para([('t', '當 '), ('m', omath(mr('x > 1'))), ('t', ' 時，f(x) 是（　　）')]),
    para([('t', 'A．單調遞增')]),
    para([('t', 'B．單調遞減')]),
    para([('t', 'C．不確定')]),
] + write_lines(3)))
P.append(problem_box([
    para([('t', '3．已知 '), ('m', omath(mr('f(x)='), sup(mr('e'), mr('x')), mr('−x'))), ('t', '，求 '), ('m', omath(mr("f'(x)=")))]),
] + write_lines(2)))

# 練習B（中階）
P.append(heading(f'二、練習B（{star_label(2)}）—— 求單調區間與極值（依「講義」範例的四步驟框架作答）'))
P.append(problem_box([
    para([('t', '4．求函數 '), ('m', omath(mr('f(x)=2'), sup(mr('x'), mr('3')), mr('−6'), sup(mr('x'), mr('2')), mr('+7'))),
          ('t', ' 的單調區間，並求出極大值與極小值。')]),
] + write_lines(6)))
P.append(problem_box([
    para([('t', '5．求函數 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('3')), mr('+3x'))), ('t', ' 的單調區間。')]),
    para([('t', '（提示：先求 f\'(x)，再看看 f\'(x)=0 有沒有解——每個函數不一定都有極值！）')]),
] + write_lines(5)))

# 練習C（高階）
P.append(heading(f'三、練習C（{star_label(3)}）—— 極值、最值與情境應用'))
P.append(problem_box([
    para([('t', '6．求函數 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('3')), mr('−27x'))), ('t', ' 的極大值與極小值。')]),
] + write_lines(4)))
P.append(problem_box([
    para([('t', '7．求函數 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('3')), mr('−27x'))),
          ('t', ' 在閉區間 [−4，4] 上的最大值與最小值。（提示：把極值和兩端點 f(−4)、f(4) 一起比較）')]),
] + write_lines(4)))
P.append(problem_box([
    para([('t', '8．某工廠某產品的日產量為 x 公噸時，獲利函數為 '),
          ('m', omath(mr('P(x)=−'), sup(mr('x'), mr('3')), mr('+9'), sup(mr('x'), mr('2')))),
          ('t', '（單位：萬元），其中 x∈[0，8]。請問日產量為多少公噸時獲利最大？最大獲利是多少萬元？')]),
] + write_lines(5)))

P.append(pagebreak())
P.append(heading('教師用：參考答案'))
P.append(para([('t', '1．B（遞減，因為 f\'(x) = −2 < 0 對所有 x 成立）')]))
P.append(para([('t', '2．f\'(x)=2x−2；x > 1 時 f\'(x) > 0 → A（遞增）')]))
P.append(para([('t', '3．f\'(x)=eˣ−1')]))
P.append(para([('t', '4．f\'(x)=6x²−12x=6x(x−2)，零點 x=0, 2。x < 0 遞增、0 < x < 2 遞減、x > 2 遞增。')]))
P.append(para([('t', '　極大值 f(0)=7；極小值 f(2)=2(8)−6(4)+7=−1')]))
P.append(para([('t', '5．f\'(x)=3x²+3，對所有 x 恆正（永遠 > 0），所以 f(x) 在整個定義域 R 上都是單調遞增，沒有極值。')]))
P.append(para([('t', '6．f\'(x)=3x²−27=3(x−3)(x+3)，零點 x=−3, 3。極大值 f(−3)=−27+81=54；極小值 f(3)=27−81=−54')]))
P.append(para([('t', '7．候選值：f(−4)=−64+108=44、f(−3)=54、f(3)=−54、f(4)=64−108=−44。')]))
P.append(para([('t', '　最大值＝54（於 x=−3）；最小值＝−54（於 x=3）')]))
P.append(para([('t', '8．P\'(x)=−3x²+18x=−3x(x−6)，零點 x=0, 6（x=0為端點）。0 < x < 6 時遞增、6 < x < 8 時遞減，x=6為極大。')]))
P.append(para([('t', '　候選值：P(0)=0、P(6)=−216+324=108、P(8)=−512+576=64。')]))
P.append(para([('t', '　答：日產量 6 公噸時獲利最大，最大獲利 108 萬元。')]))

out = build_docx(
    P,
    r'C:\Users\KongChiLok\notebookLM\inclusive-derivative-intro_高三數學\練習_導數在研究函數中的應用(單調性與極值)_抽離小班共用版.docx',
    footer_text='高三數學．單調性與極值單元',
)
print(out)
