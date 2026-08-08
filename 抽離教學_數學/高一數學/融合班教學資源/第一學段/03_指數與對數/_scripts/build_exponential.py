#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

# ===== 講義 =====
lecture_para = []
lecture_para.append(masthead('高一數學', '4.2 指數函數', '課堂講義'))
lecture_para.append(student_info_row())

lecture_para.append(heading('一、指數函數的定義'))
lecture_para.append(para('指數函數是形如 {y = a^x} 的函數，其中底數 {a > 0} 且 {a ≠ 1}。'))
lecture_para.append(para('我們已經學過指數運算（例如 {2^3 = 8}），現在要研究當 {x} 是任意實數時，{a^x} 如何變化。'))

lecture_para.append(heading('二、指數函數的性質'))
lecture_para.append(para('1. 定義域：所有實數 {mathbb(R)}'))
lecture_para.append(para('2. 值域：所有正實數 {(0, +∞)}（注意：{a^x > 0} 對所有 {x} 恆成立）'))
lecture_para.append(para('3. 必過定點：所有指數函數圖像都過點 {(0, 1)}（因為 {a^0 = 1}）'))
lecture_para.append(para('4. 單調性：'))
lecture_para.append(para('   • 當 {a > 1} 時，{y = a^x} 單調遞增（{x} 越大，函數值越大）'))
lecture_para.append(para('   • 當 {0 < a < 1} 時，{y = a^x} 單調遞減（{x} 越大，函數值越小）'))

lecture_para.append(heading('三、已完成範例'))
lecture_para.append(shaded_box('例題：計算 {2^5 · 2^{-1}}'))
lecture_para.append(para('步驟1：依指數運算法則，同底相乘時指數相加'))
lecture_para.append(para('      {2^5 · 2^{-1} = 2^{5+(-1)} = 2^4}'))
lecture_para.append(para('步驟2：計算 {2^4 = 16}'))
lecture_para.append(para('答案：{16}'))

lecture_para.append(para('接下來請拿《課堂練習——指數函數》，依照上面四個性質和這個範例的步驟框架，完成練習A、B、C。'))

# 儲存講義
out_lecture = build_docx(lecture_para, r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\講義_4.2指數函數_融合版.docx', footer_text='高一數學．指數函數')
print(f"講義已產出：{out_lecture}")

# ===== 練習 =====
practice_para = []
practice_para.append(masthead('高一數學', '4.2 指數函數', '課堂練習'))
practice_para.append(student_info_row())

practice_para.append(para('回顧講義的四個性質和範例步驟，完成下面的練習。'))

# 練習A
practice_para.append(heading(f'練習A {star_label(1)}'))

practice_para.append(problem_box([
    para('1. 計算 {3^2 · 3^1}'),
    para('   步驟1：同底相乘，指數相加'),
    para('          {3^2 · 3^1 = 3^{□} = 3^□}'),
    para('   步驟2：計算 {3^□ = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：指數相加 {m + n}；{3^3 = 27}'))

practice_para.append(problem_box([
    para('2. 計算 {5^0 + 2^3}'),
    para('   步驟1：分別計算 {5^0} 和 {2^3}'),
    para('          {5^0 = □}，{2^3 = □}'),
    para('   步驟2：相加得 {□ + □ = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：任何非零數的0次方等於1'))

# 練習B
practice_para.append(heading(f'練習B {star_label(2)}'))

practice_para.append(problem_box([
    para('3. 計算 {(2^3)^2 ÷ 2^2}'),
    para('   步驟1：由冪的冪法則，{(2^3)^2 = 2^{3×2} = 2^□}'),
    para('   步驟2：同底相除，指數相減：{2^□ ÷ 2^2 = 2^{□-2}}'),
    para('   步驟3：{2^□ = □}'),
] + write_lines(3)))

practice_para.append(shaded_box('提示：{(a^m)^n = a^{m·n}}；{a^m ÷ a^n = a^{m-n}}'))

practice_para.append(problem_box([
    para('4. 比較大小：{2^{0.5}} _______ {2^{0.3}}（填>、<或=）'),
    para('   步驟1：函數 {y = 2^x} 的底數 {a = 2 > 1}，所以函數單調_______'),
    para('   步驟2：因為 {0.5 > 0.3}，且函數遞_______'),
    para('   步驟3：所以 {2^{0.5}} _______ {2^{0.3}}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：利用指數函數的單調性比較大小'))

practice_para.append(problem_box([
    para('5. 解方程 {3^x = 9}'),
    para('   步驟1：觀察 {9 = 3^□}'),
    para('   步驟2：因此 {3^x = 3^□}'),
    para('   步驟3：所以 {x = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：化成同底，然後比較指數'))

# 練習C
practice_para.append(heading(f'練習C {star_label(3)}'))

practice_para.append(problem_box([
    para('6. 已知 {y = a^x} 過點 {(1, 2)}，求 {a} 的值，並判斷函數單調性。'),
    para('   步驟1：因為點 {(1, 2)} 在函數上，代入得 {a^1 = □}'),
    para('   步驟2：所以 {a = □}'),
    para('   步驟3：判斷單調性：因為 {a = □ > 1}，所以函數單調_______'),
    para('   答案：{a = □}；函數單調_______'),
] + write_lines(3)))

practice_para.append(shaded_box('提示：當 {a > 1} 時遞增；當 {0 < a < 1} 時遞減'))

practice_para.append(problem_box([
    para('7. 若 {2^{x-1} = 1/4}，求 {x}'),
    para('   步驟1：化簡 {1/4 = 2^{□}}'),
    para('   步驟2：因此 {2^{x-1} = 2^{□}}'),
    para('   步驟3：比較指數得 {x - 1 = □}'),
    para('   步驟4：解得 {x = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：{1/4 = 2^{-2}}；{(1/a)^n = a^{-n}}'))

# 參考答案
practice_para.append(pagebreak())
practice_para.append(heading('參考答案', page_break_before=False))

practice_para.append(para('練習A'))
practice_para.append(para('1. {3^3 = 27}'))
practice_para.append(para('2. {1 + 8 = 9}'))

practice_para.append(para('練習B'))
practice_para.append(para('3. {2^6 ÷ 2^2 = 2^4 = 16}'))
practice_para.append(para('4. {2^{0.5} > 2^{0.3}}（因為 {y=2^x} 單調遞增，{0.5 > 0.3}）'))
practice_para.append(para('5. {x = 2}（{9 = 3^2}）'))

practice_para.append(para('練習C'))
practice_para.append(para('6. {a = 2}；函數單調遞增'))
practice_para.append(para('7. {x = -1}（{1/4 = 2^{-2}}，所以 {x-1 = -2}，{x = -1}）'))

# 儲存練習
out_practice = build_docx(practice_para, r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\練習_4.2指數函數_融合版.docx', footer_text='高一數學．指數函數')
print(f"練習已產出：{out_practice}")

print("✓ 指數函數講義和練習 docx 已產出")
