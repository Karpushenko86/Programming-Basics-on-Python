#region Map - Функция высшего порядка
#       map(function, iterable) - функция высшего порядка, которая применяет 
#       переданную функцию к каждому элементу итерируемого объекта и возвращает 
#       итератор с результатами.
#endregion

from typing import Callable, Iterable

lst = list(range(6))

#region Примеры использования Map (для разных подходов программирования)

# 1. Императивный подход (Imperative Programming)
lst10 = []
for i in lst:
    lst10.append(i * 10)


# 2. Декларативный подход (List Comprehension)
lst10 = [i * 10 for i in lst]


# 3. Функциональный подход (Functional Programming)
def multiply_by_10(x: int) -> int:
    return x * 10
lst10_map = list(map(multiply_by_10, lst))


# 4. Функциональный подход (Functional Programming) (map + lambda)
lst10_lambda = list(map(lambda x: x * 10, lst))
print(lst10_lambda)
#endregion