// 2019 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(A)　\(\{x:-2<x<3\}\)`, parts: [ P("", [
    reg(r`工序 1 · 因式分解`, r`
x^2-x-6 &= (x-3)(x+2)
`),
    reg(r`工序 2 · 解不等式（取兩根間）`, r`
(x-3)(x+2) &< 0
-2 &< x < 3
`),
  ])]},

  2: { ans: r`(E)　增加 \(87.5\%\)`, parts: [ P("", [
    reg(r`工序 1 · 建立變分式`, r`
x &= k\dfrac{\sqrt{m}}{n^2}
`),
    reg(r`工序 2 · 代入變化`, r`
\sqrt{1.44m} &= 1.2\sqrt{m}
(0.8n)^2 &= 0.64n^2
`),
    reg(r`工序 3 · 求倍數`, r`
x' &= \dfrac{1.2}{0.64}x
&= 1.875x
`),
    reg(r`工序 4 · 百分比`, r`
\Delta x &= 87.5\%
`),
  ])]},

  3: { ans: r`(C)　\(a+b=5\)`, parts: [ P("", [
    reg(r`工序 1 · 設商展開`, r`
x^3+4x^2+bx+3 &= (x^2+ax+1)(x+c)
&= x^3+(a+c)x^2+(ac+1)x+c
`),
    reg(r`工序 2 · 對照係數`, r`
c &= 3
a &= 4-c
&= 1
b &= ac+1
&= 4
`),
    reg(r`工序 3 · 求和`, r`
a+b &= 5
`),
  ])]},

  4: { ans: r`(D)　\(6-\sqrt{35}\)`, parts: [ P("", [
    reg(r`工序 1 · 配對提一個因式`, r`
\text{原式} &= (6-\sqrt{35})\big[(6-\sqrt{35})(6+\sqrt{35})\big]^{99}
`),
    reg(r`工序 2 · 平方差`, r`
(6-\sqrt{35})(6+\sqrt{35}) &= 36-35
&= 1
`),
    reg(r`工序 3 · 求值`, r`
&= (6-\sqrt{35})\cdot 1^{99}
&= 6-\sqrt{35}
`),
  ])]},

  5: { ans: r`(A)　\(\dfrac{1}{a+1}\)`, parts: [ P("", [
    reg(r`工序 1 · 改寫 \(a\)`, r`
2^a=5 &\Rightarrow a=\log_2 5
`),
    reg(r`工序 2 · 換底`, r`
\log_{10}2 &= \dfrac{\log_2 2}{\log_2 10}
&= \dfrac{1}{\log_2(2\cdot 5)}
`),
    reg(r`工序 3 · 展開分母`, r`
&= \dfrac{1}{1+\log_2 5}
&= \dfrac{1}{1+a}
`),
  ])]},

  6: { ans: r`(B)　\(2x-3\)`, parts: [ P("", [
    reg(r`工序 1 · 根號配平方`, r`
\sqrt{x^2-2x+1} &= |x-1|
&= x-1 \quad(x>2)
`),
    reg(r`工序 2 · 去絕對值`, r`
|2-x| &= x-2 \quad(x>2)
`),
    reg(r`工序 3 · 相加`, r`
(x-1)+(x-2) &= 2x-3
`),
  ])]},

  7: { ans: r`(D)　最大數 \(=52\)`, parts: [ P("", [
    reg(r`工序 1 · 求平均`, r`
\bar{x} &= \dfrac{430}{10}
&= 43
`),
    reg(r`工序 2 · 定中間兩數`, r`
&\text{第 5,6 個}=42,\ 44
`),
    reg(r`工序 3 · 數到最大`, r`
\text{第 10 個} &= 44+2\times 4
&= 52
`),
  ])]},

  8: { ans: r`(C)　\(b=-4\)`, parts: [ P("", [
    reg(r`工序 1 · 交點在 \(y\) 軸`, r`
x &= 0
`),
    reg(r`工序 2 · 求交點 \(y\)`, r`
2y+4 &= 0
y &= -2
`),
    reg(r`工序 3 · 代入第二線`, r`
-b(-2)+8 &= 0
2b &= -8
b &= -4
`),
  ])]},

  9: { ans: r`(D)　I, II, III 全在 \(D\) 內`, parts: [ P("", [
    reg(r`工序 1 · I \((1,1)\)`, r`
1-1=0 &\ge -2
3+2=5 &\le 24
`),
    reg(r`工序 2 · II \((4,6)\)`, r`
4-6=-2 &\ge -2
12+12=24 &\le 24
`),
    reg(r`工序 3 · III \((7,0)\)`, r`
7 &\ge -2
21 &\le 24
`),
    reg(r`工序 4 · 結論`, r`
&\Rightarrow \text{三點皆在 }D
`),
  ])]},

  10: { ans: r`(A)　\(119988\)`, parts: [ P("", [
    reg(r`工序 1 · 每數每位出現次數`, r`
\text{次數} &= \dfrac{4!}{4}
&= 6
`),
    reg(r`工序 2 · 每位數字和`, r`
6\times(1+3+5+9) &= 108
`),
    reg(r`工序 3 · 乘位值`, r`
108\times 1111 &= 119988
`),
  ])]},

  11: { ans: r`(C)　\(\tan\angle ABD=\dfrac{2}{9}\)`, parts: [ P("", [
    reg(r`工序 1 · 設邊長`, r`
AC &= 2,\ DC=1
CB &= 4
`),
    reg(r`工序 2 · 兩角正切`, r`
\tan\angle ABC &= \dfrac{2}{4}
&= \dfrac{1}{2}
\tan\angle DBC &= \dfrac{1}{4}
`),
    reg(r`工序 3 · 角差公式`, r`
\tan\angle ABD &= \dfrac{\frac12-\frac14}{1+\frac12\cdot\frac14}
&= \dfrac{1/4}{9/8}
&= \dfrac{2}{9}
`),
  ])]},

  12: { ans: r`(B)　\(x^2-7x+1=0\)`, parts: [ P("", [
    reg(r`工序 1 · 韋達定理`, r`
\alpha+\beta &= 3
\alpha\beta &= 1
`),
    reg(r`工序 2 · 新根之和`, r`
\alpha^2+\beta^2 &= (\alpha+\beta)^2-2\alpha\beta
&= 7
`),
    reg(r`工序 3 · 新根之積`, r`
\alpha^2\beta^2 &= (\alpha\beta)^2
&= 1
`),
    reg(r`工序 4 · 新方程`, r`
x^2-7x+1 &= 0
`),
  ])]},

  13: { ans: r`(E)　\((-2,-1)\cup(2,+\infty)\)`, parts: [ P("", [
    reg(r`工序 1 · 分母為正`, r`
a+2 &> 0
a &> -2
`),
    reg(r`工序 2 · 焦點在 \(y\) 軸`, r`
a^2 &> a+2
(a-2)(a+1) &> 0
a>2 &\ \text{或}\ a<-1
`),
    reg(r`工序 3 · 取交集`, r`
&(-2,-1)\cup(2,+\infty)
`),
  ])]},

  14: { ans: r`(D)　\((5,1)\)`, parts: [ P("", [
    reg(r`工序 1 · 右移 3`, r`
x:\ 2 &\to 5
`),
    reg(r`工序 2 · 上移 1`, r`
y:\ 0 &\to 1
`),
    reg(r`工序 3 · 新頂點`, r`
&(5,1)
`),
  ])]},

  15: { ans: r`(B)　對所有 \(n\ge m\) 成立`, parts: [ P("", [
    reg(r`工序 1 · 已知`, r`
&P(m)\ \text{為真}
`),
    reg(r`工序 2 · 骨牌往後傳`, r`
P(m) &\Rightarrow P(m+1)\Rightarrow\cdots
`),
    reg(r`工序 3 · 結論`, r`
&P(n)\ \text{對所有}\ n\ge m\ \text{成立}
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(\tfrac{1}{5}\)　(b) \(\tfrac{99}{100}\)　(c) \(\tfrac{2}{5}\)`, parts: [
    P(r`（a）個位是 3 或 7`, [
      reg(r`工序 1 · 每 10 個有 2 個`, r`
P &= \dfrac{2}{10}
&= \dfrac{1}{5}
`),
    ]),
    P(r`（b）不是完全立方數`, [
      reg(r`工序 2 · 立方數個數`, r`
1^3,\dots,10^3 &\Rightarrow 10\ \text{個}
`),
      reg(r`工序 3 · 對立事件`, r`
P &= 1-\dfrac{10}{1000}
&= \dfrac{99}{100}
`),
    ]),
    P(r`（c）可被 4 或 5 整除`, [
      reg(r`工序 4 · 各倍數個數`, r`
\lfloor 1000/4\rfloor &= 250
\lfloor 1000/5\rfloor &= 200
\lfloor 1000/20\rfloor &= 50
`),
      reg(r`工序 5 · 排容原理`, r`
|A\cup B| &= 250+200-50
&= 400
P &= \dfrac{400}{1000}=\dfrac{2}{5}
`),
    ]),
  ]},

  2: { ans: r`(a) \(m=-\tfrac{1}{3},\ b=\tfrac{10}{3}\)　(b) \((x-1)^2+(y-3)^2=5\)`, parts: [
    P(r`（a）求垂直平分線`, [
      reg(r`工序 1 · 斜率`, r`
k_{AB} &= \dfrac{5-2}{0-(-1)}=3
m &= -\dfrac{1}{3}
`),
      reg(r`工序 2 · 過中點求 \(b\)`, r`
\text{中點} &= \left(-\tfrac{1}{2},\tfrac{7}{2}\right)
\tfrac{7}{2} &= -\tfrac{1}{3}\left(-\tfrac{1}{2}\right)+b
b &= \tfrac{10}{3}
`),
    ]),
    P(r`（b）求圓 \(C\)`, [
      reg(r`工序 3 · 圓心在兩線上`, r`
x+3y &= 10
2x+y &= 5
`),
      reg(r`工序 4 · 解圓心`, r`
x &= 1
y &= 3
`),
      reg(r`工序 5 · 半徑與方程`, r`
r^2 &= 1^2+(3-5)^2
&= 5
(x-1)^2+(y-3)^2 &= 5
`),
    ]),
  ]},

  3: { ans: r`最大面積 \(=\dfrac{18}{4+\pi}\) 平方米`, parts: [
    P("", [
      reg(r`工序 1 · 由周界表示 \(h\)`, r`
2h+2r+\pi r &= 6
h &= \dfrac{6-(2+\pi)r}{2}
`),
      reg(r`工序 2 · 面積函數`, r`
A &= 2rh+\dfrac{\pi r^2}{2}
&= 6r-\left(2+\dfrac{\pi}{2}\right)r^2
`),
      reg(r`工序 3 · 求極值`, r`
A' &= 6-(4+\pi)r
r &= \dfrac{6}{4+\pi}
`),
      reg(r`工序 4 · 最大面積`, r`
A_{\max} &= \dfrac{18}{4+\pi}
`),
    ]),
  ]},

  4: { ans: r`(a) \(a_n=\left(\tfrac{1}{2}\right)^{n}\)　(b) \(S_n=-\dfrac{2n}{n+1}\)`, parts: [
    P(r`（a）求通項`, [
      reg(r`工序 1 · 由 \(a_4^2=4a_3a_7\) 求 \(q\)`, r`
(a_1q^3)^2 &= 4(a_1q^2)(a_1q^6)
1 &= 4q^2
q &= \dfrac{1}{2}
`),
      reg(r`工序 2 · 求 \(a_1\) 與通項`, r`
2a_1 &= 1
a_1 &= \dfrac{1}{2}
a_n &= \left(\dfrac{1}{2}\right)^{n}
`),
    ]),
    P(r`（b）求 \(S_n\)`, [
      reg(r`工序 3 · 求 \(b_n\)`, r`
\log_2 a_k &= -k
b_n &= -\dfrac{n(n+1)}{2}
`),
      reg(r`工序 4 · 裂項`, r`
\dfrac{1}{b_n} &= -2\left(\dfrac{1}{n}-\dfrac{1}{n+1}\right)
`),
      reg(r`工序 5 · 相消求和`, r`
S_n &= -2\left(1-\dfrac{1}{n+1}\right)
&= -\dfrac{2n}{n+1}
`),
    ]),
  ]},

  5: { ans: r`(a) \(\sin(\alpha-\beta)=1\)　(b) \(\cos\!\left(\tfrac{\pi}{6}+\beta\right)=1\)（得證）`, parts: [
    P(r`（a）求 \(\sin(\alpha-\beta)\)`, [
      reg(r`工序 1 · 兩式平方相加`, r`
(\sin\alpha+\cos\beta)^2+(\cos\alpha-\sin\beta)^2 &= 3+1
`),
      reg(r`工序 2 · 展開化簡`, r`
2+2(\sin\alpha\cos\beta-\cos\alpha\sin\beta) &= 4
2+2\sin(\alpha-\beta) &= 4
`),
      reg(r`工序 3 · 求值`, r`
\sin(\alpha-\beta) &= 1
`),
    ]),
    P(r`（b）求證 \(\cos\!\left(\tfrac{\pi}{6}+\beta\right)=1\)`, [
      reg(r`工序 4 · 定 \(\alpha-\beta\)`, r`
\alpha-\beta &= \dfrac{\pi}{2}
`),
      reg(r`工序 5 · 回代求 \(\cos\beta,\sin\beta\)`, r`
\cos\beta &= \dfrac{\sqrt{3}}{2}
\sin\beta &= -\dfrac{1}{2}
`),
      reg(r`工序 6 · 展開目標式`, r`
\cos\!\left(\dfrac{\pi}{6}+\beta\right) &= \dfrac{\sqrt3}{2}\cdot\dfrac{\sqrt3}{2}-\dfrac{1}{2}\left(-\dfrac{1}{2}\right)
&= \dfrac{3}{4}+\dfrac{1}{4}
&= 1
`),
    ]),
  ]},
};

module.exports = { choice, solution };
