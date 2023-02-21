import pytest

from app.main import get_human_age


@pytest.mark.parametrize("age1, age2, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_get_human_age(age1: int, age2: int, expected: list) -> None:
    assert get_human_age(age1, age2) == expected
