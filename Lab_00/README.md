# Лабораторная работа №0 — Первое знакомство с Python

## Задание для самостоятельного выполнения
### Сложность: Rare
- Создайте репозиторий для дисциплины на GitHub.
- Склонируйте его себе на ПК.
- Напишите свою первую программу.
- Ззапустите её.
- Сделайте коммит и пуш.
- Напишите отчёт в README.md. Отчёт должен содержать:
- Задание
    - Описание проделанной работы
    - Консольные команды
    - Скриншоты результатов
    - Ссылки на используемые материалы
- Добавьте для себя в отчёт шпаргалку по работе с git.

## Описание проделанной работы
1. Создал репозиторий на GitHub: [https://github.com/Karpushenko86/Programming-Basics-on-Python](https://github.com/Karpushenko86/Programming-Basics-on-Python "Перейти по ссылке *ТЫК*")

<img src="../_Additional_Materials/Images/Lab_00_00.JPG" width="600" alt="Создание репозитория на компьютер.">

2. Склонировал репозиторий на компьютер.

<img src="../_Additional_Materials/Images/Lab_00_01.JPG" width="600" alt="Клонирование репозитория на компьютер.">

3. Написал файл `hello_world.py` с выводом "Hello, World!".

<img src="../_Additional_Materials/Images/Lab_00_02.JPG" width="600" alt="Написание первой программы для 'Лабораторной работы №0'.">

4. Запустил программу через терминал и сделал скриншот результата выполнения.

<img src="../_Additional_Materials/Images/Lab_00_03.JPG" width="600" alt="Запуск программы через терминал и результат его выполнения.">

5. Закоммитил изменения и отправил на GitHub.

<img src="../_Additional_Materials/Images/Lab_00_04.JPG" width="600" alt="Создание 'commit' и его отправка в репозиторий на GitHub.">

<img src="../_Additional_Materials/Images/Lab_00_05.JPG" width="600" alt="Внесение измениний и исправлений.">

<img src="../_Additional_Materials/Images/Lab_00_06.JPG" width="600" alt="Внесение измениний и исправлений (2).">

6. Оформил данный отчёт в [Lab_00/Rare/README.md](./README.md).

7. Ссылки на используемые материалы.
- [Tutorial: Get started with Visual Studio Code](https://code.visualstudio.com/docs/getstarted/getting-started "Перейти по ссылке *ТЫК*")
- [Working with GitHub in VS Code](https://code.visualstudio.com/docs/sourcecontrol/github)
- [Doka Guide - Язык разметки Markdown](https://doka.guide/tools/markdown/ "Перейти по ссылке *ТЫК*") 
- [GitHub - Демонстрационный пример отчёта в Markdown](https://github.com/still-coding/report_demo "Перейти по ссылке *ТЫК*")
- [Марк Лутц. Изучаем Python. Том 1](https://github.com/Karpushenko86/Programming-Basics-on-Python/blob/main/_Additional_Materials/Books/Learning_Python_Tom_1.pdf "Перейти по ссылке *ТЫК*")
- [Марк Лутц. Изучаем Python. Том 2](https://github.com/Karpushenko86/Programming-Basics-on-Python/blob/main/_Additional_Materials/Books/Learning_Python_Tom_2.pdf "Перейти по ссылке *ТЫК*")
- [Allen Downey. Think Python](https://github.com/Karpushenko86/Programming-Basics-on-Python/blob/main/_Additional_Materials/Books/Think_Python.pdf "Перейти по ссылке *ТЫК*")

## Консольные команды

```bash
# Клонирование
git clone https://github.com/Karpushenko86/Programming-Basics-on-Python.git
cd Programming-Basics-on-Python

# Запуск программы
python hello_world.py

# Git-команды
git add hello_world.py
git commit -m ""
git push origin main