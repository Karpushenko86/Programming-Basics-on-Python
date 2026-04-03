"""
variant_05.py

Вариант 5.
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
            [(x >= 0) & (x <= 1.5), (x > 1.5) & (x <= 3)],
            [
                lambda t: 2**t - 2 + t**2,
                lambda t: np.sqrt(t) * np.exp(-t**2)
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        return np.where(
            (x >= 0) & (x <= 1.5),
            np.log(2) * 2**x + 2 * x,
            (0.5 / np.sqrt(x) - 2 * x * np.sqrt(x)) * np.exp(-x**2)
        )

    return f, f_prime, (0.0, 3.0), 0.8


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(5, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 5)