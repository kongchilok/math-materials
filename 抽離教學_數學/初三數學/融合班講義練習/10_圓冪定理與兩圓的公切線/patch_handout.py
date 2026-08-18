# -*- coding: utf-8 -*-
"""在《講義_圓冪定理與兩圓的公切線_融合版.docx》的 §三 之後、練習指示句之前，
插入新的「四、兩圓的公切線長度」（2026-08-17 補齊：單元標題承諾咗「公切線」，
但原稿只教咗位置關係判斷同圓心距，冇教公切線長度本身點計算）。

主設計 D7 提示卡（定義框＋示意圖＋算式範例——沿用 §一～§三 原有嘅版面手法，
呢份文件冚唪唥都係呢種版面，只係未曾正式標註設計代號）
對應 S5 幾何定理與推理。

§一、§二、§三 原有內容一字不改。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch_common import *      # noqa: F401,F403
from patch_common import (seeded_registry, para_start, patch, guard,
                          _tbl, _PAGE_CONTENT_WIDTH, expand_image)
import tangent_fig

FIGS = os.path.join(HERE, 'figs')
os.makedirs(FIGS, exist_ok=True)
DOCX = os.path.join(HERE, '講義_圓冪定理與兩圓的公切線_融合版.docx')
guard(DOCX, '四、兩圓的公切線長度')

svg = tangent_fig.tangent_construction_fig()
FIG_PATH = os.path.join(FIGS, 'tangent_construction.png')
tangent_fig.ds.svg_to_png(svg, FIG_PATH)

media, N_SEED = seeded_registry(['rIdImg1', 'rIdImg2', 'rIdImg3'])   # 原檔三張圖先佔位

# ==================== 組裝 §四 ====================
P = []
P.append(heading('四、兩圓的公切線長度'))
P.append(para('上面學咗點判斷兩圓嘅位置關係、點由半徑求圓心距。而家再進一步：'
              '知道咗 R、r、d，仲可以求返公切線本身有幾長。'))

P.append(shaded_box('設兩圓半徑 R、r（R≥r），圓心距 d。'
                    '外公切線長 {L=sqrt(d^2-(R-r)^2)}（d≥R−r 時存在）；'
                    '內公切線長 {L=sqrt(d^2-(R+r)^2)}（只喺兩圓外離，'
                    '即 d＞R+r 時先存在）。', keep_next=True))

P.append(expand_image(image_para(FIG_PATH, width_cm=15,
                    caption='圖：外公切線與內公切線的推導（虛線 O₂C 是輔助線，平行於切線）'),
                    media))

P.append(para('推導：由圓心 O₁、O₂ 分別向切點 A、B 連半徑，半徑必垂直於切線'
              '（圓的切線性質）。過小圓心 O₂ 作大圓半徑 O₁A 的平行線，'
              '交 O₁A（外公切線）或其延長線（內公切線）於 C，'
              '咁 O₂C ∥ AB，即 {O_2C=AB=L}（公切線長）；'
              '外公切線：C 在 O₁A 上，{O_1C=R-r}；'
              '內公切線：C 在 O₁A 延長線上，{O_1C=R+r}。'
              '三角形 O₁O₂C 的直角喺 C，斜邊 {O_1O_2=d}，用勾股定理就得出公式。',
              keep_next=True))

P.append(shaded_box('範例：兩圓半徑 R=7、r=2，圓心距 d=13，求外公切線的長度。',
                    keep_next=True))
P.append(worked_example_table([
    span_row('R=7，r=2，d=13（外公切線）', why='先記下已知，求 L'),
    eq_row('{L^2}', '{d^2-(R-r)^2}', why='外公切線公式'),
    eq_row('{L^2}', '{13^2-(7-2)^2}', why='代入已知'),
    eq_row('{L^2}', '{169-25}', why='先算平方：13²=169，(7−2)²=5²=25'),
    eq_row('{L^2}', '{144}', why='相減'),
    eq_row('{L}', '{12}', why='開平方；長度取正，不用分兩支'),
    answer_row('{L=12}', why='外公切線長 12（就是熟悉嘅 5-12-13 直角三角形：'
                             'R−r=5、L=12、d=13）'),
], why_pct=0.34))

new_section = ''.join(P)

# ==================== 教師實施說明頁（放在全份最後；原稿冇呢一頁，新增） ====================
TN = ''.join(teacher_notes(
    main_design='D7 提示卡（本頁只說明新增的「四、兩圓的公切線長度」；'
                '一～三為原有內容，沿用同一套「定義框＋示意圖＋算式範例」版面）',
    aux_designs=(),
    reason='對應 S5 幾何定理與推理：公切線長度公式要求學生同時記住「先判斷 R−r 定'
           'R+r」＋「畢氏定理」兩件事，記憶檢索負荷高。D7 三件套（文字定義＋'
           '推導示意圖＋代數算式範例）並列，同時支援視覺型與符號型學生；'
           '示意圖畫出輔助線 O₂C 嘅由來，令公式唔係死背，而係睇得到點推出嚟。',
    density='全班共用',
    fading='完整推導圖＋逐步算式範例 → 只留公式框（唔畫推導圖，要求學生自己畫）→ '
           '只留一句「先判斷 R±r，再套勾股定理」→ 完全唔提示，直接讀 R、r、d 求 L。',
    iep_codes=('a3 提示題目重點',),
))

# ==================== 插入 ====================
import zipfile
with zipfile.ZipFile(DOCX) as z:
    xml = z.read('word/document.xml').decode('utf-8')

pos_section = para_start(xml, '接下來請拿本單元《課堂練習》，完成練習 A、B、C。')
pos_tail = xml.index('<w:sectPr>')

patch(DOCX, DOCX, [(pos_section, new_section), (pos_tail, TN)], media, N_SEED)
print('OK', DOCX, 'figs:', len(media.items) - N_SEED)
