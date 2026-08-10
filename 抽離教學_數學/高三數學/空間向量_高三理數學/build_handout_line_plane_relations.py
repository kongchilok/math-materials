# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 向量法判斷直線與平面的位置關係（對應課本 1.2.1+1.2.2）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '向量法判斷直線與平面的位置關係'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、直線的方向向量'))
P.append(para('一條直線 l 上任取兩點 A、B，{vec(AB)}（或者佢嘅任何非零倍數）就叫做 l 的一個「方向向量」。一條直線嘅方向向量唔係唯一嘅，但方向係唯一確定嘅。'))
P.append(blank())

P.append(heading('二、線線角、線線垂直'))
P.append(para('兩條直線 {l_1}、{l_2} 嘅方向向量分別係 {vec(v_1)}、{vec(v_2)}：'))
P.append(shaded_box('線線角（規定喺 0° 到 90° 之間）：{fn(cos)θ=|fn(cos)⟨vec(v_1),vec(v_2)⟩|=frac(|vec(v_1)·vec(v_2)|,|vec(v_1)|*|vec(v_2)|)}'))
P.append(para('注意最外層嗰對絕對值符號：向量夾角可以去到180°，但線線角規定唔超過90°，所以要加絕對值，確保個答案唔會變負。'))
P.append(shaded_box('線線垂直：{l_1⊥l_2} ⟺ {vec(v_1)·vec(v_2)=0}'))
P.append(blank())

P.append(heading('三、平面的法向量'))
P.append(para('若一條直線垂直於平面 α，咁呢條直線嘅方向向量 {vec(n)} 就叫做平面 α 嘅「法向量」，記做 {vec(n)⊥α}。'))
P.append(shaded_box('法向量唔係唯一嘅（任何非零倍數都仲係法向量），但方向係唯一確定嘅——所以通常淨係要搵一個就夠。'))
P.append(para('求法：喺平面內揾兩個不共線嘅向量 {vec(a)}、{vec(b)}，設 {vec(n)=(x,y,z)}，解聯立方程 {vec(n)·vec(a)=0} 同 {vec(n)·vec(b)=0}（未知數比方程多一條，可以自由設一個變量嘅值）。'))
P.append(blank())

P.append(heading('四、法向量最直接的用途：判斷線面垂直'))
P.append(shaded_box('若直線 l 嘅方向向量 {vec(v)} 同平面 α 嘅法向量 {vec(n)} 平行（{vec(v)∥vec(n)}），咁 {l⊥α}。'))
P.append(blank())

P.append(heading('五、範例：求平面的法向量'))
P.append(para('正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系（同上一課一樣）。求平面 {ACD_1} 的一個法向量。'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u4_fig1.png'), width_cm=6.5),
     '已知：正方體棱長2，D為原點。要求：平面 ACD₁（由A、C、D₁三點決定）的一個法向量n。'),
], media=media))
P.append(worked_example_table([
    span_row('① 寫出坐標：{A(2,0,0)}、{C(0,2,0)}、{D_1(0,0,2)}，喺平面內揾兩個向量：{vec(AC)=(-2,2,0)}，{vec(AD_1)=(-2,0,2)}'),
    span_row('② 設 {vec(n)=(x,y,z)}，列聯立方程：{vec(n)·vec(AC)=0} → {-2x+2y=0}；{vec(n)·vec(AD_1)=0} → {-2x+2z=0}'),
    span_row('③ 解方程：由第一式 {x=y}；由第二式 {x=z}。自由設 {x=1}，得 {y=1}、{z=1}'),
    answer_row('{vec(n)=(1,1,1)}', '④ 就是平面 {ACD_1} 的一個法向量'),
    span_row('驗算：{vec(n)·vec(AC)=-2+2+0=0}✓，{vec(n)·vec(AD_1)=-2+0+2=0}✓'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box('接下來請拿《向量法判斷直線與平面的位置關係——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D7 判定定理卡',
    aux_designs=('D5 圖文雙軌', 'D2 手順卡'),
    reason='S9 立體幾何與空間：本課是「線面關係判定」系列的起點，四種線面/面面平行垂直判定'
           '（見《工具卡_空間向量判定定理卡》）要同時提取多條判定條件，記憶檢索負荷高，'
           '以D7提示卡把「觸發語→判定條件→公式」三件套個人化、桌面化；求法向量的四步驟'
           '仍需要對住圖先睇到邊兩個向量喺平面內（D5），並以D2手順卡落地。',
    density='抽離小班（Tier 2）',
    fading='判定卡完整版（放桌面）→ 只留四種判定的公式清單 → 移除，學生自己判斷用邊條公式',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_向量法判斷直線與平面的位置關係_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
