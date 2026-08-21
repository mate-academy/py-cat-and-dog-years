from app.main import get_human_age
import pytest


def test_if_array_returned() -> None:
    assert isinstance(get_human_age(3, 3), list)


def test_length_of_array() -> None:
    assert len(get_human_age(3, 3)) == 2


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
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
    ]

)
def test_get_human_age_boundaries(
        cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_cat_age_raises_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 5)


def test_negative_dog_age_raises_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(5, -1)


def test_non_integer_type_raises_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("5", 5)
