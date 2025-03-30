import pytest
from app.main import get_human_age

test_data = [
    (0, 0, [0, 0]),
    (-1, -5, [0, 0]),
    (5, -1, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (100, 100, [21, 17]),
    (150, 120, [33, 21]),
]


@pytest.mark.parametrize("cat_age, dog_age, expected", test_data)
def test_get_human_age_parametrized(cat_age: int,
                                    dog_age: int,
                                    expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_age() -> None:
    assert get_human_age(-5, -10) == [0, 0]
    assert get_human_age(-1, 10) == [0, 0]
    assert get_human_age(10, -1) == [0, 0]
