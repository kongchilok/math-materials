# -*- coding: utf-8 -*-
# 練習（練習A/B/C＋教師用答案）—— 導數在研究函數中的應用（單調性與極值）
# 2026-08-12：從舊資料夾 inclusive-derivative-intro_高三數學 搬入本資料夾，
# 順道改用 {} 標記語法統一風格（原為手寫 omath()），並修正輸出路徑（原本誤指
# 向已停用的舊碟舊資料夾 C:\Users\KongChiLok\notebookLM\...，改寫回本檔所在資料夾）。
# 內容與答案數值完全不變。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '導數在研究函數中的應用（單調性與極值）'
FOOTER = '高三數學．單調性與極值單元'

P = []

P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(shaded_box('請先讀《導數在研究函數中的應用（單調性與極值）——課堂講義》的「範例」，練習B會用到同一套四步驟框架。'))
P.append(blank())

# 練習A（初階）
P.append(heading(f'一、練習A（{star_label(1)}）—— 判斷單調性（選擇題，3選項）'))
P.append(problem_box([
    para('1．{f(x)=-2x+1}，{f\'(x)=-2}。這個函數在定義域上的單調性是（　　）'),
    para('　　A．單調遞增　　B．單調遞減　　C．無法判斷'),
] + write_lines(2)))
P.append(problem_box([
    para('2．{f(x)=x^2-2x+4}，{f\'(x)=} ______（先求導數）。'),
    para('當 {x>1} 時，f(x) 是（　　）'),
    para('　　A．單調遞增　　B．單調遞減　　C．不確定'),
] + write_lines(3)))
P.append(problem_box([
    para('3．已知 {f(x)=e^x-x}，求 {f\'(x)=}'),
] + write_lines(2)))

# 練習B（中階）
P.append(heading(f'二、練習B（{star_label(2)}）—— 求單調區間與極值（依「講義」範例的四步驟框架作答）'))
P.append(problem_box([
    para('4．求函數 {f(x)=2x^3-6x^2+7} 的單調區間，並求出極大值與極小值。'),
] + write_lines(6)))
P.append(problem_box([
    para('5．求函數 {f(x)=x^3+3x} 的單調區間。'),
    para('（提示：先求 {f\'(x)}，再看看 {f\'(x)=0} 有沒有解——每個函數不一定都有極值！）'),
] + write_lines(5)))

# 練習C（高階）
P.append(heading(f'三、練習C（{star_label(3)}）—— 極值、最值與情境應用'))
P.append(problem_box([
    para('6．求函數 {f(x)=x^3-27x} 的極大值與極小值。'),
] + write_lines(4)))
P.append(problem_box([
    para('7．求函數 {f(x)=x^3-27x} 在閉區間 [−4，4] 上的最大值與最小值。（提示：把極值和兩端點 f(−4)、f(4) 一起比較）'),
] + write_lines(4)))
P.append(problem_box([
    para('8．某工廠某產品的日產量為 x 公噸時，獲利函數為 {P(x)=-x^3+9x^2}（單位：萬元），其中 {x∈[0,8]}。請問日產量為多少公噸時獲利最大？最大獲利是多少萬元？'),
] + write_lines(5), trailing_blank=False))

P.append(pagebreak())
P.append(heading('教師用：參考答案'))
P.append(para('1．B（遞減，因為 {f\'(x)=-2<0} 對所有 x 成立）'))
P.append(para('2．{f\'(x)=2x-2}；{x>1} 時 {f\'(x)>0} → A（遞增）'))
P.append(para('3．{f\'(x)=e^x-1}'))
P.append(para('4．{f\'(x)=6x^2-12x=6x(x-2)}，零點 {x=0,2}。{x<0} 遞增、{0<x<2} 遞減、{x>2} 遞增。'))
P.append(para('　極大值 {f(0)=7}；極小值 {f(2)=2(8)-6(4)+7=-1}'))
P.append(para('5．{f\'(x)=3x^2+3}，對所有 x 恆正（永遠 {>0}），所以 f(x) 在整個定義域 R 上都是單調遞增，沒有極值。'))
P.append(para('6．{f\'(x)=3x^2-27=3(x-3)(x+3)}，零點 {x=-3,3}。極大值 {f(-3)=-27+81=54}；極小值 {f(3)=27-81=-54}'))
P.append(para('7．候選值：{f(-4)=-64+108=44}、{f(-3)=54}、{f(3)=-54}、{f(4)=64-108=-44}。'))
P.append(para('　最大值＝54（於 x=−3）；最小值＝−54（於 x=3）'))
P.append(para('8．{P\'(x)=-3x^2+18x=-3x(x-6)}，零點 {x=0,6}（x=0為端點）。{0<x<6} 時遞增、{6<x<8} 時遞減，x=6為極大。'))
P.append(para('　候選值：{P(0)=0}、{P(6)=-216+324=108}、{P(8)=-512+576=64}。'))
P.append(para('　答：日產量 6 公噸時獲利最大，最大獲利 108 萬元。'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_導數在研究函數中的應用(單調性與極值)_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
