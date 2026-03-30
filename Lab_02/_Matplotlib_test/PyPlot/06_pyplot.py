# ────────────────────────────────────────────────────────────────
# 2.3 Работа с линейным графиком
# ────────────────────────────────────────────────────────────────
# Линейный график — самый частый тип в Matplotlib.
# Параметры внешнего вида (стиль, цвет, маркер, толщина и др.)
# можно задавать:
#   1. прямо в plt.plot(x, y, color='red', linestyle='--', ...)
#   2. через короткую запись fmt = '[маркер][стиль линии][цвет]'
#   3. через plt.setp(объект_линии, linestyle='--', ...)

# 2.3.1 Стиль линии (linestyle / ls)
# Возможные значения:
#   '-'   или 'solid'     → непрерывная
#   '--'  или 'dashed'    → штриховая
#   '-.'  или 'dashdot'   → штрих-пунктирная
#   ':'   или 'dotted'    → пунктирная
#   'None', ' ', ''       → без линии (только маркеры)

# 2.3.2 Цвет линии (color / c)
# Варианты задания цвета:
#   • имя:           'blue', 'red', 'purple', 'darkgreen'...
#   • короткий код:  'b','g','r','c','m','y','k','w'
#   • HEX:           '#FF5733'
#   • RGB-кортеж:    (0.1, 0.4, 0.8)
#   • серый:         '0.3' (0 = чёрный, 1 = белый)
#   • xkcd:          'xkcd:electric blue'
#   • Tableau:       'tab:blue', 'tab:orange'...

# Короткая запись fmt: стиль + цвет + маркер
# Примеры:  '--r'   → штриховая красная
#           '-.gX'  → штрих-пунктирная зелёная с крестиками

# 2.3.3 Тип графика — линия или маркеры
# Если указан только маркер (без линии) → точечный график
# Популярные маркеры:
#   'o'  — кружок
#   '.'  — маленькая точка
#   'x'  — крестик
#   '+'  — плюс
#   '*'  — звёздочка
#   's'  — квадрат
#   'D'  — ромб
#   '^'  — треугольник вверх и др.

# 2.4 Размещение нескольких графиков
# Два основных простых способа:
# 1. plt.subplot(nrows, ncols, index) или plt.subplot(221)
# 2. fig, axs = plt.subplots(nrows, ncols) → современный и рекомендуемый

# ────────────────────────────────────────────────────────────────
# ПРИМЕР: демонстрация всех основных возможностей
# ────────────────────────────────────────────────────────────────

import matplotlib.pyplot as plt
import numpy as np

# Данные (как в учебнике)
x = np.array([1, 5, 10, 15, 20])
y1 = np.array([1, 7, 3, 5, 11])
y2 = y1 * 1.2 + 1
y3 = y2 * 1.2 + 1
y4 = y3 * 1.2 + 1

# ─── Вариант A: Один график — разные стили и цвета ─────────────────
plt.figure(figsize=(10, 6))
plt.suptitle("Один график: разные стили, цвета, маркеры", fontsize=14)

plt.plot(x, y1, '-',       color='blue',   linewidth=2, label='solid blue')
plt.plot(x, y2, '--',      color='green',  linewidth=2.5, label='dashed green')
plt.plot(x, y3, '-.',      color='red',    linewidth=3,   label='dashdot red')
plt.plot(x, y4, ':',       color='purple', linewidth=2,   label='dotted purple')

# Короткая запись fmt
plt.plot(x, y1 + 15, '--ro', markersize=8, label='dashed red circles')
plt.plot(x, y2 + 20, '-.gX', markersize=9, label='dashdot green X')
plt.plot(x, y3 + 25, ':Ds',  markersize=7, label='dotted orange ромбы')

plt.xlabel('День')
plt.ylabel('Значение')
plt.title('Примеры стилей и маркеров', pad=15)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=9, framealpha=0.9)
plt.tight_layout(rect=[0, 0, 1, 0.94])
# plt.show()   # можно включить позже


# ─── Вариант B: 2×2 сетка графиков через subplots() ────────────────
fig, axs = plt.subplots(2, 2, figsize=(12, 9), sharex=True)
fig.suptitle("Четыре отдельных графика через plt.subplots()", fontsize=16)

# График 1: линия + маркеры
axs[0, 0].plot(x, y1, 'o-', color='darkblue', linewidth=2, markersize=8, label='кружки + линия')
axs[0, 0].set_title("Solid + маркеры")
axs[0, 0].grid(True, linestyle='--', alpha=0.6)
axs[0, 0].legend()

# График 2: только маркеры (без линии)
axs[0, 1].plot(x, y2, 's', color='forestgreen', markersize=10, label='только квадраты')
axs[0, 1].set_title("Только маркеры")
axs[0, 1].grid(True)
axs[0, 1].legend()

# График 3: xkcd-цвет + толстая штриховая
axs[1, 0].plot(x, y3, '--', color='xkcd:electric purple', linewidth=4, label='xkcd цвет')
axs[1, 0].set_title("Штриховая + xkcd")
axs[1, 0].grid(True, color='gray', alpha=0.5)
axs[1, 0].legend()

# График 4: короткая запись + разные маркеры
axs[1, 1].plot(x, y4, '-.m', linewidth=3, label='dashdot magenta')
axs[1, 1].plot(x, y4 + 5, 'D', color='darkorange', markersize=9, label='ромбы')
axs[1, 1].set_title("Короткая запись + маркеры")
axs[1, 1].grid(True)
axs[1, 1].legend()

fig.tight_layout()
fig.subplots_adjust(top=0.92)  # место под suptitle

plt.show()