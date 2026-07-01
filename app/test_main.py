from app.main import get_human_age
import pytest


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
        (100, 100, [21, 17]),
        (24, 28, [2, 2]),
        (24, 29, [2, 3]),
        (1000, 1000, [246, 197]),
        (-5, -1, [0, 0])
    ]
)
def test_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_raises_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)
