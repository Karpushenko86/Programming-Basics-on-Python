"""Урок 1. Быстрый старт с matplotlib"""

import matplotlib.pyplot as plt
import numpy as np


def run():
    """Запуск всех примеров урока 1"""
    print("=== Урок 1. Быстрый старт ===\n")

    # Простой линейный график
    print("1. Простой линейный график")
    x = np.linspace(0, 10, 100)
    y = 2 * x + 1

    plt.figure(figsize=(7, 4))
    plt.plot(x, y, 'b-', label='y = 2x + 1')
    plt.title("Линейная зависимость")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Два графика на одном поле
    print("\n2. Несколько графиков на одном поле")
    y2 = x ** 2

    plt.figure(figsize=(7, 4))
    plt.plot(x, y, label='линейная', linewidth=2)
    plt.plot(x, y2, label='квадратичная', linestyle='--', color='orange')
    plt.title("Линейная и квадратичная функции")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.4)
    plt.legend()
    plt.show()

    # Столбчатая диаграмма
    print("\n3. Столбчатая диаграмма")
    fruits = ['Яблоки', 'Груши', 'Апельсины', 'Бананы', 'Киви']
    counts = [25, 18, 32, 14, 9]

    plt.figure(figsize=(7, 5))
    plt.bar(fruits, counts, color='skyblue', edgecolor='navy', linewidth=1.2)
    plt.title("Количество фруктов в магазине")
    plt.ylabel("Количество, шт")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

    print("\nУрок 1 завершён.\n")


if __name__ == "__main__":
    run()