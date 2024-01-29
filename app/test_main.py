import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dogs_age, expected",
    [
        (-5, -7, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(
        cat_age: int,
        dogs_age: int,
        expected: list[int]) -> None:
    assert get_human_age(cat_age, dogs_age) == expected


def test_get_human_age_invalid() -> None:
    with pytest.raises(TypeError):
        get_human_age("seven", "two")
