import pytest
from typing import Type
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17])
])
def test_get_human_age_valid_arguments(
        cat_age: int,
        dog_age: int,
        expected_result: Type[Exception]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (-1, 3, [0, 0]),
    (2, -5, [0, 0]),
    (-3, -2, [0, 0]),
    ("string", 30, TypeError),
    (10, "string", TypeError),
    ("string", "string", TypeError),
])
def test_get_human_age_invalid_arguments(
        cat_age: int,
        dog_age: int,
        expected_result: TypeError
) -> None:
    with pytest.raises(Exception) as e:
        get_human_age(cat_age, dog_age)
        assert e == expected_result
