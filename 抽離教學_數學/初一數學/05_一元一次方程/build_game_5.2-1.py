# -*- coding: utf-8 -*-
"""build_game_5.2-1.py — 初一 5.2-1〈合併同類項〉課堂互動遊戲（投影版）＋講義紀錄表。

題庫只在這裡改一次（由 講義練習_5.2-1_合併同類項_融合版 的重溫與練習第 1–5 題改寫成選擇／是非題）。
執行：
  python build_game_5.2-1.py            只驗算（sympy），驗算表印到 stdout
  python build_game_5.2-1.py --inject   驗算通過後：題庫注入投影版 HTML，並出講義紀錄表 docx
選項次序在這裡定死（投影版與紀錄表的 ①②③④ 完全一致），學生可以在紙上圈號碼。
"""
import io, json, random, re, sys
from pathlib import Path
import sympy as sp

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = Path(__file__).resolve().parent
a, x, y = sp.symbols('a x y')
NS = dict(a=a, x=x, y=y)
CIRC = '①②③④'

# ---------------------------------------------------------------------
# 記法：$…$ 包住數學式；F(p,q) 分數；[[步驟]] 解說裡的步驟字卡；<br> 題目換行。
# t：yn 二選一（yl＝兩個選項字）；mc 四選一（opts＝選項次序照寫，不重排）
# mvd：合併後的方程（紀錄表「合併後：」格的答案，教師頁列出）
# chk：驗算方式，見 verify()
# ---------------------------------------------------------------------
TF = ['對', '不對']
LINES = ['第 1 行', '第 2 行', '第 3 行', '沒有錯']
LEVELS = [
 {'key': '合併同類項', 'short': '合併', 'sec': '對應重溫、練習第 1 題',
  'steps': ['標', '合'],
  'tips': ['符號跟著項一起看', '係數相加減，$x$ 照抄'],
  'rule': '合併同類項：係數相加減，$x$ 照抄。$x$ 的係數是 1，$-x$ 的係數是 $-1$。',
  'qs': [
   {'id': '1a', 't': 'mc', 'core': 1, 'ask': '合併後是哪一個？', 'q': '$4x+3x$', 'a': '$7x$',
    'o': ['$7x^2$', '$12x$', '$7$'],
    'why': '[[合]] 係數相加：$4+3=7$，$x$ 照抄，得 $7x$。',
    'chk': ('simp', '4x+3x')},
   {'id': '1b', 't': 'mc', 'core': 1, 'ask': '合併後是哪一個？', 'q': '$5x-2x$', 'a': '$3x$',
    'o': ['$7x$', '$-3x$', '$3$'],
    'why': '[[標]] 第二項是 $-2x$。[[合]] $5-2=3$，得 $3x$。',
    'chk': ('simp', '5x-2x')},
   {'id': '1c', 't': 'mc', 'core': 1, 'ask': '合併後是哪一個？', 'q': '$x-3x$', 'a': '$-2x$',
    'o': ['$2x$', '$-3x$', '$4x$'],
    'why': '[[標]] $x$ 的係數是 1。[[合]] $1-3=-2$，得 $-2x$。',
    'chk': ('simp', 'x-3x')},
   {'id': '1d', 't': 'mc', 'core': 1, 'ask': '合併後是哪一個？', 'q': '$2x-7x+x$', 'a': '$-4x$',
    'o': ['$-5x$', '$-6x$', '$4x$'],
    'why': '[[合]] 三個係數一起算：$2-7+1=-4$，得 $-4x$。最後的 $x$ 不要漏。',
    'chk': ('simp', '2x-7x+x')},
   {'id': '1e', 't': 'mc', 'ask': '合併後是哪一個？', 'q': '$F(1,2)x+F(3,2)x$', 'a': '$2x$',
    'o': ['$x$', '$F(3,4)x$', '$4x$'],
    'why': '[[合]] $F(1,2)+F(3,2)=F(4,2)=2$，得 $2x$。同分母相加，分母不變。',
    'chk': ('simp', 'F(1,2)x+F(3,2)x')},
   {'id': '1f', 't': 'yn', 'yl': TF, 'core': 1, 'ask': '這句話對不對？', 'q': '$-x$ 的係數是 $-1$。', 'a': '對',
    'why': '[[標]] $-x$ 就是 $-1$ 個 $x$，所以係數是 $-1$。',
    'chk': ('coef', '-x', -1)},
   {'id': '1g', 't': 'mc', 'ask': '右邊的常數合併後是？', 'q': '$2×4-11$', 'a': '$-3$',
    'o': ['$3$', '$-19$', '$19$'],
    'why': '[[合]] 先乘後減：$8-11=-3$。',
    'chk': ('simp', '2×4-11')},
  ]},
 {'key': '合併解方程', 'short': '解方程', 'sec': '對應練習第 1、4 題',
  'steps': ['標', '合', '化'],
  'tips': ['① 含 $x$　② 常數', '化成 $ax=b$', '除以 $x$ 的係數'],
  'rule': '標 → 合 → 化：合併同類項化成 $ax=b$，再兩邊除以 $x$ 的係數。',
  'qs': [
   {'id': '2a', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$4x+3x=21$', 'a': '$3$',
    'o': ['$14$', '$147$', '$F(1,3)$'], 'mvd': '7x=21',
    'why': '[[合]] $7x=21$　[[化]] 兩邊除以 7：$x=3$。',
    'chk': ('solve', '4x+3x=21', 'x')},
   {'id': '2b', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$5x-2x=-12$', 'a': '$-4$',
    'o': ['$4$', '$-F(12,7)$', '$-9$'], 'mvd': '3x=-12',
    'why': '[[合]] $3x=-12$　[[化]] 兩邊除以 3：$x=-4$。',
    'chk': ('solve', '5x-2x=-12', 'x')},
   {'id': '2c', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$x-3x=8$', 'a': '$-4$',
    'o': ['$4$', '$-F(8,3)$', '$2$'], 'mvd': '-2x=8',
    'why': '[[合]] $-2x=8$　[[化]] 兩邊除以 $-2$：$x=-4$。除以係數，連負號一起除。',
    'chk': ('solve', 'x-3x=8', 'x')},
   {'id': '2d', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$6x-4x=-10$', 'a': '$-5$',
    'o': ['$5$', '$-1$', '$-8$'], 'mvd': '2x=-10',
    'why': '[[合]] $2x=-10$　[[化]] 兩邊除以 2：$x=-5$。',
    'chk': ('solve', '6x-4x=-10', 'x')},
   {'id': '2e', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$F(1,2)x+F(3,2)x=10$', 'a': '$5$',
    'o': ['$10$', '$20$', '$8$'], 'mvd': '2x=10',
    'why': '[[合]] $2x=10$　[[化]] 兩邊除以 2：$x=5$。',
    'chk': ('solve', 'F(1,2)x+F(3,2)x=10', 'x')},
   {'id': '2f', 't': 'mc', 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$F(x,3)+F(2x,3)=-4$', 'a': '$-4$',
    'o': ['$4$', '$-F(4,3)$', '$-12$'], 'mvd': 'x=-4',
    'why': '[[合]] $F(1,3)+F(2,3)=1$，左邊就是 $x$，所以 $x=-4$。',
    'chk': ('solve', 'F(x,3)+F(2x,3)=-4', 'x')},
   {'id': '2g', 't': 'mc', 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$-2x+0.5x=9$', 'a': '$-6$',
    'o': ['$6$', '$-3.6$', '$-13.5$'], 'mvd': '-1.5x=9',
    'why': '[[合]] $-1.5x=9$　[[化]] 兩邊除以 $-1.5$：$x=-6$。',
    'chk': ('solve', '-2x+0.5x=9', 'x')},
  ]},
 {'key': '找錯與應用', 'short': '找錯', 'sec': '對應練習第 2、4、5 題',
  'steps': ['設', '列', '合', '化'],
  'tips': ['設未知數', '各部分的和＝總量', '合併同類項', '除以 $x$ 的係數'],
  'rule': '找錯：合併時有沒有看漏符號？化的時候是不是「除以係數」？',
  'qs': [
   {'id': '3a', 't': 'yn', 'yl': TF, 'core': 1, 'ask': '這個解對不對？', 'q': '解 $-3x=12$，得 $x=4$。', 'a': '不對',
    'why': '[[化]] 兩邊除以 $-3$，不是除以 3：$x=-4$。',
    'chk': ('claim', '-3x=12', 4)},
   {'id': '3b', 't': 'yn', 'yl': TF, 'core': 1, 'ask': '這個解對不對？', 'q': '解 $F(1,3)x=6$，得 $x=2$。', 'a': '不對',
    'why': '[[化]] 係數是 $F(1,3)$，兩邊要乘 3：$x=18$。',
    'chk': ('claim', 'F(1,3)x=6', 2)},
   {'id': '3c', 't': 'yn', 'yl': TF, 'ask': '這個解對不對？', 'q': '解 $2x+x=9$，得 $x=3$。', 'a': '對',
    'why': '[[合]] $3x=9$　[[化]] $x=3$。',
    'chk': ('claim', '2x+x=9', 3)},
   {'id': '3d', 't': 'mc', 'long': 1, 'opts': LINES, 'ask': '哪一行出錯？',
    'q': '解 $x-6x+2x=4-19$<br>第 1 行　$x-6x+2x=-15$<br>第 2 行　$-3x=-15$<br>第 3 行　$x=-5$', 'a': '第 3 行',
    'why': '[[化]] 兩邊除以 $-3$，負數除以負數得正數：$x=5$。',
    'chk': ('wrong', 'x-6x+2x=4-19', ['x-6x+2x=-15', '-3x=-15', 'x=-5'])},
   {'id': '3e', 't': 'mc', 'long': 1, 'opts': LINES, 'ask': '哪一行出錯？',
    'q': '解 $3x-5x+x=2×4-11$<br>第 1 行　$-x=8-11$<br>第 2 行　$-x=-3$<br>第 3 行　$x=3$', 'a': '沒有錯',
    'why': '[[合]] $3-5+1=-1$，左邊是 $-x$。[[化]] 兩邊除以 $-1$：$x=3$。每一行都對。',
    'chk': ('wrong', '3x-5x+x=2×4-11', ['-x=8-11', '-x=-3', 'x=3'])},
   {'id': '3f', 't': 'mc', 'core': 1, 'long': 1, 'ask': '方程是哪一個？',
    'q': '小明、小華、小美共有郵票 120 張。小華的是小明的 2 倍，小美的是小明的 3 倍。設小明有 $x$ 張。',
    'a': '$x+2x+3x=120$', 'o': ['$x+2x+6x=120$', '$2x+3x=120$', '$x+(x+2)+(x+3)=120$'],
    'why': '[[設]] 小華 $2x$ 張，小美 $3x$ 張（都是和小明比）。[[列]] 三人加起來是 120：$x+2x+3x=120$。',
    'chk': ('tr', 'x+2x+3x=120', 20)},
   {'id': '3g', 't': 'mc', 'sub': 1, 'ask': '小明有多少張？（接上題）', 'q': '解 $x+2x+3x=120$', 'a': '$20$',
    'o': ['$24$', '$40$', '$720$'], 'mvd': '6x=120',
    'why': '[[合]] $6x=120$　[[化]] $x=20$。檢：$20+40+60=120$。',
    'chk': ('solve', 'x+2x+3x=120', 'x')},
  ]},
]


# ---------------------------------------------------------------- 驗算
def E(s):
    s = s.replace('^', '**').replace('×', '*').replace('÷', '/')
    s = re.sub(r'F\(([^,()]+),([^()]+)\)', r'((\1)/(\2))', s)
    s = re.sub(r'(\d)([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z)])([a-z(])', r'\1*\2', s)
    return sp.sympify(s, locals=NS, rational=True)


def EQ(s):
    l, r = s.split('=')
    return E(l), E(r)


def strip(t):
    return t.replace('$', '')


def sols(s, v=x):
    l, r = EQ(s)
    return set(sp.solve(sp.Eq(l, r), v))


def same(s1, s2, v=x):
    """兩條方程同解（一元一次方程同解＝等價）。"""
    return sols(s1, v) == sols(s2, v)


def verify():
    rows, bad = [], []
    for L in LEVELS:
        for Q in L['qs']:
            k, ok, note = Q['chk'], False, ''
            if k[0] == 'mv':            # 移項：答案與原方程同解，三個干擾項都不同解
                s0 = sols(k[1])
                ds = [sols(strip(o)) for o in Q['o']]
                ok = sols(strip(Q['a'])) == s0 and all(d != s0 for d in ds)
                note = f'原方程解 x={",".join(map(sp.sstr, s0))}；干擾項解 ' + '、'.join(
                    ','.join(map(sp.sstr, d)) or '無' for d in ds)
            elif k[0] == 'tfmv':        # 這樣移項對不對：同解＝對
                truth = same(k[1], k[2])
                ok = (Q['a'] == '對') == truth
                note = f'{k[1]} 解 {sols(k[1])}；{k[2]} 解 {sols(k[2])}'
            elif k[0] == 'prop1':       # 兩邊加 c 的結果＝移項結果
                l, r = EQ(k[1])
                ok = sp.simplify(l + k[2] - x) == 0 and Q['a'] == '對'
                note = f'{k[1]} 兩邊加 {k[2]}：左 {sp.simplify(l + k[2])}，右 {sp.simplify(r + k[2])}，與移項結果 x=3+5 相同'
            elif k[0] == 'solve':       # 解方程：答案＝解；移項後式子同解；干擾項都不是解
                v = NS[k[2]]
                s0 = sols(k[1], v)
                ans = E(strip(Q['a']))
                ds = [E(strip(o)) for o in Q['o']]
                ok = s0 == {ans} and all(d != ans for d in ds)
                if Q.get('mvd'):
                    ok = ok and same(k[1], Q['mvd'], v)
                    note = f'移項後 {Q["mvd"]} 同解；'
                note += f'{k[2]}={sp.sstr(ans)}；干擾項 ' + '、'.join(sp.sstr(d) for d in ds)
            elif k[0] == 'wrong':       # 哪一行出錯：第一條與原方程不同解的行
                s0 = sols(k[1])
                first = next((i for i, ln in enumerate(k[2]) if sols(ln) != s0), None)
                exp = LINES[first] if first is not None else '沒有錯'
                ok = Q['a'] == exp
                note = f'原方程解 {s0}；各行解 ' + '、'.join(sp.sstr(sols(ln)) for ln in k[2]) + f'→ {exp}'
            elif k[0] == 'tr':          # 列方程：答案的解合理，干擾項都不同解
                want = sp.Integer(k[2])
                ok = sols(strip(Q['a'])) == {want} and EQ(strip(Q['a'])) == EQ(k[1])
                ds = [sols(strip(o)) for o in Q['o']]
                if any(d == {want} for d in ds):
                    ok = False; note = '干擾項與答案同解！'
                note = note or f'答案解 x={want}（題意合理）；干擾項解 ' + '、'.join(
                    ','.join(sp.sstr(v) for v in d) or '無' for d in ds)
            elif k[0] == 'param':
                l, r = EQ(k[1])
                s_ = sp.solve(sp.Eq(l.subs(x, k[2]), r.subs(x, k[2])), NS[k[3]])
                ok = s_ == [E(strip(Q['a']))] and all(E(strip(o)) != s_[0] for o in Q['o'])
                note = f'代入 x={k[2]} 得 {k[3]}={s_}'
            elif k[0] == 'simp':        # 合併：答案恆等於原式，干擾項都不恆等
                want = E(k[1])
                ok = sp.simplify(E(strip(Q['a'])) - want) == 0 and all(
                    sp.simplify(E(strip(o)) - want) != 0 for o in Q['o'])
                note = f'{k[1]} ＝ {sp.sstr(want)}；干擾項 ' + '、'.join(sp.sstr(E(strip(o))) for o in Q['o'])
            elif k[0] == 'coef':
                c = E(k[1]).coeff(x)
                ok = (c == k[2]) == (Q['a'] == '對')
                note = f'{k[1]} 的係數 {c}'
            elif k[0] == 'claim':       # 「解……得 x=…」對不對
                s0 = sols(k[1])
                ok = (s0 == {sp.Integer(k[2])}) == (Q['a'] == '對')
                note = f'{k[1]} 解 {s0}；題目聲稱 {k[2]}'
            if Q['t'] == 'mc' and 'o' in Q and (Q['a'] in Q['o'] or len(set(Q['o'])) != len(Q['o'])):
                ok = False; note += '；選項重複'
            if 'opts' in Q and Q['a'] not in Q['opts']:
                ok = False; note += '；答案不在選項內'
            rows.append((Q['num'], Q['id'], '★' if Q.get('core') else '',
                         strip(Q.get('ask', '')) + ' ' + strip(Q['q']).replace('<br>', '／'),
                         strip(Q['a']), note, 'PASS' if ok else 'FAIL'))
            if not ok:
                bad.append(Q['id'])
    return rows, bad


# ---------------------------------------------------------------- 定死選項次序與題號
def finalize():
    n = 0
    pos_count = [0, 0, 0, 0]
    for L in LEVELS:
        for Q in L['qs']:
            n += 1
            Q['num'] = n
            if Q['t'] == 'yn':
                Q['opts'] = Q['yl']
            elif 'opts' in Q:
                pos_count[Q['opts'].index(Q['a'])] += 1
            else:
                p = (n + len(Q['id'])) % 4
                while pos_count[p] > min(pos_count):
                    p = (p + 1) % 4
                pos_count[p] += 1
                rest = Q['o'][:]
                random.Random(Q['id']).shuffle(rest)
                Q['opts'] = rest[:p] + [Q['a']] + rest[p:]
    return pos_count


# ---------------------------------------------------------------- 注入 HTML
GAMES = ['互動遊戲_5.2-1_合併同類項大挑戰_投影版.html']


def inject():
    keep = ('id', 'num', 't', 'core', 'ask', 'q', 'a', 'opts', 'why', 'long')
    data = [{k: v for k, v in L.items() if k != 'qs'} | {'qs': [{k: Q[k] for k in keep if k in Q} for Q in L['qs']]}
            for L in LEVELS]
    js = json.dumps(data, ensure_ascii=False, indent=1)
    for f in GAMES:
        p = HERE / f
        t = p.read_text(encoding='utf-8')
        t2, k = re.subn(r'/\*BANK\*/.*?/\*END\*/', lambda _: '/*BANK*/' + js + '/*END*/', t, flags=re.S)
        assert k == 1, f
        p.write_text(t2, encoding='utf-8')
        print('注入', f)


# ---------------------------------------------------------------- 講義紀錄表（docx）
def D(t):
    """$…$ → OMML 標記 {…}；F(p,q) → frac(p,q)；× → *。"""
    def conv(mo):
        e = mo.group(1).replace('×', '*')
        e = re.sub(r'F\(([^,()]+),([^()]+)\)', r'frac(\1,\2)', e)
        return '{' + e + '}'
    t = re.sub(r'\$(.+?)\$', conv, t)
    return re.sub(r'\[\[(.+?)\]\]', r'【\1】', t)


def build_sheet():
    sys.path.insert(0, str(HERE))
    from ch5_common import (para, heading, masthead, student_info_row, pbox, grid, tight, contrast, card,
                            eq_row, span_row, shaded_box, answers, notes, build_docx, W, GREY_FILL, _tbl, GAP, nm,
                            FOOT, SUBJ, keep_together, worked_example_table, figx, bal, MediaRegistry)

    def sol(rows, why_pct=0.34):          # 同 build_ch5.py 的 sol()
        return keep_together(tight(worked_example_table(rows, why_pct=why_pct), line=260, after=0))

    M = MediaRegistry()
    P = [masthead(SUBJ, '5.2 解一元一次方程（第 1 課時）合併同類項', '講義＋遊戲紀錄表'), student_info_row()]
    P += [shaded_box('今日玩法：老師講完簡報後，全班玩「合併同類項大挑戰」。第 1–2 頁是講義，玩的時候可以翻看；'
                     '第 3–4 頁是紀錄表，每一題都要圈答案。')]
    # ---- 講義（精簡自 講義練習_5.2-1 的「新概念」與「範例」段）
    P += [heading('一、兩個新步驟'),
          pbox([para('合併同類項', bold=True),
                para('把方程同一邊的同類項合併，把方程化成 {ax=b} 的形式。')]),
          pbox([para('係數化為 1', bold=True),
                para('方程 {ax=b}（{a!=0}）兩邊除以 {a}，得 {x=frac(b,a)}。')]),
          grid([('原方程', '合併後', '解'),
                ('{2x+5x=14}', '{7x=14}', '{x=2}'),
                ('{x-4x=9}', '{-3x=9}', '{x=-3}')],
               [3400, 3400, W - 6800])]
    P += [heading('二、合併同類項解方程三步'),
          card('合併同類項解方程三步',
               [('標：用 ① 標含 {x} 的項，② 標常數項', '符號跟著後面的項，一起標'),
                ('合：合併同類項，化成 {ax=b}', '係數相加，{x} 照抄'),
                ('化：兩邊除以 {x} 的係數', '係數是負數，答案的符號要小心')],
               trigger='方程的一邊有幾個同類項的時候')]
    P += [heading('三、範例'),
          shaded_box('某校三年共種樹 360 棵。第二年種的是第一年的 2 倍，第三年種的是第二年的 3 倍。'
                     '第一年種了多少棵？', kind='worked', keep_next=True),
          sol([span_row('設第一年種了 {x} 棵，則第二年種 {2x} 棵，第三年種 {6x} 棵。', '設'),
               span_row('第一年＋第二年＋第三年＝360', '各部分的和＝總量'),
               eq_row('{x+2x+6x}', '{360}', '列方程'),
               eq_row('{9x}', '{360}', '合'),
               eq_row('{x}', '{40}', '化：兩邊除以 9'),
               span_row('答：第一年種了 40 棵。', None)]),
          shaded_box('解方程 {frac(3,2)x-4x=7-12}。', kind='worked', keep_next=True),
          sol([span_row(nm('{frac(3,2)x}① {-4x}① ＝ 7② {-12}②'), '標'),
               eq_row('{-frac(5,2)x}', '{-5}', '合'),
               eq_row('{x}', '{2}', '化：兩邊乘 {-frac(2,5)}')]),
          shaded_box('提醒：係數化為 1 是「除以係數」。{-frac(1,2)x=4} 要兩邊乘 {-2}，得 {x=-8}，不是 {x=-2}。'),
          GAP,
          shaded_box('我們做：天平上每個灰色盒子重 {x} g，解方程 {3x+x=20}。', kind='worked', keep_next=True),
          pbox([figx(M, bal(['x', 'x', 'x', 'x'], ['20']), 'G521_w', 8.0),
                para('合併：＿＿＿＿ {x=20}　　化：{x=} ＿＿＿＿')], last=True)]
    # ---- 紀錄表
    P += [heading('四、遊戲紀錄表', page_break_before=True),
          tight(para('先圈答案；揭曉後答對打 ✔，答錯在「改正」欄寫正確答案。5 分鐘版只做 ★ 題。'
                     '第 2 關先寫「合併後」。', sz=22), line=300, after=20),
          tight(para(f'我的成績：答對 ＿＿＿ ／ {sum(len(L["qs"]) for L in LEVELS)} 題'
                     f'（5 分鐘版：答對 ＿＿＿ ／ {sum(1 for L in LEVELS for Q in L["qs"] if Q.get("core"))} 題）',
                     bold=True, sz=22), line=300, after=60)]
    w = [700, 6950, 1800, 480]
    w.append(W - sum(w))
    vis = lambda o: sum(2 if '一' <= c <= '鿿' else 1 for c in re.sub(r'[$]|F\(|[(),]', '', o))
    for li, L in enumerate(LEVELS):
        rows = [{'hdr': True, 'cells': [{'p': [tight(para(f'第 {li + 1} 關　{L["key"]}　（{" → ".join(L["steps"])}）',
                                                         bold=True, sz=23))], 'shd': GREY_FILL, 'span': 5}]},
                {'hdr': True, 'cells': [{'p': [tight(para(h, bold=True, sz=21, jc='center'))], 'shd': GREY_FILL}
                                        for h in ('題號', '題目', '圈答案', '✔', '改正')]}]
        for Q in L['qs']:
            parts = Q['q'].split('<br>')
            head = (D(Q['ask']) + '　') if Q.get('ask') else ''
            qp = [tight(para(nm(head + D(parts[0])), sz=22), line=270, after=10)]
            sub_done = False
            if Q.get('opts') == LINES:
                # 找錯題：三行算式直接配 ①②③，④＝沒有錯（與投影版「第 1 行…沒有錯」次序一致）
                cells = [f'{CIRC[i]} {D(re.sub(r"^第 \d 行　", "", p_))}' for i, p_ in enumerate(parts[1:])]
                cells.append(f'{CIRC[3]} 沒有錯')
                qp += [tight(para(nm('　　'.join(cells[:2])), sz=22), line=270, after=0),
                       tight(para(nm('　　'.join(cells[2:])), sz=22), line=270, after=0)]
                mine = ' '.join(CIRC)
            elif Q['t'] == 'mc':
                qp += [tight(para(nm('　　' + D(p_)), sz=22), line=270, after=0) for p_ in parts[1:]]
                ops = [f'{CIRC[i]} {D(o)}' for i, o in enumerate(Q['opts'])]
                tot = sum(vis(o) for o in Q['opts'])
                if Q.get('sub') and vis(Q.get('ask', '') + parts[0]) + tot <= 30:
                    # 短題：選項接在題目同一行，「合併後」獨佔一整行（夠位寫 合併後的方程）
                    qp[0] = tight(para(nm(head + D(parts[0]) + '　　' + '　'.join(ops)), sz=22), line=270, after=10)
                    lines = ['合併後：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿']
                    sub_done = True
                elif Q.get('sub') and tot <= 14:        # 題目長、選項短：合併後格放在選項同一行
                    lines = ['　　'.join(ops) + '　　合併後：＿＿＿＿＿＿＿']
                    sub_done = True
                elif tot <= 18:
                    lines = ['　　'.join(ops)]
                else:
                    lines = ['　　'.join(ops[:2]), '　　'.join(ops[2:])]
                qp += [tight(para(nm(ln), sz=22), line=270, after=0) for ln in lines]
                mine = ' '.join(CIRC[:len(Q['opts'])])
            else:
                mine = '　'.join(Q['opts'])
            if Q.get('sub') and not sub_done:
                qp.append(tight(para('合併後：＿＿＿＿＿＿＿＿＿＿＿＿＿＿', sz=22), line=320, after=0))
            star = '★' if Q.get('core') else ''
            rows.append({'cells': [
                [tight(para(f'{Q["num"]}{star}', bold=True, sz=22, jc='center'))],
                qp,
                [tight(para(mine, sz=24, jc='center', bold=True))],
                [tight(para('', sz=22))],
                [tight(para('', sz=22))]], 'h': 0})
        P += [_tbl(rows, w, trailing_blank=False)] + ([tight(para('', sz=10), line=160, after=0)] if li < len(LEVELS) - 1 else [])
    # ---- 教師頁
    ans = []
    for li, L in enumerate(LEVELS):
        parts = []
        for Q in L['qs']:
            if Q['t'] == 'mc':
                parts.append(f'{Q["num"]}．{CIRC[Q["opts"].index(Q["a"])]} {D(Q["a"])}')
            else:
                parts.append(f'{Q["num"]}．{Q["a"]}')
        ans.append(f'第 {li + 1} 關（{L["key"]}）：' + '　'.join(parts))
    ans.append('合併後：' + '　'.join(f'{Q["num"]}．{D("$" + Q["mvd"] + "$")}'
                                     for L in LEVELS for Q in L['qs'] if Q.get('mvd')))
    ans += ['投影版按 Space 揭曉／下一題，數字鍵 1–4 為該隊加 10 分，Shift＋數字扣 10 分，← 回上一題。',
            '講義「我們做」答案：{4x=20}，{x=5}。',
            '題目來源：講義練習_5.2-1 的重溫與練習第 1–5 題改寫（另加係數概念、右邊常數、「沒有錯」找錯題）；'
            '第 6–9 題未放入遊戲，可作挑戰題。逐題 sympy 驗算見 驗算_第五章_一元一次方程.md 文末。']
    P += answers(ans)
    P += notes('D2 手順卡', ('D11 標記對應法', 'D10 具體等量模型（天平）'),
               '沿用本課講義已定的設計：簡報講完「我做／我們做」後，用遊戲做「你做」。'
               '按「合併同類項 → 合併解方程 → 找錯與應用」三關闖關；紀錄表第 2 關每題先寫合併後的方程，'
               '教師課後收回，可看出學生錯在「合」還是「化」。',
               '手順卡：講義全卡 → 遊戲每題頂部重現步驟字卡 → 答錯時解說用同一組字卡。'
               '紀錄表「合併後」格：第 2 關全部提供 → 第 3 關只在解方程的題目提供。'
               '天平：只在講義「我們做」出現一次。',
               'A—2—3　掌握一元一次方程的一般解法，能解數字係數的一元一次方程；'
               'A—2—4　能根據具體問題情境中的等量關係，列出一元一次方程，解決簡單的問題',
               '課本 p.120–121（PDF 第 127–128 頁）',
               '只出投影版：學生舉手指作答、紀錄表圈號碼，分隊加分。5 分鐘版只做 ★ 題。')
    out = HERE / '講義紀錄表_5.2-1_合併同類項_遊戲版.docx'
    print(build_docx(P, str(out), footer_text=FOOT, media=M))


if __name__ == '__main__':
    pos = finalize()
    rows, bad = verify()
    print('| # | id | 5 分鐘版 | 題目 | 答案 | 驗算 | 結果 |\n|---|---|---|---|---|---|---|')
    for r in rows:
        print('| ' + ' | '.join(str(c) for c in r) + ' |')
    n = len(rows)
    print(f'\n共 {n} 題；5 分鐘版 {sum(1 for r in rows if r[2])} 題；四選一答案位置分佈 ①②③④＝{pos}；FAIL：{bad or "無"}')
    if bad:
        sys.exit(1)
    if '--inject' in sys.argv:
        inject()
        build_sheet()
