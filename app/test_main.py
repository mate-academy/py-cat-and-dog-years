import pytest
from app.main import get_human_age

# write your code here
def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_large_ages() -> None:
    assert get_human_age(200, 200) == [46, 37]

def test_low_ages() -> None:
    assert get_human_age(15, 17) == [1, 1]


def test_without_the_remained() -> None:
    assert get_human_age(5, 30) == [0, 3]


def test_non_integer_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "15")
