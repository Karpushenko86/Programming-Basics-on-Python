#region Определение Decorator (Декоратор):
#       Декоратор — это паттерн проектирования, позволяющий расширять 
#       поведение функции или метода без изменения её исходного кода.
#
#       Декоратор — это функция высшего порядка, которая принимает функцию 
#       и возвращает новую функцию-обёртку (wrapper), добавляющую 
#       дополнительное поведение.
#endregion


#region Generic Decorator в Python:
#       Generic Decorator — это универсальная функция-декоратор, спроектированная так, 
#       чтобы работать с любой функцией, независимо от количества и типа принимаемых ею аргументов.
#       Для этого используются *args и **kwargs.
#endregion


#region Пример Decorator функции в Python:
import time
from typing import Callable, Any
from functools import wraps


#region Шаблон generic-декоратора
def decorator(func: Callable) -> Callable:
    func
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper
#endregion


#region  Декоратор -> Декоратор (с поддержкой docstring) -> Декоратор (с поддержкой параметра) -> Декоратор (с дедуплицированием 'wrapper'):
def timer(
    log_file_name_or_func: str | Callable[[Any], Any] | None = None,
) -> Callable[[Callable], Callable]:
    def create_timer_decorator(log_file: str | None) -> Callable[[Callable], Callable]:
        def decorator(func: Callable) -> Callable:
            @wraps(func)  # Сохраняет имя, docstring и сигнатуру оригинальной функции
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                start = time.perf_counter()
                res = func(*args, **kwargs)
                end = time.perf_counter()
                msg = f"Function {func.__name__} took {(end - start):.7f} s.\n"
                if log_file is None:
                    print(msg)
                else:
                    with open(log_file, "a") as log_file_obj:
                        log_file_obj.write(msg)
                return res
            return wrapper
        return decorator
    
    # Поддержка двух способов использования:
    # @timer          и          @timer("log.log")
    if callable(log_file_name_or_func):
        return create_timer_decorator(None)(log_file_name_or_func)
    else:
        return create_timer_decorator(log_file_name_or_func)
#endregion


#region Пример использования: Таймер без логирования
@timer
def sleep_for(n: int | float) -> None:
    time.sleep(n)
#endregion


#region Пример использования: Таймер с логированием в файл
@timer("log.log")
def n_to_1000(n: int | float) -> int | float:
    """Возводит число n в степень 1000"""
    return n ** 1000
#endregion


#region Как работает Декаратор:
#       При написании:
#           @timer()
#           def func(): ...
#            ↓
#           func = timer()(func)            # timer возвращает wrapper
#
#
#       При использовании с параметром:
#           @timer("log.log")
#           def func(): ...
#            ↓
#           func = timer("log.log")(func)   # timer(...) возвращает функцию-декоратор,
#                                           # которая потом применяется к func  
# 
#
#       В обоих случаях в итоге имя `func` связывается с wrapper'ом,
#       который внутри себя вызывает оригинальную функцию и добавляет поведение.
#endregion


#region Механика Декоратора. Что происходит?
#       Когда интерпретатор Python встречает декоратор, он выполняет следующие действия:
#
#       1. Создаёт объект-функцию n_to_1000.
#       2. Передаёт эту функцию в декоратор timer.
#       3. Заменяет исходное имя на результат работы декоратора.
#
#       В случае с параметром это выглядит так:
#           n_to_1000 = timer("log.log")(n_to_1000)
#
#       В результате:
#       • Имя "n_to_1000" теперь указывает не на оригинальную функцию,
#         а на функцию-обёртку (wrapper).
#       • Wrapper хранит внутри себя ссылку на оригинальную функцию
#         (благодаря замыканию).
#       • При вызове n_to_1000(2) на самом деле вызывается wrapper(2),
#         который измеряет время, логирует результат и затем вызывает
#         оригинальную функцию.
#endregion


if __name__ == "__main__":
    sleep_for(1)
    print(n_to_1000(2))
    
#endregion