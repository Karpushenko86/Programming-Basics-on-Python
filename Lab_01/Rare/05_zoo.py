#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
print(f"Список животных в зоопарке: \n{zoo}")

result = zoo
for i in range(len(zoo) - 1):
    if zoo[i] == "lion" and zoo[i + 1] == 'kangaroo':
        result.insert(i + 1, 'bear')
print(f"\nПосадите медведя (bear) между львом и кенгуру: \n{result}")


# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
for i in range(len(birds)):
    result.append(birds[i])
print(f"\nДобавьте птиц из списка birds в последние клетки зоопарка: \n{result}")

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
value_to_remove = 'elephant'
while value_to_remove in result:
    result.remove(value_to_remove)
print(f"\nУберите слона и выведите список на консоль: \n{result}")

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
def find_Animal(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i + 1

print(f"\nВыведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark)")
print(f"Номер клетки в которой сидит (lion): {find_Animal(result, 'lion')}")
print(f"Номер клетки в которой сидит (lark): {find_Animal(result, 'lark')}")