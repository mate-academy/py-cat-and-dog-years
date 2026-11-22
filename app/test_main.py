import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 15, [1, 1]),
        (14, 14, [0, 0]),
        (24, 24, [2, 2]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (0, 0, [0, 0]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_raises_type_error_for_string() -> None:
    with pytest.raises(TypeError):
        get_human_age("abc", 2)


def test_get_human_age_raises_value_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-2, 15)
