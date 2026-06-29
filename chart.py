import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.random.seed(19680801)

HIST_BINS = np.linspace(-4, 4, 30)
bin_centers = (HIST_BINS[:-1] + HIST_BINS[1:]) / 2

data = np.random.randn(1000)
n, _ = np.histogram(data, HIST_BINS, density=True)

# figsize=(12, 4) — шире, чтобы столбцы смотрелись «растянутыми» по X
fig, ax = plt.subplots(figsize=(12, 4))

width = 0.25
bars = ax.bar(
    bin_centers,
    n,
    width=width,
    edgecolor='#2c3e50',      # спокойный тёмно‑серый контур
    linewidth=1,
    color='#4682b4',         # мягкий светло‑голубой
    alpha=0.9
)

ax.set_xlim(-4, 4)
ax.set_ylim(top=0.5)        # ограничивает высоту столбцов
ax.axis('off')               # убирает оси

def animate(frame_number):
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS, density=True)
    for bar, height in zip(bars, n):
        bar.set_height(height)
    return bars

# interval=300 — задержка 300 мс между кадрами (было ~50–100 по умолчанию)
# можешь ставить 200, 300, 400 и т.д. — чем больше число, тем медленнее
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=50,
    repeat=False,
    blit=True,
    interval=300
)

plt.show()




