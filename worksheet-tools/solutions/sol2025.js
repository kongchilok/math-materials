// 2025 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(A)　\(\{-4,3\}\)`, parts: [ P("", [
    reg(r`工序 1 · 代入測試 \(B\) 各數`, r`
x=-4 &:\ 16-12-4=0\ \text{（合）}
x=-2 &:\ -6<0\ \text{（不合）}
x=0 &:\ -4<0\ \text{（不合）}
x=3 &:\ 14\ge0\ \text{（合）}
`),
    reg(r`工序 2 · 交集`, r`
A\cap B &= \{-4,3\}
`),
  ])]},

  2: { ans: r`(D)　\(16\)`, parts: [ P("", [
    reg(r`工序 1 · 倒數根的和與積`, r`
\tfrac1\alpha+\tfrac1\beta &= -1
\tfrac1\alpha\cdot\tfrac1\beta &= -\tfrac12
`),
    reg(r`工序 2 · 反推 \(\alpha+\beta\)`, r`
\alpha+\beta &= \frac{-1}{-1/2}=2
`),
    reg(r`工序 3 · 合併指數`, r`
2^{\alpha+1}\cdot2^{\beta+1} &= 2^{\alpha+\beta+2}
&= 2^4=16
`),
  ])]},

  3: { ans: r`(A)　增加 \(18.3\%\)`, parts: [ P("", [
    reg(r`工序 1 · 具體化代入`, r`
V_0 &= \pi(10)^2(10)=1000\pi
`),
    reg(r`工序 2 · 新值`, r`
V_1 &= \pi(13)^2(7)=1183\pi
`),
    reg(r`工序 3 · 變化率`, r`
\frac{1183-1000}{1000} &= 18.3\%
`),
  ])]},

  4: { ans: r`(C)　\(m-1\)`, parts: [ P("", [
    reg(r`工序 1 · 上下同乘 \(m^{1/2}\)`, r`
\text{分子} &= m^2-1
\text{分母} &= m+1
`),
    reg(r`工序 2 · 平方差約分`, r`
\frac{m^2-1}{m+1} &= m-1
`),
  ])]},

  5: { ans: r`(D)　\(q-p-1\)`, parts: [ P("", [
    reg(r`工序 1 · 除變減`, r`
\log_2 0.7 &= \log_2 7-\log_2 10
`),
    reg(r`工序 2 · 展開（\(10=2\times5\)）`, r`
&= q-(1+p)
&= q-p-1
`),
  ])]},

  6: { ans: r`(E)　\(\{-1<x<2\}\cup\{3<x<6\}\)`, parts: [ P("", [
    reg(r`工序 1 · 左不等式`, r`
x^2-5x+6 &> 0
x<2 &\ \text{或}\ x>3
`),
    reg(r`工序 2 · 右不等式`, r`
x^2-5x-6 &< 0
-1 &< x < 6
`),
    reg(r`工序 3 · 取交集`, r`
&-1<x<2\ \text{或}\ 3<x<6
`),
  ])]},

  7: { ans: r`(C)　\(1440\)`, parts: [ P("", [
    reg(r`工序 1 · 女孩全排`, r`
4! &= 24
`),
    reg(r`工序 2 · 插空放男（5 隙取 3）`, r`
P^5_3 &= 60
`),
    reg(r`工序 3 · 相乘`, r`
24\times60 &= 1440
`),
  ])]},

  8: { ans: r`(C)　\(8\)`, parts: [ P("", [
    reg(r`工序 1 · 中位數求 \(x\)`, r`
\frac{(x-4)+(x+2)}{2} &= 8
x &= 9
`),
    reg(r`工序 2 · 平均`, r`
\bar{x} &= \frac{6x-6}{6}=x-1
&= 8
`),
  ])]},

  9: { ans: r`(B)　\(84\)`, parts: [ P("", [
    reg(r`工序 1 · 第一路徑`, r`
x\cdot x^3y^5 &\Rightarrow \binom{8}{5}=56
`),
    reg(r`工序 2 · 第二路徑`, r`
\tfrac{y^3}{x^2}\cdot x^6y^2 &\Rightarrow \binom{8}{2}=28
`),
    reg(r`工序 3 · 相加`, r`
56+28 &= 84
`),
  ])]},

  10: { ans: r`(E)　\(2\sqrt2\)`, parts: [ P("", [
    reg(r`工序 1 · 配方求圓`, r`
(x-2)^2+y^2 &= 4
\text{圓心}(2,0),\ r &= 2
`),
    reg(r`工序 2 · 求 \(d\) 與半弦`, r`
d &= \sqrt{1+1}=\sqrt2
\text{半弦} &= \sqrt{4-2}=\sqrt2
`),
    reg(r`工序 3 · 最短弦長`, r`
\text{弦長} &= 2\sqrt2
`),
  ])]},

  11: { ans: r`(E)　\(p=32\)`, parts: [ P("", [
    reg(r`工序 1 · 用定義（到準線）`, r`
\tfrac{p}{4}+7 &= 15
\tfrac{p}{4} &= 8
`),
    reg(r`工序 2 · 求 \(p\)`, r`
p &= 32
`),
  ])]},

  12: { ans: r`(D)　\(\tfrac{58}{243}\)`, parts: [ P("", [
    reg(r`工序 1 · 列舉 \(J+A=4\)`, r`
J3A1 &= \tfrac{6}{729}
J2A2 &= \tfrac{72}{729}
J1A3 &= \tfrac{96}{729}
`),
    reg(r`工序 2 · 相加`, r`
\frac{174}{729} &= \tfrac{58}{243}
`),
  ])]},

  13: { ans: r`(B)　\(a_7=-8\)`, parts: [ P("", [
    reg(r`工序 1 · 用 \(a_1=4,d\) 表示`, r`
S_2=8+d,\ S_3 &= 12+3d
S_4 &= 16+6d
`),
    reg(r`工序 2 · 代入解 \(d\)`, r`
2S_3^2 &= 3S_2S_4
d &= -2
`),
    reg(r`工序 3 · 求 \(a_7\)`, r`
a_7 &= 4+6(-2)=-8
`),
  ])]},

  14: { ans: r`(D)　最大值 \(=10\)`, parts: [ P("", [
    reg(r`工序 1 · 求頂點`, r`
&\left(\tfrac{11}{3},-1\right),(-3,-1),(1,1)
`),
    reg(r`工序 2 · 代入 \(z=3x+y\)`, r`
z &= 10,\ -10,\ 4
`),
    reg(r`工序 3 · 取最大`, r`
z_{\max} &= 10
`),
  ])]},

  15: { ans: r`(B)　（B 不正確）`, parts: [ P("", [
    reg(r`工序 1 · 平移到 \([4,6]\)`, r`
&\text{加 4；距 5 越近，值越小}
`),
    reg(r`工序 2 · 檢項 B`, r`
\sin\tfrac{\pi}{3},\cos\tfrac{\pi}{3} &\to 4.866,\ 4.5
4.866\ \text{近 5} &\Rightarrow f(4.866)<f(4.5)
`),
    reg(r`工序 3 · 結論`, r`
&\text{B 寫成 }>\text{，故不正確}
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(a_n=2n+1,\ b_n=2\cdot3^{n-1}\)　(b) \(T_n=2n\cdot3^n\)`, parts: [
    P(r`（a）求 \(a_n,b_n\)`, [
      reg(r`工序 1 · 由和求 \(a_n\)`, r`
a_1 &= 3
a_n &= S_n-S_{n-1}=2n+1
`),
      reg(r`工序 2 · 由 \(b_3=2a_4\) 求 \(b_n\)`, r`
b_3=2a_4 &= 18
q &= 3
b_n &= 2\cdot3^{n-1}
`),
    ]),
    P(r`（b）求 \(T_n\)`, [
      reg(r`工序 3 · 錯位相減`, r`
c_n &= (2n+1)\cdot2\cdot3^{n-1}
2T_n &= 4n\cdot3^n
`),
      reg(r`工序 4 · 結果`, r`
T_n &= 2n\cdot3^n
`),
    ]),
  ]},

  2: { ans: r`(a) \(p=4,q=6,r=3\)　(b) \(x=\dfrac{-3\pm\sqrt3}{2}\)`, parts: [
    P(r`（a）求 \(p,q,r\)`, [
      reg(r`工序 1 · 比較頭尾係數`, r`
2p=8 &\Rightarrow p=4
3r=9 &\Rightarrow r=3
`),
      reg(r`工序 2 · 餘式定理求 \(q\)`, r`
f(-1)=10(5-q) &= -10
q &= 6
`),
    ]),
    P(r`（b）求實根`, [
      reg(r`工序 3 · 第一括號（無實根）`, r`
4x^2-3x+3 &:\ \Delta=-39<0
`),
      reg(r`工序 4 · 第二括號`, r`
2x^2+6x+3 &= 0
x &= \frac{-3\pm\sqrt3}{2}
`),
    ]),
  ]},

  3: { ans: r`(a) \(\cos C=\tfrac45\)　(b) \(\sin2B=-\tfrac{7}{25}\)`, parts: [
    P(r`（a）求 \(\cos C\)`, [
      reg(r`工序 1 · 化為 \(\cos C\) 二次`, r`
\sin C &= 3(1-\cos C)
5\cos^2C-9\cos C+4 &= 0
`),
      reg(r`工序 2 · 解`, r`
(5\cos C-4)(\cos C-1) &= 0
\cos C &= \tfrac45
`),
    ]),
    P(r`（b）求 \(\sin2B\)`, [
      reg(r`工序 3 · 角度關係`, r`
2B &= 270^\circ-2C
\sin2B &= -\cos2C
`),
      reg(r`工序 4 · 求值`, r`
\cos2C &= 2\cos^2C-1=\tfrac{7}{25}
\sin2B &= -\tfrac{7}{25}
`),
    ]),
  ]},

  4: { ans: r`(a)(b)(c) 見證明`, parts: [
    P(r`（a）\(\triangle DEG\sim\triangle DFE\)`, [
      reg(r`工序 1 · AA 相似`, r`
\angle DEG=\angle DFE,\ \angle D &\ \text{共用}
\triangle DEG &\sim\triangle DFE
`),
    ]),
    P(r`（b）\(\triangle DEF\sim\triangle BDE\)`, [
      reg(r`工序 2 · 由等腰推等角`, r`
AD=AE &\Rightarrow \angle ADE=\angle AED
\angle EFD &= \angle DEB
\triangle DEF &\sim\triangle BDE
`),
    ]),
    P(r`（c）\(DG\cdot DF=DB\cdot EF\)`, [
      reg(r`工序 3 · 連立兩比例`, r`
DE^2 &= DG\cdot DF
DE^2 &= DB\cdot EF
DG\cdot DF &= DB\cdot EF\ \square
`),
    ]),
  ]},

  5: { ans: r`(a) \(\dfrac{x^2}{8}+\dfrac{y^2}{4}=1\)　(b) \(k_{OD}=-\dfrac{1}{2k}\)`, parts: [
    P(r`（a）求軌跡 \(C\)`, [
      reg(r`工序 1 · 斜率積化軌跡`, r`
\frac{y^2}{x^2-8} &= -\tfrac12
\frac{x^2}{8}+\frac{y^2}{4} &= 1
`),
    ]),
    P(r`（b）求 \(OD\) 斜率`, [
      reg(r`工序 2 · 聯立得二次`, r`
(2k^2+1)x^2+4kbx+2b^2-8 &= 0
`),
      reg(r`工序 3 · 韋達求中點`, r`
x_D &= -\frac{2kb}{2k^2+1}
y_D &= \frac{b}{2k^2+1}
`),
      reg(r`工序 4 · \(OD\) 斜率`, r`
\frac{y_D}{x_D} &= -\frac{1}{2k}
`),
    ]),
  ]},
};

module.exports = { choice, solution };
