"""
common.py

Общие функции для всех вариантов Лабораторной работы №4.
"""

import os
import sys
from typing import Callable, Dict, Tuple


def clear_terminal() -> None:
    """Очищает терминал независимо от операционной системы.

    Использует 'cls' для Windows и 'clear' для Unix-like систем.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def run_tasks_menu(
    variant_num: int,
    task_functions: Dict[int, Tuple[str, Callable[[], None]]],
) -> None:
    """Запускает универсальное меню выбора заданий внутри конкретного варианта.

    Args:
        variant_num: Номер варианта лабораторной (например, 3).
        task_functions: Словарь, где ключ — номер задания,
                        значение — кортеж (название_задания, функция_демонстрации).

    Примечание:
        Выбор 0 возвращает управление в главное меню (не завершает программу).
    """
    WIDTH = 60

    while True:
        clear_terminal()
        print(f"Вариант {variant_num}".center(WIDTH))
        print("=" * WIDTH)
        print("Выберите задание:")

        for num in sorted(task_functions.keys()):
            name, _ = task_functions[num]
            print(f"  {num}. {name}")

        print("  0. Выход из программы.")
        print("=" * WIDTH)

        choice = input("\nВведите номер задания: ").strip()

        if choice == "0":
            clear_terminal()
            input("\nПрограмма завершена. \n\nНажмите Enter для выхода...")
            clear_terminal()
            sys.exit(0)

        try:
            task_num = int(choice)
            if task_num in task_functions:
                name, func = task_functions[task_num]
                clear_terminal()
                print(f"\n{name}")
                print("=" * WIDTH)
                func()                    
                print("=" * WIDTH)
            else:
                print("Некорректный номер задания.")
        except ValueError:
            print("Ошибка: введите число.")

        input("\nНажмите Enter для возврата в меню заданий...")