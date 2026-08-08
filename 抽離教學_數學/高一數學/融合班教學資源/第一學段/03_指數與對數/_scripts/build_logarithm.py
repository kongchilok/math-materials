#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

# ===== 講義 =====
lecture_para = []
lecture_para.append(masthead('高一數學', '4.4 對數函數', '課堂講義'))
lecture_para.append(student_info_row())

lecture_para.append(heading('一、對數的定義'))
lecture_para.append(para('對數是一個反向思考的工具。'))
lecture_para.append(para('問題：「2的多少次方等於8？」'))
lecture_para.append(para('答案用對數表示：{log_2 8 = 3}（因為 {2^3 = 8}）'))
lecture_para.append(para('一般地，如果 {a^x = N}（其中 {a > 0, a ≠ 1, N > 0}），'))
lecture_para.append(para('那麼 {x = log_a N}（讀作「以 {a} 為底 {N} 的對數」）'))

lecture_para.append(heading('二、對數函數的定義'))
lecture_para.append(para('對數函數是形如 {y = log_a x} 的函數，其中 {a > 0} 且 {a ≠ 1}。'))
lecture_para.append(para('特別地，對數函數 {y = log_a x} 是指數函數 {y = a^x} 的反函數。'))

lecture_para.append(heading('三、對數函數的性質'))
lecture_para.append(para('1. 定義域：{(0, +∞)}（注意：{x} 必須大於0）'))
lecture_para.append(para('2. 值域：所有實數 {mathbb(R)}'))
lecture_para.append(para('3. 必過定點：所有對數函數圖像都過點 {(1, 0)}（因為 {log_a 1 = 0}）'))
lecture_para.append(para('4. 單調性：'))
lecture_para.append(para('   • 當 {a > 1} 時，{y = log_a x} 單調遞增'))
lecture_para.append(para('   • 當 {0 < a < 1} 時，{y = log_a x} 單調遞減'))
lecture_para.append(para('5. 與指數函數的對稱性：{y = log_a x} 與 {y = a^x} 的圖像關於 {y = x} 對稱'))

lecture_para.append(heading('四、對數運算法則'))
lecture_para.append(para('若 {M > 0, N > 0, a > 0, a ≠ 1}，則：'))
lecture_para.append(para('• {log_a(M·N) = log_a M + log_a N}（乘積變和）'))
lecture_para.append(para('• {log_a frac(M, N) = log_a M - log_a N}（商變差）'))
lecture_para.append(para('• {log_a M^n = n · log_a M}（冪變係數）'))

lecture_para.append(heading('五、已完成範例'))
lecture_para.append(shaded_box('例題：計算 {log_2 8}'))
lecture_para.append(para('步驟1：問題轉化：{log_2 8 = ?} 意思是「2的多少次方等於8？」'))
lecture_para.append(para('步驟2：列方程：{2^x = 8}'))
lecture_para.append(para('步驟3：求解：{2^x = 2^3}，所以 {x = 3}'))
lecture_para.append(para('步驟4：答案：{log_2 8 = 3}'))

lecture_para.append(para('接下來請拿《課堂練習——對數函數》，依照上面的運算法則和這個範例的步驟框架，完成練習A、B、C。'))

# 儲存講義
out_lecture = build_docx(lecture_para, r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\講義_4.4對數函數_融合版.docx', footer_text='高一數學．對數函數')
print(f"講義已產出：{out_lecture}")

# ===== 練習 =====
practice_para = []
practice_para.append(masthead('高一數學', '4.4 對數函數', '課堂練習'))
practice_para.append(student_info_row())

practice_para.append(para('回顧講義的性質、運算法則和步驟，完成下面的練習。'))

# 練習A
practice_para.append(heading(f'練習A {star_label(1)}'))

practice_para.append(problem_box([
    para('1. 計算 {log_3 9}'),
    para('   問題轉化：3的多少次方等於9？'),
    para('   列方程：{3^x = 9}'),
    para('   求解：{3^x = 3^□}，所以 {x = □}'),
    para('   答案：{log_3 9 = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：想一想 {3^1 = 3, 3^2 = 9, 3^3 = 27}'))

practice_para.append(problem_box([
    para('2. 計算 {log_5 1}'),
    para('   問題轉化：5的多少次方等於1？'),
    para('   根據指數性質，任何非零數的0次方都等於1，即 {a^0 = 1}'),
    para('   所以 {log_5 1 = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：{a^0 = 1} 對所有 {a > 0, a ≠ 1} 成立'))

# 練習B
practice_para.append(heading(f'練習B {star_label(2)}'))

practice_para.append(problem_box([
    para('3. 計算 {log_2 4 + log_2 8}'),
    para('   方法1（分別計算）：{log_2 4 = □}（{2^□ = 4}）'),
    para('                     {log_2 8 = □}（{2^□ = 8}）'),
    para('                     相加得 {□ + □ = □}'),
    para('   方法2（用運算法則）：{log_2 4 + log_2 8 = log_2(4 × 8) = log_2 □ = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：{log_a(M·N) = log_a M + log_a N}'))

practice_para.append(problem_box([
    para('4. 解方程 {log_2(x - 1) = 3}'),
    para('   步驟1：對數方程轉化為指數方程：{x - 1 = 2^3}'),
    para('   步驟2：計算 {2^3 = □}'),
    para('   步驟3：解得 {x = □ + 1 = □}'),
    para('   驗證：{log_2(□ - 1) = log_2 □ = □} ✓'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：若 {log_a x = b}，則 {x = a^b}（互化關係）'))

practice_para.append(problem_box([
    para('5. 計算 {log_3 27 - log_3 9}'),
    para('   方法1（分別計算）：{log_3 27 = □}，{log_3 9 = □}'),
    para('                     相減得 {□ - □ = □}'),
    para('   方法2（用運算法則）：{log_3 27 - log_3 9 = log_3 frac(27, 9) = log_3 □ = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：{log_a frac(M, N) = log_a M - log_a N}'))

# 練習C
practice_para.append(heading(f'練習C {star_label(3)}'))

practice_para.append(problem_box([
    para('6. 若 {log_a 4 = 2}，求 {a} 的值'),
    para('   步驟1：對數方程轉為指數方程：{a^2 = 4}'),
    para('   步驟2：求解：{a = □}（注意 {a > 0, a ≠ 1}）'),
    para('   驗證：{log_□ 4 = 2}？因為 {□^2 = 4} ✓'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：若 {log_a x = b}，則 {a^b = x}'))

practice_para.append(problem_box([
    para('7. 計算 {log_2 16 + log_3 9 - log_5 25}'),
    para('   第一項：{log_2 16 = □}（{2^□ = 16}）'),
    para('   第二項：{log_3 9 = □}（{3^□ = 9}）'),
    para('   第三項：{log_5 25 = □}（{5^□ = 25}）'),
    para('   合計：{□ + □ - □ = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：逐項計算後再相加減'))

# 參考答案
practice_para.append(pagebreak())
practice_para.append(heading('參考答案', page_break_before=False))

practice_para.append(para('練習A'))
practice_para.append(para('1. {log_3 9 = 2}（{3^2 = 9}）'))
practice_para.append(para('2. {log_5 1 = 0}（{5^0 = 1}）'))

practice_para.append(para('練習B'))
practice_para.append(para('3. 方法1：{2 + 3 = 5}；方法2：{log_2 32 = 5}'))
practice_para.append(para('4. {x - 1 = 8}，{x = 9}'))
practice_para.append(para('5. 方法1：{3 - 2 = 1}；方法2：{log_3 3 = 1}'))

practice_para.append(para('練習C'))
practice_para.append(para('6. {a = 2}（{2^2 = 4}）'))
practice_para.append(para('7. {4 + 2 - 2 = 4}'))

# 儲存練習
out_practice = build_docx(practice_para, r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\練習_4.4對數函數_融合版.docx', footer_text='高一數學．對數函數')
print(f"練習已產出：{out_practice}")

print("✓ 對數函數講義和練習 docx 已產出")
