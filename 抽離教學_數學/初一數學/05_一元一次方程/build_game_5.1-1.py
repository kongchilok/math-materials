# -*- coding: utf-8 -*-
"""build_game_5.1-1.py — 初一 5.1-1〈方程與方程的解〉課堂互動遊戲＋講義紀錄表。

題庫只在這裡改一次（由 講義練習_5.1-1_方程與方程的解_融合版 的練習第 1–9 題改寫成選擇／是非題）。
執行：
  python build_game_5.1-1.py            只驗算（sympy），驗算表印到 stdout
  python build_game_5.1-1.py --inject   驗算通過後：題庫注入手機版＋投影版 HTML，並出講義紀錄表 docx
選項次序在這裡定死（兩個 HTML 與紀錄表的 ①②③④ 完全一致），學生可以在紙上圈號碼。
"""
import io, json, os, random, re, sys
from pathlib import Path
import sympy as sp

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = Path(__file__).resolve().parent
a, m, x, y = sp.symbols('a m x y')
NS = dict(a=a, m=m, x=x, y=y)
CIRC = '①②③④'

# ---------------------------------------------------------------------
# 記法：$…$ 包住數學式；F(p,q) 分數；^{…} 多字元指數；[[步驟]] 解說裡的步驟字卡。
# t：yn 二選一（yl＝兩個選項字，預設 是／不是）；mc 四選一（fix＝選項次序照寫，不重排）
# chk：驗算方式，見 verify()
# ---------------------------------------------------------------------
YN = ['是', '不是']
TF = ['對', '不對']
LEVELS = [
 {'key': '方程與一元一次方程', 'short': '判斷', 'sec': '對應練習第 1、6 題',
  'steps': ['等號', '未知數', '一元', '一次'],
  'tips': ['有沒有「＝」？', '有沒有字母？', '只有一個未知數？', '次數是 1？'],
  'rule': '方程：含有未知數的等式。一元一次方程：只有一個未知數，次數是 1，分母沒有未知數。',
  'qs': [
   {'id': '1a', 't': 'yn', 'core': 1, 'ask': '是不是方程？', 'q': '$2x+1=7$', 'a': '是',
    'why': '[[等號]] 有「＝」；[[未知數]] 有 $x$。含有未知數的等式，就是方程。',
    'chk': ('cls', '2x+1=7', 'eq')},
   {'id': '1b', 't': 'yn', 'core': 1, 'ask': '是不是方程？', 'q': '$3+4=7$', 'a': '不是',
    'why': '[[等號]] 有「＝」，但 [[未知數]] 沒有字母。它只是等式，不是方程。',
    'chk': ('cls', '3+4=7', 'eq')},
   {'id': '1c', 't': 'yn', 'core': 1, 'ask': '是不是方程？', 'q': '$5x-2$', 'a': '不是',
    'why': '[[等號]] 沒有「＝」。它只是代數式，不是方程。',
    'chk': ('cls', '5x-2', 'eq')},
   {'id': '1d', 't': 'yn', 'core': 1, 'ask': '是不是一元一次方程？', 'q': '$x+y=10$', 'a': '不是',
    'why': '它是方程，但 [[一元]] 有 $x$、$y$ 兩個未知數，不是只有一個。',
    'chk': ('cls', 'x+y=10', 'lin')},
   {'id': '1e', 't': 'yn', 'core': 1, 'ask': '是不是一元一次方程？', 'q': '$x^2=9$', 'a': '不是',
    'why': '它是方程，但 [[一次]] $x$ 的次數是 2，不是 1。',
    'chk': ('cls', 'x^2=9', 'lin')},
   {'id': '1f', 't': 'yn', 'ask': '是不是一元一次方程？', 'q': '$F(x,3)=4$', 'a': '是',
    'why': '[[一元]] 只有 $x$；[[一次]] 次數是 1；分母是 3，沒有未知數。所以是一元一次方程。',
    'chk': ('cls', 'x/3=4', 'lin')},
   {'id': '1g', 't': 'yn', 'yl': TF, 'ask': '這句話對不對？', 'q': '等式都是方程。', 'a': '不對',
    'why': '$3+4=7$ 是等式，但沒有未知數，不是方程。方程一定是等式；等式不一定是方程。',
    'chk': ('cls', '3+4=7', 'eq_false')},
  ]},
 {'key': '列方程', 'short': '列方程', 'sec': '對應練習第 2、4 題',
  'steps': ['找', '設', '表示', '列'],
  'tips': ['找相等關係', '設未知數', '用 $x$ 表示其他量', '兩邊各寫一個式子'],
  'rule': '比……多：＋　比……少：−　是……的 3 倍：×3　等於、一樣多：＝。比 $x$ 少 5 是 $x-5$，不是 $5-x$。',
  'qs': [
   {'id': '2a', 't': 'mc', 'core': 1, 'q': '$x$ 的 3 倍加上 4 等於 19。', 'a': '$3x+4=19$',
    'o': ['$3(x+4)=19$', '$x+3+4=19$', '$4x+3=19$'],
    'why': '[[列]] 「$x$ 的 3 倍」是 $3x$，「加上 4」是 $+4$，「等於」寫＝。先乘 3 再加 4，不用括號。',
    'chk': ('tr', '3x+4=19', 5)},
   {'id': '2b', 't': 'mc', 'core': 1, 'q': '比 $x$ 少 5 的數等於 12。', 'a': '$x-5=12$',
    'o': ['$5-x=12$', '$x+5=12$', '$5x=12$'],
    'why': '「比 $x$ 少 5」是由 $x$ 減去 5：$x-5$。$5-x$ 次序反了。',
    'chk': ('tr', 'x-5=12', 17)},
   {'id': '2c', 't': 'mc', 'q': '$x$ 的一半等於 $x$ 減 6。', 'a': '$F(x,2)=x-6$',
    'o': ['$2x=x-6$', '$F(x,2)=6-x$', '$F(x,2)-6=x$'],
    'why': '「一半」是除以 2：$F(x,2)$。「$x$ 減 6」是 $x-6$，次序不能反。',
    'chk': ('tr', 'x/2=x-6', 12)},
   {'id': '2d', 't': 'mc', 'core': 1, 'long': 1,
    'q': '甲種筆每枝 3 元，乙種筆每枝 5 元。用 46 元買了兩種筆共 12 枝。設甲種筆買了 $x$ 枝。',
    'a': '$3x+5(12-x)=46$', 'o': ['$3x+5x=46$', '$3x+5(x-12)=46$', '$5x+3(12-x)=46$'],
    'why': '[[設]] 甲 $x$ 枝。[[表示]] 乙 $(12-x)$ 枝。[[列]] 甲的錢＋乙的錢＝46：$3x+5(12-x)=46$。',
    'chk': ('tr', '3x+5(12-x)=46', 7)},
   {'id': '2e', 't': 'mc', 'core': 1, 'long': 1,
    'q': '第一堆書有 50 本，第二堆有 20 本。從第一堆搬 $x$ 本到第二堆，兩堆就一樣多。',
    'a': '$50-x=20+x$', 'o': ['$50+x=20-x$', '$50-x=20$', '$50-x=2x$'],
    'why': '[[表示]] 搬完後，第一堆 $(50-x)$ 本，第二堆 $(20+x)$ 本。[[找]] 「一樣多」寫＝。',
    'chk': ('tr', '50-x=20+x', 15)},
   {'id': '2f', 't': 'mc', 'long': 1,
    'q': '某班有 40 人，女生人數比男生人數的 2 倍少 5 人。設男生有 $x$ 人。',
    'a': '$x+(2x-5)=40$', 'o': ['$x+(5-2x)=40$', '$x+2x+5=40$', '$2x-5=40$'],
    'why': '[[表示]] 女生是男生的 2 倍少 5：$(2x-5)$ 人。[[列]] 男生＋女生＝40。',
    'chk': ('tr', 'x+(2x-5)=40', 15)},
  ]},
 {'key': '方程的解', 'short': '解', 'sec': '對應練習第 3、5、6–9 題',
  'steps': ['代入', '左邊', '右邊', '比較'],
  'tips': ['把數值代入 $x$', '左邊算一次', '右邊算一次', '相等才是解'],
  'rule': '檢驗一個數是不是方程的解：代入後，左邊算一次，右邊算一次，再比較。左右相等，才是解。',
  'qs': [
   {'id': '3a', 't': 'yn', 'core': 1, 'sub': 1, 'q': '$x=3$ 是不是方程 $4x-5=7$ 的解？', 'a': '是',
    'why': '[[左邊]] $4×3-5=7$。[[右邊]] 是 7。[[比較]] 左右相等，所以是解。',
    'chk': ('sol', '4x-5=7', 3)},
   {'id': '3b', 't': 'yn', 'core': 1, 'sub': 1, 'q': '$x=1$ 是不是方程 $5x+2=3x+6$ 的解？', 'a': '不是',
    'why': '[[左邊]] $5×1+2=7$。[[右邊]] $3×1+6=9$。[[比較]] 7 和 9 不相等，所以不是解。',
    'chk': ('sol', '5x+2=3x+6', 1)},
   {'id': '3c', 't': 'yn', 'sub': 1, 'q': '$x=2$ 是不是方程 $5x+2=3x+6$ 的解？', 'a': '是',
    'why': '[[左邊]] $5×2+2=12$。[[右邊]] $3×2+6=12$。[[比較]] 相等，所以是解。',
    'chk': ('sol', '5x+2=3x+6', 2)},
   {'id': '3d', 't': 'mc', 'core': 1, 'fix': 1, 'q': '$x=-2$、$x=3$ 中，哪一個是方程 $2x-1=3x+1$ 的解？',
    'a': '$x=-2$', 'o': ['$x=3$', '兩個都是', '兩個都不是'],
    'why': '[[代入]] 負數要加括號。$x=-2$：左邊 $2×(-2)-1=-5$，右邊 $3×(-2)+1=-5$，相等。'
           '$x=3$：左邊 5，右邊 10，不相等。',
    'chk': ('which', '2x-1=3x+1', [-2, 3])},
   {'id': '3e', 't': 'yn', 'yl': TF, 'ask': '這句話對不對？', 'q': '方程 $x+1=3$ 的解是 $x=2$。', 'a': '對',
    'why': '[[代入]] [[左邊]] $2+1=3$，[[比較]] 等於右邊 3，所以 $x=2$ 是解。',
    'chk': ('sol', 'x+1=3', 2)},
   {'id': '3f', 't': 'mc', 'core': 1, 'q': '已知 $x=2$ 是方程 $3x+a=10$ 的解。$a$ ＝ ？', 'a': '$4$',
    'o': ['$16$', '$8$', '$-4$'],
    'why': '[[代入]] 把 $x=2$ 代入：$3×2+a=10$，即 $6+a=10$，所以 $a=4$。',
    'chk': ('param', '3x+a=10', 2, 'a')},
   {'id': '3g', 't': 'mc', 'q': '若 $x^{m-1}+4=0$ 是關於 $x$ 的一元一次方程，$m$ ＝ ？', 'a': '$2$',
    'o': ['$1$', '$0$', '$3$'],
    'why': '一元一次方程中，$x$ 的次數要是 1：$m-1=1$，所以 $m=2$。',
    'chk': ('deg', 'm-1', 1)},
   {'id': '3h', 't': 'mc', 'q': '下面哪一個方程的解是 $x=-3$？', 'a': '$x+5=2$',
    'o': ['$x-5=2$', '$2x=6$', '$x+3=3$'],
    'why': '[[代入]] $x=-3$：$-3+5=2$，左右相等。其他三個代入後，左右都不相等。',
    'chk': ('whicheq', -3)},
  ]},
]


# ---------------------------------------------------------------- 驗算
def E(s):
    s = s.replace('^', '**').replace('×', '*')
    s = re.sub(r'F\(([^,()]+),([^()]+)\)', r'((\1)/(\2))', s)
    s = re.sub(r'(\d)([a-z(])', r'\1*\2', s)
    s = re.sub(r'([a-z)])([a-z(])', r'\1*\2', s)
    return sp.sympify(s, locals=NS)


def EQ(s):
    l, r = s.split('=')
    return E(l), E(r)


def strip(t):
    return t.replace('$', '')


def classify(s):
    """回傳 (是方程, 是一元一次方程)。"""
    if '=' not in s:
        return False, False
    l, r = EQ(s)
    syms = (l - r).free_symbols | l.free_symbols | r.free_symbols
    if not syms:
        return False, False
    if len(syms) != 1:
        return True, False
    v = syms.pop()
    num, den = sp.fraction(sp.together(l - r))
    if den.has(v):
        return True, False
    return True, sp.Poly(sp.expand(l - r), v).degree() == 1


def sols(s):
    l, r = EQ(s)
    return set(sp.solve(sp.Eq(l, r), x))


def verify():
    rows, bad = [], []
    for L in LEVELS:
        for Q in L['qs']:
            k, ok, note = Q['chk'], False, ''
            if k[0] == 'cls':
                is_eq, is_lin = classify(k[1])
                if k[2] == 'eq':
                    truth = is_eq
                elif k[2] == 'lin':
                    truth = is_lin
                else:            # eq_false：「等式都是方程」——找到反例（等式但不是方程）即為假
                    truth = is_eq
                    note = '反例 3+4=7：'
                ok = (Q['a'] in ('是', '對')) == truth
                note += f'方程={is_eq}，一元一次={is_lin}'
            elif k[0] == 'tr':
                want = sp.Integer(k[2])
                s_ans = sols(strip(Q['a']))
                ok = s_ans == {want} and EQ(strip(Q['a'])) == EQ(k[1])
                dis = [sols(strip(o)) for o in Q['o']]
                if any(d == {want} for d in dis):
                    ok = False; note = '干擾項與答案同解！'
                note = note or f'答案解 x={want}（題意合理）；干擾項解 ' + '、'.join(
                    ','.join(sp.sstr(v) for v in d) or '無' for d in dis)
            elif k[0] == 'sol':
                l, r = EQ(k[1])
                lv, rv = l.subs(x, k[2]), r.subs(x, k[2])
                ok = (Q['a'] in ('是', '對')) == (lv == rv)
                note = f'x={k[2]}：左 {lv}，右 {rv}'
            elif k[0] == 'which':
                l, r = EQ(k[1])
                good = [v for v in k[2] if l.subs(x, v) == r.subs(x, v)]
                exp = {1: f'$x={good[0]}$'}.get(len(good), '兩個都是' if len(good) == 2 else '兩個都不是')
                ok = Q['a'] == exp
                note = '；'.join(f'x={v}：左 {l.subs(x, v)}，右 {r.subs(x, v)}' for v in k[2])
            elif k[0] == 'param':
                l, r = EQ(k[1])
                s_ = sp.solve(sp.Eq(l.subs(x, k[2]), r.subs(x, k[2])), NS[k[3]])
                ok = s_ == [E(strip(Q['a']))] and all(E(strip(o)) != s_[0] for o in Q['o'])
                note = f'代入 x={k[2]} 得 {k[3]}={s_}'
            elif k[0] == 'deg':
                s_ = sp.solve(sp.Eq(E(k[1]), k[2]), m)
                ok = s_ == [E(strip(Q['a']))] and all(E(strip(o)) != s_[0] for o in Q['o'])
                note = f'{k[1]}=1 → m={s_}'
            elif k[0] == 'whicheq':
                v = k[1]
                hit = [o for o in [Q['a']] + Q['o'] if (lambda lr: lr[0].subs(x, v) == lr[1].subs(x, v))(EQ(strip(o)))]
                ok = hit == [Q['a']]
                note = f'x={v} 只令 {strip(hit[0]) if hit else "（無）"} 成立' if ok else f'成立的有 {hit}'
            if Q['t'] == 'mc' and (Q['a'] in Q['o'] or len(set(Q['o'])) != len(Q['o'])):
                ok = False; note += '；選項重複'
            rows.append((Q['num'], Q['id'], '★' if Q.get('core') else '',
                         strip(Q.get('ask', '')) + ' ' + strip(Q['q']), strip(Q['a']), note, 'PASS' if ok else 'FAIL'))
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
                Q['opts'] = Q.get('yl', YN)
            elif Q.get('fix'):
                Q['opts'] = [Q['a']] + Q['o']
            else:
                # 答案位置輪流放（1→2→3→4…，再按 id 微調），避免老是同一個號碼
                p = (n + len(Q['id'])) % 4
                while pos_count[p] > min(pos_count):
                    p = (p + 1) % 4
                pos_count[p] += 1
                rest = Q['o'][:]
                random.Random(Q['id']).shuffle(rest)
                Q['opts'] = rest[:p] + [Q['a']] + rest[p:]
    return pos_count


# ---------------------------------------------------------------- 注入 HTML
GAMES = ['互動遊戲_5.1-1_方程大挑戰.html', '互動遊戲_5.1-1_方程大挑戰_投影版.html']


def inject():
    keep = ('id', 'num', 't', 'core', 'ask', 'q', 'a', 'opts', 'why', 'long', 'sub')
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
    from ch5_common import (para, heading, masthead, student_info_row, pbox, grid, tight, frayer, keyword_table,
                            shaded_box, answers, notes, build_docx, W, GREY_FILL, _tbl, keep_together, GAP, nm, FOOT, SUBJ)

    P = [masthead(SUBJ, '5.1 方程（第 1 課時）方程與方程的解', '講義＋遊戲紀錄表'), student_info_row()]
    P += [shaded_box('今日玩法：老師講完簡報後，全班玩「方程大挑戰」。第 1–2 頁是講義，玩的時候可以翻看；'
                     '第 3–4 頁是紀錄表，每一題都要圈答案。')]
    # ---- 講義（精簡自 講義練習_5.1-1 的「新概念」段）
    P += [heading('一、三個新名詞'),
          pbox([para('方程', bold=True), para('含有未知數的等式。例：{2x-3=5}'),
                para('方程的解', bold=True), para('使方程左、右兩邊的值相等的未知數的值。例：{x=4} 是 {2x-3=5} 的解。'),
                para('求方程的解的過程，叫作解方程。「方程的解」是一個數；「解方程」是一個過程。')])]
    P += [heading('二、「一元一次方程」的邊界'),
          frayer('一元一次方程',
                 ['只含一個未知數，未知數的次數是 1 的方程。'],
                 ['① 是等式，而且含有未知數（是方程）', '② 只有一個未知數', '③ 未知數的次數是 1，分母沒有未知數'],
                 ['{2x-3=5}', '{3x=4(x-5)}', '{frac(x,3)=4}'],
                 ['{2+3=5}：沒有未知數，違反①', '{2x-3}：沒有等號，違反①',
                  '{x+y=5}：兩個未知數，違反②', '{x^2=9}：次數是 2，違反③'])]
    P += [heading('三、列方程：把字詞翻成符號'),
          keyword_table([('比……多 5', '＋5'), ('比……少 5', '−5'), ('是……的 3 倍', '×3'),
                         ('一共、和', '把各部分加起來'), ('等於、是、一樣多、可以買', '＝')],
                        [('比 {x} 少 5 的數', '{x-5}（不是 {5-x}）')]) + GAP]
    P += [heading('四、檢驗一個數是不是方程的解'),
          grid([('1. 代入', '2. 左邊', '3. 右邊', '4. 比較'),
                ('把數值代入 {x}（負數加括號）', '左邊算一次', '右邊算一次', '相等才是解')],
               [W // 4] * 3 + [W - 3 * (W // 4)])]

    # ---- 紀錄表
    P += [heading('五、遊戲紀錄表', page_break_before=True),
          tight(para('先圈答案；老師揭曉後，答對打 ✔，答錯寫正確答案。5 分鐘版只做有 ★ 的題目。', sz=22), line=300, after=20),
          tight(para(f'我的成績：答對 ＿＿＿ ／ {sum(len(L["qs"]) for L in LEVELS)} 題'
                     f'（5 分鐘版：答對 ＿＿＿ ／ {sum(1 for L in LEVELS for Q in L["qs"] if Q.get("core"))} 題）',
                     bold=True, sz=22), line=300, after=60)]
    w = [640, 5900, 2150, 520]
    w.append(W - sum(w))
    for li, L in enumerate(LEVELS):
        rows = [{'hdr': True, 'cells': [{'p': [tight(para(f'第 {li + 1} 關　{L["key"]}　（{" → ".join(L["steps"])}）',
                                                         bold=True, sz=23))], 'shd': GREY_FILL, 'span': 5}]},
                {'hdr': True, 'cells': [{'p': [tight(para(h, bold=True, sz=21, jc='center'))], 'shd': GREY_FILL}
                                        for h in ('題號', '題目', '圈答案', '✔', '答錯時寫正確答案')]}]
        for Q in L['qs']:
            qp = [tight(para(nm(D((Q['ask'] + '　') if Q.get('ask') else '') + D(Q['q'])), sz=22), line=270, after=10)]
            if Q['t'] == 'mc':
                ops = [f'{CIRC[i]} {D(o)}' for i, o in enumerate(Q['opts'])]
                vis = lambda o: sum(2 if '一' <= c <= '鿿' else 1 for c in re.sub(r'[$]|F\(|[(),]', '', o))
                short = sum(vis(o) for o in Q['opts']) <= 18
                lines = ['　　'.join(ops)] if short else ['　　'.join(ops[:2]), '　　'.join(ops[2:])]
                qp += [tight(para(ln, sz=22), line=270, after=0) for ln in lines]
                mine = ' '.join(CIRC[:len(Q['opts'])])
            else:
                mine = '　'.join(Q['opts'])
            if Q.get('sub'):
                qp.append(tight(para('左邊＝＿＿＿＿＿　右邊＝＿＿＿＿＿', sz=22), line=320, after=0))
            star = '★' if Q.get('core') else ''
            rows.append({'cells': [
                [tight(para(f'{Q["num"]}{star}', bold=True, sz=22, jc='center'))],
                qp,
                [tight(para(mine, sz=24, jc='center', bold=True))],
                [tight(para('', sz=22))],
                [tight(para('', sz=22))]], 'h': 0})
        P += [_tbl(rows, w, trailing_blank=False)] + ([GAP] if li < len(LEVELS) - 1 else [])
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
    ans += ['左邊／右邊：14．左 7，右 7　15．左 7，右 9　16．左 12，右 12',
            '遊戲網址與 QR：見 互動遊戲_5.1-1_QR.png；投影版按 Space 揭曉／下一題，數字鍵 1–4 為該隊加 10 分。',
            '題目來源：講義練習_5.1-1 練習第 1–9 題改寫（第 9 題「自己寫方程」改為第 21 題「哪一個方程的解是 x＝−3」）；'
            '逐題 sympy 驗算見 驗算_第五章_一元一次方程.md 文末。',]
    P += answers(ans)
    P += notes('D6 明確教學三階段', ('D13 弗雷爾概念模型', 'D8 關鍵字對譯'),
               '學生不喜歡做 5.1-1 的紙本練習，改為「簡報（我做／我們做）→ 遊戲（你做）」：'
               '練習第 1–9 題原意保留，改寫成判斷／選擇題，按「判斷 → 列方程 → 方程的解」三關闖關；'
               '紀錄表讓學生每題圈答案、即時核對、寫下改正，教師課後可收回看錯在哪一關。',
               '講義頁保留四象限與關鍵字對譯全表；遊戲第 2 關每題答錯時重現步驟字卡（找→設→表示→列）；'
               '第 3 關前三題紀錄表留「左邊＝　右邊＝」格，第 4 題起不再提供。',
               'A—2—2　瞭解一元一次方程及其有關的概念；A—2—4　能根據具體問題情境中的等量關係，列出一元一次方程',
               '課本 p.111–115（PDF 第 118–122 頁）',
               '投影版：沒有平板時用，學生舉手指作答、紀錄表圈號碼，分隊加分。手機版：每人一部時用，'
               '5 分鐘倒數、自動計分；題號與選項號碼兩版一致，紀錄表通用。')
    out = HERE / '講義紀錄表_5.1-1_方程與方程的解_遊戲版.docx'
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
