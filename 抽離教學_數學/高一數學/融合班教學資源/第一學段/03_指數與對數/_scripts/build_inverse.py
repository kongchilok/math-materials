#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

# ===== 講義 =====
lecture_para = []
lecture_para.append(masthead('高一數學', '4.3 反函數', '課堂講義'))
lecture_para.append(student_info_row())

lecture_para.append(heading('一、反函數的概念'))
lecture_para.append(para('如果函數 {f} 和函數 {g} 互為反函數，那麼它們有特殊關係：'))
lecture_para.append(para('• {f(g(x)) = x}（用 {g} 的輸出去用 {f}，回到原本的 {x}）'))
lecture_para.append(para('• {g(f(x)) = x}（用 {f} 的輸出去用 {g}，也回到原本的 {x}）'))
lecture_para.append(para('簡單說：反函數「撤銷」了原函數的作用。'))

lecture_para.append(heading('二、反函數的性質'))
lecture_para.append(para('1. 定義域和值域互換：'))
lecture_para.append(para('   • 反函數的定義域 = 原函數的值域'))
lecture_para.append(para('   • 反函數的值域 = 原函數的定義域'))
lecture_para.append(para('2. 圖像對稱：反函數的圖像與原函數的圖像關於直線 {y = x} 對稱'))
lecture_para.append(para('3. 坐標互換：若點 {(a, b)} 在原函數上，則點 {(b, a)} 在反函數上'))

lecture_para.append(heading('三、求反函數的步驟'))
lecture_para.append(para('對函數 {y = f(x)}，求其反函數 {y = f^{-1}(x)} 的方法：'))
lecture_para.append(para('步驟1：令 {y = f(x)}'))
lecture_para.append(para('步驟2：對調 {x} 和 {y}：{x = f(y)}'))
lecture_para.append(para('步驟3：用 {y} 表示 {x}（解出 {y}）'))
lecture_para.append(para('步驟4：寫成 {y = f^{-1}(x)}'))

lecture_para.append(heading('四、已完成範例'))
lecture_para.append(shaded_box('例題：已知 {f(x) = 2x + 1}，求其反函數 {f^{-1}(x)}'))
lecture_para.append(para('步驟1：令 {y = 2x + 1}'))
lecture_para.append(para('步驟2：對調 {x, y}：{x = 2y + 1}'))
lecture_para.append(para('步驟3：用 {y} 表示：{2y = x - 1}，{y = frac(x-1, 2)}'))
lecture_para.append(para('步驟4：反函數為 {f^{-1}(x) = frac(x-1, 2)}'))
lecture_para.append(para('驗證：{f(f^{-1}(x)) = f(frac(x-1, 2)) = 2 · frac(x-1, 2) + 1 = x - 1 + 1 = x} ✓'))

lecture_para.append(para('接下來請拿《課堂練習——反函數》，依照上面四個性質和這個範例的步驟框架，完成練習A、B、C。'))

# 儲存講義
out_lecture = build_docx(lecture_para, r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\講義_4.3反函數_融合版.docx', footer_text='高一數學．反函數')
print(f"講義已產出：{out_lecture}")

# ===== 練習 =====
practice_para = []
practice_para.append(masthead('高一數學', '4.3 反函數', '課堂練習'))
practice_para.append(student_info_row())

practice_para.append(para('回顧講義的性質和步驟，完成下面的練習。'))

# 練習A
practice_para.append(heading(f'練習A {star_label(1)}'))

practice_para.append(problem_box([
    para('1. 已知 {f(1) = 3}，求 {f^{-1}(3)} 的值'),
    para('   若原函數在 {x=1} 時輸出 3，那麼反函數在輸入 3 時應輸出 □'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：反函數撤銷原函數的作用；若 {f(1)=3}，則 {f^{-1}(3)=1}'))

practice_para.append(problem_box([
    para('2. 點 {(2, 5)} 在 {f(x)} 上'),
    para('   那麼點 {(5, 2)} 在 {f^{-1}(x)} 上嗎？ □（是/否）'),
    para('   理由：反函數圖像與原函數圖像對稱'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：原函數上的點 {(a,b)} 對應反函數上的點 {(b,a)}'))

# 練習B
practice_para.append(heading(f'練習B {star_label(2)}'))

practice_para.append(problem_box([
    para('3. 求 {f(x) = 3x - 2} 的反函數 {f^{-1}(x)}'),
    para('   步驟1：令 {y = 3x - 2}'),
    para('   步驟2：對調 {x, y}：{x = 3y - 2}'),
    para('   步驟3：解出 {y}：{3y = x + □}，{y = frac(□, □)}'),
    para('   步驟4：{f^{-1}(x) = frac(□, □)}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：逐步列算式，用方框表示要填的空白'))

practice_para.append(problem_box([
    para('4. 已知 {f(x) = frac(x, 2)}，求 {f^{-1}(4)} 的值'),
    para('   先求反函數：令 {y = frac(x, 2)}，對調得 {x = frac(y, 2)}'),
    para('                解得 {y = □}'),
    para('   所以 {f^{-1}(x) = □}'),
    para('   代入 {x = 4}：{f^{-1}(4) = □}'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：{frac(x, 2) = x ÷ 2}，反函數應是乘以2'))

# 練習C
practice_para.append(heading(f'練習C {star_label(3)}'))

practice_para.append(problem_box([
    para('5. 已知 {f(x) = x^3}，求其反函數 {f^{-1}(x)} 的值域'),
    para('   步驟1：原函數 {f(x) = x^3} 的定義域是 _______，值域是 _______'),
    para('   步驟2：反函數的定義域 = 原函數的值域 = _______'),
    para('   步驟3：反函數的值域 = 原函數的定義域 = _______'),
    para('   答案：反函數的值域是 _______'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：定義域和值域的互換關係'))

practice_para.append(problem_box([
    para('6. 若函數 {y = 2^x} 與 {y = log_2 x} 互為反函數，且 {y = 2^x} 過點 {(1, 2)}'),
    para('   確認 {a} 的值：{a^1 = 2}，所以 {a = □}'),
    para('   寫出反函數：{y = □}'),
    para('   對應關係：{y = 2^x} 的定義域 {mathbb(R)} = {y = log_2 x} 的值域'),
] + write_lines(2)))

practice_para.append(shaded_box('提示：指數函數與對數函數互為反函數；定義域值域互換'))

# 參考答案
practice_para.append(pagebreak())
practice_para.append(heading('參考答案', page_break_before=False))

practice_para.append(para('練習A'))
practice_para.append(para('1. {f^{-1}(3) = 1}'))
practice_para.append(para('2. 是；理由：關於 {y=x} 對稱'))

practice_para.append(para('練習B'))
practice_para.append(para('3. {f^{-1}(x) = frac(x+2, 3)}'))
practice_para.append(para('4. {f^{-1}(x) = 2x}；{f^{-1}(4) = 8}'))

practice_para.append(para('練習C'))
practice_para.append(para('5. 定義域 {mathbb(R)}，值域 {mathbb(R)}；反函數值域 {mathbb(R)}'))
practice_para.append(para('6. {a = 2}；反函數 {y = log_2 x}；{y = 2^x} 的定義域 {mathbb(R)} = {y = log_2 x} 的值域'))

# 儲存練習
out_practice = build_docx(practice_para, r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\練習_4.3反函數_融合版.docx', footer_text='高一數學．反函數')
print(f"練習已產出：{out_practice}")

print("✓ 反函數講義和練習 docx 已產出")
