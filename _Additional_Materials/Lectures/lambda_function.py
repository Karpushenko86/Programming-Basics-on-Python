#region Определение Lambda (Анонимные функции):
#       Lambda-функции - это анонимные (безымянные) функции, 
#       которые определяются в одну строку с помощью ключевого слова lambda.
#
#       Общая форма:
#           lambda параметр1, параметр2, ..., параметрN: выражение
#
#       Важные особенности:
#       • lambda - это выражение (expression), а не инструкция (statement)
#       • Тело lambda может содержать только одно выражение
#       • Не может содержать блоков кода, циклов, условий (if/else) и return
#       • Возвращает результат выражения автоматически
#endregion


from typing import Callable, Any


#region Примеры Lambda-функций:

def sqr_classic(x: int) -> int:
    """Обычная именованная функция"""
    return x * x


# Эквивалентная lambda-функция
sqr_lambda = lambda x: x * x


print(sqr_classic(3))   # 9
print(sqr_lambda(3))    # 9
#endregion


#region Lambda в структурах данных (списках, словарях и т.д.):

fun_lst: list[Callable[[int], int]] = [
    lambda x: 1,                    # константная функция
    lambda x: x * x,                # квадрат
    lambda x: x * x * x,            # куб
    lambda x: x ** 4,               # четвёртая степень
]

# Использование
print(fun_lst[0](5))   # 1
print(fun_lst[1](3))   # 9
print(fun_lst[2](3))   # 27
print(fun_lst[3](3))   # 81
#endregion


#region Пример с циклом:

for i, f in enumerate(fun_lst):
    if i == 0:
        print(f"fun_lst[{i}] = {f(10)}")   # всегда 1
    else:
        print(f"fun_lst[{i}] = {f(3)}")
#endregion


#region Типичные сценарии использования lambda:
#       • Короткие функции для map(), filter(), sorted(), min(), max()
#       • Ключи сортировки (key=...)
#       • Обработчики событий и callback'и
#       • Когда функция нужна в одном месте и не требуется повторное использование
#endregion