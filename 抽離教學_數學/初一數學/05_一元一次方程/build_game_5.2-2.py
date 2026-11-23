# -*- coding: utf-8 -*-
"""build_game_5.2-2.py — 初一 5.2-2〈移項〉課堂互動遊戲（投影版）＋講義紀錄表。

題庫只在這裡改一次（由 講義練習_5.2-2_移項_融合版 的練習第 1–9 題改寫成選擇／是非題）。
執行：
  python build_game_5.2-2.py            只驗算（sympy），驗算表印到 stdout
  python build_game_5.2-2.py --inject   驗算通過後：題庫注入投影版 HTML，並出講義紀錄表 docx
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
# mvd：移項後的式子（紀錄表「移項後：」格的答案，教師頁列出）
# chk：驗算方式，見 verify()
# ---------------------------------------------------------------------
TF = ['對', '不對']
LINES = ['第 1 行', '第 2 行', '第 3 行', '沒有錯']
LEVELS = [
 {'key': '移項要變號', 'short': '變號', 'sec': '對應練習第 1、9 題',
  'steps': ['找', '移', '變號', '不動'],
  'tips': ['找出要移的項', '把它移過等號', '＋變−，−變＋', '沒移的項不變號'],
  'rule': '移項：把方程一邊的某一項變號後，移到另一邊。移項的依據是等式的性質 1。',
  'qs': [
   {'id': '1a', 't': 'mc', 'core': 1, 'ask': '移項後是哪一個？', 'q': '$x+7=10$', 'a': '$x=10-7$',
    'o': ['$x=10+7$', '$x=7-10$', '$x=-10-7$'],
    'why': '[[找]] 左邊的 $+7$ 要移到右邊。[[變號]] $+7$ 變 $-7$，所以 $x=10-7$。',
    'chk': ('mv', 'x+7=10')},
   {'id': '1b', 't': 'mc', 'core': 1, 'ask': '移項後是哪一個？', 'q': '$5x=3x-8$', 'a': '$5x-3x=-8$',
    'o': ['$5x+3x=-8$', '$5x-3x=8$', '$5x+3x=8$'],
    'why': '[[找]] 右邊的 $3x$ 要移到左邊。[[變號]] $3x$ 變 $-3x$。[[不動]] $-8$ 沒有移動，不變號。',
    'chk': ('mv', '5x=3x-8')},
   {'id': '1c', 't': 'mc', 'core': 1, 'ask': '移項後是哪一個？', 'q': '$2x-5=x+1$', 'a': '$2x-x=1+5$',
    'o': ['$2x-x=1-5$', '$2x+x=1+5$', '$2x+x=1-5$'],
    'why': '[[移]] $x$ 由右邊移到左邊，[[變號]] 變 $-x$；$-5$ 由左邊移到右邊，變 $+5$。',
    'chk': ('mv', '2x-5=x+1')},
   {'id': '1d', 't': 'mc', 'ask': '移項後是哪一個？', 'q': '$-x+4=2x$', 'a': '$-x-2x=-4$',
    'o': ['$-x+2x=-4$', '$-x-2x=4$', '$-x+2x=4$'],
    'why': '[[移]] $2x$ 移到左邊變 $-2x$；$+4$ 移到右邊變 $-4$。[[不動]] $-x$ 沒有移動，不變號。',
    'chk': ('mv', '-x+4=2x')},
   {'id': '1e', 't': 'yn', 'yl': TF, 'core': 1, 'ask': '這樣移項對不對？', 'q': '由 $x-6=1$ 得 $x=1-6$', 'a': '不對',
    'why': '[[變號]] $-6$ 移到右邊，要變成 $+6$。正確：$x=1+6$，$x=7$。',
    'chk': ('tfmv', 'x-6=1', 'x=1-6')},
   {'id': '1f', 't': 'yn', 'yl': TF, 'ask': '這樣移項對不對？', 'q': '由 $3x=2x+4$ 得 $3x-2x=4$', 'a': '對',
    'why': '[[移]] $2x$ 由右邊移到左邊，[[變號]] 變成 $-2x$。[[不動]] $4$ 沒有移動，不變號。',
    'chk': ('tfmv', '3x=2x+4', '3x-2x=4')},
   {'id': '1g', 't': 'yn', 'yl': TF, 'ask': '這句話對不對？', 'q': '移項的依據是等式的性質 1。', 'a': '對',
    'why': '$x-5=3$ 兩邊都加 5，得 $x=3+5$。結果和「把 $-5$ 移到右邊，變 $+5$」一樣。',
    'chk': ('prop1', 'x-5=3', 5)},
  ]},
 {'key': '移項解方程', 'short': '解方程', 'sec': '對應練習第 2、4 題',
  'steps': ['標', '移', '合', '化'],
  'tips': ['① 含 $x$　② 常數', '移過等號要變號', '合併同類項', '除以 $x$ 的係數'],
  'rule': '① 含 $x$ 的項去左邊，② 常數項去右邊。移過等號要變號；沒有移動的項不變號。',
  'qs': [
   {'id': '2a', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$3x+2=11$', 'a': '$3$',
    'o': ['$F(13,3)$', '$-3$', '$9$'], 'mvd': '3x=11-2',
    'why': '[[移]] $3x=11-2$　[[合]] $3x=9$　[[化]] 兩邊除以 3：$x=3$。',
    'chk': ('solve', '3x+2=11', 'x')},
   {'id': '2b', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$6x=4x-10$', 'a': '$-5$',
    'o': ['$5$', '$-1$', '$-10$'], 'mvd': '6x-4x=-10',
    'why': '[[移]] $6x-4x=-10$　[[合]] $2x=-10$　[[化]] 兩邊除以 2：$x=-5$。',
    'chk': ('solve', '6x=4x-10', 'x')},
   {'id': '2c', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$7x-2=4x+10$', 'a': '$4$',
    'o': ['$F(8,3)$', '$12$', '$-4$'], 'mvd': '7x-4x=10+2',
    'why': '[[移]] $7x-4x=10+2$（$-2$ 移過去變 $+2$）　[[合]] $3x=12$　[[化]] $x=4$。',
    'chk': ('solve', '7x-2=4x+10', 'x')},
   {'id': '2d', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$2x=5x+9$', 'a': '$-3$',
    'o': ['$3$', '$9$', '$-F(1,3)$'], 'mvd': '2x-5x=9',
    'why': '[[移]] $2x-5x=9$　[[合]] $-3x=9$　[[化]] 兩邊除以 $-3$：$x=-3$。除以係數，連負號一起除。',
    'chk': ('solve', '2x=5x+9', 'x')},
   {'id': '2e', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$y$ ＝ ？', 'q': '$8y-3=5y+12$', 'a': '$5$',
    'o': ['$3$', '$15$', '$-5$'], 'mvd': '8y-5y=12+3',
    'why': '[[移]] $8y-5y=12+3$　[[合]] $3y=15$　[[化]] $y=5$。',
    'chk': ('solve', '8y-3=5y+12', 'y')},
   {'id': '2f', 't': 'mc', 'sub': 1, 'ask': '$y$ ＝ ？', 'q': '$F(1,3)y-2=F(2,3)y$', 'a': '$-6$',
    'o': ['$6$', '$-F(2,3)$', '$-2$'], 'mvd': 'F(1,3)y-F(2,3)y=2',
    'why': '[[移]] $F(1,3)y-F(2,3)y=2$　[[合]] $-F(1,3)y=2$　[[化]] 兩邊乘 $-3$：$y=-6$。',
    'chk': ('solve', 'F(1,3)y-2=F(2,3)y', 'y')},
   {'id': '2g', 't': 'mc', 'sub': 1, 'ask': '$x$ ＝ ？', 'q': '$0.6x+3=0.2x+5$', 'a': '$5$',
    'o': ['$20$', '$2.5$', '$0.8$'], 'mvd': '0.6x-0.2x=5-3',
    'why': '[[移]] $0.6x-0.2x=5-3$　[[合]] $0.4x=2$　[[化]] 兩邊除以 0.4：$x=5$。',
    'chk': ('solve', '0.6x+3=0.2x+5', 'x')},
  ]},
 {'key': '找錯與應用', 'short': '找錯', 'sec': '對應練習第 3、5–8 題',
  'steps': ['設', '列', '移', '化'],
  'tips': ['設未知數', '找相等關係', '移過等號要變號', '求出答案'],
  'rule': '找錯：逐行檢查——移過等號的項有沒有變號？沒有移動的項有沒有亂變號？',
  'qs': [
   {'id': '3a', 't': 'mc', 'core': 1, 'long': 1, 'opts': LINES, 'ask': '哪一行出錯？',
    'q': '解 $4x+3=2x-5$<br>第 1 行　$4x+2x=-5-3$<br>第 2 行　$6x=-8$<br>第 3 行　$x=-F(4,3)$', 'a': '第 1 行',
    'why': '[[移]] $2x$ 移到左邊，要變 $-2x$。正確：$4x-2x=-5-3$，$x=-4$。',
    'chk': ('wrong', '4x+3=2x-5', ['4x+2x=-5-3', '6x=-8', 'x=-F(4,3)'])},
   {'id': '3b', 't': 'mc', 'long': 1, 'opts': LINES, 'ask': '哪一行出錯？',
    'q': '解 $-3x+5=x-7$<br>第 1 行　$-3x-x=-7-5$<br>第 2 行　$-4x=-12$<br>第 3 行　$x=3$', 'a': '沒有錯',
    'why': '[[移]] $x$ 移到左邊變 $-x$，$+5$ 移到右邊變 $-5$；$-3x$ 沒有移動，不變號。'
           '[[化]] $-12÷(-4)=3$。每一行都對。',
    'chk': ('wrong', '-3x+5=x-7', ['-3x-x=-7-5', '-4x=-12', 'x=3'])},
   {'id': '3c', 't': 'mc', 'core': 1, 'sub': 1, 'ask': '$x$ ＝ ？',
    'q': '$x$ 取什麼值時，$3x+5$ 與 $x-7$ 的值相等？', 'a': '$-6$',
    'o': ['$6$', '$-3$', '$-1$'], 'mvd': '3x-x=-7-5',
    'why': '[[列]] $3x+5=x-7$　[[移]] $3x-x=-7-5$　[[化]] $2x=-12$，$x=-6$。',
    'chk': ('solve', '3x+5=x-7', 'x')},
   {'id': '3d', 't': 'mc', 'ask': '$a$ ＝ ？', 'q': '已知 $x=2$ 是方程 $2x+a=5x-2a$ 的解。', 'a': '$2$',
    'o': ['$6$', '$-2$', '$3$'],
    'why': '代入 $x=2$：$4+a=10-2a$。[[移]] $a+2a=10-4$　[[化]] $3a=6$，$a=2$。',
    'chk': ('param', '2x+a=5x-2a', 2, 'a')},
   {'id': '3e', 't': 'mc', 'core': 1, 'long': 1, 'ask': '方程是哪一個？',
    'q': '小明出生時，爸爸 30 歲。現在爸爸的年齡是小明的 4 倍。設小明現在 $x$ 歲。', 'a': '$x+30=4x$',
    'o': ['$4x+30=x$', '$x=4(x+30)$', '$x-30=4x$'],
    'why': '[[設]] 小明 $x$ 歲；爸爸比他大 30 歲，是 $(x+30)$ 歲。[[列]] 爸爸是小明的 4 倍：$x+30=4x$。',
    'chk': ('tr', 'x+30=4x', 10)},
   {'id': '3f', 't': 'mc', 'sub': 1, 'ask': '小明現在幾歲？（接上題）', 'q': '解 $x+30=4x$', 'a': '$10$',
    'o': ['$-10$', '$6$', '$30$'], 'mvd': 'x-4x=-30',
    'why': '[[移]] $x-4x=-30$　[[化]] $-3x=-30$，$x=10$。小明 10 歲，爸爸 40 歲，正好是 4 倍。',
    'chk': ('solve', 'x+30=4x', 'x')},
   {'id': '3g', 't': 'mc', 'core': 1, 'long': 1, 'ask': '方程是哪一個？',
    'q': '甲每小時摘蘋果 9 kg，乙每小時摘 7 kg。摘完後，甲把 3 kg 給乙，兩人的蘋果就一樣多。設摘了 $x$ 小時。',
    'a': '$9x-3=7x+3$', 'o': ['$9x+3=7x-3$', '$9x-3=7x$', '$9x=7x+3$'],
    'why': '[[設]] 甲 $9x$ kg，乙 $7x$ kg。甲給乙 3 kg 後：甲 $(9x-3)$，乙 $(7x+3)$。'
           '[[列]] 一樣多：$9x-3=7x+3$。解得 $x=3$，摘了 3 小時。',
    'chk': ('tr', '9x-3=7x+3', 3)},
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
GAMES = ['互動遊戲_5.2-2_移項大挑戰_投影版.html']


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
                            FOOT, SUBJ, keep_together, worked_example_table)

    def sol(rows, why_pct=0.34):          # 同 build_ch5.py 的 sol()
        return keep_together(worked_example_table(rows, why_pct=why_pct))

    P = [masthead(SUBJ, '5.2 解一元一次方程（第 2 課時）移項', '講義＋遊戲紀錄表'), student_info_row()]
    P += [shaded_box('今日玩法：老師講完簡報後，全班玩「移項大挑戰」。第 1–2 頁是講義，玩的時候可以翻看；'
                     '第 3–4 頁是紀錄表，每一題都要圈答案。')]
    # ---- 講義（精簡自 講義練習_5.2-2 的「新概念」與「範例」段）
    P += [heading('一、什麼是移項'),
          pbox([para('移項', bold=True),
                para('把方程一邊的某一項變號後，移到另一邊。'),
                para('移項的依據是等式的性質 1。')]),
          grid([('原方程', '移項後', '哪一項移了？怎樣變？'),
                ('{x+5=9}', '{x=9-5}', '左邊 {+5} 移到右邊，變 {-5}'),
                ('{3x=2x+4}', '{3x-2x=4}', '右邊 {2x} 移到左邊，變 {-2x}'),
                ('{x-6=1}', '{x=1+6}', '左邊 {-6} 移到右邊，變 {+6}')],
               [2600, 2600, W - 5200])]
    P += [heading('二、移項解方程四步'),
          card('移項解方程四步',
               [('標：① 標含 {x} 的項，② 標常數項', '① 要去左邊，② 要去右邊'),
                ('移：在錯的一邊的項，移過等號', '移過等號要變號：＋變−，−變＋'),
                ('合：合併同類項', '沒有移動的項不變號'),
                ('化：兩邊除以 {x} 的係數', '除以係數，連符號一起除')],
               trigger='方程兩邊都有含 {x} 的項或常數項的時候',
               fading='講義全卡 → 遊戲每題重現四步字卡 → 紀錄表第 2 關自己寫「移項後」的式子')]
    P += [heading('三、範例'),
          shaded_box('解方程 {x-4=frac(3,2)x+2}。', kind='worked', keep_next=True),
          sol([span_row(nm('{x}① {-4}② ＝ {frac(3,2)x}① {+2}②'), '標'),
               eq_row('{x-frac(3,2)x}', '{2+4}', '移：{-4} 變 {+4}；{frac(3,2)x} 變 {-frac(3,2)x}'),
               eq_row('{-frac(1,2)x}', '{6}', '合'),
               eq_row('{x}', '{-12}', '化：兩邊乘 {-2}')]),
          para('最常見的一個錯：解 {5x-3=2x+9}', bold=True, keep_next=True),
          contrast([('{5x-2x=9-3}', '{5x-2x=9+3}'), ('{3x=6}', '{3x=12}'), ('{x=2}', '{x=4}')],
                   '{-3} 由左邊移到右邊，要變成 {+3}；只要移過等號，就一定要變號。')]

    # ---- 紀錄表
    P += [heading('四、遊戲紀錄表', page_break_before=True),
          tight(para('先圈答案；揭曉後答對打 ✔，答錯在「改正」欄寫正確答案。5 分鐘版只做 ★ 題。'
                     '第 2 關先寫「移項後」。', sz=22), line=300, after=20),
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
                    # 短題：選項接在題目同一行，「移項後」獨佔一整行（夠位寫 7x−4x=10+2）
                    qp[0] = tight(para(nm(head + D(parts[0]) + '　　' + '　'.join(ops)), sz=22), line=270, after=10)
                    lines = ['移項後：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿']
                    sub_done = True
                elif Q.get('sub') and tot <= 14:        # 題目長、選項短：移項後格放在選項同一行
                    lines = ['　　'.join(ops) + '　　移項後：＿＿＿＿＿＿＿']
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
                qp.append(tight(para('移項後：＿＿＿＿＿＿＿＿＿＿＿＿＿＿', sz=22), line=320, after=0))
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
    ans.append('移項後：' + '　'.join(f'{Q["num"]}．{D("$" + Q["mvd"] + "$")}'
                                     for L in LEVELS for Q in L['qs'] if Q.get('mvd')))
    ans += ['投影版按 Space 揭曉／下一題，數字鍵 1–4 為該隊加 10 分，Shift＋數字扣 10 分，← 回上一題。',
            '題目來源：講義練習_5.2-2 練習第 1–9 題改寫（第 9 題「用等式的性質說明移項」改為第 7 題是非題；'
            '另加第 16 題「沒有錯」的找錯題）；逐題 sympy 驗算見 驗算_第五章_一元一次方程.md 文末。']
    P += answers(ans)
    P += notes('D2 手順卡', ('D11 標記對應法', 'D14 錯誤分析對比'),
               '學生不喜歡做紙本練習（5.1-1 起改用遊戲），本課沿用講義已定的設計：'
               '簡報講完「我做／我們做」後，用遊戲做「你做」。練習第 1–9 題原意保留，改寫成選擇／是非題，'
               '按「移項要變號 → 移項解方程 → 找錯與應用」三關闖關；紀錄表第 2 關每題先寫移項後的式子，'
               '教師課後收回，可看出學生錯在「移」還是「化」。',
               '手順卡：講義全卡 → 遊戲每題頂部重現「標→移→合→化」字卡 → 答錯時解說用同一組字卡。'
               '紀錄表「移項後」格：第 2 關全部提供 → 第 3 關只在解方程的題目提供，列方程題不提供。'
               '正誤對比：講義雙欄 → 遊戲第 15、16 題逐行找錯（其中一題「沒有錯」，防止學生見題就說錯）。',
               'A—2—3　掌握一元一次方程的一般解法，能解數字係數的一元一次方程；'
               'A—2—4　能根據具體問題情境中的等量關係，列出一元一次方程，解決簡單的問題',
               '課本 p.122–124（PDF 第 129–131 頁）',
               '只出投影版：學生舉手指作答、紀錄表圈號碼，分隊加分。5 分鐘版 13 題（★），完整版 21 題。')
    out = HERE / '講義紀錄表_5.2-2_移項_遊戲版.docx'
    print(build_docx(P, str(out), footer_text=FOOT))


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
