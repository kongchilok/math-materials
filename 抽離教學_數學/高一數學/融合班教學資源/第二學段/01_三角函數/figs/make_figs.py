# -*- coding: utf-8 -*-
"""融合班三角函數講義配圖（黑白列印友善）"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12

OUT = os.path.dirname(os.path.abspath(__file__))
GREY = '0.35'

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close(fig)
    print('saved', name)

# ---------- fig1 象限與終邊 ----------
fig, ax = plt.subplots(figsize=(4.6, 4.6))
for s in ['top', 'right', 'bottom', 'left']:
    ax.spines[s].set_visible(False)
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)
ax.annotate('', xy=(1.25, 0), xytext=(-1.25, 0),
            arrowprops=dict(arrowstyle='->', lw=1.2))
ax.annotate('', xy=(0, 1.25), xytext=(0, -1.25),
            arrowprops=dict(arrowstyle='->', lw=1.2))
ax.text(1.28, 0.02, 'x', fontsize=13, style='italic')
ax.text(0.04, 1.27, 'y', fontsize=13, style='italic')
ax.text(0.62, 0.62, '第一象限', fontsize=13, ha='center')
ax.text(-0.62, 0.62, '第二象限', fontsize=13, ha='center')
ax.text(-0.62, -0.62, '第三象限', fontsize=13, ha='center')
ax.text(0.62, -0.62, '第四象限', fontsize=13, ha='center')
# 例: 150° 終邊
th = np.deg2rad(150)
ax.annotate('', xy=(1.05*np.cos(th), 1.05*np.sin(th)), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1.8))
arc_t = np.linspace(0, th, 60)
ax.plot(0.3*np.cos(arc_t), 0.3*np.sin(arc_t), color=GREY, lw=1.2)
ax.text(0.36*np.cos(th*0.55), 0.4*np.sin(th*0.55), '150°', fontsize=12)
ax.text(1.02*np.cos(th)-0.32, 1.08*np.sin(th)+0.05, '終邊', fontsize=12)
ax.text(0.42, -0.08, '始邊', fontsize=12)
ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35)
ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
save(fig, 'fig1_象限與終邊.png')

# ---------- fig2 單位圓定義 ----------
fig, ax = plt.subplots(figsize=(4.8, 4.8))
t = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(t), np.sin(t), color='black', lw=1.3)
ax.axhline(0, color=GREY, lw=1)
ax.axvline(0, color=GREY, lw=1)
th = np.deg2rad(53)  # P(0.6,0.8)
Px, Py = np.cos(th), np.sin(th)
ax.annotate('', xy=(1.15*Px, 1.15*Py), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1.8))
ax.plot([Px], [Py], 'ko', ms=6)
ax.plot([Px, Px], [0, Py], ls='--', color=GREY, lw=1.2)
ax.plot([0, Px], [Py, Py], ls='--', color=GREY, lw=1.2)
arc_t = np.linspace(0, th, 40)
ax.plot(0.28*np.cos(arc_t), 0.28*np.sin(arc_t), color=GREY, lw=1.2)
ax.text(0.33*np.cos(th/2), 0.33*np.sin(th/2), 'α', fontsize=14, style='italic')
ax.text(Px+0.06, Py+0.05, 'P(x, y)', fontsize=13, style='italic')
ax.text(Px-0.03, -0.16, 'x', fontsize=12, style='italic')
ax.text(-0.13, Py-0.02, 'y', fontsize=12, style='italic')
ax.text(0.52, -0.35, '半徑 r = 1', fontsize=11)
ax.text(1.18, 0.02, 'x', fontsize=13, style='italic')
ax.text(0.04, 1.2, 'y', fontsize=13, style='italic')
ax.annotate('', xy=(1.3, 0), xytext=(-1.3, 0),
            arrowprops=dict(arrowstyle='->', lw=1))
ax.annotate('', xy=(0, 1.3), xytext=(0, -1.3),
            arrowprops=dict(arrowstyle='->', lw=1))
ax.text(-0.1, -0.13, 'O', fontsize=12)
ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)
ax.set_aspect('equal'); ax.axis('off')
save(fig, 'fig2_單位圓定義.png')

# ---------- fig3 誘導公式對稱 ----------
fig, ax = plt.subplots(figsize=(5.0, 5.0))
t = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(t), np.sin(t), color='black', lw=1.3)
ax.axhline(0, color=GREY, lw=1)
ax.axvline(0, color=GREY, lw=1)
th = np.deg2rad(35)
pts = {
    'α 的終邊 P(x, y)': th,
    'π-α 的終邊\n(-x, y)': np.pi - th,
    'π+α 的終邊\n(-x, -y)': np.pi + th,
    '-α 的終邊\n(x, -y)': -th,
}
offsets = {th: (0.08, 0.06), np.pi-th: (-0.72, 0.08),
           np.pi+th: (-0.72, -0.22), -th: (0.08, -0.18)}
for label, ang in pts.items():
    x, y = np.cos(ang), np.sin(ang)
    ax.annotate('', xy=(x, y), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    ax.plot([x], [y], 'ko', ms=5)
    dx, dy = offsets[ang]
    ax.text(x+dx, y+dy, label, fontsize=10.5)
ax.plot([np.cos(th), -np.cos(th)], [np.sin(th), np.sin(th)],
        ls=':', color=GREY, lw=1)
ax.plot([np.cos(th), np.cos(th)], [np.sin(th), -np.sin(th)],
        ls=':', color=GREY, lw=1)
ax.plot([np.cos(th), -np.cos(th)], [np.sin(th), -np.sin(th)],
        ls=':', color=GREY, lw=1)
ax.set_xlim(-1.75, 1.75); ax.set_ylim(-1.55, 1.55)
ax.set_aspect('equal'); ax.axis('off')
save(fig, 'fig3_誘導公式對稱.png')

# ---------- fig4 sin 與 cos 曲線 ----------
fig, axes = plt.subplots(2, 1, figsize=(7.6, 5.2), sharex=True)
x = np.linspace(-2*np.pi, 2*np.pi, 600)
ticks = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0,
         np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
ticklabels = ['-2π', '-3π/2', '-π', '-π/2', '0',
              'π/2', 'π', '3π/2', '2π']
for ax, f, name in [(axes[0], np.sin, 'y = sin x'),
                    (axes[1], np.cos, 'y = cos x')]:
    ax.plot(x, f(x), color='black', lw=1.8)
    ax.axhline(0, color=GREY, lw=0.8)
    ax.axhline(1, color=GREY, lw=0.6, ls='--')
    ax.axhline(-1, color=GREY, lw=0.6, ls='--')
    ax.set_yticks([-1, 0, 1])
    ax.set_xticks(ticks)
    ax.set_xticklabels(ticklabels)
    ax.grid(axis='x', color='0.85', lw=0.6)
    ax.set_title(name, fontsize=13, style='italic', loc='left')
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
fig.tight_layout()
save(fig, 'fig4_sin_cos曲線.png')

# ---------- fig5 五點法空白格線 (0~2π) ----------
def five_point_grid(fname, ymin=-2.5, ymax=2.5):
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    ticks5 = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    labels5 = ['0', 'π/2', 'π', '3π/2', '2π']
    ax.set_xticks(ticks5)
    ax.set_xticklabels(labels5, fontsize=12)
    yt = np.arange(np.ceil(ymin), np.floor(ymax)+0.5, 1)
    ax.set_yticks(yt)
    ax.set_xlim(-0.35, 2*np.pi+0.35)
    ax.set_ylim(ymin, ymax)
    ax.grid(True, color='0.8', lw=0.7)
    ax.axhline(0, color='black', lw=1.1)
    ax.axvline(0, color='black', lw=1.1)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    ax.text(2*np.pi+0.38, -0.12, 'x', fontsize=13, style='italic')
    ax.text(0.06, ymax-0.25, 'y', fontsize=13, style='italic')
    fig.tight_layout()
    save(fig, fname)

five_point_grid('fig5_五點法格線.png')
five_point_grid('fig5b_五點法格線2.png')

# ---------- fig5ans 五點法答案曲線 ----------
def five_point_answer(fname, f, label, ymin=-2.5, ymax=2.5):
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    ticks5 = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    labels5 = ['0', 'π/2', 'π', '3π/2', '2π']
    x = np.linspace(0, 2*np.pi, 400)
    ax.plot(x, f(x), color='black', lw=1.8)
    xs = np.array(ticks5)
    ax.plot(xs, f(xs), 'ko', ms=6)
    ax.set_xticks(ticks5)
    ax.set_xticklabels(labels5, fontsize=12)
    yt = np.arange(np.ceil(ymin), np.floor(ymax)+0.5, 1)
    ax.set_yticks(yt)
    ax.set_xlim(-0.35, 2*np.pi+0.35)
    ax.set_ylim(ymin, ymax)
    ax.grid(True, color='0.8', lw=0.7)
    ax.axhline(0, color='black', lw=1.1)
    ax.axvline(0, color='black', lw=1.1)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
    ax.set_title(label, fontsize=12, loc='left')
    fig.tight_layout()
    save(fig, fname)

five_point_answer('fig5ans_y=1+sinx.png', lambda x: 1+np.sin(x), 'y = 1 + sin x（0 ~ 2π）')
five_point_answer('fig5ans_y=2cosx-1.png', lambda x: 2*np.cos(x)-1, 'y = 2cos x - 1（0 ~ 2π）', ymin=-3.5, ymax=3.5)

# ---------- fig6 圖像變換四格 ----------
fig, axes = plt.subplots(2, 2, figsize=(8.6, 5.6))
x = np.linspace(0, 2*np.pi, 500)
panels = [
    (axes[0][0], lambda x: 2*np.sin(x), 'y = 2sin x（縱向伸長 2 倍）'),
    (axes[0][1], lambda x: np.sin(2*x), 'y = sin 2x（週期變 π）'),
    (axes[1][0], lambda x: np.sin(x+np.pi/4), 'y = sin(x + π/4)（左移 π/4）'),
    (axes[1][1], lambda x: np.sin(x)+1, 'y = sin x + 1（上移 1）'),
]
ticks5 = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
labels5 = ['0', 'π/2', 'π', '3π/2', '2π']
for ax, f, title in panels:
    ax.plot(x, np.sin(x), color='0.6', lw=1.2, ls='--', label='y = sin x')
    ax.plot(x, f(x), color='black', lw=1.8)
    ax.axhline(0, color=GREY, lw=0.7)
    ax.set_xticks(ticks5)
    ax.set_xticklabels(labels5, fontsize=9)
    ax.set_ylim(-2.4, 2.4)
    ax.set_yticks([-2, -1, 0, 1, 2])
    ax.tick_params(labelsize=9)
    ax.set_title(title, fontsize=10.5)
    ax.grid(axis='x', color='0.88', lw=0.5)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
axes[0][0].legend(fontsize=9, loc='lower left', frameon=False)
fig.tight_layout()
save(fig, 'fig6_圖像變換.png')

# ---------- fig7 由圖求解析式（練習③B用） y=2sin(2x+π/6) ----------
fig, ax = plt.subplots(figsize=(7.2, 4.0))
x = np.linspace(-np.pi/6, 2*np.pi-np.pi/6, 500)
ax.plot(x, 2*np.sin(2*x+np.pi/6), color='black', lw=1.8)
ax.axhline(0, color='black', lw=1.0)
ax.axvline(0, color='black', lw=1.0)
# 最高點 (π/6, 2)
ax.plot([np.pi/6], [2], 'ko', ms=6)
ax.plot([np.pi/6, np.pi/6], [0, 2], ls='--', color=GREY, lw=1)
ax.plot([0, np.pi/6], [2, 2], ls='--', color=GREY, lw=1)
ticks7 = [-np.pi/12, np.pi/6, 5*np.pi/12, 2*np.pi/3, 11*np.pi/12, 7*np.pi/6]
labels7 = ['-π/12', 'π/6', '5π/12', '2π/3', '11π/12', '7π/6']
ax.set_xticks(ticks7)
ax.set_xticklabels(labels7, fontsize=10)
ax.set_yticks([-2, -1, 1, 2])
ax.set_ylim(-2.6, 2.6)
ax.set_xlim(-0.55, 2*np.pi-0.4)
ax.grid(axis='x', color='0.88', lw=0.5)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
ax.text(2*np.pi-0.42, -0.3, 'x', fontsize=13, style='italic')
ax.text(0.06, 2.35, 'y', fontsize=13, style='italic')
fig.tight_layout()
save(fig, 'fig7_求解析式.png')

# ---------- fig8 三角函數符號口訣 ----------
fig, ax = plt.subplots(figsize=(4.6, 4.6))
ax.axhline(0, color='black', lw=1.2)
ax.axvline(0, color='black', lw=1.2)
ax.text(0.5, 0.55, '第一象限\n全部為正\nsin + cos + tan +',
        fontsize=11, ha='center')
ax.text(-0.5, 0.55, '第二象限\n只有 sin 為正\nsin + cos - tan -',
        fontsize=11, ha='center')
ax.text(-0.5, -0.72, '第三象限\n只有 tan 為正\nsin - cos - tan +',
        fontsize=11, ha='center')
ax.text(0.5, -0.72, '第四象限\n只有 cos 為正\nsin - cos + tan -',
        fontsize=11, ha='center')
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05)
ax.set_aspect('equal'); ax.axis('off')
save(fig, 'fig8_符號口訣.png')

print('ALL FIGURES DONE')
