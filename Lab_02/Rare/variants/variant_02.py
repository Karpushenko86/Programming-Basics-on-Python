"""
variant_02.py

Вариант 2.
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
            [(x >= 0) & (x <= 0.25), (x > 0.25) & (x <= 0.5)],
            [
                lambda t: np.exp(np.sin(t)),
                lambda t: np.exp(t) - 1 / np.sqrt(t)
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        return np.where(
            (x >= 0) & (x <= 0.25),
            np.exp(x) * np.cos(x),
            np.exp(x) + 0.5 * x**(-1.5)
        )

    return f, f_prime, (-0.5, 2), 0.4


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(2, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 2)