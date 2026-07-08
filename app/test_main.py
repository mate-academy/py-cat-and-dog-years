from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197]),
    ],
    ids=str
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
