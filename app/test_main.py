from app.main import get_human_age
import pytest


goals_list = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
]


@pytest.mark.parametrize("cat_age, dog_age, expected", goals_list)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_value_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-8, 5)


def test_get_human_age_big_value() -> None:
    with pytest.raises(ValueError):
        get_human_age(101, 101)


def test_get_human_age_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("100", "100")
