import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_ages() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 5)
    with pytest.raises(ValueError):
        get_human_age(10, -3)


def test_float_ages() -> None:
    with pytest.raises(TypeError):
        get_human_age(5.5, 10.2)
