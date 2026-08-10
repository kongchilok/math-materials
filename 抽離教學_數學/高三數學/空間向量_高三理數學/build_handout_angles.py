# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 空間角的計算：線面角與二面角（對應課本 1.2.3+1.2.4）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間角的計算'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、直線與平面所成的角'))
P.append(para('定義：一條直線 l 與佢喺平面 α 內嘅射影所成嘅角，範圍係 0° 到 90° 之間。'))
P.append(shaded_box('設直線 l 的方向向量是 {vec(v)}，平面 α 的法向量是 {vec(n)}：{sinθ=|fn(cos)⟨vec(v),vec(n)⟩|=frac(|vec(v)·vec(n)|,|vec(v)|*|vec(n)|)}'))
P.append(para('注意：呢度用嘅係 {sinθ}（唔係 {fn(cos)θ}）！因為「方向向量與法向量的夾角」同「直線與平面所成角」係互餘關係——一個變大，另一個就變細，加埋等於90°。'))
P.append(blank())

P.append(heading('二、二面角'))
P.append(para('定義：由一條公共棱發出嘅兩個半平面組成嘅圖形，範圍係 0° 到 180° 之間。'))
P.append(shaded_box('分別求兩個面嘅法向量 {vec(n_1)}、{vec(n_2)}：{|fn(cos)θ|=|fn(cos)⟨vec(n_1),vec(n_2)⟩|=frac(|vec(n_1)·vec(n_2)|,|vec(n_1)|*|vec(n_2)|)}'))
P.append(para('【非常重要】：呢條公式淨係俾到 {|fn(cos)θ|}，即係話真正嘅二面角可能係計出嚟嗰個銳角，都可能係佢嘅補角（180°減嗰個銳角）。一定要睇返個立體圖形嘅實際形狀，判斷二面角本身係銳角定係鈍角，先至揀啱嗰個——唔可以計完數就直接當答案，呢步判斷唔可以省略。'))
P.append(blank())

P.append(heading('三、範例：求線面角'))
P.append(para('正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系（同之前幾課一樣）。求 {vec(AB_1)} 與底面 {ABCD} 所成角的正弦值。'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u4_fig1.png'), width_cm=6.5),
     '已知：正方體棱長2，底面ABCD法向量n=(0,0,1)。要求：AB₁與底面ABCD所成角θ的正弦值。'),
], media=media))
P.append(worked_example_table([
    span_row('① 底面 {ABCD} 就是 {z=0} 平面，法向量可以直接取 {vec(n)=(0,0,1)}（z軸方向）'),
    eq_row('{vec(AB_1)}', '{A(2,0,0)}、{B_1(2,2,2)}，{vec(AB_1)=(0,2,2)}', '② 寫出坐標，求 AB₁'),
    answer_row('{sinθ=frac(|vec(AB_1)·vec(n)|,|vec(AB_1)|*|vec(n)|)=frac(|0+0+2|,sqrt(0+4+4)*1)=frac(2,2*sqrt(2))=frac(1,sqrt(2))=frac(sqrt(2),2)}', '③ 代入公式'),
    span_row('④ 所以正弦值是 {frac(sqrt(2),2)}，即 {θ=45°}。（可以用返中二學過嘅直角三角形驗算：AB是底邊、{BB_1}是高，兩者都是棱長2，{tanθ=frac(2,2)=1}，一樣得45°）'),
], why_pct=0.36))
P.append(blank())

P.append(heading('四、範例：求二面角（示範判斷銳鈍角嗰步）'))
P.append(para('求二面角 D₁-AC-B（棱是AC，一邊嘅半平面有 {D_1}，另一邊有 B）的大小。'))
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u4_fig1.png'), width_cm=6.5),
     '已知：{D_1} 喺正方體上方、B 喺底面，兩者分處AC兩側。要求：判斷二面角 D₁-AC-B 是銳角定係鈍角，再求大小。'),
], media=media))
P.append(worked_example_table([
    span_row('① 分別求平面 {ACD_1} 和平面 {ACB} 的法向量：平面 {ACD_1} 上一課求過 {vec(n_1)=(1,1,1)}；平面 {ACB} 就是底面，{vec(n_2)=(0,0,1)}'),
    answer_row('{|fn(cos)θ|=frac(|vec(n_1)·vec(n_2)|,|vec(n_1)|*|vec(n_2)|)=frac(|1|,sqrt(3)*1)=frac(1,sqrt(3))=frac(sqrt(3),3)}', '② 代入公式'),
    span_row('③ 判斷銳鈍角：{D_1} 喺正方體上方、B 喺底面，兩者分處 {AC} 兩側，張開嘅角明顯超過90°（睇返個正方體嘅圖），所以呢個二面角係鈍角。'),
    span_row('④ 所以二面角 {=180°-fn(arccos)frac(sqrt(3),3)≈125.3°}（唔係嗰個約54.7°嘅銳角）。'),
], why_pct=0.36))
P.append(shaded_box('提提大家：呢度兩個範例啱啱好都係鈍角，但唔代表二面角例牌都係鈍角——每一題都要獨立判斷，唔可以憑上次經驗直接當晒。'))
P.append(blank())

P.append(shaded_box('接下來請拿《空間角的計算——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D7 判定定理卡',
    aux_designs=('D5 圖文雙軌', 'D2 手順卡'),
    reason='S9 立體幾何與空間：線面角用sinθ、二面角用|cosθ|，兩條公式極易撞埋（研究明確警告的'
           '記憶檢索失敗），以D7提示卡把「觸發語（問乜嘢角）→用邊條公式→sin定cos」三件套個人化；'
           '二面角嘅銳鈍角判斷一定要對住圖先做到，用D5圖文雙軌；四步驟固定框架以D2手順卡落地。',
    density='抽離小班（Tier 2）',
    fading='判定卡完整版（放桌面）→ 只留「線面角=sin／二面角=|cos|」一句提示 → 移除',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_空間角的計算_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
