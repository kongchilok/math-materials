# -*- coding: utf-8 -*-
r"""
build_remedial_20261126_circle_tangent.py — 初三數學補救班 課後補救教學（2026-11-26，週四）
範圍：圓（基本概念）→ 垂徑定理 → 圓心角、圓周角 → 圓內接四邊形 → 點／直線與圓 → 切線 → 切線長定理（含內切圓）

使用者 2026-11-26：「由圓至切線長定理」；內容參考 `08_圓的有關性質\新修訂\`；
難度比「抽離課堂檢測 02」高一點＝抽離練習 B 至 C 程度；基礎題可以有但要少；
整體內容比上一次（11-19，17 題 6 頁）少；題目壓縮至 4 頁。
題源：新修訂資料夾 23-24 初三乙幾何統測、複習_圓（數據原樣或略改，出處寫教師卷）＋單元 09 練習第 7 題（倒轉改編）。
版面層：import `..\..\初三數學\融合班講義練習\08_圓的有關性質\新修訂\circle_common.py`（跨資料夾依賴）。
`python build_remedial_20261126_circle_tangent.py --verify`：用圖的座標重算全部答案。
逐題驗算見《驗算_課後補救教學20261126_圓到切線長定理.md》。
"""
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(
    HERE, '..', '..', '初三數學', '融合班講義練習', '08_圓的有關性質', '新修訂')))
from circle_common import *  # noqa: E402,F401,F403
from omml_docx import MediaRegistry, _tbl  # noqa: E402,F401

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

OUT = HERE
FIG = os.path.join(HERE, '_tmp_fig_tangent')
import circle_common as cc  # noqa: E402
cc.FIG = FIG
SUBJ_R = '初三數學（補救班）'
UNIT = '圓：由圓的基本概念到切線長定理'
BASE = '課後補救教學_初三數學補救班_20261126_圓到切線長定理'
FOOT_R = '初三數學補救班．課後補救教學 2026-11-26'
PAREN = '（　　　）'
C65 = math.cos(math.radians(65))


# ================================ 幾何資料（圖與 --verify 共用） ================================
def pol(deg):
    a = math.radians(deg)
    return (math.cos(a), math.sin(a))


def vertex(t1, t2):
    """內切圓（r＝1）上相鄰兩切點的度數 → 兩條切線的交點（三角形頂點）。"""
    mid = (t1 + t2) / 2
    d = 1 / math.cos(math.radians(abs(t2 - t1) / 2))
    return (d * math.cos(math.radians(mid)), d * math.sin(math.radians(mid)))


# 練 11：內切圓切點 E 270°、D 150°、F 40°（∠DOF＝110° → ∠A＝70°）
T11 = {'D': 150, 'E': 270, 'F': 40}
V11 = {'A': vertex(40, 150), 'B': vertex(150, 270), 'C': vertex(270, 400)}

# 練 12：三邊 AB＝7、BC＝9、CA＝8 的真實三角形與內切圓（以內切圓半徑為單位）
_B, _C = (0.0, 0.0), (9.0, 0.0)
_ax = (49 - 64 + 81) / 18
_A = (_ax, math.sqrt(49 - _ax ** 2))
_a, _b, _c = 9, 8, 7
_I = ((_a * _A[0] + _b * _B[0] + _c * _C[0]) / 24, (_a * _A[1] + _b * _B[1] + _c * _C[1]) / 24)
_R12 = (0.5 * 9 * _A[1]) / 12


def _u12(p):
    return ((p[0] - _I[0]) / _R12, (p[1] - _I[1]) / _R12)


def _foot(p, q):
    """I 到直線 pq 的垂足。"""
    vx, vy = q[0] - p[0], q[1] - p[1]
    t = ((_I[0] - p[0]) * vx + (_I[1] - p[1]) * vy) / (vx * vx + vy * vy)
    return (p[0] + t * vx, p[1] + t * vy)


V12 = {'A': _A, 'B': _B, 'C': _C, 'D': _foot(_A, _B), 'E': _foot(_B, _C), 'F': _foot(_C, _A)}


def xy(p, off=(12, -10)):
    return ('xy', p[0], p[1], off)


# ================================ 圖 ================================
FIGS = {
    # 切線工具箱：PA、PB 切 ⊙O 於 A、B
    'r_t': lambda: circ({'A': (60, 1.1), 'B': (300, 1.1), 'P': xy((2, 0), (14, 4))},
                        segs=[('P', 'A'), ('P', 'B'), ('O', 'A'), ('O', 'B'), ('O', 'P', {'dash': 1})],
                        right=[('A', 'O', 'P'), ('B', 'O', 'P')], r=62, olab=(-18, 6)),
    # 練 3：r＝13、AB＝24 在 O 上方（OP＝5），EF 是鉛直直徑，E 在上
    'q3': lambda: circ({'A': (180 - math.degrees(math.atan2(5, 12)), 1.1), 'B': (math.degrees(math.atan2(5, 12)), 1.1),
                        'E': (90, 1), 'F': (270, 1), 'P': xy((0, 5 / 13), (-14, -12))},
                       segs=[('A', 'B'), ('E', 'F'), ('O', 'A'), ('O', 'B')], right=[('P', 'E', 'B')],
                       olab=(8, 14)),
    # 練 4：正方形 ABCD 內接，P 在劣弧 CD 上
    'q4': lambda: circ({'A': (135, 1), 'B': (45, 1), 'C': (315, 1), 'D': (225, 1), 'P': (262, 1)},
                       segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('P', 'B'), ('P', 'C')],
                       olab=(-6, -10)),
    # 練 5：AB 直徑，C 100°、D 300°，∠ADC＝40°
    'q5': lambda: circ({'A': (180, 1.1), 'B': (0, 1.1), 'C': (100, 1), 'D': (300, 1.1)},
                       segs=[('A', 'B'), ('A', 'C'), ('A', 'D'), ('D', 'C')], olab=(-6, -10)),
    # 練 6：等邊 △ABC 內接，D 在弧 AC（不含 B）上，∠DAC＝20°
    'q6': lambda: circ({'A': (90, 1), 'B': (210, 1.1), 'C': (330, 1.1), 'D': (10, 1.1)},
                       segs=[('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('D', 'C')], olab=(-20, 6)),
    # 練 7：PA 切 ⊙O 於 A，PO 交 ⊙O 於 B，∠P＝30°（OP＝2r）
    'q7': lambda: circ({'A': (60, 1.1), 'B': xy((1, 0), (12, 16)), 'P': xy((2, 0), (14, 4))},
                       segs=[('P', 'A'), ('O', 'P')], r=62, olab=(-6, 18)),
    # 練 8：∠APB＝60°，AB 交 OP 於 C（OC＝r/2）
    'q8': lambda: circ({'A': (60, 1.1), 'B': (300, 1.1), 'P': xy((2, 0), (14, 4)), 'C': xy((0.5, 0), (10, 14))},
                       segs=[('P', 'A'), ('P', 'B'), ('O', 'A'), ('O', 'P'), ('A', 'B')], r=62, olab=(-18, 6)),
    # 練 9：∠AOB＝130°，AC 直徑
    'q9': lambda: circ({'A': (65, 1.1), 'B': (295, 1.1), 'C': (245, 1.1), 'P': xy((1 / C65, 0), (14, 4))},
                       segs=[('P', 'A'), ('P', 'B'), ('A', 'C'), ('A', 'B')], r=58, olab=(-20, 2)),
    # 練 10：PA、PB、CD 都是切線，E 是 CD 的切點
    'q10': lambda: circ({'A': (60, 1.1), 'B': (300, 1.1), 'E': (0, 0.8), 'P': xy((2, 0), (14, 4)),
                         'C': xy((1, 1 / math.sqrt(3)), (4, -14)), 'D': xy((1, -1 / math.sqrt(3)), (4, 16))},
                        segs=[('P', 'A'), ('P', 'B'), ('C', 'D')], r=62, olab=(-18, 6)),
    # 練 11：內切圓，∠DEF＝55°
    'q11': lambda: circ({**{k: (v, 1.15) for k, v in T11.items()},
                         'A': xy(V11['A'], (0, -14)), 'B': xy(V11['B'], (-12, 8)), 'C': xy(V11['C'], (12, 8))},
                        segs=[('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E'), ('E', 'F')], r=52, olab=(-4, -10)),
    # 練 12：三邊 7、9、8 的真實比例
    'q12': lambda: circ({'A': xy(_u12(V12['A']), (0, -14)), 'B': xy(_u12(V12['B']), (-12, 8)),
                         'C': xy(_u12(V12['C']), (12, 8)), 'D': xy(_u12(V12['D']), (-12, -6)),
                         'E': xy(_u12(V12['E']), (0, 16)), 'F': xy(_u12(V12['F']), (12, -6))},
                        segs=[('A', 'B'), ('B', 'C'), ('C', 'A')], r=48, olab=(-4, -10)),
}


def cut_tail(xml):
    """aside_layout() 表後自帶 1.5 行空段；剪走，改由 GAP／GAPK 做框距。"""
    i = xml.rfind('</w:tbl>')
    return xml[:i + len('</w:tbl>')]


def F(media, key, w=4.6):
    return expand_image(fig(FIGS[key](), 'r_' + key, w), media)


_RULE_PPR = ('<w:pPr><w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="808080"/>'
             '<w:between w:val="single" w:sz="5" w:space="4" w:color="808080"/></w:pBdr>'
             '<w:spacing w:before="0" w:after="0" w:line="380" w:lineRule="exact"/></w:pPr>')


def ruled(label=''):
    """一條書寫線（行高 19pt）；要有 w:between 每行才有線（記憶 docx_adjacent_border_paras_merge）。"""
    run = (f'<w:r><w:rPr><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>'
           f'<w:t xml:space="preserve">{label}</w:t></w:r>') if label else ''
    return f'<w:p>{_RULE_PPR}{run}</w:p>'


def Q(media, head, body=(), key=None, n=3, w=4.0, opts_=None, pct=0.66, hint_=None):
    main = [tight(para(head, keep_next=True), line=290, after=30)]
    main += [tight(para(nm(x), keep_next=True), line=290, after=30) for x in body]
    if opts_:
        main += [tight(para(x, ind=300), line=290, after=30) for x in opts_]
    if hint_:
        main.append(tight(para(nm('提示：' + hint_), sz=21, keep_next=True), line=300, after=30))
    main += [ruled() for _ in range(n)] + [ruled('改正：')]
    if key:
        return cut_tail(aside_layout(main, [F(media, key, w)], main_pct=pct, media=media, boxed=True)) + GAP
    return pbox(main)


def review(media, key, lines_, w=2.8):
    """工具箱：左欄一行一件事（灰底），右欄配圖；整塊 keepNext 黐住下一題。"""
    left = [para('切線工具箱', bold=True, spacing=False, shd=GREY_FILL)]
    left += [tight(para(nm(x), shd=GREY_FILL, sz=22), line=290, after=30) for x in lines_]
    xml = cut_tail(aside_layout(left, [F(media, key, w)], main_pct=0.70, media=media, boxed=True))
    xml = keep_together(xml).replace('<w:pPr>', '<w:pPr><w:keepNext/>').replace(
        '<w:keepNext/><w:keepNext/>', '<w:keepNext/>')
    return xml + GAPK


# ================================ 學生卷 ================================
def student():
    M = MediaRegistry()
    P = [masthead(SUBJ_R, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('建議 45 分鐘完成　共 12 題　滿分 100 分　先畫輔助線再列式；批改後在「改正」欄訂正。', bold=True))

    # ---------------- 一 ----------------
    P.append(heading('一、基礎熱身（12 分）'))
    P.append(Q(M, '練 1．（6 分，每空 1 分）{⊙O} 的半徑是 5 cm。',
               ['(1) 若 {OP=4} cm，則點 P 在 {⊙O} ＿＿＿＿（填「內」「上」或「外」）；',
                '(2) 若直線 l 與 {⊙O} 相交，圓心 O 到 l 的距離為 d，則 d ＿＿ 5（填「>」「<」或「=」）；',
                '(3) 若圓心 O 到直線 m 的距離是 5 cm，則 m 與 {⊙O} ＿＿＿＿，公共點有＿＿個；',
                '(4) {⊙O} 中最長的弦長是＿＿＿＿ cm；',
                '(5) 兩個同心圓的圓心是 O，大圓的弦 AB 與小圓只有一個公共點 C，且 C 是 AB 的中點，'
                '則直線 AB 與小圓＿＿＿＿。'], n=0))
    P.append(Q(M, '練 2．（6 分）四邊形 ABCD 內接於 {⊙O}，{∠A:∠C=2:3}，{∠B=100°}。'
                  '求 {∠A}、{∠C} 和 {∠D}。', n=2))

    # ---------------- 二 ----------------
    P.append(heading('二、垂徑定理、圓心角與圓周角（34 分）'))
    # 2026-11-26 排版：兩題短題放前，令第 1 頁塞得落（圖 key 保留 q5／q6／q3／q4）
    P.append(Q(M, '練 3．（7 分）如圖，AB 是 △ADC 外接圓的直徑，{∠D=40°}，求 {∠CAB} 的度數。',
               key='q5', n=2, w=3.6, hint_='連接 BC，找出和 {∠D} 同對一條弧的角。'))
    P.append(Q(M, '練 4．（7 分）如圖，D 是等邊 △ABC 外接圓上的點，{∠DAC=20°}，求 {∠ACD} 的度數。',
               key='q6', n=2, w=3.6))
    P.append(Q(M, '練 5．（10 分）如圖，AB 是 {⊙O} 的弦，{AB=24}，{⊙O} 的半徑是 13。'
                  '直徑 EF 垂直平分 AB，垂足是 P（E 在 AB 的上方），連接 OA、OB。',
               ['(1) 求 OP 的長；（4 分）', '(2) 求 PF 和 PE 的長。（6 分）'], key='q3', n=3))
    P.append(Q(M, '練 6．（10 分）如圖，正方形 ABCD 的外接圓為 {⊙O}，點 P 在劣弧 CD 上（不與 C、D 重合）。',
               ['(1) 求 {∠BPC} 的度數；（5 分）', '(2) 若 {⊙O} 的半徑為 8，求正方形 ABCD 的邊長。（5 分）'],
               key='q4', n=3, hint_='連接 OB、OC。'))

    # ---------------- 三 ----------------
    P.append(heading('三、切線與切線長定理（54 分）'))
    P.append(review(M, 'r_t', ['切線垂直於經過切點的半徑：見切點，連半徑，得直角。',
                               '切線長定理：從圓外一點 P 引兩條切線，{PA=PB}，PO 平分 {∠APB}。',
                               '三角形的內切圓：每個頂點引出的兩條切線段相等。']))
    P.append(Q(M, '練 7．（8 分）如圖，P 為 {⊙O} 外一點，PA 切 {⊙O} 於點 A，PO 交 {⊙O} 於點 B，'
                  '{∠P=30°}，{OB=3}。',
               ['(1) 求線段 BP 的長；（4 分）', '(2) 求切線長 PA。（4 分）'], key='q7', n=3))
    P.append(Q(M, '練 8．（9 分）如圖，PA、PB 是 {⊙O} 的兩條切線，切點分別為 A、B，連接 OA、OP、AB，'
                  'OP 與 AB 相交於點 C。若 {∠APB=60°}，{OC=2} cm，求 PC 的長。',
               key='q8', n=3, hint_='先求 {∠AOP}，再在 △AOC 中求 OA。'))
    P.append(Q(M, '練 9．（10 分）如圖，PA、PB 是 {⊙O} 的切線，A、B 為切點，AC 是 {⊙O} 的直徑，'
                  '{∠BAC=25°}。求 {∠PAB} 和 {∠P} 的度數。', key='q9', n=3))
    P.append(Q(M, '練 10．（8 分）如圖，PA、PB 分別切 {⊙O} 於點 A、B，CD 切 {⊙O} 於點 E，'
                  '分別交 PA、PB 於點 C、D。若 {PA=6}，求 △PCD 的周長。', key='q10', n=3,
               hint_='CE 和 CA 都是由點 C 引出的切線。'))
    P.append(Q(M, '練 11．（9 分）如圖，△ABC 的內切圓 {⊙O} 與 AB、BC、AC 分別相切於點 D、E、F。'
                  '若 {∠DEF=55°}，求 {∠A} 的度數。', key='q11', n=3, hint_='連接 OD、OF，看四邊形 ADOF。'))
    P.append(Q(M, '練 12．（10 分）如圖，△ABC 的內切圓與 AB、BC、CA 分別相切於點 D、E、F，'
                  '{AB=7}，{BC=9}，{CA=8}。求 AD、BE、CF 的長。', key='q12', n=4,
               hint_='設 {AD=AF=x}，用 x 表示 BD、CF，再用 BC 列方程。'))
    out = os.path.join(OUT, BASE + '_學生卷.docx')
    print(build_docx(P, out, footer_text=FOOT_R, media=M))


# ================================ 教師卷 ================================
DATA = [
    ('一', None, None, None),
    ('練 1（6 分）', '(1) 內　(2) <　(3) 相切，1　(4) 10　(5) 相切',
     '(1) {d=4<r}。(3) {d=r} → 相切。(5) 連 OC：C 是弦 AB 中點 → {OC⊥AB}（垂徑定理推論），'
     'AB 過小圓半徑 OC 的外端且垂直於它 → 相切。',
     '23-24 初三乙幾何統測 第 7、16、1、8 題（合併改填空）'),
    ('練 2（6 分）', '{∠A=72°}，{∠C=108°}，{∠D=80°}',
     '對角互補：{∠A+∠C=180°}，{∠A=180°×frac(2,5)=72°}（2 分），{∠C=108°}（2 分）；{∠D=180°-100°=80°}（2 分）。',
     '23-24 統測 第 15 題（加 {∠B}、問三個角）'),
    ('二', None, None, None),
    ('練 3（7 分）', '{50°}',
     '連 BC：AB 直徑 → {∠ACB=90°}（2 分）；{∠B=∠D=40°}（同對 {arc(AC)}）（3 分）；'
     '{∠CAB=90°-40°=50°}（2 分）。另法：連 OC，{∠AOC=80°}，△AOC 等腰。',
     '23-24 統測 第 14 題（原題）'),
    ('練 4（7 分）', '{40°}',
     '{∠B=60°}（1 分）；ABCD 是圓內接四邊形 → {∠D=180°-60°=120°}（3 分）；'
     '{∠ACD=180°-120°-20°=40°}（3 分）。誤答 {20°}（以為 {∠ACD=∠DAC}）不給分。',
     '23-24 統測 第 5 題（選擇改解答）'),
    ('練 5（10 分）', '(1) {OP=5}　(2) {PF=18}，{PE=8}',
     '(1) {AP=24÷2=12}（2 分）；{OP^2=13^2-12^2=25}，{OP=5}（2 分）。'
     '(2) F 在 O 的另一邊：{PF=PO+OF=5+13=18}（3 分）；{PE=OE-OP=13-5=8}（3 分）。',
     '23-24 統測 第 28(2) 題（數據不改；刪尺規作圖、加問 OP、PE）'),
    ('練 6（10 分）', '(1) {45°}　(2) {8sqrt(2)}',
     '(1) 正方形對角線互相垂直 → {∠BOC=90°}（2 分）；{∠BPC} 與 {∠BOC} 同對 {arc(BC)}，'
     '{∠BPC=frac(1,2)×90°=45°}（3 分）。(2) {BC^2=8^2+8^2=128}（3 分），{BC=8sqrt(2)}（2 分）。',
     '23-24 統測 第 29 題（原題）'),
    ('三', None, None, None),
    ('練 7（8 分）', '(1) {BP=3}　(2) {PA=3sqrt(3)}',
     '(1) 連 OA：{∠OAP=90°}（1 分）；{OA=OB=3}，30° 所對直角邊是斜邊一半 → {OP=6}（2 分）；{BP=6-3=3}（1 分）。'
     '(2) {PA^2=6^2-3^2=27}（2 分），{PA=3sqrt(3)}（2 分）。',
     '23-24 統測 第 17 題（加問 PA）'),
    ('練 8（9 分）', '{PC=6} cm',
     '{∠APO=30°}，{∠OAP=90°} → {∠AOP=60°}（2 分）；切線長定理 → OP 垂直平分 AB，{∠OCA=90°}（2 分）；'
     '△AOC 中 {∠OAC=30°} → {OA=2OC=4}（2 分）；△AOP 中 {OP=2OA=8}（2 分）；{PC=8-2=6}（1 分）。',
     '複習_圓 第 36 題（原題）'),
    ('練 9（10 分）', '{∠PAB=65°}，{∠P=50°}',
     '{∠OAP=90°}（切線⊥半徑）（2 分）；{∠PAB=90°-25°=65°}（3 分）；{PA=PB} → {∠PBA=65°}（2 分）；'
     '{∠P=180°-65°-65°=50°}（3 分）。',
     '23-24 統測 第 19 題（原題）'),
    ('練 10（8 分）', '12',
     '切線長定理：{CE=CA}，{DE=DB}，{PB=PA=6}（3 分）；'
     '周長＝{PC+CE+ED+DP=PC+CA+DB+DP=PA+PB=12}（5 分）。',
     '複習_圓 第 12 題（選擇改解答）'),
    ('練 11（9 分）', '{70°}',
     '{∠DOF=2∠DEF=110°}（同對 {arc(DF)}）（3 分）；{∠ADO=∠AFO=90°}（切線⊥半徑）（3 分）；'
     '四邊形 ADOF：{∠A=360°-90°-90°-110°=70°}（3 分）。',
     '23-24 統測 第 26 題（選擇改解答）'),
    ('練 12（10 分）', '{AD=3}，{BE=4}，{CF=5}',
     '設 {AD=AF=x}（2 分）；{BD=BE=7-x}，{CF=CE=8-x}（3 分）；'
     '{BE+CE=BC}：{(7-x)+(8-x)=9}（2 分），{x=3}（1 分）；{BE=4}，{CF=5}（2 分）。驗：{3+4=7}，{4+5=9}，{5+3=8}。',
     '單元 09 練習 第 7 題倒轉改編（原題已知切線段求周長）'),
]


def teacher():
    P = [masthead(SUBJ_R, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。分值為建議分配，滿分 100 分；括號內為步驟分。', sz=22))
    P.append(para('實施日期：補救班 2026-11-26（週四）。', sz=22, bold=True))
    w = [int(W * 0.09), int(W * 0.20), int(W * 0.50)]
    w.append(W - sum(w))
    rows = [{'hdr': True, 'cells': [{'p': [tight(para(h, bold=True, sz=21))], 'shd': GREY_FILL}
                                    for h in ('題號', '答案', '解析與評分', '題源')]}]
    for n_, a, why, src in DATA:
        if a is None:
            rows.append([{'p': [tight(para(f'{n_}、', bold=True, sz=21))], 'span': 4, 'shd': GREY_FILL}])
            continue
        rows.append([[tight(para(n_, sz=21))], [tight(para(nm(x), bold=True, sz=21)) for x in a.split('　')],
                     [tight(para(nm(why), sz=21))], [tight(para(src, sz=20))]])
    P.append(_tbl(rows, w, trailing_blank=False) + GAP)
    P.append(heading('重整說明', keep_next=True))
    for t in ['範圍：圓的基本概念 → 垂徑定理 → 圓心角、圓周角 → 圓內接四邊形 → 點和直線與圓的位置關係 → 切線 → '
              '切線長定理（含三角形內切圓）。上一份（11-19）已練基本概念至圓周角定理，本份只留 2 題基礎熱身，'
              '切線部分（上一份未練）佔 54 分。',
              '難度：以抽離練習 B 至 C 為準，比抽離課堂檢測 02 高一級——10 題中 8 題要兩步以上'
              '（先補輔助線或先找等量，再計算）；只在練 3、6、8、10、11、12 留一句提示，不給步驟格。',
              '練 5 用到垂徑定理：丙班教案未排垂徑定理，丙班學生如未學過可只做 (2) 的 PF、PE（直接給 OP＝5）。',
              '練 12 為改編題（原題已知 AD、BE、CF 求周長），其餘數據與原卷相同或只加問一小題。',
              '圖形：全部按題意重畫（黑白），用座標把角度、長度調成與題目數據一致，核對見驗算檔。']:
        P.append(tight(para(t, sz=21), line=300, after=40))
    out = os.path.join(OUT, BASE + '_教師卷.docx')
    print(build_docx(P, out, footer_text=FOOT_R))


# ================================ 座標核對 ================================
def ang(v, a, b):
    ux, uy = a[0] - v[0], a[1] - v[1]
    wx, wy = b[0] - v[0], b[1] - v[1]
    c = (ux * wx + uy * wy) / (math.hypot(ux, uy) * math.hypot(wx, wy))
    return math.degrees(math.acos(max(-1, min(1, c))))


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def verify():
    O = (0.0, 0.0)
    # 練 5：r＝13
    t = math.atan2(5, 12)
    A, B = (-13 * math.cos(t), 13 * math.sin(t)), (13 * math.cos(t), 13 * math.sin(t))
    Pp, E, Fp = (0, 5.0), (0, 13.0), (0, -13.0)
    print(f'練5 AB {dist(A, B):.2f} OP {dist(O, Pp):.2f} PF {dist(Pp, Fp):.2f} PE {dist(Pp, E):.2f} '
          f'∠OPB {ang(Pp, O, B):.1f}')
    # 練 6：r＝8
    sq = {k: tuple(8 * c for c in pol(d)) for k, d in {'A': 135, 'B': 45, 'C': 315, 'D': 225, 'P': 262}.items()}
    print(f'練6 ∠BPC {ang(sq["P"], sq["B"], sq["C"]):.1f} BC {dist(sq["B"], sq["C"]):.4f} 8√2 {8 * math.sqrt(2):.4f}')
    q = {k: pol(d) for k, d in {'A': 180, 'B': 0, 'C': 100, 'D': 300}.items()}
    print(f'練3 ∠ADC {ang(q["D"], q["A"], q["C"]):.1f} ∠CAB {ang(q["A"], q["C"], q["B"]):.1f}')
    q = {k: pol(d) for k, d in {'A': 90, 'B': 210, 'C': 330, 'D': 10}.items()}
    print(f'練4 △ABC 角 {ang(q["A"], q["B"], q["C"]):.1f}/{ang(q["B"], q["A"], q["C"]):.1f} '
          f'∠DAC {ang(q["A"], q["D"], q["C"]):.1f} ∠ACD {ang(q["C"], q["A"], q["D"]):.1f}')
    # 練 7：r＝3
    A, B, Pp = tuple(3 * c for c in pol(60)), (3.0, 0.0), (6.0, 0.0)
    print(f'練7 ∠OAP {ang(A, O, Pp):.1f} ∠P {ang(Pp, A, O):.1f} BP {dist(B, Pp):.4f} PA {dist(Pp, A):.4f} '
          f'3√3 {3 * math.sqrt(3):.4f}')
    # 練 8：r＝4
    A, B, Pp = tuple(4 * c for c in pol(60)), tuple(4 * c for c in pol(300)), (8.0, 0.0)
    C = (2.0, 0.0)
    print(f'練8 ∠APB {ang(Pp, A, B):.1f} ∠OAP {ang(A, O, Pp):.1f} C 在 AB 上 {abs(A[0] - C[0]) < 1e-9} '
          f'OC {dist(O, C):.2f} PC {dist(Pp, C):.2f}')
    A, B, C, Pp = pol(65), pol(295), pol(245), (1 / C65, 0.0)
    print(f'練9 ∠OAP {ang(A, O, Pp):.1f} ∠OBP {ang(B, O, Pp):.1f} ∠BAC {ang(A, B, C):.1f} '
          f'∠PAB {ang(A, Pp, B):.1f} ∠P {ang(Pp, A, B):.1f}')
    A, B, Pp, E = pol(60), pol(300), (2.0, 0.0), (1.0, 0.0)
    C, D = (1, 1 / math.sqrt(3)), (1, -1 / math.sqrt(3))
    per = dist(Pp, C) + dist(C, D) + dist(D, Pp)
    print(f'練10 C 在 PA 上 {abs(ang(C, A, Pp) - 180) < 1e-6} CE {dist(C, E):.4f} CA {dist(C, A):.4f} '
          f'周長 {per:.4f} PA+PB {dist(Pp, A) + dist(Pp, B):.4f}')
    V, T = V11, {k: pol(d) for k, d in T11.items()}
    print(f'練11 切點在邊上 D:{abs(ang(T["D"], V["A"], V["B"]) - 180) < 1e-6} '
          f'E:{abs(ang(T["E"], V["B"], V["C"]) - 180) < 1e-6} F:{abs(ang(T["F"], V["C"], V["A"]) - 180) < 1e-6} '
          f'∠DEF {ang(T["E"], T["D"], T["F"]):.1f} ∠A {ang(V["A"], V["B"], V["C"]):.1f} '
          f'∠B {ang(V["B"], V["A"], V["C"]):.1f} ∠C {ang(V["C"], V["A"], V["B"]):.1f}')
    V = V12
    print(f'練12 AB {dist(V["A"], V["B"]):.3f} BC {dist(V["B"], V["C"]):.3f} CA {dist(V["C"], V["A"]):.3f} '
          f'r {_R12:.4f} ID {dist(_I, V["D"]):.4f} IE {dist(_I, V["E"]):.4f} IF {dist(_I, V["F"]):.4f} '
          f'AD {dist(V["A"], V["D"]):.3f} AF {dist(V["A"], V["F"]):.3f} BE {dist(V["B"], V["E"]):.3f} '
          f'BD {dist(V["B"], V["D"]):.3f} CF {dist(V["C"], V["F"]):.3f} CE {dist(V["C"], V["E"]):.3f}')


if __name__ == '__main__':
    if '--verify' in sys.argv:
        verify()
    else:
        os.makedirs(FIG, exist_ok=True)
        student()
        teacher()
