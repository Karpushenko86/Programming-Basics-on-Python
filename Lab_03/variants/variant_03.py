"""
variant_03.py

Вариант 3.
"""

from itertools import product
from typing import List

from common import save_result, run_tasks_menu


def count_valid_combinations() -> int:
    """Подсчитывает количество 6-буквенных комбинаций из букв 'АНДРЕЙ'
    с ограничениями:
    - буква 'Й' встречается не более 1 раза
    - 'Й' не стоит в начале и в конце
    - отсутствуют сочетания 'ЕЙ' и 'ЙЕ'
    """
    total = 0
    letters = "АНДРЕЙ"

    for code in product(letters, repeat=6):
        s = "".join(code)

        if (
            s.count("Й") <= 1
            and s[0] != "Й"
            and s[-1] != "Й"
            and "ЕЙ" not in s
            and "ЙЕ" not in s
        ):
            total += 1

    return total


def get_valid_combinations() -> List[str]:
    """Возвращает список всех валидных 6-буквенных комбинаций
    (используется для сохранения полного переборa в файл).
    """
    letters = "АНДРЕЙ"
    valid: List[str] = []

    for code in product(letters, repeat=6):
        s = "".join(code)

        if (
            s.count("Й") <= 1
            and s[0] != "Й"
            and s[-1] != "Й"
            and "ЕЙ" not in s
            and "ЙЕ" not in s
        ):
            valid.append(s)

    return valid


def _is_prime(n: int) -> bool:
    """Проверяет, является ли число простым (оптимизированный алгоритм)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def _task1() -> None:
    """Задача 1. Кодовые слова — сохраняем ВСЕ валидные комбинации в файл."""
    combinations = get_valid_combinations()
    print(f"Найдено валидных кодовых слов: {len(combinations)}")
    result_text = "\n".join(combinations)
    save_result(3, 1, result_text)


def _task2() -> None:
    """Задача 2. Количество единиц в двоичной записи числа."""
    value = 8**2020 + 4**2017 + 26 - 1
    ones_count = bin(value).count("1")
    print(f"Количество единиц в двоичной записи: {ones_count}")
    save_result(3, 2, str(ones_count))


def _task3() -> None:
    """Задача 3. Простые числа в отрезке [245690; 245756]."""
    start, end = 245690, 245756
    output_lines: List[str] = []

    print("Найденные простые числа:")

    for num in range(start, end + 1):
        if _is_prime(num):
            position = num - start + 1
            line = f"{position} {num}"
            print(line)
            output_lines.append(line)

    save_result(3, 3, "\n".join(output_lines))


def run() -> None:
    """Точка входа для Варианта 3."""
    tasks = {
        1: ("Задача 1. Кодовые слова из букв А, Н, Д, Р, Е, Й", _task1),
        2: ("Задача 2. Количество единиц в двоичной записи", _task2),
        3: ("Задача 3. Простые числа в отрезке [245690; 245756]", _task3),
    }
    run_tasks_menu(3, tasks)