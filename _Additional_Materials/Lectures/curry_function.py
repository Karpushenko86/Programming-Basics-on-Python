#region Определение Currying (Каррирование):
#       Каррирование (Currying) — это преобразование функции, принимающей 
#       несколько аргументов, в последовательность функций, каждая из которых 
#       принимает ровно один аргумент.
#
#       f(x, y, z)  →  f(x)(y)(z)
#
#       Позволяет частично применять функцию (partial application) и 
#       создавать более гибкие и компонуемые функции.
#endregion


#region Определение Uncurrying (Декаррирование):
#       Декаррирование (Uncurrying) — обратная операция каррирования.
#       Преобразует цепочку функций, каждая из которых принимает один аргумент,
#       обратно в функцию, принимающую несколько аргументов.
#
#       f(x)(y)(z)  →  f(x, y, z)
#endregion


from typing import Any, Callable


Number = int | float


#region Пример Каррирования в Python:

def pow(x: Number, n: Number) -> Number:
    return x ** n


# Каррирование. Классическая реализация (через вложенные функции)
def curry2(f: Callable[[Any, Any], Any]) -> Callable[[Any], Callable[[Any], Any]]:
    def g(x: Any) -> Callable[[Any], Any]:
        def h(y: Any) -> Any:
            return f(x, y)
        return h
    return g


# Каррирование через lambda-выражения
def curry2_lambda(f: Callable[[Any, Any], Any]) -> Callable[[Any], Callable[[Any], Any]]:
    return lambda x: lambda y: f(x, y)


# Применение
pow_curried = curry2(pow)
pow_curried_lambda = curry2_lambda(pow)

print(pow_curried(2)(10))        # 1024
print(pow_curried_lambda(3)(4))  # 81
#endregion


#region Пример Декаррирования в Python:

# Декаррирование. Классическая реализация (через вложенные функции)
def uncurry2(g: Callable[[Any], Callable[[Any], Any]]) -> Callable[[Any, Any], Any]:
    def f(x: Any, y: Any) -> Any:
        return g(x)(y)
    return f


# Декаррирование через lambda-выражения
def uncurry2_lambda(g: Callable[[Any], Callable[[Any], Any]]) -> Callable[[Any, Any], Any]:
    return lambda x, y: g(x)(y)


# Применение
pow_uncurried = uncurry2(pow_curried)
pow_uncurried_lambda = uncurry2_lambda(pow_curried_lambda)

print(pow_uncurried(2, 10))        # 1024
print(pow_uncurried_lambda(3, 4))  # 81
#endregion


#region Преимущества каррирования:
#       • Поддержка частичного применения (partial application)
#       • Улучшает композицию функций (особенно с HOF)
#       • Делает код более декларативным
#       • В Python часто заменяется на functools.partial, но каррирование — фундаментальная концепция ФП
#endregion