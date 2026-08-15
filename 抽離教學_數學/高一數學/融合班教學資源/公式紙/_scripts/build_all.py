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
    ('data_02_函數的概念與性質.json', '公式紙_高一數學_02函數的概念與性質.docx'),
    ('data_03_指數與對數.json', '公式紙_高一數學_03指數與對數.docx'),
    ('data_04_多項式與因式定理.json', '公式紙_高一數學_04多項式與因式定理.docx'),
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
