# -*- coding: utf-8 -*-
"""
validate_data.py — 公式紙資料前置驗證

在呼叫 build_formula_sheet.py 之前，先把每一條 name/formula/note 丟進
{} 解析器跑一次，並掃描「印出來會變垃圾字串」的已知地雷：
  - LaTeX 反斜線指令（\\neq、\\infty…）：解析器不認得，會原樣印在考卷上
  - HTML 實體（&gt; &lt; &amp;）：來源抽取常見殘留
  - 裸 infty / inf ty：應寫 Unicode ∞
  - 斜體連字的 log/sin/cos：應寫 fn(log) 等正體函數名

（2026-07-21 既有成品 公式紙_高一數學_4.1-4.4指數與對數.pdf 就是踩了前兩項，
  印出 `a \\!\\neq 1`、`(0,+infty)`。本檔即為防止重演。）

用法：python validate_data.py <data*.json> [more.json ...]
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.expanduser('~'),
                                '.claude', 'skills', '_shared-math-docx'))
from omml_core import text_to_segments, math_to_omml, MathParseError  # noqa: E402

LANDMINES = [
    (re.compile(r'\\[A-Za-z!]'), 'LaTeX 反斜線指令（解析器不認得，會原樣印出）'),
    (re.compile(r'&(gt|lt|amp|nbsp);'), 'HTML 實體殘留'),
    (re.compile(r'(?<![A-Za-z])inf(ty)?(?![A-Za-z])'), '裸 infty（應寫 Unicode ∞）'),
    (re.compile(r'\{[^}]*(?<![a-z(])(log|sin|cos|tan|lg|ln)_'),
     '對數/三角函數未用 fn() 包（會印成斜體連字）'),
    (re.compile(r'sqrt\(\s*\)'), '空根號（會印出沒有被開方數的 √ 殘件）'),
    (re.compile(r'　／　'), '用 ／ 分隔多條式子（易與集合條件豎線 ｜ 混淆，改用 \\n 分行）'),
]

# 集合建構式：ASCII { } 會被 {} 標記語法當分隔符吃掉，印出來就少了大括號。
# 2026-07-21 實錄：'{A∪B}＝{x｜x∈A 或 x∈B}' 印成 A∪B＝x｜x∈A 或 x∈B（大括號不見了）。
# 規則：含全形豎線 ｜（set-builder 標記）的數學片段，必須同時含全形 ｛ ｝。
_SETBUILDER = re.compile(r'\{([^{}]*｜[^{}]*)\}')


def check_setbuilder(label, text, problems):
    for m in _SETBUILDER.finditer(text or ''):
        body = m.group(1)
        if '｛' not in body or '｝' not in body:
            problems.append(
                f'{label} 集合建構式缺全形大括號（ASCII {{}} 會被吃掉，印出來沒有大括號）'
                f' ← {m.group(0)}　應寫成 {{｛{body}｝}}')


def check_field(label, text, problems):
    if not text:
        return
    for rx, why in LANDMINES:
        m = rx.search(text)
        if m:
            problems.append(f'{label} 地雷[{why}] 命中 {m.group(0)!r} ← {text}')
    check_setbuilder(label, text, problems)
    try:
        segs = text_to_segments(text)
    except Exception as e:
        problems.append(f'{label} 分段失敗：{e} ← {text}')
        return
    for kind, payload in segs:
        if kind != 'm':
            continue
        if not payload.lstrip().startswith('<m:'):
            problems.append(f'{label} 公式片段未包成 OMML ← {payload!r}')


def main(paths):
    grand = 0
    for p in paths:
        with open(p, encoding='utf-8') as f:
            data = json.load(f)
        problems, n = [], 0
        for sec in data['sections']:
            st = sec['title']
            for item in sec['formulas']:
                n += 1
                tag = f"[{os.path.basename(p)}] {st} / {item.get('name','?')}"
                for key in ('name', 'formula', 'note'):
                    check_field(f'{tag} .{key}', item.get(key, ''), problems)
        head = f'{os.path.basename(p)}：{len(data["sections"])} 區 / {n} 條'
        if problems:
            print(f'FAIL {head}')
            for x in problems:
                print('   -', x)
        else:
            print(f'PASS {head}')
        grand += len(problems)
    print(f'\n=== 總問題數：{grand} ===')
    return 1 if grand else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
