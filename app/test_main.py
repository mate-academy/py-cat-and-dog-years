import pytest

from app.main import get_human_age


test_cases = [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
]


@pytest.mark.parametrize("cat_age, dog_age, expected_result", test_cases)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_no_one_or_all_values() -> None:
    try:
        assert get_human_age() == [0, 0]
    except TypeError:
        print("function take 2 parameters")


def test_another_type() -> None:
    try:
        assert get_human_age("13", "10") == [0, 0]
    except TypeError:
        print("False type")
