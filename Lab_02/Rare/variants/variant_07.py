"""
variant_07.py

Вариант 7.
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
            [(x >= -1) & (x <= 1), (x > 1) & (x <= 2)],
            [
                lambda t: np.exp(-2 * np.sin(t)),
                lambda t: t**2 - np.cos(t) / np.sin(t),
            ],
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        left = -2 * np.cos(x) * np.exp(-2 * np.sin(x))

        right = np.zeros_like(x, dtype=float)
        mask_right = (x > 1) & (x <= 2)
        sin_x = np.sin(x[mask_right])
        safe = np.abs(sin_x) > 1e-12

        right[mask_right] = 2 * x[mask_right]
        right[mask_right][safe] += np.cos(x[mask_right][safe]) / (sin_x[safe] ** 2)

        return np.where((x >= -1) & (x <= 1), left, right)

    return f, f_prime, (-1.0, 2.0), 0.0


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(7, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 7)