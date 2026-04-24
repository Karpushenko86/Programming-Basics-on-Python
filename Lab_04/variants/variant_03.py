"""
variant_03.py

Решение Варианта 3 лабораторной работы №4 (Recursion).
"""

from typing import Any, List

from common import run_tasks_menu


# ====================== Задача 1: Распаковка вложенной структуры ======================

def unpack_recursive(data: Any) -> List[Any]:
    """Рекурсивная версия распаковки.

    Терминальная ветвь: элемент не контейнер → добавляем в результат.
    Рекурсивная ветвь: элемент — контейнер → рекурсивно обрабатываем содержимое.
    """
    result: List[Any] = []

    if isinstance(data, (list, tuple, set)):
        for item in data:
            result.extend(unpack_recursive(item))
    elif isinstance(data, dict):
        for key, value in data.items():
            result.extend(unpack_recursive(key))
            result.extend(unpack_recursive(value))
    else:
        # Терминальная ветвь
        result.append(data)

    return result


def unpack_iterative(data: Any) -> List[Any]:
    """Итеративная версия распаковки (использует стек)."""
    result: List[Any] = []
    stack: List[Any] = [data]

    while stack:
        current = stack.pop()

        if isinstance(current, (list, tuple, set)):
            stack.extend(reversed(list(current)))
        elif isinstance(current, dict):
            for key, value in reversed(list(current.items())):
                stack.append(value)
                stack.append(key)
        else:
            result.append(current)

    return result


# ====================== Задача 2: Рекуррентная последовательность w_n ======================

def calculate_w_recursive(n: int) -> float:
    """Рекурсивная версия вычисления w_n.

    Терминальная ветвь: n == 1 или n == 2.
    Рекурсивная ветвь: w_n = w_{n-1} * w_{n-2} * (n-1)^2 / (n+1)^3
    """
    if n == 1:
        return 0.3
    if n == 2:
        return -1.5

    # Рекурсивная ветвь
    prev1 = calculate_w_recursive(n - 1)
    prev2 = calculate_w_recursive(n - 2)
    return prev1 * prev2 * ((n - 1) ** 2) / ((n + 1) ** 3)


def calculate_w_iterative(n: int) -> float:
    """Итеративная версия (эффективнее для больших n)."""
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


# ====================== Демонстрационные функции ======================

def _task1() -> None:
    """Задача 1. Рекурсивная распаковка вложенной структуры."""
    print("Рекурсивная версия unpack():")
    test_data: Any = [None, [1, ({2, 3}, {"foo": "bar"})]]
    result = unpack_recursive(test_data)
    print(f"Входные данные : {test_data}")
    print(f"Результат      : {result}")


def _task2() -> None:
    """Задача 1. Итеративная распаковка вложенной структуры."""
    print("Итеративная версия unpack():")
    test_data: Any = [None, [1, ({2, 3}, {"foo": "bar"})]]
    result = unpack_iterative(test_data)
    print(f"Входные данные : {test_data}")
    print(f"Результат      : {result}")


def _task3() -> None:
    """Задача 2. Рекурсивное вычисление последовательности w_n."""
    print("Рекурсивная версия calculate_w(n)")
    print("n".ljust(6), "w_n")
    print("-" * 60)
    for i in range(1, 11):
        print(f"{i:<6} {calculate_w_recursive(i):.10f}")


def _task4() -> None:
    """Задача 2. Итеративное вычисление последовательности w_n."""
    print("Итеративная версия calculate_w(n)")
    print("n".ljust(6), "w_n")
    print("-" * 20)
    for i in range(1, 11):
        print(f"{i:<6} {calculate_w_iterative(i):.10f}")


def run() -> None:
    """Точка входа для Варианта 3."""
    tasks: Dict[int, Tuple[str, Callable[[], None]]] = {
        1: ("Задача 1. Распаковка (рекурсия)", _task1),
        2: ("Задача 1. Распаковка (итерация)", _task2),
        3: ("Задача 2. Последовательность w_n (рекурсия)", _task3),
        4: ("Задача 2. Последовательность w_n (итерация)", _task4),
    }
    run_tasks_menu(3, tasks)