// 2021 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(B)　\(3\) 個`, parts: [ P("", [
    reg(r`工序 1 · 因式分解定 \(Q\)`, r`
x^2-15x+36 &= (x-3)(x-12)
Q &= \{x:3<x<12\}
`),
    reg(r`工序 2 · 取 \(P\) 中落在區間`, r`
P\cap Q &= \{5,7,11\}
&= 3\ \text{個}
`),
  ])]},

  2: { ans: r`(E)　\(\tfrac{60}{7}\) 小時`, parts: [ P("", [
    reg(r`工序 1 · 各自效率`, r`
\text{瑪麗}=\tfrac{1}{4},\ \text{約翰} &= \tfrac{1}{3}
`),
    reg(r`工序 2 · 合作效率`, r`
\tfrac{1}{4}+\tfrac{1}{3} &= \tfrac{7}{12}
`),
    reg(r`工序 3 · 完成 5 件`, r`
T &= \dfrac{5}{\frac{7}{12}}
&= \dfrac{60}{7}
`),
  ])]},

  3: { ans: r`(A)　\(a_{10}=19\)`, parts: [ P("", [
    reg(r`工序 1 · 由和求通項`, r`
a_n &= S_n-S_{n-1}
&= n^2-(n-1)^2
&= 2n-1
`),
    reg(r`工序 2 · 第 10 項`, r`
a_{10} &= 19
`),
  ])]},

  4: { ans: r`(B)　\(m>\sqrt3\)`, parts: [ P("", [
    reg(r`工序 1 · 恆正兩條件`, r`
m &> 0
\Delta=36-12m^2 &< 0
`),
    reg(r`工序 2 · 解`, r`
m^2 &> 3
m &> \sqrt3
`),
  ])]},

  5: { ans: r`(B)　\(7x^2-3x+2=0\)`, parts: [ P("", [
    reg(r`工序 1 · 韋達定理`, r`
\alpha+\beta &= \tfrac{3}{2}
\alpha\beta &= \tfrac{7}{2}
`),
    reg(r`工序 2 · 新根和與積`, r`
\tfrac{1}{\alpha}+\tfrac{1}{\beta} &= \tfrac{\frac32}{\frac72}=\tfrac{3}{7}
\tfrac{1}{\alpha\beta} &= \tfrac{2}{7}
`),
    reg(r`工序 3 · 重建方程`, r`
x^2-\tfrac{3}{7}x+\tfrac{2}{7} &= 0
7x^2-3x+2 &= 0
`),
  ])]},

  6: { ans: r`(A)　\(31-8\pi\)`, parts: [ P("", [
    reg(r`工序 1 · 半徑`, r`
2r &= 4
r &= 2
`),
    reg(r`工序 2 · 兩圓覆蓋（容斥）`, r`
4\pi+4\pi-3 &= 8\pi-3
`),
    reg(r`工序 3 · 陰影`, r`
28-(8\pi-3) &= 31-8\pi
`),
  ])]},

  7: { ans: r`(C)　\(-3\le k<0\)`, parts: [ P("", [
    reg(r`工序 1 · 換元`, r`
t &= 3^{-x^2}\in(0,1]
9^{-x^2} &= t^2
`),
    reg(r`工序 2 · 配方`, r`
k &= t^2-4t
&= (t-2)^2-4
`),
    reg(r`工序 3 · 求值域`, r`
t\to0^+ &\Rightarrow k\to0^-
t=1 &\Rightarrow k=-3
&\Rightarrow -3\le k<0
`),
  ])]},

  8: { ans: r`(D)　\(m=4\)`, parts: [ P("", [
    reg(r`工序 1 · 因式定理`, r`
f\!\left(-\tfrac{1}{2}\right) &= 0
`),
    reg(r`工序 2 · 代入化簡`, r`
2-\tfrac{m}{2} &= 0
m &= 4
`),
  ])]},

  9: { ans: r`(C)　十位數字 \(=4\)`, parts: [ P("", [
    reg(r`工序 1 · 只看末兩位`, r`
103^{10} &\equiv 3^{10} \pmod{100}
`),
    reg(r`工序 2 · 計算`, r`
3^{10} &= 59049
`),
    reg(r`工序 3 · 十位數字`, r`
&= 4
`),
  ])]},

  10: { ans: r`(A)　\(x=\tfrac{1}{4}\) 或 \(2\)`, parts: [ P("", [
    reg(r`工序 1 · 換元`, r`
u &= \log_4 x
y &= u+3
`),
    reg(r`工序 2 · 代入第二式`, r`
2u^2 &= 1-u
(2u-1)(u+1) &= 0
`),
    reg(r`工序 3 · 求 \(x\)`, r`
u=\tfrac{1}{2} &\Rightarrow x=2
u=-1 &\Rightarrow x=\tfrac{1}{4}
`),
  ])]},

  11: { ans: r`(B)　\(y=3+2\cos2x\)`, parts: [ P("", [
    reg(r`工序 1 · 中線與振幅`, r`
b &= \tfrac{5+1}{2}=3
a &= \tfrac{5-1}{2}=2
`),
    reg(r`工序 2 · 定週期`, r`
\text{半週期} &= \tfrac{\pi}{2}
T=\pi &\Rightarrow \omega=2
`),
    reg(r`工序 3 · 結論`, r`
y &= 3+2\cos2x
`),
  ])]},

  12: { ans: r`(E)　\(3x+y-4=0\)`, parts: [ P("", [
    reg(r`工序 1 · 中點`, r`
M &= (2,-2)
`),
    reg(r`工序 2 · 斜率與垂線`, r`
k_{PQ} &= \tfrac{1}{3}
m &= -3
`),
    reg(r`工序 3 · 點斜式`, r`
y+2 &= -3(x-2)
3x+y-4 &= 0
`),
  ])]},

  13: { ans: r`(D)　\(10\) 和 \(1\)`, parts: [ P("", [
    reg(r`工序 1 · 平均乘 10`, r`
\bar{x}' &= 10\times1=10
`),
    reg(r`工序 2 · 方差乘 \(10^2\)`, r`
s'^2 &= 10^2\times0.01=1
`),
  ])]},

  14: { ans: r`(A)　\(68-2\sqrt{1155}\)`, parts: [ P("", [
    reg(r`工序 1 · 分子提 2`, r`
\sqrt{140}-\sqrt{132} &= 2(\sqrt{35}-\sqrt{33})
`),
    reg(r`工序 2 · 有理化（乘共軛）`, r`
\text{原式} &= \frac{2(\sqrt{35}-\sqrt{33})^2}{35-33}
`),
    reg(r`工序 3 · 展開`, r`
&= \frac{2(68-2\sqrt{1155})}{2}
&= 68-2\sqrt{1155}
`),
  ])]},

  15: { ans: r`(C)　\(ab_{\min}=\tfrac{80}{9}\)`, parts: [ P("", [
    reg(r`工序 1 · 算幾不等式`, r`
3 &= \tfrac{5}{a}+\tfrac{4}{b}
&\ge 2\sqrt{\tfrac{20}{ab}}
`),
    reg(r`工序 2 · 平方求下界`, r`
9 &\ge \tfrac{80}{ab}
ab &\ge \tfrac{80}{9}
`),
    reg(r`工序 3 · 最小值`, r`
ab_{\min} &= \tfrac{80}{9}
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(\tfrac{2}{7}\)　(b) \(\tfrac{1}{210}\)`, parts: [
    P(r`（a）中英數各一本`, [
      reg(r`工序 1 · 總取法與有利`, r`
\binom{9}{3} &= 84
4\times2\times3 &= 24
`),
      reg(r`工序 2 · 概率`, r`
P &= \tfrac{24}{84}=\tfrac{2}{7}
`),
    ]),
    P(r`（b）同類相鄰`, [
      reg(r`工序 3 · 捆綁法`, r`
\text{有利} &= 3!\cdot4!\cdot2!\cdot3!
`),
      reg(r`工序 4 · 概率`, r`
P &= \frac{3!\,4!\,2!\,3!}{9!}
&= \frac{1}{210}
`),
    ]),
  ]},

  2: { ans: r`(a) \((x-4)^2+(y-4)^2=\tfrac{16}{5}\)　(b) \(m=\tfrac{1}{2}\)`, parts: [
    P(r`（a）求圓的方程`, [
      reg(r`工序 1 · 半徑 = 圓心到 \(L_1\) 距`, r`
r &= \frac{|2(4)-4|}{\sqrt5}
&= \frac{4}{\sqrt5}
`),
      reg(r`工序 2 · 圓方程`, r`
(x-4)^2+(y-4)^2 &= \tfrac{16}{5}
`),
    ]),
    P(r`（b）求 \(m\)`, [
      reg(r`工序 3 · \(L_2\) 也相切`, r`
\frac{|4m-4|}{\sqrt{m^2+1}} &= \frac{4}{\sqrt5}
`),
      reg(r`工序 4 · 解 \(m\)`, r`
5(m-1)^2 &= m^2+1
(m-2)(2m-1) &= 0
m &= \tfrac{1}{2}\ (\ne 2)
`),
    ]),
  ]},

  3: { ans: r`(a)(b) 見證明　(c) \(x=\dfrac{ma}{\sqrt{1-m^2}}\)`, parts: [
    P(r`（a）證恆等式`, [
      reg(r`工序 1 · 展開右邊`, r`
a^2-(x-my)^2 &= a^2-x^2+2mxy-m^2y^2
`),
      reg(r`工序 2 · 代入已知 \(a^2\)`, r`
&= y^2-m^2y^2
&= (1-m^2)y^2\ \square
`),
    ]),
    P(r`（b）證 \(y\) 最大`, [
      reg(r`工序 3 · 解 \(y^2\)`, r`
y^2 &= \frac{a^2-(x-my)^2}{1-m^2}
`),
      reg(r`工序 4 · 最大條件`, r`
(x-my)^2\ge0 &\Rightarrow x=my\ \text{時最大}
`),
    ]),
    P(r`（c）求 \(x\)`, [
      reg(r`工序 5 · 代回求 \(x\)`, r`
y_{\max} &= \frac{a}{\sqrt{1-m^2}}
x &= my_{\max}=\frac{ma}{\sqrt{1-m^2}}
`),
    ]),
  ]},

  4: { ans: r`(a) \(a_n=2n-1\)　(b) \(n=10\)`, parts: [
    P(r`（a）求通項`, [
      reg(r`工序 1 · 公差與首項`, r`
18d &= 36
d &= 2
a_1 &= 1
`),
      reg(r`工序 2 · 通項`, r`
a_n &= 2n-1
`),
    ]),
    P(r`（b）求 \(n\)`, [
      reg(r`工序 3 · 裂項`, r`
\frac{1}{a_na_{n+1}} &= \frac{1}{2}\left(\frac{1}{2n-1}-\frac{1}{2n+1}\right)
`),
      reg(r`工序 4 · 求和`, r`
S_n &= \frac{n}{2n+1}
`),
      reg(r`工序 5 · 解 \(n\)`, r`
\frac{n}{2n+1} &= \frac{10}{21}
21n &= 20n+10
n &= 10
`),
    ]),
  ]},

  5: { ans: r`(a) \(\sin^2C=\tfrac{2}{3}\)　(b) 面積 \(=\dfrac{25\sqrt2}{2}\)`, parts: [
    P(r`（a）求 \(\sin^2 C\)`, [
      reg(r`工序 1 · 定角`, r`
C-A &= 90^\circ
\sin B &= \tfrac{1}{3}
`),
      reg(r`工序 2 · 求 \(\cos2C\)`, r`
2C &= 270^\circ-B
\cos2C &= -\sin B=-\tfrac{1}{3}
`),
      reg(r`工序 3 · 二倍角求 \(\sin^2C\)`, r`
-\tfrac{1}{3} &= 1-2\sin^2C
\sin^2C &= \tfrac{2}{3}
`),
    ]),
    P(r`（b）求面積`, [
      reg(r`工序 4 · 求 \(\cos C,\sin A\)`, r`
\cos C &= -\tfrac{\sqrt3}{3}
\sin A &= -\cos C=\tfrac{\sqrt3}{3}
`),
      reg(r`工序 5 · 正弦定理求 \(BC\)`, r`
BC &= \frac{AC\sin A}{\sin B}
&= 5\sqrt3
`),
      reg(r`工序 6 · 面積`, r`
\text{面積} &= \tfrac{1}{2}\cdot5\sqrt3\cdot5\cdot\sqrt{\tfrac{2}{3}}
&= \tfrac{25\sqrt2}{2}
`),
    ]),
  ]},
};

module.exports = { choice, solution };
