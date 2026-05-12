"""
optimized_variant_03.py

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
    """Преобразует структуру в полностью хэшируемую форму (рекурсивно)."""
    if isinstance(data, (list, tuple)):
        return tuple(_make_hashable(x) for x in data)
    if isinstance(data, set):
        return frozenset(_make_hashable(x) for x in data)
    if isinstance(data, dict):
        return tuple((_make_hashable(k), _make_hashable(v)) for k, v in data.items())
    return data


@lru_cache(maxsize=None)
def _unpack_recursive_cached(hashable: Any) -> tuple[Any, ...]:
    """Сверхбыстрая кэшируемая рекурсивная распаковка (tuple-конкатенация)."""
    if not isinstance(hashable, (tuple, frozenset)):
        return (hashable,)

    # Dict case: строго tuple из 2-элементных кортежей (key, value)
    if (
        isinstance(hashable, tuple)
        and hashable
        and all(isinstance(item, tuple) and len(item) == 2 for item in hashable)
    ):
        result: tuple[Any, ...] = ()
        for k, v in hashable:
            result += _unpack_recursive_cached(k) + _unpack_recursive_cached(v)
        return result

    # Обычный tuple / frozenset
    result: tuple[Any, ...] = ()
    for item in hashable:
        result += _unpack_recursive_cached(item)
    return result



def unpack_recursive_optimized(data: Any) -> tuple[Any, ...]:
    """Рекурсивная распаковка с оптимизированным аккумулятором.

    Ускоренная распаковка относительно оригинальной unpack_recursive_*
    за счёт минимального количества аллокаций списков.

    Args:
        data: Вложенная структура произвольной глубины.

    Returns:
        Кортеж всех элементов в порядке обхода.
    """
    if data is None:
        return (None,)
    if not data:
        return ()

    result: list[Any] = []

    def _helper(item: Any) -> None:
        """Внутренний рекурсивный помощник с прямым append в общий список."""
        if not isinstance(item, (list, tuple, set, dict)):
            result.append(item)
            return

        if isinstance(item, (list, tuple, set)):
            for sub_item in item:
                _helper(sub_item)
        else:  # dict
            for key, value in item.items():
                _helper(key)
                _helper(value)

    _helper(data)
    return tuple(result)



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