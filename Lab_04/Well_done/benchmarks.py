"""
benchmarks.py - измерение производительности оптимизаций Well-done.

Сравнивает время выполнения оригинальных функций из Rare
с оптимизированными версиями из Well-done.
"""

import sys
import timeit
from pathlib import Path
from typing import Callable

# Добавляем папку Rare в PYTHONPATH
RARE_PATH = Path(__file__).parent.parent / "Rare"
sys.path.insert(0, str(RARE_PATH))

# Оригинальные реализации
from Rare.variants.variant_03 import (
    calculate_w_recursive,
    calculate_w_iterative,
    unpack_recursive,
    unpack_iterative,
)

# Оптимизированные реализации
from Well_done.variants.optimized_variant_03 import (
    calculate_w_recursive_optimized,
    calculate_w_iterative_optimized,
    unpack_recursive_optimized,
    unpack_iterative_optimized,
)


# Тестовые данные
TEST_DATA_UNPACK = [None, [1, ({2, 3}, {"foo": "bar", "x": [10, 20, [30]]})]]
TEST_N_VALUES = [10, 50, 100, 200]


def benchmark(func: Callable, *args, number: int = 10000) -> float:
    """Измеряет среднее время выполнения функции в миллисекундах."""
    return timeit.timeit(lambda: func(*args), number=number) / number * 1000


print("=== Бенчмарк производительности Well-done ===\n")

print("1. calculate_w_recursive (рекурсия):")
for n in TEST_N_VALUES:
    t_orig = benchmark(calculate_w_recursive, n)
    t_opt = benchmark(calculate_w_recursive_optimized, n)
    speedup = t_orig / t_opt if t_opt != 0 else float("inf")
    print(f"  n={n:3d} | оригинал: {t_orig:6.3f} мс | оптимизировано: {t_opt:6.3f} мс | ускорение: {speedup:.1f}x")

print("\n2. calculate_w_iterative:")
for n in TEST_N_VALUES:
    t_orig = benchmark(calculate_w_iterative, n)
    t_opt = benchmark(calculate_w_iterative_optimized, n)
    speedup = t_orig / t_opt if t_opt != 0 else float("inf")
    print(f"  n={n:3d} | оригинал: {t_orig:6.3f} мс | оптимизировано: {t_opt:6.3f} мс | ускорение: {speedup:.1f}x")

print("\n3. unpack (на сложной вложенной структуре):")
t_orig_rec = benchmark(unpack_recursive, TEST_DATA_UNPACK)
t_opt_rec = benchmark(unpack_recursive_optimized, TEST_DATA_UNPACK)
t_orig_it = benchmark(unpack_iterative, TEST_DATA_UNPACK)
t_opt_it = benchmark(unpack_iterative_optimized, TEST_DATA_UNPACK)

print(f"  recursive оригинал     : {t_orig_rec:6.3f} мс")
print(f"  recursive оптимизировано: {t_opt_rec:6.3f} мс → {t_orig_rec / t_opt_rec:.1f}x")
print(f"  iterative оригинал     : {t_orig_it:6.3f} мс")
print(f"  iterative оптимизировано: {t_opt_it:6.3f} мс → {t_orig_it / t_opt_it:.1f}x")

print("\nБенчмарк завершён.")