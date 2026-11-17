# -*- coding: utf-8 -*-
"""build_game_4.2.py — 初一 4.2〈整式的加減〉課堂互動遊戲：題庫＋sympy 驗算＋注入兩個 HTML。

題庫只在這裡改一次；執行後：
  1. 每題用 sympy 驗算（答案＝題目化簡結果；每個干擾項都≠答案）；
  2. 把題庫（JSON）寫進手機版與投影版 HTML 的 /*BANK*/ … /*END*/ 之間；
  3. 驗算表印到 stdout，可貼進 驗算_第四章_整式的加減.md。
用語、記號、手順步驟對齊 講義練習_4.2-1／4.2-2／4.2-3（_融合版）。
"""
import io, json, re, sys
from pathlib import Path
import sympy as sp

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = Path(__file__).resolve().parent
a, b, c, m, n, x, y = sp.symbols('a b c m n x y')
NS = dict(a=a, b=b, c=c, m=m, n=n, x=x, y=y)


def E(s):
    """'3x^2-4y' → sympy（補乘號）。"""
    s = s.replace('^', '**')
    s = re.sub(r'(\d)([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z)])([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z)])(\d)', r'\1*\2', s)  # 不會出現，保險
    return sp.expand(sp.sympify(s, locals=NS))


def strip(t):
    return t.replace('$', '')


# ---------------------------------------------------------------------
# 題庫：t＝mc 選擇／yn 是不是同類項／line 哪一行出錯（選項次序固定）
# chk：('expr', 題目式) → 答案與干擾項逐一比對；('val', 題目式, {代入}) → 數值
# ---------------------------------------------------------------------
LEVELS = [
 {'key': '合併同類項', 'short': '合併', 'sec': '4.2-1', 'steps': ['找', '移', '加', '查'],
  'tips': ['用 ①②③ 標出同類項', '連符號一起搬', '係數相加，字母和指數照抄', '還有同類項嗎？'],
  'rule': '同類項：字母相同，指數也相同。合併：係數相加，字母和指數照抄。',
  'qs': [
   {'id': '1a', 't': 'yn', 'core': 1, 'q': '$-6mn^2$　與　$n^2m$', 'a': '是',
    'why': '字母都是 $m$、$n$；$m$ 的指數都是 1，$n$ 的指數都是 2。字母次序不同沒關係。',
    'chk': ('like', '-6mn^2', 'n^2m')},
   {'id': '1b', 't': 'mc', 'core': 1, 'q': '$a^2+a^2$ ＝ ？', 'a': '$2a^2$', 'o': ['$a^4$', '$2a^4$', '$a^2$'],
    'why': '[[加]] 係數 1＋1＝2，字母和指數照抄：$2a^2$。指數不相加，不是 $a^4$。',
    'chk': ('expr', 'a^2+a^2')},
   {'id': '1c', 't': 'mc', 'q': '$-7ab+6ab$ ＝ ？', 'a': '$-ab$', 'o': ['$-1$', '$ab$', '$-13ab$'],
    'why': '[[加]] 係數 $-7+6=-1$，$-1ab$ 寫成 $-ab$。字母 $ab$ 照抄，不會消失。',
    'chk': ('expr', '-7ab+6ab')},
   {'id': '1d', 't': 'mc', 'core': 1, 'q': '$3a+2b$ ＝ ？', 'a': '不能再合併', 'o': ['$5ab$', '$5a$', '$5b$'],
    'why': '$3a$ 和 $2b$ 字母不同，不是同類項，絕對不能合併成 $5ab$！答案就是原樣照抄。',
    'chk': ('nolike', '3a', '2b')},
   {'id': '1e', 't': 'mc', 'core': 1, 'q': '合併同類項：$3x-4y-5x+y$', 'a': '$-2x-3y$',
    'o': ['$-2x-4y$', '$8x-3y$', '$-2x-5y$'],
    'why': '[[找]] $3x$①　$-4y$②　$-5x$①　$+y$②　[[加]] $x$ 項 $3-5=-2$；$y$ 項 $-4+1=-3$。最後的 $y$ 係數是 1，不是 0。',
    'chk': ('expr', '3x-4y-5x+y')},
   {'id': '1f', 't': 'mc', 'q': '合併同類項：$2x^2-3x+5-2x^2+x$', 'a': '$-2x+5$',
    'o': ['$4x^2-2x+5$', '$-4x+5$', '$-2x-5$'],
    'why': '[[加]] $x^2$ 項 $2-2=0$，$0x^2$ 等於 0，不用寫；$x$ 項 $-3+1=-2$；常數 5 照抄。',
    'chk': ('expr', '2x^2-3x+5-2x^2+x')},
  ]},
 {'key': '去括號', 'short': '去括號', 'sec': '4.2-2', 'steps': ['看', '乘', '定號', '合'],
  'tips': ['括號前面是什麼？', '乘括號內每一項', '括號前是「−」，每一項都變號', '再合併同類項'],
  'rule': '括號前是「＋」：各項全部不變號；是「−」：各項全部變號；是一個數：每一項都要乘。',
  'qs': [
   {'id': '2a', 't': 'mc', 'core': 1, 'q': '去括號：$-(x-3)$', 'a': '$-x+3$', 'o': ['$-x-3$', '$x-3$', '$x+3$'],
    'why': '[[看]] 括號前是「−」，沒有寫數字，就是乘 $-1$。[[定號]] 每一項都變號：$-x+3$。',
    'chk': ('expr', '-(x-3)')},
   {'id': '2b', 't': 'mc', 'core': 1, 'q': '去括號：$a-(b-c)$', 'a': '$a-b+c$', 'o': ['$a-b-c$', '$a+b-c$', '$a+b+c$'],
    'why': '[[定號]] 括號前是「−」，括號內的第二項 $-c$ 也要變號，變成 $+c$。',
    'chk': ('expr', 'a-(b-c)')},
   {'id': '2c', 't': 'mc', 'core': 1, 'q': '去括號：$2(x-3)$', 'a': '$2x-6$', 'o': ['$2x-3$', '$2x+6$', '$x-6$'],
    'why': '[[乘]] 2 乘括號內每一項：$2×x=2x$，$2×(-3)=-6$。最後一項最容易漏乘。',
    'chk': ('expr', '2(x-3)')},
   {'id': '2d', 't': 'mc', 'q': '去括號：$-3(a+4)$', 'a': '$-3a-12$', 'o': ['$-3a+12$', '$-3a+4$', '$3a-12$'],
    'why': '[[乘]] 括號外的數連符號是 $-3$：$(-3)×a=-3a$，$(-3)×4=-12$。',
    'chk': ('expr', '-3(a+4)')},
   {'id': '2e', 't': 'mc', 'core': 1, 'q': '化簡：$5x-(2x-1)$', 'a': '$3x+1$', 'o': ['$3x-1$', '$7x-1$', '$-3x+1$'],
    'why': '[[定號]] $-(2x-1)$ 得 $-2x+1$。[[合]] $5x-2x+1=3x+1$。',
    'chk': ('expr', '5x-(2x-1)')},
   {'id': '2f', 't': 'line', 'q': '下面的化簡，哪一行出錯？<br>$(3y-2)-2(4-y)$<br>第 1 行　$=3y-2-8-2y$<br>第 2 行　$=y-10$',
    'a': '第 1 行', 'o': ['第 1 行', '第 2 行', '沒有錯'],
    'why': '第 1 行：$(-2)×(-y)$ 得 $+2y$，不是 $-2y$。正確是 $3y-2-8+2y=5y-10$。',
    'chk': ('line', '(3y-2)-2(4-y)', ['3y-2-8-2y', 'y-10'])},
  ]},
 {'key': '整式的加減', 'short': '加減', 'sec': '4.2-3', 'steps': ['括', '去', '合', '代'],
  'tips': ['每個整式先加括號', '去括號', '合併同類項', '化簡完才代入'],
  'rule': '有括號就先去括號，再合併同類項。求和或差：每個整式先加括號。要求值：化簡完才代入。',
  'qs': [
   {'id': '3a', 't': 'mc', 'core': 1, 'q': '計算：$(2x+5y)-(x-3y)$', 'a': '$x+8y$', 'o': ['$x+2y$', '$3x+8y$', '$x-8y$'],
    'why': '[[去]] $-(x-3y)$ 得 $-x+3y$。[[合]] $2x-x+5y+3y=x+8y$。',
    'chk': ('expr', '(2x+5y)-(x-3y)')},
   {'id': '3b', 't': 'mc', 'core': 1, 'long': 1, 'q': '求 $2a+b$ 與 $a-3b$ 的<u>差</u>，應該怎樣列式？',
    'a': '$(2a+b)-(a-3b)$', 'o': ['$2a+b-a-3b$', '$(2a+b)+(a-3b)$', '$(a-3b)-(2a+b)$'],
    'why': '[[括]] 求差：每個整式先加括號，中間寫「−」。漏了括號，$-3b$ 就不會變號。',
    'chk': ('expr', '(2a+b)-(a-3b)')},
   {'id': '3c', 't': 'mc', 'q': '求 $4m-n$ 與 $2m+3n$ 的<u>和</u>。', 'a': '$6m+2n$', 'o': ['$2m-4n$', '$6m+4n$', '$6m-2n$'],
    'why': '[[括]] $(4m-n)+(2m+3n)$。[[去]] 括號前是「＋」，各項不變號。[[合]] $6m+2n$。',
    'chk': ('expr', '(4m-n)+(2m+3n)')},
   {'id': '3d', 't': 'mc', 'core': 1, 'q': '計算：$3(a^2-b)-(2a^2-3b)$', 'a': '$a^2$', 'o': ['$a^2-6b$', '$5a^2-6b$', '$a^2+6b$'],
    'why': '[[去]] $3a^2-3b-2a^2+3b$。[[合]] $a^2$ 項 $3-2=1$；$b$ 項 $-3+3=0$，不用寫。結果是 $a^2$。',
    'chk': ('expr', '3(a^2-b)-(2a^2-3b)')},
   {'id': '3e', 't': 'mc', 'core': 1, 'q': '先化簡，再求值：$(3x-2)-(x-4)$，其中 $x=-3$', 'a': '$-4$',
    'o': ['$-12$', '$8$', '$4$'],
    'why': '[[去]][[合]] $3x-2-x+4=2x+2$。[[代]] 負數加括號：$2×(-3)+2=-4$。',
    'chk': ('val', '(3x-2)-(x-4)', {'x': -3})},
   {'id': '3f', 't': 'mc', 'q': '一個多項式加上 $x-4$，得到 $3x+2$。這個多項式是？', 'a': '$2x+6$',
    'o': ['$2x-2$', '$4x-2$', '$-2x-6$'],
    'why': '[[括]] 所求＝$(3x+2)-(x-4)$。[[去]] $3x+2-x+4$。[[合]] $2x+6$。',
    'chk': ('expr', '(3x+2)-(x-4)')},
  ]},
]


def monos(s):
    """單項式 → (係數, 字母指數 dict)。"""
    e = E(s)
    coeff, rest = e.as_coeff_Mul()
    return coeff, sp.Poly(e, *[a, b, c, m, n, x, y]).monoms()[0]


def verify():
    rows, bad = [], []
    for L in LEVELS:
        for Q in L['qs']:
            k = Q['chk']
            note = ''
            if k[0] == 'like':
                same = monos(k[1])[1] == monos(k[2])[1]
                ok = same == (Q['a'] == '是')
                note = '字母與指數' + ('相同' if same else '不同')
            elif k[0] == 'nolike':
                same = monos(k[1])[1] == monos(k[2])[1]
                ok = not same and all(E(strip(o)) != E(k[1]) + E(k[2]) for o in Q['o'])
                note = '字母不同；三個干擾項都≠原式'
            elif k[0] == 'expr':
                val = E(k[1])
                ok = E(strip(Q['a'])) == val
                for o in Q['o']:
                    if E(strip(o)) == val:
                        ok = False; note += f'干擾項 {o} 等於答案！'
                note = note or f'化簡＝{sp.sstr(val)}；干擾項 {len(Q["o"])} 個皆≠'
            elif k[0] == 'val':
                simp = E(k[1])
                v = simp.subs({NS[s]: val for s, val in k[2].items()})
                ok = sp.Integer(int(strip(Q['a']))) == v and all(sp.Integer(int(strip(o))) != v for o in Q['o'])
                note = f'化簡＝{sp.sstr(simp)}；代入得 {v}'
            elif k[0] == 'line':
                start, lines = E(k[1]), [E(t) for t in k[2]]
                first_bad = next((i + 1 for i, t in enumerate(lines) if t != start), None)
                # 第 2 行要和第 1 行一致（只錯一處）
                consistent = all(lines[i] == lines[i + 1] for i in range(len(lines) - 1))
                ok = consistent and Q['a'] == (f'第 {first_bad} 行' if first_bad else '沒有錯')
                note = f'原式＝{sp.sstr(start)}；第 1 行＝{sp.sstr(lines[0])}（錯），第 2 行與第 1 行一致'
            if Q['t'] != 'yn' and Q['t'] != 'line':
                if Q['a'] in Q['o'] or len(set(Q['o'])) != len(Q['o']):
                    ok = False; note += '；選項重複'
            rows.append((L['sec'], Q['id'], '★' if Q.get('core') else '', strip(Q['q']).replace('<br>', ' ／ '),
                         strip(Q['a']), note, 'PASS' if ok else 'FAIL'))
            if not ok:
                bad.append(Q['id'])
    return rows, bad


def inject(rows):
    data = [{k: v for k, v in L.items() if k != 'qs'} | {'qs': [{k: v for k, v in Q.items() if k != 'chk'} for Q in L['qs']]}
            for L in LEVELS]
    js = json.dumps(data, ensure_ascii=False, indent=1)
    for f in ['互動遊戲_4.2_整式加減大挑戰.html', '互動遊戲_4.2_整式加減大挑戰_投影版.html']:
        p = HERE / f
        t = p.read_text(encoding='utf-8')
        t2, k = re.subn(r'/\*BANK\*/.*?/\*END\*/', lambda _: '/*BANK*/' + js + '/*END*/', t, flags=re.S)
        assert k == 1, f
        p.write_text(t2, encoding='utf-8')
        print('注入', f)


if __name__ == '__main__':
    rows, bad = verify()
    print('| 節 | # | 5 分鐘版 | 題目 | 答案 | 驗算 | 結果 |\n|---|---|---|---|---|---|---|')
    for r in rows:
        print('| ' + ' | '.join(r) + ' |')
    print(f'\n共 {len(rows)} 題；5 分鐘版 {sum(1 for r in rows if r[2])} 題；FAIL：{bad or "無"}')
    if bad:
        sys.exit(1)
    if '--inject' in sys.argv:
        inject(rows)
