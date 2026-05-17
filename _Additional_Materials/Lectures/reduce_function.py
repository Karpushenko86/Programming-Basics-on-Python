#region Reduce - Функция высшего порядка
#       reduce(function, iterable[, initial]) - сворачивает последовательность 
#       в одно значение, последовательно применяя к ней функцию.
#       Находится в модуле: from functools import reduce
#endregion

from functools import reduce
from typing import Any, Callable, Iterable

lst = list(range(6))   # [0, 1, 2, 3, 4, 5]

#region Примеры использования Reduce

# Сумма элементов
total = reduce(lambda x, y: x + y, lst)                   # 15

# Сумма с начальным значением
total_init = reduce(lambda x, y: x + y, lst, 100)         # 115

# Произведение элементов
product = reduce(lambda x, y: x * y, lst[1:])             # 1*2*3*4*5 = 120

print(total, total_init, product)
#endregion


#region functools реализация Reduce
print(reduce(lambda x, y: x + y, lst))
print(reduce(lambda x, y: x + y, lst, 1))
print(reduce(lambda x, y: x * y, lst[1:], 1))
#endregion


#region Собственная реализация Reduce
def my_reduce(func: Callable[[Any, Any], Any], 
              iterable: Iterable, 
              initial: Any = None) -> Any:
    
    it = iter(iterable)
    
    if initial is None:
        result = next(it)
    else:
        result = initial
    
    for item in it:
        result = func(result, item)
    
    return result

print(my_reduce(lambda x, y: x + y, lst))
print(my_reduce(lambda x, y: x + y, lst, 1))
print(my_reduce(lambda x, y: x * y, lst[1:], 1))
#endregion