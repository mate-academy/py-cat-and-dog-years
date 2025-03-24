from app.main import get_human_age
import pytest


test_data = [
    (12, 12, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
]

@pytest.mark.parametrize("a,b,expected", test_data)
def test_should_check_correct_output(a, b, expected) -> None:
    assert (get_human_age(a, b) == expected)


