"""
test_variant_03.py

Вариант 3.
Проверяем корректность реализаций unpack_* и calculate_w_* через тесты.
"""


from typing import Any

import pytest

from Rare.variants.variant_03 import (
    calculate_w_iterative,
    calculate_w_recursive,
    unpack_iterative,
    unpack_recursive,
    unpack_yield_from,
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


#region unpack_* tests

@pytest.mark.parametrize(
    "unpack_func",
    [unpack_recursive, unpack_yield_from, unpack_iterative],
    ids=["unpack_recursive", "unpack_yield_from", "unpack_iterative"]
)
def test_unpack_implementations(unpack_func) -> None:
    """Проверяет, что все реализации unpack_* возвращают одинаковый результат.

    Сравнивает поведение recursive, yield_from и iterative реализаций
    на сложном вложенном примере.
    """
    case = EXPECTED_UNPACK["full_example"]
    assert unpack_func(case["data"]) == case["expected"]


@pytest.mark.parametrize(
    "case_name", 
    list(EXPECTED_UNPACK.keys()), 
    ids=lambda x: f"unpack_case_{x}"
)
def test_unpack_all_cases(case_name: str) -> None:
    """Проверяет все известные кейсы распаковки для каждой реализации.

    Args:
        case_name: Ключ тестового случая из EXPECTED_UNPACK.
    """
    case = EXPECTED_UNPACK[case_name]
    for func in (unpack_recursive, unpack_yield_from, unpack_iterative):
        assert func(case["data"]) == case["expected"]

#endregion


#region calculate_w_* tests

def test_calculate_w_base_cases() -> None:
    """Проверяет базовые значения последовательности w_n.

    w(1) = 0.3 и w(2) = -1.5 должны возвращаться всеми реализациями.
    """
    assert calculate_w_recursive(1) == pytest.approx(0.3)
    assert calculate_w_iterative(1) == pytest.approx(0.3)
    assert calculate_w_recursive(2) == pytest.approx(-1.5)
    assert calculate_w_iterative(2) == pytest.approx(-1.5)


@pytest.mark.parametrize(
    "n", 
    range(1, 11), 
    ids=lambda n: f"w_n={n}")
def test_calculate_w_equal_implementations(n: int) -> None:
    """Проверяет, что рекурсивная и итеративная версии дают одинаковый результат."""
    assert calculate_w_recursive(n) == pytest.approx(
        calculate_w_iterative(n), abs=1e-12
    )


@pytest.mark.parametrize(
    "n, expected",
    list(EXPECTED_W.items()),
    ids=[f"w_n={n}" for n in EXPECTED_W]
)
def test_calculate_w_known_values(n: int, expected: float) -> None:
    """Проверяет корректность вычисления известных значений w_n до n=10.

    Args:
        n: Порядковый номер члена последовательности.
        expected: Ожидаемое значение с высокой точностью.
    """
    assert calculate_w_recursive(n) == pytest.approx(expected, abs=1e-12)
    assert calculate_w_iterative(n) == pytest.approx(expected, abs=1e-12)

#endregion

@pytest.mark.parametrize(
    "func", 
    [calculate_w_recursive, calculate_w_iterative], 
    ids=["recursive", "iterative"]
)
def test_calculate_w_raises_on_invalid_input(func) -> None:
    """Проверка реакции функций calculate_w на некорректные входные данные."""
    with pytest.raises((TypeError, ValueError, RecursionError)):
        func("string")

    with pytest.raises((TypeError, ValueError, RecursionError)):
        func(0)

    with pytest.raises((TypeError, ValueError, RecursionError)):
        func(-5)

#endregion