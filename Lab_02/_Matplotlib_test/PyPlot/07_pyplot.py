# ────────────────────────────────────────────────────────────────
# 3. Настройка элементов графика
# ────────────────────────────────────────────────────────────────
# Основные темы урока (примерно страницы 37–77 учебника):
#
# 1. Легенда — как её создавать, перемещать, оформлять, делать вне графика
# 2. GridSpec — гибкая (самая мощная) система размещения нескольких графиков на одной фигуре
# 3. Текстовые элементы:
#    • suptitle — общий заголовок всей фигуры
#    • title — заголовок каждого отдельного графика (Axes)
#    • xlabel / ylabel — подписи осей
#    • text — произвольный текст в координатах данных
#    • annotate — текст + стрелка-указатель
#    • figtext — текст относительно всей фигуры (не привязан к осям)
# 4. Свойства текста (класс matplotlib.text.Text):
#    размер, стиль, жирность, поворот, выравнивание, фоновая рамка и др.
# 5. Colorbar — цветовая шкала (здесь показан базовый пример)

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# ────────────────────────────────────────────────────────────────
# Подготовка данных, которые будем использовать во всех примерах
# ────────────────────────────────────────────────────────────────
x = np.linspace(0, 10, 200)                     # 200 точек от 0 до 10 — гладкая кривая
y1 = np.sin(x) * 2 + np.random.normal(0, 0.25, len(x))   # синусоида + небольшой шум
y2 = np.cos(x) * 1.8 + np.random.normal(0, 0.2, len(x))  # косинусоида + шум
y3 = x**1.5 / 5                                 # степенная функция для разнообразия

# ────────────────────────────────────────────────────────────────
# Пример 1. Работа с легендой — все основные варианты
# ────────────────────────────────────────────────────────────────

fig1, axes1 = plt.subplots(2, 2, figsize=(14, 10))
fig1.suptitle("Урок 3.1 — Легенда: от простого до сложного", fontsize=18, y=0.98)

# График 1 — самая простая легенда (автоматическая)
ax = axes1[0, 0]
ax.plot(x, y1, 'b-', linewidth=2, label='Синусоида + шум')
ax.plot(x, y2, 'r--', linewidth=2, label='Косинусоида + шум')
ax.legend()                                 # по умолчанию — в лучшем свободном месте
ax.set_title("1. Автоматическая легенда (label + legend())")
ax.grid(alpha=0.3)

# График 2 — задаём свои названия и выбираем место
ax = axes1[0, 1]
ax.plot(x, y1, 'b-')
ax.plot(x, y2, 'r--')
ax.legend(['Синяя кривая (sin)', 'Красная кривая (cos)'],
          loc='upper right', fontsize=10, framealpha=0.95)
ax.set_title("2. legend() с собственными названиями")
ax.grid(alpha=0.3)

# График 3 — меняем порядок элементов в легенде + handles
ax = axes1[1, 0]
line1, = ax.plot(x, y1, 'b-', lw=2.5)
line2, = ax.plot(x, y2, 'r--', lw=2.5)
ax.legend([line2, line1], ['Сначала красная', 'Потом синяя'],
          loc='lower center', ncol=2, fontsize=10)
ax.set_title("3. Управление порядком и расположением (handles)")
ax.grid(alpha=0.3)

# График 4 — легенда ВНЕ графика + красивое оформление
ax = axes1[1, 1]
ax.plot(x, y1, 'teal', label='Синус')
ax.plot(x, y2, 'coral', label='Косинус')
ax.plot(x, y3, 'purple', label='Степень 1.5')
ax.legend(
    loc='upper left',
    bbox_to_anchor=(1.02, 1),               # 1.02 — чуть правее правого края осей
    fontsize=11,
    title='Легенда кривых',                 # заголовок самой легенды
    title_fontsize=12,
    frameon=True,
    edgecolor='navy',
    facecolor='#f8f8ff',
    shadow=True,
    borderpad=1
)
ax.set_title("4. Легенда снаружи + стиль")
ax.grid(alpha=0.3)

fig1.tight_layout(rect=[0, 0, 1, 0.96])     # оставляем место под suptitle

# ────────────────────────────────────────────────────────────────
# Пример 2. GridSpec — гибкое размещение графиков
# ────────────────────────────────────────────────────────────────

fig2 = plt.figure(figsize=(15, 9))
fig2.suptitle("Урок 3.2 — GridSpec: произвольная компоновка", fontsize=18)

# Создаём сетку 4 строки × 5 столбцов с разными пропорциями
gs = fig2.add_gridspec(
    nrows=4,
    ncols=5,
    width_ratios=[1, 1, 1.4, 0.8, 0.6],     # разная ширина столбцов
    height_ratios=[1.2, 1, 1, 0.7],          # разная высота строк
    wspace=0.35,                             # расстояние между графиками по горизонтали
    hspace=0.4                               # по вертикали
)

# Большой график — занимает всю первую строку и 4 столбца
ax_big = fig2.add_subplot(gs[0, 0:4])
ax_big.plot(x, y1, 'b-', lw=1.8, label='sin')
ax_big.plot(x, y2, 'r--', lw=1.8, label='cos')
ax_big.legend(loc='upper right')
ax_big.set_title("Большой график — gs[0, 0:4]")
ax_big.grid(alpha=0.25)

# Маленький график справа от большого (zoom)
ax_zoom = fig2.add_subplot(gs[0, 4])
ax_zoom.plot(x[30:70], y1[30:70], 'g.-', ms=5)
ax_zoom.set_title("Zoom-фрагмент")

# Вторая строка — два графика разного размера
ax_left = fig2.add_subplot(gs[1, 0:2])
ax_left.plot(x, y1**2, 'purple', lw=1.5)
ax_left.set_title("Левая часть второй строки")

ax_right = fig2.add_subplot(gs[1, 2:5])
ax_right.plot(x, y3, 'darkorange')
ax_right.set_title("Правая часть — шире")

# Третья строка — один график на всю ширину
ax_full = fig2.add_subplot(gs[2, :])
ax_full.plot(x, y1 + y2, 'k-', lw=2.2)
ax_full.set_title("Третья строка — на всю ширину (gs[2, :])")

# Четвёртая строка — маленький график внизу справа
ax_small = fig2.add_subplot(gs[3, 3:5])
ax_small.hist(y2, bins=25, color='lightblue', edgecolor='navy')
ax_small.set_title("Гистограмма внизу")

fig2.tight_layout()

# ────────────────────────────────────────────────────────────────
# Пример 3. Текстовые элементы + свойства текста
# ────────────────────────────────────────────────────────────────

fig3 = plt.figure(figsize=(12, 8))
fig3.suptitle("Урок 3.3–3.4 — Все виды текста на графике", fontsize=20, y=1.02)

gs3 = fig3.add_gridspec(2, 2, wspace=0.3, hspace=0.35)

axA = fig3.add_subplot(gs3[0, 0])
axB = fig3.add_subplot(gs3[0, 1])
axC = fig3.add_subplot(gs3[1, :])

# График A — подписи осей и заголовок
axA.plot(x, y1, 'teal', lw=2)
axA.set_title("Заголовок графика (set_title)", fontsize=14, pad=12, color='darkblue')
axA.set_xlabel("Подпись оси X (xlabel)", fontsize=12, labelpad=10)
axA.set_ylabel("Подпись оси Y", fontsize=12, rotation=0, labelpad=25, va='center')
axA.grid(alpha=0.3)

# График B — text() и annotate()
axB.plot(x, y2, 'coral', lw=2)
axB.text(1.5, 1.8, "text(x,y,\nпроизвольный текст)", 
         fontsize=13, color='darkred', ha='left', va='top',
         bbox=dict(facecolor='yellow', alpha=0.25, edgecolor='orange', boxstyle='round,pad=0.6'))
axB.annotate('annotate — стрелка указывает сюда',
             xy=(7.5, 0.2),                   # куда указывает стрелка
             xytext=(2, 1.2),                 # где находится текст
             fontsize=12, color='indigo',
             arrowprops=dict(facecolor='black', width=2, headwidth=10, shrink=0.05))
axB.set_title("text() и annotate() со стрелкой")

# График C — разные стили текста + figtext
axC.plot(x, np.sin(x)*np.cos(x*1.3), 'm-', lw=2.5)

# Примеры разных свойств текста
axC.text(1, 0.9, "Жирный + курсив + поворот", 
         fontsize=13, fontweight='bold', fontstyle='italic', rotation=15,
         color='darkgreen', backgroundcolor='lightyellow')

axC.text(4, -0.8, "С рамкой и выравниванием", 
         fontsize=12, ha='center', va='center',
         bbox=dict(facecolor='lightgray', edgecolor='gray', boxstyle='round,pad=0.8', alpha=0.7))

axC.text(8, 0.4, "Обычный текст", fontsize=11)

# Текст на всю фигуру (независимо от осей)
fig3.text(0.01, 0.01, "figtext — текст привязан к фигуре, а не к осям", 
          fontsize=10, color='gray', ha='left', va='bottom')

axC.set_title("Разные свойства текста в одном графике")

# Вместо tight_layout() можно попробовать так (если предупреждение раздражает):
# fig3.tight_layout(rect=[0, 0.03, 1, 0.95])   # оставляем место снизу и сверху

plt.show()