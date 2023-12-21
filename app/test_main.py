import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (5, 10, [0, 0]),
    (8, 15, [0, 1]),
    (20, 10, [1, 0]),
    (15, 8, [1, 0]),
])
def test_get_human_age_with_expected_values(
    cat_age: int, dog_age: int, expected_result: Any
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected_result


@pytest.mark.parametrize("cat_age, dog_age, expected_error", [
    ([5], 10, TypeError),
    (8, {15}, TypeError),
    ((20,), 10, TypeError),
    (15, [8], TypeError),
    ({"cat": 5}, "dog", TypeError),
    ("cat", {10}, TypeError),
])
def test_get_human_age_with_error_inputs(
    cat_age: Any, dog_age: Any, expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
