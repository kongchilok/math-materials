# -*- coding: utf-8 -*-
"""IEP第8/9點 —— 高三理組（精簡版：導數＋積分＋空間向量＋四校複習＋矩陣，全學年通用草稿）"""
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\macau-iep-math-goals\scripts")
from fill_iep import open_iep, set_subject, set_curriculum_adaptation, set_service, set_long_term, set_short_term, save_iep

doc = open_iep()
set_subject(doc, '數學')
set_curriculum_adaptation(doc, '與普通生課程無異')

set_service(doc,
    content='因應學生於高三理科數學課堂進度所需時間較長，以抽離小班將導數、積分、空間向量、矩陣等單元內容拆解為較小步驟教授，並配合歷屆四校聯考試題分類索引進行單元複習，鞏固基礎運算與解題步驟習慣。',
    goals=[
        '1. 能在提示步驟卡協助下，完成課堂例題的基礎運算題',
        '2. 能說出解題的關鍵步驟',
        '3. 能使用計算機檢查運算結果',
    ])

set_long_term(doc, [
    '1. 能求基本初等函數的導數（含隱函數求導）',
    '2. 能運用導數判斷函數的單調性、極值與凹凸性',
    '3. 能求函數的不定積分',
    '4. 能計算定積分並運用於求面積',
    '5. 能進行空間向量的運算',
    '6. 能運用空間向量解決立體幾何問題',
    '7. 能運用歷屆試題分類索引進行四校聯考單元複習',
    '8. 能進行矩陣的基本運算並求逆矩陣',
    '9. 能用矩陣方法解線性方程組及求多項式最大公因式',
])

ST = [
    # 長期1．導數（含隱函數求導）
    {'goal': '1-1. 能根據導數定義的極限式，說出導數表示的幾何意義（切線斜率）', 'assess': 'A', 'aid': 'a3'},
    {'goal': '1-2. 能代入基本初等函數的求導公式，求出函數的導數', 'assess': 'B', 'aid': 'a6,b5'},
    {'goal': '1-3. 能運用四則運算求導法則，求兩個函數和、差、積、商的導數', 'assess': 'B', 'aid': 'a3,a6,c3'},
    {'goal': '1-4. 能對簡單的隱函數方程兩邊求導，解出dy/dx', 'assess': 'B', 'aid': 'a3,a6,c3'},
    # 長期2．導數的應用
    {'goal': '2-1. 能透過判斷一階導數的正負，說出函數的遞增或遞減區間', 'assess': 'B', 'aid': 'a3,a6'},
    {'goal': '2-2. 能透過一階導數等於零的點，求出函數的極值', 'assess': 'B', 'aid': 'a3,a6,c3'},
    {'goal': '2-3. 能透過判斷二階導數的正負，說出函數圖像的凹凸區間及拐點', 'assess': 'D', 'aid': 'a3'},
    # 長期3．不定積分
    {'goal': '3-1. 能根據不定積分與導數的互逆關係，寫出基本初等函數的不定積分公式', 'assess': 'A', 'aid': 'a3'},
    {'goal': '3-2. 能運用不定積分的運算法則（和差、常數倍），求出函數的不定積分', 'assess': 'B', 'aid': 'a3,a6,c3'},
    # 長期4．定積分
    {'goal': '4-1. 能代入微積分基本定理，計算簡單函數的定積分', 'assess': 'B', 'aid': 'a6,b5,c3'},
    {'goal': '4-2. 能運用定積分計算曲線與坐標軸所圍成的面積', 'assess': 'B', 'aid': 'a3,c3'},
    # 長期5．空間向量的運算
    {'goal': '5-1. 能根據三角形法則，把兩個首尾相接的空間向量化簡為一個向量', 'assess': 'B', 'aid': 'a6'},
    {'goal': '5-2. 能代入數量積公式，求出兩個已知坐標的空間向量的數量積', 'assess': 'B', 'aid': 'a6,b5'},
    {'goal': '5-3. 能代入公式求出已知坐標的空間向量的模', 'assess': 'B', 'aid': 'a6,b5'},
    {'goal': '5-4. 能代入兩點距離公式求出空間中兩點之間的距離', 'assess': 'B', 'aid': 'a6,b5'},
    # 長期6．空間向量解決立體幾何問題
    {'goal': '6-1. 給定平面內兩條相交直線的方向向量，能代入方程組解出平面的法向量', 'assess': 'B', 'aid': 'a3,a6,c3'},
    {'goal': '6-2. 能代入線面角公式，求直線與平面所成角的正弦值', 'assess': 'B', 'aid': 'a3,a6,b5'},
    {'goal': '6-3. 能代入二面角公式，求兩平面法向量夾角餘弦值的絕對值', 'assess': 'B', 'aid': 'a3,a6,b5'},
    {'goal': '6-4. 能代入點到平面距離公式，求點到平面的距離', 'assess': 'B', 'aid': 'a3,a6,b5'},
    # 長期7．四校複習
    {'goal': '7-1. 能使用歷屆試題分類索引，查出指定單元的歷屆試題題號', 'assess': 'C', 'aid': ''},
    {'goal': '7-2. 能完成指定高頻單元（如二次方程及二次函數、數列、解析幾何）的基礎選擇題', 'assess': 'B', 'aid': 'a3,c3'},
    # 長期8．矩陣的基本運算並求逆矩陣
    {'goal': '8-1. 能對兩個同階矩陣進行加法或減法運算', 'assess': 'B', 'aid': 'a6'},
    {'goal': '8-2. 能對矩陣進行純量乘法運算', 'assess': 'B', 'aid': 'a6'},
    {'goal': '8-3. 能對兩個可相乘的矩陣進行矩陣乘法運算', 'assess': 'B', 'aid': 'a3,a6,c3'},
    {'goal': '8-4. 能代入公式計算2×2矩陣的行列式，並判斷矩陣是否存在逆矩陣', 'assess': 'B', 'aid': 'a3,a6,b5'},
    {'goal': '8-5. 能代入公式求2×2矩陣的逆矩陣', 'assess': 'B', 'aid': 'a3,a6,b5'},
    {'goal': '8-6. 能運用逆矩陣解形如AX=B的矩陣方程', 'assess': 'B', 'aid': 'a3,a6,c3'},
    # 長期9．矩陣方法解線性方程組及多項式最大公因式
    {'goal': '9-1. 能運用高斯消元法或克拉瑪法則解二元一次方程組', 'assess': 'B', 'aid': 'a3,a6,c3'},
    {'goal': '9-2. 能透過係數列相減消去最高次項，求出兩個同次多項式的最大公因式', 'assess': 'B', 'aid': 'a3,a6'},
]
assert len(ST) == 29, len(ST)
set_short_term(doc, ST)

out = save_iep(doc, r'C:\Users\KongChiLok\notebookLM\抽離教學_數學\高三數學\IEP第8-9點_數學科_高三理組_全學年_通用草稿.docx')
with open(r'C:\Users\KONGCH~1\AppData\Local\Temp\claude\C--Users-KongChiLok-notebookLM\a6dcd49a-7c23-45c9-8b4e-576a5a0e40a8\scratchpad\iep_out_path.txt', 'w', encoding='utf-8') as f:
    f.write(out)
print('OK')
