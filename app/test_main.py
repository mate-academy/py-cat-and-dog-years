import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
])
def test_boundary_values_do_not_change_before_threshold(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_threshold_differs_from_dog_at_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_negative_age_returns_zero() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_large_values() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17]
