// 2020 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(A)　\(\{0,1,2\}\)`, parts: [ P("", [
    reg(r`工序 1 · 先求聯集`, r`
Q\cup R &= \{0,1,2,3,4\}
`),
    reg(r`工序 2 · 再求交集`, r`
P\cap(Q\cup R) &= \{0,1,2\}
`),
  ])]},

  2: { ans: r`(E)　約 \(2{,}120{,}000\)`, parts: [ P("", [
    reg(r`工序 1 · 複利公式`, r`
P_3 &= 2000000\times 1.02^3
`),
    reg(r`工序 2 · 計算取最近`, r`
&\approx 2122416
&\Rightarrow 2{,}120{,}000
`),
  ])]},

  3: { ans: r`(B)　\((3x-2y)(3x+2y-1)\)`, parts: [ P("", [
    reg(r`工序 1 · 平方差與提項`, r`
9x^2-4y^2 &= (3x-2y)(3x+2y)
-3x+2y &= -(3x-2y)
`),
    reg(r`工序 2 · 提公因式`, r`
&= (3x-2y)(3x+2y-1)
`),
  ])]},

  4: { ans: r`(B)　\(\sqrt[3]{7.2}<\sqrt{4.1}<\sqrt[4]{17}\)`, parts: [ P("", [
    reg(r`工序 1 · 化次方估值`, r`
7.2^{1/3} &\approx 1.93
4.1^{1/2} &\approx 2.02
17^{1/4} &\approx 2.03
`),
    reg(r`工序 2 · 比較`, r`
7.2^{1/3}<4.1^{1/2} &< 17^{1/4}
`),
  ])]},

  5: { ans: r`(C)　\(-3\le x\le-\tfrac{1}{3}\)`, parts: [ P("", [
    reg(r`工序 1 · 去絕對值`, r`
-4 &\le -3x-5 \le 4
`),
    reg(r`工序 2 · 整理（除以 \(-3\) 變號）`, r`
1 &\le -3x \le 9
-3 &\le x \le -\tfrac{1}{3}
`),
  ])]},

  6: { ans: r`(D)　II 及 III`, parts: [ P("", [
    reg(r`工序 1 · 取對數`, r`
x^5=y^{13} &\Rightarrow 5\log x=13\log y
`),
    reg(r`工序 2 · 求兩對數`, r`
\log_x y &= \tfrac{5}{13}
\log_y x &= \tfrac{13}{5}
`),
    reg(r`工序 3 · 判斷`, r`
&\Rightarrow \text{II, III 為真}
`),
  ])]},

  7: { ans: r`(A)　\(x=\tfrac{9}{16}\)`, parts: [ P("", [
    reg(r`工序 1 · 有理化（乘共軛）`, r`
(\sqrt{x+7}-\sqrt{x})(\sqrt{x+7}+\sqrt{x}) &= 7
\sqrt{x+7}+\sqrt{x} &= \tfrac{7}{2}
`),
    reg(r`工序 2 · 與原式相減`, r`
2\sqrt{x} &= \tfrac{7}{2}-2
\sqrt{x} &= \tfrac{3}{4}
`),
    reg(r`工序 3 · 求 \(x\)`, r`
x &= \tfrac{9}{16}
`),
  ])]},

  8: { ans: r`(B)　\(36\) 個`, parts: [ P("", [
    reg(r`工序 1 · 個位為 0`, r`
5\times 4 &= 20
`),
    reg(r`工序 2 · 個位為 6（首位 \(\ne0\)）`, r`
4\times 4 &= 16
`),
    reg(r`工序 3 · 合計`, r`
20+16 &= 36
`),
  ])]},

  9: { ans: r`(A)　\(495\)`, parts: [ P("", [
    reg(r`工序 1 · 通項定次方`, r`
2(12-k)-k &= 0
k &= 8
`),
    reg(r`工序 2 · 代入`, r`
T_9 &= \binom{12}{8}
&= 495
`),
  ])]},

  10: { ans: r`(E)　I 及 III`, parts: [ P("", [
    reg(r`工序 1 · 圓心與半徑`, r`
M &= \left(\tfrac{a}{2},-\tfrac{b}{2}\right)
r &= \tfrac{1}{2}\sqrt{a^2+b^2}
`),
    reg(r`工序 2 · 驗 I \((0,0)\)`, r`
\text{到 }M\text{ 距} &= r \ \text{（在圓上）}
`),
    reg(r`工序 3 · 驗 III \((a,-b)\)`, r`
\text{到 }M\text{ 距} &= r \ \text{（在圓上）}
`),
    reg(r`工序 4 · 驗 II \((a,b)\)`, r`
\text{到 }M\text{ 距} &\ne r \ \text{（不在）}
`),
  ])]},

  11: { ans: r`(A)　\(y=(x-3)^2-5\)`, parts: [ P("", [
    reg(r`工序 1 · 右移 4`, r`
y &= (x-4+1)^2
&= (x-3)^2
`),
    reg(r`工序 2 · 下移 5`, r`
y &= (x-3)^2-5
`),
  ])]},

  12: { ans: r`(C)　\(|AB|=\tfrac{5}{2}\)`, parts: [ P("", [
    reg(r`工序 1 · \(L_1\) 的 \(y\) 截距`, r`
x=0 &\Rightarrow y=3
A &= (0,3)
`),
    reg(r`工序 2 · 平行求 \(m\)`, r`
\tfrac{1}{4} &= \tfrac{2}{m}
m &= 8
`),
    reg(r`工序 3 · \(L_2\) 截距與 \(|AB|\)`, r`
x=0 &\Rightarrow y=\tfrac{1}{2}
|AB| &= 3-\tfrac{1}{2}=\tfrac{5}{2}
`),
  ])]},

  13: { ans: r`(D)　\(9\) 項`, parts: [ P("", [
    reg(r`工序 1 · 公差與通項`, r`
d &= \tfrac{13-22}{3}=-3
a_n &= 28-3n
`),
    reg(r`工序 2 · 正值條件`, r`
28-3n &> 0
n &< \tfrac{28}{3}
`),
    reg(r`工序 3 · 計數`, r`
n &\le 9 \Rightarrow 9 \text{ 項}
`),
  ])]},

  14: { ans: r`(C)　\(\angle PAB=78^\circ\)`, parts: [ P("", [
    reg(r`工序 1 · 弦切角定理`, r`
\angle PAB &= \angle ACB
`),
    reg(r`工序 2 · 求 \(\angle ACB\)`, r`
\angle ACB &= 180^\circ-84^\circ-18^\circ
&= 78^\circ
`),
    reg(r`工序 3 · 結論`, r`
\angle PAB &= 78^\circ
`),
  ])]},

  15: { ans: r`(B)　\(\cos2\theta=-\tfrac{7}{25}\)`, parts: [ P("", [
    reg(r`工序 1 · 平方求 \(\sin2\theta\)`, r`
(\sin\theta-\cos\theta)^2 &= 1-\sin2\theta
\tfrac{1}{25} &= 1-\sin2\theta
\sin2\theta &= \tfrac{24}{25}
`),
    reg(r`工序 2 · 定 \(\cos2\theta\) 符號`, r`
\cos2\theta &= -\sqrt{1-\sin^2 2\theta}
&= -\tfrac{7}{25}
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(0.64\)　(b) \(\tfrac{112}{275}\)`, parts: [
    P(r`（a）抽出可用磁碟`, [
      reg(r`工序 1 · 全概率`, r`
P &= 0.4\times 1+0.6\times 0.4
&= 0.64
`),
    ]),
    P(r`（b）抽 2 張都可用`, [
      reg(r`工序 2 · 可用張數`, r`
40+60\times 0.4 &= 64
`),
      reg(r`工序 3 · 不放回`, r`
P &= \tfrac{64}{100}\times\tfrac{63}{99}
&= \tfrac{112}{275}
`),
    ]),
  ]},

  2: { ans: r`(a) \(T=\tfrac{23}{20}+\tfrac{x}{50}\)　(b) \(x=230\) 公里`, parts: [
    P(r`（a）以 \(x\) 表示總時間`, [
      reg(r`工序 1 · 分段相加`, r`
T &= 2+\tfrac{45}{60}+\tfrac{x-80}{50}
&= \tfrac{23}{20}+\tfrac{x}{50}
`),
    ]),
    P(r`（b）求距離`, [
      reg(r`工序 2 · 令等於原計劃時間`, r`
\tfrac{23}{20}+\tfrac{x}{50} &= \tfrac{x}{40}
\tfrac{23}{20} &= \tfrac{x}{200}
x &= 230
`),
    ]),
  ]},

  3: { ans: r`(a) \(a_2=\tfrac34,a_3=\tfrac89,a_4=\tfrac{15}{16}\)　(b) \(a_n=\dfrac{n^2-1}{n^2}\)`, parts: [
    P(r`（a）求前幾項`, [
      reg(r`工序 1 · 逐項計算`, r`
a_2 &= \tfrac{3}{4}
a_3 &= \tfrac{8}{9}
a_4 &= \tfrac{15}{16}
`),
    ]),
    P(r`（b）猜測並證明`, [
      reg(r`工序 2 · 猜測通項`, r`
a_n &= \frac{n^2-1}{n^2}
`),
      reg(r`工序 3 · 歸納步`, r`
a_{k+1} &= \frac{k^2-1}{k^2}+\frac{2k+1}{k^2(k+1)^2}
&= \frac{(k+1)^2-1}{(k+1)^2}\ \square
`),
    ]),
  ]},

  4: { ans: r`(a) \(a=2\) 或 \(3\)　(b) 其餘根 \(2+\log_2 3\)（當 \(a=2\)）或 \(2+\log_3 2\)（當 \(a=3\)）`, parts: [
    P(r`（a）求 \(a\)`, [
      reg(r`工序 1 · 代入 \(x=3\)`, r`
a^2-5a+6 &= 0
a &= 2\ \text{或}\ 3
`),
    ]),
    P(r`（b）求其餘根`, [
      reg(r`工序 2 · 換元 \(t=a^{x-2}\)`, r`
t^2-5t+6 &= 0
t &= 2\ \text{或}\ 3
`),
      reg(r`工序 3 · 解其餘根`, r`
a=2 &\Rightarrow x=2+\log_2 3
a=3 &\Rightarrow x=2+\log_3 2
`),
    ]),
  ]},

  5: { ans: r`(a) \(P=(2,3),\ r=5\)　(b) 均過 \(P\)　(c) 面積 \(=\tfrac{25}{4}\)`, parts: [
    P(r`（a）求圓心與半徑`, [
      reg(r`工序 1 · 配方`, r`
(x-2)^2+(y-3)^2 &= 25
P=(2,3),\ r &= 5
`),
    ]),
    P(r`（b）證兩線過 \(P\)`, [
      reg(r`工序 2 · 驗 \(\ell_1\) 過 \((2,3)\)`, r`
3(3) &= 3\tan30^\circ\cdot 2+9-2\sqrt3
9 &= 2\sqrt3+9-2\sqrt3
`),
      reg(r`工序 3 · 驗 \(\ell_2\) 過 \((2,3)\)`, r`
3 &= \tan60^\circ\cdot 2-(2\sqrt3-3)
3 &= 2\sqrt3-2\sqrt3+3
`),
    ]),
    P(r`（c）求 \(\triangle PAB\) 面積`, [
      reg(r`工序 4 · 夾角與面積`, r`
\theta &= 60^\circ-30^\circ=30^\circ
\text{面積} &= \tfrac{1}{2}\cdot 5^2\cdot\sin30^\circ
&= \tfrac{25}{4}
`),
    ]),
  ]},
};

module.exports = { choice, solution };
