import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dogs_age, expected",
    [
        (-10, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (1000, 1000, [246, 197])
    ]
)
def test_get_human_age(
        cat_age: int,
        dogs_age: int,
        expected: list[int]) -> None:
    assert get_human_age(cat_age, dogs_age) == expected
