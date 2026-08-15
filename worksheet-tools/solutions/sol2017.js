// 2017 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(B)　\(a=-2\)`, parts: [ P("", [
    reg(r`工序 1 · 由 \(3\in Q\) 求 \(a\)`, r`
a^2-a-3 &= 3
(a-3)(a+2) &= 0
a &= 3 \ \text{或}\ -2
`),
    reg(r`工序 2 · 驗 \(a=3\)`, r`
P &= \{-2,1,3\}
Q &= \{1,3,-5\}
P\cap Q &= \{1,3\}\ \text{（不合）}
`),
    reg(r`工序 3 · 驗 \(a=-2\)`, r`
P &= \{-2,-4,3\}
Q &= \{1,3,-5\}
P\cap Q &= \{3\}\ \text{（合）}
`),
  ])]},

  2: { ans: r`(C)　\(x>-\tfrac{1}{2}\)`, parts: [ P("", [
    reg(r`工序 1 · 左半不等式`, r`
\frac{x+2}{3} &< \frac{4x+5}{6}
2(x+2) &< 4x+5
x &> -\tfrac{1}{2}
`),
    reg(r`工序 2 · 右半不等式`, r`
\frac{4x+5}{6} &< \frac{7x+8}{9}
12x+15 &< 14x+16
x &> -\tfrac{1}{2}
`),
    reg(r`工序 3 · 取交集`, r`
x &> -\tfrac{1}{2}
`),
  ])]},

  3: { ans: r`(B)　\(r=4\%\)`, parts: [ P("", [
    reg(r`工序 1 · 代入複利公式`, r`
5000(1+r)^2 &= 5408
(1+r)^2 &= 1.0816
`),
    reg(r`工序 2 · 解 \(r\)`, r`
1+r &= 1.04
r &= 4\%
`),
  ])]},

  4: { ans: r`(E)　\(a+b=20\)`, parts: [ P("", [
    reg(r`工序 1 · 取以 2 為底對數`, r`
y &= ab^x
\log_2 y &= \log_2 a+(\log_2 b)x
`),
    reg(r`工序 2 · 由 \((-2,0),(0,4)\) 求直線`, r`
\text{斜率} &= \frac{4-0}{0-(-2)}
&= 2
\log_2 y &= 2x+4
`),
    reg(r`工序 3 · 對照求 \(a,b\)`, r`
\log_2 a=4 &\Rightarrow a=16
\log_2 b=2 &\Rightarrow b=4
`),
    reg(r`工序 4 · 求 \(a+b\)`, r`
a+b &= 20
`),
  ])]},

  5: { ans: r`(C)　\(x=6\) 或 \(\tfrac{1}{6}\)`, parts: [ P("", [
    reg(r`工序 1 · 觀察對稱結構`, r`
x+\frac{1}{x} &= 6+\frac{1}{6}
`),
    reg(r`工序 2 · 直接讀解`, r`
x &= 6 \ \text{或}\ \frac{1}{6}
`),
  ])]},

  6: { ans: r`(D)　\(-\tfrac{4}{3}\)`, parts: [ P("", [
    reg(r`工序 1 · 分子`, r`
2\log_{10}2+\log_{10}6 &= \log_{10}4+\log_{10}6
&= \log_{10}24
`),
    reg(r`工序 2 · 分母`, r`
-\log_{10}3-3\log_{10}2 &= -(\log_{10}3+\log_{10}8)
&= -\log_{10}24
`),
    reg(r`工序 3 · 括號的 5 次方`, r`
\left(\frac{\log_{10}24}{-\log_{10}24}\right)^{5} &= (-1)^5
&= -1
`),
    reg(r`工序 4 · 後項`, r`
9^5\times3^{-11} &= 3^{10}\times3^{-11}
&= \frac{1}{3}
`),
    reg(r`工序 5 · 合計`, r`
-1-\frac{1}{3} &= -\frac{4}{3}
`),
  ])]},

  7: { ans: r`(B)　\(a=1\)`, parts: [ P("", [
    reg(r`工序 1 · 因式定理代入`, r`
f(1) &= 1+3-a-3
&= 1-a
`),
    reg(r`工序 2 · 令 \(f(1)=0\)`, r`
1-a &= 0
a &= 1
`),
  ])]},

  8: { ans: r`(C)　最小值 \(=38\)`, parts: [ P("", [
    reg(r`工序 1 · 展開兩項`, r`
6(7-x) &= 42-6x
[9-(7-x)]x &= (2+x)x
&= x^2+2x
`),
    reg(r`工序 2 · 合併同類`, r`
42-6x+x^2+2x &= x^2-4x+42
`),
    reg(r`工序 3 · 配方求最小`, r`
x^2-4x+42 &= (x-2)^2+38
\text{最小值} &= 38
`),
  ])]},

  9: { ans: r`(E)　\(\sin x\cos x=\tfrac{4}{9}\)（不在 A–D，選 E）`, parts: [ P("", [
    reg(r`工序 1 · 兩邊平方`, r`
(\sin x-\cos x)^2 &= \tfrac{1}{9}
\sin^2x-2\sin x\cos x+\cos^2x &= \tfrac{1}{9}
`),
    reg(r`工序 2 · 用 \(\sin^2+\cos^2=1\)`, r`
1-2\sin x\cos x &= \tfrac{1}{9}
\sin x\cos x &= \tfrac{4}{9}
`),
    reg(r`工序 3 · 比對選項`, r`
\tfrac{4}{9} &\notin \{\text{A,B,C,D}\}
&\Rightarrow \text{選 (E)}
`),
  ])]},

  10: { ans: r`(B)　1 個實根`, parts: [ P("", [
    reg(r`工序 1 · 合併對數`, r`
\ln(x-1)+\ln x &= \ln 6
x(x-1) &= 6
`),
    reg(r`工序 2 · 解二次`, r`
x^2-x-6 &= 0
x &= 3 \ \text{或}\ -2
`),
    reg(r`工序 3 · 驗真數條件`, r`
x=3 &:\ \text{真數}>0\ \text{（合）}
x=-2 &:\ \text{真數}<0\ \text{（捨）}
&\Rightarrow 1\ \text{個實根}
`),
  ])]},

  11: { ans: r`(A)　\(a_2a_3=\tfrac{2}{3}\)`, parts: [ P("", [
    reg(r`工序 1 · 韋達定理求積`, r`
a_1a_4 &= \frac{c}{a}
&= \frac{2}{3}
`),
    reg(r`工序 2 · 等比性質`, r`
a_2a_3 &= a_1a_4
&= \frac{2}{3}
`),
  ])]},

  12: { ans: r`(E)　\(y=e^{x-1}+1\)`, parts: [ P("", [
    reg(r`工序 1 · 上移 1 單位`, r`
y &= e^x+1
`),
    reg(r`工序 2 · 右移 1 單位`, r`
y &= e^{x-1}+1
`),
  ])]},

  13: { ans: r`(D)　\(\alpha\in\left(\tfrac{3\pi}{2},2\pi\right)\)`, parts: [ P("", [
    reg(r`工序 1 · 各條件定象限`, r`
\cos\alpha>0 &\Rightarrow \text{Q1 或 Q4}
\tan\alpha<0 &\Rightarrow \text{Q2 或 Q4}
`),
    reg(r`工序 2 · 取交集`, r`
&\Rightarrow \text{第四象限}
\alpha &\in \left(\tfrac{3\pi}{2},2\pi\right)
`),
  ])]},

  14: { ans: r`(B)　周長 \(=18\)`, parts: [ P("", [
    reg(r`工序 1 · 求 \(a,c\)`, r`
a &= 5
c &= \sqrt{25-9}
&= 4
`),
    reg(r`工序 2 · 三邊和為周長`, r`
MF_1+MF_2 &= 2a=10
F_1F_2 &= 2c=8
\text{周長} &= 18
`),
  ])]},

  15: { ans: r`(A)　常數項 \(=-252\)`, parts: [ P("", [
    reg(r`工序 1 · 通項定常數項`, r`
T_{k+1} &= \binom{10}{k}(-1)^k x^{10-2k}
10-2k &= 0
k &= 5
`),
    reg(r`工序 2 · 代入求值`, r`
T_6 &= \binom{10}{5}(-1)^5
&= 252\times(-1)
&= -252
`),
  ])]},
};

const solution = {
  1: { ans: r`\(\dfrac{x^3+x}{x^2-3x+2}=x+3-\dfrac{2}{x-1}+\dfrac{10}{x-2}\)`, parts: [
    P("", [
      reg(r`工序 1 · 長除法`, r`
x^3+x &= (x^2-3x+2)(x+3)+(8x-6)
\text{原式} &= (x+3)+\frac{8x-6}{(x-1)(x-2)}
`),
      reg(r`工序 2 · 設部分分式`, r`
\frac{8x-6}{(x-1)(x-2)} &= \frac{A}{x-1}+\frac{B}{x-2}
`),
      reg(r`工序 3 · 求 \(A\)（代 \(x=1\)）`, r`
A &= \frac{8(1)-6}{1-2}
&= -2
`),
      reg(r`工序 4 · 求 \(B\)（代 \(x=2\)）`, r`
B &= \frac{8(2)-6}{2-1}
&= 10
`),
      reg(r`工序 5 · 結果`, r`
&= (x+3)-\frac{2}{x-1}+\frac{10}{x-2}
`),
    ]),
  ]},

  2: { ans: r`(a) \((x-2)^2+(y-3)^2=9\)　(b) \(5-3\sqrt{2}<b<5+3\sqrt{2}\)　(c) \(b=1\) 或 \(9\)`, parts: [
    P(r`（a）求圓 \(C\) 的方程`, [
      reg(r`工序 1 · 半徑（圓心到 \(x\) 軸）`, r`
r &= 3
`),
      reg(r`工序 2 · 圓方程`, r`
(x-2)^2+(y-3)^2 &= 9
`),
    ]),
    P(r`（b）求相交於兩點的 \(b\) 範圍`, [
      reg(r`工序 3 · 圓心到 \(L\) 距離`, r`
L &:\ x+y-b=0
d &= \frac{|2+3-b|}{\sqrt{2}}
`),
      reg(r`工序 4 · 相交條件 \(d<r\)`, r`
\frac{|5-b|}{\sqrt{2}} &< 3
|5-b| &< 3\sqrt{2}
5-3\sqrt{2} &< b < 5+3\sqrt{2}
`),
    ]),
    P(r`（c）由 \(|AB|=2\) 求 \(b\)`, [
      reg(r`工序 5 · 弦長公式求 \(d^2\)`, r`
\sqrt{r^2-d^2} &= 1
d^2 &= 8
`),
      reg(r`工序 6 · 解 \(b\)`, r`
\frac{(5-b)^2}{2} &= 8
(5-b)^2 &= 16
b &= 1 \ \text{或}\ 9
`),
    ]),
  ]},

  3: { ans: r`(a) \(\tfrac{1}{35}\)　(b) \(\tfrac{18}{35}\)　(c) \(\tfrac{12}{35}\)　(d) \(\tfrac{34}{35}\)`, parts: [
    P(r`總取法 \(\binom{7}{3}=35\)`, [
      reg(r`工序 1 · (a) 3 男`, r`
P &= \frac{\binom{3}{3}}{\binom{7}{3}}
&= \frac{1}{35}
`),
      reg(r`工序 2 · (b) 1 男 2 女`, r`
P &= \frac{\binom{3}{1}\binom{4}{2}}{\binom{7}{3}}
&= \frac{18}{35}
`),
      reg(r`工序 3 · (c) 2 男 1 女`, r`
P &= \frac{\binom{3}{2}\binom{4}{1}}{\binom{7}{3}}
&= \frac{12}{35}
`),
      reg(r`工序 4 · (d) 至少 1 女`, r`
P &= 1-\frac{1}{35}
&= \frac{34}{35}
`),
    ]),
  ]},

  4: { ans: r`(a) \(a_n=n-2\)　(b) \(S_n=\dfrac{n}{2(n+2)}\)`, parts: [
    P(r`（a）求通項 \(a_n\)`, [
      reg(r`工序 1 · 由 \(S_3,S_5\) 求中項`, r`
3a_2 &= 0
a_2 &= 0
5a_3 &= 5
a_3 &= 1
`),
      reg(r`工序 2 · 公差與通項`, r`
d &= a_3-a_2
&= 1
a_1 &= a_2-d
&= -1
a_n &= n-2
`),
    ]),
    P(r`（b）求前 \(n\) 項和 \(S_n\)`, [
      reg(r`工序 3 · 裂項`, r`
a_{n+3} &= n+1
a_{n+4} &= n+2
b_n &= \frac{1}{(n+1)(n+2)}
&= \frac{1}{n+1}-\frac{1}{n+2}
`),
      reg(r`工序 4 · 裂項相消`, r`
S_n &= \left(\frac{1}{2}-\frac{1}{3}\right)+\cdots+\left(\frac{1}{n+1}-\frac{1}{n+2}\right)
&= \frac{1}{2}-\frac{1}{n+2}
&= \frac{n}{2(n+2)}
`),
    ]),
  ]},

  5: { ans: r`對所有正整數 \(n\)，\(22\mid 3^{3n+1}-5^{n+2}\)（得證）`, parts: [
    P(r`數學歸納法`, [
      reg(r`工序 1 · 基礎 \(n=1\)`, r`
3^4-5^3 &= 81-125
&= -44
&= -2\times22
`),
      reg(r`工序 2 · 歸納假設`, r`
&\text{設 }22\mid(3^{3k+1}-5^{k+2})
`),
      reg(r`工序 3 · 歸納步 \(n=k+1\)`, r`
3^{3k+4}-5^{k+3} &= 27\cdot3^{3k+1}-5\cdot5^{k+2}
&= 27(3^{3k+1}-5^{k+2})+22\cdot5^{k+2}
`),
      reg(r`工序 4 · 結論`, r`
&\text{兩項皆被 22 整除}
&\Rightarrow n=k+1\ \text{成立}\ \square
`),
    ]),
  ]},
};

module.exports = { choice, solution };
