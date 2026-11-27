# -*- coding: utf-8 -*-
"""build_homework_20261127.py — 初一丙週末功課（5.1-1、5.1-2、5.2-1）。

執行：python build_homework_20261127.py
sympy 逐題驗算（寫入同資料夾 驗算_*.md）全部 PASS 才出 docx。
"""
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from ch5_common import (para, heading, masthead, student_info_row, shaded_box, shaded_multi_box,  # noqa: E402
                        build_docx, write_lines, star_label, pbox, grid, cols, q, qparts, answers,
                        nm, GAP, W_IN, SUBJ, FOOT, BLANK, CHECKBOX)

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NAME = '功課_週末_5.1至5.2-1_方程至合併同類項_融合版'
x, y, a = sp.symbols('x y a')


def R(p, q_=1):
    return sp.Rational(p, q_)


# ------------------------------------------------------------ 驗算（先於出檔）
def solve(l, r):
    s = sp.solve(sp.Eq(l, r), x)
    assert len(s) == 1
    return s[0]


CHECKS = [
    # (題號, 算式／項目, 重算值, 功課答案)
    ('2(1)', '4x+3=23 的解（列方程可解）', solve(4*x + 3, 23), 5),
    ('2(2)', 'x−6=10 的解', solve(x - 6, 10), 16),
    ('2(3)', '50−5x=15 的解', solve(50 - 5*x, 15), 7),
    ('3(1)', 'x=4：3x+2 與 14', ((3*x + 2).subs(x, 4), 14), (14, 14)),
    ('3(2)', 'x=2：5x−1 與 2x+8', ((5*x - 1).subs(x, 2), (2*x + 8).subs(x, 2)), (9, 12)),
    ('3(3)', 'x=3：5x−1 與 2x+8', ((5*x - 1).subs(x, 3), (2*x + 8).subs(x, 3)), (14, 14)),
    ('4(1)', 'x−4=10', solve(x - 4, 10) - 10, 4),
    ('4(2)', 'x+7=12', 12 - solve(x + 7, 12), 7),
    ('4(3)', '5x=35', solve(5*x, 35), 7),
    ('4(4)', 'x/4=3', solve(x/4, 3), 12),
    ('5(3)', '−3x=15 的解', solve(-3*x, 15), -5),
    ('6(1)', 'x−8=−3', solve(x - 8, -3), 5),
    ('6(2)', '−4x=28', solve(-4*x, 28), -7),
    ('6(3)', '3x+4=19', solve(3*x + 4, 19), 5),
    ('7(1)', '3x+2x=20', solve(3*x + 2*x, 20), 4),
    ('7(2)', '7x−4x=−15', solve(7*x - 4*x, -15), -5),
    ('7(3)', '2x−6x=12', solve(2*x - 6*x, 12), -3),
    ('8(1)', '8x−3x=−30', solve(8*x - 3*x, -30), -6),
    ('8(2)', 'x+4x=17−2', solve(x + 4*x, 17 - 2), 3),
    ('8(3)', '5x−7x+x=9', solve(5*x - 7*x + x, 9), -9),
    ('9', 'x+3x=48（科普、故事）', (solve(x + 3*x, 48), 3*solve(x + 3*x, 48)), (12, 36)),
    ('10', 'x=3 代入 2x+a=11', sp.solve(sp.Eq(2*3 + a, 11), a)[0], 5),
    ('記一記', '2x−1=9', solve(2*x - 1, 9), 5),
    ('記一記', '6x−2x=12', solve(6*x - 2*x, 12), 3),
]


def verify():
    out = ['# 驗算：初一週末功課（2026-11-27，5.1-1、5.1-2、5.2-1）', '',
           '- 由 `build_homework_20261127.py` 以 sympy 逐題重算；判斷題與列方程的式子列為人工核對。', '',
           '| 題號 | 項目 | 重算值 | 功課答案 | 結果 |', '|---|---|---|---|---|']
    bad = []
    for no, item, got, want in CHECKS:
        ok = got == want
        out.append(f'| {no} | {item} | `{got}` | `{want}` | {"PASS" if ok else "FAIL"} |')
        if not ok:
            bad.append(no)
    out += ['| 1 | 方程／一元一次方程判斷 | `方程：3x−2=7、x+y=8、x²=4、y/2=5；一元一次：3x−2=7、y/2=5` | 同左 | 人工核對 |',
            '| 2 | 列出的方程 | `4x+3=23；x−6=10；50−5x=15` | 同左 | 人工核對 |',
            '| 5 | 判斷 | `對／對／不對／不對` | 同左 | 人工核對 |', '',
            f'共 {len(CHECKS)} 項程式驗算；FAIL：{"、".join(bad) or "無"}', '']
    io.open(os.path.join(HERE, '驗算_週末功課_5.1至5.2-1.md'), 'w', encoding='utf-8').write('\n'.join(out))
    print(f'驗算 {len(CHECKS)} 項，FAIL：{bad or "無"}')
    assert not bad


# ------------------------------------------------------------ 版面
def memo(title, *lines):
    return shaded_multi_box([para(f'記一記：{title}', bold=True, keep_next=True)]
                            + [para(nm(s), keep_next=True) for s in lines], trailing_blank=False) + GAP


def side(title, eqs, n=3):
    """三小題並排：每欄上面是方程，下面是作答線。"""
    cells = [[para(nm(e))] + write_lines(n) for e in eqs]
    return pbox([para(title), grid([cells], cols(3, W_IN), head=False, inner=True)])


def build():
    P = [masthead(SUBJ, '第五章 一元一次方程（5.1 至 5.2 第 1 課時）', '週末功課'), student_info_row(),
         shaded_box('先看「記一記」，再做題目。第 10 題是挑戰題，可以選做。')]

    # ---- 一
    P += [heading(f'一、方程與方程的解（{star_label(1)}）'),
          memo('方程',
               '方程：含有未知數的等式。　　方程的解：使左、右兩邊相等的未知數的值。',
               '一元一次方程：只有一個未知數，次數是 1，分母沒有未知數。')]
    w = cols(7, W_IN, first=2300)
    P += [pbox([para('1．哪些是方程？哪些是一元一次方程？在方格內打勾。'),
                grid([('', '{3x-2=7}', '{5+4=9}', '{2y+1}', '{x+y=8}', '{x^2=4}', '{frac(y,2)=5}'),
                      ('是方程', *[CHECKBOX] * 6),
                      ('是一元一次方程', *[CHECKBOX] * 6)], w, inner=True)]),
          pbox([para('2．列方程（不用解）。'),
                para(f'(1) {{x}} 的 4 倍加上 3，等於 23。　方程：{BLANK}{BLANK}'),
                para(f'(2) 比 {{x}} 少 6 的數是 10。　方程：{BLANK}{BLANK}'),
                para(f'(3) 練習簿每本 {{x}} 元，買 5 本，付 50 元，找回 15 元。　方程：{BLANK}{BLANK}')]),
          pbox([para('3．把 {x} 的值代入左、右兩邊，判斷它是不是方程的解。'),
                grid([('方程', '{x} 的值', '左邊', '右邊', '是不是解'),
                      ('{3x+2=14}', '{x=4}', f'{{3*4+2}} ＝ {BLANK}', '14', ''),
                      ('{5x-1=2x+8}', '{x=2}', '', '', ''),
                      ('{5x-1=2x+8}', '{x=3}', '', '', '')],
                     [2300, 1300, 2600, 2600, W_IN - 8800], inner=True, row_h=540)])]

    # ---- 二
    P += [heading(f'二、等式的性質（{star_label(1)}）'),
          memo('等式的性質',
               '① 等式兩邊加（或減）同一個數，結果仍相等。',
               '② 等式兩邊乘同一個數，或除以同一個不是 0 的數，結果仍相等。',
               '例：{2x-1=9}　→　兩邊加 1：{2x=10}　→　兩邊除以 2：{x=5}'),
          pbox([para('4．填空。'),
                grid([(f'(1) 如果 {{x-4=10}}，那麼 {{x=10+}} {BLANK}', f'(2) 如果 {{x+7=12}}，那麼 {{x=12-}} {BLANK}'),
                      (f'(3) 如果 {{5x=35}}，那麼 {{x=}} {BLANK}', f'(4) 如果 {{frac(x,4)=3}}，那麼 {{x=}} {BLANK}')],
                     cols(2, W_IN), head=False, inner=True, row_h=620)]),
          pbox([para('5．判斷對錯，圈出答案。'),
                grid([('題目', '圈答案'),
                      ('(1) 如果 {a=b}，那麼 {a+2=b+2}。', '對　　不對'),
                      ('(2) 如果 {a=b}，那麼 {3a=3b}。', '對　　不對'),
                      ('(3) 由 {-3x=15}，得 {x=5}。', '對　　不對'),
                      ('(4) 如果 {a=b}，那麼 {a-5=b+5}。', '對　　不對')],
                     [W_IN - 2400, 2400], inner=True, row_h=480)]),
          side('6．利用等式的性質解方程。', ['(1) {x-8=-3}', '(2) {-4x=28}', '(3) {3x+4=19}'])]

    # ---- 三
    P += [heading(f'三、合併同類項解方程（{star_label(2)}）'),
          memo('標 → 合 → 化',
               '標：① 含 {x} 的項，② 常數項（符號一起標）。　合：合併同類項。　化：兩邊除以 {x} 的係數。',
               '例：{6x-2x=12}　→　合：{4x=12}　→　化：{x=3}'),
          pbox([para('7．解方程。已經替你標好 ①②。'),
                grid([('方程', '合：化成 {ax=b}', '化：{x=}'),
                      ('(1) {3x}① {+2x}① ＝ 20②', '', ''),
                      ('(2) {7x}① {-4x}① ＝ {-15}②', '', ''),
                      ('(3) {2x}① {-6x}① ＝ 12②', '', '')],
                     [4200, 3000, W_IN - 7200], inner=True, row_h=500)]),
          side('8．解方程。', ['(1) {8x-3x=-30}', '(2) {x+4x=17-2}', '(3) {5x-7x+x=9}']),
          q(['9．圖書角共有故事書和科普書 48 本，故事書的本數是科普書的 3 倍。兩種書各有多少本？',
             f'設科普書有 {{x}} 本，則故事書有 {BLANK} 本。　方程：{BLANK}{BLANK}'], n=2),
          q(['10．（挑戰，選做）已知 {x=3} 是方程 {2x+a=11} 的解，求 {a} 的值。'], n=2, last=True)]

    P += answers([
        '1．方程：{3x-2=7}，{x+y=8}，{x^2=4}，{frac(y,2)=5}；一元一次方程：{3x-2=7}，{frac(y,2)=5}',
        '2．(1) {4x+3=23}　(2) {x-6=10}　(3) {50-5x=15}（或 {5x+15=50}）',
        '3．{x=4}：左邊 14，右邊 14，是解；{x=2}：左邊 9，右邊 12，不是解；{x=3}：左邊 14，右邊 14，是解',
        '4．(1) 4　(2) 7　(3) 7　(4) 12',
        '5．(1) 對　(2) 對　(3) 不對，{x=-5}　(4) 不對，兩邊要同時減 5',
        '6．(1) {x=5}　(2) {x=-7}　(3) {3x=15}，{x=5}',
        '7．(1) {5x=20}，{x=4}　(2) {3x=-15}，{x=-5}　(3) {-4x=12}，{x=-3}',
        '8．(1) {5x=-30}，{x=-6}　(2) {5x=15}，{x=3}　(3) {-x=9}，{x=-9}',
        '9．故事書 {3x} 本；{x+3x=48}，{4x=48}，{x=12}。答：科普書 12 本，故事書 36 本。',
        '10．把 {x=3} 代入：{6+a=11}，{a=5}',
    ])
    print(build_docx(P, os.path.join(HERE, NAME + '.docx'), footer_text=FOOT))


if __name__ == '__main__':
    verify()
    build()
