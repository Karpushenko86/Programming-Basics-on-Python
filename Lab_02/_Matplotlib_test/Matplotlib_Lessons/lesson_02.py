"""Урок 2. Основы работы с модулем pyplot"""

import matplotlib.pyplot as plt
import numpy as np


def run():
    """Запуск всех примеров урока 2"""
    print("=== Урок 2. Основы pyplot ===\n")

    x = np.array([1, 5, 10, 15, 20])
    y = np.array([1, 7, 3, 5, 11])

    # Текстовые элементы
    print("1. Текстовые надписи на графике")
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'o-', color='darkgreen', linewidth=2, markersize=8, label='Цена стали')
    plt.title("Динамика цены стали", fontsize=14, pad=12)
    plt.xlabel("День", fontsize=12, color='navy')
    plt.ylabel("Цена, у.е.", fontsize=12, color='navy')
    plt.text(12, 6, "Рост!", fontsize=12, color='red', ha='center')
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.5)
    plt.show()

    # Стили линий, цвета, маркеры
    print("\n2. Стили линий, цвета, маркеры")
    plt.figure(figsize=(9, 6))
    plt.plot(x, y, '-', label='solid', color='blue')
    plt.plot(x, y * 1.3, '--', label='dashed', color='green')
    plt.plot(x, y * 0.8, '-.', label='dashdot', color='red')
    plt.plot(x, y * 1.6, ':', label='dotted', color='purple')
    plt.plot(x, y * 0.5 + 12, 's', label='квадраты', color='orange', markersize=9)
    plt.title("Разные стили линий и маркеры")
    plt.xlabel("День")
    plt.ylabel("Значение")
    plt.legend(title="Легенда")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.show()

    # subplots (сетка графиков)
    print("\n3. Несколько графиков через subplots()")
    fig, axs = plt.subplots(2, 2, figsize=(11, 8), sharex=True)
    fig.suptitle("Примеры разных типов графиков", fontsize=16)

    axs[0, 0].plot(x, y, 'b-o', label='линейный + точки')
    axs[0, 0].set_title("Линейный + маркеры")
    axs[0, 0].legend()
    axs[0, 0].grid(True, alpha=0.3)

    axs[0, 1].plot(x, y**2, 'r--', label='квадратичная')
    axs[0, 1].set_title("Квадратичная функция")
    axs[0, 1].legend()
    axs[0, 1].grid(True, alpha=0.3)

    axs[1, 0].plot(x, np.sin(x*0.5), 'g-.', label='синусоида')
    axs[1, 0].set_title("Синусоида")
    axs[1, 0].legend()
    axs[1, 0].grid(True, alpha=0.3)

    axs[1, 1].bar(['A', 'B', 'C', 'D'], [4, 9, 2, 7], color='purple', alpha=0.7)
    axs[1, 1].set_title("Столбчатая диаграмма")
    axs[1, 1].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()

    print("\nУрок 2 завершён.\n")


if __name__ == "__main__":
    run()