#region Filter - Функция высшего порядка
#       filter(function, iterable) - функция высшего порядка, которая оставляет 
#       только те элементы, на которых функция возвращает True.
#       Возвращает итератор.
#endregion

from typing import Callable, Iterable

lst2 = list(range(-3, 6))   # [-3, -2, -1, 0, 1, 2, 3, 4, 5]

#region Примеры использования Filter

# 1. Императивный подход (Imperative Programming)
odd_imperative = []
for x in lst2:
    if x % 2 != 0:          
        odd_imperative.append(x)

odd_imperative_bit = []
for x in lst2:
    if x & 1:       
        odd_imperative.append(x)


# 2. Декларативный подход (List Comprehension)
odd_comprehension = [x for x in lst2 if x % 2 != 0]
odd_comprehension_bit = [x for x in lst2 if x & 1]


# 3. Функциональный подход (Functional Programming)
odd_filter_mod = list(filter(lambda x: x % 2 != 0, lst2))
odd_filter_bit = list(filter(lambda x: x & 1, lst2)) 


print("Императивный подход:")
print("Нечётные (mod):", odd_imperative)
print("Нечётные (bit):", odd_imperative_bit)

print("Декларативный подход:")
print("Нечётные (mod):", odd_comprehension)
print("Нечётные (bit):", odd_comprehension_bit)

print("Функциональный подход:")
print("Нечётные (mod):", odd_filter_mod)
print("Нечётные (bit):", odd_filter_bit)
#endregion