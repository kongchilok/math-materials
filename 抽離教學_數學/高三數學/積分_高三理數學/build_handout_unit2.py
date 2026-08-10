# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 定積分（13.3 概念與計算 + 13.4 幾何應用，精簡2節版）
# 主設計 D6 明確教學三階段；輔助 D11 標記對應（①②③④貫穿「求原函數→代入上限→代入下限→相減」）、D2 手順卡
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '定積分（概念、計算與幾何應用）'
FOOTER = '高三數學．定積分單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

# ---------------- 一、定積分的概念（13.3） ----------------
P.append(heading('一、什麼是定積分（承接不定積分）'))
P.append(para('上一課學了「不定積分」——求回原函數，答案裡有個不確定的C。這一課的「定積分」是把原函數在兩個特定點的值相減，C 會自動抵消，答案是一個確定的數字（不再有C）。'))
P.append(shaded_box('定積分記做 {∫[a,b] f(x)dx}，a 叫下限、b 叫上限。幾何意義：當 f(x)≥0，它代表函數圖形與x軸、直線x=a、x=b 圍出來的「曲邊梯形」面積。'))
P.append(blank())

P.append(heading('二、公式卡：牛頓－萊布尼茨公式（怎麼算出定積分）'))
P.append(shaded_box("若 {F'(x)=f(x)}，則 {∫[a,b] f(x)dx=F(b)−F(a)}　　（求出原函數後，代入上限、下限相減，就是答案）"))
P.append(blank())

# ---------------- 三、範例：我做1 → 我們做1（13.3計算，D2+D11） ----------------
P.append(heading('三、範例：求 ∫₁³(2x+1)dx（我做——老師先示範一次）'))
P.append(shaded_box('固定四步驟，跟不定積分單元同一套邏輯，只是多了「代入上下限相減」。算式裡每一項都標了同一個號碼①②③④，代表同一件事在不同步驟的樣子。', kind='worked', keep_next=True))
P.append(worked_example_table([
    span_row('① 先求被積函數的一個原函數（不用加C，因為相減時C會抵消）：{F(x)=x^2+x}'),
    eq_row('{F(3)}', '{3^2+3=12}', '② 代入上限 b=3'),
    eq_row('{F(1)}', '{1^2+1=2}', '③ 代入下限 a=1'),
    answer_row('{∫[1,3](2x+1)dx=F(3)−F(1)=12−2=10}', '④ 上限的值減下限的值'),
], why_pct=0.4))
P.append(shaded_box('雙重檢查：這條函數是直線，圖形剛好是梯形——x=1時y=3，x=3時y=7，梯形面積=(3+7)/2×2=10，跟算出來的一樣，可以互相驗證。'))
P.append(blank())

P.append(heading('四、範例：求 ∫₀²3x²dx（我們做——你跟老師一起完成）'))
P.append(para('照「我做」的四個步驟自己走一次，每一步寫在下面：'))
P.append(shaded_box('{∫[0,2] 3x^2 dx=?}　　（提示：先求原函數，再代入上限2、下限0，最後相減）'))
P.extend(write_lines(4))
P.append(blank())

# ---------------- 五、13.4 幾何應用：我做2 → 我們做2 ----------------
P.append(heading('五、公式卡：定積分求平面圖形面積'))
P.append(shaded_box('若 f(x)≥0，曲線 y=f(x) 與x軸、直線x=a、x=b 圍成的面積：{S=∫[a,b] f(x)dx}'))
P.append(shaded_box('⚠ 陷阱：若 f(x) 在區間內有正有負（圖形一部份在x軸上方、一部份在下方），不能直接整段積分——正負會互相抵消，算出來的不是面積。要先分段、負的部份取絕對值，再相加（練習C會考這一點）。'))
P.append(image_para(os.path.join(OUT, '_assets', 'fig_area_sign_trap.png'), width_cm=7.0,
                     caption='y=x 在 [−1,2]：陰影一部分在x軸下方（x從−1到0）、一部分在上方（x從0到2）——直接整段積分兩部分會互相抵消，不是實際面積，一定要先分段、負的部分取絕對值再相加。'))
P.append(blank())

P.append(heading('六、範例：求 y=x²、x=0、x=2、x軸所圍的面積（我做——老師先示範一次）'))
P.append(shaded_box('面積應用只是多一步：先確認 f(x)≥0（這裡 x²≥0 恆成立），再直接套用定積分公式。', kind='worked', keep_next=True))
P.append(image_para(os.path.join(OUT, '_assets', 'fig_area_trapezoid.png'), width_cm=7.0,
                     caption='y=x² 在 [0,2] 與x軸圍成的曲邊梯形——陰影部分就是要求的面積 S。'))
P.append(worked_example_table([
    span_row('{S=∫[0,2] x^2 dx}', '① 寫出面積公式'),
    span_row('{F(x)=frac(x^3,3)}', '② 求原函數'),
    answer_row('{F(2)−F(0)=frac(8,3)−0=frac(8,3)}', '③④ 代入上下限相減'),
], why_pct=0.4))
P.append(blank())

P.append(heading('七、範例：求 y=2x、x=1、x=3、x軸所圍的面積（我們做——你跟老師一起完成）'))
P.append(para('先確認 f(x)=2x 在 [1,3] 是否≥0，再照「我做」的步驟自己走一次：'))
P.append(shaded_box('{S=∫[1,3] 2x dx=?}　　（提示：先求原函數 F(x)，再代入上限3、下限1相減）'))
P.extend(write_lines(4))

P.append(shaded_box('接下來請拿《定積分——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

# ---------------- 教師實施說明頁 ----------------
P.extend(teacher_notes(
    main_design='D6 明確教學三階段（我做－我們做－你做）',
    aux_designs=('D11 標記對應', 'D2 手順卡'),
    reason='延續不定積分單元同一套設計邏輯（S2結構：多步驟程序運算）。13.3定積分計算新增'
           '「代入上下限相減」兩步，13.4面積應用是13.3的直接延伸，認知負荷來自「多一層應用情境」'
           '而非全新概念，故沿用同一主設計不重新導入。ASD學生受益於流程一致性——同一套四步驟框架'
           '貫穿兩節課，減少額外的規則切換負荷。',
    density='抽離小班（Tier 2）：練習A/B/C各2題',
    fading='D2手順卡：完整版（工具卡：求原函數→代入上限→代入下限→相減）→只留關鍵詞清單→只留'
           '步驟數量提示→完全移除。D11標記：練習A不需要（單步驟直接代公式）→練習B給滿①②③④→'
           '練習C不給，學生自己走流程。',
    flows=('F5 課前流程預告（今天兩件事：定積分怎麼算→定積分怎麼求面積）',
           'F2 番茄鐘分段（配合練習B/C之間的核對點）'),
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
    extra=[('範圍說明（教師參考）',
            '體積應用（旋轉體積分）因課時由4節壓縮為2節，本份完全未納入教學與練習，'
            '聚焦在「定積分計算」與「平面圖形面積」兩個核心技能；如學生需要體積應用，'
            '建議另外安排課時補課，不建議與本份內容混合教。')],
))

out1 = build_docx(P, os.path.join(OUT, '講義_定積分_抽離小班共用版.docx'), footer_text=FOOTER)
print(out1)
