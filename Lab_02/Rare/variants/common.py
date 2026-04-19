"""
common.py

Общая логика для Лабораторной работы №2.
"""

import os
from collections.abc import Callable, Sequence
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt


def print_tangent_info(variant: int, x0: float, y0: float, slope: float) -> None:
    """
    Выводит информацию о точке касания.

    Args:
        variant: Номер варианта лабораторной работы.
        x0: Абсцисса точки касания.
        y0: Ордината точки касания f(x0).
        slope: Значение производной f'(x0).
    """
    print(f"=== Вариант {variant} ===")
    print(f"Точка касания: x₀ = {x0}")
    print(f"f({x0})  = {y0:.6f}")
    print(f"f'({x0}) = {slope:.6f}\n")


def create_and_configure_plot(
    f: Callable[[np.ndarray], np.ndarray],
    xmin: float,
    xmax: float,
    x0: float,
    y0: float,
    slope: float,
    variant: int,
) -> None:
    """
    Построение графика кусочно-заданной функции с автоматическим определением разрывов.

    Разрывы определяются по значительным скачкам в значениях y.
    Каждая непрерывная ветвь рисуется отдельной линией.

    Args:
        f: Кусочно-заданная функция.
        xmin: Левая граница области построения.
        xmax: Правая граница области построения.
        x0: Абсцисса точки касания.
        y0: Ордината точки касания.
        slope: Значение производной в точке касания.
        variant: Номер варианта для имени файла.
    """
    fig, ax = plt.subplots(figsize=(11, 7.5))

    # Генерация плотной сетки и вычисление значений функции
    num_points: int = 2400
    x_full: np.ndarray = np.linspace(xmin, xmax, num_points)
    y_full: np.ndarray = f(x_full)

    # Автоматическое разбиение на непрерывные сегменты по разрывам
    segments: list[tuple[np.ndarray, np.ndarray]] = _split_into_continuous_segments(x_full, y_full)

    # Отрисовка каждой непрерывной ветви
    for i, (xs, ys) in enumerate(segments):
        label = r"$f(x)$" if len(segments) == 1 else f"$f(x)$ (ветвь {i + 1})"
        color = "b-" if i % 2 == 0 else "g-"
        ax.plot(xs, ys, color, linewidth=2.8, label=label)

    # Касательная
    tan_width: float = (xmax - xmin) * 0.28
    x_tan: np.ndarray = np.linspace(
        max(xmin, x0 - tan_width),
        min(xmax, x0 + tan_width),
        700,
    )
    y_tan: np.ndarray = y0 + slope * (x_tan - x0)

    ax.plot(x_tan, y_tan, "r--", linewidth=3.0, label=f"Касательная в x = {x0:.2f}")
    ax.plot(x0, y0, "ro", markersize=11, zorder=10)

    # Настройка границ осей
    ax.set_xlim(xmin - 0.2, xmax + 0.2)
    y_all: np.ndarray = np.concatenate([ys for _, ys in segments] + [y_tan])
    y_min_val: float = float(np.min(y_all))
    y_max_val: float = float(np.max(y_all))

    y_range: float = y_max_val - y_min_val
    x_range: float = xmax - xmin
    padding: float = y_range * 0.15 if y_range > 0 else 1.0

    ax.set_ylim(y_min_val - padding, y_max_val + padding)

    # Адаптивная аннотация
    dx: float = x_range * 0.08
    dy: float = (y_range + 2 * padding) * 0.12

    if x0 > (xmin + xmax) / 2:
        dx = -dx * 3.5

    ax.annotate(
        f"Точка касания\nx = {x0:.2f}\nf(x) ≈ {y0:.3f}\nf'(x) ≈ {slope:.3f}",
        xy=(x0, y0),
        xytext=(x0 + dx, y0 + dy),
        arrowprops=dict(facecolor="black", shrink=0.07, width=1.5, headwidth=8),
        bbox=dict(boxstyle="round,pad=0.6", facecolor="lightyellow", alpha=0.9, edgecolor="gray"),
        fontsize=11,
    )

    # Оформление графика
    ax.set_title("Кусочно-заданная функция и касательная", fontsize=17, fontweight="bold", pad=25)
    ax.set_xlabel("Ось X", fontsize=14)
    ax.set_ylabel("Ось Y", fontsize=14)
    ax.grid(True, alpha=0.35)
    ax.legend(loc="best", fontsize=11.5)

    plt.tight_layout()

    os.makedirs("graphs", exist_ok=True)
    filename: str = f"Lab_02/Rare/graphs/lab02_variant_{variant:02d}.png"
    plt.savefig(filename, dpi=320, bbox_inches="tight")
    print(f"График сохранён: {filename}\n")
    plt.show()


def _split_into_continuous_segments(
    x: np.ndarray, y: np.ndarray
) -> list[tuple[np.ndarray, np.ndarray]]:
    """
    Разбивает массивы x и y на непрерывные сегменты по обнаруженным разрывам.

    Используется улучшенная эвристика, учитывающая как относительные,
    так и абсолютные скачки.
    """
    if len(y) <= 1:
        return [(x, y)]

    dy = np.abs(np.diff(y))
    y_range = float(np.ptp(y)) if np.ptp(y) > 0 else 1.0

    # Улучшенный порог: максимум из относительного и абсолютного
    rel_threshold = 0.03 * y_range          # 3% от размаха
    abs_threshold = 0.05                    # минимальный заметный скачок
    threshold = max(rel_threshold, abs_threshold)

    # Дополнительно усиливаем чувствительность рядом с типичными границами (0, 1, -1 и т.д.)
    jump_indices = np.where(dy > threshold)[0]

    segments: list[tuple[np.ndarray, np.ndarray]] = []
    start = 0

    for idx in jump_indices:
        # Берём сегмент до скачка включительно
        if idx + 1 > start:
            segments.append((x[start:idx + 1], y[start:idx + 1]))
        start = idx + 1

    # Последний сегмент
    if start < len(x):
        segments.append((x[start:], y[start:]))

    # Если ничего не нашли — возвращаем как один сегмент
    return segments if segments else [(x, y)]