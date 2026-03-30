"""Урок 3. Настройка элементов графика (легенда, GridSpec, текст и т.д.)"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


def run():
    """Запуск всех примеров урока 3"""
    print("=== Урок 3. Настройка элементов графика ===\n")

    x = np.linspace(0, 10, 150)
    y1 = np.sin(x) + 0.15 * np.random.randn(len(x))
    y2 = np.cos(x) * 1.4

    # Легенда — разные варианты
    print("1. Разные способы работы с легендой")
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].plot(x, y1, label='Синус + шум')
    axs[0].plot(x, y2, label='Косинус')
    axs[0].legend()
    axs[0].set_title("Обычная легенда")
    axs[0].grid(alpha=0.3)

    axs[1].plot(x, y1, label='Синусоида')
    axs[1].plot(x, y2, label='Косинусоида')
    axs[1].legend(
        loc='upper left',
        bbox_to_anchor=(1.02, 1.0),
        fontsize=10,
        title='Легенда кривых',
        framealpha=0.9,
        shadow=True
    )
    axs[1].set_title("Легенда снаружи графика")
    axs[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()

    # GridSpec — гибкая компоновка
    print("\n2. Пример использования GridSpec")
    fig = plt.figure(figsize=(13, 8))
    gs = gridspec.GridSpec(3, 4,
                           width_ratios=[1, 1, 1.4, 0.7],
                           height_ratios=[1.1, 1, 0.8],
                           wspace=0.35, hspace=0.4)

    ax1 = fig.add_subplot(gs[0, 0:3])
    ax1.plot(x, y1 + y2, 'k-', lw=1.6)
    ax1.set_title("Широкий график (верхняя строка)")

    ax2 = fig.add_subplot(gs[0, 3])
    ax2.plot(x[:50], y1[:50], 'r.-', ms=5)
    ax2.set_title("Увеличенный фрагмент")

    ax3 = fig.add_subplot(gs[1:, :])
    ax3.plot(x, y1, 'b', label='sin(x)')
    ax3.plot(x, y2, 'orange', label='cos(x)')
    ax3.legend(loc='upper right')
    ax3.set_title("Нижняя часть — на всю ширину")
    ax3.grid(True, alpha=0.35)

    fig.suptitle("Пример компоновки с GridSpec", fontsize=16)
    plt.show()

    # Текст и аннотации
    print("\n3. Текстовые элементы и аннотации")
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    ax.plot(x, y1, 'teal', lw=2)
    ax.set_title("Заголовок графика", fontsize=15, color='darkblue', pad=15)
    ax.set_xlabel("Время", fontsize=12)
    ax.set_ylabel("Значение", fontsize=12, rotation=0, labelpad=25)

    ax.text(1.8, 1.4, "Важная зона", fontsize=13,
            bbox=dict(facecolor='yellow', alpha=0.35, edgecolor='orange'))

    ax.annotate("Пик", xy=(np.pi/2, 1.1), xytext=(2, 1.8),
                fontsize=12, color='indigo',
                arrowprops=dict(facecolor='black', shrink=0.06, width=1.8))

    fig.text(0.02, 0.015, "Нижний текст всей фигуры • matplotlib lesson", 
             fontsize=9, color='gray', ha='left')

    plt.show()

    print("\nУрок 3 завершён.\n")


if __name__ == "__main__":
    run()