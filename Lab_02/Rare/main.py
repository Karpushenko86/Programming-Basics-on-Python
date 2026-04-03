"""
main.py

Консольное меню для запуска вариантов Лабораторной работы №2.
"""

import os
import sys
from typing import Dict, Callable

from variants.variant_01 import run as var_01
from variants.variant_02 import run as var_02
from variants.variant_03 import run as var_03
from variants.variant_04 import run as var_04
from variants.variant_05 import run as var_05
from variants.variant_06 import run as var_06
from variants.variant_07 import run as var_07
from variants.variant_08 import run as var_08
from variants.variant_09 import run as var_09
from variants.variant_10 import run as var_10
from variants.variant_11 import run as var_11
from variants.variant_12 import run as var_12

number_of_variants = 12

def clear_terminal() -> None:
    """Очищает терминал независимо от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu() -> None:
    """Выводит главное меню."""
    print("\nЛабораторная работа №2 — Кусочно-заданные функции")
    print("=" * 55)
    print(f"Выберите вариант (1-'{number_of_variants}') или действие:")

    for i in range(number_of_variants):
        if i < 9:
            print(f"  {i + 1}  — Вариант {i + 1}")
        else:
            print(f" {i + 1}  — Вариант {i + 1}")

    print("  0  — Выход из программы")
    print("=" * 55)


def main() -> None:
    """Главное консольное меню программы."""
    variants: Dict[str, Callable[[], None]] = {
        "1": var_01,
        "2": var_02,
        "3": var_03,
        "4": var_04,
        "5": var_05,
        "6": var_06,
        "7": var_07,
        "8": var_08,
        "9": var_09,
        "10": var_10,
        "11": var_11,
        "12": var_12,
    }

    while True:
        clear_terminal()
        show_menu()

        choice = input("\nВведите номер варианта или 0 для выхода: ").strip()

        if choice == "0":
            clear_terminal()
            input("\nПрограмма завершена. \n\nНажмите Enter для выхода...")
            clear_terminal()
            sys.exit(0)

        if choice in variants:
            clear_terminal()
            try:
                variants[choice]()
            except Exception as e: 
                print(f"Ошибка при выполнении варианта {choice}: {e}")
            input("\nНажмите Enter для возврата в меню...")
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 0 до 12.")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
    