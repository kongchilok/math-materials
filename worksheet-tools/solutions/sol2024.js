// 2024 教師版詳解（工序分析法，多區域、等號對齊）
// 每區 math 為多行字串，各行已含 & 對齊點；產生器以 " \\ " 串成 aligned 環境
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

// ============ 選擇題 ============
const choice = {
  1: { ans: r`(B)　\(a=-6\)`, parts: [ P("", [
    reg(r`工序 1 · 求集合 \(A\)`, r`
x^2-3x-4 &\le 0
(x-4)(x+1) &\le 0
(x-4)(x+1) &= 0
x &= 4\ \text{或}\ -1
A=\{x: -1\le x &\le 4\}
`),
    reg(r`工序 2 · 求集合 \(B\)`, r`
3x+a &\ge 0
B=\{x: x &\ge -\tfrac{a}{3}\}
`),
    reg(r`工序 3 · 由交集求 \(a\)`, r`
-\tfrac{a}{3} &= 2
a &= -6
`),
  ])]},

  2: { ans: r`(B)　\(f(15)=1\)`, parts: [ P("", [
    reg(r`工序 1 · 改寫遞迴`, r`
f(x) &= f(x+1)+1
f(x+1) &= f(x)-1
`),
    reg(r`工序 2 · 通項`, r`
f(n) &= f(0)-n
`),
    reg(r`工序 3 · 求 \(f(15)\)`, r`
f(15) &= 16-15
&= 1
`),
  ])]},

  3: { ans: r`(C)　減少 2`, parts: [ P("", [
    reg(r`工序 1 · 展開右側`, r`
x(y+1)-(x-1)(y-1) &= (xy+x)-(xy-x-y+1)
&= 2x+y-1
`),
    reg(r`工序 2 · 化簡方程`, r`
4x+5y &= 2x+y-1
2x+4y &= -1
y &= -\tfrac{1}{2}x-\tfrac{1}{4}
`),
    reg(r`工序 3 · 求 \(\Delta y\)`, r`
\Delta y &= -\tfrac{1}{2}\times 4
&= -2
`),
  ])]},

  4: { ans: r`(C)　係數 \(=176\)`, parts: [ P("", [
    reg(r`工序 1 · 冪次條件`, r`
\tfrac{k}{2}+j &= 1
(k,j) &= (2,0),\ (0,1)
`),
    reg(r`工序 2 · \((k,j)=(2,0)\)`, r`
\binom{5}{2}(\sqrt{x})^2(-2)^3\,\binom{4}{0}(-1)^4 &= 10\cdot x\cdot(-8)\cdot 1
&= -80x
`),
    reg(r`工序 3 · \((k,j)=(0,1)\)`, r`
\binom{5}{0}(-2)^5\,\binom{4}{1}(2x)(-1)^3 &= (-32)\cdot 4\cdot 2x\cdot(-1)
&= 256x
`),
    reg(r`工序 4 · 合計係數`, r`
-80+256 &= 176
`),
  ])]},

  5: { ans: r`(D)　\(x^2+y^2-4x-6y=0\)`, parts: [ P("", [
    reg(r`工序 1 · 圓心與半徑`, r`
r=|OP| &= \sqrt{2^2+3^2}
&= \sqrt{13}
`),
    reg(r`工序 2 · 標準式`, r`
(x-2)^2+(y-3)^2 &= 13
`),
    reg(r`工序 3 · 展開`, r`
x^2-4x+4+y^2-6y+9 &= 13
x^2+y^2-4x-6y &= 0
`),
  ])]},

  6: { ans: r`(A)　原式 \(=1\)`, parts: [ P("", [
    reg(r`工序 1 · 分子`, r`
3\log\tfrac{1}{2}+\log 16 &= \log\tfrac{1}{8}+\log 16
&= \log\tfrac{16}{8}
&= \log 2
`),
    reg(r`工序 2 · 分母`, r`
\log 4+\log 5-1 &= \log 20-\log 10
&= \log\tfrac{20}{10}
&= \log 2
`),
    reg(r`工序 3 · 原式`, r`
\frac{\log 2}{\log 2} &= 1
`),
  ])]},

  7: { ans: r`(D)　\(a_{20}=262144\)`, parts: [ P("", [
    reg(r`工序 1 · 列方程`, r`
ar(1+r^3) &= 9
ar^6(1+r^3) &= 288
`),
    reg(r`工序 2 · 求公比 \(r\)`, r`
\frac{ar^6(1+r^3)}{ar(1+r^3)} &= \frac{288}{9}
r^5 &= 32
r &= 2
`),
    reg(r`工序 3 · 求首項 \(a\)`, r`
2a(1+8) &= 9
18a &= 9
a &= \tfrac{1}{2}
`),
    reg(r`工序 4 · 求 \(a_{20}\)`, r`
a_{20} &= ar^{19}
&= \tfrac{1}{2}\cdot 2^{19}
&= 2^{18}=262144
`),
  ])]},

  8: { ans: r`(A)　中位數 \(=4\)`, parts: [ P("", [
    reg(r`工序 1 · 由平均求 \(n\)`, r`
\frac{13n+8}{5} &= 6.8
13n+8 &= 34
n &= 2
`),
    reg(r`工序 2 · 代入各數`, r`
\{n,n-3,2n+5,4n-4,5n+10\} &= \{2,-1,9,4,20\}
`),
    reg(r`工序 3 · 排序取中位數`, r`
\text{排序} &:\ -1,\ 2,\ 4,\ 9,\ 20
\text{中位數} &= 4
`),
  ])]},

  9: { ans: r`(C)　\(\dfrac{m^2}{2}+\dfrac{1}{2m^2}\)`, parts: [ P("", [
    reg(r`工序 1 · 通分`, r`
1+\left(\tfrac{m^4-1}{2m^2}\right)^2 &= \frac{(2m^2)^2+(m^4-1)^2}{(2m^2)^2}
&= \frac{4m^4+m^8-2m^4+1}{4m^4}
`),
    reg(r`工序 2 · 分子湊平方`, r`
m^8+2m^4+1 &= (m^4+1)^2
`),
    reg(r`工序 3 · 開根`, r`
\sqrt{\frac{(m^4+1)^2}{4m^4}} &= \frac{m^4+1}{2m^2}
&= \frac{m^2}{2}+\frac{1}{2m^2}
`),
  ])]},

  10: { ans: r`(E)　\(|BC|=5\)`, parts: [ P("", [
    reg(r`工序 1 · 求 \(\cos C\)`, r`
\cos C &= \sqrt{1-\sin^2 C}
&= \sqrt{1-\tfrac{48}{49}}
&= \tfrac{1}{7}
`),
    reg(r`工序 2 · 餘弦定理`, r`
|AB|^2 &= |AC|^2+|BC|^2-2|AC||BC|\cos C
64 &= 49+|BC|^2-2\cdot 7\cdot|BC|\cdot\tfrac{1}{7}
`),
    reg(r`工序 3 · 解二次`, r`
|BC|^2-2|BC|-15 &= 0
(|BC|-5)(|BC|+3) &= 0
|BC| &= 5
`),
  ])]},

  11: { ans: r`(B)　\(n_{\max}=\dfrac{16}{3}\)`, parts: [ P("", [
    reg(r`工序 1 · 交點式`, r`
y &= a(x+2)(x-6)
`),
    reg(r`工序 2 · 求 \(a\)`, r`
4 &= a(2)(-6)
4 &= -12a
a &= -\tfrac{1}{3}
`),
    reg(r`工序 3 · 對稱軸`, r`
x &= \frac{-2+6}{2}
&= 2
`),
    reg(r`工序 4 · 最大值`, r`
n &= -\tfrac{1}{3}(2+2)(2-6)
&= -\tfrac{1}{3}(4)(-4)
&= \tfrac{16}{3}
`),
  ])]},

  12: { ans: r`(C)　\(\left(\pi,\tfrac{3\pi}{2}\right)\)`, parts: [ P("", [
    reg(r`工序 1 · \(\cos\) 遞增區間`, r`
\theta &\in [2k\pi-\pi,\ 2k\pi]
`),
    reg(r`工序 2 · 反推 \(x\)（取 \(k=1\)）`, r`
x+\tfrac{\pi}{3} &\in [\pi,\ 2\pi]
x &\in [\tfrac{2\pi}{3},\ \tfrac{5\pi}{3}]
`),
    reg(r`工序 3 · 比對選項`, r`
\left(\pi,\tfrac{3\pi}{2}\right) &\subset [\tfrac{2\pi}{3},\tfrac{5\pi}{3}]
`),
  ])]},

  13: { ans: r`(A)　\(\theta=\tfrac{\pi}{6}\) 或 \(\tfrac{5\pi}{6}\)`, parts: [ P("", [
    reg(r`工序 1 · 化為 \(\sin\theta\) 二次`, r`
1+\sin\theta-2(1-\sin^2\theta) &= 0
2\sin^2\theta+\sin\theta-1 &= 0
`),
    reg(r`工序 2 · 因式分解`, r`
(2\sin\theta-1)(\sin\theta+1) &= 0
\sin\theta &= \tfrac{1}{2}\ \text{或}\ \sin\theta = -1
`),
    reg(r`工序 3 · 取 \([0,\pi)\) 內解`, r`
\sin\theta=\tfrac{1}{2} &\Rightarrow \theta=\tfrac{\pi}{6},\ \tfrac{5\pi}{6}
\sin\theta=-1 &\Rightarrow \text{無解}
`),
  ])]},

  14: { ans: r`(B)　\(x^4+\dfrac{1}{x^4}=47\)`, parts: [ P("", [
    reg(r`工序 1 · 求 \(x+\tfrac{1}{x}\)`, r`
x^2-3x+1 &= 0
x+\tfrac{1}{x} &= 3
`),
    reg(r`工序 2 · 求 \(x^2+\tfrac{1}{x^2}\)`, r`
x^2+\tfrac{1}{x^2} &= \left(x+\tfrac{1}{x}\right)^2-2
&= 9-2=7
`),
    reg(r`工序 3 · 求 \(x^4+\tfrac{1}{x^4}\)`, r`
x^4+\tfrac{1}{x^4} &= \left(x^2+\tfrac{1}{x^2}\right)^2-2
&= 49-2=47
`),
  ])]},

  15: { ans: r`(E)`, parts: [ P("", [
    reg(r`工序 1 · 偶函數性質`, r`
f(x) &= f(|x|)\quad(\text{正向遞增})
`),
    reg(r`工序 2 · 比較絕對值`, r`
2^{-\tfrac73} &\approx 0.198
3^{-\tfrac27} &\approx 0.732
\left|\log_3\tfrac{2}{7}\right| &\approx 1.14
`),
    reg(r`工序 3 · 排序`, r`
\left|\log_3\tfrac{2}{7}\right| &> 3^{-\tfrac27} > 2^{-\tfrac73}
`),
    reg(r`工序 4 · 結論`, r`
f\!\left(\log_3\tfrac{2}{7}\right) &> f\!\left(3^{-\tfrac27}\right) > f\!\left(2^{-\tfrac73}\right)
`),
  ])]},
};

// ============ 解答題 ============
const solution = {
  1: { ans: r`(a) \(P(X\ge2)=\dfrac{1}{3}\)　(b) \(E(X)=\dfrac{6}{5}\)`, parts: [
    P(r`（a）求至少 2 件次品的概率`, [
      reg(r`工序 1 · \(P(X=2)\)`, r`
P(X=2) &= \frac{\binom{3}{2}\binom{7}{2}}{\binom{10}{4}}
&= \frac{3\cdot 21}{210}
&= \frac{3}{10}
`),
      reg(r`工序 2 · \(P(X=3)\)`, r`
P(X=3) &= \frac{\binom{3}{3}\binom{7}{1}}{\binom{10}{4}}
&= \frac{7}{210}
&= \frac{1}{30}
`),
      reg(r`工序 3 · \(P(X\ge2)\)`, r`
P(X\ge2) &= \tfrac{3}{10}+\tfrac{1}{30}
&= \tfrac{1}{3}
`),
    ]),
    P(r`（b）求次品數的期望`, [
      reg(r`工序 4 · 其餘機率`, r`
P(X=0) &= \frac{\binom{7}{4}}{\binom{10}{4}}=\frac{1}{6}
P(X=1) &= \frac{\binom{3}{1}\binom{7}{3}}{\binom{10}{4}}=\frac{1}{2}
`),
      reg(r`工序 5 · 期望值`, r`
E(X) &= 1\cdot\tfrac{1}{2}+2\cdot\tfrac{3}{10}+3\cdot\tfrac{1}{30}
&= \tfrac{15+18+3}{30}
&= \tfrac{6}{5}
`),
    ]),
  ]},

  2: { ans: r`(a) \(\tan(\alpha+\beta)=1\)　(b) \(\cos(\alpha+2\beta)=\dfrac{\sqrt{26}}{26}\)`, parts: [
    P(r`（a）求 \(\tan(\alpha+\beta)\)`, [
      reg(r`工序 1 · 求 \(\sin\beta\)`, r`
\sin^2\beta &= 1-\cos^2\beta
&= 1-\frac{9\cdot 13}{169}
&= \frac{52}{169}
\sin\beta &= \frac{2\sqrt{13}}{13}
`),
      reg(r`工序 2 · 求 \(\tan\beta\)`, r`
\tan\beta &= \frac{\sin\beta}{\cos\beta}
&= \frac{2\sqrt{13}/13}{3\sqrt{13}/13}
&= \frac{2}{3}
`),
      reg(r`工序 3 · 求 \(\tan(\alpha+\beta)\)`, r`
\tan(\alpha+\beta) &= \frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}
&= \frac{\frac{1}{5}+\frac{2}{3}}{1-\frac{1}{5}\cdot\frac{2}{3}}
&= \frac{\frac{13}{15}}{\frac{13}{15}}
&= 1
`),
    ]),
    P(r`（b）求 \(\cos(\alpha+2\beta)\)`, [
      reg(r`工序 4 · 定 \(\alpha+\beta\)`, r`
\alpha+\beta &\in (0,\pi)
\tan(\alpha+\beta) &= 1
\alpha+\beta &= \frac{\pi}{4}
`),
      reg(r`工序 5 · 拆角`, r`
\alpha+2\beta &= (\alpha+\beta)+\beta
&= \frac{\pi}{4}+\beta
`),
      reg(r`工序 6 · 求 \(\cos(\alpha+2\beta)\)`, r`
\cos(\alpha+2\beta) &= \cos\!\left(\frac{\pi}{4}+\beta\right)
&= \frac{\sqrt{2}}{2}(\cos\beta-\sin\beta)
&= \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{13}}{13}
&= \frac{\sqrt{26}}{26}
`),
    ]),
  ]},

  3: { ans: r`(a) \(a_n=3\) 或 \(a_n=6n-3\)　(b) \(n_{\min}=6\)`, parts: [
    P(r`（a）求通項公式`, [
      reg(r`工序 1 · 設公差列式`, r`
a_2 &= 3+d
a_5 &= 3+4d
`),
      reg(r`工序 2 · 等比中項解 \(d\)`, r`
(3+d)^2 &= 3(3+4d)
9+6d+d^2 &= 9+12d
d^2-6d &= 0
d_1 &= 0\ \text{或}\ d_2 = 6
`),
      reg(r`工序 3 · 通項`, r`
d=0 &\Rightarrow a_n=3
d=6 &\Rightarrow a_n=6n-3
`),
    ]),
    P(r`（b）求最小正整數 \(n\)`, [
      reg(r`工序 4 · 求 \(S_n\)`, r`
d=0 &\Rightarrow S_n=3n
d=6 &\Rightarrow S_n=3n^2
`),
      reg(r`工序 5 · 解不等式（取 \(d=6\)）`, r`
3n^2 &\ge 12n+36
n^2-4n-12 &\ge 0
(n-6)(n+2) &\ge 0
(n-6)(n+2) &= 0
n &= 6\ \text{或}\ -2
n &\ge 6
`),
      reg(r`工序 6 · 結論`, r`
n_{\min} &= 6
`),
    ]),
  ]},

  4: { ans: r`(a) \(1\le x\le 9\)　(b) \(a=10+2\sqrt{2}\) 或 \(10-2\sqrt{2}\)`, parts: [
    P(r`（a）\(a=8\) 時解 \(f(x)\ge0\)`, [
      reg(r`工序 1 · 轉化`, r`
f(x)\ge 0 &\Leftrightarrow |x-3|+|x-7|\le 8
`),
      reg(r`工序 2 · 分段求解`, r`
x<3 &:\ 10-2x\le 8\Rightarrow x\ge 1
3\le x\le 7 &:\ 4\le 8\ (\text{恆成立})
x>7 &:\ 2x-10\le 8\Rightarrow x\le 9
`),
      reg(r`工序 3 · 合併`, r`
1 &\le x\le 9
`),
    ]),
    P(r`（b）由最小值求 \(a\)`, [
      reg(r`工序 4 · 化簡 \(f(x)\)`, r`
x\in[-1,1] &\Rightarrow x<3<7
f(x) &= a-(3-x)-(7-x)
&= 2x+a-10
`),
      reg(r`工序 5 · 寫出 \(g(x)\)`, r`
g(x) &= xf(x)
&= 2x^2+(a-10)x
`),
      reg(r`工序 6 · 對稱軸（在 \([-1,1]\) 內）`, r`
x_0 &= -\frac{a-10}{4}
6 &\le a\le 14
`),
      reg(r`工序 7 · 由頂點最小值解 \(a\)`, r`
-\frac{(a-10)^2}{8} &= -1
(a-10)^2 &= 8
a_1 &= 10+2\sqrt{2}\ \text{或}\ a_2 = 10-2\sqrt{2}
`),
    ]),
  ]},

  5: { ans: r`(a) \(\dfrac{x^2}{2}-\dfrac{y^2}{3}=1\)　(b) \(m=2\sqrt{3}\) 或 \(-2\sqrt{3}\)`, parts: [
    P(r`（a）求雙曲線方程`, [
      reg(r`工序 1 · \(A\) 在曲線上`, r`
\frac{8}{a^2}-\frac{9}{b^2} &= 1
`),
      reg(r`工序 2 · 離心率條件`, r`
\frac{a^2+b^2}{a^2} &= \frac{10}{4}
b^2 &= \frac{3}{2}a^2
`),
      reg(r`工序 3 · 解 \(a^2,b^2\)`, r`
\frac{8}{a^2}-\frac{6}{a^2} &= 1
a^2 &= 2,\quad b^2=3
`),
      reg(r`工序 4 · 方程`, r`
\frac{x^2}{2}-\frac{y^2}{3} &= 1
`),
    ]),
    P(r`（b）求 \(m\)`, [
      reg(r`工序 5 · 聯立`, r`
3x^2-2(x+m)^2-6 &= 0
x^2-4mx-2m^2-6 &= 0
`),
      reg(r`工序 6 · 韋達定理`, r`
x_1+x_2 &= 4m
x_1x_2 &= -2m^2-6
`),
      reg(r`工序 7 · 垂直條件`, r`
x_1x_2+y_1y_2 &= 0
2x_1x_2+m(x_1+x_2)+m^2 &= 0
`),
      reg(r`工序 8 · 解 \(m\)`, r`
2(-2m^2-6)+4m^2+m^2 &= 0
m^2 &= 12
m_1 &= 2\sqrt{3}\ \text{或}\ m_2 = -2\sqrt{3}
`),
    ]),
  ]},
};

module.exports = { choice, solution };
