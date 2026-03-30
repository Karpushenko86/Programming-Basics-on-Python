"""
Matplotlib Lessons Launcher

Простое консольное меню для запуска уроков по Matplotlib.
Для выполнения лабораторных работ по программированию.

Уроки:
    1 — Быстрый старт
    2 — Основы pyplot
    3 — Настройка элементов графика

Использование:
    python .\Lab_02\_Matplotlib_test\Matplotlib_Lessons\main.py

Зависимости:
    matplotlib
    numpy
"""

import sys
import os

# Автоматически добавляем текущую папку в путь поиска модулей
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Теперь импорты должны работать независимо от того, откуда запустили
from lesson_01 import run as lesson1
from lesson_02 import run as lesson2
from lesson_03 import run as lesson3

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_terminal()

        print("Добро пожаловать в уроки по matplotlib!\n")
        print("  1  — Урок 1. Быстрый старт")
        print("  2  — Урок 2. Основы pyplot")
        print("  3  — Урок 3. Настройка элементов графика")
        print("  0  — Выход\n")

        choice = input("Выберите номер урока: ").strip()

        clear_terminal()

        if choice == '1':
            lesson1()
        elif choice == '2':
            lesson2()
        elif choice == '3':
            lesson3()
        elif choice == '0':
            clear_terminal()
            print("До новых встреч!\n")
            break
        else:
            print("Нажмите Enter...")
            input()


if __name__ == "__main__":
    main()