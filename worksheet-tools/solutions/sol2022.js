// 2022 教師版詳解（工序分析法）
const r = String.raw;
const reg = (h, math) => ({ h, math });
const P = (title, regions) => ({ title, regions });

const choice = {
  1: { ans: r`(B)　\(\{x:\sin x+\cos x=3\}\)`, parts: [ P("", [
    reg(r`工序 1 · 逐一檢查其餘`, r`
A=\{0\} &\Rightarrow \text{有元素}
C: x=\pm1 &\Rightarrow \text{有解}
E: (0,0) &\Rightarrow \text{有解}
`),
    reg(r`工序 2 · 檢 B`, r`
\sin x+\cos x &= \sqrt2\sin\!\left(x+\tfrac{\pi}{4}\right)
\max &= \sqrt2<3
&\Rightarrow \text{無解（空集）}
`),
  ])]},

  2: { ans: r`(C)　\(\tfrac{b}{a}<\tfrac{b+m}{a+m}\)`, parts: [ P("", [
    reg(r`工序 1 · 作差`, r`
\frac{b+m}{a+m}-\frac{b}{a} &= \frac{m(a-b)}{a(a+m)}
`),
    reg(r`工序 2 · 判正負`, r`
a>b>0,\ m>0 &\Rightarrow >0
`),
    reg(r`工序 3 · 結論`, r`
\frac{b}{a} &< \frac{b+m}{a+m}
`),
  ])]},

  3: { ans: r`(E)　\(a=-6\)`, parts: [ P("", [
    reg(r`工序 1 · 兩餘數`, r`
P(2) &= 20+2a+b
P(-1) &= 2-a+b
`),
    reg(r`工序 2 · 令相等解 \(a\)`, r`
20+2a &= 2-a
3a &= -18
a &= -6
`),
  ])]},

  4: { ans: r`(B)　\(2-\sqrt3\)`, parts: [ P("", [
    reg(r`工序 1 · 配完全平方`, r`
7-4\sqrt3 &= (2-\sqrt3)^2
`),
    reg(r`工序 2 · 開根（取正）`, r`
\sqrt{7-4\sqrt3} &= |2-\sqrt3|
&= 2-\sqrt3
`),
  ])]},

  5: { ans: r`(D)　\(p\ge-\tfrac{9}{7}\)`, parts: [ P("", [
    reg(r`工序 1 · \(p=0\)（退化）`, r`
-6x-1 &= 0 \ \text{（有實根）}
`),
    reg(r`工序 2 · \(p\ne0\) 判別式`, r`
\Delta &= 4(7p+9)\ge0
p &\ge -\tfrac{9}{7}
`),
    reg(r`工序 3 · 合併`, r`
p &\ge -\tfrac{9}{7}
`),
  ])]},

  6: { ans: r`(A)　\(2\)`, parts: [ P("", [
    reg(r`工序 1 · 化為對數`, r`
\tfrac{1}{a} &= \log_{\sqrt{10}}2
\tfrac{1}{b} &= \log_{\sqrt{10}}5
`),
    reg(r`工序 2 · 相加`, r`
\tfrac{1}{a}+\tfrac{1}{b} &= \log_{\sqrt{10}}10
&= 2
`),
  ])]},

  7: { ans: r`(A)　\(r=84-48\sqrt3\)`, parts: [ P("", [
    reg(r`工序 1 · 相切兩圓水平距`, r`
d &= 2\sqrt{r_1 r_2}
`),
    reg(r`工序 2 · 列方程`, r`
2\sqrt{3r}+2\sqrt{4r} &= 4\sqrt3
\sqrt{r}(\sqrt3+2) &= 2\sqrt3
`),
    reg(r`工序 3 · 解 \(r\)`, r`
\sqrt{r} &= \frac{2\sqrt3}{2+\sqrt3}
r &= 84-48\sqrt3
`),
  ])]},

  8: { ans: r`(D)　\(\tfrac{37}{64}\)`, parts: [ P("", [
    reg(r`工序 1 · 對立事件（零次）`, r`
P(\text{零次}) &= \left(\tfrac{3}{4}\right)^3=\tfrac{27}{64}
`),
    reg(r`工序 2 · 至少一次`, r`
P &= 1-\tfrac{27}{64}=\tfrac{37}{64}
`),
  ])]},

  9: { ans: r`(D)　區域 IV`, parts: [ P("", [
    reg(r`工序 1 · 三條邊界`, r`
&y=2x+4,\ x+y=5,\ y=2
`),
    reg(r`工序 2 · 各取半平面`, r`
y-2x\le4 &:\ \text{下方}
x+y\ge5 &:\ \text{右上}
y\ge2 &:\ \text{上方}
`),
    reg(r`工序 3 · 交集`, r`
&\Rightarrow \text{區域 IV}
`),
  ])]},

  10: { ans: r`(A)　\(\left(0,\tfrac{7}{2}\right)\)`, parts: [ P("", [
    reg(r`工序 1 · 垂線斜率`, r`
m_1 &= \tfrac{2}{3}
m &= -\tfrac{3}{2}
`),
    reg(r`工序 2 · 點斜式求截距`, r`
y-2 &= -\tfrac{3}{2}(x-1)
x=0 &\Rightarrow y=\tfrac{7}{2}
`),
  ])]},

  11: { ans: r`(B)　\(5200\) 人`, parts: [ P("", [
    reg(r`工序 1 · 行數`, r`
6400\div32 &= 200
`),
    reg(r`工序 2 · 每行人數（坐4空1）`, r`
32 &= 5\times6+2
\text{每行} &= 24+2=26
`),
    reg(r`工序 3 · 總數`, r`
200\times26 &= 5200
`),
  ])]},

  12: { ans: r`(E)　\(m=2\)`, parts: [ P("", [
    reg(r`工序 1 · 韋達定理`, r`
x_1+x_2 &= \tfrac{8}{3}
x_1x_2 &= \tfrac{m}{3}
`),
    reg(r`工序 2 · 倒數和 \(=4\)`, r`
\frac{x_1+x_2}{x_1x_2} &= \tfrac{8}{m}=4
m &= 2
`),
  ])]},

  13: { ans: r`(C)　\(\tfrac{3}{5}\)`, parts: [ P("", [
    reg(r`工序 1 · 總取法`, r`
5\times4 &= 20
`),
    reg(r`工序 2 · 有利（十位 1,2,3）`, r`
3\times4 &= 12
`),
    reg(r`工序 3 · 概率`, r`
P &= \tfrac{12}{20}=\tfrac{3}{5}
`),
  ])]},

  14: { ans: r`(C)　\(x=0\)`, parts: [ P("", [
    reg(r`工序 1 · 展開`, r`
6^x-2^x &= 2\cdot2^x-6\cdot6^x+4\cdot2^x
`),
    reg(r`工序 2 · 合併同類`, r`
7\cdot6^x &= 7\cdot2^x
`),
    reg(r`工序 3 · 求 \(x\)`, r`
3^x &= 1
x &= 0
`),
  ])]},

  15: { ans: r`(E)　\(n=2\sqrt3\) 或 \(\sqrt3\)`, parts: [ P("", [
    reg(r`工序 1 · 定內角`, r`
\angle P &= 180^\circ-150^\circ=30^\circ
`),
    reg(r`工序 2 · 餘弦定理`, r`
3 &= n^2+9-6n\cos30^\circ
n^2-3\sqrt3\,n+6 &= 0
`),
    reg(r`工序 3 · 解`, r`
n &= \frac{3\sqrt3\pm\sqrt3}{2}
n &= 2\sqrt3\ \text{或}\ \sqrt3
`),
  ])]},
};

const solution = {
  1: { ans: r`(a) \(a=1,b=-4,c=-5\)　(b) \(y=x^2+2x-5\)　(c) 最大 \(16\)、最小 \(-9\)`, parts: [
    P(r`（a）求 \(a,b,c\)`, [
      reg(r`工序 1 · 頂點式`, r`
f(x) &= a(x-2)^2-9
`),
      reg(r`工序 2 · 過 \((5,0)\) 求 \(a\)`, r`
0 &= 9a-9
a &= 1
f(x) &= x^2-4x-5
`),
    ]),
    P(r`（b）平移後表達式`, [
      reg(r`工序 3 · 左移 3、上移 3`, r`
y &= (x+3)^2-4(x+3)-5+3
&= x^2+2x-5
`),
    ]),
    P(r`（c）求 \(g(x)=f(3\sin x)\) 最值`, [
      reg(r`工序 4 · 換元 \(t=3\sin x\)`, r`
t &\in[-3,3]
g &= (t-2)^2-9
`),
      reg(r`工序 5 · 取最值`, r`
t=-3 &\Rightarrow g=16
t=2 &\Rightarrow g=-9
`),
    ]),
  ]},

  2: { ans: r`(a) \(a_n=\left(\tfrac14\right)^{n-1},\ b_n=\tfrac{n}{4^n}\)　(b) \(S_n=\tfrac43\!\left(1-\tfrac{1}{4^n}\right),\ T_n=\tfrac49\!\left(1-\tfrac{1}{4^n}\right)-\tfrac{n}{3\cdot4^n}\)`, parts: [
    P(r`（a）求通項`, [
      reg(r`工序 1 · 等差中項求 \(q\)`, r`
2(4a_2) &= a_1+16a_3
16q^2-8q+1 &= 0
q &= \tfrac{1}{4}
`),
      reg(r`工序 2 · 通項`, r`
a_n &= \left(\tfrac{1}{4}\right)^{n-1}
b_n &= \tfrac{n}{4^n}
`),
    ]),
    P(r`（b）求 \(S_n,T_n\)`, [
      reg(r`工序 3 · \(S_n\)（等比和）`, r`
S_n &= \frac{1-(1/4)^n}{1-1/4}
&= \tfrac{4}{3}\!\left(1-\tfrac{1}{4^n}\right)
`),
      reg(r`工序 4 · \(T_n\)（錯位相減）`, r`
T_n-\tfrac{1}{4}T_n &= \sum_{k=1}^{n}\tfrac{1}{4^k}-\tfrac{n}{4^{n+1}}
`),
      reg(r`工序 5 · 整理`, r`
T_n &= \tfrac{4}{9}\!\left(1-\tfrac{1}{4^n}\right)-\tfrac{n}{3\cdot4^n}
`),
    ]),
  ]},

  3: { ans: r`(a) \(\dfrac{x^2}{16}+\dfrac{y^2}{32}=1\)　(b) \(k_1k_2=-2\)（得證）`, parts: [
    P(r`（a）求 \(C\) 的方程`, [
      reg(r`工序 1 · 離心率關係`, r`
e=\frac{c}{a}=\frac{\sqrt2}{2} &\Rightarrow a^2=2b^2
`),
      reg(r`工序 2 · 代點求 \(a^2,b^2\)`, r`
\frac{8}{b^2}+\frac{16}{a^2} &= 1
b^2=16,\ a^2 &= 32
`),
      reg(r`工序 3 · 方程`, r`
\frac{x^2}{16}+\frac{y^2}{32} &= 1
`),
    ]),
    P(r`（b）證 \(k_1k_2=-2\)`, [
      reg(r`工序 4 · 點差法`, r`
\frac{(x_1+x_2)(x_1-x_2)}{16}+\frac{(y_1+y_2)(y_1-y_2)}{32} &= 0
`),
      reg(r`工序 5 · 代入斜率`, r`
k_1k_2 &= -\frac{32}{16}
&= -2\ \square
`),
    ]),
  ]},

  4: { ans: r`(a) \(2\cos\!\left(\theta+\tfrac{\pi}{6}\right),\ [-2,2]\)　(b) \(\theta=\tfrac{\pi}{2}\) 或 \(\tfrac{7\pi}{6}\)　(c) \(\dfrac{\sqrt{10}}{4}\)`, parts: [
    P(r`（a）輔助角與範圍`, [
      reg(r`工序 1 · 輔助角公式`, r`
\sqrt3\cos\theta-\sin\theta &= 2\cos\!\left(\theta+\tfrac{\pi}{6}\right)
\text{範圍} &= [-2,2]
`),
    ]),
    P(r`（b）解方程`, [
      reg(r`工序 2 · 化簡`, r`
\cos\!\left(\theta+\tfrac{\pi}{6}\right) &= -\tfrac{1}{2}
`),
      reg(r`工序 3 · 求解`, r`
\theta+\tfrac{\pi}{6} &= \tfrac{2\pi}{3},\ \tfrac{4\pi}{3}
\theta &= \tfrac{\pi}{2},\ \tfrac{7\pi}{6}
`),
    ]),
    P(r`（c）求 \(\sin\!\left(\tfrac{\theta}{2}+\tfrac{\pi}{12}\right)\)`, [
      reg(r`工序 4 · 求 \(\cos\)`, r`
\cos\!\left(\theta+\tfrac{\pi}{6}\right) &= -\tfrac{1}{4}
`),
      reg(r`工序 5 · 二倍角`, r`
-\tfrac{1}{4} &= 1-2\sin^2\!\left(\tfrac{\theta}{2}+\tfrac{\pi}{12}\right)
\sin^2 &= \tfrac{5}{8}
`),
      reg(r`工序 6 · 取正`, r`
\sin\!\left(\tfrac{\theta}{2}+\tfrac{\pi}{12}\right) &= \tfrac{\sqrt{10}}{4}
`),
    ]),
  ]},

  5: { ans: r`對所有正整數 \(n\)，\(14\mid 3^{4n+2}+5^{2n+1}\)（得證）`, parts: [
    P(r`數學歸納法`, [
      reg(r`工序 1 · 基礎 \(n=1\)`, r`
3^6+5^3 &= 729+125
&= 854=14\times61
`),
      reg(r`工序 2 · 歸納假設`, r`
&14\mid(3^{4k+2}+5^{2k+1})
`),
      reg(r`工序 3 · 歸納步 \(n=k+1\)`, r`
3^{4k+6}+5^{2k+3} &= 81\cdot3^{4k+2}+25\cdot5^{2k+1}
&= 56\cdot3^{4k+2}+25(3^{4k+2}+5^{2k+1})
`),
      reg(r`工序 4 · 結論`, r`
56=14\times4 &\Rightarrow \text{兩項皆被 14 整除}
&\Rightarrow S(k+1)\ \square
`),
    ]),
  ]},
};

module.exports = { choice, solution };
