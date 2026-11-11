# -*- coding: utf-8 -*-
"""verify_ch4.py — 用 sympy 逐題重算第四章六份講義練習的答案，並寫出《驗算_第四章_整式的加減.md》。
每一項＝(課, 題號, 說明, 重算值, 講義答案)；兩者不等就 FAIL 並以非零碼結束。"""
import io
import os
import sys
from sympy import symbols, Rational as R, pi, expand, simplify, Poly, degree, sympify

a, b, c, m, n, p, q, t, x, y, z, k, r = symbols('a b c m n p q t x y z k r')
ROWS = []
BAD = 0


def chk(lesson, no, desc, got, want):
    global BAD
    ok = simplify(sympify(got) - sympify(want)) == 0
    BAD += (not ok)
    ROWS.append((lesson, no, desc, str(got), str(want), 'PASS' if ok else 'FAIL'))


def note(lesson, no, desc, text):
    ROWS.append((lesson, no, desc, text, '—', '人工核對'))


def tdeg(e):
    """單項式／多項式的次數（所有字母合計的最高次）。π 當作數。"""
    e = expand(e)
    syms = sorted(e.free_symbols, key=str)
    return Poly(e, *syms).total_degree() if syms else 0


# ---------------- 第 1 課　單項式
L = '1 單項式'
chk(L, '範例', '−4a²b³c 的次數', tdeg(-4*a**2*b**3*c), 6)
chk(L, '範例', '−¾x²y 的次數', tdeg(-R(3, 4)*x**2*y), 3)
chk(L, '我們做', '⅖x³y 的次數', tdeg(R(2, 5)*x**3*y), 4)
for e, d in ((6*a**2, 2), (-x*y, 2), (R(1, 2)*m**3*n, 4)):
    chk(L, 2, f'{e} 的次數', tdeg(e), d)
chk(L, 2, '−7 的次數', tdeg(sympify(-7)), 0)
chk(L, 3, '長 a 寬 b 面積 ab 的次數', tdeg(a*b), 2)
for e, co, d in ((-5*x**2*y, -5, 3), (R(2, 3)*a*b**3, R(2, 3), 4), (-t, -1, 1), (pi*r**2, pi, 2), (2**3*x**2, 8, 2)):
    syms = sorted(e.free_symbols, key=str)
    chk(L, 4, f'{e} 的係數', Poly(e, *syms).LC(), co)
    chk(L, 4, f'{e} 的次數', tdeg(e), d)
note(L, 1, '單項式判斷', '3x、−5、mn²、t 是；a+2 有加號、2/y 分母有字母，不是')
note(L, 5, '判斷', '(1) −x²y 係數 −1 → 錯；(2) −6 次數 0 → 對；(3) 3/x 非單項式 → 錯；(4) 2πr 係數 2π → 錯')
chk(L, 6, '例 −3x²y² 次數', tdeg(-3*x**2*y**2), 4)
chk(L, 6, '例 −3ab³ 次數', tdeg(-3*a*b**3), 4)
chk(L, 7, 'm+2=5 → m', 5 - 2, 3)
chk(L, 8, '4x²y⁴ 次數 6，a+3=6 → a', tdeg(4*x**2*y**4) - 3, 3)
note(L, 9, '開放題', '12m：每盒 12 隻、m 盒；情境合理即可')

# ---------------- 第 2 課　多項式
L = '2 多項式與整式'
chk(L, '範例', '−2a²b+3ab−5 的次數', tdeg(-2*a**2*b + 3*a*b - 5), 3)
chk(L, '範例', '降冪排列前後相等', 5*x - 3*x**3 + 2 + x**2, -3*x**3 + x**2 + 5*x + 2)
chk(L, '我們做', 'x³−4x²y²+y−1 的次數', tdeg(x**3 - 4*x**2*y**2 + y - 1), 4)
for e, d in ((3*x - 7, 1), (a**2 - 2*a*b + b**2, 2), (-x**3 + 4*x - 1, 3)):
    chk(L, 2, f'{e} 的次數', tdeg(e), d)
note(L, 1, '分類', '單項式：4r²、3、−t；多項式：2a+1、x²−5y+1、m³−n')
chk(L, 3, '周長', 2*(a + b), 2*a + 2*b)
for e, d in ((-5*a**2*b + 2*a*b - b**4, 4), (R(1, 2)*t**2 - 2*t + 3, 2), (x**3 - 2*y + x**2, 3), (x*y**2 - 1, 3)):
    chk(L, 4, f'{e} 的次數', tdeg(e), d)
chk(L, 5, '(1)', 4 - x**2 + 3*x, -x**2 + 3*x + 4)
chk(L, 5, '(2)', 2*y - 5*y**3 + y**2 - 1, -5*y**3 + y**2 + 2*y - 1)
chk(L, 5, '(3)', 4*x**2*y - 2*x*y**2 - x**3 + y**3, -x**3 + 4*x**2*y - 2*x*y**2 + y**3)
chk(L, 6, '(2) a³b−4ab−6 的次數', tdeg(a**3*b - 4*a*b - 6), 4)
chk(L, 6, '(3) m³+m+5 一次項係數', Poly(m**3 + m + 5, m).coeff_monomial(m), 1)
chk(L, 7, 'n=4 時為四次', tdeg(x**4 + 4*x - 7), 4)
chk(L, 8, 'm=3 時為四次', tdeg(3*x**3*y - 2*x + 1), 4)
chk(L, 9, '例 −x²+2x+3 二次項係數', Poly(-x**2 + 2*x + 3, x).LC(), -1)

# ---------------- 第 3 課　合併同類項
L = '3 合併同類項'
chk(L, '重溫', '7×3+5×3', 7*3 + 5*3, 36)
chk(L, '範例一', '', 3*x**2 + 5*x - 4 - x**2 + 2*x + 9, 2*x**2 + 7*x + 5)
chk(L, '範例二', '', 5*a*b - 2*a**2 + 3*b**2 - a*b + 2*a**2, 4*a*b + 3*b**2)
chk(L, '我們做', '', 2*a + 5*b - 6*a + b, -4*a + 6*b)
note(L, 1, '同類項判斷', '是／不是（指數不同）／是／是／不是（字母不同）')
chk(L, 2, '(1)', 5*x + 4*x, 9*x)
chk(L, 2, '(2)', -7*a*b + 6*a*b, -a*b)
chk(L, 2, '(3)', 10*y**2 - R(1, 2)*y**2, R(19, 2)*y**2)
chk(L, 2, '(4)', m - 3*m, -2*m)
chk(L, 3, '', 6*a + 3*b - 2*a + 5*b - 1, 4*a + 8*b - 1)
chk(L, 4, '(1)', 4*x - x - 6*x, -3*x)
chk(L, 4, '(2)', -a + R(2, 5)*a - R(12, 5)*a, -3*a)
chk(L, 4, '(3)', p - q**2 - 5*p + 3*q**2, -4*p + 2*q**2)
chk(L, 4, '(4)', R(1, 2)*y - R(3, 2)*y + 3*y, 2*y)
chk(L, 4, '(5)', -4*x**2*y + 5*x*y**2 + x**2*y - 2*x*y**2, -3*x**2*y + 3*x*y**2)
chk(L, 5, '(1) 5y²−2y²', 5*y**2 - 2*y**2, 3*y**2)
chk(L, 5, '(2) x²+x²', x**2 + x**2, 2*x**2)
chk(L, 5, '(3) 4ab−4ba', 4*a*b - 4*b*a, 0)
chk(L, 6, '化簡', 4*x - 3*y - x + 5*y, 3*x + 2*y)
chk(L, 6, '求值', (4*x - 3*y - x + 5*y).subs({x: 2, y: -1}), 4)
chk(L, 7, '合併', 3*x**3*y**2 - 5*x**3*y**2, -2*x**3*y**2)
chk(L, 8, 'k=3 時一次項係數', Poly((2*x**2 + k*x - 3*x + 1).subs(k, 3), x).coeff_monomial(x), 0)
chk(L, 9, '例', 5*a - 3*a + 1 - 4, 2*a - 3)

# ---------------- 第 4 課　去括號
L = '4 去括號'
chk(L, '重溫', '3×(10+2)', 3*(10 + 2), 36)
chk(L, '範例一', '', 6*x + 3*y + (2*x - 5*y), 8*x - 2*y)
chk(L, '範例二', '', (3*y - 2) - 2*(4 - y), 5*y - 10)
chk(L, '對比', 'a−(b−c)', a - (b - c), a - b + c)
chk(L, '我們做', '(1)', 5*a - (2*a - 3*b), 3*a + 3*b)
chk(L, '我們做', '(2)', -3*(x - 4), -3*x + 12)
chk(L, 1, '(1)', x + (y - 2), x + y - 2)
chk(L, 1, '(2)', x - (y - 2), x - y + 2)
chk(L, 1, '(3)', m - (-n + 3), m + n - 3)
chk(L, 1, '(4)', -(p + q), -p - q)
chk(L, 2, '(1)', 2*(3*x - 5), 6*x - 10)
chk(L, 2, '(2)', -3*(a + 4), -3*a - 12)
chk(L, 2, '(3)', -4*(2 - y), -8 + 4*y)
chk(L, 2, '(4)', R(1, 2)*(6*m - 8), 3*m - 4)
chk(L, 3, '正確結果', 7*a - (3*a - 2), 4*a + 2)
chk(L, 4, '(1)', 5*x - (2*x - 1), 3*x + 1)
chk(L, 4, '(2)', (4*a - b) + (a + 3*b), 5*a + 2*b)
chk(L, 4, '(3)', 4*(2*x - R(1, 4)), 8*x - 1)
chk(L, 4, '(4)', -2*a + (4*a - 3) - (5*a - 1), -3*a - 2)
chk(L, 4, '(5)', R(1, 2)*(4*y - 6) + 3*(y + 2), 5*y + 3)
chk(L, 5, '(1)', x**2 - (3*x - y + 1), x**2 - 3*x + y - 1)
chk(L, 5, '(2)', 3*(x - 2), 3*x - 6)
chk(L, 5, '(3)', -(m - n) + (m*n - 1), -m + n + m*n - 1)
chk(L, 5, '(4) 原式正確', 2*(a + b) - (a - b), a + 3*b)
chk(L, 6, '周長', 2*(2*a + 3) + 2*(a - 1), 6*a + 4)
chk(L, 7, '', 4*a - (3*a - 2*(a - 1)), 3*a - 2)
chk(L, 8, '(1)', a - (b - c), a - b + c)
chk(L, 8, '(2)', x**2 - (2*x - 1), x**2 - 2*x + 1)
chk(L, 8, '(3)', m + (n - p), m + n - p)
chk(L, 9, '例', 5 - (x - 2), 7 - x)

# ---------------- 第 5 課　整式的加減
L = '5 整式的加減'
chk(L, '概念框／對比', '(2a+b)−(a−3b)', (2*a + b) - (a - 3*b), a + 4*b)
chk(L, '範例一', '', (4*a - 3*b) - (a - 5*b), 3*a + 2*b)
e = 2*(x**2 - 3*x) - (x**2 - 5*x + 1)
chk(L, '範例二', '化簡', e, x**2 - x - 1)
chk(L, '範例二', '求值 x=−2', e.subs(x, -2), 5)
chk(L, '我們做', '', (5*m + 2*n) - (3*m - n), 2*m + 3*n)
chk(L, 1, '(1)', (3*x + 2*y) + (x - 5*y), 4*x - 3*y)
chk(L, 1, '(2)', (6*a - b) - (2*a + 3*b), 4*a - 4*b)
chk(L, 1, '(3)', (x**2 + 3*x) - (x**2 - 2), 3*x + 2)
chk(L, 2, '', (3*x - y) - (x + 2*y), 2*x - 3*y)
e = 2*(a + b) - (a - b)
chk(L, 3, '化簡', e, a + 3*b)
chk(L, 3, '求值', e.subs({a: 4, b: -1}), 1)
chk(L, 4, '(1)', (3*x - 2*y + z) + (y - 4*x - 5*z), -x - y - 4*z)
chk(L, 4, '(2)', (5*a*b - a**2 + 2*b**2) - (2*a**2 - b**2 + 5*a*b), -3*a**2 + 3*b**2)
chk(L, 4, '(3)', 2*(3*a**2 - b) - 3*(a**2 - 2*b), 3*a**2 + 4*b)
chk(L, 4, '(4)', (x**2 - 2 + 3*x) - 2*(x - x**2 + R(1, 2)), 3*x**2 + x - 3)
e = 3*(x**2*y - 2*x*y) - 2*(x**2*y - 3*x*y) - 5
chk(L, 5, '化簡', e, x**2*y - 5)
chk(L, 5, '求值', e.subs({x: -2, y: 3}), 7)
chk(L, 6, '', (5*x + 1) - (2*x - 3), 3*x + 4)
chk(L, 7, '(1)', (4*a + 3*b) + (2*a + 5*b), 6*a + 8*b)
chk(L, 7, '(2)', (4*a + 3*b) - (2*a + 5*b), 2*a - 2*b)
chk(L, 8, '', (2*x**2 + 3*x - 1) - (2*x**2 - 5 + 3*x), 4)
chk(L, 9, '(1) 恆等：兩式相加', (x**2 + x*y) + (y**2 - x*y), x**2 + y**2)
chk(L, 9, '(1) 值', 5 + 2, 7)
chk(L, 9, '(2) 恆等：兩式相減', (x**2 + x*y) - (y**2 - x*y), x**2 + 2*x*y - y**2)
chk(L, 9, '(2) 值', 5 - 2, 3)

# ---------------- 第 6 課　章末複習
L = '6 章末複習'
chk(L, '重溫表', '2x²y−x²y', 2*x**2*y - x**2*y, x**2*y)
chk(L, '易錯表', '3(x−2)', 3*(x - 2), 3*x - 6)
chk(L, 1, 'B：x²y 次數', tdeg(x**2*y), 3)
chk(L, 2, '3x²y−5xy−2 次數', tdeg(3*x**2*y - 5*x*y - 2), 3)
chk(L, 3, '(1)', -5*x*y + 8*x*y, 3*x*y)
chk(L, 3, '(2)', -3*(2*a - b), -6*a + 3*b)
chk(L, 4, '', 2*x - 5 + x**3 - 4*x**2, x**3 - 4*x**2 + 2*x - 5)
chk(L, 5, '(1)', 2*a**2 - 5*a**2 - b**2 + a**2 + b**2, -2*a**2)
chk(L, 5, '(2)', 6*x - (2*x - 3*(x - 1)), 7*x - 3)
chk(L, 6, '', (2*a + b) - (2*a - b), 2*b)
chk(L, 7, '(1) m=3 時次數', tdeg(-2*x**3*y**3), 6)
chk(L, 7, '(2) n=4 時次數', tdeg(x**4 - 5*x + 2), 4)
e = 3*(x**2 - x*y) - 2*(x**2 - 2*x*y) + x*y
chk(L, 8, '化簡', e, x**2 + 2*x*y)
chk(L, 8, '求值', e.subs({x: -1, y: 2}), -3)
chk(L, 9, '恆等', (m**2 + m*n) - (n**2 - m*n), m**2 + 2*m*n - n**2)
chk(L, 9, '值', 4 - 7, -3)
chk(L, 10, 'A−(3−x)', (5 - x) - (3 - x), 2)
chk(L, 11, '第二邊', (3*a + 2*b) - a, 2*a + 2*b)
chk(L, 11, '第三邊', (2*a + 2*b) + b, 2*a + 3*b)
chk(L, 11, '周長', (3*a + 2*b) + (2*a + 2*b) + (2*a + 3*b), 7*a + 7*b)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '驗算_第四章_整式的加減.md')
with io.open(out, 'w', encoding='utf-8') as f:
    f.write('# 驗算：初一數學 第四章〈整式的加減〉六份講義練習\n\n')
    f.write('- 由 `verify_ch4.py` 以 sympy 逐題重算產生；「重算值」是程式由題目算出的結果，「講義答案」是印在教師用參考答案的結果。\n')
    f.write('- 題目全部自擬（與課本、舊卷同型不同數）。判斷題與開放題列為「人工核對」。\n\n')
    cur = None
    for les, no, desc, got, want, st in ROWS:
        if les != cur:
            cur = les
            f.write(f'\n## 第 {les}\n\n| 題號 | 項目 | 重算值 | 講義答案 | 結果 |\n|---|---|---|---|---|\n')
        f.write(f'| {no} | {desc} | `{got}` | `{want}` | {st} |\n')
    f.write(f'\n合計 {len(ROWS)} 項，FAIL {BAD} 項。\n')
sys.stdout.write(f'rows={len(ROWS)} fail={BAD}\n')
sys.exit(1 if BAD else 0)
