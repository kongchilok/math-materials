// 2018 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(A)　\(X\subset Y\)`, parts: [ P("", [
    reg(r`工序 1 · 代入小值`, r`
6^1-5(1)-1 &= 0
6^2-5(2)-1 &= 25
6^3-5(3)-1 &= 200
`),
    reg(r`工序 2 · 均為 25 倍數`, r`
\{0,25,200\} &\subset Y
&\Rightarrow X\subset Y
`),
  ])]},

  2: { ans: r`(B)　餘數 \(=5\)`, parts: [ P("", [
    reg(r`工序 1 · 餘式定理設值`, r`
2x-5 &= 0
x &= \tfrac{5}{2}
`),
    reg(r`工序 2 · 代入求餘數`, r`
f\!\left(\tfrac{5}{2}\right) &= \frac{250+50-580+320}{8}
&= \frac{40}{8}
&= 5
`),
  ])]},

  3: { ans: r`(D)　\(k=-\tfrac{3}{4}\)`, parts: [ P("", [
    reg(r`工序 1 · 韋達定理`, r`
\alpha+\beta &= \tfrac{4}{3}
\alpha\beta &= \tfrac{k}{3}
`),
    reg(r`工序 2 · 用根差平方`, r`
(\alpha-\beta)^2 &= (\alpha+\beta)^2-4\alpha\beta
\tfrac{25}{9} &= \tfrac{16}{9}-\tfrac{4k}{3}
`),
    reg(r`工序 3 · 解 \(k\)`, r`
\tfrac{4k}{3} &= -1
k &= -\tfrac{3}{4}
`),
  ])]},

  4: { ans: r`(C)　\(\dfrac{a^6}{8b^8c}\)`, parts: [ P("", [
    reg(r`工序 1 · 展開分母`, r`
(2a^{-1}b^2c)^3 &= 8a^{-3}b^6c^3
`),
    reg(r`工序 2 · 同底相減指數`, r`
\frac{a^3b^{-2}c^2}{8a^{-3}b^6c^3} &= \tfrac{1}{8}a^{6}b^{-8}c^{-1}
`),
    reg(r`工序 3 · 整理`, r`
&= \frac{a^6}{8b^8c}
`),
  ])]},

  5: { ans: r`(C)　\(M_{\max}=23\)`, parts: [ P("", [
    reg(r`工序 1 · 讀可行域頂點`, r`
&(1,4),(3,6),(7,4),(6,1),(2,2)
`),
    reg(r`工序 2 · 代入 \(M=3x+2y-6\)`, r`
(1,4) &\to -1
(3,6) &\to 15
(7,4) &\to 23
(6,1) &\to 14
(2,2) &\to 4
`),
    reg(r`工序 3 · 取最大`, r`
M_{\max} &= 23 \quad\text{於 }(7,4)
`),
  ])]},

  6: { ans: r`(B)　最大值 \(=0\)`, parts: [ P("", [
    reg(r`工序 1 · 展開`, r`
\log_a\tfrac{a}{b}+\log_b\tfrac{b}{a} &= (1-\log_a b)+(1-\log_b a)
`),
    reg(r`工序 2 · 設 \(t=\log_a b\)`, r`
&= 2-\left(t+\tfrac{1}{t}\right)
`),
    reg(r`工序 3 · 用 \(t+\tfrac1t\ge2\)`, r`
&\le 2-2
&= 0
`),
  ])]},

  7: { ans: r`(E)　\(x=\dfrac{y+y^2}{1+2y}\)`, parts: [ P("", [
    reg(r`工序 1 · 交叉相乘`, r`
xy &= (1+y)(y-x)
`),
    reg(r`工序 2 · 展開`, r`
xy &= y+y^2-x-xy
`),
    reg(r`工序 3 · 收 \(x\) 提公因`, r`
2xy+x &= y+y^2
x(2y+1) &= y+y^2
`),
    reg(r`工序 4 · 解 \(x\)`, r`
x &= \frac{y+y^2}{1+2y}
`),
  ])]},

  8: { ans: r`(D)　I, II, III 全對`, parts: [ P("", [
    reg(r`工序 1 · 由平均（III）`, r`
79+m+n &= 99
m+n &= 20
`),
    reg(r`工序 2 · 由中位數（I）`, r`
\text{已 5 個}<9 &\Rightarrow m,n\ge 9
`),
    reg(r`工序 3 · 推（II）`, r`
m\ge9,\ m+n=20 &\Rightarrow n\le 11
`),
    reg(r`工序 4 · 結論`, r`
&\Rightarrow \text{I, II, III 全對}
`),
  ])]},

  9: { ans: r`(E)　\(\tfrac{12}{35}\)`, parts: [ P("", [
    reg(r`工序 1 · 兩種順序相加`, r`
P &= \tfrac{3}{15}\cdot\tfrac{12}{14}+\tfrac{12}{15}\cdot\tfrac{3}{14}
`),
    reg(r`工序 2 · 計算`, r`
&= \frac{36+36}{210}
&= \frac{12}{35}
`),
  ])]},

  10: { ans: r`(C)　首項 \(=5\)`, parts: [ P("", [
    reg(r`工序 1 · 兩條件`, r`
\frac{a}{1-r} &= 3
\frac{a^2}{1-r^2} &= 45
`),
    reg(r`工序 2 · 相除`, r`
\frac{a}{1+r} &= 15
`),
    reg(r`工序 3 · 解 \(r\)`, r`
3(1-r) &= 15(1+r)
1-r &= 5+5r
r &= -\tfrac{2}{3}
`),
    reg(r`工序 4 · 求首項`, r`
a &= 3(1-r)
&= 5
`),
  ])]},

  11: { ans: r`(E)　右焦點 \((4,0)\)`, parts: [ P("", [
    reg(r`工序 1 · 化標準式`, r`
9x^2+25y^2 &= 225
\frac{x^2}{25}+\frac{y^2}{9} &= 1
`),
    reg(r`工序 2 · 求 \(c\) 與右焦點`, r`
c &= \sqrt{25-9}
&= 4
\text{右焦點} &= (4,0)
`),
  ])]},

  12: { ans: r`(B)　\(280\) 個`, parts: [ P("", [
    reg(r`工序 1 · 個位須為奇`, r`
\text{個位} &\in \{1,3,5,7,9\}
`),
    reg(r`工序 2 · 乘法原理`, r`
5\times 8\times 7 &= 280
`),
  ])]},

  13: { ans: r`(D)　\(a<0\) 且 \(b<0\)`, parts: [ P("", [
    reg(r`工序 1 · 開口方向`, r`
&\text{開口向下}\Rightarrow a<0
`),
    reg(r`工序 2 · 頂點在 \(y\) 軸右`, r`
-b &> 0
b &< 0
`),
    reg(r`工序 3 · 結論`, r`
&a<0,\ b<0
`),
  ])]},

  14: { ans: r`(A)　\(x>\tfrac{2}{3}\)`, parts: [ P("", [
    reg(r`工序 1 · 必要條件`, r`
2x &> 0
x &> 0
`),
    reg(r`工序 2 · 分段 \(x\ge2\)`, r`
x-2 &< 2x \quad(\text{恆成立})
`),
    reg(r`工序 3 · 分段 \(0<x<2\)`, r`
2-x &< 2x
x &> \tfrac{2}{3}
`),
    reg(r`工序 4 · 合併`, r`
x &> \tfrac{2}{3}
`),
  ])]},

  15: { ans: r`(A)　\((1,2)\)`, parts: [ P("", [
    reg(r`工序 1 · 頂點公式`, r`
P &= A+B-C
`),
    reg(r`工序 2 · 代入`, r`
P &= (3+2-4,\ 4+0-2)
&= (1,2)
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(\sin\!\left(\alpha+\tfrac{\pi}{4}\right)=\dfrac{\sqrt2}{10}\)　(b) \(\sin2\alpha+\cos2\alpha=-\dfrac{31}{25}\)`, parts: [
    P(r`先求 \(\cos\alpha\)（第二象限）`, [
      reg(r`工序 1 · 平方關係`, r`
\cos\alpha &= -\sqrt{1-\tfrac{16}{25}}
&= -\tfrac{3}{5}
`),
    ]),
    P(r`（a）求 \(\sin\!\left(\alpha+\tfrac{\pi}{4}\right)\)`, [
      reg(r`工序 2 · 和角公式`, r`
\sin\!\left(\alpha+\tfrac{\pi}{4}\right) &= \sin\alpha\cos\tfrac{\pi}{4}+\cos\alpha\sin\tfrac{\pi}{4}
&= \tfrac{4}{5}\cdot\tfrac{\sqrt2}{2}-\tfrac{3}{5}\cdot\tfrac{\sqrt2}{2}
&= \tfrac{\sqrt2}{10}
`),
    ]),
    P(r`（b）求 \(\sin2\alpha+\cos2\alpha\)`, [
      reg(r`工序 3 · \(\sin2\alpha\)`, r`
\sin2\alpha &= 2\cdot\tfrac{4}{5}\cdot\left(-\tfrac{3}{5}\right)
&= -\tfrac{24}{25}
`),
      reg(r`工序 4 · \(\cos2\alpha\) 與和`, r`
\cos2\alpha &= 1-2\left(\tfrac{4}{5}\right)^2
&= -\tfrac{7}{25}
\sin2\alpha+\cos2\alpha &= -\tfrac{31}{25}
`),
    ]),
  ]},

  2: { ans: r`(a) \(f(x)=6x-x^2\)　(b) \(x=2\) 或 \(4\)`, parts: [
    P(r`（a）求 \(f(x)\)`, [
      reg(r`工序 1 · 設模型代入`, r`
f(x) &= ax+bx^2
2a+4b &= 8
6a+36b &= 0
`),
      reg(r`工序 2 · 解 \(a,b\)`, r`
a &= -6b
-8b &= 8
b &= -1
a &= 6
`),
      reg(r`工序 3 · 得 \(f(x)\)`, r`
f(x) &= 6x-x^2
`),
    ]),
    P(r`（b）解方程`, [
      reg(r`工序 4 · 由對數求 \(f(x)\)`, r`
\log_{\tfrac12}\sqrt{f(x)} &= -\tfrac{3}{2}
\sqrt{f(x)} &= 2^{\tfrac32}
f(x) &= 8
`),
      reg(r`工序 5 · 解二次`, r`
6x-x^2 &= 8
x^2-6x+8 &= 0
(x-2)(x-4) &= 0
x_1 &= 2\ \text{或}\ x_2 = 4
`),
    ]),
  ]},

  3: { ans: r`(a) \(p=8,\ q=6\)　(b) \(C=(8,6)\)　(c) 面積 \(=28\)`, parts: [
    P(r`（a）求 \(p,q\)`, [
      reg(r`工序 1 · 代 \(B(0,6)\)`, r`
6 &= q
`),
      reg(r`工序 2 · 代 \(A(7,-1)\)`, r`
-1 &= 49-7p+6
7p &= 56
p &= 8
`),
    ]),
    P(r`（b）求 \(C\)`, [
      reg(r`工序 3 · 令 \(y=6\)`, r`
x^2-8x+6 &= 6
x(x-8) &= 0
x_1 &= 0\ \text{或}\ x_2 = 8
C &= (8,6)
`),
    ]),
    P(r`（c）求面積`, [
      reg(r`工序 4 · 底與高`, r`
|BC| &= 8
h &= |6-(-1)|
&= 7
`),
      reg(r`工序 5 · 面積`, r`
\text{面積} &= \tfrac{1}{2}\times 8\times 7
&= 28
`),
    ]),
  ]},

  4: { ans: r`(a) \(a_n=2^{\,n-3}\)　(b) \(T_n=2^{(n^2-5n)/2}\)`, parts: [
    P(r`（a）求通項`, [
      reg(r`工序 1 · 由 \(a_3a_7=a_5^2\)`, r`
a_5^2 &= 16
a_5 &= 4
`),
      reg(r`工序 2 · 由 \(a_4+a_6\) 求 \(q\)`, r`
a_5\!\left(\tfrac{1}{q}+q\right) &= 10
q+\tfrac{1}{q} &= \tfrac{5}{2}
q &= 2
`),
      reg(r`工序 3 · 首項與通項`, r`
a_1 &= \frac{a_5}{q^4}
&= \tfrac{1}{4}
a_n &= 2^{\,n-3}
`),
    ]),
    P(r`（b）求前 \(n\) 項乘積`, [
      reg(r`工序 4 · 指數求和`, r`
T_n &= \prod_{k=1}^{n}2^{\,k-3}
&= 2^{\sum_{k=1}^{n}(k-3)}
&= 2^{(n^2-5n)/2}
`),
    ]),
  ]},

  5: { ans: r`(a) \(a=1,\ b=2\)（即 \(\sum=\dfrac{n}{2n+1}\)）　(b) 見證明`, parts: [
    P(r`（a）求和並定 \(a,b\)`, [
      reg(r`工序 1 · 裂項`, r`
\frac{1}{4k^2-1} &= \frac{1}{2}\left(\frac{1}{2k-1}-\frac{1}{2k+1}\right)
`),
      reg(r`工序 2 · 求和`, r`
\sum_{k=1}^{n}\frac{1}{4k^2-1} &= \frac{1}{2}\left(1-\frac{1}{2n+1}\right)
&= \frac{n}{2n+1}
`),
      reg(r`工序 3 · 定 \(a,b\)`, r`
a &= 1,\ b=2
`),
    ]),
    P(r`（b）數學歸納法`, [
      reg(r`工序 4 · 基礎 \(n=1\)（左＝右，成立）`, r`
\text{左} &= \tfrac{1}{3}
\text{右} &= \tfrac{1}{3}
`),
      reg(r`工序 5 · 歸納步`, r`
S_{k+1} &= \frac{k}{2k+1}+\frac{1}{(2k+1)(2k+3)}
&= \frac{k+1}{2k+3}
&\Rightarrow n=k+1\ \text{成立}\ \square
`),
    ]),
  ]},
};

module.exports = { choice, solution };
