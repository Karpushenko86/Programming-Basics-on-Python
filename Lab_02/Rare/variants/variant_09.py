"""
variant_09.py

Вариант 9.
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
            [(x >= -1.5) & (x <= 0), (x > 0) & (x <= 1.5)],
            [
                lambda t: (t**2 - 2 * t**3) * np.cos(t**2),
                lambda t: np.exp(np.sin(2 * t))
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        return np.where(
            (x >= -1.5) & (x <= 0),
            (2 * x - 6 * x**2) * np.cos(x**2) - 2 * x * (x**2 - 2 * x**3) * np.sin(x**2),
            np.exp(np.sin(2 * x)) * np.cos(2 * x) * 2
        )

    return f, f_prime, (-1.5, 1.5), -0.5


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(9, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 9)