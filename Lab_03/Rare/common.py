"""
common.py

Общие функции для всех вариантов лабораторной работы №3.
"""

import os
import sys
from typing import Callable, Dict, Tuple


def clear_terminal() -> None:
    """Очищает терминал независимо от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')


def save_result(variant: int, task: int, result: str) -> None:
    """Сохраняет результат задачи в файл results/variant_XX_task_Y.txt"""
    os.makedirs("results", exist_ok=True)
    filename = f"Lab_03/Rare/results/variant_{variant:02d}_task_{task}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nРезультат сохранён в файл: {filename}")


def run_tasks_menu(
    variant_num: int,
    task_functions: Dict[int, Tuple[str, Callable[[], None]]],
) -> None:
    """Универсальное меню заданий внутри варианта."""
    WIDTH = 55

    while True:
        print(f"Вариант {variant_num}".center(WIDTH))
        print(f"{'=' * WIDTH}")
        print("Выберите задание:")

        for num in sorted(task_functions.keys()):
            name, _ = task_functions[num]
            print(f"  {num}. {name}")

        print("  0. Выход из программы")
        print(f"{'=' * WIDTH}")

        choice = input("\nВведите номер варианта или 0 для выхода: ").strip()

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
                print("-" * WIDTH)
                func()
                print("-" * WIDTH)
            else:
                print("Некорректный выбор задания.")
        except ValueError:
            print("Некорректный ввод. Введите число.")

        input("\nНажмите Enter для возврата в меню заданий...")
        clear_terminal()