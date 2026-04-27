"""
variant_03.py

Вариант 3.

Содержит рекурсивную и итеративную реализации двух задач:
1. Распаковка вложенной структуры произвольной глубины.
2. Вычисление члена рекуррентной последовательности w_n.
"""

from typing import Any, Iterable, List, Tuple, Callable 

from common import run_tasks_menu


#region Unpacking Functions

def unpack_recursive(data: Any) -> List[Any]:
    """Рекурсивно распаковывает вложенную структуру в плоский список.

    Поддерживаемые типы: int, str, list, tuple, dict, set, None и другие примитивы.

    Терминальная ветвь: Элемент не является контейнером добавляется в результат.

    Рекурсивная  ветвь: Контейнер рекурсивно распаковывается.

    Args:
        data: Вложенная структура произвольной глубины.

    Returns:
        Плоский список всех найденных элементов (в порядке обхода).
    """
    if not isinstance(data, (list, tuple, set, dict)):
        return [data]

    result: List[Any] = []

    if isinstance(data, (list, tuple, set)):
        for item in data:
            result.extend(unpack_recursive(item))
    else:  
        for key, value in data.items():
            result.extend(unpack_recursive(key))
            result.extend(unpack_recursive(value))

    return result


def unpack_yield_from(data: Any) -> List[Any]:
    """Рекурсивно распаковывает вложенную структуру в плоский список с помощью yield from.

    Питонобразная реализация рекурсивной распаковки.
    Использует внутренний генератор `helper` и конструкцию `yield from`.

    Поддерживаемые типы: list, tuple, set, dict и любые примитивные типы.

    Args:
        data: Вложенная структура произвольной глубины.

    Returns:
        Плоский список всех найденных элементов (в порядке обхода).
    """
    def helper(item: Any) -> Iterable[Any]:

        if not isinstance(item, (list, tuple, set, dict)):
            yield item
            return

        if isinstance(item, (list, tuple, set)):
            for sub_item in item:
                yield from helper(sub_item)
        else:
            for key, value in item.items():
                yield from helper(key)
                yield from helper(value)

    return list(helper(data))


def unpack_iterative(data: Any) -> List[Any]:
    """Итеративная версия распаковки вложенной структуры (использует стек).

    Args:
        data: Вложенная структура произвольной глубины.

    Returns:
        Плоский список всех найденных элементов.
    """
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

#endregion

#region Recurrent Sequence

def calculate_w_recursive(n: int) -> float:
    """Вычисляет n-й член последовательности w_n рекурсивно.

    Формула:
        w_1 = 0.3
        w_2 = -1.5
        w_i = w_{i-1} * w_{i-2} * (i-1)^2 / (i+1)^3   для i >= 3

    Терминальная ветвь: n == 1 или n == 2.
    Рекурсивная ветвь: зависит от двух предыдущих членов.

    Args:
        n: Номер члена последовательности (n >= 1).

    Returns:
        Значение w_n как float.
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
    """Вычисляет n-й член последовательности w_n итеративно.

    Более эффективна при больших n по сравнению с рекурсивной версией.

    Args:
        n: Номер члена последовательности (n >= 1).

    Returns:
        Значение w_n как float.
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

#region Demonstration

def _task1() -> None:
    """Задача 1. Рекурсивная распаковка вложенной структуры."""
    print("Рекурсивная версия unpack():")
    test_data: Any = [None, [1, ({2, 3}, {"foo": "bar", "x": [10, 20]})]]
    result = unpack_recursive(test_data)
    print(f"Входные данные : {test_data}")
    print(f"Результат      : {result}")


def _task2() -> None:
    """Демонстрация распаковки с использованием yield from."""
    print("Рекурсивная версия unpack() с использованием yield from:")
    test_data: Any = [None, [1, ({2, 3}, {"foo": "bar", "x": [10, 20]})]]
    result = unpack_yield_from(test_data)
    print(f"Входные данные : {test_data}")
    print(f"Результат      : {result}")


def _task3() -> None:
    """Задача 1. Итеративная распаковка вложенной структуры."""
    print("Итеративная версия unpack():")
    test_data: Any = [None, [1, ({2, 3}, {"foo": "bar", "x": [10, 20]})]]
    result = unpack_iterative(test_data)
    print(f"Входные данные : {test_data}")
    print(f"Результат      : {result}")


def _task4() -> None:
    """Задача 2. Рекурсивное вычисление последовательности w_n."""
    print("Рекурсивная версия calculate_w(n)")
    print("n".ljust(6), "w_n")
    print("-" * 60)
    for i in range(1, 11):
        print(f"{i:<6} {calculate_w_recursive(i):.10f}")


def _task5() -> None:
    """Задача 2. Итеративное вычисление последовательности w_n."""
    print("Итеративная версия calculate_w(n).")
    print("n".ljust(6), "w_n")
    print("-" * 20)
    for i in range(1, 11):
        print(f"{i:<6} {calculate_w_iterative(i):.10f}")


def run() -> None:
    """Точка входа для Варианта 3.

    Запускает меню заданий варианта 3 с четырьмя демонстрациями.
    """
    tasks: dict[int, Tuple[str, Callable[[], None]]] = {
        1 : ("Задача 1. Распаковка (рекурсия)", _task1),
        2 : ("Задача 1. Распаковка (рекурсия c yield from)", _task2),
        3 : ("Задача 1. Распаковка (итерация)", _task3),
        4 : ("Задача 2. Последовательность w_n (рекурсия)", _task4),
        5 : ("Задача 2. Последовательность w_n (итерация)", _task5),

    }
    run_tasks_menu(3, tasks)

#endregion