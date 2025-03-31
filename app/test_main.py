import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-10, -5, [0, 0]),
        (-76, -53, [0, 0]),
    ])
def test_get_human_age(cat_age: int, dog_age: int,
                       expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected", [
        ("cat", "dog", TypeError),
        (100, [1, 0, 0], TypeError),
        ({"cat": 100}, {"dog": 100}, TypeError),
    ])
def test_get_human_age_type_error(cat_age: int, dog_age: int,
                                  expected: list[int]) -> None:
    with pytest.raises(Exception):
        assert get_human_age(cat_age, dog_age) == TypeError
