#region Определение Функция высшего порядка (Higher-Order Function):
#       Функция высшего порядка (Higher-Order Function) - это функция, 
#       которая принимает одну или несколько функций в качестве аргументов 
#       И/ИЛИ возвращает другую функцию в качестве результата.
#
#       Функции высшего порядка — ключевой элемент функционального программирования,
#       позволяющий работать с функциями как с обычными данными.
#endregion


#region Свойства Функция высшего порядка (Higher-Order Function):
#       • Сохранять функцию в переменной
#       • Передавать функцию в качестве аргумента в другую функцию
#       • Возвращать функцию из другой функции
#endregion


from typing import Callable


Number = int | float
NumberFunc = Callable[[Number], Number]


#region Пример High Order Function в Python:
def sqr(x: Number) -> Number:
	return x * x


def plus2(x: Number) -> Number:
	return x + 2


def compose(f: NumberFunc, g: NumberFunc):
	def composition(x: Number) -> Number:
		return f(g(x))
	return composition


# Использование
c = compose(sqr, plus2)

print (c(3))	# (3 + 2)² = 25

#endregion


#region Что происходит в примере:
#       Функция compose — это функция высшего порядка, потому что:
#       1. Принимает две функции (f и g) в качестве аргументов.
#       2. Возвращает новую функцию (composition).
#
#       c = compose(sqr, plus2)  →  c(x) = sqr(plus2(x))
#endregion