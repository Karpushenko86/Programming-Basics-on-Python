"""
variant_03_optimized.py

Вариант 3.
Повысьте производительность своих функций минимум в 2 раза относительно исходных вариатов решения.
"""


from functools import lru_cache
from collections import deque
from typing import Any


#region Optimized calculate_w

@lru_cache(maxsize=None)
def calculate_w_recursive_optimized(n: int) -> float:
    """Рекурсивная реализация w_n с полной мемоизацией через lru_cache.

    Args:
        n: Порядковый номер члена последовательности (n >= 1).

    Returns:
        Значение n-го члена последовательности w_n.

    Raises:
        RecursionError: При очень большом n (маловероятно из-за кэша).
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
    """Итеративная реализация w_n с минимальным количеством операций в цикле.

    Args:
        n: Порядковый номер члена последовательности (n >= 1).

    Returns:
        Значение n-го члена последовательности w_n.
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


#region Optimized unpack

def _make_hashable(data: Any) -> Any:
    """Преобразует произвольную структуру данных в полностью хэшируемую форму.

    Используется внутренне для корректной работы lru_cache.
    """
    if isinstance(data, (list, tuple)):
        return tuple(_make_hashable(x) for x in data)
    if isinstance(data, set):
        return frozenset(_make_hashable(x) for x in data)
    if isinstance(data, dict):
        hashable_items = [
            (_make_hashable(k), _make_hashable(v)) 
            for k, v in data.items()
            ]
        return tuple(sorted(hashable_items))
    return data


@lru_cache(maxsize=None)
def _unpack_recursive_cached(hashable: Any) -> tuple[Any, ...]:
    """Внутренняя кэшируемая функция для рекурсивной распаковки.

    Принимает только хэшируемые данные.
    """
    result: list[Any] = []

    if isinstance(hashable, (tuple, frozenset)):
        for item in hashable:
            result.extend(_unpack_recursive_cached(item))
    elif isinstance(hashable, tuple) and hashable and isinstance(hashable[0], tuple):
        for k, v in hashable:
            result.extend(_unpack_recursive_cached(k))
            result.extend(_unpack_recursive_cached(v))
    else:
        result.append(hashable)

    return tuple(result)


def unpack_recursive_optimized(data: Any) -> tuple[Any, ...]:
    """Рекурсивная распаковка вложенных структур с мемоизацией (lru_cache).

    Args:
        data: Вложенная структура (list, tuple, set, dict, None или примитив).

    Returns:
        Кортеж со всеми "листовыми" элементами в порядке глубинного обхода.
    """
    if data is None:
        return (None,)
    hashable = _make_hashable(data)
    return _unpack_recursive_cached(hashable)


def unpack_iterative_optimized(data: Any) -> list[Any]:
    """Самая быстрая итеративная распаковка с использованием deque.

    Args:
        data: Вложенная структура данных.

    Returns:
        Список всех "листовых" элементов в порядке обхода.
    """
    if data is None:
        return [None]
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