"""
benchmark.py

Бенчмарк производительности для функций относительно исходных вариатов решения.
Сравнивает неоптимизированные и оптимизированные реализации unpack_* и calculate_w_*.
"""

from typing import Any, Callable, TypeVar, ParamSpec
from functools import wraps
from time import perf_counter

from Lab_04.Rare.variants.variant_03 import (
    calculate_w_iterative as calculate_w_iterative_original,
    calculate_w_recursive as calculate_w_recursive_original,
    unpack_iterative as unpack_iterative_original,
    unpack_recursive as unpack_recursive_original,
)
from Lab_04.Well_done.variants.optimized_variant_03 import (
    calculate_w_iterative_optimized,
    calculate_w_recursive_optimized,
    unpack_iterative_optimized,
    unpack_recursive_optimized,
)


T = TypeVar("T")
P = ParamSpec("P")
width: int = 70


def timer(func: Callable[P, T]) -> Callable[P, T]:
    """Декоратор для замера времени выполнения функции."""
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        """Обёртка с замером времени."""
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = perf_counter() - start
            print(f"{func.__name__:<35} = {duration:9.6f} сек".center(width))

    return wrapper


# ========================== БЕНЧМАРК ==============================

def run_benchmark() -> None:
    """Запускает все замеры производительности с красивым оформлением."""

    double_line = "=" * width

    print("\n" + double_line)
    print("BENCHMARK START".center(width))
    print(double_line + "\n")


    # === Усложнённые тестовые данные ===
    small_n = 5
    large_n = 10    # Не рекомендуется использовать значение больше 30 (время выполнения > 1.5 сек)

    test_data: Any = [
        None,
        42,
        "hello world",
        [1, 2, 3, [4, 5, [6, 7, {"a": 1, "b": [8, 9, 10]}]]],
        {
            "user": {
                "id": 12345,
                "name": "Иван Иванов",
                "contacts": {
                    "email": "test@example.com",
                    "phones": ["+79001234567", "+79007654321"],
                    "social": {"tg": "@username", "vk": None}
                }
            },
            "orders": [
                {"id": 1, "items": [{"name": "book", "price": 999.99}, {"name": "pen", "price": 49.5}]},
                {"id": 2, "items": []}
            ],
            "tags": {"python", "benchmark", "nesting", None}
        },
        (True, False, None, 3.14159, {"nested_tuple": (1, 2, [3, 4])}),
        [[[[[1, 2, 3]]]]],
    ] * small_n

    # === Unpack functions ===
    print(f"UNPACK FUNCTIONS (n = {small_n})".center(width, '-'))

    timer(unpack_iterative_original)(test_data)
    timer(unpack_iterative_optimized)(test_data)
    timer(unpack_recursive_original)(test_data)
    timer(unpack_recursive_optimized)(test_data)

    print()

    # === calculate_w functions ===
    title = (f"CALCULATE_W FUNCTIONS (n = {large_n})".center(width, '-'))
    print(title.center(width))

    timer(calculate_w_iterative_original)(large_n)
    timer(calculate_w_iterative_optimized)(large_n)
    timer(calculate_w_recursive_original)(large_n)
    timer(calculate_w_recursive_optimized)(large_n)

    print("\n" + double_line)


if __name__ == "__main__":
    run_benchmark()