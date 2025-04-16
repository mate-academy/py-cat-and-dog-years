from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),

        (14, 0, [0, 0]),
        (15, 0, [1, 0]),
        (16, 0, [1, 0]),

        (23, 0, [1, 0]),
        (24, 0, [2, 0]),

        (27, 0, [2, 0]),
        (28, 0, [3, 0]),

        (0, 14, [0, 0]),
        (0, 15, [0, 1]),
        (0, 16, [0, 1]),

        (0, 23, [0, 1]),
        (0, 24, [0, 2]),
        (0, 25, [0, 2]),

        (0, 28, [0, 2]),
        (0, 29, [0, 3]),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_age_is_less_then_zero() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -5)


def test_age_is_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", 14.5)
