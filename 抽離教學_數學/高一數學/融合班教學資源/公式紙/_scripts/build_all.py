# -*- coding: utf-8 -*-
"""build_all.py — 一次產出第一學段四個單元的公式紙 .docx

用法：python build_all.py
資料檔＝同資料夾的 data_NN_*.json；輸出到上一層（公式紙\）。
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.dirname(HERE)
BUILDER = os.path.join(os.path.expanduser('~'), '.claude', 'skills',
                       'jh-math-formula-sheet', 'scripts',
                       'build_formula_sheet.py')

JOBS = [
    ('data_01_集合與常用邏輯用語.json', '公式紙_高一數學_01集合與常用邏輯用語.docx'),
    # 2026-08-21：單元二原本 5 區 38 條、3 頁。合併冪函數＋去重後仍 3 頁，改為拆上／下兩張。
    ('data_02A_函數的概念與性質.json', '公式紙_高一數學_02A函數的概念與性質.docx'),
    ('data_02B_冪函數與複合函數.json', '公式紙_高一數學_02B冪函數與複合函數.docx'),
    # 2026-08-21：單元三原本 46 列 7 節、擠成 3 頁（違反 ≤2 頁規則），拆成上／下兩張，
    # 各自 ≤2 頁、零內容刪減。舊的合併版已退役到 _archive\退役交付檔\。
    ('data_03A_指數與對數函數.json', '公式紙_高一數學_03A指數與對數函數.docx'),
    ('data_03B_指對數運算與方程.json', '公式紙_高一數學_03B指對數運算與方程.docx'),
    # 2026-08-21：單元四同樣拆上／下兩張（原 4 區 26 條、3 頁）。
    ('data_04A_多項式與因式定理.json', '公式紙_高一數學_04A多項式與因式定理.docx'),
    ('data_04B_二次函數與一元二次不等式.json',
     '公式紙_高一數學_04B二次函數與一元二次不等式.docx'),
]


def main():
    bad = 0
    for src, dst in JOBS:
        r = subprocess.run(
            [sys.executable, BUILDER, os.path.join(HERE, src),
             os.path.join(OUT_DIR, dst)],
            capture_output=True, text=True, encoding='utf-8')
        status = 'OK  ' if r.returncode == 0 else 'FAIL'
        print(f'{status} {dst}')
        for line in (r.stdout or '').splitlines():
            print('      ', line)
        if r.returncode:
            bad += 1
            for line in (r.stderr or '').splitlines()[-12:]:
                print('   ERR', line)
    print(f'\n=== 失敗 {bad} / {len(JOBS)} ===')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
