"""
variant_03_optimized.py

Вариант 3.
Повысьте производительность своих функций минимум в 2 раза относительно исходных вариатов решения.
"""
from functools import lru_cache
from collections import deque
from typing import Any


#region Optimized calculate_w_*

@lru_cache(maxsize=None)
def calculate_w_recursive_optimized(n: int) -> float:
    """Рекурсивная реализация w_n с полной мемоизацией через lru_cache.

    Использование кэширования даёт экспоненциальное ускорение
    по сравнению с наивной рекурсией.

    Args:
        n: Номер члена последовательности (n >= 1).

    Returns:
        Значение n-го члена последовательности w_n.

    Raises:
        RecursionError: При слишком большой глубине рекурсии (хотя cache сильно снижает риск).
    """
    if n == 1:
        return 0.3
    if n == 2:
        return -1.5
    return (
        calculate_w_recursive_optimized(n - 1)
        * calculate_w_recursive_optimized(n - 2)
        * ((n - 1) ** 2)
        / ((n + 1) ** 3)
    )


def calculate_w_iterative_optimized(n: int) -> float:
    """Высокооптимизированная итеративная реализация w_n.

    Минимизировано количество операций внутри цикла.
    
    Args:
        n: Номер члена последовательности (n >= 1).

    Returns:
        Число с плавающей точкой, представляющее результат n-й итерации вычисления w.
    """
    if n == 1:
        return 0.3
    if n == 2:
        return -1.5

    w_prev2 = 0.3
    w_prev1 = -1.5

    for i in range(3, n + 1):
        w_current = w_prev1 * w_prev2 * ((i - 1) ** 2) / ((i + 1) ** 3)
        w_prev2 = w_prev1
        w_prev1 = w_current

    return w_prev1

#endregion


#region Optimized unpack_*

@lru_cache(maxsize=None)
def unpack_recursive_optimized(data: Any) -> tuple[Any, ...]:
    """Рекурсивная распаковка с мемоизацией (lru_cache).

    Возвращает tuple (а не list), чтобы результат был хэшируемым
    и мог кэшироваться.

    Args:
        data: Вложенная структура (list, tuple, set, dict, примитивы).

    Returns:
        Кортеж со всеми "листовыми" элементами в порядке обхода.
    """
    if not isinstance(data, (list, tuple, set, dict)):
        return (data,)

    result: list[Any] = []

    if isinstance(data, (list, tuple, set)):
        for item in data:
            result.extend(unpack_recursive_optimized(item))
    else:  # dict
        for key, value in data.items():
            result.extend(unpack_recursive_optimized(key))
            result.extend(unpack_recursive_optimized(value))

    return tuple(result)


def unpack_iterative_optimized(data: Any) -> list[Any]:
    """Быстрая итеративная распаковка с использованием (deque).

    Использование эффективной очереди.

    Args:
        data: Вложенная структура (list, tuple, set, dict, примитивы).

    Returns:
        Плоский список, содержащий все примитивные значения и элементы пар (ключ, значение) из словарей.
    """
    if not data:
        return []

    result: list[Any] = []
    queue: deque = deque([data])

    while queue:
        current = queue.popleft()

        if isinstance(current, (list, tuple, set)):
            queue.extend(current)
        elif isinstance(current, dict):
            queue.extend(current.items())
        else:
            result.append(current)

    return result

#endregion


__all__ = [
    "calculate_w_recursive_optimized",
    "calculate_w_iterative_optimized",
    "unpack_recursive_optimized",
    "unpack_iterative_optimized",
]