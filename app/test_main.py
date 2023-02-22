import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cats_age, dogs_age, expected", [
    (-23, -24, [0, 0]),
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
    (999, 999, [245, 197]),
])
def test_get_human_age(cats_age: int, dogs_age: int, expected: list) -> None:
    assert get_human_age(cats_age, dogs_age) == expected


def test_get_human_age_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("14", 14)
    with pytest.raises(TypeError):
        get_human_age(15, "15")
