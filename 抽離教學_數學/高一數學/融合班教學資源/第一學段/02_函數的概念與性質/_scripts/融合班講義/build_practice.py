# -*- coding: utf-8 -*-
"""練習_函數的概念與定義域_高一數學.docx 產生腳本（2026-08-07 按最新規則重出）。
三層次（A初階/B中階/C高階）同源同概念：函數定義域的求法＋同一函數的判斷。
教學設計：輔 D2 手順卡（褪除：A 每題重印精簡步驟號／B 區塊開頭一次／C 不放）
         ＋輔 D12 自我核對清單（每區塊末尾）。題目一律用 aside_layout：左題目＋作答，右提示。
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

SUBJECT = '高一數學'
UNIT = '函數的概念與定義域'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(para('請先複習《函數的概念與定義域課堂講義》的手順卡，再用同一套「①根式條件→②分式條件→'
              '③交集→④結論」四步驟完成以下練習。'))

# ================= 練習A（初階） =================
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(aside_layout(
    main=[para('1．已知 {f(x)=sqrt(x+2)}（根號內是 x+2）。判斷下列 x 值能不能代入 f(x)，並說明理由：')]
        + [para('(1) x=7 能不能代入？為什麼？')] + write_lines(2)
        + [para('(2) x=-2 能不能代入？為什麼？')] + write_lines(2)
        + [para('(3) x=-5 能不能代入？為什麼？')] + write_lines(2),
    aside=[shaded_box('對應手順卡第①步：根號裡面的算式（被開方數）不能是負數，必須 ≥0。等於 0 也可以！')],
    boxed=True,
))

P.append(aside_layout(
    main=[para('2．已知 {g(x)=sqrt(x-3)}。老師已經幫你完成一半，請把空格填滿：')]
        + [para('被開方數是 ＿＿＿，要求 ＿＿＿ ≥ 0，即 x ≥ ＿＿＿，所以定義域是 [ ＿＿＿ , +∞)')]
        + write_lines(2),
    aside=[shaded_box('對應手順卡第①步：被開方數 ≥0，才能開根號。')],
    boxed=True,
))

P.append(aside_layout(
    main=[para('3．在數線上：−3 是實心點，2 是空心圈，中間畫了一條粗線段（−3 到 2 之間都在範圍內）。')]
        + [para('(1) 寫出這個範圍的區間記號：')] + write_lines(2)
        + [para('(2) 用集合寫法 ｛{x}｜...｝ 再寫一次：')] + write_lines(2),
    aside=[shaded_box('提示：實心點●＝這個數可以取到；空心圈○＝這個數取不到。')],
    boxed=True,
))

P.append(aside_layout(
    main=[para('4．判斷下列何者「不能」代入 {f(x)=frac(1,x+4)}：')]
        + [para('(A) x=0　　(B) x=-4　　(C) x=4')] + write_lines(2),
    aside=[shaded_box('對應手順卡第②步：分母不能等於 0，其他情況都可以。')],
    boxed=True,
))

P.append(selfcheck_list([
    '每一題都寫低「能唔能代入」／答案，並且有講出理由',
    '有分清楚「根號要 ≥0」定係「分母要 ≠0」，冇兩條規則搞亂',
    '區間記號嘅實心●／空心○有對應返題目講嘅「取得到／取唔到」',
]))

P.append(checkpoint_rule())

# ================= 練習B（中階） =================
P.append(heading(f'二、練習B（{star_label(2)}）'))
P.append(step_card(
    '求函數定義域　手順卡（精簡版）',
    steps=['①根式 ≥0', '②分式 ≠0', '③兩者取交集', '④寫成區間記號'],
    compact=True,
))

P.append(aside_layout(
    main=[para('5．已知 {f(x)=sqrt(x+4)+frac(1,x-3)}：')]
        + [para('(1) 求 f(x) 的定義域（請寫出①根式條件②分式條件③交集④結論四個步驟）：')]
        + write_lines(5)
        + [para('(2) 求 f(0) 的值：')] + write_lines(2)
        + [para('(3) 求 f(5) 的值：')] + write_lines(2),
    aside=[shaded_box('提示：根式條件 ≥0，分式條件 ≠0，最後把兩個條件的解集取「交集」。')],
    boxed=True,
))

P.append(aside_layout(
    main=[para('6．已知 {h(x)=frac(sqrt(x-2),x-5)}，求 h(x) 的定義域：')]
        + [para('解：')] + write_lines(5),
    aside=[shaded_box('提示：先分別列出分子根式、分母的條件，再取交集；別忘記分母本身也要 ≠0。')],
    boxed=True,
))

P.append(aside_layout(
    main=[para('7．判斷下列各組函數是否為同一函數，並說明理由：')]
        + [para('(1) {f(x)=x} 與 {g(x)=(sqrt(x))^2}：')] + write_lines(2)
        + [para('(2) {f(t)=t} 與 {g(t)=sqrt[3](t^3)}：')] + write_lines(2)
        + [para('(3) {f(x)=x} 與 {g(x)=sqrt(x^2)}：')] + write_lines(2)
        + [para('(4) {f(n)=n} 與 {g(n)=frac(n^2,n)}：')] + write_lines(2),
    aside=[shaded_box('提示：判斷同一函數要「兩項都相同」：①定義域是否相同？②對應關係是否一致？'
                       '化簡前後定義域可能已經改變，要特別小心。')],
    boxed=True,
))

P.append(selfcheck_list([
    '四步驟（根式／分式／交集／結論）有冇跳步，逐步寫低',
    '化簡前同化簡後嘅定義域有冇比較過先落結論',
    '答案有冇寫成區間記號（唔係淨係寫返不等式）',
]))

P.append(checkpoint_rule())

# ================= 練習C（高階） =================
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(para('8．已知函數 k(x) 的定義域是 [-4,-2)∪(-2,5]，請寫出一個可能符合這個定義域的解析式，'
              '並說明理由：'))
P.append(problem_box([para('解：')] + write_lines(4)))

P.append(para('9．請你自己設計一題「求定義域」的題目（要同時包含一個根式與一個分式），'
              '並完整解出你自己出的題目的定義域：'))
P.append(problem_box(
    [para('你的題目：')] + write_lines(2)
    + [para('你的解答：')] + write_lines(5)
))

P.append(para('10．舉出一對「化簡後看起來一樣，但其實不是同一函數」的例子'
              '（不可以跟練習B第7題的例子重複），並說明理由：'))
P.append(problem_box([para('解：')] + write_lines(4), trailing_blank=False))

P.append(selfcheck_list([
    '第8題嘅解析式，三個條件嘅交集是否真係等於指定嘅定義域',
    '第9題嘅自訂題目係咪同時有根式同分式，解答有冇寫齊四步驟',
    '第10題嘅例子有冇同第7題重複、有冇講清楚係邊一項（定義域／對應關係）唔一樣',
]))

# ================= 參考答案與解析 =================
P.append(heading('參考答案與解析', page_break_before=True))

P.append(heading('練習A', sz=BODY_SZ))
P.append(para('1．(1) x=7：x+2=9≥0，可以代入，{f(7)=sqrt(9)=3}。'
              '(2) x=-2：x+2=0，0≥0 仍然成立，可以代入，{f(-2)=sqrt(0)=0}（等於 0 的邊界值是可以取的）。'
              '(3) x=-5：x+2=-3<0，不可以代入（根號內不能是負數）。'))
P.append(para('2．被開方數是 x−3，要求 x−3≥0，即 x≥3，所以定義域是 {[3,+∞)}。'))
P.append(para('3．(1) 區間記號：{[-3,2)}。(2) 集合寫法：｛{x}｜{-3≤x<2}｝。'))
P.append(para('4．答案：(B)。因為 x=-4 會使分母 x+4=0，不能代入；(A)(C) 代入後分母都不為 0，可以代入。'))

P.append(heading('練習B', sz=BODY_SZ))
P.append(para('5．(1) ①根式：x+4≥0 ⇒ x≥-4，即 {[-4,+∞)}；②分式：x-3≠0 ⇒ x≠3；'
              '③交集：{[-4,+∞)} 去掉 x=3，即 {[-4,3)∪(3,+∞)}；④結論：定義域是 {[-4,3)∪(3,+∞)}。'
              '(2) {f(0)=sqrt(4)+frac(1,0-3)=2-frac(1,3)=frac(5,3)}。'
              '(3) {f(5)=sqrt(9)+frac(1,5-3)=3+frac(1,2)=frac(7,2)}。'))
P.append(para('6．分子根式：x-2≥0 ⇒ x≥2；分母：x-5≠0 ⇒ x≠5；交集：{[2,+∞)} 去掉 x=5，'
              '定義域是 {[2,5)∪(5,+∞)}。'))
P.append(para('7．(1) 不是同一函數：{g(x)=(sqrt(x))^2} 必須先算 {sqrt(x)}，要求 x≥0，'
              '所以 g 的定義域是 {[0,+∞)}，跟 f 的定義域 R 不同（陷阱：化簡後兩式看似都等於 x，'
              '但前面的根號已經限制了定義域）。'))
P.append(para('(2) 是同一函數：{g(t)=sqrt[3](t^3)} 對任何實數 t 都有意義（三次方根沒有正負限制），'
              '定義域都是 R，而且對所有 t，{sqrt[3](t^3)=t}，對應關係也一致。'))
P.append(para('(3) 不是同一函數：{g(x)=sqrt(x^2)=|x|}，雖然定義域都是 R（跟 f 相同），'
              '但當 x<0 時 g(x)=-x≠f(x)=x，對應關係不一致（陷阱：定義域相同不代表就是同一函數，'
              '還要檢查對應關係）。'))
P.append(para('(4) 不是同一函數：{g(n)=frac(n^2,n)} 要求 n≠0，定義域是 {(-∞,0)∪(0,+∞)}，'
              '跟 f 的定義域 R 不同。'))

P.append(heading('練習C', sz=BODY_SZ))
P.append(para('8．參考答案：{k(x)=sqrt(x+4)+frac(1,x+2)+sqrt(5-x)}。'
              '理由：{sqrt(x+4)} 要求 x≥-4；{frac(1,x+2)} 要求 x≠-2；{sqrt(5-x)} 要求 x≤5；'
              '三個條件的交集正好是 [-4,-2)∪(-2,5]（本題答案不唯一，只要三個條件的交集'
              '確實等於指定的定義域即可）。'))
P.append(para('9．本題無固定答案。教師驗收標準：學生自訂的題目要同時出現根式與分式；'
              '解答要完整寫出①根式條件②分式條件③交集④結論四個步驟，且交集結果要與自己列出的'
              '兩個條件一致。'))
P.append(para('10．參考答案：{f(x)=x-3} 與 {g(x)=frac(x^2-6x+9,x-3)}——分子 {x^2-6x+9} 是完全平方 '
              '{(x-3)^2}，約分後 g(x)=x-3，兩式化簡後看起來一樣，但 g(x) 要求分母 x-3≠0，即 x≠3，'
              '定義域是 {(-∞,3)∪(3,+∞)}，跟 f 的定義域 R 不同，所以不是同一函數'
              '（本題答案不唯一，只要清楚指出定義域或對應關係的差異、且不與第7題(1)-(4)重複即可）。'))

out = build_docx(P, os.path.join(OUT_DIR, '練習_函數的概念與定義域_高一數學.docx'),
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
