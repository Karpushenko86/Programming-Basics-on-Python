"""
main.py

Главное консольное меню лабораторной №4.
Один входной файл для Rare / Medium / Well-done.
"""

import subprocess
import sys
from typing import Dict
from Lab_04.Rare.common import clear_terminal

NUMBER_OF_VARIANTS: int = 12

width: int = 60

def _select_variant(level_name: str) -> int | None:
    """Простое меню выбора варианта 1–12"""
    while True:
        clear_terminal()

        if level_name == "Medium":
            print("\nЛабораторная работа №4 — Модуль [ Medium ]")

        if level_name == "Well-done":
            print("\nЛабораторная работа №4 — Модуль [ Well-done ]")
        
        print("=" * width)
        print(f"Выберите вариант (1-{NUMBER_OF_VARIANTS}) или действие:")

        for i in range(NUMBER_OF_VARIANTS):
            num = i + 1
            print(f"  {num:2d} — Вариант {num}")

        print("   0 — Выход из программы")
        print("=" * width)

        try:
            choice = int(input("\nВведите номер варианта: ").strip())
            
            if choice == 0:
                clear_terminal()
                input("\nПрограмма завершена.\n\nНажмите Enter для выхода...")
                clear_terminal()
                break
            
            if 1 <= choice <= 12:
                return choice
            
            input("Нажмите Enter для продолжения...")  
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число от 0 до 12.")


def _run_rare() -> None:
    """Запускает полное меню Rare (как было раньше)."""
    print("\nЗапускаем меню заданий модуля [ Rare ]...\n")
    try:
        subprocess.run(
            [sys.executable, "-m", "Lab_04.Rare.main"], 
            check=True
        )
    except subprocess.CalledProcessError:
        print("Ошибка при запуске меню заданий модуля [ Rare ].")


def _run_medium(variant: int) -> None:
    """Запускает pytest для выбранного варианта Medium."""
    test_file = f"Lab_04/Medium/test/test_variant_{variant:02d}.py"
    print(f"\nЗапускаем тесты из модуля [ Medium ] — Вариант {variant:02d}...\n")
    try:
        subprocess.run(
            [sys.executable, "-m", "pytest", test_file, "-q", "--tb=no"],
            check=True,
        )
    except subprocess.CalledProcessError:
        print("Ошибка при запуске тестов модуля [ Medium ].")


def _run_well_done(variant: int) -> None:
    """Запускает бенчмарк модуля [ Well-done ]."""
    print(f"\nЗапускаем бенчмарк Well-done - Вариант {variant:02d}...\n")
    try:
        subprocess.run(
            [sys.executable, "-m", "Lab_04.Well_done.benchmarks"], 
            check=True
        )
    except subprocess.CalledProcessError:
        print("Ошибка при запуске бенчмарка модуля [ Well-done ].")


def main() -> None:
    """Главное меню лабораторной №4."""
    levels: Dict[int, tuple[str, callable]] = {
        1: ("Rare", _run_rare),
        2: ("Medium", lambda v: _run_medium(v)),
        3: ("Well-done", lambda v: _run_well_done(v)),
    }

    while True:
        clear_terminal()
        print("\n" + "=" * width)
        print("ЛАБОРАТОРНАЯ №4 — Главное меню".center(width))
        print("=" * width)
        print("   1 — Запуск модуля [   Rare   ]".center(width//2))
        print("   2 — Запуск модуля [  Medium  ]".center(width//2))
        print("   3 — Запуск модуля [ Well-done]".center(width//2))
        print("   0 — Выход из программы        ".center(width//2))
        print("=" * width + "\n")

        try:
            level_choice = int(input("Выберите модуль: ").strip())
            if level_choice == 0:
                clear_terminal()
                input("\nПрограмма завершена.\n\nНажмите Enter для выхода...")
                clear_terminal()
                sys.exit(0)
            if level_choice not in levels:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 3.")
                continue
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 3.")
            continue

        level_name, runner = levels[level_choice]

        if level_choice == 1:
            clear_terminal()
            runner()

        if level_choice == 2:
            variant = _select_variant(level_name)
            clear_terminal()
            if variant is None:
                continue
            runner(variant)
            input("\nПрограмма завершена.\n\nНажмите Enter для выхода...")
            clear_terminal()

        if level_choice == 3:
            variant = _select_variant(level_name)
            clear_terminal()
            if variant is None:
                continue
            runner(variant)
            input("\nПрограмма завершена.\n\nНажмите Enter для выхода...")
            clear_terminal()


if __name__ == "__main__":
    main()