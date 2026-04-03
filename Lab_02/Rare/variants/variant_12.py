"""
variant_12.py

Вариант 12.
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
            [(x >= -2) & (x <= 0), (x > 0) & (x <= 1)],
            [
                lambda t: t**2 * np.sin(np.cbrt(t) - 3),
                lambda t: np.sqrt(t) * np.cos(2 * t)
            ]
        )

    def f_prime(x: np.ndarray) -> np.ndarray:
        def der_first(t: np.ndarray) -> np.ndarray:
            cbrt_t = np.cbrt(t)
            safe = np.abs(t) > 1e-8
            result = np.zeros_like(t, dtype=float)
            
            term_derivative_cbrt = (1.0 / 3.0) / (np.cbrt(t[safe])**2)
            
            result[safe] = (
                2 * t[safe] * np.sin(cbrt_t[safe] - 3) +
                t[safe]**2 * np.cos(cbrt_t[safe] - 3) * term_derivative_cbrt
            )
            return result


        def der_second(t: np.ndarray) -> np.ndarray:
            safe = t > 1e-10
            result = np.zeros_like(t, dtype=float)
            result[safe] = (
                0.5 / np.sqrt(t[safe]) * np.cos(2 * t[safe])
                - 2 * np.sqrt(t[safe]) * np.sin(2 * t[safe])
            )
            return result

        return np.where((x >= -2) & (x <= 0), der_first(x), der_second(x))

    return f, f_prime, (-2.0, 1.0), -1.0


def run() -> None:
    f, f_prime, (xmin, xmax), x0 = get_function()
    y0 = float(f(np.array([x0]))[0])
    slope = float(f_prime(np.array([x0]))[0])

    print_tangent_info(12, x0, y0, slope)
    create_and_configure_plot(f, xmin, xmax, x0, y0, slope, 12)