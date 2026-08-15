// 2023 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(E)　\([4,6)\)`, parts: [ P("", [
    reg(r`工序 1 · 因式分解定 \(M\)`, r`
x^2-2x-8 &= (x-4)(x+2)\ge0
M &= \{x\le-2\ \text{或}\ x\ge4\}
`),
    reg(r`工序 2 · 與 \(N\) 取交集`, r`
M\cap N &= [4,6)
`),
  ])]},

  2: { ans: r`(D)　\(f(3)=7\)`, parts: [ P("", [
    reg(r`工序 1 · 除式的根`, r`
x^2-x-6 &= (x-3)(x+2)
`),
    reg(r`工序 2 · 代 \(x=3\)`, r`
f(3) &= 3(3)-2
&= 7
`),
  ])]},

  3: { ans: r`(C)　\(\tfrac{3}{4}\)`, parts: [ P("", [
    reg(r`工序 1 · 倒數對消`, r`
\log_{12}17\cdot\log_{17}12 &= 1
`),
    reg(r`工序 2 · 換底化簡`, r`
\log_9125\cdot\log_{25}3 &= \frac{3\ln5}{2\ln3}\cdot\frac{\ln3}{2\ln5}
&= \frac{3}{4}
`),
  ])]},

  4: { ans: r`(C)　\(\{-1,4\}\)`, parts: [ P("", [
    reg(r`工序 1 · 換元解 \(t\)`, r`
t=\sqrt{x^2-3x} &\Rightarrow t^2+4t-12=0
(t+6)(t-2) &= 0
t &= 2
`),
    reg(r`工序 2 · 回代解 \(x\)`, r`
x^2-3x-4 &= 0
(x-4)(x+1) &= 0
x &= 4\ \text{或}\ -1
`),
  ])]},

  5: { ans: r`(D)　\(a=-\tfrac{3}{7}\) 或 \(\tfrac{3}{5}\)`, parts: [ P("", [
    reg(r`工序 1 · 二次須 \(\Delta=0\)`, r`
[2(a+3)]^2-4(4a^2)(9) &= 0
(a+3)^2 &= 36a^2
`),
    reg(r`工序 2 · 解 \(a\)`, r`
a+3 &= \pm6a
a &= \tfrac{3}{5}\ \text{或}\ -\tfrac{3}{7}
`),
  ])]},

  6: { ans: r`(C)　\(-160\)`, parts: [ P("", [
    reg(r`工序 1 · 一般項定次方`, r`
T_{k+1} &= \binom{6}{k}(2\sqrt{x})^{6-k}\!\left(-\tfrac{1}{\sqrt{x}}\right)^{k}
3-k &= 0 \Rightarrow k=3
`),
    reg(r`工序 2 · 代入`, r`
T_4 &= \binom{6}{3}2^3(-1)^3
&= -160
`),
  ])]},

  7: { ans: r`(D)　\(\left[-\tfrac{1}{2},\infty\right)\)`, parts: [ P("", [
    reg(r`工序 1 · \(a=0\)`, r`
f(x)=4x+1 &\ \text{（遞增）}
`),
    reg(r`工序 2 · \(a>0\)（軸 \(\le2\)）`, r`
-\tfrac{2}{a}\le2 &\ \text{恆成立}
`),
    reg(r`工序 3 · \(a<0\)（軸 \(\ge4\)）`, r`
-\tfrac{2}{a} &\ge 4
a &\ge -\tfrac{1}{2}
`),
    reg(r`工序 4 · 合併`, r`
a &\ge -\tfrac{1}{2}
`),
  ])]},

  8: { ans: r`(A)　\(-\tfrac{1}{12}<x<\tfrac{1}{12}\)`, parts: [ P("", [
    reg(r`工序 1 · 求 \(f(5)\)`, r`
f(5) &= 25-40+17=2
`),
    reg(r`工序 2 · 用第一段 \(\log_2\)`, r`
\log_2 u+2 &> 0
u &> \tfrac{1}{4}
`),
    reg(r`工序 3 · 解 \(x\)`, r`
\tfrac{1}{2}-3|x| &> \tfrac{1}{4}
|x| &< \tfrac{1}{12}
`),
  ])]},

  9: { ans: r`(E)　\(\tfrac{32}{27}\) 米`, parts: [ P("", [
    reg(r`工序 1 · 球體積`, r`
V &= \tfrac{4}{3}\pi(2)^3=\tfrac{32}{3}\pi
`),
    reg(r`工序 2 · 底面積`, r`
\pi(3)^2 &= 9\pi
`),
    reg(r`工序 3 · 水位上升`, r`
\Delta h &= \frac{32\pi/3}{9\pi}=\tfrac{32}{27}
`),
  ])]},

  10: { ans: r`(B)　\(a_{34}=-82\)`, parts: [ P("", [
    reg(r`工序 1 · 公差`, r`
9d &= 26-80=-54
d &= -6
`),
    reg(r`工序 2 · 第 34 項`, r`
a_{34} &= 26+18(-6)
&= -82
`),
  ])]},

  11: { ans: r`(A)　\(4x+3y+14=0\)`, parts: [ P("", [
    reg(r`工序 1 · 中點`, r`
M &= (-2,-2)
`),
    reg(r`工序 2 · 垂線斜率`, r`
m &= -\tfrac{4}{3}
`),
    reg(r`工序 3 · 點斜式`, r`
y+2 &= -\tfrac{4}{3}(x+2)
4x+3y+14 &= 0
`),
  ])]},

  12: { ans: r`(E)　最小值 \(=8\)`, parts: [ P("", [
    reg(r`工序 1 · 離心率求關係`, r`
9a^2 &= a^2+b^2
b^2 &= 8a^2
`),
    reg(r`工序 2 · 目標式`, r`
\frac{b^2+2}{a} &= 8a+\frac{2}{a}
`),
    reg(r`工序 3 · 算幾不等式`, r`
8a+\frac{2}{a} &\ge 2\sqrt{16}
&= 8
`),
  ])]},

  13: { ans: r`(A)　\(\dfrac{-6-4\sqrt{21}}{25}\)`, parts: [ P("", [
    reg(r`工序 1 · 兩餘弦（第二象限取負）`, r`
\cos A &= -\tfrac{\sqrt{21}}{5}
\cos B &= -\tfrac{3}{5}
`),
    reg(r`工序 2 · 和角公式`, r`
\sin(A+B) &= \sin A\cos B+\cos A\sin B
&= \tfrac{2}{5}\!\left(-\tfrac{3}{5}\right)+\!\left(-\tfrac{\sqrt{21}}{5}\right)\!\tfrac{4}{5}
&= \frac{-6-4\sqrt{21}}{25}
`),
  ])]},

  14: { ans: r`(B)　\(a=-2,\ b=2\)`, parts: [ P("", [
    reg(r`工序 1 · 由最大／最小定 \(a,b\)`, r`
b+|a| &= 4
|a|=2,\ b &= 2
`),
    reg(r`工序 2 · 由遞減定符號`, r`
x=0\ \text{附近遞減} &\Rightarrow a<0
a &= -2
`),
  ])]},

  15: { ans: r`(E)　\(D=(3,-5)\)`, parts: [ P("", [
    reg(r`工序 1 · 順時針轉 \(90^\circ\)`, r`
A(-2,3) &\to B(3,2)
`),
    reg(r`工序 2 · 對 \(x\) 軸對稱`, r`
B &\to C(3,-2)
`),
    reg(r`工序 3 · 下移 3`, r`
C &\to D(3,-5)
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(\tfrac{13}{4}\!\left(\tfrac34\right)^{9}\)　(b) \(\dfrac{3^9}{4^{10}}\)　(c) \(\left(\tfrac34\right)^{9}\)`, parts: [
    P(r`（a）最多一次正面`, [
      reg(r`工序 1 · 0 次與 1 次`, r`
P_0 &= \left(\tfrac{3}{4}\right)^{10}
P_1 &= \binom{10}{1}\tfrac{1}{4}\left(\tfrac{3}{4}\right)^9
`),
      reg(r`工序 2 · 合計`, r`
P &= \tfrac{13}{4}\left(\tfrac{3}{4}\right)^9
`),
    ]),
    P(r`（b）第十次才首次正面`, [
      reg(r`工序 3 · 前 9 反、第 10 正`, r`
P &= \left(\tfrac{3}{4}\right)^9\cdot\tfrac{1}{4}
&= \frac{3^9}{4^{10}}
`),
    ]),
    P(r`（c）第十次取得第三次正面`, [
      reg(r`工序 4 · 前 9 恰 2 正、第 10 正`, r`
P &= \binom{9}{2}\!\left(\tfrac{1}{4}\right)^2\!\left(\tfrac{3}{4}\right)^7\!\cdot\tfrac{1}{4}
&= \left(\tfrac{3}{4}\right)^9
`),
    ]),
  ]},

  2: { ans: r`(a) \(F=(0,1)\)　(b) \(|AB|=\tfrac{25}{4}\)　(c) \(|CD|=8\sqrt2\)`, parts: [
    P(r`（a）求焦點`, [
      reg(r`工序 1 · 由 \(x^2=4y\)`, r`
4p &= 4 \Rightarrow p=1
F &= (0,1)
`),
    ]),
    P(r`（b）求 \(|AB|\)`, [
      reg(r`工序 2 · 聯立 \(L_1\)`, r`
x^2 &= 3x+4
x &= -1\ \text{或}\ 4
`),
      reg(r`工序 3 · 焦點弦長`, r`
|AB| &= y_A+y_B+2
&= \tfrac{1}{4}+4+2=\tfrac{25}{4}
`),
    ]),
    P(r`（c）求 \(|CD|\)`, [
      reg(r`工序 4 · 聯立 \(L_2\) 與韋達`, r`
x^2-4x-4t &= 0
x_1+x_2 &= 4
`),
      reg(r`工序 5 · 用 \(|DM|=3|CM|\)`, r`
x_2 &= -3x_1
x_1=-2,\ x_2 &= 6
`),
      reg(r`工序 6 · 弦長`, r`
|CD| &= \sqrt{2}\,|x_2-x_1|
&= 8\sqrt{2}
`),
    ]),
  ]},

  3: { ans: r`(a) \(k=\tfrac32,\ a_n=2\cdot3^n\)　(b) \(T_n=\tfrac14\!\left(1-\tfrac{1}{3^n}\right)+n+\tfrac{n(n+1)}{2}\log_2 3\)　(c) \(n=2\)`, parts: [
    P(r`（a）求 \(k\) 及 \(a_n\)`, [
      reg(r`工序 1 · 求前三項`, r`
a_1 &= 9-2k
a_2 &= 18
a_3 &= 54
`),
      reg(r`工序 2 · 等比中項求 \(k\)`, r`
(9-2k)(54) &= 18^2
k &= \tfrac{3}{2}
`),
      reg(r`工序 3 · 通項`, r`
a_1=6,\ q &= 3
a_n &= 2\cdot3^n
`),
    ]),
    P(r`（b）求 \(T_n\)`, [
      reg(r`工序 4 · 拆 \(b_n\)`, r`
b_n &= \frac{1}{2\cdot3^n}+1+n\log_2 3
`),
      reg(r`工序 5 · 分組求和`, r`
T_n &= \tfrac{1}{4}\!\left(1-\tfrac{1}{3^n}\right)+n+\tfrac{n(n+1)}{2}\log_2 3
`),
    ]),
    P(r`（c）求 \(f(n)\) 最大時 \(n\)`, [
      reg(r`工序 6 · 頂點 \(c=\tfrac{1}{10}\)`, r`
c_n &= 3^{-n}
f=-5c^2+c,\ \text{頂點} &\ c=\tfrac{1}{10}
`),
      reg(r`工序 7 · 取最近`, r`
n=2 &\Rightarrow c=\tfrac{1}{9}\approx0.111
&\Rightarrow n=2
`),
    ]),
  ]},

  4: { ans: r`(a) \(f(x)=2\sin\!\left(\tfrac23 x-\tfrac{\pi}{6}\right)-1\)　(b) \(\sin A=\dfrac{\sqrt5-1}{2}\)`, parts: [
    P(r`（a）求 \(f(x)\)`, [
      reg(r`工序 1 · 降冪與輔助角`, r`
f(x) &= \sqrt3\sin2\omega x-(1+\cos2\omega x)
&= 2\sin\!\left(2\omega x-\tfrac{\pi}{6}\right)-1
`),
      reg(r`工序 2 · 由週期定 \(\omega\)`, r`
\frac{2\pi}{2\omega} &= 3\pi
\omega &= \tfrac{1}{3}
f(x) &= 2\sin\!\left(\tfrac{2}{3}x-\tfrac{\pi}{6}\right)-1
`),
    ]),
    P(r`（b）求 \(\sin A\)`, [
      reg(r`工序 3 · 由 \(f(C)=0\) 求 \(C\)`, r`
\sin\!\left(\tfrac{2}{3}C-\tfrac{\pi}{6}\right) &= \tfrac{1}{2}
C &= \tfrac{\pi}{2}
`),
      reg(r`工序 4 · 化簡條件`, r`
2\sin^2 B &= \cos B+\sin A
\cos B &= \sin A
`),
      reg(r`工序 5 · 解 \(\sin A\)`, r`
1-\sin^2 A &= \sin A
\sin A &= \tfrac{\sqrt5-1}{2}
`),
    ]),
  ]},

  5: { ans: r`(b) \(-\tfrac{1}{5}\le z\le\tfrac{7}{4}\)　(c) \(t_{\min}=13\)`, parts: [
    P(r`（a）區域頂點`, [
      reg(r`工序 1 · 三邊界與頂點`, r`
&3x+2y=13,\ x=5,\ 2x-2y+3=0
\text{頂點}: A(2,\tfrac{7}{2}),\ B(5,\tfrac{13}{2}) &,\ C(5,-1)
`),
    ]),
    P(r`（b）求 \(z=\tfrac{y}{x}\) 範圍`, [
      reg(r`工序 2 · \(z\) 為連線斜率`, r`
z &= \frac{y}{x}
`),
      reg(r`工序 3 · 頂點取極值`, r`
z_C &= -\tfrac{1}{5}
z_A &= \tfrac{7}{4}
-\tfrac{1}{5}\le z &\le \tfrac{7}{4}
`),
    ]),
    P(r`（c）求 \(t=x^2+y^2\) 最小`, [
      reg(r`工序 4 · 垂足在最近邊界`, r`
OD\perp(3x+2y=13) &\Rightarrow y=\tfrac{2}{3}x
`),
      reg(r`工序 5 · 求交點與最小`, r`
(x,y) &= (3,2)
t_{\min} &= 9+4=13
`),
    ]),
  ]},
};

module.exports = { choice, solution };
