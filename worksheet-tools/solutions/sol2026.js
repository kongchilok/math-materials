// 2026 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(A)　\([-2,0]\)`, parts: [ P("", [
    reg(r`工序 1 · 解 \(A\)`, r`
(x+2)(x-1) &\le 0
A &= [-2,1]
`),
    reg(r`工序 2 · 解 \(B\)`, r`
|x-1| &\ge 1
x\ge2 &\ \text{或}\ x\le0
`),
    reg(r`工序 3 · 取交集`, r`
A\cap B &= [-2,0]
`),
  ])]},

  2: { ans: r`(B)　\(\tfrac{5}{8}\)`, parts: [ P("", [
    reg(r`工序 1 · 交叉相乘`, r`
3x+5y &= 5(2y-x)
`),
    reg(r`工序 2 · 移項求比`, r`
8x &= 5y
\frac{x}{y} &= \frac{5}{8}
`),
  ])]},

  3: { ans: r`(C)　\(a-b=-2\)`, parts: [ P("", [
    reg(r`工序 1 · 整理`, r`
(3+b)x+(-a-5) &= 0
`),
    reg(r`工序 2 · 係數與常數皆 0`, r`
b &= -3
a &= -5
`),
    reg(r`工序 3 · 求 \(a-b\)`, r`
a-b &= -2
`),
  ])]},

  4: { ans: r`(E)　\(k<9\)`, parts: [ P("", [
    reg(r`工序 1 · 兩相異實根須 \(\Delta>0\)`, r`
36-4k &> 0
k &< 9
`),
  ])]},

  5: { ans: r`(D)　\(\dfrac{1+3^{1001}}{4}\)`, parts: [ P("", [
    reg(r`工序 1 · 餘式定理`, r`
\text{餘} &= f(-3)
`),
    reg(r`工序 2 · 等比和`, r`
f(-3) &= \frac{1-(-3)^{1001}}{1-(-3)}
&= \frac{1+3^{1001}}{4}
`),
  ])]},

  6: { ans: r`(C)　\(\tfrac{21}{4}\)`, parts: [ P("", [
    reg(r`工序 1 · 根與係數`, r`
a+b &= \tfrac52
ab &= \tfrac12
`),
    reg(r`工序 2 · 恆等式`, r`
a^2+b^2 &= (a+b)^2-2ab
&= \tfrac{25}{4}-1=\tfrac{21}{4}
`),
  ])]},

  7: { ans: r`(B)　\(\dfrac{x}{x-1}\)`, parts: [ P("", [
    reg(r`工序 1 · 求 \(\log_a b\)`, r`
\log_a ab=1+\log_a b &= x
\log_a b &= x-1
`),
    reg(r`工序 2 · 換底`, r`
\log_b ab &= \frac{x}{x-1}
`),
  ])]},

  8: { ans: r`(D)　\(3x+4y+16=0\)`, parts: [ P("", [
    reg(r`工序 1 · 配方求圓心`, r`
(x+1)^2+(y-3)^2 &= 25
\text{圓心} &= (-1,3)
`),
    reg(r`工序 2 · 切線斜率`, r`
k_{\text{半徑}} &= \frac{-1-3}{-4+1}=\tfrac43
k_{\text{切}} &= -\tfrac34
`),
    reg(r`工序 3 · 點斜式`, r`
y+1 &= -\tfrac34(x+4)
3x+4y+16 &= 0
`),
  ])]},

  9: { ans: r`(E)　\(f(-2)=-66\)`, parts: [ P("", [
    reg(r`工序 1 · 由 \(f(2)\) 求整體`, r`
8a+2b-36 &= -6
8a+2b &= 30
`),
    reg(r`工序 2 · 求 \(f(-2)\)`, r`
f(-2) &= -(8a+2b)-36
&= -66
`),
  ])]},

  10: { ans: r`(A)　\(180\)`, parts: [ P("", [
    reg(r`工序 1 · 3 男 2 女`, r`
C^6_3C^4_2 &= 120
`),
    reg(r`工序 2 · 4 男 1 女`, r`
C^6_4C^4_1 &= 60
`),
    reg(r`工序 3 · 相加`, r`
120+60 &= 180
`),
  ])]},

  11: { ans: r`(D)　\(\{0,3\}\)`, parts: [ P("", [
    reg(r`工序 1 · 移項平方`, r`
x+2 &= \sqrt{3x^2-2x+4}
`),
    reg(r`工序 2 · 再平方`, r`
2x(x-3) &= 0
x &= 0\ \text{或}\ 3
`),
    reg(r`工序 3 · 驗根`, r`
&\text{皆成立}\Rightarrow\{0,3\}
`),
  ])]},

  12: { ans: r`(A)　\(-\tfrac{1}{7}\)`, parts: [ P("", [
    reg(r`工序 1 · 化簡角度`, r`
\tan\!\left(\tfrac{9\pi}{4}+x\right) &= \tan\!\left(\tfrac{\pi}{4}+x\right)=-7
`),
    reg(r`工序 2 · 目標化為倒數`, r`
\frac{1-\sin2x}{\cos2x} &= \frac{1-\tan x}{1+\tan x}
&= \frac{1}{\tan\!\left(\frac{\pi}{4}+x\right)}
`),
    reg(r`工序 3 · 求值`, r`
&= \frac{1}{-7}=-\tfrac17
`),
  ])]},

  13: { ans: r`(E)　\(a_5+a_7=63\)`, parts: [ P("", [
    reg(r`工序 1 · 由第一式求 \(q\)`, r`
2a(1+q+q^2) &= a(q^3-1)
q &= 3
`),
    reg(r`工序 2 · 由第二式求 \(a\)`, r`
a_3+a_5=90a &= 7
a &= \tfrac{7}{90}
`),
    reg(r`工序 3 · 求目標`, r`
a_5+a_7 &= 810a=63
`),
  ])]},

  14: { ans: r`(B)　\(a\le-2\)`, parts: [ P("", [
    reg(r`工序 1 · 對稱軸`, r`
x &= \frac{a-1}{3}
`),
    reg(r`工序 2 · 遞減條件（軸 \(\le-1\)）`, r`
\frac{a-1}{3} &\le -1
a &\le -2
`),
  ])]},

  15: { ans: r`(C)　\([0,\infty)\)`, parts: [ P("", [
    reg(r`工序 1 · 避開負輸出`, r`
t\in(-4,0) &\Rightarrow f(t)<0\ \text{須避開}
`),
    reg(r`工序 2 · 覆蓋 \([0,\infty)\)`, r`
t\ge0 &\Rightarrow f\ \text{覆蓋}\ [0,\infty)
`),
    reg(r`工序 3 · 連續區間結論`, r`
g\ \text{值域} &= [0,\infty)
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(P_0=\tfrac1{24},P_1=\tfrac14,P_2=\tfrac{11}{24},P_3=\tfrac14\)　(b) \(\tfrac{9}{14}\)`, parts: [
    P(r`（a）A 隊各分數機率`, [
      reg(r`工序 1 · 逐一列舉`, r`
P(0) &= \tfrac{1}{24}
P(1) &= \tfrac{1}{4}
P(2) &= \tfrac{11}{24}
P(3) &= \tfrac{1}{4}
`),
    ]),
    P(r`（b）條件機率 \(B>A\)`, [
      reg(r`工序 2 · 共 3 分機率`, r`
P(\text{總}3) &= \tfrac{49}{256}
`),
      reg(r`工序 3 · \(B>A\) 部分`, r`
P(B>A,\text{總}3) &= \tfrac{63}{512}
`),
      reg(r`工序 4 · 相除`, r`
P &= \frac{63/512}{49/256}=\tfrac{9}{14}
`),
    ]),
  ]},

  2: { ans: r`(a) \(P(0,5),Q(2,9)\)　(b) \(M\!\left(\tfrac57,0\right)\)`, parts: [
    P(r`（a）求 \(P,Q\)`, [
      reg(r`工序 1 · 交點與頂點`, r`
P &= (0,5)
Q &= (2,9)
`),
    ]),
    P(r`（b）求 \(M\)`, [
      reg(r`工序 2 · 作對稱點與連線`, r`
P' &= (0,-5)
P'Q:\ y &= 7x-5
`),
      reg(r`工序 3 · 與 \(x\) 軸交`, r`
y=0 &\Rightarrow x=\tfrac57
M &= \left(\tfrac57,0\right)
`),
    ]),
  ]},

  3: { ans: r`(a) \(a_n=8n+4\)　(b) \(T_n=\tfrac{3}{16}-\tfrac{1}{8(n+1)}-\tfrac{1}{8(n+2)}\)　(c) 見證明`, parts: [
    P(r`（a）求 \(a_n\)`, [
      reg(r`工序 1 · 求首項與公差`, r`
a_1=12,\ d &= 8
a_n &= 8n+4
`),
    ]),
    P(r`（b）求 \(T_n\)`, [
      reg(r`工序 2 · 求 \(S_n\) 並裂項`, r`
S_n &= 4n(n+2)
b_n &= \tfrac18\!\left(\tfrac1n-\tfrac1{n+2}\right)
`),
      reg(r`工序 3 · 裂項相消`, r`
T_n &= \tfrac{3}{16}-\tfrac{1}{8(n+1)}-\tfrac{1}{8(n+2)}
`),
    ]),
    P(r`（c）求證範圍`, [
      reg(r`工序 4 · 上界`, r`
T_n &< \tfrac{3}{16}\ (\text{減正數})
`),
      reg(r`工序 5 · 下界`, r`
T_n\ \text{遞增},\ T_1 &= \tfrac{1}{12}
\tfrac{1}{12}\le T_n &< \tfrac{3}{16}\ \square
`),
    ]),
  ]},

  4: { ans: r`(a) \(\dfrac{x^2}{4}-\dfrac{y^2}{2}=1\)　(b) \(AM\perp BM\)（得證）`, parts: [
    P(r`（a）求 \(E\) 的方程`, [
      reg(r`工序 1 · 離心率關係`, r`
e^2=\tfrac32 &\Rightarrow a^2=2b^2
`),
      reg(r`工序 2 · 代點求 \(a^2,b^2\)`, r`
b^2=2,\ a^2 &= 4
\frac{x^2}{4}-\frac{y^2}{2} &= 1
`),
    ]),
    P(r`（b）證 \(AM\perp BM\)`, [
      reg(r`工序 3 · 聯立與韋達`, r`
x^2-24x+76 &= 0
x_1+x_2=24,\ x_1x_2 &= 76
`),
      reg(r`工序 4 · 驗垂直`, r`
\vec{MA}\cdot\vec{MB} &= 2x_1x_2-8(x_1+x_2)+40
&= 152-192+40=0
&\Rightarrow AM\perp BM
`),
    ]),
  ]},

  5: { ans: r`(a) \(x_2=1,x_3=\tfrac34\)　(b) \(x_n=\dfrac{3}{n+1}\)　(c) 最大值 \(\dfrac{\sqrt3}{2}\)`, parts: [
    P(r`（a）求 \(x_2,x_3\)`, [
      reg(r`工序 1 · 逐步代入`, r`
x_2 &= 1
x_3 &= \tfrac34
`),
    ]),
    P(r`（b）猜想並證明`, [
      reg(r`工序 2 · 猜想`, r`
x_n &= \frac{3}{n+1}
`),
      reg(r`工序 3 · 歸納步`, r`
x_{k+1} &= \frac{3x_k}{x_k+3}=\frac{3}{k+2}\ \square
`),
    ]),
    P(r`（c）求 \(g(x)\) 最大值`, [
      reg(r`工序 4 · 化簡 \(g\)`, r`
g(x) &= \frac{3x}{x^2+3}=\frac{3}{x+\frac3x}
`),
      reg(r`工序 5 · 算幾不等式`, r`
x+\tfrac3x &\ge 2\sqrt3
g(x) &\le \frac{3}{2\sqrt3}=\frac{\sqrt3}{2}
`),
    ]),
  ]},
};

module.exports = { choice, solution };
