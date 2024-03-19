import pytest
from app.main import get_human_age, convert_to_human
from typing import List


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "age, first_year, second_year, each_year, expected",
    [
        (15, 15, 9, 4, 1),
        (24, 15, 9, 4, 2),
        (27, 15, 9, 4, 2),
        (28, 15, 9, 5, 2),
        (100, 15, 9, 4, 21),
    ],
)
def test_convert_to_human(
    age: int, first_year: int, second_year: int, each_year: int, expected: int
) -> None:
    result = convert_to_human(age, first_year, second_year, each_year)
    assert result == expected


def test_should_raise_error_correctly() -> None:
    with pytest.raises(TypeError):
     get_human_age("12", [20])
