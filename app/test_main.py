import pytest
from app.main import get_human_age

@pytest.mark.parametrize("age1, age2, expected", [
    (14, 14, [0, 0]),
    (1, 1, [0, 0]),
    (24, 24, [2, 2]),
    (55, 81, [9, 13]),
    (27, 28, [2, 2]),
    (28, 29, [3, 3]),
    (15, 15, [1, 1])
])
def test_get_human_age(age1, age2, expected):
    assert get_human_age(age1, age2) == expected