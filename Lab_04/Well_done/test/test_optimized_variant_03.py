"""
Тесты для оптимизированных реализаций Варианта 3 (уровень Well-done).

Модуль содержит тесты корректности и сравнения результатов
оптимизированных функций (с мемоизацией и алгоритмическими улучшениями)
с оригинальными реализациями из Rare.
"""

import pytest

# Оригинальные реализации (Rare)
from Rare.variants.variant_03 import (
    calculate_w_recursive,
    calculate_w_iterative,
    unpack_iterative,
    unpack_recursive,
)

# Оптимизированные реализации (Well-done)
from Well_done.variants.optimized_variant_03 import (
    calculate_w_recursive_optimized,
    calculate_w_iterative_optimized,
    unpack_iterative_optimized,
    unpack_recursive_optimized,
)


#region Expected test data

EXPECTED_UNPACK = {
    "task_example": {
        "data": [None, [1, ({2, 3}, {"foo": "bar"})]],
        "expected": [None, 1, 2, 3, "foo", "bar"],
    },
    "full_example": {
        "data": [None, [1, ({2, 3}, {"foo": "bar", "x": [10, 20]})]],
        "expected": [None, 1, 2, 3, "foo", "bar", "x", 10, 20],
    },
    "empty_list": {"data": [], "expected": []},
    "empty_tuple": {"data": (), "expected": []},
    "empty_dict": {"data": {}, "expected": []},
    "empty_set": {"data": set(), "expected": []},
    "flat_list": {"data": [1, 2, 3, 4], "expected": [1, 2, 3, 4]},
    "nested_list": {"data": [1, 2, [3, [4, 5]]], "expected": [1, 2, 3, 4, 5]},
    "simple_dict": {"data": {"a": 1, "b": [2, 3]}, "expected": ["a", 1, "b", 2, 3]},
    "primitive_int": {"data": 42, "expected": [42]},
    "primitive_str": {"data": "hello", "expected": ["hello"]},
    "primitive_none": {"data": None, "expected": [None]},
}


EXPECTED_W = {
    1: 0.3,
    2: -1.5,
    3: -0.028125,
    4: 0.0030375,
    5: -0.000006328125,
    6: -0.0000000014009970617711365,
    7: 0.0000000000000006233684436225331,
    8: -0.00000000000000000000000005870168798063752,
    9: -0.000000000000000000000000000000000000000002341937911968356,
    10: 0.000000000000000000000000000000000000000000000000000000000000000000008366290304169621,
}

#endregion


#region Correctness tests — calculate_w

def test_calculate_w_optimized_base_cases() -> None:
    """Проверяет базовые значения последовательности w_n в оптимизированных функциях.

    Тест гарантирует, что w(1) = 0.3 и w(2) = -1.5 возвращаются корректно.
    """
    assert calculate_w_recursive_optimized(1) == pytest.approx(0.3)
    assert calculate_w_iterative_optimized(1) == pytest.approx(0.3)
    assert calculate_w_recursive_optimized(2) == pytest.approx(-1.5)
    assert calculate_w_iterative_optimized(2) == pytest.approx(-1.5)


@pytest.mark.parametrize("n", range(1, 11), ids=lambda n: f"w_n={n}")
def test_calculate_w_optimized_equals_original(n: int) -> None:
    """Сравнивает результаты оптимизированных и оригинальных реализаций calculate_w_*.

    Args:
        n: Порядковый номер члена последовательности.
    """
    assert calculate_w_recursive_optimized(n) == pytest.approx(
        calculate_w_recursive(n), abs=1e-12
    )
    assert calculate_w_iterative_optimized(n) == pytest.approx(
        calculate_w_iterative(n), abs=1e-12
    )


@pytest.mark.parametrize(
    "n, expected",
    list(EXPECTED_W.items()),
    ids=[f"w_n={n}" for n in EXPECTED_W]
)
def test_calculate_w_optimized_known_values(n: int, expected: float) -> None:
    """Проверяет известные значения последовательности w_n до n=10.

    Args:
        n: Номер члена последовательности.
        expected: Ожидаемое значение с высокой точностью.
    """
    assert calculate_w_recursive_optimized(n) == pytest.approx(expected, abs=1e-12)
    assert calculate_w_iterative_optimized(n) == pytest.approx(expected, abs=1e-12)

#endregion


#region Correctness tests — unpack

@pytest.mark.parametrize(
    "case_name", 
    list(EXPECTED_UNPACK.keys()), 
    ids=lambda x: f"unpack_case_{x}"
)
def test_unpack_optimized_equals_original(case_name: str) -> None:
    """Проверяет корректность оптимизированных unpack-функций
    путём прямого сравнения с оригинальными реализациями.

    Сравниваем:
        - unpack_iterative_optimized  ==  unpack_iterative
        - unpack_recursive_optimized  ==  unpack_recursive
    """
    case = EXPECTED_UNPACK[case_name]
    data = case["data"]
    expected = case["expected"]

    # Сравнение итеративных версий
    assert unpack_iterative_optimized(data) == expected
    assert unpack_iterative(data) == expected

    # Сравнение рекурсивных версий
    assert list(unpack_recursive_optimized(data)) == expected
    assert unpack_recursive(data) == expected

#endregion


#region Performance comparison

@pytest.mark.parametrize("n", [10, 30, 50, 100], ids=lambda n: f"n={n}")
def test_calculate_w_performance_comparison(n: int) -> None:
    """Заготовка для будущих бенчмарк-тестов производительности.

    Проверяет корректность результата перед измерением скорости.
    """
    assert calculate_w_recursive_optimized(n) == pytest.approx(
        calculate_w_iterative_optimized(n), abs=1e-12
    )

#endregion