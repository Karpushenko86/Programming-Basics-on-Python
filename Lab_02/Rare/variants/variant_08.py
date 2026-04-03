"""
variant_08.py

Вариант 8.
"""

import numpy as np
from typing import Callable, Tuple

from .common import print_tangent_info, create_and_configure_plot


def get_function() -> Tuple[
    Callable[[np.ndarray], np.ndarray],
    Callable[[np.ndarray], np.ndarray],
    Tuple[float, float],
    float,
]:
    def f(x: np.ndarray) -> np.ndarray:
        return np.piecewise(
            x,
            [(x >= 0) & (x <= 0.6), (x > 0.6) & (x <= 1.6)],
            [
                lambda t: 1 / (1 + 25 * t**2),
                lambda t: (t + 2 * t**4) * np.sin(t**2)
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        return np.where(
            (x >= 0) & (x <= 0.6),
            -50 * x / (1 + 25 * x**2)**2,
            (1 + 8 * x**3) * np.sin(x**2) + (x + 2 * x**4) * np.cos(x**2) * 2 * x
        )

    return f, f_prime, (0.0, 1.6), 0.3


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(8, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 8)