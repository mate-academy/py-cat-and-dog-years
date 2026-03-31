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
        (100, 100, [21, 17])
    ]
)
def test_eval(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("a", 0)


def test_dog_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age(0, "a")


def test_negative_cat_input() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 0)


def test_negative_dog_input() -> None:
    with pytest.raises(ValueError):
        get_human_age(0, -1)


def test_large_cat_input() -> None:
    with pytest.raises(ValueError):
        get_human_age(101, 0)


def test_large_dog_input() -> None:
    with pytest.raises(ValueError):
        get_human_age(0, 101)
