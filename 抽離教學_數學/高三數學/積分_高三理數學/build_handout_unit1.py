# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 不定積分（13.1 定義 + 13.2 運算法則）
# 主設計 D6 明確教學三階段；輔助 D11 標記對應（①②③貫穿多項式運算法則的三個階段）、D2 手順卡
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '不定積分（定義與運算法則）'
FOOTER = '高三數學．不定積分單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

# ---------------- 一、不定積分的定義（13.1，明確教學三階段之「我做」前置） ----------------
P.append(heading('一、什麼是不定積分（由導數反過來想）'))
P.append(para("導數是「已知函數，求變化率」；不定積分是它的逆運算——「已知變化率，求回原本的函數」。"))
P.append(shaded_box("若 {F'(x)=f(x)}，就稱 F(x) 是 f(x) 的一個原函數。f(x) 所有原函數的集合，記做 {∫f(x)dx}（讀作「f(x) 的不定積分」），寫成 {∫f(x)dx=F(x)+C}（C 是任意常數，叫積分常數）。"))
P.append(para('為什麼要加 C：把 F(x) 求導會得到 f(x)，但 F(x)+1、F(x)+5……求導也一樣得到 f(x)（常數的導數是 0）。所以「所有」原函數要用 F(x)+C 一次寫完，C 代表這個不確定的常數。'))
P.append(blank())

# ---------------- 二、公式卡：基本初等函數的不定積分公式（查表用，不推導） ----------------
P.append(heading('二、公式卡：基本初等函數的不定積分公式'))
P.append(para('這些是「查表就能用」的固定公式——每一條都可以用「求導數」反過來驗證（例如驗證第2條：把 {x^{n+1}/(n+1)} 求導，剛好得到 {x^n}）。之後每一題都是套用這些公式，不用重新推導。'))
P.append(shaded_box('1．{∫0 dx=C}'))
P.append(shaded_box('2．{∫x^n dx=frac(x^{n+1},n+1)+C}　　（n≠−1，這個限制很重要，練習C會考這一點）'))
P.append(shaded_box('3．{∫frac(1,x) dx=fn(ln)|x|+C}'))
P.append(shaded_box('4．{∫e^x dx=e^x+C}'))
P.append(shaded_box('5．{∫a^x dx=frac(a^x,fn(ln) a)+C}　　（a>0 且 a≠1）'))
P.append(shaded_box('6．{∫fn(cos) x dx=fn(sin) x+C}'))
P.append(shaded_box('7．{∫fn(sin) x dx=−fn(cos) x+C}'))
P.append(blank())

# ---------------- 三、公式卡：不定積分的運算法則 ----------------
P.append(heading('三、公式卡：不定積分的運算法則（13.2）'))
P.append(shaded_box('常數倍法則：{∫k*f(x) dx=k∫f(x) dx}　　（k 是常數，把係數整個提出來）'))
P.append(shaded_box('和差法則：{∫[f(x)±g(x)] dx=∫f(x) dx±∫g(x) dx}　　（幾項相加減，可以逐項分開算）'))
P.append(para('這兩條法則合起來用，就能把「一個多項式的不定積分」拆成「每一項分別查公式卡」再合併。'))
P.append(blank())

# ---------------- 四、範例：我做 → 我們做（D6 + D11標記對應） ----------------
P.append(heading('四、範例：求 ∫(6x²−4x+3)dx（我做——老師先示範一次）'))
P.append(shaded_box('跟著這套固定流程走，之後每一題（不管幾項）都用同一套框架。留意：算式裡每一項都標了同一個號碼①②③，代表「原式這一項」一路對應到「答案這一項」，是同一件事，只是換了個樣子。', kind='worked', keep_next=True))
P.append(worked_example_table([
    span_row('{∫(①6x^2②−4x③+3) dx}', '① 先看清楚是幾項相加減，逐項標號'),
    span_row('{①6∫x^2 dx②−4∫x dx③+3∫1 dx}', '② 用和差法則拆開，每項再用常數倍法則提出係數'),
    span_row('{①6*frac(x^3,3)②−4*frac(x^2,2)③+3x}', '③ 對每項套用公式卡第2條逐項計算'),
    span_row('{①2x^3②−2x^2③+3x}', '④ 化簡每一項'),
    answer_row('{2x^3−2x^2+3x+C}', '⑤ 所有項合併，最後只加「一個」C（不是每項各加一個C）'),
], why_pct=0.4))
P.append(blank())

P.append(heading('五、範例：求 ∫(9x²+2x−5)dx（我們做——你跟老師一起完成）'))
P.append(para('先幫每一項標號，再照「我做」的五個步驟自己走一次，每一步寫在下面：'))
P.append(shaded_box('{∫(①9x^2②+2x③−5) dx = ?}　　（提示：跟「我做」一樣，先拆項、提係數，再查公式卡第2條）'))
P.extend(write_lines(4))

P.append(shaded_box('接下來請拿《不定積分——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

# ---------------- 教師實施說明頁 ----------------
P.extend(teacher_notes(
    main_design='D6 明確教學三階段（我做－我們做－你做）',
    aux_designs=('D11 標記對應', 'D2 手順卡'),
    reason='13.1不定積分定義為全新概念導入（S10結構），需要放聲思考＋預告流程；13.2運算法則為多步驟程序運算'
           '（S2結構），易在拆項/提係數/加C時序列崩潰。學生為ASD，語義理解與執行功能較弱，'
           '需標記對應把「原式各項」與「答案各項」連成同一件事，並用手順卡把內隱步驟外顯化。',
    density='抽離小班（Tier 2）：練習A/B/C各2題；練習B區塊開頭放一次手順卡精簡版',
    fading='D2手順卡：完整版（工具卡）→只留關鍵詞清單（拆項/提係數/套公式/加C）→只留步驟數量提示'
           '（「這題有四步」）→完全移除。D11標記：練習A不需要（單項無跨項對應問題）→練習B給滿①②③'
           '→練習C不給，學生自己劃分。',
    flows=('F5 課前流程預告（上課前展示今天四件事：複習導數→公式卡→我做我們做→練習）',
           'F2 番茄鐘分段（配合練習B/C之間的核對點）'),
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
))

out1 = build_docx(P, os.path.join(OUT, '講義_不定積分_抽離小班共用版.docx'), footer_text=FOOTER)
print(out1)
