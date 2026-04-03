"""
variant_06.py

Вариант 6.
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
                lambda t: 8 * t**3 * np.cos(t),
                lambda t: np.log(1 + np.sqrt(t)) - np.cos(t)
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        return np.where(
            (x >= 0) & (x <= 1),
            24 * x**2 * np.cos(x) - 8 * x**3 * np.sin(x),
            0.5 / (np.sqrt(x) * (1 + np.sqrt(x))) + np.sin(x)
        )

    return f, f_prime, (0.0, 2.0), 0.5


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(6, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 6)