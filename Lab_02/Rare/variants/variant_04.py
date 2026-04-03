"""
variant_04.py

Вариант 4.
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
            [(x >= 0) & (x <= 1), (x > 1) & (x <= 2)],
            [
                lambda t: np.sqrt(t + 1) - np.sqrt(t) - 0.5,
                lambda t: np.exp(-t - 1 / t)
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        return np.where(
            (x >= 0) & (x <= 1),
            0.5 / np.sqrt(x + 1) - 0.5 / np.sqrt(x),
            np.exp(-x - 1 / x) * (-1 + 1 / x**2)
        )

    return f, f_prime, (0.0, 2.0), 0.4


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(4, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 4)