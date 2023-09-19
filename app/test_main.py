import pytest
from app.main import get_human_age, convert_to_human


def test_convert_to_human_less_than_first_year() -> None:
    assert convert_to_human(10, 15, 9, 4) == 0


def test_convert_to_human_between_first_and_second_year() -> None:
    assert convert_to_human(20, 15, 9, 4) == 1


def test_convert_to_human_more_than_second_year() -> None:
    assert convert_to_human(30, 15, 9, 4) == 2


def test_convert_to_human_more_than_second_year_with_remainder() -> None:
    assert convert_to_human(32, 15, 9, 4) == 2


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
