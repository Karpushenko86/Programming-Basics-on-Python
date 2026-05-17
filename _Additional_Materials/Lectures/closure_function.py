#region Определение Замыкание (Closure):
#       Замыкание (Closure) - это функция, которая запоминает значения 
#       переменных из внешней области видимости даже после того, 
#       как внешняя функция завершила свою работу.
#endregion

#region Определение Ячейки Замыкания (Closure Cell):
# 		Ячейка Замыкания (Closure Cell) - это специальный объект (контейнер) в куче (Heap), 
# 		который хранит "живую" ссылку на переменную внешней области видимости, 
# 		предотвращая её уничтожение после завершения работы внешней функции.
#endregion

#region Формальные признаки Замыкания (Closure):
#       Замыкание возникает при соблюдении трёх условий:
#       1. Наличие вложенной функции;
#       2. Вложенная функция ссылается на нелокальные переменные (переменные внешней функции);
#       3. Внешняя функция возвращает вложенную функцию.
#endregion


from random import choice
from typing import Any, Callable


#region Пример Closure в Python:
def make_greeter(name: str = "stranger") -> Callable[[], None]:
	def greet() -> str:
		greetings = ("Hi", "Nice to meet you", "Good day")
		return f"{choice(greetings)}, {name}!"
	return greet


# Создаём несколько замыканий
noname = make_greeter()
danila = make_greeter("Danila")
nikita = make_greeter("Nikita")


print(noname())
print(danila())
print(nikita())
#endregion


#region Что происходит в примере:
#       Каждая из функций (noname, danila, nikita) — это замыкание.
#       Они «захватили» и сохранили своё собственное значение переменной name.
#       Даже после завершения работы make_greeter() переменная name продолжает жить
#       внутри каждой из возвращённых функций благодаря Closure Cell.
#endregion